---
title: Procedurally mask deforming / animated geometry - Houdini
source: YouTube
url: https://www.youtube.com/watch?v=UL-VdOBmXgE
author: the point and prim
ingested: 2026-07-16
houdini_version: "Not specified"
tags: [smooth-function, distance-along-geometry, masking, procedural-animation, rest-attribute, performance-optimization, the-point-and-prim]
extraction_status: complete
frames_dir: tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedurally mask deforming / animated geometry - Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=UL-VdOBmXgE)
**Author:** the point and prim
**Duration:** 8m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, and sorry for the long absence. In this video we are continuing with smooth
[0:08] function masks. We are going to expand on the last video's method, so if you haven't
[0:12] seen it, you'll find the link below. We are now going to go through how to apply this
[0:16] effect to curved and deforming surfaces from any and multiple angles. If you want this
[0:21] hip file, grab it on Gumrood. If you downloaded the last one already, the product has been updated
[0:25] to contain this project as well. Link in the description. I am just starting off here
[0:28] with this model that has been subdivided and remest, so that is comprised of triangles.
[0:33] One quick tip is that the USD Import node tries to re-import on every frame, so make sure
[0:38] to set it to a static number, or it will attempt to cook the entire tree every frame. The key
[0:43] node for this effect is the distance along geometry node. Let's wire that up, manually select
[0:48] some start points temporarily, and visualize the output disk attribute. So what is actually
[0:52] happening here? The Docs definition reads as, measures the distance of the shortest path
[0:57] along the geometry's edges or surfaces from each start point. What does that even mean?
[1:02] Why can't I just use some basic vector maths or point cloud functions like attribute transfer?
[1:06] And the answer is simple. Simply measuring the distance between points or using point
[1:10] clouds like attribute transfer, both work entirely by measuring distance in world space,
[1:15] regardless of the connectivity or topology of the geometry. Distance along geometry respects
[1:19] these aspects, and that's why he can see how the attribute visualizer flows along the
[1:23] contours of the geometry. Back in the example, let's visualize our disk attribute. Our main
[1:28] problem now is that the attribute is not mapped between 0 and 1, as it returns the exact
[1:32] values that are measured along the geo. In this case, the attribute is mapped between
[1:35] 0 and roughly 0.6. In order to work with the smooth function easily, we will have to
[1:40] remap this between 0 and 1. A simple way to do this is to use an attribute promote, set
[1:45] to detail and maximum. Then we drop down a point for and wire it into the second input.
[1:50] Let's just clean this stuff up and bind in the disk attribute from the first input.
[1:54] Then we will want an import detail up to get the promoted disk attribute from the second
[1:57] input, and then a fit range with the promoted attribute piped into the source max, and we
[2:01] can bind up the new normalize data. That's now fit nicely between 0 and 1.
[2:07] Let's grab the visualizer again. We can see the full heat map is now visible. If that
[2:11] doesn't make sense, we have our disk attribute and the ramp is mapped between 0 and 1, but
[2:15] the disk attribute only occupies the range between 0 and around 0.6, which doesn't encompass
[2:19] the full range of the ramp. All we did with the promoted attribute is push the new maximum
[2:23] up to 1, remap in the attribute to a full 0 to 1 range. We won't get as complex with
[2:27] the smooth function remap this time as we covered it in the previous video. If any of
[2:32] this doesn't make sense, check that out first. I am just piping in the new disk attribute
[2:36] and exposing a parameter that I will animate. This time I am adding with an exposed parameter
[2:41] that I will name with that will let me control a softer looking fall off.
[2:46] As done previously, in order to break up the uniform band, I am just going to add some
[2:50] noise to the min value which will distort the edge. You probably already know this, but
[2:56] a nice way to get more interesting noise patterns is to use a different noise on the input
[2:59] position of your main noise. I am leaving it quite basic in this demo, but play around
[3:03] with stacking a bunch of them together and you can get some pretty nice results. One of
[3:07] the great advantages of this method is that you can change where the mask spreads from
[3:10] simply by changing the selection of the start points, allowing for easy art direction.
[3:15] This will work in multiple start points and from any angle as long as the geometry is
[3:18] connected. One of my favourite ways to proceduralize this is to set an ID on the points and then
[3:25] sort them randomly and blast out a range of them. Then I set a group with an on creative
[3:33] name such as start and copy that back into the main stream setting ID in the match by
[3:37] attribute field. If we turn on the group visualizer, we can see that the points have copied
[3:41] over in their exact locations from the second stream, which you can see here when we turn
[3:45] on the disks as well. If we come down to our distance along geometry node and replace
[3:49] the manual selection with the start group, you can see that the heat map interpolates
[3:53] between all of these start points. And of course, the animated mask will then work with
[3:56] our new start group. There is another important concept that we need to talk about and that
[4:00] is applying this to animated deforming geometry as the order of operations is important to
[4:04] maintain performance. So what I'm doing here is just making a grid and remashing it until
[4:10] we reach about a million points so that we can see a visible difference in terms of speed.
[4:15] Now let's just grab the nodes from the other example and paste them onto our new geo.
[4:19] Everything is working as intended as we have proceduralized the start group. We need
[4:23] some defamation to demonstrate this, so let's just put down a twist node and set a couple
[4:27] of keyframes. Everything is working fine until we go down to our distance along geometry
[4:31] node and let the timeline scrub. This footage is sped up by 300% and look how slow it is.
[4:37] This is because the node is performing quite an expensive calculation on every frame.
[4:41] The solution for this is to calculate the disk attribute only once and then copy the
[4:45] attribute onto the animated stream, which can be done easily here by just repositioning
[4:49] the twist node. As you can see, we instantly get our real time playback again. I'm just
[4:54] setting two keyframes on the mask parameter to match those from the twist. And the effect
[4:59] works nicely synced up now. The only issue is the noise button buzzing and that is caused
[5:03] by the noise swimming through world space. And of course, that is easily solved by setting
[5:07] a rest attribute before the animation and then using that to drive the noise instead of
[5:10] P. If we play the animation now, the buzzing issue has been rectified. We will now do a surface
[5:16] level walkthrough of this project to see how flexible this technique is. As with the last
[5:21] video, this will contain some more advanced techniques that I won't go through in depth
[5:24] here, so I encourage you to grab the hip file if you want to explore further.
[5:29] I start off with a circle animated with dollar F. This is all I'm using to get the flow
[5:33] effect along the curves. Then I just give it a 180 twist, rotate it, and merge the copies
[5:38] together. Here I am just applying a subtle animated noise and sweeping the curves into
[5:42] several rows. I apply another noise which is offset by each curve and sweep the curves
[5:47] again with a square profile. I am using connectivity to get a class attribute for the curves, which
[5:53] will be needed in the next steps. So now I am using a single frame of both the swept geometry
[5:58] and its original curves. The latter is assigned a group as I will need to split in the loop
[6:02] below. So we are looping over each of the curves according to the class attribute from
[6:06] before. It is hard to see in the wireframe, but essentially we have two streams now. The
[6:10] polygonal data and the original curve. I am creating the scale geometry by using a few
[6:15] tricks such as divide with compute dual and a primitive soft to scale each prime separately,
[6:21] and just extruding the pieces. I am setting rest here as we will need it for noise later,
[6:25] like the demonstration before. Over here I set the start group to an arbitrarily selected
[6:30] point number, and pipe that into a distance long geometry node, which I will attribute
[6:35] transfer to the scales geo. Now the stream that contains the curve, I am using this for
[6:40] one purpose mainly, and that is to open a point cloud where I will fill to P and use that
[6:44] to calculate a vector that is pointing away from the center of the curve. The last line
[6:48] is just retrieving the class attribute from the curve as I did replace it with a separate
[6:52] class attribute that I didn't actually end up using. So after we let this run over each
[6:57] piece, we have our original class attribute, the dist attribute, by directionally mapped
[7:01] along the length of each curve, as well as this vector attribute for displacement. Something
[7:05] to note is that I am fully aware that I am able to do this sort of thing with some clever
[7:09] manipulation of attributes along tangent U, but I have decided to save that for a future
[7:13] video as is another topic on its own. So now I simply apply this move function mask
[7:18] via the dist attribute. This is almost completely identical to what we did in the demonstration
[7:22] before, except I have some random offset via the class attribute, and I am just controlling
[7:26] the mask width inside the point bump. After that, it is simply a case of point forming
[7:30] the geometry using the animated swept curves from before. Important to note is that I am
[7:35] using the class attribute in the point forms that each curve deforms individually. This
[7:39] is the bulk of the work and the slowest calculation, so I pack the geometry and write it to
[7:43] disk. I calculate the velocity and then remove all points that have a color value less than
[7:47] 0.1. In this wrangle, I am applying some displacement based off of the direction vector I created
[7:52] earlier. I actually did an account for the fact that I deformed the geometry but did not
[7:57] update the attribute to match, which caused this shearing effect instead of the scales
[8:00] moving directly outwards, but I opted to keep it as I thought it looked interesting.
[8:04] The final point for up down here is a bit of noise break up, which uses rest like in
[8:08] the example, so that it doesn't swing through world space as the geomobes. I am not going
[8:12] to talk about the particle sim as it is out of scope of the video. It is a modified
[8:16] vex version of a technique featured by Simon Fiedler and the fantastic antagonist team,
[8:20] who explained the concept perfectly. I will link the video in the description. If you
[8:24] want to have a look at the rendering setup or study the effects setup further, please
[8:27] do grab the hip file. As mentioned in the intro, if you already have access to this product,
[8:31] I have updated it to now contain this project too. Please note that I have now set a suggested
[8:36] price of $10 as I have been completely consumed by greed, but you can still get it for free
[8:40] by just replacing it with a zero. That wraps up this chapter on smooth function masks.
[8:44] I hope you got some useful information out of these videos. Thanks so much for watching
[8:48] and see you in the next one.



