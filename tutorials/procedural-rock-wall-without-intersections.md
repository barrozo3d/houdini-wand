---
title: Procedural Rock Wall without intersections
source: YouTube
url: https://www.youtube.com/watch?v=q-9cVBVMv2E
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-rock-wall-without-intersections/
frame_count: 0
frame_status: pending-selection
---

# Procedural Rock Wall without intersections

**Source:** [YouTube](https://www.youtube.com/watch?v=q-9cVBVMv2E)
**Author:** cgside
**Duration:** 3m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-rock-wall-without-intersections <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So last year I created this stone wall for a
[0:05] project and it took me quite a while to do it in Zbrush and then assemble it in
[0:16] Maya. As you can see I even created custom scripts and whatnot so I thought I
[0:24] would give Odinia go to try to create something similar. So here's my attempt
[0:31] creating the stone wall. It's quite a simple setup. The stones are
[0:37] eye-poly at this point but here for the simulation they are very low-poly and
[0:45] let me show you how I did this. So basically I created some rocks. Here you can
[0:55] see one example. I created a few in a loop and I created the eye-poly and the
[1:03] proxy geo for the simulation. Basically with poly-redoos and from there I
[1:13] copy two points, the low poly, I copy two points to agree with a
[1:27] scatter node with a lot of relaxed iterations and this is the result I got. So now
[1:37] having this copy to point southputs we can fill it to an RBD solver and try to
[1:45] avoid intersections and create the final shape. So basically here I'm using a
[1:52] bound node with all settings and then I'm animating the transform, the scale
[2:01] Y from 1 to 0.4 something like this. So this is exactly the shape I want for
[2:13] the wall and I'm animating along a few frames so it has some time to to
[2:21] calculate properly. So now if I enable the solver and play it you can see how
[2:34] it's starting to compress the stones against each other and creating the
[2:40] the final look. This should be the trick as you can see we have no intersections
[2:54] and this should be good enough. So now you can export these and create textures but
[3:03] in this case I am just back injecting the iPoly from above. You're in the
[3:12] split I have the low poly and in this branch I have the iPoly so now I can just
[3:22] back inject the iPoly. Just as a previous visualization of what it might look
[3:35] like at the end. So that's basically it you can grab the file from my Patreon if
[3:42] you want to investigate on your own feel free to leave some suggestions and
[3:47] comments and I will see you in the next one.



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
