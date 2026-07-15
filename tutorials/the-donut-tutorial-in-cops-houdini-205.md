---
title: The Donut Tutorial in Cops | Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=meX4fLnITR0
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.301"
tags: [cops, copernicus, uvs, procedural-textures, tile-pattern, karma, food, donut]
extraction_status: complete
frames_dir: tutorials/frames/the-donut-tutorial-in-cops-houdini-205/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# The Donut Tutorial in Cops | Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=meX4fLnITR0)
**Author:** cgside
**Duration:** 42m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome!
[0:04] So in this video we're going to be building the Zonod from scratch, mostly using Cubs.
[0:10] This is based on a tutorial by Daniel Tiger on the Nvidia Studio channel on YouTube.
[0:18] And we're not going to be following step by step that tutorial.
[0:25] There will be a few shortcuts and we will just create the basic setup.
[0:33] So yeah, let's get started!
[0:35] Okay, let's start by dropping a geometry container and a Cubs network.
[0:44] And the first thing we're going to do is to build our Zonod shape and our Udvis.
[0:50] So let's create a subimport, drop down a torus and we will set 32 by 64 to have the square dot.
[1:05] Now we're going to UV.
[1:10] So for that I'm going to create a...
[1:12] Now I'm going to set select here the seams.
[1:18] So I'm going to select this one and this one in the middle.
[1:24] So click on an edge, shift A and it will select the loop.
[1:33] So let's press top and group and let's call it seams.
[1:41] And from there we can just see we flatten this.
[1:49] And this one look much.
[1:52] We need to select the seams and disable manual layout.
[1:58] Let's see how they look.
[2:00] So we want to rectify.
[2:04] We won't have perfect UVs but it will be close enough.
[2:11] So now we need to stretch these UVs so they fill the entire UV area, UV tile.
[2:24] So I'm not aware of any tool in Odinita.
[2:28] Does that by default?
[2:30] So I'm going to just create a wrangle and this will be really simple.
[2:36] We will just create unwrap to geo.
[2:40] So geo unwrap.
[2:43] So we can get the bounds.
[2:48] And we need this to be on the vertices.
[2:54] So make sure we have everything.
[2:58] And let's create a variable for our bounding box max.
[3:06] So get bounding box max geo.
[3:13] And now we just need to assign that to the UVs.
[3:17] So set in the x we won't do anything.
[3:25] And on the z will be zero.
[3:30] And on the y we will just stretch it.
[3:33] So we will start with the initial value.
[3:39] So you V dot y and here we need your V dot x.
[3:45] And we will divide it by the bounding box max dot y.
[3:53] So this should do the trick.
[3:57] Let's see if it did stretch the UVs.
[4:05] And as you can see it's also upside down.
[4:10] So what we might do is to negate this and do the same for this one.
[4:19] But now they are out of the one, the first style.
[4:25] So what we can do is to add one in the x.
[4:29] And add one in the y or in the V, you and V.
[4:35] So a bit of a stretch in here but hopefully you learn something new with this setup.
[4:44] So now let's create some basic information with a mountain.
[4:51] And I'm going to this place it just point to two.
[4:55] I'm going to follow some values but feel free to use your own setup.
[5:02] I encourage you to create your own setup.
[5:06] And I'm going to just really hard code them.
[5:12] And as you can see we have some deformation.
[5:17] So now let's create an output node which is always advised.
[5:22] Well otherwise we might have to display flag on another node.
[5:30] And this way it will always evaluate the last node.
[5:34] So let's place a sub divide.
[5:36] Let's see our V's.
[5:39] Let's place a sub divide.
[5:41] For now let's keep it a tree and maybe we can increase it later.
[5:47] And let's also place a normal.
[5:52] And that's our setup done.
[5:59] So let's start now by creating a Franklin voice.
[6:04] We will create first the icing mask.
[6:08] So I'm going to create a fractal noise and change the element size to point 0479.
[6:18] Just a number I have.
[6:21] And I'm going to change, I'm going to stretch it so we can have those drips of the icing.
[6:29] So about four.
[6:31] And we can, I'm not sure why this offset doesn't really work.
[6:38] So for that I'm going to create a check 3D noise until you can animate and offset it.
[6:49] So you can offset it in here.
[6:53] And I might reduce the liquidity.
[7:01] And also the reference.
[7:05] So something like this.
[7:07] Then I'm going to blur it.
[7:12] And you will see in a bit where we're coming with this.
[7:16] If you watch that, then you'll tie the tutorial.
[7:19] You will be very aware of what we're doing.
[7:25] So I'm going to blur it just a little bit.
[7:28] And create a ramp.
[7:32] Set it to vertical.
[7:36] And let me see.
[7:38] I'm going to change the position of the ramp.
[7:44] So something like this.
[7:48] And now I'm going to blend it.
[7:53] So blend this to
[7:57] hooks. And I'm going to change it to overlay.
[8:04] So we're starting to create that dripping pattern.
[8:09] So now we need to tighten this mask.
[8:15] So for that I'm going to use a remap.
[8:20] And I'm going to change
[8:27] these values.
[8:32] Something like this.
[8:35] I'm not going to follow exactly.
[8:38] So this will be fine.
[8:43] And from here, we can actually make these even sharper.
[8:50] So we want it ties.
[8:53] One ties, one ties are
[8:56] and change the segments too.
[8:59] So we get a sharp premise.
[9:02] So when you know that we haven't talked about before.
[9:08] And what else?
[9:11] Now we can start to...
[9:15] Let's preview these in our mesh.
[9:20] So preview material.
[9:22] Create a geometry and place...
[9:25] For now, let's place it in the base color.
[9:30] So we get something like this.
[9:36] And we might end up changing this.
[9:42] So we need to create some extra drips.
[9:47] And for that, I'm going to
[9:54] organize this and after the blends.
[9:59] I'm going to create a remap.
[10:04] And we're going to change this to here.
[10:08] Maybe tighten a bit the mask.
[10:11] So a bit more maybe.
[10:18] And we will create a tile pattern.
[10:22] So let's create a tile pattern.
[10:27] And we will change the divisions to 18.
[10:32] Change this to compound and act.
[10:36] Which is the closest I found to the draping shape.
[10:42] And let's change the radius.
[10:47] And we will create some jittering.
[10:52] So about 0.4.
[10:57] And play with the seeds.
[11:03] And we want to play with the size to...
[11:07] So let's change this to varying and variation to about 0.3 on the size.
[11:16] And we will change this vertical scale to 2.7.
[11:22] So we have these elongated shapes.
[11:25] And maybe play with the seeds.
[11:28] So in my example I add to 31.
[11:34] And I believe that's all.
[11:39] So now we will use this map as a mask as you can see.
[11:46] And we can create a street blur to elongate it even more.
[11:59] Maybe change the angle to 90.
[12:05] And the rest is fine.
[12:09] And we can create some distortion also.
[12:13] Let's move this to a lot of the way.
[12:16] And create a distort.
[12:20] And fractal noise.
[12:22] Change this to UV.
[12:30] And center to 0.
[12:32] So we have both positive and negative values.
[12:38] So let's change the scale to 1.
[12:42] And we will play with the size of the noise.
[12:45] And with the amplitude.
[12:47] So size wise we can set it to .05.
[12:52] And the amplitude really small .062.
[12:57] So we have something like this.
[13:00] Maybe you can play with the offset.
[13:02] Now here the offset works for some reason.
[13:09] Maybe we decrease the roughness to .1.
[13:15] Something like this.
[13:17] And now we can again quantitize and change the segments to .2.
[13:26] So we have a very sharp mask.
[13:31] So now we will blend this with original mask.
[13:39] So we are going to grab this one.
[13:47] And this one.
[13:50] And set it in this case to max.
[13:54] And we need to transform them down.
[13:59] So let's move them down.
[14:01] And I'm going to move it to .05.
[14:14] Now of course this doesn't line up with my initial setup.
[14:23] Let me see what I've done differently here.
[14:31] Let me check.
[14:35] Well we can move on because we will actually create some mask after this.
[14:46] So for now let's leave it like that.
[14:52] And we will equalize.
[15:01] And let's make sure.
[15:16] Let's equalize also here.
[15:23] Hmm.
[15:27] So let's remove this one.
[15:31] Let's see.
[15:33] Why is this?
[15:35] Maybe we need to play here with a remap.
[15:40] Nope.
[15:45] Let's see.
[15:49] We want floor.
[15:50] Let's go to get this issue.
[16:02] Let me just reset.
[16:04] See if that's something I'm missing.
[16:08] Maybe change this to multiply or add.
[16:13] And so we will actually remove this quantitize from here.
[16:23] And.
[16:27] And from here.
[16:31] And we can do it afterwards.
[16:35] So something like this.
[16:37] It's different from my initial setup.
[16:39] I'm not sure what's going on, but this seems to work out well.
[16:45] Let's preview this.
[16:55] So.
[17:03] We're landing.
[17:04] What's going on in here?
[17:07] Let me reset the viewpoints.
[17:11] And unplug.
[17:13] And plug again.
[17:16] So now it's working.
[17:19] So we will need to work a bit more on this mess.
[17:25] So.
[17:30] Now we will create some.
[17:32] Adds detect.
[17:38] And the default one will be fine.
[17:44] And let's change the details to .5.
[17:50] And blur a bit.
[17:53] .1485.
[17:56] .1585.
[17:59] And we don't want this to repeat.
[18:02] So let's create a layer properties.
[18:07] And change this to const.
[18:12] Clamp.
[18:14] I believe I changed it to clamp.
[18:16] Yes.
[18:18] And now let's blend with the initial setup.
[18:21] We're just trying to round out these initial shapes.
[18:26] .
[18:28] So we will blend it as .
[18:32] So as you can see, the effect it has.
[18:38] And.
[18:40] I'm going to totally change.
[18:43] Let me check.
[18:48] So you need actually to move this.
[18:56] .
[18:58] Let's change the radius.
[19:07] And maybe move this a bit more down.
[19:14] Oh, I know what is happening.
[19:18] In my initial setup, I am actually
[19:22] .
[19:24] blasting a few.
[19:40] I am burning.
[19:41] Yes, I'm burning a few shapes.
[19:46] So.
[19:52] You can remove a few.
[19:57] Something like this.
[20:01] Now is looking better.
[20:05] We'll move this in a bit.
[20:09] So for now, let's continue with this one.
[20:13] .
[20:18] And I might want to move these down a bit.
[20:26] So that's our main issue.
[20:32] And.
[20:36] Let's see.
[20:37] Let's move also these down.
[20:44] And maybe reduce the radius.
[20:57] And increase the repetitions.
[21:03] And we need to move these again up.
[21:09] So .5.
[21:14] So something like this.
[21:19] Let's see.
[21:28] There's a lot of tweaking.
[21:38] Maybe we don't move it so much.
[21:44] And.
[21:46] By springing.
[22:01] Let's continue with this one now.
[22:04] So we don't get stuck in here.
[22:09] So now I want to create the effect on the inside.
[22:15] So.
[22:18] For that, I'm going to first create a mask.
[22:22] So with a ramp.
[22:26] I'm going to change it to vertical.
[22:31] And change this to constant.
[22:33] And.
[22:37] And.
[22:39] I'm going to mask the top part.
[22:46] So create a constant.
[22:50] Set it to black.
[22:54] And create this mask.
[22:58] Something like this.
[23:00] I'm going to create a transform to the
[23:03] to mirror this part in here.
[23:10] And I'm going to rotate this 180.
[23:16] And move this by minus 0.8.
[23:21] So it will wrap around.
[23:26] And then I'm going to blend.
[23:30] With the modes set.
[23:35] Maxing.
[23:38] Something like this.
[23:42] And let's check the results as you can see.
[23:46] It's creating that.
[23:48] Interior detail.
[23:50] Again, due to the Yoviz, this will.
[23:54] Repeat a bit more on the inside because the Yoviz are.
[23:59] Stretching in a way.
[24:02] So there's no perfect way of unwrapping donuts or a sphere.
[24:08] As far as I know.
[24:11] This is the.
[24:13] The best approach I believe.
[24:15] So.
[24:18] I'm still thinking about this.
[24:21] Maybe.
[24:22] Let me see.
[24:26] Maybe we can increase.
[24:30] I can increase the.
[24:34] The size.
[24:38] So something like this.
[24:40] Let's see.
[24:44] It's okay, but instead of increasing the size, let's decrease it.
[24:52] And increase the strict blur.
[25:00] Let's see.
[25:08] For some reason, it's not updating.
[25:13] Let me check if I disable.
[25:23] I always quantitize.
[25:26] So.
[25:30] We might quantitize here.
[25:37] And set it to.
[25:43] And let's see.
[25:50] Let's increase again.
[25:53] This.
[25:59] And I'm not sure this is updating.
[26:02] So I'm going to just.
[26:04] Remove.
[26:08] And this should be working now.
[26:23] Looks like I'm having some issues.
[26:26] This.
[26:29] This is not.
[26:31] Updating properly.
[26:35] So let me reconnect this.
[26:40] Let's keep this for now.
[26:45] And we have done the flipping.
[26:48] Now let's maybe work on some colors.
[26:58] So let's create.
[27:00] Let's do that in the next parts.
[27:04] So let's tweak these a little bit.
[27:08] So starting with these.
[27:11] And let's maybe move these.
[27:17] If it's right time.
[27:23] And let's change this.
[27:26] We mark.
[27:35] Let's maybe do this.
[27:37] Which is the tile pattern.
[27:42] And let's say we like this for now.
[27:47] So let's create some color.
[27:50] So I'm going to start with the fractal noise.
[27:59] And I'm going to change this.
[28:01] This can stay at point one.
[28:04] I'm going to reduce the octaves.
[28:09] And increase the bit to roughness.
[28:15] And this will be fine.
[28:18] Now let's duplicate it.
[28:23] And let's change the element size to a very low number.
[28:30] So we will.
[28:33] Decrease the octaves.
[28:36] And increase the roughness to point nine.
[28:39] So something like this.
[28:42] Now we will blend it.
[28:51] And change it to multiply.
[28:57] And maybe reduce the opacity.
[29:02] And now create a model toward you.
[29:14] And I'm going to create here some colors that I have been from before.
[29:23] So I'm going to drag this to about here.
[29:27] And this one to here.
[29:29] To create some contrast.
[29:34] And loading the other color.
[29:45] This will be the download base.
[29:49] Now let's create a blend.
[29:51] And this will be our background.
[30:00] And create a constant.
[30:03] And our constant will be our chocolate.
[30:10] So we'll change it to RGB.
[30:14] And as a mask, we will use.
[30:26] A blurred version.
[30:31] So let's just reduce it to a little bit.
[30:40] And connect it in here.
[30:44] And this will be our base color.
[30:51] So it doesn't look that bad, right?
[30:55] We just need to tweak it a little bit.
[30:59] So let's blur it a bit more for the height.
[31:04] So point O O 9.
[31:11] And connect it to the height.
[31:16] And this will be way too much.
[31:22] And we will change it.
[31:24] And I point O to it.
[31:30] So something like this.
[31:32] Next we can increase the resolution of the mesh and the texturing.
[31:38] But for now, let's keep it this way.
[31:45] So we can start to create the details.
[31:52] So the sprinkles.
[31:55] And let me see.
[31:57] Yeah, we can do that.
[31:59] So let's create a SDR shape.
[32:06] And we have one here that will be
[32:10] really good for this, which is a line.
[32:12] And we add thickness.
[32:15] And the lines.
[32:16] Let's change it to point 9.
[32:21] And create a mono SDR tomorrow.
[32:32] And now we can create a tile pattern.
[32:37] And connect this to the stamp.
[32:42] And we can just increase maybe the regions.
[32:46] Change this uniform G-Term.
[32:53] Maybe not so much.
[32:57] And change the offset.
[33:01] The seat.
[33:03] And rotate this by 180 and set it to varying.
[33:10] Or just set this one to zero and increase the rotation variation.
[33:18] And now we can play with offset.
[33:21] And since they are overlapping a bit, we can change this to other bounds.
[33:26] Change again to 20.
[33:29] This will be a bit better.
[33:31] Not perfect, but maybe we can decrease the G-Term.
[33:40] And now let's connect
[33:46] which one, this one, this mask from the height to the point mask.
[33:54] And let's save some more space.
[34:01] And we will blur this a bit since we're going to connect this to the height.
[34:07] So not too much.
[34:10] Maybe the default settings will be fine.
[34:13] Create a multiply constant.
[34:15] So we can decrease the height.
[34:18] And let's set it over the base height.
[34:25] So I'm going to decrease the height.
[34:30] Brightness to 0.6.
[34:37] Just decrease the bit height.
[34:41] And change the height now.
[34:44] And then this height.
[34:51] So this is starting to look like something.
[34:56] Now we will create the colors.
[35:01] So for that, I'm going to pick this one.
[35:07] Create the RGB.
[35:10] RGB.
[35:14] Then brand the RGB.
[35:18] That's what I want.
[35:19] And connect the ID to the seeds.
[35:22] And I believe I used blackbody.
[35:31] And I'm going to multiply it.
[35:36] So I get rid of the yellow color on the background.
[35:40] I'm going to multiply this by the tiles.
[35:49] So something like this.
[35:53] Now we can add it to the color.
[36:01] So, return it.
[36:06] So this will be just fine.
[36:20] And let's check the results.
[36:25] So starting to look like the final results.
[36:29] Now I'm going to actually increase the resolution to 2K.
[36:41] Hopefully it updated.
[36:45] And also increase the subdivisions to 4.
[36:50] So we start to see a bit better our results.
[36:54] So as you can see some of the shapes are bleeding out.
[37:03] So we can just maybe use this one as a mask.
[37:15] And we need to use the same for the height.
[37:20] So when we do the adds,
[37:25] we need to use this as a mask too.
[37:31] Let's see if I can use this one.
[37:36] Now it's better to use the color one, yes.
[37:40] So, all right, let's now work a bit on the normal.
[37:53] So I'm going to start with this texture in here.
[37:57] And create a archivist tomorrow.
[38:08] And I turn on the normal.
[38:16] And I'm going to decrease to 0.25.
[38:27] Create a fat noise.
[38:42] And I'm going to decrease the element size to 0.2
[38:47] and change this to 0.1.2.
[38:52] And this should be fine.
[38:58] Create another right normal.
[39:01] This will be for our shoplets.
[39:05] And for this one, we actually want to develop 0.6.
[39:18] Now we can blend this.
[39:22] Oops, this one in here.
[39:30] And we will use as a mask this one.
[39:36] Now we can connect this to the normal.
[39:39] And of course, we need to decrease it quite a bit.
[39:52] So, 0.03.
[39:56] So we have some displacement, some lot of mapping.
[40:00] So, now we can finally work on the roughness map.
[40:12] So, let's create a remap.
[40:16] A remap will be just fine.
[40:22] And
[40:23] let's change this output mean to 0.5.
[40:39] And this is the shoplets to be.
[40:43] So, the shoplet will be slightly shinier.
[40:47] So, about 0.3, this will be fine.
[40:51] Let's connect it to the roughness.
[40:55] This is a very simple roughness map.
[41:00] And this is basically our final result.
[41:06] Let me maybe, maybe we can.
[41:10] And again, guys, this outer draping shape is not the best.
[41:18] As I tried to change it a bit, but I'm not gonna bother.
[41:26] So, I'm just going to risk something in here.
[41:32] Change this to 5.
[41:35] And let's see if this works.
[41:40] And it does.
[41:43] And as you can see, we have finer details with a very high resolution mesh.
[41:51] Then again, you can import these to salaries and render with karma, but I'm gonna leave it here.
[41:58] And feel free to tweet the final results.
[42:03] It's a bit random, but that's what we got today.
[42:09] Thank you for watching and I'll see you next time.



