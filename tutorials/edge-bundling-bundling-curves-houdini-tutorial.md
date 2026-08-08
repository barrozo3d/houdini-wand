---
title: Edge Bundling / Bundling Curves – Houdini Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=Mypavnx92tw
author: Konstantin Magnus
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/edge-bundling-bundling-curves-houdini-tutorial/
frame_count: 0
frame_status: pending-selection
---

# Edge Bundling / Bundling Curves – Houdini Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=Mypavnx92tw)
**Author:** Konstantin Magnus
**Duration:** 6m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py edge-bundling-bundling-curves-houdini-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] My name is Konstantin Magnus. In this Houdini tutorial, we are going to bundle curves into networks, either that kind of bubble shape, or when we want to pin down the endpoints, we get this kind of network.
[0:14] Let's start from scratch. With a new document, we are going to set up a grid. The grid can be oriented to the XY plane. I'll choose a size of 1 by 1 for now, and switch the connectivity to rows.
[0:34] If you enable the points, you can tell that we are able to increase the number of rows while we keep the divisions to none, so just choose two columns for two endpoints.
[0:52] I would like to collapse the entire grid to zero, so I have more control when I randomly place the endpoints using a jitter node.
[1:06] Let's disable the x-axis. We have a set of two-dimensional curves, potentially intersecting each other.
[1:18] Now I would like to increase the resolution using a resample node set to 0.01, so that way we have plenty of points to bundle.
[1:30] We are going to use two standard nodes to shape these curves using the attribute blur node set to proximity.
[1:42] This will enable us to bundle these curves as soon as we disable the pinning of the boundary points. I can increase the maximum neighbors to all points for now. This is of course not ideal, but it's a start.
[2:03] I'll use a rather low radius, let's say 0.06. There are two modes we can use. I would recommend to start with volume preserving to get those bubbles.
[2:17] As you can tell the curves look a bit damaged, so I would like to compensate the shape with a smooth node, which we can set to a low quality and a strength of just five.
[2:37] This is roughly the effect I'm after. In order to really be able to change the look, I would like to cut out these nodes and put them inside a for loop.
[2:57] This looks promising. Let's see whether it still looks good after 40 iterations. This is where you can dial in the effect. The resolution of the curves set to 0.01, the blur set to 40 by 0.06 and the smoothness which currently stands on a strength of five.
[3:20] This is one look we are after and we can also play with pinning down the endpoints. In a separate geometry stream, I would like to use the group expression node to select the endpoints after the resampling because the resolution has changed.
[3:45] We should choose the point group and the preset called point valence set to one. I call that group pin and these endpoints I would like to not change.
[4:06] Let's choose the group pin with an exclamation mark in front to spare these points. For this effect, I want to switch to the Laplacian mode, which looks more like a road network in this case.
[4:22] Inside the smooth node, I also want to constrain the pinpoints. After a few iterations, I get this kind of result which is too extreme for my liking. Let's try to find out how to dial this in.
[4:37] It gets a lot better by not blurring the positions as much and we could also play with the smoothing depending whether you would like to have a rather rounded curvy look or a rather strict look. You can play with the settings here as well.
[4:58] Once you're happy with the results, you can also copy out these nodes inside a solver. That way we can create an animation.
[5:09] I'll choose the real-time toggle and inside the solver, I just integrate these three nodes in my case. When we jump back, we can now hit play and see our curves in effect.
[5:30] For more clarity, you may want to use a color node set to primitive random. That way it's easier to see what's going on.
[5:41] The same would work for the slightly longer way, which creates these networks. Let me quickly demonstrate this inside another solver.
[6:11] Alright, thank you for watching.



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
