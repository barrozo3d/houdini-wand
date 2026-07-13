---
title: Mechanical rigging in Houdini - Attaching custom controls
source: YouTube
url: https://www.youtube.com/watch?v=7J-hDF0H6ck
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H18+)"
tags: [rigging, kinefx, mechanical, controls, wrangle, matrix, fit-range, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Mechanical rigging in Houdini - Attaching custom controls

**Source:** [YouTube](https://www.youtube.com/watch?v=7J-hDF0H6ck)
**Author:** cgside
**Duration:** 13m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So, we will do the remaining of the packing in a bit.
[0:05] For now let's attach some controls to this.
[0:11] So for that I'm going to create in your a net node and create two points.
[0:18] Or we can do a point generate.
[0:21] And generate two points just to be different.
[0:23] They will be at the origin.
[0:26] I can see them.
[0:27] Why I can see my grid?
[0:29] Press age.
[0:31] Let's do a name.
[0:34] And let's name point zero as star get left and point point as star get right.
[0:49] And make sure we set it to points of course.
[0:52] Now we will need a read doctor.
[0:57] This will also be transformed.
[1:01] I think shell has transforms.
[1:03] And now let's just create a sphere.
[1:05] Set it to primitive.
[1:08] And I'm going to change the size to be 0.05.
[1:15] Give it a color.
[1:18] Can be this kind of pool.
[1:22] You can pick any shape.
[1:23] Let's just name it.
[1:26] And this one is need to be on primitive.
[1:29] Let's need to control.
[1:31] Now let's do an attach control.
[1:34] Not attach control is attach.
[1:36] Join geo.
[1:38] Join geo.
[1:40] And let's make sure we don't want to rest both.
[1:46] So let's connect these and this.
[1:49] And let's attach the name target left to control.
[1:57] Let's just do up.
[2:00] And we have two points.
[2:02] If we want different control for each one, you can pick or a different shape.
[2:06] And now let's just do a read doctor.
[2:10] No, read post.
[2:13] And we can enter this and pick target right.
[2:19] Move it to the right target left.
[2:20] Move it to the left.
[2:22] Let's do 1 and 0.5 on y.
[2:29] 0.5 on y and minus 1.
[2:32] Now let's lock this because we don't want to rotate them.
[2:39] And we also want to lock the y and the z.
[2:48] So these are our controls.
[2:52] Now let's attach them to make them interact with our skeleton.
[3:02] So basically we want this controls to rotate the root points.
[3:06] So 1 for each.
[3:07] So that's what we have in here.
[3:09] And instead for now we are doing these read posts.
[3:13] But we want to do this in a different way.
[3:15] So re-gather with triangle.
[3:18] And this one it will be a bit of controls.
[3:27] Let's give it some color and connect this to here.
[3:32] Now we just want to fit these controls to the max angle that we calculated in here.
[3:40] So that's basically what we want to do.
[3:42] But we want to do these for two points.
[3:45] So instead of iterating over points, we can actually iterate maybe over numbers.
[3:53] So just a different way.
[3:54] And we will do end points and input one.
[3:58] So we will iterate twice.
[4:00] So and what have I done in here?
[4:08] I just used these numbers and points input one.
[4:13] So we should have two points.
[4:16] Now let's just use this field to select some points.
[4:19] So it's point six and we can do something like this.
[4:26] And now we can do int on array of the points that we selected.
[4:31] So expand points group input zero.
[4:35] And the group is just the channel string group.
[4:40] Because this one in here is named group.
[4:43] So if we print this.
[4:49] So it's a point we should have six and sixteen.
[4:52] Yeah, that's correct.
[4:55] And now we will do, we will grab the local transform of these points because we want to
[5:03] extract the exposition and then fit it to the rotation might single.
[5:08] And we will fit it between some bounds that already worked for me.
[5:12] So it's a matrix for an x form.
[5:17] And we want we want to grab from the point input one to local transform.
[5:25] And the point number it will be just LM.
[5:27] No, so zero or one in this case because we have two iterations.
[5:32] Now to get the translate text of both we will do get comp and get the from these matrix.
[5:41] We will get this row and this column.
[5:47] And then we will grab the local x form of our points that we selected.
[5:51] So six and sixteen the mirror one.
[5:54] And it will be just so let's name it local x form.
[5:59] And we can copy from here.
[6:02] But in this case input zero and we want to grab this specific point.
[6:06] So either six or four sixteen because we are arriving from this array that we previously
[6:12] selected.
[6:13] Now make single it will be just detail.
[6:21] And we will grab the angle.
[6:24] And we will multiply it by two because we will mirror it.
[6:27] We will basically we bit to the other side.
[6:31] So that's the maximum.
[6:33] And now it's simple.
[6:34] We just set up an angle which will be a fit function between that we will absolute
[6:41] translation X because we might have negative we in one of the so on the left side we
[6:46] will have negative so we will just fit the positive number between I found the value 0.6
[6:53] and 1.2 on the translation will work well and from zero to the max angle.
[7:02] So this should work and now we can just re rotate the local x form and ingredients we will
[7:14] set the angle and radians we set the angle and then we do it of course on the z axis.
[7:23] All this will do nothing so it will not rotate but what we need to do is set point transform
[7:35] to point that we got I mean because we are working in numbers which is basically detail
[7:43] with the parallel processing.
[7:45] So we will set the local transform and we will just select from the points the current
[7:53] point we want to set so L Lm now.
[7:59] So this is the points and the value we want to set is a local x form that has been pre-rotated
[8:04] in the previous line.
[8:05] So if this works yes now we can select this and within a range we can rotate to the
[8:12] max angle.
[8:14] Now if we look at our re you can see it aligns perfectly and we can come in here and open
[8:21] and close everything.
[8:24] Oops.
[8:25] Okay it might go to the other side so we have to keep the control on this side.
[8:37] But this one in here is not working because we is not working because we haven't bind
[8:41] it to geometry of course.
[8:45] So we have to use this control in here and now we can get rid of this repose and I think
[8:54] the only thing left to do is to capture the remaining two.
[8:58] So let's do that.
[8:59] Just to run and back because this is back geometry let's use name but with color it will
[9:10] make everything better.
[9:15] So let's just now copy do the same for the other side.
[9:21] This should work the same way.
[9:29] So we just need to follow the logic so if you remember so let's add one and the first
[9:34] one we selected was this link and it was 0.0 so now it should be the mirror 0.0.
[9:46] Then we add the second one and this should be 0.6.
[10:01] Let's keep pointing on this and this should be 0.2.
[10:12] And then what else did we do?
[10:14] So we selected this part and we did 0.1.
[10:26] And after 0.1 we have the tree so this one and sorry this one and after that so after
[10:40] 0.3 we have 0.4 which I think is this one.
[10:45] Yep.
[10:47] And finally this one here which is 0.8.
[10:57] Now let's see all it looks.
[11:06] So it seems to be working.
[11:09] Let's just go to the controls.
[11:14] Let's close it and yeah everything should be working guys.
[11:20] Now this also means that we can place a reading here because we have that possibility of
[11:31] for example so let's let's do the following.
[11:36] Let's close this.
[11:39] Let's maybe move them apart a bit and let's come in here.
[11:48] We can also do the following.
[11:50] Select this point and open the flap.
[11:53] And also select this and so this point is kind of not working.
[12:03] Let me see.
[12:05] Oh I'm selecting this one should be this one as you can see it's working.
[12:12] So as you can see we can also control other things and now the idea is you have this base
[12:20] and you can make it better and make it perfect rig with all the controls.
[12:26] In this case we only add two controls but you can add as much as you like.
[12:33] So yeah guys that's basically it for our first lesson on this procedural mechanical rigging
[12:38] course.
[12:39] I hope you have enjoyed sorry for any delays but I had something working and then when
[12:46] I tried to replicate it it didn't work so well so in the end it worked out fine so I
[12:53] hope you have learned something new from this.
[12:55] As always feedback is welcome and you can always contact me and ask me any questions.
[13:00] Don't forget to download the file from this link I will leave a link below and yeah thank
[13:06] you for watching and I'll see you next time.



---

## Captured Frames

- [1:08] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_000.jpg
- [1:49] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_001.jpg
- [2:22] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_002.jpg
- [4:26] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_003.jpg
- [7:14] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_004.jpg
- [8:12] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_005.jpg
- [11:06] tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/frame_006.jpg

---

## Structured Notes

### Core Technique
Attaches sphere-shaped animation controls to a mechanical rig and drives symmetric pairs of joint rotations by extracting each control's translation distance, fitting it to a precomputed max-rotation-angle range, and writing the resulting rotated matrix back onto the rig points — all done in parallel over a "number of points" wrangle rather than looping per-point manually.

### Key Steps
1. Build simple sphere controls: create two points (via a **Point Generate**, name them e.g. `target_left` / `target_right` via a **Name** node set to Points mode), run them through **Rig Doctor** for transforms, then instance a small **Sphere** (Primitive type, scale ~0.05, given a distinct color) per point, named and set to Primitive mode.
2. **Attach Control / Attach Joint Geo**: join the control geometry to the rig geometry (disable resting both inputs), wiring the named target attribute so each sphere attaches to its corresponding named point.
3. Use **Rig Pose** to position each control sphere relative to its target (e.g. offsets like 1 / 0.5 on Y and -1 on the mirrored side), then **lock rotation and lock Y/Z translation** on the controls so animators can only translate them along the intended single axis.
4. **Driving the rig from the controls (the core trick):** rather than iterating per-point with a for-each loop, use a **Rig Attribute Wrangle** iterating over **numbers** (`npoints(1)`) instead of points, so both symmetric points are processed together in one parallel pass.
5. Select the relevant rig points into an array (e.g. `expandpointgroup` with a **channel string group**, resolving to specific point numbers like 6 and 16 for a mirrored pair), then pull each point's **local transform matrix** (from the second input) and use **getcomp** to extract the translate components (row/column of the matrix) needed for the fit.
6. Compute the **max rotation angle** once, in detail mode: grab the local transform of the same selected points from the *first* input (the un-driven rest rig), extract the angle via `matrix → makesingle` style decomposition, and multiply by two (to account for mirroring the rotation to the opposite side).
7. Per point: **Fit** the absolute value of the control's translate-X (since one side is negative) between an empirically-found distance range (e.g. 0.6 to 1.2) onto an output range of 0 to the max angle computed in step 6 — this converts "how far did you drag the control" into "how much should the joint rotate."
8. **Pre-rotate** the point's local transform by that fitted angle (in radians) around the relevant axis (Z in this example), then explicitly **set the point transform** back onto the correct point using the current-point index from the numbers iteration (`@ptnum`/`i@elemnum`-equivalent local variable) — necessary because working in "numbers" mode (parallel over an array) doesn't automatically write per-point like a native points-context wrangle would.
9. Verify: opening/closing the control causes the rig to rotate symmetrically and align correctly at the driven positions; note that a control can end up needing to be constrained to only one side (dragging too far the wrong way can flip it to the opposite equivalent solution).
10. **Repeat symmetrically for the remaining rig points**: capture remaining joints one at a time (using Name+color for clarity), following the same point-selection/mirrored-fit logic established above but with different empirically-tuned values per joint pair (the video walks through several joints such as 0.0/mirror-0.0, 0.6, 0.2, 0.1, 0.3/0.4, 0.8 as example distance-fit tuning values).
11. Once all points are captured and driven, the base rig is functional with just two controls demonstrated — the presenter notes this pattern scales to as many controls as needed for a full production rig.

### Houdini Nodes / VEX / Settings
Point Generate → Name (Points mode, target_left/target_right) → Rig Doctor (init transforms) → Sphere (Primitive, small scale, colored) → **Attach Control/Attach Joint Geo** (join geo, no resting) → **Rig Pose** (position offsets, lock Rotate + lock Translate Y/Z) → **Rig Attribute Wrangle** in "numbers" mode (`npoints(1)` iteration instead of per-point) → `expandpointgroup` (channel string group → point array) → local transform matrix extraction (`getcomp`) → detail-mode max-angle calc (matrix decomposition ×2 for mirroring) → **Fit** (abs(translateX) between empirical distance bounds → 0..max_angle) → matrix pre-rotate (radians, chosen axis) → explicit **set point transform** by current-array-index point number → **Capture Period Geometry** for the remaining joints.

### Difficulty
Intermediate — requires comfort with VEX matrix functions (`getcomp`, transform extraction, `prerotate`/similar), the "iterate over numbers instead of points" wrangle pattern, and general rig-control setup; conceptually more advanced than typical point-wrangle work due to the parallel-array indexing trick.

### Houdini Version
Not stated explicitly; uses standard KineFX/rigging nodes (Rig Doctor, Rig Pose, Rig Attribute Wrangle, Capture Period Geometry) available in any modern Houdini (H18+).

### Tags
#rigging #kinefx #mechanical #controls #wrangle #matrix #fit-range #intermediate

---

## Related Tutorials
Cross-link with [Tuna Can | procedural modeling and rig with KineFX](tuna-can-procedural-modeling-and-rig-with-kinefx.md) — shares #kinefx #rigging; that tutorial's point-transform-copy-with-offset trick for making one piece follow another's animation is a related matrix-manipulation pattern to this video's fit-driven rotation setup.
