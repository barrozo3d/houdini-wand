---
title: Houdini Tips | Tileable Noises, Cam from Stage, TOPS and more
source: YouTube
url: https://www.youtube.com/watch?v=zItss8TuZMo
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tips-tileable-noises-cam-from-stage-tops-and-more/
frame_count: 0
frame_status: pending-selection
---

# Houdini Tips | Tileable Noises, Cam from Stage, TOPS and more

**Source:** [YouTube](https://www.youtube.com/watch?v=zItss8TuZMo)
**Author:** cgside
**Duration:** 17m28s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tips-tileable-noises-cam-from-stage-tops-and-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video we'll be going over five different setups in Odini.
[0:06] Hopefully there will be a tip for everyone. So let's get started.


### Import Camera from Stage/LOPs [0:12]
**Transcript (timestamped):**
[0:12] So the first thing we're going to have a look is on how to import the camera from stage
[0:20] to the object level.
[0:23] Let me just resume the renders. You can see I have an animated camera in here.
[0:28] And with the camera position setup, I end up wanting to import it to the object level.
[0:38] So what we can do is go to the object level and in here we can use a lot of import camera.
[0:48] And we will go in here and go to camera 2 in this case and pick the camera 2.
[1:00] And as you can see we have the camera imported and if we go to the Loving Port camera 1,
[1:06] we can show the timeline. Let's go again to the camera. And as you can see we have the camera here
[1:15] with the animation and everything. This can be useful if you want to export your camera
[1:21] from the stage. And that's the only way I know that you can do that apart from USD.


### Problem Space with RBD Fracture [1:28]
**Transcript (timestamped):**
[1:28] So now I'm going to show you how I created this stretched out look in some sort of rock wall.
[1:37] So the idea is simple. I'm starting with a cube that I rematched or a box.
[1:46] And then I'm transforming it. As you can see I am using the scale along the Z axis
[1:56] to make it bigger along the Z axis. And also share I am introducing some shear to have this
[2:03] skewed effect. Then I'm doing the normal RBD fracture.
[2:12] And if I show the attribute as you can see I have the normal result of the RBD fracture.
[2:21] But in here before fracturing the object I'm in the transform. I'm outputting the X-form attribute.
[2:31] So I can use a match size and transform it back to the original shape. That way getting the
[2:38] distortion for free. So in here in the match size I can restore the transform and use the same
[2:45] attribute. Then it's quite easy. I can assemble the pieces and group the front ones as you can see
[2:54] by just using the bonding box on the Z and then blasting away those primitives.
[3:01] And from there I can start to reshape the different parts.
[3:07] And in the end I can end up with something like this.
[3:16] Which is somewhat interesting in my opinion.
[3:21] So you can get this file on my Patreon if you're interested in looking at the setup.
[3:27] It's nothing too complicated but if you're interested it will be available on my Patreon.


### Converting/Resizing Images with TOPs [3:35]
**Transcript (timestamped):**
[3:36] So I downloaded some 16K HDRs from the internet and they are too big to use at least in my
[3:44] scenes. So I'm going to convert them to 2K and 4K. So for that I'm using a top net
[3:55] and in this case I can use a file pattern and load in all the files. So star in that specific folder.
[4:06] So I can generate the nodes and you will see I will have the file, the two files and I will have
[4:17] the directory extension and file name that I can use in the output node. So for both textures.
[4:26] And then I can just use the image magic nodes and in the output file paths I can say add the
[4:35] directory. So the folder then I can create a custom folder named convert it. Then file name.
[4:47] File name and then the extension. Ignore this for now because as I told you I need to
[4:57] to create two versions of the file. So one with one with 2K and another one with 4K.
[5:05] So for that I'm using a loop. So just create a forage loop with feedback.
[5:13] But in this case I'm not going to use the feedback option. So I'm untaking feedback.
[5:20] And creating two iterations and as you can see I have the loop iteration in here variable that I
[5:27] can use. So in here I can go to the widths and multiply 2K by the loop iteration plus one
[5:35] since I don't want to multiply it by zero which is the first iteration. So I will have 2K
[5:42] and then in the second iteration I will have 4K. And as you can see I'm also naming the output file
[5:51] with that loop iteration ID let's say. And I'm doing the same for the I'd bet you don't need because
[5:58] there's a preserve aspect ratio in here. So if I cook this node right now
[6:07] and it's cooked it took about 10 seconds I don't know. And as you can see I have now a folder
[6:19] called converted and I have 2K version and 4K version if I enable one to one as you can see it's
[6:32] much bigger. And for the other file I also have a 2K version,
[6:38] fineable here. I am using a full HD monitor. So and the 4K version in here.
[6:50] So yeah that's how you can convert your files to a more manageable format let's say.


### Tileable Noises in Houdini [6:59]
**Transcript (timestamped):**
[6:59] So now we're going to have a look on how to tile noises to make noises
[7:05] tileable textures. So for that I have just a plane that is one by one in here and I subdivided and
[7:14] created some UVs. So I can export it later as a texture. And in here I have another grid which is
[7:24] 3 by 3 and I'm extracting the centroid and copying two points so I can see the the
[7:31] the tile levels. The tileable texture. As you can see in here I already have one setup
[7:38] that I'm going to start over. So let's go with a point for
[7:45] and I'm going to create a unified noise static in this case connect the position
[7:54] to the position and the noise to the CD. So this is not tiling by default and to tile it what
[8:06] you need to do is set it to periodic and you need to copy the frequency and use it in the periodic.
[8:16] And as you can see the simplex is not a tileable noise although it has this periodic option.
[8:22] So for tileable noises you will see you have perline as you can see it's already tiling. Let me
[8:30] just change the frequency to something like 16 and you can see style is tiling if I unchecked
[8:42] periodic is not tiling and other noises that are tiling you can just experiment what this
[8:52] elevator is as you can see but if I increase a bit you can see it starts to break the tiling
[9:02] if you look closely that's because you can only have integers in the frequency
[9:09] so as you can see now is it works again and you can obviously have an offset
[9:24] and you can also introduce some fractal but if you look closely it's already broke the tiling
[9:34] effect so what you need to do is add the like an arity to an integer value and now you get tiling back
[9:43] so just some rules you have to follow and let's decrease the frequency
[9:51] oops
[9:57] let's say 2 by 2
[10:02] and now you want to to distort this noise so what you can do is create another unified noise
[10:12] unify a new static and connect it to the position set it to a 3D noise since we want to distort
[10:24] and let's say sparse convolution and change it to periodic and let's copy and paste
[10:34] and increase this to 3 and create an add node
[10:43] and add it to the position so as you can see it's creating the distortion that is not tiling
[10:51] properly so what we need to do is change the noise type because the sparse convolution is not
[10:58] palatable so we need to change it to pardon flow or simplex is not palable either so you can change
[11:07] it to warlay but the best one would be the pardon flow and then you can if it's distorting too much
[11:16] you can go to the amplitudes and change it decrease it quite a bit
[11:25] and maybe reduce the frequency to
[11:33] so that's how you do it and maybe we can change this nice type
[11:42] and we get this sort of patterns so in here i create this one which is also tiling
[11:52] and the only thing i did different was changing the noise type and the frequency as you can see
[12:02] all numbers again no floating point numbers which causes the tiling to break
[12:10] so yeah that's about it tiling noises in Odini that you can export from Odini and use as
[12:20] displacement maps or anything you need so in this one i'm going to show you how you can easily


### Vellum random Emit [12:24]
**Transcript (timestamped):**
[12:27] emit objects randomly using valum in this case i am using it to emit some debris and fall
[12:38] over the between the tiles so as you can see i have a file in here a lambic file
[12:47] where i imported some dead lips then i'm unpacking and converting it to polygons as you can see
[12:54] i have the UVs then just for quick visualization i'm using a UV quickshade
[13:01] the leading end is small lips that i don't need
[13:06] then i'm deleting everything but keeping the normals and the UV and the materials
[13:14] using a name to name it before the simulation and a connectivity so as you can see if i change
[13:21] this to class and remove this visualization we have a class for each a different number for each
[13:30] leaf then we can use it to copy over to some lines that are animated or randomized
[13:42] first of all in the point jitter i'm using dollar f times something just a random number
[13:49] so they jitter up and down along the or along the z axis i mean and then i'm using a transform
[13:59] but it's just to move them up no animation and then setting some p scale and in the normals
[14:09] is where i'm randomizing also to have some random orientation so in the global seed dollar f times
[14:18] some random number and we have this animated thing going on and let me see in the resample it's
[14:31] always 10 then i'm copying two points those objects who's using a attribute from pieces
[14:39] set to random and in a copy to points i'm using the piece attribute as we covered before
[14:46] so it's is copying random leaves to the points and this is the result
[14:54] then i'm doing a valum close just default settings and i'm outputting the geo and the constraints in here
[15:07] then using the this geometry as a collider in a valum solver as you can see no inputs for the valum
[15:16] geometry or the constraints and in the valum solver in the valum solver i'm using a valum source
[15:29] and for every 10 frames i'm emitting and i'm loading in the sub-pad of the geo and the constraints
[15:41] and if we have a look at this and make sure to visualize this
[15:54] we are in this emitting the leaves and the twigs at each 10 frames as you can see
[16:06] it's pretty slow because i'm recording but if i have a look at this simplified example in here
[16:15] which is just the same but some simpler objects and agree and i use a valum solver
[16:24] you can see if i disable the visualization so as you can see it's emitting
[16:35] every 10 frames because you don't want to emit every frame so you want to emit from time to time


### Outro [16:45]
**Transcript (timestamped):**
[16:46] so yeah guys that's basically it hopefully you picked up something new so as always we will be able to
[16:55] get the files on my patreon as you can see in here i have a lot of other files that you can download
[17:06] and you can also check my shop where you will be able to find three different products right now
[17:14] and they are pretty cheap as you can see so if you want to support the channel have a look at those
[17:22] so yeah that's basically thank you for watching and i'll see you around



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
