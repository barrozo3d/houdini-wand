# -*- coding: utf-8 -*-
import re, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tutorials")

def update_file(path, frontmatter_updates, structured_notes, related_entries):
    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    for key, value in frontmatter_updates.items():
        content = re.sub(rf'^{key}:.*$', f'{key}: {value}', content, flags=re.MULTILINE)
    new_block = structured_notes + "\n\n---\n\n## Related Tutorials\n" + related_entries + "\n"
    content = re.sub(r'### Core Technique\n.*', new_block, content, flags=re.DOTALL)
    with open(path, 'w', encoding='utf-8-sig', newline='\r\n') as f:
        f.write(content)
    print(f"  OK: {os.path.basename(path)}")

EXTRACTIONS_B = {

    # ── Renascence 1.0 — Module II ────────────────────────────

    "module-ii-week-01-01-basic-bullet-sim-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[dop, sop, rbd, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Introducing Rigid Body Dynamics from a bare single box, then escalating to Voronoi/Boolean fracture and a constraint network that holds pieces together until impact breaks the glue.

### Summary
Starts bare-bones: a single box, raised and rotated, then Tab -> "RBD Bullet Solver" auto-creates two nodes (RBD Configure + DOP Import) and an immediate working simulation. Escalates to Voronoi fracture: a Voronoi Fracture SOP with a point cloud controlling chunk size, then a Boolean fracture pass for sharper edges, followed by the RBD Bullet Solver on the fractured geometry. Introduces constraints for holding pieces together before shattering: an Assemble SOP adds a `name` attribute per piece, feeding a Voronoi Fracture Configure Object / Constraint Network. Explains the constraint network geometry: each constraint is a line segment between two piece centers, read by the Constraint Network DOP to link pieces. Glue constraints hold until impact force exceeds the strength threshold.

### Key Steps
1. [Bare box test] Raise/rotate a box; Tab -> "RBD Bullet Solver" shelf tool auto-builds RBD Configure + DOP Import
2. [`Voronoi Fracture SOP`] Fracture geometry using a point cloud to control chunk size
3. [`Boolean fracture`] Add a Boolean pass for sharper fracture edges
4. [`Assemble SOP`] Add a `name` attribute per piece, required for constraints
5. [`Constraint Network DOP`] Build a constraint network from line-segment geometry connecting piece centers
6. [Glue constraints] Set break strength threshold so pieces hold until sufficient impact force

### Houdini Nodes / VEX / Settings
- RBD Bullet Solver (shelf tool) — auto-creates RBD Configure + DOP Import for a quick working sim
- `Voronoi Fracture SOP` — fractures geometry based on a guide point cloud
- `Assemble SOP` — assigns a unique `name` attribute per piece, required by constraint nodes
- `Constraint Network` DOP — reads line-segment geometry (one line per constrained pair) to link pieces with glue/hard constraints

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)""",
        'related': """- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — applies these same RBD/Bullet fundamentals to bridge geometry
- [Importing the Geometry (Module II W02)](module-ii-week-02-01-importing-the-geometry-v1-1080p.md) — the following week's multi-object destruction
- [RBD Configure Deep Dive](week-01-11-rbd-configure-v1-1080p.md) — detailed look at collision proxy settings on RBD Configure""",
    },

    "module-ii-week-02-01-importing-the-geometry-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[dop, sop, rbd, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Importing a multi-LOD Brooklyn building Alembic asset for a multi-object destruction shot, with an LOD strategy that simulates at low resolution and renders at high resolution.

### Summary
Imports a compressed Alembic asset with multiple LODs; extracts it and selects LOD2 as the balance between polygon detail and simulation speed. Creates a geometry node named "building," adds an Alembic SOP, and scales the import to 0.01 since the building was modelled at real-world scale in meters and needs shrinking for the Houdini scene. The week's concept is a reverse-gravity / attractor-beam effect, where building chunks rise upward in an organized way suggesting anti-gravity or an energy beam. Establishes the LOD strategy: simulate with LOD2/LOD3 (fewer polygons) and render with LOD0/LOD1 via a post-sim copy-back step.

### Key Steps
1. [Import Alembic] Extract the compressed multi-LOD Brooklyn building asset
2. [`Alembic SOP`] Create a "building" geometry node and import LOD2 for simulation
3. [`Transform SOP`] Scale the import by 0.01 to correct real-world-meter to Houdini-unit mismatch
4. [Reverse gravity setup] Configure the RBD sim so chunks rise upward in an organized pattern
5. [LOD strategy] Plan to simulate on LOD2/LOD3 and swap to LOD0/LOD1 for the final render pass

### Houdini Nodes / VEX / Settings
- `Alembic SOP` — imports the multi-LOD building asset
- `Transform SOP` — corrects scale mismatch (real-world meters vs. Houdini scene units) via a 0.01 multiplier
- LOD strategy — simulate at low resolution, swap to high resolution for render via a post-sim copy-back

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)""",
        'related': """- [Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — the preceding week's RBD/constraint fundamentals
- [Splitting by Material](module-ii-week-03-01-splitting-by-material-v1-1080p.md) — the following week's multi-material fracture
- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — a parallel multi-piece RBD destruction setup""",
    },

    "module-ii-week-03-01-splitting-by-material-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[dop, sop, rbd, attributes, intermediate, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Splitting destruction geometry by material group and applying the RBD Material Fracture SOP, which generates characteristic shard shapes per material (glass, wood, concrete) in a single node.

