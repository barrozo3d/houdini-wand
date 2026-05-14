"""
Houdini Wand Skill — Tutorial Ingestion Script

Usage:
  python ingest.py <URL>
  python ingest.py <URL> --title "Custom Title"
  python ingest.py <URL> --dry-run   (preview without saving)

Supports:
  - YouTube videos (extracts transcript via yt-dlp)
  - Web articles / documentation (via urllib + basic HTML stripping)

Output:
  - Creates tutorials/<slug>.md with structured content
  - Updates tutorials/INDEX.md with new entry
  - Auto-commits and pushes to GitHub

NOTE ON BOOK CHAPTERS:
For book content (PDFs, pasted text), use Mode 3 in the skill directly
rather than this script. The skill handles manual ingestion with
Claude doing the extraction pass.
"""

import sys
import os
import re
import json
import subprocess
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

SKILL_DIR = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
INDEX_FILE = TUTORIALS_DIR / "INDEX.md"


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_-]+", "-", slug)
    return slug[:60].strip("-")


def is_youtube(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url


def fetch_youtube(url: str) -> dict:
    """Extract metadata and transcript from YouTube via yt-dlp."""
    print(f"Fetching YouTube: {url}")

    meta_cmd = [
        sys.executable, "-m", "yt_dlp",
        "--dump-json", "--no-playlist",
        url
    ]
    result = subprocess.run(meta_cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp metadata failed: {result.stderr}")

    meta = json.loads(result.stdout)
    title = meta.get("title", "Unknown")
    author = meta.get("uploader", "Unknown")
    description = meta.get("description", "")
    duration = meta.get("duration", 0)

    # Get transcript
    transcript = ""
    transcript_cmd = [
        sys.executable, "-m", "yt_dlp",
        "--write-auto-subs", "--sub-lang", "en",
        "--sub-format", "vtt",
        "--skip-download",
        "--output", str(TUTORIALS_DIR / "%(id)s"),
        url
    ]
    subprocess.run(transcript_cmd, capture_output=True, timeout=120)

    vid_id = meta.get("id", "")
    vtt_file = TUTORIALS_DIR / f"{vid_id}.en.vtt"
    if vtt_file.exists():
        raw = vtt_file.read_text(encoding="utf-8", errors="ignore")
        lines = []
        for line in raw.split("\n"):
            if "-->" in line or line.startswith("WEBVTT") or line.strip().isdigit():
                continue
            clean = re.sub(r"<[^>]+>", "", line).strip()
            if clean and (not lines or clean != lines[-1]):
                lines.append(clean)
        transcript = " ".join(lines)
        vtt_file.unlink()

    return {
        "title": title,
        "author": author,
        "description": description,
        "transcript": transcript,
        "duration_seconds": duration,
        "url": url,
        "type": "youtube",
    }


def fetch_article(url: str) -> dict:
    """Fetch web article content."""
    print(f"Fetching article: {url}")
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch URL: {e}")

    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"&nbsp;", " ", html)
    html = re.sub(r"&[a-z]+;", "", html)
    text = re.sub(r"\s+", " ", html).strip()

    title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else urlparse(url).netloc

    return {
        "title": title,
        "author": urlparse(url).netloc,
        "description": "",
        "transcript": text[:8000],
        "duration_seconds": 0,
        "url": url,
        "type": "article",
    }


def build_tutorial_markdown(data: dict, custom_title: str = None) -> str:
    title = custom_title or data["title"]
    now = datetime.now().strftime("%Y-%m-%d")
    source_type = "YouTube" if data["type"] == "youtube" else "Article"
    slug = slugify(title)

    content_for_analysis = data.get("transcript") or data.get("description", "No content available")

    md = f"""---
title: {title}
source: {source_type}
url: {data['url']}
author: {data['author']}
ingested: {now}
houdini_version: unknown
tags: []
---

# {title}

**Source:** [{source_type}]({data['url']})
**Author:** {data['author']}
**Ingested:** {now}

---

## Description

{data.get('description', 'N/A')[:500]}

---

## Raw Content (for analysis)

{content_for_analysis[:6000]}

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/{slug}.md and extract:
> - Core Houdini technique taught
> - Step-by-step workflow
> - Key nodes, VEX, or settings
> - Houdini version
> - Difficulty level
> - Tags"

### Core Technique
[To be extracted]

### Key Steps
[To be extracted]

### Houdini Nodes / VEX / Settings
[To be extracted]

### Difficulty
[Beginner / Intermediate / Advanced / Expert]

### Houdini Version
[Version if mentioned, otherwise "Not specified"]

### Tags
[To be added]
"""
    return md


def update_index(title: str, url: str, filename: str, source_type: str, author: str) -> None:
    entry = f"""
### {title}
- **Source:** {source_type}
- **URL:** {url}
- **Author:** {author}
- **Houdini Version:** (check file)
- **Tags:** (check file)
- **Summary:** (analyze file to extract summary)
- **File:** tutorials/{filename}
"""
    content = INDEX_FILE.read_text(encoding="utf-8")
    marker = "*(Empty — add your first entry by saying"
    if marker in content:
        content = content.replace(
            '*(Empty — add your first entry by saying "ingest this: [URL]")*',
            entry.strip()
        )
    else:
        insert_before = "---\n\n## Tag Reference"
        content = content.replace(insert_before, f"\n{entry}\n{insert_before}")

    INDEX_FILE.write_text(content, encoding="utf-8")
    print(f"Updated INDEX.md with: {title}")


def main():
    parser = argparse.ArgumentParser(description="Ingest a tutorial into the Houdini Wand skill")
    parser.add_argument("url", help="YouTube URL or article URL to ingest")
    parser.add_argument("--title", help="Custom title override")
    parser.add_argument("--dry-run", action="store_true", help="Preview without saving")
    args = parser.parse_args()

    url = args.url

    if is_youtube(url):
        data = fetch_youtube(url)
    else:
        data = fetch_article(url)

    title = args.title or data["title"]
    slug = slugify(title)
    filename = f"{slug}.md"
    output_path = TUTORIALS_DIR / filename

    md = build_tutorial_markdown(data, custom_title=title)

    if args.dry_run:
        print("\n--- DRY RUN OUTPUT ---")
        print(md[:2000])
        print(f"\nWould save to: {output_path}")
        return

    if output_path.exists():
        print(f"Warning: {filename} already exists. Overwriting.")

    output_path.write_text(md, encoding="utf-8")
    print(f"Saved: {output_path}")

    source_type = "YouTube" if data["type"] == "youtube" else "Article"
    update_index(title, url, filename, source_type, data["author"])

    print(f"\nDone. Tutorial saved to: tutorials/{filename}")

    try:
        repo_dir = SKILL_DIR
        subprocess.run(["git", "add", str(output_path), str(INDEX_FILE)], cwd=repo_dir, check=True)
        subprocess.run(["git", "commit", "-m", f"ingest: {title}"], cwd=repo_dir, check=True)
        subprocess.run(["git", "push"], cwd=repo_dir, check=True)
        print("Pushed to GitHub.")
    except Exception as e:
        print(f"Warning: auto-push failed ({e}). Run 'git push' manually.")

    print("To extract structured notes, ask Claude:")
    print(f'  "Analyze tutorials/{filename} and fill in the structured notes section"')


if __name__ == "__main__":
    main()
