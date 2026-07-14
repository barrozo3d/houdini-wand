---
title: Modern Furniture Modeling in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=at27qaTVrFc
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, vex, procedural, expressions, furniture, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/modern-furniture-modeling-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Modern Furniture Modeling in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=at27qaTVrFc)
**Author:** cgside
**Duration:** 20m11s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So I've been building this environment using Odini
[0:06] and Unreal Engine as you can see and in today's video I wanted to show you how
[0:12] you can build this particular asset here, this table designer table let's say.
[0:19] And if you would like to see more content like this please let me know in the
[0:26] comments maybe you want to know how I model this table, how I did, how I model
[0:33] and simulated this couch or this chair. So let me know in the comments. Okay let's
[0:39] get started. So let's start by dropping a geometry container and we will start


### Modeling [0:42]
**Transcript (timestamped):**
[0:47] with a flat plane so we can deform it later. So let's start with a grid that is
[0:54] 10 by 1 and two columns, two rows and 30 columns and we want to change it to
[1:10] alternating triangles so we have that typical remeshed look. Now we will start to
[1:17] copy these shapes and see we want several levels. So let's copy by the
[1:24] bounding box size, the size. So we will just offset by the size of the initial shape
[1:35] and now we want to scale it to point three and as you can see is not scaling
[1:42] from that particular spot where we meet the two shapes but actually from the
[1:50] center as you can see. So what we can do is go into the pivot transform, copy
[1:56] this expression and play based on the Z, the Z mean. Now it will scale from
[2:05] that particular spot. Now we want to output the groups. So we have copy group 1,
[2:14] copy group 0 and 1. Let's do another copy. We can just copy this one but this time
[2:26] we call this copy group 3 and let's not scale it and let's see all the groups.
[2:37] Let's try to disconnect it. Yeah, sometimes the groups get messed up but now it's working.
[2:49] So let's combine the groups so we can blast these last shape that we don't want.
[2:58] So we'll name it last and we will combine copy group B1 and subtract copy group 0.
[3:10] So we get this shape in here so you can just blast.
[3:18] Now we want to create an image reboot for each row we have here. So for that I'm
[3:31] going to use a group combine again and I already have this setup but basically I'm
[3:42] going to say level A is going to be equal to copy group B0 and we will subtract it
[3:56] with copy group 1. So let's see if that works. Copy group 1. No, not copy group 0.
[4:12] But actually copy group B0. So this will be a level 1 and we want to add another one.
[4:22] Call it level B and we will be equals to copy group 1 and we will have another one level C
[4:36] and we'll be equal to copy group 0, subtract it by copy group B0. So let's see our groups now.
[4:50] Let's do a group delete and let's delete everything that is not level.
[5:05] Does this work? Not really.
[5:12] This is a simple word. Let me see. Level is not about it groups. Let's do this and this.
[5:30] The latest levels. Oops.
[5:42] The latest groups. Let's see. Does this work? No.
[5:58] It actually needs to be separated by a space. So if we do all but the level groups it should work.
[6:08] I didn't test this before. Sorry about that. So now let's create a name from groups and
[6:20] we will do level and let's check it and we have the name attributes.
[6:32] So now we want to do a few things. First of all let's create a loop. So for reach name
[6:41] primitive and we will iterate over each level and the first thing we need to do is to select
[6:58] these middle edges. Since we don't want them it will not mimic the correct shape. So let's do a group range
[7:11] and select every other primitive and we will select our triangles. So now we can group
[7:21] remote and group remote the group one to edges and let's do this one and don't include
[7:35] shared edges. Now we want to create a group for the unshared edges. So edges and let's
[7:48] group combine again. This is a masterclass on group combine and let's do edges and we group one
[8:02] and let's union with the unshared. So now we have everything but those edges that we want to delete.
[8:15] So what we can do now is do dissolve and we will dissolve the edges and we will dissolve
[8:31] and unselect it. So we got rid of those extra edges. Now we want to deform this shape to a cylinder


### Deformation [8:39]
**Transcript (timestamped):**
[8:45] to look like a cylinder. So for that we will use the petal form and we will use a circle.
[8:57] So let's create a circle and we want it in the ZX plane. Let's give it a few
[9:10] subdivisions and say we want to open our. After that let's connect it here and see the result.
[9:28] So this node is a bit tricky to work with. So what we want to do first is to find the correct axis
[9:39] and in this case we want X and Z. So still looking a bit off. What we need to do is to use
[9:54] a fraction of the curved length and now it should work fine. We could possibly re-sample
[10:04] but let's leave it like that for now. So now we still let's do this flat shading.


