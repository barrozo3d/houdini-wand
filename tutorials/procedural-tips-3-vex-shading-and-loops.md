---
title: Procedural Tips #3 VEX Shading and Loops
source: YouTube
url: https://www.youtube.com/watch?v=bgUI52CFMLU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-tips-3-vex-shading-and-loops/
frame_count: 0
frame_status: pending-selection
---

# Procedural Tips #3 VEX Shading and Loops

**Source:** [YouTube](https://www.youtube.com/watch?v=bgUI52CFMLU)
**Author:** cgside
**Duration:** 6m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-tips-3-vex-shading-and-loops <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. In this video I wanted to share a few procedural tips from
[0:06] shading to wax, hopefully you learned something new and you can always grab the project files
[0:13] from my Patreon. So I'm creating some simple procedural buildings and houses and the roof
[0:21] was the trickiest part. As you can see I'm aligning some grids to the roof shape so I can
[0:27] use the subdivisions to instance the tiles. And this is simple enough. Here in a basic
[0:35] scene you can see the setup, starting with the grid, with alternating triangles and moving
[0:41] up the middle points. Computing the normals and extracting the centroid of the frames while
[0:47] transferring the normals along. Here I have the grid to copy over which is laying flat
[0:53] on the ground. Now copying these over won't give us the desired results but that is quite
[1:00] simple to solve. We have the normals already, we just need to create the up attribute pointing
[1:08] in the y axis. And then to align it properly we need to rotate the grid 90 degrees since
[1:15] by default whatever is facing the z axis will align with the normal of the points. And
[1:22] this works even with the largest side of the grid aligning properly. But curiosity got the
[1:30] best out of me and as I am stubborn I wanted to find a solution that didn't rely on the
[1:37] initial orientation of the grids. So as you can see in this setup I have exactly the same
[1:42] result but no transform node neither computed normals. And with a few lines of wax we can calculate
[1:51] a new direction of the normal and use the same up attribute. First I am getting the topmost
[1:58] point with the bounding box max function, then calculating a vector by subtracting the current
[2:04] position from the top point, assigning that vector to the normal and using the same up attribute.
[2:15] As you can see by the visualizers now the normal is pointing towards the center top point
[2:22] and up facing in the y. And I still believe there's even a simpler way to achieve this but
[2:30] that's what I came up with, waiting for your suggestions in the comments. Let's move on.
[2:37] Let's see here I did a shading tutorial using Arnold and Maya on creating this rainbow CD effect
[2:45] and wanted to try it in karma. So we're starting with this type of ramp that we will map to the
[2:52] specular rotation at the end. Not gonna bother you with the mat behind but you can see the steps
[2:59] by my setup. The most important node here is the material X rotate to D that will create the
[3:06] rainbow effect, basically offsetting a few degrees the ramp in each shader. Then I have three
[3:14] different materials where the only difference is the base color, one is red, second is green and third is blue.
[3:22] And finally I am adding them together that should add up to white while creating the rainbow effect
[3:30] on the reflection. For the shaders I just have the ramps connected to the specular rotation and
[3:38] an isotropy and metalness set one. As a final touch I use the grunge texture on the roughness channel
[3:46] using a custom triplanar node. So procedural rocks we all been there and in these basic setup I have
[3:57] few tips. The first one is to use the initial shape copy to a single point with a randomized
[4:03] scale attribute. This allows to change the size and shape of the rock by playing with the seeds
[4:10] of the attribute randomized. Another quick tip are now to use a subdivide node to control the
[4:17] roundness of your rock just by playing with the crease weights and adding one or two subdivisions.
[4:25] Let's add a mountain node to randomize the shape and let's say you don't like the effect on the
[4:32] Y axis mostly on the bottom part. Of course you can remove the Y components on the mountain node
[4:39] but that also gets rid of the noise on top. So what you can do is to create a point for
[4:46] with a noise inside using the display's along normal nodes and to achieve the flattening just on
[4:53] the negative Y you can use a clamp on your normals setting the Y component to 0 on min and the
[5:00] desired amount for positive Y. Okay now an exercise on stacking objects with four loops. In this case
[5:10] I have a simple box and using a forage count to generate more in a loop and to align the boxes we
[5:18] access the previous iteration with a new begin node set this time to fetch feedback.
[5:25] Then we can use the result in a match size to align the new box with the previous one in this
[5:31] case the bottom to the top or min to an max. And in between I'm also randomizing the rotation
[5:40] and scale with the iteration value. So I saved the worst tip for last and it's really simple
[5:48] but since Odinit doesn't have a capsule primitive we can create one just with two nodes.
[5:54] A simple line, a sweep node set to round the tube and the end cap to grid. You can then control
[6:03] the height with the line and the subdivisions with the line points and grid subdivisions.
[6:09] So that's it so hopefully you got something out of this feel free to leave a comment and don't
[6:15] forget you can grab all the files from my videos on Patreon along with exclusive tutorials.
[6:23] Thank you and see you in the next one.



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
