---
title: All* the Procedural Modeling tricks in one video
source: YouTube
url: https://www.youtube.com/watch?v=Ba3Py4lodL8
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H19+, uses Exoside QuadRemesher)"
tags: [modelling, procedural, vex, uv, vellum, quadremesh, advanced]
extraction_status: complete
frames_dir: tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# All* the Procedural Modeling tricks in one video

**Source:** [YouTube](https://www.youtube.com/watch?v=Ba3Py4lodL8)
**Author:** cgside
**Duration:** 27m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] I have everyone and welcome back.
[0:02] So, in today's video, I wanted to break down how to create this kind of architectural elements
[0:07] in Odini.
[0:08] So, it's not the typical program to use for this kind of test, but I use Odini mostly,
[0:13] so I do it in Odini.
[0:15] And we also have some nice UVs that I will show you how to do it.
[0:18] And a quad mesh in the end.
[0:20] So it's not perfect, it's just an automatic quad remesh, but I will show you some tricks
[0:24] to get these even flow of polygons.
[0:28] So let's get to the top, so this is the network, a bit of a setup, but it's not too difficult.
[0:35] So everything starts with this circle.
[0:38] And in order to create this kind of pattern, so this pattern that we have here with these
[0:45] kind of shapes, we need to find a way to divide this circle into those sections.
[0:52] So the way I'm doing that is with a Varanoi fracture, so if I show you the edges, so we
[0:55] start from this and go to this.
[0:57] So basically, my idea was to create four points, one on each edge of the circle and control
[1:03] the distance that they are from the edges, and then we can create this pattern with just
[1:09] a Varanoi as you can see.
[1:11] And you could easily place an add node and manipulate the points in this case, I just did
[1:15] it with, so I did it with Vex, just placing the point at the boundaries.
[1:22] So in this case, I have control for the distance, in this case, I didn't control this one,
[1:27] but anyways.
[1:28] So basically, we start with the circle, since we want to create points, we connect the
[1:32] geometry to the second input.
[1:34] We get the bounding box max, bounding, so bounding box max of the circle, so x size, y
[1:39] size, and so on.
[1:40] In this case, it's not y, z, but anyways.
[1:43] We get the bounding box max, then the min, then the center.
[1:48] We create some controls to control the final distance, then we manipulate the, for example,
[1:53] position one.
[1:54] Let me see, position one is point one.
[1:57] So is this one in here?
[1:58] So we start to set the position, so the min x, that makes sense, we have to access x,
[2:03] x is in here, so the min x, 0.0 because this is at 0, 0 in y.
[2:10] And finally, the center dot that, so we just want the bounding box center, which is
[2:15] in here, we just get the z, in this case.
[2:17] So we get them in here.
[2:20] What else?
[2:21] Then we do, for the second point, then we do to the other points, and then we just
[2:24] manipulate the position with the multiplier in here.
[2:30] So in this case, I'm using the first two points, I'm doing them in manually in here, just
[2:36] with two add points, and for the other two, I'm just running a loop with two iterations
[2:40] and manipulating the z position in here.
[2:45] It's the same, I just do a loop, so I don't have to add two points manually, just like
[2:48] I did in here, as you can see.
[2:50] Then I'm placing them at center and multiplying by the size z, in this case.
[2:57] So I hope you got something out of these anyways.
[3:02] So with nothing, I know there's a lot of code in here, it's not a lot, but there's enough
[3:06] code to scare some people, but this is the most basic things you can do with Vex, and it
[3:10] doesn't require much knowledge in the end.
[3:13] So now we get the spatter that we can manipulate.
[3:17] So I'm just going, since this is separated, and I'm just going to fuse, group the center
[3:21] points and an easy way to do that in this case is just by bounding box.
[3:24] I was too lazy to think in a more elaborate manner.
[3:28] I will leave that for later for other things that I will show you.
[3:32] Convert to line, and then I want to sort the primitives.
[3:36] So I want the center primitive to be zero, so I'm doing approximately 2.00, since this
[3:40] is at the origin, always go to model at the origin, you'll get many, many benefits from
[3:45] it.
[3:46] So starting that, then I'm doing a transform in here, and this one is interesting, because
[3:50] I'm rotating in here 30 degrees to start to initialize the shape.
[3:54] So 30 degrees on X, and we get this result.
[3:56] But then later, I'm doing an exclusion, as you can see in here.
[4:00] And if I don't compensate that rotation with some scaling, I don't get this round shape
[4:06] at the end.
[4:07] So if I delete this, you can see we get this oval shape.
[4:12] And we want to compensate that rotation, since we're going to X-road this round, and we
[4:16] just take 1.0 and divide it by the cosine of the X rotation in this case.
[4:21] So I'm going to be honest with you, I got this met from an AI, because I didn't know
[4:27] how to do it otherwise, since I was really, really bad at met in school, so I had to ask
[4:33] for some help.
[4:36] So we get the, we do the compensation for the scale, then we do a transform on the primitive
[4:41] 0, since I saved it in this case is just a point.
[4:45] Anyways, I could have used primitive 0 since I sorted them.
[4:48] So we were here, I just move it down, then move it a bit to the front.
[4:54] So this edge group that we saved in here, the points.
[4:58] Then I'm doing a resample in this case, 10 segments on each curve.
[5:02] So right now they are separated curves, as you can see, each one individually.
[5:06] Then the thing is, if you try to mesh this, this won't work at all, because, well, it
[5:13] won't work without some work, because right here we have a rounded shape, then we are
[5:16] going to draw these linear ones, these straight ones, and it will just create a problematic
[5:23] mesh if you try to polygon fill or something similar to this, it will not work at all.
[5:28] So what we need to do now is to actually mesh this manually.
[5:33] So what I'm doing in here, I'm copying first, creating a new copy of the primitive 0,
[5:38] so we get two primitives in here, just that.
[5:41] Then I'm selecting in here the sides, because I want to mesh them separately, that was
[5:45] my easiest way to mesh this instead of trying on everything, so in here I'm separating
[5:50] the two parts.
[5:52] And this is really easy, we just take the position X, do an absolute to get the positive
[5:55] and negative, and we just say if it's bigger than point two, so we don't select the middle
[6:00] ones.
[6:01] And we do that on primitives, and on primitives the position is the center point of the curve,
[6:05] so we take advantage of that.
[6:07] Then we split those, so in this case I'm splitting and inverting the selection, and we
[6:12] get this, and we have a duplicated primitive in here, so I'm going to sort, in this case,
[6:16] by that.
[6:17] And the reason is so I can skin this more easily, because we need properly sorted primitives
[6:23] in order to create a skin.
[6:25] In this case, for some reason I'm doing it this way, it doesn't make much different,
[6:29] it just reverses the order, but anyways.
[6:31] So I'm skinning by columns and skipping doing groups of each two primitives.
[6:38] So in this case I'm skinning from here to this prime, and then the second prime that
[6:41] is there to there.
[6:43] So we do that skinning, then I'm doing a resample, and the reason I'm not doing, in this
[6:47] case, what relatros in here is because I want to control the density in the, so I want
[6:53] to make, to have more polygons in the middle.
[6:56] So that's why I'm doing columns, then I do a resample.
[6:59] Now I can do a proper skin and get a nice subdivided model in this case.
[7:06] Reverse doing a normal, because this skin, I don't know what's going on in here, but
[7:11] anyways, I always have this problem with the skin node, but anyways we just do reverse
[7:15] and normals, and that's fine.
[7:17] Then on this side is something similar, I'm just selecting in here again with the same
[7:21] expression, these inner primitives and splitting them, and doing a reverse, then on this
[7:27] side, I'm doing a resample, let me see, five segments, fusing polypads to unite the
[7:33] curve, so we have zero and one, then reverse the primitive zero, because they were, this
[7:37] one was different from this one, the prim, the cortex order, then I do a resample, and
[7:43] we have this one in here, we merge them, and this resample, let me see, we have 22 points
[7:50] and 22 points in here, so this resample, this one is just to reorganize the points, yeah,
[7:56] exactly, and this one is to match the points count of these ones, so now they have the
[8:01] same point count from this to this one in here, and now we sort again the primitives, in
[8:06] this case by X and with skin, and we get, since we have the same amount of points, we will
[8:11] have no problems, and as you can see now, having enough subdivisions in here, we can
[8:16] probably mesh this part, this was the problematic part anyways, then we just merge, and we get
[8:22] our initial shape, then just deleting the group, doing a basic UV flatten, to get some
[8:27] UVs going, selecting the unshared points, fusing, I'm fusing the point in here, yeah, because
[8:37] this was unconnected, yes, then I'm selecting the unshared ledges, and grouping also the entire
[8:43] mesh, calling it top, and doing again the polypads route, and we get the round shape at
[8:48] the end, then in order to create some, I want to fill this mesh, so I'm just filling on
[8:52] a separated branch, and doing a UV flatten on the patch group, so on this polypheal, I'm
[8:58] saving a patch group, and doing that, that UV flatten just for that group, and from here
[9:03] I want to transfer a group, in this case the unshared, this unshared point group we created
[9:08] in here, so I can later modify it, promoting it to edges, and doing a basic UV flattening
[9:16] here, this UV flattening is just to redistribute the shelves, so I'm preserving the seams only,
[9:23] as you can see, I'm not actually unwrapping it again, then we do an Etch Cus, to separate
[9:29] the mesh on the unshared edges, so in here, in here we have it working, so on the unshared
[9:39] edges, I'm just disconnecting the mesh, because I want to create some seams on the
[9:43] valum seam, so far that I need to separate the mesh, and then weld on stitch points,
[9:48] or something like that, then I do quite a ivory mesh, not so a pointy tree, in this case
[9:53] we get something like this, and you can increase to have even more pronounced wrinkles,
[10:01] but in this case this one worked pretty well, so then I'm doing again some UVs, because
[10:06] I don't want these all flipped and whatnot, so as you can see I want these properly oriented,
[10:13] so I'm using these orient UVs in here, it takes a while because the mesh is not
[10:18] actually, it takes two seconds because the mesh is quite dense, so in order to orient
[10:23] the UVs, this works on quad meshes, so to make it work on this triangulated mesh, I
[10:29] have to weld a clip in the middle, so we can properly find a neighbor to orient it, because
[10:34] I shared this before, this is using a matrix that is based on a point and a neighbor,
[10:44] so if it finds a neighbor to this direction, it will just orient the UVs this direction,
[10:49] and if we do a basic cut in the middle, in this case it will do the trick, and we also
[10:54] have a new parameter in here, which is the tolerance for what the islands, so if I set this
[11:01] to what I had previously, which is 5, it will not rotate properly this one, but you can
[11:05] play with the values, and it will assume these are quad islands and orient it properly,
[11:11] and as you can see we now have the UVs properly oriented, even this bottom one, as you can
[11:16] see, then we can just, UV transfer to the original mesh, because I don't want this cut,
[11:21] and we have nice UVs, they are just on top of each other because they were rotated like
[11:25] that, so what we can do, we don't, we can do a basic UV flatten,
[11:31] just to get rid of some inconsistencies, so we can see here is a bit distorted, and if
[11:39] we do a UV flatten with these settings and manually out, it will re-reproject the UVs,
[11:45] as you can see, then we do a basic UV flatten, so access alignment to non, so it doesn't
[11:50] rotate, no rotations, and apply some island pending, as you can see, so we don't go through
[11:55] to the edge.
[11:57] Okay, then I'm going to subdivide this, because I want even more geometry, and open
[12:02] subdivlop, and in this case I'm increasing the decrease, I'm doing some cruising, we can
[12:09] ignore this part, and then it comes the valumatri, send a mask, so if we look in here, if we
[12:19] apply, I'm doing a basic valum, valum pressure, so the configurable one thing, and if we apply
[12:24] the same pressure to all the mesh, it will just blow up the bottom, blow up the sides,
[12:30] and in here it can also blow up a bit more, but I want to control how much sheet inflating
[12:36] this side, and how much sheet inflates on the bottom, and in here on the cushions, so I
[12:42] want to have some control over it, so I actually didn't know about this attribute called
[12:47] pressure scale, that you can input into valum, it was shared with me by a friend on Discord,
[12:54] his name is Philipp Weasling, he also does tutorials, I will try to remember to leave a link
[12:59] to his channel on the description, it has pretty cool stuff, but anyways, this pressure scale
[13:05] can control the inflation of the valum seams, otherwise it's way too complicated to do
[13:10] it, so Philipp told me about this attribute that we're going to use in our valum seam,
[13:15] so I'm setting, I don't need to set these on the inside the solver, because I'm just
[13:21] doing these for a still and not animating the pressure going up, and what not, this
[13:25] is just a modeling exercise, and we're using valum to model, not to create animations
[13:30] in this case, or mograph something like that, so I'm just creating a mask in here, so I
[13:35] have, if you remember, we did a group, or the top part, here it is, and I'm just saying
[13:42] in-prem group, top, I-prem num, and we create a pressure mask, so you can see in here,
[13:47] pressure mask, so I'm selecting the primitive, the points, that are part of that primitive
[13:51] group, and I create the mask, and I also create an attribute called the pressure scale, this
[13:56] one you really need to name it like that, and I'm just learning between negative inflation
[14:01] for the sides, so for the zero values, for the sides and the bottom, and for the values
[14:07] that match one, in this case I'm setting a scale of 0.15, and just blending it with the
[14:12] mask, so this one, minus 0.4, a negative inflation, because for some reason I have to set a negative
[14:18] inflation, otherwise it would go in, I'm not sure if you know why that let me know in
[14:23] the comments, then 0.15 on these questions that I want to inflate out, doing a basically
[14:30] basic unshared points in here, because I want to do some welding in valum, in here I'm
[14:37] creating a mask, let me see, yeah a mask for the base on the unshared points, and I want
[14:42] to increase it, so I do an attribute adjust float, multiply it by a big value, increase it
[14:49] with an attribute blur, and I can increase it even more, but then the values with well
[14:53] blow up, so I'm clamping those values to 0 and 1 with this clamp, then I'm doing an
[14:59] attribute noise to multiply some noise over and contrasting a bit the mask, so we can
[15:05] have this sort of noisy mask, otherwise the wrinkles will be too uniform, so we have to
[15:11] noise upload attributes, in this case is underscore mask, and I have another one, the pressure mask,
[15:17] which is just a mask for this part that we're going to also use, so by the way this mask,
[15:23] I'm also blurring it, but just likely just one iteration I think, yes, then we're doing
[15:28] a valum stitch on the unshared points, and there's nothing else to eat in here, I'm just
[15:34] stitching the points, then I do a basic valum, configure valum, so valum clouds set the stiffness
[15:40] to 10,000 on the stretch constraints, and to a really low value on the bands, so it creates
[15:45] those nice wrinkles, and this one I'm saving as default the cloud to stretch, because I want
[15:51] to manipulate them inside the solver, and on the valum pressure I'm renaming it to pressure,
[15:56] and I set 100 for the 6th to the power of 100, I think that's the way you're supposed to say it,
[16:02] so the stretch constraints, the most important part is this pressure that I'm saving in here,
[16:08] then it comes the solver, so let me get rid of these masks, and let's see how this goes,
[16:14] so I'm just updating in here, let me see, I'm just updating in here,
[16:22] on the not on the bands, on the stretch constraints, I want to update the wrestling scale,
[16:27] so it creates, so you can see in here it's creating those wrinkles, and then on the pressure,
[16:32] I want to control the pressure, so more pressure here, less pressure in here,
[16:35] otherwise this would be really blow up, and we get these sort of results, I really like these
[16:41] wrinkles, and I will show you what trick to actually have these kind of wrinkles, so let's go inside
[16:47] the solver and see what I'm doing in here, so first of all I'm selecting the stretch constraints,
[16:55] so the ones from the clouds, to create these extra fabric, so I'm selecting wrestling scale,
[17:01] and in here I'm just lurping between a big value and a small value, so in this case,
[17:09] I want this part of, so let me show you actually the mask, so this one is the underscore mask,
[17:17] so this one in here, let's forget about these two lines, so we have this underscore mask in here
[17:22] that we are seeing on the viewport, and I want those right values, those bigger values to have
[17:27] last one scale, so I want to push them in, and the other ones can be pushed out for the pressure
[17:32] constraints also, and in order to have a room for these wrinkles in here to grow, or to create them,
[17:44] so I'm just pushing in here the edges in with these small values, or smaller than one,
[17:51] which is the default value that will create no extra fabric, so I'm inverting the fact,
[17:55] at first I thought, okay I'm going to increase the wrestling scale, the rest scale on these edges,
[18:00] and that will create some wrinkles, something like these along the edges and whatnot, but then again,
[18:06] I inverted results, so I placed a nire value on the blue part in here, the zero values,
[18:12] and I decrease the edges, and these will create these nice and soft wrinkles that serves better
[18:18] the purpose of this model, so but then again in order to update in here I'm just selecting the
[18:23] pressure mask, so let me see the pressure mask, and updating the rest length, so I want
[18:31] the default rest length on these on these parts, so I'm both on these parts, and I want to increase
[18:37] a bit the rest length on the on the top part, so as you can see I'm selecting the pressure
[18:44] constraints, but and this is not rest scale, this is wrestling, so we need to increase that,
[18:50] in order to work with the pressure, this is also working with the pressure attribute that we have,
[18:55] so the pressure scale as you can see, and but then again in here on the on the clouds, we also need to
[19:03] to update the rest scale of the based on the mask on this pressure mask that we have in here,
[19:09] so on this one, so in this case I'm just loading that mask from the first input, so you can see
[19:16] first contextual geometry, which is the volume geometry, not the constraints, and then I'm just
[19:22] lurping between 1.08 and 1.1 using the second mask, and then at the end I do the final alert,
[19:31] maybe it's not the best way to do it, but basically I'm taking that lurb for the, so let me see
[19:38] again in here, so as I told you before this will shrink these red parts and increase the
[19:46] the rest scale or the fabric for these inner parts, because I also want to create some wrinkles on
[19:53] these parts and whatnot, so this is how you can control the rest scale and the pressure constraints,
[19:59] a bit tricky, but yeah, so then I just cash the frame 24, fuse the points, because
[20:08] in this case we can apply welds, but this was using each constraints, so I'm just fusing and
[20:15] apply a valentose process, which is just a subdivision and a spatial blur, and I'm doing, I know this
[20:21] is too eye-poly right now, but even that it just creates some problems on the mesh, as you can see,
[20:28] it still has some shading issues, but we can work with that, so this is not our final geometry,
[20:33] I'm gonna do that in a bit, so in order to create a quad geometry from this, I'm just splitting
[20:39] UV seams, because we still have UVs, as you can see, and promoting that to a point of tribute,
[20:44] creating a connectivity, measuring the area by that class attribute, so in here we have a class,
[20:51] and we also have, so I'm normalizing the area in here, so let me actually show you that,
[20:56] I'm calling it area targets, and we have, let me do this, and we have this kind of distribution
[21:03] of areas, as you can see, and then I'm swapping this to the UVs to position, so I can actually
[21:10] do an exosite quadremeshter on the UVs, and if you want them to do these on the 3D geometry,
[21:15] it will be a complete mess, I tried that man with some setting fan, didn't work at all, but as you
[21:20] can see, when we finally deform it, we have this kind of organized, organized edgeflow, but in order
[21:28] to have the same scale since in here, we have different scales for the parts, and I want a uniform
[21:35] distribution of quads, so we get, I just took the original area and fit it between a min and a max
[21:43] value, and then just learn between the red color and the this turquoise color based on that mask,
[21:53] so we get in the exosite quadremesh, we can use the vertex colors to define the polygon count,
[21:59] or the density on the final geometry, then I'm subdividing because I want to take advantage of
[22:08] the eyeball mesh or the triangle-like mesh to get all the details, so you can even subdivid it more,
[22:15] and this deform is just as exosite and read the position and the UVs from the second inputs,
[22:20] and on the first input where we do the exosite is just the same mesh that we have in here on the
[22:28] third input of the same point count, but this one is the UV mesh that is similar to the quad mesh,
[22:36] so we can measure the xyz to the UV mesh and then deform, grab the position from the third input,
[22:44] and we also grab the UVs, so we still get this with UVs, so that's fine. Then the only thing left
[22:50] to do is to do the piping, I think that's the name, so it's called the piping, which is just this
[22:55] part in here that goes along the edges of the mesh, and we just grab from the attribute boundary,
[23:00] so from the UVs, and we convert the line, we bless one of the frames, just based,
[23:06] so I just move it to the center, basically, instead of moving position, I save it as a rest attribute,
[23:11] and then just make sure that I want to remove this part in here, that is part of the UVs also,
[23:18] so I just move it to the center and get the from that position, I just compare it,
[23:28] compare the position dot y or the rest dot y and the rest dot z, so we fit smaller than zero,
[23:34] so it's going through that position, the negative that position, and also mostly in the center,
[23:41] so it's easy, or just blast it with a blast mode, then that's fine, so I'm just too picky about it.
[23:46] Then the ability attributes, resample, let's do another resample to get even more,
[23:52] so we do a double resample to get rid of these jacked edges, so first of all a nivre sample,
[23:57] to get them overall roundness and subdivision curves, and do then a nivre sample, then I want to,
[24:06] so let me see in here, if we do, as you know, the sweep doesn't unite corners like this,
[24:13] or let me show you, so it's not very visible, but basically, if I don't do, let me see,
[24:21] these ones in here, as you can see, we have this open mesh, and I want to make sure that at least
[24:28] the circle in here, because right now we have single primitives, so we don't have a primitive for
[24:32] this circle, a unique primitive, so I want to make sure that at least this circle on the outside
[24:38] is united, so for that I'm creating an oriental curve after the resample to get in this case the
[24:43] tangents, so we just vector along the curves, and then I'm running a wrangle to see if the
[24:55] curve is straight or not, so basically I'm taking the, creating a variable called points that is
[25:02] just a single point of the primitives, so for example this primitive 5A has all these points,
[25:09] then I'm grabbing the tangents of the first point of the primitive, so let's say is this one,
[25:16] and call it that a reference vector, then I'm starting with I'm doing a loop, or each point on
[25:23] on each primitive, and I'm reading the tangent for each point, and doing a basic dot product
[25:30] between the reference vector, so let's say this one, and the current one, so to,
[25:37] to check if they align, if they don't align, it's basically not very straight, so basically I just
[25:44] want to, in the end, to have these sort of masks, so let me go in here, and see, in here I want to
[25:51] grab these straight lines, because I will fuse and polypads these outer circles, this one is already
[25:58] connected, so we don't need to worry about it, so I just saved that attribute, that straight,
[26:03] then I do a fuse, and I do a fuse based on that attribute, and then selling this match attribute,
[26:10] and then do a polypads, and that will unite the circle, and keep these ones isolated, then if I do
[26:16] a sweep, we get these closed, and I'm already happy about it, then I create the UVs in here, but they are
[26:25] super big, as you can see, I just do a UV flatten, is it cute, with Preservesims, then also
[26:31] Island boundaries, to get them organized like this, on the 0 to 1 range, and then just creating an
[26:36] attribute called Piping, and I merge it over, and from here, it's just, since we have UVs on top of
[26:43] each other, we do a basic UV layout, so same settings as before, soft and normal,
[26:48] really dulled groups, really the unnecessary attributes, do a match size to move it to the grid,
[26:55] and just save it out. So yeah guys, a lot of work, but in the end hopefully we got a decent result,
[27:02] I hope you have learned something from this, and as always you can grab this full file on my Patreon,
[27:07] I'm gonna share it on the Patreon post, and you can also grab exclusive tutorials on there,
[27:13] hours and hours of exclusive tutorials, all the project files from my videos,
[27:17] and some custom tools also, and I'm working on a new tool to share in the next month, so stay
[27:21] tuned for that. Thank you for watching, and let me know your opinions in the comments if you
[27:25] enjoy this kind of video, I would love to hear from you. Thank you, see you next time!



