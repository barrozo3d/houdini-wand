---
title: How to (not) bake brownies in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=R3ClxIiqxag
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, vex, vdb, flip, simulation, uv, procedural, food, advanced]
extraction_status: complete
frames_dir: tutorials/frames/how-to-not-bake-brownies-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to (not) bake brownies in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=R3ClxIiqxag)
**Author:** cgside
**Duration:** 11m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'm gonna be breaking down how I did this
[0:05] chocolate brownie in Odini.
[0:08] This is not by any means the way you should do it, but it's the oddini way I guess, and
[0:14] hopefully you'll get away with a few new techniques.
[0:17] So let's get started.
[0:18] So here's the final product, we'll start from the top, just from a box, which is the initial
[0:27] point, and then I'm grouping by normals, the primitives along the X, the positive X,
[0:36] then promoting it to edges and subtracting the smaller edges by using max edge length in
[0:44] a group note, then beveling that part, adding some normals, and grouping also the outside
[0:51] frames that will be our layering on the top, and I'm doing that by using the max edge
[0:58] length on the primitives.
[1:01] Then let's go to the layering part, the cracking part, I'm blasting away those primitives,
[1:08] then what we're mashing it since I want a uniform distribution, subdividing quite a
[1:13] bit, see some going to be dividing this geometry into smaller chunks into some clusters,
[1:23] let's say, then if I disable this mountain and look at this attribute ringle linear, I'm
[1:30] just scattering some points on the surface, and then using the near point, I can create
[1:35] a cluster attribute by randomizing the near point, as you can see.
[1:40] I define through this mountain and then apply the rest, after saving a rest state, we can
[1:46] have these displaced chunks, which is my final vote, so without the mountain it will look
[1:54] like a Varanoi fracture, but with the mountain we get these organic look.
[2:01] Then what am I doing here?
[2:02] I'm grouping some parts that I want to subdivid again, so break it down into smaller chunks
[2:10] by using these randomization in here, and I can change the length, then doing the same
[2:20] again, the same clustering algorithm, let's say, but this time I scatter a few more points,
[2:32] and I'm only creating the cluster attribute where the density, so this attribute we just
[2:36] looked is bigger than point nine.
[2:38] So in this case we are just dividing the bigger chunks into smaller ones, but not everywhere,
[2:44] just in some places.
[2:47] Then in here I'm converting these to a cluster integer attribute by using random flash,
[2:54] random f-ash, I don't know how to pronounce it, and this will give you random numbers and
[3:01] some add or even negatives, so I'm just enumerating them, as you can see in here, to have them
[3:07] in order, which can be handy.
[3:11] Promoting these to the cluster attribute to a primitive one and vertex splitting, so I
[3:16] can now the pieces isolated into individual elements, and in here we can ignore these, and
[3:24] I'm promoting to primitive because this vertex split expects primitive attribute or a vertex
[3:31] attribute, so that's why.
[3:34] Going back to point and doing an edge smooth, this is a bit slow, but it will help us
[3:39] have some nicer contours, and in here I'm displacing along the normals randomly based
[3:50] on the cluster attribute, as you can see, we could always introduce a seed if you want
[3:55] to play with the look.
[3:59] And then in here I'm deleting some random pieces, because I don't want to have it completely
[4:07] filled, so I'm just deleting some random pieces and you can change the seed.
[4:12] Then I want to displace these outer edges, I want to move them a bit out, so for that
[4:19] I'm grouping the unchained points, and then creating a surface distance attribute, so
[4:27] by using the surface distance function, as you can see in here, by feeding the unchained
[4:33] points.
[4:34] Then I'm normalizing the attribute and also playing with the fall off, so I have them
[4:42] just along the edges, and just attribute blurring as you can see.
[4:48] Then introducing some noise, so I can mix both, let me show you, so I can mix both in
[4:56] the displacements, as you can see some parts are displaced, some others are not so displaced.
[5:04] And the way I'm doing that is just by displacing along the normal, multiplying the surface
[5:08] distance we created, and a bit of the noise, and you can introduce more or less, as you
[5:14] can see.
[5:16] And we get this look.
[5:22] So now I want to do some transformations to the individual pieces, and in order to do
[5:27] that I need to have a center point to transform from.
[5:32] We could use extra centroid, but some of these pieces will have the centroid of the mesh,
[5:38] so that can be an issue.
[5:40] We could probably, we could probably extract the centroid on the cluster attribute and
[5:46] write project it to the mesh, but in this case I didn't think of that, so I did it in a
[5:51] slightly different way.
[5:53] Let's see, so I'm just UV flattening and creating these UV islands.
[5:59] Then promoting the cluster attribute to a prime, and moving the geometry, moving the UVs
[6:08] to 3D space, and extracting the centroid there on the cluster prime.
[6:14] And just UV sample to the original position, as you can see.
[6:20] And from here we can also sample the normals, because we will need them to constrain the
[6:26] geometry to the inner part, because we will displace it.
[6:31] So and we get back to these where we have the spaces, and now we can rotate them randomly
[6:39] by using a Q-rotate, and taking advantage of that normal to rotate around.
[6:46] So as you can see I'm rotating randomly, 8 degrees negative or positive along the normal,
[6:54] which is the normal we extracted in here.
[6:57] So these look something like this.
[7:00] Show you the eye frame.
[7:02] So just rotating them, just adding some chaos to the geometry.
[7:09] In here I need to show you how I did this.
[7:12] So we started with this geometry, which is just the interior part, the cake part.
[7:18] Then do some basic VDV operations to have this cake look.
[7:24] And I'm just converting it to VDV, and using 3 noises, so a basic one to remove some of
[7:34] the parts, to break a bit the cake.
[7:38] And then mixing two alligator noises with another turbulent noise.
[7:44] And one is just as a smaller scale than the other one, and we get this mixed look between
[7:49] an eye frequency and low frequency noise.
[7:53] So nothing special in there.
[7:55] And then I'm creating a proxy, let's say, so I can easily do some operations.
[8:04] And from those points that we extracted, those centroids, I'm re-projecting them to
[8:11] this proxy geometry.
[8:13] Otherwise the cracking parts or the layering parts will not be on the surface, it will
[8:19] be offset.
[8:22] So for that I'm running this wrangle in here to constrain the geometry to the surface,
[8:28] as you can see, otherwise it will look something like this.
[8:35] So as you can see, it's a bit of the surface and all flat.
[8:39] And when I run this, it will be constrained to the surface and a bit randomized.
[8:44] And the way I'm doing that is by using the diagonal function, by gathering the normals
[8:51] from the initial surface.
[8:54] And the blurred normals of my proxy geometry, and then I'm just transforming from one normal
[9:01] to another one, as you can see.
[9:04] And also subtracting the center position and adding it after the fact, or in this case
[9:11] adding the point position.
[9:14] So then I'm sickening and doing some basic BDB operations in here.
[9:20] And we end up with this.
[9:22] And the BDB operations are really simple, just very eye-frequency noise and playing
[9:28] with the fit function to have just these small cracks, as you can see.
[9:34] So now we also have this feeling and I shared how I did a similar one in my last short,
[9:44] if you haven't watched your Canon Evalog.
[9:47] But basically I am starting with the proxy geometry, clipping in the middle and blasting
[9:55] away the field polygons, because I'm feeling in here in the clip.
[10:01] Ticking the geometry, creating a point from volume and a viscosity attribute, as you can
[10:05] see.
[10:06] So we will have a bearing viscosity.
[10:10] So we can have longer streaks and smaller ones than just doing a basic collision source.
[10:18] And in this flip solver, I'm loading in the flip project, creating a pop source on
[10:27] all the points, and also loading in the collision geometry.
[10:33] And for the flip solver, I'm just enabling viscosity and viscosity attribute and some surface
[10:38] tension.
[10:39] Nothing too complicated, and just part of fluid's time shift frame and mesh the surface
[10:46] and mesh the points and we get something like this.
[10:50] Then is just a matter of transforming it a bit in to fit a bit better the initial shape
[10:56] we have.
[10:58] So yeah, a lot of work, but in the end it looks somewhat decent I guess.
[11:05] This file will be available on Patreon if you want a look.
[11:11] And I hope you have learned something new.
[11:14] Thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:20] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_000.jpg
- [1:45] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_001.jpg
- [4:00] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_002.jpg
- [6:40] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_003.jpg
- [8:20] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_004.jpg
- [9:30] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_005.jpg
- [10:40] tutorials/frames/how-to-not-bake-brownies-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
A full food-modeling pipeline for a chocolate brownie: a **near-point-based random clustering** technique (scatter + nearest-point lookup) to fracture a subdivided top layer into organic Voronoi-like chunks with Mountain-noise-driven displacement, a **UV-flatten-based centroid extraction** trick to get a correct per-cluster pivot for individual-piece rotation (avoiding Extract Centroid's whole-mesh-centroid pitfall on disconnected clusters), a **normal-blend re-projection** wrangle to conform separately-generated crack/layer geometry back onto a VDB cake proxy, and a **FLIP fudge-drizzle** simulation using variable viscosity (via a point-from-volume viscosity attribute) for varied streak thickness.

### Summary
The brownie top starts as a Box, grouped by normal (positive X) and edge-length-filtered to select and Bevel specific edges, with outer frames grouped (via max edge length) for the layering/cracking pass. That grouped layer is Blasted out, Remeshed for uniform point distribution, and Subdivided heavily. The core **organic-cluster fracture technique**: Scatter a handful of points on the remeshed surface, then in a wrangle use **near-point lookup with a randomized seed** to assign each surface point to its nearest scattered point, producing a `cluster` attribute that behaves like a randomized Voronoi partition; a **Mountain** node (applied per-cluster with a saved rest state) displaces each resulting chunk, giving an organic broken-chocolate look instead of the flat, hard-edged Voronoi fracture you'd get without the Mountain pass. A second, finer clustering pass (more scattered points, restricted to areas where the first pass's density value exceeds ~0.9) subdivides only some of the bigger chunks into smaller ones rather than uniformly re-fracturing everything. Cluster IDs (originally floats/random values, some negative) are converted to clean enumerated integers, promoted to primitive, and fed into a **Vertex Split** (which needs a primitive or vertex attribute, hence the promotion) to physically separate each cluster into an individual disconnected piece; **Edge Smooth** (slow but worth it) rounds the contours, and each piece is displaced along its normal by an amount randomized per-cluster (seed-controllable). Some pieces are randomly deleted (seed-controllable) so the layering doesn't read as fully "solid." Unshared/boundary points get a **Surface Distance**-based falloff (normalized, blurred) mixed with noise to selectively displace piece edges outward more than piece interiors, creating an uneven, natural-looking crumbly edge rather than uniform displacement everywhere. To rotate each disconnected piece around its own correct pivot (Extract Centroid alone can fail here since pieces are all part of one connected mesh and Extract Centroid computes a whole-mesh centroid, not a per-cluster one), the author instead **UV Flattens** the geometry (creating one UV island per cluster), promotes the cluster ID to primitive, moves the flattened UV shell into 3D space, and runs **Extract Centroid on that UV-space geometry per cluster** — then **UV Samples** that centroid position (and separately the normal) back onto the original 3D position using the UV coordinates as the lookup key. With a correct per-cluster centroid and normal now available, each piece is randomly rotated (±8°) around its own normal via **`qrotate()`**, adding chaotic, naturalistic variation to the otherwise-flat layered chunks. The interior "cake" part is built by converting to VDB and layering three noises: a basic one removes parts of the shape (breaking up the cake's silhouette), and two additional Alligator/turbulent noises at different scales (one low-frequency, one high-frequency) are mixed together for a varied cake-crumb surface look. A simplified proxy version of this cake geometry is built specifically so the earlier-extracted cluster centroid points can be **re-projected onto it** — otherwise the layering/cracking chunks would float above/offset from the actual cake surface rather than sitting flush on it. To conform the crack/layering geometry onto this bumpy proxy surface (rather than floating flat above it), a wrangle reads the initial flat surface's normal and the proxy's (blurred) normal, builds a rotation from one to the other, and applies it while separately subtracting/re-adding the piece's center position — constraining the geometry to hug the proxy surface with natural randomized variation instead of sitting rigidly flat. That conformed geometry is then Thickened and run through simple VDB operations (high-frequency noise + a `fit()`-based range remap) to add small surface cracks. A chocolate/fudge drizzle effect (referenced as similar to a previous "short" video) is built via **FLIP**: the proxy geometry is Clipped down the middle and the resulting fill polygons Blasted away (since the Clip itself provides the fill), Thickened, and converted to a **Point from Volume** with a **viscosity attribute** so the FLIP sim can vary streak thickness per-emission-point (thicker/longer streaks vs. shorter ones) rather than using one uniform viscosity value; the FLIP Solver uses a POP Source across all points plus loaded collision geometry, with **Viscosity + Viscosity by Attribute** and some **surface tension** enabled — after a Time Shift and standard surface/point meshing, the result is transformed slightly to better fit the initial cake shape.