---

## Captured Frames

- [0:43] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_000.jpg
- [1:45] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_001.jpg
- [3:10] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_002.jpg
- [4:31] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_003.jpg
- [4:49] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_004.jpg
- [5:07] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_005.jpg
- [6:52] tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
Extends the channel's single-axis "smooth function" masking technique (from the previous video) to arbitrary curved/deforming surfaces using the **Distance Along Geometry** SOP to measure geodesic (surface-respecting) distance from procedurally-chosen start points, then re-ordering the node graph so the expensive distance calculation runs once on a static pose instead of every frame of an animated/deforming mesh.

### Summary
Building on a prior video's flat, single-axis smooth-function mask, this tutorial shows how to art-direct a mask that spreads outward from arbitrary points across curved or deforming geometry — demonstrated first on a subdivided/remeshed triangulated bust model (with a callout that the USD Import LOP re-imports every frame unless pinned to a static frame number). The key node is **Distance Along Geometry**: given start points, it measures the shortest path *along the mesh's connectivity* (respecting topology/edges/surface, unlike world-space methods like point-cloud Attribute Transfer or straight point-distance, which ignore connectivity entirely) and outputs a `dist` attribute that visibly follows the surface's contours. Because `dist` isn't naturally bounded to 0–1 (it returns raw distance, e.g. 0 to ~0.6 in the demo), it's remapped: **Attribute Promote** (detail, maximum) captures the true max distance, an **Attribute VOP**/Point VOP imports that promoted detail value, and a **Fit Range** node maps `dist` into a clean 0–1 range using the promoted max as the new source-max — the same smooth-function mask logic from the previous video (animated min/range-top parameter, noise-broken edge) is then applied on top of this normalized distance. A major advantage of this approach is that changing *where* the mask spreads from is just a matter of changing which points feed Distance Along Geometry, enabling easy art direction — including a procedural method for auto-selecting start points: set an `id` on all points, randomly sort them, blast out a range, group the result (e.g. named "start"), then copy that group back onto the main stream by matching on `id` (via the copy/group node's "match by attribute" field) rather than by manual selection. The video's second major topic is **performance on deforming geometry**: remeshing a grid to ~1M points and applying a Twist deformer reveals that recomputing Distance Along Geometry every frame is extremely slow (the demo footage is sped up 300% and still looks sluggish) because the node performs an expensive per-frame graph-distance calculation. The fix is to reposition the node graph so distance is calculated **once**, before the Twist deformer, and the resulting `dist` attribute is simply copied onto the already-deformed/animated stream afterward — instantly restoring real-time playback since the expensive calculation is no longer re-run per frame. A secondary artifact this surfaces is "noise buzzing," caused by the noise field sampling world-space `P` while the geometry moves underneath it; the fix is the same **rest-attribute pattern** used elsewhere on the channel: cache a `rest` attribute before any animation is applied and drive the noise from `rest` instead of `P` so it stays locked to the surface. The remainder of the video is a faster, less-detailed walkthrough of the actual "scales" effect used to showcase the technique: animated circles are swept into curved rows/profiles, given a `class` attribute via Connectivity, then for each curve (looped by class) a "distance-along-geometry"-driven scale/extrude system builds individual scale geometry (using Divide-with-Compute-Dual and Primitive Split to scale each primitive independently), computes a per-scale outward-displacement vector from a point-cloud lookup back to the curve's centerline, and drives per-scale reveal/growth with the same normalized-distance smooth-function mask (offset randomly per curve via the class attribute), finished with class-aware Point Deform so each curve deforms its own scales independently, some intentional shearing left in from an un-updated displacement direction attribute, and a separate (out-of-scope) particle sim credited as a modified VEX version of a technique by Simon Fiedler/Antagonist Studio.

