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

echo "🔌 Registering with Claude Code..."
if command -v claude &> /dev/null; then
    claude mcp add neutrinos-docs -- "$INSTALL_DIR/.venv/bin/neutrinos-mcp" --transport stdio
    echo "✅ Successfully registered! You can now use the 'neutrinos-docs' tool in Claude Code."
else
    echo "⚠️  Claude Code CLI ('claude') not found in PATH."
    echo "Please ensure Claude Code is installed or register the MCP manually:"
    echo "claude mcp add neutrinos-docs -- $INSTALL_DIR/.venv/bin/neutrinos-mcp --transport stdio"
fi
