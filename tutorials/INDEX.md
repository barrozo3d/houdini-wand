# Houdini Wand — Tutorial & Knowledge Base Index

This is the skill's growing knowledge base. Every ingested tutorial, article, and book excerpt is listed here.

**To add a tutorial:** say "ingest this: [URL]" and the skill will fetch, structure, and add it here automatically.
**To add a book chapter:** paste the content and say "ingest this chapter from [Book Title]".
**To search:** look for tags matching the technique you need.


### Intro to Crowds | SideFX
- **Source:** Article
- **URL:** https://www.sidefx.com/tutorials/intro-to-crowds/
- **Author:** Luca Pataracchia (SideFX)
- **Houdini Version:** H18 (course base; core concepts stable across later versions)
- **Tags:** crowd, dop, sop, chop, animation, rigging, simulation, vellum, rbd, usd, python, vex, procedural, beginner, intermediate, houdini-18
- **Summary:** Official SideFX beginner course (9 chapters, ~7h) covering the full Crowds pipeline: in-place vs. locomotion animation clips, DOP crowd solver setup, CHOPs for clip channels, the Transition Graph + Ragdoll FX, USD and FBX interoperability, the full built-in Trigger catalog plus custom VEXpressions, pre/post-sim art direction (pruning, combining sims, resimulating specific agents), a VEX Follow Path sub-pipeline, and H18 Transitions/Blendshapes. Text-only ingest (chapters are private Vimeo embeds, no transcript available) — the library's first real Crowd-context reference.
- **File:** tutorials/intro-to-crowds-sidefx.md


### Create Cinematic Oceans FAST | Realistic Shading & Render with Karma XPU | SideFX
- **Source:** Article
- **URL:** https://www.sidefx.com/tutorials/create-cinematic-oceans-fast-in-houdini-realistic-shading-render-with-karma-xpu/
- **Author:** Mario Leone (NodeFlow)
- **Houdini Version:** Houdini 20.5
- **Tags:** ocean, whitewater, solaris, lop, karma, rendering, materialx, procedural, beginner, houdini-20
- **Summary:** Builds a spectral (non-simulated) ocean via Ocean Spectrum + Ocean Evaluate in OBJ, fixes visible tiling with a wave-instancing trick (sparse point cloud feeding the Wave Instancing tab), caches to disk, then assembles in Solaris: floor + Quick Surface Material, camera/Karma XPU render settings set up before the Houdini Ocean Procedural LOP (required for its frustum-based adaptive subdivision), Karma Physical Sky lighting, and a hand-tuned wave/foam Diffuse-Specular-Transmission shading pass. Fills the "Ocean spectrum / whitewater FX" library gap.
- **File:** tutorials/create-cinematic-oceans-fast-realistic-shading-render-with-karma-xpu-sidefx.md


### Muscles and tissue
- **Source:** Article
- **URL:** https://www.sidefx.com/docs/houdini/muscles/index.html
- **Author:** SideFX (official documentation)
- **Houdini Version:** Houdini 22.0 (Otis system); Legacy Vellum muscles/tissue also documented
- **Tags:** muscles, tissue, otis, vellum, sop, dop, simulation, rigging, animation, character, procedural, advanced, houdini-22
- **Summary:** H22's Otis Muscle and Tissue System (VBD-based, single unified sim pass for muscles/bones/tissue-core-fascia/tissue-shell-fat, replacing the older multi-pass Vellum muscle workflow — not parameter-compatible with it). Full node chain: Muscle ID → Muscle Solidify (tetrahedralize) → Fiber Groom → Muscle Properties/Constraint Properties Otis → Muscle Mirror → Auto Tension Lines + Activate → Muscle Flex → Otis Configure Muscle and Tissue → Otis Solver (GPU; Substeps≈40@24fps, Iterations≈10) → skin post-processing. Six constraint types (muscle ends, muscle glue, rigid points, tissue-to-bone, tissue-to-muscle). Fills the "true muscle simulation" library gap (previously only Vellum rest-blend faking).
- **File:** tutorials/muscles-and-tissue.md


### Procedural City 1 : Building Generator | SideFX
- **Source:** Article
- **URL:** https://www.sidefx.com/tutorials/procedural-city-1-building-generator/
- **Author:** Hossam Aldin Alaliwi
- **Houdini Version:** Houdini 18.5
- **Tags:** procedural, modelling, uv, materials, pdg, mantra, redshift, instancing, beginner, intermediate, advanced, houdini-18
- **Summary:** Paid 65-lesson (18+ hour) marketplace course, Vol. 1 of a two-part Procedural City series. Builds a rules-based generator that converts box massing into detailed buildings — deciding window/balcony placement, generating procedural UVs, importing/manipulating Quixel Megascans materials, building a PDG network for variation, and rendering tests in Mantra/Redshift. Source is a paywalled marketplace listing (not free instructional content) — notes are reconstructed from the course's own description only; no exact node graph is verifiable. Fills the "procedural city/building generation" gap at an overview level.
- **File:** tutorials/procedural-city-1-building-generator-sidefx.md


### Getting Started with Houdini Engine for Unity | SideFX
- **Source:** Article
- **URL:** https://www.sidefx.com/tutorials/getting-started-with-houdini-engine-for-unity/
- **Author:** Simon Verstraete (SideFX)
- **Houdini Version:** Houdini 19
- **Tags:** hda, unity, houdini-engine, procedural, python, beginner, houdini-19
- **Summary:** Recorded Unity Live Session introducing the Houdini Engine for Unity plug-in: installing the plug-in, importing an HDA as a native Unity asset with live-editable exposed parameters (re-cooks in-editor without Houdini open), and authoring your own HDAs designed for Unity consumption. Text-only ingest (no accessible transcript/video) — session-scope summary rather than a node-by-node walkthrough. Fills the "Houdini Engine → Unity" gap (Unreal side already has ~8 tutorials + a recipe; Unity had zero).
- **File:** tutorials/getting-started-with-houdini-engine-for-unity-sidefx.md


### Free Houdini Tutorial: Machine Learning with ONNX in Houdini 20
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aCAatiY53s8
- **Author:** Entagma
- **Houdini Version:** Houdini 20
- **Tags:** python, sop, cop, vex, machine-learning, onnx, procedural, attributes, intermediate, houdini-20
- **Summary:** Explains and demonstrates H20's new ONNX Inference SOP (first official ML node, inference-only, no Python/training needed) via 3 worked examples: MNIST digit classification (direct point-attribute mapping), Mosaic style transfer (requires restructuring `Cd` into channel-planar R/G/B blocks via 3 Point Wrangles since ONNX expects all-red-then-all-green-then-all-blue, not interleaved RGB), and MiDaS depth estimation (single float output used to displace geometry into a depth map). Covers Setup Shapes from Model, Labs Attribute Normalize Float for un-normalized ML output, and discusses current limits (can't yet replace full multi-stage pipelines like Stable Diffusion, only their neural-net sub-stages). Fills the "ML SOPs / ONNX" library gap.
- **File:** tutorials/free-houdini-tutorial-machine-learning-with-onnx-in-houdini-20.md


### New in Houdini 22: Training Gaussian Splats from Infrared Photos
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yGCjD0_TIpw
- **Author:** Entagma
- **Houdini Version:** 22.0.368
- **Tags:** gaussian-splats, photogrammetry, colmap, top, solaris, usd, karma, rendering, advanced, houdini-22
- **Summary:** Quick-start pipeline for training a native Gaussian splat in H22 from real infrared-camera photos: shoot ~100-200 parallax-moved photos, run them through free/open-source COLMAP (feature extraction (OpenCV, shared) → exhaustive feature matching → reconstruction → sparse export) to get camera poses + a sparse point cloud, then in Houdini's TOP context build an `ML Train GSplat` node pointed at a manually-created `dataset.gsplats/{images,sparse/0}` folder structure. Key settings: Dataset Type = SfM (COLMAP), VRAM-fitting Data Downscale Factor, Cache Images to VRAM (minutes vs hours), Workers = CPU−1, Testing disabled for speed. Cook to train (default 30k steps, live browser monitor via Monitoring → Open Viewer), Stop & Save the `.ply`, then import via File → GSplat SOP → Transform → Blast cleanup → Solaris Sub-Import → Karma (low samples, Pixel Oracle = Uniform) to render.
- **File:** tutorials/new-in-houdini-22-training-gaussian-splats-from-infrared-photos.md


### APEX in Houdini: Evolving Animation Workflows for Production | Mattéo Martinez | Paris HUG 2026
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fhgP_W-OvUE
- **Author:** Houdini
- **Houdini Version:** H21/H22 (referenced)
- **Tags:** apex, rigging, animation, kinefx, python, procedural, hda, advanced, expert, houdini-21, houdini-22
- **Summary:** Conference talk (Paris HUG 2026) making the production case for APEX: caching a full multi-character ragdoll animation scene as a ~745x-smaller-than-Alembic APEX cache; scripting auto-rig components with Apex Script vs. hand-wiring; visual Auto-Rig Builder drag-and-drop; procedural skinning via convex-hull capture transfer; custom CFX tools for cloth art-direction and proxy animation baking; bridging VEX/SOP/OpenCL into APEX graphs; ONNX-based wrinkle ML. Advanced/Expert; not a step-by-step build tutorial.
- **File:** tutorials/apex-in-houdini-evolving-animation-workflows-for-production-matteo-martinez-pari.md


### MPM | H20.5 Masterclass
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0jJXTHjLW8g
- **Author:** Houdini
- **Houdini Version:** H20.5
- **Tags:** dop, vex, simulation, volumes, procedural, attributes, rendering, karma, solaris, advanced, expert, houdini-20
- **Summary:** Official SideFX masterclass (194 min) by Alexandre Sirois-Vigneux covering the new MPM solver: theory (deformation gradient F/Fe/Fp, jp/ge, CFL + Material Condition sub-stepping), the full node ecosystem (MPM Source/Collider/Container/Solver), and 8 full example scenes (Avalanche, Rally Drift, Ship Breach, Fruit Smash, Ice Cream Scoop, Hubble Explosion, Building Collapse) end-to-end from sim to SDF meshing to secondary emission to Karma XPU render, plus a troubleshooting/tips section (thin-collider particle-level collisions, pin constraints, sand cohesion, performance tuning).
- **File:** tutorials/mpm-h205-masterclass.md


### New Houdini 20.5 Feature: Mastering the MPM Snow Solver! ❄️
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=m2c8V94OIX8
- **Author:** FaddyVFX
- **Houdini Version:** H20.5
- **Tags:** dop, simulation, volumes, attributes, procedural, intermediate, houdini-20
- **Summary:** Short (8m46s) practical companion video sweeping each MPM Source "Chunky" (snow) preset parameter one at a time — Density, Critical Compression, Critical Stretch, Compression Hardening, Stiffness, Volume Preservation — on a simple snow-log-drop test scene, showing visually how each affects whether the material holds together or crumbles, and confirming that high stiffness drastically increases OpenCL substep count/solve time.
- **File:** tutorials/new-houdini-205-feature-mastering-the-mpm-snow-solver.md


### H21 MPM Overview
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nD183jP3H4Y
- **Author:** Houdini
- **Houdini Version:** H21
- **Tags:** dop, simulation, volumes, advanced, houdini-21
- **Summary:** Outline/trailer episode (3m28s) for the MPM H21 Masterclass series, previewing new H21 MPM features (surface tension, auto-sleep, continuous emission expansion, per-voxel varying friction/stickiness, improved deforming colliders) and 4 new post-simulation nodes (MPM Surface, MPM Debris Source, MPM Post-Fracture, MPM Deform Pieces) that enable a bullet-style fracture/retarget workflow driven by MPM. No hands-on building in this episode; assumes H20.5 MPM Masterclass knowledge.
- **File:** tutorials/h21-mpm-overview.md


### APEX Rigging | H20 MASTERCLASS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-0KbPtoP5MU
- **Author:** Houdini
- **Houdini Version:** H20
- **Tags:** apex, rigging, kinefx, python, procedural, hda, wrangler, animation, advanced, expert, houdini-20
- **Summary:** William Harley (SideFX) masterclass (71m35s) on APEX rigging via Components and Subgraphs. Builds a simple tube FK rig from scratch (auto-wiring controls to joints with a hand-authored Find Nodes/For Each/Find-and-Connect component), a reusable Squash & Stretch subgraph tool saved as a tab-searchable .pgeo, then walks a full production chicken rig: pole-vector auto-IK legs, a reusable Look-At component, twist/toe tricks, a blend-shape-driven Face Pose Blend system, Abstract-Control-driven IK/FK blending, Configure Control Shapes, materials, and export via Apex Scene Animate/Invoke to .bgeo.
- **File:** tutorials/apex-rigging-h20-masterclass.md



### Rig Builder | Project Overview
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VFF2TLfbU3A
- **Author:** Houdini
- **Houdini Version:** H21
- **Tags:** sop, cop, procedural, modelling, texturing, rigging, kinefx, animation, beginner, intermediate, houdini-21
- **Summary:** Max Rose (SideFX) tours the Houdini 21 "iBot" character project (a spherical-eyeball robot) that the Rig Builder Series is built around: fully-procedural modeling (build-once/propagate for symmetric parts), geometry processing (color/naming), UDIM UV layout, COP2 texturing (with a noted UDIM-switching workflow limitation), and skeleton creation/assembly/capture, ending in an FBX export that becomes the import source for the series' first hands-on Rig Builder episode.
- **File:** tutorials/rig-builder-project-overview.md


### Houdini 20 | How to Pose and Animate Electra
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=q6GE9WmZKeI
- **Author:** Houdini
- **Houdini Version:** H20
- **Tags:** apex, kinefx, animation, rigging, beginner, houdini-20
- **Summary:** Official SideFX beginner animator lesson (16m24s) posing/keyframing the "Electra" character via its embedded APEX rig using Apex Scene Animate (contrasted with old FK-only KineFX Rig Pose), covering Selection Sets (grouping controls, Ctrl+Shift group-rotation around a primary/COG control, importing sets shared by other animators), adding a second character via Apex Character + Apex Scene Add Character, keyframing both together across frames 10/75, and extracting the result with Apex Scene Invoke.
- **File:** tutorials/houdini-20-how-to-pose-and-animate-electra.md


