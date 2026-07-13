---
title: Procedural assets and shading with Houdini and MaterialX
source: YouTube
url: https://www.youtube.com/watch?v=fSouWuGd_Tg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-assets-and-shading-with-houdini-and-materialx/
frame_count: 0
frame_status: pending-selection
---

# Procedural assets and shading with Houdini and MaterialX

**Source:** [YouTube](https://www.youtube.com/watch?v=fSouWuGd_Tg)
**Author:** cgside
**Duration:** 4m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-assets-and-shading-with-houdini-and-materialx <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi there and welcome back. So in this video I'm going to walk you through a simple setup for creating procedural assets in Odini and
[0:08] I will look at Karma and material X noises for procedural shading.
[0:14] The project files for this video will be uploaded to Patreon if you want to dissect it.
[0:20] So for the individual bananas, I just use the mix of procedural and direct modeling techniques
[0:26] but you can just replace it with a banded tube with some tapering.
[0:31] I also painted a mask to use in salaries.
[0:35] So for the bench that looks like this, I started with a tube,
[0:40] selected a few faces with the range nodes,
[0:43] add a mirror for two layers of bananas and
[0:47] Extracted the centroid where I'll be placing them.
[0:51] Okay, now we need to add normals to worry on the bananas.
[0:55] In this wrangle, the first part is to create normals that point outwards.
[1:00] Then I am flattening the normal Y-axis.
[1:03] After that, I am creating a blend slider so I can mix the two normals orientation,
[1:09] which I am doing with the layer function. The last line just sets the attributes to the positive Y-axis.
[1:16] If I play with the blend slider, you can see how I can edit the orientation of the normals,
[1:23] making them more or less flat.
[1:26] You're just randomizing a bit the normals so I can have a less uniform distribution of the banana bunch.
[1:35] Okay, now we need to place the cluster of bananas in the main stem.
[1:40] And for that, I am starting with the line with the same size of the tube that acts as the stem.
[1:46] Adding a mountain node to break the uniformity,
[1:50] carving it so I can control where the banana bunch starts and ends along the stem,
[1:57] resembling it and adding some jitter to the Y-axis.
[2:03] Now adding normals along the X-axis.
[2:06] And here is where we orient the point so we have a spiral effect.
[2:12] So I am creating a variable where I set an interval of rotation around 90 degrees with some seed.
[2:20] Then for each point, I multiply the point number by the rotation amount,
[2:25] creating that way the spiral effect.
[2:30] Also adding some random scale for each cluster.
[2:35] And of course copying the banana cluster to these points.
[2:39] For the stem, a simple tube with a mountain node to affect the position and some gravity ends.
[2:46] Then in order to target the different parts in Solaris, I am adding a name for the stem and the bananas.
[2:52] And that's about it for the subset up.
[2:56] So the first thing you want to do in Solaris when you import back geo is to set those primitives to be a point insta-ser.
[3:05] As for the shading, first I am importing the mask for the tips of the bananas using the Geo property value nodes.
[3:15] Then using a color mix, I am assigning a dark brown to the tip and some other color mix downstream.
[3:24] Here I am using 3D noises and in order to tile them, you need to connect a position node with a multiply
[3:31] where you set the amount of repetitions you want.
[3:36] Then in the mix I am adding bits of grid.
[3:39] The last mix just blends the main yellow color with some brown using a fractal 3D noise.
[3:47] As for the shader itself, there's just some mid-graphness values and a bit of SSS.
[3:54] So that's about it. Hopefully you picked up a few tips. There are still some inconsistencies in this setup
[4:01] like avoiding intersections between the bananas or really simple shading setup.
[4:08] But hopefully I can cover that in another time.
[4:11] Don't forget to check out my Patreon if you want to support the channel and download the project files.
[4:17] Thank you and see you in the next one.



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
