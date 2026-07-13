---
title: Christmas lights vex animation in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=u7SGkPTaJKs
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H18+)"
tags: [vex, animation, instancing, lighting, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/christmas-lights-vex-animation-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Christmas lights vex animation in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=u7SGkPTaJKs)
**Author:** cgside
**Duration:** 4m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello there and welcome back.
[0:02] So in this tutorial we're going to create the Christmas lights animation with Odini.
[0:07] So this is my final setup with some lead strip, but we're going to build a simple example.
[0:14] Let's start by creating a light and set it to sphere.
[0:18] Now we need an instacer to instance the light.
[0:23] We're going to use a simple line with a few points.
[0:28] As we can't really instance lights, let's set the instacer to reference and we should have duplicates of the lights on the line points.
[0:38] Here I'm just pruning the original light so it doesn't render.
[0:46] Now inside the instacer we will create an attribute called intensity so we can use it later.
[0:52] Just link the light intensity to the value of the attribute create.
[0:57] Next I want to create a pattern of four colors repeating along the line.
[1:03] So let's create a for loop to automate the process.
[1:06] We will need detailed attributes from the metadata node, so create one.
[1:13] Now we can use a group by range to select all the points within a pattern.
[1:18] As we need for colors select one out of four in the range.
[1:22] And then we can use the offset to create the different groups of colors.
[1:27] Let's set the number of iterations to four and use the iteration value in the offset of the range node.
[1:37] And also rename it group with the iteration value.
[1:42] As you can see we have all the different groups at the end of the loop.
[1:48] Now creating all the different colors and targeting the groups from before.
[1:54] In order to assign each color to a different group we will use a switch with the input set to the iteration value.
[2:05] And we now have a pattern of four colors on the lights.
[2:08] The only thing missing is the animation.
[2:12] So inside the instacer creates a point wrangle to add some wax codes.
[2:18] I am going to load a preset for a pattern and explain how it works.
[2:23] It's quite simple maybe there are better ways of doing this.
[2:27] But this is my first time writing wax.
[2:30] Let's just connect a re-time node to cycle the animation.
[2:36] Now the codes.
[2:38] At the top I am getting the original intensity value of the lights set up in the attribute create.
[2:45] Then for 36 frames we will create the first animation pattern.
[2:50] So for every two frames and if the point number is even or for every other two frames and point number is odd,
[2:59] set the intensity of the light to the original value.
[3:05] While turning off the light when it doesn't match the pattern.
[3:09] After the first pattern till frame 54 for every other frame and if the point is even,
[3:16] the red and yellow lights turn on and off the intensity.
[3:21] And we do the same in the last pattern for the green and blue lights.
[3:26] Finally we set the intensity point attribute.
[3:30] And this is the pattern that it creates nothing complicated really.
[3:34] And you can easily change this code to create other patterns.
[3:38] For my sample scene I just created a lead strip and instance the lights in the points.
[3:44] And this is it really simple stuff but hopefully you picked up a few tips.
[3:49] Let me know how would you approach this in a different way.
[3:53] Maybe with a simple expression or some other setup.
[3:57] Thank you for watching and see you in the next one.
[4:00] Happy Holidays!



---

## Captured Frames

- [0:38] tutorials/frames/christmas-lights-vex-animation-in-houdini/frame_000.jpg
- [1:22] tutorials/frames/christmas-lights-vex-animation-in-houdini/frame_001.jpg
- [2:05] tutorials/frames/christmas-lights-vex-animation-in-houdini/frame_002.jpg
- [2:38] tutorials/frames/christmas-lights-vex-animation-in-houdini/frame_003.jpg
- [3:30] tutorials/frames/christmas-lights-vex-animation-in-houdini/frame_004.jpg
- [3:44] tutorials/frames/christmas-lights-vex-animation-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
Instances a light onto points along a line (or LED strip curve), assigns a repeating 4-color pattern via a for-loop of Group by Range + Switch nodes, then uses a single point wrangle with frame/point-number logic to animate each light's intensity through three sequential blink patterns.

