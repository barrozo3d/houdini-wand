---
title: Think Procedural Think Houdini
source: YouTube
url: https://www.youtube.com/watch?v=TWQvmqhRX3M
author: cgside
ingested: 2026-07-13
houdini_version: "21.0"
tags: [brick-wall, growth-solver, pcopen, matrix, pack-inject, edge-damage, procedural-modeling, sop-solver]
extraction_status: complete
frames_dir: tutorials/frames/think-procedural-think-houdini/
frame_count: 16
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Think Procedural Think Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=TWQvmqhRX3M)
**Author:** cgside
**Duration:** 56m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video we will be building this brick wall step by step.
[0:06] I promise you that if you stick around you will learn quite a few techniques from growth
[0:12] solvers simplified to manipulating transform attributes, there will be many many tips and tricks.
[0:19] Although we will be using a bit of Vax, it just very slightly, we won't touch on very
[0:25] advanced topics, so hopefully this will be easy to follow. So yeah, with that in mind let's get started.
[0:34] So I just saved a new scene and we will drop a Geo container and start with a line, very simple.
[0:40] We don't need walls, we don't need cubes or something like that, we will just start with a line.
[0:47] And I'm gonna orient this line along the x-axis, so 1,00.
[0:53] And two points will be fine because we will be taking advantage of that.
[0:58] And now I'm just gonna copy and transform. I believe I'm gonna copy these 24 times, yes.
[1:04] And just copy. We don't need to transform or anything, we will be manipulating the transform,
[1:10] the Peligen attribute, with just attribute adjust floats. But I want to output the copy name,
[1:16] which is just an attribute on the primitives, that has the, like the prim index,
[1:21] the prim number. So each line has a number and we have that as a attribute.
[1:27] We will promote that attribute to point, so attribute to promote, because we need it on points,
[1:31] not on prim, so from primitive to point the copy name. And we will start by manipulating the
[1:39] position dot y, so we want to move this up. So let's do a attribute to just float.
[1:44] And the attribute we want to manipulate is the b dot y. I didn't know we could do this.
[1:51] I just learned about recently, like a few months ago, and it's really powerful. You can manipulate
[1:56] the position and do many randomized effects. So we will be, in this case, there's a bunch of
[2:05] options with these attribute adjust floats. They are really powerful, so we will remap
[2:10] an attribute, and the attributes we're going to remap is the copy name.
[2:16] And we will be placing a max value of two. And right now we will, the attribute adjust floats,
[2:23] doesn't know how the range, so we need to input the range. And for that, we can just use
[2:28] end-premes. So the number of primitives in the input one, in the first input, minus one in this case.
[2:35] You can see if I don't subtract one, we won't count the last primitive.
[2:44] So now we should have, if I go in here, we should have from zero to one, the lines are
[2:52] placed. And from here, that's all I want to do in this. So now we want to manipulate the
[3:01] position.exe to create the profile. So I'm going to duplicate this one. And in this case,
[3:07] I'm going to adjust the position.exe. But as you can see, it's using this ramp to move it along,
[3:14] by the way, I'm going to just increase in here the value. But I just want to manipulate
[3:19] those outer points and not these ones. And as you can see, these ones are the even, and these ones
[3:26] are the odds. So what we can do is to manipulate every other one. But in this case, it's moving
[3:34] the even. So we can just sort by why and reverse. And as you can see, now we're manipulating these
[3:41] ones. And I want to set it to this case to multiply. And now I can play with the ramp and create
[3:48] my profile. I'm just going to copy the profile from my file. So I'm just, I just created the near
[3:56] a profile instead of me typing, you just need to, to play with it. In this case, I chose this
[4:05] profile. Now the next one, I'm going to call these. So just I just profile. And now I'm just going
[4:21] to do a natural to just float. And I'm going to just multiply these effects. So you can actually
[4:30] duplicate this. And now we will do add and constant and just manipulate in here, I'm going to set it
[4:40] to point three. Yeah, it's basically it's just increasing to create the brick wall. Hopefully you
[4:48] you see where we're going with this. So multi file. And now I'm going to create some random height
[4:59] in here. So move the lines up and down. So you already probably guessed how we're going to do that.
[5:05] In this case, we're going to just position dot y. And what we're going to do is to
[5:15] choose random. But as you can see, it's picking the element number. We want to pick a custom
[5:19] attribute and pick a name. And we don't want to we don't want to flag so a linear ramp. And in this
[5:31] case, I'm just going to pick random ads, min and max position dot y and not the nigger. And then I
[5:39] can just have a random number between a negative adjusted value. So a pretty fine value and a positive
[5:48] value. In this case, I'm just going to pick a very small value. And we had just this random
[5:54] transform. And I'm going to be the seed. Let's see. So you're probably not seeing that you can play
[6:01] with the seed in here. So this one is a random y. So we don't need to do fancy rangles. We just
[6:12] use what we have by default in ODE using default notes. Then I want to create the brick patterns
[6:18] because right now we just have we just have these curves with two points. So I'm going to do a
[6:26] resample. And we don't want the fixed amount of points on each curve. We want
[6:34] by length. So in this case, I chose a value of 0.2 that's more or less like a brick size.
[6:39] So we can name it resample and brick number of bricks. And we can actually color it.
[6:48] So that's fine. Now I want to select the end points. So I'm just going to do a group expression.
[6:54] And this is the first bit of wax that we're going to do. And I'm just going to say points and
[7:01] name the group ends. And we will select the point number. So I at pitonum is equally close to
[7:08] prim points. So each prim as points. And we will be wearing the points that each prim as. So
[7:19] prim points input 0. And just I at prim num. So for each prim primitive. And we want to get the
[7:28] first point. So we get first and we do now the same for the last point. And in fact, the last
[7:35] point is just minus one. And we get the end points. So that was easy. And now I'm grouping these
[7:41] points because I want to randomize the positions positive and negative along the line of these
[7:47] middle points. So let's do that in a wrangle. So I'm going to call it RANs. Pause.
[7:55] And let's do this. So first of all, I want to select just the points in the middle. So I can
[8:01] just say points and not ends. It was easier to select the end points and the middle ones. So
[8:06] just in part in India. And now we want to get a random position based on the point number. So for
[8:17] each point, I want a random number, but also randomize it by the prim num. So we're always sure that
[8:25] we get in our randomization. So in order to create a random number, we can do load, random
[8:30] pause. And let me increase that for you. And we will do RANs. And we will do it as a seed. We will
[8:38] use the ptnm plus the premium plus some random number. And I can have a seed to control the result.
[8:51] And from here, I can make it this will output a value between zero and one. So I want values between
[8:58] minus one and one. So I'm just going to multiply this by two and subtract one. This will make it
[9:06] between the range of minus one and one. And then I'm just going to multiply everything
[9:12] by an amp slider. So an amplitude or a displacement, just overall multiplier. I'm going to pick a
[9:20] 0.4 and an amp 0.025. Not much. Then we will need a curve view. So a curve view is just a value
[9:30] that goes from 0 to 1 along the curve based on the point. So in order to get a curve view on the
[9:36] fly, we could use the function vertex curve per M and feed in the geometry and the vertex number.
[9:44] And if you don't know what this means, we can assign it to one natural boot. And you see we have a value
[9:56] 0 to 1. Oh, we don't have it at the ends because I'm selecting it here. So as you can see, I'm selecting
[10:03] those ends. We don't have value one, but it's just a value from 0 to 1 on each curve. So you probably
[10:09] know that by now. So why do we want the curve view? Because now we can offset it. So you plus
[10:14] equals, runs, posts. And now to get the new position, we can just use another function. So we
[10:22] will assign to the position of those points. And we can use the function. Green UV that takes
[10:30] the current geometry. And we want the attribute we want to get. We want to get the position,
[10:34] the new position that we will sample based. We need to feed it the prime number. So each curve.
[10:42] And we can sample by you. Now we get a random position so I can offset it more. We can play with
[10:50] the seed. And yeah, that's basically it. So hopefully it wasn't very difficult to follow.
[10:57] And now we will extrude this up. But if you remember, we don't have fixed Y positions or a common Y
[11:09] position. We actually have a randomized one because we moved them randomly in this attribute.
[11:16] We want to just float. So we need to calculate the I. So another angle, but this one is going to be
[11:21] really easy. So this one is just the following. We will do it on point. So vector plus it will be
[11:35] we want to read the position of the prime. So it's like the center point of the prime.
[11:39] Or on its line. And we will use I. So we want to read each position. And then we can read the next
[11:46] position. So prime one plus one. And this will be pose one. And now we can do the follow. We can
[11:53] save F at this tail. It will be the position one position to name it position to sorry position to
[12:03] dot Y minus position dot Y. And now we should have a this scale. I'm calling it this scale
[12:14] because that's what I'm going to read to the X-road node. And that's the default attribute. So as you
[12:21] can see, we have been here the scale. There's one primitive that has a negative value and that's
[12:26] the primitive above because we don't have an X-prim. So what we can do now is just blast that last
[12:33] frame because we need it. So we can just place this character is like a poster for I don't know
[12:43] to be sure. I don't know for sure. I mean, so we can just do get the last primitive and delete it.
[12:49] So end-prim on the incoming geometry minus one. And as you can see, we delete the last one.
[12:55] Last, last can be with the color. So the next step is to actually right now we have
[13:04] single primitives and now we will convert line. And now we get, as you can see, we start to get
[13:12] these bricks that we can now just extrude. But in order to extrude, we need the natural roots. So
[13:19] I'm going to do attribute to just vector and I'm going to call it just up. You can call it n.
[13:25] And I'm just gonna set always ends, create a value along the y axis. So as you can see,
[13:33] just the vector pointing up. Let me get rid of this visualization. And now we can do the X-road.
[13:42] And we can extrude it up. But as you can see, this will create a problem due to the
[13:51] how this X-road node recalculates the direction and normal. So we will do point normal
[13:58] and attribute and just bit up. And as you can see, it's extruding up. And now we can come into
[14:03] the local control and pick this scale. And there we have the beginnings of our brick wall.
[14:10] So now I want to create a classic tree root. So I'm going to use this node in number 8 and name it
[14:16] less on the primitives. And this will just identify each primitive. That's an attribute that we
[14:22] use like that. Now we can do it somewhat the attribute. So attribute delete. Because every time
[14:29] we drop a new operation on you know, like poly X-road, we need to do interpolate or to transfer
[14:35] the attributes to groups and so on. So it's always a good idea to clean everything. So I'm just
[14:41] going to keep the class and I'm going to delete and select and keep these three attributes.
[14:51] Now I want to extrude these, create some thickness for these. So I'm just going to do
[14:56] and extrude let's say by individual elements and it's out. Because you can see there will all have
[15:07] the same thickness. So I want to randomize it. And for that we can just use an extruder just float.
[15:17] And I'm going to call it this scale on the primitives this time. This time and we will do add random
[15:26] can be on element number because we have single primitives as you can see and we are running these
[15:31] on primitives and we can pick a seed and also play with the values of between 0.6, 5, and 1,
[15:41] and if we come in here and apply this scale, we will have a random result. I probably want to
[15:49] output the back. So yeah. Let's see what else can we do in here. So this is basically the end of part
[15:59] one and the next part we start to create some probably the broken wall besides the bricks. So let's
[16:11] organize these and this is our base. So now we will create the broken wall and for that I'm just
[16:23] going to branch in here and when it's rough silhouette. This is a lives note. So I'm going to extract
[16:31] the Z axis. It's fine. Then I'm going to do a transform to place it in front and we're not going
[16:39] to do this randomly. Well as you can see it's more or less in the middle. So what we want to do
[16:44] and let me just get rid of this visualization. What we want to do is to move it based on the bounding
[16:53] box. So we need to read this bounding box. We could do it. We could have used the match size but
[16:58] what would we learn if we do that. So let's add a spare input and place this in here and I want to
[17:05] move this. So by the bounding box of the spare input which is minus one and I want to get the Z,
[17:13] the maximum position of Z. But that will just move it. We need to subtract the current
[17:22] max position of Z. So and the current is the input 0. So the current input. Now we should have it
[17:29] in there as you can see. So let's just a quick tip. Let's just divide this to try and
[17:38] go because this topology is a bit cursed. And the next thing we're just going to scatter. So let's
[17:45] just do a scatter. And I don't want to relax just a random scatter and I'm going to pick. You can
[17:53] pick on any points you want. I'm going to pick 30,000. So let me just go to geometry and say point
[18:01] size to four. And now I'm going to sort these points randomly. So sort and random. So they have
[18:10] a random point order. I'm going to pick a near this sorting and I'm going to create a
[18:18] to initialize a mess. Basically we will create a growth in here. So we will expand the attribute
[18:26] to create the pattern of the well of the broken wall. So I'm just going to
[18:31] in it mask. And we will do it in a solver but it will be really really fast. So nothing crazy.
[18:38] I'm just going to, since we have these points sorted randomly, we can just pick the first two,
[18:44] so zero to one. In this case, I'm going to add two seed points and I'm going to do a mask. It will
[18:50] be equal to one point. So just initialize the attribute and if we have a loop, we have one point
[18:57] in here, one point in there and we can come in here and play with the seed. And now it's here
[19:04] near. So yeah, I'm just going to keep what I had before. Sorry about that. And now I'm going to
[19:12] need a noise. No attribute to just float and it's a float noise. And not to just float. Sorry,
[19:18] attribute to just attribute, attribute noise float. Sorry. And I'm going to name it
[19:27] noise a and it will be on point and it will be positive. Let me copy my settings and let's,
[19:35] by the way, visualize it. I'm going to pick a noise pattern, alligator, amplitude of one,
[19:42] make it positive and I'm going to play with the element size, so zero point three. Then you can
[19:49] come back and play with this. I'm going to pick an offset of the thing and probably increase
[19:55] the roughness so it's a bit more dramatic, so point seven. Again, you can come and play with this
[20:04] later and I'm going to pick over. And now my idea is to take these two mask points and grow it.
[20:15] And for that, we can use some backs and this one it will be a bit more advanced, so we will use
[20:24] some geometry functions to query these attributes on the points.
[20:31] So what we're going to do is to do what we call PC Open, so in the end, and we will use a PC
[20:41] Open, so point cloud open. We will read from the first input, so this current input,
[20:47] around the position, from the current position and we need a radius, so C, radius, and we need
[20:56] Cag, max points, so how many points will we'll read? So let me just do this. We can actually do these
[21:07] in Vax. That's okay, it might space. And now we want what do we want to read? Let's just create
[21:13] this and let's say we'll go on a radius of zero point one, so this is a circle, a circle radius
[21:18] around the points and max points, we can set it to 100. And now what we will do, we will read in
[21:26] the mask, so both mask, and we can use another function called PC filter, and we can pass the
[21:32] yandl and reading the mask. And now if we do f at mask, if we assign to the mask, and we make sure
[21:41] we don't go over one with the min function, so 1.0, and we will take the current mask plus
[21:48] the mask that we sent it. Now if we come in here, we will have it growing, and it will not go over
[21:56] one, as you can see, so everything is one. But now we want to introduce that, introduce that noise
[22:02] to have, because this is just a circular growth, and we can have more points if we want.
[22:07] So I'm going to do the following mask, multiply equals beta one, and I'm going to fit this noise
[22:15] between, and I'm going to explain it a bit, so between the min mask and 1.0.
[22:24] And let's create a parameter, but as you can see, this will not grow, because we will need some
[22:30] value in here, otherwise it's just zero. So as you can see, now we should have a pattern,
[22:36] but in this case, I want to set a very small value, 0.050. Oh, sorry, we want noise A,
[22:43] noise A, let's just see. So it's getting there, as you can see, but I want to increase this
[22:53] with less dramatic effect. So the more you increase, the less noise you will add, because we will
[23:03] just be fitting a noise. So if we set this to 1, we just have the default behavior, and we start
[23:09] to introduce some noise in here. So in this case, I'm going to set it to 15, so quite a bit of noise
[23:15] in there. So that's basically our growth. I'm just going to call it grow mask, and that's our effect,
[23:26] and now we can just play it. And I'm going to time shift the frame, because we don't need this
[23:32] animation. So I'm just going to time shift the frame 120, so time shift, those stop the time
[23:39] dependency, and I'm going to pick the frame 120. Now I'm going to blast all the points that don't
[23:47] have a mask. So let me just make sure in here, 0.1, yeah, I think that's fine. So I'm just going
[23:54] to blast the points, and I'll hit non selected, at mask bigger than 0.9.
[24:03] So we get this, as you can see, this is the start of our wall.
[24:09] Now I'm going to work VDB from particles to mesh this, and by default it will be a mess,
[24:16] so we need actually, I'm just going to call this density, because we will use a volume
[24:20] up and by default it binds to density, just the naming convention. I'm going to set the
[24:26] mini radius just to 0.1, so it doesn't complain, and a point radius, this is the b scale,
[24:32] about 0.75, and we need to decrease the fossil size, otherwise we don't have enough resolution.
[24:38] Something like this. So 0.02, 0.0075, that's fine. And now we can do a reshape,
[24:48] VDB reshape, as the F, and I'm going to peak in your close, let's say 15, it will take a little bit,
[24:58] please. And now we can do a simple smooth SDF, so smooth SDF, I'm going to peak just one iteration,
[25:08] just to smooth it out, and finally we can do volume up. So volume up,
[25:17] because I want to create some more holes in the mesh on the volume in this case, and some
[25:23] details. So as you can see, this is binding to density, that's why we name the volume density.
[25:31] There are other ways you can come in here and make sure everything is binding to density,
[25:36] but I'm not coming to bother. So let's create a noise, I'm going to start with this,
[25:41] unify the noise static, because it has a bunch of options, connect the position to the position,
[25:47] and create a constant on the frequency, create a multiply constant so we can repeat the noise,
[25:54] and then a feed range, so we can control the noise, and this will all make sense in a bit,
[26:02] and then multiply constant as a global multiplier. And let's connect it, let's add this to the density,
[26:08] so we don't add no, and add it to the density. So now it disappears, so what we want to do is,
[26:15] first of all, just do a little bit, in this case I'm going to pick a value of point of 3, 6,
[26:23] so it still disappears, but I'm going to play with the range also, as you can see, this starts
[26:30] to work a bit better, and I'm going to peak in this case another noise, because the default one
[26:35] is pretty boring, so I'm going to peak in your worly cellular, I'm going to create, so let's just
[26:42] before that, let's repeat the noise about five times, and I'm going, as you can see,
[26:51] creating these holes, and I'm going to introduce some rectal, and there you go, now for this feed
[27:00] range, I'm just going to copy my value, so about point 3 to 3, so we get this, now
[27:08] this is dragging to a long lesson, let's try to speed this up, so I'm going to copy this,
[27:12] alt drag, and let's just place this one, and we will connect both at the end, and now for the
[27:20] second noise, I'm going to peak the noise, let's see, worly cellular, one, so similar, then
[27:34] a very small amplitude, so point 0.55, so just a little bit, then I'm going to feed the range,
[27:42] so about the same, and we pick the noise, but now we're going to manipulate the repetition,
[27:51] so first of all I'm going to set this to 3, and I'm going to repeat the noise along the x, y,
[27:58] and also 0.6, why, so we barely seen something, so maybe I need to increase in here,
[28:13] so point 0.55, so that's about right, let's do the following, let's do a,
[28:20] on VAR 3DB, convert VDP, and we will convert these to polygons,
[28:29] and let's do the following, let's connect this one first, and next this one, and maybe we can increase
[28:39] the effect, oh I know why, because right now, let's see, we can increase this, so point 0.55,
[28:48] and we will get this result, so maybe we can, it range a bit less, and decrease this, point 0.55, point 1,
[29:02] we start to get this result, but I want to, I want to noise up this line, so let's do turbulent noise,
[29:14] and in order to noise up the position, we need that 3D noise, and let's make it a sparse
[29:20] convolution, because it's as positive and negative values, connect this to the position,
[29:24] and just add it, so in order to manipulate, and as you can see, now we get this random noise,
[29:33] but this is too much, so let's do the following, let's create a repetition of,
[29:38] 5, and decrease the amplitude to 0.02, something like this, so let's see, 5 0.61, 3,
[29:52] let's decrease this to 0.05, and we get this sort of result, let me see if that is
[29:59] somewhere similar to my result, and yeah, this is basically it, so let's see,
[30:12] we can now just create a normal, and create a null, and this will be our wall, so
[30:22] hopefully you got something out of this, now we're just going to create another setup,
[30:28] or the bricks, basically we will extract 2 or 3 bricks from the wall,
[30:36] instead of iterating over each one, and then we will process them, like with edge damage,
[30:41] and what not, and replace these basic ones with those ones, but we will just process 2 or 3
[30:49] instead of all of it, so it should be interesting, let's do that in the next part,
[30:55] so we should still have a attributing year called class, let's have a look, and yeah,
[31:00] which identifies each brick, but now I want to extract randomly 2 or 3 to process,
[31:06] like with edge damage, and further operations if you choose, so, but I don't want to extract,
[31:12] as you can see, you can see, but I know that this starts 0, 1, 2, 3 in an order, and I want to
[31:18] extract randomly, so what we can do, and I don't think there's a default node that does this,
[31:25] so we will need to use Vex, I want to shuffle this class, so it's not ordered, so I'm just going to
[31:31] create a wrangle, and I'm going to name it shuffle class, and let's see, oops, and I'm going to run
[31:44] these on the primitives, because the class is on the primitives, and I'm going to say I
[31:49] at random index, so I'm going to just give it another attribute, and I'm going to use a function
[31:55] called random i-ash, which based on a seed, it will give us a random integer, and I'm going to
[32:01] feed the class, plus a random seed, and I can just create these, I want to say I'm going to pick 6,
[32:13] and if we have a look at that, it will be similar, so but if we have a look, we will have these
[32:22] big numbers between negative and positive, so we want to create an order for this, so for that,
[32:29] I'm just going to create another wrangle, so we can do it in the same one, and I'm going to name it
[32:34] random, random index, I'm going to color it the same, so I know they belong to the same operation,
[32:42] and I'm going to again pick primitives, and we will create an array of all the values that we have
[32:48] on that random number, so in wells, I'm going to use a function unique wells, and on the input one,
[32:57] the class is green, and the attribute is random index, so now we have an array, so a list of values,
[33:08] of all the values of these attributes, and what we can do now is to assign to the random index,
[33:16] the order, so the index, so if we do find, and we find the random index,
[33:26] this will just find its value, and this function it will output the index, so we will always have 0,
[33:34] 1, 2, 3, 4, so this is a way to manipulate the values, and now we have this order,
[33:44] so basically this function, it will output the index of this array, so we will always get from 0 to 128,
[33:52] which is the amount of bricks we have, so now we will blast to R3, so the more variations you want,
[34:02] and what I'm doing in here is to try to minimize the amount of loops we will do, so we just want to do
[34:08] three or two iterations to get in a randomization, and then we can just rotate randomly the bricks,
[34:14] and what not, so we have in a variation, so I'm just gonna blast in here,
[34:19] add random index, it will be equal from 0 to 3, since we have a random number,
[34:30] we will have these random randomization, we will have them apart from each other, and we can
[34:42] come in here and play with the seed, as you can see, and it will work out well, so now we want to
[34:50] back this, based on the index, and now we have primed and four points, let's just do a
[35:00] rangle, and I'm gonna name it move to origin, and we can just do v at v equals to 0, and we can now
[35:13] unpack, and unpack, and we will have these four bricks, so you'll pick how many you want,
[35:22] in this case I chose to be four bricks, you can pick more to have even more variation, but I think
[35:28] four of it will be just enough, now we want to do a four each named primitive, and we will use
[35:36] the random index, and I'm gonna color these, and this way we can process each brick one at a time,
[35:44] so 0, 1, 2, 3, 3, and we will focus on the first one, and we also, so we want to compile these,
[35:54] just to squeeze the most out of it, but for now, let's just do a weak edge damage, and you can
[36:00] have more effects, I'm just gonna do this edge damage really quickly, and you can pick how many
[36:05] effects you want to, to, to process, so I'm just gonna remesh, then I'm gonna do one attribute blur,
[36:14] this is very standard, so this is workflow that is been around for ages, so just one attribute blur,
[36:25] then I'm gonna attribute, remote, the class attribute, so as you can see we have a class,
[36:30] and I need it on points to have a random offset of the noise, so I'm gonna
[36:35] promote the class to point, and I'm gonna change not the original, and change it to class PT,
[36:42] and now we have a class PT as you can see, and finally we can do one mountain,
[36:46] and on this mountain, I'm just gonna do the following, I'm going to move it along the vector, but positive,
[36:57] and then simply to the 0175, that's fine, an element size of 0.05, and finally I can pick an offset,
[37:08] so 267, you can pick whichever one, but if we connect this in here, as you can see,
[37:15] the noise pattern, it will always be the same, and I don't want that, so what I can do is to use
[37:19] a vector expression, and based, based on the class PT that we just promoted, we can do the following,
[37:26] offset plus equal rent, based on the seat, we will use class PT, and we will just multiply this,
[37:38] like 20,000, and now if we have a look, we should have a different noise pattern, so again,
[37:48] before, as you can see we have the seal in here, and after, hopefully that was clear, and now we can
[37:59] just do a intersect, so bullet intersect, and we intersect in here, and let's get rid of that
[38:08] visualization, and as you can see we have the edge damage, and we can connect these in here,
[38:13] and let's see, let's just place some normal, and let's say 15, something like that, maybe not 15,
[38:24] let me see, yeah, that's okay, let's do by face area,
[38:31] say that, yeah, and now we don't want, we want this brick as a unit, so 1 by 1 by 1, so for that,
[38:40] I'm just going to do one match size, because we will use a transformer to replace these bricks,
[38:45] with replace the initial bricks, with this one, and we need to work with proper units, so I'm going to do
[38:55] scale to fit, and also not uniform scale, so we get this result, it looks a bit chunky, but it will
[39:03] be okay, and now let's just, as you can see these computes instantly, but just for fun, let's just
[39:10] go to compile block, and place this one in here, and make sure we do multi-trade it, so it's even faster,
[39:19] in case you want to process more bricks, so to be honest we could have processed all these bricks
[39:26] in an instant, but we try to optimize things and learn a few workflows, so this will be nice to
[39:33] know, so now we have four bricks to replace all of these, so we want to randomly pick one brick,
[39:40] and replace with this one, let's see how we do it, so first of all I want to promote the class
[39:48] for a maximum value, so I know how many I have, so from primitive to detail, maximum.delete,
[39:55] original, and I want to promote the class, and name it max class, let's see how that looks,
[40:02] so it's just a value of how many unique, how many unique values I have, so now I'm going to pack
[40:11] this based on the class, so pack based on the class, now I have 129 frames or points, and they are
[40:22] represented as points on the centroid, and I want to calculate a scale and a position value
[40:32] for all the bricks, and the best way to do that is to create a matrix, I know these sounds a bit
[40:38] advance, you're a beginner, but let's just do it, and you will see it's not that hard, well at least in
[40:46] this case, so how we're going to calculate the scale, so based on each brick we will iterate over each
[40:53] brick, so let's do primitive instead, and we will get the bounding box min and the bounding box max,
[41:00] in this case it's pretty easy, this is a brick, so this is a box, and we can easily get those values,
[41:09] and from there we will calculate a width, an height, and a depth, so let's actually do it, so let's
[41:15] name in class, we'll be able to buy a class, let's make sure we send it over so we transfer it,
[41:23] and now we can do vector max, it will be able to get bounding box max, but this will get it for all
[41:30] ordinary entire geometry, so we want to constrain it to the class, so plus, and we need to pass it as a
[41:38] string, so there's this function called i2way, to pass it as a string, and now we have, for each brick,
[41:46] we have bounding box max, for the x, y, and z, so it's a vector, now we will do min,
[41:53] and get bounding box min, so load, scale, x, it will be max, so load, scale, y in this case,
[42:04] it will be max.y minus min.y, so max.y minus min.y we get the i2, scale, y,
[42:15] then we have the scale x, which will be the max.x and min.x minus the min.x, and finally the scale z,
[42:24] which is the max.z minus the min.z, and finally we can create the matrix, and initialize it,
[42:35] default, so matrix, mdx, this is just the name, and we create an identity matrix, which is just
[42:43] 1 and 0, so the default, I can actually show you other clocks for mdx, it will be mdx,
[42:52] and then we can do a net, and then we remove from primitive to point the matrix, and create a net,
[43:02] and delete the points, and if we have a look at the matrix, so let's make it a marker and a
[43:07] nexus, so it will be a scale of 1, and the default orientation as you can see, so now we want to
[43:14] to have a proper scale, so for that, I'm just gonna do the following, I'm gonna scale the matrix
[43:22] by scale x, scale y, and scale z, and now if we look, it will be the size of the bricks, as you can see,
[43:34] so press h, so if we have a look, it should be the size of the bricks, now we also want to translate,
[43:42] so to get the position, so let's do well, translate matrix, and by the current position,
[43:51] which is the middle point, and we will also rotate it randomly, so we have more variation, but for now,
[44:02] let's do the following, let's create a point generate, and we will generate enough points,
[44:12] to the same amount of points we have in here, so let's just do the following, let's create this
[44:17] very input, and connect this in here, now let's just do detail, minus 1, and max class,
[44:27] this is just to read the detail attributes, called max class, and this last one is the component,
[44:33] but we want to add 1, because that's from 0, so we have 129 points at the center,
[44:40] that we will use to copy the points, so now if we do the following, so let's see,
[44:50] we have this matrix right, so if we do much, but we're not, and we go in here,
[45:01] so in here we have 129 rims, same amount of points, because it's back geometry,
[45:07] so we can do the following, we can read in the matrix, so let's do matrix, and yes, it will be
[45:15] equal to rim, input 1, we want to matrix, and paste in this case on the point number,
[45:22] and now if we do V at V, multiply equals by the matrix, we should have the points at the same position,
[45:31] and the thing is, now instead of doing this, we can save 4 by 4 transform, that the copy to points
[45:40] will read perfectly, so now we have a transform, so let's name it, it's formed, and okay,
[45:53] we can delete this resolution, no, we still need it, so now if we do a copy to points,
[46:00] but in here we just have far breaks, if I remember correctly, so what we need to do
[46:07] is to create a attribute, a variant attribute on the points, so we can feed in here to a
[46:12] piece attribute, so let's do an attribute from pieces, this is the easiest way, so we can
[46:17] populate the points, and let's do it based on the random index, let's do random, in this case,
[46:26] I chose a variable 3.3 sampling, and now we have, what this means is that on the points, now we have
[46:35] a random index based, well a random index from 0 to 4, which is the amount of breaks we have in
[46:42] here, so we are feeding everything procedurally, and now we can do a copy to pop-ups, we can do a
[46:48] copy to points, and do it based on the random index, and if we have a look, now we should have a
[46:56] brick, perfectly aligned, so if we look in here, so no edge damage, and just the edge damage,
[47:06] the thing is patterns start to emerge, because we have the same, we only have far breaks to
[47:13] randomize, and we can come in here and play with the seed as you can see, but still we don't have
[47:18] enough variation, so we can easily rotate them around, and upside down, so we have more randomization,
[47:25] so let's do that, for that I'm going to create a step or end, and this is based,
[47:36] so let's create it, this can be a bit complicated to understand, but let's try to do it,
[47:48] so basically we want to create, so let's do it first on the points, because it will be easier,
[48:00] so we will take the function, so let's do vector, underscore n, and do sample,
[48:12] it's a function to get random vectors, so sample direction uniform, and we will do random,
[48:21] i-at-p-t-n, so this will just give us, so v at underscore n, it's equal to underscore n,
[48:31] now let's visualize it, and we need to do it as marker and vector, so this will give us a random
[48:38] direction vector as you can see, but what we actually need is a step or end, so either negative,
[48:48] either to the back or the front or to the sides, and not these randomize looks, so we need to
[48:53] manipulate what we feed in here, so if we have a look, we are feeding vectors to a value, so we can
[48:59] actually manipulate it, so let's do a float, step size u equals to 0.25,
[49:11] and let's do step size v 0.5, and now we will create a value for the seed, so in seed, eaggide,
[49:23] let's create a random value for the u, but that has a step orientation, so float, u will be
[49:32] round to integer, and we will use a random function, based in this case on the point number,
[49:41] plus a random seed, and we will also receive, and we will just divide this by the step,
[49:48] step size, step size u, and also multiply it by the step size u, if that's true,
[50:03] there are no, and now let's do the same for, this is just a formula to do a step orientation,
[50:08] so 90 degrees, so float, v, step size v, and step size v, and let's do another random value,
[50:18] let's create this and play, let's speak a seed of 5, and now we can just do vector to vector to
[50:28] third, it will be a set of u and v, and now if we feed this to this argument, we should have,
[50:40] so this is based on the point number, so 0 to 5, 0 to 5, let me see, so i at ptn, that's correct,
[51:01] so there are a few brackets missing in here, so we want to close in here and multiply at the end,
[51:07] and also in here do the same, so yeah we want to remove this ones at the end, and now we should have
[51:18] a uniform direction, we will still randomize it along the way, but that's in a bit, so we can now
[51:25] move this in here, and remove this one, and do it based, and do it in this case on the primitives,
[51:33] and based on the primitives, so it's copy and copy, and if we promote this to points,
[51:46] and as you can see we should have a random direction up, down, left, right, from, back, as you can see,
[51:55] so now we want to rotate our matrix by this random direction,
[51:59] so in this case 90, always 90 degrees, so what we can do, and let's have a look,
[52:05] let's output the matrix, as you can see it's all pointing in a uniform direction, so if we come
[52:11] in here to the matrix, and we do, so we should do scale, rotate, translate, so as Rt, that's the
[52:19] transform order that we're going to operate, now we can do a rotate, and we want to rotate the
[52:25] matrix by 90 degrees, and this feeds radians, so we can either use the radians function,
[52:32] or just feed it by, which is 90 degrees, or in this case 180, and then we can feed it,
[52:41] V at underscore n, and this will rotate it, as you can see randomly,
[52:48] up and down, left to right, and from the back, now if we have a look, we should have a more randomized
[53:00] result, and we can come into the step or end and play with it, as you can see, is rotating it randomly
[53:06] on all directions, so yeah, now we can also introduce a bit more randomization, so
[53:13] mainly before, after we do the packing, so actually we'll just load, and we want to load the B dot Z,
[53:26] and in this case I want to add a random value between a min and max, so I'm just going to copy this
[53:32] one, and make it a little easier, and a maximum of 0, 0, 0, 5, I can just play with the seed,
[53:44] so as you can see it's moving randomly, you can pick, you can play a bigger value, but in this case
[53:51] I'm going to a small one, and just after the step or end, where we have that n,
[53:57] underscore n, we can do a attribute that just vector, attribute that just vector,
[54:03] and we can manipulate the n on the primitive single case, I believe yes, in different
[54:10] alternatives, and we do direction only, and we rotate randomly between min and max value,
[54:19] in this case I think I chose this five and play with the seed around the Y axis,
[54:25] so now if we have a bokeh near, we should be rotating randomly the larger root,
[54:34] and now if we feed it will feed to our matrix, and now we have a randomization,
[54:38] and we can play with the seed and maybe just treat.
[54:42] Let me see if I am missing something.
[54:45] I don't think so.
[54:46] So we can just create a map.
[54:50] And we can look at it.
[54:57] And look also at this one in here.
[55:02] And finally we can come in here and create a skylight.
[55:09] And let's eat shadows,
[55:13] or enable shadows.
[55:15] Let's move to these in here.
[55:21] Maybe a bit done.
[55:27] Yeah, something like these guys.
[55:31] Okay.
[55:34] And finally we can look and disable this.
[55:43] So yeah, guys, hopefully you picked up quite a few tips.
[55:48] We explored many, many concepts in this video.
[55:51] Let me know if you found this useful.
[55:54] And as always, you can grab the full scene on my Patreon alongside
[55:57] with exclusive tutorials like this one, for example, similar to this one,
[56:02] and other topics that I explore on Patreon.
[56:06] And you can always grab all the scene files from my videos.
[56:10] And yeah, thank you for watching.
[56:12] And let me know in the comments if you knew everything.
[56:15] Thank you. See you next time.



