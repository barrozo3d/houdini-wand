---
title: Compiling nested loops in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=g6PQu2FRKGo
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/compiling-nested-loops-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Compiling nested loops in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=g6PQu2FRKGo)
**Author:** cgside
**Duration:** 3m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py compiling-nested-loops-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone and welcome back, so in this video I'm gonna show you a few tips on how to compile your loops
[0:06] and to add a bit more complexity to it I will be using nested loops.
[0:13] So I'm working on a Roman bridge procedural model which is full of bricks and I have some sort of
[0:21] brickify setup that I shared before in a video. And in order to have different variations across
[0:27] the pillars I am looping through each individual shape. So trying to make this process faster I
[0:33] wanted to compile it. I did struggle a bit to get it working but thanks to wafer by tom and
[0:41] fanolis on this court I was able to do it. The first rule is that nodes can't read from
[0:47] direct inputs you need to use sparing puts. As you can see in this add node I have size attributes
[0:54] that I need to read below so I created a sparing puts and in the resemble I can use a point
[1:00] expression referencing it. You also can't reference geometry by specifying the name you'll need
[1:07] sparing puts. Another rule is that you can't use local variables and expressions like bebox
[1:15] you need to use wax instead. So instead of reading the bebox size expression I am using a
[1:22] wrangle to start the bounding box size. So now for the nested loops the first thing you should do
[1:29] is to color them differently that way you know which one is which. Inside the nested loops I am
[1:36] accessing the methane port node where I have the iteration attribute. So in order to access it
[1:44] you can duplicate the begin node set it to fetch inputs and connect it to the methanol from the main
[1:51] loop. This way you have node dependencies going through the block boundary only through begin
[1:57] node set to fetch inputs. And then inside the loop I can use a sparing put to reference the
[2:02] begin node and access the methanol iteration attribute. And you need to follow this rule of not
[2:09] having cross lines in the nested loops in this case I have another red nested loop and in order to
[2:16] access the methanol from the main loop I need to pass it through the first blow loop again using
[2:22] begin node set to fetch input. Also make sure you set the end nodes to multi-traded when compiled.
[2:32] I just wanted to show you another example where I would like to scale down the bricks but having
[2:37] the pivot in the center of the object. Since you can't use the centroid expression you can create
[2:44] the wrangle with the get bounding box center function and then I access it with the point expression
[2:50] in the transform node. So yeah that's basically it. Hopefully this was helpful and as always you can
[2:58] grab an example ePfile on my patron. Thank you and see you in the next time.



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
