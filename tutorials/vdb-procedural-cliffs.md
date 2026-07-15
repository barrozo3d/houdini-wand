---
title: VDB Procedural Cliffs
source: YouTube
url: https://www.youtube.com/watch?v=fBhtlmCGrK4
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.435"
tags: [vdb, volumes, vex, noise, solaris, karma, environment, cliffs, rocks, scattering, instancing]
extraction_status: complete
frames_dir: tutorials/frames/vdb-procedural-cliffs/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# VDB Procedural Cliffs

**Source:** [YouTube](https://www.youtube.com/watch?v=fBhtlmCGrK4)
**Author:** cgside
**Duration:** 5m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this video I'm going to show you how to create rocks or cliffs with VBD noises,
[0:09] then walk you through the Solaris setup.
[0:13] This is just an example of the kind of details you can create for rocks or cliffs.
[0:18] I just did this simple example.
[0:22] I started with a box and did some very basic sub-apparations like extruding and bambling,
[0:29] then added a mountain at the end to distort a bit the shape.
[0:34] After that I converted it to VDB and all the cool stuff happens at the volume drop.
[0:41] In the VBD from Polygons it's recommended you change the attribute to density instead
[0:46] of the default surface, it will make our life easier.
[0:51] And of course set the desired resolution, this can get pretty slow so for now let's
[0:56] work with a low rise version.
[0:59] So the volume pop looks like it's pretty confusing if you're a beginner, but it's actually
[1:06] repeating the same stuff over and over.
[1:10] The basic idea is to distort the shape with noises and sometimes add another noises
[1:16] to distort the main noises.
[1:19] Let's start with the first noise which is just displacing the shape overall.
[1:24] So we take the position from the inputs and we feed it to a unified noise.
[1:30] I only experimented with the noise type and changed the frequency or repetition of the
[1:37] noise.
[1:38] Then as mentioned before I am using another noise to distort the main pattern which by default
[1:44] is pretty rigid.
[1:46] Basically taking a noise, manipulating the values with the feed range and adding it to
[1:52] the position inputs.
[1:56] At the end there's just a multiply by constant to control the amount of displacement.
[2:05] So in this second layer of detail I am creating this pattern with a Manhattan cellular and increasing
[2:12] the mean value of the original range quite a bit to add some contrast to the effect.
[2:20] Then again distorting the noise with another one.
[2:32] There's nothing new going on in this third layer, just a different noise and frequency,
[2:37] playing with the values of the feed range.
[2:47] For the last pattern I am creating this cuts in the volume mostly by manipulating the frequency
[2:53] of the noise in one of the axis.
[2:56] Also rotating the pattern in X.
[3:00] And using again the unified noise which being slower than the let's say the turbulence,
[3:07] it has more variety of noises.
[3:10] And yeah this is just an example of what you can create, you can change the source shape
[3:15] and manipulate the noises in different ways to have a completely different output.
[3:21] After converting it to polygons I am creating a mask to scatter some trees.
[3:27] Basically taking the white components of the normal attributes and feeding it to a ramp.
[3:34] Finally just use a bind export to create the attribute.
[3:39] So quickly going through the cellarysetup.
[3:43] I am importing the mesh and applying a material with the trap liner nodes.
[3:50] I am also using a bit of displacement and auto-bam to add some details.
[3:55] Then adding some fog, layering some noises as covered in the 3D environment tutorial.
[4:03] And as far as I know you need to export it as a VLV and import it in a volume node to
[4:10] render in our node.
[4:12] For the trees I used the component geometry to import the different assets using the geometry
[4:19] variant setup as shown in previous videos.
[4:24] Feeding the assets into the instacer and inside I am scaling some points.
[4:31] Using the orientation and scale and using the mask or attribute created before on this
[4:37] pattern node.
[4:38] Finally adding a light, a camera and that's about it.
[4:44] And this was my final result as you can see we can create some nice details on the mesh
[4:49] just by using VDVs.
[4:53] In case you want the file I will upload it to my Patreon and also check out my gamroad
[4:58] where you can find many free tools and an environment tutorial.
[5:04] Thank you and see you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/vdb-procedural-cliffs/frame_000.jpg
- [0:40] tutorials/frames/vdb-procedural-cliffs/frame_001.jpg
- [1:05] tutorials/frames/vdb-procedural-cliffs/frame_002.jpg
- [1:40] tutorials/frames/vdb-procedural-cliffs/frame_003.jpg
- [2:55] tutorials/frames/vdb-procedural-cliffs/frame_004.jpg
- [4:00] tutorials/frames/vdb-procedural-cliffs/frame_005.jpg
- [4:50] tutorials/frames/vdb-procedural-cliffs/frame_006.jpg

---

## Structured Notes

### Core Technique
Sculpt rock/cliff surface detail procedurally by layering multiple noises inside a VDB Volume VOP (each noise distorting the previous one's position input), then take the result into Solaris for triplanar shading, displacement, fog, and instanced tree scattering.

### Summary
A simple box is extruded and beveled, then hit with a Mountain node to break up the base silhouette before converting to VDB. Inside the Volume VOP, four cascading noise layers each displace the incoming density (or distort the position feeding the next noise): a base Unified Noise displacement distorted by a secondary noise, a Manhattan Cellular pattern with an increased range mean for contrast, a third generic distortion layer, and a final "cuts" layer made by stretching frequency along one axis and rotating in X to carve directional grooves. After converting back to polygons, a mask is built from the white component of the normal (fed through a ramp and Bind Export) to drive tree scattering. In Solaris, the mesh gets a triplanar-based rock material with displacement and auto-bump, plus layered fog volumes (exported as a VDB and re-imported), while trees are brought in via Component Geometry with geometry variants and instanced with orientation/scale driven by the same normal-based mask.

### Key Steps
1. Model a rough base shape: Box → Extrude → Bevel → Mountain (to distort the silhouette before volume conversion).
2. Convert to VDB via **VDB from Polygons**, setting the attribute name to `density` (not the default `surface`) and choosing a working resolution (kept low during setup for speed, raised for the final pass).
3. Inside the **Volume VOP**, repeat the same pattern for each detail layer: take incoming position → feed to a noise (Unified Noise, Manhattan Cellular, etc.) → distort that main noise's position input with a second, secondary noise → add the result to density → multiply by a constant to control displacement amount.
4. Layer 1 (base shape): Unified Noise on position, distorted by a secondary noise via Fit Range, added to position, scaled with a Multiply Constant.
5. Layer 2 (contrast detail): Manhattan Cellular pattern with an increased Fit Range mean for more contrast, again distorted by a secondary noise.
6. Layer 3: a different noise type/frequency, values shaped with Fit Range, distorting the position similarly.
7. Layer 4 (directional cuts): stretch the noise frequency heavily along one axis and rotate the pattern in X, using Unified Noise (chosen over Turbulence for its wider noise-type variety) to carve elongated grooves into the volume.
8. Convert the finished VDB back to polygons, then build a **scattering mask**: take the white component of the point normal attribute, feed it through a Ramp, and store it with a **Bind Export** so it's available downstream as a real attribute.
9. In Solaris: import the mesh, apply a rock material using **Triplanar** nodes, add displacement and auto-bump for extra surface detail, then layer fog volumes (built the same way as covered in the studio's "3D environment" tutorial) — export the fog as a VDB file and re-import it through a Volume node for Karma to render it.
10. Tree scattering: bring trees in via **Component Geometry** with the Geometry Variant workflow shown in earlier videos, feed the assets into an Instancer, and inside it scale points and drive orientation/scale using the previously created normal-based mask/pattern attribute.
11. Finish with a light, camera, and render settings; final result shows a tall rock spire wrapped in fog with instanced trees along its top edges.

### Houdini Nodes / VEX / Settings
Box, Extrude, Bevel, Mountain, VDB from Polygons (density attribute, resolution/clipping bands), Volume VOP (cascading noise-distorts-noise pattern: Unified Noise, Manhattan Cellular, Fit Range, Multiply Constant, Add), Convert VDB / Convert to Polygons, Bind Export (mask attribute from normal), Ramp, Solaris/LOPs Triplanar material (displacement, auto-bump), fog volume export/import (VDB file round-trip, Volume node), Component Geometry + Geometry Variant setup, Instancer (orientation/scale from mask pattern), Karma render settings.

### Difficulty
Intermediate (VDB volume noise stacking is approachable once the "noise distorts noise" pattern is understood, though the full Solaris/fog/instancing pipeline assumes familiarity with the studio's other environment tutorials).

### Houdini Version
19.5.435 (visible in viewport title bar).

### Tags
vdb, volumes, vex, noise, solaris, karma, environment, cliffs, rocks, scattering, instancing

---

## Related Tutorials
- [Quick asset creation with VDB](quick-asset-creation-with-vdb.md) — same noise-distorts-noise VDB technique applied to a smaller rock asset with ZBrush/displacement-map finishing instead of Solaris scattering.
- [Environments in Houdini Part 1 - Heightfields](environments-in-houdini-part-1---heightfields.md) — related environment-building pipeline referenced as the source of the fog-layering technique reused here.
- [Rock Formations with Heightfields](rock-formations-with-heightfields.md) — alternate heightfield-based approach to similar rock/cliff surface detail.
