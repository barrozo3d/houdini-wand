---
title: Houdini Beginner Tutorial | Creating a perfume bottle
source: YouTube
url: https://www.youtube.com/watch?v=conZuTxHnoc
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, vdb, vex, procedural, fracture, texturing, beginner, product-viz]
extraction_status: complete
frames_dir: tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini Beginner Tutorial | Creating a perfume bottle

**Source:** [YouTube](https://www.youtube.com/watch?v=conZuTxHnoc)
**Author:** cgside
**Duration:** 53m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video we'll be creating this scene step by step.
[0:06] It will be a good chance to learn new things about Odin if you're kind of new to it.
[0:12] I will try to make it as beginner friendly as possible.
[0:17] We won't touch in many advanced topics like Bex and other things, but hopefully you'll
[0:26] get away with some new techniques.
[0:28] So yeah, let's get started.
[0:30] So, I just saved the new scene and we will start by dropping a Geo container and with the box,
[0:42] which will be our main object for the perfume bottle.
[0:48] So let's give it a size of 2 in X, 3 in Y and also give it a subdivision.
[0:57] Now in this case we will leave it like this.
[1:00] Now we will polybavolates, so pretty common thing in many other softwares.
[1:09] So we will bevel by 0.15 and we can leave the divisions like this and do another bevel to
[1:20] those edges and we will bevel it by 0.5.
[1:27] 0.223, so small size and 3 subdivisions.
[1:34] So we get something like this.
[1:38] Now we will create an object here in the front part, so for that let's create another box.
[1:48] And let me see which colors I used, so size of 1, 1 and point out in the Z axis.
[1:57] And now we will group an edgering in the in here, so these in our edgering so we can bevel it.
[2:07] So let's go for edges and disable the base group.
[2:13] And here in the edge length we can introduce a small bellow in this case in the next.
[2:22] So let's see this will work, now we can bevel it.
[2:29] And we will bevel it by about 0.3, 0.3 and select those edges
[2:40] and introduce some subdivisions.
[2:45] Now we will bevel it again, but this time we will ignore the flat edges
[2:55] and maybe let's say 30 and 3 divisions and a distance point.
[3:04] So as you can see if we disable this it will bevel everything.
[3:11] It's just an angle threshold.
[3:17] So now that we have this we can match size and align it to this object.
[3:26] Let's click in here to preview, control click and let's do the alignments on the
[3:33] dead by the min to the max. So the min position in the z of the small cube will align with the max
[3:45] of the perfume bottle. So we also want to move it up so we can add an offset in here.
[3:55] So point 5, 5 and now we want to create some screws let's say.
[4:06] So for that I'm going to start from here on the box and create the blast.
[4:14] And we can disable this and let's flash the primitive 0. So the front one.
[4:23] And we can fail it down.
[4:29] As for now let's create a sphere and in this case I'm going to use a WAP sphere generator
[4:37] which will give us a WAP sphere. We don't need UVs but let's keep it like that.
[4:43] And now we want to cut it but under the axis.
[4:49] And we also want to scale it a bit in on the z so by point 8.
[4:58] And let's also polyfill it because we will use some VDB alterations and we need
[5:06] it filled polygons. So single polygons will find.
[5:10] Now let's copy the points. So we'll copy geometry to these four points we have in here.
[5:20] And this is too big so we can adjust the scale with an attribute to just float.
[5:26] And the piece scale I used was 0.04 so 0.04.
[5:34] And let's march this.
[5:41] And we actually need to do this after.
[5:48] So in this case as you can see it's a bit outside so we need to scale it in.
[5:54] We can do this with primitive properties and do transformation.
[6:00] And in this case I believe I use 0.9 so just scale it a bit in.
[6:07] So as you can see we're just we're just scaling it.
[6:12] Now we can merge everything.
[6:20] And we have our base done.
[6:23] So now we want to break the objects into different pieces so we can have that broken look.
[6:31] I shall do in the beginning of the video.
[6:35] So for that we will use RBD material fracture which will break these into pieces.
[6:43] Let's wait a little bit and we don't need the second breaking or the second fracture.
[6:51] Right now we have 5 points scatter.
[6:54] We can play with a sieve.
[6:56] Not the sieve sorry.
[7:00] scatter sieve.
[7:01] Yes scatter sieve.
[7:04] And we will start to have some breaking.
[7:08] And I can play an exploded view.
[7:13] And just a little bit and we start to have that effect.
[7:18] And we can introduce some edge detail.
[7:25] So if we go to the detail and play an introduced edge detail.
[7:31] In this case I'm going to reduce it to point all three and increase the noise height.
[7:39] So it has a bit more effect.
[7:42] But now it's too much.
[7:44] We need to increase the element size which is the noise frequency.
[7:50] So something like this.
[7:51] But here's the thing.
[7:52] I don't like this particular layout or this particular scatter or distribution of this is.
[8:01] So there's one option in here that you can introduce your own points.
[8:06] So input points.
[8:09] Recall always.
[8:11] Introduce a scatter.
[8:13] Let's say 5 points.
[8:16] And we connect it to the last input.
[8:22] And we need all scatter points of 0 and introduce the input points.
[8:31] So this is a bit better.
[8:33] But in my case I really want to work direct the placement of the points.
[8:40] So I'm going to use a custom now.
[8:43] Let's point on G.
[8:50] And this enables me to place a point or drag it or delete it as you can see.
[9:00] I'll make sure to make this available on Patreon if you guys want to grab it.
[9:04] But again you don't need it.
[9:06] You can just use a scatter and the RBD material fracture.
[9:10] I'm just going to be peak here about the points and
[9:15] and place them where I want.
[9:18] So I will place one in here.
[9:20] Another one in here.
[9:23] Let me see.
[9:24] I have one here.
[9:26] One here.
[9:27] Yes.
[9:27] And then I have another one here.
[9:28] One here in the middle.
[9:30] Let's see.
[9:30] And another one back.
[9:31] Right about here.
[9:32] I'll leave that six points.
[9:33] So much like that more.
[9:35] I have two more here.
[9:35] So one at the bottom.
[9:37] And one at the top in here.
[9:38] And I'll let it up.
[9:39] At least one at the top.
[9:40] Let's see.
[9:40] So one at the top.
[9:42] Maybe you.
[9:43] So one here.
[9:45] So sorry about this.
[9:47] It's just I want really to control the placement of the damage.
[9:55] Let me see if this is even similar to my setup.
[9:59] And I guess it's similar enough.
[10:01] Let me see.
[10:03] I can drag.
[10:07] Let me see.
[10:09] I can drag this one a bit down.
[10:12] So.
[10:15] What's this one?
[10:16] Let's see.
[10:16] Let's fix it.
[10:17] I guess.
[10:20] Let's see.
[10:21] So.
[10:23] Okay.
[10:24] Let's drag this one down.
[10:25] Let's drag this one down.
[10:28] And this one to the top.
[10:29] Yeah.
[10:30] That's fixes our issuing here.
[10:33] So.
[10:35] Let me see.
[10:37] Do we have to see here?
[10:42] So we'll break one in here.
[10:48] And another on the back.
[10:51] So let's see.
[10:53] Maybe let's have another point in here.
[10:59] And we can blast.
[11:05] So now let's make sure we select.
[11:10] And now we can
[11:13] set here the group select.
[11:16] And go for attribute and name.
[11:19] Now we can select by name and press line.
[11:22] We can select fully container geometry.
[11:25] So I'm going to select this.
[11:29] And this in here.
[11:31] I'm just going to delete those.
[11:34] And maybe maybe that one too.
[11:39] So something like this.
[11:41] I'm going to re-assulate this one.
[11:46] So maybe something like this.
[11:50] It's not exactly the same as I had it, but
[11:54] it's well done for now.
[11:59] Now we will use this exploded view.
[12:02] Let me use it to point to one.
[12:07] So something like this.
[12:11] Now we will loop through these pieces and
[12:15] do some geometry operations like remesh VDBs.
[12:21] So it's better to loop them.
[12:23] It will be more optimized.
[12:25] And actually do the do a better job of
[12:29] creating the nice details we want.
[12:33] So let's do that next.
[12:37] So let's create a forage named primitive.
[12:42] So this will iterate over the different pieces we have.
[12:47] As you can see.
[12:48] And we can do operations on them.
[12:54] And at the end we will compile this loop,
[12:57] which will be a bit more optimized.
[13:00] So the first thing we're going to do is to remesh.
[13:08] And let's try that to see some possible problems.
[13:13] So as you can see, we are remashing with the same size
[13:18] to every piece, but that will cause issues.
[13:23] Because on the smaller pieces they will start to disappear.
[13:27] Although it's creating these nice effects on the edges.
[13:31] That's what I'm looking for.
[13:33] But we need to do this remesh with some algorithm in mind, let's say.
[13:41] So we need to remesh it according to their size.
[13:47] So for that outside we will measure the area.
[13:52] So we will measure the area per piece and set the name.
[13:59] And now we will need to promote to a point attribute.
[14:05] So attribute promote
[14:10] from primitive to point.
[14:16] We don't want to delete the original.
[14:19] Or we want to delete the original.
[14:23] Sorry.
[14:24] And do another attribute promote.
[14:26] And we will need the max and the min values of the area.
[14:29] So we can
[14:31] beat them to a new range.
[14:34] So let's promote the area from point to detail.
[14:38] And set minimum, change new name, and set it to min area.
[14:45] Now let's duplicate this.
[14:47] Set to maximum and we will set it to max area.
[14:52] So we now have those attributes.
[14:55] So the max area and the min area.
[14:59] And we want to create the rainbow.
[15:06] And we will just use a very simple function, which is the fit function,
[15:14] which will change the range of our values.
[15:18] So let's assign an attribute called target size.
[15:24] And let's use the fit function.
[15:26] And what we want to fit is the area.
[15:30] And we want to fit it between the detail.
[15:36] Incoming geometry and min area.
[15:40] So we want to fit it between the min area.
[15:47] And the max area.
[15:50] So these are the old min and max.
[15:55] And we want to fit them to
[15:59] mean targets area.
[16:14] And
[16:17] max target area.
[16:20] Target, not area, sorry, seven.
[16:22] So size, which will be the target size on our remesh.
[16:30] And we just need to close brackets and finish our sentence.
[16:36] Our code.
[16:37] And I found some values that work well, which will be point one point a one and point one.
[16:45] And if you look at the spreadsheet,
[16:48] we will start to see we are fitting between.
[16:52] Point one and point one, as you can see.
[16:57] So now if we go to the remesh,
[17:01] size, let's want this and say points.
[17:06] And can be any point.
[17:07] So incoming geometry, any point, I will just pick zero.
[17:11] And
[17:14] you all do, did we call it target size?
[17:17] So let's copy this.
[17:20] And paste it in here.
[17:22] And the component is just a float, so it will be zero.
[17:28] So point zero, zero, target size zero.
[17:35] And ballet.
[17:39] So when we shake, what am I doing running here?
[17:44] So
[17:49] point.
[17:52] So I have target size.
[17:56] It's on the points right on the point.
[17:59] Point zero, point zero, target size components.
[18:05] Oh, I believe we need to
[18:08] reset this and now let's work.
[18:13] Sometimes when working with loops can be
[18:19] sure why is giving me that warning.
[18:22] But as you can see, it's remashing
[18:26] in a more consistent way, where the smaller pieces get enough divisions.
[18:32] And you can play with the range and feed them
[18:36] with other values.
[18:37] But I'm looking for these breaking in here, as you can see,
[18:42] which will create some nice effect.
[18:45] Don't worry about the shading issues because we're about to VDB this out.
[18:51] And it will solve that.
[18:54] Speaking of VDBs, we will also need VDB size
[19:00] similar to this one.
[19:02] So let's copy this wrangle and take care of it right now.
[19:06] So let's go for VDB size.
[19:10] And we will change it between point zero,
[19:15] three and point all weight.
[19:19] So these were some values I found useful.
[19:23] Or that worked really well.
[19:26] And let's do some edge breakup.
[19:32] So really simple in here.
[19:34] So let's duplicate this remesh.
[19:39] And in this case, we will multiply by two.
[19:44] Because we want it really bigger.
[19:49] We will do a natural with blur.
[19:53] And let's do a smaller size.
[20:01] Something like this.
[20:05] So we just want to round it a bit.
[20:08] Let's do a big...
[20:12] I'm copying some values, but this might not work.
[20:17] Because my scene is a bit different now.
[20:21] I will pick it along the normals.
[20:24] And let's do a boobie in a second.
[20:28] And we can see we start to get some damage.
[20:34] Let's maybe label these and get something to see.
[20:39] So some values.
[20:42] And let's see how it works.
[20:48] So it's working fine with creating some damages you can see.
[20:53] And what will we do next?
[20:59] Next we will...
[21:01] Or now let's create a natural root.
[21:05] Why is this showing a time dependent?
[21:12] So let's reset.
[21:16] The edge will do something in here.
[21:23] Sometimes I'll need those strange things.
[21:36] Now we have an inside group from the RBD fracture.
[21:41] As you can see if I place these on groups and go for inside.
[21:48] You can see we have these inside pieces and we will need it.
[21:52] So let's create an attribute from that inside group and call it that inside.
[21:59] Is it working?
[22:02] And this will just create this mask that we can use in our next step which will be the VDBs.
[22:09] So now let's create those VDBs.
[22:20] So I'm going to create a VDB from polygons.
[22:24] And the idea here is to give some details to the inside pieces.
[22:31] So I'm going to create a VDB and in here I'm going to copy this expression.
[22:40] But we created that attribute called VDB size.
[22:46] So VDB size, it is at the end.
[22:51] So this will be based on the size of our geometry.
[22:56] And we will use WorldScale and fill the interior.
[23:01] And we will pass an attribute which is the inside that we're going to use to mask out the inside
[23:08] pieces. That's called the inside. Just fine.
[23:14] And now we might start to see a nail over on the pieces so we can do is set the visibility.
[23:27] And I do inside.
[23:32] So maybe it's not so visible.
[23:35] Let me reset this.
[23:40] Okay, it's not so visible but believe me this will show a nail over around the object which is
[23:49] this mask we have in here. This is attribute.
[23:53] So now we will create a volume bump.
[23:56] Volume bump.
[23:58] And we will create details.
[24:03] Let me just as like what we see here.
[24:09] For this one which has this inside part.
[24:16] And the volume bump it will be, I mean it will be simple but we have to create some notes.
[24:25] So let's create.
[24:30] Let me just check. Did I call this density? No, density.
[24:38] And am I passing the inside? I guess.
[24:47] Let's start to see.
[24:50] There's a difference there.
[24:52] So yeah, let's save it and create a unified noise static.
[24:58] Connect the position to the position.
[25:01] We will need a constant for the frequency and to scale the noise we will use a multiply constant.
[25:10] And we will also need to feed the values of feed range
[25:14] after the noise and a multiply constant to scale down the effect.
[25:22] And to add it to our noise values and add no and connect it in here.
[25:29] Now this will be too much by default so I'm gonna reduce it to 0.1.2.
[25:38] So as you can see is shrinking down the mesh.
[25:45] And let's see what sort of values we will use.
[25:50] So I'm gonna start by tapping the noise type to burnling and change the repetition to 18.
[26:01] So now the next obvious type would be to feed the range so we can start to increase this value.
[26:12] In this case I use 0.2.9.3.
[26:17] And I also reduce the effect to quite a bit. So 0.3.
[26:23] 0.3.
[26:28] And let me see what else.
[26:34] I also introduced some rectal in here so you start to see the effect.
[26:41] It's better if we look at the converted version.
[26:45] So convert VDB and convert it to polygots.
[26:49] So it's Cb effect.
[26:53] Now we have that attribute so we free bind the inside attribute inside volume.
[27:02] And we're divinative values.
[27:09] So we will be freeing through some multiply in here.
[27:13] And add this as you can see it won't affect this front part.
[27:18] And it will create the effect on the inside.
[27:24] Now I also introduce some distortion to these noise.
[27:31] So let's do that.
[27:32] Let's create a worthless noise.
[27:36] And go for a sparse convolution.
[27:39] Treat the noise because we want values between minus 1 and 1.
[27:45] Let's increase the frequency to 4.
[27:49] Connect this to the position and add it to the position of our noise.
[27:56] Main noise.
[27:58] So this will just distort a bit.
[28:02] And you can distort more or less depending on your amplitude.
[28:06] So now let's copy this setup in here.
[28:14] And duplicate it.
[28:19] And in this case, I want to change the type of noise.
[28:29] And also let me do something in here.
[28:33] Let me create a switch to turn on and off our other noises.
[28:38] Let me show the input.
[28:41] Let's set it to yellow.
[28:43] And let's disable it now.
[28:46] And do the same for this one.
[28:49] Let's enable it and connect it to the end.
[28:53] So in this noise,
[28:55] we will change this to a worthless LRF2F1.
[29:02] So to create some notes.
[29:06] And the frequency will be really small.
[29:09] I believe around 2.
[29:13] So 2.
[29:18] And what else?
[29:19] I need to fit the range better and change this to 0.2.
[29:25] So to have more effect, as you can see.
[29:28] And maybe play with the fit range in this case.
[29:32] I just reduce it to something like this.
[29:37] Or in this case increase the effect.
[29:40] So this will be nice.
[29:42] And let's enable this.
[29:46] So enabling notes.
[29:48] Now I'm seeing it's a bit too much distortion.
[29:52] Let's reduce the frequency.
[29:56] And reduce this effect.
[30:01] So this can work a little bit better.
[30:07] And let me see if I'm forgetting something.
[30:10] I'm thinking so.
[30:12] So let's run this loop and see our result.
[30:15] But I mean, I need to think of a single pass.
[30:21] And this will take a while, as we can see.
[30:24] But in the end, we will have a nice result.
[30:28] The thing is, this will take a while.
[30:30] So we need to compile it to be more optimized.
[30:34] So let's select the first note and create a compile block.
[30:40] And connect this
[30:44] in here and enable multi-traded.
[30:48] And of course, we will have an error.
[30:50] Because we are using direct reference
[30:55] in this remesh and VDB notes.
[31:00] So we actually need to use sparing boots.
[31:02] I have a video on the channel about that,
[31:06] which is named compile loops, something like that.
[31:12] Out to compile loops.
[31:14] And I'm going to add a sparing boot and connect this node and just reference.
[31:20] And do the same in here.
[31:23] So add sparing boots.
[31:26] Reference is known.
[31:28] I just want, which is this sparing boot.
[31:32] And do the same in here.
[31:33] So add sparing boots.
[31:37] And reference the node above.
[31:40] And select once.
[31:42] Let's see if now it's working.
[31:44] So it's filing.
[31:47] And there you go.
[31:48] Now it's a bit faster.
[31:51] It's quite a bit faster in this case.
[31:54] So that's our loop then.
[31:57] Now.
[32:01] We need to do the top part.
[32:06] So let's see.
[32:09] Let's start.
[32:11] Let's do that next.
[32:14] So let's start with a box.
[32:16] We want to do the top part of the bottle.
[32:21] So with the box, the Y size of point three.
[32:27] Now we will bevel it.
[32:30] Let me see how much I did bevel.
[32:35] So about 0 weight.
[32:41] And trees and divisions.
[32:43] Now in this case, just one.
[32:45] We don't want it rounded.
[32:48] As you can see.
[32:49] And now we can add another rebel.
[32:53] But this time, we've wanted this.
[32:56] So point 0.06.
[33:01] And trees and divisions.
[33:03] So we have this nice, smoothed result.
[33:10] Now we will create a tube.
[33:13] So let's reference this and create a tube.
[33:18] And in this case,
[33:22] I want a radius of 0.5
[33:28] and I want encabs.
[33:32] And reduce the height to about 0.4.
[33:36] Let's introduce quite a few divisions because we will be the readings out.
[33:43] And now let's match size.
[33:46] So we can align it.
[33:49] Let's do max and min.
[33:55] But not in this add on the wire.
[33:58] That's a min, yeah.
[34:01] Now we need a torus here in the middle.
[34:04] So let's create a torus.
[34:06] And I have some values for it.
[34:11] So we're radius of 0.2.
[34:15] And these radius, these inner radius of 0.09.
[34:21] Let's also do some subdivisions.
[34:24] Otherwise the VDB will have that low polylook.
[34:30] So let's match size this.
[34:36] To this object, I believe.
[34:39] So yeah, in the middle.
[34:41] And now let's learn a new trick.
[34:45] Select this node, this one and this one.
[34:48] And now drag to create a merge.
[34:52] And this is our top part then.
[34:57] Now we will VDB this out.
[35:00] So VDB from polygons.
[35:06] And we'll go quite low.
[35:08] So 0.105.
[35:11] To have these nicely tails.
[35:15] We will also VDB's one last year.
[35:19] To add a bit of smoothness.
[35:21] Not so much, maybe just two.
[35:24] And on the VDB.
[35:27] So we just want to unite the shapes.
[35:31] So we have a single poly, as you can see.
[35:36] Now we can match size this.
[35:43] To this geometry.
[35:45] And in this case, we want mean as X4, X and mean.
[35:53] Mean and X is.
[35:56] That was right.
[35:58] Let's merge this.
[36:00] And we have our initial shape then.
[36:06] Now the only thing to do is to do the
[36:12] the stone at the bottom.
[36:13] That you saw in the beginning of the video.
[36:18] So let's do that next.
[36:21] So now we will create the stone.
[36:23] And for that, I'm going to create a box.
[36:27] And let's change the size to 2.5.
[36:34] And 1.3 in the Z.
[36:38] And now there's an OD, not any cold edge damage.
[36:44] And you can see this is a bit slow.
[36:47] It was fast this time.
[36:49] But let's maybe increase this to weight.
[36:53] And as you can see, it's slow.
[36:56] But in this isolated object, it will work really well.
[37:01] Because it creates very nice details.
[37:05] And if you want to put it in a loop,
[37:09] if you're iterating over geometry and creating this node every time,
[37:13] it will be really slow.
[37:15] And I wouldn't recommend it.
[37:18] But for such a simple object, it works pretty well.
[37:21] And I'm happy with the result.
[37:23] Now you can just align this to the initial object and call it done.
[37:30] I'm going to go step further and maybe show you some nice techniques.
[37:35] So if you want to stick around.
[37:38] So as you can see, this will create this uneven mesh that won't work for the next step,
[37:44] which will be a triplanar displays.
[37:47] So I'm going to water and mash it.
[37:50] Just with the old iny one.
[37:52] And let's go for 100,000.
[37:55] And as you can see, we have some.
[37:57] Not saying this is the perfect apology.
[38:01] But it will it's well distributed and work well for our next step.
[38:10] So now we will select the faces on the side.
[38:15] Because I want to add some details to them.
[38:18] We have with some triplanar displays.
[38:23] So let's use a group expression.
[38:25] Not group expression.
[38:30] And let's keep it on the primitives and say.
[38:35] And so the normal that component is bigger than 0.95.
[38:43] Let's see that.
[38:46] So this selects the front faces.
[38:49] And I also want to select the back.
[38:52] So let's do an absolute.
[38:57] And this now selects the back too.
[39:01] And we need to do the same.
[39:05] Let's go with this hand symbol.
[39:08] And the X.
[39:11] So this will be fine.
[39:14] Let's create a natural root.
[39:18] And call it sides.
[39:22] Let it one.
[39:24] Visualize it.
[39:27] And select the group one.
[39:30] So this is fine.
[39:33] Now we want to blur this through root.
[39:35] Because otherwise we will have a nostransition.
[39:38] Some attribute blur.
[39:43] And we will blur the sides.
[39:46] I believe I said it to 100.
[39:52] In this case to 100.
[39:56] To 100.
[39:57] Yes.
[39:59] That's disabled visualization.
[40:01] And now we will create a triplanar displays.
[40:08] And I will be using these two assets from Megascans.
[40:15] Let me see if I can show you.
[40:18] You can just search for this one massive layer drop cliff.
[40:24] And this rock cliff.
[40:27] Can copy.
[40:31] Copy asset ideas.
[40:32] So is this one.
[40:34] And this one.
[40:35] So if you you can pause the video and search for it.
[40:39] So I'll be using those two textures.
[40:43] So if I try planar displays this.
[40:47] It will be a mess.
[40:49] So as you can see on the edges.
[40:51] But first let's connect the texture.
[40:55] I have here already the file.
[40:57] So let's place it.
[40:59] As you can see it will be a mess on this.
[41:03] So I will be using the edges.
[41:05] And I'm going to instead
[41:07] do it in the color.
[41:11] As you can see.
[41:13] And this place it's in a volume.
[41:15] So a bit on the experimental side.
[41:17] But I found it works a bit better.
[41:19] So let's change the texture scale to point four.
[41:23] And in this case I change the offset to point two.
[41:27] And point two.
[41:29] So I will be using the texture scale to point four.
[41:31] So this will be the first one.
[41:35] But we actually need to subdivide this mesh.
[41:37] Otherwise we won't have enough details.
[41:41] So let's go with the subdivide.
[41:43] And one will be fine.
[41:45] And this will give us a bit more detail.
[41:49] You can see our polycount is already a bit high.
[41:53] But if your computer can handle it.
[41:57] And only you just bypass that subdivide.
[42:01] So I'm going to use the other one.
[42:05] And I'm going to copy to the color.
[42:09] An offset of point three in here.
[42:13] And the scale of point two.
[42:17] So I will use those two textures.
[42:19] Now in point four.
[42:21] I'm going to combine them.
[42:25] So in this case I'm going to use the composite node.
[42:31] First of all we have the CD of the first input.
[42:35] Which is the color attribute as you can see in here.
[42:39] And we also have another CD in here in the input two.
[42:43] So input one we have here the CD.
[42:47] But for the input two we need to import point attributes.
[42:51] And connect it here.
[42:55] And import CD.
[42:57] Which is color diffuse I believe.
[42:59] Then we need a composite node.
[43:03] And we will composite between first this one.
[43:09] And this one.
[43:11] And let's connect this to the CD.
[43:13] And we need to change these two overlays.
[43:17] So it will make small textures.
[43:19] But in this case I reduced a bit the second texture to point seven.
[43:27] But we don't want to actually copy to the CD.
[43:30] In this case we just want the constant.
[43:33] Instead it to white and connected to remove the color.
[43:39] And we want to find the expo.
[43:42] So we want to export the attribute.
[43:46] In this case before that let's look at this.
[43:50] What's the vector to float?
[43:54] Because we don't want actually a vector.
[43:58] We just want a single channel.
[44:02] So let's find the ports.
[44:08] And at this point you are probably really bored.
[44:12] Because I keep working on this.
[44:15] I should have called it done already.
[44:17] But let's do this final stretch to learn something new.
[44:21] Possibly.
[44:23] So in this case we want to export it as this.
[44:27] A let's call it this way.
[44:29] So if you shack your attributes,
[44:33] we will have this mask.
[44:35] Which will have all the information we need for the next step.
[44:41] So let's create a VDB from polygons.
[44:47] So VDB from polygons.
[44:55] I will set it to a low value.
[44:57] But not just not right now.
[44:59] Let's set it to first to point one.
[45:03] And we will set this density.
[45:09] And use world space and fill the interior.
[45:13] Now that I'm seeing this let me check something in here.
[45:19] Oh yeah, I used for both.
[45:21] It's all right.
[45:23] So fill the interior.
[45:27] And now we will pass two values.
[45:31] Two attributes.
[45:33] So first of all, this pay.
[45:35] And we will also pass the sites.
[45:41] So this will be a bit heavy.
[45:45] Because we are creating three volumes.
[45:51] So as you can see, we have density, this pay and sites.
[45:55] It will be a bit heavy.
[45:57] As I told you, this is a bit on the experimental site.
[46:01] So let's select the density.
[46:05] And as you can see, we have these volumes that I want to write.
[46:11] That's what I'm doing.
[46:13] It's not deleting just citing individual port.
[46:17] And now let's create a volume of.
[46:23] And what we will do in here.
[46:29] In this case, we will import the bind.
[46:37] This pay.
[46:41] And we will be inverted.
[46:43] So we have compliments.
[46:47] Because in volumes, in VDB is when you have positive values you go in.
[46:53] And when you have negative viewable valves.
[46:57] But we will still need to play with the values anyway.
[47:05] So feed range.
[47:09] And we will need a feed range.
[47:13] And test it right now with the net node.
[47:17] And a multiply constant to scale down the effect.
[47:23] So let me just organize this and create a net.
[47:33] So this is not pretty.
[47:37] We need to change the multiply constant to 0.05.
[47:41] And as you can see, we are in the displacing the geometry.
[47:45] But it's also creating those ugly edges.
[47:51] So we need to control the effect.
[47:55] And we also need to remove it from the top.
[47:59] So after the feed, we can do a multiply.
[48:05] And do another bind.
[48:07] And call it slides, import the sides, and multiply.
[48:12] Now is only affecting the sides.
[48:15] And now we need to play with the values in here.
[48:19] And maybe pretty subtle, I believe.
[48:23] So 0.4.
[48:25] And this one make it negative 1.2.
[48:31] And now we need to increase this.
[48:35] So let's make 0.26.
[48:39] We need to do some interior bending.
[48:43] So as you can see, it's much better this way than with the triplan of this place.
[48:48] And I also want to introduce some cracks or some damage.
[49:00] And for that, I'm going to copy this set of from here.
[49:07] And go in here and paste it.
[49:12] And we need to steal the position from here.
[49:17] And we want to multiply with the sides.
[49:23] Let's duplicate this.
[49:29] And connect it in here.
[49:33] Now let's just see the effect in here.
[49:39] So in this case, I didn't change much.
[49:43] Played with the offset.
[49:47] Let me see if I can get the same value.
[49:51] So 40.
[49:53] And let me see the feed range.
[49:57] Maybe I changed here.
[50:01] Do I have a bit more effect?
[50:05] Played and we're to distribute the overall effect.
[50:12] So let's see both together.
[50:16] And this is the result we have.
[50:19] Now let's just convert these to polygons.
[50:28] And this is the result we have.
[50:30] So a lot of work and it's okay.
[50:35] Hopefully you learned something new.
[50:39] And before that, we need to blast.
[50:45] We need to blast the other volume.
[50:50] So let's just select the density and convert.
[50:54] Now it's fine.
[50:57] And to finish it off, I'm just going to increase this quite a bit.
[51:03] Quite a bit in terms of VDB.
[51:06] So 0.0075.
[51:11] And this might take a while.
[51:13] Well, didn't take much.
[51:15] We could increase it a bit more.
[51:17] But that's fine for now.
[51:20] Let's match size.
[51:28] And we will set this to max domain.
[51:36] And we'll match this.
[51:42] And match size.
[51:46] And set it to min.
[51:50] Create a null to get rid of that visualization.
[51:56] And I believe I'm not forgetting anything.
[52:01] Maybe we can introduce some normals.
[52:06] I also did it.
[52:07] It's an original file.
[52:10] So yeah, guys, that is basically it.
[52:14] I really hope you have learned something new.
[52:16] I try to make it as easy to follow as possible.
[52:21] Maybe it wasn't really successful.
[52:25] But if you guys have any questions, please feel free to...
[52:30] Place them below.
[52:32] And if you want to get access to this file, you can find it on Patreon.
[52:37] Alongside with this place points, HDA.
[52:43] But I'm telling you, you don't need it.
[52:45] You can just use a scatter or just the default behavior or the R-B-D material fracture.
[52:53] So yeah, other than that, I hope to see you next time.
[52:58] And thank you for tuning in with me.
[53:01] See you.



---

## Captured Frames

- [1:30] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_000.jpg
- [6:15] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_001.jpg
- [11:50] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_002.jpg
- [17:00] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_003.jpg
- [24:00] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_004.jpg
- [35:00] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_005.jpg
- [44:00] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_006.jpg
- [51:40] tutorials/frames/houdini-beginner-tutorial-creating-a-perfume-bottle/frame_007.jpg

---

## Structured Notes

### Core Technique
A full beginner-friendly, largely non-VEX build of a broken/cracked perfume-bottle asset: basic Bevel-based hard-surface modeling for the cap/base/screws, **RBD Material Fracture** with manually-placed custom seed points for controlled breakage, an area-based **remesh-density expression** (via `fit()`) so differently-sized fractured pieces all get appropriately scaled detail, a per-piece **For Each + Volume VOP** noise pass to add organic damage/erosion to the interior of broken chunks, and an experimental **Triplanar-to-volume-displacement** workflow (baking Triplanar color output into a VDB and using it to displace/carve the surface) for rock-like surface detail on the base "stone" shape.

### Summary
The bottle body starts as a simple Box with two Poly Bevels (first a modest bevel, then a larger heavily-subdivided one) for a rounded hard-surface look; a front screw/cap detail box gets its own edge-group-based Bevel (angle-thresholded to avoid rounding flat faces) and is Match-Sized into place. Small screw details are built from a WAP-sphere generator, clipped/scaled, Polyfilled (required for later VDB work), Copy-to-Points'd onto 4 target points with a small `pscale`, then individually scaled inward slightly via Primitive Properties transforms. The whole assembly is fractured with **RBD Material Fracture**, but rather than accepting its default Scatter-seeded break pattern, the author swaps in a **custom point-placement HDA** ("Place Points on Geo," to be shared separately) that lets crack-origin points be manually dragged/placed/deleted directly on the surface for full artistic control over where the object breaks (explicitly noting a plain Scatter + Input Points connection works too, just with less control) — pieces are then selectively Blasted away (via `name`-based Group selection) to leave only the desired broken fragments, and an Exploded View spaces them apart. Since looping per-fragment geometry work is more efficient than operating on the whole fractured mesh at once, a **For Each (name/primitive)** loop processes each piece: first a naive uniform-size Remesh causes small fragments to lose detail/disappear, so instead the actual mesh **area** of each piece is Measured, promoted point→detail to get scene-wide min/max area values, and a **`fit()`** expression maps each piece's own area into a small target-size range (e.g. 0.1–0.1-ish, tunable) — feeding that per-piece `target_size` attribute into the Remesh node's Edge Length parameter so small and large fragments both get appropriately fine, consistent detail. The same area-based target-size attribute also drives a **VDB size** wrangle for later volume conversion. A secondary, coarser Remesh + Mountain (picked along normals) pass adds cheap edge-breakup/chipping directly on the mesh. An `inside` mask attribute (from RBD Fracture's built-in "inside" group) flags interior/broken faces so later effects only affect the newly-exposed crack surfaces, not the original exterior. Each piece is converted to a **VDB From Polygons** (sized via the per-piece VDB-size attribute, using World Scale + Fill Interior, carrying the `inside` mask attribute along), then run through a **Volume VOP** that samples a Unified Noise (Bricconi/Worley type, tuned frequency/repetition, plus a secondary Worley F2-F1 low-frequency noise and a Sparse-Convolution position-distortion noise layered in via a Switch for A/B comparison) added into the volume's density — multiplied by the bound-in `inside` attribute so the noise-driven erosion/damage only appears on interior break-surfaces, converted back to polygons for a convincing "shattered ceramic/ceramic-like crumbling" interior look. The whole per-piece loop is wrapped in a **Compile Block** (multi-threaded) for practical iteration speed, requiring the Remesh/VDB nodes' direct geometry references to be converted to **spare-input references** first (a technique covered in a separate "compile loops" video) since Compile Blocks can't handle direct cross-node references. The bottle's cap/top is built separately from a beveled Box, a capped Tube, and a Torus, merged and VDB'd together (small VDB voxel size for detail, light VDB Smooth) for a unified rounded metal-cap look, then Match-Sized onto the fractured base. Finally, a rugged "stone" base plinth is built from a Box run through an isolated (non-looped) **Mountain** node (acceptable for a single simple object, but explicitly called out as too slow to use inside a per-piece loop), remeshed evenly, then given rock-like surface detail via an experimental workflow: front/back faces are grouped by normal threshold (`abs(N.x) > 0.95`-style Group Expression) and Attribute-Blurred for a smooth mask transition, two Megascans rock textures are projected via **Triplanar** (found visually messy directly as color, so instead baked through a Composite node blending both textures' CD/color-diffuse channels) into a mask attribute, which is then baked into a **VDB From Polygons** (carrying `density`, the mask, and the side-group attribute as separate volumes) and read back in a second Volume VOP that inverts/complements the mask (VDB convention: positive = inside), Fit-Ranges and scales it down, multiplies by the side-group mask (so displacement/cracking is restricted to the side faces, not the flat top), and adds it into density for a carved rock-crack look — plus a second near-identical noise layer for additional crack variation — before converting back to polygons at a fine VDB resolution for the final detailed stone shape.

