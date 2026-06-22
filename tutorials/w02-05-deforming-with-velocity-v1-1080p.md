---
title: w02   05   deforming with velocity v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=IuvtudgbzLw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18"
tags: [sop, attributes, vex, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/w02-05-deforming-with-velocity-v1-1080p/
frame_count: 4
---

# w02   05   deforming with velocity v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=IuvtudgbzLw)
**Author:** The VFX School Archive
**Duration:** 7m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en As I I believe I mentioned earlier, we're going to be using velocity as one of our attributes for displacing this geometry. And at the moment, if we take a look, well, we come right to the file node, select that, and then go to geometry spreadsheets, we can see what we've got. The attributes we currently have on the points just position, got normal and UVs. And primitive, we just got a couple of groups for the two different blueberries, and nothing in detail. So, we don't have our velocity attributes yet. So, we need to go ahead and and make that. So, if we take a trail sop. So, by default, if we I don't know if you'll see much here. Let's stretch that length. It'll kind of Yeah, you can see it's kind of copying the the geometry there. Making like a almost like a tail in the geometry. Let me turn this off. But we don't want that. Okay, I'm going to put this back to default and change this to compute velocity. So, this is handy also for um your motion blur if you're working with geometry with animation, and if you don't have a velocity on it, and you want to render motion blur, this is quite a common thing that I that I do and and others to to get that. A...

**Frame:** tutorials\frames\w02-05-deforming-with-velocity-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Using the Trail SOP in Compute Velocity mode to generate a velocity attribute on animated geometry, then transferring and using that velocity to displace a surface mesh — a reusable no-simulation technique for fluid-like deformation and motion blur.

### Summary
Starting from blueberry geometry with only position, normals and UVs, the instructor adds a velocity attribute using the Trail SOP set to "Compute Velocity" rather than its default trail mode. This `v` attribute is then used to drive positional displacement of the yogurt surface. The instructor also notes this is a standard technique for adding motion blur to animated geometry that lacks velocity in Arnold or Mantra. The velocity is scaled and applied per point in a wrangle for art-directable control over the splash shape.

### Key Steps
1. [`Geometry Spreadsheet`] Confirm no `v` attribute exists on the falling blueberry points
2. [`Trail SOP`] Drop Trail SOP; switch mode from "Trail" to "Compute Velocity"
3. [Verify] Check Geometry Spreadsheet to confirm `v` attribute now exists per point
4. [`Attribute Transfer SOP`] Transfer `v` from blueberry geo onto yogurt surface mesh by proximity
5. [`Attribute Wrangle`] Scale transferred velocity: `@P += @v * ch("scale");` with art-directable parameter
6. [Iterate] Adjust scale and blend to taste; check deformation in viewport
7. [Motion Blur note] Same `v` attribute is used by renderers (Arnold/Mantra) for geometry motion blur

### Houdini Nodes / VEX / Settings
- `Trail SOP` (Compute Velocity) — derives `v` from positional delta between frames without adding actual trail geometry; standard velocity-generation pattern
- `Attribute Transfer SOP` — blends attribute values from source to destination by point proximity and distance falloff
- `Attribute Wrangle` VEX: `@P += @v * ch("scale");` — point-level displacement along velocity direction
- Motion Blur — any renderer reading `v` on geometry uses it for subframe position interpolation; Trail SOP is the standard way to add this

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)

---

## Related Tutorials
- [Tabletop Week 02 Intro](w02-01-introduction-v1-1080p.md) — the week overview introducing this velocity deformation strategy
- [Module I Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — post-sim point deformation using similar attribute transfer patterns
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the next week comparing this fake technique against real FLIP
