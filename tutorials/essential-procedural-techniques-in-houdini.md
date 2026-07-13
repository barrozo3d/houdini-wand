---
title: Essential Procedural Techniques in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=JMfMxHi48Zs
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/essential-procedural-techniques-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Essential Procedural Techniques in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=JMfMxHi48Zs)
**Author:** cgside
**Duration:** 11m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py essential-procedural-techniques-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back, so in this video I'll be sharing a few interesting tips
[0:04] on procedural setups.
[0:06] So let's start with this sort of peeling effect.
[0:10] So this is pretty simple.
[0:12] We start with a quadsphere.
[0:14] I kind of transformed it and used the amount to deform it to like a potato shape.
[0:19] This is similar to a video I saw of the same effect in Blender.
[0:24] Then I'm subdividing just to have an geometry for the next step and in here I just place
[0:28] a spiral and align it with a centroid to have something like this and I reproject it
[0:32] to the potato.
[0:34] Then I make sure since we have normals in here that are coming from the potato, I'm
[0:39] just swapping it to one petribut so I can sweep it with those same normals.
[0:44] Otherwise if we don't have that petribut it will be a mess as you can see.
[0:49] Then we come back to this branch where we have the subdivided, we do a distance from
[0:52] geometry, from those curves and we have a mess that looks something like this.
[0:56] Then we clip it but this won't give us the correct result as you can see.
[1:01] But we will use this to align our UVs next.
[1:03] So we clip it based on the mask attributes and then we promote that clip touches group
[1:08] that I saved in here to a vertex group.
[1:11] And finally we do a Boolean and this Boolean is actually what will create the peel.
[1:17] Then we do a UV flatten and the UVs will look something like this because we are using
[1:21] that vertex group in here that we saved to flatten the UVs along the X.
[1:27] So along the UVs if I don't do that we get something like this which won't work for
[1:32] our next effect which is basically, first of all I'm going to split the UVs and then
[1:36] promote it to a point attribute so I can work in a point wrangle with UVs.
[1:40] And in here I'm taking the new component of the UVs.
[1:44] So this component around the X axis.
[1:48] And I'm just creating an animated mask.
[1:51] So we have a ramp based on the curve view plus some offset so we can offset it up and
[1:57] down and then just assigning that to an attribute.
[1:59] So I can show you how it looks.
[2:01] So it basically it will grow.
[2:03] It's a mask that will grow.
[2:06] And I'm just animating the offset.
[2:08] So if I let me copy this because I'm doing a bad job at explaining it.
[2:12] Basically let's say we start from minus one and we can animate it to a fully one as you
[2:16] can see along the UVs X component.
[2:20] So that's what I'm doing in here.
[2:21] I'm fitting time between zero and one second and start at minus one and go to one between
[2:27] those those frames and we get this effect.
[2:30] And then it's simple we can just affect the position dot Y.
[2:33] We subtract that mask and we play with the amplitude.
[2:36] So we get this effect.
[2:38] So yeah that was the first tip.
[2:42] So in this one I was trying to replicate those typical videos of liquids with a bottle
[2:46] spinning and creating this sort of splash effects.
[2:49] And I did that with mpm and I wanted to show you how you can use open CL which is the
[2:55] recommended methods to apply forces into the dive targets of mpm.
[3:00] So let's actually have a look at that.
[3:03] So in here as you can see I simulated the I simulated the liquid in a rest space as you
[3:10] can see.
[3:11] It's not with the bottle spinning all around but I applied the transform that I have from
[3:17] my animation because I did my animation with a transform as you can see in here with
[3:21] a transform attribute.
[3:22] So you can see in here let me show you.
[3:24] So it's basically an animated noise and playing with the rotation creating a transform
[3:28] attribute and then applying the transform attribute.
[3:30] You can have a look at the file on Patreon.
[3:32] I'm going to share all the scenes from this video.
[3:34] So yeah.
[3:35] So I'm I'm transferring the transform along the the shine of nodes.
[3:40] So for example in here I'm just copying to the detail attribute and inside the mpm
[3:45] solver.
[3:46] So as you can see this is the final result of the mpm solver and let me dive inside and
[3:52] actually pin this viewport.
[3:54] What I'm doing in here is first of all we need to bring that animated attribute to because
[3:59] it's an animated x form to to dops.
[4:02] So for that I'm just reading the matrix from the first input first contact geometry and
[4:07] saving that as an attribute.
[4:09] So otherwise it will just read the first frame like normal dops.
[4:13] So we need actually to bring it because you can do it in OpenCL.
[4:16] And since Odini always says that we should use OpenCL to in the dive target instead of
[4:23] X I try to replicate the same effect I add on Vex but using OpenCL and it's actually
[4:28] pretty simple.
[4:29] So the idea is to that I add in Vex before is just to apply gravity using the X form and
[4:37] you can do that pretty simple in OpenCL.
[4:40] You bind the first the force attributes because you can create attributes with OpenCL.
[4:45] Then you also bind the detail attribute for the X form.
[4:47] You create a parameter for the gravity that you control in here.
[4:51] And then in the kernel you just save a variable Open matrix for for the X form and you do
[4:56] a met for three back three malt which is multiplying the gravity but ignoring the just
[5:01] reading it as a three by three matrix.
[5:03] So ignores it ignores translation.
[5:06] And then we just set the force to do this variable and that will apply our transformatribute
[5:12] in rest space that we can later.
[5:14] So let me see is not in here later I am applying the X form.
[5:20] So it's in here.
[5:21] In here I'm just applying the X form from the back geometry and we get the sort of result
[5:27] that you saw in the final render.
[5:29] So yeah hopefully that will be useful on how to use actually OpenCL to apply your effects
[5:34] and this is a very simple effect but you can see how useful this can be.
[5:43] So still on the same scene after I have my geometry meshed you can see the meshing.
[5:49] This will be problematic when we interact with the bottle which will be less or plastic
[5:53] or something like that.
[5:54] As you can see we have all sorts of bumps in the mesh around where it meets the bottle.
[6:01] So what we can do is to snap it to the bottle G.O.
[6:04] So as you can see I have the interior of the bottle in here because since I model these
[6:09] all procedurally in in Odini I have access to the groups and whatnot.
[6:14] So where was I?
[6:17] We can actually bring that extrude back and just snap it to the surface.
[6:22] So if I show you before, before and after you can see how clean that is and finally we
[6:28] can do some little peak just to intersect with the bottle so which when there's nice.
[6:33] This snapping is pretty simple.
[6:35] We have the bottle G.O.
[6:37] You can actually use the full bottle I just thought it would be easier just to use the interior.
[6:41] But basically let me show you the blend mask which is something like this.
[6:46] We basically do a next-wise distance to the bottle and then we fit that distance between
[6:52] 0 and an offset value that I can set in here as you can see and all those points that
[7:00] are on the on the red part of this mask or that are part of the mask.
[7:05] We will blend between projected geometry, so mean both I can actually show you how that
[7:09] looks so we have to pass which will be just the points all projected to the bottle and
[7:16] we just blend with this mask so we don't project everything of course.
[7:20] So we basically do well-learned between the current position and the projected position
[7:24] which snaps to the surface and we use as blend the xyz distance this mask.
[7:28] So hopefully that was useful, that's basically how you can clean your mesh for rendering.
[7:33] Then do a little pick, some attribute blur and finally apply the transfer.
[7:38] So now I wanted to show you how you can do a planar projection in karma which is not that
[7:44] easy by default.
[7:45] So basically what I mean is being able to scale and move the projection around and don't
[7:50] project on the back.
[7:51] So the workflow is to start with a material exposition or if you have an animated object
[7:56] you can do a prime bar reader and read in the rest attribute so it's the same.
[8:01] Start with the position then we swivel the position where we need it to create the UVs.
[8:05] So we create UVs from the swivel position which in this case I wanted along the set so
[8:08] I'm going to grab the x and y position, combine it to a vector tool and use it as UVs in
[8:14] a material exp image.
[8:16] But I'm also placing a well a place to the node in between which I can use to scale,
[8:21] to offset on the x on the y and also place to pivot and we can also rotate as you can
[8:26] see.
[8:27] And it's important in the image that you set these to constants and constants on the
[8:29] address modes.
[8:31] So if we just connect these we will have a projection on both sides.
[8:36] So after taking the alpha and multiplying it by the mask along the z we have a correct
[8:40] alpha and finally we can just mix it.
[8:42] So for example I'm going to set the background color in here.
[8:44] So for example the yellow and just mix it with the logo.
[8:49] And now you have the sort of planar projection that you can rotate scale offset and play
[8:55] with it.
[8:56] So yeah.
[8:57] So let's say you start with the grids or any other mesh and you scatter some points and
[9:02] you want to find the near points to that specific amount which is just three points.
[9:06] If you do a near points you will find more than one point per initial point.
[9:12] So a simple way to solve this and an effective way also to solve this.
[9:17] To find exactly the amount of points you have on the second input so I can increase.
[9:21] For example to 9 and I'm from to 8 and I'm actually only selecting 8 points in total.
[9:26] So as you can see this works pretty well.
[9:28] So basically you do a wrangle and you find all the points you can do with a pacifying.
[9:32] I'm just doing with pacifying you can do with near points.
[9:35] Basically you want the array version of the near point which is near point.
[9:39] In this case I'm doing a pacifying finding the position of the input one which is the
[9:43] remeshed because you we want to find the values.
[9:47] We want to find all the values on the input mesh not these points because these points
[9:53] will be just one to zero one to want to find the point numbers on the mesh on the input
[9:58] one.
[9:59] So we do that pacifying and then we just set it as the tele-tributes.
[10:02] So if I actually look at that you can see that we have an array with all the points on
[10:06] the mesh not in here.
[10:08] So if we do it on these points we will have just the zero one to and after that we can
[10:13] just find in array.
[10:15] So basically we read that the tele-tributes on the second input and is an array and then
[10:20] we just use the find function to find in that array the current point number.
[10:25] If it finds that number so it's bigger or equals to zero otherwise it would be a negative
[10:30] number if it didn't find and we just group it and then in here we can actually place this
[10:33] an output group so we can visualize it.
[10:36] So that's basically it and you get the always the same amount of points you have you want
[10:42] to find.
[10:43] So not you don't have to tweak and play with the scale and what not to really find one
[10:50] point of so if I said it's to one I really find one point and not an island of points
[10:55] with like the default behavior of near points.
[10:58] And as always guys you can find the project files of this video on my Patreon alongside
[11:02] all the project files from my other videos as well as courses exclusive tutorials and many
[11:08] many tools.
[11:09] As always thank you for watching I hope you found this useful and I hope to see you next
[11:14] time.



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
