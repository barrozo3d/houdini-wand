---
title: Environment Technical tips and tricks
source: YouTube
url: https://www.youtube.com/watch?v=bqyaPvWT5Gc
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [solaris, lops, vex, procedural, scattering, instancing, cops, compositing, karma, environment, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/environment-technical-tips-and-tricks/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Environment Technical tips and tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=bqyaPvWT5Gc)
**Author:** cgside
**Duration:** 3m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this video I'll share a few technical tips for the environment creation.
[0:05] You can download the full scene on Patreon.
[0:08] So let's start simple on how to create a proxy for your trees.
[0:12] I am importing the tree, unpacking and scatter some points on it.
[0:17] Then you can just use the particle fluid surface to create a simplified mesh to use as proxy
[0:22] in salaries.
[0:25] Now let's see how to make simple rocks lay flat on the ground.
[0:29] So we measure the area of all the primes and in a loop create some primitive normals.
[0:35] Getting the largest prime of the rock to lay flat and in this wrangle grouping it by comparing
[0:41] the largest with the original area.
[0:44] In this one we make all the necessary transforms.
[0:48] First getting the largest prime number and it's normal, then using the diadural we transform
[0:55] from the original normal to the new position.
[0:59] Get the centroid of the base prime and finally subtract the centroid position and orient it
[1:05] with the matrix.
[1:07] The original logic was suggested by Swalsh on the CG wiki discord by the way.
[1:13] And we now have the rocks laying flat on the ground ready to be scattered.
[1:19] So now having the rocks, let's see how to make them work with the insta-serene salaries.
[1:24] So with the component geometry typical setup we object merge all the rocks and we blast
[1:31] using the name attribute along with the geo-variant index.
[1:36] And that works because of the component geometry variance set to a number with the correct
[1:42] amount of rocks.
[1:44] Create an output and an explorer variance and finally we feed it to the insta-serene
[1:49] primitive pattern.
[1:51] Now it's grabbing all the different rocks randomly and without having to split them in
[1:55] subs.
[1:56] Ok, let's see how to create camera for us to calling with salaries.
[2:01] This is based on a setup by NPT on the side effects forums.
[2:07] So inside the insta-ser the first thing you need is an object network and you import the
[2:13] camera with a lot of import camera nodes.
[2:16] Make sure to select it from the stage.
[2:19] After scattering the points you will need these wax snippets that are similar to many
[2:24] first time calling approaches using NDC and it's nice that you have some padding to.
[2:31] Now since this is a very basic scene and rendering fog takes a long time, let's see how to
[2:37] make some quick fog with hops.
[2:40] In salaries I am rendering two different streams, one for all the geometry and one for the background.
[2:48] If you want to render both just select all the render ropes and press render to disk.
[2:53] To avoid color space issues make sure to also render to ACCG.
[2:59] Then you can create a co-pnetwork loading the files and over them since we have the alpha
[3:05] channel.
[3:08] I also render a depth pass that I am normalizing and giving it some contrast to remove the
[3:15] foreground.
[3:18] Adding just a flat white color to the background so it adds fog there too and merge it over.
[3:25] And now we can use that as a mask for a simple offset by adding some value to the final image.
[3:32] You can control the fog of NDC too.
[3:35] So that's all for now, hopefully you learned something new and don't forget you can grab
[3:40] the full scene on Patreon, a lot of useful little setups in there.
[3:45] Thank you and see you soon.



---

## Captured Frames

- [0:10] tutorials/frames/environment-technical-tips-and-tricks/frame_000.jpg
- [0:35] tutorials/frames/environment-technical-tips-and-tricks/frame_001.jpg
- [1:20] tutorials/frames/environment-technical-tips-and-tricks/frame_002.jpg
- [2:10] tutorials/frames/environment-technical-tips-and-tricks/frame_003.jpg
- [2:40] tutorials/frames/environment-technical-tips-and-tricks/frame_004.jpg
- [3:20] tutorials/frames/environment-technical-tips-and-tricks/frame_005.jpg

---

## Structured Notes

### Core Technique
Five compact production tips for large-scale environment work: fast tree proxy generation via Particle Fluid Surface, VEX-driven "lay flat on ground" orientation for scattered rocks, variant-based rock instancing in Solaris without manual subnet splitting, a frustum-based camera-culling VEX snippet for Instancer, and cheap depth-based fog composited in COPs instead of a full volumetric render.

