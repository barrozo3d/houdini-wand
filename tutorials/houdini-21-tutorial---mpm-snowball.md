---
title: Houdini 21 Tutorial - MPM Snowball
source: YouTube
url: https://www.youtube.com/watch?v=aQQeEOlHqjQ
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Houdini 21"
tags: ["dop", "sop", "mpm", "grains", "simulation", "vfx", "rendering", "karma", "intermediate", "h21"]
extraction_status: complete
frames_dir: tutorials/frames/houdini-21-tutorial---mpm-snowball/
frame_count: 0
---

# Houdini 21 Tutorial - MPM Snowball

**Source:** [YouTube](https://www.youtube.com/watch?v=aQQeEOlHqjQ)
**Author:** Voxyde VFX
**Duration:** 49m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello guys, it's Mikael from Boxet here and into this video I will show you how to create this Snowball simulation inside of what you need using MPM solver. Throughout this video you will learn how to create realistic snow simulation using MPM solver. You will also learn a few tricks on how to bake your simulation properly to save disk space and also you will learn how to create secondary simulations to add extra detail to your simulation. Apart from that, we will be also covering how to render and composite this shot. And if you guys like this tutorial, let us know in the comments so we can bring more about MPM in the future. For more tiny courses and tutorials visit boxside.com. Okay, so let's just start by creating our snowball. For that we'll need a sphere and this is really big so let's change this to 0.08. So it's 8 centimeters and let's increase our rows and the columns. So we have more geometry to work with. Now let's add a mountain so we can have more detail on our sphere. This shape is not really nice so let's play around a bit with the values. Maybe in amplitude of 0.2, let's put 0.2. Maybe we want smaller element size. Maybe let's do two mountains so I will add a bigger...



---

## Structured Notes

### Core Technique
Houdini 21 MPM (Material Point Method) solver for snow simulation: building a snowball with layered `mountain` noise, configuring the MPM solver with snow material presets, baking the simulation to disk for efficient iteration, adding secondary particle simulations for snow spray, and rendering + compositing the final shot with Karma XPU.

### Summary
A 50-minute Houdini 21 tutorial focused on the MPM solver — introduced in H21 as the new standard for granular materials (snow, sand, mud). Covers building the snowball source geometry (sphere with layered mountain SOPs for surface detail), setting up the DOP network with the `mpm solver` and snow-specific material properties (stiffness, cohesion, friction), baking simulation output to disk as `.bgeo.sc` for non-destructive playback, creating secondary particle simulations (snow spray/scatter kicked up on impact) driven by the primary MPM velocity field, and a complete Karma XPU rendering and compositing pass with AOVs.

### Key Steps
1. Create snowball source: `sphere` SOP — Radius: 0.08 (8cm); increase rows/columns for polygon density; add `mountain` SOP — Amplitude: 0.2, Element Size: small, for fine surface noise; stack a second `mountain` SOP at larger element size for macro shape variation
2. Convert to MPM-ready geometry: add `scatter` SOP to fill the snowball volume with points, OR use `vdbfrompolygons` → `convertVDB` to fill; points become MPM particles
3. Set up DOP network: create `dopnet` → inside, add `mpmsolver` DOP; set Object Type to Snow; key snow parameters: Stiffness (hardness of snow), Cohesion (how much it clumps), Friction (surface interaction), Density
4. Add collision geometry: create `mpmobject` or `staticobject` DOP for the ground plane; import ground geometry via `soppath`; set Collision Type to Static
5. Bake simulation to disk: after DOPs, add `filecache` SOP; set output path and file format to `.bgeo.sc`; cook and save frames; set filecache to Read mode for fast playback without recalculation; saves significant disk vs uncompressed
6. Add secondary simulation for snow spray: at impact frame, use `attribwrangle` to extract high-velocity particles from the MPM output (`if (length(@v) > threshold)`); feed into a `popnet` as source; apply `curlnoise` and gravity for organic spray motion; merge with primary output
7. Render in Karma XPU: import MPM point cloud into Solaris via `sopimport`; add `karmarendersettings` with XPU engine; set Particle Radius for snow point rendering; use MaterialX snow material (subsurface + white diffuse); add AOVs for compositing

### Houdini Nodes / VEX / Settings
- `sphere` SOP — Radius: 0.08; Rows/Columns: increase for density
- `mountain` SOP — Amplitude: 0.2; Element Size: small (fine detail) + large (macro variation); stack two for multi-frequency surface
- `scatter` SOP — used to fill snowball volume with MPM particles; Total Count: high density for realistic snow mass
- `vdbfrompolygons` SOP — alternate volume-fill method; `convertVDB` to points for MPM source
- `dopnet` DOP — container for MPM simulation
- `mpmsolver` DOP — H21 Material Point Method solver; Object Type: Snow; Stiffness; Cohesion; Friction; Density; Substeps: increase for accuracy
- `staticobject` DOP — collision body (ground, wall); SOP Path: ground geometry
- `groundplane` DOP — flat infinite collision ground; alternative to staticobject for simple setups
- `filecache` SOP — Output: `.bgeo.sc` path; Mode: Write (cook), Read (playback); compresses simulation data efficiently
- `attribwrangle` SOP — `if (length(@v) > 2.0) { @group_spray = 1; }` — extracts high-velocity impact particles as secondary source
- `popnet` / `popsource` — secondary snow spray simulation; source from spray group
- `popcurl` DOP / `curlnoise` VOP — organic swirling motion for spray particles
- `sopimport` LOP — brings MPM point cloud into Solaris for Karma rendering
- `karmarendersettings` LOP — Render Engine: XPU; Particle Radius parameter for point cloud rendering
- Karma MaterialX snow shader — Base Color: white; Roughness: high; Subsurface: low for packed snow look

### Difficulty
Intermediate

### Houdini Version
Houdini 21

### Tags
#dop #sop #mpm #grains #simulation #vfx #rendering #karma #intermediate #h21

---

## Related Tutorials
- [Intro To Houdini for VFX - Beginner Course](./intro-to-houdini-for-vfx---beginner-course.md) — #sop #dop #vop #vex #attributes #beginner
- [Intro To Houdini Solaris - Full Beginner Course](./intro-to-houdini-solaris---full-beginner-course.md) — #lop #solaris #usd #rendering #karma #beginner
- [Houdini Tutorial - Simple Disintegration FX](./houdini-tutorial---simple-disintegration-fx.md) — #sop #dop #particles #vfx #intermediate
