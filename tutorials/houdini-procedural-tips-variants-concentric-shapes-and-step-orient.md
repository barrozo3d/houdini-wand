---
title: Houdini Procedural Tips | Variants, Concentric Shapes and Step Orient
source: YouTube
url: https://www.youtube.com/watch?v=ItIlLC6mlF4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-procedural-tips-variants-concentric-shapes-and-step-orient/
frame_count: 0
frame_status: pending-selection
---

# Houdini Procedural Tips | Variants, Concentric Shapes and Step Orient

**Source:** [YouTube](https://www.youtube.com/watch?v=ItIlLC6mlF4)
**Author:** cgside
**Duration:** 4m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-procedural-tips-variants-concentric-shapes-and-step-orient <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. In this video I'll share three different procedural setups in Odini.
[0:06] So I saw a video from the Maxon team on how to generate variations by combining different pieces of geometry
[0:14] and after some digging and help from Fanolis on Discord, here's the setup.
[0:21] Starting by generating the Geo, I have three different variations, creating a connectivity attribute, named Class and packing the Geo.
[0:32] Doing the same for the stems and let's call it flowers.
[0:37] Merging everything and then generating a new connectivity this time a name attribute.
[0:44] Then we unpack and iterate over each named primitive.
[0:50] As you can see we have the vases in the first iteration. Now using the attribute from pieces we can randomly select a piece and copy to points.
[1:00] I also randomize the seed attribute based on the iteration.
[1:04] Running the look for the necessary amount we get a random piece being copied to each point and many different variations only limited by the amount of input Geo you have.
[1:17] And of course you need to use the piece attribute on the copy to points node.
[1:23] This next tip is on generating concentric shapes. In this case I want to generate them in multiple pieces otherwise I wouldn't need the look.
[1:34] So iterating over each primitive, grouping the unshared edges and converting it to a curve.
[1:42] Extrusting the centroid and placing the shape in the center since we will copy it to points.
[1:48] Now we generate points, set the amount according to the number of copies you need.
[1:53] Then we will need an ID or index attribute on the points.
[1:58] And we manipulate the p-scale with a naturoputor just float using a remap attribute option, setting a min and max scale and finally remapping the index from 0
[2:10] to the amount of points we have.
[2:13] This part of the setup was shared by Aconoclastis on Discord also.
[2:19] Make sure to join the ThinkPrecetral server.
[2:23] So if we copy the points we have the desired result.
[2:27] Now if we run the look we do get a decent result but some of the shapes have their center bit of.
[2:36] In this shape for instance we have the centroid a bit of center.
[2:40] So what we can do instead is to measure the centroid instead which will give us a better result.
[2:51] Having the new centroid we want to move the shape to the center of the world but we did center based on the centroid.
[3:00] And that's what I'm doing in this wrangle calculating the offset between the centroid and the origin and moving the shape.
[3:13] And that's about it.
[3:17] Now for the last tip on step orientation which can be easily achieved with a scatter and a line using the round two feature.
[3:27] The only downside is that you don't really have a seed attribute for the orientation.
[3:34] So I have a Vax option that generates random rotations and then rounds it to the step we want with a seed and also a angle variation on top of the step orient.
[3:46] So we can add a small offset.
[3:51] So yeah that's what I have for today as always you can grab the file from my Patreon and if you enjoy this check out my procedural courses on the link below.
[4:02] Thank you and see you next time.



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
