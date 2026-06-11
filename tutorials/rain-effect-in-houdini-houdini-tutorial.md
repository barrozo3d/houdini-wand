---
title: Rain Effect in houdini | Houdini Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=Yi0ATGFthqk
author: Fx Guru
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [dop, sop, particles, simulation, volumes, vdb, rendering, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/rain-effect-in-houdini-houdini-tutorial/
frame_count: 4
---

# Rain Effect in houdini | Houdini Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=Yi0ATGFthqk)
**Author:** Fx Guru
**Duration:** 33m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello everyone, Welcome to FSCRU channel My name is Arbaaj and today i will show you a Rain Effect tutorial In this video we will see how we can generate Rain in Udini through Particle and then convert it into a match and render it in the temple So let's get started So first We will take an object You can take an object I will take Geometry face I will take face gel and I will increase it size about 5 something and I will transform it a little bit So this is my geometry Now i will take an emitter which will be our rain emitter So here i will take a grid I will take a grid and I will scale it according to the face 6 Now i will transform it a little bit You can use slider to do this Now we will take an particle network Pop network You can see that my grid is created by my emitter so particle is not generated but this particle is not generated because we will apply a gravity applied here So here we have a pop solver and here pop source is the object and this is the normal So first of all we will use gravity node which means my particle is a gravity applied You can see I will toggle this on real time so particle is generated You can see that it is going down because the life expectancy...

**Frame:** tutorials\frames\rain-effect-in-houdini-houdini-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
Rain effect using POP particle network: `grid` SOP as rain emitter (All Points), `popgravity` for falling motion, life expectancy control, particle-to-mesh conversion via VDB, with secondary splash particles at impact. Beginner-accessible pipeline.

### Summary
A 33-minute beginner rain effect tutorial by Fx Guru (Arbaaj). A `grid` SOP scaled to match a target geometry (scale 6) serves as the rain emitter — All Points emission from the grid via `popsource` creates dense rain columns. `popgravity` drives particles downward. Life expectancy controls rain density. Particles converted to mesh via VDB for rendering. Secondary splash effect simulated at impact point (frame 003: fountain-like splash spray). Rendered in Mantra/Karma or Redshift.

### Key Steps
1. Geo node → target geometry (face/object, scale ~5, transform into position)
2. `grid` SOP — scale to match object (scale 6); this is the rain emitter plane
3. `popnet` DOP → dive inside
4. `popsource` — Emission Type: **All Points** from grid → dense rain column
5. `popgravity` — enable gravity → particles fall straight down
6. Life expectancy parameter — control rain density and particle lifespan
7. Toggle real-time playback to preview particle flow
8. Particle to mesh: `vdbfromparticles` SOP → `convertvdb` SOP → polygon mesh
9. Secondary splash: new `popnet` with `popbounce` or custom velocity at collision point → splash spray particles
10. Render with water/glass material in Mantra/Karma

### Houdini Nodes / VEX / Settings
- `grid` SOP — scale 6 (rain emitter plane)
- `popnet` DOP
- `popsource` — All Points emission from grid
- `popgravity` — standard gravity downward
- Life expectancy — particle density control
- `vdbfromparticles` SOP — convert particles to VDB volume
- `convertvdb` SOP — VDB to polygon mesh
- Secondary `popnet` — splash at impact with `popbounce`
- Mantra/Karma water shader

### Difficulty
Beginner — Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
dop, sop, particles, simulation, volumes, vdb, rendering, beginner, intermediate

---

## Related Tutorials
- [[intro-to-houdini-particles---full-beginner-course]] — Full POP particle pipeline foundation
- [[intro-to-houdini-volumes---beginner-course]] — VDB from particles conversion
- [[houdini-tutorial-creating-realistic-waterfall-simulation-step-by-step]] — Advanced liquid/FLIP approach to similar effect
