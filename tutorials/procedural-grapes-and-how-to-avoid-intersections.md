---
title: Procedural Grapes and how to avoid intersections
source: YouTube
url: https://www.youtube.com/watch?v=9bq2Zx5zcIk
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.593"
tags: [vellum, vex, quaternion, branching, procedural-modeling, simulation, food, intersections]
extraction_status: complete
frames_dir: tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Grapes and how to avoid intersections

**Source:** [YouTube](https://www.youtube.com/watch?v=9bq2Zx5zcIk)
**Author:** cgside
**Duration:** 3m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'm going to show you how to create some simple procedural
[0:06] grapes in Odini. Starting with a line and resembling it by density set to ramp so I can have the
[0:15] initial stems or branches more concentrated towards the top. Adding a pointe heater and that's
[0:24] our base you may want to define the p-scale for the sweep and group it but that's about it.
[0:30] Now for the first set of branches I'm copying a distorted line to the points of our stem.
[0:38] Using a curve to set the start and end and I'm also reducing the p-scale along the curve using
[0:44] a naturoputagest float. Then for the orientation I am using the quaternion output from the
[0:52] oriental along curve and then in a randwell I am multiplying it with a new orientation.
[0:59] Basically what I want to do here is to set each branch 90 degrees apart along the stem
[1:06] and also add some variance in degrees. Big thanks to swalch for suggesting this approach.
[1:15] Okay adding some small branches again using the same wax wrangle as above.
[1:20] Now for the smaller ones we will use another approach using instead this sample direction
[1:28] confnction. You define a max angle and a random vector to value and we will sample the normal
[1:35] direction creating the cone effect you can see in this example. In the random u values I am
[1:42] fitting it between a min and max value so I don't get angles pointing straight up to the normal.
[1:50] Okay we need to create the grapes for that I'm using a rematched sphere and making sure I save
[1:59] the pin point for the valium seam. And just copying it to the end points of the smaller branches.
[2:10] As you can see I have a very small scale so they don't initially intersect and I'm
[2:16] animating the p-scale over the first few frames so I can solve the intersections with valium.
[2:28] For the seam a valium cloud with a very high stiffness and in the solver using the valium
[2:35] rest blend to update at each substep. And when we run the seam we avoid the undesirable
[2:43] intersections. So yeah that's about it. Check out the sin file on my patreon and don't hesitate
[2:52] on asking questions or making a suggestion below. Thank you for watching and see you in the next one.



---

## Captured Frames

- [0:10] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_000.jpg
- [0:40] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_001.jpg
- [1:05] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_002.jpg
- [1:35] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_003.jpg
- [2:05] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_004.jpg
- [2:35] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_005.jpg
- [3:00] tutorials/frames/procedural-grapes-and-how-to-avoid-intersections/frame_006.jpg

---

## Structured Notes

### Core Technique
Grow a procedural grape stem/branch hierarchy using quaternion-based orientation offsets (branches spaced 90° apart with variance) and `sample_direction()`-based cone scattering for twigs, then place small-scale grape berries at branch tips and let a **Vellum cloth simulation with animated p-scale growth** resolve all inter-berry intersections naturally instead of manually avoiding them.

### Summary
The main stem comes from a line resampled by density (ramp mode) to concentrate branch points toward the top, given a Point VOP-authored p-scale and grouped for later sweeping. First-level branches are built by copying a distorted line onto the stem points, using a curve to bound start/end and reducing p-scale via a natural-log-adjusted float; orientation comes from the quaternion output of Orient Along Curve, multiplied by a new rotation offset in a wrangle so each branch sits 90° apart around the stem with some random variance (credited to "swalch"). Smaller branches reuse the same wrangle; the smallest twigs instead use `sample_direction()` with a max angle and random vector to create a natural cone-shaped spread, with the random U fitted between min/max so angles don't point straight along the normal. Grapes are a remeshed sphere (with a saved pin point for the Vellum seam) copied to the small branches' end points at a very small initial scale so they don't intersect; the p-scale is then **animated up over the first few frames**, and a Vellum cloth solve with very high stiffness on the pin/seam constraint (updated at each substep via Vellum Rest Blend) pushes the growing berries apart naturally, eliminating the intersections a manual placement approach would otherwise require solving by hand.

### Key Steps
1. Build the stem: Line → Resample by Density (Ramp mode) to concentrate points toward the top → Point VOP for p-scale (used later for sweeping) → group for the sweep pass.
2. First branch tier: copy a distorted line to the stem points; use a curve node to define start/end bounds; reduce p-scale along the curve using a natural-log-adjusted Point VOP float.
3. Orientation: take the **quaternion output from Orient Along Curve**, then in a wrangle multiply it by a new rotation so each branch sits **90° apart** along the stem, plus some randomized variance in degrees (credit: swalch, suggested approach).
4. Repeat the same wrangle-based branching technique for smaller sub-branches.
5. For the smallest twigs, switch technique: use **`sample_direction()`** with a max angle and a random-vector "to" value to sample around the normal direction, creating a natural cone-shaped spread instead of the fixed 90°-offset pattern; fit the random U value between a min/max so angles don't point straight up along the normal (avoiding an unnaturally uniform look).
6. Build the grape berries: a remeshed sphere with a **saved pin point** (for the upcoming Vellum seam constraint), copied onto the endpoints of the smallest branches at a **very small initial scale** so berries don't overlap at spawn time.
7. **Animate p-scale up over the first few frames** to grow the berries from tiny to full size, letting the simulation resolve overlaps as they grow rather than starting large and colliding immediately.
8. Simulate with **Vellum Cloth**: set up a pin/seam constraint with very high stiffness, and in the Vellum solver use **Vellum Rest Blend** to update the constraint every substep — running the sim naturally pushes overlapping berries apart, avoiding the undesirable intersections that direct point placement would otherwise create.

### Houdini Nodes / VEX / Settings
Line, Resample by Density (Ramp), Point VOP (p-scale authoring), Curve (start/end bounds), Orient Along Curve (quaternion output), Attribute Wrangle (rotation-offset multiply, 90°-apart branch spacing with variance), `sample_direction()` VEX function (cone-shaped twig scattering, fit-clamped random U), Sphere (remeshed, pinned point saved for Vellum seam), Copy to Points, animated p-scale parameter (growth over first frames), Vellum Cloth, Vellum constraint (pin/seam, high stiffness), Vellum Rest Blend (per-substep constraint update).

### Difficulty
Advanced (quaternion-based orientation math and using a physics solver as an intersection-avoidance tool rather than for pure simulation both require solid Houdini/VEX fluency).

### Houdini Version
19.5.593 (visible in viewport title bar).

### Tags
vellum, vex, quaternion, branching, procedural-modeling, simulation, food, intersections

---

## Related Tutorials
- [Modeling Assets with Vellum](modeling-assets-with-vellum.md) — shares this channel's broader pattern of using Vellum as a modeling/de-intersection tool rather than pure simulation.
- [Procedural Rock Wall without intersections](procedural-rock-wall-without-intersections.md) — parallel technique using RBD instead of Vellum to resolve overlapping-geometry intersections naturally via simulation.
