---
title: Bake room maps in karma from HDRI interiors H20
source: YouTube
url: https://www.youtube.com/watch?v=6hbyMIxU1oI
author: cgside
ingested: 2026-07-13
houdini_version: "H20 (Karma XPU)"
tags: [karma, lighting, hdri, materials, solaris, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Bake room maps in karma from HDRI interiors H20

**Source:** [YouTube](https://www.youtube.com/watch?v=6hbyMIxU1oI)
**Author:** cgside
**Duration:** 5m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna show you how you can
[0:04] take an interior like this and interior scene you can have geometry in here
[0:10] but in this case I'm just projecting an HDR interior to the geometry and then I
[0:20] can bake it to a texture to a cube map let's say or an interior map and then
[0:35] we can apply it to some geometry and we would get something like this this
[0:43] parallax effect. So let's see how it's done. I'm starting with a subcreate
[0:52] creating a box and we will need to subdivide it otherwise we will get this
[1:02] distorted projection as you can see. So place a sub divide in violinier mode in
[1:11] this case is a very simple interior but you can elaborate more. Then I'm
[1:17] reversing the normal so I can see the interior by taking remove back faces.
[1:25] Then I am your view projecting and at the same time using a quickshade with my
[1:33] HDR so I can see the result and I can manipulate the rotation and play also
[1:46] with the box scale to see where it fits better as you can see. It's really easy
[1:55] to do this kind of image-based modeling and I have an output in here called Geo and
[2:09] from there I'm creating a material library with an unlead surface and just a
[2:15] material like the image loading my HDR and this step is really important
[2:22] otherwise you will get a lot of grain in your final image. So then I'm creating
[2:30] a camera and setting the view is just default 000 to position and in the view I'm
[2:38] setting the aspect ratio to 1 to 1 since I want to render a square texture and
[2:44] in the karma tab I'm using a lens shader that you need to create inside a
[2:50] matte network, a material network as you can see in here. So then in the
[2:57] caramel room lens shader in the different variables here the X-min, Y-min, Z-max,
[3:07] I'm inputting the bounding box and the corresponding bound so the X-min, the X-max
[3:17] and so on and also adding a very small value of offset you will need to play
[3:24] around to see where it lands the perfect result because sometimes you get some
[3:33] noise and you also need to increase a bit the samples to get rid of some of
[3:39] that noise. So then if you render you will have a perfect or near perfect room map.
[3:52] And finally you can create a plane and attach the room map frame just default
[4:01] settings create a material and attach the room map that we rendered and the
[4:11] corresponding attributes, room beat, engine view, engine view and that's about
[4:20] it you have your room map working as you can see. We have the ceiling and the walls,
[4:32] the floor. In this case I didn't use a square grid to render to a geometry to
[4:46] render this effect because otherwise I would get stretching so what I did was
[4:55] in the sub-create on the grid I loaded as a spare input my geometry my original
[5:01] geometry where I projected the HDRI and used the bounding box size Z-x and Y so it
[5:10] creates a similar ratio to the original geometry but you don't need to do that
[5:19] because I was getting some stretching in some areas and this is better this way
[5:27] but you can totally make it square and from distance this looks pretty convincing.
[5:36] So yeah you can grab the file on my Patreon and thank you everyone that joins
[5:43] so far and I will see you soon thank you.



---

## Captured Frames

- [1:11] tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/frame_000.jpg
- [2:22] tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/frame_001.jpg
- [2:50] tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/frame_002.jpg
- [3:52] tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/frame_003.jpg
- [4:32] tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/frame_004.jpg

---

## Structured Notes

### Core Technique
Projects an HDRI interior panorama onto simple room-shaped geometry, then bakes that projection into a flat "room map" texture using a custom Karma lens shader — producing a cheap, parallax-correct fake-interior texture that can be applied to any flat plane (a classic fake-interior/room-cube-map technique).

### Summary
Starts from a subdivided box standing in for a room, projects an HDRI panorama onto its interior faces (viewing it via UV Project + Quick Shade to preview and adjust rotation/box scale interactively), then renders that projected interior through a custom Karma lens shader HDA to bake it into a square texture — a "room map." Applying the resulting room map texture to a flat plane (with the correct camera-relative UV attributes) reproduces a convincing parallax fake-interior effect from a distance, at a fraction of real interior geometry's cost.

### Key Steps
1. Create a **Box**, then **Subdivide** it (Linear/uniform mode) — subdividing is required or the HDRI projection will be visibly distorted.
2. **Reverse Normals** (or use Remove Backfaces) so the interior faces are visible from inside the box.
3. **UV Project** the box (e.g. camera/perspective-style projection) and preview it live with **Quick Shade** using the target HDRI — interactively adjust the projection's rotation and the box's overall scale until the interior "reads" correctly from the intended viewing angle.
4. Build a **Material Library** with an **Unlit Surface**/Unlit Image shader loading the HDRI texture directly — using an *unlit* shader here is called out as important, otherwise the final baked render picks up extra noise/grain from lighting response.
5. Create a **Camera** at the origin (default 0,0,0), set its **aspect ratio to 1:1** (since the output is a square texture map).
6. In the camera's Karma tab, assign a **Lens Shader** — this must be authored as its own small node network inside a **Material Network** (a Lens Shader HDA/VOP subnet), not a normal surface shader.
7. Inside that lens shader network, wire in the box's **bounding box min/max (X/Y/Z)** as parameters, plus a small **offset** value — tune the offset empirically since incorrect values introduce visible noise/artifacts in the bake.
8. Increase **render samples** as needed to clean up remaining noise in the baked result, then render — this produces the near-final "room map" image.
9. To use the result: create a **Grid/Plane**, build a material assigning the baked room-map texture, and wire in the matching **room-map camera/view attributes** (so the shader knows the original camera-relative projection) — this reproduces the ceiling/wall/floor parallax illusion on a flat surface.
10. To avoid stretching on the destination geometry: instead of using a plain square grid, load the *original* projected geometry as a spare input on the destination grid and derive its X/Z or X/Y bounding-box ratio to set the grid's aspect — a perfectly square grid caused visible stretching in some areas for the presenter, so matching the source geometry's proportions gave a cleaner result (though a square grid still "mostly" works from a distance).

### Houdini Nodes / VEX / Settings
Box → Subdivide (Linear) → Reverse Normals/Remove Backfaces → UV Project + Quick Shade (HDRI preview) → Material Library (Unlit Surface/Unlit Image, HDRI texture) → Camera (aspect ratio 1:1) → custom **Lens Shader** built inside a Material Network / VOP subnet (bounding-box min/max X/Y/Z inputs + offset parameter) → Karma render settings (increased samples to reduce noise) → destination Grid/Plane with room-map material + matching room-map/camera-view attributes; optional bounding-box-ratio-matched grid to avoid stretching.

### Difficulty
Intermediate — the room-shape/HDRI-projection part is simple, but building and correctly wiring a custom Karma lens shader HDA with bounding-box-driven parameters requires some Solaris/Karma material-network familiarity.

### Houdini Version
Houdini 20 (Karma XPU render engine, Solaris/USD-based material network for the custom lens shader).

### Tags
#karma #lighting #hdri #materials #solaris #product-viz #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers custom Karma lens shaders or room-map/fake-interior baking — cross-link with any future Karma material or HDRI-lighting tutorials once extracted from this batch.
