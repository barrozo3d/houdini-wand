---
title: Double Sided Leaf Animation using Cops in Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=yeA_0tL3GlU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/double-sided-leaf-animation-using-cops-in-houdini-21/
frame_count: 0
frame_status: pending-selection
---

# Double Sided Leaf Animation using Cops in Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=yeA_0tL3GlU)
**Author:** cgside
**Duration:** 22m8s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py double-sided-leaf-animation-using-cops-in-houdini-21 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Project overview [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna show you how I created these two
[0:05] side animated leaf using sobs and cops combining boats and getting this final result. This is an
[0:12] interesting exercise and hopefully you'll get away with some new techniques. So let's get into it.
[0:20] So we will start in here in sobs and the first thing I do is to import in another
[0:26] copnet I imported the leaf texture and extracted an alpha with the gear and then in the trace node
[0:32] I just load it that alpha and we get this mesh. So the first thing I want to do is to swap this
[0:41] to UV space so we get to live in the 0 to 1 space. Later it will be easier to work with cops.
[0:48] I'm doing a bunch of things in here just to have a curve view and uniting the curve and starting
[0:58] the points but that's not important. The important thing in here the first I wanted to show you is


### Identifying mesh landmarks [1:02]
**Transcript (timestamped):**
[1:02] to find the landmarks on the mesh. So basically what I mean is to get this point in here. So this
[1:09] corner points and of course you could have selected by an even what not but that's not the idea in
[1:15] here. We want to create things procedurally even if that takes longer. So the way I'm doing that
[1:22] you can see by the features on this curve that if we measure the curvature we will get a bunch of
[1:29] points all over the place and we just want these corners and we just want these corners because
[1:35] the idea is to create a skeleton. Something that would look like this as you can see this is the
[1:42] final result of the skeleton that like we can bend and animate with a regrangle.
[1:47] So how can we do this? So I'm just copying with a natribute swap. I'm copying the position to
[1:53] rest attribute and then I'm blurring that rest which means that we will end up with a mesh like this.
[1:58] Here I'm just switching between rest and bit and in near that's what I'm measuring the curvature
[2:05] and as you can see near it's much easier. Unfortunately I had to branch in here because
[2:10] although we have these position attributes it doesn't look like it's working it will always work on
[2:17] B. I believe you can only switch between B and UV and not another attribute so I had to re-branch
[2:24] in here or branch in here and after we measuring the curvature as you can see it successfully
[2:29] identified those landmarks then I can copy the curvature to my original mesh because they have
[2:34] the same point count it's just attribute copy will work and then in attribute expression I'm just
[2:40] selecting the curvature above threshold so we get these points and now I thought okay cool now I can
[2:47] just group expanding and get a single point but easier said than done because some points some
[2:54] selections have a fixed amount of points and others selections have more or less points so that
[3:03] will be a problem we can do a group expression so my idea was create a class attribute for each
[3:09] selection or each isolated selection and that comes down as a view triangle so basically I'm running
[3:17] over detail so just once expanding the point group of the landmarks so this point group and I'm
[3:23] gonna iterate over each single point that are in this group so that is in this group so I'm just
[3:30] saving a previous view previous curve view and a class attribute so I have a curve view on this curve
[3:36] as you can tell and I'm just basically comparing if this curve view is similar enough to this one
[3:43] so for example in here if this point has a similar enough curve view I'm gonna keep it in the same
[3:48] class but for example between these two that there will be a difference so in this case I'm setting
[3:53] a threshold of point of one and that way I'm gonna create a new class so I'm starting class at zero
[3:58] then I can iterate or I can increase or the class and then I'm just setting the point attribute
[4:06] because we are on detail and saving the previous view for the next comparison so that's basically how
[4:12] I'm creating a different class as you can see by the colors that each selection has a different
[4:16] class then I can just get a single point in this create group where I'm basically oh again over
[4:23] detail I'm getting all the unique values of the class so in this case I'm getting from zero to
[4:30] 12 so 13 classes it's rating over them and in here I'm expanding a point group for each class
[4:40] and selecting what I trying to manipulate to be the middle point so basically getting
[4:48] from that selection of the current class I'm getting the middle point so in this case I'm
[4:53] going to select the index that's the length of this group of these points divided by two so it's
[4:59] actually a way of selecting the middle point of the class as you can see sometimes it's not very
[5:03] successful but I didn't want to create any more loops so after getting that specific point I'm just
[5:12] gonna do a near point from that position and setting the point group I believe I could have done
[5:20] it in a different way maybe I could have just set the point directly but anyways I'm doing this
[5:26] way so yeah that's basically finding the landmarks on the mesh after this let me just check I'm


### Building the leaf skeleton [5:31]
**Transcript (timestamped):**
[5:34] deleting some groups polyfilling removing the curve with this wrangle we have done this before remashing
[5:41] and we have some distorted UV so I'm just doing a UV project on the UVs UV project on the mesh I mean
[5:49] and then here is where I'm creating the base of the skeleton so something like this and basically I
[5:58] have the mesh and I'm isolating those points that we selected above and creating an ad note so
[6:06] creating this interior mesh converting to line creating a convex a convex and a concave group so
[6:16] so I can select these interior points with these wrangle in here basically two oriental
[6:21] uncurved ones with next edge one of previous edge and just doing a cross product then I'm adding the
[6:29] in this case the convex ones and converting to line and now that we have this structure we can
[6:34] just extract a centroid in here and we will have some landmarks besides these ones in here that we
[6:40] already have so after converting this to line I'm going to sweep a Boolean union and Boolean
[6:47] with the bound and isolate the the faces or the geometry we can get rid of the visualization of the
[6:53] UVs so now we have this in this in this one I'm just doing a bound rectangle and Boolean in
[7:00] this case shatter and saving this group that I can later isolate extracting the centroid and now
[7:07] we have the landmarks in the middle and from here I'm generating a few points in the middle sorting
[7:14] the by proximity to the center points creating an ID so I can connect them like this
[7:21] so that's basically this part then I'm extending this to the to the boundary points
[7:33] and basically just creating a near point just doing a near point on the outer the boundary points
[7:42] getting the position of that near point and adding a point at that position and then I'm just
[7:49] bridging from this corner points in this center points to the edge and I'm also not going to
[7:58] operate on the point zero which is the middle that's why we did this sorting in here
[8:05] so now the I'm already going over a lot of detail on this I intended only to show you these
[8:14] little tips but yeah let's keep going so I'm extending then fusing polypads selecting the middle
[8:21] points just by comparing the the current point number to the primitive points in this case we have
[8:27] a single primitive for each line and that I'm just selecting the middle one with this prime points one
[8:32] since I only have three points on each line cutting there and here is a small trick so if we
[8:40] look at this oriental on curve so basically I need a normal that goes in this case is the
[8:50] usually the out vector along the x-axis I'm saving it as underscore n and basically if I don't
[8:56] input in the in the second input as you can see the normals don't follow the correct orientation
[9:04] so if I place a second input in here it will orient it also helps if you move a little bit the lines
[9:11] so I'm using the same geometry but in this case I didn't even add to move the geometry I just
[9:17] connected to the second input and automatically it will create a proper normal attribute or
[9:23] orientation attribute so that's one trick and now I want to show you how you can do like an


### Spine construction techniques [9:26]
**Transcript (timestamped):**
[9:28] intersect without actually intersecting that was my challenge because what I want to do is to
[9:35] create and let me show you again the geometry is to create this this spying in here in the on each
[9:44] leaf and also on it in the stem so we we have these normal attributes and the idea is to when I
[9:52] stay intersect without intersecting is I could have created the just a sweep with ribbon preset
[9:59] along the boundary and shoot a ray and get the that position but I wanted to try something
[10:05] different so I'm doing this workflow which is around the near point so basically we have
[10:11] this normal as I told you and is like in the right direction to the boundary and the line that I
[10:18] want to create so I'm first setting a target position for the near point so basically if I do a
[10:25] near point at this position I will get the closest point maybe this one let's focus on this point
[10:32] in here so maybe this one and I will not get that one so I'm manipulating the position by getting
[10:38] the position attribute of the near point so I'm getting starting with the position then move it
[10:43] along the direction and multiply it via distance and you have to play with the distance in here
[10:48] because if I increase as you can see that one won't work out well and if I if it's too small this
[10:54] case too small is not bad as you can see so I can but anyways I'm gonna leave it like that
[11:00] so I'm gonna put this is the initial distance check to find where that point is in space
[11:07] so I'm doing and I'm doing that on the n-shared on the boundary on this group that we have in
[11:12] here so this on the near point is the target mesh so the target group on the mesh then I'm saving
[11:19] the distance between the current position and the position of the point that we found and
[11:25] creating a prim so I'm creating a prim for each iteration so in this case we're
[11:30] creating over points over the middle point so that's 1, 2, 3, 4, 5, 6, 6 points that we are
[11:35] iterating over and for each point I'm gonna create a prim I'm gonna start by creating a body line
[11:40] and also setting a group in here as you can see if I go over the primitives I have a primitive
[11:46] call spine I didn't found a better name so now I'm iterating in a for loop not for each just a
[11:53] for loop twice so I can create two points and two vertices for my my spine and I'm right away I
[12:02] know that I need a positive distance and a positive direction and a negative direction so I'm
[12:08] just getting I which is just 0 and 1 and make it from 0 to 1 to minus 1 to 1 with this multiply by
[12:14] 2 minus 1 so this is my sign then I'm gonna do the same again the near point on the uncharted
[12:19] on the target position which is again manipulated by the current position plus the direction
[12:24] and now I introduce the sign so it goes above and below in this case or front and back
[12:30] and then I'm multiplied by the distance that I saved which is a safe check and then I do the
[12:37] near point find the position and add a point in that position so 1 in here 1 in there and or all
[12:43] the remaining leaves and this time also and then I just need to add the vertex to complete the
[12:49] primitive and that's basically how I've done this intersecting without intersecting in here
[12:56] there's a bunch of code because I don't want to use copy and transform and I just use a numbers
[13:01] a wrangle to iterate over in this case the the amount of frames we have in the in the first input
[13:12] oops so this one in here so which is 6 and creating duplicates again doing some more for loops
[13:20] and creating a fall of for the shape so I'm not going to explain you all of these you can get
[13:28] the file on patreon and explore on your own and if you have questions you can always the mme and ask
[13:32] me there so yeah then I'm just basically I'm just duplicating this this shape around then I'm
[13:40] creating a transfer attribute from the orientation that we have so we can later re-grangle this so


### Rigging and animation [13:43]
**Transcript (timestamped):**
[13:46] after preparing the the spine or the skeleton for rigging I'm also placing a rig doctor to
[13:53] initialize the name attribute I'm doing this rig wrangle that I'm gonna come back in a bit but
[14:00] I also have a second rig wrangle for I believe it's called a curling effect basically these on the
[14:07] leaves and if I haven't done this adjust transform as you can see that will be
[14:14] these effects of not mirroring the the curling which is not ideal so in in this adjust transform I'm
[14:23] making sure I am on the correct group and then I just rotate the transform attribute by 90 degrees
[14:31] along the z axis this way I have the correct result as you can see so always if you when working
[14:38] with rigs the transform attribute is the most important thing so if you learn to manipulate it you
[14:43] can do anything you want basically so in this case I'm doing a very simple operation of just
[14:49] re-rotating and creating this curl effect but it's always nice to know how to manipulate this
[14:56] transform attribute which I'm creating in here so now let's go through I ended up not using
[15:02] this curling effect because it was messing up my mesh since I have the leaves don't really go
[15:10] through all the way so it will it would create problems as you can see there are ways around it
[15:16] by blurring a bit more the and increasing the max influence of points but I didn't want
[15:24] in the end to act is curling effect it was just an experiment but it's there if you want to play
[15:29] with it and check the file so how am I doing these animations so we have done this plenty of times
[15:36] on my tutorials doing this re-rotating and creating but creating this effect but basically if I
[15:44] disable this noise we just have in here an angle to play with so we just rotate around curve
[15:50] create enough set in case we want to control the effect and that's basically it but in this case
[15:57] I'm introducing a noise and if I apply the noise if we check we will get these randomized results
[16:06] and looks a bit more natural and the thing I wanted to share in here is that when you create a
[16:13] noise with wax or with vops which is more common you don't necessarily need V at B as a position
[16:18] attribute so in this case I'm using the point ID which is like the prime ID is just on points since
[16:24] this runs on points and it's the same thing same attribute just on points and I'm using that to
[16:32] randomize the noise based on that seed you cannot think of this as a seed attribute it's not the
[16:37] same thing but you can think of it like that and I'm also introducing tea which is time as you can
[16:43] see in here I'm just having the spare parameter as you can see in or as a parameter I'm just calling
[16:48] time in here and that way I can play with the frequency so let's run this I can increase the
[16:54] frequency to have a more turbulent result as you can see or I can play with the amplitude so it
[17:01] goes a bit more select with the amplitude let's say five as you can see it will be on the even more
[17:10] and that's basically I can also play with the offset so I have a different result so as you can
[17:16] see if I come in here this is my initial offset I can play and get this is the real seed in here
[17:21] just offsetting the noise and yeah that's basically it then I'm just bound deforming the mesh and
[17:28] get this result and this is the outlay now let's have a look why I've done the
[17:36] the double-sided effects in cops so now in cops I'm gonna show you how I'm creating these double-sided


### Double-sided leaf shader [17:42]
**Transcript (timestamped):**
[17:47] leaf shader let's say starting by importing the outlay and resturizing and moving it to the
[17:54] to the middle where cops operates between minus one and one by resturizing the position
[17:59] and then in this wrangle is where I'm creating these double-sided effects so if you increase a lot
[18:05] the resolution this might get a bit slow because this runs on a cpil but anyway so as you can see
[18:10] we have green for the front right for the front side and green for the back side and that was the
[18:16] effect I was after so I can later texture sample the front side and the back side and blame it with
[18:23] the mask as you can see so you can have a front and a back texture and texture sample so to create
[18:30] these double-sided effects we're basically doing an intersect function so we're going from the
[18:36] original position which will look something like this is just like a position map in the wrangle
[18:42] in cops so 0 0 in here and basically we're starting from the geo and we want to get these back
[18:52] and also the UVs so we're doing the intersect function on the first input which is our geometry
[19:01] and we're going from the origin which is the current position and along the direction which is
[19:06] the negative z axis and then we're saving ipos and iovw so we can use the premium v to retrieve
[19:13] the original position so this one the normal that we will also use and the UVs that we will use
[19:22] to texture sample and i'm also manipulating in here the the origin so I basically want to subtract
[19:29] a bit from the direction from the origin and play with the with an offset as you can see otherwise
[19:39] it won't work very well because it will be flat it since this flat we need to offset it a bit
[19:47] and let me get back to this back face so you can see if i don't offset i will start to lose a bit of
[19:54] the geometry in front because we start at the same position that the geometry is in and also playing
[20:00] with the max distance in case you want to manipulate that so we're reading the position the normal
[20:05] and UVs and we also creating a mask so basically if we eat primitive we create a white mask that's
[20:13] what i'm doing in here saving the original position that i'm not using anyways and saving the normal
[20:19] that i'm going to use to light the the final effect so and the back face is really simple we just
[20:27] since we have these obvious z axis on the mesh we just say if the normal lot that is bigger than
[20:35] 0.1 we set it to red so we need to reset it to red otherwise we set it to green so this was just a
[20:41] quick way to create a double sided mask and we also multiplied by our mask that we saved so we
[20:49] get the proper outline so then we just assign the UVs to the UV port that i'm creating in here
[20:57] so then we just texture sample the front the front texture and we texture sample the back texture
[21:04] we channel x-rat in here the green channel and we use it as a blend for both textures as you can see
[21:11] and we get the final effect so the front leaf the front texture and the back texture
[21:17] then we can play with this light cop and have more or less intensity to have some sort of 3D effect
[21:27] so yeah guys that's basically it's hopefully you found this useful and as always you can find
[21:33] this scene this particular scene on my patreon right away you can dissect it and explore it more
[21:38] i hope you have learned something new on my patreon you can also find exclusive tutorials where i
[21:44] go the over this rig wrangle thing on detail on past patreon tutorials i also have courses
[21:51] so i'm just plugging near my patreon which is what allows me to do these videos so let me know in
[21:57] the comments if you learned something new if you and let me know what kind of tutorials you would
[22:02] like to see next i hope you found this useful and thank you for watching see you next time



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
