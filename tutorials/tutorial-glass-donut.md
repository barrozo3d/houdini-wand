---
title: [Tutorial] Glass Donut
source: YouTube
url: https://www.youtube.com/watch?v=j5Ew_6-W8DE
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, vop, modelling, animation, rendering, redshift, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-glass-donut/
frame_count: 4
---

# [Tutorial] Glass Donut

**Source:** [YouTube](https://www.youtube.com/watch?v=j5Ew_6-W8DE)
**Author:** Alexander Eskin
**Duration:** 13m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Let's create your node. Let's put the last dominant. Diving side. Let's create our dark. It stores orientation x size 0.5, 0.15. Rows 400. Columns 800. Good. Now we should add some noise with point wall noise. We're going to use anti-aliased flow noise because it has the flow attribute. Let's add this noise to the current position. And this is what we got. Let's tweak the parameters a bit. Roughness should be 0.6 or takes 4. Frequency 4. These ones should be 0 and the amplitude should be 0.0.25. Here's our dominant. The anti-aliased flow noise has the flow parameter which allows us to cycle through noise. We have the 0 and 1 would be the same image all the noise. And while we scroll this or animate it, there will be some motion. We can create some loops with these. That's what we're going to do. We promote this parameter because we can't animate it. And whoops. Kill this. Small stuff. I don't need this. We don't need this. We're going to separate this. And animate it. Set the 30th phase. And animate it from 0 to 1. Set the interpolation to linear. And move this frame to 301. Otherwise, the first frame and the frame 300 will help the same noise pattern. And I'm going to have a bump ...

**Frame:** tutorials\frames\tutorial-glass-donut\frame_000.jpg


---

## Structured Notes

### Core Technique
English companion to Glass Donut RU — same `aanoise` flow loop technique with specific parameter values: torus (X orientation, rows 400, cols 800), roughness 0.6, octaves 4, frequency 4, amplitude 0.025. Seamless loop: promote `flow`, animate 0→1 linear with **end key at frame 301** (not 300) to prevent frame 1 and frame 300 having identical noise.

### Summary
A 13-minute English tutorial confirming the Glass Donut workflow with exact parameter values. Torus (X, size 0.5×0.15, 400 rows × 800 cols) + `aanoise` added to position (roughness 0.6, octaves 4, frequency 4, amplitude 0.025). Promote `flow` parameter (mandatory — can't keyframe inside VOP). Animate flow 0→1 linear; place end keyframe at frame **301** so frame 300 in a 300-frame loop never coincides with the start value. `polyextrude` for thickness + Redshift glass.

### Key Steps
1. Geo node → `torus` SOP — orientation X, size 0.5 × 0.15, rows **400**, columns **800**
2. `attribvop` or mountain — apply `aanoise` (anti-aliased flow noise), add to position
3. Noise params: roughness **0.6**, octaves **4**, frequency **4**, amplitude **0.025**
4. **Promote `flow` parameter** to node interface (required to keyframe it)
5. Keyframe `flow`: frame 1 = 0, frame **301** = 1, linear interpolation
6. Why 301: frame 300 in a 300-frame loop plays before the key, never matching frame 1 → seamless
7. `polyextrude` SOP — add thickness for glass geometry
8. Redshift glass shader + render

### Houdini Nodes / VEX / Settings
- `torus` SOP — X orientation, 0.5 × 0.15, 400 rows, 800 cols
- `attribvop` — `aanoise` added to P; roughness 0.6, octaves 4, freq 4, amplitude 0.025
- `flow` parameter promoted — keyframe: 0 at frame 1, **1 at frame 301** (linear)
- `polyextrude` SOP
- Redshift glass shader

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, vop, modelling, animation, rendering, redshift, intermediate

---

## Related Tutorials
- [[урок-стеклянный-пончик]] — Russian companion with full extraction
- [[vops-02---random-noise---houdini-beginner-tutorial]] — aanoise and flow noise fundamentals
- [[tutorial-glass-tiles]] — Redshift glass material context
