# -*- coding: utf-8 -*-
import re, os

BASE = r"C:\Users\KABUM\.claude\skills\houdini-wand\tutorials"

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

EXTRACTIONS_A = {

    # ── Film FX Season 1 ──────────────────────────────────────────

    "00-weeks-overview-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[sop, dop, pyro, particles, rbd, rendering, mantra, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
A 2.5-minute curriculum overview for the Houdini Film FX Program Season 1, framing the course's progression from modelling and shading through particles, pyro, RBD destruction and FLIP fluids.

### Summary
Walks through the course week-by-week: Week 1 covers Houdini versions/hardware, the interface, modelling Thor's hammer, shaders and a Mantra render. Week 2 covers scene setup, CHOP-based animation of the hammer, ray effects, WOPS for geometry and ramps. Week 3 introduces particles and POPs for a lightning/ray storm. Later weeks cover pyro (smoke/fire), RBD destruction, FLIP fluids and final compositing. Establishes that the course requires Houdini FX (not Core) on roughly the H18 toolset.

### Key Steps
1. [Week 1] Modelling Thor's hammer, shading, Mantra render basics
2. [Week 2] CHOP-driven animation, WOPS geometry workflows, ramps
3. [Week 3] POPs for a lightning/ray storm effect
4. [Later weeks] Pyro smoke/fire, RBD destruction, FLIP fluids
5. [Final weeks] Compositing the rendered passes

### Houdini Nodes / VEX / Settings
- Houdini FX license — required for the simulation work covered later in the course (Core lacks RBD/pyro/fluids/particles)
- Mantra — the renderer used throughout this season

### Difficulty
Beginner

### Houdini Version
Houdini 18 (Film FX Season 1)""",
        'related': """- [Houdini Versions Explained](03-houdini-versions-v1-1080p.md) — licensing context referenced in this overview
- [Introducing the SOP Solver](51-introducing-the-sop-solver-v1-1080p.md) — first hands-on particle lesson from this season
- [Starting the Smoke Vortex](76-starting-the-smoke-vortex-v1-1080p.md) — pyro lesson from the later weeks mentioned here""",
    },

    "03-houdini-versions-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[beginner, procedural]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
A 3-minute explainer of Houdini's licensing tiers and why the Film FX course requires Houdini FX specifically.

### Summary
Houdini Core includes all SOP/VOP/CHOP modelling tools but excludes every simulation solver (no fluids, RBD, particles, crowds or pyro). Houdini FX is the complete commercial package with all simulation solvers included. Houdini Indie offers the same toolset as FX but with a revenue cap for small studios/freelancers. Houdini Learning/Apprentice is free and non-commercial with watermarked renders. The recommendation for this course is FX, since all later simulation lessons depend on it.

### Key Steps
1. [Core] All modelling/SOP/VOP/CHOP tools, no DOP simulation solvers
2. [FX] Full commercial license, all solvers included
3. [Indie] FX toolset under a commercial revenue cap
4. [Learning/Apprentice] Free, non-commercial, watermarked output
5. [Recommendation] Use FX for this course since destruction/fluids/particles are required later

### Houdini Nodes / VEX / Settings
- License tiers — Core, FX, Indie, Learning/Apprentice; the simulation toolset (DOPs) is gated behind FX/Indie

### Difficulty
Beginner

### Houdini Version
Houdini 18 (licensing comparison remains accurate through current versions)""",
        'related': """- [Weeks Overview](00-weeks-overview-v1-1080p.md) — the course this licensing choice supports
- [Introducing the SOP Solver](51-introducing-the-sop-solver-v1-1080p.md) — first simulation-adjacent lesson requiring FX
- [Your First Houdini Project](module-i-week-01-01-your-first-houdini-project-v1-1080p.md) — later course also requiring FX""",
    },

    "51-introducing-the-sop-solver-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[sop, dop, vex, particles, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Building a manual particle solver entirely inside a SOP Solver to teach the underlying integration mechanics before switching to the dedicated POP system.

