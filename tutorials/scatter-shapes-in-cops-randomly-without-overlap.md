---
title: Scatter shapes in cops randomly without overlap
source: YouTube
url: https://www.youtube.com/watch?v=bTA8XwTEcRg
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [cops, point-relax, uv-gradient, tiling, matrix, stamping, rock-material, seamless]
extraction_status: complete
frames_dir: tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Scatter shapes in cops randomly without overlap

**Source:** [YouTube](https://www.youtube.com/watch?v=bTA8XwTEcRg)
**Author:** cgside
**Duration:** 13m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I wanted to break down now I did the
[0:04] simple material of a couple stones that are like randomized and don't collide
[0:10] with each other. I'm not sure how they approach this kind of material in
[0:13] substance designer but in Odini is not as easy as it seems because for example if I
[0:20] create the different variation of the rocks which I did here and then I import
[0:25] them and try to apply for example with scatter shapes as soon as I increase
[0:30] the jitters you can see they will go over each other and I have to find a
[0:35] solution for this it's quite a bit of work but hopefully you'll get the idea
[0:39] so let's get into it. So the first thing I'm doing in here is just creating the
[0:46] different variations so in this case I chose four and they look something like
[0:51] this well I still did some things to it and they look more like this let me
[0:56] get rid of this triple lighting so they look something like this then I will
[1:01] have more effects on top. Then what I do is I bring this is a nightmare and I
[1:06] bring with a remap note I create a mask and this is what I will export to
[1:12] soft to isolate each rock and bring it as a new cop layer so that's what I'm
[1:19] doing in this subnet so you can create a subnet in cops go inside and since we
[1:23] don't have loops or loops in cops so we have to do these in subs but it's
[1:29] simple. So let's dive first into the copnet so I have the four variations then
[1:34] I'm isolating each tile based on the iteration doing just the math to divide
[1:38] these into four tiles into four sections I mean then I extract the different
[1:44] rock based on the iteration of these loops so this note then I just set the
[1:48] name at first I add other layers but I just ended up using the Ipe so if we
[1:53] have a look on each iteration we have a different rock isolated so in this
[1:57] case I only have four so it's fine. Okay now what's next so as I told you I
[2:04] import those layers and do a geo to layer and extract all the variations so now
[2:09] they leave on cops as a layer so they are not because in year they are still
[2:14] geometries since I did it in a subnet so I bring all the so I'm not visualizing
[2:19] this okay I bring them into cops with a geo to layer then I do a cable pack and
[2:23] I feed that to the stem cop and that kind of works and I can play with the
[2:30] variation so in this case I only have four I set it to four to random and play
[2:34] but this works fine for for these more systematic materials but as soon as I
[2:42] want to add variation as you can see it completely breaks and again I'm not
[2:46] very experienced with procedural materials but I had to dig deeper to find a
[2:51] solution so what I ended up doing was importing the same rock geo to layer as
[2:58] always cable pack then I make sure they don't tile and then I cable renamed it to
[3:06] shape which will feed the the special ports in the open CL nodes or any other
[3:11] nodes in cops that support these years I'm not sure what they they are cables
[3:16] anyways so I bring them and I stamp them manually with this custom stamping
[3:23] that I did it I called it's templates is not a tool is just something I build
[3:26] for this and basically this is a bunch of points that I bring from subs with
[3:31] the transform attributes four by four transform so a matrix four and I iterate
[3:37] over the all the points and then I manipulate the UVs with my transform and
[3:44] it finally stamp it with image sample so that's basically it and the idea I
[3:50] wanted to show you and by the way this as soon as I place a layer properties
[3:57] this will tile as you can see and it's not as easy as it seems to make it tile
[4:02] but I will show you how I did it with this with this point so this is just a
[4:07] bunch of points at the origin 100 points to be specific that's the we'll make
[4:15] it stamp the points in here so right now they don't tile but as soon as I place
[4:20] a layer properties will drop it so let's look at those points at the top so as you
[4:25] can see it's a bit of a work but basically we end up with this tile with this
[4:30] tile visualization as you can see they tile what did I do in here so I bring my
[4:34] variations in with a trace node from that mess we created and I
[4:39] numerate them to have a class attribute so like a variant attribute so each
[4:43] rock has a different variant all right then I generate a grid in this case I
[4:48] chose 10 by 10 so 100 points with point and rate create an index because we will
[4:52] use it later and then I gridify it with this wrangle this way with the wrangle I
[4:57] can set a column and a row attribute and as you can see they are in the middle
[5:01] of the grid point of the grid landmarks so they are not exactly at one and minus one
[5:08] then I create an attribute from pieces to create a variant attribute like we do
[5:14] like we do with a copy to point so I basically enumerate them here then do a random
[5:20] random variation in here with a class so the class 4 will have a bunch of points the class 2
[5:26] and other at a point and so on so as you can see from here so from 0 to 3 that's simple
[5:33] then I create a piece scale and some random attributes like normal and end up to
[5:39] instant some points but at this point they all go over each other because I place this
[5:43] attribute noise to give it some variation and whatnot that I will on purpose disable this node
[5:49] in here where I match the attributes of to make it tile and we will come back to it later
[5:55] so what I do then is to pack this geometry and do a relax and this will relax based on the
[6:01] piece scale we set in here so in here I did a random piece scale as you can see I can change it
[6:08] and whatnot and this will always relax them so I do this point relax then I apply some noise
[6:14] and I match the attributes again so then it breaks okay that's fine
[6:25] okay they break because I don't have this because I met you in here of course sorry about that
[6:35] I was just posting the video and thinking my life choices right now so don't worry as you see if
[6:42] we don't have these match attributes it will break the tiling so this is just a preview of the
[6:47] tiling so I can make sure it tiles so you can see you see the workflow we relax the points and now
[6:53] we have these they apart from each other and they don't overlap anymore and we still can apply a
[6:58] small noise to make it a bit more to give it a bit more variation so that's how I'm doing it
[7:06] okay let's look at the what makes it tile so basically I take in here we have the points
[7:14] and we need to match these attributes the orientation attributes the variant attributes and the
[7:19] position of those points to this column from this column to this column and from this row to this row
[7:25] and also the corners so and that's what I'm doing in here I have a function called copy attributes
[7:30] that basically will copy from one to another one to another and then is just a matter of matching so
[7:35] if the column ID is columns minus one so the last one we create a source which in this case I
[7:42] just take the point number and subtract the the last column so calls minus one which is nine and
[7:50] we go back to the first column so we want to copy from this and we do the same for all the columns
[7:55] and I also create some groups in here so that's how I match the different attributes and when we copy
[8:03] oh sorry when we copy there will be tiling as you can see of course this is a bit
[8:10] too uniform and it might be visible on the tiling way or if you tiling too much but then again
[8:16] there are other techniques to solve that so I can actually show you how I created the transformator
[8:23] root because as a challenge and yeah mostly as a challenge I wanted to have just a bunch of points
[8:29] in the center and stamp those points so how did I create that transformator root so after
[8:35] matching the position again in here very similar to what we did in the match attributes because I
[8:40] introduced some noise and it would break a bit the tiling so I just did it again then I am measuring
[8:46] the area for the scaling so I can match the scale so measuring the area by piece promoting the
[8:53] position to a centroid so I can have a center point for each piece based on the index the index is
[8:59] in here each individual route that we have in here not the variant so it's just like a class attribute
[9:07] then I measured the gradients of the UVs and that's what I'm using to feed in the transformator
[9:12] root so if you look at these gradients so how do I add that how is it called UVX so UVF and I need to
[9:24] set it as a vector so it's just a vector pointing in the x-axis of the UVs and I do the same for the y-axis
[9:31] so this and since we have two stable vectors we can create a transformator root here I'm just
[9:37] calculating the scale vector from the original pieces that are this size to the new pieces that
[9:46] we have in here the in here I'm just building the transform as you can see so taking those vectors
[9:52] and creating a matrix with a four by four matrix so I just normalize the vectors get the pivot to do
[9:58] the translation and as always you do the scale you do the rotation and then you do the translation
[10:03] and I also saved those as matrix and one the pivot then I extracted the points in a point
[10:09] wrangle and transfer the attributes and I do the same on this side on this side so on this side we
[10:15] have just a copy to points I move them to the center so by subtracting the centroid then I do the
[10:21] same measurements and create the transform the same way this one is simple because it's just
[10:31] this could be easily I identity matrix so I'm just doing it this way then I extract the points
[10:36] and as you can see they are they are at the middle and then I can save the matrix by reading the
[10:43] the same one from this input no sorry I have the points in here with the matrix then I do a
[10:48] difference matrix which is just the one inverted by multiplying an inverted matrix by the
[10:55] current matrix in this case we don't make much difference because this one is just an identity matrix
[11:00] so I just do that and then I save the save data that transform any if I preview and I object merge
[11:09] all at the top so these are original shapes so these are just four shapes that we have in here
[11:14] I just move them to the center so I can easily apply the transform and if we copy the points with
[11:20] that transform attributes we have now we should have the same result in here as we have in here as
[11:26] you can see so they are in the same position because I'm saving these as transform attributes again
[11:32] I did the scaling I did the translation by the centroid and I did the rotation with those
[11:38] vectors from the ovis in this case it was easy to create the transform attribute because I could
[11:42] just use the ovis okay guys that's basically it as you can see it tiles perfectly and if I come
[11:51] in here you can see how it works and if I enable these let me go back to this transform and I can
[11:59] play in here with the noise the same in here as you can see of course this is not especially to
[12:08] randomize but you know that's the best I could do maybe you have another idea and now I have this
[12:14] problem that I'm getting it starts to to to have this time dependency what I usually do is just
[12:21] to disable one of the nodes and now it works yeah guys that's basically it then I apply a few more
[12:28] more effects I bought these plugin from cobstains I think that's the name that's just 20 20 something
[12:37] euros but you have these substance designer nodes to apply slowblurs and whatnot and you are I'm
[12:44] just gonna warn you that if you open this file on patreon you will have maybe a problem with these
[12:49] specific nodes but again the same workflow the the soft workflow and everything will be there so you
[12:55] can have a look okay guys I admit this is a rabbit hole and probably it's just over your ad but
[13:02] I tried to explain it as much as I could hopefully you'll find it useful as always thank you for
[13:08] watching and you can grab the files on my patreon alongside with exclusive tutorials and hours and
[13:14] hours of exclusive tutorials all the files of my videos and yeah thank you for watching and I guess
[13:20] I'll see you next time thank you



---

## Captured Frames

- [0:55] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_000.jpg
- [1:40] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_001.jpg
- [3:00] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_002.jpg
- [4:20] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_003.jpg
- [5:40] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_004.jpg
- [7:00] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_005.jpg
- [8:20] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_006.jpg
- [9:50] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_007.jpg
- [11:10] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_008.jpg
- [12:30] tutorials/frames/scatter-shapes-in-cops-randomly-without-overlap/frame_009.jpg

---

## Structured Notes

### Core Technique
Scatter multiple rock-shape variations across a seamlessly-tileable material without any overlap — the default Cops "Scatter Shapes" node breaks down as soon as jitter is increased (shapes clip through each other), so the fix is a SOPs-side pipeline: **pack the shapes as points, run a p-scale-aware point Relax to physically push them apart**, then feed the relaxed positions/orientations back into Cops via a custom stamping setup, plus a from-scratch **UV-gradient-based transform-matrix** system to make the tile pattern wrap seamlessly at all four grid edges/corners.

### Summary
Four rock variations are modeled in SOPs, masked out individually (a subnet used only because Cops lacks native loops — the subnet does the per-variation math and outputs each rock's mask as an image layer), then imported into Cops via Geo-to-Layer, Cable Pack, and stamped with the built-in Stamp Cop — which works fine for a small, systematic set but breaks down (heavy overlap) as soon as jitter/variation is increased for a more organic look. The fix moves variation-placement math into SOPs: a 10×10 grid of points (100 total) is built with Point Generate, given column/row attributes via a wrangle (offset so grid points sit at cell centers, not at -1/1), and each gets a random `variant` attribute (0–3) via Attribute from Pieces (based on a per-class enumerate on the imported rock variations) plus random p-scale/normal/orient attributes to instance geometry — but at this stage pieces still overlap heavily because of the added noise-based attribute jitter. **Pack the geometry, then run a point Relax** driven by each piece's p-scale — this physically separates overlapping instances based on their actual size, guaranteeing no intersections; a small amount of additional noise can be reintroduced afterward without breaking the relax result, as long as the attributes are re-matched before the tiling step (otherwise tiling breaks). To make the grid **tile seamlessly**, a custom function (`copy attributes`) copies orientation/variant/position attributes from the last column to the first column and from the last row to the first row (and handles corners), so points on opposite edges of the tile match exactly — visualized as a small preview grid of ~100 points at the origin that only actually tiles once a Layer Properties node is set (otherwise the pattern visibly repeats/drops at tile boundaries). To stamp geometry with correct scale/rotation at each point (beyond simple position matching), a from-scratch **transform-matrix pipeline** is built: measure each piece's area (by-piece, promoted to a per-piece centroid based on an index/class attribute, not the random variant), then **measure the UV gradients** (`uv.x` and `uv.y` as separate vector attributes, `UVF`) to get two stable per-piece coordinate axes usable for constructing a matrix — since the original pieces and the copy-destination points differ in scale, a scale vector is computed between them, and a full 4×4 transform matrix is built from the gradient vectors (normalized, used as look/up axes), a translation to the point's pivot, and the computed scale, producing a matrix that (when applied) reproduces each piece's original position/orientation exactly if fed identity scale, or the destination's actual scale/rotation otherwise. A "difference matrix" (an inverted-matrix multiply against the current matrix) is also saved for cases needing a relative rather than absolute transform. Once verified (object-merging the 4 original variant shapes at the top of the network, moving them to the center via Copy-to-Points with the built transform attributes to confirm they land back in the same position/orientation), the technique reliably tiles the scattered rock pattern with per-piece random scale/rotation and zero overlap, and can be further randomized (with the same noise-then-rematch caveat) before handing off to a paid Substance-Designer-style plugin node for slope blur / noise post-processing.

### Key Steps
1. Model 4 rock-shape variations in SOPs; isolate each with a subnet-based per-iteration mask (subnets used specifically because Cops has no native loop construct) and bring them into Cops as separate mask layers via **Geo to Layer**.
2. Use **Cable Pack** + the built-in **Stamp** Cop to place the systematic set — works for small, uniform variation counts but breaks (heavy overlap) once jitter is increased for more organic placement.
3. Build a **10×10 Point Generate** grid, derive column/row attributes with a wrangle (offset so points land at cell centers), and assign a random `variant` (0–3, via Attribute from Pieces keyed on an enumerated class) plus random p-scale/normal/orient attributes for instance variation.
4. **Pack the resulting geometry, then run a point Relax driven by each piece's p-scale** — physically separates overlapping instances based on true piece size, eliminating intersections that naive jittered placement would otherwise cause.
5. **Make the grid tile seamlessly**: build a custom "copy attributes" pass that copies orientation/variant/position from the last column to the first column and last row to first row (handling corners too), so opposite tile edges match exactly; verify by placing a **Layer Properties** node (without it, the preview looks fine but doesn't actually repeat correctly across tile boundaries).
6. If adding extra noise/randomization after relaxing, always **re-match the tiling attributes afterward** — noise alone will break the seamless-tile matching if left unmatched.
7. **Build a from-scratch transform matrix per stamped piece**: measure each piece's area (grouped/promoted by index/class, not the random variant), then measure the **UV gradients** (`uv.x`, `uv.y` as separate vector attributes) to get two stable, piece-relative coordinate axes.
8. Compute a scale vector between the original piece size and its destination point's size, then build a full 4×4 matrix from the normalized gradient vectors (as look/up axes), the point's pivot as translation, and the computed scale.
9. Extract points from the transform network and transfer the matrix attribute, saving an optional "difference matrix" (current matrix × inverted reference matrix) for cases needing a relative rather than absolute transform.
10. Verify by object-merging the 4 original variant shapes, moving them to center, and Copy-to-Points-ing with the built transform attribute — confirms each piece lands back in its original position/orientation before trusting the matrix pipeline for the full tiled scatter.
11. Optionally layer in a paid Substance-Designer-style Houdini plugin (slope blur, Voronoise, etc.) for additional post-processing once the base tileable, non-overlapping scatter is confirmed correct.

### Houdini Nodes / VEX / Settings
Cops: Geo to Layer, Cable Pack, Stamp, custom subnet (per-iteration masking, loop substitute), custom "copy attributes" tiling function, Layer Properties (tile verification). SOPs: Point Generate (10×10 grid), column/row wrangle, Attribute from Pieces (variant selection via enumerated class), random p-scale/normal/orient attribute noise, Pack, point **Relax** (p-scale-driven, non-overlap guarantee), Enumerate (class attribute), area Measure (by-piece, index/class-grouped), UV gradient Measure (`uv.x`/`uv.y` as vector attributes, "UVF"), scale-vector wrangle, 4×4 transform-matrix construction (gradient-based look/up axes + pivot translation + scale), difference-matrix wrangle (inverted-matrix multiply), Point extraction + matrix attribute transfer, Object Merge (verification), Copy to Points (transform-attribute-driven placement).

### Difficulty
Advanced (the UV-gradient-based from-scratch transform-matrix construction and the p-scale-driven Relax-for-non-overlap technique are both sophisticated, non-obvious production solutions to a real material-authoring problem).

### Houdini Version
Not specified.

### Tags
cops, point-relax, uv-gradient, tiling, matrix, stamping, rock-material, seamless

---

## Related Tutorials
- [UV Randomizer - Texturing Multiple Objects](uv-randomizer---texturing-multiple-objects.md) — shares the piece-scattering-without-overlap goal, using Connectivity+ID+Sort for UV-space stacking instead of a physical point Relax.
- [Procedural Environments in Houdini | Patreon February '26 Free Lesson](procedural-environments-in-houdini-patreon-february-26-free-lesson.md) — shares the OpenCL-based custom Cops workflow approach used here for organic edge/tiling effects.
- [Wood Barrel Texturing in Cops](wood-barrel-texturing-in-cops.md) — shares the uvdist()/UV-gradient-based attribute-resurrection approach for building custom per-piece Cops workflows.
