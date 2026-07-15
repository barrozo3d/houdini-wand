---
title: Procedural Rock Wall without intersections
source: YouTube
url: https://www.youtube.com/watch?v=q-9cVBVMv2E
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.593"
tags: [rbd, simulation, scatter, packed-primitives, procedural-modeling, environment, stone-wall]
extraction_status: complete
frames_dir: tutorials/frames/procedural-rock-wall-without-intersections/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Rock Wall without intersections

**Source:** [YouTube](https://www.youtube.com/watch?v=q-9cVBVMv2E)
**Author:** cgside
**Duration:** 3m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So last year I created this stone wall for a
[0:05] project and it took me quite a while to do it in Zbrush and then assemble it in
[0:16] Maya. As you can see I even created custom scripts and whatnot so I thought I
[0:24] would give Odinia go to try to create something similar. So here's my attempt
[0:31] creating the stone wall. It's quite a simple setup. The stones are
[0:37] eye-poly at this point but here for the simulation they are very low-poly and
[0:45] let me show you how I did this. So basically I created some rocks. Here you can
[0:55] see one example. I created a few in a loop and I created the eye-poly and the
[1:03] proxy geo for the simulation. Basically with poly-redoos and from there I
[1:13] copy two points, the low poly, I copy two points to agree with a
[1:27] scatter node with a lot of relaxed iterations and this is the result I got. So now
[1:37] having this copy to point southputs we can fill it to an RBD solver and try to
[1:45] avoid intersections and create the final shape. So basically here I'm using a
[1:52] bound node with all settings and then I'm animating the transform, the scale
[2:01] Y from 1 to 0.4 something like this. So this is exactly the shape I want for
[2:13] the wall and I'm animating along a few frames so it has some time to to
[2:21] calculate properly. So now if I enable the solver and play it you can see how
[2:34] it's starting to compress the stones against each other and creating the
[2:40] the final look. This should be the trick as you can see we have no intersections
[2:54] and this should be good enough. So now you can export these and create textures but
[3:03] in this case I am just back injecting the iPoly from above. You're in the
[3:12] split I have the low poly and in this branch I have the iPoly so now I can just
[3:22] back inject the iPoly. Just as a previous visualization of what it might look
[3:35] like at the end. So that's basically it you can grab the file from my Patreon if
[3:42] you want to investigate on your own feel free to leave some suggestions and
[3:47] comments and I will see you in the next one.



---

## Captured Frames

- [1:00] tutorials/frames/procedural-rock-wall-without-intersections/frame_000.jpg
- [1:40] tutorials/frames/procedural-rock-wall-without-intersections/frame_001.jpg
- [2:25] tutorials/frames/procedural-rock-wall-without-intersections/frame_002.jpg
- [2:55] tutorials/frames/procedural-rock-wall-without-intersections/frame_003.jpg
- [3:30] tutorials/frames/procedural-rock-wall-without-intersections/frame_004.jpg
- [3:55] tutorials/frames/procedural-rock-wall-without-intersections/frame_005.jpg

---

## Structured Notes

### Core Technique
Use an RBD Bullet solver as a *compression tool* rather than a destructive simulation: scatter low-poly proxy stones with heavy relaxed-iteration overlap removal, then animate a bounding container's scale down over time so the solver naturally compresses the stones against each other and each other's collision shapes, eliminating intersections without manual placement.

### Summary
Individual rocks are modeled once in a loop, each generating both a high-poly render version and a very low-poly proxy for simulation. The low-poly proxies are copied to scattered points (using a Scatter node with many relaxation iterations to reduce initial overlap), then fed into an RBD Bullet Solver alongside a **Bound** node (all-sides collision box) whose Y-scale is animated from 1 down to ~0.4 over a number of frames. Playing the sim causes the stones to compress against each other and the shrinking bound, settling into a tightly packed, intersection-free arrangement resembling a real stacked-stone wall. Afterward the pieces are packed into single points, and the original high-poly geometry is back-injected onto the simulated low-poly transforms for the final render-ready result.

### Key Steps
1. Model a handful of individual rock variations in a loop, generating for each: a high-poly render version and a corresponding very-low-poly proxy geometry (via PolyReduce) for simulation.
2. **Scatter** the low-poly proxies with a high point count and many **relaxation iterations** to spread them out with minimal initial overlap before simulation even begins.
3. **Copy to Points**: distribute the low-poly rock variations onto the relaxed scatter points.
4. Feed the copied geometry into an **RBD Bullet Solver**.
5. Create a **Bound** node with "all sides" collision enabled to act as a compressing container, then animate its **Transform scale Y** from 1 down to about 0.4 across several frames — giving the solver time to settle properly.
6. Enable the solver and play through the animated timeline: the stones compress against each other and against the shrinking bound, producing the desired wall-like packed shape with **no geometry intersections**.
7. **Pack** the simulated result into packed primitives (single points per piece) so they can be treated as individual objects downstream.
8. **Back-inject the high-poly geometry**: using the split branches created earlier (low-poly for sim, high-poly kept in a separate branch), swap the final low-poly simulated pieces for their corresponding high-poly source geometry, using the packed transforms to place them correctly.
9. Result: a fully packed, intersection-free stone wall ready for texturing, achieved without the extensive ZBrush + manual Maya assembly process the author used previously for the same effect.

### Houdini Nodes / VEX / Settings
PolyReduce (proxy geometry), Scatter (high relaxation iterations), Copy to Points, RBD Bullet Solver, Bound (all-sides collision), Transform (animated scale Y 1→0.4 over several frames), Pack, back-injection of high-poly geometry via packed-primitive transforms/split branches.

### Difficulty
Intermediate (the core idea — using RBD + a shrinking bound as a "compression" tool — is simple, but the proxy/high-poly split and back-injection setup requires some organizational care).

### Houdini Version
19.5.593 (visible in viewport title bar).

### Tags
rbd, simulation, scatter, packed-primitives, procedural-modeling, environment, stone-wall

---

## Related Tutorials
- [Ruins randomized brick wall](ruins-randomized-brick-wall.md) — alternate, non-simulation-based procedural approach (Voronoi Fracture + jittering) to broken/randomized wall construction from the same channel.
- [RBD rock surfaces with Houdini](rbd-rock-surfaces-with-houdini.md) — another RBD-fracture-based rock-surface technique from the same author.
- [Procedural Materials in Houdini 21 | Patreon December '25 - Free Lesson](procedural-materials-in-houdini-21-patreon-december-25---free-lesson.md) — shares the Connectivity/For-Each-per-piece pattern used here, applied there to a from-scratch cobblestone-chunking pipeline.
