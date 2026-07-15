---
title: Procedural Duct Tape in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=D6449n2Pvcc
author: cgside
ingested: 2026-07-13
houdini_version: "21.0.359"
tags: [wrinkle-deformer, uv-flatten, area-scale-factor, xyzdist, object-merge, tape, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-duct-tape-in-houdini/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Duct Tape in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=D6449n2Pvcc)
**Author:** cgside
**Duration:** 16m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So before we jump into making the tape, I'm gonna start by modeling a simple pipe like this banded pipe.
[0:10] So I'm gonna set a radio scale of 0.5 and 10 rows. And I'm also going to pick and catch.
[0:20] Then I want to target this primitive. So I'm gonna sort the primitives by Y.
[0:28] And we get 0 at the bottom that way I can do what poly-inch.
[0:34] And I'm gonna target the primitive 0. I just want to move the primitive 0.
[0:40] And I'm gonna change this to position and direction to be procedural.
[0:44] And I'm gonna use on the Y the bounding box. The Y mean.
[0:50] So I want to move from that position. And now I can just offset in here.
[0:56] So let me just set this to 0. And I want to set this to 90 of course.
[1:04] And this value can be something like 0.6. So we get something like this.
[1:09] Then we can mirror this. And let me see how I did this. So on the X that's fine.
[1:15] But I want to use the bounding box 0, the X max.
[1:21] Yeah. Then I want to match size this. I'm just jumping through this quickly.
[1:29] And then we can just create a hole.
[1:33] So this is our initial shape. Now let's place the tape in here.
[1:39] So let me organize this.
[1:43] And for the tape I'm gonna use, first of all, I'm gonna target this side.
[1:48] So for that I'm gonna use a group expression.
[1:51] And I'm gonna name this left left and one.
[1:57] And I'm gonna choose in here preset, left side. So we're speaking both.
[2:02] So I'm gonna do and VFP dot X is less than 0. So we get this one.
[2:10] Now we can get the spiral.
[2:14] And you will see how we did that.
[2:17] Why we did this group in a bit.
[2:20] So I'm gonna do a spiral.
[2:22] Gonna change the I to 0.475 is a value of 1.12.
[2:27] 4.5 turns.
[2:31] I'm also gonna change these two explicit.
[2:34] And I'm gonna pick the radius of the tube. So radius scale.
[2:39] Let's actually see that and paste.
[2:43] And copy these and paste in here.
[2:47] And now we need to divide this by two.
[2:51] Oops, whatever I done.
[2:53] So divide this by two. So we get same radius.
[2:55] But I'm gonna increase just a bit.
[2:57] Now I'm also going to open these lightly.
[3:00] So multiply it by 0.975.
[3:05] So we get no other lives when we wrap it around.
[3:09] And then I'm just gonna do a match size.
[3:13] And match these two here.
[3:16] And make sure I do use groups.
[3:19] And in the target group, I choose left and gone.
[3:22] And then I can just move it down.
[3:25] Let's say by negative 0.5.
[3:28] So we get something like this.
[3:30] And this is our spiral.
[3:35] That we're going to mesh.
[3:39] So that I'm gonna do a sweep.
[3:44] Set these two ribbon.
[3:49] And I fight a bit with this.
[3:51] But basically we need to use the same end up vector.
[3:55] And I also want to compute your V's and normalize your V.
[4:00] No, let's find compute your V's because we want this full strip.
[4:05] And then in the surface, which is gonna roll it.
[4:09] So in here, I'm gonna roll it by minus 90.
[4:13] Let's see.
[4:14] And then we want to change the width column.
[4:18] So that's fine.
[4:19] And we to 0.115.
[4:22] So we get something like this.
[4:25] So we have to use these.
[4:27] Now, I don't like these huge UVs.
[4:30] But our other option is to add them compressed like this,
[4:34] which I don't want because I want to use those UVs for something.
[4:38] So I'm just gonna do a UV flatten.
[4:40] Let's look at UVs.
[4:43] And we want to preserve seams and island boundaries.
[4:47] And we had these results.
[4:50] So that's fine.
[4:52] Now we will move these to UV space over the split.
[4:59] UVs split.
[5:01] Blit UV seems that's the thing.
[5:03] I just want to promote it.
[5:04] We don't need this.
[5:05] We could just have promoted because we only have one island.
[5:08] But either way, it's a good practice.
[5:10] And I'm gonna subdivide this.
[5:13] And I'm gonna subdivide this by 3 for now.
[5:18] So quite a bit.
[5:19] But still, we only got 60k frames.
[5:22] So that's fine.
[5:24] Then we're gonna create an urinal
[5:26] because this is our original position
[5:29] that we will later deform.
[5:33] Then we want to move these UVs to the position.
[5:40] So let's do that.
[5:41] And we will see an issue.
[5:43] So UV to be.
[5:46] And let me just resize this.
[5:51] And we can do the following.
[5:53] You can do vector UV.
[5:55] It will be equal to V at UV.
[5:58] And vector pulse.
[6:00] We can manipulate in your swissile the position.
[6:03] So let's do V at UV dot X.
[6:06] Along the Y, we can set it to zero.
[6:10] And along the Z, we can set it to Y.
[6:15] Not V at UV, sorry.
[6:17] We don't need to.
[6:19] We have that variable.
[6:21] And we free to V at V equals pause.
[6:24] We move these to UV space.
[6:29] But we might want to reverse this in here.
[6:33] So the problem with this is, you can see,
[6:35] we have a huge size difference.
[6:37] And these will artist when we try to displace the final mesh.
[6:41] So in order to have the same ratio, the same size,
[6:45] we need to measure the, I didn't found another way.
[6:48] So what we will do is to measure.
[6:51] The area throughout, we want the full area, not by primitive.
[6:54] That's costly.
[6:55] And we don't need that.
[6:58] And then we will name this area, target.
[7:02] Then we will measure again the area after we moved it to this.
[7:07] Let's name it UV position.
[7:09] Let's name the area area source.
[7:12] Then we're gonna scale this.
[7:16] Scale ratio.
[7:20] Scale factor.
[7:23] And let me see, we just need to divide one area by the other.
[7:28] So let's do float source.
[7:31] Area source to be able to film.
[7:35] And we get the area source.
[7:38] And we can begin a primitive, so just zero.
[7:41] Then we can do area targets.
[7:45] And name the same in here.
[7:48] And then we can do float factor.
[7:51] And since we are dealing with areas, we need to do a square root.
[7:55] So we divide the target area.
[7:58] Area target by the area source.
[8:01] So we have a scale factor.
[8:03] And then we can just do VLP times equal factor.
[8:08] And we get, if we look now, so before we moved it,
[8:14] it's a bit hard to see.
[8:16] But as you can see, we should have about the same thickness and length.
[8:21] So now this will help us to have the correct displacement at the end.
[8:26] So we still have UVs, which is important.
[8:31] And after this, we will do the deformation.
[8:36] And we won't use any solver.
[8:39] We will just use an alternative, which is the ring called a former.
[8:46] And then we want to create a null in here.
[8:50] And let's name this rest.
[8:54] And now I want to create another null.
[8:58] Let's just create a null in here.
[9:00] One for the geometry to deform.
[9:03] And another for the rest.
[9:06] We don't want to do anything to the rest.
[9:08] We just want to affect the geometry to the form.
[9:13] So let's do an attribute, now is even vector.
[9:17] And we will change the position.
[9:20] So this will be a bit too much.
[9:23] So I'm going to play with this, so zero centred.
[9:26] So we get both positive and negative values.
[9:29] And I put a load of zero five.
[9:32] So just a little bit.
[9:33] Then we can reduce the element size to something like this.
[9:37] And I also played with an offset that worked well for me.
[9:42] So something like this.
[9:44] Then we can do hybrid terrain.
[9:47] The both settings will be fine.
[9:49] And I also want to scale along the Y.
[9:51] So first of all, I don't want to move along the set probably, probably.
[9:55] Maybe we can change that later.
[9:57] But I want to change the amplitude to 0.3.
[10:02] Is this what I'm going for?
[10:04] So if I do the ring called the former, we start to see the duct tape emerging.
[10:12] Those wrinkles.
[10:14] But I want to play in here with this.
[10:17] So I'm going to first of all, increase the constraint iteration, change this to cloth.
[10:24] And I'm going to play with the rest of the scale.
[10:26] So increase a bit the cloth.
[10:27] So with the forms a bit more.
[10:29] Then I'm going to increase the smooth iterations.
[10:32] So we get something like this.
[10:34] I hope you can see through the recording.
[10:36] You can see we have these fake wrinkles.
[10:39] Well, they are pretty real in this case.
[10:42] Not so fake.
[10:44] So I think that's all for now.
[10:49] What we can do, that's all for the wrinkle deformer.
[10:53] I mean, you could try to play with the noise.
[10:56] As you can see, we get a different pattern.
[10:58] You can try to play with the amount of subdivisions.
[11:03] So you can see this case three will be more than enough.
[11:08] You can play also with the algorithm in here.
[11:11] The topology you can play with surface struts.
[11:15] It's not bad, right?
[11:17] Maybe we can increase the folds or we can decrease them.
[11:21] The size of the folds.
[11:23] But I prefer the cloth presets.
[11:25] So yeah, I think I'm going to stick with it.
[11:28] You can also increase these to have more.
[11:32] Or cloth to play with.
[11:34] It's just like the ballon, rest on scale.
[11:37] And yeah, I'm talking too much.
[11:39] So I'm just going to do in here the deformation.
[11:42] So I'm going to take the original position and take the rest.
[11:47] With the object merge, we have done this object merge quick.
[11:51] Quick.
[11:54] I mean, I did a video on this where you can use a simple python script
[11:58] to create this quick object merge on command.
[12:01] So that's it if you're curious about.
[12:03] And let's do the deformation.
[12:05] So let's notice the form.
[12:07] We want to move this back to the original position, which is this one, but with the deformation.
[12:13] So maybe there are easier ways, but I'm going to connect the rest, which is this before the deformation.
[12:20] And I'm going to connect in here the original position on the 13th.
[12:25] And then I can just do an x-wise list.
[12:29] So far the x-wise it is.
[12:31] We will need premium.
[12:32] We will need an X-prem.
[12:35] So int X-prem, which is a target.
[12:39] And we also need a vector.
[12:42] And I'm going to name it X-UVW.
[12:44] You can name it whatever you want, like it.
[12:47] Prem and it.
[12:48] U-VW.
[12:49] That's more common or source.
[12:50] Prem.
[12:51] So U-VW.
[12:52] Anyways.
[12:53] Then I'm going to do an X-wise list.
[12:56] Go to the input one from the current position and save the X-prem and the X-UVW.
[13:01] Or write to them.
[13:03] Here we just initializing and here we are writing to them.
[13:06] And then we can do V at P.
[13:09] Z.
[13:10] Or let's do vector plus is equal to premium V.
[13:15] Now we want to read from the third input source to.
[13:19] And we want to read the position.
[13:22] And using the X-prem and X-UVW coordinates.
[13:28] And if we do V at P equals pause.
[13:33] We should have this.
[13:35] But as you can see, even if we have the normal.
[13:40] We have a flat geometry.
[13:44] So we need somehow to save this Y deformation that we have in here.
[13:50] For that I'm just going to do something really quick in here.
[13:54] So before we deform, we can create a wrangle.
[14:02] Let's create a wrangle in here and target the flat plane.
[14:08] And we want to save the vector displacement in here.
[14:11] So basically we will do V at this.
[14:15] It will be equal to V at P minus V at off input one bit.
[14:19] So the position from the second input.
[14:22] Since we have the same amount of geometry we can do this.
[14:25] And if we have a look, we should have a displacement.
[14:29] It's not very noticeable, but it's there because it's too small.
[14:33] So the values are really small.
[14:35] So we have the displacement.
[14:37] Now we need to displace these along the normal.
[14:41] Using the in this case the displacement dot Y.
[14:44] Since we are just interested in the Y component.
[14:48] So if we do now, if we read in first normal, so vector n.
[14:59] And we want n from the second input.
[15:02] And now we do plus plus and multiply by V at this dot Y.
[15:09] And we get our geometry.
[15:12] So as you can see, we have our deformation there.
[15:19] We have a look in here, not here, sorry, here.
[15:25] And what else can we do?
[15:27] Did I did something in here?
[15:29] Let me see.
[15:30] I want to start angle of minus 45.
[15:33] So I have some tape in here.
[15:35] Now we can do something really quick,
[15:38] which is change this to three point lighting and create a material preview.
[15:47] And let's do a metalna.
[15:49] So one.
[15:51] And if you want, you can in my final C9,
[15:53] reduce some ramps in here to create the texture.
[15:59] But I'm not gonna even do that because this is dragging to a long lesson.
[16:03] And we can also, I guess, we can also divide this.
[16:10] And yeah, guys, that's basically it.
[16:13] So this is probably the last tutorial of the year.
[16:16] I hope you really enjoyed.
[16:18] Really please let me know your feedback below.
[16:20] It's always important.
[16:21] I just want to take the chance to thank you all for your continuous support,
[16:26] especially in my patrons.
[16:28] And yeah, I hope we can accomplish some cool projects in the next year.
[16:33] See you.
[16:34] Thank you.