---

## Captured Frames

- [1:40] tutorials/frames/think-procedural-think-houdini/frame_000.jpg
- [5:00] tutorials/frames/think-procedural-think-houdini/frame_001.jpg
- [8:00] tutorials/frames/think-procedural-think-houdini/frame_002.jpg
- [12:10] tutorials/frames/think-procedural-think-houdini/frame_003.jpg
- [15:00] tutorials/frames/think-procedural-think-houdini/frame_004.jpg
- [18:20] tutorials/frames/think-procedural-think-houdini/frame_005.jpg
- [21:20] tutorials/frames/think-procedural-think-houdini/frame_006.jpg
- [24:50] tutorials/frames/think-procedural-think-houdini/frame_007.jpg
- [28:10] tutorials/frames/think-procedural-think-houdini/frame_008.jpg
- [31:40] tutorials/frames/think-procedural-think-houdini/frame_009.jpg
- [35:00] tutorials/frames/think-procedural-think-houdini/frame_010.jpg
- [39:10] tutorials/frames/think-procedural-think-houdini/frame_011.jpg
- [43:20] tutorials/frames/think-procedural-think-houdini/frame_012.jpg
- [47:30] tutorials/frames/think-procedural-think-houdini/frame_013.jpg
- [51:40] tutorials/frames/think-procedural-think-houdini/frame_014.jpg
- [55:50] tutorials/frames/think-procedural-think-houdini/frame_015.jpg

