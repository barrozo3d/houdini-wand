# Houdini Wand — Tutorial & Knowledge Base Index

This is the skill's growing knowledge base. Every ingested tutorial, article, and book excerpt is listed here.

**To add a tutorial:** say "ingest this: [URL]" and the skill will fetch, structure, and add it here automatically.
**To add a book chapter:** paste the content and say "ingest this chapter from [Book Title]".
**To search:** look for tags matching the technique you need.

---

## How to Read This Index

```
### [Title]
- **Source:** YouTube / Article / Book
- **URL / Reference:** link or book citation
- **Author:** creator name
- **Houdini Version:** version shown
- **Tags:** #technique #context #level
- **Summary:** 2-3 sentence description
- **File:** tutorials/filename.md
```

---

## Entries

### Intro To Houdini for VFX - Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JbxNElzALrM
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #dop #vop #vex #attributes #particles #simulation #wrangler #procedural #beginner
- **Summary:** A 2-hour beginner course covering everything needed to start creating VFX in Houdini from zero. Progresses from UI navigation and basic SOP geometry through attributes, Attribute VOPs, VEX wrangles, and DOP simulation networks, ending with an overview of all major solver types (Pyro, FLIP, Vellum, RBD) and noise-driven per-frame deformation inside a SOP Solver.
- **File:** tutorials/intro-to-houdini-for-vfx---beginner-course.md


### Intro To Houdini Particles - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=94YAomHfMbw
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #dop #sop #vop #particles #simulation #attributes #wrangler #procedural #intermediate
- **Summary:** A 2-hour course on Houdini particle simulations covering the full DOP particle pipeline: popnet/popsource/popsolver setup, custom velocity via Geometry VOP, multiple sourcing types, attribute inheritance, interpolate source for animated geometry, and static/moving collisions. Emphasizes building proper VOP-based workflows over shelf presets.
- **File:** tutorials/intro-to-houdini-particles---full-beginner-course.md


### Intro To Houdini Volumes - Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wR0SDptfygg
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vop #volumes #simulation #procedural #vdb #intermediate
- **Summary:** A 2-hour course covering all core Houdini volume concepts: fog VDB vs SDF distance fields, Volume VOP for per-voxel manipulation with named bind/bind-export, scalar vs vector velocity fields, curve-based velocity volumes, and two methods for converting particle clouds to renderable volumes (vdbfromparticles vs volumerasterizeattributes).
- **File:** tutorials/intro-to-houdini-volumes---beginner-course.md


### Intro To Houdini Pyro - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=m8w2OND3rH0
- **Author:** Voxyde VFX
- **Houdini Version:** H20–H21 (Pyro Burst Source requires H20+; core workflow H18+)
- **Tags:** #pyro #fire #smoke #simulation #dop #vdb #sourcing #micro-solvers #collision #explosion #beginner
- **Summary:** 145-minute comprehensive Pyro beginner course. Covers all fields (density, velocity, temperature, divergence, flame), all Shape tab micro-solvers (turbulence, disturbance, shredding, wind, gas damp), collisions, resolution/OpenCL workflow, and efficient scatter-based sourcing with the Pyro Burst Source node for explosions.
- **File:** tutorials/intro-to-houdini-pyro---full-beginner-course.md


### Intro to VOPS - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Kx3CJJei_Vs
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #vop #sop #attributes #math #noise #procedural #beginner
- **Summary:** A 59-minute beginner tutorial covering core VOP math nodes used daily in Houdini VFX work: the `attribvop` and its variants, add/subtract/multiply, parameter promotion, displacement along normals (`displacealongn`), fit range remapping, ramp gradients, complement/negate for value inversion, and sine/cosine for cyclic procedural patterns.
- **File:** tutorials/intro-to-vops---houdini-beginner-tutorial.md


### VOPS 02 - Random & Noise - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mORz1y05T7E
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #vop #sop #noise #random #attributes #procedural #beginner
- **Summary:** A 46-minute beginner tutorial dedicated to noise and randomness in Houdini VOPs: the `random` VOP (uniform and Gaussian), `turbulentnoise`, `aanoise` (anti-aliased flow noise for directionless animation), `curlnoise` (fluid-like swirling with 4D simplex), `worleynoise` (cellular Voronoi patterns), and the `relbbox` (relative bounding box) VOP for object-space gradient masks.
- **File:** tutorials/vops-02---random-noise---houdini-beginner-tutorial.md


