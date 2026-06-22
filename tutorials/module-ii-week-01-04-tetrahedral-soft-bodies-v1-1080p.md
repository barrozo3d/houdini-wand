---
title: module ii   week 01   04   tetrahedral soft bodies v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=pxWRHQjHpNk
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, rigging, simulation, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p/
frame_count: 4
---

# module ii   week 01   04   tetrahedral soft bodies v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=pxWRHQjHpNk)
**Author:** The VFX School Archive
**Duration:** 8m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, um, let's just drop a position node for the, uh, hunter as well. I just want to move him forward just a tiny bit five. So that when the crocodile's mouth is actually shut, he's in the mouth. Okay, that's when he gets gets caught. So, let's um yeah, set up our our sim really quick. So, yeah, for this part, we'll just use the um shelf tools. So for our hunter, for the body, okay, we're uh we're not going to be obviously we'll s simulate the cloth and everything separately. For the body, we're going to be using this uh these new tetrahedral constraints. Okay. So I'm just going to click on that, click on the hunter, press enter with my cursor in the viewport here. Can see that it builds up our Vellum solver for us. Okay. So, let's go back out and see what we've got. So, the hunter. Let's see. It's all messed up. All this pointer form stuff. Let's get rid of that because we we'll build that later. Okay. So, we've got a poly reduce. Okay. So, obviously there we can see a problem straight away. That's being reduced too much. So, let's do uh percentage and let's I don't know could drop it to 50% whatever you want. Okay, just to simplify the geometry but in f...

**Frame:** tutorials\frames\module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Setting up a Vellum tetrahedral soft body for the hunter character via the Vellum Solid Object shelf tool, with a Poly Reduce proxy mesh tuned to balance simulation speed against recognizable shape.

### Summary
Positions the hunter at X=5 so he sits correctly inside the crocodile's mouth when it closes. Uses the Vellum shelf tool: select the hunter geometry -> Vellum Solid Object (tetrahedral). The shelf automatically adds Poly Reduce (a proxy mesh for speed), Tet Conform, Vellum Solid Object constraints, and a Vellum Solver. A noted problem is that Poly Reduce defaults are too aggressive, over-simplifying the shape — switching to percentage mode at roughly 50% keeps a recognizable shape while still speeding up the sim. Tetrahedral constraints fill the volume with tetrahedra via Tet Conform, and Vellum Solid Object then adds internal constraints connecting all tet vertices, giving volumetric soft-body behaviour (squishing under pressure) rather than surface-only cloth constraints. The key parameter is shape stiffness: very low values produce jelly-like behaviour, high values produce rubber-like behaviour.

### Key Steps
1. [Position] Place the hunter character at X=5 for correct mouth placement
2. [Vellum shelf tool] Select geometry -> Vellum Solid Object (tetrahedral), auto-building the network
3. [`Poly Reduce`] Switch from aggressive default to percentage mode (~50%) for a usable proxy mesh
4. [`Tet Conform`] Fill the volume with tetrahedra
5. [`Vellum Solid Object`] Add internal tet-vertex constraints for volumetric soft-body behaviour
6. [Shape stiffness] Tune between jelly-like (low) and rubber-like (high) behaviour

### Houdini Nodes / VEX / Settings
- `Vellum Solid Object` (shelf tool) — auto-builds Poly Reduce, Tet Conform, constraints and Vellum Solver for tetrahedral soft bodies
- `Poly Reduce` (percentage mode, ~50%) — balances proxy-mesh simulation speed against recognizable shape; default mode is too aggressive
- `Tet Conform` — fills mesh volume with tetrahedra for internal constraint generation
- Shape stiffness — key Vellum Solid Object parameter; low = jelly, high = rubber

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)

---

## Related Tutorials
- [Updating the Rest Blend](module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md) — the following lesson re-posing this same soft-body setup
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — combines this soft body with cloth and point-deform
- [Introduction to Vellum: Cloth/String/Grain Fundamentals](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — broader Vellum fundamentals referenced here
