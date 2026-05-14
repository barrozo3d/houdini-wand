# Render Pipeline — Karma, Mantra, Redshift, MaterialX

Houdini rendering: engines, Solaris/LOPs, MaterialX shaders, and output.

---

## Render Engines Overview

| Engine | Type | Best for | Context |
|--------|------|----------|---------|
| **Karma CPU** | Path tracer | Production quality, accurate GI | Solaris/LOPs |
| **Karma XPU** | Hybrid CPU+GPU | Fast iteration + quality | Solaris/LOPs |
| **Mantra** | Path tracer | Legacy VEX shaders, volume rendering | ROP network |
| **Redshift** (3rd party) | GPU biased | Fast, industry-standard | OBJ or Solaris |

---

## Solaris / LOPs (Recommended Modern Pipeline)

Solaris is Houdini's USD-based scene assembly and rendering context. Use for all new Karma renders.

### Basic LOP Setup
```
/stage network:

[SOP Import] → imports SOP geometry as USD primitive
  ↓
[Material Library] → define MaterialX shaders
  ↓  
[Assign Material] → assign to USD prims by path or collection
  ↓
[Light] (Dome, Rect, Sphere, Distant, Cylinder)
  ↓
[Camera] → set resolution, focal length
  ↓
[Karma] render node → kick off render
```

### SOP Import to Solaris
```
LOP: SOP Import
  SOP Path: /obj/geo1
  Import Path Prefix: /World/geo
  Primitives: Meshes (or All)
```

### USD Scene Graph Concepts
```
Primitive path   /World/geo/myobject
Xform            transforms (translate, rotate, scale)
Mesh             geometry
Material         shader assignment
Look             collection of material assignments
Layer            USD layer for non-destructive overrides
```

---

## MaterialX Shaders (Karma)

MaterialX is the shader language for Karma (and USD-based pipelines).

### Standard Surface (PBR)
The main shader for realistic materials:
```
LOP: Material Library node
  Inside: MatX Standard Surface

Key inputs:
  Base Color        — albedo (texture or constant)
  Metalness         — 0 = dielectric, 1 = metal
  Roughness         — 0 = mirror, 1 = diffuse
  Specular          — dielectric reflectivity
  Transmission      — 0-1 for glass/water
  IOR               — index of refraction (glass: 1.5, water: 1.33)
  Subsurface        — skin/wax SSS amount
  Emission Color    — emissive surface
  Normal            — bump/normal map input
  Displacement      — for true displacement rendering
```

### Connecting Textures
```
MatX Image node → connect to Standard Surface inputs
  File: $HIP/../tex/mymap.exr
  colorspace: srgb_texture (for color maps)
              raw (for roughness, normal, metalness)
```

---

## Karma Settings

```
Karma ROP / karmarendersettings LOP:

Resolution          — output image size
Camera              — which camera to render from
Frame Range         — start/end/step

Sampling:
  Max Samples       — higher = less noise (128-2048 typical)
  Min Samples       — early termination threshold
  Noise Threshold   — stops sampling when noise below this

Lighting:
  Enable Sky        — use dome light environment
  Indirect Bounces  — GI depth (default 8)

Motion Blur:
  Enable            — toggle
  Shutter           — 0-1 (0.5 = half frame = cinematic)

Volumes:
  Volume Step Rate  — quality vs speed for volumes

Output:
  Image Path        — $HIP/../render/$OS.$F4.exr
  Image Format      — EXR (multi-layer for AOVs)
```

### Render AOVs (Multi-layer EXR)
```
Add Karma ROP → Products tab → Add Product
  Type: LPE (Light Path Expression) or Named (beauty, diffuse, specular, etc.)
  Output goes into multi-layer EXR for compositing
```

---

## Mantra (Legacy)

Still useful for VEX-shader-based workflows and volume rendering.

```
Render → Create Render Node → Mantra (ifd)

Key settings:
  Rendering: Physically Based Rendering (PBR) mode
  Sampling: Pixel Samples (default 3x3), Ray Samples (secondary)
  Limits: Diffuse/Reflect/Refract/Volume reflect limits
  
Materials: VEX/SHOP networks
  principledshader.vfl — equivalent to Standard Surface
  
Output: Mantra ROP → Output picture: $HIP/../render/$OS.$F4.exr
```

---

## Lighting in Solaris

### Light Types (LOP)
```
Dome Light    — HDRI environment, wraps whole scene
Rect Light    — area light (rectangle)
Sphere Light  — area light (sphere / soft)
Disk Light    — area light (disk)
Cylinder Light— area light (tube/strip)
Distant Light — directional sun (infinite)
Point Light   — legacy point light (avoid in Karma)
```

### HDRI Environment
```
LOP: Dome Light
  Texture File: path/to/env.hdr or .exr
  Intensity: 1.0
  Exposure: 0.0 (adjust instead of intensity for stop-based control)
  Enable Color Temperature: for warm/cool shift
```

### Three-Point Lighting in Solaris
```
Key Light    — Rect, high intensity, offset 30-45° from camera
Fill Light   — Rect or Dome (low), opposite side, 1/3 key intensity
Rim/Back     — Rect behind subject, highlights silhouette
```

---

## Output & Compositing

```
EXR workflow:
  Render to multi-layer .exr (beauty + AOVs)
  Import into Nuke, Fusion, After Effects (via ProEXR), or Blender Compositor
  
AOV passes (common):
  beauty / rgb         — final composite
  diffuse_direct       — direct diffuse lighting
  diffuse_indirect     — GI / bounced light
  specular_direct      — direct highlights
  specular_indirect    — indirect reflections
  emission             — emissive objects
  cryptomatte          — object/material ID masks
  depth (Z)            — depth of field / fog in comp
  normal               — relighting / denoising
```

### Houdini Compositor (COP2 / TOPs)
```
/img network:
  Render node pulls render output
  Color correction, glow, DOF, chromatic aberration
  Output: Write node to disk
  
Note: Full compositing is usually done outside Houdini (Nuke, Fusion)
Houdini comp is best for quick lookdev iteration
```
