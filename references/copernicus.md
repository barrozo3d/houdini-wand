# Copernicus — 2D Compositing & Texture Pipeline Reference

Houdini's COP2 replacement, introduced in H20.5 and production-ready in H21. A node-based 2D/image processing network (COP context) with GPU-accelerated cable connections, deep integration with Karma renders, and procedural texture generation. Replaces the old Composite Operators network.

---

## Overview

```
Old system:  COP2 (legacy) — tile-based, CPU, legacy nodes
New system:  Copernicus — GPU-accelerated, cable-based, full float precision

Copernicus lives in:  /img  network context  (same URL bar as COP2)
Entry point:  Geometry → right-click → Create New COP Network
             OR: pane header bar → change context to COP
```

Copernicus is designed for three use cases:
1. **In-compositor render post-processing** — tweak Karma renders without leaving Houdini
2. **Procedural texture generation** — build tileable textures, masks, height maps as SOP-like networks
3. **Image analysis + data extraction** — sample image data back into SOP geometry via attributes

---

## Core Concepts

### Cable-Based Evaluation
Unlike COP2's tile-based pipeline, Copernicus uses "cables" — data flows from node to node as full-resolution images. Each cable carries:
- A typed image (color, depth, normal, mask, etc.)
- A resolution and format
- An optional time dimension (image sequences)

### Node Types
| Category | Description |
|----------|-------------|
| **Input nodes** | Load images, Karma render output, SOP geometry |
| **Generator nodes** | Procedural patterns (noise, gradients, shapes) |
| **Filter nodes** | Blur, sharpen, color correction, distort |
| **Composite nodes** | Merge, over, blend layers |
| **Output nodes** | Write to disk, export to SOP attributes |

---

## Getting Started

### Load a Karma Render into Copernicus
```
1. In Karma ROP → check "Send to Copernicus" or use Live Render LOP
2. In the COP network: Karma Render COP node → points to Karma ROP
3. Image appears as a cable — pipe into color correction nodes
4. Final → COP Output node → writes to disk
```

### Standalone Procedural Texture
```
1. In /img network: Tab → Noise COP (or Pattern COP)
2. Adjust frequency, octaves, offset
3. Pipe through Ramp COP for color grading
4. Add Normal COP for height-to-normal conversion
5. COP Output → save as .exr/.rat/.png
```

---

## Key Nodes

### Input / Output
| Node | Purpose |
|------|---------|
| `File COP` | Load image from disk (EXR, PNG, TIFF, RAT, etc.) |
| `Karma Render COP` | Pull live or cached Karma render output |
| `SOP Import COP` | Convert SOP geometry UV attribute data to image |
| `COP Output` / `COP ROP` | Write final image to disk |
| `Fetch COP` | Import image from another COP network |

### Generators
| Node | Purpose |
|------|---------|
| `Noise COP` | Perlin, Worley, Alligator, Simplex noise patterns |
| `Pattern COP` | Geometric patterns (checker, brick, grid, dots) |
| `Gradient COP` | Linear/radial gradient image |
| `Constant COP` | Solid color fill |
| `UV Texture COP` | Generate UV-space coordinate texture |
| `Ramp COP` | Map value range to a color gradient |

### Filters
| Node | Purpose |
|------|---------|
| `Blur COP` | Gaussian, box, or motion blur |
| `Sharpen COP` | Unsharp mask |
| `Color Correct COP` | HSV, levels, curves, exposure |
| `Chromatic Aberration COP` | Lens aberration effect |
| `Lens Distort COP` | Barrel/pincushion distortion |
| `Warp COP` | Distort image by a vector displacement field |
| `Bilateral Filter COP` | Edge-preserving smoothing |
| `Denoise COP` | Optix/Intel denoiser for Karma renders |

### Compositing
| Node | Purpose |
|------|---------|
| `Merge COP` | Combine multiple images (over, under, add, multiply, etc.) |
| `Mask COP` | Composite using alpha or luminance mask |
| `Crop COP` | Crop to region |
| `Resize COP` | Resize/resample image |
| `Transform COP` | 2D translate/rotate/scale |
| `Switch COP` | Conditional image select |

### Data / Analysis
| Node | Purpose |
|------|---------|
| `Sample COP` | Sample image at UV coordinates → outputs values |
| `Histogram COP` | Analyze image tone distribution |
| `Analyze COP` | Extract statistics (min, max, mean, variance) per channel |

---

## AOV Compositing Workflow (Karma → Copernicus)

```
Karma renders multi-layer EXR:
  beauty, diffuse, specular, emission, depth, cryptomatte, normal, velocity

In Copernicus:
  File COP ("beauty.exr")
    ↓ Split EXR Layers COP → separate AOV cables
    ↓ Denoise COP (beauty)
    ↓ Color Correct COP
    ↓ Merge COP (add specular bloom)
    ↓ Lens Distort COP
    ↓ COP Output → final.exr
```

---

## Procedural Texture Pipeline

### Tileable Noise Texture
```
Noise COP
  → frequency: 4  octaves: 6  roughness: 0.5
  → Ramp COP   → map 0-1 to color gradient
  → Normal COP → height-to-normal (strength: 1.5)
  → COP Output → save bump.exr + normal.exr
```

### Height-to-Normal Map
```
File COP (heightmap.png)
  → Normal COP
    → Method: Sobel
    → Strength: 2.0
    → Output Space: DirectX or OpenGL
  → COP Output → normalmap.exr
```

---

## SOP ↔ Copernicus Data Exchange

### SOP → COP (geometry to image)
```
SOP level: UV Texture Attribute on mesh (u, v per point/vertex)
COP level: SOP Import COP → reads attribute as image
Use case: bake point cloud colors into a UV texture
```

### COP → SOP (image to geometry attribute)
```
COP level: finish network, pipe to output node
SOP level: COP Import SOP → reads COP network as image
           → Attribute From Map SOP → map image pixels to point attributes
Use case: displacement from procedural texture, color per point from image
```

---

## Copernicus in H20.5 vs H21

| Feature | H20.5 | H21 |
|---------|-------|-----|
| Status | Introduced (beta/preview) | Production-ready |
| GPU acceleration | Yes | Improved |
| Karma integration | Basic | Live Render LOP + Background Plate LOP |
| Node count | Limited | Full node library |
| COP2 compatibility | Can import COP2 networks | Legacy COP2 still accessible |

---

## Accessing Old COP2 Nodes
If you need a node that exists in COP2 but not yet in Copernicus:
```
/img network → Tab → search "COP2" prefix → legacy nodes still work
But: cannot directly cable COP2 output into Copernicus node
Workaround: COP2 → write to disk → File COP in Copernicus to read
```

---

## Common Pitfalls

1. **Resolution mismatch** — when merging two images of different sizes, add a `Resize COP` before the Merge
2. **Color space confusion** — Karma renders in linear; File COP may auto-apply OCIO; disable "Apply Color Correction" in File COP for EXR inputs
3. **Depth channel** — depth AOV from Karma is in world-space distance, not normalized; use `Fit COP` to normalize before visualizing
4. **COP Output vs COP ROP** — `COP Output` inside the network is for final delivery; `COP ROP` at `/out` is for batch rendering via hbatch
5. **Performance** — very large resolutions (4K+) slow preview; use `Viewport Resolution` override in COP preferences for fast iteration

---

## Related Reference Files
- `references/render-pipeline.md` — Karma XPU/CPU, AOVs, EXR output
- `references/release-notes-h21.md` — H21 Copernicus production-ready status + Background Plate LOP
- `references/release-notes-h20-5.md` — H20.5 Copernicus introduction
