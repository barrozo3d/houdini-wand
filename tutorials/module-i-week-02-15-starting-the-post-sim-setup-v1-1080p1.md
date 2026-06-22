---
title: module i   week 02   15   starting the post sim setup v1 1080p1
source: YouTube
url: https://www.youtube.com/watch?v=XFOd1dy92Eg
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1/
frame_count: 4
---

# module i   week 02   15   starting the post sim setup v1 1080p1

**Source:** [YouTube](https://www.youtube.com/watch?v=XFOd1dy92Eg)
**Author:** The VFX School Archive
**Duration:** 2m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right. I'm just going to drop a null down here underneath this cache and call this uh Okay. And then uh yeah, let's do the same as before. So, I'm going to split this top and bottom. Um and yeah, they're both pinned, so it's good. And then I'll make another geometry node and call this uh post post sim jump in there. Then object merge um everything that we need. Right. So we'll start with this one up here. So that we get all the bits there. We'll also need I could probably just copy and paste a load of these across the metal sim. So, Ctrl + C, Crl + V that. So, we get this. Okay. So, that's the animated kind of fractured bit, right? Um, so we're going to need the metal to actually deform with that. So, uh Oh, I need to stay in here, go out here, and go into my metal sim. No, the fracture and then find Yeah. So, there's metal prefrure. Okay. Okay. So, come across and then drag that in there. Okay. So, this is the non fractured bit. And then, yeah, we'll need this glass as well. So, remember this piece of glass which is not broken. We'll have to deform that to follow the animation. And one more thing, I think just the collider. If we go to here at the botto...

**Frame:** tutorials\frames\module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1\frame_000.jpg


---

## Structured Notes

### Core Technique
Establishing the post-simulation network for applying the proxy RBD result back to high-resolution render geometry, using named Nulls and Object Merge to assemble a stable multi-input setup.

### Summary
Adds a Null SOP after the DOP Import cache (named e.g. "OUT_SIM") to cap the simulation stream. A Split SOP (or separate Blast) separates top vs. bottom pieces for independent treatment. A new geometry node named "post_sim" is created, using Object Merge SOPs to pull in: the cached RBD fractured geometry, the original un-fractured metal mesh (pre-fracture geo for deformation), the glass mesh, and the collider geometry. This multi-input post_sim SOP is where the RBD Deform Pieces node operates in the following lesson. The key habit emphasized is always inserting named Nulls as network outputs to keep Object Merge paths stable.

### Key Steps
1. [`Null SOP`] Cap the DOP Import cache output with a named Null (e.g. "OUT_SIM")
2. [`Split SOP` / `Blast SOP`] Separate top vs. bottom pieces for independent treatment
3. [New geometry node] Create "post_sim" as the destination network
4. [`Object Merge`] Pull in cached RBD geo, pre-fracture metal mesh, glass mesh and collider geometry
5. [Naming convention] Use named Nulls throughout so Object Merge paths remain stable across edits

### Houdini Nodes / VEX / Settings
- `Null SOP` — named network output caps, used as stable Object Merge targets
- `Split SOP` / `Blast SOP` — separates geometry by region (top/bottom) for independent post-sim treatment
- `Object Merge` — multi-input pattern pulling cached sim, pre-fracture mesh, glass mesh and collider into one post_sim network

### Difficulty
Intermediate

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)

---

## Related Tutorials
- [Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — the following lesson that operates on this post_sim setup
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the week this post-sim pipeline supports
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — the subsequent post-sim cleanup lesson
