---
title: module ii   week 01   06   updating the rest blend v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=aUkXMjjLT-k
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, rigging, attributes, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-06-updating-the-rest-blend-v1-1080p/
frame_count: 4
---

# module ii   week 01   06   updating the rest blend v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=aUkXMjjLT-k)
**Author:** The VFX School Archive
**Duration:** 12m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Now, when we come to simulate the whole um uh the whole kind of thing, um we'll find that the the position of the body of the hunter kind of stays, right? So, this is the rest position of of the body. And if he's you know, he's going to be kind of holding his arms up like this as if he's holding a gun, which kind of looks weird. So, um what I want to do is just I'm just going to bend the arms down because that's the most noticeable thing, you know, you could kind of straighten the legs out or put him in some kind of other pose, but I just want to bring the bend in these elbows out, okay? And then I'll show you how we can bring that into the simulation after the first frame. So, first we need to group and I've come bring a different um you know, bring this off to the side here. Okay, I'm going to group the arms, so and I want the left and then both separately. Left arm and the right arm. Right arm there. Okay, and then we're going to do this uh on the points, yeah? And we're going to use bounding region, bounding sphere. And if I grab the tool, I can bring this over cuz yeah, obviously I don't want to bend um all of the body. Just do each arm individually...

**Frame:** tutorials\frames\module-ii-week-01-06-updating-the-rest-blend-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Re-posing a character's arms and blending the new pose into the Vellum solid-body constraints as the rest state, using the `restblend` attribute as a spring-like target-position control without simulating actual muscles.

### Summary
The hunter's arms are raised in a T-pose / gun-holding pose, which looks wrong at rest. The fix is to manually re-pose the arms and blend this new rest position into the Vellum constraints so the solver treats it as the natural rest state. Workflow: group the left and right arms separately using bounding-sphere group mode, apply a Transform SOP per group to lower the arms, then feed this re-posed geometry into the Vellum Solid Object as the rest geometry via the "rest blend" parameter (which blends from the sim-current shape toward the rest shape). The `restblend` float attribute (0-1) controls how strongly the body is attracted back toward the rest pose, acting as a target-position spring. The rest blend is evaluated after each Vellum substep, making it an effective way to add muscle-like stiffness without simulating actual muscles.

### Key Steps
1. [`Group SOP`] Select left arm and right arm separately using bounding-sphere mode
2. [`Transform SOP`] Lower each arm group from the raised T-pose
3. [Rest geometry input] Feed the re-posed geometry into Vellum Solid Object's rest blend input
4. [`restblend` attribute] Set the 0-1 float controlling pull-back strength toward the new rest pose
5. [Verify] Confirm the rest blend is applied after each substep, giving muscle-like stiffness without actual muscle simulation

### Houdini Nodes / VEX / Settings
- `Group SOP` (bounding-sphere mode) — isolates limb regions for independent re-posing
- `Transform SOP` — applies the manual re-pose to lower the arms
- `restblend` attribute (float, 0-1) — Vellum Solid Object parameter blending sim-current shape toward a custom rest shape, evaluated per substep
- Rest-pose blending — a target-position-spring technique for muscle-like stiffness without true muscle simulation

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)

---

## Related Tutorials
- [Tetrahedral Soft Bodies](module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md) — the preceding setup this rest-blend correction applies to
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the combined sim using this corrected rest pose
- [Introduction to Vellum: Cloth/String/Grain Fundamentals](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — broader Vellum constraint fundamentals
