---
title: Making Trash in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=KCy4Sw3nbcQ
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [modeling, rbd, vellum, vdb, vex, uv, procedural, environment, advanced]
extraction_status: complete
frames_dir: tutorials/frames/making-trash-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Making Trash in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=KCy4Sw3nbcQ)
**Author:** cgside
**Duration:** 11m47s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So I've been building this environment in
[0:04] Odini for a tutorial and in today's video I wanted to show you how I did this
[0:09] trash assets. So nothing to complicate it but it might have a few tips for you.
[0:16] So let's dive into this trash and as you can see I have this variation so far.


### Trash [0:17]
**Transcript (timestamped):**
[0:25] It's not too much but it's also since I'm building this from scratch it takes a
[0:31] little bit of time to do them. So let's see. Since I had this scan from a
[0:36] previous tutorial I'm reusing it so it's nothing really complicated just a
[0:41] curve with a profile and then revolving and we will do that in the last
[0:45] assets but I'm starting with this one and then I quad-remesh it also. So I'm
[0:50] starting with this base. You can ignore this since I tried first doing this
[0:55] with Vellum then I'm doing the UBs by selecting the seams in here because I have a
[1:00] group of the seams as you can see really simple. You can ignore this then I'm
[1:09] going to do these with RBD to squash the can as you can see. So for that I have
[1:16] the input then I'm scattering 500 points and doing a simple Varunovic
[1:21] fracture. We get something like this. Then I'm pinning part of these constraints
[1:27] since these Varunovic fractures also output the constraints and I'm pinning part
[1:32] of it so the top so I can actually show you how that looks like. So I'm pinning
[1:40] those top points by using the relative point pounding box and I can select
[1:45] more or less this case I just want to top part so it doesn't deform. Then
[1:50] RBD configure I'm not using these bounding box just changing a bit the
[1:56] collision padding in here and a shrink amount. Then I'm converting the
[2:00] constraints to surface points that usually works better. From here I am setting
[2:06] the constraints properties, setting to soft and enable the switch constraints
[2:12] to be glue. So at the end I want to switch them to glue these are my settings
[2:16] you can increase or decrease these and play with it. I don't think plus this
[2:20] is plasticity in here is enabled yeah. So then on the top can I'm setting those to
[2:28] be soft but quite high as you can see the same for the glue and then I'm just
[2:38] simulating these and switching the constraints that frame 18 so we
[2:42] I simulate this and of course I have also a box crashing the acting as the
[2:51] collider and it will look something like this. So as you can see my box is
[2:55] coming down and acting as a collider to crush the the can. So as I told you at
[3:02] frame 18 I'm switching to the ars constraints. Then it's simple as using the
[3:06] RBD deform pieces and I can deform the incoming geometry with the constraints
[3:13] and with the proxy geometry which in this case will be just for geometry. Then
[3:18] just time shift it and this is my can. Match size it to have a real world size
[3:26] and that's my can. Then moving into the back which looks something like this.
[3:34] So this is supposed to be a bag of ships. For that I'm starting with a
[3:39] planner patch. Then planner inflates this is a new logo for the new 20.5.
[3:46] Saving the boundary edges so these edges in here because I'm gonna use it
[3:51] later for UVs. Clipping a bit of the end as you can see. Yoviflaton and I'm using
[4:00] as sims those boundary edges and we have perfect UVs or close to it. Then
[4:07] doing a simple valum cloth and a valum solver in here that will do something
[4:11] like this effect. And inside the valum solver to have this effect I could have
[4:17] used a pop attract but in this case I just used the just manipulator here the
[4:23] velocity by getting the bounding box center creating a vector from the bounding
[4:30] box center minus the P so a vector pointing in and I added also some zero
[4:35] center offset noise in here to the position so I get some sort of random effect
[4:41] as you can see so it's not very uniform. Then just multiplying a bit the
[4:45] velocity so it's not so quick let's say. So that's basically the effect and I
[4:52] valum post process adding some subdivision and also some thickness just
[4:58] than just time shifted and cashed. From there I can just place it on the floor as
[5:05] you can see. So now let's move into the cup we have two versions this one and


