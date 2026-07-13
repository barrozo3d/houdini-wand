---
title: Quality of life tips in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=iQql20c4Gio
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/quality-of-life-tips-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Quality of life tips in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=iQql20c4Gio)
**Author:** cgside
**Duration:** 6m13s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py quality-of-life-tips-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back, in this video we will have a look at several quality of live tips in Odini.


### Start orientation picking: snap objects [0:06]
**Transcript (timestamped):**
[0:06] So let's say I want to snap an orient and object to the windshield of this took took.
[0:11] Going to set up the main model as reference by Ctrl clicking on the flag and drop a box in the network.
[0:19] Now I can enter the tool state by pressing enter and with a not key I can pick the location target and just let click.
[0:28] Finally I can resize my box and do any further modifications to it.
[0:33] And of course you can pick any location on the model.
[0:37] So the default dot key doesn't work on my keyboard which is Shift semicolon I believe.
[0:43] Just search for start orientation picking in the odd key manager and assign your desired dot key.


### Poly hinge node procedurally in Houdini 20 [0:51]
**Transcript (timestamped):**
[0:51] Okay now let's look at the new bolly engine node and how to set it up procedurally.
[0:56] I just created a circle and dropped the node and to enter the procedural mode you need to change it to position an orientation.
[1:06] I'm picking an angle of 90 degrees and you just need to move it in this case along X.
[1:13] The older way of doing this is by creating a few copies and divide the angle by the number of copies minus 1.
[1:21] Move the pivot and finally skin the shapes.
[1:25] And you can see we have identical results.


### Reorder your class attribute with enumerate [1:29]
**Transcript (timestamped):**
[1:29] Let's fill the shape and extrude the patch group so we can look at some more scenarios.
[1:36] So for that I'm going to create a connectivity node on the Prims and pick the patch in the include group.
[1:44] And we have now a class value for each part.
[1:47] Ready if we check the geometry spreadsheet we ended up with some random values.
[1:54] The easier way to organize them is by using the enumerate nodes with the mode set to enumerate pieces.


### Poly hinge with expressions [2:02]
**Transcript (timestamped):**
[2:02] Now enter the select tool and pick the custom class attribute as a filter.
[2:07] In this case I'm going to select the class with value of 2 and isolate it with the blast.
[2:13] Drop a new inch node and select again the same class.
[2:17] And when we set it to position and your orientation we have these default results.
[2:23] So what we can do is to pick the centroid of the isolated class and immediately we will have the polygon snap to that location.
[2:34] Finally we can adjust the position in Y to move it up.
[2:38] It might be a bit difficult at first to understand but in the end it should make sense.


### Smooth mesh preview in Houdini [2:45]
**Transcript (timestamped):**
[2:45] So with other odd keys the default keyboard combination for smooth mesh preview doesn't work on my keyboard.
[2:52] But as you can see I set up another key and I'm able to switch between the smoothed version and default.
[2:59] You just need to go to the odd key manager and search for subdivision.
[3:04] Then change the keys in my case I pick the keypad plus and minus.
[3:09] And if you press the on the viewport under the geometry tab you can change the level of detail for a smoother version.


### Selection modes tips [3:18]
**Transcript (timestamped):**
[3:19] Now let's look at some selection modes in Odini.
[3:22] You can double click to flood fill to connect the geometry but as I work with a tablet pen that doesn't work all the time.
[3:30] So for those situations you can press H and select to flood fill connected geo.
[3:36] To make our life easier we can select by 3D connectivity and easily select multiple pieces of geo.
[3:43] You can see I'm trying to select the battery but I was also picking geo on the back of the model and to avoid that you can enable select visible geometry only.
[3:55] And since this is a model I did in Maya and was exported with different pieces I also have an Olympic pet attribute which in this case is not very organized.
[4:06] But it's another option to separate organized and possibly apply different materials.
[4:11] And the last selection tip is on how to select between boundaries.
[4:16] I'm going to select this edge loop and another one on the right side.
[4:20] Now I can press shift edge in between and it will flood fill the selection.
[4:26] I can also press only H to select the polygons in between.


### Edit node and transform tools [4:31]
**Transcript (timestamped):**
[4:31] When working with the added node it can be frustrating switching between the select tool and the transform nodes.
[4:38] To avoid that you can uncheck secure selection and it will allow you to select even if you're using the transform tools.


### Camera and viewport tips [4:46]
**Transcript (timestamped):**
[4:47] Okay if you're in the camera tool pressing 1, 2, 3 and 4 will switch between camera views.
[4:53] But let's say you are on the left view and you need the right one.
[4:57] Well just press again the same key and it will alternate between the right and left views.
[5:02] Same for top, bottom and front back.
[5:06] Another common problem is when you accidentally tilt the camera and now you can't really have control over your tumbling.
[5:14] A quick fix is to press H and it will reset to the home view.
[5:19] Really useful odd key.
[5:22] To zoom into a region you can pick the region with control alt and drag.
[5:28] Another way to zoom is to double-left click on the part of the geometry you want to zoom in.


### Custom Matcaps in Houdini [5:35]
**Transcript (timestamped):**
[5:35] And the final tip is on how to use custom matcaps in Odinit to check your shading issues.
[5:41] You can enter the matcap mode and if you press D under the material tab you'll find a matcap texture
[5:48] and pick your downloaded matcaps.
[5:51] I have this from PixelFondue which work great in Odinit.


### Outro [5:54]
**Transcript (timestamped):**
[5:55] And that's about it, let me know in the comments if you learned something new and don't forget you can check out my Patreon page where I share all the project files from my videos.
[6:05] You can also find my procedural courses on Patreon shop, links below.
[6:10] Thank you and I'll see you next time.



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
