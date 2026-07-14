---
title: Houdini tips to save the day
source: YouTube
url: https://www.youtube.com/watch?v=lT0b8D6LmtM
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, uv, procedural, modeling, deformation, tips, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tips-to-save-the-day/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini tips to save the day

**Source:** [YouTube](https://www.youtube.com/watch?v=lT0b8D6LmtM)
**Author:** cgside
**Duration:** 10m27s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to share a few tips and tricks.
[0:05] I haven't done one of these in a while, so hopefully you'll get away with some new techniques.
[0:11] So I wanted to start with this simple example where let's say you want to scatter or some
[0:17] out-transform the outside parts or the ins or only the inside of this geometry and you
[0:23] have no access to the full network. So this could be easily done by targeting the
[0:29] prims facing the positive Z or the negative Z. But let's say you don't have access to
[0:35] the previous part and you only have this geometry. So the end goal is to create this sort
[0:41] of mask, so either outside or inside part and then we can clip it. And the way I'm
[0:48] going to do that, so we have the geometry. We calculate a connectivity, so just a class
[0:53] attribute on prims. Then we extract the centroid we add by group and we orient along the curve
[1:03] and we create some custom normals. In this case I don't want to save it as normal, I want
[1:07] to save it as underscore N or any other name. So that way I can copy that attribute to
[1:13] normals to the geometry and we will have that attribute as you can see. And in order to
[1:19] target the outside parts I can just do a comparison of the normals and that's normal attribute
[1:26] with that out product. And if we output that as a mask we have the outside part and if we
[1:32] invert the sign in here we get the inside that we can like very clip by a attribute as you
[1:38] can see. So I want to go back to a subject that we have explored before on orienting UVs


### UV Orientation [1:40]
**Transcript (timestamped):**
[1:46] up, as you can see. In this case I have this rough light shape and I have on purpose changed
[1:53] the rotation of the UVs. But even if we just do a UV flatten some of the islands might
[2:00] be become inverted as you can see, especially if you have a mirrored light shape. And this
[2:07] HDA that I created that I'm going to show you next can easily orient the UVs up and even
[2:14] if you feed a more complex geometry as you can see I have the UVs sort of scrambled in
[2:21] here and I can just place this one and it should orient properly up. So let's have a look
[2:28] at that HDA I'm going to switch to the simple geometry so this one in here and let's see what UVs
[2:36] I'm going to pick this one. So the idea is still the same we create the connectivity by UV
[2:44] islands and we will have an ID 40 challenge. Then we use the relative point bounding box to get
[2:53] the Y component so we have a value going on the Y direction and as you can see we just use
[3:02] the relative point bounding box and extract the Y component. Then we measure the gradient of that Y
[3:09] valve by piece attribute so by these islands and instead of using the default one of the position
[3:16] attribute which is P we use UV so we can do it in UV space. So this way we don't need to convert
[3:23] this geometry to UV like UV equal or P is equal to UV and after do the measuring there we can just
[3:32] do it in place in here by using the position attribute as UV. Then we just orient the UVs up with
[3:38] these vax snippets which we get the I'm saving these up tangent and we get that we using the
[3:47] prime function. Then we create in here a geo variable that we will unwrap the geometry in place
[3:58] that way we can get the bounding box on the bounding box center in UV space. So we can later subtract
[4:07] the that bounding box center rotate the UVs and get back to the original position
[4:14] after doing the rotation of course. Then we calculate the angle of that with the 8.2 and we do
[4:21] the rotation along the Z axis which is the axis that UVs operate on and that's how we do
[4:29] these UV oriental vz and we can change it to a more complex geometry. So in this one I wanted to


### Uniform Distribution [4:38]
**Transcript (timestamped):**
[4:39] talk about how to do some uniform distribution of shapes. So in this case if I come in here I have
[4:46] just a circle the form along the x axis or scale down and I'm copying these two points as you
[4:53] can see they have a uniform distribution but if I disable these and disable the p-scale they
[5:00] will still have the same uniform distribution but let's say I want to add some random some p-scale
[5:05] along the in this case the x axis. So I'm just mirroring here the bounding box x. So it gets
[5:12] scale down at the ends and more at the bottom at the middle and in order to redistribute them I can
[5:19] use a similar ramp in here but inverted with a resampled by density and I can change the the
[5:27] amount of segments I want then I would need to change the p-scale of course but in this case
[5:32] setting it to 4 and I can come in here and align this better and I can even distribute them the way
[5:37] I want if I want to change that but generally speaking you want to have a similar shape you have
[5:45] on your p-scale. So in the end I have this basic geometry that I build from just those shapes you
[5:53] have in here. You can have a look at the file on patreon if you're interested.


### Conform [5:59]
**Transcript (timestamped):**
[5:59] So let's say you have some geometry in this case I have these towers and I want to
[6:03] conform it to the to this tube. A simple way you can do that is by creating a grid then
[6:11] re-projecting the grid to the tube and use a lattice in point mode. We have a we have a look at
[6:17] this before. Use a lattice in point mode and play with radius and project that's the
[6:23] towers to the shape or conform it to the tube. Another way you can do this is by using the surface
[6:29] deform and as you can see it works a bit better although in some situations it might deform too much
[6:36] the shape. So that's a way to conform a shape to another without because the re-project here it
[6:45] wouldn't work since it has a thickness. So let's have a look at a more complex approach. So in this
[6:52] case let's see I have a circle fusing and sweeping just to get the rows in this case resembling
[7:01] any near I'm saving a prem ID that I probably won't use. Then I'm calculating an aperture
[7:07] boot as you can see in here to point out just by normalizing P and that will be important in a bit.
[7:15] Then I'm sweeping in near some rounded corners like a rectangle and I get this sort of look.
[7:27] Now let's say I want to conform this shape to the sphere so they wrap around.
[7:36] We can use the same approaches in here, use a grid and use the surface deform or the lattice but
[7:42] here the lattice won't work very well. So what we can do or the lattice or the surface deform will
[7:49] deform it too much. So in this case I'm doing after doing this sweep I'm doing another one in here
[7:56] set to ribbon. Then I'm assigning the up to the normals so I can easily re-project it to the sphere.
[8:06] And this is the deform geometry, this is the rest and this is the geometry to be deformed.
[8:11] Then with a simple point deform we can get this sort of look. If I use a surface deform I believe
[8:19] this gives a different result so we back to rest and the deformed as you can see it's not bad,
[8:28] it's just another just another way to do it but as you can see it will look much different. This one
[8:36] this one will have a more bulged out effect so in this case this one may work even better.
[8:43] So that's another way. So as you can see you can use more complex geometry and multiple shapes and
[8:48] these will hold up. I also have a custom one in here that is using a deformation matrix.
[8:57] Basically I wanted to show you in here so let's see how much different that is.
[9:04] So it's not much different but I wanted to show you something in here. So after calculating the
[9:09] matrix by using the normals in an aperture boot I am reading that deformation matrix by using
[9:16] the UV sample and since I have UVs in here because I UV flatten those ribbons I can simply read
[9:26] the position or sample any attribute by using the UVs but in this geometry I don't have the same
[9:36] UVs, I don't even have UVs. So what I can do is to UV sample based on position the UV attribute
[9:44] as you can see and we do get stretched UVs but that won't matter because we can now use the same
[9:51] UV sample to deform to reading that matrix that we calculated by using the UVs again and if we
[9:58] haven't calculated those UVs this wouldn't work as you can see. So just UV sample is such a powerful
[10:05] function that you can apply to reading normals and read any attributes you might want.
[10:12] So yeah guys all the project files will be available on my patreon alongside with exclusive tutorials
[10:19] if you are interested in learning more and as always thank you for watching and I hope to see you
[10:25] next time. Thank you.



---

## Captured Frames

- [0:30] tutorials/frames/houdini-tips-to-save-the-day/frame_000.jpg
- [1:50] tutorials/frames/houdini-tips-to-save-the-day/frame_001.jpg
- [3:50] tutorials/frames/houdini-tips-to-save-the-day/frame_002.jpg
- [5:00] tutorials/frames/houdini-tips-to-save-the-day/frame_003.jpg
- [6:20] tutorials/frames/houdini-tips-to-save-the-day/frame_004.jpg
- [7:30] tutorials/frames/houdini-tips-to-save-the-day/frame_005.jpg
- [9:00] tutorials/frames/houdini-tips-to-save-the-day/frame_006.jpg

---

## Structured Notes

### Core Technique
Four deep-dive procedural tricks: deriving an inside/outside mask purely from **per-piece custom normals** (`_N`) when you don't have access to the network that built the geometry, a general-purpose **UV-orient-up HDA** that works on any UV-island layout (even mirrored/scrambled ones) using UV-space gradient measurement, a **ramp-driven resample-by-density** technique for keeping copy-to-points distributions visually uniform despite varying `pscale`, and three different approaches (Lattice/Surface Deform, a custom ribbon-sweep + Point Deform, and a UV-Sample-driven deformation-matrix method) for **conforming repeated geometry to a curved surface** like a cylinder or sphere.

### Summary
**Inside/outside mask without network access:** given only a finished geometry (no access to how it was built), Connectivity assigns a `class` per piece, Extract Centroid + Group by class gets one representative point per piece, and **Orient Along Curve** computes a custom per-piece normal saved under a **different name** (`_N`, not `normal`) so it doesn't collide with the mesh's real normals; that custom attribute is copied back onto the full geometry, and a dot product between the real surface normal and this custom `_N` attribute (output as a mask, sign-inverted for the opposite selection) cleanly separates outside-facing vs. inside-facing pieces — usable directly in a Clip by Attribute. **UV-orient-up HDA:** rather than fighting UV Flatten's tendency to produce inconsistently-rotated or inverted islands (especially with mirrored geometry), a general HDA runs Connectivity **by UV islands** to assign each island an ID, uses **Relative Point Bounding Box** to extract the island's Y-direction component, then **measures the gradient of that Y value per-piece** — critically using the **UV attribute instead of P** as the position input to the gradient measure (avoiding any need to actually swap `P = UV` first, since the position-source parameter can just be pointed at `uv` directly), giving an "up tangent" direction per island. A geo-scoped VOP variable unwraps the geometry in-place to get each island's UV-space bounding-box center, subtracts that center (to rotate around the island's own pivot), computes the rotation angle via `atan2()`, rotates around the Z axis (the axis UVs conceptually operate on), then re-adds the center offset to restore position — producing correctly "up"-oriented UVs for arbitrarily scrambled or mirrored island layouts. **Uniform distribution with varying pscale:** copying shapes onto points along a curve normally gives uniform spacing, but introducing `pscale` variation (e.g. mirrored across the curve's X bounding box, larger in the middle, smaller at the ends) breaks that visual uniformity; the fix is an inverted ramp (matching the pscale variation's shape) fed into **Resample by Density**, letting you control segment count and re-align the varying-scale copies so the overall distribution still reads as evenly spaced despite the non-uniform individual sizes. **Conforming geometry to a curved surface (three methods):** (1) the simplest approach re-projects a Grid onto the target tube/sphere, then uses a **Lattice in point mode** (tuning radius) to conform separate "tower" objects to that projected grid — doesn't work when the target surface has real thickness, since Re-project can't handle that; (2) **Surface Deform** works better in many cases but can over-deform the source shape in some situations; (3) for a more complex multi-shape case (rounded-rectangle towers swept around a circle), a custom pipeline computes a per-point **aperture vector** (normalized `P`) during the initial build, sweeps a second "ribbon" copy of the same geometry with **Up assigned to the normals** (so it can be cleanly re-projected onto the sphere), and uses that ribbon as the **rest** shape input to a **Point Deform** against the actual sphere-deformed geometry — giving a look different from (and sometimes better than, less "bulged") Surface Deform's result on the same input. A fourth variant reads a **deformation matrix via UV Sample**: since the ribbon geometry was UV-flattened, its computed per-point deformation matrix (built from normals + aperture vector) can be looked up by UV coordinate on the target shape — critically, if the target shape has no native UVs, you can still build a throwaway UV attribute via **UV Sample based on position** (accepting stretched/meaningless UV shapes, since only the lookup matters, not the UV layout itself) and use that same "position-derived UV" both to sample and to store the deformation matrix — demonstrating that **UV Sample is a general-purpose "look up any attribute by proximity" tool**, not just for texture UVs.

