---
title: Procedural and Organic Modeling in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=8hUjc7BEI9g
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.724"
tags: [vdb, poly-bridge, lattice, vex, volume-vop, organic-modeling, sculpture, karma]
extraction_status: complete
frames_dir: tutorials/frames/procedural-and-organic-modeling-in-houdini/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural and Organic Modeling in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=8hUjc7BEI9g)
**Author:** cgside
**Duration:** 27m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video we will be creating this
[0:05] Etern Apple from start to finish step by step and although this is a very simple
[0:13] network as you can see there will be always a chance you can learn thing or
[0:19] to. So yeah let's get started! So as always we start with the geometry container
[0:27] let's drop a sphere and we will make it polygon and a frequency of 30. Now we
[0:39] want to create a mask for the top and bottom part. So for that let's use a point
[0:47] of up and we will use the relative bounding box and the y-components of vector
[1:00] of float and let's check the y-components and as you can see is going from the
[1:12] bottom to the top from 0 to 1 and we want to subtract constants we want to mirror
[1:21] this effect so let's subtract 0.5 and now we can absolute those values so we get
[1:32] something like this. Now we want to extend the range so let's go with a frequency
[1:43] range and say in the source mean to 0.33 something like this. Now we want to
[1:55] distort a bit this shape so for that we will use a turbulence noise connect
[2:04] position and we will make it as parse convolution and a 3D noise since we're going to be
[2:14] dealing with vectors and in this case I want a frequency of 6 and I'm going to offset
[2:31] it and the amplitude will be really small so 0.11 something like this we might increase
[2:41] turbulence but let's about it. So now we'll clip those polygons around the mask so
[2:56] for that I'm going to create a rest position. Create a random oops and I'm going to say
[3:10] vhp.y is equal to hcd.r so something like this now we can clip and we'll say
[3:27] our primitives and create another rest and this time extract so we create the attributes
[3:39] and check so we've clicked. Let's see where this is failing so we have that b dot y so this
[4:08] should be working so clip I might need to adjust so I'm going to create first the groups
[4:17] and say point of four I'm going to offset it all it'll be it and now it's creating a line.
[4:28] So I created the group so I can split the polygons now so let's say above plain and create
[4:38] two nodes so we have both geometries for this one I just want to set the bytes so when
[4:52] I feed it to the vdb it will be small enough so about two and for this one I'm going to group
[5:09] the unshared edges so I'm share the edges and on work line to convert those two curves so
[5:24] I'm shared and remove unused points and connect pets so we have a single primitive per curve
[5:34] now I'm going to re-sample about points and group the points so let's say points and
[5:59] I'm shared and create boundary groups so we have two groups one for each curve and now we can
[6:08] group the nodes and we will promote group zero and group one to edges and now we can poly breach
[6:22] and we will breach the group zero to group one so something like this
[6:37] and we want to increase the subdivisions so to about 60 and also play with the thickness ramp
[6:53] let's just play some reverse in here and go to the breach and under the thickness ramp so we'll
[7:09] create a point and let's go with this plane and move it down and create two points in here
[7:21] maybe maybe move this up a bit and these extremes so something like this
[7:39] as you can see it's all jacked up but we don't need to worry about that let's just make sure it's
[7:48] using at the same so let's just use and point all over one so you can see it's using some points
[8:08] and now let's get rid of the curves I have a back snippet for that so where is that? Remove curves
[8:21] just check for the priming tree is it closed and if it's open it will remove the the
[8:29] frames which are the curves so now we can create an attribute blur and we will blur it quite a bit
[8:45] so let's say about 500 and we want to do it in the edge line so we can keep the shape
[8:54] and now we will create a group for the unshared points and also a mask so these
[9:09] distance along geometry let's select the unshared and go for the mask let's see how that looks
[9:24] so something like this everyone is indeed to parameter in invert the mask and move for like one
[9:37] so something like this and now let's also create an attribute and we'll call it inside
[9:49] so we can target those that area after and let's say one so it's similar to the mask but it
[10:01] encompass all the geometry so I believe that's all now we can use smudge
[10:15] and let's remove let's see how that looks something like this and now we will create a VDVs
[10:26] so we will change it to density and let's say point all
[10:43] all weight for now we will increase it in a bit and since we want different densities for the masks
[10:54] we will duplicate this one and remove and let's get the inside and put the inside
[11:11] and get the mask and the VDV in notch I'm just trying to optimize and in this case we want also to
[11:28] fill the interior and increase the exterior band to point one so quite a bit
[11:42] and now let's just side those masks so I'm gonna say expose oops unshared primitives
[11:56] to why it's everything else when now let's create a volume box and if you check we have the
[12:05] inside and we have the mask now let's create a volume box and we will create also
[12:17] turbulence noise so turbulent noise let's connect the position and add it to the density
[12:30] it won't look like much because we need to multiply it with the mask so bind mask
[12:48] so something like this and we will change the type of noise to sparse convolution noise
[13:08] and repeat it to something like this and also offset it and change the amplitude to point all six
[13:27] and we can even reduce the roughness and the turbulence so let's just check here maybe we want to decrease
[13:43] so let's actually set the final resolution 0.03 and point all let's see I used the lower one but just speed up
[14:06] now I'm getting these weird results let me I know I need to fill the interior
[14:20] and let's use this and increase the point one
[14:27] yeah something like this now in this middle part I want to stretch a bit the noise so for that I'm
[14:45] going to duplicate this noise and change the frequency to five and now I need to copy this set up
[14:59] from above so let's go in here and copy these relative bounding books until here
[15:19] let's paste it we can remove these ads because we want that noise we just want to mess
[15:29] let me find some space and we'll take the vectors of track point five the absolute
[15:44] and use a mix to mix between these noise which will look like this so kind of stretch but I don't
[16:03] like what it does here on the on the top and bottom part so I'm going to mix it so mix this one
[16:17] with this one
[16:21] and the final result will be multiplied with a mask
[16:27] and as the mixing factor I'm going to use this one but adjust the feed range so I'm going to see
[16:43] point two and you can say zero and let's check the result
[16:55] so as you can see we have the other noise in here but it's stretching over here
[17:01] so I guess this is done and now let's move to create a smooth SDF
[17:20] and we will do just one iteration on the mean curvature flow
[17:32] and we will get probably a warning because we have different VDBs so let's go with density
[17:44] and let's convert polygons
[17:55] and we still get a pretty sharp transition
[18:02] and then we could increase
[18:07] it's already pretty good so let's keep going now let's do a natural vote from volume
[18:20] and let's then read the inside and inside
[18:26] so we have the mask as you can see and now let's create this indentation on the on the top let's
[18:40] keep the bottom like that so let's do a rematch and I'm going to rematch it
[18:55] about point 0 weight
[18:57] and I'm going to also use a lattice to deform the shape so let's create a lattice
[19:11] this will go in here the resposition let's create a habit
[19:19] and place it in here and change these two points
[19:27] and it will load for a bit
[19:40] and we need to change some things in here let's first do some edits so I'm going to create
[19:49] select these two and go over to points and unlock the selection I'm going to pick
[19:58] the middle point let's use this one and press t for the move tool
[20:06] increase the soft radius and maybe not so much
[20:14] something like this you know I'm going to pick these points
[20:25] and move them up so maybe reduce the radius
[20:30] let's move them up so something like this let's check the lattice
[20:41] create an all and it's not changing much because we need to change
[20:49] the settings in here and also the radius which is too much now
[21:00] so let's change it to point 1
[21:11] we got something maybe we need to move those points down a bit
[21:20] now as you can see it's pretty fast
[21:31] we got something we can do the same on the bottom but I'm going to leave it up to you
[21:40] and now it's pretty simple we just need to create a group
[21:50] first of all let's create an attribute layer and do we turn the inside
[22:03] let's say five let's see how that looks and create a color
[22:10] let's speak a red color
[22:21] and create another one and yellowish star
[22:27] so I can like this and create
[22:35] add it into the inside so
[22:40] and go for points
[22:44] say point 5 point 6
[22:49] so there we have the colors and we can target that same attribute for materials
[22:59] and now let's come in here and select maybe this is not so in the middle but okay
[23:08] let's forget about that now is not even properly set
[23:19] and I'm having trouble selecting the middle point
[23:28] something like this let's create a line along the z axis
[23:37] along the y can keep along the y copy the points
[23:43] and the target point will be group 2
[23:52] and this will copy along the z axis so we can just set it with just the vector
[24:01] and place it in here to reset the normals
[24:05] and we will also
[24:14] decrease the length to point 15 and say 20 points I'm just trying to create the stem
[24:24] just quickly
[24:25] and let's press enter press b and bend it
[24:33] keep pressing b now it's bending
[24:38] let's bend it this direction
[24:46] so
[24:46] so I actually want to bend it to the top
[24:56] so something like this
[25:01] and maybe let's see
[25:07] yeah this is correct
[25:09] so now I can attribute the lathe
[25:13] the lathe call the attributes
[25:16] create a sweep
[25:18] sweep
[25:20] round 2
[25:24] let's check this control click
[25:29] now I'm going to decrease these
[25:32] create a grid and create some divisions apply scale
[25:45] and let's go repeat it spline maybe increase these
[25:55] and decrease the roundness
[25:57] and now we still much
[26:03] which is need to increase this one
[26:07] so something like this
[26:11] let's create some coloring here
[26:16] and finally select routes
[26:20] and marches
[26:22] so yeah guys that was it hopefully you learned a new trick or two
[26:33] and make sure to check out my patreon where you can find exclusive courses, exclusive tutorials
[26:41] and all the project files from my videos including this one
[26:46] so if you feel like supporting me over there it will be nice
[26:51] and anyways I hope you have enjoyed this one and I'll see you in the next one bye



