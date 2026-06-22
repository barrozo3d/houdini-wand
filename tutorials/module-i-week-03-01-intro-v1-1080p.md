---
title: module i   week 03   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=QkzF0SC76qY
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, attributes, animation, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-03-01-intro-v1-1080p/
frame_count: 4
---

# module i   week 03   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=QkzF0SC76qY)
**Author:** The VFX School Archive
**Duration:** 1m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, here we are at week three and for the last two weeks or week three and four we're doing one big project. We're finishing with a with a car crash so we've got a car kind of we've got a nice animation of a car sliding in sideways and then we're going to jump into a simulation where the car kind of slams into a post and we got lots of kind of metal bending and glass smashing everywhere but in the third week we're just looking at the metal and we're spending quite a bit of time in the in this in the third week kind of isolating and organizing the car because it's quite a complex piece of geometry. We've got lots of different pieces, you know, it's quite detailed. You know, it's a really nice model of the car so we've got to go through there and select pieces that we want to actually simulate and make it bend like metal. We're doing a lot to try and make it more efficient so the simulation time doesn't actually take too long in the end. It goes pretty fast but we get a really nice result, you know. So and also we're we're doing the wheel so the wheels are obviously spinning. They just spin a little, they don't need to because we're kind of sliding sidew...

**Frame:** tutorials\frames\module-i-week-03-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Organizing a complex car model's geometry for a car-crash simulation, separating pieces that need simulation from those kept rigid or pre-animated for performance.

### Summary
Overview of Week 3 (weeks 3 and 4 form one large project): the car slides in sideways and impacts a post, with metal bending and glass shattering across the two weeks. Week 3's focus is geometry organization — the car model is complex with many named parts, a detailed chassis, wheels and windows — and selecting the right pieces for simulation versus keeping others rigid or kinematic is critical for performance. Efficiency work includes simplifying/merging small non-simulating parts and isolating the bending panels. Wheels spin during the slide (pre-animated in SOPs), but that spin doesn't need to be simulated — wheels are kept kinematic and only become active on impact. The week outputs a cached simulation ready for Week 4's glass fracture pass.

### Key Steps
1. [Geometry audit] Inspect the complex car model's named parts, chassis, wheels and windows
2. [Simplify/merge] Combine small non-simulating parts to reduce piece count for performance
3. [Isolate bending panels] Separate body panels that need plasticity-driven deformation
4. [Pre-animate wheels] Animate wheel spin in SOPs; keep wheels kinematic until impact triggers activation
5. [`RBD Solver`] Run and cache the Week 3 simulation as the basis for Week 4's glass pass

### Houdini Nodes / VEX / Settings
- Geometry organization pass — merging/simplifying non-simulating parts is a performance-critical step before any RBD setup
- Kinematic-to-active wheel handling — pre-animated spin stays kinematic until an impact-triggered activation switches it to simulating
- Cached simulation hand-off — Week 3's cache feeds directly into Week 4's glass fracture pass

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I)

---

## Related Tutorials
- [Car Glass Fracture](module-i-week-04-01-intro-v1-1080p.md) — the direct continuation of this car-crash project
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the preceding week's multi-material destruction
- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — the staged-activation technique relevant to the wheel impact trigger
