---
title: Procedural tips and tricks in Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=wgStaCuEglI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-tips-and-tricks-in-houdini-205/
frame_count: 0
frame_status: pending-selection
---

# Procedural tips and tricks in Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=wgStaCuEglI)
**Author:** cgside
**Duration:** 3m22s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-tips-and-tricks-in-houdini-205 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome. In this video I'll share a few procedural techniques in Odini,
[0:05] from Vax to the new cops, I hope you can learn something new with this.


### Circular group selections with vex [0:10]
**Transcript (timestamped):**
[0:10] So as you can see I have these stone holders and the way I'm building them is by using the fine
[0:15] shortest path node. And for that I need groups of points, initially I used the manual selection,
[0:23] but since I might change the stone shape I decided to have a more procedural approach.
[0:29] What I need is to select a few points in a circular pattern.
[0:34] For that I found some sample code online by Animatrix, that creates points in a circular pattern
[0:41] by using the sample circle function. I just said to adapt to group the near points,
[0:47] also adding a distance parameter to the position.
[0:52] And in the main network I just said that another parameter to the Y position so I can have
[0:57] control over this selection. Okay having these curves I need to create the stone holder mesh.


### radial sort and add by attr with modulo [1:00]
**Transcript (timestamped):**
[1:04] I start by resampling to have 20 points, then selecting the first 8 points of each curve,
[1:11] creating an attribute on the points with Modulo and the amount of points on each curve.
[1:16] And as you can see it will create this pattern along the lines that I can use to connect them.
[1:22] If I add them now by attribute and using the group it will get all over the place due to the
[1:28] point sorting. Luckily there's a lab sort that lets you sort points in a circular pattern,
[1:35] which will work right in this example. Again lab sort not the main one.
[1:40] From there I can skin the shape and it will be ready for the next step.
[1:45] Now having both surfaces combined I want to make a VDB out of it so I can blend it with the ring.


### Open geo vdb with topology to sdf [1:46]
**Transcript (timestamped):**
[1:52] But the mesh is open and just creating a VDB won't be enough. We actually need to use the topology
[1:59] SDF which will create this shell VDB. Then smooth it out and blend it with the ring.


### Seamless noises with COPS [2:06]
**Transcript (timestamped):**
[2:07] So having a your VD mesh I want to create some seamless noises for displacement using cops.
[2:13] And the way you can get seamless noises with cops is by using the Racerize setup set to UVs.
[2:20] And now in the Racerize GU output both the position and alpha layers.
[2:26] The next step is to connect that original position to the noise 3D input position.
[2:31] In this case I am also distorting a bit the initial position layer with another noise.
[2:37] If I connect this to the preview material you'll get some visible seams.
[2:44] This is the enough to fix just use the extra plate boundaries with that mask we saved from the alpha.
[2:51] And now you should have a seamless noise pattern.


### Stone cuts in Houdini [2:56]
**Transcript (timestamped):**
[2:56] So I tried a few approaches to create the stone cats.
[3:00] But using just a whirling noise in a mountain and the mesh sharpen actually gave me the best result.


### Outro [3:09]
**Transcript (timestamped):**
[3:10] And yeah I hope this helps you out and make sure to check out my Patreon where I upload all project files
[3:16] from my videos including this one. Thank you.



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
