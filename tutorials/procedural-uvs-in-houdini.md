---
title: Procedural UV's In Houdini
source: YouTube
url: https://www.youtube.com/watch?v=7ZJeWIFYSxg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-uvs-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural UV's In Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=7ZJeWIFYSxg)
**Author:** cgside
**Duration:** 4m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-uvs-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'll be showing you how you can do some procedural
[0:05] UVs in Odinni.
[0:06] Basically I add this geometry which is a bit iPolly from a VDB operation and I couldn't
[0:14] select any seams or do the UVs in a more traditional way so I have a technique to show you
[0:21] now you can UV a mesh like this.
[0:24] So yeah let's get into it.
[0:27] Okay starting with this initial geometry which is a bit iPolly and a weird
[0:33] uh, tessellation as you can see.
[0:36] So let's look at this what I called sheep UVs.
[0:39] So first I'm remashing it to reduce the polycount and re-projecting it to the original
[0:45] geometry so we keep the silhouette.
[0:48] Then poly reducing because I'm going to select only those art angles, those edges
[0:56] by using the mean edge length and as you can see it's doing a good job.
[1:02] This will end up being our seams.
[1:05] Then converting to a line, re-sampling it quite a bit and re-projecting it to the original
[1:11] cake geometry.
[1:13] Smoothed bit lines, creating a group called seams and now I'm going to add a color in
[1:20] this case red and a black color to the cake then transferring that and since we're going
[1:25] to use the fine shortest pet node we'll use this as a cost attribute.
[1:31] But in this case we need it inverted, that's why I am using this.
[1:37] I am inverting the red color and coming to this part of the network we have to the curves.
[1:46] Now we need to re-sample it quite a bit otherwise we would iterate too many times in the loop.
[1:52] So re-sampling it and converting to line so each segment becomes a single primitive as
[1:57] you can see.
[1:58] I can show you the points.
[2:00] And we will iterate over each line which just have two points.
[2:06] And in the fine shortest pet we can introduce that pet cost that we created and start an
[2:11] end points to 0 and 1.
[2:13] And if we iterate we get the shortest pet of those lines.
[2:21] And then we can group it and group transfer it to the original geometry as you can see.
[2:27] Then it's a matter of UV flatten and passing the seams and we end up with some almost perfect
[2:37] UVs for this kind of geometry.
[2:41] So as you can see some of the UV shells are slightly rotated and of course you can
[2:46] use a UV transfer.
[2:48] But let's level up the procedural approach using this HDEI created.
[2:54] And I will make sure to include these on the patron files.
[2:58] But basically I am creating a connectivity on the UVs.
[3:02] Then adding a mask along the Y using the relative bounding box.
[3:08] Swapping these two UV space and now we can measure the gradients of that mask as you can
[3:14] see we will have the direction.
[3:16] And finally we can calculate the angle by using some bags.
[3:22] And swapping it again to 3D space let's say and UV layouts to have them because in this
[3:32] part they can be overlapping each other.
[3:39] Some UVs to vertices I believe yes and then fusing the points.
[3:46] And that's basically how I've done the UVs for this cake and I've done the same for
[3:50] the slice as you can see.
[3:52] And of course this is basic geometry but I hope this is coming in handy in some of your
[3:59] future projects.
[4:01] So yeah that's basically it.
[4:02] If you want you can grab this part of the scene on Patreon and I hope to see you next
[4:07] time.



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
