---
title: Procedural Boat in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=050av2q2ihg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-boat-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural Boat in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=050av2q2ihg)
**Author:** cgside
**Duration:** 21m4s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-boat-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I'm gonna be breaking down how I did this procedural
[0:05] boat, you know the ini. So this should be a fun exercise and hopefully you will get away
[0:11] with a few tips. So let's start at the top. I'm starting this just with a line along


### Boat [0:15]
**Transcript (timestamped):**
[0:17] the z axis. Doing a re-sample with 40 points, basically you'll define the resolution of
[0:23] your base of the boat. Then deforming the shape just with a channel ramp, nothing to
[0:29] complicate it just along the position y and you'll define the shape you want. And this will be
[0:37] our initial shape and I'm computing the normals along the x axis. So the out usually this is
[0:43] called out and I'm just setting it to end. Then on this part I am doing the other parts of the
[0:51] model and for that I'm just blasting the first and the last point of this curve, this initial curve
[0:58] as you can see in here. Then re-sampling it and sweeping by setting it to ribbon and columns,
[1:07] just one in this case you can set more if you want, playing with the width and doing a scale ramp.
[1:12] So we get this fall off or this curvature as you can see. For some reason I'm doing again an
[1:20] oriental long carving here to set it along the y axis, the normals and then displacing along the
[1:26] normals and with a channel ramp and creating this sort of effect as you can see to create the
[1:32] shape of the boat. So these are the initial lines that will define the shape of the boat. I'm sorting
[1:38] the primitives by x and skinny. In this case setting it to columns if I didn't sort they will
[1:47] get all messed up. So we need to sort them by x. Then doing the skinny and we get this sort of
[1:56] shape that now we can we can now create the back part of the boat as you can see just by adding
[2:04] the from the primitive zero the point zero to the point 82 if you can see in here.
[2:14] So we're adding that back part then re-sampling and setting it to interpolating curves to create
[2:20] the boat shape as you can see. What am I doing in here? I'm sorting by the z axis
[2:28] so I can easily select one of the primitives in here. This will be for the UVs.
[2:35] So I'm promoting that to points after it and first of all before doing the UVs I'm skinny
[2:40] in the shape and if we reverse and fuse and apply the normals we will get the boat shape as you
[2:47] can see as simple as that. Then I'm doing the UVs so I have that group where I will cut the shape.
[2:54] So first of all before applying that I'm grouping the by the main edge angle to get the hard edges
[3:03] and promoting that range group to to edges and doing the UV flatten which will look something like
[3:11] this. But then I want this part to be flat because I'm gonna do an operation after it.
[3:19] So I'm creating a connectivity on the UVs and grouping that specific part which is
[3:26] class one which it will always be based on the area of that UV shell so in this case it will be
[3:34] the middle one so one and promoting that to vertices so I can do a new UV flatten and preserve
[3:41] the seams and a rectify group I feed that specific group and then we get that group rectified.
[3:50] So this is one way to to manipulate UVs so we have that basic shape. What am I doing in here?
[3:57] I'm creating a Planck's attribute which will be based on this resample that we did in
[4:04] year so resample 6 which has 10 segments as you can see so this one in here and so I'm creating
[4:13] that Planck's attribute so I can divide it into Planck as you can see let me get rid of the UVs
[4:18] and the visualization of the curve and now we can just where it explains based on that Planck's
[4:23] attribute and poly extrude it just in set it a little bit and remove the side trims so I'm just
[4:30] in setting a little bit then I can poly extrude to create the stripes and you get this sort of
[4:39] result as you can see hopefully you can see it with the recording and this will be the base of
[4:44] the boat. Then we can create a line and do a small transform to place it where we want.
[4:57] In this case I'm going to create a nearer platform then I'm re-projecting this along the X
[5:02] so I'm just re-projecting it to the boat doing a mirror and then doing the skin to create this
[5:10] particular to this particular platform and then we will close it in a bit so what we will look
[5:18] next let's see in here I'm loading these curves on the initial setup doing a group by range because
[5:27] I want to create the seat in here so doing a group by range just selecting 10 out of all the points
[5:32] and affect disconnected geometry so by connectivity so we can select on both sides and blessing those
[5:38] frames. Blasting everything else I mean then I'm loading the base model of the boat so just the
[5:43] skin shape and blasting that particular class way that we rectify as you can see then we can copy
[5:50] the UVs to the curves with a UV sample so it will look something you should have the UV in here
[5:59] for some reason I'm not seeing them so we have the UVs in here and we should oh I'm not saving
[6:09] as UV I am saving it underscore UV so it doesn't output UVs in this case so this will copy the
[6:16] UVs from the shape to the curves and then I can just offset them along that particular shape as you
[6:23] can see by setting first the UV attribute or the UV variable and offsetting along the Y by
[6:30] you define the mount and I can move them up and down as you can see and in this case I want to move
[6:36] them in opposite directions so I can just set the sign on the premium and make it between minus 1
[6:43] and 1 then the position is just the UV sample with that fitting that those UVs so that's a nice
[6:50] trick to know then I'm just skinny subdividing and doing the normals and extruding it a bit as you can
[6:58] see and this will be the seat so we have the base shape this seat and this part here in here
[7:09] let's look at this part now so I believe I in this part I'm doing the I'm closing this gap in here
[7:16] so I'm converting this initial shape we have in here this platform as I called it and I'm
[7:23] converting it to line so I'm working by the Zed I believe yeah and then blasting the primitive 0
[7:29] since sorting it I will have the primitive 0 always here so this is still procedural and we're
[7:35] blasting that primitive resampling and re-projecting to the boat as you can see I have the boat
[7:42] and if we merge it we will have this and we can just skin and fuse and we will have the close platform
[7:49] and if we look at the boat and this part in here we should have the basis of our boat


