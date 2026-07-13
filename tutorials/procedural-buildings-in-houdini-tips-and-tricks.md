---
title: Procedural Buildings in Houdini | Tips and Tricks
source: YouTube
url: https://www.youtube.com/watch?v=JCdVrNwiMGk
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-buildings-in-houdini-tips-and-tricks/
frame_count: 0
frame_status: pending-selection
---

# Procedural Buildings in Houdini | Tips and Tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=JCdVrNwiMGk)
**Author:** cgside
**Duration:** 13m57s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-buildings-in-houdini-tips-and-tricks <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So I've been maling this building in Odinne for a few days and
[0:07] part of most parties done procedurally. And in this video I will be sharing a few tips
[0:12] that I learned along the way. So yeah let's get into it.


### Procedural brick dome [0:17]
**Transcript (timestamped):**
[0:17] So let's start with the brickify setup of the dome. So I believe it's in here. I start
[0:23] with the base, which is just a sweep node with 8 divisions and with the profile adjusted.
[0:32] Then I'm scattering quite a few points because I need to do these width points so I can easily
[0:38] do over an eye fracture and create the bricks or the divisions. So I'm scattering quite
[0:45] a few points. Then I'm dividing that into layers so I can come in here, change the amount
[0:51] of layers. So the way I'm doing that is by defining the amount of layers first, then get
[0:57] the bounding box min and the bounding box max. From that I can also get the ith. That's
[1:04] I can divide by the amount of layers and for that I get the layer ith. So the section
[1:10] in here, the gap. Then I'm also calculating, I'm also creating a layer attribute so I can
[1:17] have 0, 1, 2, 3 and so on. And from that I can just manipulate or modulate the position
[1:23] dot y. So the y position of the points. And I started the bounding box min, then add
[1:29] the layer, so 0, 1, 2 and so on and scale it by the layer, so that we calculated in here.
[1:35] And then we get the sort of look, we get these sections and it will always snap to the
[1:42] bounding box max. Then I'm fusing the points, but then right now they are two, two uniform,
[1:52] so like they are relaxed and I want them randomized along the y position. So I want them offset
[2:01] it from each other, so it creates that typical look. In here I'm just snapping these to the
[2:08] surface, so we do so to make sure they are on the surface. So in order to have that random
[2:16] offset in here, I am sorting the points along in a circular way. This is not the typical sort,
[2:24] this is the lab's sort, so not the default one. That has this option to do circular sorting.
[2:31] And I'm sorting them, adding and converting to line. So I can sample the u position, the
[2:40] intrinsic uv's of these curves. And that's what I'm doing here, first using the xyz list,
[2:47] first to find the prim and the uv coordinates. And then I'm creating a random layer, a random
[2:56] float value with the layer as a seed. For the position, I'm taking the u components of the
[3:06] intrinsic uv's from these curves, adding an offset and the random offset that I created in here.
[3:14] Then just make sure to module it to one so we can easily wrap around the points.
[3:20] And then just updating the position with the prim uv and sampling that u position of the
[3:28] intrinsic uv's. I hope that makes sense. It is quite an headache to wrap our heads around.
[3:36] So yeah, that's basically how I did the fracturing, how I did the brickify setup in here,
[3:44] I'm just dividing these into layers. And then in here is where I'm doing the different bricks.
[3:51] As you can see, if we didn't upset them, well, they still look okay, but I wanted a more randomized
[3:57] look and to control the seed. So I did this in here. And we need to do these in stages. So
[4:08] taking each layer and veranoi fracturing, otherwise we will get some unpredictable results.
[4:14] So yeah, that's how I'm doing the brickify setup.


### Custom shape generation [4:18]
**Transcript (timestamped):**
[4:18] So now I wanted to share how I created this shape in here, which can be a bit challenging.
[4:23] I tried with the bridge tool, but it didn't give me the control I wanted, so I ended up with
[4:30] custom solution, let's say. So I have the base model and I'm extracting the
[4:36] distriangle in here just by clipping it. And then I match size it to the position I want to start
[4:48] the copying of the layers. Since I'm going to copy, scale them progressively and then use a skin.
[4:57] So I have the base shape, which is this triangle, then creating a point on the back of that shape,
[5:05] so I can easily create a bunch of points here and copy the triangles.
[5:10] For that, I'm just manipulating the bounding box mean and the bounding box size, so I add the point
[5:16] at the back of the model. Then using punch and rate, I generate 32 points, you can generate more or
[5:23] less depending on the resolution you want in your model. And in here is where everything is
[5:28] happening, as you can see, if I show you the original position of that triangle,
[5:37] I can come in here and change the amount of points and it will always adjust to that position
[5:42] and distribute them equally. So I first take the bounding box max of the original position,
[5:48] so input one in here, then the base pose will always be at zero. And I calculate the height,
[5:56] so I get the height. Then it's pretty simple, I just manipulate the y position by adding
[6:02] the current point number, so zero, one, two, and so on and divide it by the amount of points,
[6:08] so that way I get the normalized value. And then I just multiply it by the right, so I get,
[6:17] this is not doing anything in here, forget about that. So I can come in here, change the amount
[6:23] of points as I told you and it will always adjust. So hopefully that was clear. Then in here,
[6:28] I'm copying two points, as you can see, since I generated these points to use a copy to point
[6:34] setup. And I'm also manipulating, so this by default will look something like this, and then I'm
[6:40] manipulating the p-scale and the way I'm doing that with with an attributed just float, set to
[6:44] bounding box along y. And then in here I can change the profile of that p-scale, so I can
[6:53] come in here and change anyway, I want it. In this case I wanted this flight look and then this
[7:01] all off in here. So then I'm just scanning the shape, so since we have these layers, we can just
[7:10] scan and we get also polyfilling and we get something like this. So yeah, that's basically how I've
[7:16] done it. Hopefully this was useful to you. So as you can see by this shape, I wanted to define
[7:25] quite well the sharp corners in here to have this polygonal look. And I wanted to find these


