#!/usr/bin/env python3
"""
watch_inbox.py
Lightweight inbox monitor.
Watches the inbox/ folder for newly dropped .tex and .pdf files
and notifies you or launches the intake assistant automatically.
"""

import time
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INBOX_DIR = BASE_DIR / "inbox"
ARCHIVE_SCRIPT = BASE_DIR / "scripts" / "archive.py"

def check_inbox():
    tex_files = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() == ".tex"]
    pdf_files = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"]
    return tex_files, pdf_files

def main():
    print(f"👀 Monitoring inbox folder at: {INBOX_DIR}")
    print("Drop your .tex and .pdf files into inbox/ to archive them.")
    print("Press Ctrl+C to stop.")

    processed_pairs = set()

    try:
        while True:
            tex_files, pdf_files = check_inbox()
            if tex_files and pdf_files:
                tex = tex_files[0]
                pdf = pdf_files[0]
                pair_key = f"{tex.name}:{pdf.name}:{tex.stat().st_mtime}:{pdf.stat().st_mtime}"
                
                if pair_key not in processed_pairs:
                    print(f"\n🔔 New resume pair detected in inbox/!")
                    print(f"   - LaTeX: {tex.name}")
                    print(f"   - PDF:   {pdf.name}")
                    print("\nStarting intake assistant...\n")
                    subprocess.run([sys.executable, str(ARCHIVE_SCRIPT)])
                    processed_pairs.add(pair_key)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped inbox watcher.")

if __name__ == "__main__":
    main()
