---
title: Environments in Houdini  | Part 2  - Stone Bridge
source: YouTube
url: https://www.youtube.com/watch?v=kPtCgMWIBj4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/environments-in-houdini-part-2---stone-bridge/
frame_count: 0
frame_status: pending-selection
---

# Environments in Houdini  | Part 2  - Stone Bridge

**Source:** [YouTube](https://www.youtube.com/watch?v=kPtCgMWIBj4)
**Author:** cgside
**Duration:** 36m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py environments-in-houdini-part-2---stone-bridge <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in today's video we'll be modeling this bridge.
[0:04] Should be pretty simple to follow along and yeah let's get into it.
[0:12] So this is where we left off. Let's pin this geometry and create a line
[0:22] that will be the beginnings of our bridge and in this case I wanted along the x-axis
[0:29] and also center them on the origin of the world so I'm gonna paste
[0:36] relative reference divided by two and make it negative this way we can scale
[0:41] it from the center. So I'm gonna put the size of like 2.6 something like that
[0:46] and now I want to transform it back.
[0:53] I'm gonna just place a transform down
[0:58] and enter the tool and I'm gonna move it back quite a bit by about this.
[1:07] I'm gonna try to follow some values I have and I'm gonna move it up also by about
[1:15] 0.2 and also on the x by 0.15 so minus 0.15
[1:25] just something like that and now we will resemble it because we need a few more points
[1:33] and the length of let's do. Let's enable this and a length of 0.1 should be good
[1:44] and now let's deform the curve and for that we will need the curve view attribute
[1:53] and we can just say at p dot y so the position y we will add in this case a ramp
[2:03] so we can deform this and I'm gonna use a ramp in this case I can use a curve view
[2:13] and we will multiply it by a displacement amount so let's call it like that
[2:23] and we can change if we can increase this so this will display our curve
[2:29] and we can change this to heal and start to play with the interpolation but in this case I'm gonna
[2:36] do something different I'm gonna create a float ramp disk and it will be equal to the curve view attribute
[2:50] so this will do basically the same but we will replace it here and this will do exactly the same
[2:57] as you can see but now I want to mirror this ramp so for that I'm going to multiply it by two
[3:05] and subtract one and also make it absolute and subtract from one so this way we get the mirror effect
[3:15] and now we can just play with the ramp I'm gonna try to be a bit precise in here so I'm gonna
[3:24] create a show the full curve and let me see so I'm gonna change it first to this plane
[3:34] sure this is working and I'm gonna move this one to develop one to about here
[3:41] then I will have another point in here
[3:49] so you like this and we'll be tip it up and I will have another point
[3:59] but by about 2.1 and 2.1 and 5.4 so now I just have to adapt it
[4:11] so let's see and also I'm gonna change the displacement 0.8 and we can adjust this curve
[4:21] let's do it
[4:24] let's make it like this so let's say this is our initial shape
[4:34] we'll move this a bit down so something like this let me see
[4:40] this case it should be a bit more rounded
[4:52] let's say this is fine
[4:59] and now I'm gonna create an off and call it curve rich
[5:10] now we can create a box or cube this will be our in-nil's initial shape
[5:18] I'm gonna change the size to 10 by 1.1 and 0.2 so something like this will be by 0.9
[5:28] and negative 2.5 on the set
[5:33] so this should be okay now we discover we can use the lipstickon
[5:39] and extrude it in both directions its case 1.8 and now we can just volumine intersects
[5:51] this shape with this one and we get these results
[6:00] now we will divide this geometry into sections of bricks so for that I'm gonna create a line
[6:07] along the wise line and default settings are also fine because we're going to use our match size
[6:16] and match it with this shape and make sure we still fit
[6:23] and now I'm going to re-sample we introduce the amount of divisions we want in this case I'm
[6:30] gonna use maximum segments and set it to 6 and since we're going to use the
[6:39] the volumine fracture we need center points and not these segments we need actually to
[6:45] center it so there are plenty of ways of doing this but in this case I'm going to use
[6:52] a converged line because right now we have a single primitive and we can converge line
[7:00] and now we can use a bit of x just to create the center points
[7:06] it is not necessary but just as a learning experience so I'm gonna create the center position
[7:13] of the primitive so vector center will be equal to prime uv and 0 for the incoming geometry
[7:21] be for the attribute at prime um is the primitive number we want to get and 0.5 which is the center
[7:30] of the primitive now we can just remove points incoming geometry and point number and also
[7:37] remove the primitives with one and then we just set points 0 which is the incoming geometry
[7:44] and the position we saved this should give us the center points of our primitives as you can see
[7:53] and now is is quite easy we just need a volumine fracture volumine fracture and we take this geometry
[8:02] and fracture with this one and we get this sort of result as you can see if I didn't use those
[8:07] center points some of the the extremities will get smaller so that's why we extracted the centriots
[8:16] of the primitives all right now we have also an emitter boot that we can iterate through to create
[8:24] the brits and to do them line by line or section by section so I am gonna also save this attribute
[8:34] as I'm gonna call it rows so I'm going to say primitive and copy and I'm gonna copy the name
[8:44] and save it as rows so we have these attributes because we will divide again this with a volumine
[8:51] fracture and the name attribute and the name attribute will be cluttered with pieces so I'm gonna
[8:58] using step this rows to refer later to another geo operation we will do so now we can just do the
[9:08] brits so for that or the brits the stones so for that I'm gonna do a for each name primitive
[9:16] and this should have already the attribute in here and we iterate to the primitives
[9:21] and let's see we can create a line in this case along the x and the wimps size just the same
[9:34] as we did before so in this case match size the line to this geometry and we can scale to fit
[9:43] then we can re-sample but in this case we want to use the length otherwise the
[9:51] the size will be inconsistent so I found a value of 0.3 worth fine then we can do the same as in
[9:58] here so let's copy this so convert line and extracts and try let's see is that correct yes
[10:11] and we can just read the mountain on the points and my mouse is that strange
[10:18] so in this case we don't want along the normals of course we want we want a longer vector and also we
[10:27] just want along x so we just want to displace it along the x I'm gonna change this to 0.4 the amplitude
[10:39] and we can change the element size to 1.25 and now we can do work for my fracture
[10:48] and let's see what sort of result we get so as you can see we get bigger and smaller
[10:56] stones let's see that for everything and this right now is too uniform for my taste so I'm
[11:05] gonna randomize it a bit here in the offset and for that I'm gonna use the iteration attribute so
[11:12] create metting port nodes and go to the mountain create a spare input let's drag it
[11:22] and in here I'm gonna use the detail attribute iteration to randomize the offset or its row so I'm
[11:29] gonna use a round and I'm gonna call the detail attribute in this case minus one because it's
[11:36] the sparing goods and the attribute is the iteration and the component is the x is the single
[11:44] component then I'm gonna do the detail iteration so in this case I'm gonna do add a value let's say
[11:55] for 60 and multiply it by a big value so in this case I have something wrong in here because I
[12:04] don't need this in here so this is what I don't let me see so I guess this is similar enough
[12:15] you can play with this value in here and get a different seed so that I chose this one and this
[12:21] is our big setup now let's organize this a bit I mean it's quite organized and we can just use
[12:29] a compile so this works a bit faster and make sure we use multi-trade it and let's see if that works
[12:40] and it does and as you can see it's pretty fast so let's do the rest in the next part
[12:48] well now we want to do the bricks that are in this opening this rounded part so for that I'm gonna
[12:55] do an object mount and bring in the curve that will help us solve the curve bridge
[13:03] and I'm also going to re-sample because those are just a lot of points so I'm gonna use point
[13:10] 19 wire blast points I'm gonna do a sweep
[13:15] and in this case I'm gonna change it to a ribbon I believe that's what I did and it's
[13:27] going to be the size and set the columns to one so it's fine now I'm gonna save a
[13:36] attribute on the primitives so I'm gonna set it to primitives and say I add prime id it will be
[13:46] equal to prime now so each primitive will have a different a different id so we can refer back to
[13:53] it because right now I'm gonna I'm going to subdivide it so subdivide to have a more rounded look
[14:02] and in this case I'm gonna subdivide it twice and as you can see we get this rounded look but we
[14:07] still have that attribute on the primitives that we can use to offset the bit the shapes
[14:14] so let's just go back a little bit because in here I want to do something to this I want to create
[14:19] an exploded view and I'm gonna before that I'm gonna use connectivity
[14:31] point and class attribute will be fine and in the x-plotus view I'm gonna change this to point
[14:36] and set it to class and the x-plotus view I just want to create some spacing between the
[14:41] stones and that change is to point or tree and as you can see along the y is not evenly spaced
[14:48] so I'm gonna set it to one point seats on scale to have a more evenly distribution of spacing of space
[14:56] so now we will continue in here after the subdivide I'm gonna do a vertex split to split the
[15:08] primitives with that particular attribute so not I'm gonna use instead prime id
[15:13] and all the extrude
[15:20] in this case we can inset and remove the in this case the side primitives so to create the spacing
[15:29] and I'm gonna change it just so it'll be point a little five that is fine then we can just
[15:36] extrude and also I'm gonna match size this
[15:48] so let's move this down and I'm gonna match size to this geometry and in this case
[15:57] let's see I want to remove the justify x and y because I want it in that position but changes
[16:03] that to mean and also I'm going to move it a bit back by negative point or two
[16:16] do I have it like that yeah so now let's see now we want to extrude it of course after the inset
[16:27] and in this case I'm gonna extrude it by about 5.3 so this is fine and I'm gonna put the back
[16:41] and from here we can just merge it
[16:45] and then we'll do visualization of the h root so this is our progress so far
[16:58] now I want to remove since I have this spacing I want to remove this inner geometry that we have
[17:04] from the wall so for that I'm gonna do a simple singing here which is from
[17:15] from this vertex plate I'm gonna extract the silhouette so I just gonna
[17:21] silhouette from the labs notes and this will be along the z and I'm going to poly extrude it
[17:35] by the same amount plus abnormal
[17:42] and also pull the intersect oh in this case it's not intersecting it's subtracting sorry so we
[17:55] just subtracting that and I also want to beat it on the bit so I'm gonna beat it by about
[18:04] going to 0.5 just do a little bit more to the shape we can play with the gnomos but that's fine
[18:15] so what else can we do in here now we will need to iterate over this geometry and create some edge
[18:26] damage okay now we will create some damage on the on the corners of these bricks or these stones
[18:36] so for that I'm gonna create connectivity and I believe I did on the frames
[18:42] and I'm gonna override the name attribute so I'm gonna change the frame and call the name
[18:48] I'm gonna just override it so we can easily iterate through them without changing the attribute
[18:54] so for each name primitive and we can connect this and we have 200 pieces
[19:02] let's iterate one by one this should be pretty fast because we want to
[19:08] bigger changes to our geometry we will do just chip operations so this will be a very
[19:15] cheap edge damage so first of all I'm gonna rematch this by about point of weight that will be
[19:23] enough and then I'm gonna blur the geometry so attribute blur the position by one is fine
[19:34] and then I'm gonna create the mountain and this will be too much which is one
[19:41] of a little bit so point 05 and change the element size to point of 3 and I also have
[19:52] ample enough sets 17 something like this and now we can do a volume intersect
[20:00] this time is a volume intersect and in this case is a bit too much so
[20:12] am I doing point of 5 point of 5 and oh of course I need to do positive and not zero centred
[20:20] so let's just remove the visualization and let's run to all the pieces and this is
[20:27] fine enough let's see we get an issue in here on this piece so we could probably change the offset
[20:38] and it will take us 12 different results now we can just compile this
[20:49] and make sure we multi-trade it and let's see and that is working fine so this is our geometry now
[20:59] as I told you it will be really cheap operation and now we can start to build our bridge a little
[21:07] bit more so I'm gonna mirror this to the other side not that we will really see it but
[21:15] and I'm gonna change the distance to point 3 to 3 point 3 point 2 negative 3 point 2
[21:24] and along the z of course so this will be the distance and what else will we do
[21:34] uh I want to as you can see we still have we should have the rows attributes so let's see that
[21:43] and make sure we visualize it as a color so random from attributes and as you can see we still
[21:51] have these rows I want to remove randomly some of those top rows top some of the stop stones
[21:59] which in this case we have the attribute for so it should be pretty simple
[22:05] so in this case I'm gonna create a connectivity after we're some connectivity
[22:11] on the point because we will need to remove some of the stones so let's see that connectivity we
[22:19] have the classic roots and first of all let's see I'm gonna create an attribute rainbow
[22:34] and I want it just on the rows piece 8 so if we do remove point 0 as we do now and remove the
[22:47] primitives we should have that row deleted hope we need to set these to primitives yes
[22:54] so as you can see we have that row in there I know it's the piece 8 because it's the last
[22:59] and that's fine but we don't want to do this so we want to pre-read first a seed in seed
[23:06] it will be channeling to jerk seed so we can change the result and then we can do if we will
[23:15] just remove randomly some pieces so random I add class based on the classic root plus seed
[23:24] and let's say if that is smaller than a threshold that we will establish so threshold
[23:32] we will remove the point so remove point in common geometry point number and remove also the primitives
[23:46] and now we can set the thresholds so we can just remove some and change the seed and as you can see
[23:53] it will not have the the mirror effect on the back so it's randomized based on each brick
[24:01] ID so as you can see which will help us with some of the perspective we get from the camera
[24:09] so as you can see it's not the same all the way back so in this case I use the threshold of point
[24:16] 3 6 and a seed of 4 which in this case produces a bad result so I'm going to change this
[24:27] and remove some more change the seed
[24:32] I don't want to remove too many so a better approach might be to
[24:44] to create a noise and remove based on that but I'm gonna keep it like that so
[24:52] and now we can also do some random rotations or for the top stones
[25:02] I'm not sure if I'm gonna do it because it's quite a bit it's more a bit more advanced but yeah
[25:09] let's do it just as a learning experience so if
[25:13] rent so we will do the same I at class let's see it and I'm gonna change this
[25:22] we will I will introduce a new value and just have a fixed threshold in this case of 0.3
[25:32] and we will select randomly some of the top pieces because this is running on the p-sate
[25:38] and we will randomly rotate them by about let's say 25 degrees so the first thing we need is a
[25:45] variable called angle and it will be radians 25 degrees and we will multiply it by random
[25:57] of the class and we will use the seed and add up value a random value
[26:04] and we can put this between the parentheses
[26:13] in this case and we can just multiply it by 2.0 and remove 1 so we have both positive and negative
[26:21] values and so we can go from minus 25 to 25 in this case this is just a quick way to fit the values
[26:32] then we need a quaternion you can use matrices but I'm gonna use quaternions because I'm
[26:36] more familiar so quaternion and we want to rotate this angle we we establish and we want to
[26:45] rotate it along the y axis in this case so 0.1.0 now we also if we do let's do that let's create the
[26:56] let's actually rotate the pieces using the q rotate function and we will rotate the quaternion
[27:04] and back the position so as you can see they will rotate but they need to rotate from their
[27:11] center from their center right so for that to work we actually need to do an exercise so I'm
[27:18] gonna say bounding box center it will be equal to get points bounding box and if we do
[27:28] just that without a point group we will get the center of all the primitives of all the
[27:34] the stones on that's a rope so we need actually to give it the individual class attribute
[27:41] so I'm gonna use a point group in here and for it at class it will be equal to i2Way i at class
[27:56] what am I doing along in here at class equally so this should be working
[28:04] no i2Way i what is there so unexpected
[28:19] this should be working
[28:23] screen oh sorry we want to get point bounding box center that is fine and now we can just
[28:34] move it to the center to the center of the wall so v at b minus it goes to bounding box center
[28:42] and now there will be in the center of the wall and now we just need to edit back so let's just copy this
[28:52] and in this case we will edit back as you can see some of them will be rotated randomly
[29:00] and we can change the seed
[29:07] and we can change the seed also in here so a lot of work and it won't make that much of a difference
[29:15] but you know we just try to show off and let's maybe change the seedle it will be it's
[29:24] and that will be fine what else will we do so we can just create them
[29:31] no in here let's organize this a bit
[29:40] but now we can start to merge this in this case we will need to do a geometry for the center
[29:50] and also a pet and we will be good to go so what will we do in here we will create an object margin
[30:02] here and we will merge let's see
[30:10] on the bottom of my fracture so right here we will create a mouth
[30:20] and we will merge this in
[30:26] so this is our our initial geometry and from here we can just scale it
[30:33] so I will just match size and move it this case to
[30:41] let's organize this a bit and let's create a match size and move it to this mirror node
[30:50] and that is fine
[30:54] I'm just going to clip it a little bit on the Y because otherwise it will be on the way
[30:59] off the pet so this case we want primitives below the plane
[31:04] and about 1.2 and let's fill the polygons
[31:13] and I'm also going to create a transfer
[31:18] and make sure we are scaling from the center so in this case I'm just using the central
[31:22] idx, dy and dz on the viva translate and I'm going to scale it by a value of 6 on the z
[31:30] and just for visualization I'm going to place another one here
[31:35] and let's move this in here and create a merge so select both alpha drag and merge and shift R
[31:43] so this is fine and I will just need to create the pet which should be simple enough
[31:51] it will be just something really really simple
[31:55] I'm going to create a let's see from
[32:01] here I'm going to create a box
[32:05] and set this to 9 by 0.15 and 1.2
[32:13] and now I'm going to match size this
[32:15] so let's see what we have in here so the initial geometry and we will do mean to max
[32:28] and change this to max also
[32:32] and we need here so we want it in the middle so to create the route and I also want to move it down
[32:40] to something along those lines well I'm with this along this top row
[32:46] so this will be fine and then we can just create a scatter this will be really really simple
[32:53] so I'm going to use a scatter change the point amount to 500 and I'm not even going to
[33:00] oh we want some relaxing relax situations so we can do a one on a fracture
[33:06] so this is the points and this is the geometry and we have something like this
[33:13] so we will have smaller and bigger parts and that's totally fine and now we can just do an
[33:21] exploded view so explode the view
[33:28] and it will be in this case I didn't do an exploded view because I'm going to use a remesh
[33:35] and that already will give some space between them and a value of 5 worked well and I'm just doing
[33:44] the remesh on everything at once which runs smoothly on this simple geometry and then I'm going
[33:50] to do a smooth work better than the edge root blur and I'm going to smooth it by 3
[33:58] and also increase the field equality to so it doesn't get that smooth
[34:02] we can do maybe a sub-anormous let's see all that works for us
[34:09] and that's maybe yeah that can work I just want this rounded look on the stones
[34:17] and finally I believe this should align properly so let's connect this to here
[34:25] and move this and let's see
[34:28] and I guess it's aligning properly
[34:35] let's see how that looks over our terrain so let's create another merge in here
[34:42] let's select this and this and drive and I guess that looks fine over our terrain
[34:52] so yeah guys it's a lot of work but in the end I leave it up to you to tell me if you enjoyed
[35:00] this one please let me know in the comments I plan to continue this so in the next part
[35:06] we should be able to do let's see we should be able to do the presentation let's see if this
[35:14] loads if it's too slow so in the next part we will do this I added some vines in here I'm not
[35:21] sure if I'm gonna keep them but let's see I'm gonna do this vines setup and also create this tree
[35:28] we have in here right now I only have one tree but maybe we will create some other ones
[35:34] but before the trees maybe we will do the rocks I also have a set up in here for the rocks
[35:40] it's pretty simple but should give us a good enough result so let's see let me know if you guys
[35:47] are interested in continuing this project and please make sure to follow me at least on Patreon
[35:55] and check out my courses in there and also my exclusive tutorials and you will be able to find
[36:01] these project files and all the others from my videos on there too thank you and I'll see you next time



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
