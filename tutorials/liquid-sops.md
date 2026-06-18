---
title: Liquid SOPs
source: YouTube
url: https://www.youtube.com/watch?v=YKnqahKFNuY
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["sop", "liquid", "procedural-animation", "vex", "vop", "noise", "curves", "non-simulation", "motion-graphics"]
extraction_status: complete
frames_dir: tutorials/frames/liquid-sops/
frame_count: 4
---

# Liquid SOPs

**Source:** [YouTube](https://www.youtube.com/watch?v=YKnqahKFNuY)
**Author:** Houdini.School
**Duration:** 0m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Liquid Sops is a new class focusing on building art-directorable liquid effects without actually using any simulation solvers. The goal is to generate the look and movement of liquid, but without the overhead and complexity of actual simulation calculations. So this means no flip particle simulations, no volume-ed-vection, not even vellum will be used in this class. It's good old-fashioned ingenuity, procedural animation, noises, curves, vops, and of course some vex to make it all work together. This class should get you to think about the mechanics of liquids, which will allow you to think differently and breaking down that information into simpler ways that can be built with just geometry. To learn more, head over to hoodyne.school.

**Frame:** tutorials\frames\liquid-sops\frame_000.jpg


---

## Structured Notes

### Core Technique
Creating convincing liquid-like effects entirely within SOPs using procedural animation, noise, curves, VOPs, and VEX — with no simulation solvers (no FLIP, no volume advection, no Vellum) to achieve maximum art direction and performance.

### Summary
This Houdini.School course presents a solver-free approach to liquid effects, emphasizing art direction and procedural control over physical accuracy. The course teaches artists to think about the mechanics of liquid motion and decompose that understanding into geometry-only setups using noises, curves, VOPs, and VEX. By eliminating FLIP, volume advection, and Vellum entirely, the workflow is fast to iterate, fully art-directable, and suitable for motion graphics contexts where simulation overhead is impractical. Students leave with a fundamentally different way of thinking about liquid effects.

### Key Steps
1. Analyze the visual characteristics of liquid motion (surface tension, flow, pooling)
2. Break down liquid behavior into geometry deformation patterns
3. Use noise-driven displacement to simulate liquid surface rippling and undulation
4. Build curve-based flow paths to guide liquid movement directionally
5. Use VOPs to combine noise layers for complex, natural-looking liquid surfaces
6. Write VEX to add per-point liquid behavior and attribute-driven animation
7. Animate the procedural parameters to create convincing liquid motion over time
8. Refine the look for rendering without relying on any simulation cache

### Houdini Nodes / VEX / Settings
- Attribute Wrangle (VEX)
- VOP SOP (procedural noise network)
- Mountain SOP
- Noise types (Perlin, Worley, Alligator)
- Resample SOP
- Curve SOP
- PolyLoft / PolyFrame
- Carve SOP
- VEX: noise(), curlnoise(), smooth()

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
sop, liquid, procedural-animation, vex, vop, noise, curves, non-simulation, motion-graphics

---

## Related Tutorials
- [Small Scale Fluids](small-scale-fluids.md) — simulation-based counterpart using FLIP for small-scale liquid effects
- [Surface Advection](surface-advection.md) — organic flowing motion on surfaces using volume advection
- [Noise](noise.md) — deep dive into noise types and techniques used extensively in Liquid SOPs
