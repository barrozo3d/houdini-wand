---
title: Experimental Motion - CHOPS
source: YouTube
url: https://www.youtube.com/watch?v=0XnjEVcaq6A
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["chops", "motion", "animation", "procedural-animation", "organic", "rendering", "art-direction"]
extraction_status: complete
frames_dir: tutorials/frames/experimental-motion---chops/
frame_count: 4
---

# Experimental Motion - CHOPS

**Source:** [YouTube](https://www.youtube.com/watch?v=0XnjEVcaq6A)
**Author:** Houdini.School
**Duration:** 84m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en okay we so my name is Yan Paul dman I'm a Dutch digital artist and I'm mostly focus on natural shapes and everything being very relaxed and very smooth and chops helps a lot with that but the it's because I'm looking for a certain feeling when I'm working and I found out when I was looking back at my portfolio that feeling is this feeling it's very calm and I want it to usually be in the background I really like to work on large exhibitions where there's these flowers that are coloring the room and you might look at them directly once or twice but the most important thing is that it fills the room with a certain Vibe and this vibe that I'm going for is very calm so professionally I also work with different agencies so this is these are different art pieces that are made for an agency in the Netherlands and it I still think it has this kind of calm focused vibe to it and so I really like rendering we won't be touching on that too much today but please reach out if you want if you have questions about this but I mostly today I'm going to talk about these very smooth movements so um oh sorry on my Instagram you will be able to see a lot of my experimentatio...

**Frame:** tutorials\frames\experimental-motion---chops\frame_000.jpg


---

## Structured Notes

### Core Technique
Using CHOPs (Channel Operators) in Houdini to create smooth, organic, art-directed motion for natural and ambient visual work — particularly for exhibition and installation contexts.

### Summary
Yan Paul Dubbelman, a Dutch digital artist known for calm, nature-inspired motion work, presents an 84-minute live session on using CHOPs to generate smooth, experimental motion. His focus is on achieving a specific artistic feeling — very calm and organic — rather than technically driven effects. The session demonstrates how CHOPs can process and shape motion data to create the kind of fluid, living movement present in his portfolio of flowers, plants, and large-scale exhibition pieces. Rendering techniques are touched on briefly alongside the CHOP-driven motion workflows.

### Key Steps
1. Understand the philosophy behind CHOPs as a motion processing network (not just animation curves)
2. Set up a basic CHOP network to drive point positions or transform attributes
3. Use noise and filter CHOPs to generate smooth, organic motion channels
4. Apply the channel data back to geometry using CHOP to SOP feedback
5. Layer multiple CHOP signals for complex but calm compound motion
6. Art-direct the motion feel by adjusting timing, amplitude, and phase in CHOPs
7. Set up rendering with appropriate lighting for the motion-driven final output

### Houdini Nodes / VEX / Settings
- CHOP network context
- Noise CHOP
- Filter CHOP (lag, spring)
- Math CHOP
- Channel CHOP
- CHOP to SOP (export/binding)
- Geometry CHOP
- Rendering context (lighting setup)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
chops, motion, animation, procedural-animation, organic, rendering, art-direction

---

## Related Tutorials
- [Experimental Motion - The SOP Solver](experimental-motion---the-sop-solver.md) — companion session by same author using the SOP Solver for organic life-like motion
- [Procedural Growth with KineFX and the Labs Tree Tools](procedural-growth-with-kinefx-and-the-labs-tree-tools.md) — procedural growth and wind animation using VEX and CHOPs together
- [Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants](yan-paul-dubbelman-procedural-nature-procedural-living-plants.md) — same artist's natural shape procedural work, directly related aesthetic approach
