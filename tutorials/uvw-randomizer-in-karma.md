---
title: UVW randomizer in karma
source: YouTube
url: https://www.youtube.com/watch?v=1SXCz_Ta4Lc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/uvw-randomizer-in-karma/
frame_count: 0
frame_status: pending-selection
---

# UVW randomizer in karma

**Source:** [YouTube](https://www.youtube.com/watch?v=1SXCz_Ta4Lc)
**Author:** cgside
**Duration:** 3m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py uvw-randomizer-in-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this quick tip I want to show you how you can set up a UVW randomizer
[0:07] like you see in renders like V-Ray that's using karma in Odinni and which means going from
[0:17] these really obvious styling patterns to something like this where it's not so obvious and it really
[0:26] breaks the repetition. So yeah let's see how that goes. So we start with a texture coordinates
[0:36] by the way I'm pressing X to preview the note then I'm doing the tiling in this case I'm repeating
[0:45] 15 times so with a multiply on the constants then I can use the module to actually repeat the UVs
[0:55] module set to 1 and this will be the texture coordinates for our place to the where we will do the
[1:07] rotation and for the random rotation we will need to take the multiply where we repeat the texture
[1:16] the UVs and floor it is hard to see but we start to get individual values and it can get better if
[1:27] we do a cell noise to the as you can see and to have some control to have a seed we can use
[1:35] this note keeps getting in the way we can use a random float and as you can see I can change the
[1:44] seeds however I want since we have a different input for each cell then we can remap it this won't
[1:53] look much because I'm remapping it from 0 to 360 which will be the random rotations so having the
[2:01] remap we want to orient it in steps so steps of in this case 90 degrees so we will divide the random
[2:11] values by that step angle which won't look much then we floor that calculation and finally we
[2:21] multiply it again with the step orient so it will look something like this which doesn't
[2:29] meet much but when we connect it to the rotate of the place to D and the place to D the pivot must be
[2:35] on the center so it rotates from the center you can see we have random rotations on the UV tiles
[2:42] and if we feed that to the shader we have something like this and you can see going from this obvious
[2:54] look of tiling to this random field and you can change the seeds so if you don't like the result
[3:05] you can it's right over the seed values and you can change how much repetition you have so 12
[3:17] and let's see if that's still too obvious in the non-randomizer so it's still really obvious on
[3:26] these lines in here and if we check the randomization it looks much better so yeah I will be posting
[3:36] this setup on my patreon if you want to grab it but I believe I showed you everything you need so
[3:44] yeah that was the quick tip I hope you got something out of this and I'll see you next time



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