---

## Captured Frames

- [0:30] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_000.jpg
- [1:40] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_001.jpg
- [3:20] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_002.jpg
- [6:20] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_003.jpg
- [8:40] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_004.jpg
- [10:50] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_005.jpg
- [13:20] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_006.jpg
- [15:50] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_007.jpg
- [18:00] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_008.jpg
- [19:40] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_009.jpg
- [22:30] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_010.jpg
- [24:30] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_011.jpg
- [26:20] tutorials/frames/procedural-and-organic-modeling-in-houdini/frame_012.jpg

---

## Structured Notes

### Core Technique
Build an abstract organic hourglass/vase sculpture (crown-and-trunk form) from a masked sphere clipped into two rings, **Poly Bridge**d together with a thickness ramp, then roughened via VDB volume noise (masked by an "inside" vs. edge distance-along-geometry attribute for different density per region), refined with Smooth SDF + a Lattice-based pinch deformation, and finished with a bent-line-and-Sweep stem.

### Summary
A frequency-30 Sphere gets a top/bottom mask via a Point VOP computing the relative bounding-box Y component, mirrored (`abs(y - 0.5)`) and range-expanded, then distorted with a sparse-convolution 3D Turbulence noise on position. A rest-position + random attribute drives a **Clip** operation (comparing `v@P.y` to `@Cd.r`) to cut the sphere into a jagged ring boundary; the boundary is split into "above"/"below" groups, unshared edges converted to curves, resampled, and grouped into boundary-group pairs. **Poly Bridge** connects the two ring curves with high subdivision count and a customized **thickness ramp** (points moved to shape a pinched-waist profile), followed by a VEX snippet to remove leftover open-curve primitives, then a heavy **Attribute Blur** (~500 iterations, edge line mode) smooths the bridged shape while preserving its overall silhouette. Two attribute masks are built: a **distance-along-geometry** mask from the unshared/boundary points (inverted, offset) for edge-region control, and a separate uniform "inside" attribute (~1) covering the whole interior for a different noise density. Converting to VDB (density type, fill interior, thicker exterior band) and blending in a masked **Turbulence** noise (sparse convolution, tuned frequency/amplitude/offset) roughens the surface — reduced by multiplying with the mask so only intended regions get noise. A second, higher-frequency noise variant is duplicated and stretched (via a reused relative-bounding-box setup, `abs()` on tracked point components) then **mixed** with the first noise using a Fit-Ranged version of the edge mask as the mixing factor, blended so the stretched detail only shows in the middle rather than top/bottom. A **Smooth SDF** (one iteration, mean curvature flow) softens the sharp VDB transition before converting back to polygons; an **Attribute from Volume** re-imports the "inside" mask onto the polygon mesh. A **Lattice** deformer (driven by manually-edited points with a soft-radius move tool) creates a pinched indentation specifically at the top, tuned via Lattice's Kernel Function/Radius/Normalize Threshold parameters. Color variation uses the "inside" attribute (layered/blurred) to assign red (crown) vs. tan/beige (trunk) colors via Color nodes, usable later for material assignment. Finally, a stem/trunk-topper element is built from a short **Line** (0.15 length, 20 points) with normals reset, **Bent** toward the top, then given attribute-based orientation/Sweep (round tube profile, grid end cap, adjusted repeat/roundness), copied to a target point, and merged into the final sculpture.