### Summary
Creates a geometry network with a Scatter SOP (100 points) as the particle source. Explains that a particle solver tracks each point's position and velocity as vectors and integrates motion each frame: new_position = old_position + velocity * timestep. Builds this directly with an Attribute Wrangle inside a SOP Solver using `@P += @v * ch('timestep');`. Adds gravity by subtracting from the Y component of velocity each frame, then introduces age/life attributes to kill particles once they exceed their lifespan. The key teaching point is that POPs are simply a specialized, optimized wrapper around this exact SOP Solver logic.

### Key Steps
1. [`Scatter SOP`] Generate 100 points as the initial particle source
2. [`SOP Solver`] Wrap the points in a SOP Solver to iterate per-frame state
3. [`Attribute Wrangle`] Integrate position from velocity: `@P += @v * ch('timestep');`
4. [`Attribute Wrangle`] Apply gravity by decrementing `@v.y` each frame
5. [Age/Life attributes] Track `@age` and `@life`; remove points once age exceeds life
6. [Verify] Inspect the Geometry Spreadsheet to confirm position and velocity update correctly each frame

### Houdini Nodes / VEX / Settings
- `Scatter SOP` — generates the initial particle point cloud
- `SOP Solver` — iterates geometry frame-by-frame, feeding its own output back as input
- `Attribute Wrangle` — VEX: `@P += @v * ch('timestep');` for Euler integration; gravity via `@v.y -= ch('gravity');`
- `age` / `life` attributes — standard Houdini particle lifespan pattern, manually implemented here

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)""",
        'related': """- [Creating a Simplified Particle System](52-creating-a-simplified-particle-system-v1-1080p.md) — extends this manual solver to emit new particles each frame
- [Recreating Our Solver With POPs](53-recreating-our-solver-with-pops-v1-1080p.md) — rebuilds this exact system using POPs for comparison
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — later course revisiting POPs terminology""",
    },

    "52-creating-a-simplified-particle-system-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[sop, dop, particles, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Extending the manual SOP Solver particle system to continuously emit new particles every frame, using a frame-dependent random seed and a Merge inside the solver to accumulate state.

### Summary
Uses `$F` as the global seed on the Scatter node so each frame produces a fresh point distribution. Inside the solver, merges the previous frame's existing particles (first input) with the new frame's freshly scattered particles (second input) using a Merge SOP, so the system continuously grows rather than resetting. Adds age tracking by incrementing `@age += 1/$FPS` each frame, and adds per-particle velocity variation via an Attribute Wrangle that randomizes initial `@v`. The Geometry Spreadsheet is used to confirm that, without the random seed logic, all particles share an identical constant velocity.

### Key Steps
1. [`Scatter SOP`] Set the random seed expression to `$F` so each frame emits a new distribution
2. [`Merge SOP`] Inside the SOP Solver, merge existing particles (input 1) with newly emitted particles (input 2)
3. [`Attribute Wrangle`] Increment age each frame: `@age += 1/$FPS;`
4. [`Attribute Wrangle`] Randomize initial velocity per new particle for variation
5. [Verify] Use the Geometry Spreadsheet to confirm velocity differs per particle once randomization is added

### Houdini Nodes / VEX / Settings
- `$F` expression — global current-frame variable used as a per-frame random seed for continuous emission
- `Merge SOP` (inside SOP Solver) — combines persisted particle state with newly emitted particles each frame
- `Attribute Wrangle` — VEX: `@age += 1/$FPS;` for time-correct age accumulation independent of frame rate
- Geometry Spreadsheet — used as the primary debugging tool to inspect per-point attribute values in real time

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)""",
        'related': """- [Introducing the SOP Solver](51-introducing-the-sop-solver-v1-1080p.md) — the foundational manual solver this extends
- [Recreating Our Solver With POPs](53-recreating-our-solver-with-pops-v1-1080p.md) — the POP-based equivalent of this continuous emission setup
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — POP terminology built on these SOP fundamentals""",
    },

    "53-recreating-our-solver-with-pops-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[dop, sop, particles, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Rebuilding the hand-crafted SOP Solver particle system with a proper POP Network, demonstrating the 1:1 correspondence between manual SOP-level particle logic and the dedicated POP toolset.

