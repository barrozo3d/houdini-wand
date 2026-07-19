---
title: Houdini 22 | How to Create Terrains in COPs | Utilize Height Fields
source: YouTube
url: https://www.youtube.com/watch?v=5v9lmJcIrIw
author: Houdini
ingested: 2026-07-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-create-terrains-in-cops-utilize-height-fields/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to Create Terrains in COPs | Utilize Height Fields

**Source:** [YouTube](https://www.youtube.com/watch?v=5v9lmJcIrIw)
**Author:** Houdini
**Duration:** 12m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-create-terrains-in-cops-utilize-height-fields <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This video is going to walk you through how to make a simple heightfield in Copernicus.
[0:08] A lot of the core concepts that we're going to look at here are going to remain from the
[0:11] original SOPs workflow, but in this case, we're going to leverage some of what Copernicus
[0:15] allows us to do with more control over individual heightfield layers as we build this up.
[0:20] So let's jump in and take a look at how to make a heightfield from scratch.
[0:24] Okay, so the first thing that we're going to do here is we're going to add a cop network
[0:28] into our scene.
[0:29] So if we hit tab here in our object level and type in cop network, you'll see that
[0:33] we have two different options.
[0:34] We have a cop network and a heightfield cop network.
[0:36] Now the cop network is going to make a default cop network inside of a geometry object and
[0:42] everything is just going to be set to its defaults.
[0:44] So in this case, we won't want to use that one.
[0:47] So we'll take that out of here and we will just say copnet and we can see here we have
[0:51] a heightfield cop network.
[0:53] And let's take a look at what that does.
[0:55] So this is going to also create a geometry for us and inside of it, we're going to have
[0:59] our heightfield cop net.
[1:00] Now this is just a standard cop network with a few things set on it.
[1:04] And so what we're going to look here is we're going to see that we've changed the default
[1:06] order for it.
[1:07] So it's just going to make sure that the values all clamp at the edge.
[1:10] And when you look at the canvas, this is kind of the most important change.
[1:14] This is where we're saying basically we want to have everything default to the zx plane.
[1:19] And we also have a uniform scale here.
[1:21] Now I'm going to bump this up just a little bit just to create it at the scale kind of
[1:26] that I wanted.
[1:27] This is going to make a two kilometer square instead of a one kilometer square.
[1:30] But based on the settings I had in the, and the properties, that was what I had found
[1:34] would was a nice size for what we were making.
[1:37] So I'm going to add that really everything else is fine the way it is.
[1:41] And we can jump inside and then we can add our heightfield here.
[1:44] And heightfield is just going to be a layer.
[1:47] We can see here this just a regular layer node.
[1:49] I'm going to zoom out.
[1:51] And what we can see here is that the type info has been set to height.
[1:54] So what that means is when we go in at height information to this grid, we're going to actually
[1:58] see this grid deform and this, this layer to form.
[2:02] So that is really the benefit of using this height layer and setting this type info to
[2:06] height.
[2:07] Other than that, it's basically just a standard layer in Copernicus and we can use it as such.
[2:13] So let's now start to add some noise to this.
[2:15] So what we're going to do is we're going to use our heightfield noise.
[2:17] So I'm just going to type in hf noise and drop this in here.
[2:22] Now we've got some heightfield noise that we can work with.
[2:24] We're going to go down here to visualize this and we can see our network here.
[2:29] So by default, this adds a pretty nice terrain for us to be able to take a look at.
[2:33] We're not really going to go in and change too much on this.
[2:35] I'm pretty happy with how this looks.
[2:37] It's got kind of a nice terrain for us overall.
[2:40] However if we wanted to take a look at some of what these, these parameters do, you can
[2:43] see here, obviously we have an amplitude control.
[2:46] We have our element size was going to change how large these features are on our terrain.
[2:50] And then we can also come in here and change things like roughness.
[2:53] We could smooth this out, change the number of octaves that are going to be in our noise
[2:56] here so we can get finer and finer details as we go up higher into the noise levels
[3:02] of octaves that we're adding into our noise.
[3:04] So this, I'm just going to leave the base terrain as it is.
[3:07] There's really no reason for me to adjust the noise here, but just keep in mind that
[3:10] this layer is getting plugged into the size reference.
[3:13] Basically what that's doing is pulling the information from this height field and, and
[3:17] now showing that in this fractal noise.
[3:20] This really isn't transferring it per se.
[3:22] It's not passing this layer through.
[3:23] It's actually kind of creating a new layer in a way because we have this dotted line
[3:26] here.
[3:27] So it's just a reference that we're using, but that is enough for us in this case.
[3:31] The next thing I'm going to add to this is some terracing.
[3:34] So I'm going to add in a, I'm going to do HF Terrace and we'll drop that down.
[3:41] And what we're going to do with this is we're going to kind of add in some of these layers
[3:45] to the terrain.
[3:46] So we've got these kind of nice little levels that we're going to kind of build in here
[3:50] almost as if, you know, this is like a deserty kind of scene that we're going to build up.
[3:54] So the first thing that we want to do here is we want to go in and maybe compute the
[3:59] range of what this height is going to be.
[4:01] So let's come in here and we can compute this and we can see, yep.
[4:03] So now that's our minimum and maximum values that we have here.
[4:06] So that's really a nice thing to be able to do.
[4:08] We can kind of see, you know, where these different levels are.
[4:11] And so I'd already gone through and kind of played with this a little bit.
[4:13] So I'm going to bring this up a little bit.
[4:15] Maybe around here, about 23, 24, somewhere in that range.
[4:19] And then we're going to come in here and we're going to bring some of these top ones down
[4:22] to about maybe 36-ish.
[4:25] So now we've got just kind of this layer here where we're getting some terracing in this.
[4:31] And so that's going to be really nice.
[4:32] We're going to use that to kind of build up some of our, you know, some of the kind of
[4:36] base kind of steps in this height field.
[4:40] So this is going to kind of be large scale terrain that we're going to work with.
[4:44] And so what we're going to do then is we're going to change some information here with
[4:47] how big these individual steps are.
[4:50] So I'm going to come down here and change the random step up to one.
[4:54] So we've got some random height in this.
[4:56] And then we can also adjust the step seed so we can get this.
[4:59] And I found that I liked number 56.
[5:02] So that gave us kind of a nice little variation here, some bigger, some smaller, things like
[5:06] that.
[5:08] And then if we come back over here, I'm just going to adjust the global seed as well.
[5:12] So something like that.
[5:13] There we go.
[5:14] And that was where I kind of liked it.
[5:15] I felt like this gave us a really nice overall terrain that we can kind of work with.
[5:20] Now that we have these kind of large features built into our terrain, the next thing we
[5:23] want to do is make this look a bit more natural.
[5:26] And really one of the best ways of doing that is with the height field of road.
[5:29] So I'm going to type in HF road and enter.
[5:33] And there we go.
[5:34] Now we have some erosion built into this.
[5:35] And you might think, well, didn't we just get rid of all of that kind of large scale
[5:39] features that we just put in in the last step?
[5:41] I'm just going to turn this off so we can see this a little bit better now.
[5:45] And if we can actually turn this terrace on and off just to see what the difference is
[5:48] here.
[5:49] And you're going to see that there's quite a few spots where we're actually getting
[5:52] some more levels and kind of flat spots and things like that in here than if we didn't
[5:57] have the terracing.
[5:58] So it's a subtle difference, but it certainly is a difference.
[6:01] So if we turn this terracing back on, you'll see that there's like these flat areas here,
[6:05] which feel a bit more natural than just having the whole thing be completely smoothed out
[6:10] by this erosion.
[6:12] And I'm not going to really do anything much with this height field of road.
[6:14] You can come in here and change things with random seeds and different things like that.
[6:17] However, I'm pretty happy with the way that this looks.
[6:20] And I thought it's a pretty nice overall detail to add into here.
[6:25] And now that we have this erosion kind of built in, what we can do is add some small
[6:28] fine details back in using the height field strata node.
[6:32] So I'm going to type that in HF strata and enter.
[6:36] And there we go.
[6:37] Now we've got our height field strata plugged in here.
[6:39] And what this is going to do is now add in some really tiny features to this height
[6:44] field so that we can have just a little bit of that kind of stepping put back in here
[6:49] without doing too much, you know, kind of large scale editing on this.
[6:53] So let's take a look at what we might want to control here.
[6:56] So first of all, we can take a look at the amplitude here.
[6:59] And this is going to obviously change how much or how little these these individual steps
[7:04] kind of stick out.
[7:05] And I'm just going to turn the amplitude up to 10.
[7:07] I kind of really want these to be very pronounced.
[7:09] So I'm going to just put it up like that.
[7:11] And that's starting to get a nice little element to it.
[7:15] And the next thing that we want to do is just adjust the element size a little bit.
[7:18] And so we can obviously have finer and finer details, or we could have larger and larger
[7:22] details.
[7:23] And so I wanted these to be a little bit larger.
[7:25] So we'll go up to maybe about the 340, 350 range, something like that.
[7:30] And now we can see that we're starting to get, you know, a pretty nice little setup here.
[7:35] And the next thing that I want to do is just adjust the strata size a little bit so that
[7:38] we're having a little bit more height in between here.
[7:40] So I'm just going to go up with this a little bit and go up to maybe around 15, something
[7:45] like that.
[7:46] So now we have the strata being applied, but it's not all of these individual ridges.
[7:52] There's kind of these larger gaps between them.
[7:54] And so now it's starting to feel a little bit more like what you would see maybe in a desert,
[7:58] you know, the desert Southwest type of environment.
[8:01] So this is going to now give us a bit of that realism back while still putting in a little
[8:05] bit of that erosion that we had from before.
[8:09] The last thing that we want to do is actually visualize this with some color on it.
[8:13] So what we're going to do is we're going to go from our height field strata here, and
[8:16] I'm just going to type in hfviz and add that in.
[8:20] And by default, you're not really going to see much change with this, because obviously
[8:24] we don't have any color plugged into this.
[8:26] And so with that in mind, we want to go in and actually add some color in here.
[8:31] And you can see that on this height field visualize, we have a few different inputs
[8:34] that allow us to color and add some masks into this height field visualization.
[8:39] And you can see the output of this is going to be geometry.
[8:42] And so what we're going to do is we can add in a node in between here that's going to
[8:46] be called mono to RGB.
[8:49] And so we're going to pull the mono to RGB in, we're going to drop that down here, and
[8:53] we're going to start wiring this in here.
[8:54] So this is going to be our mono to RGB.
[8:57] And so this is going to be bringing in our height information.
[9:00] And based on the height, we're going to color it, obviously RGB color.
[9:04] So I'm going to compute the range here just with the high and low so that this ramp is
[9:07] going to fit across the entire thing.
[9:10] So that's going to be really helpful for us.
[9:12] And so what we can do next then is take this RGB here and plug this into the color.
[9:17] And so now if we take a look at our height field visualize, you can see that this is
[9:19] now finally starting to color this.
[9:22] Obviously this black to white is not what we'd want.
[9:24] Let's come in here and take a look at some of our presets that we have.
[9:28] And I'm going to open up this little folder here because we have a bunch of nice new terrain
[9:32] options that are in here.
[9:33] And I'm going to go to the mountain and I really enjoyed this mountain 07.
[9:36] So I'm going to come in here and add this in.
[9:38] And now we're starting to get some really nice colors on this.
[9:42] And so let's just close that.
[9:44] And now we can take a look at this and kind of evaluate what's going on here.
[9:48] And it's looking pretty nice.
[9:50] So one thing that I don't really love about this method is that it perfectly maps the
[9:56] height to the color, right?
[9:57] And so as we look at it from the side, the colors are just almost too perfect.
[10:01] They go too perfectly with this.
[10:03] But since we're in Copernicus, we can do some really nice stuff here that is really simple
[10:07] to kind of tweak and adjust our height field because we can take our height field and actually
[10:12] modify it before we get to this mono RGB.
[10:14] And so what we're going to do here is we're going to come in and add an ad here and drop
[10:18] this in here.
[10:19] And so we're just layers.
[10:21] So we don't have to really worry too much about what's going on here as far as Copernicus
[10:25] goes.
[10:26] We can just literally wire in some noise here and add it into this.
[10:30] So what I'm going to do is just add in some fractal noise.
[10:33] And so this is just literally going to be the most basic noise just to throw in here and
[10:37] kind of break up this height field.
[10:38] Now you're going to see that this is going to start to look a little bit odd.
[10:42] And so let's keep the viewer here and let's change the amplitude here.
[10:46] We want to really push this a bit.
[10:47] So we're going to up this to, I don't know, 60 because that's actually going to show up
[10:51] as some actual height differences.
[10:52] And now obviously this is adjusting the look of our height, but that doesn't matter because
[10:56] it's just a map.
[10:57] Remember, this is just kind of a layer.
[10:59] We're seeing the height, but really ultimately what we want to have out of it is this color
[11:04] adjustment.
[11:05] And so what you can see here is if you turn this on and off, it's just going to change
[11:08] the way that this is actually being visualized.
[11:11] So we want to just break up this noise pattern a little bit so that it's not perfectly one
[11:15] to one.
[11:16] Just add in some noise there.
[11:17] And then we want to make this look a little bit nicer.
[11:19] The other thing that we can do is tweak the element size a little bit.
[11:21] So I don't want it to be such fine noise.
[11:24] We can come in here and we can obviously make it really, really, really fine or we can make
[11:28] it these larger scale noises.
[11:30] And so for this, I'm just going to go to 0.2.
[11:33] It's going to be slightly larger scale, but that should be just fine for us.
[11:38] And then we can come in here to our fractal, just change that over to maybe the terrain
[11:42] fractal just so that it kind of matches a little bit closer to the way that the height
[11:46] fields are going.
[11:47] And so now as we come back over here and take a look at this height field visualize, what
[11:51] we're actually going to see is that this is not going to any more line up perfectly one
[11:55] to one.
[11:56] And we're going to have a little bit of randomness in these heights.
[11:58] And you can see that some of these colors will kind of move across the terrain.
[12:03] And I'll just come down here and mute this.
[12:05] And you can see how much just that one little node really breaks that up, gives you a little
[12:09] bit of variation and makes your terrain feel a little bit more, just a little bit more
[12:16] natural.
[12:17] And so that is going to be where we end this video.
[12:20] So hopefully this gives you a great idea of how to get started working and building terrains
[12:24] in Copernicus.



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