---

## Structured Notes

### Core Technique
Build a full procedural brick wall from a single 2-point line using only default nodes and Attribute Adjust Float manipulations (no custom VEX for the base wall), a simplified point-cloud-based **growth solver** (`pcopen()`/`pcfilter()`, no actual DOP simulation) to create a randomized broken-wall silhouette, and a from-scratch **matrix-based transform** system (scale/rotate/translate built manually per-brick) to swap a handful of edge-damaged high-detail bricks back into thousands of instanced positions via Pack Inject.

### Summary
The wall starts from a single Line (2 points) copied 24 times, using **Attribute Adjust Float** (a relatively obscure but powerful node) driven by the primitive's `copy_name`/`copyname` attribute (remapped 0–1 via `end-primitives-1`) to manipulate `P.y` (overall wall height profile) and `P.x` (brick-course width profile, applied only to alternating "outer" points via a Sort-by-Y-and-reverse trick to distinguish even/odd points) using custom ramps — entirely without wrangles. A second Attribute Adjust Float randomizes each line's Y position (small range, seeded) for natural unevenness. **Resample by Length** (not fixed point count, ~0.2 = brick size) turns each 2-point line into a multi-point brick-course curve; a Group Expression selects each curve's end points (`ptnum == primpoints @ prim - 1` style), and a wrangle randomizes only the *middle* points' position along the curve using `random(ptnum + prim + seed)` (zero-centered, small amplitude) combined with `vertexcurveparm()` for curve-view sampling, then re-samples position via `primuv()`-based lookup — creating irregular brick-length variation without touching the fixed endpoints. Point-to-point Y-difference (`pos2.y - pos.y`) becomes each brick's extrude scale (fed to Poly Extrude's local-control "scale" input), and after converting to Line, a point-normal-vector-based Poly Extrude (with a per-primitive random scale, seeded) raises the bricks with individually randomized heights. For the broken/missing-brick silhouette, a rough Boolean-derived silhouette shape is Scattered with ~30,000 randomly-sorted points; a **simplified growth solver** (not a DOP network — just a point wrangle with `pcopen()`/`pcfilter()`) seeds two random mask=1 points, then iteratively reads each point's neighborhood via `pcopen(0, P, radius, maxpoints)` and does `mask = min(mask + pcfilter(handle, "mask"), 1.0)` to grow the selection outward each pass; a **noise-remapped growth rate** (`fit(noise, min_mask, 1.0, ...)`) makes the growth boundary irregular instead of a perfect circle. After Time-Shifting to a fixed frame (stopping the time dependency) and Blasting all points below a mask threshold, the surviving points are meshed via **VDB from Particles** (density/mini-radius/point-radius/voxel-size tuned) → VDB Reshape (close) → Smooth SDF → Volume VOP (layered static/turbulent noise via multiple Volume Noise nodes chained, each with its own frequency/repeat/range) to punch organic holes and add surface detail → Convert VDB to Polygons — producing the broken wall's silhouette shape. For brick-level detail variation, the wall's `class` attribute (per-brick ID) is **shuffled** using `random_ihash(class + seed)` and then re-ordered into a clean sequential index via `find(unique_vals, random_index)` (an array of all unique random values, indexed to recover 0,1,2,3...) — this "shuffle-then-reindex" trick lets a handful of random classes (e.g. 4) be selected for expensive per-brick processing (edge damage, remeshing) instead of processing all ~128 bricks, wrapped in a Compile Block for speed. Each selected brick gets a quick Remesh + Attribute Blur + noise-based Mountain (offset seeded by `class` × a large multiplier so each brick's noise pattern differs) → Boolean Intersect against itself for a chipped/damaged edge look, then Match Size (non-uniform scale) to normalize to unit-brick dimensions for later per-instance scaling. To place these processed variant bricks back at all ~128 original brick positions, a **from-scratch matrix workflow** is built: per original brick (packed by class), bounding-box min/max derive `scale.x/.y/.z` values, an identity matrix is scaled by those values then translated to the brick's centroid, producing a full 4×4 transform per point (read via `primintrinsic` matrix + point generation matching the class count) that Copy-to-Points can consume directly as a `transform` attribute alongside a **`fromPieces`-attribute** (random index 0–3) selecting which of the 4 processed brick variants to stamp at each position — giving perfect per-brick scale/position without needing per-piece manual placement. Final randomization adds a **step-oriented rotation** (a Set/Rotate/Translate — "srt" — matrix order) using `sampleDirectionUniform()` fed a quantized (`round()`+division by a step-size) U/V pair so each brick randomly faces one of a few fixed cardinal-like orientations (not fully random directions) via `qrotate()`-equivalent matrix rotation by 90°/180° increments, plus a small random Z-jitter and Y-axis-only rotation jitter (via Attribute Adjust Vector, direction-only) for natural-looking variation without breaking the brick's rectangular silhouette. A Skylight with shadows finishes the render setup.

