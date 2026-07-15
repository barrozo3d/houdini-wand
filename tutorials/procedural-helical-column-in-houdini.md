---
title: Procedural Helical Column in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=HDIIwy11otU
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.319"
tags: [vdb, vex, intersection-analysis, orient-along-curve, quad-remesh, architecture, column, box-clip]
extraction_status: complete
frames_dir: tutorials/frames/procedural-helical-column-in-houdini/
frame_count: 14
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Helical Column in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=HDIIwy11otU)
**Author:** cgside
**Duration:** 36m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video we'll be continuing our procedural modeling techniques.
[0:08] This time we'll be building this helical column and it will be a good chance to learn a few techniques.
[0:18] It might look a bit too simple at first but we will have a challenger to face.
[0:25] So yeah let's get started.
[0:28] So let's start by dropping a geopontainer and we will start with a spiral.
[0:36] So it's a spiral and we will set the i220.
[0:45] Change this to be explicit and reduce and set it to 1.
[0:51] And I'm gonna set here 1.2 for the radio scale and 5 turns.
[0:59] Something like this.
[1:01] And we might want to play with a start angle.
[1:06] In my case I used a value of 207 but you feel free to use your own.
[1:15] So this will be our base and now let's drop a line.
[1:23] And it will be on the y-axis and let's match size to the spiral.
[1:32] And let's see that scale to fit and we will need to resize it a bit so we can transform.
[1:41] I'm gonna scale it up by 1.2.
[1:45] So i and y, 1.2.
[1:49] And let's merge this and sweep it with a round tube.
[2:02] So round tube and we will need to increase the size.
[2:10] So let's go with 12 divisions and a radius of 1.
[2:17] And we can set the end cap to single polygon.
[2:24] And we might need to change the thickness individually.
[2:29] So for that I'm gonna place here a netribe with just float for the p-scale.
[2:36] And set this to 1.1 and for the default 1.2.
[2:44] So slightly bigger.
[2:47] And now we can start to clip this.
[2:54] So let's clip on the y-axis.
[2:59] So 0, 1, 0.
[3:02] So it clips the bottom.
[3:05] That's fine.
[3:07] Now let's clip the top.
[3:10] So drop another one.
[3:13] And we want a distance of 15 and primitive below the plane.
[3:23] And make sure we fill the polygons on both.
[3:27] So we can VDB this out.
[3:32] And that's what we're going to do next.
[3:35] So let's create a VDB from polygons.
[3:39] And I'm gonna set it 0.1 is fine.
[3:45] So we have this.
[3:47] Now we need to smooth it because otherwise it will look...
[3:52] It will have this low polygon look.
[3:56] So let's VDB smooth as the F.
[4:00] And we will smooth it quite a bit to have that round that transition.
[4:06] So let's go for 20.
[4:08] So as you can see we already have this low, helical look.
[4:13] And if we convert this now to polygons...
[4:20] It still will look...
[4:24] ...low quality.
[4:26] I'm not sure if it's going through the recording.
[4:29] But I'm seeing some artifacts.
[4:32] So we will have to do some adjustment in here.
[4:37] First of all we will create a VDB re-sample.
[4:45] And we will create use voxel size and go for 0.3.
[4:52] So we will re-sample the VDB.
[4:55] Then we will reshape it.
[4:58] Since we're going to smooth it, so reshape as the F.
[5:02] Since we're going to smooth it, it's better to dilate it a bit.
[5:05] So one is fine.
[5:07] And then we can drop a smooth as the F.
[5:11] Smooth as the F.
[5:13] For iteration is fine.
[5:16] And let's look now.
[5:18] We have a more high quality and result.
[5:23] So let's continue next.
[5:27] So I want to do some operations with this mesh.
[5:32] And this is too high poly.
[5:34] So let's try to quadrimash it.
[5:37] Just with the default...
[5:41] Aldeni native node.
[5:45] We want like 5,000 is more than enough.
[5:49] And we have a smooth result which is fine.
[5:52] We can always subdivided later.
[5:54] So now we will create some railings in here.
[6:00] I don't know how to call it properly.
[6:03] So let's go in here.
[6:10] After the sweep, we create a node.
[6:14] So now we can create an intersectional analysis.
[6:18] We want to create a railing shape that goes over here,
[6:23] over the intersections.
[6:26] So let's create an intersection analysis.
[6:28] And that is already giving us the result we want.
[6:32] Let's just output as a curve.
[6:38] And now we can copy this clip.
[6:47] Make it a reference copy.
[6:51] And this will clip to bottom.
[6:53] And maybe copy this one.
[6:57] But for this one...
[7:01] So for the first one we might want to change the distance to 0.01.
[7:06] So it cuts near the grid.
[7:13] And now we don't have any small parts going on.
[7:18] So we can just...
[7:21] Let's see...
[7:22] Let's polypads to join the curves.
[7:25] So polypads.
[7:27] And let's see...
[7:30] Now we can just re-sample.
[7:36] And let's see the final result.
[7:39] So let's use a length of 1 and use subdivision curves.
[7:46] And now we want to use yet another re-sample.
[7:49] But this time we point or wait.
[7:55] Subdivision curves is fine.
[8:00] Okay.
[8:03] Now after this we can place an only new...
[8:10] And let's re-decurves to the mesh.
[8:18] Because we want them in that specific position.
[8:24] And we want to change it to a minimum distance.
[8:28] So as you can see it's on the mesh.
[8:31] And it's where we need them.
[8:35] So right in there.
[8:38] But it's a bit jagged.
[8:40] As you can see the points are a bit going up and down
[8:43] due to the minimum distance algorithm.
[8:46] So let's place a smooth.
[8:51] And we will go like 50.
[8:53] And this will look better.
[8:56] It's already better.
[9:00] And now what will we do next?
[9:04] We can create the sweep.
[9:08] Since we want to create those railings.
[9:11] I keep calling it railings.
[9:14] But there must be a decent name for that.
[9:18] So we want to create this.
[9:21] And now go with the normal.
[9:25] And let's check how it looks.
[9:32] It's not looking bad.
[9:38] But in this case I want to create a specific shape.
[9:43] Which is more elongated in one side.
[9:46] So for that I'm going to create a lap simple shapes.
[9:52] And this will be a wadz.
[9:56] And not equal.
[9:58] So copy the top to the base.
[10:01] And I'm going to use point four in here.
[10:06] And one point seven.
[10:09] Let's see how that looks.
[10:14] It looks something like this.
[10:16] And let's go on the x-wipe plane.
[10:20] And let's use this to sweep.
[10:24] And let's change this to cross section.
[10:28] And of course we need to scale down this to point three.
[10:37] But as you can see, we need to orient this somehow.
[10:42] Because it won't look correct over our mesh.
[10:48] As you can see.
[10:50] So we need to create an orient attribute or an app and normal vectors to point them down.
[10:59] So let's do exactly that.
[11:02] Or maybe I'm thinking here.
[11:06] Maybe we can transfer the normals.
[11:12] Maybe we can do that.
[11:15] Let's try.
[11:18] And let's see, first of all, if we have normals and redone.
[11:22] So let's create normal on points.
[11:27] And let's transfer those normals.
[11:33] And this is looking alright.
[11:36] So I'm just testing.
[11:38] I did it in a different way.
[11:41] And now we can attribute swap.
[11:47] And let's swap the normal for the app.
[11:52] And we will move.
[11:56] And let's see.
[12:03] Still giving us a few issues.
[12:06] So let's try an oriental on curve.
[12:13] And do this as app.
[12:19] Not really what I was expecting.
[12:22] So let's maybe try 1.1 in here and 0.4 in here.
[12:33] And this is my like it.
[12:36] Although we have some issues.
[12:47] But maybe we can just attribute blur.
[13:00] Let me see.
[13:02] Not attribute blur in here, but let's see.
[13:15] Let's maybe attribute blur in here.
[13:20] Let's instead begin.
[13:23] Let's keep it to default.
[13:26] And do a few iterations.
[13:30] I'm not showing me the end.
[13:38] Oh, I'm doing the attribute swap.
[13:42] So let's blur it.
[13:46] We go with 500.
[13:50] And now we can swap it.
[13:54] And create the sweep.
[13:57] Does that help?
[14:04] Maybe it's because our curve is a bit messed up.
[14:20] Oh, okay.
[14:22] Let's not be in the border points.
[14:25] And now do the attribute swap and the sweep.
[14:31] Let's see.
[14:32] And that is looking better.
[14:35] Let's try 300.
[14:38] So that is looking fine.
[14:40] Let's see how it looks over our mesh.
[14:44] And it's almost perfect.
[14:49] I believe this way.
[14:51] So maybe we can decrease the size.
[14:54] Sorry for this.
[14:57] Rumble.
[14:58] But I was trying something different in here.
[15:02] And maybe you could learn a thing or two.
[15:09] So that's basically done.
[15:11] Now let's focus on the next part.
[15:15] So now we need to create some points here on this middle part
[15:20] to place the flowers.
[15:24] And we will need a bit of wax for that.
[15:29] So maybe in here after the smooth.
[15:33] Let's create another one.
[15:36] And we have these shapes, these curves.
[15:41] So we need to create center points.
[15:44] So let's maybe try to do this quickly.
[15:51] So we will need XYZ distance to measure the distance between the two curves.
[15:59] So let's go with the floats.
[16:01] This equals XYZ this.
[16:05] And it will be on input one.
[16:09] And we will need to set a green group.
[16:12] In this case primitive one.
[16:15] And on the position.
[16:18] And we will also use sample only the first curve.
[16:24] And the group types set to primitives.
[16:28] Now we will need to create a point.
[16:31] So int point equals to add point.
[16:36] We are on the incoming geometry.
[16:39] And we will set the position to be at p dot x.
[16:48] Let's just divide it here.
[16:51] And at p dot z.
[16:54] And on the y we will add.
[16:58] So we'll add the distance divided by two.
[17:03] And this should place it in the center.
[17:09] Not in the center but where we want it to be.
[17:14] So let's see.
[17:16] In this case not really.
[17:24] Let's see why.
[17:32] This should be in here.
[17:39] So maybe let's...
[17:42] Yeah it's negative in this case.
[17:45] Because the order of the curve must be swapped.
[17:49] Let's check.
[17:51] And yeah it's correct now.
[17:54] So that's it.
[17:56] That's our middle points.
[17:59] And now we will group them.
[18:02] So set point group, set point group.
[18:08] And it will be on the incoming geometry.
[18:11] And let's call it center points.
[18:15] And the point number will be pt.
[18:18] We just created and set it to 1.
[18:22] So if we check our points and we have the center points.
[18:29] So now let's isolate those points.
[18:33] So let's blast.
[18:35] And a little non-selected.
[18:38] And let's create a curve from it.
[18:41] And I should do the trick.
[18:43] And it does.
[18:45] Re-sample.
[18:47] Because we have way too many points.
[18:51] So we will re-sample by a length of point five.
[18:57] And set it to subdivision curves.
[19:00] That is fine.
[19:02] Now we will need those normals.
[19:07] So we can just object margin.
[19:15] This geometry.
[19:18] I believe is this one.
[19:21] Yes.
[19:25] And let's use Vax again to transfer those normals.
[19:33] So we need to create an int, it's pre-m.
[19:36] Because we will need this for the premium wave functions.
[19:41] So vector it, your VW.
[19:46] And we will create x, y, z, this, z, one.
[19:51] In this case, which is the column, V of p, and it pre-m.
[20:00] And it your VW.
[20:03] Which so many spaces.
[20:07] And now we can just...
[20:11] In this case, I'm not getting the normals.
[20:13] I'm getting the UVs.
[20:16] Will that be useful for me?
[20:20] I don't think we need this.
[20:23] Let's sorry about that.
[20:27] Because I was experimenting with cops.
[20:31] And patting the end, I don't need those UVs.
[20:35] So I was just going to sample the UVs to have them on the curves.
[20:40] But I don't actually need them.
[20:42] So let's just set in here.
[20:46] Outpoints.
[20:50] And I will just create...
[20:56] I will use again this geometry.
[20:59] And ray that...
[21:04] In this case, set to minimum distance.
[21:07] And it will be right on the center.
[21:11] And we might need a peak over here.
[21:20] But we need to import actually.
[21:24] We need to sample the normal.
[21:28] Normal.
[21:30] And now if we pick...
[21:32] As you can see is working.
[21:34] So let's keep it lightened for now.
[21:39] And...
[21:48] We will re-sample this now.
[21:55] To 0.6.
[21:58] So it doesn't change much.
[22:01] And set it to subdivision curves.
[22:04] And now we want to place some flower patterns in here.
[22:10] So let's see.
[22:15] And let's create that for now before we orient it.
[22:22] So I'm going to start in here with a circle.
[22:30] Which will be four divisions.
[22:33] Since we want to create...
[22:35] It's a very simple setup.
[22:38] And create a circle again.
[22:42] We want say 64.
[22:44] Just copy to point.
[22:48] Oops, this is in here.
[22:52] And this will be just fine.
[22:57] And let's boolean for union.
[23:02] Boolean.
[23:04] Set it to union.
[23:09] Let's dissolve light edges to remove those inner geometry, inner edges.
[23:17] And now you have two options.
[23:19] You can either remesh it.
[23:21] So remesh.
[23:24] And you will have something like this.
[23:26] You can play with the iteration then smoothing.
[23:29] You will either do that.
[23:30] But since I have the...
[23:33] The exercise quad remeshera, I will use it.
[23:38] So set to 500.
[23:43] And let's see.
[23:45] And smear around the X and Y.
[23:48] We can try the quad remesh, but it won't work really well.
[23:54] As you can see, so let's set this to 500.
[23:59] As you can see, it's not really good.
[24:03] Maybe we can remesh it first and then quad remesh it.
[24:09] Let's try that.
[24:10] Even that is a bit of a mess.
[24:14] So either way, either remesh or the exercise quad remeshera.
[24:21] I'm going to go with the quad remeshera.
[24:25] And now we want to create an inner amask.
[24:30] So we can change the...
[24:34] So we can change the depth of this flower.
[24:37] So it goes a bit on the second on the right part.
[24:42] That way they can overlap in a pattern.
[24:45] I hope that makes sense.
[24:47] So let's create an attribute to just float.
[24:52] And this will be called center.
[24:55] First before that directional mask, we will create one from the center.
[25:01] So let's visualize it.
[25:03] And we want this to be a radial.
[25:07] And let's just... let's invert it and place it in here.
[25:13] And something like this will be fine.
[25:17] I guess.
[25:19] Let's duplicate this and call this one mask X.
[25:25] And let's set it to bounding box.
[25:28] Let's reverse this and see.
[25:34] And we might need to change the interpolation in here.
[25:47] So first of all this needs to be on the X.
[25:51] So it's correct.
[25:53] And let's change the interpolation to B spline.
[25:58] Does that make a difference?
[26:01] I believe so.
[26:02] On the geometry it will.
[26:05] And now let's just displace it.
[26:08] So to have center, we want it to be flat.
[26:16] And we have the directional mask to change the depth.
[26:24] So let's create an attribute triangle which will be a lot simpler to work with.
[26:32] And we will do a position on the Z.
[26:36] We will be plus equals to F at mask X times channel flow to which we will be called this.
[26:51] And let's see how that goes.
[26:53] So we'll increase this.
[26:55] It will create this fall off.
[27:04] Why is not changing it to this plane?
[27:11] Is this bleep?
[27:16] I guess it is.
[27:22] So maybe change it to bezier.
[27:25] So that is fine.
[27:28] And let's go with point 25.
[27:32] So this way they can overlap when we copy them around.
[27:38] And let's also do if center bigger than point 7.
[27:51] We can set the Z position to be minus and let's make it point 25.
[28:02] So we have this indentation.
[28:08] And let's maybe smooth it.
[28:15] And the default settings are fine.
[28:20] And let's set through it.
[28:22] So poly extrude.
[28:25] And we will go distance of point 3.
[28:30] And now we can bevel it.
[28:35] Ignore flat edges.
[28:37] Increase the angle.
[28:39] And this case I went to a value of point 26 and 3 subdivisions.
[28:50] So this I guess will be fine.
[28:56] Now we can create the center parts.
[29:02] And let's just tool that quickly with the tube.
[29:10] And along the Z axis and the radius of point 1.25.
[29:17] A knight of point 24 and 64 columns and end caps.
[29:26] Now just blast the primitive zero and poly fill it.
[29:34] So we can have a rounded look with the quadrilateral grid.
[29:41] It's always a difficult word to say.
[29:44] Quadrilateral.
[29:46] So let's increase the surface offset to point 5.
[29:51] And other than that is fine.
[29:54] Totally fine.
[29:55] We can replay with these.
[29:58] And now we can just match size.
[30:09] And let's see.
[30:12] We can march this.
[30:19] And in the match size we will need to adjust the depth.
[30:23] So in this case I used a value of minus point 2.
[30:30] And set this to min and max.
[30:36] So this is totally fine.
[30:40] So let's maybe take this and create a subnet out of it.
[30:46] And name it flower.
[30:50] And we have an output already.
[30:52] So it's fine.
[30:55] And now we can copy this over.
[31:00] So let's actually do that next.
[31:03] So copy the points.
[31:05] And let's see how that looks.
[31:08] Of course we need to create some orientation attributes.
[31:12] As this won't look much, let's first of all change the p-scale.
[31:17] Set a uniform p-scale.
[31:19] So let's reboot the just world.
[31:22] And set a p-scale of point 2, which is fine.
[31:27] And now this should be pretty simple.
[31:32] So let's create first the...
[31:37] Let's create an aperture root.
[31:39] And then we can add a length of length.
[31:43] Because we already have the normals.
[31:47] As you can see.
[31:50] So this is looking fine.
[31:52] We just need to create the app.
[31:56] So the app will be on here.
[31:59] So app.
[32:04] So it's oriented on the tangent.
[32:08] And the natural root is just vector.
[32:12] Because we need to rotate to where the flower has that indentation.
[32:19] So it works that direction.
[32:22] And let's see if this is similar to the file I have.
[32:26] So we want to orientate the app.
[32:29] Change to direction only.
[32:31] And rotate around the normal.
[32:36] So this is correct.
[32:38] And change this to minus 90.
[32:41] So yeah, this is correct.
[32:46] Let me check.
[33:00] Do we have the normals correct?
[33:05] I'm recomputing them now.
[33:07] So that's why they weren't correct.
[33:10] So now they are.
[33:12] So as you can see, we just rotated them to have that indentation.
[33:18] And the same goes for the app, which will orient them properly.
[33:24] So finally, we can start to learn some of these.
[33:33] So this one and this one.
[33:38] And finally, this one.
[33:43] And of course, it will be a bit out of place because we need to pick it a little bit.
[33:56] Something like this.
[34:04] Let me check.
[34:06] In this case, I used point of four.
[34:13] So as you can see, it's not really perfect because I actually forget we need to create a bend the four.
[34:25] I bend the former.
[34:27] So let's create a bend.
[34:32] Press Enter, B.
[34:35] Change the angle in this case to 26.
[34:38] And clip pressing B.
[34:40] So this is it.
[34:42] So let's just set this to 0 and 0.
[34:45] And the farming both directions.
[34:47] So this should be fine.
[34:50] Let's see how that looks now.
[34:56] And that is looking better.
[34:59] It's not perfect, but you know, this is what we got today.
[35:08] So hopefully you got something out of this.
[35:11] I believe I'm not forgetting anything.
[35:15] And sorry, if I did any mistake, I'm open to suggestions in the comments.
[35:22] If you have any, and other than that, just check out my Patreon where you can find all the project files from my videos alongside with exclusive tutorials.
[35:35] And I also have the 3R4 courses, which are pretty cheap, so you can have a look at those.
[35:44] And yeah, thank you for watching and I'll see you next time.
[35:48] Bye.
[35:49] Okay, guys, I actually forget something.
[35:52] We can create here a box clip.
[35:55] Labs box clip.
[35:58] And we will create also a bound.
[36:01] So we can tile these a little bit.
[36:05] And in the bounds, you want to play with the values, but I have some values of minus 1.2.
[36:18] To clip the bottom and minus 2.1 to clip the top.
[36:24] And we can just play some edge size.
[36:28] And set this to min.
[36:30] And now you can tile these anyway you want it.
[36:35] I mean, you can tile it vertically.
[36:38] So yeah, that's it. See you.