### Key Steps
1. Start from a triangulated/remeshed deforming mesh (watch for USD Import LOPs re-cooking every frame — pin them to a static frame).
2. Wire up **Distance Along Geometry** from manually (or later procedurally) selected start points and visualize the resulting `dist` attribute to confirm it follows surface contours rather than world-space straight lines.
3. Normalize `dist` to 0–1: **Attribute Promote** (detail, maximum) to get the true max distance value, then a **Fit Range** using that promoted max as source-max to remap `dist` cleanly into 0–1.
4. Apply the previously-covered smooth-function mask logic (animated range-top parameter, noise added to the min value for edge break-up, optionally with a second noise driving the first noise's input position for more interesting patterns) on top of the normalized distance.
5. Procedurally select start points instead of manual picks: set an `id` attribute, **Sort** randomly, **Blast** out a range, group the result (e.g. "start"), then copy that group back onto the main stream matching by the `id` attribute so it survives topology changes.
6. To test performance, remesh a grid to ~1M points and add a **Twist** SOP with keyframes; observe that Distance Along Geometry recalculating every frame is very slow on deforming geometry.
7. **Fix the performance issue** by moving the Distance Along Geometry node earlier in the graph (before the Twist/deformer) so it computes `dist` once on the static pose, then copy that attribute onto the animated/deformed stream afterward for instant real-time playback.
8. Fix any resulting "noise swimming" by caching a `rest` attribute before the deformation and driving the mask-breakup noise from `rest` instead of `P`.
9. (Showcase effect) Build curved scale rows via animated circle sweeps + noise, tag each curve with a `class` attribute (Connectivity), loop per-class to build scale geometry (Divide/Compute Dual + Primitive Split + Extrude), compute an outward vector via a point-cloud lookup to the curve center, drive reveal via the same distance-along-geometry mask (with per-class random offset), and Point Deform the scales onto the animated curves per-class.

### Houdini Nodes / VEX / Settings
Distance Along Geometry (start-point-based geodesic distance), USD Import (static-frame pinning caveat), Attribute Promote (detail, maximum), Point VOP / Attribute VOP (Import Detail, Fit Range), Fit Range, smooth function (mask remap, from the prior video in the series), Sort (random), Blast, Group (copy-with-match-by-attribute for procedural start points), Twist SOP (deformation test case), rest attribute (pre-deformation caching to fix noise-swimming), Connectivity (`class` attribute), Divide (Compute Dual), Primitive Split, Extrude, Point Cloud lookup (`pcopen`/`pcfilter`-style, centerline direction vector), Point Deform (per-class), Time Shift.

### Difficulty
Intermediate to Advanced (the core masking concept is approachable, but the node-graph-reordering performance fix and the full scales showcase involve non-obvious attribute/point-cloud tricks).

### Houdini Version
Not specified.

### Tags
#smooth-function #distance-along-geometry #masking #procedural-animation #rest-attribute #performance-optimization #point-cloud #connectivity #the-point-and-prim

---

## Related Tutorials
- [Houdini: How to mask with the smooth function](houdini-how-to-mask-with-the-smooth-function.md) — the direct prequel; this video explicitly builds on that video's single-axis smooth-function mask technique.
- [Particle rotations in Houdini (how to rotate orient)](particle-rotations-in-houdini-how-to-rotate-orient.md) — same channel/author; shares the smooth-function-driven-by-attribute approach for procedural animation without simulation.
- [Techniques for Fast Disintegration FX in Houdini](techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach.md) — same channel/author; reuses the Distance Along Geometry + smooth-function mask + rest-attribute pattern from this video as the basis for its disintegration mask.
