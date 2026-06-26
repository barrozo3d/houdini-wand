---
title: module ii   week 03   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=F2vdSX1Dzgk
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [vellum, cloth, soft-body, point-deform, collisions, pin, breaking-welds, course-intro, intermediate]
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
**Transcript:** Welcome to week three and this week we actually get our first complete simulation. We're going to bring everything together, although the cloth that we set up, the soft body, the crocodile, the collider, we're going to bring all together and get a really nice simulation out of it. Before we do that, we, you know, a couple of little bits and barbs that we have to do. Something really important that I found that helped out a lot to this simulation and kind of a neat trick was to point to form the body. So the whole body is just kind of following around the crocodile's mouth and then just pinning the part of the body which is on the inside of the mouth. So only, you know, this part of the body is not actually simulating. It's just following the animation of the crocodile's mouth and that prevents, you know, a whole load of problems with them. Collisions, you know, when you've got the crocodile's mouth closing down on the, on the body, you're just asking for trouble with collisions with something like that. You know, you've got layer upon layer being crushed between two colliders which, you know, cannot give way if they need to. So, you know, we'll be doing that. And also a little bit of a Vex, I think, with breaking welds and constraints are looking at the ripping and then the point of forming the original geometry. So the, you know, we're using the simulated soft body and we're going to be using that to deform their nice clean, you know, render geometry as well.

**Frame:** tutorials\frames\module-ii-week-03-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Module II Week 3: first complete simulation combining soft body, cloth, and crocodile collider; key trick = pin the body part inside the croc's mouth to the croc's animation (avoiding impossible collision layers), then Point Deform the render geometry using the sim result.

### Summary
1m41s intro for Module II Week 3. This week brings everything together into a complete simulation: soft body hunter + cloth + crocodile collider. Key problem solved: the part of the body inside the croc's mouth is pinned to the croc's animation (not simulated) to avoid unsolvable collision stacking between two colliders. Also covers: VEX for breaking welds/constraints (cloth tearing), Point Deform to transfer sim deformation onto clean render geometry.

### Key Steps
- Pin body section inside crocodile's mouth to croc animation (prevents collision stack failure)
- Only exposed body parts simulate; mouth-interior part follows croc jaw animation exactly
- Breaking welds/constraints via VEX (cloth ripping)
- Point Deform: use simulated low-res body to deform high-res render geometry
- First complete end-to-end sim in the course

### Houdini Nodes / VEX / Settings
- Point Deform SOP — deform render geo using sim result
- Vellum SOP solver — soft body + cloth combined
- VEX — break weld/constraint attributes procedurally
- Pin to animation — body part inside mouth follows croc jaw

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[vellum, cloth, soft-body, point-deform, collisions, pin, breaking-welds, course-intro, intermediate]

---

## Related Tutorials
- module-ii-week-02-01-introduction-v1-1080p.md (week 2: cloth setup)
- module-ii-week-03-01-splitting-by-material-v1-1080p.md (splitting geo by material)
- module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p.md (VEX constraint breaking)
- module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md (rest blend / soft body)
