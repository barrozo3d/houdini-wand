---
title: Procedural Rock Formations  Part 2
source: YouTube
url: https://www.youtube.com/watch?v=6GV1b8Ed_JI
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.752"
tags: [rbd, fracture, vdb, triplanar, shortest-path, vines, procedural-modeling, rocks, environment, texturing]
extraction_status: complete
frames_dir: tutorials/frames/procedural-rock-formations-part-2/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Rock Formations  Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=6GV1b8Ed_JI)
**Author:** cgside
**Duration:** 3m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. Let's see how we can create some rock formations using very basic techniques in Odini.
[0:08] We start by fracturing a cube and transforming it so we get dollar shapes.
[0:15] In this loop I am applying some edge damage and placing the assets in the center.
[0:20] We will copy these shapes to some points and starting with a circular patch I am creating a naturoput mask that goes from the edges to the center so I can manipulate the scale of the shape.
[0:35] Remapping the values and in here I am assigning that attribute to the scale Y so I can get longer shapes at the center.
[0:43] Then randomizing a bit the scale and the normals and of course scattering some points.
[0:50] And when we copy to points we get this sort of follow from the center to the edges created by the scale attribute and the initial mask.
[1:01] Okay in the next step I am applying some volume noise to break the surface using VDVs.
[1:07] Nothing I haven't shared before if you've been following this series.
[1:14] Then I am remashing in this case in a compiled loop so it goes a bit faster.
[1:20] From here I am applying some triplanar textures for displacement and also some quick texturing.
[1:28] And in the point of up I am displacing the geo and exporting the texture attributes like the grass texture.
[1:37] We will also need some procedural maps for texturing like the slope and the curvature and finally we can apply some textures to the model.
[1:52] In this case using a few color mix notes to blend between textures using the respective procedural maps.
[2:01] Then just assigning some quick material for preview purpose.
[2:07] So just to finish we can use the shortest path notes to create some vines at the bottom.
[2:16] I am creating a start point group at the bottom creating a mask along the Y axis and keeping the bottom part where I will have the vines.
[2:28] Now we need the end points so for that I am just creating a random selection of points and we can create the shortest path from the initial point to all the end points.
[2:40] From there we just sweep it, add some UVs and finally a quick material.
[2:48] Might not be the most convincing vines but it will do the trick.
[2:54] So there you go some quick setup I wanted to share with you and feel free to grab the file on my Patreon.
[3:01] Hopefully you get away with some new techniques for your next project.
[3:07] Thank you for watching and see you soon as Adini20 is around the corner.



---

## Captured Frames

- [0:10] tutorials/frames/procedural-rock-formations-part-2/frame_000.jpg
- [0:35] tutorials/frames/procedural-rock-formations-part-2/frame_001.jpg
- [1:05] tutorials/frames/procedural-rock-formations-part-2/frame_002.jpg
- [1:30] tutorials/frames/procedural-rock-formations-part-2/frame_003.jpg
- [2:00] tutorials/frames/procedural-rock-formations-part-2/frame_004.jpg
- [2:30] tutorials/frames/procedural-rock-formations-part-2/frame_005.jpg
- [2:55] tutorials/frames/procedural-rock-formations-part-2/frame_006.jpg

---

## Structured Notes

### Core Technique
Build layered rock formations from fractured/transformed boulder shapes, arranged using a radial normal-based mask (edge-to-center) to control per-piece scale, then add VDB surface breakup, Triplanar texture blending, and finish with a Find Shortest Path-based vine generator along the surface.

### Summary
A cube is fractured and transformed into "boulder" shapes, given edge damage, and centered as reusable assets. These are copied onto scattered points over a circular patch, where a **radial mask (normalized distance from edge to center)** drives the Y-scale (longer shapes toward the center) via Remap, plus randomized overall scale/normal jitter — producing a natural mounded arrangement. VDB volume noise breaks up the merged surface (standard technique from the series), followed by a **compiled Remesh loop** for speed. Triplanar textures drive both displacement and quick color blending via multiple Color Mix nodes keyed to procedural slope/curvature maps, with a Quick Material for preview. Finally, **Find Shortest Path** creates simple vines: a start-point group is built at the bottom of a Y-axis mask, random end points are chosen higher up, and the shortest path between them is swept with UVs and a quick material for a rough but effective vine effect.

### Key Steps
1. Base assets: fracture a cube, transform pieces into boulder-like shapes, apply edge damage in a loop, and place assets at the center for reuse as copy-to-points sources.
2. Build the radial mask: on a circular patch, create a natural-log/point-based mask that goes from the edges to the center of the patch.
3. **Remap** the mask values and assign the result to the **scale Y attribute**, producing longer shapes concentrated at the center.
4. Randomize overall scale and normals, scatter points on the patch, then **Copy to Points** — the earlier mask + scale attribute creates a natural flow effect from center to edges across the copied boulders.
5. Apply **VDB volume noise** to break up the merged surface (same technique used throughout this tutorial series).
6. **Remesh inside a compiled loop** for faster iteration on the broken-up surface.
7. Apply **Triplanar textures** for displacement, plus separate procedural texturing.
8. In a Point VOP, displace the geometry and export texture attributes (e.g. grass texture) using generated procedural maps: **slope** and **curvature**, which drive multiple **Color Mix** nodes to blend between different textures.
9. Assign a **Quick Material** for preview purposes.
10. **Vines**: create a start-point group at the bottom by masking along the Y axis and keeping only the lower part; create random end points higher up; run **Find Shortest Path** from the start point to all end points.
11. **Sweep** the resulting shortest-path curves, add UVs, and apply a quick material — described as "not the most convincing vines, but it'll do the trick."

### Houdini Nodes / VEX / Settings
Fracture (cube), Transform (boulder shaping), edge-damage loop, radial mask (natural log/point-distance based), Remap (mask → scale Y), randomized scale/normal jitter, Scatter, Copy to Points, VDB volume noise (surface breakup), compiled Remesh loop, Triplanar (displacement + color), Point VOP (slope/curvature procedural maps, Color Mix blending), Quick Material, Find Shortest Path (start/end point groups, Y-axis masking), Sweep (vine geometry), UVs.

### Difficulty
Intermediate (builds directly on earlier videos in the same series; the Find Shortest Path vine trick is a nice standalone technique).

### Houdini Version
19.5.752 (visible in viewport title bar).

### Tags
rbd, fracture, vdb, triplanar, shortest-path, vines, procedural-modeling, rocks, environment, texturing

---

## Related Tutorials
- [Procedural tips and tricks in Houdini 20.5](procedural-tips-and-tricks-in-houdini-205.md) — shares the Find Shortest Path technique used here for vines, applied there to jewelry stone-holder wire meshes.
- [Environments in Houdini Part 4 - Vines, Rocks and Fog](environments-in-houdini-part-4---vines-rocks-and-fog.md) — related vine-generation technique (`pcopen()`-based attachment mask) from the same channel, useful to compare against this Find Shortest Path approach.
- [VDB Procedural Cliffs](vdb-procedural-cliffs.md) — shares the same VDB surface-breakup technique referenced as "nothing new" in this video.
- [Rock formations with heightfields](rock-formations-with-heightfields.md) — alternate heightfield-based approach to similar rock formation goals.
