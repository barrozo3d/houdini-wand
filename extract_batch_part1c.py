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

EXTRACTIONS_C = {

    # ── Renascence 2.0 — Module II intros ──────────────

    "module-ii-week-01-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, cloth, simulation, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Introducing the Vellum-focused Module II with a crocodile-attack scene, rapidly demonstrating cloth, tetrahedral soft bodies, string/wires and grains in a single solver to show Vellum's range.

### Summary
Project: a crocodile attack scene where a hunter is grabbed in the crocodile's mouth. Vellum is praised for being fast and versatile, handling cloth, string, hair, soft bodies and grains all in one solver. Week 1 is a rapid overview demonstrating cloth, soft bodies (tetrahedral constraints), string/wires and grains in a single lesson. The full project pipeline simulates the soft-body hunter (tetrahedral Vellum) together with cloth (the hunter's clothes) in one pass, then adds grains separately as a post-sim effect using the Vellum result as a collider. Introduces the Vellum sub-solver concept: a multi-step position-based-dynamics process that resolves constraints iteratively.

### Key Steps
1. [Cloth] Quick demo of Vellum cloth constraints
2. [Soft body] Quick demo of tetrahedral Vellum constraints
3. [String/wire] Quick demo of Vellum string/wire constraints
4. [Grains] Quick demo of Vellum grains
5. [Pipeline plan] Combine soft-body hunter + cloth clothes in one sim; add grains afterward using the Vellum result as a collider
6. [Sub-solver] Note the Vellum sub-solver as the iterative constraint-resolution mechanism shared by all types

### Houdini Nodes / VEX / Settings
- Vellum (single solver) — handles cloth, string, soft body and grains together with shared collision
- Vellum sub-solver — multi-step position-based-dynamics iteration that resolves constraints within each timestep
- Pipeline order — soft body + cloth simulated together first; grains added as a separate post-sim pass colliding against that result

### Difficulty
Intermediate

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)""",
        'related': """- [Introduction to Vellum: Cloth/String/Grain Fundamentals](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — the deep-dive gap-filler for the techniques previewed here
- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — the following week's cloth-specific focus
- [Tetrahedral Soft Bodies](module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md) — the gap-filler detailing the soft-body setup for the hunter""",
    },

    "module-ii-week-02-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, cloth, simulation, intermediate, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Cloth draping workflow: fitting clothing to the body in T-pose before simulation, with remeshing, constraint grouping, tearing and stitching covered as the week's core Vellum cloth techniques.

### Summary
Workflow begins by draping cloth in T-pose: fitting the clothing geometry to the body before the main simulation so clothing sits correctly at frame 0. Geometry preparation includes a Remesh SOP to triangulate cloth (Vellum produces more natural folds on triangles), group creation for constraint regions, and pre-fracturing cloth with cut lines ready for the simulation to tear along. Key Vellum cloth techniques covered: weld constraints (stitching seams), attachment constraints (pinning cloth to the body), tearing (enabling a break threshold on cloth constraints), and the Vellum sub-solver for draping in rest pose. A bonus topic covers handling cloth intersection at the start of simulation.

### Key Steps
1. [T-pose drape] Fit clothing geometry to the body before the main simulation begins
2. [`Remesh SOP`] Triangulate cloth geometry for natural Vellum folding
3. [Group creation] Define constraint regions (e.g. seams, pin areas) via groups
4. [Pre-fracture cut lines] Add tear lines to the cloth ahead of simulation
5. [Weld constraints] Stitch seams together
6. [Attachment constraints] Pin cloth to the body where needed
7. [Tearing] Enable break threshold on selected cloth constraints
8. [Intersection handling] Resolve cloth/body intersection present at simulation start

### Houdini Nodes / VEX / Settings
- `Remesh SOP` — triangulates cloth for better Vellum fold behaviour
- Vellum weld constraints — stitches seams together
- Vellum attachment constraints — pins cloth to underlying body geometry
- Break threshold (tearing) — enables cloth constraints to fail and tear under stress
- Vellum sub-solver — used here specifically for draping cloth into rest pose before the main sim

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)""",
        'related': """- [Vellum Module Intro: Crocodile Attack Overview](module-ii-week-01-01-introduction-v1-1080p.md) — the preceding week's broader Vellum overview
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the following week's combined cloth+soft-body assembly
- [Breaking Welds and Constraints](module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p.md) — the gap-filler detailing animated constraint breaking for this same cloth setup""",
    },

    "module-ii-week-03-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, cloth, simulation, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Assembling all Vellum elements into one simulation by point-deforming the part of the hunter's body inside the crocodile's mouth to follow the jaw animation directly, avoiding collision-explosion artifacts while the rest of the body simulates as a true soft body.

