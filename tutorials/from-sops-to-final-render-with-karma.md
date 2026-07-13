---
title: From sops to final render with Karma
source: YouTube
url: https://www.youtube.com/watch?v=O_oxVn-YVB0
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/from-sops-to-final-render-with-karma/
frame_count: 0
frame_status: pending-selection
---

# From sops to final render with Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=O_oxVn-YVB0)
**Author:** cgside
**Duration:** 28m33s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py from-sops-to-final-render-with-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video we'll be looking at the bridge between
[0:05] Sobs and Solaris and then at the end we'll bring everything together to Cops and
[0:10] do some basic compositing techniques to create or recreate this shot. So hopefully
[0:15] that will be a tip for everyone. Let's get into it! So I'm going to start with


### Scene setup [0:20]
**Transcript (timestamped):**
[0:22] this initial scene where I set up the camera, the background plate and the model.
[0:27] You can recreate a similar one. I have done previously two videos on CGI
[0:33] integration so you can have a look at that, how to orient the camera and read the
[0:37] exit data and so on. It's a very recent one so you can find it easy. So in
[0:42] here I just brought my modeling, created a rest attribute and placed the
[0:47] transform to layout in the scene. So now I want to create here a localized fog
[0:54] otherwise the Karma fog box won't be really able to create the effect I'm
[0:59] after which is this fog in front of the lights. So for that I'm going to
[1:05] blast some parts of this geometry. So in here I'm gonna blast the light, the
[1:15] front metal, so light of metal and the litmus selected. So this is the one. Then
[1:21] since I have the rest in here before I did the transformation I can create
[1:25] another rest and do extra rest so it will move back to the original position
[1:32] as you can see. And now I can create the connectivity and can be called name and
[1:42] on Prims so I can simply pack it or just create an assemble notice the same
[1:48] thing but I can pack it and add two points or two frames. I can create the
[1:53] net and the lit geometry but keep points. Now I'm going to create a line which
[2:00] will be along the axis. I'm gonna copy two points, this line to the points so
[2:08] that's fine. Now I'm gonna sweep and create the geometry in this case will be
[2:14] around two. Let me see what sort of settings did I use. So in this case I chose
[2:21] in here a length of 2.1 and as for the points I also picked eight points. And
[2:31] or the sweep we need to play with the falloff. So in this case I'm gonna apply
[2:37] scale and in reduce it right here. So something like this is incorrect yeah.
[2:44] And then I'm going to increase this to like 0.5 something bit. So this will be
[2:49] our shape. Now I believe I also placed so I'm gonna decrease this a bit and I
[2:59] also created a grid in here and increased also the subdivisions to something
[3:04] like 24. So that is fine. Now I can create a VDB from this. So let's create a VDB
[3:17] from polygons. I'm gonna use a box of size of 0.01 in this case 0.01 and might
[3:28] be worth it to subdivide this. So it's subdivide C. We get a better result.
[3:33] Yeah. And now we can do a fog VDB. Yeah. And then finally we can do a volume
[3:43] bob. And for this volume bob I'm gonna take advantage of the relative
[3:53] point bounding modes. That's why I extracted the rest so I can easily now map
[4:00] the Z axis with relative point bounding modes. So now we can do a vector to
[4:06] float to extract the Z axis and we can simply multiply it over our density. So
[4:16] not the Y axis or the Z axis. And I also want to invert it so complement to make
[4:24] it fall off along the front part. And I might also introduce a feed range and
[4:33] playing here with the fall off. Let me see what so far. So about 0.5 in here. So
[4:41] that is fine. Now I also want to create some noise in this to make it more
[4:45] interesting. I'm going to connect this to the position. Eligator is fine and
[4:50] let's try to fit also this. So if it range and connect it in here now this will
[4:56] be too much. So in the feed I might increase a little bit the low value, the
[5:04] low output. So about this. And in the turbulence I'm gonna increase the frequency to
[5:12] about 2 and play with the offset. And also might increase a bit the reference.
[5:21] So something like this should work fine. We could spend more time with it but
[5:27] I'm happy with the result. So now we need to transform this back to the
[5:34] final position so we can't really apply the rest right now. So what we can do
[5:39] is do a attribute copy. And let's see where is that. So write about here. So
[5:51] oops. Let's connect it in here. And when I did this transform I outputed the
[5:59] X-Farm attribute. So I believe I can just copy it in here. And then if we do
[6:06] transform by attribute we could easily get that back. So let's see if that aligns
[6:13] and it does. And I might want to move back a bit this initial line. So it
[6:23] integrates a bit more in here. So I guess something like this will work fine. So
[6:31] yeah that's the first part done. Now let's just output in here the VDB. Let's
[6:38] create a null and I'm gonna call it out light. So yeah now let's continue in
[6:49] the next part. So now let's move this into Salari. So in this case just a
[6:55] basic lognet. I'm gonna switch in here and press tool. And in here I already have
[7:01] something set up. So basically importing the truck from Sobs. Then creating a
[7:07] ground plane which is just agreed. Scene import camera so I can have my camera in
[7:12] here. And I also edit the camera just like I did in the last video where I
[7:18] removed the background. So Scene import camera and I removed the background in
[7:24] here. The background image. I have the materials also for the truck and a dome
[7:29] light which loads in the HDRI for this specific environment. So then just set up
[7:36] the F-top and the focus distance for some depth of field but we will look at that
[7:40] a bit later. So now let's do another Sop import and bring in our fog. So let's
[7:46] fold. And I'm gonna load in here the outlight path so that should bring it
[7:57] start to see that is there. And we will also create a material for the fog. So
[8:06] let's do that which will be just a cloud material. So karma cloud material.
[8:12] Let's do that karma cloud material. And let's take a second and I'm gonna increase
[8:21] just the intensity to 3 and don't change anything else just leave it as default.
[8:25] That will be fine. Now I'm gonna out of here and I already edit the scene but I
[8:33] can do it again so I can come in here to the fog and just assign to everything
[8:40] inside. We can take a look at how this looks. So as you can see we have the fog
[8:47] working and it has some cloudy material and now would be a good time to set up
[8:54] the background plate. So let's do that. Let's go in here and I'm gonna create
[9:03] just a background plate after this can read it. Background plate and connect in
[9:11] here and make sure you import render bars and import render products. I'm gonna
[9:15] drop in the ground and the plate which I have somewhere let me have a look.
[9:25] Actually it's in the images and this is one that I resized with tops. You can
[9:33] have a look at the file on patreon and see how I did that. So that's the background
[9:37] plate. We have the grounds and we should have the fuse and glossy reflection.
[9:43] Let's have a look at that. And as you can see it's working. We have some
[9:50] glossy reflection and somewhat some shadows in there. I'm also going to do
[10:00] most of the things in compositing. So I will end up removing this background.
[10:05] We can actually do it right now with the render settings I believe and if we
[10:13] select the ground. No what we need to do is not render geometry settings. This
[10:21] is render settings and we come into karma and we set the background. Okay this
[10:29] was the end before advanced. So in the image you have in here use background we
[10:34] set it to off. And let's have a look. Now it's creating the A of this. As you
[10:41] can see the reflection, the shadows and I also set up in here an A or A or B.
[10:49] So an ambient occlusion. And I also the next render bar for the depth. So I
[10:57] just changed in here to depth and namely depth 2 because the default depth was
[11:02] giving me a strange result. So I changed this to another depth map just just
[11:08] renamed it. And we should have that also in here. So let's have a look.
[11:13] Depth 2. As you can see the depth 1. In this case is working but when we
[11:18] introduce the fog it will create a strange result. I can show you later. So what
[11:24] else we will do in here? We will start doing the... Oh we need to set up the
[11:31] lights in here first. So for that I'm going to create light. They add light I
[11:35] mean. And I'm going to change this to rectangle. And I'm going to set the
[11:42] exposure to 7 in this case and change the width and height to 0.15. Now I'm
[11:50] going to create an instacer to install the lights to this geometry. So let's
[11:55] create an instacer. Connect it in here. And we need to dive inside to create the


