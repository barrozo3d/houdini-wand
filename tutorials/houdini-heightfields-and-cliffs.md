---
title: Houdini Heightfields and Cliffs
source: YouTube
url: https://www.youtube.com/watch?v=fF01Lyg_G48
author: cgside
ingested: 2026-07-13
houdini_version: "20"
tags: [heightfield, terrain, procedural, erosion, texturing, materials, environment, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-heightfields-and-cliffs/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini Heightfields and Cliffs

**Source:** [YouTube](https://www.youtube.com/watch?v=fF01Lyg_G48)
**Author:** cgside
**Duration:** 11m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'll share a few tips on how to
[0:05] create terrains in Odini, especially using the new Pegasus tools to colorize the
[0:14] terrain and also how to incorporate some cliffs in your terrain. So let's get
[0:23] started. I'm starting with the Night Fields which is 500 by 700. Then I'm adding
[0:34] a noise and this noise typically looks like this like if it was a desert but in
[0:47] this case I used which is the Worldly Cellular F1. In this case I used the
[0:52] compliment so I can get these shapes and then I can distort it and you will
[1:06] start to get some interesting results. The distortion is just a color with a very
[1:13] high element size and some amplitude. We get something like this. Then I want to
[1:23] incorporate some raw formations. This is similar to a video I shared before but
[1:30] just in case you didn't watch it. I'm basically taking a very distorted shape
[1:39] and projecting it to my battlefield. Then I'm using a mask expand set to
[1:46] height instead of mask and I get the square-doubt shapes and yeah that's
[1:55] basically it. Then I'm incorporating in the terrain with the battlefield layer and
[2:03] in here I'm distorting only the cliff or the raw formations and in here I am blurring the bottom
[2:15] by using again a Night Fields layer with manipulating the masks and then blurring it and I can
[2:24] blur the bottom. So it incorporates better into the terrain. That I'm saving this to mountain
[2:32] layer and in here I'm creating a volume knob to add some custom noise. In this case I'm using
[2:42] a cloud noise and bind exporting it to the mask and I can use a remap and you can see we got
[2:52] we start to get this cloudy look in the terrain which will help in the erosion stage.
[3:00] So in the remap I just increase the output max, compute range and then increase the output max.
[3:08] And I'm clearing the mask and doing a first pass of erosion.
[3:16] And we start to get these valleys but still is not in a resolution. As you can see we only have
[3:26] 2 million vuxels which is low. Then I am again loading the mask with a copy layer by
[3:38] specifying the source as mountain and this nation as a mask. Then I'm blurring the result from
[3:47] the erosion on the mountain, on the raw formations. Then I'm resampling it
[3:56] to a higher resolution as you can see 40 million vuxels.
[4:02] And then I'm just creating a mask of the terrain so I don't erode too much the raw formations
[4:13] and I'm doing a second pass of erosion.
[4:16] And as you can see we start to get way better results with these typical rock shapes
[4:28] with a lot of valleys. And then I want to flatten more these areas and remove these noise that we have
[4:40] and just overall flatten them. So I'm using a mask by feature.
[4:46] We mask last load to get these flat areas and I'm using an i'd field flatten.
[4:56] And we should get these results as you can see. We go from these to these flatten areas.
[5:05] So this is where we catch the results and we have quite interesting terrain and some rock
[5:18] formations. And this is where I will start to use the Pegasus tools. Mainly the i'd field material
[5:28] that you can use to colorize the terrain. In this case I'm creating a mask by i'd just selecting
[5:36] everything and just adding some terrain texture, some base texture. Then in the second one I'm adding
[5:51] some darker value on the occlusion. So I'm just layering the mask and then mask by feature.
[6:00] In this case I'm using occlusion and tending the result as you can see.
[6:10] And we start to get some more interesting results.
[6:13] Then in this one I am masking the more flat areas and adding some grass as you can see.
[6:29] This is pretty simple. You just plug the color and the height if you want to add some height.
[6:35] And then you can play with the distortion so the texture doesn't rip it so obviously.
[6:43] So in this case I am tending a bit the grass mask, the grass texture I mean. And then
[6:56] remapping it or increasing the tinge value. But in here what I'm doing is creating a mask noise
[7:05] on the previous grass mask so I can remove some areas. And then tending it with a gradient.
[7:15] As you can see from green to yellowish white. And then just increasing the value of the tinge.
[7:25] This is a pretty useful node.
[7:27] And you can see we start to get this interesting result.
[7:38] Then in here I am masking more the cliff areas and adding some texture there.
[7:47] And doing again the same in here. Some more details.
[8:01] And I am also increasing the brightness of those cliffs.
[8:07] And now I am creating an occlusion mask I believe.
[8:16] Yes an occlusion mask really tight. And tending the resulting texture.
[8:27] By a gradient you can see if I increase the strengths we get a more
[8:35] occluded look. But in this case I wanted to be subtle.
[8:41] And that's basically it for the terrain.
[8:47] So there's only one thing I wanted to share to finish this video.
[8:53] Which is as you can see the texture of this cliff won't really hold up even for
[9:03] mid-distance. So what we can do is separate the cliff from the terrain. And if you remember
[9:14] we have that attribute in here. We have that point attribute which is the mountain.
[9:21] As you can see we have it here. So we can split the mountain after converting the attribute.
[9:35] And isolate it. And we keep the terrain in here.
[9:43] And then we can merge it over the top.
[9:51] And in this case I am just what remashing the cliff. So we can get some displacement at
[10:02] render time using the new triplaner node in the 20. And I am doing that just by
[10:10] probably reducing in this case in a loop. And then what remashing it we get some nice
[10:22] result, nice quad mesh. And then in the salaries I can target this specific geometry.
[10:32] So as you can see we have the idtl terrain and good topology cliff so that we can
[10:45] displace it at render time. So yeah that's basically what I wanted to share with you today.
[10:53] And I hope you have taken something out of this. Again if you want more details on the
[11:01] idfield material and all the other Pegasus nodes I encourage you to watch that master class or that
[11:11] series of tutorials. It's definitely really interesting and informative. So if you want to
[11:20] grab the file feel free to do it on my Patreon page and I'll see you next time. Thank you.



---

## Captured Frames

- [0:40] tutorials/frames/houdini-heightfields-and-cliffs/frame_000.jpg
- [1:30] tutorials/frames/houdini-heightfields-and-cliffs/frame_001.jpg
- [3:10] tutorials/frames/houdini-heightfields-and-cliffs/frame_002.jpg
- [4:20] tutorials/frames/houdini-heightfields-and-cliffs/frame_003.jpg
- [5:10] tutorials/frames/houdini-heightfields-and-cliffs/frame_004.jpg
- [6:10] tutorials/frames/houdini-heightfields-and-cliffs/frame_005.jpg
- [9:20] tutorials/frames/houdini-heightfields-and-cliffs/frame_006.jpg
- [10:20] tutorials/frames/houdini-heightfields-and-cliffs/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a rocky terrain with embedded cliff/rock formations using layered Heightfield noise/distortion, a **two-pass erosion workflow** (low-res pass first, then mask-preserved resample to high-res for a second, finer erosion pass), the third-party **Pegasus** toolset's Heightfield Material/Tint nodes for procedural terrain texturing/coloring, and a final split-and-quad-remesh step so the cliff geometry holds up under render-time Triplanar displacement.

### Summary
The terrain starts as a 500x700 Heightfield with a **Worley Cellular F1** noise (complemented for a desert-like look), then distorted with a very-high-element-size, high-amplitude Heightfield Distort by Noise for more interesting broad shapes. Rock/cliff formations are added by taking a heavily-distorted separate shape and projecting it onto the base terrain, then using **Mask Expand set to "height"** (instead of plain mask mode) to get squared-off rock-like silhouettes; this is incorporated into the terrain via the "mountain" heightfield layer, with additional distortion restricted to just the cliff area and a blurred-mask blend at the base so the rock formations integrate smoothly into the surrounding terrain rather than looking pasted-on. A **Volume VOP** adds a custom cloud-type noise, bind-exported to the mask channel and Remapped (raising output max) to create a cloud-like density pattern used to drive erosion variation. **First erosion pass** runs at low resolution (~2M voxels) — enough to establish major valley/drainage shapes but too coarse for fine rock detail. The mask from erosion is then re-loaded via **Heightfield Copy Layer** (source: mountain, destination: mask), blurred specifically over the rock formations, and the whole heightfield is **Resampled up to ~40M voxels**; a fresh terrain-limiting mask (so erosion doesn't over-erode the actual rock formations) enables a **second, finer erosion pass** that produces much more convincing rock-valley detail. A **Mask by Feature** (flat-area detection) plus **Heightfield Flatten** then smooths/flattens areas that shouldn't retain erosion noise (e.g. path or building-pad areas), for a cleaner final terrain silhouette. Texturing uses the third-party **Pegasus** Heightfield Material system: a base mask selecting everything gets a base ground texture; a Mask by Feature (occlusion-based) darkens crevices; a flat-area mask adds grass texture (color + optional height blend, with the grass texture's own distortion tuned so it doesn't read as an obviously-repeating tile) — layered further with a **secondary noise mask + gradient Tint** (green-to-yellowish-white) to break up uniform grass coloring, an increased "tinge" value for stronger color variance, cliff-area masks adding rock texture/brightness, and a final **tight occlusion mask + gradient Tint** for subtle ambient-occlusion-like darkening in crevices (kept deliberately subtle rather than a strong occluded look). Finally, since the cliff's baked texture detail visually falls apart even at mid-distance, the terrain is converted to polygons and the previously-saved "mountain" point attribute is used to **split the cliff geometry from the rest of the terrain** (Blast/isolate by that attribute), the isolated cliff mesh is **QuadRemeshed** (reduced/remeshed, apparently inside a loop per-piece) for clean topology, then merged back over the original terrain — giving the cliff a proper quad mesh that can receive real render-time displacement via the new Houdini 20 **Triplanar** node in Solaris, rather than relying on a texture that can't hold up under scrutiny.

### Key Steps
1. **Base terrain noise:** Heightfield (500x700), **Heightfield Noise** (Worley Cellular F1, Complement enabled for a desert-like look).
2. **Broad distortion:** **Heightfield Distort by Noise** with a very high element size and amplitude for more interesting large-scale terrain variation.
3. **Rock formation shape:** take a separately-built, heavily-distorted shape, project it onto the base terrain, then apply **Mask Expand set to "height" mode** (not plain mask) to get squared-off, rock-like silhouettes.
4. **Integrate into the mountain layer:** incorporate the rock shape into the terrain's "mountain" heightfield layer; restrict additional distortion to just the cliff/rock area; blur the base/bottom transition (via another masked, blurred heightfield layer) so the rock integrates smoothly rather than looking pasted on; save the result to the mountain layer.
5. **Cloud-noise mask for erosion variation:** **Volume VOP** adding a custom cloud-type noise, bind-exported to the mask channel, then **Remap** (raise output max, compute range) to shape the cloud-like density pattern used to bias the upcoming erosion.
6. **First (low-res) erosion pass:** clear the mask, run **Heightfield Erode** at the current low resolution (~2M voxels) — establishes major valley/drainage shapes but lacks fine detail.
7. **Preserve mask + resample to high resolution:** **Heightfield Copy Layer** (source: mountain, destination: mask) to reload the mask onto the rock formations, **Blur** the erosion result specifically over those formations, then **Heightfield Resample** up to ~40M voxels for much finer detail capacity.
8. **Second (high-res) erosion pass:** build a mask limiting erosion to the terrain (so the actual rock formations aren't over-eroded), then run a **second Heightfield Erode** pass at the new high resolution — produces convincing valley/rock detail.
9. **Flatten unwanted noise:** **Mask by Feature** (flat-area detection) + **Heightfield Flatten** to smooth/flatten specific areas that shouldn't retain erosion-driven noise.
10. **Pegasus base texture:** using the third-party **Pegasus Heightfield Material** system, create a mask selecting everything and apply a base ground texture.
11. **Occlusion darkening + grass layering:** a Mask by Feature (occlusion-based) darkens crevices; a flat-area mask adds a grass texture/color (with height blend optional), tuning the grass's own distortion so its tiling doesn't read obviously; layer in a secondary noise mask + gradient **Tint** node (green → yellowish-white) with an increased "tinge" strength for natural color variation across the grass.
12. **Cliff texture + tight AO:** mask the cliff areas specifically to add rock texture and increased brightness; finish with a tight occlusion mask + gradient Tint for subtle crevice darkening (kept intentionally understated).
13. **Convert + split cliff from terrain:** convert the finished heightfield to polygons; using the previously-saved "mountain" point attribute, **Blast**/isolate the cliff geometry from the rest of the terrain.
14. **Quad remesh the cliff:** run the isolated cliff mesh through a reduce + **QuadRemesh** pass (mentioned as done per-piece, likely in a loop) to get clean, render-ready quad topology.
15. **Recombine + render-time displacement:** merge the remeshed cliff back over the original terrain; in Solaris, target the cliff geometry specifically with the new Houdini 20 **Triplanar** node to add real render-time displacement, since the baked texture alone wasn't convincing at mid-distance.

### Houdini Nodes / VEX / Settings
Nodes: Heightfield, Heightfield Noise (Worley Cellular F1, Complement), Heightfield Distort by Noise, Heightfield Project, Mask Expand (height mode vs. mask mode), Heightfield Layer (mountain), Blur (masked), Volume VOP (custom cloud noise, bind export to mask), Heightfield Remap (compute range, output max), Heightfield Erode (x2 — low-res then high-res pass), Heightfield Copy Layer (source/destination layer targeting), Heightfield Resample (low → ~40M voxels), Mask by Feature (flat-area and occlusion-based detection), Heightfield Flatten, Heightfield to Polygons, Blast (attribute-based cliff isolation), QuadRemesh. Third-party Pegasus toolset: Heightfield Material, Heightfield Tint (gradient-driven color tinting), various Pegasus mask nodes (by feature, by height, by direction, by constant). Karma X-Style Triplanar (Houdini 20, Solaris render-time displacement).

### Difficulty
Advanced — combines multi-pass heightfield erosion at different resolutions, custom volume-noise masking, and a third-party procedural-texturing toolset (Pegasus); assumes solid heightfield fundamentals.

### Houdini Version
20 (explicitly references "the new Triplaner node in the 20"; Pegasus tools referenced as a separate paid/third-party masterclass series).

### Tags
#heightfield #terrain #procedural #erosion #texturing #materials #environment #advanced

---

## Related Tutorials
Cross-link with environments-in-houdini-part-1---heightfields.md (same author, overlapping heightfield/erosion vocabulary) once indexed together; author references an earlier video covering the rock-formation projection technique in more detail.
