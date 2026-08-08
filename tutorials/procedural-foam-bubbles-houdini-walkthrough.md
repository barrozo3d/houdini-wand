---
title: Procedural Foam Bubbles Houdini Walkthrough
source: YouTube
url: https://www.youtube.com/watch?v=eQBSMVwHB40
author: newa
ingested: 2026-08-08
houdini_version: "19.5+/20.x (Solaris + Karma volumes)"
tags: [bubbles, foam, scatter, non-overlap-packing, pscale, vdb, pyro-bake, volume-shading, thin-film, karma, boolean-avoidance, clip, ambient-occlusion, procedural-texturing]
extraction_status: complete
frames_dir: tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Foam Bubbles Houdini Walkthrough

**Source:** [YouTube](https://www.youtube.com/watch?v=eQBSMVwHB40)
**Author:** newa
**Duration:** 17m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone!
[0:02] Recently I've been playing a bit with bubbles in Houdini and I wanted to share the setup that I'm using for some of the renders.
[0:10] Here is the result of the file that I'm going through right now.
[0:15] So we start out with basic grid, get normal UVs and do extra subdivide.
[0:24] Here in my Copnet I have a logo that I get the alpha off.
[0:30] And I here use the SDF to get a smoother transition.
[0:38] Then this is my height, if I put it in my material. This is the height that I'm getting.
[0:44] So here I'm doing the height on the grid.
[0:50] Then in here I'm just displacing it by the attribute.
[0:54] And when we... oh yes, wait.
[1:00] And when we then do attribute from map from this volume, make sure to have the correct name.
[1:08] Then I just displaced the grid using that attribute.
[1:12] Normalize, do normal second-o-mash and delete the color because this one also creates a color.
[1:20] So then I have a nice smooth mesh.
[1:24] Then I get the ambient occlusion for this because I wanted to have a better outline of the bubbles.
[1:34] Then here I just make the mask 1 minus the height.
[1:42] Then here, this is like the first mask because I didn't want bubbles in the center.
[1:48] Then do a minimum of just some noise. Then add some more noise on top of it.
[1:55] Then remove the ambient occlusion here.
[2:02] We get the minimum of the mask, the invert of the ambient occlusion and the height for the bottom part.
[2:10] So I have three sizes of points, let's say, that I'm using because you could use a dart throwing algorithm.
[2:20] I want to have more control of the shapes and distribution.
[2:25] So here I just draw some zero values from a mask because I don't need points over there.
[2:33] Then I create a scatter with some points using the mask.
[2:38] Then create a p-scale attribute and I placed two extra bubbles because I wanted to have them there.
[2:46] I'm using this to visualize my points as spheres.
[2:50] You could also probably use disks here but it's less good.
[3:02] Or you can do this first so you don't even need this basically.
[3:10] So these are the big bubbles.
[3:14] Then here I'm just setting a frequency for the remesh bubbles.
[3:18] So the bigger ones have more density than the smaller ones so everything has an equal mesh density.
[3:25] Let's say I just give them a group for later on.
[3:29] Then here I draw my mask for the... I know I do a minimum again on the mask to scatter more bubble points.
[3:40] I fix the p-scale here by getting the near points in a certain radius.
[3:46] Then if it's not the current point, then we get our point, we get the position of that point,
[3:55] we get the distance from our current point to that point and then we calculate the p-scale.
[4:02] So this p-scale is just the distance to the closest point divided by two.
[4:08] Then here you could also just do an attribute that just floats and not even this.
[4:14] But here I did some overlapping to get some better bubble shapes.
[4:19] Then here the mask is adjusted.
[4:23] So I look in a certain radius, I create my mask and then for each point in the radius,
[4:32] so like for the 100 points in the 1 radius, I also get the distance from our current point to the point that we found.
[4:41] I get the p-scale of that point and if the distance is smaller than our current p-scale divided by two
[4:51] and the other point p-scale, then mask is 1.
[4:56] So that means if I then remove the points based on the mask, I don't have overlapping points inside of here.
[5:08] And then here I also just set the frequency and create a group for the medium size points.
[5:16] Then here I again have my mask attribute and I create the edge.
[5:25] If you visualize it, it's just like this using the height basically the relative point box.
[5:32] Again, do some noise on the mask, some more noise.
[5:37] Then say then add the edge back on the mask, but make the less bit strong.
[5:43] And then scatter a lot of points here using the mask again.
[5:49] Then we again do the p-scale fix by setting the p-scale to like the closest point that it can find.
[5:56] So they never overlap.
[5:58] But then again, adjust it a bit using some noise.
[6:02] Then here random to get some more variation in sizes.
[6:08] Then here I just do if it's too big then just delete them.
[6:13] I don't know if it's not doing anything even.
[6:16] Then here we again do the same with these points so we don't have points inside of there.
[6:23] So if we then blast these points, we get the non-overlapping points here.
[6:31] And then here yes, it's frequency and a group again.
[6:35] So when we merge everything, some bubbles overlap because that's how bubbles are.
[6:41] But it's not like there are a lot of bubbles inside each other then.
[6:47] Yeah, this was again to preview it.
[6:50] Then here make them overlap a bit more.
[6:55] I use this node to do some camera calling.
[6:59] So if this is my camera, I don't have like points everywhere.
[7:04] You just need to be careful with the reflection of your bubbles that you don't see like that there's nothing anymore.
[7:09] Here I just save my p-scale again because in the remesh bubbles it doesn't transfer the p-scale attribute.
[7:16] So I just created an extra one.
[7:18] Then when we do the remesh bubbles, we get our bubbles.
[7:24] And they are nicely bubbly.
[7:29] So yeah, here yeah, this doesn't matter anymore because we set our frequency ourselves.
[7:39] Then I just added some bulge, made them a bit smoother and did a very small offset for like, get a bit more gaps.
[7:50] Then this group is like the small.
[7:54] And then get the intersecting small ones with when the p-scale is like too big for like the biggest points in the small group to give them some more resolution otherwise like here.
[8:10] You could see like the faces when they're too big so I just simplified them once extra.
[8:17] So then these are like our main bubbles.
[8:20] But I wanted to have like, so here I have my grid.
[8:28] Then I just extruded to have like my soap bar.
[8:33] But I didn't want my bubbles to intersect with the mesh.
[8:37] So what I did was I got my volume and then I displaced the position of the bubbles by the volume.
[8:47] So when we do a clip just on the zero axis like this and then we get our rest position back.
[8:55] We have like the nice cut out otherwise without this.
[9:03] We would just have a flat thing and when we would place it on our soap bar then if you look inside.
[9:13] It's just flat and it's not going inside the thing anymore.
[9:19] So I just add the same displacement to my bubbles, clip it and then just put them back to the rest position.
[9:29] This was a very handy trick because first I was doing it with Booleans but that was way too long to look.
[9:35] So this was a good solution.
[9:37] Here I remove every attribute except these, save my rest position and my rest normals.
[9:44] And these are my bubbles.
[9:48] And yeah, then I just promote this.
[9:51] Do some naming for insularis that I can use.
[10:00] Because I wanted to try and optimize it a bit.
[10:03] I don't know if I still used it but to not have like HRI reflections on the small ones and only on the bigger ones.
[10:11] Because on the small ones you probably wouldn't see it.
[10:13] So that's why I needed names.
[10:15] But then here we can merge the bubbles with our displaced grids.
[10:22] So then we can...
[10:25] Here I got the index.
[10:27] I don't know if I really needed my setup.
[10:31] I was doing some fine attribute fell probably.
[10:35] So that's why I needed the index but I think it's fine without.
[10:41] So what I do is I get my ambient occlusion.
[10:51] Like this.
[10:53] Then I wanted to add some very tiny noise.
[10:58] So yeah, I originally had this.
[11:02] I blur it and I get the difference between the two.
[11:05] And then there's a blend for noise but I don't think it really does anything.
[11:13] So then I have my bubble attribute here.
[11:18] So just like where there's ambient occlusion.
[11:22] That's where the foam is going to be by the way.
[11:25] Then we do some noise again on top of that.
[11:29] And then do our...
[11:31] Yeah, because I didn't want like here some of the down things to make it more still have the original shape.
[11:41] Then I cleaned it.
[11:43] Scattered it.
[11:45] Scattered some points on it.
[11:47] Okay, so yeah, I recorded this but when I was recording my scatter and density were too high of a resolution.
[11:55] And my Houdini or like my recording was lagging.
[11:59] So this was the value I'm using here but I'm going to reduce both of them a bit.
[12:05] And I also already reduced my scatter.
[12:08] I first had 4 million but now it's 1 million.
[12:13] So this is my scatter.
[12:16] Then in this attribute fob I'm doing the density of the points.
[12:23] So like the max points and then fitting the points found from 1 and this value to 0 and 1.
[12:33] So where it's like more dense we get brighter colors and where it's like less dense.
[12:41] It's darker.
[12:43] So then we can map this to the p-scale.
[12:46] The little color.
[12:48] Do some more curling.
[12:51] Then a VDB from particles.
[12:54] Now you don't almost see anything but if you do a pyro bake we can see the foam.
[13:00] So this is a lower resolution than I originally used.
[13:03] I used 0,0,0,9 but for the recording I lowered it a bit.
[13:09] Then a smooth.
[13:11] Do smooth the mesh a bit like the volume.
[13:16] So yes.
[13:18] And then here I'm just looking if my density is inside the SDF.
[13:24] Then I'm setting the density to 0 so we don't have any foam inside or bubbles.
[13:31] So yeah this is the SDF I'm using.
[13:35] Then here this is the result.
[13:39] It's a lower resolution so maybe more gets deleted now.
[13:43] Then here I just add some very small noise by multiplying it and then multiplying this with the original density.
[13:53] And because we want some specular on our volume we also need the gradient of the volume.
[14:00] This is like similar to the normals.
[14:04] It's like the normals of the volume basically.
[14:07] And then we merge these so we have our density and gradient and to optimize it a bit I resampled my gradient so it's less, it's like a higher voxel size.
[14:20] So and then I cache this and then this was my result with the high resolution.
[14:27] So yeah.
[14:29] Then in the materials.
[14:31] So then the materials are pretty simple.
[14:36] Let's check.
[14:38] I import my camera that I had for the calling.
[14:41] I reference to the SD file of the bubbles.
[14:44] I set here bubbles.
[14:47] Then this is just the volume that's pointing to the cache.
[14:53] And then here yeah the switch is just on this one.
[14:57] Then here is just also reference to the soap bar UC file.
[15:03] The materials also pretty simple.
[15:07] The soap bar is just, yeah no wait.
[15:16] Yes, yeah the soap bar is just some subsurface and stuff.
[15:21] The bubbles, I am doing some stuff with the bubbles.
[15:26] Wait, maybe disable this for.
[15:31] So for the bubbles I'm using a noise as the thin film thickness but normally this has more of the spurly type noise patterns.
[15:44] So what I'm doing is if you visualize it here.
[15:51] Yeah this is a noise pattern I'm using but it's just two noises mixed.
[15:57] And then these noises I'm using as the position for my other noise here.
[16:04] So it gets a bit distorted and then ranging this from the minimum thickness to the max thickness.
[16:13] And also blending it a bit with another noise and 600.
[16:17] So the average is 600 then.
[16:20] Yeah just transmission roughness low.
[16:24] So yes.
[16:26] Okay so yeah this is the volume shader.
[16:30] And it's just like, it's a preset white water material.
[16:36] So here we need our gradient.
[16:38] Then here it's just scattering color density.
[16:41] I remap it to a larger number.
[16:47] I get some reflection color here.
[16:50] Set the roughness to 0.15 and then the stroke to minus 0.4.
[16:57] And if we add everything together then.
[17:03] We can see now it's like a very dark volume.
[17:07] But it's because you don't have enough volume limit when not breathing in the Karma Render setting.
[17:14] So when you preview it here with enough limits we can see it gets white and it's fine.
[17:20] So yeah that's the work through of the setup.
[17:23] Hopefully it was useful and thanks for watching.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_000.jpg
- [0:38] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_001.jpg
- [1:20] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_002.jpg
- [2:33] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_003.jpg
- [2:46] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_004.jpg
- [4:02] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_005.jpg
- [6:35] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_006.jpg
- [7:18] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_007.jpg
- [8:28] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_008.jpg
- [9:44] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_009.jpg
- [12:51] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_010.jpg
- [13:35] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_011.jpg
- [14:20] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_012.jpg
- [15:57] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_013.jpg
- [17:14] tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/frame_014.jpg

---

## Structured Notes

### Core Technique
A full procedural soap-bubble/foam pipeline: bubbles are built as non-overlapping, size-varied scattered spheres (three density tiers) remeshed into a single connected mesh, clipped against a soap-bar volume so they never poke through it, plus a separate finer foam layer built as scattered points converted to a VDB volume and rendered as a Karma volume shader — all driven by a logo-shaped height/mask field rather than a full liquid sim.

### Summary
Starting geometry is a subdivided grid with normals/UVs. A logo image is read into a **Copnet**, its alpha converted to an **SDF** (for a smoother falloff than a hard mask) and blurred to produce a height field, which is baked to the grid via **Attribute from Map**, then used to displace the grid (normalized, re-meshed, color attribute deleted since the SDF conversion also writes one). Ambient occlusion is computed on this displaced mesh purely to get a cleaner bubble-outline mask later.

Bubble placement uses **three deliberately scattered size tiers instead of a dart-throwing/Poisson-disk algorithm**, specifically for more manual control over shape/distribution: a mask (built from `1 - height`, combined with layered noise and the inverted AO) drives a scatter for large bubbles first, then medium, then small, each in its own group with its own remesh frequency (bigger bubbles get denser remesh polycount so final mesh density reads as roughly uniform across bubble sizes). Two bubbles are manually added by hand on top of the scatter for art-directed placement.

**Non-overlap fix (the key trick):** after scattering each tier, a wrangle searches nearby points within a radius, and for each pair sets `pscale` to (distance to the nearest other point) / 2 — this guarantees no two bubble spheres overlap by construction, rather than relying on collision/relaxation. A second pass then explicitly checks, for every nearby point pair, whether the distance is smaller than the sum of the two half-pscales, and masks/deletes the point if so, catching any pairs the pure-nearest-distance rule left overlapping. This two-pass radius/pscale procedure is repeated per size tier (large → medium → small), each building on the previous tier's already-placed points so smaller bubbles fill gaps without overlapping the larger ones already placed. A **Camera Cull** node removes points not visible to camera before the expensive remesh step (with the caveat that reflections can reveal culled/missing bubbles, so cull conservatively). Each tier is visualized as spheres via a **VDB from Particles → Remesh Bubbles**-style step (note: Remesh Bubbles doesn't propagate the `pscale` attribute through, so it must be re-saved as a separate attribute beforehand), then merged into one mesh; some overlap between size tiers is expected/acceptable ("that's how bubbles are") as long as it isn't heavy nesting. A slight bulge + smooth + tiny offset gap is added post-remesh for a nicer bubble read, and any small bubbles too close to the biggest ones get extra subdivision so their faces aren't oversized relative to neighbors.

