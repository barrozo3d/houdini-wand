---
title: Edge Bundling / Bundling Curves – Houdini Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=Mypavnx92tw
author: Konstantin Magnus
ingested: 2026-08-08
houdini_version: "20.5.684"
tags: [edge-bundling, curve-bundling, attribute-blur, proximity, laplacian, volume-preserving, for-loop, solver, group-expression, point-valence, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Edge Bundling / Bundling Curves – Houdini Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=Mypavnx92tw)
**Author:** Konstantin Magnus
**Duration:** 6m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] My name is Konstantin Magnus. In this Houdini tutorial, we are going to bundle curves into networks, either that kind of bubble shape, or when we want to pin down the endpoints, we get this kind of network.
[0:14] Let's start from scratch. With a new document, we are going to set up a grid. The grid can be oriented to the XY plane. I'll choose a size of 1 by 1 for now, and switch the connectivity to rows.
[0:34] If you enable the points, you can tell that we are able to increase the number of rows while we keep the divisions to none, so just choose two columns for two endpoints.
[0:52] I would like to collapse the entire grid to zero, so I have more control when I randomly place the endpoints using a jitter node.
[1:06] Let's disable the x-axis. We have a set of two-dimensional curves, potentially intersecting each other.
[1:18] Now I would like to increase the resolution using a resample node set to 0.01, so that way we have plenty of points to bundle.
[1:30] We are going to use two standard nodes to shape these curves using the attribute blur node set to proximity.
[1:42] This will enable us to bundle these curves as soon as we disable the pinning of the boundary points. I can increase the maximum neighbors to all points for now. This is of course not ideal, but it's a start.
[2:03] I'll use a rather low radius, let's say 0.06. There are two modes we can use. I would recommend to start with volume preserving to get those bubbles.
[2:17] As you can tell the curves look a bit damaged, so I would like to compensate the shape with a smooth node, which we can set to a low quality and a strength of just five.
[2:37] This is roughly the effect I'm after. In order to really be able to change the look, I would like to cut out these nodes and put them inside a for loop.
[2:57] This looks promising. Let's see whether it still looks good after 40 iterations. This is where you can dial in the effect. The resolution of the curves set to 0.01, the blur set to 40 by 0.06 and the smoothness which currently stands on a strength of five.
[3:20] This is one look we are after and we can also play with pinning down the endpoints. In a separate geometry stream, I would like to use the group expression node to select the endpoints after the resampling because the resolution has changed.
[3:45] We should choose the point group and the preset called point valence set to one. I call that group pin and these endpoints I would like to not change.
[4:06] Let's choose the group pin with an exclamation mark in front to spare these points. For this effect, I want to switch to the Laplacian mode, which looks more like a road network in this case.
[4:22] Inside the smooth node, I also want to constrain the pinpoints. After a few iterations, I get this kind of result which is too extreme for my liking. Let's try to find out how to dial this in.
[4:37] It gets a lot better by not blurring the positions as much and we could also play with the smoothing depending whether you would like to have a rather rounded curvy look or a rather strict look. You can play with the settings here as well.
[4:58] Once you're happy with the results, you can also copy out these nodes inside a solver. That way we can create an animation.
[5:09] I'll choose the real-time toggle and inside the solver, I just integrate these three nodes in my case. When we jump back, we can now hit play and see our curves in effect.
[5:30] For more clarity, you may want to use a color node set to primitive random. That way it's easier to see what's going on.
[5:41] The same would work for the slightly longer way, which creates these networks. Let me quickly demonstrate this inside another solver.
[6:11] Alright, thank you for watching.



---

## Captured Frames

- [0:34] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_000.jpg
- [1:06] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_001.jpg
- [1:18] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_002.jpg
- [1:42] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_003.jpg
- [2:03] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_004.jpg
- [2:17] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_005.jpg
- [2:57] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_006.jpg
- [3:20] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_007.jpg
- [4:06] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_008.jpg
- [4:37] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_009.jpg
- [5:09] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_010.jpg
- [5:30] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_011.jpg
- [5:41] tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/frame_012.jpg

---

## Structured Notes

### Core Technique
Procedural **edge bundling**: starting from a set of straight point-to-point curves with random endpoints, iteratively pull nearby curve segments toward each other using an **Attribute Blur** (proximity mode) + **Smooth** node pair run inside a **For Loop** (or a **Solver** for an animated version), producing either organic "bubble"-shaped bundled networks or, with endpoints pinned, road-network-like converging bundles.

### Summary
**Base setup:** a `grid` (1×1, XY plane, connectivity set to Rows, 2 columns/0 row-divisions) gives exactly two points per row — the endpoints of a set of straight lines. The whole grid is collapsed to zero (all points at the origin) so a `pointjitter` node has full control randomly scattering each endpoint independently, producing a set of straight 2D curves (X-axis disabled/flattened) with potentially intersecting/crossing paths. A `resample` node (set to a small length like 0.01) subdivides each curve into many points — bundling needs enough point density along each curve to actually deform smoothly, not just move the two endpoints.

