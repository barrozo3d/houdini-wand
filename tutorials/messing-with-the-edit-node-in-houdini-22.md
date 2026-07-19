---
title: Messing with the Edit node in Houdini 22
source: YouTube
url: https://www.youtube.com/watch?v=Wkj1DMn-X2w
author: cgside
ingested: 2026-07-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/messing-with-the-edit-node-in-houdini-22/
frame_count: 0
frame_status: pending-selection
---

# Messing with the Edit node in Houdini 22

**Source:** [YouTube](https://www.youtube.com/watch?v=Wkj1DMn-X2w)
**Author:** cgside
**Duration:** 12m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py messing-with-the-edit-node-in-houdini-22 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So while I was working on this scene, Houdini 22 was released,
[0:06] so I had to try to implement something into my workflow for this current scene,
[0:12] and I ended up using a lot the edit nodes, and found a few problems with it that I was able to solve
[0:18] by investigating a bit, and that's what I'm going to share in this video. Hope you enjoy!
[0:24] So before we jump into the final scene, I wanted to give you a simple example.
[0:27] So in LOPs, I have in here a subcreate where I create this mesh, where I start with a box,
[0:33] and create an extrusion in here, then just set a simple name and some normals.
[0:39] From there, I just graphed in here a sphere to my scene, so we end up with this render mesh,
[0:44] and with this sphere, a component, and the elite mesh. What I'm going to do now is to create the
[0:50] edit nodes and show you an issue where we'll add. So I'm going to make sure I just translate this up
[0:56] so I can collide it later, and I'm going to select both and add physics,
[1:00] physics mode, and draw a sim geometry. And as you can see, we can see from the green geometry,
[1:05] the sim geometry, that we will have an issue. This sphere is fine because this creates by
[1:09] default convex hulls, and there's no way as far as I can tell to change that,
[1:15] so this is for performance reasons probably. And when I drag the sphere in the physics mode,
[1:21] as you can see, this will ramp up and will not collide with the simple wall we have in here.
[1:26] So I had the same issue in my CD scene that I showed you in the intro, and I'm gonna
[1:32] show you now how you can solve this. Basically, you need to create a proxy mesh,
[1:36] and let's dive again into the subcreate. And after the polyuxrude, I'm doing a convex decomposition
[1:43] with the following set, basically just reducing the max concatity. And we get two different pieces,
[1:48] and I can show you that when I do an exploded view. Then from there, I just delete the name
[1:53] attribute, I don't want two different meshes for the proxy. And then just set the name,
[1:57] I'm calling it proxy mesh. And I'm gonna merge it in, now we will have one on top of each other.
[2:03] Then I can configure primitive, set the render geometry to the render purpose,
[2:08] and set the proxy geometry to the proxy purpose. And now I can iterate over render and proxy,
[2:14] as you can see. So let's leave it at final mesh, and we graph the sphere. And let's just for good
[2:20] measure drop another edit node. And now let's do the following. Let's select these and these,
[2:28] and add physics. Nope, let's just grab these and move it up.
[2:35] Oops. And now we added a physics, so physics mode and draw some geometry. And as you can see,
[2:40] now we have the proper collision mesh. And we can drag it against the wall, as you can see.
[2:45] So this is the core idea of creating custom collision meshes for the edit node in Lops.
[2:53] So I'm gonna walk you through how I created a decent collision mesh for my CDs.
[2:59] So let's actually have a look at the final setup. So as you can see, I start by dragging the different
[3:09] variations I have. So I import the assets and the variants, I set the different variants.
[3:16] From there, this geometry will be too small. So I did it not to scale, but similar enough. But it
[3:23] will be too small. So I'm scaling it up quite a bit. And then I will scale it down to the original
[3:29] size. And in the edit node, as you can see, if we created convex cells, the limit, the collision
[3:35] mesh of these open CD will be in here. And I wouldn't be able to drag the CD, as you can see,
[3:40] to these to these edges here. So that's why I did some custom collision mesh. So if I enable physics
[3:49] mode, as you can see, my collision mesh is properly set, even for rounded shapes, as you can see.
[3:56] And now I'm going to show you how I did it. So here's my initial mesh. So we have the CD and the
[4:02] case open. And now let's start simple. So in here, I just split the case and the CD. For the CD,
[4:09] simple, I just use a convex decomposition or convex cell, and it will work fine. But as you
[4:15] can see, we lost the hole. And in case we want to do the holes, we need to work in a different way.
[4:22] So in the end, I didn't use this mesh because this was just adding too much pieces. But that's
[4:27] definitely a way to do it for RBD and whatnot. And in LOP, edit node is probably using RBD
[4:32] in the background. So just for good measure, I'm going to show you how I did it. So let's say we
[4:37] start with a small piece. I'm going to need some subdivisions. So I'm going to subdivide. And then
[4:42] I just create a density at your goods that will add more scatter points here on the edges. And then
[4:48] I just gather based on density, not too many pieces and do over an eye fracture that will look
[4:53] something like this. So as you can see, we have more pieces defining the hole in the
[4:58] in the edges, as you can see, and less in the middle. Then we just do a convex decomposition
[5:03] and we get almost a perfect collision mesh that will work well for RBD or the edit nodes
[5:08] in Solaris. And I just did the same for the other part. But as I was telling you, this is just too
[5:14] much for what I needed. So I ended up just using these convex decomposition simple one.
[5:19] Let's see next. In here, we have this shape. And now if I do a convex decomposition,
[5:31] and as you can see, we will have this. And this will not work when I want to place the CD.
[5:38] If you remember from the final mesh, I placed the CD, the CD only on that part of the mesh.
[5:44] And it will it will not collide properly because this geometry extends to the bounding box.
[5:50] So this is a bit being nitpicky, but I wanted to go that deep. So you can actually try to do
[5:57] 0.1. This will take a second. No, maybe less 0.03.
[6:04] And now we get a better representation, but still is not a
[6:16] divided mesh. So it doesn't have the different bounding boxes. The ideal solution would be to
[6:22] have a scenario would be to have a single box in here, another box in here, representing the
[6:31] different features of the object. So what I did in the end is create a cluster for each part of
[6:37] the mesh that looks something like this. This might be a bit too much, but in the end it worked okay.
[6:43] And then I can iterate over each cluster and do a convex and we get a perfect
[6:48] representing or segmented geometry. So the way I'm doing that is actually pretty simple.
[6:54] We start with the relative point bounding box, which is just a value representing from 0 to 1
[7:00] representing the bounding box of our objects. So for y, for x and for z, then I create a ramp
[7:07] for each axis. In this case, I only use x and z. So I didn't need that to
[7:14] divide the mesh into sections on the y axis. And we use that ramp. So for example, let me get rid
[7:20] of the z bucket. And now I'm just taking the x mask, the relative bounding box x component,
[7:27] and I'm just positioning where I want those cuts, as you can see. And I'm doing the same for z.
[7:35] So let me get rid of this and go to z. And as you can see, I'm doing the same in here, just
[7:40] positioning where I want. You can subdivide the mesh if needed. So that's it. So I'm just using
[7:45] the positions in here. So I take the ramp, the value of the ramp and multiply it by the different
[7:52] sections I want and round it to an integer. So let me combine now both, make sure you
[7:58] add an offset so we don't have clusters being equal. And then just assign it to a natural.
[8:05] Then we iterate over each piece, each index piece, and just to, in this case, the convex
[8:10] cell, not even convex decomposition. And that's basically how I did for all the pieces. So for
[8:16] example, this one, this one was simpler. I just needed to do one y to separate the rounded part
[8:23] and then do a convex cell. And then for this one, since it has this range shape, I just
[8:28] place some points and do a or an oil fracture, as you can see, and do the convex decomposition.
[8:33] And this will be more than enough. I don't, for my final scene, I don't even need that this.
[8:38] But again, I wanted to go deep on this topic. That's why I ended up doing all of this.
[8:44] Let's look at this one. This is just a convex cell. This one is again, I do, I divided on the y again,
[8:51] again using these constant ramps and two convex cells. And for this one, let's see,
[8:58] this one ended up being a bit more complicated because I had these floating parts. So I did the
[9:03] same in here, divided into sections, but in this case, I also included the y is the same workflow.
[9:09] And yeah, that's basically how I've done all the segmentation of the geometry.
[9:15] This one is just the CD. Then we have the segmented geometry. I'm also doing a rig to
[9:25] close out the shape. You can look on Patreon on how I did that. And I'm then combined the
[9:30] different variations of the closed, the closed with CD, the open with CD and the CD only.
[9:36] And I merge back and I just merge from a different attribute I had to create the name attribute.
[9:43] And the name attribute will be pretty simple. So let's see the name attributes in this case is
[9:49] this one. So it either it starts with the variation, then CD and overall name. And then if it's the
[9:55] case or the disc, that's basically it. And then we move into Solaris where I did the setup for
[10:03] creating the asset. So basically, I start with a single primitive, let's actually do this.
[10:12] And go in here. So I start with a single component, then create oops, then create the scopes.
[10:19] So proxy and render, configure the primitive just like we did in the other example. So one
[10:24] per proxy, one per render, then in a for each iterating over each premium in the second input,
[10:29] which is the variations of the render geometry. And then we have the variations of the proxy
[10:34] geometry. I'm grafting the branches for the the render geometry and for the proxy and just
[10:41] adding a variant. And in the end, we can come in here and switch to different variants. So CD
[10:48] closed. So let me actually go to with CD and then open and we can switch also for the proxy.
[10:56] So let me pick another one and pick final render, you can see we have the different variation,
[11:00] then export it as an exit as an asset. Then in the final part,
[11:06] so I just imported the different assets and position it more or less where I want. And then
[11:12] with the edit node, I can actually using physics place it when wherever I want. So basically what
[11:18] I do is to, for example, place this and then in physics mode, I can just drag it and place it
[11:24] where I want. So that was basically it. So another important thing is that if I used the original
[11:34] scale of the scene, which is basically really small, the collision geometry using the proxy.
[11:42] So let me actually go again to this, the collision geometry wouldn't work that well. So I had to
[11:48] scale up the scene as I told you before. And it's pretty simple to do. We just create a simple
[11:54] scale matrix. In this case, I created a matrix for and then we do usd transform and use the
[12:01] print path, which is the scene, which is at the top of our hierarchy. And then I name it and do it
[12:10] by the x form. Then we do the edit nodes to put everything in place. You can see the difference.
[12:15] This one was intersecting. And then we revert the scale. So we just do the inverse one divided by
[12:21] the scale that we applied. And that's basically how I set all these up. So yeah, that's basically it.
[12:28] I will create a demo scene so you can have a look on your own on Patreon. And yeah,
[12:32] if you enjoyed, please leave a comment and I will see you next time.



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
