---
title: week 03   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=OnBsOG4SwIU
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [rbd, simulation, dop, instancing, attributes, beginner]
extraction_status: complete
frames_dir: tutorials/frames/week-03-01-intro-v1-1080p/
frame_count: 4
---

# week 03   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=OnBsOG4SwIU)
**Author:** The VFX School Archive
**Duration:** 1m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, welcome to uh week three. Um in this week we're looking at the cars. We'll be simulating the cars using bullet and we'll start out by importing um the geometry. We're bringing in um a variation of different um vehicles and then we'll be grouping them into separate separating them into wheels and and bodies because we're we'll be doing some simple kind of um suspension. Uh we'll be setting up some points so that we can scatter these onto the road and they've got to be you know pointing in the right direction but with a bit of variation. So I'll be using the scatter align and the attribute from pieces stops. They're new um stops which are introduced in Houdini 18.5. Um and then we'll be looking at a procedural system of removing the intersecting cars. Then we'll do a quick little simple um simulation um to kind of move the cars around a little bit uh so that the first frame of the next simulation is a bit more interesting. So they're kind of pressed up against each other and they slide around a bit. Um I'll be using um soft constraints and cone twist cone twist constraints to set up this uh simulation uh the suspension simulation for the cars as well...

**Frame:** tutorials\frames\week-03-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-three overview: procedurally scattering and simulating a fleet of cars on the bridge road surface using Bullet RBD, including cone-twist suspension constraints and a procedural intersection-removal system.

### Summary
The instructor explains how to import varied vehicle geometry, separate bodies from wheels, and scatter them across the road using new Houdini 18.5 SOPs (Scatter and Align, Attribute from Pieces). A procedural system removes intersecting cars before a lightweight pre-simulation settles them against each other. The main sim then uses soft constraints and cone-twist constraints to fake vehicle suspension behaviour during the destruction event.

### Key Steps
1. [`File SOP`] Import a variety of vehicle models
2. [`Group SOP`] Separate wheel geometry from body geometry per vehicle
3. [`Scatter and Align SOP`] Place vehicles on the road surface with directional variation (Houdini 18.5)
4. [`Attribute from Pieces SOP`] Transfer per-piece attributes to scattered instances (Houdini 18.5)
5. [`VEX Wrangle`] Procedurally detect and remove intersecting cars
6. [`RBD Solver`] Run a quick pre-sim to settle/slide cars before the main destruction
7. [`Constraint Network`] Apply cone-twist constraints for wheel suspension behaviour
8. [`RBD Solver`] Run the full main destruction simulation with the cars included

### Houdini Nodes / VEX / Settings
- `Scatter and Align SOP` (H18.5) — scatters points on a surface and aligns them to the surface normal with variation
- `Attribute from Pieces SOP` (H18.5) — copies per-piece attributes onto scattered instances
- Cone Twist Constraints — allow constrained rotation within a cone angle, ideal for wheel pivots
- Soft Constraints — used alongside cone-twist to provide suspension spring-like behaviour

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Bridge Destruction course)

---

## Related Tutorials
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — RBD/Bullet fundamentals that underpin the car sim
- [Module I Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — active attribute usage relevant to staged activation of cars
- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — the road fracture sim the cars ride on