### Key Steps
1. **Per-piece custom normal (inside/outside mask):** run **Connectivity** for a `class` attribute per piece, **Extract Centroid** + Group to get one representative point per piece, **Orient Along Curve** to compute a custom per-piece normal saved under a non-default name (`_N`) so it doesn't overwrite the mesh's real `normal` attribute.
2. **Copy the custom normal back + build the mask:** copy the `_N` attribute back onto the full geometry, then compute `dot(normal, _N)` and output it as a mask — this cleanly separates outside-facing pieces from inside-facing ones (invert the sign for the opposite selection); feed into **Clip by Attribute**.
3. **UV-island connectivity for orient-up HDA:** run **Connectivity by UV islands** to assign each island a unique ID.
4. **UV-space gradient measurement:** use **Relative Point Bounding Box** to extract each island's Y-direction component, then **Measure** (Gradient) that Y value per-piece — pointing the measure's position-source parameter at the **UV attribute instead of P**, avoiding any need to literally swap `P = UV` first.
5. **Rotate islands to face up (VEX):** in a geo-scoped VOP, unwrap the geometry in-place to get each island's UV-space bounding-box center; subtract that center (to rotate around the island's own pivot), compute the rotation angle via **`atan2()`** from the measured gradient's up-tangent, rotate around Z (the UV-space rotation axis), then re-add the center offset to restore the island's original position — works on arbitrarily scrambled or mirrored UV layouts.
6. **Base uniform copy setup:** copy a shape to points along a curve for a naturally uniform spacing baseline.
7. **Introduce varying pscale:** mirror a bounding-box-derived value (e.g. X size) to make copies larger in the middle and smaller at the ends, which visually breaks the previously-uniform spacing.
8. **Re-uniform via ramp + Resample by Density:** build an inverted ramp matching the pscale variation's shape, feed it into **Resample by Density** (tuning segment count), and adjust pscale to re-align — restoring a visually even-looking distribution despite the underlying scale variation.
9. **Conform via Lattice (simple case, no thickness):** re-project a Grid onto the target tube/sphere, then use **Lattice** in point mode (tuning radius) to conform separate tower objects to that projected grid — fails once the target surface has real thickness (Re-project can't handle that case).
10. **Conform via Surface Deform (alternative):** apply **Surface Deform** directly instead of the Lattice approach — generally works better with thickness, but can over-deform the source shape in certain situations; compare both to pick the better result per-case.
11. **Complex multi-shape conform — build a deformable ribbon:** while building the source geometry (e.g. rounded-rectangle towers swept around a circle), compute a per-point **aperture vector** (`normalize(P)`) early on; separately Sweep a second "ribbon" copy of the geometry with **Up assigned to the normals** so it can be cleanly re-projected onto the target sphere.
12. **Point Deform via the ribbon:** use the flat/rest ribbon as the rest-state input and the sphere-re-projected ribbon as the deformed-state input to a **Point Deform** targeting the actual repeated tower geometry — produces a different (sometimes better, less "bulged-out") look compared to Surface Deform on the same source.
13. **Deformation-matrix via UV Sample (advanced variant):** since the ribbon was UV-flattened, compute a per-point deformation matrix from normals + aperture vector, then look it up on the target shape via **UV Sample** using the ribbon's UV coordinates.
14. **UV Sample without real UVs:** if the target shape has no native UVs at all, build a throwaway UV attribute via **UV Sample based on position** (the resulting UV shapes will be stretched/meaningless, but that's fine since only the lookup matters) — use that same position-derived UV attribute both to sample and to store the deformation matrix, demonstrating UV Sample's general use as a "look up any attribute by proximity" tool rather than strictly a texturing feature.

### Houdini Nodes / VEX / Settings
SOPs: Connectivity (`class` attribute, and UV-island mode), Extract Centroid, Group, Orient Along Curve (custom-named normal output, e.g. `_N`), Attribute Copy, Attribute Wrangle (VEX: `dot()` for inside/outside mask, sign inversion), Clip (by attribute), Relative Point Bounding Box, Measure (Gradient, UV-based position source), VOP (geo-scoped, in-place unwrap for bounding-box center, `atan2()` rotation angle, Z-axis rotation, center-offset restore), Ramp (inverted, pscale-shape-matched), Resample by Density, Grid, Re-project, Lattice (point mode, radius), Surface Deform, Sweep (ribbon variant with Up = normals), Point Deform (rest/deformed ribbon inputs), UV Flatten, UV Sample (attribute lookup by UV or by position-derived UV), Attribute Wrangle (VEX: aperture-vector `normalize(P)` computation, deformation-matrix construction from normals + aperture vector).

### Difficulty
Advanced/Expert — combines custom-named-attribute VEX tricks, gradient-based UV-space rotation math, and three distinct conform-to-surface deformation strategies; assumes strong procedural-modeling and VEX fundamentals.

### Houdini Version
20.5 (UI matches Houdini 20.5-era toolset; Surface Deform and Point Deform workflow consistent with current versions).

### Tags
#vex #uv #procedural #modeling #deformation #tips #advanced

---

## Related Tutorials
Cross-link with groups-patterns-in-houdini.md and essential-procedural-techniques-in-houdini.md (same author, overlapping VEX-tips/UV-manipulation vocabulary) and houdini-tips-expressions-vex-recursive-cuts-and-more.md (shares the intrinsic/attribute-driven procedural-selection philosophy) once indexed together.
