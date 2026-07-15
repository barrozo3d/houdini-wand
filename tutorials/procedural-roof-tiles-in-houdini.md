---
title: Procedural Roof Tiles in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=rvmDcbSMXh8
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.598"
tags: [vex, uvs, divide, for-each-loop, compile-block, roof, architecture, procedural-modeling, dihedral]
extraction_status: complete
frames_dir: tutorials/frames/procedural-roof-tiles-in-houdini/
frame_count: 11
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Roof Tiles in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=rvmDcbSMXh8)
**Author:** cgside
**Duration:** 37m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'm gonna show you step by step how you can create a
[0:06] procedural workflow like this one. Let's get started. So let's start by dropping the geometry
[0:15] note and we will use a grid. Let's set dimensions to something like 16 and 12. You can change this
[0:27] latent and let's see rows and columns to 3 to have this center point and
[0:34] connectivity we can set it to alternating triangles to have that rough shape. Now we
[0:43] can transform the center points of our that let's pull and we can do
[0:51] founding regions and points and that already gives us the result we want and let's now
[1:00] transform it up. So let's raise it the center point something like 3 in the translate
[1:11] way. Now we don't need these edges in here these middle edges so let's blast them or
[1:19] this all so we can just use this all flat edges. Now let's see our normals. We might want to add
[1:31] some odd normals to other than the geometries so let's go with verticeses since it to 0 because
[1:41] it's more like this because we will copy a few grids to this that can be used to instance our geometry
[1:51] our tiles. So now let's extract the same trade to copy the geometry to here. Let's go to primitives
[2:05] and we lose our normals so let's go to an attribute promote and promote from vertex to primitive
[2:17] and let's go with normal and should have our normal we just need to set transfer attributes to normal.
[2:28] This should do the trick. Now let's copy the geometry so creating a grid can be on the
[2:40] exit blenders in a problem and we can copy the points and this will give us this result which is
[2:53] not ideal it's not what we want we want them to be flat on these planes up to root so we can change
[3:04] the orientation and whatnot and create the aperture roots but let's do it the hardware let's say
[3:13] so we can learn something new so creating an attribute triangle to do some basic wax
[3:21] so the first thing we want to do is to create the aperture roots so we'll set it on the y
[3:38] and that already gets some orientation going and let's also create
[3:49] let's also give some some aspect ratio a different aspect ratio to the grid so we can know
[3:59] if it's oriented correctly so in the attribute wrangle let's create
[4:08] let's see the normals so right now let me just change the usual guides stay on the one
[4:19] so our normals are pointing like this let's create an out attribute so we can then use it to
[4:28] create another one which will be the sides and then we can orient the planes properly let's go
[4:35] one by one so let's go to v at out it will be equal to let's normalize it and let's subtract the
[4:49] position from the middle points but on the y plane of the points so let's show zero zero zero
[5:02] but in the y let's create let's say at p dot y so let's see that's out that roots
[5:14] and let's control click it and say it's a marker vector let's say it's blue blue you can see it
[5:26] so let's keep it yellow so now we have this one going out and let's create the side one
[5:36] just we will need it so let's go with v at sides c equals to cross and let's cross the
[5:49] out and then okay let's see the side and let's again edit it to vector let's see this one is red
[6:12] so now we have the side attributes and finally we can say v at 10 let's set it on normals and cross
[6:28] between the and and the side
[6:32] and now our normals should be pointing like this along the geometry along the these triangles
[6:46] let's get rid of the visualization in the normals and let's see so now everything should be
[6:57] as expected as we have our geometry and the planes are oriented correctly
[7:11] so let's show to the trick now we need to create the proper size for the planes we will need to fit
[7:18] these these grids to the original rough geometry so for that we will need to calculate the width of
[7:31] these frames so let's go in here and first create a measure so let's move this up
[7:45] and create a measure we will need the area so let's go with area parallel this fine and area
[7:59] and now
[8:04] now in a wrangle we will calculate the width and the height so for that
[8:10] let's go over primitives and say create the bounding box
[8:19] not that should but let's keep it in a variable get bounding box size
[8:25] so we get the size of the frames and now we will need a difference width and height for each
[8:38] frame so we need to somehow filter through them so some primitives the primitives that are facing
[8:47] the z axis need to be different from the frames facing the x axis so what we can do is to use the
[8:57] normals so if we say if absolute v dot v dot x is smaller than 0.001
[9:20] we can set the weighted root v f dot v is equal to bounding box dot x so in this case for
[9:36] these primitives we will measure the x size of the bounding box and for the other ones we will
[9:44] measure the z size so now we can just say else
[9:55] widths will be the bounding box dot x and for the right i just found the final line
[10:08] that you can say two times the area and divided by the widths
[10:24] this is the formula for the lights as far as i know so now we need to use
[10:32] spare point that you're good so we will need to look so far each point we will need to use the
[10:40] copy two points in a loop and now we can set the attributes on the grid so we need the width
[10:54] and the light so for the width let's say points and we will reference the far each begin so far each
[11:09] begin one and we will need the point zero let's say and get the widths
[11:21] and the index is a float so it's the default one now this is turning out zero we need to promote it
[11:34] in here the width and the height in this case something is wrong
[11:47] so let's see width
[11:53] so I believe I have something wrong in here let's see
[12:05] you need to actually it didn't throw an error so now this should do the trick let's see
[12:13] I mean I'm not sure if it's let me see so this is actually correct the width is working we just
[12:30] need to set the height so let's go to the grid and copy this expression and let's go for
[12:39] right
[12:44] and let's see in the this is also correct but we need to set the centroid to be bounding box center
[12:59] now this should do the trick
[13:01] let's also create a natural boot in here so let's go after this one it's creating a
[13:14] attribute wrangle and just save that string attribute let's say
[13:25] bring in id we'll be able to write away so integer to string and let's say
[13:35] prime num so for each prime it will create an attribute so let's say primitives and in here
[13:48] we should have a prime id with in this case it's numbers but they are it's a string attribute
[13:56] all right so we have it working let's continue
[14:02] now we need to set the density so the rows and calls so for that let's create the two attributes
[14:16] to flow the attributes so in this case let's say it's density rows density rows
[14:34] and flows let's apply let's control c control v and density calls for columns
[14:46] so now we have this two attributes and we can take for the rows will be the density y let's say
[15:01] so let's copy the y component of the size and pass it in here and now we can save one and copy this
[15:13] and multiply it with the density so we can just have a multiplier
[15:25] first step is to one and let's copy the x or let's just copy this expression paste it and say x
[15:35] and calls
[15:42] so this way we can set this one and we will add the square dot
[15:51] and divisions but we don't want them spoiled i have some values here 1.6 and 2.5
[16:03] but you can play with it so this way when we copied the tiles to the same
[16:08] right of the print they will be equally distributed both on the x and z
[16:21] so now we need to get rid of these extra shapes that we don't need we won't need the
[16:28] tiles in here but we should leave at least some room so it fits perfectly on the edges
[16:40] so it will make more sense later on but for now let's just object merge
[16:49] the so let's say in here
[16:58] we can create another layer
[17:03] and let's say it's through this let's copy it to the three here
[17:14] create a thickin
[17:18] we cannot draw first this group and say it's
[17:24] points and keep by bounding regions and bounding objects and as you can see that point work
[17:35] we will need to add a thickin so let's say both directions and it's not selecting the corner points
[17:44] because it's right on the edge so what we can do is just create a transform
[17:50] and make sure it's in the center so center i the x dy and z and let's go for point
[17:59] roll one just to select the corner points
[18:05] now we can leave some room to make sure the tiles fit perfectly so for that we can create a
[18:12] group group expands and let's say group two group two and one is fine we will have some extra room
[18:27] so we can cut them later and from here let's press
[18:34] press
[18:36] press now select it and let's say group two so now we have this
[18:43] we have some extra room to play with
[18:47] now i will paste in here just the tile model
[18:52] there's nothing complicated i just did with a few extrusions and bubbles
[18:58] so as you can see it's pretty simple
[19:04] just to speed up and let's create the copy to points
[19:14] and we will need to extract the centroid
[19:18] extract centroid
[19:23] and let's go with primitives
[19:25] and let's copy this to you
[19:34] and right now it's just too big so it's creating attribute
[19:38] create and let's say this scale
[19:44] we will also need normals so after the blast we will need to add a normal
[20:04] and let's say primitives
[20:11] and the extract centroid transfer the normal
[20:17] and let's also rotate these 90 degrees
[20:25] and we will need also one attribute
[20:33] so in the same attribute create let's go with another one and say up
[20:39] and this one needs to be rectum and say one
[20:46] so now that is working properly
[20:48] and we will also need for later the primid
[20:58] so you still have it here
[21:02] no let me see
[21:08] primid, primid, where did i lost it following here
[21:14] so we need to promote all sounds the primid
[21:20] still a lot of it
[21:23] and it's right here that we lose it so let's make sure we promote it
[21:32] from points to primitive and primid and in here we pass it to primid
[21:41] so there you go
[21:46] let's see that attribute and make sure
[21:52] it is set to color and random form it's
[22:00] and we have the id for each section that we will need for the booyah
[22:06] in this case we want to use booyah and we will lose another technique that is more efficient
[22:14] or faster so in this case i don't want them rotated exactly 90 degrees
[22:22] so let's say it's 85 to have that typical styling effect on top of each other
[22:30] so that is fine
[22:36] and again we have the primid as a point attribute because we extracted the centroid
[22:45] so let's promote it back to prim
[22:50] so from point to primitive and primid and now we will cut
[23:00] the actual geometry so for that let's create a forage loop so we can iterate over each piece to cut it
[23:14] so let's go with the forage forage imprimitive and let's say primid
[23:25] this should work fine
[23:39] and now we can use booyahs but again it will be a bit slow at least on my machine it's a bit slow
[23:47] so i found another solution which will be using the clip node with the proper orientation
[23:59] that we can extract from the normals let's say so let's try that let's copy this object merge
[24:10] and create the meta import style of meta
[24:20] as we will need the iteration let's paste here
[24:24] and let's blast let's blast the primitives so let's go with the detail
[24:47] we will just extract one primitive at a time so let's go with the check
[25:01] do we have the primid in here? no so we need to change this roof base to be
[25:17] in here just add this isn't no
[25:26] so yeah so let's say this will be at-premid will be equal to primid in my
[25:42] will be equal to detail and we will use iteration iteration and index 0
[25:59] and in here we will use minus 1 for the sparing put so let's create that sparing put
[26:08] and we will connect the meta node
[26:15] so
[26:24] let's let's see
[26:26] let's forget that for now actually we will need to delete non-selected
[26:41] so if we do this we have this one
[26:47] and if we go for single pass 2 we have this one so it's working
[26:52] and now having this we can create some normals to extract these points these edges
[27:03] so we can use it for cutting our geometry so let's go with the polyframe
[27:12] and let's say the tangent name will be in
[27:22] so we have done like this and now we can just
[27:26] just
[27:29] drop it
[27:32] let's go with group
[27:36] and say edges
[27:41] and keep by normals 1
[27:48] let's go minus 1
[27:50] and this should do the trick
[27:55] now we can just convert it to curves
[27:59] curve
[28:02] group 3
[28:08] from here we can
[28:11] as you can see this is
[28:12] this is a single primitive so a single curve so what we can do is to cut it so
[28:22] probably cut
[28:26] and let's say cut and cut point so now if we don't exploit it we have to separate geometries
[28:39] let's
[28:43] now see how we do this so let's split
[28:52] and let's split primitive 0
[28:56] and we can create a wrangle
[29:03] and copy this one in here
[29:09] so
[29:12] what we can do
[29:19] first of all
[29:26] yet we will need to orientate first the two curves
[29:33] so let's do oriental curve
[29:38] so oriental curve
[29:43] after the cut
[29:48] and we need to set it to point and we need x axis so let's go and
[30:01] we might need to reverse this let me see
[30:09] we need them pointing outwards let's see if we reverse in here
[30:21] now it's working properly
[30:25] so now we in a clip
[30:30] we can set the direction
[30:42] we can set the direction
[30:48] not here let's see as you can see we can set the direction and that's what we're
[30:53] going to use to cut the corners so let's create the direction
[31:00] direction attribute so and we will need two clips one for the left and one for the right so
[31:06] direction one will be point and input one and and zero and let's do the direction two to
[31:22] direction two will be input input two and the normal
[31:30] so in here we will connect input two to two so zero one two and in the clip
[31:39] now we can set the first direction
[31:46] so in the clip let's go with point
[31:52] and let's use sparing puts minus one because we will compile this
[32:00] and direction one and zero and let's add the sparing puts so let's sparing put let's connect this
[32:12] so index zero components
[32:21] and components two
[32:28] so we might need to change this primities below the plane so now we just created the cuts on the right
[32:37] and let's create another clip just copy this one and we can set the sparing put to the above
[32:53] unit in all let's say direction two direction two direction two and that should look a trick
[33:07] now hopefully we should have everything working let's see
[33:12] let's change the single pass and it works on all the prims but one because the normals are
[33:23] inverted so in here we need to check each which so is the single pass one so the pass one
[33:38] and for that we can just get rid of the reverse so let's create a switch
[33:46] and use the reverse and use not the reverse in the second input let's say
[33:55] a detail let's use the iteration so we can just copy create the sparing put
[34:09] and connect the metadata now let's say detail minus one
[34:20] the iteration zero is equal to one so that should do the trick let's remove the single pass
[34:34] and there we we have it everything cuts perfectly
[34:41] now we can just compile this so let's get the compile plot
[34:50] now let's add it in here and in here let's see if it's ready
[34:56] and this should do the trick
[35:04] let's just see it's mostly
[35:12] it's just warnings that we don't need to we don't need to pay attention
[35:20] so from here I'm just going to show you what's done so let me just copy
[35:33] it
[35:47] from here
[35:51] oops
[35:52] oh the object merge we need to make sure we use this one
[36:00] and the same here this one is fine so I just copied a few tiles in here pretty pretty easy
[36:13] just create the curves and a few attributes the aperture would get rid of the middle ones
[36:21] create a p-scaled attribute and we have another model of a tile you can get this on my patron
[36:28] the project file and in here I'm just creating two different tiles oriented and slightly
[36:39] offended and then add a boolean at the end to unify everything not perfect but that should work
[36:48] I'm just doing this now because it's already a very long video and I don't want to bother you anymore
[36:58] so you can grab the files on my patreon if you want to and explore it on your own
[37:07] so I just want to mention that I just created a new course called Roman Bridge
[37:13] procedural asset creation and I also have another modeling course you can check those out
[37:22] so I have this one that is the old course not very old it's still on out in 19.5
[37:30] and I have this new course that I just created that I believe it might interest you if you want to
[37:38] to dive into proceduralism so that's basically it's if you guys want the project files just check
[37:47] my patreon I will be uploading to there and I hope that you have learned something new today
[37:54] thank you and see you next time



