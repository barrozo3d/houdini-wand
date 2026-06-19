# KineFX & APEX — Character Rigging Reference

Houdini's character system: KineFX (SOP-level skeleton + animation data) and APEX (procedural rigging graph + character packaging). Available from H18+ (KineFX) and H20+ (APEX). Covers rigging, retargeting, simulation, and the full character production pipeline.

---

## Architecture Overview

```
KineFX layer  →  works with skeleton/joint data as SOP geometry
APEX layer    →  procedural graph driving KineFX skeleton
Character Folder  →  packaged structure: skeleton + rig + skin + animation
```

- **KineFX:** joints are geometry points with transform attributes; all SOP tools work on them
- **APEX:** a graph (similar to VOP network) where nodes are rig components; evaluated per-frame
- **Character Folder:** the production-ready package combining both; imported as a single asset

---

## KineFX — Skeleton & Joint SOPs

### Core Skeleton Nodes
| Node | Role |
|------|------|
| `Skeleton SOP` | Create and edit a joint hierarchy interactively in the viewport |
| `Rig Pose SOP` | Interactively pose a character's joints |
| `Rig Doctor SOP` | Diagnose and fix common rig problems |
| `Extract Bone SOP` | Extract individual bones from a skeleton |
| `Skeleton Capture SOP` | Paint capture weights to bind skin geometry to skeleton |
| `Skeleton Deform SOP` | Deform skin geometry using skeleton pose |
| `Skeleton Mirror SOP` | Mirror joint transforms across an axis |
| `Bone Capture Proximity SOP` | Assign weights by proximity (automatic) |
| `Bone Capture Biharmonic SOP` | Biharmonic-based smooth weighting |

### Joint Attribute Conventions
```vex
// Joints are points — access like any SOP geometry
// Key transform attributes:
matrix3 xform = 3@transform;         // local rotation matrix
vector   t    = v@localpos;          // local translation
vector   rest = v@restpos;           // rest-pose position (world)

// Joint name (used for matching across retargeting)
string name = s@name;

// Parent pointer (point number, -1 for root)
int parent = i@parent;
```

### Rest Pose
```
Rig Stash Pose SOP   → capture current pose as "rest"
Rig Match Pose SOP   → match one rig's pose to another by joint names
Rig Vop SOP          → VOP-level access to joint transforms per-joint
```

---

## APEX Rigging

### What APEX Is
APEX is a graph-based rigging system where each node is a "component" (IK limb, FK chain, blend shape, etc.). The graph runs inside a SOP context and outputs a character folder structure.

### Core APEX Nodes
| Node | Role |
|------|------|
| `APEX Autorig Builder SOP` | Interactive viewport tool — drag components onto joints |
| `APEX Graph SOP` | Visual graph editor for the rig network |
| `APEX Configure Graph SOP` | Set constraint/component parameters |
| `APEX Pack Character SOP` | Convert KineFX character → character folder |
| `APEX Unpack Character SOP` | Extract skin, capture pose, animated pose from folder |
| `APEX Scene Animate SOP` | Evaluate character folder at animation time |
| `APEX Bake Animation SOP` | Bake animation from APEX to joint transforms |

### Autorig Builder Workflow (H21)
```
1. Import skeleton geometry (FBX/glTF or hand-built with Skeleton SOP)
2. Place APEX Autorig Builder SOP → enter interactive mode
3. Drag rig component icons onto joints in viewport:
   - Biped Spine, Biped Leg, Biped Arm, Neck, Head
   - Hand (fingers auto-detected), Foot (reverse foot auto-included)
4. Hit Build → APEX Graph SOP generated automatically
5. Add APEX Pack Character SOP → outputs character folder
```

### Autorig Components (H21)
```
limb          — IK/FK arm or leg chain
hand          — full finger rig with spread/cup/fist controls
foot          — reverse foot roll (heel, ball, toe pivot)
neck          — stretch/squash neck chain
scapula       — clavicle simulation driven by arm
ulna          — forearm twist correction
root          — world/hip root with global scale
twist joints  — intermediate twist joints for forearm/upper arm
joint rotate corrective — corrective shapes driven by joint angle
```

### APEX Script
Node-level scripting language for programmatic graph construction:
```python
# APEX Script syntax (runs inside APEX Graph SOP)
# Create a graph function
@subgraph(name="MyRig")
def build():
    # Add a node
    ik_node = apex.node("APEX::Limb")
    # Set parameters
    ik_node.set("start_joint", "shoulder")
    ik_node.set("end_joint", "wrist")
    # Connect
    ik_node.input("skeleton") = input_skeleton
    output_skeleton = ik_node.output("skeleton")
```

