---
title: module i   week 02   15   starting the post sim setup v1 1080p1
source: YouTube
url: https://www.youtube.com/watch?v=XFOd1dy92Eg
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, post-sim, object-merge, destruction, intermediate]
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
**Transcript:** Kind: captions Language: en Right. I'm just going to drop a null down here underneath this cache and call this uh Okay. And then uh yeah, let's do the same as before. So, I'm going to split this top and bottom. Um and yeah, they're both pinned, so it's good. And then I'll make another geometry node and call this uh post post sim jump in there. Then object merge um everything that we need. Right. So we'll start with this one up here. So that we get all the bits there. We'll also need I could probably just copy and paste a load of these across the metal sim. So, Ctrl + C, Crl + V that. So, we get this. Okay. So, that's the animated kind of fractured bit, right? Um, so we're going to need the metal to actually deform with that. So, uh Oh, I need to stay in here, go out here, and go into my metal sim. No, the fracture and then find Yeah. So, there's metal prefrure. Okay. Okay. So, come across and then drag that in there. Okay. So, this is the non fractured bit. And then, yeah, we'll need this glass as well. So, remember this piece of glass which is not broken. We'll have to deform that to follow the animation. And one more thing, I think just the collider. If we go to here at the bottom, I've got the collider there. So I can just copy that and bring that up here as well. Okay. So I think that's everything. I can just delete this now. So we got the this geometry. We got this which we will use to bend or to deform this geometry. Then we also have the glass which will follow that animation and the collider as well. Um so that's everything we need to uh finish our shot.

**Frame:** tutorials\frames\module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1\frame_000.jpg


---

## Structured Notes

### Core Technique
Post-sim network setup: creating a dedicated geometry node ("post_sim") and object-merging all required simulation outputs (fractured cache, pre-fracture metal, unbroken glass, collider) into one place for deformation and finalization.

### Summary
2m13s lesson covering the organizational step of post-sim setup. Creates a null after the simulation cache, then a new geometry node "post_sim" with Object Merges of: (1) sim output (fractured animated geometry), (2) pre-fracture metal (for Point Deforming), (3) unbroken glass (for deforming to follow sim), and (4) collider geometry. Sets up the input infrastructure for the deformation steps that follow.

### Key Steps
1. Drop null after sim cache → named anchor point
2. Create new geometry node "post_sim"
3. Inside: Object Merge the sim cache output (gets all animated fractured bits)
4. Object Merge pre-fracture metal geometry (non-fractured, will be point-deformed)
5. Object Merge unbroken glass (will follow sim animation via Point Deform)
6. Object Merge collider geometry (needed for final composite)

### Houdini Nodes / VEX / Settings
- **Null** — named cache anchor after simulation
- **Object Merge** — reference other nodes by path; avoids long wires across network

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[rbd, post-sim, object-merge, destruction, intermediate]

---

## Related Tutorials
- module-i-week-02-01-intro-v1-1080p.md (project intro)
- module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md (next step: deform pieces)
- module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md (RBD disconnected faces)
