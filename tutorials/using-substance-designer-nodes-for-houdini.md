---
title: Using Substance Designer nodes for Houdini
source: YouTube
url: https://www.youtube.com/watch?v=ObBXMX-VH90
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.734"
tags: [heightfields, substance-designer, third-party-plugin, pegasus, vex, texturing, rocks, karma]
extraction_status: complete
frames_dir: tutorials/frames/using-substance-designer-nodes-for-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Using Substance Designer nodes for Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=ObBXMX-VH90)
**Author:** cgside
**Duration:** 8m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I wanted to show you how I used the
[0:05] new Substance Designer textures for our DNA by Powell Kaboosh to create this
[0:12] sort of rocky material and also combine it with the Pegasus nodes to create some
[0:20] textures. So from the beginning I'm starting with the shape from the circle, from
[0:29] the circle, then extruding it, exactly one unit to have the full range when I
[0:35] connect it to the Substance Designer texture, promoting the extrude front
[0:41] group and fusing and placing it on the positive X. So when I connect it it will
[0:53] be aligned with the Substance Designer texture. You can see if I have it as
[0:59] height, I will have this sort of shape but I want it as a grayscale. Then I have
[1:09] gradients with Substance Designer tile sampler and then I just blend it. We
[1:19] can move it to a minimum. Then using a tile sampler and here is where you
[1:28] will increase the repetition and play a lot with the offset random disorder and
[1:35] random amplitude and scale and also introduce some rotation. As you can see I
[1:44] have set it to input pattern and connected to the second input. Then just doing
[1:51] an auto-levels and I can show you how it looks. So if I connect it to the
[1:58] visualization node, the height visualization, this is the current setter. So doing
[2:07] an auto-levels, then I am wrapping a bit the texture and you can see what
[2:18] that is doing. Then doing a blend to carve a bit the shapes. So with a
[2:31] Berlin levels and doing a blend set to a minimum and you can see I can carve more or less.
[2:46] Then doing an overall rope as you can see by using a Berlin and in this case playing
[2:59] with the angle and in here I'm doing another plans to create the surface details
[3:12] by using a Voronoise set to crystal and a Berlin in a sloppler and then just
[3:22] blend it set to minimum and reducing the opacity to have these sorts of effects.
[3:28] Then just doing another sloppler in here to create even more variation let's say
[3:39] with a Berlin. So that's our id map. Now in order to use id field nodes since we are
[3:50] in a very small scale and a different orientation we will need to rotate this shape, this volume
[3:59] or this id field and scale it up quite a bit. So the default scale for the id field is about
[4:07] 1000. So in an id field transform I increase the scale to 1000 and rotate it minus 90 degrees.
[4:17] So in the end we will have something like this around 1000.
[4:24] And now we can use the new Pegasus nodes to load some diffuse and displacement textures and playing
[4:33] oops. And playing with the scale as you can see I love that this mega-scan texture.
[4:47] Then I'm introducing another one if I can show you if I disable the marks this is the
[4:55] the most texture I'm introducing in the cavities and for that I'm using a visualized with the
[5:02] faulty tinting and doing a night field mask by feature set to occlusion. And then I'm just
[5:12] blending the two materials as you can see. Then in order to have a proper range for the id map I
[5:22] am scaling it down again to a size of one. So as you can see I have a size of one
[5:35] and just doing a match size to have it on the center. And I can create a night field output
[5:45] save the texture. And in the channels I'm inputting the RGNB
[5:55] id fields or volumes as you can see for red RGNB. And for the alpha I can use the id so I can save
[6:08] in only one texture. So after you save to this it's pretty fast. In this case I used two K-map.
[6:19] And let's go to salaries. And if you render this I am just loading a simple
[6:29] quad sphere and this is the result of the material. In the texture I'm loading the texture as you
[6:38] can see. In this case I'm just repeating once. And then for the id or for the displacement I'm
[6:46] separating using a separate color for since this is a loaded color for for the alpha channel.
[6:56] And the id will be on the alpha so I'm connecting that to the displacement. If I disconnect it
[7:02] you can see we have no displacement. And for the color I'm just doing some basic color correction
[7:11] and loading also random normal map just to add some surface detail. Hopefully you can see it
[7:19] in the even with YouTube compression. So yeah guys feel free to download these new nodes from
[7:29] the link in the description. I will link the outer page on Github. And if you want this particular
[7:38] file you can also find it on my Patreon. And alongside with dozens of project files and
[7:48] some tutorials, some exclusive tutorials and also some courses in the Patreon shop.
[7:57] Thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:30] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_000.jpg
- [1:30] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_001.jpg
- [2:45] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_002.jpg
- [3:50] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_003.jpg
- [5:00] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_004.jpg
- [6:20] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_005.jpg
- [7:20] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_006.jpg
- [7:50] tutorials/frames/using-substance-designer-nodes-for-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Sculpt a procedural rock shape entirely with a ported **Substance Designer node set for Houdini** (by Pawel Kabus) — Tile Sampler, Blend, Levels, Warp, Slope Blur, Voronoise — operating on a heightfield derived from an extruded circle, then combine it with third-party **Pegasus** nodes to load Megascans diffuse/displacement textures masked by an occlusion-based cavity mask, packing the result into a single RGBA texture for Solaris.

