#!/usr/bin/env bash
#
# archive.sh - Quick CLI intake assistant for Resume versions & master updates.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_EXEC="python3"

if ! command -v "$PYTHON_EXEC" &> /dev/null; then
    echo "❌ Error: python3 is not found in your PATH."
    exit 1
fi

"$PYTHON_EXEC" "$SCRIPT_DIR/scripts/archive.py" "$@"
