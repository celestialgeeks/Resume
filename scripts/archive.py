#!/usr/bin/env python3
"""
archive.py
Resume Version Archive & Automated Indexing Engine.
Handles intake, date-wise storage, metadata tracking, PDF preview rendering,
and Markdown documentation syncing (README.md and INDEX.md).
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from datetime import datetime, date
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MASTER_DIR = BASE_DIR / "master"
VERSIONS_DIR = BASE_DIR / "versions"
INBOX_DIR = BASE_DIR / "inbox"
ASSETS_DIR = BASE_DIR / "assets"
SCRIPTS_DIR = BASE_DIR / "scripts"
REGISTRY_FILE = BASE_DIR / "registry.json"
INDEX_FILE = BASE_DIR / "INDEX.md"
README_FILE = BASE_DIR / "README.md"
MASTER_PREVIEW_PNG = ASSETS_DIR / "master_preview.png"
MASTER_PLACEHOLDER_SVG = ASSETS_DIR / "master_placeholder.svg"

# Import generate_preview
sys.path.insert(0, str(SCRIPTS_DIR))
try:
    from generate_preview import generate_preview
except ImportError:
    generate_preview = None


def load_registry():
    """Loads the central resume registry."""
    if not REGISTRY_FILE.exists():
        return {"master": None, "versions": []}
    try:
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"master": None, "versions": []}


def save_registry(registry_data):
    """Saves the central resume registry formatted cleanly."""
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry_data, f, indent=2, ensure_ascii=False)


def sanitize_tag(tag: str) -> str:
    """Sanitizes a tag string for clean directory naming."""
    clean = "".join(c if (c.isalnum() or c in ("-", "_")) else "_" for c in tag.strip())
    clean = clean.strip("_")
    return clean or "version"


def find_inbox_files():
    """Finds .tex and .pdf files in inbox/."""
    tex_files = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() == ".tex"]
    pdf_files = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"]
    return tex_files, pdf_files


def run_git_command(args, cwd=BASE_DIR):
    """Runs a git command safely."""
    try:
        res = subprocess.run(
            ["git"] + args,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return res.returncode == 0, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return False, "", str(e)


def sync_markdown_docs(registry):
    """Regenerates README.md and INDEX.md to reflect current state."""
    master_info = registry.get("master")
    versions = registry.get("versions", [])
    
    # Sort versions reverse-chronologically
    sorted_versions = sorted(versions, key=lambda x: (x.get("date", ""), x.get("timestamp", "")), reverse=True)
    total_versions = len(sorted_versions)

    # 1. Generate INDEX.md
    index_lines = [
        "# 📑 Resume Versions & Changelog Index",
        "",
        "> Complete chronological index of all resume versions, target applications, and tailored changes.",
        "",
        f"**Total Archived Versions:** `{total_versions}` | **Last Cataloged:** `{datetime.now().strftime('%Y-%m-%d %H:%M')}`",
        "",
        "---",
        "",
        "| Date | Target / Tag | Description of Changes | Files | Preview |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    if not sorted_versions:
        index_lines.append("| — | *No versions archived yet* | *Drop files into inbox/ and run ./archive.sh* | — | — |")
    else:
        for v in sorted_versions:
            v_date = v.get("date", "N/A")
            v_tag = f"**{v.get('tag', 'Version')}**"
            v_desc = v.get("description", "").replace("\n", " ").strip()
            tex_rel = v.get("files", {}).get("tex", "")
            pdf_rel = v.get("files", {}).get("pdf", "")
            prev_rel = v.get("files", {}).get("preview", "")

            files_cell = []
            if tex_rel:
                files_cell.append(f"[LaTeX Source]({tex_rel})")
            if pdf_rel:
                files_cell.append(f"[PDF]({pdf_rel})")
            files_str = " · ".join(files_cell) if files_cell else "—"

            prev_str = f"[View Image]({prev_rel})" if prev_rel and os.path.exists(BASE_DIR / prev_rel) else "—"

            index_lines.append(f"| `{v_date}` | {v_tag} | {v_desc} | {files_str} | {prev_str} |")

    index_lines.extend([
        "",
        "---",
        "",
        "### 🔗 Quick Links",
        "- [Back to Master Showcase](README.md)",
        "- [Canonical Master LaTeX](master/resume.tex)",
        "- [Canonical Master PDF](master/resume.pdf)",
    ])

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")

    # 2. Generate README.md
    master_has_pdf = (MASTER_DIR / "resume.pdf").exists()
    master_has_tex = (MASTER_DIR / "resume.tex").exists()
    master_preview_exists = MASTER_PREVIEW_PNG.exists()
    preview_img_rel = "assets/master_preview.png" if master_preview_exists else "assets/master_placeholder.svg"

    master_date_str = master_info.get("updated", "Awaiting ingestion") if master_info else ("Present" if master_has_pdf else "Awaiting ingestion")
    latest_v_str = sorted_versions[0].get("tag", "None yet") if sorted_versions else "None yet"
    latest_v_date = sorted_versions[0].get("date", "—") if sorted_versions else "—"

    readme_content = f"""# 📄 Master Resume & Version Catalog

