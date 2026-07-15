---
title: Spiral Splash Tutorial in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=xz1oNZGq7P0
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.319"
tags: [vex, quaternion, pop-network, pop-fluid, vellum, super-formula, karma, subsurface, food, product-viz]
extraction_status: complete
frames_dir: tutorials/frames/spiral-splash-tutorial-in-houdini/
frame_count: 16
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Spiral Splash Tutorial in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=xz1oNZGq7P0)
**Author:** cgside
**Duration:** 34m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this video we'll be creating step-by-step
[0:04] this liquid spiral.
[0:06] It will be a fun little experiment to starting to get used to
[0:11] dobnetworks and in this case we'll use popnetwork
[0:14] and maybe you will be able to learn something along the way.
[0:18] So yeah, let's get into it.
[0:21] So we will start in subs by creating a geocontainer and creating a line.
[0:27] And we want this line along the x-axis.
[0:31] So and we also want it in the center so that we can take the length
[0:37] and paste it in the origin divided by 2 and place it in the negative.
[0:42] So something like this.
[0:44] We want a length of 1 and 2 points that's fine.
[0:48] Now we will resample it.
[0:51] So let's go with a resample.
[0:54] And point 1 will be fine.
[0:56] Let me see.
[0:57] Yeah, point 1.
[0:59] And now we will create a mountain just to distort a bit the line.
[1:02] We'll give it some initial shape.
[1:05] And in this case we don't want noise along vector.
[1:08] We want zero centroid and amplitude of point 2.
[1:11] I'm going to follow some values but feel free to use your own.
[1:14] An element size of point 4, 8 and an offset of 20.7.
[1:21] So I guess this is fine.
[1:23] I'll retrain.
[1:25] Let me see if I change something in here.
[1:28] I don't think so.
[1:29] Yeah, that's fine.
[1:31] Now we will resample it again.
[1:33] So we can have a subdivided curve.
[1:38] So resample and go with subdivision curves and a length of point 1.
[1:44] So we get something like this as an initial shape.
[1:49] Now we want to create a UV texture to have a UV attribute.
[1:54] So in this case we want arc length to spine.
[2:00] Spine.
[2:01] So we get something like this.
[2:04] The UV is along the curve.
[2:06] It's just like a curve.
[2:09] Now we want to rotate this to create a spiral.
[2:13] And I will be using facts.
[2:16] But maybe you can get away by using the sweep soap.
[2:21] But just to be fancy, I'm going to use some wax.
[2:23] And maybe you can learn anything or two.
[2:26] So first of all, I'm going to drop an oriental on curve to create the first vectors.
[2:31] And we will create on the x axis the tangent V.
[2:36] And on this tangent we will create a tangent U.
[2:41] Let's check out those vectors.
[2:43] So tangent U will be along the tangent.
[2:48] And we will also have the tangent V, which will be pointing in outwards, as you can see by the x axis.
[2:59] Alright, let's get into the Vex part.
[3:04] Alright, let's drop down a attribute wrangle.
[3:07] And this might be a bit intimidating, but you'll get used to it, I guess.
[3:13] So let's create a flow to you.
[3:15] And this will be equal to our U component of the UV in this case x component.
[3:23] And we will multiply it by a channel.
[3:25] So we can repeat the revolutions in this case.
[3:30] And mold.
[3:30] Let's create that parameter.
[3:33] In this case, I'm going to set it to three for now.
[3:36] Next, we will normalize our vectors.
[3:39] So vector 10 U will be equal to normalize just in case the vector at 10 U.
[3:49] And we will also normalize the tangent V.
[3:52] So tangent V.
[3:55] And let me get this out and V.
[3:58] Now we will create a full revolution for that.
[4:01] We will multiply the U by pi times 2, which is equal to 1 revolution,
[4:08] but then we will repeat it three times.
[4:11] Next, we will create the quaternion.
[4:14] So in this case, I'm going to use quaternions.
[4:15] You can use matrices, but I'm just more used to quaternions.
[4:20] So vector 4, I'm going to call it quads.
[4:23] And it will be a quaternion.
[4:26] And the angle in this case will be the U.
[4:31] And along the tangent U.
[4:35] Next, we will rotate.
[4:37] So tangent V will be equal to quaternion.
[4:44] I don't know what to say.
[4:45] Quaternion, that's it.
[4:47] And then we will rotate the quaternion along the tangent V.
[4:52] And let's see if we have any errors now.
[4:54] Let me just get rid of the visualization.
[4:57] And now we can assign to the position plus equal to tangent V.
[5:03] And we will multiply it by an amplitude.
[5:06] So we can control the amount.
[5:08] In this case, I'm going to call it amp.
[5:12] Let's see how that goes.
[5:13] Let's.
[5:16] And we will go with the value of 0.029.
[5:22] In this case, it's not doing much.
[5:23] It's because I've done something wrong.
[5:27] So normalized tangent V.
[5:30] Multi-your by times 2.
[5:34] Vector 4, quaternion U, tangent U, tangent V,
[5:37] quaternion, tangent V.
[5:42] V, tangent V, amp.
[5:44] So why?
[5:46] This is not working.
[5:49] I believe I know why, because we need to set this to point.
[5:52] Yeah, that was the problem.
[5:54] So the amount of revolutions, as long as you have enough points,
[5:58] in this case, I want 3.
[6:00] And the amount you want to displace in this case, point 0 to 9.
[6:04] So make sure you have this on point,
[6:05] because we are using, we are running these over points.
[6:10] And now we can just create the aperture boot for the sweep.
[6:14] So V at up, it will be equals to normalize the tangent V.
[6:23] And I believe that will work.
[6:25] Let's just let me check.
[6:28] So let me reduce the size.
[6:30] And we will have this spiral effect.
[6:34] And now if we sweep this, so in this case,
[6:38] we want to set it to ribbon.
[6:42] And I believe that so.
[6:46] Let me see how much I use the width of point 0 to 9.
[6:52] So then you have this spiral effect.
[6:58] So let's drop down the normal just in case.
[7:01] And create a null.
[7:04] Called out spiral.
[7:09] And next we will drop a pop network.
[7:15] And let's dive into it.
[7:17] Let me just check what am I doing in here.
[7:21] In this case, it will be pretty simple.
[7:24] Let's make sure in the source,
[7:27] we are using use first context geometry.
[7:32] So that's fine.
[7:34] On the bird, we will emit 5000 points
[7:39] and just a life expectancy of just one second.
[7:45] And let's interpolate the source forward
[7:50] to get rid of some jittering.
[7:55] And other than that, I can just set the inert velocity to 0.
[7:59] But I don't have any velocity.
[8:00] It's just fine.
[8:02] So 5000 points.
[8:03] Let's see how that looks.
[8:06] Just creating the points.
[8:09] And after one second, they will disappear.
[8:12] Let me just check this and set it to 120.
[8:17] This will be more than enough.
[8:20] Make sure we are on real time playback.
[8:23] And now we want to create some pop horse in here.
[8:28] So pop horse to create some more interesting shapes.
[8:33] And in this case, I'm going to use an amplitude of 0.45.
[8:38] This is just amplitude of the effect and a swirl size of 0.3.
[8:43] And I also played with the offset of 50.
[8:46] You can follow these values, our introduce your own.
[8:49] But now if I play, you see the points will go all
[8:53] in all the directions because of this noisy effect
[8:56] that we have in the pop horse.
[8:59] So we want to constrain it not totally,
[9:02] but partially along this shape, this initial shape,
[9:07] this spiral we have in here.
[9:08] And also make it flow along the shape.
[9:12] So for that, we will need a bit of wax.
[9:14] So let's create a pop wrangle.
[9:17] And the first thing you want to set up are the inputs.
[9:22] So in this case, I'm going to go to the inputs, set this
[9:26] to myself, and the second one to a solve.
[9:29] And let's target the spiral.
[9:33] Let's go to the codes.
[9:35] And we will use the min position to attract the points
[9:39] to the surface.
[9:40] So let's create a vector min pause.
[9:43] We'll be able to min pause.
[9:45] In fact, our MP will be able to min pause
[9:50] of the first input and the P.
[9:55] And I will create the direction force.
[9:58] So vector there will be able to normalize.
[10:02] Min pause minus the current position.
[10:08] And we will also multiply it by, let's just call it min pause.
[10:15] It's not a good name, but it will be easier to understand.
[10:18] And let's create that.
[10:21] Let's multiply, let's keep it at one for now.
[10:24] And let's see.
[10:26] So for some reason, of course, we need to apply the force.
[10:32] So V at force, it will be all good there.
[10:37] And let's see now.
[10:38] You can see it's constraining for the most part
[10:42] of the geometry.
[10:44] If we don't do that, it will be all wild.
[10:49] Let me just check if I raise this.
[10:53] It will be even faster.
[10:55] But we don't want that.
[10:56] In this case, we want a force of 0.349.
[10:59] Let's see how that goes.
[11:02] Yeah, that's fine.
[11:04] Now, we also, this is not really necessary.
[11:08] But I want the points to be flowing around the spiral.
[11:13] So for that, I'm going to create a vector.
[11:17] And you, it will be equal to V at 10 u that we put we add from before.
[11:25] And we will, and we will multiply it by again, a multiplier.
[11:31] So let's just call it mold.
[11:34] And let's create the parameter.
[11:37] In this case, I want point of view.
[11:40] And now we can just add this.
[11:43] So plus 10 u.
[11:46] Oops, 10 u.
[11:48] Let's see.
[11:50] Let's decrease this.
[11:52] Let's disable this.
[11:53] And you'll see they are moving along.
[11:55] And I can increase the velocity.
[11:58] The force.
[11:59] I mean, so in this case, I want just a small value.
[12:02] As you can see, they are moving.
[12:04] This is more like if you want to create an animation.
[12:07] In this case, I'm going to use a still frame, but you can create an animation from this.
[12:12] So I believe that so.
[12:14] And now we will introduce the pop force, of course.
[12:18] And let's see the result.
[12:20] And now we want to create some tendrils to create that liquid effect.
[12:24] So for that, we're going to use the pop fluid.
[12:27] And I have some values from before.
[12:30] So let me just check.
[12:32] In this case, I want a particle separation of point 0.01.
[12:36] Let's see how that goes.
[12:38] So it starts to create these clusters of points.
[12:42] And let's increase the constraint iterations and the stiffness.
[12:47] To have a more stable simulation, we can reduce the tensile radius.
[12:53] And maybe increase the viscosity to point two.
[12:56] So let's check out that looks.
[12:58] And we start to get this liquid effect, which is pretty cool in my opinion.
[13:02] But I'm just starting to learn more about the simulation notes.
[13:06] I've been exploring almost exclusively the sub net, the sub operators and, and,
[13:15] and salaries.
[13:17] So I'm a bit behind on the simulation notes.
[13:20] So yeah, that's done.
[13:23] Now, what we will do, we will time shift the frame that I liked.
[13:29] And hopefully it will look similar.
[13:31] Otherwise, I'm going to be playing with the frame in here.
[13:36] So 53.
[13:37] Let me see just to check if that is what I had in mind.
[13:45] So I guess that's different.
[13:50] Let me see.
[13:56] Why is that different?
[14:00] Let me check the spiral.
[14:07] Let me see in this sweep, point on line.
[14:14] I have a different spiral.
[14:18] When this case on the sweep, I applied some scale along the curve.
[14:22] Let me just check.
[14:24] And I have a value of point three, three, three.
[14:28] So this is more like it.
[14:30] Let me just check.
[14:32] Let me play back this again.
[14:35] So do I have a reset simulation in here?
[14:39] So let me just try this.
[14:44] Let me simulate this again.
[14:47] And time shift the frame.
[14:50] 53, in this case, is correct.
[14:54] And I get a similar enough result.
[14:58] It's pretty similar in this case.
[15:00] It's not the same though.
[15:02] I don't know why.
[15:04] Let me just check if I have something in here different.
[15:09] So 5,001, four words.
[15:12] Let me see the pop flow.
[15:14] I might have something different, 0.2, 0.1.
[15:18] No, it's basically the same.
[15:20] But you know what?
[15:22] Let's keep it like that.
[15:25] And then put those 0.3, 0.5.
[15:29] That is fine, I guess.
[15:32] I wonder why this is a bit different.
[15:37] But I guess this will do.
[15:39] Let's see, let's mesh it and see how that goes.
[15:43] So we will use, let's see, that's fine.
[15:47] And we will use a particle fluid surface.
[15:51] Whoops, particle fluid surface.
[15:56] And let's go with a particle separation of 0.0,3.
[16:01] And the result is not bad.
[16:05] And the rest is fine.
[16:08] And we will convert this.
[16:11] So convert to polygons, because this is a polysup, I believe.
[16:16] Polysup, yes, whatever that means.
[16:20] And we will also, while cache it, so, cache.
[16:25] And that's our liquid line created.
[16:31] So let's create an all and call it out, fluid.
[16:38] And right now, you're probably tired of listening to this ramble.
[16:43] But I'm gonna continue on.
[16:46] And if you want to learn a bit more, stay with me,
[16:50] because I'm gonna create some art shapes, shockwats like.
[16:54] So let's create a super formula shape,
[16:59] which is where we have an art.
[17:01] So super formula shapes.
[17:04] And we will create an art.
[17:07] Let's go. We have quite a few in here.
[17:09] If you want to play with shapes, so art.
[17:11] And we will use a weight of 1.1 in this case.
[17:15] And we will re-sample, because it's too much.
[17:18] Point of weight is fine.
[17:20] Now we will thicken this, to create the extrusion.
[17:26] And in this case, we will do both directions and 1.5.
[17:31] Let's get rid of the UBs.
[17:34] And maybe, let's keep it like that.
[17:37] Now, polyfew.
[17:40] And I believe I used just single polygons,
[17:43] so let's just not get it, but trouble.
[17:46] And reverse.
[17:49] And probably can apply some normals.
[17:51] I didn't do that, but just will be easier to visualize.
[17:56] Now, we want to create this balloon-like art.
[18:00] So we can play with the sculpting tools,
[18:03] but I'm not very good with sculpting, I admit.
[18:06] And so I'm going to use instead, valum.
[18:09] So for that, I'm going to remesh,
[18:11] to have a nice topology for valum.
[18:14] And in this case, a target size of 0.0 weight.
[18:18] Let's blur it a bit, so attribute blur.
[18:22] And we will blur it.
[18:24] One is fine.
[18:26] Now let's create a valum, configure balloon.
[18:32] Let's see, an valum solver.
[18:36] Let's press J and drag.
[18:39] Let's see if this doesn't take ages to compile.
[18:43] And reduce, just remove the gravity.
[18:47] We don't need that.
[18:48] And let's see how that goes.
[18:50] So it doesn't move.
[18:51] Let's go to the valum pressure and set the rest length of grid to increase.
[18:56] And now it will rotate around.
[18:58] It's creating the ideal shape.
[19:00] In this case, I believe I played with the valum clause in the stretch.
[19:05] Did I?
[19:06] Yeah, I don't think so.
[19:09] Let me just check.
[19:13] And why is this so slow?
[19:17] Okay.
[19:19] In this case, I didn't play with this.
[19:21] So that's fine.
[19:23] Now we need to make, make this static.
[19:28] So for that, I'm going to create a valum constraint.
[19:32] And in this case, set it to pin two targets.
[19:37] Now it's too fast.
[19:39] You're good.
[19:40] And we're going to set it to soft.
[19:44] So it can still deform.
[19:47] But we want, let's set the stiffness to one.
[19:51] In this case, let's see if that helps.
[19:53] And it does.
[19:54] It just rotates a little bit.
[19:58] So that's fine.
[20:00] That's maybe time shift.
[20:03] And this case, I'm going to time shift to frame 6D, which is fine.
[20:10] And we have this nice arch.
[20:16] Let's create a valum post process.
[20:19] So valum post process.
[20:23] I'm going to blur it by 0.1 or 6.
[20:27] And give it a subdivision.
[20:30] In this case, look, because we are working with triangles.
[20:33] Let's see if that gives us a nice shape, I guess.
[20:37] And now you can keep it like this.
[20:39] In this case, I'm going to quadrimesh it.
[20:42] So in this case, I have the exercise quadrimeshere, which I recommend.
[20:46] Now it was too much.
[20:48] I just want 500.
[20:50] And I'm going to set x and on the z.
[20:53] I believe that's what I did.
[20:55] Then I'm going to just freeze this so you can have access to it on my Patreon files.
[21:01] And I'm going to subdivide it just once.
[21:04] And now the roster doesn't stop their lords.
[21:07] Sorry about that.
[21:10] And the next part, we will create some liquid forming on top.
[21:18] So now let's create some decoration draw on top of this art.
[21:24] What the heck?
[21:26] So just on this one, let's create a draw curve, which is the simplest way of doing this instead of trying to do this with some wax or something like that.
[21:37] So let's press enter.
[21:39] And in this case, I'm just going to do it freestyle.
[21:43] Maybe try another one.
[21:47] But now I'm getting too sloppy.
[21:53] So something like this will be fine.
[21:56] Let's save it.
[21:57] And in this case, I'm going to resample it.
[22:02] And we will resample by 0.05 and set to subdivision curves.
[22:09] And do another bigger resample.
[22:12] So let's copy this and do 0.01.
[22:16] That's fine.
[22:18] Let's maybe move these on the Z-axis.
[22:24] So let's move these by 1.
[22:26] And we will ray over this geometry.
[22:32] Minimum position will be fine.
[22:34] Let's just make sure we output the it-brim and we will blast.
[22:40] And we will blast at it-brim equals to minus 1.
[22:47] So the ones that didn't eat.
[22:50] So, caps lock.
[22:52] It-brim.
[22:54] So, that's fine.
[22:56] And now we will resample it again.
[23:02] In this case, quite a bit I guess.
[23:05] 0.01 and set it to subdivision.
[23:09] That is fine.
[23:12] And let's create an attribute that just float for the p-scale.
[23:16] Let's just set this to 1 to some value, I mean.
[23:21] And let's create a sweep.
[23:23] And see what we got.
[23:25] So, round the tube.
[23:27] And we won't see this case.
[23:29] Let's see.
[23:31] Let's reduce it quite a bit.
[23:34] And also, we want to create an end cap of grid.
[23:39] To create this round the shape.
[23:41] And now we want to play with the p-scale.
[23:44] In this case, I'm gonna set it to noise.
[23:48] To create some irregularities.
[23:50] And I mean, value of 0.18.
[23:53] And I'm gonna play with the element size.
[23:56] Maybe not so much.
[23:57] And the offset, let me find a good value.
[24:03] So, something like this, let me just play a bit more.
[24:09] Yeah, this is fine.
[24:12] And next, we can create a name.
[24:18] And what do I call this, liquid art?
[24:22] Art liquid.
[24:25] And let's name this art shape.
[24:32] And merge this two with the old.
[24:37] And create the null.
[24:43] Let me just shake.
[24:46] I have so many attributes.
[24:48] So, let's just, we will attribute the lead top to it.
[24:52] So, let's get this and create a subnet.
[24:55] And this will calculate again, unfortunately.
[24:58] Well, that's fine.
[24:59] Call it art.
[25:02] That's fine.
[25:04] Let me get back to my file.
[25:08] And let's see.
[25:12] Let's get this into here.
[25:15] And we will create a normal.
[25:18] Because we will scatter some points on this liquid line.
[25:21] So, on the points.
[25:23] And also scatter.
[25:27] And in this case, I'm gonna scatter eight points.
[25:32] I use this seed, but probably we'll have to change it.
[25:36] Let's find, let's see if we have the normals.
[25:38] Yes, let's pick it a little bit.
[25:40] So, the arts are a bit of set it from the liquid shape.
[25:45] Just a small distance of 0.004.
[25:50] We will ensure to delete any attributes in this case.
[25:56] We can just delete all.
[25:58] So, we have many.
[26:00] So, let's just delete all.
[26:02] And attribute.
[26:04] I just looped for the scale.
[26:07] And let's first of all, copy it.
[26:09] So, copy points.
[26:11] Copy these out to here.
[26:14] And the scale will be too much.
[26:17] So, first of all, we can create this random.
[26:23] And between 0.65 and 1, seed of 50,
[26:28] something like this, create another scale.
[26:31] In this case, I'm gonna set it to constant and multiply.
[26:36] Multiply.
[26:37] So, we can control the overall.
[26:40] The global effect.
[26:41] So, in this case, point of 5.
[26:43] What do you find?
[26:45] And we will also create an attribute, randomize.
[26:50] In this case, we will randomize the orient.
[26:53] And direction and orientation for.
[26:56] And play with the seed around to really get something decent.
[27:01] Let's maybe...
[27:04] Let's organize these.
[27:08] And create a merge.
[27:11] And merge these two streams.
[27:16] Let's maybe play with the orientation.
[27:23] And play with the scatter seed.
[27:27] The cast is well-defined.
[27:30] Nothing.
[27:31] Too much.
[27:33] And now, we need to create a name also for this plash.
[27:37] So, name.
[27:40] Let's call it splash.
[27:44] Now, we just need to delete some attributes.
[27:46] In this case, we just want to keep the name.
[27:49] So, attribute delete.
[27:51] We will delete all, but the name.
[27:55] And create an all.
[27:58] And set it to all, salaries.
[28:02] Let's check just the name, attributes.
[28:05] And we indeed have a unique name for every piece.
[28:09] Now, let's move into salaries.
[28:14] Okay, let's move into salaries then.
[28:17] Let's change our desktop.
[28:19] And create a sub import.
[28:22] Let's merge it and create import the out salaries.
[28:27] Let's zoom into it.
[28:29] Oops, H.
[28:31] Is our orientation properly?
[28:33] Yeah.
[28:34] So, we will need a material library to create our materials.
[28:37] This will be a really simple setup.
[28:39] But while we're here, we will create some rendering.
[28:43] Some materials and make a picture out of it.
[28:47] Let's set it to flat, flat long.
[28:50] And I have an HDR, an HDR, right?
[28:58] Or poly heaven, I should say.
[29:01] And I will include this on the final file.
[29:05] And let me create a camera from here.
[29:08] So, let's create just a camera.
[29:10] This is fine.
[29:12] Let's lock it and make sure we're rendering the viewport size.
[29:15] Background dark.
[29:17] Let's find.
[29:18] And we have the camera.
[29:20] Now, let's create the render settings and the renderer.
[29:24] Let's change it to X view.
[29:26] Y 12 is fine.
[29:28] And we will use SSS.
[29:30] So, we can increase the limit quite a bit.
[29:33] Let's see how that looks.
[29:35] The dome light, everything is working.
[29:37] Let's see.
[29:40] So, that is fine.
[29:42] Let's get rid of the grid.
[29:44] And let's create the material.
[29:47] So, the first material will be the liquid.
[29:54] So, let's create the camera material.
[29:56] Let's call it splash matte.
[30:01] Oops.
[30:03] Splash matte.
[30:06] And let's see.
[30:13] I don't want any diffuse.
[30:15] Specular, we want a value around 0.43.
[30:23] And we also want some codes around 0.45.
[30:29] Revenous of 0.1 is fine.
[30:31] Let's increase the subsurface.
[30:33] Connect the color to the radius and scale in this case.
[30:39] Of really small, in this case of 0.002.
[30:43] And we want a color, something like this.
[30:47] A light gray.
[30:49] We can get rid of this.
[30:52] Let's see if that works for us.
[30:54] So, let's assign this to the splash.
[30:58] Oops.
[31:01] And let's see how that looks.
[31:09] Am I using the correct?
[31:15] I'm not seeing.
[31:18] So, the material is fine.
[31:22] And the dome light.
[31:24] Like long, empty room.
[31:27] Why is it looking so different?
[31:31] Let me just shake.
[31:37] Am I applying the correct material?
[31:40] Sorry, I was looking at the wrong material.
[31:43] Let's just make sure we have a scale of 0.005 to have a more subsurface look.
[31:53] And in this case, I don't want any code.
[31:56] I just want a specular of 0.25.
[31:59] And let's see how that looks now.
[32:02] And that starts to look like the liquid I want.
[32:08] We can maybe play a bit with the rotation.
[32:12] Let's see.
[32:13] Let's go with the rotation Y.
[32:20] In this case, it wouldn't help too much.
[32:25] Let's leave it like that and create the remaining materials.
[32:29] In this case, we will duplicate this one and create a shock of parts.
[32:38] Matt.
[32:41] And now, let's see.
[32:44] We will maybe play with roughness.
[32:48] And add some code.
[32:50] So in this case, 0.45, roughness of 0.1.
[32:54] And for the subsurface, I have some coloring here.
[32:58] I'm going to use this value.
[33:00] You can copy if you want.
[33:02] And this is the depth 0.001.
[33:07] Let's assign it to the art shape.
[33:12] And let's see how that looks.
[33:15] That is fine.
[33:18] And let's just create the last one.
[33:21] In this case, choke of liquid Matt.
[33:28] And we will leave the specular as it is.
[33:34] And just change this subsurface.
[33:37] In this case, we will set it to this value.
[33:41] So let's apply it to the art liquid.
[33:47] And let's see how that looks.
[33:50] Let's save and render.
[33:54] And we can possibly apply some denoiser.
[33:59] Let's see how that looks.
[34:02] And yeah, that starts to look a little bit better.
[34:07] And that's really fast.
[34:10] So we're not wasting too much time in here.
[34:13] So yeah, guys, it's a very simple tutorial.
[34:16] But I hope that you have learned a thing or two.
[34:19] It's just making something really simple, a bit complex,
[34:22] which doesn't make much sense.
[34:24] But in the end of the day, you might learn a thing or two.
[34:28] So if you want, you can grab this scene on my Patreon,
[34:31] alongside with hundreds of project files,
[34:35] of exclusive tutorials, really in depth, step by step.
[34:39] And I also have some cheap courses on there,
[34:41] but in my opinion, have a good quality.
[34:44] So if you want to check that out, make sure to see my shop on Patreon.
[34:50] So other than that, thank you for watching, and I'll see you next time.



