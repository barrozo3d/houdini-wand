---
title: w03   04   adding viscosity v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9N9CavpgoB4
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [flip, simulation, dop, attributes, intermediate]
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
**Transcript:** Kind: captions Language: en So, we're going to be trying to simulate um chocolate pouring onto the ice cream. And obviously chocolate has a very different look to this. This is way too fluid. So, we need to add some viscosity um to our setup here. So, to do that, if you head into the flip solver and it's as easy as going to viscosity and enabling viscosity. So, that turns on uh the viscosity. Later on, we will be importing the viscosity attribute from outside of the sim so that we can have um different viscosities on different fluids. But for now, just for demonstration purposes, we'll we'll leave that um we'll just build it it will create the attributes here inside. And oops, we don't need to go in there. We need to select this. Where's our How did that all disappear now? What's going on? There we go. So, let's head into the flip object. Um cuz at the moment we still we've got the viscosity turned on. Just going to hide the ground plane, but we don't have any value. So, come into the flip object and actually give it under physical uh we leave everything else as default, but actually give it some viscosity. We'll try 100. Let's see how that looks. There we go. See some change. Alre...

**Frame:** tutorials\frames\w03-04-adding-viscosity-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Enabling and tuning viscosity in a FLIP fluid simulation — toggling the viscosity option in the FLIP Solver and setting per-object viscosity values in the FLIP Object's Physical tab, with a workflow for later importing per-point viscosity attributes for multi-fluid scenarios.

### Summary
Starting from a too-watery chocolate fluid, the instructor walks through the exact steps to add viscosity: first enabling it in the FLIP Solver, then navigating to the FLIP Object and setting a viscosity value (e.g. 100) in the Physical tab. The resulting sim shows visibly thicker, slower flow. The instructor previews the future step of importing per-point `viscosity` attribute from outside the DOP network to support multiple fluid types with different viscosities in one sim.

### Key Steps
1. [`FLIP Solver`] Enter the solver; navigate to the Viscosity tab and check "Enable Viscosity"
2. [`FLIP Object` > Physical tab] Set the Viscosity parameter to an initial value (e.g. 100)
3. [Playback] Run sim and observe thicker flow behaviour
4. [Iterate] Try values between 50-5000 to find desired thickness for chocolate
5. [Ground plane] Hide ground plane for cleaner preview
6. [Future step noted] Connect an external `viscosity` point attribute via FLIP Source for per-fluid variation
7. [Verify] Confirm fluid stacks and slows convincingly for a food-shot look

### Houdini Nodes / VEX / Settings
- `FLIP Solver` > Viscosity tab > Enable Viscosity — must be checked; without it the viscosity value on the object has no effect
- `FLIP Object` > Physical > Viscosity — global viscosity for the object (cP-like units); 0 = water, 100 = thick chocolate, 5000+ = very stiff
- Per-point `viscosity` attribute — advanced workflow: set `viscosity` per emitter point externally and import via FLIP Source to override the global value

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the week overview motivating this viscosity work
- [Viscosity and Surface Tension](w04-11-viscosity-and-surface-tension-v1-1080p.md) — expanded treatment in week 4
- [Small Scale Fluids](small-scale-fluids.md) — reference for FLIP viscosity in small-scale contexts
