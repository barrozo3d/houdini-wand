# Houdini 22 Release Notes — Condensed Reference

**Source:** https://www.sidefx.com/docs/houdini/news/22/index.html (fetched 2026-07-18)
**Status:** Current release. Sub-pages: kinefx, muscles, feathers, crowds, solaris, karma, pdg, ml, engine, copernicus, model, viewport, mpm, pyro, rbd, vellum, vex, hqueue, licensing, platforms.

---

## Headline Themes
1. **COPs everywhere** — Pyro simulation in Copernicus, HeightField terrain tools in COPs, 70+ new COP nodes, adjacency system for seamless cross-UV-island processing.
2. **Machine Learning** — native Gaussian-splat training, Neural Cellular Automata, SAM2 masking, MoGe-2 depth estimation, computer-vision training, neural terrain erosion.
3. **Implicit surfaces** — new geometry primitive type ("shapes defined by math"): infinite resolution, exact collision, boolean ops; used by COP Pyro sources/collisions and VEX.
4. **Animation UX** — Animate desktop, Character Picker, Secondary Motion tool, Motion Mixer redesign, parallel rig evaluation (20 rigs realtime).
5. **Metal destruction** — RBD Material Fracture 2.0 bends and tears metal.
6. **Viewport** — OpenGL removed, Vulkan primary; GPU subdivision; volumetric fog; GSplat shadows.

---

## Copernicus (COPs)
- **HeightField terrain in COPs**: HeightField COP Network, Layer, Noise, Blur, Strata, Terrace, Mask by Feature, Erode, Slump, Transform 2D/3D, Project, Clip, Visualize. 3D Output flag distinguishes 3D-viewer display; terrain color-ramp preset gallery.
- **13 grunge map nodes**: Aurora, Bark Strips, Birch Bark, Drips, Galvanized Steel, Layered Noise, Leaking Streaks, Moisture, Mold Spots, Pine Bark, Rust, Rusty Surface, Sheets, Wipe Trails.
- **Adjacency system** (seamless across UV seams): `Attribute Sample with Adjacency`, `Distort with Adjacency`, `Extrapolate with Adjacency`, `Geometry to Adjacency`, `Space Transform with Adjacency`.
- **Temporal COPs**: Time Blend, Time Loop, Time Pack, Time Shift.
- Notable new COPs (70+ total): Paint 3D, Camera / Camera Blend, Convolve Filter, Corner Detect, Despill, Drop Shadow, FFT, Height to Caustics, Knit, Weave, Normal to Height, Ocean Spectrum/Evaluate, Poisson Solver, **Rasterize GSplats**, Rasterize Implicit Surface, Ripple solver, Star Glow, Turing Patterns, UDIM Pack, USD Material, UV Inverse/Shape, Visualize Velocity.
- Workflow: drag COPs into Scene Viewer (camera ops); UDIM via `op:` syntax; Texture Material Library LOP for COP-powered shading; UE supports Copernicus HDAs.

## COP Pyro (new workflow — FX editions only)
- Minimal-node pyro around **Pyro Block Begin/End** (Block 2.0 — all solver controls on Block End, no solvers inside the loop).
- Recipes: Fire, Fireball, Candle Flame, Billowy Smoke, Cigarette Smoke, Large Smoke Plume, Dry Ice.
- 16 nodes incl. `Pyro Configure`, `Pyro Activate`, `Pyro Advect`, `Pyro Build Advection Map`, `Pyro Buoyancy`, `Pyro Velocity Scale Force`, `Pyro Vortex Confinement Force`, `Pyro Source from Layer/Shape/Volume`, `Pyro Emit From Flame`, `Pyro Collision Shape`, `Pyro Collision from Shape`, `Pyro Source Shape`.
- **Deprecated**: Pyro Solver DOP, Smoke Solver DOP, Smoke Object DOP, Smoke Configure Object DOP, legacy Pyro shelf → migrate to Sparse variants or SOP/DOP Pyro FX shelves.
- Implicit surfaces as lightweight sim domains/collision (exact detection, boolean-able).
- See library tutorial: houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes.md

