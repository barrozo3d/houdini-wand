---
title: module ii   week 04   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=SlbMugY762Q
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [grains, vellum, rbd, bullet, rendering, karma, course-intro, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-04-01-introduction-v1-1080p/
frame_count: 4
---

# module ii   week 04   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=SlbMugY762Q)
**Author:** The VFX School Archive
**Duration:** 1m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So welcome to week four of module two, the last, we're at the last week now, so we're bringing everything together and getting a nice render result at the end, you know, seeing the results of all of our hard work. So obviously this week we're tackling the grains and we're starting out by building a good source geometry. So to kind of save unnecessary simulation time, wasting simulation time, we're going to build a source geometry based on our previous simulations, so using the weather crocodile and the hunter go to generate a, a kind of block or an area for to generate the grains. And because this happens over time, we need to use the solver node to do that, right? So that's a neat little trick to kind of save you some time and be more efficient, which is always good. Then we jump in and build our, build our simulation network in the, in dots from scratch. I think we use the, the shelf tool at the beginning, but this time, you know, we just build it up from scratch, not too complicated. Then we get our nice high res sim and appraise the simulation, so getting a bit more detail for free without having to simulate that. Then we just do a really simple simulation on the gun. This has to be a bullet simulation, so because it's obviously metal as hard, it doesn't bend, it's not vellum. So we just do that quickly. And then run through the rendering, so setting up materials, shaders on the crocodile, the hunter, as well, setting up some nice lights, rendering it out and enjoying our work of art.

**Frame:** tutorials\frames\module-ii-week-04-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Module II Week 4 (final week): grains from source geometry built using Solver SOP (dynamic emission over time), high-res sim upres, gun bullet sim (Bullet solver), and full Karma render with materials/shaders/lighting.

### Summary
1m55s intro for Module II Week 4 (last week of the VFX School Renaissance program Volume 2). Wraps up the crocodile attack project: (1) Grain source geometry built procedurally from previous sim results (croc + hunter geometry) using a Solver SOP to generate evolving emission volumes; (2) Full grain simulation from scratch in DOPs; (3) High-res upres from low-res grain cache; (4) Gun simulated as Bullet RBD (metal = rigid, not Vellum); (5) Karma render pass: materials, shaders for croc/hunter, lighting, final output.

### Key Steps
- Build grain source from previous crocodile + hunter sim geometry (evolving over time via Solver SOP)
- Solver SOP trick: generate dynamic source area that grows with simulation (save unnecessary grain emission)
- Grain DOP network built from scratch (not shelf tool this time)
- Upres: get high-res sim from low-res cache for free
- Gun sim: Bullet RBD (hard metal, not Vellum cloth)
- Karma render: materials, shaders, lights, final beauty pass

### Houdini Nodes / VEX / Settings
- Solver SOP — build time-evolving grain source from animated sim geometry
- Vellum Grain solver (DOP) — built from scratch
- Upres technique — improve sim detail without full re-sim
- Bullet RBD solver — gun simulation (rigid body)
- Karma renderer — materials, shaders, lights

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[grains, vellum, rbd, bullet, rendering, karma, course-intro, intermediate]

---

## Related Tutorials
- module-i-week-06-01-introduction-to-grains-v1-1080p.md (Vellum grains overview)
- module-ii-week-04-01-importing-the-geometry-v1-1080p.md (week 4 geometry import)
- module-ii-week-01-01-introduction-v1-1080p.md (module 2 intro)
- module-ii-week-01-01-basic-bullet-sim-v1-1080p.md (Bullet RBD basics)
