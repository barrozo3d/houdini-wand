"""
batch_ingest.py — Ingest a list of NEW YouTube URLs using the enhanced pipeline.

Add URLs to the URLS list below, then run:
  python batch_ingest.py
  python batch_ingest.py --skip-video       # no frames at all, text-only
  python batch_ingest.py --whisper-model small
  python batch_ingest.py --dry-run          # preview which URLs are new (no ingest)

Already-ingested URLs (those in tutorials/INDEX.md) are automatically skipped.
Each tutorial is committed and pushed individually.

NOTE: this only runs Step 1 (ingest.py) per URL — transcript collection, no
video/frame download (that's deferred to Step 2, content-aware, see
select_frames.py). After this script finishes, tell Claude Code: "extract all
pending tutorials" — for each one, Claude reads the timestamped transcript,
picks real technique/result moments (even inside official chapters — don't
trust chapter_start+5s blindly), runs `select_frames.py <slug> <ts...>`, then
writes the Structured Notes and commits.
"""

import sys
import subprocess
import argparse
import re
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

    # ── The VFX School Archive ─────────────────────────────────────────────────
    # Each course = a playlist. Strategy: intro video per week/module + targeted
    # gap-fillers for techniques absent from the current knowledge base.
    # Estimated version per course noted below.

    # Houdini Film FX Program Season 1 (~H18, Mantra renderer, no Solaris/Karma)
    # Course overview + version identification
    "https://www.youtube.com/watch?v=W1_pCONvY_o",   # 00 weeks overview
    "https://www.youtube.com/watch?v=EMmAmGGsI6I",   # 03 houdini versions (explicit version mention)
    # Gap: SOP Solver concept + SOP→POP comparison (not covered elsewhere)
    "https://www.youtube.com/watch?v=8HkP7iVgi0Y",   # 51 introducing the sop solver
    "https://www.youtube.com/watch?v=l65A4S4YhSw",   # 52 creating a simplified particle system
    "https://www.youtube.com/watch?v=9objvx69_58",   # 53 recreating our solver with pops
    # Gap: pyro vortex technique (distinct from standard pyro, not in skill)
    "https://www.youtube.com/watch?v=BFZ3tItjKn8",   # 76 starting the smoke vortex
    "https://www.youtube.com/watch?v=FAE7gVev-ss",   # 78 building the vortex dop network

    # Houdini Renascence Program 1.0 (~H19, Solaris/Karma + Nuke comp)
    # Module I — one intro per week
    "https://www.youtube.com/watch?v=Mq1snWFUBj0",   # mod I w01 — first project, scattering basics
    "https://www.youtube.com/watch?v=Mjw4gT36Ub4",   # mod I w02 — scattering pt2, Megascans instances
    "https://www.youtube.com/watch?v=hEcmhhNlpzY",   # mod I w03 — intro to volumes / clouds
    "https://www.youtube.com/watch?v=9S5YABmK_eU",   # mod I w04 — intro to particles
    "https://www.youtube.com/watch?v=Fo3HaNq9f8M",   # mod I w05 — POP fluid / FLIP intro
    "https://www.youtube.com/watch?v=XPDsqVutqDw",   # mod I w06 — intro to grains
    # Module II — one intro per week
    "https://www.youtube.com/watch?v=vQSQgkSvm8g",   # mod II w01 — basic bullet sim + Voronoi clustering
    "https://www.youtube.com/watch?v=tC3H8wBaytE",   # mod II w02 — multi-object destruction
    "https://www.youtube.com/watch?v=cvAuweF1fvg",   # mod II w03 — multi-material fracture (glass/wood)
    "https://www.youtube.com/watch?v=uPPW2sI_oyw",   # mod II w04 — concrete + metal destruction

    # Houdini Renascence Program 2.0 (~H19-H20, advanced RBD + Vellum characters)
    # Module I intros
    "https://www.youtube.com/watch?v=ZYFlDsFBxhA",   # mod I w01 — city ground destruction intro
    "https://www.youtube.com/watch?v=G1JI3ACUZN4",   # mod I w02 — bus stop metal/wood/glass intro
    "https://www.youtube.com/watch?v=QkzF0SC76qY",   # mod I w03 — car destruction intro
    "https://www.youtube.com/watch?v=w9p4zfurT2A",   # mod I w04 — car glass + render intro
    # Gap: active attribute for staged destruction (critical RBD technique, absent from skill)
    "https://www.youtube.com/watch?v=VXkmQAGzBbA",   # mod I w01 09 — setting the active attribute
    # Gap: post-sim point deform on destruction geometry (not covered)
    "https://www.youtube.com/watch?v=XFOd1dy92Eg",   # mod I w02 15 — starting post sim setup
    "https://www.youtube.com/watch?v=oZh_MAnZyaQ",   # mod I w02 16 — point deforming metal and glass
    "https://www.youtube.com/watch?v=R-ay-5fX_Os",   # mod I w02 17 — rbddisconnectedfaces fix
    # Module II intros
    "https://www.youtube.com/watch?v=Y00rlBFqpxQ",   # mod II w01 — Vellum character intro
    "https://www.youtube.com/watch?v=161Gcdsi6Nw",   # mod II w02 — cloth draping intro
    "https://www.youtube.com/watch?v=F2vdSX1Dzgk",   # mod II w03 — creature mouth deformation intro
    "https://www.youtube.com/watch?v=SlbMugY762Q",   # mod II w04 — Vellum grains intro
    # Gap: Vellum fundamentals (biggest gap — dop-nodes.md lists nodes but no tutorial exists)
    "https://www.youtube.com/watch?v=LKhBUByCqJw",   # mod II w01 02 — introduction to vellum
    "https://www.youtube.com/watch?v=pxWRHQjHpNk",   # mod II w01 04 — tetrahedral soft bodies
    "https://www.youtube.com/watch?v=aUkXMjjLT-k",   # mod II w01 06 — updating the rest blend
    "https://www.youtube.com/watch?v=dfD5FUdMCTc",   # mod II w03 06 — breaking welds and constraints

    # Bridge Destruction in Houdini (~H18-H19, Mantra, Vellum cables)
    # One intro per week
    "https://www.youtube.com/watch?v=9ocqYW1XHk4",   # w01 — road + metal fracture intro
    "https://www.youtube.com/watch?v=IoxlDdh5OPg",   # w02 — cable sims intro
    "https://www.youtube.com/watch?v=OnBsOG4SwIU",   # w03 — car scatter + RBD intro
    "https://www.youtube.com/watch?v=GQSxmuvXsvM",   # w04 — debris + pyro intro
    "https://www.youtube.com/watch?v=_UqQ526rOzI",   # w05 — materials + Mantra render intro
    # Gap: RBD Configure node deep dive (mentioned in recipe but no tutorial)
    "https://www.youtube.com/watch?v=dIBS14jw25k",   # w01 11 — rbd configure
    # Gap: guided simulations (entirely absent from skill)
    "https://www.youtube.com/watch?v=9qkYzPC9IKM",   # w02 03 — starting the guided sim
    "https://www.youtube.com/watch?v=ykTr02tft_k",   # w02 04 — finishing the guided cable sim
    # Gap: Vellum wire + breaking threshold
    "https://www.youtube.com/watch?v=cecNdA8cLTo",   # w02 07 — starting vellum wire sim
    "https://www.youtube.com/watch?v=9TNDsfFNoq4",   # w02 08 — strong constraints + breaking threshold
    # Gap: cull by speed (velocity-based particle culling, not documented)
    "https://www.youtube.com/watch?v=UFrvmv0rwQI",   # w04 06 — cull by speed

    # Table Top Food Simulation in Houdini (~H18-H19, FLIP + RBD, Mantra/Principled)
    # One intro per week
    "https://www.youtube.com/watch?v=RQBrvngXM6Y",   # w01 — food scatter + RBD intro
    "https://www.youtube.com/watch?v=C7vpFqAZClk",   # w02 — SOP deformation (yogurt) intro
    "https://www.youtube.com/watch?v=yP83h4H-lgU",   # w03 — FLIP sauce intro
    "https://www.youtube.com/watch?v=S4VjdIf5BKQ",   # w04 — FLIP milk pour intro
    "https://www.youtube.com/watch?v=AysHWEqNhwg",   # w05 — RBD + FLIP combined intro
    # Gap: velocity-driven SOP deformation (unique technique not in skill)
    "https://www.youtube.com/watch?v=IuvtudgbzLw",   # w02 05 — deforming with velocity
    # Gap: FLIP viscosity + surface tension in depth
    "https://www.youtube.com/watch?v=9N9CavpgoB4",   # w03 04 — adding viscosity
    "https://www.youtube.com/watch?v=H56dPbE3S2E",   # w03 11 — meshing (VDB layer separation)
    "https://www.youtube.com/watch?v=1yb3mindncw",   # w04 11 — viscosity and surface tension
]
# ─────────────────────────────────────────────────────────────────────────────


