---
title: Christmas lights vex animation in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=u7SGkPTaJKs
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/christmas-lights-vex-animation-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Christmas lights vex animation in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=u7SGkPTaJKs)
**Author:** cgside
**Duration:** 4m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py christmas-lights-vex-animation-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello there and welcome back.
[0:02] So in this tutorial we're going to create the Christmas lights animation with Odini.
[0:07] So this is my final setup with some lead strip, but we're going to build a simple example.
[0:14] Let's start by creating a light and set it to sphere.
[0:18] Now we need an instacer to instance the light.
[0:23] We're going to use a simple line with a few points.
[0:28] As we can't really instance lights, let's set the instacer to reference and we should have duplicates of the lights on the line points.
[0:38] Here I'm just pruning the original light so it doesn't render.
[0:46] Now inside the instacer we will create an attribute called intensity so we can use it later.
[0:52] Just link the light intensity to the value of the attribute create.
[0:57] Next I want to create a pattern of four colors repeating along the line.
[1:03] So let's create a for loop to automate the process.
[1:06] We will need detailed attributes from the metadata node, so create one.
[1:13] Now we can use a group by range to select all the points within a pattern.
[1:18] As we need for colors select one out of four in the range.
[1:22] And then we can use the offset to create the different groups of colors.
[1:27] Let's set the number of iterations to four and use the iteration value in the offset of the range node.
[1:37] And also rename it group with the iteration value.
[1:42] As you can see we have all the different groups at the end of the loop.
[1:48] Now creating all the different colors and targeting the groups from before.
[1:54] In order to assign each color to a different group we will use a switch with the input set to the iteration value.
[2:05] And we now have a pattern of four colors on the lights.
[2:08] The only thing missing is the animation.
[2:12] So inside the instacer creates a point wrangle to add some wax codes.
[2:18] I am going to load a preset for a pattern and explain how it works.
[2:23] It's quite simple maybe there are better ways of doing this.
[2:27] But this is my first time writing wax.
[2:30] Let's just connect a re-time node to cycle the animation.
[2:36] Now the codes.
[2:38] At the top I am getting the original intensity value of the lights set up in the attribute create.
[2:45] Then for 36 frames we will create the first animation pattern.
[2:50] So for every two frames and if the point number is even or for every other two frames and point number is odd,
[2:59] set the intensity of the light to the original value.
[3:05] While turning off the light when it doesn't match the pattern.
[3:09] After the first pattern till frame 54 for every other frame and if the point is even,
[3:16] the red and yellow lights turn on and off the intensity.
[3:21] And we do the same in the last pattern for the green and blue lights.
[3:26] Finally we set the intensity point attribute.
[3:30] And this is the pattern that it creates nothing complicated really.
[3:34] And you can easily change this code to create other patterns.
[3:38] For my sample scene I just created a lead strip and instance the lights in the points.
[3:44] And this is it really simple stuff but hopefully you picked up a few tips.
[3:49] Let me know how would you approach this in a different way.
[3:53] Maybe with a simple expression or some other setup.
[3:57] Thank you for watching and see you in the next one.
[4:00] Happy Holidays!



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
