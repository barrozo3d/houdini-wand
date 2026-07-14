---
title: Kinefx and Vellum Fluid in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=6wqRXRV7oxk
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [kinefx, rigging, vellum, simulation, vex, procedural, animation, advanced]
extraction_status: complete
frames_dir: tutorials/frames/kinefx-and-vellum-fluid-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Kinefx and Vellum Fluid in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=6wqRXRV7oxk)
**Author:** cgside
**Duration:** 19m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So ever since I saw this simulation here in Reddit,
[0:07] I wanted to create my own version in Odinni and this was done by Max Vujje, I don't know
[0:18] how to pronounce it, sorry. And you can check out his own version on his Patreon, so just
[0:26] giving credit, I did it on a slightly different way and I want to walk you through how I have done it.
[0:38] So here in Odinni I can show you my final result, as you can see it's not as great as Max version,
[0:46] but I did my best and still don't want to spend much time on it.
[0:53] So let's get started breaking down, I did everything in Odinni including this modeling,
[0:59] which is really simple and I'm gonna walk you through the network. So I'm just starting
[1:08] by creating a circle and rounded square with the simple shapes around it. And I'm merging them both
[1:21] and doing a poly bridge. From there I'm placing it in the center and grouping this bottom
[1:31] bottom points and promoting it to an edge group to do the Yovis as you can see. This is how the Yovis
[1:39] look, which can be used later on texturing if I ever texture this. Then I am polyfilling it
[1:48] and beveling the the R-deges, also doing the Yovis on those parts and creating a Yovila out.
[1:59] Let me just add the normal, so this is our base model. Let me just add the camera
[2:08] or I can do other objects. Then I'm selecting the patch group that was created by this polyfiel
[2:20] and I am group expanding it so I can create some more stiffness on the valum seam.
[2:29] As you can see I'm creating the bend stiffness. I am giving it a value of 10 on those frames
[2:40] and a value of 1 on the rest. 10, let me just say that. Then I'm creating two valum seams.
[2:51] So one that is I just let the object drop and it's like the initial state of the tube.
[3:03] So on the floor and slightly is not completely full as you can see and I have another one which
[3:13] is the tube empty and I just play honestly with the bend stiffness and that's basically it as you
[3:24] can see by the values. Then I'm just attributing just keeping the Yovis to clean off the attributes.
[3:38] Then I'm going to create the rig. We will use kin effects. So for that I'm creating a line
[3:47] along the Z axis and match sizing it to the tube and re-sampling it creating the
[3:57] carview attribute as you can see and then I'm transferring to the tube.
[4:09] From here first of all I have the two states that I told you and I am blending between them using
[4:18] some procedural animation. So fitting the frame between 1 and 48 from 0 to 1 I'm blending the two
[4:28] shapes. Since they have the same amount of topology I can just use a lurp and getting the position
[4:36] the position from the second inputs which is this geometry and just using a lurp to blend them
[4:46] as you can see. So from here I have the line that will be used as our rig.
[5:02] Let me just disable these points. Then I'm creating an aperture boot along these axes.
[5:10] Doing a slightly a slight transform, a slight scale because I was getting some issues with the rigging.
[5:20] So you can ignore that but it's there. Doing a rig doctor to initialize the rig and then doing
[5:32] a capture by proximity as you can see and it will look something like this.
[5:42] And from here I have a lot of points but I want to have a more straight look as you can see.
[5:52] I don't want this fully rounded. I want more this straight look and I should have done
[6:00] different sizes for each part but I didn't so that's how it goes. So in order to create this
[6:11] low-pollilup let's say or this straight look I am creating a group by range and selecting
[6:19] some points in an interval and then in the rig wrangle which I add the help of swalch.
[6:30] I'm creating first the spiral then doing an offset so I can scrub so I can unroll the spiral
[6:40] and I'm also using this ramp so I can have more control where it's position which is just a
[6:52] multiplier of the angle which is the spiral itself and then I'm animating it with a feed function
[7:04] from completely unrolled to almost fully rolled.
[7:13] Then I'm using a bond deform as you can see from the capture by proximity and using as the second
[7:22] input the rest position and then the animated one and this is how it looks so it shouldn't be too
[7:31] slow but I'm recording. From here so we have this and from here we're doing an attribute blur
[7:44] to smooth out a bit the shape because I was getting some intersection. Basically this capture by
[7:50] proximity is really fast but it's not the best rigging algorithm let's say or the best capturing
[8:00] system is just the fastest one and it worked well in this case.
[8:09] Then I'm caching so this is how it looks.
[8:17] Deleting some attributes just keeping the normals and UVs and also deleting most of the
[8:25] groups just keeping the patch one and from here I have the two animations and let's see
[8:36] in here actually it's pretty simple I'm just creating a valum seam to have some displacement to
[8:42] use later in rendering so nothing fancy in here and let's move on to also I have here the top part
[8:57] the modeling part of this top piece and this nothing fancy just started from the patch group
[9:08] and did an extrusion and created a spiral and position it in here so that's just a static mesh
[9:16] that we need to deform to follow the tube animation so in here I'm loading the tube and doing a time shift
[9:27] and in here I'm orienting it to the tube as you can see and the way I'm doing that is by grouping
[9:43] that top part of the tube the patch and then converting it to points and creating a reference point
[9:56] group so as you can see I have here in here basically by calculating the group point
[10:03] pounding box center of those primitives I have previously selected and from there I can just
[10:12] create a near point from that position and set the point group so that's how I'm selecting that
[10:23] point adding the normals which is really important in this case point normals so I can have the normal
[10:30] of that specific point that you can see in here from there I have the shape that is positioned in the center
[10:44] and I can move it there and the way I'm doing that is again the same logic as I have done in
[10:54] two videos already we have a selection of these unshared points and we grab the center the
[11:05] bounding box center of that selection with getting get point bounding box center then we create the
[11:11] normals for it so it will be on the minus z then we have that specific point in here that I talked
[11:23] about and we grab the normals then you create the rotation matrix we diagonal so from the
[11:33] from this base position which is in here to the target one which is that reference point
[11:44] and then we grab the position and we do the transforms again I told you before logic by swolch
[11:53] and in here I'm doing the point the form so basically taking the
[12:06] the tube animation and the rest state of the first frame and transforming it as you can see
[12:16] but I had the slight problem in here so basically when I did the first point the form
[12:26] I was getting this stretch look so I did one with a naturoput blur but as you can see it also
[12:37] transforms the outer part so in the end I mixed both with the mask that I created in here I believe
[12:48] so mask and I just mixed both results as you can see in here
[12:58] then doing a naturoput blur let me just get rid of this visualization and this is our top part
[13:06] and is animated and we just merge it with everything else and this is the final result
[13:17] so from here we go into the valum simulation to create the valum fluid
[13:24] basically we start with this frame that we have here that I saved as a
[13:30] a prime group so I am deleting everything but that group those polygons then deleting all the
[13:40] small frames with a measure and a blast and creating the normals that we will be using for the
[13:50] the for the velocity from here we can do a small peak and extrusion and deleting the attributes
[14:05] and then do a time blend to create some sub frames or some floating how it's called fractional frames
[14:17] so we don't get stepping in our simulation at least is what I have noticed
[14:27] so in here I'm just creating some tubes to select from the valum fluid so I can give it a different
[14:38] color since I'm not going to do the UVs and in the valum fluid is simple you just put
[14:45] you just give it a really high viscosity we can introduce some surface tension and then you can
[14:54] change the particle size as you like in this case I used a relatively small value
[15:03] in here I'm creating just the color lines and transferring the normals as you can see
[15:11] and they look like this and they are animated as you can see
[15:22] or the geometry is animated then I'm creating a point velocity from the normals
[15:29] so we find our normed trails
[15:33] oops
[15:40] I've done something in here so if I turn on the trails as you can see
[15:51] is pointing in that direction and then I create a netribe to adjust factor to increase the
[16:02] the velocity a long time as you can see is changing the length
[16:11] and then I am introducing some randomization based on a sine wave
[16:19] so we get the liquid going left and right randomly
[16:25] so this is basically a sine wave implementation with amplitudes and frequency I can just change
[16:37] how much frequency I want and the amplitude to so this is our initial setup for the fluid
[16:48] then in here I am getting the collision shape of the top parts which is also animated
[16:58] and doing the volume solver in here I'm just increasing the sub steps and everything
[17:04] and the ground position which will be colliding with and everything is by default
[17:12] so if we check the final result we get this
[17:20] and we also have an ancient reboot and some lines that we can use in shading
[17:32] you tend to not being the greatest mask because I don't have enough points to have a smooth transition
[17:50] as you can see by the meshing I try to do some blurring and sharpening and it gets better but it's
[17:59] still a bit well you will have to increase the resolution of the sim and by the way this sim took
[18:09] on a potato computer like mine about 10 minutes so it's not that complicated and about 50
[18:18] megabytes of cache so really that is as simple as of course I'm doing the meshing so nothing
[18:30] fancy just passing the age and the color lines as a attribute and decreasing a bit the particle
[18:39] separation in comparison to the particle size in the valent fluids so always a good idea as you can
[18:52] see this is a bit messed up but then again so yeah that's basically the end of our network
[19:03] if I can show you again the final result and remove that ugly lines and see how it looks
[19:18] so as always you can grab the file on my patreon and you can also grab my procedural courses
[19:26] and many other perks there and I hope you enjoyed this one and again if you really want to
[19:34] create this for real I encourage you to check max patreon and support him thank you and I'll see you
[19:44] next time