### VOPS 03 - Vector Operations - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oT6qzs-Vffk
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #vop #sop #vectors #math #attributes #procedural #beginner
- **Summary:** A 31-minute focused tutorial on vector math as used in VFX simulations: creating direction vectors via `subtract` + `normalize`, computing distances with `length`, cross product for perpendicular vectors, dot product for angle-based facing masks (-1 to 1), and the `reflect` VOP for bounce direction calculations — the mathematical foundation for controlling any simulation movement.
- **File:** tutorials/vops-03---vector-operations---houdini-beginner-tutorial.md


### VOPS 04 - Geometry Interactions - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qDtKmbCDn3k
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #vop #sop #attributes #geometry #procedural #beginner #intermediate
- **Summary:** A 44-minute tutorial on cross-geometry attribute transfer inside `attribvop`: six methods for making geometries communicate — `importpointattrib`, `nearpoint`, `findattribval`, `minpos`/`xyzdist`/`primuv` for primitive-based surfaces, `intersect` for ray-surface collision, and `pcopen`/`pcfilter` for radius-based point cloud queries. Essential for morphing effects and particle attraction to meshes.
- **File:** tutorials/vops-04---geometry-interactions---houdini-beginner-tutorial.md


### Intro To Houdini Solaris - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3BX97YIQERE
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #lop #solaris #usd #rendering #karma #lighting #materialx #instancing #beginner
- **Summary:** A 4.5-hour comprehensive Solaris beginner course covering the complete LOP workflow: USD scene graph, `sopimport`, Stage Manager, MaterialX Karma material authoring, `componentbuilder` for USD asset packaging, light types (Karma Physical Sky, area, dome), `karmafogbox` for volumetric lighting, `instancer` LOP for scattering millions of instances, and a complete magical forest shot built entirely in Houdini with Karma XPU render and AOVs.
- **File:** tutorials/intro-to-houdini-solaris---full-beginner-course.md


### Houdini Tutorial - Simple Disintegration FX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O2F1Qzl22oU
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #dop #vop #particles #attributes #vfx #destruction #intermediate
- **Summary:** A 21-minute tutorial building a geometry disintegration effect entirely in SOPs: `remesh` for uniform triangle density, a noise-driven `dissolve` attribute animated over time as a deletion threshold, `blast` SOP to progressively delete geometry, and a `popnet` with curl noise to emit and animate dust particles at the dissolve boundary — no complex DOP setup required.
- **File:** tutorials/houdini-tutorial---simple-disintegration-fx.md


### Houdini 21 Tutorial - MPM Snowball
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aQQeEOlHqjQ
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini 21
- **Tags:** #dop #sop #mpm #grains #simulation #vfx #rendering #karma #intermediate #h21
- **Summary:** A 50-minute Houdini 21 tutorial on the MPM (Material Point Method) solver for snow simulation: snowball source with layered `mountain` noise, MPM DOP setup with snow stiffness/cohesion/friction parameters, efficient `.bgeo.sc` disk caching via `filecache`, secondary particle spray simulation driven by high-velocity particle extraction, and full Karma XPU rendering and compositing with AOVs.
- **File:** tutorials/houdini-21-tutorial---mpm-snowball.md


### Houdini Solaris Tutorial - Rendering Multiple ROPS Together
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qg3OFz4JZs4
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #lop #solaris #rendering #karma #top #pipeline #beginner
- **Summary:** A quick 1.5-minute tip tutorial showing how to batch-render multiple Karma/Solaris ROP outputs (character, blast, particles, rain, water) simultaneously using a TOP network with `ropfetch` nodes — one per render element — with "node by node" cook order and frame batching to eliminate manual sequential rendering.
- **File:** tutorials/houdini-solaris-tutorial---rendering-multiple-rops-together.md


### Improve Solaris Performance - Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QfWUzrfsDaY
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #lop #solaris #usd #rendering #karma #performance #pipeline #intermediate
- **Summary:** A 23-minute practical tutorial covering strategies to keep the Houdini Solaris viewport fast: always bake simulations (RBD, Vellum, particles, animated characters) to `.bgeo.sc` or USD caches via `filecache` before `sopimport`, use the `instancer` LOP with pre-exported USD assets instead of live SOP instancing, and use `configurelayer` proxy geometry for viewport speed while keeping render-res for final output.
- **File:** tutorials/improve-solaris-performance---houdini-tutorial.md


### Houdini Tutorial - Wispy Smoke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RRmvyQu39-4
- **Author:** Voxyde VFX
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #dop #sop #pyro #smoke #volumes #vdb #simulation #vfx #intermediate
- **Summary:** A 27-minute tutorial on achieving a wispy cigarette/incense smoke aesthetic using the Houdini Pyro solver: starting from the `configure pyro` shelf preset with a small sphere emitter, tuning Density Dissipation, Buoyancy, Turbulence, Shredding, and Disturbance micro-solvers for thin tendrils instead of dense smoke, and applying a volume shader in Karma/Mantra for the final look.
- **File:** tutorials/houdini-tutorial---wispy-smoke.md


