---
title: Groups Patterns in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=FLWrmz8QPZQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/groups-patterns-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Groups Patterns in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=FLWrmz8QPZQ)
**Author:** cgside
**Duration:** 11m34s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py groups-patterns-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
