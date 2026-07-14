---
title: Groups Patterns in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=FLWrmz8QPZQ
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, procedural, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/groups-patterns-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Groups Patterns in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=FLWrmz8QPZQ)
**Author:** cgside
**Duration:** 11m34s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video we'll have a look at some tips and tricks when using groups.
[0:08] We'll be having a look at some expressions, some Vax examples and so on.


### Group expression normals [0:15]
**Transcript (timestamped):**
[0:15] So let's start simple by using these boxes and examples.
[0:20] And let's say you want to group the top and bottom primitives or the primitives facing the Y axis.
[0:28] And for that we can use group expression and set at n.y.
[0:35] So this actually works in some cases but it fails if you change the dimensions of the box.
[0:45] So let's see a number where it fails right here.
[0:50] And a fix for this is actually to use another expression which is absolute n.y is bigger than 0.5 giving it a threshold.
[1:01] And that way you can get the top and bottom primitives no matter the size of the box as you can see.
[1:11] Another way to achieve this is quite simple is by using the normal group nodes, the most simple one.
[1:20] And you can enable keep by normals as you can see and change it to Y and 0.
[1:28] And if you have by default you only have one primitive but you can check this box include normals matching opposite direction.
[1:39] And then you will have both the both prims.
[1:43] But let's say you want to group the X and Z primitives.
[1:51] So you can use the same expression but this time inverting the signal and that way you can get the inverse effect.
[2:01] Which you can't really get with the group node by default as far as I know.


### Separate groups by connectivity [2:09]
**Transcript (timestamped):**
[2:09] Okay let's look at the second example. In here I have a line and I'm bending it and creating a sweep with a few columns.
[2:18] And let's say you want to group the ends of this shape, something like this.
[2:26] You can use a group range with the following expression.
[2:31] First selecting the columns amounts, in this case is 5.
[2:37] We need to add 1 since we're selecting points.
[2:42] And from there we can subtract from the total amount of points the selection amounts that way ending with the X-Rimities selected.
[2:56] If you want to select just one X-Rimity or one ends, you can use the same expression in the select amount and just use end points in the second input.
[3:10] Another way to do this is again with a group range but dividing selecting the range type to equal partitions.
[3:21] And then in the number of partitions we can input the number of points on the initial line and then we can offset the partition as you can see.
[3:34] We can pass.
[3:38] So that's another way.
[3:40] Moving back to the first example where I'm selecting the ends of the shape, let's say you want to divide these into two groups.
[3:51] So one way you can do that is by using a connectivity node and set the pointing-loop group to the group one, which is this one.
[4:02] And now we can simply in a group node set the add class equals to 0, it will select this group here, this ends and then add class equals to 1, it will select this one.
[4:16] And we can also invert the result by setting add class equals minus 1, which is not included.
[4:26] So now I have a set of curves and I want to select the first point of each one.


### Group range by connectivity [4:27]
**Transcript (timestamped):**
[4:33] One way we can do that if you have access to the construction is the real, let's say, you can group here the first point and then it will propagate to the other curves when you copy the points.
[4:50] But in case you don't have access to it, we can use a group by range and select the start, invert the range and in here check the connectivity in the connectivity top.
[5:05] In this example I wanted to show you how you can select edge loops procedurally with the fault group nodes.
[5:15] By using the group by bounding box, I am starting with the box that is two units in the X and as a few subdivisions on the Y axis.


### Group by edge loop [5:19]
**Transcript (timestamped):**
[5:28] And first of all, if you are using group by bounding regions or bounding box, you want to set the size in this case the size of the box.
[5:41] And as a few subdivisions on the Y axis.
[5:45] And first of all, if you are using group by bounding regions or bounding box, you want to set the size in this case the Z size is equal to 1, so I don't need to change it.
[6:01] Just in case you can use the bounding box in this case and set the Z size, so in case you change it, it will work procedurally.
[6:15] And I have the X size and the Z size and since I just want to select a line of a single loop, I am using a very small scale on the Y.
[6:29] And for the center, this is where the expression comes in handy.
[6:34] We can select, we can start the center from the Y axis, so from the top and subtract the bounding box size divided by the number of subdivisions.
[6:47] And then multiply that unit, let's say, that measurements by the Z loop you want to select, so let's say 12 from 12 to 0, as you can see, or 13.
[7:07] So let's say you have drawn a simple curve and you want to convert it to have smooth transitions and sharp corners where it should be.


