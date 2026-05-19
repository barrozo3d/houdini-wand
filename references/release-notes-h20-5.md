# Houdini 20.5 — Release Notes Reference

**Source:** https://www.sidefx.com/docs/houdini/news/20_5/  
**Ingested:** 2026-05-19  
**Status:** Previous major release (H21 is current)

---

## Key Theme: APEX + Copernicus Introduction

H20.5 introduced two major systems that H21 then matured:
1. **Copernicus** — brand new GPU-based COP image processing framework
2. **APEX** rigging system expansion — APEX Script, full rig component library

---

## Copernicus (Introduced in H20.5)

> "COP is a 2D and 3D GPU image processing framework" for real-time image manipulation within 3D space.

- Replaces the deprecated old Compositing network ("COP Network - Old")
- Processes single images (layers) or Houdini geometry through interconnected nodes
- Output: images or volumes
- **Vulkan-based geometry rasterizer** for fast processing
- **ONNX inference engine** for machine learning applications
- Point stamping functionality
- Real-time viewport visualization across 2D, 3D, and Karma renderers
- Full interoperability with SOPs
- Slap composite support (interactive and offline)
- Supports OpenCL nodes, OpenFX plug-ins, VEX, video input
- Direct access to SOP, DOP, LOP, and OP data
- Procedural texture/pattern generation (2D/3D noise, terrain)
- Edge detection and hatching algorithms
- Interactive Texture Mask Paint
- SDF-based shape generators and tileable patterns

---

## KineFX and APEX (H20.5)

### Animation
- **Layered Animation System** — non-destructive layered animation curves
- **Motion Visualization** — motion paths as editable 3D curves in viewport
- **Dynamic Parenting** — transient constraints shift control hierarchies during animation
- **Ragdoll Pose Mode** — real-time physics for character positioning
- **UI Refinements** — lockable HUD panels, expanded right-click menus, new hotkeys

### Procedural Rigging
- **Attribute Adjust Array SOP** — procedural skeleton tagging for automated rig prep
- **Pre-Built Components** — full-body IK, spline deformers, constraint systems
- **APEX Script Interface** — Python-like syntax for APEX graph construction without manual node placement

---

## VEX and OpenCL (H20.5)

### New VEX Functions
| Function | Purpose |
|----------|---------|
| `cospi`, `sinpi`, `tanpi` | Cosine/sine/tangent of value × π |
| `findlowerbound` | Largest item in array smaller than target |
| `findlowerboundsorted` | Optimized variant for pre-sorted arrays |
| `findsorted` | Locate items in sorted arrays |

### OpenCL
- OpenCL kernel compiling can be interrupted
- GPU-accelerated image processing in COP (Copernicus uses OpenCL)
- OpenCL-based SOP for realtime quasi-static wrinkles
- GPU acceleration for Volume Blur SOP via OpenCL option

---

## Other H20.5 Areas

Full sub-pages available at `https://www.sidefx.com/docs/houdini/news/20_5/[section].html`:
- `kinefx.html` — APEX and animation details
- `muscles.html` — Muscles and tissue
- `feathers.html` — Hair, fur, feathers
- `crowds.html` — Crowds
- `solaris.html` — Solaris/USD
- `karma.html` — Karma renderer
- `pdg.html` — PDG/TOPs
- `mpm.html` — MPM solver
- `rbd.html` — Rigid body dynamics
- `vellum.html` — Vellum cloth/grains
- `ml.html` — Machine learning
- `model.html` — Modeling and geometry
- `viewport.html` — Viewport and UI

---

## H20.5 → H21 Progression

| Feature | H20.5 | H21 |
|---------|--------|-----|
| Copernicus | Introduced, beta | Production ready, 70+ new nodes, Cables |
| APEX Rigging | APEX Script introduced | Autorig Builder, full component library |
| Vulkan Viewport | Available | Default on macOS |
| Karma XPU | Core features | +16-shader blending, shadow linking, SSS tracesets |
| glTF Support | Basic import | KineFX animation/skinning import SOPs |