### Summary
Week 3 brings everything together into a single simulation. The key technique is point-deforming the hunter body to follow the crocodile mouth animation: the inner part of the body, inside the croc's mouth, is not simulated — it simply follows the croc mouth's deformation, preventing collision-explosion artifacts when the mouth closes on the body. Only the body parts outside the croc's mouth actually simulate as soft bodies. A constraint pins the body part inside the mouth to the croc jaw geometry using Vellum attach-to-geometry constraints. Cloth (shirt, pants, boots) is layered on top of this soft-body setup, with proper collision detection between cloth-to-soft-body and cloth-to-croc geometry.

### Key Steps
1. [`Point Deform`] Make the in-mouth portion of the hunter body follow the croc jaw animation directly (not simulated)
2. [Vellum attach-to-geometry] Pin the in-mouth body region to the croc jaw geometry
3. [Soft-body sim] Simulate only the body parts outside the croc's mouth as true Vellum soft bodies
4. [Layer cloth] Add shirt/pants/boots cloth on top of the soft-body setup
5. [Collision setup] Configure cloth-to-soft-body and cloth-to-croc collision detection
6. [Verify] Confirm no collision explosion occurs as the croc mouth closes on the body

### Houdini Nodes / VEX / Settings
- Point Deform (non-simulated region) — used to prevent collision-explosion artifacts at hard mouth-closure contact
- Vellum attach-to-geometry constraint — pins the point-deformed body region to the animated croc jaw
- Layered Vellum collision — cloth, soft body and croc geometry all collide within the same solver pass

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)""",
        'related': """- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — the preceding week's cloth-specific techniques layered on here
- [Tetrahedral Soft Bodies](module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md) — the soft-body setup being combined with cloth in this lesson
- [Vellum Grains: Source from Sim](module-ii-week-04-01-introduction-v1-1080p.md) — the following week's grains pass built on this combined sim""",
    },

    "module-ii-week-04-01-introduction-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, particles, rendering, karma, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Sourcing grains from the contact regions of the existing crocodile/hunter Vellum simulation rather than scattering across the whole scene, then up-resing the grain sim for final render quality.

### Summary
The final Vellum week covers grains simulation and full render. The grain-sourcing efficiency trick uses the previous Vellum simulation (crocodile + hunter) to generate a time-varying source volume: as the croc thrashes and the hunter is squeezed, the contact region emits grains, driven by a SOP Solver or DOP stamp inside the grains network. The grain network is built from scratch in DOPs rather than from the shelf tool this time: Vellum Grains Source + Vellum Solver + Vellum Constraint. An up-res technique runs a low-res grain sim first for timing/behaviour, then re-sims at high pscale with finer constraint sub-steps for render-quality results. The final render uses Karma XPU with Megascans materials for ground/mud.

### Key Steps
1. [Contact-driven sourcing] Derive a time-varying grain source volume from the croc/hunter Vellum sim's contact regions
2. [`SOP Solver` / DOP stamp] Drive grain emission timing from the existing sim rather than a fixed scatter
3. [Vellum Grains network] Build from scratch in DOPs: Vellum Grains Source + Vellum Solver + Vellum Constraint
4. [Low-res pass] Simulate grains at low resolution first to confirm timing and behaviour
5. [Up-res pass] Re-simulate at high pscale with finer sub-steps for render quality
6. [Render] Apply Megascans ground/mud materials; render in Karma XPU

