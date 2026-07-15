---
title: Gestation Effect in Houdini. Scene Breakdown.
source: YouTube
url: https://www.youtube.com/watch?v=JiQyPj-rLII
author: Pixel In The Frame
ingested: 2026-07-15
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/gestation-effect-in-houdini-scene-breakdown/
frame_count: 0
frame_status: pending-selection
---

# Gestation Effect in Houdini. Scene Breakdown.

**Source:** [YouTube](https://www.youtube.com/watch?v=JiQyPj-rLII)
**Author:** Pixel In The Frame
**Duration:** 14m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py gestation-effect-in-houdini-scene-breakdown <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video I will key through the Goudini scene file and breakdown the process I used
[0:04] to create the gestation effect.
[0:06] In the beginning I tried couple methods, do animation with Vex, in sub-solver as well
[0:11] particle simulations, but best way to achieve organic look is to use Vellum solver and Varanoid
[0:17] fracture.
[0:18] Let's check the setup.
[0:19] I started with a sphere, created Vellum, configure Balloon node to set constraints and output
[0:25] pressure group.
[0:28] It's a lot later to control reslinks value from top network with Vellum constraint properties
[0:33] node.
[0:34] I won't go into details of this part of the setup because I follow team one healthy
[0:39] and tutorial about cells pleading with Vellum solver and if you're interested you can
[0:43] go and check original video.
[0:45] It's a nice guide.
[0:46] I did couple adjustments though, I used groups and split nodes to separate preserved cells
[0:52] from dividing one, it gives more stable result.
[0:55] Another thing I added, cell id primitive attribute to be able later to basic copy operations
[1:01] and use it for seed calculation and so on, after importing from dope to solve level,
[1:06] they can check Vellosity attribute.
[1:08] Later I will use it as initial Vellosity for small simulations to maintain the originality
[1:13] of cell motion due to division process.
[1:17] Scale it down a bit.
[1:20] After that clean up attributes, keep Vellosity and some primitive attribute.
[1:25] Here you can see and cell id.
[1:28] Let me visualize it.
[1:29] Let's create color node, set random from attribute and choose cell id class primitive.
[1:47] Let me dive into log network to find first layer of effect.
[1:54] Alright, inner cell part.
[2:01] Here I added boolean node with union operation to not have overlapping in case of an intersection,
[2:07] calculated normals and applying transform to get better loop from camera view.
[2:12] After I will reference this node for all other parts of the setup.
[2:23] Next layer is connection lines between core and outer shell, but I'll talk about it later.
[2:28] Now let's check core part itself.
[2:30] This object merge fetching cell central points, I generated them in the forage loop using
[2:36] cell id to separate every cell independently.
[2:39] After that extracting centroid and copying cell id to generate center point.
[2:48] Inside soapsolver I create in life attribute, basically it's one frame incremental.
[2:54] Setting p-scale and parent id, copying spheres to points, and transferring velocity attribute
[3:04] generated in point velocity node with central different approximation.
[3:12] Creating class attribute and inside for a loop added noise to points position.
[3:19] I'm using a flow noise, absolute value to avoid negative numbers, feed range, clamp values
[3:26] and feed to displacement.
[3:30] To get animation I feed time to flow parameter and control speed with multiply by constant
[3:35] node.
[3:41] Precalculating velocities, converting it to VDB and adding pirate source node to scatter
[3:47] points with density attribute inside sdf.
[3:51] Increase a lot density value, transferring velocities and normalizing it.
[3:59] Next volume rasterize from attributes for density and velocity and finally pirate
[4:05] solver.
[4:07] Nothing special here, in fact I do not use temperature so I can disable it from sourcing as well as
[4:13] flame field.
[4:17] I have pretty high dissipation because I do not need smoke stay too long.
[4:21] In shape tab I'm using disturbance and turbulence with density as control field and small
[4:29] amount of viscosity.
[4:31] Exporting density and velocity fields, converting them into VDB and using 16-bit float as well
[4:37] resembling velocity field.
[4:39] Caching it.
[4:44] Let's display cell itself, so now you can see core smoke stays inside of the cell.
[4:52] Here I'm splitting density and velocity fields, density I'll render a smoke inside core geometry.
[4:58] Here I clamp density value, I want to keep only high density area.
[5:04] And reference and final orientation of effect.
[5:11] In this part I'm doing core geometry.
[5:13] Again, clipping low density values, scattering points inside and running particle simulation.
[5:25] Inside popnet I add vectors particles by volume, as speaking about particles at the
[5:29] action topic and introduction to Goudini particles course you can check it on my channel.
[5:35] Ritting velocities from pirate simulation.
[5:39] Using pop kill to delete zero speed particles.
[5:44] Recalculating velocities by ID.
[5:48] And doing particles trail with sound sub steps and frame duration too.
[5:54] Using scale alone length option.
[5:57] Using weeds attribute as p scale.
[6:00] And creating VDB from particles.
[6:07] Now let's take a look at second branch.
[6:10] Again, prune low density area.
[6:14] Converting to sdf, resample it.
[6:16] But I think resample VDB node is some legacy, not think, so you can skip it.
[6:22] Sdf, resample points from volume and using density as p scale attribute.
[6:27] Modifying p scale values.
[6:30] Converting it to sdf volume.
[6:33] And smoothing VDB.
[6:36] After caching I create in single volume with sdf union operation and float on all b into
[6:41] first a option.
[6:44] Since later I want to offset level set values with a noise.
[6:47] I need to expand voxels with VDB activate node and calculate closest point.
[6:59] After offsetting values, I deactivate in unnecessary voxels.
[7:02] Keeping only surface field.
[7:05] Finally converting to polygon mesh.
[7:09] Caching it and assigning velocities from velocity volume.
[7:17] Find reference transformation.
[7:24] Next part is small particles around core.
[7:26] I am taking points what we used for small commeter.
[7:33] And killing all low speed particles.
[7:42] Next creating smoke volume emitter.
[7:48] Pire solver setting almost the same.
[7:51] Disappation is lower here.
[7:52] That's the main difference.
[7:59] Disturbance through blends with the velocity staying the same.
[8:04] One thing I forgot to mention that for both pire solver nodes I added inside static object
[8:09] node for cell geometry collisions.
[8:11] This inverted sign to collide inside geometry.
[8:14] Collision volume itself here I created VDB from polygons called field collision and checked
[8:19] field interior.
[8:25] That's how looks simulation.
[8:32] After caching again through low dense areas.
[8:35] Caching volume these points and fitting it into popnet.
[8:40] Similar setting this first popnet.
[8:42] Just here I added pop kill and for cell geometry as well.
[8:45] In case if any particles will leave its boundaries.
[8:49] Addression counts from second pire simulation.
[9:03] Caching p scale with curve based on normalized h.
[9:06] Applying transformation and calculating velocities by id.
[9:12] Now I can speak about connections between core and cell surface.
[9:20] As an input I take in center spheres and outer cell geometry.
[9:25] Let's set ghost inflect to keep it visible.
[9:29] Center spheres we used as input for small committer.
[9:33] Putting them in different groups to be able split them later and promoting cell id from
[9:38] point to primitive back.
[9:40] Because I will need to use this attribute for forage loop.
[9:46] Inside of forage I split in geometries, calculating normals for center sphere and scattering
[9:51] few points on its surface.
[9:53] I use spare input to fetch metadata and use iteration detail attribute in expression
[9:59] for seed.
[10:00] Next creating name id, projecting point to outer surface with ray node, projection based
[10:05] on normal direction.
[10:09] Creating polylines between points with add node.
[10:13] Then I iterate in on every polyline, duplicating each four times but you can do how many want.
[10:21] I slightly shift position for every of it.
[10:35] And recreating name id.
[10:39] Re-sample it to add more resolution to polylines.
[10:41] Don't forget check your few attribute in re-sample node.
[10:46] Add attribute warp, add in some flow noise to position, controlled by ramp and in the
[10:51] end smooth it.
[10:57] After forage loop I apply an animation based on cure view, animating grows forward and
[11:02] backward.
[11:05] Add in pull the wire to have a shell and use clean soap to remove degenerative primitives.
[11:11] And finally reference in transformation.
[11:16] Here is outer cell part.
[11:21] Doing polygstrude to get shell.
[11:32] Convert into sdf, performs smooth separation, calculating closest point with vdb analysis.
[11:41] Unplug volumes, smooth it again and apply small noise.
[11:51] Simple a flow noise.
[11:55] Delayed sdf, another level of noise with absolute values, objective 8 voxels and blast
[12:04] extra fields.
[12:06] I would like to blend between sdfs during time, so I use in blend shapes node and animating
[12:13] mixed parameter.
[12:22] Re-sample vdb and converting to polygons.
[12:25] Smooth in the end.
[12:26] For shading later I use in one more vdb analysis node, calculating curvature inside and create
[12:32] point attribute from it with attribute from volume node.
[12:39] Applying reference transformation.
[12:42] The last part is overall atmo, simple box converted into constant fork, only I subtract volume
[12:49] of cells from it.
[12:57] For lights I have dome light with studio HDR, top strong light and 3-quarter weak light.
[13:05] For both inner and outer cell surface, I'm using Fresnel to control opacity of it.
[13:14] Connections has transmission shader, body has transmission and sub surface shader with
[13:22] opacity set 2.6.
[13:34] Small particles is subtlayer.
[13:43] Next outer surface, again opacity here controlled by Fresnel.
[13:52] body smoke layer needed to absorb some light for the core.
[13:59] Smoke inside cell, just basically some volume with noise.
[14:06] And last thing is general atmo.
[14:11] That's it, hope you enjoyed.



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
