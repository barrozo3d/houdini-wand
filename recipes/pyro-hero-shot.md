# Recipe: Pyro Hero Shot Pipeline

A production-quality hero pyro shot (fire, explosion, or smoke) from sourcing through Karma XPU render with full AOVs. Assumes H20+.

---

## Stage 1 — Source Geometry

```
SOP level (inside a Geometry object):

Box/Sphere/Custom Geo
  → Pyro Source SOP
    → Mode: "Use Surface" (fills interior volume)
    → Attributes to Generate: density ✓  temperature ✓  fuel ✓  vel ✓
    → Velocity Scale: 1.0 (increase for more turbulent sourcing)
  → Scatter SOP (optional — for point-based sourcing on surface only)
```

**Tip:** Scatter + `Pyro Burst Source SOP` gives the best explosion sourcing — set Burst Time to 0.1s with a high Spread.

---

## Stage 2 — DOP Network

```
DOP Network inside the same Geometry object:

Volume Source
  → SOP Path: point to the Pyro Source SOP above
  → Activation: $SF == 1 (first frame) for explosion; $SF >= 1 for continuous fire/smoke

Pyro Solver
  → Pyro tab:
      Enable Combustion: ON (for fire), OFF (pure smoke)
      Time Scale: 1.0 (lower = slow motion)
      Buoyancy: 1.5–3.0
      Cooling Rate: 0.75–0.9 (lower = temperature persists longer)
  → Shape tab (micro-solvers applied each step):
      Turbulence: 0.5–2.0 at low frequency (0.5)
      Disturbance: 0.4–1.0 at medium frequency (1.0–2.0)
      Shredding: 0.2–0.5 (tears billowing edges)
      Wind: optional — adds directional drift
  → Advection:
      Method: Back and Forth (most accurate)
      CFL Condition: 1.0
  → Resolution:
      Uniform Divisions: 100–200 for hero quality
      Enable OpenCL: ON (major speed boost on GPU)

Output
  → connect Pyro Solver → Output
```

**Tip:** For explosion, disable Cooling Rate on the first 10 frames to let fire bloom outward, then ramp it back up.

---

## Stage 3 — Caching

Always cache before rendering. Cache to fast storage (NVMe).

```
Post-sim SOP (new Geometry object or same SOP):

DOP Import Fields
  → DOP Network: /obj/geo1/dopnet1
  → Fields: density  temperature  vel  flame  (add fuel if combustion is on)

File Cache SOP
  → File: $HIP/cache/pyro.$F.bgeo.sc   (or .vdb for smaller files)
  → Save to Disk (click once to cache full range)
  → After caching: File Mode → "Read from Disk"
```

**VDB is ~3–5x smaller than .bgeo.sc for volume data. Use .vdb for large sims.**

---

## Stage 4 — Art Direction Pass

After caching, open the cache in a SOP network and add VDB-level art direction:

```
File Cache SOP (read mode)
  → Volume VOP SOP
    → Read density field → add extra noise for high-frequency detail
    → Ramp result to crush blacks or enhance silhouette
  → VDB Smooth SOP (optional — reduces blocky voxels)
  → VDB Resample SOP (optional — upsample to 2x resolution for final render)
```

---

## Stage 5 — Solaris / LOPs Setup

```
In /stage (Solaris):

SOP Import LOP
  → SOP Path: /obj/pyro_cache/vdbimport1

Karma Physical Sky LOP (or Dome Light LOP)
  → Sky preset or HDRI

Volume Light LOP (optional — for fire self-illumination)
  → SOP Path: same volume cache

Karma Render Settings LOP
  → Min Samples: 8  Max Samples: 512
  → Path Tracing: ON
  → Enable Volumes: ON
```

---

## Stage 6 — Karma XPU Render Settings

```
Karma Render Settings LOP:
  Renderer: Karma XPU
  Pixel Samples: 8–16 (hero), 4 (preview)
  Volume Step Size: 0.1–0.5 (smaller = denser fire detail, slower)
  Volume Shadow Step Size: 1.0
  
AOVs to enable:
  beauty (default)
  diffuse    — unlit fire glow contribution
  emission   — pure fire emission pass
  depth      — for lens blur in comp
  cryptomatte — for isolation masking
  motionvec  — for motion blur in comp
```

---

## Stage 7 — Karma Volume Shader

```
In Material Library LOP:

Karma Volume VOP
  → Scatter Color: warm orange/yellow tint
  → Scatter Density: 1.0–3.0
  → Emission Color: connect to temperature field (hotter = brighter orange)
  → Blackbody Intensity: 1.0–2.0 (temperature → emission color)
  → Blackbody Temperature: 1200–2000 K range

Assign Material LOP
  → Target: the volume prim
  → Material: the Karma Volume VOP
```

---

## Stage 8 — Output

```
USD Render ROP  (in /out):
  → Stage Path: /stage
  → Render Settings LOP: /stage/karma_rendersettings
  → Output: $HIP/render/pyro.$F4.exr
  → Frame range: $FSTART–$FEND

hbatch command-line (farm-ready):
  hbatch -e /out/karma_render -f 1 100 myscene.hip
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Sim too noisy, no shape | Lower Turbulence, raise Disturbance frequency |
| Sim looks flat/blobby | Add Shredding 0.3–0.5; check buoyancy isn't too low |
| Render too slow | Reduce Volume Step Size to 0.5; enable OpenCL; lower Max Samples |
| Fire too bright/dark | Adjust Blackbody Intensity in the volume shader |
| Sim diverges/explodes | Lower Time Scale; reduce Velocity Scale on the source |

---

## Related
- `references/dop-nodes.md` — Pyro node reference and all micro-solver parameters
- `references/render-pipeline.md` — Karma XPU setup and AOV list
- `recipes/flip-fluid-render.md` — FLIP fluid pipeline (same caching/render pattern)
