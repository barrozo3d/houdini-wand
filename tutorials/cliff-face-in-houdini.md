---
title: Cliff Face in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=mcP3wLo1lIQ
author: cgside
ingested: 2026-07-13
houdini_version: "H20+ (Copernicus/COPS, Labs tools)"
tags: [procedural, vdb, quadremesh, cops, texturing, uv, scattering, vellum, advanced]
extraction_status: complete
frames_dir: tutorials/frames/cliff-face-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Cliff Face in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=mcP3wLo1lIQ)
**Author:** cgside
**Duration:** 11m0s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'll be showing you how you can
[0:04] create this sort of cliff face in Odini and also how to apply some procedural
[0:12] texturing with cops. So let's get started in the top of the network. I'm


### Tutorial [0:20]
**Transcript (timestamped):**
[0:20] basically creating a grid and scattering some points. Also applying some point
[0:28] cheater on the Z axis and copying some boxes over. Here I'm just randomizing
[0:34] the aperture wood to have random orientations and also the scale, not the
[0:40] p-scale, but the scale with a natural wood noise. Then I'm just applying some
[0:49] overall distortion with a mountain and box clipping. So I can cut off the top
[0:58] in there as you can see and also feeling the nose. Then from here I'm applying
[1:07] let me remove the lighting. I'm applying a mesh sharpen to have these more
[1:15] polygonal look that you can identify better as rock shapes. Then doing a basic
[1:26] BDB conversion so I can unify the mesh and also some some Boolean intersection
[1:37] to cut off some shapes. As you can see near this just will out to give some
[1:46] variation basically with a remesh, a jubot blur, big until a little bit
[1:52] mountain and then doing a Boolean intersection. Then again another mesh sharpen
[2:00] and you start to see the planes of the rocks. That's the idea.
[2:07] And then using a doing again a BDB conversion to have the mesh we in better shading.
[2:19] Now I want to quad remesh it. But as you can see we lose some detail although
[2:27] I'm using 50,000 polygons but before it was 600,000 so I'm subdividing the mesh and then
[2:38] re-projecting it to the original mesh with minimum distance. This way we can get
[2:45] the fidelity but keep the better topology. Then I'm doing some cuts on the rocks with a volume
[3:00] up in a BDB setup. As you can see basically by manipulating the frequency of the noise in this
[3:13] case is just a simplex noise and that's turbulence noise to the position to distort it a bit.
[3:25] And then just fit the values to where these cuts on the rocks.
[3:34] And I'm caching this. This will be my iPoddy. We know you've used for now.
[3:42] So then I'm poly reducing in this case in a loop so it can be a bit faster
[3:49] and quad remesh it as you can see and this will be my loop poly. I just need to do some
[3:57] UVs for that I'm scattering some points creating a attribute with the point number and transferring it
[4:04] to the mesh as you can see. So I have these mesh divided into tiles.
[4:12] Then I'm just promoting it to a primitive attribute and iterating in a loop using a UV
[4:18] flatten and this will UV my mesh and then just lay it out and this will be my final UVs.
[4:32] Then that's my loop poly mesh transferring the UVs over the main mesh
[4:39] and this is how it looks. As you can see it did a pretty good job these labs UV transfer
[4:50] then measuring the curvature and creating an emiotic vision best so I can texture these
[4:59] in the cups. So in cups let's see how this looks so this is basically the texture in which is
[5:14] again pretty basic. I'm importing the iPoddy, restaurizing to UVs in this case set the space to
[5:26] UVs then restaurizing the attributes in this case the the AO, the concavity, the convexity from
[5:35] the curvature and then the alpha. Then create from the AO mask I'm creating a monotone GB
[5:46] as you can see and I sample the texture and then re-sample the ramp using the
[5:57] snippets I shared in the last video on the re-sample color ramps.
[6:03] Then doing it I just we adjust just to color correct a bit the initial colors then from the concavity
[6:20] I'm applying some color correction again I can show you how that looks so on the low poly mesh in
[6:29] this case so basically I'm darkening those concave areas then doing another edges we adjust in
[6:40] this case brightening the the convex areas as you can see if that's not this one this one
[6:54] as you can see I'm brightening those areas and since we have these sort of issues due to our UVs
[7:04] I'm just taking the alpha and extrapolating the boundaries as you can see and that should fix our issue
[7:14] so now for the vines there's nothing to complex really this can get pretty complex if you want to
[7:30] create a growth system and whatnot but I just kept it as simple as possible basically by importing
[7:38] the low poly clip it and scattering some points then sorting them by the y axis group ranging some


