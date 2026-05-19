# Houdini 21.0 — Release Notes Reference

**Source:** https://www.sidefx.com/docs/houdini/news/21/  
**Ingested:** 2026-05-19  
**Status:** Current version as of May 2026

---

## KineFX, APEX, and Animation

### Animation System
- **Animation Catalog** — save, manage, and reuse animations and single-frame poses across projects
- **Motion Mixer** — combine and edit animation clips of multiple characters in a timeline view
- **Animation Layer Inheritance** — upstream layers can be inherited through `APEX Scene Animate SOP` via "Inherit Animation Layers from Input"
- **Animation Retargeting** — use `APEX Animation from Skeleton SOP` to retarget animations onto characters
- **Full Body IK Tool** — applies full body IK letting you pose by adjusting high-level targets
- **Ragdoll Tethers** — attach ragdoll objects to each other; `APEX Configure Ragdoll` recipe streamlines setup

### APEX Rigging
- **Autorig Builder** — interactively apply pre-built and custom rig components via viewport; maintains procedural flexibility
- **APEX Graph SOP** (renamed from APEX Edit Graph SOP) — enter animate state with visual graph representation; input character folder structures auto-display rig; **Subgraphs** section for subnets
- **Fuse graph operation** — merge rig functionality from one graph into an existing rig
- **APEX Pack Character SOP** — converts KineFX characters to character folder structure
- **APEX Unpack Character SOP** — outputs skin, capture pose, animated pose
- **APEX Configure Graph SOP** (new) — configure constraint and component parameters
- **Packed Folder Copy SOP** (new) — copy, rename, and move character folder data

### New APEX Autorig Components
limb, hand, foot, neck, scapula, ulna, root, twist joints, joint rotate corrective, clean, rename

### APEX Script Enhancements
- Create interfaces for graph inputs
- Access/set vector and matrix components
- `#<tag_name>` alternative path pattern syntax for filtering tags
- `+` operator extends arrays
- Keyword arguments in `@subgraph` decorator

### Deprecations (Animation)
- `APEX Rigscript Component SOP` deprecated → use `APEX Autorig Component SOP` with "Build Rigscript" parameter
- APEX Autorig Component v1.0 SOP no longer supported

### Test Characters
- **Otto** — realistic male character with biped rig and muscle/skeletal bone geometry
- **Electra v2.0** — updated skeleton, industry-standard setups, twist joints, IK/FK fingers, reverse foot, auto clavicle

### glTF / FBX Changes
- New SOPs: `GLTF Animation Import`, `GLTF Character Import`, `GLTF Skin Import`
- FBX: `fbx_node_type` attribute specifies FBX scene element type
- FBX: **Normalize Joint Scales** and **Remove Namespaces from Joint Names** parameters
- **Joint Display Scale** parameter on all FBX import/export SOPs

### Audio Subsystem Rewrite
- Completely rewritten on top of FFmpeg; resolves long-standing issues
- Read: `.aac`, `.aiff`, `.flac`, `.m4a`, `.mp3`, `.ogg`, `.wav`
- Write: `.aiff`, `.flac`, `.mp3`, `.ogg`, `.wav`
- Removed: `.au`, `.it`, `.mod`, `.mp2`, `.s3m`, `.sf`, `.snd`, `.spx`, `.xm`
- Max sample rate increased to 48 KHz

---

## Modeling, Geometry, and Terrains

### New SOPs
| SOP | Purpose |
|-----|---------|
| `Attribute Sort SOP` | Sort attributes ascending/descending |
| `UV Flatten from Points SOP` | UV maps measuring distance/direction along surfaces |
| `Edge Relax SOP` | Move points so edge lengths match a reference |
| `Separate Pieces SOP` | Separate overlapping geometry pieces by string/int attribute |
| `Split by Point Attribute SOP` | Insert new points where attributes change across edges |
| `Topo Slide by Curve References SOP` | Slide geometry across surface using reference curve pairs |
| `Unsubdivide SOP` | Construct polygon mesh approximating Catmull-Clark subdivision |
| `Shot Sculpt SOP` | Interactive tool for time-based deformations |
| `Extract Contours SOP` | Extract contour edges as viewed from a camera |

