---
title: 76 starting the smoke vortex v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=BFZ3tItjKn8
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [dop, sop, pyro, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/76-starting-the-smoke-vortex-v1-1080p/
frame_count: 4
---

# 76 starting the smoke vortex v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=BFZ3tItjKn8)
**Author:** The VFX School Archive
**Duration:** 7m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, let's test what we just learned on a new setup. I'm going to delete this sphere, which was just for demonstration purposes of the sign function. And I'm going to create a Taurus. And I'm going to dive inside. And I'm going to align it with the Z axis. Okay, let me adjust the size of this. It's a bit too big. 0.6. And let's reduce this to 0.05. Probably even more. 0.025. Yeah. Next, I'm going to transform. I'm going to increase the rows here to 16 and give it a bit more resolution here. Maybe twice as much because we're going to want to Let me press shift W so you can see the subdivisions. I'm going to apply a transform which I'm going to be using for scaling this on this direction. Yeah. And then I'll subdivide So we have more geometry and get smoother. Okay, this is going to be the main object that we're going to be use for for sourcing. I'm also going to pull it up one so it doesn't really touch the ground. And let's animate it to rotate. Okay, we'll go here to the rotation on the Z axis and say times 90. Okay. Times 80. So now it rotates. Probably go faster. Let's say 20. Okay. Something like that. This is going to be the object that we'll use f...

**Frame:** tutorials\frames\76-starting-the-smoke-vortex-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Building a spinning torus as the velocity-imparting source geometry for a smoke vortex effect, relying on the torus's own rotation to seed the swirling motion rather than any external force field.

### Summary
Creates a Torus SOP aligned to the Z-axis, scaled to 0.6 radius with a tube radius of 0.025, with rows increased to 16 for resolution and a Subdivide added for smoothness. Animates rotation on the Z axis at `$F * 20` degrees for a fast spin. Uses a sign() function (covered in a prior lesson) to create an oscillating velocity field around the torus surface. Lifts the torus 1 unit off the ground so the resulting smoke column rises cleanly. This source geometry feeds into the Volume Source node in the DOP network built in the following lesson.

### Key Steps
1. [`Torus SOP`] Create and align to the Z-axis; set radius to 0.6, tube radius to 0.025
2. [Resolution] Increase rows to 16 for smoother geometry
3. [`Subdivide SOP`] Smooth the torus surface further
4. [Animate rotation] Set Z-axis rotation to `$F * 20` degrees for a fast spin
5. [`Attribute Wrangle`] Use `sign()` to create an oscillating velocity field around the torus
6. [Position] Lift the torus 1 unit off the ground for a clean rising smoke column
7. [Output] Pass this animated source geometry to the Volume Source node (next lesson)

### Houdini Nodes / VEX / Settings
- `Torus SOP` — the spinning source shape; radius and tube radius control its silhouette
- Rotation expression `$F * 20` — drives a continuous fast spin tied to frame number
- `sign()` VEX function — used to build the oscillating velocity field around the torus surface
- `Subdivide SOP` — smooths torus geometry before it becomes a pyro source

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)

---

## Related Tutorials
- [Building the Vortex DOP Network](78-building-the-vortex-dop-network-v1-1080p.md) — the following lesson that wires this source into a Pyro Solver
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — foundational volume concepts used by pyro sources
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — another pyro setup driven by a velocity source