### Cup [5:06]
**Transcript (timestamped):**
[5:12] this one. So for this one I'm starting with the tube then I have a sphere which
[5:20] I transform into a VDB and I also smooth it a bit and then the form the geometry
[5:25] with that VDB. So in this case by doing the volume sample and a volume gradient
[5:31] and moving the position along the gradient multiplied by the SDF and we get
[5:38] this sort of effect. So just like a big deformer or something like that. Then I'm
[5:43] grouping in here a center loop just by selecting 12 points out of the
[5:52] these 12 points are also the columns of the tube and I'm selecting that from
[5:58] multiple points and then offsetting by in this case the same amount of columns
[6:03] times three I can increase in here which I can select in here which one I want
[6:07] just by offsetting this one. Then subdividing your Veon rap cylinder which will
[6:12] work fine for this case. Then in here I'm grouping the unchair points and also
[6:19] saving the boundary groups promoting those two edges. Then on the first one I am
[6:24] polyfilling and polybippling as you can see I'm selecting that one of the
[6:28] boundaries for the other boundary I'm converting into a line and sweeping and
[6:32] we get the cup then I transform it down match size it to the correct size in
[6:38] this case something like that. Then for the second version I'm object merging
[6:43] this mesh and then with that range that we selected in here this middle one I'm
[6:50] just soft transforming that in along an axis and playing with the soft radius as
[6:55] you can see. Pending a little bit transforming it to place and match sizing. So
[7:01] that's cup B. So for the container so the container is something like this as
[7:08] you can see and I'm just doing off of it because I'm lazy. So I'm starting with


### Container [7:10]
**Transcript (timestamped):**
[7:14] agreed in set it a little bit transforming that in that the extruded front
[7:20] group polybippling everything to give that rounded look. So actually unshared
[7:27] edges. Poly extruding those unshared edges in a curved way as you can see
[7:32] because I'm coming in here and I'm extruding those unshared and setting in this
[7:38] case the shape to be curved and then I go into spine control and playing with
[7:46] the magnet in here as you can see and with all these parameters. Cleeping
[7:53] in off on both sexes so I can subdivide it better. UV flatten really simple
[8:00] just don't need to give any sort of seams subdividing because right now I'm
[8:09] going to create the noise so I can clip it with clip by attribute that specific
[8:16] noise as you can see. So in here just come and clip it to have some some of
[8:22] dissolves. Poly extruding to have some thickness and also I'm probably reducing
[8:28] because I don't need those many polygons. I just wanted that to to have enough
[8:33] geometry for the enough subdivisions for the noise to work. Match sizing and
[8:38] that's my container. I also have in here an experimental second version which is
[8:45] by merging in the single side geometry then remaching. Scalch it a bit with
[8:52] flattened brush and with the move brush to have this sort of result and
[8:58] subdividing and doing a mesh sharpen to start to have this crumblet look. Then I
[9:05] do another attribute blur set to proximity which is very similar to the
[9:09] mesh sharpen and from there I can I don't want this sort of geometry at the end
[9:16] because it's still broken and cursed so I'm going to remach it. Measure the
[9:22] curvature to get those sharp edges and from here I can create a target mesh
[9:30] size so I can remach it by attribute as you can see it's added to adaptive and
[9:35] in the target mesh size I'm just decreasing the value of those convex areas
[9:41] convex areas yeah and then re-projecting it to the original version. This
[9:47] doesn't too much but then I do a small mesh sharpen and soften normals and
[9:52] calculate the UVs again and then just transform it in place and we get
[9:59] something like this. So not very successful but anyways so the last one is the


