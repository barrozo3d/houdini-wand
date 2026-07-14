---
title: Handy Houdini Tips | Vellum, UVS, Modeling and More
source: YouTube
url: https://www.youtube.com/watch?v=h6wt3KJy2W4
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, uv, vellum, modeling, procedural, animation, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Handy Houdini Tips | Vellum, UVS, Modeling and More

**Source:** [YouTube](https://www.youtube.com/watch?v=h6wt3KJy2W4)
**Author:** cgside
**Duration:** 12m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] Though in today's video I'm going to share a few different tips from modeling to UVs
[0:06] to VACs.
[0:07] There will be something for everyone, hopefully.
[0:10] So I wanted to start with this example, which is using the Slurp function in VACs.
[0:15] So basically I start with a PAC object that just has a color applied to the front face
[0:23] as you can see that I apply in here.
[0:25] And then I'm packing, you end with a single point, single print, PAC primitives, then
[0:30] I'm transforming to a position, so in this case this position, and then transforming
[0:35] it to a target position.
[0:37] And then I want to blend between those two positions and do some rotations in between.
[0:43] So how can we achieve this?
[0:46] So let me press E and let's have a look at the code.
[0:50] So first of all I'm getting the...
[0:53] I'm creating a time variable where I will do the animation, which is just a feat of time
[0:57] between 0 and 1 seconds and then from 0 to 1, just the blend amount.
[1:05] Then I'm getting the PAC transform, both from the first input and the second inputs,
[1:09] and then doing a Slurp, which is like a Lurp, but for matrices.
[1:14] So I'm slurping between the first position and the second position and as a blend amount
[1:19] I'm using the animation as you can see from 0 to 1.
[1:22] But in between I want to add some rotation, so for that I'm creating in your rotation
[1:26] angle that I'm going to create as a spare parameter and I'm doing by times tool, which
[1:34] is a full rotation as you can see.
[1:38] And then I am multiplying that by the animation, so it blends along the way, so it transforms
[1:46] from one angle to another.
[1:49] Then using that angle in a Quaternion along the Y axis and converting that rotation
[1:55] Quaternion to a matrix, matrix, and finally just multiplying the rotation matrix by that
[2:02] matrix that we have created with a Slurp, then just using a setback transform, we can set
[2:08] the final matrix and we get this interpolation and we can come in here and set this by times
[2:14] 4 and it will do more rotations or only 5 and it will rotate only once as you can see,
[2:22] only 180 and that's the effect is to do the 360.
[2:27] So yeah, that was the first tip.
[2:30] So in this one I wanted to share how you can create UVs from pipe geometry, let's say
[2:35] this kind of rounded geometry that you end up with these kind of UVs.
[2:40] So as you can see I haven't modeled these, I have modeled these not using the sweep,
[2:46] so I started with the tube, oops, let me select these, then the polyfill, started the
[2:52] primities by Y, did the polywinge, polyinge, then extruded another one and then in
[2:57] here I selected the endgones and blessed them away.
[3:03] So as you can see I haven't modeled these with a sweep and in order to do the UVs I wanted
[3:07] to find an automatic way, automatic but requires some work of course.
[3:13] Of course you can just use a UV flatten and select one seam but let's say you want to
[3:17] do these in an HDA and you want to do it automatically.
[3:21] So you start with the geometry, then we select the Unchared but create a boundary group
[3:27] so it creates a group for each boundary, then we select one of the boundaries and in a
[3:33] group expand we expand the whole contain geometry and create a step attribute and what
[3:38] this will do is create these attributes along the mesh as you can see.
[3:42] So like an ID is an integer, so let me actually get rid of that visualization, then we select
[3:48] a start point.
[3:50] So basically in a detail wrangle we expand the point group of these Unchared points in
[3:56] here and we select the last one, in this case this point three 97.
[4:01] So we select the last one in here and we set that point group called start, then we
[4:07] extend the loop with the group point path, we extend this loop and we get the loop in
[4:18] the starting from that point, we get this loop inside and of course we also get these
[4:24] on the Unchared points but that doesn't matter because they are unchared and what be part
[4:28] of the UVs.
[4:30] So we convert that to edges and we just UV flat and as you can see and we do the same
[4:37] and we do rectify and we get something like this.
[4:41] Of course if you get the UVs upside down you we can easily orient them the way you want
[4:48] just by unwrapping in place the UVs and using that geo as to get the bounding box center
[4:55] of the UV shell, move it to the center, transform the UVs in this case I'm inverting.
[5:00] So just flipping them around and then making them placing them at the center again as
[5:06] you can see so it stays in the same place and we don't need to UV layout.
[5:10] So again pretty useful in case you are doing this type of geometry but also useful if you
[5:15] want to get some overview on how you can play with selections and procedural selections
[5:22] and procedural UVs.
[5:25] So I did this volume simulation that you can see like wrapping a candy and I wanted to
[5:33] show you how you can take masks from the geometry input where I have for example in here this
[5:42] zip mask that it's around where it's smaller and I also have a mask in here for the top
[5:48] part that I'm procedurally you can look at the piles on Patreon or no I did this
[5:53] setup but today I wanted to share how you can take that mask in geometry and move it into
[5:58] constraints.
[5:59] So as you can see it will be pretty simple just a simple wrangle and in here I'm just using
[6:04] the UV sample to sample that attribute using the position as a sample value and you can
[6:12] take that mask that now lives on constraints and inside the solver you can take that and
[6:19] let me see where did I read that in this case I'm using it I'm reading it's in the
[6:23] point so I'm reading that using just ptnm in a point expression in a point function and
[6:28] then lurping between a rest scale of one and reducing it a bit on that mask and other
[6:35] values I'm using the mask of course.
[6:38] So that's how I what I wanted to share in this tip just using UV sample is the easiest
[6:43] way to sample attributes from geometry to constraints and at the end we get this result
[6:50] you can have a look at the file on Patreon I'm gonna share all the scenes that I've demoed
[6:53] in this video so yeah.
[6:58] So this one I wanted to show you how you can easily model mockups to sell online or something
[7:04] like that.
[7:05] So in this case the way I'm modeling this is by creating first a circle then clipping
[7:12] it in half let me run through the notes.
[7:15] Re-sample it, symmetrize and fuse and polypating to have a unite curve and make sure the
[7:22] points are are mirrored so I always have a point at the center.
[7:29] So this is one part then in the other I'm just using a simple shapes rounded rectangle
[7:34] transforming it around clipping and doing the same things symmetrize fuse and polypate
[7:38] and making sure I reverse.
[7:41] Then I'm creating two points from that geometry using the numbers by reading the position
[7:48] of the points and adding two points that I can later add and re-sample and finally do
[7:53] a skin and if we look at the result we can get this re-sample and define the amount of
[8:00] divisions we want and the same in here we can define the amount of divisions we have.
[8:05] Just make sure you have the same amount of points on the two shapes that you are using
[8:08] to skin with.
[8:10] So in this case I'm skinning this line that I created and then using those two shapes
[8:16] as a second input as cross sections.
[8:20] So this is you and re-cross sections.
[8:23] So that's how I'm doing the modeling of the tube and it doesn't get cleaner than this.
[8:29] Using a UV flatten just to create the UVs, fusing normal blurring it a bit and then
[8:35] playing around with the wrinkle deformer.
[8:38] So let me get back to this.
[8:41] I bet as you can see this doesn't look like grumblet so what I'm doing is measuring the
[8:47] thickness so I can get this mask as you can see and then I'm also creating another mask
[8:56] along the z.
[8:58] I can blend it and do a pick so I don't want to pick on the areas and need around the
[9:03] small areas otherwise I will get clipping.
[9:06] So and then I'm subdividing so this peak in here similar to what we have done in the
[9:11] Chocolate Break project is just creating that grumblet look as you can see.
[9:16] Then I'm modeling this part which is just a bunch of extrogements.
[9:20] So yeah that's how I'm doing this quick mockup.
[9:26] So I was trying to model a guitar case with a specific design that had this indentation
[9:32] in your like a V shape on the top and then this line extruding out and then some smoothing
[9:39] at the end.
[9:40] So hopefully you can see it in the recording let me do 3 point lighting and as you can
[9:45] this is easier to show you.
[9:49] So how did I did that part?
[9:50] So after I can run you basically I'm using an alpha tracing triangulating blessing
[9:58] away some creams, symmetrising remesh, what remesh extruding and you know doing the
[10:04] basic modeling and then bubbling the corners and that's our base shape.
[10:09] Now how do I add that indentation?
[10:11] First of all since we're going to work deform geometry we need to have fidelity we need
[10:16] some resolution that we can later and subdivid if we need.
[10:20] So I'm starting by drawing two shapes that V shape at the top that I can just easily mirror.
[10:25] So starting with the curve just model took just drawn took curves then symmetrise it,
[10:30] fuse it polypads, re-sample fuse then selecting the primitive zero button points.
[10:37] So just saying that premium is equal to zero in a group expression.
[10:41] Then as you can see this lays flat on the Z axis so I'm going to do a software transform
[10:46] and move it a bit on those points.
[10:50] And I'm blasting the one of those creams since I just want to skin the top part and then
[10:59] polyx rooting and polyfilling it and and placing it where it needs to be.
[11:04] So we get this sort of placement as you can see and shape.
[11:08] And then it's pretty simple we can just do a simple XYZDist and we get these distance
[11:14] attributes as you can see that we can blur a bit and just move it just this place it
[11:21] along the normal and we add the final result which is similar to this and then we can
[11:28] un-sadivide if needed.
[11:31] So in case you need one subdivided you don't get as much detail but it's still there as
[11:36] you can see.
[11:37] So yeah those were the tips I wanted to share today guys and I hope you found them useful.
[11:43] I'm trying to do a new project on the channel the Chocolate Split but unfortunately not
[11:47] many of you are interested in that project.
[11:51] I will try to fit it between videos since not many people show interest in that project.
[11:58] I think I was doing something worth it watching but unfortunately it didn't get the views
[12:03] or the feedback so I'm going to finish that project but meanwhile I will do other videos
[12:11] random videos like I do on the channel on different topics.
[12:14] So yeah as always you can grab all the scene files on my Patreon alongside with exclusive
[12:18] tutorials every month I do an exclusive tutorial that's about one hour or more sometimes
[12:23] two hours of video going step by step on a specific project and yeah you'll free to join
[12:30] the Patreon where you support me and you get all the perks.
[12:34] So thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_000.jpg
- [2:35] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_001.jpg
- [4:20] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_002.jpg
- [6:00] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_003.jpg
- [7:10] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_004.jpg
- [9:10] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_005.jpg
- [11:10] tutorials/frames/handy-houdini-tips-vellum-uvs-modeling-and-more/frame_006.jpg

