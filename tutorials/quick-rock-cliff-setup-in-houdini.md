---
title: Quick Rock Cliff Setup in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=iSIXaa3rknU
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.598"
tags: [vdb, triplanar, boolean, displacement, megascans, environment, rocks, composite]
extraction_status: complete
frames_dir: tutorials/frames/quick-rock-cliff-setup-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Quick Rock Cliff Setup in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=iSIXaa3rknU)
**Author:** cgside
**Duration:** 7m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. So today I wanted to share with you how I created this rock
[0:06] like surface or cliff. So basically I am starting with a curve. This is a setup that I
[0:18] saw online on 80 level I believe. So I am starting by drawing a curve. Then I'm extruding
[0:27] it up and I'm also outputting the textured back seam and grouping also the middle seam since
[0:40] I am adding a subdivision. Then I'm extruding the volume to create this shape and piercing
[0:55] the points. This is one side of the branch. Then I am copying two points a few boxes, nothing
[1:03] special with the box. Just a box scaled in Y. We're matching it a bit, blurring the normals and using a
[1:16] mount and saw. Then I am just using a Sphereify P. I believe preset to just smooth out the initial shape.
[1:30] And I'm doing these in a loop. So for the point let me just show you the points. I am extracting
[1:40] those two edge loops and re-sampling it, removing the curves and just give two points, adding a
[1:52] point heater and some randomization of P scale and the orientation. This script I shared before in
[2:00] the channel. And I am copying two points in a loop, something like this, because I want to change a bit
[2:11] the amplitude with a fit function and the offset of the noise. In the end doesn't really make that
[2:20] difference but just in case. So after copying the shapes I am boolean, I am doing a boolean
[2:35] and I get something like this. Then I'm deleting the small parts,
[2:40] fusing and remashing. So we get these regular shapes. Then I am using VDB from polygons and
[2:53] converges to smooth out the shape as you can see. Then I am doing a remash
[3:07] and clipping the back and the bottom, because we don't need those extra polygons.
[3:15] The leading again the small parts, there are some extra pieces. And I'm applying a subdivision before I
[3:25] use the triplanar displays notes. But in this case I am not using it to this place. I am using it for
[3:37] color. As you can see I am just using the color here. And I'm doing that for two different textures
[3:46] that will be used for displacement later in the point of op. And two colors just to visualize the
[3:55] some texture. One grass texture for the top and one rock surface for the front side.
[4:09] I am also blurring the normals just in case the displacement goes a bit wild.
[4:16] Now in the point op, if I enable the subdivision, it takes a little bit because I am subdividing it
[4:31] three times. So as you can see we get the color and the displacement. Let me show you what's
[4:44] going on in the point op. As I told you before I am I have two textures for displacement and two
[4:53] for color. We will ignore the the last ones for the color because it's just a previous visualization
[5:03] here. We won't actually use this for final render. So for the displacement I'm importing the first
[5:12] one which is just directly to the CD. And I'm importing the second one just in part point
[5:20] attribute and the CD. And I'm compositing it. I'm mixing the two textures with a composite mode.
[5:28] In this case I set it to darken. You can try overlay. You can try lighten depending on the input
[5:36] textures. These are just mega-scan textures and that's why I'm also remapping them
[5:45] between minus point five and point five. Then I'm just displacing. You can play with the amount.
[5:55] And I don't want displacement on top. So what I'm doing I'm taking the initial position.
[6:03] And mixing it with the position from the displacement. So I have the the y component is the original
[6:13] position. It's from the original position and the x and z is from the displacement. So I can
[6:22] assign it to the new position. As for the color it's not really important but you can have a look
[6:32] at the file in my Patreon if you are interested. So yeah that's basically it.
[6:40] Then you can reduce it because this is a bit typoly. You can reduce it and delete any x
[6:48] reparts. So yeah that's basically it. If you want you can have a look at my at the file on my
[6:55] Patreon I will be uploading there. And yeah thank you for watching. See you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_000.jpg
- [1:00] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_001.jpg
- [1:40] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_002.jpg
- [2:30] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_003.jpg
- [3:40] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_004.jpg
- [4:40] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_005.jpg
- [5:40] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_006.jpg
- [6:30] tutorials/frames/quick-rock-cliff-setup-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Build a rock cliff face by copying mountain-distorted, sphereized boxes along a hand-drawn ground-profile curve, Boolean-merging them into a single mass, VDB-smoothing the result, then driving both displacement and color entirely through a **Point VOP compositing two Megascans displacement/color texture pairs** (mixed with a Composite node) instead of a single texture.

