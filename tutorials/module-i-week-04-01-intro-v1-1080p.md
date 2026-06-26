---
title: module i   week 04   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=w9p4zfurT2A
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, glass, fracture, car-crash, constraints, laminated-glass, course-intro, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-04-01-intro-v1-1080p/
frame_count: 4
---

# module i   week 04   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=w9p4zfurT2A)
**Author:** The VFX School Archive
**Duration:** 1m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Right, here we are at week four, the end of the AVD module, and we're continuing with our car crash, as I said. So we're working on top of our simulation that we finish that the cache that we get from week three. We've got the metal down and the car and the wheels and all of that simulation. So I'm going to talk about glass in this week, and we're starting by fracturing the glass. And because as this is a car, you'll notice, or maybe you know that if you've ever seen a car, the windscreen and the other windows and a car break is not like, as you'd expect, normal glass to break. So the windscreen is laminated glass, so it's going to be kind of, it's going to be treated like a plastic almost. So we have lots of tiny pieces. It breaks into, you know, thousands of tiny little kind of blocks, but then kind of stays together. And it has a bit of a bendy effect to it. And then the passenger side window that doesn't have the plastic in it, it's not laminated, it's just tempered. So it just breaks up into loads of tiny pieces. So we're doing the fracturing kind of a two step. I'm doing the kind of traditional, what do you, what do you expect out of a glass fracture first where you get the triangles in a kind of spider web pattern. And then on top of that again, I'm, we're going to be fracturing it again with a more, just a traditional kind of a, for an eye fracture to get all those tiny little pieces. Then we, you know, setting up constraints. And as we've got different things going on, we're doing a few bits and bobs to strengthen certain parts, we can certain parts, you know, sticking up, we got to stick them to the windows and, you know, doing things over time in the simulation also. And then bringing that all together, you know, setting some materials lights and getting a nice render at the end.

**Frame:** tutorials\frames\module-i-week-04-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Week 4 car crash: glass fracture pipeline (laminated windscreen = two-step Voronoi + spider web, tempered side window = small pieces), constraints for glass stick-to-frame behavior, final render.

### Summary
1m53s intro for Week 4 (final week of Module I RBD course). Builds on Week 3 metal simulation. Covers: laminated glass (windscreen) fracture — first a triangular spider-web pattern then Voronoi fine fracture; tempered glass (side window) — simple fine Voronoi pieces; constraint setup to keep glass pieces stuck to window frame initially; per-frame constraint manipulation in simulation; materials/lights for final car crash render.

### Key Steps
- Windscreen (laminated): 2-step fracture — spider web triangles first → Voronoi again for tiny blocks; plastic/bending behavior, stays together
- Side window (tempered): single Voronoi fracture → thousands of tiny pieces, flies apart
- Constraints: stick glass to window frame, selectively weaken over time in sim
- Final: materials + lights + render

### Houdini Nodes / VEX / Settings
- RBD Material Fracture (glass mode) — spider web pattern
- Voronoi Fracture — second pass for sub-fracture into tiny pieces
- Constraint networks — time-based weakening

### Difficulty
Intermediate (context video)

### Houdini Version
H18.5

### Tags
[rbd, glass, fracture, car-crash, constraints, laminated-glass, course-intro, intermediate]

---

## Related Tutorials
- module-i-week-03-01-intro-v1-1080p.md (Week 3: metal and wheels)
- module-i-week-05-01-importing-the-geometry-v1-1080p.md (Module I Week 5)
