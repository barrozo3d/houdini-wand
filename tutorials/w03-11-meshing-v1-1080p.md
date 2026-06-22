---
title: w03   11   meshing v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=H56dPbE3S2E
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [flip, volumes, sop, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/w03-11-meshing-v1-1080p/
frame_count: 4
---

# w03   11   meshing v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=H56dPbE3S2E)
**Author:** The VFX School Archive
**Duration:** 7m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Now, I want to go ahead and generate our uh mesh. So, we've got our points, we need to make a mesh from this. And the workflow we're going to use is VDB. So, I'm going to find a VDB from uh particles. Okay, connect that up. We get an error there. Probably the voxel size is too big. Let's drop that down a little. Still nothing. Maybe the radius scale. It does say that we shouldn't drop it past 1.5, but we're going to be smoothing the the VDB after anyway. Try dropping that down to one. Still nothing. I'm going to drop this down .1. There we go. Getting something. Still a bit coarse. So, I'm going to drop the VDB scale down even further. 0.025. It'll take a while. Now, we're getting something nice and smooth. Probably drop this down a bit. I don't think it'll make much difference now. Should be fine. Cool. Okay. Looks looking nice now, but still you can see little a bit of roughness there. So, we can just drop a VDB VDB smooth. Oops. Drop VDB smooth SDF. And this as simple as that. Just connect it up and we get a much nicer result. Then, to bring it back into uh polygon geometry, we need a convert. I think just by default it will generate Yeah, our polygon...

**Frame:** tutorials\frames\w03-11-meshing-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Converting FLIP particle points to a render-ready polygon mesh using a VDB workflow: VDB from Particles -> VDB Smooth SDF -> Convert VDB, with careful voxel size and radius scale tuning to produce a clean mesh that separates distinct fluid layers.

### Summary
The instructor builds the particle-to-mesh pipeline from scratch, troubleshooting VDB from Particles settings (voxel size and radius scale) until a visible level set appears. VDB Smooth SDF is then applied to remove particle-level roughness. Convert VDB extracts a polygon mesh. The key insight is that tuning voxel size to a very small value (0.025) in combination with VDB smoothing produces a mesh clean enough for a food close-up render, and distinct VDB layers can be produced per fluid group to keep sauces separate.

### Key Steps
1. [`VDB from Particles`] Connect FLIP particle output; set Voxel Size (try 0.1 -> 0.025) until a surface appears
2. [Radius Scale] Tune Radius Scale (try 1.5 -> 1.0) if the default produces nothing
3. [`VDB Smooth SDF`] Connect downstream; default settings remove particle-level noise
4. [`Convert VDB`] Extract polygon mesh from the smoothed SDF level set
5. [Per-fluid separation] Use a Blast/Group to separate fluid by group; run VDB pipeline per fluid for distinct meshes
6. [Verify] Check mesh in viewport; confirm smooth continuous surface with no popping or holes
7. [Output] Feed polygon mesh into shading/rendering network

### Houdini Nodes / VEX / Settings
- `VDB from Particles` — converts point clouds to VDB level sets; Voxel Size (smaller = more detail, slower) and Radius Scale (minimum 1.0 recommended by Houdini) are the two critical parameters
- `VDB Smooth SDF` — Gaussian or mean-curvature flow smoothing on a signed distance field; reduces noise without collapsing thin features
- `Convert VDB` — extracts polygons from a VDB SDF; default Adaptivity=0 gives uniform quads
- Layer separation — processing separate fluid groups through independent VDB pipelines keeps sauce colours/shaders distinct

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the week overview that introduces this meshing step
- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — week 4 also uses VDB meshing for the milk pour
- [Small Scale Fluids](small-scale-fluids.md) — FLIP meshing reference for small-scale setups
