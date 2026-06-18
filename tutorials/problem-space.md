---
title: Problem-Space
source: YouTube
url: https://www.youtube.com/watch?v=nUwA8xsmnS0
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["attributes", "rest-position", "uv", "world-space", "object-space", "simulation", "instancing", "procedural", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/problem-space/
frame_count: 4
---

# Problem-Space

**Source:** [YouTube](https://www.youtube.com/watch?v=nUwA8xsmnS0)
**Author:** Houdini.School
**Duration:** 1m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, I'm Kevin. I'm a technical artist and TD at Buck Design in Los Angeles. I love digital tinkering, understanding the way things work, and reframing things in a different perspective. All these things come together in my class, problem space. We start the course by experimenting with how we can manipulate attributes like color and UV using classic world space transforms, as well as the rest position. Next, we'll expand on the technique by manipulating courses for simulations and instances. Finally, we'll be supercharging our favorite stops by distorting their input space and bending them to our will. By the end of the course, you'll be able to bring a new level of creativity and control to some of your favorite tools and workflows, or the curiosity to trailblaze one of your own. Learn more, visit my course problem space at Houdini.school.

**Frame:** tutorials\frames\problem-space\frame_000.jpg


---

## Structured Notes

### Core Technique
Manipulating attribute lookup space in Houdini — distorting world space, object space, rest position, and UV space to gain creative control over color, texture, simulation behavior, and instance placement in SOPs.

### Summary
Kevin (Technical Artist/TD at Buck Design) presents a course on problem-space thinking in Houdini — the technique of distorting the coordinate space in which attributes are evaluated rather than the attributes themselves. The course starts with world space and rest position manipulation for color and UV attributes, then expands to using space distortion for simulations and instances, and finally covers "supercharging" favorite SOP nodes by feeding them manipulated input space. This is an advanced conceptual course that teaches a transferable reframing skill applicable to any Houdini workflow.

### Key Steps
1. Understand world space vs. object space vs. rest position in Houdini attributes
2. Use the Rest SOP to capture a pre-deformation position and use it as attribute lookup space
3. Manipulate color and UV attributes using world space transforms
4. Distort the rest position to achieve animated texture-sticking on deforming geometry
5. Apply the technique to simulation outputs — e.g., making textures stick to a Vellum cloth sim
6. Extend space distortion to instanced geometry for coherent instance texturing
7. Distort the input space of existing SOP nodes (Mountain, Noise) to achieve new behaviors
8. Experiment with non-Euclidean space distortions for creative effects

### Houdini Nodes / VEX / Settings
- Rest SOP (rest position capture)
- Attribute Wrangle (space manipulation)
- UV Project / UV Texture SOP
- Mountain SOP (with distorted input space)
- Noise VOP (space-distorted input)
- Transform SOP
- Copy to Points / Instancing
- VEX: @rest, @uv, @Cd attributes

### Difficulty
Advanced

### Houdini Version
unspecified

### Tags
attributes, rest-position, uv, world-space, object-space, simulation, instancing, procedural, advanced

---

## Related Tutorials
- [Attributes](attributes.md) — foundational understanding of attribute types and classes required for this course
- [Noise](noise.md) — noise manipulation is one of the primary spaces that gets distorted in problem-space techniques
- [Surface Advection](surface-advection.md) — surface-constrained space is another form of non-standard space manipulation
