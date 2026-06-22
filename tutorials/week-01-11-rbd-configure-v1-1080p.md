---
title: week 01   11   rbd configure v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=dIBS14jw25k
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rbd, simulation, dop, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-01-11-rbd-configure-v1-1080p/
frame_count: 4
---

# week 01   11   rbd configure v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=dIBS14jw25k)
**Author:** The VFX School Archive
**Duration:** 10m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right, let's drop in RBD configure. So, this will pack and prepare all of the geometry for the simulation. Alt click to just tidy this up a bit. Like that. Okay, let's visualize that. Now, straight away, what I'm going to do is just uh drop a delete node just to isolate one of these pieces. Um, if I just come in here and grab one of these. So, just grab that. Um, delete that. Actually, two delete nodes there. Um, and delete non selected. So, we're just isolating that. And then drop a bullet solver again here. The reason I'm doing this just I want to see the collision geometry. It's always a good idea to look at your collision geome geometry. By default, you don't see it. So, you've got to turn it on. Come into the visualize tab and show geometry representation. And then we can see it's quite a lot bigger than our actual geometry. And that's controlled by um you've either got it here solver your collision padding. Okay. So, if I put that to zero, you can see it's there's nothing there. um put that back to default or you can do it here um which is what I'm going to do. Go into collision shapes. You can change the collision uh geometry representation. You c...

**Frame:** tutorials\frames\week-01-11-rbd-configure-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Deep dive into the `RBD Configure` node — visualising and tuning collision geometry representation and padding to ensure accurate Bullet solver contacts for bridge destruction pieces.

### Summary
The instructor drops in the RBD Configure node, then isolates a single piece using Delete nodes to inspect its collision geometry. The Visualize tab is used to reveal the collision proxy, which is larger than the actual mesh by default due to collision padding. The tutorial covers how to adjust collision padding on the solver vs. per-piece, and how to switch collision shape type (convex hull, bounding box, concave) for different piece types.

### Key Steps
1. [`RBD Configure`] Drop and connect to pack all simulated geometry
2. [`Delete SOP`] Isolate a single piece for per-piece collision inspection
3. [`Bullet Solver`] Connect a test solver; enable Visualize > Show Geometry Representation
4. [Solver settings] Adjust Collision Padding on the solver to reduce proxy inflation
5. [`RBD Configure` > Collision Shapes] Change collision shape type (convex hull / bounding box / concave)
6. [Per-piece override] Set collision padding per primitive group for finer control
7. [Verify] Inspect final collision proxy fits actual mesh before caching

### Houdini Nodes / VEX / Settings
- `RBD Configure` — packs geometry and writes RBD-required point/primitive attributes; exposes Collision Shapes tab for per-piece proxy type
- `Bullet Solver` — Visualize tab > Show Geometry Representation displays active collision proxy
- Collision Padding — gap added around each proxy shape; reduces interpenetration but inflates collisions if too large
- Collision Shape Types — Convex Hull (default, fast), Box (fastest), Concave (accurate, slow)

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — the overall week where RBD Configure is first introduced
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — foundational Bullet sim setup
- [Module I Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — related per-piece RBD attribute work
