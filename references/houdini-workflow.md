# Houdini Workflow Patterns

Network editor patterns, project structure, HDAs, and general Houdini workflow practices.

---

## Network Editor Fundamentals

### Context Hierarchy
```
/obj                    OBJ level — scene, cameras, lights (legacy), object containers
/obj/geo1/              SOP level — geometry nodes inside an object
/obj/dopnet1/           DOP level — simulation nodes
/stage                  LOP level — Solaris/USD scene assembly
/img                    COP level — compositing
/ch                     CHOP level — animation/audio/motion data
/tasks                  TOP level — PDG task graphs
```

### Node Color Convention (community standard)
```
Red/Orange   — generators (Box, Sphere, Scatter)
Blue         — deformers / modifiers
Green        — attribute operations
Yellow       — utility / null / output nodes
Purple       — VOPs / wrangles
Cyan         — simulation nodes
Grey         — disabled / reference nodes
```

### Naming Conventions
```
ALL_CAPS    — input/output nulls (e.g., IN_geo, OUT_result)
lowercase   — working nodes
PascalCase  — HDAs / digital assets
prefix_     — grouped operations (cloth_setup, sim_source)
```

---

## Essential Workflow Patterns

### The Null Pattern
Always terminate networks with named Null nodes:
```
[final SOP] → Null (OUT_result)
```
- Locks the output reference so upstream changes don't break downstream connections
- Makes intent clear — where to connect from outside

### Object Merge Pattern
Pull geometry from other objects without parenting:
```
Object Merge → type path to source object's output
```
Key setting: **Transform** — "Into This Object" transforms to local space

### Non-Destructive Stack
```
Base Geometry
→ Transform (normalize)
→ [modification A] — bypass with B key
→ [modification B]
→ [modification C]
→ Null OUT_final
```
Keep each step as a separate node. Use **bypass** (B key) to toggle steps.

### Attribute → Variation Pipeline
```
[geometry]
→ Scatter
→ Attribute Randomize (s@variant = random int as string)
→ Copy to Points
   [merged asset collection] → input 2
```

---

## HDAs — Houdini Digital Assets

HDAs are encapsulated subnetworks that appear as a single node.

### Creating an HDA
1. Build network inside a Geometry object
2. Select all nodes → right-click → Collapse into Subnet
3. Right-click subnet → Convert to Digital Asset
4. Set **Operator Name**, **Label**, **Save to Library** (.hda file)
5. Define interface: **Type Properties** → Parameters tab

### HDA Parameter Types
```
Float / Int / Toggle / String / Color / Ramp / Button / Label
Folder (Tab) — groups parameters into tabs
Multiparm Block — repeatable parameter groups (variable-count arrays)
```

### Linking Internal Parameters
```
Inside HDA: right-click parameter → "Promote Parameter to Node"
Automatically creates UI parameter + links via channel reference: ch("../../myparam")
```

### HDA Best Practices
```
- Always expose key parameters (don't bury values in nodes)
- Add Help text to every parameter (right-click → Edit Parameter Interface → Help)
- Use spare parameters for documentation
- Version HDAs: change Minor Version when adding params, Major for breaking changes
- Store HDAs in project's otls/ folder and add to HOUDINI_OTLSCAN_PATH
```

---

## Project Structure

```
project/
├── hip/          — .hip scene files
├── geo/          — cached geometry (.bgeo.sc, .vdb)
├── sim/          — simulation caches (.sim, .simdata)
├── render/       — render output images
├── comp/         — compositing files
├── tex/          — textures
├── otls/         — HDAs (.hda, .otl)
├── scripts/      — Python scripts
└── ref/          — reference images/video
```

Use `$HIP` (current hip file dir) and `$JOB` (project root) in file paths:
```
$HIP/../geo/myfile.$F4.bgeo.sc    — frame-padded cache
$JOB/tex/mytexture.rat
```

---

## File Cache Pattern

Always cache heavy SOPs and sim results:
```
[heavy SOP or DOP Import] → File Cache → [downstream network]
```
- File Cache SOP: set path to `$HIP/../geo/cachename.$F4.bgeo.sc`
- Toggle **Save to Disk** to bake, then switch to **Load from Disk**
- Downstream nodes don't recompute when cache exists

---

## Expressions & HScript

```hscript
# Channel references
ch("../othernode/parm")      — float channel from another node
chs("../node/strparm")       — string channel
chop("/ch/path/channel")     — CHOP channel value

# Frame/time
$F                           — current frame
$T                           — current time (seconds)
$FPS                         — frames per second
$NFRAMES                     — total frame count

# Fit/ramp
fit($F, 1, 100, 0, 1)       — remap frame to 0-1 over 100 frames
smooth(0, 1, fit($F, 1, 50, 0, 1))  — smoothstep version

# Random per-prim/point (in Attribute Expression SOP)
rand($PT)                    — random per point
rand($PR)                    — random per primitive
```

---

## Performance Tips

```
1. Compile SOP networks between Compile Begin/End nodes
   — 5-20x speedup on parallelizable chains

2. Pack geometry before Copy to Points for large instance counts
   — Packed Primitives are instances, not duplicates

3. Use File Cache at sim output — prevents full re-sim on downstream changes

4. Lock nodes with heavy background processing:
   Node → right-click → Save Geometry to Node (locked)

5. Viewport: reduce display flag resolution for heavy geos
   — Click the small monitor icon on the node

6. Use VEX wrangles over Python SOPs for per-point/prim operations
   — VEX is multi-threaded; Python is not

7. Instancing at render time (Instance SOP or s@instance attribute)
   — Millions of copies without mesh duplication in memory
```

---

## Useful Keyboard Shortcuts

```
Network Editor:
  Tab              — node search / add node
  B                — bypass toggle
  L                — layout selected nodes
  W                — wireframe toggle (viewport)
  Y                — select all in current subnet
  Enter            — dive into subnet
  Escape           — go up one level
  /                — jump to /obj root

Viewport:
  Space + 1/2/3/4  — perspective / top / front / right views
  G                — frame selected
  H                — frame all
  5                — toggle perspective/ortho
  Numpad 0         — camera view
  Z                — zoom to cursor

Timeline:
  Space            — play/pause
  Alt+Left/Right   — step one frame
  Shift+Left/Right — jump to start/end
```