---

## Captured Frames

- [0:30] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_000.jpg
- [1:40] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_001.jpg
- [3:20] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_002.jpg
- [4:20] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_003.jpg
- [6:40] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_004.jpg
- [9:10] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_005.jpg
- [10:50] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_006.jpg
- [13:20] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_007.jpg
- [15:00] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_008.jpg
- [17:30] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_009.jpg
- [20:00] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_010.jpg
- [22:30] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_011.jpg
- [25:50] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_012.jpg
- [27:30] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_013.jpg
- [30:50] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_014.jpg
- [33:20] tutorials/frames/spiral-splash-tutorial-in-houdini/frame_015.jpg

---

## Structured Notes

### Core Technique
Build a stylized "splashing liquid" hero shot (a chocolate splash arcing over a heart-shaped chocolate piece) by hand-deriving a spiral curve entirely in VEX (quaternion rotation around a tangent basis built from Orient Along Curve), driving a POP network (Pop Noise + a custom min-position attraction wrangle + Pop Fluid) constrained to that spiral guide, meshing the result with Particle Fluid Surface, and separately sculpting a Super Formula heart shape into a balloon-like form via Vellum (rather than manual sculpting) before adding hand-drawn Ray-projected surface decoration.

### Summary
A centered Line is Resampled, lightly Mountain-distorted for an organic base curve, Resampled again into a dense subdivision curve, and given an arc-length "spine" UV attribute. The **spiral itself is built entirely in VEX**: Orient Along Curve provides a tangent basis (`tangentU`/`tangentV`, one along the curve direction, one pointing outward along X); a wrangle computes an angle from the UV's U component scaled by a revolutions channel and 2π, normalizes both tangent vectors, builds a **quaternion** (`quaternion(angle, tangentU)`) and uses it to **rotate `tangentV`** around `tangentU`, then displaces position along the rotated `tangentV` by an amplitude parameter — producing a true procedural spiral entirely from VEX rotation math (with the "up" attribute for the following Sweep set from the normalized rotated `tangentV`). The spiral curve is Swept (Ribbon mode) into a thin ribbon guide mesh. A **POP Network** emits 5000 points with a 1-second life (source-interpolated, no inherited velocity), given chaotic motion via **Pop Noise** (Turbulence-style amplitude/swirl-size/offset), then reined in via a **custom Pop Wrangle**: `minpos()` finds the nearest point on the spiral guide, a normalized direction-to-target vector is computed and scaled by a force multiplier and applied as the POP force (constraining points to loosely follow the spiral rather than flying off chaotically), with an additional velocity term added along `tangentU` (scaled by a small multiplier) to make points flow along the spiral's length. A **Pop Fluid** (tight particle separation, increased constraint iterations/stiffness, reduced tensile radius, increased viscosity) turns the constrained points into a cohesive, tendril-forming liquid simulation; a specific frame is Time Shifted and meshed via **Particle Fluid Surface**, converted to polygons and cached as the finished splash geometry. Separately, a **Super Formula** node generates an arc/heart-adjacent profile shape, which is Resampled, thickened (Extrude both directions) into a closed shell, Polyfilled and reversed, then — rather than manually sculpting a rounded, balloon-like form — **Remeshed** for clean Vellum topology, blurred, and inflated via **Vellum Configure Balloon** + Vellum Solver (gravity removed, pressure rest-length-scale increased) until it settles into the desired plump shape; a **Vellum Constraint set to Pin to Target (Soft, stiffness 1)** keeps the shape mostly static while still allowing subtle secondary deformation, and the settled frame is Time Shifted, Vellum Post-Processed (blur + one subdivision, needed since the base mesh is triangulated), and Quad Remeshed (~500) for a clean final "heart" surface. Decorative liquid squiggles on top of this heart shape are added via a **freehand Draw Curve** tool (simpler than trying to script the pattern), Resampled at two densities, moved off-surface slightly, and **Ray**-projected (Minimum Position) onto the heart mesh with an `it_prim` hit-test attribute used to Blast away any curve points that failed to project; the surviving curve is Resampled again, given a noise-driven p-scale (for organic thickness variation), and Swept (round tube, Grid end cap) into raised liquid-drip geometry merged with the heart. Small decorative splash droplets are scattered on the main liquid line (8 points, random scale ~0.65–1, randomized orientation) and Copy-to-Pointed for extra detail. Everything is named uniquely per piece and brought into Solaris, where three simple Karma Standard Surface materials (splash, choc-arc, choc-liquid — each with tuned specular/coat/roughness and small-scale subsurface scattering with distinct SSS colors) are assigned, lit with a Dome Light (Poly Haven HDRI) and a locked viewport-sized camera, and rendered with SSS limit increased and denoiser enabled for the final hero shot.