### Key Steps
1. **Bottle body:** Box (2x3, subdivided) → Poly Bevel (small, few divisions) → Poly Bevel (larger, more subdivisions) for the rounded main body shape.
2. **Front detail box:** second Box, Group an edge ring, Bevel it (angle-thresholded via "ignore flat edges" style angle parameter to avoid rounding flat faces), Match Size (min-to-max alignment) onto the body with a small offset.
3. **Screw details:** WAP-sphere generator (UVs not needed) → Clip in half → Scale on Z → Polyfill (needed for later VDB work) → Copy to Points onto 4 target points with a small `pscale` (~0.04) → per-instance inward scale via Primitive Properties transform (~0.9) → Merge everything into the base shape.
4. **Fracture with controlled seed points:** **RBD Material Fracture** on the merged base; instead of its default internal Scatter, feed in custom crack-origin points via a **custom "Place Points on Geo" HDA** (manual drag/place/delete control over break locations) — or, as a simpler built-in alternative, a plain Scatter node wired into the fracture's Input Points connection.
5. **Select desired fragments:** use Group (by `name` attribute) to Blast away unwanted fracture pieces, keeping only the fragments that form the intended "broken bottle" look; use Exploded View to preview spacing.
6. **Per-piece area-based remesh sizing:** inside a **For Each (name/primitive)** loop, **Measure** (Area) per piece, promote point→detail to get scene-wide min/max area, then use **`fit(area, min_area, max_area, min_target_size, max_target_size)`** to compute a per-piece `target_size` attribute — feed this into the Remesh node's Edge Length (per-point value) so small fragments don't lose geometric detail and large fragments aren't over-tessellated.
7. **VDB-size attribute:** duplicate the area-measurement wrangle to compute a similar per-piece `VDB size` attribute (different target range, e.g. 0.03–0.08) for use in the later VDB conversion step.
8. **Cheap edge breakup:** a secondary coarser Remesh (roughly double size) + Attribute Blur + Mountain (picked along normals, small amplitude/element size) adds cheap chip/damage detail directly on the mesh surface.
9. **Interior mask:** create an `inside` point/primitive attribute from RBD Fracture's built-in "inside" group, marking which faces are newly-exposed break surfaces (vs. original exterior) — used to restrict later noise/erosion effects to just the interior.
10. **VDB + noise erosion on interior faces:** **VDB From Polygons** (sized via the per-piece VDB-size attribute, World Scale + Fill Interior, carrying the `inside` attribute) → **Volume VOP**: sample a Unified Noise (Bricconi/Worley-type, tuned frequency/repetition) plus a secondary low-frequency Worley F2-F1 noise and an optional Sparse-Convolution position-distortion layer (toggled via a Switch for comparison), Fit-Range and scale the combined noise, **multiply by the bound `inside` attribute** so it only affects interior break surfaces, add into density, then convert back to polygons.
11. **Compile the loop:** wrap the whole per-piece chain in a **Compile Block** (multi-threaded) for practical speed across many fragments; since Compile Blocks reject direct cross-node geometry references, convert the Remesh/VDB nodes' direct references into **spare-input references** first (per the author's separate "compile loops" technique video).
12. **Cap/top assembly:** Box (beveled, one bevel unrounded/angular, one small heavily-subdivided rounded bevel) + capped Tube (radius/height tuned, subdivided) + Torus (tuned radii, subdivided to avoid a low-poly VDB look) → select all three and drag-merge → **VDB From Polygons** (small voxel size) → light **VDB Smooth** (~2) → convert to polygons for a unified rounded metal-cap shape → Match Size onto the fractured base.
13. **Stone base — shape + coarse detail:** Box → isolated (non-looped) **Mountain** for organic bumps (explicitly called out as too slow to run per-piece inside a loop, but fine for one simple standalone object) → Remesh evenly (~100,000 points) for good topology ahead of the Triplanar/volume-displacement step.
14. **Stone base — side mask:** Group Expression selecting front+back faces via `abs(N.x) > 0.95`-style normal threshold, named `sides`, then Attribute Blur (~100) for a smooth mask falloff (avoiding a hard visible seam later).
15. **Stone base — rock texture via baked Triplanar mask:** load two Megascans rock textures (cliff/mossy-rock sets) via **Triplanar**, found messy when displacing directly from color, so instead route each texture's CD/color-diffuse output through a **Composite** node (Overlay-style blend, second texture scaled down ~0.7) to combine them into a single grayscale mask attribute (bound/exported, vector-to-float'd down to a single channel).
16. **Stone base — volume displacement from the baked mask:** **VDB From Polygons** carrying `density` + the baked mask attribute + the `sides` attribute as separate volumes → **Volume VOP**: import/bind the mask (complemented, since VDB convention treats positive values as "inside"), Fit-Range and scale down, **multiply by the bound `sides` attribute** (restricting the effect to side faces only, not the flat top), add into density; layer a second, near-identical noise pass for additional crack variation; convert back to polygons at a fine VDB resolution for the final rock-textured stone shape.
17. **Final assembly:** Match Size the stone base and cap onto the fractured bottle body; merge everything into the completed broken perfume-bottle scene.