### Outro [7:40]
**Transcript (timestamped):**
[7:50] of the top points to be our start and then some of the middle in here connecting edges adjacent pieces
[8:02] adding some costature votes by using some noise and finding the shortest path as you can see
[8:11] fusing the points polypads we sample it with subdivision curves and then create these curve branches
[8:22] which is a lives note that allows you to create some branches I just said it the hda and promoted
[8:30] global seed from here I'm splitting the the branches creating an orientation along curve
[8:42] so I can copy some leaves to it but before that I have the the vines and just sweeping it as you can see
[8:53] and for the the leaves and creating again the orientation grouping some points randomly so where
[9:04] why we'll copy the leaves doing it at your good randomize for the p scale and then for the leaves
[9:16] I'm just drawing the curve as you can see pretty randomly fusing, resembling doing a mesh sharpen to
[9:25] have these sharp corners resembling again creating the geometry deleting the curves remashing
[9:38] and creating some UVs then I'm doing some UV draw sharp to fit the texture to it as you can see
[9:51] and also did some bend and I have three variations of leaves so one darker one more orange and one
[9:59] lighter that I'm doing I'm doing the attribute from pieces so I can randomize the
[10:08] the leaves and in the copy to points I am using the piece attribute in this case class from
[10:16] this connectivity note and attribute from pieces set in this case to piece weights
[10:25] and then I'm just copying the the leaves and altogether it comes something like this
[10:34] and with some lighting it will look even better so yeah guys that was it hopefully you got something
[10:44] out of this and don't forget you can grab all the files from my videos in Patreon on my Patreon
[10:51] and also check out my courses there other than that thank you for watching and I'll see you next time



---

## Captured Frames

- [0:40] tutorials/frames/cliff-face-in-houdini/frame_000.jpg
- [1:15] tutorials/frames/cliff-face-in-houdini/frame_001.jpg
- [1:52] tutorials/frames/cliff-face-in-houdini/frame_002.jpg
- [2:45] tutorials/frames/cliff-face-in-houdini/frame_003.jpg
- [3:25] tutorials/frames/cliff-face-in-houdini/frame_004.jpg
- [4:18] tutorials/frames/cliff-face-in-houdini/frame_005.jpg
- [6:29] tutorials/frames/cliff-face-in-houdini/frame_006.jpg
- [10:25] tutorials/frames/cliff-face-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Builds a procedural cliff face from scattered/noised boxes pushed through repeated VDB round-trips and Boolean intersections to fake rock-plane faceting, quad-remeshes and re-projects for clean topology, tiles+UVs it via a piece-based UV Flatten loop, textures it procedurally in COPS using curvature/AO masks, and finishes with a simple curve-based vine-and-leaf scatter system.

