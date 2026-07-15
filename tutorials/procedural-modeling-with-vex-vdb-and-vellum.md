---
title: Procedural Modeling with VEX, VDB and Vellum
source: YouTube
url: https://www.youtube.com/watch?v=8RIneeMCbAg
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [vex, vdb, vellum, xyzdist, quaternion, compile-block, upholstery, couch, curve-manipulation]
extraction_status: complete
frames_dir: tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/
frame_count: 11
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Modeling with VEX, VDB and Vellum

**Source:** [YouTube](https://www.youtube.com/watch?v=8RIneeMCbAg)
**Author:** cgside
**Duration:** 40m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome!
[0:02] So in this video we will be modeling the simple couch.
[0:05] At first it might look a bit boring or easy to do,
[0:08] but there will be some challenges along the way.
[0:11] And if you dive in with me, you might learn anything or two.
[0:14] So let's get started.
[0:16] So I just saved the new theme,
[0:18] and we'll drop a Geo container and a circle.
[0:22] So this will be our base for the sofa.
[0:26] Let's place it on the ZX plane to be flat on the ground.
[0:30] 12 divisions, that's fine.
[0:32] Now we need to convert this to a line.
[0:35] So convert line and we will connect the pet.
[0:38] So we have a single primitive.
[0:40] So the idea now is that we need to do some sort of resampling of these points.
[0:45] I still want 12 points, but I want to bring them together at a location.
[0:50] So some parts of the sofa are smaller than others.
[0:55] This will be like a ramp going around assembling the points.
[1:00] So we will work on points.
[1:03] So let's drop a net node.
[1:06] And you will see what I mean in a bit.
[1:08] So let's delete geometry but keep points.
[1:11] And now we want to drag a naturoput wrangle.
[1:17] And let's connect this to the first input.
[1:20] And this one to the second input.
[1:22] So we will look at the line since it has primitives.
[1:24] And we will use the premium function and the X, X, Y, Z list.
[1:29] So we can bring together those points.
[1:33] And this is the very classical way of doing things.
[1:40] The idea is to offset the point using the premium function and assembling the primitive with X, Y, Z list.
[1:50] So this is always useful to have.
[1:53] But right now we have, let's see, we have 12 points.
[1:57] Yeah, we don't need to fuse because we have 12 points.
[2:00] So that's fine.
[2:02] And we can actually start our coding.
[2:06] So let's go in here.
[2:09] And the first thing I'm going to do is to use the X, Y, Z list function to go from the points to the curve.
[2:17] So float X, this just as an as a variable.
[2:21] And we will use X, Y, Z list.
[2:24] And we will look for the input one.
[2:27] So the primitive for the curve from the current position.
[2:30] And we will save some attributes.
[2:32] So we can save V at it.
[2:36] Prem. So the primitive that found.
[2:39] And so this is not V, this is I since it's primitive.
[2:45] And we will also look at it.
[2:48] Your VW.
[2:51] And let me see if I use here a distance.
[2:54] I don't think so.
[2:55] So that's fine.
[2:56] That's our first line.
[2:57] Now let's say we want to rotate the points around.
[3:01] So for that, we will do.
[3:04] We will create a variable called update boss.
[3:10] And this will be equal to the it you be.
[3:14] So we at it.
[3:16] You'll be W dot X.
[3:19] Since it's.
[3:21] We are we are working with cars.
[3:23] So we only have the you attribute.
[3:27] So you V dot X.
[3:29] And we can just add to the position.
[3:32] So we will add here a temporary channel.
[3:35] So 10th offset.
[3:38] And that's good for now.
[3:41] And let's update the position.
[3:43] So V at B.
[3:44] It will be equals to premium.
[3:48] The primitive, the second input and the position.
[3:54] Sample the position.
[3:57] The primitive is always zero.
[3:59] So we can set it like that.
[4:01] And we will update the the you V attributes.
[4:04] So update boss.
[4:05] Update boss.
[4:07] Let's see how that goes.
[4:10] So V at B.
[4:12] It will be equal to premium V.
[4:15] And let's create a slider.
[4:17] And as you can see, it's rotating.
[4:19] But it won't wrap around because we haven't used the model function.
[4:24] So right in here, we can do.
[4:27] We can do module one.
[4:31] So it wraps around.
[4:32] Let's see if that works now.
[4:34] So it's not working because I'm not using.
[4:38] We need to set some brackets in here.
[4:40] So this goes first.
[4:43] And now it should work.
[4:44] As you can see, it's rotating around.
[4:47] And the idea now is to create a system.
[4:50] So we can.
[4:52] Bring some points closer together than others.
[4:55] So let's do this step by step.
[4:58] First of all, we will need a curvy attribute.
[5:01] So we could use a sample and get it for free.
[5:04] But let's use one in here.
[5:06] So float you it will be equal to vertex curve bar.
[5:10] So vertex curve farm input zero.
[5:15] And we will do add vertex.
[5:18] No, I believe that's how it's done.
[5:21] We can type cast it.
[5:23] And let's see that works for us.
[5:27] So actually we might need to do this on the input one,
[5:31] because this one doesn't have a primitive.
[5:33] Let's.
[5:36] So let's actually see that f at the view it will be equal to you.
[5:42] Let's disable the visualization and have a look in here.
[5:47] So as you can see, let's use input one.
[5:50] And this should do it.
[5:54] So actually it doesn't.
[5:57] So vertex curve farm.
[6:02] So since we don't have vertices in the first input, as you can see,
[6:07] by the spreadsheet, we can actually just use the point number instead of the VTX num.
[6:14] So let's do it with the num.
[6:16] And this will give us the curvy attribute that we need.
[6:21] So what else we will do in here?
[6:25] We will need to mirror this effect.
[6:29] So for that, let's actually.
[6:32] I believe there's a way to increase the point.
[6:37] So in the geometry point size, there we go.
[6:41] Now we can see clearly that is going from zero to one or seem closer to one.
[6:47] And now I want to mirror this effect.
[6:51] So for that, I'm going to create.
[6:55] Use the air some math.
[6:57] So I'm going to do you it will be equal to absolute.
[7:01] You you times 2.0 minus 1.0.
[7:07] And this should mirror the effect.
[7:11] So as you can see, now we have one in here, zero in here.
[7:15] And we will we can actually see that we the marker.
[7:20] So as you can see, we are mirroring the ramp or the curvy attribute.
[7:27] And now the idea is to move the points together at a certain point.
[7:35] And we also need to make some values negative.
[7:41] So it goes one way, another values positive.
[7:44] So it goes another way.
[7:46] And we will use here this the position dot z as a sign input, let's say.
[7:51] So let's actually do that.
[7:53] So if we do you times equal sign at p dot z.
[8:05] So since we wanted on this axis.
[8:08] So it makes negative one in one size and positive one in the other side.
[8:13] Because if we don't do that and we.
[8:17] We move it in here.
[8:19] So we can actually delete this.
[8:25] So and we will do we will use the your component.
[8:29] So let's do you.
[8:33] Times.
[8:35] C.H.F.
[8:36] Journal float.
[8:37] Most so we can control the overall effect.
[8:41] And let's do minus instead.
[8:44] So to move it in the other direction.
[8:46] And let's delete this one.
[8:48] Delete spare input and create another one.
[8:51] So as you can see, it's moving in one way.
[8:53] It's doing what we want using the curvy.
[8:56] But it's only it's only moving it in one direction.
[8:59] So let's do this you offset.
[9:02] This is your sign, let's say.
[9:04] And now if we move it, you can see that it's going in both directions, both positive and negative.
[9:10] As you can see, here is negative and here is positive.
[9:14] So that was a lot of work just to do this effect.
[9:17] But you know, we actually get something out of this.
[9:22] And now to control it's even better, we can use a ramp.
[9:26] But in this case, I didn't found it necessary.
[9:29] So I'm just going to do a power function.
[9:32] So we can do it in here.
[9:35] So you it will be equal to power of you.
[9:40] And we will use in here a channel float and call it you.
[9:48] And let's do this.
[9:50] And as you can see, these help us will help us control the effect.
[9:55] So if we move and we can control the effect with this power function.
[9:59] So I'm going to set the multiplier to point all three four.
[10:03] And the power function to point three one.
[10:08] So a lot of work, right?
[10:11] But now we have what we need.
[10:13] That's so we have some parts of the model that will be smaller and some parts bigger within a progressive effect.
[10:22] So that's fine.
[10:23] Now that we have this out of the way, let's move to the next part.
[10:28] So just to be 100% accurate, we are passing a year of float.
[10:33] But this is the UV attribute.
[10:35] So we should actually set here a vector.
[10:39] So this will be the X and we will do 0.0 and 0.0 for Y and Z.
[10:45] So this will result in the same way.
[10:47] But it will be slightly more accurate.
[10:50] And it's actually a good practice.
[10:52] That's all.
[10:53] So we have the points ordered, right?
[10:56] So we can just create geometry from this.
[11:00] So let's create an add and go to polygons by group and close.
[11:04] So we have the geometry.
[11:06] And we now can, we will convert it to a line again.
[11:14] So from a vertical line.
[11:16] I'm following my file, but I'm not sure I needed all those steps.
[11:20] But let's do it anyways.
[11:22] So let's make sure we have a single.
[11:25] No, we need actually these, these primitives.
[11:28] So we don't want to have a single primitive.
[11:30] Because right now we will save an attribute for each prime number,
[11:33] which will come in handy in a bit.
[11:35] So let's do an attribute wrangle and create a frame ID attribute.
[11:42] And it will be equal to add a frame number.
[11:45] And we want to set it to integer and run it over primitives.
[11:50] So let's actually see that.
[11:52] And there we go.
[11:54] We have the attributes.
[11:56] And now I want to resample this.
[12:05] And the idea is to have slightly more points.
[12:11] So we can make it a circle again, but still keep this attribute.
[12:19] So let's do a resample.
[12:22] Let me see in here.
[12:23] We will do a resample.
[12:27] And set it to 0.05.
[12:31] Let's see how that goes.
[12:34] And now we will copy this dark line here.
[12:36] So control alt shift drag to make a reference copy.
[12:40] And we will change the division.
[12:42] Let's say to 128.
[12:46] Now we can convert line.
[12:53] And we will connect the pet to every single primitive in this case.
[12:57] And let's just make these a circle.
[13:00] So we will do an attribute wrangle and do a simple min pose.
[13:04] So v at b it will be equal to min pose.
[13:08] Of the input one and the current position.
[13:12] Let's see if that works.
[13:14] And it does.
[13:15] We just made it a circle since it's our final shape.
[13:18] And we have more points to play with.
[13:20] And we still have that useful attribute that we'll need.
[13:23] So as you can see, the primitive zinear are bigger.
[13:26] Or the attribute that we have in here is bigger than this part in here.
[13:32] So what will we do now?
[13:35] We will create some geometry from this.
[13:40] So let's actually create a polypads to unite the primitives.
[13:47] And we will connect and point where we'll lose that attribute.
[13:50] But we will get it in a bit.
[13:52] So poly extrude now.
[13:54] And I'm going to extrude about 0.4.
[13:57] So poly extrude and let's do minus 0.4 to move it in.
[14:03] And we will also reverse it.
[14:07] That's fine.
[14:09] Let's get rid of this visualization.
[14:12] And our geometry is working great.
[14:14] And now let's do a natural transfer.
[14:18] And we will transfer from here to here.
[14:21] And let's see the primid.
[14:24] And let's visualize it.
[14:26] So this should work fine.
[14:31] And we might want to play here with the distance.
[14:35] It won't really make a difference.
[14:37] So let's keep it default.
[14:39] Now we want to rotate these a bit since I don't want it looking at the x-axis.
[14:45] I'll actually want it along the z.
[14:47] So let's do a transfer.
[14:49] And rotate it minus 90 on the y.
[14:53] So we have this weight.
[14:55] It will be easier to work with.
[14:58] And now we want to split these polygons.
[15:04] So we can work with them separately.
[15:07] So let's do a vertex split.
[15:11] And we will split not the end, but the primid.
[15:15] So if we do now and explore that view,
[15:19] you can see they are separated.
[15:21] And before it wasn't.
[15:24] So we will do now poly extrude to create some geometry from these.
[15:31] And we will extrude by about 1.3.
[15:34] So 1.3.
[15:36] And we will have.
[15:37] We will start with our geometry.
[15:40] We will also clip it.
[15:44] So let's do a clip.
[15:52] And we will clip it along the y.
[15:55] And let's see.
[15:58] What is that?
[16:00] So we need to move this up.
[16:03] And we want primitives below the plane and fill polygons.
[16:07] And we just need to do something like this.
[16:10] So as you can see.
[16:12] And I'm actually going to copy my original clip so we can keep some consistency.
[16:20] But it is the same that I've just done in here.
[16:23] So in this case, we are clipping along the y that's rotated in the Z axis.
[16:30] So these were the values I used.
[16:32] If you want, you can pause and copy it.
[16:34] But it's just to keep some consistency.
[16:36] I'm going to reuse the same clip.
[16:39] So now I want to be able to these edges in here.
[16:43] But if I try to do that since the geometry is separated,
[16:48] it will select the inner edges also.
[16:51] So if I do include biages, I mean a max edge angle, or in this case,
[16:56] I mean a jungle.
[16:57] As you can see, selecting these inner parts.
[16:59] And I don't want to be able to.
[17:00] Those I just want to be able to this outer and inner edges.
[17:06] So we can do a trick in here.
[17:08] We can do a Boolean Boolean union.
[17:12] And this will unite the shape.
[17:14] And now we can do that group.
[17:16] I shouldn't have deleted it.
[17:18] And we can do include biages, max edges and mean a jungle.
[17:24] And as you can see, now we're selecting.
[17:26] And I also need to output the back in here.
[17:31] And we can just group transfer.
[17:34] So group transfer to the original geometry.
[17:37] And that will work just fine.
[17:39] So we don't even have to do anything.
[17:41] Just will be will work great.
[17:45] And now we can do the babbling.
[17:47] So let's do a babble.
[17:49] And let's babble those edges.
[17:51] So group one.
[17:52] And I'm going to increase the distance to about 1.15.
[17:58] And let's say four divisions.
[18:00] So as you can see, it's working great.
[18:03] Now we will do some VDB operations in this.
[18:07] So let's do that next.
[18:10] So as I was saying, we will do some VDB operation.
[18:13] But to keep the geometry separated into these sections,
[18:17] we will actually need to do it in a loop.
[18:21] So since we have this attribute also,
[18:23] we can use that prem ID to iterate over.
[18:26] So for each named primitive,
[18:28] and we say your prem ID instead of name.
[18:33] So as you can see, it's rating over each primitive,
[18:37] each prem ID attribute.
[18:40] And now we can do the following.
[18:44] I want to keep these white sharp at this edge,
[18:50] but smooth a bit this middle part.
[18:54] So far that I'm going to create an attribute.
[18:56] So first of all, I'm going to group primitives that's fine.
[19:00] And do normal, not normal, sorry.
[19:03] We will do edges and do max edge angle.
[19:06] So we will select these frames.
[19:08] And now let's do, let's create an attribute.
[19:11] So let's go to the triangle.
[19:14] And we will go over primitives.
[19:17] And the group will also be primitive.
[19:20] So this group tool and the F at,
[19:23] at shell mask, it will be equal to one.
[19:27] And this will look something like this.
[19:31] And now we can do VDB from polygons,
[19:34] let's see how much data I use in here.
[19:37] In this case, I used 0.02.
[19:41] And I'm actually going to fill the interior
[19:45] and use world's face.
[19:46] That's fine.
[19:47] And pass here an attribute.
[19:48] So we will do shell mask.
[19:50] And let's call it mask.
[19:53] Now we can see the zealous.
[19:54] So far that we can do a visibility.
[19:58] And I did.
[19:59] So I did the mask.
[20:01] And I did.
[20:02] So I did the mask.
[20:04] That's fine.
[20:05] 0.02 is fine, I guess.
[20:08] And let's do a VDB smallest year.
[20:11] VDB is smallest year.
[20:14] And we want to pass the mask.
[20:16] So we will use as an alpha mask the mask.
[20:19] And let's see how much data I use in here.
[20:22] So about 10 iterations.
[20:24] And as you can see, it's keeping that.
[20:27] I just need to say surface in here.
[20:30] It's keeping that outer edge more less intact.
[20:34] And now we can do a simple VDB smallest year again.
[20:39] And now we will do on the surface.
[20:45] And we will do just one iteration.
[20:48] Just to get rid of the texture,
[20:51] those extra issues in there.
[20:54] So let's do just one iteration.
[20:57] So this is the result, as you can see.
[20:59] We'll try to keep that part flat or more sharp.
[21:03] So let's convert this to polygons, convert VDB.
[21:08] And we will change it to polygons.
[21:10] That's fine.
[21:11] We could probably increase the resolution.
[21:14] But let's keep it like that to be faster.
[21:17] And we will at the end do a simple remesh.
[21:21] And for the remesh, we will use 0.0.02.
[21:28] And let's increase the smoothing to 0.5 and the iterations to 6.
[21:34] So we will have these sort of results.
[21:39] Let me see in here.
[21:43] Yeah, something like this.
[21:45] And now we can compile this.
[21:47] So let's do a compile block.
[21:49] Let's look at this.
[21:51] Place it in here.
[21:53] Oops. And drag it over.
[21:56] Make sure we use multi-traded and we don't have single pencil.
[22:00] Let's look and it should be pretty fast.
[22:02] So you can see we were able to keep some sharpness.
[22:05] That was my idea initially.
[22:07] And we have a nice remeshed surface that we can use in our next step,
[22:13] which will be the valent part.
[22:16] So let's just organize this year a bit.
[22:20] And now we will move into valent.
[22:22] So I just want to inflate a bit the shape.
[22:25] This is pretty boring and computer-like look, computer-generated look.
[22:31] So let's give it some life with a simple valent simulation.
[22:35] It should be pretty fast.
[22:36] It's nothing complicated.
[22:37] We will just do a valent balloon.
[22:39] So valent configure balloon.
[22:42] And, oops, let's connect it in here.
[22:45] And let's do a valent solver.
[22:48] Let's all J and drag.
[22:50] Let's find.
[22:51] Let's see if it doesn't take too much to compile.
[22:53] Let's see in here.
[22:56] We will, before simulating, we will increase this cache and remove the gravity.
[23:07] Since I don't want this to fall down.
[23:09] And we will also introduce the ground plane.
[23:11] So it collides and it doesn't start to jump around.
[23:17] Since I want the bottom to be flat.
[23:20] So let's simulate.
[23:22] And we should have the sort of effect.
[23:24] So nothing is moving.
[23:26] Let's increase the pressure of this valent effect.
[23:34] Let's do the rest length.
[23:35] Let's save for.
[23:37] And I also want to increase the damping ratio.
[23:40] Now it's a bit more controlled.
[23:43] And I'm also going to increase the sub-steps.
[23:49] And this one, just to do.
[23:51] Let's see how that looks.
[23:53] So as you can see, it's creating that effect.
[23:56] But it's also starting to fly around and whatnot.
[24:01] So what we can do is to use another.
[24:07] So let me see.
[24:09] Did I change something in here?
[24:12] So let's do, first of all, a valent constraint.
[24:17] And let's do pin to target.
[24:20] So I want to keep it in the same position.
[24:23] So let's do pin to target.
[24:25] But right now it will just stay on the same place.
[24:29] And we will not inflate.
[24:31] So we actually need to make it soft.
[24:34] We need to make it soft.
[24:36] And I'm going to change this to 10.
[24:42] So it has some possibilities of expanding without flying around.
[24:49] So as you can see now it's working great.
[24:51] But it's also inflating and deflating all over the place.
[24:55] We can pick a frame, but just to control it, we can use the plasticity.
[25:00] In here, so on the stretch constraints.
[25:04] So enable plasticity.
[25:05] I'm going to change the threshold to 0.5 and the rate.
[25:09] So it stays more consistent to 5.
[25:13] Let's see how that looks.
[25:15] So now it should keep more or less the inflation.
[25:21] And as you can see, it's still wobbling around, but it's more consistent.
[25:26] I'm also going to change something on the cloud.
[25:30] So I'm going to let it have some geometry to play with for the inflation.
[25:38] So I'm going to increase the wrestling scale to 1.5.
[25:43] 100 is fine.
[25:44] And I might change the other rest is fine.
[25:47] Let's see, I changed anything on the valum pressure.
[25:51] So this is fine.
[25:55] And yeah, I think that's all.
[25:58] We can just have a look in here.
[26:02] Now it will have some more geometry to play with.
[26:07] And we can actually time shift the frame.
[26:10] So let's time shift.
[26:12] And we can do the frame.
[26:14] Let's say 25.
[26:16] And we should have something like this, which is a bit better.
[26:22] So before we move on, let's actually change something in here.
[26:25] So if we look at this in real time.
[26:30] So is wobbling quite a lot.
[26:33] So we can go in here in the process and change the velocity.
[26:37] Then being to 0.5.
[26:38] So it's a bit more controlled.
[26:40] So as you can see, it will be less wobbly.
[26:45] And this should be quite more stable.
[26:47] That's just an overall control if you're not animating.
[26:51] So let's do 25.
[26:53] That's fine.
[26:55] And now, as you can see, we still have some roundness in here and some gaps.
[27:01] And I want to fill those gaps.
[27:03] So for that, we can create a mask in between the shapes and do some picking of the geometry over there.
[27:12] But I'm not sure it's that easy to create a mask between the shapes without using the intersection function.
[27:20] Might be possible with just the race op.
[27:24] But I'm not sure.
[27:26] So let's actually use the intersect function and it will be a nice way to actually learn about it.
[27:35] So we have a bunch of attributes.
[27:37] Let's just delete everything.
[27:39] We don't need them.
[27:41] So let's delete non-selected and we have this.
[27:44] Let's add a normal and I believe I did it on points.
[27:48] Right?
[27:49] Yes.
[27:51] So normal on points.
[27:53] It's fine.
[27:54] And now we will explode these a bit so we can.
[27:59] So when we do the intersect function, it won't be we won't have intersecting geometry here in the middle.
[28:06] So we need to explode these a bit.
[28:08] So it's when exploded bill.
[28:11] Let's see.
[28:12] That's working fine.
[28:14] And I'm going to use a value of 0.097.
[28:19] So we will have some space.
[28:21] So the intersect function actually creates a full mask.
[28:24] It's not strictly necessary, but let's keep it like that.
[28:28] And before that, we will save a rest attribute.
[28:31] So we address it will be floated to current position.
[28:35] So later we can just run attributes.
[28:38] Or use a wrangle is the same.
[28:40] And the rest it will be equals to t.
[28:44] And we get back to the initial rest position.
[28:49] But right now we will do the intersect function.
[28:53] So this requires a bit of a setup.
[28:56] Let's do that.
[28:58] First of all, we will need the normal.
[29:01] So we will intersect on itself.
[29:04] And so we can find here the intersecting parts.
[29:09] So let's do, let's first of all, normalize the energy boot, which is the direction we will perform the ray operation.
[29:17] So normalize.
[29:19] V at n.
[29:22] And for the intersect function, we will need two variables.
[29:27] So we will need an iPod and a UVW.
[29:31] So we will need a position and a UV variable.
[29:37] So now we will create the intersect function.
[29:39] I'm going to call it hyperimp and do intersects.
[29:43] Of the current intersects, the current inputs on itself.
[29:48] And from the current position along the normal.
[29:52] And we will multiply here.
[29:55] So we can control the distance.
[29:59] We will also need iPods and I will be W.
[30:04] So I post I will be W.
[30:07] It's fine.
[30:08] Let's just create a mask.
[30:11] Let's call it mask for.
[30:13] And the iPream is so if it did something.
[30:16] So I bring is not equal to minus one.
[30:19] Just to make sure it did.
[30:22] I bring not equals to minus one.
[30:29] So is not factors.
[30:31] Sorry, is a float.
[30:35] I also I didn't call it iPream.
[30:38] So sorry.
[30:40] So let's look at that mask and create those.
[30:43] So as you can see, even if we play with the distance,
[30:46] we want to get the mask because we actually need is
[30:49] intersecting on itself.
[30:51] We need to offset a bit the position.
[30:53] So do a small peak.
[30:55] So we can do that really easily just by adding doing a peak.
[30:59] So along the normal and multiplied by point all of one.
[31:03] Let's say.
[31:04] And now it's creating that mask.
[31:06] As you can see.
[31:07] So now we have the mask.
[31:09] And let's do point all nine three.
[31:12] Let's say, let's find.
[31:14] We could also set a group if you want.
[31:17] So let's do I at group intersect.
[31:25] And we can do the iPream not equals to minus one.
[31:28] So let's look at that group on the points.
[31:31] And as you can see.
[31:34] So I bring.
[31:38] Should be creating the group right.
[31:41] I had to look intersect.
[31:43] I bring it was the minus one.
[31:45] Is it creating the group?
[31:49] So let's disable the visualization.
[31:55] Is creating the group.
[31:57] Well, we want need this.
[31:59] So let's forget about it.
[32:01] So let's move on.
[32:04] Let's.
[32:06] In this case, I don't think it's working.
[32:08] So let's move on.
[32:10] Let's do the attributes.
[32:11] We'll move it back to the position.
[32:13] And we have that attribute as you can see.
[32:16] Now we can just do.
[32:18] Let's look at the attribute and the one attribute player.
[32:20] So that's a particular.
[32:22] That specific attributes.
[32:25] So let's remove the position and use mask for.
[32:28] Let's increase it a bit.
[32:31] And in this case, I only use 10.
[32:36] And now we can do another angle to pick that mask.
[32:40] So let's so we have to be times equals to read along the normal and multiplied by the mask for.
[32:48] And we also need them displacement multipliers.
[32:51] So this.
[32:53] And this should work.
[32:55] Let's see.
[32:57] As you can see, it's closing those gaps.
[33:00] And I'm going to just use a value of point of.
[33:03] Let's remove that mask and let's.
[33:07] We can actually increase the splurring iterations.
[33:10] And as you can see, it's closing that cap, which is the result I want it.
[33:14] So a lot of work, but I guess it pays off.
[33:19] So let's just do now a simple smooth.
[33:24] We will do let's say 25.
[33:27] And this is almost done.
[33:30] Now we need to do some stitches that should be pretty easy and do these middle part in here.
[33:37] So let's actually hide the timeline since we don't need it anymore.
[33:41] And let's create now some stitches.
[33:44] So let's do an intersection analysis.
[33:48] And this should give us a nice result.
[33:50] So we can see and we will output intersection segments to have those lines.
[33:57] Let's unite the shape by doing a polypads.
[34:03] That should give us a single primitive.
[34:07] Now it's a bit wobbly so we can do when natural but lower.
[34:13] This now is amazing.
[34:15] So let's do along the.
[34:19] Let's remove the pin borders and do 100 iterations to have it quite smooth.
[34:26] Now I want to pick it a little bit, move it a bit in.
[34:29] So it stays a oops, it stays.
[34:34] A bit more in I guess let's see.
[34:36] Let's do an oriental on curve.
[34:39] We'll get the normal since right now we don't have them.
[34:42] And we want actually the x axis and let's output again.
[34:46] And that will be fine.
[34:48] I'm not sure I did the resample in here after the attribute blur.
[34:51] Yeah, the resample.
[34:54] And in this case I used a value of 0.001.
[35:01] So quite a bit I guess.
[35:06] Let me see.
[35:08] Yeah, I actually use a lot of points.
[35:11] Because I need them for the displacement for creating the stitches I guess.
[35:16] I don't need any I will need a curvy so let's keep it.
[35:22] And on the attribute blur I actually reduce the step size.
[35:27] So to about point of weight.
[35:30] So it doesn't blur so much.
[35:33] So now that we have the normals we can do a small flick so big.
[35:37] And we will need those normals to display along them.
[35:41] So we don't want to recompute and we will just a small peak.
[35:46] So minus point all three.
[35:50] As you can see and we still have the normals.
[35:53] So I'm just picking them a little bit in.
[35:55] We might need to adjust that in a bit.
[35:58] So now we can actually create the stitches and.
[36:05] Let's do a wrangle and we will take advantage of the scene function.
[36:10] And also using the curvy attribute and the normals.
[36:14] So we will display the position so V at B plus equals along the normals.
[36:21] And we will multiply it by the scene of the curvy.
[36:29] Curvy multiply by the amount of repetitions so we can do channel float.
[36:36] Let's call it reps.
[36:38] It's not really a great name.
[36:40] And to have a perfect repetition or revolution we will multiply it with by.
[36:46] And now we can just do a simple amplitude slider.
[36:50] So let's call it amp.
[36:52] Let's see if that works for us.
[36:55] So we will change the repetitions to 70 and play with the amplitude.
[37:00] And as you can see it's working.
[37:02] I'm going to choose the amplitude to point 0.5.
[37:05] And now it's going up and down along the normals.
[37:08] So I'm actually just for I just want positive values.
[37:12] So I'm going to do an absolute function to make them positive and close the bracket in here before the amplitude.
[37:18] So as you can see, creating the perfect pattern.
[37:22] So now we can just mesh this.
[37:26] Let's actually delete the normals.
[37:29] So we can delete everything and do a simple fuse.
[37:35] Because with the resample we will have open curves.
[37:39] And now let's do a sweep with a round tube.
[37:45] And we need to change of course the radius.
[37:49] So point 0.2.
[37:52] So I guess that's fine.
[37:55] Let's do a soften normals.
[37:58] Just in case.
[38:01] And we can organize this a bit better.
[38:05] And let's merge.
[38:07] Let's see how that goes over our.
[38:12] You can actually remove this mode in here and just do it.
[38:16] You know, near.
[38:17] Oops.
[38:18] So what am I moving in here?
[38:22] Let's do this.
[38:24] And as you can see, we did that small peak.
[38:28] And we can actually adjust it in here.
[38:31] But the this value will work by.
[38:34] And we have the stitches.
[38:36] Now it's pretty easy.
[38:37] We just need to do a simple to.
[38:42] So let's do it to let's visualize this.
[38:47] And we can use indirect mode.
[38:49] And let's.
[38:50] Oops.
[38:51] Let's offset this in here.
[38:52] Let's do end caps.
[38:55] It can.
[38:56] Oops.
[38:57] Now it's rotating.
[38:58] Right.
[38:59] That's great.
[39:00] We can move this up.
[39:02] And we can actually snap these to the grid.
[39:04] So if we do this and snap it in here, remove the snapping.
[39:09] And let's move it up.
[39:11] Oops.
[39:12] Now it's rotating.
[39:15] We can move this down.
[39:17] Let me see.
[39:19] I might need to increase this or control alt and drag.
[39:24] That's fine.
[39:26] And now let's do a poly bevel.
[39:29] So.
[39:30] Bevel.
[39:32] And we can use the flat edge, ignore flat edges and do point 1.1.
[39:39] And let's see five sub divisions.
[39:44] And I'm going to also increase the sub divisions initially to 64.
[39:50] To have a more rounded look.
[39:53] I guess this is fine.
[39:54] We can come in here and play a bit with this.
[39:59] So with this controller, that's fine.
[40:04] And let's merge it over.
[40:07] And create a north.
[40:10] And this will be out.
[40:13] So yeah, guys, a lot of work.
[40:16] I hope you have learned something new with this.
[40:19] As always, you can grab the file on my Patreon alongside with all the project files from my videos.
[40:25] And I have exclusive video tutorials, hours of exclusive videos.
[40:29] And also I have some courses in there that are pretty cheap if you want to check them out and support my work.
[40:35] Other than that, thank you for watching.
[40:37] And let me know in the comments if you enjoyed this one.
[40:39] Thank you.
[40:40] And I'll see you next time.



---

## Captured Frames

- [3:40] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_000.jpg
- [9:10] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_001.jpg
- [12:19] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_002.jpg
- [14:57] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_003.jpg
- [18:03] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_004.jpg
- [20:57] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_005.jpg
- [23:56] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_006.jpg
- [27:22] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_007.jpg
- [33:00] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_008.jpg
- [36:40] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_009.jpg
- [40:07] tutorials/frames/procedural-modeling-with-vex-vdb-and-vellum/frame_010.jpg

---

## Structured Notes

### Core Technique
Model a tufted circular couch/ottoman entirely from a hand-written VEX pipeline: a rotating, wrap-around ramp assembles a variable-width base profile from a 12-point circle, VDB cascading-noise softens the resulting extruded/beveled shell while preserving sharp seam edges, a Vellum balloon simulation inflates it into pillow-like cushions, and a from-scratch VEX self-intersection ("intersect") function closes the gaps between cushions before adding swept, sine-wave-displaced stitching detail.

### Summary
The couch starts from a 12-point circle converted to a single-primitive line, then re-assembled point-by-point with a VEX point wrangle that offsets each point's position via `prim()`-sampled curve data — creating a variable spacing ("ramp going around") so some sections of the couch profile are naturally smaller than others. The core VEX exercise walks through building this from primitives: sampling `xyzdist()`/`prim()` position and UV data from an input curve, applying a rotation via a `chf` slider with `%1` wraparound, then deriving a curve-parameter attribute (`vertexcurveparm()`, falling back to point number when vertices aren't available on point-only geometry) to drive a mirrored (`abs(u*2-1)`), sign-flipped (multiplied by `sign(P.z)`), power-function-remapped (`pow(u, upow)`) falloff that pulls points together at specific spots to fake a scalloped couch-cushion silhouette. This ramp-driven point cloud is turned into geometry (Add → Polygons by group, Convert Line, frame-ID attribute via primitive number, Resample to a fine circle, then `minpos()`-snapped back to a perfect circle to keep the falloff attribute while adding resolution). The shape is Poly-Extruded/Poly-Bevel'd, split into independent per-primitive pieces via Vertex Split (using the primitive-ID attribute), separately Poly-Extruded and Clipped into panel sections, boolean-unioned just to get a clean edge-angle group selection (since edge selection differs on separated vs. connected geometry), then chamfered/bevelled with Group Transfer to carry that selection back. A for-each loop (keyed on the earlier primitive-ID attribute) runs VDB operations per panel: an edge-angle mask ("shell mask") feeds VDB From Polygons and a masked VDB Smooth SDF (alpha = the mask, ~10 iterations) that rounds the panel interior while keeping the outer seam sharp, followed by a second unmasked single-iteration VDB Smooth SDF pass to clean texture artifacts, then VDB Convert to Polygons and a Remesh — wrapped in a Compile Block (multithreaded, no single-thread flag) for speed. The resulting clean remeshed shell is inflated with a Vellum Configure Balloon + Vellum Solver (no gravity, ground-plane collision, pressure/rest-length/damping-ratio tuning, Pin-to-Target constraint with a softness of ~10 so it can expand without flying apart, Plasticity enabled on stretch constraints with threshold 0.5/rate 5 to hold the inflated shape, and increased Rest Scale on the cloth so there's extra geometry available for wrinkling) — a Time Shift locks a representative simulated frame (e.g. frame 25) and Velocity Damping is increased for a calmer, non-animated pose. To close the remaining gaps between the separately-inflated cushion pieces, the tutorial builds a from-scratch VEX self-intersection ("intersect") function: normals are computed, geometry is exploded slightly (Point VOP-style explode by a small amount) so the intersect ray doesn't self-hit at zero distance, positions are saved to a rest attribute, then a wrangle uses `intersect()` (fed the current geometry against itself, current position offset slightly along the normal via `P + N*epsilon`, and an outgoing `hitpos`/`hituv`) to build a mask of points whose ray actually hit something (`primhit != -1`), which is then used with `attribvalue()`-based interpolation and Attribute Blur to smoothly pull the mask-selected points toward their hit position, closing the gap. Finally, an Intersection Analysis node extracts the seam curve as intersection segments, which is unified with Polypath, relaxed (Attribute Blur, no pin borders, ~100 iterations), Resampled/oriented (Orient Along Curve for banking-stable normals), and swept with a small tube profile after a VEX displacement wrangle adds sine-wave-based stitching detail along the curve (`sin(curvy * reps) * amp`, clamped positive with `abs()`), giving the couch its final piped seam and puckered-tuft look, finished with a Poly Bevel on the outer frame edges.

