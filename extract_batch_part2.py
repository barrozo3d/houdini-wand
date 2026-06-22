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

EXTRACTIONS_PART2 = {

    # =========================================================================
    # BRIDGE DESTRUCTION IN HOUDINI — Week intro videos
    # =========================================================================

    "week-01-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rbd, simulation, dop, procedural, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-one overview of the Manhattan Bridge Destruction course: importing, organising and preparing bridge geometry for a multi-body RBD simulation including Voronoi fracture of the road and Boolean fracture of the deformable metal.

### Summary
The instructor outlines what week one covers: importing the bridge model, splitting it into simulated vs. static parts, and further categorising those parts into deformable metal, rigid metal and road geometry. The road is fractured with a Boolean (cutting geometry) method while the metal uses Voronoi. Soft constraints with plasticity are configured to give the metal realistic bending behaviour, and the bridge itself is animated to sway as if in wind, driving the simulation.

### Key Steps
1. [`File SOP`] Import the bridge model and inspect geometry
2. [`Blast SOP`] Separate static vs. simulated sections of the bridge
3. [`Group SOP`] Organise simulated geometry into deformable metal, rigid metal and road groups
4. [`Boolean Fracture`] Fracture the road using cutting geometry (Boolean method)
5. [`Voronoi Fracture SOP`] Fracture the deformable metal elements
6. [`RBD Configure`] Pack and prepare all fractured pieces for the Bullet solver
7. [`Constraint Network`] Set up soft constraints with plasticity for the metal
8. [`Channel CHOP / Keyframes`] Animate the bridge sway to drive the simulation

### Houdini Nodes / VEX / Settings
- `File SOP` — reads the bridge model from disk
- `Blast SOP` — isolates static vs. simulated geometry
- `Group SOP` — tags pieces as deformable metal, rigid metal or road
- `Boolean Fracture` — cuts road geometry with user-defined cutting shapes
- `Voronoi Fracture SOP` — shatters metal into irregular rigid chunks
- `RBD Configure` — packs geo and adds required RBD attributes for Bullet solver
- Soft Constraints + Plasticity — lets metal bend and hold shape under stress

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — shared RBD/Bullet fundamentals
- [RBD Configure Deep Dive](week-01-11-rbd-configure-v1-1080p.md) — detailed look at the RBD Configure node used in this week
- [Module I Intro](module-i-week-01-01-intro-v1-1080p.md) — parallel RBD intro from the earlier course""",
    },

    "week-02-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rbd, vellum, simulation, dop, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-two overview of the Bridge Destruction course: simulating the bridge cables — stiff horizontal cables using Bullet's guided-sim workflow and flexible vertical cables using Vellum.

### Summary
The instructor introduces the cable simulation strategy, distinguishing between the heavy, near-rigid horizontal suspension cables (simulated with Bullet hard constraints driven by the week-one guided sim result) and the more flexible vertical hanger cables (simulated with Vellum). The geometry is simplified to four strands before simulation. The guided simulation workflow in Houdini 18 is introduced as a key technique for making secondary elements follow the main RBD sim without a full independent solve.

### Key Steps
1. [`File SOP`] Load the cable geometry from the bridge model
2. [`Resample / Curve`] Simplify complex cable geometry to four clean strands
3. [`RBD Constraints from Rules`] Build hard constraints between cable segments
4. [`RBD Material Fracture` / Guided Sim setup] Wire the guided sim so cables follow the week-one road/metal sim
5. [`Vellum Configure Wire`] Set up the vertical hanger cables as Vellum wires
6. [`Vellum Solver`] Run the Vellum wire simulation for vertical cables
7. [`RBD Solver`] Run the Bullet sim for horizontal cables

### Houdini Nodes / VEX / Settings
- `RBD Constraints from Rules` — procedurally generates constraints between adjacent cable pieces
- Hard Constraints — preferred over soft for stiff cable-like behaviour with no plasticity needed
- Guided Simulation (Bullet) — drives secondary sim pieces from a reference simulation result
- `Vellum Configure Wire` — sets up wire (hair/cable) constraints in Vellum
- `Vellum Solver` — solves the Vellum constraint network each frame

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Starting the Guided Sim](week-02-03-starting-the-guided-sim-v1-1080p.md) — hands-on guided sim setup for the horizontal cables
- [Starting the Vellum Sim](week-02-07-starting-the-vellum-sim-v1-1080p.md) — hands-on Vellum wire setup for the vertical cables
- [Module II Intro to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — foundational Vellum concepts""",
    },

    "week-03-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18.5"',
            'tags': '[rbd, simulation, dop, instancing, attributes, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-three overview: procedurally scattering and simulating a fleet of cars on the bridge road surface using Bullet RBD, including cone-twist suspension constraints and a procedural intersection-removal system.

### Summary
The instructor explains how to import varied vehicle geometry, separate bodies from wheels, and scatter them across the road using new Houdini 18.5 SOPs (Scatter and Align, Attribute from Pieces). A procedural system removes intersecting cars before a lightweight pre-simulation settles them against each other. The main sim then uses soft constraints and cone-twist constraints to fake vehicle suspension behaviour during the destruction event.

