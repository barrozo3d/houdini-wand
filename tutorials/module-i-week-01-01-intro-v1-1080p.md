---
title: module i   week 01   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=ZYFlDsFBxhA
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, pyro, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-01-01-intro-v1-1080p/
frame_count: 4
---

# module i   week 01   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=ZYFlDsFBxhA)
**Author:** The VFX School Archive
**Duration:** 1m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello and welcome to week one of module one of the Renaissance course. And this is the first project that we're starting off with and we're looking at RBD bullet for module one rigid body dynamics and we're starting with a bang literally. So we've got a street scene with a kind of an explosion and the ground pushing all kind of bits of rock and rubble and you know paving into the sky with this great big explosion. So yeah obviously we're focusing on in in this week on you know getting a nice fracture and a good and good behavior from that fracture. We're not looking at constraints so much. We do use them a little bit but we're not looking at breaking so much. But we're setting up some really nice geometry making fracturing the geometry with a Boolean system so that we can get some really nice detail you know really interesting shapes very variety of big and small shapes. Then once we have our main simulation we use that as a source to set up our debris. So you know using the velocity and the size and stuff like that to source the debris so we get a nice kind of second layer and then on top of that again we use the similar source you know related to the s...

**Frame:** tutorials\frames\module-i-week-01-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Overview of a city ground explosion shot using Boolean fracture for varied chunk shapes and a three-layer debris/pyro sourcing hierarchy all driven by the same RBD simulation's velocity and piece-size attributes.

### Summary
Covers a city ground explosion with rock/rubble/paving erupting upward. The RBD focus is a Boolean fracture system for high-quality, varied chunk shapes — big and small pieces with interesting silhouettes, rather than uniform Voronoi output. Constraints are set up minimally, mainly to hold the initial state rather than to drive complex breaking behaviour. A debris-sourcing pipeline uses the main RBD sim's velocity and piece-size attributes to source a secondary debris particle layer, which in turn sources a third pyro layer — a three-layer hierarchy entirely driven by the same underlying simulation. The render pipeline uses Solaris/Karma with Megascans materials for rock/concrete.

### Key Steps
1. [`Boolean fracture`] Generate varied, high-quality chunk shapes for the ground explosion
2. [Minimal constraints] Hold initial geometry state without complex breaking logic
3. [`RBD Solver`] Run the primary destruction simulation, exporting velocity and piece-size attributes
4. [`POP Network`] Source a secondary debris particle layer from the RBD sim's attributes
5. [`Pyro Solver`] Source a third pyro layer from the debris particle layer
6. [Render] Apply Megascans rock/concrete materials; render in Solaris/Karma

### Houdini Nodes / VEX / Settings
- Boolean fracture — preferred over Voronoi here for more varied, art-directable chunk silhouettes
- Three-layer sourcing hierarchy — RBD velocity/size attributes -> debris POPs -> pyro source, all chained from one simulation
- Solaris/Karma + Megascans — render pipeline for rock/concrete surfacing

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module I)

---

## Related Tutorials
- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — the staged-activation gap-filler for this same module
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the following week's multi-material destruction
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — another debris-to-pyro sourcing hierarchy
