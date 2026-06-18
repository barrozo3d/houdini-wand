---
title: Procedural Growth with KineFX and the Labs Tree Tools
source: YouTube
url: https://www.youtube.com/watch?v=j5XxDiG25wQ
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["kinefx", "labs", "tree", "growth", "vex", "chops", "procedural", "wind", "rigging", "vegetation", "animation"]
extraction_status: complete
frames_dir: tutorials/frames/procedural-growth-with-kinefx-and-the-labs-tree-tools/
frame_count: 4
---

# Procedural Growth with KineFX and the Labs Tree Tools

**Source:** [YouTube](https://www.youtube.com/watch?v=j5XxDiG25wQ)
**Author:** Houdini.School
**Duration:** 1m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hello everybody my name is Mark Fancher and I am here with Houdini school to teach you about how to build rig and animate procedural trees using the side effects Labs tree tools there are multiple apps and plugins out there that are dedicated to procedural vegetation generation many of them are not cheap but the side effects Labs tree tools are totally free open and they work directly inside of Houdini with these tools as a starting point we'll extend our setup by rigging and animating our tree using the kinefx tool set inside of Houdini then we'll build a procedural growth and wind system using Vex and chops and if all that wasn't enough in the end we'll be diving into an even more advanced example where I'll show you how you can get under the hood and mod the behavior of the tree tools to make them even more flexible this is an intermediate to Advanced course that assumes students have a basic grasp of Vex and other General Houdini Concepts think of this as a technical exercise was super satisfying results while we're building this beautiful tree animation this is just the setting where we're going to learn a handful of really powerful tricks that can ...

**Frame:** tutorials\frames\procedural-growth-with-kinefx-and-the-labs-tree-tools\frame_000.jpg


---

## Structured Notes

### Core Technique
Building, rigging, and animating procedural trees using the free SideFX Labs Tree Tools combined with KineFX rigging — then adding a procedural growth and wind animation system using VEX and CHOPs, plus modding the Labs tools for greater flexibility.

### Summary
Mark Fancher presents an intermediate-to-advanced Houdini.School course on procedural vegetation using the free, built-in SideFX Labs Tree Tools as the starting geometry, then extending into KineFX rigging and animation. The course covers rigging the tree with KineFX, building a procedural growth sequence and a wind animation system using VEX and CHOPs, and goes deep into modifying the Labs tree tools themselves for more flexible behavior. The course assumes VEX familiarity and is described as a technical exercise with highly satisfying artistic results.

### Key Steps
1. Generate a tree using SideFX Labs Tree Tools and explore the tool parameters
2. Rig the tree structure using KineFX — convert the tree to a KineFX skeleton
3. Set up KineFX constraints and joint hierarchies for the branches
4. Build a procedural growth system in VEX — animate the tree growing from seed over time
5. Build a wind animation system using CHOPs for natural branch oscillation
6. Connect CHOP animation channels back to KineFX skeleton transforms
7. Dive into the Labs Tree Tools internals and mod the HDA for greater flexibility
8. Render the final animated tree with wind and growth effects

### Houdini Nodes / VEX / Settings
- SideFX Labs Tree Generator SOP
- KineFX skeleton tools
- Rig Stash Pose SOP
- Full Body IK (KineFX)
- Attribute Wrangle (VEX growth logic)
- CHOP network (wind oscillation)
- Channel CHOP / Spring CHOP
- Labs Tree Tools HDA (internal modification)
- VEX: chramp(), fit(), smooth()

### Difficulty
Advanced

### Houdini Version
unspecified

### Tags
kinefx, labs, tree, growth, vex, chops, procedural, wind, rigging, vegetation, animation

---

## Related Tutorials
- [Experimental Motion - CHOPS](experimental-motion---chops.md) — CHOPs for smooth organic animation, directly applicable to the wind system in this course
- [Mechanical rigging in Houdini - Attaching custom controls](mechanical-rigging-in-houdini---attaching-custom-controls.md) — KineFX rigging techniques used in mechanical and organic rig setups
- [Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants](yan-paul-dubbelman-procedural-nature-procedural-living-plants.md) — related procedural plant creation from the same natural/botanical domain
