---
title: Houdini UV Unwrapping Fundamentals
source: YouTube
url: https://www.youtube.com/watch?v=cguHzZ9L87g
author: Mat Sola
ingested: 2026-06-11
houdini_version: "Not specified (H20–H21 UI)"
tags: [sop, modelling, uv, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/houdini-uv-unwrapping-fundamentals/
frame_count: 4
---

# Houdini UV Unwrapping Fundamentals

**Source:** [YouTube](https://www.youtube.com/watch?v=cguHzZ9L87g)
**Author:** Mat Sola - Learn Destruction FX in Houdini & UE5
**Duration:** 65m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I want to share with you my six step workflow for laying out UVs in Houdini for practically anything, your hard surface, your soft surface models, and everything in between. And by the end of this video, if you follow along, you too will know how to project UVs, how to define and cut seams, how we can flatten them out into a 2D space, how we can pack and organize everything. How do you visualize results? How do you export UVs to the package of your choice? Well, these are the questions we're going to look at today. But first, if you're new here, be sure to subscribe, like, and leave a nice comment. These things help me, help you. Now, let's look at this six step workflow. Here we go. Let's look at this six step workflow that I have defined in my own head, and I'm going to try to pass to you. Which technically is, well, seven steps, because everything starts at step zero, which is right here in the pink color, which is geometry preparations. Before we can do anything in Houdini, or for that matter in any 3D application, we want to work with geometry that are well prepared, that do not have errors of any kinds that don't have open holes, that don't have duplicate faces...

**Frame:** tutorials\frames\houdini-uv-unwrapping-fundamentals\frame_000.jpg


---

## Structured Notes

### Core Technique
A 7-step (Step 0 through Step 6) UV unwrapping workflow for any geometry type in Houdini — covering geometry preparation, projection, seam definition, flattening, packing, visualization, and export.

### Summary
A 65-minute comprehensive UV fundamentals course by Mat Sola covering a complete reusable workflow: geometry cleanup as a prerequisite, UV projection methods, seam cutting via edge groups, `uvpeel`/`uvunwrap` for flattening, `uvlayout` for packing, `uvquickshade` for visualization in the viewport UV editor, and export-ready UV output. Demonstrated on both hard-surface and soft/organic models (human head mesh visible in frames).

### Key Steps
1. **Step 0 — Geometry prep**: ensure mesh has no open holes, duplicate faces, or non-manifold errors; use `clean` SOP or `polyDoctor` to validate
2. **Step 1 — UV Projection**: `uvproject` SOP — choose projection type (planar, cylindrical, spherical) per region; set axis and scale to fit geometry
3. **Step 2 — Define seams**: select seam edges manually or via `edgegroup`; use `polysplit` to mark cuts; these drive `uvpeel` seam inputs
4. **Step 3 — Flatten**: `uvpeel` SOP — input seam edges group; flattens islands with minimal distortion; alternative: `uvunwrap` for automatic seam detection
5. **Step 4 — Pack and organize**: `uvlayout` SOP — packs all UV islands into 0–1 space; adjust padding, scale, and resolution settings
6. **Step 5 — Visualize**: open UV viewport (press space → UV editor); use `uvquickshade` SOP with a checkerboard texture to check for stretching and distortion
7. **Step 6 — Export**: wire into `rop_geometry` or `filecache`; standard `.obj` / `.fbx` export carries UVs; can also pass directly to LOPs for USD pipeline

### Houdini Nodes / VEX / Settings
- `uvproject` SOP — projection type: Planar/Cylindrical/Spherical; Axis parameter
- `edgegroup` or manual edge selection — seam definition
- `polysplit` SOP — optional seam cutting
- `uvpeel` SOP — seam input group; flattening method
- `uvunwrap` SOP — automatic seam detection alternative
- `uvlayout` SOP — padding, scale, resolution; packs all islands into 0–1 UV space
- `uvquickshade` SOP — checkerboard visualization shader
- `clean` SOP — geometry validation; remove duplicate faces, fix normals
- UV Viewport editor — Space bar in viewport → UV display mode

### Difficulty
Intermediate

### Houdini Version
Not specified (H20–H21 UI)

### Tags
sop, modelling, uv, procedural, intermediate

---

## Related Tutorials
- [[intro-to-houdini-for-vfx---beginner-course]] — SOP geometry fundamentals prerequisite
- [[improve-solaris-performance---houdini-tutorial]] — Pipeline context where UV-ready assets are exported to USD/Solaris
