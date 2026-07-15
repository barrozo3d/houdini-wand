---
title: Procedural VDB Cookies
source: YouTube
url: https://www.youtube.com/watch?v=WKs4KHfHpyA
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.534"
tags: [vdb, volumes, vex, noise, cops, food, karma, solaris, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-vdb-cookies/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural VDB Cookies

**Source:** [YouTube](https://www.youtube.com/watch?v=WKs4KHfHpyA)
**Author:** cgside
**Duration:** 4m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. In this tutorial we will procedurally model a cookie using VDB
[0:06] anoises. Let's start by dropping a Geocontainer, Diving inside and creating a sphere.
[0:14] Now let's clip it and transform it in the Y-axis to make it flat.
[0:20] Closing the mesh with a polyfill and saving the patch group.
[0:24] Extruding the patch group and saving the front seam for the next step.
[0:31] Now we can bevel the front seam and finally subdivide the mesh to give the VDB a smoother input.
[0:38] Let's drop a VDB from polygons, increase it with the resolution. We will increase it even more
[0:45] for the final mesh. Change the name to density and fill the interior. These are common settings for
[0:53] a VDB setup. We can smooth the VDB quite a bit and let's drop a volume up.
[1:01] Let's start by deforming a bit the overall shape with a NaE noise, adding it to the density
[1:10] and decrease the intensity with a multiply constant. We will also need to increase the exterior
[1:17] band to avoid those holes in the volume. One thing that we can also change is out the bottom is
[1:24] deformed by the noise as usually it's pretty flat. So let's export an attribute using the
[1:31] relative pounding box Y-components so we can visualize it.
[1:38] Drop a color note before the VDB from polygons and in the surface attributes save out the point.cds
[1:46] color. We end up with this fog light preview so let's hide it with visualized notes.
[1:54] Now we need to convert it to polygons and with an attribute from volume we can finally visualize
[2:02] the attribute color. Let's adjust the ramp to mask out the bottom part. And back to the VOP
[2:10] we just need to multiply the noise by the mask and the bottom should be flat now.
[2:21] Now we can add our main noise, a unified static, connect it to the position and create a
[2:27] control for the frequency and amount. We want to use the wordlayF2F1, reduce the intensity,
[2:37] and invert it with the complement checkbox.
[2:44] With a feed range we can clamp out the inputs to create those typical broken parts and finally add
[2:50] some fractal distortion. You can also play with the scale of the noise or even reduce the effect
[2:58] with the feed range and multiply constant. Here I'm just creating switch notes to turn on and off
[3:06] the effect of each noise so we can focus on each noise separately. Let's duplicate the unified
[3:13] noise setup to create the next effect. Here we just need to clamp a bit more the inputs,
[3:19] play with the frequency and remove the fractal. We will instead use a turbulence to distort
[3:27] the noise so we can create some details on the cookie surface. We just need to add the turbulence
[3:36] to the position inputs of the original noise. In the final resolution everything will be more
[3:42] details. Let's keep it low rest for now to have a faster feedback. So in this final noise we want
[3:51] to create some fine details. Let's use again a unified noise and copy the setup notes from before.
[3:58] We'll use a Warly F1, play with the feed range and finally scale the effects to have those fine details.
[4:12] Let's enable all the noises and set a final resolution on the VDB.
[4:18] And as you can see all the details are now much more pronounced, you can always play with the noises
[4:24] and get your own result. From here you can compose the scene and take it to Salaris with some
[4:31] procedural noises and masks generated. You can create some materials for the cookies and render it.
[4:39] So yeah hopefully you learned something new and you can grab the scene file from my Patreon if
[4:45] you want to play with it. Thank you for watching and see you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-vdb-cookies/frame_000.jpg
- [0:40] tutorials/frames/procedural-vdb-cookies/frame_001.jpg
- [1:10] tutorials/frames/procedural-vdb-cookies/frame_002.jpg
- [1:35] tutorials/frames/procedural-vdb-cookies/frame_003.jpg
- [2:10] tutorials/frames/procedural-vdb-cookies/frame_004.jpg
- [2:55] tutorials/frames/procedural-vdb-cookies/frame_005.jpg
- [3:40] tutorials/frames/procedural-vdb-cookies/frame_006.jpg
- [4:30] tutorials/frames/procedural-vdb-cookies/frame_007.jpg

---

## Structured Notes

### Core Technique
Model a cookie's characteristic broken/cracked surface procedurally using a stack of cascading VDB noises, while specifically flattening the bottom (which real dough noise wouldn't do on its own) via a bounding-box-derived mask, and previewing color/attribute data on volumes using a Color-node + Attribute-from-Volume round-trip before final detail.

### Summary
Starting from a clipped, flattened sphere closed with Polyfill and beveled/subdivided for a smooth VDB input, the cookie shape is converted to a VDB and detailed inside a Volume VOP with four layered noises of increasing fineness. A key trick is exporting the relative-bounding-box Y-component as a visualizable mask (via a Color node feeding CD into VDB from Polygons, then Attribute from Volume to read it back after Convert to Polygons) so the bottom of the cookie can be kept flat despite the noise — done by multiplying the noise contribution by this bottom mask inside the VOP. The main noise uses Worley F2F1 with Complement inversion and Fit Range clamping to create the classic "broken parts" look, and a final Turbulence-distorted fine-detail pass adds surface roughness. The result is exported to Solaris for material/scene composition and Karma rendering.

### Key Steps
1. Base shape: Sphere → Clip (flatten via Y-axis transform) → Polyfill (closing the mesh, saving the patch group) → Extrude the patch group → Bevel the front seam → Subdivide for a smooth VDB input.
2. **VDB from Polygons**: increase resolution (higher for the final pass), rename the attribute to `density`, enable Fill Interior, then **Smooth VDB** before the Volume VOP.
3. First noise layer: a basic noise deforms the overall shape, added to density and scaled down with a Multiply Constant; increase the **exterior band** to avoid holes forming in the volume.
4. **Flat-bottom mask**: export the relative bounding-box Y-component as an attribute so the effect can be visualized; use a **Color node** before VDB from Polygons to save this value into `Cd`, then after Convert to Polygons use **Attribute from Volume** to read the color back as a real attribute — adjust a Ramp to mask out just the bottom, then multiply the main noise by this mask inside the VOP so the bottom stays flat despite the noise.
5. Main "broken parts" noise: a Unified Static noise connected to position, with user-facing frequency/amount controls; use **Worley F2F1**, reduce intensity, and invert with the **Complement** checkbox.
6. Use **Fit Range** to clamp the noise inputs, producing the characteristic broken/cracked parts, then add fractal distortion on top; switch nodes are used to toggle each noise layer on/off individually for isolated tuning.
7. Second noise layer: duplicate the first noise setup, clamp the inputs more aggressively, adjust frequency, and remove the fractal component — instead distort this noise's position with a **Turbulence** node to add fine surface detail directly on the cookie surface.
8. Final fine-detail noise: another Unified Static copy using **Worley F1**, shaped with Fit Range and scaled down for very fine, close-up detail.
9. Enable all noise layers together and set the final production resolution on the VDB — details become far more pronounced at full res.
10. Take the finished mesh to Solaris, compose the scene with procedural noises/masks for material variation, assign cookie materials, and render with Karma.

### Houdini Nodes / VEX / Settings
Sphere, Clip, Polyfill (patch group), Extrude, Bevel, Subdivide, VDB from Polygons (density attribute, resolution, Fill Interior), VDB Smooth, Volume VOP (Bounding Box relative-Y export, Ramp mask, Multiply-by-mask for flat bottom, Unified Static noise, Worley F2F1/F1, Complement inversion, Fit Range clamping, Fractal distortion, Turbulence distortion, Switch nodes for isolating layers), Color node (CD export for volume preview), Attribute from Volume (reading baked attributes back after Convert to Polygons), Convert VDB to Polygons; Solaris/LOPs scene composition and Karma render.

### Difficulty
Intermediate (the cascading-noise VDB pattern is approachable, but the bounding-box-mask flat-bottom trick and color-round-trip preview technique require some VOP fluency).

### Houdini Version
19.5.534 (visible in viewport title bar).

### Tags
vdb, volumes, vex, noise, cops, food, karma, solaris, procedural-modeling

---

## Related Tutorials
- [VDB Procedural Cliffs](vdb-procedural-cliffs.md) — same cascading noise-in-Volume-VOP technique applied to rock surfaces instead of food.
- [Procedural tips | Heightfields and VDB](procedural-tips-heightfields-and-vdb.md) — covers the same color-node/Attribute-from-Volume preview trick for visualizing volume noise attributes.