---

## Structured Notes

### Core Technique
Five unrelated but reusable tips: animating a packed object between two positions with combined **slerp**-based translation and rotation in VEX, procedurally UV-unwrapping non-swept "pipe" geometry via boundary-loop path selection, sampling a geometry mask into Vellum constraints via **UV Sample**, a Skin-based approach to modeling smooth mockup shapes from two cross-section curves, and a distance-field-driven V-shaped indentation deformer for hard-surface props.

### Summary
**Slerp animation:** a packed object carrying two transforms (current position + target position, both extractable as matrices from input 1 and input 2) is animated by computing a 0-1 blend value from `fit(time, 0, 1, 0, 1)`, then using **`slerp()`** (Lerp for matrices) to interpolate between the two position matrices using that blend factor. A separate rotation-only angle (a spare parameter, multiplied by `2*PI` for one full turn, itself scaled by the same blend factor) is converted to a Y-axis quaternion, turned into a rotation matrix, and multiplied into the slerped position matrix before being applied via **`setpackedtransform()`** — letting the object simultaneously translate and spin any number of times (tunable via the multiplier) during the transition.

**Procedural pipe UVs:** for hand-modeled "pipe" geometry (built without Sweep — starting from a tube, polyfilling, splitting by primitive-Y, wedging/extruding, then blasting away n-gon caps), a fully automatic UV-unwrap suitable for HDA use is built by: grouping the unshared boundary edges (with "create boundary groups" so each boundary gets its own sub-group), Group Expand-ing one boundary across the whole connected mesh to stamp a sequential integer **step attribute** as a path-distance ID, then a detail wrangle expands that same unshared point group and picks the last point in it as a loop **start point**; **Group Find Path** extends a seam loop starting from that point, which is converted to edges and fed to **UV Flatten + Rectify** — producing a clean, single-seam UV layout without ever manually picking a seam. If the resulting UVs come out flipped/upside-down, they're corrected by Unwrapping in Place, computing the UV-shell's bounding-box center, moving it to origin, flipping (Transform), then moving back — avoiding a full UV Layout pass.

