---
title: Houdini Mini Course  |  Cops, Vex and Karma
source: YouTube
url: https://www.youtube.com/watch?v=24vjgnyZRTw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-mini-course-cops-vex-and-karma/
frame_count: 0
frame_status: pending-selection
---

# Houdini Mini Course  |  Cops, Vex and Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=24vjgnyZRTw)
**Author:** cgside
**Duration:** 54m38s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-mini-course-cops-vex-and-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back to this video we'll create this scene from scratch.
[0:05] We'll touch on topics such as Cops, extensively, some Vax concepts and also how to set up
[0:12] the scene in Solaris and do the final render.
[0:15] So yeah hopefully you will find this useful and let's get started.


### Generating the points and attributes [0:19]
**Transcript (timestamped):**
[0:19] So in order to set up the scene we will use a bit of Vax combining SOAP and Cops.
[0:26] We could probably do something similar with the tile sampler in the Copnet work but
[0:33] I want a very particular look where some rocks are more rotated than others and it will
[0:38] be a good chance to combine both workflows of the SOAPs and Cops.
[0:43] So yeah let's get started by dropping a geometry container.
[0:46] Oops, geocontainer.
[0:48] Oh, I already have a geocontainer in here.
[0:51] Okay, let's create the grid and this will be on the ZX plane that's fine.
[0:58] We'll set the size of 1 by 1 and in this case I'm going to use 21 rows and 21 columns.
[1:07] And now we'll extract the centroid from this so we can just create an attribute wrangle
[1:12] or do the extract centroid is the same but I'm going to set these to primitives.
[1:17] Let's find to the current inputs and position and remove prim
[1:26] current inputs at prim norm.
[1:30] These will create points on the centroid.
[1:32] Remove prim 0, prim norm.
[1:35] Remove
[1:38] prim 0 at prim norm.
[1:42] So waste is not working.
[1:45] Int int.
[1:46] Oh, we need we need to add a one in here so remove the points also.
[1:57] Now that we have the points I want to remove some of the middle points and place a single
[2:04] one in there so we can add the out in a logo or any logo you want to place in there.
[2:10] So I'm going to create another wrangle.
[2:12] So this will be a lot of wrangles but hopefully you will learn something from it.
[2:18] So we're going to create a mask from the center.
[2:20] So float center equals length v at p.
[2:27] So the length of the position and we can actually visualize that by assigning to an attribute
[2:35] and you can see that we have a mask from the center.
[2:39] It's not normalized but that's okay.
[2:42] Now we can leave this one.
[2:44] Now we will delete some points in the center so if center smaller than some threshold we
[2:55] will remove the points.
[2:59] Remove points 0 incoming inputs and ptina.
[3:06] So let's see how that works.
[3:08] And you can see is relating from the center in a circular pattern.
[3:12] In this case I just a value of 173.
[3:16] So something like this.
[3:18] And now what's next?
[3:20] Now we will add the point to the center.
[3:22] So create another wrangle.
[3:25] And in this case we just want to add one point so let's add it to the detail.
[3:29] Let's create a vector bounding about center.
[3:31] It will be get bounding box center.
[3:34] 0 inputs and let's create a detail.
[3:38] Let's reboot in this case and let's add the point.
[3:43] 0, pbc.
[3:46] Let's see if that works for us.
[3:47] It does.
[3:48] Let's disable the mask and we have that point in the center.
[3:55] So now we need to tell the co-network which layer to use in the points.
[4:06] So in this middle point I want to use the layer 1 or the stamp one.
[4:11] And in all the other ones I want to use the stamp 0.
[4:15] So for that we will create another wrangle.
[4:19] And let's set these to points.
[4:21] And we need to set the stamp attribute.
[4:23] It's all the co-network recognizes it.
[4:25] And I'm going to do a simple if statement with the select function.
[4:30] And I'm going to say that it in AMP is equal to detail 0 center points.
[4:39] So if the point number is the center point so if we are targeting this one we will set
[4:45] it the layer to 1 or the stamp to 1 otherwise set it to 0.
[4:50] Let's see if that works for us.
[4:52] So if we set this stamp and we set it to marker and we have 0 and 1 in the middle.
[4:59] So we need to do quite a bit of setup to make this work but hopefully in the end it will
[5:05] be worth it.
[5:06] I'm going to also use the same expression to set the p-scale.
[5:13] I have some values so in this case I'm going to use 5 for the center one and 1 for all
[5:19] the other ones.
[5:22] Let's see what next.
[5:24] Now we will group some random points.
[5:26] We could use a group node but just to keep it this wax base based approach.
[5:35] We will use some wrangle.
[5:37] And I'm going to create a group named RandsPines.
[5:42] And it's going to be random of the bitinum.
[5:47] Let's see it.
[5:52] And I'm going to say that this is smaller than some threshold.
[5:57] So the threshold.
[6:00] And let's see.
[6:03] And we can actually get this copy this name and I'll put it in here.
[6:09] So let's make sure we select some points.
[6:12] In this case I add a value of 0.272 and a seed of 7.
[6:19] So these random points that we have will have a different amount of rotation.
[6:23] It's just a particular look I was after that I saw in my reference.
[6:28] You don't need to follow that but in this case we are doing it this way.
[6:34] So next we need to take care of the rotations.
[6:39] And we are about done with the slops attack.
[6:43] So let's create just random attributes.
[6:46] A attribute to just float.
[6:49] And I'm going to call it mask.
[6:52] Rot which will mask the rotation.
[6:55] We will multiply it with some rotation values.
[6:58] I'm going to set it to random.
[7:02] And I have some values in here.
[7:04] A value of 0.08 and a default value a seed of 14.
[7:11] And this will be more visible in a bit.
[7:14] But for now let's just set up this and a default value that we will assign to all the other
[7:20] points.
[7:23] So we have that set up.
[7:24] Now let's do the most complicated parts which is the rotations.
[7:31] We will be able to see right after this the cop result.
[7:38] Let's create a seed.
[7:39] And seed is equal to channel integer seed.
[7:48] Let's create the attribute for cop.
[7:50] So in this case we will need them along the y.
[7:54] So set 0.10.
[7:58] Let's create the normal along the x in this case.
[8:05] 1 0 0.
[8:08] And now we need some random value.
[8:12] So I'm going to call it load.
[8:15] I'm going to call it amount n.
[8:19] And it will be a rent.
[8:22] And we will rotate it randomly between minus pi and pi.
[8:33] So, so float amount pi equals to a feet of 1, amount n.
[8:43] So the previous value and between minus pi and pi.
[8:49] And now we can just multiply.
[8:51] So let's actually do the cotterion first.
[8:54] So vector for what will be equal to cotterion.
[9:00] And the amount the angle we want to rotate is the amount pi and along the axis of the
[9:09] and now we just need to rotate it.
[9:11] So rot will be equal to u rotate, rotate the cotterion and to the n.
[9:22] And now we just need to assign this to the normal.
[9:26] So quite a bit of setup.
[9:28] But now let's actually do work out network.
[9:35] And let's do a sub import.
[9:38] Let's first of all create the null in here.
[9:41] And name it out.
[9:44] Finds.
[9:46] Let's copy control C. Sub import use external and paste.
[9:52] Now we will rest arise the setup.
[9:56] And we want to move it to the cop space, which will be in the position and bounding box
[10:02] scale to fit.
[10:05] And this case I think I used.
[10:09] And I used the app.
[10:11] Yes.
[10:12] So this case the app, which is the fault space for the cop network.
[10:18] Now let's stamp the point.
[10:21] And this will be the point and let's see if we change the radius, which in this case
[10:27] I use a value of point 0 for 2.
[10:31] And as you can see we have a lot of random rotations.
[10:35] Let's pin this view.
[10:36] And now let's go again in here.
[10:40] And let's multiply the rotation by the mask that we created.
[10:46] So in this case we need to go in here and say amount by.
[10:51] Oops.
[10:52] The amount by times equals have at mask rot.
[11:01] And this will rotate them.
[11:04] But in this case we want to target the points in here.
[11:08] So in this case I'm going to say the group type, the group to be not the random points
[11:15] we selected.
[11:17] So you can see we rotate more those values in the random points.
[11:25] And yeah, I guess this is it.
[11:28] Now let me check something.
[11:31] We also need an attribute noise in here.
[11:34] So attribute noise, attribute noise.
[11:38] And beyond CD.
[11:42] In this case we will use in the B.
[11:46] And this will be too much.
[11:47] So we want 0 centred and point of 3.
[11:52] And an element scale of point 11.
[11:56] Oops.
[11:59] And what is going on in here?
[12:05] So if we remove this, let me see.
[12:13] Do we want it to be so much of a noise?
[12:18] Am I doing this properly?
[12:19] Oh, we don't want to recompute the normals.
[12:25] That's why it was not working.
[12:28] So let's actually pin this and let's make sure we don't recompute the normals in the
[12:34] post process I think.
[12:37] So there we have the random positions.
[12:40] So we just scatter them around a little bit.
[12:44] And in this case, I played with the offset.
[12:46] I'm going to repeat it the same way.
[12:48] So as you can see, some of the tiles or some of the stones will have more rotation than
[12:53] others.
[12:55] And this is just a particular look I found.
[12:57] Well, you don't have to follow this, but that's what we have for now.
[13:01] Let's keep going on the next part.


