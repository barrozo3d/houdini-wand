---
title: Controlling instance probability in Solaris
source: YouTube
url: https://www.youtube.com/watch?v=OWMKqhVaFF8
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/controlling-instance-probability-in-solaris/
frame_count: 0
frame_status: pending-selection
---

# Controlling instance probability in Solaris

**Source:** [YouTube](https://www.youtube.com/watch?v=OWMKqhVaFF8)
**Author:** cgside
**Duration:** 2m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py controlling-instance-probability-in-solaris <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] I have everyone and welcome back. In this quick tip I'm going to show you how you can have control over your instances in Solaris.
[0:08] So as you can see I have these color trees just as an example.
[0:15] And by default the InstaSare in Solaris is using a random distribution. We can change the seed but that's about it.
[0:23] We also have the index but it's not very useful by itself and the option we are looking for is index attribute.
[0:33] So we need to create that attribute inside the InstaSare but also keep some randomization.
[0:40] Let's use the attribute randomize, change the name to probability, you can emit anything you want and change the distribution to custom discrete.
[0:52] Now here you need to enter the amount of objects you have in this case I only have three.
[0:58] Next you want to give it an index starting from zero.
[1:03] Let's copy the name of the attribute and paste it in the InstaSare index attribute field.
[1:10] As you can see we have no change. We can check the warning reporting that didn't find any attribute named probability and it's using the index zero or red trees.
[1:23] The problem is that the attribute randomize is outputting float values and we need integers for the index attribute.
[1:33] So that's easy to solve just use an attribute cast and we can convert it to an integer.
[1:40] And now we can control the amount of each tree or the probability of a particular instance.
[1:46] So yeah as you can see it's quite easy to set it up but you have to know the logic and step required.
[1:54] Hopefully this can help you and as I'm working on this project I might be sharing a few tips.
[2:00] Check out my patron and Gumroad if you feel like supporting the channel and see you in the next one.



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
