Write-Host "🚀 Installing neutrinos-mcp for Claude Code..."

$INSTALL_DIR = "$HOME\.neutrinos-mcp"
$REPO_URL = "https://github.com/jitin-neutrinos/neutrinos-mcp.git"

if (Test-Path "$INSTALL_DIR") {
    Write-Host "🔄 Updating existing repository..."
    Set-Location -Path "$INSTALL_DIR"
    git pull origin main
} else {
    Write-Host "📥 Cloning repository..."
    git clone $REPO_URL $INSTALL_DIR
    Set-Location -Path "$INSTALL_DIR"
}

Write-Host "🐍 Setting up Python virtual environment..."
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

Write-Host "📦 Installing package and dependencies..."
pip install -e .

New-Item -ItemType Directory -Force -Path data | Out-Null

Write-Host "🗄️ Fetching the latest pre-built database..."
if (Get-Command gh -ErrorAction SilentlyContinue) {
    gh release download -R jitin-neutrinos/neutrinos-mcp -p "neutrinos.db" -D data/ --clobber
} else {
    Write-Host "⚠️ GitHub CLI ('gh') not found. DB will be downloaded automatically on first use."
}

Write-Host "🔌 Registering with Claude Code..."
if (Get-Command claude -ErrorAction SilentlyContinue) {
    claude mcp add neutrinos-docs -- "$INSTALL_DIR\.venv\Scripts\neutrinos-mcp.exe" --transport stdio
    Write-Host "✅ Successfully registered! You can now use the 'neutrinos-docs' tool in Claude Code."
} else {
    Write-Host "⚠️ Claude Code CLI ('claude') not found in PATH."
    Write-Host "Please run manually: claude mcp add neutrinos-docs -- $INSTALL_DIR\.venv\Scripts\neutrinos-mcp.exe --transport stdio"
}
