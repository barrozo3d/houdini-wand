---
title: Procedural Anisotropy in Karma
source: YouTube
url: https://www.youtube.com/watch?v=68WNINd8vE0
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-anisotropy-in-karma/
frame_count: 0
frame_status: pending-selection
---

# Procedural Anisotropy in Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=68WNINd8vE0)
**Author:** cgside
**Duration:** 30m37s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-anisotropy-in-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. Let's see how we can build something like this.
[0:05] Cake pan, we done isotropic reflections, we will model it, UV and shade it
[0:14] procedurally in karma. So let's get started by going to Solaris. Let's drop a


### Modeling and UV's [0:18]
**Transcript (timestamped):**
[0:24] substrate and we want to enable this panel and let's start by dropping a
[0:39] circle and we want it in the zx plane and reverse it and give it 64 subdivisions.
[0:54] Now we want to extrude it.
[1:03] Extrude and I'm gonna insert it.
[1:17] Let's see something like this and we want to keep the front group and let's
[1:29] extrude it again and we will extrude the front group.
[1:42] Now we want something like this and also insert it a little bit.
[1:55] Alright now we want to extrude the outside so let's drop the unshared edges.
[2:12] Let's say edges and let's see our normals. Now we want to create that
[2:29] typical tapering effect. So we will blend between these normals and another set of
[2:42] normals. So let's go with ourienta long curve and let's say this will be n.
[2:54] So we have this sort of normals. Let's call it n2.
[3:02] Now we can blend them so that you go to combine and we will have the destination to be
[3:14] normal and we want to blend it with ourienta long curve.
[3:21] And we don't want to add, we want to copy.
[3:27] So now the amount will be something like this.
[3:45] Something like this and let's extrude it.
[3:51] And we want to extrude the unshared and let's say point normal existing and let's copy
[4:07] these extrude and paste it in here.
[4:13] Let's see if there's not this one.
[4:22] Which one it is? Yes, it is this one.
[4:36] Now it's giving a different height so let's try something. Let's set it to edge.
[4:49] This way we can keep the same height.
[5:04] So now let's add the normal.
[5:10] And now we want to do you be these objects in two different ways. One along the cylinder in a
[5:29] cylindrical way and another one in an orthographic view in the y-axis.
[5:36] So let's split by normal, let's split parameters by normal.
[5:47] And let's say y and now we will create two nodes.
[6:05] So in here we have the cylindrical parts and here the y-projection.
[6:13] So let's go with the UV texture.
[6:20] Let's see the UVs we are on the Z-axis.
[6:24] I probably want to flip it and move it up again.
[6:33] This way we have it on the Z-axis one range.
[6:39] And in here we will create a range to create the seams.
[6:52] So let's go for points and we want to select two one.
[7:02] Select first one and copy this and select one out of 64.
[7:11] So something like this then promote it.
[7:20] We want to promote it for edges and the Rope 1, Rope 1 and only up elements in the boundary.
[7:35] And now we can create the UV flatten.
[7:45] And we want to select the seams.
[7:50] So this gives us something like this.
[7:53] So if we ratify everything and we disable that we will lay out.
[7:59] We will add the correct UVs.
[8:08] So now we can merge it.
[8:11] We'll probably need to work a bit more on the UVs since we are going to extrude and give it some thickness.
[8:21] That will create some problems.
[8:25] So let's find our Rope.
[8:30] These and go inside.
[8:40] Now we want to fuse it.
[8:49] And let's extrude it.
[8:56] And I'm going to extrude it by about about 0.44.
[9:18] And I want to output back.
[9:25] So let's see what this is looking.
[9:29] Overlapping UVs, let's find fun now.
[9:35] Now if we bevel this.
[9:43] And let's see if we want to flatten edges.
[9:54] Let's increase the bit.
[9:59] Let's re-trace the UVs.
[10:04] And let's see.
[10:09] As you can see it's creating some problems in here.
[10:15] Let's see also.
[10:17] It's also created in the poly extrude.
[10:21] So we need to split here.
[10:25] So we will split after the poly extrude.
[10:31] So split and split it by side-room.
[10:42] And now we can just re-tilt and create a noun.
[10:52] Let's see the UVs in here.
[10:54] As you can see this is the problematic part.
[10:59] So what we can do is just copy this.
[11:03] Note the UV texture.
[11:07] And paste it in here.
[11:12] So now it should be working fine.
[11:18] And let's merge it.
[11:23] And now we can fuse it again.
[11:35] And let's poly bevel.
[11:40] Let's see.
[11:41] That is creating the correct apology.
[11:48] The correct UVs in here.
[11:54] Let's see.
[11:55] Point out two.
[12:03] Maybe not so much.
[12:07] And let's also subdivide it.
[12:10] Otherwise it will create issues.
[12:14] And it will create some facetting in the rendering of an as a trophy reflections.
[12:22] So let's subdivide it.
[12:25] Maybe by two.
[12:30] That won't create any issues.
[12:33] Now you have this.
[12:35] That's fine.
[12:42] Let's create just an attribute.
[12:48] So we can use in shading.
[12:50] So let's say in the side group say we create a flow tetraboot outside.
[13:01] Let's see.
[13:05] Yeah.
[13:06] This should do it.
[13:11] And let's also soften the normals.
[13:19] Soft normals.
[13:21] This is always a good practice.
[13:24] We have the proper normals.
[13:28] And that's how we're modeling them.
[13:32] So now we will go through the shading part.


