---
title: Infinite Mirror in Karma XPU
source: YouTube
url: https://www.youtube.com/watch?v=5jfjCGDdbqs
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, materials, shaders, mtlx, karma, cops, compositing, procedural, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/infinite-mirror-in-karma-xpu/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Infinite Mirror in Karma XPU

**Source:** [YouTube](https://www.youtube.com/watch?v=5jfjCGDdbqs)
**Author:** cgside
**Duration:** 4m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I wanted to show you how I created
[0:04] this infinite mirror effect in Odini. As you can see we have a quite thin
[0:12] surface but inside we have this infinite look. Let's have a look first time
[0:20] creating the text and that's easy enough just with a font then extrude it, place
[0:28] it in the center then I'm grouping the front and back primitives and splitting
[0:36] them here and grouping again the solid parts and then the mirror part. Then just
[0:51] setting a small bevel and soften the models as you can see. Then for the
[1:00] material that's where the magic happens here in the mirror I'm creating a
[1:09] metallic mirror so met on a set to 1 and roughness to 0 and then a glass
[1:18] material transmission set to 1 and roughness to 0 and in world and then I'm
[1:26] mixing those two materials with a rain part set to ray back face. This is the way
[1:34] you can create two sided materials. So in front we will have the glass and on
[1:42] the back of the face we will have the mirror. So for the lead strip it's quite
[1:51] simple I'm just importing the text, keeping just one of the primitives,
[2:03] converting it to curves and then splitting them here by perimeter so I can work
[2:12] on both sides and then extruding the bitin so I can place the lead strip not
[2:22] necessarily adjacent to the text then grouping the the unshared edges, converting
[2:36] them to curves and then applying a color attributes to every 20 points,
[2:47] just attribute a just color and then sweeping it to a ribbon as you can see in
[2:57] here and just something than normal. Then for the rather geometry settings I am
[3:07] treating it as a light source giving it some diffuse intensity and some
[3:21] specular intensity to and just don't like to eliminate the outer material that I
[3:28] haven't showed you but it's just a solid material in this case two materials
[3:34] mixed again with the back face. One is more rough and the other one is less rough.
[3:45] So if you render everything we should get something like this.
[3:57] The infinite look.
[4:03] Then in Cops I am loading the render blurring it a bit and adding it on top so I can
[4:21] create this glow effect and just crop it and that's about it. You can grab the
[4:27] file from my Patreon and thank you everyone for the support and I'll see you
[4:33] next year. Thank you.



---

## Captured Frames

- [0:10] tutorials/frames/infinite-mirror-in-karma-xpu/frame_000.jpg
- [0:40] tutorials/frames/infinite-mirror-in-karma-xpu/frame_001.jpg
- [1:20] tutorials/frames/infinite-mirror-in-karma-xpu/frame_002.jpg
- [2:10] tutorials/frames/infinite-mirror-in-karma-xpu/frame_003.jpg
- [3:00] tutorials/frames/infinite-mirror-in-karma-xpu/frame_004.jpg
- [4:05] tutorials/frames/infinite-mirror-in-karma-xpu/frame_005.jpg

---

## Structured Notes

### Core Technique
Faking a classic "infinite mirror" LED sign effect using a genuinely thin real geometry: a **two-sided material trick** (mixing a mirror shader and a glass shader via the "Ray Back Face" mix input) so the front face renders as transparent glass while the back face renders as a mirror, combined with an LED-strip ribbon geometry treated as a **self-illuminating light source** (via Render Geometry Settings' diffuse/specular intensity) sandwiched between the two surfaces — producing the illusion of infinite depth entirely through shading and real-but-thin geometry, finished with a simple bloom pass in COPs.

### Summary
Text geometry is built from a **Font** node, Extruded, and centered; primitives are grouped by front/back and split, with the front further grouped into "solid" (frame/border) vs. "mirror" (the reflective glass-facing part) sub-groups; a small Bevel and Vertex Normals soften the model. The core trick is the **material**: a metallic mirror shader (Metallic = 1, Roughness = 0) and a glass shader (Transmission = 1, Roughness = 0, in an MtlX Standard Surface) are blended together using a **mix node whose factor is set to "Ray Back Face"** — this is a general technique for building any two-sided material in MaterialX/Karma: the front-facing side of a polygon renders one material (glass, so you see "into" the sign) and the back-facing side of the *same* polygon renders the other (mirror, so light bounces back) — with no actual mirror/glass double-walled geometry needed. For the LED strip: only one primitive of the imported text is kept, converted to **curves**, split at the perimeter (so both "sides" of each stroke can be worked on independently), and offset via Poly Extrude's "bias" parameter so the strip doesn't sit directly adjacent to the text stroke; the unshared edges of that offset shape are grouped and converted to curves, an **Attribute Adjust Color** assigns a color value every 20 points (creating a segmented multi-color pattern along the strip), and the colored curve is **Swept** into a ribbon with normals set to drive the sweep's orientation. This ribbon geometry is then treated purely as a **light source** at render time: in Render Geometry Settings, its diffuse and specular intensity are boosted so the geometry itself glows and illuminates the mirror/glass sandwich, rather than needing a separate light object. The outer frame/border geometry gets its own simple two-sided material (again mixed via Ray Back Face) — one side rougher, one side less rough — for a believable metal-frame look. Once rendered, the whole "infinite tunnel" illusion emerges purely from the glass-front/mirror-back sandwich reflecting the glowing LED ribbon repeatedly. Finishing touches happen in **COPs**: the render is loaded, **Blurred**, and added back on top of the sharp original for a cheap **glow/bloom** effect, then cropped to the final frame.

### Key Steps
1. **Text base geometry:** build text via **Font**, Extrude, and center in world space.
2. **Group front/back/solid/mirror regions:** group and split front vs. back primitives; further group the front primitives into "solid" (frame) and "mirror" (reflective face) sub-groups.
3. **Soften the model:** apply a small **Bevel** and compute vertex normals for a softer, more realistic edge profile.
4. **Two-sided mirror/glass material:** build a metallic mirror shader (Metallic = 1, Roughness = 0) and a glass shader (MtlX Standard Surface, Transmission = 1, Roughness = 0), then blend them with a mix node whose factor input is set to **"Ray Back Face"** — front-facing polygon sides render as glass, back-facing sides of the same geometry render as mirror, achieving a two-sided material without duplicate geometry.
5. **LED strip curve extraction:** import the text, keep only one primitive, convert to **curves**, split at the perimeter so both sides of each stroke are independently workable.
6. **Offset the strip from the text:** use Poly Extrude's **bias** parameter to place the strip geometry at a controlled offset rather than directly adjacent to the original text stroke.
7. **Segment-colored curve:** group the unshared edges of the offset shape, convert to curves, then use **Attribute Adjust Color** to assign a color value every 20 points — producing a segmented, multi-color pattern along the strip's length.
8. **Sweep into a ribbon:** **Sweep** the colored curve into a ribbon shape, using the curve's normal to drive cross-section orientation.
9. **Treat the ribbon as a light source:** in **Render Geometry Settings**, boost the ribbon geometry's diffuse and specular intensity so it self-illuminates and lights the mirror/glass sandwich directly, without needing a separate light object.
10. **Outer frame material:** build a second simple two-sided material (again mixed via Ray Back Face) for the outer solid/frame geometry — one side rougher, one side less rough — for a convincing metal-frame look.
11. **Render:** with the glass-front/mirror-back material sandwich and the glowing LED ribbon in between, the render produces the illusion of infinite depth/reflection.
12. **COPs bloom finishing:** load the render into a CopNet, **Blur** a copy, **Add** it back on top of the sharp original for a cheap glow/bloom effect, then Crop to the final output frame.

### Houdini Nodes / VEX / Settings
SOPs: Font, Extrude, Group (front/back, solid/mirror sub-groups), Bevel, Vertex Normals, Convert Line (curves), Poly Extrude (bias offset), Group (unshared edges), Attribute Adjust Color (every-20-points segment coloring), Sweep (normal-driven ribbon orientation). Materials (MaterialX/Karma): Standard Surface (Metallic=1/Roughness=0 for mirror; Transmission=1/Roughness=0 for glass), Mix node (factor = Ray Back Face, for two-sided materials — used twice, once for the mirror/glass sandwich and once for the outer frame's dual-roughness look). Render: Render Geometry Settings (diffuse intensity, specular intensity — treating emissive geometry as a light source). COPs: Blur, Add (bloom/glow compositing), Crop.

### Difficulty
Intermediate — the core Ray-Back-Face two-sided material trick is simple to apply once understood; the rest is straightforward modeling/sweep/compositing work.

### Houdini Version
20.5 (Karma XPU/MaterialX workflow consistent with Houdini 20.5-era tools).

### Tags
#modeling #materials #shaders #mtlx #karma #cops #compositing #procedural #product-viz #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers the Ray-Back-Face two-sided material trick — cross-link with any future MaterialX/Karma shading tutorials that use double-sided materials once extracted from this batch.
