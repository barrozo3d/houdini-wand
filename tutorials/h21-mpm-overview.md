---
title: H21 MPM Overview
source: YouTube
url: https://www.youtube.com/watch?v=nD183jP3H4Y
author: Houdini
ingested: 2026-07-20
houdini_version: "H21"
tags: [dop, simulation, volumes, advanced, houdini-21]
extraction_status: complete
frames_dir: tutorials/frames/h21-mpm-overview/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# H21 MPM Overview

**Source:** [YouTube](https://www.youtube.com/watch?v=nD183jP3H4Y)
**Author:** Houdini
**Duration:** 3m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:35] tutorials/frames/h21-mpm-overview/frame_000.jpg
- [1:25] tutorials/frames/h21-mpm-overview/frame_001.jpg
- [2:10] tutorials/frames/h21-mpm-overview/frame_002.jpg
- [3:00] tutorials/frames/h21-mpm-overview/frame_003.jpg

---

## Structured Notes

### Core Technique
Outline/trailer episode for the official SideFX "MPM H21 Masterclass" series — introduces the new MPM features and post-simulation nodes added in Houdini 21 as a follow-up to the H20.5 MPM Masterclass, without hands-on building (that happens in the other episodes of the same masterclass series).

### Summary
3m28s overview by Alexandre Sirois-Vigneux (SideFX, same presenter as the H20.5 masterclass) previewing what's new for MPM in Houdini 21. Explicitly **not** an MPM introduction — assumes the viewer already knows the solver basics from the H20.5 masterclass. Covers, at a high level: new solver features (surface tension, auto-sleep, continuous emission expansion for sourcing material onto existing material to build internal pressure, per-voxel varying friction/stickiness on colliders — replacing the old H20.5 workaround of duplicating colliders per friction value — and greatly improved deforming colliders), four new post-simulation nodes (MPM Surface, MPM Debris Source, MPM Post-Fracture, MPM Deform Pieces) that streamline surfacing, fracture-driven debris emission, and a "bullet-body-dynamics-style" workflow (simulate a stiff material like concrete with MPM, use the final sim state to post-fracture the original asset, then retarget the MPM dynamics onto the fractured asset), and a list of the practical demo scenes covered later in the masterclass series: Paintball Impact, Pumpkin Smash, Car Rain, Wolf Snow, Creature Breach, Train Wreck, and Building Attack.

### Key Steps
1. (Context-setting only, no hands-on steps in this episode.) New H21 MPM solver features to look for on the MPM Source/Solver: surface tension, auto-sleep, continuous emission expansion, per-voxel varying friction and stickiness (collider-level), improved deforming colliders.
2. New post-simulation node pipeline introduced in H21: **MPM Surface** (surfacing/meshing helper) → **MPM Debris Source** (fracture-driven secondary emission) → **MPM Post-Fracture** (fractures the original asset using the final MPM sim state — for stiff materials like concrete) → **MPM Deform Pieces** (retargets MPM dynamics onto the post-fractured asset, replicating a bullet/RBD-style workflow but driven by MPM).
3. Full masterclass series then walks through 7 demo scenes (Paintball Impact, Pumpkin Smash, Car Rain, Wolf Snow, Creature Breach, Train Wreck, Building Attack) applying these new features/nodes — covered in other episodes of the same YouTube playlist, not in this overview video itself.

### Houdini Nodes / VEX / Settings
- **New H21 nodes named on-screen:** MPM Surface, MPM Debris Source, MPM Post-Fracture, MPM Deform Pieces.
- **New H21 solver features named on-screen:** Surface Tension, Auto Sleep, Continuous Emission Expansion, Varying Friction and Stickiness (per-voxel), Improved Deforming Colliders.
- No parameter values or on-screen node-graph building in this episode — purely a scoped preview/outline slide plus demo-reel B-roll (e.g. a train wreck / metal wreckage MPM shot).

### Difficulty
Advanced — targeted at viewers who already completed the H20.5 MPM Masterclass; this episode itself has no hands-on content.

### Houdini Version
Houdini 21 (MPM solver new features/nodes).

### Tags
dop, simulation, volumes, advanced, houdini-21

---

## Related Tutorials
- `tutorials/mpm-h205-masterclass.md` — the prerequisite H20.5 MPM Masterclass this overview explicitly builds on (same presenter, same solver); shares tags: dop, simulation, volumes.
- `tutorials/new-houdini-205-feature-mastering-the-mpm-snow-solver.md` — practical MPM parameter companion; shares tags: dop, simulation, volumes.
