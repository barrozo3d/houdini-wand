---
title: week 02   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=IoxlDdh5OPg
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [rbd, vellum, cables, constraints, guided-sim, bullet, bridge, destruction, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-01-intro-v1-1080p/
frame_count: 4
---

# week 02   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=IoxlDdh5OPg)
**Author:** The VFX School Archive
**Duration:** 2m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to week two. Now in week one we have already covered the bullet simulation of the actual road itself and the metal elements, well the kind of deforming metal elements. In this week we're looking at the cables and we're going to be using bullets for one and valum for the other. So they kind of go together obviously and the vertical cable hang from the horizontal cables. So we start out with the horizontal cables because they're so heavy and rigid you know they don't bend a lot. We're just going to be using bullets for simulating them. Now the geometry is quite intricate with kind of small pieces. So we're going to be looking at simplifying that geometry first, you know just creating four simple strands that we go into simulates and also because the kind of animation we're looking for is not to animated I suppose is a very simple movement. So we'll be using hard constraints for that and we'll actually be using the simulation that we generated in the first week to guide the simulation. So we're using the new guided sim workflow in Houdini with bullet. So there's something new that was introduced not too long ago where you can guide one simulation with other animated geometry. Then for the horizontal cables, sorry the vertical cables which will be much more bendy and animated and active we'll be using valum for that. So again we'll have to prepare some kind of appropriate geometry to feed into valum and some kind of proxy geometry. And then so that the top of the cables follow along with the animation. They'll be pinned to the previous animation and will be breaking constraints over the bottom of the cables will be connected to the bridge itself at the the road and they will have to break when their underserts and stresses and we'll be using scale and drag to kind of give a sense of scale to this bridge as it's such a big object.

**Frame:** tutorials\frames\week-02-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only. Week 2 of Manhattan Bridge Destruction: horizontal cables = Bullet (simplify to 4 strands, hard constraints, guided sim from Week 1 animation); vertical cables = Vellum (proxy geometry, pin top to previous animation, breaking constraints at bottom under stress, scale+drag for large-object feel).

### Summary
2m12s week intro by VFX School Archive. Week 2 of the Manhattan Bridge Destruction project. Covers two cable types:
- **Horizontal cables**: Heavy, rigid → Bullet sim. Simplified from intricate geo to 4 proxy strands. Hard constraints. Guided Sim workflow (Houdini feature that guides one sim using animated geometry from Week 1 road sim).
- **Vertical cables**: Bendy, active → Vellum sim. Proxy geometry prepared first. Top pinned to bridge animation. Bottom connected to road/bridge with breaking constraints (break when under stress). Scale + Drag forces for convincing large-bridge scale feel.

### Key Steps
*(Week introduction — see other week-02-xx lessons for specifics)*

Week 2 pipeline:
1. Horizontal cables: simplify geo → 4 strands; Bullet solver; hard constraints; Guided Sim workflow
2. Vertical cables: create proxy Vellum geometry; pin top to animated bridge; connect bottom to road with breakable constraints; add Scale + Drag forces

### Houdini Nodes / VEX / Settings
- Bullet solver with hard constraints (horizontal cables)
- Guided Sim workflow (Houdini) — guide simulation from previous animated geometry
- Vellum solver (vertical cables) — breakable constraints at bottom
- Scale + Drag forces for large-bridge motion feel

### Difficulty
Intermediate

### Houdini Version
H18+

### Tags
[rbd, vellum, cables, constraints, guided-sim, bullet, bridge, destruction, intermediate]

---

## Related Tutorials
- week-01-01-intro-v1-1080p.md (week 1 overview)
- week-02-03-starting-the-guided-sim-v1-1080p.md (guided sim detail)
- week-02-07-starting-the-vellum-sim-v1-1080p.md (Vellum cable sim detail)
