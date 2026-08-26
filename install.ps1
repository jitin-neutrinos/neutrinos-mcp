#Requires -Version 5.1
# Windows installer, mirrors install.sh (macOS/Linux). See README "Distribution and auto-update".
$ErrorActionPreference = "Stop"

Write-Host "Installing neutrinos-mcp for Claude Code..." -ForegroundColor Cyan

$InstallDir = Join-Path $HOME ".neutrinos-mcp"
$RepoUrl    = "https://github.com/jitin-neutrinos/neutrinos-mcp.git"

if (Test-Path $InstallDir) {
    Write-Host "Updating existing repository..."
    Push-Location $InstallDir
    git pull origin master
    Pop-Location
} else {
    Write-Host "Cloning repository..."
    git clone $RepoUrl $InstallDir
}

Set-Location $InstallDir

Write-Host "Setting up Python virtual environment..."
python -m venv .venv

Write-Host "Installing package and dependencies..."
# `python -m pip`, never a bare `pip`/`pip.exe` invocation: some locked-down
# corporate machines block the pip.exe launcher via execution policy while
# still allowing python.exe itself (confirmed on this project's own dev
# machine) -- `-m pip` runs pip as a module inside the already-allowed
# interpreter instead of spawning the separate wrapper executable.
& ".\.venv\Scripts\python.exe" -m pip install -e . --quiet

New-Item -ItemType Directory -Force -Path data | Out-Null

Write-Host "Fetching the latest pre-built database..."
if (Get-Command gh -ErrorAction SilentlyContinue) {
    gh release download -R jitin-neutrinos/neutrinos-mcp -p "neutrinos.db" -D data --clobber
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Could not download DB via gh. It will download automatically on first use." -ForegroundColor Yellow
    }
} else {
    Write-Host "GitHub CLI ('gh') not found. The database will download automatically the first time Claude Code queries the tool." -ForegroundColor Yellow
}

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
    Write-Host "Successfully registered! Start a new Claude Code session to pick up the 'neutrinos-docs' tools." -ForegroundColor Green
} else {
    Write-Host "Claude Code CLI ('claude') not found in PATH." -ForegroundColor Yellow
    Write-Host "Register manually:"
    Write-Host "  claude mcp add neutrinos-docs --scope user -- `"$PythonExe`" -m neutrinos_mcp.server"
}