---

## Captured Frames

- [0:50] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_000.jpg
- [2:30] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_001.jpg
- [4:30] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_002.jpg
- [6:20] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_003.jpg
- [7:20] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_004.jpg
- [10:30] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_005.jpg
- [15:00] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_006.jpg
- [17:20] tutorials/frames/kinefx-and-vellum-fluid-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
A homage/breakdown recreating a Reddit-viral "squeezed toothpaste tube" animation (originally by Max Vujje) entirely in Houdini: **Vellum cloth** to get two believable tube states (full vs. squeezed-empty) blended procedurally, a **KineFX line rig** capturing the tube via the fast-but-crude **Capture by Proximity** algorithm, a custom VEX "unrolling spiral" rig-wrangle animation to simulate the tube physically curling/uncurling as it's squeezed, a Point Deform + diagonal-rotation-matrix trick to keep the tube's cap/top piece correctly oriented as it follows the animated body, and a final **Vellum Fluid** sim (with sine-wave-randomized velocity and a shading trick using per-particle colored trail lines) for the extruded paste itself.

### Summary
The tube body starts as simple modeling (circle + rounded square merged and Poly Bridged, UVs computed early via bottom-point grouping for potential later texturing, capped and beveled). Rather than simulating the actual squeeze, the tube's two "poses" — a naturally-drooping filled state and a squeezed/emptied state — are each produced as separate **Vellum cloth sims** (with the polyfilled cap-patch group's edges Group-Expanded for extra bend stiffness, value 10 vs. 1 elsewhere) and simply **`lerp()`-blended between the two cached position sets** over a 1-48 frame animated fit range, since both share identical topology. That blended shape feeds a simple **KineFX line rig**: a Z-axis line Match-Sized and Resampled onto the tube (with a saved `curveu`/curve-view attribute), Rig Doctor-initialized, and captured via **Capture by Proximity** — chosen explicitly for speed over rigging accuracy ("not the best capturing system... just the fastest one"). To get the desired straighter, less-organically-rounded look for parts of the tube, a **Group by Range** isolates specific point intervals, and a custom rig wrangle (credited to community member "Swalch") computes a procedurally-animated **unrolling spiral**: an angle/offset drives a spiral shape, a Ramp gives positional control over the spiral's falloff, and a `fit()`-based time expression animates it from fully unrolled to nearly fully rolled — this spiral motion is applied via **Bone Deform** (rest position + this newly animated position as the two inputs) to physically simulate the tube curling as paste is squeezed out, followed by an Attribute Blur to soften self-intersection artifacts from the fast capture algorithm. For the cap/top piece (a separately-modeled static mesh — an extruded spiral shape positioned at the tube's opening) to correctly follow the tube's animation: the tube's cap-patch area is grouped, converted to points, and a **near-point + bounding-box-center** lookup finds the correct attachment point and its normal each frame; a **diagonal rotation matrix** (`dihedral()`-style, from base position/normal to the target reference point/normal) plus position offset (subtract-then-re-add center, the pattern reused across several videos in this batch) orients the static cap piece correctly; a **Point Deform** (rest state = first frame, target = the animated tube) then deforms the cap to follow — but produced an unwanted stretching artifact on a first attempt, fixed by blending two Point Deform results (one Attribute-Blurred first) together via a mask so the outer part of the cap doesn't over-stretch while the inner deforming part still follows correctly. Everything is merged for the final animated tube+cap. The **Vellum Fluid** paste itself starts from the previously-saved patch/cap primitive group (isolated via Blast, cleaned of small stray primitives via Measure + Blast), Peaked/Extruded slightly, then **Time Blend**-interpolated to add fractional in-between frames and avoid visible stepping in the sim. Vellum Fluid is configured with high viscosity, some surface tension, and a relatively small particle size; colored guide-tube lines (for later shading, since UVs weren't planned) transfer normals, and a **Point Velocity from Normals** wrangle drives emission direction, with an **Attribute Adjust Float** scaling velocity magnitude over time and a **sine-wave-based randomization** (tunable amplitude/frequency) added on top to make the extruded paste wiggle unpredictably left-right rather than emitting in a perfectly straight line. The animated cap geometry itself is used as the FLIP/Vellum collision shape, the ground plane provides the floor collision, and the Vellum Solver just needs increased substeps for stability. The final mesh is built by passing age and the colored guide-line attribute through as shading data, with particle separation reduced relative to particle size (called out as generally good practice for Vellum Fluid) — noted honest caveats: the mask driving mesh smoothing isn't perfectly smooth due to insufficient point density, and the whole sim took ~10 minutes / ~50MB cache on modest hardware, i.e. this is a comparatively cheap effect to attempt.

