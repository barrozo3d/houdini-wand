---
title: module i   week 02   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=G1JI3ACUZN4
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, attributes, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-01-intro-v1-1080p/
frame_count: 4
---

# module i   week 02   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=G1JI3ACUZN4)
**Author:** The VFX School Archive
**Duration:** 1m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right, welcome to week two of the RBD module. And this week we're looking at a bus stop. So, it's kind of a I suppose a strange thing to choose, but the reason we're doing that is because of the range of materials that we've got. So, we're focusing on, you know, mixing materials and being able to destroy them all together. So, we've got obviously the metal of the frame of the bus stop. We're looking at glass fracturing and wood as well. And that gives us a nice kind of um a variety of stuff going on there, right? So, yeah, in the first week, you know, we looked at concrete stone kind of thing, which is, you know, very common. Now, we're doing this is metal and wood and glass. And we're really utilizing some of the new tools that are provided by SideFX. So, you know, we're using the RBD material fracture node to create the wood and the glass. We're using the plasticity, which is a new thing I think in Houdini 18, if I'm not mistaken, for the soft constraints to get the metal kind of holding its shape, you know, so it doesn't spring back into where it got, which works really well in my opinion in in this project, you know, it kind of holds and bends and cr...

**Frame:** tutorials\frames\module-i-week-02-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
A bus stop destruction shot combining three material types — steel, glass and wood — using RBD Material Fracture together with plasticity-driven soft constraints so metal permanently deforms rather than springing back.

### Summary
Covers a bus stop with mixed-material destruction: a steel frame (metal), glass panels and wood planks. The new technique highlighted is the RBD Material Fracture SOP for both glass and wood fracture patterns. The key technique for metal is "plasticity" (new around H18) applied to soft constraints — metal holds its bent/deformed shape after impact instead of springing back, with constraints weakening and permanently deforming rather than breaking cleanly, producing realistic crushed-metal behaviour. Post-sim, Point Deform applies the low-res proxy simulation to the high-res render mesh. Also mentions the RBD Disconnected Faces fix for glass shards that separate at impact.

### Key Steps
1. [`RBD Material Fracture`] Fracture glass and wood with material-appropriate patterns
2. [Plasticity] Apply plasticity to metal soft constraints so it deforms permanently under impact
3. [`RBD Solver`] Run the combined multi-material simulation
4. [`Point Deform`] Apply the low-res proxy sim result to the high-res render mesh
5. [`RBD Disconnected Faces`] Fix glass shards that separate incorrectly at impact

### Houdini Nodes / VEX / Settings
- `RBD Material Fracture SOP` — generates glass and wood fracture patterns appropriate to each material
- Plasticity — soft-constraint property letting metal permanently bend/deform rather than spring back or break
- `Point Deform` — transfers proxy sim transforms onto high-res render geometry
- `RBD Disconnected Faces` — reconnects glass faces that float free after fracture/deform

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I)

---

## Related Tutorials
- [Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — the gap-filler lesson detailing the Point Deform step used here
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — the gap-filler detailing the disconnected-faces fix mentioned here
- [City Ground Destruction Intro](module-i-week-01-01-intro-v1-1080p.md) — the preceding week's Boolean fracture setup
