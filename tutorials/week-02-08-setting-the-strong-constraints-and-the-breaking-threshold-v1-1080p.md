---
title: week 02   08   setting the strong constraints and the breaking threshold v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9TNDsfFNoq4
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [vellum, simulation, dop, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p/
frame_count: 4
---

# week 02   08   setting the strong constraints and the breaking threshold v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9TNDsfFNoq4)
**Author:** The VFX School Archive
**Duration:** 12m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, let's bring in uh the rest of the uh these um cables now. So, I'm going to come to here and disable that delete blast node. Okay. So, that will cycle through all of those now. So, it'll take a little bit of time. There we are. So, we got all the uh all the cables coming through there. Now I want to make uh the kind of these longer pieces here. I want to make them the attach constraints unable to break there. Okay. So the ones kind of nearer the back while doing tests. So some of these seem to be breaking uh too early. So I've decided to make uh these at the back unable to come away from the from the um from the bridge. Okay. And also, you know, that part of the bridge doesn't fall anyway. So, I'm dropping an object merge here. And I'm going to bring in um Oh, we've already got it actually. Yeah. Sorry. Uh just alt click and drag. Bring this over. Or we could use the same one, but well, I'll just uh stick with this one. So, let's drop a time shift and go to the last frame on this. um delete channels there and go to frame 250. Okay. So yeah, obviously this part doesn't ever fall. And so it stands to reason that these cables shouldn't break, right? So, ...

**Frame:** tutorials\frames\week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Enabling all bridge vertical cables in the Vellum sim and differentiating constraint break strength — making rear-section cable attach constraints unbreakable while allowing forward-section cables to snap at a tuned threshold, driving the visual cable-snapping destruction effect.

### Summary
With a single test cable working, the Delete/Blast node isolating it is disabled so all cables enter the sim together. The instructor identifies that rear bridge cables should never detach (the rear section of the bridge remains intact), so those attach constraints are flagged as unbreakable using a geometry-based selection combined with a TimeShift to the last frame. A break threshold is then set on the remaining forward cables, controlling at what stress value they snap — producing the signature bridge cable snap effect during destruction.

### Key Steps
1. [`Blast SOP`] Disable the isolating Blast node to include all cable geometry
2. [`Object Merge`] Bring in rear bridge section geometry for spatial reference
3. [`TimeShift SOP`] Sample the rear bridge geo at the last frame (e.g. frame 250) to confirm it never falls
4. [`Attribute Wrangle`] Set `breakthreshold` attribute to a very high value (unbreakable) on rear cable constraints
5. [`Attribute Wrangle`] Set tuned `breakthreshold` on forward section cable constraints
6. [`Vellum Solver`] Run full cable sim; verify rear cables hold and forward cables snap at collapse
7. [Iterate] Adjust break threshold values until snap timing matches the desired destruction beat

### Houdini Nodes / VEX / Settings
- `breakthreshold` attribute — per-constraint Vellum attribute; controls the stress value at which a constraint is deleted
- `TimeShift SOP` — freezes geometry to a specific frame for spatial queries; used here to sample final bridge position
- `Object Merge` — references geometry from another area of the network for constraint spatial selection
- `Blast SOP` — used earlier to isolate test cables; disabled here to restore all cables

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Starting the Vellum Sim](week-02-07-starting-the-vellum-sim-v1-1080p.md) — the preceding step that established the Vellum wire setup
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — foundational Vellum concepts including constraint attributes
- [Starting the Guided Sim](week-02-03-starting-the-guided-sim-v1-1080p.md) — the Bullet guided sim for horizontal cables, parallel to this Vellum work
