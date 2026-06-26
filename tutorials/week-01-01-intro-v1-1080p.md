---
title: week 01   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9ocqYW1XHk4
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [rbd, destruction, fracture, voronoi, boolean, plasticity, constraints, active-animated, bridge, intermediate]
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
**Transcript:** Hello and welcome to week one of the Manhattan Bridge destruction project. So we're going to start out this week by importing our lovely model. We'll analyze it and look at what we need to do to prepare for the simulation. We'll split it into a pattern we'll simulate and the pattern will just be static. Then we'll further organize it so into parts which will be deformable metal, rigid metal and then the road which we will fracture. We'll clean and prepare everything ready for the simulation again. We'll be fracturing the road with a bolean method using, you know, we'll create cutting geometry and then we'll fracture the deformable metal with a Voronoi method. We will be configuring plus this, sorry, soft constraints and configuring plasticity with that for the metal obviously and for just generally holding everything together. We'll be animating the bridge so that it kind of looks like it's in an earthquake or in windy conditions so it's kind of swaying back and forwards and this animation will be in the simulation itself and then we'll be playing around with the active and animated attributes so that we have so that we can kind of mix that animated element with the simulated element. We'll be cashing that out in a nice and efficient way so that it's not too heavy on your hard drive and then post simulation will be deforming the metal to get deforming the high res rendered geometry with the lowest proxy geometry and kind of bringing everything together so that we have a nice smooth simulated geometry ready for render at the end.

**Frame:** tutorials\frames\week-01-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only. Manhattan Bridge destruction: Week 1 overview — model import, fracture prep (boolean for road, Voronoi for metal), plasticity + soft constraints, active/animated attributes for sim/animation blend, efficient caching, post-sim deformation of hi-res geometry from low-res proxy.

### Summary
1m58s intro for Week 1 of VFX School's "Manhattan Bridge Destruction Project" course. Topics previewed: import bridge model, analyze and split into simulated/static parts (deformable metal + rigid metal + road). Fracture: road = boolean with custom cutting geo; deformable metal = Voronoi fracture. Configure plasticity and soft constraints (for metal bending behavior). Animate bridge (earthquake/wind sway). Active/animated attributes to blend animation with simulation. Cache efficiently. Post-sim: deform hi-res render geometry using low-res proxy simulation.

### Key Steps
*(Week introduction — see other week-01-xx lessons for specifics)*

Week 1 pipeline overview:
1. Import Manhattan Bridge model → analyze, prepare
2. Split geometry: deformable metal / rigid metal / road (fracture zones)
3. Fracture: road → Boolean fracture with custom cutting geometry; deformable metal → Voronoi fracture
4. Configure plasticity + soft constraints (metal behavior)
5. Animate bridge oscillation (earthquake/wind)
6. `active` and `animated` attributes → blend simulated elements with animation
7. Cache simulation efficiently (low disk footprint)
8. Post-sim: deform hi-res geometry using low-res proxy transform data

### Houdini Nodes / VEX / Settings
- Boolean fracture (custom cutting geo) for road
- Voronoi fracture for deformable metal
- Soft constraints + plasticity (RBD metal behavior)
- `active` / `animated` point attributes (DOP: controls which points simulate vs animate)
- Point Deform / Lattice for hi-res deformation from low-res proxy

### Difficulty
Intermediate

### Houdini Version
H18+

### Tags
[rbd, destruction, fracture, voronoi, boolean, plasticity, constraints, active-animated, bridge, intermediate]

---

## Related Tutorials
- week-01-11-rbd-configure-v1-1080p.md (same week, RBD configure details)
- week-02-01-intro-v1-1080p.md (week 2 intro, same project)