### Fuse [10:10]
**Transcript (timestamped):**
[10:14] Now we still have this edge here that is not deforming the shape correctly as you can see.
[10:23] It's creating this pattern and we want a flat one. So what we can do is use a fuse.
[10:33] And we will fuse, we will not fuse the points but output the snap points.
[10:45] So as you can see if we go to points we have this grouping here that now we can promote
[10:55] to edges. So snap points to edges and it includes only elements in the boundary.
[11:06] And we can now fuse everything now for real and dissolve that particular edge.
[11:21] So snap points. Okay. All right, let's see how this is looking.
[11:29] So we have all the shapes necessary but they are all on top of each other which we need to fix somehow.
[11:40] So this is actually pretty simple. We just need to match size.
[11:50] And we will duplicate these inputs by all dragging and say fetch feedback so we can access the previous iteration.
[12:03] And let's match size with the last iteration and we will domain and max.
[12:11] And these should give us the shapes correctly. Let's see. Let's add an normal.
[12:24] And we set it to vertices but and remove the name attribute visualization.


### Reverse Curve [12:35]
**Transcript (timestamped):**
[12:35] We might want to reverse the patches. So let's just see if we have an option in here.
[12:43] And yes, we have reverse curve.
[12:48] So now they since they have the triangles in the same position we need to offset each shape a bit.
[12:58] So for that we will use a transform. Let's use a transform.
[13:07] And we will rotate the shape. And first of all we need to rotate.
[13:16] Let's see.
[13:20] We rotate in Y. It's not rotating from the center.
[13:29] Oh, in the match size we need to set this to none.
[13:36] So now it's rotating from the center.
[13:41] So how much do we need to rotate?
[13:45] So we will take the grid columns which created this initial pattern.
[13:58] So let's copy this parameter.
[14:04] And let's divide 360 which is a full circle by the oops.
[14:18] I didn't copy. I need to paste relative.
[14:23] So now just rotate everything.
[14:28] Since I don't want to rotate the first one which is the iteration 0 I can use the detailed attributes on this loop.
[14:37] So in the second level it will rotate one time and then two.
[14:44] So what we can do is create the metadata node.
[14:51] Oops. Let's drag it here and add it as pairing puts.
[15:03] And we will just multiply this.
[15:17] So let me see.
[15:20] We need to multiply this by the detail.
[15:31] 9 of 1 which is the pairing puts, iteration 0.
[15:42] So we also need to remove one from here.
[15:53] We need a pair of parentheses here.
[16:00] And the minus one.
[16:03] Yeah, that works.
[16:05] And multiply it by oops.
[16:12] Yeah, that works.
[16:14] If I 360 by the columns and multiply it with the iteration.
[16:20] And now we have everything working as you can see.
[16:30] Alright.
[16:33] So now we want to give it a tapering effect but kind of mirrors.


### Taper [16:34]
**Transcript (timestamped):**
[16:41] So let's use a linear taper which is just a bend node but with a taper preset.
[16:52] And let's press enter on the viewport and press B.
[17:02] And let's just taper.
[17:08] It's working right now.
[17:14] And we don't actually want a taper that instead do a squish.
[17:29] And take the pivot.
[17:31] We can play with the pivot but we will enable ramp.
[17:36] Choose B spline and do something like this.
[17:42] And create another point here.
[17:45] So we can actually taper it every time.
[17:49] And we can play with the pivot.
[17:57] So something like this and maybe play with the capture lens.
[18:10] So let me check my original file.
[18:13] But you get the idea.
[18:19] So actually I have one.
[18:23] Let's use to one.
[18:26] So something like this.
[18:31] And now our geometry is not connected.
[18:35] So let's add a fuse.
[18:40] And the normal.
[18:42] You can just copy from here.
[18:45] So we can visualize it better.
[18:48] And now let's fill the clips.
[18:53] So fill the clip.
[18:56] And fill it with a triangle fan.
[19:01] And let's do a battle to pinch it off.
[19:09] For each one is too much.
[19:12] Let me see how much I used.
[19:15] And 0.5.
[19:20] And let's do a trick.
[19:23] Now I can do a sub and almost.
[19:28] So that's our final shape.
[19:30] Hopefully you'll learn a few techniques along the way.
[19:34] It's not too complex but I don't see it being modeled at the rise.
[19:40] It will be quite hard to be this precise.
[19:45] So yeah, I'll do it safe the day.
[19:49] And again, if you want to see anything else modeled.
[19:53] That you can see in this working progress.
[19:57] I can definitely do one other tutorial covering that.
[20:03] So that's about it.
[20:05] Thank you.
[20:06] Grab the file on Patreon.
[20:08] And I'll see you next time.
[20:10] Bye.



