---
title: Direct and Procedural Modeling in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=t1QemBG462g
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/direct-and-procedural-modeling-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Direct and Procedural Modeling in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=t1QemBG462g)
**Author:** cgside
**Duration:** 4m15s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py direct-and-procedural-modeling-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
