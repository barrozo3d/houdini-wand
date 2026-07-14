---
title: Cleaning fractured geometry in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=n-UAPewvMgQ
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H18+)"
tags: [rbd, procedural, vex, cleanup, modelling, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/cleaning-fractured-geometry-in-houdini/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Cleaning fractured geometry in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=n-UAPewvMgQ)
**Author:** cgside
**Duration:** 4m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back! So in this video I wanted to share with you a
[0:04] simple way to clean geometry that looks like this that you can see here and we
[0:12] end up with something like this which is way more clean. So we have all these
[0:21] inside geometry that we need to clean. So let's go from the beginning I'm
[0:31] creating a few blanks wood planks then I'm iterating and creating a
[0:37] fracture and removing some of the middle parts with the bound. So we end up with
[0:45] something like this after the blast. You can take a look at the file on my
[0:52] patron I will be uploading it there and from here we can unpack and we get
[1:02] this. So we can now blast away in this case the wood grain outside. We can keep
[1:14] the wood grain outside as the base then we can fuse the points and dissolve the
[1:22] flat edges. This will get rid of all those edges that we have quite a fault and as
[1:31] you can see inside there is no geometry which is good and in the other branch we
[1:40] need these end pieces. So we need both parts the one that we will keep and the
[1:50] one that is going to be removed. So we can get only this geometry that we can
[1:57] really get from the groups of the fracture. So let's keep the inside here and
[2:06] do the same in here. Then in a wrangle we are setting these variable
[2:15] founds that will search the near points with a very small radius and if
[2:22] didn't find any near points between the two geometries it will remove the
[2:27] points from the first inputs. So that's why we are using actually two
[2:36] inputs. One is used here the input one and the other one which is the main is
[2:45] where we remove the points. So a very simple wax code that will give us this
[2:55] resulting geometry. Then we have some floating edges and we can just use a
[3:03] clean with the fault settings and then we can merge it over the other parts
[3:13] fuse the points and soften the normals and from this to this. So that's
[3:25] basically what I wanted to share with you guys. Just quickly I wanted to let you
[3:31] know that I just released a course called Church Ruins. It's available on the
[3:37] My Patreon shop and it's a download downloadable file. Contains about nine hours
[3:44] of video contents fully step by step and narrate it. If you guys are interested
[3:51] add over to my Patreon shop and you can find it there. So that's basically it. Let
[3:58] me know in the comments if you have another approach to this kind of issue and
[4:03] if this helped you in any way. Thank you and see you in the next one.



---

## Captured Frames

- [0:04] tutorials/frames/cleaning-fractured-geometry-in-houdini/frame_000.jpg
- [0:45] tutorials/frames/cleaning-fractured-geometry-in-houdini/frame_001.jpg
- [1:22] tutorials/frames/cleaning-fractured-geometry-in-houdini/frame_002.jpg
- [2:55] tutorials/frames/cleaning-fractured-geometry-in-houdini/frame_003.jpg
- [3:13] tutorials/frames/cleaning-fractured-geometry-in-houdini/frame_004.jpg

---

## Structured Notes

### Core Technique
Removes the hidden/interior faces left over from a boolean-style bounding-box fracture cut, using a two-geometry nearpoint VEX wrangle to detect which points on the "kept" piece don't actually border the "removed" piece, then cleans up the resulting jagged mesh.

### Summary
When cutting a shape (e.g. a wood plank) with a bounding-box-driven fracture and discarding a chunk via Blast, the kept piece is left full of messy interior geometry that was only ever meant to face the removed chunk. The fix: unpack the fracture result, isolate the "keep" branch (dissolving flat edges to clean obvious wall-facing faces) and separately isolate the "remove" branch/end-pieces from the fracture's own groups, then run both geometries through a wrangle that checks — for every point on the keep geometry — whether a matching point exists nearby on the remove geometry within a tiny radius; if no match is found, that point (and its geometry) is deleted. This leaves only the true boundary geometry, which is then cleaned of degenerate/floating edges and merged with the rest of the piece.

### Key Steps
1. Start with the source shape (wood planks in the demo), run it through an iterating **Fracture** (bounding-box driven, not a full RBD/Voronoi fracture) and use **Blast** to remove the middle chunk — this leaves the kept plank full of internal, only-partially-relevant geometry from the cut.
2. **Unpack** the fracture result to work with the individual pieces directly.
3. On the piece you want to **keep**: Blast away the outer wood-grain shell (or keep it as the visible base, depending on direction), **Fuse** points, and **Dissolve flat edges** — this removes most of the obviously-unwanted interior faces, leaving a clean outside with (ideally) no leftover geometry inside.
4. Separately, isolate the **removed/end-piece geometry** using the fracture node's own pre-existing groups (both the "kept" and "removed" halves come from the same fracture, so their groups are already available to select from) — you need both geometries side by side for the next step.
5. **The core VEX trick**: in a wrangle with two inputs (input 0 = the main "keep" geometry to clean, input 1 = the "remove" reference geometry), for every point search for a nearby point on the second input within a very small radius (`nearpoint()`-style search); if no matching nearby point is found, **remove that point** from input 0. This isolates exactly the boundary geometry that used to face the removed chunk — a simple two-line VEX approach.
6. The result usually has some **floating/degenerate edges** left over — clean these with a **Clean** node using default settings.
7. **Merge** the cleaned boundary piece back with the rest of the kept geometry, **Fuse** points again, and **soften normals** for a proper final shading result.

### Houdini Nodes / VEX / Settings
Fracture (bounding-box driven) → Blast (remove middle chunk) → Unpack → [keep branch: Blast (outer shell) → Fuse → Dissolve Flat Edges] + [remove branch: isolated via fracture's own groups] → **Attribute Wrangle** (2 inputs; `nearpoint()`-based proximity test between input 0 and input 1, `removepoint()` on no-match) → **Clean** (default settings, removes floating/degenerate edges) → Merge → Fuse → soften normals.

### Difficulty
Intermediate — the concept is simple once explained, but requires understanding how to reference two separate geometry streams in one wrangle (`nearpoint` across inputs) and how fracture groups can be reused to isolate complementary pieces.

### Houdini Version
Not stated explicitly; uses long-standing native nodes (Fracture, Blast, Wrangle, Clean) available in any modern Houdini (H18+).

### Tags
#rbd #procedural #vex #cleanup #modelling #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers this specific fractured-geometry cleanup trick — cross-link with any future RBD/fracture or VEX-cleanup tutorials once extracted from this batch.
