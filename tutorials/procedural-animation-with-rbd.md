---
title: Procedural Animation with RBD
source: YouTube
url: https://www.youtube.com/watch?v=RbiH315adq8
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.322"
tags: [rbd, simulation, packed-primitives, karma, procedural-animation, food, torque, velocity]
extraction_status: complete
frames_dir: tutorials/frames/procedural-animation-with-rbd/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Animation with RBD

**Source:** [YouTube](https://www.youtube.com/watch?v=RbiH315adq8)
**Author:** cgside
**Duration:** 6m17s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I want to show you how you can fill up a container really easily
[0:08] and along the way also create some nice animation as you can see this barrel getting filled up with the cheese balls
[0:17] So yeah let's get into it!


### Modeling [0:20]
**Transcript (timestamped):**
[0:20] So I started by modeling the barrel, nothing too complicated, just a mix between procedural
[0:29] and direct modeling, this is how it looks
[0:33] So you can have a look at the file on my Patreon if you're interested in that part and in the rest of the configuration
[0:42] So then I'm importing that low polyversion of the barrel
[0:49] Transforming a bit the leads so it's not intersecting with the main barrel
[0:58] Creating an RBD configure, setting the collision shape to convexle and also creating the...
[1:07] In this case creating backfragments, so packing the geometry
[1:12] Then I'm initializing a torque attribute and then randomizing it for the main barrel
[1:22] In this case I had to set a really high amplitude due to the scene scale
[1:27] Then doing the same for the lead, in this case setting it to 85 and playing with the seed
[1:35] Then in the RGB bullet solver I'm just reducing the angular velocity from frame 144
[1:47] So just reducing it by 0.8 and if we have a look at the final result it will look something like this
[1:55] And after frame 144 it will slow down and get to the rest state
[2:06] So now for the feeling of the container


### Filling [2:10]
**Transcript (timestamped):**
[2:11] I'm just blasting the patch group that I've created from the modeling when I filled the polygons
[2:19] Transforming it a bit, scaling it up, then adding some normals
[2:26] So I can in the next step pick it along the timeline so going up as you can see
[2:35] Then I scatter some points in this case 14 and as a global seed I use the add frame
[2:41] So it gets a different result every time, a different seed
[2:45] Then I'm creating the velocity to fit the RGB, the RBD scene
[2:53] In this case by using the cross product between the position and the up vector
[3:04] You can see so it's creating this effect
[3:12] And from there I can just copy two points and it just a sphere, a simplified sphere
[3:20] And it will look something like this
[3:25] Then RBD configure so I can set the collision shape to sphere and also pass the velocity attribute
[3:35] So we can use it in the RBD scene
[3:42] Then I will emit these spheres for every four frames and before frame 120
[3:53] And in this wrangle I'm just setting the found overlap so they intersect along the way


### Simulation Points [4:00]
**Transcript (timestamped):**
[4:00] On the RBD I have nothing, just really default settings
[4:06] And then I'm focusing the points, so the simulation points I can show you
[4:15] The simulation points and it will look something like this
[4:21] So it is going around and filling it up along the way
[4:28] So from there I'm just copying two points with those simulation points
[4:35] I'm deleting everything but the orient attribute so it can properly instance the new geometry
[4:43] Which is just a displaced sphere
[4:49] And it will look something like this
[4:56] Creating this nice, swirly animation
[5:00] And I'm also placing a label on the barrel
[5:04] And this is a node that I created
[5:09] So basically I'm starting by blasting everything but the barrel
[5:16] Then time shifting it to frame 1
[5:20] And I have this node that places a label on the geometry
[5:28] You can find that on my Patreon
[5:31] And then I'm just picking it a little bit and point the forming it so it follows the animation as you can see
[5:39] Nothing to complicate it
[5:42] And then I'm sending these to salaries and rendering with karma
[5:47] But yeah, this was a quick one to show you how you can fill up a container in a creative way
[5:58] And I would like to thank Swalves for suggesting me to do proper animation
[6:04] And not just to stick with the default filling up
[6:09] Because it looks much better
[6:12] And hopefully you can find this useful
[6:14] Thank you for watching and I'll see you next time



---

## Captured Frames

- [0:25] tutorials/frames/procedural-animation-with-rbd/frame_000.jpg
- [1:00] tutorials/frames/procedural-animation-with-rbd/frame_001.jpg
- [1:40] tutorials/frames/procedural-animation-with-rbd/frame_002.jpg
- [2:40] tutorials/frames/procedural-animation-with-rbd/frame_003.jpg
- [3:30] tutorials/frames/procedural-animation-with-rbd/frame_004.jpg
- [4:20] tutorials/frames/procedural-animation-with-rbd/frame_005.jpg
- [5:20] tutorials/frames/procedural-animation-with-rbd/frame_006.jpg
- [6:10] tutorials/frames/procedural-animation-with-rbd/frame_007.jpg

---

## Structured Notes

### Core Technique
Fill a container (a cheese-ball barrel) with a naturally swirling, non-uniform animation by giving each emitted RBD sphere an initial **cross-product-derived velocity** (position × up vector) before simulating, rather than just dropping them in with default gravity fill.

### Summary
The barrel/lid are simulated first with RBD Configure (convex hull collision, packed fragments) and a randomized initial torque (high amplitude due to scene scale) so the lid pops and settles, with angular velocity damped down after frame 144 via the RBD Bullet Solver so the barrel comes to rest. For the fill: the barrel's cap/patch-group opening is transformed/scaled/given normals so it can be Picked along the timeline to reveal an emission opening. Points are scattered (14 points, seeded per-frame via `$F` so each frame's scatter differs), each given a velocity computed as the **cross product between point position and an up vector** — this is what produces the swirling motion instead of straight-down dropping. Spheres are copied to these points, fed an RBD Configure with sphere collision shape and the custom velocity attribute, then emitted every 4 frames before frame 120 via a wrangle setting "found overlap" so intersecting spawns are tolerated. The RBD simulation itself uses default settings; simulation points are extracted separately (keeping only the `orient` attribute) so a nicer, displaced-sphere final geometry can be instanced onto them via Copy to Points for the render-quality result. A custom node places a label on the barrel by blasting everything but the barrel body, time-shifting to frame 1, and using a "place label" tool, then Point-deforming it to follow the sim.

