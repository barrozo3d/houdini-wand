---
title: Unfolding curves with vex
source: YouTube
url: https://www.youtube.com/watch?v=hAD4u2oHFo0
author: cgside
ingested: 2026-07-27
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unfolding-curves-with-vex/
frame_count: 0
frame_status: pending-selection
---

# Unfolding curves with vex

**Source:** [YouTube](https://www.youtube.com/watch?v=hAD4u2oHFo0)
**Author:** cgside
**Duration:** 12m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unfolding-curves-with-vex <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I'm gonna show you step by step how you can create these unfolding effects that you saw probably on the Marmalade YouTube video from the SideFX channel
[0:13] And I always wanted to create this effect but I wasn't sure where to start so I was guided with some tips from Swalsh on the CGWiki Discord and I ended up with this effect
[0:24] I actually did this last year but it wasn't very good and I had no other resource so I had to dig a bit deeper and in the last few hours I came up with this which I think is an elegant solution
[0:38] So yeah, without further ado let's get into it!
[0:41] So let's start with a simple example. We have this curve, just align along the X and re-sample to have quite a few points
[0:49] Then we will need a value along the curve like CarView from 0 to 1 so let's do that, let's do it in BEX, we could have used a re-sample but we can also use vertexCurveParam, 0, I, V, T, X, none
[1:03] And let's assign it to an attribute just to visualize it and we can see that's just CarView and you can see it starts from 0 and goes to 1
[1:15] That's simple, 0 and 1, we don't need that visualizer anymore
[1:19] Now what we need is to define a point along the curve where we will blend to the straight up so for that we will create a parameter called Offset
[1:31] And now we just have a float value that is defining the transition point but we also need a world position on the curve
[1:42] So for that let's do this, Vector and Pause it will be equal so we will sample in the current primitive, in the current geometry the point position of our prime
[1:56] Using the coordinates so Offset and we can pass 0.0 and 0.0, this is a vector so it's always a good idea to pass as a vector
[2:05] And if I add a point now, 0 and Pause, you can see the point in there hopefully and we are just getting the point position on that curve
[2:18] So if I do an attribute noise vector and I do it on P and maybe reduce the amplitude, you can see that it still follows that curve
[2:27] So we can just use a float value to define the world position, we need to sample the position
[2:33] Ok, now that we have the position where we will transition to the straight up, we can delete this
[2:41] And we will need a mask, which part of the curve is to be blended and which part of the curve will remain laid down and which part of the curve will be up
[2:53] So we create float bias and that just will be if the curve view is bigger or equal to the offset
[3:01] So we just create this mask and if I assign that to one, two groups and visualize it
[3:09] So bias, you can see, so float bias U plus equal offset, yes
[3:17] So we start at zero and we move in and we go to for example 0.8, you can see it's just the fraction of the curve that will be straight up
[3:26] So we just create a mask with this symbol operation
[3:30] Let's keep it this here and now each primitive has a perimeter
[3:35] So if we go in here into the intrinsics and we look into the measured perimeter, you can see we have one
[3:41] If we change this, we can have different perimeters, so in this case we only have one but we could have more or less
[3:47] So we need to read in the perimeter, so we can extract the remaining perimeter of the transition zone and map it or modulate it to the Y position
[3:58] That will make sense in a bit if it doesn't now, so let's define the perimeter and we can read that intrinsic with the premium intrinsic function
[4:07] And we can read in the first inputs and measured perimeter and using the premium in this case we could have used just zero because it's just a curve
[4:16] So if we assign that to an attribute, we should have one and we do as you can see in here
[4:23] Ok, now we need the section of the perimeter that is in this red part
[4:30] So for that we can just do float, post perimeter and it will be the current perimeter multiplied by the remaining part of the curve
[4:42] So 1.0 minus offset, I mean
[4:46] So that will give us, so post perimeter
[4:53] That will be equal, so if we set this to 0.4 it will be equal to 0.3
[4:57] Because this is just a 0 to 1 range so everything will match but if we do this attribute noise, you can see that will change
[5:08] So the perimeter will change and we have more than one
[5:11] Ok, so let's get rid of this
[5:14] And now it comes the most important part
[5:18] So what we will do is take the curve view and map this section of the curve, the one that is supposed to be straight up
[5:26] Map the curve view to this part of the curve so we can easily distribute it along the y because we need a growing value to position the points along the y
[5:34] And then we modulated also by the perimeter so it correctly exports the remaining perimeter, let's say
[5:41] So for that what we will do is let's define it as post u
[5:47] And that will be a fit of the curve view
[5:50] And we will start at the offset until 1 and from 0 to 1
[5:58] And let's see what that means
[6:01] Always visualize is the most important thing when doing this kind of effect
[6:06] So as you can see at that transition point in here it starts at 0 and then goes to 1
[6:11] This way we can take this ramp and modulate it along the y position
[6:16] So let's do that now
[6:18] So let's visualize the bias first
[6:21] And now we need to create the straight up position
[6:26] So for that we will start, so hopefully this will make sense
[6:30] So vector, right, B, it will be the end position
[6:35] So, end, pause
[6:39] So the end pause is here, right?
[6:42] But if we learn it now, which is our final line, well v at B, we will blend between the current position
[6:49] And then for the straight B
[6:54] And that, and we will use of course the bias as a blending factor
[6:58] And as you can see that just claims the values to there because we don't have any y position
[7:03] This is just the flat position on the curve, so we will just clamp it to that position
[7:09] So now what we can do, we can take the straight B dot y and add the post view
[7:16] So the curve view that we remapped and multiplied by the remaining perimeter
[7:21] So post far
[7:23] And now if you see, we have the effect
[7:28] So now we need to create the more complex part which is not very complex
[7:34] But we need to create a transition effect in here so it's always rounded
[7:38] You can try an attribute blur
[7:41] And blur the position and don't pin border points
[7:44] But that will, basically we will create this with vex but without changing the end point position
[7:50] Of course you can pin those points but then the points will get further away from the other points
[7:56] And I don't want that
[7:58] So let's get rid of this and create the final effect
[8:02] So we have everything almost done
[8:05] We just need to create a transition zone as I was telling you
[8:09] So for that we need to change a few things
[8:11] So basically we need to change this bias which right now is really tight as you can see
[8:16] That's just an effect you can create so that's cool on itself
[8:19] But I want to create a smooth transition
[8:22] So let's keep this for now so it doesn't error out
[8:25] But I'm gonna create a new parameter in here so I'm gonna copy this
[8:28] And create in here a parameter called radius
[8:32] Which will be like a corner radius
[8:35] Let's define that and set it to 05
[8:38] Something like this
[8:39] Now we need to pass in here the remaining part of the curve
[8:42] So let's create another variable for it
[8:44] So this will be float anchor U
[8:49] And it will be 1.0- offset
[8:51] This is just the remaining part
[8:56] The remaining part of the curve
[9:01] And then we will need to create a transition zone
[9:07] So for that we need to change things
[9:09] First a blend start
[9:12] Which will be anchor U- the radius
[9:17] And since we don't want this to go negative
[9:19] We can just use a max
[9:21] And use a 0.0 in here
[9:24] 0.0
[9:27] And close it
[9:29] So anchor U- radius
[9:31] And we make sure we don't go below 1
[9:33] Because we are subtracting
[9:35] And finally we need to create a new bias
[9:38] So the new bias will be using the smooth function
[9:45] And basically anything less than blend start
[9:52] Will return 0
[9:54] Everything above anchor U will return 1
[9:59] And in between we will interpolate the values in a smooth transition
[10:04] Like an S shape
[10:07] And we use U as the condition in here
[10:12] So now if we have a look at the bias
[10:14] So as you can see now it's changed
[10:16] And we can increase the radius or reduce
[10:18] And we have this smooth transition
[10:21] And what we can do now is
[10:25] Instead of setting in here offset
[10:27] We will use anchor U
[10:31] And we will also use anchor U in here
[10:40] So now we will just multiply it in here by the offset
[10:46] And now we will fit between blend start
[10:52] And 1.0
[10:54] And as you can see we have our rounded effect
[10:56] And if we offset as you can see
[10:59] We get the correct result
[11:01] So we can increase the radius
[11:04] And if we get rid of the visualization
[11:06] You can see better the effect
[11:08] And that's basically it guys
[11:11] Now we can take this
[11:13] And map it to another curve
[11:16] For example this one
[11:18] This one has a different perimeter
[11:20] And we can map it in here
[11:22] And look at bias
[11:26] And if we have a look
[11:29] We can start at 1 and then start in unfolding
[11:32] Just like the guys at the Marmalade did it
[11:34] But I'm not sure how they ended up doing it
[11:36] Because I didn't copy the color
[11:38] Or even understood what I saw on screen
[11:40] So I had to recreate this with some help
[11:43] And also investigating a bit in the last day
[11:47] So I hope you have enjoyed this lesson
[11:49] I will include these on the Patreon files
[11:52] If you want to have a look
[11:53] Also have hours and hours of exclusive tutorials on there
[11:56] And all the project files from my videos
[11:58] So if you enjoyed this please let me know in the comments
[12:01] And I guess I'll see you next time



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
