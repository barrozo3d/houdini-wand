---
title: module i   week 03   01   introduction to volumes v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=hEcmhhNlpzY
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [sop, vop, volumes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-03-01-introduction-to-volumes-v1-1080p/
frame_count: 4
---

# module i   week 03   01   introduction to volumes v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=hEcmhhNlpzY)
**Author:** The VFX School Archive
**Duration:** 15m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hi guys. So, welcome to week three. Um, as per usual, let's go ahead and create a new project. Okay. So, this will be we are in module uh one week oop week three. Call it whatever you like. Um, and I'm going to save this in my D drive. Okay. accept on that and then save. Always save your hip file. So what are we? Week three version one. Great. So um yeah, this week is all about um volumes. Um so I'm just clearing up my desktop there. By the way, if you want to do the same, just delete those at the top. But you can work however you like. Now I'm going to create a geometry node. Um let's call this uh volumes intro. So we'll just have a quick look at um some volumes. So typically in Houdini, if we've just dropped down a test geometry pig head, we haven't looked at these, but they're kind of handy. If you uh again, you know, tab on your keyboard, start typing test, and you'll see you've got all these different um pieces of test geometry. You got this crag which has some animation and a rig I think. Got a pig head rubber toy which are both just models static with um textures. Your shadable this squab. This weird alien thing. Loads of cool stuff. Um so we're g...

**Frame:** tutorials\frames\module-i-week-03-01-introduction-to-volumes-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
A comprehensive introduction to Houdini volumes using a pig-head test geometry: distinguishing fog VDBs from SDFs, then building a cloud volume from a polygon mesh with procedural noise.

### Summary
Explains the fog VDB vs. SDF (signed distance field) distinction: fog is a density field (0 outside, positive inside), while an SDF is a distance field (negative inside, positive outside, zero exactly at the surface). Builds a cloud volume from a polygon mesh via the chain: mesh -> VDB from Polygons (SDF) -> VDB Reshape (dilate to add volume) -> cloud noise via Volume VOP. The Volume VOP workflow binds the density field, applies Turbulent Noise in 3D, uses Fit Range to remap noise into [0, 1], and multiplies that back into density. Introduces the built-in "test geometry" SOP variants (pig head, squab, crag, etc.) as quick geometry sources, and covers Volume Display settings — density threshold, smoke colour, and step size — for viewport preview.

### Key Steps
1. [`Test Geometry SOP`] Use the pig head (or similar) as a quick source mesh
2. [`VDB from Polygons`] Convert the mesh to an SDF level set
3. [`VDB Reshape SDF`] Dilate the SDF to add volume/thickness
4. [`Volume VOP`] Bind density; apply 3D Turbulent Noise
5. [Fit Range] Remap noise output into the [0, 1] range
6. [Multiply] Combine the remapped noise back into the density field
7. [Volume Display] Tune density threshold, smoke colour and step size for viewport preview

### Houdini Nodes / VEX / Settings
- `VDB from Polygons` — converts a closed mesh into a signed distance field volume
- `VDB Reshape SDF` — dilates/erodes an SDF to thicken or thin a volume
- `Volume VOP` / Turbulent Noise — procedural 3D noise driving cloud-like density variation
- Fit Range — remaps noise output range before recombining with density
- Fog vs. SDF — fog: 0 outside/positive inside; SDF: negative inside/positive outside/zero at surface

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)

---

## Related Tutorials
- [Creating a New Project](module-i-week-02-01-creating-a-new-project-v1-1080p.md) — the preceding scattering week
- [Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — the following week's POP work
- [Starting the Smoke Vortex](76-starting-the-smoke-vortex-v1-1080p.md) — applies volume/pyro concepts built on this VDB foundation
