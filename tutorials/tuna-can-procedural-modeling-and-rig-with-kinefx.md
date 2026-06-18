---
title: Tuna Can | procedural modeling and rig with KineFX
source: YouTube
url: https://www.youtube.com/watch?v=hHLH7pr_eZo
author: cgside
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["kinefx", "procedural-modeling", "rigging", "sop", "sweep", "quadremesh", "animation", "modeling"]
extraction_status: complete
frames_dir: tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/
frame_count: 4
---

# Tuna Can | procedural modeling and rig with KineFX

**Source:** [YouTube](https://www.youtube.com/watch?v=hHLH7pr_eZo)
**Author:** cgside
**Duration:** 13m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello everyone and welcome back. So, in this video I wanted to show you how I model this tuna can and also how I did the rigging. So, it's a simple exercise, but it might have some challenges. So, let's have a look on how we did this or how I did this. So, as you can see this is the setup. And it all starts from a simple line that I placed at the at the center of the Z axis. Then I did this sweep to create the cap. I think it's called cap. And basically what I did in here is set it to ribbon and columns and the end caps to grid and I played a bit with the end cap roundness and I also applied some scale. So, we get this shape. So, from a line we get this shape. Then I'm going to resample and [clears throat] apply some subdivision. So, I not very high resample. Then I fuse and apply some smoothing to round it a bit off. Then I'm going to select the section in here, so I can add and create the cap design. And in here I'm just using a small expression, so I can iterate over the points and select the section I want. So, then I'm doing a poly expand to create some geometry. These are my settings. I use offset surfaces, reverse, and I use the Houdini's quad rem...

**Frame:** tutorials\frames\tuna-can-procedural-modeling-and-rig-with-kinefx\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedural modeling of a tuna can from a simple line using Sweep, Resample, Fuse, PolyExpand, and QuadRemesh SOPs, then rigging the result with KineFX for animation — demonstrating a clean procedural hard-surface workflow.

### Summary
cgside presents a 13-minute practical tutorial on procedurally modeling a tuna can and rigging it with KineFX in Houdini. The modeling starts from a single line placed at the Z axis center, swept into the cap shape with ribbon mode, then resampled, fused, and smoothed. Point selection expressions iterate over points to create the cap design geometry via PolyExpand, followed by QuadRemesh for clean topology. The same author (cgside) then applies KineFX rigging for animation control, demonstrating a complete SOP modeling-to-rig pipeline for a hard-surface prop.

### Key Steps
1. Create a Line SOP at the center of the Z axis as the profile curve
2. Apply Sweep SOP set to ribbon mode with columns and grid end caps; adjust end cap roundness and scale
3. Resample the swept result for consistent point distribution
4. Apply Subdivide SOP for smoothing
5. Fuse SOP to clean up coincident points
6. Write a point selection expression to iteratively select sections for the cap design
7. Use PolyExpand SOP (offset surfaces, reverse) to create cap detail geometry
8. Apply QuadRemesh SOP for clean, animatable quad topology
9. Set up KineFX skeleton for the tuna can rigging
10. Attach controls and test the rig deformation

### Houdini Nodes / VEX / Settings
- Line SOP
- Sweep SOP (ribbon mode, end cap: grid, end cap roundness)
- Resample SOP
- Subdivide SOP
- Fuse SOP
- Group Expression SOP (point selection)
- PolyExpand SOP (offset surfaces, reverse)
- QuadRemesh SOP
- KineFX skeleton tools
- Rig Doctor SOP

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
kinefx, procedural-modeling, rigging, sop, sweep, quadremesh, animation, modeling

---

## Related Tutorials
- [Mechanical rigging in Houdini - Attaching custom controls](mechanical-rigging-in-houdini---attaching-custom-controls.md) — by same author (cgside); direct continuation showing how to attach KineFX controls to a rig
- [Character Design and Modeling](character-design-and-modeling.md) — character modeling pipeline using VDB and Boolean alongside polygon techniques
- [Procedural HDAs for Unreal](procedural-hdas-for-unreal.md) — procedural modeling-to-HDA pipeline for production use, complementary workflow
