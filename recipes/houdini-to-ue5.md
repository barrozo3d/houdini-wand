# Recipe: Houdini → Unreal Engine 5 Pipeline

Two pathways for bringing Houdini work into UE5:
1. **Houdini Engine** — live procedural HDAs inside UE5 (fully interactive, re-cooks on parameter change)
2. **Static export** — geometry/VDBs/caches baked to USD/FBX/Alembic and imported as static assets

---

## Pathway A: Houdini Engine (Procedural HDA in UE5)

### What it is
Houdini Engine for Unreal is a UE5 plugin that runs a Houdini "session" in the background. You place an HDA (Houdini Digital Asset) in the UE5 level and adjust its parameters from the UE5 Details panel — every change re-cooks the HDA and updates the mesh in-engine.

### Step 1 — Build the HDA in Houdini

Design the SOP network as a **subnet** with exposed parameters:

```
/obj level:
  Geometry Object
    → enter network
    → build procedural SOP network (e.g. building generator, road placer, scatter system)
    
    Key SOP outputs:
      → Geometry for static mesh:   first output connector
      → Curve data for splines:     string attribute s@unreal_curve = "1"
      → Packed instances:           packed prim with s@unreal_instance = "StaticMesh'/Game/...')"

Expose parameters for UE5 UI:
  Right-click any parameter → "Promote to Node" → creates control in the subnet interface
  OR: right-click → "Spare Parameters" to add custom float/int/string/toggle/file inputs
```

### Step 2 — Package as HDA

```
In /obj level:
  Right-click the Geometry object → "Create Digital Asset"
  → Name: MyAsset_v001
  → Save Path: $HIP/hdas/MyAsset_v001.hda
  → Enable "Save to Disk" → saves .hda file

Version control tip: keep .hda files in a shared UE5 Content/Houdini/ directory
```

### Step 3 — Install Houdini Engine Plugin in UE5

```
1. Download Houdini Engine for Unreal from SideFX.com
   → Match version to your installed Houdini (e.g. H21 → HoudiniEngine_H21_UE5.4)
2. Place plugin folder in: [UE5Project]/Plugins/HoudiniEngine/
3. Enable plugin: Edit → Plugins → search "Houdini Engine" → Enable
4. Restart UE5
5. Edit → Project Settings → Houdini Engine:
   → Houdini Location: C:/Program Files/Side Effects Software/Houdini X.X.X/
```

### Step 4 — Import and Use HDA in UE5

```
Content Browser → Import → select .hda file
  → HDA asset appears in Content Browser (orange H icon)

Drag HDA into level viewport
  → "HoudiniAssetActor" appears with a Houdini component

Details panel:
  → Houdini Engine Component → shows all exposed parameters
  → Adjust values → click "Recook" (or enable Auto-Recook)
  → Outputs appear as generated Static Mesh / Skeletal Mesh / Instanced components
```

### Useful HDA Patterns

#### Scatter system with UE5 foliage
```vex
// In a Point Wrangle, mark points as Unreal instances:
s@unreal_instance = "/Game/Foliage/Tree_SM.Tree_SM";
// Place a Scatter SOP + Point Wrangle → Houdini Engine creates 
// Instanced Static Mesh components in UE5, not individual actors
```

#### Procedural road/spline following
```
Houdini SOP: Curve SOP (output)
  → mark geometry as a spline with s@unreal_curve = "1"
  → UE5 receives a spline component
  → Houdini Engine auto-creates UE5 Spline Component
```

#### LOD generation
```
Multiple SOP outputs:
  Output 1 (LOD0): full detail mesh
  Output 2 (LOD1): polyreduced mesh (PolyReduce SOP at 0.5)
  Output 3 (LOD2): polyreduced mesh (PolyReduce SOP at 0.15)
  → Each output creates a LOD level on the Static Mesh in UE5
  → Set output detail attribute: detail s@unreal_lod_screensizes = "1.0 0.25 0.05"
```

---

## Pathway B: Static Export (USD / Alembic / FBX)

Best for final rendered geometry, simulations, and VDB volumes that don't need to re-cook.

### Export Animated Geometry (Alembic)
```
In Houdini (Solaris/SOP ROP):

ROP Alembic SOP (or Alembic ROP at /out):
  → Output File: $HIP/exports/mysim.abc
  → Primitive Groups: export by material group
  → Uvs, Normals: ON
  → Velocities: ON (required for motion blur in UE5)
  → Build from Path Attribute: s@path (if using Solaris)

In UE5:
  Content Browser → Import → .abc file
  → Geometry Cache type → drag into level
  → Playback via Timeline or Blueprint
```

### Export Static Mesh (FBX)
```
ROP FBX SOP at /out:
  → Export → Static Model
  → Vertex Normals, UVs: ON
  → Triangulate Geometry: ON (UE5 prefers triangulated meshes)

In UE5: Import → FBX → Static Mesh import options
```

### Export VDB Volume (for Niagara / Volumetric Fog)
```
Houdini: File Cache SOP → save as .vdb

UE5:
  Import .vdb → creates Volume Texture asset
  Use in:
    → Niagara Grid3D Collection (sparse voxel simulation)
    → Heterogeneous Volumes component (direct VDB rendering in UE5.3+)
    → Material using Volume Texture sampling
```

### Export USD Scene (Full Scene with Materials)
```
Houdini Solaris:
  USD ROP at /out → File.usdc or .usdz
  → Include: materials, cameras, lights
  → Merge with UE5 level via: Content Browser → Import → .usdc

UE5 USD Stage Editor:
  Window → USD Stage → open .usdc
  → Inspect hierarchy, tweak materials, animate
```

---

## PDG / TOPs for Batch Export to UE5

For generating many variants (building facades, prop scatter presets, etc.):

```
/obj → ROP Fetch TOP
  → Points: iterate over parameter range (e.g. seed 0–99)
  → Each work item: cooks with different seed → exports unique static mesh

File Tag TOP
  → Collect all output .fbx files

→ Import entire folder into UE5 Content Browser at once
```

---

## Common Issues

| Problem | Fix |
|---------|-----|
| HDA cooks but no geometry appears in UE5 | Check output is connected to first output connector in the HDA |
| Parameters don't show in Details panel | Make sure parameters are promoted to the subnet interface, not just in the internal network |
| UE5 crashes on HDA import | Match Houdini Engine plugin version to your Houdini installation exactly |
| Alembic plays back incorrectly | Export velocities (v@v); enable "Sample Velocities" on import |
| VDB volume renders black | Assign Heterogeneous Volumes material in UE5 + configure density channel |
| Packed instances not instanced in UE5 | Set `s@unreal_instance` on the packed primitives; do NOT unpack before export |

---

## Related
- `tutorials/houdini-fx-in-unreal.md` — tutorial covering Houdini Engine / HDA workflow in UE5
- `tutorials/procedural-hdas-for-unreal.md` — building HDAs specifically for UE5 usage
- `references/houdini-workflow.md` — HDA creation, versioning, and management
- `references/sop-nodes.md` — SOP nodes for export preparation