### Group by curvature [7:10]
**Transcript (timestamped):**
[7:27] So going from this to this in here, we can start by drawing the curve, making sure it's closed or it has a polygon.
[7:38] And then we can measure the curvature and convert it to a curve by setting the group to all.
[7:49] And if we resample it right now, you will have just set it to subdivision curves and even if you say, even if you set to resample by polygon edge, it will smooth everything as you can see.
[8:06] So one way we can avoid it is again by measuring the curvature, converting to a curve.
[8:14] And grouping, as you can see, I am grouping the corner points.
[8:24] And I am doing that by saying in the group base, add curvature bigger than point 9 in this case, and it's selecting all the art points, let's say.
[8:37] And then we can cut the line at those points and just resample it, as you can see, it will work because the primitives are not no longer connected, they will resample separately.
[8:55] And then since we have a lot of points unnecessary, we can just use a facet node and remove in line points and play with the distance until you're happy with the result.
[9:07] Then we can fuse and make it again a single line, a single primitive, let's say.
[9:16] And if you take a line and you sweep with the cross section, you will have a nice profile.


### Group nearest point with vex [9:26]
**Transcript (timestamped):**
[9:28] So in here I have a planner patch and add nodes, we just single point in the center of the world.
[9:35] And in these back snippets, I am grouping the closest point or the nearest point to the second input position.
[9:46] And you can simply do that by querying the position of the second input, of the point in the second input.
[9:56] And then just use the near points with incoming geometry or the first input in here and using the position from the second input.
[10:10] Then you just set a point group to the pin group, name it pin point or pin group and use the near point selected and use one to set the group.
[10:25] And you need to do this over the detail.
[10:31] And then we can do something similar to this procedurally.
[10:36] So if I take the add node and select, we can do this effect in here.
[10:45] And it always works because it's calculating the nearest point.
[10:52] So in case you didn't get the idea, I'm basically getting the unchared edges or unchared points.
[11:01] And then from that base group, I'm selecting just a few and using the shortest path from the center point to the unchared.


### Outro [11:12]
**Transcript (timestamped):**
[11:14] So that's about it, I hope you have learned at least something new.
[11:19] And if you are interested in this file, you can find it on my Patreon.
[11:26] And thanks to everyone that joined so far and I hope to see you next time.
[11:31] Thank you.



---

## Captured Frames

- [0:20] tutorials/frames/groups-patterns-in-houdini/frame_000.jpg
- [2:15] tutorials/frames/groups-patterns-in-houdini/frame_001.jpg
- [4:35] tutorials/frames/groups-patterns-in-houdini/frame_002.jpg
- [5:30] tutorials/frames/groups-patterns-in-houdini/frame_003.jpg
- [7:30] tutorials/frames/groups-patterns-in-houdini/frame_004.jpg
- [9:30] tutorials/frames/groups-patterns-in-houdini/frame_005.jpg
- [10:50] tutorials/frames/groups-patterns-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
A survey of seven group-selection patterns spanning Group Expression normal thresholds, range/partition/connectivity-based endpoint selection, bounding-box-driven procedural edge-loop selection, curvature-based corner detection for clean curve resampling, and VEX-based nearest-point grouping.

### Summary
(1) **Normal-based grouping:** `N.y` alone in a Group Expression only reliably selects top/bottom box primitives for cube-like proportions; `abs(N.y) > 0.5` (a thresholded absolute-value check) works regardless of box dimensions. The equivalent can be done non-expression-wise with a **Group (Normals)** node ("Keep by Normals" set to Y, 0, with "include normals matching opposite direction" to get both faces) — but the expression approach is the only way to invert the selection (e.g., grab the X/Z-facing primitives instead) since the Group node has no such invert option. (2) **Selecting shape endpoints via Group Range:** on a swept multi-column ribbon, a Group Range with a select-amount expression (`columns + 1` since points are 1-indexed, subtracted from total point count) isolates the end primitives/points; for just one end, swap the second input to `endpoints` for a simpler expression. An alternative uses Group Range's "Equal Partitions" range type, set to the original line's point count, then offsetting the selected partition. (3) **Connectivity-based end-group splitting:** running **Connectivity** with the previously-selected "ends" group as its point-group input yields a `class` attribute; a Group node with `class == 0` selects one end-group, `class == 1` the other, and `class == -1` inverts/excludes both. (4) **First point of each curve, without construction-order access:** if you don't control curve generation order (so you can't just group the first point pre-copy and let it propagate through Copy to Points), use **Group Range** with Start range type, inverted, and the Connectivity toggle enabled to isolate one point per curve. (5) **Procedural edge-loop selection via bounding box:** **Group by Bounding Region** lets you select a specific horizontal loop on a subdivided box by setting the region size to the box's actual X/Z dimensions (read via a Bounding Box expression for procedural robustness) with a very thin Y-axis scale, and computing the Y-center via `(half box height) - (box height / subdivisions) * desired loop index` to target any specific loop by number. (6) **Curvature-based corner-preserving resample:** naively resampling a hand-drawn curve (even with "resample by polygon edge") smooths sharp corners away; instead, **Measure (Curvature)**, group points above a curvature threshold (~0.9) as corners, **Cut** the curve at those points (breaking it into separate un-connected primitives so each resamples independently without smoothing across corners), clean up excess points with **Facet** (remove inline points, tuned by distance), then **Fuse** back into a single primitive — ready for a clean Sweep profile. (7) **Nearest-point grouping via VEX:** in a wrangle running over `detail` (once, not per-point), read the second input's single point position, call `nearpoint()` against the first input using that position, and set a named point group (e.g. "pin_group") to that found point number — a simple, always-correct way to dynamically group "whichever point is closest to X" procedurally; demonstrated combined with unshared/boundary-point selection and Shortest Path from a center point to build a radiating "cracks from center" effect.