### Object merge [12:02]
**Transcript (timestamped):**
[12:03] points. So for that I'm just going to object merge the truck. So truck out. I'm
[12:13] going to blast that specific part. We could have copied from cops. So we use light
[12:20] from metal. And I believe we can just create a rest and extract the rest to


### Create geometry points [12:22]
**Transcript (timestamped):**
[12:29] reset it. So let's do a truck rest. Let's do again the connectivity. So notice one
[12:34] connectivity. And copy name. And it's to be on-premise and back. And back it. And
[12:45] finally we can add. Now it's geometry points and now let's read the normal
[12:56] story of the lights properly. So in this case they will be along the Z axis. So set 0, 0, 1.
[13:07] And we might need an aperture group. So let's just set it to Y. Just in case. Now we can
[13:12] attribute copy. Not to choose from magnitude. Copy the X form. So let's organize this a bit.
[13:22] And let's copy. Oops. Let's copy from here.
[13:29] The X form. And we do a transform by attribute. And this should give us the final result.
[13:41] Let's look at that. Transform by attributes. Sorry, I believe I said that again.
[13:51] So it's steps are. And all the normals are pointing. Now we can easily maybe place a
[13:59] bit if we ever need to transform this and make sure we don't attribute the normals.
[14:06] And for now I'm just going to set a small value to point a one and create an output.
[14:11] So this will be our points and we can come near and let's look at that. Of course it will