### Summary
For tree LOD/collision proxies: unpack the tree, scatter points across it, and run **Particle Fluid Surface** on those points to generate a simplified blob mesh usable as a Solaris viewport/bound proxy — much faster than manually retopologizing. For making scattered rocks lay flat: measure each primitive's area, loop to compute primitive normals, identify the largest-area primitive as the "base" that should touch the ground, group it by comparing against the original total area, then in a wrangle use a **dihedral** transform to rotate from the rock's original normal to the target (down) direction, get the base primitive's centroid, and subtract/orient using a matrix so the rock settles flat — a technique originated by "Swalsh" on the CGWiki Discord. For efficient rock variety in Solaris: build the usual Component Geometry setup, Object Merge all rock variants together, Blast using a combination of the `name` attribute and `@geo_variant_index`, set Component Geometry Variants to "number" mode with the correct count, and feed the result straight into the Instancer's primitive pattern — this grabs different rocks randomly per instance without needing to manually split rocks into separate subnetworks. For camera culling: inside the Instancer, build an Object Network importing the actual Solaris stage camera via **Import Camera**, then after scattering points run a wrangle (based on an "NPT" setup shared on the SideFX forums) computing each point's **NDC (normalized device coordinates)** position relative to that camera, applying some padding margin, to cull/skip instances outside the camera frustum — a first-pass camera-culling approach. For fast fog without expensive volumetric rendering: split the Solaris render into two Render ROPs (main geometry + background), render both to disk in **ACEScg** color space to avoid color mismatches, then in COPs load both passes (compositing over each other using the alpha channel), load a separate depth AOV, normalize and contrast it to isolate/remove the foreground, layer a flat white color behind using that mask so distant background also fogs, and finally use the resulting mask as a simple additive offset on the final composited image to fake atmospheric fog — with NDC-based controls also usable to control fog falloff.

### Key Steps
1. **Tree proxy:** Unpack the tree geometry, Scatter points across it, run **Particle Fluid Surface** on those points to generate a simplified blob/metaball-like mesh, and use that as the lightweight Solaris viewport/collision proxy instead of the full tree.
2. **Rock lay-flat orientation:** Measure the area of all primitives; in a loop, compute primitive normals; identify the primitive with the largest area (the intended "ground contact" face) via a wrangle comparing each primitive's area to the total/original area, grouping the winner.
3. **Rock lay-flat transform:** in a wrangle, use **dihedral** to build a rotation from the rock's current base-primitive normal to the desired down-facing orientation; extract that base primitive's centroid; subtract the centroid position (to pivot correctly) and apply the orientation via a matrix — resulting in the rock naturally resting flat, ready for scattering.
4. **Rock variant instancing without subnets:** standard Component Geometry setup; Object Merge all rock variant geometry together in one stream; **Blast** using a combined check of the `name` attribute and `@geo_variant_index` (so each variant's geometry only shows for its matching index); set **Component Geometry Variants** to "number" mode with the exact rock count; create an Output + **Explore Variants**; feed directly into the Instancer's primitive-pattern input — produces fully random per-instance rock variety without manual subnetwork splitting per rock.
5. **Camera frustum culling:** inside the Instancer's network, add an **Object Network** and import the actual render camera from the stage via **Import Camera**; after the point Scatter, run a VEX wrangle (credited to an "NPT" SideFX-forum setup) that computes each point's position in **NDC space** relative to that camera and applies a padding margin, to determine which instances fall outside the visible frustum (for culling/skip logic) — described as a first-pass ("many first time") camera-culling approach.
6. **Two-stream fog render:** in Solaris, set up two separate **Render ROPs** — one for all real geometry, one for just the background — and render both to disk simultaneously (select both ROPs, press Render to Disk); render in **ACEScg** color space specifically to avoid color-space mismatches between passes.
7. **Fog compositing in COPs:** build a CopNet loading both rendered image sequences, compositing one **Over** the other using the alpha channel; separately load a rendered **depth AOV**, normalize it and boost contrast to isolate/remove foreground objects from the fog mask; add a flat white color layered behind (via the same mask) so even the far background receives fog; merge everything together, then use the resulting depth-based mask as a simple additive value offset on the final image to fake atmospheric fog cheaply — noting the same NDC-based technique from the camera-culling tip can also be used to control fog falloff/distance.

### Houdini Nodes / VEX / Settings
SOPs: Unpack, Scatter, Particle Fluid Surface, Measure (Area), For loop (primitive normals), Attribute Wrangle (VEX: largest-primitive grouping by area comparison, `dihedral()`-based rotation from source to target normal, centroid extraction/subtraction, matrix-based orientation). LOPs: Component Geometry, Object Merge, Blast (`name` + `@geo_variant_index` combined condition), Component Geometry Variants (number mode), Explore Variants, Point Instancer (primitive pattern input), Object Network + Import Camera (inside Instancer), Attribute Wrangle (VEX: NDC-space computation relative to imported camera, padding margin for frustum culling), Render ROP (x2 — geometry + background streams), ACEScg color space. COPs: image load (two render passes), Over (alpha compositing), depth AOV import, Normalize, Contrast, flat-color layer, Merge, additive mask-based fog offset.

### Difficulty
Intermediate/Advanced — each tip is short but assumes comfort with VEX (dihedral rotations, NDC math), Solaris variant/instancing concepts, and basic COPs compositing.

### Houdini Version
20.5 (Karma Physical Sky node and Solaris UI visible match Houdini 20.5-era workflow).

### Tags
#solaris #lops #vex #procedural #scattering #instancing #cops #compositing #karma #environment #tips #intermediate

---

## Related Tutorials
Cross-link with environment-creation-with-solaris-in-houdini.md and environment-creation-with-houdini---part-1.md (same author, same environment-production domain — shares Component Geometry Variants and Instancer vocabulary) once both are in the index.
