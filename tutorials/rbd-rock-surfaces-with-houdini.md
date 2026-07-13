---
title: RBD rock surfaces with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=015fds0mdyk
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/rbd-rock-surfaces-with-houdini/
frame_count: 0
frame_status: pending-selection
---

# RBD rock surfaces with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=015fds0mdyk)
**Author:** cgside
**Duration:** 4m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py rbd-rock-surfaces-with-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. In this video we're going to have a look on how to quickly create some rock like surfaces
[0:07] using the RBD fracture along with some tips.
[0:11] So I start with the box and Boolean out to other one to create an initial shape.
[0:17] Place the mesh in the grid. And in this group expression I am using some simple code to select the
[0:24] slope area without the back face. Using the normal white to select all the primitives below 0.1,
[0:33] next I am removing the bottom faces and finally the back face using the Z component of the normal.
[0:41] Remashing the shape, now expanding the slope group, transforming it in a natubert mask.
[0:50] And using an attribute blur so it's not so harsh when we use it in the next step.
[0:57] In the mountain node I am disabling the Y axis and also blending the mask attribute so it doesn't
[1:04] affect the back of the shape as I want it flat. So to fit the RBD material fracture I am flattening
[1:13] the shape so we can stretch them at the end. I am also feeding my own points to the node using a scatter
[1:21] saw. And after the fracture I am restoring the transform with a match size since I exported the
[1:28] X form from the transform node. As you can see we have the longer shapes that we can remove from
[1:35] the sides and create an interesting rock surface. In the fracture node I just played with the edge
[1:42] detail and noise to add some more variation. Then I am assembling it into packed prims so I can
[1:50] manipulate the pieces as single points. And using some geometry to group the side pieces.
[1:58] As for that bounding Giu I am using the slope group and manipulating the point normals,
[2:04] flattening the Y axis and blurring a bit the normal attribute so I can use it in the
[2:10] X-Rude node otherwise it will extrude all over the place. You can have a look at the file from
[2:17] my Patreon and see in detail what I am doing. And finally I am blasting the selected pieces within
[2:24] the group. Now you can play with the scatter see then find a good looking shape. And packing
[2:31] fusing the points and using a VDB from polygons just to rematch the shape and get rid of the
[2:37] different internal pieces. Creating a slope mask so I can use it inside the volume knob.
[2:45] And in the VOP I have these three simple whirling noises with some distortion, mostly
[2:51] manipulating the frequency of each component to stretch or flatten the noise.
[2:58] I am also multiplying all the noises with the slope masks so we get no distortion on the top part.
[3:04] More of the same would that I have been sharing on the channel and Patreon tutorials.
[3:14] Then calculating the ambient occlusion and curvature so we can use it for texturing.
[3:20] And in this point VOP creating a mask for the top parts using the normal Y and also some sort of
[3:28] wet map for the bottom part using the bounding box. But feeding a noise to the position so we can
[3:37] get some distortion going. And then caching a few variations. As for the texturing using the
[3:48] same workflow as the last video, taking advantage of the generated masks along with some color
[3:54] correction to create some variation along the textures. Again using the material XCGS
[4:01] stripe planner to avoid repetition and better normal mapping and displacement.
[4:07] And that's about it. Hopefully you learned something new. I surely did.
[4:13] And if you want to support the channel and get access to the project files and exclusive
[4:18] tutorials, check out my Patreon. Thank you and see you in the next one.



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