### Create spotlight [14:17]
**Transcript (timestamped):**
[14:22] run out because we need to set first input and 0 things. So now we watch these.
[14:33] And look at the render settings. It's look at our camera and do a small render.
[14:39] As you can see the light is there and it's eliminating. We cannot remove it.
[14:50] Oh and we need to transform this into a spotlight of course.
[14:55] So let's go in here to the shaping. We have the spotlight. And in this case we can choose some
[15:03] subs. Let's see how it looks from the top.
[15:12] And maybe we can increase these to weight. So it's clearly not doing what I want.
[15:21] There must be a reason. Oh I know why because we need this is oriented towards that axis.
[15:31] We need to rotate this to 108. So now you should work as you can see it's eliminating
[15:38] in the front part. So that is working. Let's make sure we don't introduce too much.
[15:45] That's seven. That's fine. But we can play with these. And as you can see it's getting more light.
[15:51] Let's keep it at seven. And yeah let's move into compositing.
[15:56] So now let's just do a 10% render and that should be fine. Let's do a cop network and bring in a


### Compositing [15:57]
**Transcript (timestamped):**
[16:07] slap-com block. That's fine as you can see it's loading. It's loading with the transparency with the alpha.
[16:13] Now let's bring in our backplate with a file. Let's see if I divot here I believe is this one.
[16:20] And we need to match the resolution. So let's do the size, graph, and the sub of land.
[16:32] In this case I can bring this as RGB as it doesn't have an alpha channel.
[16:38] And let's connect this one in here. So now the layer should have the same resolution of the render.
[16:43] So that's fine. Now we can actually combine it's lands.
[16:51] This will be our foreground and this one our background. Let me get more real estate in here.
[16:59] And let's look at the final. I need to reset this report. Okay. And now let's set it to over.
[17:08] As you can see it's creating that. We just need the shadows. And so we might not rendering the lights.
[17:18] Let me make sure I go in here. And we're render. Let me just change this to fixed and dark.
[17:31] Should bring in the lights right. That is fine. Let's look at it. No. Okay. The lights are dead.
[17:43] So now we also need to add a of these from last render. And the first thing we're going to
[17:49] extract is the old output films I believe. So all that shadows where is that? Let's create a now.
[18:02] And we will denoise because this comes out noisy even though I have a denoiser. So I don't know why.
[18:09] Let's convert it to mono. So RGB to mono.
[18:12] And now we can composite in here. So I just we adjust. Bring this as a mask.
[18:24] And just decrease the value. So something like this. Maybe you can play with shadow density in here.
[18:31] Now let's also bring in the reflection.
[18:37] And create a mouth and do the same denoising. And we can just add this.
[18:53] So now we are adding the reflections. I'm not sure which order is the correct. I'm just doing this by
[18:59] but there might be some correct order to do this. And let's have a look at all it working now.
[19:12] But before we continue this compositing it will be a good idea to introduce a karma box because
[19:18] I did that in my final render. So not this karma box. So I'm going to introduce it in here.
[19:24] And I'm going to scale it. So just make sure it is compositing scene.
[19:32] And I'll be tap.
[19:37] That is fine. Let's look at the camera. And right away I'm going to change this to have less
[19:45] density. So point all to another than that. That's fine. Let's maybe let's increase it in here.
[19:56] So let's select that and increase it in here.
[20:05] So it feels into the camera space.
[20:09] So now it's working a bit better. We're going to integrate in this.
[20:18] So let's render 10% and go again in here. Now we should have this.


### Ambient Occlusion [20:22]
**Transcript (timestamped):**
[20:26] And the next step would be to integrate the ambient occlusion. So let's have a look in here.
[20:38] So these are the shadows. I'm creating the shadow.
[20:47] So as you can see in here this is darkening everything on the back.
[20:53] So we might want to wipe it with another layer.
[20:58] In this case I'm just going to decrease this a bit. So something like this. Just set it to zero.
[21:08] That's fine. Now we will introduce the AO. So let's do another node.
[21:16] We could do again a denoise.
[21:20] And now if we multiply these over our backgrounds, so multiply.
[21:29] Let's move this one to the foreground.
[21:35] So as you can see is also removing the background.
[21:41] And for starters I want to decrease the effect.
[21:47] But still play with the range in here. So I'm going to denoise and play in here with the range.
[21:53] So with the remap.
[21:58] And I'm going to decrease in here this.
[22:10] And I'm also going to introduce a constant.
[22:13] It can be RGB and I'm going to use this as a size graph.
[22:18] And then I can just wipe in here. So why?
[22:22] A over B.
[22:26] And I can change the direction to 90.
[22:29] And maybe play with the offset in here.
[22:32] So something like that. Now if we do the multiplying,
[22:36] it's just setting over there.
[22:41] So setting that ambient position, which is always nice.
[22:46] Now what else? We also need to introduce here.


