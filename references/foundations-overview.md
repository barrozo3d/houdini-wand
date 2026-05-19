# Houdini Foundations — Core Concepts Reference

**Source:** SideFX Houdini Foundations book (Robert Magee), Version 19.5 Edition  
**ISBN:** 978-1-7753338-2-1  
**Ingested:** 2026-05-19  
**Note:** Foundational concepts apply across all versions. Version-specific differences in `release-notes-h21.md` and `release-notes-h20-5.md`.

---

## Core Philosophy

Everything in Houdini is procedural. Every action creates a node; nodes wire into networks forming a "recipe" that can be tweaked, iterated, and reused. Networks pass data (attributes) down the chain — this is what gives Houdini its power.

- **Non-destructive**: Changes cascade through the entire network automatically
- **Directable**: Editable deep into production without rebuilding
- **Tool-building**: Networks can be wrapped into Houdini Digital Assets (HDAs) and shared without code
- **Attributes as data**: Points, primitives, and details carry data (UVs, normals, velocities, custom values) that other nodes consume

---

## Houdini Network Types (Contexts)

| Context | Abbreviation | Purpose |
|---------|-------------|---------|
| Objects | OBJ | Scene hierarchy, object-level transforms (legacy) |
| Surface Operators | SOP | Geometry creation and modification |
| Lighting/Layout Operators | LOP (Solaris) | USD scene assembly, layout, lighting |
| Materials | MAT/VOP | Material and shader networks |
| Channel Operators | CHOP | Animation curves, motion data, audio |
| VEX Builder | VOP | Visual VEX node networks (alternative to wrangles) |
| Render Operators | ROP | Render output |
| Task Operators | TOP/PDG | Distributed processing, render farm management |
| Dynamic Operators | DOP | Physics simulations (Pyro, FLIP, RBD, Vellum, Cloth) |
| Compositing Operators | COP | 2D/3D GPU image compositing (Copernicus in H20.5+) |

---

## The Houdini Workspace

### Key Panes
- **Scene View** `Alt-1` — 3D viewport for interactive work; shelf tools and handles
- **Network View** `Alt-2` — manage nodes and networks
- **Parameter Pane** `Alt-3` — set values, add expressions, keyframe nodes
- **Tree View** `Alt-4` — hierarchical scene tree
- **Animation Editor** `Alt-6` — keyframes and animation curves; Table and Dope Sheet views
- **Material Palette** `Alt-7` — scene materials; select and assign
- **Geometry Spreadsheet** `Alt-8` — inspect attribute values (UVs, normals, custom data)
- **Render View** `Alt-9` — interactive Mantra rendering

### Radial Menus (Scene View)
- `X` — Snapping tools
- `C` — Main operations
- `V` — View options
- `N` — Network navigation

### Viewport Navigation
| Action | Hotkey |
|--------|--------|
| Tumble | `Spacebar + LMB` or `Alt + LMB` |
| Pan | `Spacebar + MMB` or `Alt + MMB` |
| Dolly | `Spacebar + RMB` or `Alt + RMB` |
| Frame All | `Spacebar + A` |
| Home Selected | `Spacebar + G` |
| Home Construction Plane | `Spacebar + H` |
| First Person Camera toggle | `M` |

