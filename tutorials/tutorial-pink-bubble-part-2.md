---
title: [Tutorial] Pink Bubble. Part 2.
source: YouTube
url: https://www.youtube.com/watch?v=uztbmUElafA
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-pink-bubble-part-2/
frame_count: 4
---

# [Tutorial] Pink Bubble. Part 2.

**Source:** [YouTube](https://www.youtube.com/watch?v=uztbmUElafA)
**Author:** Alexander Eskin
**Duration:** 10m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome back to our tutorial about making spheres inside spheres. Today we're gonna render. We're gonna do the rendering in octane because why not? To be honest I'm not a very experienced octane user so I'm gonna make some travel mistakes for all of you, octane all timers so bear with me. But I like the glass. I like how the glass looks in the octane and the refractions. So I'm gonna use octane. So first of all we're gonna move all these things into the orange context. We're not gonna render the source node. We're gonna color it green and leave it be. I'm gonna create bubble base. Bubbles. Big bubbles. Small. We're not gonna move them around or select them in the viewport so I'm gonna check the green one. I hate it. And color now it's red. Now we're gonna merge our geometry into these nodes with the object merge. Out sphere base. This is our base sphere. Nice. Orange. This is gonna be our spheres big. And this are going to be our sphere small. And that's it. Everything is merged. We'll create a camera. Create a null. Set the Z translation to 6 and select our camera. Okay. I don't think we need the 16 by 9 aspect. We're gonna use the square one. And we're gonna change the focal leng...

**Frame:** tutorials\frames\tutorial-pink-bubble-part-2\frame_000.jpg


---

## Structured Notes

### Core Technique
Octane render setup for pink bubble spheres: separate SOP geometry into OBJ-level nodes (bubble base, big bubbles, small bubbles) via `objectmerge`, camera (Z=6, square aspect, adjusted focal length), Octane glass/refraction shader for transparent spheres.

### Summary
A 10-minute English Octane render tutorial (Part 2). Separates the bubble geometry into 3 OBJ nodes (bubble_base/outer sphere, big bubbles, small bubbles); source node stays green/unrendered. `objectmerge` pulls geo into each orange/rendered node. Camera positioned at Z=6, square aspect ratio (not 16:9), adjusted focal length. Octane chosen specifically for quality glass refraction rendering of the sphere-in-sphere setup.

### Key Steps
1. Create 3 OBJ geo nodes: bubble_base (outer sphere), big_bubbles, small_bubbles — color orange
2. Keep source node green (not rendered)
3. `objectmerge` inside each node — pull geometry from SOP source
4. Camera: Z translation = **6**, square aspect ratio (not 16:9), adjust focal length
5. Create null for camera target
6. Octane render target — add Octane glass/SSS shaders per element
7. Light source (required for Octane — no light = black)

### Houdini Nodes / VEX / Settings
- OBJ geo nodes — orange (rendered): bubble_base, big_bubbles, small_bubbles
- `objectmerge` SOP — import geo from source node
- Camera — Z: 6; aspect: square; adjust focal length
- Octane render target
- Octane glass shader — refraction for spheres

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, rendering, intermediate

---

## Related Tutorials
- [[урок-розовые-пузыри-часть-2]] — Russian companion (same content, 15 min)
- [[tutorial-pink-bubble-part-1]] — Part 1 (geometry prerequisite)
- [[урок-стеклянный-пончик]] — Octane glass/refraction material context
