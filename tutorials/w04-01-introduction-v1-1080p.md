---
title: w04   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=S4VjdIf5BKQ
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [flip, simulation, dop, rendering, intermediate]
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
**Transcript:** Kind: captions Language: en Hey guys, and welcome to week four of the tabletop course. This week we're going to be simulating um a strawberry be colliding with milk. So, we've got a a kind of milk pouring in into the scene and then the strawberry colliding with that. Um again, we'll be using uh flip flip fluids in Houdini to do that. Um for for this shot, halfway through the project, I will be bringing in a new animation for the strawberry. So, you can go ahead and use that from the beginning. Okay, we've got an animated strawberry um for you to use and you can uh halfway through I I I change the animation, so you can use the new animation from the start. Um we will be generating a uh an animated emitter. We'll be producing the geometry for that and then um animating the movement. We'll be using uh again using viscosity, surface tension as well is very important in this shot. Um we'll be meshing out using VDB to to generate a flicker-free and really nice uh mesh for our our milk. And then we will be shading as well using and rendering using Arnold. We'll be We've got some quite complex uh shading going on with the strawberry. We've got a lot of subsurface and transparency, differen...

**Frame:** tutorials\frames\w04-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-four overview: simulating a strawberry colliding with poured milk using FLIP fluids with an animated emitter, viscosity, surface tension, VDB meshing for flicker-free results, and complex Arnold shading for the strawberry (subsurface + transparency).

### Summary
This week introduces an animated FLIP fluid emitter (milk pour) combined with a separately animated strawberry collision object. The instructor highlights the use of viscosity and surface tension as critical parameters that give milk its characteristic behaviour — forming a crown splash with held droplets. The sim is meshed using VDB for a stable, flicker-free mesh, and rendered in Arnold with complex subsurface-scattering and transparency on the strawberry shader.

### Key Steps
1. [Animated strawberry FBX/Alembic] Import updated strawberry animation; use the new animation from the start
2. [`FLIP Source`] Build animated emitter geometry to mimic milk pouring
3. [`Attribute Wrangle / Keyframes`] Animate emitter velocity and position to arc the pour
4. [`FLIP Solver` > Viscosity] Enable and tune viscosity for milk (low value)
5. [`FLIP Solver` > Surface Tension] Enable surface tension to create crown splash and droplet cohesion
6. [`VDB from Particles`] Convert FLIP points to VDB for smooth meshing
7. [`VDB Smooth SDF`] Smooth the VDB to remove particle-level roughness
8. [`Convert VDB`] Extract polygon mesh from VDB for rendering
9. [Arnold ROP] Shade strawberry with SSS + transparency; light and render

### Houdini Nodes / VEX / Settings
- `FLIP Solver` > Viscosity — controls resistance to flow; low values for milk (~1-10)
- `FLIP Solver` > Surface Tension — simulates cohesive force holding fluid together; critical for milk crowns and droplets
- `VDB from Particles` — converts FLIP particle points to a VDB level set; voxel size controls detail/speed tradeoff
- `VDB Smooth SDF` — Gaussian smoothing on the SDF removes particle-level noise before meshing
- `Convert VDB` — extracts polygon surface from VDB level set

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Viscosity and Surface Tension](w04-11-viscosity-and-surface-tension-v1-1080p.md) — hands-on deep dive into these FLIP parameters
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the preceding FLIP week covering viscous sauces
- [Small Scale Fluids](small-scale-fluids.md) — FLIP reference for small-scale setups
