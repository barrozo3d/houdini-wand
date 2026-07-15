---
title: Procedural tips and tricks in Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=wgStaCuEglI
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.309"
tags: [vex, find-shortest-path, vdb, cops, lab-sort, seamless-noise, jewelry, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-tips-and-tricks-in-houdini-205/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural tips and tricks in Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=wgStaCuEglI)
**Author:** cgside
**Duration:** 3m22s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome. In this video I'll share a few procedural techniques in Odini,
[0:05] from Vax to the new cops, I hope you can learn something new with this.


### Circular group selections with vex [0:10]
**Transcript (timestamped):**
[0:10] So as you can see I have these stone holders and the way I'm building them is by using the fine
[0:15] shortest path node. And for that I need groups of points, initially I used the manual selection,
[0:23] but since I might change the stone shape I decided to have a more procedural approach.
[0:29] What I need is to select a few points in a circular pattern.
[0:34] For that I found some sample code online by Animatrix, that creates points in a circular pattern
[0:41] by using the sample circle function. I just said to adapt to group the near points,
[0:47] also adding a distance parameter to the position.
[0:52] And in the main network I just said that another parameter to the Y position so I can have
[0:57] control over this selection. Okay having these curves I need to create the stone holder mesh.


### radial sort and add by attr with modulo [1:00]
**Transcript (timestamped):**
[1:04] I start by resampling to have 20 points, then selecting the first 8 points of each curve,
[1:11] creating an attribute on the points with Modulo and the amount of points on each curve.
[1:16] And as you can see it will create this pattern along the lines that I can use to connect them.
[1:22] If I add them now by attribute and using the group it will get all over the place due to the
[1:28] point sorting. Luckily there's a lab sort that lets you sort points in a circular pattern,
[1:35] which will work right in this example. Again lab sort not the main one.
[1:40] From there I can skin the shape and it will be ready for the next step.
[1:45] Now having both surfaces combined I want to make a VDB out of it so I can blend it with the ring.


### Open geo vdb with topology to sdf [1:46]
**Transcript (timestamped):**
[1:52] But the mesh is open and just creating a VDB won't be enough. We actually need to use the topology
[1:59] SDF which will create this shell VDB. Then smooth it out and blend it with the ring.


### Seamless noises with COPS [2:06]
**Transcript (timestamped):**
[2:07] So having a your VD mesh I want to create some seamless noises for displacement using cops.
[2:13] And the way you can get seamless noises with cops is by using the Racerize setup set to UVs.
[2:20] And now in the Racerize GU output both the position and alpha layers.
[2:26] The next step is to connect that original position to the noise 3D input position.
[2:31] In this case I am also distorting a bit the initial position layer with another noise.
[2:37] If I connect this to the preview material you'll get some visible seams.
[2:44] This is the enough to fix just use the extra plate boundaries with that mask we saved from the alpha.
[2:51] And now you should have a seamless noise pattern.


### Stone cuts in Houdini [2:56]
**Transcript (timestamped):**
[2:56] So I tried a few approaches to create the stone cats.
[3:00] But using just a whirling noise in a mountain and the mesh sharpen actually gave me the best result.


### Outro [3:09]
**Transcript (timestamped):**
[3:10] And yeah I hope this helps you out and make sure to check out my Patreon where I upload all project files
[3:16] from my videos including this one. Thank you.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-tips-and-tricks-in-houdini-205/frame_000.jpg
- [1:15] tutorials/frames/procedural-tips-and-tricks-in-houdini-205/frame_001.jpg
- [1:50] tutorials/frames/procedural-tips-and-tricks-in-houdini-205/frame_002.jpg
- [2:30] tutorials/frames/procedural-tips-and-tricks-in-houdini-205/frame_003.jpg
- [3:10] tutorials/frames/procedural-tips-and-tricks-in-houdini-205/frame_004.jpg

---

## Structured Notes

### Core Technique
Five procedural techniques for a stone-set ring: circular point-group selection via a `sample_circle()`-based VEX snippet feeding **Find Shortest Path** for stone-holder wire mesh generation, a **Lab Sort** node (not the regular Sort) for reliable circular point ordering before Skin, **VDB from Polygons with Topology to SDF** to properly shell an open (non-watertight) mesh, seamless COPs displacement noise via a UV-space Rasterize with position+alpha layers, and a Whirling-Noise-plus-Mountain-plus-Mesh-Sharpen combo for realistic stone facet cuts.