### Houdini Nodes / VEX / Settings
Nodes: Box, Poly Bevel (angle-threshold "ignore flat edges" option), Group (edge ring, normal-threshold expression), Match Size (min/max/mean alignment variants), WAP Sphere Generator, Clip, Polyfill, Copy to Points (`pscale`), Primitive Properties (per-instance transform scaling), RBD Material Fracture (custom Input Points connection, built-in "inside" group), custom "Place Points on Geo" HDA (manual point placement — author's own tool, alternative: Scatter), Blast (name-based group selection), Exploded View, For Each (name/primitive, wrapped in Compile Block + multi-threading, spare-input references required for compile compatibility), Measure (Area), Attribute Promote (point↔detail for min/max), Attribute Wrangle (VEX: `fit()` for area-to-target-size mapping), Remesh (per-point Edge Length from attribute), Mountain (custom vector-along-normal displacement, coarse edge-breakup variant), Attribute Blur, VDB From Polygons (World Scale, Fill Interior, multi-attribute carry-through), Volume VOP (Unified Noise — Bricconi/Worley types, Sparse Convolution position distortion, Fit Range, Multiply Constant, bind/import attribute nodes, Switch for A/B noise comparison), Convert VDB, VDB Smooth, Compile Block (multi-threaded), Tube (capped), Torus, Composite (texture-blend for baked mask), Karma Triplanar (Megascans rock textures), Vector to Float.

### Difficulty
Intermediate — explicitly framed as beginner-friendly and VEX-light (only simple `fit()` expressions used), but the area-based remesh-sizing pattern, per-piece Compile-Block loop, and experimental Triplanar-to-volume-displacement workflow are non-trivial procedural techniques worth learning from.

### Houdini Version
20.5 (UI matches Houdini 20.5-era Volume VOP/Triplanar/Karma toolset).

### Tags
#modeling #vdb #vex #procedural #fracture #texturing #beginner #product-viz

---

## Related Tutorials
Cross-link with dusty-bottles---bridging-procedural-workflows-in-houdini-and-solaris.md (same author, similar product-viz bottle-modeling + VDB workflow) and hard-surface-techniques-in-houdini.md (shares the Compile-Block-with-spare-inputs pattern) once indexed together.