### Bottle [10:05]
**Transcript (timestamped):**
[10:06] bottle and here I just started with a curve, resample it, selecting one of the
[10:12] points and this will become Andy in later stage then revolving, fusing, top
[10:21] transform to squash it a bit so I'm just selecting that group as you can see
[10:27] that group that expanded so if I go into points as you can see this group in
[10:32] here expanded to this loop then I'm doing the sub-transform and scaling
[10:39] along the Z I could play with the sub-radios and do a bit more then I'm group
[10:44] expanding so I can promote it to primitives and bless the label that I can
[10:50] pick a little bit merge it and subdivide it and we should have the label in
[10:55] here as you can see maybe I should give it a color. From here just
[11:00] transforming it down and this is the bottle. So a lot of work and we get
[11:05] something like this which in the environment it should when I scatter it
[11:14] around it should look something like this. So let me know if you guys want me to
[11:19] cover this environment on the next video I might part a new series and yeah if
[11:27] you want to grab the files from this video the trash setup you can do so on my
[11:33] patreon alongside with exclusive tutorials hours of exclusive tutorials and
[11:37] all the project files from my videos. Please let me know your thoughts in the
[11:41] comments and other than that thank you for watching and I'll see you next time
[11:45] thank you



---

## Captured Frames

- [0:20] tutorials/frames/making-trash-in-houdini/frame_000.jpg
- [1:40] tutorials/frames/making-trash-in-houdini/frame_001.jpg
- [3:20] tutorials/frames/making-trash-in-houdini/frame_002.jpg
- [4:20] tutorials/frames/making-trash-in-houdini/frame_003.jpg
- [5:40] tutorials/frames/making-trash-in-houdini/frame_004.jpg
- [7:20] tutorials/frames/making-trash-in-houdini/frame_005.jpg
- [9:00] tutorials/frames/making-trash-in-houdini/frame_006.jpg
- [10:40] tutorials/frames/making-trash-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
A five-asset trash-prop pipeline for a forest-litter environment: a **crushed soda can** via RBD (Voronoi Fracture + soft/glue constraints + a falling-box collider, with mid-sim constraint switching), a **chip bag** via a hand-tuned Vellum cloth "attract toward center + noise" velocity trick, a **VDB-deformed cup** (gradient-based volume displacement using a smoothed sphere SDF), a **spine-controlled poly-extrude container** with two variants (clean noise-clipped version and an experimental ZBrush-in-Houdini crumple pass), and a **squash-transformed bottle** with a soft-transform-based label wrap.

