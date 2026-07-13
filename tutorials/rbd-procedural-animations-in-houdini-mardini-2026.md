---
title: RBD Procedural Animations in Houdini | Mardini 2026
source: YouTube
url: https://www.youtube.com/watch?v=ITq2EBJ5nIw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/rbd-procedural-animations-in-houdini-mardini-2026/
frame_count: 0
frame_status: pending-selection
---

# RBD Procedural Animations in Houdini | Mardini 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=ITq2EBJ5nIw)
**Author:** cgside
**Duration:** 18m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py rbd-procedural-animations-in-houdini-mardini-2026 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back!
[0:02] Though in today's video I'm gonna break down yet another Mardini project I did.
[0:06] So this one was for the day collab and I ended up with this result.
[0:11] So it was my first time doing an animation for Mardini.
[0:14] I usually only do stills because it's faster, but this one I wanted to do an animation
[0:19] because it made more sense.
[0:21] So let's break it down.
[0:23] So I started this by modeling the barrel.
[0:28] Because there's nothing exciting about modeling the barrel.
[0:31] I just want to show you is just a bunch of exclusions starting from seal in there.
[0:35] So nothing to exciting.
[0:36] But in this part I'm gonna share how I did something specific.
[0:40] Which was to give thickness.
[0:41] I wanted to have a thicker wall, to have more refraction in render so the glass would
[0:46] be more noticeable.
[0:48] And in order, things I have this kind of details in here.
[0:53] If I do a normal poly-extraubed, so let me show you.
[0:57] If I go in here and just set to pre-compute or primitive, we start to have these sorts
[1:02] of intersections as you can see.
[1:03] But if I do in here with my custom normals, you see I get a nice result and we'll have
[1:09] no problem in shading.
[1:11] And the way I'm doing that is first of all I'm computing a meskin here.
[1:15] So let me show you with the distance along geometry.
[1:17] Which starts from this bottom point and goes up.
[1:20] So normalized just this.
[1:22] When I do a convexel, so I can extract some normals, some equalized normals from second
[1:29] input.
[1:30] Then I do some normals in here.
[1:32] And the problem with the extrusion is just the normals will be these arch.
[1:36] So I'm attributing the normals.
[1:38] So I'm first computing point normals, then blurring them out.
[1:42] And finally I blend the normals from the second input.
[1:45] Which is just a convexel and the first inputs.
[1:48] So I just take the mesk and do some channel ramps.
[1:51] When I do next wise it is to the second input so I can sample the normals from there.
[1:56] Then I just learn between one normal and the other normals by using one of the ramps
[2:01] based on the mesk along Y.
[2:03] So as you can see at that specific point I just blend it with another with these normals.
[2:08] And in the end we get this result which is more acceptable.
[2:13] So that was it about modeling.
[2:16] That's the only interesting part about modeling of this.
[2:19] And we need to prepare this for the RBD simulation.
[2:23] So I'm going to subdivide it since I want a bit more definition of the geometry.
[2:29] In here I'm just saving the name attribute as another name because RBD will mix it up.
[2:34] Not RBD but this one no fracture.
[2:36] It will change the name.
[2:39] So I'm also saving a rest attribute for shading.
[2:41] So I can always refer back to this position.
[2:43] I'm calling it press-shade.
[2:45] Then I do an RBD material fracture.
[2:48] And this is for the final breaking pattern.
[2:52] So this is all I'm prefracturing the geometry.
[2:54] There are other ways like doing dynamic fracturing in RBD but I didn't have the time for that
[2:59] so I just prefractured.
[3:00] And since this geometry can cause issues in shading since it's prefractured for the first
[3:04] frames I'm going to use this RBD connected faces and what this does is just this will
[3:13] save out some attributes that we can later.
[3:17] So where is that RBD connected faces and then we should have in here.
[3:23] Let me see.
[3:26] So as you can see later I'm using these disconnected faces which is the second node just to remove
[3:30] the interior faces between the meshes.
[3:34] So we just have a workflow in RBD to not having shading issues with the interior faces
[3:38] which shabon on each connected part.
[3:41] So yeah, in the end it didn't work out that well but I used it anyways.
[3:45] So we do this.
[3:46] Then we need to create a collision mesh since we can't really use concave.
[3:50] It will be too expensive and prone to error.
[3:53] So I'm first going to animate the faces in here just to have an ID.
[3:58] Then I'm going to do a Varanoi fracture so I can have a decent collision mesh because
[4:02] I'm gonna have balls inside here or spheres and if we don't have a decent collision shape
[4:07] we will have a lot of problems.
[4:09] And then I'm just copying here some attributes from this name and attributes from this RBD
[4:15] connected faces.
[4:16] In here it's important to connect to Evgen the name.
[4:19] So let me show you.
[4:20] As you can see the Varanoi fracture will replace the name and we need to copy it back so we
[4:25] can actually only break at these points in here at the edges of this name attribute.
[4:30] Then I'm packing with an RBD pack and setting an initial position.
[4:34] In this case it's just moving it by the bounding box and a bit to the side.
[4:39] And then I RBD unpack and have the packed geometry and give it and promoting the point of
[4:46] the name attribute since we are going to do RBD simulation.
[4:49] And I also have the constraints in here from the RBD material fracture which I'm just
[4:54] deleting just keeping the name and the constraint and rest length and then promoting the name
[4:59] attribute and setting a strength for the local constraint in here.
[5:04] I've seen the RBD material fracture.
[5:06] I just set it to glue.
[5:08] So I'm just setting manually the strength and this will make a bit more sense once we
[5:12] go to the RBD material fracture.
[5:14] And in here I just have some collision GU that I'm packing and attribute promoting to
[5:19] a name.
[5:20] And let's see how we did that collision GU.
[5:22] So I start with the grid which is like this.
[5:25] Then I promote some I create a point group and promote it to edges.
[5:29] So we have this and then in a loop I'm just doing one X-Rusion to the front and one
[5:34] X-Rusion down.
[5:36] So using that edge group and making sure we don't preserve groups so we doesn't replace
[5:42] it.
[5:43] So as you can see this will be a problem if we preserve the groups.
[5:46] So then I'm doing a poly-X-Route to the front to create this grounding here, then splitting
[5:55] in here, doing a unique point since I want to create some collision GU from this.
[6:01] And this will be my stairs and grounds and then I just extrude volume to have some thickness.
[6:08] And then I merge over from the stairs.
[6:10] I do a pound split by normal along the x-axis both.
[6:15] Then do a manual clip in here and do a poly-X-Route for the walls.
[6:19] And these are the walls.
[6:21] So this is my collision GU and then let's jump into the RBD simulation.
[6:27] So in here let me see.
[6:31] I'm loading the barrel in here, the glass barrel as first context geometry and active
[6:39] object, making sure I just set a small bounce and I set an initial velocity along the x-axis.
[6:46] And a bigger one along the x-axis just to bias towards the bit the x and the negative
[6:51] x and of course move it forward.
[6:55] Then I set a constraint network in here and connect a Gluo relationship and setting the
[7:02] strength just one.
[7:05] And the way I'm updating the constraint so it breaks when I in the frame I want, I'm
[7:11] in a relationship I'm attaching the internal constraints to the object itself.
[7:14] Otherwise it would create the constraint here in the relationships which I can't really
[7:20] edit with a wrangle.
[7:22] So that's why I'm doing that.
[7:24] Previously I was using a sub-solver and in here we have the relationship geometry which
[7:30] I can apply to here.
[7:32] So that's why I'm attaching to the object.
[7:34] Then I merge in, let me see, the collision GU and let's look at the bullet data so let's
[7:41] do the opposite play.
[7:42] And as you can see I did that unique point so I can have a box for each stair previously
[7:49] I was doing a boronoi fracture and the result was not that great so that's why I did that.
[7:54] So this way we just have a box representing as a convex hole.
[7:58] Then I load in here the other geometry.
[8:01] So this one, oh and make sure this one is static of course and this case is starts context
[8:06] geometry.
[8:08] And oh of course I'm loading in here.
[8:11] The spheres that we're gonna have a look in in a bit so we find this able to display.
[8:16] We have the spheres that I simulated with another RBD simulation of course so I'm just
[8:22] loading as active object.
[8:23] Then it is we will let the seam run so let's display the geometry, RBD, rigid body solver,
[8:29] some gravity and here on frame 27 I'm just after frame 27, 26 I'm just lowering the
[8:37] strength of the constraints of the parallel.
[8:39] This way it will go and after that frame it will start to lower the strength and break
[8:44] everything as you can see.
[8:46] So that's basically it's really simple but it was effective.
[8:49] In this case it will look a bit different from my final result because I updated some
[8:53] settings in here mainly setting a different collider for the stairs but then it's you
[8:59] can play with the velocity, the initial velocity in here and maybe add some noise on the start
[9:04] of the simulation to have a different result.
[9:06] So you can act a bit more.
[9:09] So let me just quickly show you how I did those spheres inside.
[9:12] Basically I'm splitting the barrel in here so by delete and this by showing pink.
[9:21] Then I'm blasting the interior part clipping and polyfilling it, doing a point from volume
[9:27] creating some p-scale and some random orient and copying some spheres but they are intersecting.
[9:32] So what I do is, and here I'm of course packing because we need these for RPD and then
[9:38] I just do an animation from frame 1 to 3 and I animate a p-scale attribute from point
[9:43] 1 to 1.
[9:45] Then I merge in the barrel as a collision GU and pack it and in a Lopnet I'm just updating
[9:50] the p-scale in here and loading this barrel just a static object and this will just
[9:56] result in the intersection as you can see.
[9:59] So that's basically then just caching attributility and setting the initial pose which is just
[10:03] a transform that I copied from here where we set the initial position.
[10:08] So that's about the RPD simulations.
[10:12] What else after we bake the seam?
[10:15] I'm creating a random class based on the name attribute or for using later to colorize
[10:23] the balls then I do an enumerate to enumerate that class attribute because this is based
[10:29] on random SS which will give us random numbers positive and negative so I just want to enumerate
[10:36] those.
[10:37] Then in here I'm splitting the barrel and the balls and what am I doing in here?
[10:41] I'm setting an initial position for the original geometry so I don't want to use actually
[10:46] this geometry so I do a transform pieces to deform the original geometry matching the name
[10:51] attribute.
[10:52] In here I'm unpacking a natural boot deleting the RPD geometry and then just copying the
[10:59] orient, the class and the ID and just computing a point velocity.
[11:04] Of course in here I did that RPD disconnected phases to delete any interior phases when
[11:10] the geometry is united like this so I can show you I have already shown but when we are
[11:16] in the when the pieces are connected when the pieces are connected yes we don't have interior
[11:21] phases but as soon as we break we will have the different connections in here so just
[11:28] for refraction.
[11:31] Then in here I'm swapping again that temporary name attribute to the final name attribute
[11:42] and merging over.
[11:45] So let me see so we have the name we copy and we delete the name attribute for some
[11:52] reason I'm doing this in here but not sure why.
[11:56] So then we merge everything and this will be our out barrel and this is our animation
[12:01] and then I just exported to USD.
[12:04] So for the shading I just did a bit of work for the walls and the stairs so for that I am
[12:13] doing a basic UVN wrap on the walls and UV layout and I do the same for the stairs so
[12:21] polybavol also and where you reflect and the UVs will look like this and I subdivide
[12:25] and this is my stairs in here I do the UVN wrap for the walls and in this UV layout I want
[12:30] to make sure they don't overlap so I just did the UV layout and moved a bit the position
[12:35] in here on the UV layout so you can move it in here for the target position.
[12:39] This way they don't overlap and I can use both to do some shading that we'll see in
[12:44] a bit so basically I want to create some interaction between the wall and the stairs that's
[12:49] why I did that specific trick.
[12:51] In here this is just a basic UV flatten for the ground and this is my environment geometry.
[13:00] So I cover everything in here what I'm doing oh this is my camera it's not important so
[13:04] let's look at the Copnet work for this specific environment which might be a bit more interesting.
[13:11] So this is the shading for the stairs and the walls let's look the stairs first so I'm
[13:20] loading the geometry then I do some fractal noise, multi-directional work to get this sort
[13:25] of result to a mono and then mono to RGB and we get something like this then another
[13:30] fractal, remap it and do some blending again with some more directional work equalizing
[13:36] it and do in here a mono to RGB with a custom ramp that I just sampled from an image so
[13:42] with these lights a feature and then just blend it over so one a bit more bright and another
[13:49] with some moss let's say and I blend it over with this mask you can see in here.
[13:53] So this is my stairs I also have some displacement for the stairs so I'm just blurring the initial
[13:59] pattern then remapping it to be zero centred and remap it again for the final displacement
[14:08] since we don't want that much then do a fractal noise and add a bit of noise so if we actually
[14:12] connect it will not be very very good but yeah it's just faceted but we have some displacement
[14:19] that will look better in render then for the for this material it's actually a bit tricky
[14:26] to get this it's not tricky but I wanted to know how I could get an interesting pattern
[14:30] in here so basically the interaction between the wall and the stairs so for that I'm just
[14:36] loading in here so let me get rid of this I'm loading both geometries and they share the
[14:41] same UV island the UV island UV tile then I'm baking the ambient occlusion so as you can
[14:47] see we will have some mask around the stairs then I do a cache just in case and blur a bit
[14:54] the ambient occlusion so you can see I'm loading the occlusion and then I do a remap and
[15:00] non-uniform directional work using again some noise another one to get some noise and then
[15:06] a sloped blur and finally I multiply over some noise do a shenal split remap it again and
[15:12] blend it blend it with this ramp and I also have some some other texture for the walls so
[15:20] this is my final material and since we have that ambient occlusion mask we get this result which
[15:25] is not perfect but again it works so that was about the shading let me see what I have in here
[15:32] oh this is just the render of the video so then I have an animated camera for some reason it's not
[15:42] loading so let me see so it's just an animated camera along the path with some noise from
[15:50] from shops so as you can see I'm using some noise as constrained but there's a nice
[15:56] CGWiki video about that you can have a look so let's look next at the shading part okay now in
[16:04] salaries let's have a look in here I'm importing first the animated camera as you can see in here
[16:10] and I'm making sure since it's time-dependent I'm just doing a cache to remove the time dependency then
[16:17] I'm importing the scene so the environment scene with just a subimport then I do some gobble we just
[16:27] using a plane and blasting away some of the primitives with the with a noise then I sublayer in
[16:34] the barrel with the animation and everything so since I exported to USD then do a render geometry
[16:42] settings on the barrel just to use internal reflections then do another one for the gobble to remove
[16:50] the visibility on renders is I don't want this to show I just want to create some nice shadows using a
[16:55] dome light just a standard dome light so let's actually look at these and do a small render so I'm
[17:03] just using a dome light from poly even which was allowed to use and in here I did some some
[17:09] grass instances I used some procedural grass I did some time ago with simple tree tools so I don't
[17:15] want to cover that right now but then I'm just using an instacer on the plane just a bunch of points
[17:19] and copying over the variations that I have on the grass then for the materials as you can see let me
[17:24] show you an initial frame we have the the displacements of the of the stairs so for that let me see
[17:33] stairs I'm just loading the image from cops with the opc syntax do some color correction and loading
[17:38] also the displacement and changing a bit the eye so it's not so over the top and I'm also doing
[17:44] some displacement on the edges of the of the stairs as you can see besides the normal noisy one in
[17:51] here so yeah and this is for the stairs for the balls it's really simple just a random color based
[17:57] on that class that we generated then the walls is just the same just diffuse in this case just an
[18:03] albedo to create the walls and some color correction and I'm also doing the leads so just coloring
[18:11] it yellow and that's about it for the final image so this specific file will be available a
[18:19] stop-tier patreon benefits this month for the month of April you can go there download it and
[18:24] explore it on your own and the full file I'm not I'm sharing the full file you probably have to
[18:30] cache some things because I'm not going to share a huge file with caches so you will have to cache
[18:34] most of the texture I generated with cops so the only thing I don't I have a X-aner file is the
[18:41] HDRI but then again you can you can pick it from poly event so yeah thank you for watching I hope
[18:47] you found this interesting and I hope to see you next time thank you



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