### Summary
Continues from the Week 2 building Alembic, resaving the project under a new name. A key setup step is the Connectivity SOP set to "primitives" mode to identify separate geometry pieces, followed by a Convert SOP to move from PolySoup to standard polygons. Geometry is split by material groups so different pieces receive different fracture treatment: the RBD Material Fracture SOP (an H18.5+ node) handles glass, wood and concrete fracture in one node, with each material type generating characteristic shard shapes — glass produces many small sharp fragments, wood produces long splinters along the grain, and concrete produces chunky irregular blocks. The `name` attribute remains critical, since each piece needs a unique name for the constraint network.

### Key Steps
1. [`Connectivity SOP`] Set to "primitives" mode to identify separate geometry pieces
2. [`Convert SOP`] Convert from PolySoup to standard polygons
3. [Material groups] Split geometry into glass, wood and concrete groups
4. [`RBD Material Fracture SOP`] Fracture each material group with its characteristic shard pattern
5. [`Assemble SOP`] Re-assign unique `name` attributes after fracture for the constraint network

### Houdini Nodes / VEX / Settings
- `Connectivity SOP` (primitives mode) — groups geometry by connected-piece membership before material splitting
- `RBD Material Fracture SOP` (H18.5+) — single node producing material-appropriate fracture patterns (glass/wood/concrete)
- `name` attribute — required uniquely per piece for the downstream constraint network

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)""",
        'related': """- [Importing the Geometry (Module II W02)](module-ii-week-02-01-importing-the-geometry-v1-1080p.md) — the preceding week establishing the building asset
- [Concrete + Metal Destruction](module-ii-week-04-01-importing-the-geometry-v1-1080p.md) — the following week's skyscraper collapse
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — a later course applying RBD Material Fracture to glass and wood""",
    },

    "module-ii-week-04-01-importing-the-geometry-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[dop, sop, rbd, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Importing a multi-LOD skyscraper Alembic for a realistic downward-collapse simulation, and introducing the "active attribute" pipeline that activates pieces progressively as a wave propagates from the impact point.

### Summary
Uses a different skyscraper Alembic asset with multiple LODs available, selecting LOD3 for simulation. The import workflow mirrors Week 2: Alembic SOP -> Transform at 0.01 scale -> visual check. The week's concept is a realistic downward collapse where the building folds and pancakes floor by floor, with separate simulation of concrete slabs, steel rebar/frame, and glass panes. Sets up the "active attribute" pipeline: pieces start inactive (kinematic) and become active (simulating) based on a wave propagating downward from the impact point. This lesson covers only the geometry import and scale step; the active-attribute technique itself is covered in the Renascence 2.0 gap-filler lesson 09.

### Key Steps
1. [Import Alembic] Select LOD3 of the skyscraper asset for simulation-resolution geometry
2. [`Alembic SOP`] Import; `Transform SOP` scale to 0.01 to match Houdini scene units
3. [Material separation] Plan separate simulation streams for concrete slabs, steel frame and glass panes
4. [Active-attribute pipeline] Establish that pieces will start kinematic (`active=0`) and switch to simulating (`active=1`) as a wave propagates from the impact point — implemented in the linked gap-filler lesson

### Houdini Nodes / VEX / Settings
- `Alembic SOP` + `Transform SOP` (0.01 scale) — same import pattern as Module II Week 2
- Active attribute pipeline — pieces toggle from kinematic to simulating based on distance/wave from impact; full implementation deferred to a gap-filler lesson

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module II)""",
        'related': """- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — the gap-filler lesson implementing the active-attribute technique referenced here
- [Splitting by Material](module-ii-week-03-01-splitting-by-material-v1-1080p.md) — the preceding multi-material fracture week
- [City Ground Destruction Intro](module-i-week-01-01-intro-v1-1080p.md) — a later course's parallel staged-destruction setup""",
    },

    # ── Renascence 2.0 — Module I intros ──────────────────────

    "module-i-week-01-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, pyro, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Overview of a city ground explosion shot using Boolean fracture for varied chunk shapes and a three-layer debris/pyro sourcing hierarchy all driven by the same RBD simulation's velocity and piece-size attributes.

