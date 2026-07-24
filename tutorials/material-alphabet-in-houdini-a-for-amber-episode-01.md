---
title: Material alphabet in Houdini: A for Amber | Episode 01
source: YouTube
url: https://www.youtube.com/watch?v=nyqL7CA6phk
author: Kotov Roman
ingested: 2026-07-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/material-alphabet-in-houdini-a-for-amber-episode-01/
frame_count: 0
frame_status: pending-selection
---

# Material alphabet in Houdini: A for Amber | Episode 01

**Source:** [YouTube](https://www.youtube.com/watch?v=nyqL7CA6phk)
**Author:** Kotov Roman
**Duration:** 10m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py material-alphabet-in-houdini-a-for-amber-episode-01 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey, this is the first piece of my Material Alphabet series.
[0:04] In this series, I'm going through the alphabet and creating a different material study for each letter.
[0:08] The goal is not to make a perfect production breakdown or a strict step-by-step tutorial,
[0:13] but to show the process behind the piece, how I approach the form, texture, lighting, rendering,
[0:18] and look development in Houdini and Redshift. This is part one, so I'll start with the foundation
[0:23] of the setup and begin shaping the main loop. We're starting with Ember. Let's begin with
[0:29] our foundation, an empty container labeled setup in colored red. Inside, I'll drop down a font
[0:36] node and lay it flat. I will copy this node and type in Ember. I have no idea if I'm going to end
[0:42] up using this one, but let's increase space between the letters just in case I will.
[0:48] Let's pull up our references. Right from the start, I can see that it's reflective,
[0:52] not a ton of roughness is going on. And surfaces are rather smooth, except for this one. Has a bunch
[0:58] of surface and internal details. Let's see how we can replicate something like that. First of all,
[1:04] I will need a thickness, so let's add poly extrude node and bevel the edges with the help of poly bevel.
[1:10] Sadly, bevel doesn't really work with that complex geometry. Luckily, we can use VDP from
[1:15] polygons instead, because we don't need to maintain that level of details from our sort
[1:18] geometry. Let's convert it back to polygons with the VDP convert node. We get a lot of
[1:23] jagged edges in the process, but nothing VDP smooth can fix. I like the general direction this is going
[1:28] so far. But I think VDP smooth is doing a bit too much. Let's increase the resolution and adjust it.
[1:35] VDP convert node doesn't generally give a great topology to work with. It fixes that I will use
[1:40] a remesh node and drop down target size. From this point on, for the next several minutes,
[1:45] I went on a bit of a side quest. I was trying to get this level of surface details,
[1:50] and I didn't use any of that really. But that's a learning process.
[1:54] Let's get back to a simpler setup. I think I will be going for this kind of look,
[1:59] with intricate cracks on the surface and on the inside. First, I will deal with the insides.
[2:06] There are several ways of doing that. The easiest one, in my opinion, is just to get some geometry in
[2:10] there. For that, I'm going to be using VDP fog and a scatter node. To make scatter more interesting,
[2:17] I'm going to be using volume VOP to add some noise in there. My usual go to noise is NTA list
[2:23] noise. It goes from minus 0.3 to 0.3, so we will have to use a fit node. I will also attach a ramp
[2:29] node later. It's going to be set to scalar. To make it easier for myself and not jump in and out of
[2:35] the VOP, I will promote noise parameters to the outside of it. That's where the ramp comes in handy.
[2:43] After that, I would need a scatter node. Let's reduce the point count.
[2:47] And add a random normal vector, using attribute randomize. If you're doing the random vector,
[2:52] you should use inside sphere. And if you plan on doing the animation, it's best to use ID attribute
[2:57] to the seed. If you're using ID attribute, don't forget to export it from a scatter node. Now we
[3:03] are ready to copy some geometry onto those points. Standard way of doing that is using copy to points.
[3:09] I will be copying the grid geometry, but I will make it smaller. Right now, it kind of looks like a
[3:13] mess, but I will make it even worse when I add a mountain node. Think the grid size is still way too
[3:19] big. Let's make it a bit smaller. Now it looks more to scale. And to the fun part, let's add a Boolean
[3:26] intersect node. It's very important to wire up the letter geometry into the first input,
[3:31] and a grid geometry into the second. Because a grid geometry doesn't have any volume,
[3:36] we should set B to surface. Now that that's working, I can adjust the resolution of the grid and its
[3:41] noise. Usually after a Boolean, it's a good idea to add a normal node. So I will do just that.
[3:50] Now I'm ready to set it up for rendering. But before I do that, I will add a mob's noise
[3:55] falloff. I have no idea if I'm gonna end up using this one, but I think I will for shading.
[4:01] I will add a series of nulls. Their names will start without, so it will be easier to find them
[4:06] later. So out shell and out insides. I will add two more geometry containers. Call them shell render
[4:13] and inside render. Inside of them, I will add an object merge and merge those nulls in there.
[4:19] Now we can start setting up the lighting. Let's drop down dome light and choose any HDRI.
[4:26] And don't forget the camera. My current layout is best suited for horizontal videos.
[4:32] This one is gonna be vertical, so let's make some adjustments.
[4:35] If you hold Alt and click left square bracket, it will split any window vertically.
[4:40] Right square bracket will split it horizontally. As usual, I will create a Rob node.
[4:46] Call it cam 1 and assign a camera to it. Now we can start rendering.
[4:50] Forgot to disable deadline worker there.
[4:54] Now we can start rendering for sure. Just have to adjust my camera a bit.
[4:58] Let's start by creating one material. Call it amber and assign it to a shell geometry.
[5:04] I also would like to get some sort of background going, so let's add a grid geometry.
[5:10] Let's make some more room to work with and start with the material.
[5:14] I'd like to set transparency to 1, increase depth and color it orange.
[5:19] I also would like to increase extra roughness and reduce reflection roughness to 0.
[5:29] Maybe I will set extra roughness to 0 as well for now.
[5:32] Let's make a snapshot and a screenshot for future references.
[5:36] And see if I can dial in refraction and reflection roughness.
[5:42] Let's assign this material to the insides as well.
[5:45] They turned out black. Not really what I was expecting.
[5:49] Let's try to fix that by turning on thin bulb. That doesn't really work either.
[5:53] I will try a different approach. I will create a new material for the insides.
[5:57] And let's try to turn on thin bulb there.
[6:00] Okay, let's see if that's something we can fix with a trace depth.
[6:04] That sort of works, but it's still not what I'm looking for.
[6:14] Usually something doesn't work as I expected. I like to start from scratch.
[6:19] Let's create a new standard material. Turn on transparency, but leave it white.
[6:24] Now I'm thinking maybe I should adjust geometry itself.
[6:28] That looks even worse somehow. I will continue trying to find the right balance.
[6:36] That seems like a bit too much of the insides, but I still want to see how it looks on the render.
[6:41] Still not the best. I will try bringing back trace depth to its original values.
[6:47] And maybe making grids smaller and fewer.
[6:51] Let's check out how the insides look by themselves now.
[6:56] I can see that they didn't look correct at all, so I will start there.
[7:00] First, I will change the lighting.
[7:06] Second, I will try to add some thickness to them using Thickness Lab node.
[7:10] But for it to work, I will have to switch B to Solid in Boolean.
[7:16] That looks already closer, but it's still too noisy. I will have to simplify that a lot.
[7:23] Maybe changing the type of the noise will help.
[7:31] Or reducing the number of the grids.
[7:35] That's what it's supposed to look like. Let's see how it looks with a shell geometry.
[7:40] And it's not working again.
[7:54] Let's change the number of the grids again.
[7:57] That looks really close to what I want. The only thing left to do is to figure out
[8:00] how to make it work with a shell. I think the main problem is the lighting.
[8:04] We can see the background through the glass. That's why it's lacking contrast.
[8:08] It also would have helped if I would have disabled thined walled on the shell.
[8:14] I will make a screenshot of that, again for future references.
[8:18] And of this one as well.
[8:20] Now is a good time to look at the references and see what the difference is.
[8:24] The biggest one that I can see is that it has a black background.
[8:27] So let's start there.
[8:29] I will disable the grid and also camera rays in the HDRi.
[8:33] I will probably rework lighting completely and use a rest light instead.
[8:38] I'm gonna position behind and slightly higher from our subject.
[8:44] Now I can get back to thicken the material. I will start with the clean material
[8:48] and set it up from scratch.
[8:52] I like the roughness, but the light shines through way too much.
[8:55] Let's move it higher and increase exposure to compensate.
[9:00] I will also make it wider so I get more reflections on the leather.
[9:04] Now we're getting somewhere. Let's screenshot that as well.
[9:08] Let's see if I can set up the second light.
[9:13] I will copy the existing one and move it down and to the left.
[9:19] I don't want it to shine through too much, so I will not move it under the leather.
[9:24] We're definitely getting closer. I will screenshot that as well.
[9:31] And I did not disable thined walled for this material.
[9:34] I will do that and see what difference does it make.
[9:37] I am not a big fan of that look, but I will screenshot that just in case.
[9:42] Maybe if I decrease the intensity of the light it will work better.
[9:47] At this point I would like to add air bubbles to the setup.
[9:51] It's gonna be done in a similar way I did the insides, but instead of grids it's gonna be just
[9:56] points and instead of randomizing normals I will be randomizing p-scale.
[10:00] I will get another and call it out points.
[10:03] Now I will need to get additional geometry container and merge that null in there.
[10:07] In order for Houdini to render points and spheres you have to check render
[10:11] objects as particles in the particles tab.
[10:14] And I remembered that I didn't check the p-scale attribute. Let's do that now.
[10:22] That's it for this part. In the next part I will continue from here and develop the piece further.
[10:27] If you missed any previous parts the links are in the video description.
[10:31] And if you want to follow the rest of the material of the bit series I have linked the full playlist
[10:36] there as well. Thanks for watching.
[10:39] Thanks for watching.
[10:41] Thanks for watching.
[10:44] Watching.
[10:45] Thanks for watching.



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
