---
title: Creating Procedural Environment Assets in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=VJ4AnxgCvQU
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H18+, uses Labs Instant Meshes)"
tags: [heightfields, triplanar, remesh, uv, substance-painter, baking, displacement, solaris, karma, advanced]
extraction_status: complete
frames_dir: tutorials/frames/creating-procedural-environment-assets-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Creating Procedural Environment Assets in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=VJ4AnxgCvQU)
**Author:** cgside
**Duration:** 21m40s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to share a technique with you
[0:05] or a few techniques on how to add details to your eye fields where you might want to
[0:13] create some clips or mountains and add some life to it. So basically I'm starting with
[0:23] the night fields. These are some of the techniques I shared on Patreon on my last post. There's


### Night Field [0:25]
**Transcript (timestamped):**
[0:31] one hour video tutorial on there that you can watch but I'm going to break it down for
[0:40] you in a few minutes. So I'm starting with the night field and I'm drawing a mask. I went
[0:48] through a few iterations and subtracted some shapes and whatnot. Then I'm blending two masks,
[0:58] one slightly blurred, then remapping so I can have I blurred the one so I can have this transition
[1:08] in the bottom. Then I'm adding some noises. I'm not so sure about these wave wave effects but
[1:19] it's there so I won't change it now. Then I'm adding some distortion blurring a bit the details,
[1:31] clearing the mask. Then I'm creating a mask for the slope where I will be adding the side details.
[1:45] As you can see I'm using a copy layer to save it in the slope layer. Then I'm blurring quite a bit
[1:56] the side details. So I don't get too much distortion as in input.


### Triplaner Note [2:05]
**Transcript (timestamped):**
[2:05] Converting the night fields and as you can see this sort of geometry is stretched out
[2:12] polygons. Won't give us a good result when using the triplanar node which is what we're going
[2:18] to use to add some details. So I'm remaching everything after a clip.
[2:30] And we should have something like this. I ended up adding a few iterations to remove some
[2:38] clusters of geometry as you can see we still have some of it. Then the more geometry you have as an


### Subdividing [2:45]
**Transcript (timestamped):**
[2:51] input before the triplanar the better the result will be or at least until some point. So in this case
[3:02] I'm subdividing three times. Let's just place one to be a bit faster and we can see the result.
[3:15] So this is one subdivision and here are three subdivisions. Quite a bit more detail but also
[3:29] very eye poly but this is the result I ended up using as an input for to create the
[3:40] the eye map, the displacement map. So let's say we just have one level and we're using the triplanar
[3:50] this place. I believe I shared before this technique we using the triplanar this place
[3:56] in the coloring inputs not the displacement and I'm using one to and three. These are just
[4:07] mega scan assets. Then I'm also blurring the normals creating point normals and blurring and
[4:14] it's important you do it after the triplanar this place otherwise the triplanar this place won't
[4:21] update the normals or you will lose the normals after the triplanar this place. So do it after
[4:30] and so we have the result and in the point of I'm just importing I'm just compositing the
[4:39] different triplaners. In this case you import the second and the third inputs with import
[4:46] point attributes and importing the CD and I'm just compositing with an overlay mode
[4:55] and maybe we can reduce some of the some of the alpha of the different textures
[5:06] and I'm compositing the first two then adding the third as you can see I'm reducing the alpha


