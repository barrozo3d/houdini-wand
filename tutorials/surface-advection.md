---
title: Surface Advection
source: YouTube
url: https://www.youtube.com/watch?v=w_NnhoKeLlE
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["advection", "particles", "volumes", "surface", "sop", "dop", "redshift", "rendering", "simulation", "organic"]
extraction_status: complete
frames_dir: tutorials/frames/surface-advection/
frame_count: 4
---

# Surface Advection

**Source:** [YouTube](https://www.youtube.com/watch?v=w_NnhoKeLlE)
**Author:** Houdini.School
**Duration:** 1m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Surface advection is a new class focused on generating organic flowing movement along the surface of your geometry. In the first session, I will go over a couple different advection setups, one involving adopts volume simulation, and another using a non-simulated BOPS solution. In session two, I'll show you how to take what we've already learned and explain how we can adjust that method for a more complex surface. The time around, simulating particles to drive our flow, plus animating volume sources, and of course, I'll share tips along the way. After taking this class, you should have a better understanding of extracting volume data onto particles, simulating particles along geometry surfaces, creating unique advection input data, as well as handling redshift 3D proxy exports and rendering geometry instances. Surface advection will be coming late September 2021 to Houdini.school, so don't miss out and make sure to sign up today.

**Frame:** tutorials\frames\surface-advection\frame_000.jpg


---

## Structured Notes

### Core Technique
Generating organic flowing movement along geometry surfaces using two approaches: a DOP volume simulation-driven advection setup and a non-simulated SOP-only solution — plus particle simulation for complex surfaces.

### Summary
This Houdini.School course focuses exclusively on surface advection — constraining particle flow to move along geometry surfaces rather than through free space. Two approaches are taught: Session 1 introduces a DOP-based volume simulation approach and a faster non-simulated SOP solution. Session 2 applies these techniques to more complex geometry using simulated particles and animated volume sources for the advection input. The course also covers practical production topics: extracting volume data onto particles, Redshift 3D proxy exports, and rendering geometry instances. The style is methodical and tips-focused.

### Key Steps
1. Understand surface advection conceptually — constraining velocity to flow along a surface
2. Set up the DOP-based approach: create a volume velocity field constrained to the surface
3. Use the volume to advect particles that stay on the surface in simulation
4. Build the non-simulated SOP alternative for fast, cache-free surface flow
5. Extend both methods to complex surfaces in Session 2
6. Simulate particles explicitly along the surface using particle POP network
7. Animate volume sources to create evolving, non-uniform surface flow
8. Extract volume data onto particles for attribute-driven rendering
9. Set up Redshift 3D proxy exports for instanced particle renders
10. Render instanced geometry along the advected particle trails

### Houdini Nodes / VEX / Settings
- POP network (particle simulation)
- POP Advect by Volumes
- Volume Advect SOP (non-simulated)
- Volume Sample / Volume Gradient VEX
- DOP network
- Particle Fluid Surface SOP
- Volume Source DOP (animated)
- Redshift Proxy (RSProxy) SOP
- Instance / Copy to Points SOP

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
advection, particles, volumes, surface, sop, dop, redshift, rendering, simulation, organic

---

## Related Tutorials
- [Velocity Forces 2.0: Advanced](velocity-forces-20-advanced.md) — covers potential flow and volume optical flow on 3D surfaces, complementary to surface advection
- [Forces: Building Custom Velocity Setups](forces-building-custom-velocity-setups.md) — building the velocity fields that drive advection
- [Liquid SOPs](liquid-sops.md) — non-simulated surface flow without particles; shares the art-directed philosophy
