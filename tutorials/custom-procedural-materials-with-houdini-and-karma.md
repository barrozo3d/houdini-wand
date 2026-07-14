---
title: Custom Procedural Materials with Houdini and Karma
source: YouTube
url: https://www.youtube.com/watch?v=M6W_EP48BaI
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, texturing, uv, baking, materials, shaders, mtlx, karma, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/custom-procedural-materials-with-houdini-and-karma/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Custom Procedural Materials with Houdini and Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=M6W_EP48BaI)
**Author:** cgside
**Duration:** 16m15s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Creating the pattern [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm going to show you how to create something like this.
[0:08] Because some material made with Odini and in material X.
[0:14] So let's jump in. So the first thing we will have a look is on how to create this pattern in here.
[0:23] That will end up creating this bulging effect on the...
[0:29] This is supposed to be an old mattress. So let's start looking in here.
[0:38] We start with a circle then we carve it.
[0:42] And save out the bounding box size of this curve.
[0:49] Then I'm copying it a few times using the... the bounding box.
[0:55] Then placing it in the center. Now I can box clip.
[1:02] So I can extract the... the tiling pattern.
[1:06] That's our goal to create the tiling pattern.
[1:10] So I'm using the dead attribute we saved of the bounding box X and Z.
[1:18] Then as this is not actually joined, I'm creating a polypads.
[1:24] Then grouping the center points and cutting them.
[1:29] So I get these four different shapes.
[1:34] And this is our pattern.
[1:36] Now we need to transform it if we have a look at the size here.
[1:43] It's not squared. So we need to make it square so we can bake it to a texture.
[1:51] So in the transform we take the X size which is the largest one.
[2:00] And divided by the Z size which is a smaller one.
[2:05] And we target the X as this scale.
[2:10] And now that we have a square pattern, we can save out again the bounding box size of this pattern.
[2:22] So we can use it later.
[2:24] And we copy it a few times and place it in the center as we have done before.
[2:35] Because I want to create some geometry from this.
[2:42] So now I am sorting the primitives by proximity to points.
[2:48] And in a range I can select the four last primitives that I want to blast.
[2:57] Then I'm grouping one of the elements.
[3:03] And blasting everything else.
[3:06] Ginding the pads.
[3:09] And now I can polyfill it.
[3:12] And blast away the curves.
[3:15] Rematch it.
[3:17] And now I want to create a mask.
[3:19] So I can create that bulging effect, that displacement effect.
[3:24] So far that I'm going to group the unshared edges.
[3:27] The unshared points I mean.
[3:29] And then create a distance along geometry to create the mask from those points.
[3:38] And I'm blurring a bit the mask.
[3:40] And in a point of I'm just displacing the with that mask with that distance that you would.
[3:54] Saving again the bounding box size of this pattern.
[3:59] And copying it a few times.
[4:04] Generating a connectivity for some reason.
[4:11] And clipping it again using the bounding box size that we saved in here.
[4:19] No, that we saved before.
[4:24] And now in order to bake a color map.
[4:30] We need obviously to add some color.
[4:32] So I chose blue, which is an easy color to key.
[4:37] And it shows red for this part, which I'm going to cover now.
[4:45] So from this pattern we had before.
[4:49] I'm cutting all the points.
[4:53] Cutting all the primitives by the points.
[4:57] So creating separated primitives.
[5:01] Then in a wrangle I'm creating a attribute for every second-brim.
[5:05] So we can have a look.
[5:08] So red, blue, red, blue.
[5:12] And from there we can carve by attribute.
[5:17] This is new to all in the 20.
[5:20] You can also blast, but just let's use carve by attribute since we have it now.
[5:28] And then we can sweep.
[5:32] And we will have something like this.
[5:38] Then we can box sweep everything, give it a color.
[5:43] And this is what we're going to bake to a texture.
[5:49] So for the iris we plug this.
[5:54] And for the lower as we can just create a bound as a rectangle.
[6:00] And group some vertices, the top vertices.
[6:09] So in the UV flatten we can properly orient the UVs.
[6:16] As you can see I'm using those pin-ed vertices.
[6:22] And that's why I am grouping the vertices.
[6:27] And then just adding some subdivisions because sometimes it helps for the baking process.
[6:34] And in here I'm just baking.
[6:39] I am baking the eye and the color.
[6:43] And I can show you how that looks.
[6:50] So this is the color that I baked.
[6:56] And this is the displacement which doesn't look like much, but if we normalize it or equalize it, you can see how it's looking.


### Creating the texture [7:10]
**Transcript (timestamped):**
[7:11] Now let's see how to create something like this.
[7:14] This stitching pattern.
[7:18] So I'm starting with a trace of an image I had.
[7:24] And placing it on the ground.
[7:30] Then I am dividing horizontally along the Z axis I believe.
[7:37] Yes.
[7:39] And what I'm doing in here is taking the Z size of the pounding box and dividing it by the number of divisions I want.
[7:49] As you can see I have, I can change this to 150 or more or less.
[7:57] And you can do this for all the axis.
[8:02] Then I'm grouping the inner edges using this mean edge angle.
[8:12] And dissolving everything.
[8:17] I mean I am grouping all these edges and creating curves from that group.
[8:30] And then fusing polypads to create single primitives.
[8:36] And then re-sampling it.
[8:41] Then I can use a polycut to cut all the primitives just like we have done before.
[8:47] And in here just instead of using the curve I am just removing every second cream.
[8:54] Then sweep it and that's basically it.
[8:59] And I can import the texture with an attribute from map.
[9:05] And since it is so flat you won't need much geometry.
[9:10] The colors will spread out well.
[9:14] At least good enough.
[9:17] And then I can promote it to primitives to have a better flat shading.
[9:26] And that's basically it.
[9:28] I want to add a background line so it doesn't render transparent.
[9:37] And then you bake out the, in this case I am baking out the normal and the color map.
[9:49] And again the same thing for the low resolution mesh.
[9:58] When you are baking just using a flat plane.
[10:02] You can see all these looks.
[10:04] They can be overlapping. There is no problem.
[10:07] Because we have a max-res distance here.
[10:13] You can set it to a value that makes sense.
[10:19] If we have a look at it and show individualize there is plenty of space to bake out the texture.
[10:30] And when you have it baked, we can have a look.
[10:37] We will have something like this.
[10:46] We will have this flowering pattern that I found online.
[10:51] And it's okay to use an external file as long as it is at least styleable.
[10:58] And you can manipulate it in a way that fits your needs.
[11:04] So that's totally fine to use styleable textures in a procedural workflow.
[11:13] And of course we also have the normal map that we baked.
[11:18] So it's looking nice.
[11:21] No errors of that whatsoever.
[11:24] So we can move to shading now.


### Shading [11:28]
**Transcript (timestamped):**
[11:29] So this is our final shader.
[11:32] And let's break it down right now.
[11:35] So let me connect the unlit material to the surface.
[11:47] And we start with the noise.
[11:56] We start with this noise that I created by using the unified noise.
[12:03] Set to worldly and displacing it a bit with or disturbing the noise with another one, which is a fractal.
[12:16] And from there we can import our baked textures.
[12:22] So first this one in here, that is the flower pattern.
[12:31] And in order to separate them, we can use a separate tree or a vector to float.
[12:39] And we need to remap them and clamp them somehow to extract the different channels.
[12:46] So in this case I want to extract the red and the green.
[12:56] And then I'm using that with the color mix.
[13:02] So the first one we're colorizing these leaves.
[13:09] And then in the other one we are colorizing the flowers.
[13:18] And all of that mixed together we get something like this.
[13:28] And also adding a background color, this beige color.
[13:36] As you can see in here.
[13:40] And for the mix I am using the two masks added together.
[13:55] Then I'm also adding the stitches, adding some color to the stitches,
[14:05] by importing that particular mask that I've picked.
[14:11] And then just multiplying the noise on top.
[14:22] And we get something like this.
[14:32] And let's switch to the shader, main shader.
[14:42] And as you can see for the I am using two normal maps in here.
[14:54] So in order to connect them you can create a normal map.
[15:02] Import the image, create a normal map and then connect the second normal map to the normal of the first one.
[15:11] So I believe I'm using these normal map in here.
[15:17] And a textile normal map for the main color.
[15:29] And of course we're using the displacement as you can see in here.
[15:33] It's creating this waving effect and also the stitching.
[15:38] Which is a bit too big, but I guess now I won't change it.
[15:48] So that's basically it.
[15:52] I hope you have learned something new.
[15:55] As always you can get the files on my Patreon.
[15:59] And thank you everyone that is supporting me over there.
[16:03] That helps me to continue to create these tutorials and share project files with you guys.
[16:11] Thank you for watching. See you next time.



---

## Captured Frames

- [0:10] tutorials/frames/custom-procedural-materials-with-houdini-and-karma/frame_000.jpg
- [1:35] tutorials/frames/custom-procedural-materials-with-houdini-and-karma/frame_001.jpg
- [4:40] tutorials/frames/custom-procedural-materials-with-houdini-and-karma/frame_002.jpg
- [7:15] tutorials/frames/custom-procedural-materials-with-houdini-and-karma/frame_003.jpg
- [11:35] tutorials/frames/custom-procedural-materials-with-houdini-and-karma/frame_004.jpg
- [15:05] tutorials/frames/custom-procedural-materials-with-houdini-and-karma/frame_005.jpg

---

## Structured Notes

### Core Technique
Building a procedural "old mattress" tufted-fabric material for Karma/MaterialX by generating low-poly geometric proxies (bulge pattern + stitching pattern) purely from curves/copies/clips, baking color+normal+displacement maps from those proxies onto a flat plane, then combining the baked maps with layered noise inside a MaterialX shader network.

### Summary
Covers three linked stages: (1) building a tileable bulging/tufted pattern from curve-clip geometry and displacing it via a boundary-distance mask to fake a puffy mattress surface, (2) building a separate embroidered stitching pattern from a traced reference image using the same alternating-curve-cut trick (helped by Houdini 20's new Carve by Attribute node), and (3) baking both hi-res proxies down to color/normal/displacement maps on a flat low-res plane, then assembling a full MaterialX shader that layers noise, the baked flower/stitch masks, and two chained normal maps to produce the final upholstered-fabric material rendered in Karma.

### Key Steps
1. **Bulge/tufted pattern geometry:** Start with a circle → Carve → save its bounding-box size as an attribute → Copy the curve several times, centered → Box Clip using the saved bbox X/Z attributes to extract a tileable pattern → Polypatch (curves aren't joined) → group center points and cut, yielding 4 separate wedge shapes forming one tile.
2. **Squaring the tile:** Since the raw tile isn't square, use a Transform where the scale = (largest bbox axis) / (smaller bbox axis) applied to the larger axis, producing a square tile that can be baked to a square texture; re-save the new bbox size for reuse.
3. **Building the bulge mesh:** Copy the squared pattern into a grid, sort primitives by proximity to points, range-select the last four primitives, group one, blast the rest, grid the polypatches, Polyfill, blast away the curves, and remesh.
4. **Bulge displacement mask:** Group the unshared (boundary) points of each patch, run Distance Along Geometry from that group to build a radial falloff mask, blur it slightly, then use a Point VOP/Point Wrangle to displace points along normal by that distance-based mask — producing the bulging/tufted look.
5. **Color-map prep for baking:** Rebuild the same clipped pattern, generate connectivity, re-clip with the saved bbox size, then cut all primitives by point and (in a wrangle) assign an alternating attribute per primitive (e.g. "red, blue, red, blue...") so **Carve by Attribute** (new in Houdini 20) can split the curve alternately without a manual Blast; sweep the result and color it, and this becomes the bake source for the iris/color detail.
6. **UV setup for baking:** Create a flat rectangular bound plane, group the top vertices, and use UV Flatten with those pinned vertices to properly orient the UVs before baking; add extra subdivisions to the low-res mesh since it helps bake quality; bake color and displacement (height) maps — displacement needs normalizing/equalizing to be visible since raw values are subtle.
7. **Stitching-pattern geometry (second pattern):** Trace a reference image and place it flat on the ground; divide the plane along Z by computing (bbox Z size / desired division count, e.g. ~150) — repeatable per axis; group inner edges by mean edge angle, dissolve, and build curves from that edge group; Fuse polypatches into single primitives and resample; use Polycut to cut primitives, removing every second curve (same alternating-pattern idea as before); Sweep the result to get 3D stitching geometry.
8. **Stitching bake:** Import a traced/painted reference texture via Attribute from Map (a flat mesh doesn't need much subdivision since colors spread out fine), promote the color to primitives for flatter shading, add a background plane so bakes don't render transparent, and bake normal + color maps for both hi-res and flat low-res proxy meshes (max-ray-distance setting lets overlapping bake geometry work fine); can layer in an external, tileable found texture (a flower pattern) as long as it tiles seamlessly and is manipulated to fit — perfectly fine within a procedural workflow.
9. **Shading (MaterialX/Karma):** Build the surface from a **Unified Noise** (Worley-type) disturbed/distorted by a second fractal noise for the base "waviness"; import the baked flower-pattern texture and split it into channels via a Separate/Vector-to-Float node, then remap/clamp channels to isolate leaves vs. flowers masks; use **Color Mix** nodes driven by those masks to colorize leaves and flowers separately, add a beige background color, and use the sum of both masks as the final mix factor.
10. **Stitch coloring + normal layering:** Import the picked stitching mask to color the stitches, multiply the base noise on top for subtle variation; chain **two Normal Map** nodes (import image → Normal Map node → feed as the "normal" input of a second Normal Map node) to combine the mattress-bulge normal with a separate textile-weave normal map; plug the baked displacement into the Displacement input for the waving/bulge effect, and route the baked stitching displacement in as well (noted as "a bit too big" but left as-is).

### Houdini Nodes / VEX / Settings
Nodes/techniques used: Circle, Carve, Copy to Points (bbox-based), Box Clip, Polypatch, Group Create (center points / unshared points / bbox), Blast, Transform (non-uniform scale to square a pattern), Sort (by proximity to points), Polyfill, Remesh, Distance Along Geometry, Blur, Point Wrangle/Point VOP (mask-driven displacement along normal), Connectivity, Attribute Wrangle (alternating per-primitive attribute), **Carve by Attribute** (new in Houdini 20), Sweep, Color (constant, keyed blue for masking), UV Flatten (with pinned vertices), Attribute from Map, Bake Texture (color + displacement + normal, hi-res and low-res flat proxy), max-ray-distance bake setting. Shading (MaterialX): Unified Noise (Worley), fractal noise disturbance, Separate Color/Vector to Float, Remap, Clamp, Color Mix (mask-driven), two chained Normal Map nodes, Displacement input on the Karma surface/displacement shader.

### Difficulty
Intermediate/Advanced — no complex VEX, but requires understanding of bbox-driven tiling patterns, UV baking pipelines (hi-res to low-res), and layered MaterialX shading with multiple normal maps and mask-driven color mixing.

### Houdini Version
20.5 (references "new to all in the 20" for Carve by Attribute; UI matches 20.5 Karma/MaterialX workflow).

### Tags
#modeling #texturing #uv #baking #materials #shaders #mtlx #karma #procedural #intermediate

---

## Related Tutorials
Cross-link with any other cgside COPs/materials/baking-focused tutorials (e.g. designer-like materials in COPs, custom procedural materials series) once extracted from this batch.
