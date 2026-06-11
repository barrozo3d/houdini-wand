---
title: [Tutorial] Glass Tiles
source: YouTube
url: https://www.youtube.com/watch?v=Ps6ZOKEdDos
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, modelling, procedural, instancing, rendering, redshift, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-glass-tiles/
frame_count: 4
---

# [Tutorial] Glass Tiles

**Source:** [YouTube](https://www.youtube.com/watch?v=Ps6ZOKEdDos)
**Author:** Alexander Eskin
**Duration:** 25m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's start with the Juno. Ju... tiles... source... green. Let's make a tile. It's going to be made from a box. Box... of 0.1, 0.5. And that's it. We're going to color the other side, so it would be easier to determine which side this tile is facing. So the fifth primitive should be red. And now it is. Let's make it more complicated than just a box for the extrude. By extruding it, primitive number 5, number 4 should be extruded by a bit. And inserted by a fair bit. And we should probably check for it. Or a battle. Because we're going to render it and they're going to be glassy or whatever. The refractions will look much, much better. On the battle shapes and subdivided ones. They should be held by a small amount. In the crease mode, two divisions. Like this and subdivided. It's going to look like this. And I'm happy with it. Now... Oh, tiles. So we made a singular tile. Now we should make some points. To copy those tiles to size 10 and height is 2.5. Oh, the X is different. YZ. We didn't need any polygons. We need only points 128, 128. So, copy the points. Copy the points. Don't forget to check the back end instance. And they copied, but they're huge. We need to scale them d...

**Frame:** tutorials\frames\tutorial-glass-tiles\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedural glass/mosaic tile wall: single tile built from `box` + `polyextrude` + `subdivide` (crease mode, 2 divisions), oriented by coloring a reference primitive, distributed on a 128×128 point grid via `copytopoints`, with per-tile attribute variation for luxury glass refraction rendering in Redshift.

### Summary
A 25-minute tutorial by Alexander Eskin building a procedural glass tile wall for luxury brand rendering. A single tile is modeled from a `box` (0.1 × 0.5), one primitive colored red for orientation reference, then `polyextrude` + `subdivide` with crease (2 divisions) for smooth beveled edges needed for glass refraction. Tiles are distributed on a 128×128 point grid (size 10, height 2.5, YZ plane, points-only mode) via `copytopoints` with per-instance scaling. Final render uses Redshift with glass/refraction shader.

### Key Steps
1. Geo node → `box` SOP — size 0.1 × 0.5; this is the single tile unit
2. Color primitive 5 red (`primitive` SOP or `attribwrangle`) — orientation reference to know which face is front
3. `polyextrude` — extrude primitive 4 by a small amount; insert face by a fair amount for beveled profile
4. `subdivide` SOP — **crease mode**, 2 divisions → smooth beveled tile shape (critical for glass refraction)
5. Tile is complete. Pivot/clean attributes as needed
6. `grid` SOP — size 10, height 2.5, YZ plane; **points only** mode (no polygons); 128×128 points
7. `copytopoints` SOP — copy tile to grid points; enable **"Pack and Instance"** option
8. Scale instances down to fit grid spacing (tiles are huge initially)
9. Per-tile attribute variation via `attribwrangle` — randomize rotation, `pscale`, or `orient` per point
10. Redshift material — glass shader with refraction; enable subdivision in Redshift object settings

### Houdini Nodes / VEX / Settings
- `box` SOP — size 0.1 × 0.5
- `primitive` SOP or `attribwrangle` — color primitive 5 red for orientation
- `polyextrude` SOP — extrude primitive 4+5; insert offset for bevel
- `subdivide` SOP — crease mode, 2 divisions
- `grid` SOP — size 10 × 2.5, YZ plane, 128×128 rows/cols, **points only**
- `copytopoints` SOP — Pack and Instance enabled
- `attribwrangle` — per-tile scale/rotation randomization
- Redshift glass shader — refraction + subdivision

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, modelling, procedural, instancing, rendering, redshift, intermediate

---

## Related Tutorials
- [[model-a-procedural-flower-houdini-tutorial]] — similar copytopoints distribution approach
- [[houdini-tutorial-make-any-geometry-knitted]] — procedural pattern distribution on geometry
- [[houdini-uv-unwrapping-fundamentals]] — UV prep for textured tile rendering
