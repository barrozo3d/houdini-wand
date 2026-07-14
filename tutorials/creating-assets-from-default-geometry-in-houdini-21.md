---
title: Creating assets from default geometry in Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=oEIXFY-Kxdk
author: cgside
ingested: 2026-07-13
houdini_version: "21"
tags: [modeling, rigging, vex, procedural, skeleton, deformation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/creating-assets-from-default-geometry-in-houdini-21/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Creating assets from default geometry in Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=oEIXFY-Kxdk)
**Author:** cgside
**Duration:** 9m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, just a quick video to show you how you can transform an input mesh, a default
[0:06] or any mesh, for example, and transform it into some sort of asset.
[0:10] In this case, I'm trying to make a glove that I saw online, something similar.
[0:15] You tell me if it was successful or not.
[0:17] I kind of like the result.
[0:19] So yeah, let's get into it.
[0:21] Let me just change this to default lighting and go what the top.
[0:24] As you can see, the network is not too complicated, but I will try to explain everything.
[0:29] So we start with the template body that has these clean ends that we can extract.
[0:34] And of course, I extract one of the ends.
[0:37] But as you can see, this will be, we'll have an uneven edge and I want to equalize it,
[0:42] let's say.
[0:43] So first of all, in order to move it to a rest space, I'm extracting the oriented bounding
[0:48] box and saving the transform attribute that I can use later.
[0:52] And I'm also saving the Unshared group where I want to equalize the edge.
[0:58] And in this wrangle, as you can see, I'm doing that equalizing all the points.
[1:02] Of course, I could have moved it to rest space by inverting the transform and applied to
[1:06] the position, but I wanted to make it harder just to learn something new.
[1:11] So basically what I'm doing in these bit of X, and I think is the only bit of X I'm using
[1:15] in this project, I'm first selecting one of the points of it.
[1:19] I'm, first of all, I'm only iterating over the Unshared point.
[1:21] So as you can see, I'm concerning to that group.
[1:24] And selecting the first point of that group, as you can see, in this X-Pand points group,
[1:29] I'm just selecting the first one.
[1:30] Then I'm also grabbing the position of that specific point because I want to snap all
[1:34] the other points to that position.
[1:36] But as you can see, this is not in a simple axis, this is like oriented in this position.
[1:43] So what we do, I first grab one of the axes of the transform attribute that I'm reading
[1:50] in here.
[1:51] So in this case, it will be this axis along the X in this case, because that's how the
[1:56] bound X-RUX transformed it.
[1:59] So I'm extracting that specific vector from the matrix.
[2:03] Then I do a dot product between the current position and that specific axis, that direction,
[2:09] that vector, to see how far along the point is along that direction.
[2:15] So as you can see, this is the direction.
[2:18] And I'm measuring basically the sign distance of if it's in front or behind that specific
[2:22] point.
[2:23] Let's say this is the point, this point will be behind, this point will be in front.
[2:26] So I'm doing that basically projecting one vector into another.
[2:29] This is useful for this kind of local space transforms.
[2:34] And then I'm also doing a dot product between that reference position and the direction.
[2:39] So I can extract the basically clamped values to that reference position.
[2:48] Then just displacing along that direction, let's say that's the normal, I can actually
[2:53] show you that direction if I assign it really there, it's equal to there.
[2:58] And I can show you how that looks.
[3:00] So basically this vector in here.
[3:02] And I'm just moving the points along that direction, basically by doing this subtraction
[3:09] in here.
[3:10] So if it's in front, it will move back of that reference point.
[3:13] And if it's in behind, it will move it to the front to that specific axis position.
[3:21] So maybe a bit too complicated.
[3:22] I could have just transformed it into a rest position like I'm doing in here.
[3:27] And then just move the points along, in this case along the axis.
[3:30] Anyways, so as you can see in here, I'm just placing a match size and restoring the
[3:34] X form, the transform.
[3:35] So I can move it to rest space.
[3:37] And then just doing a manual transform in here, rotating so I have it oriented in this
[3:41] position.
[3:43] So then what I want to do is to inflate this match to create the glove shape.
[3:47] But as you can see, we have very little space between the fingers.
[3:51] So I kind of want to move the fingers apart from each other.
[3:55] So far that I'm going to first to read this match, create a skeleton, I mean.
[4:01] And also I need the skeleton because I'm going to pose also the end.
[4:05] So that's another requirement.
[4:10] So for that, I'm just polyfilling it because right now it's open and the rest right is
[4:14] calent and 3D.
[4:16] So we get these sorts of skeleton.
[4:20] And I can show, I just freeze it because you can take like 10 seconds to cool.
[4:24] In this case, it took like five seconds or something.
[4:26] I use these settings.
[4:28] Then this outputs a bunch of attributes.
[4:29] I'm deleting it, deleting the groups also.
[4:33] I'm doing an idea for some reason, but I don't really, I think I don't really need it.
[4:38] Then doing a basic resample.
[4:39] In this case, it was like a sheep way to get the rig with the correct bones, as you can
[4:48] see, so with the correct points.
[4:50] So in the middle of the finger, in the back and in the front.
[4:54] So it's more or less correct.
[4:56] You know, I'm lazy.
[4:57] I'm trying to do everything procedural this way.
[5:00] I can waste all the time doing the procedural thing, but then be lazy to not do it manually
[5:06] for the most of the time.
[5:07] If that makes sense.
[5:08] Fuelling, polypating.
[5:10] And in this case, I'm selecting the NZ near, but I don't really need it.
[5:13] Neither I need these decent, so long geometry, but this is useful.
[5:17] If you have reversed primitives, you can create some sort of curvy that is correct in this
[5:22] case.
[5:23] Let me get rid of the obvious.
[5:24] Then I do a basic edit in here.
[5:27] So I'm just doing a basic, let me see.
[5:29] A basic editing here to basically align it a bit better with the input mesh.
[5:35] It's not really that important because then again, we will use the delta mesh to smooth
[5:39] out the rig and the deformation.
[5:41] So I've seen that this doesn't make much difference, but I did it.
[5:46] So it's there.
[5:48] I'm doing a reverse in here because I want to create that transform attributes, but again,
[5:53] this is another thing that I didn't end up using that much, but it's just a basic
[5:57] transform attribute from the normals and an napa tree boots.
[6:01] So I end up with this kind of transform attribute.
[6:04] As you can see, the x axis is fixed.
[6:06] Then we have the z axis along the normal, the tangent and pointing that.
[6:10] Please, it's just easier because I will manually pose this and this way we have some reference
[6:15] to it.
[6:17] So and please, we can ignore this is my basic rig.
[6:21] Then I place a rig doctor and here it comes the capturing.
[6:26] So before showing you the capturing, I just did a rig pose and moved the end like this.
[6:31] So I can later pick the geometry along the normal.
[6:35] This way I don't get intersections.
[6:37] So I'm just setting these rest pose.
[6:40] And for the capturing, I'm doing four ends.
[6:43] I learned this trick a while ago.
[6:45] You can do a bone capture lines.
[6:47] This will subdivide your point, your curves.
[6:51] Then do a pet conform.
[6:53] And by the way, in here I'm just doing a remesh to the end and doing a pet conform between
[6:59] the mesh and the bone capture lines and then to capture by harmonic.
[7:03] In this case, capturing by distance didn't give me a great result.
[7:08] It was more or less okay, but again, the fingers are way too close and that can cause an issue.
[7:12] And then using that pose rig, so the one with the fingers apart, I'm doing a bone deform
[7:19] and a delta mesh.
[7:20] Then we get an okay result for this static mesh.
[7:23] Of course, if this is going to be animated, it can be more problematic.
[7:27] And that's our pose.
[7:28] Then I'm doing a basic pick in here, as you can see.
[7:32] So we get the glove shape and doing an attribute blur on the points.
[7:37] And then we have another rig pose.
[7:38] In this case, where I'm setting the final pose, as you can see, just moving the bones around
[7:43] and we get this sort of pose.
[7:46] So we do, so where was I?
[7:50] So we do the blur on this position.
[7:53] Then we do a bond the form with that new pose and do a delta mesh.
[7:56] And we get an okay result for this.
[7:58] It can be pretty forgiving for this kind of asset.
[8:01] And then I do another yet another bond the form, but for the original position.
[8:06] So this one in here, where the fingers are more close together and we get this sort of
[8:14] result.
[8:15] A delta mesh and this will be our rest state and this will be the original position.
[8:21] And then we do a basic wrinkle the former and we get this sort of result because we are
[8:26] deforming from this original position to this position.
[8:30] And in here, I'm also doing a pick with a mask along the Z axis, as you can see, just
[8:36] an attribute that just float with bounding box set to Z.
[8:39] And then we can also get some wrinkles and it mimics closer to my reference and we get
[8:44] this sort of result.
[8:45] Then we just subdivide and yeah, guys, that's basically it.
[8:49] And we go from, let me just change in here, 3 point lighting and maybe ambient occlusion.
[8:57] And we go from these to the sort of asset and we still have UVs, as you can see.
[9:01] So you could probably you'll be flattened them to relax the UVs.
[9:05] But anyways, this was just a quick setup that I wanted to share.
[9:09] There are some bits and pieces that are interesting.
[9:12] At least I found them interesting, that's why I'm sharing.
[9:15] And as always, you can grab the full scene on my Patreon alongside with the exclusive tutorials,
[9:20] hours and hours and all the project files from my videos.
[9:23] So if you found this interesting, please leave a comment below.
[9:26] I would love to hear your opinions and how you would do it in a different way.
[9:31] I always like to learn from your suggestions.
[9:34] So thank you for watching and I guess I'll see you next time.
[9:37] Bye.



