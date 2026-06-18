---
title: Velocity Forces 2.0: Advanced
source: YouTube
url: https://www.youtube.com/watch?v=EuL8598tnm4
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["velocity", "vdb", "volumes", "vex", "optical-flow", "surface-advection", "turbulence", "simulation", "math", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/velocity-forces-20-advanced/
frame_count: 4
---

# Velocity Forces 2.0: Advanced

**Source:** [YouTube](https://www.youtube.com/watch?v=EuL8598tnm4)
**Author:** Houdini.School
**Duration:** 1m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en I'm David too and I'll be taking you through even more intricacies of making velocity fields in Houdini welcome to Velocity forces 2.0 Advanced we're going to explore the nuances between Houdini standard volumes and open VDB volumes I'll show you techniques to eliminate velocity field activation stepping as well as how to blend and mix multiple velocity fields for greater creative control across all of your simulations we'll use simulation outputs as velocity field sources which which can be a powerful easy solution to unique and organic movement I'll take you step by step through making vertical and how to implement them into your Sims these will include weight turbulence fields and adding sub details to low resolution smoke Sims after all of that we dive into volume Optical flow Fields both on 2D planes and 3D surfaces and see how to use the potential flow node for a 3D surface advection along the way we will ditch volume based fields and take a dynamic Vex coating approach which eliminates the volume caching overhead and we dive into advanced mathematical Concepts as well from matrices and qurans to cross products and Vector math this course is design...

**Frame:** tutorials\frames\velocity-forces-20-advanced\frame_000.jpg


---

## Structured Notes

### Core Technique
Advanced velocity field construction in Houdini — covering VDB vs. standard volumes, velocity stepping elimination, multi-field blending, simulation-output-driven velocity, vortex turbulence, optical flow fields (2D and 3D surface), and VEX-coded dynamic velocity without volume caches.

### Summary
David Torno (also teaches Attributes, Loops, Noise) presents the advanced sequel to his Forces course. Velocity Forces 2.0 dives deep into the nuances of Houdini volume types (standard vs. OpenVDB) and their impact on velocity field behavior. Techniques covered include eliminating activation stepping artifacts, blending multiple velocity fields, using simulation outputs as velocity sources, building vortex turbulence and sub-detail fields for low-res smoke, volume optical flow on 2D planes and 3D surfaces, the Potential Flow node for surface advection, and replacing volume-based fields entirely with dynamic VEX code to eliminate caching overhead. Advanced math concepts (matrices, quaternions, cross products) are integrated throughout.

### Key Steps
1. Understand the differences between Houdini native volumes and OpenVDB volumes for velocity
2. Diagnose and eliminate velocity field activation stepping artifacts
3. Blend and mix multiple velocity fields for layered creative control
4. Feed simulation outputs (Pyro, FLIP) back as velocity field sources
5. Build vortex turbulence fields for organic swirling motion
6. Add sub-detail noise to low-resolution smoke simulations via velocity
7. Implement volume optical flow on 2D planes for image-driven velocity
8. Extend optical flow to 3D surfaces using the Potential Flow node for surface advection
9. Rewrite volume-based velocity setup in pure VEX to eliminate caching overhead
10. Apply matrices, quaternions, and cross products to advanced VEX velocity coding

### Houdini Nodes / VEX / Settings
- VDB Volume SOP
- Volume Mix SOP
- Potential Flow SOP
- Volume Optical Flow SOP
- Volume Wrangle (VEX velocity fields)
- POP Advect by Volumes
- Pyro Solver (velocity source)
- VEX: cross(), dot(), normalize()
- VEX: quaternion(), qrotate()
- VEX: matrix3 operations
- Attribute Wrangle (VEX-coded velocity)

### Difficulty
Advanced

### Houdini Version
unspecified

### Tags
velocity, vdb, volumes, vex, optical-flow, surface-advection, turbulence, simulation, math, advanced

---

## Related Tutorials
- [Forces: Building Custom Velocity Setups](forces-building-custom-velocity-setups.md) — foundational prerequisite course by same author; covers velocity field basics
- [Surface Advection](surface-advection.md) — surface-constrained particle advection; the Potential Flow node is a bridge between these two courses
- [Maths for Artists](maths-for-artists.md) — the mathematical foundation (quaternions, matrices, cross products) used extensively in this advanced course