### Key Steps
1. **Base sphere + top/bottom mask**: Sphere (frequency 30) → Point VOP computing relative bounding-box Y, subtract 0.5 and `abs()` to mirror, then Fit Range to expand the effect.
2. **Distortion**: connect position to a **Turbulence** noise set to sparse convolution / 3D noise (frequency 6, small amplitude ~0.11, offset tuned).
3. **Clip boundary**: create a rest-position attribute and a random attribute per point; use a wrangle comparing `v@P.y == @Cd.r`-style logic to build a clip test, then Clip the polygons around this jagged mask boundary.
4. **Split and curve extraction**: Split above/below the clip plane into two node streams; on one, keep bytes small for VDB feeding; group unshared edges, Convert Line, remove unused points, Connect Pieces (single primitive per curve), Resample, and group boundary points per curve (unshared, create boundary groups) — promoting to edges for the bridge input groups.
5. **Poly Bridge**: bridge group 0 to group 1, increase subdivisions (~60), and customize the **thickness ramp** by adding/moving ramp points to shape a pinched-waist profile.
6. **Cleanup**: remove leftover curve primitives with a VEX snippet checking if the primitive is closed (removes open curve primitives), then apply a heavy **Attribute Blur** (~500 iterations, edge-line mode) to smooth the bridged mesh while preserving the silhouette.
7. **Masks**: build a **distance-along-geometry** mask from the unshared/boundary point group (inverted, offset ~1), and a separate uniform **"inside"** attribute (~1) spanning the whole interior for differentiated noise density.
8. **VDB conversion**: VDB from Polygons (density type, fill interior, exterior band increased ~0.1); duplicate for the mask-driven density variant.
9. **Volume noise**: in a Volume VOP, add a **Turbulence** noise (position input, sparse convolution type, tuned frequency/amplitude/offset) to density, multiplied by the mask via Bind so the noise only affects intended regions.
10. **Stretched secondary noise**: duplicate the noise setup with a different frequency (~5), reuse the relative-bounding-box computation, track/`abs()` a point component, and **Mix** the two noises together using a Fit-Ranged version of the edge mask as the mixing factor — concentrating the stretched-noise look in the middle section only.
11. **Smooth SDF**: apply one iteration of mean curvature flow to soften the sharp VDB transition, then convert back to polygons.
12. **Attribute from Volume**: re-import the "inside" mask attribute from the volume onto the new polygon mesh.
13. **Lattice-based pinch**: Remesh lightly, build a **Lattice** deformer, manually edit specific lattice points (soft-radius move tool) to create a pinched indentation at the top (author leaves the bottom as a reader exercise), tuning Kernel Function/Radius/Normalize Threshold as needed.
14. **Coloring by region**: layer/blur the "inside" attribute, then use **Color** nodes keyed to point ranges (e.g. point 5-6 vs. others) to assign a red crown color and a tan/beige trunk color for later material targeting.
15. **Stem**: build a short **Line** (length ~0.15, 20 points), reset normals, **Bend** it toward the top of the shape, attribute-lathe the orientation, then **Sweep** (round profile, Grid end cap, adjusted repeat count and roundness), Copy to a target point, and merge into the final sculpture.