### Key Steps
1. Build a 12-point circle, Convert to Line, then reassemble the points with a `prim()`/`xyzlist()`-based point wrangle that offsets position from the primitive's sampled curve position — the classic "offset via `prim()` and reassemble with `xyzdist()`" pattern for procedural curve manipulation.
2. Add a rotation slider (`chf` angle, wrapped with `%1` so it loops smoothly) driving a `vertexcurveparm()`-derived U attribute (falling back to `ptnum`-based U on point-only geometry where vertices aren't available).
3. Mirror the U falloff with `abs(u*2-1)`, then flip its sign per-side using `sign(P.z)` so the pull-together effect works symmetrically on both halves of the couch profile.
4. Shape the falloff with a `pow(u, upow)` power function (values like multiplier 0.034, power 0.31) to control where the profile narrows vs. widens — a progressive effect instead of abrupt scaling.
5. Rebuild geometry from the ordered points (Add → Polygons by group, Convert Line), tag each primitive with a `frame_id` (int, primitive number) attribute for later per-section iteration, then Resample finer and `minpos()`-snap back to a perfect reference circle to add resolution while preserving the falloff attribute.
6. Poly Extrude/Poly Bevel the ring into a couch-panel shell, Vertex Split by the primitive-ID attribute to separate panels, Poly Extrude+Clip each into individual sections, and use a temporary Boolean Union just to get a clean max-edge-angle selection (since separated geometry selects differently than connected geometry) before Group-Transferring that selection back for bevelling.
7. Run VDB operations per panel inside a for-each loop keyed on the primitive-ID attribute (wrapped in a multithreaded Compile Block): build an edge-angle "shell mask" group → VDB From Polygons (with the mask passed as an alpha attribute) → masked VDB Smooth SDF (~10 iterations, alpha = mask, keeps the sharp outer seam while rounding the interior) → unmasked single-iteration VDB Smooth SDF cleanup → VDB Convert to Polygons → Remesh.
8. Inflate the remeshed shell with Vellum Configure Balloon + Vellum Solver: disable gravity, add a ground-plane collider, tune pressure/rest-length/damping ratio, add a Vellum Constraint (Pin to Target, softness ~10) so it can expand without flying apart, enable Plasticity on the stretch constraints (threshold 0.5, rate 5) to lock in the inflated shape, and increase the cloth's Rest Scale for extra wrinkle geometry; Time Shift to a representative frame (e.g. 25) and increase Velocity Damping for a calm still pose.
9. Close inter-cushion gaps with a from-scratch VEX self-intersection function: compute/normalize normals, explode the geometry slightly to avoid zero-distance self-hits, save a rest-position attribute, then use `intersect()` (current geometry vs. itself, ray origin offset slightly along the normal) to find hit points (mask = `primhit != -1`), and pull the masked points toward their `hitpos` with Attribute Blur smoothing to close the visible seam gap.
10. Extract the final seam with Intersection Analysis (output intersection segments), unify with Polypath, relax with Attribute Blur (no pin borders, ~100 iterations), Resample and Orient Along Curve (for stable banking normals) — then displace along the normal with a VEX sine-wave wrangle (`sin(curvy * reps) * amp`, `abs()`-clamped positive) to create repeating puckered stitching, and Sweep with a small round-tube profile for the final piped seam geometry.
11. Finish with Poly Bevel on the outer frame edges (flat-edge-ignoring, ~5 subdivisions, 64 initial subdivisions for roundness) and merge everything into the final couch output.

### Houdini Nodes / VEX / Settings
Circle (12 divisions, ZX plane), Convert Line, point wrangle (`prim()`, `xyzdist()`-style position offset), `chf` rotation slider with `%1` wraparound, `vertexcurveparm()` / point-number-based U fallback, `abs()` mirroring, `sign(P.z)` flip, `pow(u, upow)` falloff shaping, Add (Polygons by group), frame-ID attribute (int, primitive number), Resample, `minpos()` circle-snap wrangle, Poly Extrude, Poly Bevel, Vertex Split (by primitive ID), Clip, Boolean Union (selection-only trick), Group (max edge angle), Group Transfer, For-Each Named Primitive (keyed on frame-ID) wrapped in a multithreaded Compile Block, VDB From Polygons (with alpha/mask attribute), VDB Smooth SDF (masked + unmasked passes), VDB Convert to Polygons, Remesh, Vellum Configure Balloon, Vellum Solver (no gravity, ground collider, pressure/rest-length/damping tuning), Vellum Constraint (Pin to Target, softness), Plasticity (stretch constraints, threshold/rate), Rest Scale, Time Shift, Velocity Damping, VEX self-intersection wrangle (`intersect()`, `primhit`, `hitpos`, `hituv`, normal-offset peak), Attribute Blur, Intersection Analysis (output intersection segments), Polypath, Orient Along Curve, VEX sine-displacement wrangle (`sin()`, `abs()`, curve-view/reps/amp), Sweep (round tube), Poly Bevel (flat-edge-ignoring, high subdivision count for roundness).

### Difficulty
Advanced (combines hand-written VEX curve-manipulation math, per-section VDB compile-block workflows, Vellum balloon simulation tuning, and a from-scratch VEX self-intersection/gap-closing function).

### Houdini Version
Not specified.

### Tags
vex, vdb, vellum, xyzdist, quaternion, compile-block, upholstery, couch, curve-manipulation

---

## Related Tutorials
- [Sushi Modeling and Rendering in Houdini](sushi-modeling-and-rendering-in-houdini.md) — shares the Vellum Shape Match / grain-growth style de-intersection approach applied here to closing gaps between inflated cushion pieces.
- [Vellum Typography in Houdini](vellum-typography-in-houdini.md) — another Vellum-balloon-style inflation setup using Plasticity and Pin-to-Target constraints for a controlled puffy result.
- [Spiral Splash Tutorial in Houdini](spiral-splash-tutorial-in-houdini.md) — shares the from-scratch VEX quaternion/curve-parameter math approach used here for the ramp-driven profile assembly.
