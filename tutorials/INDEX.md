# Houdini Wand — Tutorial & Knowledge Base Index

This is the skill's growing knowledge base. Every ingested tutorial, article, and book excerpt is listed here.

**To add a tutorial:** say "ingest this: [URL]" and the skill will fetch, structure, and add it here automatically.
**To add a book chapter:** paste the content and say "ingest this chapter from [Book Title]".
**To search:** look for tags matching the technique you need.

---

## How to Read This Index

```

### Intro To Houdini for VFX - Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JbxNElzALrM
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19-H21 UI)
- **Tags:** "sop", "dop", "vop", "vex", "attributes", "particles", "simulation", "wrangler", "procedural", "beginner"
- **Summary:** A 2-hour beginner course covering everything needed to start creating VFX in Houdini from zero. Progresses from UI navigation and basic SOP geometry through the attributes system, Attribute VOPs, VEX wrangles, and DOP simulation networks. Ends with an overview of all major solver types (Pyro, FLIP, Vellum, RBD) and noise-driven per-frame deformation inside a SOP Solver.
- **File:** tutorials/intro-to-houdini-for-vfx---beginner-course.md


### Intro To Houdini Particles - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=94YAomHfMbw
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "dop", "sop", "vop", "particles", "simulation", "attributes", "wrangler", "procedural", "intermediate"
- **Summary:** A 2-hour course on Houdini particle simulations from Voxyde VFX, pitched at beginners but covering production-level techniques. Covers the full DOP particle pipeline: popnet/popsource/popsolver setup, custom velocity via Geometry VOP (rather than pre-built POP forces), multiple sourcing types, attribute inheritance, interpolate source for animated geometry, and static/moving collisions....
- **File:** tutorials/intro-to-houdini-particles---full-beginner-course.md


### Intro To Houdini Volumes - Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wR0SDptfygg
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "sop", "vop", "volumes", "simulation", "procedural", "vdb", "intermediate"
- **Summary:** A 2-hour course covering all core Houdini volume concepts from Voxyde VFX. Explains standard volumes vs VDBs, fog density volumes vs SDF distance fields, and how to manipulate them with Volume VOP (the per-voxel equivalent of Attribute VOP). Covers multiple volume fields per object, scalar vs vector fields for velocity, curve-based velocity volumes, and two methods for converting particle...
- **File:** tutorials/intro-to-houdini-volumes---beginner-course.md


### Intro To Houdini Pyro - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=m8w2OND3rH0
- **Author:** Voxyde VFX
- **Houdini Version:** H20–H21 (Pyro Burst Source available)
- **Tags:** "pyro", "fire", "smoke", "simulation", "dop", "vdb", "sourcing", "micro-solvers", "collision", "explosion", "beginner"
- **Summary:** A 145-minute comprehensive beginner Pyro course by Voxyde VFX. Starts with a single fog-volume density source and systematically adds each field: velocity (noise-driven and wind), temperature (drives buoyancy and combustion), divergence (expansion/explosion scale), and flame. Explains the critical naming relationship between VDB names and Pyro solver target fields. Covers all Shape tab...
- **File:** tutorials/intro-to-houdini-pyro---full-beginner-course.md


### Intro to VOPS - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Kx3CJJei_Vs
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "vop", "sop", "attributes", "math", "noise", "procedural", "beginner"
- **Summary:** A 59-minute beginner tutorial covering the core VOP math nodes used daily in Houdini VFX work. Starts with the `attribvop` and its variants (point/primitive/vertex/volume VOP), then walks through add/subtract/multiply, parameter promotion to expose controls at the geometry level, displacement along normals using the `displacealongn` VOP, the `fit` (fit range) node for remapping values, the...
- **File:** tutorials/intro-to-vops---houdini-beginner-tutorial.md


### VOPS 02 - Random & Noise - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mORz1y05T7E
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "vop", "sop", "noise", "random", "attributes", "procedural", "beginner"
- **Summary:** A 46-minute beginner tutorial dedicated to noise and randomness in Houdini VOPs. Covers the `random` VOP using point number as seed for per-point color or value variation, then progresses through five noise types: turbulent noise (classic workhorse, 1D–3D signatures), anti-aliased flow noise (directional-free animation via a flow input), curl noise (divergence-free fluid-like motion with 4D...
- **File:** tutorials/vops-02---random-noise---houdini-beginner-tutorial.md


### VOPS 03 - Vector Operations - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oT6qzs-Vffk
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "vop", "sop", "vectors", "math", "attributes", "procedural", "beginner"
- **Summary:** A 31-minute focused tutorial on vector math as used in VFX simulations. Covers creating direction vectors by subtracting positions, normalizing them to unit length, computing lengths/distances, and visualizing vectors via the N (normal) attribute with point normal display. Explains the cross product (result perpendicular to two input vectors) and dot product (returns -1 to 1 based on angle...
- **File:** tutorials/vops-03---vector-operations---houdini-beginner-tutorial.md


### VOPS 04 - Geometry Interactions - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qDtKmbCDn3k
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "vop", "sop", "attributes", "geometry", "procedural", "intermediate", "beginner"
- **Summary:** A 44-minute tutorial on one of the most critical VFX skills: making two geometries communicate and transfer attributes inside a VOP network. Covers `importpointattrib` for reading a specific point's attribute from a second geometry, `nearpoint` for finding the closest point index, `findattribval` for searching by attribute value, `minpos` for snapping points to the nearest surface position on...
- **File:** tutorials/vops-04---geometry-interactions---houdini-beginner-tutorial.md


### Intro To Houdini Solaris - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3BX97YIQERE
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** "lop", "solaris", "usd", "rendering", "karma", "lighting", "materialx", "instancing", "beginner"
- **Summary:** A 4.5-hour comprehensive Solaris beginner course covering the complete LOP (Lighting Operator) workflow from USD scene graph fundamentals to final Karma XPU render. Part 1 covers all key ingredients in isolation: USD scene graph concepts, importing SOP geometry via `sopimport`, stage assembly and the Stage Manager, MaterialX-based Karma material authoring inside a `materiallibrary`, the...
- **File:** tutorials/intro-to-houdini-solaris---full-beginner-course.md


### Houdini Tutorial - Simple Disintegration FX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O2F1Qzl22oU
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "sop", "dop", "vop", "particles", "attributes", "vfx", "destruction", "intermediate"
- **Summary:** A 21-minute tutorial showing how to build a clean disintegration effect entirely in SOPs. Starts by remeshing a test geometry to uniform triangle density using the `remesh` SOP, then scatters points across the surface. A noise-driven threshold attribute (using `attribvop` or `attribwrangle`) is animated over time to define a deletion mask — geometry below the threshold is deleted with a...
- **File:** tutorials/houdini-tutorial---simple-disintegration-fx.md


### Houdini 21 Tutorial - MPM Snowball
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aQQeEOlHqjQ
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini 21
- **Tags:** "dop", "sop", "mpm", "grains", "simulation", "vfx", "rendering", "karma", "intermediate", "h21"
- **Summary:** A 50-minute Houdini 21 tutorial focused on the MPM solver — introduced in H21 as the new standard for granular materials (snow, sand, mud). Covers building the snowball source geometry (sphere with layered mountain SOPs for surface detail), setting up the DOP network with the `mpm solver` and snow-specific material properties (stiffness, cohesion, friction), baking simulation output to disk as...
- **File:** tutorials/houdini-21-tutorial---mpm-snowball.md


### Houdini Solaris Tutorial - Rendering Multiple ROPS Together
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qg3OFz4JZs4
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** "lop", "solaris", "rendering", "karma", "top", "pipeline", "beginner"
- **Summary:** A quick 1.5-minute tip tutorial demonstrating how to render multiple Karma/Solaris ROP outputs (e.g. character, blast, particles, rain, water) in a single automated batch using a TOP network. The workflow creates a `topnet`, adds one `ropfetch` TOP node per ROP output (named to match the LOP render node names), sets the ROP fetch node's path to the corresponding LOP stage, switches the cook...
- **File:** tutorials/houdini-solaris-tutorial---rendering-multiple-rops-together.md


### Improve Solaris Performance - Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QfWUzrfsDaY
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** "lop", "solaris", "usd", "rendering", "karma", "performance", "pipeline", "intermediate"
- **Summary:** A 23-minute practical tutorial covering strategies to keep the Houdini Solaris viewport fast when dealing with complex scenes containing characters, animated geometry, RBD simulations, Vellum cloth, and particles. The core principle is to never import heavy live-cooking SOP networks directly into Solaris — instead, bake simulations and animations to disk as caches (`.bgeo.sc`, `.usd`, or...
- **File:** tutorials/improve-solaris-performance---houdini-tutorial.md


### Houdini Tutorial - Wispy Smoke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RRmvyQu39-4
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** "dop", "sop", "pyro", "smoke", "volumes", "vdb", "simulation", "vfx", "intermediate"
- **Summary:** A 27-minute tutorial focused on achieving a wispy, thin cigarette-smoke aesthetic using Houdini's Pyro solver. The approach starts from the `configure pyro` shelf tool preset (used as a quick base), replaces the default torus source with a small sphere emitter, and then shapes the simulation by reducing density emission, increasing dissipation rate, adding high-frequency turbulence for wispy...
- **File:** tutorials/houdini-tutorial---wispy-smoke.md


### Introduction to Particles in Houdini 21 [FULL Beginner Course 2026]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=041qemBc_1Q
- **Author:** Pixel In The Frame
- **Houdini Version:** 21
- **Tags:** particles, dop, sop, vex, instancing, simulation, rendering, karma, lop, solaris, beginner, houdini-21
- **Summary:** A 165-minute beginner-to-intermediate walkthrough covering virtually every node in the POP (Particle Operator) toolset in H21. The viewer builds up a DOP network from scratch, learning POP Source emission types (scatter on surface, all points, location), all force nodes (Force, Wind, Drag, Axis Force, Curve Force, Attract, Interact, Advect by Volume), collision handling (POP Collision Detect +...
- **File:** tutorials/introduction-to-particles-in-houdini-21-full-beginner-course-2026.md


### Houdini UV Unwrapping Fundamentals
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cguHzZ9L87g
- **Author:** Mat Sola
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** sop, modelling, uv, procedural, intermediate
- **Summary:** A 65-minute comprehensive UV fundamentals course by Mat Sola covering a complete reusable workflow: geometry cleanup as a prerequisite, UV projection methods, seam cutting via edge groups, `uvpeel`/`uvunwrap` for flattening, `uvlayout` for packing, `uvquickshade` for visualization in the viewport UV editor, and export-ready UV output. Demonstrated on both hard-surface and soft/organic models...
- **File:** tutorials/houdini-uv-unwrapping-fundamentals.md


### Model a Procedural Flower | Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pIp3cYSBZc4
- **Author:** Fifo
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** sop, dop, vop, vellum, modelling, procedural, curves, attributes, simulation, intermediate
- **Summary:** A 38-minute SOP tutorial building a fully procedural and animated flower. Covers: curve-based stem with `resample` and `sweep`, blossom modeling with `blendshape` for open/closed states, implementing the golden angle in a VOP `crossproduct` for phyllotaxis spiral alignment, `copytopoints` with time-offset `pscale` ramp for staged blooming, and a Vellum cloth solver with pin constraints to...
- **File:** tutorials/model-a-procedural-flower-houdini-tutorial.md


### Houdini Tutorial | Creating Realistic Waterfall Simulation (Step-by-Step)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eYqxarTsOrE
- **Author:** VFX Grace
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** flip, dop, sop, simulation, volumes, vdb, rendering, intermediate, advanced
- **Summary:** A 151-minute comprehensive waterfall tutorial covering the complete FLIP pipeline from reference to final composite. Includes: reference analysis of real waterfall characteristics, cliff geometry modeling, FLIP source with initial velocity, higher sim resolution for foam detail (side-by-side comparison shown), white water solver tuning, manual particle-to-mesh conversion and cleanup of...
- **File:** tutorials/houdini-tutorial-creating-realistic-waterfall-simulation-step-by-step.md


### Grain Vortex in Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8fcfu6gmzUQ
- **Author:** raphaël
- **Houdini Version:** Not specified
- **Tags:** "dop", "sop", "rbd", "simulation", "procedural", "advanced"
- **Summary:** Two-stage Bullet RBD sim: a Megascans rock reduced to a ~100-face proxy is scattered, de-intersected (Boolean Detect + iterative nearest-point Blast), and dropped/settled in a box collider; a second sim then carves a smiley-face hole and adds POP Axis Force + POP Wind for a swirling vortex, with a `v.y=0` wrangle to suppress excess upward ejection. Re-timed with a 10x slowdown plus a custom by-frame speed-ramp for a fast-slow-fast feel, then the high-poly mesh is transferred back onto the simulated low-poly points via a transform-zeroing + Transform Pieces trick.
- **File:** tutorials/grain-vortex-in-houdini-tutorial.md


### [Урок] Тяжелый Люкс. Часть 1. (Heavy Lux — Luxury Particle Effect, Part 1)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gsrHHeYadZ0
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** dop, sop, vex, particles, simulation, intermediate
- **Summary:** A 29-minute Russian-language tutorial by Alexander Eskin (Part 1) on creating a "Heavy Lux" luxury particle effect for brand/social media use (final frame shows Dior logo render). Covers POP network setup with All Points emission from 10,000-point grid, stable particle count across frames, wind velocity (value 6) bound to a mask via VEX wrangle using `windgroupraw` (not `windgroup`), and `Cd`...
- **File:** tutorials/урок-тяжелый-люкс-часть-1.md


### Houdini Tutorial: Make Any Geometry Knitted
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mTnQji8a8nw
- **Author:** PolygonCGI
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** sop, vop, modelling, procedural, curves, attributes, rendering, redshift, intermediate, advanced
- **Summary:** A 27-minute tutorial by PolygonCGI building a fully procedural knitted-geometry effect on a skull. The core insight is using UV connectivity + attribute swap to project a tiling knit stitch (built from `mirror`/`polyfuse`/`copytopoints`) onto any mesh surface. Strands are generated via `sweep` with `curlnoise` variation and a `rest` attribute for fiber randomization. Final render uses...
- **File:** tutorials/houdini-tutorial-make-any-geometry-knitted.md


### [Tutorial] Heavy Chic. Part 1.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fjVERoS2olY
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** dop, sop, vex, particles, simulation, intermediate
- **Summary:** A 24-minute English tutorial by Alexander Eskin (Part 1) building a "Heavy Chic" luxury particle effect for social media at 30 FPS. The key technique is using the expression `$F==1` in popsource birth parameters to emit only on frame 1, locking the count at exactly 100,000 particles for the entire animation without multiplication. Frames show progression from blue grid source → jagged...
- **File:** tutorials/tutorial-heavy-chic-part-1.md


### [Tutorial] Heavy Chic. Part 2.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mOKs6Dht5Mw
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** dop, sop, vex, particles, simulation, rendering, intermediate
- **Summary:** A 17-minute continuation tutorial (Part 2) completing the Heavy Chic luxury particle effect. The key refinement is masking particle noise by multiplying amplitude by `Cd` — particles with zero Cd won't flutter. A sharp B-spline ramp corrects gamma for the visual look. Point count scales from ~700k to 11 million by reducing point separation from 0.01 to 0.004. Sim is cached to disk via...
- **File:** tutorials/tutorial-heavy-chic-part-2.md


### [Урок] Тяжелый Люкс. Часть 2. (Heavy Lux Part 2 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UrDkzEXDdLM
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** dop, sop, vex, particles, simulation, rendering, intermediate
- **Summary:** A 22-minute Russian-language continuation (Part 2) by Alexander Eskin completing the "Heavy Lux" particle effect. Covers: noise frequency tuned to 1.7, turbulent noise added via "Add to" blend, float-type (not vector) ramp node with B-spline/Spline interpolation for sharper peak contrast in the mask, sim caching via `filecache`, and final Karma/Mantra render — final frame shows a golden luxury...
- **File:** tutorials/урок-тяжелый-люкс-часть-2.md


### [Tutorial] Glass Tiles
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ps6ZOKEdDos
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, modelling, procedural, instancing, rendering, redshift, intermediate
- **Summary:** A 25-minute tutorial by Alexander Eskin building a procedural glass tile wall for luxury brand rendering. A single tile is modeled from a `box` (0.1 × 0.5), one primitive colored red for orientation reference, then `polyextrude` + `subdivide` with crease (2 divisions) for smooth beveled edges needed for glass refraction. Tiles are distributed on a 128×128 point grid (size 10, height 2.5, YZ...
- **File:** tutorials/tutorial-glass-tiles.md


### [Урок] Стеклянная Плитка (Glass Tile — RU, Extended)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-s-AnXgjw-o
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, modelling, procedural, instancing, attributes, animation, rendering, redshift, intermediate
- **Summary:** A 32-minute Russian-language tutorial (7 minutes longer than the English counterpart) by Alexander Eskin covering the full glass tile pipeline plus tile rotation animation. Builds a single tile (box 0.1×0.5, crease/subdivide bevel), distributes on 128×128 point grid (YZ, 10×2.5), scales via `pscale`. The extended section creates a large secondary geometry to generate a noise-based attribute...
- **File:** tutorials/урок-стеклянная-плитка.md


### [Урок] Мягкая Ткань (Soft Fabric/Weaving — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ju8pDlzR3vM
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vex, procedural, curves, attributes, modelling, intermediate
- **Summary:** A 43-minute Russian-language tutorial by Alexander Eskin building procedural woven fabric geometry purely in SOPs via VEX math. A Z-axis line (2000 points, length 1) → `resample` → `curveu` → `attribwrangle` ("weaving") applies `sin(curveu * freq)` to Y and X positions with controllable amplitude and phase offset. Frequency ~100–200 creates fabric-like loops; parameters promoted to sliders...
- **File:** tutorials/урок-мягкая-ткань.md


### [Tutorial] Soft Weave
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ohj4ag8DZRo
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vex, procedural, curves, attributes, modelling, intermediate
- **Summary:** A 36-minute English tutorial by Alexander Eskin building procedural woven fabric geometry via VEX sine math on a 2000-point line. The key insight: Y gets `sin(@curveu * 100)` and X gets `sin(@curveu * 50)` — dividing X frequency by 2 creates the characteristic interlocking weave pattern (not just parallel waves). Amplitude = coefficient outside brackets; frequency = multiplier inside brackets....
- **File:** tutorials/tutorial-soft-weave.md


### [Урок] Губка (Sponge — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cQd2YXWiQ4k
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vop, vdb, procedural, volumes, modelling, rendering, intermediate
- **Summary:** A 32-minute Russian-language tutorial by Alexander Eskin recreating a sponge/foam effect inspired by Max Shulgi's Instagram work. Workflow: box (0.7 height, 15 wide) → polygon conversion with higher resolution → default noise displacement → points scattered via `pointsfromvolume` → `rest` attribute added for downstream color/material control → `pscale` attribute for size variation. Final...
- **File:** tutorials/урок-губка.md


### [Tutorial] Purple Sponge
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O5cFGKp0n_A
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, dop, vdb, volumes, vellum, particles, simulation, rendering, intermediate
- **Summary:** A 29-minute English tutorial by Alexander Eskin (inspired by Mark's Instagram work) building a purple sponge effect. The pipeline is more complete than the Russian version: box converted to fog VDB via `vdbfrompolygons` + `cloudnoise` default settings → `pointsfromvolume` scatter (400k points, separation 0.07) → secondary noise (Y-component, freq 15, amplitude × 0.05) for organic shape...
- **File:** tutorials/tutorial-purple-sponge.md


### [Урок] Стеклянный Пончик (Glass Donut — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HkMJWwyqo-I
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vop, modelling, animation, rendering, redshift, beginner, intermediate
- **Summary:** A 13-minute Russian-language tutorial building an animated glass donut with flowing surface noise. Uses a `torus` primitive (X-axis, radius 1.5, top/bottom segs 1), applies `aanoise` (anti-aliased flow noise) — the `flow` parameter is animated 0→1 linearly across 300 frames for a seamless loop. Key gotcha: set end frame at 299 (not 300) to avoid duplicate frame at loop boundary. `polyextrude`...
- **File:** tutorials/урок-стеклянный-пончик.md


### [Tutorial] Glass Donut
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=j5Ew_6-W8DE
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vop, modelling, animation, rendering, redshift, intermediate
- **Summary:** A 13-minute English tutorial confirming the Glass Donut workflow with exact parameter values. Torus (X, size 0.5×0.15, 400 rows × 800 cols) + `aanoise` added to position (roughness 0.6, octaves 4, frequency 4, amplitude 0.025). Promote `flow` parameter (mandatory — can't keyframe inside VOP). Animate flow 0→1 linear; place end keyframe at frame **301** so frame 300 in a 300-frame loop never...
- **File:** tutorials/tutorial-glass-donut.md


### [Урок] Розовые Пузыри. Часть 1. (Pink Bubbles Part 1 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=alOGxWIIwTk
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vop, vdb, particles, instancing, simulation, procedural, intermediate
- **Summary:** A 30-minute Russian tutorial (Part 1) by Alexander Eskin building pink bubbles packed inside a large sphere. A polygon sphere (64 cols, scale 2) is split into two streams — one for interior bubble placement, one for surface wave animation. `vdbfrompolygons` → `scatter` (65 points) → `pscale` 0.1 varied by noise multiplication (attribvop) for different bubble sizes. Key: `peak` SOP pushes each...
- **File:** tutorials/урок-розовые-пузыри-часть-1.md


### [Tutorial] Pink Bubble. Part 1.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ypJL4PXxQpg
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, vop, vdb, particles, instancing, simulation, procedural, rendering, intermediate
- **Summary:** A 25-minute English tutorial (Part 1) building pink bubbles inside a sphere, rendered with Octane. Sphere (scale 2, polygon, freq 64) → `peak` to shrink → `vdbfrompolygons` (fog type, reduced voxel size) → `scatter` 65 pts → `pscale` 0.1 → `attribadjust` float, multiply by noise (offset 1.3) for size variation → second `attribadjust` float to set minimum size. Viewport preview via...
- **File:** tutorials/tutorial-pink-bubble-part-1.md


### [Урок] Розовые Пузыри. Часть 2. (Pink Bubbles Part 2 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=faWPP0UPcU0
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, rendering, intermediate
- **Summary:** A 15-minute Russian-language Part 2 completing the Pink Bubbles effect with Octane rendering. Exports geometry elements separately from the SOP network, sets up camera and scene. Key: `subdivide` uses "roll" parameter (not crease) for the final bubble geometry. Creates Octane render target + 3 Octane shaders (Ground, Bubble, Bubble Main). White/preview materials first; colored in final....
- **File:** tutorials/урок-розовые-пузыри-часть-2.md


### [Tutorial] Pink Bubble. Part 2.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uztbmUElafA
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, rendering, intermediate
- **Summary:** A 10-minute English Octane render tutorial (Part 2). Separates the bubble geometry into 3 OBJ nodes (bubble_base/outer sphere, big bubbles, small bubbles); source node stays green/unrendered. `objectmerge` pulls geo into each orange/rendered node. Camera positioned at Z=6, square aspect ratio (not 16:9), adjusted focal length. Octane chosen specifically for quality glass refraction rendering...
- **File:** tutorials/tutorial-pink-bubble-part-2.md


### [Урок] Помада. Часть 1. Моделирование (Lipstick Pt1 Modeling — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fMNkSvAwIFk
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, modelling, procedural, intermediate
- **Summary:** A 15-minute Russian-language modeling tutorial (Part 1 of Lipstick series) by Alexander Eskin. Draws a lipstick profile curve in front view, revolves it (8–12 divisions, not critical) with `revolve` SOP, smooths with `subdivide`, cleans top with `fuse`. The characteristic angled top cut is made by clipping with a rotated `box` (boolean, ~5–6°). A logo is projected onto the surface using...
- **File:** tutorials/урок-помада-часть-1-моделирование.md


### [Tutorial] Lipstick. Part 1. Modeling
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Zqle_HOS7Jg
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, modelling, procedural, intermediate
- **Summary:** An 18-minute English modeling tutorial by Alexander Eskin building a lipstick for product visualization. Front-view `curve` (polygon) → `revolve`; clip top before revolve to prevent overlap. `subdivide` with **4 divisions** (important for the logo emboss field later) → `fuse`. Boolean cut: `box` stretched + rotated ~55° around the cutting axis, then 90° around Y → creates the characteristic...
- **File:** tutorials/tutorial-lipstick-part-1-modeling.md


### [Урок] Помада. Часть 2. Flip Sim (Lipstick Pt2 FLIP Droplets — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H17o8w-CFUM
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, dop, flip, simulation, particles, vdb, modelling, intermediate, advanced
- **Summary:** A 34-minute Russian-language tutorial (Part 2) adding FLIP fluid droplets to the modeled lipstick from Part 1. Creates a "lipstick_droplets" geo node, scatters points on the lipstick surface (density ~0.8), trims to the visible rear half only (front half excluded — don't simulate what can't be seen). `pscale` attribute set to 0.03 with `attribvop` noise variation (scale 2) + random float for...
- **File:** tutorials/урок-помада-часть-2-flip-sim.md


### [Tutorial] Lipstick. Part 2. Flip Sim
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=T1OTnyioFrA
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, dop, flip, simulation, particles, vdb, modelling, intermediate, advanced
- **Summary:** A 26-minute English FLIP droplet tutorial (Part 2) with key production insight: three separate scatter passes at different scales — tiny (density scale ~55), medium, and big (~100 scattered, ~10 largest) — merged together for realistic droplet size distribution on the lipstick. Each pass gets `pscale` = 0.03 base + `attribadjust` random (multiply, mean 0.2) + noise multiply (smaller element...
- **File:** tutorials/tutorial-lipstick-part-2-flip-sim.md


### [Tutorial] Lipstick. Part 3. Rendering
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6V7Y5aBmjo4
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, rendering, intermediate
- **Summary:** A 14-minute Octane rendering tutorial (Part 3 of Lipstick series). Sets up geo nodes: lipstick body, droplets, large droplets (water material). Octane camera "shot_10_output" at half resolution. Octane render target "render_target_010" — path tracing, spectre depth 24, max samples 200, adaptive sampling enabled. No deep image, no environment texture initially (render starts black until lights...
- **File:** tutorials/tutorial-lipstick-part-3-rendering.md


### [Урок] Помада. Часть 3. Рендер (Lipstick Pt3 Render — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pcHSG38zTJg
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** sop, rendering, intermediate
- **Summary:** A 22-minute Russian-language Octane rendering tutorial (Part 3, longer than the 14-minute English companion) completing the lipstick product visualization. Sets up Octane render node + camera "shot_010", render target "render_target_010" (half resolution, specular depth 4, adaptive sampling), Cryptomatte by material/model name. IPR initially black (no lights). Final render shows professional...
- **File:** tutorials/урок-помада-часть-3-рендер.md


### Rain Effect in Houdini | Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Yi0ATGFthqk
- **Author:** Fx Guru (Arbaaj)
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** dop, sop, particles, simulation, volumes, vdb, rendering, beginner, intermediate
- **Summary:** A 33-minute beginner rain effect tutorial by Fx Guru (Arbaaj). A `grid` SOP scaled to match a target geometry (scale 6) serves as the rain emitter — All Points emission from the grid via `popsource` creates dense rain columns. `popgravity` drives particles downward. Life expectancy controls rain density. Particles converted to mesh via VDB for rendering. Secondary splash effect simulated at...
- **File:** tutorials/rain-effect-in-houdini-houdini-tutorial.md



### Tuna Can | procedural modeling and rig with KineFX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hHLH7pr_eZo
- **Author:** cgside
- **Houdini Version:** unspecified
- **Tags:** "kinefx", "procedural-modeling", "rigging", "sop", "sweep", "quadremesh", "animation", "modeling"
- **Summary:** cgside presents a 13-minute practical tutorial on procedurally modeling a tuna can and rigging it with KineFX in Houdini. The modeling starts from a single line placed at the Z axis center, swept into the cap shape with ribbon mode, then resampled, fused, and smoothed. Point selection expressions iterate over points to create the cap design geometry via PolyExpand, followed by QuadRemesh for...
- **File:** tutorials/tuna-can-procedural-modeling-and-rig-with-kinefx.md


### Mechanical rigging in Houdini - Attaching custom controls
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7J-hDF0H6ck
- **Author:** cgside
- **Houdini Version:** unspecified
- **Tags:** "kinefx", "rigging", "controls", "mechanical", "joints", "sop", "procedural-rigging"
- **Summary:** This cgside tutorial demonstrates the practical process of attaching custom control shapes to a mechanical rig in Houdini using KineFX SOP-level rigging. The workflow uses Add SOP or Point Generate to create named target points, initializes transforms with Rig Doctor, creates custom control geometry (sphere, any shape), and connects everything through the Attach Joint Geo node. The tutorial...
- **File:** tutorials/mechanical-rigging-in-houdini---attaching-custom-controls.md


### Yan Paul Dubbelman | Procedural Nature | High-Quality Custom Leaves
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=d3pMfIsvAyQ
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "procedural", "nature", "leaves", "copernicus", "textures", "instancing", "unreal-engine", "modeling", "organic", "vegetation"
- **Summary:** Yan Paul Dubbelman presents a 100-minute session on building high-quality leaf models procedurally in Houdini, with a focus on quality/weight balance for production. The session has two main parts: building the procedural leaf model generators (optimized geometry), then using Houdini's new Copernicus system to generate textures that can be applied to even low-resolution geometry. The resulting...
- **File:** tutorials/yan-paul-dubbelman-procedural-nature-high-quality-custom-leaves.md


### MOPs: Motion Operators for Houdini Part 3
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=q_aD6sza6gA
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "mops", "linear-algebra", "vectors", "matrices", "math", "motion-graphics", "vex", "education", "transforms"
- **Summary:** Henry Foster delivers a 163-minute session (MOPs 103) devoted entirely to the mathematics underlying MOPs and 3D graphics in general. The focus is linear algebra — vectors, matrices, transformations — explained as practical concepts artists can understand and use rather than abstract theory. Henry bridges the gap between "click buttons to parent objects" and actually understanding what...
- **File:** tutorials/mops-motion-operators-for-houdini-part-3.md


### MOPs: Motion Operators for Houdini Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=J2g0v1k6MBs
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "mops", "motion-graphics", "spline", "animation", "packed-primitives", "advanced-modifiers", "procedural-animation"
- **Summary:** Henry Foster continues from Part 1 with MOPs 102, a 170-minute deep-dive into advanced MOPs modifiers. The session leads with the Move Along Spline modifier — a solution to the common motion design problem of moving objects along arbitrary curves. Building on the packed primitive foundation from Part 1, this session explores the trickier modifier nodes that solve more complex kinetic problems....
- **File:** tutorials/mops-motion-operators-for-houdini-part-2.md


### MOPs: Motion Operators for Houdini Part 1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=g9eSle9IVjU
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "mops", "motion-graphics", "packed-primitives", "animation", "falloffs", "instancing", "procedural-animation", "beginners"
- **Summary:** Henry Foster (Toadtorm, developer of MOPs) delivers a 165-minute live session as MOPs 101 — the first comprehensive introduction to the toolkit. Starting with a conceptual PowerPoint on what MOPs is and how it works, he then walks through installation and dives into the core nodes: generators for distributing instances, modifiers for transforming them (translate, rotate, scale), and falloffs...
- **File:** tutorials/mops-motion-operators-for-houdini-part-1.md


### Experimental Motion - CHOPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0XnjEVcaq6A
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "chops", "motion", "animation", "procedural-animation", "organic", "rendering", "art-direction"
- **Summary:** Yan Paul Dubbelman, a Dutch digital artist known for calm, nature-inspired motion work, presents an 84-minute live session on using CHOPs to generate smooth, experimental motion. His focus is on achieving a specific artistic feeling — very calm and organic — rather than technically driven effects. The session demonstrates how CHOPs can process and shape motion data to create the kind of fluid,...
- **File:** tutorials/experimental-motion---chops.md


### Experimental Motion - The SOP Solver
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=A11B_UE07ac
- **Author:** Houdini.School
- **Houdini Version:** Not specified
- **Tags:** "sop", "vop", "particles", "procedural", "advanced"
- **Summary:** Yan Paul Dubbelman's 89-minute SOP Solver workshop covering two generative systems: (1) coral-like growth via a `life` attribute driving Soft Peak (push along normals) inside a per-frame Remesh loop, with normal-biased velocity, Curl Noise, Labs Sharpen Mesh, and `fit($F,...)` tapering for art-directed organic/crystalline shapes; (2) a 3D vein/"synapse" network built with Find Shortest Path + Tetrahedron Embed + Fuse + Resample, then animated via Point Cloud Open/Filter spreading a decaying `life` attribute for pulsing neuron-firing visuals, drivable into a Sweep's radius or shader color.
- **File:** tutorials/experimental-motion---the-sop-solver.md


### Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xjf_mQKI3R8
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "procedural", "nature", "plants", "flowers", "organic", "modeling", "art-direction", "instancing", "no-simulation"
- **Summary:** Yan Paul Dubbelman presents a 74-minute accessible introduction to building procedural botanical elements (flowers, plants, natural forms) in Houdini. The session is explicitly designed to break down the intimidating "Houdini wall" — the misconception that Houdini requires simulations and heavy coding for natural work. No simulations are used at all; everything is SOP-level procedural geometry...
- **File:** tutorials/yan-paul-dubbelman-procedural-nature-procedural-living-plants.md

### Procedural HDAs for Unreal
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rKcH4oIfoVw
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "hda", "unreal-engine", "procedural", "splines", "building-generator", "houdini-engine", "session-sync", "materials", "pipeline"
- **Summary:** Julian (Technical Artist at Cloud Imperium Games, creator of tools for Star Citizen) teaches a step-by-step course on building a production-ready procedural building generator HDA. The workflow uses interactive splines/curves as the building footprint input, procedurally models the structure, adds an automated cable system, and exposes a user-friendly parameter interface. The HDA is then...
- **File:** tutorials/procedural-hdas-for-unreal.md


### Velocity Forces 2.0: Advanced
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EuL8598tnm4
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "velocity", "vdb", "volumes", "vex", "optical-flow", "surface-advection", "turbulence", "simulation", "math", "advanced"
- **Summary:** David Torno (also teaches Attributes, Loops, Noise) presents the advanced sequel to his Forces course. Velocity Forces 2.0 dives deep into the nuances of Houdini volume types (standard vs. OpenVDB) and their impact on velocity field behavior. Techniques covered include eliminating activation stepping artifacts, blending multiple velocity fields, using simulation outputs as velocity sources,...
- **File:** tutorials/velocity-forces-20-advanced.md


### Small Scale Fluids
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aKJB3uOKFKM
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "flip", "fluid", "simulation", "small-scale", "meshing", "redshift", "karma", "viscosity", "vdb", "production"
- **Summary:** This Houdini.School course (Small Scale Fluids 235) takes a production-focused approach to small-scale FLIP fluid simulations designed for close-up, macro-style camera sequences. The two-session live course covers project setup, FLIP settings best practices, emission and variable viscosity control, collision geometry optimization, advanced meshing techniques, and VDB-based approaches to shape...
- **File:** tutorials/small-scale-fluids.md


### Surface Advection
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=w_NnhoKeLlE
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "advection", "particles", "volumes", "surface", "sop", "dop", "redshift", "rendering", "simulation", "organic"
- **Summary:** This Houdini.School course focuses exclusively on surface advection — constraining particle flow to move along geometry surfaces rather than through free space. Two approaches are taught: Session 1 introduces a DOP-based volume simulation approach and a faster non-simulated SOP solution. Session 2 applies these techniques to more complex geometry using simulated particles and animated volume...
- **File:** tutorials/surface-advection.md


### Forces: Building Custom Velocity Setups
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=v1psrXhj9IY
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "velocity", "forces", "simulation", "vex", "volumes", "vector-fields", "pop", "procedural"
- **Summary:** This Houdini.School course takes a progressive, two-session approach to custom velocity setups. Session 1 breaks down the fundamental concepts: what vectors, forces, velocity, and velocity fields actually mean in Houdini's context. Session 2 builds a collection of practical force setups using those concepts. The course is structured as a toolkit — students end up with multiple approaches they...
- **File:** tutorials/forces-building-custom-velocity-setups.md


### Attributes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VM3m52SHUrk
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "attributes", "geometry", "vex", "rbd", "flip", "vellum", "crowds", "fundamentals", "beginner"
- **Summary:** David Torno (Houdini.School instructor) presents a comprehensive course on Houdini attributes, structured as step-by-step sessions covering geometry component foundations through advanced attribute workflows. The course clarifies terminology, explains attribute classes and types, details the geometry spreadsheet, and covers intrinsics. Practical implementation examples are drawn from RBD,...
- **File:** tutorials/attributes.md


### Art Directing Cloth in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=psd-vus4U5s
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "vellum", "cloth", "simulation", "redshift", "karma", "rendering", "mops", "forces"
- **Summary:** Paul Estevez (CG generalist and motion designer from Munich) presents a Houdini.School course on art directing cloth with Vellum. The course covers the full process from basic geometry setup through applying forces and tools for realistic fabrics, setting up attributes for export to other software, and lighting, texturing, and rendering cloth with Redshift and Karma. Distinctive techniques...
- **File:** tutorials/art-directing-cloth-in-houdini.md


### MOPs: Motion Operators for Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pqGY2M2VBQo
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "mops", "motion-graphics", "animation", "procedural-animation", "rbd", "vellum", "falloffs", "packed-primitives"
- **Summary:** Henry Foster (developer of MOPs, 15-year technical artist) presents the MOPs toolkit course for Houdini.School. MOPs is a free open-source toolkit designed to make motion design in Houdini as intuitive as C4D MoGraph. The course covers MOPs generators, modifiers, and falloffs for duplicating, bouncing, aiming, and rotating points and geometry. MOPs can be layered on top of RBD and Vellum...
- **File:** tutorials/mops-motion-operators-for-houdini.md


### Problem-Space
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nUwA8xsmnS0
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "attributes", "rest-position", "uv", "world-space", "object-space", "simulation", "instancing", "procedural", "advanced"
- **Summary:** Kevin (Technical Artist/TD at Buck Design) presents a course on problem-space thinking in Houdini — the technique of distorting the coordinate space in which attributes are evaluated rather than the attributes themselves. The course starts with world space and rest position manipulation for color and UV attributes, then expands to using space distortion for simulations and instances, and...
- **File:** tutorials/problem-space.md


### History of Houdini Systems
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mwUn21-v_0s
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "history", "flip", "particles", "l-systems", "noise", "ocean", "fundamentals", "education"
- **Summary:** Kate Zegarace (VFX artist at MPC Toronto and Houdini.School teacher) delivers a four-lecture series on the history and evolution of Houdini's key systems. Lecture 1 covers FLIP ocean tools and particle-based hydrodynamics. Lecture 2 explores L-systems and their mathematical basis for generating natural patterns like trees and lightning. Lecture 3 traces the history of Houdini's noise tools...
- **File:** tutorials/history-of-houdini-systems.md


### Maths for Artists
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=krZVhZFvAo0
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "math", "vectors", "matrices", "quaternions", "vex", "fundamentals", "education", "calculus", "complex-numbers"
- **Summary:** This Houdini.School course demystifies the mathematics underlying Houdini's core systems for artists who may lack a formal math background. The curriculum progresses from number systems and complex numbers through Cartesian and polar coordinates, then to vectors (with both problem-solving and art-direction applications), multivariable calculus basics for understanding vector fields,...
- **File:** tutorials/maths-for-artists.md


### Procedural Growth with KineFX and the Labs Tree Tools
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=j5XxDiG25wQ
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "kinefx", "labs", "tree", "growth", "vex", "chops", "procedural", "wind", "rigging", "vegetation", "animation"
- **Summary:** Mark Fancher presents an intermediate-to-advanced Houdini.School course on procedural vegetation using the free, built-in SideFX Labs Tree Tools as the starting geometry, then extending into KineFX rigging and animation. The course covers rigging the tree with KineFX, building a procedural growth sequence and a wind animation system using VEX and CHOPs, and goes deep into modifying the Labs...
- **File:** tutorials/procedural-growth-with-kinefx-and-the-labs-tree-tools.md


### Scientific Phenomena in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=g-EDNX2uaXo
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "scientific-visualization", "volumes", "particles", "pyro", "planets", "fractals", "procedural", "vfx", "simulation"
- **Summary:** Kate Zegarace (VFX artist at MPC Toronto, credits: Umbrella Academy, The Boys, Raised by Wolves, The Witcher) teaches a course bridging scientific knowledge with VFX practice in Houdini. Each session introduces the science of a phenomenon before building the corresponding VFX setup. Sessions cover: storm cloud formation and volumetric simulation, procedural planetary systems informed by...
- **File:** tutorials/scientific-phenomena-in-houdini.md


### Visualizing Protein Data Bank Information
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=f7QwzqZqtFI
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "scientific-visualization", "data-visualization", "pdb", "molecular", "attributes", "particles", "simulation", "biology"
- **Summary:** Kate Zegarace (Houdini.School instructor and VFX artist) presents a course on molecular visualization using Protein Data Bank (PDB) data as the input. The course covers the biology basics of proteins (what they are, how they work) then builds the Houdini pipeline to process PDB files and generate multiple visualization modes: space-filling, wireframe, ball-and-stick models. Atoms are animated...
- **File:** tutorials/visualizing-protein-data-bank-information.md

### Liquid SOPs
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YKnqahKFNuY
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "sop", "liquid", "procedural-animation", "vex", "vop", "noise", "curves", "non-simulation", "motion-graphics"
- **Summary:** This Houdini.School course presents a solver-free approach to liquid effects, emphasizing art direction and procedural control over physical accuracy. The course teaches artists to think about the mechanics of liquid motion and decompose that understanding into geometry-only setups using noises, curves, VOPs, and VEX. By eliminating FLIP, volume advection, and Vellum entirely, the workflow is...
- **File:** tutorials/liquid-sops.md


### From C4D to Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=V31YogBW2Y0
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "beginner", "cinema4d", "mograph", "attributes", "procedural", "cloner", "motion-graphics", "fundamentals"
- **Summary:** Matt Taylor (Houdini artist and animation director) teaches Houdini.School students coming from Cinema 4D how to translate their existing C4D knowledge into Houdini workflows. The course runs parallel builds — constructing the same animated scene in both C4D and Houdini to highlight equivalences. Key topics include reading, creating, and manipulating geometry attributes, and recreating MoGraph...
- **File:** tutorials/from-c4d-to-houdini.md


### Houdini FX in Unreal
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RDiA2R47Wzo
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "unreal-engine", "virtual-production", "hda", "megascans", "rendering", "aces", "substance-painter", "procedural", "pipeline"
- **Summary:** Guido Poncini presents a comprehensive course on integrating Houdini with Unreal Engine for virtual production and installation sequences. The course uses the Maxi Museum in Rome as the location reference, covering procedural modeling and UV mapping in Houdini, import into Unreal, scene organization with sequences and subsequences, Megascans material application, HDRI-based lighting, and ACES...
- **File:** tutorials/houdini-fx-in-unreal.md


### Loops
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OQDFQtoTOuA
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "loops", "sop", "vop", "vex", "for-each", "while", "procedural", "fundamentals", "beginner"
- **Summary:** David Torno (Houdini.School instructor, also teaches Attributes) presents a focused course demystifying loops in Houdini. The course covers all four loop types (for, for-each, while, do-while) across SOPs, VOPs, and VEX contexts, giving students a complete picture of where and how to use repetitive processing in Houdini workflows. Both complete finished builds and abstract technical examples...
- **File:** tutorials/loops.md


### Simulated Creatures
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=M8HOGm6FxIw
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "fem", "soft-body", "simulation", "vellum", "animation", "keyframe", "constraints", "procedural-animation", "creatures"
- **Summary:** Matt Taylor (animation director, 3D artist, teacher) presents a course focused on using Houdini's FEM solver to create convincingly soft and organic creature movement. The course covers geometry preparation for FEM, multiple animation methods within FEM (forces, constraints, animated rest states, target strengths, pin constraints), and FEM management for efficiency. A key element is the...
- **File:** tutorials/simulated-creatures.md


### Magical FX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=J9dhXxxLPfI
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "particles", "pop", "pyro", "vop", "fluids", "lighting", "rendering", "vfx", "procedural", "portal"
- **Summary:** This Houdini.School course takes a project-based approach, building three distinct magical FX types across multiple sessions. It begins with customizable particle effects for characters, progresses to a particle disintegration system built with VOPs and POPs, then creates a pyro-based flame effect. These individual effects combine in the final session into a portal scene that is fully lit,...
- **File:** tutorials/magical-fx.md


### Working with Scientific Datasets in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GRUGv5ydLFQ
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "scientific-visualization", "data-visualization", "vdb", "bgeo", "particles", "volumes", "python", "datasets", "medical"
- **Summary:** Kalina Bocavic (Director of the Advanced Visualization Lab at the National Center for Supercomputing Applications) presents a course bridging supercomputing scientific datasets and Houdini. The course covers multiple scientific data formats: BGEO for volumetric cloud and particle simulations, OpenVDB for volumetric data, medical scan image stacks converted to geometry, and adaptive mesh...
- **File:** tutorials/working-with-scientific-datasets-in-houdini.md


### Noise
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FKHhGJFvjys
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "noise", "vop", "vex", "attributes", "volumes", "particles", "shaders", "pdg", "python", "procedural"
- **Summary:** This Houdini.School course (David Torno) goes beyond basic noise applications to teach artists how to make noise-driven setups that are not immediately recognizable. The course covers all of Houdini's stock noise types and how to manipulate them to produce more visually interesting results. Use cases include driving attribute values, creating shaders and materials, adding detail to volumes,...
- **File:** tutorials/noise.md


### BUILD YOUR BRAIN – Cell division in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EE1wuXaI8wI
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "vellum", "vdb", "advection", "growth", "rendering", "redshift", "karma", "compositing", "procedural"
- **Summary:** Tim (Houdini.School instructor) presents a course building a procedural brain/cell-division growth effect in Houdini. The setup combines Vellum ring simulations with VDB advection and various sub-techniques stitched together into a continuous growth sequence. The course covers rendering inside Houdini's rendering context with Redshift (primary renderer) and Karma (secondary walkthrough), then...
- **File:** tutorials/build-your-brain-cell-division-in-houdini.md


### Character Design and Modeling
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4tJmvGrhxA4
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** "modeling", "character", "vdb", "boolean", "polygon", "character-design", "animation", "procedural"
- **Summary:** Christopher Rutledge (CG artist and short filmmaker) teaches a Houdini.School course on creating original characters entirely within Houdini. The workflow starts with concept sketching and design, then moves to blocking out the body and eyes using polygons alongside VDB, Boolean, and reshape operations. A distinctive element is the translation of 2D hand-drawn animation techniques into Houdini...
- **File:** tutorials/character-design-and-modeling.md


### 00 weeks overview v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=W1_pCONvY_o
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vop", "particles", "simulation", "pyro", "beginner"
- **Summary:** Syllabus/overview (not hands-on) for a 5-week Thor's Hammer lightning-strike VFX course: Week 1 modeling/shading/interface basics; Week 2 CHOPs animation + ray/lightning VOPs setup; Week 3 points/particles/collisions + spark system; Week 4 volumes/Pyro solver smoke pass; Week 5 materials/render passes/COPs compositing.
- **File:** tutorials/00-weeks-overview-v1-1080p.md


### 03 houdini versions v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EMmAmGGsI6I
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "beginner"
- **Summary:** Licensing/edition overview (not version-specific): Houdini Core has the full toolset minus simulation (no Pyro/fluids/RBD/particles/crowds); FX is the complete unlimited commercial package; Indie is FX features under a limited commercial license capped at 4K×4K render output; Education is FX features for verified teaching institutions; Apprentice is free with full FX features for learning, watermarked and resolution-capped. Apprentice is sufficient for following a learning course.
- **File:** tutorials/03-houdini-versions-v1-1080p.md


### 51 introducing the sop solver v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8HkP7iVgi0Y
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vex", "wrangler", "particles", "simulation", "beginner"
- **Summary:** Manually builds a position-integration solver to demystify what POP/particle solvers do: scatters points on a grid, gives them a constant velocity attribute, and wires a Point Wrangle (`@P = @P + @v;`) inside a SOP Solver so each frame feeds back the previous frame's result. Catches and fixes the classic per-frame-vs-per-second bug by multiplying velocity by Houdini's `$TimeInc` global variable.
- **File:** tutorials/51-introducing-the-sop-solver-v1-1080p.md


### 52 creating a simplified particle system v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=l65A4S4YhSw
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vex", "wrangler", "particles", "simulation", "beginner"
- **Summary:** Extends the manual SOP Solver setup into a hand-rolled particle system: Scatter's Global Seed set to `$F` for continuous emission, an `age` attribute incremented via `@age += $TimeInc` each frame, lifespan-based death via `removepoint()` when age exceeds a `life` attribute, and per-particle randomized velocity via `rand(@ptnum + @Frame)` + `fit01()`. Sets up a later comparison against native POPs.
- **File:** tutorials/52-creating-a-simplified-particle-system-v1-1080p.md


### 53 recreating our solver with pops v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9objvx69_58
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vop", "particles", "simulation", "beginner"
- **Summary:** Rebuilds the prior two lessons' hand-rolled SOP Solver particle system using a native POP Network instead: a POP Source on the Birth tab replaces the manual scatter/emission rate (matched to 2400 particles/sec = 100/frame at 24fps), Set Initial Velocity + Variance replaces the hand-coded velocity randomization, and Life Expectancy replaces the manual age/life wrangle — same visual result, far more attributes tracked automatically (id, age, life, position-previous, UV, etc.) than the manual version.
- **File:** tutorials/53-recreating-our-solver-with-pops-v1-1080p.md


### 76 starting the smoke vortex v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=BFZ3tItjKn8
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "dop", "sop", "pyro", "smoke", "simulation", "intermediate"
- **Summary:** Builds a rotating, noise-distorted Torus as Pyro emitter geometry: Trail SOP (Compute Velocity) derives a true velocity field from the torus's rotation + Mountain-noise shape change, transferred via Attribute Transfer onto points generated by a Pyro Source's Volume Scatter. Attribute Noise adds animated density/temperature variation, rasterized into source volumes via Volume Rasterize Attributes for the next lesson's actual Pyro DOP sim.
- **File:** tutorials/76-starting-the-smoke-vortex-v1-1080p.md


### 78 building the vortex dop network v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FAE7gVev-ss
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "dop", "pyro", "smoke", "simulation", "advanced"
- **Summary:** Builds the Pyro DOP network (Pyro Solver, Smoke Object, Volume Source) around the prior lesson's torus source, sizing the container via a temporary Static Object proxy. Redirects Buoyancy Direction away from "up" to drive the vortex sideways instead. Main teaching point: the Dissipation micro-solver's Control Field (remaps dissipation by Temperature over a Control Range) appears to do nothing at the default 0-1 range because the source's density/temperature values run up to ~2 and are re-added every step by Volume Source — raising the Control Range max to ~4 makes dissipation visibly take effect.
- **File:** tutorials/78-building-the-vortex-dop-network-v1-1080p.md


### module i   week 01   01   your first houdini project v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mq1snWFUBj0
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** sop, lop, solaris, karma, rendering, beginner
- **Summary:** Sets up the default "build" desktop layout and drops a sphere to introduce the basic SOP geometry workflow. Week 1's project is procedural modelling of a scattering-based scene, followed by lighting/materials in Solaris (the new USD-based context), rendering with Karma (the new render engine), and a light comp pass in Nuke. Establishes the course pipeline: SOP geometry -> Solaris LOP -> Karma...
- **File:** tutorials/module-i-week-01-01-your-first-houdini-project-v1-1080p.md


### module i   week 02   01   creating a new project v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mjw4gT36Ub4
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** sop, instancing, attributes, procedural, intermediate
- **Summary:** This week's focus is scattering objects over a surface — specifically distributing elements over a head mesh. Two sub-projects are introduced: building the scattered geometry entirely inside Houdini, and using Megascans models as instanced scatter elements through a Quixel Bridge workflow. New H18.5 scatter-related nodes and improved Copy to Points workflows are introduced. The head surface is...
- **File:** tutorials/module-i-week-02-01-creating-a-new-project-v1-1080p.md


### module i   week 03   01   introduction to volumes v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hEcmhhNlpzY
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** sop, vop, volumes, intermediate
- **Summary:** Explains the fog VDB vs. SDF (signed distance field) distinction: fog is a density field (0 outside, positive inside), while an SDF is a distance field (negative inside, positive outside, zero exactly at the surface). Builds a cloud volume from a polygon mesh via the chain: mesh -> VDB from Polygons (SDF) -> VDB Reshape (dilate to add volume) -> cloud noise via Volume VOP. The Volume VOP...
- **File:** tutorials/module-i-week-03-01-introduction-to-volumes-v1-1080p.md


### module i   week 04   01   introduction to particles v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9S5YABmK_eU
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** dop, sop, particles, simulation, beginner
- **Summary:** Clarifies that in SOPs these entities are called "points," while inside a DOP simulation the same entities are called "particles" — both inspected via the Geometry Spreadsheet. Sets up a POP Network sourcing from a medium-resolution pig-head test geometry, using POP Source (surface emission), POP Gravity, POP Drag and POP Color. Demonstrates key particle attributes: `@age`, `@life`, `@dead`...
- **File:** tutorials/module-i-week-04-01-introduction-to-particles-v1-1080p.md


### module i   week 05   01   importing the geometry v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Fo3HaNq9f8M
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** sop, flip, dop, intermediate
- **Summary:** Workflow: File -> New Project, drag the .abc into the project geo folder, create a geometry node, add an Alembic SOP and browse to the file. A critical step is adding a Convert SOP after Alembic to convert from PolySoup to regular polygons — necessary for correct geometry selection and attribute access later. The animation is slowed using a Time Shift SOP: integer frames are disabled and time...
- **File:** tutorials/module-i-week-05-01-importing-the-geometry-v1-1080p.md


### module i   week 06   01   introduction to grains v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XPDsqVutqDw
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** dop, sop, vellum, simulation, intermediate
- **Summary:** FBX import workflow: File -> Import Filmbox FBX, then scale down to 0.1 for proper scene scale (~2m character height). Creates a geometry node, uses Object Merge to bring in the zombie, then converts it via VDB From Polygons -> Points From Volume to scatter grain particles throughout the body volume. The grain setup uses the Vellum Grains shelf tool to create the PBD grain solver. Key grain...
- **File:** tutorials/module-i-week-06-01-introduction-to-grains-v1-1080p.md


### module ii   week 01   01   basic bullet sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vQSQgkSvm8g
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** dop, sop, rbd, attributes, intermediate
- **Summary:** Starts bare-bones: a single box, raised and rotated, then Tab -> "RBD Bullet Solver" auto-creates two nodes (RBD Configure + DOP Import) and an immediate working simulation. Escalates to Voronoi fracture: a Voronoi Fracture SOP with a point cloud controlling chunk size, then a Boolean fracture pass for sharper edges, followed by the RBD Bullet Solver on the fractured geometry. Introduces...
- **File:** tutorials/module-ii-week-01-01-basic-bullet-sim-v1-1080p.md


### module ii   week 02   01   importing the geometry v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tC3H8wBaytE
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** dop, sop, rbd, intermediate
- **Summary:** Imports a compressed Alembic asset with multiple LODs; extracts it and selects LOD2 as the balance between polygon detail and simulation speed. Creates a geometry node named "building," adds an Alembic SOP, and scales the import to 0.01 since the building was modelled at real-world scale in meters and needs shrinking for the Houdini scene. The week's concept is a reverse-gravity /...
- **File:** tutorials/module-ii-week-02-01-importing-the-geometry-v1-1080p.md


### module ii   week 03   01   splitting by material v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cvAuweF1fvg
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** dop, sop, rbd, attributes, intermediate, advanced
- **Summary:** Continues from the Week 2 building Alembic, resaving the project under a new name. A key setup step is the Connectivity SOP set to "primitives" mode to identify separate geometry pieces, followed by a Convert SOP to move from PolySoup to standard polygons. Geometry is split by material groups so different pieces receive different fracture treatment: the RBD Material Fracture SOP (an H18.5+...
- **File:** tutorials/module-ii-week-03-01-splitting-by-material-v1-1080p.md


### module ii   week 04   01   importing the geometry v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uPPW2sI_oyw
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** dop, sop, rbd, attributes, intermediate
- **Summary:** Uses a different skyscraper Alembic asset with multiple LODs available, selecting LOD3 for simulation. The import workflow mirrors Week 2: Alembic SOP -> Transform at 0.01 scale -> visual check. The week's concept is a realistic downward collapse where the building folds and pancakes floor by floor, with separate simulation of concrete slabs, steel rebar/frame, and glass panes. Sets up the...
- **File:** tutorials/module-ii-week-04-01-importing-the-geometry-v1-1080p.md


### module i   week 01   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZYFlDsFBxhA
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, pyro, advanced
- **Summary:** Covers a city ground explosion with rock/rubble/paving erupting upward. The RBD focus is a Boolean fracture system for high-quality, varied chunk shapes — big and small pieces with interesting silhouettes, rather than uniform Voronoi output. Constraints are set up minimally, mainly to hold the initial state rather than to drive complex breaking behaviour. A debris-sourcing pipeline uses the...
- **File:** tutorials/module-i-week-01-01-intro-v1-1080p.md


### module i   week 02   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=G1JI3ACUZN4
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, attributes, advanced
- **Summary:** Covers a bus stop with mixed-material destruction: a steel frame (metal), glass panels and wood planks. The new technique highlighted is the RBD Material Fracture SOP for both glass and wood fracture patterns. The key technique for metal is "plasticity" (new around H18) applied to soft constraints — metal holds its bent/deformed shape after impact instead of springing back, with constraints...
- **File:** tutorials/module-i-week-02-01-intro-v1-1080p.md


### module i   week 03   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QkzF0SC76qY
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, attributes, animation, advanced
- **Summary:** Overview of Week 3 (weeks 3 and 4 form one large project): the car slides in sideways and impacts a post, with metal bending and glass shattering across the two weeks. Week 3's focus is geometry organization — the car model is complex with many named parts, a detailed chassis, wheels and windows — and selecting the right pieces for simulation versus keeping others rigid or kinematic is...
- **File:** tutorials/module-i-week-03-01-intro-v1-1080p.md


### module i   week 04   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=w9p4zfurT2A
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, rendering, karma, advanced
- **Summary:** Two types of car glass require different fracture treatment. The windscreen uses laminated glass (with a PVB plastic inner layer): it fractures into thousands of small blocks that stay together and bend slightly like plastic rather than scattering as shards, achieved with dense fine Voronoi fracture, soft glue constraints and slight plasticity. Side windows use tempered glass: it shatters into...
- **File:** tutorials/module-i-week-04-01-intro-v1-1080p.md


### module i   week 01   09   setting the active attribute v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VXkmQAGzBbA
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, attributes, vex, advanced
- **Summary:** Explains the standard H19+ RBD workflow node chain, where every RBD node has a pink primary input plus constraint and proxy inputs: RBD Configure -> RBD Material Fracture -> RBD Constraint Properties -> RBD Solver. The `active` integer attribute (0 = kinematic/frozen, 1 = simulating) is set per primitive. Two common methods are shown: keyframe-animating `active` inside a SOP Solver within the...
- **File:** tutorials/module-i-week-01-09-setting-the-active-attribute-v1-1080p.md


### module i   week 02   15   starting the post sim setup v1 1080p1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XFOd1dy92Eg
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, procedural, intermediate
- **Summary:** Adds a Null SOP after the DOP Import cache (named e.g. "OUT_SIM") to cap the simulation stream. A Split SOP (or separate Blast) separates top vs. bottom pieces for independent treatment. A new geometry node named "post_sim" is created, using Object Merge SOPs to pull in: the cached RBD fractured geometry, the original un-fractured metal mesh (pre-fracture geo for deformation), the glass mesh,...
- **File:** tutorials/module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1.md


### module i   week 02   16   point deforming the metal and glass v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oZh_MAnZyaQ
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, attributes, advanced
- **Summary:** Before this node existed, the old method used a for-each loop capturing each piece's transform and deforming the matching hi-res piece individually — complex and slow. The RBD Deform Pieces workflow instead takes the high-res render geometry on input 0 and the fractured/simulated proxy geometry stream on input 1, matching pieces by their shared `name` attribute and applying per-piece rigid...
- **File:** tutorials/module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md


### module i   week 02   17   fixing post sim fix and rbddisconnectedfaces node v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=R-ay-5fX_Os
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, sop, rbd, rendering, advanced
- **Summary:** After glass fracture and deformation, some faces become disconnected from their pieces — they float in space because they lost their piece-level transform. The RBD Disconnected Faces SOP reconnects orphaned faces back to their nearest named piece. Workflow: after RBD Deform Pieces, add RBD Disconnected Faces with "fix" mode enabled. The post-sim output is then split by name groups: a Blast SOP...
- **File:** tutorials/module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md


### module ii   week 01   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Y00rlBFqpxQ
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, cloth, simulation, intermediate
- **Summary:** Project: a crocodile attack scene where a hunter is grabbed in the crocodile's mouth. Vellum is praised for being fast and versatile, handling cloth, string, hair, soft bodies and grains all in one solver. Week 1 is a rapid overview demonstrating cloth, soft bodies (tetrahedral constraints), string/wires and grains in a single lesson. The full project pipeline simulates the soft-body hunter...
- **File:** tutorials/module-ii-week-01-01-introduction-v1-1080p.md


### module ii   week 02   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=161Gcdsi6Nw
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, cloth, simulation, intermediate, advanced
- **Summary:** Workflow begins by draping cloth in T-pose: fitting the clothing geometry to the body before the main simulation so clothing sits correctly at frame 0. Geometry preparation includes a Remesh SOP to triangulate cloth (Vellum produces more natural folds on triangles), group creation for constraint regions, and pre-fracturing cloth with cut lines ready for the simulation to tear along. Key Vellum...
- **File:** tutorials/module-ii-week-02-01-introduction-v1-1080p.md


### module ii   week 03   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F2vdSX1Dzgk
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, cloth, simulation, advanced
- **Summary:** Week 3 brings everything together into a single simulation. The key technique is point-deforming the hunter body to follow the crocodile mouth animation: the inner part of the body, inside the croc's mouth, is not simulated — it simply follows the croc mouth's deformation, preventing collision-explosion artifacts when the mouth closes on the body. Only the body parts outside the croc's mouth...
- **File:** tutorials/module-ii-week-03-01-introduction-v1-1080p.md


### module ii   week 04   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SlbMugY762Q
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, particles, rendering, karma, advanced
- **Summary:** The final Vellum week covers grains simulation and full render. The grain-sourcing efficiency trick uses the previous Vellum simulation (crocodile + hunter) to generate a time-varying source volume: as the croc thrashes and the hunter is squeezed, the contact region emits grains, driven by a SOP Solver or DOP stamp inside the grains network. The grain network is built from scratch in DOPs...
- **File:** tutorials/module-ii-week-04-01-introduction-v1-1080p.md


### module ii   week 01   02   introduction to vellum v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=LKhBUByCqJw
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, cloth, particles, intermediate
- **Summary:** Setup: a new project "croc_attack" with a "vellum_intro" geometry node. Cloth: grid -> Remesh (to triangulate for better folds) -> Vellum Cloth SOP (via shelf or tab), with bend stiffness, stretch stiffness and mass as the key parameters. Pinning is done by grouping the top edge and attaching it to geometry, or using Vellum Attach to Geometry. String/wire: a curve feeds Vellum String SOP, with...
- **File:** tutorials/module-ii-week-01-02-introduction-to-vellum-v1-1080p.md


### module ii   week 01   04   tetrahedral soft bodies v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pxWRHQjHpNk
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, rigging, simulation, advanced
- **Summary:** Positions the hunter at X=5 so he sits correctly inside the crocodile's mouth when it closes. Uses the Vellum shelf tool: select the hunter geometry -> Vellum Solid Object (tetrahedral). The shelf automatically adds Poly Reduce (a proxy mesh for speed), Tet Conform, Vellum Solid Object constraints, and a Vellum Solver. A noted problem is that Poly Reduce defaults are too aggressive,...
- **File:** tutorials/module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md


### module ii   week 01   06   updating the rest blend v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aUkXMjjLT-k
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, rigging, attributes, advanced
- **Summary:** The hunter's arms are raised in a T-pose / gun-holding pose, which looks wrong at rest. The fix is to manually re-pose the arms and blend this new rest position into the Vellum constraints so the solver treats it as the natural rest state. Workflow: group the left and right arms separately using bounding-sphere group mode, apply a Transform SOP per group to lower the arms, then feed this...
- **File:** tutorials/module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md


### module ii   week 03   06   breaking welds and constraints v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dfD5FUdMCTc
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 19
- **Tags:** dop, vellum, attributes, vex, advanced
- **Summary:** The collar stitch and boot attachment constraints need to break at a specific frame when the crocodile flips the hunter over. Weld breaking is enabled via the "breaking" checkbox on the Vellum Weld node with a break threshold of 1. Because the break threshold cannot be keyframed directly on the Vellum node, a SOP Solver inside the DOP network is required to modify the constraint geometry per...
- **File:** tutorials/module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p.md


### week 01   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9ocqYW1XHk4
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rbd, simulation, dop, procedural, beginner
- **Summary:** The instructor outlines what week one covers: importing the bridge model, splitting it into simulated vs. static parts, and further categorising those parts into deformable metal, rigid metal and road geometry. The road is fractured with a Boolean (cutting geometry) method while the metal uses Voronoi. Soft constraints with plasticity are configured to give the metal realistic bending...
- **File:** tutorials/week-01-01-intro-v1-1080p.md


### week 02   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IoxlDdh5OPg
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rbd, vellum, simulation, dop, beginner
- **Summary:** The instructor introduces the cable simulation strategy, distinguishing between the heavy, near-rigid horizontal suspension cables (simulated with Bullet hard constraints driven by the week-one guided sim result) and the more flexible vertical hanger cables (simulated with Vellum). The geometry is simplified to four strands before simulation. The guided simulation workflow in Houdini 18 is...
- **File:** tutorials/week-02-01-intro-v1-1080p.md


### week 03   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OnBsOG4SwIU
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18.5
- **Tags:** rbd, simulation, dop, instancing, attributes, beginner
- **Summary:** The instructor explains how to import varied vehicle geometry, separate bodies from wheels, and scatter them across the road using new Houdini 18.5 SOPs (Scatter and Align, Attribute from Pieces). A procedural system removes intersecting cars before a lightweight pre-simulation settles them against each other. The main sim then uses soft constraints and cone-twist constraints to fake vehicle...
- **File:** tutorials/week-03-01-intro-v1-1080p.md


### week 04   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GQSxmuvXsvM
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** particles, pyro, simulation, dop, attributes, beginner
- **Summary:** This week covers three simulations: one POP (particle) simulation for debris chunks and two Pyro smoke simulations. The Debris Source SOP scatters points between separating RBD pieces and deletes them by age. Particles are then culled by speed so only fast-moving geometry emits debris. Noise is added to density and temperature attributes before feeding into the Pyro sims, which are enhanced...
- **File:** tutorials/week-04-01-intro-v1-1080p.md


### week 05   01 intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_UqQ526rOzI
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rendering, mantra, volumes, compositing, beginner
- **Summary:** The final week of the Bridge Destruction course focuses on rendering. Pre-built shaders and cameras are merged in from a provided scene file. Vehicle colours are randomised procedurally to add visual variety. Fog volumes are generated to set atmosphere, then everything is lit with an HDRI and a distant light. The Mantra render passes are taken into Nuke for a straightforward but dramatic...
- **File:** tutorials/week-05-01-intro-v1-1080p.md


### week 01   11   rbd configure v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dIBS14jw25k
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rbd, simulation, dop, attributes, intermediate
- **Summary:** The instructor drops in the RBD Configure node, then isolates a single piece using Delete nodes to inspect its collision geometry. The Visualize tab is used to reveal the collision proxy, which is larger than the actual mesh by default due to collision padding. The tutorial covers how to adjust collision padding on the solver vs. per-piece, and how to switch collision shape type (convex hull,...
- **File:** tutorials/week-01-11-rbd-configure-v1-1080p.md


### week 02   03   starting the guided sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9qkYzPC9IKM
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rbd, simulation, dop, attributes, intermediate
- **Summary:** The instructor gives the cable blocks a `name` attribute so each segment is individually identifiable, then feeds them into RBD Constraints from Rules to generate surface-point-based hard constraints between adjacent pieces. Hard constraints are chosen over soft because the cables are stiff and need no plasticity. The guide simulation is then established by linking the cable RBD network to the...
- **File:** tutorials/week-02-03-starting-the-guided-sim-v1-1080p.md


### week 02   04   finishing the horizontal cable sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ykTr02tft_k
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rbd, simulation, dop, attributes, intermediate
- **Summary:** The instructor resolves a constraint-visibility issue caused by the guided sim removing intra-guide constraints by default, which is toggled off to restore correct cable connections. Guide strength is demonstrated by setting it to zero, causing all pieces to fall immediately and freely, showing how strength controls the blending between guided and free-simulated motion. The angular and linear...
- **File:** tutorials/week-02-04-finishing-the-horizontal-cable-sim-v1-1080p.md


### week 02   07   starting the vellum sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cecNdA8cLTo
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** vellum, simulation, dop, attributes, intermediate
- **Summary:** The instructor uses Vellum Configure Cloth (treated as a wire/cable) for the vertical cables. The key discovery is setting Rest Length Scale to 0.8 (below 1.0), which makes the constraints shorter than the actual geometry, placing the cables under tension from the first frame of the simulation — physically accurate for bridge suspension cables. Pin points are grouped and wired to the main...
- **File:** tutorials/week-02-07-starting-the-vellum-sim-v1-1080p.md


### week 02   08   setting the strong constraints and the breaking threshold v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9TNDsfFNoq4
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** vellum, simulation, dop, attributes, intermediate
- **Summary:** With a single test cable working, the Delete/Blast node isolating it is disabled so all cables enter the sim together. The instructor identifies that rear bridge cables should never detach (the rear section of the bridge remains intact), so those attach constraints are flagged as unbreakable using a geometry-based selection combined with a TimeShift to the last frame. A break threshold is then...
- **File:** tutorials/week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p.md


### week 04   06   cull by speed v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UFrvmv0rwQI
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** particles, pyro, attributes, vex, intermediate
- **Summary:** The instructor caches the POP sim result to disk and enables load-from-disk for fast flipbook playback. Particles are displayed as pixels or small points for viewport clarity. The core technique reads the `v` (velocity) attribute on each point, computes its length, and uses a threshold to delete slow-moving points so that only high-speed objects contribute to pyro emission sources. This...
- **File:** tutorials/week-04-06-cull-by-speed-v1-1080p.md


### w01   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RQBrvngXM6Y
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** rbd, simulation, dop, instancing, rendering, beginner
- **Summary:** The instructor introduces the tabletop course by describing the coffee bean shot goal. The week covers instancing bean geometry to scattered points, varying instance orientations and initial velocities, feeding the points into a Bullet dynamics network, and adding spin and gravity for realistic collisions. Post-simulation, retiming is used and the bean count is doubled without re-simulating....
- **File:** tutorials/w01-01-introduction-v1-1080p.md


### w02   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=C7vpFqAZClk
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** sop, attributes, procedural, animation, intermediate
- **Summary:** Instead of running a FLIP simulation for the yogurt, the instructor uses purely procedural SOP deformation to recreate the look of blueberries and chocolate falling into yogurt. Velocity attributes from the falling objects are sampled and used to displace the yogurt surface geometry. This approach avoids heavy fluid simulation entirely, making it extremely quick to iterate while still...
- **File:** tutorials/w02-01-introduction-v1-1080p.md


### w03   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yP83h4H-lgU
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** flip, simulation, dop, rendering, intermediate
- **Summary:** This is the course's first full FLIP simulation week. Three different fluid emitters each carry a different viscosity attribute value to mimic distinct food fluids (e.g. runny caramel vs. thick chocolate). The FLIP solver's viscosity features are central to achieving sticky, slow-flowing behaviour. The week takes the sim all the way through to Mantra/Arnold lighting, shading and rendering.
- **File:** tutorials/w03-01-introduction-v1-1080p.md


### w04   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=S4VjdIf5BKQ
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** flip, simulation, dop, rendering, intermediate
- **Summary:** This week introduces an animated FLIP fluid emitter (milk pour) combined with a separately animated strawberry collision object. The instructor highlights the use of viscosity and surface tension as critical parameters that give milk its characteristic behaviour — forming a crown splash with held droplets. The sim is meshed using VDB for a stable, flicker-free mesh, and rendered in Arnold with...
- **File:** tutorials/w04-01-introduction-v1-1080p.md


### w05   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AysHWEqNhwg
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** flip, rbd, simulation, dop, rendering, intermediate
- **Summary:** This final tabletop week uses a FLIP tank setup (contained fluid volume) rather than an emitter. Strawberries are first simulated with Bullet RBD to settle on a surface, then the packed geo is converted into a static collider for the FLIP solver. Splash shape is controlled by adjusting initial fluid velocity. Viscosity and surface tension are applied again. The week concludes with the full...
- **File:** tutorials/w05-01-intro-v1-1080p.md


### w02   05   deforming with velocity v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IuvtudgbzLw
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** sop, attributes, vex, animation, intermediate
- **Summary:** Starting from blueberry geometry with only position, normals and UVs, the instructor adds a velocity attribute using the Trail SOP set to "Compute Velocity" rather than its default trail mode. This `v` attribute is then used to drive positional displacement of the yogurt surface. The instructor also notes this is a standard technique for adding motion blur to animated geometry that lacks...
- **File:** tutorials/w02-05-deforming-with-velocity-v1-1080p.md


### w03   04   adding viscosity v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9N9CavpgoB4
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** flip, simulation, dop, attributes, intermediate
- **Summary:** Starting from a too-watery chocolate fluid, the instructor walks through the exact steps to add viscosity: first enabling it in the FLIP Solver, then navigating to the FLIP Object and setting a viscosity value (e.g. 100) in the Physical tab. The resulting sim shows visibly thicker, slower flow. The instructor previews the future step of importing per-point `viscosity` attribute from outside...
- **File:** tutorials/w03-04-adding-viscosity-v1-1080p.md


### w03   11   meshing v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H56dPbE3S2E
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** flip, volumes, sop, rendering, intermediate
- **Summary:** The instructor builds the particle-to-mesh pipeline from scratch, troubleshooting VDB from Particles settings (voxel size and radius scale) until a visible level set appears. VDB Smooth SDF is then applied to remove particle-level roughness. Convert VDB extracts a polygon mesh. The key insight is that tuning voxel size to a very small value (0.025) in combination with VDB smoothing produces a...
- **File:** tutorials/w03-11-meshing-v1-1080p.md


### w04   11   viscosity and surface tension v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1yb3mindncw
- **Author:** The VFX School Archive
- **Houdini Version:** Houdini 18
- **Tags:** flip, simulation, dop, attributes, intermediate
- **Summary:** Starting from a chaotic, formless splash, the instructor adds structured fluid behaviour by combining viscosity (light, for milk) and surface tension. The jitter seed on the FLIP Source is animated with `$F` so initial particle positions vary per frame, preventing grid patterns. A simple isolated DOP network is built to demonstrate the viscosity and surface tension interaction clearly. Surface...
- **File:** tutorials/w04-11-viscosity-and-surface-tension-v1-1080p.md

### Effective TD
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c9qw6hVstEA
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** hda, python, pyro, optimization, pipeline, td, ui, procedural, houdini-digital-assets
- **Summary:** Jesper (Houdini.School instructor) teaches a three-session TD-focused course centered on real-world pipeline thinking. The scenario: a TD receives a Pyro simulation file from an artist and must optimize it for caching/rendering, wrap it into a procedural HDA, and then add Python automation and improved UI for usability. Session 1 covers simulation data analysis and optimization; Session 2 covers HDA creation; Session 3 focuses on Python-driven UI and automation.
- **File:** tutorials/effective-td.md


### Effective TD (intro v1)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7NejsDXzxXI
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** hda, python, pipeline, td, ui
- **Summary:** A separately-recorded, shorter intro to the same Houdini.School Effective TD course. Jesper introduces himself and previews the curriculum: optimizing data for caching, wrapping the system into an HDA, and adding a Python-driven UI to control the optimization. Frames the course around data management/optimization rather than the Pyro-simulation/three-session structure described in the other Effective TD recording.
- **File:** tutorials/effective-td-7nejsdxzxxi.md


### Animate Gaussian Splats with Houdini - Free Tutorial + Scene Files
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=MqtMQl8DtjQ
- **Author:** SOP Cemetery
- **Houdini Version:** Houdini 21
- **Tags:** #kinefx #apex #rigging #animation #attributes #karma #rendering #advanced
- **Summary:** Rigs and animates a Gaussian-splat scan (a fly) via KineFX skeleton + Harmonic Capture + APEX rig, then re-deforms the original splat points with Gaussian Splat Deform (since direct skin-driven deformation fails to reorient splats), finally rendering in Karma XPU with no materials, just camera DoF/motion blur and a shadow-catcher plane.
- **File:** tutorials/animate-gaussian-splats-with-houdini---free-tutorial-scene-files.md


### Guest Tutorial: Creating realistic honey with FLIP
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5oHU1bmYKs0
- **Author:** Entagma (Philip Danger)
- **Houdini Version:** H18+
- **Tags:** flip, viscosity, fluid-sim, gas-field-vop, custom-vop, per-particle-viscosity, stickiness, honey, bubbles, octane, rendering, advanced
- **Summary:** Builds a realistic honey FLIP sim using per-particle velocity-based viscosity (fast particles = higher viscosity for folding; slow = lower for sliding/coating) plus noise variation for layered sheets. Custom Gas Field VOP adds attraction velocity toward the collision surface instead of vanilla blend-to-zero stick. Post-processing integrates Alvaro Moreira's meshing setup and Tom Taylor's bubble technique. Rendered in Octane with transmission + scatter medium.
- **File:** tutorials/guest-tutorial-creating-realistic-honey-with-flip.md


### How to make a Short Film in Houdini | Magnus Møller & Jesper Andkjær
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EPIdMwuMK-M
- **Author:** Houdini (official) — Magnus Møller & Jesper Andkjær, Studio Tumblehead
- **Houdini Version:** Houdini 20 / 20.5
- **Tags:** pipeline, production, short-film, usd, solaris, kinefx, apex, rigging, animation, compositing, copernicus, karma-xpu, hda, python, automation, lookdev, lighting, lpe-aov, hair-grooming, blendshapes, tumblehead, houdini-20, conference-talk, advanced
- **Summary:** SideFX HIVE conference talk — Studio Tumblehead's complete open-source Houdini pipeline "Stormelpipe" for their short film *Turbulence* (H20/20.5). Covers every department: modeling (NomadSculpt/ZBrush/QuilVR import), blendshapes (GoZ or in-Houdini SkullThings sculpt), LookDev (Karma + LookDev Studio HDA), tube-to-hair HDA, KineFX/APEX auto-rigger (one Python module builds APEX rig from tagged skeleton), layout with Import Asset HDA, animation with Build Shot HDA (USD sub-layer stacker) + transient constraints + global transform mode + bone jiggle + geometry noise HDAs, CFX/seat belt tricks (Scott node + Point Deform), LPE AOV lighting in Karma XPU, Copernicus compositing with auto-built comp tree (Tumblehead Build Comp HDA). Pipeline is free and open-source on GitHub. Project site: sidefx.com/tech-demos/turbulence.
- **File:** tutorials/how-to-make-a-short-film-in-houdini-magnus-møller-jesper-andkjær.md


### The Only HAIR GROOMING Tutorial You Need! (Houdini for Artists)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rVogGr7f0Cg
- **Author:** June Chevalier
- **Houdini Version:** Not specified (H20–H20.5 UI)
- **Tags:** sop, curves, attributes, procedural, vex, wrangler, modelling, beginner, intermediate
- **Summary:** An 85-minute beginner-friendly end-to-end hair grooming tutorial covering: mesh import + scale correction, density mask painting and mirroring, VDB collision setup, guide sculpting with the Draw tool, hair generation, and three realism layers — primary/secondary/tertiary clumping (including a VEX mask-invert trick for lower-section clumps), guide-process frizz noise, and stray/flyaway hairs via a random guide mask. Result: a realistic short men's hairstyle. Explicitly compared to and positioned as less buggy than Maya XGen.
- **File:** tutorials/the-only-hair-grooming-tutorial-you-need-houdini-for-artists.md


### Why you need to learn vex in Houdini #1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ntf3zMAez50
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/why-you-need-to-learn-vex-in-houdini-1.md


### Chocolate break rig and Liquid Stretch in Houdini Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=f5vt8n8CB-U
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson.md


### Houdini techniques to improve your level
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=zWlJ8QLkFH4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/houdini-techniques-to-improve-your-level.md


### Scissor Lift rig in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QPiEZM1o-ME
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/scissor-lift-rig-in-houdini.md


### Coin spin | Sops vs Vex vs OpenCL
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AGTOukqBmhU
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/coin-spin-sops-vs-vex-vs-opencl.md


### Essential Procedural Techniques in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JMfMxHi48Zs
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/essential-procedural-techniques-in-houdini.md


### Camera Match tool for Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NkVT9NtRMk0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/camera-match-tool-for-houdini-21.md


### Layered Textures in Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GQMsl6TiFXY
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/layered-textures-in-karma.md


### RBD Procedural Animations in Houdini | Mardini 2026
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ITq2EBJ5nIw
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/rbd-procedural-animations-in-houdini-mardini-2026.md


### Procedural Food in Houdini | Mardini 2026
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VjX9v92PJNU
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-food-in-houdini-mardini-2026.md


### Creating Cliff Shapes in Cops | Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=62Mo7udZM_o
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/creating-cliff-shapes-in-cops-free-lesson.md


### Volume rays in Cops for Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nCS6sy53_aw
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/volume-rays-in-cops-for-houdini-21.md


### Creating assets from default geometry in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oEIXFY-Kxdk
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/creating-assets-from-default-geometry-in-houdini-21.md


### Orient UVS like a PRO in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eqXFo0pxdXc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/orient-uvs-like-a-pro-in-houdini-21.md


### Basic Procedural Texturing with Cops in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AB9rwjcX0Xg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/basic-procedural-texturing-with-cops-in-houdini-21.md


### Roasting my Houdini Setups #1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rvDsbo3slXc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/roasting-my-houdini-setups-1.md


### Scatter shapes in cops randomly without overlap
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bTA8XwTEcRg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/scatter-shapes-in-cops-randomly-without-overlap.md


### Procedural Environments in Houdini | Patreon February '26 Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F_xggmIONZ4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-environments-in-houdini-patreon-february-26-free-lesson.md


### Direct vs Procedural in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Quj03TwHAN4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/direct-vs-procedural-in-houdini.md


### Think Procedural Think Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=TWQvmqhRX3M
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/think-procedural-think-houdini.md


### Double Sided Leaf Animation using Cops in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yeA_0tL3GlU
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/double-sided-leaf-animation-using-cops-in-houdini-21.md


### Matrix color transform in cops for Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZDlL81gmafE
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/matrix-color-transform-in-cops-for-houdini-21.md


### Procedural Duct Tape in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=D6449n2Pvcc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-duct-tape-in-houdini.md


### Tips and Tricks to level up your Houdini Skills
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DV0ABu_-yvc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/tips-and-tricks-to-level-up-your-houdini-skills.md


### Procedural Materials in Houdini 21 | Patreon December '25  - Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=iZwfnJGQUlI
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-materials-in-houdini-21-patreon-december-25---free-lesson.md


### Procedural environment assets in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SwtUCds8UCY
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-environment-assets-in-houdini-21.md


### CGI Integration | The Indie Way with Houdini(USD) and Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RchQ9K5QXtI
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/cgi-integration-the-indie-way-with-houdiniusd-and-nuke.md


### New Houdini Course  - Procedural Product Shots | Part 1 Free
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FxrSPbnI3tI
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/new-houdini-course---procedural-product-shots-part-1-free.md


### Tips and tricks in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gv_gXOSjCN0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/tips-and-tricks-in-houdini-21.md


### Optimizing Baked Trees with Instancing in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0C8ek1aDe8o
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/optimizing-baked-trees-with-instancing-in-houdini.md


### Bring your 3D renders to life with Houdini - Patreon October '25 Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=M8odmzpj2dc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/bring-your-3d-renders-to-life-with-houdini---patreon-october-25-trailer.md


### Handy Houdini Tips | Vellum, UVS, Modeling and More
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=h6wt3KJy2W4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/handy-houdini-tips-vellum-uvs-modeling-and-more.md


### Procedural Favela in Houdini  | Tips and Tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Nmnf_3mp1OU
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-favela-in-houdini-tips-and-tricks.md


### Heightfields and Cops workflow in Houdini 21 -  Patreon September 25 Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pbwra2esNqc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/heightfields-and-cops-workflow-in-houdini-21---patreon-september-25-trailer.md


### Houdini 21 | Opacity vs Stencil vs Geometry
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ha85low9Bmo
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/houdini-21-opacity-vs-stencil-vs-geometry.md


### Daily dose of Houdini Tips | Sweep secrets, opencl textures and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1QTfNMlvF1E
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more.md


### Dusty Bottles - Bridging procedural workflows in Houdini and Solaris
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=CHySFnWfKLk
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris.md


### Procedural Brick Wall with COPS  - Patreon August Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Eb4KIaOJT5Y
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-brick-wall-with-cops---patreon-august-trailer.md


### Making Trash in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KCy4Sw3nbcQ
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/making-trash-in-houdini.md


### Houdini tips to save the day
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lT0b8D6LmtM
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/houdini-tips-to-save-the-day.md


### No VEX challenge #1   Procedural Water Tower
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NxWpxFDaSJE
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/no-vex-challenge-1-procedural-water-tower.md


### Jellyfish Procedural Animation with Houdini and Vex | Patreon July Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=udPSR7Gjp9Y
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/jellyfish-procedural-animation-with-houdini-and-vex-patreon-july-trailer.md


### Procedural Boat in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=050av2q2ihg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-boat-in-houdini.md


### Quick object merge with Python in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fDV8SQegEDc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/quick-object-merge-with-python-in-houdini.md


### Vex Quick Tips #4 - Pineapple Crown
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oDXQsMo2aaQ
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/vex-quick-tips-4---pineapple-crown.md


### Interactive Tools with Houdini Python States | Draw pts on geo
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ARJFJC79k3k
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/interactive-tools-with-houdini-python-states-draw-pts-on-geo.md


### Creating a Procedural Rock Wall with Houdini | Patreon May - Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mljby-SKlUI
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/creating-a-procedural-rock-wall-with-houdini-patreon-may---trailer.md


### From sops to final render with Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O_oxVn-YVB0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/from-sops-to-final-render-with-karma.md


### Quick CG integration with Houdini and Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kxg05cfgdQI
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/quick-cg-integration-with-houdini-and-karma.md


### Procedural Buildings in Houdini | Tips and Tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JCdVrNwiMGk
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-buildings-in-houdini-tips-and-tricks.md


### Advanced Waterdrops Setup in Houdini | Patreon April Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2HYYRRW7tws
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/advanced-waterdrops-setup-in-houdini-patreon-april-trailer.md


### Texture Projection Tool for Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=t9ldXkD7oqA
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/texture-projection-tool-for-houdini-205.md


### Procedural Graffiti in Houdini and COPS #mardini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=suiPD-s1I9U
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-graffiti-in-houdini-and-cops-mardini.md


### Procedural UVS and Texturing in COPS | Patreon March Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-lVYE0LRu6w
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-uvs-and-texturing-in-cops-patreon-march-trailer.md


### Environments in Houdini | Part 5 - Solaris and rendering with Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=h6MN80ka4Vg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/environments-in-houdini-part-5---solaris-and-rendering-with-karma.md


### Vex quick tips #2 | Iterating over numbers
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7PHYAnZbTvM
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/vex-quick-tips-2-iterating-over-numbers.md


### Vex quick tips | Overhang look with channel ramps
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SHAgvzji9vM
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/vex-quick-tips-overhang-look-with-channel-ramps.md


### Procedural Modeling, Rigging and Animation with Houdini | Patreon February Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=08lvfWum09M
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-modeling-rigging-and-animation-with-houdini-patreon-february-trailer.md


### Procedural Modeling with VEX, VDB and Vellum
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8RIneeMCbAg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-modeling-with-vex-vdb-and-vellum.md


### Procedural Pizza in COPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mL2TkAB_Rqc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-pizza-in-cops.md


### Quick CGI Integration with Houdini and Solaris
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xm9d-Un3Hrg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/quick-cgi-integration-with-houdini-and-solaris.md


### Environments in Houdini | Part 4 - Vines, Rocks and Fog
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cXbdFwd3u9o
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/environments-in-houdini-part-4---vines-rocks-and-fog.md


### Building Tools in Houdini with vex and python | Flatten Loop
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=enW-PwgBWE4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/building-tools-in-houdini-with-vex-and-python-flatten-loop.md


### Environments in Houdini  | Part 3  - Vegetation with Simple Tree Tools
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FvM09fA0cKY
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/environments-in-houdini-part-3---vegetation-with-simple-tree-tools.md


### Environments in Houdini  | Part 2  - Stone Bridge
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kPtCgMWIBj4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/environments-in-houdini-part-2---stone-bridge.md


### Environments in Houdini | Part 1 -  Heightfields
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ER_W3w3SkGk
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/environments-in-houdini-part-1---heightfields.md


### Product Shot in Houdini and Solaris | Part 2 | Patreon December
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aaNiFlx6Vi0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/product-shot-in-houdini-and-solaris-part-2-patreon-december.md


### How to (not) bake brownies in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=R3ClxIiqxag
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/how-to-not-bake-brownies-in-houdini.md


### Houdini Mini Course  |  Cops, Vex and Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=24vjgnyZRTw
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/houdini-mini-course-cops-vex-and-karma.md


### Vex Problem Solving in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Fiw_NedtssQ
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/vex-problem-solving-in-houdini.md


### Product Shot in Houdini Part 1 | Patreon November
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Joe8Cu40_as
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/product-shot-in-houdini-part-1-patreon-november.md


### Wood Barrel Texturing in COPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O6T5eVYJHsA
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/wood-barrel-texturing-in-cops.md


### Beginner Procedural Modeling/UVS Tutorial in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-1kxDkdmcV4
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/beginner-procedural-modelinguvs-tutorial-in-houdini.md


### Spiral Splash Tutorial in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xz1oNZGq7P0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/spiral-splash-tutorial-in-houdini.md


### Tiling Patterns with COPS and SOPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=05uuRimyHfY
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/tiling-patterns-with-cops-and-sops.md


### Custom patterns with COPS |  October Patreon Exclusive
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bM7hzXqBq0Y
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/custom-patterns-with-cops-october-patreon-exclusive.md


### Procedural UV's In Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7ZJeWIFYSxg
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-uvs-in-houdini.md


### Enhance your renders in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c193tsyLH-0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/enhance-your-renders-in-houdini.md


### Houdini Beginner Tutorial | Creating a perfume bottle
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=conZuTxHnoc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/houdini-beginner-tutorial-creating-a-perfume-bottle.md


### Tips and Tricks for a better Houdini Time
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VL5N4jKidVA
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/tips-and-tricks-for-a-better-houdini-time.md


### Model and Rig a Wardrobe in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c_t8JwyHJrA
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/model-and-rig-a-wardrobe-in-houdini.md


### Cliff Face in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mcP3wLo1lIQ
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/cliff-face-in-houdini.md


### Resample Color Ramps in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=P-2FPlUJO60
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/resample-color-ramps-in-houdini.md


### Procedural Shading with COPS and Karma - Preview
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3bP9uKsn-9U
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-shading-with-cops-and-karma---preview.md


### UVW randomizer in karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1SXCz_Ta4Lc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/uvw-randomizer-in-karma.md


### VDB Procedural Modeling in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ag7I-FK4TF0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/vdb-procedural-modeling-in-houdini.md


### Procedural Helical Column in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HDIIwy11otU
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-helical-column-in-houdini.md


### Procedural Modeling with Houdini 20.5 Tools
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=k7-5PaOccYc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-modeling-with-houdini-205-tools.md


### Procedural Leaking Texture in Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8iK3GD3yeCE
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-leaking-texture-in-houdini-205.md


### Procedural tips and tricks in Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wgStaCuEglI
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/procedural-tips-and-tricks-in-houdini-205.md


### The Donut Tutorial in Cops | Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=meX4fLnITR0
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/the-donut-tutorial-in-cops-houdini-205.md


### Shoe Laces in Houdini | Vex and Vellum
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rlrWEjoO8jQ
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/shoe-laces-in-houdini-vex-and-vellum.md


### Designer like Materials in Cops | Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Lm5cG2XxRwU
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/designer-like-materials-in-cops-houdini-205.md


### Displacement maps in cops | Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xOeZncLWztc
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/displacement-maps-in-cops-houdini-205.md


### Useful Vex snippets | Houdini tips and tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_C6-g1C--ws
- **Author:** cgside
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/useful-vex-snippets-houdini-tips-and-tricks.md

---

## Tag Reference

### By Context
`#sop` `#dop` `#lop` `#cop` `#chop` `#top` `#vop` `#obj`

### By Technique
`#vex` `#python` `#hda` `#procedural` `#animation` `#rigging`
`#pyro` `#flip-fluid` `#rbd` `#vellum` `#cloth` `#grains` `#wire`
`#volumes` `#particles` `#crowd`
`#materials` `#shaders` `#displacement` `#uv`
`#rendering` `#karma` `#mantra` `#redshift` `#materialx`
`#solaris` `#usd` `#lighting` `#hdri`
`#compositing` `#cop2` `#color-management`
`#pdg` `#pipeline` `#hscript`

### By Subject
`#motion-design` `#vfx` `#product-viz` `#environment` `#character`
`#destruction` `#fire` `#smoke` `#liquid` `#cloth` `#abstract`
`#scattering` `#instancing` `#curves` `#terrain`

### By Level
`#beginner` `#intermediate` `#advanced` `#expert`

### By Houdini Version
`#h19` `#h20` `#h20-5` `#h21`

### By Source Type
`#book` `#youtube` `#article` `#sidefx-docs` `#masterclass`