### Key Steps
1. [`File SOP`] Import a variety of vehicle models
2. [`Group SOP`] Separate wheel geometry from body geometry per vehicle
3. [`Scatter and Align SOP`] Place vehicles on the road surface with directional variation (Houdini 18.5)
4. [`Attribute from Pieces SOP`] Transfer per-piece attributes to scattered instances (Houdini 18.5)
5. [`VEX Wrangle`] Procedurally detect and remove intersecting cars
6. [`RBD Solver`] Run a quick pre-sim to settle/slide cars before the main destruction
7. [`Constraint Network`] Apply cone-twist constraints for wheel suspension behaviour
8. [`RBD Solver`] Run the full main destruction simulation with the cars included

### Houdini Nodes / VEX / Settings
- `Scatter and Align SOP` (H18.5) — scatters points on a surface and aligns them to the surface normal with variation
- `Attribute from Pieces SOP` (H18.5) — copies per-piece attributes onto scattered instances
- Cone Twist Constraints — allow constrained rotation within a cone angle, ideal for wheel pivots
- Soft Constraints — used alongside cone-twist to provide suspension spring-like behaviour

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Bridge Destruction course)""",
        'related': """- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — RBD/Bullet fundamentals that underpin the car sim
- [Module I Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — active attribute usage relevant to staged activation of cars
- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — the road fracture sim the cars ride on""",
    },

    "week-04-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[particles, pyro, simulation, dop, attributes, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-four overview: generating debris particles with the Debris Source node and driving two separate Pyro simulations — one based on the POP sim output — to produce realistic dust and smoke for the bridge destruction.

### Summary
This week covers three simulations: one POP (particle) simulation for debris chunks and two Pyro smoke simulations. The Debris Source SOP scatters points between separating RBD pieces and deletes them by age. Particles are then culled by speed so only fast-moving geometry emits debris. Noise is added to density and temperature attributes before feeding into the Pyro sims, which are enhanced with disturbance and turbulence for realistic detail.

### Key Steps
1. [`Debris Source SOP`] Scatter debris points at separation boundaries between RBD pieces
2. [`POP Solver`] Simulate debris particles with gravity and lifetime
3. [`Attribute Wrangle`] Add noise to `density` and `temperature` point attributes
4. [`Speed Cull`] Filter points so only high-velocity pieces emit debris/smoke
5. [`Pyro Source`] Convert the POP points into a volumetric pyro source
6. [`Pyro Solver`] Run first Pyro sim for general dust cloud
7. [`Pyro Solver`] Run second Pyro sim driven by the POP sim result for localised smoke

### Houdini Nodes / VEX / Settings
- `Debris Source SOP` — detects close RBD pieces and scatters emission points at their boundaries; points deleted by an `age` attribute ramp
- `Pyro Source SOP` — converts point or volume data into density/temperature fields for Pyro
- Disturbance + Turbulence — Pyro solver microsolver settings that break up the smoke for added realism
- Speed-based culling — velocity threshold on points controls which pieces contribute emission

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Cull by Speed](week-04-06-cull-by-speed-v1-1080p.md) — deep dive into the velocity-based culling step introduced this week
- [Building the Vortex DOP Network](78-building-the-vortex-dop-network-v1-1080p.md) — advanced Pyro techniques for comparison
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — foundational POP concepts""",
    },

    "week-05-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rendering, mantra, volumes, compositing, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-five overview: bringing the full bridge destruction scene to a final render in Mantra — importing shaders and cameras, randomising vehicle colours, generating fog volumes, lighting with HDRI and distant light, and compositing in Nuke.

### Summary
The final week of the Bridge Destruction course focuses on rendering. Pre-built shaders and cameras are merged in from a provided scene file. Vehicle colours are randomised procedurally to add visual variety. Fog volumes are generated to set atmosphere, then everything is lit with an HDRI and a distant light. The Mantra render passes are taken into Nuke for a straightforward but dramatic composite result.

### Key Steps
1. [`File Merge`] Import shaders and cameras from a provided Houdini scene
2. [`Attribute Randomize / Wrangle`] Randomise colour attributes across car/truck pieces
3. [`Volume SOP / Fog Volume`] Generate atmospheric fog volumes
4. [`Mantra ROP`] Configure and launch the Mantra renderer
5. [`Environment Light`] Set up HDRI sky lighting
6. [`Distant Light`] Add directional sunlight
7. [Nuke comp] Import render passes and produce final composite