### Key Steps
1. Model the barrel (mix of procedural/direct modeling), import the low-poly proxy version, and slightly transform the lid so it doesn't intersect the barrel body at rest.
2. **Barrel/lid RBD setup**: RBD Configure with collision shape set to Convex Hull, enable packed fragments; initialize a torque attribute and randomize it for the main barrel (high amplitude due to scene scale) and separately for the lid (value ~85, its own seed).
3. In the **RBD Bullet Solver**, reduce angular velocity starting at frame 144 (multiply by ~0.8) so the barrel settles into a rest state after that frame.
4. **Container opening**: blast the patch group created during modeling (the fill opening), transform/scale it up, add normals, then **Pick** it along the timeline to open a gap for emission.
5. **Fill points**: scatter 14 points, using `$F` (current frame) as the global seed so every frame produces a different scatter result.
6. **Velocity for swirl**: compute each point's velocity as the **cross product of its position and an up vector**, producing the characteristic swirling fill motion rather than straight-down gravity dropping.
7. Copy a simplified sphere to these points, then **RBD Configure** with collision shape set to Sphere and the custom velocity attribute passed through so the RBD Bullet Solver can use it.
8. **Staggered emission**: emit new spheres every 4 frames, and only before frame 120; in a wrangle set "found overlap" so initially-overlapping spawn points don't cause simulation errors.
9. Run the RBD simulation with otherwise default settings; isolate just the **simulation points** (deleting everything but the `orient` attribute) so a nicer, displaced-sphere geometry can be instanced onto them for final render quality via **Copy to Points**.
10. **Barrel label**: blast everything but the barrel body, Time Shift to frame 1 (the pre-sim rest pose) to place a custom "place label" node's output, then Point Deform it so the label follows the barrel's animation.
11. Send the final result to Solaris and render with Karma.

### Houdini Nodes / VEX / Settings
RBD Configure (Convex Hull / Sphere collision shapes, packed fragments), Attribute Adjust Vector (torque initialization/randomization), RBD Bullet Solver (angular velocity damping from a specific frame), Pick (timeline-driven opening), Scatter (`$F`-seeded per-frame), cross-product velocity wrangle (`position × up`), Copy to Points, Attribute Wrangle (staggered frame-based emission, "found overlap" flag), simulation-point isolation (keep only `orient`), Copy to Points (final displaced-sphere instancing), Time Shift, custom "place label" node, Point Deform.

### Difficulty
Intermediate (the cross-product velocity trick is simple once known, but the multi-stage RBD setup — barrel settle, opening pick, staggered fill emission, and final re-instancing — requires careful sequencing).

### Houdini Version
20.5.322 (visible in viewport title bar).

### Tags
rbd, simulation, packed-primitives, karma, procedural-animation, food, torque, velocity

---

## Related Tutorials
- [Making Trash in Houdini](making-trash-in-houdini.md) — related RBD mid-sim technique (glue-to-rigid constraint switching) from the same channel.
- [Procedural Rock Wall without intersections](procedural-rock-wall-without-intersections.md) — another example of using RBD as a controlled animation/compression tool rather than pure destructive simulation.