### Summary
Covers a city ground explosion with rock/rubble/paving erupting upward. The RBD focus is a Boolean fracture system for high-quality, varied chunk shapes — big and small pieces with interesting silhouettes, rather than uniform Voronoi output. Constraints are set up minimally, mainly to hold the initial state rather than to drive complex breaking behaviour. A debris-sourcing pipeline uses the main RBD sim's velocity and piece-size attributes to source a secondary debris particle layer, which in turn sources a third pyro layer — a three-layer hierarchy entirely driven by the same underlying simulation. The render pipeline uses Solaris/Karma with Megascans materials for rock/concrete.

### Key Steps
1. [`Boolean fracture`] Generate varied, high-quality chunk shapes for the ground explosion
2. [Minimal constraints] Hold initial geometry state without complex breaking logic
3. [`RBD Solver`] Run the primary destruction simulation, exporting velocity and piece-size attributes
4. [`POP Network`] Source a secondary debris particle layer from the RBD sim's attributes
5. [`Pyro Solver`] Source a third pyro layer from the debris particle layer
6. [Render] Apply Megascans rock/concrete materials; render in Solaris/Karma

### Houdini Nodes / VEX / Settings
- Boolean fracture — preferred over Voronoi here for more varied, art-directable chunk silhouettes
- Three-layer sourcing hierarchy — RBD velocity/size attributes -> debris POPs -> pyro source, all chained from one simulation
- Solaris/Karma + Megascans — render pipeline for rock/concrete surfacing

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module I)""",
        'related': """- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — the staged-activation gap-filler for this same module
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the following week's multi-material destruction
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — another debris-to-pyro sourcing hierarchy""",
    },

    "module-i-week-02-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, attributes, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
A bus stop destruction shot combining three material types — steel, glass and wood — using RBD Material Fracture together with plasticity-driven soft constraints so metal permanently deforms rather than springing back.

### Summary
Covers a bus stop with mixed-material destruction: a steel frame (metal), glass panels and wood planks. The new technique highlighted is the RBD Material Fracture SOP for both glass and wood fracture patterns. The key technique for metal is "plasticity" (new around H18) applied to soft constraints — metal holds its bent/deformed shape after impact instead of springing back, with constraints weakening and permanently deforming rather than breaking cleanly, producing realistic crushed-metal behaviour. Post-sim, Point Deform applies the low-res proxy simulation to the high-res render mesh. Also mentions the RBD Disconnected Faces fix for glass shards that separate at impact.

### Key Steps
1. [`RBD Material Fracture`] Fracture glass and wood with material-appropriate patterns
2. [Plasticity] Apply plasticity to metal soft constraints so it deforms permanently under impact
3. [`RBD Solver`] Run the combined multi-material simulation
4. [`Point Deform`] Apply the low-res proxy sim result to the high-res render mesh
5. [`RBD Disconnected Faces`] Fix glass shards that separate incorrectly at impact

### Houdini Nodes / VEX / Settings
- `RBD Material Fracture SOP` — generates glass and wood fracture patterns appropriate to each material
- Plasticity — soft-constraint property letting metal permanently bend/deform rather than spring back or break
- `Point Deform` — transfers proxy sim transforms onto high-res render geometry
- `RBD Disconnected Faces` — reconnects glass faces that float free after fracture/deform

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I)""",
        'related': """- [Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — the gap-filler lesson detailing the Point Deform step used here
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — the gap-filler detailing the disconnected-faces fix mentioned here
- [City Ground Destruction Intro](module-i-week-01-01-intro-v1-1080p.md) — the preceding week's Boolean fracture setup""",
    },

    "module-i-week-03-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, attributes, animation, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Organizing a complex car model's geometry for a car-crash simulation, separating pieces that need simulation from those kept rigid or pre-animated for performance.

