---
title: From sops to final render with Karma
source: YouTube
url: https://www.youtube.com/watch?v=O_oxVn-YVB0
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [solaris, lops, karma, vdb, cops, compositing, lighting, cgi-integration, procedural, advanced]
extraction_status: complete
frames_dir: tutorials/frames/from-sops-to-final-render-with-karma/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# From sops to final render with Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=O_oxVn-YVB0)
**Author:** cgside
**Duration:** 28m33s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:25] tutorials/frames/from-sops-to-final-render-with-karma/frame_000.jpg
- [3:20] tutorials/frames/from-sops-to-final-render-with-karma/frame_001.jpg
- [7:10] tutorials/frames/from-sops-to-final-render-with-karma/frame_002.jpg
- [9:10] tutorials/frames/from-sops-to-final-render-with-karma/frame_003.jpg
- [12:30] tutorials/frames/from-sops-to-final-render-with-karma/frame_004.jpg
- [16:10] tutorials/frames/from-sops-to-final-render-with-karma/frame_005.jpg
- [20:30] tutorials/frames/from-sops-to-final-render-with-karma/frame_006.jpg
- [26:00] tutorials/frames/from-sops-to-final-render-with-karma/frame_007.jpg

---

## Structured Notes

### Core Technique
A full CGI-integration pipeline for compositing a modeled truck into a real night-time background plate: building a **localized VDB fog volume** in SOPs around the headlights (since Karma's default fog box can't create light-shaft falloff on its own), bringing everything into **Solaris** with instanced spotlights matched to headlight geometry, then finishing in **COPs** with a multi-pass (shadow/reflection/AO/depth) compositing setup over the real background plate, plus a fake depth-of-field built from a custom depth pass wipe rather than Karma's native DOF.

