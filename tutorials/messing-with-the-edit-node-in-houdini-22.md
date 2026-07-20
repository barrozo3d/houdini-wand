---
title: Messing with the Edit node in Houdini 22
source: YouTube
url: https://www.youtube.com/watch?v=Wkj1DMn-X2w
author: cgside
ingested: 2026-07-19
houdini_version: "22"
tags: [lop, solaris, usd, rbd, sop, procedural, intermediate, advanced, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/messing-with-the-edit-node-in-houdini-22/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Messing with the Edit node in Houdini 22

**Source:** [YouTube](https://www.youtube.com/watch?v=Wkj1DMn-X2w)
**Author:** cgside
**Duration:** 12m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [1:05] tutorials/frames/messing-with-the-edit-node-in-houdini-22/frame_000.jpg
- [2:40] tutorials/frames/messing-with-the-edit-node-in-houdini-22/frame_001.jpg
- [3:49] tutorials/frames/messing-with-the-edit-node-in-houdini-22/frame_002.jpg
- [5:03] tutorials/frames/messing-with-the-edit-node-in-houdini-22/frame_003.jpg
- [7:27] tutorials/frames/messing-with-the-edit-node-in-houdini-22/frame_004.jpg
- [10:41] tutorials/frames/messing-with-the-edit-node-in-houdini-22/frame_005.jpg

---

## Structured Notes

### Core Technique
Building custom proxy collision meshes so the Houdini 22 Edit node's physics mode (LOPs/Solaris) collides correctly with concave geometry, using convex decomposition, ramp-driven clustering, and USD purpose assignment (render vs proxy).

### Summary
cgside hits the core limitation of the new Edit node's physics placement in Houdini 22: it builds convex hulls of scene geometry by default, so objects can't nestle into concave shapes (a sphere won't drop behind a wall; a CD won't sit in its case tray). The fix is authoring a **proxy-purpose mesh** per asset: convex-decompose (or cluster then per-cluster convex hull) the geometry in SOPs, name it, assign it to the USD **proxy** purpose with Configure Primitive while the full-res mesh gets **render** purpose — the Edit node then uses the proxy as the collision shape. The video also covers a scene-scale gotcha (tiny real-world scale breaks collisions; scale the whole stage up via a matrix + USD Transform on the root prim, edit, then invert) and a full component-builder/variant workflow for a CD-case asset.

### Key Steps
1. **Reproduce the issue** [frame_000, 1:05; frame_001, 2:40] — in LOPs: SOP Create mesh (box + PolyExtrude wall), graft a sphere, drop an Edit node, select prims → Add Physics → physics mode → Draw Sim Geometry: the green sim geometry shows a convex hull bridging the concavity, so the sphere won't collide into the pocket (no exposed way to change hull generation — likely for performance).
2. **Simple fix** — inside the SOP Create, after PolyExtrude: **Convex Decomposition** (reduce Max Concavity) → delete `name` → set `name = proxy_mesh` → Merge with the render mesh; then **Configure Primitive** ×2: render geometry → purpose **render**, proxy geometry → purpose **proxy**. Edit node now collides against the true concave shape.
3. **Preserving holes** [frame_003, 5:03] — plain convex decomposition erases a CD's center hole. Better: Subdivide → density attribute weighting scatter toward edges → scatter → **Voronoi Fracture** → Convex Decomposition per piece: pieces trace the hole; heavier but valid for RBD too (the Edit node likely runs RBD under the hood).
4. **Ramp-clustered segmentation** [frame_004, 7:27] — for box-like cases: **Relative Point Bounding Box** (0–1 per axis) → per-axis ramps (`chramp`) positioned at desired cut locations → multiply ramp value by section count and `rint()` to an integer cluster id; combine axes with an offset so ids stay unique; write to an attribute; then For-Each over cluster → **Convex Hull** per cluster = clean segmented collision boxes. Y-axis included only where needed (floating parts).
5. **Asset build in Solaris** [frame_005, 10:41] — Component-style graph: create render/proxy scopes, Configure Primitive per purpose, For-Each over variant prims grafting render + proxy branches, **Add Variant**; switch variants (closed / open / with CD / disc only) and export as a USD asset.
6. **Scene-scale workaround** — at real-world (tiny) scale the proxy collisions misbehave: build a scale matrix (matrix4), **USD Transform** on the root prim path, place everything with Edit-node physics at the large scale, then apply the inverse (1/scale) transform.

### Houdini Nodes / VEX / Settings
- LOPs: SOP Create, Graft Branches, **Edit** (Add Physics, physics mode, Draw Sim Geometry), Configure Primitive (purpose: render/proxy), Add Variant, For-Each (prims), USD Transform, Set Variant
- SOPs: PolyExtrude, Convex Decomposition (Max Concavity ~0.03–0.1), Convex Hull, Voronoi Fracture, Scatter (density-weighted), Subdivide, Merge, Name/Attribute Delete, Relative Point Bounding Box, For-Each (pieces)
- VEX (cluster wrangle): per-axis `chramp()` on relbbox components, `rint(ramp * sections)`, axis combine with offset → cluster attribute
- USD: purposes render/proxy; component/variant asset structure; root-prim scale matrix + inverse
- Default Edit-node sim geometry = convex hulls (not user-configurable)

### Difficulty
Intermediate–Advanced

### Houdini Version
Houdini 22 (Edit node physics mode)

### Tags
lop, solaris, usd, rbd, sop, procedural, intermediate, advanced, houdini-22

---

## Related Tutorials
- [Intro To Houdini Solaris - Full Beginner Course](intro-to-houdini-solaris---full-beginner-course.md) — the component-builder/variant foundations this asset workflow uses
- [Improve Solaris Performance - Houdini Tutorial](improve-solaris-performance---houdini-tutorial.md) — proxy-geometry authoring for viewport speed; same render/proxy purpose mechanics
- [H22 - Modeling & Solaris | Fianna Wong | Houdini 22 HIVE](h22---modeling-solaris-fianna-wong-houdini-22-hive.md) — the H22 Solaris feature context around the Edit node
