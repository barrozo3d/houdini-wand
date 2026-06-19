"""
check_skill.py — Health check for houdini-wand skill.
Run from the skill root: python check_skill.py
"""
import os, re

print("=== HOUDINI WAND SKILL CHECK ===")

# 1. Count tutorials + pending extraction
idx = open("tutorials/INDEX.md", "r", encoding="utf-8-sig").read()
entries = re.findall(r"^### ", idx, re.MULTILINE)
pending_idx = re.findall(r"\[PENDING\]", idx)
print(f"Tutorials in INDEX: {len(entries)} total, {len(pending_idx)} with PENDING fields")

# 2. Check extraction_status in tutorial files
tutorial_files = [f for f in os.listdir("tutorials") if f.endswith(".md") and f != "INDEX.md"]
pending_extraction = []
for tf in tutorial_files:
    content = open(f"tutorials/{tf}", "r", encoding="utf-8-sig").read()
    if "extraction_status: pending" in content:
        pending_extraction.append(tf)
print(f"Tutorial files with extraction_status=pending: {len(pending_extraction)}")
for p in sorted(pending_extraction):
    print(f"  PENDING: {p}")

# 3. Check all referenced files in skill file exist
skill = open("SKILL.md", "r", encoding="utf-8").read()
refs_mentioned = re.findall(r"`(references/[^`]+\.md)`", skill)
refs_mentioned += re.findall(r"`(recipes/[^`]+\.md)`", skill)
# Skip template placeholders (hXX, XX patterns)
refs_mentioned = [r for r in refs_mentioned if 'XX' not in r and 'X-X' not in r]
refs_missing = [r for r in refs_mentioned if not os.path.exists(r)]
print(f"Files mentioned in skill file: {len(refs_mentioned)}, missing: {len(refs_missing)}")
for r in refs_missing:
    print(f"  MISSING: {r}")

# 4. Check for dead cross-refs in reference files
ref_files = [f for f in os.listdir("references") if f.endswith(".md")]
broken = []
for rf in ref_files:
    content = open(f"references/{rf}", "r", encoding="utf-8-sig").read()
    file_refs = re.findall(r"`((?:references|recipes|tutorials)/[^`]+\.md)`", content)
    for fr in file_refs:
        if not os.path.exists(fr) and 'XX' not in fr and 'X-X' not in fr:
            broken.append((rf, fr))
# Also check recipe files
if os.path.isdir("recipes"):
    for rcf in os.listdir("recipes"):
        if not rcf.endswith(".md"):
            continue
        content = open(f"recipes/{rcf}", "r", encoding="utf-8-sig").read()
        file_refs = re.findall(r"`((?:references|recipes|tutorials)/[^`]+\.md)`", content)
        for fr in file_refs:
            if not os.path.exists(fr) and 'XX' not in fr and 'X-X' not in fr:
                broken.append((rcf, fr))
print(f"Broken cross-refs: {len(broken)}")
for src, dest in broken:
    print(f"  {src} -> {dest}")

# 5. Check version-tracker
vt = open("references/version-tracker.md", "r", encoding="utf-8-sig").read()
checked_match = re.search(r"last_checked:\s*\*?\*?(.+)", vt)
stable_match  = re.search(r"H(\d+(?:\.\d+)?)\s*\(current\)", vt)
print(f"Version tracker last_checked: {checked_match.group(1).strip() if checked_match else 'NOT FOUND'}")
print(f"Version tracker current stable: {'H' + stable_match.group(1) if stable_match else 'NOT FOUND'}")

# 6. Tutorial file / INDEX consistency
referenced = set(re.findall(r"tutorials/([^\s/]+\.md)", idx))
referenced.discard("filename.md")  # template example
all_files = set(tutorial_files)
orphans = all_files - referenced
missing_on_disk = referenced - all_files
print(f"Tutorial files: {len(all_files)} on disk, {len(referenced)} in INDEX")
print(f"Orphaned files (on disk, not in INDEX): {len(orphans)}")
for o in sorted(orphans):
    print(f"  ORPHAN: {o}")
print(f"Missing files (in INDEX, not on disk): {len(missing_on_disk)}")
for m in sorted(missing_on_disk):
    print(f"  MISSING: {m}")

print()
print("=== CHECK COMPLETE ===")