### Introduction to Particles in Houdini 21 [FULL Beginner Course 2026]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=041qemBc_1Q
- **Author:** Pixel In The Frame
- **Houdini Version:** 21
- **Tags:** #particles #dop #sop #vex #instancing #simulation #rendering #karma #lop #solaris #beginner #houdini-21
- **Summary:** 165-minute comprehensive beginner course covering every major POP node in H21: POP Source (scatter/all-points/location emission), all force nodes (Force, Wind, Drag, Axis Force, Curve Force, Attract, Interact, Advect by Volume), collisions (POP Collision Detect + Static Object with deforming geo), particle lifecycle (Color, Group, Awaken, Kill, Replicate), orient/spin, VEX inside POP VOP and POP Wrangle (curl noise on velocity), SOP-level instancing via Copy to Points, LOP-level USD instancing with Karma motion blur, and a final project combining RBD simulation with Pyro volume sourcing rendered in Karma.
- **File:** tutorials/introduction-to-particles-in-houdini-21-full-beginner-course-2026.md
- **File:** tutorials/introduction-to-particles-in-houdini-21-full-beginner-course-2026.md


### Houdini UV Unwrapping Fundamentals
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cguHzZ9L87g
- **Author:** Mat Sola
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #sop #modelling #uv #procedural #intermediate
- **Summary:** 65-minute comprehensive UV workflow: geometry prep, projection (`uvproject`), seam cutting via edge groups, flattening with `uvpeel`/`uvunwrap`, island packing with `uvlayout`, checkerboard visualization via `uvquickshade`, and export. Covers both hard-surface and organic models.
- **File:** tutorials/houdini-uv-unwrapping-fundamentals.md


### Model a Procedural Flower | Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pIp3cYSBZc4
- **Author:** Fifo
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #sop #dop #vop #vellum #modelling #procedural #curves #attributes #simulation #intermediate
- **Summary:** 38-minute tutorial building a fully procedural animated flower: curve-based stem with `resample`/`sweep`, blossom modeled with `blendshape` for open/closed states, phyllotaxis golden angle (137.518°) distribution via VOP cross product, `copytopoints` with time-offset pscale ramp for staged bloom, and Vellum cloth constraints to resolve petal intersections naturally.
- **File:** tutorials/model-a-procedural-flower-houdini-tutorial.md


### Houdini Tutorial | Creating Realistic Waterfall Simulation (Step-by-Step)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eYqxarTsOrE
- **Author:** VFX Grace
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #flip #dop #sop #simulation #volumes #vdb #rendering #advanced
- **Summary:** 151-minute comprehensive FLIP waterfall tutorial: reference analysis, velocity-sourced emitter, collision geometry, white water/foam solver with quality comparison, manual particle-to-mesh conversion, sub-mesh point cleanup, water shader, and full Karma/Mantra render + composite pipeline. Discusses FPS effect on water dynamics (60 FPS used).
- **File:** tutorials/houdini-tutorial-creating-realistic-waterfall-simulation-step-by-step.md


### Grain Vortex in Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8fcfu6gmzUQ
- **Author:** raphaël
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #dop #sop #rbd #simulation #instancing #procedural #intermediate
- **Summary:** 25-minute tutorial building a vortex grain animation with Megascans rocks: `polyreduce` proxy workflow for fast Bullet RBD sim, custom vortex force field, initial shape arrangement (smiley face), and high-poly copy-back post-sim for rendering.
- **File:** tutorials/grain-vortex-in-houdini-tutorial.md


### [Урок] Тяжелый Люкс. Часть 1. (Heavy Lux — Luxury Particle Effect, Part 1)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gsrHHeYadZ0
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #dop #sop #vex #particles #simulation #intermediate
- **Summary:** 29-minute Russian-language tutorial (Part 1) on building a dense luxury glitter/dust particle effect for brand advertising (Dior logo shown in final render). POP network with All Points emission from 10k-point grid, stable birth rate, wind velocity 6 with VEX mask control using `windgroupraw`, and Cd-based color variation.
- **File:** tutorials/урок-тяжелый-люкс-часть-1.md


