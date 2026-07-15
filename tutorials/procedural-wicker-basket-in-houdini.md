---
title: Procedural Wicker Basket in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Qs5Sk6QPGcM
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.598"
tags: [sweep, vex, fuse, weaving, procedural-modeling, orient-along-curve, wicker]
extraction_status: complete
frames_dir: tutorials/frames/procedural-wicker-basket-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Wicker Basket in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Qs5Sk6QPGcM)
**Author:** cgside
**Duration:** 5m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. Let's have a look on how to create this weaker basket
[0:05] procedurally. So I'm starting with a line and resembling it and from there we can
[0:11] use a sweep node set to RoundTube and the Surface type to Rose to create these horizontal
[0:17] sections. I am also creating a profile with the ScaleGram controls. Now I am adding normal
[0:25] pointing inwards with the Polyframe node. My goal here is to create that wave effect along
[0:32] the rows. So in this point, I am switching between the incoming normals and inverted normals
[0:40] for every other point with the module node. You can also use Vax of course. Then we can just use
[0:48] the pick to transform the points along the normals. Converting the geometry to curves and applying
[0:54] some blur to smooth out the shapes. In this case, I am also applying some random b-scaled to the
[1:00] shapes for the next sweep. We just need to promote it to a point attribute. Now transforming every
[1:07] other primitive so they are opposite to each other and finally doing the sweep. For the columns,
[1:15] you can compute the normals and add a nap attribute so that when you duplicate the curves with the
[1:23] sweep node, you will have the correct orientation here using the ribbon preset.
[1:30] And we can now combine everything. Now for this part, start by isolating the last frame,
[1:39] convert it to curve and do a series of sweep nodes. But in this case, we want to add some twist to
[1:48] to create the desired look. As for the handle, we can deform an initial line, creating a ramp profile
[1:55] along the curve view attribute and transforming it on the y-axis. Then sweep it with a few columns
[2:04] and some twists. So now we have four curves. Let's split them into two streams and using again the
[2:11] same vex code to deform based on curve view, we can recreate the original form. Then just add more lines
[2:21] and mesh it. Okay, so far the bottom part is a bit tricky but not complex at all. We start with
[2:30] circle, convert it to curve and extrude it in to create room for the center part.
[2:38] Grouping all the edges, then shrinking the selection with a group expand, convert it to lines and
[2:45] grouping the start points of each curve. And now we want to create the desired shape in the center,
[2:52] in this case we'll use a grid, slightly transformed and use it as a second input in the fuse.
[3:00] By the way, thanks a lot to Asluck from CGWikis Discord for the help on this part.
[3:08] In the fuse node, make sure you set the mode to closest target point and don't actually
[3:14] fuse the point since we want to bridge these shapes. Next we need to create a group for the side
[3:21] shapes. In this case I manipulated the normal so we'll do that, splitting it into two streams
[3:28] and using the sort and add no still bridge to the curves. I am also grouping the center points
[3:35] in the second stream so I can transform them later. Using the polypad nodes to make unique
[3:42] primitives for curve and also smoothing a bit the shapes. As you can see I am also doing a
[3:50] soft transform on that group I saved earlier, then I'm duplicating the curves with a sweep node
[3:57] and finally mesh it. On this side I'm creating the circular pattern with the same extrude but
[4:06] this time with fuse subdivisions, then selecting every other vertex so I can promote it to an edge
[4:14] group ending up with the circular pattern, converting it to lines and making sure the
[4:20] frames are correctly sorted. Using again the same point for a approach to create the wavey
[4:27] or zigzag effect but this time the normals are facing up and down. Picking and then blurring a
[4:35] bit the shape as done before, doing the same transform of set and finally sweeping the shapes
[4:41] with a round tube. And if we merge everything it should align correctly.
[4:47] Alright there you have the finish assets as always you can grab the file from my Patreon
[4:54] and thank you everyone that joined so far. See you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-wicker-basket-in-houdini/frame_000.jpg
- [0:45] tutorials/frames/procedural-wicker-basket-in-houdini/frame_001.jpg
- [1:15] tutorials/frames/procedural-wicker-basket-in-houdini/frame_002.jpg
- [1:50] tutorials/frames/procedural-wicker-basket-in-houdini/frame_003.jpg
- [2:25] tutorials/frames/procedural-wicker-basket-in-houdini/frame_004.jpg
- [3:00] tutorials/frames/procedural-wicker-basket-in-houdini/frame_005.jpg
- [3:40] tutorials/frames/procedural-wicker-basket-in-houdini/frame_006.jpg
- [4:20] tutorials/frames/procedural-wicker-basket-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Model a woven wicker basket entirely from curves and Sweep nodes: horizontal weave rows use a modulo-alternated normal-flip to create an over-under wave pattern, columns reuse the same wave logic with ribbon Sweeps for correct orientation, and the base uses a Fuse "closest target point" bridge between a circle and a transformed grid to create the radial spoke pattern.

