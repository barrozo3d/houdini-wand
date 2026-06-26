---
title: module i   week 02   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=G1JI3ACUZN4
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, destruction, glass, metal, wood, plasticity, course-intro, beginner]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-01-intro-v1-1080p/
frame_count: 4
---

# module i   week 02   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=G1JI3ACUZN4)
**Author:** The VFX School Archive
**Duration:** 1m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Right, welcome to week two of the ABD module. And this week we're looking at a bus stop. So it's kind of a, I suppose, a strange thing to choose, but the reason we're doing that is because of the range of materials that we've got. So we're focusing on mixing materials and being able to destroy them all together. So we've got obviously the metal of the frame of the bus stop. We are looking at glass fracturing and wood as well. And that gives us a nice kind of variety of stuff going on there. So yeah, in the first week, we looked at concrete stone kind of thing, which is very common. Now we're doing this metal and wood and glass. And we're really utilizing some of the new tools that are provided by side effects. So we're using the ABD material fracture node to create the wood and the glass. We're using the plasticity, which is a new thing. I think in Houdini 18, if I'm not mistaken, for the soft constraints to get the metal kind of holding it shape, you know, so it doesn't spring back into where it got, which works really well in my opinion in this project. You know, it kind of holds and bends and creaks and pops when it breaks. You know, it has a really nice metal effect. And yeah, we're kind of bringing it all together in two separate simulations. So the first simulation for the big, heavy metal. And then after that, once we're done, we use the metal to simulate the glass and the wood. And a couple of little tips and tricks along the way as well.

**Frame:** tutorials\frames\module-i-week-02-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Week 2 RBD bus stop destruction with mixed materials (metal/glass/wood), RBD Material Fracture, plasticity for soft constraints, and two separate simulations.

### Summary
1m41s intro for Module I Week 2. Bus stop destruction project: metal frame, glass panels, and wood benches all destroyed together. Key new tools introduced: RBD Material Fracture node for glass and wood fracture, plasticity (H18) for soft metal constraints that bend/creak/pop instead of springing back. Two simulations: first the heavy metal, then glass and wood driven by the metal result.

### Key Steps
- Project: bus stop with metal frame + glass + wood bench
- RBD Material Fracture node: generates glass and wood fracture patterns
- Plasticity (H18 feature): soft constraints that plastically deform — metal bends and stays bent, creaks/pops
- Pipeline: Sim 1 (heavy metal frame) → use metal result to drive Sim 2 (glass + wood)
- Focus: mixing RBD materials and their interaction in a single destruction sequence

### Houdini Nodes / VEX / Settings
- **RBD Material Fracture** — fractures based on material type (glass/wood patterns)
- **Plasticity** (H18) — constraint property for permanent plastic deformation (metal bending)

### Difficulty
Intermediate (context video)

### Houdini Version
H18.5

### Tags
[rbd, destruction, glass, metal, wood, plasticity, course-intro, beginner]

---

## Related Tutorials
- module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1.md (post-sim setup continuation)
- module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md (deforming metal/glass post-sim)
- module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md (RBD disconnected faces + wood fix)