### Summary
Overview of Week 3 (weeks 3 and 4 form one large project): the car slides in sideways and impacts a post, with metal bending and glass shattering across the two weeks. Week 3's focus is geometry organization — the car model is complex with many named parts, a detailed chassis, wheels and windows — and selecting the right pieces for simulation versus keeping others rigid or kinematic is critical for performance. Efficiency work includes simplifying/merging small non-simulating parts and isolating the bending panels. Wheels spin during the slide (pre-animated in SOPs), but that spin doesn't need to be simulated — wheels are kept kinematic and only become active on impact. The week outputs a cached simulation ready for Week 4's glass fracture pass.

### Key Steps
1. [Geometry audit] Inspect the complex car model's named parts, chassis, wheels and windows
2. [Simplify/merge] Combine small non-simulating parts to reduce piece count for performance
3. [Isolate bending panels] Separate body panels that need plasticity-driven deformation
4. [Pre-animate wheels] Animate wheel spin in SOPs; keep wheels kinematic until impact triggers activation
5. [`RBD Solver`] Run and cache the Week 3 simulation as the basis for Week 4's glass pass

### Houdini Nodes / VEX / Settings
- Geometry organization pass — merging/simplifying non-simulating parts is a performance-critical step before any RBD setup
- Kinematic-to-active wheel handling — pre-animated spin stays kinematic until an impact-triggered activation switches it to simulating
- Cached simulation hand-off — Week 3's cache feeds directly into Week 4's glass fracture pass

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I)""",
        'related': """- [Car Glass Fracture](module-i-week-04-01-intro-v1-1080p.md) — the direct continuation of this car-crash project
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the preceding week's multi-material destruction
- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — the staged-activation technique relevant to the wheel impact trigger""",
    },

    "module-i-week-04-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, rendering, karma, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Completing the car crash with two distinct glass fracture treatments — dense fine Voronoi with plasticity for laminated windscreen glass, and small-piece Voronoi with low break threshold for tempered side-window glass — followed by a final Solaris/Karma render.

### Summary
Two types of car glass require different fracture treatment. The windscreen uses laminated glass (with a PVB plastic inner layer): it fractures into thousands of small blocks that stay together and bend slightly like plastic rather than scattering as shards, achieved with dense fine Voronoi fracture, soft glue constraints and slight plasticity. Side windows use tempered glass: it shatters into many small pebble-shaped fragments that scatter completely, achieved with Voronoi using small pieces and a low break threshold. Both glass simulations use the Week 3 metal sim cache as the collision source. The final week delivers a Solaris/Karma render of the full car crash with all layers composited.

### Key Steps
1. [Windscreen] Dense fine `Voronoi Fracture` + soft glue constraints + slight plasticity for laminated, plastic-like cracking
2. [Side windows] `Voronoi Fracture` with small pieces + low break threshold for tempered, scattering glass
3. [Collision source] Use the cached Week 3 metal RBD sim as the collider for both glass sims
4. [`RBD Solver`] Run both glass simulations against the cached metal collision geometry
5. [Render] Composite metal + glass layers; render the full crash in Solaris/Karma

### Houdini Nodes / VEX / Settings
- Laminated glass technique — dense fine Voronoi + soft glue + plasticity, producing cohesive plastic-like deformation
- Tempered glass technique — Voronoi with small pieces + low break threshold, producing full scatter
- Cached collision hand-off — Week 3's metal sim cache is reused directly as the Week 4 glass collider
- Solaris/Karma — final render engine for the composited crash

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I)""",
        'related': """- [Car Crash: Metal Bending Geometry Organization](module-i-week-03-01-intro-v1-1080p.md) — the preceding week whose cache feeds this glass pass
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — another multi-material destruction using RBD Material Fracture
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — a relevant glass post-sim fix""",
    },

    # ── Renascence 2.0 — Module I gap-fillers ─────────────────

    "module-i-week-01-09-setting-the-active-attribute-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, attributes, vex, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Using the `active` integer attribute to control when RBD pieces become live in the simulation, enabling staged destruction that propagates outward from an impact point or follows a keyframed activation sequence.

