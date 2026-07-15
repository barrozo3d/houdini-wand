---
title: Procedural Fries with Mtlx and Karma XPU
source: YouTube
url: https://www.youtube.com/watch?v=lcgNaIicsZU
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.331"
tags: [materialx, karma-xpu, hda, decals, vex, boolean, displacement, food, product-viz]
extraction_status: complete
frames_dir: tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Fries with Mtlx and Karma XPU

**Source:** [YouTube](https://www.youtube.com/watch?v=lcgNaIicsZU)
**Author:** cgside
**Duration:** 3m36s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there, today I wanted to share a few tips on procedural texturing, you know, Dini,
[0:05] showing up this simple project.
[0:08] So the first challenge I had was on how to project vehicles or logos similar to my


### Projecting Decals [0:11]
**Transcript (timestamped):**
[0:13] as planar projection feature.
[0:16] So in subs I created a very simple HDA that uses UV planar projection, which allows me
[0:23] to control the position of the decal, and it also creates a proximity based mask, so
[0:29] the texture doesn't show up in the back of the model.
[0:33] As you can see it's just a point in the same position of the planar projection, and transferring
[0:39] an attribute to the geometry.
[0:42] I'll share this HDA on Patreon along with the full scene, that way you can also see how
[0:48] I've modeled the cup and simulated the fries.
[0:52] So in Solaris I am first controlling the scale with the place to denote, loading the texture,
[0:59] making sure I set the address mode to Constance, so the texture doesn't tile.
[1:04] Then multiplying the alpha with the mask from sobs, again so it doesn't repeat on the
[1:09] back as you can see here, since I've just done a planar projection.
[1:19] And then using the mask as a mixing factor to combine the texture and the red in background.
[1:26] I also have a final detail on the cup, where I'm placing this line along the top, which
[1:31] I've accomplished with a primitive attribute to get the desired sharpness.


### Primitive Attributes [1:36]
**Transcript (timestamped):**
[1:36] So this is the attribute as you can see, I had no idea on how to do this in a procedural
[1:42] texture-based way, so I've just modeled the detail into the final geometry.
[1:48] Since I had some edge groups on the modeling, I extracted the side ones and created the
[1:53] normal along the curves.
[1:56] Then transfer them to the top edge curve, this way I can pick it along the shape.
[2:01] From there I am resampling to make it smoother, duplicating the curve with a sweep, and the
[2:07] ugly parts, a Boolean set to Shutter mode, and finally created the attribute with the
[2:12] resulting group.
[2:14] Again, not the most elegant way, but sourdlobs here are your ideas on the comments below.
[2:20] Now let's quickly have a look at the price shader.


### Fries Shader [2:24]
**Transcript (timestamped):**
[2:24] First in the albedo I have a mix of colors and noises to create some variation.
[2:29] In the first part I mix between orange and yellow, controlled by a whirling noise, then
[2:34] using another noise to mix the main yellow shades and other mix of colors.
[2:40] For the displacement using the unified noise, but distorting it a bit with a fractal by
[2:46] adding it to the position just like in Vops.
[2:50] I duplicated the noise and changed the frequency and type, and added them together while remapping
[2:55] it to fit the displacement range I needed.
[2:59] I am also adding some bump to it, a distorted noise.
[3:05] So the final shader, I am using the yellow color mix for both albedo and subsurface, which
[3:12] is said to a small scale, this will always depend on the size of your scene of course.
[3:17] So yeah that's basically it, nothing too impressive, but I thought that this might be useful
[3:22] to you, let me know.
[3:24] Don't forget you can grab the full scene on Patreon, and thank you for watching, see
[3:29] you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/frame_000.jpg
- [0:50] tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/frame_001.jpg
- [1:30] tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/frame_002.jpg
- [2:00] tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/frame_003.jpg
- [2:35] tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/frame_004.jpg
- [3:10] tutorials/frames/procedural-fries-with-mtlx-and-karma-xpu/frame_005.jpg

---

## Structured Notes

### Core Technique
A custom UV-planar-projection HDA generates a proximity-based mask so a logo decal (e.g. a McDonald's-style cup) only appears on the front of a cylindrical surface, driven in Solaris by multiplying the texture's alpha against that SOP-computed mask; a separate rim-sharpening detail is achieved by extracting/transferring edge-curve normals and Boolean-shattering a swept ring rather than attempting it in pure procedural shading.

### Summary
A simple custom HDA performs UV planar projection with a point placed at the same position as the projection plane, transferring a proximity-based attribute to the geometry so the decal naturally fades out anywhere not facing the projector — avoiding the logo wrapping onto the back of the cup. In Solaris, a Place2D-style node controls texture scale, the texture's Address Mode is set to **Constant** (not tiled/repeat) so it doesn't repeat around the cylinder, and the texture's alpha is multiplied by the SOP-computed mask (again preventing back-of-model bleed from the planar projection) before using that combined mask as the mix factor between the decal texture and the base red material. A rim/sharpness detail line at the cup's top is achieved by modeling rather than shading: side edge groups (saved during modeling) are used to compute normals along the curves, transferred onto the top edge curve so it can be "picked" (peaked) along the shape, resampled for smoothness, duplicated via Sweep, then Boolean'd in **Shatter mode** to break up the swept ring into the desired jagged detail pattern, with the resulting group stored as the sharpness-driving primitive attribute. The fries shader mixes orange/yellow via a whirling noise for albedo variation, distorts a Unified Noise with a Fractal noise added to position for displacement (duplicated with a different frequency/type and remapped to the needed displacement range), adds bump via another distorted noise, and reuses the same yellow color mix for both albedo and a small-scale subsurface contribution.

### Key Steps
1. **Decal/logo projection mask**: build a small custom HDA doing **UV planar projection**, placing a reference point at the same position as the projection plane and transferring a **proximity-based mask** attribute onto the geometry so the projected decal naturally fades where it shouldn't appear (e.g. the back of a cylindrical cup).
2. In Solaris, control decal scale via a Place2D-style node; load the texture and set its **Address Mode to Constant** so it doesn't tile/repeat around the surface.
3. Multiply the texture's alpha by the SOP-computed mask attribute (again preventing the decal from bleeding onto the back).
4. Use the combined mask as the **mix factor** between the decal texture and the base color material.
5. **Rim detail (modeled, not shaded)**: extract the side edge groups saved during modeling, compute normals along those curves, and transfer them onto the top edge curve so it can be Peaked along the shape's contour.
6. **Resample** the top curve for smoothness, duplicate it with a **Sweep**, then use a **Boolean set to Shatter mode** to break the resulting swept ring into the jagged detail pattern; store the resulting group as a primitive attribute driving the sharpness look.
7. **Fries shader — albedo**: mix orange and yellow using a whirling noise; use a second noise to mix in additional yellow-shade color variation.
8. **Displacement**: distort a Unified Noise by adding a Fractal noise to its position input (VOP-style); duplicate the noise setup with a different frequency/type, add the two together, and remap to fit the target displacement range.
9. Add **bump** via a separately distorted noise.
10. **Final shader assembly**: reuse the same yellow color-mix network for both albedo and a small-scale subsurface scattering contribution (SSS scale depends on overall scene scale).

### Houdini Nodes / VEX / Settings
Custom HDA (UV planar projection + proximity mask), Place2D-style scale control, MaterialX texture node (Address Mode: Constant), alpha/mask multiply + mix, Attribute Transfer (curve normals), Peak (contour-following pick), Resample, Sweep, Boolean (Shatter mode), primitive attribute (sharpness group), MaterialX Noise nodes (whirling/turbulent for albedo mix), Unified Noise + Fractal noise (position-distorted displacement), noise duplication + Remap (displacement range), bump-mapping noise, Standard Surface shader (albedo/SSS shared color mix).

### Difficulty
Intermediate (the planar-projection mask HDA and modeled-rim-detail workaround are the standout non-obvious techniques; the shader itself is a straightforward noise-mixing setup).

### Houdini Version
20.5.331 (visible in viewport title bar).

### Tags
materialx, karma-xpu, hda, decals, vex, boolean, displacement, food, product-viz

---

## Related Tutorials
- [Procedural assets and shading with Houdini and MaterialX](procedural-assets-and-shading-with-houdini-and-materialx.md) — related MaterialX food-shading technique (bananas) from the same channel.
- [Procedural Tips: Flow Maps, RBD Emit and more](procedural-tips-flow-maps-rbd-emit-and-more.md) — shares product-viz shading tricks (COPs-driven textures) in a similar drink/food-glass context.
