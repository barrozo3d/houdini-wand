# DOP Nodes — Simulation Reference

Core Dynamic Operator nodes for Houdini simulations: Pyro, FLIP Fluid, RBD, Vellum, Cloth, Grains, Wire.

---

## Simulation Setup Pattern (all sims)

```
OBJ level:
  [Geometry Object] with SOP network producing source geometry
  [DOP Network] object — simulation runs inside here

Inside DOP network:
  [Solver-specific nodes] → [Merge] → [Output]
  
Post-sim:
  [DOP Import] SOP (in geometry object) — pulls sim data back to SOPs
```

---

## Pyro (Fire & Smoke)

### Core Nodes
| Node | Role |
|------|------|
| `Pyro Source` (SOP) | Converts geometry to pyro source attributes (density, heat, fuel, temperature) |
| `DOP Network` | Contains the pyro simulation |
| `Pyro Solver` (DOP) | Main solver — handles advection, buoyancy, combustion |
| `Source Volume` (DOP) | Injects source attributes each frame |
| `Volume Source` (DOP) | H20+ unified source node |
| `Gas Field VOP` (DOP) | VEX/VOP access to volume fields per-step |
| `Smoke Object` (DOP) | Creates the smoke/pyro object |

### Key Pyro Parameters
```
Pyro Solver:
  Divisions      — voxel resolution (higher = more detail, slower)
  Time Scale     — slow motion control (0.1 = 10x slowdown)
  Buoyancy       — upward lift force
  Cooling Rate   — how fast temperature drops
  Dissipation    — how fast density fades
  Turbulence     — adds detail noise to fields

Combustion:
  Fuel Inefficiency  — leftover fuel after burning
  Flame Height       — visual flame intensity
  Enable Combustion  — toggle fire vs smoke
```

### Quick Setup (H20+)
```
SOP level:
  geometry → Pyro Source → cached to disk (optional)

DOP level:
  Volume Source → Pyro Solver → Output

Post-sim SOP:
  DOP Import → volume render or further processing
```

---

## FLIP Fluid

### Core Nodes
| Node | Role |
|------|------|
| `FLIP Source` (SOP) | Converts geo to FLIP particles |
| `FLIP Object` (DOP) | Contains FLIP particle data |
| `FLIP Solver` (DOP) | Main solver — handles pressure, viscosity, surface tension |
| `Source Particles` (DOP) | Injects particles into the sim |
| `Collision Source` (SOP) | Converts static/animated geo to collision |
| `Static Object` (DOP) | Adds collider to the sim |
| `Kinematic Body` (DOP) | Animated collider |

### Key FLIP Parameters
```
FLIP Solver:
  Particle Separation  — controls resolution (smaller = more particles, slower)
  Substeps             — accuracy for fast-moving sims
  Viscosity            — 0 = water, higher = honey/lava
  Surface Tension      — droplet behavior
  Reseeding            — maintain particle distribution

FLIP Object:
  Initial Velocity     — starting velocity
  Particle Radius Scale — visual particle size
```

### Surface Extraction (post-sim)
```
DOP Import (FLIP particles)
→ Particle Fluid Surface (builds mesh from particles)
   → Smooth, Subdivide for final look
→ VDB from Particles → Polygons from Volume (alternative)
```

---

## Rigid Body Dynamics (RBD)

### Core Nodes
| Node | Role |
|------|------|
| `RBD Material Fracture` (SOP) | Fracture geometry (Voronoi, surface, Boolean) |
| `Assemble` (SOP) | Pack pieces + create name/pivot attributes |
| `RBD Object` (DOP) | Adds packed geometry as RBD object |
| `RBD Bullet Solver` (DOP) | Bullet physics solver (fast, stable) |
| `Static Object` (DOP) | Ground plane / static colliders |
| `Gravity` (DOP) | Global gravity force |
| `Fan` (DOP) | Wind-like directional force |
| `RBD Constraint Network` (DOP) | Glue/spring/hinge constraints between pieces |

