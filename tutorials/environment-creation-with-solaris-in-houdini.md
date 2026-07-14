---
title: Environment creation with Solaris in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=2f_40GhnBXI
author: cgside
ingested: 2026-07-13
houdini_version: "19.5"
tags: [solaris, lops, usd, scattering, instancing, vex, materials, shaders, arnold, procedural, environment, advanced]
extraction_status: complete
frames_dir: tutorials/frames/environment-creation-with-solaris-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Environment creation with Solaris in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=2f_40GhnBXI)
**Author:** cgside
**Duration:** 65m18s | 12 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Initial setup, dome light in Solaris [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] We will continue where we are left off in this terrain slash fields project.
[0:08] And let's get started by in the network.
[0:12] Let's drop in a null and call it up to the rain.
[0:21] Let's connect it to our terrain here.
[0:26] And now we can go to the so we go to the salaries and change this to stage.
[0:36] And we have an empty stage so let's import our terrain.
[0:42] Let's go out to rain except unload this reference.
[0:45] If you see this warning you just need to save the file and it will go away.
[0:54] So let's drop a light, so don't light.
[0:58] And I have a texture somewhere.
[1:01] Yeah, this one.
[1:09] Let's enable these nodes and we can use karma or redshift but I'm going to use Arnold
[1:17] as I'm more familiar with it.
[1:21] So the first thing we see is the format of the light is not correct, we need to change
[1:28] it to a light long.
[1:30] And let's also go to the Arnold settings set or creating the samples and set it to two.
[1:39] Let's create a more dramatic light lighting by rotating a bit the light not so much.
[1:50] Something like this.
[1:54] Yeah, this should do.
[1:58] Let's disable the grid.
[2:01] Okay, now let's create a material library to assign some materials to our terrain.


### Shading the terrain [2:05]
**Transcript (timestamped):**
[2:10] And let's create the material builder, Arnold material builder.
[2:15] Let's call it to rain, land, let's dive inside and create a standard surface.
[2:25] Let's give it some color and connect the shader to the surface.
[2:32] Now in the material library you can click on out of film materials and let's assign it
[2:37] to the heights which is the name of our geometry.
[2:43] So yeah, it is working.
[2:48] Can this saturate a little bit?
[2:50] Yeah, but we will use another technique.
[2:54] So let's create a vector, a little state vector.
[3:00] Let's set it to shading normal and with that we can connect the dot products, connect
[3:06] the vector to the input one, set just, we just want the y and let's connect it to the
[3:15] base color.
[3:17] So nothing much to see.
[3:19] So let's create a ramp and in here we can connect to the first input to the input.
[3:29] I mean, and we can drag this.
[3:35] As you can see we start to create a mask to make some textures later.
[3:49] So let's load some textures.
[3:53] Let me see if I have it here.
[3:55] It's not this one.
[3:58] Yeah, it's here.
[4:01] It's the albedo.
[4:04] This is the grass texture.
[4:07] Let's connect it to color connectors and then to a triplaner.
[4:18] Tryplaner.
[4:21] Let's go to inputs and connect it to the second color of the ramp.
[4:33] So let's increase the exposure and fix the tiling.
[4:39] We will use a triplaner because it has some attributes to control the repetition.
[4:44] So base relative reference and let's go to point 01.0808.015.
[5:00] So something like this.
[5:08] Now we can load another texture.
[5:12] Let me see if I find it here.
[5:14] It's not this one.
[5:18] Yeah, I believe it is this one.
[5:24] So we can revert the values to factory defaults and let's connect this triplaner to the color
[5:34] one.
[5:39] Let's see how it is the repetition.
[5:46] And so to something like this.
[5:55] Let's also create the roughness.
[6:02] We don't need these two.
[6:03] Just connect it from here.
[6:08] And let's load the roughness.
[6:17] So click roughness and this one is correct.
[6:22] Let's just change it to raw utility raw.
[6:33] And let's connect one of the channels to the specular roughness.
[6:42] Now we can adjust the bits and the colors.
[6:48] Maybe we remove the bit of saturation.
[7:05] And the rough one is looking a bit too reddish.
[7:10] So let's increase the bit to you.
[7:13] Maybe not so much.
[7:17] Yeah, something like this.
[7:24] Still this rough texture is a bit...
[7:34] Let's increase the gamma.
[7:43] We can adjust it later.
[7:44] Let's leave it like this for now.
[7:47] Now we will also benefit from some displacements.
[7:52] So let's reuse this setup.
[8:02] And loading the displacements.
[8:05] Let's just get rid of the color correction nodes.
[8:09] And loading the displacements.
[8:11] Not the JPEG but the XR.
[8:13] I'm still loading the same one.
[8:18] So yeah.
[8:23] Now we can connect it to the displacement outputs.
[8:31] So as you can see we have the material assigned.
[8:35] No sign of displacement.
[8:38] So let's create render geometry settings.
[8:48] We don't need subdivision but displacements.
[8:52] So let's enable out of them.
[8:54] Set the padding to 3, something like this.
[8:56] 0 value to 0.5.
[8:59] And let's get light time.
[9:04] But still we see no displacement.
[9:05] I believe this is bug.
[9:09] Because everything is assigned and it should work.
[9:14] But it's not loading in the displacement.
[9:17] So let's instead of assigning here to work around this to assign material.
[9:23] Use an assigned material.
[9:26] And now we can change the primitives to height.
[9:31] And the material path should be the rain mat.
[9:39] Let's see if the displacement is working now.
[9:41] And yeah, now it's working.
[9:45] The speed is a bit too much.
[9:53] Let's just do something here in the material.
[9:59] We want to play with blends and salad roots to rotate a bit the textures.
[10:12] So let's copy this parameter and paste it.
[10:19] Let's paste relative reference.
[10:24] And we need to paste in all of them.
[10:33] I should have done this in the beginning.
[10:40] Let's also copy this one.
[10:47] Place it here.
[10:53] Place it here.
[10:58] Here.
[11:06] So let's see.
[11:08] Now we no longer see those lines.
[11:25] Let's try to add a subdivision.
[11:37] Maybe reduce the height to weight.
[11:44] Let's go to the material.
[12:01] Push the RAM value.
[12:08] Let's leave it like this for now.
[12:16] Okay, let's check again the render.
[12:38] This green is a bit too intense.
[12:40] So let's come here.
[12:44] And this is one.
[12:48] Let's change.
[12:51] The U is okay.
[12:54] That perhaps the saturation.
[12:57] Yeah, something like this will work better.
[13:05] We can increase the bits.
[13:10] This one.
[13:15] Still this one is a bit too yellow.
[13:23] Let's keep it like this for now.
[13:30] Maybe increase a bit the height.
[13:39] We will see from here.
[13:43] Yeah, let's leave it like this.


