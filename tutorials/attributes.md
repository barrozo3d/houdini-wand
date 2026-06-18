---
title: Attributes
source: YouTube
url: https://www.youtube.com/watch?v=VM3m52SHUrk
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["attributes", "geometry", "vex", "rbd", "flip", "vellum", "crowds", "fundamentals", "beginner"]
extraction_status: complete
frames_dir: tutorials/frames/attributes/
frame_count: 4
---

# Attributes

**Source:** [YouTube](https://www.youtube.com/watch?v=VM3m52SHUrk)
**Author:** Houdini.School
**Duration:** 2m35s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hi my name is David torno and this is my new Houdini dot school class called attributes attributes are the heart and soul of Houdini so many beginners and even intermediate users stumble over the importance of knowing the ins and outs of attributes understanding this topic is vital to getting the most out of Houdini itself my goal is to give you a much deeper understanding of attributes so I have broken down this class into smaller topics this way I can take you step by step from the core geometry component foundations to common workflows as well as reading and writing attributes from scratch I'll take you through examples of actual attribute implementations relating to RBD flip Vellum crowd Sim and show some viewport GL attributes in session one you will be shown the core geometry components and how they relate to attributes you'll also be given some clarity to confusing terminology plus learn what attribute classes and types you have available also covered will be a full explanation of the geometry spreadsheet plus some tips on how you can sort through all of the data that it presents I'll run you through what intrinsics are how they can be accessed an...

**Frame:** tutorials\frames\attributes\frame_000.jpg


---

## Structured Notes

### Core Technique
Deep-dive exploration of Houdini attributes — their types, classes, reading/writing patterns, and practical use across multiple simulation contexts including RBD, FLIP, Vellum, and crowds.

### Summary
David Torno (Houdini.School instructor) presents a comprehensive course on Houdini attributes, structured as step-by-step sessions covering geometry component foundations through advanced attribute workflows. The course clarifies terminology, explains attribute classes and types, details the geometry spreadsheet, and covers intrinsics. Practical implementation examples are drawn from RBD, FLIP, Vellum, and crowd simulations, making the knowledge directly applicable across Houdini's major simulation contexts. Viewport GL attributes for visualization are also covered.

### Key Steps
1. Learn the core geometry components (points, vertices, primitives, detail) and their relationship to attributes
2. Understand attribute classes (point, vertex, primitive, detail) and data types (float, integer, vector, string, etc.)
3. Navigate and sort data in the Geometry Spreadsheet
4. Learn how to access and read intrinsic attributes
5. Read and write attributes from scratch using Attribute Wrangle and related nodes
6. Apply attributes in RBD simulation contexts for collision and constraint control
7. Use attributes in FLIP fluid simulations for emission and viscosity
8. Implement Vellum attributes for constraint and pin control
9. Set up crowd simulation attributes for agent behavior
10. Configure viewport GL attributes for visual feedback in the 3D viewport

### Houdini Nodes / VEX / Settings
- Attribute Wrangle (SOP)
- Attribute Create
- Attribute Promote
- Attribute Transfer
- Geometry Spreadsheet
- Intrinsic attributes
- Viewport GL attributes (gl_lit, gl_color, etc.)
- RBD simulation attributes
- FLIP fluid attributes
- Vellum constraint attributes
- Crowd simulation attributes

### Difficulty
Beginner

### Houdini Version
unspecified

### Tags
attributes, geometry, vex, rbd, flip, vellum, crowds, fundamentals, beginner

---

## Related Tutorials
- [Loops](loops.md) — David Torno also teaches loops in SOPs, VOPs, and VEX; pairs naturally with attribute workflows
- [Noise](noise.md) — noise heavily uses and drives attributes; natural follow-on to attributes fundamentals
- [Problem-Space](problem-space.md) — advanced manipulation of attributes in world/object/rest space