### Key Steps
1. **Base spiral curve setup**: centered Line → Resample → light Mountain distortion (zero-centroid, small amplitude) → Resample again (subdivision curves, dense) → UV Texture set to Arc Length / Spine for a `spine`/U attribute along the curve.
2. **VEX spiral construction**: Orient Along Curve → wrangle computing `angle = @uv.x * ch("revolutions") * 2*PI`; normalize `tangentU`/`tangentV`; build `quaternion(angle, tangentU)` and rotate `tangentV` around `tangentU` with it; displace `@P += rotated_tangentV * ch("amp")` (must run over **points**, not primitives, for this to work); set `up` from the normalized rotated `tangentV` for the following Sweep.
3. **Sweep** the spiral curve in **Ribbon** mode (small width) into a thin guide ribbon; Normal + Null (`out_spiral`) for downstream reference.
4. **POP Network setup**: Source from first-context geometry; Birth 5000 points, 1-second life expectancy, source-interpolated (reduces jitter), zero inherited velocity.
5. Add **Pop Noise** (Turbulence-style amplitude ~0.45, swirl size ~0.3, offset ~50) for chaotic initial motion — unconstrained, this sends points flying in all directions.
6. **Custom Pop Wrangle constraint**: two-input wrangle (self + Solver targeting the spiral guide); use **`minpos()`** to find the nearest point on the spiral, build a normalized direction-to-target vector, scale by a force multiplier (~0.349) and apply as `@force` — pulling points back toward loosely following the spiral shape.
7. Add a **flow-along-spiral** term: multiply the guide's `tangentU` vector by a small multiplier (~0.2) and add it to the force/velocity, so particles drift along the spiral's length rather than just clustering at the surface.
8. **Pop Fluid**: tight particle separation (~0.01), increased constraint iterations/stiffness, reduced tensile radius, increased viscosity (~0.2) — turns the constrained point cloud into a cohesive, tendril-forming liquid look.
9. **Time Shift** to a chosen frame (found by trial — frame 53 in this session, dependent on exact node values matching), then **Particle Fluid Surface** (tight particle separation ~0.03) to mesh the splash, Convert to Polygons, and File Cache the result as the finished splash geometry.
10. **Heart/arc shape base**: **Super Formula** node (Arc preset, tuned weight) → Resample → Extrude (both directions, thickness) → Polyfill (single polygon) → Reverse.
11. **Vellum-based sculpting (instead of manual sculpting)**: Remesh for clean Vellum topology → Attribute Blur → **Vellum Configure Balloon** + Vellum Solver (gravity removed, pressure rest-length-scale increased) — inflates/rounds the shape into the desired plump form.
12. Add a **Vellum Constraint (Pin to Target, Soft, stiffness 1)** to keep the shape mostly static/pinned while still allowing subtle secondary motion; Time Shift to the settled frame (~60 in this session).
13. **Vellum Post Process** (blur ~0.16, one subdivision — needed since the working mesh is triangulated) then **Quad Remesh** (~500, X/Z symmetry) for a clean final shape; freeze/cache for reuse.
14. **Hand-drawn surface decoration**: use the **Draw Curve** tool freestyle (simpler than scripting), Resample at two progressively finer densities, offset slightly off the surface (Z axis), then **Ray** (Minimum Position) project onto the heart mesh, using the `it_prim` hit attribute to **Blast away** any points that failed to find a hit (`it_prim == -1`).
15. Resample the surviving projected curve densely, add a noise-driven **p-scale** attribute for organic thickness variation, and **Sweep** (round tube, small radius, Grid end cap) into raised liquid-drip geometry merged with the heart shape.
16. **Small splash droplets**: Scatter ~8 points on the main liquid splash line, pick slightly off-surface, randomize scale (~0.65–1) and orientation, Copy to Points for extra decorative detail; name and merge with the main splash.
17. **Solaris setup**: import all named pieces, build a Material Library with three Karma **Standard Surface** materials (splash, choc-arc/heart, choc-liquid decoration) — each with tuned specular/coat/roughness and a **small-scale subsurface** contribution (distinct SSS colors/scale per material, e.g. ~0.002–0.005) for a convincing chocolate/liquid look; light with a **Dome Light** (Poly Haven HDRI), lock a viewport-sized camera, increase the SSS sample limit, enable the denoiser, and render the final hero shot.

