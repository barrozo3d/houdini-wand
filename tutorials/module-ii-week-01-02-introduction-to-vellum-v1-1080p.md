---
title: module ii   week 01   02   introduction to vellum v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=LKhBUByCqJw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, cloth, particles, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-02-introduction-to-vellum-v1-1080p/
frame_count: 4
---

# module ii   week 01   02   introduction to vellum v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=LKhBUByCqJw)
**Author:** The VFX School Archive
**Duration:** 15m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right, so let's go ahead and create a new project right from the get-go. I'm just going to call this uh croc croc attack. Um and put this in my D Oops. D drive. Let's see. I'll leave them as as they are. Doesn't matter. Okay, click accept and then save that. Okay, in hip and then find find that project. And let's give it the same name. uh croc attack version 1.hip Good to go. Now I'm just going to get rid of this um original one in the middle. I don't It's a bit distracting. So, what I want to do for the first um lesson here is just a very quick overview of some of the some of the possibilities with Vellum. Okay, so I'm just going to drop a geo here. I'm just going to throw together some random um kind of bits and bobs with Vellum. Okay? So, let's call this um Vellum intro. Jump inside. Okay? I'm just going to drop a grid right off the get-go. Okay, and then typically Vellum likes to work with triangles. You know, well, I do you just kind of get better folds and things with triangles. So, I'm going to drop a remesh. It's going to give me some nice triangles and you know, some something that's less uniform. And you know, it's not kind of all the same. So,...

**Frame:** tutorials\frames\module-ii-week-01-02-introduction-to-vellum-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
A comprehensive Vellum fundamentals lesson demonstrating cloth, string/wire and grains setups, with the Vellum Solver shown as a single DOP network that resolves all Vellum object types together with shared collision.

### Summary
Setup: a new project "croc_attack" with a "vellum_intro" geometry node. Cloth: grid -> Remesh (to triangulate for better folds) -> Vellum Cloth SOP (via shelf or tab), with bend stiffness, stretch stiffness and mass as the key parameters. Pinning is done by grouping the top edge and attaching it to geometry, or using Vellum Attach to Geometry. String/wire: a curve feeds Vellum String SOP, with wire stiffness distinguishing cable-like from rope-like behaviour. Grains: scattered points feed Vellum Grains SOP, with friction, restitution and pscale as key parameters. The Vellum Solver setup always lives inside a DOP network and reads all Vellum object types together, resolving them with shared collision. Increasing substeps improves accuracy but scales simulation time linearly. The key tip given is to always remesh cloth geometry before Vellum, since quad-dominant meshes produce poor fold quality.

### Key Steps
1. [`Remesh SOP`] Triangulate grid geometry before applying Vellum Cloth
2. [`Vellum Cloth SOP`] Set bend stiffness, stretch stiffness and mass
3. [Pinning] Group the top edge; attach via geometry group or Vellum Attach to Geometry
4. [`Vellum String SOP`] Convert a curve to a wire; tune wire stiffness for cable vs. rope behaviour
5. [`Vellum Grains SOP`] Scatter points; tune friction, restitution and pscale
6. [`Vellum Solver`] Combine cloth, string and grains in one DOP network with shared collision
7. [Substeps] Increase substeps for accuracy, noting the linear cost increase

### Houdini Nodes / VEX / Settings
- `Remesh SOP` — required pre-step for cloth; quad-dominant meshes fold poorly in Vellum
- `Vellum Cloth SOP` — bend stiffness, stretch stiffness, mass
- `Vellum String SOP` — wire stiffness differentiates cable vs. rope behaviour
- `Vellum Grains SOP` — friction, restitution, pscale
- `Vellum Solver` (single DOP network) — resolves all Vellum types together with shared collision; substep count trades accuracy for sim time

### Difficulty
Intermediate

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)

---

## Related Tutorials
- [Vellum Module Intro: Crocodile Attack Overview](module-ii-week-01-01-introduction-v1-1080p.md) — the overview lesson this gap-filler expands on
- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — applies these cloth fundamentals to a full draping workflow
- [Introduction to Grains](module-i-week-06-01-introduction-to-grains-v1-1080p.md) — the earlier course's parallel grains-only lesson