### Cabin [8:00]
**Transcript (timestamped):**
[8:00] so now we will have a look at creating this this cabin in here
[8:07] it's simple but still has some things to it some caveats so I'm starting with the box
[8:15] and matchizing it to this platform we have in here and then I'm going to to create in this case
[8:25] I'm going to do need to do some volumes to cut out the the holes for the windows and doors so
[8:32] then I will copy the windows and doors so I need to create some points from from this shape
[8:38] so for that I'm going to shrink wrap it and do like a to-dead shrink wrap to create the
[8:44] it's like extracting the silhouette along the y so I'm just upsetting a little bit and set the
[8:50] plane normal to be along y using just in case and converting to line now we will look in a bit
[8:57] what I'm doing in here but for now I'm just going to create the normals by normalizing P
[9:04] and setting the normal dot y to zero so we have this flat normal spawning out then I can do a simple
[9:10] dot product between the normals and the negative z axis so I can select only the front points
[9:15] because I don't want the doors or windows at the back so I can bless those points and I'm also
[9:20] going to do a manual selection in this case of the of the dollar point which will be here on the right
[9:28] then I'm just doing in here a transform just to offset a bit the the windows and doors to be at the top
[9:38] and in here I need to make sure I have correct normals for the insusing so I'm just you you
[9:44] of example in the normals from the box and it will give us this straight out normals pointing out
[9:50] then I'm doing a basic transform to to the door which will be based on the heights of my door that I
[10:00] have in here so based on the what we're going to do next in this case setting the p scale and setting
[10:08] the scale of the door as you can see I'm just selecting that point from that group and I'm affecting the
[10:15] y scale of just that point and setting the others to one this is scale not p scale the p scale I'm
[10:21] just multiplying by or setting point one and we will have this but we need to have uniform distribution
[10:29] because right now if I have this this this shaping here and I do a simple recent path
[10:39] and let's say I'm gonna have this amount of doors and windows and I remove this and I copy these
[10:47] two points as you can see we can't make them we first of all if we remove the corner points which
[10:54] there are ways to do it we won't have the perfect alignment as you can see they will have more gaps
[11:00] more more gaps space in the at the edges and less in the middle so we need some how to do a
[11:06] uniform distribution of these windows and doors and I'm gonna try attempts to explain you what this
[11:14] this one is doing in here so I show you as you can see we have the same amount of gaps
[11:20] and uniform distribution there might be another ways to do this but I did it with Vex
[11:27] basically we basically we set the amount of windows and doors we want we can't have much more
[11:33] which is we can only fit three for this amount of for this amount of for this size of the windows
[11:41] and we also need the window width in this case I'm setting it by the the width the size x of the
[11:49] geometry being copied multiplied by the p-scale so that's just that that's the window width
[11:56] then I'm extracting from this box as you can see we have several frames and I'm extracting the
[12:01] first and the second point using print points and extracting the first and the second points position
[12:07] as you can see in here then I'm calculating the direction so from left to right or in all the
[12:14] directions in all the faces I mean from there I also since I did the convert line these outputs
[12:21] the this computes the rest length so I can just use the length the length can be just this
[12:27] rest length then the total windows will be the number of windows time the total window size I mean
[12:34] it will be the number of windows times the window width so window width times trig then we need to
[12:41] calculate the equal gap size and for that we can just from the length of the the initial curve that
[12:48] we have that's the wall we subtract from the length the total amount of windows and divide that by
[12:54] four gaps so the number of windows plus one then we just iterate over each amount of points
[13:02] and we do the calculation basically starting with the gap multiplied by the the current iteration plus
[13:08] one so it creates instead of starting from zero it will create the first gap then we add the window width
[13:16] and multiply it by the so we need to accumulate the offset of the window width and gap width
[13:23] so we add the window width and multiply it by the iteration which will be zero at the start so
[13:28] we need to offset it by half of it so the point is in the center of the window and that's what we're
[13:34] doing in here with this one then we just create the position for the point which will be from the
[13:39] point zero so from the point zero which will be at the left and we add the direction and we
[13:46] multiply it by the the offset we calculate in here at the point and remove any frames so this is
[13:53] just creating the necessary points. It's a bit overkill I know but in the end it works and I'm
[13:59] happy with it then I'm just doing a Boolean and we get this equal distribution. You might come
[14:06] in and in one of your future projects and if you have another solution please let me know I would
[14:12] love to hear your thoughts so after the Boolean we're just blasting in here I'm going to do some
[14:22] some blanks here at the bottom some divisions so I'm just blasting the from this Boolean to be
[14:27] inside a which are the the B primitives. Getting real off this bottom by doing this split
[14:38] frame by normal and selecting Y then clipping and getting real off the top frames and I'm going to
[14:46] divide this and this division we will just be the break polygons and we're going to take the X
[14:53] and divide it by the number of divisions we want so we can just set how many we want and we copy the
[14:59] same value to the to the side Z as you can see and we will have the same amount of divisions
[15:10] then just doing a polyx rule as always doing an inset and removing the side frames doing an
[15:16] exclusion and what am I doing in here so in this case I'm creating in here a rail some sort of rail
[15:23] so I'm just in this case creating a shrink wrap converting it to line and we will have
[15:32] still this this shape that we want to get rid of so for that I'm just selecting the door point in
[15:38] here so blasting the door point doing a rep rejection on that curve and attribute copy the
[15:44] it-frame and then we can get real off the that's primitive doing a few spottipad and sweep
[15:53] with a simple shape as you can see in here and it will look something like this if we add
[15:59] everything up we have the base of our cabin let's see from this bullion I'm also group expanding
[16:11] the B inside day or shrinking the selection and getting the window so I can color them black
[16:18] and in here I'm just creating the door so this case blasting the everything but the B inside day
[16:26] calculating the area and the max area and just comparing if the if the area is equal to the max area
[16:32] so I get the door in here I'm calculating the width and the height of the elements and
[16:41] I have a door from a previous project that I'm compute from that computer that we denied I'm
[16:48] feeding in here the size so I get the perfect size then just offsetting it to the original position
[16:57] of the door and making sure I offset it a bit on the Z axis with a match size and we will have
[17:04] the cabin that's as simple as that and I'm also loading in here the boat and the also the shell
[17:12] so I can cover up in here the this inside so this is just oh this is just creating a sweep from
[17:23] the outline curves and we get something like this so let's finish this by having a look at now to


