---
title: Forces: Building Custom Velocity Setups
source: YouTube
url: https://www.youtube.com/watch?v=v1psrXhj9IY
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["velocity", "forces", "simulation", "vex", "volumes", "vector-fields", "pop", "procedural"]
extraction_status: complete
frames_dir: tutorials/frames/forces-building-custom-velocity-setups/
frame_count: 4
---

# Forces: Building Custom Velocity Setups

**Source:** [YouTube](https://www.youtube.com/watch?v=v1psrXhj9IY)
**Author:** Houdini.School
**Duration:** 0m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** I've split this class in the two sessions. First, we will focus on the breakdowns of what a vector, a force, velocity, and velocity fields mean in the context of Houdini building upon each breakdown. You will end up with a collection of possible approaches to choose from when building your own setups. This progressive approach will guide you through each build and reveal different ways to control the forces. All simulations involved manipulating data in various ways. Understanding how to influence that data, to create the movement you want, will get you that much closer to meeting your client's needs.

**Frame:** tutorials\frames\forces-building-custom-velocity-setups\frame_000.jpg


---

## Structured Notes

### Core Technique
Building custom velocity fields and forces in Houdini from first principles — understanding vectors, forces, and velocity fields conceptually before constructing a library of reusable force approaches for simulations.

### Summary
This Houdini.School course takes a progressive, two-session approach to custom velocity setups. Session 1 breaks down the fundamental concepts: what vectors, forces, velocity, and velocity fields actually mean in Houdini's context. Session 2 builds a collection of practical force setups using those concepts. The course is structured as a toolkit — students end up with multiple approaches they can choose from when building their own simulations. The underlying philosophy is that all simulations are data manipulation, and understanding how to influence that data is the core skill.

### Key Steps
1. Learn what a vector means in Houdini — direction and magnitude in 3D space
2. Understand the difference between force and velocity in simulation contexts
3. Define velocity fields — volume-based and point-based approaches
4. Build approach #1: simple uniform velocity field using a volume
5. Build approach #2: VEX-based procedural velocity field without volumes
6. Build approach #3: geometry-driven velocity using surface normals or gradients
7. Build approach #4: combining multiple velocity fields with blend/weight controls
8. Apply each approach to a POP or DOP simulation and compare results

### Houdini Nodes / VEX / Settings
- Volume VOP (velocity field setup)
- Attribute Wrangle (VEX velocity)
- POP VOP / POP Wrangle
- DOP Force nodes
- Pyro / FLIP velocity inputs
- Vector math in VEX (normalize, length, dot, cross)
- Volume Sample VEX function

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
velocity, forces, simulation, vex, volumes, vector-fields, pop, procedural

---

## Related Tutorials
- [Velocity Forces 2.0: Advanced](velocity-forces-20-advanced.md) — advanced continuation covering VDB volumes, optical flow, and VEX-based velocity approaches
- [Surface Advection](surface-advection.md) — surface-constrained advection using velocity fields on geometry
- [Maths for Artists](maths-for-artists.md) — mathematical foundation for vectors, matrices, and vector fields used in velocity setups