---

## Captured Frames

- [0:50] tutorials/frames/modern-furniture-modeling-in-houdini/frame_000.jpg
- [2:00] tutorials/frames/modern-furniture-modeling-in-houdini/frame_001.jpg
- [6:30] tutorials/frames/modern-furniture-modeling-in-houdini/frame_002.jpg
- [9:00] tutorials/frames/modern-furniture-modeling-in-houdini/frame_003.jpg
- [11:40] tutorials/frames/modern-furniture-modeling-in-houdini/frame_004.jpg
- [13:30] tutorials/frames/modern-furniture-modeling-in-houdini/frame_005.jpg
- [17:00] tutorials/frames/modern-furniture-modeling-in-houdini/frame_006.jpg
- [19:15] tutorials/frames/modern-furniture-modeling-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Modeling a modern designer table with a stacked, rotating, tapered "petal ring" base — a striped triangulated strip is deformed into multiple stacked cylindrical rings via **Petal Form** (a curve-based radial deformer), each ring individually offset in rotation using a **for-each-loop iteration index expression**, then the whole stack is reshaped with a **Linear Taper (squish preset)** and finished with a Poly Bevel — a build the author calls too precise to be practical to hand-model directly.

### Summary
The base pattern starts as a **Grid** (10x1, alternating-triangle remesh mode) that gets **Copy-and-Transform**'d using the bounding-box size as the offset (so shapes stack edge-to-edge), scaled down to 0.3 — critically **pivoting the scale from the shared meeting edge** (via a copy-pasted `Z-mean` expression in Pivot Transform) rather than each shape's own center, so the scaled copies visually taper toward the join. Three separate Copy nodes output differently-scoped groups (`copy_group_0`, `copy_group_1`, and an unscaled `copy_group_3`), which are combined via **Group Combine** (subtracting overlapping groups) to isolate exactly the geometry belonging to each "level" (ring) of the eventual stack — with a debugging note that Houdini's group-name-list syntax requires **space-separated** names in a "keep all but" expression, not comma-separated. A **Name from Groups** node converts the level groups into a proper `name` attribute, enabling a **For Each (name/primitive)** loop to process each ring independently: inside the loop, every-other primitive (the "filler" triangles) is grouped via Group Range and promoted to edges (excluding shared edges) to isolate the unwanted **middle seam edges**, which are then unioned with the boundary/unshared edges (another Group Combine pass) and **Dissolved** to clean up the strip before deformation. **Petal Form** (fed a subdivided Circle in the ZX plane) bends the flat striped strip into a cylindrical ring — described as "a bit tricky to work with," requiring the correct axis pair (X/Z) and switching the length parameter to a **fraction of curve length** (rather than absolute) to get proper wrapping. A visible seam artifact where the strip's start/end don't align cleanly is fixed via **Fuse** set to output **snap points** (not merge them outright), promoting that snap-point group to edges (boundary-only), then a second real Fuse plus Dissolve on that specific edge to close the seam invisibly. Since all the loop-generated rings initially stack at the same position, **Match Size** (mean/max alignment, referencing the *previous* loop iteration via a duplicated Fetch/feedback input) staggers them into a proper vertical stack; some ring curves need **Reverse Curve** to correct triangle-pattern orientation. Since every ring's triangle pattern starts at the same rotational phase, a **Transform** rotates each ring by `(360 / grid_columns) * (iteration - 1)`, read via a **Metadata** node exposing the for-each loop's `iteration` as a spare input/detail attribute — the `-1` term intentionally skips rotating the very first ring (iteration 0) so the base ring stays in its original orientation while subsequent rings each rotate one additional increment, creating a spiraling/staggered visual pattern up the stack (with an important side note: Match Size's Pivot must be set to **None**, not automatic, or the subsequent rotation won't pivot correctly from the ring's true center). Finally, a **Linear Taper** node (bend-node taper preset, entered/pressed B interactively) squeezes the stacked-ring cylinder into an hourglass-like silhouette — using a **B-spline capture ramp** with an added control point to shape exactly where the squish concentrates, and tuning the capture length — followed by Fuse + Normal to reconnect now-disconnected geometry after the taper deformation, **Fill (triangle fan)** to cap the open top/bottom, and a final **Poly Bevel** (~0.5) to soften/pinch the capped edges for the finished table-base shape.