### Point Flop [5:08]
**Transcript (timestamped):**
[5:15] of the third texture converting it to a float fitting the range between minus point five and point five
[5:22] because the zero value of the mega scan structures are zero point five multiplying by the slope
[5:31] and displacing this placing quite a bit because this is a large model as you can see
[5:38] so we need to replace it quite a bit and just adding a constant to the color otherwise
[5:45] we have the triplanar colored so after that as you can see this is with three subdivisions we have
[6:02] I believe enough detail and we have it all the way around and one thing you should play with
[6:12] is the offsets of the of the textures this will give you slightly different results
[6:24] if I just use the first one let's connect the CD to the vector to float as you can see this one
[6:35] this particular texture acts as a overall detail overall shape forming let's say
[6:45] and from there you can add more detailed ones more eye frequency textures
[6:56] and you can also add procedural noises I just found that these sort of textures give you better
[7:05] results and it's faster so with three levels of subdivisions you get this and after that you have
[7:17] the eye poly completed now you need to create some UVs and low poly geometry and the way I'm doing
[7:26] that I'm not sure if it's the best option but I'm reducing the polygons remashing and then create
[7:36] instant meshes and this will give me a result which looks something like this which is pretty clean
[7:43] and works well as a low poly and after that we create the UVs but and the reason I'm doing
[7:54] these three operations in this particular order is because after the eye poly this is a
[8:03] very dense mesh if you try to remesh this it will be really slow so it's just an optimization
[8:10] and I'm also reducing and remashing within a loop so let's see let's add to manual
[8:19] and I'm creating a scatter I'm scattering some points and creating a natural boots to be on
[8:28] on some islands to the so the mesh is divided into different islands and then I'm reducing in a
[8:38] loop in this case it's compiled again I go more into detail and do it step by step on my patron
[8:45] video you can check that out but it should be easy to see the result if we check the
[8:57] file cache so as you can see we have these lines that are the different islands that we're splitting
[9:05] the geometry into so we remashing by iterations instead of I mean we're reducing by iterations instead
[9:17] of reducing all at once that would be really slow and after the poly reduce I am remashing
[9:31] and the reason the reason I am remashing is to give a cleaner input to the instant meshes
[9:38] otherwise it wouldn't work this is a very picky node sometimes just doesn't want to collaborate
[9:48] so I'm remashing again with the same workflow so dividing the mesh into small islands with
[9:57] the natural roots and then doing the remesh you can take a look at the file and you explore on
[10:08] your own so after I do instant meshes 40k polygons and also do a smooth
[10:18] so actually it was pretty fast to calculate this so I also do a smooth just to have a cleaner input


### UVS [10:32]
**Transcript (timestamped):**
[10:33] and then I'm caching and this is our base mesh without UVs and after that I am creating the UVs
[10:44] and again let me show you this time how it works I'm creating a natural roots called divider
[10:52] and just divides the mesh into different sections different islands and then I'm promoting
[11:01] to primitive and iterating over and creating a UV flatten so this should give you something
[11:13] like this it doesn't look very promising then you can do a UV layout and you get
[11:28] and you get the different islands again this is just a way to do it quickly
[11:37] and without worrying too much about UVs as we will be using triplanar to
[11:45] as I was saying we will be using triplanar projections to create the textures inside substance
[11:53] so then I am caching this
[11:57] and softening the normals so we don't get any errors on substance side and I'm also creating a slow
[12:12] petri-boot just for the scattering of the grass that I will be adding later
[12:19] in this case I want to output it as a natural root and saving the low poly geometry
[12:31] and then in the maps baker I can just set up the i-channel as an EXR
[12:39] set your resolution and it's important to set the correct distance
[12:45] and so we can actually visualize the distance
[12:54] and in this case I have set it to 4 this is quite a big mesh


### Height Map [12:59]
**Transcript (timestamped):**
[12:59] I also noticed that if you had a subdivide with one or two iterations it also helps to give
[13:07] you a better result in the item map or displacement map so this is really simple just set your
[13:15] distance according to the detail in the ipoly and you are good to go just press render
[13:25] then you can go to the composite view and as you can see let me just show you something this is
[13:34] the first version and if I disable this if I disable this equalize as you can see
[13:47] we have some problems here so the distance was not enough I believe I set it to 2 at first
[13:56] and as you can see we have some holes which is not visible when you will equalize it
[14:05] sorry this is not visible here at least not so noticeable so although it's good to see the
[14:16] equalized version to check if everything is working it's also important to have a look at the raw
[14:27] input so you can debug these little errors so this is the second version as you can see
[14:35] it's there are still some parts where it has some problems but overall it's much better
[14:44] and you can eliminate those by increasing the distance
[14:49] so this is the item map and we can just go to obj and synvue and let's go to salaries
[15:06] stage and let me just give you an example
[15:18] here I have some snapshots so let me see this is the raw geometry the low poly geometry
[15:26] this is the first one so it doesn't matter so this is the displacement map working


