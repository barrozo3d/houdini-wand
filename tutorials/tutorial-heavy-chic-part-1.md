---
title: [Tutorial] Heavy Chic. Part 1.
source: YouTube
url: https://www.youtube.com/watch?v=fjVERoS2olY
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [dop, sop, vex, particles, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-heavy-chic-part-1/
frame_count: 4
---

# [Tutorial] Heavy Chic. Part 1.

**Source:** [YouTube](https://www.youtube.com/watch?v=fjVERoS2olY)
**Author:** Alexander Eskin
**Duration:** 24m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So let's do some heavy particles chic. Start with the G now. Let's call it particles Sim color green. Start with a simple grid we'll fix it later on because everything is procedural you know, hoodie and stuff. Then scatter some points let's say 100,000 at a p-scale attribute. We'll gonna need it later on and add a pop network. Diving. Let this one we don't need it. An emission type just all points that's gonna mean that we're gonna meet from each point every frame. So the first frame will only have 100,000 and later frames are gonna have 1 million. No. We're gonna need only those points that exist in the frame one. So we're gonna exit by writing an expression f equals equals one. That means that if the frame equals one then the statement is true if it's two then it's zero because the number of the frame is two. Now we're gonna meet only on frame one. So say 100,000 or 100,000 points. Also fixed frame rate. 24 is for the movies we're doing it for the social media so it's 30. So Diving and at pop wind. Pop wind say wind velocity is six. Now every point is gonna fly upwards as expected. But what we need is for some unevenness in their behavior. We can do this by introducing noise like...

**Frame:** tutorials\frames\tutorial-heavy-chic-part-1\frame_000.jpg


---

## Structured Notes

### Core Technique
Social-media luxury particle animation: POP network with frame-1-only emission via `$F==1` expression to lock particle count at exactly 100,000, `popwind` velocity 6, noise for uneven behavior — produces falling silk curtain / rising crystal column aesthetics at 30 FPS. English-language Part 1 by Alexander Eskin (companion to Heavy Lux series).

### Summary
A 24-minute English tutorial by Alexander Eskin (Part 1) building a "Heavy Chic" luxury particle effect for social media at 30 FPS. The key technique is using the expression `$F==1` in popsource birth parameters to emit only on frame 1, locking the count at exactly 100,000 particles for the entire animation without multiplication. Frames show progression from blue grid source → jagged mountain/crystal particle formations → flowing silk curtain aesthetic. Companion series to Heavy Lux (Russian).

### Key Steps
1. Geo node → `grid` SOP; name it `particles_sim`; color `Cd` green
2. `scatter` SOP → 100,000 points; add `pscale` attribute (needed later)
3. `popnet` DOP → dive inside
4. `popsource` — Emission Type: **All Points**; in Birth parameters set expression **`$F==1`** — emits only on frame 1, so count stays exactly 100,000 throughout (not multiplying each frame)
5. Set frame rate to **30 FPS** (social media standard, not 24 for film)
6. `popwind` — wind velocity: **6** → all particles fly upward
7. Add noise (curl noise or turbulence) to `popwind` or via `popwrangle` for uneven particle behavior
8. Adjust `pscale` for particle size variation

### Houdini Nodes / VEX / Settings
- `grid` SOP — particle source geometry
- `scatter` SOP — 100,000 points; `pscale` attribute
- `popnet` DOP
- `popsource` — Emission Type: All Points; Birth expression: **`$F==1`** (critical: locks count at frame-1 value)
- Frame rate: **30 FPS** (social media)
- `popwind` — wind velocity: 6
- Noise wrangle — curl/turbulence noise for behavioral variation

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
dop, sop, vex, particles, simulation, intermediate

---

## Related Tutorials
- [[урок-тяжелый-люкс-часть-1]] — Russian companion tutorial (same author, same series concept)
- [[intro-to-houdini-particles---full-beginner-course]] — Full POP network foundation
- [[vops-02---random-noise---houdini-beginner-tutorial]] — Noise patterns for particle variation
