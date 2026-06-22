---
title: 52 creating a simplified particle system v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=l65A4S4YhSw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [sop, dop, particles, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/52-creating-a-simplified-particle-system-v1-1080p/
frame_count: 4
---

# 52 creating a simplified particle system v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=l65A4S4YhSw)
**Author:** The VFX School Archive
**Duration:** 7m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Now another common thing is for the pop solver to be able to generate new particles on each frame. And the way we can do that is pretty straightforward. Let's go here to the scatter first. If you notice on the scatter we have this global seed and as you change the global seed the distribution of the particles on the surface changes. So we'll put here dollar f and this means that on each frame we'll have a different distribution of particles and here on the solver we'll take that into account. What we're going to be doing is we're going to be merging these particles whose position has been updated and then we'll merge the new particles coming in from input one. Let's go up. We go to the solver. We should now see that we're emitting particles, a stream of particles, and they all have the same speed, the same velocity vector. If you go to the geometry spreadsheet, you'll see that the velocity is constant for all of them, but the position is being updated based on the velocity. What else can we do to kind of simulate the functioning of a pop solver? What we can do is for instance we could also update the age of the particles. One of the characteristics of po...

**Frame:** tutorials\frames\52-creating-a-simplified-particle-system-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Extending the manual SOP Solver particle system to continuously emit new particles every frame, using a frame-dependent random seed and a Merge inside the solver to accumulate state.

### Summary
Uses `$F` as the global seed on the Scatter node so each frame produces a fresh point distribution. Inside the solver, merges the previous frame's existing particles (first input) with the new frame's freshly scattered particles (second input) using a Merge SOP, so the system continuously grows rather than resetting. Adds age tracking by incrementing `@age += 1/$FPS` each frame, and adds per-particle velocity variation via an Attribute Wrangle that randomizes initial `@v`. The Geometry Spreadsheet is used to confirm that, without the random seed logic, all particles share an identical constant velocity.

### Key Steps
1. [`Scatter SOP`] Set the random seed expression to `$F` so each frame emits a new distribution
2. [`Merge SOP`] Inside the SOP Solver, merge existing particles (input 1) with newly emitted particles (input 2)
3. [`Attribute Wrangle`] Increment age each frame: `@age += 1/$FPS;`
4. [`Attribute Wrangle`] Randomize initial velocity per new particle for variation
5. [Verify] Use the Geometry Spreadsheet to confirm velocity differs per particle once randomization is added

### Houdini Nodes / VEX / Settings
- `$F` expression — global current-frame variable used as a per-frame random seed for continuous emission
- `Merge SOP` (inside SOP Solver) — combines persisted particle state with newly emitted particles each frame
- `Attribute Wrangle` — VEX: `@age += 1/$FPS;` for time-correct age accumulation independent of frame rate
- Geometry Spreadsheet — used as the primary debugging tool to inspect per-point attribute values in real time

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)

---

## Related Tutorials
- [Introducing the SOP Solver](51-introducing-the-sop-solver-v1-1080p.md) — the foundational manual solver this extends
- [Recreating Our Solver With POPs](53-recreating-our-solver-with-pops-v1-1080p.md) — the POP-based equivalent of this continuous emission setup
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — POP terminology built on these SOP fundamentals
