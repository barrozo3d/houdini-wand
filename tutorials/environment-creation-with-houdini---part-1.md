---
title: Environment Creation with Houdini - Part 1
source: YouTube
url: https://www.youtube.com/watch?v=nGKGXKw4_Zw
author: cgside
ingested: 2026-07-13
houdini_version: "19.5"
tags: [heightfield, terrain, procedural, scattering, vex, environment, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/environment-creation-with-houdini---part-1/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Environment Creation with Houdini - Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=nGKGXKw4_Zw)
**Author:** cgside
**Duration:** 11m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. So in this video we're going to create the basis for the image you see
[0:06] creating the terrain and do some initial scattering. It will be a good opportunity to learn not any basics
[0:14] from for loops to height fields and also some simple wax.
[0:21] Let's start by creating a night field changing the dimensions
[0:27] and apply some initial noise.
[0:33] Blaring a bit the result as we don't need detail for this part.
[0:38] We need to somehow divide the terrain, the back hills and the fields in front.
[0:44] So I'm creating a line positioning in the center
[0:48] and also copy the width of the height field and add a small value to it.
[1:00] I also want the back hills to be around 40% of the entire terrain so let's copy the depth of the
[1:07] height field and position the line 10% from the center. Adding a point cheater to proceed
[1:14] really shape the line and only displacing along the Z axis.
[1:23] When you're happy with the shape add a re-sample mostly to smooth out the curve with the subdivision curves option.
[1:35] Now let's create a mesh from this curve by doing a few explosions and mirroring the results at the end.
[1:42] We will use these to mask the height field but also to cut the geometry later.
[1:51] Load the mesh we just created in an object merge and do a mask by object.
[1:58] Now we have a mask to separate the different sections of the terrain.
[2:03] Add a night field noise and play it with the attributes we want to create some small mountains in the back.
[2:12] You will also need to blur the mask with the transition.
[2:23] After blurring a bit the result we can start to play with some erosion.
[2:28] I am not changing much only the overall amount.
[2:36] I also want to distort a bit the result with a low frequency.
[2:41] Here I am just going back as I am not yet happy with the result mostly changing the seat of the offset of the noise.
[2:58] Let's now create a path on our terrain by using a more traditional way drawing a curve.
[3:04] Re-sample the curve to smooth out the points.
[3:12] And let's project it on our terrain with a ray and create a mesh with a sweep.
[3:22] Now we can create a mask from the path.
[3:25] Having the mask we can carve the road on the terrain by using a night field project.
[3:35] We will need a negative transform in the way to carve the path and also play with the combined methods of the projection.
[3:46] Let's save this mask to a layer using the copy layer node.
[3:51] We will also need a mask for the sides of the road to scatter some trees around.
[3:57] So let's expand the road mask and subtract the original mask from it.
[4:07] We need also to save it to a new layer to use later.
[4:13] As the transition is a bit harsh between the road and the terrain let's manipulate a bit the
[4:18] mask's two-blur that transition.
[4:29] And finally we can cover the eye field to a mesh.
[4:46] Let's move on by creating a bullion between the back shape and the terrain.
[4:59] In the next step we will use a Voronoi fracture to divide the front part into fields.
[5:05] So start by scattering a few points for the fracture.
[5:09] We want to disable creating the rear surfaces in the Voronoi and now we have the base for our fields.
[5:24] Around the different patches I want to scatter some bushes so let's group the unshared edges and convert them into curves.
[5:32] We will need to fuse the points and then create a mesh from it.
[5:42] But as you can see we have double geometry so let's go back and fuse the unshared edges group we created.
[5:55] Okay now I want to mask this sweep mesh on the terrain but let's make sure we
[6:01] re-project the mesh as by now it's flat.
[6:07] Alright moving to the last part of this long tutorial I want to divide the pieces from the Voronoi into
[6:14] different groups so I can scatter different meshes later. Let's pack the geometry with the
[6:21] assemble nodes. Now we will need a bit of wax to create a random index of the packed frames.
[6:28] Carty of Leninmost Prime user on reddit. Basically we're creating a natu-boot with some controls
[6:36] for the number of groups we want and also the seed value. Let's group by attribute to visualize what we've done.
[6:52] Now we can use a name to transform the groups into an attribute.
[6:56] I'm realizing now that maybe I don't need these much steps but it was the way that it was working for me.
[7:04] Let me know in the comments how would you have done it. Promoting the point attribute to primitive
[7:11] so we can use it in the next step. Now we will use a for loop to scatter different meshes into
[7:18] the tree groups of fields we created before. We want to change the method to extract this
[7:25] our points. Make sure you set the name attribute in the loop and node, piece attribute.
[7:35] I made a small mistake before the loop but we will fix it in a bit. For now let's unpack the
[7:42] geometry and combine the road masks so we can feed it to the density attribute on the scatter.
[7:49] We will also need a metadata node to use it the iteration or index of the loop.
[7:56] And before correcting the small mistake I made let's invert the mask as we want to scatter outside
[8:03] the road. The missing part here is in the name attribute. We need to set the class to point and
[8:12] not primitives. Let's create the tree scatters for the tree groups we have and use the mask we
[8:23] just combined as density. Now we need a way to select the different scatter node at each iteration.
[8:31] So using a switch node feeding it the iteration attribute should do the trick.
[8:37] And we can use a copy to points and place different objects at each group of patches.
[8:46] Let's reuse this switch node and place a few different colorate boxes for now.
[8:51] Finally let's combine the result with the original terrain and we are done with the fields.
[9:08] The only thing left to do is to scatter some bushes around the patches and trees on the roadside.
[9:16] So let's start with the curves we had before and split it with a polypads. I am doing this
[9:23] because I want to remove some of the back lines. Creating a shape from it and scattering a few points
[9:31] making sure we remove the ones on the roads.
[9:34] Lastly, with a copy to point we can insert a few boxes for now.
[9:49] The only thing left to do is to distribute some trees on the sides of the road.
[10:04] Create a cylinder and place it on the grid with the H-Gripped code Y-min.
[10:10] Scatter a few points on the roadside and use a copy to point to instance the tube.
[10:24] Let's just make the trees face up by setting the normal attribute.
[10:30] And the very last step is to rotate the tube so it sits up.
[10:35] And that's everything I wanted to share with you for now. Hopefully you learned something new.
[10:42] I certainly did doing this small project. And the next step is to take everything we've done
[10:48] to Salaris context and do some shading, lighting and rendering. Let me know if you would be
[10:55] interested in that. Thank you and see you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/environment-creation-with-houdini---part-1/frame_000.jpg
- [1:45] tutorials/frames/environment-creation-with-houdini---part-1/frame_001.jpg
- [3:15] tutorials/frames/environment-creation-with-houdini---part-1/frame_002.jpg
- [5:10] tutorials/frames/environment-creation-with-houdini---part-1/frame_003.jpg
- [7:20] tutorials/frames/environment-creation-with-houdini---part-1/frame_004.jpg
- [10:10] tutorials/frames/environment-creation-with-houdini---part-1/frame_005.jpg

