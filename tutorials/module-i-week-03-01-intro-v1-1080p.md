---
title: module i   week 03   01   intro v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=QkzF0SC76qY
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, destruction, car-crash, metal, glass, constraints, course-intro, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-03-01-intro-v1-1080p/
frame_count: 4
---

# module i   week 03   01   intro v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=QkzF0SC76qY)
**Author:** The VFX School Archive
**Duration:** 1m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, here we are at week three and for the last two weeks, so week three and four, we're doing one big project. We're finishing with a car crash show. We've got a car kind of, we've got a nice animation of a car sliding inside ways and then we're going to jump into a simulation where the car kind of slams into a post and we've got lots of kind of metal bending and glass smashing everywhere. But in the third week we're just looking at the metal. We're spending quite a bit of time in this in the third week at kind of isolating and organizing the car because it's quite a complex piece of geometry. We've got lots of different pieces and it's quite detailed. It's a really nice model of the car. So we've got to go through there and select pieces that we want to actually simulate to make it bend like metal. We're doing a lot to try and make it more efficient so the simulation time doesn't actually take too long in the end. It goes pretty fast but we've got a really nice result. And also we're doing the wheels. The wheels are obviously spinning. They just spin a little. They don't need to because we're sliding sideways. But we're having to use contrus constraints and soft constraints to simulate the a little bit of bounce for the suspension and obviously allow the wheels to move around a little and spin around the axis as well. And then in the next week we move on to the rest of the simulation.

**Frame:** tutorials\frames\module-i-week-03-01-intro-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Course intro only — Week 3 of a 2-week car crash RBD project: organizing complex car geometry, isolating metal bending pieces, wheel suspension with constraints.

### Summary
1m37s intro for Module I Week 3. Two-week car crash project: animated car slides sideways and slams into a post. Week 3 = metal setup (geometry organization, selecting pieces for plasticity bending, efficiency optimization, wheel constraints). Week 4 = rest of simulation (glass, other elements). Wheels use control constraints + soft constraints for suspension bounce and free spin around axis.

### Key Steps
- Complex car geometry → select/isolate pieces for RBD simulation
- Metal bending: plasticity/soft constraints for permanent deformation
- Wheels: controlled with constraints (spin on axis, suspension bounce via soft constraints)
- Week 3: metal only. Week 4: rest of sim (glass, etc.)

### Houdini Nodes / VEX / Settings
- Plasticity / soft constraints — wheel and metal bending
- Control constraints — wheel spin axis

### Difficulty
Intermediate (context video)

### Houdini Version
H18.5

### Tags
[rbd, destruction, car-crash, metal, glass, constraints, course-intro, intermediate]

---

## Related Tutorials
- module-i-week-02-01-intro-v1-1080p.md (Week 2 bus stop project)
- module-i-week-04-01-intro-v1-1080p.md (Week 4: continuation of car crash)