<div align="center">

![Total Versions](https://img.shields.io/badge/Archived_Versions-{total_versions}-blue?style=for-the-badge&logo=git)
![Master Status](https://img.shields.io/badge/Master_Resume-{"Active" if master_has_pdf else "Ready_for_Upload"}-emerald?style=for-the-badge&logo=latex)
![LaTeX Engine](https://img.shields.io/badge/Engine-Tectonic-purple?style=for-the-badge)
![Privacy](https://img.shields.io/badge/Access-Private_Repository-darkred?style=for-the-badge&logo=github)

<br/>

**A structured, automated repository for maintaining the canonical Master Resume, date-stamped customized versions, and instant visual previews.**

[📥 Master PDF](master/resume.pdf) • [📝 Master LaTeX](master/resume.tex) • [📑 Full Version Index (INDEX.md)](INDEX.md) • [🚀 How to Archive](#-how-to-drop--archive-versions)

</div>

---

## 🌟 Master Resume Showcase

<div align="center">
  <p><b>Canonical Living Master Resume</b></p>
  <a href="master/resume.pdf">
    <img src="{preview_img_rel}" alt="Master Resume Preview" width="650" style="border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.15);" />
  </a>
  <p><i>Click the image above to open the full master PDF.</i></p>
</div>

<br/>

### 📊 Repository Summary & Factors

| Metric | Status | Details |
| :--- | :--- | :--- |
| **Master Resume** | `{"✅ Synced" if master_has_pdf else "⏳ Awaiting Files"}` | `master/resume.tex` & `master/resume.pdf` |
| **Last Master Update** | `{master_date_str}` | Source of truth for all role-specific derivatives |
| **Total Tailored Versions** | `{total_versions}` | Tracked in [registry.json](registry.json) |
| **Latest Tailored Role** | `{latest_v_str}` | Cataloged on `{latest_v_date}` |
| **Compiler** | `Tectonic` | Standalone modern TeX/LaTeX engine |

---

## 🕒 Recent Tailored Versions (Latest 5)

| Date | Target / Company | Key Changes Made | Files |
| :--- | :--- | :--- | :--- |
"""

    if not sorted_versions:
        readme_content += "| — | *No tailored versions yet* | *Drop version files into inbox/ and run ./archive.sh* | — |\n"
    else:
        for v in sorted_versions[:5]:
            v_d = v.get("date", "N/A")
            v_t = f"**{v.get('tag', 'Version')}**"
            v_desc = v.get("description", "").replace("\n", " ").strip()
            tex_rel = v.get("files", {}).get("tex", "")
            pdf_rel = v.get("files", {}).get("pdf", "")
            f_links = []
            if tex_rel:
                f_links.append(f"[LaTeX]({tex_rel})")
            if pdf_rel:
                f_links.append(f"[PDF]({pdf_rel})")
            readme_content += f"| `{v_d}` | {v_t} | {v_desc} | {' · '.join(f_links)} |\n"

    readme_content += f"""
👉 **[View all {total_versions} archived versions in the complete index (INDEX.md)](INDEX.md)**

---

## 🚀 How to Drop & Archive Versions

### 1. Ingesting New Master Resume Files
When you want to update your primary base resume:
```bash
# Option A: Place resume.tex and resume.pdf into inbox/ or master/, then run:
./archive.sh --master

# Option B: Pass explicit paths
./archive.sh --master --tex /path/to/my_resume.tex --pdf /path/to/my_resume.pdf
```
*This automatically renders the high-resolution preview image and updates the README showcase.*

### 2. Archiving a Tailored Version (Date-wise)
Whenever you customize your resume for a specific job application, role, or company:
```bash
# Step 1: Drop the .tex and .pdf into the inbox/ folder
# Step 2: Run the intake assistant:
./archive.sh
```
The interactive assistant will ask:
- **Target / Tag**: (e.g. `Google_SWE`, `Apple_CoreML`, `JaneStreet_Quant`)
- **Description of changes**: (e.g. `Tailored experience bullets to distributed systems and low-latency C++`)

Or run with direct flags in one command:
```bash
./archive.sh --tag "Google_SWE" --desc "Focused on backend infrastructure and caching optimizations"
```

The system will:
1. Move the files to `versions/YYYY-MM-DD_<tag>/`
2. Create `metadata.json` with the changelog
3. Generate a thumbnail preview
4. Update `registry.json`, `INDEX.md`, and `README.md`
5. Create a clean Git commit and push to your private GitHub repo!

---

## 🛠 Directory Layout

```
Resume/
├── master/                      # Canonical living master resume
│   ├── resume.tex
│   └── resume.pdf
├── versions/                    # Date-wise customized versions
│   └── YYYY-MM-DD_<tag>/
│       ├── resume.tex
│       ├── resume.pdf
│       ├── preview.png
│       └── metadata.json
├── inbox/                       # Quick-drop folder for incoming files
├── assets/                      # Generated previews & badges
│   ├── master_preview.png
│   └── master_placeholder.svg
├── scripts/                     # Automation & indexing tools
├── archive.sh                   # Main CLI entrypoint
├── registry.json                # Single machine-readable source of truth
├── INDEX.md                     # Full chronological index table
└── README.md                    # Showcase & documentation
```

---

## ⚡ LaTeX Compilation with Tectonic
To compile any `.tex` file directly to `.pdf`:
```bash
tectonic master/resume.tex
# Or compile a version:
tectonic versions/2026-09-24_google-swe/resume.tex
```
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content.strip() + "\n")


def archive_master(tex_path=None, pdf_path=None, push=True):
    """Processes master resume files into master/ and regenerates preview and docs."""
    print("🚀 Ingesting Master Resume...")
    MASTER_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    # Resolve tex and pdf paths
    if not tex_path or not pdf_path:
        # Check inbox first
        inbox_tex, inbox_pdf = find_inbox_files()
        if not tex_path and inbox_tex:
            tex_path = str(inbox_tex[0])
        if not pdf_path and inbox_pdf:
            pdf_path = str(inbox_pdf[0])

    if not tex_path and (MASTER_DIR / "resume.tex").exists():
        tex_path = str(MASTER_DIR / "resume.tex")
    if not pdf_path and (MASTER_DIR / "resume.pdf").exists():
        pdf_path = str(MASTER_DIR / "resume.pdf")

    if not tex_path or not os.path.exists(tex_path):
        print("❌ Error: Missing master .tex file.")
        return False
    if not pdf_path or not os.path.exists(pdf_path):
        print("❌ Error: Missing master .pdf file.")
        return False

    dest_tex = MASTER_DIR / "resume.tex"
    dest_pdf = MASTER_DIR / "resume.pdf"

    if os.path.abspath(tex_path) != os.path.abspath(dest_tex):
        shutil.copy2(tex_path, dest_tex)
        if str(tex_path).startswith(str(INBOX_DIR)):
            try:
                os.remove(tex_path)
            except OSError:
                pass

    if os.path.abspath(pdf_path) != os.path.abspath(dest_pdf):
        shutil.copy2(pdf_path, dest_pdf)
        if str(pdf_path).startswith(str(INBOX_DIR)):
            try:
                os.remove(pdf_path)
            except OSError:
                pass

    # Generate preview
    print("🎨 Generating high-res preview of master PDF...")
    if generate_preview:
        generate_preview(str(dest_pdf), str(MASTER_PREVIEW_PNG), dpi=150)

    # Update registry
    registry = load_registry()
    today_str = date.today().isoformat()
    now_iso = datetime.now().isoformat()
    registry["master"] = {
        "updated": today_str,
        "timestamp": now_iso,
        "files": {
            "tex": "master/resume.tex",
            "pdf": "master/resume.pdf",
            "preview": "assets/master_preview.png"
        }
    }
    save_registry(registry)
    sync_markdown_docs(registry)

    # Git commit
    print("📦 Staging master updates in Git...")
    run_git_command(["add", "master/", "assets/", "registry.json", "README.md", "INDEX.md"])
    success, _, _ = run_git_command(["commit", "-m", f"update(master): updated canonical resume [{today_str}]"])
    if success:
        print("✅ Git commit created.")
        if push:
            print("🌐 Pushing changes to remote...")
            run_git_command(["push"])
    else:
        print("ℹ️ No new changes to commit in git.")

    print(f"🎉 Master resume successfully updated & documented!")
    return True


def archive_version(tex_path=None, pdf_path=None, tag=None, description=None, target_date=None, push=True):
    """Archives a customized resume version date-wise with metadata and indexing."""
    print("🚀 Archiving Tailored Resume Version...")
    VERSIONS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Resolve files from inbox if not explicitly given
    if not tex_path or not pdf_path:
        inbox_tex, inbox_pdf = find_inbox_files()
        if not tex_path and inbox_tex:
            tex_path = str(inbox_tex[0])
            print(f"📂 Found LaTeX file in inbox: {os.path.basename(tex_path)}")
        if not pdf_path and inbox_pdf:
            pdf_path = str(inbox_pdf[0])
            print(f"📂 Found PDF file in inbox: {os.path.basename(pdf_path)}")

    if not tex_path or not os.path.exists(tex_path):
        print("❌ Error: Could not locate .tex file. Drop it into inbox/ or specify --tex <path>.")
        return False
    if not pdf_path or not os.path.exists(pdf_path):
        print("❌ Error: Could not locate .pdf file. Drop it into inbox/ or specify --pdf <path>.")
        return False

    # 2. Interactive prompt for missing info if in interactive terminal
    if not tag:
        default_tag = "tailored"
        try:
            val = input(f"🏷️ Enter target role / company / tag [{default_tag}]: ").strip()
            tag = val if val else default_tag
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            return False

    if not description:
        try:
            description = input("📝 Describe the key changes made: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            return False

    if not description:
        description = "Tailored resume version."

    # 3. Determine destination directory
    date_str = target_date or date.today().isoformat()
    clean_tag = sanitize_tag(tag)
    version_id = f"{date_str}_{clean_tag}"
    dest_dir = VERSIONS_DIR / version_id

    # Handle duplicates by appending counter
    counter = 2
    while dest_dir.exists():
        version_id = f"{date_str}_{clean_tag}_v{counter}"
        dest_dir = VERSIONS_DIR / version_id
        counter += 1

    dest_dir.mkdir(parents=True, exist_ok=True)

    # 4. Copy files
    dest_tex = dest_dir / "resume.tex"
    dest_pdf = dest_dir / "resume.pdf"
    dest_preview = dest_dir / "preview.png"

    shutil.copy2(tex_path, dest_tex)
    shutil.copy2(pdf_path, dest_pdf)

    # Clean up inbox if files originated there
    if str(tex_path).startswith(str(INBOX_DIR)):
        try:
            os.remove(tex_path)
        except OSError:
            pass
    if str(pdf_path).startswith(str(INBOX_DIR)):
        try:
            os.remove(pdf_path)
        except OSError:
            pass

    # 5. Generate thumbnail preview
    if generate_preview:
        generate_preview(str(dest_pdf), str(dest_preview), dpi=100)

    # 6. Create version metadata.json
    now_iso = datetime.now().isoformat()
    rel_tex = f"versions/{dest_dir.name}/resume.tex"
    rel_pdf = f"versions/{dest_dir.name}/resume.pdf"
    rel_prev = f"versions/{dest_dir.name}/preview.png" if dest_preview.exists() else None

    meta = {
        "id": dest_dir.name,
        "date": date_str,
        "timestamp": now_iso,
        "tag": tag,
        "description": description,
        "files": {
            "tex": rel_tex,
            "pdf": rel_pdf,
            "preview": rel_prev
        }
    }
    with open(dest_dir / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    # 7. Update central registry
    registry = load_registry()
    registry.setdefault("versions", []).append(meta)
    save_registry(registry)

    # 8. Sync docs
    sync_markdown_docs(registry)

    # 9. Git commit & push
    print(f"📦 Staging version '{dest_dir.name}' in Git...")
    run_git_command(["add", f"versions/{dest_dir.name}/", "registry.json", "INDEX.md", "README.md"])
    commit_msg = f"archive({date_str}): {tag} - {description[:70]}"
    success, _, _ = run_git_command(["commit", "-m", commit_msg])
    if success:
        print(f"✅ Git commit created: {commit_msg}")
        if push:
            print("🌐 Pushing changes to remote...")
            run_git_command(["push"])
    else:
        print("ℹ️ Git commit skipped or nothing changed.")

    print(f"🎉 Successfully archived to: versions/{dest_dir.name}/")
    print(f"📄 Updated INDEX.md and README.md with new version entries.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Resume Version Archive & Automated Indexing Engine")
    parser.add_argument("--master", action="store_true", help="Ingest/update master resume")
    parser.add_argument("--tex", type=str, help="Path to .tex file")
    parser.add_argument("--pdf", type=str, help="Path to .pdf file")
    parser.add_argument("--tag", type=str, help="Target role, company, or version identifier")
    parser.add_argument("--desc", type=str, help="Short description of changes made")
    parser.add_argument("--date", type=str, help="Custom date YYYY-MM-DD (defaults to today)")
    parser.add_argument("--no-push", action="store_true", help="Skip git push")
    parser.add_argument("--sync", action="store_true", help="Only resync README.md and INDEX.md from registry")

    args = parser.parse_args()

    if args.sync:
        print("🔄 Resyncing markdown documentation from registry.json...")
        reg = load_registry()
        sync_markdown_docs(reg)
        print("✅ INDEX.md and README.md successfully synced.")
        return

    push_to_git = not args.no_push

    if args.master:
        archive_master(tex_path=args.tex, pdf_path=args.pdf, push=push_to_git)
    else:
        archive_version(
            tex_path=args.tex,
            pdf_path=args.pdf,
            tag=args.tag,
            description=args.desc,
            target_date=args.date,
            push=push_to_git
        )


if __name__ == "__main__":
    main()