### Initial displacement texture in Cops [13:05]
**Transcript (timestamped):**
[13:06] So now we also want to put a logo in here.
[13:09] In this case, I'm going to use the Arduino logo.
[13:11] So let's go in here and add a new stamp.
[13:15] Stop too.
[13:16] And as you can see, we have that logo in there.
[13:20] And I'm going to load a file.
[13:23] Let me check in here.
[13:24] I just downloaded a logo from the side effects website.
[13:28] And I'm going to place in here.
[13:32] So this is the logo.
[13:33] And we will RGB to RGB8 to mono.
[13:39] So to convert this to a mono, let's make sure we set this to maximum.
[13:43] To have the white value.
[13:45] And now we can connect this to the stamp one.
[13:48] And we will have this now.
[13:56] I have a different result in this case.
[13:59] Let me see.
[14:03] I might need to play with orientation in here.
[14:07] So let me make sure I have the correct seeds.
[14:13] I mean, we can play around with this setup.
[14:18] But in this case, I'm going to make sure I have the same seed.
[14:22] So same seed.
[14:26] And then we have a tribute just float.
[14:29] And we can play with the seed in here.
[14:31] So yeah, we need to set a different seed.
[14:34] So you can play around in this case.
[14:37] I'm going to pick the number seven.
[14:39] All right.
[14:41] So now that we have everything saved.
[14:45] And let's see.
[14:46] We have the ID.
[14:47] We have the UVs.
[14:49] And we have the stamp.
[14:50] So we have everything we need.
[14:54] What we will create next.
[14:55] So we have a vibrato in here.
[14:59] So we will just create a distort first.
[15:02] So this start.
[15:04] Distort.
[15:06] And we will distort this stamp.
[15:10] And we will create a fracon noise.
[15:15] And we will set it to UV and center to zero.
[15:19] Let's make sure we distort all the way, I believe.
[15:22] Yes.
[15:24] And then we can play with the amplitude.
[15:26] So just say 1, 0, 16, and the element size of 0.08.
[15:38] So something like this, maybe a little less.
[15:46] So something along those lines.
[15:49] So we just want a bit of distortion.
[15:53] And in this case, I changed the noise type to Berlin.
[16:00] So it has a bit more effect on it.
[16:02] Reset the viewport.
[16:06] So what else we will do?
[16:08] We will create another fracon noise.
[16:11] So let's copy this one.
[16:14] And in this case, we will set the center to 0.5.
[16:17] So we reset and set this to 1.
[16:20] And we will use Warly Cellular F2F1.
[16:24] And why is this?
[16:27] So let's have an amplitude of 0.7 and change the element size.
[16:38] Something like this.
[16:40] And maybe a register of this.
[16:42] So something along those lines.
[16:45] Now we will remap this.
[16:47] So remap.
[16:50] Because we want to introduce some cracks.
[16:52] This is just a shape way of doing it.
[16:55] And I'm going to change the mean and the max.
[17:03] Something like this.
[17:07] And I'm going to use a similar set up in here.
[17:11] Let it start.
[17:12] Let's see all that looks.
[17:14] In this case, I used a bigger amplitude.
[17:19] And a bigger element size.
[17:24] Nothing like this.
[17:27] Now we can take a minimum.
[17:33] Which is just a blend mode.
[17:36] And we will take these as foreground.
[17:39] And distort as background.
[17:43] So let's see.
[17:44] And we introduce some cracks in here.
[17:48] OK.
[17:49] Now we will convert this.
[17:53] We will create segments by connectivity.
[17:59] So we can have some ID.
[18:04] As you can see.
[18:07] As you can see, I don't believe I didn't play with anything.
[18:12] And now let me see.
[18:17] Create a random moment.
[18:21] And connect the ID to the seeds.
[18:26] And in this case, we want to have the black background.
[18:29] A seed of 21.
[18:32] The rest will be fine.
[18:34] And now we will take another random mono.
[18:39] And get the ID from here.
[18:46] And for this one, we'll set the seed to 36.
[18:52] And play with this ramp.
[18:53] I believe I set it to black.
[18:55] And update the constant.
[19:03] I can see which one I used.
[19:05] So it's flat.
[19:07] Or I need one value in here.
[19:09] So we're just removing some of the stems.
[19:15] So this case, about 79.
[19:20] Maybe a bit more.
[19:24] Something like this.
[19:28] And now we will blend.
[19:32] So after this random moment, we will blend.
[19:39] And we will blend these as a mask.
[19:45] And again, let me see.
[19:49] As a part round, we will get this one.
[19:58] And this one as a background.
[20:00] Let's see how it looks.
[20:02] So we're taking the random mono and the other one.
[20:07] And we're just widening and lightening some of the tiles.
[20:11] So now we will extract some parts from it with a compare.
[20:22] And compare, we will set this to A greater than B.
[20:31] Let's see.
[20:32] And play with the threshold.
[20:33] So we'll just remove some of the parts in this case.
[20:38] I set it to 0.315.
[20:43] This will be fine.
[20:49] And this is our new texture.
[20:54] And let's keep going on the next part.


