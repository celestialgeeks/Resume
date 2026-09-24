# 📥 Resume Drop Zone (Inbox)

Welcome to your resume drop zone. This directory is configured for quick staging of your edited resumes.

---

## 🎯 How It Works

### Option 1: AI-Powered Assistant (Recommended)
1. **Drop your resume** (`.tex`, `.pdf`, or both) directly into this `inbox/` folder.
2. In the Antigravity chat, tell the assistant what you want to do:
   - **For Master**: *"I added the newly edited resume to inbox, move it to master."*
   - **For a Tailored Version**: *"I added my new resume to inbox, move it to a version for Google SWE."*
3. **Antigravity will automatically**:
   - 🔍 Inspect and analyze your resume files.
   - ⚡ Compile LaTeX via Tectonic if only `.tex` was provided.
   - 📝 Compare changes against Master and write a detailed, professional description/changelog.
   - 📂 Move the files to `master/` or `versions/YYYY-MM-DD_<tag>/`.
   - 🎨 Generate high-resolution visual previews.
   - 📑 Update `registry.json`, `INDEX.md`, and `README.md`.
   - 🚀 Commit and push the updates directly to GitHub!

---

### Option 2: Terminal Command
You can also run the command line intake tool at any time:

```bash
# To ingest files as the canonical Master resume:
./archive.sh --master

# To archive files as a role-specific version:
./archive.sh --tag "Target_Role" --desc "Description of changes"
```

*(Optional: You can also drop a `tag.txt` or `desc.txt` file here in `inbox/` if you want `./archive.sh` to read them automatically.)*
