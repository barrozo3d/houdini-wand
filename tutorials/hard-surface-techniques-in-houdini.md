---
title: Hard Surface Techniques in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=qtzO_NoQbtE
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, vex, vellum, hard-surface, procedural, subdivision, tips, advanced]
extraction_status: complete
frames_dir: tutorials/frames/hard-surface-techniques-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Hard Surface Techniques in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=qtzO_NoQbtE)
**Author:** cgside
**Duration:** 10m22s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So I decided to model this object in Odini that is by the artist CG gear in art station.
[0:10] As you can see this is the original object. And I decided to model it in Odini to see what the challenges were.
[0:21] And I've got some tips that I want to share with you guys today.


### 3D clip on curved surfaces [0:26]
**Transcript (timestamped):**
[0:27] So for the cloud pads I have these sections in here.
[0:32] And the way I'm doing that is after the basic extruding and beveling I am blasting as a group.
[0:43] And then I'm selecting this in this case you can ignore this range.
[0:49] And what I'm doing in here is creating an image reboot for each 8 primitives.
[0:58] So dividing the primnum by 8. But since I want them aligned in a specific order I am also sorting, so shifting by 4.
[1:09] So I have them in the correct position. So just shift the primitive order.
[1:16] Then in a loop I am creating this setup in here. So for each named primitive I am creating a rest position.
[1:27] Then selecting the bottom and converting it to vertices and doing some UVs with the UV flatten.
[1:38] Then I promote the UVs to points and I assign to the position the UV attribute.
[1:45] So I can have it flat. That way I can use a box clip to clip part of it which wouldn't be really possible with curved surface as you can see.
[1:58] So basically I want to clip the sides and that's what I'm doing in here with this box clip.
[2:07] Then I am again extracting the rest position and sending it back to the original position as you can see it's curved.
[2:17] But now it is clipped.
[2:22] Then just doing a quad remesh and re-project it.
[2:27] So it keeps the same position let's say.
[2:31] Because with the quad remesh it softens a bit the shape.
[2:36] Then I am using a ray to align it better to the original position.
[2:43] So that's basically it.


### Randomizing vellum cloth patterns [2:46]
**Transcript (timestamped):**
[2:48] Now for this slot seam I have identical parts as you can see.
[2:55] So they would end up giving the same exact pattern if I show you in here the version one.
[3:03] As you can see they have almost the same pattern which is not nice and doesn't resemble our reference.
[3:12] So as you can see in this second version they no longer have the same patterns.
[3:19] They are slightly different at least different enough as you can see.
[3:27] And the way I'm doing that is by creating a bend stiffness attribute before the seam.
[3:35] With the noise pattern as you can see just changing the min value to not be zero and the element size.
[3:46] And then in the volume cloth I am assigning to the bend stiffness scaled by attribute and using that attribute in here.
[3:55] And that way I can get a slightly different result on each pad.
[4:04] So for this specific object I am using the exercise quad remeshier.


### Quad remesh control by groups [4:05]
**Transcript (timestamped):**
[4:11] And if I show you an option in here use primitive groups boundaries.
[4:16] If I disable this you can see I will get corners all jacked up.
[4:22] And if I enable it you can see how clean this looks and how useful it can be.
[4:31] Because before that I had basically this result which is not nice for subdividing it.
[4:41] So the way I'm doing those basically this is using all the primitive groups that you have before the quad remeshier.
[4:50] And it will use them to split the quad remeshier let's say.
[4:57] So I have a Boolean and from there I can create a group using the min edge angle.
[5:04] As you can see to select the art edges let's say.
[5:08] Then I'm doing an edge concept of those edges so separating the mesh by edges.
[5:14] Then I can use a connectivity of course and I will have a different class for each of those primitives.
[5:26] Then I can do a group from name and use the class attributes and give it in a prefix.
[5:34] Deleting any groups that are not in those that I set here.
[5:41] Fusing the points and then doing the quad remesh.
[5:46] And as you can see that gives a pretty good result that we can later combine
[5:54] and get something like this.


### Crease corners in Houdini [6:00]
**Transcript (timestamped):**
[6:01] So coming back to the objects I have these art corners in here, these sharp corners.
[6:08] And I would like to subdivid it.
[6:11] And if I subdivided I will get these rounded corners.
[6:18] And because I have these inner extrusion in here, these insets.
[6:25] So the way I'm avoiding that I'm group combining some of the edges, mostly the corner edges.
[6:33] And then I'm doing a crease on that group and increase it quite a bit.
[6:40] Then when I'm subdividing, I won't get that rounded corner look.
[6:48] And also I will get a smooth transition in here because I'm not applying the crease on there.
[6:56] But I am applying in here which is totally fine, it's just on the corner, but not in the center or in this rounded part.
[7:05] So that's how you can do the grising.
[7:09] Because if I overwrite the look, you will start to see, let me change the mat cap.
[7:17] You will start to see the low poly look, let's say.
[7:25] And if I remove it, we will get a smooth look.