### Creating the Albedo in Cops [20:58]
**Transcript (timestamped):**
[20:59] OK, now let's create the Albedo texture or the diffuse texture.
[21:02] So for that, I'm going to load a file.
[21:04] It will be easier than just play around with random noises.
[21:08] And I'm going to use this texture from Polyaven.
[21:11] And then I'm going to UV sample.
[21:14] So this will be the texture.
[21:16] And I'm going to set it to RGB instead of RGBA.
[21:20] Because we will use this in the base color.
[21:24] And let's connect this to the UV.
[21:28] And if we look at the result, we will sample the texture.
[21:33] Let's set this to 2K for now.
[21:36] And this already looks better in the end.
[21:38] We might change the resolution.
[21:42] So now we will multiply this.
[21:48] Since here we have all the stones, we will multiply this
[21:51] with our current mask.
[21:53] So let's sample this.
[21:57] It doesn't matter which input it is.
[21:59] So we will multiply it with this.
[22:03] So let's make it do this.
[22:05] And we will get this sort of result.
[22:10] And after that, we will add some random color corrections.
[22:20] So from the seeds, we will create a random moment.
[22:25] So let's create a random moment.
[22:28] And connect this to our which one did I connect?
[22:34] So in this case, the first one.
[22:37] So let's connect this to maybe let's do it different.
[22:41] Let's connect it to this one.
[22:46] And I want to make sure I do zero negative by this.
[22:51] And what else?
[22:53] We can't click it like this.
[22:57] And now let's do one.
[22:58] I just read just this is this is just like the color correction
[23:02] node.
[23:04] Now, if we increase the saturation, you can see everything
[23:06] will get the same saturation.
[23:08] But if we introduce this to the mask, some will have some
[23:11] will not according to these mask as you can see.
[23:17] Which I don't know which sort of values I use in here,
[23:19] but maybe a value of 1.4, a year shift of five.
[23:26] Let's see.
[23:28] Maybe.
[23:31] And the rest I get this same way.
[23:34] Let's see.
[23:36] In truth of some saturation.
[23:40] And if we remove the mask, let's keep it like this.
[23:46] What else will we will do?
[23:47] We will create the ground texture.
[23:52] In this case, I'm going to be lazy and use the exact same one.
[23:56] There's color corrected.
[23:57] So I'm going to create an a just via just.
[24:03] And I'm going to this case, I'm going to reduce the value.
[24:07] Something like this.
[24:10] And now I'll blend it.
[24:12] So let's create a blend.
[24:15] And these will be the foreground.
[24:19] And as the background, we will use this one.
[24:21] And as a mask, we will use this one or mask.
[24:27] So let's keep it like this.
[24:31] Some ways are to organize these networks.
[24:34] As you can see, we already have a pretty cool diffuse
[24:37] texture, or albedo.
[24:41] Let's maybe do some vinyl adjustments
[24:44] with an a just via just.
[24:46] So this is an overall color correction.
[24:48] Or you can do it in karma.
[24:51] In this case, I'm going to use you something.
[25:02] So a bit more, something like this.
[25:05] Increase just a bit the saturation.
[25:09] And a bit of the value scale also.
[25:15] So something like this is just an overall color correction.
[25:21] Let me see if that looks similar.
[25:23] It does.
[25:24] And now let's just create a null.
[25:27] And call this albedo.
[25:33] So that's our main texture then.


