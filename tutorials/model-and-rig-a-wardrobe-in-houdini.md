---
title: Model and Rig a Wardrobe in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=c_t8JwyHJrA
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, kinefx, rigging, vex, fracture, procedural, furniture, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/model-and-rig-a-wardrobe-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Model and Rig a Wardrobe in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=c_t8JwyHJrA)
**Author:** cgside
**Duration:** 10m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'll show you how we can create this
[0:04] asset in Odini and also how to rig it so rig the opening of the doors. So let's
[0:14] get started by looking at the top. I'm starting with the grid which will
[0:19] like the single panel, then I'm copying it several times. In this case by using
[0:26] the bounding box exercise so it aligns properly or perfectly, then place it
[0:34] in the center and in this case I'm running a loop to divide the geometry into
[0:41] sections. I am switching between, in this case I have a switch in here that
[0:47] randomly switches between just a wide division so just dividing the
[0:56] primitive in the middle. In this case by using the bounding box y size and
[1:03] divide it by two. As you can see this will give you the distance that it should
[1:10] place the line and on the other side I'm taking the primitive, creating a line
[1:20] to match the same size, in this case I'm taking uniform scale, then reassembling
[1:26] it to the amount of sections you want. Then in order I'm using a
[1:32] Voronoi fracture. If I disable this point cheater you can see that it's
[1:37] perfectly dividing the geometry into sections. I can do that easily with a
[1:45] divide. But since I wanted to randomize I use this setup which is a Voronoi
[1:51] fracture and for the Voronoi fracture you actually need point centers. As you
[1:58] can see I can show you. So you actually need point centers and not the
[2:06] the intersections itself. So in order to create the point centers after the
[2:13] re-sample I'm subdividing to get those point centers. Then selecting the
[2:21] outer ones so the original points by using a group arranged node selecting
[2:28] one or two, blasting those and that's basically how you get even distribution
[2:36] of sections. And then just I'm randomizing it so first selecting the inner
[2:44] points and then adding a point cheater to those inner points. In this case I
[2:49] changed the seed on each iteration which you can do by using the detail, the
[2:57] the iteration detail attribute. And you get something like this. So in here I'm
[3:06] just alternating between the inputs by using a random function and multiplying
[3:13] by the output which is the number of inputs we have. And if I show you let me
[3:21] get this. Rightly parameters. If I show you in here the switch you can see switching
[3:34] between switching between 1 and 0. So that's how I've done that part. Then I'm
[3:49] just extracting the edges, the silhouette I mean basically by extruding it in
[3:59] or inserting it. And then I ended up with something like this, fusing the points,
[4:06] extruding it back, taking a bound and placing it in the back and just merging
[4:14] everything. At this point you can create some name attributes to target different
[4:19] geometries but I'm just doing this as an example so that's our wardrobe base.
[4:26] And now for the rigging. I'm starting with the base which is this part in here.
[4:35] So the base. Then selecting half of the frames in this case I have four I will get to by using
[4:44] in the end 10 frames divided by two. This case is getting to blessing every other primitive.
[4:53] And from here why should we go so first of all I'm creating an image reboot for each primitive
[5:05] by using a prefix and the prime number as a string. And here I'm doing some sub
[5:14] operations but we'll get there in a bit. So for the rigging I'm first creating some
[5:22] points at the center, at the left center of each prime by using the bounding box center
[5:30] and the bounding box mean commands. And then adding those points in this case by group with an
[5:40] add node, placing a rig doctor and initializing transforms. Then doing the capture back GU
[5:52] in this case using the name attributes and a bone deform. And where everything happens is on
[6:01] this rig wrangle that was kindly shared by swalch on the CG weekly scores. So so basically we
[6:13] create a parameter for the rotation in this case in radians. We want the input as degrees
[6:23] but we need to translate it to radians. In here we are we are alternating between minus one
[6:30] for even points and one for odds to create the alternating directions as you can see in here.
[6:38] Then we need on the first point to rotate only half. So we this is basically an if statement. If the
[6:46] point is zero, we want just to multiply by half of the rotation for the other one just
[6:56] use one which will have no effect multiplying by one. And in here we just use the pre-rotate
[7:03] for the local transform and multiply the panel angle which is this angle we have in here,
[7:09] this parameter and multiply it by the panel sign which is alternating directions. And also for
[7:19] the first panel which we just want to rotate half. And we want to rotate around why that's why
[7:26] we use the X's. Again shared by swalch which I'm very grateful and if you're interested in
[7:36] joining the CG weekly scores just check out Matistella Patreon and you'll get access to it.
[7:45] So having this we can now mirror the effect and we will get these nice sliding doors.
[8:01] Then we can just matchize it to the main part of the wardrobe and that's basically how it's done.
[8:12] For this pattern in here it's actually pretty simple. First of all let me see I already covered
[8:23] this part. So we're iterating over each frame and basically dividing it evenly, dividing each
[8:34] primitive evenly as you can see in here. So if you remember from these divide nodes and I shared
[8:44] these plenty of times on my channel. Basically you take the bounding box the size of the
[8:52] axis you're working with and divided by the number of divisions you want. So let's say five I
[8:59] get five sections in this case I set it to two and in here we're we're using a multiplier which
[9:12] I call density and basically taking the in this case the X size and dividing it by the same
[9:22] X size but with a seal since we want integer numbers and multiplied by the density.
[9:29] And if I change this to 20 we get less and we do the same for the Y axis as you can see.
[9:38] Then just extrude it in this case I am in setting it, extruding and creating some normals
[9:49] and we get something like this. So yeah that's basically it's if you like to get access to the
[9:57] full scene feel free to join my patreon and you can get all the project files from my videos along
[10:05] with exclusive tutorials and I also have some courses in there. So if you want to check that out
[10:12] and other than the self promotion that was basically it's thank you and I'll see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_000.jpg
- [1:45] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_001.jpg
- [3:20] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_002.jpg
- [4:10] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_003.jpg
- [5:00] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_004.jpg
- [7:40] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_005.jpg
- [9:00] tutorials/frames/model-and-rig-a-wardrobe-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
Modeling a wardrobe/shelving unit with **recursively randomized shelf divisions** (a Voronoi-Fracture-based alternative to a plain Divide node, seeded per-iteration for varied panel splits), then rigging its accordion-style **bi-fold sliding doors** with KineFX — a community-shared (Swalch/CG Wiggle Discord) rig wrangle that alternates rotation direction per panel and halves the rotation on the outer/first panel so the fold visually "closes" symmetrically.