### Beveling techniques [7:30]
**Transcript (timestamped):**
[7:32] vertical edges and this is a known technique that I'm going to show you, but that might,
[7:41] some of you might not know, so I'm gonna share it anyways. So I'm starting with a curve,
[7:46] to define the profile, then revolve it. Then in here, I'm selecting in vertex mode one out of two
[7:54] and then just promoting two edges as you can see. And with this group range, I can offset between the
[8:01] horizontal, let's say, horizontal edges and the vertical ones. So just by using vertex. And this
[8:09] is quite a useful technique that some of you might not know, so I'm sharing it.
[8:15] Anyways, so yeah, that's basically how I've beveled those edges individually and the same goes for
[8:23] the other part, as you can see. Then I'm also adding a bevel to the sharp edges to get some light,
[8:30] but that's with another polybevel as you can see. So yeah. So I have this particular model in here


### Connecting shapes [8:35]
**Transcript (timestamped):**
[8:37] that I need to divide into sections because it was easier to do to have this rounded look in
[8:42] here and this polygon-like look in here on the bottom. So one problem was the connection between the
[8:51] shape. So I started with this polygonal look. Then I have this rounded look in here and they
[8:59] would look disconnected. So besides, I'm dividing it, it wouldn't really work that well because I have
[9:06] this bevel to define the polygonal look. So I need somehow to round it with a fall off. So in the
[9:14] end, we get something like this, as you can see. So it still has that polygon look and the bevel
[9:23] edge, but it falls off to connect with the original shape. And so we have this already sorted out.
[9:33] We have manipulated this shape and we have to round it look and we start with this polygonal
[9:38] connection in here. Then I'm feeding that into feedback loop. And the first step I do is to,
[9:48] let me reset this, is to select the unshared points and create boundary groups. So this way,
[9:58] I have a group for the top boundary and one for the bottom. I'm only interested in the top. So I'm
[10:03] promoting the first one to edges so I can easily convert it to a line. So we get something like this.
[10:11] Then I'm resampling quite a bit to have enough resolution. Then I'm also extracting the
[10:20] these edge in here, converting it to curve. So the rounded one and I'm re-projecting it. So I'm
[10:27] taking the polygonal one and re-projecting it to the rounded one. Then using a lattice in
[10:36] points modes, then input I take the original shape. And as the, which input is it, the rest geometry,
[10:46] I take also the original edge. And as the third input, the foreign geometry, I'm taking the rounded
[10:54] circle. And then if we have a look at the result, let me just select this. We start to get that
[11:04] edge deforming to a rounded loop. And if we do that for a few iterations, with a sub-dividing
[11:10] between, we get the rounded loop. So if I go back one to three and we get the correct result.
[11:20] This sub-divided is just here if the iteration is bigger than zero. So in the first iteration,
[11:29] I don't want to subdivide. So yeah, that's basically how I connected those two shapes. So nothing
[11:36] too crazy, but it's always some nice trick to know. So as a last tip, I wanted to show you how I


### Detailing and conclusion [11:43]
**Transcript (timestamped):**
[11:45] did this paneling in here on the art edges. Basically by having these overlap look, so as they
[11:55] connect. So let me go in here. I'm using a shame sub to copy some geometry, which is just this
[12:05] paneling in here, as you can see. And I'm copying that to the edges of the geometry, the art edges,
[12:12] and then using a shame. And I'm also, so if I disable in here this rigid mask, we get this sort of
[12:21] look. But I'm creating instead a rigid mask, which is just manipulation of the bounding box
[12:34] of this geometry. So I'm taking the bounding box Z, since this is oriented towards the Z.
[12:40] And then I'm mirroring that with this expression in here. And finally, I'm manipulating that with
[12:48] ramp. As you can see, that looks something like this. So it goes above and below or above and below
[12:54] in here. And I'm saving that as a mask, which went fed into this shame sub, if I can show you.
[13:06] So in here, it will go below. And on this part, it will go above. So I can come in here and manipulate
[13:16] this as you can see. And we get that typical look. So yeah, nothing too crazy, but hopefully that was
[13:23] useful. So yeah, guys, this is basically it. I hope you have enjoyed this video.
[13:29] You can grab some sample files with everything and the code that I showed in this video on my Patreon,
[13:38] alongside with exclusive tutorials and all the project files from my videos.
[13:44] Also, if you want me to cover something specific about this project that I am doing,
[13:49] I can do another video. So let me know in the comments. And yeah, that's basically it.
[13:53] Thank you for watching and I'll see you next time.



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