### Summary
Creates a POP Network and feeds the surface geometry directly into its first input (no need to pre-scatter). Inside the network: a POP Solver handles all integration automatically, a POP Object stores all simulation state (the DOP-level container analogous to the manual attribute storage used previously), and a POP Source emits particles with surface emission and a constant birth rate matching the prior 100/frame. POP Wind adds directional force and POP Gravity adds downward acceleration. The lesson confirms both setups produce identical motion, validating that POPs are exactly the manual SOP Solver technique wrapped in a more convenient, optimized interface.

### Key Steps
1. [`POP Network`] Create a popnet fed directly by the surface geometry
2. [`POP Source`] Set emission type to surface with a constant birth rate of 100/frame
3. [`POP Solver`] Let the solver handle position/velocity integration automatically
4. [`POP Object`] Confirm this is the DOP-level state container equivalent to the earlier manual attributes
5. [`POP Wind`] Add directional force
6. [`POP Gravity`] Add downward acceleration
7. [Verify] Compare resulting motion against the manual SOP Solver version from lesson 52

### Houdini Nodes / VEX / Settings
- `POP Network` (popnet) — container DOP network for particle simulation
- `POP Source` — emits particles from geometry; birth rate and emission type configurable
- `POP Solver` — automatic position/velocity integrator, replacing the manual wrangle logic
- `POP Object` — DOP data container analogous to manually managed point attributes
- `POP Wind`, `POP Gravity` — standard force microsolvers

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)""",
        'related': """- [Creating a Simplified Particle System](52-creating-a-simplified-particle-system-v1-1080p.md) — the manual SOP Solver version this recreates with POPs
- [Introducing the SOP Solver](51-introducing-the-sop-solver-v1-1080p.md) — the original from-scratch particle integration lesson
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — later course applying POPs to a production shot""",
    },

    "76-starting-the-smoke-vortex-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[dop, sop, pyro, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Building a spinning torus as the velocity-imparting source geometry for a smoke vortex effect, relying on the torus's own rotation to seed the swirling motion rather than any external force field.

### Summary
Creates a Torus SOP aligned to the Z-axis, scaled to 0.6 radius with a tube radius of 0.025, with rows increased to 16 for resolution and a Subdivide added for smoothness. Animates rotation on the Z axis at `$F * 20` degrees for a fast spin. Uses a sign() function (covered in a prior lesson) to create an oscillating velocity field around the torus surface. Lifts the torus 1 unit off the ground so the resulting smoke column rises cleanly. This source geometry feeds into the Volume Source node in the DOP network built in the following lesson.

### Key Steps
1. [`Torus SOP`] Create and align to the Z-axis; set radius to 0.6, tube radius to 0.025
2. [Resolution] Increase rows to 16 for smoother geometry
3. [`Subdivide SOP`] Smooth the torus surface further
4. [Animate rotation] Set Z-axis rotation to `$F * 20` degrees for a fast spin
5. [`Attribute Wrangle`] Use `sign()` to create an oscillating velocity field around the torus
6. [Position] Lift the torus 1 unit off the ground for a clean rising smoke column
7. [Output] Pass this animated source geometry to the Volume Source node (next lesson)

### Houdini Nodes / VEX / Settings
- `Torus SOP` — the spinning source shape; radius and tube radius control its silhouette
- Rotation expression `$F * 20` — drives a continuous fast spin tied to frame number
- `sign()` VEX function — used to build the oscillating velocity field around the torus surface
- `Subdivide SOP` — smooths torus geometry before it becomes a pyro source

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)""",
        'related': """- [Building the Vortex DOP Network](78-building-the-vortex-dop-network-v1-1080p.md) — the following lesson that wires this source into a Pyro Solver
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — foundational volume concepts used by pyro sources
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — another pyro setup driven by a velocity source""",
    },

    "78-building-the-vortex-dop-network-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[dop, sop, pyro, volumes, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Building the DOP network for the spinning-torus smoke vortex: a Pyro Solver, Smoke Object and Volume Source, sized and sourced so the torus's own spin velocity drives the swirling column with no additional force fields.

