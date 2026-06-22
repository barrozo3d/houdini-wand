---
title: w03   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=yP83h4H-lgU
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [flip, simulation, dop, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/w03-01-introduction-v1-1080p/
frame_count: 4
---

# w03   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=yP83h4H-lgU)
**Author:** The VFX School Archive
**Duration:** 1m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello and welcome to week three of the tabletop course. This week is all about viscosity. So we will be emitting three different types of fluid. So we've got like chocolates and and caramel and they'll all have different viscosity attributes and mixing together and falling onto the onto the ice cream. It's the first week so that we are diving into the flip solver and actually simulating a fluid. In week one we simulated with RBDs with bullets. Week two we kind of faked the simulation. But this week we are doing a fully simulated fluid. And viscosity is a really fun thing to play with in in Houdini. We get some really nice sticky thick viscous effects with it. And again yeah we'll be bringing that right through to lighting, shading and rendering. And we'll get a really nice result at the end of this.

**Frame:** tutorials\frames\w03-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-three overview of the Tabletop course: simulating multiple thick, viscous fluid streams (chocolate, caramel and similar sauces) pouring onto ice cream using the FLIP solver with per-fluid viscosity attributes.

### Summary
This is the course's first full FLIP simulation week. Three different fluid emitters each carry a different viscosity attribute value to mimic distinct food fluids (e.g. runny caramel vs. thick chocolate). The FLIP solver's viscosity features are central to achieving sticky, slow-flowing behaviour. The week takes the sim all the way through to Mantra/Arnold lighting, shading and rendering.

### Key Steps
1. [`FLIP Fluid Object`] Create a FLIP fluid object for the first sauce emitter
2. [`Source Volume SOP`] Define per-emitter geometry as the fluid source
3. [`Attribute Wrangle`] Set `viscosity` attribute per emitter point to differentiate fluid types
4. [`FLIP Solver` > Viscosity] Enable viscosity solving in the FLIP solver
5. [`FLIP Object` > Physical] Set viscosity value per fluid object (e.g. 100-5000 range)
6. [Collision geometry] Set up ice cream bowl/surface as a static collision object
7. [Meshing] Convert FLIP particles to a mesh via VDB for rendering
8. [Shading + Render] Apply Principled Shader per fluid; light and render

### Houdini Nodes / VEX / Settings
- `FLIP Fluid Object` — DOP node defining a FLIP particle fluid; Physical tab contains viscosity parameter
- `FLIP Solver` — Viscosity tab must have "Enable Viscosity" checked for viscous behaviour
- `viscosity` attribute — per-point float that can override the global viscosity value when imported
- `Source Volume SOP` — converts SOP geometry into a velocity/density source for the FLIP object

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Adding Viscosity to FLIP](w03-04-adding-viscosity-v1-1080p.md) — detailed hands-on step for viscosity configuration
- [Meshing (VDB Layer Separation)](w03-11-meshing-v1-1080p.md) — the meshing step introduced this week
- [Small Scale Fluids](small-scale-fluids.md) — parallel FLIP small-scale reference
