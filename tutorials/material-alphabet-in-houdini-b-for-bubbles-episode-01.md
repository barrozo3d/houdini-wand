---
title: Material alphabet in Houdini: B for Bubbles | Episode 01
source: YouTube
url: https://www.youtube.com/watch?v=uYQGsriGNm4
author: Kotov Roman
ingested: 2026-08-06
houdini_version: "Not specified"
tags: [sop, vop, volumes, particles, procedural, attributes, modelling, advanced]
extraction_status: complete
frames_dir: tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Material alphabet in Houdini: B for Bubbles | Episode 01

**Source:** [YouTube](https://www.youtube.com/watch?v=uYQGsriGNm4)
**Author:** Kotov Roman
**Duration:** 11m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey, I'm Kotov. This is B4Bubbles, the next chapter in Material Alphabet and Houdini series.
[0:06] In this episode, we're building a liquid with bubbles inside, completely without simulation.
[0:11] Instead of relying on dynamics, we'll use procedural geometry to get a total control over the placement and movement.
[0:18] Throughout the process, we'll move back and forth between geometry and rendering as we develop the look.
[0:23] And let's get to it.
[0:25] Let's start by creating a geo-container, calling it setup and coloring it red.
[0:29] I will also change the background to the gray.
[0:32] As usual, we will need some geometry to work with. Let's drop down font node and type in B.
[0:37] Maybe I will also change the font to anything else, really.
[0:44] This one should work nicely for the bubbles setup, but we will need some thickness.
[0:48] Learning from my mistakes, I will not be using bevel node and instead jump right into VDB from Polygons.
[0:54] And before we go into simulation, it's probably a good idea to change our FPS settings.
[0:59] Bubbles should be smoother than that. Let's add VDB smooth node and crank it up a lot.
[1:05] This shape already resembles liquid. Now let's think on how we can make it appear.
[1:10] I will be using Mop's shape falloff for that.
[1:13] This falloff will drive most of the look. It will do displacement, appearance of the liquid and movement of the bubbles inside.
[1:19] Because it's just 0 to 1 gradient, it's really easy to work with inside the point valve.
[1:24] To make animation look more interesting, let's add displacement first.
[1:28] I will be using displacement along normal's node.
[1:31] To add some visual interest to it, I will also add some noise in there.
[1:39] Now let's bring in our Mop's falloff attribute.
[1:45] I will add a ramp to it to make it easier to work with.
[1:50] The configuration of the displacement along normal's node is really easy.
[1:55] Only do you plug in position into position and Mop's falloff into the mount.
[1:59] Scale will determine how much of the displacement we have.
[2:02] And because we have added ramp to the Mop's falloff, we can shame the displacement.
[2:06] Now let's add some noise to it by multiplying Mop's falloff with the noise.
[2:10] Let's see what kind of displacement we can dial in with this setup.
[2:19] Now that we have that, let's tackle in appearance of the shape.
[2:23] For that, I will be using points from volume node.
[2:26] We can do a full link copy of the node by holding down Ctrl Alt Shift and dragging that node.
[2:31] Let's do that for our Mop's shape falloff.
[2:36] You can see falloff going from 0 to 1.
[2:39] The idea is that we will multiply pscale with it.
[2:42] So when we use VDP from particles later, points with 0 pscale will just disappear.
[2:47] We can visualize that by tackling this instead of points in our viewport.
[2:53] Now we are ready to use VDP from particles.
[2:56] I've set pscale to a very small value.
[2:58] I will increase that so VDP from particles can pick it up.
[3:05] I will also make further adjustment to the displacement.
[3:09] It's time to convert VDP back to polygons, but I will add VDP smooth in between.
[3:14] That's a start, but it cuts off way too smoothly.
[3:17] I want to break it up with the noise.
[3:19] Luckily, Mop's shape falloff makes it easy to add the noise.
[3:22] Let's set it up.
[3:24] I am looking for a really smooth and fluid noise pattern.
[3:30] Hopefully you can see the vision now.
[3:33] Let's animate that falloff.
[3:35] Going from down to up.
[3:43] Now we are ready to cache that stage.
[3:45] Let's drop down File Cache Note and choose our folder.
[3:48] Now that I can see that in motion, I would like to make some small adjustments.
[3:52] First, I will increase displacement amount.
[3:54] And second, I will change the noise pattern.
[4:06] I will also check if I can find some better options in VDP smooth.
[4:24] Let's cache that iteration as well.
[4:27] I like the first one more, but it's still not what I am looking for.
[4:32] I will revert some of the changes back.
[4:43] That looks good.
[4:45] Now let's work on the bubbles inside.
[4:47] Because we already have the points inside our shape, we can use them for the bubbles.
[4:51] We have to delete most of them and leave only a few.
[4:54] I was trying to use Vax for that step, but for some reason it just didn't work.
[4:58] If you can explain me in the comments why is that, I would be really grateful.
[5:02] Let's build the same thing in point-fop instead.
[5:12] Now that threshold value determines how many points were not deleted.
[5:19] We will do a similar thing we did before.
[5:21] I will multiply pscale value with the maps falloff.
[5:31] But instead of directly specifying pscale value, we will be using random one based on point number.
[5:37] Random function gives us values from 0 to 1, so we can easily use fit function to adjust them.
[5:45] Let's display particles as disks.
[5:48] And adjust the ramp.
[5:52] It will add a ramp in between random and fit functions.
[5:56] We can control the ratio of the smaller and bigger particles.
[6:02] Let's make further adjustments to the maps falloff ramp.
[6:12] Now we see the problem that we have.
[6:15] Because point number changes every frame, our pscale value jumps as well.
[6:19] Luckily that's easy enough to fix.
[6:21] We will use timeshift frozen on the last frame.
[6:24] And a relative copy of the maps falloff.
[6:26] Now points state the same, we are just changing their size based on the maps falloff value.
[6:31] But to make it more interesting, I also would like to move them a bit, based on the same maps falloff.
[6:36] For that we will be using my favorite noise.
[6:39] If we add noise to the position value of the points, we will displace them in space.
[6:44] Basically that's what mount and sob does under the hood.
[6:47] And I could have just used that, but I decided to build it from scratch.
[6:51] We will be adding maps falloff value to the y component of the position.
[6:55] That way particles will go higher the first time they appear and then settle down.
[7:05] But I don't want them to rise with the same value, so let's add the noise.
[7:17] Now the points are static, aside from the size animation.
[7:29] We can make points move constantly with a simple time expression, put into the offset of the noise.
[7:35] As we are done with the shell, let's add a null to it.
[7:39] And most likely points are going outside of the shell.
[7:42] Let's fix that.
[7:45] The easiest way to do that is to use mask from geometry, and to scale down all the points that are outside our shell.
[7:53] Now all the points that are outside has mask value of 0.
[7:58] We will use blast to delete them.
[8:03] And I will use the second mask from geometry to scale down any points that are close to the surface.
[8:15] I am done with the bubbles. I will add a null to them.
[8:22] But to see what they are doing inside the shell, I will use an alpha.
[8:26] That's only for previewing purposes. You can skip that step entirely.
[8:32] And finally, let's add a file cache to the bubbles.
[8:45] Preview of the bubbles is a bit janked, but that's because of an alpha.
[8:50] We will preview them in a different way.
[8:53] Right now let's do the usual.
[8:55] Add geometry container for each thing we want to render, and add object merge inside.
[9:00] It also would be nice to set up a camera right now.
[9:15] I am not a big fan of the bubbles movement right now. Let's adjust the noise.
[9:31] I want to get a feel like they are moving in the same direction, but each independently.
[9:36] And let's cache that version as well.
[9:45] Right now all of them are moving at the same speed.
[9:48] I want to make them move faster the first time they appear.
[9:51] To do that, instead of directly using time function, we will multiply it with the mobs falloff.
[9:59] Let's use parameter to set our default time value.
[10:08] Now we have successfully recreated the function we had before.
[10:12] Attribute previews don't work for some reason, but near displaying particles as disks.
[10:17] I had to make sure that I have mobs falloff attribute on that stream.
[10:21] Now let's use the ramp from mobs falloff to change the speed dynamically.
[10:28] Now we have a ramp to control how fast particles are moving at any stage of the animation.
[10:32] It's getting a bit heavy. Let's add another file cache before the final one.
[10:38] We can see that it works. Now we have to configure it.
[10:57] That shouldn't be good. Let's cache it out.
[11:07] And let's do the final cache as well.
[11:14] That's it for the first episode.
[11:16] The next one pickups where we left off and pushes the setup further.
[11:20] In the meantime, you can check out the complete ember material.
[11:23] Link to material alphabet and huddy-nupilid is in the description below.
[11:27] If this helped, consider subscribing and leave a comment if you have questions.
[11:31] It helps the channel going.
[11:33] I hope this gave you a few useful ideas you can apply to your own work.
[11:37] Thanks for watching.



---

## Captured Frames

- [0:44] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_000.jpg
- [1:05] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_001.jpg
- [2:10] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_002.jpg
- [3:43] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_003.jpg
- [5:45] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_004.jpg
- [8:15] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_005.jpg
- [10:28] tutorials/frames/material-alphabet-in-houdini-b-for-bubbles-episode-01/frame_006.jpg

---

## Structured Notes

### Core Technique
Fully procedural, simulation-free liquid-with-bubbles look: a MOPs Shape Falloff (0-1 gradient) drives displacement, appearance and bubble motion on a VDB-round-tripped font letter, while the bubbles themselves are pscale-randomized, time-shifted points scattered from the same volume — all sculpted by hand instead of run through a DOP solver.

### Summary
Episode 1 of Kotov Roman's "B for Bubbles" builds a liquid letter "B" with internal bubbles **without any dynamics simulation** — pure procedural geometry for full control over placement and motion. Starting from a flat Font SOP letter (frame_000, [0:44]), thickness comes from VDB from Polygons (bevel was abandoned after failing on complex geometry in the Amber episodes) plus a strong VDB Smooth pass that immediately reads as liquid (frame_001, [1:05]). A **MOPs Shape Falloff** node becomes the single driver for the whole effect: fed through Displace Along Normal (with noise layered on top, scaled/shaped via a ramp on the falloff) to bulge the surface, then multiplied into a copy of the falloff feeding **Points from Volume → pscale** so that low-falloff points vanish, and finally through **VDB from Particles → VDB Smooth → Convert** to rebuild the liquid mesh with a noise-broken (not perfectly smooth) edge (frame_002, [2:10], showing the raw falloff gradient colorized on the letter). The falloff is animated bottom-to-top to make the liquid "appear" over time and cached to disk (frame_003, [3:43], showing the falloff's animation curve). Bubbles reuse the same interior points: a Point VOP-based delete-by-threshold (VEX didn't work for the author here, so Point VOP substituted) thins them out, pscale is randomized per point (`random()` off point number, fit + ramp to control the small/large mix) and displayed as disks (frame_004, [5:45]). Because point number reshuffles every frame, a **Timeshift frozen on the last frame** plus a relative copy of the falloff keeps point identity stable while still driving size and a hand-built rise-and-settle motion (falloff added to the Y position, offset by noise, with a `$T`-based expression in the noise offset for continuous drift) — deliberately built from scratch instead of using Mountain SOP. Stray bubbles are cleaned up with two **Mask from Geometry** passes (one deletes points outside the shell via Blast, one shrinks points near the surface) (frame_005, [8:15], "I am done with the bubbles"). Final assembly uses per-element geometry containers + Object Merge, a camera, and a second falloff-driven speed control (time multiplied by the falloff, then remapped through a ramp) so bubbles move fast on first appearing and slow down over the shot (frame_006, [10:28]), with staged File Cache nodes at each major iteration.

### Key Steps
1. **Setup container** (`setup`, colored red), gray viewport background; **Font** SOP typed "B" (font swapped for a rounder look).
2. **Thickness**: skip PolyBevel (known to fail on complex letterforms per the Amber episodes) — go straight to **VDB from Polygons**; adjust FPS settings before proceeding into the volume workflow.
3. **Liquid read**: **VDB Smooth**, cranked up, immediately sells the shape as liquid (frame_001).
4. **Shape driver**: **MOPs Shape Falloff** (0-1 gradient) — used for displacement, appearance, and bubble motion throughout; full-link-copy the node (Ctrl+Alt+Shift+drag) wherever it's needed downstream so all instances stay synced.
5. **Displacement**: **Displace Along Normals** — Position → `position`, MOPs Falloff → `amount`; a **Ramp** on the falloff shapes where displacement is strongest; a **Noise** multiplied with the falloff adds irregularity.
6. **Volume re-scatter**: **Points from Volume** on the letter volume; a linked copy of the falloff multiplies into **pscale** so points at low falloff shrink toward zero — visualized by switching the viewport to Points display; **VDB from Particles** (pscale must be scaled up first to register) rebuilds a volume from only the surviving points.
7. **Re-mesh**: **VDB Smooth → Convert to Polygons**; the cutoff reads too smooth, so a second **Noise** is fed through the (again-copied) MOPs Shape Falloff to break up the edge; **File Cache** to disk once acceptable.
8. **Falloff animation**: animate the Shape Falloff bottom-to-top so the liquid appears to rise into frame over time; iterate displacement amount and noise pattern, re-caching each pass; compare cached versions and partially revert changes that didn't read well.
9. **Bubble points**: reuse the interior points already generated; delete most of them down to a sparse set — attempted in VEX first (didn't work, cause undetermined), rebuilt as a **Point VOP** thresholding a value against the falloff.
10. **Bubble sizing**: multiply pscale by the (linked) MOPs falloff, but drive it from `random()` seeded by point number instead of a constant, run through **Fit** then a **Ramp** to control the ratio of small vs. large bubbles; display as disks to check.
11. **Stable point identity**: point numbers reshuffle every frame → **Timeshift** frozen on the last frame supplies stable points, combined with a *relative* copy of the falloff so only size (not identity) animates off it.
12. **Bubble motion (hand-built, not Mountain SOP)**: add the falloff value to each point's Y position (rise higher the earlier they appear, then settle), offset by **Noise** so bubbles don't rise uniformly; a `$T`-based time expression in the noise's offset parameter keeps points drifting continuously rather than freezing once risen.
13. **Cleanup**: two **Mask from Geometry** nodes — one flags points outside the liquid shell (mask = 0) and deletes them with **Blast**; a second shrinks points close to the surface so bubbles don't poke through.
14. **Bubble preview/cache**: **Null**, temporary **Alpha** node for interior visibility (preview-only, skippable), then **File Cache**.
15. **Render assembly**: a geometry container per render element with **Object Merge**, plus a camera.
16. **Motion polish**: adjust the drift noise for a "moving together but independently" feel; re-cache; replace a flat time-based drive with **time × MOPs Falloff** (via a parameter for the base time value) so bubbles move faster right after appearing, then use the falloff's **Ramp** to control speed dynamically across the whole animation; a second, earlier File Cache stage added before the final one as the network gets heavy.

### Houdini Nodes / VEX / Settings
- **Geometry / volumes**: Font, VDB from Polygons (thickness, replacing PolyBevel), VDB Smooth (×2 — shape read, and edge break-up before Convert), Convert (VDB → polygons), Points from Volume, VDB from Particles, Timeshift (frozen on last frame), Blast, Null, File Cache (multiple staged caches through the iteration).
- **MOPs**: Shape Falloff (0-1 gradient; the single driver node, full-link-copied wherever reused), its built-in Ramp (reshapes the gradient per use), Mask from Geometry (×2 — outside-shell delete, near-surface shrink).
- **VOP / attributes**: Displace Along Normals (position + MOPs falloff → amount), Volume/Point VOP with Noise (surface irregularity, edge break-up, and bubble drift), `random()` seeded by point number, Fit, Ramp, Point VOP threshold-delete (substituted for a non-working VEX attempt), pscale multiplied by falloff for both volume-thinning and bubble-size control, time expression (`$T`-driven) in a noise offset parameter for continuous drift, time × falloff for appear-fast-then-settle bubble speed.
- **Assembly**: geometry containers per element + Object Merge, camera, Alpha (interior preview only).
- **UI**: full-link node copy via Ctrl+Alt+Shift+drag; switching viewport display to Points to check scatter/pscale results.

### Difficulty
Advanced

### Houdini Version
Not specified

### Tags
sop, vop, volumes, particles, procedural, attributes, modelling, advanced

---

## Related Tutorials
- [Material alphabet in Houdini: A for Amber | Episode 01](material-alphabet-in-houdini-a-for-amber-episode-01.md) — same author, same series; shares the VDB from Polygons (bevel-avoidance) and scatter/randomize-attribute patterns
- [Material alphabet in Houdini: A for Amber | Episode 02](material-alphabet-in-houdini-a-for-amber-episode-02.md) — same author, same series; continuation-style material study on a letterform
- [Abstract liquid in Houdini | Part 01 - Building the simulation](abstract-liquid-in-houdini-part-01---building-the-simulation.md) — same author's other liquid-look project, useful contrast: a real FLIP sim vs. this episode's fully procedural, sim-free approach to the same "liquid" read
