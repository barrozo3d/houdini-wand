---
title: week 02   03   starting the guided sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9qkYzPC9IKM
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [rbd, simulation, dop, attributes, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-03-starting-the-guided-sim-v1-1080p/
frame_count: 4
---

# week 02   03   starting the guided sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9qkYzPC9IKM)
**Author:** The VFX School Archive
**Duration:** 6m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So let's uh give these blocks some attributes. So uh they need well that's given us a name attribute which uh it looks like we got the visualizer left turned on there. Okay. So each block will have a separate name. Uh let's connect them together. So I'm not going to pack this yet. Let's give this a proper name. So, we'll call it main uh cable. Okay. And let's drop a uh RBD constraints from rules. So, into the render geometry and the proxy geometry together. Okay. Um again, I want surface points here. So, you can see we're connecting up the edges between them. Um just obviously important that they don't we don't have constraints between the the cables like that. Um so just by default like that is fine. And then RBD constraint properties. Where are we? There we go. Okay. And for this I'm not going to use soft. I'm going to use I found that hard constraints work better for me when I want something really um rigid and kind of stiff looking um like cables and also we don't need plasticity. So obviously with the soft constraints it's nice to have the plasticity for you know metal. Uh but in this case it's a cable and it's very stiff. It's not going to move a l...

**Frame:** tutorials\frames\week-02-03-starting-the-guided-sim-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Setting up the Bullet guided-simulation workflow for the bridge's horizontal cables — assigning name attributes, building hard constraints with RBD Constraints from Rules, and wiring the guide sim to inherit motion from the week-one road/metal RBD result.

### Summary
The instructor gives the cable blocks a `name` attribute so each segment is individually identifiable, then feeds them into RBD Constraints from Rules to generate surface-point-based hard constraints between adjacent pieces. Hard constraints are chosen over soft because the cables are stiff and need no plasticity. The guide simulation is then established by linking the cable RBD network to the previously cached week-one simulation so cable motion is guided by bridge collapse motion rather than solved independently.

### Key Steps
1. [`Attribute Wrangle / Name SOP`] Assign a unique `name` attribute to each cable block
2. [`RBD Constraints from Rules`] Generate surface-point constraints between cable pieces; connect render and proxy geometry inputs
3. [`RBD Constraint Properties`] Switch constraint type from soft to hard for cable stiffness
4. [`Guided Simulation SOP`] Load the week-one sim as a guide source
5. [Guide Strength] Set the strength parameter controlling how strongly pieces follow the guide
6. [Guide Release Thresholds] Configure angular and linear thresholds for when pieces detach from the guide
7. [`RBD Solver`] Run the guided cable simulation and verify cable motion follows bridge collapse

### Houdini Nodes / VEX / Settings
- `Name SOP` — assigns a string name attribute per piece, required by constraint-building nodes
- `RBD Constraints from Rules` — generates constraint geometry from proximity/rules between named pieces
- `RBD Constraint Properties` — sets constraint type (hard/soft/cone-twist) and strength
- Guided Simulation — Houdini 18 feature allowing one RBD sim to follow another; guide strength and release thresholds control the transition
- Hard Constraints — zero-compliance constraints; ideal for stiff cables that must not bend

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)

---

## Related Tutorials
- [Finishing the Horizontal Cable Sim](week-02-04-finishing-the-horizontal-cable-sim-v1-1080p.md) — continuation of this exact setup
- [Bridge Destruction Week 02 Intro](week-02-01-intro-v1-1080p.md) — overview of the cable week
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — Vellum approach used for vertical cables
