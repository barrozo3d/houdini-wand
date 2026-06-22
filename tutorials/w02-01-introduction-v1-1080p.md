---
title: w02   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=C7vpFqAZClk
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [sop, attributes, procedural, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/w02-01-introduction-v1-1080p/
frame_count: 4
---

# w02   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=C7vpFqAZClk)
**Author:** The VFX School Archive
**Duration:** 1m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello everybody and welcome to week two of the tabletop course for uh this project we're going to be recreating the shots that you can see here in front of you. We've got these blueberries and chunks of chocolate falling into yogurt. To achieve this we're not actually going to be simulating any fluids at all. We're going to be reproducing this using um clever procedural uh techniques. So no fluid simulation at all, which means it's very quick to uh process, easy to iterate and try out different values, but we still achieve this really nice subtle uh fluid behavior here. Um I'll walk you through using the velocity and um the geometry itself to to form these shapes. We're going to be uh looking at obviously shading, lighting, and rendering this whole scene so you'll have exactly the same thing.

**Frame:** tutorials\frames\w02-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-two overview of the Tabletop course: faking fluid surface deformation (yogurt displacement) using procedural SOP techniques driven by velocity and geometry rather than any fluid simulation, for fast iteration with convincing splash shapes.

### Summary
Instead of running a FLIP simulation for the yogurt, the instructor uses purely procedural SOP deformation to recreate the look of blueberries and chocolate falling into yogurt. Velocity attributes from the falling objects are sampled and used to displace the yogurt surface geometry. This approach avoids heavy fluid simulation entirely, making it extremely quick to iterate while still achieving believable fluid-like shapes. Shading, lighting and rendering complete the week.

### Key Steps
1. [Review falling objects] Inspect blueberry/chocolate RBD geo and its velocity attributes
2. [`Trail SOP`] Compute velocity (`v`) on the falling geometry via Trail SOP in "Compute Velocity" mode
3. [`Attribute Transfer SOP`] Transfer velocity from falling objects onto yogurt surface points
4. [`Attribute Wrangle`] Displace yogurt surface point positions using transferred velocity magnitude
5. [Noise + Ramp] Add procedural noise to the displaced surface for organic fluid-like ripples
6. [Shading] Apply Principled Shader to yogurt with subsurface and gloss parameters
7. [Arnold ROP] Light and render the combined scene

### Houdini Nodes / VEX / Settings
- `Trail SOP` (Compute Velocity mode) — calculates per-point velocity vector from positional change between frames without leaving a trail
- `Attribute Transfer SOP` — copies attributes (here `v`) from one geometry to another based on proximity
- `Attribute Wrangle` — displaces `@P` along the transferred velocity or normal direction proportional to speed
- This technique avoids any DOP/FLIP entirely — all computation stays in SOPs

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Deforming with Velocity](w02-05-deforming-with-velocity-v1-1080p.md) — hands-on implementation of the velocity deformation introduced this week
- [Module I Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — related SOP deformation by attributes
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — next week using actual FLIP simulation
