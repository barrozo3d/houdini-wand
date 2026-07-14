---
title: Houdini tips and tricks #2
source: YouTube
url: https://www.youtube.com/watch?v=rVduzdrKYZg
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, karma, materials, shaders, mtlx, triplanar, cgi-integration, procedural, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tips-and-tricks-2/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini tips and tricks #2

**Source:** [YouTube](https://www.youtube.com/watch?v=rVduzdrKYZg)
**Author:** cgside
**Duration:** 6m5s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. In this video we'll have a look at 5 different
[0:05] tips in Odini that I believe are interesting to know. So let's start on how to


### Spherical hdri projections in Houdini [0:09]
**Transcript (timestamped):**
[0:10] project a spherical hdr ion onto geometry in case you want to do some
[0:17] spatial lighting. As you can see I have this hdr I projected into a simple
[0:23] geometry and for the material I am using the material X and LITS with the image
[0:28] connected to the emission color. So the idea here is to start with simple shapes
[0:35] like a grid and adjust your projection to fit the floor then you can start to
[0:41] extrude the walls and create other shapes. In the UV project set the type to
[0:47] polar which is a spherical projection. Then looking at your image you can
[0:52] transform the projection accordingly with the translate and rotations
[0:56] gizmos. And I am adding some simple assets and a shadow catcher at the end. In
[1:04] this case I will recreate the lighting so it makes sense to make the set geometry
[1:08] invisible in the final render but still contributing to the lighting. You do that
[1:13] with the render geometry settings and under render visibility set it to
[1:20] invisible to primary rays. Adding the lights and a camera then you want to
[1:28] preview your backplate in the render for that use a background plate node and
[1:33] your shadow catcher object and the image. And in the end you'll have your
[1:40] objects added to the backplate. This is a very simple setup but should give you an
[1:45] idea of the workflow. So the second tip is about track planer projections. As you


### Fixing triplanar projections on multiple geometries [1:48]
**Transcript (timestamped):**
[1:53] might know in order to change the dialing we need a position node with a
[1:57] multiply. As for the offset you can use an add node. And as you can see by the
[2:04] fault we have quite a repetitive pattern along the seats. The first thing we
[2:10] can do to avoid repetition is to set the position node space to world but
[2:15] still we have repetition. So what we can do is use the add node to introduce
[2:22] some random offset and that's what I'm doing with this attribute. Each seat
[2:28] will have a different offset in the x, y and z position for the track planer
[2:33] projection. And you probably know how I have created that attribute just with a
[2:41] netribute randomized. Don't forget to pack your geometry if you have multiple
[2:47] meshes so it creates a point for each object. In this one I am just sharing


### Camera match in Houdini with fspy cam loader [2:51]
**Transcript (timestamped):**
[2:52] someone else's work that created an awesome HD8 to import FSPY files into
[2:58] Odini. Basically you will line your imagine FSPY and save it as a JSON file.
[3:04] In Odini you will add the FSPY Camloader HTA, add the JSON and image file and
[3:12] finally just read file and create camera. It can also do camera projections.
[3:18] Having the camera and image in place you can start to do your image based
[3:22] modeling. I live a link in the description. It's totally free. So this one is


### Random rotations with vex [3:27]
**Transcript (timestamped):**
[3:29] actually an update to what I have shared already on the channel. It's about
[3:34] random rotations and how to have control over the orient attributes when
[3:39] scattering geometry. I have a box that I want to scatter in this terrain but
[3:44] would like to give it some random rotation where I can control the angles and
[3:50] possibly orient them along the normal. So between the scatter and the
[3:55] copy to points I have this wrangle. As you can see I can control the rotation
[4:00] mean and max for all axis. Ever see value if I don't like the results? I can
[4:06] also orient the instances along the normal of the terrain without losing the
[4:11] initial rotation and finally offset the geo from the terrain in case we have
[4:17] floating instances. The code is quite basic as I'm still learning Vex but works
[4:24] pretty well. Basically we are creating a vector from the random rotations
[4:29] along with some UI channels for the mean and max rotation. At the beginning I
[4:36] have a channel to control the surface orient. Then in the statement if it's
[4:42] checked I can use this function to set the orient attributes. In a new variable I am using the
[4:49] alert to quarter nune's function to convert the values in degrees. And finally we can
[4:56] multiply the existing orient attributes with the new one. At the end I just
[5:01] have an offset along the y axis or the normal.
[5:05] So let's say you want to add some color or gain variation to leaf symmetry but the geometry


### Color variation on merged geometry [5:07]
**Transcript (timestamped):**
[5:14] is merged. First you need to isolate the target geometry and create a connectivity node.
[5:20] Then in a wrangle you can create a attribute between 0 and 1 giving the class attribute from
[5:27] the connectivity as the seed. Pretty simple but works well I have done the same thing for the
[5:35] leaves. And in salaries I am controlling the gain of the leaves with the attribute connected to a ramp.
[5:45] Using it also for the fruits but this time to set the base color. So yeah hopefully you got
[5:52] something out of this and don't forget to check my patreon where I share project files and
[5:57] exclusive tutorials and tools. Thank you for watching and see you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/houdini-tips-and-tricks-2/frame_000.jpg
- [1:55] tutorials/frames/houdini-tips-and-tricks-2/frame_001.jpg
- [3:00] tutorials/frames/houdini-tips-and-tricks-2/frame_002.jpg
- [3:50] tutorials/frames/houdini-tips-and-tricks-2/frame_003.jpg
- [5:20] tutorials/frames/houdini-tips-and-tricks-2/frame_004.jpg

---

## Structured Notes

### Core Technique
Five tips: projecting a spherical HDRI onto simple geometry (via a **polar UV Project**) to build a lit CGI-integration set with a shadow catcher, fixing Triplanar repetition across multiple merged objects with a per-piece randomized position offset, using a free **fSpy Cam Loader HDA** for camera-matched image-based modeling, a reusable VEX **random-rotation + surface-orient wrangle** for Scatter/Copy to Points, and a **Connectivity-seeded random attribute** for adding color/gain variation to merged geometry (leaves/fruit) without needing separate per-object pieces.

### Summary
**Spherical HDRI projection:** starting from a simple Grid (fit to the floor) extruded into walls/other set pieces, a **UV Project** node set to **Polar** type creates a spherical projection matching an HDRI panorama; the projection is manually transformed (translate/rotate gizmos) to align with the reference image, and the HDRI is fed into a **MaterialX Uber/Lights** shader's emission color so the geometry itself visibly displays the projected environment. Real assets and a shadow catcher are added on top; since the projected "set" geometry only exists to contribute lighting/shadows (not to be seen directly), its **Render Geometry Settings → Render Visibility** is set to **"Invisible to Primary Rays"** so it lights the scene but doesn't render. A **Background Plate** node combined with the shadow catcher and the original image lets the final composite show real objects seamlessly added onto the photographed backplate. **Fixing Triplanar repetition across merged objects:** Triplanar's default position-based tiling (adjusted via a **Position node + Multiply** for scale, **Add** for offset) shows an obviously repetitive pattern across multiple identical objects (e.g. church pews) even after switching Position space to World; the real fix is feeding the Add/offset node a **per-object randomized attribute** (built with Attribute Randomize) so each mesh gets its own unique X/Y/Z Triplanar offset — critically requiring the geometry to be **Packed** first so there's exactly one point (and thus one random value) per object/piece. **fSpy camera matching:** using the free, third-party **fSpy Cam Loader HDA**, align vanishing-point lines on a reference photo in the standalone fSpy app, save as JSON, then in Houdini load both the JSON and the source image into the HDA and click "Read File" + "Create Camera" to instantly get a matched camera (with projection support) for image-based modeling — link provided in the video description, tool is free. **Random rotation + surface orient (VEX, updated from an earlier video):** a wrangle placed between Scatter and Copy to Points exposes UI channels for min/max rotation per axis (with a re-roll/reseed option), an optional toggle to orient instances along the scattered surface's normal **without discarding the random rotation already applied**, and a final offset along the surface normal to lift instances off the terrain (avoiding floating/clipping issues) — built from a vector of random rotation values combined with the min/max UI channels, converted via `radians()`(described as "alert to quaternions") into a quaternion, and multiplied against the existing `orient` attribute rather than replacing it outright, so both the random spin and the surface alignment are preserved together. **Color/gain variation on merged geometry:** for merged geometry where you want per-piece color/gain variation but don't want to keep pieces separate, isolate the target geometry and run **Connectivity** to get a `class` attribute per contiguous piece, then in a wrangle generate a 0-1 random attribute seeded by that class value — applied identically to both leaves (driving shader **gain** via a Ramp in Solaris) and fruit (driving **base color** via the same pattern), giving natural per-cluster variation without ever needing to split the merged mesh apart.

### Key Steps
1. **Build the projection set:** start from a Grid fit to represent the floor, extrude walls/other simple shapes to roughly match the reference photo's geometry.
2. **Polar UV projection:** apply **UV Project** set to **Polar** type for a spherical projection matching an HDRI panorama; manually align it to the reference image using translate/rotate gizmos.
3. **Display the projection:** feed the HDRI image into a **MaterialX Uber/Lights** shader's emission color input so the projected geometry visibly shows the environment texture.
4. **Hide the set from camera, keep its lighting:** set the projection-set geometry's **Render Geometry Settings → Render Visibility** to **"Invisible to Primary Rays"** so it still contributes bounce lighting/shadows without appearing directly in the render.
5. **Composite over the real backplate:** add a **Background Plate** node referencing the shadow-catcher object and the original reference image so real CGI assets appear seamlessly composited into the photographed scene.
6. **Diagnose Triplanar repetition:** notice that Triplanar's default position-driven tiling (Position node + Multiply for scale, Add for offset) repeats obviously across multiple copies of the same object, even after switching Position space to **World**.
7. **Randomize the Triplanar offset per object:** feed the Add/offset node a per-piece **randomized attribute** (built via Attribute Randomize) so each object gets a unique X/Y/Z Triplanar offset, breaking the repetition.
8. **Pack before randomizing:** ensure multiple meshes are **Packed** first so exactly one point (and thus one random offset value) exists per object — without packing, the randomization won't apply per-object correctly.
9. **fSpy camera setup:** align vanishing-point lines in the standalone fSpy app on a reference photo, export as JSON; in Houdini, add the **fSpy Cam Loader HDA**, load the JSON + image, click Read File then Create Camera to get a matched camera ready for image-based modeling and projection.
10. **Random-rotation wrangle (Scatter → Copy to Points):** expose UI channels for min/max rotation per axis (with re-seed control); build a vector of random rotation values combined with those channels.
11. **Convert to quaternion and combine:** convert the rotation values (in degrees, via `radians()`) into a quaternion, then **multiply the existing `orient` attribute** by the new rotation quaternion (rather than overwriting it) so any prior orientation data is preserved.
12. **Surface-orient toggle:** add a checked UI toggle that, when enabled, orients instances along the scattered surface's normal **while still respecting the random rotation** already computed — combining both effects rather than one replacing the other.
13. **Offset to avoid floating instances:** add a final position offset along the surface normal (Y axis in the flat-terrain case) to lift/seat instances properly against the terrain surface.
14. **Isolate + connectivity for color variation:** isolate the target merged geometry (e.g. leaves, separately fruit) and run **Connectivity** to assign a `class` attribute per contiguous piece.
15. **Seeded random attribute:** in a wrangle, generate a random 0-1 value using the `class` attribute as the seed — giving each connected piece a consistent, unique random value.
16. **Drive shading variation in Solaris:** feed the class-seeded random attribute into a **Ramp** in Solaris to control shader **gain** for the leaves, and reuse the identical pattern to drive **base color** for the fruit — natural per-cluster variation with zero extra modeling work.

### Houdini Nodes / VEX / Settings
Nodes: Grid, Extrude, UV Project (Polar type), MaterialX Uber/Lights (emission color), Render Geometry Settings (Render Visibility: Invisible to Primary Rays), Background Plate, Shadow Catcher, Position (Triplanar, World space), Multiply (Triplanar scale/dialing), Add (Triplanar offset, attribute-driven), Attribute Randomize (per-piece offset generation), Pack (required before per-object randomization), fSpy Cam Loader HDA (third-party, free — JSON + image load, Read File, Create Camera), Scatter, Copy to Points, Attribute Wrangle (VEX: UI-channel-exposed min/max rotation per axis, `radians()` conversion, quaternion construction, multiplication against existing `orient` attribute, surface-normal-orient toggle, normal-offset lift), Connectivity (`class` attribute per piece), Attribute Wrangle (VEX: class-seeded random 0-1 attribute), Ramp (Solaris, gain/base-color driver).

### Difficulty
Intermediate — each tip is compact; the VEX random-rotation/orient-preservation wrangle and Triplanar packing requirement are the most non-obvious details.

### Houdini Version
20.5 (MaterialX/Karma workflow consistent with Houdini 20.5-era tools).

### Tags
#vex #karma #materials #shaders #mtlx #triplanar #cgi-integration #procedural #tips #intermediate

---

## Related Tutorials
Cross-link with from-sops-to-final-render-with-karma.md (same author, same CGI-integration/backplate/shadow-catcher workflow) and essential-procedural-techniques-in-houdini.md (shares the random-rotation-preserving quaternion VEX pattern) once indexed together.
