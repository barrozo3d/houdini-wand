---
title: Procedural Hard Surface Modeling Tips
source: YouTube
url: https://www.youtube.com/watch?v=pTQGJM0k9b0
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-hard-surface-modeling-tips/
frame_count: 0
frame_status: pending-selection
---

# Procedural Hard Surface Modeling Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=pTQGJM0k9b0)
**Author:** cgside
**Duration:** 2m35s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-hard-surface-modeling-tips <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there, let's see how to solve some problems with procedural modeling.
[0:05] This scene file is on Patreon by the way.
[0:08] The first issue I faced in this small project was on how to remove alpha of the left tube
[0:14] in a non-disruptive way.


### Removing Left Tube [0:15]
**Transcript (timestamped):**
[0:16] So the solution is actually pretty simple, first I am computing the UVs of the sweep nodes,
[0:21] then I can get the boundary of the UV attribute.
[0:25] From there, expand the selection and promote it to primitives.
[0:30] Invert the group and then splitting it or blasting well though.


### tapering [0:34]
**Transcript (timestamped):**
[0:35] Now to create this tapering effect, I am using the Curveo attribute previously saved.
[0:41] So in a point 4, I am mixing between the current geometry with 1 with a peak.
[0:48] And as the mixing factor, I am using the Curveo and playing with the values of the feed range
[0:54] to have the desired transition.
[0:56] And since I don't want the effect on the right shape, I am overriding the Curveo in there.


### removing arch transition [1:02]
**Transcript (timestamped):**
[1:03] In this part of the model, I wanted to get rid of the R's transition.
[1:08] So for that, I am extracting the seams group from the Boolean and promoting it to points.
[1:15] Then creating a attribute and blur it.
[1:18] And the only thing left to do is to use that mask in a attribute blur as a white factor.


### rounding [1:24]
**Transcript (timestamped):**
[1:25] To make the top part rounded, I am promoting a previously saved group to primitives and
[1:30] expanding it.
[1:33] Extrusting that part, then create a bound and get only the primitive zero.
[1:38] Bevel the top left corner and now we can extend it and Boolean the initial shape with it.
[1:45] Now let's look at the attribute blend to create this inset extrusion.
[1:50] I have the initial curves with the normals along the tangents and transfer them to the geometry,
[1:57] renaming or swapping the normals by N2 and reversing them in the smaller shape.
[2:03] Calculating the new normals, pointing in by reversing them, and finally blend the two
[2:09] normals with an attribute combined.
[2:12] You can also use a lurb with wax or vops.
[2:15] Then it's just a matter of extruding those inner edges along the pre-existing normals.
[2:21] So that's about it, so hopefully you got something out of this that you can explore in your
[2:26] next projects.
[2:27] Thank you and see you around.



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