### Houdini Nodes / VEX / Settings
- `Mantra ROP` — the render output operator driving Mantra
- `Environment Light` — sphere light accepting an HDRI map for image-based lighting
- `Distant Light` — parallel sun-direction light
- Volume SOP (fog) — creates low-density atmospheric volumes for depth and haze
- Attribute randomise — randomises `Cd` or shader parameter per piece for colour variation

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — the debris/pyro sims being rendered this week
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — the RBD elements feeding into this render
- [Module I Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — parallel rendering setup from the earlier course""",
    },

    # =========================================================================
    # BRIDGE DESTRUCTION — Gap-filler videos
    # =========================================================================

    "week-01-11-rbd-configure-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rbd, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Deep dive into the `RBD Configure` node — visualising and tuning collision geometry representation and padding to ensure accurate Bullet solver contacts for bridge destruction pieces.

### Summary
The instructor drops in the RBD Configure node, then isolates a single piece using Delete nodes to inspect its collision geometry. The Visualize tab is used to reveal the collision proxy, which is larger than the actual mesh by default due to collision padding. The tutorial covers how to adjust collision padding on the solver vs. per-piece, and how to switch collision shape type (convex hull, bounding box, concave) for different piece types.

### Key Steps
1. [`RBD Configure`] Drop and connect to pack all simulated geometry
2. [`Delete SOP`] Isolate a single piece for per-piece collision inspection
3. [`Bullet Solver`] Connect a test solver; enable Visualize > Show Geometry Representation
4. [Solver settings] Adjust Collision Padding on the solver to reduce proxy inflation
5. [`RBD Configure` > Collision Shapes] Change collision shape type (convex hull / bounding box / concave)
6. [Per-piece override] Set collision padding per primitive group for finer control
7. [Verify] Inspect final collision proxy fits actual mesh before caching

### Houdini Nodes / VEX / Settings
- `RBD Configure` — packs geometry and writes RBD-required point/primitive attributes; exposes Collision Shapes tab for per-piece proxy type
- `Bullet Solver` — Visualize tab > Show Geometry Representation displays active collision proxy
- Collision Padding — gap added around each proxy shape; reduces interpenetration but inflates collisions if too large
- Collision Shape Types — Convex Hull (default, fast), Box (fastest), Concave (accurate, slow)

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Bridge Destruction Week 01 Intro](week-01-01-intro-v1-1080p.md) — the overall week where RBD Configure is first introduced
- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — foundational Bullet sim setup
- [Module I Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — related per-piece RBD attribute work""",
    },

    "week-02-03-starting-the-guided-sim-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rbd, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Setting up the Bullet guided-simulation workflow for the bridge's horizontal cables — assigning name attributes, building hard constraints with RBD Constraints from Rules, and wiring the guide sim to inherit motion from the week-one road/metal RBD result.

### Summary
The instructor gives the cable blocks a `name` attribute so each segment is individually identifiable, then feeds them into RBD Constraints from Rules to generate surface-point-based hard constraints between adjacent pieces. Hard constraints are chosen over soft because the cables are stiff and need no plasticity. The guide simulation is then established by linking the cable RBD network to the previously cached week-one simulation so cable motion is guided by bridge collapse motion rather than solved independently.

### Key Steps
1. [`Attribute Wrangle / Name SOP`] Assign a unique `name` attribute to each cable block
2. [`RBD Constraints from Rules`] Generate surface-point constraints between cable pieces; connect render and proxy geometry inputs
3. [`RBD Constraint Properties`] Switch constraint type from soft to hard for cable stiffness
4. [`Guided Simulation SOP`] Load the week-one sim as a guide source
5. [Guide Strength] Set the strength parameter controlling how strongly pieces follow the guide
6. [Guide Release Thresholds] Configure angular and linear thresholds for when pieces detach from the guide
7. [`RBD Solver`] Run the guided cable simulation and verify cable motion follows bridge collapse

### Houdini Nodes / VEX / Settings
- `Name SOP` — assigns a string name attribute per piece, required by constraint-building nodes
- `RBD Constraints from Rules` — generates constraint geometry from proximity/rules between named pieces
- `RBD Constraint Properties` — sets constraint type (hard/soft/cone-twist) and strength
- Guided Simulation — Houdini 18 feature allowing one RBD sim to follow another; guide strength and release thresholds control the transition
- Hard Constraints — zero-compliance constraints; ideal for stiff cables that must not bend

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Finishing the Horizontal Cable Sim](week-02-04-finishing-the-horizontal-cable-sim-v1-1080p.md) — continuation of this exact setup
- [Bridge Destruction Week 02 Intro](week-02-01-intro-v1-1080p.md) — overview of the cable week
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — Vellum approach used for vertical cables""",
    },

    "week-02-04-finishing-the-horizontal-cable-sim-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rbd, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Completing the guided Bullet simulation for the bridge's horizontal cables — resolving intra-guide constraint removal, tuning guide strength and release thresholds to control when cable segments detach and fall freely.

### Summary
The instructor resolves a constraint-visibility issue caused by the guided sim removing intra-guide constraints by default, which is toggled off to restore correct cable connections. Guide strength is demonstrated by setting it to zero, causing all pieces to fall immediately and freely, showing how strength controls the blending between guided and free-simulated motion. The angular and linear release thresholds within the Guided Simulation settings are then tuned to define the exact point at which cable segments break away from the guide and simulate independently.

### Key Steps
1. [Guided Sim > Constraints Tab] Disable "Remove Intra-Guide Constraints" to restore constraint visibility
2. [`RBD Solver` playback] Verify constraints now appear and hold correctly
3. [Guide Strength] Set strength to 0 to see unconstrained fall; then restore to working value
4. [Guided Sim > Simulation Settings] Locate angular threshold and linear threshold parameters
5. [Angular Threshold] Tune the angle at which a piece detaches from the guide
6. [Linear Threshold] Tune the linear velocity/displacement that triggers detachment
7. [`RBD Solver`] Final playback confirming cables follow guide then release on collapse

### Houdini Nodes / VEX / Settings
- Guided Sim Constraints Tab > Remove Intra-Guide Constraints — toggle that incorrectly removes constraints between guided pieces; must be disabled
- Guide Strength — float parameter (0-1) blending guide influence; 0 = fully free, 1 = fully guided
- Angular Release Threshold — maximum angular deviation from guide before a piece goes free
- Linear Release Threshold — maximum positional deviation before a piece detaches

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Starting the Guided Sim](week-02-03-starting-the-guided-sim-v1-1080p.md) — the preceding setup step this video completes
- [Bridge Destruction Week 02 Intro](week-02-01-intro-v1-1080p.md) — week overview
- [Starting the Vellum Sim](week-02-07-starting-the-vellum-sim-v1-1080p.md) — Vellum wire approach for the vertical cables""",
    },

    "week-02-07-starting-the-vellum-sim-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[vellum, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Setting up a Vellum cloth/wire simulation for the bridge's vertical hanger cables, including pin constraints, match animation, and using rest length scale below 1 to pre-tension the cables so they are taut from frame one.

