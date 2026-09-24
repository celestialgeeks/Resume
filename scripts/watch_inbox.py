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
            if tex_files or pdf_files:
                detected_names = [f.name for f in tex_files + pdf_files]
                mtimes = [str(f.stat().st_mtime) for f in tex_files + pdf_files]
                batch_key = ":".join(detected_names + mtimes)
                
                if batch_key not in processed_pairs:
                    print(f"\n🔔 New resume file(s) detected in inbox/!")
                    for f in tex_files:
                        print(f"   - LaTeX: {f.name}")
                    for f in pdf_files:
                        print(f"   - PDF:   {f.name}")
                    print("\nStarting intake assistant...\n")
                    subprocess.run([sys.executable, str(ARCHIVE_SCRIPT)])
                    processed_pairs.add(batch_key)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped inbox watcher.")

if __name__ == "__main__":
    main()