### Summary
Horizontal weave rows start as a resampled Line, Swept with Round Tube/Rows surface type, with a Ramp-controlled profile for tapering. Polyframe adds inward-pointing normals; a wrangle switches between the incoming normal and its inverse for every other point using modulo, then Peak moves points along the (possibly inverted) normal to create the wave. Curves are extracted from this, blurred for smoothness, and randomized b-scale is added before the next Sweep; every-other primitive is transformed opposite to its neighbor (a mirrored offset) so the weave alternates correctly between adjacent rows. For vertical columns, normals plus a computed "up" attribute let duplicated Sweep-based curves get correct orientation using the **ribbon** preset. The last row/tier uses the same technique with added twist for visual variety. The handle deforms an initial line with a ramp profile keyed to curve-view, transformed on Y, then swept with a few columns and twist; four resulting curves are split into two streams and run through the same curve-view-based deformation wrangle to recreate the handle's woven form, merged and meshed at the end. The base/bottom is the trickiest part: starting from a circle converted to a curve and extruded inward for a center recess, edges are grouped then shrunk with Group Expand, converted to lines, and the start points of each curve grouped; a transformed grid becomes the second input to a **Fuse** node set to "closest target point" (not actually fusing points, just bridging), creating the radial center pattern (credit: Asluck, CGWiki Discord). Side shapes get their own group (via manipulated normals), split into two streams, sorted, and bridged to the curves with an Add node set by attribute; Polypath makes unique primitives per curve and smooths shapes; a soft Transform is applied to the earlier-saved center-points group before duplicating with Sweep and meshing. The circular-pattern side uses the same Extrude (with fuse subdivisions) then selects every other vertex, promotes to an edge group for the circular pattern, converts to lines, sorts frames, and reuses the same point-VOP wave/zigzag technique (this time normals facing up/down) before Sweeping with a round tube.

### Key Steps
1. **Horizontal weave rows**: Line → Resample → Sweep (Round Tube, Rows surface type) with a Ramp-controlled profile for tapering.
2. Add normals pointing inward via **Polyframe**; in a wrangle, switch between the incoming normal and its inverse for every other point using **modulo** (VEX or a node-based equivalent).
3. **Peak** the points along the (possibly inverted) normal to create the wave/zigzag; convert the resulting geometry to curves and **Attribute Blur** to smooth the shapes.
4. Add randomized **p-scale** (promoted to a point attribute) for the next Sweep pass; transform every other primitive opposite to its neighbor so weave rows alternate correctly.
5. **Columns**: compute normals plus a matching "up" attribute so duplicated curves orient correctly when Swept using the **ribbon** preset.
6. **Combine and add twist** for the last tier/row for visual variety using the same wave technique.
7. **Handle**: deform an initial line with a Ramp profile keyed to **curve-view (curveu)**, transform on Y, then Sweep with a few columns and some twist.
8. Split the resulting 4 curves into two streams; run the same curve-view-based deformation wrangle on each to reconstruct the handle's original form; merge and add more supporting lines, then mesh.
9. **Base/bottom**: start with a Circle converted to a curve, extrude inward to create room for the center recess, group all edges then shrink the selection with **Group Expand**, convert to lines, and group the start points of each curve.
10. Build a transformed **Grid** as the second input into a **Fuse** node set to **"closest target point"** mode (without actually fusing the points) to bridge the grid and circle shapes into the radial center pattern (credit: Asluck, CGWiki Discord).
11. Create a group for the side shapes (via manipulated normals), split into two streams, **Sort** and **Add** (set by attribute) to bridge them into curves; **Polypath** to make unique primitives per curve, and smooth the shapes slightly.
12. Apply a **soft Transform** to the earlier-saved center-points group, then duplicate the curves via **Sweep** and mesh the result.
13. **Circular side pattern**: reuse the same Extrude (with fuse subdivisions), select every other vertex, promote to an edge group for the circular pattern, convert to lines, ensure frames are correctly sorted, and reapply the **same point-VOP wave/zigzag technique** (this time with normals facing up/down instead of side-to-side) before a final round-tube **Sweep**; merge everything to align the completed basket.

### Houdini Nodes / VEX / Settings
Line, Resample, Sweep (Round Tube: Rows surface type, ribbon preset, twist), Ramp (profile shaping, curve-view keyed deformation), Polyframe, Attribute Wrangle (modulo normal-flip for wave pattern), Peak, Convert Line, Attribute Blur, Attribute Randomize (p-scale), Transform (mirrored per-primitive offset), Circle, Extrude, Group + Group Expand, Convert Line, Fuse ("closest target point" bridging technique, credit: Asluck/CGWiki Discord), Sort, Add (by attribute), Polypath, soft Transform, per-vertex edge-group promotion (circular pattern selection).

### Difficulty
Advanced (the alternating-normal wave technique repeated across rows/columns/base, plus the Fuse-based radial bridging trick, assume solid curve/VEX fluency).

### Houdini Version
19.5.598 (visible in viewport title bar).

### Tags
sweep, vex, fuse, weaving, procedural-modeling, orient-along-curve, wicker

---

## Related Tutorials
- [Procedural Problem Solving in Houdini](procedural-problem-solving-in-houdini.md) — reuses the same "basket effect" alternating-weave technique referenced explicitly in that video.
- [Handy Houdini Tips - Vellum, UVs, Modeling and More](handy-houdini-tips-vellum-uvs-modeling-and-more.md) — shares related Sweep/curve-based modeling shortcuts from the same channel.
- [Procedural Boat in Houdini](procedural-boat-in-houdini.md) — shares the Skin-based hull/surface-building approach used here, applied there to a full boat hull.