---

## Captured Frames

- [0:40] tutorials/frames/procedural-helical-column-in-houdini/frame_000.jpg
- [2:10] tutorials/frames/procedural-helical-column-in-houdini/frame_001.jpg
- [4:20] tutorials/frames/procedural-helical-column-in-houdini/frame_002.jpg
- [5:40] tutorials/frames/procedural-helical-column-in-houdini/frame_003.jpg
- [7:40] tutorials/frames/procedural-helical-column-in-houdini/frame_004.jpg
- [10:40] tutorials/frames/procedural-helical-column-in-houdini/frame_005.jpg
- [14:00] tutorials/frames/procedural-helical-column-in-houdini/frame_006.jpg
- [18:00] tutorials/frames/procedural-helical-column-in-houdini/frame_007.jpg
- [19:20] tutorials/frames/procedural-helical-column-in-houdini/frame_008.jpg
- [23:20] tutorials/frames/procedural-helical-column-in-houdini/frame_009.jpg
- [28:20] tutorials/frames/procedural-helical-column-in-houdini/frame_010.jpg
- [32:30] tutorials/frames/procedural-helical-column-in-houdini/frame_011.jpg
- [35:00] tutorials/frames/procedural-helical-column-in-houdini/frame_012.jpg
- [36:20] tutorials/frames/procedural-helical-column-in-houdini/frame_013.jpg