---

## Captured Frames

- [1:11] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_000.jpg
- [4:00] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_001.jpg
- [7:06] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_002.jpg
- [10:49] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_003.jpg
- [16:41] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_004.jpg
- [21:59] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_005.jpg
- [26:16] tutorials/frames/all-the-procedural-modeling-tricks-in-one-video/frame_006.jpg

---

## Structured Notes

### Core Technique
End-to-end procedural build of an architectural cushioned-panel element: VEX-driven circle subdivision → manual quad skinning → Vellum-simulated wrinkle detail (using the `pressure_scale`/`rest_scale` attribute trick) → Exoside QuadRemesher retopology with vertex-color density control → procedural "piping" trim detail.

### Summary
A dense, single-take breakdown of building a stylized architectural/upholstery-like panel shape entirely proce41rally. Starts from a circle divided into quadrants via Voronoi Fracture (points placed with a short VEX snippet using bounding-box min/max/center), builds a rotated, scale-compensated base profile, manually meshes the resulting curves by splitting/skinning them in controlled column groups (because a naive PolyFill fails on the mixed round/straight geometry), lays out and orients UVs (including a matrix-based neighbor-orientation trick requiring a quad mesh), simulates cloth-like wrinkles with Vellum using an attribute called `pressure_scale` (credited to a friend, Philipp Weasling) to locally control inflation instead of a uniform pressure value, retopologizes the wrinkled high-poly result with Exoside QuadRemesher using vertex-color-encoded density targets, and finally adds a procedural "piping" trim by detecting straight vs. curved mesh boundaries via tangent dot-products in a wrangle.

