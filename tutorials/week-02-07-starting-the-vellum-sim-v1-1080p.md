---
title: week 02   07   starting the vellum sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=cecNdA8cLTo
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [vellum, simulation, dop, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-07-starting-the-vellum-sim-v1-1080p/
frame_count: 4
---

# week 02   07   starting the vellum sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=cecNdA8cLTo)
**Author:** The VFX School Archive
**Duration:** 8m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Now let's drop a vellum configure cloth. There we go. Okay. Plug this into the first input. You can see that's uh generating constraints for us. Okay. Um let's see now. Uh we want cloth. Distance along edges is fine. Uh don't need a group. That's going to be the same for everything. Leave these. uh kind of do these these work by default now as of um Houdini 18. I think they're really they work really easily for us. No, Houdini 17.5. I think this calculate varying um and thickness um really helps out. Okay. Um what else do we want? Oh, we want to set up these pin points. Okay. So that pin group we just made and this match animation is really important as well. So they follow around. Okay. Um, so the stretch stiffness, we'll leave that on. So that's really, really stiff by default. Um, now something important here, the rest length scale. I'm going to drop this down to 8. Okay, so that means these want to be um shorter than they are now. Okay, so the rest length is shorter than their current length of these constraints. So what that does, it means when the simulation starts, they'll be under tension. and they'll be pulling um on themselves, which makes sens...

**Frame:** tutorials\frames\week-02-07-starting-the-vellum-sim-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Setting up a Vellum cloth/wire simulation for the bridge's vertical hanger cables, including pin constraints, match animation, and using rest length scale below 1 to pre-tension the cables so they are taut from frame one.

### Summary
The instructor uses Vellum Configure Cloth (treated as a wire/cable) for the vertical cables. The key discovery is setting Rest Length Scale to 0.8 (below 1.0), which makes the constraints shorter than the actual geometry, placing the cables under tension from the first frame of the simulation — physically accurate for bridge suspension cables. Pin points are grouped and wired to the main cable attachment locations, and Match Animation is enabled so pins follow the animated bridge structure throughout the sim.

### Key Steps
1. [`Vellum Configure Cloth`] Drop and connect vertical cable geometry as the first input
2. [Constraint Generation] Leave Distance Along Edges at default; verify constraint lines appear
3. [Pin Group] Create a point group for cable attachment points; assign as the Pin to Animation group
4. [Match Animation] Enable Match Animation so pinned points follow the animated bridge
5. [Rest Length Scale] Set to 0.8 so constraints are shorter than rest state, placing cables under pre-tension
6. [Stretch Stiffness] Leave at high default for near-inextensible cables
7. [`Vellum Solver`] Connect and run; verify cables start taut and respond to bridge motion

### Houdini Nodes / VEX / Settings
- `Vellum Configure Cloth` — generates distance and bend constraints; used here for wire-like cable behaviour
- Rest Length Scale — multiplier on constraint rest lengths; values below 1.0 pre-compress/pre-tension the sim
- Pin to Animation — group name whose points are locked to animated positions each frame
- Match Animation — Vellum solver setting that keeps animated pin points synced to animated input geometry
- Stretch Stiffness — resistance to length change along constraint edges; high = near-inextensible

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Setting Strong Constraints and Breaking Threshold](week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p.md) — the next step adding breakable vs. unbreakable constraints
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — foundational Vellum concepts
- [Bridge Destruction Week 02 Intro](week-02-01-intro-v1-1080p.md) — week overview introducing the Vellum approach
