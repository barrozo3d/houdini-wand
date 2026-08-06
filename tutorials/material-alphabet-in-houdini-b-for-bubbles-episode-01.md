---
title: Material alphabet in Houdini: B for Bubbles | Episode 01
source: YouTube
url: https://www.youtube.com/watch?v=uYQGsriGNm4
author: Kotov Roman
ingested: 2026-08-06
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/
frame_count: 0
frame_status: pending-selection
---

# Material alphabet in Houdini: B for Bubbles | Episode 01

**Source:** [YouTube](https://www.youtube.com/watch?v=uYQGsriGNm4)
**Author:** Kotov Roman
**Duration:** 11m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py material-alphabet-in-houdini-b-for-bubbles-episode-01 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey, I'm Kotov. This is B4Bubbles, the next chapter in Material Alphabet and Houdini series.
[0:06] In this episode, we're building a liquid with bubbles inside, completely without simulation.
[0:11] Instead of relying on dynamics, we'll use procedural geometry to get a total control over the placement and movement.
[0:18] Throughout the process, we'll move back and forth between geometry and rendering as we develop the look.
[0:23] And let's get to it.
[0:25] Let's start by creating a geo-container, calling it setup and coloring it red.
[0:29] I will also change the background to the gray.
[0:32] As usual, we will need some geometry to work with. Let's drop down font node and type in B.
[0:37] Maybe I will also change the font to anything else, really.
[0:44] This one should work nicely for the bubbles setup, but we will need some thickness.
[0:48] Learning from my mistakes, I will not be using bevel node and instead jump right into VDB from Polygons.
[0:54] And before we go into simulation, it's probably a good idea to change our FPS settings.
[0:59] Bubbles should be smoother than that. Let's add VDB smooth node and crank it up a lot.
[1:05] This shape already resembles liquid. Now let's think on how we can make it appear.
[1:10] I will be using Mop's shape falloff for that.
[1:13] This falloff will drive most of the look. It will do displacement, appearance of the liquid and movement of the bubbles inside.
[1:19] Because it's just 0 to 1 gradient, it's really easy to work with inside the point valve.
[1:24] To make animation look more interesting, let's add displacement first.
[1:28] I will be using displacement along normal's node.
[1:31] To add some visual interest to it, I will also add some noise in there.
[1:39] Now let's bring in our Mop's falloff attribute.
[1:45] I will add a ramp to it to make it easier to work with.
[1:50] The configuration of the displacement along normal's node is really easy.
[1:55] Only do you plug in position into position and Mop's falloff into the mount.
[1:59] Scale will determine how much of the displacement we have.
[2:02] And because we have added ramp to the Mop's falloff, we can shame the displacement.
[2:06] Now let's add some noise to it by multiplying Mop's falloff with the noise.
[2:10] Let's see what kind of displacement we can dial in with this setup.
[2:19] Now that we have that, let's tackle in appearance of the shape.
[2:23] For that, I will be using points from volume node.
[2:26] We can do a full link copy of the node by holding down Ctrl Alt Shift and dragging that node.
[2:31] Let's do that for our Mop's shape falloff.
[2:36] You can see falloff going from 0 to 1.
[2:39] The idea is that we will multiply pscale with it.
[2:42] So when we use VDP from particles later, points with 0 pscale will just disappear.
[2:47] We can visualize that by tackling this instead of points in our viewport.
[2:53] Now we are ready to use VDP from particles.
[2:56] I've set pscale to a very small value.
[2:58] I will increase that so VDP from particles can pick it up.
[3:05] I will also make further adjustment to the displacement.
[3:09] It's time to convert VDP back to polygons, but I will add VDP smooth in between.
[3:14] That's a start, but it cuts off way too smoothly.
[3:17] I want to break it up with the noise.
[3:19] Luckily, Mop's shape falloff makes it easy to add the noise.
[3:22] Let's set it up.
[3:24] I am looking for a really smooth and fluid noise pattern.
[3:30] Hopefully you can see the vision now.
[3:33] Let's animate that falloff.
[3:35] Going from down to up.
[3:43] Now we are ready to cache that stage.
[3:45] Let's drop down File Cache Note and choose our folder.
[3:48] Now that I can see that in motion, I would like to make some small adjustments.
[3:52] First, I will increase displacement amount.
[3:54] And second, I will change the noise pattern.
[4:06] I will also check if I can find some better options in VDP smooth.
[4:24] Let's cache that iteration as well.
[4:27] I like the first one more, but it's still not what I am looking for.
[4:32] I will revert some of the changes back.
[4:43] That looks good.
[4:45] Now let's work on the bubbles inside.
[4:47] Because we already have the points inside our shape, we can use them for the bubbles.
[4:51] We have to delete most of them and leave only a few.
[4:54] I was trying to use Vax for that step, but for some reason it just didn't work.
[4:58] If you can explain me in the comments why is that, I would be really grateful.
[5:02] Let's build the same thing in point-fop instead.
[5:12] Now that threshold value determines how many points were not deleted.
[5:19] We will do a similar thing we did before.
[5:21] I will multiply pscale value with the maps falloff.
[5:31] But instead of directly specifying pscale value, we will be using random one based on point number.
[5:37] Random function gives us values from 0 to 1, so we can easily use fit function to adjust them.
[5:45] Let's display particles as disks.
[5:48] And adjust the ramp.
[5:52] It will add a ramp in between random and fit functions.
[5:56] We can control the ratio of the smaller and bigger particles.
[6:02] Let's make further adjustments to the maps falloff ramp.
[6:12] Now we see the problem that we have.
[6:15] Because point number changes every frame, our pscale value jumps as well.
[6:19] Luckily that's easy enough to fix.
[6:21] We will use timeshift frozen on the last frame.
[6:24] And a relative copy of the maps falloff.
[6:26] Now points state the same, we are just changing their size based on the maps falloff value.
[6:31] But to make it more interesting, I also would like to move them a bit, based on the same maps falloff.
[6:36] For that we will be using my favorite noise.
[6:39] If we add noise to the position value of the points, we will displace them in space.
[6:44] Basically that's what mount and sob does under the hood.
[6:47] And I could have just used that, but I decided to build it from scratch.
[6:51] We will be adding maps falloff value to the y component of the position.
[6:55] That way particles will go higher the first time they appear and then settle down.
[7:05] But I don't want them to rise with the same value, so let's add the noise.
[7:17] Now the points are static, aside from the size animation.
[7:29] We can make points move constantly with a simple time expression, put into the offset of the noise.
[7:35] As we are done with the shell, let's add a null to it.
[7:39] And most likely points are going outside of the shell.
[7:42] Let's fix that.
[7:45] The easiest way to do that is to use mask from geometry, and to scale down all the points that are outside our shell.
[7:53] Now all the points that are outside has mask value of 0.
[7:58] We will use blast to delete them.
[8:03] And I will use the second mask from geometry to scale down any points that are close to the surface.
[8:15] I am done with the bubbles. I will add a null to them.
[8:22] But to see what they are doing inside the shell, I will use an alpha.
[8:26] That's only for previewing purposes. You can skip that step entirely.
[8:32] And finally, let's add a file cache to the bubbles.
[8:45] Preview of the bubbles is a bit janked, but that's because of an alpha.
[8:50] We will preview them in a different way.
[8:53] Right now let's do the usual.
[8:55] Add geometry container for each thing we want to render, and add object merge inside.
[9:00] It also would be nice to set up a camera right now.
[9:15] I am not a big fan of the bubbles movement right now. Let's adjust the noise.
[9:31] I want to get a feel like they are moving in the same direction, but each independently.
[9:36] And let's cache that version as well.
[9:45] Right now all of them are moving at the same speed.
[9:48] I want to make them move faster the first time they appear.
[9:51] To do that, instead of directly using time function, we will multiply it with the mobs falloff.
[9:59] Let's use parameter to set our default time value.
[10:08] Now we have successfully recreated the function we had before.
[10:12] Attribute previews don't work for some reason, but near displaying particles as disks.
[10:17] I had to make sure that I have mobs falloff attribute on that stream.
[10:21] Now let's use the ramp from mobs falloff to change the speed dynamically.
[10:28] Now we have a ramp to control how fast particles are moving at any stage of the animation.
[10:32] It's getting a bit heavy. Let's add another file cache before the final one.
[10:38] We can see that it works. Now we have to configure it.
[10:57] That shouldn't be good. Let's cache it out.
[11:07] And let's do the final cache as well.
[11:14] That's it for the first episode.
[11:16] The next one pickups where we left off and pushes the setup further.
[11:20] In the meantime, you can check out the complete ember material.
[11:23] Link to material alphabet and huddy-nupilid is in the description below.
[11:27] If this helped, consider subscribing and leave a comment if you have questions.
[11:31] It helps the channel going.
[11:33] I hope this gave you a few useful ideas you can apply to your own work.
[11:37] Thanks for watching.



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