### Key Steps
1. **Base strip pattern:** Grid (10x1, alternating-triangle remesh setting, e.g. 30 columns) for the initial striped triangle strip.
2. **Copy + center-pivoted scale:** **Copy and Transform**, offsetting by the shape's own bounding-box size (edge-to-edge stacking), scaling to ~0.3 — fix the scale pivot by copying a **Z-mean expression** into Pivot Transform so scaling happens from the shared meeting edge, not each shape's own center.
3. **Output per-level groups:** run three Copy nodes with different group outputs (`copy_group_0`, `copy_group_1`, unscaled `copy_group_3`), then use **Group Combine** (subtracting overlapping group sets) to isolate exactly the primitives belonging to each ring "level."
4. **Fix the group-list syntax bug:** in a "keep all but the level groups" expression, group names must be **space-separated**, not comma-separated, or the filter silently fails.
5. **Convert groups to a name attribute:** **Name from Groups** turns the per-level groups into a proper `name` attribute for looping.
6. **Per-ring cleanup loop:** **For Each (name/primitive)**; inside, Group Range selects every-other ("filler") primitive, promotes to edges (excluding shared edges) to isolate unwanted middle seam edges, unions with boundary/unshared edges via another Group Combine, then **Dissolve** to remove them before deforming.
7. **Cylindrical deformation:** feed a subdivided **Circle** (ZX plane) into **Petal Form** to bend the flat strip into a ring; select the correct axis pair (X/Z) and switch the length parameter to **fraction of curve length** (not absolute) for correct wrapping.
8. **Close the deform seam:** **Fuse** set to output snap points (not merge outright), promote the snap-point group to edges (boundary-only), then a second real Fuse + Dissolve on that specific edge to seamlessly close the ring.
9. **Stack the rings:** **Match Size** (mean/max alignment, Pivot explicitly set to **None**) referencing the *previous* loop iteration (via a duplicated Fetch/feedback input) to stagger each ring vertically into a proper stack; **Reverse Curve** on rings where the triangle pattern orientation needs flipping.
10. **Per-ring rotation offset:** add a **Metadata** node exposing the for-each loop's `iteration` as a spare input; **Transform** each ring by `(360 / grid_columns) * (iteration - 1)` — the `-1` skips rotating the first ring (iteration 0), so the stack builds a progressively-rotated spiral pattern.
11. **Overall silhouette shaping:** apply a **Linear Taper** (bend node's taper/"squish" preset) to the full stacked-ring cylinder; use a **B-spline capture ramp** (with an added control point) to precisely control where the squish concentrates, tuning the capture length for the desired hourglass profile.
12. **Reconnect + cap:** **Fuse** + **Normal** to reconnect geometry disconnected by the taper; **Fill** (triangle fan mode) to cap the open top/bottom.
13. **Finish:** **Poly Bevel** (~0.5) to soften/pinch the capped edges for the final table-base shape.

### Houdini Nodes / VEX / Settings
Nodes: Grid (alternating-triangle remesh mode), Copy and Transform (bounding-box-size offset, Pivot Transform Z-mean expression for center-pivoted scale), Group Combine (multi-pass level isolation, space-separated group-name syntax), Name from Groups, For Each (name/primitive loop), Group Range (every-other primitive selection), Group Promote (point/edge, shared-edge exclusion), Dissolve, Petal Form (circle-driven radial deform, axis selection, fraction-of-curve-length mode), Fuse (snap-points-only mode, then full fuse), Match Size (mean/max, Pivot: None, Fetch/feedback reference to previous iteration), Reverse Curve, Metadata (loop iteration as spare input/detail attribute), Transform (expression-driven per-iteration rotation), Linear Taper (bend-node taper preset, B-spline capture ramp with added control point, capture length), Normal, Fill (triangle fan), Poly Bevel.

### Difficulty
Intermediate — heavy use of group-combine logic and for-each-loop iteration expressions, but no VEX required; assumes comfort with procedural group manipulation and node-based deformers (Petal Form, Taper).

### Houdini Version
20.5 (UI matches Houdini 20.5-era modeling toolset).

### Tags
#modeling #vex #procedural #expressions #furniture #product-viz #intermediate

---

## Related Tutorials
Author is building a larger Houdini + Unreal environment and mentions a couch/chair simulation asset from the same project — cross-link once a matching tutorial is found in this batch. Shares the Metadata-node iteration-index rotation pattern with model-and-rig-a-wardrobe-in-houdini.md.