### Key Steps
1. Build the base wall profile purely with **Attribute Adjust Float** nodes (no wrangles): copy a 2-point Line 24 times, promote `copy_name` to points, remap it 0–1 (`end-primitives-1`), and drive `P.y` (overall height silhouette) and `P.x` (brick-width profile, applied only to alternating/outer points via Sort-by-Y-and-reverse) with custom ramps.
2. Add a second Attribute Adjust Float to randomize each line's Y position slightly (seeded) for natural unevenness, then **Resample by Length** (~0.2, brick-sized) each 2-point line into a multi-point brick-course curve.
3. Randomize only the curve's *middle* points (endpoints excluded via a Group Expression) along the curve using `random(ptnum + prim + seed)` (zero-centered, small amplitude) combined with `vertexcurveparm()` curve-view and a `primuv()`-based position re-sample.
4. Convert to Line, compute per-segment Y-difference (`pos2.y - pos.y`) as an extrude-scale attribute, feed to **Poly Extrude**'s local-control scale via point-normal-vector attribute, and randomize per-brick height with a seeded scale wrangle.
5. Build the broken-wall silhouette with a **simplified growth solver** (not a DOP sim): Scatter ~30,000 randomly-sorted points on a rough Boolean base shape, seed two mask=1 points, then a point wrangle iteratively grows the mask via `pcopen()`/`pcfilter()` (`mask = min(mask + pcfilter(...), 1.0)`), with a noise-remapped growth rate (`fit()`) for an irregular (not circular) growth boundary.
6. **Time Shift** to a fixed frame (stop time dependency), Blast all points below the mask threshold, then mesh the survivors with **VDB from Particles** → VDB Reshape (close) → Smooth SDF → **Volume VOP** (layered static + turbulent Volume Noise nodes for organic holes/detail) → Convert VDB to Polygons for the final broken-wall shape.
7. **Shuffle and reindex** the wall's per-brick `class` attribute: `random_ihash(class + seed)` for a shuffled value, then `find(unique_vals_array, random_index)` to recover a clean sequential index — lets a small subset (e.g. 4) of bricks be selected for expensive detail work instead of processing all ~128.
8. For each selected brick (wrapped in a **Compile Block**, multithreaded): Remesh, Attribute Blur, apply a class-seeded Mountain noise offset, Boolean Intersect against itself for chipped-edge damage, then Match Size (non-uniform) to normalize to unit-brick dimensions.
9. Build a **from-scratch per-brick transform matrix**: pack original bricks by class, derive scale values from each brick's bounding-box min/max, scale an identity matrix by those values, translate to the brick's centroid — producing a full 4×4 transform per point usable directly by Copy-to-Points.
10. Add a **`fromPieces`-style random-index attribute** (0–3) to select which of the processed brick variants gets stamped at each of the ~128 original positions via Copy-to-Points reading the manual transform attribute.
11. Add **step-oriented random rotation**: quantize a U/V pair (`round()` + step-size division) fed into `sampleDirectionUniform()` so each brick randomly picks one of a few fixed orientations (not arbitrary), apply via matrix rotation (90°/180° increments) in Scale-Rotate-Translate order, plus small Z-position jitter and Y-axis-only rotation jitter (Attribute Adjust Vector, direction-only) for natural variation.
12. Finish with a Skylight (shadows enabled) for a quick render/preview.