### Creating the Displacement in Cops [25:38]
**Transcript (timestamped):**
[25:38] So now let's create the displacement.
[25:41] So we can take this ID and create a random moment.
[25:50] Oops, connect this to the seeds and make this very negative.
[26:02] Yeah, we can take this one.
[26:04] And I'm going to set the seed of 30.
[26:08] And multiply this over our current mask.
[26:12] So this is our current displacement map.
[26:16] So we multiply this.
[26:23] Not this one.
[26:24] Sorry.
[26:25] This one in here after the compare.
[26:29] So we'll get this sort of result.
[26:33] Now we can add some elevation variations.
[26:36] So some tones will be on an angle.
[26:41] So for that, I'm going to take the UVs and the UV transform.
[26:48] And in this case, I'm going to also take the seed,
[26:56] the ID as a seed, and do some random rotations around 180.
[27:04] And I played with the seed also.
[27:07] So something like this, as you can see,
[27:10] they will rotate around.
[27:13] And now we can take this and create a ramp.
[27:18] So let's create a ramp moment.
[27:21] Take the UVs to the position.
[27:24] And this will be fine.
[27:28] And now we can multiply this over our current results.
[27:32] So multiply and oops.
[27:38] And take this.
[27:41] This will just create some elevation variation.
[27:44] But in this case, I don't want it so intense.
[27:49] So about 0.56.
[27:58] And let's see.
[28:03] Maybe this is too much, but let's keep it like that.
[28:08] So let's try to create a material.
[28:12] So create a material and connect this to the Alpeon or this color.
[28:17] And this is displacement.
[28:19] So the I channel right away, I'm going
[28:22] to change the displacement amount 0.5 and change this to 500.
[28:30] Let's see how that looks.
[28:33] So maybe this is too much.
[28:36] Let's see how much I use.
[28:39] So 0.25.
[28:44] So something along these lines, I can see
[28:48] that some of the stones are really steep.
[28:53] So maybe we can remove some of these blending.
[29:00] And maybe in here, we just random model where we randomize
[29:07] the height in this case.
[29:09] We can change this a bit.
[29:11] So now I'm just improvising, but it should give
[29:14] a similar result, hopefully.
[29:18] So I still want to add some noise to the stones and some blurring.
[29:26] In this case, I'm going to create a fertile noise.
[29:29] So after this fertile noise.
[29:34] And this will be around 0.08.
[29:39] And the rest is fine.
[29:40] Maybe reduce a bit to roughness.
[29:44] And I'm going to multiply it over our current displacement
[29:52] amount.
[29:54] This case reduce it a bit.
[29:57] And now we will take another fertile noise,
[30:01] because I want to change the size and around 0.03
[30:07] and change it to parallel in this case.
[30:11] And rest is fine.
[30:14] Then we want to remat this.
[30:18] I just want to create some overall displacement on the rocks.
[30:22] Let's see how that looks.
[30:24] That won't give us much.
[30:26] It's a bit hard to see.
[30:27] But maybe if we introduce these noise, and in this case,
[30:31] I'm going to play with these outputs.
[30:35] I don't want to displace it as much.
[30:38] And in this case, let me see.
[30:49] Let's see the final result.
[30:50] I want some more displacement in this case.
[30:53] So let's reduce these noise.
[30:57] And also maybe a bit 1,000 divisions.
[31:05] It's a bit hard to see.
[31:06] But we start to see, let me play with this specular.
[31:11] So as you can see, we have that noise on the surface.
[31:15] And now this noise, we will let it all blend this.
[31:24] And we will take this as the four grounds.
[31:27] And this one as the background.
[31:29] This is just the noise for the dark texture or the ground
[31:32] part.
[31:34] And we will take at the moment.
[31:38] So which one will take the compare notes?
[31:43] So we should create an all-in-year.
[31:47] But it's fine.
[31:49] So this will just add some noise to the background.
[31:51] And let's connect this to the height.
[31:55] And yeah, this is the sort of result we get.
[31:59] We will be able to introduce a bit more displacement.
[32:04] So that is fine.
[32:08] I wonder why, oops, why the logo is not so displaced.
[32:13] Let me see.
[32:16] This should be as white.
[32:19] I'm multiplying in here.
[32:23] Maybe we shouldn't take the random monofram here,
[32:26] but actually from here, from this ID.
[32:32] This is OK.
[32:33] Yeah, something like this.
[32:44] And we can play with the seeds.
[32:46] So we have more displacement in here.
[32:48] These lines.
[32:50] But I don't think this is correct.
[32:53] So maybe let's go back again.
[32:55] And get it from here.
[33:00] This will look better, hopefully.
[33:03] Let's see.
[33:04] And now we have some more displacement in the logo.
[33:10] What else?
[33:11] We might want to blur a bit the displacement map.
[33:21] So maybe give it a slight blur.
[33:27] Not so much.
[33:28] Let's just point over one.
[33:31] Let's create another.
[33:34] And call it this.
[33:39] And let's work on the roughness map next.


