---
title: Optimizing Baked Trees with Instancing in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=0C8ek1aDe8o
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.590"
tags: [instancing, optimization, vex, matrices, opacity-to-mesh, hda, vegetation, python, usd, solaris]
extraction_status: complete
frames_dir: tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Optimizing Baked Trees with Instancing in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=0C8ek1aDe8o)
**Author:** cgside
**Duration:** 13m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So I've been working on this HDA that converts
[0:05] opacity raised leaves to geometry as you can see by this example. But the problem
[0:11] is when you have an asset for example that's you have a lot of geometry like a
[0:17] tree that's this tree for example is from Max tree and it comes already baked
[0:23] with all the geometry and is really eye-poly. If we try to convert this as you
[0:29] can see we have opacity based leaves and in case you want to convert this this
[0:34] will take a while to compute. I already have this sketched and so we
[0:39] doesn't take too much but this will take like 20 seconds 30 seconds to compute
[0:45] all this geometry and you end up with in this case 4 million 4 and half
[0:49] million points which is not ideal. So my idea was to extract one of the leaves
[0:56] and reset the transforms to the origin then do the conversion as you can see
[1:03] and then extract the orientatribute from the original leaves. I can show you
[1:09] the original leaves overlayed over and as you can see I successfully re-
[1:14] extracted the transform or the orientatributes and then you can copy to points
[1:18] and pack an instance and you only get the you get a version which is really
[1:24] optimized and you can export these to USD and render in salaries or even export
[1:29] only the points the point clouds with the transform attributes and you can
[1:35] instance in salaries if you prefer like. So to the in today's video I'm gonna show
[1:39] you how you can do that. So we have our bake assets let me just get rid of these
[1:46] attributes so we have the geometry and fortunately we have a shop material pet
[1:51] with or a name attribute with the leaves and whatnot so I'm extracting in
[1:55] here the the leaves then within the leaves I'm calculating a connectivity and
[2:04] these will give us an ID for each leaf and if you shake and we go to primitives
[2:10] we have around well almost 40,000 in different leaves. Then I'm promoting the
[2:18] UVs to point to a point attribute by by splitting the UV seams and promoting
[2:25] to point attribute. Now we have our UVs on points and if you notice we have all
[2:29] the leaves we only have one variation so you'll have to adapt to your
[2:32] different scenarios. So we have the UVs always in the same position for all
[2:38] the leaves so we can easily extract this point in here and from there we can do
[2:44] further operations. So I'm gonna blast in here the class zero or you can blast
[2:49] any random class I'm just going start with zero so we have this geometry in
[2:55] space which is just class zero. Then from here I'm selecting the back point so
[3:01] in this wrangle I'm just since I have the the UVs always in the same position I'm
[3:07] unwrapping in place with this geo unwrap and getting the bounding box center of
[3:11] this UV geometry and then the bounding box mean. From there I'm manipulating the
[3:17] two positions and do in a detail mode a near point to find this point and I'm
[3:23] also saving the that point position on a attribute called center. So right now
[3:29] we will have a attribute in here called center which grabs the UV position, the
[3:39] UV position of that so why is not showing so zero one and two so grabs the UV
[3:46] position of that point. From there let me connect this in here so I'm doing a
[3:54] clip and this clip will run on the UVs and I'm selecting only the
[4:00] exposition of that center attributes so I'm connecting in here and this will let
[4:06] me get rid of this visualization as you can see is clipping right there. Then we
[4:11] can convert to line the clip edges that we saved previously and we will get
[4:16] something like this which relates to the tree and we can also extract the scale
[4:21] with the rest lines. Then we attribute promote these to a point
[4:27] attributes and do a re-sample with one segment to get only this line in here.
[4:34] Then we do an oriental on curve and in here I'm just saving the tangent as an
[4:39] attribute as you can see we have a vector going along our curve. From there we
[4:45] can compute the transform attributes so if I show you that I have this matrix
[4:50] in here and it's not really visible because I need to enable let me just
[4:57] increase the size. So in here I'm just using the look at function to create all
[5:03] the necessary cross products and we get we feeding the from a from vector then
[5:11] we feed the end to the two inputs and then an up which is just along the
[5:16] Y. Then we need to translate to in order to have proper four by four matrix
[5:21] that we will need. We need to translate the position also on the translate the
[5:26] matrix with the current position. Then we just save out the matrix and as you
[5:30] can see we have the Z axis maybe it's difficult to see we have the Z axis going
[5:35] along the curve the Y axis pointing out and the X axis on the local X axis. So we
[5:42] successfully extracted the transform then we can do a curve and extract only the
[5:48] first point this is the point that we're going to winstance and that's our
[5:53] compile block that's I'm running in here as you can see so is the same result as
[5:58] this. So we get this point then it's really simple we take the original
[6:05] blasted isolated leaf and we invert the transform with that matrix and we get
[6:12] the geometry at the center and oriented along the Z axis. Then we can do a unit
[6:17] transform because I'm also going to input a scale attribute I will show you in a
[6:22] bit and this just takes the target scale and divided by the Z size of the
[6:28] original geometry. So we get like 1.2 scale on the Z axis. You can set it just to
[6:38] 1.0 but since I have some geometry going back I gave it a little bit of run.
[6:43] So now we have the single leaf we just need to do the same for all the points.
[6:49] So we need to extract to transform for all the leaves. So if you remember we
[6:55] extracted that center position on the UVs so what we can do is to copy that
[7:00] the detail attribute so we copy to this geometry that UV position which will
[7:05] be the same for all the leaves and then we do the invoke which is the same as
[7:09] this clip convert line and computing the matrix and if we wait a while we will
[7:15] have all the points with the respect it transformed. Then we need to
[7:22] multiply it a bit the such roots this matrix because we need actually to set
[7:27] a transform so the copy to points can read it. So reading the matrix then we
[7:33] make sure we reset the position so we translate the matrix to minus V at P.
[7:37] Then we scale with the rest length that we computed in here so if you remember
[7:45] and finally we can assign this to a transform a true then cast it to a matrix
[7:51] for and if you look at that transform attribute it will look pretty similar to
[7:57] our matrix and then we can just copy to points and if we go back and look at
[8:05] the original geometry it should reserve the position the orientation and the
[8:09] scale. So it's a neat trick I wanted to show you hopefully that was useful and
[8:16] of course in here I forgot to show you that after we have the single leaf we
[8:22] promote the UVs to vertex and then we do the opacity to mesh. So I wanted to
[8:29] show you right now this opacity to mesh workflow so for example in here I'm
[8:34] gonna post the HDA on my Patreon shop if you're interested in buying it will
[8:40] be pretty cheap so don't worry. So I'm loading in some geometry in this
[8:45] case this is Fern. In this case I'm just deleting the color because I don't want
[8:50] to see the color and then doing the opacity to mesh. Basically you just load in
[8:54] the opacity file you set a remesh size which is how much geometry you want.
[8:59] Then you have in here the step size which these nodes uses a trace to trace the
[9:05] opacity map and this is the setting for the resample. So if in this case by
[9:10] default is set to 50 and this takes a while to remesh as you can see it's not
[9:15] very true to the original geometry because we don't have enough points for
[9:21] the resample so you want to reduce it to something like that and as you can see
[9:25] the trace will take a while because now is an ivory sample and also the
[9:30] remesh is a bit high so you get these results. But this is an extreme case so
[9:37] for example this is mega scans then I have for example in here a asset from
[9:42] PolyAven which as you can see are also opacity based let me see if I can show
[9:49] you in here as you can see you can see the the black border in here and then I
[9:54] just convert it to geometry and in this case I can tell the system that this
[10:03] is only using leaves and I can transfer any attribute I want so by default it
[10:09] will transfer the position otherwise this will be in UV space so make sure
[10:12] you always transfer the position to have the original position and you can
[10:16] also transfer the material if you have a material or any other attribute that
[10:21] the mesh notes by default so you can see I'm only transferring position and
[10:26] material shop material pet and you can see this is only calculating for the
[10:33] leaves this is an optimization in case you don't have any stems or flowers or
[10:40] branches so like 3D geometry as you can see in here for example I have these
[10:47] shrunks and I also have these I can say these are flowers or something like
[10:53] that so in here I can't only input lips if you have an option to isolate the
[10:58] leaves if you have an image reboot it will be faster to isolate the leaves but in
[11:04] this case I don't so I need to play with these thresholds so this
[11:09] threshold will is a value that will find the lips so basically I select the
[11:15] leaves from these 3D geometry let's say so if I change this default value I
[11:20] think is 0.1 and this takes well because we have a lot of geometry but as you
[11:26] can see these ones work very well in here it will just treat it as lips so we
[11:33] need to increase a bit this threshold so you have to play with the values this
[11:37] is an extreme case and as you can see it's a successfully isolated lips and
[11:43] this geometry this 3D geometry remains original to the input mesh so what
[11:52] else can I show you so far I can show you another example in here so as you
[11:55] can see we have these these tubes in here and in this case a value a threshold of
[12:01] 0.1 will work fine and in here if you want to do well the lips at once and
[12:06] skip all these instances in step we can select only lips because otherwise
[12:13] these will take a while if we didn't isolate the lips this would take really a
[12:17] lot of time so in this case we can just input only lips and it will work fine
[12:23] let me actually try to try to show you how much it takes to compute all these
[12:30] lips so is reloading the file first so it's not counting and now is doing the
[12:37] opacity based conversion and as you can see it takes a little bit and there you
[12:43] have it but it's always better to do this workflow of instance in the the
[12:50] lips so we have way less memory issues so again this HTA it will be available
[12:58] on my patreon shop if you want to have a look and other than that I hope this
[13:05] was useful I try to fit in the promotion of the HTA with this cool trick of
[13:12] getting baked geometry into instance geometry so hopefully you'll find some
[13:17] value and as always you can grab the files on my patreon alongside with
[13:20] exclusive tutorials and yeah thank you for watching please leave a comment and
[13:25] I'll see you next time thank you



