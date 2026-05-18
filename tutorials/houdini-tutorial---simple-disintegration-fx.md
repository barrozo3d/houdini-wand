---
title: Houdini Tutorial - Simple Disintegration FX
source: YouTube
url: https://www.youtube.com/watch?v=O2F1Qzl22oU
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Not specified (H19–H21 UI)"
tags: ["sop", "dop", "vop", "particles", "attributes", "vfx", "destruction", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tutorial---simple-disintegration-fx/
frame_count: 0
---

# Houdini Tutorial - Simple Disintegration FX

**Source:** [YouTube](https://www.youtube.com/watch?v=O2F1Qzl22oU)
**Author:** Voxyde VFX
**Duration:** 21m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey guys, I'm Malel Toby, you'll probably see me around on Boxer.com a bit more and on the YouTube channel. I've been asked by a few people to share how I made the disintegration effect that I did on the breakdown. It is actually a quite simple effect and I've been asked a couple of times on both our Discord channel and on LinkedIn. So I thought I'll instead of just sharing the hip file, I'll just walk you through how I did that. So I'm in Houdini and let's create a geometry node and I've been and I'll just put down a test geometry in here. Let's use the squab, display it in here and let's just quickly take a look at the geometry. It's fairly low resolution. You can actually increase it here as well, I think. No, not all this one. I'll remove the shader, we don't need that. And we need to sub-divide this so we have kind of an equal amount of subdivisions everywhere. So we'll just remesh it so we have triangles that are equal in size everywhere. Let's add the remesh, display it and let's increase the resolution in here by lowering this target size to say something like 0.001 to begin with. And I'll just increase this moving in here and the iterations to 10 to say it's a bit smoother...



---

## Structured Notes

### Core Technique
SOP-level disintegration effect: remesh geometry to uniform triangles, scatter points on the surface, use a noise-driven age/mask attribute to progressively delete geometry and emit particles — creating the illusion of a mesh dissolving into dust particles without any DOP simulation.

### Summary
A 21-minute tutorial showing how to build a clean disintegration effect entirely in SOPs. Starts by remeshing a test geometry to uniform triangle density using the `remesh` SOP, then scatters points across the surface. A noise-driven threshold attribute (using `attribvop` or `attribwrangle`) is animated over time to define a deletion mask — geometry below the threshold is deleted with a `blast` or `delete` SOP while above-threshold points are used as particle emission sources. The resulting particles drift away using the `popnet`/`popsolver` with curl noise for organic movement, and the threshold sweep creates the characteristic edge dissolve. Includes tips on controlling the transition edge sharpness and baking the result.

### Key Steps
1. Start with test geometry (e.g. `rubbertoy` or `pig` SOP); add `remesh` SOP — Target Size: ~0.001 (small triangles); Iterations: 10; Smooth: enabled — produces uniform triangle density needed for consistent dissolve edge
2. Create a noise-based dissolve mask: add `attribvop` or `attribwrangle` after remesh; use `turbulentnoise` VOP driven by position P to generate a 0–1 float attribute named `dissolve`; animate an offset or threshold parameter over time to make the mask advance across the geometry
3. Use `attribwrangle` to compare `@dissolve` against an animated threshold: `if (@dissolve < ch("threshold")) { @group_delete = 1; }` — creates a group that advances as the threshold increases
4. Add `blast` SOP referencing the group to delete geometry below the threshold — this creates the disintegrating surface
5. Use a `scatter` SOP before the blast (on full geometry) or at the deletion boundary to generate particle source points; feed these into a `popnet` for particle emission
6. Inside `popnet`: use `popsource` from the scatter points; add `popcurl` or use `attribvop` with `curlnoise` to give particles drifting organic motion; set short lifetime with aging so particles fade quickly
7. Control edge sharpness: remap the noise with `fit` VOP — narrow source/dest range creates a sharper dissolve front; wider range creates a softer gradient
8. Combine: `merge` SOP — surviving geometry (from blast) + particles (from popnet output) into a single renderable stream

### Houdini Nodes / VEX / Settings
- `rubbertoy` / `pig` SOP — test geometry source
- `remesh` SOP — Target Size: ~0.001; Iterations: 10; Smooth: on; produces uniform triangle mesh required for even dissolve edge
- `attribvop` SOP — turbulent noise → fit → remap to 0–1 dissolve attribute; animate noise offset or threshold over time
- `attribwrangle` SOP — VEX: `if (@dissolve < ch("threshold")) { @group_delete = 1; }` — creates deletion group dynamically
- `blast` SOP — Group: group_delete; Delete Non Selected: off; removes geometry falling below threshold
- `scatter` SOP — Total Count: ~5000–20000; scatters points on geometry surface as particle source
- `popnet` / `popsource` — source from scatter points at the deletion boundary; Emission: continuous or burst
- `popsolver` — particle dynamics engine; add gravity and drag for natural falloff
- `curlnoise` VOP / `popcurl` DOP — adds swirling fluid-like motion to disintegrated particles
- `merge` SOP — combines surviving geometry with particle output for unified render
- `turbulentnoise` VOP — Element Size; Amplitude; feeds dissolve mask; offset animated over `$T` to advance front
- `fit` VOP — Source Min/Max: narrow range (e.g. 0.4–0.6) for sharp edge; Dest: 0–1 for mask

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
#sop #dop #vop #particles #attributes #vfx #destruction #intermediate

---

## Related Tutorials
- [Intro To Houdini for VFX - Beginner Course](./intro-to-houdini-for-vfx---beginner-course.md) — #sop #dop #vop #vex #attributes #particles #beginner
- [Intro To Houdini Particles - Full Beginner Course](./intro-to-houdini-particles---full-beginner-course.md) — #dop #sop #vop #particles #simulation #attributes
- [Houdini Tutorial - Wispy Smoke](./houdini-tutorial---wispy-smoke.md) — #pyro #smoke #dop #sop #simulation #vfx
