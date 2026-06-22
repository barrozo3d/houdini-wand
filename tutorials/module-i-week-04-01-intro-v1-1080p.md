---
title: module i   week 04   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=w9p4zfurT2A
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, rendering, karma, advanced]
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
**Transcript:** Kind: captions Language: en Right, here we are at week four, the end of the RBD module and we're continuing with our car crash as I said. So, we're working on top of our simulation that we finished at the cache that we get from week three. We've got the metal done on the car and the wheels and all of that simulation. So, it's all about glass in this week and we're starting by fracturing the glass and because as this is um a car, you'll you'll notice or maybe you know that if you've ever seen a car, the the windscreen and the other windows on a car break, it's not like as you'd expect normal glass to break. So, the windscreen is laminated glass so it's going to be kind of it's going to be treated like a plastic almost so we have lots of tiny pieces. It breaks into, you know, thousands of tiny little kind of blocks but then kind of stays together and has a bit of a bendy effect to it and then the passenger side window that doesn't have the plastic in it, it's not laminated, it's just tempered. So, it just breaks up into loads of tiny pieces. So, we're doing the fracturing kind of a two-step. I'm doing kind of traditional, what do you what you'd expect out of a glass fracture first wh...

**Frame:** tutorials\frames\module-i-week-04-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Completing the car crash with two distinct glass fracture treatments — dense fine Voronoi with plasticity for laminated windscreen glass, and small-piece Voronoi with low break threshold for tempered side-window glass — followed by a final Solaris/Karma render.

### Summary
Two types of car glass require different fracture treatment. The windscreen uses laminated glass (with a PVB plastic inner layer): it fractures into thousands of small blocks that stay together and bend slightly like plastic rather than scattering as shards, achieved with dense fine Voronoi fracture, soft glue constraints and slight plasticity. Side windows use tempered glass: it shatters into many small pebble-shaped fragments that scatter completely, achieved with Voronoi using small pieces and a low break threshold. Both glass simulations use the Week 3 metal sim cache as the collision source. The final week delivers a Solaris/Karma render of the full car crash with all layers composited.

### Key Steps
1. [Windscreen] Dense fine `Voronoi Fracture` + soft glue constraints + slight plasticity for laminated, plastic-like cracking
2. [Side windows] `Voronoi Fracture` with small pieces + low break threshold for tempered, scattering glass
3. [Collision source] Use the cached Week 3 metal RBD sim as the collider for both glass sims
4. [`RBD Solver`] Run both glass simulations against the cached metal collision geometry
5. [Render] Composite metal + glass layers; render the full crash in Solaris/Karma

### Houdini Nodes / VEX / Settings
- Laminated glass technique — dense fine Voronoi + soft glue + plasticity, producing cohesive plastic-like deformation
- Tempered glass technique — Voronoi with small pieces + low break threshold, producing full scatter
- Cached collision hand-off — Week 3's metal sim cache is reused directly as the Week 4 glass collider
- Solaris/Karma — final render engine for the composited crash

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I)

---

## Related Tutorials
- [Car Crash: Metal Bending Geometry Organization](module-i-week-03-01-intro-v1-1080p.md) — the preceding week whose cache feeds this glass pass
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — another multi-material destruction using RBD Material Fracture
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — a relevant glass post-sim fix
