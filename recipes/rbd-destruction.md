# Recipe: RBD Destruction Pipeline

Full procedural destruction from fracturing through constraint teardown, secondary debris, pyro sourcing from impacts, and Karma render. Assumes H20+.

---

## Stage 1 — Fracturing

Choose the fracture method based on the destruction look:

### Voronoi (Default — Chunky Shards)
```
SOP level:

Source Geometry (e.g. Wall/Building mesh)
  → Voronoi Fracture Points SOP  (scatter interior points)
    → Number of Points: 50–200 (more = smaller pieces)
    → Relax Iterations: 5 (distributes points evenly)
  → Voronoi Fracture SOP
    → Input 1: source geo, Input 2: scatter points
    → Inside Surface: enable + assign a material tag
    → Connectivity: add piece attribute ✓
    → Primitive group "outside_group" for exterior faces
```

### Boolean Fracture (Cuts Along Detail Lines)
```
Knife SOP  or  Boolean Fracture SOP
  → Cut geometry along pre-modeled detail meshes (window frames, panel seams)
  → Combine with Voronoi for interior chunks
```

### Detail Pass (Add Chipping)
```
After fracture:

Scatter SOP → scatter 200 points on surface
Voronoi Fracture SOP (second pass, smaller pieces: 0.05 scale)
  → Creates surface chip/spall geometry
  → Merge with main fracture pieces

Assemble SOP
  → Creates packed primitives (one prim per piece — HUGE performance gain)
  → Enable "Create Name Attribute" for constraint network
  → Name attribute: "name"
```

---

## Stage 2 — Constraint Network

Constraints hold pieces together until forces cause them to break.

```
SOP level (new Geometry object: "constraints"):

Connectivity SOP → component: "primitive"
Primitive Wrangle → build constraint network:

// Builds glue constraints between adjacent pieces
// Run this in a Point Wrangle on the Assemble output

// Auto-generate constraints:
SOP Solver → Constraint Network SOP
```

**Recommended approach — Constraint Network SOP:**
```
Assemble SOP output
  → Constraint Network SOP
    → Mode: "Surface Contact"  (connects touching pieces)
    → Maximum Distance: 0.01   (close-tolerance only)
    → s@constraint_name = "glue"   (default glue constraint type)
    → f@strength = 1e6             (max force before breaking)
    → Add groups: "outer" (exterior) vs "inner" (structural)
```

---

## Stage 3 — DOP Network

```
RBD Material Fracture DOP  (H20+ preferred, handles all-in-one)
  → SOP Path: /obj/fractured_geo/assemble1
  → Constraint Network: /obj/constraints/constraintnetwork1
  → Collision Layer: static floor/ground object

Rigid Body Solver DOP
  → Sub Steps: 2–4 (more = more accurate constraint teardown)
  → Constraint Iterations: 100–250

Gravity DOP
  → Magnitude: -9.81

Static Object DOP (floor, ground plane)
  → Type: Volume Collision
  → SOP Path: /obj/ground/box1

Constraint Network DOP
  → Groups:
      "outer" → Glue Constraint → Strength: 1e5 (breaks with moderate impact)
      "inner" → Glue Constraint → Strength: 1e7 (structural, needs large force)
```

---

## Stage 4 — Debris & Secondary Particles

Emit dust/pebble particles at impact locations.

```
Post-sim SOP (DOP Import):

DOP Import SOP
  → Import: active_state attribute, v (velocity), P

Dust Source:
  Point Wrangle
    → Emit from high-velocity impact points
    → if (length(v@v) > 3.0 && i@active == 1) i@emit = 1;

Pop Network
  → Source: above wrangle (emit 50–100 particles per impact point)
  → Force: Drag 0.8 + Turbulence 1.0
  → Life: 1.5–3.0 seconds

VDB from Points SOP
  → Convert particle cloud to renderable volume for dust mist
```

---

## Stage 5 — Pyro from Impacts (Optional)

Source pyro/smoke from impact points using the same technique:

```
// In the RBD post-sim SOP:
Point Wrangle:
  if (length(v@v) > 5.0 && i@active) {
    v@pyro_vel = v@v * 0.3;   // inject velocity into pyro source
    f@density  = 1.0;
  }

Pyro Source SOP (on the impact points)
  → connect to a DOP Pyro Solver (separate DOP network)
  → Use "velocity injection" mode for impact direction
```

---

## Stage 6 — Caching

```
Cache order (important):
1. RBD sim → $HIP/cache/rbd.$F.bgeo.sc   (packed primitives, small files)
2. Dust particles → $HIP/cache/dust.$F.bgeo.sc
3. Pyro (if used) → $HIP/cache/pyro.$F.vdb

DOP Import SOP → File Cache SOP for each.
After caching, set File Cache to Read mode.
```

---

## Stage 7 — Solaris Setup

```
SOP Import LOP (RBD chunks — packed prims)
  → Houdini auto-unpacks packed prims into USD
  → Geometry instancing preserves performance

SOP Import LOP (dust + debris particles)

SOP Import LOP (pyro volume, if used)

Assign Material LOP:
  → Concrete material → USD path to chunk prims
  → Dust volume material → Karma Volume VOP
```

---

## Stage 8 — Karma Render

```
Karma Render Settings LOP:
  Motion Blur: ON (critical for destruction — pieces are moving fast)
  Shutter: 0.5
  Motion Samples: 2

AOVs:
  beauty
  depth       (for focal blur in comp)
  cryptomatte (chunk isolation for compositing)
  motionvec   (motion vectors)

Camera: low angle, wide (28–35mm) → makes destruction feel large-scale
```

---

## Art Direction Tips

| Goal | Technique |
|------|-----------|
| Slower, bigger feel | Lower Time Scale on Rigid Body Solver (0.5–0.7) |
| Pieces should drift, not slam | Reduce constraint strength on outer group |
| More dust | Lower dust velocity threshold in Point Wrangle |
| Pieces look too uniform | Add `mountain` SOP noise to fracture interior faces |
| Structural collapse feel | Start with inner constraints 10x stronger than outer; let outer break first |

---

## Related
- `references/dop-nodes.md` — RBD Solver, Constraint Network, Voronoi Fracture parameters
- `references/sop-nodes.md` — Assemble, Voronoi Fracture, Connectivity SOPs
- `recipes/pyro-hero-shot.md` — Pyro setup for dust/smoke from impacts
- `references/render-pipeline.md` — Karma render settings for destruction shots
