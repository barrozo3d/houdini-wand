---
title: Vex quick tips | Overhang look with channel ramps
source: YouTube
url: https://www.youtube.com/watch?v=SHAgvzji9vM
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/
frame_count: 0
frame_status: pending-selection
---

# Vex quick tips | Overhang look with channel ramps

**Source:** [YouTube](https://www.youtube.com/watch?v=SHAgvzji9vM)
**Author:** cgside
**Duration:** 9m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vex-quick-tips-overhang-look-with-channel-ramps <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this video I wanted to show you how you can create this overhang using ramps, which
[0:07] is not as straightforward as it might look because by default you can't do the overhangs
[0:13] in channel ramps, but with a few tricks we can get this look.
[0:17] So let's get started.
[0:20] So we will start from scratch.
[0:22] So let's create a Geo container in a new scene and I'm going to start with a line.
[0:28] I don't think I change anything in here and then we can add a resample to get the
[0:32] curve view.
[0:34] So let's do a resample.
[0:35] In this case I'm going to subdivide it quite a bit, so point all to and I'm going to output
[0:42] the curve view.
[0:44] So let's see we have quite a few points because we will need it to displace it properly
[0:48] and we have the curve view, which is available from 0 to 1 along the curve.
[0:54] So now we will first displace it to have the leaf contour.
[0:59] So for that I'm going to create a wrangle and do a simple displace along the normal.
[1:03] So to make this easy we can create the normals along the x.
[1:10] So back to normal it will be 0 to 1 0 0 so along x.
[1:17] And then we can create a ramp to displace it.
[1:19] So I'm going to call it leave ramp and it will be equal to a C-d ramp.
[1:25] I'm going to call it leave and I'm going to use the curve view to displace it.
[1:29] So curve view.
[1:32] And now we can just displace it along the normals.
[1:37] We have done this plenty of times before and we can multiply it by the leaf ramp.
[1:43] And in the end we can have just another multiplier to control the effect.
[1:48] So I'm going to call it leave this.
[1:52] Let's see how that looks.
[1:53] So leave ramp lower case.
[1:57] So let's create this and increase the displacement as you can see is displacing along the x.
[2:02] This case I'm going to set it to 5.5 and I'm going to pick your busier.
[2:09] Because in this case I can just have a value like so I'm going to put this one down and
[2:19] just displace it in here.
[2:22] So something along those lines we'll do.
[2:26] Let me just check.
[2:29] So around 0.7 something.
[2:31] So just to create the leaf look and I'm going to make sure to drag this one to the end.
[2:36] So something like that if we mirror this we will have the leaf shape and you can play
[2:42] with it to have more or less and play with the displacement amount.
[2:46] This case I think I'm going to yeah something like that will do.
[2:50] So now we want to create that over and look.
[2:53] But before that let's create the normals because we will need them.
[2:57] So already on the long curve and in this case we want we don't want the normals along
[3:03] the tangents we actually want them along the x axis.
[3:07] So this we want this normal so we can rotate them and create that over and look.
[3:14] So now let's create another angle and we still have that curve view that we will need
[3:21] to displace along the attributes and we have the normal.
[3:27] Let's see what we will do.
[3:30] So first of all I'm going to create a float variable called you which will be equal to
[3:35] curve view because we will manipulate it and instead of always typing curve view we can
[3:39] just use a variable it will be easier.
[3:43] Then before we create the overang let's just create let's just displace the normals.
[3:53] So let's do v at n it will be multiplied by a Shannon ramp and I'm going to call it
[3:59] this and along you and then I'm going to displace it.
[4:06] So just like we have done before and I'm going to multiply it by a displacement amount.
[4:13] This per mount.
[4:16] Let's see how that looks so we can create a displacement amount and now in the displacement
[4:22] we can do the following we can take the last value we can create here a new value and
[4:28] drag the last value down and we create this overang look.
[4:34] And now we can repeat the curve view so we can just say we can create the repeating pattern
[4:42] just by multiplying the curve view by a Shannon amount so I'm going to call it perhaps
[4:53] if we do that and let's say 20 and then we need to modular so we can repeat so on the
[5:02] low by 1.0 so we can wrap around.
[5:05] So as you can see it's creating the effect and we can control the displacement amount but
[5:09] as you can see it's not really creating the overang look because to do that we actually
[5:14] need to rotate the normals.
[5:16] So let's do that.
[5:17] Let's create first an angle so a variable called angle and it will be a Shannon ramp.
[5:25] Let's call it angle ramp and it will be along we'll manipulate the U value.
[5:36] Then we want to rotate so far that I'm going to create a quaternion so vector 4 but it
[5:42] will be equal to a quaternion and we will rotate by the angle amount and along in this
[5:48] case along the z axis so set 0 0 1.
[5:55] And let's see all that loops and next we need to actually rotate the normals so we will
[6:02] say v at n it will be equal to q rotate q rotate and we will rotate the quaternion along
[6:12] the normals.
[6:15] So let's see how that looks and if we create the values as you can see it's already
[6:20] creating that look so in this case we want to play with this ramp and as you can see
[6:26] it's creating that look but I still want to tweak it so for that I'm going to create
[6:36] another ramp I believe.
[6:39] We need to create here another ramp for the angle so we can manipulate it along the U
[6:44] attribute.
[6:45] So let's do angle times equals C-A-d ramp and we will say angle, note along the in this
[6:56] case along the curve view not the U because the U is already being repeated.
[7:03] So now if we adjust properly the ramps so the displacement is fine and in the angle ramp
[7:12] we can manipulate it a bit so let's do something like this and for the angle multiplier we
[7:20] can start I and reduce it a bit in here and as you can see it's creating that over-angle
[7:27] look and if we change the displacement about we have something like this.
[7:33] And to finish it off we can actually use a power function in here to create a more smooth
[7:41] look along the U. So if we do U equals to power function of U and let's create a channel
[7:50] float called U power and let's actually create that and let's set it to 1.5 so 1.5.
[8:03] As you can see we can manipulate in here where it starts the follow-up effect let's say.
[8:11] So in this case I set it to 1.5 and you can always manipulate here how it ends in this case
[8:18] I'm gonna set it like this so I can repeat it easily so I can mirror it and it has this look.
[8:25] So that's basically it. I hope you got something out of this it was something I wanted to do for a
[8:33] while but I didn't know how to so now you can you welcome know how to do it and hopefully it will
[8:40] be helpful in your future projects and we can manipulate here the ramp and create in here let's say
[8:48] B spline and we can create another different look and you can always increase in here
[9:00] and create this more rounded look let's say. So you can play with it and yeah that was basically
[9:08] it you can also change the repetitions if you want less let's say 15 and you have this over and
[9:15] look thank you for watching if you want you can grab the file on my patreon alongside with
[9:20] our words of exclusive tutorials and also some some courses that you can find in there. See you
[9:26] next time thank you.



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
