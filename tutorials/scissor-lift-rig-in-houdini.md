---
title: Scissor Lift rig in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=QPiEZM1o-ME
author: cgside
ingested: 2026-07-13
houdini_version: "21.0"
tags: [rig-doctor, ik-chain, point-transform, matrix, kinefx, scissor-lift, procedural-rigging]
extraction_status: complete
frames_dir: tutorials/frames/scissor-lift-rig-in-houdini/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Scissor Lift rig in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=QPiEZM1o-ME)
**Author:** cgside
**Duration:** 22m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in today's video I wanted to create these rig from scratch,
[0:05] even including modeling the parts.
[0:07] So it will be a quick exercise, but hopefully you'll get away with some new techniques.
[0:12] So yeah, let's get into it.
[0:14] So I'm gonna pause this and jump into another scene.
[0:17] Let's create a Geocontainer.
[0:19] Let's not waste too much time, create a line, we'll start just from a line.
[0:23] And this one will be along the Y axis, but I'm gonna center it, so I'm gonna take the
[0:27] length as always, paste it on the offset, multiply it by half, and negate it.
[0:33] So it stays at the center.
[0:35] I'm also going to set the points, so my num block is not working.
[0:41] Okay, 10 points.
[0:43] And I'm gonna enumerate this.
[0:46] So I'm gonna give each point an ID, so let's change it to points, and let's do ID.
[0:54] Then we're gonna create the zigzag pattern, that should be simple enough.
[0:58] So let's do it with a wrangle, just offset every other point.
[1:02] Let's name it zigzag.
[1:06] And for this, we will do, we will change the position.x, so v at p.x, it will be equal
[1:14] to, so let's do I at pt num and 1, and let's multiply it by an amplitude.
[1:24] And let's see, if we do this, this will move only to the positive side, so it will be
[1:30] either 0 or 1, or every other one.
[1:33] So what we can do to make it 0 centred, so from minus 1 to 1, or to the example to slider,
[1:39] we can take this and just 0 centred it, so multiply it by 2.0, minus 1.0.
[1:49] And that way we have it 0 centred.
[1:50] So let's just set an amplitude of 0.065, so now we have the zigzag 0 centred.
[1:57] So that wasn't too hard, and I also want to group these points in here, but maybe I
[2:05] can get away with it just by, because I wanna cut these lines in this point for my rig.
[2:14] So what we can do, let's see, point cut, and these are the even, so I think I can do
[2:22] the following cut and do all every other two.
[2:26] So let's do an exploded view, I think that will work.
[2:30] Yes, that will work, I just want this, the cards like this.
[2:35] So we can skip setting a group in here, I'm not sure if I'm gonna need it later, but
[2:40] let's skip it for now.
[2:42] Now we want to blast the primitive 0, because I don't want that extra cream, so blast primitive
[2:49] 0, what am I 0?
[2:54] Okay, then we will create an all in here, this is already in both, and I'm gonna sort
[3:01] both the primitives and the points by y.
[3:05] So let's do that by y, and by y, so it starts in here and goes up, it's fine.
[3:13] Next, we're gonna create, we're gonna initialize the rig, so rig doctor, and we just need this
[3:21] and initialize transform.
[3:22] So now we have a transform, and a local transform that we will need.
[3:25] We don't need to do anything else.
[3:29] And the next step is to create the IK chains, so we don't want to do an IK chain for each
[3:37] one, we will just do for one, and then copy the transforms to all the other components.
[3:43] So let's do the following, let's create an all in here, just in case, and let's blast
[3:49] let's be the primitive 0, yeah, let's just blast primitive 0.
[3:57] Then we can just for good measure, we can parent joints and see if the order is correct, otherwise,
[4:02] yeah, this is the parent child, parent child, that's correct.
[4:06] And then we can do word rig pose, just to pose our rig, and we will change in this case the point,
[4:15] so let's see our name attribute, so we have 0.01 and 2, and we want to change, so we want to move
[4:22] this point to down, but this is not doing the IK chains, we need to do it next, so let's do
[4:28] IK chains, and this is for a 2-bone IK chain, this node, so what we want to do is create one,
[4:36] and just say 0.0 is our root, so in here, 0.1 is our mids, and the tip will be 0.2, and if we do
[4:45] match by name, now we can do the IK chain, but as you can see it's only working for one point,
[4:52] for one chain, we need to copy to the other ones, instead of creating for all the other ones,
[4:57] and even that I'm not sure if it would keep the same offset between the chains, so the way I'm
[5:03] going to show you, it will work even better possibly. Just to preview, I'm going to do a simple
[5:09] animation in here, but I'm just going to do, let's see, because just up and down movement of time,
[5:20] 200, but that's probably too fast maybe, so maybe we want to fit it between some values, so let's see,
[5:30] this goes between minus 1 and 1, so we will fit this, so we can do fit, that's fit 1, 1 work,
[5:39] with H-crypt, let's see, yeah it should work, so from minus 1 to 1,
[5:44] to let's say 0.1 and minus 0.2, let's see if that works, any tests, that were good,
[5:52] and now we just need to copy to the other ones, but in order to copy, we need to calculate the offset
[5:58] between this 0.0 and 0.2, so that's what we're going to do now, let's place a wrangle,
[6:05] and let's copy, let's create distance attributes, and it will be equal to F, at underscore this,
[6:13] and it will be just, we can do length instead of creating several variables, and we can just do a
[6:20] subtraction between the vector, the point position, so 0.0, I want the position, so position of 0.0,
[6:29] and let's copy this, and just subtract 2.1, and this should give us the distance, let's have a look,
[6:40] so this, we don't want to hold the points, right, let's see, where is the distance, it's in here, and
[6:55] so 0.0 and 0.2, it's not 0.1, sorry, it's 0.2, and now we should have an updated distance, yeah,
[7:04] an animated distance, but maybe I'm going to do this differently, then my setup, I'm going to set it
[7:08] to detail, and let's see, yeah, we have the value there, we only need a single value, and now we just
[7:14] need to copy the transforms, and we could possibly do it with the rig attribute VOP, but I'm going to
[7:21] try to do this with the rig wrangle, just by copying some functions, that I kind of looked using
[7:31] the rig attribute VOP, and I'm going to use the rig attribute wrangle, so we don't want to transform
[7:38] either 0.0, 0.1 or 0.2, so instead of filtering in here, I'm just going to do it in here, so if
[7:45] I, at ptn, is bigger than 2, so if it starts in 0.3, and we're going to open this,
[7:55] we're just going to process those, but I still want to access the first few points, so what we want to do
[8:02] is to, for every third point, we want a pattern of 0.1, 2, 0.1, 2, so we can copy from a source,
[8:08] this source points, to all the other ones, using that pattern, so we'll do a pattern near,
[8:14] called, star, spt, and it just be i at ptn, module, 3, so this will give a 0.1, 2, 0.1, 2, and so on,
[8:25] then we can copy the point transform, this is not the local transform, this is the world
[8:29] transform, so matrix, ours, world, it will be equal to this function called point transform,
[8:37] and we will copy from the source, pt, so we just want to copy from these three points,
[8:45] even if we are iterating over these points, we will still copy from 0.1, 2, because we have this
[8:50] pattern, and now we want to set the matrix, these matrix y components to have the offset of the
[8:56] distance, so we will do a source, world dot, w, y, which is the called y component of the matrix,
[9:07] and we will multiply it by the distance, no, we will add the distance, and multiply it by
[9:14] available that I'm going to create, which is the i at index, and this index is something I forgot
[9:22] to create, which is at here at the top before the rig doctor, let's create a wrangle,
[9:29] let's name it index, and this will be on point, but I'm going to source the prime number,
[9:34] so i at index, it will be the prime number, which we'll just give as a point attribute,
[9:41] or for each, we will get a point attribute, but targeting each prime, so every shine let's say,
[9:49] so this is our index, we have the distance, now we multiply, we added the distance multiplied by
[9:54] each index, now we just need to set the point transform, so for that there's only one line missing,
[10:02] which is set point transform, we also have transforms if you want to iterate over, input 0,
[10:09] the current point number, using the matrix or swirls, and just make sure we set it to 1,
[10:15] so what is this last value, I'm not sure, let me see, oh we set it as constraint, yes,
[10:25] okay, and now if we look, so we just copy the transform from the first three points to all the
[10:32] other ones, and making sure we set up the correct distance also, so that's basically it,
[10:38] now we just need to create some geometry, so for that, so if you want to skip the remaining part,
[10:46] I understand that, because the core idea is done, but if you want to end up with some geometry
[10:51] transform, let's keep going, so i'm going to create in your convert line, so i want to transform
[10:59] each segment to a line, so that's correct, now after that I want to poly cut every segment,
[11:07] so poly cut, because this doesn't cut the geometry, so poly cut and cut everything,
[11:16] so each line becomes independent, then I want to create the pattern of the Cesar lift,
[11:21] so for that I'm just going to create a wrangle, and basically extend these lines, so that way,
[11:27] so let's see if we can do that, so let's name it extend, and let me just do a minute a bit,
[11:35] and for that we will grab the pivot, which is the pivot of each line, the first position of each line,
[11:43] and for that we will use pre-move, first input, we want to grab the position from each
[11:50] pre-move, and we will grab the position 0.0, and it's a vector, so it's always a good practice,
[11:58] to do it as a vector, in this case it's not the zero component, it's the last element, because the
[12:04] curve starts here, at least that was what i said it before, so we can actually see that by using a
[12:12] resample, not resample, and just create curve view, and let's see, yeah as you can see, the line
[12:18] starts at this part, and goes to 1, so we want actually the 1 value, because we want to extend
[12:23] from here, we want to scale the line from this point, so it extends, hopefully that was clear,
[12:29] then it's simple, we just scale by 2, so we do v at b minus equal to pivots, to move the lines,
[12:37] to a resposition, then we do v at b multiply by 2.0, then we extend it, and then we do v at b,
[12:45] plus equal pivots, to move it to the original position, so we have successfully extended lines,
[12:53] so that's one part, now we want to sweep this, basically i want to create these rounded geometry
[13:00] from these lines, so some like ribbon lines, but we'd rounded ends, so let's do that, let's
[13:08] create first a sweep, and we want to create, let me see in here, we want to create a ribbon,
[13:17] but oriented in the z axis, let's reduce this, to maybe 0, 0 to 3, let's get rid of the numbers,
[13:28] let's change the columns to 1, make sure we do read, I think, and we don't want what we're
[13:37] letters, we want columns, so we get something like this, now we can, if we do this let's see the
[13:45] ID it will be messed up, so we need to promote this, to primitives, so id from point to primitives,
[13:55] and let's see maybe 1, 1 to change this to minimum, yeah, it will start at 0, I know this
[14:02] This color is 0 and this one is 1, so it's correct.
[14:06] And now we can use, because some points are open, so let's do an exploded view actually
[14:13] to check.
[14:14] Yeah, that should be working.
[14:17] Let's see if this is... no, that's okay.
[14:20] So we have individual elements and then we can do also polypads, because right now we
[14:26] might have more primitives than we want.
[14:28] We just want one primitive parallel image.
[14:32] And then we will polyfill to create some geometry, because I don't see the other way to create
[14:39] geometry from this.
[14:40] So I'm just going to polyfill it.
[14:42] Let me see.
[14:43] I think I use single polygon and we're going to get rid of the curves.
[14:50] So I have something in here, remove curves, based on a premium trinzig.
[14:54] So let me see, remove curves.
[14:56] So it's just this command.
[14:58] If the primitive is closed, we remove the primitive.
[15:02] We remove the primitive, yes.
[15:03] So this will just remove the curves.
[15:06] But as you can see, we lost our idea to put.
[15:08] But fortunately enough, we have in here the same amount of primitives, so 8, if you can
[15:13] see here, I know it's a bit small, we have the same amount of primitives.
[15:16] So what we can do, just with a wrangle.
[15:20] So this one is remove curves and we can copy the ID from here.
[15:25] So copy ID.
[15:30] So this will be on primitives.
[15:33] So we have ID in here on primitives.
[15:35] So we can do I, let's underscore underscore ID.
[15:39] It will be I at op input, input one ID.
[15:46] Let's see if that works.
[15:48] And it does.
[15:49] So we have to do an underscore and then the name of the attribute, which in this case
[15:52] is three underscores.
[15:53] So as you can see, let's see.
[15:55] That's working.
[15:57] So now we did it, when we polyfill, we lose the attribute.
[15:59] So we had to copy over and we are copying from the input that has the same amount of primitives.
[16:04] So that's important.
[16:06] Or if you're doing on points, it's the same way.
[16:09] Then what we can do, we can second this.
[16:14] So let's do a second.
[16:18] And this is dragging to a long lesson.
[16:20] So both directions, and let's do 0.005.
[16:25] But as you can see, we got geometry on top of each other.
[16:28] We want to offset every other one.
[16:31] So for that, we will do a simple wrangle.
[16:36] So let's do wrangle.
[16:39] And we need to take into consideration that thickness.
[16:41] So we need to copy this value.
[16:43] So for that, I'm just going to create a float.
[16:46] Seatness.
[16:48] Seat, jaff, click.
[16:53] And we will also need the index of float in the RID.
[16:59] Let's do, let's name it index anyways.
[17:02] And it will be the prime function.
[17:04] And we will read the ID because we have it on primitives and using the prime number.
[17:12] Since this geometry is disconnected, it will be OK.
[17:14] So we will have no problem.
[17:17] Let's just create this and copy this thickness and make sure we multiply it by 2.
[17:24] Because in here, we did it on both directions.
[17:27] So it's actually duplicated or multiplied by 2.
[17:31] So let's do the offset now, which will just be a float of the index module 2, multiply
[17:41] by the thickness.
[17:43] And now if we do position dot z plus it was offset.
[17:48] So every other one, every other ID, it will offset.
[17:51] And we get the correct offset.
[17:54] So this will be offset.
[17:57] And now we need, we have the geometry.
[17:59] And we need to connect this to the geometry, to the capturing.
[18:05] So let's do a capture, pack geometry.
[18:09] But we have two options.
[18:14] We either create a pattern to connect each piece, each ID to this side or we do it manually.
[18:22] In this case, I'm going to quickly create a pattern for the name of the root.
[18:26] So I'm going to create the name of the root.
[18:28] So let's do it quickly.
[18:29] Basically, we want, let's see.
[18:34] We want to connect this point to one piece and the second point to other piece.
[18:43] And do it always like that.
[18:44] Keep every third point.
[18:46] So for that, let's create the name of the root.
[18:50] And this will be a bit tricky.
[18:52] We have to do basically a group first.
[18:57] That will be I underscore underscore ID divided by two.
[19:02] So make sure we set these on primitives.
[19:04] Then we will create a pulse, which will be I at underscore underscore ID module two.
[19:11] Maybe there are other ways, but this is the way I ended up doing.
[19:14] And then as a name, it will be a concat.
[19:19] This is just to join strings.
[19:23] And since the name attribute on the points, so let's actually have a look at that.
[19:28] So this is point underscore.
[19:30] So we need to do the same in here.
[19:32] Let's start with point just underscore.
[19:35] Then we do integer to string or to ask a group.
[19:41] And we skip every third one and add the position.
[19:45] So that should work.
[19:48] So let's have a look all that looks in the end.
[19:51] So we have point zero point one and then skip to point three point four, then skip to point six, seven, and so on.
[19:59] And now we simple, we just to capture back geometry and we do a packing put.
[20:03] We don't want to pack using connectivity.
[20:04] We want to use using name and we capture by attribute name.
[20:07] Let's see if we have and we have the capture working.
[20:10] So this just simplified our lives.
[20:13] And now we can do a simple bone the form.
[20:16] Oh, and we don't want to do this in here.
[20:18] We want to do this at the rig doctor, of course, at the rest post.
[20:22] And now we do a bone the form.
[20:25] And this is the last bit of the tutorial.
[20:27] So let's maybe connect it in here and connect this one to the different one.
[20:32] Let's just name this copy X form.
[20:36] Now let's have a look and now let's see.
[20:39] And yeah, it's working.
[20:41] As you can see, this is the end result.
[20:45] Maybe just because this one will be back now so we can maybe unpack and do a better visualization of this with the name attributes for the ID.
[20:55] Let's say that maybe change the colors a bit.
[21:00] And let's just create the new and this will be the out.
[21:05] So yeah, guys, that's basically it for our tutorial.
[21:08] I really hope you have enjoyed this.
[21:10] It was a bit longer than I expected, but I think I share I share the few techniques that might be useful for you in the future.
[21:20] So on Patreon this this file will be available on Patreon, but I'm also going to share some different setups from these toolbox rig that we have done before.
[21:32] So I'm going to share this full file and I also have this is our lift.
[21:37] Same way, I'm also going to share this piston that I did.
[21:41] And also these for bar linkage.
[21:45] As you can see using the in this case, the full body IK.
[21:50] So yeah, if you are interested in getting those files, this will be part of the Patreon benefits for this month.
[21:55] So yeah, you can grab them there.
[21:57] As always, thank you for watching.
[21:58] You can leave a comment if you feel like and roast me in the comments if you want.
[22:03] And other than that, thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:45] tutorials/frames/scissor-lift-rig-in-houdini/frame_000.jpg
- [2:10] tutorials/frames/scissor-lift-rig-in-houdini/frame_001.jpg
- [3:40] tutorials/frames/scissor-lift-rig-in-houdini/frame_002.jpg
- [5:20] tutorials/frames/scissor-lift-rig-in-houdini/frame_003.jpg
- [6:40] tutorials/frames/scissor-lift-rig-in-houdini/frame_004.jpg
- [7:40] tutorials/frames/scissor-lift-rig-in-houdini/frame_005.jpg
- [9:10] tutorials/frames/scissor-lift-rig-in-houdini/frame_006.jpg
- [10:50] tutorials/frames/scissor-lift-rig-in-houdini/frame_007.jpg
- [13:00] tutorials/frames/scissor-lift-rig-in-houdini/frame_008.jpg
- [15:00] tutorials/frames/scissor-lift-rig-in-houdini/frame_009.jpg
- [16:30] tutorials/frames/scissor-lift-rig-in-houdini/frame_010.jpg
- [19:10] tutorials/frames/scissor-lift-rig-in-houdini/frame_011.jpg
- [20:50] tutorials/frames/scissor-lift-rig-in-houdini/frame_012.jpg

