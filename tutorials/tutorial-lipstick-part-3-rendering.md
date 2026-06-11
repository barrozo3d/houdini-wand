---
title: [Tutorial] Lipstick. Part 3. Rendering
source: YouTube
url: https://www.youtube.com/watch?v=6V7Y5aBmjo4
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-lipstick-part-3-rendering/
frame_count: 4
---

# [Tutorial] Lipstick. Part 3. Rendering

**Source:** [YouTube](https://www.youtube.com/watch?v=6V7Y5aBmjo4)
**Author:** Alexander Eskin
**Duration:** 14m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's render the thing. Geo, we don't need that. We need stick, droplets, lipstick, lipstick itself. Droplets, large droplets. Set the material to water. Now we should create oak, tin, red or no. Camera, call it shot 10 output. We don't need the output. Everything stays the same. We only need to overwrite camera resolution to half. This is going to be contour 1. Go to material, create a container and a target. Color it black, color it, render target 010. Path tracing, quality. Spectre depth 24, max samples 200, something adaptive, light, no deep image, no environment, texture. But for now we want to set the HDR. So it's going to be black. Camera, camera, order focus stays on for now. Image, A still mapping. Denoiser, no, obstetor, no, post processing, no, AOV. You're probably going to need a cryptomite by material node name. That's going to be it for the render settings. That's going to be it. Now we can start the render. Shortcut, go to shortcut number 1 and open up an IPR. My IPR should be black because we don't have an environment or lights yet. Indeed it is. So let's start with the simplest material. It's the background. It shouldn't have any specular weight. And it shoul...

**Frame:** tutorials\frames\tutorial-lipstick-part-3-rendering\frame_000.jpg


---

## Structured Notes

### Core Technique
Octane render setup for the lipstick product visualization: separate OBJ nodes (body, droplets, large droplets with water material), Octane camera (half res), render target (path tracing, spectre depth 24, max samples 200, adaptive), Cryptomatte AOV by material. Background material = no specular, matte.

### Summary
A 14-minute Octane rendering tutorial (Part 3 of Lipstick series). Sets up geo nodes: lipstick body, droplets, large droplets (water material). Octane camera "shot_10_output" at half resolution. Octane render target "render_target_010" — path tracing, spectre depth 24, max samples 200, adaptive sampling enabled. No deep image, no environment texture initially (render starts black until lights added). Cryptomatte AOV by material node name. Background shader: no specular weight, diffuse only. IPR opened with shortcut 1.

### Key Steps
1. Assign large droplets material: **water** shader
2. Octane camera: name "shot_10_output"; **half resolution**; order focus on; image A still mapping
3. Octane render target "render_target_010": path tracing, spectre depth **24**, max samples **200**, adaptive enabled; no deep image; no environment; no denoiser; no post processing
4. AOV: **Cryptomatte by material node name** (essential for comp)
5. Background material: no specular weight; diffuse/matte
6. Open IPR with shortcut 1 — initially black (no lights yet)
7. Add HDRI environment + area lights for lipstick material response
8. Build lipstick body shader (metal cap, plastic body, wax tip), droplet glass/SSS shader

### Houdini Nodes / VEX / Settings
- OBJ geo nodes: lipstick body, droplets, large_droplets
- Large droplets: Octane water shader
- Octane camera: half resolution, order focus, A still mapping
- Octane render target: path tracing; spectre depth 24; max samples 200; adaptive
- AOV: Cryptomatte (by material node name)
- Background shader: no specular, diffuse
- IPR shortcut: 1

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, rendering, intermediate

---

## Related Tutorials
- [[tutorial-lipstick-part-2-flip-sim]] — Part 2 (FLIP droplets prerequisite)
- [[tutorial-pink-bubble-part-2]] — Octane render setup comparison
- [[урок-розовые-пузыри-часть-2]] — Similar Octane workflow