### Depth of field [22:47]
**Transcript (timestamped):**
[22:51] Some sort of depth of field.
[22:57] So I'm going to get in here and this depth.
[23:00] Create a model.
[23:03] And play, improvise it maybe.
[23:09] That's fine. And as you can see, if I use the default depth,
[23:13] I would get this. I'm not sure why.
[23:16] But I have to create an separator of view for that.
[23:18] So we also need to do no easy type of waves.
[23:23] So let's just do that.
[23:26] The noise. And I'm not even playing with the settings, just default settings.
[23:30] So in this case, I can't do noise because it's a mono layer.
[23:39] Let's try with the optics. Let's see if that works.
[23:44] So it's working now. Let's see.
[23:48] Now it's not working. The optics inizer is not working in here.
[23:55] Let's change this to Intel.
[23:58] Now it's Intel. Single-channel raster is not supported. Let's forget about that.
[24:03] And do again the y pin here.
[24:11] And in this case, we want it. How do we want this?
[24:19] In this case, I want to increase this.
[24:27] And decrease the mask.
[24:32] So yeah, in this case, we can just do minus 90.
[24:36] And play in here because this is for the defaults of the background.
[24:39] And I want to do it with that channel.
[24:42] Plus some iding of the background.
[24:45] Maybe something like this.
[24:48] So something like this will work fine.
[24:52] And now we can just do a simple blur.
[24:57] Big blur and make sure we match a similar level to the depth of fields as we set up.
[25:05] So let's connect the wipe.
[25:08] In this case, we want to convert it to mono.
[25:11] So add a bit to mono.
[25:13] And let's do a blur.
[25:15] In this case, I used a value of .01.
[25:19] So let's see in here .01.
[25:25] That's the amount of blur I use.
[25:27] And as you can see, it's not the starting as blurring as much here in the foreground.
[25:31] Maybe it's starting a bit too much.
[25:33] So let's see.
[25:35] So let's see.
[25:37] This is not blurring as much here in the foreground.
[25:39] Maybe it's starting a bit too much.
[25:43] So I can come in here.
[25:45] With this wipe.
[25:47] And increase a bit this.
[25:51] And as you can see, now we have a look at this.


### Final render [25:52]
**Transcript (timestamped):**
[25:55] And at the end, we can also do.
[25:59] So where is that in here?
[26:03] We can do a glow.
[26:07] That is looking a bit better with the glow on the car.
[26:11] Now we don't have actually many color correct notes.
[26:15] So in this case, I use a contrast.
[26:19] And I play it in here with the contrast, of course.
[26:23] But also with the lights.
[26:25] Something like this.
[26:29] And maybe play a bit more with the contrast.
[26:33] And I guess this is similar enough.
[26:37] Let me see in here.
[26:39] So I'm not going to show you this one.
[26:43] So this is my previous result.
[26:45] And this is similar enough, I guess.
[26:47] Maybe if decrease a bit the brightness of bright.
[26:59] So yeah.
[27:07] I can't really work with the highlights and whatnot.
[27:11] So we should have a color correct anyways.
[27:15] So let's do a final render of this setup.
[27:19] And we can do in here.
[27:21] CarMaxView.
[27:23] And if we enable this slap comp, we should be able to see everything together.
[27:27] And we have the reflection, we have the shadows, the ambient pollution, the blurring,
[27:33] alongside with the blurring, with the depth of field that we created in here.
[27:37] The light pads, we could probably try to...
[27:43] And this becomes really slow when we enable slap comp and background plates for some reason.
[27:48] So probably we'll be fixed in a new release.
[27:52] But for now is a bit slow.
[27:54] So I'm just going to increase this.
[27:56] Maybe now is too much.
[27:58] So let's decrease this to 7.5.
[28:06] And yeah guys, so hopefully you'll picked up a few tips.
[28:09] I tried to do this step by step.
[28:11] As always you can grab the files on my Patreon.
[28:14] I'm not going to include the track.
[28:16] But we'll include the full setup that you can follow along.
[28:21] And yeah, thank you for watching.
[28:23] And as always, a leave a comment.
[28:26] It's always nice to hear what you think.
[28:29] And thank you for watching.
[28:30] See you next time.



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
