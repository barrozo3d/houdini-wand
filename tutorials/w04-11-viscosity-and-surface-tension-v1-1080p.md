---
title: w04   11   viscosity and surface tension v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=1yb3mindncw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [flip, simulation, dop, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/w04-11-viscosity-and-surface-tension-v1-1080p/
frame_count: 4
---

# w04   11   viscosity and surface tension v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=1yb3mindncw)
**Author:** The VFX School Archive
**Duration:** 12m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Now, before I forget, there's one one more thing I want to do in the emitter, if we jump into the flip source, and I'm just going to press spacebar and F to to focus in on the on our selected node. I'm just going to put this in wireframe so we can see the points. So, if I press play now, you can kind of see they're kind of static. So to get just a bit more variation in in their initial position, can use this jitter seed. Right? So if I move that, you can see they move. And to get this moving per frame, we've done this before. Dollar F. And that way when I press play, they will each frame they'll have a different position. Okay. The jitter scale is just how much they move. If I put this to zero, you can see it'll be in a grid. So one is fine for us. There's no can't see any pattern there. So just that um what I want to focus on now. So if the the last flip book we did was pretty um chaotic. You know the there wasn't much form in in the splash of the the fluid. So I'm going to look at adding a couple of things just to demonstrate. I'm just going to make another dot network here actually just to have something simple and clear. You don't have to do this if ...

**Frame:** tutorials\frames\w04-11-viscosity-and-surface-tension-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Tuning FLIP fluid viscosity and surface tension parameters together to achieve realistic milk splash behaviour — using jitter seed animated with `$F` for non-repeating emitter variation, then adjusting surface tension to create cohesive droplet crowns.

### Summary
Starting from a chaotic, formless splash, the instructor adds structured fluid behaviour by combining viscosity (light, for milk) and surface tension. The jitter seed on the FLIP Source is animated with `$F` so initial particle positions vary per frame, preventing grid patterns. A simple isolated DOP network is built to demonstrate the viscosity and surface tension interaction clearly. Surface tension creates the cohesive forces that hold milk droplets together into a crown shape, turning a chaotic spray into a photogenic food-shot splash.

### Key Steps
1. [`FLIP Source`] Navigate to the FLIP Source; locate Jitter Seed parameter
2. [Animate Jitter Seed] Set Jitter Seed expression to `$F` so variation changes each frame
3. [Jitter Scale] Set Jitter Scale to 1 for natural variation; 0 would produce a grid
4. [Isolated test network] Build a minimal DOP network to test viscosity and surface tension in isolation
5. [`FLIP Solver` > Viscosity] Enable and set low viscosity (~5-20) for milk
6. [`FLIP Solver` > Surface Tension] Enable surface tension; increase value until droplets and crown form
7. [Iterate] Flip-book and compare; surface tension too high collapses the fluid, too low makes it chaotic
8. [Apply to main network] Transfer confirmed values back to the main sim

### Houdini Nodes / VEX / Settings
- Jitter Seed (`$F`) — animated seed on FLIP Source prevents repeating particle grid patterns per frame
- Jitter Scale — controls magnitude of per-particle position randomisation; 0 = perfect grid, 1 = natural scatter
- `FLIP Solver` > Surface Tension — adds cohesive force between particles; value range typically 0.01-1.0 for water-like fluids; creates crown splashes and hanging droplets
- `FLIP Solver` > Viscosity — low values (1-20) for water/milk; works in conjunction with surface tension

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — the week overview introducing viscosity and surface tension for the milk pour
- [Adding Viscosity to FLIP](w03-04-adding-viscosity-v1-1080p.md) — the week 3 viscosity introduction this builds on
- [Small Scale Fluids](small-scale-fluids.md) — reference for FLIP surface tension in small-scale setups
