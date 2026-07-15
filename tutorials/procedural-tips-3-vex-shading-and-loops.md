---
title: Procedural Tips #3 VEX Shading and Loops
source: YouTube
url: https://www.youtube.com/watch?v=bgUI52CFMLU
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.598"
tags: [vex, for-each-loop, karma, materialx, rotate-to-vector, fetch-feedback, capsule, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-tips-3-vex-shading-and-loops/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Tips #3 VEX Shading and Loops

**Source:** [YouTube](https://www.youtube.com/watch?v=bgUI52CFMLU)
**Author:** cgside
**Duration:** 6m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. In this video I wanted to share a few procedural tips from
[0:06] shading to wax, hopefully you learned something new and you can always grab the project files
[0:13] from my Patreon. So I'm creating some simple procedural buildings and houses and the roof
[0:21] was the trickiest part. As you can see I'm aligning some grids to the roof shape so I can
[0:27] use the subdivisions to instance the tiles. And this is simple enough. Here in a basic
[0:35] scene you can see the setup, starting with the grid, with alternating triangles and moving
[0:41] up the middle points. Computing the normals and extracting the centroid of the frames while
[0:47] transferring the normals along. Here I have the grid to copy over which is laying flat
[0:53] on the ground. Now copying these over won't give us the desired results but that is quite
[1:00] simple to solve. We have the normals already, we just need to create the up attribute pointing
[1:08] in the y axis. And then to align it properly we need to rotate the grid 90 degrees since
[1:15] by default whatever is facing the z axis will align with the normal of the points. And
[1:22] this works even with the largest side of the grid aligning properly. But curiosity got the
[1:30] best out of me and as I am stubborn I wanted to find a solution that didn't rely on the
[1:37] initial orientation of the grids. So as you can see in this setup I have exactly the same
[1:42] result but no transform node neither computed normals. And with a few lines of wax we can calculate
[1:51] a new direction of the normal and use the same up attribute. First I am getting the topmost
[1:58] point with the bounding box max function, then calculating a vector by subtracting the current
[2:04] position from the top point, assigning that vector to the normal and using the same up attribute.
[2:15] As you can see by the visualizers now the normal is pointing towards the center top point
[2:22] and up facing in the y. And I still believe there's even a simpler way to achieve this but
[2:30] that's what I came up with, waiting for your suggestions in the comments. Let's move on.
[2:37] Let's see here I did a shading tutorial using Arnold and Maya on creating this rainbow CD effect
[2:45] and wanted to try it in karma. So we're starting with this type of ramp that we will map to the
[2:52] specular rotation at the end. Not gonna bother you with the mat behind but you can see the steps
[2:59] by my setup. The most important node here is the material X rotate to D that will create the
[3:06] rainbow effect, basically offsetting a few degrees the ramp in each shader. Then I have three
[3:14] different materials where the only difference is the base color, one is red, second is green and third is blue.
[3:22] And finally I am adding them together that should add up to white while creating the rainbow effect
[3:30] on the reflection. For the shaders I just have the ramps connected to the specular rotation and
[3:38] an isotropy and metalness set one. As a final touch I use the grunge texture on the roughness channel
[3:46] using a custom triplanar node. So procedural rocks we all been there and in these basic setup I have
[3:57] few tips. The first one is to use the initial shape copy to a single point with a randomized
[4:03] scale attribute. This allows to change the size and shape of the rock by playing with the seeds
[4:10] of the attribute randomized. Another quick tip are now to use a subdivide node to control the
[4:17] roundness of your rock just by playing with the crease weights and adding one or two subdivisions.
[4:25] Let's add a mountain node to randomize the shape and let's say you don't like the effect on the
[4:32] Y axis mostly on the bottom part. Of course you can remove the Y components on the mountain node
[4:39] but that also gets rid of the noise on top. So what you can do is to create a point for
[4:46] with a noise inside using the display's along normal nodes and to achieve the flattening just on
[4:53] the negative Y you can use a clamp on your normals setting the Y component to 0 on min and the
[5:00] desired amount for positive Y. Okay now an exercise on stacking objects with four loops. In this case
[5:10] I have a simple box and using a forage count to generate more in a loop and to align the boxes we
[5:18] access the previous iteration with a new begin node set this time to fetch feedback.
[5:25] Then we can use the result in a match size to align the new box with the previous one in this
[5:31] case the bottom to the top or min to an max. And in between I'm also randomizing the rotation
[5:40] and scale with the iteration value. So I saved the worst tip for last and it's really simple
[5:48] but since Odinit doesn't have a capsule primitive we can create one just with two nodes.
[5:54] A simple line, a sweep node set to round the tube and the end cap to grid. You can then control
[6:03] the height with the line and the subdivisions with the line points and grid subdivisions.
[6:09] So that's it so hopefully you got something out of this feel free to leave a comment and don't
[6:15] forget you can grab all the files from my videos on Patreon along with exclusive tutorials.
[6:23] Thank you and see you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_000.jpg
- [1:00] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_001.jpg
- [1:40] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_002.jpg
- [2:45] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_003.jpg
- [3:40] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_004.jpg
- [4:20] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_005.jpg
- [5:20] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_006.jpg
- [6:15] tutorials/frames/procedural-tips-3-vex-shading-and-loops/frame_007.jpg

---

## Structured Notes

### Core Technique
A grab-bag of six procedural tips: roof-tile alignment via a manually-computed cross-product normal (vs. relying on grid orientation), a MaterialX Rotate2D-based rainbow-CD shader recreation, several quick procedural-rock modeling shortcuts, a Fetch-Feedback for-loop for stacking objects, and building a capsule primitive from just a Line + round Sweep since Houdini has no native capsule.

### Summary
For roof-tile instancing, rather than relying on a grid's default orientation (needing a Transform + "up" attribute + 90° rotation since Sweep-copied geometry aligns its Z axis to the point normal by default), a VEX-only alternative computes the normal directly: get the topmost point via bounding-box max, subtract the current position from it to get a direction vector, assign that as the normal, and reuse the same up attribute — achieving identical orientation results without any Transform node or precomputed normals. For a MaterialX/Karma recreation of an Arnold/Maya "rainbow CD" reflection shader, a ramp type is mapped to the specular rotation; the key node is **MaterialX Rotate2D**, offsetting the ramp a few degrees per shader instance; three materials (red/green/blue base color) are additively combined so they sum toward white while producing the rainbow reflection effect, with isotropy and metalness set to 1, plus a custom Triplanar grunge texture on roughness. Quick procedural-rock tips: copy the base shape to a single point with a randomized scale attribute (seed-driven variety), use Subdivide's crease-weight controls plus 1-2 subdivisions to control roundness, and to avoid Mountain's Y-axis noise removal also killing top detail, use a Point VOP noise via Displace Along Normal with the normal's Y component clamped (0 on the min side, desired amount on the max) so only the underside flattens. A "stacking objects" for-loop exercise uses a For-Each Count loop with **Fetch Feedback** to access the previous iteration's result, feeding it into Match Size (aligning new box bottom to previous box top) while randomizing rotation/scale per iteration. Finally, since Houdini lacks a native capsule primitive, one is built from just a **Line** + a **Sweep** node set to Round/Tube with an End Cap set to Grid — line length/points control height/subdivisions, and grid subdivisions control the round cap's resolution.

### Key Steps
1. **Roof-tile orientation without a Transform node**: instead of computing normals + up attribute + rotating 90°, use a wrangle to find the topmost point via `bbox_max`, subtract current position to get a direction vector, assign it directly as the normal, and reuse the same up attribute — verified to produce identical results to the Transform-based approach.
2. **Rainbow CD shader**: build a ramp mapped to specular rotation; the key node is **MaterialX Rotate2D**, offsetting the ramp by a few degrees per material instance to create the rainbow effect.
3. Create three near-identical materials differing only in base color (red, green, blue); additively combine them in the shading network so they sum toward white while the reflection shows rainbow banding; set isotropy and metalness to 1; add a **custom Triplanar** grunge texture on roughness as a finishing touch.
4. **Rock modeling tip 1**: copy the base rock shape to a single point with a **randomized scale attribute**, allowing quick size/shape variation just by changing the attribute's seed.
5. **Rock modeling tip 2**: use a **Subdivide** node's crease-weight controls plus 1-2 subdivisions to control overall roundness without extra geometry operations.
6. **Rock modeling tip 3**: to distort a rock with Mountain but avoid killing the desired noise on top when disabling the Y axis to fix bottom distortion, use a **Point VOP** with noise fed through **Displace Along Normal**, clamping the normal's Y component (0 for the min bound, the desired amount for the max) so only the underside is flattened while the top keeps its noise detail.
7. **Stacking objects with a for-loop**: use a For-Each **Count** loop; inside, access the previous iteration's geometry via a new Begin node set to **Fetch Feedback**; feed that into **Match Size** to align the new box's bottom to the previous box's top (or min-to-max); randomize rotation and scale per iteration using the loop's iteration value.
8. **DIY capsule primitive**: since Houdini has no native capsule, build one from just a **Line** node feeding a **Sweep** node set to **Round/Tube** with **End Cap set to Grid** — control height via the line's length/points, and cap resolution via the grid's subdivisions.

### Houdini Nodes / VEX / Settings
Attribute Wrangle (`bbox_max` topmost-point normal derivation, up-attribute reuse), MaterialX Rotate2D (specular-rotation ramp offset), additive material combination (red/green/blue base color sum), custom Triplanar (roughness grunge texture), Copy to Points (single point, randomized scale attribute), Subdivide (crease weights, subdivision count for roundness), Mountain (Y-axis disable), Point VOP (Displace Along Normal, clamped normal-Y noise mask), For-Each loop (Count mode, Fetch Feedback Begin node), Match Size (min-to-max alignment), Transform (per-iteration randomized rotation/scale), Line, Sweep (Round/Tube profile, End Cap set to Grid).

### Difficulty
Intermediate (each tip is a compact, standalone technique; the Fetch-Feedback loop and clamped-normal noise mask are the more advanced items).

### Houdini Version
19.5.598 (visible in viewport title bar).

### Tags
vex, for-each-loop, karma, materialx, rotate-to-vector, fetch-feedback, capsule, procedural-modeling

---

## Related Tutorials
- [Procedural Roof Tiles in Houdini](procedural-roof-tiles-in-houdini.md) — deeper dive into the same roof-tile orientation problem this video offers a VEX shortcut for.
- [Infinite Mirror in Karma XPU](infinite-mirror-in-karma-xpu.md) — related Karma material trick from the same channel using layered reflective shading.
- [Procedural Hard Surface Modeling Tips](procedural-hard-surface-modeling-tips.md) — companion grab-bag tips video with similar VEX/attribute-based problem-solving format.
