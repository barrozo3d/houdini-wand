---
title: module ii   week 04   01   introduction v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=SlbMugY762Q
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, particles, rendering, karma, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-04-01-introduction-v1-1080p/
frame_count: 4
---

# module ii   week 04   01   introduction v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=SlbMugY762Q)
**Author:** The VFX School Archive
**Duration:** 1m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, welcome to week four of module two, the last we're at the last week now, so we're bringing everything together and getting a nice render result at the end. Um you know, seeing the the results of all of our hard work. So, obviously this week we're tackling the grains and we're starting out by building a good um source geometry. So, to kind of save um unnecessary simulation time wasting simulation time, we're going to build a source geometry based on our previous simulation. So, using the weather crocodile and the hunter go to generate a um a kind of block or an area for for to generate the the uh grains and because this happens over time, we need to use the solver nodes to do that, right? Um so, that's a neat little trick to to kind of save you some time and be be more efficient, which is always good. Um then we jump in and build our uh build our simulation network in the in DOPs from scratch. I think we used the um the shelf tool at the beginning, but this time, you know, we just build it up from scratch. It's not too complicated. Then um we get our nice high-res sim and uh up-res the simulation, so getting a bit more detail for free without having t...

**Frame:** tutorials\frames\module-ii-week-04-01-introduction-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Sourcing grains from the contact regions of the existing crocodile/hunter Vellum simulation rather than scattering across the whole scene, then up-resing the grain sim for final render quality.

### Summary
The final Vellum week covers grains simulation and full render. The grain-sourcing efficiency trick uses the previous Vellum simulation (crocodile + hunter) to generate a time-varying source volume: as the croc thrashes and the hunter is squeezed, the contact region emits grains, driven by a SOP Solver or DOP stamp inside the grains network. The grain network is built from scratch in DOPs rather than from the shelf tool this time: Vellum Grains Source + Vellum Solver + Vellum Constraint. An up-res technique runs a low-res grain sim first for timing/behaviour, then re-sims at high pscale with finer constraint sub-steps for render-quality results. The final render uses Karma XPU with Megascans materials for ground/mud.

### Key Steps
1. [Contact-driven sourcing] Derive a time-varying grain source volume from the croc/hunter Vellum sim's contact regions
2. [`SOP Solver` / DOP stamp] Drive grain emission timing from the existing sim rather than a fixed scatter
3. [Vellum Grains network] Build from scratch in DOPs: Vellum Grains Source + Vellum Solver + Vellum Constraint
4. [Low-res pass] Simulate grains at low resolution first to confirm timing and behaviour
5. [Up-res pass] Re-simulate at high pscale with finer sub-steps for render quality
6. [Render] Apply Megascans ground/mud materials; render in Karma XPU

### Houdini Nodes / VEX / Settings
- Contact-driven grain sourcing — deriving emission volume/timing from an existing simulation's contact regions rather than static scatter
- Vellum Grains Source / Vellum Solver / Vellum Constraint — built manually in DOPs for full control
- Up-res workflow — low-res timing pass followed by a high-pscale, finer-substep render pass
- Karma XPU — final renderer with Megascans ground/mud materials

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)

---

## Related Tutorials
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the preceding week's combined sim this grain pass sources from
- [Introduction to Grains](module-i-week-06-01-introduction-to-grains-v1-1080p.md) — the earlier course's foundational Vellum Grains lesson
- [Tabletop Week 01 Intro](w01-01-introduction-v1-1080p.md) — another instancing/particle-heavy render pipeline for comparison
