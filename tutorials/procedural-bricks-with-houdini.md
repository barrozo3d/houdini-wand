---
title: Procedural Bricks with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=-5cycyb5m-E
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-bricks-with-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural Bricks with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=-5cycyb5m-E)
**Author:** cgside
**Duration:** 4m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-bricks-with-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello and welcome back. In this video I'm going to show you a simple way of creating brick patterns with Odini.
[0:07] We'll also have a look at some simple H scripts to make it as procedural as it can be.
[0:14] So I have this geometry that I want to transform part of it into bricks.
[0:20] Let's start by creating a subnetwork to have a cleaner graph.
[0:24] Kniving inside we need to select the bottom part where we'll have the pattern.
[0:29] Let me just enable the polycount display as we will need it.
[0:34] As you can see we have 22 primes or faces in this object.
[0:39] Let's select 11 of 22 which is the polycount of this geo.
[0:44] Now we can blast the primes selected previously.
[0:49] Creating a grid as it will be the base of our pattern.
[0:56] Using the match size node we can scale the grid to the same size of the original geometry.
[1:08] Let's separate the faces with the face set nodes.
[1:12] And we can visualize it with the explode view to make sure the faces or primes are indeed separated.
[1:20] Now we need to select every odd or even rows.
[1:23] For that let's use a range.
[1:26] In the first field under the amount of columns, subtracting one,
[1:31] and in the second input we multiply the same columns field by two.
[1:36] Basically we are selecting the amount of faces in the horizontal axis and skipping the same amount.
[1:42] Finally we can offset the selected faces and in this case I want it to be exactly in the middle of the faces above and below.
[1:51] So we need to find a way to make it procedural.
[1:55] As soon as I change the values on the grid it's no longer creating the exact pattern.
[2:01] So let's start by querying the bounding box size of the incoming geometry.
[2:06] And we are getting the expected results of setting exactly by the X size.
[2:12] The next variable we need to take into consideration is the number of bricks in off the grid.
[2:18] So let's divide the previous variable by the number of horizontal bricks in this case the grid columns minus one.
[2:26] And multiply it by two with the required brackets just like with simple math.
[2:35] Now we can change the grid pattern and it will always offset off-brick in the horizontal axis.
[2:42] The next step is to clip the pattern as we have some additional geometry on the sides and for that we can use a box clip node.
[2:51] We want to match the size we had before so we can use the bounding box of the match size both for X and Y.
[3:00] And then center the box clip to the same centroid of the previous geometry.
[3:09] Make sure you spell everything correctly in this case I was missing the end quotes.
[3:14] And as you can see we now have the correct clipping.
[3:21] We just have another problem there are bricks missing on the left hand side but that's an easy fix.
[3:28] Let's just use a transform in between to scale the grid in the X axis.
[3:33] If you need also to scale in the Y there's an extra step we need to center the pivot.
[3:40] Just enter the default variable CXCY and CZ in the pivot translates.
[3:48] Now everything should work as expected.
[3:51] We can scale the pattern, change the amount of bricks and we have a completely procedural system.
[4:00] As a final touch we can extrude a bit the polygons and give it a small bevel to sell the effect.
[4:07] And that's it I'm still a beginner in Odini but as I'm learning I will share a few tips along the way.
[4:13] Let me know if you enjoyed this and see you next time.



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
