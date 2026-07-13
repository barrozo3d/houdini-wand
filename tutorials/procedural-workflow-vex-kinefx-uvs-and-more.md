---
title: Procedural workflow | Vex, Kinefx, UV's and more
source: YouTube
url: https://www.youtube.com/watch?v=T7CoIJg8Dx4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/
frame_count: 0
frame_status: pending-selection
---

# Procedural workflow | Vex, Kinefx, UV's and more

**Source:** [YouTube](https://www.youtube.com/watch?v=T7CoIJg8Dx4)
**Author:** cgside
**Duration:** 2m47s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-workflow-vex-kinefx-uvs-and-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this video I'll show you a few procedural techniques in Odini.
[0:04] The full scene is available on Patreon by the way.


### Create masks and sort points with uv's [0:07]
**Transcript (timestamped):**
[0:07] The first one is on how useful UVs can be besides the default purpose.
[0:13] So selecting a sim group and flattening the UVs.
[0:16] Then I need the mask around my object for that I can simply use the U component of the UV attribute.
[0:23] So along the X axis.
[0:26] After that I can easily displace my GU along the mask with the Alp of Cine.
[0:32] Another useful feature with UVs is two sword points.
[0:36] In here I am using it to sort along the U component so I can easily select rings around my GU.
[0:43] Without it the point sword is all messed up.
[0:46] And I am sorting again this time by the V component of the UVs or along Y.
[0:53] Otherwise I would get alternating vertex orders when converting the rings to curves,
[0:59] which leads to several issues when working with rings.


### falloff mask for kinefx [1:03]
**Transcript (timestamped):**
[1:03] So as you can see I have this fall of effect on Marie and that is pretty simple to create.
[1:09] Basically using the XYZDist function we create a fall of from the starting primitives.
[1:16] Then just use a ramp to adjust it.
[1:18] I created this icing with a spiral and a sweep node.


### Vellum stick on collision [1:19]
**Transcript (timestamped):**
[1:23] And now I want to integrate it with the cake.
[1:26] See sitting right on top.
[1:28] For that I am setting up a basic valum seam where I let it rest on top of the collision GU.
[1:36] But as you can see it's sticking and not sliding on the collision GU.
[1:41] And in order to where I shift that inside the solver I am creating some valum constraints
[1:47] that evaluate each frame set to attach with a small distance.
[1:51] That way it sits perfectly on top without sliding.


### Slope mask with dot product [1:57]
**Transcript (timestamped):**
[1:57] As you can see I have some sprinkles on top of the icing.
[2:02] And I am placing it only where interior makes sense.
[2:06] By using the dot product between the normals and the effectors set to Y
[2:12] then just scattering on those areas.
[2:14] So you can easily get random rotations by using the attribute adjust vector node.


### Random rotations made easy [2:15]
**Transcript (timestamped):**
[2:20] In this case I am randomizing the app vector.
[2:23] But since the sprinkles have some bend and it is always facing the same direction
[2:29] I also added another one to rotate the normals around the app vector.


### Outro [2:37]
**Transcript (timestamped):**
[2:37] And that was it.
[2:38] Let me know if you learned something new in the comments and make sure to check out the file on Patreon.
[2:43] Thank you.



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