### Solaris Setup [13:37]
**Transcript (timestamped):**
[13:38] Let's pass the camera and focus it.
[13:44] Let's just create some notes, material library for the material.
[13:51] And let's create the diamond material.
[13:56] Let's all bend.
[14:02] Let all turn light.
[14:07] Let's assign it.
[14:11] Oops.
[14:14] Let's assign it to everything.
[14:19] Create the on-white.
[14:24] And I'm going to load.
[14:28] I will leave this one.
[14:29] Set it to light long.
[14:32] And create the polymer inner settings.
[14:37] Change it to XPU.
[14:39] And let's show it.
[14:44] Let's save it.
[14:46] And now let's go and see.
[14:51] The rendering.
[15:01] Maybe I want to change the direction of the light.
[15:08] So let's go.
[15:18] Something like this.
[15:21] And I also want to disable the environment lights and set it to dark.
[15:29] And also set it to view point size.
[15:35] So this should be good.
[15:38] Now let's go through the material creation.


### Procedural shading [15:43]
**Transcript (timestamped):**
[15:47] So let's create.
[15:54] Let's see how we'll do this.
[15:56] Let's create an elite and connect it to our surface.
[16:04] So we can focus on the texture.
[16:08] The first thing we need to do is to create a spiral ramp for these two parts.
[16:14] For the rounded parts.
[16:19] Or not rounded, but these flat parts that will have that typical anisotropy look.
[16:28] And then for this one we can just play with anisotropy rotation.
[16:35] So to create that spiral ramp is pre-dultav preset.
[16:44] So we will need to create around.
[16:47] So let's start by creating a texture coordinate node.
[16:53] And the form, I will just do the formula.
[17:00] And we will need a subtract.
[17:04] You can find this if you're looking to create this sort of effects.
[17:09] You can search for blender procedural texturing.
[17:15] And you will have a lot of this sorted out for you.
[17:19] And you just need to re-create it in material X.
[17:25] So rotate. That's what I usually do.
[17:28] We can keep here rotate.
[17:33] And we will need a distance.
[17:38] And set it to 0.5.
[17:44] So it grades from the center.
[17:52] And now we have to use these.
[17:57] Let's separate them.
[18:02] Just like a vector to float.
[18:07] Then we will need a 8.2.
[18:13] And connect it.
[18:16] And finally remap.
[18:23] And we will remap it to 0.1.
[18:30] But between minus dollar sign pi.
[18:36] And dollar sign pi.
[18:43] And now we just need to combine it.
[18:51] Combine to this one.
[18:58] And here this one.
[19:04] So let's check the result.
[19:10] As you can see we have duvis.
[19:21] That's a part of manner that we wanted.
[19:27] And we also have these ones just in here.
[19:36] That we like as our specular rotation.
[19:41] And this one will be used to map our noise to create the bumpy fact.
[19:49] So let's start to put this together.
[19:57] Let's first create our specular rotation.
[20:04] So we will need geometry property value.
[20:08] We need the sides.
[20:11] If you remember.
[20:17] We have the sides.
[20:22] So let's mix.
[20:27] And we will mix.
[20:31] The mixed factor will be the attributes.
[20:36] And we will mix.
[20:40] Days in the background.
[20:43] And let's check.
[20:49] And we want some some teleportation.
[20:52] Let's go.
[20:55] Something like this.
[20:57] And we will use the same rotation.
[21:02] So let's now use our material.
[21:07] And connect this to specular rotation.
[21:15] We will crease the metalness.
[21:19] The roughness.
[21:21] And then use a drop.
[21:25] And then we will have a loop.
[21:35] Now we have the desired results.
[21:38] You can see the typical and is a drop in reflections.
[21:43] You can increase or decrease the effect.
[21:50] And then in here the drop is going this way.
[21:55] Let's imagine the group's the bump map goes along the surface.
[22:01] And the reflection is something like this.
[22:06] In that direction.
[22:10] And of course we can control the rotation in here.
[22:24] In my case I found the battle point to the correct result.
[22:35] And let's continue on.
[22:38] Let's now create the bump effect.
[22:45] So for the side this is pretty easy.
[22:50] We can just create a unified noise to the.
[22:56] And let's connect it to our elite.
[23:06] Oops.
[23:09] Yeah.
[23:11] Now we just need to repeat it.
[23:14] Say 10, 10.
[23:16] We can leave it to purling.
[23:19] And let's say 10 by 600.
[23:23] And we get this sort of effect.
[23:29] You still can see some seams but won't be noticed.
[23:32] Not small in the when the effect is fully working.
[23:40] So obviously these groups are incorrect.
[23:44] We need them in a circular manner.
[23:46] That's why we created this sort of ramp.
[23:53] Oops.
[23:56] This one.
[23:59] I can connect it for some reason.
[24:09] So that's why we created this ramp.
[24:11] So we can fit it to a unified noise.
[24:18] So let's create another one.
[24:22] Let's connect the texture coordinates.
[24:25] And let's see.
[24:29] So obviously this part is incorrect.
[24:31] As you can see in the circular parts it's working pretty well.
[24:39] Let's maybe decrease it.
[24:43] So 6 by 400.
[24:48] 100.
[24:51] Let's say 400.
[24:54] And now we can just combine both.
[24:58] So where is our attribute?
[25:01] So we can mix.
[25:05] We can combine.
[25:10] So we have the sides.
[25:16] And we can combine.
[25:18] So the sides will be the the flat one.
[25:23] And this one in here is the background.
[25:27] And now we can check the result.
[25:32] So now everything should be working properly.
[25:39] So now what can we do to help a bit to give a better result to our anisotropy effect?
[25:52] Is to connect a bump map.
[25:56] So we can create a bump.
[26:00] Materialized bump.
[26:02] Connected to the height.
[26:04] And connect this to the normal.
[26:11] And now it will be two intents.
[26:15] So let's decrease it substantially.
[26:19] 0.001.
[26:23] Even that is a bit too much.
[26:26] 0.005.
[26:31] And clearly it will put a lot.
[26:36] And now we can even introduce some denoiser.
[26:48] And maybe give it some more samples.
[26:55] Let me check how much I used for bump.
[27:00] So maybe a bit more.
[27:04] 0.005.
[27:11] And you can always come back in here and rotate it.
[27:30] So something like this.
[27:41] And let's go to this one.
[27:45] Raise our rotation in here.
[28:05] And that's how it's looking.
[28:07] And we can add a burst metal.
[28:11] But maybe we can add an extra roughness to help sell out the look a bit more.
[28:24] So what can we do?
[28:27] Let's create a triplanar.
[28:31] And let me load the dirt texture.
[28:41] So I can show you how it looks.
[28:46] So let's go to the emission and surface.
[28:57] So we have this sort of texture.
[29:01] And now let's separate it.
[29:10] And now let's do like the blender folks do.
[29:17] With the mix node and we will mix.
[29:24] We will connect it to our specular roughness.
[29:32] Let's see.
[29:38] Obviously it's looking horrible.
[29:43] But we can just say between 0.25 and 0.45.
[29:55] Let's see how that looks.


### Final Result [30:02]
**Transcript (timestamped):**
[30:02] And as you can see that dirt map really helps to give some more life to it.
[30:12] So yeah that's basically what I wanted to share today.
[30:16] I hope you have learned something new.
[30:19] And I'm not saying this is the correct way to do things by any means.
[30:25] But it's the way I found out it works more or less okay.
[30:31] Okay guys thank you and see you next time.



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