---

## Structured Notes

### Core Technique
Rig and model a scissor-lift mechanism from scratch: build a single 2-bone IK chain in KineFX's Rig Doctor, then **copy that one chain's world transforms to every other repeating scissor segment** via a from-scratch VEX point-transform read/write (`pointtransform()`/`setpointtransform()`) driven by a repeating index pattern — avoiding the need to build an IK chain per segment — followed by procedural cross-brace geometry generation (extend, sweep, offset-thickness) and a name-pattern-based Pack/Capture setup that skips manual per-piece binding.

### Summary
The rig starts from a centered 2-point Line (points enumerated with an `ID` attribute), deformed into a zigzag with a wrangle that offsets alternating points' X position (`(ptnum % 2) * amplitude`, zero-centered via `×2−1`) — a simple, loop-free way to build the classic scissor pattern. Points are grouped in threes via `pointcut` and an exploded view to visualize the pairing, then the primitive-0 curve is blasted away, sorted by Y, and fed into **Rig Doctor** (Initialize Transform) to set up the base rig skeleton and local transforms. Rather than building an IK chain for every scissor segment, a single **2-Bone IK Chain** is built once (root/mid/tip = points 0/1/2, matched by name) and animated/posed as a preview (time channel fit between two rotation-limit values). To propagate that one chain's motion to all other segments, the **distance between point 0 and point 2** of the animated chain is measured each frame (`length(pos(0,"P") - pos(0,"P",2))`) and stored as a detail attribute — this becomes the fixed spacing multiplier for the copy step. A **Rig Attribute Wrangle** (built by hand rather than the Rig Attribute VOP) then processes every point beyond the first three: using a repeating 0/1/2 pattern (`ptnum % 3`) as a "source point" index, it reads the **world transform** of the corresponding source point via `pointtransform()`, then modifies that matrix's Y-translation component by the earlier distance × a per-segment `index` attribute (built separately as `prim_num` promoted to points) — before writing the result back with `setpointtransform()` — reproducing the single animated chain's pose at every repeating segment position with correct spacing, all without a second IK setup. Geometry is then generated: Convert Line per segment, Poly Cut to separate each into independent curves, then an **extend wrangle** scales each curve outward from its pivot (`P -= pivot; P *= 2.0; P += pivot`) to lengthen the cross-brace arms past their rotation points. A Sweep (ribbon) with computed vertex/primitive IDs, Polypath (single-polygon), and a **remove-curves** wrangle (deletes closed primitives) turns the extended lines into flat ribbon geometry; since Poly Fill drops the earlier ID attribute, it's copied back in from a same-primitive-count reference via `op:input1'ID`-style indexing. A **Thicken** node (both directions) gives the ribbons volume, but pushes overlapping segments on top of each other — fixed by an offset wrangle that alternates thickness direction based on `(ID % 2)`, scaled by the thickness value ×2 (since Thicken already doubled it). A procedural **capture-region naming scheme** (`"point_" + ID/2 + "_" + (ID%2)`, built to skip every-third-point via the same `%3` logic) lets **Capture by Name** and **Bone Deform** bind all the flat cross-brace ribbons to the rig automatically, matched purely by string name rather than manual per-piece assignment.

### Key Steps
1. Build a centered 2-point **Line**, enumerate points for an ID attribute, then deform into a zigzag via `(ptnum % 2) * amplitude` (zero-centered) — a loop-free way to generate the classic scissor pattern.
2. Group points in threes via **Point Cut** and visualize with an Exploded View to confirm pairing; blast the primitive-0 curve, sort by Y, and feed into **Rig Doctor** (Initialize Transform) to build the base rig skeleton.
3. Build a single **2-Bone IK Chain** (root/mid/tip = points 0/1/2, matched by name) and pose/animate it as a preview reference — this is the *only* IK chain built for the entire rig.
4. Measure the **distance between the animated chain's point 0 and point 2** each frame (`length()`), store as a detail attribute — this becomes the fixed spacing multiplier used to propagate the pose.
5. Build an `index` attribute (primitive number promoted to points) and a repeating `ptnum % 3` "source point" pattern to identify which of the 3 chain points each other point should copy from.
6. In a hand-written **Rig Attribute Wrangle** (skipping points 0–2, the original chain): read the source point's **world transform** via `pointtransform()`, modify its Y-translation by `distance × index`, and write it back with `setpointtransform()` — propagating the single chain's animated pose to every repeating segment with correct spacing, no additional IK needed.
7. Generate cross-brace geometry: **Convert Line** per segment, **Poly Cut** to fully separate curves, then an **extend wrangle** (`P -= pivot; P *= 2.0; P += pivot`) to lengthen each curve past its rotation pivot.
8. **Sweep** (ribbon) the extended lines, **Polypath** (single polygon), and a **remove-curves** wrangle (deletes closed primitives) to get flat ribbon geometry; copy the earlier `ID` attribute back in via a same-count reference wrangle since Poly Fill drops it.
9. **Thicken** (both directions) for ribbon volume; fix overlapping segments with an offset wrangle alternating direction via `(ID % 2)`, scaled by thickness ×2 to account for Thicken's own doubling.
10. Build a procedural **capture-region name** per piece (e.g. `"point_" + ID/2 + "_" + (ID%2)`, using the same `%3`-based logic to skip the every-third source points), then use **Capture by Name** + **Bone Deform** to bind all cross-brace ribbons to the rig purely by string match — no manual per-piece capture assignment.

### Houdini Nodes / VEX / Settings
Line, Enumerate (ID attribute), zigzag point wrangle (`ptnum % 2`, zero-centered scale), Point Cut, Exploded View, Blast, Sort (by Y), Rig Doctor (Initialize Transform), 2-Bone IK Chain (root/mid/tip by name), `fit()` animation preview, `length()`/`pos()` distance-measurement wrangle (detail attribute), Rig Attribute Wrangle (`pointtransform()`, `setpointtransform()`, `ptnum % 3` source-index pattern, `index` attribute via primitive-number promotion), Convert Line, Poly Cut, extend wrangle (pivot-relative scale), Sweep (ribbon), Polypath, remove-curves wrangle (closed-primitive deletion), ID-attribute-copy wrangle (`op:input1` reference), Thicken (both directions), offset wrangle (`ID % 2` alternating direction), procedural capture-name wrangle (string concatenation), Capture by Name, Bone Deform.

### Difficulty
Advanced (the single-IK-chain-to-many-segments propagation via manual `pointtransform()`/`setpointtransform()` matrix manipulation, and the procedural string-based Capture-by-Name binding, are both sophisticated, non-obvious KineFX rigging techniques).

### Houdini Version
21.0 (visible in viewport title bar).

### Tags
rig-doctor, ik-chain, point-transform, matrix, kinefx, scissor-lift, procedural-rigging

---

## Related Tutorials
- [Shoe Laces in Houdini VEX and Vellum](shoe-laces-in-houdini-vex-and-vellum.md) — shares procedural point-placement and matching-by-name/index tricks for repeating mechanical geometry.
- [Procedural Helical Column in Houdini](procedural-helical-column-in-houdini.md) — shares the VEX-driven mechanical/architectural geometry-generation philosophy (Sweep, extend, thicken) used here.
- [Think Procedural Think Houdini](think-procedural-think-houdini.md) — shares the from-scratch per-instance transform-matrix construction philosophy used here for propagating the IK chain's pose.
