---
title: module ii   week 01   01   basic bullet sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=vQSQgkSvm8g
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [dop, sop, rbd, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-01-basic-bullet-sim-v1-1080p/
frame_count: 4
---

# module ii   week 01   01   basic bullet sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=vQSQgkSvm8g)
**Author:** The VFX School Archive
**Duration:** 7m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Right, so here we are in week two. And this week is all about rigid body simulations. Rigid body dynamics, as they're known, RBD. So, let's create a project. So, project name will be module uh two. I said we're in week two and we're in module two, week one. Week one. Let's have a little dash there. Okay. As per usual, you save it wherever you want. Um So, we'll Yeah, we'll basically just, you know, build up in in complexity in this first um week, just looking at the the bare bones of a uh rigid body bullet simulation. And just kind of um you know, start off super simple, look at a little bit of fracturing and some constraints towards the end as well. So, let's just start with a geometry node here. And uh we'll call this RBD intro. Okay, dive inside. Let's get a box. We'll start with just the easiest way to make some kind of simulation. We'll start with a box there. Press P to get my parameters, and just uh raise it up. Maybe rotate it randomly. Don't worry about copying parameters. And then press tab and look for RBD bullet solver. Okay. Visualize that. And we've got two nodes, and we've got a simulation. I mean, it's not super interesting. It's just fal...

**Frame:** tutorials\frames\module-ii-week-01-01-basic-bullet-sim-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Introducing Rigid Body Dynamics from a bare single box, then escalating to Voronoi/Boolean fracture and a constraint network that holds pieces together until impact breaks the glue.

### Summary
Starts bare-bones: a single box, raised and rotated, then Tab -> "RBD Bullet Solver" auto-creates two nodes (RBD Configure + DOP Import) and an immediate working simulation. Escalates to Voronoi fracture: a Voronoi Fracture SOP with a point cloud controlling chunk size, then a Boolean fracture pass for sharper edges, followed by the RBD Bullet Solver on the fractured geometry. Introduces constraints for holding pieces together before shattering: an Assemble SOP adds a `name` attribute per piece, feeding a Voronoi Fracture Configure Object / Constraint Network. Explains the constraint network geometry: each constraint is a line segment between two piece centers, read by the Constraint Network DOP to link pieces. Glue constraints hold until impact force exceeds the strength threshold.

### Key Steps
1. [Bare box test] Raise/rotate a box; Tab -> "RBD Bullet Solver" shelf tool auto-builds RBD Configure + DOP Import
2. [`Voronoi Fracture SOP`] Fracture geometry using a point cloud to control chunk size
3. [`Boolean fracture`] Add a Boolean pass for sharper fracture edges
4. [`Assemble SOP`] Add a `name` attribute per piece, required for constraints
5. [`Constraint Network DOP`] Build a constraint network from line-segment geometry connecting piece centers
6. [Glue constraints] Set break strength threshold so pieces hold until sufficient impact force

### Houdini Nodes / VEX / Settings
- RBD Bullet Solver (shelf tool) — auto-creates RBD Configure + DOP Import for a quick working sim
- `Voronoi Fracture SOP` — fractures geometry based on a guide point cloud
- `Assemble SOP` — assigns a unique `name` attribute per piece, required by constraint nodes
- `Constraint Network` DOP — reads line-segment geometry (one line per constrained pair) to link pieces with glue/hard constraints

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)

---

## Related Tutorials
- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — applies these same RBD/Bullet fundamentals to bridge geometry
- [Importing the Geometry (Module II W02)](module-ii-week-02-01-importing-the-geometry-v1-1080p.md) — the following week's multi-object destruction
- [RBD Configure Deep Dive](week-01-11-rbd-configure-v1-1080p.md) — detailed look at collision proxy settings on RBD Configure
