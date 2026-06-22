---
title: week 02   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=IoxlDdh5OPg
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rbd, vellum, simulation, dop, beginner]
extraction_status: complete
frames_dir: tutorials/frames/week-02-01-intro-v1-1080p/
frame_count: 4
---

# week 02   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=IoxlDdh5OPg)
**Author:** The VFX School Archive
**Duration:** 2m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Welcome to week two. Now in week one we have already covered the um bullet simulation of the actual road itself and the metal elements. Well the kind of uh deforming metal elements. In this week we're looking at the cables and we're going to be using um bullet for one and vellum for the other. So um but they kind of go together obviously and and the vertical cables hang from the horizontal cables. So we start out with the horizontal cables. um because they're so um heavy and rigid, you know, they don't bend a lot. We we're just going to be using um bullets for simulating them. Um now, the geometry is quite intricate with kind of uh small pieces. So, we're going to be looking at simplifying that geometry first, you know, just creating four simple strands that we going to simulate. And also because the the kind of animation we're looking for is not too um animated, I suppose. is very simple movement. Uh so we'll be using hard constraints for that and we'll actually be using the simulation that we generated in the first week to guide this simulation. So we're using the new guided sim workflow in Houdini uh with with bullet. Um so that's something new that w...

**Frame:** tutorials\frames\week-02-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Week-two overview of the Bridge Destruction course: simulating the bridge cables — stiff horizontal cables using Bullet's guided-sim workflow and flexible vertical cables using Vellum.

### Summary
The instructor introduces the cable simulation strategy, distinguishing between the heavy, near-rigid horizontal suspension cables (simulated with Bullet hard constraints driven by the week-one guided sim result) and the more flexible vertical hanger cables (simulated with Vellum). The geometry is simplified to four strands before simulation. The guided simulation workflow in Houdini 18 is introduced as a key technique for making secondary elements follow the main RBD sim without a full independent solve.

### Key Steps
1. [`File SOP`] Load the cable geometry from the bridge model
2. [`Resample / Curve`] Simplify complex cable geometry to four clean strands
3. [`RBD Constraints from Rules`] Build hard constraints between cable segments
4. [`RBD Material Fracture` / Guided Sim setup] Wire the guided sim so cables follow the week-one road/metal sim
5. [`Vellum Configure Wire`] Set up the vertical hanger cables as Vellum wires
6. [`Vellum Solver`] Run the Vellum wire simulation for vertical cables
7. [`RBD Solver`] Run the Bullet sim for horizontal cables

### Houdini Nodes / VEX / Settings
- `RBD Constraints from Rules` — procedurally generates constraints between adjacent cable pieces
- Hard Constraints — preferred over soft for stiff cable-like behaviour with no plasticity needed
- Guided Simulation (Bullet) — drives secondary sim pieces from a reference simulation result
- `Vellum Configure Wire` — sets up wire (hair/cable) constraints in Vellum
- `Vellum Solver` — solves the Vellum constraint network each frame

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Starting the Guided Sim](week-02-03-starting-the-guided-sim-v1-1080p.md) — hands-on guided sim setup for the horizontal cables
- [Starting the Vellum Sim](week-02-07-starting-the-vellum-sim-v1-1080p.md) — hands-on Vellum wire setup for the vertical cables
- [Module II Intro to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — foundational Vellum concepts
