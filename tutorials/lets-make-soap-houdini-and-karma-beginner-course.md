---
title: Let's make soap! Houdini and Karma beginner course
source: YouTube
url: https://www.youtube.com/watch?v=Y-CjDhFmclQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/lets-make-soap-houdini-and-karma-beginner-course/
frame_count: 0
frame_status: pending-selection
---

# Let's make soap! Houdini and Karma beginner course

**Source:** [YouTube](https://www.youtube.com/watch?v=Y-CjDhFmclQ)
**Author:** cgside
**Duration:** 64m40s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py lets-make-soap-houdini-and-karma-beginner-course <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this one we're going to build the simple scene in Odini and rendering in Karma XPU.
[0:08] Hopefully it will be a beginner friendly tutorial as I'm going to do it step by step.
[0:15] And we will also touch in some intermediate topics like expressions and maybe some Vex.
[0:24] And yeah let's get started.


### Modeling the soap bar [0:27]
**Transcript (timestamped):**
[0:28] So let's start by dropping a geometry container.
[0:33] And I need to import the logo so I'm going to use a regions from image and leave all the default
[0:43] settings and paste. And I'm going to paste the image pad which I have in here.
[0:53] So something like this and let's wait.
[0:59] So since this takes a little bit to load I'm going to probably cache it. I'm just going to add this.
[1:08] Add a custom attribute and say the black color will be logo so we can select it later.
[1:16] So let's just file cache and remove the time dependent cache as we just want a single frame.
[1:26] Let's name it logo.
[1:27] And logo FC.
[1:37] And let's blast.
[1:42] And we will blast.
[1:44] Oops, do we have this?
[1:48] I forgot to add the name attribute.
[1:50] And now we can save and pick the logo.
[1:56] And we're going to delete all the attributes.
[1:58] So attribute delete, attribute delete.
[2:04] And we're going to just say delete unselected which will delete everything.
[2:11] And now we will create the soap.
[2:16] So let's create a box.
[2:22] Let me adjust the UI.
[2:26] And we will say 0.7 in x, 0.16 in y, and 0.4 in z.
[2:35] And we will add some subdivisions like 6, 3, and 4.
[2:41] Something like this to have it even.
[2:46] And now we're going to bevel it.
[2:52] And we don't want to bevel if we bevel everything.
[2:57] If we just bevel it will bevel everything.
[3:00] So we need to exclude the flat edges.
[3:02] So let's say utility.
[3:05] And for the size 0.9, and we will add some subdivisions, something like 3.
[3:16] And now we can place it with the logo.
[3:22] We can place the logo.
[3:25] I mean, we can place so much size.
[3:30] We can place the logo on top of this soap.
[3:36] So let's do mean.
[3:41] And max.
[3:45] And we will also say scale to fit.
[3:50] And probably move it a bit down.
[3:55] Let's move it a bit down.
[4:02] Minus 0.005.
[4:08] Just a little bit.
[4:09] And I'm going to transform it to scale it down.
[4:15] And I'm going to scale it down by 0.75.
[4:22] But we want to do it in the center.
[4:27] So we will use the centroid expression.
[4:30] So 0.75.
[4:32] So it doesn't sing in.
[4:37] Now I'm going to place an L.
[4:39] So we can reference it later.
[4:42] And I'm going to say it's front.
[4:47] And we're going to extrude it.
[4:53] So I'm going to extrude it by 0.02.
[4:59] 0.02.
[5:01] So this should be enough.
[5:07] And as you can see, we don't have the back faces.
[5:10] And as we want to intersect these two objects,
[5:15] so we will create a Boolean.
[5:18] We will also mirror in the Y axis in this case.
[5:24] And here's the trick.
[5:28] We are mirroring from the world origin.
[5:34] So 0.00.
[5:36] That's why we don't have the objects connected.
[5:40] So for that, we can say in the origin,
[5:43] we box 0, the Y mean.
[5:49] So we want to mirror at that, at the Y mean of the object.
[5:57] So the minimum bounding box.
[6:01] And now we can finally Boolean it.
[6:05] So let's create a Boolean.
[6:11] And we will say union.
[6:14] And connect this and this.
[6:18] Do I want to...
[6:20] So here's the thing.
[6:22] We can create a Boolean union in here.
[6:27] And this will totally be fine.
[6:31] As you can see, we can use this for final render.
[6:35] But I'm going to go a step further and do some remaching in this.
[6:41] So instead of Boolean union, I'm going to use a shatter mode.
[6:51] And as you can see, this creates these interior faces.
[6:55] So I'm going to use surface in here.
[6:59] So we get just this logo stamped out.
[7:03] And I'm also going to subdivide in here.
[7:06] So I have more information for the remaching algorithm.
[7:12] So I'm going to subdivide it by two.
[7:15] And I'm also going to create a group, a primitive group.
[7:21] And I'm going to call it soap base.
[7:30] And now we're going to create a connectivity.
[7:37] And we want it on the primitive.
[7:43] So we have something like this.
[7:49] I'm going to fuse it.
[7:56] And I'm going to fuse by a smaller value.
[8:02] So it doesn't fuse very close points.
[8:07] And I'm going also to triangulate.
[8:17] And doing a quad remach.
[8:19] You don't need to do this if you don't have it.
[8:23] But since I have it, I'm going to do it.
[8:29] You can totally do Boolean union and do a small bival afterwards.
[8:36] And it will be fine.
[8:37] But I'm going to just show you another technique that I saw.
[8:43] Also on a quick tip from CGWikis Discord.
[8:47] So I'm going to use 20,000.
[8:51] And use the class attributes.
[8:55] So it knows where to orient the polygons.
[8:59] So let's quad remesh it.
[9:01] You can use the trial version, by the way.
[9:04] That's what I'm using right now.
[9:05] But I'm going to totally buy this because it's worth it.
[9:10] It's a really great plugin.
[9:14] So as you can see, we have the polygons oriented.
[9:20] And I'm going to file cache it.
[9:23] So when you look at the file, you don't have to have this plugin.
[9:26] You can just use the file cache.
[9:28] And from here, I'm going to import the font.
[9:42] So we have this.
[9:45] I'm going to extrude it.
[9:49] And I'm going to set it by a little bit since we want to do a group transfer.
[10:05] So I don't want to spill out too many outside faces when we do a group transfer.
[10:13] So I'm going to remove output side.
[10:16] And remesh it a little bit so we have some more subdivisions.
[10:24] So if we do 0.05.
[10:30] And do some smoothing iterations.
[10:37] And we can group this.
[10:43] And the group transfer.
[10:52] And I'm going to remove this and transfer the group to.
[11:00] And you need to play a little bit with the values.
[11:02] I know a value of 0.0061.
[11:08] It will be just fine as you can see.
[11:15] As you can see, it's not working in here.
[11:17] So we might add a subdivision.
[11:21] So let's try to subdivide it.
[11:23] Since we did a remesh, we want to subdivide it with open subdiv loop.
[11:28] And let's say two.
[11:30] Let's see if that fixes that issue.
[11:32] And it does.
[11:34] Because we have some, as you can see, if we don't have this,
[11:38] it will not work properly the group transfer.
[11:42] Because we don't have enough geometry.
[11:46] So,
[11:48] extrude.
[11:53] And we will extrude the group to.
[11:57] And it's working fine.
[12:01] Let me just check something.
[12:07] And we will extrude by 0.03.
[12:11] 0.03.
[12:14] So it's up to you how much you want to extrude.
[12:17] I'm just trying to match my reference.
[12:21] And we will also bevel it.
[12:27] And we will bevel it by, let's first exclude the flat edges.
[12:35] I know a value of 89, it will work just fine.
[12:39] And 0.001, as I don't want too much beveling.
[12:45] And let's say three divisions.
[12:48] So it's, as you can see, this is working much better to do the beveling
[12:53] with proper topology.
[12:55] Or a good enough topology, I should say.
[12:59] And as you can see, if we play with this value,
[13:01] it will pick some hard edges.
[13:03] So a value of 89, it will work just fine.
[13:10] So yeah, now we can just subdivide it.
[13:14] And let's subdivide it by one is fine.
[13:25] I guess this is okay.
[13:29] And let's create just a not good node or a null.
[13:36] And call it soap.
[13:39] So this is the first part done.


### Creating bubble and foam in Houdini 20 [13:43]
**Transcript (timestamped):**
[13:44] So let's now create the bubbles and foam.
[13:52] So for that, I'm going to scatter some points.
[13:55] But before that, I'm going to create a density attribute with a attribute noise.
[14:05] And I'm going to say density and float.
[14:09] Oops, float.
[14:12] And let's say we use simplex, so element size, so how big the noise is, in this case point for two.
[14:20] And I know an offset of 7.7 will give me a nice result.
[14:26] You can just play with this until you find where you want your bubbles.
[14:35] And I'm going to scatter.
[14:39] And I'm going to scatter 400 points.
[14:44] So 400.
[14:47] And use the density attribute, but as you can see, it's still placing points on some parts I don't
[15:00] want. So I'm going to remap this, so enable remap ramp.
[15:04] And let me see, I'm going to push it quite a bit and push the reds, the i values.
[15:18] So something like this should do it.
[15:21] And let's see, our scatter is better.
[15:24] Maybe you can push it a bit more.
[15:27] Something like this is fine.
[15:33] And I'm going to play with the seat.
[15:38] And maybe remove the the relax situations.
[15:43] Let's see.
[15:45] Yeah, let's maybe remove that.
[15:49] And I'm going to do a natural randomize.
[15:53] And I'm going to say P scale.
[16:00] And going to use the new feature, which is the rematch bubbles to create some bubbles.
[16:12] So as you can see, this is way too big.
[16:17] So I'm going to global scale it to point of seven.
[16:23] And I want to control a bit more the size.
[16:28] I want to have some precision, let's say, on the size of the bubble.
[16:34] So I'm going to use a custom ramp.
[16:37] So custom ramp.
[16:40] And I'm going to play with these values.
[16:43] Let me just set it to one.
[16:47] And I'm going to say I want some big bubbles, then some smaller ones.
[16:56] And maybe increase this one and this one.
[17:02] And I'm going to totally play with the seat.
[17:08] Let's say we like this.
[17:10] Maybe play with the seat here.
[17:13] So maybe we like this.
[17:29] Now you just need to find a good position.
[17:34] So let's keep it like this.
[17:36] We can change it later.
[17:38] So this is our bubbles.
[17:43] And now let's go in here and create the foam.
[17:55] So I'm going to group the density.
[18:02] So points at the density bigger than point one.
[18:16] And I'm also going to group expand it.
[18:19] Like doing an attribute expand.
[18:22] So I'm using the group.
[18:26] So group three.
[18:27] Group three.
[18:29] And I'm going to expand it by four.
[18:34] Let's see.
[18:35] So I want to grow the foam a little bit.
[18:40] And now we can just blast.
[18:45] The lead non-selected and blast the group tree.
[18:50] And we can remove the visualization.
[18:55] And the leads any small parts.
[18:59] So let's go with the smaller something like this.
[19:08] And I'm also going to pick it.
[19:13] Because we will convert this to a VDB.
[19:17] And it will go a bit outside the surface.
[19:24] So minus point 0.01.
[19:27] This is not strictly necessary.
[19:29] But and now I'm going to create a VDB from polygons.
[19:37] But this is not a closed surface.
[19:39] So we will need to use another trick in here.
[19:44] So bear with me.
[19:47] So in the VDB from polygons, I'm going to say this is density.
[19:53] And point 0.01.
[19:59] And let's see.
[20:00] Okay.
[20:01] Now create a VDB topology to SDF.
[20:08] And as you can see, we get this thickened shape.
[20:13] We could just extrude it.
[20:15] But and do a VDB.
[20:18] But this will also work fine.
[20:23] So now we want to reshape it.
[20:26] So reshape SDF.
[20:30] And we will dilate it quite a bit.
[20:33] So by 5.
[20:34] So we have a thicker foam.
[20:39] And we will convert VDB.
[20:45] And we will convert this to a VDB.
[20:49] Let me see.
[20:51] We will convert this to a VDB.
[20:54] And VDB class, we will convert SDF to fog.
[20:59] We don't see much.
[21:01] But we can create a volume visualized with visualization.
[21:08] And play with density scale.
[21:12] So this is our fog.
[21:17] Now,
[21:18] we can just create a name in here.
[21:24] Because we will use that later.
[21:26] And now let's create a VDB from polygons.
[21:32] And we can just copy from here.
[21:48] And we will use instead the fog VDB.
[21:53] And maybe fill the interior.
[21:58] And use this.
[22:01] Point over one is fine.
[22:04] And in this case, we want to actually increase the density.
[22:08] So we will use a volume wrangle.
[22:12] And we will say,
[22:16] at density times 5.
[22:25] So in this case, we will have actually some more density.
[22:31] And now we can create a VDB combine.
[22:36] And we will do subtract.
[22:50] So we will do subtract.
[22:57] So we get something like this.
[23:00] Let me check here.
[23:05] Yeah.
[23:07] Now let's create a volume visualization in here.
[23:11] And increase it.
[23:14] So we get this result, which is fine.
[23:20] So this is for the phone.
[23:24] And we can create a null.
[23:28] And call it out volume.
[23:32] But this fog or this foam will be just too uniform.
[23:42] In here, we will have the bubbles.
[23:45] But we'll be too uniform in here.
[23:48] So let's create some noise.
[23:51] And we can actually do that pretty simple with volume noise.
[24:02] And we will create zero centred.
[24:08] And I amplitude.
[24:14] And an element size of 0.003.
[24:20] You can see this will simulate the smaller bubbles that we don't actually have.
[24:26] But just play with the offset.
[24:30] And this will be our volume.


### Modeling the plate with equidistant expression [24:37]
**Transcript (timestamped):**
[24:37] Now we will create a shape to hold our soap.
[24:41] So like a plate, I'm going to call it like a plate.
[24:45] So I'm going to start from the soap.
[24:51] Create a null.
[24:53] And we will start with the box.
[25:00] And do a match size.
[25:05] Match size.
[25:08] And let's check our soap.
[25:13] Something like this.
[25:17] And we will scale to fit and remove the uniform scale.
[25:21] And we will also give it some subdivision.
[25:27] So 9, 2 and 6.
[25:33] And the match size, we also need...
[25:38] Now this one is fine.
[25:42] Now we place it in the center.
[25:45] So another match size.
[25:46] And now comes the tricky part.
[26:00] We need to scale it while keeping it equidistant.
[26:08] I believe that's the word.
[26:10] So buried me.
[26:13] We will if we scale it like this.
[26:19] As you can see the space between the old sides is not the same.
[26:29] So we could eyeball it.
[26:31] So let's say we scale it by 1.26.
[26:36] And we can try to eyeball it.
[26:38] But I'm not very good at eyeballing it.
[26:44] So I'm going to use instead an expression.
[26:50] And this will be quite a big expression.
[26:56] Maybe there are better ways of doing this.
[27:00] But the thing I'm going to do is calculate the size.
[27:09] The ratio between the original size and the scale size.
[27:13] So getting the difference.
[27:15] And then adding it to the scale set in this case.
[27:19] As you can see by the Gismo.
[27:21] So I'm not very good at explaining it.
[27:25] But maybe you will get the idea.
[27:28] So expression edit expression.
[27:31] Since it's going to be a long one.
[27:34] And we're going to do bounding box.
[27:37] We will take the Z size.
[27:41] So the Z scale.
[27:45] And we will subtract again the bounding box size.
[27:56] Z Z by the X size.
[28:06] And multiply it by this channel.
[28:11] So I know that's channel.
[28:16] Scale X.
[28:18] Scale X.
[28:20] And I'm going to divide it by the bounding box.
[28:32] So I can just paste it by the bounding box at size.
[28:39] And as you can see.
[28:42] That is not yet working properly because we need to do some breaketing.
[28:47] So we will place one here.
[28:53] And another one in here.
[29:01] So it's not working yet.
[29:05] So we need one here.
[29:08] Bounding box at size minus
[29:11] bounding box at size.
[29:15] X size multiplied by channel X.
[29:20] One to three and divided by two Z size.
[29:26] So let me see why it's not working properly.
[29:33] So it's giving me two.
[29:39] While it should give me 1.4.
[29:48] So in here it's actually X size.
[29:53] So now it should be working properly.
[29:55] As you can see we have the same space between this size and this size.
[30:01] So again we will use this expression another time.
[30:07] So it's good to have it working.
[30:13] So that was the way to scale it uniformly.
[30:18] Or not uniformly but keeping it equidistant.
[30:23] Believe that's the word.
[30:25] So now let's just clip this.
[30:29] But we will do all primitives.
[30:32] So clip it in the middle.
[30:34] And we will also create the group.
[30:36] So we can extract it later.
[30:39] And now we're going to do the same.
[30:47] We're going to scale down the bottom.
[30:50] So let's group the bottom primitives.
[30:54] So by normal one zero.
[30:58] And let's do minus one.
[31:02] So we will group these bottom primitives.
[31:06] And let's again transform it.
[31:10] And we will transform the group for.
[31:16] So group for.
[31:18] And as you can see if we transform it
[31:23] uniformly we will have again the same issue.
[31:28] As you can see it's not the same space.
[31:31] So we will do instead point nine in here and copy the same expression.
[31:38] So oops.
[31:39] Control C.
[31:46] Control V.
[31:48] So as you can see now we are bit working.
[31:52] Which just makes me feel a bit less stressful let's say.
[31:58] Although it's always a pain to find the right expression.
[32:02] And chat GPD can't really help you that much.
[32:07] At least with with the prompt Ciantra it didn't help you much.
[32:15] So let's say we want to bevel now this bottom.
[32:19] So point oh wait.
[32:24] And let me see how we need to blast.
[32:30] And we will blast the below the top I mean.
[32:39] And now we can bevel it.
[32:41] And we will enter six divisions.
[32:44] So we have something like this.
[32:49] And let's group the unshare edges.
[32:55] And we want to extrude now these edges out.
[33:02] So let's try to extrude.
[33:07] And we will extrude the unshared.
[33:12] And as you can see it's not working the way I want it.
[33:17] Neither the options.
[33:20] So we will need to manipulate normals.
[33:24] So for that let's create a normal.
[33:28] And I believe I need it on the points.
[33:31] As you can see they are all pointing down in this edge.
[33:35] So we can use an attribute expression.
[33:39] And flatten.
[33:40] So let's speak normal and flatten ZX plane.
[33:45] And now we have them straight.
[33:47] This is a nice trick.
[33:49] And now we can use existing normal.
[33:52] And we will extrude it by .084.
[34:02] And now we have the normals all messed up.
[34:06] So let's create a normal.
[34:11] Everything is working.
[34:15] And now we might want to bevel this edge in here.
[34:21] So let's create a bevel.
[34:26] And we will exclude the flat edges.
[34:31] And with a distance of .084.
[34:36] And tree subdivisions.
[34:42] Now let's extrude this.
[34:44] So extrude by .075.
[34:52] And as you can see it's extruding out.
[34:55] I want to extrude to the other side.
[34:58] So we can use a reverse in here.
[35:02] And use the output back.
[35:06] And then we can use the output back.
[35:08] And then we can use the output back.
[35:10] And then we can use the output back.
[35:12] And we can use another normal to fix that issue.
[35:18] And we can just subdivide.
[35:26] And we can subdivide two times maybe.
[35:33] And then just place a softenable.
[35:38] That will fix our issue.
[35:49] So let's select this press A and drag to smooth out the network.
[35:58] And now we will create a we will align this shape.
[36:04] So let's go let's first merge the incoming geometry.
[36:18] So let's create a name.
[36:23] So we can target it in salary.
[36:25] So soap and bubbles.
[36:30] And we can merge.
[36:34] So like this.
[36:40] And then we can match.
[36:43] We can actually match size in here.
[36:54] And we will do max and min.
[37:01] And let's check this.
[37:05] And we will offset it.
[37:09] 0.39.
[37:14] Oops maybe not so much.
[37:19] Let's press control to actually see the shape.
[37:23] And let me check.
[37:37] We will need to play a little bit with it.
[37:46] Something like this will do fine.
[37:49] And let's create a name in here.
[37:55] And call it plate.
[38:03] And now we can merge.
[38:07] This name with this margin here.
[38:11] So something like this.
[38:17] That's attribute delete.
[38:18] And we will just keep.
[38:23] Let's delete non-select it.
[38:26] Keep the normal and the name.
[38:31] So we have a name for each object.
[38:36] And also group delete.
[38:37] Let's clean a bit the geometry.
[38:43] And let's delete everything.
[38:46] Maybe we need to play with these bubbles.
[38:49] I'm not too happy with that.
[38:50] But let's see.
[38:53] So create an all and create out.
[38:56] So.
[38:58] Fight Club.
[39:01] Fight Club is a great movie.
[39:03] It's one of my favorites.
[39:06] So let's maybe do like this.
[39:11] And.
[39:15] And we have the volume.
[39:20] And we have the scene.
[39:23] And now we can move on to shading.
[39:26] Okay guys let's move into salaries.


### Solaris setup and main materials with material X [39:27]
**Transcript (timestamped):**
[39:31] So before that we might want to do a file cache.
[39:38] So let's name it.
[39:40] So FC.
[39:45] So FC.
[39:48] Let's save it because sometimes it starts to calculate the network.
[39:55] And it might cause some crashing and slowdown.
[39:58] So it's always a good idea.
[40:00] So let's press D.
[40:02] Go.
[40:02] And I don't want to see the environment lights.
[40:05] And I need a darkwick round.
[40:09] And I want to render the viewport size.
[40:13] So let's stop import.
[40:17] And let's pick out soap.
[40:24] So this.
[40:27] Let's create a nice name.
[40:29] So.
[40:32] Oops.
[40:33] Let's have a done.
[40:34] And let's duplicate it.
[40:37] And call it come.
[40:40] And import the volume.
[40:45] So we should be having the volume.
[40:49] Let's create a material library.
[40:54] And also a dome light.
[40:57] We will do some custom lighting.
[41:01] But for now.
[41:04] Let's create.
[41:10] Let's use this one from polyaven.
[41:16] We can also create a camera.
[41:20] So something like this.
[41:23] And create a new camera.
[41:27] And karma render karma.
[41:31] It will create a render rope.
[41:33] And the karma render settings.
[41:36] So.
[41:39] Let's remove the visualization of the camera.
[41:46] And we can create a basic material.
[41:50] So karma material builder.
[41:52] And let's decrease the diffuse.
[42:03] And assign to walk.
[42:07] I mean.
[42:11] We can remove the form for now.
[42:14] And let's just see how this looks.
[42:16] So we actually need to change this to XPU.
[42:25] And I'm going to change a few settings.
[42:29] So I'm going to the limits.
[42:31] You don't need to do actually this much.
[42:35] But I'm going to increase it anyways.
[42:37] I increase the reflection limit.
[42:40] And set the volume to 16.
[42:44] And the SSS to 12.
[42:47] Let's say.
[42:50] Because we're going to use some subsurface scattering on the soap.
[42:56] So let's start by that.
[42:58] Let's start by creating the soap material.
[43:02] So let's create a karma material builder.
[43:06] And I'm going to say soap.
[43:09] Matt.
[43:10] Oops.
[43:11] All the evids from Maya.
[43:15] Always name it Matt.
[43:17] We don't actually need it in here.
[43:19] But.
[43:22] And.
[43:28] I'm going to change the few settings.
[43:30] So we can leave the diffuse because we will use a full subsurface scattering.
[43:37] So roughness.
[43:39] I'm going to change it to 0.37.
[43:44] And I'm also going to include some code.
[43:50] And in the subsurface, I'm going to use a custom color.
[43:58] And just copy to the radius.
[44:01] So copy and paste.
[44:05] And increase the subsurface.
[44:08] And as the scale, I'm going to use point 0.2.
[44:12] So let's out of film.
[44:16] And go in here and pick the soap.
[44:19] And let's see how that looks.
[44:25] So it's a bit too reflective.
[44:30] But it matches a bit more my reference.
[44:34] So I'm going to keep it like this.
[44:36] But feel free to introduce some roughness.
[44:40] A more rough material.
[44:43] I might play with the code roughness.
[44:49] So.
[44:50] But yeah, I'm going to keep it like this.
[44:56] And when we introduce some lights, it will create a large dramatic look.
[45:01] So yeah, that's our soap material then.
[45:05] Now let's create the material for the bubbles.
[45:14] So let's create another carbon material builder.
[45:17] You call it bubbles matte.
[45:24] And for this one is quite simple.
[45:27] We just need to increase the transmission to one.
[45:31] And check tin walls.
[45:35] And we will also introduce some tin film.
[45:40] So let me just make sure we assign the material.
[45:45] So out of film.
[45:47] And create a bubble and assign to the bubbles.
[45:53] Let's check.
[45:54] It's a bit hard to see.
[45:56] But again with the other lights, it will look better.
[46:01] But you can see how this is looking.
[46:04] And let's now introduce some tin film.
[46:16] Let's say we want the index over fraction of 1.8.
[46:22] And thickness of 200.
[46:27] We will start to see something.
[46:29] But I actually want to use a noise to have some more variations.
[46:36] So I'm going to use a unified noise 3D.
[46:42] And a frequency of 40.
[46:50] And let's see, I'm not set up 30.
[46:52] That's the values I used before.
[46:54] But you feel free to use another ones.
[47:00] And I'm going to also use a feed range.
[47:05] Feet range.
[47:08] It's a strange, not feed range.
[47:12] And I'm going to say, I'm going to use that thickness of
[47:17] between 50 and 250.
[47:22] And you can have a look at the noise.
[47:24] So if I unleads.
[47:29] If I show you how this looks.
[47:33] So this is how the noise looks.
[47:38] And if we connect this to the tin film thickness.
[47:50] Should be able to start to see some tin film.
[47:55] And if we don't see much, we can increase.
[48:00] As you can see now it's more noticeable.
[48:05] Let's keep it to 1.9 for now.
[48:10] And we will see if we need more.
[48:15] So that's our bubbles then.
[48:18] Now let's create the material for the plate.
[48:27] So parameter material builder.
[48:31] Let's make.
[48:32] I'm saying plate, but I don't actually know the name for this.
[48:36] So forgive me for that.
[48:39] And I'm going to use, I'm going to say it's going to be a metal.
[48:47] And as the specular roughness, I'm going to load a custom texture.
[48:52] So karma.
[48:54] Triplaner.
[48:57] And let me see which texture I used.
[49:01] So see one for.
[49:07] I'm going to have to pick it.
[49:10] So I just pick my texture.
[49:12] I can show you how it looks.
[49:14] And lead.
[49:17] And lead material.
[49:20] There should be a way to debug the nodes.
[49:28] But the debug button doesn't actually work.
[49:32] And we need to assign this to the plate.
[49:42] And let's wait a little bit.
[49:44] So this is how it looks.
[49:49] And I'm actually going to increase the size.
[49:53] And also increase the blending.
[49:56] As you can see that helps with this edge.
[50:01] And let's introduce some random scale.
[50:07] And play with the seeds.
[50:11] Something like this.
[50:14] And now let's connect it.
[50:18] Let's create a separate color for.
[50:21] So we can extract just one channel.
[50:25] And let's use a mix.
[50:29] We can use the red channel.
[50:32] And we will say our roughness will vary between point four and point two three.
[50:39] Those were the values I in like.
[50:43] So specular roughness.
[50:47] And we will have this look.
[50:56] Let's maybe try to introduce now the lights.
[51:02] So let's focus on that next.


### Lighting and foam volume material [51:06]
**Transcript (timestamped):**
[51:07] Okay, so let's create a rectangle light.
[51:12] So light and airy light.
[51:15] So light one.
[51:18] And I'm going to pick a rectangle.
[51:22] And look through selected.
[51:25] And enable the lock.
[51:29] And I'm going to place it.
[51:34] So right here.
[51:36] So something like this.
[51:50] So let's check our lights.
[51:52] So we have a light there.
[51:55] And let's look through our camera.
[52:01] And when the red carmex view.
[52:04] Let's disable the dome light.
[52:09] And we will crease it to four.
[52:14] And maybe one.
[52:18] Maybe that's too much.
[52:21] So something like this.
[52:24] We have this nice lighting.
[52:27] And let's create another one.
[52:29] So maybe I don't like the sharpness of the lights.
[52:35] So I'm going to introduce a texture.
[52:38] So I have here an HDR texture to use as a light.
[52:46] So as you can see it gets darker.
[52:48] So we need to increase the exposure.
[52:55] Something like this.
[52:56] It will just create a softer falloff.
[52:58] As you can see.
[53:01] And let's duplicate the light.
[53:05] And I'm going to place it on the other side.
[53:10] So look through light.
[53:12] Light to lock it.
[53:15] And let's place it in here.
[53:23] Let's say.
[53:24] And let's look through our camera.
[53:32] And we will decrease the effect of this light.
[53:36] So actually let's see.
[53:44] Let's increase it actually.
[53:46] Two.
[53:48] Two.
[53:49] Two.
[53:52] And let's enable the other light.
[53:57] And let's actually use a bit of the dome light.
[54:02] So set it to 0.3.
[54:05] And let's enable it.
[54:08] And of course it will compile again.
[54:11] And so it's already looking much better the lighting.
[54:17] So now we will introduce the phone.
[54:22] So let's enable it.
[54:27] And we will create a material for the phone.
[54:30] So let's see.
[54:32] Karma.
[54:35] Uniform volume material.
[54:40] And that's fine.
[54:43] Let's edit.
[54:47] And we will add it to the phone.
[54:53] Let's see if that works.
[55:04] So that's actually not working.
[55:07] Let me check.
[55:10] Carom material.
[55:23] Let's see.
[55:27] And we will smoke, scatter, fire, binding density.
[55:31] Let's increase this.
[55:35] So it's not binding the material properly.
[55:39] So let's do the following.
[55:42] Let's cut it from here.
[55:47] And let's create another material library.
[55:52] Maybe.
[55:56] Maybe we need to remove this one.
[55:59] This default material.
[56:01] So let's see now.
[56:06] Is it binding?
[56:09] It should be.
[56:14] Let me check.
[56:27] Okay now it's working.
[56:31] We just needed to remove that particular material in there.
[56:35] So let's pick.
[56:42] Let's check.
[56:44] Oh, this looks.
[56:49] And volumes don't work well with render regions.
[56:54] And one issue I was having when trying to render this scene
[56:59] was that I was getting some shadowing between the bubbles and the phone.
[57:05] And I don't actually want that.
[57:09] So let's do the following.
[57:14] Let's create a render geometry settings.
[57:22] And load the phone.
[57:25] Let's load the soap bubbles.
[57:32] And the phone.
[57:38] And let's put the final render.
[57:45] And in here we will be shading, set or create
[57:52] and remove the shadow contribution.
[57:57] So let's check again.
[58:08] And we might need to increase.
[58:14] Let's see.
[58:22] And the render region doesn't work well with volumes.
[58:33] So let's increase the density.
[58:40] So 150.
[58:42] Hmm.
[58:48] We might need to play a bit.


### Editing the volume [58:54]
**Transcript (timestamped):**
[58:58] This is not looking.
[59:00] Hmm.
[59:06] So this is okay, but maybe we need a bit more thickness on this volume.
[59:15] So let's go back to sobs.
[59:22] And maybe let's see the result.
[59:27] So control click.
[59:28] And look at the volume.
[59:32] F.
[59:36] As you can see, it's just not thick enough.
[59:47] Let's have a look in here.
[59:49] So.
[59:50] So.
[59:57] Yeah, it's just too thin.
[60:00] So in the VDB reshape, maybe we will decrease the group expand to two.
[60:10] And we will increase the reshape to 12.
[60:20] Maybe not so much, maybe nine.
[60:32] And maybe, maybe increase the amount of bubbles.
[60:38] So 600.
[60:45] And play with the seed.
[60:50] Let's see something like this.
[60:54] And I was calculating the volume anyways.
[60:59] Let's try these again.
[61:04] Maybe let's increase these .05.
[61:14] And maybe increase this one to wait.
[61:20] Let's try that.
[61:24] Oops, I need to save it.
[61:29] So the volume is fine, but in here I need to save to this.
[61:37] And let's go again to salaries.
[61:41] And this will not be the same as the final result I had because I tweak it quite a bit.
[61:48] But let's try to get something good.
[61:54] This tutorial is pretty much done.
[61:56] So if you want to skip this part, feel free.
[62:02] But let's just check now.
[62:06] Maybe we need to decrease now the.
[62:08] And maybe let's play a bit with the lighting.
[62:16] So let's decrease this to four.
[62:23] Maybe not.
[62:28] And let me render and see the result.
[62:32] Let's maybe decrease the density of the volume.
[62:35] So let's go again to 100.
[62:41] Because that's way too much.
[62:42] And now is looking a bit better.
[62:46] Let's render it.
[62:49] And I will be back in the second.
[62:53] So maybe the size of this fog volume is too much.
[62:59] These fog noise.
[63:01] So let's just quickly change that.
[63:07] So in here 0.025.
[63:14] Let's go back to the stage and do the rendering.
[63:24] So yeah guys, I ended up doing a full render with some more samples.
[63:30] So as you can see, I increased it quite a bit.
[63:33] And just click on render to em play.
[63:36] And I'm just doing a 720p, which is fine.
[63:41] And as you can see, the soap is looking better with a smaller scale in the fog noise.
[63:46] It looks like we have some small little bubbles in there, as you can see.
[63:53] And overall it's okay.


### Final Render + Outro [63:54]
**Transcript (timestamped):**
[63:54] It's not perfect.
[63:56] But I thought about creating a simple project to show off
[64:02] some of the Odini capabilities and karmas.
[64:06] So hopefully you have enjoyed this one.
[64:09] Also I have Patreon if you want to check it out.
[64:14] Where I have also some courses, as you can see, I created in the past.
[64:20] And I also share the project files from all my videos in the channel.
[64:29] So check that out.
[64:32] So yeah, that's basically it.
[64:34] So hopefully you enjoyed this one.
[64:36] And I hope to see you next time.
[64:38] Leave a comment.



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
