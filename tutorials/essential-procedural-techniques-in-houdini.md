---
title: Essential Procedural Techniques in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=JMfMxHi48Zs
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, uv, opencl, mpm, simulation, materials, shaders, karma, procedural, tips, advanced]
extraction_status: complete
frames_dir: tutorials/frames/essential-procedural-techniques-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Essential Procedural Techniques in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=JMfMxHi48Zs)
**Author:** cgside
**Duration:** 11m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back, so in this video I'll be sharing a few interesting tips
[0:04] on procedural setups.
[0:06] So let's start with this sort of peeling effect.
[0:10] So this is pretty simple.
[0:12] We start with a quadsphere.
[0:14] I kind of transformed it and used the amount to deform it to like a potato shape.
[0:19] This is similar to a video I saw of the same effect in Blender.
[0:24] Then I'm subdividing just to have an geometry for the next step and in here I just place
[0:28] a spiral and align it with a centroid to have something like this and I reproject it
[0:32] to the potato.
[0:34] Then I make sure since we have normals in here that are coming from the potato, I'm
[0:39] just swapping it to one petribut so I can sweep it with those same normals.
[0:44] Otherwise if we don't have that petribut it will be a mess as you can see.
[0:49] Then we come back to this branch where we have the subdivided, we do a distance from
[0:52] geometry, from those curves and we have a mess that looks something like this.
[0:56] Then we clip it but this won't give us the correct result as you can see.
[1:01] But we will use this to align our UVs next.
[1:03] So we clip it based on the mask attributes and then we promote that clip touches group
[1:08] that I saved in here to a vertex group.
[1:11] And finally we do a Boolean and this Boolean is actually what will create the peel.
[1:17] Then we do a UV flatten and the UVs will look something like this because we are using
[1:21] that vertex group in here that we saved to flatten the UVs along the X.
[1:27] So along the UVs if I don't do that we get something like this which won't work for
[1:32] our next effect which is basically, first of all I'm going to split the UVs and then
[1:36] promote it to a point attribute so I can work in a point wrangle with UVs.
[1:40] And in here I'm taking the new component of the UVs.
[1:44] So this component around the X axis.
[1:48] And I'm just creating an animated mask.
[1:51] So we have a ramp based on the curve view plus some offset so we can offset it up and
[1:57] down and then just assigning that to an attribute.
[1:59] So I can show you how it looks.
[2:01] So it basically it will grow.
[2:03] It's a mask that will grow.
[2:06] And I'm just animating the offset.
[2:08] So if I let me copy this because I'm doing a bad job at explaining it.
[2:12] Basically let's say we start from minus one and we can animate it to a fully one as you
[2:16] can see along the UVs X component.
[2:20] So that's what I'm doing in here.
[2:21] I'm fitting time between zero and one second and start at minus one and go to one between
[2:27] those those frames and we get this effect.
[2:30] And then it's simple we can just affect the position dot Y.
[2:33] We subtract that mask and we play with the amplitude.
[2:36] So we get this effect.
[2:38] So yeah that was the first tip.
[2:42] So in this one I was trying to replicate those typical videos of liquids with a bottle
[2:46] spinning and creating this sort of splash effects.
[2:49] And I did that with mpm and I wanted to show you how you can use open CL which is the
[2:55] recommended methods to apply forces into the dive targets of mpm.
[3:00] So let's actually have a look at that.
[3:03] So in here as you can see I simulated the I simulated the liquid in a rest space as you
[3:10] can see.
[3:11] It's not with the bottle spinning all around but I applied the transform that I have from
[3:17] my animation because I did my animation with a transform as you can see in here with
[3:21] a transform attribute.
[3:22] So you can see in here let me show you.
[3:24] So it's basically an animated noise and playing with the rotation creating a transform
[3:28] attribute and then applying the transform attribute.
[3:30] You can have a look at the file on Patreon.
[3:32] I'm going to share all the scenes from this video.
[3:34] So yeah.
[3:35] So I'm I'm transferring the transform along the the shine of nodes.
[3:40] So for example in here I'm just copying to the detail attribute and inside the mpm
[3:45] solver.
[3:46] So as you can see this is the final result of the mpm solver and let me dive inside and
[3:52] actually pin this viewport.
[3:54] What I'm doing in here is first of all we need to bring that animated attribute to because
[3:59] it's an animated x form to to dops.
[4:02] So for that I'm just reading the matrix from the first input first contact geometry and
[4:07] saving that as an attribute.
[4:09] So otherwise it will just read the first frame like normal dops.
[4:13] So we need actually to bring it because you can do it in OpenCL.
[4:16] And since Odini always says that we should use OpenCL to in the dive target instead of
[4:23] X I try to replicate the same effect I add on Vex but using OpenCL and it's actually
[4:28] pretty simple.
[4:29] So the idea is to that I add in Vex before is just to apply gravity using the X form and
[4:37] you can do that pretty simple in OpenCL.
[4:40] You bind the first the force attributes because you can create attributes with OpenCL.
[4:45] Then you also bind the detail attribute for the X form.
[4:47] You create a parameter for the gravity that you control in here.
[4:51] And then in the kernel you just save a variable Open matrix for for the X form and you do
[4:56] a met for three back three malt which is multiplying the gravity but ignoring the just
[5:01] reading it as a three by three matrix.
[5:03] So ignores it ignores translation.
[5:06] And then we just set the force to do this variable and that will apply our transformatribute
[5:12] in rest space that we can later.
[5:14] So let me see is not in here later I am applying the X form.
[5:20] So it's in here.
[5:21] In here I'm just applying the X form from the back geometry and we get the sort of result
[5:27] that you saw in the final render.
[5:29] So yeah hopefully that will be useful on how to use actually OpenCL to apply your effects
[5:34] and this is a very simple effect but you can see how useful this can be.
[5:43] So still on the same scene after I have my geometry meshed you can see the meshing.
[5:49] This will be problematic when we interact with the bottle which will be less or plastic
[5:53] or something like that.
[5:54] As you can see we have all sorts of bumps in the mesh around where it meets the bottle.
[6:01] So what we can do is to snap it to the bottle G.O.
[6:04] So as you can see I have the interior of the bottle in here because since I model these
[6:09] all procedurally in in Odini I have access to the groups and whatnot.
[6:14] So where was I?
[6:17] We can actually bring that extrude back and just snap it to the surface.
[6:22] So if I show you before, before and after you can see how clean that is and finally we
[6:28] can do some little peak just to intersect with the bottle so which when there's nice.
[6:33] This snapping is pretty simple.
[6:35] We have the bottle G.O.
[6:37] You can actually use the full bottle I just thought it would be easier just to use the interior.
[6:41] But basically let me show you the blend mask which is something like this.
[6:46] We basically do a next-wise distance to the bottle and then we fit that distance between
[6:52] 0 and an offset value that I can set in here as you can see and all those points that
[7:00] are on the on the red part of this mask or that are part of the mask.
[7:05] We will blend between projected geometry, so mean both I can actually show you how that
[7:09] looks so we have to pass which will be just the points all projected to the bottle and
[7:16] we just blend with this mask so we don't project everything of course.
[7:20] So we basically do well-learned between the current position and the projected position
[7:24] which snaps to the surface and we use as blend the xyz distance this mask.
[7:28] So hopefully that was useful, that's basically how you can clean your mesh for rendering.
[7:33] Then do a little pick, some attribute blur and finally apply the transfer.
[7:38] So now I wanted to show you how you can do a planar projection in karma which is not that
[7:44] easy by default.
[7:45] So basically what I mean is being able to scale and move the projection around and don't
[7:50] project on the back.
[7:51] So the workflow is to start with a material exposition or if you have an animated object
[7:56] you can do a prime bar reader and read in the rest attribute so it's the same.
[8:01] Start with the position then we swivel the position where we need it to create the UVs.
[8:05] So we create UVs from the swivel position which in this case I wanted along the set so
[8:08] I'm going to grab the x and y position, combine it to a vector tool and use it as UVs in
[8:14] a material exp image.
[8:16] But I'm also placing a well a place to the node in between which I can use to scale,
[8:21] to offset on the x on the y and also place to pivot and we can also rotate as you can
[8:26] see.
[8:27] And it's important in the image that you set these to constants and constants on the
[8:29] address modes.
[8:31] So if we just connect these we will have a projection on both sides.
[8:36] So after taking the alpha and multiplying it by the mask along the z we have a correct
[8:40] alpha and finally we can just mix it.
[8:42] So for example I'm going to set the background color in here.
[8:44] So for example the yellow and just mix it with the logo.
[8:49] And now you have the sort of planar projection that you can rotate scale offset and play
[8:55] with it.
[8:56] So yeah.
[8:57] So let's say you start with the grids or any other mesh and you scatter some points and
[9:02] you want to find the near points to that specific amount which is just three points.
[9:06] If you do a near points you will find more than one point per initial point.
[9:12] So a simple way to solve this and an effective way also to solve this.
[9:17] To find exactly the amount of points you have on the second input so I can increase.
[9:21] For example to 9 and I'm from to 8 and I'm actually only selecting 8 points in total.
[9:26] So as you can see this works pretty well.
[9:28] So basically you do a wrangle and you find all the points you can do with a pacifying.
[9:32] I'm just doing with pacifying you can do with near points.
[9:35] Basically you want the array version of the near point which is near point.
[9:39] In this case I'm doing a pacifying finding the position of the input one which is the
[9:43] remeshed because you we want to find the values.
[9:47] We want to find all the values on the input mesh not these points because these points
[9:53] will be just one to zero one to want to find the point numbers on the mesh on the input
[9:58] one.
[9:59] So we do that pacifying and then we just set it as the tele-tributes.
[10:02] So if I actually look at that you can see that we have an array with all the points on
[10:06] the mesh not in here.
[10:08] So if we do it on these points we will have just the zero one to and after that we can
[10:13] just find in array.
[10:15] So basically we read that the tele-tributes on the second input and is an array and then
[10:20] we just use the find function to find in that array the current point number.
[10:25] If it finds that number so it's bigger or equals to zero otherwise it would be a negative
[10:30] number if it didn't find and we just group it and then in here we can actually place this
[10:33] an output group so we can visualize it.
[10:36] So that's basically it and you get the always the same amount of points you have you want
[10:42] to find.
[10:43] So not you don't have to tweak and play with the scale and what not to really find one
[10:50] point of so if I said it's to one I really find one point and not an island of points
[10:55] with like the default behavior of near points.
[10:58] And as always guys you can find the project files of this video on my Patreon alongside
[11:02] all the project files from my other videos as well as courses exclusive tutorials and many
[11:08] many tools.
[11:09] As always thank you for watching I hope you found this useful and I hope to see you next
[11:14] time.



