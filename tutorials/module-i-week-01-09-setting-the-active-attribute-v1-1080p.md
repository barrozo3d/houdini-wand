---
title: module i   week 01   09   setting the active attribute v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=VXkmQAGzBbA
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, attributes, vex, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-01-09-setting-the-active-attribute-v1-1080p/
frame_count: 4
---

# module i   week 01   09   setting the active attribute v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=VXkmQAGzBbA)
**Author:** The VFX School Archive
**Duration:** 10m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en All right, let's continue. So, I'm going to drop a another new node. I mean the configure. Which is here. So, another new part of this pipeline. So, every I haven't explained but every node that kind of looks like this with this pink import and the two, you know, and the multiple imports and outputs is part of the new kind of RBD workflow. Uh the volume workflow kind of looks similar. And but, you know, these will all be called RBD something or other. And they'll all have, you know, the main geometry line, a constraint line, you know, this doesn't have to be this way. It's just neater because, you know, whenever you're building the the idea was, you know, when a typical RBD workflow would have all of these kind of lines anyway and they would be separate and you know, you'd have one here, one there and they'd be sharing things back and forth. So, it's easier just to keep them all together um in this one kind of uh one stack, I suppose you'd call it, okay? So, we got Yeah, we've got the main geometry, the constraints and the proxy geometry that we built. And if you're not sure, you know, sometimes they have four or three, you can just hover over the top. T...

**Frame:** tutorials\frames\module-i-week-01-09-setting-the-active-attribute-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Using the `active` integer attribute to control when RBD pieces become live in the simulation, enabling staged destruction that propagates outward from an impact point or follows a keyframed activation sequence.

### Summary
Explains the standard H19+ RBD workflow node chain, where every RBD node has a pink primary input plus constraint and proxy inputs: RBD Configure -> RBD Material Fracture -> RBD Constraint Properties -> RBD Solver. The `active` integer attribute (0 = kinematic/frozen, 1 = simulating) is set per primitive. Two common methods are shown: keyframe-animating `active` inside a SOP Solver within the DOP network, or setting `active` based on distance from an impact point so pieces near the blast go active first and outer pieces follow. The VEX pattern is `i@active = (@P.y < ch('threshold')) ? 1 : 0;` or a distance-based variant. Critically, `active` must be set at the SOP level before the DOP network, or inside a SOP Solver inside DOPs for animated activation.

### Key Steps
1. [Node chain] Establish RBD Configure -> RBD Material Fracture -> RBD Constraint Properties -> RBD Solver
2. [`Attribute Wrangle`] Set `i@active` per primitive: `i@active = (@P.y < ch('threshold')) ? 1 : 0;`
3. [Distance-based activation] Drive `active` by distance from an impact point for outward-propagating destruction
4. [`SOP Solver` (inside DOPs)] Keyframe-animate `active` over time for scripted activation sequences
5. [Verify] Confirm pieces stay kinematic (active=0) until their trigger condition, then simulate (active=1)

### Houdini Nodes / VEX / Settings
- `active` attribute (int, 0/1) — per-primitive switch between kinematic and simulating state
- VEX pattern: `i@active = (@P.y < ch('threshold')) ? 1 : 0;` — position/distance-based activation
- `SOP Solver` (inside DOPs) — required for animating `active` over time rather than a single static condition
- RBD node chain — RBD Configure / RBD Material Fracture / RBD Constraint Properties / RBD Solver, each with pink primary + constraint + proxy inputs

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)

---

## Related Tutorials
- [City Ground Destruction Intro](module-i-week-01-01-intro-v1-1080p.md) — the project this staged-activation technique supports
- [Concrete + Metal Destruction](module-ii-week-04-01-importing-the-geometry-v1-1080p.md) — references this exact technique for skyscraper collapse
- [Car Crash Geometry Organization](module-i-week-03-01-intro-v1-1080p.md) — the wheel impact-trigger activation relevant here