### Summary
The instructor uses Vellum Configure Cloth (treated as a wire/cable) for the vertical cables. The key discovery is setting Rest Length Scale to 0.8 (below 1.0), which makes the constraints shorter than the actual geometry, placing the cables under tension from the first frame of the simulation — physically accurate for bridge suspension cables. Pin points are grouped and wired to the main cable attachment locations, and Match Animation is enabled so pins follow the animated bridge structure throughout the sim.

### Key Steps
1. [`Vellum Configure Cloth`] Drop and connect vertical cable geometry as the first input
2. [Constraint Generation] Leave Distance Along Edges at default; verify constraint lines appear
3. [Pin Group] Create a point group for cable attachment points; assign as the Pin to Animation group
4. [Match Animation] Enable Match Animation so pinned points follow the animated bridge
5. [Rest Length Scale] Set to 0.8 so constraints are shorter than rest state, placing cables under pre-tension
6. [Stretch Stiffness] Leave at high default for near-inextensible cables
7. [`Vellum Solver`] Connect and run; verify cables start taut and respond to bridge motion

### Houdini Nodes / VEX / Settings
- `Vellum Configure Cloth` — generates distance and bend constraints; used here for wire-like cable behaviour
- Rest Length Scale — multiplier on constraint rest lengths; values below 1.0 pre-compress/pre-tension the sim
- Pin to Animation — group name whose points are locked to animated positions each frame
- Match Animation — Vellum solver setting that keeps animated pin points synced to animated input geometry
- Stretch Stiffness — resistance to length change along constraint edges; high = near-inextensible

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Setting Strong Constraints and Breaking Threshold](week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p.md) — the next step adding breakable vs. unbreakable constraints
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — foundational Vellum concepts
- [Bridge Destruction Week 02 Intro](week-02-01-intro-v1-1080p.md) — week overview introducing the Vellum approach""",
    },

    "week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[vellum, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Enabling all bridge vertical cables in the Vellum sim and differentiating constraint break strength — making rear-section cable attach constraints unbreakable while allowing forward-section cables to snap at a tuned threshold, driving the visual cable-snapping destruction effect.

### Summary
With a single test cable working, the Delete/Blast node isolating it is disabled so all cables enter the sim together. The instructor identifies that rear bridge cables should never detach (the rear section of the bridge remains intact), so those attach constraints are flagged as unbreakable using a geometry-based selection combined with a TimeShift to the last frame. A break threshold is then set on the remaining forward cables, controlling at what stress value they snap — producing the signature bridge cable snap effect during destruction.

### Key Steps
1. [`Blast SOP`] Disable the isolating Blast node to include all cable geometry
2. [`Object Merge`] Bring in rear bridge section geometry for spatial reference
3. [`TimeShift SOP`] Sample the rear bridge geo at the last frame (e.g. frame 250) to confirm it never falls
4. [`Attribute Wrangle`] Set `breakthreshold` attribute to a very high value (unbreakable) on rear cable constraints
5. [`Attribute Wrangle`] Set tuned `breakthreshold` on forward section cable constraints
6. [`Vellum Solver`] Run full cable sim; verify rear cables hold and forward cables snap at collapse
7. [Iterate] Adjust break threshold values until snap timing matches the desired destruction beat

### Houdini Nodes / VEX / Settings
- `breakthreshold` attribute — per-constraint Vellum attribute; controls the stress value at which a constraint is deleted
- `TimeShift SOP` — freezes geometry to a specific frame for spatial queries; used here to sample final bridge position
- `Object Merge` — references geometry from another area of the network for constraint spatial selection
- `Blast SOP` — used earlier to isolate test cables; disabled here to restore all cables

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Starting the Vellum Sim](week-02-07-starting-the-vellum-sim-v1-1080p.md) — the preceding step that established the Vellum wire setup
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — foundational Vellum concepts including constraint attributes
- [Starting the Guided Sim](week-02-03-starting-the-guided-sim-v1-1080p.md) — the Bullet guided sim for horizontal cables, parallel to this Vellum work""",
    },

    "week-04-06-cull-by-speed-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[particles, pyro, attributes, vex, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Velocity-based particle culling — reading velocity magnitude from RBD simulation points and removing (culling) those below a speed threshold so that only fast-moving debris pieces emit smoke/dust particles.

### Summary
The instructor caches the POP sim result to disk and enables load-from-disk for fast flipbook playback. Particles are displayed as pixels or small points for viewport clarity. The core technique reads the `v` (velocity) attribute on each point, computes its length, and uses a threshold to delete slow-moving points so that only high-speed objects contribute to pyro emission sources. This prevents stationary or slowly-settling debris from generating unwanted smoke.

### Key Steps
1. [Cache + Load from Disk] Cache the POP sim to disk; enable Load from Disk on the File Cache node for fast playback
2. [`Merge SOP`] Temporarily merge debris into the main network for preview
3. [Viewport Display] Press D > Geometry > Particles Display; switch to Pixels or Points with reduced size for clarity
4. [`Attribute Wrangle`] Compute velocity magnitude: `float spd = length(v);`
5. [`Blast SOP` or Wrangle] Delete points where `spd` is below the speed threshold
6. [Iterate] Flipbook to verify only fast-moving pieces retain points
7. [Output] Feed culled points into the Pyro Source for smoke/dust emission

