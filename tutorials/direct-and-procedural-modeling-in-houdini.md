---
title: Direct and Procedural Modeling in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=t1QemBG462g
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, vex, procedural, hard-surface, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/direct-and-procedural-modeling-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Direct and Procedural Modeling in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=t1QemBG462g)
**Author:** cgside
**Duration:** 4m15s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello and welcome everyone! In this video I'll share some of the things I learned while modeling this asset in Odini.


### Select by pattern [0:07]
**Transcript (timestamped):**
[0:07] So the first tip is on how to use smart direct selections.
[0:14] Having these two, I can select a pattern and expand the selection accordingly by using Shift-Up Arrow to expand forward.
[0:27] Now I can continue modeling by extruding the frames and then select again a new pattern if I want to manipulate the inner faces.
[0:35] And you can also select by normal, interactively in the viewport, which can be really handy for quick selections.


### Clean draw curve results [0:43]
**Transcript (timestamped):**
[0:44] Now there was a pattern I needed to recreate on this bottle and the easiest way I found was to draw the pattern directly by using the draw curve.
[0:53] But as you can see it's all over the place, it's hard to get a clean result from the draw curve.
[1:00] So to clean it up I start by clipping them to have the same main points.
[1:05] Then I do a big resample to just get the overall curvature and finally I can resample with a smaller length and subdivide the curves.
[1:15] We end up with a clean result.


### Facet node vs neighbours count [1:18]
**Transcript (timestamped):**
[1:19] As you can see I have these extra points from a Boolean operation and to clean them I tried using a facet node and play with the tolerance to remove the inline points.
[1:30] But unfortunately could not get it to work as it ended up deleting parts of the geo and that's when Vex comes in handy.
[1:41] So I am just using the neighbors count function to group any points that I have two or less neighbors and then blasting the grouped points.


### Fuse to target geometry [1:52]
**Transcript (timestamped):**
[1:52] So on the same subject after the Boolean I ended up with some bad topology and another technique I used to clean it was to fuse the border points.
[2:03] So I am extracting the curve from the ABCM group to use later and expanding the border points group so I can collapse that area.
[2:14] And finally in the fuse I am using the second input as target geo so the overall shape doesn't change.


### Peak connected pieces with vex [2:23]
**Transcript (timestamped):**
[2:23] Now I wanted to offset this floating geometry from the bottle body so it doesn't z-fight.
[2:32] And in this case a really small peak does the trick but as you can see in the case I wanted to do a bigger peak I get a distorted shape.
[2:42] So I wanted to find a way to avoid distortion.
[2:47] And that's easy enough just assemble the geo and pick it since we will just have a single point purpose that works but I decided to get a Vex alternative.
[3:00] So one of the ways was to calculate the connectivity, extract the centroid while transferring the normals.
[3:08] And in this Vex snippet running over numbers I am getting the normals from the centroid, getting the point numbers corresponding to each piece and iterating over the array of points to pick the geo along the normal of the centroid.
[3:26] But too much code right?
[3:28] So I found a simpler solution by running over points, reading the normals from the second input.
[3:36] We can use the classes point number since the extract centroid orders the class and then just picking the position with the normal and the multiplier.
[3:48] There is also a way to do it without the centroid but it's just too much code and it's not as performant.


### Outro [3:56]
**Transcript (timestamped):**
[3:56] So yeah these were the tips I will add for you today. Let me know if you found them interesting.
[4:02] And don't forget you can grab all the files from my videos on Patreon along with exclusive tutorials and courses.
[4:10] Take care and see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/direct-and-procedural-modeling-in-houdini/frame_000.jpg
- [0:55] tutorials/frames/direct-and-procedural-modeling-in-houdini/frame_001.jpg
- [1:30] tutorials/frames/direct-and-procedural-modeling-in-houdini/frame_002.jpg
- [2:10] tutorials/frames/direct-and-procedural-modeling-in-houdini/frame_003.jpg
- [3:15] tutorials/frames/direct-and-procedural-modeling-in-houdini/frame_004.jpg
- [4:10] tutorials/frames/direct-and-procedural-modeling-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
A collection of hard-surface modeling tips (learned while modeling a spray bottle) mixing direct/interactive modeling shortcuts with small targeted VEX snippets for cleanup tasks that Houdini's stock SOPs handle poorly: curve cleanup, stray-point removal, border fusing to a target shape, and distortion-free peak/offset of disconnected pieces.