### Creating the Roughness in Cops [33:45]
**Transcript (timestamped):**
[33:46] So now let's create the roughness map.
[33:50] So for that, I'm going to take before the HSV adjust.
[33:55] I'm going to create RGB to mono.
[33:58] This will be just a sheep way of doing it.
[34:02] You can load the specular map from this texture,
[34:05] but or the roughness map.
[34:07] But I'm going to just create it like this.
[34:11] And now we will remap and change the input max to around 0.6.
[34:17] So I want still some specs of some specular highlights.
[34:24] So I'm going to keep it like this.
[34:26] And now I'm going to introduce some variation.
[34:28] So let's keep this.
[34:31] I'm going to create a fractal noise.
[34:34] Oops.
[34:37] And increase these to about 0.15.
[34:44] And maybe a bit of the roughness.
[34:47] And now let's remap these.
[34:51] And I did some heavy remaping these.
[34:55] So input max to 0.4 something.
[34:58] And this one, around 0.7.
[35:02] So something like this.
[35:04] And now let me see if I played with offset in this case now.
[35:09] But we can.
[35:11] And then just multiply this over the top of our specular map.
[35:20] In this case, we don't want to multiply.
[35:21] So we want to max.
[35:24] So maximum.
[35:26] So we have some, maybe we can decrease the scale to have some
[35:32] light areas, let's say.
[35:34] And we might want to reduce a bit the effect, something like this.
[35:40] Introduce some blurring.
[35:41] In this case, I don't want it as much.
[35:48] 0.3 will be fine.
[35:52] And let's see if we get enough and call this rough.
[36:00] And let's connect these to the roughness.
[36:08] So this one to look like much right now.
[36:11] I want this rainy look on the ground.
[36:14] So this will be ideal.
[36:17] Or now.
[36:17] And then we can adjust it if needed.
[36:22] So that's the roughness done.
[36:24] And we have our full network.
[36:27] I don't believe I'm forgetting anything.
[36:29] So we have the albedo, the roughness, and the displacements.
[36:36] I mean, it's not something great, but hopefully you have learned
[36:44] something new from this.
[36:45] And now to finish it off, we will do the rendering in karma.
[36:51] So now we will move into Solaris.
[36:53] Let's just change this to 4K.
[36:56] And let it calculate.
[36:58] Let's make sure we have the resolution.
[37:02] And we do the diffuse file that I use is 4K also.
[37:06] So it will work nice.
[37:09] And the rest will be procedural.
[37:11] So we will have no issues with that.


