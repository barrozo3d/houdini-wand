---
title: Dusty Bottles - Bridging procedural workflows in Houdini and Solaris
source: YouTube
url: https://www.youtube.com/watch?v=CHySFnWfKLk
author: cgside
ingested: 2026-07-13
houdini_version: "20"
tags: [modeling, vex, vdb, tops, solaris, lops, karma, materials, shaders, procedural, usd, advanced]
extraction_status: complete
frames_dir: tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Dusty Bottles - Bridging procedural workflows in Houdini and Solaris

**Source:** [YouTube](https://www.youtube.com/watch?v=CHySFnWfKLk)
**Author:** cgside
**Duration:** 19m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video, I'm going to be breaking down the simple render from procedural modeling
[0:07] tips and tricks to Solaris workflows.
[0:10] So yeah, let's start from the Geo container in here, on top.
[0:17] I always like to do things on subs first instead of doing a subcreate because then I can
[0:22] export easily to USD and reference that in Solaris.
[0:26] So of course I started by modeling the bottle, so the wine bottle.
[0:33] Doing a sample just to, after of course the wine bottle, I'm doing a sample just to sort
[0:40] the points so I'm not even subdividing.
[0:43] Creating in here, me increasing here the point size and also in here.
[0:51] So I'm creating in here a group by rain to select part that I'm going to extract later.
[0:58] Then also selecting a point for the UV themes, revolving and at this point I'm also creating
[1:03] the UVs as you can see, but I'm not going to use these UVs because they are not very
[1:08] good in my opinion, at least for the thing I want to do.
[1:12] But I'm still computing them because I'm going to use the same for later, so I don't have
[1:17] to select it manually.
[1:19] Pusing because at the bottom there's an open point in there.
[1:23] Group promoting the same two edges and UV flatten.
[1:26] And I'm using rectify.
[1:27] I know this is not very accurate because the UVs are decreasing at the top, but I prefer
[1:34] it this way because I can have clean UVs to work with to do their projections.
[1:40] From here this is just the bottle geos, so I'm poly extruding, subdividing, subdividing
[1:44] a bit more for some reason.
[1:45] And as you can see I have the thickness and that's the bottle.
[1:48] Then we move into the top part and I completely forgot how is that called, but yeah I'm going
[1:54] to call it top parts.
[1:56] So I'm group promoting that range pointer to good that got promoted to got expanded to
[2:04] all these frames.
[2:06] Blessing that part, picking a little bit and creating the Unshared Points group with
[2:12] the boundary group so I can promote them individually.
[2:15] So I can, for example, fill the top part and not the bottom.
[2:20] From here what am I doing in here?
[2:21] So I'm selecting every other vertices, vertex and promoting to an edge group.
[2:28] This way I can convert these two lines and create at the end the drips of these top
[2:35] part, as you can see, this is the top part that I'm referring.
[2:38] So in order to do that, after the convert line I'm creating an aperture boot just by normalizing
[2:43] P and I can show you actually how that looks.
[2:46] So that's that as you can see just pointing out and I did normalize it, but since I'm working
[2:52] in real world scale, this might be a bit to some for the visualizer.
[2:57] Then I'm selecting randomly some frames with this random expression and I've received
[3:01] and whatnot.
[3:02] Blessing those frames, doing a attribute, a attribute randomized for a curve attribute
[3:08] that I'm feeding in here to the curve.
[3:10] So this is new.
[3:12] I believe we've been losing to see now the need to 20 so you can curve via attributes.
[3:16] So some are longer, some are smaller, just feeding these attributes randomized.
[3:21] Reassembling, creating the p-scale with this back snippet just by creating a ramp on
[3:27] the curve view because I'm outputting curve view in here and then make sure the mean p-scale
[3:33] is 0.6 with this max expression.
[3:37] I'm just sweeping and I'm using a second input in here which is this flat shape so I
[3:42] get this flat look instead of the rounded one by default.
[3:45] VDB from polygons and in here I'm doing this part so I'm blessing away those bottom
[3:54] primitives by grouping by range with the divisions of that revolve.
[3:57] So always procedural.
[3:59] Only feeling on the top, extracting these polyfill at the bottom, doing a slight transform,
[4:08] remashing and mountain so I can woolean out the shape and extract the largest piece as
[4:13] you can see in here.
[4:16] So I have these randomized at the bottom.
[4:19] Doing a poly extrude subdivide that is not working perfectly in here because we have
[4:23] the Boolean but then I'm just doing a VDB from polygons combined with SDS union and
[4:29] we have both shapes united then VDB reshape, VDB smooth, VDB reshape again to do some
[4:35] dilation and convert it.
[4:37] But since I don't like these topologies, since I have exosite quadrimeshers, I can easily
[4:41] remesh it.
[4:42] It didn't work so well with the Aldini default quadrimeshers so I ended up relying on this.
[4:48] I tried to avoid to use plugins for tutorials because some of you might not have it but this
[4:53] tool is really really good, this exosite quadrimeshers.
[4:57] I'm just adding some color.
[4:59] In here these pink nodes are the ones that I am driving in a topnet.
[5:04] By a topnet I mean to randomize the variations that I'm going to cover next then just
[5:09] doing a name and deleting some of the attributes.
[5:11] So what else am I missing in here?
[5:13] So we cover this part, we cover this part and after this bottle I'm creating some dust
[5:21] with layers so I'm blasting just the outside part, merging it over with the top which right
[5:28] now it doesn't show because the variation right now is set to not show that top part.
[5:36] But anyways, I'm creating a natural boot noise vector so just zero centroid offset and
[5:43] then in here I'm just creating a mask.
[5:46] So as you can see I'm creating a mask to fit the dust layer and the air generation.
[5:51] So just adding a bit of noise to the normals and capturing the normals outweighs so the
[5:56] parts that should collect dust and I'm adding a bit more randomization since in my reference
[6:02] it was all over the place.
[6:05] Doing an air gen in here masking the thickness by a mask and masking also the density by
[6:10] that mask we generated.
[6:12] Add the length randomized, let me see, do some bending also and some freeze and some
[6:23] clamping here because I noticed in my reference that some of the dust was in similar clusters
[6:32] and then attributally the name and that's our dust that will combine with the different
[6:36] material later.
[6:38] What do we have in here?
[6:40] So in here we have these details I'm calling it details.
[6:44] It's just like a label and some some chords.
[6:51] So I'm object merging the the bottle then subdividing and in here I'm creating a curve just
[7:00] with two points and poly extruding and mirroring so it's and end up intersecting the bottle.
[7:08] And I'm doing a billion in sim modes using resampling and make sure it's on the bottle.
[7:16] Recymbling doing a small mountain to distribute it using and doing a sweep and this sweep
[7:22] is that round tube and columns and I'm also doing some twist.
[7:26] Then I'm doing another sweep to generate curves on curves, doing round two columns and
[7:31] also do some twisting.
[7:33] Then I'm doing some randomization of B by using a natural noise vector and I'm also setting
[7:42] a different offset for each frame as you can see in here.
[7:44] I'm just adding to the offset.
[7:46] That's what gives it a different look.
[7:50] So which curve will receive a different seed.
[7:53] Then just sweeping with round two nothing special and we get these, what is it called?
[7:56] Rob some sort of rope here.
[7:58] That's what I mean by chord.
[8:00] Then I'm doing another sweep on this side but steady to rows sorting lap sort with doing
[8:06] a circular sort.
[8:08] Then just grabbing the first frame.
[8:11] So this one in here and blasting, transferring it a bit and doing a sweep and this will
[8:17] end up with something like this.
[8:20] Then after this transform I'm selecting one of the points at the edges doing a small transform
[8:26] and blasting away that specific point or keeping that specific point.
[8:31] Then just duplicating in this case I'm using a network wrangle running by numbers.
[8:36] I just need two points so that's easy.
[8:39] Then we can take the LMNUM which is like the pitinum in this case or the iteration that
[8:44] we're running and do zero centred offset with design.
[8:48] Then we can move the position dot that and move it a little bit so you can control
[8:53] is in here.
[8:54] I'll remove.
[8:55] Which was just a quick way to create two points.
[8:58] Then adding and poly extruding, subdividing, doing a mountain and adding some thickness.
[9:04] So that's how I created that detail in there.
[9:08] So for some reason I press shift S.
[9:11] Yeah, now the so I prefer the wires like this.
[9:15] So let's see.
[9:17] We have these.
[9:19] Then I'm also doing some corking here so that's pretty simple.
[9:25] This is not the core.
[9:26] Yeah, it is the core.
[9:27] So I'm doing that subdividing, poly feeling, blasting away the field, picking up a little
[9:32] bit, scale it, reverse it, extruding, bivaling, doing the quadri measure and selecting manually
[9:40] some seams and doing the yogis as you can see.
[9:44] And subdividing and mountain, that's the core really simple.
[9:47] Did I cover these?
[9:49] Yes.
[9:50] So that's basically it.
[9:53] And all these pink nodes are driven by a top network.
[9:57] As you can see, I have the noise offset.
[10:00] So I can have different dust patterns.
[10:02] And I'm driving that by a wedge that is called top subset for noise.
[10:07] Then I'm also running.
[10:08] So did I cover this?
[10:11] Yes.
[10:12] Then I'm running in here a random rotation around Y.
[10:16] So I can have a different instead of generating different models.
[10:19] I'm just upsetting around Y.
[10:21] Randomizing the rotation.
[10:22] So it feels different.
[10:24] So I didn't put too much effort in creating nice variations, but you can see in here if I
[10:30] enabled this node and generate nodes.
[10:33] So if I actually look at this and disable the yogis and the attributes, let's see if
[10:41] we can see this.
[10:43] So yeah.
[10:44] So as you can see, I'm also switching in here between, so when I have this, for example,
[10:49] this top part, I'm switching in here between zero and one.
[10:52] So I can have, I can either have it or not have it.
[10:56] If I don't have it, I still have the cork on the bottle.
[11:01] So this is my first variation with the fur for the dust.
[11:05] And just the bottle, then I have a second one, which has the detail and the top parts and
[11:10] so on.
[11:11] So that's just generating different variations.
[11:13] And that's pretty easy just with a wedge creating in this case a random integer, random
[11:19] integer and connecting those to the switches and also random floats for the random rotation
[11:26] and the offset of the noise.
[11:28] Then just outputting that to geometry and creating the USD variants, which I won't cover in
[11:33] this particular case because there are easier ways to do it.
[11:37] And I'm going to link below a video that I followed to do that.
[11:42] So that's basically the top part.
[11:44] Now let's move into Lops.
[11:48] So I created a camera also in here.
[11:51] And first of all, I'm referencing the geometry, which has different variations models.
[11:56] So I can show you in here.
[11:58] As you can see, I have the different variations, which in this case I just generated five
[12:03] since I didn't have many attributes to play with.
[12:06] Explore variants.
[12:07] So I can actually explore variants and set it to use bounds.
[12:11] And there we have, we should have a name in here.
[12:16] Okay.
[12:17] So these are the different variations.
[12:19] I'm going to just duplicate them.
[12:21] Then I'm flattening the stage so I can feed this to an instacer, which is really, really
[12:26] basic.
[12:27] It's just agreed and we are saving in here a bottle ID so I can randomize a bit on shading.
[12:34] So in this case, is each point number gets a different ID.
[12:38] Then I'm doing a backdrop just by using a grid and bending it up, nothing too complicated.
[12:44] Then we're going to check out the materials.
[12:46] So for that, I'm going to actually, before the materials, I just have to like one warmer
[12:52] in here on the left as main delight and one feel light, which is slightly cooler, so more
[12:58] bluish, just to feel in the, I'm not especially sun-liking, but I think it worked.
[13:04] Okay.
[13:05] So let's do a small render and I see in this, make sure I go to camera.
[13:16] Let's see if I can leave it.
[13:20] Okay.
[13:21] So let's check out the materials.
[13:23] So for the bottle, where am I doing in here?
[13:28] Can I go in?
[13:29] Okay.
[13:30] So I didn't cover the label, but I just used my texture projection tool to do a projection
[13:37] or in this case tool.
[13:39] Then I can later link with this file node.
[13:44] So in here, I'm just promoting the file attribute and giving it a default location for the
[13:51] copnet where I'm doing the projection.
[13:53] So that's the projection.
[13:55] Then I'm blending in with a color, so the bottle color, which is greenish and do some transmission
[14:02] and whatnot.
[14:04] Then from here, I'm blending two materials with a material like Smith.
[14:08] And the second material is just a dust.
[14:11] So I'm just increasing the roughness and doing some sheen.
[14:13] So I can actually show you.
[14:15] Sorry.
[14:16] I do this.
[14:19] So it's not actually very visible in this day.
[14:21] So I'm gonna do, I'm gonna connect this to the surface.
[14:25] And as you can see, I'm upsetting the position with that bottle ID that we created.
[14:31] So we get a different pattern on each bottle.
[14:33] So just loading a position, then doing a random float from that bottle ID and adding
[14:38] it to the position and feeding that to the Karma X tile track banner.
[14:42] So we get this texture, which is just a texture I found on my library, doing a conversion
[14:48] to RGB and feeding that to the material.
[14:52] So that's the dust.
[14:54] I don't want to visualize this, sorry.
[14:56] So as you can see, we have this sheen and mixing with the airs that we have in here,
[15:01] which just have a basic material, nothing to complicate it, just a gray material and
[15:05] it works okay.
[15:07] And then we also have the bottle mat I can show you how that looks.
[15:12] So nothing complicated as you can see, just some refraction and some roughness.
[15:18] And when I mix both and for the mix factor, I'm reading in that mask attribute we created
[15:24] from that combination of the normals.y and noise who offset a bit.
[15:32] And I'm loading that as a mask, but I'm also increasing the outlaw and contrasting a
[15:37] bit to the mask.
[15:38] So I can have more dust collecting even on the flat areas, on the non dust areas, as
[15:44] you can see.
[15:46] So in the end looks something like this, but then the trick in here is how do we get random
[15:52] variations of texture.
[15:56] And before I show you that, since I'm doing the insta serinear, I'm also playing with
[16:01] the seed to get different variations of bottles, as you can see.
[16:06] And yeah, that's basically how I'm doing the nothing really complicated, just playing
[16:11] with the random seed in here for the texture.
[16:15] So as you can see, in this case, I'm assigning the bottle, but I'm overriding in here with
[16:20] this assigned material.
[16:21] And this is not really complicated.
[16:24] Let's see.
[16:25] I'm assigning to the bottle geo, so these are the primitives.
[16:29] These are just an assigned material with a backsextpression.
[16:33] Then the material pads, I'm loading that to the material pads.
[16:36] Then in this backsextpression, I'm first of all splitting the primpad, which is this
[16:42] one in here, so I can actually show.
[16:47] Let's see.
[16:48] So let's print the name that I'm doing in here.
[16:54] And as you can see, we have the different, I'm just splitting by the forward slash, and
[16:59] we get the different rings.
[17:03] And we need to save that as an array.
[17:05] Then I'm doing a OP digits to extract the number in here of the model variant.
[17:11] So as you can see, we have 0, 1, 2, 3, 4.
[17:14] And that way I can drive a random using that seed and have a different variation for
[17:19] each file.
[17:21] So in this case, I have two projections.
[17:23] So I'm just building the pet in here.
[17:26] So to the texture projection, then I have texture projection 1 and 2.
[17:30] So this way I can feed that random between 0 and 1.
[17:35] So I can add 1 to be between 1 and 2 and do the rest of the pets.
[17:39] Then in here, on the C-bex bindings, I'm binding that file attribute, file parameter, that
[17:46] we have in here promoted.
[17:49] So as you can see, it's named file.
[17:52] And then I can link that to the file name that we created in here in the expression.
[17:57] And if I do a render, I can actually show you how that looks because I'm also creating
[18:02] a seed in here.
[18:05] So I shouldn't print this.
[18:08] So as you can see, now they both have the same.
[18:10] So I need to play with the seed and get the different variation.
[18:13] So now they still have both the same.
[18:16] So now is the other way around.
[18:18] So between 0 and 1, it will output a different variation.
[18:24] So that's how I'm building the, and you can do the same with random colors, random roughness
[18:29] for each ID, and so on.
[18:33] And you can also bring a premium var that you're good.
[18:36] So as you can see, previously I was using the USD-prim var function to bring in the, and
[18:42] then feeding the, the print path, which in this case was named and the first, the first,
[18:49] sorry, like this.
[18:51] So I was bringing the, the first string of this plate and that's actually what that
[18:58] I've created a bottle ID.
[19:00] So in this case, I didn't need it because I already had a different number for each bottle
[19:04] on the model variation.
[19:06] So yeah, then the camera, some depth of feels, some karma samples, rendering with XPU, and
[19:14] yeah, that's basically how I created this render.
[19:16] As always, you can grab the full scene on my Patreon alongside with exclusive tutorials,
[19:21] all the project files from my videos.
[19:23] And if you enjoyed this one and learned something new, please feel free to leave a comment.
[19:27] I don't ask for subscriptions or anything like that, but a comment always goes a long
[19:32] way.
[19:33] So thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:15] tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/frame_000.jpg
- [5:20] tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/frame_001.jpg
- [8:00] tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/frame_002.jpg
- [11:00] tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/frame_003.jpg
- [13:10] tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/frame_004.jpg
- [17:00] tutorials/frames/dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris/frame_005.jpg

