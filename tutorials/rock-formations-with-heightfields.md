---
title: Rock formations with heightfields
source: YouTube
url: https://www.youtube.com/watch?v=rEn0ochILjU
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.593"
tags: [heightfields, terrain, triplanar, displacement, ambient-occlusion, texturing, rocks, environment]
extraction_status: complete
frames_dir: tutorials/frames/rock-formations-with-heightfields/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Rock formations with heightfields

**Source:** [YouTube](https://www.youtube.com/watch?v=rEn0ochILjU)
**Author:** cgside
**Duration:** 5m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to show you how I created this
[0:07] sort of rock formations using I'd fields. So I started with the Nightfield and drawing
[0:20] a mask. In this case you can change to the shape you want. Then I'm using a Nightfield
[0:28] layer to mix two masks, one slightly more blurred. As you can see so we can layer a bit
[0:37] the bottom and I'm setting the Nightfield layer to maximum. Then in this volume drop I am
[0:46] just creating a random baronoid pattern that will create different heights at each point
[0:57] and you can change the seed and minimum value and the maximum value for heights. And this
[1:07] is done by using a baronoid noise and then using a random from the near output just using
[1:19] a random and I'm just adding a value here for the seeds and finally fitting the range and
[1:28] multiplying by the mask, the current mask. So after that we can use the mask expands but set to
[1:40] the height layer so we can create these square life shapes. You can change the amount. In this
[1:52] case I set it to a quite high value. Doesn't look much right now but should have a better shape at
[2:01] the end. Then I'm blurring a bit and clearing the mask. Then right here I'm just creating
[2:10] the slope layer mask that we will use later and just clearing and then I'm using a Nightfield
[2:19] noise here set to Shabby Shaps, as you can see and then I'm using a Distort by Layer that will create
[2:31] these random shapes as you can see. Then I'm blurring a bit the Nightfield and doing another distortion,
[2:46] just basic distortion, masking the flat areas just a bit more than the flat areas so it has some
[2:57] some falloff and then using a noise to distort a bit the tops as you can see using the mask with some blur.
[3:13] Then I'm clearing the mask and doing again a mask expands set to the eye channel so it creates
[3:23] these bulky shapes as you can see. Then another Distort, small Distort and converting the Nightfield.
[3:38] Then I am clipping the the extra parts remashing
[3:46] as you can see because this sort of geometry won't work while with for texturing or displacement
[3:59] so we need to remesh it. Then right here I'm applying a triplanet this place as I have shown in
[4:10] other tutorials. I am applying two in this case blurring the normals and doing the displacements
[4:19] if I enable the sub divide we should see a weather result. So this is the result of the displacement
[4:27] just adding the details on the sides that are difficult to devolume environment like the Nightfields.
[4:37] If you don't have some sort of slope it won't really create details.
[4:45] So then I'm calculating the ambient occlusion.
[4:52] As you can see this is a result of the ambient occlusion.
[4:56] Then I'm doing a point pop to add some color and the way I'm adding color is by sampling a
[5:07] texture by right clicking here and choosing sample screen colors and then you can sample from a
[5:16] texture in this case I use this one just drag the mouse along the texture then I'm just
[5:25] since it's too dark I'm using a quick material and that should give us a more normalized output.
[5:36] So yeah that's basically it's if you want to download the file feel free to do it on my patron
[5:43] and let me know what you think in the comments. Thank you and see you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/rock-formations-with-heightfields/frame_000.jpg
- [1:00] tutorials/frames/rock-formations-with-heightfields/frame_001.jpg
- [1:40] tutorials/frames/rock-formations-with-heightfields/frame_002.jpg
- [2:25] tutorials/frames/rock-formations-with-heightfields/frame_003.jpg
- [3:20] tutorials/frames/rock-formations-with-heightfields/frame_004.jpg
- [4:20] tutorials/frames/rock-formations-with-heightfields/frame_005.jpg
- [5:20] tutorials/frames/rock-formations-with-heightfields/frame_006.jpg

---

## Structured Notes

### Core Technique
Build tall rock-spire/cliff formations from a Heightfield by layering multiple masked Heightfield Distort passes (each shaped by a different noise and mask-expand step), then convert to polygons, apply Triplanar displacement for fine detail, and finish with ambient occlusion plus a screen-color-sampled texture for quick shading.

### Summary
Starting from a hand-drawn Heightfield mask, a Heightfield Layer mix (set to Maximum) blends two versions of the mask (one blurred) to build up the base silhouette. A Voronoi-based random-height pattern (via a random function seeded per point) adds per-point height variation, scaled and masked. Mask Expand grows/blocks out squarish base shapes, followed by blurring and mask-clearing between passes. A slope-layer mask is created for later use, then a "Shabby Shapes" Heightfield Noise combined with Distort by Layer produces the jagged, randomized silhouette characteristic of rock spires — repeated with additional smaller distortions and falloff-aware masking (more falloff on flatter areas) to add variation at the tops. A second Mask Expand pass with the "eye" channel creates bulky lower-body shapes, followed by more small distortion and heightfield-to-polygon conversion. After clipping/remeshing (since heightfield-derived geometry doesn't work well directly for texturing/displacement), a Triplanar setup with blurred normals drives fine surface displacement, followed by Ambient Occlusion calculation. Finally, color is quickly added via a Point VOP using Houdini's "sample screen colors" eyedropper feature to pull colors directly from a reference texture, brightened with a Quick Material.

### Key Steps
1. Draw an initial **Heightfield mask** (any desired base shape).
2. Use **Heightfield Layer** (mode: Maximum) to blend two versions of the mask — one slightly more blurred — layering detail at the bottom.
3. Create a **random Voronoi/Baronoid height pattern**: use a Voronoi noise, take its "near" output through a `random()` function with a seed offset, then Fit Range and multiply by the current mask to vary point heights (min/max controls exposed).
4. Use **Mask Expand** on the height layer to create squarish base shapes; blur afterward and clear the mask for the next pass.
5. Create a **slope layer mask** for later use, clear, then apply a **Heightfield Noise** set to "Shabby Shapes" combined with **Distort by Layer** to create randomized jagged silhouettes.
6. Blur the heightfield, apply another distortion pass, mask flat areas slightly more than non-flat areas (adding falloff), and use a further noise (with blur) to distort the tops specifically.
7. Clear the mask, run another **Mask Expand** using the "eye" channel to create bulky lower-body shapes, apply a small additional distortion, then **Convert Heightfield** to polygons.
8. **Clip** the extra parts and **Remesh** — heightfield-derived geometry at this stage doesn't work well directly for texturing/displacement without remeshing first.
9. Apply **Subdivide**, then use **Triplanar** displacement (as covered in other tutorials by this author) with two textures blurred normals beforehand to avoid overly wild displacement results.
10. **Ambient Occlusion** calculation for shading/masking use.
11. Add color via a **Point VOP**: right-click to use "sample screen colors," dragging across a reference texture image to sample colors directly onto the geometry — a quick way to add believable variation without full texturing.
12. Since the sampled colors can be too dark, finish with a **Quick Material** to normalize/brighten the output for a presentable render.

### Houdini Nodes / VEX / Settings
Heightfield (draw mask), Heightfield Layer (Maximum blend), Voronoi/Baronoid noise + `random()` with seed, Fit Range, Heightfield Mask Expand (multiple passes, "eye" channel), Heightfield Blur, Heightfield Mask Clear, Heightfield Noise ("Shabby Shapes"), Heightfield Distort by Layer, Convert Heightfield (to polygons), Clip, Remesh, Subdivide, Triplanar (displacement, blurred normals), Ambient Occlusion, Point VOP with "sample screen colors" eyedropper, Quick Material.

### Difficulty
Intermediate (relies on the studio's established Triplanar-displacement workflow; the heightfield mask-layering sequence is approachable once the "distort → mask → blur → clear" rhythm is understood).

### Houdini Version
19.5.593 (visible in viewport title bar).

### Tags
heightfields, terrain, triplanar, displacement, ambient-occlusion, texturing, rocks, environment

---

## Related Tutorials
- [Procedural tips | Heightfields and VDB](procedural-tips-heightfields-and-vdb.md) — companion heightfield-masking tips (bias vs. Mask Expand, Chippy Shapes erosion masking) directly applicable to this workflow.
- [Houdini Heightfields and Cliffs](houdini-heightfields-and-cliffs.md) — related two-pass erosion + third-party texturing approach to heightfield cliffs from the same channel.
- [VDB Procedural Cliffs](vdb-procedural-cliffs.md) — alternate VDB-based (rather than heightfield-based) approach to similar rock-spire silhouettes.