---

## Captured Frames

- [0:15] tutorials/frames/creating-assets-from-default-geometry-in-houdini-21/frame_000.jpg
- [3:00] tutorials/frames/creating-assets-from-default-geometry-in-houdini-21/frame_001.jpg
- [6:25] tutorials/frames/creating-assets-from-default-geometry-in-houdini-21/frame_002.jpg
- [7:40] tutorials/frames/creating-assets-from-default-geometry-in-houdini-21/frame_003.jpg
- [8:55] tutorials/frames/creating-assets-from-default-geometry-in-houdini-21/frame_004.jpg

---

## Structured Notes

### Core Technique
Turning an open-ended cylindrical mesh (a "template" tube) into a posed, sculpted asset (here, a glove) by building a temporary skeleton with **bone capture**, posing it twice (fingers-apart capture pose vs. final closed pose), and blending the resulting **delta mesh** deformations together with VEX-driven masks.

### Summary
Starts from a plain open-ended tube, equalizes its ragged end edge with a hand-written VEX wrangle that projects points onto a local axis (via oriented-bounding-box transform + dot product), then polyfills and unrolls a skeleton from the mesh using **Skeleton from Mesh**-style resampling. The skeleton is posed apart (to avoid finger-intersection during capture), captured onto the mesh via **bone capture lines + pet conform + capture by harmonic**, then deformed back through a "real" closed pose using **Bone Deform + Delta Mesh** so the fingers separate cleanly without self-intersecting. Two more delta-mesh passes (per-Z-axis point-position blur/mask) recombine rest/posed states to add wrinkle-like surface detail near the joints, and the piece finishes with a subdivide + 3-point lighting/AO render.