### Key Steps
1. **Base pattern:** start from a circle; use a **VEX wrangle** to place 4 points at the circle's bounding-box min/max/center (X and Z) as Voronoi Fracture seeds, giving control over how far each point sits from the edge; run **Voronoi Fracture** to divide the circle into the quadrant pattern.
2. Group/fuse the resulting center points by bounding box, **Convert to Line**, sort primitives so the center primitive is index 0 (helps keep everything modeled at the origin).
3. **Transform** with a 30° X rotation to initialize the shape, then apply an **exclusion** — compensate the resulting oval distortion by scaling by `1 / cos(rotation)` (the presenter notes getting this specific math trick from an AI assistant).
4. **Resample** each curve (10 segments), then because a straight-edge + rounded-edge mix breaks naive **PolyFill**, mesh manually: duplicate the primitive, separate "side" vs "middle" curves using `abs(position.x) > threshold` primitive selection, split/invert, sort, and **Skin** in column pairs (not straight across) to control polygon density — denser in the middle.
5. Reverse normals as needed after Skin (a recurring quirk with the Skin node per the presenter), repeat the split/resample/skin process for the other side, then **resample to match point counts** between pieces before final skinning so both sides merge without seams.
6. Basic **UV Flatten**, fuse unshared points/edges, group the mesh as "top", and use **Orient UVs** to fix island rotation — this node relies on matrix orientation from a neighboring quad, so on a triangulated mesh you must first weld/cut a seam (e.g. down the middle) to expose a valid neighbor; also tune the **island tolerance** parameter for correct quad-island detection.
7. Use **UV Transfer** to move the corrected orientation back onto the original (uncut) mesh, then a final **UV Flatten** (no rotation, island padding) to clean up remaining distortion.
8. **Subdivide** for extra geometry, then set up **Vellum**: build a `pressure_mask` (from the earlier "top" primitive group) and a custom attribute named **exactly** `pressure_scale`, blending between a negative value (sides/bottom, "negative inflation" — needed even though it seems counterintuitive) and a small positive value (~0.15) on the top/cushion faces via the mask.
9. Build a second mask on unshared/weld points, boost it with **Attribute Adjust Float × Attribute Blur**, clamp 0-1, then run **Attribute Noise** over it to break up uniformity — a purely uniform mask produces unrealistically even wrinkles.
10. **Vellum Cloth**: set Stretch Constraint stiffness very high (~10,000) and Bend stiffness very low to encourage wrinkling; save the cloth's rest-scale-manipulation channel as default so it can be driven per-point inside the solver; rename the Vellum Pressure exponent parameter to `pressure` for reference inside the solver.
11. Inside the **Vellum Solver**: on the cloth stretch constraints, lerp `rest_scale` between a small and large value using the noisy mask — pushing edges IN (rest scale < 1, the default with no extra fabric) creates room for wrinkles to form (the presenter notes their first instinct — increasing rest scale — gave the opposite, wrong result). On the pressure constraints, similarly lerp/update `rest_length` using the `pressure_mask` to control local fabric slack tied to the pressure attribute.
12. **Cache the sim** (frame 24 used as the final still), fuse points, apply **VDB-based smoothing** ("Valentose process" — subdivision + spatial blur) to clean up the high-poly mesh, accepting some remaining shading artifacts at this stage since it isn't final geometry yet.
13. **Retopology:** split UV seams, promote to point attribute, build connectivity, measure per-shell area (a "class" attribute), normalize area into an "area target" value, and **bake that as vertex color** — feed the UV-space mesh (not the 3D mesh, which the presenter tried and found produces a complete mess) into **Exoside QuadRemesher**, using the vertex colors to drive local polygon density/count.
14. **Deform back:** use a Point Deform-style setup with the same point count between the flat UV-quadremeshed mesh and the original 3D+UV mesh, subdividing further afterward to recover detail from the original triangle/eyeball-dense mesh.
15. **Piping/trim detail:** grab the mesh boundary attribute from UVs, convert to line, save a rest position, then in a **wrangle** compute per-primitive tangents via **Orient Along Curve**, take a reference tangent from each primitive's first point, and dot-product every other point's tangent against it to classify the curve as "straight" vs "not straight" (curved) — this mask is used to fuse/PolyPatch only the genuinely circular sections (so they weld into one primitive) while leaving straight runs isolated, letting a subsequent **Sweep** close the circular sections properly without merging incompatible straight segments.
16. Final UV pass on the piping geometry (flatten, preserve seams + island boundaries), merge with the main "Piping" attribute, then do a final cleanup UV layout, delete unnecessary groups/attributes, and **Match Size** to normalize scale before export.

