---
title: Procedural Modeling tips for beginners
source: YouTube
url: https://www.youtube.com/watch?v=rhRaQa-a8q4
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [beginner, procedural-modeling, groups, extrusion, ramp, copy-to-points, polyframe, group-by-range, vex]
extraction_status: complete
frames_dir: tutorials/frames/procedural-modeling-tips-for-beginners/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Modeling tips for beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=rhRaQa-a8q4)
**Author:** cgside
**Duration:** 4m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. As I continue this procedural modeling project in Odini,
[0:06] I thought I could share a few tips for anyone getting started like me.
[0:11] So for this particular shape I wanted to find a procedural and easy solution. I started with
[0:18] a few circles distributed on a grid. Then I am covering the empty space with a grid,
[0:24] boolean with union and next select all the unshare edges to get the border.
[0:31] Converting the edge group to a curve but now I have these sharp transitions and I need a way to
[0:37] blend the shapes. So the solution is actually pretty simple, just use a smooth node with a high value
[0:44] and we get the desired result. Thanks to Octop user on the Odini subreddit that helped me with this.
[0:52] Ok the next tip is about shaping an extrusion. In this case I wanted to create a profile
[0:58] and that's easy, just scroll down in the extrusion node and look for a thickness.
[1:04] There you can edit a ramp to create the desired profile of the extrusion. You can add points
[1:12] and change its value and position along the extrusion. And of course you can go over the boundaries
[1:19] meaning setting a value over one if you need to. The next tip is about outputting groups
[1:25] procedurally so you can use them later in the graph. Right here I am extruding the circle
[1:32] and as you can see in the output geometry and groups I am enabling the side group.
[1:39] This will create a group of those faces or primitives that I can use in the next step.
[1:45] Now I can load the side group in this extrusion and only affect those polygons.
[1:53] Ok let's see how we can create patterns of geometry with proper orientation.
[2:00] I start with a circle again with eight sides and as I am using this to create the points for
[2:07] the distribution I will also resemble it with the desired amount of points.
[2:14] Then we have the polyframe nodes and we'll get back to it in a second.
[2:19] Using again a resemble just to remove the geometry and output only points.
[2:25] Now selecting and deleting the corners as I only want points on the sides.
[2:31] Using the copy to points to distribute and objects along those points.
[2:37] And as you can see the geometry is correctly oriented along the shape.
[2:41] The trick here is the polyframe nodes. If we set it to normal in the tangent name it will
[2:49] orient the points the correct way. Also I had to use the first edge in the style drop down.
[2:56] And this was the way I did all these repeating patterns for this lamp.
[3:02] Ok within the same setup I am going to show you how to select points with the group by range node.
[3:08] My goal here is to select all the corner points in a procedural way.
[3:13] So let's use a group by range nodes and set the group type to points.
[3:19] Now we can copy the number of segments in the Re-sample node to select the corners.
[3:24] The problem with this is that if we go back and change the amount of points it won't work anymore.
[3:31] So what we can do is to link those parameters.
[3:35] Copy the parameter from the Re-sample node and paste relative reference in the range.
[3:42] And now we can easily change the amount of points and it works procedurally as desired.
[3:48] And those were the tips I wanted to share for anyone getting started with Daudini.
[3:53] Very basic stuff but quite useful.
[3:56] Thank you for watching and see you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/procedural-modeling-tips-for-beginners/frame_000.jpg
- [1:35] tutorials/frames/procedural-modeling-tips-for-beginners/frame_001.jpg
- [2:20] tutorials/frames/procedural-modeling-tips-for-beginners/frame_002.jpg
- [3:25] tutorials/frames/procedural-modeling-tips-for-beginners/frame_003.jpg
- [3:45] tutorials/frames/procedural-modeling-tips-for-beginners/frame_004.jpg

---

## Structured Notes

### Core Technique
A grab-bag of five beginner-level procedural modeling tips: blending overlapping shapes with Smooth, shaping an extrusion profile with a ramp, outputting procedural groups from Extrude for later reuse, orienting copied geometry along a shape with Polyframe, and selecting corner points procedurally with Group by Range linked to Resample.

### Summary
Starting from circles scattered on a grid and covered with a boolean-unioned grid, sharp transitions between the shapes are blended away with a high-value Smooth node. A tapering/profile extrusion is shaped using the built-in ramp under the Extrude node's Thickness parameter (values can exceed 1 to overshoot the boundary). Extrude's "Output Geometry and Groups" option is used to procedurally tag a "side" group of faces so a second downstream Extrude can target only that group. A repeating-pattern lamp design uses Polyframe (set to Normal, tangent named, "first edge" style) to correctly orient copied objects along a resampled/corner-deleted point set via Copy to Points. Finally, corner points of a shape are selected procedurally with Group by Range by copying the Resample node's segment-count parameter with paste-relative-reference, so the corner selection stays correct even if the point count changes later.

### Key Steps
1. **Blending shapes**: distribute circles on a grid, cover empty space with a grid, Boolean union the two, select all un-shared edges to get the border, convert the edge group to a curve, then blend the resulting sharp transitions using a **Smooth node with a high value** (credit: Octop, r/Houdini).
2. **Shaping an extrusion profile**: in the Extrude node, scroll to the Thickness parameter and edit its ramp — add points and change value/position along the extrusion length; values can go above 1 to overshoot the boundary intentionally.
3. **Procedural group output**: while extruding a circle, enable the "side" group under Output Geometry and Groups so the resulting side faces/primitives are grouped automatically; load that group into a second downstream Extrude to affect only those polygons.
4. **Oriented copy-to-points pattern**: build a circle (8 sides) as the distribution source, Resample it to the desired point count, run it through **Polyframe** (this is the key node — bring it in early), then Resample again to strip geometry down to points only, delete the corner points (keep only side points), and Copy to Points to distribute objects with correct orientation along the shape.
5. **Polyframe orientation trick**: set Polyframe to output **Normal** with the tangent name set, and use the **"first edge"** style dropdown option — this is what makes the copied geometry orient correctly along the host shape instead of defaulting to world orientation.
6. **Procedural corner selection**: use Group by Range with Group Type set to Points; instead of hardcoding the segment count, **copy the Re-sample node's segment parameter and paste-relative-reference it** into the range node's field, so changing the point count elsewhere in the graph keeps the corner selection valid automatically.

### Houdini Nodes / VEX / Settings
Circle (grid-scattered), Grid, Boolean (union), Group (unshared edges), Convert Line, Smooth (high value), Extrude (Thickness ramp parameter, Output Geometry and Groups → side group), Resample, Polyframe (Normal output, tangent name, "first edge" style), Delete (corner points), Copy to Points, Group by Range (points, paste-relative-reference to Resample's segment parameter).

### Difficulty
Beginner (explicitly framed as tips for those new to Houdini's procedural workflow).

### Houdini Version
Not specified in transcript or frames.

### Tags
beginner, procedural-modeling, groups, extrusion, ramp, copy-to-points, polyframe, group-by-range, vex

---

## Related Tutorials
- [Procedural Modeling Tips in Houdini #2](procedural-modeling-tips-in-houdini-2.md) — direct follow-up video in the same beginner-tips series, covering extrusion shaping, tiling, and dome displacement.
- [Direct and Procedural Modeling in Houdini](direct-and-procedural-modeling-in-houdini.md) — related beginner-friendly VEX/procedural tips from the same channel.