### Houdini Nodes / VEX / Settings
Line (2 points), Copy (24×, output copy name), Attribute Promote (copyname → point), Attribute Adjust Float (×3+: height profile, width profile via Sort+reverse, Y-position randomization), custom Ramps, Resample (by Length), Group Expression (endpoint selection via `primpoints`), point wrangle (`random()`, `vertexcurveparm()`, `primuv()`-based re-sample), Convert Line, Poly Extrude (point-normal-vector local control, per-brick random scale), Boolean (rough silhouette base), Scatter (~30,000 points, random sort), growth-solver point wrangle (`pcopen()`, `pcfilter()`, `min()`, noise-remapped `fit()` growth rate), Time Shift, Blast (mask-threshold), VDB from Particles, VDB Reshape, Smooth SDF, Volume VOP (layered static + turbulent Volume Noise), Convert VDB to Polygons, `random_ihash()` shuffle + `find()`-based reindexing, Compile Block (multithreaded per-brick detail loop), Remesh, Attribute Blur, class-seeded Mountain, Boolean Intersect (self, edge damage), Match Size (non-uniform), bounding-box-derived scale matrix construction, identity-matrix scale/translate, Point Generate, Copy to Points (manual transform + fromPieces-style random-index attribute), `sampleDirectionUniform()` with quantized U/V (step-size `round()`), matrix rotation (SRT order, 90°/180° increments), Attribute Adjust Vector (direction-only Y-axis jitter), Skylight (shadows).