### Component geometry, Instancer and scattering some trees in Solaris [13:53]
**Transcript (timestamped):**
[13:53] So let's go back to the object context.
[13:55] Let's create a geometry.
[13:59] Let's go in this assets.
[14:06] Let's create an Olympic.
[14:17] And let's load.
[14:21] I believe is this one.
[14:23] Yeah, we can hide all the other objects.
[14:28] Let's just transform it, scale it down.
[14:32] Because it's too big.
[14:35] Something like this.
[14:40] And we can call it a tree trillion.
[14:50] Let's get back to the stage.
[14:53] This time we will use a component geometry.
[15:02] And by being inside, we can object merge the tree in the assets tree.
[15:12] Let's connect it to the default.
[15:15] And as for the proxy, we can just create a match size and a box.
[15:23] Let's resize it.
[15:26] And here we can scale to fit Sanante, any form scale.
[15:32] So yeah, it is working.
[15:36] Okay.
[15:39] Now we have the tree.
[15:41] We can create an instance.
[15:43] Let's add it to the first input.
[15:48] And zero.
[15:50] And here, let's load our terrain.
[15:55] Let's create an earlier and call it terrain.
[16:01] And let's go to the lobbying boards.
[16:07] Let's go to terrain.
[16:15] And we will scatter.
[16:18] But as you can see, it's not showing any points.
[16:24] It's just reduced the points.
[16:29] What we need to do is to unpack the USD for this to work.
[16:36] Please should work.
[16:38] Let's check.
[16:41] It's not working.
[16:45] So lobby import.
[16:46] Oh, we need to import the terrain.
[16:51] Stage terrain and primitives.
[16:53] We need to set it to height.
[16:56] And now, at least we should have the points.
[17:11] Oh, we need to set it to height.
[17:15] Now we do have the points.
[17:21] So we can change here to file render.
[17:25] Or preview.
[17:26] That's much faster.
[17:30] So in the let's merge these inputs with the trees.
[17:40] So we have these trees all over the place.
[17:42] I want to have them here on the sides of the road.
[17:46] And we do have a mask for that.
[17:50] Let's go to the density and go to side mask.
[17:55] And yeah, now is working as we want.


