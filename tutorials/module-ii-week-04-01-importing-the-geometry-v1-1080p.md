---
title: module ii   week 04   01   importing the geometry v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=uPPW2sI_oyw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [dop, sop, rbd, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-04-01-importing-the-geometry-v1-1080p/
frame_count: 4
---

# module ii   week 04   01   importing the geometry v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=uPPW2sI_oyw)
**Author:** The VFX School Archive
**Duration:** 3m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, here we are in week four. So, as usual go ahead and create a new project file, new project. And where are we? Module two week four And this will go into the D drive. Okay, accept, creates that. And before I forget, save as into job there, that's fine. So, what are we doing here? Let's call it collapse um version one. So, just go ahead and navigate to that um project and then um we'll go into geo, no, ABC alembics as that's what we've got. And then drag in I've already unpacked these um these skyscrapers, okay? So just do that and I'll bring that out of the way again. I'm going to delete these. Create a new geometry node. Call this uh tower or let's call it skyscraper. Okay, dive inside there. Drop in alembic. And then I'm going to press P on my keyboard, go inside and go into geo. It's not there. Why is that? Oh. Let me try just deleting that and making another alembic. I'm not sure why that's not coming up. Oh, there we go. Uh into hip ABC, there we go. And I'm going to grab uh LOD three. Open that. So, if we press uh spacebar and F, we can see it's really big. Again, so just like before, transform. Set that to uh 0.01. Okay, visualize that. Space...

**Frame:** tutorials\frames\module-ii-week-04-01-importing-the-geometry-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Importing a multi-LOD skyscraper Alembic for a realistic downward-collapse simulation, and introducing the "active attribute" pipeline that activates pieces progressively as a wave propagates from the impact point.

### Summary
Uses a different skyscraper Alembic asset with multiple LODs available, selecting LOD3 for simulation. The import workflow mirrors Week 2: Alembic SOP -> Transform at 0.01 scale -> visual check. The week's concept is a realistic downward collapse where the building folds and pancakes floor by floor, with separate simulation of concrete slabs, steel rebar/frame, and glass panes. Sets up the "active attribute" pipeline: pieces start inactive (kinematic) and become active (simulating) based on a wave propagating downward from the impact point. This lesson covers only the geometry import and scale step; the active-attribute technique itself is covered in the Renascence 2.0 gap-filler lesson 09.

### Key Steps
1. [Import Alembic] Select LOD3 of the skyscraper asset for simulation-resolution geometry
2. [`Alembic SOP`] Import; `Transform SOP` scale to 0.01 to match Houdini scene units
3. [Material separation] Plan separate simulation streams for concrete slabs, steel frame and glass panes
4. [Active-attribute pipeline] Establish that pieces will start kinematic (`active=0`) and switch to simulating (`active=1`) as a wave propagates from the impact point — implemented in the linked gap-filler lesson

### Houdini Nodes / VEX / Settings
- `Alembic SOP` + `Transform SOP` (0.01 scale) — same import pattern as Module II Week 2
- Active attribute pipeline — pieces toggle from kinematic to simulating based on distance/wave from impact; full implementation deferred to a gap-filler lesson

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)

---

## Related Tutorials
- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — the gap-filler lesson implementing the active-attribute technique referenced here
- [Splitting by Material](module-ii-week-03-01-splitting-by-material-v1-1080p.md) — the preceding multi-material fracture week
- [City Ground Destruction Intro](module-i-week-01-01-intro-v1-1080p.md) — a later course's parallel staged-destruction setup