### Summary
Starts from a pre-built scene (camera oriented to real-world EXIF data and a background plate, covered in earlier videos) with the modeled truck placed via a saved `rest` attribute + Transform. To fake a localized volumetric light-shaft in front of the headlights, the front-metal/headlight geometry is Blasted out, moved back to its pre-transform rest position (via a second `rest` extraction), given a `name`/Connectivity attribute, packed, and reduced to points via Add (keep points). A **Line + Copy to Points + Sweep** (falloff-scaled cross-section, ~8 points) builds a cone-like light-shaft proxy shape, converted via **VDB From Polygons → Fog VDB → Volume VOP**: density is masked using **Relative Point Bounding Mode** (only possible because of the earlier rest-position extraction) on the Z axis, complemented/Fit-Ranged for a forward falloff, and layered with position-driven Turbulent Noise (frequency ~2, tuned offset/reference) for a more organic light-shaft look — finally transformed back to its original placement via **Attribute Copy of the saved xform attribute + Transform by Attribute**. In Solaris, the truck, fog VDB (assigned a **Karma Cloud material**, intensity ~3), ground grid, camera (background image removed per an earlier video's technique), truck materials, and a Dome Light (HDRI) are assembled; the actual background plate image is loaded via a **Background Plate** node with Karma's render-settings **"Use Background" toggled off** so the render captures pure shadow/reflection/AO/depth passes for later compositing rather than a baked-in plate. Headlight spotlights are built the same way as the fog shape (Object Merge truck → Blast headlight geometry → rest/Connectivity/pack/Add-keep-points → orient normals to Z, aperture group set to Y → Attribute Copy the xform → Transform by Attribute) feeding a Point **Instancer** of a Rectangle light (exposure ~7, small width/height ~0.15) converted to a cone/spot shape (rotated 180° once the orientation issue was found) so headlights actually cast forward. Compositing happens in a **CopNet**: a Slap Comp block imports the (alpha-carrying) Karma render, combined **Over** a resized background-plate File node (matched resolution via a Size/Graph node) for the base composite; then separate render passes are layered in — a denoised shadow pass (RGB to Mono, used as a darkening mask via a decreased-value blend), a denoised reflection pass (added on top, order determined empirically), a **Karma Box** volume (added specifically to help the fog integrate into camera space, scaled/positioned per-camera), a denoised **AO pass** (Remap-tuned range, multiplied over the background, wiped in at a controllable angle/offset via a Wipe node driven by a Constant so AO only affects part of frame), and finally a custom **depth-of-field** built by hand: the default Depth AOV misbehaves with the fog (renamed to a second "Depth2" AOV to work around it), fed through a Wipe (angle -90°, offset-tuned) combined with the background's own depth-based blurred layer, RGB-to-Mono converted, Blurred (~0.01) to match a desired DOF falloff, and Wiped back against the sharp foreground at a tuned blend point. The shot finishes with a **Glow** pass on the car, then simple Contrast/Brightness color-correction to match the author's original reference render, and a final Karma Max View slap-comp preview combining reflections, shadows, AO, DOF blur, and light passes together (noting a known performance issue where enabling slap comp + background plate together in this Houdini version becomes very slow).

### Key Steps
1. **Localized fog shape (SOPs):** Blast the headlight/front-metal geometry from the placed truck; use a saved pre-transform `rest` attribute to move it back to its original (untransformed) position; add `name`/Connectivity, pack, and Add (keep points) to reduce to representative points.
2. **Cone/shaft proxy geometry:** build a **Line** along the light axis, **Copy to Points**, then **Sweep** (length ~2.1, 8 points, cross-section scaled down toward the tip via the falloff ramp, ~0.5 falloff value) to create a light-shaft cone shape per headlight; also build a subdivided **Grid** for later use.
3. **VDB fog conversion:** **VDB From Polygons** (small voxel size ~0.01, subdivide enabled for a cleaner result) → **Fog VDB** → **Volume VOP**.
4. **Density shaping (Volume VOP):** use **Relative Point Bounding Mode** on the Z axis (enabled specifically by the earlier rest-position extraction) via Vector to Float, multiply into density, **Complement** to flip the falloff direction (fading toward the front), and **Fit Range** to tune the falloff shape (~0.5).
5. **Organic noise detail:** feed position into a **Turbulent Noise**, Fit-Range the result (raising the low output value to control minimum density), tune frequency (~2) and offset/reference for a less uniform, more natural-looking light shaft.
6. **Transform back to placement:** **Attribute Copy** the originally-saved transform (`xform`) attribute onto the fog geometry, then **Transform by Attribute** to move the localized fog shape back into its correct final position in the scene; output via a named Null (`out_light`).
7. **Solaris scene assembly:** Sop Import the truck, a ground-plane Grid, Scene Import Camera (background image removed, per an earlier referenced video), truck materials, and a Dome Light (HDRI); Sop Import the fog VDB (`out_light`), assign a **Karma Cloud material** (intensity ~3, defaults otherwise) to the whole fog volume.
8. **Background plate + AOVs:** load the real background plate via a **Background Plate** node (Import Render Vars + Import Render Products enabled); disable Karma's **"Use Background"** render setting so the render output isolates reflections/shadows/AO rather than baking the plate directly into the beauty pass; add an **Ambient Occlusion** render var and a renamed **Depth** AOV (default depth gave a "strange result," so a second depth pass named "Depth2" is used instead as a workaround).
9. **Headlight spotlights:** build point positions the same way as the fog shape (Object Merge truck → Blast headlight geo → rest → Connectivity → pack → Add keep-points), orient normals along Z (`{0,0,1}`), set the aperture/up group to Y, Attribute-Copy the xform, and Transform by Attribute to place points at the correct final headlight locations; feed into a Solaris **Point Instancer** referencing a **Rectangle Light** (exposure ~7, width/height ~0.15) converted to a **spotlight/cone shape**, rotated 180° to fix an initial backward-facing orientation bug, so the lights actually illuminate forward from the headlights.
10. **Base composite (COPs):** Slap Comp block imports the Karma render (with alpha); load the real background plate via a **File** node, match resolution with a **Size/Graph** node (loaded as RGB since the plate has no alpha); **Over**-composite the render onto the plate for the base integrated shot.
11. **Shadow/reflection passes:** extract the render's shadow AOV, **Denoise**, convert **RGB to Mono**, use as a darkening mask (value decreased, tunable "shadow density") multiplied/blended over the composite; separately extract and denoise the **reflection** pass and **Add** it on top (order determined by visual testing, not a strict rule).
12. **Karma Box for fog integration:** add a **Karma Box** volume specifically to help the localized fog visually integrate into camera space, scaled/positioned to fit the camera frustum, with reduced density (~0.1x) for subtlety.
13. **Ambient occlusion integration:** denoise the AO pass, **Remap** to control its range/strength, **Multiply** over the composite (careful — naive multiply also darkens/removes background, so a **Wipe** node driven by a **Constant** (angle ~90°, tunable offset) restricts the AO's influence to only the intended region of frame.
14. **Depth of field (manual, not Karma-native):** since the default Depth AOV misbehaves once fog is introduced, use the renamed second depth pass; **Wipe** (angle -90°, offset-tuned) blends it with the background plate's own depth-based blur layer; convert to **Mono**, **Blur** (~0.01) to set the desired defocus falloff amount, then Wipe back against the sharp foreground with a tuned blend threshold so foreground (truck) stays sharp while background falls off believably.
15. **Finishing:** add a **Glow** pass specifically on the car for a bit of bloom appeal; apply simple **Contrast**/brightness color-correction (no extensive color-grading network) to match a previously-created reference render; final preview via **Karma Max View** with the full Slap Comp enabled (reflections, shadows, AO, DOF blur, lights) — noting this combination is currently slow/laggy in this Houdini build when slap comp + background plate are both active simultaneously.

### Houdini Nodes / VEX / Settings
SOPs: Blast, rest attribute extraction (x2 — original + re-extracted for the fog shape), Connectivity, Name, Pack, Add (keep points), Line, Copy to Points, Sweep (falloff ramp/cross-section scale), VDB From Polygons, Fog VDB, Volume VOP (Relative Point Bounding Mode, Vector to Float, Complement, Fit Range, Turbulent Noise), Attribute Copy (xform attribute), Transform by Attribute, Null (named output). LOPs/Solaris: Sop Import, Scene Import Camera, Background Plate (Import Render Vars/Products), Karma Render Settings (Use Background toggle, Ambient Occlusion render var, custom-named Depth AOV), Dome Light, Material Library, Karma Cloud material, Light (Rectangle → spotlight/cone conversion), Point Instancer, Karma Box (camera-space fog integration volume). COPs: Slap Comp, File, Size/Graph (resolution matching), Over, RGB to Mono, Denoise, Blend/Multiply, Remap, Wipe (Constant-driven angle/offset masking), Blur, Glow, Contrast/color-correct.

### Difficulty
Advanced/Expert — combines rest-attribute-driven VDB fog authoring, Solaris light-instancing, and a substantial manual multi-pass COPs compositing pipeline (custom depth-of-field, wipe-masked AO, shadow/reflection layering) rather than relying on Karma's native DOF or fog box.

### Houdini Version
20.5 (Solaris/Karma/Copernicus workflow consistent with Houdini 20.5; references a "very recent" prior CGI-integration video from the same author).

### Tags
#solaris #lops #karma #vdb #cops #compositing #lighting #cgi-integration #procedural #advanced

---

## Related Tutorials
Author references two prior CGI-integration videos (camera orientation from EXIF data, background-image removal from Scene Import Camera) as prerequisites — cross-link once those are ingested from this batch. Also shares the Karma Cloud/VDB fog vocabulary with the environments-in-houdini-part-4/5 tutorials.