### Randomizing rotation and scale [18:03]
**Transcript (timestamped):**
[18:05] So now you can see all the trees are facing the same direction.
[18:08] Have the same orientation.
[18:11] And I want to change that.
[18:12] Give it some random rotation.
[18:14] So let's go to the instacer.
[18:17] Let's spin this view.
[18:19] Go to the instacer and create an attribute triangle.
[18:26] So let's start by creating a random vector.
[18:34] The vector.
[18:36] Let's call it R.
[18:39] It's equal to a vector.
[18:43] Vector, if I can type.
[18:48] Let's give it a random function to the points.
[18:56] And create a control for it.
[18:59] All seed.
[19:02] And let's close one, two.
[19:08] So let's create another vector this time for the mean and max rotations.
[19:18] We will feed them in the range of 0 to 1.
[19:24] Let's create the controls.
[19:27] Rotation mean.
[19:32] It's not foot, but fit.
[19:35] And rotation max.
[19:40] Should be like this.
[19:43] Let's create a matrix 3.
[19:45] So we can manipulate the vectors.
[19:52] And now let's rotate those values.
[20:03] The radians.
[20:07] First time the rotation max.
[20:13] And we want to set it on the first axis.
[20:18] Selects.
[20:21] This should do.
[20:25] And do the same for the y and z.
[20:29] Just changing here.
[20:36] So let's orient them.
[20:40] This is where the rotations happen.
[20:43] Whatternion.
[20:47] And this should do the trick.
[20:51] Let's test it.
[20:52] Let's hit this button to create the controls.
[20:56] And let's go minus 360 to 360.
[21:02] And yeah, it's working.
[21:06] We can also rotate it on the x and on the z.
[21:12] Minus 80 to 80.
[21:14] And we get these those random rotations.
[21:18] So we might need a weight.
[21:24] A weight to orient the instances along the normal of the surface.
[21:30] So let's create a control for that.
[21:34] Let's go create an integer.
[21:37] Called switch.
[21:41] And create the control.
[21:44] Called surface orient.
[21:51] It's not CH3.
[21:54] It's CHI.
[21:57] And so if the switch is equals to 1, we want to orient less equals.
[22:17] We don't conflict with the other orient.
[22:20] We'll use this function.
[22:23] And set it to the y axis.
[22:33] And the normal.
[22:39] Let's see if this is correct.
[22:44] And yeah, as you can see.
[22:47] Now it's oriented along the normal of the surface.
[22:53] And we can switch between those.
[22:55] This might be useful for other assets we will gather.
[23:12] While we're here, let's create some controls for the scale.
[23:21] So let's create a min scale.
[23:26] Min scale equals CHF or float.
[23:32] It's called min scale.
[23:38] Let's call it this one max scale.
[23:46] And now we want to create a random scale 501.
[23:57] The random function in the points.
[24:06] Let's see.
[24:18] And let's create it to the min scale.
[24:28] And the only thing left to do is to affect the b scale.
[24:33] So random scale.
[24:39] And yeah, this will create by default.
[24:44] By default it will be in the 0.
[24:47] But we can change that.
[24:51] Let's put something like 1.2 and 0.9.
[24:54] And we can change the zeal.
[25:02] So now that we have these controls, we might want to have access to them in the stage.


### Creating an interface for the random attributes [25:10]
**Transcript (timestamped):**
[25:19] So let's create an 0 and edit parameter in the face.
[25:25] And let's create a folder for the random rotation.
[25:36] Yeah, no, what?
[25:39] And from here, let's go to the Instensor and it will wrangle.
[25:45] And let's drag all these attributes.
[25:48] And we get a warning because we have this option enabled.
[25:52] So let's disable and let's drag it.
[25:56] Seeds, let's call it rotation min and rotation max.
[26:07] Let's add a spacer between the inputs.
[26:16] And we have something like this.
[26:21] And for the surface, we can change it to what toggle.
[26:28] Yeah, it's easier.
[26:31] Okay, let's do the same for the random scale from nodes.
[26:41] Min scale, max scale.
[26:44] Let's put the zeal above and call it just zeal.
[26:51] And give it some space.
[26:59] Here, let's apply.
[27:05] Why is not working?
[27:08] Let's change it to simple here and also here.
[27:14] GenC is working.
[27:17] And the scale, we want probably to increase the range to 3.
[27:24] So if we want to control a bit more.
[27:32] Okay, we might want to have access to some scattering attributes.
[27:36] Let's create a new folder.
[27:38] Change it to simple and set the scatter options.
[27:43] And from the nodes, let's go to the instacer scatter options.
[27:50] And the number of points, let's apply the number of points.
[27:56] And let's also use the global seed.
[28:01] And we can just add a spacer.
[28:06] Okay, for the number of points, we might want to reduce it to 10,000s the range.
[28:19] Yeah, something like this.
[28:21] Maybe even 1000s.
[28:28] Something like this.
[28:30] And we can change the global seed.
[28:35] Okay.
[28:45] Let's just rename this to Instacer renderMizer.
[28:57] And we can connect it here.