### Displacement Map [15:33]
**Transcript (timestamped):**
[15:37] and this is the ipoly render it so I just brought in the 4 million polygons or 7 million polygons
[15:46] I believe geometry and this is the render and then this is with displacements so just the
[15:55] base mesh the low poly with displacement so very similar and this is pretty easy to set up
[16:07] you just create a material like image, set it to float, create a displacement in this case I'm
[16:14] reducing a bit but if you leave it at one it will give you the exact exact results
[16:21] and then just create a surface material and connect your standard to the surface shader and the
[16:27] displacement to the displacement shader and that's basically it's I can show you a small render of


### Example Render [16:33]
**Transcript (timestamped):**
[16:40] so this is a test render I did with some grass and with all the textures and whatnot I still going
[16:47] to show you the substance parts not the texturing itself but the workflow let's say
[16:56] so this is an example render I'm also adding some clouds
[17:02] and some grass


### Exporting to Substance [17:11]
**Transcript (timestamped):**
[17:12] and you can play with the render geometry settings with the amount of testing quality but one
[17:19] should be pretty good maybe it's a bit even overkill and yeah let's see in substance
[17:29] let's see the other part of the graph first so let's see obj so I have shown this part
[17:41] and in here I'm doing the same but the same concept of dividing the geometry into sections
[17:51] and it's rating overreach because I want to export the ipoly to use in substance to back the maps
[18:01] and I don't want to render just one file it just will be to load in substance and to have on this
[18:11] it will be just too heavy so I'm creating a loop and with the python I believe I'll share this
[18:19] tip before and I saw it somewhere too so I'm just executing the the raw geometry by using the
[18:29] press button function and in the raw geometry I'm using the iterate detail attribute the iteration
[18:41] detail attribute to rename the pieces or to name the pieces and yeah the python here does everything
[18:50] then you execute the loop and check this node render this node and it will automatically
[18:59] exports each part to file so here I am in substance painter where I did really basic texturing techniques


### Baking [19:05]
**Transcript (timestamped):**
[19:13] just using some textures and smart masks and a mask editor to create some
[19:24] some details some blending between the different textures I believe I use three textures so
[19:36] there's one then added some in the occluded areas added the grass
[19:43] we did I believe the let's see the world normal yeah world space normal
[19:57] and that's basically it's very simple setup and the most important thing here I wanted to show
[20:06] you is the baking process so you select the maps you want to bake
[20:13] imports your in this case I have 32 pieces of the i-poly you can have less or more depending on the
[20:22] the amount of polyvants you have to start with set your resolution and just hit bake
[20:28] make sure your bounds are looking okay and you can just press bake
[20:33] and you should have a pretty good bake in this case let me see mesh maps we have the normal from
[20:50] the i-poly the curvature the a-o as you can see thickness and so on
[21:04] so yeah that's basically everything I wanted to share with you today if you want to investigate
[21:10] on your own you can check the file on my patreon and I also have a lesson there with one
[21:18] with over one hour where I go to step by step not this project but a similar one with the same workflow
[21:29] and you can check that out if you want other than that thank you for watching and see you in the next one



---

## Captured Frames

- [1:45] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_000.jpg
- [3:15] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_001.jpg
- [6:02] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_002.jpg
- [7:43] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_003.jpg
- [9:57] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_004.jpg
- [11:13] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_005.jpg
- [15:26] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_006.jpg
- [20:33] tutorials/frames/creating-procedural-environment-assets-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
A condensed breakdown of a full heightfield-to-game/render-ready-asset pipeline: mask-driven heightfield detailing, Triplanar Displace for micro-detail on a remeshed/subdivided high-poly, an island-based iterative poly-reduce → Instant Meshes low-poly workflow, procedural per-island UVs, Substance Painter baking (high-to-low), and final Solaris/Karma displacement rendering.