### Creating the geometry/Initial setup in Solaris [37:14]
**Transcript (timestamped):**
[37:14] So out of geometry context, we will not use any of these.
[37:19] So let's move to Solaris.
[37:23] I'm going to change a few things.
[37:25] I'm going to make sure the camera is rendering the view
[37:27] in port size and the background can be dark and not display the environment lights.
[37:34] Let's do a subcreate.
[37:38] And we will use the grid and set some initial divisions like 50.
[37:46] Let's create the UV texture and an output.
[37:53] And this UV texture will be reversed.
[37:55] So we need to reverse in here and make sure we are in the first style.
[38:02] Now let's create just a name.
[38:04] This will be the grid for our workground.
[38:08] And we will name it round yes.
[38:13] Now we will use the same one, but in this case create the mountain.
[38:21] And I changed in this case to a worldly cell.
[38:27] This doesn't need to be forward.
[38:31] But let's maybe might want to subdivide this.
[38:39] And I'm going to change the element size and play with the offset.
[38:49] Let me see.
[38:51] I just want to create some paddles.
[38:54] Maybe we can go into the wrapping and create some lettuce warp and gradient warp.
[39:03] So something along those lines.
[39:07] And now let's create a name.
[39:12] So we can target the salaries and name it water.
[39:16] Now let's launch this.
[39:23] And we need to move this up quite a bit.
[39:25] So transform.
[39:26] Let's enable the transform.
[39:30] And it will be tough like so.
[39:35] Maybe.
[39:37] Maybe a bit more.
[39:39] So now it's the part where you can get creative.
[39:43] I'm just going to do it quickly so I don't waste much of your time.
[39:49] And I believe this is the setup for now.
[39:54] Now we can create some initial setup.
[39:57] We will need render geometry settings to change the displacement quality.
[40:04] We will need the material library for our materials.
[40:07] We will need the dome light.
[40:11] And also the karma setting, render settings.
[40:19] And let's...
[40:20] Oh now I'm going to use an HDRI from PolyEvon.
[40:26] So change this to let alone.
[40:30] Like a desk, I HDRI.


