---
title: Houdini Solaris Tutorial - Rendering Multiple ROPS Together
source: YouTube
url: https://www.youtube.com/watch?v=qg3OFz4JZs4
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Not specified (H20–H21 UI)"
tags: ["lop", "solaris", "rendering", "karma", "top", "pipeline", "beginner"]
extraction_status: complete
frames_dir: tutorials/frames/houdini-solaris-tutorial---rendering-multiple-rops-together/
frame_count: 0
---

# Houdini Solaris Tutorial - Rendering Multiple ROPS Together

**Source:** [YouTube](https://www.youtube.com/watch?v=qg3OFz4JZs4)
**Author:** Voxyde VFX
**Duration:** 1m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey guys, it's Som here from Waxa.com and in this video I will show you a really quick way to render all your sequences at the same time. So I got my scene here, I got my rain character and some other effects and I set it up my renders so I got my character, my blast and I don't want to render out everything manually so a render to disk. So we use an automation for this, so we're creating a top network like so and diving in. In here we're just using one specific node, the ROG fetch node. If you have a lot of different renders, there's a really quick way to also set it up procedural. Just name your ROG fetch node exactly like your ROG outputs nodes. So I will call this my character, this will be my blast, I also got my bug, my rain and the water. Now I just select all the nodes and in the ROG head node I type stash stage, flash the lowest. After that we're changing the ROG cook order from frame by frame to node by node. With this change we're starting with the character and just rendering out completely the character after the blast and so on. You could also use the frame by frame but I prefer this. After that we switch to frames and batching. In here we change from single frame to ...



---

## Structured Notes

### Core Technique
Using a TOP (Task Operator) network with `ropfetch` nodes to automate batch rendering of multiple Solaris/LOP ROP outputs simultaneously, with node-by-node cook order and frame batching for efficient pipeline render submission.

### Summary
A quick 1.5-minute tip tutorial demonstrating how to render multiple Karma/Solaris ROP outputs (e.g. character, blast, particles, rain, water) in a single automated batch using a TOP network. The workflow creates a `topnet`, adds one `ropfetch` TOP node per ROP output (named to match the LOP render node names), sets the ROP fetch node's path to the corresponding LOP stage, switches the cook order from "frame by frame" to "node by node" so each sequence renders completely before the next, then switches frame mode to batching for chunked render submissions. Eliminates the need to manually trigger each render-to-disk sequentially.

### Key Steps
1. Set up multiple Karma ROP / render-to-disk nodes in the LOP network — one per render element (e.g. character, blast, rain, water, particles); name each node clearly
2. At the OBJ level (or anywhere above LOPs), create a `topnet` node and dive inside
3. Inside the TOP network, add one `ropfetch` TOP node per LOP render node; name each `ropfetch` node identically to its corresponding LOP render node name for easy mapping
4. In each `ropfetch` node: set the ROP path to `stash:/stage/<lop_render_node_name>` (or use the direct LOP path); this connects the TOP to the Solaris render chain
5. Select all `ropfetch` nodes → in parameters: change **ROP Cook Order** from "Frame by Frame" to "Node by Node" — this renders all frames of one sequence before moving to the next (preferred for disk I/O efficiency)
6. Switch to **Frames and Batching** mode; change from Single Frame to a batch size matching your frame range (e.g. 1–240); allows chunked submission to render farm or local queue
7. Press Cook or submit to PDG/farm — all ROP outputs render sequentially without manual intervention

### Houdini Nodes / VEX / Settings
- `topnet` — TOP network container; create at OBJ level or inside Solaris
- `ropfetch` TOP — ROP Path: `stash:/stage/<rop_node_name>` or direct LOP node path; one per render element; name matches LOP render node
- **ROP Cook Order** — "Frame by Frame" (all ROPs per frame, then next frame) vs "Node by Node" (all frames of one ROP, then next ROP); Node by Node preferred for sequential disk writes
- **Frames and Batching** — Single Frame vs batch size; set frame range for full sequence submission
- `karmarendersettings` LOP — the render nodes being fetched; must be configured with camera, resolution, output path before TOP submission
- `renderproduct` LOP — sets file output path for Karma; referenced by ropfetch

### Difficulty
Beginner

### Houdini Version
Not specified (H20–H21 UI)

### Tags
#lop #solaris #rendering #karma #top #pipeline #beginner

---

## Related Tutorials
- [Intro To Houdini Solaris - Full Beginner Course](./intro-to-houdini-solaris---full-beginner-course.md) — #lop #solaris #usd #rendering #karma #beginner
- [Improve Solaris Performance - Houdini Tutorial](./improve-solaris-performance---houdini-tutorial.md) — #lop #solaris #usd #rendering #performance