### Constraint Types
```
Glue     — holds pieces together until force threshold (destruction)
Spring   — elastic connection
Pin      — fixed pivot point
Hinge    — rotation only
Cone Twist — cone-limited rotation (ragdoll joints)
```

### Fracture Workflow
```
SOP: [base geometry]
→ Voronoi Fracture (or Boolean Fracture / RBD Material Fracture)
→ Assemble (pack + name pieces)
→ [into DOP]
DOP: RBD Object (packed) → Bullet Solver → Output
Post: DOP Import → unpack for rendering
```

---

## Vellum

Vellum is a unified solver for cloth, soft body, hair, grains, and inflatables using Position Based Dynamics (PBD). Much faster setup than old Wire/Cloth solvers.

### Core Nodes
| Node | Role |
|------|------|
| `Vellum Configure Cloth` (SOP) | Set up cloth constraints |
| `Vellum Configure Soft Body` (SOP) | Tetrahedral soft body |
| `Vellum Configure Hair` (SOP) | Strand/hair simulation |
| `Vellum Configure Grain` (SOP) | Sand/grain simulation |
| `Vellum Weld Points` (SOP) | Attach pieces together |
| `Vellum Solver` (DOP) | Main PBD solver |
| `Vellum Constraints` (DOP) | Input constraints into sim |
| `Vellum Source` (DOP) | Inject geo/constraints mid-sim |
| `Vellum Object` (DOP) | The vellum body |

### Key Vellum Parameters
```
Cloth constraints:
  Stretch Stiffness   — resistance to stretching (1e6 = rigid, 1e3 = stretchy)
  Bend Stiffness      — resistance to bending
  Mass                — heavier = falls faster
  Damping             — energy loss (higher = quicker settling)

Vellum Solver:
  Substeps            — accuracy (3-5 for cloth, 10+ for collisions)
  Constraint Iterations — quality of constraint solving
  Gravity             — default {0, -9.8, 0}
```

### SOP-Level Vellum (H19+)
Vellum can run entirely in SOPs without a DOP network using the **Vellum Solver SOP**. Simpler to set up, good for most uses.

```
[geometry]
→ Vellum Configure Cloth
→ [Pin groups if needed: Group by proximity to attach points]
→ Vellum Solver SOP   ← runs sim inline
→ [post-process]
```

---

## Wire (Curves/Ropes)

```
[curve geometry]
→ Wire Object (DOP)
→ Wire Solver (DOP)
→ Static Object for collisions

Key params:
  Linear Stiffness  — resistance to stretching
  Angular Stiffness — resistance to bending
  Mass              — heavier = more sag
```

Note: For most new work, Vellum Hair is preferred over Wire solver.

---

## Grains / Sand

Vellum Grains is the modern approach:
```
[sphere/point cloud]
→ Vellum Configure Grain
→ Vellum Solver SOP
Key param: Friction, Repulsion Stiffness, Clumping
```

---

## Common DOP Utilities

| Node | Role |
|------|------|
| `Gravity` | Constant acceleration force |
| `Drag` | Air resistance / damping |
| `Fan` | Directional wind force |
| `Uniform Force` | Constant force in any direction |
| `POP Wind` | Wind force for particles |
| `Ground Plane` | Infinite flat collider |
| `DOP Import` (SOP) | Import sim data back to SOPs |
| `DOP I/O` (SOP) | Read/write sim state mid-simulation |

---

## Simulation Best Practices

```
1. Always cache sims to disk (File Cache SOP after DOP Import)
   — prevents re-simulation on parameter changes downstream

2. Start low-res: get the motion right before increasing resolution
   — Pyro: increase Divisions last
   — FLIP: increase particle separation last
   — RBD: fewer fracture pieces first

3. Use substeps for fast-moving objects
   — Rule of thumb: 2-4 substeps for normal sims, 8-16 for impacts

4. Pre-roll: simulate a few frames before frame 1 for settled initial state
   — Use Time Shift to offset the sim start

5. Constraints before fracture in RBD
   — Build constraint network before breaking

6. Vellum over old solvers: use Vellum for cloth/hair/soft in H19+
```
