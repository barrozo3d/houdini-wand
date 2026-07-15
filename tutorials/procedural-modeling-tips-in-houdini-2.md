---
title: Procedural Modeling tips in houdini #2
source: YouTube
url: https://www.youtube.com/watch?v=Kc_6yws1AH8
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.569"
tags: [extrude, uvs, material-fracture, vex, for-each-loop, displacement, architecture, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-modeling-tips-in-houdini-2/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Modeling tips in houdini #2

**Source:** [YouTube](https://www.youtube.com/watch?v=Kc_6yws1AH8)
**Author:** cgside
**Duration:** 4m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. In this video I am going to be sharing a few tips on procedural modeling.
[0:07] So the first one is on how to control the extrusion shape.
[0:11] If for example you need to create a tapering effect like you see in these shapes.
[0:17] I'm starting with this shape with the normal pointing inward.
[0:21] And now with some basic facts I can manipulate the normals with ramp based on the curve view.
[0:29] And on the extrude node you can set the mode to point normal and make sure you use the existing
[0:35] normals. Then you can play with the ramp shape to get the desired result.
[0:42] Now in this example I wanted to create some horizontal tiles divided into vertical sections while
[0:48] maintaining the initial shape of the cylinder. So starting with the tube and creating some UVs with
[0:55] flattened UV nodes. And here I am flattening the cylinder using the UV attribute and mapping it to
[1:04] the position. Now as I said before I need to create horizontal randomly sized tiles.
[1:11] So for now I am going to get rid of the vertical subdivisions and create the horizontal ones.
[1:18] Basically using the fit function and the bounding box by components.
[1:23] If you want you can grab the scene files from my Patreon where you can find dozens of project files
[1:30] from my videos and hours of exclusive tutorials. And for the tiles I am using the lots of
[1:37] division nodes which is the perfect node for this setup. That takes into consideration the initial
[1:44] topology. That's why I just had the horizontal subdivisions. Then I am adding back the vertical
[1:52] subdivisions so I can deform it back to the initial cylindrical shape.
[1:59] As you can see we kept the initial shape adding the desired tiles.
[2:06] Still on the tiles I wanted to break some of them along the ends of the shape.
[2:11] So after the material fracture I am assembling the pieces. Then I need to select the ends so
[2:17] for that I am using a group expression with a following vex snippet. Testing if the
[2:24] exposition of the points is bigger than the bounding box mean plus the size of the bounding box
[2:30] x multiplied by the percentage you want to keep. You can play with the value to select more or less
[2:37] pieces. Now for the last one I created this dome with the loop and
[2:47] some displacement. Started with a tube and did some extrusion inside the loop.
[2:55] Make sure you set the loop to fetch feedback if you are doing modeling operations like this.
[3:02] So in order to create this spherical effect you will need some basic math.
[3:07] In this case the power function will work just fine and playing with the value still you have
[3:12] the desired shape. We will need UVs for the displacement so in order to keep a consistent pattern
[3:19] I am creating seams across each level and flattening the islands into rectangular shapes.
[3:26] So we have the UVs correctly oriented for the dome. Finally in a point warp importing some
[3:33] displacement textures and mixing them with a composite node set to overlay and use the
[3:40] display cell on normal's warp. So that's basically it. I hope you have learned something new
[3:45] and feel free to grab the example files from my Patreon and huge thanks for everyone that
[3:50] already is supporting me over there. So yeah thank you and see you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_000.jpg
- [0:45] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_001.jpg
- [1:15] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_002.jpg
- [1:50] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_003.jpg
- [2:25] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_004.jpg
- [2:55] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_005.jpg
- [3:40] tutorials/frames/procedural-modeling-tips-in-houdini-2/frame_006.jpg

---

## Structured Notes

### Core Technique
Three architectural modeling tips applied to a cathedral tower: ramp-controlled extrusion tapering via point-normal mode, topology-preserving horizontal tiling via UV-flattened Divide, and end-piece selection via a bounding-box-percentage VEX group expression — plus a power-function dome silhouette with seam-aware UV flattening for displacement.

### Summary
A tapering extrusion effect is achieved by manipulating point normals with a ramp based on curve-view position, then setting Extrude to **Point Normal** mode with "use existing normals" enabled — the ramp shape directly controls the taper profile. For horizontal tile rows on a cylinder that must respect the original topology, UV Flatten unwraps the cylinder and maps UV back to position, strips the vertical subdivisions (keeping only horizontal), and uses **Lots of Division** (the ideal node for this since it respects incoming topology) to create horizontal tiles before re-adding vertical subdivisions to deform the tiled sheet back into the cylindrical shape. To selectively break some tiles at the shape's ends after a Material Fracture, packed pieces are assembled and a **group expression VEX snippet** tests whether a point's X position exceeds `bbox_mean + bbox_size_x * percentage` to select end pieces procedurally, with the percentage value tunable to include more or fewer pieces. Separately, a domed roof shape is built inside a **Fetch Feedback for-loop** with extrusions per iteration, using a simple **power function** for the spherical falloff profile; UV seams are placed across each level and islands flattened into rectangles for a consistent tiling pattern, then a Point VOP imports displacement textures, mixes them via a Composite node set to Overlay, and applies the result along normals via Displace Along Normals.

### Key Steps
1. **Tapering extrusion**: start with a shape whose normals point inward; use VEX/point-normal manipulation with a **ramp keyed to curve-view (curveu) position** to shape the taper; set Extrude to **Point Normal mode** with "use existing normals" enabled; adjust the ramp shape to dial in the desired taper profile.
2. **Topology-preserving horizontal tiles**: start with a tube, create UVs via **UV Flatten**, then flatten the cylinder by mapping the UV attribute onto position.
3. Strip vertical subdivisions (keeping only what's needed for horizontal tiling), then use **Lots of Division** — the ideal node for this since it respects the incoming topology instead of arbitrary re-tessellation — to generate horizontal, randomly-sized tiles.
4. Add back the vertical subdivisions and deform the flattened tile sheet back into the original cylindrical shape, preserving the tile pattern.
5. **Selective end-piece breaking**: after a Material Fracture, assemble the pieces (packed); select the end pieces via a **group expression** using a VEX snippet testing whether a point's X position is greater than `bounding_box_mean + bounding_box_size_x * percentage` — tune the percentage to select more or fewer pieces from the ends.
6. **Domed roof profile**: build inside a **for-loop set to Fetch Feedback** (required for chained modeling operations like this), starting from a tube and extruding inward each iteration.
7. Shape the spherical falloff using a simple **power function** applied to the loop's scale/position values — tune the exponent for the desired dome curvature.
8. **UV consistency for displacement**: create seams across each dome level and flatten each island into a rectangular shape, ensuring a consistent, non-distorted tiling pattern across the whole dome.
9. In a **Point VOP**, import displacement textures, mix multiple textures using a **Composite node set to Overlay**, and apply the result via **Displace Along Normals** using the imported displacement as the input.

### Houdini Nodes / VEX / Settings
Attribute Wrangle/VOP (ramp keyed to curveu, point-normal manipulation), Extrude (Point Normal mode, "use existing normals"), UV Flatten, position-from-UV mapping, Lots of Division (topology-respecting horizontal tiling), Material Fracture, Pack, group expression VEX (`@P.x > bbox_mean + bbox_size_x*percentage`), For-Each loop (Fetch Feedback mode), power function (dome falloff), UV seam creation + island flattening (rectangular islands for tiling), Point VOP (displacement texture import, Composite node set to Overlay, Displace Along Normals).

### Difficulty
Intermediate (each tip is a compact, reusable technique; the group-expression VEX and Fetch-Feedback loop assume some VEX/loop fluency).

### Houdini Version
19.5.569 (visible in viewport title bar).

### Tags
extrude, uvs, material-fracture, vex, for-each-loop, displacement, architecture, procedural-modeling

---

## Related Tutorials
- [Procedural Modeling | First steps with Houdini](procedural-modeling-first-steps-with-houdini.md) — same cathedral-tower project this set of tips is applied to.
- [Procedural Bricks with Houdini](procedural-bricks-with-houdini.md) — companion brick-pattern tutorial on the same tower model.
- [Groups, Patterns in Houdini](groups-patterns-in-houdini.md) — related group-selection VEX patterns including bounding-box-percentage expressions.
