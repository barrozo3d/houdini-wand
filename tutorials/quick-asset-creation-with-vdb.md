---
title: Quick asset creation with VDB
source: YouTube
url: https://www.youtube.com/watch?v=j0s0HkBCaQQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/quick-asset-creation-with-vdb/
frame_count: 0
frame_status: pending-selection
---

# Quick asset creation with VDB

**Source:** [YouTube](https://www.youtube.com/watch?v=j0s0HkBCaQQ)
**Author:** cgside
**Duration:** 4m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py quick-asset-creation-with-vdb <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this video we're going to have a look at a quick way to create rock assets using VDB.
[0:06] I'll be showing you all the settings, but in case you want the file with all the custom textures and model, it will be available on my Patreon.
[0:16] So this is just a quick example that I created, but that I think it has some interesting shapes and details.
[0:25] Okay, I started using a grid with a few subdivisions, extrude it, and then use the mountains op to have a more interesting shape to fit to the VDB setup.
[0:37] Now with the VDB from Bollygons we convert it to VDB, and it's where we can set the resolution and the clipping of the volume or bands.
[0:47] Next we have the volume knob where we're creating the noises that I'll be exploring in a minute, and finally we convert it to polygons that also helps to smooth out the shape, and just remove any small floating parts at the end.
[1:03] Okay, let me just reduce the resolution so we can work a bit faster.
[1:09] So this is my setup in the volume knob, only two noises and other two detect as distortion.
[1:17] The basic idea is to create an add-nose and add the incoming density with the noise and output the result.
[1:25] Not forgetting to connect the incoming position to the position attribute of the noise.
[1:31] Then you can start to play with the noise types and see which one fits better.
[1:36] There is room for epic accidents too.
[1:40] So the next step would be to play with the frequency of the noise, which is like the tiling of a texture.
[1:48] With a simple constant node and a divide by constant you can have a more intuitive control.
[1:54] If you increase the value it will produce a bigger noise and the other way around.
[2:01] Another thing you can do is to add a multiply constant to control the overall effect of the resulting noise.
[2:08] The last step of this setup after you have the main noise is to create a simple noise to distort it.
[2:14] This is a common use setup, using a turbulence or AA noise to distort the unified static.
[2:24] And that's pretty much what I have done here. You can identify your distortion noise and then the main noise with the frequency and multiply controls.
[2:39] The same goes for the second main noise.
[2:43] But this time using a feed range node to control the mean and max values that will help to create different outputs.
[2:51] As for the frequency I am also playing with the original values, mainly stretching the Y axis so it creates this particular look.
[3:02] The X-Renode here is a transform matrix that allows you for instance to rotate the noise. It can be interesting for some effects.
[3:13] As for the main noise I am using Manhattan Cellular F2F1 and using the complement attribute to invert the result.
[3:22] And that is the simple setup for this assets.
[3:29] Then I imported the Geo4in Z-Brush and did some Z-Remashing, Auto-UVs and exported a low poly and a displacement map.
[3:40] Then in Solaris I am bringing the Acetin, adding some subdivisions to the geometry, a material, light, camera and render settings.
[3:50] I am also doing a basic animation to render a turn table.
[3:55] So yeah that was it, another rock cliff tutorial and probably not the last. Hopefully I am not repeating myself.
[4:03] Thank you for watching and check out my Patreon and Gamurov if you'd like to support the channel. See you soon.



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
