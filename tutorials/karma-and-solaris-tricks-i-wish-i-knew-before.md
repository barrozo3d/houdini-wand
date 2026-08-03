---
title: Karma and Solaris Tricks I wish I knew before
source: YouTube
url: https://www.youtube.com/watch?v=fbRhHne8x4E
author: cgside
ingested: 2026-07-30
houdini_version: "Not specified (Solaris/LOPs + Karma, recent H19.5+ era UI)"
tags: [karma, solaris, lops, lighting, texture-projection, look-at-constraint, color-management, substance-painter]
extraction_status: complete
frames_dir: tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Karma and Solaris Tricks I wish I knew before

**Source:** [YouTube](https://www.youtube.com/watch?v=fbRhHne8x4E)
**Author:** cgside
**Duration:** 6m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Karma, Rainport, E2V, IntrinsicQV coordinates, UnV, X and Y, U-Inverted, Minimum Output, X and Y, MirrorEffect
[0:27] Y, Minimum Output, BOTH, 1 to 0, 1 to 1, SIGNASLIDER
[0:41] From here you can put it all together into an HDA and sell it on GANROTE.
[0:46] So in this one I want to show you how you can use a light to project textures in Solaris or using Karma.
[0:53] So as you can see I'm projecting a texture using this light.
[0:56] And of course you can set the contribution of the light of the diffuse and specular to 0 so it doesn't affect your scene.
[1:03] In this case I'm just using flat shading, but yeah.
[1:06] So you start with the light, you position it and then in a wrangle you can extract the local transform using the primitive path that you place in here.
[1:14] In this case I'm using light's light1 and then you set the prim var in this case I'm naming it X-Form and I'm saving that matrix which means that now in my light I should have a prim var called X-Form.
[1:33] No sorry, I'm targeting in here another primitive which is my mesh where I want to receive the projection.
[1:39] So if we come in here we should see somewhere, here it is, prim var X-Form.
[1:44] You can name it wherever you want.
[1:46] Then it comes the shading part which is a bit more complex, maybe there are easier ways but it's not that difficult.
[1:52] So we start with position, so this is just the position attribute in object space.
[2:00] Then we import the matrix in here with a prim var reader, so we import the X-Form that is in our mesh.
[2:06] Then we transform the position into the local space of the light by inverting the matrix and doing a transform matrix.
[2:15] So now the position attribute is on the light's local transform if that makes sense.
[2:22] And from here we just create a square mask by separating both the X and Y and manipulating it to a mask.
[2:34] So like this.
[2:36] And then of course this is projecting on both sides so what we can do is take the normal,
[2:41] do the same, extract the Z-axis of the matrix, the Z-component and do a dot product between that and the normal.
[2:49] So we get this sort of mask.
[2:52] Then we can tighten the mask with an if greater and finally multiply it with a square mask.
[2:58] And now we have a perfect mask for our texture sampling which we will do next by combining the X and Y components of the transform position.
[3:07] And then we just fit it to be on the correct spot.
[3:10] And if we sample the image, in this case I'm just using the default button fly, and then we can just mix it with another color in the background.
[3:19] And from there you can just place your light wherever you want and the projection will follow and works in XPU and also in CPU as you can see.
[3:28] Of course it won't work while in the viewport because we are dealing with matrices and what not.
[3:33] Well at least it doesn't work on my viewport but you can test it on your own.
[3:38] So this is just an excuse to not buy my texture projection tool so you can use this workflow.
[3:44] So this is how you can make your light look at any object in the thin, any hero object.
[3:49] So as you can see I have this light and I'm constraining it to my hero object which is the rubber toy.
[3:55] And I can place it on top, on bottom and move it around really easily.
[3:59] And the way I'm doing that, so I'm just importing the rubber toy, then I'm creating the light and I move it wherever I want.
[4:06] Then with the look at constraint I set my look at to the rubber toy and then my source to the light.
[4:12] So I'm just setting the source and the look at primitives or the target primitives.
[4:16] Then you can set the orientation, you can set the axis to look at, in this case minus Z, and then the up axis.
[4:24] And the up back is the Y axis. So I hope that makes sense.
[4:27] And then you just place your light wherever you want and that's how you can constrain the light to a hero object.
[4:34] So a quick tutorial to substance where I was painting some textures.
[4:38] And I was using the ACS workflow because you know, the NEI'm also using ACS and I want to render there.
[4:44] So in my project settings I started with the open color IO as color management and ACS 2.0.
[4:50] The other are the default ones.
[4:52] Then in order to, I was having some trouble where the color of the textures wouldn't match.
[4:57] So what I did in the end is when I export the textures I created a custom template and made sure I include, so...
[5:05] As you can see in here I didn't have the color space variable and you can enable those in here.
[5:11] So you can append and also if you're using Yudim workflow you want also to append the Yudim tag.
[5:17] So, but the most important is the color space because that will make sure we append the suffix called ACCG or RAW or any other sRGB or something like that.
[5:27] And when we export them and report them into Rodini, as you can see we have that tag.
[5:34] And if we go to color preferences, OCIO, as you can see any pattern that matches ACCG or sRGB or in this case RAW.
[5:46] We'll have the correct color space because this one in here doesn't seem to do anything.
[5:51] So you have to rely on the names on your textures on these tags.
[5:55] So that's how you can match your colors from substance into karma.
[6:00] So as always thank you for watching guys. These were the tips that I wanted to share today.
[6:04] I hope you have learned something new and you can grab the files on my Patreon also if you're interested.
[6:10] And yeah, thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:53] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_000.jpg
- [1:14] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_001.jpg
- [2:34] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_002.jpg
- [3:19] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_003.jpg
- [3:55] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_004.jpg
- [4:16] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_005.jpg
- [5:05] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_006.jpg
- [5:46] tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/frame_007.jpg