### Summary
A dense recap of a technique the author covers in full (~1 hour) elsewhere on Patreon, compressed into ~20 minutes here. Starts from a heightfield with hand-iterated masks (blended/blurred/remapped/noised) plus a **slope mask** (via Calculate Slope) for side-detail placement. Since raw heightfield geometry has stretched polygons that break triplanar projection, the mesh is **remeshed after clipping**, then **subdivided** (author settles on 3 iterations as a fidelity/speed tradeoff) before feeding into **Triplanar Displace** using Megascans rock textures on the *color* inputs (not displacement directly) — normals must be recomputed/blurred *after* the triplanar displace or they won't update correctly. Multiple triplanar texture layers are composited together (Import Point Attributes pulling CD from each layer, blended with Overlay mode and tuned alpha), converted from color to a float and remapped (accounting for Megascans' 0.5 mid-gray convention) to drive the actual displacement, scaled up substantially since the model is large-scale. For **low-poly + UVs**: rather than remeshing the dense high-poly directly (too slow), the mesh is divided into islands (Scatter + a Voronoi-style split via a natural/normal-based grouping), **poly-reduced iteratively per-island inside a compiled loop**, remeshed again (Instant Meshes is described as "picky" and needs a clean/simple input to cooperate), then run through **Labs Instant Meshes** (~40k target polys) and smoothed. The same per-island-division trick is reused to build **UVs**: divide into islands, promote to primitive, loop a UV Flatten per island, then UV Layout. For texturing, the high-poly is exported in per-island pieces (looping with Python, using a `press button` function and an iteration/detail attribute to name each export) to Substance Painter, since exporting the full dense mesh as one file would be too heavy — baked maps include Normal, Curvature, AO, Thickness, ID, Position, with **Max Frontal/Rear Distance** tuned per the model's scale (values around 2-4 for this large asset), and it's important to inspect the *raw* (non-equalized) baked map for gaps/holes that the equalized preview can hide. Rendering (Solaris/Karma) applies the baked height/displacement map: an Image node set to Float feeding a Displacement shader, connected alongside a standard surface shader — displacement strength near 1.0 gives the closest match to the high-poly reference.

### Key Steps
1. **Heightfield mask prep**: hand-draw/iterate a base mask (subtracting shapes as needed), blend two versions (one blurred) with a Remap for a smooth bottom transition, layer in noise and distortion, blur, then clean the mask. Separately build a **slope mask** (Calculate Slope) for side-detail placement, saved via a Copy Layer.
2. **Prep for triplanar**: heightfield-derived geometry has stretched polygons that break triplanar projection — fix by **Remeshing after a Clip**, running a few iterations to remove stray geometry clusters, then **Subdividing** (3 iterations used here as the fidelity/speed sweet spot for this asset, tested against 1 iteration for comparison).
3. **Triplanar Displace for detail**: feed 2-3 Megascans rock textures into **Triplanar Displace**'s *color* inputs (not the displacement input directly) to layer surface detail; recompute and blur point normals **after** the triplanar displace step specifically — doing it before means the triplanar displace won't update the normals correctly and you lose them.
4. **Composite the triplanar layers**: Import Point Attributes to pull the CD (color) from each triplanar layer, blend with **Overlay** mode, tune each layer's alpha; convert the composited color to a float and **Fit** it into a -0.5 to 0.5 range (accounting for Megascans textures' 0.5 mid-gray zero-point convention), multiply by the slope mask, then use it to actually displace the position — scale needs to be large since this is a big-scale model. Experiment with per-texture **offsets** for varied results; the first/base texture layer acts as overall large-scale shaping, with additional higher-frequency textures (or procedural noise, which the author found gives comparably good and faster results) layered for finer detail.
5. **Low-poly + optimization via islands**: rather than remeshing the very dense high-poly directly (too slow), **Scatter** points and build islands via a natural/normal-grouping approach, then **poly-reduce iteratively per-island inside a compiled loop** — much faster than reducing the whole mesh at once. Remesh again afterward specifically to give **Labs Instant Meshes** a cleaner, simpler input (Instant Meshes is described as finicky and unreliable on messy input).
6. Run **Labs Instant Meshes** targeting ~40k polygons, then a **Smooth** pass for a cleaner low-poly base mesh (no UVs yet).
7. **Procedural UVs**: reuse the same island-division trick — a "divider" primitive-group split, promote to primitive attribute, loop a **UV Flatten** per island/piece, then run **UV Layout** to pack everything — described as a fast, low-effort UV approach acceptable specifically because triplanar projection (not UV-based texturing) drives the visuals in Substance later. Soften normals afterward to avoid Substance Painter import errors; also bake a separate low-poly scatter/point-cloud output for later grass scattering.
8. **Height/displacement map baking (in Houdini)**: use the Maps Baker with EXR output, correct resolution, and critically the correct **Max Frontal/Rear Distance** (author used ~4 for this large mesh) — too small a distance (e.g. 2) produces visible holes/gaps in the raw bake that an "equalized" preview can mask; always check the **non-equalized raw output** to catch these errors, not just the equalized preview.
9. **Displacement setup for render** (Solaris/Karma): create an Image material node set to **Float**, wire it into a **Displacement** shader node, connect a Standard Surface shader for the base material, and wire both the surface and displacement shaders into the final material output — a displacement strength near 1.0 best matches the original high-poly reference, though it can be reduced for stylization/practicality.
10. **Batch-exporting high-poly pieces for Substance Painter**: since the dense high-poly is too heavy to export/import as one file, loop through each island piece with a small **Python** script using a `pressbutton()`-style function on the ROP/export node combined with an iteration/detail attribute to rename each output piece per loop iteration — the script handles execution and per-piece naming automatically once set up.
11. **Substance Painter texturing/baking**: basic texturing with a few base textures, Smart Masks/Mask Editor for blending, adding grass in occluded areas, using World Space Normal for some effects. The key process to note: select which maps to bake (Normal, Curvature, AO, Thickness, ID, Position, etc. — "Mesh Maps"), import all the exported high-poly pieces (32 in this example), set resolution, verify the bake **bounds** look correct, then Bake — producing a full mesh-map set ready for texturing/shading downstream.

