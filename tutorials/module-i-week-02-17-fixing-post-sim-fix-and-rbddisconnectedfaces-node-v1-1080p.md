---
title: module i   week 02   17   fixing post sim fix and rbddisconnectedfaces node v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=R-ay-5fX_Os
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, rendering, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p/
frame_count: 4
---

# module i   week 02   17   fixing post sim fix and rbddisconnectedfaces node v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=R-ay-5fX_Os)
**Author:** The VFX School Archive
**Duration:** 10m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right, so to demonstrate the the glass thing, so to delete those primitives there, uh we need to well, you don't need to, but I find it easier to show with um if we apply a shader to it. So, I'm just going to quickly make a glass a principal shader with the glass uh preset turned on. Okay, and I'll just call this glass. Just leave it at that and you know, we're not worrying, it's just to show you. I'm also going to hide all these for a moment. Maybe let's drop a quick environment lights as well. Um just again, just for visualization, right? Okay, get rid of that. Let's jump in here. And yeah, so right away you can see we got the metal there, so we need to delete that cuz we've already, you know, we've done the everything we need with the metal. Uh so, on the points and it's going to be name is it was just a big metal we want to get rid of. So, uh name is big metal. Goodbye. Okay, and yeah, keeping the small metal bits and the wood and the glass. So, good and then let's split the glass. So, name is glass. And this needs to be I don't know why we have to select the group for it to work there. Okay. Cool, and then the material give it that glass material. A...

**Frame:** tutorials\frames\module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Fixing the RBD Disconnected Faces artifact, where faces lose their piece-level transform after deformation and float free, by reconnecting them to their nearest named piece and splitting the output for independent shading.

### Summary
After glass fracture and deformation, some faces become disconnected from their pieces — they float in space because they lost their piece-level transform. The RBD Disconnected Faces SOP reconnects orphaned faces back to their nearest named piece. Workflow: after RBD Deform Pieces, add RBD Disconnected Faces with "fix" mode enabled. The post-sim output is then split by name groups: a Blast SOP with `name == 'big_metal'` isolates and deletes the proxy geometry, and a separate Blast with `name == 'glass'` splits the glass stream for independent shader assignment. A quick visualization shader — Principled Shader with a glass preset (refraction IOR ~1.5) — is applied only to the glass group for a visual check before final render.

### Key Steps
1. [`RBD Disconnected Faces`] Add after RBD Deform Pieces; enable "fix" mode to reconnect floating faces
2. [`Blast SOP`] Isolate and delete `name == 'big_metal'` proxy geometry
3. [`Blast SOP`] Split out `name == 'glass'` geometry for independent shading
4. [`Principled Shader`] Apply a glass preset (refraction IOR ~1.5) to the glass group for a quick visual check
5. [Verify] Confirm no floating disconnected faces remain before final render

### Houdini Nodes / VEX / Settings
- `RBD Disconnected Faces SOP` — reconnects orphaned faces to their nearest named piece after deformation; "fix" mode performs the repair
- `Blast SOP` (by `name` group) — standard pattern for splitting post-sim geometry by piece-name for independent shading
- `Principled Shader` (glass preset, IOR ~1.5) — used here purely as a fast visual-check shader

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)

---

## Related Tutorials
- [Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — the preceding deform step that can introduce this artifact
- [Car Glass Fracture](module-i-week-04-01-intro-v1-1080p.md) — another glass-heavy shot where this fix is relevant
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the week this fix supports