### Difficulty
Advanced (combines a from-scratch simplified growth solver using point-cloud functions instead of DOPs, a shuffle-and-reindex trick for selective expensive processing, and a fully hand-built per-instance transform-matrix pipeline for swapping detailed variants back onto thousands of positions).

### Houdini Version
21.0 (visible in viewport title bar, partially "Houdini ... Commercial 21.0...").

### Tags
brick-wall, growth-solver, pcopen, matrix, pack-inject, edge-damage, procedural-modeling, sop-solver

---

## Related Tutorials
- [Ruins - Randomized Brick Wall](ruins-randomized-brick-wall.md) — alternate, Voronoi-Fracture-based approach to a similar randomized brick-wall problem from the same channel.
- [Procedural Rock Wall without intersections](procedural-rock-wall-without-intersections.md) — shares the RBD/Bullet-as-modeling-tool philosophy of building irregular wall shapes without manual sculpting.
- [Roasting my Houdini Setups #1](roasting-my-houdini-setups-1.md) — shares the "avoid unnecessary for-loops, use pcopen()/pcfilter() growth-style solvers instead" philosophy demonstrated here.
- [Scissor Lift rig in Houdini](scissor-lift-rig-in-houdini.md) — shares the from-scratch per-instance transform-matrix construction philosophy used here, applied there to propagating an IK chain's pose across repeating segments.
