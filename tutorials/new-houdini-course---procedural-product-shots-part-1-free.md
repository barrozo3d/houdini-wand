---
title: New Houdini Course  - Procedural Product Shots | Part 1 Free
source: YouTube
url: https://www.youtube.com/watch?v=FxrSPbnI3tI
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, vex, uv, procedural, product-viz, course, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# New Houdini Course  - Procedural Product Shots | Part 1 Free

**Source:** [YouTube](https://www.youtube.com/watch?v=FxrSPbnI3tI)
**Author:** cgside
**Duration:** 17m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome to this new Wildiniel adventure. In this project we will
[0:05] model, rig, animate and seam this product shot from start to finish. It's
[0:10] packed with valuable information and if you enjoy my videos you'll like this
[0:14] one too. This will be a Patreon project for the month of November but I will
[0:19] make the first part for free year on YouTube. If you like what you see or would
[0:23] like to have a big at this course continue watching this video for the
[0:26] modeling part and we will continue on Patreon right after this video ends. Hope to
[0:31] see you there. Thank you and enjoy. So guys let's get started by modeling the
[0:39] container first. So I'm gonna start with the grid that will be one by one in size
[0:49] and two rows and two columns so we don't have subdivisions at all. Then I want to
[0:58] have so if we look at the point numbers I want to have point zero in one of
[1:02] these corners so I'm gonna sort because we're going to do adjusted pebble on
[1:08] these corners so let me just shift the point order by two so we have zero in
[1:13] here. Then I'm gonna create the battle attribute so it should just float and
[1:18] that's p-scale and I'm just gonna set a constant value of 0.5 and the default
[1:27] value for the other ones at 0.2 and now if we do pebble and we do based on points
[1:41] and for the amount we're gonna set it to one and eight divisions and I'm gonna
[1:48] do a scale by attribute. So before I'm gonna do the letter root that just floats
[1:59] on all but zero so we get this result of not here sorry on the attribute that
[2:07] just floats so all but zero and we get this sort of result so one corner is more
[2:14] the other corners are more bevel than the number zero. So that's fine let's save
[2:21] and do a clip for now to divide these into two parts and we're gonna do a
[2:28] clip on the x and z so a diagonal clip and do 0.15 and we will keep using this
[2:36] values and I'm gonna do alt primitives let me just make sure I am doing this
[2:43] properly yeah and then we're gonna save the clip edges and above and below
[2:50] primitives so we have some groups to play with. Oh let's create a null and call
[2:59] this base just give it some color and that's fine then we're going to extrude
[3:09] this to insert this I mean so extrude and we're gonna do individual elements and
[3:16] set by 0.055 something like that and then we want to save the extrude front group
[3:30] from there we're gonna blast or isolate that group so the extrude front the inside we're
[3:38] gonna do a resample since this doesn't have geometry in the middle we can use little
[3:43] to a resample we just want to round off these shapes so a length of 0.05 and then we're
[3:52] going to do a natural blur and we're gonna blur with tree iterations and not being
[4:02] border points so we get this sort of result then we're going to immerge in the base
[4:09] so object merge the base and we're going to do a boolean so boolean I believe is shatter I used
[4:17] yeah is shatter and we need to send this to surface and surface because this doesn't have
[4:21] thickness and we're going to do just a boolean in here and we get this sort of result.
[4:28] Now let's group do it the extrude front and keep the others then we're going to try and
[4:37] go light so try and light which is the divide not because we will go through a water rematch right
[4:45] now then we can fuse and in order to have a better result with the water rematch we're going to
[4:54] rematch this quite a bit and remember we let me just rematch this first and I will tell you what I
[5:01] mean so remember we have these groups that we need to harden in here otherwise we don't
[5:09] keep the groups correctly so we have a bovean below and we want to keep these groups even after
[5:17] even after the quad rematch so unfortunately the Aldini quad rematcher doesn't work that well so
[5:23] I'm going to have to use the acrocyte one again if you're serious about
[5:30] Aldini and this sort of stuff you really should consider buying at least quad rematcher I don't
[5:35] use many plugins in Aldini I try to avoid them but the acrocyte quad rematcher is such a powerful
[5:41] plugin that I really advise you to buy it and it's not expensive and it is forever you keep it
[5:53] is a perpetual license so you don't have to pay each month and whatnot so it's always a good deal
[5:59] I think it's about $70 or something so I'm gonna set this acrocyte quad rematcher to
[6:05] use primitive group boundaries to keep the rematch consistent it kind of changes this to 248
[6:12] I'm going to disable this and the other things can be like test default and let's look at the result
[6:23] oh sorry guys I know why because I forgot to add in here the a-pollys group so where is that
[6:33] b-pollys I mean so this one inside and now when we quad rematch we should have that group in
[6:40] there that that flow and now it's looking better let me lock the node so even if you don't have
[6:45] quad rematcher you can access it so now we want to do a group transfer let's see and but as you
[6:55] can see it won't be perfect so first of all what I'm going to do is to reduce this
[7:01] this in structural to 1 and to have a proper transfer we need enough polygons so I'm gonna just do
[7:08] another rematch in here and I'm gonna set these to our the n-edge groups and do let's say point
[7:17] oh one and now we have a perfect group transfer so you can easily see how this is such a powerful
[7:25] workflow with this exercise quad rematcher you can even transfer groups and have the different
[7:30] edge flow going properly so yeah I hope I convinced you to get quad rematcher anyway so I'm
[7:38] gonna leave this locked and you can access the file from here and continue doing the tutorial so I'm
[7:44] gonna do a name not this one name from groups which is just a preset for the name nodes and I'm going
[7:52] to name both and below so I want a name attribute from those groups let's see that so name and we have a name
[8:07] now here's the thing I want to reverse this name I'm not sure I can do below and above no it won't
[8:19] work so we have to do some work in here to ring to order these groups properly because I know I'm
[8:24] gonna need it later so just follow me it will be simple first of all we're gonna create an array
[8:32] called names and it will be a unique valve of pre-matery boots so prem and we want the name
[8:41] so this just will output below and above the group that we have in here so let's see below and above
[8:49] those are not great names but let's keep it for now now we're gonna reverse that array names
[8:57] that should be simple to understand and then we're going to set to reorder the attributes so let's
[9:05] do index we're gonna do a fine to find the index of of that name so since we reversed we will have
[9:18] in the reverse order of course so we just found the index and then we can just set name
[9:23] with the following expression so we're gonna select names from the names array that we have
[9:29] as a variable and I'm gonna just do one offset so idx plus one and we can just
[9:36] modular to the length of the names which is just two and let's see if that works well it doesn't
[9:44] because I've probably done some stake so modular length names this is correct names
[9:54] as a name idx names reverse names you need oh we need to set this to primities of course so we get
[10:01] the reverse and I'm gonna name it reverse reverse name that was a bit of work but hopefully you got
[10:11] something out of it then I'm gonna do a group from attribute boundary and let's see let's just
[10:21] do boundary and we're going to remove ub and just say name and we don't want to include and share
[10:35] that is not to include and share that just and yeah we get this edge in the middle so that's our
[10:41] boundary then we're going to do a simple ub texture and a projection on the y will be fine but as
[10:50] you can see that it reversed so I'm gonna reverse this in here and since this will go
[10:57] well why I can't view my uv's what's going on let me reset the viewport
[11:06] so apparently I can see my uv's but anyway stress me if we reverse we need to offset to get to
[11:12] the uv tile 1001 so the first tile of the uv's I'm gonna fix I'm gonna restart what we need to
[11:18] have the uv view back then we're going to save a rest because we will need it later
[11:25] and I'm gonna just create null and call it top and let's just color this all right
[11:37] now we're going to branch off in here and the word vertex will read
[11:49] and we're gonna split it not based on normals but based on name which will mean we will have
[11:54] this separated right yeah and let's do a voluix root R and I'm just gonna extrude one of the groups
[12:09] which is the oops b polis and we're gonna set the distance to minus 0.2 to work on this container
[12:21] and then we're gonna save the output the extra font as base on dainer because we'll take advantage
[12:28] of that later and the rest is fine just add a normal and I'm gonna set the cost pangle to 55 for now
[12:40] then we will do another poly extrude and this poly extrude
[12:48] sorry I forgot to do something in here when we do this poly extrude as you can see this is just
[12:53] going down and I noticed in the reference that this does a little tapering so we're going to
[12:59] to spine control yeah spine control yes so let's go to spine control and here in the
[13:09] thickness ramp we can decrease this one so let me check in here I have one and in the last one I
[13:15] have 0.8 so let me change that to 0.8 and we get this little tapering as you can see which will work
[13:25] better all right now we want to add the thickness to the to the mesh because right now we have a
[13:33] single single geometry single sided so in this case I'm gonna set this to 0.009 and I'm gonna save
[13:43] the extrude front and I'm going also to output the back and we get this result don't worry about
[13:49] the UVs we won't need UVs at all but we can easily do that with UV unwrap no there's something
[13:55] like that so don't worry about that right now let's create an all let's group promote the boundary
[14:06] the boundary group the boundary to I believe I'm gonna promote it to primitives let me just
[14:15] check in here yes I'm gonna promote it to primitives but for some reason this is not working
[14:22] why is that let me check my group again so let's go to point the wedges boundary
[14:33] something is fishing around here primitive groups
[14:41] so we are saving in here the boundary right that's correct let me check in here on my file
[14:52] sorry I forgot we don't want to save edges we want to save points so it preserves better the geometry
[15:02] the group I mean so now when compared to primitives we will have this and finally we can manipulate it
[15:10] so let's do group expand and do expand the boundary and boundary and we can just do a step of one
[15:24] and then we do yet another one because I want to isolate these inner primitives to set the
[15:29] greasier group and I'm gonna do two steps and we get the interior ones if we do an exploded view
[15:38] let's do it before and we get let's get rid of the attributes as you can see we get the interior
[15:45] ones which I want to crease so group expand let's find now let's do a small polypebble so polypebble
[15:57] this is an unnecessary but just for for visual fidelity let's do a distance of
[16:05] let's let's do a distance of 0.005 and I'm gonna do ignore flat edges and do like say 59
[16:17] and two divisions will be enough let's see that is just creating a battle to help on the subdivision
[16:26] now let's do a crease and we will do a crease based on those primitives so boundary let's do a
[16:36] crease of 10 and now when we do a subdivide and one will be fine as you can see those primitives
[16:43] will be creased if we don't do that this will round off which I don't want
[16:48] and after doing the subdivide we can just add a normal and I don't think I did anything
[16:59] yeah just default settings create an all and this will be out on the painter
[17:10] okay guys not very exciting so far but we accomplish already most of the modeling and next we
[17:17] will do the reading let's do that in the next part



---

## Captured Frames

- [0:50] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_000.jpg
- [2:20] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_001.jpg
- [4:25] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_002.jpg
- [6:25] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_003.jpg
- [7:25] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_004.jpg
- [9:50] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_005.jpg
- [12:10] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_006.jpg
- [15:40] tutorials/frames/new-houdini-course---procedural-product-shots-part-1-free/frame_007.jpg

---

## Structured Notes

### Core Technique
Part 1 (free preview) of a paid multi-part course modeling a rounded product container: a rounded-square base from an asymmetric per-corner **Peak/Bevel** with a point-order-dependent `pscale` attribute, a **diagonal Boolean split** (matched by re-projecting a resampled/blurred surface) to divide the shape into "above"/"below" halves, an Exoside-QuadRemesher pass with **primitive-group-boundary preservation** so a subsequent **Group Transfer** carries clean edge flow across the remeshed geometry, a VEX array-based **group name reversal** trick (needed for later shading/UV logic), and a final interior-primitive **crease-before-subdivide** pass for sharp inner corners without losing the rounded outer silhouette.

### Summary
The base starts as a 1x1 **Grid** (2x2, no subdivisions) with points **Sorted** so point 0 lands in a specific corner, then a `pscale` **Attribute Adjust Float** gives that corner a bigger bevel value (0.5) versus the rest (0.2 default) via an "all but point 0" attribute expression — feeding a **Peak/Bevel-based-on-points** pass (1 amount, 8 divisions, scale-by-attribute) for an asymmetric rounded-corner look (one corner more rounded than the others). A diagonal **Clip** (X/Z axes, all primitives) splits the shape into two halves, saving the clip edge plus above/below primitive groups for later use; the shape is Extruded (individual elements, insert-style) to create wall thickness, with the extrude-front group saved and isolated (Blast), then cleaned up via Resample + Attribute Blur (3 iterations, not affecting border points) for smooth rounded interior corners. The base shape is Object-Merged back in and **Boolean** (Shatter mode, Surface-Surface since the base has no thickness) cuts the extruded shell against it. To prep for quad remeshing, a **Divide** ("Try and Light") pass plus Fuse cleans topology, then the mesh is Remeshed fairly densely specifically because groups need to survive the remesh — critically, Houdini's native QuadRemesher doesn't reliably preserve primitive groups, so the **Exoside QuadRemesher** (recommended as a worthwhile ~$70 perpetual-license purchase) is used instead, with **"Use Primitive Group Boundaries"** enabled (fed the saved above/below Boolean groups) to keep the remesh topology aligned to those group boundaries — after fixing a missed group-input connection, the remesh result correctly preserves the split. A subsequent **Group Transfer** (needing sufficient polygon density from an extra Remesh pass at a fine edge length, ~0.01) then successfully carries the original groups' edge-flow information onto the new quad-remeshed topology — described as a genuinely powerful combined workflow (remesh + group-boundary preservation + group transfer) worth the plugin cost. A **Name from Groups** node creates a `name` attribute from the "below"/"above" groups, but since their alphabetical/creation order isn't what's needed downstream, a **VEX array-reversal trick** manually reorders them: build a `names[]` array from `prim(0, "name", uniqueval)`-style unique-value lookup, **reverse the array**, then re-derive each primitive's name by finding its original index in the *un-reversed* list and using `names[(idx+1) % len(names)]` to remap it to the reversed order — described as "a bit of work" but functional. A **Group from Attribute Boundary** (on the `name` attribute, excluding unshared) isolates the seam edge between the two halves; a simple planar **UV Texture** projection (Y axis) handles UVs, reversed and offset to land in UDIM tile 1001, with the pre-reversal position saved as a `rest` attribute for later use. From here, the model branches into two halves via a **Blast + Split** (by `name`, not normal) — one half (`b_polys`) gets **Poly Extruded** inward (distance ~-0.2) to hollow out the container interior, with the extrude-front group saved as `base_container` for later reuse, followed by Normal (crease angle 55). A second Poly Extrude adds a slight **taper** via **Spine Control**'s thickness ramp (dropping the far end to 0.8) to match a slightly tapered reference profile, then the whole shell is given real thickness (~0.009) with both front and back groups saved (UVs explicitly not needed on this pass — noted as fixable later via a "UV unwrap" auto-approach if ever required). The boundary group is Group-Promoted to **points** (not edges — a subtle but important distinction the author catches mid-video, since promoting from edges rather than points didn't preserve the geometry correctly) then to primitives; **Group Expand** by one step isolates the boundary ring, and a second two-step expand isolates the deeper **interior primitives** specifically to receive a crease. A small cosmetic **Poly Bevel** (~0.005, ignore-flat-edges, angle ~59, 2 divisions) softens those interior primitives slightly before a **Crease** (value 10) locks their edges sharp; a final **Subdivide** (depth 1) then rounds everything else off smoothly while the creased interior primitives stay crisp — without the crease step, those primitives would incorrectly round off along with the rest of the shape. The part ends with a Normal recompute and a named Null output, with the next installment (behind Patreon) planned to cover UV/texturing/shading of the modeled container.