### Summary
A short, beginner-friendly example of instancing actual light objects (not geometry) and driving their per-instance intensity with VEX. Since lights can't be instanced via the normal geometry-instancing path, the trick is setting the Instancer's method to **Reference** so it duplicates the light object itself onto each point, then pruning the original so it doesn't render directly. Each instance gets an `intensity` point attribute (linked to the light's actual Intensity parameter) that VEX can drive per-point. Color variety comes from a for-loop building four alternating groups via **Group by Range** (using the loop's iteration value as the range offset) and assigning a distinct color to each via a **Switch** keyed on that same iteration value. The animation itself is one point wrangle (the author's first time writing VEX, done from a preset/pattern they explain rather than derive) that reads each point's original intensity, then for three sequential frame windows (first ~36 frames, then up to frame 54, then to the end) alternates which lights are lit based on `frame % 2` and whether the point number is even or odd — different point parity/color groups take turns being lit in each phase — feeding into a **Retime** node so the whole sequence loops.

### Key Steps
1. Create a **Light** (set to sphere shape) and a simple **Line** with a handful of points to act as the LED positions.
2. Add an **Instancer**, set its instancing **Method to Reference** (not the default geometry-instance path) pointing at the light — since lights aren't regular geometry, Reference mode is what allows duplicating the light object itself onto every line point.
3. **Prune** the original light object so only the instanced copies render, not the source.
4. Inside the instancer, add an **Attribute Create** for a float `intensity` attribute, and link the light's actual Intensity parameter to reference that attribute's value — this exposes intensity as something VEX can drive per point.
5. **Color pattern via a for-loop**: bring in **Detail** metadata (for the loop's iteration count), then inside the loop use **Group by Range** to select every 4th point (one group per color slot), offsetting the range by the current iteration value each pass, and renaming the group using that iteration value so 4 distinct point groups exist after 4 iterations.
6. Outside the loop, create four distinct **Colors** and assign each to its matching group using a **Switch** node keyed on the iteration value — this produces a clean repeating 4-color pattern across the instanced lights.
7. **Animation via a single point wrangle** (inside the instancer): at the top, read each point's original intensity (from the earlier Attribute Create) into a variable. Then, using `frame`/`$F`-style checks and `point number % 2` parity tests, implement three sequential timed phases: (a) up to frame ~36 — every other frame, alternate even/odd points on/off at the original intensity, turning off intensity when a point doesn't match the current frame's pattern; (b) up to frame ~54 — every other frame, only even points among the red/yellow-colored lights turn on/off; (c) remaining frames — same logic applied to the green/blue-colored lights. Finally, write the computed value back to the intensity point attribute.
8. Add a **Retime** node so the (finite, hand-authored) animation window loops continuously rather than playing once.
9. For a real production version, apply the same instancer + wrangle setup to a proper LED-strip curve instead of a simple line — same technique, just driven by a more complex/curved point layout.

### Houdini Nodes / VEX / Settings
Light (sphere) + Line → **Instancer** (Method: Reference) + Prune (hide source light) → Attribute Create (`intensity` float, linked to Light Intensity parameter) → for-loop: Detail (metadata/iteration count) → **Group by Range** (offset by iteration value, renamed per-iteration) → Switch (color assignment keyed on iteration value) → point **Wrangle** (frame-number + point-number-parity conditional logic driving the `intensity` attribute across three sequential animation phases) → **Retime** (loop the cycle).

### Difficulty
Beginner / Intermediate — the instancing-a-light trick (Reference method + Prune) and the for-loop group-pattern construction are approachable beginner techniques; the animation wrangle's nested frame/parity conditionals are a bit more involved but still simple VEX (the author notes it was their first time writing VEX and that better approaches likely exist).

### Houdini Version
Not stated explicitly; uses standard Instancer/Attribute Create/Group by Range/Switch/Wrangle/Retime nodes available in any modern Houdini (H18+).

### Tags
#vex #animation #instancing #lighting #beginner #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers light instancing or intensity-driven VEX animation — cross-link with any future lighting or VEX-animation tutorials once extracted from this batch.