### Houdini Nodes / VEX / Settings
- `File Cache SOP` (Load from Disk) — reads pre-cached .bgeo.sc frames for near-instant playback of point sims
- `Attribute Wrangle` — VEX: `float spd = length(v); if (spd < threshold) removepoint(0, @ptnum);`
- `v` attribute — world-space velocity vector on RBD/POP points; standard Houdini velocity attribute
- Viewport Display (D key > Particles) — switches particle display mode to Pixels or Points for better visibility

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Bridge Destruction course)""",
        'related': """- [Bridge Destruction Week 04 Intro](week-04-01-intro-v1-1080p.md) — the week overview that introduces this speed cull concept
- [Module I Introduction to Particles](module-i-week-04-01-introduction-to-particles-v1-1080p.md) — foundational POP/particle work
- [Building the Vortex DOP Network](78-building-the-vortex-dop-network-v1-1080p.md) — Pyro that consumes these culled points""",
    },

    # =========================================================================
    # TABLE TOP FOOD SIMULATION — Week intro videos
    # =========================================================================

    "w01-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[rbd, simulation, dop, instancing, rendering, beginner]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-one overview of the Tabletop Food Simulation course: reproducing a coffee bean avalanche shot using Bullet RBD with instanced geometry, varied orientations and velocities, retiming tricks, and a full lighting/shading/rendering pipeline in Arnold.

### Summary
The instructor introduces the tabletop course by describing the coffee bean shot goal. The week covers instancing bean geometry to scattered points, varying instance orientations and initial velocities, feeding the points into a Bullet dynamics network, and adding spin and gravity for realistic collisions. Post-simulation, retiming is used and the bean count is doubled without re-simulating. The week concludes with Arnold lighting, shading and rendering.

### Key Steps
1. [`Scatter SOP`] Scatter points above the shot area as initial bean positions
2. [`Copy to Points SOP`] Instance coffee bean geometry onto scattered points
3. [`Attribute Wrangle`] Vary `orient` and `v` (velocity) attributes per instance for randomness
4. [`RBD Configure`] Pack instanced geometry for Bullet solver
5. [`RBD Solver`] Build bullet sim with gravity and angular velocity (spin)
6. [Collision geometry] Set up collision surface for beans to land on
7. [Post-sim retiming] Use a Time Blend or retime trick to slow/speed the sim
8. [`Copy to Points`] Double bean count by merging a time-offset version of the sim
9. [Arnold ROP] Shade, light and render the final result

### Houdini Nodes / VEX / Settings
- `Copy to Points SOP` — instances geometry per point; reads `orient`, `pscale`, `v` attributes for per-instance variation
- `Attribute Wrangle` — sets random orientations (`orient` quaternion) and velocities (`v`) per point
- `RBD Configure` — packs geo and prepares RBD attributes for Bullet
- `RBD Solver (Bullet)` — rigid-body dynamics solver driving bean collisions
- Retiming — time-warp technique applied post-cache to create slow-motion without re-simulating

### Difficulty
Beginner

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Module II Week 01 Basic Bullet Sim](module-ii-week-01-01-basic-bullet-sim-v1-1080p.md) — foundational RBD Bullet techniques
- [Module I Intro](module-i-week-01-01-intro-v1-1080p.md) — parallel beginner RBD intro
- [Tabletop Week 05 Intro](w05-01-intro-v1-1080p.md) — the final course week combining RBD with FLIP""",
    },

    "w02-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[sop, attributes, procedural, animation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-two overview of the Tabletop course: faking fluid surface deformation (yogurt displacement) using procedural SOP techniques driven by velocity and geometry rather than any fluid simulation, for fast iteration with convincing splash shapes.

### Summary
Instead of running a FLIP simulation for the yogurt, the instructor uses purely procedural SOP deformation to recreate the look of blueberries and chocolate falling into yogurt. Velocity attributes from the falling objects are sampled and used to displace the yogurt surface geometry. This approach avoids heavy fluid simulation entirely, making it extremely quick to iterate while still achieving believable fluid-like shapes. Shading, lighting and rendering complete the week.

### Key Steps
1. [Review falling objects] Inspect blueberry/chocolate RBD geo and its velocity attributes
2. [`Trail SOP`] Compute velocity (`v`) on the falling geometry via Trail SOP in "Compute Velocity" mode
3. [`Attribute Transfer SOP`] Transfer velocity from falling objects onto yogurt surface points
4. [`Attribute Wrangle`] Displace yogurt surface point positions using transferred velocity magnitude
5. [Noise + Ramp] Add procedural noise to the displaced surface for organic fluid-like ripples
6. [Shading] Apply Principled Shader to yogurt with subsurface and gloss parameters
7. [Arnold ROP] Light and render the combined scene

