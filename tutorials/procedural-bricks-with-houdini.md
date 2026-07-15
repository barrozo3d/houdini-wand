---
title: Procedural Bricks with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=-5cycyb5m-E
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.398"
tags: [beginner, hscript-expressions, bricks, procedural-modeling, groups, box-clip, architecture]
extraction_status: complete
frames_dir: tutorials/frames/procedural-bricks-with-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Bricks with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=-5cycyb5m-E)
**Author:** cgside
**Duration:** 4m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello and welcome back. In this video I'm going to show you a simple way of creating brick patterns with Odini.
[0:07] We'll also have a look at some simple H scripts to make it as procedural as it can be.
[0:14] So I have this geometry that I want to transform part of it into bricks.
[0:20] Let's start by creating a subnetwork to have a cleaner graph.
[0:24] Kniving inside we need to select the bottom part where we'll have the pattern.
[0:29] Let me just enable the polycount display as we will need it.
[0:34] As you can see we have 22 primes or faces in this object.
[0:39] Let's select 11 of 22 which is the polycount of this geo.
[0:44] Now we can blast the primes selected previously.
[0:49] Creating a grid as it will be the base of our pattern.
[0:56] Using the match size node we can scale the grid to the same size of the original geometry.
[1:08] Let's separate the faces with the face set nodes.
[1:12] And we can visualize it with the explode view to make sure the faces or primes are indeed separated.
[1:20] Now we need to select every odd or even rows.
[1:23] For that let's use a range.
[1:26] In the first field under the amount of columns, subtracting one,
[1:31] and in the second input we multiply the same columns field by two.
[1:36] Basically we are selecting the amount of faces in the horizontal axis and skipping the same amount.
[1:42] Finally we can offset the selected faces and in this case I want it to be exactly in the middle of the faces above and below.
[1:51] So we need to find a way to make it procedural.
[1:55] As soon as I change the values on the grid it's no longer creating the exact pattern.
[2:01] So let's start by querying the bounding box size of the incoming geometry.
[2:06] And we are getting the expected results of setting exactly by the X size.
[2:12] The next variable we need to take into consideration is the number of bricks in off the grid.
[2:18] So let's divide the previous variable by the number of horizontal bricks in this case the grid columns minus one.
[2:26] And multiply it by two with the required brackets just like with simple math.
[2:35] Now we can change the grid pattern and it will always offset off-brick in the horizontal axis.
[2:42] The next step is to clip the pattern as we have some additional geometry on the sides and for that we can use a box clip node.
[2:51] We want to match the size we had before so we can use the bounding box of the match size both for X and Y.
[3:00] And then center the box clip to the same centroid of the previous geometry.
[3:09] Make sure you spell everything correctly in this case I was missing the end quotes.
[3:14] And as you can see we now have the correct clipping.
[3:21] We just have another problem there are bricks missing on the left hand side but that's an easy fix.
[3:28] Let's just use a transform in between to scale the grid in the X axis.
[3:33] If you need also to scale in the Y there's an extra step we need to center the pivot.
[3:40] Just enter the default variable CXCY and CZ in the pivot translates.
[3:48] Now everything should work as expected.
[3:51] We can scale the pattern, change the amount of bricks and we have a completely procedural system.
[4:00] As a final touch we can extrude a bit the polygons and give it a small bevel to sell the effect.
[4:07] And that's it I'm still a beginner in Odini but as I'm learning I will share a few tips along the way.
[4:13] Let me know if you enjoyed this and see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/procedural-bricks-with-houdini/frame_000.jpg
- [0:55] tutorials/frames/procedural-bricks-with-houdini/frame_001.jpg
- [1:30] tutorials/frames/procedural-bricks-with-houdini/frame_002.jpg
- [2:20] tutorials/frames/procedural-bricks-with-houdini/frame_003.jpg
- [3:15] tutorials/frames/procedural-bricks-with-houdini/frame_004.jpg
- [3:55] tutorials/frames/procedural-bricks-with-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
Build a fully procedural, self-scaling brick pattern using a Grid sized/positioned via **expressions referencing the incoming geometry's bounding box**, so the pattern automatically re-offsets, re-clips, and re-fills correctly if the source geometry or grid resolution changes — applied here to the base of a Gothic cathedral tower.

