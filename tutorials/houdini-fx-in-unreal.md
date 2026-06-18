---
title: Houdini FX in Unreal
source: YouTube
url: https://www.youtube.com/watch?v=RDiA2R47Wzo
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["unreal-engine", "virtual-production", "hda", "megascans", "rendering", "aces", "substance-painter", "procedural", "pipeline"]
extraction_status: complete
frames_dir: tutorials/frames/houdini-fx-in-unreal/
frame_count: 4
---

# Houdini FX in Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=RDiA2R47Wzo)
**Author:** Houdini.School
**Duration:** 4m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en my name is Guido poncini and I am extremely happy to introduce you to my course Houdini effects in a real engine throughout this course we will explore the key techniques that are used to create sequence scg sequence designed for virtual production installation with this particular course in mind in our first session we will cover the main techniques used to model a location inspired by a real workplace the Maxi Museum in Rome will go over the basics of modeling techniques procedural UV mapping and importing your meshes into unreal once inside unreal we will discuss how to organize your project in folders how to work with a main sequence and subsequences and understand our unreal and Houdini systems work together and also how they differ we will also see how to apply Mega scans materials create an hdri base the lighting for the interior how to set up your lighting and post processing and prepare your render in Aces color space just ready to export in XR sequence that you will be able to import in your DaVinci Resolve session we will then explore how I transformed a Shark model into a procedural robot and how I textured it inside substance painter finally...

**Frame:** tutorials\frames\houdini-fx-in-unreal\frame_000.jpg


---

## Structured Notes

### Core Technique
Creating a complete virtual production pipeline using Houdini and Unreal Engine together — from procedural modeling and HDAs in Houdini to scene assembly, lighting, and rendering in Unreal Engine with ACES color space and DaVinci Resolve delivery.

### Summary
Guido Poncini presents a comprehensive course on integrating Houdini with Unreal Engine for virtual production and installation sequences. The course uses the Maxi Museum in Rome as the location reference, covering procedural modeling and UV mapping in Houdini, import into Unreal, scene organization with sequences and subsequences, Megascans material application, HDRI-based lighting, and ACES color space setup for final export. A unique segment covers transforming a shark model into a procedural robot using Houdini, textured in Substance Painter. The Houdini Engine / Session Sync connection between both applications is also demonstrated.

### Key Steps
1. Model the location environment (museum interior) using Houdini procedural modeling
2. Set up procedural UV mapping on all meshes in Houdini
3. Import geometry into Unreal Engine and organize assets in folders
4. Set up a main sequence with subsequences for multi-shot organization
5. Configure Houdini Engine Session Sync between Houdini and Unreal
6. Apply Megascans materials to environment geometry in Unreal
7. Create HDRI-based interior lighting and set up post-processing
8. Configure ACES color space for export
9. Export the rendered sequence as EXR for import into DaVinci Resolve
10. Build the procedural robot from a shark base model in Houdini and texture in Substance Painter

### Houdini Nodes / VEX / Settings
- Houdini Engine (Unreal plugin)
- Session Sync (Houdini–Unreal live link)
- Houdini Digital Asset (HDA)
- UV Unwrap / UV Flatten SOP
- Procedural UV mapping
- Megascans materials (Unreal)
- HDRI / Skylight (Unreal)
- ACES color space (Unreal post-process)
- Sequencer (Unreal main/subsequences)
- Substance Painter (external texturing)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
unreal-engine, virtual-production, hda, megascans, rendering, aces, substance-painter, procedural, pipeline

---

## Related Tutorials
- [Procedural HDAs for Unreal](procedural-hdas-for-unreal.md) — focused course on building and deploying HDAs inside Unreal Engine
- [Effective TD](effective-td.md) — covers HDA creation and optimization workflow, foundational for Houdini-Unreal pipeline
- [Procedural Growth with KineFX and the Labs Tree Tools](procedural-growth-with-kinefx-and-the-labs-tree-tools.md) — procedural vegetation that can be exported to Unreal environments
