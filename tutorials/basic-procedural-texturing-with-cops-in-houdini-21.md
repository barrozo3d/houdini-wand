---
title: Basic Procedural Texturing with Cops in Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=AB9rwjcX0Xg
author: cgside
ingested: 2026-07-13
houdini_version: "Houdini 21 (Copernicus/COPS)"
tags: [cops, texturing, procedural, materials, triplanar, mardini, normal-map, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Basic Procedural Texturing with Cops in Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=AB9rwjcX0Xg)
**Author:** cgside
**Duration:** 25m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'm going through step by step on how to
[0:04] texture an asset using Cops in Odini 21. So this is not supposed to be a beautiful
[0:09] texture in you can see but it will show you all the technical difficulties you might have
[0:14] when tackling tasks like this. So yeah let's get into it. Let me move this to my other monitor
[0:20] and let's get started. So basically I start with these assets that I modeled, I'm
[0:25] uploaded like a year ago for Mardini. It has some nice UVs already laid out so you can access
[0:31] the file on Patreon to get started. I'm just gonna drop a copnet and let's create a null in here
[0:39] and let's name it out and we will import it to Cops. Let's just do a sub import
[0:52] and import this. So this is our pen. Okay the first thing we want to do is to bake some utility
[1:01] masks that we can probably use in texturing like ambient occlusion, edge mask and whatnot.
[1:06] So what we can do now is to use a bake setup, bake geometry textures and we will start by
[1:14] connecting these to the low and in here we will set it to single mesh low poly only because we don't
[1:21] have a night poly to bake from in this case. So if we bake this let's see and the first thing I
[1:27] want to do is to enable for example ambient occlusion that's fine let's actually look at that map.
[1:32] So if we go into occlusion we have something like this and if we preview that.
[1:38] So let me just fetch and connect these in here and set up tools and connect these to geometry
[1:46] and occlusion to the base color and we will get something like this. So there we have our ambient
[1:53] occlusion but for example if we bake the curvature and let's look at that we see these obvious
[2:00] indentations or these wireframe because it's just too low poly. So in this case since we don't
[2:05] have a night poly version we need to increase the resolution. So instead of going back to
[2:11] subs I'm just gonna quit. Sopping vogue in here and go inside and we will just subdivide this
[2:18] and let's say twice and we get this sort of geometry and when we go back and we bake our let's see
[2:26] our curvature we should have something a bit better as you can see. So if we don't subdivide we will
[2:33] get this in printing on the mesh and same goes if you want to bake a displacement map and what not
[2:38] it's always good to subdivide a bit the low poly mesh. So what will we bake in here? So the first
[2:45] thing I want to do is to go to let me see here the normal. So the world normal and we need actually
[2:54] to bake in here the world normal but we don't want this version we want the one that is signed so we
[3:00] can use it later on a triplanar node. So that's our normal then we will need the position.
[3:08] The edge normal also let's look at that so edge normal so edge normal is to pound the edge normal
[3:16] I guess. So let's see yes that's the edge normal we might need that. Let's also bake to world
[3:24] position so let's have a look at that position but this one is again it's not the right format we
[3:29] don't want relative we want absolutes and then what else do I want to bake so we have the occlusion
[3:36] let's look at the curvature maybe we need to play a bit with curvature in here so geometry curvature
[3:44] I'm gonna I'm just gonna increase the samples in here so for the ambient occlusion I'm gonna set it
[3:50] to 128 or the curvature the same so we increase the samples I also want to bake the edge map so we get
[3:59] something like this so we get these edges and on the edge map I might need to increase also
[4:07] the samples so let me just fetch this one in here instead and we are having some issues in here
[4:18] on the on the boundaries of the obvious but we will fix them in a bit so other than edge we also
[4:24] want to bake the cavity and let's also increase the samples and let's look at the cavity map
[4:30] we get something like this and the rest is fine so now we want to cable pack all of this so cable
[4:38] pack and we want to drag in the edge normal the world normal let's have a look so edge normal
[4:48] world normal we want the position we also want the occlusion the curvature the edge the cavity
[4:58] and that's about it we might need the alpha also so now we just set fields from inputs
[5:05] and then let's have a look in here first at the for example the occlusion one
[5:11] this one is not some noticeable so let's look instead at the position and set it to flat as you
[5:19] can see we have these ugly seams that we need to fix so for that I'm gonna do it instead of
[5:26] doing only at one map we will do it for all so we can do an extra polite boundaries
[5:33] so like everything and as a mask I'm just gonna load in here the alpha
[5:37] so not the mask so the fill area mean so let's move this up and we want also to play in here
[5:47] with the edge of set so point over one I believe yeah and then we can finally do a cable and pack
[5:55] just to test and let set fields and now so we add these for the position map let's look now
[6:03] we should have fixed everything and this will work for all the maps as you can see so they don't
[6:09] have that problem anymore so let's have a look so as you can see in here we are fixing that issue
[6:16] for the most part okay so now that we have the maps we can start to working on the texturing of
[6:24] this so the first thing I'm gonna do is to import a map so I'm gonna import this map from mega
[6:32] scans it's just a platter that will work for the main texturing of the pen and I'm gonna
[6:38] do a remap and I'm just gonna play with the values in here so just increase a bit the
[6:48] the input mean to add some contrast and then if we evolve if we for example place this into
[6:56] paste collar you can see we'll have the problem with the seams so what I'm going to do is to
[7:02] create a triplanar in this case x-tile since I want to randomize it load this as a texture load
[7:09] my position and my normal and let's have a look we get something like this and if we connect to
[7:15] the paste collar we should have this kind of effect and I'm gonna play with a triplanar so first of
[7:22] all I'm gonna increase the scale and let me change this to 2k and we'll take a bit more so I'm
[7:34] going to also increase some scale random rotate random set it to 1 and I'm also going to play with
[7:42] the blending in here so we plan the bit more something like this and let me see maybe I don't want
[7:49] yeah I want to change the scale to get something like this and we can play with the seed
[7:56] so we get like this result and as you can see we have no visible tiling
[8:02] and in order to fit the position in normal in here if I didn't change the
[8:09] for example the position to be absolute if we do relative as you can see we will have some
[8:12] problems of stretching and the same goes for the world normal if I set it to offset
[8:18] we will have some problems as you can see so we need this to be signed and this to be absolute
[8:24] in order to feed this triplanar exile so that's fine now we want to
[8:31] create some color for these so I'm just gonna do I'm gonna do RGB
[8:38] and we can for example let me open in here some texture something to sample from so I'm just
[8:45] gonna do sample screen colors and sample in here something and we get something like this
[8:53] and then I have this script that I can re-sample these ramps but in this case I'm just gonna use
[9:01] the one I sample previously so we to look something like this and we get this so if we connect
[9:07] these in here we get this result but then again I want to play with this so I'm gonna place
[9:14] ages via just and I'm just going to decrease the saturation quite a bit and also develop
[9:24] to something like this let's have a look might be a bit too dark so maybe something like this
[9:33] and we can change that at the end so that's our base map then I'm gonna fetch in here the maps
[9:41] so this one in here I'm gonna call it maps and then I'm gonna create a fractal noise 3D in this case
[9:52] because I want to connect the position to the position so it tiles so if I connect this to the
[9:56] base color as you can see this will tile perfectly because we are using the original position
[10:04] and I'm just going to play with the fractal noise in this case I'm gonna set a scale of point
[10:11] 3 something and I'm gonna yeah the rest is fine then I'm going to do the following I'm going to
[10:18] create a node that is part of a plugin called cobstance which is the substance designer nodes for
[10:26] Odini for cobst and it's pretty cheap and I really encourage you to have a look at those if you want
[10:33] create some substance designer effect in Odini so this one is the slope blur I'm gonna connect in
[10:39] here the edge map that we have in here so let me have a look at map I'm gonna connect that to the
[10:45] source and connect this noise to the slope and this will give us this result but we want to increase
[10:50] the samples and what else we also need to play with the intensity so basically I just want to create
[10:57] this sort of effect so you probably can get away with a with a distort node to do something similar
[11:02] I'm just gonna use this node since I have it and I like the result so then we will create some mask
[11:10] what we're creating in here is just some some mask for the rest so I'm going to use the edges if we
[11:17] have a look at that we get something like this that we can later blend with some other noises so now
[11:26] I'm just gonna create a branch rest create the rest and I'm gonna play in here with the
[11:32] amplitude so increase it a bit more the center can be the same the element side 0.2 and I can also
[11:43] in this case I want to complement it to invert it maybe place with the coverage increase a bit
[11:50] the softness and decrease a bit the rest and the rest is more or less fine so something like this
[11:59] then I want to do the same in here the triplanar that planner actile connect the texture so I want to
[12:05] connect this as a texture the position and the world normal and we get these results let's have a look
[12:14] so something like this now we want to play with the x-tile so we want to randomize it maybe
[12:20] decrease the scale random the rotate random and the random seed we can play with it something like
[12:28] this maybe play also with the blend we get like these results then we can do a blend in here
[12:37] and blend the edge mask with this and we do a maximum in this case so let's have a look at that
[12:45] and maybe that will be just way too much so in this case we need to play let's see
[12:56] let's decrease the coverage to something like this and now we need to import a rust map so I have
[13:05] one year from from mega scans that looks something like this and we can again do the same
[13:14] and let's have a look at that result so here we have the rust maybe let's play with the settings
[13:22] of this triplanar increase the scale and play with the seed and the rest should be just fine
[13:32] then we can do a simple blend so if we creating here a blend and we connect these as the background
[13:42] these as the foreground and as a blend we use our mask and we connect it to the base color we get
[13:50] something like this and if we have a look at the material and maybe play in here with the coverage
[14:04] and the element size we can get different results
[14:08] you can see we also have it on the edges
[14:15] so that's fine now we also want to create some normals so right now this is way too light so let's
[14:26] create a normal map from this so the way I'm going to create a normal map is just duplicate this maps
[14:34] note and I'm going to create from the position I'm going to create a fractal tree the noise
[14:40] using the position and for the first one we will blend several ones so I'm going to increase
[14:46] the the element size decrease the roughness and create yet another one and for this one I'm just
[14:54] going to decrease these to 0.07 and increase the roughness and yet another one at a smaller scale
[15:03] that I'm going to just increase a bit and then I'm just going to do a slow blur
[15:11] and connect these in here and for example use these first noise as a map
[15:17] increase the samples and decrease the amplitude and set it to mean and decrease the amplitude
[15:23] so we get something like this so we get this sort of result then we're going to create
[15:33] a normal map from this a white to normal this will be the first one which is the largest scale I'm
[15:41] going to just decrease these to 0.018 then I'm going to create one for this and this one will be
[15:49] 0.079 and we combine normals to mix in the normal map and the default settings should be fine
[16:01] then I'm going to do the same for this one and this one will have a value of 0.01
[16:10] and we do the same again we combine the normals and in this case I might decrease the scale no
[16:17] let's find then if we connect these to the normal input so let's connect these to the normal input
[16:28] we get something like this we need actually to play with the scale of the noise maybe so the scale
[16:36] of the normal map I mean so if we come in here and change this to 0.75 that's a global control
[16:41] and we also need to create a roughness map but I want also to set the normal for these parts of
[16:51] the rest so I'm going to blend in the rest map over here you have the rest so I guess we will
[17:04] patch this one and we're going to create again a knight from this then another map so I mean
[17:14] so I do normal we get something like this so we might need to we need to decrease it by the bit
[17:24] and also invert it so it goes in and set it to about 0.5 and then we can again combine normals and take
[17:35] this one and this one and connect these in here and in here I'm just going to decrease the operation
[17:50] and we get you can see this indentation in here and you can increase or decrease the effect
[17:56] I'm just going to leave it like that let's quickly create a roughness map that's really
[18:03] basic so I'm just going to open here with the fetch this is not how you create a roughness map
[18:10] but I'm just going to do it really quickly so I'm just going to load in the trackliner and load the map
[18:17] and do a basic remat and connect these to roughness get something like this and we will play
[18:28] in here increase this the output mean then maybe increase this one so something like this but we
[18:37] also want to play in here with with the value so we want to decrease this let's play a bit more
[18:47] let me see if I change anything so I guess not we can play a bit more just to give it some more
[18:54] effect so we really exaggerated but you can play with the settings so we get something like this
[19:03] now I also want to create some text in here to imprint in our normal map to create some effects
[19:13] so in order to create a text we will start with a card 3D that we have on cops go to the front
[19:19] with space bar 3 let's enable the snapping and change this to a busier place 1.0 near and drag
[19:28] to maybe something like this and place another point in here and we can press F select and press
[19:35] 3 to edit the tangents and something like this will work and maybe move this a bit up
[19:41] something like this will refine then in order to create UVs from this we need a mesh so for that
[19:49] I'm just gonna stop in bulk and I'm gonna dive inside in this case I'm going to create just going
[20:01] to re-sample this so set it to point 1 is fine then I'm gonna sweep it and set it to ribbon in this
[20:11] case and a value of point 5 should be just fine and then we can create a UV flatten let's look at that
[20:22] let's make sure we do a rectify so we get something like this so that should be fine and now we can
[20:29] just uh, restoreize the GU so restoreize geometry and I'm going to add UVs so let's have a look at
[20:40] that we get something like this maybe that was a bit too big but that's fine then we're gonna
[20:47] create some text or with the font and I'm going to call it Sabry whatever that means it's just
[20:57] something I found on my reference and I'm gonna change the font to that again search kind of
[21:04] I'm gonna change it to this font is so full so let's change it to what's it called time's bolt
[21:13] so time's bolt and maybe increase this to something like this and the rest is fine then I'm just
[21:21] not gonna create a layer property so it doesn't tile just as you can see this will tile and I want
[21:27] to set it to constant and then we can just do a new v-set and this will be on texture
[21:37] and of course this will be black because we need to play in here with the UV so UV transform
[21:44] and in this case we might need to change the pivot let's see let's try to rotate it we start to see
[21:50] something so maybe play with the scale and play with the offset in here we might need to increase
[22:01] this to something like this so let's see this increases to 0.5 and decrease this to something like
[22:12] 0.2 and we can play with the scale after so something like this so now we just need to place it on
[22:20] on the correct space so before that I'm just gonna blur this something like point to tree
[22:29] and then with that transform to the we cannot really place it or where it belongs so let's have
[22:37] a look in here if we have something like maybe in here before we do the x-erpa-late boundaries
[22:44] so let's fix this one and in this so can't we do that okay and now we can come in here to
[22:57] this transform and let's say we want to place it I'm gonna say it's in here and let's have a look now
[23:04] so it's not exactly there but we can come to the transform and decrease this
[23:18] this is fine maybe it's just too big so yeah I need to play with the uniform scale and make sure
[23:28] we don't tie it so let's go to the sample to transform and set the border to constant and play again
[23:37] with these so something like this will work then we can do an i2 normal and connect again the fuse
[23:53] we get these results and then we can do a combine normals
[24:05] and connect this one in here and maybe just play the planing
[24:15] and we add something like this maybe we can play again with this and decrease
[24:23] this is a bit play with the reference map
[24:31] and set some ambient occlusion and we can again increase these
[24:40] and play again
[24:44] say yeah guys something like this as you can see the final result is not amazing
[24:49] but again this was just to show you a full workflow how you can do this sort of procedural
[24:54] texturing with cops so hopefully you got something out of this and maybe this normal map is just too
[25:01] much so let's decrease it so yeah guys hopefully you got something out of this as always you can
[25:07] wrap the full scene on my patron with this with this mesh this assets and the project file finished
[25:15] and yeah you can also grab exclusive tutorials in there hours and hours of exclusive tutorials
[25:21] all the project files from my videos and you support me if you find my videos useful so again thank
[25:27] you for watching and I'll see you next time thank you



