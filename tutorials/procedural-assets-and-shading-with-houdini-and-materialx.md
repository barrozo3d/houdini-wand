---
title: Procedural assets and shading with Houdini and MaterialX
source: YouTube
url: https://www.youtube.com/watch?v=fSouWuGd_Tg
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.403"
tags: [materialx, karma, vex, food, procedural-modeling, solaris, spiral, normals]
extraction_status: complete
frames_dir: tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural assets and shading with Houdini and MaterialX

**Source:** [YouTube](https://www.youtube.com/watch?v=fSouWuGd_Tg)
**Author:** cgside
**Duration:** 4m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi there and welcome back. So in this video I'm going to walk you through a simple setup for creating procedural assets in Odini and
[0:08] I will look at Karma and material X noises for procedural shading.
[0:14] The project files for this video will be uploaded to Patreon if you want to dissect it.
[0:20] So for the individual bananas, I just use the mix of procedural and direct modeling techniques
[0:26] but you can just replace it with a banded tube with some tapering.
[0:31] I also painted a mask to use in salaries.
[0:35] So for the bench that looks like this, I started with a tube,
[0:40] selected a few faces with the range nodes,
[0:43] add a mirror for two layers of bananas and
[0:47] Extracted the centroid where I'll be placing them.
[0:51] Okay, now we need to add normals to worry on the bananas.
[0:55] In this wrangle, the first part is to create normals that point outwards.
[1:00] Then I am flattening the normal Y-axis.
[1:03] After that, I am creating a blend slider so I can mix the two normals orientation,
[1:09] which I am doing with the layer function. The last line just sets the attributes to the positive Y-axis.
[1:16] If I play with the blend slider, you can see how I can edit the orientation of the normals,
[1:23] making them more or less flat.
[1:26] You're just randomizing a bit the normals so I can have a less uniform distribution of the banana bunch.
[1:35] Okay, now we need to place the cluster of bananas in the main stem.
[1:40] And for that, I am starting with the line with the same size of the tube that acts as the stem.
[1:46] Adding a mountain node to break the uniformity,
[1:50] carving it so I can control where the banana bunch starts and ends along the stem,
[1:57] resembling it and adding some jitter to the Y-axis.
[2:03] Now adding normals along the X-axis.
[2:06] And here is where we orient the point so we have a spiral effect.
[2:12] So I am creating a variable where I set an interval of rotation around 90 degrees with some seed.
[2:20] Then for each point, I multiply the point number by the rotation amount,
[2:25] creating that way the spiral effect.
[2:30] Also adding some random scale for each cluster.
[2:35] And of course copying the banana cluster to these points.
[2:39] For the stem, a simple tube with a mountain node to affect the position and some gravity ends.
[2:46] Then in order to target the different parts in Solaris, I am adding a name for the stem and the bananas.
[2:52] And that's about it for the subset up.
[2:56] So the first thing you want to do in Solaris when you import back geo is to set those primitives to be a point insta-ser.
[3:05] As for the shading, first I am importing the mask for the tips of the bananas using the Geo property value nodes.
[3:15] Then using a color mix, I am assigning a dark brown to the tip and some other color mix downstream.
[3:24] Here I am using 3D noises and in order to tile them, you need to connect a position node with a multiply
[3:31] where you set the amount of repetitions you want.
[3:36] Then in the mix I am adding bits of grid.
[3:39] The last mix just blends the main yellow color with some brown using a fractal 3D noise.
[3:47] As for the shader itself, there's just some mid-graphness values and a bit of SSS.
[3:54] So that's about it. Hopefully you picked up a few tips. There are still some inconsistencies in this setup
[4:01] like avoiding intersections between the bananas or really simple shading setup.
[4:08] But hopefully I can cover that in another time.
[4:11] Don't forget to check out my Patreon if you want to support the channel and download the project files.
[4:17] Thank you and see you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_000.jpg
- [0:45] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_001.jpg
- [1:15] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_002.jpg
- [1:50] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_003.jpg
- [2:25] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_004.jpg
- [2:55] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_005.jpg
- [3:50] tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/frame_006.jpg

---

## Structured Notes

### Core Technique
Build a banana bunch procedurally by blending outward-pointing and Y-flattened normals (for controllable "flatness" of individual banana clusters), then placing clusters along the main stem in a spiral pattern via a VEX rotation-per-point-number trick, and shade everything with tileable 3D MaterialX noises in Karma.

### Summary
Individual bananas use mixed procedural/direct modeling. On the bunch, faces are selected via range nodes, mirrored for two layers, and the centroid extracted as the placement anchor. A wrangle creates outward-pointing normals, flattens the Y component, and blends the two orientations with a slider using `lerp()`, letting the artist dial in how "flat" vs "pointing out" each bunch looks, then locks the normal to positive Y; slight randomization avoids a too-uniform bunch distribution. The main stem placement uses a Line matching the tube's size, a Mountain node for non-uniformity, Carve to control where the bunch starts/ends along the stem, Resample, and Y-jitter. Normals along X are added, and the **spiral placement trick**: a variable sets a ~90° rotation interval with a seed, then for each point the point number is multiplied by that rotation amount — creating the spiral effect around the stem. Random per-cluster scale is added before Copy to Points places the banana clusters. The stem itself is a simple tube with a Mountain node affecting position, plus gravity-like bending. Names are added for Solaris targeting (stem vs. bananas). In Solaris, primitives are set to be a point instancer; shading uses a Geo Property Value mask for banana tips (dark brown via Color Mix), tiled 3D MaterialX noises (tiled by multiplying the Position node output by a repetition-count constant before feeding the noise), a grid-blend layer, and a final mix blending main yellow with brown via a fractal 3D noise; the shader itself uses modest roughness values and some SSS.

### Key Steps
1. Model individual bananas via a mix of procedural and direct modeling (details left to project files); build the bench/bunch base from a tube.
2. Select a subset of tube faces with Range nodes, Mirror for two layers of bananas, and extract the **centroid** as the eventual placement point.
3. **Orientation wrangle**: create normals pointing outward, flatten the Y component of a second normal copy, blend the two with a slider (`lerp()`-based mixing function) to control how flat vs. outward-facing each cluster is, then lock the resulting attribute to point along positive Y — visually tunable via the blend slider.
4. Randomize the normals slightly for a less uniform bunch look.
5. **Main stem placement**: build a Line matching the stem tube's size, add a Mountain node for non-uniformity, use **Carve** to control where along the stem the bunch starts/ends, Resample, and jitter along Y.
6. Add normals along X, then implement the **spiral effect**: define a rotation-interval variable around 90° with a random seed, and for each point multiply the point number by that rotation amount — producing a spiraling placement pattern up the stem.
7. Add random scale per cluster, then **Copy to Points** to place the banana clusters along the spiral.
8. Build the stem geometry itself from a simple tube with a Mountain node affecting position plus a gravity-like bending end.
9. Add name attributes for the stem and bananas separately, for targeted material assignment in Solaris.
10. **Solaris setup**: set the imported geo's primitives to be a **point instancer**.
11. **Shading**: import a banana-tip mask via **Geo Property Value**, use Color Mix to assign a dark brown tip color, then blend downstream with more Color Mix nodes.
12. Use **3D MaterialX noises**, tiled by connecting a **Position** node through a **Multiply** by a repetition-count constant before feeding the noise (standard tiling trick for 3D noise in MaterialX).
13. Add a grid-blend mix layer, then a final mix blending the main yellow banana color with brown using a **fractal 3D noise**.
14. Shader itself uses modest roughness values with a bit of SSS for a believable banana-peel look.

### Houdini Nodes / VEX / Settings
Range (face selection), Mirror, Extract Centroid, Attribute Wrangle (outward normal, Y-flatten, `lerp()` blend slider, lock to +Y, randomize), Line, Mountain, Carve, Resample, Jitter, Normal (X-axis), VEX rotation-per-point-number spiral wrangle (seeded interval ~90°), Attribute Randomize (per-cluster scale), Copy to Points, Tube (stem, Mountain-driven bend), Name attribute, Solaris point instancer flag, Geo Property Value (tip mask), Color Mix, MaterialX 3D noise (Position × repetition-constant tiling trick), Fractal 3D noise (yellow/brown blend), Standard Surface shader (roughness, SSS).

### Difficulty
Intermediate (the spiral-placement VEX trick and normal-blend orientation wrangle are the standout non-obvious techniques; overall pipeline is approachable).

### Houdini Version
19.5.403 (visible in viewport title bar).

### Tags
materialx, karma, vex, food, procedural-modeling, solaris, spiral, normals

---

## Related Tutorials
- [Procedural Fries with MtlX and Karma XPU](procedural-fries-with-mtlx-and-karma-xpu.md) — related MaterialX food-shading technique from the same channel.
- [Modeling Assets with Vellum](modeling-assets-with-vellum.md) — shares the same channel's food-modeling focus, using Vellum instead of pure procedural placement.
