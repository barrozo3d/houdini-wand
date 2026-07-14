---
title: Houdini techniques to improve your level
source: YouTube
url: https://www.youtube.com/watch?v=zWlJ8QLkFH4
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, flip, simulation, uv, python, procedural, tips, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-techniques-to-improve-your-level/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini techniques to improve your level

**Source:** [YouTube](https://www.youtube.com/watch?v=zWlJ8QLkFH4)
**Author:** cgside
**Duration:** 14m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'm going to share yet another set of tips and tricks in Odini, maybe diving a bit deeper on some projects, but yeah you should get away with some new techniques.
[0:12] So the first project I wanted to share with you was this kind of drip effect using Flip. I tried with PopFluid but didn't get a good result so why used Flip instead.
[0:23] So let's have a look on how to set up this. So I first modeled the bottle of course, but that's not important. The important thing is where we set up the flip.
[0:34] So starting with the main body of the bottle, then I'm going to clip a little bit to create my emitter.
[0:42] So just clip like this, then I'm going to thicken this just slightly to create a thin layer of points, which I'm doing with the flip source.
[0:52] Here I'm just adding the surface because I don't want to see the VDB or the SDF and here I have a thin layer of particles.
[1:02] Then in this wrangle that we will come back in a bit, I'm just setting the velocity of each drip and the position of each drip.
[1:13] So and for that I'm first from these clip parts, I'm converting to line the clip edges and then scattering a few points.
[1:22] Maybe change these two points and as you can see I'm scattering a few points in this case just nine playing with the seed with over a lacs iteration and we get this distribution.
[1:31] Then I am sampling those positions to get the dripping positions.
[1:36] And for that, let's ignore this density. I'm just doing a pacifying or you can do with near points.
[1:42] So I'm reading from the first input the position and I'm using the current position plus some noise as you can see these positions are a bit distorted because I pre-confer to the noise vector and played with the amplitude and so on.
[1:54] So sampling from the current position and some noise which is a set to 0.1 not too much and then around the radius that I defined so I can increase it or decrease it and just getting one point.
[2:07] Then I'm computing a mask so just the length of this of the points found if that is bigger to one that will create as a mask so that mask equals to mask I can show you how that looks.
[2:20] Let's have a look that just creates a zero one mask of where those points live where that radio sleeps that sampling so we don't need this and then I'm just computing a random value for each drip so I can affect the velocity so they don't fall at the same time.
[2:36] In this case I'm not going to affect velocity I'm going to affect gravity so they fall one goes more slow the other one goes faster and so on.
[2:45] So I'm just computing a random value playing with a seed I can change the seed and then I want to make sure that they have at least 0.2 so I don't get values closer to zero close to zero.
[2:57] I mean then just multiply it by the mask to mask out only these parts so I want zero here and some random values around the shape then inflate so let me just run the simulation quickly so I can show you something.
[3:16] So as you can see this is my simulation and you notice that we have a very well distributed point cloud as you can see and that is achieved by not as you can see I'm not using any collisions any collider I mean static object because I'm doing that within a volume collision in this wrangle and I'm also applying the particle separation so I have this uniform distribution.
[3:41] And so let's have a look on how I'm achieving the collision because in here I am loading an SDF in the second input that we can have a look it's basically the bottle SDF I'm not going to have a look at it I lost the cash but basically before I cash again so this is the SDF of the bottle body and let me cash this again.
[4:03] So here we are and as you can see we have the steam layer of particles that was my goal in the end and to create those drips of course so let's have a look again I'm loading the SDF that I showed you in the second inputs and that's the SDF I'm sampling so sampling the bottle SDF to create the collisions.
[4:25] Then in order to move the point that otherwise would be just falling down randomly or with gravity I am computing the gradient the gradient is like the normal soft that SDF that bottle body so I'm computing the gradient from the first input or the second input in this case and then just normalize it.
[4:44] Then let's ignore this part in order to move the points to the SDF surface we just started the current position of the points move it along the gradient and snap it to the surface which is just grad multiplied by the SDF in this case we invert the sign because values inside the SDF are negative so you usually want to invert the sign in here.
[5:06] Then the other thing I'm doing if I show you in here I'm creating not I'm not just snapping to the surface I want to create some thickness as you can see in here and in order to achieve that I'm creating a in your thickness slider that I can change and fitting the random value between the surface which at the surface which is 0.0 and an outer edge let's say that I'm calling the thickness which is 0.0.3.
[5:35] So the points will start at the surface and then move a bit out and then in here I'm just making sure that I take into consideration that then I'm just having so much rewards that I'm not going to even use but yeah that's basically the effect of snapping the points to the surface.
[5:52] Then in the force it's simple I create a gravity and just place the gravity values not using a gravity node as you can see because it doesn't allow for custom custom wax expressions and also you can place it in here you just have to place it after to play flips over but it's basically force with these values so I'm creating gravity and then using that value I want to make sure my value is over one so if you remember the previous values we had on the
[6:21] on the initial points on the source so I'm targeting the values that have some that are not zero for that I just multiply the gravity with the current value which is that random value we set otherwise if it's zero value we just multiply it by a small value the gravity by a small value so it doesn't move so quickly as you can see this parts in here that have no value for the drips won't move so quickly.
[6:47] Then you can find on this and create another another rules if you want then I'm also I noticed that if I set a variable viscosity between the same boundaries I can get a nicer dripping effect so I'm just doing some variable viscosity between a value of 35 and 6 and just slow down everything with some resistance this is the same of.
[7:12] Of how is it called of up drag yeah that's basically it's then in here as I told you I'm applying some particle separation I have receiving on making sure I have enough sub steps and as I did an h particles that might come in and the
[7:31] and in volume motion I'm also enabling some surface tension and don't forget viscosity by attribute we need to enable viscosity and set viscosity by attribute so that's basically I'm achieving that clean look of the trips then it comes the meshing and some re timing but you can have a look at that so on the file that I'm going to share on patron but basically I'm just rounding off with some small operations and some dilation and we get this sort of results so basically this.
[8:01] Just build up at the beginning and then slow down at the end and mesh the particles so yeah that's basically it for this project so in the last year I modeled this truck but in the end I didn't do the UVs I just set up some triplanar shading and to do to do the trick but since I want to properly texture it I started to go over the file which is a bit of a mess and UV each part separately and today I want to share how I texture this tire which might look simple but poses a few challenges.
[8:31] So let me have a look in here so basically I start with this mesh so let me have a look not this solid, let's have a look here so I basically started with this mesh and then did the detailing inside but let's have a look instead of the UVs and I'm going to share this part of the model in the patron file so you can follow along how I did all of this.
[8:56] So let's do these UVs which will look something like this let's do this live so with the what sort of a UV flat anode and let's connect it and by default this will look something like this I want to disable manual layouts to compute the layout automatically.
[9:14] I'm going to enter the tool and let me just change in here and first of all we will be in cuts or see what seems so seems so I'm going to pick the middle one shift A and middle click to cut in here so it's not right in the middle but it will do then I'm going to cut in here and you will see a problem that this will create so if I try now to rectify this you can see that it wants to make a difference.
[9:44] It won't rectify it even if I try to do angle base which will be a bit better but still won't rectify as you can see and the reason is that we have some some of these edges in here and the same happens in other UV based programs like RISM UV I had the same problem and I find the solution which is basically to
[10:13] give out any some help which means we go again to the tool and we look for align vertices in you or V direction so let's click that and let's shift A and let's let's try to select first these ones.
[10:31] So let me select this one and presenter and this will align it along and you can come in here and set it to you or V or you can also shift click on the line groups to toggle between your V alignment.
[10:47] Now I can select this, shift, middle click and presenter and now we can select this one in here, presenter and the same for the other side.
[11:04] So let's go a bit closer so this will want me to select that edge.
[11:11] Let's try like this and like this.
[11:20] And there you go now we have rectified everything without rectifying just by setting some constraints on the UV mesh and if we look at the UVs they now look perfectly aligned.
[11:32] And that's basically how I went about UVing all of these so as you can see I have a lot of straight rectified groups and that's basically how I did it.
[11:46] So as the final tip I wanted to share how I improved the texture projection tool to basically increase by a lot its performance as you can see I have this projection in here and it's moving pretty fast because we have a low poly mesh.
[12:05] And if I increase these let's say to four so we get about almost one million points and if I drag as you can see the performance is still there.
[12:16] I just need to move it grab it and if I move it everything should work just fine. But in the previous version which I have a demo in here that I'm going to share on Patreon if we try to move this projection as you can see it's still pretty slow.
[12:35] So how did I improve this so basically before I was drawing a point on the mesh and then sampling its normals the normals of the mesh and that UV sample I tried with near point I tried with XYZD I tried with PC find and all gave about the same performance as you sample.
[12:57] So what I did in the end since since I'm doing the intersection on on Python so if I go to edit this viewer state module and if I look in here to the intersector so since I'm using an intersection already I can sample the not only the position to where I place the point I can use it also to sample the normal by doing self.geo intersector.normal
[13:25] which is another attribute that the intersect function in Python gives us or the geometry intersection so that way I can feed that normal to parameter that I'm doing in here somewhere so self.normal in here so I'm I have an even an even parameter in here that has the normal that I'm sampling for each point that way I can make the tool go fast because I don't need to do that you'll be sample.
[13:54] And if we look inside as you can see where I was sampling the normals I'm just copying an attribute and no longer sampling the normals so I'm going to share this setup that basically mimics the texture projection tool and strips down the core parts and also all everything that is happening on cops so yeah you can have a look and explore on your own and if you want to get the updated version you can do so on my Patreon it's a free upgrade.
[14:24] So yeah guys that's basically what I wanted to share today hopefully you'll got away with some new techniques and let me know if you enjoyed this video see you next time.



---

## Captured Frames

- [0:45] tutorials/frames/houdini-techniques-to-improve-your-level/frame_000.jpg
- [1:35] tutorials/frames/houdini-techniques-to-improve-your-level/frame_001.jpg
- [3:10] tutorials/frames/houdini-techniques-to-improve-your-level/frame_002.jpg
- [4:10] tutorials/frames/houdini-techniques-to-improve-your-level/frame_003.jpg
- [7:40] tutorials/frames/houdini-techniques-to-improve-your-level/frame_004.jpg
- [9:00] tutorials/frames/houdini-techniques-to-improve-your-level/frame_005.jpg
- [10:30] tutorials/frames/houdini-techniques-to-improve-your-level/frame_006.jpg
- [12:10] tutorials/frames/houdini-techniques-to-improve-your-level/frame_007.jpg

---

## Structured Notes

### Core Technique
Three deep-dive techniques: a **FLIP-based bottle-drip simulation** using a thin-layer particle source, VEX-driven per-drip randomized gravity/mask (instead of POP Fluid, which gave poor results), an SDF-gradient point-snapping trick to hug a collider surface with controllable thickness, a UV-rectification fix for stubborn non-rectifiable seams via **Align Vertices in U or V**, and a Python **texture-projection tool speedup** by reusing the intersector's own normal sample instead of a separate UV-sample lookup.

### Summary
For the drip effect: the bottle body is Clipped to carve out an emitter region, **Thickened** slightly to create a thin shell of source points (with only the surface enabled on FLIP Source, not the VDB/SDF), and a wrangle sets each drip's initial velocity/position. Drip origin points are generated by converting the clip boundary edges to a line and Scattering a handful of points (~9, tuned via seed and relax iterations); a **`pcfind()`/near-points** query (position sampled from the source plus a small noise offset for organic distortion) locates the nearest scattered point within a defined radius, and the found-point count becomes a 0/1 **mask** marking which particles belong to an active drip stream. A per-drip random value (seeded, floored at a minimum ~0.2 to avoid near-zero values, multiplied by the mask so non-drip particles get zero) is later used to scale **gravity** per-drip (not velocity) so different drips fall at different rates — producing a naturally uneven, staggered drip pattern instead of gravity node's uniform pull (since the stock Gravity node doesn't support custom VEX expressions, gravity is instead built manually as a Force with VEX-driven values, placed after the FLIP Solver). Collision against the bottle uses no actual collider object at all: an **SDF of the bottle body** is loaded into a wrangle's second input and sampled directly; the **gradient of that SDF** (its "normal," essentially) is computed and normalized, then each particle's position is moved along that gradient by the (sign-inverted, since SDF interior values are negative) SDF value to snap it exactly onto the surface — with an added **thickness** parameter that fits the snap position between the surface (0.0) and a small outer offset (~0.03) so particles sit just outside the surface rather than exactly on it. Simulation quality comes from **particle separation** enforced within the same custom wrangle (eliminating the need for a real collision object while still getting an evenly-distributed point cloud), plus tuned substeps, variable **viscosity** (~35 to a low value, acting like a drag/resistance force) enabled via "Viscosity by Attribute," and surface tension in Volume Motion — together producing drips that build up initially then slow into a clean trailing shape, finished with standard meshing/dilation and a bit of retiming. For the truck-tire UVing: after a basic UV Flatten with manual layout disabled, cutting seams at obvious edges sometimes leaves geometry that **refuses to Rectify** (even with angle-based rectify) due to certain edge configurations — the fix is the **Align Vertices in U or V** tool (found in the same Tool menu), selected per-edge-loop (Shift-click to toggle between U/V alignment) to explicitly constrain vertices into straight rows/columns before flattening, which then rectifies perfectly without ever needing the Rectify operation itself. Finally, the author's custom **texture projection tool** (a Python viewer-state tool) was slow to drag/move once mesh density got high (~1M points) because it sampled the mesh's UV attribute via a separate lookup (tried Near Point, XYZ Distance, and `pcfind()` — all similarly slow) after placing the projected point via an intersection; the fix was realizing the same **Python intersection call already used to place the point can also return the surface normal directly** (`self.geo_intersector.normal`), eliminating the need for any separate UV-sample/normal-lookup call and dramatically speeding up the tool even at high mesh resolution.

### Key Steps
1. **FLIP emitter setup:** Clip the bottle body to define an emitter region, **Thicken** slightly to create a thin shell of source points, configure **FLIP Source** to output only the surface (not VDB/SDF).
2. **Drip origin points:** Convert the clip's boundary edges to a Line, **Scatter** a small number of points (~9, tuned seed/relax iterations) to define individual drip-stream locations.
3. **Drip-mask sampling (VEX):** in a wrangle, use **`pcfind()`**/near-points to locate the nearest scattered drip-origin point to each source particle's position (offset by a small noise vector, ~0.1 amplitude, for organic variation) within a tunable radius; the found-point count becomes a 0/1 mask flagging which particles belong to an active drip.
4. **Per-drip random gravity scale:** compute a seeded random value per drip (floored at ~0.2 minimum to avoid near-zero, multiplied by the drip mask so non-drip particles get 0), later used to scale gravity strength per-drip for staggered fall timing.
5. **Custom gravity via Force (not Gravity node):** since the stock Gravity DOP doesn't accept custom VEX expressions, build gravity manually as a **Force** node placed after the FLIP Solver, using the per-drip random value to scale magnitude — drip particles with a non-zero mask value fall at varied custom rates; zero-mask particles move minimally.
6. **SDF-based collision without a collider object:** load an **SDF of the bottle body** into a wrangle's second input; compute the **gradient** of that SDF (normalize it) as a pseudo-normal, then move each particle along that gradient by the (sign-inverted) SDF value to snap it exactly onto the surface.
7. **Controllable surface thickness:** add a `thickness` parameter and fit the snap distance between the surface (0.0) and a small outer offset (e.g. 0.03) so particles rest just outside the true surface rather than exactly on it.
8. **Particle separation for even distribution:** enforce particle separation directly inside the same custom wrangle (rather than via a real collider), producing a well-distributed point cloud without any actual collision geometry.
9. **Sim tuning:** variable **viscosity** between two values (e.g. ~35 down to a low value) enabled via "Viscosity by Attribute" (acts like drag/resistance, slowing the drip flow), surface tension enabled in Volume Motion, tuned substep count, standard meshing + dilation + light retiming for the final clean drip look.
10. **UV flatten + seam cutting:** run **UV Flatten** with manual layout disabled (auto layout), enter the UV tool, cut seams at chosen edges (Shift+A then middle-click to cut).
11. **Diagnose non-rectifiable UVs:** attempting **Rectify** (even angle-based) on certain cut shapes fails to produce a clean rectangular result due to specific edge configurations — a problem also observed in other UV tools like RizomUV.
12. **Fix via Align Vertices in U or V:** in the same Tool menu, use **Align Vertices in U or V**, select an edge loop (Shift+A, then Enter to align), toggle between U/V alignment via Shift-click on the loop, and repeat per edge group — constraining vertices into straight rows/columns manually so the shape naturally comes out perfectly aligned without ever running Rectify.
13. **Diagnose slow texture-projection tool:** the custom Python viewer-state projection tool became sluggish at high mesh density (~1M points after subdividing) because, after placing a point via mesh intersection, it performed a **separate UV-sample lookup** for the surface normal (tried Near Point, XYZ Distance, `pcfind()` — all similarly slow).
14. **Speed fix via reusing the intersector:** since the tool already calls a Python geometry **intersection** to place the projected point, that same intersection object can return the surface normal directly via **`self.geo_intersector.normal`** — eliminating the separate normal/UV-sample lookup entirely and restoring fast interactive performance even on dense meshes.

### Houdini Nodes / VEX / Settings
FLIP/DOP: Clip, Thicken, FLIP Source (surface-only output), Convert Line, Scatter, Attribute Wrangle (VEX: `pcfind()`/near-points drip-mask sampling with noise-offset position query, seeded random-value generation with a floor, SDF gradient computation + `normalize()`, sign-inverted SDF-based position snapping, thickness-based `fit()` offset, particle-separation enforcement), Force (custom VEX-driven gravity, placed post-FLIP-Solver since the stock Gravity node rejects custom expressions), FLIP Solver (Viscosity by Attribute, variable viscosity range, surface tension in Volume Motion, substep tuning), meshing + Dilate + retime. SOPs (UV): UV Flatten (manual layout disabled), UV seam-cut tool, Rectify (angle-based, noted as failing on certain edge configurations), Align Vertices in U or V (per-edge-loop selection, U/V toggle via Shift-click). Python (texture-projection viewer-state tool): geometry intersection call (`self.geo_intersector`), `.normal` attribute reuse to avoid a separate UV/normal-sample lookup.

### Difficulty
Advanced/Expert — combines custom VEX-driven FLIP forces/collision (no collider object, SDF-gradient snapping), a non-obvious UV-rectification workaround, and Python viewer-state tool optimization; assumes strong VEX, FLIP, and Python/HDK familiarity.

### Houdini Version
20.5 (UI matches Houdini 20.5-era FLIP/UV toolset).

### Tags
#vex #flip #simulation #uv #python #procedural #tips #advanced

---

## Related Tutorials
Cross-link with essential-procedural-techniques-in-houdini.md (same author, shares the OpenCL/VEX force-application philosophy for simulation dive targets) once indexed together.
