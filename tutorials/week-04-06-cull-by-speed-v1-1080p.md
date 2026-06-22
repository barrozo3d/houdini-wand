---
title: week 04   06   cull by speed v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=UFrvmv0rwQI
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [particles, pyro, attributes, vex, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-04-06-cull-by-speed-v1-1080p/
frame_count: 4
---

# week 04   06   cull by speed v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=UFrvmv0rwQI)
**Author:** The VFX School Archive
**Duration:** 7m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, let's come up here. Check load from disk and then we can scroll forward. You can see it plays back super fast. It's only points. They don't take much time. So, let's take a look at a flip book. I'm just going to drop a merge and then just connect that right to the top um for preview purposes. Turn that on. So, it's kind of hard to see here. You know, these points are really big. Um, so I'm gonna come out here and go press D on my keyboard and go to geometry and then change this. So particles display. We can display them as pixels. They're just tiny points. Or we can go to uh points and just make it smaller. Maybe I'll do that. Well, that looks pretty good. 1.5 seems about fine. And then let's get rid of this ground plane. Maybe I'd just add some quick color to this as well. Okay. Under there. And just some kind of dark brownie color. Desaturated. Darker than that. Uh, you know, don't worry about copying this. I'm We'll probably come back to this later for the uh, you know, before rendering. Um, less color than that. Still kind of looks brown there, doesn't it? Well, that'll do. Um, okay. And then, well, actually, if I just come here, I want to show y...

**Frame:** tutorials\frames\week-04-06-cull-by-speed-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Velocity-based particle culling — reading velocity magnitude from RBD simulation points and removing (culling) those below a speed threshold so that only fast-moving debris pieces emit smoke/dust particles.

### Summary
The instructor caches the POP sim result to disk and enables load-from-disk for fast flipbook playback. Particles are displayed as pixels or small points for viewport clarity. The core technique reads the `v` (velocity) attribute on each point, computes its length, and uses a threshold to delete slow-moving points so that only high-speed objects contribute to pyro emission sources. This prevents stationary or slowly-settling debris from generating unwanted smoke.

### Key Steps
1. [Cache + Load from Disk] Cache the POP sim to disk; enable Load from Disk on the File Cache node for fast playback
2. [`Merge SOP`] Temporarily merge debris into the main network for preview
3. [Viewport Display] Press D > Geometry > Particles Display; switch to Pixels or Points with reduced size for clarity
4. [`Attribute Wrangle`] Compute velocity magnitude: `float spd = length(v);`
5. [`Blast SOP` or Wrangle] Delete points where `spd` is below the speed threshold
6. [Iterate] Flipbook to verify only fast-moving pieces retain points
7. [Output] Feed culled points into the Pyro Source for smoke/dust emission

### Houdini Nodes / VEX / Settings
- `File Cache SOP` (Load from Disk) — reads pre-cached .bgeo.sc frames for near-instant playback of point sims
- `Attribute Wrangle` — VEX: `float spd = length(v); if (spd < threshold) removepoint(0, @ptnum);`
- `v` attribute — world-space velocity vector on RBD/POP points; standard Houdini velocity attribute
- Viewport Display (D key > Particles) — switches particle display mode to Pixels or Points for better visibility

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — the week overview that introduces this speed cull concept
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — foundational POP/particle work
- [Building the Vortex DOP Network](78-building-the-vortex-dop-network-v1-1080p.md) — Pyro that consumes these culled points
