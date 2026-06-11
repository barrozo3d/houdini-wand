---
title: Grain vortex in Houdini tutorial
source: YouTube
url: https://www.youtube.com/watch?v=8fcfu6gmzUQ
author: raphaël
ingested: 2026-06-11
houdini_version: "Not specified (H20–H21 UI)"
tags: [dop, sop, rbd, simulation, instancing, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/grain-vortex-in-houdini-tutorial/
frame_count: 4
---

# Grain vortex in Houdini tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=8fcfu6gmzUQ)
**Author:** raphaël
**Duration:** 24m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey guys, I hope you're doing good. Today I'm going to be showing you how I made this animation in Houdini using a bullet solver. Before we start, if you want to grab the scene file for this, you can do so on my Gumroad for a couple bucks. Alright, so let's get started with a Geonode, of course, and then I'm going to bring in the Geometry I want to scatter. In my case, it's going to be a rock, but I grab from Megascans. And I'm taking the high polyversion. We're going to reduce it down to make it proxy for the simulation. And then at the end, we're going to put the high poly back onto our simulated points. Okay, so as you can see, it's massive, so we're going to need to match size it down. Let's make it two centimeters and scale to fit. Also, I want to remove some attributes I don't need. I just want to keep position normal UV and that's it. Alright, so this is going to be our high poly geo. Let's create a null for it. Whoops. Okay, and now we need a low polyversion for the sim, so let's do a poly reduce. Alright, so we currently have about a million faces, which is way too much. Let's go point O1 on the percent to keep. There we go. We now have a hundred faces, 50 points. And I th...

**Frame:** tutorials\frames\grain-vortex-in-houdini-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
Bullet RBD simulation of scattered Megascans rocks using low-poly proxies for fast simulation, a custom vortex force field, and high-poly copy-back for final rendering — with initial rock arrangement forming a custom shape (smiley face) that then dissolves into a vortex scatter.

### Summary
A 25-minute intermediate tutorial building a vortex grain animation: a Megascans rock is reduced to a ~100-face proxy via `polyreduce`, scattered across a flat plane in a custom shape pattern, then simulated with Bullet RBD using a vortex/tornado velocity force. Post-sim, the high-poly mesh is restored onto simulated point positions and orientations for rendering. Frames show the smiley face arrangement mid-collapse into the scatter vortex.

### Key Steps
1. Import Megascans rock (high poly) → `matchsize` SOP → scale to 2cm, `matchsize` → Scale to Fit
2. `attribdelete` SOP — remove all attributes except `P`, `N`, `uv`
3. `polyreduce` SOP — set "Percent to Keep" to 0.01% → ~100 faces / 50 points proxy
4. Create null for high-poly reference, work with proxy downstream
5. `scatter` or `copytopoints` SOP — distribute proxy rocks across ground plane
6. Arrange initial shape using attribute mask or SDF-based selection (smiley face pattern visible)
7. `rbdpackedobjects` or `assemble` SOP — pack geometry for Bullet simulation
8. Bullet RBD DOP network — add custom vortex velocity via `popadvectbyvolumes` or VEX wrangle on `popforceField`
9. Simulate; cache to disk for playback
10. Post-sim: `copytopoints` or `unpackpoints` — transfer high-poly mesh onto simulated proxy positions/orientations using `orient` attribute

### Houdini Nodes / VEX / Settings
- `matchsize` SOP — Scale to Fit mode, target size 2cm
- `attribdelete` SOP — keep only `P`, `N`, `uv`
- `polyreduce` SOP — Percent to Keep: 0.01% → ~100 faces
- `assemble` or `rbdpackedobjects` SOP — pack geo for RBD
- `bulletrbdsolver` DOP
- `staticobject` DOP — ground collision plane
- Velocity/vortex force: `popadvectbyvolumes` or custom `gasfieldupdateattribs` wrangle
- `copytopoints` SOP — high-poly restore post-sim using `orient` + `P` from cache
- `unpackpoints` SOP — optional unpack for final mesh

### Difficulty
Intermediate

### Houdini Version
Not specified (H20–H21 UI)

### Tags
dop, sop, rbd, simulation, instancing, procedural, intermediate

---

## Related Tutorials
- [[intro-to-houdini-for-vfx---beginner-course]] — SOP and DOP foundational workflow
- [[houdini-tutorial---simple-disintegration-fx]] — Similar destruction/scatter aesthetic using different solver approach
- [[introduction-to-particles-in-houdini-21-full-beginner-course-2026]] — RBD + particle instancing pipeline
