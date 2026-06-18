---
title: Procedural HDAs for Unreal
source: YouTube
url: https://www.youtube.com/watch?v=rKcH4oIfoVw
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["hda", "unreal-engine", "procedural", "splines", "building-generator", "houdini-engine", "session-sync", "materials", "pipeline"]
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
**Transcript:** Kind: captions Language: en I'm Julian I'm a technical artist at Cloud emperium games I've created procedural tools for bigname project such as Star Citizen as well as other personal pieces such as the Berlin sidewalk generator and office table generator in this course I'll walk you step by step on creating your very own building generator HDA ready for other artists to use inside of unreal we'll be using interactive splines or Curves to start creating our building tool then we'll work our way to procedural modeling and create an automated cable system to add a more organic and connected feel to our scene we're going to talk about randomizing asset creation but at the same time maintaining enough control for our direct ability we'll create a simple parameter interface that other artists can use when working with your HDA afterwards we will import our HDA into unreal or we'll be accessing unreal sui with Houdini attributes for example will we use Houdini to create systems where we can import meshes for asset spawning or an interface for procedurally assigning materials all within unreal and to top it all off we will learn how to use session sync so udini and unreal can communicate w...

**Frame:** tutorials\frames\procedural-hdas-for-unreal\frame_000.jpg


---

## Structured Notes

### Core Technique
Building a procedural building generator HDA in Houdini — from interactive splines through procedural modeling and randomized asset creation — then deploying it to Unreal Engine via Houdini Engine with full Session Sync communication.

### Summary
Julian (Technical Artist at Cloud Imperium Games, creator of tools for Star Citizen) teaches a step-by-step course on building a production-ready procedural building generator HDA. The workflow uses interactive splines/curves as the building footprint input, procedurally models the structure, adds an automated cable system, and exposes a user-friendly parameter interface. The HDA is then imported into Unreal Engine where Houdini attributes control mesh spawning, material assignment, and Session Sync enables live two-way communication between Houdini and Unreal for iterative development.

### Key Steps
1. Design the HDA architecture and define what parameters artists will need
2. Build the interactive spline/curve input for building footprint definition
3. Create procedural modeling logic driven by the spline (walls, floors, details)
4. Build an automated cable/wire generation system for organic scene detailing
5. Add randomization with art-direction controls for asset variation
6. Design a clean parameter interface (folders, labels, sensible defaults)
7. Export/save the HDA for use in Unreal Engine
8. Import the HDA via the Houdini Engine plugin in Unreal
9. Access Houdini attributes from Unreal — mesh import, material assignment
10. Set up Session Sync for live Houdini-Unreal communication during development

### Houdini Nodes / VEX / Settings
- Houdini Digital Asset (HDA) creation
- Curve SOP / Bezier Curve input
- PolyExtrude / PolyBevel SOP
- Copy to Points SOP (randomized assets)
- Attribute Randomize SOP
- Cable/curve sweep system
- HDA parameter interface editor
- Houdini Engine plugin (Unreal)
- Session Sync (Houdini ↔ Unreal)
- Houdini attributes in Unreal (unreal_material, unreal_instance, etc.)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
hda, unreal-engine, procedural, splines, building-generator, houdini-engine, session-sync, materials, pipeline

---

## Related Tutorials
- [Houdini FX in Unreal](houdini-fx-in-unreal.md) — complete Houdini-Unreal virtual production pipeline covering environment modeling and rendering
- [Effective TD](effective-td.md) — HDA creation workflow and Python UI automation for artist-facing tools
- [Tuna Can | procedural modeling and rig with KineFX](tuna-can-procedural-modeling-and-rig-with-kinefx.md) — procedural SOP modeling techniques used in building HDAs
