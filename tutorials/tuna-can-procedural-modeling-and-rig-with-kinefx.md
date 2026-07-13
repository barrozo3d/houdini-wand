---
title: Tuna Can | procedural modeling and rig with KineFX
source: YouTube
url: https://www.youtube.com/watch?v=hHLH7pr_eZo
author: cgside
ingested: 2026-07-13
houdini_version: "H19+"
tags: [kinefx, procedural-modeling, rigging, capture-proximity, sweep, quadremesh, polyfill, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Tuna Can | procedural modeling and rig with KineFX

**Source:** [YouTube](https://www.youtube.com/watch?v=hHLH7pr_eZo)
**Author:** cgside
**Duration:** 13m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back, so in this video I wanted to show you how I model this
[0:05] tunnecan and also how I did the rigging.
[0:07] So it's a simple exercise but it might have some challenges.
[0:10] So let's have a look on how we did this, how I did this.
[0:16] So as you can see this is the setup and it all starts from a simple line that I placed
[0:23] at the center of the Z axis.
[0:28] When I did this sweep to create the cap, I think it's called cap and basically what I
[0:32] did in here is set it to ribbon and columns and the end caps to grid and I played a bit
[0:37] with the end cap roundness and I also applied some scale.
[0:40] So we get this shape.
[0:42] So from the line we get this shape.
[0:44] Then I'm going to re-sample and apply some subdivision so not very high re-sample.
[0:50] Then I fuse and apply some smoothing to round it a bit off.
[0:54] And I'm going to select the section in here so I can add and create the cap design.
[1:00] Any near I'm just using a small expression so I can iterate over the points and select
[1:05] the section I want.
[1:08] Then I'm doing a poly-expand to create some geometry.
[1:10] These are my settings.
[1:11] I use offset surfaces, reverse and I use the Odinis quadrimash.
[1:15] In my settings are I enable symmetry on the x axis and I also set in here the edgeflow
[1:21] control to edge.
[1:22] If we set it to face it will be a mess.
[1:24] The rest is default settings.
[1:26] Then I'm applying some smoothing so we equalize a bit the edges.
[1:31] Then some thickness.
[1:33] After that some more smoothing, step divides and soften the normals.
[1:38] And that's my cap.
[1:39] Then I also created some this part, the interior part which is basically from the quadrimash.
[1:47] I created a group for the n-chair edges and create one for each n-chair edge, so one,
[1:51] two and three.
[1:53] And then I promote the respective group from a point to an edge group.
[1:58] Polyfill, X-Rat the patch, extrude it a bit in or inset it I mean.
[2:03] Then I do a circle from edges on that same group.
[2:07] Then extrude, blast, polyfill to have quads.
[2:09] You don't need to do that.
[2:11] Then just babel it, extrude the other edge.
[2:14] So when we apply some match mode, it doesn't end up with some gaps in here.
[2:24] Without the extrusion you can see we will have some gaps.
[2:27] So that's what I am doing in there.
[2:28] Then just transform it and match it to this part, to this leads.
[2:35] And the lead is an interesting approach because if we have a look, as you can see we have
[2:40] this kind of staircase effect where we are creating all these levels.
[2:46] And the way I am doing that is basically, so let me show you.
[2:50] I am creating this geometry as you can see.
[2:52] This is the base geometry.
[2:54] So we will have this staircase effect as I told you.
[2:56] And for that I am starting with a circle.
[3:00] Then I am generating 10 points because I want 5 levels and a teach level.
[3:04] So let me show you something in here.
[3:06] So I want to create this.
[3:07] And what I need to manipulate is the position dot y of the circles that I am going to copy
[3:13] and also the p scale.
[3:14] And the rules are for point zero and point one, we set the same y offset, same position dot
[3:21] y for point two and three.
[3:22] We also have the same, but we add one and so on.
[3:25] And for the p scale, we skip the point zero.
[3:29] And then we apply the same pattern to so point one and point two have the same p scale
[3:35] and point three and point four have the same p scale.
[3:38] And this and that ends up with this pattern.
[3:42] It's hard to see, but when we mesh it, it should look something like this.
[3:45] So we generate a bunch of 10 points because I want five levels and then we create the
[3:49] offset.
[3:50] So first one is the position dot y.
[3:52] So we divide the point, these are the point numbers as you can see, but right now they
[3:56] are only in the y.
[3:59] And we divide the point number by two.
[4:00] So we get four point four points for each two numbers.
[4:04] We get zero then one then two.
[4:06] So that's how we're offset for the position dot y.
[4:09] Then we just add some amplitudes, the desired amplitude.
[4:14] Then for the p scale, we do the same pattern with some scale, also to control the scale.
[4:18] But we offset one.
[4:19] So we only start at point one and point two.
[4:22] That's basically the result.
[4:23] And when we copy to points, we have this kind of concentric curves.
[4:27] But with enough geometry, so when we skin it, we create this pattern.
[4:32] So it's simple, but we might be happy to explain for me, but I think you get the idea.
[4:39] Then we smooth to get some slope.
[4:44] Often the normals, we group the center primitives because I don't want the least triangle mesh.
[4:50] Then I take the opportunity to write a boundary group from that selection.
[4:56] If we use that group, then polyfill using that boundary group, I polyfill it with a quadrilateral grid.
[5:03] And that's my can top.
[5:05] And after that, I just do a bavol, a subdivision, soften and create an image root.
[5:11] And that's our main parts.
[5:14] Then it comes to the rest of the body.
[5:17] And I'm gonna go pretty quickly with this.
[5:19] We start with the can top.
[5:21] So let me solve like this.
[5:24] And we group the unshared, convert to line.
[5:27] And we adjust the scale for the sweep that I'm using.
[5:31] Let me see in here a square tube.
[5:34] And this scale allows me to scale on different axis.
[5:38] Or the square tube is not round tube, square tube.
[5:42] Then I also output in here the prim call, which will give me an attribute on the primitives.
[5:48] That I can later in a group expression targets the desired primitives to extrude.
[5:53] So if the prim call is this ID and I can cycle through them.
[5:57] So you don't need to do that, so you can totally manually select it.
[6:01] But I decided to do it this way.
[6:03] Then I extrude it and mirror polybavol and subdivide.
[6:09] Then for the bottom part, I just take these poly extrude, which I'm outputting the extrude
[6:14] front seam, which will have this line in here, convert that to a line, which in this case
[6:20] will have two sort by proximity to point.
[6:24] So the interior primitive is always zero.
[6:27] So I can blast it.
[6:28] Then polyfill it with watery light rolls again and blast the curve.
[6:34] Just match size to the main position of the can.
[6:38] And then I can subdivide it and merge it over.
[6:41] And that's our procedural modeling done.
[6:45] Now let's have a look at the rig.
[6:46] Then I just match sizes, of course, to place it in the grid.
[6:49] That's about it.
[6:52] So now let's have a look at the rigging.
[6:54] And there's nothing too complicated.
[6:55] I share this technique many times before.
[6:58] So we have two rigs in here, one for the cap that we, it's a rigid, rigid former, and
[7:08] one for the lid, which is a softer one.
[7:12] That's not the technical name, but I'm trying here.
[7:15] So we start by merging over the leads and this interior part that will be attached to
[7:20] the leads and in the other side we merged the cap.
[7:25] And for the cap is just maybe we have a look at the grid for a delete first.
[7:29] So from the lead, I'm creating a line for the rig.
[7:32] So basically manipulating the positions of the pounding box min and max from the input
[7:37] one.
[7:38] And this goes to the input one, of course.
[7:41] And then just adding the point and adding a polyline between point point point and point
[7:45] two.
[7:46] Then I'm resembling quite a bit because you can that working better with the iPoint count.
[7:52] This will be our capturing rig.
[7:56] I'm also reversing.
[7:57] So when I apply the deformation, it goes from this side instead of the other one, as you
[8:03] can see.
[8:04] So that's just an easy fix.
[8:06] I'm reversing the winding order.
[8:09] Then I initialize the rig.
[8:10] So just initialize transforms and we have an image report.
[8:13] Then we capture by proximity.
[8:15] I use these settings.
[8:17] You have to play with the drop off and the max point influence.
[8:21] And then we have to point the form.
[8:23] So the bond form.
[8:24] So for the bond form, we connect geometry to the first input, the rest skeleton or the
[8:29] rest rig to the second input, as you can see.
[8:32] And for the third input, we deform.
[8:34] So let's have a look first at this one.
[8:37] So I have done this before.
[8:39] Basically for this line, we are creating a curve view.
[8:42] So just a point attribute along the curve.
[8:44] Let's start from zero and goes to one.
[8:47] Then we create an angle, a parameter for an angle.
[8:50] That's the amount of rotation we will do to the local transform.
[8:55] So basically this amount of rotation.
[8:58] And I'm also adding some offsets.
[8:59] So it doesn't rotate all the runs.
[9:03] I mean, so as you can see, I just want to offset just the tip.
[9:07] I just want to rotate the tip, I mean.
[9:09] So that's why I'm doing these offsets.
[9:10] Then for the animation, I am fitting the time variable between point one second and point
[9:15] 35 seconds from zero to one.
[9:18] And then I remap.
[9:19] So it's not so linear.
[9:21] So as you can see, it starts and goes and jumps right away to the final position.
[9:27] And I've done this plenty of times.
[9:29] Then we just rotate the angle and we multiply the animation.
[9:33] So we have the animation, of course.
[9:36] The animation is just a value that goes from zero to one.
[9:39] So we start at the rest position and then we animate it.
[9:42] We animate the angle along the time.
[9:45] And we rotate it around X because if we look at the transform or local transform can
[9:50] be, as you can see, this is the exact same.
[9:53] We want to rotate it around that axis.
[9:55] So that's basically it.
[9:56] And then we do the second animation, which is basically opening up the lid.
[10:05] And that's the exact same setup, but I'm just animating the offset in here just linearly
[10:10] and setting a small angle.
[10:13] So yeah, that's basically it.
[10:15] And we get this result.
[10:16] And I'm just inviting the sign of the angle because I want to go the other way around.
[10:21] And we can play with the angle to have more or less.
[10:24] And as you can see, I am entering some specific values on the offset.
[10:29] So we get these very small follow-off on the offset.
[10:35] So from one to minus point, point two.
[10:38] So yeah, then is just the point of the form as I told you.
[10:42] And we get the animation.
[10:44] Now we need the cap to follow this animation, of course.
[10:48] So far that's, I am bringing in the cap.
[10:52] Looking at point, that's the correct position.
[10:56] You can create it manually.
[10:57] I just decided to manipulate again the bounding box, max and min and place the points in there
[11:02] for my rig, rig doctor to initialize the transforms and the name attribute.
[11:07] And we just do a capture pack deal.
[11:09] So we just connect the point to the G.
[11:11] That's basically it.
[11:12] And we pack the input.
[11:14] Then we have this boundary form that is going.
[11:19] This boundary form that is going to animate.
[11:23] And we are not rotating in here.
[11:24] We are taking the rotation from this rig in here.
[11:29] So basically I am loading the point transform, which is the world transform of the input
[11:36] one, which is this animated rig.
[11:38] And I'm grabbing the first point, so point zero.
[11:41] And I want to grab the transform in there.
[11:47] I want to grab the transform from that point and copy to my point in this point of my
[11:56] cap.
[11:58] So I'm grabbing that transform that I'm just calculating an offset because if I don't do
[12:03] that, so let me show you in here.
[12:05] If I go in here and I just grab the transform and set the point transform to the anim, as
[12:12] you can see, there will be an offset.
[12:14] Because my initial position of that point of that specific point is not in the exact position
[12:21] of this point.
[12:22] So I am just doing a quick step up in here to offset one point from the other.
[12:28] So just calculate this offset and add it to the result.
[12:30] So that's basically what I'm doing in here manipulating the matrix.
[12:34] Then after we have that point transform copied, we should have the animation and the cap
[12:40] following the lead.
[12:42] So now if we have a look, we have the initial animation and then the it unfolds properly.
[12:51] Then we just merge it over our geometry and we can possibly have a look at the name
[12:56] attribute and we get the final result.
[13:01] So yeah, guys, this is basically the final result.
[13:03] I hope you have enjoyed and learned something new.
[13:05] As always, you can grab the full file on my Patreon alongside all the other project files
[13:09] from my videos.
[13:11] And that's basically it.
[13:14] I hope you like this and let me know in the comments if you do this differently.
[13:20] Thank you and see you next time.



---

## Captured Frames

- [0:32] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_000.jpg
- [1:11] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_001.jpg
- [2:52] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_002.jpg
- [4:23] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_003.jpg
- [5:57] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_004.jpg
- [8:13] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_005.jpg
- [12:51] tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/frame_006.jpg

---

## Structured Notes

### Core Technique
Procedurally models a tuna can (ring-pull lid with a staircase-patterned embossed top, and a mirrored square-tube can body) then rigs the lid with a KineFX capture/deform skeleton so the pull-tab lid animates open, with the metal cap following the lid's motion via a point-transform-copy trick.

### Summary
Starts from a single line swept (Ribbon + Columns, grid end caps) into the lid's cross-section profile, then builds the embossed "staircase" pattern on the lid top using paired point offsets on concentric circles (position.y and pscale grouped in twos with incrementing offsets) before skinning them into rings. The can body is built separately from a mirrored square-tube sweep driven by a `primnum`-based group expression so specific faces can be targeted for extrusion. For the rig: a simple 2-point capture line (built from the lid's bounding box) drives a proximity-captured bind deform that rotates/opens over an eased 0-1 time range, and the rigid cap is made to follow that same animated rig by copying the first point's world transform onto the cap's own point (correcting for the initial offset between the two points via a matrix-based offset calculation) before a Capture Pack/Bone Deform.

### Key Steps
1. **Lid cross-section:** start from a single **Line** centered on the Z axis, run a **Sweep** with cross-section set to Ribbon + Columns, end caps set to Grid, tune end-cap roundness and apply some scale to get the base lid profile shape.
2. **Resample** lightly, **Fuse** + smooth to round the profile, then select the section to receive the embossed cap design (via a small point-index expression to iterate/select which points).
3. **Poly Expand** to build geometry for the design (Offset Surfaces mode, Reverse enabled), then run **Houdini's native QuadRemesh** with X-axis symmetry enabled and **Edge Flow control set to Edge** (setting it to Face instead produces a broken/messy result).
4. Smooth to equalize edges, add **thickness**, smooth again, subdivide, and soften normals to finish the embossed cap piece.
5. **Interior/n-gon cleanup:** from the quadremesh result, group each n-gon (non-quad) edge separately (one group per n-gon, e.g. groups 1/2/3), promote each point group to an edge group, then **PolyFill** the patch and extrude/inset it; run **Circle from Edges** on the same group, extrude, blast, and PolyFill again to force clean quads. Extruding the matching edge before Match Mode avoids visible gaps between pieces that appear if you skip the extrusion.
6. **Staircase/embossed pattern:** start from a Circle, generate 10 points for 5 levels (2 points per level). Point pairs 0-1, 2-3, 4-5... share the same `position.y` offset, incrementing by one level each pair; for `pscale`, the pattern is offset by one point (skip point 0), pairing points 1-2 and 3-4 with matching scale values. The Y offset is computed as `floor(point_number / 2) * amplitude`; copying these circles to points produces concentric rings that, once given enough resample density, **Skin** into the staircase pattern when meshed.
7. Smooth for slope, soften normals, group the center primitives (to avoid a degenerate triangle-fan mesh at the center), save a boundary group from that selection, then **PolyFill** the center hole using a quadrilateral-grid fill via that boundary group. Bevel, subdivide, soften, and add an Image ROP to finish the can top.
8. **Can body:** from the can top, group unshared edges, Convert to Line, and run a **Sweep** with a square-tube cross-section (not round) — the tube's Scale parameter allows independent per-axis scaling for the square profile. Output a `primnum`-derived attribute (a "prim call" ID) so a **Group Expression** can target specific primitives for extrusion by index instead of manual selection.
9. Extrude, **Mirror**, PolyBevel, and Subdivide for the main body wall. For the bottom, take the Poly Extrude's "extrude front" seam output, convert to a line, sort the two resulting curves by proximity to a point (so the interior primitive is always index 0), blast it, PolyFill with a quad-grid, blast the remaining curve, Match Size to the can's main position, subdivide, and merge everything together.
10. **Rig setup — lid capture:** build a 2-point line for the capture rig by manipulating the input's bounding-box min/max positions, add points and a polyline between them; resample for a better point count. Reverse the winding order if the deformation runs from the wrong end.
11. **Rig Doctor**-initialize the transforms (produces an Image ROP too), then **Capture by Proximity** (tune Drop Off and Max Point Influence) followed by **Bone Deform** — geometry into input 1, rest skeleton into input 2, the animated/deformed rig into input 3.
12. **Lever animation:** build a curve-parameter (`curveu`, 0-to-1 along the curve), add an Angle parameter for local-transform rotation amount, plus an offset so only the tip rotates (not the whole rig). Drive the animation by **Fit** on the time channel between two specific seconds mapped 0-1, then **Remap** the result so it isn't linear (fast start that eases into the final position). Multiply the angle by this animation value and rotate around the axis matching the rig's local transform (X in this case).
13. A second, near-identical animated setup opens the lid itself — same structure, but animating the offset linearly with a small angle value and inverting the angle's sign for the opposite rotation direction; small offset values (e.g. 1 to -0.2) give a subtle falloff on where the bend concentrates.
14. **Cap-follows-lid:** bring in the cap geometry, place its rig point by manipulating the bounding-box min/max (same trick as before), Rig Doctor to initialize transforms + name attribute, then **Capture Pack** (connect the point to the geometry, pack the input).
15. In the boundary/animated Bone Deform for the cap: instead of driving its own rotation, load the **world transform (point transform)** of the first point (point 0) from the already-animated lid rig, then in a wrangle copy that transform onto the cap's own point — computing and adding an offset first, since the cap's initial point position doesn't exactly coincide with the lid rig's point (directly assigning the transform without this offset correction introduces a visible positional jump).
16. Merge the cap and lid/body geometry together; the cap now follows the lid's opening animation correctly, completing the rig.

### Houdini Nodes / VEX / Settings
Line → Sweep (Ribbon+Columns, Grid end caps) → Resample/Fuse/smooth → point-index expression (section select) → Poly Expand (Offset Surfaces, Reverse) → native **QuadRemesh** (X symmetry, Edge Flow = Edge) → per-n-gon Group + PolyFill + Circle from Edges + extrude/blast/PolyFill cleanup → staircase pattern (`floor(pointnum/2)` Y-offset + paired-offset pscale on 10-point circle, Copy to Points, Skin) → boundary-group PolyFill (quad grid) → Sweep (square tube cross-section) + `primnum`-driven Group Expression for targeted extrusion → Mirror/PolyBevel/Subdivide → sort-by-proximity-to-point for bottom cap seam → **Rig Doctor** (init transforms) → **Capture by Proximity** (Drop Off, Max Point Influence) → **Bone Deform** (3-input: geo / rest rig / animated rig) → curveu attribute + Angle parameter + offset wrangle → Fit (time→0-1) + Remap (ease) for animation driving → **Capture Pack** + world-point-transform copy wrangle (with computed offset) for the cap-follows-lid trick.

### Difficulty
Intermediate — the modeling side (sweep, quadremesh, n-gon cleanup, staircase pattern) is approachable; the KineFX rigging side (capture/bone-deform chain, curve-parameter-driven animation, and especially the point-transform-copy-with-offset trick for making the cap follow the lid) assumes prior KineFX rigging familiarity.

### Houdini Version
Not stated explicitly; uses native QuadRemesh and standard KineFX rigging nodes (Rig Doctor, Capture by Proximity, Bone Deform, Capture Pack) available in Houdini 19+.

### Tags
#kinefx #procedural-modeling #rigging #capture-proximity #sweep #quadremesh #polyfill #animation #intermediate

---

## Related Tutorials
Cross-link with [Mechanical rigging in Houdini - Attaching custom controls](mechanical-rigging-in-houdini---attaching-custom-controls.md) — shares #rigging #kinefx; that tutorial covers a complementary custom-control attachment technique for KineFX rigs.
