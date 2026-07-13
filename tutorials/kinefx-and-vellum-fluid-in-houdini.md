---
title: Kinefx and Vellum Fluid in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=6wqRXRV7oxk
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/kinefx-and-vellum-fluid-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Kinefx and Vellum Fluid in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=6wqRXRV7oxk)
**Author:** cgside
**Duration:** 19m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py kinefx-and-vellum-fluid-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So ever since I saw this simulation here in Reddit,
[0:07] I wanted to create my own version in Odinni and this was done by Max Vujje, I don't know
[0:18] how to pronounce it, sorry. And you can check out his own version on his Patreon, so just
[0:26] giving credit, I did it on a slightly different way and I want to walk you through how I have done it.
[0:38] So here in Odinni I can show you my final result, as you can see it's not as great as Max version,
[0:46] but I did my best and still don't want to spend much time on it.
[0:53] So let's get started breaking down, I did everything in Odinni including this modeling,
[0:59] which is really simple and I'm gonna walk you through the network. So I'm just starting
[1:08] by creating a circle and rounded square with the simple shapes around it. And I'm merging them both
[1:21] and doing a poly bridge. From there I'm placing it in the center and grouping this bottom
[1:31] bottom points and promoting it to an edge group to do the Yovis as you can see. This is how the Yovis
[1:39] look, which can be used later on texturing if I ever texture this. Then I am polyfilling it
[1:48] and beveling the the R-deges, also doing the Yovis on those parts and creating a Yovila out.
[1:59] Let me just add the normal, so this is our base model. Let me just add the camera
[2:08] or I can do other objects. Then I'm selecting the patch group that was created by this polyfiel
[2:20] and I am group expanding it so I can create some more stiffness on the valum seam.
[2:29] As you can see I'm creating the bend stiffness. I am giving it a value of 10 on those frames
[2:40] and a value of 1 on the rest. 10, let me just say that. Then I'm creating two valum seams.
[2:51] So one that is I just let the object drop and it's like the initial state of the tube.
[3:03] So on the floor and slightly is not completely full as you can see and I have another one which
[3:13] is the tube empty and I just play honestly with the bend stiffness and that's basically it as you
[3:24] can see by the values. Then I'm just attributing just keeping the Yovis to clean off the attributes.
[3:38] Then I'm going to create the rig. We will use kin effects. So for that I'm creating a line
[3:47] along the Z axis and match sizing it to the tube and re-sampling it creating the
[3:57] carview attribute as you can see and then I'm transferring to the tube.
[4:09] From here first of all I have the two states that I told you and I am blending between them using
[4:18] some procedural animation. So fitting the frame between 1 and 48 from 0 to 1 I'm blending the two
[4:28] shapes. Since they have the same amount of topology I can just use a lurp and getting the position
[4:36] the position from the second inputs which is this geometry and just using a lurp to blend them
[4:46] as you can see. So from here I have the line that will be used as our rig.
[5:02] Let me just disable these points. Then I'm creating an aperture boot along these axes.
[5:10] Doing a slightly a slight transform, a slight scale because I was getting some issues with the rigging.
[5:20] So you can ignore that but it's there. Doing a rig doctor to initialize the rig and then doing
[5:32] a capture by proximity as you can see and it will look something like this.
[5:42] And from here I have a lot of points but I want to have a more straight look as you can see.
[5:52] I don't want this fully rounded. I want more this straight look and I should have done
[6:00] different sizes for each part but I didn't so that's how it goes. So in order to create this
[6:11] low-pollilup let's say or this straight look I am creating a group by range and selecting
[6:19] some points in an interval and then in the rig wrangle which I add the help of swalch.
[6:30] I'm creating first the spiral then doing an offset so I can scrub so I can unroll the spiral
[6:40] and I'm also using this ramp so I can have more control where it's position which is just a
[6:52] multiplier of the angle which is the spiral itself and then I'm animating it with a feed function
[7:04] from completely unrolled to almost fully rolled.
[7:13] Then I'm using a bond deform as you can see from the capture by proximity and using as the second
[7:22] input the rest position and then the animated one and this is how it looks so it shouldn't be too
[7:31] slow but I'm recording. From here so we have this and from here we're doing an attribute blur
[7:44] to smooth out a bit the shape because I was getting some intersection. Basically this capture by
[7:50] proximity is really fast but it's not the best rigging algorithm let's say or the best capturing
[8:00] system is just the fastest one and it worked well in this case.
[8:09] Then I'm caching so this is how it looks.
[8:17] Deleting some attributes just keeping the normals and UVs and also deleting most of the
[8:25] groups just keeping the patch one and from here I have the two animations and let's see
[8:36] in here actually it's pretty simple I'm just creating a valum seam to have some displacement to
[8:42] use later in rendering so nothing fancy in here and let's move on to also I have here the top part
[8:57] the modeling part of this top piece and this nothing fancy just started from the patch group
[9:08] and did an extrusion and created a spiral and position it in here so that's just a static mesh
[9:16] that we need to deform to follow the tube animation so in here I'm loading the tube and doing a time shift
[9:27] and in here I'm orienting it to the tube as you can see and the way I'm doing that is by grouping
[9:43] that top part of the tube the patch and then converting it to points and creating a reference point
[9:56] group so as you can see I have here in here basically by calculating the group point
[10:03] pounding box center of those primitives I have previously selected and from there I can just
[10:12] create a near point from that position and set the point group so that's how I'm selecting that
[10:23] point adding the normals which is really important in this case point normals so I can have the normal
[10:30] of that specific point that you can see in here from there I have the shape that is positioned in the center
[10:44] and I can move it there and the way I'm doing that is again the same logic as I have done in
[10:54] two videos already we have a selection of these unshared points and we grab the center the
[11:05] bounding box center of that selection with getting get point bounding box center then we create the
[11:11] normals for it so it will be on the minus z then we have that specific point in here that I talked
[11:23] about and we grab the normals then you create the rotation matrix we diagonal so from the
[11:33] from this base position which is in here to the target one which is that reference point
[11:44] and then we grab the position and we do the transforms again I told you before logic by swolch
[11:53] and in here I'm doing the point the form so basically taking the
[12:06] the tube animation and the rest state of the first frame and transforming it as you can see
[12:16] but I had the slight problem in here so basically when I did the first point the form
[12:26] I was getting this stretch look so I did one with a naturoput blur but as you can see it also
[12:37] transforms the outer part so in the end I mixed both with the mask that I created in here I believe
[12:48] so mask and I just mixed both results as you can see in here
[12:58] then doing a naturoput blur let me just get rid of this visualization and this is our top part
[13:06] and is animated and we just merge it with everything else and this is the final result
[13:17] so from here we go into the valum simulation to create the valum fluid
[13:24] basically we start with this frame that we have here that I saved as a
[13:30] a prime group so I am deleting everything but that group those polygons then deleting all the
[13:40] small frames with a measure and a blast and creating the normals that we will be using for the
[13:50] the for the velocity from here we can do a small peak and extrusion and deleting the attributes
[14:05] and then do a time blend to create some sub frames or some floating how it's called fractional frames
[14:17] so we don't get stepping in our simulation at least is what I have noticed
[14:27] so in here I'm just creating some tubes to select from the valum fluid so I can give it a different
[14:38] color since I'm not going to do the UVs and in the valum fluid is simple you just put
[14:45] you just give it a really high viscosity we can introduce some surface tension and then you can
[14:54] change the particle size as you like in this case I used a relatively small value
[15:03] in here I'm creating just the color lines and transferring the normals as you can see
[15:11] and they look like this and they are animated as you can see
[15:22] or the geometry is animated then I'm creating a point velocity from the normals
[15:29] so we find our normed trails
[15:33] oops
[15:40] I've done something in here so if I turn on the trails as you can see
[15:51] is pointing in that direction and then I create a netribe to adjust factor to increase the
[16:02] the velocity a long time as you can see is changing the length
[16:11] and then I am introducing some randomization based on a sine wave
[16:19] so we get the liquid going left and right randomly
[16:25] so this is basically a sine wave implementation with amplitudes and frequency I can just change
[16:37] how much frequency I want and the amplitude to so this is our initial setup for the fluid
[16:48] then in here I am getting the collision shape of the top parts which is also animated
[16:58] and doing the volume solver in here I'm just increasing the sub steps and everything
[17:04] and the ground position which will be colliding with and everything is by default
[17:12] so if we check the final result we get this
[17:20] and we also have an ancient reboot and some lines that we can use in shading
[17:32] you tend to not being the greatest mask because I don't have enough points to have a smooth transition
[17:50] as you can see by the meshing I try to do some blurring and sharpening and it gets better but it's
[17:59] still a bit well you will have to increase the resolution of the sim and by the way this sim took
[18:09] on a potato computer like mine about 10 minutes so it's not that complicated and about 50
[18:18] megabytes of cache so really that is as simple as of course I'm doing the meshing so nothing
[18:30] fancy just passing the age and the color lines as a attribute and decreasing a bit the particle
[18:39] separation in comparison to the particle size in the valent fluids so always a good idea as you can
[18:52] see this is a bit messed up but then again so yeah that's basically the end of our network
[19:03] if I can show you again the final result and remove that ugly lines and see how it looks
[19:18] so as always you can grab the file on my patreon and you can also grab my procedural courses
[19:26] and many other perks there and I hope you enjoyed this one and again if you really want to
[19:34] create this for real I encourage you to check max patreon and support him thank you and I'll see you
[19:44] next time



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