### Summary
The core network uses three nodes: Pyro Solver, Smoke Object and Volume Source. A sizing trick temporarily adds a Static Object with the torus geometry to visually calibrate the Smoke Object's bounding box, which is then removed once sizing is confirmed. The smoke container is set to roughly 3 units wide, centered at 1.5 height to match the torus position, using "copy parameter / paste relative references" to link the container's center Y to half its size. The Volume Source uses SDF source type, links to the torus geometry, and sources both temperature and density. The Pyro Solver enables Disturbance and Turbulence microsolvers to break up the vortex edge. The key vortex technique is that the spinning torus imparts its own velocity to the smoke at emission, creating the helical swirling column without any extra custom force fields.

### Key Steps
1. [`Static Object`] Temporarily add the torus geometry to visually size the Smoke Object's bounds
2. [`Smoke Object`] Set container size to ~3 units, centered to match the torus height (linked via relative parameter reference)
3. [`Volume Source`] Set source type to SDF, link to torus geometry, source temperature and density
4. [`Pyro Solver`] Enable Disturbance and Turbulence microsolvers for vortex edge detail
5. [Remove sizing aid] Delete the temporary Static Object once the container is correctly sized
6. [Verify] Playback confirms the spinning torus geometry alone drives the helical smoke motion

### Houdini Nodes / VEX / Settings
- `Pyro Solver` — core combustion/smoke solver; Disturbance and Turbulence add visual breakup
- `Smoke Object` — defines the simulation container bounds and resolution
- `Volume Source` (SDF mode) — converts torus geometry into temperature/density source fields
- `Static Object` — used temporarily and only for visual bounding-box calibration
- Relative parameter references ("copy parameter / paste relative") — links container center to half its size for self-adjusting bounds

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Film FX Season 1)""",
        'related': """- [Starting the Smoke Vortex](76-starting-the-smoke-vortex-v1-1080p.md) — the preceding lesson building the spinning torus source
- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — another Pyro setup using Disturbance/Turbulence
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — foundational fog/SDF volume concepts""",
    },

    # ── Renascence 1.0 — Module I ─────────────────────────────────────

    "module-i-week-01-01-your-first-houdini-project-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[sop, lop, solaris, karma, rendering, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Introducing the updated Renascence Program Volume 1, working in Houdini 18.5 — the first version to include the Solaris context and Karma renderer — and establishing the course's SOP-to-render pipeline.

### Summary
Sets up the default "build" desktop layout and drops a sphere to introduce the basic SOP geometry workflow. Week 1's project is procedural modelling of a scattering-based scene, followed by lighting/materials in Solaris (the new USD-based context), rendering with Karma (the new render engine), and a light comp pass in Nuke. Establishes the course pipeline: SOP geometry -> Solaris LOP -> Karma render -> Nuke comp. This was the first VFX School program to adopt Solaris/Karma; earlier Film FX Season 1 lessons used only Mantra.

### Key Steps
1. [Desktop] Use the default "build" layout for the session
2. [`Sphere SOP`] Drop a sphere to demonstrate basic SOP geometry creation
3. [Procedural modelling] Build the week's scattering-based scene in SOPs
4. [Solaris LOP] Move geometry into the USD-based Solaris context for lighting/materials
5. [Karma render] Render the staged scene using the Karma engine
6. [Nuke comp] Take the Karma render into Nuke for a light compositing pass

### Houdini Nodes / VEX / Settings
- `Sphere SOP` — first geometry node used to demonstrate the SOP workflow
- Solaris (LOP context) — new in H18.5; USD-based staging context for lighting/materials/cameras
- Karma — new renderer introduced alongside Solaris in H18.5, replacing Mantra for this course's pipeline
- Pipeline pattern: SOP geometry -> Solaris LOP -> Karma render -> Nuke comp

### Difficulty
Beginner

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)""",
        'related': """- [Weeks Overview](00-weeks-overview-v1-1080p.md) — the earlier Film FX course that used Mantra instead of Solaris/Karma
- [Creating a New Project](module-i-week-02-01-creating-a-new-project-v1-1080p.md) — the following week's scattering project
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — continues the H18.5 Renascence pipeline""",
    },

    "module-i-week-02-01-creating-a-new-project-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[sop, instancing, attributes, procedural, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Scattering geometry over a head surface using two parallel approaches: building scatter elements entirely inside Houdini, and instancing Megascans models via the Quixel Bridge workflow.

