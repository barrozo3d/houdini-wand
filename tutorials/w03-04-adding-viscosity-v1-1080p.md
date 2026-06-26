---
title: w03   04   adding viscosity v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9N9CavpgoB4
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [flip, fluid, viscosity, simulation, chocolate, beginner]
extraction_status: complete
frames_dir: tutorials/frames/w03-04-adding-viscosity-v1-1080p/
frame_count: 4
---

# w03   04   adding viscosity v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9N9CavpgoB4)
**Author:** The VFX School Archive
**Duration:** 4m45s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So we're going to be trying to simulate chocolate pouring onto the ice cream and obviously chocolate has a very different look to this. This is way too fluid. So we need to add some viscosity to our set up here. So to do that, if you head into the flip solver and it is easy as going to viscosity and enabling viscosity, so that turns on the viscosity. Later on we will be importing the viscosity attributes from outside of the sim so we can have different viscosities on different fluids. But for now, just for demonstration purposes, we'll leave that, we'll just create the attributes here inside. And we don't need to go in there, we need to select this, where is that? That's all disappeared now. It's going on. There we go. So let's head into the flip object because at the moment we still, we've got the viscosity turned on. It's going to hide the ground plane. But we don't have any value. So come into the flip object and actually give it under physical, we'll leave everything else as defaults, but actually give it some viscosity, we'll try 100. Let's see how that looks. There we go. See some change. Already looks much better. Now you can see also some color there. Maybe if we come to initial date, so you don't have to do this, it's just to show you initial viscosity. So I'm going to just give some velocity to the beginning. Let's do like five, ten up. You can see the color change there already actually. You see that? So that's because the color is based on the velocity. So you jump up, there is it. And splat. So we're visualizing the velocity here. If we come to guides, visualizes particles are on. We can see here where visualizing the velocity within this range. So later on, when we've got different rates of viscosity, we can use this to look at them all. Let's watch that again. We get that nice splat. We try raising it even more. Go right to the top, ten thousand. So you see the values go up quite high. You can see that it kind of looks like, almost like clay or patty or something. So in your visualization, you can also look at the surface. It's kind of like a volume representation. Look at that. Cool. We'll leave just on particles for now. I'm going to turn off this initial velocity because we're not going to want that. Again, we're going to import our velocity from our emitter. Let's make the box smaller. If we have any particles which escape and kind of travel far away, somehow from our simulation, they'll be calculated and we'll be wasting lots of resources. So we can make this a lot smaller. I'm going to head into the flip solver and volume motion volume limits. Let's change this just to two, two and two. The scale is going to be way smaller. I'm going to raise this up to point eight.

**Frame:** tutorials\frames\w03-04-adding-viscosity-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Enable viscosity in FLIP Solver (viscosity tab) + set viscosity value in FLIP Object (Physical tab); value 100 = thick fluid, 10000 = clay-like. Volume Limits on FLIP Solver to prevent stray particle computation waste.

### Summary
4m45s VFX School Archive module. Part of a chocolate-over-ice-cream FLIP sim tutorial. Shows how to add viscosity: enable in FLIP Solver viscosity tab, set value in FLIP Object Physical tab (100 for chocolate, 10000 for clay). Mentions importing viscosity attributes from outside (multi-fluid workflow for later). Demonstrates velocity-based color visualization in guides. Sets Volume Limits to 2×2×2 to prevent stray particles from wasting compute. Adjusts flip object scale to 0.8.

### Key Steps
1. **FLIP Solver → Viscosity tab** — check "Enable Viscosity" (required first)
2. **FLIP Object → Physical tab** → set viscosity value:
   - 100 → thick chocolate-like fluid
   - 10,000 → clay / putty behavior
3. **Initial Velocity demo** (optional): FLIP Object → Initial tab → set velocity (e.g. {0, 10, 0}) to see color change (velocity-based Cd visualization)
4. **Guides tab** → visualize particles → displays velocity-based color in viewport
5. **Volume Limits** (FLIP Solver): set to 2, 2, 2 → constrains sim volume; stray escaping particles won't waste calculation resources
6. **FLIP Object scale** → raise to 0.8 after reducing volume limits

### Houdini Nodes / VEX / Settings
- **FLIP Solver → Viscosity tab**: enable viscosity checkbox
- **FLIP Object → Physical tab**: viscosity value (100=thick, 10000=clay)
- FLIP Object → Guides tab → visualize particles → velocity color preview
- FLIP Solver → Volume Motion → Volume Limits: 2,2,2 for tighter sim bounds
- Note: viscosity attribute can also be imported from emitter geometry (future lesson)

### Difficulty
Beginner

### Houdini Version
H18+

### Tags
[flip, fluid, viscosity, simulation, chocolate, beginner]

---

## Related Tutorials
- w02-05-deforming-with-velocity-v1-1080p.md (same course, velocity deformation)
- w03-11-meshing-v1-1080p.md (same course, FLIP meshing)
- w04-11-viscosity-and-surface-tension-v1-1080p.md (same course, advanced viscosity)
