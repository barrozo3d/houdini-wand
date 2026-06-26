---
title: module i   week 05   01   importing the geometry v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Fo3HaNq9f8M
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [alembic, import, time-shift, flip-fluids, pop-fluid, beginner]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-05-01-importing-the-geometry-v1-1080p/
frame_count: 4
---

# module i   week 05   01   importing the geometry v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=Fo3HaNq9f8M)
**Author:** The VFX School Archive
**Duration:** 2m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, so here I am in a fresh Houdini scene and I'm going to create a new project. What am I doing? New project. We are in module one and it's week five. And this goes into D. Go accept. Go ahead and find that project and I'm going to drag in the horse Olympic file. So just leave that in there. And then we'll save it as well. Save as. And we call this horse pop fluid. There's one. Accept. Okay, and then just show you see the we get the hip file in there. So it's great. And then we'll bring in that horse first, create a geometry file called this horse. And type inside press. We want an Olympic. So press P to get my parameters. Find the horse. So hip and then ABC horse accept. And there's our lovely horse with the animation. So we need to at the moment you can see this is kind of like we don't have access to the geometry. So just drop a convert. First and then we can select polygons. I also want to if we turn on the real time toggle there, I want this to be pretty slow. So I'm going to use a time shift. And turn off integer frames. And I'm going to set this multiply this by 0.3. So it's really slow. And change this to dollar. I think any dollar FF. I'm not sure. So this will give me float frames for the simulation for sub steps within a simulation. But yeah, well, we can check if we go like like that. You can see we get information between frames, which is good. There we go. There we leave it there and then we'll be sourcing into our creating the source in a moment.

**Frame:** tutorials\frames\module-i-week-05-01-importing-the-geometry-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Import Alembic animated horse geometry into Houdini, convert to polygons, and slow down time with Time Shift (×0.3, float frames via `$FF`) for use as a POP fluid source.

### Summary
2m42s setup lesson (VFX School Module I Week 5: horse POP fluid). Creates new project, imports Alembic horse animation, drops Convert SOP to get access to polygons, then uses Time Shift with `$FF` (float frame variable) and multiplier 0.3 to slow animation to 30% speed — critical for proper fluid sourcing with substeps.

### Key Steps
1. New project → horse_pop_fluid scene
2. Alembic SOP: import horse.abc; press P → browse to file
3. Convert SOP → select polygons (unlocks geometry access from Alembic container)
4. Time Shift: turn off integer frames; multiply `$FF` by 0.3 → slows animation to 30%
   - `$FF`: float frame (includes sub-frame values between integers, unlike `$F`)
   - Required so the slow animation is smooth when solver cooks at sub-frame intervals

### Houdini Nodes / VEX / Settings
- **Alembic SOP** — import animated .abc file; Press P to set file path
- **Convert SOP** → select polygons — unlock geometry from Alembic container for manipulation
- **Time Shift SOP** — `$FF * 0.3` — use `$FF` (float frame) not `$F` for sub-frame accuracy; "integer frames" = off
- `$FF` vs `$F`: `$FF` includes fractional frame values for substep evaluation

### Difficulty
Beginner

### Houdini Version
H18.5

### Tags
[alembic, import, time-shift, flip-fluids, pop-fluid, beginner]

---

## Related Tutorials
- module-i-week-04-01-introduction-to-particles-v1-1080p.md (Week 4 particles intro)
- module-i-week-06-01-introduction-to-grains-v1-1080p.md (Week 6: grains)
