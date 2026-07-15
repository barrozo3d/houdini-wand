---
title: Why you need to learn vex in Houdini #1
source: YouTube
url: https://www.youtube.com/watch?v=ntf3zMAez50
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [vex, surface-deform, cluster, minpos, flood-fill, croissant, spiral, vex-showcase]
extraction_status: complete
frames_dir: tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Why you need to learn vex in Houdini #1

**Source:** [YouTube](https://www.youtube.com/watch?v=ntf3zMAez50)
**Author:** cgside
**Duration:** 5m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this quick video I wanted to show you how you can create a
[0:03] cross-a interior like this one you see in here. So I covered before how I created
[0:08] the cross-a just with a bunch of exclusions and a sculpt node and then we move
[0:13] into the interior which is the trickiest part. So I start with the sliced
[0:19] cross-a then blast the field polygons and since this is a simple surface we
[0:24] can actually re-sample it. From there I want to transform a spiral into the
[0:29] cross-a interior shape. So I start by having a rest geometry for the spiral
[0:34] which is this unit circle which takes advantage of the sample circle uniform
[0:38] by manipulating the U value that you feed into the function. You can create a
[0:42] circle from the initial cross-a shape and I make sure that they have the same
[0:47] size, the initial surface as the same size of the circle. So I just scale it to
[0:52] fit with a match size and then we take the spiral, the rest geometry which is
[0:56] the unit circle and the forming geometry and we use the surface deform to
[1:01] deform the spiral to this shape. I scale it a bit with a primitive then re-sample
[1:05] it with subdivision curves to smooth it out. Create an oriental long curve with
[1:10] some normals which is basically the tangent along the shape or the curve.
[1:15] This is just a single curve as you can see. Then it starts the clustering. So I
[1:20] first initialize the cluster to minus one because later I will need this
[1:24] value to be negative. Then in here I create some random clusters just a single
[1:31] point with this wrangle. So each random point in here has a different cluster
[1:35] and they are not uniform or linear. They are at random positions and the way I
[1:40] do that is by rating over numbers, setting the number of clusters I want. In
[1:45] this case 128. Then I create like a U value from 0 to 1 based on the iterations.
[1:50] So just like a curve view it's a value from 0 to 1. Then I assign a random
[1:54] position and the random value is based on each iteration. Make sure it's
[2:00] zero centred so between minus one and one and then I just scale it with an
[2:04] amplitude slider with a multiplier that I set really low. Then I make sure I
[2:09] exclude the first and end point and position which will be a value of 0 or 1
[2:15] and I start at the linear value U and add the random position so they are not
[2:21] linear. Then I read that position on the curve using cream UV and the U value
[2:26] and find a nearest point because we can't map it directly to a point. So I find
[2:31] a nearest point and just assign that cluster to root. So if you can see we have
[2:35] different clusters on random points. It's still a bit linear but we are adding
[2:39] that random offset. I also assign a group as you can see to where those
[2:43] clusters are and that will come in and later. Then in here I need to flood
[2:47] fill the selection so I need to fill the random clusters. So what I do is in a
[2:53] detail I grab all the points on the curve so a selection of all the points in
[2:57] the curve and initialize the variable to grab the current cluster so we can
[3:01] flood fill it. Then I will the points in order. So cluster is also ordered by
[3:06] default because the work we've done before. Grab the current cluster value so
[3:10] let's say 0, 1, 2, 3 and make sure when we when we are iterating over the
[3:16] points that we carry forward the last ID until we find a new one. Since the
[3:20] values in between will be minus 1, these max operation will make sure that we
[3:24] fill those values with the last value grab. Then we just update the point at
[3:29] root cluster and we get the flood fill and why we are doing this? Well it will
[3:33] make sense in a bit. So in here I have also an open-shell version but you can
[3:37] ignore this because it's lower. Then I copy a new curve so now we have two
[3:42] curves on top of each other. We have set it from one another so just by grabbing
[3:46] the just by creating a normal attribute that is pointing out and we grab the
[3:53] current normal which is that tangent U that we add that I call it normal and we
[3:58] cross-product with a vector along the Z axis so pointing to us and that will
[4:03] create an out vector that we can use to offset the curves. So just that we
[4:08] can offset a bit more or less and we get that result. Then we the here the
[4:13] trick we fills the points based on that near point group that we add as you
[4:18] can see but we if we don't we do that by default this won't work we need to
[4:22] match the attribute by the cluster so they don't go on top of each other and
[4:26] we get the beginnings of our effect. Then I just polypate to unite the curves
[4:31] and then in a feedback loop so fetch feedback and by count I just resample just
[4:36] like in a sub-solver but in this case we are using a feedback loop and then I
[4:40] attribute to our just one iteration and we get this sort of result. Fuse, polypate
[4:44] and that's basically it. Of course we can iterate more or less but you can see
[4:50] the iterations going over our geometry we can go a bit more if you need it but
[4:55] the attend iterations in here will work fine. As always you can grab the file on
[4:59] my patreon alongside with the with the cross-site and everything and the
[5:03] final effect. Then for mashing this it's a project for another time. I hope you
[5:08] enjoyed. Thank you. See you next time.



---

## Captured Frames

- [0:20] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_000.jpg
- [1:00] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_001.jpg
- [1:40] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_002.jpg
- [2:10] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_003.jpg
- [2:40] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_004.jpg
- [3:20] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_005.jpg
- [4:00] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_006.jpg
- [4:30] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_007.jpg
- [5:00] tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/frame_008.jpg

---

## Structured Notes

### Core Technique
Build a croissant's laminated/swirled interior cross-section using a **Surface Deform**-driven spiral (a flat unit circle sampled via `sampleCircleUniform()` transformed onto the actual croissant silhouette), then generate an organic honeycomb-like cell pattern along that spiral with a **random flood-fill clustering** algorithm (nearest-point search + `minpos()`) run inside a **Fetch Feedback** loop instead of a Sub-Solver — a first-principles VEX showcase demonstrating how far basic point/curve functions can go without any simulation.

### Summary
Starting from a pre-sliced croissant cross-section (built earlier with a bunch of extrusions and a Sculpt node, covered in a prior video), the interior detail begins by blasting away the filled polygons and resampling the resulting simple boundary curve. The core trick is building a "rest geometry" spiral: a unit circle sampled with **`sampleCircleUniform()`** by manipulating the U parameter creates a perfect flat spiral of the desired size (matched via Match Size to the croissant's own silhouette). **Surface Deform** then takes that flat spiral rest geometry and the croissant's actual cross-section as the deforming target, warping the spiral into the croissant's real silhouette shape — after scaling with a Primitive node and re-sampling with Subdivision Curves to smooth it, an **Orient Along Curve** derives stable tangent-based normals for the single resulting curve. The organic cell/honeycomb pattern is grown next: a `cluster` int attribute is initialized to -1 everywhere (so it can later be tested for "unclaimed"), then random single-point clusters are seeded via a for-loop over numbers (128 clusters by default) — each iteration picks a random U value (0–1, zero-centered/scaled by a small amplitude and offset so seed points aren't perfectly evenly spaced, excluding the very start/end of the curve), samples that position on the rest curve via `primuv()`, then uses **`nearpoint()`** to snap the random position to the actual nearest real point and assigns that point its own unique cluster ID. To grow (flood-fill) these random seed clusters across all remaining points, a **detail-level loop over all points on the curve** initializes a running "current cluster" variable to -1, then — since points are already ordered along the curve — walks through them in order, using **`max()`** to carry the last-seen valid cluster ID forward through any still-`-1` points, filling every gap with whichever cluster was most recently established upstream (a simple, elegant flood-fill via monotonic max-carry rather than any actual pathfinding/BFS). A second curve is then copied directly on top of the first (offset via a normal-cross-product-with-Z "out" vector for a slight radial separation so the two curves aren't perfectly coincident), and points are matched/fused **by their shared cluster attribute** (not spatial proximity) so cells only connect to same-cluster neighbors, producing a honeycomb/vein-like connectivity pattern purely from the flood-filled IDs. Rather than a Sub-Solver (which would need actual DOP context), the entire multi-pass refinement (Polypath to unify, then repeated resample+relax) is wrapped in a **Fetch Feedback** loop — set to iterate "by count" — which repeatedly re-feeds the previous iteration's output back into a light Attribute Blur, over 10 iterations, progressively smoothing/relaxing the pattern into a natural, organic result matching the reference. A final Fuse + Polypath + a bit more cleanup yields the finished honeycomb interior mesh, ready to be meshed (left as "a project for another time" in this video, since the meshing pass wasn't covered here).

### Key Steps
1. Start from a pre-built, sliced croissant cross-section (interior polygons already Blasted away), Resample the remaining simple boundary curve.
2. Build a flat "rest geometry" spiral by sampling a unit circle with **`sampleCircleUniform()`**, manipulating the U parameter to generate the spiral shape; Match Size it to match the croissant silhouette's scale.
3. Run **Surface Deform** using the flat spiral as rest geometry and the croissant's actual cross-section shape as the deforming target — warps the flat spiral into the croissant's real, organic silhouette.
4. Scale with a Primitive node, Resample with Subdivision Curves for smoothness, then run **Orient Along Curve** to derive stable tangent-based normals on the single resulting curve.
5. Initialize a `cluster` int attribute to **-1** everywhere (marks "unclaimed"), then in a for-loop over numbers (e.g. 128 iterations), generate a random U value (zero-centered, scaled/offset so seeds aren't perfectly even, excluding curve start/end), sample that position via `primuv()`, and use **`nearpoint()`** to snap it to the actual nearest real point — assign that point a unique cluster ID (the loop iteration number).
6. **Flood-fill the clusters**: in a detail-level loop over all ordered points along the curve, initialize a running "current cluster" variable to -1, and at each point use **`max()`** to carry forward the last valid (non–1) cluster ID seen — filling every still-unclaimed (-1) point with whichever cluster was most recently established, producing a complete, organically-partitioned pattern with zero pathfinding.
7. Copy a second curve directly onto the first, offset slightly outward via a normal-cross-Z "out" vector for radial separation, then **fuse points by the shared cluster attribute** (not spatial distance) so only same-cluster points connect — producing the honeycomb/vein connectivity.
8. Wrap the multi-pass refinement (Polypath unify → resample → relax) in a **Fetch Feedback** loop (iterate by count, ~10 iterations) instead of a Sub-Solver, repeatedly feeding the previous pass's output through a light Attribute Blur for progressive, organic smoothing.
9. Finish with a Fuse + Polypath cleanup pass to produce the final honeycomb-interior curve network (left un-meshed as a follow-up project).

### Houdini Nodes / VEX / Settings
Blast, Resample, `sampleCircleUniform()` (spiral generation via U manipulation), Match Size, Surface Deform (rest geometry → target-shape warp), Primitive (scale), Subdivision Curves resample, Orient Along Curve, cluster-initialization wrangle (`cluster = -1`), for-each-over-numbers random seed wrangle (`random()`, zero-centered/scaled U, `primuv()`, `nearpoint()`, unique cluster assignment), detail-level flood-fill wrangle (`max()`-based running-cluster carry-forward), normal-cross-Z "out" vector offset, Fuse (match by cluster attribute, not distance), Polypath, Fetch Feedback (iterate by count, Attribute Blur per pass).

### Difficulty
Advanced (the `nearpoint()`+`max()`-carry flood-fill clustering algorithm and the Surface-Deform-driven spiral-to-silhouette warp are both non-obvious, from-scratch VEX techniques built without any simulation or default node shortcuts).

### Houdini Version
Not specified.

### Tags
vex, surface-deform, cluster, minpos, flood-fill, croissant, spiral, vex-showcase

---

## Related Tutorials
- [Spiral Splash Tutorial in Houdini](spiral-splash-tutorial-in-houdini.md) — shares the from-scratch VEX quaternion/curve-parameter spiral-construction approach used here.
- [Procedural tips and tricks in Houdini 20.5](procedural-tips-and-tricks-in-houdini-205.md) — shares the `sample_circle()`-based circular-group and Lab-Sort circular-ordering techniques used here for the spiral rest geometry.
- [Vex Problem Solving in Houdini](vex-problem-solving-in-houdini.md) — shares this channel's from-scratch VEX-first problem-solving philosophy (Cluster-node-style seam detection, custom flood-fill logic).
- [Learning Vex - Recreating attribute reorient sop](learning-vex---recreating-attribute-reorient-sop.md) — shares the same "recreate it from scratch to really understand it" VEX-education philosophy.