### Creating the materials and camera in Solaris [40:32]
**Transcript (timestamped):**
[40:33] Let's create the material so we can start to see.
[40:36] I'm going to use the builder.
[40:39] And I'm going to change this to round.
[40:43] Oops.
[40:44] Round, matte.
[40:50] And we will just load the texture.
[40:52] So image.
[40:54] Let's see if we have them copied.
[40:57] Nope.
[40:58] So OP.
[40:59] And we have OPJ.
[41:02] Kio.
[41:03] And I've copied that.
[41:06] And I'll be there.
[41:07] So that is frame.
[41:08] And it's an RGB.
[41:09] Let's connect it to the base color.
[41:11] Let's duplicate and select the roughness.
[41:15] And change this to float.
[41:17] Connect this to the specular roughness.
[41:22] And take this one as float also infinitely.
[41:26] And do this.
[41:30] Now we will connect this to the displacement.
[41:34] So displacement.
[41:36] And we will change this to 5.
[41:40] Since our scene now is 10 times bigger, we will need more displacement.
[41:45] If you want to keep the same size or the same values, you might want to use a grid of
[41:49] 1 by 1.
[41:52] So let's create also the water material.
[42:00] And I'm going to use a color material at builder.
[42:03] And then we will add the water matte.
[42:08] I'm going to go to the transmissions, set it to 1.
[42:13] I have some color, some light blue color.
[42:17] You don't have to follow this.
[42:21] And I'm going to change the depth.
[42:24] And I believe that.
[42:26] So very simple water material.
[42:28] This is not a rendering masterclass.
[42:31] So just keep that in mind.
[42:37] So let's add a few materials and assign to geometry.
[42:40] And I'm going to select the wound.
[42:43] Connect it in here.
[42:45] And the water.
[42:46] Connect it in here.
[42:49] So let's disable the light in here and create a camera.
[42:55] So we will go in here.
[42:58] And maybe something along those lines.
[43:05] So let's go in here and your camera.
[43:11] And let's fill in the view.
[43:16] Something like this.
[43:20] We might change that.
[43:22] Let's set this to light.
[43:25] And go to the camera mess.
[43:27] Let's set it to 1.
[43:29] All right.
[43:31] Now we will create another light.
[43:35] But let's just render like this and see how it looks.
[43:42] So nothing much.
[43:43] We can see some pedals here and there.
[43:46] But we will change this.
[43:48] And it will have a dramatic impact in our render.


### Adjusting the displacement quality [43:51]
**Transcript (timestamped):**
[43:51] So in this case, we will select the render geometry settings
[43:57] and target the ground.
[44:00] And we will set the dicing to a higher value.
[44:05] In this case, I chose 1.5.
[44:06] It's a bit too much.
[44:07] But for this simple scene, we don't make a difference.
[44:10] Well, depending on your hardware, of course.
[44:12] And let's see if that helps us with the displacements.
[44:16] And we start to see some more displacements.
[44:20] Maybe the displacement amount is too much.
[44:23] Now that I see it.
[44:24] But let's keep it like that for now.
[44:27] And now we will create a new light.


### Adding the main light with gobo(ramble) [44:29]
**Transcript (timestamped):**
[44:30] So let me just check where did I use that light.
[44:38] So let's see.
[44:41] We have a camera in here.
[44:43] And we want a light coming from here.
[44:45] So let's create a light.
[44:47] Let's disable this one for now.
[44:51] And this one will be a rectangle light.
[44:55] So rectangle.
[44:58] And it's maybe able to select it.
[45:04] So we can go look to a light, light one.
[45:09] And make sure we don't lock the view.
[45:15] And in this case, I want it something along these lines.
[45:26] Let's see our light in this case.
[45:29] And we want to use a global.
[45:33] So I'm going to create a light filter library.
[45:39] So let's filter a library.
[45:42] It's a mouthful.
[45:43] And create a global.
[45:45] And I'm going to use a global from grayscale burry light
[45:49] belief.
[45:50] I got some years ago.
[45:51] And I don't believe I'd change anything in here.
[45:56] Now I just need to apply it to the light.
[46:01] So this case, I'm going to use the light.
[46:07] I'm going to go in here, light filter, and select.
[46:12] Light filter, global.
[46:18] I believe that's how we do it.
[46:20] And I'm also going to change the width.
[46:23] Let's see how that looks by default.
[46:25] So if we take a quick render, of course,
[46:30] we need to increase the intensity.
[46:33] So 10 and 14.
[46:37] And let's see if that copo is taking effect.
[46:41] Maybe we need to reduce the size.
[46:43] Something like 0.2 and 0.2.
[46:47] And we start to see the effect of that copo.
[46:52] Now I don't remember how I did this.
[46:55] But let's see if it's in here.
[47:01] So in the transform tab, I'm going to enable look at it.
[47:12] And it's hard to see that copo taking effect.
[47:17] So let's actually render this.
[47:21] So maybe what is done.
[47:29] The exchange the scale.
[47:36] Let me see if I have similar quality here.
[47:39] I didn't change the scale.
[47:42] So maybe I'll just move these down.
[47:44] Oops.
[47:47] Let's move these down.
[47:58] Several.
[47:59] Let's see how it can run.
[48:03] And this is not.
[48:06] So let's see again.
[48:07] I'm having.
[48:08] Oops.
[48:12] So my graphics card just tripped.
[48:14] I need to restart the thing.
[48:16] Let's see if we can get these lights to look properly.
[48:21] So something along those lines.
[48:23] And to be honest, I'm going to change this to some values
[48:26] I have.
[48:26] So point seven, six.
[48:29] And this can be like this.
[48:31] And I'm going to change the rotation.
[48:34] And around this end look at them.
[48:38] I'm going to play with it.
[48:40] And it looks something like my.
[48:44] I see.
[48:47] And still looks way different.
[48:56] But let's get it like this.
[48:56] So this will be our result.
[49:00] And now we can introduce the.
[49:03] The light.
[49:03] So let's do it.
[49:05] And I'm going to change this.
[49:07] The intensity of the sunlight to 0.35.
[49:10] Let's see how that looks.
[49:13] And that will dramatically.
[49:15] It will change dramatically to the look.
[49:17] Maybe let's reduce the intensity of the area light.
[49:21] So 12.
[49:23] 13.