### Working with variants in Solaris [29:01]
**Transcript (timestamped):**
[29:01] So now let's work on some grass.
[29:04] Let's go back to the object level.
[29:07] And let's load a file.
[29:11] Let's see.
[29:14] Can be this one, var one.
[29:17] Let's unpin it.
[29:21] And let's delete those colors.
[29:27] Where it's except your good color.
[29:30] And let's also transform it to point one.
[29:36] Something like this.
[29:39] And let's create a proxy.
[29:47] And match size.
[29:50] So we want to resize the box to the same size of the grass.
[29:56] So if we see this one, then template is.
[29:59] And see it's working.
[30:05] Okay.
[30:07] Let's create the output.
[30:10] Grass.
[30:12] Grass.
[30:15] Out grass.
[30:17] Roxy.
[30:22] And now let's create a subnetwork from this.
[30:25] Now let's call it to var one.
[30:29] Let's go here and change this to var two.
[30:36] Yep.
[30:37] And for the var three, I'm going to load another one instead of trick.
[30:42] But it won't matter because it will be just called var three.
[30:50] So we have these three different variations of grass.
[30:56] For this one, let's change it to point three.
[31:01] Let's see.
[31:02] Yeah, it's about the same size.
[31:05] Maybe point two.
[31:08] Maybe point three, maybe point two.
[31:12] Maybe point three.
[31:15] I'm going to keep going.
[31:18] Okay.
[31:21] Okay.
[31:22] Okay.
[31:23] Okay.
[31:24] Let's get back to the stage.
[31:27] And create a component geometry to load the assets.
[31:31] Let's go to an object merge.
[31:35] connect it to the default and now let's load here the proxy and we can see it's working
[31:49] let's just change the render and proxy yeah okay now we want to create the
[32:01] variation so let's put down component geometry very variance and in
[32:11] cell of inputs we want to change it to number and we know we have three so now
[32:19] this node has a built-in variable called let me see if I remember it's called
[32:27] at geo variance index I believe this is a name so we can copy this and let's
[32:41] proceed really loads the variations between beck ticks geo var variance index
[32:48] plus one because it starts from zero and our variance start from one so this
[32:56] should work it will give you a warning but it should not find yeah I changed
[33:04] you to final render and let's explore the variance to see if everything is loading
[33:12] and it's only loading geo that's maybe it's geo var index
[33:26] let's change it to kind of variance and it's only loading the first one for
[33:45] some reason or geo variance index oh we need to to set it also here not only there
[33:58] index index and now it's working so now we have all the three variance as you can
[34:21] see and let's instant them in the next one okay now we want to instant this grass on


### Instancing multiple meshes in Solaris [34:29]
**Transcript (timestamped):**
[34:33] our terrain so let's copy this and connect it here and as you can see it's it's not in
[34:48] the origin so we need to set it to zero but it's loading all the three variants in the same
[34:54] spots so on on all the points so what we need to do here is to set it to explore variance asset
[35:08] that still is loading every single it's loading the parent so we need to load the children
[35:18] like this and now it should work properly as you can see it's loading all the variance so for the grass
[35:30] let's just merge it here let's just see if this is working yeah now we're scattering on the same
[35:56] on the same mask what we want to do is to scatter instead on the front fields let's just a bit slow let's
[36:06] just change it to proxy and let's get back to object level to the geometry and right here where we
[36:18] have the fields divided we want to create and we want to create an L and call it out fields let's go
[36:32] back to the stage and on the insensor we can delete those two nodes disable the mask and let's
[36:45] load object merge let's load the geometry out fields
[36:58] and let's see if this is working and what we need to do to go back to the object level
[37:10] and we need to copy as we want to use this scatter but we need these attributes the unpack the
[37:20] attribute combined for the masks and the invert mask so let's copy these three nodes and on the
[37:29] insensor let's paste it here and this should work now we're scattering grass on the fields but we
[37:44] want to control all the specific groups we created so let's get back to it and in the scatter node
[37:55] let's change let's make sure we unpack the name we transfer the name and in the scatter we want to
[38:06] select let's say group zero let's increase the number of points and yeah risk scattering while we
[38:14] want okay as you see we have assets and everything is called assets so what we can do is for
[38:34] example here create a component output and let's call it a grass grass oh one
[38:49] is still working yeah and here we can call it grass oh one
[39:08] and is working
[39:09] so let's create the material for the grass so after the insensor let's
[39:26] let's let's create material library and in here let's create a standard surface