### Summary
The wardrobe's back panel starts as a Grid, Copied several times using a **bounding-box-driven expression** for perfect alignment, then centered. To divide the resulting large panel into an irregular grid of shelf/drawer sections, rather than a plain Divide node, a **loop-based recursive Voronoi Fracture** is used: each iteration randomly Switches (`random()` × input count) between a horizontal-only split (computed via bounding-box Y-size / 2) and a vertical-only split (matched-size line via uniform scale), reassembled to the desired section count. Since Voronoi Fracture needs actual **point centers**, not raw line intersections, the split lines are Resampled and Subdivided specifically to generate center points, with the original/outer points (from a Group Range selection) Blasted away, leaving evenly-spaced interior centers; those interior points are then Point-Jittered with a **seed that changes per for-each iteration** (via the loop's `iteration` detail attribute) for organic randomized subdivision instead of a rigid grid. After building up the fractured panel pattern, the silhouette/edges are extracted (via Inset + Extrude), points Fused, extruded back for thickness, a Bound added for the back panel, and everything merged into the base wardrobe carcass (author notes name attributes could be added per-part for later shading, but weren't in this pass, since it's just a demo). **Rigging the sliding-door "accordion" panels:** starting from the base wardrobe's front frame (e.g. 10 divisions halved via Blast to isolate every-other primitive), an Object Merge per primitive (named via a prefix + primitive-number string) sets up individual door panels; a rig point is placed at each panel's **left-center** (Bounding Box Center combined with Bounding Box Mean), grouped via Add, initialized with **Rig Doctor**, captured via **Capture by Group** (using the name attributes), and driven by **Bone Deform**. The actual fold/open animation logic lives in a **Rig Wrangle** (shared by community member "Swalch" via the CG Wiggle Discord, accessible through Matteo Stella's Patreon): a user-facing rotation-angle parameter (input in degrees, converted to radians), an **alternating sign** (`-1` for even points, `1` for odd, so adjacent panels fold in opposite directions like a real accordion door), and a special case for the very first panel — an `if` check multiplying its rotation by **half** the angle (all other panels multiply by the full 1x) so the outermost hinge panel only swings half as far, keeping the fold symmetric and closing flush; the final pre-rotation is applied to the local transform (rotating around the **Y axis**) as `panel_angle * panel_sign * (half-multiplier for panel 0)`. Mirroring this rigged half onto the other side produces the complete pair of accordion sliding doors, then Match-Sized onto the main wardrobe body. **Panel/divider pattern (recap):** the general technique used throughout — computing a `density` value as `(axis_size / ceil(axis_size)) * density_constant` and feeding it into a Divide node's per-axis division count — is the same bounding-box-driven, integer-safe division-count pattern the author has shared repeatedly across other videos; increasing the density constant produces finer divisions, decreasing it produces coarser ones; finished with Extrude + Normal recompute for the paneled surface look.

### Key Steps
1. **Base panel array:** Grid → Copy (bounding-box-driven expression for perfect alignment) → center.
2. **Randomized recursive division setup:** inside a for-each loop, use a **Switch** driven by `random()` × input count to alternate between a horizontal split (bbox Y-size / 2) and a vertical split (matched-size line via uniform scale) each iteration.
3. **Generate true point centers for Voronoi:** Resample and Subdivide the split lines specifically to produce point centers (Voronoi Fracture requires actual points, not raw line/edge intersections).
4. **Isolate interior centers:** Group Range selects the original/outer points; Blast removes them, leaving only the evenly-distributed interior center points needed to seed the fracture.
5. **Randomize per iteration:** apply Point Jitter to the interior points with a **seed sourced from the for-each loop's `iteration` detail attribute** — changes every recursive pass for organic, non-repeating subdivision.
6. **Reassemble to target section count:** repeat the loop for the desired number of shelf/drawer sections, reassembling results each pass.
7. **Extract panel silhouette:** Inset + Extrude to pull out clean edge geometry from the fractured pattern, Fuse points, Extrude back for material thickness.
8. **Assemble the carcass:** add a Bound for the back panel, merge all pieces into the base wardrobe (name attributes optional per-part, skipped here as a demo).
9. **Isolate door-panel primitives:** from the base wardrobe's front frame, Blast to keep every-other primitive (e.g. half of 10 divisions) — these become individual bi-fold door segments.
10. **Per-panel setup:** Object Merge each primitive (named via prefix + primitive number), place a rig point at each panel's **left-center** (Bounding Box Center + Bounding Box Mean), group with Add.
11. **KineFX rig init:** **Rig Doctor** to initialize transforms, **Capture by Group** (using the panel name attributes) to bind geometry to rig points, **Bone Deform** to apply the resulting animation.
12. **Custom rig wrangle (Swalch/CG Wiggle):** expose a rotation-angle parameter (degrees, converted to radians internally); compute an **alternating sign** (`-1` even points / `1` odd points) so adjacent panels fold in opposite directions; special-case the first/outermost panel via an `if` to multiply its rotation by **half** the angle (others use the full multiplier) so the hinge panel swings only half as far.
13. **Apply the rotation:** pre-rotate the local transform around the **Y axis** by `panel_angle * panel_sign * (half-factor if panel 0)`.
14. **Mirror + finalize:** Mirror the rigged half to produce the complete accordion door pair, **Match Size** onto the main wardrobe body.
15. **General panel-division pattern (reused technique):** compute `density = (axis_size / ceil(axis_size)) * density_constant`, feed into a **Divide** node's per-axis division count for integer-safe, tunable panel counts (higher constant = finer divisions); finish with Extrude + recomputed Normals for the surface panel look.

### Houdini Nodes / VEX / Settings
Modeling: Grid, Copy (bounding-box expression alignment), For Each loop (iteration detail attribute for per-pass random seeding), Switch (random-driven horizontal/vertical split alternation), Resample, Subdivide (point-center generation for Voronoi), Group Range, Blast, Point Jitter (iteration-seeded), Voronoi Fracture, Inset, Extrude, Fuse, Bound, Merge, Divide (bounding-box/ceil-driven density expression), Normal. Rigging/KineFX: Object Merge (per-primitive, name-prefixed), Bounding Box Center, Bounding Box Mean, Add (grouping), Rig Doctor, Capture by Group (name-attribute-based), Bone Deform, Rig Wrangle (VEX: `radians()` conversion, alternating even/odd sign, `if`-based half-rotation for the first panel, pre-rotate around Y using panel angle × sign × half-factor), Mirror, Match Size.

### Difficulty
Intermediate — the recursive Voronoi-based division and KineFX rig wrangle are non-trivial but well-explained; assumes comfort with for-each loops, group/point manipulation, and basic KineFX rigging concepts.

### Houdini Version
20.5 (UI matches Houdini 20.5-era KineFX/modeling toolset; rig wrangle credited to community member Swalch via the CG Wiggle Discord).

### Tags
#modeling #kinefx #rigging #vex #fracture #procedural #furniture #intermediate

---

## Related Tutorials
Cross-link with kinefx-and-vellum-fluid-in-houdini.md (same author, overlapping KineFX rig-wrangle and Capture-based rigging vocabulary) once indexed together — the general bounding-box/ceil-driven Divide-density pattern is reused across multiple other cgside tutorials in this batch.
