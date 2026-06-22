---
title: module i   week 04   01   introduction to particles v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9S5YABmK_eU
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [dop, sop, particles, simulation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-04-01-introduction-to-particles-v1-1080p/
frame_count: 4
---

# module i   week 04   01   introduction to particles v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9S5YABmK_eU)
**Author:** The VFX School Archive
**Duration:** 13m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay. So, week four, we're looking at um particles. So, um let's create a new project quickly. So, I'm going to call this uh module one. Uh what are we for? Okay. Um oops. Into d accept and then save as. save as into job. And let's call this um particles version one. Accept. Great. Okay. And I'm just going to delete these. There we go. Fantastic. Okay. So, particles. Let's start by creating a geometry node as per usual. And let's call this particles intro. dive in there and create a geometry. Let's create a test geometry pig head. Press P on my keyboard to get the parameters and I don't want the shader and we'll leave it on the medium difficulty. That's fine. So, um yeah, the wording can be a bit confusing if you're new to Houdini. You know, what are particles and what are points and what's the difference? So basically particles are um how we refer to points or particles within a simulation. So you can see here on the particles shelf particle particle they're all related to particles. And when we're in um outside of the do um which is dynamic operators context they'll be referred to as points. And you know um you can work on the geometry in the same way....

**Frame:** tutorials\frames\module-i-week-04-01-introduction-to-particles-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Introducing particles in the context of the Renascence program, clarifying SOP "points" vs. DOP "particles" terminology, and building a POP Network sourced from a pig-head test mesh.

### Summary
Clarifies that in SOPs these entities are called "points," while inside a DOP simulation the same entities are called "particles" — both inspected via the Geometry Spreadsheet. Sets up a POP Network sourcing from a medium-resolution pig-head test geometry, using POP Source (surface emission), POP Gravity, POP Drag and POP Color. Demonstrates key particle attributes: `@age`, `@life`, `@dead` (set to 1 to kill a particle), and `@pscale` (per-particle render size). Introduces the shelf-based POP workflow as an alternative to building manually inside a popnet, and connects forward to instancing: after simulation, Copy to Points replaces particle points with geometry instances for rendering.

### Key Steps
1. [Terminology] Distinguish SOP "points" from DOP "particles" — same data, different context
2. [`POP Network`] Source particles from the pig-head test geometry (surface emission)
3. [`POP Source`, `POP Gravity`, `POP Drag`, `POP Color`] Assemble the basic force/appearance chain
4. [Attributes] Use `@age`, `@life`, `@dead` and `@pscale` to control lifespan and per-particle size
5. [Shelf tools] Note the shelf-based POP workflow as a faster alternative to manual popnet building
6. [`Copy to Points`] Replace simulated particle points with render geometry after simulation

### Houdini Nodes / VEX / Settings
- `POP Source` — surface emission from the pig-head test geometry
- `POP Gravity`, `POP Drag` — standard force microsolvers
- `POP Color` — sets particle colour attribute for visualization
- `@dead` attribute — setting to 1 marks a particle for removal
- `Copy to Points SOP` — post-sim instancing step converting particle points into renderable geometry

### Difficulty
Beginner

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)

---

## Related Tutorials
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — the preceding week's volume work
- [Recreating Our Solver With POPs](53-recreating-our-solver-with-pops-v1-1080p.md) — the Film FX season's foundational POP lesson this builds on
- [Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — the following week's FLIP setup
