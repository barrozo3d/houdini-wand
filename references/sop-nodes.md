# SOP Nodes Reference

Core Surface Operator nodes in Houdini. Organized by category with usage notes.

---

## Geometry Creation

| Node | What it does | Key parameters |
|------|-------------|----------------|
| `Box` | Cube/box mesh | Size, Divisions |
| `Sphere` | UV or polygon sphere | Type, Rows/Cols |
| `Grid` | Flat plane | Rows, Cols, Size |
| `Tube` | Cylinder / cone | Radius, Height, Caps |
| `Torus` | Donut shape | Radii, Rows/Cols |
| `Line` | Line of points | Origin, Direction, Points |
| `Circle` | Circle curve or polygon | Type, Divisions |
| `Curve` | Freehand curve (NURBS/Bezier/polygon) | Type, Order |
| `Font` | 3D text from font | Text, Font, Size, Extrude |
| `Volume` | Creates a volume primitive | Size, Divisions |

---

## Geometry Modification

| Node | What it does | Notes |
|------|-------------|-------|
| `Transform` | Move/rotate/scale geometry | Non-destructive |
| `Blast` | Delete points/prims/edges by group or expression | Use "Delete Non-Selected" to invert |
| `Delete` | Delete by expression or attribute value | |
| `Dissolve` | Remove edges while merging faces | Good for topology cleanup |
| `Divide` | Triangulate, convert quads, clean mesh | "Remove Shared Edges" for triangulation |
| `PolyExtrude` | Extrude faces/edges along normals | "Local Translate" for inset+extrude |
| `PolyBevel` | Bevel edges/points | Offset, Segments |
| `PolySplit` | Split edges interactively | |
| `Subdivide` | Catmull-Clark subdivision | Depth controls iterations |
| `Smooth` | Average point positions | Strength, Iterations |
| `Remesh` | Uniform triangle remesh | Target Edge Length |
| `Boolean` | Union/Subtract/Intersect mesh operations | Robust Boolean available H20+ |
| `Clip` | Cut geometry with a plane | |
| `Mirror` | Mirror across axis | Merge option |
| `Bend` | Bend/twist/taper geometry | Capture Region |
| `Lattice` | Deform with a control lattice | |
| `Wireframe` | Convert curves to tube geometry | |

---

## Points & Attributes

| Node | What it does | Notes |
|------|-------------|-------|
| `Scatter` | Distribute points on surface | Density, Seed |
| `Points from Volume` | Distribute points inside volume | Uses `Distribute Points in Volume` internally |
| `Attribute Create` | Add/set an attribute | Class: Point/Prim/Vertex/Detail |
| `Attribute Delete` | Remove attributes | |
| `Attribute Rename` | Rename an attribute | |
| `Attribute Promote` | Change attribute class (Point→Prim etc.) | |
| `Attribute Transfer` | Copy attributes between geos via proximity | |
| `Attribute Blur` | Smooth attribute values across mesh | |
| `Attribute Randomize` | Add random variation to an attribute | |
| `Attribute Noise` | Apply noise to attribute values | |
| `Attribute from Map` | Sample texture map into attribute | |
| `Point Wrangle` | VEX code applied per-point | Most versatile SOP |
| `Prim Wrangle` | VEX code applied per-primitive | |
| `Detail Wrangle` | VEX code applied once (detail context) | |
| `Vertex Wrangle` | VEX code applied per-vertex | |
| `Sort` | Reorder points/prims by attribute or spatially | |
| `Measure` | Calculate perimeter, area, curvature, volume | Writes to attributes |

---

## Curves

| Node | What it does | Notes |
|------|-------------|-------|
| `Resample` | Redistribute points along curve evenly | Segment Length or Max Segments |
| `Fuse` | Merge points within tolerance | Essential for watertight meshes |
| `PolyPath` | Convert poly curves to single polygon | |
| `Convert` | Convert between types (NURBS↔Bezier↔Poly) | |
| `PolyFrame` | Generate N/T/B frame along curve | |
| `Sweep` | Extrude a cross-section along a path | Profile curve + Path curve |
| `Skin` | Skin surface through profile curves | |
| `Rails` | Build surface from two guide rails | |
| `Loft` | Surface through multiple profile curves | |

---

## Instancing & Scattering

| Node | What it does | Notes |
|------|-------------|-------|
| `Copy to Points` | Instance geometry at each point | Uses `orient`/`N`/`up` attributes for rotation |
| `Copy and Transform` | Stamp with transforms along a path | |
| `Instance` | Lightweight point instancing (render-time) | Uses `instance` string attribute |
| `Packed Primitives` | Pack geometry into packed prims | Efficient for large counts |
| `Unpack` | Unpack packed primitives to geo | |

### Key attributes for Copy to Points
```
v@N         — normal (up direction)
v@up        — secondary up
p@orient    — full quaternion rotation (overrides N/up)
v@scale     — per-instance scale (or f@pscale for uniform)
f@pscale    — uniform scale
s@instance  — path to instanced object (for Instance SOP)
```

---

## Volumes

| Node | What it does | Notes |
|------|-------------|-------|
| `VDB from Polygons` | Convert mesh to VDB SDF/fog | Voxel Size controls resolution |
| `VDB from Particles` | Convert particle system to VDB fog | |
| `Polygons from Volume` | Convert VDB back to mesh | |
| `Volume VOP` | VEX for volumes via VOPs | |
| `Volume Wrangle` | VEX code on volume voxels | |
| `VDB Combine` | Boolean/math ops on VDB volumes | |
| `VDB Smooth` | Smooth a VDB volume | |
| `VDB Reshape` | Dilate/erode a VDB | |
| `VDB Activate` | Expand/contract active voxel region | |
| `Volume Blur` | Gaussian blur on a volume | |

---

## Procedural & Utility

| Node | What it does | Notes |
|------|-------------|-------|
| `Switch` | Toggle between inputs | Driven by expression or parameter |
| `Null` | Pass-through, used for organization/naming | Best practice: name inputs/outputs |
| `Merge` | Combine multiple geometry streams | |
| `Object Merge` | Pull geometry from another object | Essential for inter-object references |
| `Fetch` | Fetch attribute from another node | |
| `Time Shift` | Sample geometry at a different time | |
| `Trail` | Generate motion trail from animated points | |
| `Group` | Create point/prim/edge groups | |
| `Group by Range` | Group by index range | |
| `Group Expression` | Group by VEX expression | |
| `Partition` | Create groups from attribute values | |
| `Foreach Begin/End` | Loop over prims/points | Merge feedback for accumulation |
| `Compile Block` | Mark compiled SOP network for speed | Significant performance gains |
| `Labs` | SideFX Labs toolset — hundreds of extra SOPs | Install via SideFX Labs plugin |

---

## Essential Workflow Patterns

### Clean Procedural Pattern
```
[Creation SOP]
→ Transform (normalize position/scale)
→ [Modification chain]
→ Null (OUT_name)    ← always end with a named null
```

### Attribute-Driven Variation
```
Scatter (on base geo)
→ Attribute Randomize (per-point seed values)
→ Copy to Points
    [Instance geo] → input 2
→ Null OUT_instances
```

### Feedback Loop (iterative deformation)
```
Foreach Begin (Feedback, iterations=N)
→ [deformation step]
→ Foreach End (Feedback)
```