### Summary
This week's focus is scattering objects over a surface — specifically distributing elements over a head mesh. Two sub-projects are introduced: building the scattered geometry entirely inside Houdini, and using Megascans models as instanced scatter elements through a Quixel Bridge workflow. New H18.5 scatter-related nodes and improved Copy to Points workflows are introduced. The head surface is the distribution surface, with attributes like `pscale`, `orient` and `Cd` controlling per-instance variation. The week's deliverable is a moss/plant-covered head scene rendered in Karma.

### Key Steps
1. [`Scatter SOP`] Distribute points across the head surface
2. [`Attribute Wrangle`] Set `pscale`, `orient` and `Cd` per point for instance variation
3. [Megascans / Quixel Bridge] Import Megascans models as alternate instance geometry
4. [`Copy to Points SOP`] Instance geometry (built-in or Megascans) onto the scattered points
5. [Render] Light and render the moss/plant-covered head in Karma

### Houdini Nodes / VEX / Settings
- `Scatter SOP` — distributes points over the head surface for instancing
- `Copy to Points SOP` (H18.5 improved workflow) — instances geometry per point, reading `pscale`/`orient`/`Cd`
- Quixel Bridge / Megascans — external asset library imported as instanced scatter geometry
- `Attribute Wrangle` — randomizes per-instance attributes for natural variation

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)""",
        'related': """- [Your First Houdini Project](module-i-week-01-01-your-first-houdini-project-v1-1080p.md) — the preceding week establishing the course pipeline
- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — the following week's cloud/volume work
- [Module I Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — another attribute-driven per-piece technique from a later module""",
    },

    "module-i-week-03-01-introduction-to-volumes-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[sop, vop, volumes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
A comprehensive introduction to Houdini volumes using a pig-head test geometry: distinguishing fog VDBs from SDFs, then building a cloud volume from a polygon mesh with procedural noise.

### Summary
Explains the fog VDB vs. SDF (signed distance field) distinction: fog is a density field (0 outside, positive inside), while an SDF is a distance field (negative inside, positive outside, zero exactly at the surface). Builds a cloud volume from a polygon mesh via the chain: mesh -> VDB from Polygons (SDF) -> VDB Reshape (dilate to add volume) -> cloud noise via Volume VOP. The Volume VOP workflow binds the density field, applies Turbulent Noise in 3D, uses Fit Range to remap noise into [0, 1], and multiplies that back into density. Introduces the built-in "test geometry" SOP variants (pig head, squab, crag, etc.) as quick geometry sources, and covers Volume Display settings — density threshold, smoke colour, and step size — for viewport preview.

### Key Steps
1. [`Test Geometry SOP`] Use the pig head (or similar) as a quick source mesh
2. [`VDB from Polygons`] Convert the mesh to an SDF level set
3. [`VDB Reshape SDF`] Dilate the SDF to add volume/thickness
4. [`Volume VOP`] Bind density; apply 3D Turbulent Noise
5. [Fit Range] Remap noise output into the [0, 1] range
6. [Multiply] Combine the remapped noise back into the density field
7. [Volume Display] Tune density threshold, smoke colour and step size for viewport preview

### Houdini Nodes / VEX / Settings
- `VDB from Polygons` — converts a closed mesh into a signed distance field volume
- `VDB Reshape SDF` — dilates/erodes an SDF to thicken or thin a volume
- `Volume VOP` / Turbulent Noise — procedural 3D noise driving cloud-like density variation
- Fit Range — remaps noise output range before recombining with density
- Fog vs. SDF — fog: 0 outside/positive inside; SDF: negative inside/positive outside/zero at surface

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)""",
        'related': """- [Creating a New Project](module-i-week-02-01-creating-a-new-project-v1-1080p.md) — the preceding scattering week
- [Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — the following week's POP work
- [Starting the Smoke Vortex](76-starting-the-smoke-vortex-v1-1080p.md) — applies volume/pyro concepts built on this VDB foundation""",
    },

    "module-i-week-04-01-introduction-to-particles-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[dop, sop, particles, simulation, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Introducing particles in the context of the Renascence program, clarifying SOP "points" vs. DOP "particles" terminology, and building a POP Network sourced from a pig-head test mesh.

### Summary
Clarifies that in SOPs these entities are called "points," while inside a DOP simulation the same entities are called "particles" — both inspected via the Geometry Spreadsheet. Sets up a POP Network sourcing from a medium-resolution pig-head test geometry, using POP Source (surface emission), POP Gravity, POP Drag and POP Color. Demonstrates key particle attributes: `@age`, `@life`, `@dead` (set to 1 to kill a particle), and `@pscale` (per-particle render size). Introduces the shelf-based POP workflow as an alternative to building manually inside a popnet, and connects forward to instancing: after simulation, Copy to Points replaces particle points with geometry instances for rendering.

### Key Steps
1. [Terminology] Distinguish SOP "points" from DOP "particles" — same data, different context
2. [`POP Network`] Source particles from the pig-head test geometry (surface emission)
3. [`POP Source`, `POP Gravity`, `POP Drag`, `POP Color`] Assemble the basic force/appearance chain
4. [Attributes] Use `@age`, `@life`, `@dead` and `@pscale` to control lifespan and per-particle size
5. [Shelf tools] Note the shelf-based POP workflow as a faster alternative to manual popnet building
6. [`Copy to Points`] Replace simulated particle points with render geometry after simulation

### Houdini Nodes / VEX / Settings
- `POP Source` — surface emission from the pig-head test geometry
- `POP Gravity`, `POP Drag` — standard force microsolvers
- `POP Color` — sets particle colour attribute for visualization
- `@dead` attribute — setting to 1 marks a particle for removal
- `Copy to Points SOP` — post-sim instancing step converting particle points into renderable geometry

### Difficulty
Beginner

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)""",
        'related': """- [Introduction to Volumes](module-i-week-03-01-introduction-to-volumes-v1-1080p.md) — the preceding week's volume work
- [Recreating Our Solver With POPs](53-recreating-our-solver-with-pops-v1-1080p.md) — the Film FX season's foundational POP lesson this builds on
- [Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — the following week's FLIP setup""",
    },

    "module-i-week-05-01-importing-the-geometry-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[sop, flip, dop, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Importing an animated horse Alembic file as the geometry source for the week's POP fluid / FLIP simulation, including a critical PolySoup-to-polygon conversion step and a slow-motion retiming pass.

### Summary
Workflow: File -> New Project, drag the .abc into the project geo folder, create a geometry node, add an Alembic SOP and browse to the file. A critical step is adding a Convert SOP after Alembic to convert from PolySoup to regular polygons — necessary for correct geometry selection and attribute access later. The animation is slowed using a Time Shift SOP: integer frames are disabled and time is multiplied by 0.3 to produce a slow gallop. This establishes the horse as the emission source (surface scatter) for the FLIP fluid that will coat it in the week's simulation.

