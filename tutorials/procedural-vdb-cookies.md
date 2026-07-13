---
title: Procedural VDB Cookies
source: YouTube
url: https://www.youtube.com/watch?v=WKs4KHfHpyA
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-vdb-cookies/
frame_count: 0
frame_status: pending-selection
---

# Procedural VDB Cookies

**Source:** [YouTube](https://www.youtube.com/watch?v=WKs4KHfHpyA)
**Author:** cgside
**Duration:** 4m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-vdb-cookies <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. In this tutorial we will procedurally model a cookie using VDB
[0:06] anoises. Let's start by dropping a Geocontainer, Diving inside and creating a sphere.
[0:14] Now let's clip it and transform it in the Y-axis to make it flat.
[0:20] Closing the mesh with a polyfill and saving the patch group.
[0:24] Extruding the patch group and saving the front seam for the next step.
[0:31] Now we can bevel the front seam and finally subdivide the mesh to give the VDB a smoother input.
[0:38] Let's drop a VDB from polygons, increase it with the resolution. We will increase it even more
[0:45] for the final mesh. Change the name to density and fill the interior. These are common settings for
[0:53] a VDB setup. We can smooth the VDB quite a bit and let's drop a volume up.
[1:01] Let's start by deforming a bit the overall shape with a NaE noise, adding it to the density
[1:10] and decrease the intensity with a multiply constant. We will also need to increase the exterior
[1:17] band to avoid those holes in the volume. One thing that we can also change is out the bottom is
[1:24] deformed by the noise as usually it's pretty flat. So let's export an attribute using the
[1:31] relative pounding box Y-components so we can visualize it.
[1:38] Drop a color note before the VDB from polygons and in the surface attributes save out the point.cds
[1:46] color. We end up with this fog light preview so let's hide it with visualized notes.
[1:54] Now we need to convert it to polygons and with an attribute from volume we can finally visualize
[2:02] the attribute color. Let's adjust the ramp to mask out the bottom part. And back to the VOP
[2:10] we just need to multiply the noise by the mask and the bottom should be flat now.
[2:21] Now we can add our main noise, a unified static, connect it to the position and create a
[2:27] control for the frequency and amount. We want to use the wordlayF2F1, reduce the intensity,
[2:37] and invert it with the complement checkbox.
[2:44] With a feed range we can clamp out the inputs to create those typical broken parts and finally add
[2:50] some fractal distortion. You can also play with the scale of the noise or even reduce the effect
[2:58] with the feed range and multiply constant. Here I'm just creating switch notes to turn on and off
[3:06] the effect of each noise so we can focus on each noise separately. Let's duplicate the unified
[3:13] noise setup to create the next effect. Here we just need to clamp a bit more the inputs,
[3:19] play with the frequency and remove the fractal. We will instead use a turbulence to distort
[3:27] the noise so we can create some details on the cookie surface. We just need to add the turbulence
[3:36] to the position inputs of the original noise. In the final resolution everything will be more
[3:42] details. Let's keep it low rest for now to have a faster feedback. So in this final noise we want
[3:51] to create some fine details. Let's use again a unified noise and copy the setup notes from before.
[3:58] We'll use a Warly F1, play with the feed range and finally scale the effects to have those fine details.
[4:12] Let's enable all the noises and set a final resolution on the VDB.
[4:18] And as you can see all the details are now much more pronounced, you can always play with the noises
[4:24] and get your own result. From here you can compose the scene and take it to Salaris with some
[4:31] procedural noises and masks generated. You can create some materials for the cookies and render it.
[4:39] So yeah hopefully you learned something new and you can grab the scene file from my Patreon if
[4:45] you want to play with it. Thank you for watching and see you in the next one.



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