### Summary
**Crushed can:** starting from a revolved/QuadRemeshed profile curve (reused from a prior tutorial's scan asset) with UVs picked via a saved seam group, the can is Scattered with 500 points and **Voronoi Fractured** to generate crushable pieces plus RBD glue constraints; the top rim points are pinned (selected via **Relative Point Bounding Box**) so the can's top stays rigid while the body crushes; **RBD Configure** tunes collision padding and shrink amount, constraints are converted to surface points (generally works better), and constraint properties are set to **Soft** with **Switch Constraints set to Glue** and plasticity enabled — soft/glue values tuned higher specifically on the can's top for extra rigidity there. A falling Box acts as the crushing collider; partway through the sim (frame 18), the constraints are **switched to RBD** to transition from a soft-holding-together phase into a proper rigid-body break/crush phase. Finally **RBD Deform Pieces** deforms the original (proxy) incoming geometry using the simulated constraint data, Time Shift grabs the crushed final frame, and Match Size sets real-world scale. **Chip bag:** built from a planar patch **Inflated** (a new Houdini 20.5 node), with boundary edges saved before a bit of end-clipping, UV Flattened using those boundary edges as seams for near-perfect UVs; a **Vellum Cloth** sim gets its crinkled look not from a POP Attract but from a hand-built velocity in the Vellum Solver: a vector from each point toward the **bounding-box center** (`bbcenter - P`) pulls geometry inward, with **zero-centered position noise** layered in for a non-uniform, organic crinkle, and the resulting velocity scaled down to avoid overly fast motion; finished with post-process subdivision and thickness, then Time Shifted, cached, and placed on the floor. **Cup (two versions):** a Tube is deformed by a smoothed-sphere **VDB**: a **Volume Sample + Volume Gradient** pair computes a displacement direction, and points are moved along that gradient scaled by the sampled SDF value — effectively a bespoke "bulge" deformer using volume data instead of a dedicated deform node. A center loop is selected by picking every Nth point matching the tube's column count (offset tunable to select different loops), Subdivided ("Veon wrap cylinder" — likely "Open Subdiv" catmull-clark), boundary groups promoted to edges: one boundary is Polyfilled + Poly-Beveled for a rim, the other Converted to Line and Swept for a base — producing the cup shape, Match-Sized to real-world scale. The second cup variant reuses the same mesh and the previously-selected middle point range, applying a **Soft Transform** along one axis (tuning soft radius) to pinch/reshape the profile differently, then Peaked and Match-Sized. **Container:** a Grid, slightly transformed, with its front group Extruded and Polypatched for a rounded look; unshared edges are **Poly Extruded with Shape set to Curved**, using **Spine Control**'s magnet parameters to sculpt the curve profile; edges are clipped on both axes for cleaner subdivision, UV Flattened (no manual seams needed), Subdivided for enough resolution to support a later noise-driven **Clip by Attribute** pass (creating dissolve/decay-like cuts), Poly Extruded for thickness (polycount reduced afterward since the noise step didn't need that much density), and Match-Sized. A second, experimental container variant merges in single-sided geometry, Remeshes, hand-sculpts with the **Flatten** and **Move** sculpt brushes for a crumpled look, Subdivides, and runs **Mesh Sharpen** plus an **Attribute Blur (Proximity mode)** (similar effect to Mesh Sharpen) to emphasize creases — but the resulting mesh was "still broken and cursed," so it's Remeshed again, **Measure (Curvature)** flags sharp edges, and a **Remesh by Attribute** step (adaptive, target mesh size reduced specifically in convex areas) re-projects onto the original crumpled version for cleaner topology, finished with a light Mesh Sharpen, softened normals, and recomputed UVs — the author candidly calls this second pass "not very successful." **Bottle:** a resampled profile Curve (one point saved for a later handle/neck feature) is Revolved, Fused, and reshaped with a **Soft Transform** (scale along Z, tuned soft radius) on an expanded point-group loop to squash the silhouette; the label is created by Group-Expanding and promoting to primitives, Blasting away the label region, Peaking it slightly outward, merging back, and Subdividing for a raised label look (author notes it should probably be colored), then Match-Sized to finish.