---

## Captured Frames

- [0:30] tutorials/frames/procedural-roof-tiles-in-houdini/frame_000.jpg
- [4:10] tutorials/frames/procedural-roof-tiles-in-houdini/frame_001.jpg
- [8:00] tutorials/frames/procedural-roof-tiles-in-houdini/frame_002.jpg
- [12:30] tutorials/frames/procedural-roof-tiles-in-houdini/frame_003.jpg
- [17:30] tutorials/frames/procedural-roof-tiles-in-houdini/frame_004.jpg
- [21:40] tutorials/frames/procedural-roof-tiles-in-houdini/frame_005.jpg
- [25:50] tutorials/frames/procedural-roof-tiles-in-houdini/frame_006.jpg
- [29:10] tutorials/frames/procedural-roof-tiles-in-houdini/frame_007.jpg
- [32:30] tutorials/frames/procedural-roof-tiles-in-houdini/frame_008.jpg
- [35:50] tutorials/frames/procedural-roof-tiles-in-houdini/frame_009.jpg
- [37:30] tutorials/frames/procedural-roof-tiles-in-houdini/frame_010.jpg

---

## Structured Notes

### Core Technique
A full step-by-step build of a procedural pyramid-roof tile system: hand-derived VEX cross-product orientation per roof face (out/side/normal basis vectors), area/bounding-box math to compute each face's real-world width and height for correctly-scaled tile grids, and a compiled per-piece for-loop using Clip nodes (instead of slow Boolean) to cut individual tiles cleanly along each face's true edges.