### Snap orient with vex [7:31]
**Transcript (timestamped):**
[7:31] Okay, in these particular objects I have created these from curves and doing a bridge between the curves.
[7:44] And then I want to boot you out the middle part so as you can see in here.
[7:52] And the way I'm doing that is of course by using a box.
[7:57] But I need to orient it somehow to this point here in the middle that I manually selected.
[8:03] So the way I'm doing that, as you can see, is by using some Vex.
[8:08] And a script that I shared before, just snippets that I shared before here on the channel.
[8:16] And basically I'm taking the, I have a base-prem in here.
[8:21] So as you can see, this primitive in here that I'm more yending to that specific point.
[8:29] So I'm getting the primitive number of that base-prem and getting the normal.
[8:39] Then from this target point in here, I am extracting also the normals and doing a rotation matrix from the base from this polygon in here to the target point normal.
[9:02] And then just getting the position from this point and orienting the box as you can see.
[9:13] You can get a pretty similar result with copy two points, but you will need to play with the app.
[9:21] And you will need to mess with the rotations of the initial object.
[9:25] Or you can do it also in Vex, but it's just another way to do things.
[9:31] And you get it pretty aligned in the middle, which is also nice.


### Outro and Shop promo [9:37]
**Transcript (timestamped):**
[9:38] Okay guys, that was it. I hope you have found this useful.
[9:43] And as always, you can grab this thin file on my Patreon.
[9:48] And you can also check out my courses page or the shop page on Patreon,
[9:57] where I just released a new course on creating this procedural cookie and the fluid simulation or valence simulation, I should say.
[10:06] And I also have other ones that I released in past, so if you're guys interested, as you can see, they are really cheap.
[10:14] And that's it. Thank you, and I'll see you around.



---

## Captured Frames

- [0:10] tutorials/frames/hard-surface-techniques-in-houdini/frame_000.jpg
- [0:55] tutorials/frames/hard-surface-techniques-in-houdini/frame_001.jpg
- [3:05] tutorials/frames/hard-surface-techniques-in-houdini/frame_002.jpg
- [4:25] tutorials/frames/hard-surface-techniques-in-houdini/frame_003.jpg
- [6:20] tutorials/frames/hard-surface-techniques-in-houdini/frame_004.jpg
- [8:10] tutorials/frames/hard-surface-techniques-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
Five hard-surface techniques used to recreate a sci-fi prop from an ArtStation reference: **flattening curved geometry via UV-as-position** to make a Box Clip behave like it were on a flat surface, randomizing Vellum-simulated cloth pad patterns with a noise-driven bend-stiffness attribute, controlling Exoside QuadRemesher results by feeding it primitive-group boundaries, a **crease-based subdivision** trick to keep sharp corners while still rounding the rest of a shape, and a **VEX-based orient-to-point** snap (an alternative to Copy to Points) for aligning a box to a manually-picked target point/normal.

### Summary
For the cloth pads: after basic extrude/bevel modeling, pieces are grouped in batches of 8 (via `primnum / 8`, with a `shift by 4` sort so groups align correctly with the visual layout), then a **For Each (name/primitive)** loop saves a `rest` position, selects/converts the bottom to vertices, runs **UV Flatten**, promotes UVs to points, and assigns the UV attribute directly to position — flattening the curved geometry into a literal flat plane so a **Box Clip** (which only makes sense on planar/axis-aligned geometry) can cleanly clip the sides — something not possible directly on the curved original. The rest position is then extracted and the clipped shape sent back to its original curved placement, followed by a **QuadRemesh** (which softens the shape slightly) and a **Ray** projection back onto the original surface to restore precision. For Vellum cloth-pattern variation: identical geometry pieces produce identical simulation results by default (visibly unrealistic against the reference), fixed by creating a **noise-driven bend-stiffness attribute** before the seam constraint (min value raised off zero, tuned element size) and feeding it into the Vellum solver's Volume Cloth "bend stiffness scale" via that attribute — giving each pad a slightly different, more natural simulated pattern. For quad remeshing multi-piece hard-surface geometry with the third-party **Exoside QuadRemesher**: enabling "Use Primitive Groups Boundaries" (fed by primitive groups created *before* the remesher) prevents corners from getting "jacked up," producing dramatically cleaner topology than the default; the groups themselves come from a Boolean result, Group (min edge angle) on the sharp/art edges, **Edge Cusp** to separate the mesh along those edges, **Connectivity** to assign a per-piece `class`, and **Group from Name** (using the class attribute with a name prefix, deleting any unwanted groups) before Fusing points and running the remesher. For preserving sharp corners under Subdivide: rather than accepting the smoothed/rounded corners a plain Subdivide produces (problematic where inner extrusions/insets exist), a **Group Combine** of the corner edges feeds a **Crease** node with a high crease value — leaving the corner sharp while the rest of the shape (where no crease is applied) still smooths naturally, avoiding a chunky low-poly look without needing to give up subdivision entirely. Finally, to align a box precisely onto a manually-picked point in the middle of a curve-bridged shape (rather than fighting Copy to Points' orientation/normal quirks), a **VEX snippet** (reused from a previously-shared script) reads the base primitive's number and normal, extracts the target point's normal, builds a **rotation matrix** from the base-polygon normal to the target-point normal, and uses the target point's position to orient the box directly — described as functionally similar to what Copy to Points can achieve, but avoiding the need to fiddle with the copied object's initial rotation/orientation.

