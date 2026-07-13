---
title: Procedural Grapes and how to avoid intersections
source: YouTube
url: https://www.youtube.com/watch?v=9bq2Zx5zcIk
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/
frame_count: 0
frame_status: pending-selection
---

# Procedural Grapes and how to avoid intersections

**Source:** [YouTube](https://www.youtube.com/watch?v=9bq2Zx5zcIk)
**Author:** cgside
**Duration:** 3m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-grapes-and-how-to-avoid-intersections <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'm going to show you how to create some simple procedural
[0:06] grapes in Odini. Starting with a line and resembling it by density set to ramp so I can have the
[0:15] initial stems or branches more concentrated towards the top. Adding a pointe heater and that's
[0:24] our base you may want to define the p-scale for the sweep and group it but that's about it.
[0:30] Now for the first set of branches I'm copying a distorted line to the points of our stem.
[0:38] Using a curve to set the start and end and I'm also reducing the p-scale along the curve using
[0:44] a naturoputagest float. Then for the orientation I am using the quaternion output from the
[0:52] oriental along curve and then in a randwell I am multiplying it with a new orientation.
[0:59] Basically what I want to do here is to set each branch 90 degrees apart along the stem
[1:06] and also add some variance in degrees. Big thanks to swalch for suggesting this approach.
[1:15] Okay adding some small branches again using the same wax wrangle as above.
[1:20] Now for the smaller ones we will use another approach using instead this sample direction
[1:28] confnction. You define a max angle and a random vector to value and we will sample the normal
[1:35] direction creating the cone effect you can see in this example. In the random u values I am
[1:42] fitting it between a min and max value so I don't get angles pointing straight up to the normal.
[1:50] Okay we need to create the grapes for that I'm using a rematched sphere and making sure I save
[1:59] the pin point for the valium seam. And just copying it to the end points of the smaller branches.
[2:10] As you can see I have a very small scale so they don't initially intersect and I'm
[2:16] animating the p-scale over the first few frames so I can solve the intersections with valium.
[2:28] For the seam a valium cloud with a very high stiffness and in the solver using the valium
[2:35] rest blend to update at each substep. And when we run the seam we avoid the undesirable
[2:43] intersections. So yeah that's about it. Check out the sin file on my patreon and don't hesitate
[2:52] on asking questions or making a suggestion below. Thank you for watching and see you in the next one.



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
