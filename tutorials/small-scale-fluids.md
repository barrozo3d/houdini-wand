---
title: Small Scale Fluids
source: YouTube
url: https://www.youtube.com/watch?v=aKJB3uOKFKM
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["flip", "fluid", "simulation", "small-scale", "meshing", "redshift", "karma", "viscosity", "vdb", "production"]
extraction_status: complete
frames_dir: tutorials/frames/small-scale-fluids/
frame_count: 4
---

# Small Scale Fluids

**Source:** [YouTube](https://www.youtube.com/watch?v=aKJB3uOKFKM)
**Author:** Houdini.School
**Duration:** 1m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to Small Scale Fluids 235. A course that offers a unique approach to creating small scale fluids specifically designed for macro style short sequences in production. In this two session live course, students will delve into various concepts including good self-sustention approaches, custom fluid simulation control and workflow techniques and hacks. Topics include project setups, dos and don'ts, flip settings, emission and variable discosities, basic forces working with collision optics for optimization, meshing advanced use of forces, BDB techniques, fluid bending and look they're using render engines like redshift and karma. You'll leave this course with a better understanding of flips and relations for unique short cases including the advantages and disadvantages inherent in these scenarios. Additionally, you will learn valuable workflow practices utilized by me in my client work. At the end of the course, you'll be ready to apply these new skills to real world projects.

**Frame:** tutorials\frames\small-scale-fluids\frame_000.jpg


---

## Structured Notes

### Core Technique
FLIP fluid simulation for small-scale, macro-photography-style liquid sequences in production — covering custom control, variable viscosities, advanced meshing, and rendering with Redshift and Karma.

### Summary
This Houdini.School course (Small Scale Fluids 235) takes a production-focused approach to small-scale FLIP fluid simulations designed for close-up, macro-style camera sequences. The two-session live course covers project setup, FLIP settings best practices, emission and variable viscosity control, collision geometry optimization, advanced meshing techniques, and VDB-based approaches to shape the fluid look. Rendering is covered with both Redshift and Karma. The instructor shares workflow hacks and lessons from real client work, emphasizing practical production knowledge alongside technical FLIP understanding.

### Key Steps
1. Set up the project correctly — scale, simulation units, frame rate for macro fluid look
2. Configure FLIP solver settings (substeps, particle separation, surface tension)
3. Set up fluid emission with custom emission rates and timing
4. Implement variable viscosity for different fluid behaviors within the same simulation
5. Set up collision geometry and optimize for simulation performance
6. Apply basic forces (gravity, drag, turbulence) and advanced custom forces
7. Use VDB techniques to shape and control fluid behavior mid-simulation
8. Mesh the FLIP particles for a clean fluid surface using Particle Fluid Surface SOP
9. Apply fluid bending and look development tricks for the rendered result
10. Render with Redshift and Karma, comparing workflow differences between the two

### Houdini Nodes / VEX / Settings
- FLIP Solver (DOP)
- Fluid Source SOP
- Particle Fluid Surface SOP (meshing)
- VDB from Particles
- Collision Source SOP
- Viscosity attribute (`@viscosity`)
- Surface Tension parameter (FLIP)
- POP Force / POP Drag
- Redshift renderer
- Karma renderer (LOPs)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
flip, fluid, simulation, small-scale, meshing, redshift, karma, viscosity, vdb, production

---

## Related Tutorials
- [Liquid SOPs](liquid-sops.md) — solver-free alternative approach to liquid effects, useful when FLIP is too heavy
- [History of Houdini Systems](history-of-houdini-systems.md) — historical context on FLIP and hydrodynamics systems in Houdini
- [Forces: Building Custom Velocity Setups](forces-building-custom-velocity-setups.md) — custom velocity/force setups applicable to FLIP fluid control