### Houdini Nodes / VEX / Settings
Line, Resample, Mountain, UV Texture (Arc Length/Spine), Orient Along Curve, Attribute Wrangle (`quaternion()`, tangent-vector rotation, normalize, position displacement along rotated tangent), Sweep (Ribbon mode), POP Network (Source, Birth, life expectancy, source interpolation), Pop Noise (Turbulence-style), Pop Wrangle (`minpos()`-based attraction force, tangent-flow velocity term), Pop Fluid (particle separation, constraint iterations/stiffness, tensile radius, viscosity), Time Shift, Particle Fluid Surface, Convert to Polygons, File Cache, Super Formula (Arc preset), Extrude, Polyfill, Reverse, Remesh, Attribute Blur, Vellum Configure Balloon, Vellum Solver (gravity disabled, pressure rest-length-scale), Vellum Constraint (Pin to Target, Soft), Vellum Post Process (blur + subdivision), Quad Remesh, Draw Curve (freehand tool), Ray (Minimum Position, `it_prim` hit-test), Blast (`it_prim == -1` cleanup), Attribute Randomize (p-scale noise), Sweep (round tube, Grid end cap), Scatter (droplets), Copy to Points, Name, Material Library, Standard Surface (specular/coat/roughness, small-scale SSS per material), Dome Light (Poly Haven HDRI), Karma render settings (SSS limit, denoiser).

### Difficulty
Advanced (the from-scratch VEX quaternion spiral construction and the POP-network min-position/tangent-flow constraint wrangle are both substantial custom-simulation techniques; the Vellum-balloon-as-sculpting-tool approach is a nice alternative-to-manual-sculpting trick).

### Houdini Version
20.5.319 (visible in viewport title bar).

### Tags
vex, quaternion, pop-network, pop-fluid, vellum, super-formula, karma, subsurface, food, product-viz

---

## Related Tutorials
- [KineFX and Vellum Fluid in Houdini](kinefx-and-vellum-fluid-in-houdini.md) — shares a similar sine/quaternion-driven VEX animation approach combined with Vellum from the same channel.
- [Vellum Balloon Text in Houdini](vellum-balloon-text-in-houdini.md) — shares the same "Vellum as a sculpting/inflation tool rather than manual sculpting" technique used here for the heart shape.
