---
title: Procedural and Organic Modeling in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=8hUjc7BEI9g
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-and-organic-modeling-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural and Organic Modeling in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=8hUjc7BEI9g)
**Author:** cgside
**Duration:** 27m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-and-organic-modeling-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video we will be creating this
[0:05] Etern Apple from start to finish step by step and although this is a very simple
[0:13] network as you can see there will be always a chance you can learn thing or
[0:19] to. So yeah let's get started! So as always we start with the geometry container
[0:27] let's drop a sphere and we will make it polygon and a frequency of 30. Now we
[0:39] want to create a mask for the top and bottom part. So for that let's use a point
[0:47] of up and we will use the relative bounding box and the y-components of vector
[1:00] of float and let's check the y-components and as you can see is going from the
[1:12] bottom to the top from 0 to 1 and we want to subtract constants we want to mirror
[1:21] this effect so let's subtract 0.5 and now we can absolute those values so we get
[1:32] something like this. Now we want to extend the range so let's go with a frequency
[1:43] range and say in the source mean to 0.33 something like this. Now we want to
[1:55] distort a bit this shape so for that we will use a turbulence noise connect
[2:04] position and we will make it as parse convolution and a 3D noise since we're going to be
[2:14] dealing with vectors and in this case I want a frequency of 6 and I'm going to offset
[2:31] it and the amplitude will be really small so 0.11 something like this we might increase
[2:41] turbulence but let's about it. So now we'll clip those polygons around the mask so
[2:56] for that I'm going to create a rest position. Create a random oops and I'm going to say
[3:10] vhp.y is equal to hcd.r so something like this now we can clip and we'll say
[3:27] our primitives and create another rest and this time extract so we create the attributes
[3:39] and check so we've clicked. Let's see where this is failing so we have that b dot y so this
[4:08] should be working so clip I might need to adjust so I'm going to create first the groups
[4:17] and say point of four I'm going to offset it all it'll be it and now it's creating a line.
[4:28] So I created the group so I can split the polygons now so let's say above plain and create
[4:38] two nodes so we have both geometries for this one I just want to set the bytes so when
[4:52] I feed it to the vdb it will be small enough so about two and for this one I'm going to group
[5:09] the unshared edges so I'm share the edges and on work line to convert those two curves so
[5:24] I'm shared and remove unused points and connect pets so we have a single primitive per curve
[5:34] now I'm going to re-sample about points and group the points so let's say points and
[5:59] I'm shared and create boundary groups so we have two groups one for each curve and now we can
[6:08] group the nodes and we will promote group zero and group one to edges and now we can poly breach
[6:22] and we will breach the group zero to group one so something like this
[6:37] and we want to increase the subdivisions so to about 60 and also play with the thickness ramp
[6:53] let's just play some reverse in here and go to the breach and under the thickness ramp so we'll
[7:09] create a point and let's go with this plane and move it down and create two points in here
[7:21] maybe maybe move this up a bit and these extremes so something like this
[7:39] as you can see it's all jacked up but we don't need to worry about that let's just make sure it's
[7:48] using at the same so let's just use and point all over one so you can see it's using some points
[8:08] and now let's get rid of the curves I have a back snippet for that so where is that? Remove curves
[8:21] just check for the priming tree is it closed and if it's open it will remove the the
[8:29] frames which are the curves so now we can create an attribute blur and we will blur it quite a bit
[8:45] so let's say about 500 and we want to do it in the edge line so we can keep the shape
[8:54] and now we will create a group for the unshared points and also a mask so these
[9:09] distance along geometry let's select the unshared and go for the mask let's see how that looks
[9:24] so something like this everyone is indeed to parameter in invert the mask and move for like one
[9:37] so something like this and now let's also create an attribute and we'll call it inside
[9:49] so we can target those that area after and let's say one so it's similar to the mask but it
[10:01] encompass all the geometry so I believe that's all now we can use smudge
[10:15] and let's remove let's see how that looks something like this and now we will create a VDVs
[10:26] so we will change it to density and let's say point all
[10:43] all weight for now we will increase it in a bit and since we want different densities for the masks
[10:54] we will duplicate this one and remove and let's get the inside and put the inside
[11:11] and get the mask and the VDV in notch I'm just trying to optimize and in this case we want also to
[11:28] fill the interior and increase the exterior band to point one so quite a bit
[11:42] and now let's just side those masks so I'm gonna say expose oops unshared primitives
[11:56] to why it's everything else when now let's create a volume box and if you check we have the
[12:05] inside and we have the mask now let's create a volume box and we will create also
[12:17] turbulence noise so turbulent noise let's connect the position and add it to the density
[12:30] it won't look like much because we need to multiply it with the mask so bind mask
[12:48] so something like this and we will change the type of noise to sparse convolution noise
[13:08] and repeat it to something like this and also offset it and change the amplitude to point all six
[13:27] and we can even reduce the roughness and the turbulence so let's just check here maybe we want to decrease
[13:43] so let's actually set the final resolution 0.03 and point all let's see I used the lower one but just speed up
[14:06] now I'm getting these weird results let me I know I need to fill the interior
[14:20] and let's use this and increase the point one
[14:27] yeah something like this now in this middle part I want to stretch a bit the noise so for that I'm
[14:45] going to duplicate this noise and change the frequency to five and now I need to copy this set up
[14:59] from above so let's go in here and copy these relative bounding books until here
[15:19] let's paste it we can remove these ads because we want that noise we just want to mess
[15:29] let me find some space and we'll take the vectors of track point five the absolute
[15:44] and use a mix to mix between these noise which will look like this so kind of stretch but I don't
[16:03] like what it does here on the on the top and bottom part so I'm going to mix it so mix this one
[16:17] with this one
[16:21] and the final result will be multiplied with a mask
[16:27] and as the mixing factor I'm going to use this one but adjust the feed range so I'm going to see
[16:43] point two and you can say zero and let's check the result
[16:55] so as you can see we have the other noise in here but it's stretching over here
[17:01] so I guess this is done and now let's move to create a smooth SDF
[17:20] and we will do just one iteration on the mean curvature flow
[17:32] and we will get probably a warning because we have different VDBs so let's go with density
[17:44] and let's convert polygons
[17:55] and we still get a pretty sharp transition
[18:02] and then we could increase
[18:07] it's already pretty good so let's keep going now let's do a natural vote from volume
[18:20] and let's then read the inside and inside
[18:26] so we have the mask as you can see and now let's create this indentation on the on the top let's
[18:40] keep the bottom like that so let's do a rematch and I'm going to rematch it
[18:55] about point 0 weight
[18:57] and I'm going to also use a lattice to deform the shape so let's create a lattice
[19:11] this will go in here the resposition let's create a habit
[19:19] and place it in here and change these two points
[19:27] and it will load for a bit
[19:40] and we need to change some things in here let's first do some edits so I'm going to create
[19:49] select these two and go over to points and unlock the selection I'm going to pick
[19:58] the middle point let's use this one and press t for the move tool
[20:06] increase the soft radius and maybe not so much
[20:14] something like this you know I'm going to pick these points
[20:25] and move them up so maybe reduce the radius
[20:30] let's move them up so something like this let's check the lattice
[20:41] create an all and it's not changing much because we need to change
[20:49] the settings in here and also the radius which is too much now
[21:00] so let's change it to point 1
[21:11] we got something maybe we need to move those points down a bit
[21:20] now as you can see it's pretty fast
[21:31] we got something we can do the same on the bottom but I'm going to leave it up to you
[21:40] and now it's pretty simple we just need to create a group
[21:50] first of all let's create an attribute layer and do we turn the inside
[22:03] let's say five let's see how that looks and create a color
[22:10] let's speak a red color
[22:21] and create another one and yellowish star
[22:27] so I can like this and create
[22:35] add it into the inside so
[22:40] and go for points
[22:44] say point 5 point 6
[22:49] so there we have the colors and we can target that same attribute for materials
[22:59] and now let's come in here and select maybe this is not so in the middle but okay
[23:08] let's forget about that now is not even properly set
[23:19] and I'm having trouble selecting the middle point
[23:28] something like this let's create a line along the z axis
[23:37] along the y can keep along the y copy the points
[23:43] and the target point will be group 2
[23:52] and this will copy along the z axis so we can just set it with just the vector
[24:01] and place it in here to reset the normals
[24:05] and we will also
[24:14] decrease the length to point 15 and say 20 points I'm just trying to create the stem
[24:24] just quickly
[24:25] and let's press enter press b and bend it
[24:33] keep pressing b now it's bending
[24:38] let's bend it this direction
[24:46] so
[24:46] so I actually want to bend it to the top
[24:56] so something like this
[25:01] and maybe let's see
[25:07] yeah this is correct
[25:09] so now I can attribute the lathe
[25:13] the lathe call the attributes
[25:16] create a sweep
[25:18] sweep
[25:20] round 2
[25:24] let's check this control click
[25:29] now I'm going to decrease these
[25:32] create a grid and create some divisions apply scale
[25:45] and let's go repeat it spline maybe increase these
[25:55] and decrease the roundness
[25:57] and now we still much
[26:03] which is need to increase this one
[26:07] so something like this
[26:11] let's create some coloring here
[26:16] and finally select routes
[26:20] and marches
[26:22] so yeah guys that was it hopefully you learned a new trick or two
[26:33] and make sure to check out my patreon where you can find exclusive courses, exclusive tutorials
[26:41] and all the project files from my videos including this one
[26:46] so if you feel like supporting me over there it will be nice
[26:51] and anyways I hope you have enjoyed this one and I'll see you in the next one bye



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
