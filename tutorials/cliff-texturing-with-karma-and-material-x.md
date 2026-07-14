---
title: Cliff texturing with karma and material X
source: YouTube
url: https://www.youtube.com/watch?v=WAyk2xCn5rs
author: cgside
ingested: 2026-07-13
houdini_version: "H20+ (Solaris/Karma, MaterialX)"
tags: [materials, karma, triplanar, hda, uv, texturing, heightfields, vdb, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/cliff-texturing-with-karma-and-material-x/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Cliff texturing with karma and material X

**Source:** [YouTube](https://www.youtube.com/watch?v=WAyk2xCn5rs)
**Author:** cgside
**Duration:** 4m3s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. So in this video I'm going to show you how you can quickly
[0:05] texture an asset using procedural techniques. But before we jump into the cliff shading,


### Material X [0:08]
**Transcript (timestamped):**
[0:12] let's have a look at the custom material X note that I will be using in this video.
[0:17] You'll be able to access it through the material X menu, CGS TrackLaner,
[0:23] which is the material X version of previous digital asset I posted.
[0:28] But this one has some advantages when it comes to speed and overall experience.
[0:34] At the top you have the signature. Basically use color for albedo, float for roughness and displacement
[0:42] and vector tree for normal maps. Let's connect the texture. You have the option to pick a different
[0:48] one for you chexes. So this is basically a UV randomizer but within a TrackLaner projection,
[0:56] so you don't need UVs at all. You have a seat for the randomization if you don't like the default
[1:02] look, the tiling amount, the TrackLaner blending of the different projections and the UV blending
[1:10] that controls the sharpness between each repetition of the texture.
[1:15] Here I have this scene with two spheres. The one on the left is using my notes and the one on the right
[1:21] the default TrackLaner projection. I have the different channels mapped, just changing the
[1:28] signature and textures inputs, so they all share the same tiling and randomization settings.


### Comparison [1:39]
**Transcript (timestamped):**
[1:39] As you can see the one using the default material X node is repeating the patterns and doesn't
[1:46] work properly on normal maps and even displacement maps due to the blending between projections.
[1:55] And the CGS TrackLaner is doing a better job at hiding the repetitions and works perfectly
[2:02] with normal maps and other channels. You can grab all the scenes from this video along with the
[2:09] TrackLaner node from my Patreon. Let's get to the clip shading, so I created this example


### Shading [2:12]
**Transcript (timestamped):**
[2:16] cliff with some mightfields and VDB as shown before on the channel. Then I'm creating some custom
[2:23] masks to use in texturing, first convexity mask and then in point-vop a slope mask.
[2:31] Moving into Solaris importing the geo and let's see the shader setup. As you can see I'm using
[2:38] the custom TrackLaner node and this is how it looks with everything combined. So in the first
[2:44] TrackLaner I'm loading a mega-scan texture of a cliff and I am mixing with another rock texture.
[2:52] And as the mixing factor I am using the convexity mask but you can also use the
[2:58] concavity one for a different look. This is how it looks both textures combined.
[3:06] Then I am mixing on top the grass texture using the slope mask.
[3:14] As for the remaining channels I am just using the respective textures,
[3:19] making sure I'll love the TrackLaner node share the same tiling and randomization settings
[3:25] using reference nodes. And this is how it looks with displacement.
[3:32] And finally I added a simple ocean and some other elements and you can see the final result of
[3:38] the texturing. This was a quick setup you can create more masks and experiment with different


### Final result [3:40]
**Transcript (timestamped):**
[3:45] textures to get the desired look, add noises and so on. So yeah hopefully this can help you in your
[3:52] next project and feel free to get all the files plus the custom TrackLaner node from my Patreon.
[3:59] See you in the next one!



---

## Captured Frames

- [0:48] tutorials/frames/cliff-texturing-with-karma-and-material-x/frame_000.jpg
- [1:21] tutorials/frames/cliff-texturing-with-karma-and-material-x/frame_001.jpg
- [1:46] tutorials/frames/cliff-texturing-with-karma-and-material-x/frame_002.jpg
- [2:44] tutorials/frames/cliff-texturing-with-karma-and-material-x/frame_003.jpg
- [3:06] tutorials/frames/cliff-texturing-with-karma-and-material-x/frame_004.jpg
- [3:38] tutorials/frames/cliff-texturing-with-karma-and-material-x/frame_005.jpg

---

## Structured Notes

### Core Technique
Introduces a custom "CGS Triplanar" MaterialX HDA (a faster, UV-free triplanar projection node with built-in tiling randomization) and uses it to shade a heightfield/VDB cliff by mixing a rock texture pair via a convexity mask and blending in grass via a slope mask, all channels sharing tiling/seed settings via reference nodes.

### Summary
Compares a custom MaterialX HDA ("CGS Triplanar," a MaterialX port of the author's earlier VEX-based triplanar tool) against the stock MaterialX triplanar node on two test spheres. The custom node projects textures without requiring UVs, exposing a randomization Seed, Tiling amount, a Triplanar Blending control (blend sharpness between the three projection axes), and a UV Blending control (sharpness between repeated tile instances). The signature accepts Color (albedo), Float (roughness/displacement), and Vector3 (normal maps) inputs. In a side-by-side render, the stock MaterialX triplanar shows obvious repeating tiling and breaks down on normal/displacement channels due to blending artifacts between the three projection directions, while the custom node hides repetition convincingly and handles normal/displacement channels correctly. Applied to a heightfield+VDB cliff (built as shown in earlier videos on the channel) with custom convexity and slope masks (the slope mask built in a Point VOP): a base rock Megascans texture is mixed with a second rock texture using the convexity mask (concavity could be used instead for a different look), then a grass texture is blended on top using the slope mask. All the remaining material channels (roughness, normal, displacement) use matching texture sets, with their triplanar nodes wired via **Reference** nodes so every channel shares identical tiling/seed/randomization settings automatically. Finished with a simple ocean plane and extra set-dressing elements for the final shot.

### Key Steps
1. **Custom triplanar node overview**: the "CGS Triplanar" MaterialX HDA takes inputs for two texture sets (for masked blending) plus a **Signature** parameter (Color/Float/Vector3) that adapts it for albedo, roughness/displacement, or normal-map use respectively.
2. Exposed controls: **Seed** (randomizes the projection look if the default doesn't suit), **Tiling** amount, **Triplanar Blending** (controls blend sharpness between the X/Y/Z projection axes), and **UV Blending** (controls the sharpness of the transition between repeated tile instances) — no UVs required at all, since it's a pure triplanar/world-space projection.
3. **Validate with a side-by-side test**: two spheres, one wired through the custom node, one through the stock MaterialX triplanar, sharing identical texture/tiling/randomization inputs (achieved by just swapping the Signature and texture inputs) for a fair comparison.
4. **Comparison result**: the stock node visibly repeats its tiling pattern and produces broken-looking normal maps and displacement (blending artifacts where the three projection directions meet); the custom node hides the repetition convincingly and renders normal/displacement channels correctly.
5. **Build masks for shading** on the heightfield/VDB cliff geometry (constructed using the channel's earlier heightfield+VDB techniques): a **convexity mask** and, via a **Point VOP**, a **slope mask** (surface-angle-based).
6. **Base rock shading**: bring the geometry into Solaris, wire up the custom triplanar node loading a Megascans cliff rock texture, then mix in a second rock texture using the **convexity mask** as the blend factor (swap to the concavity mask instead for a different distribution of the two textures).
7. **Grass layer**: blend a grass texture on top of the combined rock base using the **slope mask** — steeper areas stay rock, flatter areas pick up grass.
8. **Channel consistency**: for roughness, normal, and displacement, load the matching texture sets into their own triplanar node instances, but drive their tiling/seed/randomization parameters via **Reference** nodes pointing back to the main triplanar setup — guarantees every channel's projection lines up rather than drifting out of sync.
9. **Final scene assembly**: add a simple ocean plane and a few extra set-dressing elements around the cliff for the final presentation shot; the author notes this is a deliberately quick setup and that more masks (additional noise-driven blends, etc.) could be layered in for further variation.

### Houdini Nodes / VEX / Settings
Custom **CGS Triplanar** MaterialX HDA (Signature: Color/Float/Vector3; parameters: Seed, Tiling, Triplanar Blending, UV Blending) vs. stock MaterialX triplanar node (comparison) → heightfield + VDB cliff base geometry → Convexity mask + Point VOP-built **Slope mask** → triplanar-mixed rock textures (convexity-driven blend) → grass layer (slope-driven blend) → matching roughness/normal/displacement triplanar instances wired via **Reference** nodes for shared tiling/seed settings → ocean plane + set dressing.

### Difficulty
Intermediate — using the custom HDA itself is straightforward, but understanding *why* triplanar projection needs careful blending controls (and recognizing the stock node's failure modes on normal/displacement channels) benefits from some shading/lookdev background.

### Houdini Version
Houdini 20+ (Solaris/Karma, MaterialX-based shading network); relies on a custom author-distributed MaterialX HDA (CGS Triplanar), not a stock Houdini node.

### Tags
#materials #karma #triplanar #hda #uv #texturing #heightfields #vdb #intermediate

---

## Related Tutorials
Cross-link with [Cliff Face in Houdini](cliff-face-in-houdini.md) — shares the same cliff-building/procedural-texturing subject matter, with that tutorial covering the geometry construction and a full manual COPS texturing pipeline as an alternative to this video's triplanar-MaterialX shading approach.
