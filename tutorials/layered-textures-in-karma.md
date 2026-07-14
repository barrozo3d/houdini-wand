---
title: Layered Textures in Karma
source: YouTube
url: https://www.youtube.com/watch?v=GQMsl6TiFXY
author: cgside
ingested: 2026-07-13
houdini_version: "21"
tags: [karma, materials, shaders, mtlx, triplanar, cops, python, uv, procedural, environment, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/layered-textures-in-karma/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Layered Textures in Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=GQMsl6TiFXY)
**Author:** cgside
**Duration:** 8m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video I wanted to introduce you to a new node I'm releasing for Karma and
[0:05] MaterialX, which is this LayerX node.
[0:09] It's a native MaterialX node, so no subnet or something like that is really I compiled
[0:13] it for MaterialX and Karma, and it allows you to layer different textures over your diffuse,
[0:19] your albedo, your roughness and what not even for displacement.
[0:23] It works.
[0:24] So for example, I have this graphite in here.
[0:25] I can disable or I can change the blending mode to a normal, or in this case I'm going
[0:30] to set it to overlay.
[0:31] We have possibility for alpha blending and you have for example I can enable in your
[0:36] new layer and blend it a bit with the previous ones or change the blending mode.
[0:43] So but yeah, we will be back to this in a minute.
[0:45] Now let's look at the first I wanted to share the initial setup that I did for this
[0:50] scene.
[0:51] So I just don't promote this.
[0:52] I'm going to give you some tips before that.
[0:55] So let's go to the Geocon text.
[1:00] Any near, if you remember we modeled this water tower previously on a video and I wanted
[1:05] to give it some textures.
[1:07] So for just to clean it up a bit, I'm going to delete most of the attributes and I only
[1:15] have normal and UVs.
[1:16] Then I use my HGA to orient the UVs up and do a basic UV layout with these settings.
[1:22] Then I do a connectivity in here.
[1:24] So in this case, I didn't save a name attribute for the different parts and I really need that
[1:29] for shading later.
[1:31] So as you can see here in the trust for example, it has all different pieces and the same
[1:36] for the leather.
[1:37] So what I did in here really quickly was to using the class attributes that I saved on
[1:43] primitives.
[1:44] I'm isolating the different parts just by pressing 9, just by entering this, pressing 9 and
[1:51] selecting by class and then I selected some of them and I'd each section.
[1:57] So the trust, the leather, but for that I also did an exploded view so I can easily select
[2:03] the different parts.
[2:04] Then I disable it and I select everything, including the ceiling, the body and the body
[2:08] B.
[2:09] Now I run a python script that basically looks for all the visibility nodes in the inputs
[2:15] in all the notes in the previous nodes and reads the group parameter and set the data
[2:22] attributes with those values of the group.
[2:25] So something like this.
[2:27] So in here we have an array and in the first element we have the first selection and so
[2:32] on.
[2:33] Then it's easy.
[2:34] We set a new visibility node just to show all the primitives and we set a new class based
[2:39] on that visibility groups array.
[2:42] Basically checking if the current prime number is in the selected group that we are iterating
[2:47] over and assigning the class to a new class that I'm just using the iterator in here.
[2:54] So that's basically it.
[2:55] That's how I'm cleaning up and this can be useful to isolate different parts as we will
[2:58] do in shading.
[3:00] Then I'm just cleaning again some attributes, doing a soft and normal, setting a basic name
[3:05] and outputting the cache.
[3:09] In a copnet I also did something a bit specific because if we are going to procedural
[3:13] shaders in Solaris we don't have access to many nodes like ambient occlusion and
[3:19] be ready dirt for example which is a very useful node in be ready.
[3:22] We don't have that kind of luxury.
[3:24] So it's a good idea to set up a copnet and in this case I'm baking some attributes like
[3:31] ambient occlusion for example as you can see and I can use that in shading so I'm creating
[3:36] an output for the AO but no that I can reference and that way I can use it in Solaris.
[3:43] You could of course output curvature, edge, cavity and all the other maps but for example
[3:47] position and world normal we have that in Solaris so we don't need it.
[3:51] In this case I did a quick and dirty job and I'm just using occlusion and it's not even
[3:56] that noticeable.
[3:58] So that's about it for this setup.
[4:00] Hopefully I run through pretty quickly but you can have a look at the file on Patreon
[4:05] and you will be able to go through more slowly.
[4:10] So let's go through the Solaris.
[4:12] In here I'm just importing the geometry and creating a dome light and some render settings.
[4:19] So for the material let's quickly have a look.
[4:23] So these material X node, the layer X node you can find it.
[4:27] Let me see here on material X and compositing and you will find it here.
[4:30] So it's a native material X node as I told you before and it's pretty simple.
[4:35] So let me disable all these layers.
[4:42] You have, I also have some roughness in here but that's not really that important right
[4:47] now.
[4:48] So besides that we have a base that we can set to a different color and then we can enable
[4:53] a new layer and in this case I'm loading an alpha so you can see in here.
[4:58] I don't have any color.
[4:59] The color is set here so I can set it to a different color for example.
[5:02] But as an alpha I'm loading from a mega scan structure which is this one.
[5:07] I'm loading the texture, doing some color correction and then just playing with the range as
[5:11] you can see.
[5:15] So now I did karma see you sorry.
[5:17] So that's pretty simple.
[5:19] I'm just loading that as an alpha and I can play with the color in here and pick the
[5:23] color I want.
[5:24] So let's say it's this.
[5:26] Then we have another layer.
[5:27] So layer two we enable that and that just goes as color arrest texture in this case from
[5:34] mega scans also and as an alpha I'm using a tri planner which looks something like this.
[5:42] So that's my alpha and we need to restart the render because this visualized node is
[5:47] broken in node in it 21 for some reason.
[5:50] So that's why so we have layer two and of course we can change the planning mode.
[5:54] So for example to overlay or to multiply but since we were using an alpha that's not
[5:59] really that important in here.
[6:01] Then I'm loading in here a grid texture.
[6:04] So let me make that really noticeable.
[6:07] Basically is the let me see where I have that is the grid node.
[6:12] So let's see it's a grid node that I just added some fractal to break out the edges.
[6:18] Then I do I X route only one channel and I multiply it over my class.
[6:24] So in here I'm reading that class that we created converting to a float and doing if equal.
[6:29] So for example I'm comparing to this value in here.
[6:33] So if class two I want to mask around that different section in this case is the class
[6:38] number one.
[6:39] So I'm just outputting white or black depending on the class.
[6:42] So it looks something like this.
[6:43] So I can change in here which section I want to target.
[6:47] And of course I did a pretty simple job in this section with all this information and
[6:51] more cops baking.
[6:52] You can you can elaborate as much as you like.
[6:56] So let's keep enabling this in this case I'm just reading the ambient occlusion in here.
[7:00] So yeah I can actually play with that.
[7:03] So let me make that even more noticeable with the range node.
[7:07] So I'm just reading the ambient occlusion in here.
[7:09] Then we have the graphite.
[7:12] So let me set that to normal and that is in here.
[7:17] So I'm just loading some graphite decals I have I bought on art station and I'm since
[7:23] this is a PNG image with an alpha I'm setting it to color for and using the place node just
[7:28] to place it where I want with the offset and scaling it up or down in this case and making
[7:33] sure I set the address mode you and V2 constant so it doesn't repeat around.
[7:37] Then I'm extracting the alpha in here with a separate color for and using that as an alpha
[7:43] in the layer five as you can see in here hopefully it's visible.
[7:47] Then I'm just multiplying down a bit the alpha since I don't want so much blending so
[7:51] as you can see and you can set that to overlay and play with the alpha so just some post
[7:56] process and we get the sort of result.
[8:00] So yeah guys I'm really thinking this for Patreon if you want to grab it and I'm also
[8:07] releasing this scene there if you want to have a look on how I did all of this setup.
[8:11] Of course this was pretty quick and dirty you can do a much better job but I find these
[8:15] nodes pretty useful if you want to layer up to different textures and effects so let
[8:21] me know your opinions in the comments and I hope to see you next time.
[8:24] Thank you.



