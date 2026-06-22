---
title: module ii   week 02   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=161Gcdsi6Nw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, cloth, simulation, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-02-01-introduction-v1-1080p/
frame_count: 4
---

# module ii   week 02   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=161Gcdsi6Nw)
**Author:** The VFX School Archive
**Duration:** 1m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, welcome to week two of the course of the Vellum course. So, this week we're focusing on clothes on the fabric. I'm starting out by draping the cloth onto the onto the body. So, using the T-pose of the model to you know, fit the clothes accurately as if you know, they're they're so they're sitting correctly at the beginning of the simulation. We're also going to be you know, preparing the the geometry so it's good for simulation. Making sure that the geometry is good. The you know, the we're going to be using remeshes and stuff like that. Setting up groups and things as well ready for the constraints. And then we're also going to be looking at tearing clothes. So, you know, pre-cutting the the cloth ready for pre-fracturing I suppose we should we should say ready for the simulation to tear them apart. Again, looking at welding them together. Stitching and attaching to geometry stuff like that. Obviously, setting up the constraints for the clothes themselves. We'll be actually simulating the drape. So, you know, we'll be doing that seamlessly and I think we do that in the Vellum sub-solver. And then a little bonus at the end where I kind of worked out ...

**Frame:** tutorials\frames\module-ii-week-02-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Cloth draping workflow: fitting clothing to the body in T-pose before simulation, with remeshing, constraint grouping, tearing and stitching covered as the week's core Vellum cloth techniques.

### Summary
Workflow begins by draping cloth in T-pose: fitting the clothing geometry to the body before the main simulation so clothing sits correctly at frame 0. Geometry preparation includes a Remesh SOP to triangulate cloth (Vellum produces more natural folds on triangles), group creation for constraint regions, and pre-fracturing cloth with cut lines ready for the simulation to tear along. Key Vellum cloth techniques covered: weld constraints (stitching seams), attachment constraints (pinning cloth to the body), tearing (enabling a break threshold on cloth constraints), and the Vellum sub-solver for draping in rest pose. A bonus topic covers handling cloth intersection at the start of simulation.

### Key Steps
1. [T-pose drape] Fit clothing geometry to the body before the main simulation begins
2. [`Remesh SOP`] Triangulate cloth geometry for natural Vellum folding
3. [Group creation] Define constraint regions (e.g. seams, pin areas) via groups
4. [Pre-fracture cut lines] Add tear lines to the cloth ahead of simulation
5. [Weld constraints] Stitch seams together
6. [Attachment constraints] Pin cloth to the body where needed
7. [Tearing] Enable break threshold on selected cloth constraints
8. [Intersection handling] Resolve cloth/body intersection present at simulation start

### Houdini Nodes / VEX / Settings
- `Remesh SOP` — triangulates cloth for better Vellum fold behaviour
- Vellum weld constraints — stitches seams together
- Vellum attachment constraints — pins cloth to underlying body geometry
- Break threshold (tearing) — enables cloth constraints to fail and tear under stress
- Vellum sub-solver — used here specifically for draping cloth into rest pose before the main sim

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)

---

## Related Tutorials
- [Vellum Module Intro: Crocodile Attack Overview](module-ii-week-01-01-introduction-v1-1080p.md) — the preceding week's broader Vellum overview
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the following week's combined cloth+soft-body assembly
- [Breaking Welds and Constraints](module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p.md) — the gap-filler detailing animated constraint breaking for this same cloth setup
