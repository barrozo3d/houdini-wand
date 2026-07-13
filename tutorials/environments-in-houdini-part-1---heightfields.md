---
title: Environments in Houdini | Part 1 -  Heightfields
source: YouTube
url: https://www.youtube.com/watch?v=ER_W3w3SkGk
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/environments-in-houdini-part-1---heightfields/
frame_count: 0
frame_status: pending-selection
---

# Environments in Houdini | Part 1 -  Heightfields

**Source:** [YouTube](https://www.youtube.com/watch?v=ER_W3w3SkGk)
**Author:** cgside
**Duration:** 24m25s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py environments-in-houdini-part-1---heightfields <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction and overview [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So I thought about creating a new series here on the
[0:05] channel and maybe also on Patreon on creating an environment from start to
[0:11] finish. So this is what I got so far and I think today we can start to work on
[0:17] the battlefield then moving to the bridge and do the vegetation next. We will also
[0:22] do the plants in Odini and everything else. So yeah let's get into it. So I just


### Setting up the heightfield [0:30]
**Transcript (timestamped):**
[0:30] saved a new scene and we will start by dropping a geocontainer. So as I was
[0:35] saying today we'll focus on the battlefield. So let's create a night field and by
[0:42] default this will be too big so on the ZX is I'm gonna set it to 700. And now I
[0:49] want to display it more along the back of the night field so for that I need to
[0:54] create a mask. You can try using the night field pattern which as a rank
[1:02] preset but I find it hard to control and as a learning purpose let's also use
[1:08] the night field which will be more simple in my opinion to set up. So let me
[1:16] check in here. Yeah we just need to create a bindage part and we will export it
[1:25] to the mask which is our second night field or second volume I should say. And
[1:29] if we do let's say a constant of one and we export it we will have a mask all
[1:37] over the place but we don't want this so let's get rid of this and let's do a
[1:43] vector to float from our position and we can take the Z axis and I'll put it
[1:50] to the mask but as you can see that won't give us that gradient because we
[1:54] need to fit this mask. Right now is between minus 350 and 350 because it's
[2:02] self of the Z size so let's copy this parameter and let's do a fit range
[2:09] and we will do in here base relative references and divide this by two and do
[2:16] the same in here and divide by two and make this one negative. So and now we
[2:25] have to mask. Yeah we also need to complement it's because oops complement so
[2:36] we just want minus X one minus mask so we can invert it because I want it
[2:41] bigger on the backside and what else can we do? So I guess we can we can just do
[2:52] the I'd feel remap and see how that goes. I'd feel remap and we will use this
[3:00] mask and let's compute the range and it will be 00 and in this case let's in
[3:09] the output max let's introduce a big value so 200 and as you can see we have
[3:14] this linear fall off and I don't want that I want a more organic one so for
[3:20] that in the actual vote I'm gonna create a ramp so let's go to create a ramp
[3:26] parameter and we want a spline ramp and let's go outside let's add it to a
[3:36] linear because it was all flat and I believe in here I use the interpolation to
[3:46] be splined and started to play in here it won't be exactly the same but it will
[3:56] be similar enough so let me check how that looks and yeah I guess this is fine
[4:03] maybe drag it a bit more something along those lines and with the noises and
[4:11] everything this will be much different from this linear look or this
[4:17] smaller look so let's create a point and I also want to save this mask so I'm
[4:26] gonna use a copy layer I'd feel copy layer and this is simple we just set the
[4:31] source to mask and I believe I call it mask that will just output to this
[4:41] when you layer so we can refer back later so now we want to create a mask also


### Ground and noise displacement [4:47]
**Transcript (timestamped):**
[4:50] around in the I mean we want to create a mask in the middle of this
[4:56] I feel so it doesn't displace the edges this is optional but I'm gonna do it
[5:02] anyway so I'm gonna create a bound and also create the mask from object as
[5:12] from geometry I mean I'd feel mask from geometry and I'm gonna connect this
[5:17] and this will create the mask like that and now I just want to work on this
[5:22] bound so I need to I have a preset in here that just copies this value to the
[5:32] all the other values around Z and positive X and what this does is just
[5:40] decreases the size of the pound and creates this effect so you just copy this
[5:46] parameter and paste on positive X and negative and positive Z so that's the
[5:52] effect and now I'm gonna blur this quite a bit so something along those lines
[6:00] and the first idea that I have in mind is to create some displacement near the
[6:07] ground so some overall noise in the I'd field and for that I'm gonna use the
[6:17] worldly sampler F2F1 noise so I'm gonna create a night field noise and then
[6:23] we're going to distort it so I'm gonna connect the mask this way we don't affect
[6:27] those areas so that's a nice trick and I'm gonna follow some values so I can
[6:34] have a similar result but basically I'm gonna change this to F2F1 and not
[6:39] center the noise and what else can we do we can lower quite a bit the
[6:47] amplitude so to 15 and we barely see it and now we can increase this part
[6:52] decrease this element size so we get this sort of result and now we want to
[6:59] distort it and this distort will have a big impact so don't get to attach to
[7:05] this look it's always like that in night fields so we can do a night field
[7:10] distort by noise and I'm gonna change the element size to 1000 and now we can
[7:21] start to distort it and I'm gonna distort it by about 400 and I'm also going to
[7:33] load in the mask and I'm gonna change the offset to a value I have to 600 so
[7:41] something along those lines and also decrease the roughness you can decrease
[7:44] the roughness and it won't have such a big effect but the scales I'm gonna keep
[7:50] this like this so as you can see we start to have some ground displacement and
[7:56] also some elevation in here you can play with the look this is the look I found
[8:02] worked well for me so what else can we do now we will create some yields on the


### Adding back area details [8:07]
**Transcript (timestamped):**
[8:11] back part of the design field so for that I'm gonna load the mask along to
[8:19] that's a copy layer I'd feel copy layer and I'm gonna load from the mask that
[8:27] to the mask so this way we can work with this layer and I'll do an actual noise
[8:35] again and we can use this mask and instead of me playing around with values
[8:47] back and forth I'm just gonna copy some values so this is basically the intensity
[8:51] of the noise I'm gonna set it to 17 and I also have the same element size
[8:58] strangely oddly enough and I have an offset up to 100 so you can play with the
[9:03] offset to get your desired look and I also decrease the roughness a bit
[9:09] something along those lines that seems to be similar to my setup now I'm gonna
[9:19] do a night field resample to have a bit more resolution so in this case I
[9:25] feel resample and I'm gonna set it to read and this should give us a bit more
[9:36] resolution to work with as you can see the box was here increased quite a bit from
[9:42] 500,000 to 4 million and now we can do this part quite really short by noise
[9:52] and let's see we can distort this back part so I'm gonna just distort the
[10:02] yellows on the back I will have quite a bit of distortion that increase the
[10:09] element size to something like it's 100 and also decrease the roughness that's
[10:22] the trick also decreasing the roughness it will always give you a more pleasing
[10:27] result and in here as this as the mask I'm gonna use let me see as the mask I
[10:43] think I'm gonna use this warning here let's see how that looks yeah I'm gonna
[10:49] use this one because I also want to distort everything let me check no sorry I'm
[11:01] gonna distort and it's running here I'm seeing me here
[11:11] now I must are going to play with the offset in here so about 600 I'm not sure why
[11:24] I'm getting this in here maybe the mask let's see yeah this resample as something here
[11:31] but I didn't change anything particularly so when I'm doing the resample I'm
[11:44] also getting this problem on the back and this didn't happen on my initial scene so
[11:51] I'm not sure where is that coming from let me see in my mask everything is working
[12:01] which follows that I used in here let me see so about right so I guess we'll just
[12:14] ignore this and move on to the to a new distort and maybe that will go away and in this
[12:22] distort I'm gonna copy from here the mask so on this middle mask so in this case this
[12:33] distort won't help won't help to fix that particular issue on the back but let's see so on
[12:40] this new distort I'm gonna just set it you know what we can just create a default one
[12:47] you connect this in here let's see yeah that just helps us just the default settings
[12:58] just to have some distortion on the i'd field so now we're going to move on creating


### Creating the lake feature [13:06]
**Transcript (timestamped):**
[13:08] the small lake we have on the middle so for that I'm gonna create a box and right away I'm
[13:19] gonna change the uniform scale to 80 and we can control shift and click in here and let's
[13:28] let me see which short of values I use maybe a bit less on here so I'm holding shift and using the
[13:36] handles so and then I'm gonna scale it also in here holding shift and also on the y
[13:48] why THESE Too much
[14:06] you see
[14:14] So I guess this is fine.
[14:18] And now I'm going to do a band, do some tapering.
[14:24] So I'm not going to bend.
[14:26] I'm going to do a tapering.
[14:29] And let's increase it and change, change, keep pressing B.
[14:35] And I guess this is the correct way.
[14:37] I'm just going to the capture length and change this to positive and this to minus 1.
[14:44] So just to invert.
[14:46] And I also can remove the hex component.
[14:54] Or I mean, remove the y component because I don't want to display.
[14:59] In this case, remove the hex component because I don't want to display it down to y.
[15:04] So let's increase the tapering to 6.
[15:10] So quite a bit.
[15:11] And now we can do a mask from geometry, mask from geometry, mask biometric, sorry.
[15:20] And do this and remove the visualization and we have this sort of result.
[15:26] So what else can we do?
[15:28] We can distort this path.
[15:31] So let's read the nitrile, distort my noise.
[15:36] And we will distort the, in this case, we don't need to plug the mask.
[15:43] We will distort the mask instead.
[15:45] And I'm going to change the amplitude to 30.
[15:49] The element size to about 100.
[15:52] And the roughness, I can leave it at 2.3 something like that.
[15:57] So we just send it.
[15:59] And I'm going to also change the offset.
[16:02] So something along those lines.
[16:04] As you can see, when we distort, we lose the connection to the endpoints.
[16:09] So we can actually do a simple trick.
[16:12] So in a nitrile, let's create that.
[16:18] And we can, let's see, I feel, I feel, I feel, I feel, sorry, volume sample.
[16:27] And we will sample this position and this input.
[16:33] We can say primitive name and we will sample the mask, the current mask.
[16:40] And let's bind the export to the mask.
[16:45] And we should get the same result, yeah.
[16:48] And now we can do what transform matrix, this x form.
[16:53] And we can scale it along the z as you can see.
[16:57] And now we don't have that problem anymore.
[16:59] This is not strictly necessary, but just as an ice match.
[17:07] And I believe that's what I've done in there.
[17:10] But let's do first the I'd feel remap and we will worry about the next issue next.
[17:19] So let's do a I'd feel mess blur.
[17:24] And I'm gonna blur these by about 80, not quite a bit.
[17:31] And do a nitrile remap.
[17:34] So I just want to move this to the ground to make it flat.
[17:40] So I'm gonna plug the mask and I'm gonna complete range.
[17:46] And we can claim to minimum and claim to maximum.
[17:53] Copy this parameter to this one.
[17:56] And we all just set it to minus 15.
[17:58] So something along those lines.
[18:01] But I don't want this small lake to end abruptly.
[18:07] So I'm gonna leave some displacement there on the back.
[18:11] So I can then distort the lake and still have some lines to finish the path.
[18:19] Or the lake if that makes sense.
[18:22] So I'm gonna go in the spot and load.
[18:27] So find the mask that.
[18:33] And then we can just be trained just as a quick fix.
[18:42] What's the one multiply?
[18:44] See what that keeps us.
[18:47] So as you can see is the other way around.
[18:48] So let's compliment.
[18:53] And now we have some displacement on the back.
[18:58] So what we can do is to in this feed range, we can increase this to 0.7 to something.
[19:11] Along those lines and also decrease the source mix.
[19:20] So something like that.
[19:22] So we still have some values in there and this will help us along the way.


### Lake refinement and paths [19:28]
**Transcript (timestamped):**
[19:28] Alright, what else can we do?
[19:32] Let's see what's next.
[19:35] We can now create some noise on these lake parts.
[19:39] I'm gonna call it a path.
[19:41] So I'm gonna do a mask expands to win compass a bit more of this area.
[19:50] And I'm gonna expand it quite a bit.
[19:53] So 55.
[19:58] And then I'm gonna create a night field noise.
[20:02] So I'm gonna keep doing the same as fancy.
[20:06] So I filled noise.
[20:08] I'm gonna load it, load the mask.
[20:12] And I'm gonna say about 38 and all elements side of 96.
[20:20] So this is fine.
[20:23] And now we can just do another distortion.
[20:25] I filled this door by noise and load these as a mask.
[20:32] And let's see, in here I believed I want to change the lock of this path.
[20:39] So this started quite a bit.
[20:41] So I'm gonna change the amplitude to 36 and the element size to about 100.
[20:47] And also reduce the roughness.
[20:49] That's the main trick.
[20:53] So something like that.
[20:55] As you can see that helps to break the oven of the path.
[21:01] These lakesides.
[21:04] And now what we will do is to...
[21:12] I'm gonna also do a mask shrink.
[21:14] Because later I'm gonna use this mask to scatter some rocks.
[21:18] So I'm gonna do a mask shrink and shrink it.
[21:22] See, let's see, by 45.
[21:27] And I'm gonna copy layer.
[21:31] Load the layer.
[21:33] And I'm gonna change these.
[21:35] So let's say mask and the situation will be liver.
[21:41] And then we can mask clear.
[21:47] And convert light shield.
[21:52] Oops, let's remove this visualization.
[21:56] And before we finish this, let's read the match size.
[22:04] And I'm gonna scale it to fit and to end.
[22:09] I don't want those huge environments.
[22:12] And I'm gonna change this to me.
[22:14] We want those lines.
[22:16] And now we can create...


### Finalizing water and layout [22:18]
**Transcript (timestamped):**
[22:21] Agreed for our water.
[22:23] So let's create a grid and see how that pattern is going.
[22:28] And...
[22:33] In this case...
[22:40] Let's see.
[22:42] I used in here 300 times point of one.
[22:46] Because I was not sure if I was going to use...
[22:50] The original I'd feel dimensions.
[22:53] Or how would scale it right away?
[22:55] So I use this in here.
[22:57] And I also use the scale of this...
[23:01] I'd feel...
[23:04] So along the z-tor, I...
[23:06] And paste it in here.
[23:08] And also multiply it by point...
[23:11] Multiply it by point of one.
[23:13] Since we just use the scale of...
[23:16] 10 in here on this match size.
[23:19] So let's merge this.
[23:25] And in this match size, I also...
[23:28] Layed with a value along Y.
[23:30] So I reduced it to minus point 15.
[23:35] And...
[23:37] Let's also create a color.
[23:40] And change this to this...
[23:44] Just blue.
[23:46] And I'm going to create a natural looks.
[23:51] And I'm going to change this to alpha...
[23:54] ...if both to one and value to point seven.
[23:59] And yeah, this is our setup so far.
[24:03] So hopefully you enjoy this one.
[24:06] Maybe we can move this a bit up.
[24:10] Something like that.
[24:12] And this is our...
[24:14] Our eye field.
[24:15] And in the next part we will create the bridge.
[24:19] And then move on from that.
[24:21] Thank you.
[24:22] And I'll see you next time.



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