### Summary
A curve is drawn to define the cliff's ground silhouette; it's extruded upward, with the back seam and middle seam grouped for later use, then extruded again and pierced open on one side (one side of the branch). Boxes (scaled in Y) are copied onto resampled/point-heated points along two edge loops (with randomized p-scale and orientation, reused from an earlier shared script), matched, normal-blurred, and Mountain-distorted, then run through a Sphereify preset to round out the shapes; two separate copy passes use slightly different Fit-function amplitude/offset values on the noise for variation. The pieces are Boolean-merged, small parts deleted, fused, and Remeshed for regular topology, then converted to VDB and back (Convert VDB) to smooth the surface. After clipping the back/bottom (unneeded polygons) and deleting small parts again, a Subdivide precedes Triplanar — but here Triplanar is used purely for **color**, not displacement: two different Megascans textures (one grass, one rock) are sampled for color, later used for displacement in the Point VOP. Normals are blurred beforehand to keep displacement well-behaved. In the **Point VOP**, the first texture's color goes straight to Cd; the second is imported as a separate point attribute and also assigned to Cd, then the two are **mixed via a Composite node set to Darken** (Overlay/Lighten also suggested as alternatives depending on input textures) — Megascans textures are remapped between -0.5 and 0.5 before use since raw values aren't centered for displacement. The mixed result finally displaces the geometry, but selectively: the **Y component keeps the original position** (undisplaced) while X/Z take the displaced position, assigned back as the new point position, so the top of the cliff isn't affected by displacement while the front face gets full detail.

### Key Steps
1. Draw a ground-profile **curve**, Extrude it upward, output the texture-back seam and group the middle seam for the next steps.
2. Extrude the volume again to build the branch shape, piercing one side open.
3. Extract two edge loops, resample and remove the curves (keep points), add a **Point Heater** with randomized p-scale/orientation (reused script from earlier videos).
4. **Copy boxes** (scaled in Y) to these points in a loop, varying the Fit-function amplitude/offset of the driving noise slightly between passes for variety.
5. **Match Size**, blur normals, apply **Mountain** distortion, then a **Sphereify** preset to round the boxes into organic rock-like lumps.
6. Merge all copied shapes, **Boolean** them together into a single mass.
7. **Delete small parts**, **Fuse**, and **Remesh** for regular, clean topology.
8. Convert to **VDB from Polygons** then back (**Convert VDB**) to smooth the surface further.
9. **Clip** the back and bottom (unneeded extra polygons), delete small parts again, and **Subdivide** before texturing.
10. Apply **Triplanar** for **color only** (not displacement): sample one Megascans grass texture and one Megascans rock texture for their respective color outputs, remapping both textures between **-0.5 and 0.5** since raw Megascans textures aren't centered for displacement use.
11. In a **Point VOP**: assign the first texture's color to `Cd`; import the second texture as a separate point attribute, also assigning it to `Cd`; mix the two Cd values with a **Composite node set to Darken** (try Overlay/Lighten depending on your specific input textures).
12. **Displace** using the mixed result, but selectively reconstruct the final position: keep the **original Y** (undisplaced, so tops stay clean) while taking the **displaced X and Z**, then assign this composite vector as the new point position.
13. Reduce polycount and delete any extra parts for the final optimized cliff asset.

### Houdini Nodes / VEX / Settings
Curve, Extrude (back-seam + middle-seam groups), Resample, Point Heater (randomized p-scale/orientation), Copy to Points (looped with varying Fit-function noise amplitude/offset), Match Size, Attribute Blur (normals), Mountain, Sphereify preset, Boolean, Delete Small Parts, Fuse, Remesh, VDB from Polygons + Convert VDB (smoothing round-trip), Clip, Subdivide, Triplanar (color-only sampling, two Megascans textures), Fit Range (-0.5/0.5 remap), Point VOP (Cd assignment, Composite node — Darken/Overlay/Lighten mix, selective Y-preserving position reconstruction).

### Difficulty
Intermediate (the selective-axis displacement trick and dual-texture Composite mixing are the standout non-obvious techniques; overall pipeline reuses established studio patterns).

### Houdini Version
19.5.598 (visible in viewport title bar).

### Tags
vdb, triplanar, boolean, displacement, megascans, environment, rocks, composite

---

## Related Tutorials
- [RBD rock surfaces with Houdini](rbd-rock-surfaces-with-houdini.md) — alternate rock-cliff generation approach (RBD Material Fracture) from the same channel, targeting a similar visual result.
- [Houdini Heightfields and Cliffs](houdini-heightfields-and-cliffs.md) — related two-pass texturing approach for cliffs using third-party materials instead of the Composite-mixed dual-texture method here.
