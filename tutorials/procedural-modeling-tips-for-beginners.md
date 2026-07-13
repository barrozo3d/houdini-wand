---
title: Procedural Modeling tips for beginners
source: YouTube
url: https://www.youtube.com/watch?v=rhRaQa-a8q4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-modeling-tips-for-beginners/
frame_count: 0
frame_status: pending-selection
---

# Procedural Modeling tips for beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=rhRaQa-a8q4)
**Author:** cgside
**Duration:** 4m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-modeling-tips-for-beginners <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
