---
title: Procedural Hard Surface Modeling Tips
source: YouTube
url: https://www.youtube.com/watch?v=pTQGJM0k9b0
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.310"
tags: [hard-surface, boolean, vex, procedural-modeling, uvs, attribute-blend, tapering]
extraction_status: complete
frames_dir: tutorials/frames/procedural-hard-surface-modeling-tips/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Hard Surface Modeling Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=pTQGJM0k9b0)
**Author:** cgside
**Duration:** 2m35s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there, let's see how to solve some problems with procedural modeling.
[0:05] This scene file is on Patreon by the way.
[0:08] The first issue I faced in this small project was on how to remove alpha of the left tube
[0:14] in a non-disruptive way.


### Removing Left Tube [0:15]
**Transcript (timestamped):**
[0:16] So the solution is actually pretty simple, first I am computing the UVs of the sweep nodes,
[0:21] then I can get the boundary of the UV attribute.
[0:25] From there, expand the selection and promote it to primitives.
[0:30] Invert the group and then splitting it or blasting well though.


### tapering [0:34]
**Transcript (timestamped):**
[0:35] Now to create this tapering effect, I am using the Curveo attribute previously saved.
[0:41] So in a point 4, I am mixing between the current geometry with 1 with a peak.
[0:48] And as the mixing factor, I am using the Curveo and playing with the values of the feed range
[0:54] to have the desired transition.
[0:56] And since I don't want the effect on the right shape, I am overriding the Curveo in there.


### removing arch transition [1:02]
**Transcript (timestamped):**
[1:03] In this part of the model, I wanted to get rid of the R's transition.
[1:08] So for that, I am extracting the seams group from the Boolean and promoting it to points.
[1:15] Then creating a attribute and blur it.
[1:18] And the only thing left to do is to use that mask in a attribute blur as a white factor.


### rounding [1:24]
**Transcript (timestamped):**
[1:25] To make the top part rounded, I am promoting a previously saved group to primitives and
[1:30] expanding it.
[1:33] Extrusting that part, then create a bound and get only the primitive zero.
[1:38] Bevel the top left corner and now we can extend it and Boolean the initial shape with it.
[1:45] Now let's look at the attribute blend to create this inset extrusion.
[1:50] I have the initial curves with the normals along the tangents and transfer them to the geometry,
[1:57] renaming or swapping the normals by N2 and reversing them in the smaller shape.
[2:03] Calculating the new normals, pointing in by reversing them, and finally blend the two
[2:09] normals with an attribute combined.
[2:12] You can also use a lurb with wax or vops.
[2:15] Then it's just a matter of extruding those inner edges along the pre-existing normals.
[2:21] So that's about it, so hopefully you got something out of this that you can explore in your
[2:26] next projects.
[2:27] Thank you and see you around.



---

## Captured Frames

- [0:12] tutorials/frames/procedural-hard-surface-modeling-tips/frame_000.jpg
- [0:35] tutorials/frames/procedural-hard-surface-modeling-tips/frame_001.jpg
- [0:55] tutorials/frames/procedural-hard-surface-modeling-tips/frame_002.jpg
- [1:20] tutorials/frames/procedural-hard-surface-modeling-tips/frame_003.jpg
- [1:50] tutorials/frames/procedural-hard-surface-modeling-tips/frame_004.jpg
- [2:20] tutorials/frames/procedural-hard-surface-modeling-tips/frame_005.jpg

---

## Structured Notes

### Core Technique
Five hard-surface modeling problem-solving tips applied to a Y-branch pipe fitting: non-disruptive alpha removal via UV boundary extraction, curve.u-driven tapering with Point-mix, Boolean seam-masked Attribute Blur, primitive-bound-based corner rounding, and normal-blended attribute-combine insets.

### Summary
To remove a tube's end alpha non-destructively, the sweep's UVs are computed, the UV boundary extracted, expanded, and promoted to primitives, then the inverted group is blasted away. A Curveu attribute (saved earlier) drives a tapering effect via a Point VOP mixing the current geometry with a Peaked version, using Fit Range to shape the transition, with the effect suppressed on the opposite branch by overriding Curveu there. Boolean-created ridge transitions are smoothed by extracting the Boolean's seam group, promoting to points, creating and blurring a mask attribute, then using it as the Attribute Blur's weight input. For corner rounding, a saved group is promoted to primitives and expanded, extruded, then a Bound node isolates just primitive 0 so the top-left corner alone can be beveled before extending and Boolean-ing it into the main shape. Finally, an inset-extrusion look is built via Attribute Blend: curve normals are transferred to the geometry (renamed N2, reversed on the smaller shape), a second reversed-inward normal is calculated, and the two are blended with Attribute Combine (or a VEX/VOP lerp) before extruding the inner edges along the blended normals.

### Key Steps
1. **Non-disruptive alpha removal**: compute UVs on the Sweep node, extract the UV boundary attribute's edge group, expand the selection, promote to primitives, invert the group, then Blast (or Split) to remove the unwanted end alpha cleanly.
2. **Tapering via Curveu**: using a previously saved Curveu attribute, mix the current geometry with a Peaked version in a Point VOP/wrangle, using the Curveu value as the blend factor; shape the transition with Fit Range; override Curveu to a constant on the opposite branch to suppress the effect there.
3. **Removing Boolean ridge transitions**: extract the seams group produced by the Boolean, promote it to points, create a mask attribute from it and blur it, then feed that blurred mask as the **weight** input of an Attribute Blur to smooth the ridge without affecting the rest of the geometry.
4. **Rounding a corner**: promote a previously saved group to primitives and expand it, extrude that part, then use a **Bound** node and keep only primitive 0 so a single top-left corner can be isolated, beveled, extended, and Boolean-ed back into the main shape.
5. **Inset-extrusion via normal blending**: transfer curve normals (with tangents) onto the geometry, rename/swap them to `N2`, reverse them on the smaller inner shape; calculate a second set of normals pointing inward by reversing them; blend the two normal sets with **Attribute Combine** (VEX or VOP `lerp` also works); finally extrude the inner edges along the blended normal to produce a smooth inset look.

### Houdini Nodes / VEX / Settings
Sweep (UV computation), Group (UV boundary, expand, promote to primitives), Blast/Split, Point VOP (Curveu-driven Peak mix, Fit Range), Boolean (seam group extraction), Attribute Promote, Attribute Blur (weight-driven by mask), Bound (single-primitive isolation), Bevel, Extrude, Boolean (corner integration), Attribute Transfer (curve normals + tangents), attribute rename/swap (N → N2), Attribute Combine (normal blending, VEX or VOP lerp), Extrude (inset along blended normal).

### Difficulty
Intermediate–Advanced (each tip solves a specific, non-obvious hard-surface modeling problem; assumes comfort with groups, Booleans, and attribute-level VEX/VOP work).

### Houdini Version
20.5.310 (visible in viewport title bar).

### Tags
hard-surface, boolean, vex, procedural-modeling, uvs, attribute-blend, tapering

---

## Related Tutorials
- [Hard Surface Techniques in Houdini](hard-surface-techniques-in-houdini.md) — related hard-surface problem-solving techniques (UV-as-position flattening, VEX orient-to-point) from the same channel.
- [Direct vs Procedural in Houdini](direct-vs-procedural-in-houdini.md) — shares similar sign/modulo and group-based selection tricks for hard-surface work.
