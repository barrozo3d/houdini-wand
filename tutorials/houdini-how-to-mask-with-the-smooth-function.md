---
title: Houdini: How to mask with the smooth function
source: YouTube
url: https://www.youtube.com/watch?v=7U8slXjQ3-s
author: the point and prim
ingested: 2026-07-16
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-how-to-mask-with-the-smooth-function/
frame_count: 0
frame_status: pending-selection
---

# Houdini: How to mask with the smooth function

**Source:** [YouTube](https://www.youtube.com/watch?v=7U8slXjQ3-s)
**Author:** the point and prim
**Duration:** 7m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-how-to-mask-with-the-smooth-function <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back.
[0:03] Today we are starting a new series of videos.
[0:05] Normally I concentrate on a specific effect and share that information with you, but this
[0:09] series will be about some of the more low level core techniques that I use day to day in
[0:13] production.
[0:14] These techniques serve as the building blocks, the foundation for a lot of the work I do,
[0:18] and we use together can achieve a lot of different types of effects.
[0:21] These videos will be done in more of a classical step-by-step tutorial fashion.
[0:25] We will concentrate on theory rather than achieving a final effect.
[0:28] However, if you would like to see how the effect showcase has been built, the project
[0:32] files are available on Gumroad.
[0:33] I am currently planning to keep adding to this project over time as the series progresses,
[0:37] so be sure to check back later for more content.
[0:39] Knowing how to create, control, and animate procedural masks along the length of geometry
[0:43] is one of the key components needed to build effects.
[0:46] But before we can start making cool stuff, we need to know the technical foundation behind
[0:49] this technique, which is why we are going to start this series with creating masks in
[0:53] the simplest form, along a single axis.
[0:56] After that in the following videos we can build on top of their techniques, we already
[0:58] know to increase complexity over time.
[1:01] So let's get started.
[1:03] Let's start with a humble box, moving it into a zero to one range for clarity, and
[1:08] remissioning to get more resolution to work with.
[1:10] I'll put down a point for up and jump inside.
[1:12] The first thing we want to do is to use a relb box node.
[1:15] This will return the bounds of the geometry and a range that is always normalized between
[1:18] zero and one.
[1:20] If we split the result of this node up into its components and visualize x only, we
[1:24] can see that it has been mapped perfectly between zero and one as expected.
[1:27] Drop down a smooth drop onto this connection.
[1:29] You may notice there is a slight changing color, especially around the black area.
[1:33] And that is because the smooth function is now computing ease out interpolation instead
[1:37] of linear.
[1:38] If you don't know, that is basically just the default tweeting who Deany gives you if
[1:41] you set two keyframes.
[1:43] So if we play with the ranges, we start to squeeze black and white together, and that
[1:46] is because anything less than range bottom will return a zero and anything greater than
[1:50] range top will return a one and whatever is left between gets the ease in and out interpolation
[1:54] between zero and one.
[1:56] Now that we understand the theory, let's reset the ranges.
[2:01] And expose range top as a new parameter.
[2:03] By adding a tiny amount to range top and plugging it into range bottom, we can create
[2:06] a super sharp animated mask as the interpolator values are squeezed super tightly.
[2:10] This basic technique forms the foundation of a surprising amount of effects and is exactly
[2:15] the same technique I used in two of my videos for this channel.
[2:18] If you haven't seen those yet and want to, you'll find the links in the description.
[2:22] So we've got this sharp line mapped perfectly along X.
[2:25] You will of course ask, how do we get some break up and distortion on it?
[2:28] And a simple way to do that is just to add a little bit of noise to the range top parameter.
[2:32] This is just going to add and subtract values from the incoming parameter based on the
[2:35] noise pattern.
[2:36] If we come up here and set a couple of keyframes, we can see what that looks like on the
[2:39] fly.
[2:40] If this doesn't completely make sense, I'll try to explain the theory.
[2:43] So we have our full range from 0 to 1 and let's say our range top palm is at 0.5.
[2:47] If we would add 0.1, we get 0.6 and if we subtract 0.1, we get 0.4.
[2:55] Instead we're just going to use a noise pattern with a max value of 0.1 in both the negative
[3:00] and positive directions.
[3:01] Our line is made up of a bunch of points which will then just get remapped based off of
[3:05] the noise pattern.
[3:06] So it ends up looking something like this.
[3:09] So now that we understand that, what else can we do with this?
[3:12] If we just disable the noise for a second and drop a float ramp set to heel on our x component,
[3:16] we can see that it has now remapped our line into a central band that squeezes inwards
[3:20] from both sides.
[3:21] If we re-enable the noise, it is still working as intended.
[3:26] Theory time again.
[3:28] So by default, we have our values mapped from 0 to 1 linearly like this.
[3:32] And then we would set our range top to 0.5, we are effectively squeezing the values into
[3:36] this sharp interpolation.
[3:38] But by setting the ramp to heel, we are changing the mid-value to 1 and the end-value to 0.
[3:46] So if we were then to change our parameter 0.3, we're going to squeeze the bottom towards
[3:50] 1 but also the top as it is now mapped to 0.
[3:54] Say we wanted to keep the shape of this band but have it animated from left to right like
[3:57] we did before.
[3:58] How do we do that?
[3:59] Well we could crunch all the ramp values together and then keyframe them but that would
[4:03] get messy really fast.
[4:05] Let's set these back to something a little more reasonable.
[4:08] Jump back into the point for it.
[4:10] The way we can do this is by offsetting the value piping into the ramp.
[4:13] This can be done by simple addition or subtraction.
[4:16] So we can promote a parameter called offset and then keyframe that instead.
[4:19] This way all of the parameters that define the shape of the band remain static, such
[4:23] as the range and noise and then the only palm that is dynamic is the offset.
[4:27] So we have our x component being piped into the ramp which only remaps values between 0
[4:31] and 1.
[4:32] Let's first visualize with linear interpolation.
[4:35] If we would subtract 1 from this all the values encapsulated in the ramp would be 1.
[4:39] If we add 1 instead all values will be 0.
[4:42] Subtracting 0.5 clips all values above 0.5 to 1 and adding 0.5 would clip all values below
[4:49] 0.5 to 0.
[4:51] This means that animating the offset amount is just dynamically changing the value being
[4:54] fed to the ramp.
[4:55] Of course we've got this squeezed band but what we're doing to the values is exactly
[4:59] the same, just offsetting the incoming value of the x component.
[5:03] Now I'm actually going to disconnect the animated parameter because I want to replace it
[5:07] with the frame global palm.
[5:09] We can use a fit range and remap our desired frame range between minus 1 and 1 and that
[5:13] will give us a clean wipe across the geometry.
[5:15] In the example shot the wipe effect repeats itself and that of course is easily done using
[5:19] the modulo function.
[5:21] By default you'll want to set the modulo value to be the same as the source max and fit
[5:24] range in order to create a loop.
[5:26] But I halved the source max so there is a pause in between the pulses.
[5:30] At this point we are done with the key components of the effect and the rest will just be artistic
[5:34] changes.
[5:35] All I do here is disconnect the range top of the smooth in order to get softer fall off
[5:38] and then tweak the noises a little bit.
[5:40] If you are new to Houdini and didn't understand some of the things that I've gone through
[5:43] in this video, this is a good point to stop watching and just start making lots of different
[5:46] versions of this vop and playing around with all the different components to see what
[5:49] you can squeeze out of this simple setup.
[5:52] The amount of combinations is surprising and the best way to learn in my opinion is by
[5:55] doing an analyzing.
[5:58] This video is not about the effects but I will quickly walk you through the setup anyway
[6:02] so I just swapped up the standard box for a slightly more complex one and the same point
[6:06] vop still works.
[6:07] I delete all the primes using an ad note and cash out the points.
[6:11] I use two clip nodes just to trim off the top and bottom faces as I don't want to emit
[6:14] particles from there and just add some curl noise mixed with bespoke velocity along the
[6:19] normal and negative wide direction.
[6:21] Next I just stuck up some noises to disturb the points of it, gradually making the frequency
[6:25] smaller with each stack and neat trick is to also attribute blurp of the particles and
[6:29] then merge it back with the original as it will create two different looking layers.
[6:33] Next I set density to cd.x so that it fades off around the edges of the band and then
[6:37] I rasterize it.
[6:39] Usually rasterize makes volumes a bit blobby so I often add a cloud with speed noise to
[6:43] break it up a bit.
[6:44] Here I'm using the bounding box of the original geo just to fade off the density around
[6:48] the top and bottom.
[6:49] After this I cash out this source volume which will of course next be piped into a pirousova.
[6:53] This smoke doesn't need to be perfect as it isn't rendered but it will take the particle
[6:57] movement via advection.
[6:58] I use the original cash point as the particle source and in terms of the potnet there
[7:03] is nothing fancy, just the pop advect and a bit of pop wind mixed in with it.
[7:07] The pop sim comes out looking like this with the velocity from the smoke sim doing all
[7:10] the heavy lifting.
[7:12] Finally I use the atrored blur, patriotic again to get another layer of complexity and
[7:16] merge it back with the original stream.
[7:18] The final nodes here are just setting attributes for rendering such as p-scale and some tweaks
[7:22] to velocity.
[7:24] I'm not going to be covering shading and rendering in this video but if that is something
[7:27] that you'd like to look at further I encourage you to download the free project file on Gumroad.
[7:31] You'll find the link in the description below.
[7:33] That is it for this video, in the next one we will continue to build on top of this
[7:36] knowledge to achieve more complex masking effects.
[7:39] As always, thanks for watching and see you in the next one.



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
