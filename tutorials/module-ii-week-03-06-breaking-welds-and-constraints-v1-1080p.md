---
title: module ii   week 03   06   breaking welds and constraints v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=dfD5FUdMCTc
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 19"
tags: [dop, vellum, attributes, vex, advanced]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p/
frame_count: 4
---

# module ii   week 03   06   breaking welds and constraints v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=dfD5FUdMCTc)
**Author:** The VFX School Archive
**Duration:** 11m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right. So, we're pretty much ready to uh to run our cache here. Um I just want to organize this a bit better before I forget. I noticed just put the names here. And let me see the stitch is what's that doing? The collar. Okay. And then also in this weld, which is here, I just want to turn on braking. Set that to one. Okay. So because I want to um I want to change that as as we uh as we progress through the through the simulation, right? So the longer into the simulation, the weaker I want that to become. So I can't animate it here. So I'm going to do that inside the solver, right? Um and we're also going to be animating uh if you remember the the left boot, right? So um we want we don't need to turn on braking here. Um but within the Sovia we can um basically delete those constraints at at a certain point right so if we look at the crocodile simulation the animation you know there's a part here so he flips over and I think yeah around there so the you know the body's going to be flipping round well actually we can see here he's going to be like that and I think it'd be good if the the boot kind of flies off as he's flipping over. Okay. So, at, you know, ...

**Frame:** tutorials\frames\module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Dynamically breaking Vellum weld and stitch constraints at specific simulation times using a SOP Solver inside the Vellum DOP network, since break thresholds cannot be keyframed directly on the Vellum nodes themselves.

### Summary
The collar stitch and boot attachment constraints need to break at a specific frame when the crocodile flips the hunter over. Weld breaking is enabled via the "breaking" checkbox on the Vellum Weld node with a break threshold of 1. Because the break threshold cannot be keyframed directly on the Vellum node, a SOP Solver inside the DOP network is required to modify the constraint geometry per frame: a wrangle reads the current frame and lowers the break threshold along a time ramp using `f@breakthreshold = fit($F, start, end, 1.0, 0.01);`. The boot attachment is handled differently — at the specific flip frame, the boot constraints are deleted entirely using a Delete SOP gated on `$F > threshold`, producing a clean instant detach. The general pattern established is that a SOP Solver inside Vellum DOPs is the standard way to animate any Vellum constraint attribute over time.

### Key Steps
1. [`Vellum Weld`] Enable the "breaking" checkbox; set break threshold to 1
2. [`SOP Solver` (inside DOPs)] Add to allow per-frame modification of constraint attributes
3. [`Attribute Wrangle`] Ramp the break threshold down over time: `f@breakthreshold = fit($F, start, end, 1.0, 0.01);`
4. [`Delete SOP`] For the boot attachment, delete constraints entirely when `$F > threshold` for an instant clean detach
5. [Verify] Confirm collar and boot constraints break at the intended flip frame, not before or after

### Houdini Nodes / VEX / Settings
- `Vellum Weld` (breaking enabled) — stitch/weld constraints that can fail once stressed past threshold
- `SOP Solver` (inside DOPs) — required pattern for animating any Vellum constraint attribute, since Vellum nodes don't support direct keyframing
- VEX: `f@breakthreshold = fit($F, start, end, 1.0, 0.01);` — time-ramped threshold reduction
- `Delete SOP` gated on `$F > threshold` — instant clean constraint removal for the boot detach

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)

---

## Related Tutorials
- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — the cloth setup whose collar stitch is broken here
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the week this animated breaking technique supports
- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — a parallel time-driven attribute-animation pattern from the RBD context
