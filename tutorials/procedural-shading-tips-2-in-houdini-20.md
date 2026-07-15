---
title: Procedural Shading Tips #2 in Houdini 20
source: YouTube
url: https://www.youtube.com/watch?v=r2SSCwpgnVQ
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.306"
tags: [karma, materialx, solaris, room-maps, udim, cops, vellum, favela, procedural-shading, texturing]
extraction_status: complete
frames_dir: tutorials/frames/procedural-shading-tips-2-in-houdini-20/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Shading Tips #2 in Houdini 20

**Source:** [YouTube](https://www.youtube.com/watch?v=r2SSCwpgnVQ)
**Author:** cgside
**Duration:** 4m15s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello and welcome back. So in this video I'm sharing a few tips on procedural shading in Odin
[0:05] 20. All the techniques shown here can be found as sample files on my Patreon. The first one is


### Assigning random textures [0:11]
**Transcript (timestamped):**
[0:12] on out to assign random textures to the different apartments in the Islam-like building. As you can see
[0:19] I already have a unique attribute for each apartment, but I just want to use three different textures
[0:25] so I need to divide it randomly as seen in this render. The first step is to promote the
[0:30] attribute to detail, set to maximum, this way I have the amount of iterations I need.
[0:37] Then in the wrangle I am running over numbers and the count will be the detail attribute we just
[0:43] created. Then I am saving the primitive numbers with the respective attribute using the find attribute
[0:50] value function. And for each one assigning a random value between 0 and 2 in this case,
[0:56] so three variations to what cast a attribute named Outstexture. And you can easily change the
[1:03] amount of variations and the seed. Now in Solaris I have three different textures to be assigned


### Assigning different textures [1:07]
**Transcript (timestamped):**
[1:10] to the walls. And using a material like switch node I can feed the attribute to the
[1:16] which input to assign the different textures based on the attribute.


### Assigning different room textures [1:22]
**Transcript (timestamped):**
[1:22] So now we can use a similar logic to assign a different room texture to which window interior
[1:28] geometry. As you can see I am assigning a room map frame, just default settings,
[1:33] and in this wrangle running over each frame assigning a random integer value between 0 and 2.
[1:39] In this case I only have three textures to use as an interior. In Solaris you can see that I


### Loading different room textures [1:44]
**Transcript (timestamped):**
[1:46] have each texture divided into three different groups following the attribute we just created.
[1:52] Loading room p tangent u and v as in the last video, but this time using the room offset inputs
[2:00] with our attribute to pick different textures. And the way you do that is by loading different
[2:06] u-dim tiles, in this case I only add three. Now this tip is not necessarily on procedural shading,


### Importing subset groups [2:09]
**Transcript (timestamped):**
[2:13] but still I find it useful to organize our setup. As you can see I have different groups in
[2:20] these assets and need to target those groups to assign different materials. In Solaris we do have
[2:27] the different groups under the name attributes, but it's not loaded by default.
[2:33] So what you need to do is under import data, make sure you're importing the different subset
[2:38] groups, this way you can easily target them in our material assignment.


### Creating a leak map [2:45]
**Transcript (timestamped):**
[2:46] Okay this last one is on the experimental side, but still wanted to share it on how to create a
[2:53] lit map to use in shading. First I'm copying over a few deform spheres that will be the base of our
[3:01] volume fluid, randomizing a bit the viscosity attribute, and then you can create a volume
[3:08] solver to run the sim. Assign a color to the fluid particles and in a solver we can create a wetmap
[3:19] using an attribute transfer. Then we can pick a frame and cache it as we won't need the animation.
[3:26] Instead of subdividing our source geometry we can just render this to a texture using the
[3:32] attribute importing cops. As you can see we have this lick texture over the base.


### Mixing textures [3:43]
**Transcript (timestamped):**
[3:43] And in Solaris the easiest way to mix the texture in is by gaining down the base texture and mixing
[3:50] it with the original using the lick's mask as an input. I'm also adding a bit of noise but that's
[3:58] about it. So yeah hopefully you picked up a few tips and don't forget you can join my Patreon


### Outro [4:00]
**Transcript (timestamped):**
[4:04] and get sample files along with exclusive tutorials. Thank you and see you next time.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_000.jpg
- [1:00] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_001.jpg
- [1:40] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_002.jpg
- [2:25] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_003.jpg
- [3:10] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_004.jpg
- [3:30] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_005.jpg
- [4:05] tutorials/frames/procedural-shading-tips-2-in-houdini-20/frame_006.jpg

---

## Structured Notes

### Core Technique
Five procedural-shading tips applied to a stacked favela-style apartment building: random-per-piece texture/material assignment via a detail-max wrangle loop and `findattribval()`, room-interior texture variation via UDIM offsets keyed to a random attribute, importing LOP subset groups for material targeting, and an experimental volume-based dirt/wetness "lick map" baked to a texture via COPs.

### Summary
To avoid every apartment unit rendering with the same texture, a wrangle promotes a unique-ID attribute to detail-max (getting the total count of variations needed), then loops over that count assigning each matching primitive a random integer (0–2 for 3 texture variations) via `findattribval()`, stored as an `outs_texture`-style attribute; a MaterialX Switch node in Solaris reads this attribute to pick between the 3 different wall textures per unit. The same random-assignment pattern is reused for **room interior textures**: each window's interior geometry gets a random 0–2 value, and since only 3 interior textures exist, the geometry uses **Room Map** texture-projection frames with the offset input driven by that random attribute — practically, this means loading different **UDIM tiles** per room based on the attribute rather than swapping texture files. Solaris often hides sub-geometry groups by default, so under **Import Data** the LOPs "subset groups" option must be enabled to expose an asset's internal named groups for material targeting. The final, more experimental tip: build a believable "lick"/wetness/dirt map by scattering deformed spheres as a fluid volume source (with randomized viscosity), running a volume solver, assigning fluid-particle color, and using an **Attribute Transfer** inside the solver to paint a wetmap onto the surface; a single settled frame is cached (no animation needed), then instead of subdividing the base geometry for detail, the wetmap is **rendered directly to a texture via COPs attribute-import**, producing a usable "lick texture" that's mixed into the base texture in Solaris by gaining down the original and blending in the lick mask, with extra noise layered on top.

### Key Steps
1. **Random texture assignment**: promote a unique per-piece ID attribute to a **detail max** value (the count of distinct pieces/variations); loop over that count in a wrangle using `findattribval()` to find each primitive matching a given ID, and assign it a random value between 0 and 2 (for 3 texture variations) stored as an `outs_texture` attribute.
2. In Solaris, use a **MaterialX Switch** node fed by that attribute to route each apartment unit to one of 3 different wall textures.
3. **Random room interior textures**: apply the same detail-max + `findattribval()` random-assignment pattern to each window's interior geometry, this time producing values 0–2 for 3 available interior textures.
4. Load the interior textures using **Room Map** projection frames (as covered in a prior video), but this time feed the **room offset inputs** with the random attribute — practically achieved by loading different **UDIM tiles** per room rather than swapping separate texture files (only 3 UDIMs needed here).
5. **Exposing internal subset groups**: note that Solaris doesn't load an asset's named/internal groups by default; under **Import Data**, enable the **subset groups** option so those groups become available for targeted material assignment.
6. **Experimental lick/wetness map**: copy several deformed spheres to act as the base of a **volume fluid** simulation source, randomizing each one's viscosity attribute.
7. Assign a color to the fluid particles; inside the fluid **solver**, use an **Attribute Transfer** to paint a wetmap onto the source/collision geometry as the sim runs.
8. Pick a single representative frame and **cache** it (no animation needed for this static wet-look effect).
9. Instead of subdividing the source geometry to add render-time detail, **render the wetmap directly to a texture via COPs** using an attribute-import node — producing a standalone "lick texture" usable like any other map.
10. In Solaris, mix the lick texture in by **gaining down** the base texture and blending in the lick mask as an input, with a bit of extra noise layered on top for texture believability.

### Houdini Nodes / VEX / Settings
Attribute Promote (detail max), Attribute Wrangle (`findattribval()`-driven random assignment loop), MaterialX Switch (texture/UDIM routing by attribute), Room Map projection frames (UDIM-offset-driven room textures), LOPs Import Data (subset groups exposure), Scatter/Copy (deformed sphere fluid source), Attribute Randomize (per-particle viscosity), Volume Fluid Solver, Attribute Transfer (wetmap painting inside solver), Cache (single frame), COPs (attribute-import texture bake of the wetmap), gain-based texture mixing with noise layering.

### Difficulty
Intermediate–Advanced (the random per-piece texture assignment is broadly applicable and simple; the volume-fluid lick-map bake is explicitly framed by the author as experimental/advanced).

### Houdini Version
20.5.306 (visible in viewport title bar).

### Tags
karma, materialx, solaris, room-maps, udim, cops, vellum, favela, procedural-shading, texturing

---

## Related Tutorials
- [Procedural Favela in Houdini Tips and Tricks](procedural-favela-in-houdini-tips-and-tricks.md) — very likely the modeling/building-generation companion to this shading-tips video, sharing the same favela apartment-block project.
- [Handy Houdini Tips - Vellum, UVs, Modeling and More](handy-houdini-tips-vellum-uvs-modeling-and-more.md) — shares the Room Map / UV-sample texture-projection technique reused here for room interiors.
