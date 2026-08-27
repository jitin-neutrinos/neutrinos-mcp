#Requires -Version 5.1
# Windows installer, mirrors install.sh (macOS/Linux). See README "Distribution
# and auto-update" and implementation_plan.md AD-13.
#
# Transactional by design. Two things Windows PowerShell needs that a naive
# `$ErrorActionPreference = "Stop"` script doesn't give you for free:
#
#   1. `$ErrorActionPreference = "Stop"` only governs cmdlets -- a failing
#      native command (git.exe, python.exe) does NOT throw and does NOT stop
#      the script; it just sets $LASTEXITCODE and execution continues past
#      it. Every native call below is followed by an explicit check that
#      throws on failure, which is what actually gets the `catch`/`finally`
#      below to run. (This exact class of bug is a filed, confirmed issue
#      against Claude Code's own install.ps1: it printed "Installation
#      complete!" after a step had already failed --
#      github.com/anthropics/claude-code/issues/26880.)
#   2. A completion marker (.install_complete) distinguishes a genuinely
#      finished prior install from a partial one left by an interrupted or
#      failed run. This is the exact bug that broke a real install attempt
#      here: a stale directory from an earlier failed run made `git clone`
#      fail with "already exists", and nothing cleaned it up first. Only the
#      marker's presence means "safe to `git pull` and update in place";
#      otherwise the directory is wiped and re-cloned fresh.
#
# Cleanup on failure only removes what THIS run created or judged unsafe to
# reuse (a fresh clone, or a stale partial one it wiped first) -- it never
# deletes a previously-working install just because the DB fetch or
# `claude mcp add` failed afterward. Those two are deliberately non-fatal
# (checked, warned, not thrown) because a working local install that hasn't
# fetched its DB yet, or still needs manual registration, is not "failed" --
# it recovers on the next run or the server's own auto-update.

$ErrorActionPreference = "Stop"

function Assert-LastExitCode([string]$What) {
    if ($LASTEXITCODE -ne 0) {
        throw "$What failed (exit code $LASTEXITCODE)"
    }
}

$InstallDir   = Join-Path $HOME ".neutrinos-mcp"
$RepoUrl      = "https://github.com/jitin-neutrinos/neutrinos-mcp.git"
$Marker       = Join-Path $InstallDir ".install_complete"
$FreshInstall = $false
$Succeeded    = $false