### Shading the grass [39:27]
**Transcript (timestamped):**
[39:42] let's call it grass net and let's load an image let me see if I can snap this one
[39:57] let's not this one yeah so let's load the alpiso and we can also place a color correct
[40:17] make sure you're using the Arnold nodes let's color and let's enable the shaker
[40:22] and now we can load the roughness and connect it to the specular roughness make sure
[40:38] set it to utility rock let's load also the normal
[40:47] and then the bump to the bump net vector normal
[40:58] and let's also load the translucency
[41:07] so we have we don't have translucency oh is not this texture let me check
[41:18] no not this one so let's go to models and grass textures that looks yeah this is one
[41:48] let's go here is roughness and here is normal and right here
[42:02] let's just paste it and go to translucency yeah now we can connect it to the subsurface color
[42:10] make sure we enable the invalid and in a subsurface let's set it I don't know to point for something like that
[42:22] and let's just assign it assign and assign to geometry and let's assign it
[42:32] this should work
[42:44] we barely can see any instance so let's increase the amount 30 000
[42:54] and yeah the material is working
[42:56] let's just go to the material increase the exposure
[43:11] play a bit with your shifts
[43:26] now we can see much because the render settings are very low so let's go back to the stage
[43:38] and after the right here let's create a render settings and set it to manual
[43:46] and go to the Arnold tab and change the
[43:53] change the camera samples let's say to four just to check
[44:07] so as you can see it's a bit too uniform so let's go to the material
[44:12] and let's set the G-turn on
[44:21] connect the albedo to the input let's go per object
[44:28] you can change these per object and let's connect it to the base color and change the video
[44:38] so you can see we can affect the colors
[44:48] let's also be with some in and max gain not much
[44:56] so now we have a bit more variation what we can do
[45:01] is to increase the amount of instances let's say 60 000
[45:11] so we will probably change a bit the colors but let's leave it like this for now
[45:32] so what we can do next is to copy this part


### Continue the scattering [45:35]
**Transcript (timestamped):**
[45:46] and here we still have the same
[45:50] directly
[45:51] you can Flow Settings
[45:53] control armies
[45:56] go same
[46:06] with any settings
[46:08] you can change the canvas
[46:11] mins
[46:13] you can also
[46:13] phases
[46:16] press 0.2
[46:25] and now let's connect it here
[46:34] and let's go in the Instensor and change the group
[46:39] let's go to group 1 for instance
[46:41] let's see
[46:52] it's working properly
[46:59] oh explore variants too
[47:06] let's see if we need to rename the materials
[47:11] we need to
[47:15] have other don't like
[47:19] and let's change the 1000
[47:24] yeah so instance are three proper types
[47:30] yeah now it's working
[47:34] change it to 30,000
[47:36] and let's see the materials
[47:42] yeah it's changing everything so we just need to rename this
[47:46] press meant
[47:51] and come here and
[47:55] this should be the trick
[48:00] you can just remove this
[48:02] yeah it's always working
[48:06] so let's not expose so much
[48:10] maybe something like this for now
[48:13] change the your shift
[48:17] to something like this
[48:19] maybe we can change this one too a bit
[48:24] okay
[48:25] and now let's create the last one
[48:35] so grads out tree
[48:38] explore variants tree
[48:39] explore variants tree
[48:41] grads out tree
[48:44] and the material library
[48:47] we need to change the tree
[48:49] and
[48:51] the rest is tree
[48:53] tree
[48:54] and tree
[48:56] and hole
[49:01] now we just need to go here
[49:03] and change it to group
[49:05] to
[49:15] now we have everything
[49:20] let's change it to 30,000
[49:24] how many we have here
[49:27] it's gonna be 46, 25
[49:33] and let's do a render
[49:41] let's change the material a bit
[49:49] so let's change again
[49:57] i'm not liking these brownish tones
[50:19] so
[50:30] so let's leave it like this for now
[50:33] and we can get back to roots
[50:37] let's continue now
[50:41] so once again create
[50:45] let's go back to the object level
[50:48] assets
[50:51] and let's create
[50:55] let's slow it in on a wig
[51:00] and
[51:02] which one it is
[51:03] there is this one
[51:05] nope
[51:07] nope
[51:08] so
[51:13] so let's slow the first one
[51:20] so let's just scream it again
[51:31] now
[51:34] whoosh
[51:37] And let's create a match size just to create the boxes box and right here.
[51:52] In here we can call it proxy.
[51:57] Okay now we can create a set network from it.
[52:03] Copy this all one.
[52:07] Let's go in here and change it to two.
[52:14] And in this one you can change it to three.
[52:20] Yeah.
[52:26] So on to three, let's go back to the stage.
[52:32] And let's create the switch node to disable temporarily the grasses.
[52:48] Let's copy this component geometry.
[52:52] Let's set this network and instead of loading the grass, let's load.
[53:02] Let's copy this part.
[53:06] And let's load the bush.
[53:12] And instead of this we're going to use the variable.
[53:21] Let's copy this.
[53:29] Let's copy this.
[53:32] Let's copy this.
[53:38] And right here.
[53:46] This would work.
[53:54] Let's see.
[53:58] Let's see.
[54:10] We have three variants.
[54:16] Let's check file render.
[54:20] Let's not loading the correct ones.
[54:24] So let's get back to these and see.
[54:34] This is a bit buggy.
[54:37] Let me check.
[54:39] Oh yeah, it's working.
[54:41] It's just that we have here an output that is showing up after the explore variants.
[54:49] But that's no problem.
[54:51] If we go to the instanceer and we change it to four bushes.
[55:04] Let's change it to preview.
[55:12] By the way, let's go to 500.
[55:18] As you can see, it's loading all the tree.
[55:22] Interredule elements.
[55:28] Okay, let's just not scatter on the same patterns.
[55:34] We want to scatter around the fields.
[55:40] So for that, let's go to the object context geometry.
[55:48] And I believe this one.
[55:54] Yeah, we want to scatter on this.
[55:58] So let's create an earlier.
[56:02] Let's go for out fields, outlines.
[56:08] Let's get back to the stage.
[56:14] Let's disable this for now.
[56:16] And right here.
[56:18] We want instead.
[56:22] The outfield outlines.
[56:26] We don't want to unpack neither of these.
[56:32] And in the scatter.
[56:42] We want to use these.
[56:46] So outfields.
[56:50] And right here.
[56:58] Let's check.
[57:00] Yeah, it's working.
[57:02] The points are just as small to see.
[57:06] So I think we need the number of points.
[57:10] For some reason, we are not loading the correct parts.
[57:18] Oh, I know why.
[57:22] It's loading the correct proxy, but I need to scale to fit.
[57:26] And disable the uniform scale.
[57:30] Scale to fit.
[57:34] And the last one.
[57:38] So now it should work.
[57:42] Let's just change the amount to something like this.
[57:52] Maybe a bit more.
[57:58] Let's also connect the switch now.
[58:10] And yeah, something like this.
[58:14] So I created all these materials outside recording.


