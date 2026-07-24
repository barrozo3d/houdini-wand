---
title: Abstract liquid in Houdini  |  Part 01 - Building the simulation
source: YouTube
url: https://www.youtube.com/watch?v=pFvA23fP5I8
author: Kotov Roman
ingested: 2026-07-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/abstract-liquid-in-houdini-part-01---building-the-simulation/
frame_count: 0
frame_status: pending-selection
---

# Abstract liquid in Houdini  |  Part 01 - Building the simulation

**Source:** [YouTube](https://www.youtube.com/watch?v=pFvA23fP5I8)
**Author:** Kotov Roman
**Duration:** 15m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py abstract-liquid-in-houdini-part-01---building-the-simulation <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello! Today we will be looking at the first part of the 3-part tutorial series.
[0:05] In the first tutorial we will dial in the simulation.
[0:08] In the second one we will tackle the development.
[0:11] And finally in the third part we will do some light composing.
[0:14] I hope you find this tutorial useful and pick up something new along the way.
[0:20] Let's create a geo container, call it setup.
[0:23] I like to color mine red, so let's do that and jump right into it.
[0:29] We would need a box, just a simple box, but we will squish z-axis to 0.01.
[0:38] Nothing fancy so far, but we will fix that later.
[0:44] After the box, let's create points from volume.
[0:48] And I would like to lower particle separation to 0.01.
[0:53] Maybe even something lower, like 0.005, so we would have around 80,000 particles.
[1:04] Next, let's create a group.
[1:07] Set it to points, call it density, and then should be bound in box.
[1:13] I would like to shift mine to center, so 0.5 in center, white axis.
[1:20] And let's set it up a bit, in case we will change our box size later.
[1:25] Next, we would need to create density and viscosity attributes.
[1:29] And there are several ways to do that.
[1:31] First one, let's create point-wap, run it over density group.
[1:34] If we jump inside, we can create bind expert node.
[1:37] In the name field, type in density.
[1:40] Let's copy it and type in viscosity.
[1:43] If we middle mouse click and promote parameter, we will be able to reach those parameters outside of WAPnet.
[1:50] But I forgot to label mine, so let's do this real quick.
[1:53] Let's copy density and paste it into label.
[1:56] And let's do the same for viscosity.
[2:00] So now that we have them nicely labeled, we can control density and viscosity through point-wap.
[2:05] But there is an easier way to do that through attribute wrangle, so let's create one.
[2:10] Run over density group and let's write a simple script.
[2:14] So f at density equals channel float density.
[2:23] And let's do the same for viscosity.
[2:25] So f at viscosity equals channel float viscosity.
[2:30] You could also use attribute create node, but I prefer wrangle.
[2:35] Let's click icon in the right corner and set density to 10.
[2:38] So we have the same setup as we did with point-wap.
[2:41] You could use either one. They basically do the same thing.
[2:44] Next, let's create null, call it flip and connect wrangle to it.
[2:50] That's gonna be our source.
[2:52] After that, we would need dot network, so let's create one and jump right into it.
[2:57] For that, I have my second network view.
[2:59] And by the way, to quickly jump between context, you can hold N and choose whichever context you want.
[3:05] So let's type wringed to the dot net.
[3:07] In here, we would need flip object and flip solver.
[3:10] Let's quickly create them and wire them to an output.
[3:13] As you can see, it looks nothing like our source points, but that's fixable.
[3:17] All we need to do is go into flip object and change input back to particle field and drop our null into subpath.
[3:24] Next, what I would like to do is change our preview type from spheres to actually particles.
[3:29] So let's do that real quick.
[3:31] Another problem we have is our collision box doesn't match with the box we created earlier.
[3:36] But that's an easy fix as well.
[3:38] All we need to do is go into the flip solver and copy the size from the box we had earlier.
[3:43] If we use relative reference, they will stay always connected to one another.
[3:47] We can do the same for the box center.
[3:51] Now our collision will match to the box we have in our sub level.
[3:55] Let's visualize our density attribute.
[3:58] Ctrl middle mouse, click on the null and toggle density.
[4:03] Now we can see density attribute visualized, so 0 and 10 in our case.
[4:10] We still have a few things to do in the dot network.
[4:14] First, let's create gravity node and wire it up.
[4:20] In flip object, what we have to do is change particle separation to the one we had in the points from volume.
[4:26] So copy relative reference and paste it in there.
[4:30] As you can see, now they are the same.
[4:34] What we need to do next is click close boundaries, so our simulation doesn't go beyond those.
[4:40] I would say that now is a good time to do our first simulation and see what will come out of it.
[4:45] So let's save a scene and click play.
[4:48] There is definitely something wrong with the simulation, so let's stop it.
[4:52] And first, I would like to change velocity type to swirly and I forgot to enable density and viscosity attributes.
[5:00] So let's do that real quick.
[5:02] And while we are here, let's see what else I might be forgetting.
[5:06] We could enable receiving, but that's not necessary for the simulation.
[5:10] What I would like to do is enable id attribute because that will come in handy later.
[5:15] And now it looks good so far, so let's save a scene and click play.
[5:20] We definitely see nice swirls in there, but they are too fast for my liking.
[5:25] We have a couple of ways for fixing that.
[5:30] What I would like to do is go into the dot network and change time scale to 0.2, let's say.
[5:36] Now they are nice and slow, that's what I was looking for.
[5:41] We do have nice swirls, but we can make them even better.
[5:47] First, let's scale up the box so we would not be able to see the edges of our simulation later.
[5:54] And run it again.
[6:02] Yeah, that's still good.
[6:05] It would be nice to have noise, not just flat density, so let's dive into point-fab and create anti-aliase noise.
[6:14] We can visualize this noise if we plug it into the color and disable our density preview.
[6:22] This noise goes from minus 0.3 to 0.3, so let's wire up the fit and dive in those numbers.
[6:32] We would also need a ramp, so let's quickly do that.
[6:36] I would like to color my ramp noise and change the type to spline ramp.
[6:42] We could plug it directly into the density.
[6:45] Right-click on the noise, create input parameters.
[6:48] Now we have control over our noise outside of point-fab.
[6:51] Let's enable density visualization again.
[6:54] As you can see, it's all black, but that's because ramp is at 0.
[6:58] I'll quickly dial in the frequency of the noise.
[7:01] Something like that should work fine.
[7:03] I would like to lower roughness as well.
[7:05] Now we can wire up the point-fab instead of running into the fit null and run the simulation again.
[7:11] Nothing is happening, that's because our density is at 1 and it was at 10.
[7:15] Let's maybe crack it up to 15.
[7:19] Now we almost can see the noise in the density, but to better see it, let's go into visualization and change the maximum to 15.
[7:28] Now we can see much more details in there.
[7:31] Let's let it run and see how many usable frames we can get out of it.
[7:36] There are definitely nice patterns in there, but at some point it just becomes too noisy.
[7:42] So I think around frame 200, that's gonna be the end of our simulation.
[7:47] Let's end read time and change the mode to by frame.
[7:51] We would have to do some little tweaks here.
[7:54] That should be good.
[7:56] Now we can get to animation.
[7:58] So let's go to the first frame and set keyframe to 1 and go to the last frame and set keyframe to 200.
[8:08] We could also increase cache memory size, so more of our simulation is fitted into the RAM.
[8:14] Let's wait a bit and see how our last frame looks like.
[8:19] Honestly, not so bad.
[8:22] I think I could decrease point size in the viewport, so it would be easier to see details in there.
[8:29] Obviously, our first frame is frame 1 and I would like to change that.
[8:34] Maybe something around 120 would look closer to what I want.
[8:37] Let's see how the speed looks.
[8:40] Not bad, but we can see some jitter in there.
[8:43] Luckily, that's easy fixable, we just need to change interpolation to subdivision.
[8:48] Now that looks smoother.
[8:50] I would like to play with start and end frame a bit, maybe come up with some nicer values.
[8:55] I think starting at frame 100 looks good.
[8:58] Maybe we will change the last frame as well.
[9:01] Let's try something like 250.
[9:04] That's a bit too much, 220.
[9:09] I think 200 was good.
[9:11] Now we are close to caching our simulation, but first let's see what attributes we have.
[9:17] And I see that we don't need all of them, so let's add attribute delete.
[9:21] Click delete non-selected and select density and ID.
[9:28] Now that looks much cleaner and we will save space on the drive.
[9:33] Let's add file cache and we will be caching to the cache folder.
[9:39] Let's call our simulation flip scene 01.
[9:43] Maybe flip scene 02, because I already have 01 in that folder.
[9:51] The rest of the fields looks good.
[9:54] And I think that we are ready to save to the disk.
[10:03] Now that it is done, we can see how it looks like.
[10:07] Nice details in there.
[10:10] But I think we might have a little bit too many particles, but anyway, let's see if that's going to be a problem later.
[10:15] Let's add attribute randomize and randomize color.
[10:19] To see color, we need to disable density visualization.
[10:22] Important thing is to use id attribute as a seed.
[10:26] Right, after that, let's add another attribute randomize and randomize pscale.
[10:31] That's a float attribute.
[10:33] We use id at a seed again and use custom ramp.
[10:36] The minimum is set to 0.01 and maximum is set to the same for now.
[10:41] And let's preview disks so we would be able to assess their size.
[10:45] Now we could adjust minimum and maximum values more comfortably.
[10:49] That looks good for now, but we will come back to that later.
[10:53] It's always a good idea to start rendering as soon as possible, but first we would need to make some little tweaks.
[10:59] Let's add transform and lay our simulation flat.
[11:03] And also bring back density visualization.
[11:08] Now let's make some more room.
[11:11] And I would like to add some noise, so let's drop mountains up.
[11:17] As you can see, nothing happens, not because we need to click off noise along vector.
[11:22] Now that's closer to what I want.
[11:24] Let's maybe drop down roughness.
[11:27] And play with the amplitude and element size.
[11:30] Right now noise goes into all directions.
[11:33] I would like it to go only into white axis.
[11:36] And just a little bit more tweaks and I think we will be good to go.
[11:39] Let's set amplitude to 0.2 and element size to 0.2 as well.
[11:47] Maybe element size a bit bigger and amplitude a bit smaller.
[11:52] That looks closer to what I want.
[11:54] Now I would like to displace our density attribute, so let's drop point one.
[11:59] But actually before we do that, we should add attribute remap
[12:04] and remap our density attribute to itself.
[12:08] We should set input max to 15, because if you remember density goes from 0 to 15.
[12:14] So if we do that, our new density goes from 0 to 1 and we can adjust our visualization accordingly.
[12:21] Now it would be much easier to work with, so let's jump into point one and add bind node.
[12:27] Into the name field, let's type in density.
[12:30] I would want to split position into its components, so let's add vector to float and float to vector.
[12:36] If we connect x to y, we can add a new value to it.
[12:40] So let's add vector to float and float to vector.
[12:43] If we connect x to x, y to y and z to z and wire all of that to the position, nothing changes.
[12:49] That's because we don't do anything.
[12:51] Let's add add node.
[12:53] But before we can wire any density into that node, I would like to get a ramp.
[12:59] That ramp should be scalar and let's call it ramp density.
[13:03] The same goes in the label.
[13:05] Now we can wire up that ramp into the add node.
[13:08] As you can see, effect is quite drastic.
[13:11] We should lower our ramp to a really small value.
[13:16] Something like 0.01 should be good.
[13:20] Let's maybe clamp it on the zero as well.
[13:28] Something like that looks good to me.
[13:31] And finally, let's add null and call it out wins.
[13:36] Now we are ready to start rendering.
[13:38] Let's copy our null, create geo container, call it or ins, render and drop inside.
[13:45] In here, we would need object merge and paste our null into the object field.
[13:50] Let's organize our network just a bit.
[13:52] I like to color my render nodes into green.
[13:55] To render particles in Redshift, we should take render objects as particles.
[14:00] And now let's split screen so we can add Redshift render view.
[14:07] We don't have any camera to render, so let's create one, call it cam 01.
[14:14] And let's look through it.
[14:17] I would like to set resolution to 180 to 1920.
[14:21] And let's maybe try and find some nice angle for our camera to look through.
[14:26] I would like to change focal length to something like 150, that should be good.
[14:32] Let's also increase point size for our particles, so it would be easier to see them.
[14:38] And let's maybe jump to frame 150, so we are right in the middle of our simulation.
[14:44] And finally, to start rendering, we would need lights.
[14:47] So let's add dome light.
[14:49] We could leave it white for now, but I have an editor I pack that I really like to start any look development with.
[14:56] So let's maybe load up one of those HDR eyes.
[15:02] Number 13 is my favorite.
[15:08] We don't have Rob network nodes, so let's create one.
[15:14] Let's call it cam 01 and check that the camera matches.
[15:18] It does.
[15:20] Now we can start rendering.
[15:25] It doesn't look like much for now, but it never does at the start.
[15:29] So I will see you in the second part, where we will start working on the look development in Houdini and Breadshift.
[15:48] Thanks for watching.



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
