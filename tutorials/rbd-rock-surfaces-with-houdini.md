---
title: RBD rock surfaces with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=015fds0mdyk
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.598"
tags: [rbd, material-fracture, vdb, vex, packed-primitives, triplanar, karma, environment, rocks]
extraction_status: complete
frames_dir: tutorials/frames/rbd-rock-surfaces-with-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# RBD rock surfaces with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=015fds0mdyk)
**Author:** cgside
**Duration:** 4m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. In this video we're going to have a look on how to quickly create some rock like surfaces
[0:07] using the RBD fracture along with some tips.
[0:11] So I start with the box and Boolean out to other one to create an initial shape.
[0:17] Place the mesh in the grid. And in this group expression I am using some simple code to select the
[0:24] slope area without the back face. Using the normal white to select all the primitives below 0.1,
[0:33] next I am removing the bottom faces and finally the back face using the Z component of the normal.
[0:41] Remashing the shape, now expanding the slope group, transforming it in a natubert mask.
[0:50] And using an attribute blur so it's not so harsh when we use it in the next step.
[0:57] In the mountain node I am disabling the Y axis and also blending the mask attribute so it doesn't
[1:04] affect the back of the shape as I want it flat. So to fit the RBD material fracture I am flattening
[1:13] the shape so we can stretch them at the end. I am also feeding my own points to the node using a scatter
[1:21] saw. And after the fracture I am restoring the transform with a match size since I exported the
[1:28] X form from the transform node. As you can see we have the longer shapes that we can remove from
[1:35] the sides and create an interesting rock surface. In the fracture node I just played with the edge
[1:42] detail and noise to add some more variation. Then I am assembling it into packed prims so I can
[1:50] manipulate the pieces as single points. And using some geometry to group the side pieces.
[1:58] As for that bounding Giu I am using the slope group and manipulating the point normals,
[2:04] flattening the Y axis and blurring a bit the normal attribute so I can use it in the
[2:10] X-Rude node otherwise it will extrude all over the place. You can have a look at the file from
[2:17] my Patreon and see in detail what I am doing. And finally I am blasting the selected pieces within
[2:24] the group. Now you can play with the scatter see then find a good looking shape. And packing
[2:31] fusing the points and using a VDB from polygons just to rematch the shape and get rid of the
[2:37] different internal pieces. Creating a slope mask so I can use it inside the volume knob.
[2:45] And in the VOP I have these three simple whirling noises with some distortion, mostly
[2:51] manipulating the frequency of each component to stretch or flatten the noise.
[2:58] I am also multiplying all the noises with the slope masks so we get no distortion on the top part.
[3:04] More of the same would that I have been sharing on the channel and Patreon tutorials.
[3:14] Then calculating the ambient occlusion and curvature so we can use it for texturing.
[3:20] And in this point VOP creating a mask for the top parts using the normal Y and also some sort of
[3:28] wet map for the bottom part using the bounding box. But feeding a noise to the position so we can
[3:37] get some distortion going. And then caching a few variations. As for the texturing using the
[3:48] same workflow as the last video, taking advantage of the generated masks along with some color
[3:54] correction to create some variation along the textures. Again using the material XCGS
[4:01] stripe planner to avoid repetition and better normal mapping and displacement.
[4:07] And that's about it. Hopefully you learned something new. I surely did.
[4:13] And if you want to support the channel and get access to the project files and exclusive
[4:18] tutorials, check out my Patreon. Thank you and see you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_000.jpg
- [0:55] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_001.jpg
- [1:30] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_002.jpg
- [2:10] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_003.jpg
- [2:55] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_004.jpg
- [3:40] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_005.jpg
- [4:20] tutorials/frames/rbd-rock-surfaces-with-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
Quickly generate rock-like cliff surfaces using **RBD Material Fracture** as a modeling tool (not simulation): a masked/flattened box is fractured with custom scattered seed points, then packed pieces are selectively removed via slope-masked normal-driven Extrude, VDB-remeshed, and detailed with three whirling noises masked by slope so tops stay undistorted.

