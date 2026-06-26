---
title: week 03   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=OnBsOG4SwIU
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5+"
tags: [rbd, bullet, cars, scatter, scatter-align, attribute-from-pieces, constraints, suspension, bridge, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-03-01-intro-v1-1080p/
frame_count: 4
---

# week 03   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=OnBsOG4SwIU)
**Author:** The VFX School Archive
**Duration:** 1m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, welcome to week three. In this week we're looking at the cars, we'll be simulating the cars using bullet. We'll start out by importing the geometry, we're bringing in a variation of different vehicles and then we'll be grouping them into separating them into wheels and bodies because we'll be doing some simple kind of suspension. We'll be setting up some points so that we can scatter these onto the road and they've got to be pointing in the right direction but with a bit of variation. So I'll be using the scatter align and the attribute from pieces, sops, the new sops which are introduced in Houdini 18.5 and then we'll be looking at a procedural system of removing the intersecting cars. Then we'll do a quick little simple simulation to kind of move the cars around a little bit so that the first frame of the next simulation is a bit more interesting so they're kind of pressed up against each other and they slide around a bit. I'll be using soft constraints and twist, contus constraints to set up this simulation, the suspension simulation for the cars as well.

**Frame:** tutorials\frames\week-03-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only. Week 3 of Manhattan Bridge Destruction: cars simulated with Bullet; groups for wheels/bodies (suspension); Scatter Align + Attribute From Pieces (H18.5) to place cars on road with correct direction + variation; procedural intersection-removal; soft + twist constraints for suspension sim.

### Summary
1m22s week intro by VFX School Archive. Week 3 of Manhattan Bridge Destruction: vehicle simulation. Topics previewed: import multiple vehicle variations; group into wheels vs bodies for suspension simulation; Scatter Align SOP (H18.5) to place cars on road pointing in correct direction with variation; Attribute From Pieces SOP (H18.5) for attribute propagation; procedural system for removing intersecting cars; quick initial sim to settle cars against each other (initial state for main sim); soft constraints + twist/angular constraints for wheel/body suspension behavior.

### Key Steps
*(Week introduction — see other week-03-xx lessons for specifics)*

Week 3 pipeline:
1. Import vehicle variations → group wheels and bodies
2. Scatter Align SOP (H18.5) — place cars on road with correct orientation + variation
3. Attribute From Pieces SOP (H18.5) — propagate attributes across vehicle pieces
4. Procedural intersection removal system
5. Quick pre-sim to settle/press cars against each other
6. Soft constraints + twist (angular) constraints → suspension behavior

### Houdini Nodes / VEX / Settings
- **Scatter Align SOP** (H18.5) — scatter with alignment direction + variation
- **Attribute From Pieces SOP** (H18.5) — attribute propagation from pieces
- Bullet solver for vehicle simulation
- Soft constraints + twist/angular constraints for suspension
- Groups: wheels vs bodies (separate constraint types)

### Difficulty
Intermediate

### Houdini Version
H18.5+

### Tags
[rbd, bullet, cars, scatter, scatter-align, attribute-from-pieces, constraints, suspension, bridge, intermediate]

---

## Related Tutorials
- week-01-01-intro-v1-1080p.md (week 1: bridge destruction overview)
- week-02-01-intro-v1-1080p.md (week 2: cables Bullet+Vellum)
- week-04-06-cull-by-speed-v1-1080p.md (week 4: rain particles on bridge)