### Forgotten Metal Knowledge | Vray, Cycles, Arnold..
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uz8PIi3ELJg
- **Author:** Lucas
- **Houdini Version:** N/A (Blender/Cycles content)
- **Tags:** rendering, advanced
- **Summary:** NOTE: demonstrated entirely in Blender/Cycles, not Houdini — kept as a materials-theory reference. Renderer-agnostic PBR research on why real metal shows a "reflection tail-off" (sharp core + soft halo) from microscopic scratch density/roughness variation, and how to recreate it by stacking multiple BSDF layers of increasing roughness/decreasing presence rather than one roughness value. Compares this multi-layer approach against Clearcoat (cheap but distorts base material/isn't properly metallic) and GGX Tailoff control (near-free but limited/engine-dependent). Portable to Houdini via layered `mtlxstandard_surface`/`mtlxmix` MaterialX networks in Karma; see `references/render-pipeline.md`.
- **File:** tutorials/forgotten-metal-knowledge-vray-cycles-arnold.md


### Create Seamless Textures with Adjacency Nodes and Simulations | Houdini 22
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XKpfGoQVvQY
- **Author:** Inside The Mind
- **Houdini Version:** H22
- **Tags:** cop, procedural, attributes, simulation, texturing, intermediate, houdini-22
- **Summary:** Feature demo (9m17s) of Houdini 22's new Copernicus Adjacency nodes (Geometry to Adjacency + Attribute Sample with Adjacency), which rasterize mesh attributes/3D noise with zero UV seams — replacing the old H21 Rasterize Geometry + Fractal Noise 3D workflow. Also covers curvature-driven texturing via a SOP Measure node, a material-attribute gotcha blocking the COPs 3D preview, and adjacency-enabled simulation nodes (Reaction-Diffusion block, new Ripple solver) vs. not-yet-enabled ones (Flow block).
- **File:** tutorials/create-seamless-textures-with-adjacency-nodes-and-simulations-houdini-22.md


### New Time Nodes in COPs | Houdini 22
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ewNpXaxZI6w
- **Author:** Inside The Mind
- **Houdini Version:** H22
- **Tags:** cop, time, retiming, looping, flipbook, simulation, intermediate, houdini-22
- **Summary:** Walkthrough of H22's four new Copernicus time nodes — Time Blend (hold first/last frames), Time Loop (cycle/zigzag/blend loop types), Time Shift (absolute/by-time/relative/custom retiming), and Time Pack + Cable Unpack (multi-frame sampling into color0..N planes, likely for Denoise AI-style temporal nodes) — plus the beta Copernicus auto-unload setting for freeing VRAM.
- **File:** tutorials/new-time-nodes-in-cops-houdini-22.md


### Houdini 22 | How to Render Terrains in Solaris | Height Fields from COPs to LOPs
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IeVvQt0bHQ0
- **Author:** Houdini
- **Houdini Version:** H22
- **Tags:** cop, lop, solaris, karma, rendering, usd, volumes, intermediate, houdini-22
- **Summary:** Official SideFX how-to (18m3s): take a COPs-authored heightfield to a final Karma XPU render in Solaris. COPnet-level resolution switching (2K work / 4K final), `Convert HeightField` volume→polygon conversion, Use External COP output pinning, exporting `HeightField Erode` debris/sediment/flow fields via `Cable Pack` (Fields From Inputs) as geometry attributes for render masks, Scene Import → Karma Physical Sky with Atmosphere dome mode (Rayleigh scale + scatter distribution 6.25 for haze), real-world scale fix via Transform LOP (All Mesh Primitives), Quick Surface Material roughness 0.75, snapshot-strip 2K/4K comparison, and H22's new Image Filters on Karma Render Settings (chromatic aberration, vignette, ACES Filmic tone map).
- **File:** tutorials/houdini-22-how-to-render-terrains-in-solaris-height-fields-from-cops-to-lops.md


### Morph Anything with VDBs in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QUnkozOK4Ro
- **Author:** Voxyde VFX
- **Houdini Version:** H22 (Indie 22.0; technique version-agnostic)
- **Tags:** vdb, sdf, volumes, vop, sop, cop, solaris, karma, compositing, animation, intermediate, houdini-22
- **Summary:** Voxyde VFX production technique (23m23s): reveal a shoe-sole tread pattern by morphing between two SDFs instead of deforming geometry (no topology matching or self-intersections). Pipeline: isolate + PolyFill the sole → pattern SDF via `VDB from Polygons` (final voxel 0.005) and smooth SDF via Reshape(Dilate)→Smooth→Reshape(Erode) → match voxel sizes with `VDB Resample` + expand bands with `VDB Activate SDF` (needed for push/erode) → `Volume VOP` blending via `Volume Sample`+`Mix` driven by an animated relative-bbox gradient mask (promoted Animate/Width params + simplex turbulent noise) with a 0→1→0 ramp × Push (-0.02) SDF dilation ridge as leading edge → `Convert VDB` for render. Includes Solaris walkthrough (COPs diamond tread texture via Feather + Shape Scatter, 4-light rim rig) and a Nuke comp segment building the final dark-green look from reflection/rim AOVs with comp-side bokeh DOF.
- **File:** tutorials/morph-anything-with-vdbs-in-houdini.md


### Summon VFX | 3 | Set the Character & Cloth
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bh9PRfO-ebk
- **Author:** Houdini
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/summon-vfx-3-set-the-character-cloth.md


### Abstract liquid in Houdini  |  Part 01 - Building the simulation
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pFvA23fP5I8
- **Author:** Kotov Roman
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/abstract-liquid-in-houdini-part-01---building-the-simulation.md


### Abstract liquid in Houdini | Part 02 - Look Development
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=axBNpCzJuPY
- **Author:** Kotov Roman
- **Houdini Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/abstract-liquid-in-houdini-part-02---look-development.md

---

## How to Read This Index

```

### Intro To Houdini for VFX - Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JbxNElzALrM
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini (any modern, H18+)
- **Tags:** beginner, fundamentals, attributes, vops, vex, dops, solvers, pop, simulation, navigation, beginner
- **Summary:** Voxyde VFX comprehensive beginner course (120m8s, 19 sections). Teaches Houdini from absolute zero: UI orientation (only need scene view, OBJ window, parameter window), context networks (OBJ→geometry→DOPs levels), node operations (Tab menu, display/bypass/template flags, wire cutting with Y), operator types (SOPs/VOPs/DOPs). Deep section on attributes: class (point is king; primitive for poly...
- **File:** tutorials/intro-to-houdini-for-vfx---beginner-course.md


### Intro To Houdini Particles - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=94YAomHfMbw
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini (any modern, H18+)
- **Tags:** particles, pop, beginner, geometry-vop, velocity, sourcing, collisions, curl-noise, intermediate
- **Summary:** Voxyde VFX full beginner particle course (122m30s, 8 sections). Establishes the core principle: Geometry VOP inside the DOPs network (same as Attribute VOP at SOPs but runs every frame) trumps all pre-built POP nodes for real-world control. Covers: particle basics (POP Network, source, color, life), Geometry VOP workflow (velocity vs. force, goal-seek with subtract+normalize, tornado with...
- **File:** tutorials/intro-to-houdini-particles---full-beginner-course.md


### Intro To Houdini Volumes - Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wR0SDptfygg
- **Author:** Voxyde VFX
- **Houdini Version:** any modern (H18+)
- **Tags:** volumes, vdb, sdf, velocity-field, vop, point-cloud, volume-rasterize, beginner-intermediate
- **Summary:** Voxyde VFX comprehensive volumes beginner course (137m16s, 15 sections). Covers voxel math and resolution control (by-size mode, 0.1 = 10 voxels per unit), VDB sparse grids vs standard, SDF (signed distance field — positive outside, negative inside), Volume VOP internals (position = voxel center; bind/bind export; density vs field name), practical fog VOP examples (gradient fade via bounding...
- **File:** tutorials/intro-to-houdini-volumes---beginner-course.md


### Intro To Houdini Pyro - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=m8w2OND3rH0
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini (any modern, H19+)
- **Tags:** pyro, fire, smoke, beginner, sourcing, micro-solvers, velocity-field, divergence, temperature, flame, collisions, intermediate
- **Summary:** Voxyde VFX comprehensive pyro beginner course (145m31s, 15 sections). Covers the full pyro pipeline from zero: basic setup (pyro solver, fog VDB source, sourcing tab), velocity field sourcing (VDB container + Volume VOP curl noise), all 5 target fields (density/temperature/divergence/flame/velocity) with operation types (add/maximum/pool/copy), all shape micro-solvers (buoyancy, turbulence,...
- **File:** tutorials/intro-to-houdini-pyro---full-beginner-course.md


### Intro to VOPS - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Kx3CJJei_Vs
- **Author:** Voxyde VFX
- **Houdini Version:** any modern (H18+)
- **Tags:** vops, attribute-vop, math, noise, ramp, fit-range, bind, beginner
- **Summary:** Part 1 of a VOP series. Covers the full spectrum of foundational VOP nodes used in production VFX: vector/float types, all basic math ops (add/subtract/multiply/divide with constant shortcuts), parameter promotion, bind/bind export for attribute I/O, import point attribute for cross-geometry lookups, mix/blend, turbulent noise + displace-along-normal, fit range, ramp parameter (spline and...
- **File:** tutorials/intro-to-vops---houdini-beginner-tutorial.md


### VOPS 02 - Random & Noise - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mORz1y05T7E
- **Author:** Voxyde VFX
- **Houdini Version:** H19+
- **Tags:** vops, noise, random, vex, particles, simulation, turbulent-noise, curl-noise, worley-noise, flow-noise, bounding-box, beginner
- **Summary:** 45m51s beginner VOPs tutorial by Voxyde VFX (Part 2 of VOPs series). Covers 6 major topics:  1. **Random & Gaussian Random** — Random node with ptnum seed; 1D float and 3D vector outputs; Fit Range for negative-to-positive; Gaussian Random for direct negative values / true random vector. 2. **Turbulent Noise** — Noise types (alligator default, simplex preferred, sparse convolution for...
- **File:** tutorials/vops-02---random-noise---houdini-beginner-tutorial.md


### VOPS 03 - Vector Operations - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oT6qzs-Vffk
- **Author:** Voxyde VFX
- **Houdini Version:** H19+
- **Tags:** vops, vectors, cross-product, dot-product, normalize, particles, simulation, beginner-intermediate
- **Summary:** 31m12s VOPs Part 3 by Voxyde VFX. Four sections: 1. **Subtract, Normalize, Length** — Create direction vectors with subtract; normalize for uniform speed; length for scalar from vector; interactive point via Add node + Import Point Attribute; turbulent noise for randomization; scale with multiply (vector must be first input). 2. **Cross Product** — Perpendicular vector to plane formed by two...
- **File:** tutorials/vops-03---vector-operations---houdini-beginner-tutorial.md


### VOPS 04 - Geometry Interactions - Houdini Beginner Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qDtKmbCDn3k
- **Author:** Voxyde VFX
- **Houdini Version:** H19+
- **Tags:** vops, geometry-interaction, distance, nearpoint, point-cloud, pcopen, intersect, attribute-transfer, particles, beginner-intermediate
- **Summary:** 44m22s VOPs Part 4 by Voxyde VFX. Six sections covering all major ways geometry can communicate with geometry in Houdini:  1. **Distance & Import Point Attribute** — distance node for float gradient; import point attribute recap; turbulent noise on position for organic density source 2. **Nearpoint** — nearest point number from multi-point second input; must combine with import point attribute...
- **File:** tutorials/vops-04---geometry-interactions---houdini-beginner-tutorial.md


### Intro To Houdini Solaris - Full Beginner Course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3BX97YIQERE
- **Author:** Voxyde VFX
- **Houdini Version:** any modern (H19.5+)
- **Tags:** solaris, lops, usd, scene-assembly, instancer, component-builder, look-dev, karma, aov, materials, lighting, rendering, beginner-intermediate
- **Summary:** Voxyde VFX comprehensive Solaris beginner course (286m6s, 19 sections). Part 1 covers each ingredient in isolation: USD & scene graph (paths, opinion layering, character workflow), scene assembly (SOP import/create, path prefix, name vs path attribute), stage manager (hand-placement, duplicates, groups, physics collision), material library (karma material builder, material linker, AMD material...
- **File:** tutorials/intro-to-houdini-solaris---full-beginner-course.md


### Houdini Tutorial - Simple Disintegration FX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O2F1Qzl22oU
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini 19/20
- **Tags:** vops, disintegration, mask, noise, particles, vfx, intermediate
- **Summary:** Voxyde VFX 21-min tutorial on a simple disintegration effect (triangles break apart from center outward). Geometry: test squab → Remesh (target size 0.001, 10 iterations) = equal triangles. Mask (Point VOP): BBox node → average Pmin+Pmax = centroid → Vector to Float (X, Z only) → Float to Vector2 for both position and centroid → Distance 2D → fit to 0–1 (source min = "anim" param, max =...
- **File:** tutorials/houdini-tutorial---simple-disintegration-fx.md


### Houdini 21 Tutorial - MPM Snowball
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aQQeEOlHqjQ
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini 21
- **Tags:** mpm, simulation, snow, particles, vdb, karma, compositing, secondary-sim, intermediate
- **Summary:** Voxyde VFX (Mikael) 50-min Houdini 21 MPM tutorial: snowball hitting a helmet. Snowball: sphere (0.08 radius) + two Mountain SOPs (large elements high strength + small elements low strength). MPM Configure creates source/collider/solver. Collider fix for concave helmets: enter MPM Collider → VDB Collider → VDB from Polygons enable Pressure Falls + add VDB Reshape SDF. Source settings: Snow...
- **File:** tutorials/houdini-21-tutorial---mpm-snowball.md


### Houdini Solaris Tutorial - Rendering Multiple ROPS Together
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qg3OFz4JZs4
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini (any modern, Solaris)
- **Tags:** solaris, rendering, rop, tops, batch-render, workflow, beginner
- **Summary:** Voxyde VFX short tip (1m25s): batch render all Solaris ROP sequences without manually triggering each one. Workflow: create TOP Network → dive in → create one ROP Fetch node per ROP output (character, blast, bug, rain, water), naming each ROP Fetch identically to its ROP output → select all ROP Fetch nodes → set "Stash Stage" to flush at lowest → change ROP cook order from Frame by Frame to...
- **File:** tutorials/houdini-solaris-tutorial---rendering-multiple-rops-together.md


### Improve Solaris Performance - Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QfWUzrfsDaY
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini (any modern with Solaris, H19+)
- **Tags:** solaris, lops, performance, proxy-geo, poly-reduce, usd, pipeline, point-deform, intermediate
- **Summary:** Voxyde VFX tutorial (22m50s) covering how to efficiently load all common simulation types into Solaris/LOPs with fast viewport performance. The core pattern: SOP network produces two branches (render geo = full quality, proxy geo = low poly), each tagged with `s@purpose` and merged under a common path structure. Covers 6 geometry types: static single mesh, multi-instance (fern), animated...
- **File:** tutorials/improve-solaris-performance---houdini-tutorial.md


### Houdini Tutorial - Wispy Smoke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RRmvyQu39-4
- **Author:** Voxyde VFX
- **Houdini Version:** Houdini (any modern)
- **Tags:** pyro, pop, particles, curves, volume, smoke, karma, wispy, intermediate
- **Summary:** Voxyde VFX 27-min tutorial on wispy (cigarette-style) smoke. Core pipeline: (1) Pyro sim (Config Pyro → sphere source, no flame, buoyancy 0.4, turbulence remapped to hill shape, viscosity 0.1, animated velocity noise layers, gas turbulence inside + vortex confinement, time scale 1.5). (2) Scatter particles from volume (1000–5000, animated density attr with noise, animated seed $F). (3)...
- **File:** tutorials/houdini-tutorial---wispy-smoke.md


### Introduction to Particles in Houdini 21 [FULL Beginner Course 2026]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=041qemBc_1Q
- **Author:** Pixel In The Frame
- **Houdini Version:** H21 / any modern (H19+)
- **Tags:** particles, pop, pop-solver, pop-force, pop-vop, pop-wrangle, collisions, instancing, karma, solaris, lops, motion-blur, beginner-intermediate
- **Summary:** 165-minute comprehensive course by Pixel In The Frame for Houdini 21. Covers 22 sections end-to-end from POP network setup through final Karma render. Notable for: detailed collision setup (surface vs volume SDF), orient/quaternion hierarchy (orient > N > v), POP Look-at node, Particle Trail SOP, volume advection with velocity VDB, and a full instancing-in-LOPs workflow using Collection node....
- **File:** tutorials/introduction-to-particles-in-houdini-21-full-beginner-course-2026.md


### Houdini UV Unwrapping Fundamentals
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cguHzZ9L87g
- **Author:** Mat Sola
- **Houdini Version:** Houdini (any modern, H18+)
- **Tags:** uv, unwrapping, fundamentals, uv-layout, uv-flatten, auto-seams, workflow, beginner-intermediate
- **Summary:** Mat Sola comprehensive UV fundamentals course (65m23s). Covers the complete end-to-end UV pipeline in Houdini with concrete examples for each step. Geometry preparation section covers 7 common problems (non-manifold edges, single-vertex sharing, unwelded points, flipped normals, scale issues, overlapping geometry, zero surface area, stale attributes/groups). Seam creation covers 4 methods...
- **File:** tutorials/houdini-uv-unwrapping-fundamentals.md


### Model a Procedural Flower | Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pIp3cYSBZc4
- **Author:** Fifo
- **Houdini Version:** any modern (H19+)
- **Tags:** procedural-modeling, vellum, wire-solver, copy-to-points, for-each, quaternion, golden-angle, phyllotaxis, sweep, intermediate
- **Summary:** 38-minute tutorial by Fifo building a complete procedural growing flower. Core innovations: using the golden ratio angle with quaternion rotation for realistic flower phyllotaxis; for-each loop TimeShift trick for sequential blooming (bottom-to-top); Vellum cloth constraints with "match animation" rest blend for intersection resolution. No rigid body physics — all Vellum. Final setup has...
- **File:** tutorials/model-a-procedural-flower-houdini-tutorial.md


### Houdini Tutorial | Creating Realistic Waterfall Simulation (Step-by-Step)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eYqxarTsOrE
- **Author:** VFX Grace
- **Houdini Version:** Houdini 19/20
- **Tags:** flip, waterfall, white-water, vdb, mantra, compositing, particles, simulation, advanced
- **Summary:** Daily Course 151-min comprehensive waterfall tutorial. Key insight: terrain flatness is critical — flat terrain = stable dynamics; too much relief = chaotic simulation. Workflow: (1) Height field terrain: start flat, add noise in the bevel/drop area only, blur for rectangle shapes, mask for upland slope. Convert to mesh + Poly Reduce + Cast. Rocks: sphere + Subdivide + Mountain SOP. (2) FLIP...
- **File:** tutorials/houdini-tutorial-creating-realistic-waterfall-simulation-step-by-step.md


### Grain Vortex in Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8fcfu6gmzUQ
- **Author:** raphaël
- **Houdini Version:** Not specified
- **Tags:** "dop", "sop", "rbd", "simulation", "procedural", "advanced"
- **Summary:** Scatters a Megascans rock (reduced to a ~100-face/50-point low-poly proxy for sim performance, high-poly kept separately via a Null for final render) onto 10,000 points scattered inside a box volume (Scatter on an ISO-Offset volume), randomizing per-instance orientation with a MOPs Randomize node. De-intersects the scattered copies using a Boolean (Detect operation) to flag intersecting...
- **File:** tutorials/grain-vortex-in-houdini-tutorial.md


### [Урок] Тяжелый Люкс. Часть 1. (Heavy Lux — Luxury Particle Effect, Part 1)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gsrHHeYadZ0
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** particles, pop, heightfield, sand, logo, mask-animation, turbulence-noise, vdb, points-from-volume, intermediate-advanced
- **Summary:** 29m43s tutorial by Alexander Eskin. Luxury brand Instagram-style shot: "Dior" logo imprinted in animated sand terrain with particles rising in wave. Pipeline: Grid scatter 10k points → POP Network (All Points emission) → POP Wind (velocity=6) driven by color/mask attribute so particles in white zones fly, black zones stay; animated radial gradient mask (fit on distance) sweeps outward frame...
- **File:** tutorials/урок-тяжелый-люкс-часть-1.md


### Houdini Tutorial: Make Any Geometry Knitted
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mTnQji8a8nw
- **Author:** PolygonCGI
- **Houdini Version:** Houdini (any modern, H19+)
- **Tags:** knit, procedural, uv, copy-to-points, sweep, attribute-swap, redshift, shading, intermediate
- **Summary:** PolygonCGI beginner/intermediate tutorial (27m27s). Build a single knit stitch by modeling half a loop, mirroring, and using CurveKnot for procedural width control. Tile the stitch across a grid using Points from Volume + Copy to Points. Flatten the target skull mesh into UV space (Connectivity UV → Vertex Split → Attribute Swap P↔UV), align the knit grid into UV space, then Attribute Swap...
- **File:** tutorials/houdini-tutorial-make-any-geometry-knitted.md


### [Tutorial] Heavy Chic. Part 1.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fjVERoS2olY
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** particles, pop, height-field, volume, scatter, noise, logo-trace, animation, pscale, intermediate
- **Summary:** 24m4s tutorial by Alexander Eskin. Builds a "heavy chic" particle sand/logo effect. Workflow: scatter points on a height field, emit only frame 1, drive upward pop wind velocity by noise (turbulence via `windpointy *= Cd.x`), animate an expanding wave mask (length + fit) to control when/where particles rise. Complex height field: Height Field Noise + VOP binding trick (height→density) +...
- **File:** tutorials/tutorial-heavy-chic-part-1.md


### [Tutorial] Heavy Chic. Part 2.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mOKs6Dht5Mw
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** particles, rendering, mantra, instancing, gold-material, file-cache, fracture, pscale, depth-of-field, intermediate
- **Summary:** 17m52s tutorial by Alexander Eskin (continuation of Heavy Chic Part 1). Polishes the particle simulation: adds noise multiplied by Cd (so stationary particles don't drift), applies a b-spline gamma ramp to redistribute particle density, increases point count from 700K to 11M (point separation 0.004). Caches to disk with `$OS.$F4.bgeo.sc`. Creates custom particle geometry: fractures a box,...
- **File:** tutorials/tutorial-heavy-chic-part-2.md


### [Урок] Тяжелый Люкс. Часть 2. (Heavy Lux Part 2 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UrDkzEXDdLM
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** particles, instancing, voronoi, rendering, redshift, file-cache, multi-shot, orient-random, intermediate-advanced
- **Summary:** 22m5s tutorial by Alexander Eskin. Part 2 of luxury brand particle shot. Polishes the noise mask (frequency 1.7, Turbulence noise added, ramp with Spline interpolation for sharper contrast peaks). File Cache full simulation (1M particles) keeping only pscale+ID. Creates Voronoi fragment instance geometry: Box → Scatter 45 pts → Voronoi Fracture → Pack (Instancer) → Blast exterior pieces...
- **File:** tutorials/урок-тяжелый-люкс-часть-2.md


### [Tutorial] Glass Tiles
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ps6ZOKEdDos
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** glass, tiles, animation, orient, quaternion, attribute-transfer, pop, trails, material, blend-material, rendering, mantra, intermediate
- **Summary:** 25m6s tutorial by Alexander Eskin. Builds an animated glass tile wall that flips from opaque tiles to glowing emissive to transparent glass in a wave. Tile: Box + PolyExtrude + Bevel + Subdivide. Wall: Copy to Points on grid (128×128 pts, P_scale control). "Rotor" attribute driven by Attribute Transfer from a Mountain-noised grid (undisplaced transfer + Attribute Copy trick). Orient rotated...
- **File:** tutorials/tutorial-glass-tiles.md


### [Урок] Стеклянная Плитка (Glass Tile — RU, Extended)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-s-AnXgjw-o
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** procedural-animation, tiles, orient, quaternion, attribute-transfer, particles, trails, octane, intermediate
- **Summary:** 32m14s tutorial by Alexander Eskin. Creates animated glass tile wall with procedural wave flip rotation. Pipeline: tile box (0.1×0.5) → PolyBevel → Mountain → SubDiv; scatter on 128×128 plane grid → Copy to Points with pscale; animated wave attribute via Attribute Transfer from moving grid (dense 55×55, falloff/blend); noise on attribute for organic variation; VEX quaternion for orient; 3...
- **File:** tutorials/урок-стеклянная-плитка.md


### [Урок] Мягкая Ткань (Soft Fabric/Weaving — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ju8pDlzR3vM
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** procedural-modeling, weaving, sine-waves, animation, growth, sweep, vellum, point-deform, hair-shader, intermediate
- **Summary:** 43m32s tutorial by Alexander Eskin. Creates animated woven/knitted fiber effect. Pipeline: 2000-point line → VEX sine displacement (`Z = sin(curveu * freq) * amp`, `X = sin(curveu * freq - phase) * amp`) → Copy to Points with even/odd phase flip (`@ptnum % 2 ? -1 : 1`) for interlocking loops → Sweep (170 twists, small radius) for 3D tubes → curveu-driven pscale for thickness variation. Grow...
- **File:** tutorials/урок-мягкая-ткань.md


### [Tutorial] Soft Weave
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ohj4ag8DZRo
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** sweep, weave, sine-wave, curve-u, blend, attribute-transfer, hair, redshift, vellum, point-deform, intermediate-advanced
- **Summary:** 36m17s tutorial by Alexander Eskin. Builds a soft weaving fabric animation entirely from procedural SOP geometry (no simulation for the weave itself). Lines with CurveU-based sine-wave offsets create a weave pattern; alternating line direction prevents uniformity. Multiple Sweep SOPs (5 passes at different radii/twists) create strand variety. pscale grow animation via P lerp (not direct pscale...
- **File:** tutorials/tutorial-soft-weave.md


### [Урок] Губка (Sponge — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cQd2YXWiQ4k
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** vellum, grains, particles, instancing, cotton-fibers, friction, cluster, pscale, shader, beginner-intermediate
- **Summary:** 32m49s tutorial by Alexander Eskin, recreating an Instagram work by Max Shulgiy. Creates a sponge simulation using Vellum Grains: box geometry → scattered points → Vellum Grains solver with custom gravity, granular collision for wet-sand look, and cluster attribute (32 clusters) fed into Random for friction variation. Cotton fiber clumps built from 3 custom catmull curve shapes (3 variations),...
- **File:** tutorials/урок-губка.md


### [Tutorial] Purple Sponge
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O5cFGKp0n_A
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** vellum, grains, clustering, instancing, redshift, noise, rest-attribute, cotton, attraction-weight, intermediate
- **Summary:** 29m17s tutorial by Alexander Eskin (inspired by Mark's work on Instagram). Creates a "purple sponge" cotton-ball mound effect. Box → VDB (cloud noise) → Points from Volume (400K pts, pscale=0.5) with bounding region blast + Y=0 delete + additional positional noise. Vellum Grains sim: fix ground intersection with `P.y += pscale`, interaction_weight=1 for wet-sand clumping, Cluster Points (32) +...
- **File:** tutorials/tutorial-purple-sponge.md


### [Урок] Стеклянный Пончик (Glass Donut — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HkMJWwyqo-I
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** modeling, torus, noise, seamless-loop, glass-shader, redshift, dome-light, cop-texture, subdiv-displacement, beginner
- **Summary:** 13m15s tutorial by Alexander Eskin. Quick product-style glass donut render. Creates Torus primitive with Mountain noise displacement → key insight: noise values at offset 0 and 1 are identical → animate offset 0→1 over 300 frames (linear) → set frame 300 keyframe equal to frame 1 value → perfect seamless loop. PolyExtrude for glass thickness. Gradient textures built in Houdini COPs (4000×2000...
- **File:** tutorials/урок-стеклянный-пончик.md


### [Tutorial] Glass Donut
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=j5Ew_6-W8DE
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** glass, torus, noise, flow-noise, rendering, mantra, hdri, material, subdivision, beginner-intermediate
- **Summary:** 13m28s tutorial by Alexander Eskin. Creates a glass donut (torus) with animated, loopable noise displacement. Flow noise (anti-aliased) cycles from 0→1 over 300 frames for a seamless loop. Two-layer extrusion thickens the surface. Glass shader: full transmission + reflection, zero diffuse. Lighting uses two custom gradient HDRIs (painted in AE with circle feather, color grading, Video Copilot...
- **File:** tutorials/tutorial-glass-donut.md


### [Урок] Розовые Пузыри. Часть 1. (Pink Bubbles Part 1 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=alOGxWIIwTk
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** vellum, balloons, bubbles, particles, ripple-solver, scatter, noise, pop-wind, attribute-interpolate, intermediate
- **Summary:** 30m52s tutorial by Alexander Eskin. Creates pink bubbles floating inside a large sphere (Vellum Balloon simulation). Three bubble layers: large (65 scatter points → copy sphere → Vellum Balloons sim with wind, grain collision, drag variation); small (55000 scatter → noise scale variation → static); tiny (static on sphere surface, displaced). Sphere gets ripple-wave surface: POP particles spawn...
- **File:** tutorials/урок-розовые-пузыри-часть-1.md


### [Tutorial] Pink Bubble. Part 1.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ypJL4PXxQpg
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** vellum, balloon, grains, ripple-solver, pop, scatter, pscale, vellum-pack, wind, intermediate
- **Summary:** 25m54s tutorial by Alexander Eskin. Builds a complex "pink bubble" scene: large deforming Vellum Balloon spheres scattered inside a VDB shell, plus 55K small Vellum Ring grain-spheres on the surface, inside a collider sphere with zero gravity + wind (upward, noise-driven). Vellum Pack → merge → Vellum Unpack avoids the tedious manual constraint merging. Solver: uncheck "Assume Uniform Radius...
- **File:** tutorials/tutorial-pink-bubble-part-1.md


### [Урок] Розовые Пузыри. Часть 2. (Pink Bubbles Part 2 — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=faWPP0UPcU0
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** rendering, octane, glass-shader, bubbles, trails, particles, specular, strand-material, beginner-intermediate
- **Summary:** 15m49s tutorial by Alexander Eskin. Part 2 of Pink Bubbles project — rendering and scene polish. Exports geometry elements, builds Octane Render Target with 3 shaders (background, outer bubbles, inner bubbles). Background: plane (bottom wall only, SubDiv smooth). Bubble material: Octane Specular (aSpecular mode) → glass look; inner bubbles need Reverse normals for correct refraction....
- **File:** tutorials/урок-розовые-пузыри-часть-2.md


### [Tutorial] Pink Bubble. Part 2.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uztbmUElafA
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** rendering, octane, glass, dispersion, specular-material, instancing, lighting, beginner-intermediate
- **Summary:** 10m13s render tutorial by Alexander Eskin (Part 2 of Pink Bubble series). Sets up an Octane renderer for the bubble scene from Part 1. Uses Octane Specular material (glass-like). Small bubble spheres were just points — fix by Copy to Points of actual sphere geo (scale=2, polygon). Reverse normals on small spheres for correct reflections. Background: large reversed box (blast two open faces)....
- **File:** tutorials/tutorial-pink-bubble-part-2.md


### [Урок] Помада. Часть 1. Моделирование (Lipstick Pt1 Modeling — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fMNkSvAwIFk
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** modeling, hard-surface, revolve, boolean, vdb, logo-engraving, uv, octane, beginner-intermediate
- **Summary:** 15m37s tutorial by Alexander Eskin. Models a lipstick product for render. Part 1 of a series (Parts 2/3 cover FLIP simulation and rendering). Workflow: draw profile curve → Revolve (8–19 divisions) → Fuse pole → Boolean cut angled tip with Box (5–6° tilt) → SubDiv; Alpha texture image → VDB for engraved logo cutouts → Hole node → Divide (convex off, crack thickness 0.3) → VDB Sample 0.1 for...
- **File:** tutorials/урок-помада-часть-1-моделирование.md


### [Tutorial] Lipstick. Part 1. Modeling
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Zqle_HOS7Jg
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** modeling, revolve, boolean, trace, logo-emboss, vdb-remesh, uv, bevel, subdivide, procedural, intermediate
- **Summary:** 18m30s modeling tutorial by Alexander Eskin. Builds a complete lipstick product shot asset procedurally. Lipstick body: polygon curve drawn in front view → Revolve → clip overlap → Subdivide → Fuse; tip cut with Boolean (rotated box ~55°). Logo: Trace SOP on PNG alpha → Resample → Hole SOP → Divide (convex, crease); Raytrace project onto lipstick surface; lift 0.01 → PolyExtrude inward −0.025...
- **File:** tutorials/tutorial-lipstick-part-1-modeling.md


### [Урок] Помада. Часть 2. Flip Sim (Lipstick Pt2 FLIP Droplets — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H17o8w-CFUM
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** flip-sim, fluid-simulation, viscous, particles, vdb, surface-reconstruction, octane, intermediate
- **Summary:** 34m20s tutorial by Alexander Eskin. Part 2 of the lipstick series: takes the modeled lipstick geometry from Part 1 and simulates fluid FLIP dynamics to create realistic liquid-lipstick surface behavior. Transcript was not captured during ingestion (Russian audio without auto-captions). Based on title and series context, expected content: FLIP Object setup, viscosity/surface tension parameters...
- **File:** tutorials/урок-помада-часть-2-flip-sim.md


### [Tutorial] Lipstick. Part 2. Flip Sim
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=T1OTnyioFrA
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** flip, fluid, droplets, surface-tension, stick-field, velocity-field, vdb, collision, pscale, intermediate-advanced
- **Summary:** 26m21s FLIP tutorial by Alexander Eskin. Creates realistic water droplets that cling to the lipstick surface. Three passes of scatter (tiny ~0.03 pscale, medium, big ~0.05–0.8) with random pscale noise variation, displaced outward along surface normals proportionally to pscale. Points from Volume is the FLIP source (resolution from control null parameter `flip_res = 0.01`). Lipstick as VDB...
- **File:** tutorials/tutorial-lipstick-part-2-flip-sim.md


### [Tutorial] Lipstick. Part 3. Rendering
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6V7Y5aBmjo4
- **Author:** Alexander Eskin
- **Houdini Version:** H19
- **Tags:** rendering, octane, material, sss, flakes, metal-bump, hdri, cop2, lighting, water-shader, intermediate
- **Summary:** 14m27s render tutorial by Alexander Eskin (continuation of Parts 1+2). Uses **Octane renderer** inside Houdini (not Mantra/Karma). Render settings: Contour=1, path tracing, spectral depth=24, max samples=200, adaptive, cryptomatte by material name. Materials: background=emissive (weight=3), water=specular (default), metal=metallic+roughness=0+reflectance=0.4, lipstick=specular+SSS (random...
- **File:** tutorials/tutorial-lipstick-part-3-rendering.md


### [Урок] Помада. Часть 3. Рендер (Lipstick Pt3 Render — RU)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pcHSG38zTJg
- **Author:** Alexander Eskin
- **Houdini Version:** H19+
- **Tags:** rendering, octane, shading, materials, lighting, product-visualization, vdb, intermediate
- **Summary:** 22m14s tutorial by Alexander Eskin. Part 3 (final) of the lipstick series: renders the modeled and simulated lipstick in Octane for Houdini. Transcript was not captured during ingestion (Russian audio without auto-captions). Based on title, series context, and Part 1 notes (which mention Octane materials: lipstick, metal, cap, background), expected content: setting up Octane materials...
- **File:** tutorials/урок-помада-часть-3-рендер.md


### Rain Effect in Houdini | Houdini Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Yi0ATGFthqk
- **Author:** Fx Guru (Arbaaj)
- **Houdini Version:** H19
- **Tags:** particles, pop, rain, collision, vdb, static-object, rendering, beginner
- **Summary:** 33m6s beginner tutorial by Fx Guru (Arbaaj). Builds a rain effect from scratch: a flat grid emitter generates particles in a Pop Network, gravity pulls them down, inherited velocity variation removes per-frame layering artifacts. Collision is set up using a VDB generated by a Collision Source SOP from the character geometry, then fed into a Static Object / Static Solver inside the DOP network....
- **File:** tutorials/rain-effect-in-houdini-houdini-tutorial.md



### Tuna Can | procedural modeling and rig with KineFX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hHLH7pr_eZo
- **Author:** cgside
- **Houdini Version:** H19+
- **Tags:** kinefx, procedural-modeling, rigging, capture-proximity, sweep, quadremesh, polyfill, animation, intermediate
- **Summary:** Starts from a single line swept (Ribbon + Columns, grid end caps) into the lid's cross-section profile, then builds the embossed "staircase" pattern on the lid top using paired point offsets on concentric circles (position.y and pscale grouped in twos with incrementing offsets) before skinning them into rings. The can body is built separately from a mirrored square-tube sweep driven by a...
- **File:** tutorials/tuna-can-procedural-modeling-and-rig-with-kinefx.md


### Mechanical rigging in Houdini - Attaching custom controls
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7J-hDF0H6ck
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** rigging, kinefx, mechanical, controls, wrangle, matrix, fit-range, intermediate
- **Summary:** Attaches sphere-shaped animation controls to a mechanical rig and drives symmetric pairs of joint rotations by extracting each control's translation distance, fitting it to a precomputed max-rotation-angle range, and writing the rotated matrix back onto the rig points — done in parallel in a number-of-points wrangle (Point Generate + Name + Rig Doctor + instanced spheres; Attach Joint Geo; Rig Pose with locked rotation/axes so animators can only translate the intended axis).
- **File:** tutorials/mechanical-rigging-in-houdini---attaching-custom-controls.md


### Yan Paul Dubbelman | Procedural Nature | High-Quality Custom Leaves
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=d3pMfIsvAyQ
- **Author:** Houdini.School
- **Houdini Version:** H20.5+
- **Tags:** procedural-nature, leaves, copernicus, tree-branch-generator, uv-deform, voronoi, quad-remesh, texture-baking, tops-wedge, labs, patterns, intermediate
- **Summary:** 100m33s Houdini.School live session by Yan Paul Dubbelman. Complete workflow for generating photorealistic procedural leaf models with textures for real-time (Unreal Engine) or render pipelines. Pipeline: define leaf shape with grid + Linear Taper; build vein skeleton with Labs tree tools; UV-deform skeleton to match any shape with one wrangle line; clean up overshooting curves via Proximity +...
- **File:** tutorials/yan-paul-dubbelman-procedural-nature-high-quality-custom-leaves.md


### MOPs: Motion Operators for Houdini Part 3
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=q_aD6sza6gA
- **Author:** Houdini.School
- **Houdini Version:** H18.5+
- **Tags:** mops, math, vectors, matrices, quaternions, vex, linear-algebra, trigonometry, aim-constraint, forward-kinematics, transform, dot-product, cross-product, slurp, quaternion, intermediate-advanced
- **Summary:** 163m38s masterclass on the linear algebra and trigonometry that powers MOPs (and all of CG). Three example files — `01_vectors`, `02_trig`, `03_transforms` — walk from first principles to practical VEX. Topics: vectors (normalize, dot product, projection, Lambert/Fresnel shading, cross product, right-hand rule, double-cross for geo-normal forces), trig (sine/cosine as triangle ratios and...
- **File:** tutorials/mops-motion-operators-for-houdini-part-3.md


### MOPs: Motion Operators for Houdini Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=J2g0v1k6MBs
- **Author:** Houdini.School
- **Houdini Version:** any (H18.5+, MOPs 1.7.1)
- **Tags:** mops, motion-graphics, move-along-spline, move-along-mesh, delay, spring, sequences, pivot, reorient, apply-attributes, vellum, rbd, bullet, intermediate-advanced
- **Summary:** 170m22s live class (Houdini.School, Part 2). Covers: Move Along Spline (attach/animate stages, arc length mode, maintain offset, vexpressions); Move Along Mesh (Orient Mesh up vector, simulation, blend orient, relax); VEX snippets in modifier nodes; MOPs Neighbors (plexus connections); MOPs Delay (time-offset any attribute by falloff); MOPs Spring (Hooke's law; mass/spring-K/damping); packed...
- **File:** tutorials/mops-motion-operators-for-houdini-part-2.md


### MOPs: Motion Operators for Houdini Part 1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=g9eSle9IVjU
- **Author:** Houdini.School
- **Houdini Version:** any (H18.5+, MOPs 1.7.1)
- **Tags:** mops, motion-graphics, instancing, packed-primitives, intrinsics, transform, falloff, spread, noise, animation, intermediate
- **Summary:** 165m31s live class (Houdini.School, Henry/ToadStorm). Part 1 of a 3-part MOPs series. Covers: MOPs philosophy + installation, instancing pipeline (template point attrs vs intrinsic transforms), generators (Instancer, Convert, Explode, Trails), modifiers (Transform, Aim, Randomize, Noise), and falloffs (Shape, Noise, Spline, Object, Spread, Transform Falloff). Also covers using MOPs falloffs as...
- **File:** tutorials/mops-motion-operators-for-houdini-part-1.md


### Experimental Motion - CHOPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0XnjEVcaq6A
- **Author:** Houdini.School
- **Houdini Version:** Houdini (any modern)
- **Tags:** chops, animation, procedural, secondary-motion, jiggle, spring, filter, kinefx, vellum, mops, intermediate
- **Summary:** Houdini.School workshop by Jampal Duman (84 min): using CHOPs for organic, no-keyframe procedural animation. Philosophy: no keyframes — build filter systems instead. Setup: split viewport into 3 panes (main + CHOP network editor + Motion Effects Viewer). Core pipeline: (1) Animated SOP → (2) CHOP Network (Geometry node reads SOP, filter chain, CHOP Out) → (3) Channel node (reads CHOP, applies...
- **File:** tutorials/experimental-motion---chops.md


### Experimental Motion - The SOP Solver
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=A11B_UE07ac
- **Author:** Houdini.School
- **Houdini Version:** Not specified
- **Tags:** "sop", "vop", "particles", "procedural", "advanced"
- **Summary:** A long-form artistic workshop (Yan Paul Dubbelman / Houdini.School) on using the SOP Solver philosophically — guiding a system toward a result rather than authoring every step. **System 1 (coral growth):** starting from a sphere, create a `life` float attribute (Attribute Adjust Float) driven by a Noise pattern, feed it into a Soft Peak node's Distance input (pushes points outward along their...
- **File:** tutorials/experimental-motion---the-sop-solver.md


### Yan Paul Dubbelman | Procedural Nature | Procedural Living Plants
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xjf_mQKI3R8
- **Author:** Houdini.School
- **Houdini Version:** H19+
- **Tags:** procedural-nature, plants, trees, animation, growth, curl, labs-tree-tools, mops, guide-deform, rig-wrangle, orient-along-curve, sweep, beginner-intermediate
- **Summary:** 73m59s Houdini.School live session by Yan Paul Dubbelman (intro to procedural nature series). Builds an animated growing/unfurling plant from scratch using only Labs Tree tools + one VEX line. Pipeline: Labs Tree Trunk Generator + Labs Tree Branch Generator (2–3 levels) for skeleton; Resample for even point spacing; Orient Along Curve (3×3 transform output renamed to "orient"); Rig Attribute...
- **File:** tutorials/yan-paul-dubbelman-procedural-nature-procedural-living-plants.md

### Procedural HDAs for Unreal
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rKcH4oIfoVw
- **Author:** Houdini.School
- **Houdini Version:** H19+
- **Tags:** procedural-nature, plants, trees, animation, growth, curl, labs-tree-tools, mops, guide-deform, rig-wrangle, orient-along-curve, sweep, beginner-intermediate
- **Summary:** 73m59s Houdini.School live session by Yan Paul Dubbelman (intro to procedural nature series). Builds an animated growing/unfurling plant from scratch using only Labs Tree tools + one VEX line. Pipeline: Labs Tree Trunk Generator + Labs Tree Branch Generator (2–3 levels) for skeleton; Resample for even point spacing; Orient Along Curve (3×3 transform output renamed to "orient"); Rig Attribute...
- **File:** tutorials/procedural-hdas-for-unreal.md


### Velocity Forces 2.0: Advanced
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EuL8598tnm4
- **Author:** Houdini.School
- **Houdini Version:** H19+
- **Tags:** velocity, volumes, vex, openvdb, simulation, fluid, smoke, optical-flow, vorticals, matrices, quaternions, intermediate-advanced
- **Summary:** 1m24s course trailer for "Velocity Forces 2.0: Advanced" by David Torno at Houdini.School. Sequel to Velocity Forces 1. Covers: nuances between standard Houdini volumes and OpenVDB, techniques to eliminate velocity field activation stepping, blending/mixing multiple velocity fields, using simulation outputs as velocity sources for organic movement, creating vorticals (weighted turbulence...
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
- **Houdini Version:** Not specified
- **Tags:** "attributes", "beginner", "intermediate"
- **Summary:** Introduces a 3-session paid course on Houdini attributes: Session 1 covers core geometry components, attribute classes/types, the geometry spreadsheet, and intrinsics. Session 2 covers the many ways to create/read attributes, attributes vs. variables (global vs. local, `$` vs. `@` syntax history), and touches VOPs/VEX/HScript/Python alongside native SOP attribute nodes for non-coders. Session...
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
- **Houdini Version:** H19+
- **Tags:** kinefx, labs, tree-tools, procedural, growth, vex, chops, rigging, animation, vegetation, intermediate-advanced
- **Summary:** 1m22s promotional trailer. Course covers: (1) SideFX Labs Tree Tools (free, built into Houdini) for procedural vegetation generation; (2) KineFX rigging of the generated tree; (3) VEX + CHOPs procedural growth and wind animation; (4) advanced module: modding Labs tree tool internals for more flexibility. Instructor: Mark Fancher. Intermediate–Advanced level; requires prior VEX and general...
- **File:** tutorials/procedural-growth-with-kinefx-and-the-labs-tree-tools.md


### Scientific Phenomena in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=g-EDNX2uaXo
- **Author:** Houdini.School
- **Houdini Version:** H19+
- **Tags:** volumes, procedural, simulation, clouds, ocean, planetary, fractals, fluid, vfx, intermediate-advanced
- **Summary:** 1m57s promotional trailer. Instructor Kate Sagarar (VFX artist, NPC Toronto; credits: Umbrella Academy, The Boys, Raised by Wolves, The Witcher) teaches how science informs and improves VFX builds. Each session covers the real science then applies it in Houdini. Topics: cloud types and storm systems (volumetric simulation), procedural planetary system based on astronomy, fractal/procedural...
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
- **Tags:** "scientific-visualization", "data-visualization", "pdb", "molecular", "attributes", "particles", "simulation", "biology"
- **Summary:** Kate Zegarace (Houdini.School instructor and VFX artist) presents a course on molecular visualization using Protein Data Bank (PDB) data as the input. The course covers the biology basics of proteins (what they are, how they work) then builds the Houdini pipeline to process PDB files and generate multiple visualization modes: space-filling, wireframe, ball-and-stick models. Atoms are animated...
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
- **Houdini Version:** Houdini (any modern)
- **Tags:** unreal-engine, vat, niagara, kinefx, vellum, rbd, pyro, pipeline, intermediate-advanced
- **Summary:** Short promotional overview (4m25s) for a Houdini.School 3-session course on using Houdini FX inside Unreal Engine. Session 1: modeling techniques + procedural UV mapping → import to Unreal → project/folder organization → MN sequence + subsequences → Megascans materials → HDRI interior lighting → ACES color space render → EXR export for DaVinci → procedural robot from shark model (Substance...
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
- **Houdini Version:** H19+
- **Tags:** noise, vex, vops, pdg, topnet, python, shaders, volumes, particles, motion-graphics, beginner-intermediate
- **Summary:** 1m31s promotional trailer for the Houdini.School "Noise" full course. No technical content taught in this clip. Course promises: (1) survey of all stock Houdini noise types and simple manipulations to produce more interesting visuals; (2) practical use cases — driving attributes, creating maps/shaders, adding volume detail, defining particle emission; (3) PDG TOPnet workflow for...
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
- **Summary:** Outlines a 5-week project-based course: Week 1 — Houdini interface/versions/hardware, procedural workflow basics, modeling a Thor's Hammer asset with shaders and a first render. Week 2 — animating the hammer via CHOPs, building the main "ray"/lightning-strike setup with ray ramifications and extra rays, VOPs for geometry modification and attribute ramps. Week 3 — points, particles, and...
- **File:** tutorials/00-weeks-overview-v1-1080p.md


### 03 houdini versions v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EMmAmGGsI6I
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "beginner"
- **Summary:** Explains SideFX's Houdini license tiers: Core (full toolset minus FX — no Pyro/fluids/RBD/particles/crowds, still capable for modeling/lighting/general work), FX (complete unlimited package), Indie (FX feature set, limited commercial license, render cap 4K×4K), Education (FX features for verified teaching institutions), and Apprentice (free, full FX features for learning, with watermarked...
- **File:** tutorials/03-houdini-versions-v1-1080p.md


### 51 introducing the sop solver v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8HkP7iVgi0Y
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vex", "wrangler", "particles", "simulation", "beginner"
- **Summary:** Before touching POPs, builds the same per-frame position update manually to demystify what a solver actually does. Scatters 100 points on a grid, gives them a constant velocity attribute `v` (vector, meters/second — Houdini's native unit), and writes a Point Wrangle (`@P = @P + @v;`) that nudges position once. Demonstrates that running this wrangle once doesn't animate anything over time — it...
- **File:** tutorials/51-introducing-the-sop-solver-v1-1080p.md


### 52 creating a simplified particle system v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=l65A4S4YhSw
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vex", "wrangler", "particles", "simulation", "beginner"
- **Summary:** Direct continuation of "introducing the sop solver." First, makes the Scatter node re-randomize every frame by setting its Global Seed to `$F` (frame number), then merges the solver's own previous-frame output with freshly-scattered Input 1 particles each frame, producing continuous particle emission rather than one static batch. Adds an `age` float attribute (starts at 0) and increments it...
- **File:** tutorials/52-creating-a-simplified-particle-system-v1-1080p.md


### 53 recreating our solver with pops v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9objvx69_58
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "sop", "vop", "particles", "simulation", "beginner"
- **Summary:** Shows that a POP Network needs no manual Scatter step — the source surface can feed directly into the network's first input, and the POP Solver/POP Object/operator structure handles emission, integration, and storage automatically. Converts the earlier hand-built rates and values into POP Network terms: a **POP Source** node (Source: surface, Emission Type: Scattered onto surfaces) on the...
- **File:** tutorials/53-recreating-our-solver-with-pops-v1-1080p.md


### 76 starting the smoke vortex v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=BFZ3tItjKn8
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "dop", "sop", "pyro", "smoke", "simulation", "intermediate"
- **Summary:** Continuation lesson (follows a prior sine-function/sphere demo) applying the same animation principles to a new emitter shape. Builds a Torus (aligned to Z, tuned radius/thickness ~0.6/0.025), increases its row/column resolution, applies a Transform (kept separate, for non-uniform scaling) and a Subdivide for smoother geometry, lifts it off the ground, and animates rotation around Z via `time...
- **File:** tutorials/76-starting-the-smoke-vortex-v1-1080p.md


### 78 building the vortex dop network v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FAE7gVev-ss
- **Author:** The VFX School Archive
- **Houdini Version:** Not specified
- **Tags:** "dop", "pyro", "smoke", "simulation", "advanced"
- **Summary:** Sets up the minimum required Pyro sim network: Pyro Solver, Smoke Object, and a Volume Source referencing the torus source built previously. To size the Smoke Object's simulation bounds correctly relative to the source torus, creates a throwaway Static Object referencing the torus (via Object Transform + copied sub-path), merges it temporarily into the view for visual sizing reference only,...
- **File:** tutorials/78-building-the-vortex-dop-network-v1-1080p.md


### module i   week 01   01   your first houdini project v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mq1snWFUBj0
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** beginner, ui, navigation, project-setup, contexts, solaris, karma, beginner
- **Summary:** 9m34s intro lesson from The VFX School Renaissance Programme Vol.1 (H18.5). Covers the absolute basics: viewport navigation controls (Alt+LMB tumble, MMB pan, RMB zoom), the context hierarchy (OBJ, SOP, Chops, Stage/LOP), switching contexts, parameter window usage (floating vs corner P key), dropping geometry nodes, and setting up a project folder + saving the hip file.
- **File:** tutorials/module-i-week-01-01-your-first-houdini-project-v1-1080p.md


### module i   week 02   01   creating a new project v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mjw4gT36Ub4
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** scatter, project-setup, beginner, course-intro
- **Summary:** 1m53s intro for Module I Week 2 of The VFX School Renaissance course. Describes two projects: (1) scatter geometry built in Houdini over a surface using new nodes/workflows, (2) scatter Megascans models over a head. Setup steps: create new project "week2_scatters", save with version number using `$JOB`.
- **File:** tutorials/module-i-week-02-01-creating-a-new-project-v1-1080p.md


### module i   week 03   01   introduction to volumes v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hEcmhhNlpzY
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** volumes, vdb, sdf, fog-volume, velocity-field, vdb-reshape, beginner-intermediate
- **Summary:** 15m11s intro lesson (VFX School Week 3, module-i) introducing volume concepts before cloud simulation. Covers native Houdini volumes vs VDB (efficiency = VDB only stores non-empty voxels); fog VDB vs surface/SDF VDB; storing velocity as a vector inside a volume (for simulation); multiple visualization methods (Volume Slice, Volume Trail, point generation from volume, VDB Viz Tree); boolean...
- **File:** tutorials/module-i-week-03-01-introduction-to-volumes-v1-1080p.md


### module i   week 04   01   introduction to particles v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9S5YABmK_eU
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** particles, pop, pop-solver, dop, sourcing, impulse, constant, gravity, beginner
- **Summary:** 13m34s intro lesson (VFX School Module I, Week 4) on particles in Houdini. Uses pig head test geometry. Explains the OBJ↔DOP context bridge (points → particles inside DOP → points on exit), autodop network auto-generated by shelf tools, and each DOP node's role. Covers sourcing modes, activation types (impulse = per frame/substep, constant = per second), ID attribute, life expectancy,...
- **File:** tutorials/module-i-week-04-01-introduction-to-particles-v1-1080p.md


### module i   week 05   01   importing the geometry v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Fo3HaNq9f8M
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** alembic, import, time-shift, flip-fluids, pop-fluid, beginner
- **Summary:** 2m42s setup lesson (VFX School Module I Week 5: horse POP fluid). Creates new project, imports Alembic horse animation, drops Convert SOP to get access to polygons, then uses Time Shift with `$FF` (float frame variable) and multiplier 0.3 to slow animation to 30% speed — critical for proper fluid sourcing with substeps.
- **File:** tutorials/module-i-week-05-01-importing-the-geometry-v1-1080p.md


### module i   week 06   01   introduction to grains v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XPDsqVutqDw
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** grains, vellum, vellum-configure-grain, points-from-volume, substeps, attraction, beginner-intermediate
- **Summary:** 9m56s intro lesson (VFX School Module I Week 6: zombie grains). Imports FBX zombie, creates grain setup from volume. Covers: Vellum Configure Grain (create points from volume, pscale/grain_size attributes, `grain` attribute for solver identification), Poly Fill for non-watertight geometry, Vellum Solver (no constraints required for basic grains), grain vs particle difference (interpenetration...
- **File:** tutorials/module-i-week-06-01-introduction-to-grains-v1-1080p.md


### module ii   week 01   01   basic bullet sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vQSQgkSvm8g
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, bullet, packed-geometry, dop, rigid-body-solver, beginner
- **Summary:** 7m21s intro to RBD bullet simulation (VFX School Module II Week 1). Demonstrates the same falling box sim two ways: quick SOP-level RBD Bullet Solver (H18.5 wrapper node, 2 nodes total) vs. manual DOP network approach. Explains why packed geometry is required (bullet works only with packed prims), how Pack SOP changes geometry representation (intrinsic packed transform attributes), and the...
- **File:** tutorials/module-ii-week-01-01-basic-bullet-sim-v1-1080p.md


### module ii   week 02   01   importing the geometry v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tC3H8wBaytE
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** import, alembic, lod, path-attribute, exploded-view, rbd, beginner
- **Summary:** 4m48s lesson (Module II Week 2, lesson 1). Imports a Brooklyn building Alembic with multiple LODs. LOD 2 chosen: separate tiles, windows, wooden panels (all distinct pieces). LOD 1 is fused and unworkable for fracture. Workflow: Geometry node → Alembic SOP → scale to 0.01 → Unpack → inspect path attribute for material IDs → 3D connectivity display (key 9) to confirm piece separation → Exploded...
- **File:** tutorials/module-ii-week-02-01-importing-the-geometry-v1-1080p.md


### module ii   week 03   01   splitting by material v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cvAuweF1fvg
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, fracture, path-attribute, split-sop, material-separation, building, area-attribute, intermediate
- **Summary:** 5m31s lesson. Splits a Brooklyn building Alembic into material-based geometry streams for selective fracturing. Workflow: Connectivity SOP (set to primitives) → Convert (polysoups to polygons) → Split SOP chain using path attribute wildcards. Groups created: glass (windows), bits (small area pieces < 0.5), wood, fiberglass. Each split feeds its own fracture operation for variety. Uses exploded...
- **File:** tutorials/module-ii-week-03-01-splitting-by-material-v1-1080p.md


### module ii   week 04   01   importing the geometry v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uPPW2sI_oyw
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** import, alembic, rbd, skyscraper, polysoup, performance, beginner
- **Summary:** 3m21s lesson (Module II Week 4, lesson 1). New project "collapse v1" — skyscraper RBD collapse. Imports packed Alembic skyscraper LOD 3, scales to 0.1. Poly soup converts to 3.6M polygon points (heavy) — use wireframe display. Simulation strategy: 3 separate sims to manage complexity, inactive geometry at bottom, omit fine detail geo.
- **File:** tutorials/module-ii-week-04-01-importing-the-geometry-v1-1080p.md


### module i   week 01   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZYFlDsFBxhA
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, destruction, fracture, debris, pyro, course-intro, beginner
- **Summary:** 1m38s intro video for Week 1, Module 1 of The VFX School Renaissance Course. Describes the project pipeline: boolean-based fracture for interesting shapes, RBD simulation, debris secondary simulation sourced from the RBD velocity and object size, and a tertiary pyro simulation sourced from crack edges. No technical instruction — context only.
- **File:** tutorials/module-i-week-01-01-intro-v1-1080p.md


### module i   week 02   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=G1JI3ACUZN4
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, destruction, glass, metal, wood, plasticity, course-intro, beginner
- **Summary:** 1m41s intro for Module I Week 2. Bus stop destruction project: metal frame, glass panels, and wood benches all destroyed together. Key new tools introduced: RBD Material Fracture node for glass and wood fracture, plasticity (H18) for soft metal constraints that bend/creak/pop instead of springing back. Two simulations: first the heavy metal, then glass and wood driven by the metal result.
- **File:** tutorials/module-i-week-02-01-intro-v1-1080p.md


### module i   week 03   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QkzF0SC76qY
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, destruction, car-crash, metal, glass, constraints, course-intro, intermediate
- **Summary:** 1m37s intro for Module I Week 3. Two-week car crash project: animated car slides sideways and slams into a post. Week 3 = metal setup (geometry organization, selecting pieces for plasticity bending, efficiency optimization, wheel constraints). Week 4 = rest of simulation (glass, other elements). Wheels use control constraints + soft constraints for suspension bounce and free spin around axis.
- **File:** tutorials/module-i-week-03-01-intro-v1-1080p.md


### module i   week 04   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=w9p4zfurT2A
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, glass, fracture, car-crash, constraints, laminated-glass, course-intro, intermediate
- **Summary:** 1m53s intro for Week 4 (final week of Module I RBD course). Builds on Week 3 metal simulation. Covers: laminated glass (windscreen) fracture — first a triangular spider-web pattern then Voronoi fine fracture; tempered glass (side window) — simple fine Voronoi pieces; constraint setup to keep glass pieces stuck to window frame initially; per-frame constraint manipulation in simulation;...
- **File:** tutorials/module-i-week-04-01-intro-v1-1080p.md


### module i   week 01   09   setting the active attribute v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VXkmQAGzBbA
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, destruction, active-attribute, rbd-configure, attribute-transfer, speed-limit, intermediate
- **Summary:** 10m22s lesson (VFX School Module I, Week 1, lesson 9). Covers the full RBD Configure node setup for an explosion simulation: packing geometry, applying concrete material presets, activating the `active` attribute (1=simulates, 0=collides but doesn't move), creating a border ring of inactive pieces by attribute-transferring from edge geometry (delete by normal to isolate sides), and adding...
- **File:** tutorials/module-i-week-01-09-setting-the-active-attribute-v1-1080p.md


### module i   week 02   15   starting the post sim setup v1 1080p1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XFOd1dy92Eg
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, post-sim, object-merge, destruction, intermediate
- **Summary:** 2m13s lesson covering the organizational step of post-sim setup. Creates a null after the simulation cache, then a new geometry node "post_sim" with Object Merges of: (1) sim output (fractured animated geometry), (2) pre-fracture metal (for Point Deforming), (3) unbroken glass (for deforming to follow sim), and (4) collider geometry. Sets up the input infrastructure for the deformation steps...
- **File:** tutorials/module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1.md


### module i   week 02   16   point deforming the metal and glass v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oZh_MAnZyaQ
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, post-sim, point-deform, rbd-deform-pieces, destruction, intermediate
- **Summary:** 5m15s lesson. Introduces the new RBD Deform Pieces node (H18.5+) which dramatically simplifies per-piece mesh bending that previously required a complex For-Each capture/deform loop. Metal pre-fracture is subdivided with Divide (brick polygons, 0.05 size) then fed into RBD Deform Pieces with "match proxy by attribute" enabled (cluster attribute keeps each structural section self-contained)....
- **File:** tutorials/module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md


### module i   week 02   17   fixing post sim fix and rbddisconnectedfaces node v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=R-ay-5fX_Os
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** rbd, post-sim, glass, disconnected-faces, blend-shapes, destruction, intermediate
- **Summary:** 10m44s finishing lesson for the Week 2 bus stop project. Covers: splitting geometry by name attribute into metal/glass/wood streams; RBD Disconnected Faces node (set to "delete connected") for progressive glass crack reveal; blending two frozen simulation frames with Blend Shapes + animation + Switch to fix a jarring wood jitter at break moment; final merge of all components with...
- **File:** tutorials/module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md


### module ii   week 01   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Y00rlBFqpxQ
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, cloth, soft-body, tetrahedral, grains, rest-blend, course-intro, intermediate
- **Summary:** 2m46s intro for Module II of the VFX School Renaissance program (Volume 2). Module focus: Vellum simulation — all solver types in one system (cloth, string, hair, tetrahedral soft bodies, grains). Project: crocodile attack sequence. Week 1 sets up: Vellum overview (quick cloth/grain/soft body/string intro), soft body of the human hunter using tetrahedral mesh (H17/18 feature), rest blend for...
- **File:** tutorials/module-ii-week-01-01-introduction-v1-1080p.md


### module ii   week 02   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=161Gcdsi6Nw
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, cloth, tearing, stitching, drape, remesh, course-intro, intermediate
- **Summary:** 1m40s intro for Module II Week 2 of the VFX School Renaissance program. Focus: Vellum cloth simulation for the crocodile attack project. Week covers: draping cloth onto body starting from T-pose (precise fit at sim start), geometry prep (Remesh, groups, constraint setup), cloth tearing (pre-fracturing / pre-cutting), welding and stitching, full drape simulation in Vellum SOP solver, bonus...
- **File:** tutorials/module-ii-week-02-01-introduction-v1-1080p.md


### module ii   week 03   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F2vdSX1Dzgk
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, cloth, soft-body, point-deform, collisions, pin, breaking-welds, course-intro, intermediate
- **Summary:** 1m41s intro for Module II Week 3. This week brings everything together into a complete simulation: soft body hunter + cloth + crocodile collider. Key problem solved: the part of the body inside the croc's mouth is pinned to the croc's animation (not simulated) to avoid unsolvable collision stacking between two colliders. Also covers: VEX for breaking welds/constraints (cloth tearing), Point...
- **File:** tutorials/module-ii-week-03-01-introduction-v1-1080p.md


### module ii   week 04   01   introduction v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SlbMugY762Q
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** grains, vellum, rbd, bullet, rendering, karma, course-intro, intermediate
- **Summary:** 1m55s intro for Module II Week 4 (last week of the VFX School Renaissance program Volume 2). Wraps up the crocodile attack project: (1) Grain source geometry built procedurally from previous sim results (croc + hunter geometry) using a Solver SOP to generate evolving emission volumes; (2) Full grain simulation from scratch in DOPs; (3) High-res upres from low-res grain cache; (4) Gun simulated...
- **File:** tutorials/module-ii-week-04-01-introduction-v1-1080p.md


### module ii   week 01   02   introduction to vellum v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=LKhBUByCqJw
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, cloth, soft-body, struts, string, glue, pin, remesh, beginner-intermediate
- **Summary:** 15m34s hands-on Vellum introduction. Drops a grid, demonstrates Configure Cloth (with Remesh for triangles), Vellum Solver with Torus collider. Shows zero-mass pinning, the mass-from-area gotcha (degenerate triangles after Remesh become zero-mass and freeze), strut soft body constraints (lines bridging geometry to prevent volume collapse), string constraints on a line primitive with partial...
- **File:** tutorials/module-ii-week-01-02-introduction-to-vellum-v1-1080p.md


### module ii   week 01   04   tetrahedral soft bodies v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pxWRHQjHpNk
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, tetrahedral, soft-body, solid-conform, remesh, vellum-source, collisions, intermediate
- **Summary:** 8m50s lesson (Module II Week 1, lesson 4). Sets up soft body simulation for a human hunter character in a crocodile attack scene. Covers: Poly Reduce + Remesh for cleaner input, Solid Conform to convert hollow polygon mesh into tet volume, Vellum Configure Tet Soft Body for FEM-like volume-preserving soft body, Vellum Source node for external geometry input, and using "Use Deforming Geometry"...
- **File:** tutorials/module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md


### module ii   week 01   06   updating the rest blend v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aUkXMjjLT-k
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, rest-blend, bend-sop, bounding-sphere, group, soft-body, intermediate
- **Summary:** 12m37s lesson. Problem: soft body hunter holds arms in an unnatural raised gun position (rest pose). Solution: (1) create arm groups via bounding sphere/bounding object selection, (2) use the Bend SOP to reshape each arm to a natural lowered position, (3) feed this new geometry into a Rest Blend node inside the Vellum DOP on frame 1 of the sim (band + stretch constraint groups). The Vellum...
- **File:** tutorials/module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md


### module ii   week 03   06   breaking welds and constraints v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dfD5FUdMCTc
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5
- **Tags:** vellum, cloth, breaking-welds, vellum-constraint-property, wrangle, break-threshold, caching, vellumio, intermediate
- **Summary:** 11m46s lesson. Final setup before caching the full crocodile attack Vellum sim. Two constraint-breaking techniques: (A) Vellum Constraint Property node inside the DOP — enable "remove" at `$F > 170` to delete the boot attachment constraints and let the boot fly off; (B) Geometry Wrangle on weld streams — animate `break_threshold` using fit() so welds progressively break from frame 140 to 200,...
- **File:** tutorials/module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p.md


### week 01   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9ocqYW1XHk4
- **Author:** The VFX School Archive
- **Houdini Version:** H18+
- **Tags:** rbd, destruction, fracture, voronoi, boolean, plasticity, constraints, active-animated, bridge, intermediate
- **Summary:** 1m58s intro for Week 1 of VFX School's "Manhattan Bridge Destruction Project" course. Topics previewed: import bridge model, analyze and split into simulated/static parts (deformable metal + rigid metal + road). Fracture: road = boolean with custom cutting geo; deformable metal = Voronoi fracture. Configure plasticity and soft constraints (for metal bending behavior). Animate bridge...
- **File:** tutorials/week-01-01-intro-v1-1080p.md


### week 02   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IoxlDdh5OPg
- **Author:** The VFX School Archive
- **Houdini Version:** H18+
- **Tags:** rbd, vellum, cables, constraints, guided-sim, bullet, bridge, destruction, intermediate
- **Summary:** 2m12s week intro by VFX School Archive. Week 2 of the Manhattan Bridge Destruction project. Covers two cable types: - **Horizontal cables**: Heavy, rigid → Bullet sim. Simplified from intricate geo to 4 proxy strands. Hard constraints. Guided Sim workflow (Houdini feature that guides one sim using animated geometry from Week 1 road sim). - **Vertical cables**: Bendy, active → Vellum sim. Proxy...
- **File:** tutorials/week-02-01-intro-v1-1080p.md


### week 03   01   intro v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OnBsOG4SwIU
- **Author:** The VFX School Archive
- **Houdini Version:** H18.5+
- **Tags:** rbd, bullet, cars, scatter, scatter-align, attribute-from-pieces, constraints, suspension, bridge, intermediate
- **Summary:** 1m22s week intro by VFX School Archive. Week 3 of Manhattan Bridge Destruction: vehicle simulation. Topics previewed: import multiple vehicle variations; group into wheels vs bodies for suspension simulation; Scatter Align SOP (H18.5) to place cars on road pointing in correct direction with variation; Attribute From Pieces SOP (H18.5) for attribute propagation; procedural system for removing...
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
- **Houdini Version:** H18+
- **Tags:** rbd, destruction, active-attribute, collision, fracture, animated-noise, constraints, bridge, intermediate
- **Summary:** 10m34s VFX School Archive module. Part of Manhattan Bridge Destruction Week 1. Covers RBD Configure SOP setup, collision geometry visualization, and creating an animated `active` attribute that propagates from the center out to the edges over time (simulating progressive destruction). The active boundary is a box with Mountain noise deforming its face positions (flow noise, animated height...
- **File:** tutorials/week-01-11-rbd-configure-v1-1080p.md


### week 02   03   starting the guided sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9qkYzPC9IKM
- **Author:** The VFX School Archive
- **Houdini Version:** H17.5+
- **Tags:** rbd, guided-sim, bullet, constraints, cables, hard-constraints, active-attribute, bridge, intermediate
- **Summary:** 6m47s VFX School Archive module. Part of Manhattan Bridge Destruction Week 2. Sets up horizontal cable simulation with Bullet + Guided Sim workflow. Creates name attributes, hard constraints between cable blocks (no plasticity, stiff behavior), RBD Configure with inactive regions at bridge towers (boxes at ±19 X). ABD Bullet Solver with Guided Simulation tab: imports Week 1 bridge simulation...
- **File:** tutorials/week-02-03-starting-the-guided-sim-v1-1080p.md


### week 02   04   finishing the horizontal cable sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ykTr02tft_k
- **Author:** The VFX School Archive
- **Houdini Version:** H17.5+
- **Tags:** rbd, guided-sim, bullet, cables, air-resistance, file-cache, strength-attribute, bridge, intermediate
- **Summary:** 9m3s VFX School Archive module. Continuation of Week 2 horizontal cable sim. Fixes constraint popping by disabling "Remove Intro-Guide Constraint" in the Guided Sim constraints tab. Introduces `weak` group: wrangle sets `f@weak=4` on all proxy points, then `f@weak=0` for points inside the active/falling zone (object-merged from Week 1 active boundary). Feeds `f@weak` into Guided Sim strength...
- **File:** tutorials/week-02-04-finishing-the-horizontal-cable-sim-v1-1080p.md


### week 02   07   starting the vellum sim v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cecNdA8cLTo
- **Author:** The VFX School Archive
- **Houdini Version:** H17.5+
- **Tags:** vellum, cables, cloth, constraints, pin, rest-length, tension, bridge, intermediate
- **Summary:** 8m7s VFX School Archive module. Sets up Vellum cloth sim for vertical bridge cables. Key parameters: rest length scale=0.8 (shorter than actual → under tension → spring up violently when released); compression stiffness=max; bend stiffness=1M; pin group (top of cables) + match animation; Vellum Attach to Geometry (cables → bridge road, group="attach", breakable at threshold 0.01). Fix for...
- **File:** tutorials/week-02-07-starting-the-vellum-sim-v1-1080p.md


### week 02   08   setting the strong constraints and the breaking threshold v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9TNDsfFNoq4
- **Author:** The VFX School Archive
- **Houdini Version:** H17.5+
- **Tags:** vellum, cables, constraints, breaking, timescale, file-cache, vdb, bridge, intermediate
- **Summary:** 12m37s VFX School Archive module. Final step of vertical cable Vellum sim. Brings in all cables (disable blast node). Creates "strong" constraint group for cables near non-falling bridge section (conservative VDB selection + Group Promote to primitives). Inside Vellum Solver: two Vellum Constraint Property nodes — one animates break threshold for "attach" group (strengthens then weakens over...
- **File:** tutorials/week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p.md


### week 04   06   cull by speed v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UFrvmv0rwQI
- **Author:** The VFX School Archive
- **Houdini Version:** H18+
- **Tags:** particles, rain, vex, wrangle, cull, velocity, speed, file-cache, beginner
- **Summary:** 7m0s VFX School Archive module. Part of Week 4 rain particle sim on the Manhattan Bridge. Loads cached point sim, adjusts viewport display (pixels or small points, size 1.5). Discovers points flying upward from bridge geometry collision artifacts. Fix: Attribute Wrangle after file cache reads velocity length as speed; `removepoint` for points exceeding threshold (ch("speed_cull") ≈ 10-20)....
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
- **Houdini Version:** H18+
- **Tags:** flip, fluid, viscosity, surface-tension, meshing, vdb, rendering, arnold, beginner
- **Summary:** 1m42s week introduction by VFX School Archive. Week 4 of the "Tabletop Course": simulates a strawberry colliding with poured milk. Topics previewed: animated FLIP emitter geometry; viscosity and surface tension (important for milk); VDB meshing for high-quality milk surface; Arnold renderer with complex strawberry shader (subsurface, transparency, noise-driven roughness map, SSS) and milk SSS...
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
- **Houdini Version:** H18+
- **Tags:** velocity, attribute-transfer, deformation, trail, vex, wrangle, beginner
- **Summary:** 7m30s VFX School Archive module lesson. Part of a blueberry/yogurt tutorial series. Shows how to derive velocity from animated geometry using the Trail SOP, transfer that velocity to a deformable grid as color (via Attribute Transfer + Vector to Float), then use an Attribute Wrangle to displace grid points along Y proportional to the velocity-derived color. Creates a ch() parameter slider for...
- **File:** tutorials/w02-05-deforming-with-velocity-v1-1080p.md


### w03   04   adding viscosity v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9N9CavpgoB4
- **Author:** The VFX School Archive
- **Houdini Version:** H18+
- **Tags:** flip, fluid, viscosity, simulation, chocolate, beginner
- **Summary:** 4m45s VFX School Archive module. Part of a chocolate-over-ice-cream FLIP sim tutorial. Shows how to add viscosity: enable in FLIP Solver viscosity tab, set value in FLIP Object Physical tab (100 for chocolate, 10000 for clay). Mentions importing viscosity attributes from outside (multi-fluid workflow for later). Demonstrates velocity-based color visualization in guides. Sets Volume Limits to...
- **File:** tutorials/w03-04-adding-viscosity-v1-1080p.md


### w03   11   meshing v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H56dPbE3S2E
- **Author:** The VFX School Archive
- **Houdini Version:** H18+
- **Tags:** flip, meshing, vdb, particles, attribute-transfer, color-ramp, beginner
- **Summary:** 7m49s VFX School Archive module. Part of a chocolate-over-ice-cream FLIP sim tutorial. Meshes cached FLIP particles using the VDB workflow: VDB from Particles (requires small voxel size ~0.025 and radius scale ~1 — don't go below 1.5 without smoothing planned) → VDB Smooth SDF → Convert VDB. Colors particles by viscosity attribute (ramp, range 0–250, brown tones for different chocolate...
- **File:** tutorials/w03-11-meshing-v1-1080p.md


### w04   11   viscosity and surface tension v1 1080p
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1yb3mindncw
- **Author:** The VFX School Archive
- **Houdini Version:** H18+
- **Tags:** flip, fluid, viscosity, surface-tension, jitter, kernel, sub-steps, simulation, beginner-intermediate
- **Summary:** 12m32s VFX School Archive module. Part of the Week 4 strawberry-collides-with-milk simulation. First demonstrates viscosity + surface tension on a simple cube DOP test, then applies those settings to the main strawberry+milk sim. Key concepts: FLIP Source jitter seed `$F` for per-frame variation; surface tension prevents square-shaped splashes (makes sphere/circle); viscosity holds fluid...
- **File:** tutorials/w04-11-viscosity-and-surface-tension-v1-1080p.md

### Effective TD
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c9qw6hVstEA
- **Author:** Houdini.School
- **Houdini Version:** H18+
- **Tags:** flip, fluid, viscosity, surface-tension, jitter, kernel, sub-steps, simulation, beginner-intermediate
- **Summary:** 12m32s VFX School Archive module. Part of the Week 4 strawberry-collides-with-milk simulation. First demonstrates viscosity + surface tension on a simple cube DOP test, then applies those settings to the main strawberry+milk sim. Key concepts: FLIP Source jitter seed `$F` for per-frame variation; surface tension prevents square-shaped splashes (makes sphere/circle); viscosity holds fluid...
- **File:** tutorials/effective-td.md


### Effective TD (intro v1)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7NejsDXzxXI
- **Author:** Houdini.School
- **Houdini Version:** unspecified
- **Tags:** hda, python, pipeline, td, ui
- **Summary:** Jesper introduces himself (10+ years in VFX at companies including DNEG and Framestore, has taught at schools in Vancouver, currently writes pipelines at Raw Power Games) and previews the "Effective TD" course. The course covers the role of a technical director, emphasizing data management and optimization: starting with optimizing data for caching to improve read/write speed, then wrapping...
- **File:** tutorials/effective-td-7nejsdxzxxi.md


### Animate Gaussian Splats with Houdini - Free Tutorial + Scene Files
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=MqtMQl8DtjQ
- **Author:** SOP Cemetery
- **Houdini Version:** Houdini 21
- **Tags:** gaussian-splats, kinefx, apex, rigging, animation, karma, point-deform, spherical-harmonics, advanced
- **Summary:** SOP Cemetery (Bogdan) 81-min tutorial: animate a Gaussian splat fly in Houdini 21. Plugin needed: G-SOP (GitHub) for GS import/bake/deform nodes (unlocked versions included in project files — G-SOP install not required). Pipeline: (1) Import fly .ply → Bake GS Splat (compute spherical harmonics = split SH into RGB components) → transform to Y-up. (2) Manual segmentation: select points by hand...
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
- **Summary:** 68m35s SideFX HOUDINI HIVE talk by Magnus Møller and Jesper Andkjær of Studio Tumblehead (14 artists total, incl. programmer Søren and TD Remy) presenting their full Houdini production pipeline developed for the short film *Turbulence* (H20/20.5, made with SideFX). Covers the complete asset workflow (modeling from NomadSculpt/ZBrush/QuilVR, blendshapes via GoZ or SkullThings, LookDev with...
- **File:** tutorials/how-to-make-a-short-film-in-houdini-magnus-møller-jesper-andkjær.md


### The Only HAIR GROOMING Tutorial You Need! (Houdini for Artists)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rVogGr7f0Cg
- **Author:** June Chevalier
- **Houdini Version:** Not specified (H20–H20.5 UI)
- **Tags:** sop, curves, attributes, procedural, vex, wrangler, modelling, beginner, intermediate
- **Summary:** An 85-minute beginner-friendly tutorial by June Chevalier covering the full pipeline for character hair grooming in Houdini. Starting from mesh import and unit-scale correction, the tutorial builds a density mask, VDB collision volume, sculpted guides, and generated hair strands, then layers in the three key realism drivers: layered clumping (primary, secondary, tertiary), guide-process noise...
- **File:** tutorials/the-only-hair-grooming-tutorial-you-need-houdini-for-artists.md


### Why you need to learn vex in Houdini #1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ntf3zMAez50
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vex, surface-deform, cluster, minpos, flood-fill, croissant, spiral, vex-showcase
- **Summary:** Starting from a pre-sliced croissant cross-section (built earlier with a bunch of extrusions and a Sculpt node, covered in a prior video), the interior detail begins by blasting away the filled polygons and resampling the resulting simple boundary curve. The core trick is building a "rest geometry" spiral: a unit circle sampled with **`sampleCircleUniform()`** by manipulating the U parameter...
- **File:** tutorials/why-you-need-to-learn-vex-in-houdini-1.md


### Chocolate break rig and Liquid Stretch in Houdini Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=f5vt8n8CB-U
- **Author:** cgside
- **Houdini Version:** any modern (H18+, uses Exoside QuadRemesher)
- **Tags:** rbd, procedural, vex, quadremesh, fracture, advanced
- **Summary:** Starts from an imported chocolate-bar mesh, quad-remeshed and locked for a stable base. Builds an interior "shell" by branching off a Shrink Wrap–style inward-offset copy (peaked inward, snapped via a min-position VEX pass, smoothed, and normal-reversed) merged back with the original to give the bar real wall thickness. The break pattern comes from a **feedback loop of Clip nodes**: each...
- **File:** tutorials/chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson.md


### Houdini techniques to improve your level
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=zWlJ8QLkFH4
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, flip, simulation, uv, python, procedural, tips, advanced
- **Summary:** For the drip effect: the bottle body is Clipped to carve out an emitter region, **Thickened** slightly to create a thin shell of source points (with only the surface enabled on FLIP Source, not the VDB/SDF), and a wrangle sets each drip's initial velocity/position. Drip origin points are generated by converting the clip boundary edges to a line and Scattering a handful of points (~9, tuned via...
- **File:** tutorials/houdini-techniques-to-improve-your-level.md


### Scissor Lift rig in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QPiEZM1o-ME
- **Author:** cgside
- **Houdini Version:** 21.0
- **Tags:** rig-doctor, ik-chain, point-transform, matrix, kinefx, scissor-lift, procedural-rigging
- **Summary:** The rig starts from a centered 2-point Line (points enumerated with an `ID` attribute), deformed into a zigzag with a wrangle that offsets alternating points' X position (`(ptnum % 2) * amplitude`, zero-centered via `×2−1`) — a simple, loop-free way to build the classic scissor pattern. Points are grouped in threes via `pointcut` and an exploded view to visualize the pairing, then the...
- **File:** tutorials/scissor-lift-rig-in-houdini.md


### Coin spin | Sops vs Vex vs OpenCL
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AGTOukqBmhU
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** vex, opencl, matrix, uv, animation, packed-primitives, expert, advanced
- **Summary:** An explicitly educational, three-difficulty-level comparison video. **Part 1 — reset transforms**: fixes a Sketchfab-scanned coin's inverted/offset USD "ST" UVs (renamed to `uv`, Y-flipped and offset via a wrangle), then centers and orients the coin three different ways: (easy) native Transform + Match Size nodes; (medium) a single VEX wrangle using bounding-box center subtraction and a...
- **File:** tutorials/coin-spin-sops-vs-vex-vs-opencl.md


### Essential Procedural Techniques in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JMfMxHi48Zs
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, uv, opencl, mpm, simulation, materials, shaders, karma, procedural, tips, advanced
- **Summary:** **Peeling effect:** starting from a deformed QuadSphere ("potato" shape), a spiral curve is aligned to the centroid and reprojected onto the potato surface; the potato's own normals are copied to a `pscale`/orient-style attribute so the spiral can be Swept using those normals (without this, the sweep result is a broken mess). The subdivided potato gets a Distance-from-Geometry mask relative to...
- **File:** tutorials/essential-procedural-techniques-in-houdini.md


### Camera Match tool for Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NkVT9NtRMk0
- **Author:** cgside
- **Houdini Version:** H21
- **Tags:** camera, photogrammetry, hda, plugin, image-based-modeling, intermediate
- **Summary:** A Patreon-shared HDA demoed across three vanishing-point scenarios: two-point perspective (most common — one axis per horizontal vanishing point, with the vertical assumed straight), one-point perspective (focal length must be eyeballed rather than solved, since one vanishing point alone under-constrains the solve), and three-point perspective (e.g. a tall building shot from below, where the...
- **File:** tutorials/camera-match-tool-for-houdini-21.md


### Layered Textures in Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GQMsl6TiFXY
- **Author:** cgside
- **Houdini Version:** 21
- **Tags:** karma, materials, shaders, mtlx, triplanar, cops, python, uv, procedural, environment, intermediate
- **Summary:** **The LayerX node itself:** a native (not subnet-based) MaterialX node compiled specifically for Karma, exposing a stack of enable/disable layers, each with its own **blend mode** (Normal, Overlay, Multiply, etc.) and optional **alpha** input for masking — usable on base color, roughness, and even displacement inputs. **Model prep:** starting from a previously-modeled water tower, most...
- **File:** tutorials/layered-textures-in-karma.md


### RBD Procedural Animations in Houdini | Mardini 2026
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ITq2EBJ5nIw
- **Author:** cgside
- **Houdini Version:** 21.0.303
- **Tags:** rbd, glue-constraints, voronoi-fracture, convex-hull-collision, karma-xpu, mardini, barrel, animation
- **Summary:** The barrel's thick glass wall is built by first computing a mask via **distance-along-geometry** (bottom to top, normalized), converting it to Mono for equalized normals, then blending point normals (blurred) with the mask-driven Mono normals via a channel ramp along Y — this custom-normal approach avoids the visible self-intersection artifacts that a naive Poly Extrude produces at the...
- **File:** tutorials/rbd-procedural-animations-in-houdini-mardini-2026.md


### Procedural Food in Houdini | Mardini 2026
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VjX9v92PJNU
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** volume-cloth, rbd, flip, packed-primitives, matrix, cops, food, mardini
- **Summary:** The French toast starts as a Box, using inverted-normal-comparison selections (`abs(N.y) > abs(N.y)`) to separately grab the top and sides, an alternating-vertex Poly Bevel for the crust edges, then Poly Extrude with **thickness** (instead of inset) to get evenly-spaced edge segments before a UV unwrap/layout. A Remesh + a **Volume Cloth** simulation (edge-length scale, pinned-point group...
- **File:** tutorials/procedural-food-in-houdini-mardini-2026.md


### Creating Cliff Shapes in Cops | Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=62Mo7udZM_o
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** cops, procedural, texturing, noise, terrain, environment, intermediate
- **Summary:** Starting from a `polygon`/regular-polygon COP shape (5-sided base), the tutorial builds up a rock-face pattern by blending an ISO-distance-inverted shape with a Cube 3D COP-constant, then repeatedly layering **tileable 2D noises** (never 3D noise, which wouldn't tile without mesh-based position/`P`/`uv` attributes) through **Multi-Directional Warp** and **Directional Warp** nodes to distort...
- **File:** tutorials/creating-cliff-shapes-in-cops-free-lesson.md


### Volume rays in Cops for Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nCS6sy53_aw
- **Author:** cgside
- **Houdini Version:** 21.0.622
- **Tags:** cops, hda, god-rays, luma-key, compositing, matrix-color-transform, tool-development, houdini-21
- **Summary:** **Volume Rays** works by first selecting the brightest areas of the source image via a **luminance-range** threshold (a luma-key-style operation), then repeating/streaking those bright pixels along a direction using an internal **iteration** count (how many times the pixels are repeated) combined with a **step scale** multiplier that controls the spacing/distance of each repetition — pushing...
- **File:** tutorials/volume-rays-in-cops-for-houdini-21.md


### Creating assets from default geometry in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oEIXFY-Kxdk
- **Author:** cgside
- **Houdini Version:** 21
- **Tags:** modeling, rigging, vex, procedural, skeleton, deformation, intermediate
- **Summary:** Starts from a plain open-ended tube, equalizes its ragged end edge with a hand-written VEX wrangle that projects points onto a local axis (via oriented-bounding-box transform + dot product), then polyfills and unrolls a skeleton from the mesh using **Skeleton from Mesh**-style resampling. The skeleton is posed apart (to avoid finger-intersection during capture), captured onto the mesh via...
- **File:** tutorials/creating-assets-from-default-geometry-in-houdini-21.md


### Orient UVS like a PRO in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eqXFo0pxdXc
- **Author:** cgside
- **Houdini Version:** 21
- **Tags:** uvs, python, hda, matrices, oriented-bounding-box, vex, dihedral, procedural-uvs
- **Summary:** Building on an earlier, simpler "Orient UVs Up" tool that failed on many real-world meshes, this HDA reliably auto-orients any set of UV islands right-side-up regardless of scramble. It works by giving every island a unique ID (via UV-seam split + boundary group + connectivity, since plain UV connectivity can merge overlapping islands), computing a `position.y` gradient in UV space per island...
- **File:** tutorials/orient-uvs-like-a-pro-in-houdini-21.md


### Basic Procedural Texturing with Cops in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AB9rwjcX0Xg
- **Author:** cgside
- **Houdini Version:** Houdini 21 (Copernicus/COPS)
- **Tags:** cops, texturing, procedural, materials, triplanar, mardini, normal-map, intermediate, advanced
- **Summary:** A warts-and-all, full-workflow walkthrough (not a polished-result tutorial) texturing a previously-modeled asset (a Mardini pen/vessel) entirely inside COPS. Covers baking a full utility-map set from geometry (important gotcha: bake from a *subdivided* low-poly proxy, or curvature/displacement bakes show visible low-poly faceting), fixing UV-seam bleeding on every baked map at once via...
- **File:** tutorials/basic-procedural-texturing-with-cops-in-houdini-21.md


### Roasting my Houdini Setups #1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rvDsbo3slXc
- **Author:** cgside
- **Houdini Version:** 21.0.303
- **Tags:** for-loop-optimization, capture-by-proximity, labs-file-cache, rig-doctor, wedge, retrospective, best-practices
- **Summary:** The first old setup builds a rig from a sphere: originally, extracting a clean "every-other-vertex" edge group required a for-loop iterating over per-section IDs, because promoting a raw group-by-range selection to edges also picked up unwanted collapsed-to-a-point selections at the poles. The improved approach: select all vertices with a **neighbor count less than 5** (isolating vertices away...
- **File:** tutorials/roasting-my-houdini-setups-1.md


### Scatter shapes in cops randomly without overlap
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bTA8XwTEcRg
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** cops, point-relax, uv-gradient, tiling, matrix, stamping, rock-material, seamless
- **Summary:** Four rock variations are modeled in SOPs, masked out individually (a subnet used only because Cops lacks native loops — the subnet does the per-variation math and outputs each rock's mask as an image layer), then imported into Cops via Geo-to-Layer, Cable Pack, and stamped with the built-in Stamp Cop — which works fine for a small, systematic set but breaks down (heavy overlap) as soon as...
- **File:** tutorials/scatter-shapes-in-cops-randomly-without-overlap.md


### Procedural Environments in Houdini | Patreon February '26 Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F_xggmIONZ4
- **Author:** cgside
- **Houdini Version:** 21.0
- **Tags:** cops, openCL, rip-mask, edge-smooth, divide, brick-wall, houdini-21, patreon-course
- **Summary:** The ripping/edge-damage effect is built entirely in a Cop network using **OpenCL** since it's simple enough not to need the default node bindings: a bound `edge` float parameter is multiplied by the image's X resolution to get a pixel-space edge threshold, then a mask is grown from the left (`pixel.x < edge`) and right (`pixel.x > xres - edge`) sides of the image using simple threshold...
- **File:** tutorials/procedural-environments-in-houdini-patreon-february-26-free-lesson.md


### Direct vs Procedural in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Quj03TwHAN4
- **Author:** cgside
- **Houdini Version:** 20
- **Tags:** modeling, vex, uv, procedural, hard-surface, tips, cops, intermediate
- **Summary:** Walks through when procedural selection beats manual grouping and vice versa. Sign-of-position wrangles replace manual top/bottom group creation on a symmetric box; vertex-index-modulo wrangles select every-other edge for beveling; attribute-driven bevel widths let one Polybevel vary per group instead of needing multiple nodes; a Poly Extrude "thickness ramp" trick (instead of plain Inset)...
- **File:** tutorials/direct-vs-procedural-in-houdini.md


### Think Procedural Think Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=TWQvmqhRX3M
- **Author:** cgside
- **Houdini Version:** 21.0
- **Tags:** brick-wall, growth-solver, pcopen, matrix, pack-inject, edge-damage, procedural-modeling, sop-solver
- **Summary:** The wall starts from a single Line (2 points) copied 24 times, using **Attribute Adjust Float** (a relatively obscure but powerful node) driven by the primitive's `copy_name`/`copyname` attribute (remapped 0–1 via `end-primitives-1`) to manipulate `P.y` (overall wall height profile) and `P.x` (brick-course width profile, applied only to alternating "outer" points via a Sort-by-Y-and-reverse...
- **File:** tutorials/think-procedural-think-houdini.md


### Double Sided Leaf Animation using Cops in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yeA_0tL3GlU
- **Author:** cgside
- **Houdini Version:** 21
- **Tags:** vex, rigging, animation, cops, procedural, skeleton, shaders, texturing, noise, advanced
- **Summary:** Starts by tracing a leaf's alpha texture into mesh geometry (Trace SOP) and moving it into UV space (0-1) for easier COPs work later. The hardest part is fully procedural landmark detection: since curvature analysis on the raw boundary is noisy, the mesh is duplicated into a heavily blurred "rest" version (position stored as a `rest` attribute, blurred, then swapped into `P` via a rest/current...
- **File:** tutorials/double-sided-leaf-animation-using-cops-in-houdini-21.md


### Matrix color transform in cops for Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZDlL81gmafE
- **Author:** cgside
- **Houdini Version:** 21
- **Tags:** cops, vex, opencl, python, color-management, cgi-integration, hda, advanced
- **Summary:** The workflow: drop a **Matrix Color Transform** COP, feed it a cropped-down HDRI image containing a physical color chart (chart region pre-extracted in Affinity Photo), then enter the node's custom **Python States** tool (Houdini 21's new COPs Python state support) — a fully custom UI with working undo/redo — to drag-align four corner handles of a rendered reference color-chart overlay onto...
- **File:** tutorials/matrix-color-transform-in-cops-for-houdini-21.md


### Procedural Duct Tape in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=D6449n2Pvcc
- **Author:** cgside
- **Houdini Version:** 21.0.359
- **Tags:** wrinkle-deformer, uv-flatten, area-scale-factor, xyzdist, object-merge, tape, procedural-modeling
- **Summary:** The base pipe is modeled with a bent tube (Poly Hinge targeting primitive 0, moved/rotated via bounding-box-relative position and mirrored for the other end). The tape itself starts as a Spiral (explicit radius scale matched to the tube, ~4.5 turns, slightly overlapped) Match-Sized onto the left side of the pipe, then Swept into a ribbon (rolled -90°, width ~0.115) with computed UVs. Rather...
- **File:** tutorials/procedural-duct-tape-in-houdini.md


### Tips and Tricks to level up your Houdini Skills
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DV0ABu_-yvc
- **Author:** cgside
- **Houdini Version:** 21.0.359
- **Tags:** rest-attribute, clip-by-attribute, uvdist, pack-inject, rbd, cops, sushi, tips-and-tricks
- **Summary:** The first tip splits primitives in half at random orientations using rest-space cutting: after isolating target primitives, a per-primitive random-direction vector is built with `sampleDirectionUniform()` seeded by primitive number plus a random offset (giving a repeatable, seed-controllable "each 90 degrees" random rotation), then a **rest attribute** is created by getting each primitive's...
- **File:** tutorials/tips-and-tricks-to-level-up-your-houdini-skills.md


### Procedural Materials in Houdini 21 | Patreon December '25  - Free Lesson
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=iZwfnJGQUlI
- **Author:** cgside
- **Houdini Version:** 21.0.512
- **Tags:** connectivity, for-each, uv-flatten, xyzdist-alternative, cobblestone, houdini-21, patreon-course, sops-to-cops
- **Summary:** The source geometry is a wavy S-curve-like shape (this is a free excerpt from a paid monthly Patreon lesson on generating a Cops/SOPs tiling pattern in Houdini 21). Since not everyone has access to the Labs Voronoi Fracture SOP used for a quick reference result, the tutorial builds an equivalent from scratch: first populate **Connectivity** on primitives (naming the class attribute "class"),...
- **File:** tutorials/procedural-materials-in-houdini-21-patreon-december-25---free-lesson.md


### Procedural environment assets in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SwtUCds8UCY
- **Author:** cgside
- **Houdini Version:** 21.0
- **Tags:** packed-primitives, transform-attribute, uv-flatten, primitive-sort, tunnel, level-environment, houdini-21, patreon-course
- **Summary:** The tunnel starts from a Tube (Z axis, 8 rows, 50 columns) that gets grid-expression-based groups removed/flattened to create an open, prick-shaped cross-section: `P.y < threshold` group expressions isolate a "bottom" strip, a second lower threshold isolates the part to Blast away, and a Group-From-Match-With-Boundary (points, matched against the bottom group) plus a "not bottom" variant,...
- **File:** tutorials/procedural-environment-assets-in-houdini-21.md


### CGI Integration | The Indie Way with Houdini(USD) and Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RchQ9K5QXtI
- **Author:** cgside
- **Houdini Version:** H21 (Solaris/Karma XPU)
- **Tags:** solaris, usd, karma, rbd, tops, camera, vfx-integration, aces, color-pipeline, advanced
- **Summary:** An end-to-end "poor man's VFX integration" workflow using consumer gear (phone footage shot in Log) and free/trial tools. **DaVinci Resolve** (free version): imports Log footage, uses Color Space Transform twice — once to convert Log→ACES linear (for compositing/3D work, no tone mapping) and once ACES→sRGB/Rec.709 (for a display-referred JPEG sequence used in tracking) — exporting both an...
- **File:** tutorials/cgi-integration-the-indie-way-with-houdiniusd-and-nuke.md


### New Houdini Course  - Procedural Product Shots | Part 1 Free
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FxrSPbnI3tI
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vex, uv, procedural, product-viz, course, intermediate
- **Summary:** The base starts as a 1x1 **Grid** (2x2, no subdivisions) with points **Sorted** so point 0 lands in a specific corner, then a `pscale` **Attribute Adjust Float** gives that corner a bigger bevel value (0.5) versus the rest (0.2 default) via an "all but point 0" attribute expression — feeding a **Peak/Bevel-based-on-points** pass (1 amount, 8 divisions, scale-by-attribute) for an asymmetric...
- **File:** tutorials/new-houdini-course---procedural-product-shots-part-1-free.md


### Tips and tricks in Houdini 21
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gv_gXOSjCN0
- **Author:** cgside
- **Houdini Version:** 21.0.300
- **Tags:** vex, matrix, look-at, gradient, uv-flatten, pick-node, houdini-21, normal-map, fork
- **Summary:** For a book-lamp animation rig, band deformation is applied to curve-oriented normals (via Oriented-Along-Curve), but since the normals themselves don't follow the resulting bend, the fix is computing a **look-at-based transform matrix** from the curve attributes first (so the transform bends correctly with the geometry), then extracting any needed axis vector by multiplying a unit axis vector...
- **File:** tutorials/tips-and-tricks-in-houdini-21.md


### Optimizing Baked Trees with Instancing in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0C8ek1aDe8o
- **Author:** cgside
- **Houdini Version:** 19.5.590
- **Tags:** instancing, optimization, vex, matrices, opacity-to-mesh, hda, vegetation, python, usd, solaris
- **Summary:** Baked, high-poly assets (e.g. from MaxTree/Megascans) with opacity-mapped leaves are expensive to convert to real mesh at full resolution (millions of points). Instead of converting every leaf, the video extracts one leaf, zeroes its transform, converts it once, then reconstructs a per-leaf transform matrix (via `nearpoint()`, `clip`, `convertline`, `resample`, `orientalongcurve`, and...
- **File:** tutorials/optimizing-baked-trees-with-instancing-in-houdini.md


### Handy Houdini Tips | Vellum, UVS, Modeling and More
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=h6wt3KJy2W4
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, uv, vellum, modeling, procedural, animation, tips, intermediate
- **Summary:** **Slerp animation:** a packed object carrying two transforms (current position + target position, both extractable as matrices from input 1 and input 2) is animated by computing a 0-1 blend value from `fit(time, 0, 1, 0, 1)`, then using **`slerp()`** (Lerp for matrices) to interpolate between the two position matrices using that blend factor. A separate rotation-only angle (a spare parameter,...
- **File:** tutorials/handy-houdini-tips-vellum-uvs-modeling-and-more.md


### Procedural Favela in Houdini  | Tips and Tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Nmnf_3mp1OU
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vertex-selection, skin, wrinkle-deformer, cops, tile-pattern, height-blend, architecture, favela
- **Summary:** The house starts from a box with primitives sorted by Y and reversed so primitive 0 is reliably the top face — this predictable indexing lets later selections stay procedural rather than manual. A "corner" selection (for later downward transform) is made via a point wrangle constrained to the top-face group, selecting only points on the negative X axis. For selecting alternating roof edges,...
- **File:** tutorials/procedural-favela-in-houdini-tips-and-tricks.md


### Houdini 21 | Opacity vs Stencil vs Geometry
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ha85low9Bmo
- **Author:** cgside
- **Houdini Version:** 21
- **Tags:** karma, solaris, lops, vdb, scattering, instancing, materials, vegetation, benchmark, intermediate
- **Summary:** Four identical leaf-scatter setups (~6000 packed instances) are benchmarked on the same demo scene. Baseline geometry (flat cards, no opacity map, no real cutout shape) rendered in **26s** (later re-verified closer to ~15-16s after the author suspected a measurement fluke on the first run). Switching the material to use an **opacity map** (real leaf-shaped alpha cutout) balloons render time to...
- **File:** tutorials/houdini-21-opacity-vs-stencil-vs-geometry.md


### Daily dose of Houdini Tips | Sweep secrets, opencl textures and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1QTfNMlvF1E
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, opencl, vellum, animation, procedural, texturing, cops, tips, intermediate
- **Summary:** Covers four independent tricks from one project. First: to mesh an animated curve/rig (the straw's accordion joints) instead of using Skin, connect the curve only to Sweep's *second* input with default settings — remembering to close the implicit backbone or the mesh stays open. Second: to fake a stop-motion "pop" on the accordion folds, drive a simple line-based deformation with Attribute...
- **File:** tutorials/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more.md


### Dusty Bottles - Bridging procedural workflows in Houdini and Solaris
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=CHySFnWfKLk
- **Author:** cgside
- **Houdini Version:** 20
- **Tags:** modeling, vex, vdb, tops, solaris, lops, karma, materials, shaders, procedural, usd, advanced
- **Summary:** The bottle body starts as a revolved profile (deliberately computing but not using default revolve UVs, since a manual UV-flatten + Rectify pass gives cleaner top/bottom control), then gets poly-extruded and subdivided for thickness. The neck/foil "top part" uses alternating-vertex edge selection converted to curves, randomized per-curve length/pscale via VEX curve attributes (a Houdini 20...
- **File:** tutorials/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris.md


### Making Trash in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KCy4Sw3nbcQ
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, rbd, vellum, vdb, vex, uv, procedural, environment, advanced
- **Summary:** **Crushed can:** starting from a revolved/QuadRemeshed profile curve (reused from a prior tutorial's scan asset) with UVs picked via a saved seam group, the can is Scattered with 500 points and **Voronoi Fractured** to generate crushable pieces plus RBD glue constraints; the top rim points are pinned (selected via **Relative Point Bounding Box**) so the can's top stays rigid while the body...
- **File:** tutorials/making-trash-in-houdini.md


### Houdini tips to save the day
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lT0b8D6LmtM
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, uv, procedural, modeling, deformation, tips, advanced
- **Summary:** **Inside/outside mask without network access:** given only a finished geometry (no access to how it was built), Connectivity assigns a `class` per piece, Extract Centroid + Group by class gets one representative point per piece, and **Orient Along Curve** computes a custom per-piece normal saved under a **different name** (`_N`, not `normal`) so it doesn't collide with the mesh's real normals;...
- **File:** tutorials/houdini-tips-to-save-the-day.md


### No VEX challenge #1   Procedural Water Tower
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NxWpxFDaSJE
- **Author:** cgside
- **Houdini Version:** Not specified (H20-era UI)
- **Tags:** procedural-modeling, no-vex, vops, sweep, groups, point-clouds, textures, cops, texture-projection, uv, hard-surface, beginner-friendly
- **Summary:** The tank body is built from a tube whose ends are split into boundary groups, then reshaped into a domed sphere-like cap and a tapered cone top via centroid-pivot Transforms and copy/scale-to-zero "cone from ID" tricks, skinned back together into one continuous shell. A circular curve (from an Object Merge of the base tube) becomes the observation platform via Transform+Extrude, with...
- **File:** tutorials/no-vex-challenge-1-procedural-water-tower.md


### Procedural Boat in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=050av2q2ihg
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** channel-ramp, skin, uv-rectify, connectivity, uv-sample, procedural-modeling, boat, hull
- **Summary:** The hull starts from a Line (Z axis, 40-point resample) deformed along Y with a channel ramp to define the base silhouette, with normals computed along X. Side profile curves are built by blasting the first/last points of that base curve, resampling, Sweeping (ribbon, single column) with a width/scale-ramp falloff for curvature, then re-orienting (Orient Along Curve, Y axis) and displacing...
- **File:** tutorials/procedural-boat-in-houdini.md


### Quick object merge with Python in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fDV8SQegEDc
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** python, hou-module, shelf-tool, object-merge, hotkey, tool-development, workflow-automation
- **Summary:** The script grabs the current selection with `hou.selectedNodes()[0]`, then creates an Object Merge node as a child of the selected node's parent (`selection.parent().createNode("object_merge")`). To avoid the new node overlapping the source, it reads the selected node's position via `.position()` and offsets the new Object Merge by `-1` in both X and Y (`hou.Vector2(sel_pos[0]-1,...
- **File:** tutorials/quick-object-merge-with-python-in-houdini.md


### Vex Quick Tips #4 - Pineapple Crown
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oDXQsMo2aaQ
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vex, quick-tips, golden-angle, quaternion, look-at, transform-attribute, sweep, pineapple, plant-generator
- **Summary:** Leaves are placed by copying two-point lines onto a circle of instance points, with p-scale shrinking progressively along a resampled base line (cascading effect). A **class** attribute (point number) tags each leaf for later per-piece transforms. Leaves are first bent upward using a cross product between the surface normal and the Y axis (an "up" vector), then rotated via `qrotate()`; p-scale...
- **File:** tutorials/vex-quick-tips-4---pineapple-crown.md


### Interactive Tools with Houdini Python States | Draw pts on geo
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ARJFJC79k3k
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** python, hda, procedural, tips, advanced
- **Summary:** The HDA is built around a multi-parm **Add** SOP (one entry per drawn point) wrapped in a Subnet and converted to a Digital Asset with the "Interactive" template plus "On Draw" and "Handle States" enabled. By default, the state's built-in interaction intersects against the flat construction plane/grid — not what's wanted, since points should snap onto the actual input geometry. The fix...
- **File:** tutorials/interactive-tools-with-houdini-python-states-draw-pts-on-geo.md


### Creating a Procedural Rock Wall with Houdini | Patreon May - Trailer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mljby-SKlUI
- **Author:** cgside
- **Houdini Version:** not specified (trailer only)
- **Tags:** tops, uv, packing, cops, solaris, karma, mardini
- **Summary:** The trailer verbally outlines what the full paid course will cover, without demonstrating any of it on-screen: generating rock variations via a **TOPs network**, building both low-poly and high-poly ("ipoly") versions, procedurally generating UVs, assembling the wall with "a few techniques," using **packed instances** to swap the low-poly stand-ins for high-poly geometry at render time,...
- **File:** tutorials/creating-a-procedural-rock-wall-with-houdini-patreon-may---trailer.md


### From sops to final render with Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O_oxVn-YVB0
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** solaris, lops, karma, vdb, cops, compositing, lighting, cgi-integration, procedural, advanced
- **Summary:** Starts from a pre-built scene (camera oriented to real-world EXIF data and a background plate, covered in earlier videos) with the modeled truck placed via a saved `rest` attribute + Transform. To fake a localized volumetric light-shaft in front of the headlights, the front-metal/headlight geometry is Blasted out, moved back to its pre-transform rest position (via a second `rest` extraction),...
- **File:** tutorials/from-sops-to-final-render-with-karma.md


### Quick CG integration with Houdini and Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kxg05cfgdQI
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** camera-matching, depth-map, onnx, machine-learning, cops, solaris, karma-xpu, cgi-integration, texture-projection
- **Summary:** The pipeline starts with a real back-plate photo (from Polyhaven) plus its RAW original (used only to read EXIF: camera model, focal length, crop factor) for accurate camera matching — a reference box of assumed real-world dimensions is placed and aligned to vanishing points in the image, using an assumed human-height camera position and a corrected focal length (`nativeFocalLength ×...
- **File:** tutorials/quick-cg-integration-with-houdini-and-karma.md


### Procedural Buildings in Houdini | Tips and Tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JCdVrNwiMGk
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** brickify, voronoi-fracture, labs-sort, lattice, poly-bevel, architecture, ornament, procedural-modeling
- **Summary:** The dome's "brickify" pattern starts by scattering many points on a swept 8-division base shape, then dividing them into horizontal layers by computing the bounding-box min/max, deriving a per-layer height ("layer height"), assigning each point a `layer` index, and remapping `P.y` from the bounding-box min plus `layer * layerHeight` so points snap into discrete bands that always reach the...
- **File:** tutorials/procedural-buildings-in-houdini-tips-and-tricks.md


### Texture Projection Tool for Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=t9ldXkD7oqA
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** hda, python-states, cops, texture-projection, uv-less, tool-development, product-packaging
- **Summary:** This is a tool demo/showcase rather than a from-scratch build tutorial: the presenter walks through a beta HDA that projects flat textures (logos, labels) onto arbitrary geometry interactively. The tool checks the input mesh for vertex UVs and no UDIMs (a "check" indicator shows "all good") since the underlying compositing runs in Cops, which doesn't support UDIMs — meaning highly non-planar...
- **File:** tutorials/texture-projection-tool-for-houdini-205.md


### Procedural Graffiti in Houdini and COPS #mardini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=suiPD-s1I9U
- **Author:** cgside
- **Houdini Version:** 21.0
- **Tags:** packed-primitives, planar-inflate, cops, openCL, sdf-shape, negative-id, drips, graffiti, mardini
- **Summary:** Starting from a bold **Font** node (text set to "CUPS" for the demo), the letters are Resampled and simplified with Subdivision curves to lose sharp corners and get a rounder graffiti look. Since each letter is a single primitive, per-letter random transforms are applied entirely in VEX rather than a for-loop: a random scale (`fit()`-remapped `random(prim_num + seed)`) is applied relative to...
- **File:** tutorials/procedural-graffiti-in-houdini-and-cops-mardini.md


### Environments in Houdini | Part 5 - Solaris and rendering with Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=h6MN80ka4Vg
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** solaris, lops, usd, karma, materials, shaders, triplanar, lighting, fog, scattering, instancing, environment, advanced
- **Summary:** Before importing to Solaris, every SOP output gets an explicit `name` attribute (terrain, water, bridge arch, bridge stones, vines, leaves, terrain-back) so LOPs can address each part individually, plus a **grass mask** primvar (built from `N.y` fit-ranged and bind-exported) and a UV-based water mask — all cached via **File Cache** for a stable base. In Solaris, a Sub Import brings this in...
- **File:** tutorials/environments-in-houdini-part-5---solaris-and-rendering-with-karma.md


### Vex quick tips #2 | Iterating over numbers
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7PHYAnZbTvM
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vex, quick-tips, for-each, lots-of-division, random-cut, find-shortest-path, expand-point-group
- **Summary:** By default, feeding a flat plane straight into Lots of Division produces a visually obvious fixed seam from its first subdivision iteration. The fix is to cut a random path across the grid first with Find Shortest Path, then subdivide. The tutorial builds row/column attributes on a Grid (`row = floor(ptnum/cols)`, `col = ptnum % cols`, with `max_col` stored as a detail attribute), then...
- **File:** tutorials/vex-quick-tips-2-iterating-over-numbers.md


### Vex quick tips | Overhang look with channel ramps
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SHAgvzji9vM
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vex, quick-tips, channel-ramp, quaternion, curve, overhang, procedural-modeling
- **Summary:** Starting from a Line, Resample heavily (0.02) with curve-view output, the curve is first displaced along its X-axis normals using a channel ramp sampled by curve view (`leafRamp`) multiplied by a displacement-amount slider to build a simple leaf-shaped silhouette (mirrorable for a full leaf). To get the overhang look, a second wrangle recomputes normals along the tangent's perpendicular (X...
- **File:** tutorials/vex-quick-tips-overhang-look-with-channel-ramps.md


### Procedural Modeling with VEX, VDB and Vellum
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8RIneeMCbAg
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vex, vdb, vellum, xyzdist, quaternion, compile-block, upholstery, couch, curve-manipulation
- **Summary:** The couch starts from a 12-point circle converted to a single-primitive line, then re-assembled point-by-point with a VEX point wrangle that offsets each point's position via `prim()`-sampled curve data — creating a variable spacing ("ramp going around") so some sections of the couch profile are naturally smaller than others. The core VEX exercise walks through building this from primitives:...
- **File:** tutorials/procedural-modeling-with-vex-vdb-and-vellum.md


### Procedural Pizza in COPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mL2TkAB_Rqc
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** cops, materialx, procedural-texturing, stamping, leaf-generation, uv, rasterize, karma, food
- **Summary:** The crust look starts from a ring compared against an SDF, smoothed to get a rounded profile, then previewed via a height/displacement connection; a pointy artifact from a small grid-division size is fixed by blurring and blending with Minimum mode against the original texture (repeated at increasing scale) to keep some sharp corners while rounding the rest. A separate distortion pass is...
- **File:** tutorials/procedural-pizza-in-cops.md


### Quick CGI Integration with Houdini and Solaris
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xm9d-Un3Hrg
- **Author:** cgside
- **Houdini Version:** 20.5.410
- **Tags:** solaris, karma, cops, aov, uv-projection, background-plate, physical-sky, cgi-integration, product-viz
- **Summary:** A half-sphere "dome" (Polyfill, Bevel, Subdivide) is polar UV-projected and rotated to align with the background plate, then set to **remove back faces** (Optimize display option) so its interior — where the HDRI texture will be projected — is visible in the viewport, with normals reversed so the camera sees the interior rather than the exterior. This dome is Quick-Shaded with the HDRI (or a...
- **File:** tutorials/quick-cgi-integration-with-houdini-and-solaris.md


### Environments in Houdini | Part 4 - Vines, Rocks and Fog
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cXbdFwd3u9o
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, vdb, procedural, fracture, environment, scattering, volumes, fog, third-party-plugin, advanced
- **Summary:** Hanging vines under the bridge arch are grown from a mask built almost entirely in VEX as a learning exercise (rather than pure VOPs): the bridge's arch curve is Match-Sized and Swept into a thin ribbon purely to serve as an attribute-transfer proxy, then a wrangle uses **`pcopen()`** (point-cloud open, searching the swept ribbon's points within a radius) to build an initial proximity mask,...
- **File:** tutorials/environments-in-houdini-part-4---vines-rocks-and-fog.md


### Building Tools in Houdini with vex and python | Flatten Loop
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=enW-PwgBWE4
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** vex, python, hda, editor-scripting, tool-development, radial-menu, beginner, intermediate
- **Summary:** A "meta" tutorial about tool-building rather than modeling itself: starts from a simple VEX averaging wrangle (select points, compute their average position, snap them to it along one axis) and evolves it step by step into a fully productionized interactive tool. Key beats: iterating over a point *group* parameter with `expandpointgroup`, building an array of positions to feed to VEX's `avg()`...
- **File:** tutorials/building-tools-in-houdini-with-vex-and-python-flatten-loop.md


### Environments in Houdini  | Part 3  - Vegetation with Simple Tree Tools
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FvM09fA0cKY
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, procedural, scattering, environment, python, vegetation, third-party-plugin, intermediate
- **Summary:** Opens with a quick bug-fix from Part 2: the random top-brick rotation VEX had a bracket misplaced, accidentally mixing the rotation-angle randomization with the zero-centered position offset, causing bricks to rotate consistently to one side instead of both; moving the parenthesis fixes it. The main lesson uses **Simple Tree Tools** (a third-party paid plugin, explicitly recommended over...
- **File:** tutorials/environments-in-houdini-part-3---vegetation-with-simple-tree-tools.md


### Environments in Houdini  | Part 2  - Stone Bridge
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kPtCgMWIBj4
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vex, procedural, fracture, environment, hard-surface, advanced
- **Summary:** The bridge starts from a centered **Line** (arch profile), transformed and resampled, then deformed using its curve-U (`curveu`)-driven **Ramp** (mirrored via `abs(u*2-1)` math) to hand-sculpt an arch silhouette. That curve is swept/extruded into a **Box** cross-section and Boolean-intersected against a wider slab to carve the arch opening. To divide the resulting wall into individual bricks,...
- **File:** tutorials/environments-in-houdini-part-2---stone-bridge.md


### Environments in Houdini | Part 1 -  Heightfields
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ER_W3w3SkGk
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** heightfield, terrain, procedural, environment, vex, intermediate
- **Summary:** The terrain starts as a basic **Heightfield** (Z size 700), with a custom gradient mask built manually in VOPs for finer control than the built-in Heightfield Pattern ramp preset: a Vector to Float extracts the Z component of position, **Fit Range** normalizes it (using base-relative-reference divided by 2, negated on one side) into a 0-1 gradient, complemented/inverted to bias more toward the...
- **File:** tutorials/environments-in-houdini-part-1---heightfields.md


### How to (not) bake brownies in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=R3ClxIiqxag
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vex, vdb, flip, simulation, uv, procedural, food, advanced
- **Summary:** The brownie top starts as a Box, grouped by normal (positive X) and edge-length-filtered to select and Bevel specific edges, with outer frames grouped (via max edge length) for the layering/cracking pass. That grouped layer is Blasted out, Remeshed for uniform point distribution, and Subdivided heavily. The core **organic-cluster fracture technique**: Scatter a handful of points on the...
- **File:** tutorials/how-to-not-bake-brownies-in-houdini.md


### Houdini Mini Course  |  Cops, Vex and Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=24vjgnyZRTw
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, cops, karma, solaris, texturing, materials, lighting, procedural, advanced
- **Summary:** Rather than using the Tile Sampler COP directly, the author deliberately combines SOPs and COPs: a 21x21 Grid's primitive centroids become points (Extract Centroid style wrangle), a radial distance-from-center mask (`length(@P)`) is used to delete a circular cluster of center points, and a single point is re-added exactly at the bounding-box center to host a logo tile later. A chain of point...
- **File:** tutorials/houdini-mini-course-cops-vex-and-karma.md


### Vex Problem Solving in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Fiw_NedtssQ
- **Author:** cgside
- **Houdini Version:** 20.5.410
- **Tags:** vex, vdb, sdf, cluster, uvs, gradient, quaternion, vines, ivy-generator, procedural-uvs
- **Summary:** For an in-progress ivy/vine generator tool, points are scattered on a column surface with target positions to grow toward, constrained via a SOP Solver. The obvious approach — Ray Project (Minimum Distance) directly onto the mesh each solve step — causes points to get permanently stuck in concave crevices. The fix: convert the geometry to VDB, apply a heavy **VDB Smooth** (essentially a large...
- **File:** tutorials/vex-problem-solving-in-houdini.md


### Wood Barrel Texturing in COPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=O6T5eVYJHsA
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** cops, copernicus, uvdist, texture-paint, rasterize, karma, wood, rust, texturing
- **Summary:** Back in SOPs, a **Measure Curvature** (Labs) convexity attribute is multiplied and heavily blurred (8 iterations) to create a soft rust-origin mask around edges, then file-cached to avoid Houdini's node re-evaluation overhead. In Cops, rather than the standard "Restore Geometry"-to-UV-space workflow (known to cause edge-bleeding artifacts, as documented by others in the community), a custom...
- **File:** tutorials/wood-barrel-texturing-in-cops.md


### Beginner Procedural Modeling/UVS Tutorial in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-1kxDkdmcV4
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** modelling, procedural, vex, uv, beginner
- **Summary:** An explicitly beginner-oriented tutorial pairing a simple procedural-modeling exercise with a full, correct UV workflow for procedural assets. The barrel body starts as a Tube, bulged into shape with a **relative bounding-box** VEX wrangle feeding a **Ramp** (a hallmark simple-VEX pattern: `relbbox(0,@P)` gives 0-1 values regardless of scene position, unlike `@P` itself). Planks are separated...
- **File:** tutorials/beginner-procedural-modelinguvs-tutorial-in-houdini.md


### Spiral Splash Tutorial in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xz1oNZGq7P0
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** vex, quaternion, pop-network, pop-fluid, vellum, super-formula, karma, subsurface, food, product-viz
- **Summary:** A centered Line is Resampled, lightly Mountain-distorted for an organic base curve, Resampled again into a dense subdivision curve, and given an arc-length "spine" UV attribute. The **spiral itself is built entirely in VEX**: Orient Along Curve provides a tangent basis (`tangentU`/`tangentV`, one along the curve direction, one pointing outward along X); a wrangle computes an angle from the...
- **File:** tutorials/spiral-splash-tutorial-in-houdini.md


### Tiling Patterns with COPS and SOPS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=05uuRimyHfY
- **Author:** cgside
- **Houdini Version:** 20.5.302
- **Tags:** cops, copernicus, sops, for-each-loop, stamp-point, uv-by-id, tiling, stone, texturing
- **Summary:** The base fan/scale shape is built as an SDF circle in Cops, transformed/mirrored/inverted and multiplied to form the repeating tile motif. To instance it correctly, a **Grid of points** (scaled from center, rows/columns tied to grid size minus one) gets **row and column ID attributes** (credited to "Fenis" for this part) used to carve an X-style point pattern by filtering/removing specific...
- **File:** tutorials/tiling-patterns-with-cops-and-sops.md


### Procedural UV's In Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7ZJeWIFYSxg
- **Author:** cgside
- **Houdini Version:** 20.5.302
- **Tags:** uvs, find-shortest-path, vdb, vex, hda, gradient, cake, procedural-uvs
- **Summary:** The source geometry (from a VDB Boolean cut) is too irregular/tessellated for traditional manual seam picking. The fix: build a simplified proxy by Remeshing (reducing polycount) and Ray-projecting it back onto the original silhouette, then **Poly Reduce** it further so only the sharpest edges remain — these are selected via a **mean-edge-length/edge-angle** Group, which reliably marks the...
- **File:** tutorials/procedural-uvs-in-houdini.md


### Enhance your renders in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c193tsyLH-0
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, vdb, cops, texturing, procedural, shaders, karma, noise, food, intermediate
- **Summary:** For the lettering (imported as FBX from ZBrush with a `name` attribute from the original subtitles), the goal was to add a subtle wavy/lit edge highlight cheaply instead of hand-sculpting more detail. Corner/angle edges are isolated via **Group** (min edge angle), converted to a line, isolated to a single primitive, resampled and fused into one continuous curve, then displaced using `sin()` of...
- **File:** tutorials/enhance-your-renders-in-houdini.md


### Houdini Beginner Tutorial | Creating a perfume bottle
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=conZuTxHnoc
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vdb, vex, procedural, fracture, texturing, beginner, product-viz
- **Summary:** The bottle body starts as a simple Box with two Poly Bevels (first a modest bevel, then a larger heavily-subdivided one) for a rounded hard-surface look; a front screw/cap detail box gets its own edge-group-based Bevel (angle-thresholded to avoid rounding flat faces) and is Match-Sized into place. Small screw details are built from a WAP-sphere generator, clipped/scaled, Polyfilled (required...
- **File:** tutorials/houdini-beginner-tutorial-creating-a-perfume-bottle.md


### Tips and Tricks for a better Houdini Time
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VL5N4jKidVA
- **Author:** cgside
- **Houdini Version:** 20.5.302
- **Tags:** uvs, solaris, opacity-to-mesh, make-transform, rest-position, time-dependency, karma, workflow
- **Summary:** For UV work on a symmetrical asset, a Clip node slices the mesh in half (using Group by Normal to isolate one side for the seam), clips top/bottom, and saves the clip-edges group directly on the Clip node itself; UV Flatten then uses that saved group as its seam input, and since the resulting cuts shouldn't remain on the final render mesh, **Labs UV Transfer** copies the computed UVs back onto...
- **File:** tutorials/tips-and-tricks-for-a-better-houdini-time.md


### Model and Rig a Wardrobe in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c_t8JwyHJrA
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, kinefx, rigging, vex, fracture, procedural, furniture, intermediate
- **Summary:** The wardrobe's back panel starts as a Grid, Copied several times using a **bounding-box-driven expression** for perfect alignment, then centered. To divide the resulting large panel into an irregular grid of shelf/drawer sections, rather than a plain Divide node, a **loop-based recursive Voronoi Fracture** is used: each iteration randomly Switches (`random()` × input count) between a...
- **File:** tutorials/model-and-rig-a-wardrobe-in-houdini.md


### Cliff Face in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mcP3wLo1lIQ
- **Author:** cgside
- **Houdini Version:** H20+ (Copernicus/COPS, Labs tools)
- **Tags:** procedural, vdb, quadremesh, cops, texturing, uv, scattering, vellum, advanced
- **Summary:** A three-part pipeline (rock geometry → COPS texturing → vines/leaves). **Rock geometry**: scatter points on a grid, orient along Z, copy boxes, randomize orientation/scale with a natural/cellular noise, then repeatedly alternate between mesh operations (Mountain distortion, Box Clip, Mesh Sharpen for a faceted "rock plane" look) and volume operations (VDB conversion to unify the mesh, Boolean...
- **File:** tutorials/cliff-face-in-houdini.md


### Resample Color Ramps in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=P-2FPlUJO60
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** python, hou-module, ramp, cops, scripting, automation, quick-tip
- **Summary:** The script grabs the currently selected node via `hou.selectedNodes()[0]`, accesses its ramp parameter (named "ramp" in the example, e.g. on a `mono_to_rgb`-style Cops node), and calls `.eval()` to get the live `hou.Ramp` object. Three lists are extracted from it: `ramp.basis()` (interpolation type per key), `ramp.keys()` (key positions), and `ramp.values()` (the actual colors) — these are the...
- **File:** tutorials/resample-color-ramps-in-houdini.md


### UVW randomizer in karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1SXCz_Ta4Lc
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** materialx, karma, uvw-randomizer, cell-noise, place2d, tiling, texturing
- **Summary:** Standard UV tiling (Texture Coordinates → Multiply Constant for repetition count → Modulo set to 1 to wrap the UVs) produces the classic obviously-repeating look. To randomize per-tile, the pre-modulo repeated UV value is **floored**, collapsing each tile into a single discrete integer-pair value; feeding that into **Cell Noise** gives each tile cell a distinct pseudo-random value, and a...
- **File:** tutorials/uvw-randomizer-in-karma.md


### VDB Procedural Modeling in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ag7I-FK4TF0
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** vdb, volume-vop, vex, for-each-loop, bend, sweep, bones, organic-modeling, procedural-modeling
- **Summary:** A centered Line (7 points) is swept with a Labs Simple Shapes quad cross-section (unequal top/base sizing, rounded corners) to form the base rib shape, given end caps, subdivided, lightly Mountain-distorted (low amplitude, zero-centered), and normal-blurred to soften intersection corners. Converting to a VDB (SDF, smoothed), the core of the video builds a **four-layer cascading noise stack in...
- **File:** tutorials/vdb-procedural-modeling-in-houdini.md


### Procedural Helical Column in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HDIIwy11otU
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** vdb, vex, intersection-analysis, orient-along-curve, quad-remesh, architecture, column, box-clip
- **Summary:** Two Spiral primitives (radius scale 1.2, 5 turns, tuned start angle) are offset — one scaled up slightly (1.2 in X/Y) — merged, and swept with a round tube profile (12 divisions, radius 1, single-polygon end cap), with per-primitive p-scale variation (1.1/1.2) giving the two strands slightly different thickness. The swept mesh is clipped top and bottom, converted to VDB, heavily VDB-smoothed...
- **File:** tutorials/procedural-helical-column-in-houdini.md


### Procedural Modeling with Houdini 20.5 Tools
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=k7-5PaOccYc
- **Author:** cgside
- **Houdini Version:** 20.5.319
- **Tags:** wrinkle-deformer, planar-inflate, labs-simple-shapes, cops, vex, prim-intrinsic, headphones, fabric, procedural-modeling
- **Summary:** The earpad ring starts from a **Labs Simple Shapes** node (Quad shape, XY plane, unequal base/top sizes, rounded corners with 5 divisions), fused, Resampled (subdivision curves), then Swept (Ribbon mode, 1 column/division, weight 0.45), Extruded and Beveled (ignoring flat edges) for the front cushion rim. UVs are built by finding the boundary-point group via **Find Point/Prim Group** (rather...
- **File:** tutorials/procedural-modeling-with-houdini-205-tools.md


### Procedural Leaking Texture in Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8iK3GD3yeCE
- **Author:** cgside
- **Houdini Version:** 20.5.170
- **Tags:** cops, curvature, vex, dot-product, uv-gradient, weathering, decay, procedural-textures, karma
- **Summary:** Starting from simple box geometry with window cutouts, Subdivide adds enough resolution for **Measure Curvature** (Labs) to compute convexity and concavity attributes at SOP level (unavailable at shading level, hence the need for real geometry resolution). Leaks shouldn't originate everywhere — only where water/dirt would naturally collect, e.g. not at the bottom of windows or at the very top...
- **File:** tutorials/procedural-leaking-texture-in-houdini-205.md


### Procedural tips and tricks in Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wgStaCuEglI
- **Author:** cgside
- **Houdini Version:** 20.5.309
- **Tags:** vex, find-shortest-path, vdb, cops, lab-sort, seamless-noise, jewelry, procedural-modeling
- **Summary:** Stone-holder wire mesh generation ("prong" shapes) needs groups of points arranged in a circular pattern around each stone; rather than manual selection (fragile if the stone shape changes), a VEX snippet (adapted from sample code by Animatrix) uses `sample_circle()` to generate points in a circular pattern, grouping the nearest points and adding a distance parameter to offset their position,...
- **File:** tutorials/procedural-tips-and-tricks-in-houdini-205.md


### The Donut Tutorial in Cops | Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=meX4fLnITR0
- **Author:** cgside
- **Houdini Version:** 20.5.301
- **Tags:** cops, copernicus, uvs, procedural-textures, tile-pattern, karma, food, donut
- **Summary:** A 32x64 Torus gets UVs via seam-grouped UV Flatten (rectified, imperfect but acceptable), then a custom wrangle stretches the UVs to fill the full UV tile — using `geo unwrap`, a detail-mode bounding-box-max query, and per-component UV assignment (`uv.x` unchanged, `uv.z = 0`, `uv.y` divided by the bounding-box Y max), with sign-flips and +1 offsets to fix upside-down/out-of-range results....
- **File:** tutorials/the-donut-tutorial-in-cops-houdini-205.md


### Shoe Laces in Houdini | Vex and Vellum
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rlrWEjoO8jQ
- **Author:** cgside
- **Houdini Version:** 20.5.301
- **Tags:** vellum, vex, vellum-string, python-states, intersection-analysis, orient-along-curve, footwear, procedural-modeling
- **Summary:** Eyelet points are hand-placed on the shoe mesh using a custom HDA ("Place Points on Geo," built with Python States — the same tool later built from scratch in the author's "Interactive Tools with Python States" video). Ring geometry gets a Connectivity + centroid pass to find each eyelet's position, and the eyelet points are mirrored and sorted by X so the zig-zag lace pattern can be...
- **File:** tutorials/shoe-laces-in-houdini-vex-and-vellum.md


### Designer like Materials in Cops | Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Lm5cG2XxRwU
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** cops, procedural, texturing, materials, karma, substance-style, intermediate
- **Summary:** Builds a complete quilted-leather material from scratch in a CopNet: a **Tile Pattern** (7 divisions, concentric gradient ramp) forms the base diamond grid, which is inflated via layered blurs blended as a mask to create the puffed/padded look. Random per-tile rotation (via **UV Transform** driven by tile ID as seed) plus a ramp-driven radial pattern builds the "fold" creases between diamonds,...
- **File:** tutorials/designer-like-materials-in-cops-houdini-205.md


### Displacement maps in cops | Houdini 20.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xOeZncLWztc
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** cops, procedural, texturing, displacement, uv, tips, intermediate
- **Summary:** Covers ten quick techniques for building complex tileable displacement patterns in Houdini 20.5's Copernicus (COPs). A **Feather** node (not Blur) creates a beveled/chamfered look on hard pattern edges by controlling a distance parameter, producing sharp facet transitions rather than smoothed blur. **Tile Pattern**'s pruning options isolate single rows/columns by tolerance or...
- **File:** tutorials/displacement-maps-in-cops-houdini-205.md


### Useful Vex snippets | Houdini tips and tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_C6-g1C--ws
- **Author:** cgside
- **Houdini Version:** 20.5.760
- **Tags:** vex, uv-sample, sign-function, connectivity, minpos, vex-snippets, quick-tips
- **Summary:** Instead of a for-each loop with an internal Match Size (aligned to center) to re-center a batch of packed rock objects before Copy to Points, packed points can simply be moved to the origin with a single wrangle line setting position to zero — since with packed primitives you're really just repositioning points. For wrapping flat UV-space logo artwork onto a curved camera-body mesh: convert...
- **File:** tutorials/useful-vex-snippets-houdini-tips-and-tricks.md


### Procedural workflow | Vex, Kinefx, UV's and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=T7CoIJg8Dx4
- **Author:** cgside
- **Houdini Version:** 20.5.734
- **Tags:** uvs, kinefx, vellum, xyzdist, vex, scatter, sprinkles, cupcake, food
- **Summary:** UVs are shown to be useful beyond texturing: after flattening UVs on a selected seam group, the **U component** of the UV attribute becomes a ready-made X-axis mask for displacing geometry (fed through a ramp for shaping). The **V/U components** also make excellent **Sort Points** keys — sorting by U lets you cleanly select "rings" around the cupcake, and sorting again by V prevents the...
- **File:** tutorials/procedural-workflow-vex-kinefx-uvs-and-more.md


### Procedural and Organic Modeling in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8hUjc7BEI9g
- **Author:** cgside
- **Houdini Version:** 20.5.724
- **Tags:** vdb, poly-bridge, lattice, vex, volume-vop, organic-modeling, sculpture, karma
- **Summary:** A frequency-30 Sphere gets a top/bottom mask via a Point VOP computing the relative bounding-box Y component, mirrored (`abs(y - 0.5)`) and range-expanded, then distorted with a sparse-convolution 3D Turbulence noise on position. A rest-position + random attribute drives a **Clip** operation (comparing `v@P.y` to `@Cd.r`) to cut the sphere into a jagged ring boundary; the boundary is split...
- **File:** tutorials/procedural-and-organic-modeling-in-houdini.md


### Direct and Procedural Modeling in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=t1QemBG462g
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vex, procedural, hard-surface, tips, intermediate
- **Summary:** Six independent tips from one hard-surface build. (1) Smart direct selection: select a repeating pattern (e.g. every other face on a tube) and expand it forward with Shift+Up Arrow, plus interactive select-by-normal for quick face grouping before extruding. (2) Cleaning a hand-drawn Draw Curve: clip the messy curves to share the same key points, do a large-length resample to capture just the...
- **File:** tutorials/direct-and-procedural-modeling-in-houdini.md


### Procedural techniques in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=PcP9Eieij1g
- **Author:** cgside
- **Houdini Version:** 20.5.734
- **Tags:** flip, vex, vdb, distance-along-geometry, materialx, karma, food, density-by-attribute
- **Summary:** To get caramel that flows in visible horizontal layers rather than uniformly, a density attribute is authored on the FLIP source points by dividing the point cloud into sections using its own bounding box, blending in noise per-section plus a separate noise at the bottom via `lerp()`, remapping the result to fit the solver's expected density range, and enabling **Density by Attribute** in the...
- **File:** tutorials/procedural-techniques-in-houdini.md


### Using Substance Designer nodes for Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ObBXMX-VH90
- **Author:** cgside
- **Houdini Version:** 20.5.734
- **Tags:** heightfields, substance-designer, third-party-plugin, pegasus, vex, texturing, rocks, karma
- **Summary:** The base heightfield comes from a Circle extruded exactly one unit (so its full range maps cleanly onto Substance Designer's 0–1 height convention), with the extrude-front group promoted, fused, and positioned on positive X for correct alignment with the SD texture. A **Tile Sampler** node builds the base rock-facet pattern from gradients, with heavy use of offset/random disorder/random...
- **File:** tutorials/using-substance-designer-nodes-for-houdini.md


### Vellum Typography in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Sr7iwTjwo2E
- **Author:** cgside
- **Houdini Version:** 20.5.701
- **Tags:** vellum, curvature, remesh, materialx, karma, typography, wrinkles, animated-mask, metal
- **Summary:** Text is created via Font, arranged with an Edit node, centered/thickened via Match Size, then rounded with a VDB from Polygons → Smooth → Convert back to polygons pass. After splitting primitives along Z and grouping unshared edges, those edges are converted to curves, resampled, and re-projected onto the VDB-smoothed geometry. A curvature attribute is set to 1 on the curves and 0 on the base...
- **File:** tutorials/vellum-typography-in-houdini.md


### Sushi Modeling and Rendering in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c1tO7581nOM
- **Author:** cgside
- **Houdini Version:** 20.5.701
- **Tags:** vellum, shape-match, quad-remesh, materialx, karma, subsurface, food, connectivity, product-viz
- **Summary:** A single rice grain is built from a Line swept with scale-along-curve (thicker in the middle, grid end caps for rounded tips), Bent for shape, then blended between the bent version and a straight version via a bounding-box-X mask and `lerp()` so the underside stays flat. Subdivide + Exoside QuadRemesher clean up the pole artifact left by the sweep/bend. Since simulating the full-resolution...
- **File:** tutorials/sushi-modeling-and-rendering-in-houdini.md


### Chocolate Swirl Effect with Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4PjTMogFWqQ
- **Author:** cgside
- **Houdini Version:** any modern (H19+, uses MaterialX/Karma)
- **Tags:** vdb, procedural, materials, karma, mardini, uv, displacement, intermediate, advanced
- **Summary:** A compact, from-a-sphere procedural food-modeling breakdown. Geometry starts from a Labs Sphere Generator, clipped and filled, with two blurred masks built from a group-expand base: one blends a Mountain-node bump layer onto the sphere, the other drives a point-normal displacement. The signature swirl comes from converting the mesh to a VDB-backed **Volume Deform** (which auto-generates a...
- **File:** tutorials/chocolate-swirl-effect-with-houdini.md


### Quality of life tips in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=iQql20c4Gio
- **Author:** cgside
- **Houdini Version:** 20.5.701
- **Tags:** workflow, hotkeys, poly-hinge, connectivity, enumerate, selection-modes, matcap, viewport, quality-of-life
- **Summary:** To snap-orient a new object (e.g. a box) onto part of a reference model, Ctrl-click the reference's display flag to set it as the pick reference, drop the new object, press Enter to enter the tool state, and use the (potentially remapped) "start orientation picking" hotkey plus left-click to snap position/orientation to any point on the model. The new **Poly Hinge** node, when switched from...
- **File:** tutorials/quality-of-life-tips-in-houdini.md


### Kinefx and Vellum Fluid in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6wqRXRV7oxk
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** kinefx, rigging, vellum, simulation, vex, procedural, animation, advanced
- **Summary:** The tube body starts as simple modeling (circle + rounded square merged and Poly Bridged, UVs computed early via bottom-point grouping for potential later texturing, capped and beveled). Rather than simulating the actual squeeze, the tube's two "poses" — a naturally-drooping filled state and a squeezed/emptied state — are each produced as separate **Vellum cloth sims** (with the polyfilled...
- **File:** tutorials/kinefx-and-vellum-fluid-in-houdini.md


### Houdini and Karma tips and tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cRr4R54DRKw
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** karma, materials, shaders, mtlx, vex, procedural, modeling, tips, intermediate
- **Summary:** **Edge breakup:** instead of (or in addition to) a real Bevel, a **Round Edge** MaterialX node (with a tuned radius) is plugged into the shader's normal input to fake rounded, worn edges purely in shading — its second output is a "round mask" isolating just the affected edge area. That mask drives a **Mix** node blending between the round-edge-modified normals and a version of those same...
- **File:** tutorials/houdini-and-karma-tips-and-tricks.md


### MaterialX and Karma | procedural networks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kdpeMWXIGrY
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** karma, materials, shaders, mtlx, procedural, texturing, tips, intermediate
- **Summary:** **Debugging via solo/emission preview:** selecting any node in a MaterialX network and pressing **X** switches the viewport to a flat emission-shader preview of just that node's output — instant visual debugging without wiring a temporary output or switching contexts; pressing X again returns to the full shader. **Re-centering tiled textures:** a `MtlX Image` fed through **Texture Coordinates...
- **File:** tutorials/materialx-and-karma-procedural-networks.md


### Let's make soap! Houdini and Karma beginner course
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Y-CjDhFmclQ
- **Author:** cgside
- **Houdini Version:** 20
- **Tags:** modeling, vdb, vex, expressions, materials, shaders, karma, solaris, lighting, product-viz, beginner
- **Summary:** The soap bar starts as a beveled Box (edges excluded from bevel on flat faces via an angle threshold), with a logo imported via **Regions from Image**, cleaned, cached, and isolated by name; the logo shape is Match-Sized onto the soap's top face (mean/max alignment, scale-to-fit, then centered-scale via a **centroid-based expression** so it shrinks toward its own middle rather than a corner),...
- **File:** tutorials/lets-make-soap-houdini-and-karma-beginner-course.md


### Still Life Scene Breakdown | Houdini tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=peBkuU0Es1Q
- **Author:** cgside
- **Houdini Version:** 20.5.590
- **Tags:** ray-project, for-each-loop, cops, karma, materialx, displacement, product-viz, still-life, dust
- **Summary:** Projecting a flat label onto a bottle with Ray Project set to Minimum Distance fails, and switching to Projected Rays along Z produces unwanted stretching; the fix is to transfer the bottle's normals onto the label, promote them to point normals, **blur** them (fairly heavily), and Ray Project using those blurred normals instead of a fixed vector — eliminating the stretch. The torn-paper "neck...
- **File:** tutorials/still-life-scene-breakdown-houdini-tips.md


### Hard Surface Techniques in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qtzO_NoQbtE
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vex, vellum, hard-surface, procedural, subdivision, tips, advanced
- **Summary:** For the cloth pads: after basic extrude/bevel modeling, pieces are grouped in batches of 8 (via `primnum / 8`, with a `shift by 4` sort so groups align correctly with the visual layout), then a **For Each (name/primitive)** loop saves a `rest` position, selects/converts the bottom to vertices, runs **UV Flatten**, promotes UVs to points, and assigns the UV attribute directly to position —...
- **File:** tutorials/hard-surface-techniques-in-houdini.md


### Houdini Tips | Tileable Noises, Cam from Stage, TOPS and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=zItss8TuZMo
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** solaris, lops, tops, vex, vellum, procedural, fracture, environment, tips, intermediate
- **Summary:** **Camera from Stage:** an animated camera authored in Solaris/LOPs can be pulled back to the SOP/object level via **Object → Import Camera** (selecting the target camera prim, e.g. `camera2`), producing a native object-level camera with the same animation intact — described as the only way to get a Stage camera back to objects short of a full USD round-trip. **Stretched rock wall via RBD...
- **File:** tutorials/houdini-tips-tileable-noises-cam-from-stage-tops-and-more.md


### Groups Patterns in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FLWrmz8QPZQ
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, procedural, tips, intermediate
- **Summary:** (1) **Normal-based grouping:** `N.y` alone in a Group Expression only reliably selects top/bottom box primitives for cube-like proportions; `abs(N.y) > 0.5` (a thresholded absolute-value check) works regardless of box dimensions. The equivalent can be done non-expression-wise with a **Group (Normals)** node ("Keep by Normals" set to Y, 0, with "include normals matching opposite direction" to...
- **File:** tutorials/groups-patterns-in-houdini.md


### Houdini Tips | Expressions, VEX, Recursive Cuts and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2Vw6jvHrnBw
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, uv, vellum, cops, expressions, procedural, tips, advanced
- **Summary:** **`nprimsgroup()` expression:** when using Group Range to select "every Nth primitive" within a specific base group (e.g. a strip of extruded side faces you want to subdivide for cleaner UVs), the natural-seeming `nprims()` expression actually counts *all* primitives in the whole object, not just the target group — producing wrong divisions. The fix is **`nprimsgroup(0, "group_name")`**, which...
- **File:** tutorials/houdini-tips-expressions-vex-recursive-cuts-and-more.md


### Houdini Tips - Procedural UV's, Channel Packing and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=m00nko87HeI
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, uv, modeling, texturing, unreal, zbrush, procedural, tips, intermediate
- **Summary:** UV Texture's default behavior stretches textures on non-square flat shapes. Two fixes: (1) a VEX approach computing the incoming shape's aspect ratio, using an if-statement to scale X or Y down to fit the 0-1 UV tile (negating Y to correct orientation and offsetting to place it correctly in the tile); (2) a simpler node-based approach using **UV Flatten** with default settings, driven by an...
- **File:** tutorials/houdini-tips---procedural-uvs-channel-packing-and-more.md


### Modern Furniture Modeling in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=at27qaTVrFc
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, vex, procedural, expressions, furniture, product-viz, intermediate
- **Summary:** The base pattern starts as a **Grid** (10x1, alternating-triangle remesh mode) that gets **Copy-and-Transform**'d using the bounding-box size as the offset (so shapes stack edge-to-edge), scaled down to 0.3 — critically **pivoting the scale from the shared meeting edge** (via a copy-pasted `Z-mean` expression in Pivot Transform) rather than each shape's own center, so the scaled copies...
- **File:** tutorials/modern-furniture-modeling-in-houdini.md


### Houdini to Unreal: HDA Setup and Workflow
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fgUIMtGLIrI
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, python, pipeline, unreal, houdini-engine, instancing, materials, procedural, advanced
- **Summary:** Starting from an existing procedural lamp/branch generator (a two-seed noise-driven shape generator with imperfect but usable results), the whole network is wrapped in a **Subnet** and converted into an HDA via **Edit Parameter Interface**: relevant internal parameters (global seed, secondary seed, Mountain noise amplitude/element size/offset) are dragged out into user-facing folders...
- **File:** tutorials/houdini-to-unreal-hda-setup-and-workflow.md


### Houdini Heightfields and Cliffs
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fF01Lyg_G48
- **Author:** cgside
- **Houdini Version:** 20
- **Tags:** heightfield, terrain, procedural, erosion, texturing, materials, environment, advanced
- **Summary:** The terrain starts as a 500x700 Heightfield with a **Worley Cellular F1** noise (complemented for a desert-like look), then distorted with a very-high-element-size, high-amplitude Heightfield Distort by Noise for more interesting broad shapes. Rock/cliff formations are added by taking a heavily-distorted separate shape and projecting it onto the base terrain, then using **Mask Expand set to...
- **File:** tutorials/houdini-heightfields-and-cliffs.md


### Houdini tips : Solaris, VDB's , COPS and More
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WwwTwtlKm0A
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** solaris, lops, vdb, cops, vellum, vex, compositing, karma, procedural, tips, intermediate
- **Summary:** **Component thumbnails:** in a Component Builder's **Component Output**, the Thumbnail section can be set to actually **Render** (rather than a plain viewport capture) using Karma XPU — feeding it a "camera and scene" second input (a dedicated light, camera, and render settings) produces asset-gallery thumbnails that look identical to a real render; for glass/transparent shaders, the render...
- **File:** tutorials/houdini-tips-solaris-vdbs-cops-and-more.md


### Bake room maps in karma from HDRI interiors H20
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6hbyMIxU1oI
- **Author:** cgside
- **Houdini Version:** H20 (Karma XPU)
- **Tags:** karma, lighting, hdri, materials, solaris, product-viz, intermediate
- **Summary:** Starts from a subdivided box standing in for a room, projects an HDRI panorama onto its interior faces (viewing it via UV Project + Quick Shade to preview and adjust rotation/box scale interactively), then renders that projected interior through a custom Karma lens shader HDA to bake it into a square texture — a "room map." Applying the resulting room map texture to a flat plane (with the...
- **File:** tutorials/bake-room-maps-in-karma-from-hdri-interiors-h20.md


### Custom Procedural Materials with Houdini and Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=M6W_EP48BaI
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, texturing, uv, baking, materials, shaders, mtlx, karma, procedural, intermediate
- **Summary:** Covers three linked stages: (1) building a tileable bulging/tufted pattern from curve-clip geometry and displacing it via a boundary-distance mask to fake a puffy mattress surface, (2) building a separate embroidered stitching pattern from a traced reference image using the same alternating-curve-cut trick (helped by Houdini 20's new Carve by Attribute node), and (3) baking both hi-res proxies...
- **File:** tutorials/custom-procedural-materials-with-houdini-and-karma.md


### Procedural Anisotropy in Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=68WNINd8vE0
- **Author:** cgside
- **Houdini Version:** 20.5.590
- **Tags:** materialx, karma, anisotropy, uvs, orient-along-curve, procedural-shading, spiral-ramp, metal, product-viz
- **Summary:** The pan is modeled from a reversed 64-sided Circle (ZX plane) through several Extrude/Insert passes to build the rim and inner cup profile, with a tapering effect created by blending two Orient-Along-Curve-derived normal sets via Attribute Combine (Copy blend mode). UVs are split by normal (Y-axis) into a cylindrical UV set for the vertical wall and an orthographic Y-projection for the flat...
- **File:** tutorials/procedural-anisotropy-in-karma.md


### Modeling Assets With Vellum
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=d2Qgcbzup2s
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vellum, modeling, vex, simulation, procedural, product-viz, advanced
- **Summary:** **Earphone wires:** three curves (main wire + two earpiece branches) are hand-drawn with **Draw Curve**, Resampled, and Fused with a generous snap distance so they visually join at the branch point while remaining three separate primitives (they'll separate again once simulated) — Resample again with Subdivision Curves smoothing, then group the shared connection points (curve start/end...
- **File:** tutorials/modeling-assets-with-vellum.md


### Vellum Balloon Text in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=T-_L6BeLSkg
- **Author:** cgside
- **Houdini Version:** 20.5.331
- **Tags:** vellum, vdb, typography, karma, materialx, simulation, balloon, text-effects
- **Summary:** Text is created via a Font node, extruded (~0.2, with back cap), then converted to VDB and rounded out via **VDB Smooth**, since a straight Bevel wasn't smooth enough. After converting back to polygons to check the result, the smooth amount and an added **Erode** pass refine the rounded shape further. Since this VDB-remeshed geometry isn't well-suited for simulation directly, a separate...
- **File:** tutorials/vellum-balloon-text-in-houdini.md


### Procedural Fries with Mtlx and Karma XPU
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lcgNaIicsZU
- **Author:** cgside
- **Houdini Version:** 20.5.331
- **Tags:** materialx, karma-xpu, hda, decals, vex, boolean, displacement, food, product-viz
- **Summary:** A simple custom HDA performs UV planar projection with a point placed at the same position as the projection plane, transferring a proximity-based attribute to the geometry so the decal naturally fades out anywhere not facing the projector — avoiding the logo wrapping onto the back of the cup. In Solaris, a Place2D-style node controls texture scale, the texture's Address Mode is set to...
- **File:** tutorials/procedural-fries-with-mtlx-and-karma-xpu.md


### Time saving tips in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mxg-zhwdNlE
- **Author:** cgside
- **Houdini Version:** 20.5.301
- **Tags:** python, hotkeys, karma, materialx, triplanar, workflow, automation, hou-module
- **Summary:** Manual/auto-update mode is normally menu-driven, but binding a small shelf-tool script to a global hotkey (the author uses Ctrl+.) makes toggling it a one-key action — handy for complex scenes or quickly inspecting simple setups without full cook overhead. Separately, Houdini's default "toggle comments in VEX/Python" hotkey combination doesn't work on some keyboard layouts (including the...
- **File:** tutorials/time-saving-tips-in-houdini.md


### Infinite Mirror in Karma XPU
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5jfjCGDdbqs
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** modeling, materials, shaders, mtlx, karma, cops, compositing, procedural, product-viz, intermediate
- **Summary:** Text geometry is built from a **Font** node, Extruded, and centered; primitives are grouped by front/back and split, with the front further grouped into "solid" (frame/border) vs. "mirror" (the reflective glass-facing part) sub-groups; a small Bevel and Vertex Normals soften the model. The core trick is the **material**: a metallic mirror shader (Metallic = 1, Roughness = 0) and a glass shader...
- **File:** tutorials/infinite-mirror-in-karma-xpu.md


### Procedural Problem Solving in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5Cv1SJRm538
- **Author:** cgside
- **Houdini Version:** 20.5.311
- **Tags:** groups, vex, boundary-groups, orient-along-curve, connectivity, hot-air-balloon, procedural-modeling
- **Summary:** To manipulate multiple mesh boundaries independently (e.g. isolating just the top rim of the balloon), Group by unshared edges in points mode with **"create boundary groups"** enabled automatically creates a separate group per boundary loop. For the balloon's colored panel pattern, each gore/section gets a Connectivity ID, then a for-each loop over each piece runs a wrangle creating a...
- **File:** tutorials/procedural-problem-solving-in-houdini.md


### Houdini Procedural Tips | Variants, Concentric Shapes and Step Orient
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ItIlLC6mlF4
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, procedural, scattering, tips, intermediate
- **Summary:** **Variant generation** (adapted from a Maxon-team technique, refined with Discord help): each geometry category (e.g. 3 vase variations, 3 stem/flower variations) gets its own **Connectivity** attribute named `class` and is Packed; all categories are merged, then a second Connectivity pass assigns a `name` attribute across the whole merged set. Inside a **For Each (named primitive)** loop, the...
- **File:** tutorials/houdini-procedural-tips-variants-concentric-shapes-and-step-orient.md


### Procedural Shading Tips #2 in Houdini 20
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=r2SSCwpgnVQ
- **Author:** cgside
- **Houdini Version:** 20.5.306
- **Tags:** karma, materialx, solaris, room-maps, udim, cops, vellum, favela, procedural-shading, texturing
- **Summary:** To avoid every apartment unit rendering with the same texture, a wrangle promotes a unique-ID attribute to detail-max (getting the total count of variations needed), then loops over that count assigning each matching primitive a random integer (0–2 for 3 texture variations) via `findattribval()`, stored as an `outs_texture`-style attribute; a MaterialX Switch node in Solaris reads this...
- **File:** tutorials/procedural-shading-tips-2-in-houdini-20.md


### Houdini 20 Procedural Shading Features
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NHD3VbE2y00
- **Author:** cgside
- **Houdini Version:** 20
- **Tags:** solaris, materials, shaders, mtlx, karma, triplanar, uv, procedural, environment, intermediate
- **Summary:** A batch of procedurally generated houses (no UVs, would be painful to texture in Substance Painter) is shaded using new Houdini 20 MaterialX/Karma nodes. A per-plank random attribute created in SOPs is loaded and fed into **MaterialX Color Correct** nodes to vary gain/hue/saturation of the base wood texture per plank, with the effect range narrowed for subtlety. The wood texture itself comes...
- **File:** tutorials/houdini-20-procedural-shading-features.md


### Export a full scene from Houdini to Unreal
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=BUJg3ILS1Aw
- **Author:** cgside
- **Houdini Version:** 19.5
- **Tags:** vex, python, pipeline, unreal, fbx, houdini-engine, instancing, procedural, advanced
- **Summary:** The scene mixes packed-primitive `Copy` instances (not `Copy to Points`) with occasional manual post-pack transforms, which breaks naive approaches: a straight `add`+delete-geometry-keep-points+`Copy to Points` round-trip works for untouched objects but silently fails for pieces that were transformed after packing (e.g. plaster walls), because the packed transform doesn't survive a plain...
- **File:** tutorials/export-a-full-scene-from-houdini-to-unreal.md


### Procedural Roof Tiles in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rvmDcbSMXh8
- **Author:** cgside
- **Houdini Version:** 19.5.598
- **Tags:** vex, uvs, divide, for-each-loop, compile-block, roof, architecture, procedural-modeling, dihedral
- **Summary:** Starting from a grid with alternating-triangle connectivity, the center points are raised and the roof pyramid's rough shape is formed, then unneeded middle edges are removed. Since copying flat tile grids directly onto the sloped roof faces gives wrong orientation, the video derives correct per-face orientation from scratch in VEX rather than relying on default aperture vectors: an "out"...
- **File:** tutorials/procedural-roof-tiles-in-houdini.md


### Compiling nested loops in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=g6PQu2FRKGo
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** vex, for-loop, optimization, performance, procedural, intermediate, advanced
- **Summary:** Compiled loop blocks execute much faster than normal for-loops but impose several hard restrictions that aren't obvious until you hit them. The core rules demonstrated: (1) nodes inside a compiled block **cannot read from other nodes via direct/named references** — any cross-reference (e.g. an Add node needing size attributes from elsewhere) must go through a **spare input** instead,...
- **File:** tutorials/compiling-nested-loops-in-houdini.md


### Procedural Wicker Basket in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Qs5Sk6QPGcM
- **Author:** cgside
- **Houdini Version:** 19.5.598
- **Tags:** sweep, vex, fuse, weaving, procedural-modeling, orient-along-curve, wicker
- **Summary:** Horizontal weave rows start as a resampled Line, Swept with Round Tube/Rows surface type, with a Ramp-controlled profile for tapering. Polyframe adds inward-pointing normals; a wrangle switches between the incoming normal and its inverse for every other point using modulo, then Peak moves points along the (possibly inverted) normal to create the wave. Curves are extracted from this, blurred...
- **File:** tutorials/procedural-wicker-basket-in-houdini.md


### Procedural Tips #3 VEX Shading and Loops
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bgUI52CFMLU
- **Author:** cgside
- **Houdini Version:** 19.5.598
- **Tags:** vex, for-each-loop, karma, materialx, rotate-to-vector, fetch-feedback, capsule, procedural-modeling
- **Summary:** For roof-tile instancing, rather than relying on a grid's default orientation (needing a Transform + "up" attribute + 90° rotation since Sweep-copied geometry aligns its Z axis to the point normal by default), a VEX-only alternative computes the normal directly: get the topmost point via bounding-box max, subtract the current position from it to get a direction vector, assign that as the...
- **File:** tutorials/procedural-tips-3-vex-shading-and-loops.md


### Creating Procedural Environment Assets in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VJ4AnxgCvQU
- **Author:** cgside
- **Houdini Version:** any modern (H18+, uses Labs Instant Meshes)
- **Tags:** heightfields, triplanar, remesh, uv, substance-painter, baking, displacement, solaris, karma, advanced
- **Summary:** A dense recap of a technique the author covers in full (~1 hour) elsewhere on Patreon, compressed into ~20 minutes here. Starts from a heightfield with hand-iterated masks (blended/blurred/remapped/noised) plus a **slope mask** (via Calculate Slope) for side-detail placement. Since raw heightfield geometry has stretched polygons that break triplanar projection, the mesh is **remeshed after...
- **File:** tutorials/creating-procedural-environment-assets-in-houdini.md


### Cleaning fractured geometry in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=n-UAPewvMgQ
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** rbd, procedural, vex, cleanup, modelling, intermediate
- **Summary:** When cutting a shape (e.g. a wood plank) with a bounding-box-driven fracture and discarding a chunk via Blast, the kept piece is left full of messy interior geometry that was only ever meant to face the removed chunk. The fix: unpack the fracture result, isolate the "keep" branch (dissolving flat edges to clean obvious wall-facing faces) and separately isolate the "remove" branch/end-pieces...
- **File:** tutorials/cleaning-fractured-geometry-in-houdini.md


### Quick Rock Cliff Setup in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=iSIXaa3rknU
- **Author:** cgside
- **Houdini Version:** 19.5.598
- **Tags:** vdb, triplanar, boolean, displacement, megascans, environment, rocks, composite
- **Summary:** A curve is drawn to define the cliff's ground silhouette; it's extruded upward, with the back seam and middle seam grouped for later use, then extruded again and pierced open on one side (one side of the branch). Boxes (scaled in Y) are copied onto resampled/point-heated points along two edge loops (with randomized p-scale and orientation, reused from an earlier shared script), matched,...
- **File:** tutorials/quick-rock-cliff-setup-in-houdini.md


### Procedural Modeling tips in houdini #2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Kc_6yws1AH8
- **Author:** cgside
- **Houdini Version:** 19.5.569
- **Tags:** extrude, uvs, material-fracture, vex, for-each-loop, displacement, architecture, procedural-modeling
- **Summary:** A tapering extrusion effect is achieved by manipulating point normals with a ramp based on curve-view position, then setting Extrude to **Point Normal** mode with "use existing normals" enabled — the ramp shape directly controls the taper profile. For horizontal tile rows on a cylinder that must respect the original topology, UV Flatten unwraps the cylinder and maps UV back to position, strips...
- **File:** tutorials/procedural-modeling-tips-in-houdini-2.md


### RBD rock surfaces with Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=015fds0mdyk
- **Author:** cgside
- **Houdini Version:** 19.5.598
- **Tags:** rbd, material-fracture, vdb, vex, packed-primitives, triplanar, karma, environment, rocks
- **Summary:** A Boolean'd box has its slope faces (excluding back/bottom) selected via a group expression testing normal Y below a threshold and normal Z, then remeshed and expanded into a natural-mask-driven Mountain distortion (with the Y axis disabled and the mask blended so the flat back face is untouched). The shape is flattened before fracturing (to allow stretching afterward) and fed **custom scatter...
- **File:** tutorials/rbd-rock-surfaces-with-houdini.md


### Cliff texturing with karma and material X
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WAyk2xCn5rs
- **Author:** cgside
- **Houdini Version:** H20+ (Solaris/Karma, MaterialX)
- **Tags:** materials, karma, triplanar, hda, uv, texturing, heightfields, vdb, intermediate
- **Summary:** Compares a custom MaterialX HDA ("CGS Triplanar," a MaterialX port of the author's earlier VEX-based triplanar tool) against the stock MaterialX triplanar node on two test spheres. The custom node projects textures without requiring UVs, exposing a randomization Seed, Tiling amount, a Triplanar Blending control (blend sharpness between the three projection axes), and a UV Blending control...
- **File:** tutorials/cliff-texturing-with-karma-and-material-x.md


### Python multi asset loader in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RQ3kSr5u16A
- **Author:** cgside
- **Houdini Version:** 19.5.303
- **Tags:** python, hou-module, automation, solaris, geometry-variants, asset-loading, scripting
- **Summary:** Rather than accepting Houdini's built-in multi-file import (which dumps everything into separate Geometry containers with no folder/naming-convention support), the script opens a folder-browser dialog, creates a Geometry container, and iterates the selected folder's subfolders. It filters to subfolders starting with a configurable prefix (e.g. "var"), dives into each variant folder to grab...
- **File:** tutorials/python-multi-asset-loader-in-houdini.md


### Python in Houdini | Absolute to relative paths
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=N5DN6SwYFVs
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** python, file-references, project-management, automation, megascans, scripting
- **Summary:** Written as a workaround for Houdini's drag-and-drop "make relative" feature failing on certain model files, the script imports `os` and `hou`, grabs `$JOB`/`$HOME` absolute paths, and iterates `hou.fileReferences()` filtered to only 3D-model and texture parameters (since USD and similar references are typically already project-relative by default). For each reference it extracts the parameter,...
- **File:** tutorials/python-in-houdini-absolute-to-relative-paths.md


### Houdini tips and tricks #2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rVduzdrKYZg
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** vex, karma, materials, shaders, mtlx, triplanar, cgi-integration, procedural, tips, intermediate
- **Summary:** **Spherical HDRI projection:** starting from a simple Grid (fit to the floor) extruded into walls/other set pieces, a **UV Project** node set to **Polar** type creates a spherical projection matching an HDRI panorama; the projection is manually transformed (translate/rotate gizmos) to align with the reference image, and the HDRI is fed into a **MaterialX Uber/Lights** shader's emission color...
- **File:** tutorials/houdini-tips-and-tricks-2.md


### Opacity maps vs Geo in Karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9wMJWyni_Uc
- **Author:** cgside
- **Houdini Version:** 19.5.534
- **Tags:** karma, rendering, optimization, opacity-maps, megascans, foliage, python, vegetation, materials
- **Summary:** A quick benchmark shows opacity-mapped grass rendering ~16x slower than the same shot without opacity maps in Karma CPU. Since removing opacity entirely loses the fine blade/leaf silhouette detail from Megascans atlases, the workaround is to trace the opacity map's silhouette into real cut polygon geometry per plate, fix normals/UVs, and reassemble the plates into full grass/plant assets (e.g....
- **File:** tutorials/opacity-maps-vs-geo-in-karma.md


### Procedural assets and shading with Houdini and MaterialX
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fSouWuGd_Tg
- **Author:** cgside
- **Houdini Version:** 19.5.403
- **Tags:** materialx, karma, vex, food, procedural-modeling, solaris, spiral, normals
- **Summary:** Individual bananas use mixed procedural/direct modeling. On the bunch, faces are selected via range nodes, mirrored for two layers, and the centroid extracted as the placement anchor. A wrangle creates outward-pointing normals, flattens the Y component, and blends the two orientations with a slider using `lerp()`, letting the artist dial in how "flat" vs "pointing out" each bunch looks, then...
- **File:** tutorials/procedural-assets-and-shading-with-houdini-and-materialx.md


### Python in Houdini  | Create a texture importer for Solaris
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=zZBkR8rk-_s
- **Author:** cgside
- **Houdini Version:** 19.5.403
- **Tags:** python, solaris, materialx, hou-module, automation, texturing, scripting
- **Summary:** Working inside a Material Library node (the script's starting reference/context), the script imports `hou` and `os`, defines a list of Substance-Painter-style channel names, and prompts the user via `hou.ui.readInput()` for the object's base name (e.g. "wood", "cloth") baked into filenames, followed by a folder-picker for the texture directory. It grabs the currently selected node (the...
- **File:** tutorials/python-in-houdini-create-a-texture-importer-for-solaris.md


### 5 Tips and Tricks for Modeling in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kAXUfg2FbYY
- **Author:** cgside
- **Houdini Version:** any (H18+, workflow is version-agnostic)
- **Tags:** modelling, procedural, vex, attributes, curves, beginner, intermediate
- **Summary:** A quick five-tip video with no single throughline — each tip is a standalone, reusable technique: (1) masking a bevel's distance by a target-driven attribute so the bevel width varies smoothly along an edge; (2) copying normals from a driving curve onto a duplicate so a beam can be moved/oriented along that curve's tangent frame; (3) constraining the viewport point-snapping gizmo to a single...
- **File:** tutorials/5-tips-and-tricks-for-modeling-in-houdini.md


### Controlling instance probability in Solaris
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OWMKqhVaFF8
- **Author:** cgside
- **Houdini Version:** H19.5+ (Solaris)
- **Tags:** solaris, instancing, scattering, attributes, beginner, intermediate
- **Summary:** A short, focused quick-tip: by default, Solaris's Instancer only offers a random distribution (with a Seed) across prototypes, plus an Index field that isn't directly useful for weighted control on its own — the actual mechanism needed is the **Prototype Index Attribute** field. To drive it, build an **Attribute Randomize** node with the attribute renamed to something identifiable (e.g....
- **File:** tutorials/controlling-instance-probability-in-solaris.md


### Christmas lights vex animation in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=u7SGkPTaJKs
- **Author:** cgside
- **Houdini Version:** any modern (H18+)
- **Tags:** vex, animation, instancing, lighting, beginner, intermediate
- **Summary:** A short, beginner-friendly example of instancing actual light objects (not geometry) and driving their per-instance intensity with VEX. Since lights can't be instanced via the normal geometry-instancing path, the trick is setting the Instancer's method to **Reference** so it duplicates the light object itself onto each point, then pruning the original so it doesn't render directly. Each...
- **File:** tutorials/christmas-lights-vex-animation-in-houdini.md


### Quick color jitter with karma
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=utIfflheFqc
- **Author:** cgside
- **Houdini Version:** 19.5.435
- **Tags:** karma, materialx, hda, color-jitter, geometry-property-value, instancing, stadium
- **Summary:** Demonstrated on an instanced stadium-seat scene where all seats render the same flat color, an **Attribute Randomize** node creates a `1@jitter` (or similarly named) attribute per instance with min/max 0–1. In the material network, a **Geometry Property Value** node (the MaterialX/Karma equivalent of Arnold's User Data Float/Color) reads that attribute by name; feeding it directly into a...
- **File:** tutorials/quick-color-jitter-with-karma.md


### Environment creation with Solaris in Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2f_40GhnBXI
- **Author:** cgside
- **Houdini Version:** 19.5
- **Tags:** solaris, lops, usd, scattering, instancing, vex, materials, shaders, arnold, procedural, environment, advanced
- **Summary:** The terrain (a Null "outrain" wired to the SOP terrain output) is imported into an empty Solaris stage, lit with a Dome light (fixed light-format bug, Arnold camera samples set low for iteration), and shaded via an **Arnold Material Builder**: a Standard Surface driven by a State Vector (shading normal → Y component) feeding a Ramp for a height-based color mask, blended against...
- **File:** tutorials/environment-creation-with-solaris-in-houdini.md


### Environment Creation with Houdini - Part 1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nGKGXKw4_Zw
- **Author:** cgside
- **Houdini Version:** 19.5
- **Tags:** heightfield, terrain, procedural, scattering, vex, environment, intermediate
- **Summary:** Starts with a base **Heightfield** (custom dimensions, initial noise, blurred since fine detail isn't needed yet), then divides the terrain into "back hills" vs. "front fields" using a hand-shaped curve: a centered line sized to the heightfield's width, point-jittered and displaced along Z only, then resampled with the "subdivision curves" smoothing option. That curve is poly-extruded into a...
- **File:** tutorials/environment-creation-with-houdini---part-1.md


### Procedural Bricks with Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-5cycyb5m-E
- **Author:** cgside
- **Houdini Version:** 19.5.398
- **Tags:** beginner, hscript-expressions, bricks, procedural-modeling, groups, box-clip, architecture
- **Summary:** A portion of the tower's polygon faces is selected using the polycount display (`11 of 22`) and blasted off to be replaced by a brick pattern. A Grid is Match-Sized to the extracted section, then Face Set separates each face for an Exploded View check. A **Group by Range** selects every other row/column using an expression based on the grid's column count (columns − 1, and columns × 2) so...
- **File:** tutorials/procedural-bricks-with-houdini.md


### Procedural Modeling  | First steps with Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=L3Rvvv6pZ_8
- **Author:** cgside
- **Houdini Version:** 19.5.398
- **Tags:** beginner, boolean, revolve, groups, architecture, gothic, polywire, procedural-modeling
- **Summary:** Starting from a subdivided circle clipped in Y, two copies are Boolean-subtracted (one offset in X) using Curve nodes to select portions of each circle (playing with "keep outside/inside" toggles) to produce the classic pointed Gothic arch profile. The profile is transformed back to origin, clipped, resampled for smoothness, and Revolved into a solid frame; points are fused (important for...
- **File:** tutorials/procedural-modeling-first-steps-with-houdini.md


### Cookies and chocolate | Modeling, shading and Sim
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c90ervPv5ro
- **Author:** cgside
- **Houdini Version:** any modern (H19+, uses Exoside QuadRemesher)
- **Tags:** vdb, flip, fluid, materials, karma, procedural, uv, baking, mardini, advanced
- **Summary:** **Cookie modeling**: starts from a Tube shaped via a relative-bounding-box ramp mask and a position-tapering VEX snippet, converted to VDB, then heavily detailed entirely in volume space using **Volume Sample** to distort position with layered noises (turbulence, Worley F2F1 inverted-and-distorted, masked to protect the bottom) plus an *unclamped* Fit Range trick (creating a hard-clipped...
- **File:** tutorials/cookies-and-chocolate-modeling-shading-and-sim.md


### All* the Procedural Modeling tricks in one video
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ba3Py4lodL8
- **Author:** cgside
- **Houdini Version:** any modern (H19+, uses Exoside QuadRemesher)
- **Tags:** modelling, procedural, vex, uv, vellum, quadremesh, advanced
- **Summary:** A dense, single-take breakdown of building a stylized architectural/upholstery-like panel shape entirely proce41rally. Starts from a circle divided into quadrants via Voronoi Fracture (points placed with a short VEX snippet using bounding-box min/max/center), builds a rotated, scale-compensated base profile, manually meshes the resulting curves by splitting/skinning them in controlled column...
- **File:** tutorials/all-the-procedural-modeling-tricks-in-one-video.md


### Procedural Animation with RBD
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RbiH315adq8
- **Author:** cgside
- **Houdini Version:** 20.5.322
- **Tags:** rbd, simulation, packed-primitives, karma, procedural-animation, food, torque, velocity
- **Summary:** The barrel/lid are simulated first with RBD Configure (convex hull collision, packed fragments) and a randomized initial torque (high amplitude due to scene scale) so the lid pops and settles, with angular velocity damped down after frame 144 via the RBD Bullet Solver so the barrel comes to rest. For the fill: the barrel's cap/patch-group opening is transformed/scaled/given normals so it can...
- **File:** tutorials/procedural-animation-with-rbd.md


### Procedural Cliff Techniques
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YLrE1Zww_uc
- **Author:** cgside
- **Houdini Version:** 20.5.588
- **Tags:** vdb, voronoi-fracture, compile-block, triplanar, karma, materialx, solaris, concavity, curvature, scattering, environment, rocks
- **Summary:** A box gets low-subdivision tubes copied on and merged for a rough boulder base, then remeshed to a grid-like voxelized look via Blur/Peak/Mountain and Boolean-intersected for surface damage, before VDB conversion. Cuts across the cliff are placed by laying a line along it, resampling to 5 segments, jittering interior points (not endpoints), copying grids at each point (offset by the Metaimport...
- **File:** tutorials/procedural-cliff-techniques.md


### Environment Technical tips and tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bqyaPvWT5Gc
- **Author:** cgside
- **Houdini Version:** 20.5
- **Tags:** solaris, lops, vex, procedural, scattering, instancing, cops, compositing, karma, environment, tips, intermediate
- **Summary:** For tree LOD/collision proxies: unpack the tree, scatter points across it, and run **Particle Fluid Surface** on those points to generate a simplified blob mesh usable as a Solaris viewport/bound proxy — much faster than manually retopologizing. For making scattered rocks lay flat: measure each primitive's area, loop to compute primitive normals, identify the largest-area primitive as the...
- **File:** tutorials/environment-technical-tips-and-tricks.md


### Procedural Hard Surface Modeling Tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pTQGJM0k9b0
- **Author:** cgside
- **Houdini Version:** 20.5.310
- **Tags:** hard-surface, boolean, vex, procedural-modeling, uvs, attribute-blend, tapering
- **Summary:** To remove a tube's end alpha non-destructively, the sweep's UVs are computed, the UV boundary extracted, expanded, and promoted to primitives, then the inverted group is blasted away. A Curveu attribute (saved earlier) drives a tapering effect via a Point VOP mixing the current geometry with a Peaked version, using Fit Range to shape the transition, with the effect suppressed on the opposite...
- **File:** tutorials/procedural-hard-surface-modeling-tips.md


### Procedural Tips: Flow Maps, RBD Emit and more
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XFOiCiljWh8
- **Author:** cgside
- **Houdini Version:** 20.5.550
- **Tags:** flow-maps, cops, rbd, materialx, karma, vex, solaris, product-viz, liquid, umbrella
- **Summary:** A glass profile is revolved, with an inside-liquid point range saved and promoted to primitives so the liquid geometry can be extracted from the same revolved mesh. MaterialX's Flow Map (set to vertex-color mode, since the viewport-shader FlowMap-visualize node has a known bug) drives liquid swirl using a custom VOP COPs generator: two noises, one distorting the position of the other using the...
- **File:** tutorials/procedural-tips-flow-maps-rbd-emit-and-more.md


### Procedural UVs - UV Layout Node in Depth
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7kUDLsNn0iA
- **Author:** cgside
- **Houdini Version:** 20.5.551
- **Tags:** uvs, uv-layout, udim, procedural-uvs, vex, pebbles, texturing
- **Summary:** Beyond basic auto-unwrapping, UV Layout accepts custom primitive attributes to control exactly how islands are cut, stacked, distributed across UDIMs, scaled, and even used to pack non-UV geometry without overlaps. A window-frame example shows edge-group-driven cutting to maximize texture coverage (20%→70%). An "island" integer attribute (promoted to primitive) lets repeating geometry (8...
- **File:** tutorials/procedural-uvs---uv-layout-node-in-depth.md


### Procedural House Generator
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rzWUiyF9EJI
- **Author:** cgside
- **Houdini Version:** 19.5.752
- **Tags:** procedural-modeling, buildings, vex, xyzdist, boolean, roof, windows, architecture, environment
- **Summary:** The house starts from a grid whose dimensions use `fit()` + `random()` for size variance within a range, with middle points transformed and sides bridged for a simple tapered footprint. A tapering effect on the profile uses a Ramp over relative bounding-box X, mirrored via a formula so only one side needs authoring. Windows/doors come from extracting the wall silhouette as curves, filtering...
- **File:** tutorials/procedural-house-generator.md


### Procedural Rock Formations  Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6GV1b8Ed_JI
- **Author:** cgside
- **Houdini Version:** 19.5.752
- **Tags:** rbd, fracture, vdb, triplanar, shortest-path, vines, procedural-modeling, rocks, environment, texturing
- **Summary:** A cube is fractured and transformed into "boulder" shapes, given edge damage, and centered as reusable assets. These are copied onto scattered points over a circular patch, where a **radial mask (normalized distance from edge to center)** drives the Y-scale (longer shapes toward the center) via Remap, plus randomized overall scale/normal jitter — producing a natural mounded arrangement. VDB...
- **File:** tutorials/procedural-rock-formations-part-2.md


### Procedural Grapes and how to avoid intersections
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9bq2Zx5zcIk
- **Author:** cgside
- **Houdini Version:** 19.5.593
- **Tags:** vellum, vex, quaternion, branching, procedural-modeling, simulation, food, intersections
- **Summary:** The main stem comes from a line resampled by density (ramp mode) to concentrate branch points toward the top, given a Point VOP-authored p-scale and grouped for later sweeping. First-level branches are built by copying a distorted line onto the stem points, using a curve to bound start/end and reducing p-scale via a natural-log-adjusted float; orientation comes from the quaternion output of...
- **File:** tutorials/procedural-grapes-and-how-to-avoid-intersections.md


### Procedural Champions League football in 2 minutes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kpWtT6tPvP0
- **Author:** cgside
- **Houdini Version:** 19.5.593
- **Tags:** platonic-solids, for-each, vex, uvs, sweep, procedural-modeling, ray-project, sports
- **Summary:** A Platonic solid preset provides the base panel layout; each primitive is named, subdivided, and Ray-projected onto a sphere for a spherical starting form. Inside a for-each loop over each named primitive, normals point inward, the shape is subdivided, and a target point is picked to recreate a 5-pointed star by picking along existing normals, subdividing, and scaling down. Normals are...
- **File:** tutorials/procedural-champions-league-football-in-2-minutes.md


### Add details with regions from image labs tool
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qS5uDc8EePQ
- **Author:** cgside
- **Houdini Version:** H20.5+ (Labs Regions from Image tool)
- **Tags:** vellum, cloth, labs-tools, procedural, texturing, image-based, intermediate
- **Summary:** A quick workflow for turning a 2D color-coded reference image (made in Photoshop, with each intended piece painted a distinct flat color for easy separation) into a set of simulated cloth props. The Labs Regions from Image node auto-detects each color region as a separate named piece, which are then resampled/remeshed, corner-selected via curvature analysis, pinned, and brushed into a draped...
- **File:** tutorials/add-details-with-regions-from-image-labs-tool.md


### Rock formations with heightfields
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rEn0ochILjU
- **Author:** cgside
- **Houdini Version:** 19.5.593
- **Tags:** heightfields, terrain, triplanar, displacement, ambient-occlusion, texturing, rocks, environment
- **Summary:** Starting from a hand-drawn Heightfield mask, a Heightfield Layer mix (set to Maximum) blends two versions of the mask (one blurred) to build up the base silhouette. A Voronoi-based random-height pattern (via a random function seeded per point) adds per-point height variation, scaled and masked. Mask Expand grows/blocks out squarish base shapes, followed by blurring and mask-clearing between...
- **File:** tutorials/rock-formations-with-heightfields.md


### Ruins randomized brick wall
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QEvlyVTk4Jw
- **Author:** cgside
- **Houdini Version:** 19.5.593
- **Tags:** voronoi-fracture, vex, procedural-modeling, bricks, ruins, environment, connectivity, compile-block, texturing
- **Summary:** Rather than a uniform brick grid, the wall is built by extracting bounding-box-derived guide curves along Y, X, and Z, resampling them into sections, jittering the interior points (endpoints preserved), cutting at each point, and subdividing for consistency. The key realism trick is fracturing each "layer" (row) with its own randomized jitter seed inside a for-loop using the detail iteration...
- **File:** tutorials/ruins-randomized-brick-wall.md


### Procedural Rock Wall without intersections
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=q-9cVBVMv2E
- **Author:** cgside
- **Houdini Version:** 19.5.593
- **Tags:** rbd, simulation, scatter, packed-primitives, procedural-modeling, environment, stone-wall
- **Summary:** Individual rocks are modeled once in a loop, each generating both a high-poly render version and a very low-poly proxy for simulation. The low-poly proxies are copied to scattered points (using a Scatter node with many relaxation iterations to reduce initial overlap), then fed into an RBD Bullet Solver alongside a **Bound** node (all-sides collision box) whose Y-scale is animated from 1 down...
- **File:** tutorials/procedural-rock-wall-without-intersections.md


### Procedural tips | Heightfields and VDB
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ue-Wuo87YJI
- **Author:** cgside
- **Houdini Version:** 19.5.593
- **Tags:** heightfields, vdb, terrain, vex, volumes, optimization, masks
- **Summary:** Heightfield Pattern combined with Remap creates elevation masks (height/center controls). A second Heightfield Pattern (Chippy Shapes) masks where Erosion is applied so cliff-like breakup only appears in some areas rather than uniformly, since Erosion's default look isn't great everywhere. For growing/shrinking a masked area, playing with a noise's **bias** works better than Mask Expand. For...
- **File:** tutorials/procedural-tips-heightfields-and-vdb.md


### Procedural VDB Cookies
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WKs4KHfHpyA
- **Author:** cgside
- **Houdini Version:** 19.5.534
- **Tags:** vdb, volumes, vex, noise, cops, food, karma, solaris, procedural-modeling
- **Summary:** Starting from a clipped, flattened sphere closed with Polyfill and beveled/subdivided for a smooth VDB input, the cookie shape is converted to a VDB and detailed inside a Volume VOP with four layered noises of increasing fineness. A key trick is exporting the relative-bounding-box Y-component as a visualizable mask (via a Color node feeding CD into VDB from Polygons, then Attribute from Volume...
- **File:** tutorials/procedural-vdb-cookies.md


### UV Randomizer - Texturing multiple objects
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FK6IRzxYHiY
- **Author:** cgside
- **Houdini Version:** 19.5.493
- **Tags:** uvs, texturing, connectivity, sort, vex, procedural-uvs, tiling
- **Summary:** Instead of stacking every duplicate's UVs on top of each other for maximum texture density (which causes obvious pattern repetition), a wrangle assigns each piece an integer ID within a chosen range (the "how many distinct UV islands" control). UV Layout then stacks pieces sharing the same ID on top of each other, but lays out different IDs into separate regions — trading a bit of texture...
- **File:** tutorials/uv-randomizer---texturing-multiple-objects.md


### Quick asset creation with VDB
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=j0s0HkBCaQQ
- **Author:** cgside
- **Houdini Version:** 19.5.493
- **Tags:** vdb, volumes, vex, noise, zbrush, displacement, solaris, rocks, environment
- **Summary:** Compared to the studio's more elaborate cliff tutorials, this one keeps the Volume VOP setup deliberately simple — two main noise layers, each distorted by a secondary noise — to produce a quick rock asset. Frequency is controlled with an intuitive Constant/Divide-by-Constant pair instead of raw exponents, and a Multiply Constant scales the overall displacement strength. The second main noise...
- **File:** tutorials/quick-asset-creation-with-vdb.md


### VDB Procedural Cliffs
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fBhtlmCGrK4
- **Author:** cgside
- **Houdini Version:** 19.5.435
- **Tags:** vdb, volumes, vex, noise, solaris, karma, environment, cliffs, rocks, scattering, instancing
- **Summary:** A simple box is extruded and beveled, then hit with a Mountain node to break up the base silhouette before converting to VDB. Inside the Volume VOP, four cascading noise layers each displace the incoming density (or distort the position feeding the next noise): a base Unified Noise displacement distorted by a secondary noise, a Manhattan Cellular pattern with an increased range mean for...
- **File:** tutorials/vdb-procedural-cliffs.md


### Procedural Modeling tips for beginners
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rhRaQa-a8q4
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** beginner, procedural-modeling, groups, extrusion, ramp, copy-to-points, polyframe, group-by-range, vex
- **Summary:** Starting from circles scattered on a grid and covered with a boolean-unioned grid, sharp transitions between the shapes are blended away with a high-value Smooth node. A tapering/profile extrusion is shaped using the built-in ramp under the Extrude node's Thickness parameter (values can exceed 1 to overshoot the boundary). Extrude's "Output Geometry and Groups" option is used to procedurally...
- **File:** tutorials/procedural-modeling-tips-for-beginners.md


### Bird Flocking Simulation And Rendering In Houdini | Pro Karma Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=k2fZVt9ezQo
- **Author:** Rebelway
- **Houdini Version:** 19.5.716
- **Tags:** pop-network, flocking, karma-fog, ocean-spectrum, solaris, birds, rebelway, simulation
- **Summary:** The environment starts from a simple grid sculpted into sharp mountain silhouettes using layered Chebyshev Cellular and Spark Convolution noise, then a **Soft Transform** (created with a point selection pre-made so its pivot centers correctly) flattens the front foreground area into a usable "beach" zone before the noise ramps into peaks; a duplicated, scaled-up copy of the same mountain adds...
- **File:** tutorials/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial.md


### Learning Vex - Recreating attribute reorient sop
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=TAWtLzrITOY
- **Author:** cgside
- **Houdini Version:** Not specified
- **Tags:** vex, matrix, attribute-reorient, custom-function, uv-space, learning-vex, cross-product
- **Summary:** The motivating problem: measuring the **gradient of `P.y`** on a 3D mesh gives a vector attribute that correctly "flows" along the surface's Y-height direction — but if that mesh is then moved into UV space (via Attribute Swap, copying UV into position), the gradient vectors no longer make sense relative to the new flattened shape, since they were computed for the original orientation. The...
- **File:** tutorials/learning-vex---recreating-attribute-reorient-sop.md


### Gestation Effect in Houdini. Scene Breakdown.
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JiQyPj-rLII
- **Author:** Pixel In The Frame
- **Houdini Version:** Not specified
- **Tags:** vellum, voronoi-fracture, pyro, particle-trails, vdb-blend-shapes, cell-division, gestation, pixel-in-the-frame
- **Summary:** The base simulation follows a known Vellum-based cell-splitting method (referencing Tim van Helsdingen's original tutorial on cell-splitting with the Vellum solver) using **Vellum Configure Balloon** for constraints and a pressure-group output, with rest-length values controlled live from a top network via a Vellum Constraint Properties node. Key deviations from the reference technique:...
- **File:** tutorials/gestation-effect-in-houdini-scene-breakdown.md


### Vellum Fundamentals - Week 5: Cell Splitting Part 1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Q4R7AeCf-Os
- **Author:** Tim van Helsdingen
- **Houdini Version:** Not specified
- **Tags:** vellum, sop-solver, multisolver, dop-network, cell-splitting, vellum-fundamentals, tim-van-helsdingen
- **Summary:** The video opens by demonstrating exactly why removing points/primitives from a live Vellum sim breaks it: a basic Vellum Configure Balloon setup (built inside a DOP network, sourcing geometry and constraints from the first and second inputs via backtick-quoted `opinputpath` expressions, merged with a ground plane and gravity) produces a normal soft-body ball; but deleting a group of points at...
- **File:** tutorials/vellum-fundamentals---week-5-cell-splitting-part-1.md


### Vellum Fundamentals - Week 5: Cell Splitting Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=G7SnVk4Jj8U
- **Author:** Tim van Helsdingen
- **Houdini Version:** Not specified
- **Tags:** vellum, voronoi-fracture, multisolver, sop-solver, rest-attribute, triplanar, cell-division, vellum-fundamentals, tim-van-helsdingen
- **Summary:** Work begins outside the DOP network to prototype the actual "split" operation cheaply: a sphere is Scattered with 2 points and run through **Voronoi Fracture**, seeded by `$F` so the fracture direction changes if re-evaluated; an Exploded View confirms it cleanly separates into two convex halves. Since a Voronoi-fractured half is hollow on the cut face, a **Remesh** (smaller target size for...
- **File:** tutorials/vellum-fundamentals---week-5-cell-splitting-part-2.md


### Houdini Tutorial // Daily Fun / Alien Tendrils
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XLiXackQH_k
- **Author:** Tim van Helsdingen
- **Houdini Version:** 19.5
- **Tags:** tendrils, curl-noise, curve-view, redshift-strands, random-walk-sss, pop-network, compositing, fusion, tim-van-helsdingen
- **Summary:** This is a scene breakdown of a quick "daily render" (not a formal step-by-step tutorial). The base look comes from a 10-node "tendrils" subnetwork that is instanced ("Copy to Points" via a Fast Point Instance-style instance node) around the scene rather than modeled once at full scale. Inside the patch: a grid gets displaced with a mountain SOP for base relief, then two separate scatters (each...
- **File:** tutorials/houdini-tutorial-daily-fun-alien-tendrils.md


### Particle rotations in Houdini (how to rotate orient)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gmN76ZeObsA
- **Author:** the point and prim
- **Houdini Version:** Not specified
- **Tags:** quaternions, particle-rotation, orient-attribute, vex, vops, point-vop, the-point-and-prim
- **Summary:** The video explains how to rotate large numbers of particles procedurally, without simulating anything, by manipulating the native Houdini `orient` attribute (a Vector4/Quaternion) directly. Starting from a single point, an **Attribute Randomize** node creates the `orient` attribute as a 4-component vector (a Quaternion — described as the least ambiguous way to store 3D rotation). Inside a...
- **File:** tutorials/particle-rotations-in-houdini-how-to-rotate-orient.md


### Procedurally mask deforming / animated geometry - Houdini
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UL-VdOBmXgE
- **Author:** the point and prim
- **Houdini Version:** Not specified
- **Tags:** smooth-function, distance-along-geometry, masking, procedural-animation, rest-attribute, performance-optimization, the-point-and-prim
- **Summary:** Building on a prior video's flat, single-axis smooth-function mask, this tutorial shows how to art-direct a mask that spreads outward from arbitrary points across curved or deforming geometry — demonstrated first on a subdivided/remeshed triangulated bust model (with a callout that the USD Import LOP re-imports every frame unless pinned to a static frame number). The key node is **Distance...
- **File:** tutorials/procedurally-mask-deforming-animated-geometry---houdini.md


### Houdini: How to mask with the smooth function
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7U8slXjQ3-s
- **Author:** the point and prim
- **Houdini Version:** Not specified
- **Tags:** smooth-function, masking, procedural-animation, rel-bbox, vops, particle-simulation, pyro, the-point-and-prim
- **Summary:** This is the opening video of a new "core techniques" series (as opposed to the channel's usual full-effect tutorials), focused on foundational, low-level building blocks reusable across many effects. The demo starts with a simple box, remeshed for resolution, moved into a 0–1 space, with a Point VOP driving everything. **Relative Bounding Box** (`relbbox`) returns the geometry's bounds...
- **File:** tutorials/houdini-how-to-mask-with-the-smooth-function.md


### Art directing large scale RBD sims in Houdini using the up-res method
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=M6E3f3yY824
- **Author:** the point and prim
- **Houdini Version:** Not specified
- **Tags:** rbd, up-res, voronoi-fracture, solaris, karma-cpu, usd, procedural-lop, art-direction, the-point-and-prim
- **Summary:** This is a follow-up to the author's RBD up-res R&D video, focused on the core concepts rather than every node in the (large) project file: base fracture, guide/proxy sim, secondary (high-res) fracture, and — most importantly — the "up-res system" that decides which high-res pieces activate, plus a Solaris/Karma CPU rendering pass. The motivating problem: standard RBD iteration (sim at final...
- **File:** tutorials/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method.md


### Houdini USD RBD Procedural LOP in under 5 minutes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ixJvo0iShiM
- **Author:** the point and prim
- **Houdini Version:** Not specified
- **Tags:** rbd, usd, solaris, procedural-lop, transform-pieces, piece-name, karma, the-point-and-prim
- **Summary:** A short, practical breakdown (part of the author's larger RBD up-res R&D work) on why RBD rendering gets awkward once it moves into Solaris/USD, and how to fix it in two wrangles. The setup problem: **Transform Pieces** (a SOP-level node any experienced RBD artist knows) loads a render-resolution fracture once and applies per-frame orientation/translation from a much lighter point cloud,...
- **File:** tutorials/houdini-usd-rbd-procedural-lop-in-under-5-minutes.md


### Techniques for Fast Disintegration FX in Houdini – A Particle & Attribute Approach
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Syn7XjeCH_8
- **Author:** the point and prim
- **Houdini Version:** Not specified
- **Tags:** disintegration, particle-simulation, distance-along-geometry, smooth-function, materialx, karma-xpu, quaternion-blend, the-point-and-prim
- **Summary:** Framed as a breakdown rather than a formal tutorial, this video shows how combining simple attribute tricks with particle simulation avoids the long sim times of more literal destruction approaches. The mask driving the whole effect reuses the channel's own toolkit: **Distance Along Geometry** from a handful of manually-selected art-directed points produces a `dist` attribute, which is...
- **File:** tutorials/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach.md


### Houdini 22 | How to Create Pyro in COPs | Configure Pyro Recipes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xKrHwJRo-nI
- **Author:** Houdini (official SideFX)
- **Houdini Version:** Houdini 22
- **Tags:** cop, pyro, volumes, simulation, compositing, intermediate, houdini-22
- **Summary:** Official walkthrough of the H22 COP Pyro Recipes (Billowy Smoke + Fire), built on the COPs Pyro Block 2.0 where all solver controls (bounds, collisions, sourcing, fields, forces) live on the Block End node — no solvers inside the loop. Covers Pyro Configure (voxel size → reference VDB), implicit-surface Pyro Source Shape emitters with animated distortion, rasterizing 3D volumes to 2D via Rasterize Volume + Pyro Light Ambient/Light Scatter through COPs' built-in camera operators (frustum far plane = image plane), and 3D preview via VDB Visualize colored with Mono to RGB on temperature (black-to-orange ramp) wired through Pyro Light Ambient into CD/emit CD. Demo values: density scale 15, emission scale 45.
- **File:** tutorials/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes.md


### H22 - Gaussian Splats and Machine Learning | Jakob Ringler | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=LBkowc4gfjs
- **Author:** Houdini (official SideFX — Jakob Ringler, TD)
- **Houdini Version:** Houdini 22
- **Tags:** cop, top, pdg, compositing, rendering, karma, solaris, usd, advanced, houdini-22
- **Summary:** HIVE talk on H22's three ML pillars. (1) Neural Cellular Automata in COPs: per-cell mini-CNNs grow trained textures (NCA Core + NCA Decode split architecture, up-res ≤8x, always tileable); ML Train NCA recipe (128×128 training, features ≤10–15 px); inference controls — update masks, kernel rotation, perception scaling, COPs injected into the solve loop, self-healing regrowth; seamless on meshes via new adjacency rasterization; latent-space blending of two NCAs trained with alternating targets. (2) New neural COPs: Neural Layer to Mask (Meta SAM 2 — click/bbox prompts, confidence + embeddings outputs enable iterative self-refinement) and Neural Layer to Depth (Microsoft MoGe-2 — depth/normal/position + camera from one image; single-image PBR texturing; GSplat point output). (3) Native Gaussian-splat training: LOPs recipe + ML Process/Train GSplats TOP nodes optimize point clouds from Karma EXRs (camera metadata free in EXRs) or COLMAP photo datasets; trains extra AOVs (normal/albedo) enabling COPs relighting via Rasterize GSplats; live browser training viewer; PLY/USD export; 4D via per-frame velocity-advected checkpoints.
- **File:** tutorials/h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive.md


### Houdini 22 | How to Destroy Metal | 1 | Tearing
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=x-N5I4XS7Q4
- **Author:** Houdini (official SideFX)
- **Houdini Version:** Houdini 22
- **Tags:** rbd, dop, sop, simulation, intermediate, houdini-22
- **Summary:** Part 1 of the official H22 metal-destruction series: tearing sheet metal with RBD Material Fracture in Metal mode (glue + soft bending constraints; edge detail via detail size / noise height / element size), RBD Configure with a bounding-box Active region (pin top/sides) and Metal/Aluminum physical density, RBD Bullet Solver with an animated collider + ground plane and a lowered constraint detach distance (~0.1), then the new RBD Deform Pieces node with Boundary Connection switched from Cluster Attribute (dent-only) to Constraints (true tearing). Stabilizes springy metal via dampening ratio ×4000 + reduced angular dampening/stiffness, and shows the thick-wall variant: PolyExtrude (−0.01, output back) + Reverse/Normal → Material Fracture set to Solid with fewer scatter points and glue 100.
- **File:** tutorials/houdini-22-how-to-destroy-metal-1-tearing.md


### Houdini 22 | How to Destroy Metal | 2 | Denting
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=R4YVz0FcCOw
- **Author:** Houdini (official SideFX)
- **Houdini Version:** Houdini 22
- **Tags:** rbd, dop, sop, simulation, intermediate, houdini-22
- **Summary:** Part 2 of the official H22 metal-destruction series: denting a wall with cannon-fired steel balls. Key idea — Secondary Fracture in Proxy Only mode fractures only the collision proxy so large render fragments bend with interior detail, while Refine Geometry: Bricker subdivides the render mesh to support the deformation. Covers staggered RBD emission ($F%10 delete + v×alligator-noise cannon, emit attribute 1/0 via RBD Configure, RBD Pack→Merge→Unpack→Bullet Solver with Emit RBDs), Steel vs Aluminum physical presets, restricting constraint deletion to the primary fracture ID (metal_fracture) so tears follow primary seams while secondary pieces only bend, and RBD Deform Pieces boundary connection via the parentpiece cluster attribute.
- **File:** tutorials/houdini-22-how-to-destroy-metal-2-denting.md


### Messing with the Edit node in Houdini 22
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Wkj1DMn-X2w
- **Author:** cgside
- **Houdini Version:** Houdini 22
- **Tags:** lop, solaris, usd, rbd, sop, procedural, intermediate, advanced, houdini-22
- **Summary:** Fixing the H22 Edit node's physics-mode collisions (LOPs): default sim geometry is convex hulls, so concave shapes fail — author proxy-purpose collision meshes via Convex Decomposition (Max Concavity tuning), Voronoi-fracture + per-piece decomposition to preserve holes, and ramp-driven relbbox clustering (chramp → rint cluster ids → per-cluster Convex Hull) for segmented boxes; assign render/proxy purposes with Configure Primitive, build variants in a component graph, and work around tiny scene scale with a root USD Transform scale + inverse.
- **File:** tutorials/messing-with-the-edit-node-in-houdini-22.md


### Houdini 22 | How to Create Terrains in COPs | Utilize Height Fields
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5v9lmJcIrIw
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** cop, procedural, volumes, attributes, intermediate, houdini-22
- **Summary:** Official SideFX walkthrough of building terrain in Copernicus: the HeightField COP Network preset (border clamp, ZX-plane canvas, km-scale Uniform Scale), a height-typed Layer deforming a live grid, and the HF stack — HF Noise (Hybrid Terrain fractal), HF Terrace (Compute Range, Random Step 1, seed picking), HF Erode (keeps terraced ledges), HF Strata (Amplitude 10, Element ~340, Strata ~15) — then HF Visualize colored via Mono to RGB with the new terrain ramp presets, plus an Add + Fractal Noise before the color mapping so color stops tracking height 1:1.
- **File:** tutorials/houdini-22-how-to-create-terrains-in-cops-utilize-height-fields.md


### H22 - KineFX Rigging and Procedural Animation | Henry Dean | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0YNaNZkjwoM
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** rigging, animation, procedural, attributes, sop, advanced, houdini-22
- **Summary:** HIVE talk: rigging Dany Bittel's G-splat centipede in H22 — Bake GSplats to a point cloud (Bone Deform/Transform just work; `scale` is deliberately 3 floats, cast to vector only while scaling), kit-bash a clean rest pose from segments via Copy to Points, Capture Proximity skinning (no topology), a wheel-phase metachronal-wave gait driven by distance traveled, Spline IK body + rig-built antenna joints reused upstream, and procedural animation injected into the animate state via parameter dictionary → MotionClip → Channel Prims from MotionClip → APEX animation layers. H22's pcapdata removal called out as a major QoL win.
- **File:** tutorials/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive.md


### H22 - Gaussian Splats | Peter Sanitra | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HUTd8BHNHKI
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** solaris, usd, cop, top, pdg, volumes, karma, rendering, advanced, houdini-22
- **Summary:** Full H22 synthetic G-splat pipeline (Peter Sanitra, NVIDIA): single Solaris recipe → auto camera rigs (SOP cameras + Copy to Points; optimal-placement algorithm for interiors), OpenEXR ground truth from any Hydra renderer, TOPs training (Default prune-and-grow vs Monte Carlo fixed-count; stop at the ~30–40k-iteration loss plateau), AOV feature training (normal/albedo/subsurface) enabling COPs GSplat Rasterize relighting, PLY/USD export via the new Pixar splat schema. Volumes 10× smaller than VDB with HDR intact; fur/whisker capture; deform-static-splat animation; failure modes = camera coverage, glass/mirrors, HDR clamping, VRAM, no temporal training.
- **File:** tutorials/h22---gaussian-splats-peter-sanitra-houdini-22-hive.md


### H22 - Copernicus and Time Shift | Jakub Spacek | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EUjZ7ObaN1Y
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** cop, procedural, simulation, solaris, karma, advanced, houdini-22
- **Summary:** HIVE talk stress-testing H22's adjacency nodes on a badly-UV'd statue scan: Geometry to Adjacency cables (Cable Unpack, pass-through green inputs skip per-frame recompute), Adjacency Distort bridging UV islands, Adjacency Attribute Sample fixing noise mapping, a block-solver paint-spread (Slope Direction + distorted noise), leading edge via the new Time Shift node ($F−10 subtract), seam-free blur-in-block (small radius × ~500 iterations), masked Turing pattern + Ripple solver layers, hue/sat remapping, Solaris/Karma lookdev with Material Linker. Practical notes: fix overlapping UV islands (Labs node), bake 4K COPs output, X toggles flat/3D preview.
- **File:** tutorials/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive.md


### H22 - Animation | Motion Mixer | Sasa Budimir | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VaUleTuvWgA
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** animation, rigging, rbd, simulation, solaris, intermediate, houdini-22
- **Summary:** HIVE talk: "minimum viable animation" knight-puppet workflow — tiny all-FK clip library planned from an animatic, Motion Mixer choreography (drag=loop, Shift+drag=retime, blend overlaps, search filter, root/cycle controls), additive noise tracks with keyframed weights, H22 nested clips for sliding noise independently of top-level keys, and a ragdoll pass supplying all secondary motion (fracture/shrinkwrap collision shapes; Configure Joint Limits auto-extracted from keyframed limb-swing poses). Cardboard set + Solaris/Karma lookdev, Copernicus compositing.
- **File:** tutorials/h22---animation-motion-mixer-sasa-budimir-houdini-22-hive.md


### H22 - Modeling & Solaris | Fianna Wong | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=CFr-1PANhsk
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** modelling, sop, lop, solaris, usd, cop, karma, instancing, intermediate, houdini-22
- **Summary:** HIVE talk (SideFX): SOPs-first USD bike-shop assembly — image-to-3D asset sourcing cleaned by the new rectangular Quad Remesh (always precede with Remesh; try both modes), render-time Scatter Instances (prototypes/weights, Karma-only visibility, relax iterations for interpenetration), implicit-surface booleans (resolution-independent quad output), sculpt QoL (G floating menu, lazy-mouse visualizer), Texture Material Library hosting COP nodes directly, and the new USD Create Component + USD Parent Geometry SOPs that author a tidy USD hierarchy without leaving SOPs. PolyHaven/GLTF tips included.
- **File:** tutorials/h22---modeling-solaris-fianna-wong-houdini-22-hive.md


### H22 - KineFX Rigging and Animation | Max Rose | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2jZjaEzLdco
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** rigging, animation, rbd, simulation, procedural, intermediate, advanced, houdini-22
- **Summary:** HIVE talk (SideFX): jack-in-the-box driven by ~2 keyframes — spiral-spring rig via centerline trick + group-based Parent Joints, parent rigs in KineFX before entering APEX, Pack Character + Spline auto-rig on a tagged coil, Configure Ragdoll recipe with hand-simplified proxy geometry, layer-per-limb weights to stiffen ragdoll, SDK component fired by the crank control (sample rotate-X into min/max), H22 spring secondary motion baked to layers and weight-animated, second clip on one Scene Animate node blended in Motion Mixer. Q&A covers the APEX-script MCP server ("vibe-rigging", token-light).
- **File:** tutorials/h22---kinefx-rigging-and-animation-max-rose-houdini-22-hive.md


### H22 - Baking with Copernicus | Alex Hamer | Houdini 22 HIVE
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=orN8H41hNDE
- **Author:** Houdini
- **Houdini Version:** Houdini 22
- **Tags:** cop, rendering, procedural, uv, modelling, intermediate, houdini-22
- **Summary:** HIVE talk (Copernicus team): H22's new Bake Pre-Process node (SOP+COP) makes cage-mesh authoring visible and interactive — orange cage in a viewport state, High Res Intersections highlighting (raise offset until no red), cage softening split at UV seams/faces/edge groups to stop skewed bakes, attribute-scaled offsets, inward ray-end mesh to exclude stray geometry — feeding Bake Geometry Textures (surface-normal / cage / single-mesh tracing, Match Pieces by Name for per-part bakes). Demo: fan asset via bake-setup recipe, live multi-UDIM preview material, COP materials with curvature/occlusion-driven scratches, exported to Unreal.
- **File:** tutorials/h22---baking-with-copernicus-alex-hamer-houdini-22-hive.md


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