### Summary
A three-part pipeline (rock geometry → COPS texturing → vines/leaves). **Rock geometry**: scatter points on a grid, orient along Z, copy boxes, randomize orientation/scale with a natural/cellular noise, then repeatedly alternate between mesh operations (Mountain distortion, Box Clip, Mesh Sharpen for a faceted "rock plane" look) and volume operations (VDB conversion to unify the mesh, Boolean intersection to carve additional shape variation) — cycling mesh-sharpen → VDB → Boolean → mesh-sharpen again progressively reveals more rock-like planar faces. The dense result (600k+ polys) is **QuadRemeshed** down to ~50k, then the detail lost in that decimation is recovered by subdividing the low-poly result and **Ray**-projecting it back onto the original high-detail mesh (Minimum Distance method) — getting both good topology and full fidelity. Additional surface cuts come from a **VDB volume wrangle** driven by simplex/turbulence noise (frequency-tuned, values fit to carve cut lines). For UVs at scale, the mesh is tiled: scatter points, transfer a per-tile point-number attribute to the mesh, promote to primitive, then loop a **UV Flatten** per tile/piece and lay everything out — described as a "Labs UV Transfer"-assisted process that handles this well. **COPS texturing**: import curvature (AO/concavity/convexity) and alpha as baked maps, remap the AO into a grayscale base via a saved custom "resample color ramps" snippet from an earlier video, darken concave areas and brighten convex areas with separate HSV adjustments, and fix UV-seam bleed on the alpha via Extrapolate Boundaries. **Vines/leaves**: scatter points on the low-poly cliff, sort by Y and group-range the top/middle points as vine start locations, connect adjacent points with noise-weighted cost (shortest-path) to form organic vine paths, convert to curve branches via a Labs HDA (promoted Global Seed for variation), sweep the vine geometry, and scatter/orient three hand-drawn leaf variants (color-randomized via Connectivity + Attribute from Pieces "class"/piece-weights) along the branch curves.

### Key Steps
1. **Rock base**: Grid → Scatter points → orient along Z (point-normal-style) → Copy boxes onto points, randomizing orientation and scale via an **Attribute Noise** (Cellular/natural-wood noise type) rather than plain pscale randomization.
2. Apply overall **Mountain** distortion and a **Labs Box Clip** to cut off the top of the shape; fill holes as needed.
3. **Mesh Sharpen** to get a more faceted, identifiably-rock-like polygonal look.
4. Alternate volume/mesh passes for variation: **VDB from Polygons** (unify mesh) → **Boolean Intersection** (carve shape) → Remesh + slight blur + a touch of Mountain noise → another **Boolean Intersection** → **Mesh Sharpen** again — each cycle reveals more distinct rock "planes."
5. Convert back with VDB for clean shading topology, then **QuadRemesh** — at ~50k polys (down from ~600k), fine detail is visibly lost.
6. **Recover detail**: Subdivide the quad-remeshed low-poly mesh, then **Ray** it onto the original high-detail mesh using the **Minimum Distance** method — restores fidelity while keeping the better quad topology.
7. **Additional rock cuts**: a **Volume Wrangle** on a VDB, driven by a **simplex/turbulence noise** (tunable frequency, position distorted by the turbulence), with resulting values fit/remapped to carve visible cut lines into the rock surface. Cache this result as the working "high poly."
8. **Prep for UVs — tiling**: Poly Reduce in a loop (faster iteration) → QuadRemesh again for a lower-poly "loop poly" working mesh. Scatter points, create an attribute from the point number, transfer it to the mesh so it's effectively divided into numbered tiles.
9. Promote the tile ID to a primitive attribute, then in a for-each loop run **UV Flatten** per tile/piece, followed by a UV Layout pass — producing the final UV set on the low-poly mesh, which is then **UV-transferred** back onto the main high-detail mesh (described as the "Labs UV Transfer" doing a good job here).
10. Measure **curvature** (for AO/concavity/convexity) and bake an image-based visualization for later texturing in COPS.
11. **COPS texturing**: import the baked maps, rasterize to UV space, resample AO/concavity/convexity/alpha. From the AO mask, build a grayscale base via a saved **resample color ramps** snippet (from a prior tutorial), then color-correct: darken concave areas and brighten convex areas using separate HSV Adjust passes on the curvature masks. Fix UV-seam artifacts on the alpha channel with **Extrapolate Boundaries**.
12. **Vines**: import the low-poly cliff, Clip it, scatter points, sort by Y, and **Group Range** some top points as vine start locations and some middle points as intermediate targets.
13. Connect adjacent pieces with edges weighted by noise-based "cost," then find the **shortest path** between start/end point groups to generate organic vine routes; fuse points, PolyPath/resample with subdivision curves, then run through a **Labs "Create Curve Branches"** HDA (with Global Seed exposed/promoted) to generate branching vine geometry from the paths.
14. Split the branches, build an **Orient Along Curve** attribute, **Sweep** the vine curves into tube geometry.
15. **Leaves**: for placement, group points randomly along the vine curves (weighted so orientation follows the curve), copy leaves onto them with randomized pscale. For the leaf assets themselves: hand-draw a rough leaf outline curve, Fuse, Resample, **Mesh Sharpen** for crisp corners, Resample again, build geometry from the curve, delete the curve, Remesh, create UVs, and use **UV Draw Sharp** to fit the texture correctly; apply some bend for natural curl. Three leaf color variants (darker, more orange, lighter) are built and randomized per-instance using **Connectivity** (to derive a `class`/piece identifier) feeding an **Attribute from Pieces** node set to output piece weights, so the Copy to Points can pick a weighted-random variant per leaf.