### Houdini Tutorial: Make Any Geometry Knitted
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mTnQji8a8nw
- **Author:** PolygonCGI
- **Houdini Version:** Not specified (H20–H21 UI)
- **Tags:** #sop #vop #modelling #procedural #curves #attributes #rendering #redshift #advanced
- **Summary:** 27-minute advanced tutorial wrapping a procedural knit stitch pattern onto any geometry using a UV-space projection trick (`attribswap` P ↔ UV). Builds stitch tile from scratch, tiles it in 2D UV space via VEX, projects back to 3D surface, adds fiber variation with `curlnoise`/`sweep`, transfers texture color via `attribfrommap`, and renders with Redshift hair shader.
- **File:** tutorials/houdini-tutorial-make-any-geometry-knitted.md


### [Tutorial] Heavy Chic. Part 1.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fjVERoS2olY
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #dop #sop #vex #particles #simulation #intermediate
- **Summary:** 24-minute English tutorial (Part 1) building a "Heavy Chic" luxury particle effect for social media at 30 FPS. Key technique: `$F==1` expression in popsource locks count at exactly 100,000 particles. `popwind` velocity 6 + noise for uneven behavior. Produces falling silk curtain / rising crystal formations.
- **File:** tutorials/tutorial-heavy-chic-part-1.md


### [Tutorial] Heavy Chic. Part 2.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mOKs6Dht5Mw
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #dop #sop #vex #particles #simulation #rendering #intermediate
- **Summary:** 17-minute Part 2 refining the Heavy Chic sim: noise masked by `Cd` (stationary particles unaffected), B-spline gamma ramp on `Cd`, point separation 0.01→0.004 scaling count to 11M, `filecache` for disk playback, final golden luxury particle cloud render.
- **File:** tutorials/tutorial-heavy-chic-part-2.md


### [Урок] Тяжелый Люкс. Часть 2. (Heavy Lux Part 2 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UrDkzEXDdLM
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #dop #sop #vex #particles #simulation #rendering #intermediate
- **Summary:** 22-minute Russian-language Part 2 completing Heavy Lux: turbulent noise (freq 1.7, "Add to" blend), float-type B-spline ramp for sharper contrast, `filecache` with `$F4` frame naming, final luxury golden-fabric particle render.
- **File:** tutorials/урок-тяжелый-люкс-часть-2.md


### [Tutorial] Glass Tiles
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ps6ZOKEdDos
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #modelling #procedural #instancing #rendering #redshift #intermediate
- **Summary:** 25-minute tutorial building a procedural glass tile wall: single tile from `box` + `polyextrude` + `subdivide` (crease, 2 div) for glass-quality bevels, distributed on a 128×128 point grid via `copytopoints`, per-tile randomization, Redshift glass/refraction shader.
- **File:** tutorials/tutorial-glass-tiles.md


### [Урок] Стеклянная Плитка (Glass Tile — RU, Extended)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-s-AnXgjw-o
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #modelling #procedural #instancing #attributes #animation #rendering #redshift #intermediate
- **Summary:** 32-minute Russian-language extended Glass Tiles tutorial — same `box`/`polyextrude`/`subdivide`/`copytopoints` base, plus per-tile rotation animation via `attribtransfer` driving `orient` quaternion attribute. Produces animated wave of rotating glass tiles with glowing light-trail aesthetic.
- **File:** tutorials/урок-стеклянная-плитка.md


### [Урок] Мягкая Ткань (Soft Fabric/Weaving — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ju8pDlzR3vM
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vex #procedural #curves #attributes #modelling #intermediate
- **Summary:** 43-minute Russian-language tutorial building procedural woven fabric geometry purely in SOPs via VEX harmonic math (no Vellum). Z-axis line (2000 pts) → `resample`/`curveu` → `attribwrangle` applies `sin(curveu * freq)` to Y/X positions. Frequency ~100–200 creates fabric loops; parameters promoted as sliders.
- **File:** tutorials/урок-мягкая-ткань.md


### [Tutorial] Soft Weave
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ohj4ag8DZRo
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vex #procedural #curves #attributes #modelling #intermediate
- **Summary:** 36-minute English companion to "Мягкая Ткань" — procedural weave via VEX: Y=`sin(curveu*freq)`, X=`sin(curveu*freq/2)` (halved X frequency creates interlocking weave pattern, not parallel waves). ch() sliders for amplitude/frequency per axis. No simulation required.
- **File:** tutorials/tutorial-soft-weave.md


### [Урок] Губка (Sponge — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cQd2YXWiQ4k
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vop #vdb #procedural #volumes #modelling #rendering #intermediate
- **Summary:** 32-minute Russian-language tutorial recreating a sponge/foam effect (inspired by Max Shulgi on Instagram): box + noise displacement → `pointsfromvolume` interior scatter → `rest` attribute for coloring → `pscale` control. Final blue-teal wet sponge render with porous cavities.
- **File:** tutorials/урок-губка.md


