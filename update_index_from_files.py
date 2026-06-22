# -*- coding: utf-8 -*-
"""Sync tutorials/INDEX.md entries from completed tutorial file frontmatter + Summary section."""
import re, os

BASE = r"C:\Users\KABUM\.claude\skills\houdini-wand"
TUT_DIR = os.path.join(BASE, "tutorials")
INDEX_PATH = os.path.join(TUT_DIR, "INDEX.md")

def parse_tutorial(path):
    content = open(path, "r", encoding="utf-8-sig").read()
    fm = re.search(r"^---\n(.*?)\n---", content, re.DOTALL).group(1)
    version_m = re.search(r'^houdini_version:\s*(.+)$', fm, re.MULTILINE)
    tags_m = re.search(r'^tags:\s*(\[.+\])$', fm, re.MULTILINE)
    version = version_m.group(1).strip().strip('"') if version_m else "[PENDING]"
    tags_raw = tags_m.group(1).strip() if tags_m else "[]"
    tags_list = [t.strip() for t in tags_raw.strip("[]").split(",") if t.strip()]
    tags = ", ".join(tags_list)
    summary_m = re.search(r"### Summary\n(.+?)\n\n###", content, re.DOTALL)
    summary = summary_m.group(1).strip().replace("\n", " ") if summary_m else "[PENDING EXTRACTION]"
    if len(summary) > 400:
        summary = summary[:397].rsplit(" ", 1)[0] + "..."
    return version, tags, summary

def main():
    idx = open(INDEX_PATH, "r", encoding="utf-8-sig").read()
    complete_files = [f for f in os.listdir(TUT_DIR) if f.endswith(".md") and f != "INDEX.md"]

    updated = 0
    for fname in complete_files:
        path = os.path.join(TUT_DIR, fname)
        content = open(path, "r", encoding="utf-8-sig").read()
        if "extraction_status: complete" not in content:
            continue
        version, tags, summary = parse_tutorial(path)

        file_marker = f"tutorials/{fname}"
        pattern = re.compile(
            r"(- \*\*File:\*\* " + re.escape(file_marker) + r")",
        )
        m = pattern.search(idx)
        if not m:
            continue
        block_start = idx.rfind("### ", 0, m.start())
        block_end = idx.find("\n\n\n", m.end())
        if block_end == -1:
            block_end = len(idx)
        block = idx[block_start:block_end]

        new_block = block
        new_block = re.sub(r"- \*\*Houdini Version:\*\* .+", f"- **Houdini Version:** {version}", new_block)
        new_block = re.sub(r"- \*\*Tags:\*\* .+", f"- **Tags:** {tags}", new_block)
        new_block = re.sub(r"- \*\*Summary:\*\* .+", f"- **Summary:** {summary}", new_block)

        if new_block != block:
            idx = idx[:block_start] + new_block + idx[block_end:]
            updated += 1

    open(INDEX_PATH, "w", encoding="utf-8-sig", newline="\r\n").write(idx)
    print(f"Updated {updated} INDEX.md entries.")
    remaining_pending = len(re.findall(r"\[PENDING\]", idx))
    print(f"Remaining [PENDING] markers in INDEX.md: {remaining_pending}")

if __name__ == "__main__":
    main()
