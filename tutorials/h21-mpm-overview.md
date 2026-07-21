---
title: H21 MPM Overview
source: YouTube
url: https://www.youtube.com/watch?v=nD183jP3H4Y
author: Houdini
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/h21-mpm-overview/
frame_count: 0
frame_status: pending-selection
---

# H21 MPM Overview

**Source:** [YouTube](https://www.youtube.com/watch?v=nD183jP3H4Y)
**Author:** Houdini
**Duration:** 3m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py h21-mpm-overview <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:30] Hello and welcome to this very exciting MPM Masterclass for Udini 21.
[0:57] My name is Alexandre Wevinger and this Masterclass is a follow-up on the Masterclass that I did
[1:02] for 20.5 and just so you know, this is not an introduction to MPM.
[1:07] So this already assumes that you know how the solver works at the high level, so in general
[1:11] how to use it.
[1:12] And here we're just talking about the new features that we introduce as well as the
[1:16] new nodes that we added to streamline the post simulation workflow.
[1:20] So let's take a look at the outline of this Masterclass.
[1:24] So first thing, we look at the new features.
[1:26] So we added surface tension to MPM, another sleep mechanism, continuous emission expansion,
[1:31] so it seems a little complicated, but it's just to allow you to source material on top
[1:35] of existing material and create internal pressure.
[1:39] We added per voxel varying friction and stickiness, so this is very helpful if you want to have
[1:45] control over the friction and stickiness per voxel on your colliders.
[1:50] So this skips the hack that we used to do in 20.5 where we would duplicate the colliders,
[1:56] but we're going to see that in more details.
[1:58] We have greatly improved the deforming colliders.
[2:01] Then when we're done with the new features, we're jumping into those post simulation nodes.
[2:05] So those nodes are all there to just help you streamline the post simulation workflow.
[2:09] So it helps you with surfacing, with debris emission, based on where the material is fracturing.
[2:15] And we have those two nodes at the end that work kind of together and this helps you replicate
[2:20] body dynamics kind of workflow.
[2:23] So you can use MPM to simulate very stiff material like concrete, for example, and then at the
[2:28] end of the simulation, you can pick this last state of the MPM sim and use that to fracture
[2:34] your original asset.
[2:36] And when you're done with this step, you can just retarget the dynamics of the MPM simulation
[2:40] onto this post fractured asset.
[2:43] So this might seem a little bit confusing, but in practice, it's going to make sense
[2:48] when we look at it in Udini.
[2:51] When we have the basics out of the way, now we jump to practical demo scenes.
[2:55] And these are all the scenes that you saw at the very beginning of this presentation.
[2:58] So we're not going to do any of these from scratch because that would be way too long.
[3:02] But we're going to go through the setups and I'm going to highlight the important parts
[3:06] so you can see how to use those new feature and nodes in more like practical real world
[3:11] scenarios.
[3:12] And hopefully all of the assets and obviously the IP file is going to be available to you.
[3:18] You can look at all of those examples on your own or follow along as I'm presenting these.
[3:25] So enough talking, let's jump into it.



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