### Houdini Nodes / VEX / Settings
- `Trail SOP` (Compute Velocity mode) — calculates per-point velocity vector from positional change between frames without leaving a trail
- `Attribute Transfer SOP` — copies attributes (here `v`) from one geometry to another based on proximity
- `Attribute Wrangle` — displaces `@P` along the transferred velocity or normal direction proportional to speed
- This technique avoids any DOP/FLIP entirely — all computation stays in SOPs

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Deforming with Velocity](w02-05-deforming-with-velocity-v1-1080p.md) — hands-on implementation of the velocity deformation introduced this week
- [Module I Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — related SOP deformation by attributes
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — next week using actual FLIP simulation""",
    },

    "w03-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[flip, simulation, dop, rendering, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-three overview of the Tabletop course: simulating multiple thick, viscous fluid streams (chocolate, caramel and similar sauces) pouring onto ice cream using the FLIP solver with per-fluid viscosity attributes.

### Summary
This is the course's first full FLIP simulation week. Three different fluid emitters each carry a different viscosity attribute value to mimic distinct food fluids (e.g. runny caramel vs. thick chocolate). The FLIP solver's viscosity features are central to achieving sticky, slow-flowing behaviour. The week takes the sim all the way through to Mantra/Arnold lighting, shading and rendering.

### Key Steps
1. [`FLIP Fluid Object`] Create a FLIP fluid object for the first sauce emitter
2. [`Source Volume SOP`] Define per-emitter geometry as the fluid source
3. [`Attribute Wrangle`] Set `viscosity` attribute per emitter point to differentiate fluid types
4. [`FLIP Solver` > Viscosity] Enable viscosity solving in the FLIP solver
5. [`FLIP Object` > Physical] Set viscosity value per fluid object (e.g. 100-5000 range)
6. [Collision geometry] Set up ice cream bowl/surface as a static collision object
7. [Meshing] Convert FLIP particles to a mesh via VDB for rendering
8. [Shading + Render] Apply Principled Shader per fluid; light and render

### Houdini Nodes / VEX / Settings
- `FLIP Fluid Object` — DOP node defining a FLIP particle fluid; Physical tab contains viscosity parameter
- `FLIP Solver` — Viscosity tab must have "Enable Viscosity" checked for viscous behaviour
- `viscosity` attribute — per-point float that can override the global viscosity value when imported
- `Source Volume SOP` — converts SOP geometry into a velocity/density source for the FLIP object

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Adding Viscosity to FLIP](w03-04-adding-viscosity-v1-1080p.md) — detailed hands-on step for viscosity configuration
- [Meshing (VDB Layer Separation)](w03-11-meshing-v1-1080p.md) — the meshing step introduced this week
- [Small Scale Fluids](small-scale-fluids.md) — parallel FLIP small-scale reference""",
    },

    "w04-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[flip, simulation, dop, rendering, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-four overview: simulating a strawberry colliding with poured milk using FLIP fluids with an animated emitter, viscosity, surface tension, VDB meshing for flicker-free results, and complex Arnold shading for the strawberry (subsurface + transparency).

### Summary
This week introduces an animated FLIP fluid emitter (milk pour) combined with a separately animated strawberry collision object. The instructor highlights the use of viscosity and surface tension as critical parameters that give milk its characteristic behaviour — forming a crown splash with held droplets. The sim is meshed using VDB for a stable, flicker-free mesh, and rendered in Arnold with complex subsurface-scattering and transparency on the strawberry shader.

### Key Steps
1. [Animated strawberry FBX/Alembic] Import updated strawberry animation; use the new animation from the start
2. [`FLIP Source`] Build animated emitter geometry to mimic milk pouring
3. [`Attribute Wrangle / Keyframes`] Animate emitter velocity and position to arc the pour
4. [`FLIP Solver` > Viscosity] Enable and tune viscosity for milk (low value)
5. [`FLIP Solver` > Surface Tension] Enable surface tension to create crown splash and droplet cohesion
6. [`VDB from Particles`] Convert FLIP points to VDB for smooth meshing
7. [`VDB Smooth SDF`] Smooth the VDB to remove particle-level roughness
8. [`Convert VDB`] Extract polygon mesh from VDB for rendering
9. [Arnold ROP] Shade strawberry with SSS + transparency; light and render

### Houdini Nodes / VEX / Settings
- `FLIP Solver` > Viscosity — controls resistance to flow; low values for milk (~1-10)
- `FLIP Solver` > Surface Tension — simulates cohesive force holding fluid together; critical for milk crowns and droplets
- `VDB from Particles` — converts FLIP particle points to a VDB level set; voxel size controls detail/speed tradeoff
- `VDB Smooth SDF` — Gaussian smoothing on the SDF removes particle-level noise before meshing
- `Convert VDB` — extracts polygon surface from VDB level set

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Viscosity and Surface Tension](w04-11-viscosity-and-surface-tension-v1-1080p.md) — hands-on deep dive into these FLIP parameters
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the preceding FLIP week covering viscous sauces
- [Small Scale Fluids](small-scale-fluids.md) — FLIP reference for small-scale setups""",
    },

    "w05-01-intro-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[flip, rbd, simulation, dop, rendering, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Week-five overview: the course's first combined RBD + FLIP simulation — dropping strawberries with Bullet RBD onto a FLIP fluid tank, converting the settled RBD result into a static FLIP collider, and controlling splash shape with velocity.

### Summary
This final tabletop week uses a FLIP tank setup (contained fluid volume) rather than an emitter. Strawberries are first simulated with Bullet RBD to settle on a surface, then the packed geo is converted into a static collider for the FLIP solver. Splash shape is controlled by adjusting initial fluid velocity. Viscosity and surface tension are applied again. The week concludes with the full texturing, shading, lighting and rendering pipeline.

### Key Steps
1. [`RBD Solver`] Drop strawberries onto the surface with Bullet; cache the settled result
2. [`RBD Packed Object`] Convert cached RBD strawberry positions to static collision geometry
3. [`FLIP Tank`] Create a FLIP fluid tank filled with liquid
4. [`Static Object DOP`] Import settled strawberry geo as a static FLIP collision object
5. [`FLIP Solver` > Velocity] Control the initial fluid velocity to shape the splash
6. [`FLIP Solver` > Viscosity + Surface Tension] Apply fluid physical properties
7. [Meshing] VDB from Particles -> VDB Smooth -> Convert VDB polygon mesh
8. [Render] Apply textures (strawberry, fluid), light scene, render in Arnold

### Houdini Nodes / VEX / Settings
- `FLIP Tank` — pre-configured FLIP object that fills a bounded volume with particles
- `Static Object DOP` — brings SOP geometry into DOPs as a passive non-simulated collider
- `RBD Packed Object` — packed geometry for efficient Bullet simulation
- Velocity control on FLIP emitter — scaling or directing the initial `v` attribute on source particles shapes the crown and splash direction

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — the preceding FLIP week (milk pour)
- [Tabletop Week 01 Intro](w01-01-introduction-v1-1080p.md) — the RBD-only coffee bean week that set up RBD skills reused here
- [Module I Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — parallel rendering pipeline reference""",
    },

    # =========================================================================
    # TABLE TOP FOOD SIMULATION — Gap-filler videos
    # =========================================================================

    "w02-05-deforming-with-velocity-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[sop, attributes, vex, animation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Using the Trail SOP in Compute Velocity mode to generate a velocity attribute on animated geometry, then transferring and using that velocity to displace a surface mesh — a reusable no-simulation technique for fluid-like deformation and motion blur.

