---
title: module i   week 01   01   your first houdini project v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Mq1snWFUBj0
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [sop, lop, solaris, karma, rendering, beginner]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-01-01-your-first-houdini-project-v1-1080p/
frame_count: 4
---

# module i   week 01   01   your first houdini project v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=Mq1snWFUBj0)
**Author:** The VFX School Archive
**Duration:** 9m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello and welcome to the Houdini Renaissance Program Volume 1. This is the updated version. So we're working in Houdini 18.5. So we're going to be using all the new tools and workflows that have been um uh implemented by by Side Effects. For this first project, we're focusing on modeling. Um and we're just looking at the basis of modeling and a bit of an introduction to Houdini. Uh we're going to be uh lighting rendering um adding materials in the new um Solaris uh context and rendering with the new render engine Karma. Um and then we're going to be doing a little bit of compositing in uh Nuke and we'll end up with a really uh uh beautiful render at the end and a nice kind of basis to understanding Houdini. Okay, so here we are in Houdini. Um, if your layout doesn't look the same as mine, then just head up here and go to build. Um, it should be on this by default. So, in case you know it looks different, then you can come here, um, set it to build, and then, you know, we'll be back at the default. So, um, to introduce everything here, maybe we'll start just by dropping a sphere. So, just come here, um, click on sphere, and then just press enter. Um, if y...

**Frame:** tutorials\frames\module-i-week-01-01-your-first-houdini-project-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Introducing the updated Renascence Program Volume 1, working in Houdini 18.5 — the first version to include the Solaris context and Karma renderer — and establishing the course's SOP-to-render pipeline.

### Summary
Sets up the default "build" desktop layout and drops a sphere to introduce the basic SOP geometry workflow. Week 1's project is procedural modelling of a scattering-based scene, followed by lighting/materials in Solaris (the new USD-based context), rendering with Karma (the new render engine), and a light comp pass in Nuke. Establishes the course pipeline: SOP geometry -> Solaris LOP -> Karma render -> Nuke comp. This was the first VFX School program to adopt Solaris/Karma; earlier Film FX Season 1 lessons used only Mantra.

### Key Steps
1. [Desktop] Use the default "build" layout for the session
2. [`Sphere SOP`] Drop a sphere to demonstrate basic SOP geometry creation
3. [Procedural modelling] Build the week's scattering-based scene in SOPs
4. [Solaris LOP] Move geometry into the USD-based Solaris context for lighting/materials
5. [Karma render] Render the staged scene using the Karma engine
6. [Nuke comp] Take the Karma render into Nuke for a light compositing pass

### Houdini Nodes / VEX / Settings
- `Sphere SOP` — first geometry node used to demonstrate the SOP workflow
- Solaris (LOP context) — new in H18.5; USD-based staging context for lighting/materials/cameras
- Karma — new renderer introduced alongside Solaris in H18.5, replacing Mantra for this course's pipeline
- Pipeline pattern: SOP geometry -> Solaris LOP -> Karma render -> Nuke comp

### Difficulty
Beginner

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)

---

## Related Tutorials
- [Weeks Overview](00-weeks-overview-v1-1080p.md) — the earlier Film FX course that used Mantra instead of Solaris/Karma
- [Creating a New Project](module-i-week-02-01-creating-a-new-project-v1-1080p.md) — the following week's scattering project
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — continues the H18.5 Renascence pipeline