---

## Structured Notes

### Core Technique
Building a stylized terrain environment (back hills, foreground fields, a carved road, and initial scattering of trees/bushes) using Heightfields, curve-driven masking, Voronoi Fracture for field patches, and a for-loop-based multi-group scatter system.

### Summary
Starts with a base **Heightfield** (custom dimensions, initial noise, blurred since fine detail isn't needed yet), then divides the terrain into "back hills" vs. "front fields" using a hand-shaped curve: a centered line sized to the heightfield's width, point-jittered and displaced along Z only, then resampled with the "subdivision curves" smoothing option. That curve is poly-extruded into a mesh (mirrored) and object-merged back in as a **Heightfield Mask by Object** to separate terrain sections; a second Heightfield Noise (masked, then blurred at the transition) adds small mountains to just the back-hill region, refined with light **Erosion** and a low-frequency distortion noise (mostly tuned by adjusting the noise's seed/offset). A road is added the traditional way — hand-drawn curve, resampled, **Ray**-projected onto the terrain, and Swept into a mesh — then converted into a heightfield mask and carved into the terrain via **Heightfield Project** with a negative transform (tuning the combine method); the mask is saved to a new layer via Copy Layer, and a second "roadside" mask is derived by expanding the road mask and subtracting the original road mask (for future tree/bush scattering along the road edges), blurred slightly to soften the road/terrain transition. The heightfield is converted to a mesh, Booleaned against the back-hills shape, and the front region is subdivided into field "patches" via **Voronoi Fracture** (rear surfaces disabled) seeded by scattered points; the unshared edges of the resulting patches are grouped, converted to curves, fused, and swept into hedge/border geometry (careful to re-fuse the unshared-edges group to avoid doubled geometry), then re-projected onto the (no longer flat) terrain. Patches are packed (Assemble) and assigned to N random groups via a small VEX wrangle (credited to a Reddit user, "Cartof Leninmost Prime") that generates a controllable count of random group indices from a seed, visualized with Group by Attribute and converted to a `name` attribute (promoted point→primitive). A **For Loop** (by count) then iterates per field-group: unpacks geometry, combines with the (inverted) road mask as scatter density, uses a Metadata node to read the loop iteration for a Switch selecting between per-group Scatter nodes, and Copy-to-Points instances placeholder colored boxes (later real tree/bush assets) per patch group — the loop's `name` attribute class needed correcting from primitive to point partway through. The whole field result is combined back with the original terrain. Final scattering adds patch-border bushes (from the earlier polypatch/curve split, scattered with roadside points removed and instanced via Copy to Points) and roadside trees (a simple cylinder placed via Copy to Points onto scattered roadside points, oriented upright by setting the normal attribute and a final corrective rotation).

### Key Steps
1. **Base terrain:** create a **Heightfield** with custom dimensions, apply initial noise, and Blur it (fine detail not needed at this stage).
2. **Back-hills/front-fields divider curve:** build a centered Line sized to the heightfield's width (plus a small margin), position it ~10% from center at ~40% of the heightfield's depth (for the back-hills proportion); apply a **Point Jitter**, displace along Z only for hand-tuned shape, then Resample with "subdivision curves" to smooth it.
3. **Mask mesh from curve:** Poly Extrude the shaped curve into a mesh, mirror it, then Object Merge it back in and use **Heightfield Mask by Object** to separate the terrain into distinct back/front sections.
4. **Back-hills detail:** add a second **Heightfield Noise** masked to the back-hill section (tuned for small mountains), blur the mask at the transition edge, apply light **Erosion** (overall amount only), and a low-frequency distortion noise (mostly adjusted via seed/offset until visually satisfying).
5. **Road path:** hand-draw a curve for the road, Resample to smooth, **Ray** it onto the terrain surface to conform, then **Sweep** into 3D road geometry.
6. **Carve the road:** convert the road mesh into a heightfield mask, then use **Heightfield Project** with a negative transform and a tuned combine method to carve/indent the road into the terrain; save the mask via **Copy Layer** for reuse.
7. **Roadside mask:** expand the road mask and subtract the original (un-expanded) road mask from it to isolate a roadside band for future scattering; save to a new layer and blur slightly to soften the harsh road/terrain transition.
8. **Terrain to mesh + Boolean:** convert the finished heightfield to a polygon mesh, then Boolean it against the back-hills shape to cleanly separate front and back geometry.
9. **Field patches via Voronoi Fracture:** scatter seed points across the front terrain area, run **Voronoi Fracture** (disable "create rear surfaces") to divide it into field-like patches.
10. **Patch-border hedges:** group the unshared edges of the patches, convert to curves, **Fuse** the points (re-fuse the same unshared-edges group a second time to eliminate doubled geometry from the first fuse pass), build a mesh/sweep from the curves, then re-project the (now-flat) sweep mesh back onto the actual terrain surface.
11. **Random group assignment via VEX:** Pack (Assemble) the Voronoi patches, then run a wrangle (community-credited technique) that generates a random group index per packed piece from a seed and a target group count; visualize with **Group by Attribute**, convert the group to a `name` attribute, and promote point→primitive so it can drive a For Loop.
12. **For-loop multi-group scatter:** iterate (**For Loop**, by count) over the field groups — unpack geometry, combine with the inverted road mask as scatter density, read the loop iteration via a **Metadata** node to drive a **Switch** selecting the correct per-group Scatter node, then **Copy to Points** placeholder colored boxes onto each group's scattered points (note: the `name` attribute's class needed correcting from primitive to point mid-loop for the density/scatter step to work).
13. **Combine and finish fields:** merge the for-loop's per-group scattered result back with the original terrain.
14. **Border bushes:** split the earlier patch-border curves with **Poly Path** to remove unwanted back-facing segments, build a shape, scatter a few points (excluding roadside points), and Copy to Points placeholder boxes.
15. **Roadside trees:** build a simple cylinder ("H-grid" style placement, Y-min anchored), scatter points along the roadside band, Copy to Points to instance the cylinder per point, orient upright by setting the point normal attribute, and apply a final corrective rotation so trees actually stand upright.

### Houdini Nodes / VEX / Settings
Nodes: Heightfield (dimensions, initial noise, Blur), Line, Point Jitter, Resample (subdivision curves), Poly Extrude, Mirror, Object Merge, Heightfield Mask by Object, Heightfield Noise (masked), Erosion (Heightfield), low-frequency distortion noise, Ray (project onto terrain), Sweep, Heightfield Project (negative transform, combine method), Copy Layer (Heightfield), Group (unshared edges), Convert Line, Fuse (applied twice to fix doubled geometry), Boolean, Voronoi Fracture (rear surfaces disabled, seed scatter), Assemble (pack), Attribute Wrangle (VEX — random group-index generation from seed + group count, community-credited "Cartof Leninmost Prime" technique), Group by Attribute, Name (group→attribute), Attribute Promote (point→primitive), For Loop (by count), Metadata (loop iteration/index), Switch (iteration-driven node selection), Scatter (multiple, per-group density from combined/inverted road mask), Copy to Points, Poly Path (curve splitting), Cylinder (H-grid placement, Y-min).

### Difficulty
Intermediate — heightfield/Voronoi/for-loop fundamentals are approachable, but the group-randomization VEX wrangle and for-loop metadata-driven switch selection require comfort with attribute classes and loop iteration.

### Houdini Version
Not explicitly stated; UI style is consistent with Houdini 19.5-era heightfield/Voronoi Fracture tools (pre-20 node icon set).

### Tags
#heightfield #terrain #procedural #scattering #vex #environment #intermediate

---

## Related Tutorials
Followed directly by environment-creation-with-solaris-in-houdini.md (same author, same terrain/fields project — Part 2 covers Solaris shading, lighting, and instanced scattering). Also cross-link with other cgside environment/scattering tutorials once extracted from this batch.
