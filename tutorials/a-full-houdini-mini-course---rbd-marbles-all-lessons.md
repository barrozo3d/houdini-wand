---
title: a Full Houdini Mini Course - RBD Marbles [All Lessons]
source: YouTube
url: https://www.youtube.com/watch?v=2hYLgWms72Q
author: WTTR Labs
ingested: 2026-08-03
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/a-full-houdini-mini-course---rbd-marbles-all-lessons/
frame_count: 0
frame_status: pending-selection
---

# a Full Houdini Mini Course - RBD Marbles [All Lessons]

**Source:** [YouTube](https://www.youtube.com/watch?v=2hYLgWms72Q)
**Author:** WTTR Labs
**Duration:** 327m17s | 16 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py a-full-houdini-mini-course---rbd-marbles-all-lessons <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Lesson 00: Course Trailer [0:00]
**Transcript (timestamped):**
[0:00] K intermediate
[1:00] Welcome back and welcome to the workflow planning section for our first of the YouTube mini courses.


### Lesson 01: Workflow Planning [1:06]
**Transcript (timestamped):**
[1:15] So I'm super excited to jump into this.
[1:16] What we're going to do today in this video is we're going to actually work through the
[1:21] first three stages of the Node Navigator Blueprint core loop.
[1:26] And we're not going to learn about this loop.
[1:28] I'm just going to start kind of working here.
[1:31] And if you are interested in learning about this, I will link a video below that covers
[1:36] a little bit more about this framework itself.
[1:39] But I do recommend you download the project files because you will be able to pick up
[1:43] exactly from where we're working off and follow along with as much or as little as you would
[1:48] like.
[1:49] So very first step, I'm going to go through stage zero, the client, and we're going to
[1:54] come up with the results of what we want to make in this project.
[1:57] And if you've already seen the trailer video, which should come for this in the playlist,
[2:02] then you'll actually have seen the exact result that we are making here today.
[2:07] So let's begin.
[2:08] I'm going to get my yellow pen out here, stage zero, zero, the client.
[2:22] And what we're going to create today is we're going to create a motion graphics, motion
[2:28] design kind of 3D style, actually definitely 3D, but some kind of little animated pegboard
[2:36] of these spheres, maybe they're marbles that are starting at the very top.
[2:44] Maybe there's one row of them.
[2:47] Maybe there's two rows of these spheres.
[2:51] And then every once in a while, one of them randomly starts to fall.
[2:56] And once it does, it's colored a different color.
[3:01] And we can see that it is then active.
[3:05] And these are all kind of the darker gray ones, the less exciting ones.
[3:10] And as they fall, they're going to start interacting with maybe some shapes, some pegs, some static
[3:20] objects actually, so some ones that aren't moving.
[3:23] And then maybe some wheels that are spinning.
[3:29] And we've got a couple of different ones that spin different directions.
[3:35] Maybe there's one down here.
[3:38] And then maybe there's more pegs at the bottom that they can then bounce against.
[3:47] So as these fall, perhaps this blue one comes and hits this peg, bounces here, rolls off
[3:57] the side, and then falls down.
[4:00] Maybe this orange one would have hit here, bounced over, maybe hit this side, rolled
[4:09] down, and then rolled off again here.
[4:12] So this will be a full simulation, and we will have the opportunity to create some randomized
[4:18] seeds, some different versions, and then hopefully a couple cool shots out of the end result
[4:24] of this one.
[4:26] So I want this full simulation.
[4:28] So I'll say pegboard simulation, marble, pegboard simulation, and we want a few cool
[4:49] shots.
[4:50] And maybe this will be one wide shot, and we could have a tight shot of, if actually I
[4:56] could draft these in maybe a dotted red.
[4:59] And we've got a macro shot up close of this one here.
[5:04] Maybe there is another camera here that is looking at this orange one.
[5:12] And then maybe we've got a full frame shot of them all, and then maybe one cool shot
[5:21] of some of these on active balls.
[5:23] So maybe we can see one of them becoming active and slowly glowing.
[5:31] So yeah, that might be kind of cool.
[5:32] And we might even make up some extra shots once we see what this looks like.
[5:36] That's usually how I like to work.
[5:38] I'll create this whole setup, and then I'll just look around and see if I can find some
[5:43] cool angles that would end up looking good in a final animation.
[5:49] And that's part of the really cool thing about simulations because you don't really know
[5:52] what you're going to get.
[5:53] So it's not similar to animating where you're actually choosing exactly what you get.
[5:58] You kind of set these rules, and then you have some happy accidents that might come
[6:03] along.
[6:04] So that'll be stage one.
[6:06] Stage, excuse me, that'll be stage zero.
[6:10] Stage one is the director.
[6:24] And what we want to do in this video, or excuse me, in this stage is we're just going to list
[6:28] out the core components of our shot.
[6:33] So we have our pegboard.
[6:37] We've got our marbles.
[6:44] We've got our, we'll say lighting.
[6:50] And we've got our cameras.
[6:55] So those will be the four chunks that we're actually going to have.
[7:01] We actually will have materials as well.
[7:06] And those sometimes I like to organize under the individual objects and sometimes separately,
[7:11] but that won't be too important on how to choose to organize those for the pegboard.
[7:17] We'll have maybe the backboard.
[7:22] Maybe we'll have the pegs themselves.
[7:28] Maybe we'll have the rotating boards for the marbles.
[7:36] It really is just a sphere.
[7:38] So maybe there's one sphere and a collection of all spheres.
[7:51] Lighting, we've got an HDRI, maybe a key light.
[8:00] And then the cameras, obviously we'll have one, two, three.
[8:05] However many cameras we have and materials, I either want to do a wood material or a plaster
[8:13] material.
[8:14] So kind of a neutral color.
[8:16] And then the colors I actually want to have be mostly coming from these objects that are
[8:23] falling.
[8:25] So kind of a neutral tone.
[8:27] Maybe I'll just say pegboard material and marble material.
[8:44] I could put a little box next to each of these.
[8:49] And these would be our individual chunks.
[8:51] And we would have the option, which in this case perhaps I won't do that.
[8:54] Maybe I'll actually just do one of them.
[8:57] We can break those chunks into the individual tasks that they are the individual tasks that
[9:04] have to be completed in order for the chunk to be implemented.
[9:07] What this means is if I look at our pegs right here.
[9:15] And perhaps I imagine that my board is at a slant.
[9:21] So as these spheres fall down and become active and start bouncing around my simulation,
[9:29] they're not rolling off the edge here.
[9:33] So the way I might create these pegs is I could either create one peg.
[9:39] So create one peg, copy peg, and place peg.
[9:58] What we could do is maybe this was a grid that had a bunch of different divisions here.
[10:05] Maybe for each of these little squares, we find the center and place a peg there.
[10:11] Or on each of these vertices or these points, excuse me, we would place an individual peg.
[10:16] There's plenty of different ways to go about creating the actual geometry.
[10:20] And the point of breaking them into tasks is to reduce the complexity of a component
[10:27] of your project and make your individual setups needed be a little more straightforward to
[10:32] actually come up with.
[10:34] But for now, since this is a relatively simple project, we're going to stick with this and
[10:40] actually now moving to stage two, the pipeline manager.
[10:56] And what we need to do in this stage is we need to start thinking about the dependency
[11:00] orders of these individual components and how we're actually going to organize those.
[11:07] So what this means is we want to start thinking about which ones depend on which.
[11:11] And if we start thinking out loud, we know that the materials obviously need to be created
[11:19] and assigned.
[11:20] They could actually be created before our geometry is created, but they need to be assigned
[11:25] after our geometry has been created because we can't assign a material to a pegboard that
[11:29] doesn't exist.
[11:31] And these marbles, they could be created before our pegboard is created, but they can't be
[11:37] simulated until we have both the marbles and the pegboard and perhaps these animated objects
[11:42] as well.
[11:48] So the way I'm going to draft out this one is we'll make a network from top to bottom.
[11:56] This is the start and this is down here, the end.
[12:02] I'll put rendering here at the bottom.
[12:08] And we can actually now start to think how we can arrange these for our dependencies.
[12:13] So lighting and cameras and materials perhaps can come down at the end.
[12:19] So this can be camera.
[12:25] This can be my lighting.
[12:27] And maybe my materials are here.
[12:35] And now what I would need to do is I need to have a pegboard and marbles and then a
[12:40] simulation.
[12:44] So one pegboard might be at the very top.
[12:53] Marbles I could actually create those here or I could create them here to the side.
[13:00] So these could be my marbles.
[13:06] And the important thing to note, and we won't go into too much detail here because I'm going
[13:09] to hopefully assume we've seen some of the other videos on this channel that the items
[13:15] above are what we either are dependent on or may need in order to complete a section
[13:21] here.
[13:22] So this is kind of being sketched out in the same way that a Houdini network graph would
[13:27] be created.
[13:28] So this component right here was our simulation.
[13:34] What we need to have both the pegboard and the marbles themselves.
[13:40] And we could also do is we could create the marbles, create the pegboard and then simulate
[13:46] and kind of have these all lined up here.
[13:50] Or it could be create marbles, create pegboard and then somehow that information is merged
[14:00] and at the bottom here we simulate.
[14:04] So this will make a little bit more sense once you start using Houdini a little bit
[14:07] more.
[14:08] And hopefully this does make sense if you have seen some of the other videos.
[14:12] But for now we just need to think about the order.
[14:14] We're going to set these up in and a lot of actually setting that up is part of the engineer
[14:19] stage once we get into Houdini.
[14:23] But one more stage the pipeline manager, which perhaps does overlap with the engineer is
[14:29] actually the Houdini organization, which is kind of the scaffolding of where we'd create
[14:37] individual components here.
[14:39] So maybe we're doing the geometry context or SOPs for our pegboards and for lighting.
[14:45] Maybe we're using Solaris, which is actually what we're going to be using for this course.
[14:50] And then cameras could do that at the object level and then bring that into Solaris.
[14:55] But we want to start thinking about the containers we're actually using to organize and create
[15:01] everything we need for this project.
[15:05] So awesome.
[15:06] Apologies for that quick cut.
[15:09] We've actually just completed the first part of our workflow planning.
[15:14] And what we're going to now do is we are going to open up Houdini in the next video and start
[15:20] setting up the Houdini organization for how we're going to organize and approach the rest
[15:25] of this project.
[15:26] So awesome.
[15:27] That'll be all for this video and I'll see you in the next one.


### Lesson 02: Houdini - Context Organization [15:35]
**Transcript (timestamped):**
[15:36] Welcome back and welcome to the Houdini organization lesson for this mini course.
[15:41] What we're going to do in this video is we're going to take the plan that we came up with
[15:45] from the workflow planning lesson and we're going to start implementing or excuse me actually
[15:50] we're going to start organizing the way we want to set this network up within Houdini
[15:55] and start thinking about our data.
[15:57] So if you haven't downloaded the project files, I do recommend you do so.
[16:01] So you can follow along with this exact setup and then also have the final files once we
[16:06] complete them.
[16:07] I'm just going to rearrange these windows a little bit because I want to be able to see
[16:13] my workflow plan in the bottom right and be able to modify and move within my network
[16:19] view here in the middle.
[16:21] So very first thing I'm going to do is we're going to create a geometry container and we'll
[16:25] use this to create our pegboard.
[16:34] Perhaps we could, well we could actually create another container for the marbles.
[16:39] Maybe I'll say this is all my geo and we'll keep it simple for this one.
[16:44] We'll create a LOP network as well, which is render my scene.
[16:51] And what we need to have is we're going to have a pegboard.
[16:55] We're going to have some static objects, some animated objects, some marbles and we're actually
[17:04] going to need to have, or maybe we'll do two ones.
[17:10] We'll say setup pegboard and we'll say background assets or geo.
[17:22] So maybe we'll have some backdrops, some additional geo here and then a main pegboard as well
[17:28] as our simulation.
[17:29] And the organization of where you choose to do the work isn't really a huge deal.
[17:33] It's just however you choose to work.
[17:37] I'm going to jump inside the LOP network and we're going to create two nulls, which
[17:45] will be the start and the end.
[17:52] And now we can start thinking about how we might be organizing some of this setup here.
[17:57] So we'll grab a camera because we do know we want one of those.
[18:02] I'll add that in there.
[18:05] I'm going to say dome light.
[18:10] We need to graph the branches to connect these in merge.
[18:18] And I won't define any primitives yet because that is something I'll save for the next video.
[18:24] But what we're going to want to do perhaps is create another graph branches, put it up
[18:30] here and this could be our background scene.
[18:35] And maybe within here we've got another merge and we might have a backdrop so I could grab
[18:43] a SOP import because we might want to create a backdrop.
[18:48] I'll move these up here and this might be our background and then we may be able to
[18:56] have one for our main scene.
[19:00] So I'll say pegboard merge and hopefully all of this feels pretty familiar to you and
[19:09] if it doesn't I do recommend you check out some of the beginner videos on the channel.
[19:15] Maybe this will be pegboard.
[19:20] You could say static and then pegboard.
[19:27] Animated.
[19:29] Maybe there's parts of the board that are static parts that are animated and then we
[19:34] have our marbles.
[19:39] So again I'm not going to define any of these primitives and I'm going to wait to do that
[19:44] once we actually have some of our objects and information moving through this network.
[19:49] So another thing we're going to need is a karma render settings because we're going to be
[19:52] using karma.
[19:53] I'll ignore that error for now.
[19:56] I'll connect to this and I'll say my really great render and this is going to be all we
[20:03] need for our solaris setup and this is essentially the lighting, the camera and the render settings
[20:11] that we've got here planned at the bottom.
[20:13] We actually would need materials so I'll create a material library and one important thing
[20:18] to note we could create the materials up here but we had mentioned actually in the last
[20:25] video that we need to create the materials before we assign them and we need to create
[20:29] the geometry before we assign the materials.
[20:31] So if I didn't assign materials here that wouldn't work.
[20:36] This needs to go down at the bottom or even down here.
[20:40] For now I'll actually move all of these materials down to the very bottom and perhaps color
[20:45] those purple just hitting C to get that little color panel there.
[20:51] It's going to be all for my solaris setup.
[20:57] And now what I'll do is perhaps jump inside my background geo.
[21:02] I'll make a little network box and I like to color these dark black so they just hide
[21:08] out of the way and I'm going to get a null.
[21:11] This will be out my backdrop.
[21:16] And I'll say create backdrop here and I do want to have some kind of studio background
[21:24] because if we are looking at the side of this pegboard instead of seeing just a dark black
[21:29] scene behind or seeing our HDRI accidentally I'd rather have a solid color or some additional
[21:36] geometry that I could choose to change the materials if I see fit.
[21:40] So for now it'll be out my backdrop.
[21:42] That'll be fine for our background geo and then for the pegboard I'm going to have the
[21:51] pegboard itself.
[21:54] I'll color this dark as well.
[21:56] And maybe I'll have out static pegboard and out animated.
[22:07] And these could actually be combined.
[22:11] There's no need to have those split.
[22:14] So as we work we might see a couple different ways of organizing.
[22:18] Then maybe I'll duplicate this for spheres.
[22:22] So I sphere marble and this will be my main marble.
[22:33] And we will actually be doing a simulation in this mini course.
[22:39] So I'm going to color this dark as well and this will be our simulation.
[22:45] And we'll see a couple different ways of organizing this but we're not going to go too far into
[22:51] the fundamentals of simulations.
[22:53] We're just going to cover some of those and if you do want to learn a little bit more
[22:56] there is a RBD lesson on the channel as well.
[23:00] And then within level up Houdini we have dozens of hours actually covering simulations and
[23:08] soft workflows and dot workflows and all that good stuff all from scratch.
[23:13] So definitely check that out if you're interested in learning more Houdini.
[23:17] So that'll be my simulation.
[23:20] And that should actually be good.
[23:26] And while we're actually in here I'm going to do pegboard static, pegboard animated,
[23:32] marbles, backdrop and just to stay consistent I am actually going to link these nodes.
[23:38] So in the bottom right I'm going to go to background geo, out my backdrop.
[23:43] I'm going to drag this up to here and this parameter panel is linked to this node because
[23:48] I've got my one and my one checked up there and this one is independent because it's
[23:52] now pinned so it's working by itself.
[23:56] So that'll be good.
[23:57] Maybe I'll color that a green to note that I've added that in.
[24:02] I'll go into my setup pegboard.
[24:06] I'll put this out static on pegboard static and out animated.
[24:14] I can actually put this on pegboard animated.
[24:16] And one thing we do want to be aware of is as we start doing simulations we want to be
[24:23] considerate of where our render objects are coming from.
[24:28] So in this case I wouldn't actually connect my main marble here because I'm going to make
[24:33] a first marble and then I'm going to have to simulate and what I'll actually have is
[24:39] animated or simulated rather.
[24:45] And marbles would be down here.
[24:50] And this marble will somehow be combined with the information here and actually if I do,
[24:58] if I drag this to the null it'll snap this network view to where this one was and what
[25:04] I can see is kind of the same idea that's happening here.
[25:07] I could have my marbles in one network square.
[25:11] For now maybe I'll color those green and then I could have my pegboard in the other
[25:16] and then I combine them both and they both need the simulation rather needs the information
[25:20] from both of these objects to actually simulate.
[25:24] So we'll see that again once we set up the rest of this workflow.
[25:29] But for now that actually should be the end of our workflow organization within Houdini.
[25:38] So I'm going to go file, save as.
[25:41] I already started pegboard 01 so I'll actually override this file.
[25:46] I'm going to accept and overwrite.
[25:50] And now that should be good and we're going to start in the next video to actually start
[25:54] creating some of this setup and slowly get closer towards our end goal.
[25:58] So awesome.
[25:59] That'll be all for this one and I'll see you in the next video.


### Lesson 03: Houdini - Layout Prep [26:06]
**Transcript (timestamped):**
[26:07] Welcome back and welcome to the first of the implementation lessons for setting up some
[26:13] more of our scene.
[26:14] If you haven't yet downloaded the project files I do recommend you grab those below.
[26:19] We are just going to pick up from exactly where we left off in the last video and the
[26:23] very first thing we're actually going to do is I'm going to create our background geometry.
[26:28] So to create this background geometry I'm going to use a grid.
[26:33] Set my display flag here.
[26:34] I want two rows, two columns and I'm going to extend actually out one side, UV unwrap
[26:41] it and then move that side again to make a nice bent area.
[26:46] So I'm going to grab my selection, switch to edge, select this one down here and poly,
[26:54] extrude this and I'll set this to 10 on that unit right here.
[27:01] And while that's actually still highlighted I can grab a transform and replace that right
[27:09] up here.
[27:10] So I'll say 10 and 10 and your units might be different depending on which axis you selected.
[27:17] So in this case I've got my negative x-axis here so I've had to move that back so it's
[27:22] placed at the origin or rather actually aligned with the zero.
[27:28] Now what I want to do is I'm going to add some bend to this one.
[27:31] So I'm going to do a subdivide first to get some additional resolution.
[27:37] If I set this to open sub div by linear and set this to three I can get some of these
[27:42] supporting edge loops and then I'll do another subdivide.
[27:45] Maybe set to three as well to get some nice smooth geometry and then I can change the
[27:53] bending of this curve based on how many subdivision loops I have in this first one.
[28:00] So I'll set that to perhaps to two and I want this to be pretty big so I'm going to transform
[28:09] this up to five and connect this to out my backdrop and we actually do want to have UVs
[28:15] on this just in case.
[28:16] So I'm going to use UV unwrap and I will UV unwrap this before I actually subdivide
[28:23] it rather actually before I move this edge.
[28:28] So I'll have a nice flat UV area here and then that will be respected as we transform.
[28:35] And one thing to note is we're not actually scaling the height of this so our UVs will
[28:40] not be stretched.
[28:44] So ten and that same ten here is the same ten that I grabbed on my distance and if I
[28:49] wanted to I could link those so copy parameter and paste relative references but there is
[28:59] no need to do that.
[29:08] So I'm going to undo that and it looks like that actually wouldn't have worked.
[29:14] So we'll stick with that ten and out my backdrop and that's actually going to be good for our
[29:22] backdrop.
[29:23] So I'm going to hit U to go up and now what I want to do is I'm going to jump inside pegboard
[29:30] and I'm going to create a, I'll use a box to start creating this pegboard actually rather
[29:37] that I'm going to use a grid.
[29:39] And I only want to do a very simple setup.
[29:41] I'm going to make this a vertical pegboard so I can rotate that or I can change the orientation
[29:51] for the grid plane.
[29:55] Maybe I'll make this 12 by 6 and we can definitely change this later so there's really no issues.
[30:04] I can leave that back at the zero center and I'm going to do poly extrude to give some
[30:09] thickness to this.
[30:13] I can set this to one.
[30:16] Actually maybe let's make it a little bit thinner.
[30:17] We'll do point two five and I'll do a poly bevel point, we'll do point zero one and I
[30:31] don't want to be extruding these inside faces here.
[30:34] So if I go to exclusions, ignore flat edges and set this to a value like 25, it will only
[30:39] be bending the corners rather than these faces here or only be beveling, excuse me.
[30:45] So that the three and now what I want to do is I'm actually going to transform this so
[30:52] it's not perfectly straight because for our simulation we're going to want to have this
[30:56] be slanted.
[30:58] So I'll say rotate peg board and for now I'll connect this to the out static just because
[31:06] I want to get this into Solaris so I can start setting up a very, very basic dome light and
[31:15] HDRI just so I can see that we've got at least something to start working with.
[31:19] So I'm actually going to transform this up here within my soft context.
[31:33] So now once I jump into Solaris, I look at my backdrop and this is merging correctly because
[31:40] we have grabbed this from the previous video and now let's actually start defining our
[31:46] primitives that we'll need to use.
[31:48] So on this graph branches, I want to merge everything from the right and this is going
[31:53] to be put that on backdrop for pegboard static looks like it's the only one connected.
[32:10] So perhaps I'll actually cut these two wires by holding Y and dragging that here.
[32:19] So let's craft this one and I'll put this on slash peg board or maybe I'll say props.
[32:30] I'm going to jump inside my materials, create a very basic material for now.
[32:38] I'm going to say actually USD material X builder.
[32:44] I'll say this is backdrop.
[32:47] I'll say this is pegboard or actually simple pegboard and simple backdrop.
[33:02] And then for backdrop, let's choose a gray color and for pegboard, I'll choose some
[33:11] kind of natural wood tone.
[33:14] So I'm going to hit U to go up twice, auto fill materials, assign my materials and then
[33:24] let's assign these to our pegboards.
[33:26] So pegboard static is the prop or the primitive we want to assign the material to and the
[33:32] material I want to get is simple pegboard.
[33:36] And then we'll do another one for backdrop and I'll get simple backdrop.
[33:46] And we can actually preview our camera because that has been created down here.
[33:50] So I'll say this is hero cam set my display flag down here, either at or below.
[33:58] I could actually go all the way down, bringing in this null to end.
[34:04] And now if I select my camera, I'll see where it is, which is actually at the zero, zero,
[34:07] zero.
[34:08] So I can select my lock icon and reposition this camera.
[34:15] Let's find a nice view here where we can actually see.
[34:20] Middle mouse or excuse me, alt and middle mouse button to pan alt, right click to zoom
[34:27] and alt and left click to orbit.
[34:35] So I'll see 36, actually zero rather excuse me, two here.
[34:45] There is negative two I want to set to zero because I want to even these out.
[34:49] So we're looking straight at our object.
[34:55] And this is now negative 270, but I put this to 90, which will make that a positive.
[35:03] And negative 270 actually would have worked as well.
[35:06] Because it's 360 degrees of rotation would circle it back to where it was.
[35:13] And perhaps I'll lower this middle mouse to increment those individually.
[35:21] So maybe that'll be hero cam.
[35:25] Let's go all the way down and we can actually look at our dome light.
[35:31] And if I actually switch this to karma, we will see hopefully our render.
[35:38] And it's not too exciting because we have no actual HDRI here set up.
[35:44] So on our dome light, I'm going to go to texture.
[35:47] And I actually have included this.
[35:49] So you should have it as well.
[35:50] We're just going to use this HDRI here.
[35:55] And it looks like we're not actually getting this because we have not
[35:59] grafted this primitive into our graph branches.
[36:03] So if I select my end down here, you can actually see there is no HDRI and there's
[36:07] no lights primitive because I haven't actually done that here.
[36:10] So I'm going to switch this to the root primitive to get everything from this right side.
[36:15] And I want to place that on lights.
[36:19] And now it will be under lights and lights because this light has created this primitive
[36:24] prefix here.
[36:25] So this additional one, but I'm not going to worry about that.
[36:29] We can rotate this around.
[36:39] I'll leave it here.
[36:41] And what I also like to do is switch to correction toolbar and grab aces.
[36:46] So we can see this with a little bit better of color.
[36:49] I could hide that display of you if I wanted.
[36:52] And also I could hide my.
[36:55] Background by hitting W to switch to wireframe or hitting D display environment lights
[37:01] in the background and unchecking that.
[37:04] So all right.
[37:07] One more thing we'll do is actually assign this to Karm XPU and then make sure we've
[37:12] got our hero cam selected.
[37:16] We can even take a little snapshot by opening this one here.
[37:20] We'll say our hero cam is selected.
[37:22] We can also open this one here.
[37:24] We'll say our first render.
[37:30] All right, switch back to Houdini VK for Vulkan.
[37:34] And I think that should be good for the first setup here.
[37:46] So all right, I'm going to pause the video and come back to the next one.
[37:50] I can double click this to bring it open.
[37:53] Right click, color correction and view that again with my color.
[38:00] Or actually while we're here, perhaps let's add two or three more cameras.
[38:05] So I'm going to duplicate by alt dragging.
[38:07] I'll say this is cam 01.
[38:10] We'll select that.
[38:13] Maybe get a different angle.
[38:15] I can change my focal length.
[38:18] Maybe a 35.
[38:20] Actually, rather perhaps I want this to be longer.
[38:23] I'll do 135.
[38:26] Maybe find a nice corner.
[38:28] And I'll do it one more time.
[38:30] Cam 2.
[38:36] Maybe this is zoomed in at the center here.
[38:39] So we'll see what this all looks like once we actually add the rest of our objects.
[38:43] But for now, this should be good.
[38:45] We'll end the video here and I'll be back in the next one.


### Lesson 04: Houdini - Peg Board Modeling [38:52]
**Transcript (timestamped):**
[38:53] Welcome back and welcome to the next Houdini lesson in this mini course.
[38:57] We're going to pick up from exactly where we left off.
[39:00] And we're actually going to jump inside setup pegboard to create our main pegboard.
[39:05] As well as the animated objects that we'll be using here.
[39:10] So, very first thing I'm going to do is make a little bit more space.
[39:17] I'm going to move my grid up here.
[39:19] And I actually now want to scatter some pegs on this object.
[39:22] The two ways I could do that is I could either use these points themselves.
[39:26] Or actually rather two of the ways I could do that is use these points themselves.
[39:30] Or I could scatter points and then copy to those points.
[39:33] But before I do that, I'm going to create a tube.
[39:36] Because this is what I actually want to be copying on all of my individual points.
[39:40] So I'm going to select this guy here.
[39:43] Maybe I'll make it point two five for the radius.
[39:46] I'll add end caps.
[39:48] And I actually want to have this oriented along the Z axis.
[39:52] So I could just do a transform.
[39:55] Rotate this.
[39:59] And I'm going to use a match size to place the edge of this right at zero zero zero.
[40:05] And align it along this positive Z axis.
[40:08] So if I set this to min, I'll now have this set at zero.
[40:12] My positive axis going in this direction.
[40:15] And then we need a copy to points.
[40:21] On the right side, I put the points I want to copy to.
[40:24] And on the left side, I put the object I want to copy.
[40:30] If I preview this, we'll now see our object is correctly copied to all these points.
[40:36] And this is one way we could do it.
[40:38] We can then modify the rows and columns.
[40:41] And if we have six and 12, that will give us a square, or square grid.
[40:48] And by changing this, we'll actually change the number of objects copied.
[40:54] But perhaps we want to do a scatter, maybe with 100 points, and copy to there.
[41:01] One thing we'll actually notice is that the scatter, we're now no longer getting our object copied in the correct direction.
[41:08] And the reason for this is we now need to actually recompute these normals.
[41:12] Because these normals are implicitly calculated by Houdini by this copy to points.
[41:17] But when we scatter, these points now no longer have information about the normals.
[41:22] And they're actually not on these points.
[41:24] So we can create a normal attribute on the grid before we scatter.
[41:29] If I could create this on points here, we'll see that now on my geometry spreadsheet.
[41:34] And if I scatter, we'll actually see that that attribute is being copied to the points that are scattered on the grid.
[41:41] By enabling and disabling this, we'll see that my normal has appeared and disappeared.
[41:47] So I'll go copy points here, and we can see this grid.
[41:51] And this might give me a little bit more of an interesting setup, because I'm going to be able to get a little bit more randomization.
[41:58] And if I actually even have some of these that are too close, my balls won't be able to fall through.
[42:04] Should I leave this at 100?
[42:06] Maybe even a few, a little bit less.
[42:09] Maybe 44.
[42:14] And I can merge this.
[42:16] I actually wouldn't want to merge this yet.
[42:24] I'm going to grab my polybevel and my poly extrude, because this is the base, the back of the board.
[42:31] These are the pegs.
[42:34] So I'd merge these here together.
[42:38] And now we've got our pegs on the board.
[42:41] I might even need to add a output back for this one.
[42:53] And then for now, maybe I'll go with no scatter, just so we're getting this even split here.
[43:00] And I could even transform this grid to be a little bit bigger.
[43:05] So we're now no longer seeing that on the edges here.
[43:09] So this will be good for now.
[43:11] What I'll now actually want to do is I'm going to remove these middle ones and then replace those with some rotating objects.
[43:18] So the way I'll remove those is I can either do that on these points themselves before I copy or I can remove the whole objects once it's been copied.
[43:28] I will do a group.
[43:33] I'm going to go to delete, keep in bounding regions.
[43:39] And if I hit enter over my scene view, I'll now have this active gizmo.
[43:45] And I can just group the points that I'd want to have deleted.
[43:49] And if I set this to points, I can now use a blast node to delete these as well.
[43:57] So I'm going to go blast, go to delete, and it will remove those points here, then no longer copy here on my copy points.
[44:09] And now maybe I want more on the top so I could increase the size of my grid and we'll have more.
[44:14] But one thing I actually do want to do is on this grid, I'm going to go to the size and I want to copy the relative parameter for X and paste that on columns.
[44:23] So paste relative reference and I'm going to copy for Y the second value here and paste that on rows.
[44:30] And now no matter how big I make my grid, I'll always have an even square setup.
[44:37] So I'll leave it this at six or perhaps even 12 and 12.
[44:44] And by changing where this group is, I can choose which objects are being deleted.
[44:53] And one nice thing about this is now if I want to have just these boards be essentially where these are not, where there are no pegs, I could actually use this group.
[45:07] So I'm going to make a little bit more space, actually quite a bit more space.
[45:15] So now that I've grouped these rather than delete, because if I just did a delete node, I would have the option of deleting by a bounding volume.
[45:27] But I want to delete these for these pegs here that are copied.
[45:34] And I also want to delete non selected for the center.
[45:38] So now what I'll have is I'll have this opportunity to have these rotating little blocks.
[45:46] Welcome back.
[45:47] Apologies for that quick cut.
[45:49] Before we actually continue, what I'm going to do is rearrange this a little bit, just so it's a little bit easier to follow along with.
[45:56] Very first thing I'm going to do is hold Y to cut the wire.
[45:59] I'm going to delete my merge and I'm going to move these over the left just to make some more space.
[46:05] So on this one, I've got my pegs.
[46:08] And if I uncheck my template flag, I'll just be seeing this here.
[46:13] I'm going to name this my peg board.
[46:20] Or I'll just say pegs.
[46:25] And then here I've got the delete non selected to the opposite side of my grade here.
[46:31] And I'll actually grab the center of this using a centroid.
[46:40] If I go to detail, it'll give me a single centroid.
[46:43] But what I also want to have is I want to have the normal.
[46:47] So I'm going to transfer the attributes.
[46:54] And it won't be transferring because it is on the detail.
[46:56] So there's no normal attribute on the detail.
[46:59] And I can actually use an attribute transfer to transfer to that point and from here.
[47:08] And I just want to get that normal.
[47:10] So now the normal five preview here will be matching the same direction as the grid.
[47:16] And now I'm going to create the actual box that I'm going to copy to these points.
[47:22] So in the same way I want my positive Z axis to be the one facing outwards.
[47:27] I'm going to scale this down.
[47:30] Maybe point two.
[47:34] On my X maybe I'll make it three.
[47:38] Maybe even four and I can always change this later.
[47:41] And then I'm going to use a match size as well to match it min.
[47:46] And then that will even even these out just in case I had accidentally moved my centers.
[47:52] So this will be the object I'm now going to copy.
[47:55] I'm going to put this in another transform which I will name rotate.
[48:00] Because I will want to actually rotate this along this Z axis.
[48:05] And I can do this with a dollar F and then multiplied by maybe three.
[48:10] And this is just the frame number.
[48:12] And then the scaling of three is going to make making it rotate three times faster than whatever the frame value is.
[48:21] So I'll grab a copy to points.
[48:24] I want the geometry to copy on the left side and the target point I want to copy to on the right.
[48:31] And now if I control and click the template flag we'll see this is my pegboard with my rotating object.
[48:40] So now in this case it might be a little bit too tall because it might be a little too close to that pillar or that peg.
[48:48] So I could even decrease the X size by middle mouse dragging left and right.
[48:54] Maybe I'll leave that only at three.
[48:59] So there we go.
[49:00] Now we've got one.
[49:01] And if we did want to duplicate this.
[49:07] This can be our rotating peg.
[49:19] And because we are going to be doing simulations for this one.
[49:31] Well maybe we'll set it up first and then clean it back up for simulations because there's some attributes we'll need to create.
[49:38] But I don't want to be doing that in this video because I want to stick with just the main setup.
[49:48] Yeah we'll be okay for now.
[50:04] There's one more thing I'm thinking about and I'm deciding on how complex I want to make the simulation.
[50:09] But we'll stick with this one and it should be good to go.
[50:14] But if you have any questions let me know in the comments.
[50:16] Welcome back.
[50:17] Apologies for that quick cut.
[50:18] We're going to continue where we left off.
[50:20] And I'm trying to decide on how complex I should make the setup because there's a bunch of simulation gotchas.
[50:28] We're going to have to try to avoid.
[50:29] But instead of trying to go too complex and prep this for a really big and robust simulation setup.
[50:36] We're just going to try to keep it simple and we'll debug future problems as they come up.
[50:40] So I'm going to transform this and I'm actually going to copy the point before I copy my object to the point.
[50:50] So I will move this maybe three units maybe 3.5 actually to the right and then transform it negative 3.5 to the left.
[51:03] And then I will merge these three together to have my three points.
[51:11] And if I plug this into the copy to points, I'll now have three objects rotating here.
[51:24] And if I didn't want to rotate this around a different object or have one of them rotating a different orientation,
[51:30] the easiest way to do that would be to cut this and just copy a object that's rotating in the other direction.
[51:39] So maybe this is negative frame three and copy that one to here.
[51:45] And then I can merge these together.
[51:49] So I'll now have these rotating in different directions.
[51:53] And that actually is kind of cool how they do all line up.
[51:55] So I'm sure that's going to give some nice simulation results there.
[52:00] So this will be my rotating pegs and one actually simulation gotcha, which I will mention right now.
[52:09] We have animated geometry and it is not packed.
[52:15] So I won't do that now because I'm going to wait for the simulation lesson to set that up.
[52:20] But typically when we are working with geometry and simulations, we would want to have it packed and then animate it.
[52:26] So we don't have to use the deforming attribute within our RBD simulation, but that is a little bit more of an advanced topic for now.
[52:35] So if you're following along, do not worry about that.
[52:38] So we've got pegs.
[52:40] We've got rotating boards.
[52:42] And this one should actually be the backside of our board.
[52:49] So I'm going to move this down here.
[52:55] I'll say this is my main board.
[52:59] And I'm going to cut this wire at the bottom.
[53:03] And then let's merge this together just to see what we have.
[53:14] One thing we might want to do is I'm actually going to move this main board a little bit to the left so we're not having any intersection with that geometry.
[53:24] So I'll transform negative 0.25, which is actually just the distance we had extruded it.
[53:40] So there we go.
[53:42] Now what I'll do is I'll do a quick flip book here.
[53:45] So flip book with new settings, size.
[53:48] I like to uncheck resolution just so it renders at the same resolution as my scene view.
[53:57] And then I'll let this play out and perhaps we'll end the video here.
[54:01] So we've got some nice, easy to follow and individual lessons to go through one by one.
[54:09] And while we're actually here, perhaps I can do a file.
[54:16] Export FFM peg.
[54:22] And I'll name this a new folder, anim, say pegboard preview say 0.1.
[54:32] Accept, save, and now we've just exported an animated preview or a video preview of what we've got here.
[54:42] So awesome.
[54:44] Close that out.
[54:45] That'll be all for this video and I'll be back in the next one to keep working.


### Lesson 05: Houdini - Marble Prep [54:53]
**Transcript (timestamped):**
[54:54] Welcome back and welcome to the next lesson in this Houdini course.
[54:58] We're going to continue from exactly where we left off and the end result we had from the last video was our pegboard with these animated boards.
[55:07] And now what I want to do is we're going to set up these spheres that we're actually going to be dropping onto our objects or rather onto this board.
[55:17] So there's many different ways to set this up and there's many different ways to set this up procedurally.
[55:23] But I think the easiest way to do it is going to be just making a line and then copying some spheres on that line and making sure that the line lines up with our grid.
[55:35] So I'm going to grab a line.
[55:37] I want this to be in the Z axis.
[55:41] So I'm going to set the direction to Z.
[55:43] And for the actual length of this line, if I template this right here and even template my grid as well.
[55:52] And if I had to enter over my scene view, I can see that my line I can change its length.
[55:59] But I want the length to be the width of this grid.
[56:04] So I'm going to copy parameter and I'm going to paste that on my relative reference for the length here.
[56:11] And to make sure it's lined up, I'm going to use a match size to line it up with a grid.
[56:20] And for the Y, I will set max here.
[56:23] And now my grid is exactly or rather my line is exactly the top of this grid.
[56:30] But I don't want this exactly at the top.
[56:33] I want to be able to move it a little bit.
[56:35] So I'm going to grab another transform.
[56:37] And I want to move this actually by even just control and click this polypebble.
[56:42] You can see the grid.
[56:44] I want to move it out a little bit and up a little bit.
[56:50] And rather than actually matching size with this grid, I might match size with this transform.
[56:56] Because I had made this a little bit bigger, so it would cover the edges of our pegs we had copied.
[57:03] So this is the line we'll place our spheres on.
[57:14] And to create the number of spheres, I'm going to resample this line.
[57:20] If I toggle my preview here for points, I can see that the length, I even hit D to change my point size.
[57:39] Or rather my point marker size under guides.
[57:43] I can see that this is now visible.
[57:45] The number of segments that I have is going to be the number of points on this line.
[57:51] So I'll set that back to three.
[57:54] Or rather the length between individual points.
[57:57] Maybe I'll put that at one.
[57:59] And what I want to do is grab a sphere.
[58:03] I'll grab a polygon sphere and copy two points.
[58:09] And I'm going to copy this one to the points here.
[58:18] And I'll make that point five.
[58:20] If I uncheck my point preview, you can now see I've got some spheres up there.
[58:27] I've got this set up down here.
[58:30] So the main board.
[58:33] And let's actually line the spheres up.
[58:35] So when they do fall, they'll fall and land on these pegs.
[58:39] So I'll go back to this transform where I moved them out and up.
[58:43] And I'll maybe move it out a little bit less.
[58:52] And perhaps I will place these here so they are aligned with the...
[58:59] Or not above the top of my board.
[59:02] And that's just for me because I think it would look cool if they are placed right above the board.
[59:06] So now I'm going to merge these two together just so I can see what they look like.
[59:10] I can hit shift R to switch the wiring order on that merge.
[59:15] So there's no crossovers.
[59:17] And now I've got these spheres which can fall or will be able to fall in a little bit.
[59:24] And they're placed nice above without intersecting any of the geometry nearby.
[59:30] Alright, that's the first step.
[59:32] And the next one actually what we want to do is I want to be able to create some kind of animation
[59:40] that is going to choose whether or not these spheres are active.
[59:44] And the way we can do that is I'm going to set a color node down here.
[59:50] And I'm going to set this to active.
[59:53] And if I use a wrangle, I can set I at active equals zero.
[60:01] So set active to zero.
[60:09] And now I can use a separate wrangle to set these to one.
[60:12] And again, there's many, many different ways of doing this.
[60:15] So you can use attribute creates, you can use wrangles, you can use Vops.
[60:19] And this is a simple way of working.
[60:22] And hopefully, easy to follow along.
[60:26] So right now, I've got this active attribute of one, and that is set to blue.
[60:30] And if I disable this, it's set to red.
[60:34] But what I want to do now is perhaps we'll only run this on...
[60:45] Rather than actually doing a group, maybe I'll just compare the Z position.
[60:49] So if this active is one, if I say if, and I'll find the Z position of these points,
[60:55] I'll compare that to a float value.
[60:57] And if it's greater than that certain value, I'll set this to one.
[61:01] And then by animating that value, I can essentially start the left
[61:05] and slowly animate these to become active over time.
[61:08] So I'll say if vp.z is greater than my value, set active equals to one.
[61:29] And then the float, my value is going to be chf, so channel float, my value.
[61:39] And I should actually set this perhaps to Z position.
[61:46] And now this is set to zero by default.
[61:49] But you can see the objects that have a Z position that is greater than zero.
[61:54] So on this left side, those are set to blue.
[61:57] And maybe I could set that to green so it's a little bit easier to understand.
[62:01] Which is red is stop and green is go.
[62:03] So now by animating this Z position, I can choose which ones are active and which ones are not.
[62:12] Maybe I'll set this to six.
[62:14] I'll go to frame 24, key frame this at six.
[62:18] Maybe at frame 96, I'll set this to negative six.
[62:22] Or in this case, negative eight.
[62:25] Just to make sure that last one is covered.
[62:27] And now if I click play, these spheres are slowly turning green,
[62:32] which means this active attribute is slowly increasing or slowly toggling from zero to one.
[62:40] And that's going to be one way.
[62:42] So toggle active by line or by position.
[62:50] And the reason we're actually using this active attribute is because that is one we're going to need.
[62:55] Excuse me, a little bit later for the simulation.
[62:57] But in reality, we could name that attribute anything and we could then modify and rename that attribute before we need to simulate.
[63:06] That's one way of setting it up.
[63:08] Another way perhaps we want this to be random.
[63:10] So another way we can set that up will be here.
[63:13] So I can say set active by random.
[63:22] And I'll actually set this active to zero before.
[63:27] And let's do, let's go ahead and do this.
[63:30] So the overall idea of how I'm going to set this up is I want to say set a random number for a point.
[63:40] I'll say fit that number to certain frames.
[63:45] If frame with current frame is greater than fit frames sets to active.
[64:00] So to get a random number, a random float value on these points, I'm going to say F at random,
[64:07] random value equals random and at ptnum.
[64:13] And that just uses the point ID, which is right here on this left side,
[64:17] or rather the point number and sets that as a seed for the random value.
[64:21] And right now this random value is between zero and one, but I might want this between 24 and 96.
[64:30] So I could say F at random value equals fit.
[64:35] And I can use fit zero one because my incoming value I know is between zero and one.
[64:41] And I'll choose the value I want to fit, random value, and I want to fit it between 24 and 96.
[64:57] And it looks like I've got a typo.
[65:00] And here we go.
[65:02] So now I've got a random value between 24 and 96 for all of these.
[65:06] And I'll just compare that to the frame number.
[65:08] So now if the frame number, perhaps that frame 24 is greater than this, then it will become active.
[65:16] So if at frame is greater than F at random value, I at active equals one.
[65:31] And if I connect this to my color and even toggle my copy to points,
[65:37] we'll now see as I play these slowly turn green with a random frame number.
[65:46] And if I wanted to randomize or offset rather the seed on this random PT number,
[65:52] I could say plus CHI, just channel integer seed.
[65:58] And now I can randomize this by just adding a new seed value here.
[66:05] So that's two ways we can define these to active.
[66:08] Maybe I'll grab a switch and we can toggle between those.
[66:16] Say toggle active by random frame value.
[66:28] And we wouldn't actually need to save all these values to this random float.
[66:33] We could have to find those as variables rather than attributes.
[66:36] But for now, this will be a fine way of working.
[66:39] I'm going to switch that here and that can be choose how we get active marbles.
[66:47] All right.
[66:49] And if we wanted more, we could do a transform and duplicate these points.
[67:06] There's plenty of ways we can do that.
[67:08] One thing we would want to be aware of is how we're actually getting this geometry here.
[67:13] So we want to make sure that we'll have a name attribute for later lessons.
[67:18] But we're not going to worry about that for now.
[67:21] And perhaps actually we could extend this one more, one further value.
[67:31] And I'm going to say rather than 2496, I'm going to say CHI min frame and CHI max frame.
[67:48] And the reason I want to do a min and a max and I'm just going to make sure my parentheses are closed.
[67:53] 24 to 96 because I might want to have two of these here.
[68:02] So perhaps there's one that is low and you can actually see in my sketch, I've got two illustrations.
[68:08] And then maybe I have a second value here.
[68:11] And these are maybe one unit above.
[68:17] And I'd merge these together.
[68:26] And if I connect this merge down to the switch and toggle my copied points and actually set the switch to one.
[68:35] So you can see this wire stream is now coming through.
[68:38] We can say in this case, these are being randomly assigned the active attribute at the same time.
[68:46] And the reason for that is both the seed number and the min frame and max frame are the same.
[68:51] If I want the top row to be assigned after I can go here 96 maybe to 96 to 150.
[69:03] And now the top row won't be assigned active until at least frame 96.
[69:08] There we go.
[69:09] And if I want them to happen in a different order, I could change my seed maybe to five.
[69:16] And one thing we might actually be noticing here is it looks like perhaps this nearby point number is happening to be toggled randomly.
[69:32] And it looks like it's nearby at the same time.
[69:34] Sometimes with random numbers, if you are using nearby values, you might get those behavior.
[69:40] So instead of plus, I could even multiply the point number by this seed.
[69:45] So I'll change that here to add a little more of a variation between those values.
[69:58] All right.
[70:00] Now we've got all starting inactive, slowly toggling on to active.
[70:05] And this color itself that is here is purely for visualizing this.
[70:11] So I can move this down here at the end.
[70:13] And I can even move this actually to the side.
[70:15] So it's not connected.
[70:19] So all right, that's going to be almost the end of this video.
[70:23] One thing I want to do before we actually move forward is I want to clean this up just a little bit.
[70:28] So it's a little bit easier to see.
[70:31] So I've got my grid here.
[70:34] I'll name this as main grid.
[70:38] I'm going to connect a null just because I want these split or connected actually before they are split.
[70:46] And on this left side here, we've got my pegs.
[70:51] So I'm going to move this to the side, put that in a network box and name that pegs.
[70:57] And I'll color that dark as well.
[71:00] And actually it looks like on this side here, we've got the rotating boards.
[71:06] So I'll group these together.
[71:07] I'll put that in a network box and name that pegs.
[71:10] This side here, we've got the rotating boards.
[71:14] So I'll group these here.
[71:17] Say this is rotating boards.
[71:30] On this side in the middle, you've got the main board.
[71:35] So I'll group this and say main board.
[71:41] And I'll color this dark as well.
[71:44] And then on the right side, which we actually did not use this sphere here.
[71:51] So I will leave this for now, but we might not be needing this section later.
[72:05] I'm going to say set or create and set spheres active.
[72:15] And these are going to be the marbles that we will be dropping.
[72:19] And rather this is the marble and perhaps actually we could do a switch.
[72:26] Shape to drop.
[72:29] And I will use a cube and a switch and connect to that here.
[72:36] And I'll say this is my shape.
[72:43] So maybe we want to test out with a sphere and with a box as well.
[72:49] So this could be where we're going to be.
[72:51] And we will get into more detail about specific the use cases of some of our simulation setups later once we get there.
[72:59] But for now, I'm not thinking too much about the simulation because I don't want to make this too complex to follow along with.
[73:12] So I've got my pegs here, my rotating boards.
[73:16] My main board and my spheres.
[73:21] And now before I end this video, I'm actually going to do a group to assign each individual one of these a certain group name.
[73:33] And that is because I'm going to merge these together.
[73:36] And we've discussed in the very first video that we might want to have our pegboard on a slant.
[73:41] So in order to rotate that, I'm going to merge them together, rotate those, and then I'm going to split them out to prepare my simulation.
[73:54] So I've got my group.
[73:57] For this one, I will say pegs static.
[74:05] I'll duplicate this again.
[74:07] And I'll say this is boards animated.
[74:14] This will be board.
[74:21] I'll name that actually board static.
[74:24] And this will be marbles.
[74:30] And now when they're merged together, I've got my four groups.
[74:33] I can transform and then I could split those back out here and grab my board static, for example.
[74:48] And actually rather than split, perhaps we could do a blast.
[74:52] But I'll save this for later.
[74:55] And I'll say this no right here is all my board static.
[75:04] Objects.
[75:08] And one more thing to note, perhaps for these spheres, we will extend the top of this just a little bit more.
[75:16] So that could be done right here.
[75:22] Actually, if I extend it on this transform and template this,
[75:27] I'm going to move this down just a little bit less.
[75:34] I'll set this to negative maybe one.
[75:41] And now it is right along, so it should fall and not go off the edge.
[75:46] So alright, that'll be the end of this video and back in the next one to continue.


### Lesson 06: Houdini - SOP Level Simulation Workflow [75:55]
**Transcript (timestamped):**
[75:56] Welcome back and welcome to the next episode of this Houdini mini course.
[76:02] In this video, what we're going to do is we're going to take the results of our last setup, which is actually the pegboard.
[76:08] We've got our animated planks and we've got these spheres, which we are now going to set up for a simulation.
[76:15] So there's quite a few ways we can go about setting this up.
[76:19] But what we're going to do actually first is we're going to set this up to be a simulation we'll solve with the top level solver.
[76:28] And we'll also set this up for the top level solver.
[76:31] So we're going to go and create a few attributes and re set some of this geometry.
[76:46] But actually what we could do is we have grouped these all.
[76:53] So rather than setting that up within this network, perhaps we'll split those out and set those up down here in our simulation.
[77:01] So I'm going to cut this for now, this wire, and I'll move those to the side.
[77:06] And what I want to do is I'll grab one more null, put that down here just so it's within this box.
[77:21] And let's split these out to get these same exact four geometry streams that we had here.
[77:29] So one, two, three and four.
[77:32] And you could also set that up within this network here, but to keep this a little bit more organized of creating our setup and then preparing the simulation,
[77:41] I think it's going to be nice if we have that down here.
[77:44] So to do this, I'm going to do blast.
[77:47] And I'm going to delete.
[77:49] First, I'll keep the board static.
[77:51] So delete non selected.
[77:57] Then let's do the board animated.
[78:02] Then let's grab the marbles.
[78:12] And let's grab the last one, which was the pegs static.
[78:16] So for this, I'm going to group the static objects here on the left.
[78:23] And these, this is animated.
[78:25] And technically, actually this would be deforming, but we will, we'll get to that when we get there.
[78:39] And I might actually change this a little bit because there's one caveat of our simulation.
[78:44] That's going to be a little bit interesting to have with these cubes or with these grids.
[78:48] So board static, what I want to do now is we need to create a name attribute for our geometry.
[78:52] And if you are not familiar with RBD, I recommend you go check out the intro to RBD video that I've got on my channel.
[79:01] I'm going to actually assume that you have a watched that if you are following along here.
[79:07] So I'm going to do a assemble rather actually I'm going to do a pack to create my path to geometry.
[79:16] And then I'll do a name to create the name.
[79:21] So I can create this on the primitives, which will be board static.
[79:28] And I want to pack this and then I want to transfer this attribute of name, but I want to make sure this is a point attribute.
[79:36] So I'm going to do an attribute promote to go from primitive name to point.
[79:41] And this is my little setup for RBD prep.
[79:46] So our name attribute on the points with the path to geometry is what I want here.
[79:52] And this is the static.
[79:55] Ex static also please excuse my dog barking in the background.
[80:00] What I want to do here now is actually for each of these, I want to create a unique name attribute.
[80:05] And it's quite a few different ways I could do that.
[80:08] I could use a connectivity.
[80:09] I could use a for each loop, but one easy way we could also do that is assemble.
[80:14] And if we use assemble right now and select create packed primitives and create name attribute.
[80:21] I can set my prefix rather than piece to be peg underscore.
[80:27] And now you'll actually see I've got 107 individuals.
[80:31] And now you'll actually see I've got 107 individual packed primitives rather packed fragments, which is fine for now.
[80:40] We do mention this a little bit in the RBD section, but for our purposes, these are equivalent.
[80:45] And now this is already created the individual name attribute unique per object.
[80:51] And this actually uses the connectivity of the objects to do so.
[80:55] And it has now assigned those a unique name.
[80:57] So that is essentially doing the exact same thing that I've done here.
[81:04] So this will be create name and pack.
[81:13] And we'll need to do the same thing as well here.
[81:15] So I will use an assemble.
[81:18] Actually, rather than this, if I just packed this as is actually delete this again, I would need to set this.
[81:27] This object to deforming.
[81:29] And I don't want to have to use deforming.
[81:31] I'd rather be able to use animated for a RBD attribute.
[81:35] So I'm going to make sure I can do that.
[81:37] And the way to fix that is I need to actually pack the geometry before I animate it.
[81:46] So I'm going to go back to find where my board was made, which is the rotating board right here.
[81:51] And this rotate is the animation here.
[81:54] Whoops, I just want these two nulls and I'll color those green.
[82:00] So I'm going to add another null here just to connect those.
[82:04] And I will actually pack this geometry here.
[82:11] And rather than using a pack, I will use an assemble because that's going to create the name attribute.
[82:16] So right now these two are doing the equivalent things.
[82:18] It's creating a name attribute, packing it and promoting that to points.
[82:23] So I'll use assemble and this will be board underscore create pack primitives create name attribute.
[82:32] And here we go.
[82:34] And now one thing to note is when these do get merged, they will all have the same name attribute,
[82:39] which is fine because I will fix that down here.
[82:45] And the way I'm going to fix that is I'm going to use a wrangle just to add a point number to the end of this name attribute.
[82:52] So I'm going to say update to unique name.
[83:01] So the way I'm going to set this up is I'm going to say asset name and we're running over points.
[83:07] Because this is the packed object and our name is on the points here.
[83:11] And this is the string notation for getting my attribute.
[83:14] I want to say asset name equals asset name plus and I'm going to add an integer based on the point number.
[83:22] So ito a is the integer to string at pt num.
[83:29] And now here we go.
[83:30] I've got board zero zero board zero one and board zero two.
[83:35] And now these will be unique per name attribute and they will work fine in my simulation.
[83:43] And one more thing we're actually going to need on this one is we're going to need a animated attribute.
[83:52] So set animated and that would be I at animated equals one.
[83:58] And for some of this stuff, we can also use the RBD configure node.
[84:03] Whoops.
[84:05] RBD configure and this might actually be helpful to use because in addition to setting the animated or the active attributes will also be able to set some density and then some bounce for the individual objects here.
[84:22] So maybe I will delete that and I will use the RBD configure actually rather than delete.
[84:31] I'm going to use a switch.
[84:35] So set animated.
[84:39] And I don't want this to be connected here.
[84:42] I just want this to be on the left side.
[84:44] This is the constraints and this node can do quite a lot.
[84:47] So we're not going to go in depth at all really on what this does.
[84:52] But for now, I just want to set active to zero and animated to one.
[85:01] So set animated.
[85:03] And here we go.
[85:06] And you'll actually see if I have the RBD configure set, you'll see a few more parameters such as density and bounce.
[85:11] And those are not set if I use the wrangle because I had not set those manually.
[85:17] This will be fine for now.
[85:19] And now for the marbles, we need to do two things.
[85:22] We need to get our packed geometry because right now this is unpacked.
[85:26] And then we also need to make sure our animated attribute is correctly rather our active attribute is correctly set on these points.
[85:35] So I might go here to copy the points and another way we could do, I did show you how to assemble and then copy the points.
[85:43] We can also create our packed geometry directly on this node with a pack and instance.
[85:50] And now if I'm middle mouse, we'll see 26 packed geometries and they are now individual points.
[86:00] So pack an instance.
[86:02] This is the same way as making sure we had packed the geometry before we had copied it.
[86:11] So we'll actually use this way and then do something similar with our attributes.
[86:16] One thing I do want to make sure is we have the color and the active attribute.
[86:24] It looks like it already is transferring.
[86:31] So that is one thing to be aware of depending on how you set it up.
[86:35] So if we had packed this before and done a different setup, we might not have had those attributes coming through.
[86:41] But we do want to make sure we've got our active and our animated.
[86:45] Our active.
[86:47] Don't actually need animated, but we will need active.
[86:52] And now we do not have a name attribute.
[86:54] So let's create one of those.
[86:56] We could use a few different ways actually, but because we already have our geometry packed, let's just use a wrangle to set that up.
[87:06] Set name.
[87:09] Attribute s at name equals.
[87:13] We'll say marble underscore underscore or marble underscore plus it o a at pt num.
[87:24] And now we'll have 26 unique marble names.
[87:30] And it is a point attribute.
[87:32] And the reason we're setting this as a point attribute is because we're already operating on our packed geometry.
[87:37] So again, if you do want some more info on RBD, take a look at the RBD section.
[87:42] And actually within level up Houdini, there is a ton more on RBD.
[87:48] So that'll be all we need for now.
[87:51] We've got our name attribute on this geometry here, board static.
[87:56] We've got our name attribute on this pegs static and those are packed.
[88:02] We've got the active attribute set to zero and the animated attribute set to one.
[88:08] And more importantly, we have done the animation after we had already packed this geometry.
[88:14] So pack and name.
[88:18] We've also packed geometry with a manual pack with an assemble and with a copy of points.
[88:25] So we've created our geometry packed and our name attributes in three different ways.
[88:32] And we've got that here on our attribute as well, which we can see is active.
[88:42] And it's changing from zero to one and our color is nicely representing that as well.
[88:49] So this is actually all we need for our simulation.
[88:53] And the way we get this to work is we merge these all.
[89:01] And hit shift F or shift S excuse me to change my network wiring and we'll grab a RBD bullet solver.
[89:10] Plug this into, we'll go back to actually frame one, plug this into the start, select our solver.
[89:19] And if we click play, fingers crossed, it will work as expected.
[89:26] And there we go.
[89:30] And one thing you'll actually notice is our spheres are falling off of our little bit, maybe not that much,
[89:40] but two of them are bouncing past here and perhaps we'll leave that for now.
[89:45] But we could create another grid in front and have that only be a collision if we did want to do so.
[89:59] And actually, perhaps we will set that up.
[90:02] So the way I'm going to set that up actually is I can do that right here.
[90:08] And rather than actually doing that here, maybe it would make more sense to do that before I transform.
[90:18] So I will grab the main board, which is right here, board static before I name it.
[90:33] I'm going to transform and the distance that I'll transform it.
[90:43] Looks like I might have accidentally rotated this board, which I did.
[90:48] So I'm going to set this, actually, no, maybe I didn't hit space two to go to the side profile and space one to switch back to perspective.
[91:00] And this looks correct.
[91:02] But now what I'll do is transform this and the amount I want to transform it by is going to be the width of this peg.
[91:11] And perhaps an easier way to do that would be to do it down here.
[91:15] So I can blast the board static, delete non-selecting.
[91:23] I'm going to do a match size with the merge.
[91:30] And if I template this merge, I can see and I want the X axis.
[91:35] I want the min to the max.
[91:40] So the minimum value of this board's X axis is going to be matched to the maximum value of this merge, which in our case is this side of these pillars here.
[91:54] And then I'll do a group.
[92:00] And rather than this being in my board static, I'm going to say this is board glass cover.
[92:15] And perhaps I'll add a color just to see what this looks like in my scene view.
[92:23] And then I'm going to merge this back in and move this down.
[92:27] So this is add the glass and I'll color that blue.
[92:36] Here we go.
[92:37] And now right now I'm not actually keeping that in my simulation.
[92:43] It looks like I am because this must be in both of the groups.
[92:51] So I'll just do a group delete on this geometry here.
[92:58] And I'll actually delete all of these groups because I delete the groups.
[93:03] And then in this case, I'm actually recreating it.
[93:10] And I do actually notice one quick mistake.
[93:13] I don't want this to be the group name.
[93:15] I want this to be the base group.
[93:25] And I can't actually delete the board static.
[93:28] So I will, well, I can't delete the groups before I delete that.
[93:34] So I'll put this after the match size.
[93:39] And that will group this to board static.
[93:44] And now I should have...
[93:56] It's like I actually did have that set in the correct spot.
[94:00] So I do apologize for that mishap and I will actually leave that in the video.
[94:04] So sometimes even I get confused as I'm trying to think about a lot of things at once.
[94:09] So I apologize for that.
[94:10] All right.
[94:11] So my board static here.
[94:13] This is everything set up, but now I do not have that glass.
[94:16] So to get the glass, I will duplicate this.
[94:22] Let's find board glass cover.
[94:27] And I could actually create an assemble perhaps for this way.
[94:32] So create assemble, name it, and I'll name this glass.
[94:37] I've got my name attribute, my point glass here.
[94:41] And I do need some more attributes for this.
[94:45] So actually in this case, better practice would have been to set these attributes myself.
[94:51] So I should have set some attributes for my solver, but it looks like on these, it must be setting them by default for me.
[95:06] So actually I should be setting RBD configures on all of these.
[95:12] So these are my spheres actually rather than doing the RBD configure here.
[95:17] I will not set that.
[95:23] I will do an RBD configure because I do want to set on these pegs.
[95:32] I want them not to be active.
[95:36] So they will not be affected by the simulation or rather they will be, but they won't be able to receive forces.
[95:42] The board's static.
[95:45] I will leave that also active of zero.
[95:48] And for this glass as well, I'll leave that active of zero connect this.
[95:54] And I'm going to fix these wirings so there's no crossovers.
[96:03] And now if I go to my bullets over reset the simulation and go back to the first frame, we should see these balls are falling through.
[96:16] And they are working as expected.
[96:18] And it looks like here we go.
[96:20] We do see it bounces against the side here and is working as correct as I would be expecting.
[96:29] All right, welcome back.
[96:31] Apologies for that quick cut.
[96:32] We're going to continue from where we left off.
[96:34] And what we've got here is if I click play, we'll see our simulation is working still as expected.
[96:40] But I might want to remove this front panel just so we can see the rest of our simulation.
[96:45] I'm going to create a null and put that on the left side here.
[96:49] And we can now see we've got all our objects.
[96:52] But if I wanted to blast the glass cover, we'll actually see I am not able to do that.
[97:00] And that is now because we've packed our geometry and we have not transferred that group inside.
[97:06] So the information of that object is actually within our packed geometry.
[97:11] So I'm going to go to transfer attributes, actually rather transfer groups.
[97:16] And I want to transfer my board glass cover.
[97:19] And now it looks like that worked.
[97:24] I was expecting to have to reset the simulation, but it looks like perhaps these active attributes are being transferred through without having to re cook the simulation.
[97:34] So how we typically do workflows in RBD, I won't go too far into detail now is we wouldn't be able to do that.
[97:40] We wouldn't be running these all through a simulation.
[97:44] We'll be bringing in objects, simulating them and then copying the transforms of the original objects onto the simulated points from our actual simulation.
[97:56] So hopefully that made a little bit of sense.
[97:58] Again, check out the RBD section.
[98:01] Excuse me if that doesn't.
[98:03] But if I hit D and leave my point marker size or my simulation, here we go.
[98:18] My points a little bit smaller to two.
[98:20] You'll see that these are just individual points of my incoming objects.
[98:26] And these just represent the transforms.
[98:29] So the locations and the rotations of each individual piece and how it would work normally is I would do a transform pieces.
[98:40] Template points in the geometry I would want to transform would be incoming.
[98:46] And we now get this set up here.
[98:51] So with heavy simulations, you don't want to have to cash out the points for every object.
[98:57] So what we could even actually do is quickly set up the cash and I will do that in this video.
[99:09] So I want to set up a file cash and I'm only going to cash the points for the spheres.
[99:17] And then I'll copy the spheres back onto those original points.
[99:22] So file cash.
[99:24] I'm going to plug this into simulation points.
[99:27] This is going to be sim points marbles.
[99:31] I'll leave it on time dependent.
[99:33] I'll set this to simulation frame range.
[99:36] I'll do hip slash sim.
[99:43] And before I actually cash, I do want to only keep...
[100:08] Well, maybe I'll cash those all.
[100:12] Because I could delete these and only keep the marbles.
[100:16] So I could say at name equals marble.
[100:27] Delete non-selected on points.
[100:30] And now I'm only keeping the marbles.
[100:34] In which case if I did this, that would probably be the lightest file cash I could have.
[100:41] But we also have our boards animated, but they're not simulated.
[100:50] So this would actually be a fine way to do it.
[100:53] So I'll go sim points marbles and you could either cash all of these or sim and then delete them after.
[101:01] I will save to disk.
[101:05] So I'll delete them first and only keep the marbles and then I will delete everything else after.
[101:10] And now what we would do is we'd go back to the marbles here.
[101:15] And we would find the sim geometry coming in, which is this set up right here.
[101:21] And we would want to first time shift.
[101:27] And we need to transform pieces.
[101:30] So if I plug this straight in, it's a little to the left and I'll delete this null for now.
[101:39] I'll say this is marbles.
[101:41] I'll rename this to incoming or marbles to sim.
[101:49] And then this here would be the geometry I want to transform.
[101:52] So geometry transform.
[101:54] This is the template points.
[101:56] And if I click play, you'll see we've got our simulation.
[102:03] And typically we would actually want to time shift and freeze the incoming simulation.
[102:10] So we go to delete channel one.
[102:14] That will all have those be read because they're not active currently.
[102:19] And now we've got this simulation of them all falling and this would be the more correct workflow.
[102:26] But in this case, we wouldn't actually have the color changing.
[102:29] So because these are not moving in location, I can do this as well.
[102:34] Or what I could do is leave this on time shift and then copy back the color and actually rather just the color attribute,
[102:41] maybe even the active attribute so I could use that in shading and transform that back.
[102:46] But for now, I'll be okay.
[102:50] And I'll actually put a little note.
[102:56] Freeze the position.
[103:04] And this would be my animated marbles.
[103:11] So here we go.
[103:18] And then on this case, I wouldn't even actually need to have this through the simulation.
[103:24] So if I wanted to, I could, I'll leave those here.
[103:30] Actually, I want to leave those.
[103:31] I could just grab the geometry that I know is not being animated by the simulation.
[103:41] So I could grab this all.
[103:43] Maybe I don't want my glass panel.
[103:47] And I could merge this again down here to see my final simulation.
[103:58] So this is typically how a workflow might work.
[104:01] You would only be caching the actual simulated objects where whose position is being changed by the simulation.
[104:09] And then you'd be re-transforming the positions of the original objects onto these here.
[104:16] And actually in a more robust workflow, we would be using the proxy geometry as a simulation.
[104:23] And one interesting thing about this SOP level tool is we should be able to just plug this straight into proxy.
[104:33] And it looks like it does not like that.
[104:40] So in this case, we could actually plug those into both.
[104:44] But you technically do not need a high resolution geometry.
[104:49] You could simulate with the low resolution, only run that through a solver, and then copy back high resolution after.
[104:57] So we've got our sim working fine here, our object.
[105:05] And everything looks as correct. Looks good.
[105:11] We can actually see hopefully they are not bouncing past because we do have that glass.
[105:18] Here we go.
[105:19] This sphere looks like it was about to go through the wall.
[105:24] But then bounces against the glass, which I had not merged back here, but which is out coming in the simulation.
[105:34] So there we go.
[105:40] All right, I'm going to cut this to make it a little bit cleaner.
[105:50] And another thing we could actually do is we don't need these active attributes for our post or for our simulation.
[105:58] Or excuse me, we don't need these to preview it after the simulation.
[106:03] So I could just grab all my objects, object merge, put that here.
[106:11] So this is now fetching this null up here.
[106:15] And then I could actually blast this from right here.
[106:21] And now this, our shift R to switch those around.
[106:27] This down here is technically all I might need to have this simulation.
[106:37] So awesome. I'll do one quick flip book preview of what we've got here.
[106:48] And then I'll do a little bit more organization to make sure we keep this nice and clean.
[106:57] Actually, it looks like, before I call this a finished flip book, it looks like when we merge,
[107:06] we're merging back in our spheres as well.
[107:09] We can see those spheres, but we also have the spheres on this side.
[107:12] So in addition to deleting the board glass cover, I'd actually want to delete my marbles as well,
[107:18] because those are being merged in on this side here.
[107:22] And I'll do a new flip book.
[107:38] I'll let this one finish out.
[107:41] And then we'll do a little bit more organization.
[107:47] There we go.
[107:50] All right.
[107:53] I'll end that flip book and then let's just reorganize a little bit more.
[107:56] I'm going to hit C to hide that color panel.
[108:01] This will be fine for that.
[108:03] We could time shift.
[108:05] One thing to be aware of is if these were animated before,
[108:08] just say we wanted to randomize the starting position.
[108:11] And we did some kind of attribute noise vector to the position.
[108:20] And we animated that.
[108:22] So they were kind of jittering before they entered our simulation.
[108:25] If we then had this animated object and we transform pieces again,
[108:30] we'll notice that our pieces as they're falling are then getting a second transform applied from this animation incoming.
[108:39] So in this case, we want to have those time shifted.
[108:47] Or excuse me.
[108:59] But we don't want to have this happen.
[109:01] So if we were going to do this, what we would need to have happen is we would need to have this time shifted,
[109:07] but then we'd have to resim our setup here.
[109:10] So I'm going to delete this.
[109:13] We're going to leave this with the objects starting still.
[109:21] And then they start to fall.
[109:26] And I can even uncheck that time shift.
[109:29] It should be good to go.
[109:31] So I'll delete this null.
[109:34] Actually, I'll leave it here and I'll say preview my sim.
[109:39] This is delete everything.
[109:42] Or actually, I'll just say keep marbles.
[109:45] This is caching the marbles.
[109:47] So this is get back objects.
[109:51] And we wouldn't maybe be not merging these together because when we bring these into Solaris to render,
[109:58] we're not going to want to have them all together.
[110:00] And we could, but in our case, it might be a little bit easier to not have them all in one object.
[110:08] This will be preview our sim.
[110:21] And then let's do and we'll call this stop level solver.
[110:29] I'll call it this dark.
[110:34] And I'm actually going to name these before we end this video just for organization.
[110:40] So this is to sim.
[110:47] I'll say glass.
[110:50] And this is stuff I want to have involved in the simulation.
[110:54] So this will be to sim back board.
[111:01] This will be to sim static pegs.
[111:07] And I could drag this if I wanted to connect to this here.
[111:12] I'll do one more here.
[111:13] It'll be to sim animated boards.
[111:18] And I'll do one more.
[111:22] I'll actually use this marbles to sim.
[111:26] And I'll rename this to two sim marbles.
[111:33] So these I shift S to preview or change my wiring.
[111:37] These five nodes.
[111:39] I might color red are the ones that would be involved in my simulation.
[111:44] So that's going to be the end of this video.
[111:49] We've got our setup here in the next video.
[111:52] We are actually going to set up the same simulation, but instead of the stop level solver, we are going to be using the dot net solver.
[112:01] And we're going to create our own dot network from scratch.
[112:04] So it's going to be a lot of fun and we'll be back in the next video to do so.


### Lesson 07: Houdini - DOP Net From Scratch Simulation Workflow [112:11]
**Transcript (timestamped):**
[112:12] Welcome back and welcome to the next video in this Houdini mini course.
[112:17] In this shot or in this video, excuse me, we are going to recreate our simulation.
[112:23] We've got set up here, but rather than using the stop level solver we had done in the last video, we're actually going to create our own dot network from scratch.
[112:34] And I'm going to show you how to set that up for this case here.
[112:39] So the workflows choices that you choose to make, whether you use the stop solver here or the dot solver I'm about to show you.
[112:46] It is entirely up to you.
[112:48] My personal choice is I actually kind of prefer the dot solver for even the simple things because it's a little bit enjoyable for me to set up.
[112:57] And it's a little bit easier to control some of the more complex simulations rather than having to work with this one.
[113:04] You can kind of custom build it based on what your exact needs are.
[113:10] So to do this, we're going to grab a dot network, which is going to be our marble simulation.
[113:19] We're going to need to create a few things inside here.
[113:22] But before we do, I actually want to get a dot import.
[113:27] And I'm going to grab this one, drag that into dot networks.
[113:31] And I'm going to grab objects.
[113:33] I'm going to say marbles.
[113:37] So I'm going to say fetch my marbles.
[113:41] And I'm going to say create points to represent objects.
[113:45] And I'll do a file cache.
[113:48] This will be my dot net marble sim.
[113:54] I go to frame range, leave time dependent cache, but I will set this to sim and I'll check that for simulation.
[114:01] So there's really no correct way.
[114:06] There's quite a few ways to set up simulations and it's kind of up to the artist and up to the shot in specific.
[114:12] But what we can have, and we actually will not be covering the fundamentals of dots or a little bit more about objects and data within dots.
[114:21] If you're interested in learning more simulations, I'd recommend checking out level up Houdini.
[114:26] And we've got tons of information within there and many different projects actually for setting up simple to complex simulations.
[114:34] So inside my dot solver, my dot net, I'm going to need a few things.
[114:38] I'm going to want a gravity force to pull these objects down.
[114:42] I want a RBD packed object.
[114:48] And I want a RBD, actually a rigid body solver.
[114:56] I'll connect these here.
[115:00] This will be, and we could actually do this, the two kind of overall ideas for RBD.
[115:06] You can put everything within a single packed object or we could have one for marbles and one for the board.
[115:15] That is really up to us.
[115:17] It might even be easier to, well, we'll split two different objects here.
[115:27] We'll have one for, we'll say board.
[115:30] Actually, we will do one for marbles.
[115:33] And I'll do another one for board.
[115:36] I'm going to merge these two together.
[115:41] All right, I'll even say not marbles.
[115:47] And now what I want to have is I'll go back first to get just a single piece.
[115:55] So I'm going to grab another merge node because I want to connect all of these before I bring them into my simulation.
[116:04] I'm going to say this is two SIM below.
[116:14] So right now, if I copy this, I can jump inside.
[116:17] I would put this in not marbles, paste my soft path, hit U to go up, and then let me grab my marbles.
[116:24] So copy this, jump inside, paste the soft path.
[116:28] And one thing to be aware of the create active objects, static objects, and all of these other ones, you can either set them here or you can override them with attributes before.
[116:39] But we've set them already on the incoming geometry here.
[116:43] So we're not going to be bothering in changing these here.
[116:46] Now, if I click play, you'll actually notice nothing's happening.
[116:50] And that reason is these marbles are not going to be set animated or active until I check the overwrite active attribute here, which is going to let those now this change of my active attribute to be brought into the simulation on each frame.
[117:07] So now if I click play, whoops, not on the not marbles.
[117:16] That is fine set here.
[117:17] I want to set those on the marbles themselves.
[117:20] So overwrite active.
[117:21] And now if I click play, we'll actually see these are falling down, which is exactly what I wanted.
[117:31] And I could even do the CD here to overwrite that color attribute.
[117:38] But I shouldn't be doing that in the SIM or I could actually, but I could also transfer that back out after my sim has been completed.
[117:46] But even for now, I'll leave that checked so we can preview that within our simulation.
[117:52] And then what I could do is connect everything else to the two sim below.
[118:00] Just all these here and we can even see my objects rotating.
[118:06] And now if I go back and jump inside here and go to my wireframe, we should see everything is working as expected because I had already set up all my packed geometry.
[118:18] I had already set up all my animated attributes, all my active attributes.
[118:22] And in this case, no deforming because I had packed the geometry of these boards before I had animated them.
[118:31] So that's really all we need for this entire simulation.
[118:34] Hit U to go up.
[118:36] I can see which points I've now brought in and this is the marbles right here.
[118:44] And that's just this object right now.
[118:47] If I did want to get these other ones, I could grab the not marbles, which might be create points to represent object.
[118:59] I could get the whole geometry or what we could do in the last video is the same workflow that you typically would use when doing RBD.
[119:09] And you only cash the geometry you need.
[119:12] So let me save this here or rather you only cash the location of these points that are being transformed by the simulation.
[119:24] And then I could even grab, I'll do an object merge to grab this null right here.
[119:35] So grab my marbles.
[119:41] I've got those here and I'll use the transform pieces to connect this here.
[119:49] And there we go.
[119:52] And now I could actually connect this to the get back objects, which is a reference to this all my objects.
[120:02] But since this is a new video, I'll grab that null again, just in case you're not watching this one here, or rather not watching the.
[120:13] I suppose actually we set this all up in the last video.
[120:17] So this is maybe a bonus video to see the Dopp setup for the same simulation, because you would have had to follow along with all of these simulation preps, whether you choose to use the stop solver or the Dopp solver.
[120:32] I'm going to grab object merge, grab all my objects.
[120:38] And here, let's delete these fears.
[120:42] I'm going to blast the animated or excuse me.
[120:51] I want to blast the marbles and the glass cover because the marbles I'm bringing in from here.
[120:59] Then I'll merge this together, connect these two.
[121:03] And I did mention in the last video that typically we would want to time freeze this geometry here before we copy it with the transform pieces.
[121:13] Otherwise, we might accidentally get duplicate transforms.
[121:16] But in our case, it'll be okay because these are static.
[121:19] And I do want to have the colors still changing.
[121:24] So a better workflow perhaps would be to time freeze it and then transfer that attribute back.
[121:29] But for our case, this is plenty fine to do.
[121:38] And we've got our simulation.
[121:42] And one interesting thing we could actually do.
[121:46] So please excuse my dog barking in the background.
[121:49] We could actually do a quick test of this simulation run through the Dopp solver or the Dopp that we made.
[122:01] And see if they look the same.
[122:08] They may be very similar.
[122:10] They may be slightly different because default values on the objects themselves.
[122:29] If I try to get them to line up at least a little bit.
[122:40] You can even look at maybe frame 200 and see how they compare.
[122:45] And it looks like they are not the same.
[122:54] I'm going to do one quick check because it looks like we're getting a little bit of interesting behavior at frame 193.
[123:09] And that actually looks fine from this camera angle.
[123:12] You can see our ball is just rolling off nicely.
[123:18] And there we go.
[123:21] I'm going to do another network box here.
[123:25] We'll say this is our Dopp solver color this dark.
[123:34] And now in addition to setting this up, what we could have actually done is if I do a duplicate here, perhaps go back.
[123:45] I can say this is RBD.
[123:48] I'm going to put everything in one object so our sim and our network is even a lot cleaner.
[123:57] And then in order for this one, it would be two sim marbles, which was this one.
[124:05] So maybe I'll do another null.
[124:08] That'll be two sim all.
[124:12] And I'll use another merge to connect this one as well as that one.
[124:20] But I'll actually grab an object merge just so I'm not having a ton of network wires crossing over each other.
[124:28] So object merge will grab two sim marbles connected here and here.
[124:36] Plug it in.
[124:37] We will get a warning bounce density and animated.
[124:42] In our case, we should be fine.
[124:45] This is because some of these have different attributes that we had set, but hadn't set on them all.
[124:51] So for these marbles, for example, we hadn't set any of the density or bounce factors.
[124:59] So if I did want to set those.
[125:02] Oops.
[125:04] RBD configure object.
[125:10] RBD configure right here.
[125:12] I could set the density and the bounce here.
[125:14] And I would encourage you actually to mess around with those and see what they get because you will actually get different results for your simulation.
[125:22] But to sim all.
[125:27] And now inside.
[125:30] Say option two.
[125:32] I'll jump inside here.
[125:34] Skip back to the start.
[125:36] And for this object, I'm going to place or rather paste this null, which is going to bring everything in.
[125:42] If I click play, this should work the exact same.
[125:47] And it does because we had already set up all of the active objects, all of the static objects and all of the animated objects ourselves with the attributes we created up here.
[126:02] So if we leave this here, our attributes are going to override those.
[126:06] And this active animated deforming in CD.
[126:08] In our case, they're only changing for these spheres.
[126:14] But if we did want to, we could even make these individual pegs active at random times.
[126:20] So those collapsed down as well.
[126:23] And that might be a little side challenge for you to try, but I'm not going to show you how to set that up.
[126:28] At least not in this video.
[126:31] So two setups here for our simulation.
[126:39] All right, looks like we got a crash.
[126:42] So I'm going to end the video and hopefully come back without any loss of data.
[126:47] We just got back without any data loss from that crash.
[126:51] So we are set and we're just going to keep working.
[126:54] What we were just mentioning is that we could have extended the simulation to have now our tubes in these pegs become active.
[127:03] We could create constraints to bind those to the pegs or to the board.
[127:07] And then when the balls hit with a certain force that might break those constraints, maybe they actually snap off.
[127:14] And this slowly becomes some type of destruction simulation.
[127:18] If we want to get a little extra crazy, we could even fracture and break some of these.
[127:23] So once our balls did release some of these pegs, maybe there's splinters of wood that falls down and is involved in our simulation as well.
[127:32] So these dot net simulations and these dot networks that we created from scratch, in my opinion, are a little bit easier to expand.
[127:42] So these two different approaches here, whether we use one RBD object or two or even extend multiple ones.
[127:49] This is a little bit easier to build out and create some of this customization.
[127:55] The SOP level solver does get a little bit clunky, in my opinion, if you wanted to make this a lot more of a complex simulation.
[128:05] But for now, we're not going to go crazy there.
[128:08] If you do want some of those more exciting simulations, I do recommend you check up level up Houdini, in which case we do quite a bit of work there.
[128:18] So I believe that might be the end of our lesson for setting up the simulation for both the SOP solver as well as our dot network.
[128:42] I'm just thinking one more time, if there's anything else we should cover here.
[128:54] I think that might actually be good.
[128:56] So I'll end this video and then in the next one we'll come back and perhaps you can get this set up for our first render within Solaris.
[129:05] So I'll see you then in this next video.


### Lesson 08: Houdini - Simulation Prep to Solaris [129:12]
**Transcript (timestamped):**
[129:12] Welcome back and welcome to the next section in our Houdini mini course.
[129:17] In this video, if you're just joining us, I recommend you download the project files and then actually follow along from the last video.
[129:26] We've just completed our simulation.
[129:28] We finished our simulation prep and we actually set up a SOP level solver.
[129:34] So the SOP level workflow for creating this little pegboard simulation.
[129:39] And we did a dot level.
[129:41] Actually we did two, rather not dot level, two dot net simulations or two dot networks that we created for our simulations from scratch.
[129:51] So we've got three essentially different ways we can approach the simulation and there's many reasons why we might choose one of them.
[129:58] But the biggest one is really your personal preference.
[130:02] So you're welcome to choose whichever simulation technique and whichever organization technique you feel most comfortable with.
[130:10] So in this video, we're actually going to bring this into Solaris and start our first lighting and perhaps our first maybe camera look for what this is looking like.
[130:23] So very first thing I want to do is decide how I'm going to bring these in.
[130:30] So I'm going to go back up and see my LOP network, which we had created quite a few videos ago.
[130:37] And we can see I have a pegboard static, pegboard animated, and then marbles as well.
[130:45] And because this is the organization I had set up earlier in this course, we will actually will choose to stick with that.
[130:56] So I'm going to go back and perhaps I'll merge my marbles separately.
[131:07] So I'm going to grab one more graph branches, connect that here and grab this primitive right now.
[131:15] This is my root primitive I'm going to grab so everything from this right side and I'm going to put that on marbles.
[131:22] And now nothing is actually within these. Well, there are no's, but if we jumped to where they were, we had thus previously disconnected these from our setup.
[131:33] So these are the old ones we had used. I will actually leave these here for now, but we did modify it quite a bit once we were setting up the rest of our simulation.
[131:41] So what we first want to get is we're going to grab our animated marbles.
[131:48] And I might stick with the SOP solver for now and this approach we had here because I think this is the more artist friendly approach, perhaps, especially if some of you are just getting into rigid body dynamics and RBD.
[132:03] So we'll stick with this one and this will be the bonus side quest that if you'd like to work off of, that'd be a great challenge to try to do so.
[132:12] But essentially what we're going to be doing from now is pretty much identical for either of those approaches.
[132:18] So this is my animated marbles.
[132:32] And what I could actually do is just bring these straight into Solaris.
[132:37] So I'm going to say out to render marbles. Control C to copy that.
[132:46] I'm going to hit U, jump into my render scene, paste this and I will grab the relative path.
[132:55] And here we go.
[133:01] Looks like we've got a nice collision there between some of our objects, which is going to be pretty cool.
[133:06] So that'll be the first thing. One thing we will actually notice is that our color is gone.
[133:10] In our case, we're not going to worry about that because we're actually going to be setting up color in a different way.
[133:18] And we actually won't be going too far really at all into USD.
[133:23] As you work with RBD, USD and Solaris does get a little bit more intricate.
[133:29] So we're not going to be covering those for now.
[133:32] But if you do have any questions, let me know in the comments and I can help out.
[133:36] So we've got our marbles here. Excuse me.
[133:39] We're going to grab our pegboard animated and our pegboard static.
[133:52] So I'm going to say outs to render pegboard and we could actually grab this all if we really wanted to split.
[134:03] And perhaps we will. I might say animated, which was the group we had created earlier.
[134:13] Out to render pegboard animated.
[134:19] And I'll duplicate, delete, non selected or uncheck that. So now we're keeping and this will be static.
[134:29] I'm going to copy this.
[134:33] Go back and jump inside my render setup.
[134:38] And for static, I will paste the static export relative path.
[134:43] And for animated, I will actually go back to SOPs to copy that null individually.
[134:52] So right now out to render pegboard animated copy this.
[134:57] Go back and paste that null and I'll set this as a relative path.
[135:07] And another fine way of working would have actually been like a back all the way to set up pegboard.
[135:15] It would have been fine to have one connected directly here.
[135:20] So pegboard all, which is now my animated.
[135:31] And if we were saving out this to USD from Solaris, so right now we've got animated.
[135:37] And because this is a very light scene with just some object rotations, we're not slowing down Solaris.
[135:43] But if we had animated geometry with really heavy files or RBD, typically we would need to be a little bit more intentional with how we're setting up our Solaris scene.
[135:54] But for now, we are going to be good to go really either way.
[135:57] So you can choose whether you want to bring these in individually or combine them into one object.
[136:04] Another trick we could actually do, and you will actually see we have one piece for each packed object or each primitive rather.
[136:15] So static because these are not packed and animated, we're going to have one for each of these.
[136:24] And you'll notice we actually have one single mesh.
[136:27] And that is we had actually brought in the geometry here from all my objects.
[136:35] So that was before we had created any name attributes or any packed geometry, but our animated objects.
[136:44] If I find out which one those are, those are actually packed and they do have a name attribute, which is board 00.
[137:01] And it looks like we are getting a updated value for this, which is fine.
[137:18] So we're going to keep working as is.
[137:20] But depending on where you brought that in, the name attribute as well as a path attribute is used within Solaris to define our primitive hierarchy.
[137:30] But we'll go for now.
[137:33] Either way is fine.
[137:34] And perhaps we could clean this naming up a little bit.
[137:37] But for the purpose of our mini course lesson, we're not going to dive into that because that will be unneeded for this setup here.
[137:50] So we've got our props, we've got our marbles, materials.
[137:57] Let's go to assign my materials and it looks like props pegboard.
[138:03] So instead of just static, I could do this wild card to get both the static and the animated.
[138:10] And then for marbles, let's create a material for those.
[138:15] And I'm going to jump inside and use a material X builder.
[138:22] I'm going to say simple marbles jump inside.
[138:29] And if I set these to, let's see what color we had picked early in the videos.
[138:34] So orange, I'll set that color to orange.
[138:38] I don't need this flag time or set it back you, you to go up.
[138:43] I now need to auto fill materials to bring that into my scene, my network view rather, my scene graph path.
[138:51] And I'll assign this to the marbles for primitives.
[138:58] And I'll go to simple marbles.
[139:00] And there we go.
[139:01] You now have our orange material.
[139:05] And if we go down to lights, if I go to hero cam or even cam one, we actually did increase the size of our pegboard between from when we first created our layout camera.
[139:20] So I'm going to move this around.
[139:23] And we might even need to make our background a little bit bigger.
[139:27] So we'll go to backdrop.
[139:30] I'll do a transform right here.
[139:32] And I'll just drag the primitive.
[139:35] I'll make it five times bigger.
[139:37] Just so as we zoom out, we're not going to be seeing our HDRI.
[139:42] And if I render this now, we should see our lighting and our materials and everything else working nicely.
[139:51] All right.
[139:52] So I'll do a quick snapshot.
[139:54] I'll name this our second render.
[139:59] And that actually will be the end of our Solaris intro setup.
[140:07] So let's right click color correction.
[140:10] Go to aces.
[140:12] And we can now see we started with our pegboard, which is the smaller size we had created early, actually quite a few videos ago.
[140:20] And now we've got our little bit bigger pegboard.
[140:23] One thing maybe we'll do is I'm going to do a render geometry settings on my marbles.
[140:30] And I want to set motion blur for these.
[140:33] So I'm going to go to primitives.
[140:36] I'll grab marbles, which is this first primitive here.
[140:41] And you can actually see we have all of our individual marbles here because we don't have that many.
[140:46] This is perfectly fine when we're going to be using the same thing.
[140:50] Because we don't have that many.
[140:52] This is a perfectly fine way of working.
[140:54] But if we had thousands and thousands and thousands, that would probably slow down Solaris.
[140:59] But now for this motion blur, I will go to velocity blur, set this to velocity blur.
[141:05] And then once we start rendering this later, I'll have to actually ensure that we have our correct motion blur.
[141:14] So I go down here to karma render settings.
[141:17] I'll go to camera effects.
[141:19] I do want depth of field and I do want velocity blur.
[141:22] And I can even set this here.
[141:25] So that will be good for now.
[141:31] And maybe all we are doing our initial slayer setup, I might rearrange some of these cameras.
[141:41] So I'll make hero cam.
[141:43] Maybe we want to focus just on the center.
[141:53] Maybe camera one.
[141:59] We'll want to focus up here.
[142:02] And we'll do camera two.
[142:09] Maybe this will be a little bit wider of an angle.
[142:12] Actually, it looks like that is pretty wide.
[142:16] So maybe I'll leave camera two at, looks like it's 35 millimeters.
[142:22] I'll go to camera one.
[142:25] Maybe I want to set this to a 85 millimeter.
[142:29] It's a little bit more zoomed in.
[142:34] We'll see a nice preview of our simulation.
[142:39] And I think that might be good.
[142:42] Actually, maybe we can actually make sure we're getting these ones.
[142:47] So it looks like I've got one camera here.
[142:49] And these are the ones we had sketched out in the very, very, very first planning video.
[142:53] So to stay consistent, maybe I'll do one.
[143:03] Here, which might be this little red box.
[143:07] The hero cam was the wide setup.
[143:10] So maybe I'll zoom out again and see the entire shot.
[143:16] One zoomed in perhaps on this right side here from a little bottom angle.
[143:22] So maybe that'll be this right here.
[143:28] And then one more camera three.
[143:31] We'll place this at the top so we can see these slowly becoming active and inactive,
[143:39] or rather transitioning from inactive to active.
[143:44] And we don't actually have the color value.
[143:47] So if I render this now, they'll all still be orange.
[143:50] We'll set up how we actually bring the active attribute into our coloring of material.
[143:57] Once we get to the material section of this course.
[144:02] So I'm going to do cam 0, 3 preview.
[144:10] Perhaps I'll find a frame.
[144:13] Whoops, not CPU.
[144:15] I'll just put a little ball here.
[144:27] This will be camera one preview.
[144:36] And we will actually do quite a bit of work for look development to make this look nice.
[144:42] What for now? I just want to have something we can actually see our progress with.
[144:46] So camera 0, 2 preview.
[144:51] Let me hide my camera there and hide my light.
[144:57] I'll let it think for a second.
[144:59] And this will be hero cam wide preview.
[145:06] All right.
[145:07] So we've got some good renders here.
[145:11] All right, at least some previews here so we can continue working.
[145:15] So that's going to be the end of this video of our bringing our simulation into Solaris.
[145:23] I skip back to this object here, our pegboard setup.
[145:28] We will have our objects here we created.
[145:32] We did these nulls to actually fetch this geometry and bring it into Solaris.
[145:36] And then we had this here as well.
[145:38] Another option perhaps could be to actually only bring these points into Solaris and then instance onto those objects there.
[145:46] For now, we are perfectly fine with what we have here and this will work fine.
[145:53] So I'll go back and take one more look at my renders.
[146:01] There we go.
[146:02] And that's going to be the end of this video and we'll come back in the next one to keep working.
[146:08] Welcome back.


### Lesson 09: Houdini - Geometry Lookdev Prep [146:10]
**Transcript (timestamped):**
[146:12] And if you're just joining us, then welcome.
[146:16] We are continuing from where we left off in the last video for this Houdini mini course.
[146:22] And we are actually going to do a little bit of look development prep for our simulation where we left off in the last video.
[146:29] We had finished our simulation, which is this preview on the right.
[146:35] And then we had set up the Solaris for bringing that actually into our rendering context.
[146:46] Bring it into our rendering context to start setting it up.
[146:50] And we actually did four previews of what it looks like.
[146:56] And we do have quite a bit of work for look development to make this look nice.
[147:01] So we're going to begin in this video actually by repairing our geometry and doing a little bit more of a higher resolution version for some of these here.
[147:12] So let's just get started.
[147:15] I'm going to go back to my pegboard setup.
[147:21] And this is what we've been left off in the last video.
[147:24] One thing I want to be aware of is the simulation geometry.
[147:33] If we really, really wanted to be as optimized as possible, we might want to simulate with one set of geometry for the boards and the pegs and then create higher resolution geometry to be used for rendering.
[147:49] But for our case, to keep this a little bit more flexible and not go too complex for organization, I'm going to be fine with making this lower resolution geometry here, making this a little bit higher resolution and then simulating again with the higher resolution.
[148:11] So our sims, instead of maybe 10 seconds, they might take 45 seconds.
[148:16] But in our case, that is completely fine for what we're doing.
[148:21] So the very first thing I want to do is I actually want to make this peg a little bit more detailed.
[148:27] And that's actually right here where we've got this tube.
[148:31] So I'm going to look at the individual tube.
[148:35] And we can even increase our rows, maybe to four columns.
[148:41] I'll do 16.
[148:44] And I want to do a little polybevel.
[148:50] And if you did want to make this higher resolution and then render or simulate rather, excuse me, with the lower resolution, you could either create proxy versions of all the geometry, which might be in this case a little overkill.
[149:06] Or what you could do is you could take all your objects here, split them out and then detail before, so separately from your simulation.
[149:18] And then you'd be merging back in your rendered marbles or your simulated marbles with the higher resolution geometry here.
[149:26] So either way would work.
[149:27] That would be up to you to choose how you'd want to set that up.
[149:32] So I'm going to make a little bit more space by moving this down, polybevel, and let's do .01.
[149:45] I'm going to set divisions to maybe four and exclusions.
[149:50] I'll increase this.
[149:53] So I'm not dividing and beveling these areas that should not be beveled.
[150:02] And I can maybe even add 24 columns.
[150:09] And that should be good.
[150:11] And I actually want to UV unwrap this.
[150:17] And we're not going to worry too much about UVs, but I might want to do some noise textures based in UV space.
[150:22] So having UVs is going to be very helpful for that.
[150:27] So that's going to be all I need to do for these individual pegs.
[150:31] For the rotating boards, let's do a little bit of work here as well.
[150:36] And I'll actually move these down and then I will copy the UV unwrap and the polybevel from that tube there.
[150:50] Hit W to go into wireframe and you can see what we're working with.
[150:55] And I might even actually want to add a little bit more of these divisions.
[151:03] I'll do X and I'll do them on the Z.
[151:07] Maybe I'll do four and 12.
[151:11] And part of the reason I might be doing this is also for motion blur,
[151:16] but we're not having that fast moving of an object.
[151:19] So we don't necessarily need to have too many points on this object for all of those interesting motion blurs.
[151:26] And that might make more sense if we did have fast moving objects,
[151:30] but for now I will also have a little bit more of that resolution there.
[151:35] So that should be good.
[151:38] Let's find where our main board was here.
[151:43] Looks like we already did add some bevels here, but I might even want to increase this.
[151:49] We'll do four divisions.
[152:06] And maybe actually what we could do.
[152:10] Let's divide this a little bit bigger.
[152:14] And then I'll do another polybevel just so we've got a nice interesting edge on the side here.
[152:24] So I'll divide it once with one division and then a second time 0.01, maybe with a few more.
[152:34] Then I could add my exclusions to increase that value.
[152:38] And now I've got a little bit of a nice geometric shape on the side,
[152:42] which might give some more interesting of a render if I do have this previewed on the side.
[152:48] So I'll catch a little bit of light here on the edges.
[152:51] I'm also going to want to UV unwrap this.
[152:54] So I will UV unwrap before I bevel, but after I extrude.
[153:03] And that should be good to go.
[153:12] For our sphere, this will be plenty fine resolution.
[153:19] Perhaps we actually want to try a box simulation later.
[153:23] So I'm going to bevel this one here just to give some round edges.
[153:30] And now in this case, the round edges here on the box will also make for more interesting simulation.
[153:37] So these might give me some more interesting bounces and a little bit more of an organic look
[153:43] than if I had perfectly sharp edges for my object.
[153:47] So maybe I'll make that six or four.
[153:52] Either way would be fine.
[153:59] And I'm actually going to decrease the size of my box to I'll do 0.4 right here.
[154:07] So if I now preview the switch, the box is roughly the same size as my sphere.
[154:14] I'm going to do 0.05 for the distance.
[154:17] And the reason I want to have that the same size is so it actually fits between these pegs.
[154:23] If I do choose to simulate that later.
[154:28] So I think that should be good.
[154:30] The glass, we actually haven't brought into Solaris.
[154:37] And if you do remember, if you've been following along, we had created some glass that was a collider or really a grid here on the front.
[154:46] That was a collider in the simulation, but we deleted it after the simulation.
[154:53] And one thing we might want to do as well is normalize these UVs just so they're roughly the same scale.
[155:00] And a way I can fix that is after this UV unwrap for my grids back here, I'm going to add a UV transform, which is on the main board.
[155:13] And I'm going to scale to 10 just so my UV grid is roughly the same size.
[155:21] Because I'm not using actual textures in this case, I might be doing some tiled textures, but there's no specific materials needed for specific parts of this object.
[155:31] This is going to be a fine way of setting those up.
[155:37] So that's good. We do not have any file caches here.
[155:40] So sometimes when we prep geometry before, we want to make sure we would recache that for our setup here.
[155:47] But we should be good to go. We can even do one quick test to save this simulation to disk just to see how long it takes with this higher resolution.
[156:01] And I think it took nine or 10 seconds with the lower resolution, so really not too big of a difference at all.
[156:10] And now if I preview out to render pegboard all, I can uncheck this to hide those UV coordinates.
[156:19] And now I control and click my flag for the marbles. We can now see I've got my marble simulation working.
[156:33] There we go.
[156:35] All right, so I've got the geometry a little bit higher resolution.
[156:38] Got some nice corners that are going to be good.
[156:42] So let's go back into my scene.
[156:46] And one more thing I actually sometimes like to do is I'm going to make another camera. I'm going to call it look dev camera.
[156:53] And I like to be able to move around my scene with an actual camera so I can set some of my depth of field.
[157:04] So I'm going to go here, switch this to Karma XPU correction toolbar.
[157:13] I'll go to ACEs tone mapping.
[157:23] And I'm just looking around at my scene to see from the angles that I might want to have for this shot.
[157:32] Do I think I have enough resolution in my geometry?
[157:39] I'm going to actually increase the sphere resolution.
[157:44] So what I can do is on these marbles.
[157:49] And this might actually be a case.
[157:51] So if you remember from some of the previous videos, we've simulated these marbles here with this incoming geometry stream and this SOP solver.
[158:01] In this workflow as well for the SOP solvers that we set up from scratch, we had done this null that was fetched.
[158:09] So what I might want to do is have this geometry here, simulate it with this and then subdivide it after the simulation has been done.
[158:21] So in that case, I would do that on the geometry I'm transforming onto my simulation points.
[158:28] So if I subdivide this here, in which case actually I can't subdivide these points because they're packed geometry.
[158:35] So what I can do is I can unpack.
[158:45] And in this case, I would actually want to have it time shifted.
[158:50] So I don't want to unpack on animated geometry or on time dependent geometry because then it's going to be unpacking every frame.
[158:59] I will time shift it.
[159:03] Put this a dark gray.
[159:07] Unpack.
[159:13] Now I want to make sure I'm transferring my color and my name and my active as well.
[159:22] Subdivide this to get this higher resolution.
[159:26] And I'll even go to just because I'll go a little bit crazy.
[159:30] And then what I would do is I could assemble my geometry again and this assemble will pack my geometry and transfer the name.
[159:39] I don't want to create a name attribute, but I do want to create packed primitives.
[159:49] So in this case, perhaps I'll actually pack this manually.
[159:52] So pack.
[159:56] Pack by name.
[160:07] In this case, my name attribute on this is going to have to be on primitives.
[160:15] So I'm going to promote the name attribute back from points to primitives, then pack it, then transfer it back onto the geometry and then promote it back to the primitives to the point.
[160:32] So name.
[160:34] So now I've got my name attribute on the object here.
[160:39] And what I also want to get is my active.
[160:47] Which it looks like I have here.
[160:51] And I actually do not have the active attribute.
[160:54] So what I could do rather than setting that up.
[160:58] So I'm looking now at my packed geometry and hopefully this isn't confusing.
[161:02] But I'm looking at my pack geometry and I've got my color and my active.
[161:05] What I'm going to do is only transfer this name.
[161:10] I don't want to worry about the active yet.
[161:15] But I will promote this here.
[161:16] So now I've got my name attribute.
[161:19] And now I'm going to copy.
[161:23] To this subdivided geometry from this.
[161:30] Still animated.
[161:31] So right here still animated.
[161:34] And if I toggle this you can see my active is going to be changing.
[161:37] So is my color connected this here.
[161:42] And I want to transfer the color.
[161:46] And I also want to transfer the active.
[161:51] And now I've got this subdivided geometry with the same matching name with the same active attribute and with the same color.
[161:59] But I'm not unpacking on every single frame.
[162:10] So this is time shift to modify sphere geo.
[162:18] And now when I connect this attribute copy I can confirm I've got the same setup.
[162:27] So connect this here.
[162:28] This has my name, my active on the points.
[162:33] This has my name and active on the points.
[162:37] So I should get the exact same results here.
[162:41] Whether I connect this one with this high resolution geometry here.
[162:45] Or this one with the low resolution geometry here.
[162:49] So I do hope that made sense.
[162:50] That was a little bit intricate.
[162:52] But hopefully you kind of understand where these attributes are moving.
[162:57] How they're on certain points or primitives.
[163:00] And then where they might be looking for these attributes.
[163:04] You can see it gives me a little bit of an error.
[163:06] If I do not have my name attribute on the primitives.
[163:09] So I promoted that back from points to primitive.
[163:12] That works correctly.
[163:13] And then I bring it back from primitive to point.
[163:17] Because that is working here.
[163:19] And there's many, many different ways we can set this up.
[163:21] But this is one way that gives me my high resolution geometry.
[163:25] Transfer it onto my low res.
[163:27] And I could even do a mountain node.
[163:33] If I wanted to make these irregular like some kind of rocks.
[163:37] And in this case, I might want to do that on the simulated geometry.
[163:43] So the shape of these objects actually affects how they bounce.
[163:49] So a little bit of a hopefully understandable setup.
[163:56] We just set there.
[164:01] I'm going to move these and make sure they're all nicely in my network.
[164:10] And go back to Solaris.
[164:15] Jump inside my scene.
[164:20] And now if I look at my lookdev camera.
[164:23] I've got my karma render settings down here.
[164:31] And I'm looking through aces.
[164:32] I can now see I've got some nice high resolution sphere geometry on that object there.
[164:42] And if I did want to have my HDRI visible on dome lights karma.
[164:48] I can set render light geometry.
[164:50] And now I will see that in my render.
[165:00] So I think we might be good to go.
[165:04] I can even test out some depth of field if I want.
[165:08] So to do that, I'll go to my lookdev camera.
[165:10] Sampling.
[165:12] Maybe I'll set my focus stop at 0.5.
[165:16] If I hit enter over my scene view while holding my camera.
[165:21] I can get these tooltips that pop up.
[165:23] And I can shift and left click to set a focus distance.
[165:29] And maybe even I want to increase this to.
[165:33] Well, the lower the f stop, the more strong your depth of field will be.
[165:37] But this is also going to depend on your scene scale.
[165:40] So I can shift f1 to hide those hints.
[165:48] And we can see we have some nice depth of field for these objects.
[165:56] So this would give us some pretty cool settings if we did some rack poles for focus.
[166:00] Maybe from the far to the near.
[166:05] But I think this should be good for what we need.
[166:08] So I want to actually maybe increase my render size to 1920.
[166:16] Because all of these aspect ratios are the same.
[166:19] I'm fine leaving my hero camera here.
[166:22] But you do want to be aware of the camera and the resolution.
[166:27] So that can define your aspect ratio correctly.
[166:32] And what I mean by that is if I have a camera that's set to 16 by 9 and a 4 by 5 somewhere within here.
[166:40] It will only match the certain one.
[166:44] So I want to be kind of aware of which ones are which if I'm choosing to render in multiple aspect ratios.
[166:51] So let's do nicer camera.
[166:59] And maybe even we'll do another look to have camera as well.
[167:18] Maybe you can have one where the balls are falling down.
[167:30] And if I did want to get some denoising I can go to my image output filters and select a denoiser.
[167:39] And here we go.
[167:44] I'll do one more just for fun.
[167:52] And we will come back in the next one to improve on this look dev.
[167:59] And maybe even set up some nicer materials as well as some nicer lighting.
[168:05] But even with just these simple materials with a little bit of depth of field.
[168:13] Let me rename this to nicer camera to actually this will be looked at.
[168:22] But I'll leave that nicer camera three because this is a lot nicer of a render.
[168:29] Open that up.
[168:31] It looks like I had minimized it here and I can right click color correction.
[168:36] And now if we take a look this is our very first render we got from our initial setup.
[168:43] We got our geometry in this hilarious.
[168:45] We did a couple different camera angles to see what they look like.
[168:48] And then just by adding some additional resolution to this geometry.
[168:56] We can see we're actually catching the light a little bit nicer on some of these edges.
[169:01] And by adding some depth of field we've now got quite a nice image already.
[169:07] And we really haven't done that much look development excuse me at all.
[169:13] So awesome.
[169:14] I'm very excited about how this is looking and I hope you're encouraged and excited to keep following along.
[169:20] So that will be all for this lesson and we'll come back in the next one to keep making this look pretty cool.
[169:28] So awesome.
[169:29] I'll see you then.


### Lesson 10: Houdini - Karma Material, Peg Board [169:33]
**Transcript (timestamped):**
[169:35] Welcome back and welcome to the next lesson in this Houdini Mini course.
[169:40] In this video we're going to take a look at completing a little bit more look development for our pegboard.
[169:48] As well as some of these boards that are rotating.
[169:51] This is the animation and the simulation actually we had set up from scratch in the previous videos.
[169:57] So if you're joining us then welcome.
[169:59] You can follow along 100% from scratch by starting at the beginning of this playlist.
[170:05] But what we're going to do now is we're going to continue from where we left off.
[170:09] Which were these last three renders here.
[170:12] And we're going to set up a little bit more of an interesting material for our boards for our pegs and then for the back wall itself.
[170:26] So to get started we actually had done in the last video some more of the edges resolution add some bevels.
[170:35] And we actually did add UVs as well to our geometry.
[170:39] So we're going to make use of those to create our mapping for the textures to the objects.
[170:48] And the important thing is because we do have animated objects if we are doing some kind of a trip liner projection or a rest kind of projection for using the world position to project materials.
[171:00] We'd want to be aware of having that before having that done before it's animated.
[171:06] But because we're using UVs for everything will be fine to just map these textures as expected.
[171:11] So first thing I'm actually going to do is I'm going to take this transform for my grid.
[171:17] And I want to bring that a little bit closer just to give me some more or bring my backdrop excuse me rather a little bit closer to the object.
[171:30] So I can go a little bit wider with some of these camera angles.
[171:34] So let's go into one of our look dev cameras.
[171:42] Maybe we'll do look dev camera to Karma XPU.
[171:56] And I could shift click so I can select my look dev camera here hit enter to get my active camera gizmo and shift click to change the focus length or the focal distance rather here.
[172:11] And I think this should be a good setup for our materials.
[172:16] So I'm going to say this is before.
[172:19] And what we might even do is I'm going to duplicate this my materials and I'm going to say my materials simple.
[172:31] And I'm going to jump inside here and I will actually leave these names the same.
[172:39] And this is just going to have a little bit of a backup for some of those other materials.
[172:44] But what we're going to do is I'll actually duplicate this.
[172:57] I'll say improved.
[173:00] I'll say textured backdrop.
[173:05] And I'm going to create one and then I'm going to duplicate it again for these and actually rather than backdrop.
[173:13] I'm going to do this.
[173:15] Textured peg board.
[173:21] Jump inside here and let's go to base color.
[173:27] Open some of these up and I've actually done a.
[173:32] So I go to tiled.
[173:34] Image.
[173:35] I have included.
[173:37] Under the textures.
[173:40] I've included three different free textures actually from texture Haven.com.
[173:47] And these are ARM maps.
[173:50] So it's ambient occlusion roughness and metalness channel packed into one texture.
[173:56] So we're going to be using these for our images.
[174:04] I want to get a separate vector three.
[174:07] So this is split RGB channels.
[174:12] This is load my image actually name this my.
[174:17] I believe this is plaster or concrete.
[174:21] So you are welcome to create your own materials or follow along with me.
[174:25] I'm going to be using these textures and kind of creating my own maybe material with some different color blending and some even metalness and just make a material that I think looks cool.
[174:36] But if you would like to use a plywood material from a material library, you are more than welcome to choose your own look development approach.
[174:45] So I'll connect this first to the base color.
[174:49] And one thing we can actually do is if we go to surface on lit connect this to the output and put this into the emission color.
[174:58] This lets us get a preview of any of these nodes without having to have our lighting information.
[175:05] So I'm going to go texture pegboard.
[175:08] I will bring that up.
[175:11] If I don't actually want these to come up, I could uncheck the flags on the inside so simple doesn't bring up those materials.
[175:18] But I'm going to leave textured pegboard.
[175:21] Assign my materials.
[175:23] I'll actually duplicate this as well just to have a little backup of those.
[175:30] And for pegboard, I will assign it.
[175:39] Maybe actually I'll start with these boards here.
[175:43] Because I might want to have a different material for the back and for these fronts.
[175:47] So I'll go pegboard animated.
[175:50] Which will just assign it to this one here.
[175:53] And then for pegboard static.
[176:01] I want simple pegboard on pegboard static and then textured pegboard on pegboard animated.
[176:08] Now you can actually see if I go to karma.
[176:16] We're now seeing just the texture itself.
[176:19] And I like doing these for materials.
[176:21] Especially these channel packed ones.
[176:23] Because I can get a good amount of variation with just a simple texture.
[176:29] And even for now, I'm going to uncheck my depth of field.
[176:37] But I wanted to have these files be nice and easy to download.
[176:40] So we are using these 2k packed textures.
[176:44] So I'll go into my materials.
[176:47] Texture pegboard.
[176:49] And what I can do is a color ramp.
[176:53] And you'll actually see if I plug this concrete here.
[176:57] We'll have this color.
[176:58] And that's because it's the three maps packed on top.
[177:01] And we can kind of blend these and I might use one for texture.
[177:04] Or one for color.
[177:06] Or roughness and maybe one for the bump.
[177:08] So there's lots of different ways to mix and match these.
[177:12] But now I want this X plugged into here.
[177:16] Which will be my diffuse color.
[177:19] I can connect that into my emission color.
[177:22] And maybe this is some kind of neutral kind of beige color.
[177:33] I'm going to delete this one and click to create a second.
[177:45] This one will be a little bit brighter.
[177:47] And then this left side can be a little bit darker.
[177:50] Maybe a little bit darker and a little bit more saturated.
[178:01] And if I don't want this to be such high resolution for my preview.
[178:06] I could set this to maybe 1260 or 1280.
[178:12] And now because I've got my display flag set on Karma render settings.
[178:17] If I go back here.
[178:19] The render size is going to be forced by my Karma render settings.
[178:25] Even if I make my scene view a lot bigger.
[178:30] And if I want to get this whole thing previewed.
[178:33] I could exit my camera.
[178:37] But for now we'll leave this here.
[178:39] This is going to render a little bit quicker.
[178:41] And make my computer a little bit happier.
[178:43] Since I'm recording and working at the same time.
[179:00] I can preview again these colors.
[179:02] This is relatively bright.
[179:04] I could bring back in some contrast.
[179:06] But for now we will stick with this.
[179:15] Maybe I'll tighten that up a little bit there.
[179:19] We've got some good looks.
[179:21] Maybe even on this side I can go a bit darker.
[179:32] And this diffuse color I'll put in my base color.
[179:38] And connect my standard surface to the output.
[179:42] And we'll see what I got.
[179:46] So that'll be good for now.
[179:48] Now what I want to do is.
[179:50] I'm just going to add a roughness map and a bump map.
[179:53] Sometimes with these I'd like to set the color to a relatively dark color.
[179:59] So I've just disconnected this diffuse color.
[180:01] Because I want to be able to see the contribution of my roughness map by itself.
[180:06] And sometimes that on a dark object is a little bit easier to see.
[180:09] So I'll go to this split or GB channels.
[180:12] I'm going to grab the Y.
[180:15] And I'm going to do a float ramp.
[180:21] And I'll connect this to my emission color.
[180:23] And I'll connect the unlit to my surface output.
[180:32] And now we can see the texture I'll be working with.
[180:35] If I want a little more contrast.
[180:37] I could bring this lower value up.
[180:41] But what I should be aware of is this is now going to be the roughness value.
[180:45] So I'll connect this to my specular roughness.
[180:48] And connect that back into my material surface.
[180:58] And if I find an angle where this light is nice and visible.
[181:04] You can see exactly the effect that this roughness map is having.
[181:08] And this is why I like using it on some of these dark objects.
[181:10] Because it makes it nice to see.
[181:14] And for roughness, maybe I'll do 0.2 to 0.7.
[181:21] Maybe 0.1.
[181:24] Zero will be no roughness.
[181:25] So a fully smooth and glossy material.
[181:31] And we do have the denors are still enabled.
[181:33] So we might not see as much detail as we would in a final render.
[181:38] But that'll be okay.
[181:42] Welcome back and apologies for that quick cut.
[181:44] We're going to continue from exactly where we left off.
[181:47] And we're going to add a.
[181:50] We're going to use this height map actually and convert it to a normal map.
[181:53] And then plug that into our normal.
[181:58] To get a result right now we can see we've disconnected everything.
[182:02] And I'm going to use a height to normal.
[182:05] I'll plug this into the Y.
[182:07] Because I do actually want my roughness, which would be this one.
[182:11] And my normal map to be driven by the same texture.
[182:14] So they have similar characteristics perhaps we could say.
[182:20] And then I'll use a normal map.
[182:22] Connect this height to normal to the input.
[182:25] And output I'll plug that into normal.
[182:29] Now we can see the result of this, but this is quite a bit too intense.
[182:35] I'm going to decrease this to be 0.02, 0.01.
[182:51] And let's see if this is actually the concrete.
[182:53] This looks like it is.
[182:58] Let's take a look at what the plaster looks like.
[183:06] Maybe we'll leave it with the concrete for now.
[183:12] So that'll be the normal map, the roughness, and the diffuse color.
[183:29] And we can modify these as we need.
[183:34] Once we've got a little bit more of our lighting set up.
[183:40] So just double checking to see if this looks good.
[183:42] One thing we actually will have is these are going to have duplicate textures.
[183:47] Because they are the same object with the same UVs.
[183:50] We could either offset those UVs if we did want to.
[183:56] Or we could make some changes later, but for now we're going to be fine with that.
[184:03] And I might even want to increase this roughness to a little bit higher of a value.
[184:17] So I think that'll be good.
[184:19] Got the textured pegboard.
[184:23] I'm going to leave my UV tiling the same.
[184:27] And what I'm going to actually do is hit U to go up.
[184:30] I'm going to duplicate this as well.
[184:35] Actually I'll assign this to the whole board.
[184:38] And if we need to change the scale between the objects, we can modify the UVs of our object as well.
[184:45] So go back up, texture pegboard.
[184:47] And I'm going to assign that here on pegboard everything.
[184:54] And then I'm going to have to uncheck this bottom one here.
[184:57] And now if I render this, we should see we've got the material assigned to all of the objects.
[185:10] And because we had already set up the UVs to be relatively consistent between scaling,
[185:23] that should work correctly.
[185:27] I'm actually going to do one quick test.
[185:31] I want to add a light down here.
[185:37] And I'm just going to check to make sure my reflection values are looking a good value for roughness
[185:46] and the normal intensity and all of that.
[185:49] So I'm going to move this light up to the middle.
[185:56] I can toggle my light preview right here if I want to see where it is.
[186:00] And I'll set this one here to a sphere light.
[186:05] Decrease its size a little bit, check normalize power, and increase the exposure.
[186:13] And now if I render this and even disable my dome light,
[186:27] we can get a look at what this might look like from different angles.
[186:32] And perhaps this roughness is too low.
[186:40] Maybe I'll increase my roughness.
[186:42] So if I go here, 0.3 to 0.7, let's do 0.5 to 0.8.
[187:02] You can go back up.
[187:04] I'll now enable my dome light again and disable that temporary light.
[187:14] And let's zoom out.
[187:19] Take a look at some of our other cameras.
[187:22] If I select one of these other primitives here, you won't actually see this highlight in my scene view.
[187:28] It may be even our tiling is noticeably peating,
[187:39] but we might actually be fine with how it's set up here.
[187:48] So if we did want to have a different color, one easy way to do this,
[187:56] and I'll do this really quick, sometimes with these,
[188:00] I might be doing my output x, my value here, my float, and I might do a color.
[188:12] I'll get a constant.
[188:14] So sometimes rather than using ramps, I find it easier to use a single color.
[188:19] I'll set this to the base color that I want to have most of my object looking like.
[188:27] And then I would use a color correct to create a dark color.
[188:39] And then I use a mix and blend between these two based on a float value.
[188:50] And then this one actually rather than reverse to default, I want this to be main color.
[188:58] So I'll connect this.
[188:59] I'll even make this a orange to make this a little more visible, connect that in.
[189:04] And then what I might do is decrease my saturation, maybe decrease my exposure.
[189:10] And then I'll connect this to my output.
[189:20] And then by balancing float ramp this here, I could even set the saturation to zero on the left side.
[189:33] We can find where on this ramp our image actually is and then get some nice variation here that's driven by this color correct.
[189:50] But now the convenient thing is we can actually notice our tiling now.
[189:55] But now what we can do is modify the whole look of this by a single color.
[190:03] Because sometimes having these diffuse color ramps, you have to change a few of these to get the nice value.
[190:09] But sometimes having just one single color driving your look is a little bit easier to create.
[190:20] So maybe even I like this concrete.
[190:24] I think actually I do like the gray.
[190:30] And then one thing I'm seeing there is a little bit of a tiling.
[190:34] So if I take this color correct, drop my exposure negative five, you'll see one tile two, three, four, five, which in my case isn't a huge deal.
[190:44] But what I'm going to do is I'm going to adjust the UVs for the backboard to reduce the tiling just a little bit.
[190:51] I'm going to go back to my object level, jump into setup, headboard.
[190:57] I'll find where I have my main board, which is right up here, main board.
[191:02] I'll take my UVs, preview them, and I'll see my transform.
[191:08] I had scaled it down 10.
[191:10] So I'm going to do five just to cut that in half.
[191:14] And now if I go back into my Solaris setup, you'll see I only have one, two, three tiles instead of five.
[191:32] And I'll jump back inside materials and take this color correct, negative one, maybe negative one point five.
[191:41] So I'll say this is darker color, blend colors.
[191:50] And this, maybe I'll make this a yellow one to see it distinctly.
[191:55] But this ramp could be fine if you want to fine tune a lot of colors.
[191:59] I find this trick of a color with some color corrects is a really helpful way to get some quick variation as you're testing.
[192:10] So I do like this a lot.
[192:12] I think that might be the end actually of our pegboard materials.
[192:24] And we can actually now see our textures are quite not super high resolution since we are using 2K textures.
[192:31] So maybe instead of scaling that down to five, I'll leave this at eight.
[192:38] So I'll reduce the tiling a little bit, but not that much.
[192:42] And if you want to find 4K textures or even 8K texture to use, that would be up to you.
[192:49] But for our purpose, we will stick with these lower resolution ones.
[193:05] Maybe try to decide if I want a gray.
[193:19] So let's take a snapshot of the gray or if I want like a warmer tone.
[193:28] In this case, I might want to decrease or reduce that saturation here.
[193:34] Maybe even I increase this.
[193:39] Negative one.
[193:52] And I can even modify this ramp here.
[194:14] Well, I'll duplicate this.
[194:18] I'll leave this as that neutral color.
[194:22] Maybe I'll set this one to a gray because maybe we'll get some color cool colors from our spheres that will add a nice setup there.
[194:32] So before we end this video, I'll do one more preview, maybe two more previews with our depth of field.
[194:45] Take a snapshot.
[194:57] Find a nice cool camera angle.
[194:59] Camera two. Enter and shift left click to set the focus.
[195:20] And maybe I'll stick with this one.
[195:26] And I'll say gray, zero one, gray, zero two, and gray, zero three.
[195:35] Alright, well, it's going to be the end of this lesson.
[195:38] And the next one will come back and set up the material for our spheres.
[195:42] And also the color attribute will need to have in order to actually have these change from active to nonactive.
[195:50] So awesome. That'll be all for this video and I'll be back in the next one.
[195:57] Welcome back and welcome to the next lesson in this Houdini mini course.


### Lesson 11: Houdini - Karma Materials, Marbles [195:58]
**Transcript (timestamped):**
[196:05] In this video, we're going to continue from where we left off, which was actually creating the material for our back pegboard.
[196:12] And we're going to start setting up the material for our ball as well.
[196:16] And if you're just joining us, what we've been creating over the last few videos is this full simulation 100% from scratch in Houdini.
[196:25] And the final result of what we make is the trailer at the beginning of this video.
[196:31] So go check that out. And then if you're interested in following along, I encourage you to do so and download the project files below.
[196:37] But for now, let's jump into basically exactly where we left off in the last video and start setting up the ball materials.
[196:48] So the first thing we want to be aware of is we actually had a couple things actually.
[196:55] First of all, every single sphere is the exact same sphere.
[197:01] So I go do marbles, jump to where we brought those in.
[197:05] It was actually down here and every sphere is the same object, which is fine.
[197:12] But the same geometry as well with the same. Actually, we don't have UVs.
[197:19] So let's, because we hadn't created those yet.
[197:26] Maybe rather than UVs, let's actually do, let's try a rest noise for these objects.
[197:33] So I'm going to go to my object here.
[197:37] And actually, I could add that before my simulation or I could add this information when I do the subdivision on this geometry here.
[197:51] I'm going to choose to do it here because in this case, we are unpacking all this geometry and now it is in world space,
[198:00] which means every object has its own unique position rather than creating this attribute here where they all share the same object.
[198:09] So if I create a rest attribute here and then copy those points, all of these would share the same rest attribute because they be copies of this sphere here.
[198:19] If I did create it down here, I would then have variation built in automatically across every single sphere.
[198:26] So that'll be the approach I choose to take. I'm going to use a rest node to create my attribute.
[198:35] And that's actually all that I need to do.
[198:40] And I will not see that down here, but it is actually packed inside the geometry.
[198:46] And to see if I did one of these frames here and unpack, we can actually see my rest attribute there.
[198:55] So I'll leave it here. And while we're actually within our SOPS context, I'm going to do a geometry, or excuse me, a attribute wrangle.
[199:03] And I'm going to say V at V times equals 100.
[199:09] I'm going to say test, motion, blur.
[199:15] And for now, I will not actually use this one because I'll save this for a video when we set up final rendering, just maybe to keep our videos a little bit more on topic.
[199:27] So we've got our rest attribute here. We will not be using UVs. And because this is time shifted, we can see that our geometry is not moving.
[199:36] If we were computing a rest attribute on animated geometry, what we'd want to do is we want to freeze the geometry, compute the rest, and then transfer that back onto the animated geometry.
[199:47] But in our case, we are fine. This is what we want.
[199:54] And one thing to be aware of also is this active attribute.
[199:58] So I might actually do the two ways actually we could do this. The easiest way probably split at active equals zero.
[200:15] Whoops. Equals equals zero for points. Looks like either way would work. Interesting.
[200:23] So split the active equals zero. I could load this geometry into Solaris and texture this as one material. And this could be a separate material.
[200:36] Or what I could do, and maybe actually I'll do that.
[200:40] That might be easier because maybe I'll use the concrete material on this. So I'm going to say out to render static marbles.
[201:10] And I'll go back in here and marbles. I'll say static animated. And then on the static, I will paste this one here to be export relative path.
[201:28] I can jump to where this one was and actually don't need these nulls. So I'll duplicate this one and create a new one here. Out to render animated.
[201:40] Marbles. And there we go. And if I go back, I can merge these.
[201:53] Whoops. I hit control B, which brought full frame on this panel view. So I'm going to hit control B again to go back here. Whoops.
[202:05] I'm going to go back so I get to where I was. And I will go to this one, want to paste, which is the render animated marbles null that I had copied, which are those and static are these here.
[202:23] And then for motion blur, rather than marbles, just marbles, we want marbles wild card for everything.
[202:30] And then I'm going to go back and I'll actually enable that line of my wrangle right here to scale my velocities. I'm going to go back into Solaris.
[202:47] Go all the way back down to my render settings. Jump through on my cameras and see if we have our motion blur, which we should.
[203:17] And it looks like instance velocity blur. We have to check, I believe, because our geometry is packed.
[203:41] And we can actually now see getting quite a bit of motion blur. So I'm going to go back to Vulkan. You also notice our colors are messed up, which is fine.
[203:54] Jump back, not inside my Solaris network, but inside my pegboard. And I'm going to move this so I no longer have that set.
[204:11] And the reason our colors are messed up is because we had assigned geometry to, there we go, we can see our motion blur now.
[204:25] But we had assigned our material to marbles, but we now had renamed those primitives to marble static and marbles animated.
[204:33] So maybe what I want to do is I want to have these be the concrete. So that was actually textured pegboard was the concrete material I had used.
[204:44] So I'm going to assign a control C copy that. Oops, control C. I want textured pegboard on marbles, but I want those only on the marbles static.
[204:58] And now my display color is going to be fine. So my wireframe in my preview is red. But when I render this, we now see I've got these spheres here.
[205:12] And actually in this case, we are no longer having our textures projecting correctly because there are no UVs on these spheres.
[205:26] So let's create those very, very quickly. And the way we'll do that is we'll go to marble static, jump ahead.
[205:34] And I could actually UV unwrap here, which perhaps I will do on the sphere. And I'm fine with this projection right here.
[205:48] And another thing I could do is right now they're all going to be sharing the same UVs. If I UV unwrap again, they'll now all have different UVs.
[206:00] And then I could UV transform to scale that just to match the rest of I control click these, I can kind of see the overall scale.
[206:13] And actually I'll control click this one because this also does have my marble geometry.
[206:24] static pegs or sim board. We actually won't be seeing that because this is the old UVs right here. So I'll do transform.
[206:44] I'll leave it at five, five and five. And now they also will have a little bit different UVs per object. And I could have also offset those based on any number of things.
[206:57] But for now, this will be okay.
[207:01] And now if I render this, my UVs should be on the spheres. So I should actually see the textures within these objects here. And it looks like it is working.
[207:19] All right. Some good stuff. So now what I want to set up is I'm going to create a new material for the animated marbles.
[207:32] And I'm going to go material X. I'll say textured marbles.
[207:48] And actually, since they already do have UVs, rather than copying or creating new material, I'll just copy this one as our writing.
[207:56] So we already have all of the setup for our images and our roughness and anything we might want to set up for these.
[208:05] I'm going to go textured marbles for blend color. Maybe I'll set this to a orange autofill and then on assign my marbles.
[208:22] I can remove this pegboard static because I actually gave all the pegboards the same materials.
[208:27] I'll create a new one, textured marbles for material path and marbles animated for the ones I want to assign.
[208:36] And we'll now see that I have these orange. Whoops. I don't want to use redshift.
[208:44] All right. Welcome back. We are responding and working well again.
[208:49] And our material is now been assigned to the objects. So if I do a quick preview, we'll actually see we've got our concrete material now or our concrete like material now on our objects.
[209:03] And we've actually got our motion blur as well. So this is looking nice and solid.
[209:11] And we're going to keep moving. One thing I actually do want to do. I actually want to split because we had some of that we're supposed to be orange or and some of that was supposed to be blue.
[209:22] So there is quite a few different ways of doing it. But because we did split these two ones by object, perhaps I'll show you how to split by a material attribute within our geometry.
[209:36] So I'm going to go to marbles animated, jump ahead. And we can create that actually here, but perhaps the better way to set that up would be.
[210:01] I'm going to create a pretty much what I want to do is I want to make a random float on these points that are between zero and one.
[210:11] And I'm going to bring that into my shader because I could always split the float at point five. So half are blue, half are orange.
[210:18] But maybe I even want to do some that glow, some that are subsurface and kind of want to get a little more complex in my setup there.
[210:25] So having a float is going to give me a lot more flexibility than just an integer of zero or one.
[210:32] So I'm going to do a connectivity. And what this is going to do is it's going to create a integer attribute for the connected objects.
[210:42] Right now I can see class is zero to 25. And this is going to be used as a seed for my random values.
[210:51] And I could use an attribute randomized, set this to ran. It could be a float. So one zero to one, a random value operation is set.
[211:08] And I can seed this with my class. And now if I look here, everything that's got 25 for class is the same value for ran.
[211:20] So this is one way of doing it. Another way to do it would be to use a wrangle and just say f at ran equals ran at class.
[211:32] And this would be an equivalent way of setting that up. And you can see we see the matching random values for matching class attributes.
[211:42] I'm going to move these to make a little bit more space. And I'll actually connect this into here.
[211:48] And then one thing we want to be aware of is where our attribute is.
[211:57] So right now we've got our attribute on the geometry itself. And we are then packing that attribute and it looks like it disappeared.
[212:06] But it's actually inside this packed geometry. And if I went down here and unpacked a frame here.
[212:16] Whoops, not unique points, but unpack. We can see I now have my ran value as well.
[212:23] So I delete and I'm going to go back into Solaris and let's see if we can fetch this ran attribute into our shader.
[212:32] So we've got our marvels animated coming in. I'm going to jump inside my materials, go inside my textured marvels.
[212:39] I'm going to use a prim var reader. It's a fetch ran.
[212:44] And one thing to be aware of some of these variables and some of these attributes are renamed when they come into Solaris.
[212:52] So display color and CD is one of those UVs are also renamed to a different thing as well.
[212:58] So sometimes if you're not getting the attribute you'd expect, maybe rename it to a name that's more unique and you can figure that out then.
[213:06] So I've got this. So read in random.
[213:12] And I'm going to plug this very first just into the emission color for my surface on lit.
[213:20] And you'll actually now see it seems to be working. So if I go to Karma XPU, we should have a gray value to a black value or a white to a black rather for all of my objects and it looks like we do.
[213:38] All right. Now a way we could do this is with this main here. We can mix based off this value.
[213:50] So I'm going to use main color. Maybe this will be a blue. I'll find a blue that pairs nicely.
[213:57] So I'll do foreground background mix and connect this to my emission color.
[214:07] And we'll now have a gradient that goes between these two colors.
[214:14] But if we did want to have a sharper cut between those two, we could use a float ramp to actually modify this.
[214:24] And now how this would work is the closer we bring these two values, the sharper the distinction is going to be between the colors.
[214:35] Now it looks like actually most of these random values might even be below 0.5.
[214:42] So this is another thing why it's helpful to have this because you can actually modify the distribution of the colors.
[215:12] All right. Looks like my Karma was giving me a funny result.
[215:29] So sometimes that is a thing that happened and that did actually trip me up. So I do apologize for that.
[215:33] But the preview here might not be the actual representation of the colors.
[215:38] So you can see these are all orange. If I switch to Karma CPU, there'll be half and half, which is what I was expecting.
[215:49] And if I switch to XPU, I should see a very, very similar result to CPU. And there we go.
[215:58] So it looks like I didn't actually have to modify that too much. But if I did want to adjust the distribution, I could get more...
[216:08] Of I believe the orange color by pushing that to one side and I can get more of the blue by pushing it to the other side.
[216:19] And I kind of do like the blue. I kind of like that a lot actually. So maybe I'll leave it mostly blue.
[216:28] And I can actually flip those to flip the ramp and give me a different value.
[216:34] But I'll leave this here. That'll be the color incoming. And I'll connect this back to...
[216:45] Actually, because I've now merged this, I want this to go into the darker color as well as the blend color here.
[216:55] So this was me using the concrete texture from the previous video to get some variation on the light and dark patches of my concrete.
[217:07] And if I connect this standard surface to the output, we'll now see I have these concrete balls that are falling down.
[217:19] And if I want a little bit brighter blue, I can modify that here. And that's the other thing why it's nice having just a single color coming in.
[217:35] Alright. I think that's good. One thing we might want to do, and I'll let you make the decision on how you'd like to do the look development.
[217:44] If we wanted to add some transmission, we could make these glass so I could plug transmission color into the diffuse.
[217:58] And if I increase the depth, that will mean the light has to go further through the surface in order to catch the full color of the object.
[218:15] So the higher I make this, the more clear they're going to be.
[218:23] And we could find a glass material. And the glass is also going to have a big influence by the roughness as well.
[218:33] So it looks like we might have these a little bit too rough. So if we were going for glass, maybe what I'd want to do is I'll say this is concrete.
[218:44] Roughness, glass, roughness. Maybe I'll put that in specular. And instead of 0.5, 2.8, I'll do 0.1, 2.2.
[219:02] Maybe even 0.02 on the low.
[219:06] So then we'll see we've got some nice glass. And I actually kind of like this because we get the coloring coming through our materials.
[219:15] But one thing this will be a little bit longer to render than if we did our...
[219:24] Excuse me, I'm thinking about some other things. If we did our concrete, this would be a little bit different.
[219:30] So this is going to take a little bit longer to render. But for our purpose, perhaps it is okay.
[219:35] And then maybe for this darker color, we don't want to go quite as dark if it is glass.
[219:45] So if I let it think for a second, we'll now have the glass a little bit brighter.
[219:52] And if I enable that again, that's going to bring that a little bit darker, which did look good for the concrete.
[219:58] But maybe if it's glass, we don't want that quite as dark.
[220:03] I actually like this a lot.
[220:08] I think this looks really good. I might even want to get some more roughness on these.
[220:17] If I did want less motion blur, I can manually decrease the velocity based on the same kind of way I tested my initial motion blur and increased that velocity.
[220:28] Just with that wrangle. That's probably the most straightforward way to fix it.
[220:34] Perhaps we could even try subsurface.
[220:38] So I might connect my subsurface, this same blend colors into my subsurface radius.
[220:50] I'm going to set transmission to zero.
[220:58] I'll put it inside color, actually rather than radius.
[221:28] And the lower I make this, I can make this pretty small, actually.
[221:36] The less the subsurface value is going to be happening.
[221:41] And if I do want to tint this, perhaps I can make this 0.1 and actually plug this as well.
[221:49] The radius is going to be how far each individual color can scatter through the object.
[221:59] So maybe I'll mix a little bit of subsurface and transmission.
[222:30] Maybe I want a little more orange coming through.
[222:42] So what I could even do is I could do a color correct on the foreground here.
[222:48] Maybe 1.2.
[222:54] Maybe Cam I could go 1.2 as well.
[222:56] I'm going to go back to my look development camera to make sure I get the resolution set by my render scene.
[223:26] I can go to settings, and if I go U, U to go up, I can go to look to have camera right here.
[223:39] And shift click to set my focus distance.
[223:48] So there we go.
[223:51] So enter to get the gizmo active with my camera selected here.
[223:59] And we are getting quite a bit of motion blur.
[224:03] The motion blur is also going to have a huge effect based on the scale of the scene.
[224:09] So in this case we've got a relatively large, this is a 20 meter by 20 meter fall for these cubes.
[224:16] So they are moving very fast.
[224:18] So maybe let's do, ignore that error.
[224:24] Maybe let's leave test motion blur here and I'll say this is scale, motion blur.
[224:31] And I'll do 0.4.
[224:34] Just to scale it a little bit lower than it was.
[224:39] Jump into render my scene.
[224:42] And if I preview this here.
[224:49] And maybe for now I'll actually decrease or disable motion blur entirely and disable it on my geometry.
[225:05] Technically this is now setting it globally down here and this is setting it per object.
[225:11] So I could just set it here but I want to go and make sure my glass isn't too frosted.
[225:28] And you can actually see we've got some nice results here.
[225:32] So I really do like that.
[225:34] See what happens with one transmission and zero subsurface.
[225:46] I think I'd do like the 0.7.
[225:49] So I'm going to do 0.8 for transmission.
[225:53] One for subsurface.
[225:56] And I can decrease the depth to have more of the color.
[226:05] So again, the higher the depth the further the light has to travel in order to pretty much become the full color.
[226:13] And maybe now in this case.
[226:20] I can decrease the normal.
[226:25] I can decrease the depth.
[226:38] I maybe actually want to disable my depth of field as well.
[226:55] Alright, I think this might be good.
[227:09] Let's do a couple different renders or snapshots of what it's looking like.
[227:20] But I will actually re-enable depth of field and re-enable motion blur.
[227:34] I'm going to go to look to have one and I want to reset my focus distance to be this sphere here.
[227:42] I'll go to...
[227:44] I'll show you how I'll let this finish out before I take a snapshot.
[227:48] And I'll go to look to have camera.
[227:52] Which is this one.
[227:54] Make sure I've got my gizmo selected and then shift click to set the focus distance.
[228:00] And then we'll go down.
[228:13] One we already set.
[228:15] Two.
[228:17] Shift click.
[228:25] Which it looks like it's not changing.
[228:30] And now my focus might actually be two...
[228:47] I was looking at that I thought was not focusing.
[228:52] To look to have camera two.
[229:22] I'll go to snap shot of that one here and I'm going to say glass zero one.
[229:30] Glass zero two.
[229:33] Glass zero three.
[229:35] Glass zero four.
[229:37] Alright welcome back.
[229:39] Apologies for that quick cut.
[229:41] I've got to rename my render here to glass four.
[229:45] And we're going to open it up and just take a quick look at what we've got here.
[229:49] So we've been making some great progress.
[229:52] We have now actually completed the materials for at least for now.
[230:00] So that's going to be the end pretty much of this video here.
[230:04] We've made a lot of progress since we've got our first set up here.
[230:10] And I'm liking this a lot so I'm very very happy with how this is turning out.
[230:14] And what we're going to do now is actually end the video.
[230:16] And then in the next one we're going to come back and get a little more creative with our lighting to hopefully set up some more intentional shots.
[230:26] That might make it into the final film for this mini course.
[230:30] So awesome.
[230:32] That'll be the end of this video and I'll see you in the next one.


### Lesson 12: Houdini - Karma Lighting [230:39]
**Transcript (timestamped):**
[230:40] Welcome back and welcome to the next section of this Houdini mini course.
[230:44] If you are just joining us, we've done a lot of work actually.
[230:50] We've created this whole setup 100% from scratch.
[230:53] So if you're interested in following along, then download the project files below and go ahead to the start of the playlist to start with the project.
[231:01] So what we've done in the last couple of videos is we set up this whole simulation and all the modeling, everything, the rendering.
[231:11] And then we've done the materials for the backboard or pegboard and actually just completed in the last video, our nice half transmission, half subsurface material for these glass balls that are actually falling down.
[231:29] And we did a little bit of changing from the concrete materials actually to the glass ones and then randomized which ones got the orange and which ones got the blue.
[231:39] So it's done quite a bit here.
[231:41] And what we're going to do now in this video is we're going to make our lighting a little bit more interesting and start thinking about some of these specific shots that we actually want to capture.
[231:54] So very first thing we're going to do, I'm going to go wide to this hero cam, which is this one right here.
[231:59] I might even even out some of these values to make sure we're looking at it from straight on.
[232:20] And then let's do a quick preview of our lighting.
[232:23] So in this specific shot, actually, let's do a really quick setup.
[232:36] I do want it a little bit more interesting of a background material.
[232:39] So I am going to duplicate the textured pegboard and I'm going to say textured background, hit you to go up, auto fill, assign my materials and I'm just going to assign the backdrop.
[232:56] Actually, rather here, instead of simple backdrop, I'm going to go to textured background.
[233:09] And we'll also need to modify the tiling.
[233:19] And we'll need to modify this main color to make it a little bit darker.
[233:26] But that should be fine for now.
[233:28] You are welcome to take this in any direction you see fit for your look development.
[233:34] And maybe actually what we could do is decrease that contrast.
[233:42] So we're still getting this light value in the back, but still with a little bit of variation.
[233:49] So that's going to be good for our background.
[233:51] And now let's go.
[233:53] I'm going to name this L underscore HDRI.
[233:56] And I want to also set up these LPE tags, dollar, OS, which is going to set one based on the operator string, which is just the name of this node.
[234:09] And we haven't followed along with some of these videos in the past.
[234:12] If I go to image output down to my AOVs, I can split my beauty pass by the lights.
[234:20] And now I'll be able to start looking at the individual contributions of these lights as well.
[234:26] So for now, this was little mini point light I had created while testing some materials.
[234:33] So let's do, let's do an area light.
[234:40] And I might want to get, we didn't really think about lighting here, but I think since these are falling down, I might want to have some kind of cool barn door light that almost looks like a goba.
[234:55] Kind of split across this side to give a little bit of contrast in the lighting.
[235:03] So I'm going to go area light.
[235:05] If I disable my HDRI, I can just preview the area light.
[235:09] And I'm going to first uncheck my hero cam and place this in a position that feels reasonable.
[235:19] So I'm going to normalize the power, increase my intensity, increase my exposure.
[235:26] And let's get it lined up just so it's facing our object.
[235:32] And then we'll jump back inside the hero cam.
[235:36] And if we have this area light selected and enter, we can see these placement modes.
[235:41] And the one I like to use most is shadow.
[235:43] So I can go back to karma XPU.
[235:49] You can see our light must not be strong enough.
[235:51] I slowly increase this up. We can see it coming back.
[235:56] Maybe I'll do seven, but I could select an area and then select an area on my backdrop.
[236:03] And by shift and left clicking, I'm moving the shadow location can by regular left clicking.
[236:11] I am moving the target first location here.
[236:15] And we can pretty much place exactly where we want our shadows to be.
[236:18] And that's actually kind of a cool shot.
[236:23] That's a little bit of the rim light.
[236:27] So maybe we'll have two lights here.
[236:30] We'll do one that kind of goes through the center.
[236:35] And I can even control and middle mouse or control and even on left click to push this further away.
[236:43] And let's go to the shaping.
[236:46] I'll do spotlight.
[236:52] Let's bring up some of the barn doors until this closes on half of my object.
[237:01] So I'll go left barn door and right barn door.
[237:04] Maybe point four or five.
[237:34] And I'll find a value that's nice and giving me a little bit of contrast here, but also not too much.
[237:54] Because this will also only just be a single part of my lighting rig.
[237:58] So I've got one nice little highlight coming across there.
[238:02] And if I have my display flags set on karma render settings, I can look now at the individual contributions, which I actually have to assign a LPE tag to this one.
[238:13] I'll do dollar OS and this will be L area.
[238:18] This will be rectangle.
[238:29] So now I've got this area contribution, this one as well.
[238:34] Maybe I'll decrease point eight, my HDRI.
[238:42] And I do kind of like how the colors shining through these objects here.
[238:47] So I'm going to duplicate this one again one more time.
[238:50] And this is going to be area rim.
[238:51] For now, I'll disable these two HDRIs or these two other lights.
[239:01] And I want to keep my display flag on my render settings so I can actually see this split per LPE.
[239:07] And now in this one, I want this to be a little bit bigger.
[239:10] I'll actually uncheck the spotlight.
[239:13] I want to make sure I've got my gizmos set.
[239:15] And I'm going to use my shadow placer again to place this as a rim light.
[239:31] So what I'm trying to do is find a spot and I could even exit this if I want to see a little bit better exactly what's going on.
[239:40] This can be a little bit closer.
[239:43] And the reason I want it closer is I want a nice fall off from the top to the bottom.
[239:52] So I kind of do like this a lot.
[239:59] And actually, maybe I want to bring this one a little bit closer.
[240:03] So I'll go back to hero cam, select my area light, enter Karma XPU.
[240:12] I can go to shadow, if I disable the rim light.
[240:23] I'll actually manually place this.
[240:25] Make sure it's a little bit closer.
[240:27] Look to have camera, which actually was hero camera.
[240:36] And now I may need to decrease the size there and that'll be okay.
[240:46] It's not too much of a difference, but a little bit.
[240:50] And if we enable our area rim light again and decrease this rectangle and even increase or enable actually our HDRI,
[241:02] we'll be able to see a nice, hopefully interesting lighting setup.
[241:06] So we're getting some shadows up there.
[241:13] Might be overall a little too bright.
[241:15] I'm going to decrease the HDRI light.
[241:19] I'm liking this value here.
[241:33] Maybe increase that middle and I might even want a little bit of a left light as well.
[241:39] So HDRI, this one here, the area rectangle, the rim and let's do left.
[241:55] And if I disable these three and make sure I've got my color and set to shadow.
[242:09] And I kind of want to just catch the highlight here and let's slowly enable these so we can see them together.
[242:23] So I've got a little highlight on the left, HDRI here, the top light, which I think looks pretty interesting.
[242:33] And then this area light kind of in the middle.
[242:40] So I'm relatively happy with that lighting setup.
[242:44] I'm sure I could fine tune it for some of these individual cameras.
[242:50] So maybe let's try to do...
[242:57] Just see what these are looking like around here.
[243:10] If I was from this angle and I kind of want to have a lighting setup that is relatively solid for every camera I'm going to be looking through.
[243:22] So right now I'm thinking I want a little bit more highlight separating this from the background.
[243:28] So if I go to the area rim...
[243:34] Oops, I don't want to move that.
[243:38] Area rim light, hit enter, go to shadow.
[243:47] And I want to preview only the area rim.
[243:51] Camera one.
[244:07] And we may actually need to modify some of these for the individual shots.
[244:14] Which also if you are looking across the scene, kind of the rim lights are not going to be the same whether you're looking to the right or to the left.
[244:23] So it's reasonable you might need to modify those.
[244:44] And I believe actually I moved the wrong one.
[244:50] Which is why I kind of like turning off the ones and only looking at individual ones.
[244:57] So area rim should be coming from the top.
[245:00] So I'm going to select this one, enter, shadow, and place it from the top.
[245:08] If I select one of these pins that sticks out a little bit, I can kind of catch this lighting a little bit.
[245:15] Area left, coming from the left.
[245:19] HDRI.
[245:23] And then the area rectangle here.
[245:28] I would say the area rectangle, maybe a little bit brighter.
[245:45] What we could actually do, rectangle, enter.
[245:52] And again you're welcome to art direct this lighting however you see fit.
[245:58] What I'm going to do is decrease the outer a little bit.
[246:03] And I'll turn off the dome light as well as the left and right rim light.
[246:10] And then for the inner.
[246:31] I want.
[246:39] And this softness or this angle is going to kind of reduce it everywhere.
[247:09] And I'll enable this one again.
[247:14] You're actually enable the, this one again.
[247:20] And then I'm going to go ahead and do the same thing.
[247:25] And then I'm going to go ahead and do the same thing again.
[247:30] And then I'm going to go ahead and do the same thing again.
[247:34] You're actually enable the, this one again.
[247:49] And I'll actually leave that there. I don't need to modify these too much.
[247:54] And perhaps actually that might be too many.
[247:59] So I can disable this one.
[248:04] And maybe bump this up.
[248:06] I did add one modified it and I don't really like it.
[248:10] So I'm not going to leave it.
[248:12] But sometimes with lighting you are testing a lot of things and just making sure that
[248:18] changes or random changes to see what works.
[248:31] But all right, I do like this.
[248:33] So I'm going to render out a couple higher resolution previews.
[248:38] And then I'm going to go ahead and do the same thing again.
[248:43] Let's do, maybe let's actually place our main cameras.
[248:55] So these were just for look development.
[248:58] Perhaps we'll connect these.
[249:00] So we're now removing the look development cameras from our setup.
[249:13] Okay.
[249:25] I'll have one here.
[249:28] I want to see this top corner in this area.
[249:59] And then maybe some of these.
[250:02] And if we actually go to an early frame, we'll see that they are all concrete.
[250:20] And this looks like it's not the first one to fall, but it is one of the early ones.
[250:28] So perhaps we'll leave one here.
[250:31] And then we'll come back to the next one to refine a little bit more the camera.
[250:39] But I'll take a snapshot preview.
[250:49] I'll let this one load out.
[250:52] A quick snapshot.
[250:56] And then hero cam looks like we did move it.
[251:11] So let's even these out again.
[251:31] There we go.
[251:42] All right.
[251:47] I'm going to say this is, I'll just take glass zero or five to continue the naming convention.
[251:53] Zero six.
[251:55] And you don't really have to name these snapshots.
[251:57] They are helpful if you end up making a bunch.
[252:00] So you can remember which ones were which.
[252:05] But if we are just slowly making progress, it is fun to see how far we've come since this first render all the way now to this later render.
[252:18] So awesome.
[252:20] I'm currently liking this a lot.
[252:26] Got some good colors.
[252:28] I am liking the oranges and the blues.
[252:30] And I think this is going to turn out to be a cool final result.
[252:34] So it's going to be the end of this lighting section.
[252:37] And then in the next one, we're going to come back and finalize the cameras and perhaps prepare her rendering in the video after.
[252:43] So all right, I'll see you in the next video.


### Lesson 13: Houdini - Camera Setup + Animation [252:49]
**Transcript (timestamped):**
[252:50] Welcome back and welcome to the next video in this Houdini mini course.
[252:55] We're going to pick up from exactly where we left off.
[252:58] And this was the final lighting setup we had created.
[253:02] So if you're just joining us, we've been creating the simulation of these balls slowly falling down our little animated pegboard.
[253:11] And we've been doing this from scratch over the course of this whole course.
[253:14] So go ahead and start to the beginning if you'd like to follow along.
[253:18] But in this video, we're going to set up some camera animation and then also get our scene playing back a little quicker.
[253:24] So I'm going to minimize this here and we're just going to get started.
[253:27] So this is the final result we had at the last video.
[253:30] We did a little bit of lighting and then placed slightly a little bit different our camera locations.
[253:37] But now if we click play, we can see that our very simple scene is moving very slowly.
[253:44] And this is going to make it kind of annoying for us to be doing our camera animations because we're going to have to wait for all of this to cook in order to add.
[253:53] In order to actually complete any flip books.
[253:56] The first thing we can look at is what is time dependent here and try to fix those.
[254:01] So we actually don't have any time dependency on our static board.
[254:06] So we should be able to remove that.
[254:09] And we're going to jump to where that is and that is actually this one right here.
[254:13] So I'm going to use a time shift and delete channels and I'll leave this at frame one.
[254:21] So this is no longer time dependent.
[254:27] And I can even actually do that for the static marbles as well.
[254:40] And actually I should not do that for the static marbles because I need to have which ones are falling.
[254:52] This will be fine for our animated.
[254:54] We could actually cash these out to USD which would likely be the most effective way to have these all loading in.
[255:06] So maybe we should.
[255:11] Maybe we'll set that up.
[255:12] So let's try that.
[255:14] So I'm going to go.
[255:15] I've got my pegboard here.
[255:18] My animated objects here.
[255:22] And I'll actually just set up to do a very simple setup for our USD.
[255:29] And we'll actually use the file cache, which is a nice tool built by side effects that includes some USD setup here as well as a setup for sub layering or bringing back in the USD file that we save.
[255:44] So set this up.
[255:46] I'm going to say this is balls and our marbles actually animated.
[255:55] I want to frame range.
[255:58] And I will leave this in USD.
[256:01] It's not a simulation.
[256:05] But before I go, I'm going to set a save path for these.
[256:10] I want to set it to dollar hip slash USD slash marbles static dot USD.
[256:31] I want to set one for marbles animated.
[256:39] And that is actually all I will set.
[256:41] I'm going to say marbles all for the file cache frame range is fine.
[256:45] And I will save to disk.
[256:54] And this is not by any means the most efficient way of saving this file to disk.
[257:00] But this is going to be doing it's going to be duplicating the geometry on every frame.
[257:04] And this file cache is going to be heavier than it needs to be.
[257:07] But without having to dive too much into USD, I just want to show you the simplest way of setting this up.
[257:22] And now if I click play, you can see we have this moving quite a bit faster than I did before, which is perfect for what we want.
[257:31] And we'll do a very similar thing with these as well.
[257:36] So I'm going to do another file cache.
[257:42] I'll put it here.
[257:43] I'm going to say this is peg boards.
[257:47] I'll set the save path for static.
[257:59] And I'll do the same thing for animated.
[258:08] I'll set this to frame range peg boards all.
[258:11] Hip USD OS is fine.
[258:14] And I'll save this to disk.
[258:16] And again, this is going to be duplicating this geometry on every frame.
[258:26] So we have this loading in now correctly and have this playing.
[258:31] And if we go back to our graph branches, we can see our simulation or rather our animation is playing back much, much quicker.
[258:42] Perfect.
[258:44] Just me the very first thing we want to set up.
[258:46] And now let's take a look at some of these cameras.
[258:56] Maybe very first one hero cam.
[258:59] We could do a slow zoom in that might look kind of nice.
[259:08] So I'll go to the early frames, lock my camera.
[259:13] I'll zoom out a little bit.
[259:15] Maybe 72, 3, 0, 1.
[259:21] I'll alt left click and alt left click.
[259:24] And then if I accidentally set this not on frame zero, I can middle mouse button and drag.
[259:36] And then let's set this movie to 65.
[259:42] I'll alt click just to set a key frame on X only.
[259:49] Apologies for that quick cut.
[259:52] We just finished setting up the slight dolly in for our camera.
[259:58] And what I want to do actually is on these key frames, I'm going to type linear and tab to jump to the next one.
[260:07] Because I want these all to be linear key frames.
[260:12] And there we go.
[260:14] And we can also open up our animation editor if we did want to finesse these a little bit more.
[260:21] But for the purpose of what we're doing, I want to stay relatively simple with the animation just so we can get something done without spending too much time doing it.
[260:32] So I've got hero cam here.
[260:34] The other one I might want to set would be, I'll go back down towards the end here.
[260:42] And your camera positions may be slightly different if you had not been following along and moving every single camera.
[260:50] But let's go.
[260:53] Perhaps rather than looking just for animation.
[260:59] Let's see what these are looking like rendered.
[261:04] If we were making a more intentional shot with some specific animation, I can hide my scene view or my grid view rather here.
[261:14] Then we might want to be planning out some specifics.
[261:20] I kind of want to just find some cool angles and maybe I'll even render the same animation from a few different angles.
[261:34] So this is camera one.
[261:37] This is an 85 millimeter camera.
[261:39] I'm going to zoom all the way back to the start.
[261:44] And I'll set my focus.
[261:47] Perhaps I'll go to my camera tools.
[261:50] It's just like camera one shift left click to set the focus distance, which in that case is 35.
[261:56] Go all the way down to 240.
[262:03] And I'll set it on the end.
[262:05] And then I will need to add a f stop if I actually want to see this.
[262:12] I also have to enable my depth of field.
[262:18] So in this case actually 0.2 is probably too strong.
[262:26] 0.5 might be okay.
[262:30] And let's do a very slight animation just to have movement.
[262:35] So I'll go all the way back to frame one.
[262:43] And I'll set a keyframe.
[262:56] And maybe let's zoom and move a little bit to the left.
[263:06] Actually rather let's go.
[263:08] I'm going to undo that.
[263:14] So I do have camera one here.
[263:26] Maybe I'll actually just zoom in.
[263:36] Or perhaps I'll do translate.
[263:39] Or I'll do linear.
[263:43] Linear.
[263:45] Linear.
[263:47] Skip to the end.
[263:51] And also another keyframe.
[263:54] So maybe this one is just moving up.
[264:00] The hero cam is just moving slightly closer.
[264:06] Maybe camera two.
[264:08] Let's first preview what this looks like and then try to find a nice cool angle.
[264:24] I kind of like the split here of this light.
[264:43] Let's actually find the first ball to fall.
[264:48] Which is on that side.
[264:49] But I'll find the first ball on this side.
[264:52] I don't want that side because it's not on the shadow side.
[264:56] Here we go.
[264:58] This might be a cool shot.
[265:01] So to zoom in.
[265:03] I'm going to focus right in between these two here.
[265:11] Kind of looking directly at this center pillar.
[265:19] I might have to go wide or I can go very close.
[265:23] Or very tight angle.
[265:25] I might even stick with the 35.
[265:27] Just to kind of see some of these side ones poke out a little bit more.
[265:34] And then I'll zoom in so the edge is not visible there.
[265:48] Maybe this could be even just a static camera.
[266:01] We'll go to camera three.
[266:12] Another view perhaps of this side.
[266:17] Or actually maybe I'll get one of these, this one rotating.
[266:39] Maybe this will be a 50mm.
[266:48] I like the side angles.
[266:50] Maybe top could be cool.
[267:01] Or maybe bottom could also be cool.
[267:11] This might be cool as we actually see some of these falling down.
[267:25] Let's combine back in these LookDev cameras.
[267:30] I think we might have found some cool angles with them.
[267:36] This top camera maybe LookDev can be a little bit more zoomed in.
[267:48] And I'll hit enter to set my focus on this sphere in the corner.
[267:57] And I'll actually name that cam 04 because I will stick with that for now.
[268:12] This is the next LookDev camera one.
[268:18] Maybe I'll leave cam 05.
[268:34] Those look kind of nice all zoomed in.
[268:41] Maybe I'll delete 5 and this will be my fifth camera.
[268:46] Or rather 6th camera.
[268:49] And then 35 I think is okay but what if I go a little longer.
[268:58] So here I'll cam 5.
[269:04] My focus stop could probably be decreased.
[269:08] So it's a little less depth of field.
[269:11] Maybe I want a little more depth of field.
[269:19] And perhaps this will be a cool angle with motion blur once I enable that.
[269:36] I'll let this thing for one second.
[269:38] And then I'm going to make one quick change to actually every single camera.
[269:45] So I'm going to go to hero cam.
[269:47] I'm going to right click copy parameter.
[269:50] And then I'm going to set the aspect ratio on these other cameras.
[269:57] Right click and paste relative reference to match hero cam.
[270:03] And I actually want to go to maybe 20 by 9.
[270:14] Just to get a little bit wider of an angle.
[270:20] Let's go to hero cam.
[270:22] Now I'm going to have to decrease that to make sure I can actually see my whole shot.
[270:42] And then I'll do a nice high resolution render.
[270:50] I'll switch back to karma to reset this and hopefully have it render a little bit quicker.
[270:59] Alright welcome back.
[271:01] Houdini is now back to responding.
[271:05] So I am doing one quick preview again.
[271:09] Slightly higher resolution.
[271:12] Maybe 124 samples.
[271:25] And actually I want to get my regular speed motion blur.
[271:31] So I'm going to jump into my peg setup where I've done this scale motion blur where I multiply velocity by 0.4.
[271:38] And I'm just going to disable this.
[271:45] I'll go back to my little sketch I had made.
[271:50] Because I like this ball falling off.
[271:52] But I think from this wider angle.
[271:57] It will be cool to see it with the motion blur.
[272:02] And then I'll let this finish out.
[272:10] And then after this we'll come back in the next video to actually set up our rendering.
[272:16] So again as you follow along with this course.
[272:19] So you are welcome to modify the cameras.
[272:22] Set up your own simulation kind of however you see fit.
[272:29] And we might actually modify the size of our simulation board in a bonus video.
[272:36] But we'll see that once we get there.
[272:38] So high res preview.
[272:41] I'm going to right click color correction.
[272:43] Go to aces.
[272:45] And we've got a nice render going here.
[272:48] So I'm excited with how this is looking.
[272:50] We've got our motion blur.
[272:51] We've got some cool refractions coming through the glass.
[272:54] We've got some nice highlights.
[272:56] Some nice colors here and some bouncing of this light.
[272:59] So I'm very happy with how it's looking.
[273:01] And again a massive improvement.
[273:05] We've already come so far.
[273:07] So awesome.
[273:08] That's going to be the end of this video.
[273:10] We'll come back in the next one to set up our rendering.
[273:12] And we are making great progress.
[273:14] And almost towards the final result.
[273:16] So I'll see you in the next video.


### Lesson 14: Houdini - Karma Rendering [273:22]
**Transcript (timestamped):**
[273:23] Welcome back and welcome to the next video in our Houdini mini course.
[273:27] We are picking up from exactly where we left off.
[273:29] Which was the look development.
[273:31] Or rather actually the camera animation from our setup here.
[273:37] And we did some very very very basic camera animations.
[273:40] But we did explore a little bit what our scene might look like.
[273:44] So I'm happy with this final preview here.
[273:48] And really all we had was a zoom in.
[273:50] And we actually didn't get a flip book.
[273:52] But we're going to use this lesson now.
[273:55] To set up the main render network for rendering out each of these individual shots.
[274:02] So I've got a bunch of different animated cameras here.
[274:06] And we're going to go from my really great render.
[274:10] Render settings down here.
[274:11] And I'm going to branch out.
[274:13] I'm going to say this is prep.
[274:15] Our renders.
[274:17] And what I want to do here is I'll actually create a new render settings node.
[274:21] And I like to use these to define the file save path of where my image is going to go.
[274:27] And this will give me a warning saying I'm overriding these render settings.
[274:32] Which is fine in this case.
[274:34] And I don't mind doing that.
[274:36] But just be aware that it might give you that warning.
[274:38] So I've got hit render os dollar os.f4.
[274:43] This is kind of a standard render path that I like to use when working.
[274:47] Also this is main.
[274:49] Say hero cam.
[274:52] Actually render main cam.
[274:57] And I should actually keep the names consistent.
[275:00] So hero cam.
[275:01] Which in this case is hero cam.
[275:04] Duplicate this again.
[275:07] And I'm going to set this to render settings camera.
[275:12] And I'll go cam 1.
[275:13] And you can see on this one we actually do have some very slight camera animation.
[275:18] So this will be render cam 0 1.
[275:24] And let's find.
[275:29] I had a cool shot I think of.
[275:33] Might have actually been camera 2.
[275:36] So this will be render cam 0 2.
[275:39] And I like this one because I think this ball and this ball.
[275:43] There we go.
[275:44] We're the first to fall.
[275:46] And I think it looked pretty cool.
[275:56] So that's actually all I need to do.
[275:59] Image output I'm going to leave split by LPE tag on all of these.
[276:04] I do want to render in aces for color space.
[276:08] So if you do not have that checked you want to make sure under image output.
[276:12] Output color space output.
[276:14] Excuse me.
[276:15] You've gone and selected aces CG.
[276:18] And a trick that I've done is on karma render settings.
[276:24] You can go to image output output color space.
[276:27] And mine's already set to aces.
[276:29] So you can do is you can change it to whatever you'd like.
[276:32] And if you go to the gear icon legacy presets you can save as permanent default.
[276:37] So then every single time you create a new node those parameters will already be set up.
[276:42] And I believe I've also done that with karma XPU as well because I do a lot of rendering on GPUs.
[276:50] So that's good.
[276:51] I need a USD render Rop here.
[276:56] I'm going to say this is render hero.
[277:00] Cam.
[277:03] This will be render cam one and render cam two.
[277:10] You can see we set those here in our output camera.
[277:21] Cam zero one.
[277:24] And render cam zero two.
[277:26] And you don't actually have to name these USD render raps.
[277:29] They are easier to name because we're going to use a Rop network.
[277:36] But before we do I want to set these all to be karma XPU.
[277:44] And I also want to set these to be single frame range or specific frame range rather and render all frames within a single process.
[277:54] So that's going to have these all render within the current state of Houdini rather than opening up a version in the background.
[278:00] And that's my preferred way of rendering.
[278:04] So render all.
[278:09] And we're going to do a fetch node, which is the simplest setup for doing this fetch in a batch.
[278:18] And we'll duplicate this twice.
[278:23] And I like to offset these on the side because sometimes when they're all lined up in the middle it is a little bit easy or not a little bit easy.
[278:31] Sometimes it is possible.
[278:33] We actually only need two batches just between the fetch nodes.
[278:37] But it is possible to have those lined up and not connected.
[278:40] So there's been quite a few times where I will have maybe 20 to 30 of these set up and I might accidentally forget to render one because it looked like it was connected, but it wasn't.
[278:52] So that's one thing to note.
[278:54] Now what I want is I'm going to drag the render all to the bottom right.
[278:58] So I have this in my bottom right view.
[279:01] This is going to be hero cam.
[279:05] This will be cam 01.
[279:09] This will be cam 02.
[279:11] And if I hit P, I can open the parameters for this panel in the bottom.
[279:18] I'll do hero cam, drag in this render Rop.
[279:22] Cam 01, drag in this render Rop.
[279:25] And cam 02, drag in this render Rop.
[279:29] There we go.
[279:33] And that's actually all we need to do.
[279:37] So I'm going to confirm my frame range 100 to 140, which is actually just going to be the start and end down here.
[279:48] So maybe what I'll do on this camera render settings node, because I actually want to render every camera from...
[279:59] I want to render the whole animation from every camera.
[280:07] So I'll go back to render settings camera.
[280:20] And for now, I will set the...
[280:26] Actually, rather...
[280:29] I want to just test that this is going to work, but I don't want to render every single frame now.
[280:35] So maybe I could by decreasing my path trace samples by quite a bit.
[280:42] And I could right click, copy parameter and paste the relative reference here.
[280:50] If I wanted to use this one, maybe I'll color it a certain color to kind of set the global settings for all the resolutions.
[280:58] And sometimes if you're doing more complex shots, especially with destruction and effects, you might be rendering maybe volumes at a different resolution and then scaling up to save some render time.
[281:09] Or sparks if they're really small particles, you might render at a higher resolution.
[281:13] So it's kind of depends on the specific project.
[281:18] But for now, we're going to do 1280.
[281:21] Make sure that comes out to an even number.
[281:28] And I will maybe just test 100 to 110.
[281:38] I'll jump inside, confirm camera, cam and cam, and I'll select the last fetch node and click render.
[281:50] And I'll wait for my preview to pop up before I pause the video.
[282:10] Here we go.
[282:12] And now this actually hasn't finished half through the renders.
[282:15] What is this done is batched all the hero cam, and it's going to start rendering those all, then it's going to batch all of the camera one, then render those all, and it's going to batch all of camera two, and then render those all.
[282:27] So once this is done, I'll be back and we'll have a nice setup to look at.
[282:31] Welcome back.
[282:32] The animation or rather the render finished.
[282:35] And it turned out to take only a couple minutes.
[282:38] And now we've got our three shots.
[282:41] So we've got one here.
[282:43] And this I actually really like this.
[282:47] I just noticed that it does a cool bounce between those objects.
[282:52] So perhaps I could try to make a new camera there.
[282:55] But what I decided is I don't like this angle here of this camera.
[283:01] I think it's too static.
[283:04] And it is static, but the shot doesn't feel interesting to me.
[283:08] So I'm going to remove that one.
[283:10] I do like this one here.
[283:13] I think this will be cool for everything.
[283:15] And I think this little situation of where it bounces on this side and then goes to the other board here, whatever we call it.
[283:29] Looks pretty cool.
[283:31] So I'm going to stick with that.
[283:32] And what I want to do now, maybe I'll just come up with one more camera.
[283:37] So I've got one here on the left.
[283:40] This straight one, maybe it would be cool, but maybe I won't render that.
[283:45] Let's go back and do hero cam.
[283:50] Cam 1, which I did like.
[283:56] I got to render settings, cam 2.
[284:01] Maybe cam 3 would be more interesting.
[284:09] So I might even, I'll just change this right now.
[284:15] And I want to do this so it overrides the images.
[284:18] So camera 3.
[284:22] Or I guess it doesn't matter that much.
[284:25] I don't mind having extra cameras.
[284:27] So I'm going to change this one fetch camera 2.
[284:30] And if I change this to 3, I'll have 3, 3 and on my fetch down here, I'll be getting 3.
[284:37] And now I've also selected 3.
[284:41] So let me go to camera 3, select my lock icon and I just want to move this around.
[284:56] Maybe I'll have this angle here.
[285:15] Getting a little bit of a weird results on the placement of my camera.
[285:29] Alright, well it's doing some odd setup.
[285:32] So I'm going to set my display template flag on cam 3.
[285:50] Not sure why that's happening, but I will ignore it for now.
[286:00] And let's do a quick render preview.
[286:02] Actually I'll go down to select my render cam all the way down at the bottom.
[286:30] Alright, well I'm not liking that at all.
[286:31] I'm going to restart Houdini and hopefully have that issue fixed.
[286:34] Alright, welcome back.
[286:35] Apologies for the cuts.
[286:37] I restarted Houdini and now it looks like I am back to working as expected.
[286:44] Whoops.
[286:46] I'm going to find this placement for the camera here.
[286:53] And I liked, I didn't really like this one actually that much at all.
[286:59] I did like the front one and I did like this side.
[287:06] And I actually do really like this one here.
[287:08] I kind of like that we can see the back side.
[287:13] So let's do, I'm going to go back to my full frame range of 1 to 240.
[287:23] And I'll go camera 3, skip back to frame 1.
[287:34] And maybe I'll do some kind of interesting movement like this.
[287:39] So I kind of want to preview some of these balls at the very beginning or the marbles at the top.
[287:49] Or maybe I don't.
[288:01] So I'll set a keyframe on translate and rotate here.
[288:05] And again, I'm doing very simple animations.
[288:18] And I'll set linear.
[288:25] I'll go back and do that as well.
[288:27] I could do that in the animation editor, but I'm fine doing that right here.
[288:37] So not a very exciting animation, but it will be good for the shot I'm trying to make.
[288:48] So I like that one.
[288:55] And what even might be cool is one more shot of the top of them all falling.
[289:08] So I'm going to go back to Vulkan and zoom out.
[289:14] And I'll find maybe a wide angle for 35.
[289:27] And let's see what this will look like.
[289:34] And maybe it will be cool if we had 24, so even wider angle.
[289:52] I'll just hit control Z to undo that.
[289:59] So I want to see how this looks.
[290:03] I think I like this angle.
[290:05] I do want to be able to see the balls at the start and see them all falling down, which I think looks really cool like this.
[290:15] So I want to make sure my camera frame is visible here.
[290:22] I'll do 38, set a keyframe, and set one on Y as well.
[290:36] And then maybe 33.
[290:45] And then maybe negative 4.
[290:51] Maybe negative 2.5 on Y.
[290:57] And then I'll set these both to linear.
[291:08] I got to click here to change and select my bezier.
[291:13] And now here we go.
[291:14] Linear and linear.
[291:17] Click linear.
[291:21] And click it one more time to see the interpolation.
[291:24] And then linear is good for that one.
[291:27] So I think this might be good.
[291:30] So if I go back down here to render settings, camera.
[291:43] Which it looks like those are disconnected now.
[291:46] So I'm going to put those back in to make sure I can actually have those in my scene graph path.
[291:53] By the time I have my camera render settings, I've got one here, two here, three.
[291:59] And we do need a fourth actually because we just created a fourth.
[292:03] So that already actually named it correctly.
[292:06] I just need to change the camera that I'll be selecting.
[292:09] And then I'll need to add in my Rop network, which I could actually close this out.
[292:16] If we just want to see where it was here in the Rop network, there was this one we had set up earlier.
[292:26] So I'll go camera four and just make sure that is render cam four, which is this USD render Rop right here.
[292:37] All right, I think that's good.
[292:44] Maybe I'll do a flip book of all of these surrender hero cam.
[292:54] I'll actually flip book these off camera and then I'll come back once I have one for this one, then that one, that one and that one.
[293:01] So I'll be back in just one second.
[293:04] Welcome back. The flip book's finished and we've got all four shots here.
[293:09] One thing we will notice is that the blue balls happen to be invisible once they fall.
[293:18] So you can see right here this one in particular disappears on frame 112.
[293:23] But if I go back to my render view and go to frame 112, you'll see 111, it's visible 112.
[293:32] If I go to 111 and preview my render, we'll see it is a concrete ball.
[293:40] And then if I go to 112, we'll see it looks like it actually switched to a glass ball.
[293:46] But the idea is the same that some of these are invisible and it actually looks like the orange ones are invisible, which is interesting.
[293:59] But the important thing is they are visible in the final render, which is what matters.
[294:05] So these are going to be the four shots we will move forward with for the rest of this mini course.
[294:13] One very important thing we want to double check.
[294:16] And I'll actually do that right here.
[294:18] I'm going to create a compositing network and this is going to be test composite or I'll just tell it or name it.
[294:27] Excuse me, test comp.
[294:29] I'm going to jump inside, add a file node and I want to render or rather I want to bring in the test renders I had done earlier, which is hip slash render.
[294:43] And I'll grab my render hero cam.
[294:45] And then I do want these all selected as a sequence.
[294:49] So if I check this icon show sequences as one entry is going to let me automatically select the sequence.
[294:57] And if I go to a frame here and switch to my viewers composite view and so this is the ACEs.
[295:04] We can now see my render and the important part I want to do add AOVs from file.
[295:10] And I want to make sure that we have our individual contributions from each light.
[295:18] And it looks like we do.
[295:20] So this is the important part that I want to make sure we have because if we did want to make any changes, we could layer these back together.
[295:31] And one thing we'll also notice is that the AOVs are not denoised for our purpose that is fine.
[295:38] Because we're actually mostly going to be working just with this beauty render.
[295:42] And we might do some slight rebalancing perhaps of the intensity of our lights, but we maybe won't.
[295:53] So we'll figure out how that goes once we get there.
[295:55] So I'm going to go back to my scene view, make sure I've got my camera camera.
[296:01] It looks like these are all good to go.
[296:03] And I'm just going to double check one more time.
[296:06] So I got to do a new viewers network view, which is right here.
[296:16] And I want to jump inside.
[296:18] This is pinned, which is exactly what I want.
[296:20] I'm going to drag this render null or render all, Rob network right here.
[296:26] And I want hero cam, make sure I've got hero cam, which is correct.
[296:30] Cam one is render cam one, which is this one, correct.
[296:34] Cam three, cam three, correct cam four and cam four, correct.
[296:39] And I've got render all frames with a single process checked on karma, XPU checked on render frame range checked on.
[296:48] So I'll go inside this Rob network.
[296:51] And I'm going to render these.
[296:53] So I have the whole sequence for everything.
[296:56] And one thing we will be aware of is this is currently a low resolution render.
[297:02] So actually if I interrupt, we'll see I've got 1280.
[297:14] It looks like.
[297:19] Okay, that was an interesting said zero for the height for a second.
[297:24] But this is a low resolution render with a low quality samples.
[297:28] So not enough samples to clean it up.
[297:30] But we are testing our shots.
[297:33] So I'm going to render this and we'll come back in the next one to set up our final production quality render settings before we kick that one off for the final file and the result of this project.
[297:46] So awesome.
[297:47] That's going to be a quick pause actually, because I'll come back in the same video once the render's done and we'll keep going.
[297:55] So I'll see you in just one second.
[297:56] Welcome back.
[297:57] The renders took about 45 minutes, but I actually stopped them a little bit early because I didn't really need to see them finish up.
[298:07] In particular, I did stop this one early.
[298:10] And actually one thing I did have as well is I accidentally forgot to uncheck the camera render to.
[298:24] Or maybe I didn't.
[298:25] Maybe I actually did already.
[298:27] So we've got HeroCam, Cam1, Cam3, and Cam4.
[298:32] It looks like I actually didn't forget that.
[298:34] So I think we're all set.
[298:36] So I'm going to close this one out.
[298:38] And what we now have is the rendered and animated preview for all of our shots.
[298:50] And I think it actually looks pretty good.
[298:54] So if I can open these back up again, we've got this camera here, this camera, which might actually be my favorite, probably the bottom one or this one here.
[299:06] But I'm definitely happy with how they came out.
[299:08] What we're going to do now is actually set up our final render settings.
[299:15] And then we will set up the final render for all of these.
[299:21] And we're just going to stick with these four cameras for our final project.
[299:24] So it's going to be a really quick part of the video right now.
[299:29] And I'll choose this camera angle specifically because I think the most noise is visible.
[299:42] So I can see by noise, I actually mean de-noise.
[299:46] So you can see we're seeing quite a bit of flickering on this here.
[299:50] And that's the de-noiser on some of these other angles.
[299:53] It's not quite as noticeable.
[299:56] So if we fix the de-noise settings for this angle and use the same render settings for all of the other ones, we should be set and we should be good to go.
[300:06] So this is HeroCam.
[300:08] Time to go back.
[300:11] It actually looks like Houdini just crashed.
[300:13] So I'll be back in just one second.
[300:15] All right, we are back after restarting Houdini and it looks like we didn't lose anything.
[300:20] What we were about to do is find the render settings for this camera right here.
[300:26] And perhaps we'll do frame 100 to 105.
[300:31] So I'm going to go down here.
[300:33] I'll set this to 100 and 105.
[300:39] Go to render settings, camera.
[300:42] And actually I'm going to switch this to the full resolution, which for our purpose, maybe I'll do 2200 by 990.
[300:55] Actually, I'm going to set the width and then compute height from camera.
[301:04] Or set height, excuse me, compute width.
[301:07] And I want 1080.
[301:10] So 2400 by 1080 is the resolution I'll use for my final renders.
[301:15] And on render HeroCam, I'm going to do first uncheck.
[301:20] Actually, I'm going to go to image output and it's the de-noiser.
[301:24] I want to turn off.
[301:26] And I will quickly render one of these frames and then I'll let it go to see what 16 samples looks like.
[301:42] And commonly, I would not be rendering with the de-noiser.
[301:45] It might be de-noising after.
[301:48] So we're going to do 16 samples.
[301:52] I'll do 64.
[301:55] My expectation is I'll probably need about 200 to 400.
[302:06] And it will depend on the lights we have and the materials as well.
[302:11] So translucent materials, so glass and subsurface materials, typically de-ing a few more samples.
[302:22] And I'll do 256.
[302:26] And I will likely have to render this overnight.
[302:30] So my hope is that if I can get it less than about 30 seconds to one minute per frame with the de-noiser,
[302:39] then that'll be a nice overnight render or maybe an overnight and a half render for the final setup.
[302:51] I'm going to let this finish out to 256.
[302:54] And I think that actually might be the final value I'm going to go with.
[303:00] But I may also want to disable the depth of field on this camera.
[303:14] So I'll just set this to 128 for now, just so it'll render a little bit quicker.
[303:21] And this is just on the hero camera because there's no big depth from the foreground to the background.
[303:34] I could disable depth of field and that might save a little bit of time.
[303:38] But actually now that I'm thinking about it, I might want to have a little bit of depth of field.
[303:42] So maybe I don't mind the extra render time.
[303:52] It looks like I haven't even set that up.
[303:54] So I'm going to grab my hero cam, shift click, set the render distance.
[304:00] Set a very small value.
[304:04] And you can see we've got a nice tight focus here.
[304:10] But I'll actually set this to 2 because I want the slightest amount of depth of field on this shot.
[304:17] And then I'm going to let this finish out into 100%.
[304:32] So right now it's at 50%.
[304:34] And maybe we'll render with 128.
[304:37] I might even do 256 for the final renders, even though that might take a little bit longer.
[304:48] We always have the option to denoise more after the render is done.
[304:55] So this is 128 samples, filters.
[305:02] I can go turn on my denoiser.
[305:08] And this is 128 denoised.
[305:12] And I'll stop my render, open it up, go to aces.
[305:21] Oops, accidentally clicked that once and that flipped them.
[305:24] So I go all the way to the right.
[305:27] This is the noisy version and this is the denoised version.
[305:31] So I think 256 should be good.
[305:45] I'll leave the denoiser on.
[305:48] I'll go to this camera angle as well.
[305:53] And I likely will need to increase this to 256 for all of my renders.
[306:03] I do like this depth of field.
[306:05] Looks really nice.
[306:07] And I want to make sure my motion blur is on.
[306:11] So rendering motion blur.
[306:15] And I likely do not need this render settings geometry.
[306:18] Because I've already set the motion blur down here.
[306:22] But I will toggle that on just to be certain.
[306:27] And if I really want to go see...
[306:30] Actually I'll just leave it as this for now.
[306:32] That should be good.
[306:38] So 256.
[306:40] I'm going to go need no denoiser.
[306:48] And you can even see all of our additional lights.
[307:04] Which actually looks pretty cool.
[307:06] So this is going to be about a minute.
[307:16] Maybe a half per frame.
[307:18] Which should be about 12 to 20 hours for everything.
[307:24] And in my case I would start that this evening.
[307:28] And then have it done by tomorrow morning.
[307:31] Which would be perfect.
[307:34] Alright.
[307:40] I'll freeze this.
[307:42] It's at 57%.
[307:44] So that should be okay.
[307:46] So technically this probably only made it through about 130 samples.
[307:51] I'll go to this next one.
[307:54] Actually I want to enable my denoiser.
[308:04] 256 as well.
[308:11] And I'll even set that on render.
[308:13] Cam 4.
[308:23] I want to make sure I've got my depth of field on cam 3.
[308:28] Which it looks like I do not have.
[308:30] So cam 3.
[308:32] So I'm going to hit enter over my scene view with this highlighted.
[308:35] Go to sampling.
[308:38] Looks like I don't have it turned on.
[308:40] And depth of field with a focus stop of 0.
[308:43] Is not going to show anything.
[308:45] So let's see what I had for cam 1.
[308:48] Which was 0.2.
[308:50] So cam 3.2.
[308:54] And then again it will matter dramatically based on the size and the scale of your scene.
[308:59] So these numbers are not a definite.
[309:02] So depending on how big you made your pegboard.
[309:04] Or how small you made your scene.
[309:06] Then you might need to modify these values.
[309:08] Just to make sure they look correct.
[309:12] So that's good.
[309:16] This is on as well.
[309:19] That's good.
[309:21] And render cam 4.
[309:24] I think that would look pretty cool.
[309:26] With some depth of field.
[309:27] So I'm going to go to cam 4.
[309:29] Go to the view.
[309:31] Or actually rather sampling.
[309:41] I set it all the way at the top.
[309:43] The bottom is decently out of focus.
[309:45] But I will leave this set actually to the bottom here.
[309:51] And I'll set that down to 0.1.
[309:55] Because I want a little bit more depth of field here.
[310:13] I'm going to confirm on my instance velocity here.
[310:24] I'm going to go to frame 102.
[310:43] And just preview this.
[310:55] To make sure I'm getting the motion blur.
[310:57] And I am getting the motion blur.
[310:59] If I zoom in you can see.
[311:09] That is quite a good amount of motion blur.
[311:11] This does look pretty solid.
[311:13] So I'm happy with how it's turning out.
[311:15] So go back to render settings camera.
[311:17] Motion blur is good to go.
[311:21] Switch back to Houdini Vulkan.
[311:24] And I do know this all works.
[311:26] So instead of overriding my lower resolution.
[311:28] What I could do is.
[311:35] I'll do render HD.
[311:42] And changing this is going to change the save path.
[311:45] Because I've set this to be a operator string.
[311:48] If you explicitly set this you might have to modify that manually.
[311:52] But also HD.
[311:54] Cam 1.
[311:56] Render HD.
[311:58] Cam 4.
[312:00] Confirm everything is good to go.
[312:04] I want my frame range back to 1 to 240.
[312:11] 256, 256.
[312:14] Looks like the denoiser is on all of them which is good.
[312:19] I'm going to go rendering.
[312:23] Make sure I've got my motion blur.
[312:26] And my depth of field which is good.
[312:29] And then I'll make sure I've got my.
[312:31] Split per LPE tag.
[312:34] On all of these.
[312:36] Which is good as well.
[312:42] So awesome.
[312:44] That'll be.
[312:46] Actually the all.
[312:48] Or all that we need now.
[312:51] And I will do a.
[312:53] Render of all of these.
[312:55] And then I'll like to be back in the next video.
[312:58] To review.
[313:00] A little bit of a mini compositing section.
[313:02] And we'll keep working towards the final product.
[313:04] So awesome.
[313:06] While I'm on camera here.
[313:08] I'll actually go to render.
[313:10] To start officially.
[313:12] Our final high quality version.
[313:14] Back in the next video.
[313:16] To keep working.


### Lesson 15: Houdini - Final Compositing + Recap [313:20]
**Transcript (timestamped):**
[313:22] Welcome back.
[313:23] The renders have all finished.
[313:25] And I suppose actually welcome to the next.
[313:27] Lesson.
[313:28] In our Houdini mini course.
[313:30] So I had render all of these overnight.
[313:32] I think it took about 17.
[313:34] Or 18 hours.
[313:36] For everything to render.
[313:38] And we've got a nice high quality.
[313:40] Version actually of all four of our shots.
[313:44] So this here is probably my favorite of them all.
[313:48] And I believe cam four.
[313:50] Also might be my second favorite.
[313:52] So some great angles here.
[313:54] Some nice.
[313:56] Good looking depth of field.
[313:58] Everything turned out really well.
[314:00] Perhaps we could have done a few more samples.
[314:02] But for the purpose of this lesson.
[314:04] I think we've actually ended up with a really, really great result.
[314:08] And now by the time we've finished these.
[314:11] Whole lessons.
[314:13] You likely have actually seen the trailer.
[314:15] For the course.
[314:17] Which is also the intro.
[314:19] And the outro.
[314:21] For this.
[314:22] Video that you're watching now.
[314:24] And the end results of that trailer itself.
[314:26] Was all of these renders.
[314:28] I did a little mini edit together in after effects.
[314:31] To do.
[314:32] Some titles.
[314:33] Little bit of text.
[314:35] And then.
[314:36] Just to showcase some of the work that we were able to put together.
[314:39] So overall I'm very happy.
[314:41] With the course.
[314:43] And the last thing we're going to do today.
[314:45] Is just a little bit of.
[314:47] Posit.
[314:49] And I'll show you how to bring in our image.
[314:51] Perhaps.
[314:52] Make some adjustments.
[314:54] With an additive workflow.
[314:56] And then with a subtractive workflow for our.
[314:59] Our rebalancing some of these lightings.
[315:01] So for now.
[315:03] I'm going to delete this.
[315:05] And we'll create a new file node.
[315:07] And.
[315:08] I'll actually open up render.
[315:10] And we'll do HD cam one.
[315:13] Load that in and then I'll switch my scene view over to composite view.
[315:18] I could close down my geometry spreadsheet.
[315:21] And make a little bit more room that let me set my aces tone mapping.
[315:26] So this is my.
[315:28] HD.
[315:29] Render.
[315:30] And we have done this a little bit before so I'll move relatively quickly.
[315:34] But I have.
[315:35] Add AOVs from file which is now going to bring in.
[315:38] All of these EXR layers that I had created on my output.
[315:42] And if I go to my null.
[315:44] I can take a look at each of these individual ones.
[315:46] So this is my overall beauty pass.
[315:48] Of everything combined.
[315:50] This is the HDRI light.
[315:52] So the contribution we had set up.
[315:54] With our LPE tags.
[315:56] This is the side area light.
[315:59] The new.
[316:00] This is the side area light.
[316:04] The main rectangle light.
[316:07] And then the rim light as well.
[316:09] So if we were to combine these together.
[316:11] We might use an over node.
[316:15] I'll combine my HDRI.
[316:18] With my area light.
[316:20] Set this to add.
[316:22] Duplicate this over as well.
[316:26] Perhaps actually before I add these together I can name these nulls.
[316:29] So this is area.
[316:31] Rim light area.
[316:35] Delete that null actually.
[316:37] Or excuse me that over.
[316:39] This will be.
[316:41] Middle highlight.
[316:51] Area.
[316:52] Left.
[316:55] And HDRI.
[316:57] So as we combine these back together.
[316:59] We may use a.
[317:00] Hsv adjust or really any.
[317:02] Of the cops nodes.
[317:04] If we wanted to make a little bit of adjustments.
[317:06] So maybe I want to bring down the contribution.
[317:08] Of this HDRI light so I can decrease this value.
[317:14] I'll color this one maybe yellow.
[317:22] And perhaps I'll do a similar Hsv adjust.
[317:26] For all four of these.
[317:29] Render layers and then we can merge them together.
[317:32] With a over.
[317:36] And we'll actually change this mode to add.
[317:40] And for the purposes of our mini YouTube course here.
[317:44] This will be fine for balancing.
[317:46] And perhaps resetting some of the intensities.
[317:50] Of these lights.
[317:51] But technically this would not be.
[317:53] The most correct flow.
[317:54] Correct workflow.
[317:55] Excuse me.
[317:56] That we could set up.
[317:58] So blending and adding these beauty renders.
[318:01] Does not give the exact same correct image.
[318:04] To find disable this actually.
[318:06] This Hsv which reduced it.
[318:08] I could compare it to.
[318:10] My original combined beauty.
[318:13] Which would be see here.
[318:16] This is original.
[318:21] This is recombined.
[318:25] And I can use one single switch.
[318:29] To look at the difference.
[318:30] So I'll set my display flag on the switch.
[318:33] So right now I'm looking at the original image.
[318:35] And then the recombined image.
[318:37] It actually does look very similar.
[318:39] But you will notice on the recombined image.
[318:42] We do not have any denoising.
[318:45] That is because we had denoised just this layer.
[318:48] Rather than this main beauty layer.
[318:50] Rather than all of the individual AOVs.
[318:53] So we could use a denoise.
[318:55] If we wanted to.
[318:57] Plug back in our optics denoiser.
[319:00] And perhaps that could be done after.
[319:02] We merge everything back together.
[319:05] So if I put that on the bottom shake here to disconnect.
[319:09] Connect that to the bottom.
[319:10] Then I can compare.
[319:13] And these actually.
[319:15] Look nearly identical.
[319:18] So then to make those additional changes to some of these lights.
[319:21] We can just modify the.
[319:24] Adjustments for these individual layers before they are added back in.
[319:29] So maybe I can decrease this HDRI.
[319:37] Maybe this side light I'll increase the value to two.
[319:42] Maybe even to three.
[319:49] Maybe this middle light here.
[319:51] Maybe 0.5.
[319:54] Maybe 0.25.
[319:56] And if I did want to tint this.
[319:58] I could use a bright node.
[320:00] Maybe I'll bring in a little bit of.
[320:03] Orange.
[320:06] Or actually perhaps blue might look cool.
[320:11] And then I'll set my display flag on bright.
[320:15] I'll take one quick look at.
[320:17] I think this is the top right light and here we go.
[320:20] And maybe I'll.
[320:22] Increase the value of this one to two.
[320:27] And I can now compare the original.
[320:30] To the new recombined image we have here.
[320:33] And we can get a nice and different results.
[320:37] So in this case perhaps our light was too bright.
[320:41] When we increase the value down here.
[320:44] And that's one more thing to be aware of.
[320:46] You don't want to add.
[320:49] Too much brightness back into your image.
[320:52] So you want to balance if you do make some adjustments here.
[320:54] And this is a nice handy way to create some.
[320:58] Changes after we had read that.
[321:00] And actually kind of do like this.
[321:06] I could increase back up my.
[321:10] HDI.
[321:22] And if we had wanted to do additional compositing we could have done individual.
[321:25] Masks for each of these objects so it could be a crypto mat.
[321:29] Which is a object crypto mat or a material crypto mat.
[321:32] Or we could have done just a manual AOV.
[321:36] Defining any of these attributes or any of the material properties as well.
[321:40] But that's going to be out of the scope for this course.
[321:45] And the last thing we might want to do.
[321:47] Is if I go here.
[321:48] Compare this final image.
[321:50] I might want to do a raw image output.
[321:54] Move this to the side.
[321:58] I'll say export me.
[322:00] And then I'll drag this no into the cop path.
[322:04] And I could save this by.
[322:07] Going render frame range.
[322:10] And render to disk.
[322:15] And I'll actually let this finish.
[322:17] And then come back and take a quick look at it once it's done.
[322:20] Welcome back the.
[322:22] Export had actually finished took about a minute and a half.
[322:26] And now we can see I've got my full animation here correctly exported.
[322:32] And recolored with the same.
[322:35] Coloring that I had here within my compositing network.
[322:39] So this is a quick way if you want to adjust perhaps some of the light coloring.
[322:43] Some of the intensities of the lights.
[322:46] Or even modified just a little bit the look.
[322:49] And the overall style without having to re-render any of your images.
[322:52] This did take quite a while to render.
[322:56] So that's actually going to be the end of this section of the video.
[323:00] I can hit you to go up.
[323:02] Jump back into my scene view.
[323:05] And that's going to be kind of the end of the course.
[323:08] We've covered a lot and I really do hope if you made it this far within the course.
[323:13] You learned a lot.
[323:15] I'm going to hit you to go back up one more time.
[323:17] We kind of started with our original plan.
[323:19] Broke it down using the client stage director stage and pipeline manager stage from our core loop within the node navigator blueprint.
[323:28] And this framework really does help as you start working on bigger and bigger projects.
[323:33] Breaking them down and organizing them in this way is something that has helped me get a lot better with Houdini and also be a lot more efficient and.
[323:46] Well intentional, I suppose I could say with my projects makes them a lot more fun and enjoyable to complete.
[323:52] So we did quite a bit inside here.
[323:54] They are set up for the whole pegboard.
[323:56] We prepared this for a RBD simulation that's animated some packed geometry.
[324:03] And then we did a few tricks.
[324:05] Actually, that would be more intermediate or even advanced.
[324:09] You could consider them.
[324:11] So some proper optimization for our RBD workflows.
[324:15] We talked a little bit about the proxy geo using higher resolution geometry for rendering and then a lower resolution even for our actual simulation.
[324:25] And then we set up a workflow for the SOP level solver for two of the options of the many options actually.
[324:34] Whoops.
[324:35] Looks like we've got a crash here.
[324:37] So I'll actually end this or cut this.
[324:39] Then I'll be right back once restarted Houdini.
[324:43] Welcome back.
[324:44] Apologies for that quick cut.
[324:46] We are back within Houdini.
[324:48] Everything seems to be working fine and we didn't lose anything, which is awesome.
[324:52] But we were just talking about our Dopp setup here for our simulation.
[324:56] We had done our SOP level solver and then two approaches to setting up a Dopp net from scratch.
[325:02] One where we, I'm going to cancel this so my simulation doesn't start.
[325:06] One where we put every Dopp object or every RBD object rather within a single packed object.
[325:13] And a second one where we split it out one for the marbles and one for the not marbles.
[325:18] So as simulations get bigger and as project needs get a little bit more specific,
[325:23] sometimes having the flexibility of setting these networks up from scratch is something that's really helpful to do.
[325:30] But the approach, whether you choose to use Dopp networks,
[325:34] created yourself or the SOP level solver is entirely up to you.
[325:41] So thank you again for following along.
[325:45] I ask if you do, if you did enjoy the course, then please leave some thoughts below in the comments.
[325:50] If you have feedback or ideas for future projects, perhaps those could be cool to hear.
[325:56] And then if you completed it, I'd love to see what your final result was.
[326:00] So maybe send me an email or link below your video if you did finish it and upload it somewhere for anyone to see.
[326:09] So awesome. Thank you. That'll be all and I'll see you in the next video.
[326:26] Thank you.



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
