---
title: week 05   01 intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=_UqQ526rOzI
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rendering, mantra, volumes, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/week-05-01-intro-v1-1080p/
frame_count: 4
---

# week 05   01 intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=_UqQ526rOzI)
**Author:** The VFX School Archive
**Duration:** 0m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to the final week of the bridge destruction course. This week we are looking at rendering so we're going to be bringing in a load of shaders and cameras from a separate scene that we will provide to you and then we're going to look at kind of randomizing some colors on the on the cars and well the vehicles really because there are trucks as well. We're going to be generating some fog volumes and then rendering all of that, applying lights as well. Obviously we're using a HDR and a distant light bringing everything into nuke and just doing a nice simple comp at the end but resulting in a really dramatic beautiful render.

**Frame:** tutorials\frames\week-05-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-five overview: bringing the full bridge destruction scene to a final render in Mantra — importing shaders and cameras, randomising vehicle colours, generating fog volumes, lighting with HDRI and distant light, and compositing in Nuke.

### Summary
The final week of the Bridge Destruction course focuses on rendering. Pre-built shaders and cameras are merged in from a provided scene file. Vehicle colours are randomised procedurally to add visual variety. Fog volumes are generated to set atmosphere, then everything is lit with an HDRI and a distant light. The Mantra render passes are taken into Nuke for a straightforward but dramatic composite result.

### Key Steps
1. [`File Merge`] Import shaders and cameras from a provided Houdini scene
2. [`Attribute Randomize / Wrangle`] Randomise colour attributes across car/truck pieces
3. [`Volume SOP / Fog Volume`] Generate atmospheric fog volumes
4. [`Mantra ROP`] Configure and launch the Mantra renderer
5. [`Environment Light`] Set up HDRI sky lighting
6. [`Distant Light`] Add directional sunlight
7. [Nuke comp] Import render passes and produce final composite

### Houdini Nodes / VEX / Settings
- `Mantra ROP` — the render output operator driving Mantra
- `Environment Light` — sphere light accepting an HDRI map for image-based lighting
- `Distant Light` — parallel sun-direction light
- Volume SOP (fog) — creates low-density atmospheric volumes for depth and haze
- Attribute randomise — randomises `Cd` or shader parameter per piece for colour variation

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — the debris/pyro sims being rendered this week
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — the RBD elements feeding into this render
- [Module I Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — parallel rendering setup from the earlier course
