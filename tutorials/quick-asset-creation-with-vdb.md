---
title: Quick asset creation with VDB
source: YouTube
url: https://www.youtube.com/watch?v=j0s0HkBCaQQ
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.493"
tags: [vdb, volumes, vex, noise, zbrush, displacement, solaris, rocks, environment]
extraction_status: complete
frames_dir: tutorials/frames/quick-asset-creation-with-vdb/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Quick asset creation with VDB

**Source:** [YouTube](https://www.youtube.com/watch?v=j0s0HkBCaQQ)
**Author:** cgside
**Duration:** 4m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this video we're going to have a look at a quick way to create rock assets using VDB.
[0:06] I'll be showing you all the settings, but in case you want the file with all the custom textures and model, it will be available on my Patreon.
[0:16] So this is just a quick example that I created, but that I think it has some interesting shapes and details.
[0:25] Okay, I started using a grid with a few subdivisions, extrude it, and then use the mountains op to have a more interesting shape to fit to the VDB setup.
[0:37] Now with the VDB from Bollygons we convert it to VDB, and it's where we can set the resolution and the clipping of the volume or bands.
[0:47] Next we have the volume knob where we're creating the noises that I'll be exploring in a minute, and finally we convert it to polygons that also helps to smooth out the shape, and just remove any small floating parts at the end.
[1:03] Okay, let me just reduce the resolution so we can work a bit faster.
[1:09] So this is my setup in the volume knob, only two noises and other two detect as distortion.
[1:17] The basic idea is to create an add-nose and add the incoming density with the noise and output the result.
[1:25] Not forgetting to connect the incoming position to the position attribute of the noise.
[1:31] Then you can start to play with the noise types and see which one fits better.
[1:36] There is room for epic accidents too.
[1:40] So the next step would be to play with the frequency of the noise, which is like the tiling of a texture.
[1:48] With a simple constant node and a divide by constant you can have a more intuitive control.
[1:54] If you increase the value it will produce a bigger noise and the other way around.
[2:01] Another thing you can do is to add a multiply constant to control the overall effect of the resulting noise.
[2:08] The last step of this setup after you have the main noise is to create a simple noise to distort it.
[2:14] This is a common use setup, using a turbulence or AA noise to distort the unified static.
[2:24] And that's pretty much what I have done here. You can identify your distortion noise and then the main noise with the frequency and multiply controls.
[2:39] The same goes for the second main noise.
[2:43] But this time using a feed range node to control the mean and max values that will help to create different outputs.
[2:51] As for the frequency I am also playing with the original values, mainly stretching the Y axis so it creates this particular look.
[3:02] The X-Renode here is a transform matrix that allows you for instance to rotate the noise. It can be interesting for some effects.
[3:13] As for the main noise I am using Manhattan Cellular F2F1 and using the complement attribute to invert the result.
[3:22] And that is the simple setup for this assets.
[3:29] Then I imported the Geo4in Z-Brush and did some Z-Remashing, Auto-UVs and exported a low poly and a displacement map.
[3:40] Then in Solaris I am bringing the Acetin, adding some subdivisions to the geometry, a material, light, camera and render settings.
[3:50] I am also doing a basic animation to render a turn table.
[3:55] So yeah that was it, another rock cliff tutorial and probably not the last. Hopefully I am not repeating myself.
[4:03] Thank you for watching and check out my Patreon and Gamurov if you'd like to support the channel. See you soon.



---

## Captured Frames

- [0:15] tutorials/frames/quick-asset-creation-with-vdb/frame_000.jpg
- [0:40] tutorials/frames/quick-asset-creation-with-vdb/frame_001.jpg
- [1:10] tutorials/frames/quick-asset-creation-with-vdb/frame_002.jpg
- [1:40] tutorials/frames/quick-asset-creation-with-vdb/frame_003.jpg
- [2:35] tutorials/frames/quick-asset-creation-with-vdb/frame_004.jpg
- [3:20] tutorials/frames/quick-asset-creation-with-vdb/frame_005.jpg
- [3:55] tutorials/frames/quick-asset-creation-with-vdb/frame_006.jpg

---

## Structured Notes

### Core Technique
A leaner, quicker variant of the VDB rock-sculpting workflow: a grid is extruded and mountain-distorted, converted to VDB, and detailed with just two main noises (each distorted by a secondary noise), then the result is sent to ZBrush for retopology/UV work before final texturing and rendering in Solaris.

### Summary
Compared to the studio's more elaborate cliff tutorials, this one keeps the Volume VOP setup deliberately simple — two main noise layers, each distorted by a secondary noise — to produce a quick rock asset. Frequency is controlled with an intuitive Constant/Divide-by-Constant pair instead of raw exponents, and a Multiply Constant scales the overall displacement strength. The second main noise (Manhattan Cellular F2F1, complement-inverted) uses a Feed Range for mean/max control and a stretched Y-axis frequency for elongated shapes, with an X-Rot transform matrix available to rotate the noise pattern for creative effects. After the volume detail pass, the mesh is imported into ZBrush for Z-Remeshing and Auto-UVs, exported as a low-poly mesh plus a displacement map, then brought into Solaris with subdivision, material, lighting, camera, and a turntable animation for final render.

### Key Steps
1. Base shape: Grid (with a few subdivisions) → Extrude → Mountain node for an interesting starting silhouette before VDB conversion.
2. **VDB from Polygons**: convert the mesh, setting resolution and clip/band values for the volume.
3. **Volume VOP**: create an Add Noise node that adds incoming density with a noise's output, remembering to connect incoming position to the noise's position input.
4. Frequency control: drive the noise frequency with a **Constant node divided by another Constant** for a more intuitive "bigger constant = bigger/wider noise" control instead of raw exponent tweaking.
5. Overall strength control: add a **Multiply Constant** after the noise to scale its contribution to the final displacement.
6. Distortion layer: use a second, simpler noise (Turbulence or a similar "AA noise") to distort the main Unified Static noise's position input before it drives density — the standard "noise distorts noise" pattern.
7. Second main noise layer: repeat the pattern for a second detail pass, but this time use a **Fit Range** node to control the mean/max values of the noise output, producing a different character of detail.
8. Directional stretching: for the frequency of the second noise, stretch primarily the **Y axis** to create an elongated, columnar look; an **X-Rot transform matrix** node is available on the noise to rotate the pattern for other effects.
9. Main noise choice: **Manhattan Cellular F2F1** with the **Complement** attribute enabled to invert the result, giving the characteristic blocky-cellular rock look.
10. Convert the finished VDB back to polygons, then export to **ZBrush** for Z-Remeshing, Auto-UVs, and export of a low-poly mesh plus a baked displacement map.
11. In Solaris: import the ZBrush-processed asset, add subdivision, assign a material, set up light/camera/render settings, and animate a simple turntable for the final presentation render.

### Houdini Nodes / VEX / Settings
Grid, Extrude, Mountain, VDB from Polygons (resolution, clip/band), Volume VOP (Add Noise pattern: Unified Noise / Unified Static, position input wiring, Constant ÷ Constant for frequency, Multiply Constant for strength, Turbulence/AA noise as secondary distortion, Fit Range for mean/max shaping, Manhattan Cellular F2F1 with Complement inversion, X-Rot transform matrix for pattern rotation), Convert VDB to polygons; external ZBrush pass (Z-Remesh, Auto-UV, displacement map export); Solaris/LOPs (Subdivision, material, light, camera, turntable animation, render settings).

### Difficulty
Intermediate (same core "noise distorts noise" VDB pattern as the studio's other cliff tutorials, but presented at a faster pace with a lighter setup).

### Houdini Version
19.5.493 (visible in viewport title bar).

### Tags
vdb, volumes, vex, noise, zbrush, displacement, solaris, rocks, environment

---

## Related Tutorials
- [VDB Procedural Cliffs](vdb-procedural-cliffs.md) — more elaborate version of the same noise-distorts-noise VDB rock-sculpting technique, scaled up to a full cliff with Solaris fog and tree scattering.
- [Rock formations with heightfields](rock-formations-with-heightfields.md) — alternate heightfield-based approach to quick rock asset creation from the same channel.