**Core bundling pair:** an **Attrib Blur** node set to **Proximity** influence (not topological adjacency) with **Pin Border Points disabled** looks at each point's spatially-nearby neighbors (within a **Proximity Radius**, e.g. 0.06) *across all curves*, not just along its own curve, and blurs/averages positions toward them — this is what actually pulls separate curves together where they pass near each other. Two blur **Mode** options: **Volume Preserving** (produces rounded "bubble"/blob-like bundled shapes) and **Laplacian** (produces a more angular, road-network-like converging look — used later for the pinned-endpoint variant). Because the raw blur result looks somewhat "damaged"/jagged, a **Smooth** node (low quality setting, strength ~5) is chained after it to clean the shape back up.

**Iterating the effect:** cutting the Attrib Blur + Smooth pair out and placing them inside a **For Loop** (Feedback mode) lets the same operation repeat many times (demoed at 40 iterations) — the effect compounds each pass, and the loop is where you actually dial in the final look by tuning resample length, blur radius, iteration count, and smooth strength together as a system rather than any single parameter in isolation.

**Pinning endpoints (for the road-network variant):** in a separate parallel geometry stream, a **Group Expression** node selects points using the preset **Point Valence = 1** (i.e., points with only one connected edge — the curve endpoints, re-selected *after* resampling since resampling changes which points exist) into a group (e.g. named "pin"). That group, referenced with a **leading exclamation mark** (negated — "everyone except these points") inside the Attrib Blur's point-group field, excludes the endpoints from being moved/blurred, so they stay fixed in place while everything else bundles toward the interior — combined with **Laplacian mode**, this produces the road-network look. The Smooth node is likewise constrained to respect the same pinned group. Over-blurring the *positions* (not just over-smoothing) was found to push this look "too extreme" — backing off how strongly positions get blurred (vs. leaning more on the smooth pass) gives more control over rounded-vs-strict curve character.

**Animating it:** once a static look is dialed in, copying the same node chain (blur + smooth, or blur + smooth + resample as needed) inside a **Solver** node turns it into a frame-by-frame animation — with the viewport's real-time toggle on, playback shows the curves bundling into their final shape over time rather than as a single static pass. A `color` node set to **primitive random** coloring is recommended purely to make individual curves/strands visually distinguishable while iterating on the effect. The same overall approach (with the pinned-endpoint/Laplacian variant) works inside its own separate Solver to animate the road-network look as well.

### Key Steps
1. Build a grid with Rows connectivity and exactly 2 points per row (endpoints of straight lines); collapse it to zero.
2. Randomize endpoint positions with a `pointjitter` node (flatten to 2D by disabling the unused axis).
3. `resample` each curve to a small step size for enough point density to bundle smoothly.
4. Chain **Attrib Blur** (Proximity influence, Pin Border Points off, tuned radius) → **Smooth** (low quality, moderate strength) to pull nearby curve points together and clean up the result.
5. Choose blur **Mode**: Volume Preserving for rounded "bubble" bundles, or Laplacian for a more angular road-network look.
6. Move the blur+smooth pair inside a **For Loop** (Feedback) and iterate (e.g. ~40 times) to compound the bundling effect; tune resample length / blur radius / iteration count / smooth strength together as one system.
7. For pinned endpoints: build a `Group Expression` selecting Point Valence = 1 points (post-resample) into a named group; reference that group with a leading `!` in the Attrib Blur's (and Smooth's) point-group field to exclude endpoints from movement.
8. If a pinned/Laplacian result looks too extreme, reduce how strongly positions get blurred rather than only adjusting smooth strength, to control rounded vs. strict curve character.
9. To animate: copy the finished blur/smooth node chain inside a **Solver** node; enable the real-time viewport toggle and play back to see the bundling happen over time.
10. Add a `color` node (primitive random) for visual clarity while iterating on either variant.

### Houdini Nodes / VEX / Settings
`grid` (Rows connectivity, 2 points per row, collapsed to origin), `pointjitter` (random endpoint scatter), `resample` (small step size, e.g. 0.01, for point density), **Attrib Blur** (Influence Type: Proximity, Proximity Radius, Max Neighbors, Pin Border Points off, Mode: Volume Preserving vs. Laplacian, Blurring Iterations, Step Size), `smooth` (Quality, Strength), **For Loop** (Feedback mode, wrapping the blur+smooth pair for repeated iteration), `group expression` (Point Valence = 1 preset, post-resample, for endpoint selection), negated group reference (`!groupname`) to exclude points from an operation, `solver` (wrapping the same node chain for frame-by-frame animation), `color` node (primitive random, for visual clarity).

### Difficulty
Intermediate — no VEX required, but the technique depends on understanding how proximity-based blurring, loop/feedback iteration, and group-based point exclusion interact as a system; tuning the several interlocking parameters (radius, iterations, smooth strength) to get a specific look takes some trial and error.

### Houdini Version
Screenshots show Houdini Core 20.5.684.

### Tags
edge-bundling, curve-bundling, attribute-blur, proximity, laplacian, volume-preserving, for-loop, solver, group-expression, point-valence, procedural-modeling, konstantin-magnus

---

## Related Tutorials
None yet in this library on procedural edge/curve bundling — first entry covering this technique.
