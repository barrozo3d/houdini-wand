---
title: module ii   week 02   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=161Gcdsi6Nw
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [vellum, cloth, tearing, stitching, drape, remesh, course-intro, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-02-01-introduction-v1-1080p/
frame_count: 4
---

# module ii   week 02   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=161Gcdsi6Nw)
**Author:** The VFX School Archive
**Duration:** 1m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So welcome to week two of the course of the Vellum course. So this week we're focusing on clothes on the fabric. We're starting out by draping the cloth onto the body. So using the tipos of the model to fit the clothes accurately as if they're sitting correctly at the beginning of this simulation. We're also going to be preparing the geometry so it's good for simulation, making sure that the geometry is good, we're going to be using remashes and stuff like that, setting up groups and things as well ready for the constraints. And then we're also going to be looking at tearing clothes, so pre-cutting the cloth ready for pre-fracturing as we should say, ready for the simulation to tear them apart again, looking at welding them together, stitching and attaching to geometry, stuff like that. Obviously setting up the constraints for the cloths themselves will be actually simulating the drape. So you know, we'll be doing that sim fully and I think we do that in the Vellum Sup solver. And then a little bonus at the end where I kind of worked out a way of creating stiff areas of cloth, which can be quite hard to do with Vellum, where we kind of change the scale of the polygons on the same mesh to achieve really kind of stiff areas.

**Frame:** tutorials\frames\module-ii-week-02-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Module II Week 2: Vellum cloth simulation including draping onto body using T-pose, geometry prep (Remesh, groups), cloth tearing (pre-cut + weld/stitch), drape sim in Vellum SOP solver, and stiff cloth areas trick (scale polygons on same mesh).

### Summary
1m40s intro for Module II Week 2 of the VFX School Renaissance program. Focus: Vellum cloth simulation for the crocodile attack project. Week covers: draping cloth onto body starting from T-pose (precise fit at sim start), geometry prep (Remesh, groups, constraint setup), cloth tearing (pre-fracturing / pre-cutting), welding and stitching, full drape simulation in Vellum SOP solver, bonus stiff cloth areas (scale polygons locally to vary stiffness).

### Key Steps
- Start from T-pose of character: cloth drapes onto body to fit accurately at sim start
- Geometry prep: Remesh for triangle mesh, group assignment, constraint prep
- Pre-cut cloth for tearing + weld/stitch cloth seams together
- Full drape sim in Vellum SOP solver
- Stiff cloth areas: change polygon scale on same mesh to create locally stiff regions (tricky in Vellum otherwise)

### Houdini Nodes / VEX / Settings
- Vellum SOP solver — cloth drape simulation
- Remesh — triangle mesh for cloth
- Groups — for constraints (pin, tear, etc.)
- Weld / stitch constraints — joining cloth pieces

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[vellum, cloth, tearing, stitching, drape, remesh, course-intro, intermediate]

---

## Related Tutorials
- module-ii-week-01-02-introduction-to-vellum-v1-1080p.md (Vellum overview)
- module-ii-week-03-01-introduction-v1-1080p.md (week 3: first complete sim)
- module-ii-week-03-01-splitting-by-material-v1-1080p.md (splitting geo by material)
