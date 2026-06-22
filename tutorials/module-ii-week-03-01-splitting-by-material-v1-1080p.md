---
title: module ii   week 03   01   splitting by material v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=cvAuweF1fvg
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [dop, sop, rbd, attributes, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-03-01-splitting-by-material-v1-1080p/
frame_count: 4
---

# module ii   week 03   01   splitting by material v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=cvAuweF1fvg)
**Author:** The VFX School Archive
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, we're going to start week three with the result of week two because, you know, we're using the same building and uh um it's easier just to start off like this. I'm going to delete all of this stuff. Um and then go into file and then we can just save use the same project as well. Okay, so save as and we'll change this to uh this is going to be X Let's call it nuke. It's going to be like a new nuclear explosion. Uh version one, accept. Okay, dive inside here and again, that will delete most of this. So, let's save them down there. Delete all of that. Okay. And then let's take a look at um splitting this up again. Um so, I'm going to change this to point Where is it? This connectivity needs to be on primitives. Um and then I'm going to convert So, this is still poly soup at this point, right? So, let's just convert it to just normal everyday polygons. Okay. There you go. Okay, see it's just polygons there now. And then um I'm going to start splitting this up. So, for this week, you know, we're going to go into some detail. I think in week two we literally just did a really simple uh Voronoi fracture, right? Um so, I want to use the Let's see. I don't th...

**Frame:** tutorials\frames\module-ii-week-03-01-splitting-by-material-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Splitting destruction geometry by material group and applying the RBD Material Fracture SOP, which generates characteristic shard shapes per material (glass, wood, concrete) in a single node.

### Summary
Continues from the Week 2 building Alembic, resaving the project under a new name. A key setup step is the Connectivity SOP set to "primitives" mode to identify separate geometry pieces, followed by a Convert SOP to move from PolySoup to standard polygons. Geometry is split by material groups so different pieces receive different fracture treatment: the RBD Material Fracture SOP (an H18.5+ node) handles glass, wood and concrete fracture in one node, with each material type generating characteristic shard shapes — glass produces many small sharp fragments, wood produces long splinters along the grain, and concrete produces chunky irregular blocks. The `name` attribute remains critical, since each piece needs a unique name for the constraint network.

### Key Steps
1. [`Connectivity SOP`] Set to "primitives" mode to identify separate geometry pieces
2. [`Convert SOP`] Convert from PolySoup to standard polygons
3. [Material groups] Split geometry into glass, wood and concrete groups
4. [`RBD Material Fracture SOP`] Fracture each material group with its characteristic shard pattern
5. [`Assemble SOP`] Re-assign unique `name` attributes after fracture for the constraint network

### Houdini Nodes / VEX / Settings
- `Connectivity SOP` (primitives mode) — groups geometry by connected-piece membership before material splitting
- `RBD Material Fracture SOP` (H18.5+) — single node producing material-appropriate fracture patterns (glass/wood/concrete)
- `name` attribute — required uniquely per piece for the downstream constraint network

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)

---

## Related Tutorials
- [Importing the Geometry (Module II W02)](module-ii-week-02-01-importing-the-geometry-v1-1080p.md) — the preceding week establishing the building asset
- [Concrete + Metal Destruction](module-ii-week-04-01-importing-the-geometry-v1-1080p.md) — the following week's skyscraper collapse
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — a later course applying RBD Material Fracture to glass and wood
