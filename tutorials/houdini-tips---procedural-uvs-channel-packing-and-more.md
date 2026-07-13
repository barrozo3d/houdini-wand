---
title: Houdini Tips - Procedural UV's, Channel Packing and more
source: YouTube
url: https://www.youtube.com/watch?v=m00nko87HeI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/
frame_count: 0
frame_status: pending-selection
---

# Houdini Tips - Procedural UV's, Channel Packing and more

**Source:** [YouTube](https://www.youtube.com/watch?v=m00nko87HeI)
**Author:** cgside
**Duration:** 4m36s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tips---procedural-uvs-channel-packing-and-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. In this video I'll share a few tips like procedural UVs, channel
[0:05] packing, pet the former and others. So in this scene I have agreed where I would like


### Squared Procedural UV's [0:09]
**Transcript (timestamped):**
[0:12] to keep squared UVs so my texture doesn't stretch as this is the default behavior of the
[0:18] UV texture node. There are a few ways you can achieve this. The first one is by calculating
[0:25] the ratio of the incoming flat shape and use an if statement in the X and Y scale of
[0:32] the UVs, checking if the ratio is bigger than 1 in X and smaller in Y, then if it falls
[0:40] we can calculate the scaling factor to fit the 0 to 1 scale. We will also need to make
[0:47] the Y value negative so it are unspropriately the UVs and move them to the default UV tile
[0:53] using the offset Y. A simpler approach is by using the UV flat
[0:58] and node, which we'd pretty much default settings, just using the top vertices as an access
[1:06] align vertex group to orient the UVs. This might look like a lot of work when you can
[1:13] simply manually scale the UVs, but if we are doing procedural UVs it can be handy
[1:20] and you can always save it as a preset for later use.


### Channel Packing [1:25]
**Transcript (timestamped):**
[1:25] Now let's check an easy way of doing channel packing so we can use several vertex color
[1:30] channels in Unreal for instance. I have this CD attribute for the eyes which is occupying
[1:36] RG and B of the color attribute, but I also have a concavity mask that I would like
[1:43] to include in the vertex colors. So in a simple wrangle we can take a single value of the
[1:49] original CD and map it to the right channel and do a concavity to the green channel. If
[1:58] you have more you can map it to the blue channel also. Now in Unreal we can separate the channels
[2:04] and apply different effects to them in this case setting the eyes color and adding some
[2:09] occlusion to the concave areas. In this example I wanted to show you how I used


### From Houdini to Zbrush [2:13]
**Transcript (timestamped):**
[2:16] it in a procedural workflow to quickly create a base mesh to further sculpting in the
[2:21] Z brush. So I'm taking this elongated half circle, twisting it and applying some transforms
[2:28] while resembling and saving a curve view attribute. And then add a point in the center and
[2:34] saving it to a group so I can use it in a polycats to divide the curve into two frames.
[2:43] Finally I can sweep it and as you can see if I didn't cut the geometry in half I wouldn't
[2:49] be able to have this particular look I was after which is a mix between a mirror in both
[2:55] axis while twisting. And feeding this to a sculpting program gave me an easier time than
[3:02] sculpting a perfect infinity sign there. In this case I have a pattern following the shape


### Multiple Path Deform [3:05]
**Transcript (timestamped):**
[3:09] of an half circle and the way I'm doing that is first by starting with a chain repeating
[3:16] the pieces along the curve and packing and pat the forming it with a curved half circle.
[3:22] Then taking the original shape and pat the forming it again. And here order of operations
[3:32] matters from what I've tested so it's easier to start with the pat flight and go from there.
[3:39] Also make sure you have the correct scale for your initial pat you can use a measure
[3:44] set to length. For this one I need to orient the legs out so I'm starting by getting


### N and Up to Orient Shapes with Sweep [3:45]
**Transcript (timestamped):**
[3:50] the points from the initial geo making sure to calculate the out normals in the orient
[3:56] along curve. Then in the copy to points I'm keeping the normals and if you have a deform
[4:03] shape you can simply use the normal attribute in the copy to points as it will out of
[4:09] aligned shapes. But in case you have a flat line you will need to rename your normals to
[4:14] the aperture boot so the sweep knows how to orient the polygons. So yeah that's about


### Outro [4:18]
**Transcript (timestamped):**
[4:20] it hopefully you picked up something new that you can use in your next project.
[4:25] Wrap the example files on Patreon and thank you for everyone that joins off our. See
[4:30] you next time.



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
