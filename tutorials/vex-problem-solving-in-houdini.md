---
title: Vex Problem Solving in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Fiw_NedtssQ
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.410"
tags: [vex, vdb, sdf, cluster, uvs, gradient, quaternion, vines, ivy-generator, procedural-uvs]
extraction_status: complete
frames_dir: tutorials/frames/vex-problem-solving-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Vex Problem Solving in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Fiw_NedtssQ)
**Author:** cgside
**Duration:** 9m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hello everyone and welcome back so in this video I will be showing you two different solutions for some specific problems I faced and hopefully it you will find it useful and apply it to your future projects so let's get into it so I've been working on this IV generator tool it's not really finished or very good right now but hopefully in the future I will get it done but I will today show you how you can approach a specific problem I had so basically I'm scattering some points on the surface some initial points and I have some Target positions to to those points to to reach let's say and I need the points to be constrained to the geometry so for that I'm using a sub solver and the first thought would be to use um a ray project with the mode set to minimum distance so loading the geometry into second input and R projecting the points but as you can see they they will get stuck if I enable the r project they will get stuck around those concave areas so if I show you the geometry again so they will get stuck right here in these areas when doing the the r projection Ray projection so an approach I found was to use instead an SDF a smoothed out SDF so this is the initial geometry converted to VDB and then if I apply a smooth basically a bevel and I save this I output this as an SDF then in the sub solver I can load that SDF in the second input and in this Wrangle I'm basically moving the points where the SDF value is zero so along the surface and if I enable that as you can see the points will the green points which are the initial points that are traveling will not get stuck because we have that big bevel or that big VDB smooth so then you might ask well uh now the point will not respect the initial geometry so these these concave areas and whatnot so what we can do then after doing the trail we can uh do like an explosed view on the points by moving them along the normal and then we add the points and we can Ray project again using the same uh logic but this time using the the original SDF in this case I moved it a bit out so with the dilate that way the The Vines don't don't get inter don't intersect with the geometry so and if we do this with the same stdf projection we end up with the with the vines along the surface and not intersecting and most of and for the most part is respecting the original geometry so yeah that hopefully this was useful to you and let's get into into the second case so now we will get back to a familiar scene if youve been following this channel basically I have a mesh that has been converted from VDB operations and uh it will be difficult to select the Sims and do manual UVS so today I'm going to show you a similar approach when it comes to the orientation of the ovs but uh a different one when it comes to selecting The Sims which might be useful to you so I'm starting with a mesh with no UVS then I'm doing a remesh so we can work with less polygons this way the calculations will be faster and more easy to control then doing a basic R projection just to make sure the the corners are sharp enough and if you remember and if you watch that particular video um we use the shortest P to select the the corner points or the the hard edges but in this case I'm going to use the cluster node based on the normal so if I show you that attribute and disable this gradients you can see that is isolating the different pieces pretty well by using the normals and the way I found this works best is by using setting Computing the normals on the vertices with a cangle of zero and then promoting it to point with the promotion method set to modes you can try other approaches but modes work really well for me then just promoting these to A Primitive primitive attribute and then we can just select the boundary edges as you can see with this group from Atri boundary and we already have the seams for the UV flatten so if you don't care about the orientation this is this will give you already a pretty good result but I want to approach today how to do the UV rotation so the UV orientation in this case to set the the UVS properly so first of all we are creating a mask along the Y so using the relative Point bounding box y components so from 0 to one this way we can clearly uh see which way is up creating a connectivity based on the UVS so which UV Island will get uh a different ID we promote the UVS to a point attribute while splitting them also and then we move this to move the UVS to 3D Space by using at P equals V at UV and we also storing a rest position before that so later we can we can get get the initial mesh back you can see that this gradient this mask along Y is telling us which way is up so the red values so we need to rotate them somehow and for that I'm first going to measure the gradient of that mask based on a piece attribute in this case cluster so I can show you that gradient so it's looking something like this so you can clearly see if I show you also this one so it's pointing in the red Direction so if you watch this one is pointing down that one is pointing sideways and now we just need to calculate the the angle so that's what I'm doing in this Wrangle so we get the gradient Prim attributes so by using the prim num and then we can calculate the angle and this select uh function is like an if statement so if the length of the gradient because if I show you this gradient so in here in these pieces I don't want to rotate them and since the gradient here because they are facing the Y AIS since the gradient here is less than this threshold value in this case I found 0.1 worked well uh I will if if they are not bigger than 0.1 the length of the gradient is not bigger than 0.1 we set the the angle rot the rotation angle to zero otherwise we calculate the angle between the X component and the Y component then we get the UV Island Center and finally we do the qu quion Mets by creating the the quion first so with the the angle to rotates and the axis which will be around the Zed axis then we make sure we rotate from the center so we need to subtract the current UV position by its pivot that's why we Sav this UV Island Center and then we we rotate we rotate them using that quaternion and from that position and finally we just uh multip we just add the rotation and the pivot back so if we check the final results we get the is oriented properly then we can just attribute swap the P for the rest and we get the position back and since the UVS might be overlapping due to the rotation as you can see we can just UV layout them making sure we set to no rotations and the axis alignment to none so it doesn't rotate our Islands then just promote the point the UV attribute to vertices and fuse the point and finally we transfer back the UVS to the original mesh as you can see so going from this one to this one so yeah that's basically what I had for you today hopefully this was useful let me know in the comments and don't forget you can grab the sces on my patreon alongside with hours of exclusive tutorials and I also have some courses in there so yeah make sure to check that out thank you for watching and I'll see you next time f



