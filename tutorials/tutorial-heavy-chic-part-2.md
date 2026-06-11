---
title: [Tutorial] Heavy Chic. Part 2.
source: YouTube
url: https://www.youtube.com/watch?v=mOKs6Dht5Mw
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [dop, sop, vex, particles, simulation, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-heavy-chic-part-2/
frame_count: 4
---

# [Tutorial] Heavy Chic. Part 2.

**Source:** [YouTube](https://www.youtube.com/watch?v=mOKs6Dht5Mw)
**Author:** Alexander Eskin
**Duration:** 17m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, we need to fix a few things before starting the render. First of all, we need to add noise, amplitude 0.5, soil size 0.4, and use of expression. We should multiply amps. By our CD color, this way the particles that want move won't be affected by the noise. Otherwise, they have just float away like this. Like little worms. Now we don't need that. We'll do this. Everything looks great. Also, we need to fix the gamma a bit. We'll fix it by introducing a ramp here. It's going to be a nice, sharp ramp. Let's apply the ramp. And for the preview purposes, I'll apply it into CD. Just don't forget to plug it back. The ramp should be from 0 to 1. And it's going to be, we should add the third point, value 0.15. Select all the three of the points and tell them to be interpolated as the peace-pline. Also move this a bit. Like this. Okay. Don't forget to plug it back. Preview. Okay. Looks pretty good. Now we should increase the particle count. And the point separation decrease the point separation from 0.01 to 0.004. That should increase our point count from 700,000 points to 11 million. Now use the file cache. Name it part equals sim. Don't need it here. Move it there. Did it everything. ...

**Frame:** tutorials\frames\tutorial-heavy-chic-part-2\frame_000.jpg


---

## Structured Notes

### Core Technique
Continuation of Heavy Chic Part 1 — noise masking via Cd so stationary particles stay still, gamma ramp correction (B-spline, 3 points), scaling to 11 million particles by reducing point separation, `filecache` for disk-based playback, and final render setup.

### Summary
A 17-minute continuation tutorial (Part 2) completing the Heavy Chic luxury particle effect. The key refinement is masking particle noise by multiplying amplitude by `Cd` — particles with zero Cd won't flutter. A sharp B-spline ramp corrects gamma for the visual look. Point count scales from ~700k to 11 million by reducing point separation from 0.01 to 0.004. Sim is cached to disk via `filecache` named "part_sim", then rendered (Mantra/Karma) — final frame shows dramatic dark golden particle cloud.

### Key Steps
1. Add noise to particles in `popwrangle` or `popvop`: amplitude **0.5**, noise size **0.4**
2. Multiply amplitude by `Cd` attribute — particles with `Cd=0` (stationary) are unaffected by noise (critical masking trick)
3. Gamma correction: add `attribvop` → `ramp` node with sharp B-spline interpolation, 3 points (values: 0, 0.15, 1), apply to `Cd`
4. Preview ramp applied to `Cd`; plug back to final output after preview
5. Scale up particles: reduce point separation from **0.01 → 0.004** → count goes from ~700k to **11 million** points
6. `filecache` SOP — name: "part_sim"; cache sim to disk for playback performance
7. Render setup: Karma/Mantra with point cloud rendering; adjust point size and material for luxury glitter look

### Houdini Nodes / VEX / Settings
- `popwrangle` / `popvop` — noise: amplitude 0.5, size 0.4; multiply amplitude by `Cd` to mask stationary particles
- `attribvop` — ramp node: B-spline interpolation, 3 points (0, 0.15, 1) for gamma correction; applied to `Cd`
- Point separation: **0.01 → 0.004** (scales particle count from ~700k to 11M)
- `filecache` SOP — name: "part_sim"; writes sim to disk
- Karma or Mantra render node — point cloud / sprite rendering

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
dop, sop, vex, particles, simulation, rendering, intermediate

---

## Related Tutorials
- [[tutorial-heavy-chic-part-1]] — Part 1 (prerequisite — builds the base sim this tutorial refines)
- [[урок-тяжелый-люкс-часть-1]] — Russian companion series by same author
- [[improve-solaris-performance---houdini-tutorial]] — filecache strategy for sim caching
