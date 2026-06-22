---
title: 53 recreating our solver with pops v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9objvx69_58
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [dop, sop, particles, simulation, intermediate]
extraction_status: complete
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
Rebuilding the hand-crafted SOP Solver particle system with a proper POP Network, demonstrating the 1:1 correspondence between manual SOP-level particle logic and the dedicated POP toolset.

### Summary
Creates a POP Network and feeds the surface geometry directly into its first input (no need to pre-scatter). Inside the network: a POP Solver handles all integration automatically, a POP Object stores all simulation state (the DOP-level container analogous to the manual attribute storage used previously), and a POP Source emits particles with surface emission and a constant birth rate matching the prior 100/frame. POP Wind adds directional force and POP Gravity adds downward acceleration. The lesson confirms both setups produce identical motion, validating that POPs are exactly the manual SOP Solver technique wrapped in a more convenient, optimized interface.

### Key Steps
1. [`POP Network`] Create a popnet fed directly by the surface geometry
2. [`POP Source`] Set emission type to surface with a constant birth rate of 100/frame
3. [`POP Solver`] Let the solver handle position/velocity integration automatically
4. [`POP Object`] Confirm this is the DOP-level state container equivalent to the earlier manual attributes
5. [`POP Wind`] Add directional force
6. [`POP Gravity`] Add downward acceleration
7. [Verify] Compare resulting motion against the manual SOP Solver version from lesson 52

### Houdini Nodes / VEX / Settings
- `POP Network` (popnet) — container DOP network for particle simulation
- `POP Source` — emits particles from geometry; birth rate and emission type configurable
- `POP Solver` — automatic position/velocity integrator, replacing the manual wrangle logic
- `POP Object` — DOP data container analogous to manually managed point attributes
- `POP Wind`, `POP Gravity` — standard force microsolvers

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)

---

## Related Tutorials
- [Creating a Simplified Particle System](52-creating-a-simplified-particle-system-v1-1080p.md) — the manual SOP Solver version this recreates with POPs
- [Introducing the SOP Solver](51-introducing-the-sop-solver-v1-1080p.md) — the original from-scratch particle integration lesson
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — later course applying POPs to a production shot
