---
title: Procedural Cliff Techniques
source: YouTube
url: https://www.youtube.com/watch?v=YLrE1Zww_uc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-cliff-techniques/
frame_count: 0
frame_status: pending-selection
---

# Procedural Cliff Techniques

**Source:** [YouTube](https://www.youtube.com/watch?v=YLrE1Zww_uc)
**Author:** cgside
**Duration:** 14m22s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-cliff-techniques <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm going to be walking you
[0:05] through how to create something like this cliff procedurally about the
[0:10] modeling and the texturing. So yeah let's get into it. So here's the final


### Modeling [0:16]
**Transcript (timestamped):**
[0:18] result from the geometry. I'm gonna change this to smooth shaded. So as you can
[0:25] see is nothing too overpowered but I wanted to share some techniques with you. So
[0:32] let's get started. I'm starting with a box and copying a few tubes to it with
[0:40] very low subdivisions so like six subdivisions and merging over the top. You can
[0:48] change the scatter see to have a different shape. Then I'm remashing it to a
[0:53] grid like voxelizing the geometry and doing a natural good blur, a peak and a
[1:02] mountain and then Boolean intersecting to create some damage and sound details
[1:08] as you can see. Then I'm sharpening a bit and creating a VDB from polygons and
[1:16] converting it to VDB. So we get this result. Then from here I'm creating some cuts
[1:26] and the way I'm doing that is by copying by placing a line along the cliff.
[1:32] Reassembling it to five segments, jittering a bit the points, blasting the end
[1:42] points since I don't want to cut at the end and copying two points a few grids.
[1:48] In this case I just have an offset the seed from the meta-import node. Then I'm
[1:59] doing a Boolean fracture and you can see by the name attribute. So I'm dividing
[2:07] these into five different parts with some jittering as you can see. Then I'm
[2:14] doing a little bit of an exploded view to pull apart the different shapes. Then
[2:22] everything is happening in this loop. Let's see if I can break it down properly.
[2:27] So we iterate over each named primitive and let's see. First of all I'm
[2:41] creating a circle and using the points and creating the normals along the x-axis.
[2:50] So the out and then I'm scaling to fit to the initial geometry and
[3:01] rate projecting it as you can see in here. So I have the shape around my the
[3:08] different parts of the cliff. Then I'm reassembling it to a low resolution,
[3:13] picking a little bit, deleting the points and creating a sweep as you can see.
[3:20] Then I'm doing a lot subdivision, randomizing the z-scale with an attribute
[3:27] randomized and extruding randomly as you can see with that z-scale attribute in
[3:34] here in the local control. Then I'm subdividing and doing a simple mountain and
[3:41] bullying out from the initial shape. So we get this sort of it and look just
[3:54] to add some more edge damage, let's say. But in this case surface damage I
[4:00] should say. Then I'm creating a connectivity so I can blast away and measure
[4:07] the area and blast away the small parts. Since I'm doing a compiled loop it's
[4:14] better than the delete small parts which is not compilable. Then I'm doing a
[4:23] simple transform, a randomized transform along the x and z. As you can see with
[4:29] a fito one and a random function and I'm randomly transforming in the x and z-axis.
[4:37] So that's it. Then in here I'm doing some mesh sharpening to mash up a bit
[4:48] more the shapes. Then doing a VDB from polygons and we get this. Then doing a
[4:57] volume warp to get some some details and it's pretty simple. I shared many of
[5:05] these setups before but I'm doing in this case a shape shape cellular and
[5:10] doing some distortion with a turbulence noise set to 3D noise and sparse
[5:15] convolution and playing with the frequency so I get this stretched look. Then I'm
[5:22] doing a fit range to affect last shape and multiplying by a small number.
[5:28] Then just adding it to the density. And for the VDB combined as you can see I'm
[5:35] doing a VDB combined in here to get this edge damage let's say it's always the
[5:42] same. I'm creating a VDB from polygons in this case with a bigger resolution.
[5:49] Then doing a convert VDB, doing a blur VDB from polygons again to get more
[5:56] subdivisions. Then doing a mountain, converting it to a VDB and in this case I'm
[6:06] not doing this so I can ignore that and doing a VDB combined as you can see.
[6:12] Then converting to VDB scaling it up a bit and in the end
[6:23] and in the end we get something like this so this is from the volume
[6:29] valve as you can see it's hitting the shape a lot and also doing those
[6:35] bullions with the extrusion to get these planar faces. Maybe it wasn't very
[6:43] successful attempts but anyways I'm deleting the small parts to get
[6:52] rid of this floating geo and you can see I still have a class attribute in
[6:58] here if I want to affect the geometry in different ways. Then I'm calculating the
[7:03] slope. So let me check that attributes as you can see so I can place some
[7:13] trees in there as you saw by the final result. Then I'm measuring the curvature
[7:21] and let's see the concavity and the complexity which I will be using for shading
[7:29] and then just file caching everything. Then giving it finally a name and we can move on to shading.
[7:39] So let's have a look here at the I'm importing the cliff and in the material library
[7:46] I have this rock cliff shader and let me see if I can set up something in here to show you a bit better.


### Shading [7:58]
**Transcript (timestamped):**
[7:58] Let me just get rid of the displacement which will slow us down and we can have a look at the
[8:05] shading setup. So I'm importing I'm using the triplanar node the new carma x-style triplanar
[8:16] for every texture for the roughness the albedo displacement and normal. So you here you can see the
[8:25] initial the initial texture which doesn't look very good. Then I'm doing a color correction.
[8:37] So basically now this is the main color correction sorry.
[8:42] So I'm basically desaturating the texture playing with the gamma and the exposure
[8:52] and I'm using the concavity I believe. So the concavity and I'm mixing between two textures.
[9:05] I mean it's the same texture but I'm mixing between two color correct nodes.
[9:11] This one is more saturated as you can see and it will go along the concave various
[9:20] as you can see in here. Then I'm loading another procedural mask in this case the convexity
[9:33] and again I'm mixing I'm mixing with another color correct.
[9:42] And getting these more exposed areas along the concave areas let's say as you can see.
[9:56] So that's basically then I have the roughness and the normal connected to the same settings of
[10:04] the initial triplanar nodes and I also have some displacement which I didn't use the original
[10:12] displacement of this material. I use another one and I'm just remapping it between minus 0.5 and 0.5
[10:22] and connecting it to the displacements. And that's about it. I can show you the scattering setup
[10:33] maybe. So you still have some time as you can see the displacement is having some effects. I am also
[10:44] introducing some normal mapping just to add some more details since we don't have auto bump in
[10:52] karma expu or karma at all. So now I have also some trees that I made in speed tree a long time ago
[11:04] and I keep using them but since it's just such a small detail I can use those. I didn't have to
[11:15] make new ones. So let me see if this loads and as you can see we have the trees and this is really simple


### Tree Setup [11:26]
**Transcript (timestamped):**
[11:28] in a component geometry I'm importing both the tree and the tree proxy that I did.
[11:38] You can have a look at the file and see how this is all setup but I've shared before this.
[11:44] So I'm basically using the geometry variant index along with the component geometry variants
[11:55] set to number. In this case I have four trees then I'm creating the output nodes and then
[12:00] explore variants as you can see and then I'm using the instancer and giving it some materials
[12:09] and in the instaster it's pretty simple I'm just importing the clips. I'm importing the cliff.
[12:18] I should have done a low polyversion to use for scattering but then unpacking it to polygons
[12:25] deleting some attributes creating a p-scale attribute with an attribute noise in this case a very small scale
[12:35] then I'm doing a attribute remap on the slope because I was getting trees
[12:40] way out of the slope area then I'm doing a scatter on the slope
[12:49] then doing some vax to create the oriented attribute to randomize the rotation along the y-axis
[13:00] and doing a jitter also which is just a natural would randomize between 0 and 1
[13:08] so I can get some color correction on shading and that's what I'm doing in here so if I go to
[13:16] the leaves mat I'm loading that jitter attribute remapping it to a small range clamping it and placing
[13:25] it in the U. I could also use some some gain in here to have some different exposures so different
[13:37] gain but yeah that's basically what I'm doing and you can get this reason my patron because I did
[13:45] them and I can share them so so that's about it I hope you have enjoyed this one a very quick


### Outro [13:49]
**Transcript (timestamped):**
[13:54] overview if you are having trouble recreating this if you want to recreate it then in the first place
[14:04] you can have a look at the file on patreon and you always support my work which is nice
[14:10] and I hope to see you next time let me know your thoughts in the comments it's always nice to see
[14:17] some comments thank you



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