### Key Steps
1. Start from the template tube body; extract one open end (ragged/uneven boundary).
2. Compute the OBB (oriented bounding box) of the unshared boundary group and save its transform attribute (matrix) for later use as a local rest-space frame.
3. In a VEX wrangle (Attribute Wrangle) over just the unshared-edge point group: grab one axis of the saved OBB transform matrix, dot-product each point's position against that axis to get a signed distance (in front of / behind the reference point), then subtract along that axis to equalize/flatten the ragged edge — an alternative to simply transforming into rest space, inverting, and moving points on a plain axis.
4. Polyfill the now-flat end to close the tube, then build a skeleton: resample the capped mesh, delete extra attributes/groups, and derive a bone chain running along the tube with points centered per "finger".
5. Manually pose the skeleton with a **Rig Pose** node, spreading the "fingers" apart (to leave capture room and avoid intersections) — this is the "capture pose".
6. Capture geometry to the skeleton using **Bone Capture Lines** (subdivides curves) → **Pet Conform** (conforms lines to the remeshed mesh) → **Capture by Harmonic** (chosen over Capture by Distance, which gave a worse result given the tight finger spacing).
7. Deform with **Bone Deform** using the capture pose, then generate a **Delta Mesh** to get a clean static result for that pose.
8. Add a second **Rig Pose** for the true final pose (fingers closer together, more natural), run another Bone Deform + Delta Mesh from the capture-pose result.
9. Run a third Bone Deform + Delta Mesh back to the original rest position/pose, then blend rest ↔ posed states via a wrinkle-style deformer using a **point attribute mask along the Z axis** (bounding-box-relative float attribute) to localize surface wrinkling near joints.
10. Subdivide the final mesh and light with 3-point lighting + ambient occlusion for the final render; note UVs exist but are not relaxed/flattened in this pass.

### Houdini Nodes / VEX / Settings
Nodes used: Object Merge, Bound (oriented bounding box), Attribute Wrangle (custom VEX — the only VEX in the whole build), Polyfill, resample/skeleton-generation chain, Rig Pose (x2, capture pose + final pose), Bone Capture Lines, Pet Conform, Capture Attributes (Capture by Harmonic, not Capture by Distance), Bone Deform (x3 — capture pose, final pose, rest pose), Delta Mesh (x3, one per Bone Deform), attribute blur (on points, for wrinkle blending), a bounding-box-relative Z-axis mask attribute for localized wrinkle deformation, Subdivide. VEX snippet: extracts one axis vector from a 4x4 transform matrix, computes `dot(position, axis)` for a signed local-space distance, and displaces points along that axis to equalize the boundary edge.

### Difficulty
Intermediate — no complex VEX beyond a single wrangle, but requires solid understanding of bone capture/deform workflows, delta mesh blending, and local-space transform math (matrix axis extraction + dot products).

### Houdini Version
21 (per video title; UI matches Houdini 21's dark theme).

### Tags
#modeling #rigging #vex #procedural #skeleton #deformation #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers bone-capture/delta-mesh asset creation from primitive geometry — cross-link with any future rigging, skeleton, or delta-mesh-deformation tutorials once extracted from this batch.
