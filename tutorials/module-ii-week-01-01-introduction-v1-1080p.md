---
title: module ii   week 01   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Y00rlBFqpxQ
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [vellum, cloth, soft-body, tetrahedral, grains, rest-blend, course-intro, intermediate]
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
**Transcript:** Hello and welcome to week one of module two of the Houdini Renaissance program volume two. So this module is all about a volume we're diving right into volume and experimenting and playing around with it and I love volume so the two things that I like about it is that it's really fast and very versatile so you're able to simulate lots of different things so you can do cloth, string, hair, soft bodies and grains all in one solver and that's the reason that we're doing one big project here so we're doing this crocodile attack and in one simulation we're doing well actually not in one simulation but in one simulation we're doing the soft body of the actual hunter we're doing his clothes and what else we're also doing the grain after that after the fact we're going to use that as a collided stu it after after that but in the first lesson in the first week here I'm going to do a really quick overview of vellum and we're going to be you know actually simulating in the first lesson with cloth grains a soft body of struts, soft body not grain sorry and string and with a bit of animation in there just get a general overview then we move on into our project and bring in the geometry and kind of take a look at it and you know organize everything so where in this week we're setting up the soft body parts of the simulation so we're using the new tetrahedral soft bodies system which came in to do either 18 or 17 I'm not sure and yeah we can get really nice acurates and fast soft bodies so and also we're looking at updating the rest blend which is kind of if you understand using rest geometry or you know the rest length of constraints so they you know they want to kind of stay at one size so we can play with that and you know affect how the body wants to relax you know from to during the the simulation and then we are going to do a little bit of cloth constraints for the shoes kind of making a very stiff leather like cloth for that we're not doing the final simulation now we're just kind of setting up the constraints and doing a little bit of playing around with the animation of the crocodile just to avoid some problems with the collisions and get ready to move on to week two

**Frame:** tutorials\frames\module-ii-week-01-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Module II: Vellum module (all in one solver: cloth, string, hair, soft bodies, grains). Project: crocodile attack — tetrahedral soft body hunter + cloth + grains (post-sim collider).

### Summary
2m46s intro for Module II of the VFX School Renaissance program (Volume 2). Module focus: Vellum simulation — all solver types in one system (cloth, string, hair, tetrahedral soft bodies, grains). Project: crocodile attack sequence. Week 1 sets up: Vellum overview (quick cloth/grain/soft body/string intro), soft body of the human hunter using tetrahedral mesh (H17/18 feature), rest blend for soft body relaxation, cloth constraints for leather shoes.

### Key Steps
- Vellum advantages: fast + versatile; one solver for cloth/string/hair/soft body/grains
- Project pipeline: soft body hunter + clothes in one sim → grains as a separate pass using sim result as collider
- Tetrahedral soft bodies: new system for realistic volume-preserving soft body deformation
- Rest blend: controls how geometry wants to relax back toward its rest shape during simulation
- Cloth for shoes: high stiffness for leather-like cloth behavior

### Houdini Nodes / VEX / Settings
- Vellum Configure Cloth, Vellum Configure Grain — covered in upcoming lessons
- Tetrahedral soft bodies — Vellum Configure Tet Soft Body (H17/18+)
- Rest Blend — controls constraint rest length targeting during sim

### Difficulty
Intermediate (context video)

### Houdini Version
H18.5

### Tags
[vellum, cloth, soft-body, tetrahedral, grains, rest-blend, course-intro, intermediate]

---

## Related Tutorials
- module-ii-week-01-02-introduction-to-vellum-v1-1080p.md (Vellum quick overview)
- module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md (tet soft bodies)
- module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md (rest blend)