---

## Animation Pipeline

### Animation Catalog (H21)
The Animation Catalog saves and reuses animation clips and single-frame poses:
```
Window → Animation Catalog
  → Save current pose as "Pose Asset"
  → Save frame range as "Animation Clip"
  → Apply to character via drag-and-drop in viewport
```

### Motion Mixer (H21)
Timeline tool for blending multiple animation clips:
```
Window → Motion Mixer
  → Add characters and clips
  → Set blend regions with overlap
  → Outputs blended animation sequence
```

### Animation Retargeting
Transfer animation from one skeleton to another:
```
APEX Animation from Skeleton SOP
  → Input 1: source animation (skeletal data)
  → Input 2: target skeleton
  → Matches by joint name — rename joints if skeletons differ
  → Outputs retargeted animation on target skeleton
```

### Animation Layers
```
APEX Scene Animate SOP → "Inherit Animation Layers from Input"
  → Layer 0: base animation
  → Layer 1+: additive corrections, secondary motion
  → Each layer is a separate character folder input
```

### Ragdoll Tethers (H21)
```
APEX Configure Ragdoll SOP
  → Attach ragdoll objects to each other with tether constraints
  → Useful for hair, cloth, and secondary body parts driven by ragdoll
```

---

## Capturing & Skinning

### Workflow
```
1. Skeleton SOP → build joint hierarchy
2. Bone Capture Biharmonic SOP → auto-weight (best quality, slow)
   OR Bone Capture Proximity SOP → proximity-based (fast, manual cleanup needed)
3. Capture Layer Paint SOP → interactive weight painting
4. Skeleton Deform SOP → deform skin using skeleton
```

### Capture Weight Attributes
```vex
// After capture, each point has:
int[]   boneCapture_index   → which bones influence this point
float[] boneCapture_weight  → corresponding weights (sum = 1)

// Access in Point Wrangle:
int[]   idx = i[]@boneCapture_index;
float[] wts = f[]@boneCapture_weight;
```

---

## glTF / FBX Import/Export (H21)

### Import
```
File → Import → FBX / glTF
  → New in H21: GLTF Animation Import, GLTF Character Import, GLTF Skin Import SOPs
  → FBX: "Normalize Joint Scales" + "Remove Namespaces from Joint Names" options
  → Joint Display Scale parameter on all import SOPs
```

### Export to glTF for UE5
```
ROP FBX SOP
  → Output Type: FBX
  → Export Skeleton: enabled
  → Export Skin Weights: enabled
  → Houdini Engine can skip this step — use HDA directly in UE5
```

---

## Full Body IK (H21)

```
Full Body IK Tool (viewport toolbar)
  → Pose by adjusting high-level targets (hands, feet, hips, head)
  → Automatically solves IK for entire skeleton
  → Useful for pose library creation and mocap cleanup
```

---

## Test Characters (H21)

| Character | Description |
|-----------|-------------|
| Otto | Realistic male; biped rig; muscle/skeletal bone geometry; Electra skeleton compatible |
| Electra v2.0 | Updated skeleton; industry-standard twist joints, IK/FK fingers, reverse foot, auto clavicle |

Access: `File → Import → Houdini Test Characters`

---

## Common KineFX Pitfalls

1. **Joint name mismatches** — retargeting and APEX components rely on exact `s@name` matching; check with `Rig Doctor SOP`
2. **Rest pose drift** — always lock rest pose with `Rig Stash Pose SOP` before animating; re-stash after any skeleton edits
3. **APEX vs KineFX mode** — SOPs like `Skeleton Deform` expect KineFX joint geometry, not APEX character folders; use `APEX Unpack Character` first
4. **Weight normalization** — `boneCapture_weight` must sum to 1.0 per point; use `Normalize Weights SOP` if painting manually
5. **H20 vs H21 APEX API** — `APEX Edit Graph SOP` renamed to `APEX Graph SOP` in H21; `APEX Rigscript Component SOP` deprecated

---

## Related Reference Files
- `references/dop-nodes.md` — Vellum cloth/wire for secondary motion on rigs
- `references/sop-nodes.md` — SOP tools used in capture/deform pipeline
- `references/release-notes-h21.md` — Full H21 KineFX/APEX changelog
- `references/release-notes-h20-5.md` — H20.5 APEX Script introduction
- `recipes/rbd-destruction.md` — Ragdoll + RBD for destruction involving characters