---

## Structured Notes

### Core Technique
A full end-to-end procedural pipeline for a "dusty wine bottle" shot: modeling the bottle/cork/wire-cage/dust-cluster details in SOPs, driving model variations through a **TOPnet wedge**, referencing those variants into **Solaris/LOPs** with a point-instancer, and building randomized per-instance shading using primvar-driven seeds — all built inside SOPs first (never SubNetwork/Subnet create) specifically so it exports cleanly to USD for Solaris referencing.

### Summary
The bottle body starts as a revolved profile (deliberately computing but not using default revolve UVs, since a manual UV-flatten + Rectify pass gives cleaner top/bottom control), then gets poly-extruded and subdivided for thickness. The neck/foil "top part" uses alternating-vertex edge selection converted to curves, randomized per-curve length/pscale via VEX curve attributes (a Houdini 20 feature — curves can now carry attributes for use in Sweep), swept with a flat cross-section for a foil-drip look, then boolean-merged with a VDB-based smoothing pass (VDB From Polygons → VDB Smooth → VDB Reshape → remesh via the third-party **Exoside QuadRemesher** plugin, chosen because Houdini's built-in quad remesher gave worse topology here). Dust is generated as a separate "fur"-like layer: a noise-perturbed normal-based mask (capturing which surface areas would naturally collect dust, with extra randomization matching an uneven reference) drives an **Fur/Hair-gen** node's thickness and density, plus bend/freeze/clamp adjustments to fake clustered dust clumps like in the reference photo. Separate "detail" geometry (wire cage/cord around the bottle) is built from a 2-point curve, boolean-intersected against the bottle, resampled, distributed via Mountain-based jitter, and swept twice (tube-then-tube-on-curve) with twist and a Number-Wrangle-driven per-strand random offset for natural variation; the cork is modeled with a simple subdivide/polyfill/bevel/manual-seam-QuadRemesher pass. All the "pink" randomization-driver nodes (dust noise offset, random Y rotation, on/off switches for optional details) are wired to a **TOPnet wedge** that generates multiple output variants (5 shown) as USD variants, referenced into Solaris where a Point Instancer scatters bottles across a grid with a per-point "bottle ID" attribute for shading randomization. Shading blends a bottle-glass MaterialX layer (refraction/roughness/transmission + a projected label texture) with a dust MaterialX layer (roughness+sheen, tiled via Karma's tile/track banner texture node offset by a bottle-ID-derived random float) using the same normal-based dust mask (with extra contrast/offset) as the mix factor. Per-instance label texture variation is achieved via a **Material Assign primpath expression**: splitting the instance's primpath by "/", extracting the numeric model-variant index with `opdigits`, and using that as a random seed to pick between multiple pre-built texture-projection COPs nodes bound through the material's C-VEX file-parameter binding — giving each bottle instance a different label/text pattern without needing per-instance geometry variants.

### Key Steps
1. **Bottle body:** model in SOPs (not Subnet, for clean USD export) — Revolve the profile curve (computing default UVs but discarding them), Poly Extrude for thickness, Subdivide (x2), manual UV Flatten + Rectify on a manually-promoted boundary edge group for cleaner top/bottom UV control than the revolve default.
2. **Foil/neck detail:** Group Promote/expand the relevant vertex range, select every-other vertex, convert to line, build an "aperture vector" by normalizing `P`; randomly select some curves (via a `rand()` expression + seed), and use **VEX curve attributes** (new in Houdini 20 — curves can carry per-curve attributes usable directly by Sweep) to randomize per-curve length; build a `pscale` ramp from curve-U (curveu) with a VEX snippet targeting a mean pscale of ~0.6 via a max() expression; Sweep using a flat cross-section (second input) instead of the default round profile for a drip/foil look.
3. **Base + boolean cleanup:** VDB From Polygons on the swept drips, Blast bottom primitives by range (matching the revolve's division count) to keep only the top, Polyfill the resulting bottom cap, slight Transform + Remesh + Mountain, then Boolean to combine and extract the largest connected piece.
4. **Smoothing pass:** VDB From Polygons → SDF Union (combining shapes) → VDB Reshape → VDB Smooth → VDB Reshape again (extra dilation) → convert back to polygons → remesh with the **Exoside QuadRemesher** plugin (Houdini's stock quad remesher gave inferior topology on this shape).
5. **Dust layer:** Blast the outer surface, merge with the (conditionally visible) top part; build a mask from a **Noise VOP on normals** (zero-centered offset) to identify dust-collecting areas, adding extra randomization to match an uneven real-world reference; feed into a **Fur/Hair-gen** node, masking both thickness and density by that mask; randomize hair length, add bend, freeze, and clamp settings to emulate the clustered-dust look seen in reference photos; tag with a `name` attribute for later material combination.
6. **Wire cage/cord detail:** Object Merge the bottle, Subdivide; build a 2-point curve, Poly Extrude + Mirror so it intersects the bottle; Boolean (union mode) with resampling to conform to the bottle surface; slight Mountain-based jitter distribution; Sweep (round, N columns, with twist) to build tube strands, then a second Sweep-on-curve pass for "curves on curves"; randomize position via a **Noise VOP** with a unique offset per curve/frame (each curve gets a different seed) for varied "rope" strand looks; a separate circular-sort + Sweep pass builds a ring/band detail, using a Numbers Wrangle (`@ptnum`/iteration index, zero-centered offset) as a fast way to generate exactly two points for small connecting geometry, then Poly Extrude + Subdivide + Mountain + thickness for the final cord piece.
7. **Cork:** Subdivide, Polyfill, Blast the fill cap, slight scale + reverse, Poly Extrude, Bevel, QuadRemesher (with a few manually-picked UV seams), Subdivide + Mountain for surface variation.
8. **TOPnet-driven variation:** wire all randomization-driver nodes ("pink" nodes: dust noise offset, random Y-axis rotation instead of full remodeling, on/off switches for optional detail groups) into a **TOPnet wedge** that generates a random integer/float per variant (feeding switches and rotation/offset parameters) across N wedge iterations (5 shown), outputting each as a geometry variant for USD variant-set export (author notes an easier alternative video exists for the USD-variant export step, linked in the description rather than covered here).
9. **Solaris (LOPs) assembly:** reference the multi-variant geometry stage, use **Explore Variants** (Use Bounds mode) to inspect/select the different bottle variations, flatten the stage, feed into a **Point Instancer** built from a simple Grid + bend, saving a **bottle ID** (per-point number) attribute for later shading randomization; add a warm key light and a cooler, bluish fill light (not meant to mimic literal sunlight, but visually effective).
10. **Bottle-glass shading:** blend a bottle-color (greenish) with transmission/refraction into a base bottle material, using the label texture projection COP (built earlier, promoted as a `file` parameter with a default location) fed through a **File node** for the label.
11. **Dust shading + mix:** a second material (roughness + sheen tuned) is blended with the bottle-glass material via **Mix (MtlX Mix)**, using the same normal-based dust mask attribute (with added contrast/offset) as the mix factor so dust collects more visibly, even on nominally "clean" flat areas; the dust material's own texture is offset per-instance by feeding the point's `bottle ID` through a random-float expression added to position before a Karma **Tile/Track (UDIM-style) Banner** texture node, then converted to RGB.
12. **Per-instance label variation via primpath expression:** on the bottle's **Material Assign**, use a VEX Bindings Expression that splits the primitive's primpath by "/" into an array, extracts the model-variant number from the path segment via `opdigits()`, and uses that number as a random seed (`random(seed) * N + 1` style, to stay within valid projection-node indices) to pick between multiple pre-built **texture-projection nodes** (Texture Projection 1, 2, ...); the chosen file path is bound to the material's promoted `file` parameter via the C-VEX bindings panel, so each instance renders a different label pattern without separate per-instance geometry. Also demonstrated: reading the USD **primvar** function directly (e.ar. splitting a primpath string) as an alternative to a manually-authored bottle-ID attribute when one isn't already available.
13. **Render setup:** simple camera with depth of field, Karma XPU render settings, sample count tuning.

### Houdini Nodes / VEX / Settings
SOPs: Revolve, Poly Extrude, Subdivide, UV Flatten + Rectify, Group Promote/Expand, Convert Line, Attribute Wrangle (VEX: normalize P for aperture vector, curve-attribute randomization new to H20, pscale ramp via curveu + max() expression), Sweep (flat vs. round cross-section, twist), VDB From Polygons, Boolean (union, largest-piece extraction), VDB Reshape, VDB Smooth, Exoside QuadRemesher (third-party plugin), Mountain, Fur/Hair Generate (thickness/density masks, bend, freeze, clamp), Noise VOP (on normals, zero-centered offset; per-curve seeded position offset), Numbers Wrangle (iteration-index point generation), Bevel, Polyfill. TOPs: wedge (random integer/float generation driving switches, rotation, noise offset) for USD-variant model generation. LOPs/Solaris: Explore Variants (Use Bounds), Flatten Stage, Point Instancer (Grid-based scatter, per-point bottle-ID attribute), Material Assign (VEX Bindings Expression: primpath split by "/", `opdigits()` extraction, random-seeded projection-node selection), File node (label texture), MaterialX Mix (dust/glass blend via mask attribute), Karma Tile/Track Banner texture node (UDIM-style per-instance texture offset), Light (key + fill), Camera (depth of field), Karma XPU render settings.

### Difficulty
Advanced/Expert — combines VDB reconstruction, third-party quad remeshing, fur-based dust generation, TOPnet-driven USD variant authoring, and non-trivial primpath-parsing VEX for per-instance shading randomization in Solaris.

### Houdini Version
20 (explicitly references "new to 20" curve attributes for Sweep; UI matches Houdini 20 Solaris/Karma XPU workflow).

### Tags
#modeling #vex #vdb #tops #solaris #lops #karma #materials #shaders #procedural #usd #advanced

---

## Related Tutorials
Cross-link with any other cgside Solaris/LOPs, TOPs-variation, or VDB-reconstruction tutorials once extracted from this batch — shares the "procedural SOPs → TOPnet wedge → Solaris instancer" production pipeline pattern.
