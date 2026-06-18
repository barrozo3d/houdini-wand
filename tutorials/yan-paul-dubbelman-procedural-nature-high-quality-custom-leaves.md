---
title: Yan Paul Dubbelman | Procedural Nature | High-Quality Custom Leaves
source: YouTube
url: https://www.youtube.com/watch?v=d3pMfIsvAyQ
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["procedural", "nature", "leaves", "copernicus", "textures", "instancing", "unreal-engine", "modeling", "organic", "vegetation"]
extraction_status: complete
frames_dir: tutorials/frames/yan-paul-dubbelman-procedural-nature-high-quality-custom-leaves/
frame_count: 25
---

# Yan Paul Dubbelman | Procedural Nature | High-Quality Custom Leaves

**Source:** [YouTube](https://www.youtube.com/watch?v=d3pMfIsvAyQ)
**Author:** Houdini.School
**Duration:** 100m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hello everyone. Thank you for being here. And if you are not part of the live session, but you're just part of the if you're just watching this later, then also very welcome. And what we're going to be talking about today are 3D models and textures. And especially patterns and structures that you might find in nature. And what I found is that when I'm generating my models, I always have to balance the quality of the model and the the sort of the weight of the model. And that means the the resolution of the poly counts, but also of the textures and the materials. And ideally, you would render everything as high quality as possible without having any compromises. And so over the years, I've developed different tools to get there. And some of them I think will be familiar but I'm using some tricks to make everything as efficient as possible. And so first we we will be building these tools that generate the models. And after that we will use the new copernicus system to generate textures. And you can use those textures on very low resolution geometry. You can use them in interactive situations like Unreal Engine or you can just render them. I used instances ...

**Frame:** tutorials\frames\yan-paul-dubbelman-procedural-nature-high-quality-custom-leaves\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedurally generating high-quality leaf models with optimized poly counts and using Houdini's Copernicus system to generate textures for those leaves — balancing visual quality against geometry weight for use in instancing, Unreal Engine, and rendering.

### Summary
Yan Paul Dubbelman presents a 100-minute session on building high-quality leaf models procedurally in Houdini, with a focus on quality/weight balance for production. The session has two main parts: building the procedural leaf model generators (optimized geometry), then using Houdini's new Copernicus system to generate textures that can be applied to even low-resolution geometry. The resulting assets are suitable for instancing at scale, use in Unreal Engine for interactive scenes, or traditional offline rendering. Dubbelman's characteristic approach emphasizes making tools that are efficient, beautiful, and easy to iterate on.

### Key Steps
1. Analyze the structural patterns of real leaves — venation, margin shape, surface variation
2. Build a procedural leaf shape generator in SOPs using curves and surfaces
3. Add procedural variation parameters for leaf shape (size, curvature, tip shape)
4. Optimize geometry for efficient instancing — low poly count, clean topology
5. Set up Houdini's Copernicus system (node-based texture compositing)
6. Generate leaf texture maps in Copernicus — color, roughness, opacity, normal
7. Apply generated textures to both high and low-resolution geometry variants
8. Instance leaves across a scene and test in rendering context
9. Export assets for Unreal Engine use if needed

### Houdini Nodes / VEX / Settings
- Curve SOP (leaf profile)
- Skin / Loft SOP (leaf surface)
- PolyBevel SOP
- Attribute Wrangle (leaf shape variation)
- Copernicus (node-based texture compositing system)
- Instance SOP / Copy to Points SOP
- Houdini Engine (Unreal export)
- Material network (texture application)
- VEX: fit(), smooth(), noise() for variation

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
procedural, nature, leaves, copernicus, textures, instancing, unreal-engine, modeling, organic, vegetation

---

## Related Tutorials
- [Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants](yan-paul-dubbelman-procedural-nature-procedural-living-plants.md) — companion session by same author on building complete procedural plants
- [Experimental Motion - CHOPS](experimental-motion---chops.md) — also by Yan Paul Dubbelman; CHOPs for organic motion applied to the plants built in these sessions
- [Procedural Growth with KineFX and the Labs Tree Tools](procedural-growth-with-kinefx-and-the-labs-tree-tools.md) — related procedural vegetation creation with rigging and animation
