---
title: Procedural Pizza in COPS
source: YouTube
url: https://www.youtube.com/watch?v=mL2TkAB_Rqc
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [cops, materialx, procedural-texturing, stamping, leaf-generation, uv, rasterize, karma, food]
extraction_status: complete
frames_dir: tutorials/frames/procedural-pizza-in-cops/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Pizza in COPS

**Source:** [YouTube](https://www.youtube.com/watch?v=mL2TkAB_Rqc)
**Author:** cgside
**Duration:** 12m56s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Creating the pizza crust [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this tutorial I'm gonna be breaking down some of the parts of this procedural piece of material in Cops.
[0:09] If you want to have access to the full scene you can download it from my Patreon, but I will break down the most interesting parts. So yeah let's get into it.
[0:19] So we will start from the beginning. The first thing I did was to play around with the Crest material and the displacements to have this rounded look.
[0:30] And the way I'm doing that I start with the ring, play with the size, compared to the SDF to a mono and also smooth it a little bit.
[0:39] So I can have that typical rounded look and I can connect this to a preview material and connect this to the height.
[0:48] Let's right away play with the size, 0.01, change this to grid, divisions to 500 and let's see how that looks.
[0:57] So as you can see it doesn't look like that, so I need to increase this to 0.01 let's say.
[1:03] And as you can see this will give us this pointy shape which is not ideal.
[1:10] So the way I'm solving that is by blurring, but as you can see it will blur everything.
[1:16] Then I blend it with minimum modes with the original texture and I get this sort of result and then I just blur it a little bit more.
[1:25] And I get the desired result. If I increase these a little bit to 0.2, you start to see the results.
[1:32] So it's not perfect but it was the way I found to create these rounded look while keeping some sort of sharp corners.
[1:40] Then I'm also distorting this shape, so I'm creating this distortion, but I don't want the effect on the interior to be the same as the exterior part.
[1:51] So I'm creating a masking here to change the scale of the distortion.
[1:58] And if we look at the final result it will look something along those lines.
[2:04] And then I'm also adding some breaks on the crust and it's funny how I did that.
[2:12] I started with this asterisk shape which thinking about it doesn't make much sense to use these in any project, but in this case it was useful.
[2:22] So converting it to mono, blending with some noise, eroding it a little bit, transforming it and distorting it.
[2:29] And then when we blend it with the original shape we get this sort of result which will look something like this.
[2:37] In this case it will look to random, but when blended over the blurred result and the other materials it will look something like this.
[2:48] So as you can see in here it will have these breaks on the crust which was the sort of look I was after.


### Procedural leaf generation [2:55]
**Transcript (timestamped):**
[2:56] So the most challenging part was definitely the leaves, these leaves that go on the pizza and I'm gonna be breaking down how I did that.
[3:05] So I'm creating them in soaps and this is the powerful thing about cops that you can combine it with the other parts of Odini in this case soaps.
[3:16] And then resurrecting it to create the materials in cops.
[3:22] So I'm starting with the line with sampling and creating the curvy attribute, then deforming it to a leaf shape just by setting the normals and deforming it along the normals, play with the ramp, mirroring and from here I'm creating a polypath to unify the shape,
[3:40] polyfill it to have some geometry and adding some normals and then removing the curve.
[3:47] So this is the leaf base and for the lines I'm just copying two points a few lines.
[3:53] First of all I'm carving a little bit the top and bottom so I can control the position of the veins let's say.
[4:03] Then reassembling it and in here I'm setting the normals and let's have a look how I did that.
[4:10] Basically I'm creating the normals between one and minus one in the X axis and also creating the the aperture both the same way so I can rotate it later.
[4:24] And it's really simple we just use the modelo so we have 0 and 1 repeating and then scale it multiplied by 2 and subtract 1 to have 0 centroid offset so minus 1 and 1.
[4:36] This way it will alternate between the points minus 1 and 1.
[4:41] Then I'm doing a attribute adjust factor and rotating randomly the app the normals along the aperture boot as you can see that's why it was important to create that aperture boot.
[4:52] And then just playing with the p-scale and we get this sort of result if I can add your normals.
[5:01] And then we can re-project it to the the leaf mesh as you can see to create the veins re-sampling it and I'm also creating some vectors in here with the cross product so I can deform it down along the curve you as you can see in here.
[5:18] And then we can re-sample it again to have less points and re-sampling less time and set it to subdivision curves and we get this sort of result.
[5:30] So this is a very basic leaf that that will work for our purpose.
[5:35] I also did something here so after getting the interior part of the leaves I'm creating along after remaching also the leaf.
[5:45] I am creating a near-point group and along with the unshared.
[5:51] So in here I'm combining the two groups so I can create a mask to play with the interior parts of the leaf as you can see in here.
[6:01] If I normalize the attribute you can see the result and I'm doing that by using the surface distance function we covered that before we start with the group of points.
[6:11] And then we measure the distance between the group and the interior part.
[6:17] Then we do a attribute blur and we have everything we need for our stamping or our restoration let's say.
[6:25] So I'm re-sampleizing here the alpha which will be just the leaf and the leaf interior because I also have a attribute set in there as you can see in here, life interior.
[6:37] And also the surface distance as you can see this will help us to create that bump effect on the interior parts of the leaf.
[6:46] Creating the color and in here I'm applying a distortion to both to weld the shapes and also creating some noises for the shading.
[6:59] And I'm applying the distort to weld the attributes so I can stamp them within the same position and still have access to them as you can see that way I can blend the different layers later or the shading and the displacement also.
[7:15] So as you can see in here if I check the stamp we have the stamp we have the final result but if I look at the ID we have a different ID for the interior parts that way I can come in here, here we have.
[7:28] So if I check this compare I gave the ID of the interior parts the veins an ID of 999 so I can isolate that with a compare and then we can just blend in that attribute.
[7:43] So that's basically how I've done those leaves then I blend I also created some I also created some curling on the leaves or some band as you can see they are not flat and the way I'm doing that is by is by extracting the UVs that we have in here let's see.
[8:08] So we have here the UVs and then in here I am creating a ramp from the UVs with this inverted yield ramp and then I just blend it over our displacement map.
[8:21] So in this case I am blending them in here in here as you can see I'm multiplying over to the leaf shape to have that curling effect.
[8:32] So yeah that's mainly how I created the leaves hopefully you got some tips out of this and let's move on.


### Cloth material techniques [8:40]
**Transcript (timestamped):**
[8:40] So now I wanted to show you how I created the cloud material which on itself is quite boring but it can show us a feature or two about the scops workflow.
[8:54] So let's look first at this top import where I'm creating the points to do the stamping.
[9:00] So I'm starting with the grids with four primitives and if you look at the primitive numbers we have 0, 1, 3, 2.
[9:09] So I want this in a circular pattern so I can iterate over each two sections each two primitives and create the stamp attribute so we can overlay different colors in cups.
[9:20] So first of all I'm sorting them in a circular pattern the way I'm doing that is just by reversing the primitive order of the second and third primitives so 0, 1, 2, 3.
[9:30] Then I'm doing a 4-inch, it is called 4-inch count for each number.
[9:35] 4-inch number and I'm setting these two 4 iterations since I want four sections out of this grid.
[9:41] Then in a group range I'm selecting two primitives out of four and as an offset I'm using the 4-inch count the iteration attribute as you can see in here.
[9:51] And these will iterate over each two sets of primitives.
[9:57] Then blasting those isolated primitives in the group range is writing this and troid and here I'm setting the stamp attribute to be the iteration attribute as you can see.
[10:08] And we will have 0, 1, 2 and 3 so after each iteration and these will merge the points so we will have eight points.
[10:18] And now in here we can do the stamping and I'm stamping the first stamp will be the first and last stamp will be this white color and the second and third will be this blue.
[10:29] And if we set it to default we will have this sort of result but we've unsorted that weighted over we get this blending effect of the different stamps.
[10:42] And then we can move it to the center by translating in x and y 0.5 and then just repeat it with the uniform scale transform as you can see.
[10:52] And finally we can add some noise over the top some noise that is scaled along the X as you can see.
[10:58] And so the main takeaway is this stamp ID that we can blend with these as you can see we can change it in here the blending and get some different results.
[11:11] So yeah that's how I created the cloud material and other than that if you are interested in this full scene you can check it out on my patron how I did the normals and everything.
[11:27] And hopefully if I showed you the most interesting parts you can look in there how I did the slicing of the piece because I'm also creating that in sobs and then blending over the we can actually go over that.


### Finalizing pizza slice [11:41]
**Transcript (timestamped):**
[11:42] So in this case to do the slicing I'm starting with a circle which is white dancing divisions but it's a number that we can divide easily.
[11:55] And then doing a class attribute in here to divide it by 8.
[12:01] Blasting the part I want in this case I can change the piece in this case I chose 5 remove the unchared and doing a basic inset so I can have an attribute to play with in in cops.
[12:17] So that's basically how I've done that slicing then I'm in here I'm isolating that slice and isolating the rest transforming the slice and blending it over.
[12:30] And this is how it looks the final albedo texture as you can see.
[12:35] So yeah a lot of work it looks somewhat decent again if you are interested in the material check out my patron where you can find lots of tutorials exclusive tutorials.
[12:46] Courses and all the project files from my videos let me know in the comments if you found this useful and I guess I'll see you next time.
[12:54] Thank you.



---

## Captured Frames

- [0:57] tutorials/frames/procedural-pizza-in-cops/frame_000.jpg
- [1:25] tutorials/frames/procedural-pizza-in-cops/frame_001.jpg
- [3:22] tutorials/frames/procedural-pizza-in-cops/frame_002.jpg
- [5:22] tutorials/frames/procedural-pizza-in-cops/frame_003.jpg
- [5:01] tutorials/frames/procedural-pizza-in-cops/frame_004.jpg
- [6:37] tutorials/frames/procedural-pizza-in-cops/frame_005.jpg
- [9:41] tutorials/frames/procedural-pizza-in-cops/frame_006.jpg
- [12:08] tutorials/frames/procedural-pizza-in-cops/frame_007.jpg

---

## Structured Notes

### Core Technique
Build a full procedural pizza-slice texture set (crust, leaf toppings, cloth/napkin, sliced albedo) entirely in **Cops (COPs)**, using SOPs only to generate leaf geometry that is then stamped/resurrected as a texture layer — combining Rasterize/Stamp workflows, VEX-driven point placement, and a "surface distance from group" mask to fake bump/interior detail on 2D texture layers.

### Summary
The crust look starts from a ring compared against an SDF, smoothed to get a rounded profile, then previewed via a height/displacement connection; a pointy artifact from a small grid-division size is fixed by blurring and blending with Minimum mode against the original texture (repeated at increasing scale) to keep some sharp corners while rounding the rest. A separate distortion pass is masked so the interior distorts differently than the exterior, and a "crust breaks" detail is faked by converting an asterisk shape to Mono, blending with noise, eroding, transforming/distorting it, then blending over the base crust shape. The most involved part is generating basil/oregano-style leaves: built in SOPs from a Line with curve-parameter sampling, deformed into a leaf silhouette via normal displacement and a Ramp, mirrored, Polypath'd to unify, Polyfilled for geometry, then the curve is removed. Veins are added by copying two points per line, carving top/bottom to control vein position, and setting per-point normals using a modulo-based alternating (-1/1) "aperture" attribute so an Attribute Adjust Vector can randomly rotate normals along that aperture — the result is re-projected onto the leaf mesh, resampled, and converted to Subdivision curves for a simple usable leaf. Interior "bump" detail is faked using a **near-point group** + **surface distance** measurement between an interior point group and the leaf boundary, blurred to create a soft mask usable for stamping. The leaf is then resurrected/stamped into Cops with an alpha (leaf shape + leaf-interior sub-ID) and the surface-distance attribute, with a distort pass applied to weld shapes so different stamped layers (shading, displacement) stay in registration; a Compare on a dedicated ID (999 for veins) isolates the interior for separate blending. A subtle curling/banding look on the leaves comes from extracting the UV coordinates, building an inverted ramp along one UV axis, and multiplying that over the displacement map. A simpler "cloth material" section demonstrates a Cops stamping trick: a 4-primitive grid is reordered into a true circular primitive sequence (reversing prim order on two of the four prims), then a for-each loop over 4 iterations uses Group Range (offset by the iteration attribute) to isolate 2 primitives per iteration, sets a "stamp" attribute to the iteration number, and blends different colors per stamp ID — centered via translate + uniform-scale transform and finished with X-scaled noise. Finally, the pizza slice cut is done by taking an 8-division circle, using a class attribute to divide it into eighths, blasting/keeping one wedge (piece 5), removing unshared edges, and insetting for an extra playable attribute in Cops — the isolated slice and the rest of the pizza are transformed and blended together to produce the final albedo.

### Key Steps
1. **Crust base shape:** build a ring, compare against an SDF converted to Mono, smooth slightly, connect to a preview material via height/displacement.
2. Fix pointy grid-tessellation artifacts (small size + high grid divisions) by **blurring**, then **blending in Minimum mode** with the original unblurred texture (repeated at increasing scale/strength) to retain sharp corners while rounding the rest.
3. Mask the interior vs. exterior separately so a **distortion** pass can use a different scale on each region.
4. Fake **crust "breaks"**: start from an asterisk shape, convert to Mono, blend with noise, erode, transform/distort, then blend over the base crust for random surface breaks.
5. **Leaf base geometry (SOPs):** Line with curve-parameter sampling → deform along normals into a leaf silhouette using a Ramp → mirror → Polypath (unify) → Polyfill → add normals → remove curve.
6. **Leaf veins:** copy 2 points per line, carve top/bottom to control vein placement, reassemble, then set per-point normals using a **modulo alternation** (0/1 scaled ×2 minus 1 → range -1..1) to build an "aperture" attribute; use **Attribute Adjust Vector** to randomly rotate normals along that aperture, adjust p-scale, re-project onto the leaf mesh, resample, convert to Subdivision curves.
7. **Interior bump mask:** build a near-point group + an "unshared" boundary group, combine into a mask via **surface distance** (distance from the interior point group to the boundary), then Attribute Blur for a soft usable stamping mask.
8. **Stamp/resurrect into Cops:** re-rasterize the alpha (leaf shape + leaf-interior sub-ID via an ID of 999 for veins) plus the surface-distance attribute; apply a distort pass to weld shapes across layers so shading/displacement stamps stay aligned; use **Compare** on the vein ID to isolate and separately blend the interior detail.
9. **Leaf curling:** extract UV coordinates, build an inverted Ramp along one UV axis, multiply that ramp over the displacement map to fake curling/banding.
10. **Cloth/napkin stamping trick:** reorder a 4-primitive grid into circular order (reverse prim order on 2 of 4 prims), for-each over 4 iterations, Group Range offset by the iteration attribute isolates 2 prims per iteration, set "stamp" attribute = iteration number, blend colors per stamp ID (default vs. unsorted-weighted blending), center via translate 0.5,0.5 + uniform scale transform, finish with X-axis-scaled noise.
11. **Pizza-slice cut:** 8-division circle → Class attribute divides into eighths → Blast/keep one wedge (piece 5) → remove unshared edges → Inset for an extra Cops attribute → isolate the slice and the remainder, transform and blend together for the final sliced albedo texture.

### Houdini Nodes / VEX / Settings
Cops: Ring, SDF to Mono, Smooth, Blur, Blend (Minimum mode), distortion node with interior/exterior mask, Mono conversion, noise blend, Erode, Transform, Rasterize/Stamp, ID-based Compare, UV-based inverted Ramp, Grid (4 primitives), For-Each Number loop, Group Range (iteration-offset), Centroid write, stamp-color Blend, Transform (translate + uniform scale), X-scaled Noise, Circle (8 divisions), Class attribute, Blast, Remove Shared Edges, Inset. SOPs: Line, curve-parameter sampling, normal-based leaf deformation with Ramp, Mirror, Polypath, Polyfill, Copy-to-points (2 pts/line), modulo-based aperture attribute (`%`, ×2, -1), Attribute Adjust Vector, Re-project, Resample, Convert to Subdivision, near-point Group, Surface Distance, Attribute Blur.

### Difficulty
Intermediate/Advanced (combines a Cops-native procedural crust/breaks pipeline with a SOPs-built leaf asset resurrected into Cops via stamping and ID-based masking).

### Houdini Version
Not specified.

### Tags
cops, materialx, procedural-texturing, stamping, leaf-generation, uv, rasterize, karma, food

---

## Related Tutorials
- [The Donut Tutorial in Cops (Houdini 20.5)](the-donut-tutorial-in-cops-houdini-205.md) — shares the layered Cops texturing/drip-mask and stamping approach applied there to a torus/donut instead of a pizza.
- [Wood Barrel Texturing in Cops](wood-barrel-texturing-in-cops.md) — another SOPs-to-Cops resurrection pipeline building procedural surface detail for a food/product asset.
- [Tiling Patterns with Cops and SOPs](tiling-patterns-with-cops-and-sops.md) — shares the Cops SDF-stamped tiling and SOPs-circular-cluster for-each approach used for the leaf/cloth stamping here.