### Summary
Six independent tips from one hard-surface build. (1) Smart direct selection: select a repeating pattern (e.g. every other face on a tube) and expand it forward with Shift+Up Arrow, plus interactive select-by-normal for quick face grouping before extruding. (2) Cleaning a hand-drawn Draw Curve: clip the messy curves to share the same key points, do a large-length resample to capture just the overall curvature, then a fine resample + subdivide to get a smooth clean curve. (3) Removing stray inline points left by a Boolean: Facet's tolerance-based point removal deleted parts of the geometry, so instead a VEX wrangle using `neighbourcount()` groups any point with ≤2 neighbors and blasts them. (4) Fixing bad Boolean topology by fusing border points to a reference shape: extract a curve from the boundary group, expand the border-points group to widen the collapse area, then Fuse with the second input set as target geometry so the fuse operation snaps to the original silhouette instead of shrinking it. (5) Peaking (offsetting) multiple disconnected floating pieces along their own local normal without distortion: naive Peak distorts large offsets, and Assemble+Pick is a valid non-VEX fallback, but the faster/cleaner solution is VEX — either an array-based approach iterating connected-piece point numbers, or a simpler one-liner reading a per-piece centroid normal (ordered consistently by Connectivity) and moving each point along that normal by a multiplier. (6) Final result: a fully modeled spray-bottle asset.

### Key Steps
1. **Pattern selection:** in Edit SOP / viewport selection, pick a repeating face pattern, then press **Shift+Up Arrow** to expand the selection forward following the same pattern (not a uniform grow) — lets you keep extruding/manipulating inner faces without manually reselecting; select-by-normal works interactively in the viewport for quick related-face grouping.
2. **Draw Curve cleanup:** after using **Draw Curve** to hand-sketch a pattern directly on the surface, run **Clip** on all curves to align them to shared key points, then **Resample** with a large segment length to capture only the broad curvature, followed by a second **Resample** at fine length + **Subdivide** to smooth it into a clean usable curve.
3. **Stray-point cleanup after Boolean:** instead of Facet's tolerance-based inline-point removal (which deleted geometry here), use an **Attribute Wrangle** with VEX's `neighbourcount()` function to group points that have 2 or fewer neighbors, then **Blast** that group.
4. **Border fuse to target shape:** after a Boolean leaves bad topology, extract a curve from the ABCM/boundary group for reference, **Group Expand** the border-points group to widen the area to be collapsed, then run **Fuse** with the second input set to "target geometry" so points snap onto the reference shape rather than shrinking the silhouette inward.
5. **Distortion-free peak via VEX (array method):** run **Connectivity** to separate floating pieces, extract each piece's **centroid** (Extract Centroid transfers normals in class order), then in a VEX wrangle run over `numpoints()`, read the centroid normal per piece, gather the point numbers belonging to each piece into an array, and iterate to move each point along its piece's centroid normal — avoids the shape distortion a plain Peak node introduces at larger offsets.
6. **Distortion-free peak via VEX (simpler point-wise method):** run over points instead, read the piece's normal from the second input (Extract Centroid orders classes so `@ptnum` on the centroid input lines up with the piece's class number), then simply move each point's position along `normal * multiplier` — much shorter and more performant than the array-based version, at the cost of relying on the centroid ordering matching the class order (a full non-centroid version exists but is longer and slower).

### Houdini Nodes / VEX / Settings
Nodes: Edit/Select (pattern-based selection, Shift+Up Arrow expand-forward, select-by-normal), PolyExtrude, Draw Curve, Clip, Resample (large-length pass then fine-length pass), Subdivide (curve), Facet (point-removal tolerance — noted as unreliable here), Attribute Wrangle (VEX), Blast, Group Expand, Fuse (second input as target geometry), Boolean, Connectivity, Extract Centroid (normal transfer, class ordering), Peak (naive version, causes distortion at scale), Assemble + Pick (non-VEX fallback for the same peak problem). VEX functions: `neighbourcount()` (grouping low-connectivity points), array-based per-piece point iteration reading `normal` and `@ptnum`/piece point-number arrays, and the simpler per-point `v@P += v@N * multiplier` style approach reading normals from the second input.

### Difficulty
Intermediate/Advanced — the direct-modeling tips are beginner-friendly, but the VEX cleanup snippets (neighbour count grouping, centroid-ordered per-piece normal offsetting) assume comfort with attribute wrangles and array iteration.

### Houdini Version
20.5 (UI matches Houdini 20.5-era hard-surface modeling context).

### Tags
#modeling #vex #procedural #hard-surface #tips #intermediate

---

## Related Tutorials
Cross-link with any other cgside hard-surface-modeling or VEX-tips tutorials (e.g. daily-dose-of-houdini-tips series) once extracted from this batch — shares the "small VEX snippet fixes a SOP limitation" pattern.