### Summary
Explains the standard H19+ RBD workflow node chain, where every RBD node has a pink primary input plus constraint and proxy inputs: RBD Configure -> RBD Material Fracture -> RBD Constraint Properties -> RBD Solver. The `active` integer attribute (0 = kinematic/frozen, 1 = simulating) is set per primitive. Two common methods are shown: keyframe-animating `active` inside a SOP Solver within the DOP network, or setting `active` based on distance from an impact point so pieces near the blast go active first and outer pieces follow. The VEX pattern is `i@active = (@P.y < ch('threshold')) ? 1 : 0;` or a distance-based variant. Critically, `active` must be set at the SOP level before the DOP network, or inside a SOP Solver inside DOPs for animated activation.

### Key Steps
1. [Node chain] Establish RBD Configure -> RBD Material Fracture -> RBD Constraint Properties -> RBD Solver
2. [`Attribute Wrangle`] Set `i@active` per primitive: `i@active = (@P.y < ch('threshold')) ? 1 : 0;`
3. [Distance-based activation] Drive `active` by distance from an impact point for outward-propagating destruction
4. [`SOP Solver` (inside DOPs)] Keyframe-animate `active` over time for scripted activation sequences
5. [Verify] Confirm pieces stay kinematic (active=0) until their trigger condition, then simulate (active=1)

### Houdini Nodes / VEX / Settings
- `active` attribute (int, 0/1) — per-primitive switch between kinematic and simulating state
- VEX pattern: `i@active = (@P.y < ch('threshold')) ? 1 : 0;` — position/distance-based activation
- `SOP Solver` (inside DOPs) — required for animating `active` over time rather than a single static condition
- RBD node chain — RBD Configure / RBD Material Fracture / RBD Constraint Properties / RBD Solver, each with pink primary + constraint + proxy inputs

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)""",
        'related': """- [City Ground Destruction Intro](module-i-week-01-01-intro-v1-1080p.md) — the project this staged-activation technique supports
- [Concrete + Metal Destruction](module-ii-week-04-01-importing-the-geometry-v1-1080p.md) — references this exact technique for skyscraper collapse
- [Car Crash Geometry Organization](module-i-week-03-01-intro-v1-1080p.md) — the wheel impact-trigger activation relevant here""",
    },

    "module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, procedural, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Establishing the post-simulation network for applying the proxy RBD result back to high-resolution render geometry, using named Nulls and Object Merge to assemble a stable multi-input setup.

### Summary
Adds a Null SOP after the DOP Import cache (named e.g. "OUT_SIM") to cap the simulation stream. A Split SOP (or separate Blast) separates top vs. bottom pieces for independent treatment. A new geometry node named "post_sim" is created, using Object Merge SOPs to pull in: the cached RBD fractured geometry, the original un-fractured metal mesh (pre-fracture geo for deformation), the glass mesh, and the collider geometry. This multi-input post_sim SOP is where the RBD Deform Pieces node operates in the following lesson. The key habit emphasized is always inserting named Nulls as network outputs to keep Object Merge paths stable.

### Key Steps
1. [`Null SOP`] Cap the DOP Import cache output with a named Null (e.g. "OUT_SIM")
2. [`Split SOP` / `Blast SOP`] Separate top vs. bottom pieces for independent treatment
3. [New geometry node] Create "post_sim" as the destination network
4. [`Object Merge`] Pull in cached RBD geo, pre-fracture metal mesh, glass mesh and collider geometry
5. [Naming convention] Use named Nulls throughout so Object Merge paths remain stable across edits

### Houdini Nodes / VEX / Settings
- `Null SOP` — named network output caps, used as stable Object Merge targets
- `Split SOP` / `Blast SOP` — separates geometry by region (top/bottom) for independent post-sim treatment
- `Object Merge` — multi-input pattern pulling cached sim, pre-fracture mesh, glass mesh and collider into one post_sim network

### Difficulty
Intermediate

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)""",
        'related': """- [Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — the following lesson that operates on this post_sim setup
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the week this post-sim pipeline supports
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — the subsequent post-sim cleanup lesson""",
    },

    "module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, attributes, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Using the RBD Deform Pieces SOP to apply a low-poly proxy simulation's per-piece rigid transforms onto high-resolution render geometry, matched by the `name` attribute.

