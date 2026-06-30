---
title: [Урок] Помада. Часть 2. Flip Sim
source: YouTube
url: https://www.youtube.com/watch?v=H17o8w-CFUM
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19+"
tags: [flip-sim, fluid-simulation, viscous, particles, vdb, surface-reconstruction, octane, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/урок-помада-часть-2-flip-sim/
frame_count: 4
---

# [Урок] Помада. Часть 2. Flip Sim

**Source:** [YouTube](https://www.youtube.com/watch?v=H17o8w-CFUM)
**Author:** Alexander Eskin
**Duration:** 34m20s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Frame:** tutorials\frames\урок-помада-часть-2-flip-sim\frame_000.jpg


---

## Structured Notes

### Core Technique
**⚠️ Transcript not captured during ingestion — Russian-language audio, no auto-captions available.** Context-based notes only. FLIP fluid simulation for a lipstick (помада) product shot — Part 2 of a 3-part series (Part 1: modeling in H19; Part 3: rendering in Octane). Typical workflow for viscous/fluid lipstick surface simulation using Houdini's FLIP solver.

### Summary
34m20s tutorial by Alexander Eskin. Part 2 of the lipstick series: takes the modeled lipstick geometry from Part 1 and simulates fluid FLIP dynamics to create realistic liquid-lipstick surface behavior. Transcript was not captured during ingestion (Russian audio without auto-captions). Based on title and series context, expected content: FLIP Object setup, viscosity/surface tension parameters for a thick fluid, running the FLIP simulation, surface mesh extraction (Particle Fluid Surface SOP or VDB-based meshing), and preparation for Octane rendering in Part 3.

### Key Steps
*No transcript available — steps inferred from title and series context (Part 1: Моделирование, Part 3: Рендер).*
1. Import modeled lipstick geometry from Part 1
2. Create FLIP Object from lipstick surface
3. Configure FLIP Solver: viscosity, surface tension, voxel size
4. Add collider geometry (lipstick casing/tube) as Static Object in DOP
5. Run FLIP simulation
6. Extract surface mesh: Particle Fluid Surface SOP or VDB smoothing
7. Prepare exported mesh for Octane material/render in Part 3

### Houdini Nodes / VEX / Settings
*Inferred from topic — not confirmed from transcript.*
- **FLIP Object** — fluid container for the lipstick liquid
- **FLIP Solver** — simulation engine; viscosity attribute for thick fluid behavior; surface tension
- **Static Object** (DOP) — casing/tube geometry as collision boundary
- **Particle Fluid Surface SOP** — mesh extraction from FLIP particles
- **VDB From Particles** — alternative surface reconstruction
- Voxel size (particle separation): smaller = more detail, longer sim
- Reseeding settings for consistent fluid density

### Difficulty
Intermediate

### Houdini Version
H19+

### Tags
[flip-sim, fluid-simulation, viscous, particles, vdb, surface-reconstruction, octane, intermediate]

---

## Related Tutorials
- урок-помада-часть-1-моделирование.md (Part 1: lipstick hard-surface modeling)
- урок-помада-часть-3-рендер.md (Part 3: Octane rendering of the lipstick)
- урок-стеклянный-пончик.md (same author: fluid/procedural effects)