### Houdini Nodes / VEX / Settings
- Contact-driven grain sourcing — deriving emission volume/timing from an existing simulation's contact regions rather than static scatter
- Vellum Grains Source / Vellum Solver / Vellum Constraint — built manually in DOPs for full control
- Up-res workflow — low-res timing pass followed by a high-pscale, finer-substep render pass
- Karma XPU — final renderer with Megascans ground/mud materials

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II)""",
        'related': """- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the preceding week's combined sim this grain pass sources from
- [Introduction to Grains](module-i-week-06-01-introduction-to-grains-v1-1080p.md) — the earlier course's foundational Vellum Grains lesson
- [Tabletop Week 01 Intro](w01-01-introduction-v1-1080p.md) — another instancing/particle-heavy render pipeline for comparison""",
    },

    # ── Renascence 2.0 — Module II gap-fillers ───────────

    "module-ii-week-01-02-introduction-to-vellum-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, cloth, particles, intermediate]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
A comprehensive Vellum fundamentals lesson demonstrating cloth, string/wire and grains setups, with the Vellum Solver shown as a single DOP network that resolves all Vellum object types together with shared collision.

### Summary
Setup: a new project "croc_attack" with a "vellum_intro" geometry node. Cloth: grid -> Remesh (to triangulate for better folds) -> Vellum Cloth SOP (via shelf or tab), with bend stiffness, stretch stiffness and mass as the key parameters. Pinning is done by grouping the top edge and attaching it to geometry, or using Vellum Attach to Geometry. String/wire: a curve feeds Vellum String SOP, with wire stiffness distinguishing cable-like from rope-like behaviour. Grains: scattered points feed Vellum Grains SOP, with friction, restitution and pscale as key parameters. The Vellum Solver setup always lives inside a DOP network and reads all Vellum object types together, resolving them with shared collision. Increasing substeps improves accuracy but scales simulation time linearly. The key tip given is to always remesh cloth geometry before Vellum, since quad-dominant meshes produce poor fold quality.

### Key Steps
1. [`Remesh SOP`] Triangulate grid geometry before applying Vellum Cloth
2. [`Vellum Cloth SOP`] Set bend stiffness, stretch stiffness and mass
3. [Pinning] Group the top edge; attach via geometry group or Vellum Attach to Geometry
4. [`Vellum String SOP`] Convert a curve to a wire; tune wire stiffness for cable vs. rope behaviour
5. [`Vellum Grains SOP`] Scatter points; tune friction, restitution and pscale
6. [`Vellum Solver`] Combine cloth, string and grains in one DOP network with shared collision
7. [Substeps] Increase substeps for accuracy, noting the linear cost increase

### Houdini Nodes / VEX / Settings
- `Remesh SOP` — required pre-step for cloth; quad-dominant meshes fold poorly in Vellum
- `Vellum Cloth SOP` — bend stiffness, stretch stiffness, mass
- `Vellum String SOP` — wire stiffness differentiates cable vs. rope behaviour
- `Vellum Grains SOP` — friction, restitution, pscale
- `Vellum Solver` (single DOP network) — resolves all Vellum types together with shared collision; substep count trades accuracy for sim time

### Difficulty
Intermediate

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)""",
        'related': """- [Vellum Module Intro: Crocodile Attack Overview](module-ii-week-01-01-introduction-v1-1080p.md) — the overview lesson this gap-filler expands on
- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — applies these cloth fundamentals to a full draping workflow
- [Introduction to Grains](module-i-week-06-01-introduction-to-grains-v1-1080p.md) — the earlier course's parallel grains-only lesson""",
    },

    "module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, rigging, simulation, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Setting up a Vellum tetrahedral soft body for the hunter character via the Vellum Solid Object shelf tool, with a Poly Reduce proxy mesh tuned to balance simulation speed against recognizable shape.