## Machine Learning
- **Gaussian splats**: `ML Preprocess GSplats` + `ML Train GSplats` TOPs (Karma EXRs or SFM/COLMAP datasets; extra-AOV training e.g. normal/albedo); `Rasterize GSplats` COP; Karma noise-free GSplat rendering; USD `ParticleField3DGaussianSplat` translation; viewport GSplat shadows.
- **NCA**: `Neural Cellular Automata Core/Decode` COPs; `ML Train Neural Cellular Automata` TOP; NCA Block recipe (temporal).
- **Neural COPs**: `Neural Layer to Depth` (MoGe-2 — depth/normal/position + camera from one image), `Neural Layer to Mask` (SAM2 — click/bbox prompts).
- **Computer vision**: `ML Preprocess/Train Computer Vision` TOPs, `ML Computer Vision Inference` COP.
- `Neural Terrain Generate` SOP (custom ONNX erosion on heightfields); `Agent Add ML Deformer` (crowd skin quality).
- Infra: ML Train Regression >2GB models; ONNX inference — larger models, more dtypes, device selection, ONNX Cache.
- See library tutorial: h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive.md

## RBD / Destruction
- **RBD Material Fracture 2.0**: metal bending + tearing (parity with RBD Car Fracture); constraint tracking independent across recursion levels (no fracture-ID overlap).
- `Voronoi Split 2.0` (much faster clipping) + `Voronoi Fracture 2.0`; `RBD Replicator` DOP (replicate piece clusters + constraints to point clouds); RBD Unpack per-instance naming for USD.
- RBD Constraint Properties: paint constraint behavior directly on source geometry. Bullet soft constraints: default stiffness 1.0 when plasticity enabled (fixes inactive constraints).
- Houdini Procedural: RBD LOP gains multi-segment deformation + acceleration blur.
- See library tutorials: houdini-22-how-to-destroy-metal-1-tearing.md / -2-denting.md

## Modeling / Geometry / Terrain
- New SOPs: `Walk on Surface`, `Curve Animate` (interactive Bézier/NURBS), `UV Relax`, `Neural Terrain Generate`.
- Enhanced: Quad Remesh (rectangular mode, frame-field smoothing), Remesh (Boundary Deviation), Scatter (density texture masking), Shot Sculpt (groom guide deformation), Find Shortest Path verbified, Extrude Volume compilable.
- Interactive viewport subdivision editing; implicit surfaces as geometry primitives; `@ptnum/@primnum/@elemnum` adhoc syntax.

## Karma
- XPU: subdivided-mesh memory −50%; Texture Width <1 sharpening / 0 disables mipmapping; Bump Shadow Terminator; direct iso-surface VDB rendering; displayOpacity/Af AOVs.
- New LOPs: `Texture Material Library`, `Image Filter`, `Karma Blocker Light Filter`. New Karma VOPs: Ambient Occlusion, Distance, Curvature, Light Filter Attenuation. MtlX 1.39.5 VOPs: Flake2D/3D, Fractal2D, glTF Anisotropy, Hex Tiled Image/Normal, Lat Long Image.
- Volume sampling: Equiangular MIS option; geometry lights instancing + filters + light tree; Split Render Products by Render Var; separate denoised AOVs; stencil UDIMs; Pixel Filter Scale replaces Size.

## Solaris / USD
- New LOPs: `Relocate` (tombstone arcs), `Plane`, `Configure Guide Deform`, `Scatter Instances` (render-time Hydra procedural), `PointInstancer`; renames: Layout→`Paint Instances`, Instancer→`Copy to Points`.
- **APEX-in-LOPs (beta)**: APEX Animate, APEX SOP Rig Builder, Bake APEX Scene, Configure APEX Rig, SOP Import APEX Scene + Hydra scene-index plugin.
- RenderSettings + RenderPass prims for multi-layer one-shot rendering; `XformCommonAPI` now default transform storage; USD ROP sidecar geometry files; redesigned Context Options Editor; `%timevarying` auto-collection.
- SOP-side: `USD Create Component`, `USD Create Proxy Geometry`, `USD Parent Geometry`.

