# Recipe: FLIP Fluid + Karma Render Pipeline

A hero liquid shot from FLIP simulation through whitewater to Karma XPU render. Assumes H20+.

---

## Stage 1 — Container & Source Setup

```
SOP level (Geometry object):

Box SOP
  → Scale: 4 × 3 × 4  (your simulation domain)
  → This becomes the FLIP container

FLIP Tank SOP  (alternative to manual Box — pre-builds everything)
  → Particle Separation: 0.05 (hero) / 0.1 (preview)
  → automatically creates container + initial particles

Custom fluid source (splash/pour):
  Sphere/Curve SOP
    → FLIP Source SOP
      → Mode: "Emit Particles" (continuous stream)
      → Particle Separation: match container
```

---

## Stage 2 — DOP Network

```
FLIP Object DOP
  → SOP Path: /obj/geo1/flipsource
  → Initial Particle Separation: 0.05

FLIP Solver DOP
  → Particle Motion:
      Gravity: 0.0  -9.8  0.0
      Reseeding: ON (maintain particle density)
      Particle Radius Scale: 1.5
  → Volume Motion → Solver:
      Iterations: 3 (higher = more incompressible, slower)
  → Surface Tension: 0.0 (default) — raise to 0.01–0.05 for viscous/honey look
  → Viscosity: 0.0 → raise for thick fluid (honey: 100–500)

Static Object DOP (for collision geometry)
  → SOP Path: collision geometry
  → Collision Type: Volume (best quality)

Output DOP
```

---

## Stage 3 — Caching Particles

```
DOP Import SOP (SOP level)
  → Import: All Objects
  → Import Style: Fetch Geometry from DOP Network

File Cache SOP
  → File: $HIP/cache/flip_particles.$F.bgeo.sc
  → Cache entire frame range before meshing
```

---

## Stage 4 — Meshing (Particles → Surface)

```
File Cache SOP (read mode: cached particles)

VDB from Particles SOP
  → Voxel Size: 0.03–0.05 (finer = smoother surface, slower)
  → Particle Radius Scale: 1.5
  → Smooth Radius Scale: 1.5
  → VDB Type: Fog VDB + Level Set

VDB Smooth SOP (optional)
  → Iterations: 2–5 (softens surface, remove small ripples)

Convert VDB SOP
  → Convert to: Polygon Surface (for rendering with sharp normal detail)

Smooth SOP
  → Strength: 0.1 (after convert — minimal additional smoothing)

Vertex Normal SOP
  → Important: adds normals for correct water shader rendering
```

**Tip:** Cache meshed geometry separately from particles. Meshing is the slowest step — run overnight.

---

## Stage 5 — Whitewater

Whitewater adds foam, spray, and bubbles to the surface.

```
Whitewater Source SOP
  → Input: meshed surface from Stage 4
  → Curvature Threshold: 2.0–4.0 (higher = less emission, only at sharp waves)
  → Speed Threshold: 2.0 (only fast-moving areas emit spray)
  → Emission Scale: 0.5–1.0

DOP Network (whitewater sim):
  Whitewater Object DOP
  Whitewater Solver DOP
    → Life: 2.0–4.0 seconds
    → Buoyancy: 0.5
    → Adhesion: 0.1 (foam sticks to surface)

Cache whitewater particles:
  File Cache SOP → $HIP/cache/whitewater.$F.bgeo.sc
```

---

## Stage 6 — Solaris / LOPs

```
SOP Import LOP (fluid mesh)
  → SOP Path: /obj/fluid_mesh

SOP Import LOP (whitewater)
  → SOP Path: /obj/whitewater_cache

Environment Light LOP (Dome Light)
  → HDRI: coastal_sky.hdr
  → Intensity: 1.5

Camera LOP
  → Focal Length: 35mm, Aperture f/4.0
```

---

## Stage 7 — Water Shader (MaterialX)

```
Material Library LOP → New Material → MtlX Standard Surface VOP:

  Base Color: deep blue-green tint (0.02, 0.05, 0.06)
  Metalness: 0.0
  Specular: 1.0
  Roughness: 0.02  (very smooth for water)
  IOR: 1.33
  Transmission: 0.95  (highly transparent)
  Transmission Color: light blue-green (0.7, 0.9, 0.85)
  Subsurface: 0.1  (slight milky scattering in thick areas)
```

### Whitewater Shader
```
MtlX Standard Surface VOP (separate material):
  Base Color: white (1.0, 1.0, 1.0)
  Roughness: 0.5
  Transmission: 0.2
  Subsurface: 0.8  (foam is mostly scattered light)
  Subsurface Color: white
```

---

## Stage 8 — Karma XPU Render Settings

```
Karma Render Settings LOP:
  Renderer: Karma XPU
  Max Samples: 1024 (hero) / 64 (preview)
  Caustics: ON  (water caustics — expensive but essential for hero)
  Transmission Bounces: 8  (for light through water)
  
AOVs:
  beauty     → final composite layer
  depth      → lens blur in comp
  cryptomatte → matte for ocean layer
  motionvec  → motion blur in Copernicus
```

---

## Stage 9 — Output & Comp

```
USD Render ROP → $HIP/render/fluid.$F4.exr

Copernicus (post):
  File COP → fluid EXR
    → Denoise COP (NVIDIA Optix)
    → Color Correct COP (slight blue tint, raise highlights)
    → Lens Distort COP (subtle barrel)
    → COP Output → final.exr
```

---

## Performance Tips

| Optimization | Savings |
|-------------|---------|
| Preview with `Particle Separation: 0.1` (2x coarser) | 8x faster sim |
| Skip whitewater on first pass | 30–50% render time saved |
| Cache to `.vdb` instead of `.bgeo.sc` | 3–5x smaller disk size |
| Enable OpenCL on FLIP Solver | 2–4x faster |
| Karma XPU over CPU | 5–10x faster on modern GPU |

---

## Related
- `references/dop-nodes.md` — FLIP node reference and all solver parameters
- `references/render-pipeline.md` — Karma XPU, MaterialX, AOVs
- `references/copernicus.md` — Copernicus compositing for the final EXR
- `recipes/pyro-hero-shot.md` — Pyro pipeline (same cache/render structure)