### Enhanced SOPs
- **Poly Bridge + Poly Extrude** — can generate UVs on sides
- **Poly Extrude** — UI enhancements, better edge group handling, Polygon Soup support
- **Ray SOP** — bidirectional option with closest/farthest hit selection
- **Peak, Soft Peak, Inflate, Flatten, Point Jitter** — mask parameters added
- **UV Layout SOP** — automatically packs islands into contiguous UDIM tile ranges
- **Polyreduce SOP** — "Limit Using Normal Deviation" parameter
- **HeightField Erosion SOP** — completely redesigned; simulates hydraulic and thermal erosion at scale
- **Quad Remesh SOP** — localized adaptivity via procedural or interactive methods
- **Sculpt SOP** — surface distance sculpting, enhanced mask interface, 6 new brushes (Plow, Planar, Elastic Grab, Elastic Scale, Elastic Pinch, Elastic Twist)
- **Curve SOP** — branched curve support; creation, fusion, splitting in draw mode

### Viewport
- New **Hide Other Objects (World)** mode (previous mode renamed to Local)
- `volvis` dictionary attribute replaces cloud format for Volume Visualization SOP

---

## Solaris (USD/LOPs)

### Workflow
- **Adobe USD File Format Integration** — directly open FBX, glTF, SBSAR via sublayer/reference nodes; export via USD ROP
- **USD Path Expressions for Collections** — `%pathexpr` auto-collection in Collection LOP, Assign Material LOP, Light Linker LOP, Material Linker
- **Asset Catalog** (renamed from "Asset Gallery") — existing references auto-redirected
- **Non-Root Default Prims** — LOP nodes can author non-root primitives as default layer primitives
- **Color Management Configuration** — author `colorManagementSystem` and `colorConfiguration` metadata directly

### New LOPs
- **Live Render LOP** — live connection to Render Gallery, responds to upstream LOP changes in real time
- **Geometry Light LOP** — applies UsdLux ApiSchemas to convert meshes/points/curves/volumes into lights
- **Shot Split and Shot Switch (Beta)** — multi-shot workflow nodes
- **Render Pass LOP** — creates/edits `UsdRenderPass` primitives
- **Background Plate LOP** — COPs sample compositing setup

### USD SOP Tools
- **USD Configure Prims from Points SOP** — author special SOP attributes for USD primitives
- **USD Configure Import SOP** — set detail attributes affecting how LOPs import geometry

### Multiple Active Render Delegates
- LOP Scene Viewer can maintain multiple non-HoudiniGL render delegates simultaneously
- Switch between renderers without restarting
- Controlled via `HOUDINI_ACTIVE_RENDER_DELEGATE_COUNT`

### New Environment Variables
- `HOUDINI_ACTIVE_RENDER_DELEGATE_COUNT` — controls simultaneous render delegate count
- `HOUDINI_DEFAULT_ROP_RENDER_DELEGATE` / `_CLONE_RENDER_DELEGATE` / `_SCENEVIEWER_RENDER_DELEGATE` / `_FORCE_SCENEVIEWER_RENDER_DELEGATE` — replace `HOUDINI_DEFAULT_RENDER_DELEGATE`

---

## Karma Renderer

### Karma XPU Enhancements
- **Pre-compilation** — reduces time to first pixel
- **Volumetric Lights** — via Geometry Light LOP
- **String Primvar Support** — texture path primvars connected to MtlX Image VOP file inputs
- **Shader Blending** — blend up to 16 MtlX Standard Surface or MtlX OpenPBR VOPs (was 2)
- **MIS Compensation** — for IBL/dome and Physical Sky lights
- **Shadow Linking** — up to 4 geometry subsets per scene
- **SSS Tracesets** — light paths across meshes sharing common tracesets (4 traceset limit in XPU)