---

## Captured Frames

- [0:20] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_000.jpg
- [1:40] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_001.jpg
- [4:20] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_002.jpg
- [5:20] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_003.jpg
- [6:40] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_004.jpg
- [8:40] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_005.jpg
- [10:20] tutorials/frames/optimizing-baked-trees-with-instancing-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
Convert a heavy, pre-baked opacity-leaf tree asset (millions of points) into a lightweight instanced asset by extracting a single representative leaf, resetting it to the origin, then re-deriving each original leaf's position/orientation/scale as a matrix so the single leaf can be `copytopoints()`-instanced back — massively reducing memory/point count versus converting every opacity leaf to full geometry.

### Summary
Baked, high-poly assets (e.g. from MaxTree/Megascans) with opacity-mapped leaves are expensive to convert to real mesh at full resolution (millions of points). Instead of converting every leaf, the video extracts one leaf, zeroes its transform, converts it once, then reconstructs a per-leaf transform matrix (via `nearpoint()`, `clip`, `convertline`, `resample`, `orientalongcurve`, and `maketransform`/`lookat`) from each original leaf's UV-space "center" reference point, so all leaves can be recreated cheaply via Copy to Points → Pack and Instance. The same author's separate "Opacity to Mesh" HDA (sold on Patreon) is also demonstrated for converting opacity-based foliage assets (ferns, PolyHaven shrubs) into real geometry directly, including a leaf-isolation threshold control for mixed leaf/stem/flower assets.

