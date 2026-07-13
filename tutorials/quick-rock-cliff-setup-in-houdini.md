---
title: Quick Rock Cliff Setup in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=iSIXaa3rknU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/quick-rock-cliff-setup-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Quick Rock Cliff Setup in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=iSIXaa3rknU)
**Author:** cgside
**Duration:** 7m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py quick-rock-cliff-setup-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. So today I wanted to share with you how I created this rock
[0:06] like surface or cliff. So basically I am starting with a curve. This is a setup that I
[0:18] saw online on 80 level I believe. So I am starting by drawing a curve. Then I'm extruding
[0:27] it up and I'm also outputting the textured back seam and grouping also the middle seam since
[0:40] I am adding a subdivision. Then I'm extruding the volume to create this shape and piercing
[0:55] the points. This is one side of the branch. Then I am copying two points a few boxes, nothing
[1:03] special with the box. Just a box scaled in Y. We're matching it a bit, blurring the normals and using a
[1:16] mount and saw. Then I am just using a Sphereify P. I believe preset to just smooth out the initial shape.
[1:30] And I'm doing these in a loop. So for the point let me just show you the points. I am extracting
[1:40] those two edge loops and re-sampling it, removing the curves and just give two points, adding a
[1:52] point heater and some randomization of P scale and the orientation. This script I shared before in
[2:00] the channel. And I am copying two points in a loop, something like this, because I want to change a bit
[2:11] the amplitude with a fit function and the offset of the noise. In the end doesn't really make that
[2:20] difference but just in case. So after copying the shapes I am boolean, I am doing a boolean
[2:35] and I get something like this. Then I'm deleting the small parts,
[2:40] fusing and remashing. So we get these regular shapes. Then I am using VDB from polygons and
[2:53] converges to smooth out the shape as you can see. Then I am doing a remash
[3:07] and clipping the back and the bottom, because we don't need those extra polygons.
[3:15] The leading again the small parts, there are some extra pieces. And I'm applying a subdivision before I
[3:25] use the triplanar displays notes. But in this case I am not using it to this place. I am using it for
[3:37] color. As you can see I am just using the color here. And I'm doing that for two different textures
[3:46] that will be used for displacement later in the point of op. And two colors just to visualize the
[3:55] some texture. One grass texture for the top and one rock surface for the front side.
[4:09] I am also blurring the normals just in case the displacement goes a bit wild.
[4:16] Now in the point op, if I enable the subdivision, it takes a little bit because I am subdividing it
[4:31] three times. So as you can see we get the color and the displacement. Let me show you what's
[4:44] going on in the point op. As I told you before I am I have two textures for displacement and two
[4:53] for color. We will ignore the the last ones for the color because it's just a previous visualization
[5:03] here. We won't actually use this for final render. So for the displacement I'm importing the first
[5:12] one which is just directly to the CD. And I'm importing the second one just in part point
[5:20] attribute and the CD. And I'm compositing it. I'm mixing the two textures with a composite mode.
[5:28] In this case I set it to darken. You can try overlay. You can try lighten depending on the input
[5:36] textures. These are just mega-scan textures and that's why I'm also remapping them
[5:45] between minus point five and point five. Then I'm just displacing. You can play with the amount.
[5:55] And I don't want displacement on top. So what I'm doing I'm taking the initial position.
[6:03] And mixing it with the position from the displacement. So I have the the y component is the original
[6:13] position. It's from the original position and the x and z is from the displacement. So I can
[6:22] assign it to the new position. As for the color it's not really important but you can have a look
[6:32] at the file in my Patreon if you are interested. So yeah that's basically it.
[6:40] Then you can reduce it because this is a bit typoly. You can reduce it and delete any x
[6:48] reparts. So yeah that's basically it. If you want you can have a look at my at the file on my
[6:55] Patreon I will be uploading there. And yeah thank you for watching. See you in the next one.



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