### Multiple material assignment with material Library [58:15]
**Transcript (timestamped):**
[58:18] Just not to bore you with connecting textures.
[58:22] It just has the basic textures and some color correction and a color jitter.
[58:28] So let's now show you how to connect the materials.
[58:32] Let's out of field.
[58:34] And we have four.
[58:36] So what we can do here is go to the instances bushes.
[58:44] And we can see the name of the different parts.
[58:50] So we can just for the leaf.
[58:54] Do this.
[58:56] Leaf for one.
[59:02] Let's do video.
[59:08] Let's do start triangle one.
[59:14] And start triangle two.
[59:20] And this should do the trick.
[59:24] Let's see.
[59:32] And yeah, it's working.
[59:42] Sometimes the render region gets a bit buggy.
[59:48] Let's reset by opening the looping.
[59:58] And you can see the materials are not working.
[60:08] Let's enable everything.
[60:16] And outside recording, I'm going to fill the materials for the trees.
[60:26] And be right back.
[60:28] So I have here another tree that I want to scatter around.


### Scattering trees [60:32]
**Transcript (timestamped):**
[60:32] It's called tree two.
[60:34] Let's go to the stage.
[60:36] Let's copy one of these grasses.
[60:44] And instead of these, let's set it to three on two.
[60:58] We don't have any variants.
[61:04] Let's do it the proxy.
[61:06] And let's match tree up to three.
[61:12] Let's do a simple proxy.
[61:20] And scale it to feed.
[61:22] And we should have the tree.
[61:30] We don't need the expired variants.
[61:34] And we can just set it to default.
[61:36] And let's go to zero.
[61:40] The first input.
[61:44] Now it's gathering too many trees.
[61:48] Let's hope it will not crash.
[61:52] But it probably will.
[61:58] So we did crash.
[62:00] So we're back to the same part.
[62:04] We have the tree here in the component of the put.
[62:08] Let's go to default.
[62:10] And change it to the first input.
[62:16] Let's make sure we are on preview.
[62:20] Let me just copy the materials.
[62:24] So I have the materials for the tree.
[62:26] Let's clear it and assign it.
[62:30] So instance are six.
[62:36] And we can put leaves.
[62:48] And then let's start trunk.
[62:52] This should do.
[62:56] And in the instance are we don't want to scatter.
[63:00] Yeah, we want to scatter in the fields.
[63:04] So now we want to scatter not only on the group zero, but also in the one.
[63:14] So let's connect it to the main merge.
[63:22] And I don't know, let's also scatter on the group too.
[63:32] So we can just leave it like this.
[63:36] And then let's randomize something like this.
[63:44] Maybe a few more.
[63:52] Let's leave it like this.
[63:54] Then we have the materials.
[63:56] So let's see how it renders.
[64:04] So the materials are not working properly.
[64:14] Yeah, I assigned this should be here.
[64:22] Yeah, should be leaves.
[64:28] Yeah, it should work.
[64:36] This is able to light.
[64:40] I want to enable everything.
[64:44] And let's see how it goes the render.


