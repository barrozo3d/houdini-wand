---
title: Building Tools in Houdini with vex and python | Flatten Loop
source: YouTube
url: https://www.youtube.com/watch?v=enW-PwgBWE4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/building-tools-in-houdini-with-vex-and-python-flatten-loop/
frame_count: 0
frame_status: pending-selection
---

# Building Tools in Houdini with vex and python | Flatten Loop

**Source:** [YouTube](https://www.youtube.com/watch?v=enW-PwgBWE4)
**Author:** cgside
**Duration:** 18m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py building-tools-in-houdini-with-vex-and-python-flatten-loop <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video we're going to build a very simple tool that will help us in our modeling
[0:06] test.
[0:07] So let me demonstrate, basically you select some points and then you can hit an opkey,
[0:15] let's say flatten X and it will average out the positions and flatten it out.
[0:20] You can also enter the tool, so let's see flatten Z and select the points and click enter.
[0:26] So this is a very basic tool but that will introduce you to the world of creating these
[0:32] interactive tools in Odini.
[0:34] So let's get into it.
[0:36] So I just saved the new scene and I'm going to create a grid and this start a bit
[0:44] the shape with a mountain.
[0:47] Let's do like this and don't start along the white, don't displace and let's set this
[0:54] to 0.5.
[0:57] So now we need to try to leverage out the positions along a specific axis and for that we're going
[1:04] to use a wrangle and first of all we need to select some points.
[1:09] So select in here, this one's for example and now we'll create an array for the positions.
[1:21] So vector of the array, of the array will be an empty array and we also need to iterate
[1:30] through the group of points.
[1:31] So for that we're going to create a group variable that will be equal to this parameter
[1:39] in here.
[1:40] So parameter group.
[1:42] So we can just say C, just group.
[1:48] Now we can expand the point group so we need to find the points in this group.
[1:55] So for that we can create an array.
[2:01] So points group and it will be equal to expand point group, expand point group incoming geometry
[2:11] and the group we just set above.
[2:15] Now we need to iterate through it and add it to the positions array.
[2:20] So we need an array of the positions so we can average them out.
[2:23] So we'll do for it and we need any to write this so it will be the point and then we will
[2:31] iterate through the points group.
[2:34] So when this now we can just say vector, pause, it will be equal to the point of the incoming
[2:44] geometry, the position and the point number will be to PT.
[2:50] So we can actually visualize this by things.
[2:55] Let's say sprint in the new line and PT.
[3:00] Let's just print out the numbers so as you can see those numbers are the same as the ones
[3:05] we have in the group above.
[3:08] So let's comment this out and we have the position now which is need to append to the
[3:13] array.
[3:14] So pause array and the relevant position.
[3:19] So that should be fine.
[3:21] Now if we print out the array.
[3:29] So let's say pause array and it's to be lowercase as you can see the positions are being
[3:37] printed out.
[3:38] Now we will average them out so vector, average will be equal to average the function, pause
[3:48] array and now we can just say in this case at p dot x it will be equal to average dot x.
[4:03] Let's see if that works and it didn't works.
[4:06] Now we just need to make this more procedural.
[4:10] So what we will do, we need to make sure we have an option to select either the x, y or
[4:19] z components.
[4:20] So for that I found an easy way, there are plenty of ways I'm sure, but I found this
[4:27] one.
[4:28] I'm going to create an axis variable and a parameter, so see a channel string and I'm
[4:34] going to call it axis and I'm going to add it and I'll add it parameter interface.
[4:41] I'm going to the axis and set this to order menu and let's go to the menu and create x
[4:49] and x.
[4:50] Oops, x.
[4:53] Let's create another one for y and another one for the z.
[4:58] So guess this is fine.
[5:01] Now we have an option to select the axis.
[5:06] So in order to feed these values in here, we can directly read the parameter.
[5:12] So what we're going to do is create an int axis index.
[5:17] It will be equal to find x, y, z in the axis parameter.
[5:27] This will output 0, 1 or 2 depending on the input we have in here.
[5:31] So we can actually print that out.
[5:34] Did I remove my print?
[5:36] Cement?
[5:37] Yes.
[5:38] So we can just do int, printf and let's percentage the new line and let's say axis index.
[5:53] Image will be 0, and 1, and 2, as you can see.
[5:58] So we can just edit here.
[6:03] So it's an index.
[6:05] So axis index.
[6:10] Exist index.
[6:11] Oh, not the dot.
[6:14] So in this case, z, we need x.
[6:18] As you can see, it's working.
[6:23] You can just say B and remove this line.
[6:27] So our tool is mostly done.
[6:29] Now we just need to create a subnet.
[6:33] And let's call it Latin demo.
[6:38] And let's edit parameter interface.
[6:40] Select all of these.
[6:42] Make it invisible.
[6:45] And let's hit click apply and go in here.
[6:49] In this group, which we need to change and this axis.
[6:54] So like we have an option.
[6:58] And but we need to to make sure we in this group.
[7:04] And we need to make sure we selecting points.
[7:10] So in this case.
[7:17] So in the group parameter, we need to instead of this code we have in here, we can say geometry
[7:22] type will be equal to all dot geometry type dot points.
[7:30] And the rest is the same.
[7:31] We can apply and accept.
[7:33] And now if we select say this points and click enter, it will work.
[7:39] And select points along the Z.
[7:42] So if we set and select again, as you can see is working.
[7:48] Now we just need to make this interactive.
[7:50] Let's do that in the next part.
[7:53] So now we will publish this HDA.
[7:56] So create digital assets.
[7:58] I'm gonna not add the version either the other name, flattened demo, create and just click
[8:05] apply and accept.
[8:07] So flattened demo, we have the HDA that we can create with the radial menu.
[8:14] That's what we're going to do.
[8:15] So let's go to edit radial menus.
[8:20] And we can go in here.
[8:22] You can see I already have one in here, but I'm gonna add another one.
[8:25] So regular menu, go on the call it left and radial demo.
[8:34] The name in this case, what did I cut?
[8:39] Let's see the apply.
[8:41] And let's see, I flattened to, I can call it flattened to, flattened to v2.
[8:49] So now we can actually go into nodes and rbj digital assets, not overj.
[8:57] So, digital assets and we have a flattened demo in here that we can invoke to place the
[9:03] node.
[9:05] But we're going to use a bit of Python to have more control over how it works.
[9:12] So for that, let's remove this and go into the utilities and create a script action.
[9:18] So let's place it here and let's call it flattened.
[9:26] And in this code, we're going to write some things.
[9:32] So first of all, we're going to make sure we have the correct path for the current nodes.
[9:38] So we can append nodes below.
[9:42] So for that, I'm gonna just import our, and let's create a node variable that will be
[9:48] equal to words of pain.
[9:52] Let's do a single quote, pain and dot, current node.
[10:03] And we can actually print it out.
[10:06] So let's do print node.
[10:09] So we can see where we're going with this.
[10:12] Let's create a node key.
[10:14] So I'm gonna, I have six, but I'm gonna set it to WF7.
[10:19] So it has a different one.
[10:21] And now we can apply and let's see, let's eat F7.
[10:28] And words is not defined.
[10:33] Let me see.
[10:35] Oops.
[10:36] War works.
[10:38] No, it should work.
[10:40] Let's see again.
[10:41] Let's do it F7.
[10:43] As you can see, it's printing out the last node or the node we selected.
[10:48] That will be important.
[10:51] So let's go over here.
[10:53] And the next thing we're going to do is save out the position.
[10:57] So pause to be equal to node dot position.
[11:02] And the next we're going to wear the current selection if we have one.
[11:08] Otherwise we enter the selection mode.
[11:10] So let's create a cell.
[11:11] It will be equal to quarts dot pain, which will be the scene viewer.
[11:17] And we can say it's a left geometry.
[11:23] So select geometry, that's correct.
[11:27] And now we can create the node itself.
[11:30] So in this case it's called a flat end demo.
[11:33] So we can do let's see.
[11:37] Let's see if that works for us.
[12:02] So F7 and it didn't create the node.
[12:14] Let me see.
[12:15] No dot turns it flat end demo.
[12:20] Let's see the name flat end underscore demo.
[12:25] So I need to restart to the end.
[12:27] So the node actually is created.
[12:33] Let me try again this.
[12:34] So let's see the set create.
[12:37] Oh, we need to select the geometry of course.
[12:40] And now it's creating the nodes.
[12:44] So let's go over here and in here.
[12:46] Radio manners.
[12:49] Now that we created the node and we have the selection taken care of.
[12:53] We're going to position the node.
[12:55] So let node dot set position.
[13:03] And we need to pass a vector to so X and Y.
[13:07] Since we're working in to the viewer, the node editor here.
[13:13] So we can do all dot vector to and it will be equal to will be the argument.
[13:23] The moment will be pass the first the X components and the Y components.
[13:31] Less one.
[13:32] Let's say let's give it a space of one.
[13:35] Let's see how that works.
[13:38] We can actually select something.
[13:41] And let's press F7 and do it as you can see is creating and giving it some space.
[13:46] So now we need to connect it.
[13:50] Let's delete this and go to radio manners.
[13:54] And let's do now.
[13:58] Let's connect the node.
[14:01] So we can just say let node dot set input.
[14:08] The input will be zero and we will connect it to the node above.
[14:13] And that will work, but we also need to set.
[14:18] The point group and the axis.
[14:20] So for that, we're going to say let node dot farm axis dot set.
[14:32] And in this case, which will be along X.
[14:36] And we also will save flat node dot farm group dot set.
[14:44] And it's to be a string.
[14:47] So we'll upcast it and set the selection.
[14:51] Let's see if that works for us.
[14:55] Let's do F7 flat and X.
[14:58] Let's select and hit hinder.
[15:00] We just need to set now the display of the node.
[15:03] The flags.
[15:04] So let's go into radio manners again.
[15:08] And we will say.
[15:10] So after setting the input, we'll say flat node dot set grant true true.
[15:20] And we will also set the display flags.
[15:23] So set.
[15:24] You set this play.
[15:28] Flat true.
[15:29] We don't need this, of course.
[15:35] And we can also set the render flight.
[15:37] So set.
[15:38] Render flight to true.
[15:44] And how this should work.
[15:46] Let's see.
[15:47] So we can actually select some points.
[15:50] F7 and this work.
[15:54] And we need to work out the other ones.
[15:56] So let's go to radio manners.
[16:00] And let's create.
[16:02] Let's copy this.
[16:04] So to utilities, let's do this will be along the Y.
[16:09] So that's an Y.
[16:13] And we just need to change one thing in here, which is this parameter in here.
[16:20] So set it to Y.
[16:21] And let's do another one.
[16:24] Let's change it to Z.
[16:27] Let's.
[16:31] Let's see if that works for us.
[16:32] Let's do now one along the Z.
[16:35] So F7, flat and Z.
[16:37] We can select these points and it's working.
[16:41] We can also select the points and off let the next.
[16:45] And seems that it's working.
[16:48] Now just as a side note, we can actually edit the.
[16:54] Let's see, edit icons.
[16:57] You can go in here and change the icon.
[17:01] Let's see, H icon.
[17:03] And you have a bunch of them or you can create your own.
[17:06] In this case, I'm going to use that one.
[17:11] And the same here.
[17:13] Let's see.
[17:16] So the flat and X.
[17:21] Let's select this point.
[17:23] And as you can see, it's working.
[17:26] So I hope you got something out of this.
[17:28] I'm going to put everything on Patreon if you want to just
[17:32] download the tool and the code.
[17:35] But anyways, I hope this was helpful.
[17:37] It was a different video than the usual.
[17:40] But it's always important to have these sort of skills
[17:43] even if they are very basic, because it
[17:47] can save you out in many situations.
[17:50] Nothing too overpowered, but it's a nice addition
[17:54] to your old in-e-knowledge.
[17:57] So let me know in the comments if you enjoyed this one.
[17:59] And other than that, thank you for watching.
[18:02] And I'll see you next time.



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