---

## Captured Frames

- [1:32] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_000.jpg
- [2:26] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_001.jpg
- [5:55] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_002.jpg
- [7:15] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_003.jpg
- [9:14] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_004.jpg
- [12:14] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_005.jpg
- [16:28] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_006.jpg
- [24:44] tutorials/frames/basic-procedural-texturing-with-cops-in-houdini-21/frame_007.jpg

---

## Structured Notes

### Core Technique
Full procedural texturing pipeline in COPS (Houdini 21's Copernicus image-compositing context): bake utility maps (AO, curvature, edge, cavity, position, normal) from a low-poly mesh, fix UV-seam artifacts with Extrapolate Boundaries, build tileable materials with Triplanar (x-tile) projection fed by Megascans textures and procedural noise, layer in wear/rust via a Substance-Designer-style Slope Blur (from the "Cobstance" plugin), hand-build a multi-scale normal map from blended fractal noises, and imprint procedural text into the normal map via a hand-modeled Sweep-based text mesh with its own UVs.

### Summary
A warts-and-all, full-workflow walkthrough (not a polished-result tutorial) texturing a previously-modeled asset (a Mardini pen/vessel) entirely inside COPS. Covers baking a full utility-map set from geometry (important gotcha: bake from a *subdivided* low-poly proxy, or curvature/displacement bakes show visible low-poly faceting), fixing UV-seam bleeding on every baked map at once via **Extrapolate Boundaries** (masked by the fill-area alpha, with an Edge Offset tweak), building the base material from a Megascans texture projected through a **Triplanar x-tile** node (randomized scale/rotation/seed to hide tiling, fed by *absolute* position + *signed* world normal — using the wrong space/format on either input causes visible stretching), layering procedural noise and a "Slope Blur"-style COPS node (from the **Cobstance** plugin, a Substance-Designer-node port for Houdini) driven by the edge map to fake directional wear, blending in a second Megascans rust texture via an edge-derived mask, hand-building a normal map from three blended fractal noises at different scales (each converted to a normal via a "height to normal"-type node and combined with **Combine Normals**), building a basic roughness map from the same triplanar height data, and finally modeling a small 3D text card (Sweep + UV Flatten + Font) to imprint custom lettering into the normal map via its own UV space, transform, and blur.

### Key Steps
1. **Import geometry into COPS**: build a `copnet`, create a Null named "out" on the SOP side, and use **SOP Import** to bring the mesh in.
2. **Bake utility maps** with **Bake Geometry Textures**: connect the mesh to the "low" input, set bake type to Single Mesh (Low Poly only, since there's no high-poly to bake from). Bake, in turn: Ambient Occlusion, Curvature, Edge, Cavity, World Normal (must be the *signed* variant for triplanar use later, not the default), World Position (must be *absolute*, not relative), and Edge Normal. Increase sample counts (e.g. 128) on AO/Curvature/Edge to reduce noise.
3. **Gotcha — low-poly faceting:** baking curvature/displacement directly from the low-poly mesh prints visible facet/wireframe patterns into the map; fix by ducking into the SOP network and subdividing the proxy (e.g. twice) before baking.
4. **Cable Pack** all the baked maps together (edge normal, world normal, position, occlusion, curvature, edge, cavity, plus alpha), then **Set Fields from Inputs** to expose them as named image planes.
5. **Fix UV-seam bleeding**: baked maps (especially Position, viewed flat) show ugly seams at UV island borders. Fix with an **Extrapolate Boundaries** node applied to the whole packed bundle (not per-map) — feed it the fill-area alpha as a mask and tune the **Edge Offset** parameter until seams disappear across all maps simultaneously.
6. **Base color:** import a Megascans "platter" texture, **Remap** it (raise input-mean for contrast), then feed it through a **Triplanar (x-tile)** node along with the baked *absolute* position and *signed* world normal — getting either input's space/format wrong (e.g. relative position or offset-format normal) causes stretching artifacts. Randomize Scale, Random Rotate, and Random Seed on the triplanar to eliminate visible tiling.
7. Build color variation with an RGB/color node sampled from a reference image (Sample Screen Colors), refine via a Hue/Saturation-type node (desaturate, adjust value) to taste.
8. **Procedural tiling noise:** duplicate the maps fetch, add a **Fractal Noise 3D** driven by the *position* map (not UVs) so it tiles perfectly regardless of UV layout; tune scale (~0.3) as a base wear-pattern driver.
9. **Directional wear via Cobstance (Substance Designer nodes for Houdini):** use the **Slope Blur** node from the Cobstance plugin, feeding the baked Edge map as the "source" and the fractal noise as the "slope" input — this fakes directional edge-wear streaking; increase samples/intensity to taste (a plain Distort node can approximate this if Cobstance isn't installed).
10. Build a wear **mask** from the edge map, blended with additional fractal noise (tune Amplitude, Element Size, Coverage, Softness, and optionally invert) to control where the effect concentrates.
11. **Rust layer:** import a second Megascans rust texture, run it through its own Triplanar x-tile (scale/seed tuned independently), then **Blend** it with the base color using the wear mask (Blend mode: Maximum) as the mix control — tune mask Coverage/Element Size to balance how much rust shows.
12. **Hand-built normal map:** duplicate the maps fetch three times, each driving a separate **Fractal Noise** (using position, for tiling) at a different Element Size/Roughness (progressively smaller/rougher per layer), Slope-Blur each with decreasing amplitude, then convert each to a normal (a "height/normal" style node) at different overall scales (e.g. 0.018, 0.079, 0.01) and merge all three with **Combine Normals** — chained combines let each subsequent detail layer add fine surface variation without washing out the previous one. A global normal-map intensity control (e.g. 0.75) tones down the combined result if it reads too strong.
13. Blend in a separate normal contribution for the rust-affected areas (decrease/invert its height so it reads as recessed, ~0.5 strength) via another Combine Normals pass.
14. **Basic roughness map:** quick-and-dirty — feed the same triplanar height data through a Remap (raise output-mean, tune further) directly into the roughness input; explicitly called out as *not* a proper roughness workflow, just a fast approximation for this demo.
15. **Procedural text imprint:** model a small text-card mesh from scratch in the SOP context — draw a **Card/Curve** with snapping enabled, refine tangents (F then 3 to edit tangents), **Resample** (~0.1), **Sweep** (Ribbon mode, ~0.5), **UV Flatten** (with Rectify) to get clean UVs, then **Polydoctor**/Resize Geometry to normalize.
16. Add a **Font** node for the actual text/lettering, set its Layer Property to non-tiling (**Constant border**) so the text doesn't repeat, wire it into a new value-set field ("texture"), and use **UV Transform** to position/scale/rotate it into place on the model's UV layout (adjusting pivot as needed to get correct placement and avoid unwanted tiling).
17. Convert the text layer to a normal (**Image to Normal**-style node), **Fuse**, and **Combine Normals** it into the main normal map stack, with a small Blur pass beforehand to soften the imprint edges; adjust the combine's blend strength so the text reads as an embossed/debossed detail rather than overpowering the surface.
18. Final pass: tune overall AO strength and normal-map intensity down if the combined result reads too extreme; the presenter is explicit the final look isn't meant to be a polished hero texture — the point of the video is demonstrating the full technical workflow end-to-end.

### Houdini Nodes / VEX / Settings
**Bake Geometry Textures** (AO, Curvature, Edge, Cavity, signed World Normal, absolute World Position, Edge Normal) → Cable Pack + Set Fields from Inputs → **Extrapolate Boundaries** (alpha-masked, Edge Offset) → **Triplanar (x-tile)** ×multiple (Scale, Random Rotate, Random Seed, Blend — driven by absolute position + signed normal) → Remap (contrast/levels) → RGB/Hue-Saturation color grading → **Fractal Noise 3D** (position-driven for tiling) → **Cobstance Slope Blur** (Substance-Designer-node plugin for Houdini) → mask-driven **Blend** (Maximum mode) for rust layering → multi-scale Fractal Noise → height-to-normal conversion → **Combine Normals** (chained, multiple passes) → basic Remap-based roughness → Card/Curve + Resample + Sweep (Ribbon) + UV Flatten (Rectify) + **Font** node (Constant border) + UV Transform for the procedural text-imprint mesh.

### Difficulty
Advanced — assumes familiarity with COPS/Copernicus, triplanar projection math (position/normal space requirements), and layered normal-map compositing; the text-imprint sub-workflow additionally requires SOP curve/sweep/UV modelling skills. Not a beginner-friendly single-concept tutorial.

### Houdini Version
Houdini 21 (COPS/Copernicus is Houdini 21's new image-compositing context used throughout this tutorial); relies on the third-party **Cobstance** plugin (Substance Designer node ports) for the Slope Blur effect.

### Tags
#cops #texturing #procedural #materials #triplanar #mardini #normal-map #intermediate #advanced

---

## Related Tutorials
No other indexed cgside tutorial currently covers a full COPS texturing pipeline this comprehensively — cross-link with any other COPS/Copernicus or triplanar-materials tutorials once extracted from this batch.
