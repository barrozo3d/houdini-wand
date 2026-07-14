---
title: Houdini Procedural Tips | Variants, Concentric Shapes and Step Orient
source: YouTube
url: https://www.youtube.com/watch?v=ItIlLC6mlF4
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, procedural, scattering, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini Procedural Tips | Variants, Concentric Shapes and Step Orient

**Source:** [YouTube](https://www.youtube.com/watch?v=ItIlLC6mlF4)
**Author:** cgside
**Duration:** 4m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. In this video I'll share three different procedural setups in Odini.
[0:06] So I saw a video from the Maxon team on how to generate variations by combining different pieces of geometry
[0:14] and after some digging and help from Fanolis on Discord, here's the setup.
[0:21] Starting by generating the Geo, I have three different variations, creating a connectivity attribute, named Class and packing the Geo.
[0:32] Doing the same for the stems and let's call it flowers.
[0:37] Merging everything and then generating a new connectivity this time a name attribute.
[0:44] Then we unpack and iterate over each named primitive.
[0:50] As you can see we have the vases in the first iteration. Now using the attribute from pieces we can randomly select a piece and copy to points.
[1:00] I also randomize the seed attribute based on the iteration.
[1:04] Running the look for the necessary amount we get a random piece being copied to each point and many different variations only limited by the amount of input Geo you have.
[1:17] And of course you need to use the piece attribute on the copy to points node.
[1:23] This next tip is on generating concentric shapes. In this case I want to generate them in multiple pieces otherwise I wouldn't need the look.
[1:34] So iterating over each primitive, grouping the unshared edges and converting it to a curve.
[1:42] Extrusting the centroid and placing the shape in the center since we will copy it to points.
[1:48] Now we generate points, set the amount according to the number of copies you need.
[1:53] Then we will need an ID or index attribute on the points.
[1:58] And we manipulate the p-scale with a naturoputor just float using a remap attribute option, setting a min and max scale and finally remapping the index from 0
[2:10] to the amount of points we have.
[2:13] This part of the setup was shared by Aconoclastis on Discord also.
[2:19] Make sure to join the ThinkPrecetral server.
[2:23] So if we copy the points we have the desired result.
[2:27] Now if we run the look we do get a decent result but some of the shapes have their center bit of.
[2:36] In this shape for instance we have the centroid a bit of center.
[2:40] So what we can do instead is to measure the centroid instead which will give us a better result.
[2:51] Having the new centroid we want to move the shape to the center of the world but we did center based on the centroid.
[3:00] And that's what I'm doing in this wrangle calculating the offset between the centroid and the origin and moving the shape.
[3:13] And that's about it.
[3:17] Now for the last tip on step orientation which can be easily achieved with a scatter and a line using the round two feature.
[3:27] The only downside is that you don't really have a seed attribute for the orientation.
[3:34] So I have a Vax option that generates random rotations and then rounds it to the step we want with a seed and also a angle variation on top of the step orient.
[3:46] So we can add a small offset.
[3:51] So yeah that's what I have for today as always you can grab the file from my Patreon and if you enjoy this check out my procedural courses on the link below.
[4:02] Thank you and see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/frame_000.jpg
- [1:10] tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/frame_001.jpg
- [2:00] tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/frame_002.jpg
- [2:45] tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/frame_003.jpg
- [3:30] tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/frame_004.jpg

---

## Structured Notes

### Core Technique
Three community-sourced procedural tricks: generating combinatorial geometry **variants** (e.g. vase + stem/flower combos) via packed-piece random selection inside a for-each loop, building **concentric radial shapes** from unshared-edge boundary curves with a centroid-corrected re-centering fix, and adding a **seeded step-orient** to Scatter/Copy to Points setups (which natively lack a rotation seed) via a custom VEX rounding trick.

### Summary
**Variant generation** (adapted from a Maxon-team technique, refined with Discord help): each geometry category (e.g. 3 vase variations, 3 stem/flower variations) gets its own **Connectivity** attribute named `class` and is Packed; all categories are merged, then a second Connectivity pass assigns a `name` attribute across the whole merged set. Inside a **For Each (named primitive)** loop, the geometry is unpacked and, using **Attribute from Pieces**, a random piece is selected per iteration (with the loop's iteration number feeding the random seed for reproducible-but-varied results per point) and fed into **Copy to Points** — critically requiring the **"piece" attribute** to be set on Copy to Points so it knows to distribute per-piece rather than copying the whole merged set. Running the loop once per geometry category (vases, then stems/flowers) produces a combinatorial explosion of variations limited only by how much source geometry is fed in. **Concentric shapes**: built per-piece inside a loop (a single shape wouldn't need the loop) by grouping each primitive's unshared/boundary edges, converting to a curve, and initially recentering via **Extract Centroid** — but the author found the extracted centroid can sit visibly off-center for asymmetric shapes, so instead a **Measure** (Centroid) pass computes a truer centroid, and a wrangle computes the offset between that measured centroid and the world origin, moving the shape there for reliable re-centering before it's copied outward. Points for the radial copies are generated with a count matching the desired number of concentric rings; each point gets an **index/ID attribute**, and `pscale` is driven by an **Attribute Adjust Float** using its Remap-Attribute option (setting min/max scale, remapping the index attribute from 0 to the total point count) — producing a smooth inner-to-outer scale gradient when the shape is Copied to Points onto them (credited to a separate Discord contributor). **Step-orient with a seed**: Scatter + Line's built-in "Round To" step-orientation feature works but has no seed attribute for the rotation itself, so a VEX approach instead generates a fully random rotation, rounds it to the desired step increment with a controllable seed, and adds a small extra angle-variation on top of the stepped result for a touch of natural irregularity beyond the rigid stepping.

### Key Steps
1. **Per-category packing:** for each geometry category (e.g. 3 vase variants), run **Connectivity** (named `class`) then **Pack**; repeat for each other category (e.g. stems/flowers).
2. **Global naming pass:** **Merge** all packed categories together, then run a second **Connectivity** producing a `name` attribute spanning the whole combined set.
3. **Per-object random selection loop:** inside a **For Each (named primitive)** loop, Unpack the current object's pieces, use **Attribute from Pieces** to randomly select one piece per iteration (seeding the random pick from the loop's iteration number for repeatable-but-varied results), and feed the selection into **Copy to Points**.
4. **Enable piece-based copying:** on Copy to Points, set the **"piece" attribute** parameter so it distributes the randomly-selected individual piece per point rather than the whole merged geometry.
5. **Iterate per category:** run the loop for each geometry category needed (vases in one pass, stems/flowers in another) to build the final combinatorial variant scene — total unique combinations scale with however much source geometry is supplied.
6. **Boundary curve per shape (concentric setup):** inside a per-piece loop, group each primitive's unshared/boundary edges and convert to a curve, forming the base radial "petal"/ring shape.
7. **Initial (flawed) recentering attempt:** **Extract Centroid** to move the shape toward the origin — works for symmetric shapes but can leave the centroid visibly off-center for irregular/asymmetric shapes.
8. **Corrected recentering:** use **Measure** (Centroid mode) to compute a true geometric centroid, then a wrangle computing the offset between that centroid and world origin and subtracting it from `P` — reliably centers any shape regardless of asymmetry.
9. **Radial point generation:** generate points equal to the desired number of concentric copies; assign each an **index/ID** attribute.
10. **Scale gradient via Remap Attribute:** use **Attribute Adjust Float**'s Remap Attribute option — set min/max scale values and remap the index attribute's range (0 to point count) — producing `pscale` values that smoothly grow (or shrink) from center to edge.
11. **Final copy:** **Copy to Points** the corrected, centered shape onto the scaled radial points for the finished concentric-ring result.
12. **Seeded step-orient (VEX):** in place of Scatter/Line's native "Round To" step feature (which lacks a rotation seed), write a VEX snippet that generates a fully random rotation, **rounds it to a chosen step increment** using a controllable seed parameter, then adds a small extra random angle-variation on top of the stepped value for subtle natural irregularity beyond rigid, perfectly-even stepping.

### Houdini Nodes / VEX / Settings
Nodes: Connectivity (`class` and `name` attribute modes), Pack, Merge, Unpack, For Each (named primitive), Attribute from Pieces (random piece selection, iteration-seeded), Copy to Points (piece attribute enabled), Group (unshared/boundary edges), Convert Line, Extract Centroid, Measure (Centroid mode), Attribute Wrangle (VEX: centroid-to-origin offset calculation and repositioning; step-orient rotation — random angle generation, step-rounding with seed, added angle variation), Attribute Adjust Float (Remap Attribute option: min/max scale, index-attribute remap range), Scatter, Line (Round To step-orient feature, native limitation: no rotation seed).

### Difficulty
Intermediate — each tip is compact but assumes comfort with for-each loops, attribute-from-pieces workflows, and basic VEX for the custom step-orient rotation logic.

### Houdini Version
20.5 (UI matches Houdini 20.5-era toolset).

### Tags
#vex #procedural #scattering #tips #intermediate

---

## Related Tutorials
Cross-link with groups-patterns-in-houdini.md and essential-procedural-techniques-in-houdini.md (same author, overlapping VEX-tips/procedural-selection format) once indexed together.
