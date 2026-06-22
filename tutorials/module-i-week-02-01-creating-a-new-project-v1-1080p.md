---
title: module i   week 02   01   creating a new project v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Mjw4gT36Ub4
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [sop, instancing, attributes, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-01-creating-a-new-project-v1-1080p/
frame_count: 4
---

# module i   week 02   01   creating a new project v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=Mjw4gT36Ub4)
**Author:** The VFX School Archive
**Duration:** 1m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hi guys, welcome to week two. So this week we're looking at um scatters. So scattering objects over a over a surface. In this case, over this head. Um we're going to I've got three projects that I that I created here. We're just going to do the two. So we'll start off with this one on the left where we you know we build our geometry within Houdini. Um the the the geometry that we scatter. Um and then we're looking at a couple of new nodes as well and new workflows within Houdini which has really made things much easier now um you know different ways of controlling how we scatter objects. Uh and then we'll finish up by um recreating this head on the right uh where we use Mega Scans models to um reproduce this kind of effect here which is really cool. Okay. So, I'm just going to hide that. And I've got a fresh um Houdini scene open. So, as per usual, we'll create a new project. Let's call this one uh week uh sorry week two. And I'll call it no, let's call it scatters or scatter. Scatterer. Scatter. Perfect. Let's copy that. And then I'm going to save that to my Oops. into uh D. Okay, I'm just checking. Yeah, we can leave all them. Accept that. And then sav...

**Frame:** tutorials\frames\module-i-week-02-01-creating-a-new-project-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Scattering geometry over a head surface using two parallel approaches: building scatter elements entirely inside Houdini, and instancing Megascans models via the Quixel Bridge workflow.

### Summary
This week's focus is scattering objects over a surface — specifically distributing elements over a head mesh. Two sub-projects are introduced: building the scattered geometry entirely inside Houdini, and using Megascans models as instanced scatter elements through a Quixel Bridge workflow. New H18.5 scatter-related nodes and improved Copy to Points workflows are introduced. The head surface is the distribution surface, with attributes like `pscale`, `orient` and `Cd` controlling per-instance variation. The week's deliverable is a moss/plant-covered head scene rendered in Karma.

### Key Steps
1. [`Scatter SOP`] Distribute points across the head surface
2. [`Attribute Wrangle`] Set `pscale`, `orient` and `Cd` per point for instance variation
3. [Megascans / Quixel Bridge] Import Megascans models as alternate instance geometry
4. [`Copy to Points SOP`] Instance geometry (built-in or Megascans) onto the scattered points
5. [Render] Light and render the moss/plant-covered head in Karma

### Houdini Nodes / VEX / Settings
- `Scatter SOP` — distributes points over the head surface for instancing
- `Copy to Points SOP` (H18.5 improved workflow) — instances geometry per point, reading `pscale`/`orient`/`Cd`
- Quixel Bridge / Megascans — external asset library imported as instanced scatter geometry
- `Attribute Wrangle` — randomizes per-instance attributes for natural variation

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)

---

## Related Tutorials
- [Your First Houdini Project](module-i-week-01-01-your-first-houdini-project-v1-1080p.md) — the preceding week establishing the course pipeline
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — the following week's cloud/volume work
- [Module I Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — another attribute-driven per-piece technique from a later module
