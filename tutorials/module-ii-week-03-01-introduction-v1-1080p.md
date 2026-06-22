---
title: module ii   week 03   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=F2vdSX1Dzgk
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, cloth, simulation, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-03-01-introduction-v1-1080p/
frame_count: 4
---

# module ii   week 03   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=F2vdSX1Dzgk)
**Author:** The VFX School Archive
**Duration:** 1m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Welcome to week three, and this week we actually get our our first uh complete simulation. We're going to bring everything together, all the the cloth that we set up, the um soft body, the crocodile, the collider. Um and we're going to bring it all together and get a really nice um simulation out of it. Um before we do that, we you know, a couple of little bits and bobs that we have to do. Something really important that that I found I helped out a lot with the simulation and kind of neat trick was to uh point deform the body, so the whole body is just kind of following around the um the crocodile's mouth, and then just pinning the part of the body which is on the inside of the mouth. So, only, you know, this part of the body is not actually simulating. It's just following the animation of the crocodile's mouth, and that um prevents, you know, a whole load of problems with um collisions. You know, when you've got the crocodile's mouth closing down on the on the body, you're just asking for trouble with with collisions with something like that. You know, you've got a layer upon layer being crushed between two um uh colliders which, you know, cannot give w...

**Frame:** tutorials\frames\module-ii-week-03-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Assembling all Vellum elements into one simulation by point-deforming the part of the hunter's body inside the crocodile's mouth to follow the jaw animation directly, avoiding collision-explosion artifacts while the rest of the body simulates as a true soft body.

### Summary
Week 3 brings everything together into a single simulation. The key technique is point-deforming the hunter body to follow the crocodile mouth animation: the inner part of the body, inside the croc's mouth, is not simulated — it simply follows the croc mouth's deformation, preventing collision-explosion artifacts when the mouth closes on the body. Only the body parts outside the croc's mouth actually simulate as soft bodies. A constraint pins the body part inside the mouth to the croc jaw geometry using Vellum attach-to-geometry constraints. Cloth (shirt, pants, boots) is layered on top of this soft-body setup, with proper collision detection between cloth-to-soft-body and cloth-to-croc geometry.

### Key Steps
1. [`Point Deform`] Make the in-mouth portion of the hunter body follow the croc jaw animation directly (not simulated)
2. [Vellum attach-to-geometry] Pin the in-mouth body region to the croc jaw geometry
3. [Soft-body sim] Simulate only the body parts outside the croc's mouth as true Vellum soft bodies
4. [Layer cloth] Add shirt/pants/boots cloth on top of the soft-body setup
5. [Collision setup] Configure cloth-to-soft-body and cloth-to-croc collision detection
6. [Verify] Confirm no collision explosion occurs as the croc mouth closes on the body

### Houdini Nodes / VEX / Settings
- Point Deform (non-simulated region) — used to prevent collision-explosion artifacts at hard mouth-closure contact
- Vellum attach-to-geometry constraint — pins the point-deformed body region to the animated croc jaw
- Layered Vellum collision — cloth, soft body and croc geometry all collide within the same solver pass

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)

---

## Related Tutorials
- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — the preceding week's cloth-specific techniques layered on here
- [Tetrahedral Soft Bodies](module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md) — the soft-body setup being combined with cloth in this lesson
- [Vellum Grains: Source from Sim](module-ii-week-04-01-introduction-v1-1080p.md) — the following week's grains pass built on this combined sim
