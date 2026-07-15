---
title: Procedural techniques in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=PcP9Eieij1g
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.734"
tags: [flip, vex, vdb, distance-along-geometry, materialx, karma, food, density-by-attribute]
extraction_status: complete
frames_dir: tutorials/frames/procedural-techniques-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural techniques in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=PcP9Eieij1g)
**Author:** cgside
**Duration:** 2m40s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi there and welcome. In this video I'll show you how I combine different procedural techniques
[0:05] in Odini to create this final image. The full project can be found on the link in the
[0:11] description. So as you can see the caramel on this cookie ice cream has some layers across


### Density by attribute [0:12]
**Transcript (timestamped):**
[0:17] the Y-axis. Let's see how that can be achieved within a flip sim. So for that effect I'm creating
[0:24] a density attribute by dividing my flip source into sections using the bounds of the point
[0:30] cloud. Also adding some noise to give it some variation and lurping between the sections
[0:37] and another noise on the bottom. Finally, remap the density values to fit the flip
[0:43] sim and make sure you enable density by attribute in your flip solver. Now let's see how to


### Cookie undulating effect with vex [0:49]
**Transcript (timestamped):**
[0:50] create this only lighting effect on the cookie borders. Basically I'm using the sin function
[0:56] along the curve view, making sure it's absolute to get only positive values. To ensure we get
[1:05] consistent sizes along the curves I am also multiplying by the length of the curve and finally
[1:11] this place the position along the normal with those values. To create the burn defect on the


### Distance along geometry [1:16]
**Transcript (timestamped):**
[1:17] edges of the cookie I am saving the unshared points before the bullion, then group again the
[1:23] unshared points and group combine them to separate the holes from the border. And in the end
[1:29] just create a attribute mask with the distance along geometry for both groups. The drops were


### Adding droplets with vdb's [1:36]
**Transcript (timestamped):**
[1:37] created after the seam and for that I am manually selecting a few points and copying a curve
[1:43] to it with a random b scale. Then just sweeping it playing with the scale along curve and setting
[1:49] the end caps to grid. Create a VDB for both meshes and combine them. And finally we can
[1:56] blur the transition using a smooth SDF with a mask coming from the second input.
[2:01] So the materials on this scene are quite simple. For the cookie I am using the save


### Cookie material in karma [2:03]
**Transcript (timestamped):**
[2:08] that reboots to drive the colors. Using the material X mix node with the masks as a mix factor
[2:15] to blend different colors. Then just use a random noise detection as band map. So that's what I


### Outro [2:24]
**Transcript (timestamped):**
[2:25] have for you today. I hope you got something out of this and make sure to check out my Patreon
[2:31] where you can download this full scene and many more. Thank you and see you next time.



---

## Captured Frames

- [0:10] tutorials/frames/procedural-techniques-in-houdini/frame_000.jpg
- [0:25] tutorials/frames/procedural-techniques-in-houdini/frame_001.jpg
- [0:55] tutorials/frames/procedural-techniques-in-houdini/frame_002.jpg
- [1:20] tutorials/frames/procedural-techniques-in-houdini/frame_003.jpg
- [1:40] tutorials/frames/procedural-techniques-in-houdini/frame_004.jpg
- [2:10] tutorials/frames/procedural-techniques-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
Four combined procedural tricks for a "D"-shaped caramel-covered cookie ice cream: a **density-by-attribute FLIP source** that sections the sim volume by Y-bounds for layered caramel-flow behavior, a `sin(curveu)`-driven VEX undulation for the melty cookie-border look, `distance along geometry` masks (built from Boolean-seam groups) for edge-targeted effects, and VDB-combined swept-curve droplets blurred in with Smooth SDF.

