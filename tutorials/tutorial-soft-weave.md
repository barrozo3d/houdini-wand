---
title: [Tutorial] Soft Weave
source: YouTube
url: https://www.youtube.com/watch?v=Ohj4ag8DZRo
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, vex, procedural, curves, attributes, modelling, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-soft-weave/
frame_count: 4
---

# [Tutorial] Soft Weave

**Source:** [YouTube](https://www.youtube.com/watch?v=Ohj4ag8DZRo)
**Author:** Alexander Eskin
**Duration:** 36m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's start with a June node. Start with a dot on the left over here. Select a blue bracket over here. Now click the blue declaration and the blue arrow. And then click it to indicate an gradient layer to so that it doesn't have any shadings. 2 minus now it's in the center. Make it 2000 points for starters. Now we need some sort of the attribute for moving the points around. It could be the rest attribute or curview. I would use curview. Curview, do not resemble, just generate curview. Now we have the attribute and just create the basic structure. Wiring, I'm going to create the wiring using sine function. v starting with y v at p y equals sine curview. So now it looks like this. The amplitude is too big. The frequency is too low. The amplitude is the thing after the brackets. The frequency is multiplied inside the brackets. 100. Now we have the sine wave. Now we just copy that say p x. Since the frequency is the same, it looks like this. But if we divide the frequency by two, now we have something that resembles the weaving pattern. To make it a bit more convenient to work with, I would create some sliders for the amplitude and frequency for every axis. So the base scale wou...

**Frame:** tutorials\frames\tutorial-soft-weave\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedural woven fabric/cable geometry using VEX sine functions on `curveu` — Y axis uses `sin(curveu * freq_y)`, X axis uses `sin(curveu * freq_x / 2)` (halved frequency creates the interlocking weave pattern). No simulation — pure SOP math. English-language companion to the Russian "Мягкая Ткань".

### Summary
A 36-minute English tutorial by Alexander Eskin building procedural woven fabric geometry via VEX sine math on a 2000-point line. The key insight: Y gets `sin(@curveu * 100)` and X gets `sin(@curveu * 50)` — dividing X frequency by 2 creates the characteristic interlocking weave pattern (not just parallel waves). Amplitude = coefficient outside brackets; frequency = multiplier inside brackets. Sliders promoted for amplitude and frequency per axis. Frame 002 confirms tight woven cable-link geometry.

### Key Steps
1. Geo node → `line` SOP — 2000 points; center at origin
2. `resample` SOP (or wrangle) → generate `curveu` attribute (0→1)
3. `attribwrangle` "wiring":
```vex
// Context: Point Wrangle — woven fabric via sine
float freq  = ch("frequency");       // base frequency (e.g. 100)
float ampY  = ch("amplitude_y");
float ampX  = ch("amplitude_x");
float scale = ch("base_scale");

// Y: full frequency sine wave
v@P.y = sin(@curveu * freq * scale) * ampY;

// X: HALF frequency — creates interlocking weave (not parallel)
v@P.x = sin(@curveu * (freq / 2.0) * scale) * ampX;
```
4. Promote `frequency`, `amplitude_y`, `amplitude_x`, `base_scale` as ch() sliders
5. Start with freq ~100 → 100 loops visible; halve X freq for weave cross-pattern
6. Distribute strands via `copytopoints` or for-each on a grid
7. `sweep` SOP for strand thickness; render with glass/metal material

### Houdini Nodes / VEX / Settings
- `line` SOP — 2000 points, centered
- `resample` SOP — `curveu` attribute generation
- `attribwrangle` — `sin(@curveu * freq)` on Y; `sin(@curveu * freq/2)` on X
- VEX: `ch()` for parameter sliders — amplitude_y, amplitude_x, frequency, base_scale
- Key rule: **amplitude = coefficient OUTSIDE brackets; frequency = multiplier INSIDE brackets**
- `copytopoints` or for-each — strand distribution
- `sweep` SOP — cross-section

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, vex, procedural, curves, attributes, modelling, intermediate

---

## Related Tutorials
- [[урок-мягкая-ткань]] — Russian companion tutorial (same technique, 43 min)
- [[houdini-tutorial-make-any-geometry-knitted]] — related textile procedural using UV projection
- [[vops-02---random-noise---houdini-beginner-tutorial]] — sine/cosine in VOP context