### Summary
Starting from blueberry geometry with only position, normals and UVs, the instructor adds a velocity attribute using the Trail SOP set to "Compute Velocity" rather than its default trail mode. This `v` attribute is then used to drive positional displacement of the yogurt surface. The instructor also notes this is a standard technique for adding motion blur to animated geometry that lacks velocity in Arnold or Mantra. The velocity is scaled and applied per point in a wrangle for art-directable control over the splash shape.

### Key Steps
1. [`Geometry Spreadsheet`] Confirm no `v` attribute exists on the falling blueberry points
2. [`Trail SOP`] Drop Trail SOP; switch mode from "Trail" to "Compute Velocity"
3. [Verify] Check Geometry Spreadsheet to confirm `v` attribute now exists per point
4. [`Attribute Transfer SOP`] Transfer `v` from blueberry geo onto yogurt surface mesh by proximity
5. [`Attribute Wrangle`] Scale transferred velocity: `@P += @v * ch("scale");` with art-directable parameter
6. [Iterate] Adjust scale and blend to taste; check deformation in viewport
7. [Motion Blur note] Same `v` attribute is used by renderers (Arnold/Mantra) for geometry motion blur

### Houdini Nodes / VEX / Settings
- `Trail SOP` (Compute Velocity) — derives `v` from positional delta between frames without adding actual trail geometry; standard velocity-generation pattern
- `Attribute Transfer SOP` — blends attribute values from source to destination by point proximity and distance falloff
- `Attribute Wrangle` VEX: `@P += @v * ch("scale");` — point-level displacement along velocity direction
- Motion Blur — any renderer reading `v` on geometry uses it for subframe position interpolation; Trail SOP is the standard way to add this

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Tabletop Week 02 Intro](w02-01-introduction-v1-1080p.md) — the week overview introducing this velocity deformation strategy
- [Module I Point Deforming the Metal and Glass](module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md) — post-sim point deformation using similar attribute transfer patterns
- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the next week comparing this fake technique against real FLIP""",
    },

    "w03-04-adding-viscosity-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[flip, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Enabling and tuning viscosity in a FLIP fluid simulation — toggling the viscosity option in the FLIP Solver and setting per-object viscosity values in the FLIP Object's Physical tab, with a workflow for later importing per-point viscosity attributes for multi-fluid scenarios.

### Summary
Starting from a too-watery chocolate fluid, the instructor walks through the exact steps to add viscosity: first enabling it in the FLIP Solver, then navigating to the FLIP Object and setting a viscosity value (e.g. 100) in the Physical tab. The resulting sim shows visibly thicker, slower flow. The instructor previews the future step of importing per-point `viscosity` attribute from outside the DOP network to support multiple fluid types with different viscosities in one sim.

### Key Steps
1. [`FLIP Solver`] Enter the solver; navigate to the Viscosity tab and check "Enable Viscosity"
2. [`FLIP Object` > Physical tab] Set the Viscosity parameter to an initial value (e.g. 100)
3. [Playback] Run sim and observe thicker flow behaviour
4. [Iterate] Try values between 50-5000 to find desired thickness for chocolate
5. [Ground plane] Hide ground plane for cleaner preview
6. [Future step noted] Connect an external `viscosity` point attribute via FLIP Source for per-fluid variation
7. [Verify] Confirm fluid stacks and slows convincingly for a food-shot look

### Houdini Nodes / VEX / Settings
- `FLIP Solver` > Viscosity tab > Enable Viscosity — must be checked; without it the viscosity value on the object has no effect
- `FLIP Object` > Physical > Viscosity — global viscosity for the object (cP-like units); 0 = water, 100 = thick chocolate, 5000+ = very stiff
- Per-point `viscosity` attribute — advanced workflow: set `viscosity` per emitter point externally and import via FLIP Source to override the global value

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the week overview motivating this viscosity work
- [Viscosity and Surface Tension](w04-11-viscosity-and-surface-tension-v1-1080p.md) — expanded treatment in week 4
- [Small Scale Fluids](small-scale-fluids.md) — reference for FLIP viscosity in small-scale contexts""",
    },

    "w03-11-meshing-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[flip, volumes, sop, rendering, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Converting FLIP particle points to a render-ready polygon mesh using a VDB workflow: VDB from Particles -> VDB Smooth SDF -> Convert VDB, with careful voxel size and radius scale tuning to produce a clean mesh that separates distinct fluid layers.

