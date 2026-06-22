---
title: week 02   04   finishing the horizontal cable sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=ykTr02tft_k
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rbd, simulation, dop, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-04-finishing-the-horizontal-cable-sim-v1-1080p/
frame_count: 4
---

# week 02   04   finishing the horizontal cable sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=ykTr02tft_k)
**Author:** The VFX School Archive
**Duration:** 9m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Now, one thing uh if you come here look at the geometry here. And if I turn off guides, you can see the constraints popping back in. If I turn that back on, come into this constraints tab within the guided simulation tab, you can see we've got this remove intra guide constraint. So, that's removing constraints which uh you know, between two guided things. So, just turn that off and then we get our constraints back. All right? Um so, everything else we just uh leave at default pretty much. I'm going to go back to this setup here. And what controls this um strength is how strongly these pieces are being guided by this piece, right? So, if I turn this to zero and play that, then pretty much they'll just drop away straight away. See that? See that it's changed color and now they're just moving um independently. So, we can use this value to control you know, when when they're being um uh kind of moved by this. So, basically when you know, this is also playing with if we come to the simulation settings, we've got these guide release thresholds. So, the angular threshold and linear threshold. So, based on these two values, when this is pulled away quickly or um...

**Frame:** tutorials\frames\week-02-04-finishing-the-horizontal-cable-sim-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Completing the guided Bullet simulation for the bridge's horizontal cables — resolving intra-guide constraint removal, tuning guide strength and release thresholds to control when cable segments detach and fall freely.

### Summary
The instructor resolves a constraint-visibility issue caused by the guided sim removing intra-guide constraints by default, which is toggled off to restore correct cable connections. Guide strength is demonstrated by setting it to zero, causing all pieces to fall immediately and freely, showing how strength controls the blending between guided and free-simulated motion. The angular and linear release thresholds within the Guided Simulation settings are then tuned to define the exact point at which cable segments break away from the guide and simulate independently.

### Key Steps
1. [Guided Sim > Constraints Tab] Disable "Remove Intra-Guide Constraints" to restore constraint visibility
2. [`RBD Solver` playback] Verify constraints now appear and hold correctly
3. [Guide Strength] Set strength to 0 to see unconstrained fall; then restore to working value
4. [Guided Sim > Simulation Settings] Locate angular threshold and linear threshold parameters
5. [Angular Threshold] Tune the angle at which a piece detaches from the guide
6. [Linear Threshold] Tune the linear velocity/displacement that triggers detachment
7. [`RBD Solver`] Final playback confirming cables follow guide then release on collapse

### Houdini Nodes / VEX / Settings
- Guided Sim Constraints Tab > Remove Intra-Guide Constraints — toggle that incorrectly removes constraints between guided pieces; must be disabled
- Guide Strength — float parameter (0-1) blending guide influence; 0 = fully free, 1 = fully guided
- Angular Release Threshold — maximum angular deviation from guide before a piece goes free
- Linear Release Threshold — maximum positional deviation before a piece detaches

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Starting the Guided Sim](week-02-03-starting-the-guided-sim-v1-1080p.md) — the preceding setup step this video completes
- [Bridge Destruction Week 02 Intro](week-02-01-intro-v1-1080p.md) — week overview
- [Starting the Vellum Sim](week-02-07-starting-the-vellum-sim-v1-1080p.md) — Vellum wire approach for the vertical cables
