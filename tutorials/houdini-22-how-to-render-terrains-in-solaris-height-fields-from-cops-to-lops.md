---
title: Houdini 22 | How to Render Terrains in Solaris | Height Fields from COPs to LOPs
source: YouTube
url: https://www.youtube.com/watch?v=IeVvQt0bHQ0
author: Houdini
ingested: 2026-07-21
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-render-terrains-in-solaris-height-fields-from-cops-to-lops/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to Render Terrains in Solaris | Height Fields from COPs to LOPs

**Source:** [YouTube](https://www.youtube.com/watch?v=IeVvQt0bHQ0)
**Author:** Houdini
**Duration:** 18m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-render-terrains-in-solaris-height-fields-from-cops-to-lops <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this tutorial, you will learn how to render terrains created in COPs, as well as get familiar
[0:08] with some of the new rendering features in Houdini 22.
[0:12] You can start by opening the project file and follow along.
[0:18] We have this heightfield that we have created in the terrains how-to, so let's double-click
[0:24] on this one.
[0:26] We would find the actual COP network where this terrain was created.
[0:29] So if I double-click into this, you would find a familiar network from the other tutorial.
[0:36] Now there is one important thing that I'm going to adjust in this heightfield, and this
[0:42] would be this resolution parameter.
[0:45] So right now it is set on this first heightfield layer, but we actually want to control it
[0:51] on the COP network node itself.
[0:54] So I'm going to turn this off and let's go back.
[0:59] So now in the heightfield COPnet, I'm going to turn on the default resolution.
[1:07] And you would see that now we can control the amount of details of this terrain by changing
[1:13] this resolution through this menu.
[1:16] So I'm going to click on this one and let's say we want a higher resolution terrain, which
[1:20] is going to be 2K.
[1:23] Let's click on that one and you would see that now we have more details.
[1:26] And same would be with the 4K.
[1:27] So for the final render, I will be using the 4K resolution terrain.
[1:32] Now there is another important thing that we need to do in order to prepare this for
[1:37] rendering.
[1:38] So right now if I middle mouse click or if I just hover over and click on this displayed
[1:42] node info, you would see that this is actually not a mesh that we can render.
[1:49] This is actually a volume containing heightfield and color field.
[1:55] So we need to convert this to a mesh.
[1:57] So I'm going to put down, press Tab and type, convert heightfield.
[2:07] And now this will do an internal conversion.
[2:11] And now if I middle mouse click, you would see that I have 4 million polygons and now
[2:16] I have height and CD as geometry attribute.
[2:20] And we can also see that this is now a pretty dense mesh.
[2:26] The other thing you can do just to be safe is if you select this cop net, you can see
[2:32] there is this use external cop option.
[2:35] So you can enable this one and then if you double click on the cop net, by default, whichever
[2:43] node would be specified in that external cop, that node would be brought up to the
[2:50] upper level.
[2:51] So if, let's say you accidentally set this node to be visible and then with this one
[2:58] off, the cop net would just bring in the grid.
[3:02] So what if you went inside and you started looking at some of these nodes and then you
[3:06] went back and all of a sudden this is not now bringing our height field, it's just bringing
[3:13] some kind of color data.
[3:14] So this is why we can use this external cop.
[3:17] So let's turn this on once again.
[3:19] Let's double click and after the height field visualize, I'm going to create a null.
[3:24] So I'm going to press that and type null.
[3:28] And I'm going to plug in the geometry onto this null and I'm going to call this out
[3:33] to rain or render.
[3:37] And I'm going to select this node, press control C on my keyboard, go back and then
[3:43] put my mouse over there and press control V.
[3:47] So now no matter what I put my display flag on, so let's say I go back and put it here,
[3:54] this will always bring the terrain back.
[3:56] Okay.
[3:57] So now we have our terrain and we have the color attribute, but there are actually some
[4:03] more attributes that we can potentially use during the rendering stage.
[4:08] And I also wanted to show how you can bring those out of the cop net.
[4:12] So if we double click on the cop net again, we can see that there is this height field
[4:18] erode node and it actually has some of these extra attributes and fields that we can utilize
[4:26] in the render.
[4:27] So if I look at these individually, so for example to the flow, if I put null in here,
[4:35] you would see this gives us some kind of very interesting looking map that we can use
[4:43] as a mask or something else.
[4:45] Now in order to export these, we will need to plug them as extra layers for the height
[4:51] field visualize.
[4:53] But at the moment we can't plug in more than one, so we basically need to pack these into
[5:00] one cable.
[5:02] I'm going to hit Y and delete this and press tab and type cable, cable pack.
[5:10] So let's plug in the debris, let's plug in the sediment and the flow.
[5:15] And I'm going to put the display flag on here.
[5:18] And it's also very important to set fields from inputs.
[5:23] This will basically name them and the attributes would inherit these names.
[5:26] So now I have this packed cable that I can plug into layers.
[5:31] And now if I jump up, I can actually press the U key to go up.
[5:36] So now if I select the convert height field node and middle mouse click, you can see that
[5:40] now I have all these extra attributes that I can actually visualize here.
[5:45] So the debris is actually pretty cool.
[5:48] We can also take a look at the sediment.
[5:52] Okay.
[5:53] Now let's bring in this height field into Solaris for rendering.
[5:57] I'm going to press tab and type no.
[6:00] We're going to create an output checkpoint.
[6:05] Out.
[6:06] Rain.
[6:08] Or Solaris.
[6:12] Okay, I'm going to put my display flag on this node.
[6:15] And we can basically jump into the Solaris context by clicking and holding the
[6:21] OBJ and then choosing stage.
[6:23] And you can see now we are in Solaris or alternatively, if I jump back, we can press
[6:30] tab and type LOP network.
[6:33] And this is our lighting operators network, which will be another shortcut to Solaris.
[6:38] So if I double click on this one, you can see we're now again in Solaris.
[6:43] And to bring in our geometry, we can just do press tab and type scene import.
[6:51] So let's do scene import all.
[6:56] And you can see now our terrain is imported.
[6:59] If you have more than one object, you can actually specify what you want to bring in.
[7:03] So right now it's, everything is in this height field geometry container.
[7:09] But let's say you have other containers or cameras or light and you just want to
[7:13] bring in the height field, you just click on again.
[7:16] Let's choose this one except pattern and it will only bring in this geometry.
[7:22] Let's create a quick light.
[7:24] I'm going to press tab and type karma, karma physical sky.
[7:29] And let's plug this into the karma physical sky.
[7:34] I'm going to angle this to look from this crater towards those rocks.
[7:41] All right.
[7:43] And let's quickly create a camera from this view.
[7:50] And we can basically, we have the camera locked.
[7:53] So now I can just move it back a little bit.
[7:56] I'm going to uncheck the lock icon.
[7:58] So we can do a quick test render with karma XPU.
[8:03] So right now, if you don't see the lights in the viewport, make sure that you are
[8:11] previewing the scene lights.
[8:13] If I click on the scene lights, everything should start calculating and we should see
[8:18] our lighting.
[8:20] So I'm going to increase the intensity of this to something like 2.5.
[8:25] We can change the solar altitude.
[8:30] I want to use the atmosphere inside of the sky mode, the dome light, because I want to
[8:39] mimic some kind of distance haze and fog.
[8:43] So if I change the dome light to atmospheric, we would see something like this.
[8:47] And then if we click into the atmosphere settings, I can now adjust the Ray Lake scale
[8:54] and some of the scatter parameters.
[8:58] So I usually like to set the scale pretty high.
[9:02] And you can see we're starting to get this kind of hazy sky.
[9:06] And then we can increase the scatter distribution to something like 6.25.
[9:15] So these values usually work if your scene is set correctly.
[9:21] So another important thing is to make sure that your terrain is something that would
[9:28] be close to a real world scale terrain.
[9:34] So if I go into the scene import all, let's jump back into this height field.
[9:40] Let's double click.
[9:41] And I'm going to middle mouse click on this one.
[9:43] You can see this terrain right now is 1 kilometer by 1 kilometer, which I believe for
[9:49] the scale of this desert is a little bit too small.
[9:53] So it should be much bigger in the end in its location in 3D space.
[9:59] So let's jump back into Lops.
[10:01] Let's double click.
[10:02] And I'm going to put down a transform node after this.
[10:08] And let's scale this terrain five times.
[10:10] I'm going to press five in the uniform scale.
[10:15] And I'm going to press the scale.
[10:18] And you would notice that nothing happened.
[10:21] And that's mainly because the transform is a bit confused.
[10:25] We have to tell it to transform the mesh primitives.
[10:29] So in the transform node selected in the primitives box,
[10:35] we can click on the drop down menu and choose all mesh primitives.
[10:40] So now you can see the terrain has been scaled.
[10:43] Also for final composition, I have rotated this terrain minus 90 degrees in Y-axis.
[10:51] So you can also put down minus 90 to have a result similar to mine.
[10:57] And now we can select the camera and make sure it is locked.
[11:03] So you can see these red bars.
[11:05] And let's start zooming out to get back to our composition.
[11:09] And you would also notice that now the atmosphere is covering the terrain
[11:18] in a much more realistic way.
[11:20] We're getting this kind of very hazy fog in the back.
[11:26] So this is because now the terrain is much closer to what it be in real life.
[11:32] Now for the final camera, I actually have the numbers that I've set for final composition.
[11:39] Feel free to use any camera angle as you want, but I'm going to go ahead and put down these
[11:45] numbers quickly and get back.
[11:47] All right, so we are back and you can see these camera values.
[11:51] If you want exactly the same angle, you can just copy these values.
[11:55] After this one, let's choose the camera physical sky.
[12:00] And I'm going to go to the sun tab.
[12:03] And for the final render, I adjusted the solar azimuth to be 30 degrees.
[12:09] So we get this kind of sun from the screen right lighting up our terrain.
[12:17] And at this point, the lighting and the composition are set.
[12:22] So now we can take a look at the materials because right now this terrain doesn't have any.
[12:28] So we can press tab and type quick surface material.
[12:34] And let's select the material and we can just click and drop it to the terrain.
[12:42] Let's try it again.
[12:43] And it will ask us which geometry primitive we want to use.
[12:49] And I'm just going to choose height.
[12:51] So after dropping the material onto the terrain, you would see that it is actually very shiny.
[12:58] And what is going to happen by default, the quick surface material is going to read the
[13:03] display color attribute.
[13:07] But it has some specular and roughness set.
[13:11] And these are not really resembling what the deserted rock would be like.
[13:20] And we can change the roughness to a higher value, something like 0.75.
[13:25] Okay.
[13:26] So this is something much closer to what we're looking at.
[13:29] Now, if we want to render this terrain into the final image, we can increase the actual resolution
[13:37] from 2K to 4K and put on Karma render settings and render.
[13:41] So before we do that, I want to take a snapshot of what we have so we can compare.
[13:46] I'm going to go down and click on this hide snapshot strip.
[13:50] And I'm just going to click on snapshot to save the render at its current stage.
[13:55] Then let's select the scene import all.
[13:58] And I'm going to jump into the OBJ.
[14:00] I click on this jump icon.
[14:02] I can press space bar G to zoom into our terrain.
[14:06] And now we're going to add more details.
[14:09] So let's double click onto the height field.
[14:11] And as you can see, our cop net is currently set to resolution of 2K.
[14:15] So let's change this to be 4K.
[14:18] So now you can see our terrain is more detailed.
[14:21] We are getting much more fidelity in the erosion.
[14:25] And we can go back and start rendering this.
[14:28] So let's double click on the LOPnet.
[14:30] And at this point, Karma will start doing another render.
[14:37] I think we can just restart.
[14:39] Let's do restart render.
[14:41] And we will, I'm going to quickly pause the video.
[14:43] And then I'm going to do another snapshot.
[14:45] And we'll compare the two terrains, 2K to 4K.
[14:51] And then we will do additional things.
[14:54] All right.
[14:54] So the render is complete.
[14:55] I'm going to click on another snapshot.
[14:57] And let's just double click on one of these.
[14:59] So it will open up this window.
[15:02] And we can now basically compare.
[15:03] So this was the 2K render.
[15:06] And this is the 4K.
[15:07] You can see that we are getting way more details,
[15:10] especially in these areas and overall.
[15:13] And obviously 8K would get you even higher resolution result.
[15:18] So in order to render this to a final image,
[15:21] let's put down our Karma node.
[15:22] So let's press Tab and type Karma.
[15:25] And we want to choose Karma setup.
[15:28] So it will ask us if we want to precompile any shaders.
[15:31] Currently, we just have one simple quick surface material.
[15:34] So I'm going to do not precompile.
[15:38] And let's connect the assigned material to the Karma render settings.
[15:42] Put the display flag onto the Karma render settings.
[15:45] And if you have a strong CPU, you can keep it at CPU renderer
[15:51] and just up the samples to something like 16.
[15:53] In my case, I have a stronger GPU.
[15:55] So I'm going to use Karma XPU.
[15:59] And basically to do a final rendered image,
[16:03] you can click on this USB render op.
[16:05] And to render it into a separate window,
[16:08] you can click on render to Mplay.
[16:11] Otherwise, you can just click on render to disk.
[16:14] And this will be the directory where the image will be saved.
[16:18] So you can middle mouse click to see where exactly this will be going.
[16:22] It's important to make sure that the camera name is matching your camera.
[16:26] So this is going to be the camera it will use.
[16:29] And then additionally, before we wrap up,
[16:31] I just wanted to show you some of the new image filters
[16:34] that we have in Houdini 22.
[16:36] So if you click on filters, and then if you click on plus,
[16:41] it will add this new image filter that you can utilize
[16:44] and add some kind of interesting effects to your image before rendering.
[16:49] So we can add something like chromatic aberration, for example.
[16:55] So we can click on that.
[16:56] You can see this is a little bit extreme.
[16:58] So I usually divide the global distortion by 10.
[17:03] So we'll get some of the chromatic aberration.
[17:05] We can add some vignetting, something like this.
[17:10] So maybe let's do 0.75, 1.25, and 0.5 overall.
[17:20] So we get some kind of cinematic vignetting.
[17:24] And then we can also add another filter, something like tone mapping.
[17:30] We can tone map it as ASUS Filmic to make this a little bit more cinematic.
[17:37] So this is how you can basically add some tone mapping
[17:41] and other image filters to your final render.
[17:45] And then additionally, let's go ahead and let's click on render to end play.
[17:51] And now our final render is complete.
[17:53] And this is how you can export terrains from cops,
[17:57] import them into Solaris, and quickly render them with image filters.



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
