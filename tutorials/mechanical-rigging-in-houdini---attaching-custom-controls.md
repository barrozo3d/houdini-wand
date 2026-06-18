---
title: Mechanical rigging in Houdini - Attaching custom controls
source: YouTube
url: https://www.youtube.com/watch?v=7J-hDF0H6ck
author: cgside
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["kinefx", "rigging", "controls", "mechanical", "joints", "sop", "procedural-rigging"]
extraction_status: complete
frames_dir: tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/
frame_count: 4
---

# Mechanical rigging in Houdini - Attaching custom controls

**Source:** [YouTube](https://www.youtube.com/watch?v=7J-hDF0H6ck)
**Author:** cgside
**Duration:** 13m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, we'll do the remaining of the packing in a bit. For now, let's attach some controls to this. So, for that, I'm going to create in here an add node and create two points. Or we can do a point generate and generate two points. Just to be different, they will be at the origin. I can see them. Why I can see my grid? Okay. Press H. Uh let's do a name. And let's name point zero as target left and point one as target right. And make sure we set it to points, of course. Now, we will need uh rig doctor because this will also be transformed. Let's initialize transforms. And now, let's just create the sphere, set it to primitive. And I'm going to change the size to be 0.05. Give it a color. Can be this kind of blue. You can pick any shape. Let's just name it. And these ones need to be on primitives. Let's name it to control. Now, let's do an attach control. Not attach control, it's attach joint geo. Joint geo. And let's make sure we don't want the rest pose. So, let's connect these and these. And let's attach the name target left to control. So, let's just do up. And we have two points. If we want a different control for each one, you can pick or a different sh...

**Frame:** tutorials\frames\mechanical-rigging-in-houdini---attaching-custom-controls\frame_000.jpg


---

## Structured Notes

### Core Technique
Attaching custom control shapes to joints in a KineFX mechanical rig using the Attach Joint Geo SOP — creating named control points with custom geometry shapes that travel with the rig transforms.

### Summary
This cgside tutorial demonstrates the practical process of attaching custom control shapes to a mechanical rig in Houdini using KineFX SOP-level rigging. The workflow uses Add SOP or Point Generate to create named target points, initializes transforms with Rig Doctor, creates custom control geometry (sphere, any shape), and connects everything through the Attach Joint Geo node. The tutorial shows how to name controls, assign them to specific joints (target_left, target_right), assign colors, and set up the rig so controls transform correctly with the skeleton. It is a focused, hands-on tutorial within a larger mechanical rigging series.

### Key Steps
1. Create named target points using Add SOP or Point Generate (set to points, not primitives)
2. Name points via Name SOP — e.g., "target_left" and "target_right"
3. Use Rig Doctor SOP to initialize transforms on the target points
4. Create control shape geometry (sphere, box, or custom) and set it as a primitive
5. Assign a color to the control for visual identification
6. Name the control geometry using Name SOP on primitives
7. Connect everything through the Attach Joint Geo SOP
8. Disable "rest pose" in Attach Joint Geo settings
9. Link each named control shape to the corresponding joint name
10. Verify the controls transform correctly with the rig

### Houdini Nodes / VEX / Settings
- Add SOP / Point Generate SOP
- Name SOP (point and primitive naming)
- Rig Doctor SOP (initialize transforms)
- Sphere SOP (control shape)
- Attach Joint Geo SOP
- KineFX skeleton workflow
- Rest pose parameter (disabled)

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
kinefx, rigging, controls, mechanical, joints, sop, procedural-rigging

---

## Related Tutorials
- [Tuna Can | procedural modeling and rig with KineFX](tuna-can-procedural-modeling-and-rig-with-kinefx.md) — by same author (cgside), procedural modeling and KineFX rigging of a tuna can object
- [Procedural Growth with KineFX and the Labs Tree Tools](procedural-growth-with-kinefx-and-the-labs-tree-tools.md) — KineFX used for procedural tree rigging and animation
- [Character Design and Modeling](character-design-and-modeling.md) — character geometry creation that would need rigging as a next step