### Houdini Nodes / VEX / Settings
VEX wrangle (bounding-box min/max/center point placement) → **Voronoi Fracture** → Transform (rotation + `1/cos(angle)` scale compensation) → manual curve split/Skin-by-column (density control) → **Orient UVs** (matrix/neighbor-based, requires quad topology + seam cut) + UV Transfer + UV Flatten → **Vellum Cloth** (`pressure_scale` custom attribute, high Stretch stiffness/low Bend stiffness) → Vellum Solver internals (`rest_scale` lerp on stretch constraints, `rest_length` lerp on pressure constraints, driven by noisy masks via Attribute Adjust Float / Attribute Blur / Attribute Noise / Clamp) → VDB smoothing ("Valentose" subdivision+blur) → connectivity + area measurement → vertex-color area target → **Exoside QuadRemesher** (on flattened UV mesh) → point-deform back to 3D → tangent dot-product wrangle for straight/curved classification → Fuse/PolyPatch/Sweep for piping trim.

### Difficulty
Advanced — combines VEX scripting, manual curve-to-mesh construction, non-trivial UV orientation math, custom Vellum attribute-driven wrinkling, and a third-party quadremesh plugin; not a beginner workflow despite individual steps being explained clearly.

### Houdini Version
Not stated explicitly; requires the third-party **Exoside QuadRemesher** plugin (any modern Houdini H19+ compatible with it).

### Tags
#modelling #procedural #vex #uv #vellum #quadremesh #advanced

---

## Related Tutorials
Cross-link with [5 Tips and Tricks for Modeling in Houdini](5-tips-and-tricks-for-modeling-in-houdini.md) — shares #modelling #procedural #vex; that tutorial's off-center-mirror and attribute-driven bevel tricks complement this one's VEX-driven point placement and area-based UV/quadremesh workflow.
