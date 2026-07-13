---
title: Vellum Typography in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Sr7iwTjwo2E
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vellum-typography-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Vellum Typography in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Sr7iwTjwo2E)
**Author:** cgside
**Duration:** 6m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vellum-typography-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I'm gonna be showing you how you can
[0:06] build this typography effect using Valum. Along the way we will learn how to use
[0:11] some custom masks to feed our Valum simulation. So let's get started! So here's the
[0:20] final result of my setup. Let's start from the beginning. I used first a font to
[0:27] create the text using a custom font but you can find it for free online. Then I
[0:34] use an edit to place the letters to arrange them then creating a match size to
[0:41] place them in the center and adding some thickness. From here I can create a
[0:47] VDB from polygons, smooth it and convert it to polygons as you can see. And now
[0:57] after the thicken I can split the primitives along the Z axis and group the
[1:07] unshared edges, convert to curves, re-sample them and re-project them into the
[1:17] converted VDB, the geometry. Then I create a curvature attribute on the curves and
[1:26] with a value of 1 then one on the geometry with a value of 0 and the one
[1:35] attribute transfer as you can see. So I have these results so I can have those
[1:42] wrinkles around the curvature I guess. And I'm playing with the blend width so I
[1:52] can get this nice transition. Then in here I'm remashing by attributes so
[2:00] using the target mesh size attribute and I'm remashing between those values
[2:06] using the curvature so I get more polygons around the parts that will
[2:17] have those details. As you can see I have more polygons in here, probably can
[2:24] see it from the distance better. And then I'm animating the curvature
[2:31] attributes as you can see from 0 to 1 and I'm animating between frame 12 and 14.
[2:40] So I just want them at the ends. From here I'm creating my bounds or my
[2:51] collision geometry which is just a box from a bound and creating the valum plot.
[3:00] Pretty much default settings and I saved this output group the stretch because
[3:08] I'm going to use it in the valum solver and the valum pressure. This is just a
[3:13] valum configurable one. Then on the valum pressure I am also saving the pressure
[3:19] group and then I have the valum solver. So in the valum solver I am creating a
[3:28] valum constraint property on the pressure group and animating between frame
[3:34] 1 and 15. The rest length scale from a value of 1 to 5.5. So just expanding the
[3:42] letters. Then I have another one on the stretch group where I'm loading in the
[3:50] mask and blending the rest scale with that specific mask. Between the original
[3:57] rest scale or wrestling scale and a multiplied one in this case by 1.8.
[4:05] And if we have a look at the simulation as you can see from frame 13 at frame 12
[4:19] we don't have those details but from frame 13 to 15 we start to get them.
[4:28] And that was the desired look I was after. And I'm just time shifting on frame 15
[4:38] doing a valum post process to smooth out the geometry and give it one level of
[4:47] subdivision. Deleting the attributes and creating a connectivity and just
[4:55] softened the normals. Then in Solaris I'm importing the geometry and creating
[5:04] a material based on the class attribute we created with the connectivity nodes
[5:09] and from that I use a random material X random color and played with the U
[5:19] range and saturation and brightness and also the seeds and created that specific
[5:27] yellowish color or gold color. And I'm also adding the
[5:35] setting the metalness to one and playing with the roughness and the coat
[5:42] attributes or parameters. I have also a dome lights in the scene and the lights on
[5:53] the left side as you can see which is creating some nice reflections and if we
[6:02] render these as you can see we have that metallic look and those wrinkles are
[6:13] quite visible. So yeah this was a quick one just to show you how simple it is to
[6:21] build this typography effect. You can as always grab the file on my
[6:28] Patreon and yeah I hope to see you next time. Thank you.



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
