#!/usr/bin/env bash
#
# build_pdf.sh - Compiles a LaTeX (.tex) resume file to PDF using tectonic.
#

set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/build_pdf.sh <path-to-tex-file>"
    echo "Example: ./scripts/build_pdf.sh master/resume.tex"
    exit 1
fi

TEX_FILE="$1"

if [ ! -f "$TEX_FILE" ]; then
    echo "❌ Error: File not found: $TEX_FILE"
    exit 1
fi

if ! command -v tectonic &> /dev/null; then
    echo "❌ Error: tectonic LaTeX compiler is not installed or not in PATH."
    exit 1
fi

DIR="$(dirname "$TEX_FILE")"
BASE="$(basename "$TEX_FILE")"

echo "⚡ Compiling $TEX_FILE with Tectonic..."
(cd "$DIR" && tectonic "$BASE")
echo "✅ Compilation successful! PDF generated in $DIR/"