### Key Steps
1. **Base grid + point ordering:** 1x1 Grid (2x2, no subdivisions), **Sort** to place point 0 in the target corner (needed for the asymmetric bevel that follows).
2. **Asymmetric corner bevel:** create a `pscale` float attribute, **Attribute Adjust Float** setting a bigger value (0.5) on point 0 and a smaller default (0.2) on the rest via an "all but point 0" expression; run **Peak/Bevel-based-on-points** (amount 1, 8 divisions, scale-by-attribute) for one visibly-more-rounded corner.
3. **Diagonal split:** **Clip** on the X/Z axes (all primitives, diagonal cut ~0.15) to divide the shape in two, saving the clip edge plus above/below primitive groups.
4. **Extrude + smooth interior:** Extrude (individual elements, insert-style, ~0.055) saving the extrude-front group; isolate that group (Blast), Resample (~0.05 length) + Attribute Blur (3 iterations, border points excluded) for a smooth rounded interior.
5. **Boolean cut against the base:** Object Merge the original flat base, **Boolean** (Shatter mode, Surface-Surface since the base has no thickness) to cut the extruded shell.
6. **Pre-remesh cleanup:** **Divide** ("Try and Light") + Fuse, then Remesh at sufficient density specifically to support group preservation through the next step.
7. **QuadRemesh with group-boundary preservation:** since Houdini's native quad remesher doesn't reliably keep primitive groups, use the **Exoside QuadRemesher** with **"Use Primitive Group Boundaries"** enabled (feeding the saved above/below groups) — double-check the group input is actually wired, or the boundary constraint silently fails.
8. **Group Transfer onto the remesh:** run an extra fine **Remesh** pass (edge length ~0.01) beforehand to ensure enough polygon density, then **Group Transfer** to carry the original edge-flow groups cleanly onto the new quad topology.
9. **Name + reverse group order (VEX):** **Name from Groups** creates a `name` from the below/above groups; in a wrangle, build a `names[]` array via unique-value lookup on the `name` attribute, **reverse the array**, find each primitive's original index in the un-reversed list, and remap using `names[(idx+1) % len(names)]` to reorder the names as needed downstream.
10. **Seam + UVs:** **Group from Attribute Boundary** (on `name`, excluding unshared) isolates the seam between halves; simple planar **UV Texture** (Y axis), reversed and offset into UDIM tile 1001; save the pre-reversal position as a `rest` attribute for later use; output a named `top` Null.
11. **Split by name and extrude the container wall:** **Blast + Vertex Split** by the `name` attribute (not normal-based) to separate the halves; **Poly Extrude** the `b_polys` group inward (~-0.2) to hollow the container interior, saving the extrude-front group as `base_container`; add Normal (crease angle 55).
12. **Taper via Spine Control:** a second Poly Extrude uses **Spine Control**'s thickness ramp (drop the far-end value to ~0.8) for a subtle tapered profile matching the reference.
13. **Add shell thickness:** thicken the single-sided mesh (~0.009), saving both extrude-front and back groups; UVs intentionally skipped for now (can be added later via an auto UV-unwrap approach).
14. **Boundary group → points → primitives:** Group Promote the boundary group to **points** specifically (not edges, which was found not to preserve the geometry correctly), then to primitives.
15. **Isolate interior primitives for creasing:** **Group Expand** the boundary by 1 step (the boundary ring itself), then a second expand by 2 steps to isolate the deeper **interior primitives** that need creasing; verify via Exploded View.
16. **Crease + subdivide:** small cosmetic **Poly Bevel** (~0.005, ignore flat edges, angle ~59, 2 divisions) on the interior primitives, then **Crease** (value 10) to lock their edges sharp before a final **Subdivide** (depth 1) — without the crease, those primitives would incorrectly round off along with the rest of the shape.
17. **Finish:** recompute Normal, output a named Null for the next part of the course (UV/shading, covered on Patreon).