---

## Captured Frames

- [1:00] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_000.jpg
- [5:00] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_001.jpg
- [8:20] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_002.jpg
- [11:40] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_003.jpg
- [15:00] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_004.jpg
- [18:20] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_005.jpg
- [23:20] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_006.jpg
- [26:40] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_007.jpg
- [30:50] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_008.jpg
- [34:10] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_009.jpg
- [37:30] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_010.jpg
- [40:50] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_011.jpg
- [41:50] tutorials/frames/the-donut-tutorial-in-cops-houdini-205/frame_012.jpg

---

## Structured Notes

### Core Technique
Build a fully procedural chocolate-glazed donut with dripping icing entirely in **Copernicus (Cops)** — Houdini 20.5's new node-based image-processing context — using a custom UV-stretch wrangle (since no built-in tool fills a torus's UVs to the full 0-1 tile), layered Fractal Noise + Blend(Overlay) + Ramp masks for the drip shape, Tile Pattern nodes for both the drip-blob silhouette and the sprinkle scatter, and a mirrored/rotated Blend(Max) pass to fake interior detail from the same texture.

### Summary
A 32x64 Torus gets UVs via seam-grouped UV Flatten (rectified, imperfect but acceptable), then a custom wrangle stretches the UVs to fill the full UV tile — using `geo unwrap`, a detail-mode bounding-box-max query, and per-component UV assignment (`uv.x` unchanged, `uv.z = 0`, `uv.y` divided by the bounding-box Y max), with sign-flips and +1 offsets to fix upside-down/out-of-range results. Basic Mountain-based surface deformation, a Subdivide, and Normal round out the base SOP network, feeding a Cops network for texturing. The icing/drip mask starts as a Fractal Noise (small element size, vertically stretched ~4x) distorted by a Chip 3D Noise (animatable offset, tuned lacunarity/roughness), blurred slightly, then blended with a vertical Ramp using **Overlay** mode to create the initial dripping-pattern silhouette; Remap and Quantize (2 segments) sharpen it into a hard black/white mask. A second, independent drip-blob layer comes from a **Tile Pattern** node (Compound shape type, ~18 divisions, jittered position/size, vertical scale ~2.7 for elongated drips, tuned seed), stretched further with a directional Streak Blur (angle 90°), then distorted with a UV-centered Fractal Noise (small size/amplitude) before Quantizing again for a sharp edge; this is combined with the first mask via **Blend set to Max** and transformed down to align. An "Add Detail" node plus Layer Properties (Clamp mode) prevents tiling repetition and rounds out the shape when blended back into the main mask — extensive iterative tweaking (moving/scaling individual drip blobs, adjusting radius/repetition) refines the silhouette by eye. Interior surface detail is faked (since a torus/donut can't be perfectly UV-unwrapped) by building a top-masked Ramp, then **mirroring and rotating 180° + offsetting** a copy of the same mask, and blending the two with **Max** — approximating the underside drip detail from the same source pattern. Color comes from two Fractal Noise layers (different element sizes/octaves/roughness) blended with **Multiply**, feeding a Ramp for the caramel/dough base color, further blended against a solid chocolate-color Constant using the blurred drip mask as the mixing factor; height/displacement reuses a more-blurred version of the same mask at a small multiplier. Sprinkles are built from a thick Line (SDF/Mono SDF) fed into a **Tile Pattern** (varying rotation, jittered offset, adjusted bounds to reduce overlap), masked by the height map so they only appear on the icing, tinted per-instance via an RGB-from-ID node (Blackbody-style palette) multiplied by the tile mask to avoid background bleed-through, and layered into both the base color and height (with a Multiply Constant to keep sprinkle height subordinate to the main icing height) and a dedicated normal-map contribution. A final Remap builds the roughness map (icing base ~0.5, sprinkles shinier ~0.3), and bumping the overall Cops resolution to 2K plus increasing SOP subdivisions reveals finer detail in the final render — with the caveat, acknowledged by the author throughout, that Cops mask-tiling for the outer drip silhouette never looks fully convincing and needed constant hand-tweaking.

### Key Steps
1. **Base geometry + UVs**: Torus (32×64) → group seam edge-loops → UV Flatten (rectified) → custom wrangle to stretch UVs to fill the tile: `geo unwrap`, detail-mode bounding-box-max query, assign `uv.x` unchanged / `uv.z = 0` / `uv.y / bbox_max.y`, with sign flips and `+1` offsets to fix flipped/out-of-range results.
2. Add basic **Mountain** distortion (hardcoded values), **Subdivide** (3), **Normal**, and an explicit **Output** node (so the network doesn't depend on a display flag on an arbitrary node).
3. **Icing drip mask, layer 1**: Fractal Noise (small element size, ~4x vertical stretch) distorted by a **Chip 3D Noise** (animatable, tuned lacunarity/roughness/offset), Blur slightly, blend with a vertical **Ramp** using **Overlay** mode, then Remap + **Quantize** (2 segments) for a hard-edged mask.
4. **Icing drip mask, layer 2**: build a **Tile Pattern** (Compound shape, ~18 divisions, jitter ~0.4, size variation ~0.3, vertical scale ~2.7, tuned seed) for elongated drip-blob shapes; apply a **Streak Blur** (angle 90°) to elongate further, then distort with a UV-centered Fractal Noise (size ~0.05, amplitude ~0.062, roughness ~0.1) and Quantize (2 segments) for sharp edges.
5. **Combine masks**: Blend the two drip layers with mode **Max**, transform down (~0.05) to align; use an **Add Detail** node + **Layer Properties** (Clamp mode) to prevent tiling repetition, then blend back into the main mask to round out shapes — extensive manual tweaking (repositioning/scaling individual blobs) follows.
6. **Interior detail fake**: build a top-masked vertical Ramp, duplicate and **Transform** it (rotate 180°, offset ~-0.8) to wrap it to the opposite side, then **Blend (Max)** the two — approximating underside drip detail on the same UV-stretched torus (acknowledged as an imperfect workaround since donuts/toruses have no perfect UV solution).
7. **Color**: two Fractal Noise layers (different element size/octaves/roughness) blended with **Multiply**; feed a **Ramp** (dragged color stops) for the dough/caramel base; blend against a solid chocolate **Constant** (RGB) using a blurred version of the drip mask as the mixing factor for the base color.
8. **Height/displacement**: reuse a more heavily blurred copy of the drip mask at a small multiplier (~0.02) for subtle displacement.
9. **Sprinkles**: build a thick **Line** (SDF/Mono SDF shape), feed it into a **Tile Pattern** (varying rotation, jittered offset/seed, adjusted bounds to reduce overlap); mask by the height map so sprinkles only appear on icing; color via an **RGB from ID** node (Blackbody-style palette) multiplied by the tile mask to avoid background color bleed.
10. Layer sprinkle contributions into base color, height (via a **Multiply Constant** to keep sprinkle height subordinate to the main icing height), and a separate **normal-map** pass (Bump-style node, small strength ~0.03).
11. **Roughness**: a simple **Remap** (icing base ~0.5, sprinkles shinier ~0.3).
12. **Finishing**: preview via a Karma Preview Material with texture connections into base color/height/normal/roughness; increase Cops resolution to 2K and SOP subdivisions to 4 for finer render detail; import into Solaris and render with Karma for a full production pipeline (left as an exercise by the author).

### Houdini Nodes / VEX / Settings
Torus, Group (seams), UV Flatten, Attribute Wrangle (`geo unwrap`, detail bounding-box-max, UV component reassignment), Mountain, Subdivide, Normal, Output; Copernicus/Cops network: Fractal Noise (×3+ variants), Chip 3D Noise (animatable offset), Blur, Ramp (Overlay/Max blend modes), Remap, Quantize, Tile Pattern (×2 — drip blobs + sprinkles; Compound shape, jitter, size/rotation variation), Streak Blur, Distort (UV-centered Fractal Noise), Transform 2D (mirror/rotate/offset for interior fake), Add Detail + Layer Properties (Clamp, anti-tiling), Blend (Multiply/Max/Overlay modes), Constant (RGB chocolate color), Mono SDF (sprinkle line shape), RGB from ID (Blackbody palette), Multiply Constant, Bump/normal node, Karma Preview Material.

### Difficulty
Advanced (extensive iterative Cops mask-layering and manual tweaking; assumes comfort with Houdini 20.5's new node-based image/texture context).

### Houdini Version
20.5.301 (visible in viewport title bar) — the video explicitly showcases Houdini 20.5's new **Copernicus (Cops)** image context.

### Tags
cops, copernicus, uvs, procedural-textures, tile-pattern, karma, food, donut

---

## Related Tutorials
- [Procedural Pizza in COPs](procedural-pizza-in-cops.md) — companion food-shading-in-Cops tutorial from the same channel using similar Tile Pattern and Blend-mode techniques.
- [Wood Barrel Texturing in COPs](wood-barrel-texturing-in-cops.md) — shares the same Cops-based procedural texturing workflow applied to a different material.
- [Procedural Cliff Shapes in COPs - Free Lesson](procedural-cliff-shapes-in-cops-free-lesson.md) — related early Cops texturing tutorial from the same channel.
- [Procedural Graffiti in Houdini and COPS #mardini](procedural-graffiti-in-houdini-and-cops-mardini.md) — shares the layered Fractal-Noise/Ramp/Tile-Pattern drip-mask approach used here, applied there to graffiti drips.