---

## Captured Frames

- [0:15] tutorials/frames/essential-procedural-techniques-in-houdini/frame_000.jpg
- [1:20] tutorials/frames/essential-procedural-techniques-in-houdini/frame_001.jpg
- [2:00] tutorials/frames/essential-procedural-techniques-in-houdini/frame_002.jpg
- [3:05] tutorials/frames/essential-procedural-techniques-in-houdini/frame_003.jpg
- [6:20] tutorials/frames/essential-procedural-techniques-in-houdini/frame_004.jpg
- [7:45] tutorials/frames/essential-procedural-techniques-in-houdini/frame_005.jpg
- [9:20] tutorials/frames/essential-procedural-techniques-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
Five unrelated but reusable procedural tricks: an animated "peeling" reveal effect built from a spiral-swept Boolean cut plus UV-driven animated mask displacement, applying forces to an MPM sim's dive target via **OpenCL** (Houdini's recommended method over VEX for this), snapping simulation-meshed geometry back onto clean source geometry via a distance-based blend mask, a controllable **planar projection** setup for Karma/MaterialX that avoids projecting onto the back side, and a VEX trick to get an **exact** number of nearest points (unlike Near Points' inconsistent island-based results).

### Summary
**Peeling effect:** starting from a deformed QuadSphere ("potato" shape), a spiral curve is aligned to the centroid and reprojected onto the potato surface; the potato's own normals are copied to a `pscale`/orient-style attribute so the spiral can be Swept using those normals (without this, the sweep result is a broken mess). The subdivided potato gets a Distance-from-Geometry mask relative to the spiral curve, which is Clipped and promoted from a point group to a vertex group (needed to correctly align UVs later) — a **Boolean** using that clipped geometry is what actually cuts the peel strip free. A **UV Flatten** along that vertex group produces clean, aligned UVs; a Point Wrangle then reads the UV.x component, builds an **animated ramp-based mask driven by curve-U plus a time-based offset** (fit `time` between 0-1 seconds, offset from -1 to 1), and finally displaces `P.y` by that mask times an amplitude — producing a growing/peeling reveal animation.

**MPM force via OpenCL:** for a spinning-bottle liquid-splash effect, the sim is run in the bottle's *rest space* (not literally spinning), with the actual animated spin stored as a **transform attribute** (from an animated-noise-driven rotation) copied to a detail attribute and carried into the DOP network — critical because DOPs otherwise only reads the first frame of an attribute, not the animated value per substep. Since Houdini recommends OpenCL (not VEX) for applying forces to an MPM sim's dive target, the author reimplements a simple gravity-via-transform-attribute VEX snippet in OpenCL: bind the `force` attribute (OpenCL can create attributes), bind the detail transform-matrix attribute, expose a gravity parameter, and in the kernel multiply gravity by the matrix using **`matrix3` conversion (ignoring translation)** before assigning to `force` — after simulating in rest space, the saved transform attribute is reapplied to the final meshed geometry to get the correctly "spinning" result seen in the render.

**Snap sim mesh to clean source geometry:** simulation-meshed geometry touching a rigid object (e.g., a bottle) typically has ugly bumps at the contact area; since the bottle was modeled procedurally with known groups, its interior geometry can be reused as a clean projection target. A point-wise **distance-to-bottle mask** is Fit-ranged between 0 and a tunable offset value, and a lerp/blend between the current (bumpy) position and the bottle-projected position — driven by that distance mask — snaps only the near-contact points cleanly to the bottle surface while leaving distant points untouched; finished with a small Peak to force slight intersection, an Attribute Blur, and reapplying the earlier transform.

**Controllable planar projection (Karma/MaterialX):** instead of a naive position→UV mapping (which projects identically on both front and back), swizzle the rest/current position, combine X and Y into a Vector2 to drive an Image node's UVs, and insert a **Place2D**-style node in between to expose scale, offset (X/Y), pivot, and rotation controls; critically set the Image node's wrap/address modes to **Constant** (not the default tiling/mirror) to avoid back-side bleed. Multiply the image's alpha by a Z-axis-facing mask to get a correct alpha, then Mix the projected logo over a flat background color using that alpha — yielding a fully adjustable (scale/offset/pivot/rotate) decal-style logo projection.

**Exact-count nearest points (VEX):** Near Points' default behavior returns inconsistent point counts per query point (more than requested, in uneven "islands"), which is often undesirable. The fix: in a wrangle, use **`pcfind()`** (the array-returning point-cloud find, not `nearpoints()`) against input 1 (the actual target mesh, not the sparse query points) to retrieve exactly N point numbers into an array detail/point attribute, then on the sparse query points read that array via `find()` to check whether the current point number exists in the found set — grouping only exact matches. This guarantees precisely the requested number of nearby points (even just 1) instead of Near Points' default all-or-nothing island behavior.

### Key Steps
1. **Peel base + spiral:** transform/deform a QuadSphere into a potato shape; Subdivide for later steps; build a spiral curve aligned to the potato's centroid, reproject it onto the potato surface, copy the potato's surface normals to an attribute so **Sweep** can use them directly (otherwise the swept ribbon is malformed).
2. **Peel mask + Boolean cut:** on the subdivided potato, compute **Distance from Geometry** relative to the spiral curve, Clip based on that mask, promote the resulting point group to a **vertex group** (required for correct UV alignment later), then run a **Boolean** using that clipped piece against the main geometry — this Boolean is what actually separates the peel strip.
3. **UV alignment:** **UV Flatten** using the saved vertex group to get clean, axis-aligned UVs along the peel strip (without the vertex group, UVs come out unusable for the next step).
4. **Animated peel mask (VEX):** Split the UVs and promote to a point attribute so a Point Wrangle can read `UV.x` directly; build a ramp lookup driven by curve-U (`curveu`) plus a **time-based offset** (`fit(time, 0, 1, -1, 1)` conceptually) to create a mask that grows/animates across the surface between frames.
5. **Apply peel displacement:** subtract the animated mask (scaled by an amplitude) from `P.y` to physically displace the peel strip as it "grows," producing the final peeling reveal animation.
6. **MPM rest-space sim + transform capture:** simulate the MPM liquid in the bottle's **rest space** rather than literally spinning the container; separately drive an animated-noise-based rotation, capture it as a **transform attribute** (matrix), and copy it to a detail attribute so it survives into the DOP network (which otherwise only reads the first frame of a per-point/detail attribute, not its per-frame animated value).
7. **OpenCL gravity-via-transform kernel:** inside the MPM solver's dive target, replace a VEX force snippet with an **OpenCL** kernel: bind a `force` output attribute (OpenCL supports creating attributes), bind the detail transform-matrix attribute, expose a `gravity` parameter, and in the kernel convert the matrix to a 3x3 (`matrix3`) to strip translation, multiply by the gravity vector, and assign the result to `force`.
8. **Reapply transform after sim:** after the MPM sim completes and is meshed in rest space, reapply the earlier-saved transform attribute to the final geometry to get the visually "spinning bottle" splash effect seen in the render.
9. **Clean contact-area snapping:** after meshing simulation geometry that touches a rigid prop (e.g., bottle interior, reused from the original procedural model's groups), compute a per-point **distance to the bottle geometry**, Fit-range it between 0 and a tunable offset to build a blend mask, then **lerp** between the current (bumpy) position and a version of the geometry projected onto the bottle surface, using that mask as the blend factor — snapping only near-contact points cleanly; finish with a small **Peak** (to force slight intersection for a clean render seam), an **Attribute Blur**, and reapply any saved transform.
10. **Planar projection setup (MaterialX/Karma):** read `P` (or a `rest` primvar for animated objects) via Material Expression/primvar reader, swizzle out the X and Y components, combine into a Vector2 via **Combine/Vector 2 Float**, feed as UVs into an **Image** node (set Wrap/Address mode to **Constant** on both axes to prevent back-face bleed), and insert a **Place2D**-style node between the swizzle and the image to expose Scale, Offset (X/Y), Pivot, and Rotate controls.
11. **Correct alpha + composite:** multiply the projected image's alpha channel by a Z-axis-facing mask (so the logo doesn't appear on the back side) to get a clean alpha, then **Mix** the projected logo over a flat background color using that alpha as the mix factor.
12. **Exact-count near-point selection (VEX):** on the target mesh (input 1), run `pcfind()` (or an array-returning point-cloud query) to retrieve exactly N nearest point numbers relative to each sparse query point, storing the result as an array attribute; on the sparse query points (input 2), read that array and use **`find()`** to test whether the current point number is present (result ≥ 0 if found, negative if not), grouping only the matches — guarantees exactly N points found per query, unlike Near Points' inconsistent default behavior.

### Houdini Nodes / VEX / Settings
SOPs: QuadSphere, Transform, Subdivide, curve/spiral generation, Align (to centroid), Ray/reproject, Attribute Copy (normals for Sweep), Sweep, Distance from Geometry (Measure), Clip, Group Promote (point→vertex), Boolean, UV Flatten, Split UVs (Split Vertex Points-style), Attribute Promote (vertex→point for UV.x access), Attribute Wrangle (VEX: `chramp()`/curve-U + time-based fit for animated mask; position displacement via mask*amplitude; `pcfind()` + `find()` for exact-count nearest-point matching), Peak, Attribute Blur. DOPs/MPM: rest-space simulation, animated-noise-driven rotation → Transform Matrix → detail attribute copy, OpenCL node (bound `force` output, bound detail transform attribute, exposed `gravity` parameter, `matrix3` conversion to strip translation) as the dive-target force method (Houdini's recommended approach over VEX for MPM). Karma/MaterialX: Primvar Reader (position/rest), swizzle/Separate, Combine (Vector2), Place2D-style transform node (scale/offset/pivot/rotate), Image (Wrap/Address mode: Constant), Mix (alpha-driven composite).

### Difficulty
Advanced/Expert — spans UV-driven procedural animation, OpenCL kernel authoring for MPM dive targets, and non-trivial point-cloud VEX; each tip assumes strong existing Houdini fundamentals.

### Houdini Version
20.5 (UI/MPM/OpenCL workflow consistent with Houdini 20.5-era tools).

### Tags
#vex #uv #opencl #mpm #simulation #materials #shaders #karma #procedural #tips #advanced

---

## Related Tutorials
Cross-link with any other cgside VEX-tips or MPM/simulation tutorials once extracted from this batch — the OpenCL dive-target force technique and exact-nearest-point VEX pattern are broadly reusable across other procedural/sim setups.
