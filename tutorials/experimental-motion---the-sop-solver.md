---
title: Experimental Motion - The SOP Solver
source: YouTube
url: https://www.youtube.com/watch?v=A11B_UE07ac
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["sop-solver", "dop", "procedural-animation", "simulation", "organic", "rendering", "lighting", "art-direction"]
extraction_status: complete
frames_dir: tutorials/frames/experimental-motion---the-sop-solver/
frame_count: 4
---

# Experimental Motion - The SOP Solver

**Source:** [YouTube](https://www.youtube.com/watch?v=A11B_UE07ac)
**Author:** Houdini.School
**Duration:** 89m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en yeah thank you for everyone who's here and also thank you for watching if you see this recording after we're done my name is yanul dman today we're going to talk about the sub solver in Houdini which is a little bit tricky solver to work with but our we will go over through two different setups that will make sure that you will understand both ways to approach the sub Sol and I think you will see that it's very powerful and we will work we we will be working with more of a little bit more philosophical than last time we will be using certain Concepts that make all sense for me while I'm working and so I would like to also if anyone here has a question about how I get to a certain decision please do that because everyone works in a different way and I would like to show you how I approach the work we will mostly go over building these different systems that create life and then at the end we will be rendering a little bit as well so we can talk about how I approach lighting and certain uh tricks that make your lighting feel more realistic and also a little bit more thought out and art directed so this is what we'll be doing today we will be talking about ...

**Frame:** tutorials\frames\experimental-motion---the-sop-solver\frame_000.jpg


---

## Structured Notes

### Core Technique
Using the SOP Solver inside a DOP network to build iterative, state-aware geometry systems that create lifelike organic motion — with an emphasis on the conceptual/philosophical approach to building living systems.

### Summary
Yan Paul Dubbelman presents an 89-minute live session dedicated to the SOP Solver in Houdini. The session covers two distinct approaches to the SOP Solver, demonstrating both setups to give viewers a solid understanding of this powerful but tricky tool. Dubbelman focuses on systems that simulate "life" — organic, evolving motion — rather than standard physics simulations. The session ends with rendering and lighting techniques including tricks that make lighting feel more realistic and art-directed. The tone is philosophical: Dubbelman shares his decision-making process and encourages viewers to question how they approach their work.

### Key Steps
1. Understand the SOP Solver's place in the DOP context and why it differs from standard DOP solvers
2. Set up the first SOP Solver approach — direct geometry manipulation inside a DOP network
3. Build iterative feedback loops where geometry at frame N influences frame N+1
4. Set up the second SOP Solver approach — a more abstract conceptual system for organic behavior
5. Create systems that produce lifelike "growth" or "living" motion
6. Render the resulting animation with art-directed lighting
7. Apply lighting tricks for realism and mood — key light positioning, environment lighting, and subtle variation

### Houdini Nodes / VEX / Settings
- SOP Solver (DOP context)
- DOP Network
- Geometry data in DOPs
- Foreach iteration inside SOP Solver
- Attribute Wrangle (inside SOP Solver)
- Rendering/lighting setup

### Difficulty
Advanced

### Houdini Version
unspecified

### Tags
sop-solver, dop, procedural-animation, simulation, organic, rendering, lighting, art-direction

---

## Related Tutorials
- [Experimental Motion - CHOPS](experimental-motion---chops.md) — companion session by same author using CHOPs for smooth organic motion
- [Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants](yan-paul-dubbelman-procedural-nature-procedural-living-plants.md) — same artist's natural/botanical procedural work
- [Surface Advection](surface-advection.md) — another approach to organic flowing motion using volume advection