### Summary
A Boolean'd box has its slope faces (excluding back/bottom) selected via a group expression testing normal Y below a threshold and normal Z, then remeshed and expanded into a natural-mask-driven Mountain distortion (with the Y axis disabled and the mask blended so the flat back face is untouched). The shape is flattened before fracturing (to allow stretching afterward) and fed **custom scatter points** into RBD Material Fracture instead of relying on its default point distribution, with edge detail/noise parameters tuned for variation; a Match Size restores the original proportions using a saved transform. Pieces are assembled as **packed primitives** so they can be manipulated as single points; a geometry group targets side pieces using the slope group with flattened/blurred point normals (to avoid over-extruding), letting the "long shapes" be removed from the sides for an interesting rock-face silhouette via Blast within the group. After fusing points, a VDB from Polygons remesh cleans up internal fracture pieces, and a slope mask feeds three **whirling/turbulent noises** inside a Volume VOP — each distorted by tweaking frequency components to stretch or flatten differently — all multiplied by the slope mask so the flat top receives no distortion. Ambient occlusion and curvature are calculated for texturing, along with a top-surface mask (normal Y) and a bottom "wet map" mask (bounding-box-based, noise-distorted position) — several cached variations are generated by varying the scatter seed. Texturing reuses the studio's established slope/AO/curvature-driven color-correction workflow with a MaterialX CGS Triplanar node for repetition-free normal mapping and displacement.

### Key Steps
1. Start with a Box, Boolean out another to create the initial rough shape; place the mesh on a grid.
2. Select the **slope area excluding back/bottom faces** via a group expression: normal Y below 0.1 for slope, then remove bottom faces and the back face using the normal Z component.
3. Remesh the shape, expand the slope group, transform it into a natural-would mask, and blur the mask via Attribute Blur so the effect isn't too harsh.
4. In a **Mountain** node, disable the Y axis and blend in the mask so the back of the shape stays flat/unaffected.
5. **Flatten the shape** before fracturing (to fit RBD Material Fracture and allow stretching afterward); feed **custom scatter points** into the fracture node instead of its default distribution.
6. After fracturing, **restore the original transform** using Match Size (the transform having been exported from the earlier flattening step).
7. Tune the Fracture node's edge detail and noise parameters for surface variation, and remove long/thin shapes from the sides for a more interesting rock-face profile.
8. **Assemble into packed primitives** so pieces can be manipulated as single points; use a geometry group (the earlier slope group) with flattened, blurred point normals to select side pieces without over-extruding.
9. **Blast** the selected side-piece group to remove unwanted geometry, revealing the desired rock surface.
10. Play with the fracture's scatter seed to find a good-looking shape, then pack and fuse points; run **VDB from Polygons** to remesh and eliminate leftover internal fracture pieces.
11. Create a slope mask for use inside the **Volume VOP**: three simple whirling/turbulent noises, each with distortion, mostly tuned by adjusting each noise component's frequency to stretch or flatten the effect — multiplied by the slope mask so the flat top has no distortion.
12. Calculate **Ambient Occlusion** and **curvature** for later texturing use.
13. In a Point VOP, create a top-surface mask using normal Y, and a bottom "wet map" mask using a bounding-box-based measurement with a noise fed into position for distortion; cache several variations by varying the scatter seed.
14. Texture using the studio's established workflow (as covered in prior videos): the generated masks drive color correction/variation, and a **MaterialX CGS Triplanar** node (custom, from the same author) avoids repetition and improves normal mapping/displacement.

### Houdini Nodes / VEX / Settings
Box, Boolean, group expression (`@N.y < 0.1`, `@N.z`-based slope/back/bottom selection), Remesh, Group Expand, natural-would mask, Attribute Blur, Mountain (axis-disabled, mask-blended), Transform (flatten before fracture, export for restore), custom Scatter (seed points fed to fracture), **RBD Material Fracture** (edge detail, noise), Match Size (transform restore), Pack, geometry group (flattened/blurred point normals), Blast (side-piece removal), Fuse, VDB from Polygons (remesh cleanup), Volume VOP (three whirling/turbulent noises, frequency-tuned stretch/flatten, slope-masked multiply), Ambient Occlusion, Curvature/measure-curvature, Point VOP (top mask via normal Y, bottom wet-map via bounding-box + noise-distorted position), MaterialX CGS Triplanar (custom node).

### Difficulty
Advanced (using RBD Material Fracture purely as a modeling tool, combined with packed-primitive piece selection and multi-noise VDB detailing, assumes strong procedural fluency).

### Houdini Version
19.5.598 (visible in viewport title bar).

### Tags
rbd, material-fracture, vdb, vex, packed-primitives, triplanar, karma, environment, rocks

---

## Related Tutorials
- [Procedural Rock Wall without intersections](procedural-rock-wall-without-intersections.md) — another example of using RBD as a modeling tool (compression via a shrinking Bound) rather than pure simulation.
- [VDB Procedural Cliffs](vdb-procedural-cliffs.md) — shares the layered-noise-in-Volume-VOP detailing technique used here for the rock surface.
- [Houdini Beginner Tutorial - Creating a Perfume Bottle](houdini-beginner-tutorial-creating-a-perfume-bottle.md) — shares this author's use of RBD Material Fracture as a shape-generation tool rather than a destruction sim.
