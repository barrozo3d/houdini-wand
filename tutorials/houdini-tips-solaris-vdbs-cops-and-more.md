---
title: Houdini tips : Solaris, VDB's , COPS and More
source: YouTube
url: https://www.youtube.com/watch?v=WwwTwtlKm0A
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [solaris, lops, vdb, cops, vellum, vex, compositing, karma, procedural, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini tips : Solaris, VDB's , COPS and More

**Source:** [YouTube](https://www.youtube.com/watch?v=WwwTwtlKm0A)
**Author:** cgside
**Duration:** 7m35s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back in this video I'll share a few tips from compositing to
[0:06] salaries and working with volumes and attributes. I believe you'll get away with
[0:12] something that you didn't know before. Hopefully. So the first one is on how to get
[0:20] these nice thumbnails on your layout asset gallery. As you can see they look
[0:26] just like the the renderer image. And the way you do that you set up your
[0:32] component builder and then in the component output you go to thumbnail and you
[0:41] choose render in this case I am using camera XPU and camera and scene I'm
[0:48] choosing the second inputs and I input a light a camera and the render settings.
[0:54] In this case I needed to increase the refraction limit so I can see well the
[0:59] glass. So that's basically it and now you have these nice thumbnails that you
[1:07] can layout as you can see that I'm doing in here. So now I have these geometry,
[1:20] these chocolates and I want to transfer an attribute while doing a VDB
[1:25] conversion. So as you can see I have the attribute in here called mask is for the
[1:31] interior of the chocolate and then I'm doing a conversion to VDB so I can
[1:40] smooth out the shape and I still have the attribute as you can see. And the way
[1:49] you do that is on your VDB from polygons your pass surface attribute in this
[1:56] case is called point dot mask and I give it a name then I do my VDB
[2:04] operations and use a attribute from volume connecting the second input to the
[2:10] volume and I just paste the attributes and give it a name. Keep in mind if you
[2:22] import these into salaries it will be a tree float so if you want to use it for
[2:30] shading you will need to separate them into different components to use as a
[2:36] mask. So I created these lemon slice from boolean as you can see in here I just
[2:48] have this geometry and boolean out sphere and I get something like this then
[2:57] I'm blasting one of them and creating a attribute with the group created from
[3:03] the boolean the groups and now I want to quad rematch it but you know we
[3:10] lose the attributes so what we can do is an attribute transfer but if I do it
[3:18] with default settings without the subdivision I get some weird results so what
[3:27] we can do is before the attribute transfer subdivide your geometry the more
[3:33] you subdivide or at least at until some points you'll get way better result and
[3:41] we can just attribute blur and we get the correct attributes then we can
[3:51] split it and do the UVs and we wind up with this more clean geometry so now a
[4:06] very quick tip on how to do vignetting in cops basically you create a let me
[4:15] start from scratch you create a ramp you'll get something like this then you
[4:22] have you need to set the same resolution as your input image so what we can do
[4:29] is to steal from the input image by connecting the input now we have the
[4:37] correct resolution and then you go to concentric and in this case I want to
[4:48] invert it so white and black and you can play with the interpolation this
[4:57] case I chose is out and then you can just that's what I have in here then you
[5:04] can just multiply over your render and you get the vignetting effect you can
[5:10] also play with the color of your ramp so you get more or less darkening so yeah
[5:21] that's basically it so I created this buff with valum with some collisions
[5:31] into the initial geometry and right here I am mixing between the valum result
[5:40] which is a bit all over the place and I'm using the the initial geometry before
[5:50] the valum simulation and mixing it mixing the position with the valum geometry
[5:59] and the way I'm doing that is just by in a point of op connect the valum geometry
[6:07] and input geometry and I also have an attribute in here called mask let's see
[6:15] that I'm creating with just an attribute creates and then blurring it by
[6:23] sampling the points of the spheres that I have on the object then I'm creating
[6:32] the mask and blurring it and then in the point of op let me just disable this
[6:39] in the point of op I am mixing between the first input position and the
[6:46] second input position and as a mixed factor I'm using that mask as you can see
[6:53] and I'm also playing with the falloff so I can get these effects these wrinkles but at the same time
[7:04] flattening the valum results as you can see is a bit too much so this way I can flatten
[7:15] these areas and keep the wrinkles so yeah guys that's basically it feel free to
[7:25] grab the files from my Patreon and thank you everyone that joined so far see you
[7:32] next time



---

## Captured Frames

- [0:25] tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/frame_000.jpg
- [1:20] tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/frame_001.jpg
- [2:45] tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/frame_002.jpg
- [4:15] tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/frame_003.jpg
- [6:00] tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/frame_004.jpg

---

## Structured Notes

### Core Technique
Five varied tips: generating true rendered thumbnails for Solaris **Component Builder** assets (instead of a viewport snapshot), carrying a point attribute (`mask`) safely through a **VDB From Polygons → Attribute From Volume** round-trip (with a Solaris shading caveat about vector-vs-float unpacking), recovering lost attributes after a **QuadRemesher** pass via pre-subdivision + Attribute Transfer + Blur, a quick **COPs vignette** built from a ramp matched to the render's resolution, and mixing pre/post-**Vellum** simulation positions via a mask to selectively flatten unwanted wrinkles while keeping desired ones.

### Summary
**Component thumbnails:** in a Component Builder's **Component Output**, the Thumbnail section can be set to actually **Render** (rather than a plain viewport capture) using Karma XPU — feeding it a "camera and scene" second input (a dedicated light, camera, and render settings) produces asset-gallery thumbnails that look identical to a real render; for glass/transparent shaders, the render settings' **refraction limit** needs raising so the thumbnail reads correctly through glass. **VDB attribute round-trip:** to smooth a shape via VDB conversion (e.g. rounding a chocolate bar) while preserving a point attribute that marks the interior (a `mask` attribute), **VDB From Polygons**'s "Pass Surface Attribute" field is set to the attribute (`point.mask`, given an output name), the usual VDB smoothing/reshaping operations run as normal, and afterward **Attribute From Volume** (second input connected to the smoothed volume) copies the value back onto the resulting polygon mesh by name — a caveat: when imported into Solaris, this attribute arrives as a **vector/tuple float**, so it must be split into separate float components before it can be used as a shading mask. **QuadRemesher attribute loss fix:** for a Boolean-cut lemon slice where a group-derived attribute needs to survive a QuadRemesh pass (which otherwise discards/scrambles it), running **Attribute Transfer** at default settings directly after the remesh gives poor/noisy results — the fix is to **Subdivide the geometry first** (subdividing further generally gives cleaner transfer results, more subdivision = better accuracy up to a point), then run the Attribute Transfer, then clean up residual noise with an **Attribute Blur** — producing a clean quad-remeshed mesh with intact attributes, ready for splitting and UVing. **COPs vignette:** build a **Ramp** COP, match its resolution to the actual render by connecting/"stealing" the input image's resolution, set the ramp mode to **Concentric**, invert it (white-to-black rather than black-to-white) and choose an interpolation mode (e.g. "Ease Out") for a natural falloff curve; multiply this ramp over the render for the vignette effect, and vary the ramp's color stops to control how dark/colored the vignette darkening reads. **Selective Vellum wrinkle flattening:** for a Vellum-simulated cushion/pillow-style object colliding against initial geometry, the raw sim result can look "a bit all over the place"; the fix mixes the **pre-simulation (rest) geometry's position** with the **post-simulation Vellum result's position** using a **Point VOP**: the pre-sim geometry feeds input one, the Vellum result feeds input two, and a **mask attribute** (built via Attribute Create, sampled/blurred from the positions of reference spheres on the object) drives a position **mix/lerp** between the two, with falloff tuning to control how much of the simulated wrinkling shows through versus how much gets flattened back toward the rest shape — letting the artist selectively keep desired wrinkles while flattening unwanted deformation elsewhere on the same mesh.

### Key Steps
1. **Render-based Component thumbnails:** in Component Builder, set **Component Output → Thumbnail** to Render mode using Karma XPU; feed a "camera and scene" input containing a dedicated light, camera, and render settings so the generated thumbnail matches a true render rather than a plain viewport grab.
2. **Fix glass thumbnails:** if the thumbnail subject includes glass/transparent shading, raise the render settings' **refraction limit** so the material reads correctly in the small thumbnail render.
3. **Preserve a point attribute through VDB conversion:** on **VDB From Polygons**, set "Pass Surface Attribute" to the attribute you want carried through (e.g. `point.mask`), giving it an output name.
4. **Recover the attribute post-VDB:** after VDB smoothing/reshaping operations and converting back to polygons, use **Attribute From Volume** (second input wired to the processed volume) to copy the named attribute value back onto the resulting mesh.
5. **Solaris shading caveat:** when importing a volume-derived attribute like this into Solaris, it arrives as a **vector/tuple float** — split it into individual float components before using it as a shading mask input.
6. **QuadRemesher attribute-loss fix — subdivide first:** before running Attribute Transfer to recover a group-derived attribute lost during QuadRemesh, **Subdivide** the geometry — increasing subdivision level generally yields progressively cleaner Attribute Transfer results (more subdivisions = better up to a point of diminishing returns).
7. **Attribute Transfer + cleanup:** run **Attribute Transfer** on the subdivided mesh (default settings without subdivision give noisy/weird results, hence step 6), then apply **Attribute Blur** to smooth out any residual transfer noise, yielding clean per-point attributes ready for splitting/UVing.
8. **COPs vignette base:** create a **Ramp** COP; match its resolution to the actual render by connecting the render/input image so the ramp "steals" the correct resolution automatically.
9. **Shape the vignette falloff:** set the Ramp's mode to **Concentric**, invert it (white background, black/dark center-to-edge falloff or vice versa as needed) and choose an interpolation type (e.g. "Ease Out") for a natural-looking falloff curve; adjust the ramp's color stops to control vignette darkness/tint.
10. **Apply the vignette:** **Multiply** the shaped ramp over the render output for the final vignetted image.
11. **Vellum sim + reference mask setup:** run a Vellum simulation with collisions against the object's initial (pre-sim) geometry; build a **mask attribute** via Attribute Create, sampling/blurring based on the positions of reference spheres placed on the object to mark which regions should retain wrinkling vs. flatten.
12. **Mix pre/post-sim position via Point VOP:** wire the pre-simulation (rest) geometry into input one and the Vellum-simulated result into input two of a **Point VOP**; use the mask attribute as the mix/lerp factor between the two positions.
13. **Tune falloff for selective flattening:** adjust the mix's falloff shaping so wrinkles show through fully in masked (wanted) regions while unwanted deformation elsewhere on the mesh gets pulled back toward the flat, pre-simulation rest shape.

### Houdini Nodes / VEX / Settings
Solaris: Component Builder, Component Output (Thumbnail: Render mode, Karma XPU, camera-and-scene second input), Render Settings (refraction limit). SOPs: VDB From Polygons (Pass Surface Attribute field), VDB smoothing/reshaping ops, Attribute From Volume (second-input volume reference), Boolean, Blast, group-derived Attribute Create, Subdivide (pre-Attribute-Transfer quality step), Attribute Transfer, Attribute Blur, Split, UV tools, Vellum Solver (collisions against initial geometry), Attribute Create (mask, sphere-position sampling + blur), Point VOP (two-input position mix/lerp driven by mask attribute, falloff tuning). COPs: Ramp (Concentric mode, invert, interpolation type e.g. Ease Out, resolution stolen from input image), Multiply.

### Difficulty
Intermediate — each tip is a compact, practical fix; the Solaris vector-attribute unpacking caveat and the subdivide-before-transfer QuadRemesh workaround are the most non-obvious details.

### Houdini Version
20.5 (Solaris Component Builder/Karma XPU and Copernicus workflow consistent with Houdini 20.5-era tools).

### Tags
#solaris #lops #vdb #cops #vellum #vex #compositing #karma #procedural #tips #intermediate

---

## Related Tutorials
Cross-link with cookies-and-chocolate-modeling-shading-and-sim.md (same author, same chocolate-bar VDB-attribute workflow) and houdini-and-karma-tips-and-tricks.md (shares the render-tips/thumbnail format) once indexed together.