**Vellum mask via UV Sample:** a previously-built procedural mask (e.g. a "zip" tightening mask and a separate top-region mask on candy-wrapper geometry) is transferred from geometry into Vellum constraints with a single wrangle using **UV Sample** — sampling the mask attribute at each constraint's position — so the mask now "lives" on the constraints. Inside the Vellum solver, that constraint-space mask is read per-point via a Point Expression (`point(0, "mask", @ptnum, 0)`-style) and used to **lerp** the rest scale between 1 and a reduced value (and similarly to drive other constraint parameters), letting a purely geometric mask directly control simulation behavior without rebuilding it as a native constraint attribute.

**Mockup modeling via Skin:** to quickly model smooth product-mockup shapes (e.g. an hourglass-like bottle) without Sweep, two profile curves are built independently — one from a Circle (Clip in half, Resample, Symmetrize, Fuse, Polypatch to guarantee a mirrored center point) and one from a rounded-rectangle primitive (transformed, Clip, Symmetrize, Fuse, Polypatch, reversed for correct normal direction) — both resampled to have matching point counts. Two additional points are generated procedurally (via a Numbers-wrangle-style approach reading existing point positions, adding new points, then resampling) to define the tube's spine/rail, and finally a **Skin** node lofts a surface from that rail using the two profile curves as its two cross-sections — producing clean topology "cleaner than" alternative approaches. UVs come from a simple UV Flatten, then Fuse-normal + Blur + a **Wrinkle deformer** peaked with a mask (built from Measure Thickness combined with a Z-axis mask, blended and restricted away from thin/small areas to avoid clipping) creates a believable crumpled "candy wrapper" surface look — the same peaking technique previously used on the author's Chocolate Break project.

