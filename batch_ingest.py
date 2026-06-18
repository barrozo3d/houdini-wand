"""
batch_ingest.py — Ingest a list of NEW YouTube URLs using the enhanced pipeline.

Add URLs to the URLS list below, then run:
  python batch_ingest.py
  python batch_ingest.py --skip-video       # faster, no frame extraction
  python batch_ingest.py --whisper-model small

Each tutorial is committed and pushed individually.
"""

import sys
import subprocess
import argparse
from pathlib import Path

SKILL_DIR     = Path(__file__).parent
INGEST_SCRIPT = SKILL_DIR / "ingest.py"

# ── Add URLs here ─────────────────────────────────────────────────────────────
URLS = [
    # Standalone (not in houdini.school channel)
    "https://www.youtube.com/watch?v=hHLH7pr_eZo",
    "https://www.youtube.com/watch?v=7J-hDF0H6ck",

    # Houdini School channel — tutorials only (battles/Hip.tv/SEQUENZA/TouchDesigner excluded)
    "https://www.youtube.com/watch?v=d3pMfIsvAyQ",  # Yan Paul Dubbelman | High-Quality Custom Leaves
    "https://www.youtube.com/watch?v=q_aD6sza6gA",  # MOPs Part 3
    "https://www.youtube.com/watch?v=J2g0v1k6MBs",  # MOPs Part 2
    "https://www.youtube.com/watch?v=g9eSle9IVjU",  # MOPs Part 1
    "https://www.youtube.com/watch?v=0XnjEVcaq6A",  # Experimental Motion - CHOPS
    "https://www.youtube.com/watch?v=A11B_UE07ac",  # Experimental Motion - The SOP Solver
    "https://www.youtube.com/watch?v=xjf_mQKI3R8",  # Yan Paul Dubbelman | Procedural Living Plants
    "https://www.youtube.com/watch?v=7NejsDXzxXI",  # Effective TD
    "https://www.youtube.com/watch?v=rKcH4oIfoVw",  # Procedural HDAs for Unreal
    "https://www.youtube.com/watch?v=EuL8598tnm4",  # Velocity Forces 2.0: Advanced
    "https://www.youtube.com/watch?v=aKJB3uOKFKM",  # Small Scale Fluids
    "https://www.youtube.com/watch?v=w_NnhoKeLlE",  # Surface Advection
    "https://www.youtube.com/watch?v=v1psrXhj9IY",  # Forces: Building Custom Velocity Setups
    "https://www.youtube.com/watch?v=VM3m52SHUrk",  # Attributes
    "https://www.youtube.com/watch?v=psd-vus4U5s",  # Art Directing Cloth in Houdini
    "https://www.youtube.com/watch?v=pqGY2M2VBQo",  # MOPs: Motion Operators for Houdini
    "https://www.youtube.com/watch?v=nUwA8xsmnS0",  # Problem-Space
    "https://www.youtube.com/watch?v=mwUn21-v_0s",  # History of Houdini Systems
    "https://www.youtube.com/watch?v=krZVhZFvAo0",  # Maths for Artists
    "https://www.youtube.com/watch?v=j5XxDiG25wQ",  # Procedural Growth with KineFX and Labs Tree Tools
    "https://www.youtube.com/watch?v=g-EDNX2uaXo",  # Scientific Phenomena in Houdini
    "https://www.youtube.com/watch?v=f7QwzqZqtFI",  # Visualizing Protein Data Bank Information
    "https://www.youtube.com/watch?v=c9qw6hVstEA",  # Effective TD (2)
    "https://www.youtube.com/watch?v=YKnqahKFNuY",  # Liquid SOPs
    "https://www.youtube.com/watch?v=V31YogBW2Y0",  # From C4D to Houdini
    "https://www.youtube.com/watch?v=RDiA2R47Wzo",  # Houdini FX in Unreal
    "https://www.youtube.com/watch?v=OQDFQtoTOuA",  # Loops
    "https://www.youtube.com/watch?v=M8HOGm6FxIw",  # Simulated Creatures
    "https://www.youtube.com/watch?v=J9dhXxxLPfI",  # Magical FX
    "https://www.youtube.com/watch?v=GRUGv5ydLFQ",  # Working with Scientific Datasets
    "https://www.youtube.com/watch?v=FKHhGJFvjys",  # Noise
    "https://www.youtube.com/watch?v=EE1wuXaI8wI",  # BUILD YOUR BRAIN – Cell division
    "https://www.youtube.com/watch?v=4tJmvGrhxA4",  # Character Design and Modeling
]
# ─────────────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(description="Batch ingest new tutorials")
    parser.add_argument("--skip-video", action="store_true")
    parser.add_argument("--whisper-model", default="base",
                        choices=["tiny", "base", "small", "medium", "large"])
    args = parser.parse_args()

    if not URLS:
        print("No URLs in URLS list. Add them to batch_ingest.py and re-run.")
        return

    print(f"Ingesting {len(URLS)} URL(s)...\n")
    successes, failures = [], []

    for i, url in enumerate(URLS, 1):
        print(f"\n[{i}/{len(URLS)}] {url}")
        cmd = [sys.executable, str(INGEST_SCRIPT), url,
               "--whisper-model", args.whisper_model]
        if args.skip_video:
            cmd.append("--skip-video")

        result = subprocess.run(cmd, cwd=SKILL_DIR)
        if result.returncode == 0:
            successes.append(url)
        else:
            failures.append(url)

    print(f"\n{'='*50}")
    print(f"Done -- {len(successes)} succeeded, {len(failures)} failed")
    if failures:
        print("Failed:")
        for u in failures:
            print(f"  {u}")


if __name__ == "__main__":
    main()
