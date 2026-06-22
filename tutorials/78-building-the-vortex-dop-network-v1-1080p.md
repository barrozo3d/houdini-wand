---
title: 78 building the vortex dop network v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=FAE7gVev-ss
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [dop, sop, pyro, volumes, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/78-building-the-vortex-dop-network-v1-1080p/
frame_count: 4
---

# 78 building the vortex dop network v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=FAE7gVev-ss)
**Author:** The VFX School Archive
**Duration:** 9m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, so we have the source. Let's we'll create another dot network for this taurus pyro sim. Let's go inside create the necessary ingredients. So we need a pyro solver. We'll need a smoke object. and we'll need a volume source. These are the essentials. Let's set up the smoke object. One way that I usually um that I frequently use to set up the size of the smoke object is by creating a static object and choosing the Taurus. In this case, I'll copy this soft path and copy it here. and use object transform. And if we merge it with the scene with the simulation that we have, we'll be able to see it here. It's just a a temporary setup uh so that I can adjust the size of the smoke object properly. I'll do the same thing as usual regarding the making sure that the grid is uh on the on the ground. So I'll say copy parameter paste relative references and say this divided by two and I'll make this bigger maybe three. Give it a bit more room. Yeah I I'll put it to 1.5. I'm going to make the Taurus go higher here. 1.5. Now we need to remember that we were considering that um the center of the Taurus was at one of height. So here we need to adjust 1.5 as well just ...

**Frame:** tutorials\frames\78-building-the-vortex-dop-network-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Building the DOP network for the spinning-torus smoke vortex: a Pyro Solver, Smoke Object and Volume Source, sized and sourced so the torus's own spin velocity drives the swirling column with no additional force fields.

### Summary
The core network uses three nodes: Pyro Solver, Smoke Object and Volume Source. A sizing trick temporarily adds a Static Object with the torus geometry to visually calibrate the Smoke Object's bounding box, which is then removed once sizing is confirmed. The smoke container is set to roughly 3 units wide, centered at 1.5 height to match the torus position, using "copy parameter / paste relative references" to link the container's center Y to half its size. The Volume Source uses SDF source type, links to the torus geometry, and sources both temperature and density. The Pyro Solver enables Disturbance and Turbulence microsolvers to break up the vortex edge. The key vortex technique is that the spinning torus imparts its own velocity to the smoke at emission, creating the helical swirling column without any extra custom force fields.

### Key Steps
1. [`Static Object`] Temporarily add the torus geometry to visually size the Smoke Object's bounds
2. [`Smoke Object`] Set container size to ~3 units, centered to match the torus height (linked via relative parameter reference)
3. [`Volume Source`] Set source type to SDF, link to torus geometry, source temperature and density
4. [`Pyro Solver`] Enable Disturbance and Turbulence microsolvers for vortex edge detail
5. [Remove sizing aid] Delete the temporary Static Object once the container is correctly sized
6. [Verify] Playback confirms the spinning torus geometry alone drives the helical smoke motion

### Houdini Nodes / VEX / Settings
- `Pyro Solver` — core combustion/smoke solver; Disturbance and Turbulence add visual breakup
- `Smoke Object` — defines the simulation container bounds and resolution
- `Volume Source` (SDF mode) — converts torus geometry into temperature/density source fields
- `Static Object` — used temporarily and only for visual bounding-box calibration
- Relative parameter references ("copy parameter / paste relative") — links container center to half its size for self-adjusting bounds

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)

---

## Related Tutorials
- [Starting the Smoke Vortex](76-starting-the-smoke-vortex-v1-1080p.md) — the preceding lesson building the spinning torus source
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — another Pyro setup using Disturbance/Turbulence
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — foundational fog/SDF volume concepts
