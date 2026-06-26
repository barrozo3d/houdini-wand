---
title: Velocity Forces 2.0: Advanced
source: YouTube
url: https://www.youtube.com/watch?v=EuL8598tnm4
author: Houdini.School
ingested: 2026-06-23
houdini_version: "H19+"
tags: [velocity, volumes, vex, openvdb, simulation, fluid, smoke, optical-flow, vorticals, matrices, quaternions, intermediate-advanced]
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
**Transcript:** I'm David Torno, and I'll be taking you through even more intricacies of making velocity fields in Houdini. Welcome to Velocity Forces 2.0 Advanced. We're going to explore the nuances between Houdini standard volumes and open VDB volumes. I'll show you techniques to eliminate velocity field activation stepping, as well as how the blend and mix multiple velocity fields for greater creative control across all of your simulations. We'll use simulation outputs as velocity field sources, which can be a powerful, easy solution to unique and organic movement. I'll take you step by step through making verticals and how to implement them into your sims. These will include weight turbulence fields and adding sub-details to low-resolution smoke sims. After all of that, we dive into volume optical flow fields, both on 2D planes and 3D surfaces, and see how to use the potential flow node for a 3D surface advection. From the way we will ditch volume-based fields and take a dynamic vex coding approach, which eliminates the volume caching overhead, and we dive into advanced mathematical concepts as well, from matrices and quadrillions to cross-products and vector math. This course is designed to take what you've learned in the first Velocity Forces class and elevate your knowledge even more. So join me on this journey to redefine your mastery of Velocity Forces in Houdini and roll now at Houdini.school.

**Frame:** tutorials\frames\velocity-forces-20-advanced\frame_000.jpg


---

## Structured Notes

### Core Technique
Course trailer only. Advanced velocity field techniques: standard vs OpenVDB volumes, activation stepping elimination, blending multiple fields, simulation-output-as-velocity-source, vorticals, volume optical flow (2D planes + 3D surfaces), potential flow node for 3D surface advection, dynamic VEX approach (bypasses volume caching), advanced math (matrices, quaternions, cross-products, vector math).

### Summary
1m24s course trailer for "Velocity Forces 2.0: Advanced" by David Torno at Houdini.School. Sequel to Velocity Forces 1. Covers: nuances between standard Houdini volumes and OpenVDB, techniques to eliminate velocity field activation stepping, blending/mixing multiple velocity fields, using simulation outputs as velocity sources for organic movement, creating vorticals (weighted turbulence fields + sub-detail on low-res smoke), volume optical flow on 2D planes and 3D surfaces, potential flow node for surface advection, pure VEX dynamic approach (eliminates volume caching overhead), advanced math: matrices, quaternions, cross-products, vector math.

### Key Steps
*(Trailer only — no step-by-step content; enroll at houdini.school for full course)*

Key topic areas previewed:
1. Standard Houdini volumes vs OpenVDB — differences in velocity field behavior
2. Activation stepping elimination — smoothing velocity field on/off transitions
3. Blending and mixing multiple velocity fields for layered creative control
4. Simulation outputs as velocity sources (e.g. fluid sim driving smoke motion)
5. Vorticals — weighted turbulence fields + sub-detail pass for low-res smoke sims
6. Volume optical flow fields on 2D planes and 3D surfaces
7. Potential flow node — 3D surface advection
8. Dynamic VEX approach — velocity via code instead of volumes (no caching overhead)
9. Advanced math: matrices, quaternions, cross-products, vector math in VEX context

### Houdini Nodes / VEX / Settings
- Standard Houdini volumes vs OpenVDB (velocity field context)
- Potential Flow SOP/node — 3D surface advection
- Volume optical flow — 2D plane and 3D surface variants
- VEX dynamic velocity approach (no volume intermediate)
- Matrices, quaternions, cross-products in VEX (advanced)

### Difficulty
Intermediate–Advanced

### Houdini Version
H19+

### Tags
[velocity, volumes, vex, openvdb, simulation, fluid, smoke, optical-flow, vorticals, matrices, quaternions, intermediate-advanced]

---

## Related Tutorials
- w02-05-deforming-with-velocity-v1-1080p.md (velocity deforming geo)
- w03-04-adding-viscosity-v1-1080p.md (fluid velocity)
- mops-motion-operators-for-houdini-part-3.md (vector math, matrices, quaternions in VEX)