### New Karma Nodes
| Node | Purpose |
|------|---------|
| `Karma Texture Baker LOP` | Create texture maps defining shading states |
| `Portal Light LOP` | Rectangular portal light for Dome Light LOP |
| `Karma Shadow Catcher LOP` | Configure holdout and matte objects |
| `Bake GSplat SOP` | Gaussian Splatting for fast XPU rendering (tech preview) |
| `Karma Whitewater VOP` | Specular component for volumes |
| `Karma Fur 2.0 VOP` | GGX wetness parameters + animal fur presets |
| `Karma Melanin VOP` | Simulate melanin/pheomelanin pigment for hair/fur/feathers |
| `Karma Ray Switch VOP` | Evaluate color based on ray type (diffuse/glossy/SSS) |
| `Husk Image Metadata LOP` | Add custom metadata to render products |

### Shading
- **MatX OpenPBR Surface VOP** (new) — physically-based shader for Karma CPU and XPU
- **MtlX Normalmap Recipe** — MikkT normal map support
- **Toon Outlines** — Karma CPU rendering on Render Settings LOP
- **LPE Negation** — `!CB` syntax for negating Light Path Expressions

### Hydra 2 Support
- Houdini now supports Hydra 2 as new standard interface for render delegates
- Backward compatible; disable via `USDIMAGINGGL_ENGINE_ENABLE_SCENE_INDEX=0`

### Husk Command-Line
- `SIGTERM` handling — writes checkpoint and snapshot instead of full cancellation
- `--extra-metadata` flag for custom image metadata
- Deep image auto-tiling improvements, `--autotile-res`, `--tile-count`

---

## Copernicus (COP2) — GPU Image Processing

### Production Ready in H21
- Slap comp support in Render Gallery and LOP Vulkan Viewport
- Full texturing and slap comp workflow declared production-ready

### Cables System (new in H21)
- Combine multiple layer wires into single inputs while maintaining separate sources
- 8 new cable nodes: `Cable Filter`, `Merge`, `Pack`, `Rename`, `Sort`, `Split`, `Switch`, `Unpack`

### Baking
- **Bake Geometry Textures COP** — transfer geometry data between meshes
- **Ray Trace COP** — intersect rays against geometry
- Global UDIM parameter support

### 70+ New COP Nodes
**Simulation/Effects:** Pyro COPs (smoke/fire), Reaction-Diffusion Solver, Flow Block COPs (2D fluid), Chladni Cymatic Patterns, Phasor Noise, Bubble Noise, Cloud Noise 3D  
**Image Processing:** Lens Distort, Corner Pin, Scatter on Curves, Swirl, Bend, Pixelate, Sharpen, Vignette, Wipe, Heat Distort, Defocus, Tone Map, Color Correct, Convert Depth, Convolve 3×3  
**Advanced:** VDB integration (Layer/VDB conversion), Triplanar projection, Curve 3D, Layer from Curves, Mask from Curves, Python Snippet COP

### New Expression Functions
`copinputcablesize`, `copoutputcablesize`, `copinputtype`, `copoutputtype`, `copinputisnull`, `copoutputisnull`

### New Python Classes
`hou.CopCableStructure`, `hou.CopNode`, `hou.CopVerb`, `hou.ImageLayer`, `hou.NanoVDB`, `hou.copNodeTypeCategory`

---

## Pyro, FLIP, and Fluids

### New SOP Pyro Shelf Tools (H21)
Bullet Hits, Candle Flame, Dry Ice, Debris Dust, Dust Fireball, Wispy Smoke A/B, Aerial Barrage, Ground Barrage, Ground Shockwave variants, Ground Explosion A/B, Smokeless Flames, Thruster Exhaust, Fire Portal, Fireball with Trails, Stylized Fire

### COP Pyro
- 2D GPU solver for fire/smoke with infinite timeline
- Available in FX, Apprentice, Indie, Education (not Core)

### FLIP
- **Neural Point Surface SOP** — turns point cloud into VDB surface using pretrained CNN
- Particle Fluid Surface SOP: Neural Model options, point cloud partitioning for OpenCL memory limits
- **Gas Wind DOP** — Wind Direction, Visualization, Bindings, and OpenCL controls

### New DOPs
- **Gas Remap DOP** — fits scalar volume field to new range with ramp mapping
- **Gas Dissipate 2.0 DOP** — drives field values toward goal
- **Gas Burn DOP** — controls flame dissipation, smoke/temperature emission, divergence

### ML Volume Upres
- Sparse Billowy Smoke updated to support ML Volume Upres (ONNX model)