### Summary
Stone-holder wire mesh generation ("prong" shapes) needs groups of points arranged in a circular pattern around each stone; rather than manual selection (fragile if the stone shape changes), a VEX snippet (adapted from sample code by Animatrix) uses `sample_circle()` to generate points in a circular pattern, grouping the nearest points and adding a distance parameter to offset their position, with an extra Y-position parameter exposed in the main network for control. With these circular point groups as curves, the holder mesh is built by Resampling to 20 points, selecting the first 8 points of each curve, creating a per-point attribute via **modulo** against the point-count-per-curve to establish a connection pattern, then adding curves by attribute — but the default point sort order scrambles this, so a **Lab Sort** node (specifically the Labs version, not the standard Sort SOP) is used to sort points in a proper circular order before **Skin**ning the shape. Since the resulting mesh is open (not watertight), a plain VDB from Polygons isn't sufficient to volumize it; the fix is **VDB from Polygons with the conversion set to Topology to SDF**, which creates a proper shell VDB from open geometry, followed by smoothing and blending with the ring band. For seamless displacement noise on the VDB-derived mesh, a **Rasterize** node set to UVs outputs both a position layer and an alpha layer; the position layer feeds a 3D noise's position input (itself distorted slightly by another noise), and — critically — the resulting seams visible when previewed are fixed by using the alpha-channel mask to **extrapolate the plate boundaries**, producing a seamless tileable noise pattern. Finally, after trying several approaches for the stone-cut facet look, the best result came from a simple combination: a **Whirling Noise** distortion, a **Mountain** node, and a final **Mesh Sharpen** pass.

### Key Steps
1. **Circular group selection**: use a VEX snippet (adapted from Animatrix sample code) with `sample_circle()` to generate points in a circular pattern around each stone location; group the nearest points and add a distance offset to their position; expose an extra Y-position parameter in the main network for additional control.
2. **Stone-holder mesh build**: Resample the resulting curves to 20 points; select the first 8 points of each curve; create a point attribute using **modulo** against the per-curve point count to establish which points should connect.
3. **Add by attribute + circular sort**: connecting points by attribute directly produces a scrambled result due to default point sort order; fix by inserting a **Lab Sort** node (the Labs-specific sort, not the regular Sort SOP) configured to sort points in a circular pattern, which resolves the ordering correctly for this case.
4. **Skin** the sorted curves into the final holder mesh shape.
5. **Shell an open mesh with VDB**: since the holder mesh is open/non-watertight, a plain VDB from Polygons conversion isn't enough — set the conversion mode to **Topology to SDF** to properly generate a shell VDB, then smooth it and blend with the ring band geometry.
6. **Seamless COPs noise**: set up a **Rasterize** node targeting UV space, outputting both a **position** layer and an **alpha** layer.
7. Feed the rasterized position layer into a 3D noise's position input (optionally distorting that position layer further with a secondary noise) to drive displacement.
8. **Fix visible tile seams**: connecting the raw noise directly to a preview material shows visible seams at UV tile boundaries; fix by using the saved alpha-channel mask to **extrapolate the plate boundaries**, producing a properly seamless noise pattern.
9. **Stone facet cuts**: after experimenting with several approaches, the best-looking result came from a simple chain of **Whirling Noise** distortion → **Mountain** node → **Mesh Sharpen** — no exotic technique needed.

### Houdini Nodes / VEX / Settings
VEX `sample_circle()` snippet (circular point generation, near-point grouping, distance offset), Find Shortest Path, Resample, Attribute Wrangle (modulo-based connection pattern), Add (by attribute), Lab Sort (Labs circular point sort — distinct from the standard Sort SOP), Skin, VDB from Polygons (Topology to SDF conversion mode for open/non-watertight meshes), VDB Smooth, VDB Combine (ring blend), Rasterize (UV-space, position + alpha layer outputs), 3D Noise (position-driven, secondary noise distortion), alpha-mask-based plate-boundary extrapolation (seamless tiling fix), Whirling Noise, Mountain, Mesh Sharpen (stone facet cuts).

### Difficulty
Intermediate–Advanced (the Lab Sort circular-ordering trick, Topology-to-SDF shelling, and seamless-Cops-noise techniques are all non-obvious but individually compact).

### Houdini Version
20.5.309 (visible in viewport title bar).

### Tags
vex, find-shortest-path, vdb, cops, lab-sort, seamless-noise, jewelry, procedural-modeling

---

## Related Tutorials
- [The Donut Tutorial in Cops - Houdini 20.5](the-donut-tutorial-in-cops-houdini-205.md) — related Copernicus/Cops procedural-texturing tutorial from the same channel, though without the seamless-tiling fix covered here.
- [Procedural Rock Formations Part 2](procedural-rock-formations-part-2.md) — shares the Find Shortest Path technique used here for the stone-holder wire mesh, applied there to vines instead.
- [Tips and tricks in Houdini 21](tips-and-tricks-in-houdini-21.md) — companion tips-and-tricks video from the same channel, covering matrix-axis-extraction, UV-gradient tine tapering, and the new Pick node instead.
- [Why you need to learn vex in Houdini #1](why-you-need-to-learn-vex-in-houdini-1.md) — shares the sample_circle()-based circular spiral-construction technique used here, applied there to a croissant's interior lamination.