### Summary
Starting from a grid with alternating-triangle connectivity, the center points are raised and the roof pyramid's rough shape is formed, then unneeded middle edges are removed. Since copying flat tile grids directly onto the sloped roof faces gives wrong orientation, the video derives correct per-face orientation from scratch in VEX rather than relying on default aperture vectors: an "out" vector is built by normalizing the point position minus the flattened (Y=0) centroid-projected point, a "side" vector is the cross product of "out" and up, and the final normal is the cross product of "out" and "side" — giving each triangle face a consistent local basis regardless of the original grid orientation. To size the tile grid correctly per face, Measure computes each face's Area, then a wrangle branches on whether the face's normal is closer to the Z or X axis (`abs(N.x) < 0.001`) to decide which bounding-box axis represents "width," deriving "height" from the classic triangle-area formula (`2 * area / width`). These width/height values are passed into a for-each loop (with Fetch Feedback to reference the first iteration's point) that sets the corresponding grid's Width/Height parameters, plus a generated string ID per primitive (`itoa(primnum)`) and per-face row/column density attributes computed by multiplying the size components by a user-set density multiplier. A margin/room system reserves buffer space at the roof edges (via bounding-region point groups plus a Transform centered on the object, to correctly select even corner points) so tiles don't overhang past the roof silhouette — with an adjustable "group expand" amount trading overhang room for tighter tile fit. Actual tile geometry is copied to points via centroid extraction and normal transfer with a 90° rotation and a computed "up" attribute, then cut per-piece using a **compiled for-each loop over each primitive ID** (using a Blast + Meta Import iteration index to isolate one piece at a time) with **Clip nodes** — driven by direction attributes derived from Oriented-Along-Curve on cut curves — rather than a Boolean, since Boolean was too slow for this many per-piece cuts; a Switch based on a "reverse" detail flag per iteration corrects normal-direction inconsistencies found only on one particular piece. The compiled loop's warnings are noted as safe to ignore. The author's finished project files (a paid Roman Bridge asset course and a paid Church Ruins course) are mentioned as the source material this roof system feeds into.