### zanging wires [17:30]
**Transcript (timestamped):**
[17:33] create the zanging wires so starting with the curves again the initial curves deleting an A
[17:41] attributes and fusing them and creating a polypad to have a unique frame as you can see then I'm
[17:46] sweeping to create these columns setting it to ribbon and columns then blasting the the inside one
[17:55] poly cutting at the center point and doing a resample for the amount of in this case the amount of
[18:05] hanging wires we want so just set the length we want grabbing the ends just to make sure we don't
[18:12] affect those and in this case I'm just offsetting the just randomizing the points that are not the
[18:21] ends so I want to keep those and this is simple enough doing a premium v and making sure that we
[18:29] feed a random position to the u of that those new uv's where we all compute then converting it to line
[18:40] and we get a different primitive for each section resampling it and just offsetting them down
[18:48] by computing the curve view doing a mirror like effect we have done this plenty of times then
[18:53] channel ramp that and creating a falloff then we're just offsetting them along the y by that u
[19:03] amount to that curve view and also doing a small random so we can have more or less offset
[19:10] doing a resample polypads and sweep so we get something like this and this is the final result of
[19:19] that part and now in here we're just going to create these wires that simple enough we're going to
[19:26] start with the lines again with the curves reversing them and carving by extracting the points so I
[19:35] just I just want to replace the wires at a specific location so I'm going to extract the back and
[19:41] the front points then making sure we enumerate just creating an index for each point we do this we do
[19:49] a blast of an initial line and we point generate four points which is the same the amount we have in
[19:56] here and we do again an enumerate and we will get to these so four points at the top and four points
[20:01] at the bottom and we just add by attributes index resample computing the normals just by normalizing
[20:10] the position so we'll get something like this then we can just offset the position along the normals
[20:20] by these these yellow ramp as you can see to create these gravity effects sweep it and in here
[20:27] I'm just sweeping the initial curve that we did in here as you can see and we get the result of result
[20:35] so yeah guys hopefully you learned something from this this was just an experiment to try a bit
[20:41] procedural modeling and let me know in the comments if you grabbed something from these as always you
[20:47] can get the files on my patreon alongside with hours of exclusive tutorials all the project files
[20:53] from my videos and I also have some exclusive exclusive courses on the patreon shop so check those
[20:59] out thank you for watching and I'll see you around



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