---

## Structured Notes

### Core Technique
Build a helical (twisted-braid) decorative column by sweeping a tube along two offset copies of a Spiral primitive, VDB-smoothing/reshaping the swept twist into a clean high-quality mesh, then deriving the ornamental "railing" ribbon geometry directly from **Intersection Analysis** of the two braid strands (rather than hand-modeling it), and finally decorating the middle band with quad-remeshed flower ornaments copied along a VEX-computed center curve and bent to hug the column's curvature.

### Summary
Two Spiral primitives (radius scale 1.2, 5 turns, tuned start angle) are offset — one scaled up slightly (1.2 in X/Y) — merged, and swept with a round tube profile (12 divisions, radius 1, single-polygon end cap), with per-primitive p-scale variation (1.1/1.2) giving the two strands slightly different thickness. The swept mesh is clipped top and bottom, converted to VDB, heavily VDB-smoothed (SDF, ~20 iterations) for the characteristic soft braided look, then refined via VDB Resample (voxel size 0.3) → VDB Reshape (dilate ~1) → another VDB Smooth pass to eliminate low-poly artifacts before converting back to polygons and Quad Remeshing (~5000 target) for a clean, subdivision-ready base mesh. The ornamental ribbon/railing that traces the strand intersections is generated procedurally via **Intersection Analysis** on the pre-VDB swept curves (output as curves), cleaned up with paired Clip nodes (one close to the ends, one further in) to remove stray fragments, joined with Poly Path, then double-Resampled (subdivision curves) for clean density. These curves are **Ray**-projected onto the finished mesh (Minimum Distance) to snap them to the surface — smoothed afterward (~50) since minimum-distance projection tends to leave points jagged. The actual railing profile comes from a **Labs Simple Shapes** Quad (unequal top/base sizing for an elongated cross-section) swept along the projected curve using Cross Section mode; orientation is the trickiest part — after trying normal transfer and attribute swap, **Orient Along Curve** combined with a heavily-blurred "up" attribute (Attribute Blur, ~300–500 iterations, pinned border points) gives the cleanest, twist-consistent orientation for the swept ribbon. Center-band decoration points are derived with a hand-written VEX wrangle: `xyzdist()` measures the distance between the two braid curves at matching points, and a new point is added at the midpoint (`(p1.x+p2.x)/2, p1.y + dist/2, (p1.z+p2.z)/2`, with curve-order-dependent sign correction) — these points are grouped, isolated via Blast, converted to a curve, Resampled, then Ray-projected (Minimum Distance) onto an Object-Merged copy of the mesh with sampled normals (Peak-adjusted) to sit correctly on the surface. Flower ornaments are built from two circles Boolean-unioned, Dissolved (light edges), then Quad Remeshed (author's paid tool, ~500 target — plain Remesh works too but looks worse) for clean topology; a radial "center" mask plus a directional "mask_x" (bounding-box-derived, B-spline/Bezier interpolation) drives a VEX position offset (`P.z += mask_x * depth`, with a conditional dent for `center > 0.7`) so each petal recesses/overlaps realistically when copied in a ring pattern; Smooth, Extrude (~0.3), and Bevel (ignore flat edges) finish the petal shape, with a separate Tube-based center boss (blasted/poly-filled end cap, surface-offset rounded) match-sized into place — the whole thing collapsed into a "flower" subnet. Flowers are Copy-to-Points'd along the resampled center curve (uniform p-scale ~0.2), oriented via an aperture-root/up-vector setup (`up` set from a rotate-around-normal vector at -90°) so each flower's indentation faces the correct direction, then a final **Bend** (~26°, both directions) curves the flat flower band to hug the column's helical curvature. A bonus tip at the end shows using **Labs Box Clip** with a Bound node (tuned min/max values) to easily tile the finished column vertically for repeated architectural use.

### Key Steps
1. **Base braid geometry**: two Spiral primitives (radius scale 1.2, 5 turns, offset start angle) → merge with an offset/scaled (1.2x/1.2y) duplicate → Sweep with Round Tube profile (12 divisions, radius 1, single-polygon end cap) → per-primitive p-scale variance (1.1 vs 1.2) for slightly different strand thickness.
2. **Clip and VDB smoothing**: Clip top and bottom (fill polygons on both) → VDB from Polygons (~0.1 voxel) → VDB Smooth SDF (~20 iterations) for the soft braided silhouette → VDB Resample (voxel 0.3) → VDB Reshape (dilate ~1) → another VDB Smooth pass → Convert to Polygons → Quad Remesh (~5000) for a clean base mesh.
3. **Railing/ribbon curve generation**: run **Intersection Analysis** on the pre-VDB swept curves (output as curve) to automatically find where the two braid strands cross; clean with two Clip passes (one tight near the ends ~0.01, one further in) to remove stray fragments; Poly Path to join, then Resample twice (subdivision curves) for clean point density.
4. **Snap curves to the finished mesh**: **Ray** node set to Minimum Distance projects the curves onto the quad-remeshed surface; Smooth (~50) afterward to fix the jaggedness minimum-distance projection introduces.
5. **Railing cross-section + orientation**: build an elongated quad cross-section via **Labs Simple Shapes** (unequal top/base sizing), Sweep it along the projected curve using **Cross Section** surface type (scaled down ~0.3); after testing normal-transfer and attribute-swap approaches, settle on **Orient Along Curve** combined with a heavily blurred "up" attribute (Attribute Blur ~300–500 iterations, pinned border points) for correct, twist-consistent ribbon orientation.
6. **Center-band point derivation (VEX)**: measure the distance between corresponding points on the two braid curves with `xyzdist()`, then `addpoint()` a new point at the computed midpoint (`(p1.x+p2.x)/2`, `p1.y + dist/2`, `(p1.z+p2.z)/2`, with a sign fix depending on curve winding order); group these new points, Blast to isolate, Convert to a curve, Resample.
7. **Project center curve onto mesh**: Object Merge the finished mesh, transfer normals via VEX (primitive-intrinsic UV lookup then abandoned in favor of a simpler direct sample), **Ray** (Minimum Distance) to snap onto the surface, Peak-adjust slightly, Resample (~0.6) for the flower-placement curve.
8. **Flower ornament build**: two Circles (4 & 64 divisions) Copy-to-Points'd and **Boolean Union**'d, Dissolve (light inner edges), then Quad Remesh (author's paid Exoside-style tool, ~500 target — plain Remesh is an option but looks worse).
9. **Petal depth variation**: build a radial "center" mask (inverted) and a directional "mask_x" mask (bounding-box-derived, B-spline/Bezier ramp interpolation), then in an Attribute Wrangle offset `@P.z += mask_x * ch("depth")`, adding a conditional dent (`if (center > 0.7) @P.z -= 0.25`) so petals overlap/recess realistically once arrayed in a ring.
10. Smooth, **Extrude** (~0.3), **Bevel** (ignore flat edges, angle-tuned, 3 subdivisions) for the petal relief; build a separate center-boss **Tube** (blast + Poly Fill the end cap, surface-offset rounded), Match Size into place; collapse the whole flower network into a **subnet** for reuse.
11. **Distribute flowers**: Copy to Points along the resampled center curve with a uniform p-scale (~0.2); orient via an aperture-root "up" vector, rotated around the normal (author uses -90°) so each flower's indentation faces the correct direction relative to the column's twist.
12. Finish with a **Bend** deformer (~26°, applied in both directions) to curve the otherwise-flat flower band so it properly hugs the column's helical curvature.
13. **Bonus tiling tip**: use **Labs Box Clip** fed by a **Bound** node (tuned min/max — e.g. -1.2 bottom, -2.1 top) to easily clip/tile the finished column vertically for repeated architectural placement.

### Houdini Nodes / VEX / Settings
Spiral, Sweep (Round Tube profile, single-polygon end cap, per-primitive p-scale), Clip, VDB from Polygons, VDB Smooth SDF, VDB Resample, VDB Reshape (dilate), Convert VDB, Quad Remesh, Intersection Analysis (curve output), Poly Path, Resample (subdivision curves), Ray (Minimum Distance projection), Smooth, Labs Simple Shapes (Quad, unequal sizing), Sweep (Cross Section surface type), Orient Along Curve, Attribute Blur (up-vector smoothing, pinned borders), `xyzdist()` VEX function, `addpoint()` VEX function (midpoint curve derivation), Blast, Object Merge, Circle (Boolean Union), Dissolve, Quad Remesh (petal topology), radial "center" mask + bounding-box "mask_x" mask (B-spline/Bezier ramp), Attribute Wrangle (position-offset petal depth, conditional dent), Extrude, Bevel, Tube (center boss, surface-offset), Match Size, Subnet collapse, Copy to Points (uniform p-scale, aperture-root/up-vector orientation), Bend (both-direction curvature), Labs Box Clip + Bound (vertical tiling).

### Difficulty
Advanced (Intersection-Analysis-derived ornamental geometry, VEX-computed midpoint curves, and the multi-attempt orientation solve for the swept ribbon are all non-trivial production techniques).

### Houdini Version
20.5.319 (visible in viewport title bar).

### Tags
vdb, vex, intersection-analysis, orient-along-curve, quad-remesh, architecture, column, box-clip

---

## Related Tutorials
- [Environments in Houdini Part 2 - Stone Bridge](environments-in-houdini-part-2---stone-bridge.md) — related architectural-column/structural-element modeling from the same channel.
- [Modern Furniture Modeling in Houdini](modern-furniture-modeling-in-houdini.md) — shares similar decorative-ornament copy-to-points and orientation techniques.
- [Procedural Buildings in Houdini | Tips and Tricks](procedural-buildings-in-houdini-tips-and-tricks.md) — shares Intersection-Analysis-adjacent ornament/architectural detailing tricks from the same channel.
