---
title: Tuna Can | procedural modeling and rig with KineFX
source: YouTube
url: https://www.youtube.com/watch?v=hHLH7pr_eZo
author: cgside
ingested: 2026-06-23
houdini_version: "H19+"
tags: [kinefx, procedural-modeling, rigging, bone-deform, capture-proximity, sweep, quadremesh, polyfill, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tuna-can-procedural-modeling-and-rig-with-kinefx/
frame_count: 4
---

# Tuna Can | procedural modeling and rig with KineFX

**Source:** [YouTube](https://www.youtube.com/watch?v=hHLH7pr_eZo)
**Author:** cgside
**Duration:** 13m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello everyone and welcome back, so in this video I wanted to show you how I model this tunnecan and also how I did the rigging. So it's a simple exercise but it might have some challenges. So let's have a look on how we did this, how I did this. So as you can see this is the setup and it all starts from a simple line that I placed at the center of the Z axis. When I did this sweep to create the cap, I think it's called cap and basically what I did in here is set it to ribbon and columns and the end caps to grid and I played a bit with the end cap roundness and I also applied some scale. So we get this shape. So from the line we get this shape. Then I'm going to re-sample and apply some subdivision so not very high re-sample. Then I fuse and apply some smoothing to round it a bit off. And I'm going to select the section in here so I can add and create the cap design. Any near I'm just using a small expression so I can iterate over the points and select the section I want. Then I'm doing a poly-expand to create some geometry. These are my settings. I use offset surfaces, reverse and I use the Odinis quadrimash. In my settings are I enable symmetry on the x axis and I also set in here the edgeflow control to edge. If we set it to face it will be a mess. The rest is default settings. Then I'm applying some smoothing so we equalize a bit the edges. Then some thickness. After that some more smoothing, step divides and soften the normals. And that's my cap. Then I also created some this part, the interior part, which is basically from the quadrimash. I created a group for the n-chair edges and create one for each n-chair edge, so one, two and three. And then I promote the respective group from a point to an edge group. Polyfill, X-Rat the patch, extrude it a bit in or inset it I mean. Then I do a circle from edges on that same group. Then extrude, blast, polyfill to have quads. You don't need to do that. Then just babel it, extrude the outer edge. So when we apply some match mode, it doesn't end up with some gaps in here. Without the extrusion you can see we will have some gaps. So that's what I am doing in there. Then just transform it and match it to this part, to this leads. And the lead is an interesting approach because if we have a look, as you can see we have this kind of staircase effect where we are creating all these levels. And the way I am doing that is basically, so let me show you. I am creating this geometry as you can see. This is the base geometry. So we will have this staircase effect as I told you. And for that I am starting with a circle. Then I am generating 10 points because I want 5 levels and a teach level. So let me show you something in here. So I want to create this. And what I need to manipulate is the position dot y of the circles that I am going to copy and also the p scale. And the rules are for point zero and point one, we set the same y offset, same position dot y for point two and three. We also have the same, but we add one and so on. And for the p scale, we skip the point zero. And then we apply the same pattern to so point one and point two have the same p scale and point three and point four have the same p scale. And this and the ends up with this pattern. It's hard to see, but when we mesh it, it should look something like this. So we generate a bunch of 10 points because I want five levels and then we create the offset. So first one is the position dot y. So we divide the point, these are the point numbers as you can see, but right now they are only in the y. And we divide the point number by two. So we get four point four point zero for each two numbers. We get zero then one then two. So that's our offset for the position dot y. Then we just add some amplitudes, the desired amplitude. Then for the p scale, we do the same pattern with some scale, also to control the scale. But we offset one. So we only start at point one and point two. That's basically the result. And when we copy to points, we have this kind of concentric curves, but with the in F geometry. So when we skin it, we create this pattern. So it's simple, but might be happy to explain for me, but I think you get the idea. Then we smooth to get some slope. Often the normals we group the center primitives because I don't want the is trying all mesh. Then I take the opportunity to write a boundary group from that selection. If we use that group, then polyfill using that boundary group, I polyfill it with a quadrilateral grid and that's my can top. And after that, I just do a battle, a subdivision, soften and create an image root. And that's our main parts. Then it comes to the rest of the body and I'm going to go pretty quickly with this. We start with the can top. So let me solve like this. Then we group the unshared convert to line and we adjust the scale for the sweep that I'm using. Let me see in here a square tube. And this scale allows me to scale on different axis or the square tube is not round to square two. Then I also output in here the prim call, which will give me an attribute on the primitives that I can later in a group expression targets the desired primitives to extrude. So if the prim call is this ID and I can cycle through them, so you don't need to do that to do that. So you can totally manually select it, but I decided to do it this way. Then I extrude it and mirror polybable and subdivide. Then for the bottom part, I just take these poly extrudes, which I'm outputting the extrude front seam, which will have this line in here, convert that to a line, which in this case will have two sort by proximity to point. So the interior primitive is always zero. So I can blast it. Then polyfill it with watery light rolls again and blast the curve. Just match size to the main position of the can and then I can subdivide it and merge it over. And that's our procedural modeling done. Now let's have a look at the rig. Then I just match sizes, of course, to place it in the grid. That's about it. So now let's have a look at the rigging. There's nothing too complicated. I share this technique many times before. So we have two rigs in here, one for the cap that we, it's a rigid, rigid former and one for the lid, which is a softer one. That's not the technical name, but I'm trying here. So we start by merging over the leads and this interior part that will be attached to the leads and in the other side we merged the cap. And for the cap is just maybe we have a look at the grid for a delete first. So from the lead, I'm creating a line for the rig. So basically manipulating the positions of the pounding box min and max from the input one and this goes to the input one, of course. And then just adding the point and adding a polyline between point point point and point two. Then I'm resembling quite a bit because you can that working better with the iPoint count. This will be our capturing rig. I'm also reversing. So when I apply the deformation, it goes from this side instead of the other one, as you can see. So that's just an easy fix. I'm reversing the winding order. And I initialize the rigs. So just initialize transforms and we have an image report. Then we capture by proximity. I use these settings. You have to play with the drop off and the max point influence. And then we have the point before. So for the bond form, we connect geometry to the first input, the rest skeleton or the rest rig to the second input, as you can see. And for the third input, we deform. So let's have a look first at this one. So I have done this before. Basically for this line, we are creating a curve view. So just a point attribute along the curve that start from zero and goes to one. Then we create an angle parameter for an angle. That's the amount of rotation we will do to the local transform. So basically this amount of rotation. And I'm also adding some offsets. So it doesn't rotate all the runs. I mean, so as you can see, I just want to offset just the tip. I just want to rotate the tip. I mean, so that's why I'm doing these offsets. Then for the animation, I am fitting the time variable between point one second and point thirty five seconds from zero to one. And then I remap. So it's not so linear. So as you can see, it starts and goes and jumps right away to the final position. And I've done this plenty of times. And we just rotate the angle and we multiply the animation. So we have the animation, of course. The animation is just about that goes from zero to one. So we start at the rest position and then we animate it. We animate the angle along the time. And we rotate it around X because if we look at the transform or local transform can be as you can see, this is the exact same. We want to rotate it around that axis. So that's basically it. And then we do the second animation, which is basically opening up the lid. And that's the exact same setup, but I'm just animating the offset in here just linearly and setting a small angle. So yeah, that's basically it. And we get this result. And I'm just inviting the sign of the angle because I want to go the other way around. And we can play with the angle to have more or less. And as you can see, I am entering some specific values on the offset. So we get these very small follow-off on the offset. So from one to minus point, point two. So yeah, then is just the point of the form as I told you. And we get the animation. Now we need the cap to follow this animation, of course. So far that's I am bringing in the cap. Taking a point at the correct position, you can create it manually. I just decided to manipulate again the bounding box max and min and place the points in there for my rig. Rig doctor to initialize the transforms and the name attributes. And we just do a capture back deal. So we just connect the point to the G. That's basically it. And we pack the input. Then we have this boundary form that is going. This boundary form that is going to animate. And we are not rotating in here. We are taking the rotation from this rig in here. So basically I am loading the point transform, which is the world transform of the input one, which is this animated rig. And I'm grabbing the first point, so point zero. And I want to grab the transform in there. I want to grab the transform from that point and copy to my point in this point of my cap. So I'm grabbing that transform that I'm just calculating an offset because if I don't do that, so let me show you in here. If I go in here and I just grab the transform and set the point transform to the anim, as you can see there will be an offset. Because my initial position of that point of that specific point is not in the exact position of this point. So I am just doing a quick step up in here to offset one point from the other. So just calculate this offset and add it to the result. So that's basically what I'm doing in here manipulating the matrix. Then after we have that point transform copied, we should have the animation and the cap following the lead. So now if we have a look, we have the initial animation and then the it unfolds properly. Then we just merge it over our geometry and we can possibly have a look at the name attribute and we get the final result. So yeah guys, this is basically the final result. I hope you have enjoyed and learned something new. As always, you can grab the full file on my Patreon alongside all the other project files from my videos. And that's basically it. I hope you liked this and let me know in the comments if you would do this differently. Thank you and see you next time.

**Frame:** tutorials\frames\tuna-can-procedural-modeling-and-rig-with-kinefx\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedural tuna can modeling (line → Sweep cap, QuadRemesh inset interior, staircase lid via point-number-divide P.y + pscale pattern → Skin, body from Sweep+PolyExtrude) + KineFX rigging with two systems: Bone Deform / Capture by Proximity for soft lid animation, and Capture Packed + point-transform copy for rigid cap following the lid.

### Summary
13m21s tutorial by cgside. Full procedural workflow for a tuna can with two-part KineFX rig. Modeling: line-based Sweep creates the cap profile; QuadRemesh builds the smooth interior inset panel; lid uses a mathematical staircase pattern (point_number/2 for Y-offset, point_number-1/2 for pscale) to drive concentric curves that skin into the stepped lid geometry. Body is built from unshared-edge Sweep + PolyExtrude with primcol-based selection. Rigging: lid uses KineFX Bone Deform with Capture by Proximity on a resampled curve rig; animation drives rotation via `fit(time, 0.1, 0.35, 0, 1)` with nonlinear remap. Cap uses Capture Packed (rigid); its transform is copied from the animated lid rig point using `getpointtransform` / offset correction / `setpointtransform`.

### Key Steps

**Modeling: Cap**
1. Line at Z-axis center → **Sweep SOP** (ribbon mode, columns, end caps = grid, adjust roundness + scale) → Resample → Fuse → Smooth → base cap shape
2. Select desired section with small expression iterating over points → **PolyExtrude** → **QuadRemesh** (symmetry X, edge flow = Edge not Face — face = mess) → Smooth → Thickness → Smooth → Subdivide → Soften normals

**Modeling: Interior Panel**
3. From QuadRemesh output: group n-chair (unshared) edges, promote to edge group → **PolyFill** → **Extrude** (inset) → **Circle from Edges** on that group → Extrude → Blast → PolyFill (quads) → Bevel → extrude outer edge (to close gaps on subdivision)

**Modeling: Lid (staircase)**
4. Create 10 points (5 levels × 2); apply staircase math:
   - `P.y offset = int(ptnum/2) * amplitude` (pairs: 0,0,1,1,2,2,3,3,4,4)
   - `pscale = int((ptnum-1)/2) * scale_factor` (offset by 1 so pairs start at pt1,pt2, then pt3,pt4…)
5. Copy concentric circles to these 10 points → **Skin SOP** → staircase lid profile
6. Smooth → group center prims → PolyFill center (quadrilateral grid) → Bevel, Subdivide, Soften normals

**Modeling: Body**
7. Group unshared edges from can top → Convert to Line → **Sweep SOP** (square tube profile) → scale axes
8. Output `primcol` attribute to cycle and target each prim by expression for selective extrude
9. Extrude → Mirror → PolyBevel → Subdivide

**Modeling: Bottom**
10. Take extrude front seam line → Convert to Line → Sort by Proximity (interior prim = 0) → Blast → PolyFill (watery light grids) → Blast curve → Match size → Subdivide → Merge

**Rigging: Lid (Bone Deform, soft)**
11. From lid geometry: manipulate bounding box min/max → build polyline → **Resample** (high count for smooth deform) → **Reverse** (change deformation start direction) → **Initialize Transforms** → **Rig Doctor**
12. **Capture by Proximity**: tune drop-off and max point influence
13. Animation Wrangle: `curveU` (0→1 ramp along curve) → angle parameter → `float anim = fit(time, 0.1, 0.35, 0.0, 1.0)` → remap (nonlinear, jumps to final fast) → `rotate(localxform, angle * anim, {1,0,0})` → `setpointtransform(0, ptnum, newxform)` → offset so only tip rotates
14. Lid opening: same setup, animate offset linearly, small angle, negate for opposite direction

**Rigging: Cap (Capture Packed, rigid)**
15. Create single point at bounding box max position → **Rig Doctor** → Initialize transforms + name → **Capture Packed** (single-point-to-geo binding)
16. **Copy transform from animated lid rig**: `matrix animXform = getpointtransform(1, 0)` → compute offset between initial positions → add offset to result → `setpointtransform(0, ptnum, correctedXform)` → cap rigidly follows lid
17. **Bone Deform** (lid geo): input1=rest geo, input2=rest skeleton, input3=animated skeleton → merge with animated cap

### Houdini Nodes / VEX / Settings
- **Sweep SOP** — line → surface; ribbon mode, grid end caps, roundness control
- **QuadRemesh SOP** — remesh to quads; symmetry X; edge flow = Edge (not Face)
- **Circle from Edges** — create circle from selected edge loop
- **Skin SOP** — skin concentric curves into a surface (staircase lid)
- **PolyFill SOP** — fill boundary with polygon grid
- **Capture by Proximity** (KineFX) — attach geo points to nearest skeleton points
- **Bone Deform** (KineFX) — deform geo using skeleton animation; inputs: rest geo, rest rig, animated rig
- **Rig Doctor** (KineFX) — initialize transforms and name attributes on skeleton
- **Capture Packed** (KineFX) — rigid-body attachment of packed geo to single skeleton point
- `getpointtransform(input, ptnum)` — fetch world transform matrix from point
- `setpointtransform(input, ptnum, matrix)` — set world transform on point
- `fit(time, t0, t1, 0, 1)` — map time range to 0-1 animation value
- `primcol` attribute — assign primitive color/ID for expression-based group selection
- `int(ptnum/2)` pattern — staircase Y offset for lid modeling

### Difficulty
Intermediate

### Houdini Version
H19+

### Tags
[kinefx, procedural-modeling, rigging, bone-deform, capture-proximity, sweep, quadremesh, polyfill, animation, intermediate]

---

## Related Tutorials
- procedural-growth-with-kinefx-and-the-labs-tree-tools.md (KineFX for procedural vegetation)
- mops-motion-operators-for-houdini-part-3.md (matrix/transform math underlying KineFX)
- model-a-procedural-flower-houdini-tutorial.md (procedural SOP modeling)