def already_ingested_urls():
    """Return the set of YouTube URLs already present in tutorials/INDEX.md."""
    index_path = SKILL_DIR / "tutorials" / "INDEX.md"
    if not index_path.exists():
        return set()
    content = index_path.read_text(encoding="utf-8-sig")
    # Match lines like: - **URL:** https://www.youtube.com/watch?v=XXXXXXXXXXX
    found = re.findall(r"https://www\.youtube\.com/watch\?v=([\w-]+)", content)
    # Normalise to full URL for comparison
    return {f"https://www.youtube.com/watch?v={vid}" for vid in found}


def main():
    parser = argparse.ArgumentParser(description="Batch ingest new tutorials")
    parser.add_argument("--skip-video", action="store_true")
    parser.add_argument("--whisper-model", default="base",
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--dry-run", action="store_true",
                        help="Show which URLs are new without ingesting")
    args = parser.parse_args()

    if not URLS:
        print("No URLs in URLS list. Add them to batch_ingest.py and re-run.")
        return

    done = already_ingested_urls()
    new_urls = []
    skipped = []
    for url in URLS:
        # Normalise: strip extra params (&pp=..., &t=..., etc.) for comparison
        vid_match = re.search(r"v=([\w-]+)", url)
        canonical = f"https://www.youtube.com/watch?v={vid_match.group(1)}" if vid_match else url
        if canonical in done:
            skipped.append(url)
        else:
            new_urls.append(url)

    print(f"Total URLs: {len(URLS)}  |  Already ingested: {len(skipped)}  |  New: {len(new_urls)}")
    if skipped:
        print("Skipping (already in INDEX.md):")
        for u in skipped:
            print(f"  skip: {u}")

    if args.dry_run:
        print("\nDry run — no ingestion performed.")
        print("New URLs that would be ingested:")
        for u in new_urls:
            print(f"  {u}")
        return

    if not new_urls:
        print("Nothing new to ingest.")
        return

    print(f"\nIngesting {len(new_urls)} new URL(s)...\n")
    successes, failures = [], []

    for i, url in enumerate(new_urls, 1):
        print(f"\n[{i}/{len(new_urls)}] {url}")
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
