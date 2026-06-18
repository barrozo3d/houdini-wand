---
title: Loops
source: YouTube
url: https://www.youtube.com/watch?v=OQDFQtoTOuA
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["loops", "sop", "vop", "vex", "for-each", "while", "procedural", "fundamentals", "beginner"]
extraction_status: complete
frames_dir: tutorials/frames/loops/
frame_count: 4
---

# Loops

**Source:** [YouTube](https://www.youtube.com/watch?v=OQDFQtoTOuA)
**Author:** Houdini.School
**Duration:** 0m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, my name is David Torno and in this new class, I'm going to teach you all about repetitive node processing. This is also known as a process loop. To help you mystify this topic, I'll be taking you through various contexts of Houdini, breaking down how to use a 4, 4 each, while, and a 2-while loop. These process loops can take a few forms within Houdini, so I will be going over SOPS, VOPs, and VEX in order to help you get more comfortable with implementing loops into your workflows. Loop is going to apply to a wide range of tasks, which is why I've put together a collection of fully finished builds, as well as technical examples. This will help better illustrate the options you have. To learn more, head over to Houdini.school today.

**Frame:** tutorials\frames\loops\frame_000.jpg


---

## Structured Notes

### Core Technique
Comprehensive coverage of repetitive node processing (loops) across Houdini's three main contexts — SOPs, VOPs, and VEX — covering for, for-each, while, and do-while loop types with practical finished builds.

### Summary
David Torno (Houdini.School instructor, also teaches Attributes) presents a focused course demystifying loops in Houdini. The course covers all four loop types (for, for-each, while, do-while) across SOPs, VOPs, and VEX contexts, giving students a complete picture of where and how to use repetitive processing in Houdini workflows. Both complete finished builds and abstract technical examples are provided so students understand both the practical application and the underlying mechanics. The broad scope means loops for geometry processing, shader networks, and VEX code are all addressed.

### Key Steps
1. Understand what a process loop is and why Houdini needs them
2. Learn the For loop in SOPs using the For-Each Begin/End network
3. Learn the For-Each loop iterating over pieces, primitives, or points in SOPs
4. Explore the While and Do-While loop concepts in VOPs
5. Implement for loops in VEX using standard C-style syntax
6. Implement for-each and while loops in VEX
7. Compare SOP loop, VOP loop, and VEX loop approaches for the same task
8. Study the finished build examples to see loops applied to real-world setups

### Houdini Nodes / VEX / Settings
- For-Each Begin / For-Each End (SOP)
- For-Each Begin (Number) / (Primitives) / (Points)
- Block Begin / Block End SOP
- VOP network loop nodes
- Attribute Wrangle with VEX loops
- VEX: for(), while(), do-while()
- Feedback iteration in For-Each loops

### Difficulty
Beginner

### Houdini Version
unspecified

### Tags
loops, sop, vop, vex, for-each, while, procedural, fundamentals, beginner

---

## Related Tutorials
- [Attributes](attributes.md) — David Torno's foundational attributes course; loops and attributes pair naturally in Houdini workflows
- [Procedural Growth with KineFX and the Labs Tree Tools](procedural-growth-with-kinefx-and-the-labs-tree-tools.md) — iterative growth systems heavily rely on for-each loops in SOPs
- [Maths for Artists](maths-for-artists.md) — mathematical foundation that explains the theory behind iterative computations