---

## Captured Frames

- [0:20] tutorials/frames/vex-problem-solving-in-houdini/frame_000.jpg
- [1:30] tutorials/frames/vex-problem-solving-in-houdini/frame_001.jpg
- [2:30] tutorials/frames/vex-problem-solving-in-houdini/frame_002.jpg
- [3:40] tutorials/frames/vex-problem-solving-in-houdini/frame_003.jpg
- [5:00] tutorials/frames/vex-problem-solving-in-houdini/frame_004.jpg
- [6:20] tutorials/frames/vex-problem-solving-in-houdini/frame_005.jpg
- [7:30] tutorials/frames/vex-problem-solving-in-houdini/frame_006.jpg
- [8:40] tutorials/frames/vex-problem-solving-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Two unrelated VEX problem-solving sessions: (1) fixing vine/ivy growth points that get stuck in concave geometry areas during a SOP Solver by projecting onto a **heavily-smoothed VDB SDF** instead of the raw mesh, then re-projecting onto the original (dilated) SDF afterward to restore surface fidelity; (2) UVing a VDB-derived mesh with no clean seam options by using a **Cluster node keyed on vertex normals** (rather than Find-Shortest-Path) to detect island boundaries, then auto-orienting each resulting UV shell via a **measured mask-gradient → quaternion rotation** technique.

### Summary
For an in-progress ivy/vine generator tool, points are scattered on a column surface with target positions to grow toward, constrained via a SOP Solver. The obvious approach — Ray Project (Minimum Distance) directly onto the mesh each solve step — causes points to get permanently stuck in concave crevices. The fix: convert the geometry to VDB, apply a heavy **VDB Smooth** (essentially a large bevel), and output that as an **SDF**; inside the solver, a wrangle moves each traveling point to wherever that smoothed SDF's value is zero (i.e. onto the smoothed surface) — since there are no sharp concavities left to snag on, points travel freely. Because this smoothed-SDF surface no longer respects the original geometry's actual concave detail, a second pass fixes this after the vine paths are grown: points are pushed out along their normal (an "exploded view" offset), new connecting points/curves are added, and a second **Ray Project** — this time against the **original SDF, dilated slightly outward** — snaps everything back onto (near) the true surface without re-introducing the original stuck-in-concavity problem, since dilating the original SDF prevents the newly-added vine geometry from intersecting the mesh. For the second problem — UVing a VDB-derived mesh with no clean manual seam options — the mesh is Remeshed (fewer, easier-to-control polygons) and Ray-projected to sharpen corners; instead of the studio's earlier Find-Shortest-Path seam technique, a **Cluster** node driven by vertex normals (normals computed at a 0° cusp angle, then promoted point-wise using the **Modes** promotion method, then promoted again to primitive) isolates distinct mesh "pieces" purely from normal discontinuity — Group from Attribute Boundary on this cluster attribute directly yields usable UV Flatten seams. To also fix the resulting UV islands' rotation (not just position), a Y-axis relative-point-bounding-box mask is built to encode "which way is up," UVs are split/promoted to points and temporarily swapped into 3D position (`@P = @uv`, with the original position saved to a rest attribute first), then the **gradient of the Y-mask is measured per-cluster/piece** — the gradient vector directly reveals each island's current "up" direction in UV space. A wrangle computes the needed rotation angle (`atan2`-style logic between the gradient's X and Y components, skipped entirely via a `select()`/if-statement if the gradient length is below a ~0.1 threshold, since near-zero gradients mean the piece is already correctly Y-aligned and rotating it would be meaningless/noisy), builds a **quaternion** around the Z axis for that angle, rotates each UV point around its own island center (subtracting/re-adding the pivot), then the original position is restored via Attribute Swap. Since rotation can introduce new overlaps, **UV Layout** (rotations disabled, axis alignment set to none) resolves them without undoing the careful per-island orientation, and the UVs are transferred back to the original (non-remeshed) mesh.

