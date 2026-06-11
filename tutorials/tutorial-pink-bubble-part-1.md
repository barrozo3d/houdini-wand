---
title: [Tutorial] Pink Bubble. Part 1.
source: YouTube
url: https://www.youtube.com/watch?v=ypJL4PXxQpg
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, vop, vdb, particles, instancing, simulation, procedural, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-pink-bubble-part-1/
frame_count: 4
---

# [Tutorial] Pink Bubble. Part 1.

**Source:** [YouTube](https://www.youtube.com/watch?v=ypJL4PXxQpg)
**Author:** Alexander Eskin
**Duration:** 25m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello, hello today we're gonna do bubbles in a pink sphere and We're gonna render it with octane Let's start with the June out Gonna call it bubble source Diving and create a sphere Set the scale to two Primitive type polygon frequency 64 And we're gonna make two branches One The first one is gonna be a ripple solar for the surface and the second one we're gonna use to scatter some points Now let's start with the scattering points Use the peak node Strength the sphere a bit just to make sure that the scattered points inside want intersect with the exterior surface of the sphere Maybe from polygons Type from distance to fog Decrease the voxelsize a bit and scatter some points 65 points will be enough create a scale attribute The scale and the value should be 0.1 Let's make a preview for that GL sphere points equals one Okay turn off the grid we don't need it right now and attribute the just float To Randomize the scale of the spheres attribute name p scale already the one that we need operation multiply pattern noise Ta-da so we can adjust the element size for Offset to 1.3 and maybe decrease the Scale for the small spheres and create another attribute the just float and Decrease th...

**Frame:** tutorials\frames\tutorial-pink-bubble-part-1\frame_000.jpg


---

## Structured Notes

### Core Technique
English companion to Pink Bubbles Pt1 RU — same sphere→VDB→scatter→peak workflow with exact parameters: sphere scale 2, freq 64, fog VDB with decreased voxel size, 65 scatter points, `pscale` 0.1 varied by `attribadjust` noise multiply (offset 1.3). Two branches: ripple surface solver + scatter. Rendered with Octane (vs Redshift in the Russian version).

### Summary
A 25-minute English tutorial (Part 1) building pink bubbles inside a sphere, rendered with Octane. Sphere (scale 2, polygon, freq 64) → `peak` to shrink → `vdbfrompolygons` (fog type, reduced voxel size) → `scatter` 65 pts → `pscale` 0.1 → `attribadjust` float, multiply by noise (offset 1.3) for size variation → second `attribadjust` float to set minimum size. Viewport preview via `gl_sphere_points`. Two-branch setup: Branch 1 = ripple surface solver (Part 2), Branch 2 = scatter points.

### Key Steps
1. Geo node "bubble_source" → `sphere` SOP — scale 2, polygon, frequency 64
2. Split into 2 branches: **Branch 1** (ripple/surface wave) + **Branch 2** (bubble scatter)
3. Branch 2: `peak` SOP — shrink sphere slightly to prevent scatter from hitting exterior wall
4. `vdbfrompolygons` — type: **from distance to fog** (fog VDB); decrease voxel size for resolution
5. `scatter` SOP — **65 points**
6. `attribcreate` — `pscale` = **0.1**
7. `attribwrangle` — `i@gl_sphere_points = 1` for viewport preview
8. `attribadjust` float — attribute: `pscale`, operation: **multiply**, pattern: **noise**, element size offset: **1.3** → larger/smaller bubble variation
9. Second `attribadjust` — decrease minimum size (clamp small bubbles)
10. Continue to Part 2 for ripple surface solver + Octane render

### Houdini Nodes / VEX / Settings
- `sphere` SOP — scale 2, polygon, frequency 64
- `peak` SOP — slight inward offset
- `vdbfrompolygons` — from distance to fog; decreased voxel size
- `scatter` SOP — 65 points
- `attribcreate` — `pscale` = 0.1
- `attribwrangle` — `i@gl_sphere_points = 1`
- `attribadjust` float — multiply pscale by noise, element size offset 1.3
- Second `attribadjust` — minimum size clamp
- Octane render (Part 2)

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, vop, vdb, particles, instancing, simulation, procedural, rendering, intermediate

---

## Related Tutorials
- [[урок-розовые-пузыри-часть-1]] — Russian companion (same technique)
- [[tutorial-purple-sponge]] — similar VDB + scatter + pscale pipeline
- [[model-a-procedural-flower-houdini-tutorial]] — peak SOP usage