---

## Captured Frames

- [1:00] tutorials/frames/procedural-duct-tape-in-houdini/frame_000.jpg
- [2:10] tutorials/frames/procedural-duct-tape-in-houdini/frame_001.jpg
- [3:15] tutorials/frames/procedural-duct-tape-in-houdini/frame_002.jpg
- [4:45] tutorials/frames/procedural-duct-tape-in-houdini/frame_003.jpg
- [6:10] tutorials/frames/procedural-duct-tape-in-houdini/frame_004.jpg
- [8:00] tutorials/frames/procedural-duct-tape-in-houdini/frame_005.jpg
- [10:10] tutorials/frames/procedural-duct-tape-in-houdini/frame_006.jpg
- [12:00] tutorials/frames/procedural-duct-tape-in-houdini/frame_007.jpg
- [14:10] tutorials/frames/procedural-duct-tape-in-houdini/frame_008.jpg
- [15:40] tutorials/frames/procedural-duct-tape-in-houdini/frame_009.jpg

---

## Structured Notes

### Core Technique
Wrap a spiral of duct tape around a bent pipe using a UV-space detour (moving the tape's position into flattened UV space before adding wrinkle noise) plus an area-based scale-factor correction to keep displacement proportional regardless of the UV-flatten's size distortion, then use the **Wrinkle Deformer** as a non-simulated substitute for cloth-wrapping realism, and finally read the deformation back onto the original 3D geometry via `xyzdist()`/`primuv()` position sampling.

### Summary
The base pipe is modeled with a bent tube (Poly Hinge targeting primitive 0, moved/rotated via bounding-box-relative position and mirrored for the other end). The tape itself starts as a Spiral (explicit radius scale matched to the tube, ~4.5 turns, slightly overlapped) Match-Sized onto the left side of the pipe, then Swept into a ribbon (rolled -90°, width ~0.115) with computed UVs. Rather than leave the tape UVs stretched, a **UV Flatten** (preserve seams/island boundaries) straightens them, then the tape is **moved into UV space** (`P = {uv.x, 0, uv.y}` or similar) so wrinkle-style noise can be added on a flat, undistorted proxy rather than the curved 3D ribbon. Since flattening changes the tape's apparent scale, a **scale-factor correction** is computed by measuring total area before and after the UV-space move (`sqrt(area_target / area_source)`) and applying that as a uniform multiplier — ensuring the resulting wrinkle displacement is proportionally correct once mapped back to 3D. With the flat proxy prepared (subdivided ~3× for enough resolution), the actual wrinkle effect uses the **Wrinkle Deformer** (not a solver) fed a rest/null pair — one null is the "deform" target (offset with random noise, small element size) and the other is the pure "rest" input — the deformer is set to Cloth-preset behavior (increased constraint iterations, rest-scale, smooth iterations) to produce convincing wrinkle folds cheaply, without any actual cloth simulation. After tuning the deformer's look, the resulting flat, wrinkled displacement needs to be transferred back onto the original curved tape/pipe geometry: an **`xyzlist()`/`primuv()`**-based wrangle reads position from the deformed flat geometry using each 3D point's original UV coordinates (`primuv()` on the source geometry) to sample the corresponding deformed position — but since this only captures X/Z, the Y-axis wrinkle displacement must be captured separately as a saved displacement attribute (`current position − pre-deform position`) and re-applied along the original geometry's normal (scaled by the displacement's Y component) to recreate the 3D wrinkle bumps on the actual curved tape shape.

### Key Steps
1. Model the base pipe with a Tube, Poly Hinge (targeting primitive 0, sorted by Y), bounding-box-relative bend/offset, mirrored for the opposite end.
2. Build the tape as a Spiral (matched radius scale to the tube, ~4.5 turns, slight overlap for no visible gaps) Match-Sized onto one side of the pipe.
3. **Sweep** the spiral into a ribbon (rolled -90°, width ~0.115, computed UVs) to create the actual tape strip geometry.
4. **UV Flatten** (preserve seams + island boundaries) to straighten the tape's UVs, then **move the tape into UV space** (position derived from UV coordinates) as a flat proxy for wrinkle work.
5. Compute a **scale-factor correction**: measure total area before and after the UV-space move, take `sqrt(area_target / area_source)`, and apply as a uniform position multiplier so subsequent displacement stays proportionally correct.
6. Subdivide the flat proxy (~3×) for enough resolution, then set up two null inputs: a "rest" (undeformed) copy and a "deform" copy with an offset/noise-driven Mountain-style distortion for the wrinkle source.
7. Apply the **Wrinkle Deformer** (Cloth preset behavior: increased constraint iterations, rest scale, smooth iterations) between the rest and distorted nulls to generate realistic wrinkle folds without an actual cloth simulation.
8. Transfer the flat wrinkled result back onto the original curved 3D tape: use an `xyzlist()`/`primuv()`-based wrangle to sample position from the deformed flat geometry via each 3D point's original UV coordinates.
9. Separately capture the **Y-axis wrinkle displacement** (`current position − pre-deform position`) as its own attribute, then re-apply it along the original geometry's normal (scaled by the Y component) to reconstruct the 3D wrinkle bumps on the actual curved tape.
10. Finish with a quick three-point-lighting material preview (metalness ~1) for visualization.

### Houdini Nodes / VEX / Settings
Tube, Poly Hinge (procedural target primitive/position/direction), Spiral (explicit radius/turns), Match Size, Sweep (ribbon, roll, computed UVs), UV Flatten (preserve seams/island boundaries), UV-to-position wrangle, area Measure (×2, before/after) + `sqrt()` scale-factor wrangle, Subdivide, Mountain (distortion source), Wrinkle Deformer (Cloth preset, constraint iterations, rest scale, smooth iterations), `xyzlist()`/`primuv()` position-sampling wrangle, Y-displacement-capture wrangle + normal-scaled re-application, Object Merge (quick shelf-tool version), three-point lighting material preview.

### Difficulty
Advanced (the UV-space detour with area-based scale-factor correction, combined with the Wrinkle-Deformer-as-cloth-substitute and the xyzlist()/primuv() round-trip to restore 3D wrinkle detail, is a sophisticated multi-step production technique).

### Houdini Version
21.0.359 (visible in viewport title bar).

### Tags
wrinkle-deformer, uv-flatten, area-scale-factor, xyzdist, object-merge, tape, procedural-modeling

---

## Related Tutorials
- [Quick object merge with Python in Houdini](quick-object-merge-with-python-in-houdini.md) — the Python shelf-tool used here to quickly create the Object Merge node for the rest/deform reference geometry.
- [Vellum Balloon Text in Houdini](vellum-balloon-text-in-houdini.md) — shares the Wrinkle-Deformer-for-fake-cloth-wrinkles approach used here, applied there to inflated text.
- [Procedural Favela in Houdini | Tips and Tricks](procedural-favela-in-houdini-tips-and-tricks.md) — shares the corrected (rest/deform input order) Wrinkle Deformer workflow with a custom surface normal, applied there to a roof tarp and trash bag.
