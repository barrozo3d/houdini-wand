---
title: Still Life Scene Breakdown | Houdini tips
source: YouTube
url: https://www.youtube.com/watch?v=peBkuU0Es1Q
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/still-life-scene-breakdown-houdini-tips/
frame_count: 0
frame_status: pending-selection
---

# Still Life Scene Breakdown | Houdini tips

**Source:** [YouTube](https://www.youtube.com/watch?v=peBkuU0Es1Q)
**Author:** cgside
**Duration:** 14m26s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py still-life-scene-breakdown-houdini-tips <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'm going to be breaking down the elements of this render
[0:07] mostly how I
[0:10] created a scene
[0:12] like wrapping low labels around the bottles
[0:17] how to do these water puddles
[0:21] create dust material and
[0:24] how to create this rock in here. So let's get started


### Wrap label around bottle [0:29]
**Transcript (timestamped):**
[0:29] So let's start by having a look on how to
[0:33] project logos or labels into the bottle
[0:38] So the first thing you might think is just use the Ray project here. I have the label and the bottle and
[0:48] I just use a Ray project on let's say minimum distance and
[0:54] If we have a look as you can see it doesn't work properly
[1:00] But if we set it to projected rays and vector set to
[1:06] Along the Z axis as you can see I was getting the stretched look which is not nice
[1:13] So what I did to solve that was
[1:18] Transfer the normals from the bottle as you can see
[1:24] I have the normals here
[1:27] And let me disable that
[1:32] And then I'm promoting them to point normals as you can see I have them like this spreading out
[1:41] And then I can blur the normals and
[1:45] Ray project it
[1:48] With the normal and as you can see that fixes the stretching and
[1:55] You can play with the blur iterations of the attribute blur in this case I used it quite a bit
[2:05] But yeah, that's how I solved that problem of the stretch look as you can see before
[2:13] And after


### Tear apart bottle wrap [2:17]
**Transcript (timestamped):**
[2:18] So now let's have a look on how to do the stair the part
[2:22] Rob or neck rope and
[2:26] The way I'm doing that is by creating a tube and Ray projecting it to the bottle
[2:33] then doing some basic UVs and
[2:38] creating a circle and distorting it with a mountain and
[2:43] And
[2:45] Create doing an abstracture then I can blast away and smooth out the edges
[2:52] From there I'm converting these to I'm converting the UVs to the position as you can see in here
[3:03] Assigning the UVs to the position
[3:07] and
[3:09] Now I want to bend this
[3:12] randomly in in in different sections
[3:16] So the way I'm doing that
[3:18] might not be the best way, but
[3:21] It worked for me is creating a line along the top of the
[3:27] the bottle wrap
[3:29] Doing a resample in this case I chose four segments and then I'm creating a attribute
[3:36] For each point as you can see five transfer it to the geometry
[3:42] You can clearly see how that looks I'm doing a natural transfer
[3:49] And as you can see I have point two point one
[3:54] point zero and I have a point three that just wrapped around because this geometry will be connected later on
[4:03] So then I'm doing an attribute blur to have some smooth transitions
[4:10] And after that I'm iterating and creating in a for each feedback
[4:17] set to count
[4:19] with let's see for fetch feedback and
[4:23] By count and feedback each iteration otherwise we would duplicate the geometry
[4:29] And so let me reset this
[4:34] And remove the visualization and
[4:38] I'm doing I'm placing first the bend where it needs to be as you can see right at the top
[4:46] And then I'm
[4:48] Bending randomly with a Fito one and a random function using the
[4:54] the metting port notes
[4:56] Plus the seed that I have here at the bottom that I added and
[5:01] Between zero and minus three forty and then I'm blending. This is where everything happens
[5:09] So if I remove this as you can see
[5:13] If I I don't need to remove that I just set to no scaling it's bending everything
[5:20] But now if I scale by attribute I'm just bending that specific part of the geometry and the bend attributes is
[5:29] That attribute that we created which is named pt underscore and then the detail iteration can be used to load the attributes
[5:40] So if we have a look at each pass source
[5:45] Single pass one two three and four
[5:50] As you can see
[5:54] And some of them I can play with the seeds
[6:02] As you can see some of their are some of the
[6:06] Regions are more bent than others and I can play with this I can say minus 90
[6:16] Minus 360 oops
[6:21] Oh
[6:22] Not minus sorry plus
[6:25] So now I have some geometry that is looking straight up
[6:31] Or I can play with this
[6:34] As you can see this is randomized
[6:37] Let me just get back to where I had before which is this
[6:43] Then I can use a point deform to get it back to position and
[6:49] And then fuse the points
[6:52] Softened the normals and that's basically it's how I did this neck prop around the bottle
[7:03] Maybe that are better ways, but I'm open to suggestions if you have another idea
[7:10] Yeah, okay for the water pedals


### Water puddles with displacement [7:11]
**Transcript (timestamped):**
[7:15] As you can see I have a plane between below the table just a little bit below and
[7:23] scaled up and
[7:26] Then if I disable this and go to the camera and
[7:33] Change the material. Let me just remove the transmission
[7:39] And set the base color to reds. You can see what I mean
[7:45] Let's have a look
[7:51] And by the way as you can see is rendering the full resolution
[7:54] So I'm going to press D and go to render and save your port size
[8:00] Now I can render faster as you can see so I have a displacement in here that I created with some noises and I'm loading it
[8:12] As an image file then using a smooth step to flatten the displacement flatten the image
[8:21] to be more black or white and
[8:25] Then I'm
[8:28] Connecting it to the displacement as and as you can see is creating these water bottles from the plane that is just a simple plane that is below the surface
[8:39] and
[8:41] If I
[8:44] Change it again to be
[8:48] transmissive
[8:50] You will start hopefully seeing the
[8:54] The water pedals it's at all but it's there and I can show you how I created
[9:03] the
[9:05] The water pedals noise
[9:08] So I'm starting with the grid unrapping
[9:15] To create the UVs
[9:17] Then I'm subdividing it quite a bit promoting the UVs to
[9:22] To point the tribute so I can use it in a point valve and
[9:28] In here I'm starting by creating these soft dots
[9:36] Mask
[9:38] As you can see
[9:42] And I'm
[9:44] Distorting the UVs with a turbulence noise as you can see because by default it looks like this
[9:53] So these soft dots that I have in here. This is just a mask to contain the effect
[10:01] Then I'm using two noises
[10:03] This is the first one which is a
[10:11] Turbulent no turbulence noise a set to alligator
[10:16] Then I'm feeding the range and
[10:20] Then I have a Voron wise
[10:23] As you can see Voronoi noise and
[10:26] Is creating this effect
[10:29] Then I'm maxing the two noises
[10:32] So an additive mode and
[10:35] Multiplying it by the initial mask
[10:38] This gives me this result
[10:40] Then I can create an output in here and create a copnet
[10:47] And if I go to the composite view I'm just doing a attribute import lives attribute import
[10:54] Selecting the geometry the target output resolution and
[11:01] Then just rendering to this the current frame and as you can see we have this displacement texture
[11:09] That I am using again in salaries to create the paddle effect
[11:16] As you can see it's settled that is there just creating this
[11:21] Nice effect on the surface


### Dust on top of objects [11:26]
**Transcript (timestamped):**
[11:26] So let's have a look on how to create this dust effect on top of objects
[11:32] So I'm mixing two materials one that is the glass and the other one that is the dust I can show you how the dust looks
[11:44] It's just a
[11:46] noisy gray material
[11:49] Oops
[11:54] As you can see I have a unified noise with the eye frequency
[12:00] Not this one
[12:04] This one
[12:06] With a very eye frequency then I'm contrasting the noise with a smooth step and mixing between black and
[12:15] dark gray or light gray
[12:18] and
[12:20] I'm mixing as a mixing factor as you can see in here in the materials. I am using
[12:28] Let me show you if I connect this in here
[12:35] So this is the color noise of the glass and
[12:41] As a mixing factor I'm using this one in here
[12:49] As you can see
[12:54] And then I'm multiplying this texture which is just too much and everywhere which doesn't make sense I'm
[13:02] multiplying that
[13:04] with the normal the Y component of the normal and that looks something like this
[13:11] And
[13:15] I also slightly distorted it with a fractal as you can see I'm adding to the normal
[13:22] this fractal and then
[13:26] Extracting the Y component and using a ramp again to contrast the effect and
[13:32] With the previous texture I am just multiplying and get
[13:38] this result in here and
[13:42] This is the mixing factor of my
[13:47] materials
[13:48] both the glass and dust
[13:53] And if we put everything together
[13:59] We would get something like this


### Outro + full scene [14:03]
**Transcript (timestamped):**
[14:03] So as you can see here in more detail
[14:07] So yeah guys that was basically it. I hope you have learned something new as
[14:14] always you can grab the full scene on patreon and
[14:20] I hope to see you soon. Thank you



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
