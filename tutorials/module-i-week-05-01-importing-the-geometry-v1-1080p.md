---
title: module i   week 05   01   importing the geometry v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Fo3HaNq9f8M
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [sop, flip, dop, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-05-01-importing-the-geometry-v1-1080p/
frame_count: 4
---

# module i   week 05   01   importing the geometry v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=Fo3HaNq9f8M)
**Author:** The VFX School Archive
**Duration:** 2m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, so here I am in a fresh Houdini scene. And I'm going to create a new project. Uh, what am I doing? New project. We are in module uh one and it's week uh five. And this goes into D. There we go. Accept. So, go ahead and find that project and I'm going to drag in the horse Alembic file. So, just leave that in there. And then we'll save it as well. So, save as. And we'll call this um horse pop fluid. Version one. Accept. Okay, and then I'll just show you you can see there we get the hip file and then um So, it's great and then we'll bring in that horse first. Create a geometry file, call this horse. And dive inside, press we want an Alembic. So, press P to get my parameters. Find the horse or hip and then ABC horse. Accept. And there's our lovely horse with the animation. So, we need to at the moment you can see this is kind of like we can't we don't have access to the geometry. So, Stroker convert. First and then we can select polygons. I also want to if we turn on the real time toggle there. I want this to be pretty slow. So, I'm going to use a time shift. And turn off integer frames and I'm going to set this multiply this by point three, so it's re...

**Frame:** tutorials\frames\module-i-week-05-01-importing-the-geometry-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Importing an animated horse Alembic file as the geometry source for the week's POP fluid / FLIP simulation, including a critical PolySoup-to-polygon conversion step and a slow-motion retiming pass.

### Summary
Workflow: File -> New Project, drag the .abc into the project geo folder, create a geometry node, add an Alembic SOP and browse to the file. A critical step is adding a Convert SOP after Alembic to convert from PolySoup to regular polygons — necessary for correct geometry selection and attribute access later. The animation is slowed using a Time Shift SOP: integer frames are disabled and time is multiplied by 0.3 to produce a slow gallop. This establishes the horse as the emission source (surface scatter) for the FLIP fluid that will coat it in the week's simulation.

### Key Steps
1. [New Project] File -> New Project; drag the horse .abc into the project geo folder
2. [`Alembic SOP`] Create a geometry node and browse to the imported .abc file
3. [`Convert SOP`] Convert from PolySoup to regular polygons for correct selection/attribute access
4. [`Time Shift SOP`] Disable integer frames; multiply time by 0.3 to slow the gallop animation
5. [Output] Use the resulting slow-motion horse mesh as the surface-scatter source for the FLIP sim

### Houdini Nodes / VEX / Settings
- `Alembic SOP` — imports the animated .abc horse geometry
- `Convert SOP` — PolySoup-to-polygon conversion, required before most SOP operations work correctly on Alembic imports
- `Time Shift SOP` — retimes animation independent of frame rate; here scaled by 0.3 with integer-frame snapping disabled

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)

---

## Related Tutorials
- [Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — the preceding week's POP fundamentals
- [Introduction to Grains](module-i-week-06-01-introduction-to-grains-v1-1080p.md) — the following week's Vellum grain simulation
- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — a later FLIP-on-animated-geometry setup for comparison
