---
title: [Tutorial] Lipstick. Part 1. Modeling
source: YouTube
url: https://www.youtube.com/watch?v=Zqle_HOS7Jg
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-lipstick-part-1-modeling/
frame_count: 4
---

# [Tutorial] Lipstick. Part 1. Modeling

**Source:** [YouTube](https://www.youtube.com/watch?v=Zqle_HOS7Jg)
**Author:** Alexander Eskin
**Duration:** 18m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, to make a lipstick with it, to model a lipstick. So let's start with a June out, call it lipstick geo source. It's going to be gray, and I'm inside. Let's switch to frontal view and use curve polygon to draw a shape for the future revolve node. Something like this. Now let's enable snapping, grid snapping, and move the points around a bit. These two at least. And this one. Turn off the snapping. Let's revolve. Let's clip the top part. Because otherwise there's going to be a bit of an overlap. And it's easier to fix it right now rather than after the revolve node. Other than we subdivide it here, fuse it here. And we need to fire subdivisions for later purposes. For the field. For the bottom part. We need to cut the tip using a bullion. And we're going to use just the box. Stretch it a bit. Transform it. Turning around 55 degrees. Angle will be fine. And just eyeball it. 6131.544. Okay, just for example. Turn and transform. 90 degrees. Y axis. Okay, that's good enough. 1.56. I think we came through the same number. Anyway. Now we need the logo. We don't really need UVs right now. It's distracting. Okay, we just turn them off. For now, now we need the logo. When we use the trac...

**Frame:** tutorials\frames\tutorial-lipstick-part-1-modeling\frame_000.jpg


---

## Structured Notes

### Core Technique
English companion to Lipstick Pt1 RU — same workflow with exact angles: front-view profile curve → `revolve` → clip top first (prevents overlap) → `subdivide` (4 subdivisions for logo field) → `fuse` → `box` boolean rotated **~55°** for angled tip cut → `trace` SOP for logo.

### Summary
An 18-minute English modeling tutorial by Alexander Eskin building a lipstick for product visualization. Front-view `curve` (polygon) → `revolve`; clip top before revolve to prevent overlap. `subdivide` with **4 divisions** (important for the logo emboss field later) → `fuse`. Boolean cut: `box` stretched + rotated ~55° around the cutting axis, then 90° around Y → creates the characteristic angled lipstick tip (adjust by eye). `trace` SOP for brand logo (UVs disabled during modeling).

### Key Steps
1. Geo node "lipstick_geo_source" → switch to front view → `curve` SOP (polygon) → draw lipstick profile
2. Enable grid snapping → adjust profile points
3. Clip/trim the top of the curve to prevent revolve overlap
4. `revolve` SOP — revolve the profile around Y axis
5. `subdivide` SOP — **4 divisions** (required for logo area resolution later)
6. `fuse` SOP — clean up pinched top vertices
7. `box` SOP → `transform` — rotate ~**55°** for angled cut plane; then 90° around Y axis to align
8. `boolean` SOP — subtract box → creates angled lipstick tip
9. `trace` SOP — project logo from image file; disable UVs temporarily during setup
10. Continue to Part 2 for materials/rendering

### Houdini Nodes / VEX / Settings
- `curve` SOP — polygon type, front view profile
- `revolve` SOP — around Y axis
- `clip` SOP — trim top before revolving (prevents overlap)
- `subdivide` SOP — **4 divisions** (for logo detail)
- `fuse` SOP — clean top vertex
- `box` SOP + `transform` — rotate **~55°** + 90° Y
- `boolean` SOP — subtract for angled tip
- `trace` SOP — logo from image

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, modelling, procedural, intermediate

---

## Related Tutorials
- [[урок-помада-часть-1-моделирование]] — Russian companion (same technique)
- [[houdini-uv-unwrapping-fundamentals]] — UV workflow for product texturing
- [[tutorial-glass-tiles]] — product visualization rendering context