### Network Navigation Hotkeys
| Action | Hotkey |
|--------|--------|
| Dive into network | `I` |
| Jump up to parent | `U` |
| Toggle Objects/Geometry | `F8` |
| Go back | `` ` `` |
| Set quickmark | `Ctrl + 1–5` |
| Return to quickmark | `1–5` |

---

## Nodes and Networks

### Node Flags
- **Display Flag** `[R]` — shown with hollow ring; sets which node's output appears in viewport
- **Render Flag** `[T]` — shown with solid circle; sets render output (Ctrl-click display flag to set separately)
- **Template Flag** `[E]` — grey display for reference/snapping
- **Freeze Flag** — caches at this node; upstream nodes are bypassed
- **Bypass Flag** `[B]` — ignore node when cooking

### Node Connections
| Action | Method |
|--------|--------|
| Connect | LMB-drag from output to input |
| Connect across multiple | J-drag across nodes |
| Insert node on wire | LMB-drag onto connector wire |
| Disconnect | Select node, jiggle |
| Cut wire | Y-drag across connector wire |
| Copy nodes | `Alt + LMB-drag` |
| Reference copy | `Alt + Shift + Ctrl + LMB-drag` |
| Add dot | `Alt + LMB` on wire |

### Tab Menu
Press `Tab` in any Network or Scene view to access all nodes. Begin typing to filter.

---

## Parameters, Channels, and Attributes

### Parameters vs. Attributes
- **Parameters** — values on nodes (sliders, checkboxes, fields). Called "attributes" in other apps.
- **Attributes** — data attached to geometry points, primitives, vertices, or details. Travel down the network chain.

### Keyframes and Channels
- `Alt + LMB` on parameter name or field → sets keyframe
- Animated parameters turn green in the Parameter pane
- Expression languages: **hScript** or **Python** (choose in pane menu top-right)
- `Ctrl-E` → opens expression editor

### Attribute Classes
| Class | Description |
|-------|-------------|
| Point | One value per point (`@P`, `@N`, `@Cd`, `@v`) |
| Primitive | One value per polygon/face |
| Vertex | One value per polygon vertex (e.g. per-corner UVs) |
| Detail | Single value for the whole geometry |

### Common Built-in Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `@P` | vector | Position |
| `@N` | vector | Normal |
| `@Cd` | vector | Color (RGB) |
| `@v` | vector | Velocity |
| `@uv` | vector | UV texture coordinates |
| `@id` | int | Unique per-point ID |
| `@pscale` | float | Point scale (for instancing) |
| `@age` | float | Particle age |
| `@life` | float | Particle lifespan |
| `@mass` | float | RBD mass |
| `@name` | string | Piece name (RBD, instancing) |

### Working with Attributes
- **Attribute Wrangle** — write VEX to create/modify attributes (the most powerful approach)
- **Attribute Randomize** — create and randomize attribute values interactively
- **Attribute Transfer** — copy attributes from one piece of geometry to another
- **Geometry Spreadsheet** — inspect all attribute values; essential for debugging

---

## Selecting Geometry

### Selection Modes
- **Object mode** — select entire objects
- **Geometry mode** — select components (points, edges, primitives)
- Selection mode affects which network the Network pane shows

### Component Selection Types
| Type | Hotkey |
|------|--------|
| Points | `F5` |
| Edges | `F6` |
| Primitives | `F7` |

### Selection Operations
- Grow selection: `[ ` / Shrink: `]`
- Convert selection type: `Shift + F5/F6/F7`

---

## Modeling Tools (SOPs)

### Core Modeling Nodes
| Node | Purpose |
|------|---------|
| `Box`, `Sphere`, `Grid`, `Tube`, `Torus` | Primitive generators |
| `PolyExtrude` | Extrude faces along normal or custom direction |
| `PolyBevel` | Bevel edges and corners |
| `EdgeLoop` | Insert edge loops |
| `Subdivide` | Catmull-Clark subdivision |
| `Fuse` | Weld nearby points |
| `Divide` | Triangulate or polygon cleanup |
| `Boolean` | Subtract, Union, or Intersect geometry |
| `Copy to Points` | Stamp geometry at each input point |
| `Scatter` | Scatter points on surface |
| `Normal` | Compute or set normals |
| `UVUnwrap` | Automatic UV unwrap |
| `UVLayout` | Pack UV islands into 0-1 space or UDIM tiles |
| `Merge` | Combine multiple geometry streams |
| `Transform` | Translate, rotate, scale |
| `Null` | Pass-through; used as output markers or reference points |

### Booleans
Use `Boolean` SOP for subtract, union, intersect. Handles complex topologies. Useful for destruction (better than Voronoi for realistic results).

### Copy to Points Workflow
1. Create source geometry
2. Create a `Scatter` SOP or any point cloud
3. Wire into `Copy to Points` — one copy per point
4. Use `@pscale`, `@orient`, `@N` attributes to control scale, rotation

---

## UVs and Textures

- **UVUnwrap SOP** — automatic UV projection; multiple projection types
- **UVLayout SOP** — packs UV islands; can target UDIM tile ranges (H21+)
- **UVEdit SOP** — interactive UV editing in viewport
- **UVFlatten SOP** — flatten with seam control
- **UV Flatten from Points SOP** (H21) — UV maps measuring distance/direction along surface
- Vertex attributes `@uv` for per-corner UVs, point attributes for per-point UVs

---

## LookDev: Shaders and Materials

### Solaris/Karma Workflow (H19.5+)
1. Build geometry in SOPs
2. Import into Solaris via **SOP Import LOP** or **Component Builder**
3. Assign materials via **Assign Material LOP**
4. Use **Karma Render Settings LOP** to configure render
5. Render via **Karma CPU** or **Karma XPU**

### MaterialX (Recommended for USD/Karma)
- **MtlX Standard Surface** — PBR shader; works in Karma CPU and XPU
- **MtlX OpenPBR Surface** (H21+) — new physically-based shader
- **MtlX Image VOP** — texture lookup with UDIM support
- **MtlX Worleynoise, Fractal** — procedural patterns

### Legacy Mantra Materials
- **Principled Shader** — PBR shader for Mantra
- Built in the `MAT` context using VOPs

---

## Solaris: Layout, Cameras, and Lights

### Key Concepts
- Solaris is Houdini's USD-based scene assembly, layout, and lighting context
- Objects imported from SOPs become USD prims
- Works natively with USD (.usd, .usda, .usdc) and supports FBX, glTF, SBSAR (H21+)

### Key LOPs
| LOP | Purpose |
|-----|---------|
| `SOP Import LOP` | Import SOP geometry as USD |
| `Reference LOP` | Reference external USD files |
| `Sublayer LOP` | Layer USD files |
| `Camera LOP` | USD camera definition |
| `Distant Light LOP` | Sun/directional light |
| `Dome Light LOP` | HDR environment light |
| `Rect Light LOP` | Rectangular area light |
| `Assign Material LOP` | Assign material to USD prims |
| `Karma Render Settings LOP` | Configure Karma render |
| `USD ROP` | Export USD to disk |

### Scene Graph
- All Solaris content stored as USD prims in a stage
- Navigate via **Scene Graph Tree** pane (shows hierarchy, visibility, materials)
- **Scene Graph Details** — inspect attribute values on selected prims

---

## Rendering

### Karma (H19+, recommended)
- **Karma CPU** — path tracer, supports full MaterialX
- **Karma XPU** (H20+) — GPU + CPU hybrid; supports most features, faster interactive
- Access via Solaris/LOPs only
- Render via **Karma Render Settings LOP** → **USD ROP**

### Mantra (Legacy)
- Houdini's original renderer
- Uses **VOP** shader networks in the `MAT` context
- Still supported but Karma is the strategic direction

### Rendering Workflow
1. Set up Solaris scene (import, lights, camera)
2. Create Karma Render Settings LOP
3. Connect to USD ROP
4. Press Render or enable IPR (Interactive Photorealistic Render)

---

## Time and Motion

### Playbar
- `Spacebar` — play/stop
- `Left/Right arrows` — step one frame
- `Shift + Left/Right` — step 10 frames
- Alt+click on parameter → set keyframe

### Animation Editor
- `Alt-6` — opens Animation Editor
- Shows curves for all animated parameters
- Switch between Curve, Table, and Dope Sheet views
- Ripple Tool (H21+) — move all keys before/after cursor

### CHOPs (Channel Operators)
- Used for procedural animation, motion data, audio sync
- `Channel SOP` — imports CHOP data back into geometry
- Useful for crowd simulation, motion retargeting

---

## Character Rigging (KineFX)

### KineFX Overview (H18+, expanded in H20/H21)
KineFX is the SOP-based character rigging and animation system. Everything happens in SOPs using geometry-based skeletons.

### Skeleton SOP
- Draw skeleton directly in viewport
- Each joint is a point with `name` attribute
- Primary axis: +X (H21 default), Secondary: +Z (H21 default)

### Core KineFX Workflow
1. **Skeleton SOP** — define bone hierarchy
2. **Capture Geometry SOP** (or Paint Capture Layer SOP) — bind skin
3. **Bone Deform SOP** — apply deformation
4. **APEX Scene Add Character SOP** — add to APEX scene for animation
5. **APEX Scene Animate SOP** — animate in viewport

### APEX (H20+)
- APEX is the procedural rigging system on top of KineFX
- **APEX Graph** — visual rig graph (renamed from APEX Edit Graph in H21)
- **APEX Script** — Python-like syntax for building rig graphs programmatically
- **Autorig Components** — pre-built rig components (limb, hand, foot, IK/FK, spline, etc.)
- **Autorig Builder** (H21) — interactively assemble rigs from components in viewport

---

## Dynamic Simulations (DOPs)

### Simulation Network
- Build DOPs in the **DOP network** inside a Geometry object
- Object → Add > DOP Network

### RBD (Rigid Body Dynamics)
1. Geometry → `RBD Material Fracture SOP` (Voronoi) or `Boolean` fracture
2. Create `DOP Network` → shelf: Rigid Bodies → RBD Solver
3. Key constraints: `Glue`, `Cone Twist`, `Pin`
4. **Bullet Solver** — fast, stable; H21 is 20-30% more memory efficient

### Pyro (Smoke and Fire)
- **SOP Pyro** (H18.5+) — shelf tools drive a `Pyro Solver SOP`; no DOP network needed
- **DOP Pyro** — traditional DOP-based simulation with full microsolvers
- Key attributes: `density`, `temperature`, `fuel`, `heat`

### FLIP Fluids
1. `FLIP Tank` or `FLIP Object` SOP
2. `DOP Network` with `FLIP Solver`
3. `Particle Fluid Surface SOP` to mesh the particles
4. Cache with `File SOP` or `File Cache SOP`

### Vellum (H16.5+)
- Unified solver for cloth, grains, hair, soft bodies
- Works in SOPs via **Vellum Solver SOP** (SOP-level) or DOP network
- Key constraints: `Cloth`, `String`, `Grain`, `Strut`, `Stitch`

### Simulation Caching
- `File Cache SOP` — write simulation to disk; re-read without resimulating
- Essential for multi-pass workflows and final renders

---

## Cloud FX and Volumes

### Volume Creation
- `Volume SOP` — create empty volume
- `VDB from Polygons SOP` — convert mesh to VDB
- `OpenVDB` is the standard format (`.vdb` files)

### Pyro → Volume
- Pyro simulations output as volumes (`density`, `vel`, `temperature`)
- Render directly in Karma or Mantra using volume shaders

### Volume Visualization SOP (H21)
- Now generates `volvis` dictionary attribute (changed from cloud format)

---

## Terrain and Heightfields

### Heightfield Context
- All heightfield operations use **Heightfield** SOPs
- Data stored as 2D volumes at resolution × resolution

### Core Heightfield Nodes
| Node | Purpose |
|------|---------|
| `HeightField SOP` | Create base terrain |
| `HeightField Noise SOP` | Add noise layers |
| `HeightField Erode SOP` | Hydraulic/thermal erosion (redesigned in H21) |
| `HeightField Scatter SOP` | Scatter objects on terrain surface |
| `HeightField Mask by Feature SOP` | Create masks by slope, height, curvature |
| `HeightField Output SOP` | Export for game engines |

---

## Expressions and Scripting

### Expression Languages
- **hScript** — Houdini's expression language; `$F` = current frame, `$T` = current time
- **Python** — full Python 3 inside Houdini; `hou` module is the API
- **VEX** — C-like high-performance language for geometry/shading; runs in Wrangles and VOPs

### VEX Quick Reference
```vex
// Point Wrangle — runs once per point
float height = sin(@P.x * 0.5 + @Time) * chf("amplitude");
@P.y += height;

