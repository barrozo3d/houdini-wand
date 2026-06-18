---
title: Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants
source: YouTube
url: https://www.youtube.com/watch?v=xjf_mQKI3R8
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["procedural", "nature", "plants", "flowers", "organic", "modeling", "art-direction", "instancing", "no-simulation"]
extraction_status: complete
frames_dir: tutorials/frames/yan-paul-dubbelman-procedural-nature-procedural-living-plants/
frame_count: 0
---

# Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants

**Source:** [YouTube](https://www.youtube.com/watch?v=xjf_mQKI3R8)
**Author:** Houdini.School
**Duration:** 73m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en The big goal of this this session is to [snorts] to show you how easy it can be and Houdini need to build these flowers and plants and natural elements. If you know my portfolio, you can see that it's full of flowers and plants and I'm doing a lot of trees now as well. And using Houdini is for me the most straightforward way of getting there. And most people when they think about Houdini, they think about these simulations and a lot of coding. And there's like this Houdini wall that people seem to get stuck on, but what we're going to do today is a lot more straightforward. Step by step should be easy enough to follow along. No simulations, so you won't have to you don't you won't have to make your computer go too crazy. We're just going to do pretty easy straightforward steps. But you can see how when you add these different layers of complexity, you can get to something quite natural and beautiful, but also very easy to use and easy to iterate on. And a big part of my personal Houdini journey has been figuring out how I can make tools and make effects and make models that fit with my own artistic vision. And for me, it's very important that the softwar...

**Frame:** (no frames available)

---

## Structured Notes

### Core Technique
Building procedural flowers, plants, and natural elements in Houdini without any simulations — using layered SOP geometry operations that are easy to follow, fast to iterate, and designed to match the artist's personal visual vision.

### Summary
Yan Paul Dubbelman presents a 74-minute accessible introduction to building procedural botanical elements (flowers, plants, natural forms) in Houdini. The session is explicitly designed to break down the intimidating "Houdini wall" — the misconception that Houdini requires simulations and heavy coding for natural work. No simulations are used at all; everything is SOP-level procedural geometry with layered complexity. The teaching philosophy is step-by-step accessibility combined with iterability, matching Dubbelman's portfolio of calm, natural, exhibition-quality botanical work. The session reflects his personal artistic journey of building tools that express his visual vision.

### Key Steps
1. Start with a single simple SOP primitive as the structural base (line, circle, curve)
2. Build a first layer of complexity — a single petal or leaf element using curves and surfaces
3. Use Copy to Points SOP to distribute petal instances around a circular arrangement
4. Add per-instance variation using attributes (scale, rotation, color offset)
5. Build the stem/branch structure as a separate SOP chain
6. Layer complexity: add secondary flower structures, stamen, pistil elements
7. Combine all elements into a full plant assembly
8. Add final variation controls so the plant can be randomized easily

### Houdini Nodes / VEX / Settings
- Curve SOP (petal/leaf profiles)
- Skin / Loft SOP (surface from curves)
- Copy to Points SOP (petal instancing)
- Attribute Randomize SOP
- Transform SOP (per-instance variation)
- Merge SOP (assembling plant parts)
- Attribute Wrangle (VEX for fine variation)
- VEX: fit(), noise(), smooth(), rand()

### Difficulty
Beginner

### Houdini Version
unspecified

### Tags
procedural, nature, plants, flowers, organic, modeling, art-direction, instancing, no-simulation

---

## Related Tutorials
- [Yan Paul Dubbelman | Procedural Nature | High-Quality Custom Leaves](yan-paul-dubbelman-procedural-nature-high-quality-custom-leaves.md) — companion session by same author on high-quality leaf models and Copernicus texturing
- [Experimental Motion - CHOPS](experimental-motion---chops.md) — Yan Paul's CHOPS session for adding smooth, calm motion to these procedural plants
- [Experimental Motion - The SOP Solver](experimental-motion---the-sop-solver.md) — Yan Paul's SOP Solver session for adding living, evolving behavior to procedural forms
