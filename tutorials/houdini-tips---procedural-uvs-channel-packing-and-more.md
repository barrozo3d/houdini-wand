---
title: Houdini Tips - Procedural UV's, Channel Packing and more
source: YouTube
url: https://www.youtube.com/watch?v=m00nko87HeI
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, uv, modeling, texturing, unreal, zbrush, procedural, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini Tips - Procedural UV's, Channel Packing and more

**Source:** [YouTube](https://www.youtube.com/watch?v=m00nko87HeI)
**Author:** cgside
**Duration:** 4m36s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. In this video I'll share a few tips like procedural UVs, channel
[0:05] packing, pet the former and others. So in this scene I have agreed where I would like


### Squared Procedural UV's [0:09]
**Transcript (timestamped):**
[0:12] to keep squared UVs so my texture doesn't stretch as this is the default behavior of the
[0:18] UV texture node. There are a few ways you can achieve this. The first one is by calculating
[0:25] the ratio of the incoming flat shape and use an if statement in the X and Y scale of
[0:32] the UVs, checking if the ratio is bigger than 1 in X and smaller in Y, then if it falls
[0:40] we can calculate the scaling factor to fit the 0 to 1 scale. We will also need to make
[0:47] the Y value negative so it are unspropriately the UVs and move them to the default UV tile
[0:53] using the offset Y. A simpler approach is by using the UV flat
[0:58] and node, which we'd pretty much default settings, just using the top vertices as an access
[1:06] align vertex group to orient the UVs. This might look like a lot of work when you can
[1:13] simply manually scale the UVs, but if we are doing procedural UVs it can be handy
[1:20] and you can always save it as a preset for later use.


### Channel Packing [1:25]
**Transcript (timestamped):**
[1:25] Now let's check an easy way of doing channel packing so we can use several vertex color
[1:30] channels in Unreal for instance. I have this CD attribute for the eyes which is occupying
[1:36] RG and B of the color attribute, but I also have a concavity mask that I would like
[1:43] to include in the vertex colors. So in a simple wrangle we can take a single value of the
[1:49] original CD and map it to the right channel and do a concavity to the green channel. If
[1:58] you have more you can map it to the blue channel also. Now in Unreal we can separate the channels
[2:04] and apply different effects to them in this case setting the eyes color and adding some
[2:09] occlusion to the concave areas. In this example I wanted to show you how I used


### From Houdini to Zbrush [2:13]
**Transcript (timestamped):**
[2:16] it in a procedural workflow to quickly create a base mesh to further sculpting in the
[2:21] Z brush. So I'm taking this elongated half circle, twisting it and applying some transforms
[2:28] while resembling and saving a curve view attribute. And then add a point in the center and
[2:34] saving it to a group so I can use it in a polycats to divide the curve into two frames.
[2:43] Finally I can sweep it and as you can see if I didn't cut the geometry in half I wouldn't
[2:49] be able to have this particular look I was after which is a mix between a mirror in both
[2:55] axis while twisting. And feeding this to a sculpting program gave me an easier time than
[3:02] sculpting a perfect infinity sign there. In this case I have a pattern following the shape


### Multiple Path Deform [3:05]
**Transcript (timestamped):**
[3:09] of an half circle and the way I'm doing that is first by starting with a chain repeating
[3:16] the pieces along the curve and packing and pat the forming it with a curved half circle.
[3:22] Then taking the original shape and pat the forming it again. And here order of operations
[3:32] matters from what I've tested so it's easier to start with the pat flight and go from there.
[3:39] Also make sure you have the correct scale for your initial pat you can use a measure
[3:44] set to length. For this one I need to orient the legs out so I'm starting by getting


### N and Up to Orient Shapes with Sweep [3:45]
**Transcript (timestamped):**
[3:50] the points from the initial geo making sure to calculate the out normals in the orient
[3:56] along curve. Then in the copy to points I'm keeping the normals and if you have a deform
[4:03] shape you can simply use the normal attribute in the copy to points as it will out of
[4:09] aligned shapes. But in case you have a flat line you will need to rename your normals to
[4:14] the aperture boot so the sweep knows how to orient the polygons. So yeah that's about


### Outro [4:18]
**Transcript (timestamped):**
[4:20] it hopefully you picked up something new that you can use in your next project.
[4:25] Wrap the example files on Patreon and thank you for everyone that joins off our. See
[4:30] you next time.



---

## Captured Frames

- [0:20] tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/frame_000.jpg
- [1:40] tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/frame_001.jpg
- [2:30] tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/frame_002.jpg
- [3:20] tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/frame_003.jpg
- [4:00] tutorials/frames/houdini-tips---procedural-uvs-channel-packing-and-more/frame_004.jpg

---

## Structured Notes

### Core Technique
Five compact tips: two ways to force non-stretching square UVs from UV Texture's default (aspect-ratio-fit) behavior, packing multiple grayscale masks into RGB vertex-color channels for Unreal, using a twisted-and-mirrored half-swept curve profile as a ZBrush sculpting base mesh, and a **multi-stage Path Deform** + **N/Up-attribute** orientation pattern for building "legs"-style repeated geometry along a curve.

### Summary
UV Texture's default behavior stretches textures on non-square flat shapes. Two fixes: (1) a VEX approach computing the incoming shape's aspect ratio, using an if-statement to scale X or Y down to fit the 0-1 UV tile (negating Y to correct orientation and offsetting to place it correctly in the tile); (2) a simpler node-based approach using **UV Flatten** with default settings, driven by an axis-aligned vertex group (e.g. the top vertices) to orient the flattening — much less setup than the VEX version, and worth saving as a tool preset for reuse. **Channel packing:** a simple wrangle takes an existing CD (vertex color) attribute already using R/G/B for one purpose (eye color) and remaps a single value (a concavity mask) into an unused channel (green) — extendable to a third value in blue — so multiple grayscale masks travel together in one vertex-color attribute; in Unreal, the packed channels are separated and each drives a different material effect (eye tinting from one channel, extra occlusion in concave areas from another). **Houdini-to-ZBrush base mesh:** an elongated half-circle curve is twisted and transformed while Resampling and saving a `curveu`-based attribute, then a center point is added and grouped so a **Poly Cut** can split the curve into two halves; **Sweeping** the cut (rather than the uncut) curve produces a mixed mirror-and-twist "infinity sign" profile that would be much harder to hand-sculpt directly — feeding this pre-built base mesh into ZBrush gave an easier starting point than sculpting the shape from scratch. **Multiple Path Deform ("legs" along a curve):** build a repeating chain of pieces, pack them, and **Path Deform** them onto a half-circle curve; then Path Deform the *original* (un-repeated) shape a second time — order of operations matters here (starting with the Path Deform pass first, then working from there, was found to be the reliable sequence) — and getting the initial pattern's scale right requires **Measure (set to Length)** on the source geometry. To make the "legs" orient/splay outward correctly, points are taken from the initial geometry with **calculated out-normals** fed into **Orient Along Curve**; **Copy to Points** is set to preserve normals (works directly if you have real deformed-shape normals) — but for a flat line with no meaningful normal variation, the normal attribute must instead be renamed to the **aperture vector** so **Sweep** knows how to correctly orient the cross-section polygons along the curve.

### Key Steps
1. **Square-UV fix (VEX):** compute the flat shape's aspect ratio; if ratio > 1 in X and < 1 in Y (or vice versa), scale down the larger axis to fit the 0-1 tile, negate Y to correct flip, and offset Y to place the result in the default UV tile.
2. **Square-UV fix (node-based, simpler):** use **UV Flatten** with default settings, driven by an axis-aligned vertex group (e.g. top vertices) as the orientation reference — much less setup than the VEX version; save as a reusable tool preset.
3. **Channel packing (VEX):** in a wrangle, take a single value from an existing multi-purpose CD attribute and remap a separate mask (e.g. concavity) into an unused RGB channel (e.g. green — or blue for a third mask), packing multiple grayscale attributes into one vertex-color channel set for downstream use.
4. **Unreal channel unpacking:** in Unreal materials, separate the packed vertex-color channels and drive independent effects from each (e.g. eye tint from one channel, extra ambient occlusion in concave areas from another).
5. **ZBrush base-mesh curve setup:** take an elongated half-circle curve, twist and transform it, Resample while saving a `curveu`-based attribute; add a center point and group it.
6. **Split and sweep for a mirrored-twist look:** **Poly Cut** the curve into two halves at the grouped center point, then **Sweep** the *cut* curve (not the whole uncut curve) — producing a mixed mirror-plus-twist "infinity sign" profile impossible to get from the uncut curve, and much easier than sculpting the shape by hand; export to ZBrush as a sculpting base mesh.
7. **Repeating "legs" pattern setup:** build a repeating chain of pieces along a half-circle curve profile, **Pack** them, and run **Path Deform** to conform the chain to the curve.
8. **Second Path Deform pass:** Path Deform the *original* (non-repeated) shape a second time onto the same curve — noted that this specific order (Path Deform first, then building from there) is the sequence that reliably works, based on the author's testing.
9. **Scale calibration:** use **Measure** (set to Length) on the source geometry to determine the correct initial scale for the repeating pattern before deforming.
10. **Orient legs outward (N/Up for Sweep):** take points from the initial geometry with calculated **out-normals**, feed them into **Orient Along Curve**; in **Copy to Points**, preserve normals — this works directly for a deformed shape with real normal variation, but for a flat line (no meaningful normal direction), the normal attribute must instead be **renamed to the aperture vector** so Sweep correctly orients each cross-section's polygons along the curve.

### Houdini Nodes / VEX / Settings
Nodes: UV Texture, Attribute Wrangle (VEX: aspect-ratio if-statement for square UV scaling with Y-negation and offset; channel-packing single-value remap to unused RGB channel), UV Flatten (default settings, axis-aligned vertex-group-driven orientation), Group (vertex group for UV alignment), Resample (curveu attribute save), Group (center point), Poly Cut, Sweep, Pack, Path Deform (order-dependent, applied twice — repeating chain first, then original shape), Measure (Length mode, for pattern scale calibration), Orient Along Curve (out-normal input), Copy to Points (preserve normals option), attribute rename (normal → aperture vector, for flat-line Sweep orientation).

### Difficulty
Intermediate — each tip is compact and approachable, though the multi-stage Path Deform ordering and normal-vs-aperture-vector Sweep orientation nuance require some procedural-modeling experience to apply correctly.

### Houdini Version
20.5 (UI matches Houdini 20.5-era modeling toolset).

### Tags
#vex #uv #modeling #texturing #unreal #zbrush #procedural #tips #intermediate

---

## Related Tutorials
Cross-link with export-a-full-scene-from-houdini-to-unreal.md (same author, same Houdini-to-Unreal vertex-color/channel-packing production context) once indexed together.
