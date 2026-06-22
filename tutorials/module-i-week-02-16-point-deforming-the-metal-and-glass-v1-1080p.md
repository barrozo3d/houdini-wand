---
title: module i   week 02   16   point deforming the metal and glass v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=oZh_MAnZyaQ
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, sop, rbd, attributes, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p/
frame_count: 4
---

# module i   week 02   16   point deforming the metal and glass v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=oZh_MAnZyaQ)
**Author:** The VFX School Archive
**Duration:** 5m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, let's do the metal bending bit now. So, we need this and we need this. I'm going to move this over here. This is the results of sim two. Um and I want the We're going to be deforming that as well in this lesson now. Uh so, I'm going to put them over there. Now, there's a another new node called RBD um deform pieces. Which is really handy because what we're doing here is bending, as I said before, bending this with uh this. And you had to do like a whole kind of um for each loop where you're capturing uh the geometry and then bending it in another and and going um iterating over each separate piece in your in your geometry and it was kind of a pain and a bit complex, but now we've got this um setup which helps a lot. So, in here we have the geometry that you want to bend. Um we don't need to connect the the constraints. It does say it's required, but that's just because um well, it's it's it depends if you're using constraints here, but we're not going to do that. So, it does work without it, okay? And then this goes into the uh right hand side. Um what we do need to do here is we need If you think about it, you know, we need more geometry to be able ...

**Frame:** tutorials\frames\module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Using the RBD Deform Pieces SOP to apply a low-poly proxy simulation's per-piece rigid transforms onto high-resolution render geometry, matched by the `name` attribute.

### Summary
Before this node existed, the old method used a for-each loop capturing each piece's transform and deforming the matching hi-res piece individually — complex and slow. The RBD Deform Pieces workflow instead takes the high-res render geometry on input 0 and the fractured/simulated proxy geometry stream on input 1, matching pieces by their shared `name` attribute and applying per-piece rigid transforms directly. The constraints input (input 2) is not required unless using constraint-driven deformation. The high-res mesh needs additional polygon density to deform smoothly, so a Subdivide is added before the RBD Deform Pieces node. The result is that bending bus-stop metal follows the proxy simulation perfectly at full render resolution.

### Key Steps
1. [`Subdivide SOP`] Increase polygon density on the high-res mesh for smooth deformation
2. [`RBD Deform Pieces`] Input 0: high-res render mesh; Input 1: simulated proxy geometry stream
3. [Name matching] Confirm both inputs share the `name` attribute used for piece correspondence
4. [Optional] Connect constraints input only if constraint-driven deformation is needed
5. [Verify] Confirm high-res geometry now follows the proxy sim's per-piece transforms exactly

### Houdini Nodes / VEX / Settings
- `RBD Deform Pieces SOP` (H19+) — matches pieces by `name` and applies per-piece rigid transforms from a proxy sim onto high-res geometry
- `Subdivide SOP` — adds the polygon density required for the high-res mesh to deform smoothly
- Old for-each-loop method — superseded by this node; useful context for why RBD Deform Pieces is preferred

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)

---

## Related Tutorials
- [Starting the Post-Sim Setup](module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1.md) — the preceding setup this lesson operates within
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — the following cleanup step for artifacts this deform pass can introduce
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the week this technique is built for
