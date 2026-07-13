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

    # ── cgside channel (@cgside) — Houdini tutorials ─────────────────────────────
    # Batch added 2026-07-13. Full channel scraped (281 videos), filtered to
    # Houdini-only content: 164 matched explicit title keywords (houdini, vex,
    # cops, vellum, kinefx, solaris, karma, mardini, tops, hda, usd), plus 31
    # more confirmed Houdini via description check (channel signs almost all
    # Houdini videos "My procedural Houdini courses" / #houdini even when the
    # title itself doesn't say so). Excluded: Maya/Bifrost/Arnold/Substance
    # Painter/Zbrush/3ds Max/Photoshop videos from the channel's earlier years,
    # plus one no-info showreel and one no-DCC-mentioned "quick tip" video.
    "https://www.youtube.com/watch?v=ntf3zMAez50",  # Why you need to learn vex in Houdini #1
    "https://www.youtube.com/watch?v=f5vt8n8CB-U",  # Chocolate break rig and Liquid Stretch in Houdini Free Lesson
    "https://www.youtube.com/watch?v=hHLH7pr_eZo",  # Tuna Can | procedural modeling and rig with KineFX
    "https://www.youtube.com/watch?v=zWlJ8QLkFH4",  # Houdini techniques to improve your level
    "https://www.youtube.com/watch?v=QPiEZM1o-ME",  # Scissor Lift rig in Houdini
    "https://www.youtube.com/watch?v=7J-hDF0H6ck",  # Mechanical rigging in Houdini - Attaching custom controls
    "https://www.youtube.com/watch?v=AGTOukqBmhU",  # Coin spin | Sops vs Vex vs OpenCL
    "https://www.youtube.com/watch?v=JMfMxHi48Zs",  # Essential Procedural Techniques in Houdini
    "https://www.youtube.com/watch?v=NkVT9NtRMk0",  # Camera Match tool for Houdini 21
    "https://www.youtube.com/watch?v=GQMsl6TiFXY",  # Layered Textures in Karma
    "https://www.youtube.com/watch?v=ITq2EBJ5nIw",  # RBD Procedural Animations in Houdini | Mardini 2026
    "https://www.youtube.com/watch?v=VjX9v92PJNU",  # Procedural Food in Houdini | Mardini 2026
    "https://www.youtube.com/watch?v=62Mo7udZM_o",  # Creating Cliff Shapes in Cops | Free Lesson
    "https://www.youtube.com/watch?v=nCS6sy53_aw",  # Volume rays in Cops for Houdini 21
    "https://www.youtube.com/watch?v=oEIXFY-Kxdk",  # Creating assets from default geometry in Houdini 21
    "https://www.youtube.com/watch?v=eqXFo0pxdXc",  # Orient UVS like a PRO in Houdini 21
    "https://www.youtube.com/watch?v=AB9rwjcX0Xg",  # Basic Procedural Texturing with Cops in Houdini 21
    "https://www.youtube.com/watch?v=rvDsbo3slXc",  # Roasting my Houdini Setups #1
    "https://www.youtube.com/watch?v=bTA8XwTEcRg",  # Scatter shapes in cops randomly without overlap
    "https://www.youtube.com/watch?v=F_xggmIONZ4",  # Procedural Environments in Houdini | Patreon February '26 Free Lesson
    "https://www.youtube.com/watch?v=Quj03TwHAN4",  # Direct vs Procedural in Houdini
    "https://www.youtube.com/watch?v=TWQvmqhRX3M",  # Think Procedural Think Houdini
    "https://www.youtube.com/watch?v=yeA_0tL3GlU",  # Double Sided Leaf Animation using Cops in Houdini 21
    "https://www.youtube.com/watch?v=ZDlL81gmafE",  # Matrix color transform in cops for Houdini 21
    "https://www.youtube.com/watch?v=D6449n2Pvcc",  # Procedural Duct Tape in Houdini
    "https://www.youtube.com/watch?v=DV0ABu_-yvc",  # Tips and Tricks to level up your Houdini Skills
    "https://www.youtube.com/watch?v=iZwfnJGQUlI",  # Procedural Materials in Houdini 21 | Patreon December '25  - Free Lesson
    "https://www.youtube.com/watch?v=SwtUCds8UCY",  # Procedural environment assets in Houdini 21
    "https://www.youtube.com/watch?v=RchQ9K5QXtI",  # CGI Integration | The Indie Way with Houdini(USD) and Nuke
    "https://www.youtube.com/watch?v=FxrSPbnI3tI",  # New Houdini Course  - Procedural Product Shots | Part 1 Free
    "https://www.youtube.com/watch?v=gv_gXOSjCN0",  # Tips and tricks in Houdini 21
    "https://www.youtube.com/watch?v=0C8ek1aDe8o",  # Optimizing Baked Trees with Instancing in Houdini
    "https://www.youtube.com/watch?v=M8odmzpj2dc",  # Bring your 3D renders to life with Houdini - Patreon October '25 Trailer
    "https://www.youtube.com/watch?v=h6wt3KJy2W4",  # Handy Houdini Tips | Vellum, UVS, Modeling and More
    "https://www.youtube.com/watch?v=Nmnf_3mp1OU",  # Procedural Favela in Houdini  | Tips and Tricks
    "https://www.youtube.com/watch?v=pbwra2esNqc",  # Heightfields and Cops workflow in Houdini 21 -  Patreon September 25 Trailer
    "https://www.youtube.com/watch?v=ha85low9Bmo",  # Houdini 21 | Opacity vs Stencil vs Geometry
    "https://www.youtube.com/watch?v=1QTfNMlvF1E",  # Daily dose of Houdini Tips | Sweep secrets, opencl textures and more
    "https://www.youtube.com/watch?v=CHySFnWfKLk",  # Dusty Bottles - Bridging procedural workflows in Houdini and Solaris
    "https://www.youtube.com/watch?v=Eb4KIaOJT5Y",  # Procedural Brick Wall with COPS  - Patreon August Trailer
    "https://www.youtube.com/watch?v=KCy4Sw3nbcQ",  # Making Trash in Houdini
    "https://www.youtube.com/watch?v=lT0b8D6LmtM",  # Houdini tips to save the day
    "https://www.youtube.com/watch?v=NxWpxFDaSJE",  # No VEX challenge #1   Procedural Water Tower
    "https://www.youtube.com/watch?v=udPSR7Gjp9Y",  # Jellyfish Procedural Animation with Houdini and Vex | Patreon July Trailer
    "https://www.youtube.com/watch?v=050av2q2ihg",  # Procedural Boat in Houdini
    "https://www.youtube.com/watch?v=fDV8SQegEDc",  # Quick object merge with Python in Houdini
    "https://www.youtube.com/watch?v=oDXQsMo2aaQ",  # Vex Quick Tips #4 - Pineapple Crown
    "https://www.youtube.com/watch?v=ARJFJC79k3k",  # Interactive Tools with Houdini Python States | Draw pts on geo
    "https://www.youtube.com/watch?v=Mljby-SKlUI",  # Creating a Procedural Rock Wall with Houdini | Patreon May - Trailer
    "https://www.youtube.com/watch?v=O_oxVn-YVB0",  # From sops to final render with Karma
    "https://www.youtube.com/watch?v=kxg05cfgdQI",  # Quick CG integration with Houdini and Karma
    "https://www.youtube.com/watch?v=JCdVrNwiMGk",  # Procedural Buildings in Houdini | Tips and Tricks
    "https://www.youtube.com/watch?v=2HYYRRW7tws",  # Advanced Waterdrops Setup in Houdini | Patreon April Trailer
    "https://www.youtube.com/watch?v=t9ldXkD7oqA",  # Texture Projection Tool for Houdini 20.5
    "https://www.youtube.com/watch?v=suiPD-s1I9U",  # Procedural Graffiti in Houdini and COPS #mardini
    "https://www.youtube.com/watch?v=-lVYE0LRu6w",  # Procedural UVS and Texturing in COPS | Patreon March Trailer
    "https://www.youtube.com/watch?v=h6MN80ka4Vg",  # Environments in Houdini | Part 5 - Solaris and rendering with Karma
    "https://www.youtube.com/watch?v=7PHYAnZbTvM",  # Vex quick tips #2 | Iterating over numbers
    "https://www.youtube.com/watch?v=SHAgvzji9vM",  # Vex quick tips | Overhang look with channel ramps
    "https://www.youtube.com/watch?v=08lvfWum09M",  # Procedural Modeling, Rigging and Animation with Houdini | Patreon February Trailer
    "https://www.youtube.com/watch?v=8RIneeMCbAg",  # Procedural Modeling with VEX, VDB and Vellum
    "https://www.youtube.com/watch?v=mL2TkAB_Rqc",  # Procedural Pizza in COPS
    "https://www.youtube.com/watch?v=xm9d-Un3Hrg",  # Quick CGI Integration with Houdini and Solaris
    "https://www.youtube.com/watch?v=cXbdFwd3u9o",  # Environments in Houdini | Part 4 - Vines, Rocks and Fog
    "https://www.youtube.com/watch?v=enW-PwgBWE4",  # Building Tools in Houdini with vex and python | Flatten Loop
    "https://www.youtube.com/watch?v=FvM09fA0cKY",  # Environments in Houdini  | Part 3  - Vegetation with Simple Tree Tools
    "https://www.youtube.com/watch?v=kPtCgMWIBj4",  # Environments in Houdini  | Part 2  - Stone Bridge
    "https://www.youtube.com/watch?v=ER_W3w3SkGk",  # Environments in Houdini | Part 1 -  Heightfields
    "https://www.youtube.com/watch?v=aaNiFlx6Vi0",  # Product Shot in Houdini and Solaris | Part 2 | Patreon December
    "https://www.youtube.com/watch?v=R3ClxIiqxag",  # How to (not) bake brownies in Houdini
    "https://www.youtube.com/watch?v=24vjgnyZRTw",  # Houdini Mini Course  |  Cops, Vex and Karma
    "https://www.youtube.com/watch?v=Fiw_NedtssQ",  # Vex Problem Solving in Houdini
    "https://www.youtube.com/watch?v=Joe8Cu40_as",  # Product Shot in Houdini Part 1 | Patreon November
    "https://www.youtube.com/watch?v=O6T5eVYJHsA",  # Wood Barrel Texturing in COPS
    "https://www.youtube.com/watch?v=-1kxDkdmcV4",  # Beginner Procedural Modeling/UVS Tutorial in Houdini
    "https://www.youtube.com/watch?v=xz1oNZGq7P0",  # Spiral Splash Tutorial in Houdini
    "https://www.youtube.com/watch?v=05uuRimyHfY",  # Tiling Patterns with COPS and SOPS
    "https://www.youtube.com/watch?v=bM7hzXqBq0Y",  # Custom patterns with COPS |  October Patreon Exclusive
    "https://www.youtube.com/watch?v=7ZJeWIFYSxg",  # Procedural UV's In Houdini
    "https://www.youtube.com/watch?v=c193tsyLH-0",  # Enhance your renders in Houdini
    "https://www.youtube.com/watch?v=conZuTxHnoc",  # Houdini Beginner Tutorial | Creating a perfume bottle
    "https://www.youtube.com/watch?v=VL5N4jKidVA",  # Tips and Tricks for a better Houdini Time
    "https://www.youtube.com/watch?v=c_t8JwyHJrA",  # Model and Rig a Wardrobe in Houdini
    "https://www.youtube.com/watch?v=mcP3wLo1lIQ",  # Cliff Face in Houdini
    "https://www.youtube.com/watch?v=P-2FPlUJO60",  # Resample Color Ramps in Houdini
    "https://www.youtube.com/watch?v=3bP9uKsn-9U",  # Procedural Shading with COPS and Karma - Preview
    "https://www.youtube.com/watch?v=1SXCz_Ta4Lc",  # UVW randomizer in karma
    "https://www.youtube.com/watch?v=HDIIwy11otU",  # Procedural Helical Column in Houdini
    "https://www.youtube.com/watch?v=ag7I-FK4TF0",  # VDB Procedural Modeling in Houdini
    "https://www.youtube.com/watch?v=k7-5PaOccYc",  # Procedural Modeling with Houdini 20.5 Tools
    "https://www.youtube.com/watch?v=8iK3GD3yeCE",  # Procedural Leaking Texture in Houdini 20.5
    "https://www.youtube.com/watch?v=wgStaCuEglI",  # Procedural tips and tricks in Houdini 20.5
    "https://www.youtube.com/watch?v=meX4fLnITR0",  # The Donut Tutorial in Cops | Houdini 20.5
    "https://www.youtube.com/watch?v=rlrWEjoO8jQ",  # Shoe Laces in Houdini | Vex and Vellum
    "https://www.youtube.com/watch?v=Lm5cG2XxRwU",  # Designer like Materials in Cops | Houdini 20.5
    "https://www.youtube.com/watch?v=xOeZncLWztc",  # Displacement maps in cops | Houdini 20.5
    "https://www.youtube.com/watch?v=_C6-g1C--ws",  # Useful Vex snippets | Houdini tips and tricks
    "https://www.youtube.com/watch?v=T7CoIJg8Dx4",  # Procedural workflow | Vex, Kinefx, UV's and more
    "https://www.youtube.com/watch?v=8hUjc7BEI9g",  # Procedural and Organic Modeling in Houdini
    "https://www.youtube.com/watch?v=t1QemBG462g",  # Direct and Procedural Modeling in Houdini
    "https://www.youtube.com/watch?v=PcP9Eieij1g",  # Procedural techniques in Houdini
    "https://www.youtube.com/watch?v=ObBXMX-VH90",  # Using Substance Designer nodes for Houdini
    "https://www.youtube.com/watch?v=Sr7iwTjwo2E",  # Vellum Typography in Houdini
    "https://www.youtube.com/watch?v=c1tO7581nOM",  # Sushi Modeling and Rendering in Houdini
    "https://www.youtube.com/watch?v=4PjTMogFWqQ",  # Chocolate Swirl Effect with Houdini
    "https://www.youtube.com/watch?v=iQql20c4Gio",  # Quality of life tips in Houdini
    "https://www.youtube.com/watch?v=6wqRXRV7oxk",  # Kinefx and Vellum Fluid in Houdini
    "https://www.youtube.com/watch?v=cRr4R54DRKw",  # Houdini and Karma tips and tricks
    "https://www.youtube.com/watch?v=kdpeMWXIGrY",  # MaterialX and Karma | procedural networks
    "https://www.youtube.com/watch?v=Y-CjDhFmclQ",  # Let's make soap! Houdini and Karma beginner course
    "https://www.youtube.com/watch?v=peBkuU0Es1Q",  # Still Life Scene Breakdown | Houdini tips
    "https://www.youtube.com/watch?v=qtzO_NoQbtE",  # Hard Surface Techniques in Houdini
    "https://www.youtube.com/watch?v=zItss8TuZMo",  # Houdini Tips | Tileable Noises, Cam from Stage, TOPS and more
    "https://www.youtube.com/watch?v=S5sKJaPU7C8",  # Husk Chair - Modeling and Simulating in Houdini - Trailer
    "https://www.youtube.com/watch?v=FLWrmz8QPZQ",  # Groups Patterns in Houdini
    "https://www.youtube.com/watch?v=2Vw6jvHrnBw",  # Houdini Tips | Expressions, VEX, Recursive Cuts and more
    "https://www.youtube.com/watch?v=m00nko87HeI",  # Houdini Tips - Procedural UV's, Channel Packing and more
    "https://www.youtube.com/watch?v=at27qaTVrFc",  # Modern Furniture Modeling in Houdini
    "https://www.youtube.com/watch?v=fgUIMtGLIrI",  # Houdini to Unreal: HDA Setup and Workflow
    "https://www.youtube.com/watch?v=fF01Lyg_G48",  # Houdini Heightfields and Cliffs
    "https://www.youtube.com/watch?v=WwwTwtlKm0A",  # Houdini tips : Solaris, VDB's , COPS and More
    "https://www.youtube.com/watch?v=6hbyMIxU1oI",  # Bake room maps in karma from HDRI interiors H20
    "https://www.youtube.com/watch?v=M6W_EP48BaI",  # Custom Procedural Materials with Houdini and Karma
    "https://www.youtube.com/watch?v=68WNINd8vE0",  # Procedural Anisotropy in Karma
    "https://www.youtube.com/watch?v=d2Qgcbzup2s",  # Modeling Assets With Vellum
    "https://www.youtube.com/watch?v=T-_L6BeLSkg",  # Vellum Balloon Text in Houdini
    "https://www.youtube.com/watch?v=lcgNaIicsZU",  # Procedural Fries with Mtlx and Karma XPU
    "https://www.youtube.com/watch?v=Mxg-zhwdNlE",  # Time saving tips in Houdini
    "https://www.youtube.com/watch?v=5jfjCGDdbqs",  # Infinite Mirror in Karma XPU
    "https://www.youtube.com/watch?v=5Cv1SJRm538",  # Procedural Problem Solving in Houdini
    "https://www.youtube.com/watch?v=cvTnsmUNw3w",  # Procedural Ice cream Swirl in Houdini
    "https://www.youtube.com/watch?v=ItIlLC6mlF4",  # Houdini Procedural Tips | Variants, Concentric Shapes and Step Orient
    "https://www.youtube.com/watch?v=r2SSCwpgnVQ",  # Procedural Shading Tips #2 in Houdini 20
    "https://www.youtube.com/watch?v=NHD3VbE2y00",  # Houdini 20 Procedural Shading Features
    "https://www.youtube.com/watch?v=BUJg3ILS1Aw",  # Export a full scene from Houdini to Unreal
    "https://www.youtube.com/watch?v=rvmDcbSMXh8",  # Procedural Roof Tiles in Houdini
    "https://www.youtube.com/watch?v=g6PQu2FRKGo",  # Compiling nested loops in Houdini
    "https://www.youtube.com/watch?v=Qs5Sk6QPGcM",  # Procedural Wicker Basket in Houdini
    "https://www.youtube.com/watch?v=bgUI52CFMLU",  # Procedural Tips #3 VEX Shading and Loops
    "https://www.youtube.com/watch?v=VJ4AnxgCvQU",  # Creating Procedural Environment Assets in Houdini
    "https://www.youtube.com/watch?v=n-UAPewvMgQ",  # Cleaning fractured geometry in Houdini
    "https://www.youtube.com/watch?v=LwbK0Z_y77Y",  # Church Ruins - Houdini Procedural Modeling Course | Trailer
    "https://www.youtube.com/watch?v=iSIXaa3rknU",  # Quick Rock Cliff Setup in Houdini
    "https://www.youtube.com/watch?v=Kc_6yws1AH8",  # Procedural Modeling tips in houdini #2
    "https://www.youtube.com/watch?v=015fds0mdyk",  # RBD rock surfaces with Houdini
    "https://www.youtube.com/watch?v=WAyk2xCn5rs",  # Cliff texturing with karma and material X
    "https://www.youtube.com/watch?v=RQ3kSr5u16A",  # Python multi asset loader in Houdini
    "https://www.youtube.com/watch?v=N5DN6SwYFVs",  # Python in Houdini | Absolute to relative paths
    "https://www.youtube.com/watch?v=0-oFYKvYucA",  # Procedural Modeling of a Stadium in Houdini - Part 1
    "https://www.youtube.com/watch?v=rVduzdrKYZg",  # Houdini tips and tricks #2
    "https://www.youtube.com/watch?v=I3mf1AQCxc0",  # Custom triplanar for karma | Patreon
    "https://www.youtube.com/watch?v=CzgcCkVy50o",  # Procedural shading with karma  | Patreon exclusive
    "https://www.youtube.com/watch?v=9wMJWyni_Uc",  # Opacity maps vs Geo in Karma
    "https://www.youtube.com/watch?v=fSouWuGd_Tg",  # Procedural assets and shading with Houdini and MaterialX
    "https://www.youtube.com/watch?v=zZBkR8rk-_s",  # Python in Houdini  | Create a texture importer for Solaris
    "https://www.youtube.com/watch?v=kAXUfg2FbYY",  # 5 Tips and Tricks for Modeling in Houdini
    "https://www.youtube.com/watch?v=OWMKqhVaFF8",  # Controlling instance probability in Solaris
    "https://www.youtube.com/watch?v=u7SGkPTaJKs",  # Christmas lights vex animation in Houdini
    "https://www.youtube.com/watch?v=utIfflheFqc",  # Quick color jitter with karma
    "https://www.youtube.com/watch?v=v3irz0OHw48",  # Creating 3D Environments with Houdini and Arnold - Trailer
    "https://www.youtube.com/watch?v=2f_40GhnBXI",  # Environment creation with Solaris in Houdini
    "https://www.youtube.com/watch?v=nGKGXKw4_Zw",  # Environment Creation with Houdini - Part 1
    "https://www.youtube.com/watch?v=-5cycyb5m-E",  # Procedural Bricks with Houdini
    "https://www.youtube.com/watch?v=L3Rvvv6pZ_8",  # Procedural Modeling  | First steps with Houdini
    "https://www.youtube.com/watch?v=c90ervPv5ro",  # Cookies and chocolate | Modeling, shading and Sim
    "https://www.youtube.com/watch?v=Ba3Py4lodL8",  # All* the Procedural Modeling tricks in one video
    "https://www.youtube.com/watch?v=JO0V0xTDh9w",  # Procedural Pineapple | Patreon June - Trailer
    "https://www.youtube.com/watch?v=tG8HSBblVk8",  # Chocolate Split  | Patreon January 25  | Trailer
    "https://www.youtube.com/watch?v=RbiH315adq8",  # Procedural Animation with RBD
    "https://www.youtube.com/watch?v=IOC8hPPWrGY",  # Procedural Grapes  | Patreon September  | Trailer
    "https://www.youtube.com/watch?v=CiFOWrTiaFM",  # Procedural Coffee Beans - Preview
    "https://www.youtube.com/watch?v=YLrE1Zww_uc",  # Procedural Cliff Techniques
    "https://www.youtube.com/watch?v=g6HyohwVR1s",  # Procedural Cookie - Model, Simulate and Render - Trailer
    "https://www.youtube.com/watch?v=bqyaPvWT5Gc",  # Environment Technical tips and tricks
    "https://www.youtube.com/watch?v=pTQGJM0k9b0",  # Procedural Hard Surface Modeling Tips
    "https://www.youtube.com/watch?v=XFOiCiljWh8",  # Procedural Tips: Flow Maps, RBD Emit and more
    "https://www.youtube.com/watch?v=7kUDLsNn0iA",  # Procedural UVs - UV Layout Node in Depth
    "https://www.youtube.com/watch?v=rzWUiyF9EJI",  # Procedural House Generator
    "https://www.youtube.com/watch?v=6GV1b8Ed_JI",  # Procedural Rock Formations  Part 2
    "https://www.youtube.com/watch?v=9bq2Zx5zcIk",  # Procedural Grapes and how to avoid intersections
    "https://www.youtube.com/watch?v=kpWtT6tPvP0",  # Procedural Champions League football in 2 minutes
    "https://www.youtube.com/watch?v=qS5uDc8EePQ",  # Add details with regions from image labs tool
    "https://www.youtube.com/watch?v=G4Fb8jKQ3WM",  # Roman Bridge - Procedural Asset Creation - Trailer
    "https://www.youtube.com/watch?v=rEn0ochILjU",  # Rock formations with heightfields
    "https://www.youtube.com/watch?v=TnujEWlFdfU",  # Procedural Rock Surfaces | Patreon Exclusive
    "https://www.youtube.com/watch?v=QEvlyVTk4Jw",  # Ruins randomized brick wall
    "https://www.youtube.com/watch?v=q-9cVBVMv2E",  # Procedural Rock Wall without intersections
    "https://www.youtube.com/watch?v=Ue-Wuo87YJI",  # Procedural tips | Heightfields and VDB
    "https://www.youtube.com/watch?v=U1c1-dbgUAk",  # Prodecural Cliffs with heighfields vdb and materialX
    "https://www.youtube.com/watch?v=WKs4KHfHpyA",  # Procedural VDB Cookies
    "https://www.youtube.com/watch?v=qzs3LnMeYEE",  # Patreon Exclusive  | Add side details to cliffs | Preview
    "https://www.youtube.com/watch?v=FK6IRzxYHiY",  # UV Randomizer - Texturing multiple objects
    "https://www.youtube.com/watch?v=j0s0HkBCaQQ",  # Quick asset creation with VDB
    "https://www.youtube.com/watch?v=fBhtlmCGrK4",  # VDB Procedural Cliffs
    "https://www.youtube.com/watch?v=rhRaQa-a8q4",  # Procedural Modeling tips for beginners
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
