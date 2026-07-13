---
title: Rock formations with heightfields
source: YouTube
url: https://www.youtube.com/watch?v=rEn0ochILjU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/rock-formations-with-heightfields/
frame_count: 0
frame_status: pending-selection
---

# Rock formations with heightfields

**Source:** [YouTube](https://www.youtube.com/watch?v=rEn0ochILjU)
**Author:** cgside
**Duration:** 5m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py rock-formations-with-heightfields <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to show you how I created this
[0:07] sort of rock formations using I'd fields. So I started with the Nightfield and drawing
[0:20] a mask. In this case you can change to the shape you want. Then I'm using a Nightfield
[0:28] layer to mix two masks, one slightly more blurred. As you can see so we can layer a bit
[0:37] the bottom and I'm setting the Nightfield layer to maximum. Then in this volume drop I am
[0:46] just creating a random baronoid pattern that will create different heights at each point
[0:57] and you can change the seed and minimum value and the maximum value for heights. And this
[1:07] is done by using a baronoid noise and then using a random from the near output just using
[1:19] a random and I'm just adding a value here for the seeds and finally fitting the range and
[1:28] multiplying by the mask, the current mask. So after that we can use the mask expands but set to
[1:40] the height layer so we can create these square life shapes. You can change the amount. In this
[1:52] case I set it to a quite high value. Doesn't look much right now but should have a better shape at
[2:01] the end. Then I'm blurring a bit and clearing the mask. Then right here I'm just creating
[2:10] the slope layer mask that we will use later and just clearing and then I'm using a Nightfield
[2:19] noise here set to Shabby Shaps, as you can see and then I'm using a Distort by Layer that will create
[2:31] these random shapes as you can see. Then I'm blurring a bit the Nightfield and doing another distortion,
[2:46] just basic distortion, masking the flat areas just a bit more than the flat areas so it has some
[2:57] some falloff and then using a noise to distort a bit the tops as you can see using the mask with some blur.
[3:13] Then I'm clearing the mask and doing again a mask expands set to the eye channel so it creates
[3:23] these bulky shapes as you can see. Then another Distort, small Distort and converting the Nightfield.
[3:38] Then I am clipping the the extra parts remashing
[3:46] as you can see because this sort of geometry won't work while with for texturing or displacement
[3:59] so we need to remesh it. Then right here I'm applying a triplanet this place as I have shown in
[4:10] other tutorials. I am applying two in this case blurring the normals and doing the displacements
[4:19] if I enable the sub divide we should see a weather result. So this is the result of the displacement
[4:27] just adding the details on the sides that are difficult to devolume environment like the Nightfields.
[4:37] If you don't have some sort of slope it won't really create details.
[4:45] So then I'm calculating the ambient occlusion.
[4:52] As you can see this is a result of the ambient occlusion.
[4:56] Then I'm doing a point pop to add some color and the way I'm adding color is by sampling a
[5:07] texture by right clicking here and choosing sample screen colors and then you can sample from a
[5:16] texture in this case I use this one just drag the mouse along the texture then I'm just
[5:25] since it's too dark I'm using a quick material and that should give us a more normalized output.
[5:36] So yeah that's basically it's if you want to download the file feel free to do it on my patron
[5:43] and let me know what you think in the comments. Thank you and see you in the next one.



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
