---
title: Designer like Materials in Cops | Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=Lm5cG2XxRwU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/designer-like-materials-in-cops-houdini-205/
frame_count: 0
frame_status: pending-selection
---

# Designer like Materials in Cops | Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=Lm5cG2XxRwU)
**Author:** cgside
**Duration:** 48m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py designer-like-materials-in-cops-houdini-205 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video we'll be creating these material you
[0:06] can see here from scratch. It will be a good opportunity to learn the new
[0:12] workflows in Cops. So yeah let's get started.
[0:20] Okay let's start by dropping the geometry container and top network and we
[0:30] will create a tile pattern. We'll change the divisions to seven and I want to
[0:41] keep a rectangle and as I don't want it filled I want an gradient and the
[0:48] gradient will be a concentric ramp. So let's go with concentric and I want to
[0:59] invert it something like this and I believe that's all for now. So let's just
[1:11] create the premium material for now and connect this to the right and we get
[1:22] something like this which is not ideal so let's go to this place and change it to
[1:28] point of five and we will also change the divisions to 200. So we need to do some
[1:41] blurring and adjustments so for that I'm gonna create
[1:52] what we resize this and create a null and I'm going to blur and I'm going to
[2:07] blur just a little bit. Oh nine five oh in this case we'll blur quite a bit and
[2:19] then in the second one we'll just blur right in five and we will blame this
[2:32] fault so this one goes to the background, this to the foreground and we will
[2:43] connect this one to the mask.
[2:57] Let me check something. So point of all nine five this one is incorrect so point of all
[3:10] nine five and point of five so we get something like this. Now this is better
[3:19] looking more like an inflated look and let's continue with our pattern so now we
[3:34] will create the folds in between these corners so for that I'm going to create
[3:47] I'm gonna use this ID in here and also the UVs so let's create a UV transform and
[4:06] connect the UV and the seed and the ID to the seeds and I'm gonna change this
[4:16] randomized rotation so 180 maybe change the seed and let's do a transform since
[4:38] we want them in the corners we will just move them by one and one so they see
[4:51] to the right of the corner and create a ramp and we will change these to
[5:07] radio and just create a pattern in here I'm gonna try to mimic what I've done so
[5:20] just going up and down and maybe reduce this
[5:37] so something like this can work and from here let me see and as you can see this is fully
[6:06] randomized otherwise I would get all the same pattern so that's all right now I'm
[6:16] gonna blur this and I'm gonna blur by a value of point of four
[6:34] white arid and create another blur and go for a value point oh oh so just slightly I'm
[6:49] gonna blend out so this one to the background and this one to the background and I will need
[7:01] a mask so from this pattern in here let's create an ID to SDF and create an SDF
[7:24] from mono SDF to mono and let's change this to outline and center and the line
[7:47] rows ci
[7:48] find a weight and then also blurry petite
[8:02] 切 it and now we repeat until
[8:13] You know I can use this as a mask
[8:20] And
[8:24] And this one the line because we have these transform in here. So control all shift
[8:31] drag
[8:32] to create a reference copy and paste it in here and now we have that pattern
[8:38] So after these blends
[8:45] We'll just create a slight distortion on it. So let's create a distort
[8:54] Connect this source and create a fractal noise
[9:00] And I'm gonna change it to UV and click to add a point of two
[9:08] and on the size of 0.3
[9:12] And I want to center it to be at 0
[9:18] And the reference to be 0 also
[9:23] And change and connect this to the direction
[9:27] And I'll change the scale
[9:30] So just a slight distortion
[9:33] and let's
[9:37] And
[9:39] From here we will blend it with our main
[9:46] Our main item
[9:48] So blend
[9:51] Background
[9:53] Background
[9:56] And I'm gonna change it to soft lights
[10:01] And maybe we're just the opacity to point for
[10:06] So something like this
[10:09] And if we save it and check out the material
[10:15] So we don't have much resolution right now
[10:20] Maybe let's see it is to 400
[10:23] And we start to see our folds forming
[10:31] And this local is slightly different
[10:36] Let's see
[10:39] Maybe we can change a bit the seed in here
[11:02] And play
[11:05] With the ramp
[11:11] Maybe we can change a bit better
[11:17] To give it one random directions
[11:22] So something like this
[11:26] Now we will create the buttons at the corners
[11:37] So for that let's create the tile pattern
[11:44] And we will connect the divisions in here
[11:51] And change this to a circle
[11:57] The size of 1.18
[12:03] And a value I'm gonna save 0.4
[12:07] And change it to distance
[12:12] And a fade distance of 0.04
[12:20] And also a row
[12:22] And call them offset to be at the corners
[12:26] That's about it
[12:35] Now I can blend it
[12:44] And I'm gonna blend it
[12:48] As maximum
[12:58] And let's check our result
[13:03] And this is how it's looking
[13:07] And this is pretty much the I-TMAP created
[13:12] And we will work on the other parts next
[13:18] So we will actually create our geometry
[13:22] So let's create the subimport
[13:26] And change the divisions to 12 by 32
[13:34] I have them squared somehow
[13:38] And let's create a YUP
[13:41] A cylinder marking
[13:44] So let's use the unwrap
[13:47] cylinder
[13:50] And there we go
[13:53] And we will divide it
[13:56] And it's a good idea to create an output node
[13:59] And I'm gonna save divided by 5
[14:03] For now
[14:05] We can increase it to 206
[14:11] And let's connect it to here
[14:15] And this is looking better
[14:19] And we will also have a main transfer
[14:25] So
[14:29] We'll create a transfer into D
[14:35] And scale it
[14:39] Rotate it 45 degrees
[14:43] And uniform scale of 0.4
[14:48] So something like this
[14:55] Maybe we have too much displacement
[14:59] Let's check
[15:01] Let's leave it like that for now
[15:07] And we can adjust it later
[15:13] Or maybe
[15:15] 1.35
[15:19] This shows better
[15:23] Alright
[15:25] So
[15:27] Let's create a null
[15:31] And say this is our height
[15:37] And change it to light blue
[15:43] So what we will create next
[15:47] So let's create some color
[15:51] So for that I'm gonna start in here
[15:57] And
[16:01] Create a monotaur gb
[16:05] And
[16:11] I'm gonna copy some values
[16:17] So
[16:23] I'm gonna use a red color
[16:27] And darker reds for the blacks
[16:35] You can copy if you want
[16:39] Just enter some random ones to be fine
[16:43] And next
[16:45] We will create some
[16:51] Some pattern
[16:53] So for that let's create a whirling noise
[17:01] And we will change the element size to 0.06
[17:07] This will be quite small
[17:11] And let's change it to an hexagonor
[17:19] From the border let's create a STF tomorrow
[17:31] And the ISO offset of 0.05
[17:39] And the background will be 1 and it will shape
[17:43] So we can't see much because of the resolution
[17:47] But we will increase it in a bit
[17:51] And let's also duplicate this setup in here
[18:01] And we will distort
[18:07] And then we will change the shape
[18:11] And then we will add a point
[18:15] And then we will add a point
[18:19] And now we will add a smaller element size to
[18:23] And the rest will be fine
[18:29] Let's change it to 2k
[18:33] Let's start to see something
[18:37] Alright
[18:41] Now
[18:45] Okay we have this
[18:49] And here
[18:51] Let's
[18:53] Save it and create a multiply
[18:57] Which is just a blend set to multiply
[19:05] And maybe you can change a bit
[19:09] The blend amount
[19:11] This will be too much
[19:15] 2
[19:19] Is it going to just
[19:21] And now we will create
[19:25] Let's just get some space in here
[19:31] And let's create a fractal
[19:35] And this will be just some overall dirt
[19:41] And we will change the amplitude to 0.7
[19:47] Change this to bundling
[19:51] And we will change the distance
[19:55] And let's multiply this
[19:59] And we will change the distance to 0.35
[20:05] And we will change the distance to 0.35
[20:19] Oops, 0.35
[20:25] Something like this
[20:35] And we will create dots
[20:41] The buttons
[20:43] Colorize the buttons
[20:47] What we can do
[20:51] From the tile pattern
[20:55] We are blending this from here
[20:59] We can create an equalize
[21:03] This is just similar to water levels
[21:07] And we can dilate it a bit
[21:13] And just about 5
[21:19] And create a mono to RGV
[21:25] And I am going to change this to a specific color I have in here
[21:35] Which is like a goldish yellow
[21:39] And
[21:51] And I am going to blend it
[21:55] I am going to blend it
[22:01] Over this color
[22:05] Let's see how it looks
[22:15] Let's change it to iPod
[22:19] I have no idea what is this blending mode
[22:23] If you guys know that
[22:25] But was the one that I tried and it worked great
[22:29] So we will also create some damage on the fabric
[22:37] And material
[22:41] So before we even blend the buttons
[22:49] We will create a tile pattern
[22:55] So let's say
[22:59] Let's do this
[23:03] And create a tile pattern
[23:07] And we will change it to tree
[23:15] Circle radius of times 65
[23:23] It will be fused
[23:29] And uniform jitter
[23:33] And let's increase this
[23:37] And 196
[23:43] And some seed volume
[23:47] And let's also change the uniform scale
[23:51] 0.55
[23:55] And
[24:03] Set this to varying
[24:07] And variation of 0.5
[24:11] And see its value
[24:15] Something like this
[24:19] And now we will create another
[24:23] Distort so we can copy from here
[24:39] But in this case
[24:43] We will change the roughness to 0.9
[24:47] And then we will do 0.123
[24:51] So this is okay
[24:57] Let me see
[25:01] So that is fine
[25:17] It's a bit different from what I have
[25:21] I'm not sure why
[25:25] Does it distort the same scale?
[25:29] Yes
[25:33] Not too fragile
[25:35] Let's change the offset to 0.7
[25:39] And
[25:45] This is looking
[25:53] Alright
[26:01] And let's change it to parlay
[26:03] That's why it was different
[26:07] So
[26:11] Now we will create some feather
[26:21] And a distance of 0.3
[26:25] And create a lens
[26:29] So get the background and adjust the foreground
[26:35] And let's change it to overlay
[26:41] Now
[26:49] We will blend this with the color
[26:53] And the way we are going to do this
[26:57] We will create a constant
[27:01] And I'm going to create a color in here
[27:05] And I'm going to create a color in here
[27:09] And let's change it to our TV
[27:17] And this is fine
[27:21] And I'm going to create a frontal noise
[27:25] And this frontal noise
[27:31] We will have a contrast of 0.4 tree
[27:35] And element size of 0.4 tree
[27:39] And
[27:43] It will be a monon
[27:47] And I'm going to multiply it over this color
[27:51] So something like this
[27:55] This is for the inner padding
[27:59] And I'm going to blend
[28:03] Before this one
[28:09] And I'm going to use this as a mask
[28:15] So something like this
[28:21] And if we change it to this
[28:25] I connect this to the color
[28:29] And of course we need to transform it to
[28:39] So let's control our shift drag
[28:45] And connect this at the end
[28:55] And we will have something like this
[29:03] So while we're here already here
[29:07] Let's create
[29:11] Let's see
[29:15] We have to equalize from here
[29:19] Let's create a transform
[29:23] And
[29:27] And now
[29:31] And create all this metal
[29:35] And darkness
[29:39] And change this to green part
[29:45] And connect this to the material
[29:49] So metalness
[29:53] This way we start to see our metal in the buttons
[30:05] All right, there's one thing more I want to do
[30:09] To the color
[30:11] She's to create some
[30:15] Shadowing
[30:17] So it looks like it has some indentation
[30:23] So I'm going to
[30:31] I'm going to organize this a bit first
[30:39] So let's change this something like this
[30:43] And from here I'm going to create a mono-twice-def
[30:51] Just to get the outline
[30:59] And a left mono
[31:05] And I'm going to change it to outline
[31:11] And just increase a little bit
[31:17] And this will be fine
[31:21] Then blur it
[31:31] And in this case I want to re-emperque this
[31:37] And I'm going to blur it
[31:45] By this is fine
[31:51] And multiply it
[31:55] And multiply it before this one
[32:01] So blend it to multiply
[32:05] And let's see how this looks
[32:09] Something like this maybe it is a bit too much
[32:13] So we can change the blending to point it
[32:19] Let's see if we can see how it looks
[32:25] So now we will create some normal mapping
[32:33] And we can see the folds are working pretty well in here
[32:39] It's a very convincing effect
[32:45] All right, let's create
[32:49] What else do we need to do
[32:53] We can create the roughness and the normal
[33:01] So far the normal
[33:11] I'm going to first come in here
[33:17] This will be our main normal map
[33:21] Create a normal
[33:29] And we can create in here an item normal
[33:43] And we will have an upscale of points
[33:49] 0.5
[33:53] So quite small as you can see
[33:57] And let's create an all
[34:01] To this normal
[34:05] And upscale
[34:09] And let's connect this to the normal
[34:19] And we start to see something
[34:23] Maybe we can change the intensity of point 3
[34:33] So I just want to see how it looks
[34:37] In the end we will probably increase the resolution
[34:43] It will be better
[34:47] So this is our main normal
[34:53] But we will need a little bit more detail
[34:59] So first thing we are going to do
[35:07] This graph is fractal noise from here
[35:13] And create another item normal
[35:29] And in this case we will have it this point 0.1
[35:37] And
[35:41] And
[35:45] And we will also create a nice normal front
[35:53] From here
[36:05] And in this case
[36:09] I want to invert it
[36:13] So minus point 0.8
[36:17] So it goes like this
[36:27] And
[36:31] So we have this one
[36:35] Let's change this
[36:39] And we will change this
[36:45] This is probably not the right way to blend normal maps
[36:49] But I am going to change it to overlay
[37:01] And use as a mask
[37:05] Deezing here
[37:09] Oops
[37:13] Not really
[37:17] So we have this one
[37:21] And this should be working
[37:33] So is a mask emitting this one
[37:37] Oh maybe I need to use
[37:43] Now this is correct
[37:51] Okay and this is a foreground
[37:55] And this is background
[37:59] That's how it was in black
[38:03] And we can finally
[38:09] Blend it in here
[38:15] Change this to overlay
[38:23] And
[38:27] And
[38:31] And
[38:35] And
[38:39] And in this case
[38:41] Just set it to blend
[38:45] And use this as a mask
[38:49] And we will start this one
[38:57] So something like this
[39:03] Now we will also have to
[39:07] Betten's
[39:11] Create a constant
[39:15] I do normal
[39:25] Let's use this
[39:27] Just one
[39:31] And
[39:39] Let's blend
[39:45] And we will use as a mask
[39:49] Probably the Mattowness
[39:53] Where is that
[39:57] So we can connect this
[40:01] This is looking like spaghetti now
[40:05] But basically
[40:09] In the buttons we have no normal maps
[40:13] That's what I want
[40:17] Let's save and check the final result
[40:25] I am recording that's why it's a bit slow
[40:31] Now it's better
[40:35] So wait a minute
[40:39] This is not
[40:43] Building the final
[40:45] Sometimes you have to connect
[40:47] And disconnect
[40:49] At least that's my experience
[40:53] Or maybe
[40:57] Just
[40:59] Let's just increase the resolution
[41:07] Okay now that I see the problem is in here
[41:11] And the transform
[41:15] So let's decrease again to 2k
[41:19] So
[41:23] And
[41:27] And normal
[41:31] We need to apply the same transform
[41:37] I believe that's it
[41:43] Let's check
[41:51] Yeah that was it
[41:55] So
[41:59] Unfortunately we are not able to see the details on the fabric
[42:11] On this part in here
[42:17] And we're getting normal in the buttons
[42:21] Which is not
[42:23] Let's check the result
[42:27] And
[42:31] Oh I see why
[42:35] So
[42:39] Where is that coming from?
[42:43] Let's connect it to here
[42:47] It's not that
[42:51] So
[42:55] Oh it's not this one
[42:59] Is it this one
[43:03] Oh
[43:07] Oh
[43:11] It's not this one
[43:15] Is it this one
[43:19] Yeah
[43:21] So let's go follow that line
[43:25] And connect it to here
[43:29] Now it should work
[43:31] No normal mapping in the buttons
[43:35] So now the only thing left to do is to create
[43:39] Roughness map and increase the final resolution
[43:47] So to create the roughness map
[43:51] Let's start maybe
[43:55] After this one
[43:59] So we can create a new
[44:03] This is absolute spaghetti
[44:07] Let's go to
[44:11] RGB to
[44:13] More
[44:15] RGB
[44:17] More
[44:19] So
[44:25] I think this one
[44:27] And
[44:31] Here we go
[44:35] From days
[44:43] Running here
[44:47] From the buttons
[44:49] Let's create
[44:51] RGB
[45:01] And
[45:05] We will actually
[45:11] We will actually
[45:15] We want it
[45:19] We want it to be
[45:23] PredeShine
[45:27] And let's blend this
[45:31] And we will blend it
[45:37] And multiply
[45:41] And make sure
[45:49] I'm using two things
[45:53] And
[45:57] We will also need the same transform
[46:03] Maybe there's a better way to do this instead of
[46:07] Having these multiple transforms
[46:11] And we will also remap it
[46:15] And
[46:21] This is getting pretty slow
[46:23] Because I'm recording
[46:25] And I have two instances of a Dini running
[46:29] So
[46:33] Let's say this is our roughness map
[46:39] And we connect it to the roughness
[46:45] And we have something like this
[46:49] Now let's change this to 4K
[46:53] And we will be done
[46:57] Okay guys, thanks for the resolution
[47:01] Now we can start to see some more details on our mesh
[47:05] And on our material
[47:09] So I'm gonna just
[47:13] And sorry for the
[47:17] The roster and the dog I have a lot of animals
[47:21] And they make some lives in the morning
[47:25] So
[47:27] Let's just
[47:29] Since I have some
[47:31] Resolution issues on the buttons
[47:33] We can increase the depth to 6
[47:37] And let's save
[47:41] And look at our material
[47:45] And hopefully
[47:47] We will not crash
[47:49] And it didn't
[47:51] So I guess that's it guys
[47:55] I hope you have learned something new in this one
[47:59] Again, nothing groundbreaking
[48:01] This is a pretty common workflow for substance designer
[48:05] And whatnot
[48:07] Although I'm not experienced at all in substance designer
[48:11] I played with the software for about
[48:15] 10 times I don't know
[48:17] It was just really
[48:19] Because I needed something specific
[48:21] I used substance designer
[48:23] But
[48:25] I guess from now on
[48:27] I will keep working on my skills
[48:31] On procedural texturing
[48:33] And take you along with me
[48:37] So if you enjoyed this one
[48:39] Let me know in the comments
[48:41] And as always you can grab the
[48:43] File from my Patreon
[48:45] And check out also my courses in there
[48:49] Which are always nice
[48:53] And thank you for watching
[48:55] See you next time



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