// Access attributes
float val = f@myattr;         // float
vector col = v@Cd;            // vector
int idx = i@myint;            // int
string s = s@mystring;        // string

// Set attributes
@Cd = set(1, 0, 0);           // red
@pscale = rand(@ptnum);       // random scale per point
```

### Channel Functions (VEX/hScript)
| Function | Purpose |
|----------|---------|
| `chf("name")` | Float channel parameter |
| `chi("name")` | Integer channel parameter |
| `chv("name")` | Vector channel parameter |
| `chs("name")` | String channel parameter |
| `chramp("name", t)` | Ramp parameter lookup |

### Python (hou module)
```python
import hou

node = hou.pwd()               # current node
geo = node.geometry()          # SOP geometry
pts = geo.points()             # all points
prims = geo.prims()            # all primitives

# Read attribute
val = pt.attribValue("myattr")

# Create attribute
geo.addAttrib(hou.attribType.Point, "myattr", 0.0)
```

---

## Houdini Digital Assets (HDAs)

### What They Are
- Nodes whose internals are hidden and exposed via a custom parameter interface
- Can contain any network type (SOP, DOP, LOP, etc.)
- Saved as `.hda` or `.hdanc` files
- Shareable: load in Houdini, or in Maya/UE/Unity/3DS Max via **Houdini Engine**

### Creating an HDA
1. Select the nodes to package
2. Right-click → Collapse into subnet
3. Right-click subnet → Create Digital Asset
4. Define parameter interface in Type Properties
5. Save `.hda` file

### HDA Best Practices
- **Promote** key parameters to the top-level interface
- Use **Ordered Menu** parameters for preset choices
- Use **Folder** tabs to organize complex parameter sets
- Add **Python** callbacks for dynamic parameter behavior

---

## Tasks and PDG (TOPs)

### What PDG Does
- **Procedural Dependency Graph** for distributing tasks across machines
- Each node processes **work items** in parallel
- Used for: wedging (variations), rendering farm management, asset pipeline automation, city generation

### Core Pattern
1. Create a `TOP Network`
2. Use **Generic Generator** or **Geometry Import** to create work items
3. **Wedge** — vary parameter values across work items
4. **ROP Fetch** — trigger renders per work item
5. **Work Item Expand** — fan out from file lists

---

## File Management

### Scene Files
- `.hip` / `.hipnc` — Houdini scene files (`.hipnc` = no-commercial)
- `$HIP` — directory of the current `.hip` file
- `$HOME` — user home directory
- `$JOB` — project root (set in preferences)

### Caching
- `File Cache SOP` — explicit cache to disk; read/write control
- `File SOP` — read geometry from disk
- `Geometry ROP` — write geometry sequence to disk

### USD Export
- `USD ROP` — export full Solaris stage to USD
- `Export as Component LOP` — export object-level USD

---

## SideFX Labs (Free Add-On)

SideFX Labs is a freely available toolset extending Houdini with game-dev and pipeline tools.  
Install via: SideFX > Labs in the shelf, or download from SideFX.com.

Key tool categories:
- **Destruction** — enhanced fracturing tools
- **Gamedev** — LOD generators, UV tools, mesh baking
- **Maps Baker** — texture baking workflow
- **Instant Meshes** — quad-remeshing
- **OSM Import** — OpenStreetMap city generation
- **Heightfield tools** — additional terrain tools

---

## Houdini Engine

Run Houdini proceduralism inside other DCC apps:
- **Unreal Engine** — PCG Graph integration (H21+), real-time HDA parameter editing
- **Unity** — Unity 6.0/6.1 support (H21+)
- **Maya** — Maya 2026 support (H21+)
- **3DS Max** — 3DS Max 2026 support (H21+)

Houdini Engine exposes HDA parameters as native UI in the host application. Simulations and geometry cook procedurally from the host.

---

## Film, TV, and GameDev Pipelines

### Film/TV Pipeline Concepts
- **USD** is the standard interchange; Solaris is Houdini's USD authoring environment
- Shot-based workflow: SOP (FX) → USD export → Solaris (lighting/render)
- **PDG/TOPs** for distributing renders across farm
- VEX and Python for TD automation

### GameDev Pipeline Concepts
- HDAs are the primary way to ship procedural content to game engines
- **SideFX Labs** tools optimize for game output (LODs, baked maps)
- Heightfields export directly to Unreal terrain system
- RBD simulations can bake to animated geometry for export

---

## Version Comparison Chart (from Foundations Book H19.5)

| Product | Description |
|---------|-------------|
| **Houdini Apprentice** | Free; watermarks, render size limit; all features |
| **Houdini Indie** | ~$269/yr; removes watermarks; 4K render; <$100K revenue |
| **Houdini Core** | Commercial; modeling, animation, rendering; no dynamics FX |
| **Houdini FX** | Full commercial license; all simulations included |
| **Houdini Education** | Institutional license |

> **Note as of H21:** Karma XPU is available in all FX/Indie/Apprentice editions. Copernicus Pyro COPs require FX/Apprentice/Indie/Education (not Core).