**Guitar-case V-indentation:** starting from an alpha-traced, triangulated, symmetrized, remeshed, extruded, and corner-beveled base shape, a specific V-shaped top indentation is added procedurally: two curves (a top V-shape, hand-drawn and mirrored via symmetrize/fuse/polypatch/resample/fuse) define the indent's footprint; primitive-0 boundary points are grouped (`@primnum == 0` in a Group Expression) and Softimage-Transform-moved to displace them off the flat Z-plane where they initially lie; one crease is Blasted away since only the top part needs skinning, then Poly Extrude + Poly Fill positions the shape correctly. A simple **XYZ Distance** (distance-field) attribute from that shape onto the base geometry is Blurred and used to displace points along their normal, producing the indentation; the mesh can optionally be un-subdivided afterward for a lower-poly version that still preserves the detail.

### Key Steps
1. **Slerp animation setup:** extract packed transforms from input 1 (current) and input 2 (target) as matrices; compute an animation blend factor via `fit(time, 0, 1, 0, 1)` (0-1 over the first second); interpolate the two position matrices with **`slerp()`**.
2. **Layer in rotation:** expose a spare "rotation angle" parameter, multiply by `2π` times a user-controlled turn-count and by the same 0-1 blend factor; build a **quaternion** around the Y axis from that angle, convert to a rotation matrix, and multiply it into the slerped position matrix before applying via `setpackedtransform()` — tuning the turn-count multiplier controls how many full/partial rotations occur during the transition (e.g. x4 = multiple spins, x0.5 = a half turn).
3. **Model pipe geometry without Sweep:** Tube → Polyfill → split primitives by Y → Poly Wedge/Extrude → Blast n-gon end caps — an alternative modeling path to Sweep that leaves awkward default UVs needing a custom solution.
4. **Boundary path/step attribute:** Group the unshared edges with "create boundary groups" enabled (one sub-group per boundary loop); Group Expand one boundary across the whole mesh while writing an incrementing integer **step** attribute, effectively giving every point a path-distance ID from that boundary.
5. **Pick a start point + extend the seam:** in a detail wrangle, expand the unshared point group and select its last point as the loop start; feed that into **Group Find Path** to extend a full seam loop starting there.
6. **Flatten UVs:** convert the found path to an edge group, run **UV Flatten** + **Rectify** on it — producing clean UVs from a single automatically-chosen seam, suitable for use inside an HDA without manual seam-picking.
7. **Fix flipped UVs without UV Layout:** Unwrap in Place, compute the UV shell's bounding-box center, move the shell to the origin, apply a Transform (flip/invert), then move it back to its original position — corrects orientation while preserving placement.
8. **Vellum mask transfer via UV Sample:** in a simple wrangle, use **UV Sample** to read a pre-built geometric mask attribute (e.g. a "zip"/tightening mask, or a separate top-region mask) at each Vellum constraint's position, effectively moving the mask from geometry space into constraint space.
9. **Use the mask inside the solver:** inside the Vellum Solver, read the transferred mask per-point via a **Point Expression** (`point(0, "mask", ptnum, 0)`-style, referencing `@ptnum`), then **lerp** the rest-scale constraint parameter between 1 and a reduced target value using that mask (and similarly drive other constraint values), directly linking a geometric mask to simulation behavior.
10. **Mockup profile curves:** build one profile from a **Circle** (Clip in half, Resample, Symmetrize, Fuse, Polypatch to guarantee a mirrored center point) and a second from a rounded-rectangle shape (Transform, Clip, Symmetrize, Fuse, Polypatch, Reverse for correct normal direction); resample both to have matching point counts (required for Skin to work correctly).
11. **Build the spine + Skin:** generate two new points along the rail (reading existing point positions, adding points, then Resampling) to define the loft path; feed that rail plus the two matching-point-count profile curves into **Skin** (second input providing the two cross-sections) to loft the final tube/bottle shape.
12. **Finish the mockup surface:** simple **UV Flatten** for UVs, Fuse normals, Blur, then a **Wrinkle deformer** with Peak — masked by a blend of a **Measure (Thickness)** attribute and a separate Z-axis mask (restricted away from thin/small regions to avoid clipping artifacts) — to create a crumpled candy-wrapper "grumblet" surface look, the same peaking technique from the author's Chocolate Break project.
13. **Guitar-case base + V-curve setup:** base shape from alpha-tracing → triangulate → Blast unwanted creases → Symmetrize → Remesh → Extrude → Bevel corners; separately draw a top V-shaped curve, Symmetrize/Fuse/Polypatch/Resample/Fuse it into a clean mirrored curve.
14. **Reposition + skin the V-shape:** group primitive-0 boundary points (`@primnum == 0` Group Expression, since the curve initially lies flat on the Z plane), **Softimage Transform** to displace them off-plane into position; Blast one now-unneeded crease (only the top needs skinning), Poly Extrude + Poly Fill to close/position the shape correctly.
15. **Distance-field indentation:** compute an **XYZ Distance** attribute from the positioned V-shape onto the base guitar-case geometry, Blur it slightly, then displace base-mesh points along their normal by that (blurred) distance value — producing the believable V-shaped top indentation; optionally un-subdivide afterward for a lower-poly version that still retains the detail.

