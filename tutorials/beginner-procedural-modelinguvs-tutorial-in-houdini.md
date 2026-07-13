---
title: Beginner Procedural Modeling/UVS Tutorial in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=-1kxDkdmcV4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Beginner Procedural Modeling/UVS Tutorial in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=-1kxDkdmcV4)
**Author:** cgside
**Duration:** 18m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py beginner-procedural-modelinguvs-tutorial-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back, so in this video we'll be modeling this wine barrel.
[0:04] It will be a good chance to get familiar with some of the most used subnotes alongside
[0:10] with some very simple backs concepts and also how to do the proper UVs or this kind of
[0:18] procedural assets.
[0:20] And if you guys are interested, we can in the next lesson, texture the barrel as you can
[0:25] see here, nothing too crazy, but it could be a good exercise to get familiar with cups.
[0:31] So yeah, let's get into it.
[0:33] So let's start by dropping a geo container and we will start with a tube and I found some
[0:41] values, in this case I want a height of 1.1, 12 rows and 32 columns, so we can make out
[0:50] the wood planks.
[0:53] And I believe that would be it for now.
[0:56] Now let's drop a wrangle and we will deform this into the barrel shape.
[1:02] So let's start by storing the bounding box information or the relative bounding box.
[1:08] In this case we will use relative point bounding box and the incoming geometry and the position.
[1:16] And I can show you, if I create a natural boot in here, I can show you what this means,
[1:24] is basically the relative position of the geometry as you can see.
[1:31] So this is the y going from 0 to 1.
[1:34] If we instead used at b, it would go from minus 1 or minus 0.5 to 0.5.
[1:44] So we want to use the relative bounding box, since we have this centred in our scene.
[1:50] But in this case we don't want to use this, we will use a ramp to deform our shapes.
[1:56] So see a ramp and we will call it ramp deform and we will use the relative bounding box
[2:07] y.
[2:09] And let's have a look at that.
[2:12] Now we want to transform this to a hail shape, so it looks something like this and change
[2:17] the interpolation to b-spline.
[2:19] Let's see how that looks, if we deform both the x and z component of the position.
[2:23] So at b dot x times equals ramp and it will do that on the x and now we can just copy
[2:34] and do the z.
[2:38] As you can see it's creating that shape, but in this case we want to move those handles
[2:46] up and I'm going to copy this value to the last one, so with mirrors whenever I move
[2:53] one it will move the other and I'm going to set it to 0.7 to 5.
[2:59] This was just a value I found work 12.
[3:03] And we have our first back setup done.
[3:05] I believe it's really simple, if you are having trouble understanding it, I can go on
[3:11] the comments and help you out.
[3:14] So now we want to create an attribute for every column, so we will use a kind of bit
[3:19] of backs.
[3:20] In this case, in this one we used points, right now we're going to use primitives because
[3:25] we want an attribute on the primitives.
[3:28] And the first thing we're going to do, we're going to reference the columns from the
[3:31] two, so it will create a variable, an integer and a channel integer called calls, calls.
[3:40] And now we're going to create that parameter and come in here and copy this.
[3:44] This just makes everything more procedural instead of typing the value itself.
[3:49] And now we can just write a premium, premium ID, it will be equals to add to print, print
[4:00] them.
[4:03] And let's have a look at how that Cisco is working.
[4:07] So we have for each primitive we have an ID, a prim ID, but in this case we want to use
[4:13] module to separate them into different columns.
[4:16] So if we divide in this case by the columns, we will have a notice these rows, as you can
[4:24] see, but in this case we want to module it.
[4:27] So we get this sort of result.
[4:29] So it's always useful to divide in the module to this kind of word.
[4:34] And now we can just poly extrude it.
[4:38] So extrude.
[4:41] And we will extrude by about point of 12 was a value I found work well and I'll put
[4:48] the back.
[4:49] So we have the back polygons.
[4:51] And now we want to split it to split each plank.
[4:54] So for that we can use a vertex split.
[4:59] And by default it will use the anature root, we will remove it and use the premium ID.
[5:04] And if we do an exploded view, we will see that we've split it to the planks.
[5:10] But right here it's empty and we want to fill that.
[5:13] But for now we will first do a uniform scale of point of 1 in the exploded view.
[5:20] This will have a little bit of space as you can see.
[5:23] And now we can just poly fill.
[5:26] And what we let rolls will be fine.
[5:28] It will work perfectly as you can see.
[5:31] And that's this part done.
[5:33] So now we want to do our UV.
[5:35] So let's create a group or the seams.
[5:38] In this case I'm gonna select edges and include by edges and select mean edge angle.
[5:44] And it will select those edges.
[5:46] Now we can just see UV flatten.
[5:51] And we will do the group one.
[5:53] And also we will rectify and disable manually out.
[5:57] And if we look at our UVs, there will look clean enough.
[6:01] Please follow.
[6:03] So let's disable the visualization of UVs and create a bevel.
[6:10] And we will exclude the flight edges.
[6:14] So we just bevel the corners as you can see.
[6:19] And in this case I want a value of point of 2 rounds and 3 divisions as you can see.
[6:27] And the UVs should adapt.
[6:29] So that's fine.
[6:31] Now we will subdivide this.
[6:37] And soften the normals.
[6:38] So we have a better preview.
[6:40] As you can see we have this word shaving not sure if it's going through the recording.
[6:45] But if we soften the normals it will look a bit better.
[6:49] And finally we just need to create a attribute.
[6:53] In this case using a rainbow, why not?
[6:55] And just say we want a float attribute called barrel.
[6:59] And it will be called the one.
[7:02] So we just create a attribute.
[7:05] So we can target later in texturing.
[7:08] Now we will fill this barrel by closing in these gaps we have in here.
[7:14] And this should be simple enough.
[7:17] So let's start with a circle.
[7:19] Oops, circle.
[7:23] And we will place it on the ZX plane.
[7:26] Set the divisions to 32.
[7:28] And I know a value of point 3, 8 will be more than enough.
[7:34] And while we are here we will just use the texture of this.
[7:40] In this case on the Y.
[7:43] Let's see how that looks.
[7:44] As you can see it's reversed so we can scale it negatively.
[7:50] And but it will move it down so we can just use an offset of one.
[7:54] So that is fine.
[7:57] Now we can copy.
[7:59] Because we will need another one.
[8:01] So copy and transform.
[8:04] And if offsetting will be fine.
[8:05] It will copy just one.
[8:07] Now we will reverse one of them.
[8:09] Reverse the normals of one of them.
[8:11] So it can be zero.
[8:13] And next we will do some really simple Vex.
[8:18] We will move them apart.
[8:21] So we can just say.
[8:23] Let's see.
[8:28] VHP plus equals.
[8:32] We will display along the normal and multiply it by some value.
[8:38] So let's say this.
[8:40] Let's see if that works for us.
[8:43] And it does.
[8:44] And I know a value of point 5, 3 will be fine.
[8:49] And we also want to create a natural root.
[8:51] So it's in this case I'm going to do another one.
[8:55] And say f at the arrow tops equals to 1.
[9:02] And let's merge this.
[9:05] And see if that aligns.
[9:06] And it does.
[9:07] You can see we can go in here and play with the offset.
[9:12] So let's organize this by pressing A and dragging.
[9:15] This is fine.
[9:16] And let's create the norm.
[9:20] And call it barrel.
[9:26] And we have our UVs.
[9:27] Later on we will lay them out properly.
[9:30] So they have the same scale and whatnot.
[9:32] But for now let's keep it like this.
[9:35] So now we will create the hopes around the barrel.
[9:39] And for that we will start.
[9:41] Let's see.
[9:42] We just circle.
[9:47] And this circle can have 32 subdivision students just to keep some consistency.
[9:53] And on the ZX plane, the size doesn't really matter.
[9:58] For the UVs later we will need some groups.
[10:02] So I'm going to create a range and connect the divisions in here.
[10:09] The copy parameter and paste it in here and divided let's say by four.
[10:15] So we don't have UGV islands.
[10:18] And so this way we can divide it into sections.
[10:22] And now we will create the normals.
[10:24] So that's a good language.
[10:27] I believe I used open arc in here.
[10:29] Yeah, open arc.
[10:30] That's fine.
[10:32] And now we will just create the aperture boot for the sweep that we will use in a bit.
[10:36] So vector up it will be equal to normalize V at P.
[10:43] So this will just create the vectors pointing outwards like this.
[10:50] So that is fine.
[10:53] And now we will match size this.
[10:57] We will align it with the barrel in here.
[11:03] And in this case, let's see, let's visualize this.
[11:09] And we will align it to the max and offset it by 0.03 negative 0.03.
[11:16] So this will be the first hoop.
[11:19] And now we can copy and transform.
[11:24] And we will copy three times and place it by about point all weight, negative point all
[11:32] weights something like this.
[11:34] Now we can mirror this to have also in the bottom.
[11:38] So in this case, I want to do direction to be one in the white.
[11:44] Let's evolve.
[11:45] And it's aligning properly.
[11:48] Now we will do the same for the other.
[11:54] Let me just organize this in here.
[11:58] We will do the same for the middle ones.
[12:01] In this case, we will set it to center and offset it by part 15.
[12:08] And just copy the mirror.
[12:10] And we have this result.
[12:12] Now we can merge this.
[12:16] We have something like this, which is fine.
[12:21] Next we will fuse the points.
[12:24] Make sure we fuse.
[12:26] Because when you create an open arc circle, they will have a point where they are not
[12:31] fused.
[12:32] So it's always a good idea to fuse because right now we want to use the sweep and set
[12:37] it to ribbon.
[12:39] And since we add that aperture boot, you can see if I don't create that, it won't align
[12:44] properly.
[12:46] And in this sweep, we will just play a bit with the size.
[12:51] So two columns.
[12:53] So we don't need much geometry and a value of 0.05 the size.
[13:00] So 0.05 is fine.
[13:03] Now we will merge here the barrel so we can rate this project is geometry onto the barrel.
[13:09] So let's just drag it in here.
[13:13] And let's see, let's rate this.
[13:18] But this won't work even if you create a, if you check reverse raise.
[13:25] Probably because there are open spaces in here, I'm not sure why.
[13:29] But quick fix is just use a convex all.
[13:33] And this will create some some proxy geometry.
[13:41] And now we can rate this and check reverse raise.
[13:46] So that is fine.
[13:49] Now we can just create another wrangle and call it.
[13:54] Oops, so oops.
[13:57] And this is just for cops later so we can mask out some parts.
[14:06] Now we will pick it a little bit.
[14:09] In this case, really small distance.
[14:12] Let me see.
[14:13] So you can see the barrel is over the, the, this option geometry so we'll pick it by 0.05.
[14:23] So this is fine.
[14:25] Now we need to start to think about UVs.
[14:29] So I'm gonna create a group of the unshared edges for now and you will see why in a bit.
[14:37] So unshared edges and now we will extrude it.
[14:44] And we will extrude by about 0.03.
[14:48] And do we need to output the back?
[14:54] In this case, I'm gonna do it the way I did it.
[14:57] But in this case, we didn't need to output the back, I guess.
[15:00] But let's keep it like that.
[15:02] Now we did this grouping here, group by range.
[15:07] So we called UV the mesh now.
[15:09] So if we have a look at the range group.
[15:16] So oh, I didn't call it range.
[15:18] Let me go back and call it range.
[15:22] So as you can see, we have this grouping here.
[15:25] But it's only on the back.
[15:26] It didn't propagate with the extrusion.
[15:30] So we will need to use a node called group line path.
[15:36] So group line path.
[15:39] So we can finish the selection.
[15:41] In this case, I'm gonna call it range.
[15:45] And the base group will be range.
[15:47] Let's set these two edges.
[15:50] But before we need to promote it, of course group promote.
[15:54] Range to edges.
[15:56] Let's see.
[15:58] And in this case, we need to include only elements in the boundary, I believe.
[16:03] Yeah.
[16:04] And now in here, we can just say loops or rings and extend to edge.
[16:12] And as you can see, it created the necessary cuts for the UV flatten that we will do now.
[16:21] So let's connect the UV flatten.
[16:23] And we will use the seams, the range and the unshared and rectified the group and also
[16:31] disable enable manual by out.
[16:34] So and we have nice UVs.
[16:39] And now we can just polybable.
[16:45] And we will be able to ignore the flat edges first and be able to buy a part to point
[16:52] a really small value point of level weight and round tree divisions.
[16:59] Let's see how that looks.
[17:00] That's fine.
[17:02] And now we can just subdivide this.
[17:06] Let's see what else we can choose as softenerables.
[17:15] And let's merge these.
[17:19] And we can just copy this from here and merge it over.
[17:27] Now we will use the UVs are all over each other.
[17:33] So we will use a UV layout.
[17:37] And in this case, I want to scale the islands to match their surface area.
[17:47] And let's see.
[17:51] This doesn't look bad, but I can probably use some iterations to distribute it a little
[18:00] bit better.
[18:01] Let's see.
[18:02] And that works for me.
[18:03] Let's see how that looks in here.
[18:06] Yeah, it looks pretty similar.
[18:11] And I'm gonna introduce some batting.
[18:16] And also apply batting between the islands and the boundary.
[18:21] So that's exactly my result.
[18:25] And this is it for this lesson.
[18:27] If you want to get into the texturing part, we can do that next.
[18:31] Other than that, please check out my Patreon where you will be able to find this project
[18:35] file and many, many others.
[18:39] And also have a look at my courses in there and leave a comment.
[18:43] It's always nice.
[18:44] Thank you.



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
