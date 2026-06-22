---
title: week 01   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9ocqYW1XHk4
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rbd, simulation, dop, procedural, beginner]
extraction_status: complete
frames_dir: tutorials/frames/week-01-01-intro-v1-1080p/
frame_count: 4
---

# week 01   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9ocqYW1XHk4)
**Author:** The VFX School Archive
**Duration:** 1m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello and welcome to week one of the Manhattan Bridge destruction project. Um so we're going to start out this week by importing our um lovely model. We'll analyze it and look at you know what's uh what we need to do to prepare it for the simulation. We'll split it into a part that we'll simulate and a part that will just be static. Um then we'll further organize it so into parts of um parts which will be deformable metal, rigid metal and then the road which we will fracture. Um we'll clean and prepare with everything ready for the simulation. Again we'll be fracturing the road with um boline with a boline method using you know we we'll create cutting geometry and then we'll fracture the deformable metal with the veronoi method. We will be um configuring plastic uh sorry soft constraints and configuring plasticity with that for the for the metal obviously and and for just generally holding everything together. Um we'll be animating the bridge so so that it kind of looks like it's in an earthquake or in a um you know in windy conditions. So it's kind of swaying back and forwards. And this animation will be in the simulation itself. Um, and then we'll be p...

**Frame:** tutorials\frames\week-01-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-one overview of the Manhattan Bridge Destruction course: importing, organising and preparing bridge geometry for a multi-body RBD simulation including Voronoi fracture of the road and Boolean fracture of the deformable metal.

### Summary
The instructor outlines what week one covers: importing the bridge model, splitting it into simulated vs. static parts, and further categorising those parts into deformable metal, rigid metal and road geometry. The road is fractured with a Boolean (cutting geometry) method while the metal uses Voronoi. Soft constraints with plasticity are configured to give the metal realistic bending behaviour, and the bridge itself is animated to sway as if in wind, driving the simulation.

### Key Steps
1. [`File SOP`] Import the bridge model and inspect geometry
2. [`Blast SOP`] Separate static vs. simulated sections of the bridge
3. [`Group SOP`] Organise simulated geometry into deformable metal, rigid metal and road groups
4. [`Boolean Fracture`] Fracture the road using cutting geometry (Boolean method)
5. [`Voronoi Fracture SOP`] Fracture the deformable metal elements
6. [`RBD Configure`] Pack and prepare all fractured pieces for the Bullet solver
7. [`Constraint Network`] Set up soft constraints with plasticity for the metal
8. [`Channel CHOP / Keyframes`] Animate the bridge sway to drive the simulation

### Houdini Nodes / VEX / Settings
- `File SOP` — reads the bridge model from disk
- `Blast SOP` — isolates static vs. simulated geometry
- `Group SOP` — tags pieces as deformable metal, rigid metal or road
- `Boolean Fracture` — cuts road geometry with user-defined cutting shapes
- `Voronoi Fracture SOP` — shatters metal into irregular rigid chunks
- `RBD Configure` — packs geo and adds required RBD attributes for Bullet solver
- Soft Constraints + Plasticity — lets metal bend and hold shape under stress

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — shared RBD/Bullet fundamentals
- [RBD Configure Deep Dive](week-01-11-rbd-configure-v1-1080p.md) — detailed look at the RBD Configure node used in this week
- [Module I Intro](module-i-week-01-01-intro-v1-1080p.md) — parallel RBD intro from the earlier course
