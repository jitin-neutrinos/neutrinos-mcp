#!/bin/bash
# macOS/Linux installer. See README "Distribution and auto-update" and
# implementation_plan.md AD-13 for the Windows equivalent and the rationale
# below.
#
# Transactional by design, not just "set -e and hope":
#   - A completion marker (.install_complete) distinguishes a genuinely
#     finished prior install from a partial one left by an interrupted or
#     failed run. Only the marker's presence makes "directory exists" mean
#     "safe to `git pull` and update in place" -- this is exactly the bug
#     that broke a real install attempt: a stale directory from an earlier
#     failed run made `git clone` fail with "already exists", and nothing
#     cleaned it up first.
#   - `trap cleanup EXIT` guarantees the cleanup runs on any exit path
#     (error, Ctrl+C, or normal completion) -- see Sipos, "How Exit Traps
#     Can Make Your Bash Scripts Way More Robust", and the pattern used by
#     rustup/deno's own installers.
#   - Cleanup only removes what THIS run created or judged unsafe to reuse
#     (a fresh clone, or a stale partial one it wiped first) -- it never
#     deletes a previously-working install just because a later step (DB
#     fetch, `claude mcp add`) failed. Those two steps are deliberately
#     outside `set -e`'s reach (see the `set +e` fence below) because a
#     working local install with no DB yet, or with registration still to
#     be done by hand, is not "failed" -- it can recover on the next run.
set -euo pipefail

INSTALL_DIR="$HOME/.neutrinos-mcp"
REPO_URL="https://github.com/jitin-neutrinos/neutrinos-mcp.git"
MARKER="$INSTALL_DIR/.install_complete"
FRESH_INSTALL=false

cleanup_on_failure() {
    local exit_code=$?
    if [ "$exit_code" -ne 0 ] && [ "$FRESH_INSTALL" = true ]; then
        echo "⚠️  Install failed (exit $exit_code) -- removing partial install at $INSTALL_DIR" >&2
        cd "$HOME"
        rm -rf "$INSTALL_DIR"
    fi
    exit "$exit_code"
}
trap cleanup_on_failure EXIT

echo "🚀 Installing neutrinos-mcp for Claude Code..."

if [ -d "$INSTALL_DIR" ] && [ -f "$MARKER" ]; then
    echo "🔄 Updating existing installation..."
    cd "$INSTALL_DIR"
    git pull origin master
else
    if [ -d "$INSTALL_DIR" ]; then
        echo "⚠️  Found an incomplete previous install at $INSTALL_DIR -- removing it before retrying."
        rm -rf "$INSTALL_DIR"
    fi
    FRESH_INSTALL=true
    echo "📥 Cloning repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

echo "🐍 Setting up Python virtual environment..."
python3 -m venv .venv

echo "📦 Installing package and dependencies..."
./.venv/bin/python -m pip install -e . --quiet

mkdir -p data

echo "🗄️  Fetching the latest pre-built database..."
# From here on, a failure must NOT roll back the install: the venv and
# package are already good, and the DB downloads automatically on first
# server use regardless. `set +e` fences this off from the trap's judgment.
set +e
if command -v gh &> /dev/null; then
    gh release download -R jitin-neutrinos/neutrinos-mcp -p "neutrinos.db" -D data/ --clobber
    if [ $? -ne 0 ]; then
        echo "⚠️  Could not download DB via gh. It will download automatically on first use."
    fi
else
    echo "⚠️  GitHub CLI ('gh') not found. The database will be downloaded automatically the first time Claude Code queries the tool."
fi
set -e

# Mark complete before registration: a working, importable install with its
# data in place is "installed" even if `claude mcp add` below fails or
# `claude` isn't on PATH -- a re-run should update in place, not wipe and
# rebuild a perfectly good venv over a missing CLI.
touch "$MARKER"

echo "🔌 Registering with Claude Code..."
set +e
if command -v claude &> /dev/null; then
    # --scope user: available in every project, not just wherever this was run from.
    claude mcp add neutrinos-docs --scope user -- "$INSTALL_DIR/.venv/bin/neutrinos-mcp"
    if [ $? -eq 0 ]; then
        echo "✅ Successfully registered! Start a new Claude Code session to pick up the 'neutrinos-docs' tools."
    else
        echo "⚠️  Registration failed. Register manually:"
        echo "claude mcp add neutrinos-docs --scope user -- $INSTALL_DIR/.venv/bin/neutrinos-mcp"
    fi
else
    echo "⚠️  Claude Code CLI ('claude') not found in PATH."
    echo "Register manually once it's installed:"
    echo "claude mcp add neutrinos-docs --scope user -- $INSTALL_DIR/.venv/bin/neutrinos-mcp"
fi
set -e
