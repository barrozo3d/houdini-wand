---
title: Houdini 20 Procedural Shading Features
source: YouTube
url: https://www.youtube.com/watch?v=NHD3VbE2y00
author: cgside
ingested: 2026-07-13
houdini_version: "20"
tags: [solaris, materials, shaders, mtlx, karma, triplanar, uv, procedural, environment, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/houdini-20-procedural-shading-features/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini 20 Procedural Shading Features

**Source:** [YouTube](https://www.youtube.com/watch?v=NHD3VbE2y00)
**Author:** cgside
**Duration:** 3m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there, and welcome back. Let's see how we can use some of the new procedural shading nodes in Odin20.
[0:08] So I have some procedural generated houses, and it would be a challenge to texture them in a traditional way,
[0:15] like in Substance Painter, for example, and on top of that I didn't want to create UVs.
[0:22] But in Odin20 we have some new nodes that can help us in this task.
[0:28] I am starting by loading an attribute created in SOPS, randomizing each wood plank.
[0:34] Then we have these new material X color correct nodes, where we could plug the attribute to alter the gain,
[0:41] you or even saturation of our base texture.
[0:46] In here I am also changing the range, so the effect is more subtle.
[0:51] And as you can see we have some wood texture that is created by the new Karma X-style triplaner,
[0:59] and as I want to keep the orientation of the wood, I am removing any random rotation values,
[1:06] and just changing the size. Then I am referencing the first node to use as a roughness map,
[1:13] in this case changing the data type to raw.
[1:17] For the normal you just need to change the mode to normal, and there is no need for a normal map node,
[1:23] just plug it directly to the shader normal slot.
[1:27] I also have another attribute that gives a random value to reach house, and in case
[1:34] you want to generate a new value, you can use the new material X random node with the very
[1:40] NDC that you put. As you can see I have made some of this darker by changing the gain.
[1:46] There is also a new ramp node that you can use to change the colors of your textures, for instance,
[1:52] in this case I ended up not using it.
[1:57] So another feature that helped me in this scene were the new ROOM map nodes.
[2:03] Basically in SOPS you create the attributes necessary for shading, with the ROOM map
[2:09] frame nodes, just default settings. Then in Solaris you can use the Karma ROOM map along with
[2:15] the necessary attributes created in SOPS, ROOM P, TENGENED U, and TENGENED V, all set to Vector 3.
[2:25] And as you can see in Render we have the desired parallax effect, there are ways to randomize it,
[2:32] but since I had trouble finding cube maps I used the only one.
[2:37] So here's how it looks in context and for the amount of work we put into it it's not that bad.
[2:45] So that was it, a very quick overview of some new Karma features that I wanted to share with you.
[2:51] Don't forget you can grab a file from my Patreon and thank you, see you soon.



---

## Captured Frames

- [0:10] tutorials/frames/houdini-20-procedural-shading-features/frame_000.jpg
- [0:55] tutorials/frames/houdini-20-procedural-shading-features/frame_001.jpg
- [1:30] tutorials/frames/houdini-20-procedural-shading-features/frame_002.jpg
- [2:10] tutorials/frames/houdini-20-procedural-shading-features/frame_003.jpg
- [2:40] tutorials/frames/houdini-20-procedural-shading-features/frame_004.jpg

---

## Structured Notes

### Core Technique
Texturing procedurally-generated UV-less houses using Houdini 20's new MaterialX/Karma shading nodes — **Karma X-Style Triplanar** for projection without UVs, **MaterialX Color Correct** driven by per-plank/per-house SOP attributes for variation, and the new **Room Map** nodes for a fake-interior parallax effect through windows — entirely avoiding external texturing tools like Substance Painter.

### Summary
A batch of procedurally generated houses (no UVs, would be painful to texture in Substance Painter) is shaded using new Houdini 20 MaterialX/Karma nodes. A per-plank random attribute created in SOPs is loaded and fed into **MaterialX Color Correct** nodes to vary gain/hue/saturation of the base wood texture per plank, with the effect range narrowed for subtlety. The wood texture itself comes from the new **Karma X-Style Triplanar** node — random rotation is disabled (to preserve the wood grain's real orientation) while size is still varied; the same Triplanar node is referenced again for the roughness map (data type switched to Raw) and for the normal map (mode switched to Normal, plugged directly into the shader's normal input — no separate Normal Map node needed, unlike traditional image-texture normal setups). A second per-house random attribute feeds a **MaterialX Random** node (seeded via NDC) to darken some houses via gain — usable to procedurally generate a new random value in-shader if no attribute is available, and Houdini 20 also adds a new **Ramp** node for shader-driven color remapping (mentioned but not used in this build). For fake window-interior depth (parallax), a `room_map_frame` SOP node (default settings) is used to author the necessary per-window attributes in SOPs, then in Solaris the **Karma Room Map** node reads those SOP-authored attributes (Room P, Tangent U, Tangent V, all Vector3) to project a cube-map interior image with a parallax-like depth illusion through the window glass — noted as randomizable in principle, but a single cube map was used here due to difficulty sourcing more. The result: a full medieval-village-style render achieved with comparatively little manual texturing effort.

### Key Steps
1. **Per-plank variation attribute:** in SOPs, create a randomized attribute per wood plank (or per house) to drive shader variation without needing hand-painted textures.
2. **Color variation via MaterialX Color Correct:** load the SOP attribute into a **MaterialX Color Correct** node to alter gain/hue/saturation of the base wood albedo texture; narrow the effect's range for subtlety.
3. **UV-less texturing via Triplanar:** use the new **Karma X-Style Triplanar** node to project the wood texture without any UVs; disable random rotation (to preserve the wood grain's real-world orientation) while still varying scale/size per instance.
4. **Reuse the Triplanar for roughness:** reference the same Triplanar node again, feeding it as the **roughness** map, switching its data type to **Raw** (non-color-managed) for correct roughness values.
5. **Reuse the Triplanar for normal:** reference the Triplanar again, switch its mode to **Normal**, and plug it directly into the shader's normal input slot — Houdini 20's Triplanar handles the normal-map conversion internally, eliminating the need for a separate Normal Map node.
6. **Per-house random darkening:** feed a second per-house random SOP attribute into a **MaterialX Random** node (seeded via NDC, usable to generate a fresh random value directly in-shader when no existing attribute is available) to darken a subset of houses via gain, adding overall scene variation; note the new MaterialX **Ramp** node is also available for shader-driven color remapping (not used in this particular build).
7. **Author Room Map attributes in SOPs:** add a `room_map_frame` SOP node (default settings) per window to generate the necessary parallax attributes procedurally.
8. **Karma Room Map for fake interiors:** in Solaris, use the **Karma Room Map** node, feeding it the SOP-authored **Room P**, **Tangent U**, and **Tangent V** attributes (all set to Vector3 type) to project a cube-map interior image through each window with a parallax depth effect — a single cube map was reused across all windows due to difficulty sourcing more variety, though the technique supports randomization in principle.

### Houdini Nodes / VEX / Settings
Solaris/MaterialX nodes: MaterialX Color Correct (gain/hue/saturation, attribute-driven), Karma X-Style Triplanar (random rotation toggle, size/scale, data-type: Raw for roughness, mode: Normal for normal maps — used directly without a separate Normal Map node), MaterialX Random (NDC-seeded value generation), MaterialX Ramp (shader color remapping, mentioned not used), Karma Room Map (Room P / Tangent U / Tangent V Vector3 inputs) for parallax window interiors. SOPs: `room_map_frame` (default settings, authors Room Map attributes per window), per-plank/per-house random attribute generation (unspecified node, likely Attribute Randomize or similar).

### Difficulty
Intermediate — mostly UI-level shader-node assembly; no VEX required, but assumes familiarity with MaterialX/Karma shading concepts and Houdini 20's new node set.

### Houdini Version
20 (explicitly titled "Houdini 20 Procedural Shading Features" — Karma X-Style Triplanar, MaterialX Random/Ramp, and Room Map nodes are all new-to-20 features per the transcript).

### Tags
#solaris #materials #shaders #mtlx #karma #triplanar #uv #procedural #environment #intermediate

---

## Related Tutorials
Cross-link with custom-procedural-materials-with-houdini-and-karma.md and designer-like-materials-in-cops-houdini-205.md (same author, overlapping Triplanar/MaterialX shading vocabulary) once indexed together.
