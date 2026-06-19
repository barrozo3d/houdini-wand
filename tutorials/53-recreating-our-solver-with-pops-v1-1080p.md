---
title: 53 recreating our solver with pops v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9objvx69_58
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/53-recreating-our-solver-with-pops-v1-1080p/
frame_count: 4
---

# 53 recreating our solver with pops v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9objvx69_58)
**Author:** The VFX School Archive
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en And what we can do is we can create a pop network. And we'll The first thing is that we don't really need to scatter points. We can just feed the surface directly to the first input of the pop network. And that's going to work. We In terms of creating the attributes, we also don't need to worry too much about any any of these. Let's just go directly to the pop solver. Now, we were generating 100 particles on each frame. So, here when you go inside a pop network, we'll have to take that into consideration. So, this is the pop solver. This is where every all the calculations will happen. This is the pop object, which is where the information is going to be stored. This is basically just a container that will save all the information that we need. It's through this node that we'll be able to access what's happening. And this is These are the operators that are going to be feeding new information into the solver to make for things to change through time. The first operator that we have here is a pop source. And the pop source, by default, is going to work by using as a source, the geometry source is going to be first contact geometry, and the emission type i...

**Frame:** tutorials\frames\53-recreating-our-solver-with-pops-v1-1080p\frame_000.jpg


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
