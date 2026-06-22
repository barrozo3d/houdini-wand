---
title: 51 introducing the sop solver v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=8HkP7iVgi0Y
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [sop, dop, vex, particles, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/51-introducing-the-sop-solver-v1-1080p/
frame_count: 4
---

# 51 introducing the sop solver v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=8HkP7iVgi0Y)
**Author:** The VFX School Archive
**Duration:** 9m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Let's quickly create a new project to go over a brief introduction to particles and pops. So, we'll go over to file, new project, and I'll select the destination. I'll just call this intro to pops. Hit accept. And then I'll save the file. Intro to pops. 001. Now let's create a geometry container and I'll call this subsolver demo. Dive inside. Let's start by creating a grid. And it's just going to be a one square meter grid. It's fine. And on that grid, we'll scatter some points. Let's say 100 points and we'll disable the relax situations. Let me disable the grid and also switch to a dark background. So clicking D background dark. So these are the particles or the points that we generated on the surface. A particle solver will do is essentially grab the points position and each point's velocity and calculate what the next point's position will be based on that velocity. Position is just a vector. So you have three floats for each one of these coordinates X, Y, and Z. A velocity is also going to be a vector which with three floats for each one of the coordinates. And that vector is going to give us the direction of the movement and also the speed. The leng...

**Frame:** tutorials\frames\51-introducing-the-sop-solver-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Building a manual particle solver entirely inside a SOP Solver to teach the underlying integration mechanics before switching to the dedicated POP system.

### Summary
Creates a geometry network with a Scatter SOP (100 points) as the particle source. Explains that a particle solver tracks each point's position and velocity as vectors and integrates motion each frame: new_position = old_position + velocity * timestep. Builds this directly with an Attribute Wrangle inside a SOP Solver using `@P += @v * ch('timestep');`. Adds gravity by subtracting from the Y component of velocity each frame, then introduces age/life attributes to kill particles once they exceed their lifespan. The key teaching point is that POPs are simply a specialized, optimized wrapper around this exact SOP Solver logic.

### Key Steps
1. [`Scatter SOP`] Generate 100 points as the initial particle source
2. [`SOP Solver`] Wrap the points in a SOP Solver to iterate per-frame state
3. [`Attribute Wrangle`] Integrate position from velocity: `@P += @v * ch('timestep');`
4. [`Attribute Wrangle`] Apply gravity by decrementing `@v.y` each frame
5. [Age/Life attributes] Track `@age` and `@life`; remove points once age exceeds life
6. [Verify] Inspect the Geometry Spreadsheet to confirm position and velocity update correctly each frame

### Houdini Nodes / VEX / Settings
- `Scatter SOP` — generates the initial particle point cloud
- `SOP Solver` — iterates geometry frame-by-frame, feeding its own output back as input
- `Attribute Wrangle` — VEX: `@P += @v * ch('timestep');` for Euler integration; gravity via `@v.y -= ch('gravity');`
- `age` / `life` attributes — standard Houdini particle lifespan pattern, manually implemented here

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)

---

## Related Tutorials
- [Creating a Simplified Particle System](52-creating-a-simplified-particle-system-v1-1080p.md) — extends this manual solver to emit new particles each frame
- [Recreating Our Solver With POPs](53-recreating-our-solver-with-pops-v1-1080p.md) — rebuilds this exact system using POPs for comparison
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — later course revisiting POPs terminology