### Find the issue with the gobo/light [49:26]
**Transcript (timestamped):**
[49:26] I'm not sure if I'm getting the global.
[49:30] So I feel the I'm the global.
[49:34] Let's subtly.
[49:39] Why the hell this is 1.2.2.
[49:49] Oh, it looks better.
[49:51] Where was I changing the size of the.
[49:57] So something like that.
[49:59] Now we can see a bit better the global.
[50:01] Let's look at our camera.
[50:03] And now let's go to the camera.


### Adding depth of field in Karma [50:04]
**Transcript (timestamped):**
[50:06] Select the camera node.
[50:08] We can't do shift.
[50:10] And let's place our focus.
[50:13] We'd like to click and hold in shift.
[50:16] Let's go to the camera.
[50:17] And in this case, I use the next stop of 0.1.
[50:24] And let's see how that looks.
[50:27] So something like that is a bit different from my final results.


### Some adjustments [50:28]
**Transcript (timestamped):**
[50:31] Maybe we can play a bit with displacement amounts.
[50:35] I think it's too much.
[50:36] So let's go in there.
[50:39] Decrease this to 0.38.
[50:44] Do we need to restart the render?
[50:50] So as you can see, that global is having a nice effect.
[50:53] And again, this is not a rendering master class.
[50:56] And neither I am especially a specialist in that.
[51:00] But we try to do a bit of everything.
[51:01] And sometimes things work.
[51:03] Sometimes they don't work as well.
[51:07] But maybe let's play with a bit of this.
[51:15] Let's see.
[51:15] Let's jump in this.
[51:18] And we can add a bit less element size.
[51:25] And also play with the specularity.
[51:28] So specular 0.05.
[51:32] Let's see how that looks.
[51:35] And you can play around until you feel this is OK.
[51:41] But I believe I'm going to leave it right here.
[51:44] Maybe we can play with the object context.
[51:51] And in here, in the displacement, where I'm
[51:56] mading is.
[52:01] So maybe we can reduce the effect.
[52:04] And let's restart the render to the displacement.
[52:08] And that's a bit less aggressive.
[52:13] And what else can we do?
[52:16] In my final scene, I had a bit more specular.
[52:23] So let's maybe go to the stage, take this light, and move it a bit in.
[52:33] Not seeing the ground displacement.
[52:46] So maybe we need to go in here and reduce these offsets of 1.
[52:54] 1.
[52:57] So I think that's it, guys.
[53:09] Hopefully you learned something new.
[53:11] Let me know in the comments if you enjoyed this one.
[53:14] And if you want to check out my Patreon, where you can find this scene file along with
[53:21] hundreds of other scene files, hours of exclusive tutorials like this one.
[53:26] And also, I have been there exclusive courses that you can also check out.
[53:33] And forgive me if this was not a perfect result.
[53:38] But now that I'm seeing in here a strange thing.
[53:44] I'm actually going to move this down a bit.
[53:52] Hopefully that's what I mean.
[53:55] And let's see.
[53:57] It's hard to see in here.
[53:59] Now let's also change this to HBO, change it to 512 and the final render.
[54:03] Oh yeah, guys, this is our final render.


### Final Render and Outro [54:04]
**Transcript (timestamped):**
[54:06] I just moved a bit up the water grid and also played a bit with the specularity.
[54:13] I would like to have more specular highlights around here, but it doesn't look bad, right?
[54:18] It's not as bad as I thought it would be.
[54:22] So hopefully you enjoyed this one.
[54:23] Again, thank you for watching and please leave a comment if you want to leave a positive
[54:29] comment or negative.
[54:31] But leave a comment.
[54:32] I always like to hear your thoughts.
[54:34] So thank you for watching and I'll see you next time.



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
