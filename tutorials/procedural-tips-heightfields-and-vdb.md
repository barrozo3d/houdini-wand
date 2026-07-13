---
title: Procedural tips | Heightfields and VDB
source: YouTube
url: https://www.youtube.com/watch?v=Ue-Wuo87YJI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-tips-heightfields-and-vdb/
frame_count: 0
frame_status: pending-selection
---

# Procedural tips | Heightfields and VDB

**Source:** [YouTube](https://www.youtube.com/watch?v=Ue-Wuo87YJI)
**Author:** cgside
**Duration:** 2m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-tips-heightfields-and-vdb <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back.
[0:03] Let me share with you a few tips when dealing with light fields in Odini.
[0:07] The first one is how you can use the light field pattern to mask out parts of the terrain.
[0:13] I am using a ramp and playing with the height and center and in this case using it to create
[0:20] some elevation with the remap node.
[0:23] Now I want to create some cliff-like sections on the terrain and for that I use the terrorist
[0:29] but I ended up masking it using a light field mask noise so it's not everywhere.
[0:35] As you can see the default look of the terrorist is not so great.
[0:40] This one might be obvious but I honestly didn't know till recently.
[0:45] I wanted a section of a bigger cliff face at the front so I used a ramp to mask out
[0:51] that part and multiply the noise on top.
[0:55] But then I wanted a bigger area and while I could use a mask expanse playing with the
[1:00] bias of the noise will actually work better to grow and shrink the area.
[1:07] So the next one is an optimization tip when you are working with volume vox and want
[1:13] to clip an area of a VDB.
[1:16] Using the VDB clip you can just connect the box and cut the section to speed up the calculation
[1:22] of the volume vox while maintaining the scale of the noises and the same resolution.
[1:28] Let's say you want to preview a noise, you have volume vox as a color attribute.
[1:34] You can first add a CD attribute using a color node.
[1:38] Then in the VDB from polygons you can pass this attribute and give it a VDB name.
[1:44] Next you'll notice a fog-like preview of the attribute so you might want to hide it
[1:49] using a visibility node.
[1:53] So inside the VOP I am mixing two different noises and using another one as the mixed factor
[2:01] and I wanted to preview it so I can simply bind the export as a vector, the resulting noise
[2:08] and finally using an attribute from volume to see the result.
[2:13] So that's what I wanted to share, feel free to grab the scene on my Patreon and I hope
[2:18] you have learned something new today.
[2:20] See you in the next time.



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