**Keeping bubbles off the soap bar (the second key trick):** rather than a boolean cut (tried first, far too slow), the soap bar is modeled as an extruded grid and converted to a volume; bubble point positions are displaced by that volume's field, clipped at the zero axis, and then restored back to their original rest position/normal afterward — this produces a clean carved-out contact silhouette where bubbles meet the bar without ever computing a boolean. Bubble geometry is stripped down to only the attributes actually needed (rest position, rest normal) before being promoted/exported for use in Solaris (with per-size-tier naming so e.g. HDRI reflections can later be restricted to only the larger, more visible bubbles).

**Foam layer (separate from the bubble mesh):** ambient occlusion is again used, this time as the seed region for foam, lightly noised to break up the shape, then scattered densely (millions of points, reduced from an original 4M to 1M for a faster preview during recording). Local point density (points found within a search radius, fit 0→1) is mapped to point color, driving a curl-noise-perturbed **VDB from Particles** volume — visually near-invisible until baked through a **Pyro Bake** step, which is what actually reveals the foam structure. The volume is smoothed, then culled to zero density anywhere inside the soap-bar SDF (so foam doesn't render inside solid geometry), a touch of multiplicative noise breaks up flat density regions, and the volume's gradient (its "volume normal" equivalent) is computed and merged alongside density — the gradient volume is deliberately resampled to a coarser voxel size purely as an optimization before final caching.

**Shading:** the soap bar uses a simple subsurface-scattering material. The bubble shader drives **thin-film thickness** from a distorted double-noise pattern (one noise field used as the position input to a second noise, for a swirlier soap-film pattern instead of plain Perlin), remapped between a min/max thickness and blended toward an average around 600 (units implied nm, standard thin-film iridescence range), with low transmission roughness. The foam volume uses Karma's white-water/foam preset volume shader, fed the merged density+gradient volume, with density remapped to a larger range, a set reflection color, roughness ~0.15 and a negative (~-0.4) some "stroke"/anisotropy-like parameter. A late gotcha: the foam volume renders essentially black by default in the Karma viewport preview unless the render setting's volume step/limit is raised — once increased, the foam reads correctly as bright/white.

### Key Steps
1. Build a height/mask field from an arbitrary 2D image (Copnet: alpha → SDF → blur) and bake it onto a subdivided grid via Attribute from Map + displacement.
2. Derive multiple auxiliary masks (inverted height, layered noise, inverted ambient occlusion) to control where each bubble-size tier scatters.
3. Scatter points per size tier (large → medium → small), each building on the previous tier's placed points.
4. Fix overlap with a two-pass radius search: (a) set each point's `pscale` to half the distance to its nearest neighbor, (b) explicitly re-check and delete any pair whose true half-pscale sum still exceeds their distance.
5. Camera-cull points not visible to the render camera before the expensive remesh (watch for reflections revealing gaps).
6. Convert points to spheres and remesh into one connected mesh per tier (save `pscale` separately first — Remesh Bubbles doesn't carry it through); merge tiers, accepting minor inter-tier overlap as natural.
7. Add a slight bulge, smoothing, and tiny offset gap for a better bubble silhouette; extra-subdivide any small bubbles abutting much larger ones so face size stays consistent.
8. Model the contact surface (soap bar) as an extruded/volumed grid; displace bubble positions by that volume, clip at zero, then restore rest position/normal — avoids booleans entirely for keeping bubbles off the bar's surface.
9. Strip bubble geometry to only the needed attributes and promote/export for Solaris use, with tier-based naming for later selective shading (e.g. reflections only on larger bubbles).
10. Build the separate foam layer: seed from ambient occlusion, noise-break the shape, scatter millions of points, map local point density to color, and build a curl-noise VDB from those particles.
11. Bake the VDB through Pyro Bake to reveal actual foam structure (raw VDB from particles looks nearly empty beforehand).
12. Zero out density anywhere inside the soap-bar SDF so foam never renders inside solid geometry; add fine multiplicative noise; compute and merge the volume's gradient (resampled coarser as an optimization) before final caching.
13. Shade bubbles with a thin-film-thickness material driven by double-layered distorted noise (one noise offsetting another) remapped to a thickness range; shade foam with Karma's white-water volume preset fed density+gradient.
14. If a volume shader renders as flat black in Karma's viewport preview, check/raise the render settings' volume step/limit before assuming the shader is broken.

### Houdini Nodes / VEX / Settings
COPs: alpha extraction, `sdftomono`, `blur`. SOPs: `subdivide`, `attribfrommap` (height baking), `attribvop`/wrangle displacement, `normal`, `attribdelete` (strip SDF's extra color attribute), ambient occlusion node, mask construction via noise (`attribnoisefloat`) layering and inversion, `scatter` (per size tier), `attribwrangle` (pscale-from-nearest-distance fix; overlap-pair delete-mask pass), `attribadjustfloat` (pscale bookkeeping), `cameracull`, VDB-from-particles → **Remesh Bubbles** (per-tier frequency control; does not propagate `pscale`), `group` (per-tier), `merge`, bulge/smooth/offset finishing chain, `clip` (soap-bar contact carving, used with volume-based position displacement + rest-position/rest-normal restore instead of a Boolean), `attribpromote`. Foam: dense `scatter` (point-count reduced 4M→1M for preview speed), density-in-radius → fit 0-1 → color, curl noise, `vdbfromparticles`, `vdbsmooth`, Pyro Bake, SDF-based density zeroing, `volumevop`/gradient computation, `volumeresample` (coarser voxel size for the gradient only), file cache. Solaris/Karma: thin-film-thickness bubble shader (double noise, remapped thickness range, low transmission roughness), Karma white-water/foam volume preset (density + gradient inputs, remapped density, reflection color, roughness ~0.15), Karma render-setting volume step/limit (must be raised or volumes preview near-black).

### Difficulty
Advanced — no single hard technique, but a long chain of interacting procedural systems (mask-driven multi-tier scattering, a custom non-overlap algorithm, volume-based Boolean-avoidance, and a from-scratch foam VDB pipeline) that only reads clearly by following the whole video; several steps are presented as "trial and error I found worked" rather than a principled recipe.

### Houdini Version
Not stated on screen; Karma volume rendering + Solaris promotion workflow consistent with a recent H19.5+/20.x release.

### Tags
bubbles, foam, scatter, non-overlap-packing, pscale, vdb, pyro-bake, volume-shading, thin-film, karma, boolean-avoidance, clip, ambient-occlusion, procedural-texturing

---

## Related Tutorials
None yet in this library on procedural bubble/foam packing or thin-film shading — first entry covering this technique.
