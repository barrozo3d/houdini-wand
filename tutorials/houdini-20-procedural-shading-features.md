---
title: Houdini 20 Procedural Shading Features
source: YouTube
url: https://www.youtube.com/watch?v=NHD3VbE2y00
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-20-procedural-shading-features/
frame_count: 0
frame_status: pending-selection
---

# Houdini 20 Procedural Shading Features

**Source:** [YouTube](https://www.youtube.com/watch?v=NHD3VbE2y00)
**Author:** cgside
**Duration:** 3m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-20-procedural-shading-features <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there, and welcome back. Let's see how we can use some of the new procedural shading nodes in Odin20.
[0:08] So I have some procedural generated houses, and it would be a challenge to texture them in a traditional way,
[0:15] like in Substance Painter, for example, and on top of that I didn't want to create UVs.
[0:22] But in Odin20 we have some new nodes that can help us in this task.
[0:28] I am starting by loading an attribute created in SOPS, randomizing each wood plank.
[0:34] Then we have these new material X color correct nodes, where we could plug the attribute to alter the gain,
[0:41] you or even saturation of our base texture.
[0:46] In here I am also changing the range, so the effect is more subtle.
[0:51] And as you can see we have some wood texture that is created by the new Karma X-style triplaner,
[0:59] and as I want to keep the orientation of the wood, I am removing any random rotation values,
[1:06] and just changing the size. Then I am referencing the first node to use as a roughness map,
[1:13] in this case changing the data type to raw.
[1:17] For the normal you just need to change the mode to normal, and there is no need for a normal map node,
[1:23] just plug it directly to the shader normal slot.
[1:27] I also have another attribute that gives a random value to reach house, and in case
[1:34] you want to generate a new value, you can use the new material X random node with the very
[1:40] NDC that you put. As you can see I have made some of this darker by changing the gain.
[1:46] There is also a new ramp node that you can use to change the colors of your textures, for instance,
[1:52] in this case I ended up not using it.
[1:57] So another feature that helped me in this scene were the new ROOM map nodes.
[2:03] Basically in SOPS you create the attributes necessary for shading, with the ROOM map
[2:09] frame nodes, just default settings. Then in Solaris you can use the Karma ROOM map along with
[2:15] the necessary attributes created in SOPS, ROOM P, TENGENED U, and TENGENED V, all set to Vector 3.
[2:25] And as you can see in Render we have the desired parallax effect, there are ways to randomize it,
[2:32] but since I had trouble finding cube maps I used the only one.
[2:37] So here's how it looks in context and for the amount of work we put into it it's not that bad.
[2:45] So that was it, a very quick overview of some new Karma features that I wanted to share with you.
[2:51] Don't forget you can grab a file from my Patreon and thank you, see you soon.



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