### Key Steps
1. **Batch grouping for cloth pads:** after extrude/bevel modeling, group primitives in batches of 8 via `primnum / 8`, applying a `shift by 4` sort beforehand so the batches align with the intended visual segment boundaries.
2. **Flatten curved geometry for clipping (For Each loop):** inside a **For Each (name/primitive)** loop: save the current position as a `rest` attribute; select and convert the bottom face to vertices; run **UV Flatten**; promote the resulting UVs to points; assign the UV attribute directly to `P` — producing a literally flat version of the curved piece.
3. **Clip on the flattened version:** run a **Box Clip** on the now-flat geometry to clip the sides — a clean, simple planar clip that would be geometrically awkward or impossible directly on the original curved surface.
4. **Restore curvature:** extract the saved `rest` position and transform the clipped geometry back to its original curved placement.
5. **Clean up post-clip:** run **QuadRemesh** (which softens the shape slightly) followed by a **Ray** projection back onto the original reference surface to recover precision lost from the remesh softening.
6. **Randomize Vellum cloth pattern (bend stiffness noise):** before the seam constraint, create a **bend stiffness** point attribute driven by noise (raise the noise's minimum value off zero, tune element size for pattern scale); in the **Volume Cloth** constraint node, set "Bend Stiffness Scale" to reference that attribute — each identical-geometry pad now simulates with a slightly different bend response, breaking up the otherwise-identical repeated pattern.
7. **QuadRemesh boundary control:** enable **"Use Primitive Groups Boundaries"** on the Exoside QuadRemesher and feed it primitive groups built *before* the remesh step — without this, sharp corners get corrupted/jumbled in the remesh output; with it, topology stays clean and subdivision-ready.
8. **Build the remesh boundary groups:** start from a Boolean result; **Group** the sharp/art edges via a min-edge-angle threshold; **Edge Cusp** those edges to separate the mesh into disconnected pieces at that boundary; **Connectivity** to assign each resulting piece a `class` attribute; **Group from Name** (using the class attribute as a name prefix, deleting unwanted/unused groups) to produce the final primitive groups; **Fuse** points, then run the QuadRemesher with those groups feeding its boundary control.
9. **Crease sharp corners before Subdivide:** **Group Combine** the specific corner edges that must stay sharp (not the whole shape's edges); feed that group into a **Crease** node with the operation set to "Add to Existing Value" and a high crease amount; **Subdivide** afterward — corners with the crease stay sharp while ungrouped edges (the shape's rounded/curved sections) still smooth naturally, avoiding both an all-rounded look and a chunky unsubdivided low-poly look, especially important where inner extrusions/insets meet a corner.
10. **VEX orient-to-point (snap a box to a manual target):** in an Attribute Wrangle, read the base primitive's number and normal (`prim_normal = ...`), extract the target point's normal (`target_pt`), build a **rotation matrix** transforming from the base-polygon normal to the target-point normal, then use the target point's position combined with that rotation matrix to directly orient/position a box primitive — achieves precise alignment to a manually-selected mid-point without needing Copy to Points' orientation workarounds or messing with the source object's initial rotation.

### Houdini Nodes / VEX / Settings
Nodes: Extrude, Bevel, Blast (batch grouping via `primnum/8` + sort/shift), For Each (name/primitive), Attribute Wrangle (VEX: rest-position save; UV-to-position assignment; rotation-matrix orient-to-point using base/target normals and positions), UV Flatten, Attribute Promote (UV→point), Box Clip, QuadRemesh (Exoside third-party plugin — Use Primitive Groups Boundaries option), Ray, Volume Cloth (Vellum constraint, Bend Stiffness Scale by attribute), Noise (bend-stiffness attribute generation), Boolean, Group (min edge angle threshold), Edge Cusp, Connectivity (`class` attribute), Group from Name (name-prefix, class attribute, delete unused groups), Fuse, Group Combine (corner-edge selection), Crease (Add to Existing Value, high crease amount), Subdivide.

### Difficulty
Advanced — combines several non-obvious procedural-modeling tricks (UV-as-position flattening, boundary-controlled quad remeshing, VEX rotation-matrix orientation) that assume solid VEX and hard-surface-modeling fundamentals.

### Houdini Version
20.5 (UI matches Houdini 20.5-era hard-surface/Vellum toolset).

### Tags
#modeling #vex #vellum #hard-surface #procedural #subdivision #tips #advanced

---

## Related Tutorials
Cross-link with direct-and-procedural-modeling-in-houdini.md and groups-patterns-in-houdini.md (same author, overlapping group/VEX-cleanup and orientation-via-VEX vocabulary) once indexed together.