### Key Steps
1. [New Project] File -> New Project; drag the horse .abc into the project geo folder
2. [`Alembic SOP`] Create a geometry node and browse to the imported .abc file
3. [`Convert SOP`] Convert from PolySoup to regular polygons for correct selection/attribute access
4. [`Time Shift SOP`] Disable integer frames; multiply time by 0.3 to slow the gallop animation
5. [Output] Use the resulting slow-motion horse mesh as the surface-scatter source for the FLIP sim

### Houdini Nodes / VEX / Settings
- `Alembic SOP` — imports the animated .abc horse geometry
- `Convert SOP` — PolySoup-to-polygon conversion, required before most SOP operations work correctly on Alembic imports
- `Time Shift SOP` — retimes animation independent of frame rate; here scaled by 0.3 with integer-frame snapping disabled

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)""",
        'related': """- [Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — the preceding week's POP fundamentals
- [Introduction to Grains](module-i-week-06-01-introduction-to-grains-v1-1080p.md) — the following week's Vellum grain simulation
- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — a later FLIP-on-animated-geometry setup for comparison""",
    },

    "module-i-week-06-01-introduction-to-grains-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[dop, sop, vellum, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Introducing Vellum grain simulations using an FBX zombie animation as the source, scattering grain particles throughout the body volume and using the animated mesh as a deforming collider for a disintegration effect.

### Summary
FBX import workflow: File -> Import Filmbox FBX, then scale down to 0.1 for proper scene scale (~2m character height). Creates a geometry node, uses Object Merge to bring in the zombie, then converts it via VDB From Polygons -> Points From Volume to scatter grain particles throughout the body volume. The grain setup uses the Vellum Grains shelf tool to create the PBD grain solver. Key grain parameters covered: particle separation (controls density), pscale (render size), friction and restitution. The animated zombie is used as a deforming collider so grains interact correctly with the moving body, producing a pour-out/disintegration sand effect as it dies. Notes that Renascence 1.0 uses the Vellum Grains DOP path rather than the older POP Grains node.

### Key Steps
1. [Import FBX] File -> Import Filmbox FBX; scale to 0.1 for correct real-world scene scale
2. [`Object Merge`] Bring the zombie geometry into the working network
3. [`VDB From Polygons`] Convert the zombie mesh to a volume
4. [`Points From Volume`] Scatter grain seed points throughout the body volume
5. [Vellum Grains shelf tool] Build the PBD grain solver from the scattered points
6. [Tune grains] Set particle separation, pscale, friction and restitution
7. [Deforming collider] Use the animated zombie mesh as a collider so grains react to body motion
8. [Result] Grains pour from the zombie as it dies, producing the disintegration effect

### Houdini Nodes / VEX / Settings
- `VDB From Polygons` + `Points From Volume` — standard pipeline for filling a mesh's interior with scatter points
- Vellum Grains (shelf tool) — builds the PBD grain solver network automatically
- Grain parameters — particle separation (density), pscale (render size), friction, restitution
- Deforming collider — an animated mesh used directly as a Vellum collision object so grains respond to motion

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)""",
        'related': """- [Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — the preceding week's FLIP/Alembic workflow
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — broader Vellum fundamentals including grains
- [Tabletop Week 01 Intro](w01-01-introduction-v1-1080p.md) — another RBD/particle instancing-driven effect for comparison""",
    },

}

if __name__ == "__main__":
    for slug, data in EXTRACTIONS_A.items():
        path = os.path.join(BASE, slug + ".md")
        if not os.path.exists(path):
            print(f"  MISSING: {path}")
            continue
        update_file(path, data['fm'], data['notes'], data['related'])
    print(f"\nDone: {len(EXTRACTIONS_A)} files processed.")