### Summary
The base heightfield comes from a Circle extruded exactly one unit (so its full range maps cleanly onto Substance Designer's 0–1 height convention), with the extrude-front group promoted, fused, and positioned on positive X for correct alignment with the SD texture. A **Tile Sampler** node builds the base rock-facet pattern from gradients, with heavy use of offset/random disorder/random amplitude/scale/rotation parameters, then **Auto Levels** normalizes the range. A second Tile Sampler pass (input pattern mode) adds warping distortion, followed by a **Blend** set to Minimum to carve additional shape into the facets, using a **Levels** node to control how much carving occurs. A rope/overlay detail layer uses another **Warp** node with angle control, and surface micro-detail comes from a **Voronoise** node set to Crystal type blended with Perlin via a **Slope Blur**, then Blend (Minimum, reduced opacity) for a subtle cavity-like effect; a further Slope Blur pass adds more variation — together forming the "ID map." Since heightfield nodes operate at a much larger default scale (~1000) and different orientation than this small-scale SD network, a **Heightfield Transform** rescales to ~1000 and rotates -90°. **Pegasus** third-party nodes then load Megascans diffuse/displacement textures (scale-adjustable), with a second material introduced specifically for cavity/crevice detail using a **Heightfield Mask by Feature** set to Occlusion, blended between the two materials. The ID map is scaled back down to size 1 (Match Size, centered) so it has a proper 0–1 range again, then a **Heightfield Output** node packs the RGB channels with the diffuse/volume data and the alpha channel with the ID map, saving a single combined 2K texture — fast to render since it's just one file. In Solaris, a quad-sphere loads this texture: a Separate Color node extracts the alpha channel (the ID/displacement map) for the displacement input (demonstrated by toggling it on/off), with the RGB portion driving base color (plus basic color correction) and a separately-loaded random normal map adding extra surface detail.

### Key Steps
1. Build the base shape: Circle → Extrude exactly **1 unit** (for a clean 0–1 height range matching Substance Designer's convention) → promote the extrude-front group → Fuse → position on positive X for texture alignment.
2. Convert to a heightfield/height representation and connect the ported **Substance Designer Tile Sampler** node, building the initial facet pattern from gradients with heavy tuning of repetition, offset, random disorder, random amplitude, scale, and rotation.
3. Run **Auto Levels** to normalize the output range; add a second Tile Sampler in "input pattern" mode (fed from the first) to introduce warp-like distortion.
4. Use a **Blend** node set to **Minimum** with a **Levels** node beforehand to control how much the pattern "carves" into the shape.
5. Add an overlay/rope detail layer via another **Warp** node, adjusting its angle parameter.
6. Build surface micro-detail: **Voronoise** set to **Crystal** type combined with a **Perlin**-driven **Slope Blur**, then Blend (Minimum, reduced opacity) for a subtler cavity effect; repeat with another Slope Blur pass for additional variation — this combined output becomes the "ID map."
7. **Heightfield Transform**: since ID field/heightfield nodes default to a much larger scale (~1000) and a different orientation than the small SD network, rescale to ~1000 and rotate **-90°** to align them.
8. Load Megascans diffuse/displacement textures via the third-party **Pegasus** node set, adjusting texture scale; introduce a second material for cavity/crevice-specific detail using **Heightfield Mask by Feature** set to **Occlusion**, then blend the two materials together.
9. Scale the ID map back down to size **1** via **Match Size** (centered) so it has a proper normalized range again.
10. Use a **Heightfield Output** node to pack channels into a single texture: RGB channels carry the diffuse/volume material data, and the **alpha channel carries the ID map** — saved as one combined 2K texture for fast, single-file loading.
11. In Solaris, load a quad sphere with this packed texture; use **Separate Color** to extract the alpha (ID/displacement) channel and connect it to the shader's displacement input (demonstrated with before/after toggling); use the RGB portion for base color with basic color correction, plus a separately-loaded random normal map for additional surface detail.

### Houdini Nodes / VEX / Settings
Circle, Extrude (1 unit), Group Promote, Fuse, Substance Designer-ported nodes (Tile Sampler ×2, Auto Levels, Blend — Minimum mode, Levels, Warp ×2, Voronoise — Crystal type, Slope Blur ×2), Heightfield Transform (scale ~1000, rotate -90°), Pegasus third-party nodes (Megascans diffuse/displacement loader), Heightfield Mask by Feature (Occlusion), Match Size, Heightfield Output (RGB + alpha channel packing), Separate Color (alpha extraction for displacement), MaterialX/Karma shader (base color correction, random normal map).

### Difficulty
Advanced (relies on a specific third-party node package (Substance Designer ports by Pawel Kabus) plus Pegasus, and requires understanding heightfield/ID-field scale conventions).

### Houdini Version
20.5.734 (visible in viewport title bar).

### Tags
heightfields, substance-designer, third-party-plugin, pegasus, vex, texturing, rocks, karma

---

## Related Tutorials
- [Houdini Heightfields and Cliffs](houdini-heightfields-and-cliffs.md) — related heightfield-based rock texturing using a different third-party plugin (Pegasus Heightfield Material/Tint) from the same channel.
- [VDB Procedural Cliffs](vdb-procedural-cliffs.md) — alternate non-plugin, pure-VEX approach to similar rock-surface detail.
