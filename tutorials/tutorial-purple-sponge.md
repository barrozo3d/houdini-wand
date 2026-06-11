---
title: [Tutorial] Purple Sponge
source: YouTube
url: https://www.youtube.com/watch?v=O5cFGKp0n_A
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, dop, vdb, volumes, vellum, particles, simulation, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-purple-sponge/
frame_count: 4
---

# [Tutorial] Purple Sponge

**Source:** [YouTube](https://www.youtube.com/watch?v=O5cFGKp0n_A)
**Author:** Alexander Eskin
**Duration:** 29m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** I was inspired by Mark's true gear work on Instagram. So I'll go check it out. So I'm going to start with the June node. Name it points, source, green, dive inside, create a box. 0.7, 0.15, move it to 0. Convert to VDB, VDB from polygons. Now we need a fog VDB with higher resolution. Apply cloud noise. Default settings will do points from volume. 0.07, 0.75, yeah, 400,000 points. Add scale attribute 0.5, edit preview with the wrangle. So we're going to see how the plans look like in the viewport. IGL, sphere points, close one. Like this, and then create a group. Group by points, blaster. Bounding regions 0.5, 2 here, blast everything but the group. And delete everything below 0. Also need to add another noise. So it looks a bit more interesting. 0.4, this place. Vains, noise, get vector component. First one, position frequency 15. Add to the current position. A little to vector. Y is going to explode. Yeah, the amplitude is too big. Multiply constant 0.05. Now we have some funny looking stuff. At least a bit more funny looking. Then it was before. More details, the more the better. Now I can create Vail and Greens. They're going to look huge, but we can fix that by copying a p-scal...

**Frame:** tutorials\frames\tutorial-purple-sponge\frame_000.jpg


---

## Structured Notes

### Core Technique
Sponge/foam effect using VDB pipeline: box → `vdbfrompolygons` → `cloudnoise` displacement → `pointsfromvolume` (400k points) → secondary noise wrangle (freq 15, amp 0.05) → **Vellum Grains** simulation for the soft organic feel. `pscale` copied from source to grains to fix size. English companion to "Губка".

### Summary
A 29-minute English tutorial by Alexander Eskin (inspired by Mark's Instagram work) building a purple sponge effect. The pipeline is more complete than the Russian version: box converted to fog VDB via `vdbfrompolygons` + `cloudnoise` default settings → `pointsfromvolume` scatter (400k points, separation 0.07) → secondary noise (Y-component, freq 15, amplitude × 0.05) for organic shape variation → bounding region group + blast to clean below Y=0 → Vellum Grains simulation with `pscale` copied from source. Frame 003 confirms a fluffy dark foam/sponge render.

### Key Steps
1. Geo node "points_source" → `box` SOP — size 0.7 × 0.15; move to origin
2. `vdbfrompolygons` SOP — convert box to VDB (polygon → fog VDB)
3. `cloudnoise` VOP or `volumeVOP` — apply default cloud noise settings to the fog
4. `pointsfromvolume` SOP — point separation **0.07**, ~400,000 points; add `pscale` attribute **0.5**
5. `attribwrangle` — viewport GL preview: `i@gl_sphere_points = 1;` (optional)
6. Create group — bounding region (0.5 to 2); `blast` — keep group only; delete points below Y=0
7. `attribwrangle` — secondary noise on position:
```vex
vector noise_vec = noise(v@P * 15.0);  // freq 15
float component = noise_vec.x;         // get Y-axis component
v@P.y += component * 0.05;            // amplitude 0.05
```
8. Create **Vellum Grains** DOP — grains initially appear huge; copy `pscale` from source points via `attribcopy` to fix size
9. Vellum Grains solver — simulate soft organic grain structure
10. Render with subsurface/SSS material for sponge-like appearance

### Houdini Nodes / VEX / Settings
- `box` SOP — 0.7 × 0.15
- `vdbfrompolygons` SOP — fog VDB conversion
- `cloudnoise` — default settings on fog volume
- `pointsfromvolume` SOP — separation: 0.07; ~400k points; `pscale`: 0.5
- `attribwrangle` — `gl_sphere_points` for viewport preview
- `group` SOP — bounding region 0.5–2
- `blast` SOP — keep group; delete below Y=0
- Noise wrangle — vector noise, freq 15, Y-component, amplitude × 0.05
- `vellumgrains` / Vellum Grains DOP
- `attribcopy` — copy `pscale` from source to grains

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, dop, vdb, volumes, vellum, particles, simulation, rendering, intermediate

---

## Related Tutorials
- [[урок-губка]] — Russian companion (simpler pipeline, no Vellum)
- [[intro-to-houdini-volumes---beginner-course]] — fog VDB foundations
- [[houdini-21-tutorial---mpm-snowball]] — similar soft-particle simulation approach
- [[intro-to-houdini-for-vfx---beginner-course]] — Vellum solver overview