### Key Steps
1. Base pyramid shape: Grid with **Alternating Triangles** connectivity for a natural triangulated roof base; raise the center point(s) via Transform/bounding-regions selection, then remove unneeded middle edges via Blast.
2. Add vertex normals (set to 0 initially since the copy source will be grids used to instance tiles); extract centroid, promote/transfer normal to primitive via **Attribute Promote** (transfer attributes → normal).
3. **Custom orientation VEX** (rather than relying on default aperture): compute `out` as the normalized vector from the flattened (Y=0) centroid-referenced point to the current position; compute `side` as the cross product of `out` and world-up; compute the final `N` as the cross product of `out` and `side` — giving each triangle a consistent, correctly-oriented local frame regardless of source topology.
4. **Measure Area** per primitive; in a wrangle, branch using `abs(N.x) < 0.001` (or similar axis check) to decide whether a face's bounding-box X or Z size represents its "width" (since roof faces on different sides of the pyramid are oriented along different world axes), then derive "height" via `height = 2 * area / width`.
5. Create a string ID attribute per primitive using `itoa(primnum)` for later per-piece targeting.
6. Density attributes: multiply the width/height components by a user-controlled density value to compute the number of rows/columns needed, stored as two named float attributes.
7. **For-each loop** (by primitive, Fetch Feedback mode where needed): reference point 0 of the first loop iteration to pull the width/height attributes onto the tile grid's Width/Height parameters via copy/paste-relative-reference, so the grid auto-adjusts per-face without hardcoding.
8. **Divide** the sized grid to subdivide it cleanly (respecting the initial topology so the tile count stays procedural), clean any inner polygons produced.
9. Extract the centroid of divided-cell groups and blast the center points to treat them differently (a separate detail pass); extract the middle edge and resample it to the target tile-per-row count for the ridge-cap row, giving it a distinct ID.
10. **Margin/room system**: use bounding-region point groups (with an object-centered Transform so corner points are also correctly selected) to reserve edge buffer space, so tiles don't overhang the roof silhouette; use **Group Expand** to control how much room is left — more room needed for larger tile counts.
11. Copy the actual tile profile geometry onto the sized/positioned points via **Path Deform**, transferring the original geometry's normals; orient copied tiles with a Polyframe/normal-based up attribute plus randomized normals/scale, then **Copy to Points** using a "piece" ID attribute.
12. **Per-piece cutting via compiled loop**: since a straight Boolean approach was too slow for this many individual tile cuts, isolate one piece at a time inside a **Compile Block** using Blast driven by a Meta Import iteration-index detail attribute, then cut each piece cleanly using **Clip nodes** whose direction is derived from **Orient Along Curve** run on the cut curves (rather than Boolean geometry intersection).
13. Fix inconsistent normal direction found on one specific piece using a **Switch** driven by a per-iteration "reverse" detail flag (`detail(-1, "iteration", 0) == 1`), so only that piece gets its clip direction flipped.
14. Compile the loop (ignoring benign compile warnings) for fast, scalable per-tile cutting across the whole roof.

