---
title: Resample Color Ramps in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=P-2FPlUJO60
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/resample-color-ramps-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Resample Color Ramps in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=P-2FPlUJO60)
**Author:** cgside
**Duration:** 2m18s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py resample-color-ramps-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this quick tip I wanted to show you how you can use Python to
[0:06] re-sample your color ramps. So going from this to something like this. And this is actually pretty simple.


### Tutorial [0:15]
**Transcript (timestamped):**
[0:17] We first saving the selected node so we need to have the node selected that we want to change the
[0:28] parameter. Then we access the parameter ramp which if you can see in here is called actually ramp.
[0:38] And then we just evaluate it to gather the values. And then we need to make three lists which are the
[0:48] base of any color ramp. So the interpolation, the position and the values which in this case are
[0:56] colors. So the interpolation will be a list of the ramp basis how it's called. And then for the
[1:05] position it's called keys and for the colors is the values as I told you. Then we set the amount
[1:12] of points we want to end up with. In this case I chose 10. Then we create a list of evenly spaced
[1:23] values for the new positions. So these positions in here. And finally we we we sample the previous color
[1:33] at that specific position with the lockup command. And at the end we just set the audio
[1:41] in a little tramp to use the basis which we didn't change. The new keys, the evenly spaced positions.
[1:52] And the new values which are the sampled colors from this variable. Then we just set it at the end.


### Outro [2:00]
**Transcript (timestamped):**
[2:00] So yeah that's basically it. If you want you can grab the script on my Patreon alongside with
[2:07] all the project files from my videos and exclusive tutorials. So make sure to check that out.
[2:14] And thank you for watching. See you next time.



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