### Summary
To get caramel that flows in visible horizontal layers rather than uniformly, a density attribute is authored on the FLIP source points by dividing the point cloud into sections using its own bounding box, blending in noise per-section plus a separate noise at the bottom via `lerp()`, remapping the result to fit the solver's expected density range, and enabling **Density by Attribute** in the FLIP solver so those authored values actually drive local fluid density/behavior. The undulating "melty" look on the cookie border uses `sin()` along the curve-view (`curveu`) attribute, taking the **absolute value** to keep displacement positive-only, multiplied by curve length for consistent bump sizing regardless of curve length, then displacing position along the normal by that value. For edge-targeted effects (e.g. burn/darkening near cutouts), unshared points are saved *before* the Boolean operation, regrouped afterward, and **Group Combine**d to separate holes from the outer border, with an **Attribute Distance Along Geometry** mask built for each group to drive downstream shading/effects with proper falloff from each edge type. Caramel droplets are added after the Boolean seam is formed: a few points are manually selected and a curve is copied to each with randomized p-scale, then Swept with scale-along-curve tuning and Grid end caps; both the main cookie mesh and the droplet meshes are converted to VDB and **VDB Combined**, with a **Smooth SDF** using a mask from the second input to blur the seam transition so droplets blend seamlessly into the surface rather than looking pasted-on. Shading is comparatively simple: for the cookie, the saved distance-along-geometry attribute drives a MaterialX **Mix** node as the mix factor between different colors, plus a random-noise-driven bump map for surface variation.

### Key Steps
1. **Density by attribute FLIP setup**: on the FLIP source points, create a density attribute by dividing the point cloud into sections using its own bounding box; add noise per section and blend with `lerp()`, plus a separate noise specifically for the bottom section.
2. **Remap** the resulting density values to the range the FLIP solver expects, and enable **Density by Attribute** in the FLIP solver so the authored per-point density actually influences the simulation's local behavior — producing visible horizontal caramel layers.
3. **Undulating cookie-border effect**: use `sin()` on the `curveu` (curve-view) attribute, wrapped in `abs()` to keep only positive displacement values.
4. Multiply the sine result by the **curve's length** so bump size stays visually consistent regardless of how long the curve segment is, then displace position **along the normal** by that final value.
5. **Distance-along-geometry masks for edge effects**: before running the Boolean operation that cuts the cookie's holes, save the **unshared points** group; after the Boolean, regroup unshared points again and use **Group Combine** to separate the hole edges from the outer border edges.
6. Build an **Attribute (Distance Along Geometry)** mask for each of the two groups (holes vs. border), giving downstream shading/effects proper falloff distinguishing edge type.
7. **VDB droplets**: after the Boolean seam exists, manually select a handful of points and Copy a curve to each with a randomized p-scale.
8. **Sweep** each curve with scale-along-curve tuning and **Grid** end caps to form drip/droplet shapes.
9. Convert both the main cookie mesh and the droplet meshes to **VDB**, then **VDB Combine** them together.
10. Use a **Smooth SDF** node with a mask sourced from the second input to blur the transition seam, so the droplets blend smoothly into the cookie surface instead of looking like pasted-on geometry.
11. **Shading**: use the saved distance-along-geometry attribute as the mix factor in a MaterialX **Mix** node to blend different colors across the cookie surface, plus a random-noise-driven bump map for surface micro-detail.

### Houdini Nodes / VEX / Settings
FLIP source (density attribute authoring via bounding-box sectioning, noise, `lerp()`), Remap, FLIP Solver (Density by Attribute enabled), VEX `sin()`/`abs()` on `curveu`, curve-length multiplication, position-along-normal displacement, Boolean (with pre/post unshared-point group saving), Group Combine (hole vs. border separation), Attribute — Distance Along Geometry (per-group masks), manual point selection + Copy (randomized p-scale curves), Sweep (scale-along-curve, Grid end caps), VDB from Polygons, VDB Combine, Smooth SDF (second-input mask blending), MaterialX Mix (distance-mask-driven color blend), random-noise bump map.

### Difficulty
Advanced (density-by-attribute FLIP control and VDB-combined seam-blurred droplets are both non-trivial, production-level techniques).

### Houdini Version
20.5.734 (visible in viewport title bar).

### Tags
flip, vex, vdb, distance-along-geometry, materialx, karma, food, density-by-attribute

---

## Related Tutorials
- [Procedural Food in Houdini - Mardini 2026](procedural-food-in-houdini-mardini-2026.md) — likely related food-modeling/shading techniques from the same channel.
- [How to not Bake Brownies in Houdini](how-to-not-bake-brownies-in-houdini.md) — shares VDB-based food-detail techniques from the same channel.
