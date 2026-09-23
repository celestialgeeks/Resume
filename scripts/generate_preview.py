#!/usr/bin/env python3
"""
generate_preview.py
Generates a crisp PNG preview image from page 1 of a PDF resume.
Uses pdftoppm (poppler) if available, with a graceful fallback to macOS qlmanage.
"""

import sys
import os
import shutil
import subprocess
import glob

def generate_preview(pdf_path: str, output_png_path: str, dpi: int = 150) -> bool:
    """
    Renders page 1 of the given PDF as a PNG image at output_png_path.
    """
    if not os.path.exists(pdf_path):
        print(f"❌ Error: PDF file not found at {pdf_path}", file=sys.stderr)
        return False

    os.makedirs(os.path.dirname(os.path.abspath(output_png_path)), exist_ok=True)
    temp_prefix = os.path.join(os.path.dirname(output_png_path), "_temp_preview")

    # Clean up any leftover temp files
    for f in glob.glob(f"{temp_prefix}*"):
        try:
            os.remove(f)
        except OSError:
            pass

    # 1. Primary engine: pdftoppm
    pdftoppm_bin = shutil.which("pdftoppm")
    if pdftoppm_bin:
        cmd = [
            pdftoppm_bin,
            "-png",
            "-r", str(dpi),
            "-f", "1",
            "-l", "1",
            pdf_path,
            temp_prefix
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0:
            candidates = glob.glob(f"{temp_prefix}*.png")
            if candidates:
                first_page = sorted(candidates)[0]
                shutil.move(first_page, output_png_path)
                # Remove extra temp files if any
                for extra in glob.glob(f"{temp_prefix}*"):
                    try:
                        os.remove(extra)
                    except OSError:
                        pass
                print(f"✅ Generated high-res preview via pdftoppm: {output_png_path}")
                return True

    # 2. Fallback engine: macOS native qlmanage + sips
    qlmanage_bin = shutil.which("qlmanage")
    sips_bin = shutil.which("sips")
    if qlmanage_bin and sys.platform == "darwin":
        temp_dir = os.path.join(os.path.dirname(output_png_path), "_ql_temp")
        os.makedirs(temp_dir, exist_ok=True)
        cmd = [qlmanage_bin, "-t", "-s", "1200", "-o", temp_dir, pdf_path]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        ql_files = glob.glob(os.path.join(temp_dir, "*.png"))
        if ql_files:
            shutil.move(ql_files[0], output_png_path)
            shutil.rmtree(temp_dir, ignore_errors=True)
            print(f"✅ Generated preview via macOS QuickLook: {output_png_path}")
            return True
        shutil.rmtree(temp_dir, ignore_errors=True)

    print("⚠️ Warning: Neither pdftoppm nor qlmanage succeeded in rendering the preview.", file=sys.stderr)
    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_preview.py <input.pdf> <output.png> [dpi]")
        sys.exit(1)
    
    in_pdf = sys.argv[1]
    out_png = sys.argv[2]
    custom_dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 150
    success = generate_preview(in_pdf, out_png, custom_dpi)
    sys.exit(0 if success else 1)