### Summary
Before this node existed, the old method used a for-each loop capturing each piece's transform and deforming the matching hi-res piece individually — complex and slow. The RBD Deform Pieces workflow instead takes the high-res render geometry on input 0 and the fractured/simulated proxy geometry stream on input 1, matching pieces by their shared `name` attribute and applying per-piece rigid transforms directly. The constraints input (input 2) is not required unless using constraint-driven deformation. The high-res mesh needs additional polygon density to deform smoothly, so a Subdivide is added before the RBD Deform Pieces node. The result is that bending bus-stop metal follows the proxy simulation perfectly at full render resolution.

### Key Steps
1. [`Subdivide SOP`] Increase polygon density on the high-res mesh for smooth deformation
2. [`RBD Deform Pieces`] Input 0: high-res render mesh; Input 1: simulated proxy geometry stream
3. [Name matching] Confirm both inputs share the `name` attribute used for piece correspondence
4. [Optional] Connect constraints input only if constraint-driven deformation is needed
5. [Verify] Confirm high-res geometry now follows the proxy sim's per-piece transforms exactly

### Houdini Nodes / VEX / Settings
- `RBD Deform Pieces SOP` (H19+) — matches pieces by `name` and applies per-piece rigid transforms from a proxy sim onto high-res geometry
- `Subdivide SOP` — adds the polygon density required for the high-res mesh to deform smoothly
- Old for-each-loop method — superseded by this node; useful context for why RBD Deform Pieces is preferred

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)""",
        'related': """- [Starting the Post-Sim Setup](module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1.md) — the preceding setup this lesson operates within
- [Fixing Post-Sim: RBD Disconnected Faces](module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p.md) — the following cleanup step for artifacts this deform pass can introduce
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the week this technique is built for""",
    },

    "module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, sop, rbd, rendering, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Fixing the RBD Disconnected Faces artifact, where faces lose their piece-level transform after deformation and float free, by reconnecting them to their nearest named piece and splitting the output for independent shading.

### Summary
After glass fracture and deformation, some faces become disconnected from their pieces — they float in space because they lost their piece-level transform. The RBD Disconnected Faces SOP reconnects orphaned faces back to their nearest named piece. Workflow: after RBD Deform Pieces, add RBD Disconnected Faces with "fix" mode enabled. The post-sim output is then split by name groups: a Blast SOP with `name == 'big_metal'` isolates and deletes the proxy geometry, and a separate Blast with `name == 'glass'` splits the glass stream for independent shader assignment. A quick visualization shader — Principled Shader with a glass preset (refraction IOR ~1.5) — is applied only to the glass group for a visual check before final render.

### Key Steps
1. [`RBD Disconnected Faces`] Add after RBD Deform Pieces; enable "fix" mode to reconnect floating faces
2. [`Blast SOP`] Isolate and delete `name == 'big_metal'` proxy geometry
3. [`Blast SOP`] Split out `name == 'glass'` geometry for independent shading
4. [`Principled Shader`] Apply a glass preset (refraction IOR ~1.5) to the glass group for a quick visual check
5. [Verify] Confirm no floating disconnected faces remain before final render

### Houdini Nodes / VEX / Settings
- `RBD Disconnected Faces SOP` — reconnects orphaned faces to their nearest named piece after deformation; "fix" mode performs the repair
- `Blast SOP` (by `name` group) — standard pattern for splitting post-sim geometry by piece-name for independent shading
- `Principled Shader` (glass preset, IOR ~1.5) — used here purely as a fast visual-check shader

### Difficulty
Advanced

### Houdini Version
Houdini 19 (Renascence 2.0 — Module I, gap-filler)""",
        'related': """- [Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — the preceding deform step that can introduce this artifact
- [Car Glass Fracture](module-i-week-04-01-intro-v1-1080p.md) — another glass-heavy shot where this fix is relevant
- [Bus Stop Destruction Intro](module-i-week-02-01-intro-v1-1080p.md) — the week this fix supports""",
    },

}

if __name__ == "__main__":
    for slug, data in EXTRACTIONS_B.items():
        path = os.path.join(BASE, slug + ".md")
        if not os.path.exists(path):
            print(f"  MISSING: {path}")
            continue
        update_file(path, data['fm'], data['notes'], data['related'])
    print(f"\nDone: {len(EXTRACTIONS_B)} files processed.")
