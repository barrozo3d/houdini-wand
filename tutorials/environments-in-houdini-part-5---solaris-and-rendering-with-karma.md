---
title: Environments in Houdini | Part 5 - Solaris and rendering with Karma
source: YouTube
url: https://www.youtube.com/watch?v=h6MN80ka4Vg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/environments-in-houdini-part-5---solaris-and-rendering-with-karma/
frame_count: 0
frame_status: pending-selection
---

# Environments in Houdini | Part 5 - Solaris and rendering with Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=h6MN80ka4Vg)
**Author:** cgside
**Duration:** 74m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py environments-in-houdini-part-5---solaris-and-rendering-with-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this final part of our environment tutorial, we will move everything to
[0:07] Solaris and work on the shaders and on the lighting and hopefully we will have a
[0:12] final render at the end. So yeah let's get into it. So we will first need to
[0:18] separate these into parts, so meaning that we will have to give a name
[0:23] attribute to each piece. But before that let's go into our, if you remember we
[0:28] did the scattering of the rocks and we had this issue where the connectivity
[0:32] was generating other IDs let's say. So we don't actually need this connectivity
[0:38] because in the, when we did the rocks, we actually created a class attribute as
[0:46] you can see in here from the, in our loop. So we can use that. So if we get rid
[0:53] of this connectivity, we can actually use that, we use that class attribute as
[0:59] the seed. So you can see we should have a class attribute. And if we look at
[1:07] final result, we have to, in this case the low poly, let's enable the
[1:12] eye poly and we still have the same rocks. Next we just need to play with seed
[1:16] but let's keep it like that for now. So we will need to start to name these
[1:23] so in this first, the I'd field, we need to name it to the rain. So let's create
[1:34] the name and we will name it to the rain. So we should have only a name attribute
[1:42] that's fine. I'm going to also create here a mask which will be where we will
[1:49] scatter the grass. So for that, let's create a point for this will be really
[1:55] quick and we will take the norm, the normal and separate it so vector to float.
[2:02] And let's look at the y components on the CD and now we need to hit it so
[2:09] bit range and play with the range in here. This case I'm going to set the source
[2:15] mean to a bit higher so around 0.8.9 something like this and instead of
[2:24] outputting it to the CD, we will create a bind export and we will export it as
[2:33] mask grass. So we should have the attribute right now. Let's have a look and we do
[2:42] so this is where it's where it's welcome. So we also have the mask along Z, we
[2:49] will not need and the river that we will need. So let's keep working on our
[2:55] naming. Now we need for the river geometry and before that we will need some
[3:04] new v's. So let's read the UV texture. Let's look at the UVs and this will be
[3:11] inverted so we can set this to minus one and offset it again to the first one
[3:16] and reduce this to something like 0.4 to have the square root. I'm not going to
[3:24] use this alpha and I'm also going to name this and I believe I called it river.
[3:32] See, yeah, or in this case we can name it water. So this is the first part done.
[3:41] Let's look at the output. So we have the I'd field and the water and we don't need
[3:49] to see the UVs. So that's fine. Now in here we have the bridge I believe. Yes. So we need
[3:58] to start to name these appropriately. So in this case first of all I'm going to name
[4:07] this this bad geometry in here. Let's read the name and I'm going to call it bridge at
[4:18] and then in here this will have the same material. Not in here sorry. We need to
[4:29] actually separate these. So in here we can name these as bridge stands. And then in here
[4:51] we can do the same. Just copy this and we should have a name attribute. Let's see we
[4:59] have for the stones and for the beds. That's fine. This will go in a single output. So we
[5:06] will import these all together instead of dividing it to different sections since we have
[5:13] the name attribute. And now for these we need to name for the lines. We need to name these
[5:21] properly. So for the three measure which is the vines we can name it vines. And for these
[5:35] we can name it not vines lips or something like that or just lips. Let's find this will also go
[5:43] together. And what do we have in here? Oh we have these vines and already call it vines. So
[5:51] let's find these will also go in the same setup. And the next part will be we will actually get rid
[6:03] of this scattering. So we will not import the rocks. We will do that in a separated instance.
[6:12] So this is fine and as far as this goes we will also need that background plane.
[6:21] So let's name it the rain back. And remove these. We won't need the scattering. So
[6:31] to bring back. And I guess this will be the final output. So a good idea is to file cache this
[6:42] file cache. And let's remove the time dependent cache and the environment. The RAM cache.
[6:54] Let's say this to this. And we should have everything we need. So in this case we have more things.
[7:02] We could have cleaned that. But we have the mask rest. We have last attribute in case we need.
[7:10] We have the mask set. And we should have a different name attribute for each part. So that is fine.
[7:19] And let me see here in the leaves. Don't actually need. We don't need this texture. But we will
[7:36] replace it anyway. So let's keep it for now. So let's name this out. And let's continue on the next part.
[7:44] So we have everything ready to move into Solaris. So let's copy this and move into Solaris.
[7:53] And now let's do a sub import. I'm gonna call it this scene. And paste in here the back. So
[8:06] this should get a bit slow because we have instances. So in the primitive definition we want to
[8:12] treat the packed primitives. Not in here. So we want to treat the packed primitives.
[8:22] Let's pause this. So we want to treat it as pointy sensor. And now it should be
[8:29] wastemodern. This will actually create pointy instances for the leaves.
[8:36] And we should have the name attributes. So the breach path, the stones, the instances, the terrain,
[8:44] the terrain back. We also have four divines and water. So that's fine. Now I also created a
[8:52] camera in subs. But we can do it here. So let's just set this to your port size. Set it dark.
[9:01] And we can display the environment. Now let me see the camera that I used. We can't just
[9:11] get in here. Something.
[9:16] Now create a camera. We can roll it a bit in.
[9:23] Something like that. We can change it later. But let's keep it like that. So let's disable this.
[9:34] Now we can start to create some of the lighting. In this case I'm going to use a
[9:42] the Karma physical sky. So let's set that up. So Karma physical sky.
[9:53] And do a Karma render settings. We will change this to XPU. That's fine for now.
[10:01] And we have the camera loaded as you can see. Camera 1.
[10:06] And we can probably start to have a look at this render.
[10:12] And disable this. And let's change this. Let's go into this physical sky. And first of all
[10:22] going to increase the exposure to 2.5.
[10:28] And I'll play with the angle of the light. So in this case I'm going to set this dollar
[10:35] altitude to 27. And the azimuth to 70. And now we can also play with the angular size to
[10:43] have a bit of a softer shadows. So some like 5. We'll do. And what else did I change?
[10:54] In this case I went to the sky. Change the turbidity to weight to have this more flat look.
[11:02] And also with this blurring I don't want to see this. These are transitions. So I'm going to change
[11:08] that to something like that. And we have something along these lines.
[11:15] Now we're going to introduce our fogs right now. Probably to check how it looks.
[11:22] But I'm going to first create a material library.
[11:26] And let's create a column material builder.
[11:32] I'm going to name it default. That.
[11:37] I'm going to set this to a grayish value. And increase the reference to 0.8. It's just a preview
[11:43] material. And assign it to everything. Let's see if that doesn't take the wrong.
[11:49] And it should work. Now what we'll be doing next. Maybe we can introduce the fog.
[12:04] So let's do something for it. And we will load in from the obj object. I didn't create an
[12:14] object. So we can go into your fog. Open it to null.
[12:25] Copy this. And press it in here. This is our fog. Now we will need also a material library
[12:37] for the fog. And I'm also going to create a switch. So I can enable and disable the fog.
[12:45] And now merge this in.
[12:51] So this should work. Now let's look. And do some rendering.
[12:58] This is how it looks so far. But we want to change the material of the fog.
[13:11] So in this case, we will use a karma cloud material.
[13:15] Now let's create that karma cloud material.
[13:26] And we will assign it.
[13:33] And I'm going to increase the density to something like the other looks.
[13:37] Now as you can see the fog is terminating over there. It's not big enough.
[13:49] But it won't be too noticeable in the final render when we do the
[13:55] when we scatter the trees. So let's keep it like that for now.
[14:00] So now I'm noticing that the fog is also terminating on the bridge.
[14:05] So we might need to increase it. So let's go into the object level and go into fog.
[14:11] And here in the bound we can increase this upper padding to 2 along the Y.
[14:16] So we have a bit more. And maybe let's also so on the X.
[14:23] Can increase this to something like 2 and 2. But not the Z-Z-Z-R.
[14:29] 2 and 2 in here. Let's see if that works a bit better.
[14:33] So let's go into Solaris.
[14:36] Stage. That should work a bit better if we look at our camera and do some rendering.
[14:46] And now it's hovering all the necessary areas as I see it.
[14:51] So yeah, that is working fine. Now we probably will start to work on the scattering of the trees
[14:58] and the rocks. So let's do that next. So let's just check in here something on the trees,
[15:05] plants and trees. So we don't actually have a name. So let's read the name in here.
[15:14] 4, 3 and in this case the call is 3, 2, 3, 4 and in here we can call it 3 lips.
[15:33] And we have about 3, 1 and we can copy this and go to the stage and start to do the
[15:44] instant thing of our trees. So for that I'm going to read the component geometry.
[15:50] Component geometry to create the proxy and whatnot. So I'm going to do an object merge.
[15:56] And paste this in here. In this case we only have 1 tree.
[15:59] So we should have a look in here. Yes, and let's create a bound.
[16:07] And this will be our proxy. So that's fine. Now we can just create a component geometry variance.
[16:20] In case we have more variations, I'm just going to use 1. So I'm going to set it to number
[16:25] and 1. That's fine. Read the component geometry output. So component output.
[16:31] And I'm going to name it 3s into an explore variance.
[16:40] It's fine and now let's create an instance.
[16:44] Connected to the first input and let's tag inside.
[16:49] Let's disable this. And we will first of all object merge the terrain
[17:03] or the terrain back. I mean, so object merge. And we will go in and let me see.
[17:11] So I don't think I named that. So if we go in here object merge,
[17:18] we should have a terrain back. So in this case is name tree. So I'm going to be here name tree.
[17:26] And we will scatter a few points. In this case, I think we can just go into the overj.
[17:32] And we have here the scattering of the trees. So where is that? This is the rocks.
[17:39] And these are the trees. So we can just copy these from here.
[17:44] I'm trying to see. Let's go again into the stage and paste these in here.
[17:52] So we have the normal, the scatter. Let's paste 32 in the p scale.
[17:57] We have the normals and the randomization of the normals. Let's see if that is working.
[18:03] It is. So if we actually create an output in here,
[18:09] let's recognize this.
[18:16] Then we go out. And now we need to
[18:22] to set in here explore variance, raise and everything.
[18:28] And we should have that. Now we need to burn the original tree. So let's do what we want.
[18:34] And all the trees in here. Let's find. Now let's create the material.
[18:47] Let's have that material library there and merge over this in here.
[18:55] And we should have something like this, which is not ideal.
[19:02] So why is it over there? So let's go again in here.
[19:08] In the instance, so we have them at the center. That's fine. Now let's go in the instance.
[19:18] Maybe when I'm in, so this is name tree. Let's go in here.
[19:32] Oh, it's not this one. Sorry. It's the background.
[19:36] The background in here. So name nine. Sorry about that.
[19:41] So we go in here. We should have named that properly.
[19:46] So now we should work better. So we burn the tree, merge it over and I was looking something like that.
[19:55] Let's disable the grid and look at the render and do some simple render.
[20:02] So everything seems to be working. Now we will do the scattering of the rocks.
[20:10] When in this case, we can maybe copy from here and have a similar setup.
[20:18] Copy this. And let's do in here an object merge.
[20:23] And in this case, we will have 20 variations of rocks, I believe.
[20:34] So let's see how many do we have. So if we go to the JVJ and assets, not assets, sorry.
[20:42] We go into rocks. Let's see how many do we have in here.
[20:49] In this case, we only have seven.
[20:52] Oh, I was looking at there.
[20:56] There's your tree.
[21:02] So in this case, I think we can bring in the rocks as part of our environment.
[21:08] So let's go again. Let's go again to our object.
[21:12] OK.
[21:15] And we can bring in the rocks.
[21:19] So let's do, let's look in here.
[21:24] And let's bring in the rocks.
[21:28] Make sure this is pet instance.
[21:34] And we can get rid of these.
[21:37] And let's play the seeds of these.
[21:47] And let's maybe do the lobolly.
[21:49] So I read the amount of points, the amount of rocks and change the to the seeds.
[22:10] And if we have a look at the IPOLLE, we should have something like this.
[22:14] And now we can just do a naming here.
[22:17] And let's see, do we have a name?
[22:20] No, we can just name in here.
[22:26] And in this case, we want to do it after.
[22:28] So now we should have an import the rocks.
[22:31] And let's save that out again.
[22:33] So let's save to this.
[22:36] And now we have the rocks.
[22:37] Solver this scatterer.
[22:38] That's one way you can do it or you can import these into salaries and do the scattering again.
[22:44] But in this case, I will choose this way and only scatter the trees and the grass.
[22:50] So let's go back to salaries.
[22:54] And we should have the rocks right now.
[22:57] And we should also have the trees.
[23:00] We can actually delete these because we want to use it.
[23:05] And let's see how that moves.
[23:14] And now we have everything ready to look into the materials.
[23:23] So the shading and also to some scattering of grass elements in here.
[23:29] And yeah, let's do that next.
[23:32] So before we move into the materials, I also want to create some sort of cloud
[23:37] gobble on these environments above the environment to create some nice interactive shadows.
[23:43] So I'm going to disable this fork for now to have a more responsive feedback.
[23:50] So in here, we can actually create a salt grid.
[23:58] And let's name it cloud cloud gobble.
[24:07] And we will do the folder. We'll create a grid.
[24:11] It will be around 25 by 25.
[24:15] So quite big to cover the full environment.
[24:19] Rose and columns will be fine.
[24:21] We will just subdivide it quite a bit.
[24:23] So subdivide.
[24:25] This case, I'm going to set it to 3.
[24:28] And we can increase it later.
[24:30] Now let's do one.
[24:31] Add your noise float.
[24:34] And let's name that mess.
[24:39] And look at the result.
[24:40] As you can see, we don't have enough resolution.
[24:44] But let's see.
[24:47] Let's increase this to 5.
[24:50] And we will change the element size to something like 0.9.
[24:55] And we will also play with the offset.
[24:58] So you can pick a different seed.
[25:00] This case, I chose 25.
[25:03] And I was also going to play with the output red.
[25:06] So quite can have a more defined look.
[25:10] So in this case, I'm done.
[25:11] I'll increase this one to 0.5 something.
[25:17] And move this one everything.
[25:19] So we can create these cloud shapes.
[25:21] Now we can just blast.
[25:23] And say you point and that mess.
[25:30] Speak very carefully.
[25:32] Then point by or smaller than point by.
[25:36] So smaller than point by.
[25:37] Get something like this.
[25:40] You can also do it small parts.
[25:46] And the false setting will be fine.
[25:49] And we turn it off.
[25:53] So something like this, you can play with the seed and the size of the clouds.
[25:57] As you can see, you can have more or less.
[26:00] And play with the offset.
[26:01] That's fine.
[26:04] Now I'm going to merge these in.
[26:10] I can actually get materials in here.
[26:16] And this will be over our environment.
[26:18] So let's place a transform.
[26:20] I'm going to move this up to about 3.5.
[26:30] And also move this a bit back.
[26:36] You can leave it like that.
[26:38] Now let's create a material.
[26:40] We will need a material for this.
[26:42] And we don't want to render this cloud.
[26:43] So we don't want them visible in our camera.
[26:47] So we can do render geometry settings.
[26:52] And we will look into the shading.
[26:58] And set in here the render visibility to primary.
[27:02] So now invisible to primary race.
[27:06] So that's it.
[27:08] And now let's have a look at our render.
[27:12] Let's see if it creates some nice shadows.
[27:20] And we also need to enable the file.
[27:24] So let's name this file.
[27:31] Now we're displaying.
[27:33] Let's reset the viewport.
[27:35] Let's find.
[27:36] Let's make sure we have viewport size.
[27:44] Let's find.
[27:44] And let's render this.
[27:48] Oh, let's essentially see if that is creating
[27:53] any same in here.
[27:56] So if we move this down to do it now is over.
[28:02] Why is that rendering?
[28:05] So let's make sure we select the primitives.
[28:09] Oh, now it's working great.
[28:12] And we can actually move these up.
[28:14] Everything else.
[28:16] Three.
[28:17] And as you can see, it's creating some shadows in there.
[28:20] We could probably play with the seeds of these clouds.
[28:30] And it's also creating some make-code rays.
[28:34] Let's make sure this is actually creating something else.
[28:37] Let's create a switch.
[28:41] And create a null.
[28:44] And let's disable this.
[28:46] You can see it's pretty flat.
[28:48] And when we introduce the clouds,
[28:50] we have some more spots of darkness.
[28:52] And we can play with an opacity material to remove some of the opacity,
[28:57] to remove some of the influence.
[28:59] So we can actually pull in here and create our material filter.
[29:02] Let's disable this.
[29:05] And let's disable this clouds map.
[29:09] And I always like to put these in gaps.
[29:14] And we can do the following.
[29:17] And then go into the opacity.
[29:23] And we can go in here into the opacity and reduce the influence of the,
[29:30] of the bad darkness.
[29:32] So let's set that to 0.9.
[29:34] 0.9.
[29:35] 0.9.
[29:38] And assign this,
[29:40] to this material,
[29:42] to this geometry.
[29:44] Let's see how that looks in the end.
[29:51] So I guess I will leave it like that.
[29:53] And now we can finally start to work on the materials.
[30:00] So to create the materials for the terrain,
[30:02] I will take advantage of the karma-triplanar node,
[30:06] which will work better for this situation.
[30:08] Let's disable the fog, to make this a bit faster.
[30:11] And we can also disable the instant scene.
[30:13] So let's read another switch.
[30:15] So we can copy from here.
[30:18] And let's connect that scene here.
[30:24] And that way we can disable the scattering.
[30:28] So we can enable and disable.
[30:30] So that's fine.
[30:32] Now my idea is to use the triplanar for the terrain,
[30:38] for the terrain material.
[30:39] So that means we can create in here a karma material builder.
[30:44] And let's call it terrain mat.
[30:48] And we can start to create a planar and loading the map.
[30:54] But we also need the textures for the normal,
[30:57] the roughness and the displacements.
[31:00] And we will need to link these parameters to all the nodes,
[31:04] to all the different textures.
[31:06] So I have a script that I share before in the channel.
[31:09] And I will link the video in the description,
[31:12] which creates this automatically.
[31:16] So I just need to let's go in here.
[31:20] And in this case, I think I need to be on the material library, I guess.
[31:26] And creating here, it's loading.
[31:29] This is the material I'm going to use, roughcliffe.
[31:31] And if you paste this code on bridge,
[31:32] you can download the same texture.
[31:35] And it will create in here.
[31:36] So I can just copy the name,
[31:38] delete this node, name it, the rain mat.
[31:42] And what this will do is to create different textures,
[31:45] as you can see, for the and connect it to the material.
[31:50] And as you can see, the parameters are all linked.
[31:53] So if I change the size in here, it will change the same on the specular,
[31:56] the normal and the displacement.
[32:00] So now let's actually work a bit on the materials.
[32:07] So let's see if we can actually visualize it,
[32:11] if I create this material and assign it to the rain.
[32:17] So it's case to rain.
[32:19] Do we visualize anything?
[32:23] So if we look in here,
[32:28] and I think it's because we have the displacement on.
[32:30] So if we disable the displacement,
[32:33] we should be able to visualize it better.
[32:36] Let's set it to default shading.
[32:39] And now, I don't want random rotation,
[32:42] as I want the layered look.
[32:45] I want to change the size to two,
[32:47] and we can play with a different seed.
[32:50] And also increase the triplanar blend to something like that.
[32:56] So this will and this will propagate to the roughness,
[33:01] to the roughness map, as you can see, and the normal.
[33:04] In this case, I don't think I used normal or did I add it.
[33:10] And I'm just going to make sure I'm using point of going, let's find.
[33:14] And now we will need to mix this between the rock texture and the grass texture.
[33:22] So I'm just going to duplicate this albedo one, and load in the grass texture.
[33:32] So in this case, we'll be this one, grass wild, and you can copy this code.
[33:37] And I'm going to mix this, and I'm just going to mix the albedo.
[33:41] And so we can take this from background and this as foreground.
[33:48] And we can use a Geo property value, or a USDV printbar reader, it's the same.
[33:54] And in this case, I think it's called it, I call it mask grass.
[34:00] Let's see if that works out.
[34:02] So if I connect this to base color, yeah, mask grass.
[34:05] And if you have questions, you can always go in here,
[34:08] and look at the different printbars you have.
[34:12] So in this case, the rain, we should have been here, mask grass, as you can see.
[34:18] So that's fine.
[34:20] We have the blending.
[34:21] Now we need to do some color correction also.
[34:24] So let's do color correct.
[34:25] And I'm not even rendering right now, but we will do that in a bit.
[34:29] So I'm going to color correct both textures.
[34:32] And maybe it's a good idea not to do the rendering.
[34:38] So if we get in here,
[34:44] and let's look at the final shading, disable this, we won't need it any longer.
[34:52] And let's do some rendering.
[34:56] So right now is too dark, as you can see.
[34:59] And it's also on filing and looking up.
[35:03] And let's wait for the compiling.
[35:05] And we will do some changes to color correction.
[35:10] So let's go in here to the material library.
[35:15] And let's increase, first of all, the rain, so the rock texture.
[35:19] Let's increase the exposure to one.
[35:21] We should start to see something.
[35:23] And let's also increase the exposure of the grass, something like you.
[35:29] And I also change a bit the contrast.
[35:33] So in this case of the rock, just a little bit.
[35:39] The weapon work contrast.
[35:42] And the rest I think I like it a bit more.
[35:47] I'm going to increase the saturation of these grass textures.
[35:52] So about 1.15,
[35:55] we have this more green look.
[35:57] And I might also play with these clouds.
[36:05] So let's disable this just to check something.
[36:09] It won't make much difference.
[36:10] It's just creating some dark, some darkening on this rain.
[36:15] So now we need to work on the displacement.
[36:18] Because right now is too flat.
[36:20] So for that,
[36:25] I'm going to add the displacement.
[36:28] So in this case, let me see.
[36:32] So if I look in here, we should have the displacement in here.
[36:37] And we have the same setting.
[36:38] So that should align perfectly.
[36:41] So let's separate these into a float.
[36:43] So separate color for.
[36:46] And we will remap since it's a mega-scan.
[36:49] Direct texture.
[36:50] So we can remap it between
[36:52] minus 0.5 and 0.5.
[36:56] And we also don't want displacement on the grass.
[36:59] So for that, we will take this grass material,
[37:03] grass mask and invert it.
[37:07] And we can just multiply these over.
[37:12] So if we connect that to the displacement,
[37:16] in this case, I used a value for the displacement about 0.3.
[37:23] We won't see the preview, at least I always have that problem.
[37:28] Let's see how that looks.
[37:30] So it will compile for a bit and initialize.
[37:34] And as I can see, it's creating these nice displacements on our terrain.
[37:40] As you can see around here also, and on these parts.
[37:43] And let's actually introduce the fog to see if that looks a bit better.
[37:49] Let's wait for a bit.
[37:51] And this is how it looks with the fog.
[37:53] It looks a bit better.
[37:54] And it starts to integrate our environment.
[37:58] So, and this grass texture won't be that visible because we will scatter some grass.
[38:04] But for now, we can start maybe to work on the material for the
[38:12] this little river. So let's do that next.
[38:19] So for the material of the river, we will just do a simple displacement or normal map
[38:25] that will work just fine.
[38:27] So let's create a texture first.
[38:29] So in a cockpit, I'm going to call it water noise.
[38:35] Let's just create a rectangle 3D noise.
[38:39] Let's disable the opinion.
[38:42] And I'm going to increase this or to decrease this
[38:48] something like this.
[38:49] And also decrease the roughness as I don't want it super rough.
[38:54] So something like this and create a null.
[39:00] And let's name it out this case.
[39:04] I'm going to use this displacement.
[39:08] Let's copy that.
[39:10] And go into our material.
[39:11] Let's create our material builder.
[39:15] And name it water map.
[39:19] Let's disable this.
[39:21] And we will load some image.
[39:26] And we have loads of OP.
[39:29] And loading that displacement.
[39:31] Let's connect that to the displacement.
[39:34] So for the material, we will change it to water shader.
[39:44] So in this case, I'm not even going to bother using this displacement.
[39:48] We can just use in your normal map.
[39:56] So normal map.
[40:00] And we will need to
[40:04] create a normal from that texture.
[40:06] So in this case, let's go in here.
[40:10] And let's do out normal.
[40:12] And create an item from normal.
[40:14] Right to normal.
[40:15] And let's reduce this displacement point 1.
[40:18] 1.5.
[40:20] Oops.
[40:21] 1.5.
[40:22] So something like this, let's copy this.
[40:24] And then we can add a layer of the layer.
[40:26] And then we can add a layer of the layer.
[40:28] And then we can add a layer of the layer.
[40:30] And then we can add a layer of the layer.
[40:32] And let's copy this.
[40:37] And we were here.
[40:40] Let's load this as a factor 3.
[40:42] And it's already loading the texture.
[40:44] Let's connect this to the normal.
[40:46] And we can change the scale quite a bit.
[40:49] So let's load that to the normal.
[40:52] To create a water material.
[40:53] So we can just set the reference to really low.
[40:56] Increase the transmission.
[40:58] and let's see what we do next. So let's assign this and let's connect in here the geometry.
[41:08] So the water geometry. Let's have a look at that. And I don't have this gathering of the
[41:18] tree that's fine. Let's look at all the results. Now in this case is reflecting white a bit,
[41:25] but we might need to change the bump amount. So let's decrease this to 0.3.
[41:36] As you can see it's it's losing the reflections quite a bit and when we introduce the trees,
[41:44] if we enable the trees, so if I go in here and enable the trees and some rendering.
[41:50] So as you can see with the trees rendering in the background, we lose almost all of the
[41:58] reflection. So I'm going to sheet a little bit and introduce the light in here. So I'm going to
[42:02] create a light and it's going to be a rectangle light. Let's have a look at that.
[42:10] Maybe we can disable this for now. Let's select that light
[42:16] and rotate it like this and also increase the size and increase this along these axis and increase in here.
[42:30] And we can move it up, rotate it. So we just want to eliminate the river
[42:37] or this small pond. So I guess this will be fine. Let's see how that renders with the fog.
[42:52] And as you can see it's also illuminating the entire environment which I don't want.
[42:58] So I'm going to create a light linker and let's see on this light and I want just to
[43:07] affect the water. So let's connect it in here. Let's see how that looks.
[43:15] Now we should remove the lighting on the other objects.
[43:20] The displacement is taking quite a bit so we can probably disable it.
[43:24] So as you can see now it's creating those nice reflections. And since I lost a bit of the
[43:30] recording and that to do this part again, I believe I also changed in here the bump amount.
[43:38] So in this normal my body agrees with the point three. Let's decrease it to point one.
[43:43] Let's see if that looks a bit better and I guess it does. Maybe
[43:50] five. And we could also probably decrease the intensity of the light.
[43:58] Let's go in here. Let's increase this to point five.
[44:07] We want it really subtle as you can see which is one thing that is some water in here.
[44:13] I guess this will work fine and we can move on.
[44:17] Now let's do the material for the bridge. So this time. And for that we will go again to this material library.
[44:26] And we will load another mega scans and we will use triplanar again. So I'm going to use my script.
[44:33] And I'm going to use these material in here.
[44:37] So create that. And I'm going to name it stone bridge.
[44:46] Stone bridge.
[44:49] And let's see. I'm going to use the roughness normal but no displacement.
[44:57] So I can just delete this one. And in the albedo.
[45:04] Let me see what sort of size did I use in this case. We can assign it to the geometry.
[45:10] So in this case to bridge stones and see all that looks.
[45:17] Let's disable the fog on now.
[45:22] And we might need to change the size.
[45:29] So in this case I'm going to increase it to point five.
[45:33] And I'm also going to reduce the random rotation and play with the seed.
[45:39] And I can also play with the triplanar blend. So it blends better around the corners.
[45:51] Now I'm going to color correct this. So color correct.
[45:58] And in this case.
[46:00] I'm going to reduce the saturation to point nine.
[46:07] And as for the gain and you, I'm going to change that with the attribute.
[46:12] But for now, it's in greater exposure to 1.5.
[46:15] Otherwise, it will be too dark. But let's keep it like that for now.
[46:19] And we will work on that in a bit.
[46:21] So let's load the attribute with the geometry property value.
[46:24] And if you remember, we have that integer class attribute.
[46:28] And we can actually create a random float.
[46:32] So material random float.
[46:35] And we can load that in and load that for the gain.
[46:41] And of course, we won't have a visualization.
[46:44] So what we can do is to let's disable those clouds and those trees.
[46:53] And I'll never look at it.
[46:57] So let's render.
[47:01] And we should disable the displacement also otherwise it will take a while to loading.
[47:07] So let's go into that stone reach.
[47:11] And as you can see, it will be too dark.
[47:14] So we can right away with the exposure to 1.5.
[47:21] And we need to play with this random float.
[47:23] So in this case for the gain, I'm gonna set,
[47:27] I'm gonna play with the seed.
[47:28] As you can see, we can play in here with the seed.
[47:31] And I'm gonna set the minimum to be 1.5.
[47:35] So we just darkens a little bit.
[47:38] And I'm also going to create another random float.
[47:42] And this, and this one, it will be connected, I want to change the seed.
[47:47] And this one will be connected to the U.
[47:50] And that will just get random colors.
[47:52] So we need to play with the range in here.
[47:55] So in this case, I'm gonna set the minimum to be around 0.9.
[47:59] And maximum to be around 1.5.
[48:02] This is really sensitive.
[48:03] So you need to play with the values.
[48:05] And we had something along those lines, which looks alright.
[48:09] Let's, in this case, I don't think I changed anything else.
[48:15] We could probably play with the normal in here.
[48:18] So let's reset to 1.
[48:22] Let's start with the other big more detail.
[48:26] Let's load in the trees.
[48:29] And the fog.
[48:33] And I have a look how it renders.
[48:38] We're about to put in the trees.
[48:41] So let's load those in, because it will darken significantly the environments.
[48:49] Let's actually make sure I enable the trees.
[48:53] As you can see, it's a bit darker.
[48:56] But maybe we can decrease the exposure in here.
[49:03] Instead of 1.5, I might play
[49:08] the tree.
[49:12] I might decrease it.
[49:14] So in the color correct, 1.2, that's the
[49:19] will be a bit darker.
[49:21] And maybe it's a good idea that we introduce a dino exerne.
[49:26] So let's go in here.
[49:29] And image output filters and increase the
[49:33] scale we can use the nbd1.
[49:38] And we can also do the material for the path.
[49:42] So let's do that next.
[49:47] So we can actually apply the same material for the path.
[49:52] So let's go in here.
[49:55] We can just say,
[49:57] bridge, add.
[50:01] And then we should assign the same material.
[50:03] Let's have a look at that.
[50:12] And let's see.
[50:19] It can maybe also assign the same terrain material to the back.
[50:23] So in here, we assign this to the terrain.
[50:27] So let's do scene.
[50:30] And we do the terrain back.
[50:35] So in this case, scene.
[50:38] And let's have a look at that.
[50:44] So in this case, I had the crash at the beginning of the recording
[50:47] and lost the material of the fog now that I see it.
[50:50] So we can just create in here a karma cloud material.
[50:53] And let's disable this.
[50:55] And we will.
[50:57] And we will increase the density to two and assign it to the fog.
[51:02] So let's out of fuel and assign it.
[51:04] And let's have a look at how that renders out.
[51:08] It should have a bit more intensity on the fog.
[51:11] And it will look a bit darker.
[51:13] So as you can see, these fog material works a bit better.
[51:16] And it darkens a bit this part of the environment.
[51:19] We could probably increase it a bit more.
[51:21] But let's work next on the materials for the trees, the rocks and these vines.
[51:26] And in the end, we will do the scattering of the grass.
[51:30] So I think right now, I'm going to do the scattering of the grass.
[51:35] So we can start to have a look at how it will look in the end.
[51:40] And for that, I'm going to duplicate this scattering system I have in here.
[51:45] And we will work from there.
[51:47] So let's duplicate this.
[51:50] And in this case, we will have 20 variations if you remember from our assets in here.
[51:59] So as you can see, we have in here the assets and we have 20 variations.
[52:07] So let's go into the stage and load that in there 20.
[52:13] And in this case, we will load in from the assets.
[52:18] So let's go into assets and load the var1.
[52:23] And in this case, we will take advantage of the geo-variant index.
[52:29] So let's open these tactics and do that at geo-variant index.
[52:36] And we will increase to 1.
[52:41] And we should have that load.
[52:44] So let's do geo-variant index, geometry variance.
[52:50] Let's name this grass.
[52:53] So grass and explore variance.
[52:56] And we should have all the grass variance in here.
[53:01] So that's fine.
[53:03] And now let's do the instance in.
[53:07] So for that, I'm going to load the terrain.
[53:10] So let's go in here.
[53:12] And we will object merge to out the rain.
[53:17] We should have that in here.
[53:22] And we will just blast the terrain.
[53:29] We don't need to water.
[53:31] What are we visualizing in here?
[53:32] So that's fine.
[53:35] Now I will create an attribute in here.
[53:38] So we can use later on shading.
[53:42] So let's use a nice float.
[53:47] I'm going to call this seed.
[53:49] Let's visualize that.
[53:54] And in this case, I'm going with an element size 0.56.
[54:00] So decrease that.
[54:03] And it will be positive.
[54:05] That's fine.
[54:07] Now let's mix the attribute wrangle.
[54:15] Let's mix the river mask with the grass mask.
[54:19] So we can scatter only on those parts.
[54:23] In this case, I want to remove the river from the...
[54:26] So let's have a look at the mask grass.
[54:28] As you can see, we have also on the river.
[54:30] So I want to remove from there.
[54:32] So for that, I'm going to create a mask.
[54:35] Grass, it will be multiplied by the inverted of the river.
[54:41] Since we also have a river mask, and we should have that.
[54:45] So that is fine.
[54:48] Now we will do the scattering.
[54:52] So we can actually do the normals and do the scattering.
[54:56] And then we will scatter on the mask grass.
[55:01] We are scattering on the mask.
[55:04] And I'm going to change this to density.
[55:06] And let's see.
[55:07] 100, 1000, 2000, 500.
[55:13] So something like that.
[55:14] We will have 80,000 points.
[55:16] Let's find.
[55:18] Can't play with seeds.
[55:19] But I'm not going to bother.
[55:21] As for the p-scale,
[55:25] I'm going to use in this case, annoyed.
[55:30] So in this attributed just float, I'm going to use a noise.
[55:34] Call it p-scale.
[55:37] And I'm going to change the element size.
[55:41] So in this case,
[55:44] I'm going to change the element size to 0.25.
[55:50] And we can play with the offset.
[55:55] And
[55:57] the rest is fine, I guess.
[56:02] Nice pattern simplex.
[56:05] And now let's do the final p-scale.
[56:07] So if we go in here to constant,
[56:10] we can reduce it quite a bit to 0.03.
[56:14] As for the normal, we can do the same.
[56:17] So if we decrease this,
[56:20] so in the scatter, let's decrease this.
[56:24] Now let's have a look at the normal.
[56:27] And it should be randomized.
[56:29] Yes, so that's fine.
[56:32] We can probably play with the seed.
[56:34] Just.
[56:37] And now let's have a look at how that renders.
[56:42] So let's increase this to 0.2500.
[56:47] And in the instacer, we need to explore variants too.
[56:52] And grass and all the instaces.
[56:55] So let's prune in the grass.
[56:59] And we will assign the materials later.
[57:01] So let's merge this in.
[57:05] Let's first of all make sure this is working.
[57:08] And it is.
[57:10] Let's reset the viewport just in case.
[57:17] So that should be working.
[57:19] Let's have a look.
[57:21] And let's do a render.
[57:26] And let's make sure, let me make sure I enable these in here.
[57:30] So the cloud code is enabled.
[57:32] Let's find and let's render.
[57:36] So it will help if we do actually create a material for the grass.
[57:41] But as you can see, the scale is correct.
[57:44] And let's do now the material for the grass.
[57:48] So grass.
[57:51] And I'm using mega scans as it should be as simple as loading the texture.
[58:00] So let's do a caromaterial builder.
[58:04] And creating a grass mat.
[58:09] I'm going to load in the albedo.
[58:15] So let's do a image.
[58:17] And it will be on color.
[58:18] And this is the albedo from the Atlas.
[58:22] Let's load in as a base color.
[58:25] And we will also do a color.
[58:31] And we will duplicate this and load in the roughness.
[58:35] Mess load that in.
[58:38] It's a specular roughness.
[58:40] And we will also load in duplicate the albedo and load in the transversal scene.
[58:47] And let's connect that to the subsurface color.
[58:55] Let's make sure we increase the subsurface.
[58:58] So we listed as set it to 0.6.
[59:02] And we will use the involved since this is single-sided geometry.
[59:06] And we will also need a color correct on this.
[59:11] So let's connect that subsurface color.
[59:15] And I will need to increase the exposure quite a bit.
[59:22] So in this case I'm going to increase the exposure to
[59:26] and 2.5 on the transversal scene.
[59:29] Let's see how that renders.
[59:31] If that doesn't take too much to load, let's make sure we set this to viewport size.
[59:37] And the rest is fine.
[59:39] We might decrease the viewport size.
[59:42] So it doesn't take so much to render since I'm on a 4K monitor.
[59:47] Let's actually make sure we assign this in here.
[59:51] So let's assign this all the geometry.
[59:56] And as you can see the material and values are working nice.
[60:04] We just need maybe to play with the U, I guess.
[60:09] I'm going to randomize the U from that noise we created.
[60:14] So for that I'm going in here.
[60:18] And I'm going to do a property value and load in that seed noise that we add.
[60:24] And we can create random float from this random float.
[60:32] And in this case let's leave it like that and load that in as a U factor.
[60:40] So if we load that in as a U,
[60:44] let's apply it as a factor.
[60:47] Let's see, as you can see it's not working great.
[60:51] So we need to play with the range in here.
[60:53] This case can go with a range of 0.9.
[60:59] And maybe 0.95, I don't want it so orange and 1.25.
[61:08] And as you can see some patches are
[61:11] more towards yellowish and others more green.
[61:14] Maybe decrease these a bit, I don't want it so green.
[61:17] So I guess this will work fine.
[61:21] And that's basically our scattering done.
[61:23] We just need to work on the few materials that are left.
[61:27] So let's do that next.
[61:30] So now let's do the final materials.
[61:32] I'm going to start by disabling this fog and do the materials for the trees.
[61:38] So we have it
[61:42] grass trees.
[61:44] So let's create the current material builder.
[61:48] And let's do three leaves that
[61:55] and allow the image.
[61:58] It will be the same image.
[62:01] Let's disable for now, decrease because it's getting too slow.
[62:07] And it will be the same image we used for our previous purpose.
[62:12] On the
[62:15] on on on subs.
[62:18] So it's in here tree leaves met and I'm going to load it.
[62:23] It will be this orbital right away going to color correct.
[62:28] And connect it to the base color.
[62:30] Loading the roughness.
[62:35] And loading a scholar.
[62:38] The translucent sea.
[62:40] I'm going to reference copy this color correct.
[62:44] Connect it to the subsurface color.
[62:49] And this one to do roughness.
[62:51] Gonna enable the involved and for the subsurface.
[62:55] I'm gonna edit it to in this case to point four.
[63:00] And in the color correct, I'm going to just increase the exposure a bit.
[63:06] Or a bit let's actually apply that
[63:11] to the leaves.
[63:15] And we can also do let's actually increase this exposure to 1.8
[63:23] and do the material for the bark.
[63:27] And bark met.
[63:29] And this one.
[63:35] I will just loading a texture from Megascans.
[63:39] So it will be this one in here, this tree bark.
[63:42] There's a no section in there.
[63:45] So correct.
[63:48] Color correct.
[63:53] And I'm loading the roughness.
[63:57] So roughness to the specular roughness.
[64:02] I'm also going to loading the normal so vector tree.
[64:06] And normal.
[64:08] Create a normal map.
[64:12] And connect these to the normal inputs.
[64:17] I believe that so.
[64:18] And
[64:20] or the material.
[64:22] We can just set this one to 1.5 or the exposure.
[64:30] Let's see that and assign that to the bark or trunk.
[64:36] Did trunk I call it?
[64:38] See.
[64:40] And the tree leaves tree trunk here.
[64:43] That is fine.
[64:45] Let's have a quick look at this.
[64:47] As you can see without the bark that is working properly there.
[64:55] Let's introduce the fog and see how this looks.
[64:59] So let's make sure we have everything enabled.
[65:03] And we in this case.
[65:07] This is the grass.
[65:09] So let's also have a look at that.
[65:11] So we won't notice much color going through there due to the fog.
[65:18] But it will have an int.
[65:20] So now let's work on the material for the rocks.
[65:25] So let's disable some of these instances.
[65:30] And let's go in here to the material.
[65:34] And in this case I'm going to use again a triplanter to texture these rocks.
[65:38] So we can here and I'm going to load the mega scans again.
[65:41] This time with this rocky mossy you can copy the code as always.
[65:46] Let's load that in and let's call these rocks.
[65:49] Matt.
[65:51] And we need to figure out in here this separate color.
[65:59] Since we just want to float and remap it.
[66:02] So remap
[66:03] we have 3 minus 5 and 25.
[66:08] And then we will also change the displacement.
[66:12] So in this case I just want 0.07.
[66:16] It will be enough.
[66:18] And I'm also going to change the size in here.
[66:20] Set it to 2.
[66:23] And going to color correct it a bit.
[66:27] So from this orbita can create a color correct.
[66:33] And I'm going to increase the exposure to 1.25.
[66:39] And maybe change the U to 0.036.
[66:45] Something like this.
[66:46] Let's assign this to the rocks.
[66:49] So let's out of here.
[66:52] And in this case we have leaves and rocks.
[66:57] So if we assign this to rock.
[67:00] It should assign to the rocks.
[67:05] Let's have a look at the render.
[67:09] Let's disable the shelf.
[67:15] So when this is the final material for our rocks.
[67:18] To look somewhat decent I'm just going to leave it like that.
[67:21] Now we just need to work on the material for the vines.
[67:26] So let's do that and do the final render.
[67:29] Because you're probably tired of hearing me back and forth.
[67:33] So for the vines we will create one for the vines itself.
[67:39] So car material builder and name it vines matte.
[67:47] And in this case we will use another bark from mecha scans.
[67:53] So let's create a image.
[67:56] And I'm going to use this one in here.
[68:00] I'm going to as always fall and correct.
[68:04] I connected to the base color.
[68:06] Load in this float the roughness.
[68:10] So roughness.
[68:12] Connect that to the specular roughness.
[68:14] Now so going to load the normal in this case.
[68:18] So normal and connect this to a normal map.
[68:22] And connect it in here.
[68:26] Let me see if I changed the scale now.
[68:32] And I'm just going to decrease the gain.
[68:36] I in this in this case to point five since I wanted it quite dark.
[68:42] Let's duplicate this one.
[68:45] I'll drag and pull it all use.
[68:48] Matte.
[68:50] And for this one we will use the same Atlas texture.
[68:55] We use Don't Sobs.
[68:57] So I'm just going to select all of these.
[69:00] Change this to color.
[69:02] And paste in here in this Albedo.
[69:04] It should paste on all.
[69:06] And now we have the Albedo.
[69:09] We should have a roughness.
[69:12] And we should have in this case I don't want any normal.
[69:16] So I'm going to duplicate this and load in the translucency.
[69:21] I'm going to control all shift drag to create a reference copy.
[69:26] And paste these as subsurface colors.
[69:33] Sub subsurface color.
[69:34] As for the subsurface I'm going to set it in this case.
[69:39] It can be the same as the leaves on the trees to point four and make sure it's team walked.
[69:45] And the color from actually need actually to increase in here.
[69:52] The exposure.
[69:52] So I'm going to set to a value of 3.2.
[69:57] And I'm going to blend in this case.
[69:58] I'm going to reset the gain and change the U.
[70:01] I want it slightly more green.
[70:03] So this is a very sensitive parameter.
[70:07] So I'm going to set it to something like that.
[70:09] Let's see how that looks.
[70:11] So if we actually assign this.
[70:14] So let's set it to fine.
[70:16] Oops.
[70:18] Fines.
[70:21] And as you can see it loaded the texture in.
[70:24] Now we can assign these two leaves.
[70:31] So that is not loading.
[70:33] Let me see in here.
[70:34] So if I go into scene.
[70:37] It defines.
[70:39] And I have the instances leaves.
[70:43] So let me see if that is all material binding.
[70:48] It's binding.
[70:49] So it should be working.
[70:50] But since it's an instance is not displaying properly.
[70:53] So this should be working.
[70:57] Let's enable the grass.
[71:01] This one is enabled.
[71:02] This one is also enabled.
[71:05] Let's enable the fog.
[71:06] Let's disable the fog for now and just see how that looks.
[71:09] If it's loading the materials or not.
[71:12] So it's not loading the materials.
[71:15] Let's have a look on why it's that.
[71:20] This case.
[71:23] We need to be a bit more specific on here.
[71:28] So in here.
[71:31] We can do the following.
[71:32] We can load in this.
[71:34] Instances.
[71:38] And just do wild cards.
[71:41] Look at that work.
[71:43] So it's the same for the types leaves.
[71:48] Will that work?
[71:50] Let's have a look in here.
[71:53] And it's not working.
[71:55] Do we have.
[71:56] Do we have.
[72:04] Do we are we binding.
[72:05] So result preview material.
[72:07] Result for material.
[72:11] Do we have your V's.
[72:12] So let's go into the object.
[72:15] Geo.
[72:18] And we do have your V's.
[72:20] So why is it not working?
[72:22] Oh, I know why.
[72:23] Because we are we have this default material that is probably let's disable this default material.
[72:36] And let's disable this one.
[72:39] Oh, as you can see is working now.
[72:41] So the default material was causing an issue there.
[72:45] We had several look and see if that works now.
[72:50] Should be loading the material as you can see.
[72:55] And now let's do the final render.
[72:58] So let's increase this.
[73:01] Let's get more samples and maybe play with that SSS limit.
[73:10] And let's see how that looks.
[73:14] Do we have the phone.
[73:16] Let's control this and see how that looks.
[73:22] So I might want to reduce the exposure on those leaves because it's too much I believe.
[73:29] So I'm going near on the leaves.
[73:33] And I'm going to decrease this to 75.
[73:38] Let's see if that doesn't take a long.
[73:40] Now it might be too dark.
[73:43] So let's increase it to 3.
[73:48] And I guess this will be my final render.
[73:50] I will just maximize the view.
[73:53] And we will have a look at the final results.
[73:56] So let's just maximize this in here and we'll final render.
[74:01] So guys, this is more or less the final render.
[74:04] I just paused that like 40% because it will take a little bit longer to render everything.
[74:09] That's 4K.
[74:10] So it's not a perfect environment but hopefully you picked up a few techniques.
[74:17] And it's up to you now to leverage another level of this environment and create something better.
[74:23] So I hope you have enjoyed this series.
[74:25] It was quite a bit of work to put it together.
[74:28] But in the end, I think it's worth the effort.
[74:31] If you find this useful, please let me know in the comments.
[74:35] And don't forget, I also have a Patreon where you can download all the files from my videos,
[74:39] including this one, along with exclusive tutorials and also some courses I have in there.
[74:46] So with that in mind, thank you for watching and I guess I'll see you next time.
[74:50] Thank you.



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