### Key Steps
1. **Normal threshold expression:** `abs(N.y) > 0.5` in a Group Expression (Primitives) reliably selects top+bottom box faces regardless of box proportions, unlike a bare `N.y` check; invert the sign/axis to instead grab X/Z-facing primitives — something the equivalent Group (Normals) node cannot do by itself.
2. **Group (Normals) node equivalent:** enable "Keep by Normals," set direction to Y/0, and enable "include normals matching opposite direction" to select both the top and bottom primitive in one non-expression node.
3. **End-primitive selection via Group Range expression:** `total_points - (columns + 1)` as the select-amount (Points mode) isolates the far-end primitives of a swept multi-column shape; using `endpoints` as the second input with the same logic selects just one end simply.
4. **Equal-Partitions alternative:** Group Range with Range Type = "Equal Partitions," Number of Partitions set to the source line's point count, then offsetting which partition is selected — an alternate way to reach the same endpoint-selection result.
5. **Splitting an end-group into two via Connectivity:** run **Connectivity** using the previously-built "ends" group as its point-group input to generate a `class` attribute; Group nodes with `class==0`, `class==1`, or `class==-1` (inverted) isolate each side independently.
6. **First-point-per-curve without construction order:** **Group Range** (Start type, inverted, Connectivity toggle enabled) selects exactly the first point of each disconnected curve primitive when you can't rely on generation order to propagate a pre-copy group.
7. **Procedural bounding-box edge-loop selection:** **Group by Bounding Region**, sizing the region to the box's true X/Z dimensions (via a Bounding Box expression, e.g. `bbox("op:...", D_XSIZE)`, for procedural robustness across resizes) with a thin Y-axis scale; center the region on Y using `(half_height) - (box_height / num_subdivisions) * loop_index` to procedurally target any specific horizontal loop by index.
8. **Curvature-based corner grouping:** **Measure** (Curvature) on a closed/polygon curve, Group points where curvature exceeds a threshold (~0.9) to mark corners.
9. **Cut + independent resample:** **Cut** the curve at the corner-point group (breaking it into separate, unconnected primitives), then Resample — because each segment is now its own primitive, resampling no longer smooths across the sharp corners the way a single connected curve would.
10. **Cleanup:** **Facet** (remove inline points, tuning the distance/tolerance) to eliminate excess points introduced by the segment-wise resample, then **Fuse** to rejoin everything into a single primitive, ready for a clean Sweep cross-section profile.
11. **VEX nearest-point grouping:** in an Attribute Wrangle set to run over `detail` (once, not per point), read the second input's point-0 position, call **`nearpoint()`** against the first input's geometry with that position to find the closest point number, then set a named point group (e.g. `i@group_pin_point = 1` on that found point) — guarantees a correct nearest-point group regardless of geometry changes, since it's computed dynamically rather than hardcoded.
12. **Combined radiating-crack effect:** group unshared/boundary points, select a subset, and use **Shortest Path** from the VEX-found nearest/center point to each selected boundary point to procedurally generate radiating crack-like curves.

### Houdini Nodes / VEX / Settings
Nodes: Group (Expression: `abs(N.y) > 0.5`-style normal thresholding; Normals mode: Keep by Normals + include-opposite-direction), Group Range (Points/Primitives, select-amount expressions using point counts, Equal Partitions range type, Start range type + Connectivity toggle), Connectivity (`class` attribute generation from a seed point group), Group by Bounding Region (Bounding Box size expressions for procedural robustness, thin-axis scale, computed center offset), Measure (Curvature), Cut, Resample (note: "subdivision curves" and "by polygon edge" both smooth corners on a single connected primitive), Facet (remove inline points), Fuse, Sweep, Attribute Wrangle (VEX: `nearpoint()` for detail-scope nearest-point grouping, group-attribute assignment), Shortest Path.

### Difficulty
Intermediate — approachable group/expression patterns; the curvature-cut-resample and detail-scope VEX nearest-point techniques are the most non-obvious and broadly reusable tricks.

### Houdini Version
20.5 (UI matches Houdini 20.5-era group/expression toolset).

### Tags
#vex #procedural #tips #intermediate

---

## Related Tutorials
Cross-link with direct-and-procedural-modeling-in-houdini.md and direct-vs-procedural-in-houdini.md (same author, overlapping group-selection/VEX-cleanup philosophy) once both are indexed together.
