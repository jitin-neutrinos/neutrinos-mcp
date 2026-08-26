#!/bin/bash
set -e

echo "🚀 Installing neutrinos-mcp for Claude Code..."

# Set paths
INSTALL_DIR="$HOME/.neutrinos-mcp"
REPO_URL="https://github.com/jitin-neutrinos/neutrinos-mcp.git"

# Clone or update repository
if [ -d "$INSTALL_DIR" ]; then
    echo "🔄 Updating existing repository..."
    cd "$INSTALL_DIR"
    git pull origin main
else
    echo "📥 Cloning repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# Set up virtual environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
echo "📦 Installing package and dependencies..."
pip install -e .

# Optional: Ensure data directory exists
mkdir -p data

echo "🗄️  Fetching the latest pre-built database..."
# Use GitHub CLI if available (handles private repo auth), otherwise fallback to curl
if command -v gh &> /dev/null; then
    gh release download -R jitin-neutrinos/neutrinos-mcp -p "neutrinos.db" -D data/ --clobber || echo "⚠️ Could not download DB via gh. It will download automatically on first use."
else
    echo "⚠️ GitHub CLI ('gh') not found. The database will be downloaded automatically the first time Claude Code queries the tool."
fi

echo "🔌 Registering with Claude Code..."
if command -v claude &> /dev/null; then
    # --scope user: available in every project, not just wherever this was run from.
    claude mcp add neutrinos-docs --scope user -- "$INSTALL_DIR/.venv/bin/neutrinos-mcp"
    echo "✅ Successfully registered! You can now use the 'neutrinos-docs' tool in Claude Code."
else
    echo "⚠️  Claude Code CLI ('claude') not found in PATH."
    echo "Please ensure Claude Code is installed or register the MCP manually:"
    echo "claude mcp add neutrinos-docs --scope user -- $INSTALL_DIR/.venv/bin/neutrinos-mcp"
fi