### Render and good bye [64:47]
**Transcript (timestamped):**
[64:48] So I played a bit with the settings.
[64:52] Change the seed of the scattering.
[64:56] Change the bit the materials.
[64:58] And came up with this quick render.
[65:00] Nothing special, but we add the opportunity to look at salaries and how it works.
[65:06] How it is the workflow.
[65:08] So I hope you have learned something new.
[65:10] And if you have any questions or suggestions, please let me know.
[65:14] Thank you and see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_000.jpg
- [4:00] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_001.jpg
- [15:00] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_002.jpg
- [20:30] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_003.jpg
- [32:00] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_004.jpg
- [40:00] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_005.jpg
- [58:30] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_006.jpg
- [65:00] tutorials/frames/environment-creation-with-solaris-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Part 2 of a terrain series: bringing the SOP-built terrain/fields into **Solaris (LOPs)** to shade it with Arnold, then building a reusable **Component Geometry + Instancer** pipeline for multi-variant trees, grass, and bushes with VEX-driven random rotation/scale, USD `geo variant` switching, and per-part multi-material assignment.

### Summary
The terrain (a Null "outrain" wired to the SOP terrain output) is imported into an empty Solaris stage, lit with a Dome light (fixed light-format bug, Arnold camera samples set low for iteration), and shaded via an **Arnold Material Builder**: a Standard Surface driven by a State Vector (shading normal → Y component) feeding a Ramp for a height-based color mask, blended against Triplanar-projected grass/rock albedo/roughness textures (tuned via Triplanar's repetition and blend-softness controls), plus a displacement map — which required working around a bug where displacement wouldn't appear until switching from a plain material-library assignment to an explicit **Assign Material** LOP with the primitive path set directly to the geometry name. Trees/grass/bushes are each built the same way: a **Component Geometry** network references source geo via Object Merge, builds a lightweight proxy (Match Size + Box, "scale to fit") for viewport/bounds use, and for multi-variant assets (3 grass variants, tree/bush styles) a **Component Geometry Variants** node switches between subnetwork variants using the built-in `@geo_variant_index` USD variable (offset +1 since assets are numbered from 1 but the index starts at 0) — critically requiring **Explore Variants** set to load "children" (not "parent") for the variant switch to actually take effect downstream. Instancing uses a **Point Instancer**: source terrain points come from a **Scatter** LOP (density masked by the saved road/side/field masks from Part 1, selecting specific field `name`/group values), with an **Instancer** (Attribute Wrangle) VEX network adding fully exposed, user-facing controls — random rotation (per-axis min/max ranges, converted to radians, built into a Matrix3 → Quaternion via `orient()`), an optional "surface orient" toggle (switch between world-up rotation vs. aligning to the point's surface normal), and random uniform scale (min/max range affecting `pscale`) — all wired into an on-stage **Edit Parameter Interface** so the controls are exposed cleanly without digging into the network. Multiple instancers are layered/merged for different asset groups (trees on group 0, grass across the fields, bushes along field edges/outlines) each with their own scatter density mask, point count, and seed; per-part **multi-material assignment** on a single instanced mesh (e.g. a bush with separate leaf/stem-1/stem-2 parts) is done by targeting each named USD sub-primitive individually in the Material Assign / Instancer's per-primitive material bindings. The grass shader (Standard Surface: albedo, roughness, normal/bump, and translucency/subsurface-color textures with color correction, plus a per-instance **Color Jitter** varying hue/saturation/gain per instance for natural variation) is built the same way as the terrain shader. The video ends with a full scene combining terrain, randomized trees/grass/bushes across masked field regions, all Arnold-rendered.

### Key Steps
1. **Bring terrain into Solaris:** Null the SOP terrain output, switch the Scene view to Stage, reference the terrain in; add a **Dome Light**, fix its light-format setting, lower Arnold camera samples for fast iteration, and rotate the light for more dramatic lighting.
2. **Terrain shader:** Arnold Material Builder → Standard Surface; drive base color from a **State Vector** (shading normal) → extract Y → Ramp for a height-based gradient mask; layer grass/rock albedo textures via **Triplanar** (tune repetition/relative-reference scale and blend softness to fix visible tiling seams), plus a roughness texture (set to Raw utility colorspace) and a displacement texture.
3. **Fix displacement not appearing:** switch from a plain out-of-network material-library assignment to an explicit **Assign Material** LOP with the primitive path pointed directly at the geometry's name, and enable **Render Geometry Settings** (subdivision off, displacement on, padding ~3, zero-value ~0.5) on the target primitive.
4. **Texture rotation fix:** copy the Triplanar's "relative reference"/rotation parameters and paste them onto every texture node in the network so all textures rotate together and stop showing seams.
5. **Component Geometry for a tree:** Object Merge the source asset, build a proxy via **Match Size + Box** (uniform "scale to fit"), wrap in a Component Geometry network; connect to a **Point Instancer**'s first input, with terrain points scattered via **Scatter** (density from a saved mask, e.g. road-side mask) as the second input.
6. **Fix scatter showing no points:** Solaris/USD point-based scatter requires unpacking the USD geometry and correctly importing the terrain primitive (set to the geometry's actual name, e.g. "height") before Scatter will produce visible points.
7. **Randomize rotation/scale (Instancer VEX):** on the Instancer's attribute wrangle, build a random vector via `random()` seeded per point with a user-exposed seed; create min/max rotation range controls (`chf`/`fit` range mapping), build a **Matrix3** from the randomized per-axis rotation values (converted to radians) and derive a quaternion via `orient()`/`quaternion()` for the instance transform; add a toggle (`chi` integer switch) to optionally align instances to the surface **normal** instead of a fixed up-vector; add min/max scale range controls affecting `pscale` via another `random()` call.
8. **Expose controls on the stage:** use **Edit Parameter Interface** to drag the wrangle's rotation min/max/seed and scale min/max/seed parameters up to the LOP node itself (organized into folders), plus expose the Scatter's number-of-points and global-seed parameters — so all tuning happens without diving into subnetworks.
9. **Multi-variant assets via USD variants:** for grass (3 variants) or bush styles, build each variant as its own Component Geometry subnetwork (renamed var1/var2/var3), combine with a **Component Geometry Variants** LOP (set to "number" of variants = 3), and reference the correct one per point using the built-in `@geo_variant_index` primvar (offset +1 for 1-indexed asset numbering) inside a string expression built with backticks.
10. **Critical variant-loading fix:** **Explore Variants** must be set to load the "children" of the variant set (not the parent prim) for the per-point variant index to actually resolve to different geometry — loading the parent always shows the same (first) variant regardless of index.
11. **Layered multi-group scattering:** merge multiple Scatter+Instancer chains together for different asset categories (trees scattered on one field group, grass scattered broadly across all fields with per-group `name`/group masking reused from Part 1, bushes scattered along field-outline curves) — each pass reusing the Unpack + Combine (mask) + Invert Mask node chain copied from the terrain scatter setup, with its own point count and material assignment.
12. **Per-part multi-material assignment:** for compound assets with multiple named sub-parts (e.g. a bush's `leaf`, `stem_triangle1`, `stem_triangle2` prims), assign separate materials to each named part individually via the Instancer/Material Assign's per-primitive path targeting, rather than one material for the whole asset.
13. **Grass/foliage shading:** build a Standard Surface with albedo, roughness (Raw utility colorspace), normal/bump (Bump 2D → Vector Normal), and translucency (fed into Subsurface Color with subsurface weight ~0.4) textures; add a **Color Jitter** node (hue/saturation/gain variation, "per object"/per-instance) driven off the albedo for natural per-blade color variation across thousands of instances.
14. **Final render tuning:** raise Arnold camera samples for a real preview, adjust instance counts (thousands to tens of thousands), tweak per-material color-correct/jitter ranges, and randomize scatter seeds until the composition reads well.

### Houdini Nodes / VEX / Settings
LOPs: Reference, Dome Light, Arnold Material Builder, Standard Surface, State Vector (shading normal), Ramp, Triplaner (Triplanar — repetition/relative-reference, blend), Color Correct, Assign Material, Render Geometry Settings (subdivision/displacement/padding/zero-value), Material Library, Component Geometry, Component Geometry Variants (`@geo_variant_index` primvar), Explore Variants (children vs. parent loading mode), Scatter (density masking, group/name selection, number of points, global seed), Point Instancer, Attribute Wrangle on Instancer (VEX: `random()`, Matrix3, `orient()`/quaternion construction, `chf`/`chi` exposed parameters, `fit()` range remap), Edit Parameter Interface, Object Merge, Match Size, Merge, Color Jitter, Render Settings (Arnold camera samples, manual mode). SOPs referenced from Part 1: terrain heightfield, field/road/side masks, `name`/group attributes.

### Difficulty
Advanced — long, dense Solaris/USD production workflow requiring familiarity with LOPs concepts (component geometry, variants, primvars), Arnold shading networks, and VEX-driven instance randomization.

### Houdini Version
19.5 (references Solaris/LOPs and Component Geometry Variants workflow consistent with Houdini 19.5-era USD tooling; uses Arnold, not Karma).

### Tags
#solaris #lops #usd #scattering #instancing #vex #materials #shaders #arnold #procedural #environment #advanced

---

## Related Tutorials
Direct continuation of environment-creation-with-houdini---part-1.md (same terrain/fields project, same author) — cross-link explicitly. Also cross-link with any other cgside Solaris/LOPs or scattering/instancing tutorials once extracted from this batch.