### Key Steps
1. Isolate the leaves group from the baked tree using its `shop_materialpath`/name attribute, then run **Connectivity** to assign a per-leaf class ID (~40,000 leaves in the example tree).
2. Promote UVs to a point attribute (splitting UV seams first) so each leaf's UVs sit at consistent positions across all leaves (since MaxTree/Megascans leaves reuse one atlas layout).
3. Blast out a single leaf (class 0) to work on in isolation; unwrap in place (`geo unwrap`), compute the UV bounding-box center via a detail-mode `nearpoint()`, and store that point's world position as a `center` attribute.
4. **Clip** the leaf using its UVs at the `center` X position, **Convert Line** the clip edges to build a small curve relating to the tree's branch, then attribute-promote and **Resample** (1 segment) to collapse it to a 2-point line; **Orient Along Curve** stores the tangent as a vector attribute.
5. Build a 4x4 transform matrix per leaf using `lookat()` (feeding "from"/"to" vectors and an up vector along Y) inside a wrangle, then translate the matrix by the current position to get a proper world transform (Z axis along the curve, Y pointing out, X on local X).
6. Extract just the curve's first point (the point to instance), invert the single isolated leaf's transform using that matrix (bringing it to the origin, oriented along Z), then use a **Unit Transform**-style scale (target scale ÷ original Z-size) to normalize leaf length — this whole block runs inside a **Compile Block** for performance.
7. Repeat the matrix-computation chain (clip → convertline → matrix) for every leaf simultaneously by copying the detail `center` attribute onto all leaf points, so every leaf gets its own respective transform.
8. Convert the computed per-leaf matrix into a Houdini `transform` attribute readable by Copy to Points: translate the matrix by `-P` (reset position component), scale by the stored rest-length, cast to a `4@transform` matrix.
9. **Copy to Points** the single optimized leaf onto all the per-leaf transform points, then **Pack and Instance** — reproducing the original tree's position, orientation, and scale with a fraction of the geometry, exportable to USD or as instanced point clouds for Solaris.
10. (Separate demo) The author's **Opacity to Mesh HDA**: load an opacity texture, set remesh size and trace/resample step size, transfer position (and optionally material) attributes so geometry isn't left in UV space, and use a "select only leaves" threshold + isolation-mask option to skip non-leaf 3D geometry (stems/flowers) for large mixed assets — dramatically faster than converting the whole mesh when leaves are pre-isolated.

