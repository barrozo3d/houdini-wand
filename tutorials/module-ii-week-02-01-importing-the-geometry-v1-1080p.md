---
title: module ii   week 02   01   importing the geometry v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=tC3H8wBaytE
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [dop, sop, rbd, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-02-01-importing-the-geometry-v1-1080p/
frame_count: 4
---

# module ii   week 02   01   importing the geometry v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=tC3H8wBaytE)
**Author:** The VFX School Archive
**Duration:** 4m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right, so let's get started. I'm going to create a new project and this will be module module two, week two. Okay, and this goes into my D drive. All right. So, just go ahead and find that and then drag in the Brooklyn building. So, that's an Alembic, so we'll drop it in here. So, I've already um extracted this. It's a compressed file. And then inside you've got these different LODs. Um all the same building with different um level, you know, amounts of polygons inside. So, I'm going to be using a LOD two. You can use you know, to get the same results you'd do the same, but you can play around with the others. Uh so, let's grab a geometry node and we'll call this uh building. Okay, let's press P to get our parameters. Great, and then dive inside. Press I. Um grab an Alembic. Okay, and I just remembered to save the project. Save the hip file. Okay, so uh what are we doing here? So, reverse gravity. Or yeah. Kind of like attractor beam thing. Um and then we'll go into hip, Alembic version one. I'm going to use, like I said, LOD two. So, if we press uh space bar and F, you can see that it's way too big. So, um as per usual, we need to make this smaller. It'...

**Frame:** tutorials\frames\module-ii-week-02-01-importing-the-geometry-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Importing a multi-LOD Brooklyn building Alembic asset for a multi-object destruction shot, with an LOD strategy that simulates at low resolution and renders at high resolution.

### Summary
Imports a compressed Alembic asset with multiple LODs; extracts it and selects LOD2 as the balance between polygon detail and simulation speed. Creates a geometry node named "building," adds an Alembic SOP, and scales the import to 0.01 since the building was modelled at real-world scale in meters and needs shrinking for the Houdini scene. The week's concept is a reverse-gravity / attractor-beam effect, where building chunks rise upward in an organized way suggesting anti-gravity or an energy beam. Establishes the LOD strategy: simulate with LOD2/LOD3 (fewer polygons) and render with LOD0/LOD1 via a post-sim copy-back step.

### Key Steps
1. [Import Alembic] Extract the compressed multi-LOD Brooklyn building asset
2. [`Alembic SOP`] Create a "building" geometry node and import LOD2 for simulation
3. [`Transform SOP`] Scale the import by 0.01 to correct real-world-meter to Houdini-unit mismatch
4. [Reverse gravity setup] Configure the RBD sim so chunks rise upward in an organized pattern
5. [LOD strategy] Plan to simulate on LOD2/LOD3 and swap to LOD0/LOD1 for the final render pass

### Houdini Nodes / VEX / Settings
- `Alembic SOP` — imports the multi-LOD building asset
- `Transform SOP` — corrects scale mismatch (real-world meters vs. Houdini scene units) via a 0.01 multiplier
- LOD strategy — simulate at low resolution, swap to high resolution for render via a post-sim copy-back

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)

---

## Related Tutorials
- [Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — the preceding week's RBD/constraint fundamentals
- [Splitting by Material](module-ii-week-03-01-splitting-by-material-v1-1080p.md) — the following week's multi-material fracture
- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — a parallel multi-piece RBD destruction setup