---

## Captured Frames

- [0:25] tutorials/frames/layered-textures-in-karma/frame_000.jpg
- [1:20] tutorials/frames/layered-textures-in-karma/frame_001.jpg
- [3:30] tutorials/frames/layered-textures-in-karma/frame_002.jpg
- [4:40] tutorials/frames/layered-textures-in-karma/frame_003.jpg
- [5:40] tutorials/frames/layered-textures-in-karma/frame_004.jpg
- [6:35] tutorials/frames/layered-textures-in-karma/frame_005.jpg
- [7:20] tutorials/frames/layered-textures-in-karma/frame_006.jpg

---

## Structured Notes

### Core Technique
Introducing the author's custom **LayerX** node — a native, compiled MaterialX node for Karma that lets you stack an arbitrary number of texture layers (each with its own blend mode and alpha) directly onto base color, roughness, or displacement without building a manual Mix-node chain — demonstrated by texturing a previously-modeled water tower with rust, dirt-mask Triplanar decals, a class-based section mask, baked ambient occlusion, and a graffiti decal.

### Summary
**The LayerX node itself:** a native (not subnet-based) MaterialX node compiled specifically for Karma, exposing a stack of enable/disable layers, each with its own **blend mode** (Normal, Overlay, Multiply, etc.) and optional **alpha** input for masking — usable on base color, roughness, and even displacement inputs. **Model prep:** starting from a previously-modeled water tower, most attributes are stripped except normals and UVs; the author's own UV-orient-up HDA (built in an earlier video) plus a basic UV Layout clean up the UVs. Since the model wasn't originally saved with per-part `name` attributes (needed for shading masks), **Connectivity** produces a `class` per-piece attribute, and a custom **Python script** automates re-deriving clean shading groups: it walks backward through the network reading every upstream node's selection/visibility group parameter into an array (one array element per manually-made viewport selection, made by pressing 9/entering the geometry and selecting-by-class per section, aided by an Exploded View to separate overlapping parts), then a final wrangle checks whether the current primitive number appears in each array element and assigns a new sequential `class` value accordingly — effectively converting a series of manual viewport selections into a clean, reusable per-section class attribute without hand-authoring group expressions. **COPs pre-baking for Solaris-side shading:** since MaterialX/Karma procedural shaders in Solaris lack convenient node-based helpers like Redshift's Ambient Occlusion or Dirt nodes, a CopNet bakes attributes like **ambient occlusion** onto the model's UV space ahead of time, output via a named node so it can be referenced in Solaris shading; position and world normal don't need separate baking since those are natively available in Solaris already — the author notes this AO bake was done "quick and dirty" and isn't even very noticeable in the final result, but the workflow (bake once in COPs, reference in Solaris) generalizes to curvature, edge, and cavity maps too. **Solaris shading with LayerX:** a base color layer sets an overall tint; **Layer 1** loads a Megascans structure texture as the layer's **alpha** (with its own color picked separately, decoupled from the texture's actual RGB) for a rust/grime overlay; **Layer 2** uses a different Megascans texture as color, masked by a **Triplanar**-projected alpha (avoiding UV-seam artifacts on this particular mask); a **Grid** node (with Fractal noise added to break up its perfectly regular edges) is extracted to a single channel and multiplied against the model's `class` attribute (read, converted to float, and compared via `if (class == N)`) to build a targeted **per-section mask** — letting you isolate and texture one specific structural piece (e.g. one leg, one panel) at a time by changing which class value is compared. Further layers read back the **baked ambient occlusion** from COPs, and a final **graphite/graffiti decal layer** loads a PNG with alpha (Mono/Color4 mode), positioned/scaled via a **Place** node with **address mode set to Constant** on both U and V (so the decal doesn't tile/repeat around the model), extracts its alpha via Separate Color, feeds that as the layer's alpha (with the raw alpha multiplied down since full-strength blending was too strong), and sets the blend mode to Overlay for a subtle, non-repeating decal effect.

### Key Steps
1. **Understand LayerX:** a compiled, native MaterialX node (found under MaterialX → Compositing) exposing a stack of texture layers, each independently enable/disable-able with its own blend mode and alpha input, usable on color, roughness, and displacement.
2. **Clean up model attributes:** strip most attributes from the previously-modeled geometry, keeping only normals and UVs.
3. **Orient and layout UVs:** apply the author's own UV-orient-up HDA (from an earlier video) followed by a basic UV Layout.
4. **Generate a per-piece class attribute:** run **Connectivity** to get an initial per-piece `class`, since the model wasn't originally saved with per-part `name` attributes needed for shading masks.
5. **Manually select structural sections:** enter the geometry (press 9), select by class per structural section (truss, ladder, body, etc.), aided by an **Exploded View** to separate overlapping parts, repeating per section you want to isolate for shading.
6. **Automate group-to-class conversion via Python:** run a custom Python script that walks backward through the SOP network reading every upstream node's selection/visibility group parameter into an array (one element per manual selection made in step 5), then a wrangle checks whether the current primitive number is present in each array element and assigns a clean sequential `class` value accordingly.
7. **Finalize the mesh:** run a final cleanup pass (Attribute Delete, recompute normals), set a basic `name` attribute, and output/cache the geometry.
8. **Bake helper maps in COPs:** build a CopNet that bakes attributes unavailable as convenient Solaris shading nodes (e.g. **ambient occlusion**, since MaterialX/Karma lacks a native Dirt/AO helper node like Redshift's) directly onto the model's UV space; output via a named node for later Solaris reference; note position and world normal don't need baking since Solaris provides them natively.
9. **Import into Solaris:** bring in the geometry, add a Dome Light and basic render settings.
10. **Base color layer:** set LayerX's base to a chosen color.
11. **Alpha-masked rust layer:** enable a new layer, load a Megascans structure texture strictly as the layer's **alpha** input (color-correcting/range-tuning it), and pick the layer's actual color independently.
12. **Triplanar-masked layer:** enable another layer using a different Megascans texture as color, with its alpha driven by a **Triplanar** projection (chosen specifically to avoid UV-seam artifacts for this mask).
13. **Class-based section mask:** build a **Grid** node (with Fractal noise layered in to break up its regular edge pattern), extract a single channel, read the model's `class` attribute (converted to float), and compare with `if (class == N)` to output a binary white/black mask isolating one specific structural section — usable as an alpha for texturing just that section, with N swappable to target different pieces.
14. **AO layer:** enable a layer reading the previously COPs-baked ambient occlusion map directly as its alpha/mask input.
15. **Graffiti/graphite decal layer:** load a PNG decal with alpha (Color4/Mono mode), route through a **Place** node (offset/scale controls, **address mode U and V set to Constant** so the decal doesn't repeat/tile around the model), extract the alpha via **Separate Color**, feed it as the layer's alpha (multiplied down since full-strength blending read too strong), and set the blend mode to **Overlay** for a subtle final decal pass.

### Houdini Nodes / VEX / Settings
Custom node: **LayerX** (native compiled MaterialX node, multi-layer stack with per-layer enable/blend-mode/alpha, usable on color/roughness/displacement — found under MaterialX → Compositing). SOPs: Attribute Delete, custom UV-orient-up HDA, UV Layout, Connectivity (`class`), Exploded View, Python (`hou` node-graph traversal reading upstream group/visibility parameters into arrays), Attribute Wrangle (VEX: primitive-in-array membership check, sequential class reassignment), Normal, Name. COPs: ambient occlusion bake (UV-space), named output node for Solaris reference. Solaris/MaterialX: Dome Light, Karma Render Settings, MtlX Image (color/alpha inputs), Karma Triplanar, Grid (with Fractal noise), Vector to Float / channel extraction, Compare/`if` (class-value masking), Place (offset, scale, address mode: Constant U/V), Separate Color (alpha extraction), blend modes (Normal, Overlay, Multiply).

### Difficulty
Intermediate — LayerX itself is simple to use once available; the Python group-to-class automation and COPs AO-baking workaround are the more advanced supporting techniques.

### Houdini Version
21 (transcript explicitly references "this visualize node is broken in Odini 21"; LayerX described as newly released/compiled for current Karma/MaterialX).

### Tags
#karma #materials #shaders #mtlx #triplanar #cops #python #uv #procedural #environment #intermediate

---

## Related Tutorials
- [No VEX Challenge #1 - Procedural Water Tower](no-vex-challenge-1-procedural-water-tower.md) — the source modeling video for the water tower asset textured here with LayerX, Triplanar decals, and baked AO.
- Cross-link with houdini-20-procedural-shading-features.md and custom-procedural-materials-with-houdini-and-karma.md (same author, overlapping Triplanar/MaterialX layered-shading vocabulary).