### [Tutorial] Purple Sponge
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O5cFGKp0n_A
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #dop #vdb #volumes #vellum #particles #simulation #rendering #intermediate
- **Summary:** 29-minute English sponge tutorial: box → `vdbfrompolygons` + `cloudnoise` → `pointsfromvolume` (400k pts, sep 0.07, pscale 0.5) → noise wrangle (freq 15, amp 0.05) → Vellum Grains sim; pscale copied from source to fix grain size.
- **File:** tutorials/tutorial-purple-sponge.md


### [Урок] Стеклянный Пончик (Glass Donut — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HkMJWwyqo-I
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vop #modelling #animation #rendering #redshift #intermediate
- **Summary:** 13-minute Russian glass donut: torus + `aanoise` flow noise animated 0→1 over frames 1–299 for seamless loop (not 300 to avoid duplicate frame). `polyextrude` thickness 0.05, Redshift glass shader. Key: flow parameter enables perfect noise cycle.
- **File:** tutorials/урок-стеклянный-пончик.md


### [Tutorial] Glass Donut
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=j5Ew_6-W8DE
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vop #modelling #animation #rendering #redshift #intermediate
- **Summary:** 13-minute English companion to Glass Donut RU — same aanoise flow loop technique; see [[урок-стеклянный-пончик]] for full extraction.
- **File:** tutorials/tutorial-glass-donut.md


### [Урок] Розовые Пузыри. Часть 1. (Pink Bubbles Part 1 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=alOGxWIIwTk
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vop #vdb #particles #instancing #simulation #procedural #intermediate
- **Summary:** 30-minute Russian Part 1 building pink bubbles inside a large sphere. Sphere → `vdbfrompolygons` → scatter 65 pts → noise-varied pscale → `peak` along normals by pscale (each bubble sits on inner surface at its own radius). Two-stream: inner bubbles + surface wave (Part 2).
- **File:** tutorials/урок-розовые-пузыри-часть-1.md


### [Tutorial] Pink Bubble. Part 1.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ypJL4PXxQpg
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #vop #vdb #particles #instancing #simulation #procedural #rendering #intermediate
- **Summary:** 25-minute English companion to Pink Bubbles Pt1 RU: sphere (scale 2, freq 64) → `peak` → fog VDB → scatter 65 pts → `pscale` 0.1 → `attribadjust` noise multiply (offset 1.3) for size variation. Two branches: scatter + ripple surface. Octane render.
- **File:** tutorials/tutorial-pink-bubble-part-1.md


### [Урок] Розовые Пузыри. Часть 2. (Pink Bubbles Part 2 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=faWPP0UPcU0
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #rendering #intermediate
- **Summary:** 15-minute Russian Part 2 — Octane render/material for pink bubbles: export elements, `subdivide` with "roll" (not crease), Octane camera + 3 shaders (Ground/Bubble/Bubble Main), circular light (required — no light = black render), position ~(5,5.6,5).
- **File:** tutorials/урок-розовые-пузыри-часть-2.md


### [Tutorial] Pink Bubble. Part 2.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uztbmUElafA
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #rendering #intermediate
- **Summary:** 10-minute English companion to Pink Bubbles Part 2 RU — Octane render/material setup; see [[урок-розовые-пузыри-часть-2]] for full details.
- **File:** tutorials/tutorial-pink-bubble-part-2.md


### [Урок] Помада. Часть 1. Моделирование (Lipstick Pt1 Modeling — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fMNkSvAwIFk
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #modelling #procedural #intermediate
- **Summary:** 15-minute Russian product modeling (Part 1): lipstick profile curve → `revolve` (8–12 div) → `subdivide` → `fuse` → rotated `box` boolean for angled top cut (~5–6°) → `trace` SOP for brand logo from texture.
- **File:** tutorials/урок-помада-часть-1-моделирование.md


### [Tutorial] Lipstick. Part 1. Modeling
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Zqle_HOS7Jg
- **Author:** Alexander Eskin
- **Houdini Version:** Not specified (H19–H21 UI)
- **Tags:** #sop #modelling #procedural #intermediate
- **Summary:** 18-minute English companion to Lipstick Pt1 RU — same revolve/subdivide/boolean workflow; see [[урок-помада-часть-1-моделирование]] for full extraction.
- **File:** tutorials/tutorial-lipstick-part-1-modeling.md


### [Урок] Помада. Часть 2. Flip Sim
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H17o8w-CFUM
- **Author:** Alexander Eskin
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/урок-помада-часть-2-flip-sim.md

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
