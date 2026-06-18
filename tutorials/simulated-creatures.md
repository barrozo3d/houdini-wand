---
title: Simulated Creatures
source: YouTube
url: https://www.youtube.com/watch?v=M8HOGm6FxIw
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["fem", "soft-body", "simulation", "vellum", "animation", "keyframe", "constraints", "procedural-animation", "creatures"]
extraction_status: complete
frames_dir: tutorials/frames/simulated-creatures/
frame_count: 4
---

# Simulated Creatures

**Source:** [YouTube](https://www.youtube.com/watch?v=M8HOGm6FxIw)
**Author:** Houdini.School
**Duration:** 0m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, I'm Matt Taylor. I'm an animation director, 3D artist and teacher. Simulated creatures is a course focusing on soft body simulation of animated objects using the FEMS folder in Houdini. We'll combine elements of keyframe animation, procedural animation, and simulated animation all in one object using a variety of FEMM tools and other softs. We'll learn how to prep geometry for simulations, then we'll dive into multiple methods of animating with FEMM, including forces and constraints. We'll add additional motion with animated rest states, target strengths, pin constraints, and HB management, utilizing both keyframes and motion effects procedural animation. Overall, we'll compare FEMM to Vellan and discuss the reasons FEMM might be preferable to create believable, organic, detailed movement.

**Frame:** tutorials\frames\simulated-creatures\frame_000.jpg


---

## Structured Notes

### Core Technique
Soft body simulation of animated creatures using Houdini's FEM (Finite Element Method) solver — combining keyframe animation, procedural animation, and FEM simulation with constraints for believable organic movement.

### Summary
Matt Taylor (animation director, 3D artist, teacher) presents a course focused on using Houdini's FEM solver to create convincingly soft and organic creature movement. The course covers geometry preparation for FEM, multiple animation methods within FEM (forces, constraints, animated rest states, target strengths, pin constraints), and FEM management for efficiency. A key element is the comparison between FEM and Vellum, with clear reasoning for when FEM is the better choice for detailed, believable organic movement. Keyframe animation and procedural animation (motion effects) are both incorporated alongside the FEM simulation.

### Key Steps
1. Prepare geometry for FEM simulation — appropriate polygon density, closed geometry
2. Set up a basic FEM (Solid) simulation in a DOP network
3. Use FEM forces (gravity, external forces) to drive initial motion
4. Set up FEM constraints — pin constraints, target strengths for controlled deformation
5. Animate rest states to guide the creature's target shape over time
6. Combine FEM simulation with keyframed animation (blend between keyframes and sim)
7. Apply procedural animation (motion effects) on top of the FEM result
8. Manage FEM settings for performance — substeps, iterations, resolution
9. Compare FEM vs. Vellum for the same setup and evaluate which is better for organic creatures

### Houdini Nodes / VEX / Settings
- FEM Solver (Solid Object DOP)
- Solid Embed SOP (geometry preparation)
- Solid Fracture SOP
- Pin Constraint DOP
- Target Strength parameter (FEM)
- Animated Rest State (FEM)
- DOP network
- Vellum Solver (comparison)
- Motion Effects (procedural animation on top of sim)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
fem, soft-body, simulation, vellum, animation, keyframe, constraints, procedural-animation, creatures

---

## Related Tutorials
- [Art Directing Cloth in Houdini](art-directing-cloth-in-houdini.md) — Vellum-based soft body simulation; the Vellum counterpart to FEM discussed in this course
- [Character Design and Modeling](character-design-and-modeling.md) — character geometry creation; this course handles the simulation step after modeling
- [Forces: Building Custom Velocity Setups](forces-building-custom-velocity-setups.md) — custom forces applicable to FEM creature simulations
