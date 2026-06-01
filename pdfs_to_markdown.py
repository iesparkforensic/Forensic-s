#!/usr/bin/env python3
"""Merge a folder of PDFs into a single Markdown file.

Usage:
    python pdfs_to_markdown.py INPUT_DIR [-o OUTPUT.md] [--toc] [--page-breaks]

Examples:
    python pdfs_to_markdown.py ./pdfs
    python pdfs_to_markdown.py ./pdfs -o combined.md --toc

Requires: pymupdf4llm  (pip install pymupdf4llm)
"""
import argparse
import re
import sys
from pathlib import Path

import pymupdf4llm


def natural_key(path: Path):
    """Sort like a human: file2 before file10."""
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r"(\d+)", path.name)]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    ap = argparse.ArgumentParser(description="Merge many PDFs into one Markdown file.")
    ap.add_argument("input_dir", help="Folder containing the PDF files")
    ap.add_argument("-o", "--output", default="combined.md", help="Output Markdown file")
    ap.add_argument("--toc", action="store_true", help="Add a table of contents")
    ap.add_argument("--page-breaks", action="store_true",
                    help="Insert a horizontal rule between PDF pages")
    args = ap.parse_args()

    in_dir = Path(args.input_dir)
    if not in_dir.is_dir():
        sys.exit(f"Error: {in_dir} is not a directory")

    pdfs = sorted(in_dir.glob("*.pdf"), key=natural_key)
    if not pdfs:
        sys.exit(f"Error: no .pdf files found in {in_dir}")

    print(f"Found {len(pdfs)} PDF(s). Converting...")

    sections = []
    toc_lines = []
    for i, pdf in enumerate(pdfs, 1):
        title = pdf.stem
        print(f"  [{i}/{len(pdfs)}] {pdf.name}")
        try:
            md = pymupdf4llm.to_markdown(
                str(pdf),
                page_chunks=False,
                show_progress=False,
            )
        except Exception as e:  # keep going if one PDF is corrupt
            md = f"> **Could not convert this PDF:** {e}\n"
            print(f"      ! failed: {e}", file=sys.stderr)

        if args.page_breaks:
            md = md.replace("\n-----\n", "\n\n---\n\n")

        anchor = slugify(title)
        toc_lines.append(f"{i}. [{title}](#{anchor})")
        sections.append(f'<a id="{anchor}"></a>\n\n# {title}\n\n{md.strip()}\n')

    parts = ["# Combined PDF Export\n",
             f"*{len(pdfs)} documents merged.*\n"]
    if args.toc:
        parts.append("## Table of Contents\n\n" + "\n".join(toc_lines) + "\n")
    parts.append("\n\n---\n\n".join(sections))

    out = Path(args.output)
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"\nDone -> {out}  ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