### Houdini Nodes / VEX / Settings
Sphere, Point VOP (relative bounding-box Y, mirror/`abs()`, Fit Range), Turbulence noise (sparse convolution, 3D, position-driven), rest position + random attribute, Clip (jagged boundary), Split, Group (unshared edges), Convert Line, Connect Pieces, Resample, Group (boundary groups), Poly Bridge (thickness ramp customization), VEX snippet (closed-primitive check for curve cleanup), Attribute Blur (edge-line mode, ~500 iterations), Distance Along Geometry mask, uniform "inside" attribute, VDB from Polygons (density, fill interior, exterior band), Volume VOP (Turbulence noise, Bind mask multiply, dual-noise Mix with Fit-Ranged mixing factor), Smooth SDF (mean curvature flow), Convert VDB to polygons, Attribute from Volume, Remesh, Lattice (manual point edits, soft-radius move, Kernel Function/Radius/Normalize Threshold), Color (point-range-keyed), Line, Bend, attribute lathe, Sweep (round profile, Grid end cap), Copy to Points, Merge.

### Difficulty
Advanced (combines VDB volume-noise masking, Poly Bridge with custom thickness ramps, and Lattice-based sculptural deformation into a single organic-modeling pipeline).

### Houdini Version
20.5.724 (visible in viewport title bar).

### Tags
vdb, poly-bridge, lattice, vex, volume-vop, organic-modeling, sculpture, karma

---

## Related Tutorials
- [VDB Procedural Modeling in Houdini](vdb-procedural-modeling-in-houdini.md) — related VDB volume-noise-based organic modeling technique from the same channel.
- [Procedural and organic modeling tips](procedural-modeling-with-vex-vdb-and-vellum.md) — shares overlapping VDB/VEX organic-shaping techniques.
