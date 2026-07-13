---
title: Displacement maps in cops | Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=xOeZncLWztc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/displacement-maps-in-cops-houdini-205/
frame_count: 0
frame_status: pending-selection
---

# Displacement maps in cops | Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=xOeZncLWztc)
**Author:** cgside
**Duration:** 2m59s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py displacement-maps-in-cops-houdini-205 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, in this video I'll share a few useful workflows when working with cops in the New Odin 20.5.
[0:08] The full scene is available on my Patreon.
[0:11] So the first one is on how to create this chamfer look for your displacement maps, and it's quite easy, you can just use the feather note and play with the distance.


### Beveling with the feather node [0:12]
**Transcript (timestamped):**
[0:23] And this is different from the blur, where it would just smooth out the shapes.


### Isolating rows/columns with tile pattern [0:28]
**Transcript (timestamped):**
[0:28] If you only want one row of shapes with the style pattern notes, you can play with the pruning either by a tolerance value or by every other row or column.


### Mirror node in cops [0:39]
**Transcript (timestamped):**
[0:39] You also have a mirror note in cops, but here you need to set the angle and the distance as offset.


### Segment by connectivity, statistics by id and compare nodes [0:46]
**Transcript (timestamped):**
[0:46] So now I want to fill some shapes with patterns, and for that I am using the segment by connectivity notes, which will create this sort of pattern.
[0:57] Next I can use statistics by ID to isolate similar areas.
[1:02] In the composite view I can inspect the target value and feed it to a compare note in this case I set it to equals 2.
[1:10] And as you can see I successfully isolated the target areas.
[1:15] I have done the same for the middle parts, then just multiply some patterns over those areas.


### Custom points with orientation attribute [1:22]
**Transcript (timestamped):**
[1:22] For this specific star pattern I used a stop-import to create my own points, created a circle with the amount of points I need and also added the normals with wax, along with some custom biscale for every other point.
[1:38] And when I feed it to a stem point I get the expected result.
[1:44] Now tiling it, setting the pattern type to weather bound, which is the alternating setup.
[1:50] Instead of adding too many repetitions to the tile pattern, you can just scale it down and it will keep the tiling.


### Stamp points with custom shapes [1:58]
**Transcript (timestamped):**
[1:58] Since I found the tile pattern a bit hard to control the spacing, for this bottom pattern I created my custom points with a stop-import and used again the stem points, feeding the shape to the stem-import.


### Align patterns with mesh uv's [2:14]
**Transcript (timestamped):**
[2:14] As I need to align the pattern to my OVs I'm importing the original object using a RESTORISE setup to get the UVs position and a RESTORISE GU.
[2:27] Then I can use a blend with the pattern to check where I should translate it to.


### Final displacement/height map [2:33]
**Transcript (timestamped):**
[2:33] And finally connected to the eye channel of my preview material I am also using some ambient occlusion for preview purpose on the base color.


### Outro [2:43]
**Transcript (timestamped):**
[2:44] So I hope this helps you finding your ways in the new cups. It's still all new to me and I'm planning to share more in the future.
[2:52] Stay tuned and check the file in the description. Thank you.



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
