---
title: Modeling Assets With Vellum
source: YouTube
url: https://www.youtube.com/watch?v=d2Qgcbzup2s
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/modeling-assets-with-vellum/
frame_count: 0
frame_status: pending-selection
---

# Modeling Assets With Vellum

**Source:** [YouTube](https://www.youtube.com/watch?v=d2Qgcbzup2s)
**Author:** cgside
**Duration:** 17m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py modeling-assets-with-vellum <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'm gonna show you how I created all these assets using value in Odin
[0:09] So let's start by looking at these earphones
[0:14] Which is really simple
[0:18] So I'm starting by drawing
[0:22] three curves with the draw curve
[0:25] Just draw one two and three curves for the earphones
[0:30] Then I'm resembling it
[0:35] And fusing the points with a high snap distance
[0:41] but still they are
[0:44] Three primitives and they will separate in valon when we simulate
[0:49] So let's resample again and set to subdivision curves and now we can group
[0:58] those connecting points
[1:01] Just by selecting the ends and the starts of each
[1:08] each curve
[1:11] And this is our initial setup then with a valon hair
[1:16] We can increase the edge length scale
[1:20] So it has enough separation between the wires
[1:25] That way when we sweep it later when we create geometry it will have enough space to
[1:34] To create a believable believable shape
[1:38] Then we are stitching the points those points that we saved
[1:44] So the wires don't disconnect
[1:49] Then if we run the simulation
[1:53] As you can see they are converging to the center
[1:59] And that's because I'm using a pop attract with
[2:04] I4 scale
[2:07] And that creates the effect we're after
[2:11] So then just placing a time shift on the desired frame in this case 200
[2:17] And we get something like this and you see even that
[2:22] That
[2:23] Aslan scale was a bit too big
[2:28] But I'm gonna leave it like that
[2:31] Then just cleaning the attributes and
[2:35] And orienting
[2:37] Creating the tangent normals with the oriental on curve
[2:42] So we have normals along our curve
[2:46] That way when we copy
[2:49] the other shapes the earphones and
[2:53] the jack it will be in the correct place
[2:57] Then I'm just resampling it to subdivision curves
[3:01] Creating a connectivity
[3:06] So we have each curve with a class
[3:12] And then I can use that class to separate
[3:18] the
[3:20] Where the headphone jack will be
[3:23] And where the earphones will be placed
[3:31] Then
[3:36] Then in here I'm creating a p-scale
[3:42] I want the main wire to have a bigger scale so I'm selecting the primitive zero
[3:50] And giving it a p-scale of 1 and
[3:53] The other ones which is the default value will be 0.8
[3:58] Then I'm just sweeping
[4:01] And we will have a
[4:03] bigger wire and then to smaller ones
[4:08] Then I'm just grouping it
[4:11] And in here I'm copying two points to earphones
[4:18] To earpieces or earphones and in here I'm
[4:23] I'm connecting copying two points the
[4:28] headphone jack and we'll end up with something like this
[4:34] And in the copy to points I'm just
[4:38] selecting the target points in this case that we selected in here
[4:44] Otherwise we'll be copied all over the place and the same for this part of the graph and the earphones
[4:53] We have something like this
[4:56] And the earphone piece is really simple to do
[5:02] I'm creating a line bending it
[5:07] And then sweeping it with
[5:10] Apply scale a long curve as you can see I have this sort of shape in here can show you
[5:19] And I'm subdividing
[5:21] creating a connectivity and
[5:24] lasting
[5:26] So I'm subdividing
[5:29] creating a connectivity based on the end caps and
[5:33] Blasting the bottom one then filling it since I don't want it rounded
[5:40] Then also in the sweep note I extracted the
[5:46] The end caps as you can see in here
[5:49] And then I'm
[5:51] Group expanding it so I can have that typical part in here
[5:57] Pebbling the bottom and coloring the end caps and I'm also creating a natural good to use in salaries and karma
[6:08] And caps
[6:11] And grouping it
[6:14] For the connector
[6:17] It's really simple
[6:21] Just a line with a few points
[6:25] And
[6:27] grouping
[6:28] Every other point within a range
[6:32] So every other point within a range
[6:36] And I'm sweeping with apply a long apply scale a long curve again
[6:42] Promoting the initial group to edges
[6:46] Beveling it saving the edge fillet polys group and then extruding it to create those details and beveling also
[6:59] And I'm doing the same in here nothing new and
[7:04] then
[7:07] Just creating the edge root to use in salaries the fillets
[7:15] So that's basically how I did the
[7:21] The earphones
[7:25] Now let's have a look how to create this sort of crumbled paper or in this case tissues
[7:33] As you can see I have three of them
[7:37] Each one being a little bit different
[7:43] So this is actual pretty simple to create a planar patch I
[7:49] Have this amount of subdivisions and size three by three
[7:55] Then I'm creating a valum cloth
[7:58] You can see the settings in here
[8:01] Only thing I changed was reduce the stiffness of the band and
[8:09] Let's say for example we see the first one
[8:16] So this is how it's simulating
[8:26] It's
[8:29] Crumbling to the to the to the position I defined
[8:36] And it will end up being more in the center
[8:41] So if we time shifted
[8:44] We get something like this
[8:47] And the way I'm doing that is by using a pop attract again with a
[8:54] Scale a smaller scale and with the goal set to another
[9:00] Position in this case one in X and one in Z. That's why it's moving towards that direction and
[9:08] then a pop force with
[9:11] Amplitude of one to add a bit of noise to the whole simulation
[9:15] then just doing a post process
[9:18] In creating some thickness and we have something like this
[9:26] Then for the other ones is the same but in this case I
[9:32] have
[9:34] a different position for the pop attract and
[9:39] probably a smaller force
[9:43] Let's see if this calculates
[9:48] And there you go. So
[9:55] Position set to zero and force field to one and
[9:59] I am amplitude to create this
[10:04] This more distorted look
[10:07] So let's have a look
[10:14] So the frame is 68
[10:18] So you can see how it's simulating how that pop access force pop force is
[10:28] creating these noise on the simulation
[10:33] So about there
[10:37] 268
[10:39] We get something like this if I move the reverse normals
[10:44] You can see it's creating an interesting shape
[10:48] But I'm rendering too much so
[10:53] Let's have a look at the next setup but in ear and just
[11:02] Placing the geometry in the center and then blasting each one
[11:08] Or isolating each one so I can load them in salaries
[11:12] So
[11:16] For the tissues back I'm starting with this geometry
[11:21] Like you can see in here it's really simple to create just a box
[11:27] and then doing a bullion in your set to shutter
[11:32] Extracking this shape and then recreating this part in here
[11:37] And also doing the UVs that's what I'm doing in here
[11:41] Then for the valum I'm creating a valum plots
[11:47] Set the wrestling scale to 1.5
[11:51] And then I'm stitching
[11:55] So valum constraint set to stitch points
[12:00] This part in here so it doesn't break since they are separated meshes and I want them like that
[12:08] Then I'm creating a valum solver and
[12:15] For the collision before that for the collisions
[12:19] I have this shape in here and then I'm picking
[12:25] To create
[12:28] To create the collision geometry
[12:31] And
[12:35] And that's the geometry I'm using in there so valum plot
[12:43] Valum stitch and then in the solver I have the ground plane in here and also the inner geometry for collisions
[12:54] And then I'm just solving in the first two three frames
[13:02] As you can see in here, this is the final shape
[13:07] It's just three frames
[13:09] And one thing I wanted it was to keep this orientation or something close to it
[13:17] so for that
[13:19] I am using a pop-winds to
[13:23] To have some four sagging in here
[13:27] So as you can see I'm using a pop-wind
[13:31] It's set to 1.5 on the Z axis if I remove that force
[13:37] You can see that this will fall over which I don't want
[13:44] So I'm enabling that and then freezing at frame tree
[13:50] So that's basically it
[13:55] So for the candy wrap it's not that complicated
[14:01] I'm creating a planar patch
[14:04] Then I'm bending the geometry and I'm creating a few groups
[14:13] So in this group expression I am creating two groups where the geometry meet when I bend it so I can stitch it
[14:23] And I'm also creating two groups for where the
[14:28] It creates the twisting effects of the wrap
[14:34] So as
[14:37] Collision geometry I
[14:39] Have the candy
[14:41] Which is a really simple
[14:45] Modeling task
[14:47] Then I have two tubes that are rotating in opposite directions as you can see
[14:55] And
[14:58] And that these three objects we elect as colliders
[15:04] So I connect them to the colliders then create the valent clothes
[15:09] Really fault-selled settings almost
[15:14] Then I'm stitching those those
[15:17] those
[15:19] Top points as we saved before
[15:23] So lefty and righty
[15:26] And I'm attaching
[15:32] This tube to those points we created though that that point were created and doing the same in this side
[15:41] And then just solve it
[15:45] I don't think I have nothing in here. No, I played with the rest plan because was not working properly and
[15:52] Then just simulate and let it cook for a while
[15:58] And as you can see it will start to twist along with our collision geometry
[16:05] Again, I'm not sure if this is the best approach to create this
[16:10] the start of object
[16:13] But he gave me a good enough result and
[16:17] I'm just adding some blur and subdivisions
[16:21] Cleaning the attributes and giving giving it an aim to use in salaries
[16:31] So then I am assembling everything in salaries and creating the
[16:36] layout of the objects and the materials and everything but since this video is already too long
[16:43] I'm gonna leave that for another time and meanwhile you can download the full scene on Patreon and have a look how I
[16:53] set up
[16:55] the salaries part
[16:57] And now I created the older materials
[17:00] So that's all for now. Thank you for watching and I hope to see you next time. Thank you



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