### Summary
A portion of the tower's polygon faces is selected using the polycount display (`11 of 22`) and blasted off to be replaced by a brick pattern. A Grid is Match-Sized to the extracted section, then Face Set separates each face for an Exploded View check. A **Group by Range** selects every other row/column using an expression based on the grid's column count (columns − 1, and columns × 2) so brick offsetting scales automatically with the grid resolution rather than needing manual re-tuning. The selected faces are offset by exactly half a brick width — calculated procedurally via the incoming geometry's bounding-box X size divided by (grid columns − 1) × 2, so that changing the grid's column count still produces a correctly-centered offset instead of breaking the pattern. A **Box Clip** trims the extra edge geometry using the same bounding box (X/Y) and centroid as reference, and a **Transform** (with pivot correctly centered via `$CX $CY $CZ`) scales the grid to fill in bricks that would otherwise be missing at the edges after clipping. A final small Extrude + Bevel sells the brick relief look.

### Key Steps
1. Identify and isolate the target wall section: enable polycount display, select `11 of 22` faces (matching the target subnet's face count), Blast the selected primitives.
2. Build the base Grid and use **Match Size** to scale it to the exact bounding-box size of the removed geometry.
3. Use **Face Set** to separate the grid's faces, verified visually with Exploded View.
4. **Select every other row/column**: use Group by Range with the first field set to (grid columns − 1) and the second field set to (grid columns × 2) — this expresses "amount of faces horizontally, skip the same amount" procedurally instead of hardcoding numbers.
5. Offset the selected faces horizontally: query the **incoming geometry's bounding-box X size**, divide it by (grid columns − 1) multiplied by 2, and use that value as the offset amount — this keeps the brick stagger exactly centered even if the grid's column count changes later.
6. Clip the pattern: use a **Box Clip** node matched to the original bounding box (both X and Y from Match Size), centered on the same centroid as the source geometry — fixes extra geometry along the sides introduced by the offset grid.
7. Fix missing bricks on the edges left by the clip: add a **Transform** before the clip to scale the grid in X (and Y, if needed) — critically, set the pivot to the default `$CX $CY $CZ` expression variables so scaling happens around the object's own center rather than the world origin.
8. Confirm the whole setup is now fully parametric: changing grid resolution or brick count no longer breaks the offset or clipping.
9. Finish with a small **Extrude** and **Bevel** to sell the 3D brick relief effect.

### Houdini Nodes / VEX / Settings
Subnetwork (clean organization), polycount display, Blast, Grid, Match Size, Face Set, Exploded View, Group by Range (expression-driven: `columns-1`, `columns*2`), Transform (expression-driven offset: `bbox_x / ((columns-1)*2)`), Box Clip (bounding-box + centroid matched), Transform (`$CX $CY $CZ` pivot centering for scale), Extrude, Bevel.

### Difficulty
Beginner (explicitly noted by the author as still learning Houdini), though the expression-driven parametric approach to grid offsetting is a genuinely useful intermediate-level habit.

### Houdini Version
19.5.398 (visible in viewport title bar — same project/session as the Gothic cathedral first-steps video).

### Tags
beginner, hscript-expressions, bricks, procedural-modeling, groups, box-clip, architecture

---

## Related Tutorials
- [Procedural Modeling | First steps with Houdini](procedural-modeling-first-steps-with-houdini.md) — the Gothic cathedral tower this brick pattern is applied to; direct continuation of that build.
- [Ruins randomized brick wall](ruins-randomized-brick-wall.md) — much more advanced brick/wall generation technique (Voronoi Fracture + per-layer randomized jitter) from the same channel's later work.