### Key Steps
1. **Base tube modeling:** Circle + rounded-Square, merge, **Poly Bridge**; center the shape; group bottom points → promote to edges → compute UVs (useful for later texturing); Polyfill the cap, Bevel hard edges, compute UVs on those parts too, add normals.
2. **Two Vellum cloth "poses":** using the polyfilled cap/patch group's edges (Group Expanded for extra stiffness — bend stiffness 10 on those edges vs. 1 elsewhere), run **two separate Vellum cloth sims**: one where the tube is simply dropped/settles naturally (partially full look), and one tuned via bend-stiffness values to represent the squeezed/emptied state.
3. **Blend the two cached states:** since both sims share identical topology, **`lerp()`** the position attribute between the two cached geometries, driven by a `fit()` of the current frame (1 to 48) into a 0-1 blend factor, for a procedurally-animated squeeze transition.
4. **KineFX rig setup:** build a Z-axis **Line**, Match Size it to the tube, Resample while saving a `curveu` attribute, transfer that curve data onto the tube, Rig Doctor to initialize the rig, then **Capture by Proximity** (fast but imprecise capture algorithm, chosen deliberately for speed) to bind the tube to the line rig.
5. **Isolate straighter sub-sections:** **Group by Range** selects specific point intervals along the rig line where a straighter (less uniformly rounded) look is wanted, rather than applying the same treatment everywhere.
6. **Custom unrolling-spiral rig wrangle:** (community-credited to "Swalch") build a procedurally animated spiral from an angle + offset, use a **Ramp** for positional control over the spiral's shape/falloff, and animate the unroll amount via a `fit()`-based time expression (fully unrolled → nearly fully rolled).
7. **Apply the spiral animation via Bone Deform:** feed the rig's rest position and the newly-animated spiral position into **Bone Deform** to physically curl/uncurl the tube body as it's squeezed; Attribute Blur afterward to soften self-intersection artifacts from the fast capture algorithm.
8. **Cache and clean up:** cache the animated tube, delete unneeded attributes (keep normals + UVs) and groups (keep only the patch group) to keep the cache lean.
9. **Cap/top attachment point:** group the tube's cap-patch area, convert to points, compute the **bounding-box center** of that group, then use **Near Point** from that center position to find and select the specific attachment point (with normals added, critical for orientation).
10. **Orient the static cap piece:** compute a **diagonal/rotation matrix** (`dihedral()`-style) transforming from the cap piece's base position/normal to the target reference point/normal (found in step 9), then apply position (subtract-then-re-add center) and the rotation — the same base/target-normal orientation pattern reused across multiple videos in this batch.
11. **Deform the cap to follow the tube:** **Point Deform**, rest state = first frame of the cap geometry, target = the animated tube — produces an initial stretching artifact on the outer, less-deforming part of the cap.
12. **Fix the stretch artifact via masked blend:** run a second Point Deform pass through an **Attribute Blur** first, then blend the blurred and unblurred results together using a mask so the outer cap stays stable while the inner region still follows the tube's deformation correctly; final Attribute Blur, then merge cap + tube for the complete animated asset.
13. **Fluid source prep:** Blast down to the previously-saved cap/patch primitive group, clean up small stray primitives (Measure + Blast by size threshold), Peak/Extrude slightly, delete unneeded attributes, then **Time Blend** to add fractional sub-frames and avoid visible stepping artifacts in the simulation.
14. **Vellum Fluid configuration:** high viscosity, some surface tension enabled, relatively small particle size; separately build colored guide-tube "trail" lines (for shading, since no UVs are planned for the fluid) transferring normals from the source geometry.
15. **Velocity + randomization:** **Point Velocity from Normals** for base emission direction; **Attribute Adjust Float** scales velocity magnitude over time; layer a **sine-wave-based randomization** (tunable amplitude and frequency) on top so the extruded paste wanders left-right unpredictably instead of emitting perfectly straight.
16. **Collisions and solve:** use the animated cap geometry as the collision shape (since it's also animated, matching the squeeze motion) plus a ground plane; increase Vellum Solver substeps for stability; everything else left at default.
17. **Meshing + shading data:** mesh the resulting Vellum Fluid particles, passing through **age** and the **colored guide-line attribute** as shading data; reduce particle separation relative to particle size (called out as generally good Vellum Fluid practice) for cleaner mesh results; note the resulting mask/mesh smoothing isn't perfectly smooth due to insufficient point density in this pass, requiring more resolution to fully fix.

### Houdini Nodes / VEX / Settings
Modeling: Circle, Square (rounded), Merge, Poly Bridge, Group (bottom points), Group Promote, UV compute, Polyfill, Bevel, Normal. Vellum: Vellum Cloth Solver (x2 poses, Group Expand for bend-stiffness edges, bend stiffness values), Attribute Wrangle (VEX: `lerp()` position blend driven by `fit(frame, 1, 48, 0, 1)`). KineFX: Line, Match Size, Resample (curveu save), Rig Doctor, Capture by Proximity, Group by Range, Rig Wrangle (VEX: spiral angle/offset construction, Ramp-driven falloff, `fit()`-based unroll animation), Bone Deform, Attribute Blur. Cap orientation: Group, Convert to Points, Group Point Bounding Box Center, Near Point, Normal, Attribute Wrangle (VEX: `dihedral()`-style rotation matrix from base to target normal, center subtract/re-add position pattern), Point Deform (x2, one blurred), mask-driven Blend. Fluid: Blast, Measure (size-threshold cleanup), Peak, Extrude, Time Blend (fractional sub-frames), Vellum Fluid (Configure Fluid: viscosity, surface tension, particle size, particle separation), Point Velocity from Normals, Attribute Adjust Float (velocity scale over time), Attribute Wrangle (VEX: sine-wave randomization, amplitude/frequency), Vellum Solver (substeps, collision geometry from animated cap + ground), mesh (age + color-line attribute pass-through).

### Difficulty
Expert — combines KineFX rigging, a hand-built VEX spiral-unroll animation, dihedral-rotation-based orientation for a deforming attached piece, and a full Vellum Fluid sim with custom velocity randomization; assumes strong VEX, rigging, and simulation fundamentals.

### Houdini Version
20.5 (KineFX/Vellum Fluid workflow consistent with Houdini 20.5-era tools; credits Max Vujje's original Reddit-viral simulation as inspiration).

### Tags
#kinefx #rigging #vellum #simulation #vex #procedural #animation #advanced

---

## Related Tutorials
Cross-link with chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson.md (same author, overlapping Vellum-fluid + rig-driven-squeeze technique) and any other cgside KineFX rigging tutorials once indexed together — shares the dihedral-rotation orientation pattern with houdini-tips-to-save-the-day.md and hard-surface-techniques-in-houdini.md.