try {
    Write-Host "Installing neutrinos-mcp for Claude Code..." -ForegroundColor Cyan

    if ((Test-Path $InstallDir) -and (Test-Path $Marker)) {
        Write-Host "Updating existing installation..."
        Push-Location $InstallDir
        git pull origin master
        Assert-LastExitCode "git pull"
        Pop-Location
    } else {
        if (Test-Path $InstallDir) {
            Write-Host "Found an incomplete previous install at $InstallDir -- removing it before retrying." -ForegroundColor Yellow
            Remove-Item -Recurse -Force $InstallDir
        }
        $FreshInstall = $true
        Write-Host "Cloning repository..."
        git clone $RepoUrl $InstallDir
        Assert-LastExitCode "git clone"
    }

    Set-Location $InstallDir

    Write-Host "Setting up Python virtual environment..."
    python -m venv .venv
    Assert-LastExitCode "python -m venv"

    Write-Host "Installing package and dependencies..."
    # `python -m pip`, never a bare `pip`/`pip.exe` invocation: some locked-down
    # corporate machines block the pip.exe launcher via execution policy while
    # still allowing python.exe itself (confirmed on this project's own dev
    # machine) -- `-m pip` runs pip as a module inside the already-allowed
    # interpreter instead of spawning the separate wrapper executable.
    #
    # Live per-package progress rather than --quiet silence. pip has no
    # built-in "X of Y packages" mode -- getting an exact total ahead of time
    # means a `--dry-run --report` pass first, which costs roughly as much
    # time as the real install (measured: +67s on this project's 93-package
    # tree, almost entirely PyPI metadata resolution) just to know a number.
    # Not worth doubling install time for a cosmetic total, so this shows a
    # running count with no fixed denominator instead -- free, and still
    # answers "which dependency is installing now" and "is it making
    # progress" live. Deliberately NOT `2>&1` here: in Windows PowerShell 5.1,
    # merging a native command's stderr into the pipeline wraps every stderr
    # line as a terminating ErrorRecord under $ErrorActionPreference = "Stop"
    # (confirmed directly -- it is what made a successful `git clone` look
    # like a failure while testing this very install flow). pip's progress
    # lines go to stdout already, and unredirected stderr still prints
    # straight to the console on its own, so nothing is lost by leaving it be.
    $pkgCount = 0
    & ".\.venv\Scripts\python.exe" -u -m pip install -e . | ForEach-Object {
        if ($_ -match '^Collecting\s+([A-Za-z0-9_.\-]+)') {
            $pkgCount++
            Write-Host ("`r  [{0}] Installing: {1,-40}" -f $pkgCount, $matches[1]) -NoNewline
        } elseif ($_ -match '^Installing collected packages:') {
            # Resolution is done; pip now downloads/unpacks wheels with no
            # further per-package output until the very end -- this can be
            # the LONGEST silent stretch (large wheels like onnxruntime), so
            # without this line the display looks hung right when a fresh
            # machine with no wheel cache needs reassurance most.
            Write-Host "`n  Downloading and unpacking $pkgCount packages, this can take a while..."
        } elseif ($_ -match '^Successfully installed') {
            Write-Host "  Done: $_"
        }
    }
    Write-Host ""
    Assert-LastExitCode "pip install -e ."

    New-Item -ItemType Directory -Force -Path data | Out-Null

    Write-Host "Fetching the latest pre-built database..."
    # From here on, a failure must NOT roll back the install: the venv and
    # package are already good, and the DB downloads automatically on first
    # server use regardless (server._check_for_db_updates_once, AD-13).
    if (Get-Command gh -ErrorAction SilentlyContinue) {
        gh release download -R jitin-neutrinos/neutrinos-mcp -p "neutrinos.db" -D data --clobber
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Could not download DB via gh. It will download automatically on first use." -ForegroundColor Yellow
        }
    } else {
        Write-Host "GitHub CLI ('gh') not found. The database will download automatically the first time Claude Code queries the tool." -ForegroundColor Yellow
    }

    # Mark complete before registration: a working, importable install with
    # its data in place is "installed" even if `claude mcp add` below fails
    # or `claude` isn't on PATH -- a re-run should update in place, not wipe
    # and rebuild a perfectly good venv over a missing CLI.
    New-Item -ItemType File -Force -Path $Marker | Out-Null

    Write-Host "Registering with Claude Code..."
    # Deliberately NOT `.venv\Scripts\neutrinos-mcp.exe`: pip's generated console-
    # script launcher is a separate small executable, and the same class of
    # execution policy that blocks pip.exe on a locked-down machine blocks THAT
    # launcher too (confirmed: python.exe -m pip works, but the .exe it produces
    # fails with the identical "Access is denied" as pip.exe itself). Invoking
    # python.exe -m neutrinos_mcp.server directly never spawns a second
    # executable, so it isn't subject to that block -- and no PYTHONPATH is
    # needed here since `pip install -e .` above already made the package
    # importable to this venv's interpreter.
    $PythonExe = Join-Path $InstallDir ".venv\Scripts\python.exe"
    if (Get-Command claude -ErrorAction SilentlyContinue) {
        claude mcp add neutrinos-docs --scope user -- $PythonExe -m neutrinos_mcp.server
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Successfully registered! Start a new Claude Code session to pick up the 'neutrinos-docs' tools." -ForegroundColor Green
        } else {
            Write-Host "Registration failed. Register manually:" -ForegroundColor Yellow
            Write-Host "  claude mcp add neutrinos-docs --scope user -- `"$PythonExe`" -m neutrinos_mcp.server"
        }
    } else {
        Write-Host "Claude Code CLI ('claude') not found in PATH." -ForegroundColor Yellow
        Write-Host "Register manually once it's installed:"
        Write-Host "  claude mcp add neutrinos-docs --scope user -- `"$PythonExe`" -m neutrinos_mcp.server"
    }

    Write-Host "Registering with Claude Desktop / Cowork..."
    # Cowork (the agentic-work tab in the Claude Desktop app) is not a
    # separate app and has no config of its own -- it shares
    # claude_desktop_config.json, and Desktop's own SDK layer bridges servers
    # registered there into the sandboxed Cowork VM automatically. A server
    # added directly inside a Cowork session, by contrast, cannot connect
    # (the VM is isolated from the host) -- this is why the registration
    # target here is Desktop's config file, not something inside Cowork
    # itself. Config path per Anthropic's docs: %APPDATA%\Claude on Windows.
    $DesktopConfig = Join-Path $env:APPDATA "Claude\claude_desktop_config.json"
    New-Item -ItemType Directory -Force -Path (Split-Path $DesktopConfig) | Out-Null

    # Merged with Python, not overwritten or hand-edited: this file commonly
    # already has the user's OTHER MCP servers in it, and a naive overwrite
    # would silently delete them. A temp .py file rather than `python -c`
    # here -- reliably quoting a multi-line script through PowerShell's
    # own argument parsing is its own source of subtle breakage.
    $mergeScript = @'
import json, sys
from pathlib import Path

config_path, cmd, args = Path(sys.argv[1]), sys.argv[2], sys.argv[3:]
config = {}
if config_path.exists():
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"  Existing {config_path} is not valid JSON -- leaving it untouched.")
        sys.exit(1)

config.setdefault("mcpServers", {})["neutrinos-docs"] = {"command": cmd, "args": args}
config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
print(f"  Registered in {config_path}")
'@
    $tmpScript = Join-Path $env:TEMP "neutrinos_mcp_desktop_merge.py"
    Set-Content -Path $tmpScript -Value $mergeScript -Encoding utf8

    & $PythonExe $tmpScript $DesktopConfig $PythonExe "-m" "neutrinos_mcp.server"
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Registered with Claude Desktop (Cowork picks this up automatically -- it shares this config)." -ForegroundColor Green
        Write-Host "Restart Claude Desktop for the change to take effect."
    } else {
        Write-Host "Could not update Claude Desktop's config. Claude Code registration above is unaffected." -ForegroundColor Yellow
    }
    Remove-Item $tmpScript -ErrorAction SilentlyContinue

    $Succeeded = $true
}
finally {
    if (-not $Succeeded -and $FreshInstall -and (Test-Path $InstallDir)) {
        Write-Host "Install failed -- removing partial install at $InstallDir" -ForegroundColor Red
        Set-Location $HOME  # can't remove a directory that's the current location
        Remove-Item -Recurse -Force $InstallDir -ErrorAction SilentlyContinue
    }
}

if (-not $Succeeded) {
    exit 1
}
