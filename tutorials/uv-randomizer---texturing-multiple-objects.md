---
title: UV Randomizer - Texturing multiple objects
source: YouTube
url: https://www.youtube.com/watch?v=FK6IRzxYHiY
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/uv-randomizer---texturing-multiple-objects/
frame_count: 0
frame_status: pending-selection
---

# UV Randomizer - Texturing multiple objects

**Source:** [YouTube](https://www.youtube.com/watch?v=FK6IRzxYHiY)
**Author:** cgside
**Duration:** 2m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py uv-randomizer---texturing-multiple-objects <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:03] In this video I'm going to show you how you can build a simple UV randomizer when you
[0:08] have to texture multiple objects and want to avoid texture repetition.
[0:14] So here you can see that we have a lot of repetition on these set of objects because I am stacking
[0:19] the UVs on top of each other to have more texture density.
[0:24] But enabling these UV layout node we can get rid of it for the most part and still maintain
[0:29] enough texture resolution.
[0:32] And we can also randomize the resulting UVs.
[0:36] I'm going to start with a box duplicated 20 times and with some basic UVs applied.
[0:42] Now we need to create an integer attribute dividing the pieces of Gio into different IDs
[0:48] within a range.
[0:50] The total number means how many different islands of UVs we will have, meaning that any
[0:55] repeating ID will be stacked on top of the relative ID.
[1:03] Now we can layout the UVs but as you can see it starts to get crowded and this can
[1:08] hurt our texture resolution.
[1:14] What we can do is use the island attribute under connectivity and take advantage of the
[1:20] attribute we created before.
[1:23] We just need to promote the point attribute to primitive.
[1:29] And now you can see the resulting UVs being laid out into different regions but still
[1:34] stacking the ones with the same ID.
[1:41] In case you want to randomize the IDs you can place a sort node before the wrangle, set
[1:48] it to random and play with the seeds.
[1:51] This is what I've done for my original objects, the exact same setup.
[1:58] And the good thing is that we can still play with the random offset or even remove it if
[2:03] we notice any repeating patterns next to each other.
[2:09] So yeah that's what I wanted to share with you.
[2:12] I am not sure this is the best approach but if you know a better way please let me know.
[2:18] And please check out my Patreon and Gamro if you want to support the channel.
[2:22] Thank you and see you next time.



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
