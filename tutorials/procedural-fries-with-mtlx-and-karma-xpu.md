---
title: Procedural Fries with Mtlx and Karma XPU
source: YouTube
url: https://www.youtube.com/watch?v=lcgNaIicsZU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/
frame_count: 0
frame_status: pending-selection
---

# Procedural Fries with Mtlx and Karma XPU

**Source:** [YouTube](https://www.youtube.com/watch?v=lcgNaIicsZU)
**Author:** cgside
**Duration:** 3m36s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-fries-with-mtlx-and-karma-xpu <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there, today I wanted to share a few tips on procedural texturing, you know, Dini,
[0:05] showing up this simple project.
[0:08] So the first challenge I had was on how to project vehicles or logos similar to my


### Projecting Decals [0:11]
**Transcript (timestamped):**
[0:13] as planar projection feature.
[0:16] So in subs I created a very simple HDA that uses UV planar projection, which allows me
[0:23] to control the position of the decal, and it also creates a proximity based mask, so
[0:29] the texture doesn't show up in the back of the model.
[0:33] As you can see it's just a point in the same position of the planar projection, and transferring
[0:39] an attribute to the geometry.
[0:42] I'll share this HDA on Patreon along with the full scene, that way you can also see how
[0:48] I've modeled the cup and simulated the fries.
[0:52] So in Solaris I am first controlling the scale with the place to denote, loading the texture,
[0:59] making sure I set the address mode to Constance, so the texture doesn't tile.
[1:04] Then multiplying the alpha with the mask from sobs, again so it doesn't repeat on the
[1:09] back as you can see here, since I've just done a planar projection.
[1:19] And then using the mask as a mixing factor to combine the texture and the red in background.
[1:26] I also have a final detail on the cup, where I'm placing this line along the top, which
[1:31] I've accomplished with a primitive attribute to get the desired sharpness.


### Primitive Attributes [1:36]
**Transcript (timestamped):**
[1:36] So this is the attribute as you can see, I had no idea on how to do this in a procedural
[1:42] texture-based way, so I've just modeled the detail into the final geometry.
[1:48] Since I had some edge groups on the modeling, I extracted the side ones and created the
[1:53] normal along the curves.
[1:56] Then transfer them to the top edge curve, this way I can pick it along the shape.
[2:01] From there I am resampling to make it smoother, duplicating the curve with a sweep, and the
[2:07] ugly parts, a Boolean set to Shutter mode, and finally created the attribute with the
[2:12] resulting group.
[2:14] Again, not the most elegant way, but sourdlobs here are your ideas on the comments below.
[2:20] Now let's quickly have a look at the price shader.


### Fries Shader [2:24]
**Transcript (timestamped):**
[2:24] First in the albedo I have a mix of colors and noises to create some variation.
[2:29] In the first part I mix between orange and yellow, controlled by a whirling noise, then
[2:34] using another noise to mix the main yellow shades and other mix of colors.
[2:40] For the displacement using the unified noise, but distorting it a bit with a fractal by
[2:46] adding it to the position just like in Vops.
[2:50] I duplicated the noise and changed the frequency and type, and added them together while remapping
[2:55] it to fit the displacement range I needed.
[2:59] I am also adding some bump to it, a distorted noise.
[3:05] So the final shader, I am using the yellow color mix for both albedo and subsurface, which
[3:12] is said to a small scale, this will always depend on the size of your scene of course.
[3:17] So yeah that's basically it, nothing too impressive, but I thought that this might be useful
[3:22] to you, let me know.
[3:24] Don't forget you can grab the full scene on Patreon, and thank you for watching, see
[3:29] you in the next one.



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
