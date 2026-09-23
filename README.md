# 📄 Master Resume & Version Catalog

<div align="center">

![Total Versions](https://img.shields.io/badge/Archived_Versions-0-blue?style=for-the-badge&logo=git)
![Master Status](https://img.shields.io/badge/Master_Resume-Ready_for_Upload-emerald?style=for-the-badge&logo=latex)
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
    <img src="assets/master_placeholder.svg" alt="Master Resume Preview" width="650" style="border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.15);" />
  </a>
  <p><i>Click the image above to open the full master PDF.</i></p>
</div>

<br/>

### 📊 Repository Summary & Factors

| Metric | Status | Details |
| :--- | :--- | :--- |
| **Master Resume** | `⏳ Awaiting Files` | `master/resume.tex` & `master/resume.pdf` |
| **Last Master Update** | `Awaiting ingestion` | Source of truth for all role-specific derivatives |
| **Total Tailored Versions** | `0` | Tracked in [registry.json](registry.json) |
| **Latest Tailored Role** | `None yet` | Cataloged on `—` |
| **Compiler** | `Tectonic` | Standalone modern TeX/LaTeX engine |

---

## 🕒 Recent Tailored Versions (Latest 5)

| Date | Target / Company | Key Changes Made | Files |
| :--- | :--- | :--- | :--- |
| — | *No tailored versions yet* | *Drop version files into inbox/ and run ./archive.sh* | — |

👉 **[View all 0 archived versions in the complete index (INDEX.md)](INDEX.md)**

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
