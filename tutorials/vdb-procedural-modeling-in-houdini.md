---
title: VDB Procedural Modeling in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=ag7I-FK4TF0
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vdb-procedural-modeling-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# VDB Procedural Modeling in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=ag7I-FK4TF0)
**Author:** cgside
**Duration:** 39m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vdb-procedural-modeling-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video we'll be creating these ribs model
[0:06] mostly by using volume noises and procedural modeling techniques. So yeah let's
[0:13] get started. So as always let's start with a geometry container and we will drop down
[0:21] a line along the Z axis and we will place it in the center so let's copy the
[0:30] length and paste on the Z divided by 2 and make it negative. So we scale from the
[0:39] center. I will add seven points and we'll save, we'll place an all in here
[0:49] because I will use it later. So now we want to do sweep this and for that we
[0:57] need a profile so let's create a lot of simple shapes and it will be a quad and on
[1:08] the xy plane and let's not make it equal size and copy the top to the base so we
[1:17] can scale it accordingly and on the item I'm gonna say point on 9 and on the top
[1:25] point 3. Oops and on the top point 313 was the value I found was working great. So
[1:41] now let's sweep it and we will use this cross section and I believe we need to
[1:52] round it yes we need to round it so let's go with round corners and point
[2:00] 0,2 and 4 divisions something like this and now when we sweep it and now let's
[2:13] add a normal and we will also subdivide it twice and we will create some
[2:32] deformation. Actually in here we need to create the end caps and I'm gonna change
[2:45] the scale to point 3 and 3 divisions is fine. So we have this now we need to create
[3:01] a mountain to deform a bit the shape first so let's create a mountain and it will be
[3:10] really low amplitude point of 3 and we want it zero centred and the element size of
[3:19] point to 7. I'm just copying some values but feel free to use your own. So let me see
[3:30] yeah this looks similar now we might get some intersections in here so let's place let's
[3:42] blur the normal so point normal and attribute blur on the end we've done these several times
[3:51] and it does help a little bit on corners so yeah let's get right into the volume
[4:02] displacement but before that let's just place another subdivide to make everything a bit
[4:08] smoother and let's move to the volume displacement. Okay now be living from
[4:20] polygons create an STF out of this model and the final resolution will be smaller but for now
[4:29] let's go with point 0.05 and we need to smooth it a little bit so BDB smooth STF and I believe the
[4:43] fault iterations are fine and let's move to the volume drop so volume drop
[4:58] and also on where BDB to polygons so we can preview our result
[5:06] so I'm just going to create some initial displacement so we've done A A noise and the
[5:20] A A noise connect the position to the position and we can create a constant in here and then multiply
[5:31] constant this is the usual setup I do because if we increase this multiply by constant we can
[5:42] increase the repetition of the noise let's place also a feed range so we can control our values
[5:50] and also another multiply constant to have an overall control then we can also place a switch
[6:02] to turn on enough the noises so output 0 connect these two here and just place an add
[6:13] and I like to color them yellow and let me see we need to actually do some things in here so that
[6:26] changes the density and let's use world space and I believe I need to increase it so actually increase it
[6:38] what feel interior and increase it's quite a bit the exterior band so now it's working because we
[6:47] were not binding the density and as I said this is meant to be just an overall noise
[6:57] so first of all I'm going to increase the multiply constant the repetition of the noise
[7:03] and on the noise itself I'm going to decrease the roughness to 0.35
[7:16] and on the feed I'm just going to expand it so minus 0.15
[7:25] and decrease quite a bit this one so 0.1
[7:37] so it's just an overall noise as you can see just to break a bit the shape
[7:45] and let's move to the second one so let's create an AI static noise
[7:53] so it's not an AI unified noise I mean and let's connect these to the position
[8:02] and create a constant in here oops so create constants
[8:10] and multiply constants
[8:13] and we will also need these three in here so we can copy
[8:24] and let's add it in here let's just make sure we antique this one
[8:33] as we don't don't want to preview that noise
[8:39] so we need to do quite a few things first of all I'm going to increase the repetition of the noise
[8:46] the weight and I'm going to also change the noise type to worldly cellular f1
[8:56] so we get this sort of shape I have enough set of 80 so I'm going to replicate it but feel free to use your own values
[9:09] and I also have I'm going also to increase it in this case to expand it by 0.3
[9:20] and a multiply constant will be smaller 0.075 so something like this now we want to distort this noise
[9:30] because right now is looking to to procedural or to computer generated so for that I'm going to use
[9:40] a turbulence noise and connect the position and edit and since we want to distort in positive
[9:55] and negative we will use it we'll use sparse convolution and treat the noise
[10:02] and let me see we need to change the amplitude it's to i right now so 0.27
[10:13] and I'm going to also change here the
[10:26] the repetition so the frequency to 0.21x so we have this direction now
[10:33] noise and also I'm going to transform the position to be like in a diagonal way
[10:50] so for that I'm going to use a transform matrix how is it called transform matrix yes
[10:59] I'm going to place it here and rotate it 45 degrees so
[11:09] let me just check on the turbulence noise I'm going to offset this
[11:16] so I'm going to use some values from before as I was telling you so this one looks a bit better
[11:30] it's more likely what I want to do and I believe we only have one noise left to do so let's
[11:41] actually duplicate this setup and you can drag this to do the shelf and keep adding them
[11:53] without having to rebuild them every time or you can use a receipt now in Odini 20.5
[12:04] so I'm going to actually remove this x form and let's see what else we will need to change
[12:15] we'll increase repetition in here the frequency to 0.6 and increase this and now we want to
[12:26] just to create some overall deformation some finer detail I mean so I'm going to offset this just to
[12:36] be different and maybe change the amplitude and this will be our distortion let me just share
[12:53] okay so now we will use a different noise we'll sell the ref to f1 and we will complement it
[13:07] and now we need to play with the feet so in the feet we will say minus 1 and small value
[13:18] on the destination max so we create something like this now we also need to
[13:28] decrease this quite a bit so point 0 to so we have something like this
[13:36] let me just shake
[13:45] and of course we need to add some fractal in this case we will do standard
[13:53] and 1.56 was working fine for me and I believe that so let's enable all the noises so
[14:06] disable enable so this is our low resolution preview now let's increase to the final resolution
[14:21] and see how that goes so 0.0015
[14:27] so this is the result we got I believe it's pretty similar to what I have in my final file
[14:40] and this took about 30 seconds to cook so depending on your machine mine is really bad so
[14:49] you'll probably get away with a faster result so now we can leave this part in here but usually
[14:59] it's cut right it's more straight so I'm gonna use some boxes to
[15:07] element to make this planner on the sides so buried me we'll create a box
[15:18] and let's preview this and create a box and this is where we need to move it
[15:31] and let's resize this maybe increasing here so something like this
[15:48] three four
[15:50] so
[15:53] it's similar to what I have so let's do a mirror
[15:58] and mirror on the x and we need to add some subdivisions of 20
[16:08] so we can display it a bit so we're the mountain
[16:12] and the values I have were about 0.03 and 0.4 and 0.7 so something like this will be fine
[16:31] and now let's subdivide and we will subdivide twice do I pass some other inputs so twice
[16:42] and let's see is this okay I guess so so now let's create a VDB from polysons
[17:00] and this will have a resolution of 0.01 which will be fine totally fine
[17:08] and let's do a VDB combine and this will be a bit slow when we do the subtraction or difference
[17:24] so more 20 seconds more now and I believe we need to move it a bit more in
[17:35] so let's see let's check this and move this a bit more in
[17:53] so in this case I add a value of 0.31
[17:57] so something like this and let's test that
[18:12] so let's look at the final result and yet this is more like it and we will add some noise on the
[18:22] sides so don't worry about that and now we will do exactly that so let's create a volume
[18:36] block another one and we will also create another VDB from polygons in here
[18:47] from this boxes so we can mask the sides and let's do a fog VDB since we want to mask
[18:55] collect mask and we can use this and connect this to the second input
[19:04] so we will copy the detailing from this one so let's copy this last nice
[19:20] and paste it in here
[19:21] and let's set it
[19:34] and let's smooth this
[19:41] this is what it is
[19:47] a while so we better decrease this for now so we can concentrate on the effect and we'll
[19:58] increase it at the end so this is much faster and now we need to mask that we only want on the sides
[20:10] so we connected the mask to the second input now we can do a volume sample
[20:18] and connect the second input in here and the sample position
[20:24] and we will do a primitive name and mask and now we can simply multiply it so in here
[20:40] let's create a multiply
[20:42] and multiply this with a feed range we'll need a feed range in here and multiply it in here
[20:57] so as you can see it's not doing much because we need to play with the values so let's go with
[21:03] the source mask of point form and this Tio has some flat areas so what we can do is to place
[21:13] a transform and scale it a bit so transform
[21:23] and we can oops and we can scale it a bit so let's see the result now and now is affecting all
[21:39] the sides so as you can see and maybe we want to play with the texture on the sides so
[21:53] let me see what else did I change in here
[21:56] so let's change the amplitude in here to 0.25 and increase the frequency so we have a bit more distortion
[22:15] and the sparse convolution tree denies and let's see this one is fine I maybe want to play with the offset
[22:32] and the rest is fine I believe we see the feed multiply and yeah that's all so now we just need to
[22:53] increase the resolution so how much was it 0.0015 and 0.0015
[23:11] and let's look at the final result so lots of detailing but maybe we want
[23:19] and I'm noticing a seam in here so maybe we want to let's change this point 0.03
[23:38] sorry it was 0.03 almost crashed my ordini so maybe in the transform in here we can increase
[23:53] this to 0.9 so we don't have that visible seam in there
[23:59] you didn't happen in my initial file so I'm not sure what I've done in different in here
[24:13] so I don't know what we can do so maybe reduce in here
[24:24] so 0.25
[24:30] yeah that helps quite a bit so that's fine let's increase it again to 0.015
[24:41] and we will look at final result 0.0015
[24:47] so let's look at this now it's more clean and we don't have that sort of issues
[25:00] so let's cache this so file cache and let's name it ribs noise demo
[25:17] let's take to this let me just check
[25:22] so it was looking pretty similar to my final result on the other file so it's fine now we'll create
[25:39] the bones so now for the bones let's object merge that initial curve so let me actually have
[25:51] some more space in here and we will merge this curve in here and let's see now we will transform it a bit
[26:09] so translate it by point of weight and scale it 0.85 and we still have those points
[26:21] now we can create the bones so for that I'm gonna place a circle and we will do this
[26:32] in a loop to have some variation but for now I'm gonna just place some initial values
[26:39] so divisions we can set this to 5 for now
[26:49] and create a bevel
[26:57] and it will be on the points
[27:00] and let's say distance of 1 and divisions 3 and now let's create a random b scale so let's
[27:14] just load b scale and we want random between point of weight and 1 and let's say
[27:30] this is it and now let's scale that by attributes so we get this random scaling
[27:42] and let's extrude this so extrude
[27:48] and we'll go with distance up 3 and 7 divisions
[28:04] let's splice that's primitive 0 so we have in here so splice primitive 0 and now mirror
[28:15] so on the z let's all refuel it in this case what relateral breed let's untake the form patch
[28:32] and what else can we do we can extrude this a bit in so probably extrude I mean we can
[28:46] insert it so I'm gonna insert it by point 13 and it will be the patch group that we didn't save
[28:58] so patch group now let's extrude them in again in this case the output front
[29:16] and I'm gonna extrude it just a bit of it so now we can create a bend
[29:29] let's press enter and b increase the angle and keep pressing b until we find so this is it
[29:43] and let me check
[29:47] is this it I guess so so now we will create a can and a bevel so let's do the same setup from here
[30:04] so we can copy these nodes into a poly bevel and we will bevel the r-degis
[30:17] so let's extrude and the distance of point of two and scale it by attribute and tree divisions
[30:31] just what's on details we will mostly do it with textures but I will be creating that tutorial
[30:43] in another video so let's go with 17 and I'm just setting this up initially but in the end we will
[30:58] we will create a system with a for loop subdivide
[31:05] and finally do my match size and we want to align it on this set I believe
[31:19] so in this add I'm gonna set it to mean
[31:24] something like this and uv unwrap in this case let's skip the uv's for now since
[31:40] we we will create the textures later so now we can copy the points
[31:54] and of course we need to change a few things so first of all let's set an initial normal so
[32:11] attribute to just factor and we will set the normal along the x so like this
[32:23] another attribute to just factor but on the up and we will set it to the y axis and yet another one
[32:36] and on the n and now let's see our normals now we want not the n and now what we want to do
[32:52] is to create just we want to randomize the orientation so let's set it to direction only
[32:59] and rotate and from attribute and we want to rotate around that vector and set it to random
[33:07] so as you can see it's creating this effect so let's maybe change this copy and paste
[33:19] and do it negative and I'm gonna use a value of 13 and change the c to 44
[33:29] let me just shake so yeah now we'll just create a point shitter so we'll get another layer of
[33:43] randomization 0 0 on this axis and 1 and the scale really small point to weight
[33:53] and a seat I'm gonna use the same value but you can play around and antique update
[34:01] normal otherwise it won't work and let's just set it to just float for the p scale
[34:09] and we will do a random value between point of tree and point of five
[34:18] this will be enough and we can just change the seats
[34:26] let's see how that goes so it's copying to the right direction but now we need to do this in a loop
[34:35] so we have some random bending and all the other attributes
[34:43] so let's create a forage point
[34:52] copy this in here and the first thing we're going to do is to change
[35:02] the sides of the circle so first of all let's create the metting port so create metting port
[35:10] and like metting hoops and we will connect it to the circle so add sparing put
[35:20] and connect it in here let's copy this time
[35:28] so now we will need a seat so let's see add it to the interface let's say the
[35:41] needteger and call it seat seat and a value between 0 and 100
[35:51] so now we can on the divisions we can do a fit so one and the random on the detail
[36:05] minus 1 which is the sparing put and we want the iteration and 0 and we want to add the seats
[36:19] so base relative references and between tree and five let's see how that goes so
[36:32] we have 4, 4, 5 and in here we have 3 so and let's change the seat also so as you can see it's
[36:43] changing randomly the the amount of divisions another thing we need to do is on the pins
[36:55] so again let's add the parameter interface add the parameter interface create an integer seat
[37:12] so it's fine let's also add sparing put and it will be our metting
[37:27] and let's copy the same values in here so where are we so let's copy this
[37:37] because we will do a similar thing to 1 and we will do between minus 30 and 35 so something like
[37:51] this as you can see we have these randomness let me check if my file looks like that
[37:59] otherwise I might be doing something wrong and it does so it's fine
[38:08] so now that I'm seeing this this and beyond rap maybe we can place it elsewhere so actually
[38:18] let's leave it here and now since we're doing a copy to points it's always a good idea to
[38:24] compile it so I believe it won't complain which is always a problem with compilips
[38:35] let's multitredit and it's working fine
[38:43] let me check my movies because this looks indeed strange
[38:55] yeah let's keep it like that for now we can fix that later
[39:03] so I guess that's about it let's merge this with our meet so let's copy this
[39:18] and merge it
[39:28] and this is our final result
[39:34] so this is the working progress I have for the next part on the texturing and shading
[39:40] so stay tuned for that and other than that just check out my patreon if you want to support my
[39:47] work and download all the project files including this one on there and I'll see you next time thank you



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