### Houdini Nodes / VEX / Settings
Nodes/VEX: Attribute Wrangle (VEX: `fit()` time-to-blend, `slerp()` matrix interpolation, spare rotation-angle parameter, quaternion construction + matrix conversion, `setpackedtransform()`), Pack, Tube, Polyfill, Group (primitive-by-Y split), Poly Wedge/Extrude, Blast, Group (unshared edges, "create boundary groups"), Group Expand (step-attribute path distance), Attribute Wrangle (detail-scope: point-group expand + last-point selection for loop start), Group Find Path, Convert Line, UV Flatten, Rectify, Unwrap in Place, Bounding Box center computation, Transform (UV-shell flip), Attribute Wrangle (UV Sample for mask transfer to constraints), Point Expression (`point()` function reading constraint-space mask inside Vellum Solver), Lerp (rest-scale constraint blending), Circle, Clip, Resample, Symmetrize, Fuse, Polypatch, Reverse, Numbers Wrangle (spine-point generation), Skin (two-cross-section lofting), UV Flatten, Blur, Measure (Thickness), Wrinkle deformer + Peak (masked), Group Expression (`@primnum==0`), Softimage Transform, Poly Extrude, Poly Fill, XYZ Distance (Measure), Subdivide/Unsubdivide.

### Difficulty
Intermediate/Advanced — the slerp animation and Vellum UV-Sample mask trick are approachable; the automated pipe-UV boundary-path workflow and guitar-case distance-field indentation require solid procedural-modeling and VEX fundamentals.

### Houdini Version
20.5 (UI matches Houdini 20.5-era toolset; references the author's ongoing "Chocolate Break"/candy-wrap Patreon project).

### Tags
#vex #uv #vellum #modeling #procedural #animation #tips #intermediate

---

## Related Tutorials
Cross-link with chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson.md and cookies-and-chocolate-modeling-shading-and-sim.md (same author, same "peak/wrinkle for crumpled-wrapper look" technique referenced explicitly here) once both are indexed together.
