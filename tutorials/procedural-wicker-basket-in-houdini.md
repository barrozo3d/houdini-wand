---
title: Procedural Wicker Basket in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Qs5Sk6QPGcM
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-wicker-basket-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural Wicker Basket in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Qs5Sk6QPGcM)
**Author:** cgside
**Duration:** 5m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-wicker-basket-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