### Summary
Positions the hunter at X=5 so he sits correctly inside the crocodile's mouth when it closes. Uses the Vellum shelf tool: select the hunter geometry -> Vellum Solid Object (tetrahedral). The shelf automatically adds Poly Reduce (a proxy mesh for speed), Tet Conform, Vellum Solid Object constraints, and a Vellum Solver. A noted problem is that Poly Reduce defaults are too aggressive, over-simplifying the shape — switching to percentage mode at roughly 50% keeps a recognizable shape while still speeding up the sim. Tetrahedral constraints fill the volume with tetrahedra via Tet Conform, and Vellum Solid Object then adds internal constraints connecting all tet vertices, giving volumetric soft-body behaviour (squishing under pressure) rather than surface-only cloth constraints. The key parameter is shape stiffness: very low values produce jelly-like behaviour, high values produce rubber-like behaviour.

### Key Steps
1. [Position] Place the hunter character at X=5 for correct mouth placement
2. [Vellum shelf tool] Select geometry -> Vellum Solid Object (tetrahedral), auto-building the network
3. [`Poly Reduce`] Switch from aggressive default to percentage mode (~50%) for a usable proxy mesh
4. [`Tet Conform`] Fill the volume with tetrahedra
5. [`Vellum Solid Object`] Add internal tet-vertex constraints for volumetric soft-body behaviour
6. [Shape stiffness] Tune between jelly-like (low) and rubber-like (high) behaviour

