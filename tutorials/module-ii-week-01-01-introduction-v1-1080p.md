---
title: module ii   week 01   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Y00rlBFqpxQ
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, cloth, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-01-introduction-v1-1080p/
frame_count: 4
---

# module ii   week 01   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=Y00rlBFqpxQ)
**Author:** The VFX School Archive
**Duration:** 2m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello, and welcome to week one of module two of the Houdini Renaissance program volume two. So, um this module is all about uh Vellum. We're diving right into Vellum and and um experimenting and and playing around with it. And I love I love Vellum, so the two things that I like about it is that it's really fast and very versatile, so you're able to simulate lots of different things. So, you can do cloth, string, hair, um soft bodies, and grains. Um all in one solver, and that's the reason that we're doing one big project here. So, uh we're doing this crocodile attack, and uh in one simulation we're doing Well, actually not in one simulation, but in one simulation we're doing the soft body of the actual um hunter, we're doing his clothes, um and what else? We're also doing the grain after that after the fact. We're going to use that as a collider to it after after that. But, in the first lesson in the first week here, um I'm going to do a really quick overview of Vellum, and we're going to be, you know, actually simulating in the first um lesson um with um cloth, grains, a soft body strut, soft body, uh not grain, sorry, and string, and with a bit of anim...

**Frame:** tutorials\frames\module-ii-week-01-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Introducing the Vellum-focused Module II with a crocodile-attack scene, rapidly demonstrating cloth, tetrahedral soft bodies, string/wires and grains in a single solver to show Vellum's range.

### Summary
Project: a crocodile attack scene where a hunter is grabbed in the crocodile's mouth. Vellum is praised for being fast and versatile, handling cloth, string, hair, soft bodies and grains all in one solver. Week 1 is a rapid overview demonstrating cloth, soft bodies (tetrahedral constraints), string/wires and grains in a single lesson. The full project pipeline simulates the soft-body hunter (tetrahedral Vellum) together with cloth (the hunter's clothes) in one pass, then adds grains separately as a post-sim effect using the Vellum result as a collider. Introduces the Vellum sub-solver concept: a multi-step position-based-dynamics process that resolves constraints iteratively.

### Key Steps
1. [Cloth] Quick demo of Vellum cloth constraints
2. [Soft body] Quick demo of tetrahedral Vellum constraints
3. [String/wire] Quick demo of Vellum string/wire constraints
4. [Grains] Quick demo of Vellum grains
5. [Pipeline plan] Combine soft-body hunter + cloth clothes in one sim; add grains afterward using the Vellum result as a collider
6. [Sub-solver] Note the Vellum sub-solver as the iterative constraint-resolution mechanism shared by all types

### Houdini Nodes / VEX / Settings
- Vellum (single solver) — handles cloth, string, soft body and grains together with shared collision
- Vellum sub-solver — multi-step position-based-dynamics iteration that resolves constraints within each timestep
- Pipeline order — soft body + cloth simulated together first; grains added as a separate post-sim pass colliding against that result

### Difficulty
Intermediate

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)

---

## Related Tutorials
- [Introduction to Vellum: Cloth/String/Grain Fundamentals](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — the deep-dive gap-filler for the techniques previewed here
- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — the following week's cloth-specific focus
- [Tetrahedral Soft Bodies](module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md) — the gap-filler detailing the soft-body setup for the hunter
