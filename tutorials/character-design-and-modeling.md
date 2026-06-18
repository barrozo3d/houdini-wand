---
title: Character Design and Modeling
source: YouTube
url: https://www.youtube.com/watch?v=4tJmvGrhxA4
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["modeling", "character", "vdb", "boolean", "polygon", "character-design", "animation", "procedural"]
extraction_status: complete
frames_dir: tutorials/frames/character-design-and-modeling/
frame_count: 4
---

# Character Design and Modeling

**Source:** [YouTube](https://www.youtube.com/watch?v=4tJmvGrhxA4)
**Author:** Houdini.School
**Duration:** 0m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello fellow Houdini scholars. My name is Christopher Rutledge and I'm a CG artist and short filmmaker who primarily uses Houdini to make character-based films and in this course I'm gonna be walking through the process of creating a character in Houdini from concept art to full 3D model and in this class I'm gonna show a range of techniques that I developed for designing and creating original characters. We'll start off by designing and sketching our character ideas and then using these sketches as a guide we'll then block out the body and the eyes using polygons and a number of VDB, Boolean and reshape operations we'll also be taking a number of different concepts and methods commonly used in 2D hand drawn animation and translating them into Houdini in fun ways. I think you'll all have fun in this class while learning a lot of unique Houdini tricks that I developed while designing characters over the years to learn more vis-a-m-e class at Houdini.school

**Frame:** tutorials\frames\character-design-and-modeling\frame_000.jpg


---

## Structured Notes

### Core Technique
Full character creation pipeline in Houdini from concept sketches to finished 3D model, using polygon modeling, VDB, Boolean, and reshape operations, with 2D hand-drawn animation concepts translated into 3D techniques.

### Summary
Christopher Rutledge (CG artist and short filmmaker) teaches a Houdini.School course on creating original characters entirely within Houdini. The workflow starts with concept sketching and design, then moves to blocking out the body and eyes using polygons alongside VDB, Boolean, and reshape operations. A distinctive element is the translation of 2D hand-drawn animation techniques into Houdini workflows, giving character models expressive, stylized properties. The course presents unique tricks Rutledge developed over years of character-based filmmaking in Houdini.

### Key Steps
1. Sketch and finalize character design concepts (traditional or digital sketches)
2. Import sketches into Houdini as image planes for reference
3. Block out the body using polygon primitives and box-modeling techniques
4. Refine forms using VDB operations (convert to VDB, reshape, smooth)
5. Apply Boolean operations to combine or subtract shapes for complex areas
6. Model the eyes and expressive facial features using polygons
7. Incorporate 2D animation concepts (squash/stretch, silhouette) translated into 3D geometry operations
8. Clean up topology for final model readiness

### Houdini Nodes / VEX / Settings
- Polygon modeling tools (PolyExtrude, PolyBevel, PolyCap)
- VDB from Polygons
- VDB Reshape
- Boolean SOP
- PolyReduce / QuadRemesh
- File SOP (image reference import)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
modeling, character, vdb, boolean, polygon, character-design, animation, procedural

---

## Related Tutorials
- [Tuna Can | procedural modeling and rig with KineFX](tuna-can-procedural-modeling-and-rig-with-kinefx.md) — procedural modeling pipeline in Houdini with practical SOP techniques
- [Simulated Creatures](simulated-creatures.md) — animating and simulating organic character objects in Houdini using FEM
- [From C4D to Houdini](from-c4d-to-houdini.md) — foundational Houdini modeling and attribute workflows for artists coming from other 3D tools
