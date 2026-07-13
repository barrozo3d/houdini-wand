---
title: Procedural Modeling tips in houdini #2
source: YouTube
url: https://www.youtube.com/watch?v=Kc_6yws1AH8
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-modeling-tips-in-houdini-2/
frame_count: 0
frame_status: pending-selection
---

# Procedural Modeling tips in houdini #2

**Source:** [YouTube](https://www.youtube.com/watch?v=Kc_6yws1AH8)
**Author:** cgside
**Duration:** 4m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-modeling-tips-in-houdini-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. In this video I am going to be sharing a few tips on procedural modeling.
[0:07] So the first one is on how to control the extrusion shape.
[0:11] If for example you need to create a tapering effect like you see in these shapes.
[0:17] I'm starting with this shape with the normal pointing inward.
[0:21] And now with some basic facts I can manipulate the normals with ramp based on the curve view.
[0:29] And on the extrude node you can set the mode to point normal and make sure you use the existing
[0:35] normals. Then you can play with the ramp shape to get the desired result.
[0:42] Now in this example I wanted to create some horizontal tiles divided into vertical sections while
[0:48] maintaining the initial shape of the cylinder. So starting with the tube and creating some UVs with
[0:55] flattened UV nodes. And here I am flattening the cylinder using the UV attribute and mapping it to
[1:04] the position. Now as I said before I need to create horizontal randomly sized tiles.
[1:11] So for now I am going to get rid of the vertical subdivisions and create the horizontal ones.
[1:18] Basically using the fit function and the bounding box by components.
[1:23] If you want you can grab the scene files from my Patreon where you can find dozens of project files
[1:30] from my videos and hours of exclusive tutorials. And for the tiles I am using the lots of
[1:37] division nodes which is the perfect node for this setup. That takes into consideration the initial
[1:44] topology. That's why I just had the horizontal subdivisions. Then I am adding back the vertical
[1:52] subdivisions so I can deform it back to the initial cylindrical shape.
[1:59] As you can see we kept the initial shape adding the desired tiles.
[2:06] Still on the tiles I wanted to break some of them along the ends of the shape.
[2:11] So after the material fracture I am assembling the pieces. Then I need to select the ends so
[2:17] for that I am using a group expression with a following vex snippet. Testing if the
[2:24] exposition of the points is bigger than the bounding box mean plus the size of the bounding box
[2:30] x multiplied by the percentage you want to keep. You can play with the value to select more or less
[2:37] pieces. Now for the last one I created this dome with the loop and
[2:47] some displacement. Started with a tube and did some extrusion inside the loop.
[2:55] Make sure you set the loop to fetch feedback if you are doing modeling operations like this.
[3:02] So in order to create this spherical effect you will need some basic math.
[3:07] In this case the power function will work just fine and playing with the value still you have
[3:12] the desired shape. We will need UVs for the displacement so in order to keep a consistent pattern
[3:19] I am creating seams across each level and flattening the islands into rectangular shapes.
[3:26] So we have the UVs correctly oriented for the dome. Finally in a point warp importing some
[3:33] displacement textures and mixing them with a composite node set to overlay and use the
[3:40] display cell on normal's warp. So that's basically it. I hope you have learned something new
[3:45] and feel free to grab the example files from my Patreon and huge thanks for everyone that
[3:50] already is supporting me over there. So yeah thank you and see you in the next one.



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