### Summary
The instructor builds the particle-to-mesh pipeline from scratch, troubleshooting VDB from Particles settings (voxel size and radius scale) until a visible level set appears. VDB Smooth SDF is then applied to remove particle-level roughness. Convert VDB extracts a polygon mesh. The key insight is that tuning voxel size to a very small value (0.025) in combination with VDB smoothing produces a mesh clean enough for a food close-up render, and distinct VDB layers can be produced per fluid group to keep sauces separate.

### Key Steps
1. [`VDB from Particles`] Connect FLIP particle output; set Voxel Size (try 0.1 -> 0.025) until a surface appears
2. [Radius Scale] Tune Radius Scale (try 1.5 -> 1.0) if the default produces nothing
3. [`VDB Smooth SDF`] Connect downstream; default settings remove particle-level noise
4. [`Convert VDB`] Extract polygon mesh from the smoothed SDF level set
5. [Per-fluid separation] Use a Blast/Group to separate fluid by group; run VDB pipeline per fluid for distinct meshes
6. [Verify] Check mesh in viewport; confirm smooth continuous surface with no popping or holes
7. [Output] Feed polygon mesh into shading/rendering network

### Houdini Nodes / VEX / Settings
- `VDB from Particles` — converts point clouds to VDB level sets; Voxel Size (smaller = more detail, slower) and Radius Scale (minimum 1.0 recommended by Houdini) are the two critical parameters
- `VDB Smooth SDF` — Gaussian or mean-curvature flow smoothing on a signed distance field; reduces noise without collapsing thin features
- `Convert VDB` — extracts polygons from a VDB SDF; default Adaptivity=0 gives uniform quads
- Layer separation — processing separate fluid groups through independent VDB pipelines keeps sauce colours/shaders distinct

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Tabletop Week 03 Intro](w03-01-introduction-v1-1080p.md) — the week overview that introduces this meshing step
- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — week 4 also uses VDB meshing for the milk pour
- [Small Scale Fluids](small-scale-fluids.md) — FLIP meshing reference for small-scale setups""",
    },

    "w04-11-viscosity-and-surface-tension-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 18"',
            'tags': '[flip, simulation, dop, attributes, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Tuning FLIP fluid viscosity and surface tension parameters together to achieve realistic milk splash behaviour — using jitter seed animated with `$F` for non-repeating emitter variation, then adjusting surface tension to create cohesive droplet crowns.

### Summary
Starting from a chaotic, formless splash, the instructor adds structured fluid behaviour by combining viscosity (light, for milk) and surface tension. The jitter seed on the FLIP Source is animated with `$F` so initial particle positions vary per frame, preventing grid patterns. A simple isolated DOP network is built to demonstrate the viscosity and surface tension interaction clearly. Surface tension creates the cohesive forces that hold milk droplets together into a crown shape, turning a chaotic spray into a photogenic food-shot splash.

### Key Steps
1. [`FLIP Source`] Navigate to the FLIP Source; locate Jitter Seed parameter
2. [Animate Jitter Seed] Set Jitter Seed expression to `$F` so variation changes each frame
3. [Jitter Scale] Set Jitter Scale to 1 for natural variation; 0 would produce a grid
4. [Isolated test network] Build a minimal DOP network to test viscosity and surface tension in isolation
5. [`FLIP Solver` > Viscosity] Enable and set low viscosity (~5-20) for milk
6. [`FLIP Solver` > Surface Tension] Enable surface tension; increase value until droplets and crown form
7. [Iterate] Flip-book and compare; surface tension too high collapses the fluid, too low makes it chaotic
8. [Apply to main network] Transfer confirmed values back to the main sim

### Houdini Nodes / VEX / Settings
- Jitter Seed (`$F`) — animated seed on FLIP Source prevents repeating particle grid patterns per frame
- Jitter Scale — controls magnitude of per-particle position randomisation; 0 = perfect grid, 1 = natural scatter
- `FLIP Solver` > Surface Tension — adds cohesive force between particles; value range typically 0.01-1.0 for water-like fluids; creates crown splashes and hanging droplets
- `FLIP Solver` > Viscosity — low values (1-20) for water/milk; works in conjunction with surface tension

### Difficulty
Intermediate

### Houdini Version
Houdini 18 (Tabletop Food Simulation course)""",
        'related': """- [Tabletop Week 04 Intro](w04-01-introduction-v1-1080p.md) — the week overview introducing viscosity and surface tension for the milk pour
- [Adding Viscosity to FLIP](w03-04-adding-viscosity-v1-1080p.md) — the week 3 viscosity introduction this builds on
- [Small Scale Fluids](small-scale-fluids.md) — reference for FLIP surface tension in small-scale setups""",
    },

}

if __name__ == "__main__":
    for slug, data in EXTRACTIONS_PART2.items():
        path = os.path.join(BASE, slug + ".md")
        if not os.path.exists(path):
            print(f"  MISSING: {path}")
            continue
        update_file(path, data['fm'], data['notes'], data['related'])
    print(f"\nDone: {len(EXTRACTIONS_PART2)} files processed.")
