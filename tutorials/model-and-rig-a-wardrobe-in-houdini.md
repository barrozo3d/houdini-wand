---
title: Model and Rig a Wardrobe in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=c_t8JwyHJrA
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/model-and-rig-a-wardrobe-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Model and Rig a Wardrobe in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=c_t8JwyHJrA)
**Author:** cgside
**Duration:** 10m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py model-and-rig-a-wardrobe-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'll show you how we can create this
[0:04] asset in Odini and also how to rig it so rig the opening of the doors. So let's
[0:14] get started by looking at the top. I'm starting with the grid which will
[0:19] like the single panel, then I'm copying it several times. In this case by using
[0:26] the bounding box exercise so it aligns properly or perfectly, then place it
[0:34] in the center and in this case I'm running a loop to divide the geometry into
[0:41] sections. I am switching between, in this case I have a switch in here that
[0:47] randomly switches between just a wide division so just dividing the
[0:56] primitive in the middle. In this case by using the bounding box y size and
[1:03] divide it by two. As you can see this will give you the distance that it should
[1:10] place the line and on the other side I'm taking the primitive, creating a line
[1:20] to match the same size, in this case I'm taking uniform scale, then reassembling
[1:26] it to the amount of sections you want. Then in order I'm using a
[1:32] Voronoi fracture. If I disable this point cheater you can see that it's
[1:37] perfectly dividing the geometry into sections. I can do that easily with a
[1:45] divide. But since I wanted to randomize I use this setup which is a Voronoi
[1:51] fracture and for the Voronoi fracture you actually need point centers. As you
[1:58] can see I can show you. So you actually need point centers and not the
[2:06] the intersections itself. So in order to create the point centers after the
[2:13] re-sample I'm subdividing to get those point centers. Then selecting the
[2:21] outer ones so the original points by using a group arranged node selecting
[2:28] one or two, blasting those and that's basically how you get even distribution
[2:36] of sections. And then just I'm randomizing it so first selecting the inner
[2:44] points and then adding a point cheater to those inner points. In this case I
[2:49] changed the seed on each iteration which you can do by using the detail, the
[2:57] the iteration detail attribute. And you get something like this. So in here I'm
[3:06] just alternating between the inputs by using a random function and multiplying
[3:13] by the output which is the number of inputs we have. And if I show you let me
[3:21] get this. Rightly parameters. If I show you in here the switch you can see switching
[3:34] between switching between 1 and 0. So that's how I've done that part. Then I'm
[3:49] just extracting the edges, the silhouette I mean basically by extruding it in
[3:59] or inserting it. And then I ended up with something like this, fusing the points,
[4:06] extruding it back, taking a bound and placing it in the back and just merging
[4:14] everything. At this point you can create some name attributes to target different
[4:19] geometries but I'm just doing this as an example so that's our wardrobe base.
[4:26] And now for the rigging. I'm starting with the base which is this part in here.
[4:35] So the base. Then selecting half of the frames in this case I have four I will get to by using
[4:44] in the end 10 frames divided by two. This case is getting to blessing every other primitive.
[4:53] And from here why should we go so first of all I'm creating an image reboot for each primitive
[5:05] by using a prefix and the prime number as a string. And here I'm doing some sub
[5:14] operations but we'll get there in a bit. So for the rigging I'm first creating some
[5:22] points at the center, at the left center of each prime by using the bounding box center
[5:30] and the bounding box mean commands. And then adding those points in this case by group with an
[5:40] add node, placing a rig doctor and initializing transforms. Then doing the capture back GU
[5:52] in this case using the name attributes and a bone deform. And where everything happens is on
[6:01] this rig wrangle that was kindly shared by swalch on the CG weekly scores. So so basically we
[6:13] create a parameter for the rotation in this case in radians. We want the input as degrees
[6:23] but we need to translate it to radians. In here we are we are alternating between minus one
[6:30] for even points and one for odds to create the alternating directions as you can see in here.
[6:38] Then we need on the first point to rotate only half. So we this is basically an if statement. If the
[6:46] point is zero, we want just to multiply by half of the rotation for the other one just
[6:56] use one which will have no effect multiplying by one. And in here we just use the pre-rotate
[7:03] for the local transform and multiply the panel angle which is this angle we have in here,
[7:09] this parameter and multiply it by the panel sign which is alternating directions. And also for
[7:19] the first panel which we just want to rotate half. And we want to rotate around why that's why
[7:26] we use the X's. Again shared by swalch which I'm very grateful and if you're interested in
[7:36] joining the CG weekly scores just check out Matistella Patreon and you'll get access to it.
[7:45] So having this we can now mirror the effect and we will get these nice sliding doors.
[8:01] Then we can just matchize it to the main part of the wardrobe and that's basically how it's done.
[8:12] For this pattern in here it's actually pretty simple. First of all let me see I already covered
[8:23] this part. So we're iterating over each frame and basically dividing it evenly, dividing each
[8:34] primitive evenly as you can see in here. So if you remember from these divide nodes and I shared
[8:44] these plenty of times on my channel. Basically you take the bounding box the size of the
[8:52] axis you're working with and divided by the number of divisions you want. So let's say five I
[8:59] get five sections in this case I set it to two and in here we're we're using a multiplier which
[9:12] I call density and basically taking the in this case the X size and dividing it by the same
[9:22] X size but with a seal since we want integer numbers and multiplied by the density.
[9:29] And if I change this to 20 we get less and we do the same for the Y axis as you can see.
[9:38] Then just extrude it in this case I am in setting it, extruding and creating some normals
[9:49] and we get something like this. So yeah that's basically it's if you like to get access to the
[9:57] full scene feel free to join my patreon and you can get all the project files from my videos along
[10:05] with exclusive tutorials and I also have some courses in there. So if you want to check that out
[10:12] and other than the self promotion that was basically it's thank you and I'll see you next time.



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