### Key Steps
1. **Base bevel modeling:** Box → Group by normal (positive X) → promote to edges, filter by max edge length → Bevel; separately group outer frames (also via max edge length) for the later layering/cracking pass.
2. **Prep for clustering:** Blast the grouped layer geometry, Remesh for uniform point distribution, Subdivide heavily for enough resolution to fracture finely.
3. **Organic cluster fracture (core technique):** Scatter a handful of points on the remeshed surface; in a wrangle, use a **near-point lookup with a randomized seed** to assign each surface point a `cluster` ID matching its nearest scattered point — an organic, randomizable alternative to a strict Voronoi Fracture.
4. **Displace clusters organically:** save a `rest` state, apply **Mountain** noise per-cluster — without this step the result reads as a flat Voronoi fracture; with it, the chunks look organically broken.
5. **Second, localized clustering pass:** scatter more points and restrict the new cluster assignment to areas where the first pass's density attribute exceeds ~0.9 — subdividing only some larger chunks into smaller pieces rather than uniformly re-fracturing the whole surface.
6. **Clean cluster IDs:** convert the (possibly negative, non-sequential) random cluster values into clean enumerated integers, promote to primitive (required since Vertex Split expects a primitive or vertex attribute, not a point attribute).
7. **Physically separate pieces:** **Vertex Split** by the cluster ID to break the single connected mesh into individually disconnected pieces; **Edge Smooth** (slow, but improves contour quality) rounds each piece's silhouette.
8. **Per-piece displacement + culling:** displace each piece along its normal by a per-cluster randomized amount (seed-controllable); randomly delete some pieces (seed-controllable) so the layer doesn't read as fully solid/filled.
9. **Edge-biased displacement:** group unshared/boundary points, compute a **Surface Distance** attribute from them, normalize and tune its falloff, Attribute Blur it, then mix it with noise to displace piece edges outward more than piece interiors — producing an uneven, crumbly-edge look rather than uniform per-piece displacement.
10. **Correct per-cluster pivot via UV Flatten:** since Extract Centroid on the whole connected mesh gives a wrong (whole-mesh) centroid rather than a true per-cluster one, **UV Flatten** the geometry (one UV island per cluster), promote the cluster ID to primitive, move the flattened UVs into 3D space, and run **Extract Centroid** on that UV-space layout per cluster — giving a correct individual pivot per piece.
11. **UV Sample the centroid + normal back:** use **UV Sample** to bring both the computed centroid position and the piece's normal back onto the original 3D geometry via the UV coordinates as the lookup key (needed since the geometry will be displaced and pieces are otherwise hard to address individually).
12. **Randomized per-piece rotation:** with a correct centroid and normal now available per piece, rotate each piece randomly (±8°) around its own normal using **`qrotate()`** for naturalistic chaotic variation.
13. **Cake interior via VDB + layered noise:** convert the base cake shape to VDB; apply a basic noise to remove/break up parts of the silhouette, then mix two Alligator/turbulent noises at different scales (one low-frequency, one high-frequency) for a varied crumb-like surface.
14. **Cake proxy for re-projection:** build a simplified proxy version of the cake geometry, then **re-project** the earlier-extracted cluster centroid points onto this proxy — without this, the layering/cracking chunks would float above or offset from the real cake surface.
15. **Conform crack geometry to the bumpy proxy (normal-blend wrangle):** in a wrangle, read the flat surface's normal and the proxy's blurred normal, build a rotation transforming one into the other, and apply it while subtracting/re-adding the piece's center position — constraining the flat crack/layer geometry to hug the actual bumpy cake surface with natural variation instead of sitting rigidly flat.
16. **Surface crack detail:** Thicken the conformed geometry, convert to VDB, and add small cracks via a high-frequency noise combined with a `fit()`-based range remap.
17. **FLIP fudge drizzle setup:** Clip the proxy geometry down the middle, Blast away the resulting fill polygons (the Clip's own fill supplies the needed cap), Thicken, convert to **Point from Volume**, and assign a per-point **viscosity attribute** so different emission points can produce varying streak thickness/length.
18. **FLIP simulation:** POP Source across all points, load collision geometry, enable **Viscosity + Viscosity by Attribute** and some **surface tension** in the FLIP Solver; Time Shift a settled frame, mesh both the surface and the points, then Transform slightly to better align with the initial cake shape.

### Houdini Nodes / VEX / Settings
Modeling: Box, Group (normal-based, max-edge-length filtering), Poly Bevel, Blast, Remesh, Subdivide, Scatter, Attribute Wrangle (VEX: near-point cluster assignment with random seed; cluster-ID enumeration from `random()`; per-cluster rotation via `qrotate()`; normal-to-normal rotation blend for surface conforming), Mountain (per-cluster, with rest-state save/apply), Attribute Promote (point→primitive for Vertex Split), Vertex Split, Edge Smooth, Surface Distance (unshared-point falloff), Attribute Blur, UV Flatten (per-cluster island isolation), Extract Centroid (run on UV-space geometry), UV Sample (centroid position + normal lookup by UV), Group (unshared points). VDB: Convert VDB, layered Unified/Alligator/Turbulent noise (multi-scale mixing, `fit()` range remap for cracks), VDB Reshape/Smooth-style ops. FLIP/DOP: Clip, Thicken, Point from Volume (viscosity attribute), POP Source, FLIP Solver (Viscosity, Viscosity by Attribute, Surface Tension), Time Shift, surface + point meshing, Transform.

### Difficulty
Advanced/Expert — combines a custom near-point clustering fracture technique, a non-obvious UV-flatten-based per-cluster centroid extraction workaround, VDB layered-noise cake modeling, and a variable-viscosity FLIP drizzle sim; assumes strong VEX and simulation fundamentals.

### Houdini Version
20.5 (UI matches Houdini 20.5-era VDB/FLIP toolset; references a prior "short" video covering a similar drizzle technique).

### Tags
#modeling #vex #vdb #flip #simulation #uv #procedural #food #advanced

---

## Related Tutorials
Cross-link with cookies-and-chocolate-modeling-shading-and-sim.md, chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson.md, and handy-houdini-tips-vellum-uvs-modeling-and-more.md (same author, same chocolate/dessert-modeling project family, shares the wrinkle/peak and VDB-noise-crack vocabulary) once indexed together.
