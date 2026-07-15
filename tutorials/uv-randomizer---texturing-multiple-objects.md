---
title: UV Randomizer - Texturing multiple objects
source: YouTube
url: https://www.youtube.com/watch?v=FK6IRzxYHiY
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.493"
tags: [uvs, texturing, connectivity, sort, vex, procedural-uvs, tiling]
extraction_status: complete
frames_dir: tutorials/frames/uv-randomizer---texturing-multiple-objects/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UV Randomizer - Texturing multiple objects

**Source:** [YouTube](https://www.youtube.com/watch?v=FK6IRzxYHiY)
**Author:** cgside
**Duration:** 2m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:20] tutorials/frames/uv-randomizer---texturing-multiple-objects/frame_000.jpg
- [0:45] tutorials/frames/uv-randomizer---texturing-multiple-objects/frame_001.jpg
- [1:05] tutorials/frames/uv-randomizer---texturing-multiple-objects/frame_002.jpg
- [1:40] tutorials/frames/uv-randomizer---texturing-multiple-objects/frame_003.jpg
- [2:10] tutorials/frames/uv-randomizer---texturing-multiple-objects/frame_004.jpg

---

## Structured Notes

### Core Technique
Break up obvious texture repetition across many duplicated objects (e.g. railway sleepers/planks) by assigning each piece to one of N UV "islands" via an integer ID attribute, then using UV Layout's island-stacking behavior so same-ID pieces share space while different-ID pieces get laid out separately — randomizing the ID assignment for a natural, non-repeating look.

### Summary
Instead of stacking every duplicate's UVs on top of each other for maximum texture density (which causes obvious pattern repetition), a wrangle assigns each piece an integer ID within a chosen range (the "how many distinct UV islands" control). UV Layout then stacks pieces sharing the same ID on top of each other, but lays out different IDs into separate regions — trading a bit of texture resolution for visible variation. Randomizing the piece order with a Sort node (set to random, with a seed) before ID assignment removes any leftover visual pattern from nearby pieces sharing IDs.

### Key Steps
1. Start with the base geometry duplicated many times (example: a box duplicated 20 times to look like railway sleepers), each with basic UVs applied.
2. In a wrangle, create an **integer attribute** that divides the pieces into different IDs within a chosen range — the total number of distinct values is how many separate UV islands/regions will exist; any pieces sharing the same ID get stacked on top of each other.
3. Run **UV Layout** with default settings first to show the baseline problem: laying out every piece separately gets crowded and hurts effective texture resolution.
4. Use **Connectivity**'s island attribute together with the ID attribute created above: promote the point-level ID attribute to a **primitive attribute** (required by UV Layout to read it correctly).
5. With the primitive-level ID attribute now feeding UV Layout, pieces sharing an ID stack on top of each other while different IDs get laid out into separate regions — giving a balance between texture resolution and variation.
6. To randomize which pieces share which ID (avoiding a still-visible repeating pattern), insert a **Sort node** set to random (with a seed) before the ID-assignment wrangle, so the ID distribution across pieces is shuffled rather than sequential.
7. Fine-tune by adjusting the random offset/seed, or removing it if repeating patterns are still noticeable next to each other.

### Houdini Nodes / VEX / Settings
Box (duplicated), UV unwrap, Attribute Wrangle (integer ID attribute within a range), UV Layout (default packing vs. island-stacking via attribute), Connectivity (island attribute), Attribute Promote (point → primitive for the ID attribute), Sort (random, with seed).

### Difficulty
Beginner–Intermediate (simple attribute + UV Layout combination, easy to adapt to other repeated-asset scenes).

### Houdini Version
19.5.493 (visible in viewport title bar).

### Tags
uvs, texturing, connectivity, sort, vex, procedural-uvs, tiling

---

## Related Tutorials
- [Procedural UVs - UV Layout Node in Depth](procedural-uvs---uv-layout-node-in-depth.md) — deep dive into UV Layout's island/UDIM/scale attributes, including the same island-stacking-by-attribute technique used here.
- [Orient UVS like a PRO in Houdini 21](orient-uvs-like-a-pro-in-houdini-21.md) — related procedural UV-manipulation tooling from the same channel.
