---
title: Procedural HDAs for Unreal
source: YouTube
url: https://www.youtube.com/watch?v=rKcH4oIfoVw
author: Houdini.School
ingested: 2026-06-23
houdini_version: "H19+"
tags: [hda, unreal, procedural-modeling, building-generator, splines, cables, houdini-engine, ue5, materials, sessions-sync, intermediate-advanced]
extraction_status: complete
frames_dir: tutorials/frames/procedural-hdas-for-unreal/
frame_count: 4
---

# Procedural HDAs for Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=rKcH4oIfoVw)
**Author:** Houdini.School
**Duration:** 1m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** I'm Julian, I'm a technical artist at Cloud Imperium Games. I've created procedural tools for big name projects such as Star Citizen, as well as other personal pieces such as the Berlin sidewalk generator and an office table generator. In this course, I'll walk you step by step on creating your very own building generator HDA, ready for other artists to use inside of Unreal. We'll be using attractive splines or curves to start creating our building tool. Then we'll work our way to procedural modeling and create an automated cable system to add a more organic and connected feel to our scene. We're going to talk about randomizing asset creation, but at the same time maintaining enough control for art directability. We'll create a simple parameter interface that other artists can use when working with your HDA. Afterwards, we'll impart our HDA into Unreal, but we'll be accessing Unreal CI with Hidini attributes. For example, we'll be used Hidini to create systems where we can import meshes for assets bonding or an interface for procedurally assigning materials all within Unreal. And to top it all off, we'll learn how to use Sessions Sinks so that we can communicate with each other so we can further debug our tools all in real time. To learn more, head over to Hidini School.

**Frame:** tutorials\frames\procedural-hdas-for-unreal\frame_000.jpg


---

## Structured Notes

### Core Technique
Course trailer only — Houdini.School class by Julian (Cloud Imperium Games / Star Citizen): build a procedural building-generator HDA deployable in Unreal Engine via Houdini Engine, covering spline-driven modeling, procedural cable system, asset randomization + art directable controls, parameter UI for other artists, Houdini attributes exposed in Unreal (mesh import, material assignment), and Sessions Sync for real-time debugging.

### Summary
1m9s promotional trailer. Instructor is Julian, technical artist at Cloud Imperium Games (Star Citizen, Berlin sidewalk generator, office table generator). Course topics: (1) building generator HDA using splines/curves; (2) procedural modeling; (3) automated organic cable system; (4) randomized asset creation with art-director control; (5) simple parameter interface for artist-facing HDA; (6) Houdini Engine import to Unreal — Houdini attributes controlling mesh import slots and material assignment from UE side; (7) Sessions Sync for real-time Houdini↔Unreal communication and tool debugging.

### Key Steps
- (Trailer only — no step-by-step content)
- Topics: spline-based modeling → procedural building gen → cables → randomization → HDA parameter UI → Houdini Engine export → Unreal attribute-driven mesh/material → Sessions Sync

### Houdini Nodes / VEX / Settings
- HDA (Houdini Digital Asset) — packaged reusable tool
- Curve/spline SOPs — building generator base
- Houdini Engine — plugin linking Houdini HDA into Unreal
- Houdini attributes — drive Unreal-side mesh bounding / material assignment
- Sessions Sync — real-time Houdini↔Unreal communication for debugging

### Difficulty
Intermediate–Advanced

### Houdini Version
H19+

### Tags
[hda, unreal, procedural-modeling, building-generator, splines, cables, houdini-engine, ue5, materials, sessions-sync, intermediate-advanced]

---

## Related Tutorials
- procedural-growth-with-kinefx-and-the-labs-tree-tools.md (HDA + procedural pipeline)
- tuna-can-procedural-modeling-and-rig-with-kinefx.md (procedural modeling + HDA)
- scientific-phenomena-in-houdini.md (procedural SOP workflows)
