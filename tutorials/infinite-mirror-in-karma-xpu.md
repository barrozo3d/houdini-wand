---
title: Infinite Mirror in Karma XPU
source: YouTube
url: https://www.youtube.com/watch?v=5jfjCGDdbqs
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/infinite-mirror-in-karma-xpu/
frame_count: 0
frame_status: pending-selection
---

# Infinite Mirror in Karma XPU

**Source:** [YouTube](https://www.youtube.com/watch?v=5jfjCGDdbqs)
**Author:** cgside
**Duration:** 4m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py infinite-mirror-in-karma-xpu <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I wanted to show you how I created
[0:04] this infinite mirror effect in Odini. As you can see we have a quite thin
[0:12] surface but inside we have this infinite look. Let's have a look first time
[0:20] creating the text and that's easy enough just with a font then extrude it, place
[0:28] it in the center then I'm grouping the front and back primitives and splitting
[0:36] them here and grouping again the solid parts and then the mirror part. Then just
[0:51] setting a small bevel and soften the models as you can see. Then for the
[1:00] material that's where the magic happens here in the mirror I'm creating a
[1:09] metallic mirror so met on a set to 1 and roughness to 0 and then a glass
[1:18] material transmission set to 1 and roughness to 0 and in world and then I'm
[1:26] mixing those two materials with a rain part set to ray back face. This is the way
[1:34] you can create two sided materials. So in front we will have the glass and on
[1:42] the back of the face we will have the mirror. So for the lead strip it's quite
[1:51] simple I'm just importing the text, keeping just one of the primitives,
[2:03] converting it to curves and then splitting them here by perimeter so I can work
[2:12] on both sides and then extruding the bitin so I can place the lead strip not
[2:22] necessarily adjacent to the text then grouping the the unshared edges, converting
[2:36] them to curves and then applying a color attributes to every 20 points,
[2:47] just attribute a just color and then sweeping it to a ribbon as you can see in
[2:57] here and just something than normal. Then for the rather geometry settings I am
[3:07] treating it as a light source giving it some diffuse intensity and some
[3:21] specular intensity to and just don't like to eliminate the outer material that I
[3:28] haven't showed you but it's just a solid material in this case two materials
[3:34] mixed again with the back face. One is more rough and the other one is less rough.
[3:45] So if you render everything we should get something like this.
[3:57] The infinite look.
[4:03] Then in Cops I am loading the render blurring it a bit and adding it on top so I can
[4:21] create this glow effect and just crop it and that's about it. You can grab the
[4:27] file from my Patreon and thank you everyone for the support and I'll see you
[4:33] next year. Thank you.



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
