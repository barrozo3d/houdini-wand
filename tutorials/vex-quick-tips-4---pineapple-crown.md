---
title: Vex Quick Tips #4 - Pineapple Crown
source: YouTube
url: https://www.youtube.com/watch?v=oDXQsMo2aaQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vex-quick-tips-4---pineapple-crown/
frame_count: 0
frame_status: pending-selection
---

# Vex Quick Tips #4 - Pineapple Crown

**Source:** [YouTube](https://www.youtube.com/watch?v=oDXQsMo2aaQ)
**Author:** cgside
**Duration:** 29m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vex-quick-tips-4---pineapple-crown <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So I've been building this pineapple model, procedural model in Odini and today I wanted
[0:07] to share how I did the crown in here, basically by doing manipulating attributes with wax.
[0:15] So I thought it would be a good exercise to share here on the channel and maybe you'll
[0:19] get a tip or two from it.
[0:21] So yeah, let's get into it.
[0:24] So let's start in a fresh new scene and drop a geocontainer.
[0:28] And we will start by creating a circle.
[0:31] So this is where we will instance the different lips.
[0:35] Let's set it to Exit plane to be on the grid and I'm going to change the division just to
[0:42] 7, which is more or less the amount of lips you have around.
[0:46] I'm also going to drop a polyframe to create polyframe to create the normals because we
[0:53] will need them in a bit.
[0:55] So in this case, I want to set this to N.
[0:58] So in this case, the point in, I would like them to point out.
[1:02] So I'm going to drop a wrangle and just invert them.
[1:06] So V at N times equals minus 1.
[1:11] So now they point out.
[1:12] So that should be fun.
[1:14] And now we will instance this into a line.
[1:17] So let's create that line.
[1:20] In this case, I'm going to use some values that work for me.
[1:23] So I'm going to set these along Y and a length of about 0.11.
[1:29] So quite small, as you can see.
[1:32] Two points that's fine.
[1:33] Now I'm going to resample these to where they find the amount.
[1:38] The resample.
[1:41] And I'm not sure if I'm creating a curve.
[1:42] I don't think so.
[1:43] Yeah.
[1:44] So I'm just going to set maximum segments of thick.
[1:48] So we have six segments.
[1:50] Let me increase the point size.
[1:53] Is it in here?
[1:54] No.
[1:54] Is in guides, the scale point marker size.
[1:58] Yeah.
[1:59] So we have six segments.
[2:01] As you can see.
[2:03] Now we can just try to copy these two points and see how that goes.
[2:10] So as you can see, that's fine.
[2:12] It's creating the different copies along the line.
[2:16] But I also want to adjust the p-scales.
[2:18] So what should we just float?
[2:22] And in this case, I'm going to set the p-scale to be changing along the bounding box, along
[2:29] the Y.
[2:30] So I'm going to set these two bounding box and set these to Y.
[2:33] And as you can see, it will start small and then grow.
[2:36] In this case, I'm going to set pretty small values.
[2:39] So around 0.04 on the minimum value and about 0.01 in the maximum value.
[2:48] So as you can see, it's creating this cascading effect.
[2:52] I believe I didn't change anything else in here.
[2:54] Then what we can do, we can create a class for each geometry.
[2:59] So let's do that with an attribute wrangle.
[3:03] And we will create a class.
[3:05] It will be equal to the point number.
[3:09] So now we should have a class and we don't need to drop in a connectivity or something
[3:12] like that.
[3:13] Let me set this to flat display.
[3:16] So that's our first part done.
[3:18] Now let's see, what else do we have in here?
[3:21] We will need to rotate this to create the pattern of the leaves which are based to the golden
[3:30] ratio or golden angle.
[3:33] So we'll have to do that.
[3:34] But for now, let's just try to copy these two points.
[3:37] So if I create a line in here and I make it along the Z axis and a length of 0.2 something,
[3:46] and now we copy these two points.
[3:51] And we will start to create the different leaves that later will be leaves.
[3:58] I mean, so now we need to adjust the few things.
[4:01] Before we do the rotation that will be a bit more convoluted, we can just work on the
[4:10] rotation because we need to move this up.
[4:14] So we have the normals as you can see that we created.
[4:16] We have the normals of the geometry.
[4:18] So from here we can create a nap vector, so attribute wrangle.
[4:23] And let's create a nap vector.
[4:25] So in this case, just by doing a cross product between the normals and the y axis.
[4:34] So v at up, it will be equal to normalize.
[4:37] Always normalize when you're doing cross products.
[4:40] And we will do cross between the normals and a nap vector, let's say 0, 1, 0.
[4:48] And we should have a nap.
[4:52] And let's look at that up.
[4:54] It will be like this.
[4:58] And now what we can do, we can, in order to rotate these leaves up, we will do a natural
[5:05] vector just vector.
[5:08] And in here, we will manipulate the normals.
[5:13] So in this case, we'll manipulate the normals.
[5:16] So let's set the normals.
[5:19] And we will just play with the direction and rotate.
[5:23] And we will rotate around the up.
[5:26] And if we rotate, now we can move this up as you can see.
[5:30] And let's rotate it by 70 degrees, something like this.
[5:35] And now we need to play with the p-scale also.
[5:38] So let's do an attribute to just float.
[5:41] And you can play with the p-scale, but I'm going to be a bit more precise in here.
[5:49] So I'm going to do again the same thing.
[5:50] So bounding box.
[5:53] And along y, and in this case, I want to, I mean, value of 0.2 or something, and I'm
[6:00] it's value of 1.
[6:01] So it increases along the y axis.
[6:05] Start small and then increases.
[6:06] That's the visual feedback I got from a reference.
[6:12] So that's something already, but we still need to work a bit more on this.
[6:18] So let's do that in an acupart.
[6:21] So the idea now is to create some sort of bounding on these, some bend effect on these curves.
[6:28] So they drop, let's say with gravity, and we want to create that bend effect.
[6:35] So for that, I'm going to use a rig wrangle.
[6:38] And we can do that.
[6:40] Let's start.
[6:41] Well, let's just drop the rig wrangle.
[6:49] We will need a transform.
[6:51] So let's create an oriental on curve.
[6:53] This ones work very well, but I'm going to show you how to solve that.
[6:58] So let's drop the oriental on curve and export the transform attributes.
[7:02] And we can have a look at that transform if we scale it down.
[7:07] And it will look something like this, which if we do it one at the time, it would be easier
[7:14] to set up.
[7:15] But in this case, I want to do it all at once.
[7:18] So let's create a wrangle, the rig wrangle.
[7:21] But in this case, I'm just going to make sure I have I resemble this and have a curve
[7:28] view.
[7:29] So I'm going to resemble this curves because right now, they only have two points.
[7:33] So I'm going to resemble.
[7:35] Let me see what sort of value I use.
[7:36] So about point 0.01.
[7:39] So quite a bit of resemble.
[7:40] And I also want the curve view.
[7:42] So now we can deform them along the curve view.
[7:45] So let's look at the curve view.
[7:47] Because you can see it starts at 0 at the bottom and goes to 1.
[7:52] All right, let's manipulate that curve view that you put.
[7:55] So I'm going to create a variable called angle angle.
[8:01] And it will be a channel float that we can change.
[8:06] Then I'm going to create just an extra step to have the possibility to offset the curve
[8:14] view.
[8:15] So in this case, I'm going to grab the f curve view.
[8:19] And I'm going to subtract a channel float called offset.
[8:24] And you will see in a bit how it works.
[8:26] And then I'm going to make sure this doesn't go below 0 or above 1.
[8:32] So I'm going to claim this between 0 and 1, this straight color in front wall.
[8:40] And I'm going to multiply the angle by the offset and another attribute that we'll
[8:46] work in a bit.
[8:48] And then we can just to pre-rotate or at local transform or at local transform.
[8:56] And we will rotate by the angle and along, let's say, the x axis.
[9:01] See if that works for us.
[9:03] Oops, 1,00.
[9:07] So no errors.
[9:08] And now we can play with the angle.
[9:11] But as you can see, our transform is working in some cases.
[9:15] But not in the...
[9:17] I mean, it's not working at all.
[9:18] This is all a mess because we need to calculate the proper transform attribute because
[9:23] this one is not giving a circuit result, as you can see.
[9:28] So let's calculate that transform.
[9:32] And for that, we need to take a step back.
[9:35] So let's remove this oriental on curve and let's go back and calculate the proper
[9:40] transform.
[9:41] First of all, we need to...
[9:44] Let's see, let's disable this.
[9:48] And as you can see, they all go in the same position.
[9:52] And we need to offset them along the y axis.
[9:55] So before we create the transform, we will do the rotation along the y axis.
[10:03] So I'm trying to do this in a way that makes sense.
[10:05] I'm not doing this linearly.
[10:07] So I have some things that I have to go back and do one step at a time so you can follow
[10:13] along better.
[10:15] So I'm going to start by creating a bounding box along y with the relative point bounding
[10:20] box that I'm going to use later.
[10:22] So I'm going to call it relative bounding box y.
[10:25] And it will be relative point relative point bounding box.
[10:30] And coming geometry, VHP, and I just want the y axis.
[10:34] This will just create a follow-off along the y that I'm going to use in a bit.
[10:39] Then I'm going to create in here a variable called golden angle.
[10:46] That will be the amount of rotation we will perform.
[10:49] And this will be the fixed value.
[10:50] So in radians, I'm going to set it to 137.5.
[10:57] That's the golden angle.
[10:59] And I'm going to multiply that by the class.
[11:01] So along the different pieces, the different pieces.
[11:05] So I'm going to get the angle, or not the angle, sorry, the golden angle, and multiply it
[11:12] by the class.
[11:14] So it rotates along the different pieces.
[11:19] Then we need to actually do the rotation.
[11:21] So let's do a vector for called what?
[11:25] And it will be of what turnian.
[11:27] And we will rotate the golden angle.
[11:32] And it will rotate along the y axis.
[11:35] So 0, 1, 0.
[11:38] That is fine.
[11:39] Now we just need to do the rotation.
[11:40] So VHP will be equal to Q roll date.
[11:44] And we will rotate that returnian.
[11:46] And we will change the position.
[11:49] So now we should have rotated as you can see.
[11:52] And if we look at the result, we will have something like this, which in this case, let
[12:00] me see.
[12:01] Yeah, this just wrote if I disable this in here.
[12:07] As you can see, this just rotates along the y axis.
[12:11] I believe this is correct.
[12:13] Yeah, I guess so.
[12:15] So let's just continue and we'll see how that goes.
[12:19] Let me just check in here.
[12:23] So over there's something wrong in here because we are rotating.
[12:30] But if you see the normals, they have a bit hard to see.
[12:34] So let me go to guides and scale normal.
[12:38] As you can see, the normals don't get rotated.
[12:41] And they get all messed up.
[12:43] So we also need to rotate the normals.
[12:45] So let's go with V at n.
[12:49] And we can rotate the n.
[12:52] And now we should have the correct normals.
[12:54] And as you can see, now it's all organized.
[12:57] And you see by the alternating pattern in here along the y.
[13:02] That's why we did that rotation with a golden angle, whatever that means.
[13:05] Anyways, that's our rotation then.
[13:07] Now that we have the normals properly oriented with that rotation, we want to create the
[13:12] transform attribute.
[13:15] So for the transform attribute, that shouldn't be too difficult.
[13:20] We will create in here the we will set the vector n.
[13:25] It will be, let's just normalize it, normalize V at n.
[13:31] Let me increase that for you.
[13:33] Then we will take advantage of the look at function.
[13:39] Let's just create the different cross products by default.
[13:43] We don't need to worry about that.
[13:45] So we will do, and this takes as an arguments from 2 and up.
[13:51] So from 2 and up.
[13:55] And we need to define those.
[13:57] So the n will be our 2 axis, our 2 component.
[14:04] And in this case, we want to invert it.
[14:07] And the vector from can just be 0, 0, 0.
[14:14] And the up just along y.
[14:16] So vector up set 0, 1, 0.
[14:23] And now we have the look at.
[14:24] Let's just save that as an x form.
[14:27] So x form, oops.
[14:31] x form, 3 by 3 matrix.
[14:35] And let's also save.
[14:37] I might need this.
[14:39] So I'm going to save these normals as an alternative attribute.
[14:45] And of course, it's narrowing out because I don't have still equals in here.
[14:52] So let's look at that transform and see what it did.
[14:55] So let's actually remove these normals in here.
[15:00] And look at the x form.
[15:01] Make sure we set these as a marker and as an axis and reduce.
[15:07] So as you can see, we have the z axis pointing out.
[15:13] We have the up axis, the up is the green.
[15:16] And we have the cross product of that along the x axis, let's say.
[15:25] So that should give us an nice transform for our orientation.
[15:30] So we copy these two points.
[15:32] And now we enable this attribute wrangled, but it won't recognize that attribute that we created.
[15:37] So and the reason I didn't collect transform is because it will affect our copy to points
[15:43] and not pay attention to p scale or normal or anything.
[15:46] It will just prioritize the transform attribute.
[15:50] So we will do inside attributes swap.
[15:53] And we will do a move from the x form and we will name it transform.
[16:00] And now as you can see, our transform is working perfectly.
[16:03] And we can come in here and play with the bending and we can bend it as much as we want.
[16:08] And we can also play with the offset and bend just the tips.
[16:12] This case, I didn't use offsets and what sorts of values did I use in here?
[16:18] So let me see point 15.
[16:20] So point 15 will be the correct approach.
[16:25] Now we can do a simple sweep and create the geometry.
[16:31] So let's create a ribbon and reduce the size.
[16:37] We can reverse this.
[16:38] And let's enable the lighting and remove this.
[16:44] And we can just apply a scale and change these to where is the preset?
[16:49] So feel and change it to this plane.
[16:53] We can possibly increase these and change the bottom.
[16:58] And we start to get the desired results.
[17:00] But I still want to manipulate this a bit.
[17:03] I want to create some dance in these lips.
[17:07] That's typical to pineapple grounds.
[17:09] And that will be an extra step if you want to keep watching.
[17:13] Let's meet in the in the next part.
[17:17] So there are still a few things I want to change about this rotation
[17:20] because in my reference data don't rotate so much at the top.
[17:24] They are a bit more straight.
[17:26] So that should be easy when create a drug or to just float.
[17:32] I'm going to call it relative bounding box.
[17:37] And I'm going to change these to bounding box and a long wide default settings.
[17:42] And now I can just come in here and multiply this by that attribute.
[17:50] And now it wants to do that in reverse this.
[17:55] So zero and one.
[17:56] Yeah.
[17:56] And we can come in here and invert this.
[17:59] Something like this.
[18:00] So they will rotate more in the bottom and less at the top.
[18:04] Or we can just invert it in here is the same.
[18:07] So now we want to create some dance on the on the sides of the lips on the edges.
[18:15] And for that we will need to do the meshing in a different way.
[18:19] So this is what I came up with.
[18:21] It's a bit over the top to be complicated.
[18:24] But he should allow us to do this directly without having to point the form or without having to do.
[18:35] Some rigging some deformation with the bond the form that we can also do.
[18:41] I tried different approaches and this one was working the best for me.
[18:45] So instead of output in geometry, I'm going to change these to columns and change this to one only.
[18:51] And this will create a geometry.
[18:53] And now we just this place these.
[18:56] This curves along the normals with a sign function.
[19:00] So let's see.
[19:01] Of course, we don't have any normals.
[19:03] So these won't be properly oriented.
[19:06] So let's go one step at a time.
[19:09] So I'm going to create the sweep and I'm going to set this to point all six three.
[19:16] That's the value I used.
[19:19] And we can also change the p scale along the along the Y.
[19:25] But I'm not going to worry about it now.
[19:28] So having these curves, we can do a re-sample.
[19:31] And we will re-sample quite a bit to have enough geometry.
[19:36] So point 0, 0, 0, 5.
[19:39] So quite a bit as you can see, you can change how much you want.
[19:43] And I'm going to set these to subdivision curves.
[19:45] That's any problem.
[19:47] Otherwise, we will get faceting on our curves.
[19:50] I'm going to also output the curve view.
[19:53] And the first thing I'm going to do is to create a orient along curve.
[19:59] And I'm going to set the tangent to when.
[20:01] So let's see how that works.
[20:02] Oops.
[20:03] Let's disable the re-sample and scale the normal quite a bit down.
[20:08] So this is just the tangent along the curve.
[20:12] As you can see, it's following the curve that will be important for us.
[20:16] And what's the next step in here?
[20:18] So we can now, let's do the displacement and see our issue.
[20:25] So attribute wrangle.
[20:28] And we can do v at p plus equals v at n, also along the normals.
[20:37] And we will do a scene of the curve view, scene of the curve view,
[20:43] multiply by the repetitions.
[20:48] And we can also multiply it by byte, we have a perfect offset.
[20:54] And then we can just multiply everything.
[20:57] So multiply everything by an amount of displacement.
[21:02] So, like this.
[21:06] So this won't work very well.
[21:07] Let's change the repetitions to 65.
[21:10] And let's create the displacement.
[21:12] As you can see, the normals are not great.
[21:15] Let's remove these normals.
[21:18] And just move the position.
[21:20] So as you can see, we need a proper normal for this to work.
[21:23] Because right now we don't have that.
[21:28] So let's undo and do the normal.
[21:31] And let's do this.
[21:36] So first of all, we need to calculate the proper normal.
[21:40] And we need to go a step back and create the orientation
[21:46] when we do this copy to points.
[21:48] So right in here, after we change the normals,
[21:53] we will need to create an attribute.
[21:54] So attribute wrangle.
[21:57] And we will create the double cross-problems.
[22:02] So if you remember, we saved out an attribute called underscore N.
[22:07] And if we have a look at that, so marker vector.
[22:13] That's a copy of our normals.
[22:17] And we can take the attributes and do a cross-brow with the normals.
[22:22] So vector vector side, it will be close to normalize.
[22:28] And we will cross between the normals and that's an attribute.
[22:36] And now if we do v, we save out these attributes.
[22:40] We add out, it will be close to normalize and another cross between the side.
[22:46] And again, the normal attribute.
[22:49] Let's see what that gives us.
[22:52] So I am writing this.
[22:53] OK.
[22:54] And of course, this will reroute because so normalize cross and normalize cross between the side and the end.
[23:14] So this is correct.
[23:15] Oh, I need an equal sign in here.
[23:19] So let's look at that attribute.
[23:21] So let's enable this and create a marker and vector.
[23:28] And this will be the orientation that we need.
[23:33] Because right here we are changing the normals, the rotation of the normals.
[23:38] And we need that orientation to feed into our, as you can see, this is the attribute we need to feed into our curves.
[23:47] Not only that, we also need an extra step in here.
[23:50] So we already have this out attribute that we will take advantage.
[23:55] And after the rig wrangle, we also need that rotation that we got from the rig wrangle.
[24:02] So as you can see, if I rotate this now, it won't follow.
[24:06] And I try to rotate it in here, but this is doing something in the background with the transform attribute that I'm not sure how to mimic.
[24:14] How to do the rotation right in here.
[24:16] So we will do it in a slightly different way.
[24:19] So after the attribute wrangle, we will create the proper axis that we will need later.
[24:32] So let's create a wrangle and other wrangle and you're probably tired of this.
[24:38] So let's call it vector local x.
[24:43] And it will be a normalized between the out and the vector I believe.
[24:52] So set 0, 1, 0.
[24:56] Let's see how that looks.
[24:57] So we have the local x.
[25:00] It will be equal to local x.
[25:04] Low call x.
[25:07] Today I can type.
[25:09] So what's the problem in here?
[25:12] Local underscore x.
[25:16] What's the problem in here?
[25:19] So normalized off.
[25:21] Sorry, we need to cross in here.
[25:24] Sorry about that.
[25:25] So cross.
[25:28] That should work.
[25:29] Let's see how that looks.
[25:30] So if we look at that local x and marker and vector.
[25:37] And as you can see, we now have the proper orientation.
[25:42] With the rotation and everything, we now have the proper orientation to do the displacement.
[25:49] As you can see, it's following the shape of the curve.
[25:53] And if we do the sweep, now we just need to invert the first primitive or invert the second.
[25:59] So for that,
[26:02] we will have to do again something.
[26:05] So let's see our displacements.
[26:11] Let's reduce these.
[26:14] And it's still displacing along the normals that we haven't defined yet.
[26:19] So let's do another wrangle in here.
[26:21] Yeah, another wrangle.
[26:24] And we will do V at n.
[26:28] We'll be equal to V at local x.
[26:33] And now is displacing, but we have the same direction in both sides.
[26:37] So we need to invert this somehow.
[26:39] Let's enable this.
[26:41] Let's reduce the displacement to 001.
[26:45] Let me pick in here.
[26:46] As you can see, it's inverted in this side.
[26:48] So what we can do is simply do a sign.
[26:52] So float sign will be equal to I at frame number modulo 2.
[26:59] And we need a value between minus 1 and 1.
[27:02] So let's multiply this by 2.0 and subtract 1.
[27:06] And now we can just multiply this by the sign or inverted sign.
[27:11] And now as you can see, it's working perfectly.
[27:14] So but this is creating some sort of well design wave, which is rounded.
[27:19] So what we can do is to do, I believe it's called a sign,
[27:25] which is always called a,
[27:29] missing here a sign, not sign, sorry, which is the arc sign.
[27:35] And we do these in here, I believe.
[27:38] And now we will have the the flat look or this serrated look.
[27:47] And a lot of work just to create this.
[27:49] But as you can see, we now have a proper orientation and everything should work fine.
[27:54] So let's do.
[27:57] Let's create the geometry now.
[27:59] And for that, I'm just going to use a very cheap method of using the skin.
[28:04] Up and this will connect everything.
[28:07] If we do group of end premiums, it will connect just to and we do normals.
[28:14] And let's see, they are inverted so we can reverse them in here.
[28:20] And yeah, everything should be working as you can see.
[28:24] And we can probably play with the displacement.
[28:28] So a bit less.
[28:31] And now we can do a UV flattened and disabled manually out and they will be properly oriented.
[28:40] And you can also decrease the p scale along.
[28:41] Why, but you know how to do that already we've done most of that.
[28:47] We've done plenty of that in this lesson.
[28:50] So just with the bounding box.
[28:52] And yeah, guys, as you can see, this is not as straightforward as I would like it to be.
[28:58] And I tend to over complicate things and create try to create nice setups to share with you guys.
[29:04] And hopefully you got some tips out of this.
[29:08] If you didn't understand everything, go ahead and leave a comment.
[29:13] And I might try to explain it better.
[29:16] And as always, you can grab the file on my patron alongside with exclusive tutorials.
[29:21] And I also have some courses in there that you can check out.
[29:24] And please let me know in the comments if this was useful in any ways.
[29:28] We did quite a few things and we tried to do this in a clean way, but I understand that with so many angles.
[29:35] Sometimes is hard to follow, but we didn't do very complicated stuff.
[29:42] Most of it was quite simple.
[29:44] Maybe the most complicated part was this look at function or the rest is just cross products and manipulating attributes.
[29:52] Hopefully this was well helpful and I'll see you next time. Thank you.



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