### Houdini Nodes / VEX / Settings
Nodes: Grid, Sort (point reorder), Attribute Adjust Float (`pscale`, all-but-point-0 expression), Peak/Bevel (points-based, scale-by-attribute), Clip (X/Z diagonal, group save), Extrude (individual elements, insert-style, front-group save), Blast, Resample, Attribute Blur (iterations, border-point exclusion), Object Merge, Boolean (Shatter, Surface-Surface), Divide, Fuse, Remesh (multiple passes, density tuning), Exoside QuadRemesher (third-party plugin — Use Primitive Group Boundaries option), Group Transfer, Name from Groups, Attribute Wrangle (VEX: unique-value array build via `prim(0,"name",uniqueval)`-style lookup, array reverse, index `find()`, modulo-based remap `names[(idx+1)%len(names)]`), Group from Attribute Boundary (exclude unshared), UV Texture (planar, Y axis, reverse + UDIM-tile offset), rest attribute save, Vertex Split (by name attribute), Poly Extrude (x2 — interior hollow-out, and Spine Control taper), Spine Control (thickness ramp), Normal (crease angle), Group Promote (point-then-primitive, points not edges), Group Expand (1-step and 2-step passes), Poly Bevel (ignore-flat-edges, angle threshold), Crease, Subdivide.

### Difficulty
Intermediate — mostly straightforward modeling logic, but the VEX array-based group-name reversal and the QuadRemesher-group-boundary-preservation workflow require above-average procedural-modeling comfort.

### Houdini Version
20.5 (UI matches Houdini 20.5-era modeling toolset; explicitly a paid-course free preview part).

### Tags
#modeling #vex #uv #procedural #product-viz #course #intermediate

---

## Related Tutorials
Part 1 of a paid multi-part "Procedural Product Shots" Patreon course (author explicitly continues UV/shading/rigging/animation in subsequent paid parts, not covered in this free video) — cross-link with any later parts of this same course if found in this batch.