### Houdini Nodes / VEX / Settings
Grid + Scatter → Copy (boxes) + **Attribute Noise** (Cellular, orientation/scale randomization) → Mountain + **Labs Box Clip** → **Mesh Sharpen** → [**VDB from Polygons** → **Boolean (Intersection)** → Remesh/blur/Mountain → Boolean → Mesh Sharpen] (repeated) → VDB convert → **QuadRemesh** → Subdivide → **Ray** (Minimum Distance re-projection) → **Volume Wrangle** (simplex/turbulence noise carving) → Poly Reduce (loop) → QuadRemesh (working mesh) → tile scatter + point-number attribute transfer → primitive-promoted per-tile **UV Flatten** loop → UV Layout → Labs UV Transfer (to high-detail mesh) → curvature Measure (AO/concavity/convexity bake) · COPS: raster-to-UV import, resample color ramps (custom snippet), HSV Adjust ×2 (concave darken / convex brighten), **Extrapolate Boundaries** (alpha seam fix) · vines: Clip + Scatter + sort-by-Y + **Group Range** (start/mid points) → noise-weighted edges + **shortest path** → Fuse/PolyPath/Resample (subdivision curves) → **Labs Create Curve Branches** HDA (Global Seed) → Orient Along Curve → Sweep · leaves: hand-drawn curve → Fuse/Resample/Mesh Sharpen/Resample → build geometry → Remesh → UVs + **UV Draw Sharp** → bend → **Connectivity** (`class`) + **Attribute from Pieces** (piece weights) → randomized Copy to Points.

### Difficulty
Advanced — combines heavy VDB/Boolean iteration for rock shaping, QuadRemesh + Ray detail-recovery workflow, per-tile UV Flatten looping, full COPS procedural texturing, and a shortest-path vine-growth system with a Labs branching HDA; a lot of distinct advanced techniques chained together in one relatively short video.

### Houdini Version
Uses COPS/Copernicus (Houdini 20+) for texturing and several Labs tools (Box Clip, Create Curve Branches, UV Transfer) — recommend Houdini 20 or later.

### Tags
#procedural #vdb #quadremesh #cops #texturing #uv #scattering #vellum #advanced

---

## Related Tutorials
Cross-link with [Basic Procedural Texturing with Cops in Houdini 21](basic-procedural-texturing-with-cops-in-houdini-21.md) — shares #cops #texturing; that tutorial covers the COPS texturing workflow (bake maps, Extrapolate Boundaries, curvature-driven color correction) in more depth than this video's condensed version.
