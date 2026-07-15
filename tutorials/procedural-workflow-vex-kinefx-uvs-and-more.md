---
title: Procedural workflow | Vex, Kinefx, UV's and more
source: YouTube
url: https://www.youtube.com/watch?v=T7CoIJg8Dx4
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.734"
tags: [uvs, kinefx, vellum, xyzdist, vex, scatter, sprinkles, cupcake, food]
extraction_status: complete
frames_dir: tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural workflow | Vex, Kinefx, UV's and more

**Source:** [YouTube](https://www.youtube.com/watch?v=T7CoIJg8Dx4)
**Author:** cgside
**Duration:** 2m47s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this video I'll show you a few procedural techniques in Odini.
[0:04] The full scene is available on Patreon by the way.


### Create masks and sort points with uv's [0:07]
**Transcript (timestamped):**
[0:07] The first one is on how useful UVs can be besides the default purpose.
[0:13] So selecting a sim group and flattening the UVs.
[0:16] Then I need the mask around my object for that I can simply use the U component of the UV attribute.
[0:23] So along the X axis.
[0:26] After that I can easily displace my GU along the mask with the Alp of Cine.
[0:32] Another useful feature with UVs is two sword points.
[0:36] In here I am using it to sort along the U component so I can easily select rings around my GU.
[0:43] Without it the point sword is all messed up.
[0:46] And I am sorting again this time by the V component of the UVs or along Y.
[0:53] Otherwise I would get alternating vertex orders when converting the rings to curves,
[0:59] which leads to several issues when working with rings.


### falloff mask for kinefx [1:03]
**Transcript (timestamped):**
[1:03] So as you can see I have this fall of effect on Marie and that is pretty simple to create.
[1:09] Basically using the XYZDist function we create a fall of from the starting primitives.
[1:16] Then just use a ramp to adjust it.
[1:18] I created this icing with a spiral and a sweep node.


### Vellum stick on collision [1:19]
**Transcript (timestamped):**
[1:23] And now I want to integrate it with the cake.
[1:26] See sitting right on top.
[1:28] For that I am setting up a basic valum seam where I let it rest on top of the collision GU.
[1:36] But as you can see it's sticking and not sliding on the collision GU.
[1:41] And in order to where I shift that inside the solver I am creating some valum constraints
[1:47] that evaluate each frame set to attach with a small distance.
[1:51] That way it sits perfectly on top without sliding.


### Slope mask with dot product [1:57]
**Transcript (timestamped):**
[1:57] As you can see I have some sprinkles on top of the icing.
[2:02] And I am placing it only where interior makes sense.
[2:06] By using the dot product between the normals and the effectors set to Y
[2:12] then just scattering on those areas.
[2:14] So you can easily get random rotations by using the attribute adjust vector node.


### Random rotations made easy [2:15]
**Transcript (timestamped):**
[2:20] In this case I am randomizing the app vector.
[2:23] But since the sprinkles have some bend and it is always facing the same direction
[2:29] I also added another one to rotate the normals around the app vector.


### Outro [2:37]
**Transcript (timestamped):**
[2:37] And that was it.
[2:38] Let me know if you learned something new in the comments and make sure to check out the file on Patreon.
[2:43] Thank you.



---

## Captured Frames

- [0:10] tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/frame_000.jpg
- [0:40] tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/frame_001.jpg
- [1:10] tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/frame_002.jpg
- [1:40] tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/frame_003.jpg
- [2:10] tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/frame_004.jpg
- [2:30] tutorials/frames/procedural-workflow-vex-kinefx-uvs-and-more/frame_005.jpg

---

## Structured Notes

### Core Technique
Five compact tricks for a cupcake shot: using flattened UVs (U/V components) as procedural masks and reliable ring-sorting keys, an `xyzdist()`-driven KineFX falloff for a spiral icing rig, a per-frame Vellum "attach" constraint to keep the icing glued (not sliding) on its collision geometry, a dot-product-based slope mask for placing sprinkles only on upward-facing icing, and an easy random-rotation recipe combining two Attribute Adjust Vector nodes.

### Summary
UVs are shown to be useful beyond texturing: after flattening UVs on a selected seam group, the **U component** of the UV attribute becomes a ready-made X-axis mask for displacing geometry (fed through a ramp for shaping). The **V/U components** also make excellent **Sort Points** keys — sorting by U lets you cleanly select "rings" around the cupcake, and sorting again by V prevents the alternating-vertex-order problem that otherwise breaks ring-to-curve conversion. A spiral icing rig uses **KineFX** with an `xyzdist()`-based falloff from the starting primitives, shaped further with a Ramp; the icing shape itself is built from a spiral curve fed into a Sweep node. To make the icing sit on the cake without sliding once simulated with Vellum, a per-frame-evaluated Vellum constraint set to **"attach"** with a small distance keeps it glued in place on the collision geometry (a plain rest-on-top setup slides otherwise). Sprinkles are placed only where visually sensible using a **dot product between the icing's normals and a Y-axis effector vector** as a slope mask, then scattering points only within that masked region. Random sprinkle rotation is achieved simply: one **Attribute Adjust Vector** node randomizes the up-vector, and a second one rotates the normals **around** that up-vector — necessary because the sprinkle geometry has an inherent bend and would otherwise always face the same direction regardless of the first randomization.

### Key Steps
1. **UV-as-mask**: select a seam group, flatten UVs, then use the **U component** of the UV attribute as a ready-made mask along the X axis to displace geometry (through a ramp for shaping).
2. **UV-as-sort-key**: use **Sort Points** with the point sort mode set to sort **by attribute** on the U component to cleanly select rings around the object; without this, point order is effectively random.
3. Sort again by the **V component** before converting rings to curves — otherwise adjacent rings get alternating vertex winding order, breaking downstream curve-based operations.
4. **KineFX falloff icing rig**: use `xyzdist()` to compute a falloff distance from the rig's starting primitives, shape it with a **Ramp**; build the icing geometry from a spiral curve fed into a **Sweep** node.
5. **Vellum "stick, don't slide" fix**: when simulating the icing resting on the cake with Vellum, a basic setup slides; add a Vellum constraint set to **"attach"**, evaluated **each frame**, with a small distance value, so the icing stays glued exactly where placed instead of sliding off.
6. **Slope mask for sprinkles**: compute the **dot product between the icing's surface normals and a Y-axis effector vector** to build a mask that's only "true" on upward-facing areas, then Scatter points restricted to that masked region.
7. **Easy random rotations**: use one **Attribute Adjust Vector** node to randomize the up-vector attribute, then a second **Attribute Adjust Vector** to rotate the normals **around** that same up-vector — needed because sprinkle geometry with an inherent bend would otherwise always face one fixed direction even after the first randomization.

### Houdini Nodes / VEX / Settings
Group (seam selection), UV Flatten, UV-component masking (U/V), ramp shaping, Sort (point sort by attribute — U then V components), KineFX rig, `xyzdist()` VEX function (falloff distance), Ramp, spiral Curve + Sweep (icing geometry), Vellum Constraint ("attach" type, per-frame evaluation, small distance), dot-product slope mask (normal · Y-axis effector), Scatter (masked region), Attribute Adjust Vector (×2 — up-vector randomization + normal rotation around up-vector).

### Difficulty
Intermediate (each tip is compact and standalone; the KineFX falloff rig and Vellum attach-constraint fix are the more advanced items).

### Houdini Version
20.5.734 (visible in viewport title bar).

### Tags
uvs, kinefx, vellum, xyzdist, vex, scatter, sprinkles, cupcake, food

---

## Related Tutorials
- [Procedural Duct Tape in Houdini](procedural-duct-tape-in-houdini.md) — likely shares the UV-as-mask / ring-sorting technique from the same channel.
- [KineFX and Vellum Fluid in Houdini](kinefx-and-vellum-fluid-in-houdini.md) — related KineFX + Vellum combination technique from the same channel.
