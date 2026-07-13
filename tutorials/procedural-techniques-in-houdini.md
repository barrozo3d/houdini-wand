---
title: Procedural techniques in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=PcP9Eieij1g
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-techniques-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural techniques in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=PcP9Eieij1g)
**Author:** cgside
**Duration:** 2m40s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-techniques-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi there and welcome. In this video I'll show you how I combine different procedural techniques
[0:05] in Odini to create this final image. The full project can be found on the link in the
[0:11] description. So as you can see the caramel on this cookie ice cream has some layers across


### Density by attribute [0:12]
**Transcript (timestamped):**
[0:17] the Y-axis. Let's see how that can be achieved within a flip sim. So for that effect I'm creating
[0:24] a density attribute by dividing my flip source into sections using the bounds of the point
[0:30] cloud. Also adding some noise to give it some variation and lurping between the sections
[0:37] and another noise on the bottom. Finally, remap the density values to fit the flip
[0:43] sim and make sure you enable density by attribute in your flip solver. Now let's see how to


### Cookie undulating effect with vex [0:49]
**Transcript (timestamped):**
[0:50] create this only lighting effect on the cookie borders. Basically I'm using the sin function
[0:56] along the curve view, making sure it's absolute to get only positive values. To ensure we get
[1:05] consistent sizes along the curves I am also multiplying by the length of the curve and finally
[1:11] this place the position along the normal with those values. To create the burn defect on the


### Distance along geometry [1:16]
**Transcript (timestamped):**
[1:17] edges of the cookie I am saving the unshared points before the bullion, then group again the
[1:23] unshared points and group combine them to separate the holes from the border. And in the end
[1:29] just create a attribute mask with the distance along geometry for both groups. The drops were


### Adding droplets with vdb's [1:36]
**Transcript (timestamped):**
[1:37] created after the seam and for that I am manually selecting a few points and copying a curve
[1:43] to it with a random b scale. Then just sweeping it playing with the scale along curve and setting
[1:49] the end caps to grid. Create a VDB for both meshes and combine them. And finally we can
[1:56] blur the transition using a smooth SDF with a mask coming from the second input.
[2:01] So the materials on this scene are quite simple. For the cookie I am using the save


### Cookie material in karma [2:03]
**Transcript (timestamped):**
[2:08] that reboots to drive the colors. Using the material X mix node with the masks as a mix factor
[2:15] to blend different colors. Then just use a random noise detection as band map. So that's what I


### Outro [2:24]
**Transcript (timestamped):**
[2:25] have for you today. I hope you got something out of this and make sure to check out my Patreon
[2:31] where you can download this full scene and many more. Thank you and see you next time.



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
