---
title: How to (not) bake brownies in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=R3ClxIiqxag
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-not-bake-brownies-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# How to (not) bake brownies in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=R3ClxIiqxag)
**Author:** cgside
**Duration:** 11m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-not-bake-brownies-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'm gonna be breaking down how I did this
[0:05] chocolate brownie in Odini.
[0:08] This is not by any means the way you should do it, but it's the oddini way I guess, and
[0:14] hopefully you'll get away with a few new techniques.
[0:17] So let's get started.
[0:18] So here's the final product, we'll start from the top, just from a box, which is the initial
[0:27] point, and then I'm grouping by normals, the primitives along the X, the positive X,
[0:36] then promoting it to edges and subtracting the smaller edges by using max edge length in
[0:44] a group note, then beveling that part, adding some normals, and grouping also the outside
[0:51] frames that will be our layering on the top, and I'm doing that by using the max edge
[0:58] length on the primitives.
[1:01] Then let's go to the layering part, the cracking part, I'm blasting away those primitives,
[1:08] then what we're mashing it since I want a uniform distribution, subdividing quite a
[1:13] bit, see some going to be dividing this geometry into smaller chunks into some clusters,
[1:23] let's say, then if I disable this mountain and look at this attribute ringle linear, I'm
[1:30] just scattering some points on the surface, and then using the near point, I can create
[1:35] a cluster attribute by randomizing the near point, as you can see.
[1:40] I define through this mountain and then apply the rest, after saving a rest state, we can
[1:46] have these displaced chunks, which is my final vote, so without the mountain it will look
[1:54] like a Varanoi fracture, but with the mountain we get these organic look.
[2:01] Then what am I doing here?
[2:02] I'm grouping some parts that I want to subdivid again, so break it down into smaller chunks
[2:10] by using these randomization in here, and I can change the length, then doing the same
[2:20] again, the same clustering algorithm, let's say, but this time I scatter a few more points,
[2:32] and I'm only creating the cluster attribute where the density, so this attribute we just
[2:36] looked is bigger than point nine.
[2:38] So in this case we are just dividing the bigger chunks into smaller ones, but not everywhere,
[2:44] just in some places.
[2:47] Then in here I'm converting these to a cluster integer attribute by using random flash,
[2:54] random f-ash, I don't know how to pronounce it, and this will give you random numbers and
[3:01] some add or even negatives, so I'm just enumerating them, as you can see in here, to have them
[3:07] in order, which can be handy.
[3:11] Promoting these to the cluster attribute to a primitive one and vertex splitting, so I
[3:16] can now the pieces isolated into individual elements, and in here we can ignore these, and
[3:24] I'm promoting to primitive because this vertex split expects primitive attribute or a vertex
[3:31] attribute, so that's why.
[3:34] Going back to point and doing an edge smooth, this is a bit slow, but it will help us
[3:39] have some nicer contours, and in here I'm displacing along the normals randomly based
[3:50] on the cluster attribute, as you can see, we could always introduce a seed if you want
[3:55] to play with the look.
[3:59] And then in here I'm deleting some random pieces, because I don't want to have it completely
[4:07] filled, so I'm just deleting some random pieces and you can change the seed.
[4:12] Then I want to displace these outer edges, I want to move them a bit out, so for that
[4:19] I'm grouping the unchained points, and then creating a surface distance attribute, so
[4:27] by using the surface distance function, as you can see in here, by feeding the unchained
[4:33] points.
[4:34] Then I'm normalizing the attribute and also playing with the fall off, so I have them
[4:42] just along the edges, and just attribute blurring as you can see.
[4:48] Then introducing some noise, so I can mix both, let me show you, so I can mix both in
[4:56] the displacements, as you can see some parts are displaced, some others are not so displaced.
[5:04] And the way I'm doing that is just by displacing along the normal, multiplying the surface
[5:08] distance we created, and a bit of the noise, and you can introduce more or less, as you
[5:14] can see.
[5:16] And we get this look.
[5:22] So now I want to do some transformations to the individual pieces, and in order to do
[5:27] that I need to have a center point to transform from.
[5:32] We could use extra centroid, but some of these pieces will have the centroid of the mesh,
[5:38] so that can be an issue.
[5:40] We could probably, we could probably extract the centroid on the cluster attribute and
[5:46] write project it to the mesh, but in this case I didn't think of that, so I did it in a
[5:51] slightly different way.
[5:53] Let's see, so I'm just UV flattening and creating these UV islands.
[5:59] Then promoting the cluster attribute to a prime, and moving the geometry, moving the UVs
[6:08] to 3D space, and extracting the centroid there on the cluster prime.
[6:14] And just UV sample to the original position, as you can see.
[6:20] And from here we can also sample the normals, because we will need them to constrain the
[6:26] geometry to the inner part, because we will displace it.
[6:31] So and we get back to these where we have the spaces, and now we can rotate them randomly
[6:39] by using a Q-rotate, and taking advantage of that normal to rotate around.
[6:46] So as you can see I'm rotating randomly, 8 degrees negative or positive along the normal,
[6:54] which is the normal we extracted in here.
[6:57] So these look something like this.
[7:00] Show you the eye frame.
[7:02] So just rotating them, just adding some chaos to the geometry.
[7:09] In here I need to show you how I did this.
[7:12] So we started with this geometry, which is just the interior part, the cake part.
[7:18] Then do some basic VDV operations to have this cake look.
[7:24] And I'm just converting it to VDV, and using 3 noises, so a basic one to remove some of
[7:34] the parts, to break a bit the cake.
[7:38] And then mixing two alligator noises with another turbulent noise.
[7:44] And one is just as a smaller scale than the other one, and we get this mixed look between
[7:49] an eye frequency and low frequency noise.
[7:53] So nothing special in there.
[7:55] And then I'm creating a proxy, let's say, so I can easily do some operations.
[8:04] And from those points that we extracted, those centroids, I'm re-projecting them to
[8:11] this proxy geometry.
[8:13] Otherwise the cracking parts or the layering parts will not be on the surface, it will
[8:19] be offset.
[8:22] So for that I'm running this wrangle in here to constrain the geometry to the surface,
[8:28] as you can see, otherwise it will look something like this.
[8:35] So as you can see, it's a bit of the surface and all flat.
[8:39] And when I run this, it will be constrained to the surface and a bit randomized.
[8:44] And the way I'm doing that is by using the diagonal function, by gathering the normals
[8:51] from the initial surface.
[8:54] And the blurred normals of my proxy geometry, and then I'm just transforming from one normal
[9:01] to another one, as you can see.
[9:04] And also subtracting the center position and adding it after the fact, or in this case
[9:11] adding the point position.
[9:14] So then I'm sickening and doing some basic BDB operations in here.
[9:20] And we end up with this.
[9:22] And the BDB operations are really simple, just very eye-frequency noise and playing
[9:28] with the fit function to have just these small cracks, as you can see.
[9:34] So now we also have this feeling and I shared how I did a similar one in my last short,
[9:44] if you haven't watched your Canon Evalog.
[9:47] But basically I am starting with the proxy geometry, clipping in the middle and blasting
[9:55] away the field polygons, because I'm feeling in here in the clip.
[10:01] Ticking the geometry, creating a point from volume and a viscosity attribute, as you can
[10:05] see.
[10:06] So we will have a bearing viscosity.
[10:10] So we can have longer streaks and smaller ones than just doing a basic collision source.
[10:18] And in this flip solver, I'm loading in the flip project, creating a pop source on
[10:27] all the points, and also loading in the collision geometry.
[10:33] And for the flip solver, I'm just enabling viscosity and viscosity attribute and some surface
[10:38] tension.
[10:39] Nothing too complicated, and just part of fluid's time shift frame and mesh the surface
[10:46] and mesh the points and we get something like this.
[10:50] Then is just a matter of transforming it a bit in to fit a bit better the initial shape
[10:56] we have.
[10:58] So yeah, a lot of work, but in the end it looks somewhat decent I guess.
[11:05] This file will be available on Patreon if you want a look.
[11:11] And I hope you have learned something new.
[11:14] Thank you for watching and I'll see you next time.



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