---

## Structured Notes

### Core Technique
Three independent Solaris/Karma production tricks: (1) projecting a texture from a light's local space onto arbitrary geometry using a hand-built matrix-transform + masking VEX/VOP network, (2) constraining a light to always aim at a "hero" object via a Look At Constraint LOP, and (3) matching Substance Painter-exported texture colors correctly in Karma by tagging exported files with explicit OCIO color-space suffixes.

### Summary
A rapid-fire tips video (no chapters, ~6 min) from cgside covering three separate Solaris/Karma workflows he wishes he'd known earlier. Trick 1 (0:46-3:44) builds a from-scratch light-based texture projector: extract the light's world transform into a primitive var via a wrangle, read that matrix on the target mesh, transform the mesh's object-space position into the light's local space, build a square mask from the local X/Y bounds, cull the back face with a normal·lightZ dot product, then use the local X/Y as UVs to sample an image and composite it over a background color — the projection follows the light in real time and works in both XPU and CPU (but not in the viewport, matrix math isn't previewed live there). Trick 2 (3:44-4:34) uses Solaris's Look At Constraint LOP to keep a light always oriented at a chosen "hero" object as you freely reposition the light — set Source to the light primitive, Target to the hero-object primitive, pick the look-at axis (he used -Z) and the up axis (Y). Trick 3 (4:34-6:00) fixes texture color mismatches between Substance Painter and Karma: set Substance's project color management to OpenColorIO / ACES 2.0, then create a custom export template that appends a color-space suffix tag (e.g. ACEScg, RAW, sRGB) to each exported filename (and a UDIM tag if using UDIMs) — Houdini/Karma's OCIO texture color-space auto-detection matches those filename suffixes, so without the tag the color space silently falls back to a default and colors look wrong.

### Key Steps
**Light texture projection:**
1. Position a light (e.g. a rectangle/area light) so it faces the target geometry; set its diffuse and specular contribution to 0 so it doesn't otherwise light the scene, and use flat/unlit shading on the receiver for a clean preview.
2. On the light primitive, add an Attribute Wrangle that reads the light's world transform via `primintrinsic` and writes it out as a primitive var (named e.g. `xform`) — this bakes the light's position/orientation into a matrix attribute other nodes can read.
3. On the receiving mesh, add a Primvar Reader (or equivalent) targeting the light primitive to pull in that same `xform` matrix primvar.
4. In a VOP/wrangle network: read `P` (object-space position), invert the imported light matrix, and transform `P` by the inverted matrix — this re-expresses each surface point's position in the light's local space.
5. Build a square mask by splitting the transformed position into X and Y and remapping/clamping each into a 0-1 falloff band (fit range), multiplying X-mask × Y-mask.
6. Build a backface mask: extract the Z-axis/basis vector of the light's matrix, dot it against the surface normal, and threshold with an "if greater" comparison so the projection only appears on the light-facing side.
7. Multiply the square mask by the backface mask to get the final projection mask.
8. Use the local-space X/Y (from step 4) as UV coordinates to sample the projected image texture, then mix that sampled color with a base/background color using the combined mask as the blend factor.
9. Result: moving the light anywhere in the scene moves the projected texture with it, live, on both CPU and XPU Karma — but the effect won't preview inside the 3D viewport itself since it depends on evaluated matrix math, not native viewport projection.

**Light Look At Constraint:**
1. Import the hero object and create/position the light as normal.
2. Add a Look At Constraint LOP; set its Source primitive path to the light and its Target (look-at) primitive path to the hero object.
3. Choose the axis that should point at the target (creator used -Z) and the up axis (Y) for correct roll orientation.
4. The light can now be freely translated anywhere and will continuously re-aim itself at the hero object.

**Substance Painter → Karma color matching:**
1. In Substance Painter's project settings, set Color Management to OpenColorIO with the ACES 2.0 config (leave other settings default).
2. When exporting textures, build/use a custom export template that includes the Color Space filename variable (append it to the output filename), and also append the UDIM tag if the project uses UDIM tiling.
3. This produces exported filenames carrying a color-space suffix (e.g. `_ACEScg`, `_RAW`, `_sRGB`).
4. In Houdini, when the textures are referenced (e.g. via a texture/material node), check Color Preferences → OCIO: Houdini auto-detects color space from filename patterns matching tags like ACEScg/sRGB/RAW — with the tag present the correct space is assigned automatically; without it, the default assignment is wrong and colors won't match Substance's preview.

### Houdini Nodes / VEX / Settings
Solaris/LOPs context throughout. Attribute Wrangle (`primintrinsic` transform extraction, primvar write), Primvar Reader (matrix import on receiving mesh), VOP network for: invert-matrix + transform-position, Separate/Fit-Range nodes (square mask), dot-product + "if greater" comparison (backface mask), multiply (mask combine), texture sample node using local X/Y as UV, mix/composite node (image over background color). Look At Constraint LOP (Source, Target/Look At primitive paths, Look At Axis, Up Axis parameters). Houdini Color Preferences → OCIO panel (pattern-matches filename color-space suffixes like ACEScg/sRGB/RAW).

### Difficulty
Intermediate/Advanced — the texture-projection network (trick 1) requires comfort with matrix math, primvars, and VOP wrangling; the Look At Constraint and Substance/OCIO tricks are Beginner/Intermediate parameter-level workflow fixes.

### Houdini Version
Not specified on screen; Solaris (LOPs) + Karma XPU/CPU workflow consistent with a recent H19.5+ release.

### Tags
karma, solaris, lops, lighting, texture-projection, look-at-constraint, color-management, substance-painter

---

## Related Tutorials
- [a Full Houdini Mini Course - RBD Marbles [All Lessons]](a-full-houdini-mini-course---rbd-marbles-all-lessons.md) — shares `karma`, `solaris`, `lop`; that course's Lesson 10-12 look-dev/lighting sections (LPE-tagged multi-light setup, barn-door spotlight shaping) pair well with this video's Solaris/Karma lighting tricks.
