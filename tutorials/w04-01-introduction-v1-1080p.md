---
title: w04   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=S4VjdIf5BKQ
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [flip, fluid, viscosity, surface-tension, meshing, vdb, rendering, arnold, beginner]
extraction_status: complete
frames_dir: tutorials/frames/w04-01-introduction-v1-1080p/
frame_count: 4
---

# w04   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=S4VjdIf5BKQ)
**Author:** The VFX School Archive
**Duration:** 1m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey guys and welcome to week four of the tabletop course. This week we're going to be simulating a strawberry colliding with milk. So we've got a kind of milk pouring in into the scene and then the strawberry colliding with that. Again we'll be using flip fluids in who do you need to do that. For this shot, Padley through the project I will be bringing in the new animation for the strawberry. So you can go ahead and use that from the beginning. We've got an animated strawberry for you to use and you can Padley through I change the animation so you can use the new animation from the start. We will be generating an animated emitter we'll be producing the geometry for that and then animating the movement. We'll be using again using viscosity surface tension as well as very important in this shot. We'll be meshing out using VDB to generate a flick of free and really nice mesh for our milk and then we will be shading as well using and rendering using our knollt. We've got some quite complex shading going on with the strawberry. We've got a lot of subsurface and transparency, different maps using noise to affect the roughness and obviously some nice subsurface scattering as well with the milk shader as well.

**Frame:** tutorials\frames\w04-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only. Week 4 of VFX School Tabletop Course: strawberry colliding with milk. FLIP fluid with animated emitter, viscosity + surface tension, VDB meshing, Arnold render (strawberry SSS + noise roughness + transparency; milk SSS shader).

### Summary
1m42s week introduction by VFX School Archive. Week 4 of the "Tabletop Course": simulates a strawberry colliding with poured milk. Topics previewed: animated FLIP emitter geometry; viscosity and surface tension (important for milk); VDB meshing for high-quality milk surface; Arnold renderer with complex strawberry shader (subsurface, transparency, noise-driven roughness map, SSS) and milk SSS shader. Pre-made animated strawberry geometry provided to students.

### Key Steps
*(Week introduction — no step-by-step content; see other w04-xx lessons for specifics)*

Topics covered in Week 4:
- Animated FLIP fluid emitter (milk pouring into scene)
- Strawberry collision geometry (pre-animated, updated mid-course)
- Viscosity and surface tension for milk fluid behavior
- VDB meshing for fluid geometry
- Arnold shading: strawberry (SSS, transparency, noise roughness) + milk (SSS)

### Houdini Nodes / VEX / Settings
- FLIP Fluids with viscosity + surface tension
- VDB from Particles → Convert VDB for mesh
- Arnold renderer: SSS material, transparency, noise-driven roughness

### Difficulty
Beginner

### Houdini Version
H18+

### Tags
[flip, fluid, viscosity, surface-tension, meshing, vdb, rendering, arnold, beginner]

---

## Related Tutorials
- w04-11-viscosity-and-surface-tension-v1-1080p.md (same week, viscosity and surface tension detail)
- w03-04-adding-viscosity-v1-1080p.md (previous week viscosity intro)
- w03-11-meshing-v1-1080p.md (previous week FLIP meshing)