### Key Steps
**Problem 1 — vines stuck in concave areas:**
1. Scatter growth points on a column surface with target positions; constrain via a **SOP Solver**.
2. Identify the failure mode: Ray Project (Minimum Distance) directly onto the raw mesh each solve step causes points to get permanently stuck in concave crevices.
3. **Fix**: convert the mesh to VDB, apply a strong **VDB Smooth** (acts like a large bevel), output as an **SDF**; inside the solver wrangle, move each point to the nearest position where this smoothed SDF value equals zero — eliminates concave snag points entirely.
4. After growth completes, restore original-surface fidelity: push points outward along their normal (exploded-view offset), add connecting points/curves for the vine geometry.
5. **Re-project onto the original SDF, dilated outward slightly**, via a second Ray Project pass — snaps the vines onto (near) the true mesh surface without reintroducing the stuck-in-concavity problem, since the dilation prevents intersection.

**Problem 2 — UVing a VDB-derived mesh via Cluster + gradient-based orientation:**
6. Remesh the UV-less VDB-derived mesh (fewer, more controllable polygons); Ray Project to sharpen corners.
7. Compute vertex **normals at a 0° cusp angle**, promote to points using the **Modes** promotion method (found to work best empirically), then promote again to primitives — this **Cluster** attribute cleanly isolates distinct mesh pieces by normal discontinuity alone, no manual seam picking needed.
8. **Group from Attribute Boundary** on the cluster attribute directly yields a usable seam group for **UV Flatten** — sufficient on its own if island rotation doesn't matter.
9. **UV orientation fix**: build a **Y-axis mask** via relative point bounding box (0→1, "which way is up"); run **Connectivity** on the UVs (per-island ID); split/promote UVs to points; save the original position to a **rest** attribute, then temporarily set `@P = @uv` to work in UV-as-3D-space.
10. **Measure the gradient** of the Y-mask per cluster/piece — the resulting vector directly encodes each island's current "up" direction.
11. In a wrangle: retrieve the gradient primitive attribute by `primnum`; compute the rotation angle via `atan2`-equivalent logic between the gradient's X/Y components; use a **`select()`** (if-statement equivalent) to **skip rotation entirely** (angle = 0) when the gradient's length is below a ~0.1 threshold (near-zero gradient = already correctly aligned, e.g. pieces facing straight along Y).
12. Compute the **UV island center** (pivot); build a **quaternion** (angle, Z-axis) and rotate each UV point around its own island's center (subtract pivot → rotate via quaternion → add pivot back).
13. **Attribute Swap** the temporary `@P` back for the saved rest-position attribute to restore true 3D geometry.
14. Run **UV Layout** with rotations disabled and axis alignment set to none (to preserve the careful per-island rotation just computed) to resolve any overlaps introduced by the rotation.
15. Promote the UV attribute back to vertices, Fuse, and transfer the finished UVs back onto the original (pre-remesh) mesh.

### Houdini Nodes / VEX / Settings
SOP Solver, Ray Project (Minimum Distance), VDB from Polygons, VDB Smooth, SDF export, wrangle-based zero-value SDF point-snapping, exploded-view normal offset, VDB Dilate (original SDF), second Ray Project pass; Remesh, Normal (0° cusp angle), Attribute Promote (Modes method, point→primitive), Cluster node (normal-based island detection), Group from Attribute Boundary, UV Flatten, relative point-bounding-box Y mask, Connectivity (UV islands), Attribute Promote (UV split to point), rest-position attribute save, `@P = @uv` UV-as-3D-space trick, Measure (gradient of mask per piece), Attribute Wrangle (`primnum`-indexed gradient retrieval, `atan2`-style angle calc, `select()` threshold-based skip, quaternion construction/rotation around Z, pivot subtract/re-add), Attribute Swap (position restore), UV Layout (no rotation, no axis alignment), Attribute Promote (UV to vertices), Fuse, UV transfer to original mesh.

### Difficulty
Advanced (both problems — SDF-smoothing-then-re-projecting for stuck points, and gradient-based quaternion UV rotation — are sophisticated, non-obvious production solutions).

### Houdini Version
20.5.410 (visible in viewport title bar).

### Tags
vex, vdb, sdf, cluster, uvs, gradient, quaternion, vines, ivy-generator, procedural-uvs

---

## Related Tutorials
- [Procedural UV's In Houdini](procedural-uvs-in-houdini.md) — the earlier Find-Shortest-Path-based approach to the same "UV a VDB-derived cake mesh" problem, contrasted here with the Cluster-based alternative and gradient-orientation technique.
- [Orient UVS like a PRO in Houdini 21](orient-uvs-like-a-pro-in-houdini-21.md) — deeper, more robust version of the same gradient/quaternion-based UV-auto-orientation technique used here.
- [Environments in Houdini Part 4 - Vines, Rocks and Fog](environments-in-houdini-part-4---vines-rocks-and-fog.md) — related vine-generation technique (`pcopen()`-based attachment mask) from the same channel.
- [Why you need to learn vex in Houdini #1](why-you-need-to-learn-vex-in-houdini-1.md) — shares this channel's from-scratch VEX-first problem-solving philosophy, here building a nearpoint()/max()-carry flood-fill clustering algorithm.