### Houdini Nodes / VEX / Settings
Heightfield mask chain (draw/subtract → blend/blur/Remap → noise/distortion → clean) + **Calculate Slope** (side-detail mask, Copy Layer) → Clip → Remesh (iterated) → Subdivide (3×) → **Triplanar Displace** (color inputs, Megascans textures) → point-normal recompute + blur (post-triplanar) → Import Point Attributes (CD per layer) → Overlay blend + alpha tuning → color-to-float + Fit (-0.5..0.5) + slope-mask multiply → position displace → island Scatter/grouping → compiled per-island poly-reduce loop → Remesh (clean input for Instant Meshes) → **Labs Instant Meshes** (~40k target) → Smooth → island-based UV Flatten loop → UV Layout → soften normals → Maps Baker (EXR, Max Frontal/Rear Distance tuned to scale) → Solaris/Karma: Image (Float) → Displacement shader + Standard Surface → material output → Python `pressbutton()`-driven per-island batch export loop (iteration/detail-attribute naming) for Substance Painter ingestion.

### Difficulty
Advanced — combines heightfield detailing, triplanar projection math/gotchas, compiled per-island poly-reduction, third-party remesh tools (Labs Instant Meshes), Python-driven batch export, and cross-application (Substance Painter) baking; a compressed recap of a much longer full walkthrough elsewhere.

### Houdini Version
Not stated explicitly; uses Labs Instant Meshes and Solaris/Karma for final render, consistent with any modern Houdini (H18+).

### Tags
#heightfields #triplanar #remesh #uv #substance-painter #baking #displacement #solaris #karma #advanced

---

## Related Tutorials
Cross-link with [Cliff Face in Houdini](cliff-face-in-houdini.md) — shares #procedural #vdb-adjacent rock/environment asset techniques (that tutorial uses VDB/Boolean cycling instead of heightfield+triplanar-displace for detail, a complementary alternative approach) and with [Cliff texturing with karma and material X](cliff-texturing-with-karma-and-material-x.md) — shares #triplanar, using an in-Houdini MaterialX triplanar shader as an alternative to this video's Substance Painter baking pipeline.
