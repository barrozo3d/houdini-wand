---
title: No VEX challenge #1   Procedural Water Tower
source: YouTube
url: https://www.youtube.com/watch?v=NxWpxFDaSJE
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/no-vex-challenge-1-procedural-water-tower/
frame_count: 0
frame_status: pending-selection
---

# No VEX challenge #1   Procedural Water Tower

**Source:** [YouTube](https://www.youtube.com/watch?v=NxWpxFDaSJE)
**Author:** cgside
**Duration:** 48m35s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py no-vex-challenge-1-procedural-water-tower <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So into this video we're going to be building
[0:03] this water tower from scratch. It's a procedural model and the idea here is to do
[0:09] it without any Vex, without code. So we can, I can make this as beginner friendly as
[0:15] possible. So yeah, let's get into it. Okay, let's start with the geometry so we
[0:21] can build everything inside and the base shape will be a tube. I want to set the
[0:27] columns to 32 to have enough geometry and I'm also going to decrease the I to
[0:33] point eight. This is in meters and the rest will be fine like this so point eight.
[0:38] Yeah, let's create a null and this will be our base shape. From here we will
[0:46] extract some geometry to build out the remaining parts. So let's create in here a
[0:52] dot, by pressing old and creating a group. It will be group one. You can rename it.
[0:58] I'm not going to bother and I'm going to set these two points and go into
[1:02] include by edges and shared and create boundary groups and this will divide each
[1:08] and shared points in this case by two so we can manipulate both. So in this case,
[1:16] let me see. Yeah, I don't think I need that because I can just do unshared
[1:20] edges in this case but we will do that later. So let's from wordline. In this case,
[1:28] we don't need because it will be easier to separate them. So if we do now a split and
[1:33] we since we have one that is zero, we can just set it here to zero and it will output
[1:40] both the primitive zero and one. So yeah, we can work this way. So in this case,
[1:50] I want to invert the selection here because I want first the bottom to create the
[1:55] the spherical shape below. So for that, I'm going to create a polyfill. You can create a sphere
[2:00] and cut it but I'm just going to try to be as continuous as possible with the geometry
[2:06] always reusing parts. So you can understand a bit better of the procedural workflow. So I'm
[2:12] going to set this to what your lateral grid that's a mouthful and I'm going to start to play with
[2:19] this surface offset and let me see what sort of values did I use in here. So I'm going to reduce
[2:27] this to minus three points something and then I'm going to just try to sphereize it as possible.
[2:36] So something like this, squareize it, use that word. I don't know.
[2:40] So, verify it. I don't know. Well, anyways, now we cannot put the patch group and just blast
[2:48] everything that is not that that's patch group because right now in here, we also have the
[2:55] curve yet still. So let's blast and keep just a patch. Now we can reverse this.
[3:04] So we have something like this and we can subdivide it.
[3:14] Just one is fine. Now for this one, I want to scale it a bit up to create the comb at the top.
[3:23] So for that, I'm going to create a transform. And in the pivot I need to enter centroid. I have
[3:30] a preset in here in my recipes, centroid. You just need to write these expressions in here.
[3:35] So it scales from the center. Otherwise it will scale from the world center and it will move the
[3:42] geometry. So I'm going to scale it by 1.15. That's enough. Now I want to duplicate this shape and
[3:52] move it up and scale it to zero. So I can create some the cone shape. For that, first of all,
[3:59] I'm going to use the node and numerate. So I can have an ID. I'm going to set these to points.
[4:04] This just creates an ID on our geometry using the point number.
[4:09] The index, then I'm going to copy and transform.
[4:15] And I'm going to move it by 0.5 and scale it to zero. But as you can see, it's not scaling from
[4:24] the center. So we need to do the same in here. So centroid, 0, dx, or you can input just zero also.
[4:33] The y, I'm more used to this and the that. So now it's coming from the center. I just want to set it
[4:39] to zero. And now we still have that attribute on our points. And now it's getting duplicated.
[4:46] So if we now do a net by group and do by attribute and enter index, which is the name of that
[4:52] attribute, we create the geometry. Now I can blast this geometry in here. But let's just test
[5:03] without it. So if we create a skin, yeah, it will create some problems. So we need to create a blast.
[5:10] And first of all, I'm going to output the copy name in here. So that will look something like this.
[5:17] And we need to blast the primitive zero or the ID zero. So for that, I'm going to say that
[5:22] copy num is equal equal to zero. And if we set it to primitives, no, copy num bigger than zero.
[5:33] And we set this to points. So let me test something in here. Am I saying this correctly? So copy num.
[5:46] And this is on primitives. This should blast. So let me actually see what's going on. Marker.
[5:58] So that copy num is equal to zero. So that will work. Sorry about that. And now we can just
[6:08] skin this and it will work just fine. And this case, this is creating too much geometry. Let me see.
[6:22] So let me just do a wrap to one. Oh, yeah, in here, we need to do bigger or equals to zero.
[6:36] So it removes also any other primitive. And now we can do a skin with the V-Wrap one.
[6:42] I was confused. Sorry about that. Now we have some overlapping points in here. So if we use those
[6:51] and we do maybe let's see. Right now we have this normal issue. So we can do a soft
[6:59] anomalous and that will fix it. Maybe we can reduce this. But it's fine.
[7:07] So let's see what we've accomplished so far. If we select one node and another one and merge it,
[7:13] we have this. And if we merge in here, this one with this one, we have something like this. And
[7:22] we can take this off anomalous from here and past it and do it in here. So this is our base shape.
[7:32] So now we're going to create the platform or that I'm going to select this node in here and
[7:36] create an object merge with it. Or you can just type object merge and drag this in. I just do it
[7:42] this way because I have shared the script before about it. You can look it on my channel. So
[7:49] here we have the curve and we can polyfill it. And it will be just a single polygon and we
[7:59] still have the curve. So we in setup output in the patch group, we can just place the primitive zero.
[8:05] It will always be zero the curve. I at least I think so. And now we can transform it.
[8:12] And in this case, we want to scale it up by 1.2. And again, from the centroid. As you can see,
[8:20] it's moving the centroid in here. And I'm going to scale it to 1.2. Let's create an off.
[8:30] And now we're going to let's see, let's see what makes sense to do first.
[8:38] I'm going to create in here a group by range. And select a few points. I'm going to select
[8:47] to I'm going to divide these into sections. So right now we have 32 points. So we can do points
[8:55] and do one and copy from the two columns. And we can do paste relative reference. This will
[9:04] just select one. Let me increase that for you. So geometry marker guides point size point marker size.
[9:13] So you can see just selecting one. And I want to divide this into let's say 16 sections.
[9:23] So we get what we can just do. In this case, we don't need that. We can just, but this is useful
[9:30] because you can come in here and divide it into four. You can see or divide it into eight.
[9:35] But in this case, we can just do one out of two. That's fine. I'm now revealing my own file. And then
[9:43] we can blast just keep those points. So let's select one selected. And let's name this range.
[9:53] Let's select the near range. And let's do a net. And only geometry the slip points.
[10:04] Now we want to create the vertical vertical lines in here. So for that, I'm going to create
[10:12] the first of all an ID. So let's create an ID with any numerate. And let's set it to points.
[10:25] And now we can copy and transform and move these up. So in this case, five points to
[10:34] and let's create an ad node and my group. And we need to set it by attributes. And in next,
[10:43] and it will create the geometry. So we also want to create, you can actually just sweep this to
[10:56] have some geometry. So let's set this to square two. And I'm going to scale it to point out well.
[11:10] And we will see that this is not very underpropably, but we will fix it in a bit. Let's now focus on
[11:16] creating the remaining geometry. So now this knowing here, I'm going to create a dot with alt and
[11:26] create another node. And let's create a copy. So copy and transform.
[11:39] And we can actually copy from here. So copy these or create a reference copy and paste.
[11:46] And I'm going to split this right away. And I can split the primitive zero. Let's create a node.
[11:54] And another node to visualize the outputs. Now in here, I just want to do a sweep.
[12:01] Let's name it a stop and bottom. And let's create a sweep. And this can be around two.
[12:12] Let me see the thickness. So this is I'm going to set it to square two columns and a thickness of
[12:19] 0.17. And now for the bottom, we can just create a beacon. And I'm going to use in this case a value.
[12:34] I'm going to use the value of the same sweep.
[12:42] We have in here. So this one. So let's copy this. Let's paste it in here.
[12:51] So now we have this geometry and we can start to merge everything. So pressing alt after selecting the
[12:58] nodes. And now we can actually select this one and this one and drop down. And here we have the
[13:07] platform. Now as you can see, this is poking a bit out. So we actually need to extrude this shape a
[13:14] little bit. So for that, I'm going in here and create the unchained edges. This is just from
[13:21] labs. So I'm going to get the unchained edges. I'm going to extrude. And I'm going to extrude the
[13:32] unchained. And by the same amount of this sweep. So let's copy this and paste. And I just want to do
[13:43] all of it because the sweep will create geometry from the center. So just in case, I think I change
[13:50] in here this also to we don't need that much. So as you can see, now we have some breathing space
[13:56] in here, pot pillow, and above. And yeah, that's our platform done. Let's move on.
[14:03] So before we move on, there's still some things I want to do in this platform to create in here
[14:07] across geometry along these divisions. And also, as you can see, this is not oriented properly.
[14:14] So around the circle. And we need to create some normals or an aperture with pointing outwards.
[14:20] So these will involve just a little expression. And we can actually take advantage of a preset.
[14:28] So let me see where I have a geometry in here. And we can create this after the add I think.
[14:38] So after the numerate, for example, let's create the point point in this case, a natural expression.
[14:45] And we want to set this to let me see, it's fine fine. And if we have a look at that,
[14:54] we need to set this to normal. And as you can see, we have the normals pointing outwards. But we
[14:59] don't want the normals. We just want to set this to custom and tap. And now we should have an
[15:06] aperture with pointing outwards. And if we copy add, we should still have that aperture with as you
[15:14] can see. And it's working great. And now we can sweep. And if we have a look at the final results,
[15:21] we now have the geometry oriented properly. As you can see. So because this sweep node reads that
[15:30] aperture, we will to orient the primitives. And we will play with it in a bit later or another
[15:37] piece. So now we want to create some cross geometry in here. And without over complicating too much,
[15:43] we can use again the sweep node. So let's actually do that. Let me just start going to do the near.
[15:51] And let's take this geometry from here. And I'm going to press for me.
[16:03] And I'm going to translate it up. Like point one. And I'm going to convert line
[16:13] into a line. To make this a line, or you can use edge group to curve. And not group one, sorry. I
[16:22] just want one single one. And now we can do a sweep. But in this case, we want to set this to
[16:32] round two, but we see near a round two and two columns. And we want to set this to just
[16:40] output columns. As for the radius, I'm going to scale it to point 0.089. Let's develop our
[16:49] found work well. And now come to the trick where we can come near. And in the partial twist,
[16:58] we're going to set it to 180. And we're going to scale it per edge. And now we just need to roll
[17:07] this 90. And as you can see, we have that cross geometry that we can now sweep. And I think I
[17:14] use round shape in here. So just shake it. Now in this case, square two, square two to the two
[17:21] columns and point 0.07. And let's merge that in. And now we have that geometry, as you can see.
[17:32] So that is fine. Now let's see what's next. So now we're going to complicate a bit. Because I want
[17:40] you, if you're still a beginner, I want you to learn about other things. So I want to select this
[17:47] point so I can extrude a pull down like I want to create some geometry below. And for that, I want
[17:53] to extract this point procedurally. So we can go back when we created that geometry. So in here,
[17:59] let's create an all. And what we're doing here, we can run a detailed
[18:07] vote since we just want one point. So we just want to run these ones. And from this geometry,
[18:14] we can get the bounding box. So bounding box. And from there, we can just create a
[18:24] near point function. So near point. And we can feed this into here. And we want to select the
[18:33] mean as pass. And if we output that as the group or as a point, so buying the export. And this
[18:45] will output a natural detail to put and we can name it point. And if we have a look at that, not
[18:54] here. So let's have a look at that point. And you need to enable this. As you can see, it will be
[19:01] 126. And what we need is the number 56. So we need to manipulate here the Y position. So for that,
[19:09] instead of doing a vector to float and float to vector to set the component X and Z to zero,
[19:18] we can do a simple snippet. So this will be easier. And we do, we want to manipulate this. So
[19:25] let's do mean it will be equal to set the vector component and we set the X to zero point zero.
[19:31] The Y can be the mean bounding box dot Y. And then we can set this after zero. So if we output
[19:38] that, I was you can see we were left the point 56, which is the bottom most point, let's say.
[19:45] So let me see, do we have an error? Oh no, that's fine. And let's merge this and continue working
[19:55] the whole. So let me see here. Now we want to bless that point. So let me just not visualize it.
[20:08] Let's do a blast. And we want to work on point. And let's say, let's open this back tick and
[20:18] do a detail zero point, which is attribute and the component zero. And we get that single point in
[20:27] there. From here, we need to create the curve, which will be another exercise we need to figure
[20:35] out how to do. So let's do a point. We can easily create a line and also the kind of thing,
[20:43] but I'm going to complicate just a little bit. So we can continue working on the same geometry.
[20:49] So we have this point. Now we want to add another point below so we can create a line. So from
[20:56] that, I'm going to take the current point position and add. And I'm going to add a constant
[21:03] along a vector. So I'm going to set this to vector. And I'm going to set I want to add along the
[21:11] negative y. I'm also going to multiply constants so I can increase the distance. And if I do this,
[21:20] it will move just a point down that I don't want to do that. I want to keep the same position.
[21:26] So I'm going to get this position and add this. And from here, we can just do one net point.
[21:35] So a point to create that point below. And as you can see, we have that point there. I'm going
[21:42] to set this to one point four was the value I used. And now we can come in here, create an
[21:48] oops, create a net. And just to back group and that will work. But let's try to do this within
[21:56] Vops. So we can we want to add a primitive, which is aligned. So add, cream. And we also need to
[22:03] add vertex. And we need two of those. So the premium number connects to the premium. And the
[22:09] point number, the first one will be the point number. And the second one will be this point. And
[22:16] then we have the curve. So that is fine. Let's move down and do a simple example.
[22:27] Let's this will subdivide the curve. And I'm going to set it to point four.
[22:33] Let's do a sweep and set it to I'm two. And in this case, let me see what sort of settings
[22:42] did I use. So I'm going to set the radius of point oh eight. Twelve columns will be fine. And
[22:48] then the rest, I don't want to touch it. And from here, we can subdivide this. And I'm going to
[22:58] subdivide it. Let's say by two, and later we can work on it. And now I want to create some pattern
[23:04] on this. So for that again, I'm going to use a point pop. And this will be a bit more elaborated
[23:10] for nothing too complicated. So we can create a point drop. And let's say we do a bind it for
[23:19] to export an attribute. Let's name this you or curve you. And I'm going to do a relative point
[23:25] bounding box. Take the position and I'm going to get components, get vector components.
[23:36] And I just I'm just interested in the Y. And I'm going to output this in here. So if we go back
[23:42] and visualize that, as you can see, it will be a value from zero to one from that relative point
[23:47] bounding box zero and one at the top and everything in between. So now we want to manipulate this value
[23:54] to create some details. For that, first of all, we need in order to repeat this this attribute
[24:02] along the curve, we can do the following. You can take this output, create a multiply and create
[24:07] a constant in here. And let's say how many repetitions you want. Let's say 60. Now we just need to
[24:13] module it by one. So wait reps around. And now it will repeat. But we will need more geometries
[24:20] for this. So something like this. And let's see, did I set it to 60? Yes. And now we can just create
[24:30] a ramp to control this. So ramp around. And I'm going to set it to spline ramp.
[24:38] And don't worry about that because we can go back and just set it to wing here again. And we will
[24:44] manipulate that ramp. I also want to move these along the normal. So I want to manipulate the
[24:54] position. So let's get the position and create a net. And I want to move it by this. But I also
[25:02] want to move it along the normal. So the normals are pointing outwards. So I'm going to take the
[25:08] normals and multiply them by this mask and add it to the position. So we will get something like
[25:18] this. And now we need to create in here Constance. And we can tweak the amount in this place. And we
[25:26] also need a normal upwards. So let's set the normals. Let's set this to 0.2. Let me see 0.2.
[25:42] And now we need to manipulate that ramp. And I think we have everything here.
[25:47] we need to go back and manipulate that ramp.
[25:52] And this will be pretty simple, we're just gonna set this to heal and make sure we set it to this plane.
[25:58] And we get this sort of detail, which is nice.
[26:02] So let's merge this, select this one, and this one, oops, this one, this one, and press Alt and drag.
[26:12] And we already have some detail in there.
[26:15] Just to finish it off, I'm gonna grab this resample in here, create a note, and create some detail in here.
[26:24] So in this case, I'm gonna carve.
[26:29] And I'm gonna carve this on the second U and set this to 0.15, 0.15, just to extract that, that particular shape in there.
[26:41] I'm gonna resample it again.
[26:44] So sample.
[26:47] And I'm gonna set this to 0.03, I'm gonna move it up a little bit, because I know it will be, I will be in this transform.
[27:00] And I'm just going to sweep to around 2.
[27:05] And now let's look at this in context, see if we enable this, we control, or just by pressing E.
[27:13] It's not E, it's W, yeah.
[27:16] And we can visualize that, as you can see, I had to move that up to close the shaping there.
[27:23] And I'm gonna set in here the radius, first of all the columns to 24, to have more geometry, radios of 0.14.
[27:33] And I'm just going to manipulate the shaping here, let me try to get some similar to what I got.
[27:39] So this line, oops, this line, gonna set one in here, gonna move this one down to something like this, one in here, and this one here.
[27:54] So something like this, maybe let's move this a bit in.
[28:04] So I don't want to worry too much about it, you can always play with it.
[28:10] And yeah, this is what we got so far, I think we need to create the Truss, and then the ladder, let's do that.
[28:20] So now we want to create some supporting geometry in here.
[28:24] And for that, I'm going to merge in, let me see, is this one?
[28:29] No, let's just go up and create another object merge, Ctrl-X.
[28:33] And let's also move this one in here and create another.
[28:38] And let's paste this in all in here.
[28:41] Now we want to select four points for the start of the supporting geometry.
[28:50] So let's read the range.
[28:53] And I'm gonna select points, go up and copy this column.
[28:58] So it remains procedural.
[29:01] Gonna paste this in here, this will just select the first points.
[29:05] And I'm gonna divide this five or, and I also want to offset it.
[29:11] So I'm gonna copy this and paste and divide this by two.
[29:17] So we've offset something like this, great like this, where?
[29:21] So it's simple enough.
[29:23] Now I'm gonna create in here a group of the Unchared points, so points, and group by edges, and shared edges, and create boundary groups.
[29:34] Now we can group from now, and we want to extract the bottom one.
[29:39] So let's do one and promote two edges and take this box.
[29:45] It's going to work line.
[29:48] And let's convert that line.
[29:51] And now as you can see, we still have that point group.
[29:56] If you can see it in here, we still have that point group.
[30:00] So we can blast that specific point group.
[30:05] And add to remove the primitives.
[30:09] And now we need to do the same with either both to create the line.
[30:14] And just move the points down.
[30:19] But this time we at least, so let's do a point walk.
[30:25] And we can name this, but I'm not going to even bother.
[30:30] So let's go inside.
[30:33] And what we'll do here.
[30:41] So.
[30:45] So if we now take the current point position and just do an add point,
[30:51] we will just have points on top of each other, as you can see.
[30:55] We want to move them down.
[30:57] And that I'm going to set in here.
[31:00] Vector components get component is this one?
[31:06] Not.
[31:09] That's it.
[31:12] Vector components.
[31:15] Yeah, this one.
[31:16] It's been a while since I played with Vops.
[31:18] I've just did this for this video.
[31:20] Maybe to try something different.
[31:23] And in this case, we want to set the Y.
[31:26] I constant in here.
[31:28] Let's set these two minus two.
[31:30] And if we do that, we have the points below.
[31:33] But I don't want to set these negative values.
[31:37] So I'm going to just place and negate afterwards.
[31:40] And it will move them down.
[31:42] This way we can just increase or decrease.
[31:45] And you can totally promote these parameters and work from outside.
[31:49] That's even better.
[31:51] That's in this case.
[31:52] I'm just going to continue.
[31:55] Now, I don't want them like this parallel.
[31:59] I want them to go outwards.
[32:02] So for that, what I'm going to do is to take this vector pointing down.
[32:06] And I'm going to normalize it.
[32:10] And if I do that, as you can see, there will move.
[32:14] They will move.
[32:19] Inwards.
[32:20] If I do multiply constants.
[32:25] And I start to play with this.
[32:27] As you can see, I can move them down.
[32:29] So let's say two in here.
[32:31] Any here is not two.
[32:33] So it is.
[32:35] Am I doing add constant?
[32:38] Just a constant.
[32:41] Sorry, I made a mistake in here.
[32:44] We want to actually to add these to the point position.
[32:47] And now we can manipulate how much sheet goes down.
[32:51] And how much sheet opens or wraps around.
[32:55] So in this case, I'm going to set it to 2 and 2.
[32:58] And from here, we can actually create the curves.
[33:02] So let's do an add-prem.
[33:05] And we want to add vertex.
[33:11] And we want to add vertex.
[33:16] And the first one will connect in here.
[33:21] And duplicate this.
[33:23] Connect the point number in here to here.
[33:26] And connect this one in here.
[33:28] That's fine.
[33:29] Now, in order to orient this properly, we also need an attribute.
[33:34] So for that, I'm going to just normalize the position, I think.
[33:40] And set it to 0.
[33:44] So I'm going to copy this in here.
[33:47] And instead of setting a value, I'm just going to set it to 0.
[33:53] In this case, component 2.
[33:55] And now I'm going to normalize it.
[33:58] And if I bind the point, and let's name the, let's connect in here,
[34:03] set this to vector and up.
[34:08] And I have a look at that.
[34:11] As you can see, it will be pointing out.
[34:14] If we didn't do this, it will point in a direction from the origin.
[34:20] So now, as you can see, the other points don't have the attribute.
[34:23] And we need that.
[34:24] So we can do a set attribute.
[34:28] And we will set a vector attribute.
[34:31] geometry on the point.
[34:32] I want to set the up.
[34:34] And the point is this one.
[34:37] And we can also set the vertex.
[34:40] It doesn't make a difference in this case.
[34:43] But yeah, this is working fine.
[34:46] We have the attribute.
[34:49] Now we can re-sample this.
[34:54] And let me set this to be, in this case, 10 segments.
[34:58] It will be fine.
[35:00] This will define the amount of struts we have or trust we have.
[35:04] And now we can do a simple sweep.
[35:07] Let's set this to run to and three columns.
[35:13] And also set it to columns only.
[35:17] Is it oriented properly?
[35:19] I don't think so.
[35:20] I think we need, let's first of all, degrees of scale.
[35:25] And we need to rotate them.
[35:31] And we need to rotate them.
[35:33] So we need to 90.
[35:36] And now they will be pointing out.
[35:41] So that's fine.
[35:43] Now let's do another sweep.
[35:46] This case set it to run to.
[35:50] And the radius can be just point all one.
[35:56] Now let's go to create the struts.
[36:00] So I'm going to copy this one and make sure I copy the amount of columns.
[36:07] And I copy the radius.
[36:11] And now we can un-down and divide the copy this parameter.
[36:18] And here in the partial, please, we're going to do 360 divided by the amount of columns.
[36:26] So these will just twist the shapes, but they want to create that zigzag.
[36:30] So we will do scale by attribute.
[36:32] And let's create that attribute.
[36:34] It will be just a really simple expression using the attribute expression.
[36:39] And this is still Vex, but it's really simple.
[36:43] We're just going to set column, call it rule.
[36:46] And I'm going to set it to PtNum module.
[36:49] As you can see, it will create twists in that create that effect.
[36:54] Now we can simply copy the sweep and sweep it.
[36:58] In this case, I will go off point all of 750075.
[37:05] Let's merge those two.
[37:08] And let's merge everything and see where we add.
[37:12] Oops.
[37:15] Let's create it now.
[37:17] Let's remove any visualization we have.
[37:20] And we now just need to create the letter.
[37:23] Let's do that next.
[37:26] So for the letter, we can copy this in here.
[37:33] Let's clip it and this will be the end of our letter.
[37:37] So along Y, and we will clip it to a value of 0.1.
[37:43] Let's do all primitives and not put the clip edges.
[37:46] Let's convert line.
[37:50] And let's select sweep edges, connect this plant.
[37:53] Let's do a loop by range.
[37:57] And we will again select, let's say, 1 of endpoints.
[38:05] So the amount of points we have.
[38:08] And let's select points.
[38:10] And it will be in there so we can go up, copy again these.
[38:17] And paste these in here.
[38:20] Let's divide these by two.
[38:22] And it will select that point.
[38:24] From here, we can bless that.
[38:28] Just bless that point or just isolate that point.
[38:31] So group one.
[38:34] And if we check these by pressing E, we add that point in there, as you can see.
[38:44] So now let's manipulate this in point drop.
[38:52] So this will be pretty simple, which is going to take the position and add to it.
[38:58] And now you know how to do this.
[39:01] Set this to vector.
[39:04] And I'm going to move the first point along the negative x axis.
[39:10] And also a bit down to.
[39:13] So 0.7.
[39:16] And I'm going to multiply constants.
[39:20] And add these in here.
[39:23] And add points.
[39:25] Add points.
[39:30] And the point is, I need to decrease this to about 0.72.
[39:38] And now I'm just going to duplicate this.
[39:41] And this also.
[39:43] And this one, I'm just going to move it down.
[39:46] So 0 minus 1.
[39:51] 0 minus 1.
[39:53] And I'm going to move it from that point.
[39:56] So as you can see now is moving there.
[39:58] And I'm going to scale this by 2.3.
[40:01] So quite a bit down.
[40:03] And that's it.
[40:04] Now just going outside and create an ad.
[40:08] And do this by group.
[40:11] And there we have our leather or the beginnings.
[40:15] Now what it makes sense to do this next.
[40:18] So let's do.
[40:21] In your sweep.
[40:23] I'm going to set this to ribbon.
[40:25] Let's see how that looks.
[40:26] So we've already entered the other way around.
[40:28] Let's set this to y.
[40:30] And I'm going to set this to 2.1.
[40:34] And set this to columns.
[40:36] And just create the sweep.
[40:38] Round 2.
[40:39] Round 2.
[40:42] And I just need to decrease this by about 0.015.
[40:46] 1.015.
[40:48] Now in the other side, I'm going to first of all create a re-sample.
[40:54] Because we don't have enough points.
[40:56] The fault settings will be fine.
[40:58] So my spacing, let's do a sweep.
[41:03] And I'm going to set this to ribbon.
[41:08] Again, we can just copy from here.
[41:11] So set this to ribbon.
[41:13] But instead of going to set it to rows.
[41:16] And copy the width from here.
[41:19] And let's just do another sweep.
[41:22] I can copy this one.
[41:24] At this time point of 1.
[41:28] And if we merge these.
[41:31] We can see we still have these end frames that I don't want.
[41:35] So I can come in here and do a blast.
[41:38] And let's blast point is 0.
[41:40] And to blast the last one, we can open the back tick.
[41:43] And do end frames.
[41:45] The amount of primitives in the incoming geometry minus 1.
[41:49] And that will blast the last one.
[41:52] So let's see where we add.
[42:00] And that's our ladder.
[42:03] Now, just as a bonus, I'm going to do a texture projection in here.
[42:08] And we will create a logo to project in there.
[42:11] So let's do that next.
[42:13] So instead of grabbing a logo online, we're just going to create one.
[42:18] So for that, I'm going to create a copnet.
[42:21] I'm going to name this logo.
[42:24] And first of all, we're going to need some.
[42:29] We're going to create a font.
[42:33] And this door to beat this shape.
[42:35] But for that, I'm going to create some custom movies.
[42:38] So let's do a subimport.
[42:41] Create a circle.
[42:43] And let's set these to be 64 divisions.
[42:48] And let's wash it by 0.5.
[42:51] And let's do a custom car.
[42:53] Let's set this to open arc.
[42:55] I believe.
[42:56] Let's do it in here at the top.
[42:59] And you will see in a bit where we're going with this.
[43:02] So 614 is the value I choose in a value of 0.805.
[43:08] Let's match this.
[43:10] So we can have some action in our loop.
[43:14] Let's do a re-sample.
[43:18] Share how much did I use in here.
[43:20] 0.1 is fine.
[43:22] Let's do a sweep.
[43:25] Let's set it to ribbon.
[43:29] And default settings will be fine.
[43:32] But I won't do it in here.
[43:34] The pity college roots, which is just an attribute that goes along the columns.
[43:39] So 0.1 to 3 and so on.
[43:41] And from here, I want to create a disabled visualization.
[43:46] And let's do a UV button.
[43:50] But as you can see, the UVs are not following the counters.
[43:53] I'm going to rectify the group.
[43:55] But now they are upside down.
[43:57] So what we can do is create a group in here.
[44:01] Let's set it to points.
[44:03] And that's pt.co is equal to 0.
[44:06] So we can increase it, as you can see.
[44:09] I'm going to set it to 0.
[44:11] Now I'm going to group promote.
[44:15] Group 1 to vertices.
[44:18] And if I go into the UV flatten and enable in here, the group 1.
[44:22] It will align better, as you can see.
[44:25] So let's create an output.
[44:27] And that's our geometry.
[44:31] Let's restarize this.
[44:34] So, restarize setup first.
[44:38] Position is fine.
[44:40] And we're going to do bounding box and scale to fit.
[44:43] Restarize geometry to get the UVs.
[44:46] Let's put in here the UV and set it to UV.
[44:51] And now we can create our logo.
[44:55] So I'm just going to name it.
[44:58] I'm going to pick a funding here.
[45:00] So can't be bothered.
[45:01] I'm going to make a chest or field.
[45:06] It's based on the reference I saw.
[45:08] I'm going to scale this to 0.26.
[45:11] And now we can do a UV sample from this.
[45:16] So if we do a UV sample.
[45:21] And select this as texture and this as our UVs.
[45:26] And we of course need to transform this because it's not in the correct space.
[45:31] So let's translate this and move again.
[45:35] This let's scale this to 1.6.
[45:39] And maybe scale it to 0.78.
[45:45] And as you can see we have a bit of work.
[45:48] But now we have this more interesting shape instead of just this one.
[45:52] Which I like.
[45:55] So let's set this to 2K.
[45:59] Let's create some color from this.
[46:04] So mono to RGB.
[46:11] Let's select here the white and pick some dark brown.
[46:18] Let's convert to a PNG.
[46:22] So RGB to RGB.
[46:25] Let's select this as RGB and this is alpha.
[46:29] Now we have transparency as you can see.
[46:32] And finally we're going to route output this.
[46:36] Let's name this.
[46:39] Shaster new dot PNG.
[46:42] Oops.
[46:44] Like this.
[46:46] Shaster new dot PNG.
[46:50] Let's default settings are fine.
[46:52] Oh, I need to connect these copets and render to this.
[46:56] So now we're going up and we're going to use a custom tool that you can have access on my Patreon.
[47:02] So let's do a texture projection CGS.
[47:06] And first of all we need to unwrap these.
[47:09] There's this handy tool to unwrap cylinders from labs.
[47:13] Let's do the texture projection.
[47:18] So how good.
[47:19] And let's project here.
[47:22] Somewhere around here.
[47:24] Let's pick that logo.
[47:29] So it's in the render folder.
[47:33] And we have it.
[47:35] Now I can scale it a little bit.
[47:38] Something like this.
[47:40] Let's set this to 4K.
[47:44] And let's create just an hour.
[47:49] And yeah guys, that was basically it.
[47:52] So I don't know how many of you follow to the end.
[47:56] And but I still want to manipulate this.
[48:00] I want to move this a bit up.
[48:04] So maybe that's better.
[48:07] Yeah, that's better.
[48:09] So I don't know how many of you follow to the end, but please let me know in the comments if you did.
[48:13] And if you enjoyed this one, as always, you can grab this projection tool on my Patreon alongside with hours and hours of exclusive tutorials.
[48:22] All the project files from my videos, including this one.
[48:25] And yeah, if you want to support my work, consider supporting me on Patreon.
[48:30] Thank you for watching.
[48:31] And I guess I'll see you next time.
[48:33] Thank you.



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