### Houdini Nodes / VEX / Settings
Grid (Alternating Triangles), Transform (center-point raise, bounding-region selection), Blast, Attribute Promote (vertex→primitive normal transfer), Attribute Wrangle (custom `out`/`side`/`N` cross-product orientation basis), Measure (Area), width/height branch wrangle (`abs(N.x)` axis check, `2*area/width` formula), `itoa()` string ID, density-attribute multiplication, For-Each loop (Fetch Feedback, point-0 parameter reference via paste-relative-reference), Divide (topology-respecting subdivision), centroid extraction + Blast (center-tile isolation), Resample (ridge-cap row), Group (bounding regions, object-centered Transform for corner selection), Group Expand (margin control), Path Deform, Polyframe/normal-based orientation, Attribute Randomize (normals/scale), Copy to Points (piece ID), Compile Block, Meta Import (iteration index), Blast (per-piece isolation), Clip (direction-driven cutting), Orient Along Curve (clip-direction derivation), Switch (per-iteration reverse-normal fix via detail attribute).

### Difficulty
Advanced (hand-derived VEX orientation math, area/bounding-box-based sizing formulas, and a compiled per-piece Clip-based cutting loop are all non-trivial techniques).

### Houdini Version
19.5.598 (visible in viewport title bar).

### Tags
vex, uvs, divide, for-each-loop, compile-block, roof, architecture, procedural-modeling, dihedral

---

## Related Tutorials
- [Procedural House Generator](procedural-house-generator.md) — reuses this exact roof-tile system (manual UV-space flattening, Divide-based tile grid, Path Deform) as part of a larger house-generation pipeline.
- [Procedural Tips #3 VEX Shading and Loops](procedural-tips-3-vex-shading-and-loops.md) — offers a simpler VEX shortcut (bbox_max-based normal derivation) for the same roof-tile orientation problem tackled here from scratch.