### Houdini Nodes / VEX / Settings
Attribute Delete, Connectivity, Split by UV seams + Attribute Promote (UV to point), Blast (isolate one class), `geo unwrap`, detail-mode `nearpoint()` wrangle (stores `center` attribute), Clip (on UVs), Convert Line, Attribute Promote, Resample (1 segment), Orient Along Curve, VEX wrangle with `lookat()`/`maketransform`-style matrix construction (from/to/up vectors), Compile Block, Unit Transform (target scale ÷ Z-size), Transform (matrix translate by `-P`, scale by rest length), Copy to Points, Pack and Instance; separate **Opacity to Mesh** custom HDA (Patreon) with remesh size, trace step size/resample settings, position/material attribute transfer, and a leaf-isolation threshold for filtering 3D stem/flower geometry.

### Difficulty
Advanced (VEX matrix construction with `lookat()`, curve-based orientation extraction, and compile-block optimization assume solid procedural/VEX fundamentals).

### Houdini Version
19.5.590 (visible in viewport title bar).

### Tags
instancing, optimization, vex, matrices, opacity-to-mesh, hda, vegetation, python, usd, solaris

---

## Related Tutorials
- [Opacity Maps vs Geo in Karma](opacity-maps-vs-geo-in-karma.md) — companion render-optimization technique tackling the same opacity-leaf performance problem from the rendering side rather than the instancing side.
- [Environments in Houdini Part 3 - Vegetation with Simple Tree Tools](environments-in-houdini-part-3---vegetation-with-simple-tree-tools.md) — shares the same author's Opacity-to-Mesh HDA workflow for converting foliage plugin assets to real geometry.