---

## Rigid Body Dynamics

### New SOPs
- **RBD Car Fracture SOP** — fracture car rig with automatic constraints for sheet metal, glass, wood
- **RBD Car Transform SOP** — transform fractured car using unfractured rig or simulation points

### Bullet Solver
- 20–30% reduced memory usage for overlap-related data
- ~20% faster initial frame computation for overlapping objects
- Updating separated pairs at end of timestep is ~3.5× faster
- New **Initial Overlap Relationship** DOP type

---

## VEX and OpenCL

### New VEX Functions (H21)
| Function | Purpose |
|----------|---------|
| `osd_limit` | Evaluate point attributes as subdivision surfaces |
| `pointprimuv` | Returns intrinsic UV location of a point in its primitive |
| `medulla_diffuse` | Diffuse BSDF for hair medulla |
| `medulla_henyeygreenstein` | Anisotropic volumetric BSDF |
| `sheen` | Zeltner Sheen BSDF |
| `ocio_transformviewreverse` | Transform colors using OCIO (reverse) |
| `agentcliplayersamplelocal` | Evaluate layered animation clips — local transforms |
| `agentcliplayersampleworld` | Evaluate layered animation clips — world transforms |
| `py_dumps` | Convert VEX dictionaries to Python-style strings |
| `py_loads` | Convert Python dictionary strings to VEX format |

### OpenCL
- Driver version string now included in hash key for cached binaries (driver updates force recompile)
- New topology bindings prefixed with `topo:` (half-edge attributes, tetrahedral adjacency)

---

## Houdini Engine and APIs

- Performance optimizations for shared memory side channel
- Copernicus integration — COPs can be fetched/sent from Unreal
- Nanobind Python bindings
- **Unreal Plugin** — PCG Graph integration, Houdini Asset Editor, Unreal 5.5 + 5.6 support
- **Unity Plugin** — Unity 6.0/6.1 support, Copernicus integration
- **Maya Plugin** — Maya 2026 support
- **3DS Max Plugin** — 3DS Max 2026 support, Output Log panel, new HDA panel

---

## Viewport, UI, and Scripting

### Viewport
- **Vulkan is now default** — production ready, enabled by default on macOS
- Threading for geometry updates on by default (Linux + Windows)
- New lighting work modes: Dome Light, Physical Sky, Three Point
- Ray tracing parameters: "Use Ray Tracing", "Denoise if Needed" for AO
- New **Maximum Near Clip** parameter; free cameras no longer have far clip planes
- Tear off viewport copy for floating windows
- OpenPBR shader support
- Automatic texture cache resizing
- Enhanced snapping with consolidated menus

### UI
- **Live Simulation button** — runs independently of playbar
- **Forever mode** — plays indefinitely without stopping at frame end
- Multiparms support drag reordering and **Multiparm Label Reference** dynamic labeling
- Hotkey framework expanded to support key sequences and volatile symbols

### Python/HOM (H21)
- `hou.Drawable2D` — 2D shape drawing
- `hou.Viewport2D` — COP image viewing
- Agent/APEX: methods for local transform values, node tag management, port renaming
- `packToFolder` gains visibility and pack parameters
- `removeFromFolder` removes paths

---

## MPM (Material Point Method)

Available in sub-pages but significant DOP solver for snow, sand, mud, and hybrid material behavior. Check `https://www.sidefx.com/docs/houdini/news/21/mpm.html` for specifics.

---

## Machine Learning

ONNX inference integration throughout: ML Volume Upres for Pyro, Neural Point Surface for FLIP, Copernicus ONNX COP. Check `https://www.sidefx.com/docs/houdini/news/21/ml.html` for full details.

---

## Version Awareness Notes

- **H21 is the current major version** (May 2026: latest build ~21.0.720)
- Copernicus COP system: **introduced in H20.5**, matured in H21
- APEX rigging: **introduced in H20**, major expansion in H20.5, production-ready in H21
- KineFX: foundational system since H18, complete character pipeline by H21
- Vulkan renderer in viewport: H20.5 (beta) → H21 (production default)
- Old COP Network (compositing) is deprecated — Copernicus is its replacement
