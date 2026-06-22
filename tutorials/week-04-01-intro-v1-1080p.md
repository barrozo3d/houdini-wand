---
title: week 04   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=GQSxmuvXsvM
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [particles, pyro, simulation, dop, attributes, beginner]
extraction_status: complete
frames_dir: tutorials/frames/week-04-01-intro-v1-1080p/
frame_count: 4
---

# week 04   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=GQSxmuvXsvM)
**Author:** The VFX School Archive
**Duration:** 1m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Welcome to week four. Um, this week is debris and smoke simulations. So, there'll be three simulations in total. One popsim for the debris and two pyro simulations. So, uh, one of the pyro simulations will be based on the results of the popsim. So, we start with the popsim and we're using the debris source node which is a great um, shop. It looks at geometry which is near um pieces of geometry which are near to each other and then when they come apart it scatters points onto them and then they kind of are deleted after a bit of time based on an age attribute. We will be um setting up a pyro source or two different sources. We'll be um culling the geometry based on the speed so that we only generate um points on fastmoving objects. um we'll be using we'll be you know adding noise to the um density and temperature attributes of the points which will later go into our pyro simulation. Um and then we'll be adding nice detail to our pyro sims with um disturbance and turbulence.

**Frame:** tutorials\frames\week-04-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-four overview: generating debris particles with the Debris Source node and driving two separate Pyro simulations — one based on the POP sim output — to produce realistic dust and smoke for the bridge destruction.

### Summary
This week covers three simulations: one POP (particle) simulation for debris chunks and two Pyro smoke simulations. The Debris Source SOP scatters points between separating RBD pieces and deletes them by age. Particles are then culled by speed so only fast-moving geometry emits debris. Noise is added to density and temperature attributes before feeding into the Pyro sims, which are enhanced with disturbance and turbulence for realistic detail.

### Key Steps
1. [`Debris Source SOP`] Scatter debris points at separation boundaries between RBD pieces
2. [`POP Solver`] Simulate debris particles with gravity and lifetime
3. [`Attribute Wrangle`] Add noise to `density` and `temperature` point attributes
4. [`Speed Cull`] Filter points so only high-velocity pieces emit debris/smoke
5. [`Pyro Source`] Convert the POP points into a volumetric pyro source
6. [`Pyro Solver`] Run first Pyro sim for general dust cloud
7. [`Pyro Solver`] Run second Pyro sim driven by the POP sim result for localised smoke

### Houdini Nodes / VEX / Settings
- `Debris Source SOP` — detects close RBD pieces and scatters emission points at their boundaries; points deleted by an `age` attribute ramp
- `Pyro Source SOP` — converts point or volume data into density/temperature fields for Pyro
- Disturbance + Turbulence — Pyro solver microsolver settings that break up the smoke for added realism
- Speed-based culling — velocity threshold on points controls which pieces contribute emission

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Cull by Speed](week-04-06-cull-by-speed-v1-1080p.md) — deep dive into the velocity-based culling step introduced this week
- [Building the Vortex DOP Network](78-building-the-vortex-dop-network-v1-1080p.md) — advanced Pyro techniques for comparison
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — foundational POP concepts