### Houdini Nodes / VEX / Settings
- `Vellum Solid Object` (shelf tool) — auto-builds Poly Reduce, Tet Conform, constraints and Vellum Solver for tetrahedral soft bodies
- `Poly Reduce` (percentage mode, ~50%) — balances proxy-mesh simulation speed against recognizable shape; default mode is too aggressive
- `Tet Conform` — fills mesh volume with tetrahedra for internal constraint generation
- Shape stiffness — key Vellum Solid Object parameter; low = jelly, high = rubber

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)""",
        'related': """- [Updating the Rest Blend](module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md) — the following lesson re-posing this same soft-body setup
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — combines this soft body with cloth and point-deform
- [Introduction to Vellum: Cloth/String/Grain Fundamentals](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — broader Vellum fundamentals referenced here""",
    },

    "module-ii-week-01-06-updating-the-rest-blend-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, rigging, attributes, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Re-posing a character's arms and blending the new pose into the Vellum solid-body constraints as the rest state, using the `restblend` attribute as a spring-like target-position control without simulating actual muscles.

### Summary
The hunter's arms are raised in a T-pose / gun-holding pose, which looks wrong at rest. The fix is to manually re-pose the arms and blend this new rest position into the Vellum constraints so the solver treats it as the natural rest state. Workflow: group the left and right arms separately using bounding-sphere group mode, apply a Transform SOP per group to lower the arms, then feed this re-posed geometry into the Vellum Solid Object as the rest geometry via the "rest blend" parameter (which blends from the sim-current shape toward the rest shape). The `restblend` float attribute (0-1) controls how strongly the body is attracted back toward the rest pose, acting as a target-position spring. The rest blend is evaluated after each Vellum substep, making it an effective way to add muscle-like stiffness without simulating actual muscles.

### Key Steps
1. [`Group SOP`] Select left arm and right arm separately using bounding-sphere mode
2. [`Transform SOP`] Lower each arm group from the raised T-pose
3. [Rest geometry input] Feed the re-posed geometry into Vellum Solid Object's rest blend input
4. [`restblend` attribute] Set the 0-1 float controlling pull-back strength toward the new rest pose
5. [Verify] Confirm the rest blend is applied after each substep, giving muscle-like stiffness without actual muscle simulation

### Houdini Nodes / VEX / Settings
- `Group SOP` (bounding-sphere mode) — isolates limb regions for independent re-posing
- `Transform SOP` — applies the manual re-pose to lower the arms
- `restblend` attribute (float, 0-1) — Vellum Solid Object parameter blending sim-current shape toward a custom rest shape, evaluated per substep
- Rest-pose blending — a target-position-spring technique for muscle-like stiffness without true muscle simulation

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)""",
        'related': """- [Tetrahedral Soft Bodies](module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md) — the preceding setup this rest-blend correction applies to
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the combined sim using this corrected rest pose
- [Introduction to Vellum: Cloth/String/Grain Fundamentals](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — broader Vellum constraint fundamentals""",
    },

    "module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p": {
        'fm': {
            'houdini_version': '"Houdini 19"',
            'tags': '[dop, vellum, attributes, vex, advanced]',
            'extraction_status': 'complete',
        },
        'notes': """### Core Technique
Dynamically breaking Vellum weld and stitch constraints at specific simulation times using a SOP Solver inside the Vellum DOP network, since break thresholds cannot be keyframed directly on the Vellum nodes themselves.

### Summary
The collar stitch and boot attachment constraints need to break at a specific frame when the crocodile flips the hunter over. Weld breaking is enabled via the "breaking" checkbox on the Vellum Weld node with a break threshold of 1. Because the break threshold cannot be keyframed directly on the Vellum node, a SOP Solver inside the DOP network is required to modify the constraint geometry per frame: a wrangle reads the current frame and lowers the break threshold along a time ramp using `f@breakthreshold = fit($F, start, end, 1.0, 0.01);`. The boot attachment is handled differently — at the specific flip frame, the boot constraints are deleted entirely using a Delete SOP gated on `$F > threshold`, producing a clean instant detach. The general pattern established is that a SOP Solver inside Vellum DOPs is the standard way to animate any Vellum constraint attribute over time.

### Key Steps
1. [`Vellum Weld`] Enable the "breaking" checkbox; set break threshold to 1
2. [`SOP Solver` (inside DOPs)] Add to allow per-frame modification of constraint attributes
3. [`Attribute Wrangle`] Ramp the break threshold down over time: `f@breakthreshold = fit($F, start, end, 1.0, 0.01);`
4. [`Delete SOP`] For the boot attachment, delete constraints entirely when `$F > threshold` for an instant clean detach
5. [Verify] Confirm collar and boot constraints break at the intended flip frame, not before or after

### Houdini Nodes / VEX / Settings
- `Vellum Weld` (breaking enabled) — stitch/weld constraints that can fail once stressed past threshold
- `SOP Solver` (inside DOPs) — required pattern for animating any Vellum constraint attribute, since Vellum nodes don't support direct keyframing
- VEX: `f@breakthreshold = fit($F, start, end, 1.0, 0.01);` — time-ramped threshold reduction
- `Delete SOP` gated on `$F > threshold` — instant clean constraint removal for the boot detach

### Difficulty
Advanced

### Houdini Version
Houdini 19-20 (Renascence 2.0 — Module II, gap-filler)""",
        'related': """- [Cloth Draping Intro](module-ii-week-02-01-introduction-v1-1080p.md) — the cloth setup whose collar stitch is broken here
- [Full Vellum Assembly: Point Deform Body + Pinning](module-ii-week-03-01-introduction-v1-1080p.md) — the week this animated breaking technique supports
- [Setting the Active Attribute](module-i-week-01-09-setting-the-active-attribute-v1-1080p.md) — a parallel time-driven attribute-animation pattern from the RBD context""",
    },

}

if __name__ == "__main__":
    for slug, data in EXTRACTIONS_C.items():
        path = os.path.join(BASE, slug + ".md")
        if not os.path.exists(path):
            print(f"  MISSING: {path}")
            continue
        update_file(path, data['fm'], data['notes'], data['related'])
    print(f"\nDone: {len(EXTRACTIONS_C)} files processed.")