## KineFX / APEX / Animation
- **Animate desktop**; Character Picker (2D control layouts); Secondary Motion tool (lag/overshoot/jiggle/spring on existing anim); ragdoll forces (wind, air resistance, magnet, turbulence); full-body-IK posing during animation; Motion Mixer redesign (nested clips, override layers); animation caching; retime tool in graph view.
- New SOPs: `APEX Scene Import Animation`, `APEX Scene Merge`, `APEX Scene Add Camera`, `Biped Setup`/`Biped Retarget` (FBIK skeleton transfer), `APEX Rig Pose`, `Orient Joints 2.0`.
- Autorig Builder redesign (visual feedback, templates, auto joint orientation); rig components: Eye, Surface Deform, Set Driven Keys, Blend Shape 3.0 (screen-space + patch sliders).
- Renames: USD Animation/Character/Skin Import → **UsdSkel** Animation/Character/Skin Import SOPs. FBX/GLTF: axis conversion, UE centimeter/LUF presets.
- **Evaluate Rigs in Parallel** — ~20 full rigs in realtime playback.

## Character adjacent
- **Muscles (Otis)**: sliding constraints (Separated Shell and Core), Shell-to-Core tab, velocity blending (no lag on fast bones), Constraints-Only damping, DOP dive target for custom forces/VEX/OpenCL, Otto V2 test geo, "Tissue Shell" rename.
- **Hair/Fur/Feathers**: `Guide Deform` SOP + `Configure Guide Deform` LOP (render-time Hydra deformation), `Guide Reduce` (spatial representative guides), `Guide Utility`, Shot Sculpt overhaul; Hairgen "Blend in Skin Space" (no bald spots on short fur); Capybara test geo fur + recipe.
- **Crowds**: `Agent Add ML Deformer`, Agent Configure Joints 2.0, Agent Collision Layer 2.0 (auto collision shapes), MotionPath Edit transform handle, terrain adaptation multi-leg improvements.
- **Vellum**: quasistatic solve for hair Bend/Twist (higher stiffness); Angular Damping parameter.
- **MPM/Particles**: MPM HeightField collisions; 64-bit positions for stiff-material stability; Particle FX shelf (fireworks: Brocade/Peony/Chrysanthemum; Magic Trails A/B/C).

## VEX / OpenCL / Python
- New VEX: `implicitsurface()`, `implicitsurfacebounds()`, `implicitsurfacevel()`; `osd_limitcurvature/normal/vertex/gradient()`; `vertexprimuv()`, `volumetransform()`, `minjerk()`, `random_shash()`, `qexp()/qlog()/qpow()`, `usd_bindmaterial()`, OCIO helpers (`ocio_aliases/fullname/nanocolorname`).
- OpenCL: OSD query methods (`osd_facecount`, `osd_patchcount`, `osd_lookuppatch`, `osd_limitsurface`, `osd_limit`, `osd_limitnormal`).
- HOM: `hou.ApexUniGraphDebugger`, `hou.Camera/CameraPrim`, `hou.CopCable`, `hou.NanoVDB`, `hou.UniNode*`, `hou.OpenCLDevice`; per-viewport visibility; channel muting; retime markers.

## Viewport / UI
- **OpenGL removed — Vulkan primary**; GPU subdivision; volumetric fog; GSplat shadow cast/receive; interactive XYZ gnomon view jumping.
- Cameras: lock/edit SOP+COP cameras, drag into Scene Viewer; `Camera`, `Camera from Points`, `Camera To Points` SOPs.
- UI: Theme Editor skins, OKHSL color editor, redesigned Preferences, ramp preset gallery + generator, number rolling, F11 fullscreen, cross-platform screen color picker.

## PDG / TOPs
- New: ML CV/GSplat TOPs (above), `Make Textures` (batch to .tx), `USD Zip` (.usdz).
- Python Script TOP background tasks; Virtual Environment TOP pip config; Local Scheduler PDG services; `pdg.curPlatform()`.

---

## Migration Gotchas (H21 → H22)
- Legacy (non-sparse) Pyro/Smoke DOPs deprecated — use Sparse or COP Pyro.
- OpenGL viewport gone — Vulkan required.
- USD transform authoring defaults to XformCommonAPI (pivot-exploded, not 4×4).
- Pixel Filter Size removed in Karma → Pixel Filter Scale.
- USD character import SOPs renamed to UsdSkel*.
