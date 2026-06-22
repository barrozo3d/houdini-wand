---
title: w01   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=RQBrvngXM6Y
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rbd, simulation, dop, instancing, rendering, beginner]
extraction_status: complete
frames_dir: tutorials/frames/w01-01-introduction-v1-1080p/
frame_count: 4
---

# w01   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=RQBrvngXM6Y)
**Author:** The VFX School Archive
**Duration:** 1m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello and welcome to the tabletop course. This is week one and we will be looking at reproducing this coffee bean shot. We'll be using rigid body dynamics in Houdini. Uh along the way we'll look at uh instancing geometry to points. We'll be varying the instance, the velocity, and the orientation of the geometry. Uh we'll take all this and feed it into a into a dynamics network and build a bullet simulation. We will add some spin and gravity and uh look at getting a uh a nice collision between the coffee beans. Following this, we will do some post simulation tricks, do some retiming, and uh double the number of the quantity of coffee beans without having to resimulate. Uh once the simulation is done, we'll continue on to lighting, shading, and rendering with Arnold.

**Frame:** tutorials\frames\w01-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-one overview of the Tabletop Food Simulation course: reproducing a coffee bean avalanche shot using Bullet RBD with instanced geometry, varied orientations and velocities, retiming tricks, and a full lighting/shading/rendering pipeline in Arnold.

### Summary
The instructor introduces the tabletop course by describing the coffee bean shot goal. The week covers instancing bean geometry to scattered points, varying instance orientations and initial velocities, feeding the points into a Bullet dynamics network, and adding spin and gravity for realistic collisions. Post-simulation, retiming is used and the bean count is doubled without re-simulating. The week concludes with Arnold lighting, shading and rendering.

### Key Steps
1. [`Scatter SOP`] Scatter points above the shot area as initial bean positions
2. [`Copy to Points SOP`] Instance coffee bean geometry onto scattered points
3. [`Attribute Wrangle`] Vary `orient` and `v` (velocity) attributes per instance for randomness
4. [`RBD Configure`] Pack instanced geometry for Bullet solver
5. [`RBD Solver`] Build bullet sim with gravity and angular velocity (spin)
6. [Collision geometry] Set up collision surface for beans to land on
7. [Post-sim retiming] Use a Time Blend or retime trick to slow/speed the sim
8. [`Copy to Points`] Double bean count by merging a time-offset version of the sim
9. [Arnold ROP] Shade, light and render the final result

### Houdini Nodes / VEX / Settings
- `Copy to Points SOP` — instances geometry per point; reads `orient`, `pscale`, `v` attributes for per-instance variation
- `Attribute Wrangle` — sets random orientations (`orient` quaternion) and velocities (`v`) per point
- `RBD Configure` — packs geo and prepares RBD attributes for Bullet
- `RBD Solver (Bullet)` — rigid-body dynamics solver driving bean collisions
- Retiming — time-warp technique applied post-cache to create slow-motion without re-simulating

### Difficulty
Beginner

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — foundational RBD Bullet techniques
- [Module I Intro](module-i-week-01-01-intro-v1-1080p.md) — parallel beginner RBD intro
- [Tabletop Week 05 Intro](w05-01-intro-v1-1080p.md) — the final course week combining RBD with FLIP
