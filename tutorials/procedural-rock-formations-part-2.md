---
title: Procedural Rock Formations  Part 2
source: YouTube
url: https://www.youtube.com/watch?v=6GV1b8Ed_JI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-rock-formations-part-2/
frame_count: 0
frame_status: pending-selection
---

# Procedural Rock Formations  Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=6GV1b8Ed_JI)
**Author:** cgside
**Duration:** 3m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-rock-formations-part-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. Let's see how we can create some rock formations using very basic techniques in Odini.
[0:08] We start by fracturing a cube and transforming it so we get dollar shapes.
[0:15] In this loop I am applying some edge damage and placing the assets in the center.
[0:20] We will copy these shapes to some points and starting with a circular patch I am creating a naturoput mask that goes from the edges to the center so I can manipulate the scale of the shape.
[0:35] Remapping the values and in here I am assigning that attribute to the scale Y so I can get longer shapes at the center.
[0:43] Then randomizing a bit the scale and the normals and of course scattering some points.
[0:50] And when we copy to points we get this sort of follow from the center to the edges created by the scale attribute and the initial mask.
[1:01] Okay in the next step I am applying some volume noise to break the surface using VDVs.
[1:07] Nothing I haven't shared before if you've been following this series.
[1:14] Then I am remashing in this case in a compiled loop so it goes a bit faster.
[1:20] From here I am applying some triplanar textures for displacement and also some quick texturing.
[1:28] And in the point of up I am displacing the geo and exporting the texture attributes like the grass texture.
[1:37] We will also need some procedural maps for texturing like the slope and the curvature and finally we can apply some textures to the model.
[1:52] In this case using a few color mix notes to blend between textures using the respective procedural maps.
[2:01] Then just assigning some quick material for preview purpose.
[2:07] So just to finish we can use the shortest path notes to create some vines at the bottom.
[2:16] I am creating a start point group at the bottom creating a mask along the Y axis and keeping the bottom part where I will have the vines.
[2:28] Now we need the end points so for that I am just creating a random selection of points and we can create the shortest path from the initial point to all the end points.
[2:40] From there we just sweep it, add some UVs and finally a quick material.
[2:48] Might not be the most convincing vines but it will do the trick.
[2:54] So there you go some quick setup I wanted to share with you and feel free to grab the file on my Patreon.
[3:01] Hopefully you get away with some new techniques for your next project.
[3:07] Thank you for watching and see you soon as Adini20 is around the corner.



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