### Key Steps
1. **Can base:** reuse a revolved/QuadRemeshed profile curve; pick UVs via a saved seam group.
2. **Fracture setup:** Scatter 500 points, **Voronoi Fracture** for crushable pieces + constraints; pin the top rim (selected via Relative Point Bounding Box) so it stays rigid.
3. **RBD configuration:** tune collision padding/shrink amount in **RBD Configure**; convert constraints to surface points; set constraint properties to **Soft** with **Switch Constraints: Glue** (plasticity enabled), using higher soft/glue values specifically on the can's top.
4. **Simulate + collide:** run the sim with a falling Box collider crushing the can; at **frame 18, switch the constraints to RBD** to transition from soft-hold to rigid break/crush behavior.
5. **Deform + finalize:** **RBD Deform Pieces** applies the simulated constraint motion to the original proxy geometry; Time Shift the crushed final frame; Match Size to real-world scale.
6. **Chip bag base:** Planar Patch → **Inflate** (new in Houdini 20.5) for volume; save boundary edges before clipping the ends; UV Flatten using those saved boundaries as seams for clean UVs.
7. **Vellum crinkle velocity (custom, not POP Attract):** in the Vellum Solver, compute `bbcenter - P` as a velocity vector pulling points toward the bag's bounding-box center; add **zero-centered position noise** for non-uniform organic crinkling; scale the resulting velocity down to avoid overly fast motion.
8. **Finish the bag:** post-process subdivision + thickness, Time Shift, cache, place on the floor.
9. **Cup VDB deform:** build a smoothed-sphere **VDB**; use **Volume Sample + Volume Gradient** to compute a displacement direction per point, then move each point along that gradient scaled by the sampled SDF value for a bulge-style deformation.
10. **Cup rim/base construction:** select a center loop (every Nth point matching the tube's column count, offset tunable), Subdivide, promote boundary groups to edges — Polyfill + Poly-Bevel one boundary for the rim, Convert to Line + Sweep the other for the base; Match Size.
11. **Cup variant B:** reuse the same mesh and the earlier middle point-range selection; apply a **Soft Transform** (single-axis scale, tunable soft radius) for a differently-pinched profile; Peak and Match Size.
12. **Container base:** Grid, slight Transform, Extrude the front group, Polypatch for roundness.
13. **Spine-controlled edge extrude:** Poly Extrude the unshared edges with **Shape: Curved**, sculpting the profile via **Spine Control**'s magnet parameters.
14. **Container UV + decay noise:** Clip both axes for cleaner subdivision, UV Flatten (no manual seams needed), Subdivide for resolution, then a noise-driven **Clip by Attribute** pass to fake dissolve/decay cuts.
15. **Finish container:** Poly Extrude for thickness, reduce polycount (not needed after the noise pass), Match Size.
16. **Experimental crumpled container variant:** merge single-sided geometry, Remesh, hand-sculpt with **Flatten** and **Move** brushes for a crumpled look, Subdivide, apply **Mesh Sharpen** + **Attribute Blur (Proximity mode)** to emphasize creases.
17. **Clean up the crumpled result:** Remesh again, **Measure (Curvature)** to flag sharp edges, run **Remesh by Attribute** (adaptive, reduced target mesh size in convex areas) and re-project onto the original crumpled shape for better topology; finish with a light Mesh Sharpen, softened normals, recomputed UVs, and Transform into place.
18. **Bottle base:** resample a profile Curve (saving one point for a later neck/handle feature), Revolve, Fuse.
19. **Squash the bottle:** expand a point-group loop, apply **Soft Transform** (Z-axis scale, tunable soft radius) to reshape the silhouette.
20. **Bottle label:** Group Expand + promote to primitives, Blast away the label region, Peak it slightly outward, merge back, Subdivide for a raised label look; Match Size to finish.

### Houdini Nodes / VEX / Settings
Modeling: Revolve, QuadRemesher (third-party), Group (seam), UV Flatten, Grid, Extrude, Polypatch, Poly Extrude (Shape: Curved, Spine Control magnet parameters), Clip (both axes, and noise-driven Clip by Attribute), Subdivide, Match Size, Curve, Fuse, Soft Transform (tunable soft radius), Group Expand, Group Promote, Blast, Peak, Remesh, Mesh Sharpen, Attribute Blur (Proximity mode), Measure (Curvature), Remesh by Attribute (adaptive, target mesh size), Transform. RBD/Vellum: Scatter, Voronoi Fracture (with constraints output), Relative Point Bounding Box (pin selection), RBD Configure (collision padding, shrink), constraint-to-surface-points conversion, RBD Constraint Properties (Soft, Switch Constraints: Glue, plasticity), RBD Bullet Solver (mid-sim constraint switch at frame 18), RBD Deform Pieces, Time Shift, Inflate (new in 20.5), Vellum Solver (custom VEX velocity: `bbcenter - P`, zero-centered position noise, velocity scale-down), Vellum post-process (subdivision, thickness). Volume: VDB conversion, Volume Sample, Volume Gradient (gradient-based point displacement scaled by SDF value).

### Difficulty
Advanced/Expert — combines RBD constraint-switching simulation, custom Vellum velocity VEX, volume-gradient deformation, and adaptive curvature-based remeshing; assumes strong procedural-modeling and simulation fundamentals.

### Houdini Version
20.5 (explicitly references "Inflate... a new node for 20.5").

### Tags
#modeling #rbd #vellum #vdb #vex #uv #procedural #environment #advanced

---

## Related Tutorials
Author announces a planned follow-up environment/scattering video using these trash assets — cross-link once that tutorial is found in this batch. Shares the Relative Point Bounding Box pinning technique and RBD-constraint-switching pattern with other cgside RBD/simulation tutorials once indexed together.
