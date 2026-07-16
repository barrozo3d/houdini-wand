---
title: Particle rotations in Houdini (how to rotate orient)
source: YouTube
url: https://www.youtube.com/watch?v=gmN76ZeObsA
author: the point and prim
ingested: 2026-07-16
houdini_version: "Not specified"
tags: [quaternions, particle-rotation, orient-attribute, vex, vops, point-vop, the-point-and-prim]
extraction_status: complete
frames_dir: tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Particle rotations in Houdini (how to rotate orient)

**Source:** [YouTube](https://www.youtube.com/watch?v=gmN76ZeObsA)
**Author:** the point and prim
**Duration:** 7m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome again.
[0:02] Over the next two videos we will be talking about rotating lots of stuff.
[0:06] And by that I mean how to rotate particles as well as packed primitives without the need of simulation.
[0:12] This will give us full control as we will be using attributes or channel parameters to drive the effect.
[0:16] I will explain particle rotation in this video and packed prim rotation in the next one as it is a bit more complex.
[0:22] If you hate listening to me speak the hip file is on Gumroad as always.
[0:26] For demonstration purpose we will just start with a single point.
[0:29] Drop down an attribute randomize, set it to Orion.
[0:32] This is a native Houdini attribute and is a vector 4. So add another dimension here.
[0:36] If you didn't know what we are creating here is a Quaternion which is the most explicit way of storing spatial rotation available to us.
[0:42] I will just arbitrarily tweak the seed value to get something that I like.
[0:46] And next we want to drop down a point var and dive in. We will do all our work here.
[0:50] Starting by first binding in the Orion attribute we created and making sure to set it to vector 4 in the type parameter.
[0:56] The way to rotate Quaternions is by multiplying two of them together.
[0:59] Houdini provides us with a Q multiply var that will do this function for us.
[1:03] In order to multiply our original Orion we will need to construct a second Quaternion which can be done with a Quaternion var.
[1:09] This is going to be the main driver for our rotation.
[1:11] The inputs of our new Quaternion comprise of an angle and an axis.
[1:14] If we look at the vex documentation we can see that this function will construct a brand new vector 4 Quaternion from the combined angle and axis.
[1:21] The axis should be normalized and the angle which represents how much we want to rotate around our axis once radians as an input.
[1:28] So our Quaternion expects two inputs.
[1:30] Axis is easy. That's just a standard vector that we want to pipe through a normalized function.
[1:34] Angle is a bit weirder. We want to be able to represent 360 degrees of rotation.
[1:38] When we convert 360 to radians we get 2 times pi which evaluates to roughly 6.28.
[1:44] Needless to say, working with degrees or radians will be really annoying so we will fix that in a second.
[1:49] So back in Houdini let's just promote these two parameters and play with them for a sec.
[1:53] I want to rotate around the Z axis so let's just pop that in here.
[1:56] And our greatest fear has been confirmed. Look how annoying it is to rotate this thing with radians.
[2:00] When we input 2 times pi we will get a full rotation and pi itself will then of course be a half rotation.
[2:05] So what we will do is use pi for good, not evil. We could try to use the degrees to radians of up to convert our input.
[2:11] But I dislike this because it is still so obnoxious to work with.
[2:15] The preferred method is instead to simply multiply the input by a constant set of 2 times pi.
[2:20] This means that all we now need to work with is values between 0 and 1.
[2:24] One representing a full revolution around chosen axis.
[2:27] Anything less than 1 will be a partial rotation and anything greater than 1 being multiple rotations.
[2:31] Meaning a value of 2 would mean 2 complete revolutions.
[2:34] Now that we have a simple way to control rotation we can start doing this to multiple points.
[2:39] Right now we are still rotating around the Z axis only.
[2:42] So let's create a random vector used for the chosen axis instead.
[2:45] Here I am using an attribute adjust vector set to random 0 centred.
[2:49] Which means the vector lengths will actually be around 0.5.
[2:52] And remember the Caternion wants normalize values.
[2:55] So after we bind in the axis let's drop a normalize in between them.
[2:59] Now that that works there is only one thing left to do and that is further manipulation of the angle control.
[3:04] Because angle is now a normalized input of 1 rotation per whole value of 1.
[3:08] It is easy to get consistent rotations by using global attributes like time or frame.
[3:12] This is especially useful when you need to add random animated rotations to large amounts of points.
[3:17] A common use case is effects like snow.
[3:19] We're adding rotation helps sell the illusion of turbulence.
[3:22] And with this exact same method it is easy to make adjustments post sim.
[3:25] Here you can see I am using the exact same point for and I have just got the time multiplier set to the default of 1.
[3:30] The only thing left to talk about is control of the rotation via attribute.
[3:34] So let's create a float called foo and use an adjust float set to line to get a little diagonal gradient.
[3:39] Inside the vote let's just delete the time stuff.
[3:42] I am going to use the smooth function to animate the foo attribute.
[3:45] I won't cover this as I have already made two videos on how this works.
[3:48] If you haven't seen them I will link them below.
[3:50] The smooth function is great for working with the angle component of the cotanion as it always returns a value between 0 and 1.
[3:57] Here I am just setting some keyframes to animate the smooth value and we can see that that is rotating our auto-rein attribute nicely along that diagonal.
[4:04] This concludes the theory part of the video.
[4:06] We will now briefly step through the setup for the render in the intro to see the technique applied to something.
[4:13] So I've just got a simple sphere that I VDB and scatter about a million points inside.
[4:17] I then blast out a thousand of those and add some random velocity to them.
[4:21] I then run that through a VDB from particles to get a cluster shape for the source.
[4:25] I only want my volumes to emit on the first frame so I am just using the classic dollar f start frame trick in both density and veil.
[4:33] And what we get from that is this little unimpressive smoke puff.
[4:37] But all we want from this is a single frame of its velocity field.
[4:40] So in the left stream we have a million points scattered and we have some geometry coming in from the right stream too.
[4:46] I won't cover this now because I've done it so many times on this channel.
[4:49] But it's just using noise and points to get a really cheap edge fracture on the shell of a geometry.
[4:53] And then I actually pack the pieces and apply the primitive rotation that we will talk about in the next video to them.
[4:58] So what we get is this fuzzy blob for our particle source consisting of both points and packed frames.
[5:04] So again we can just set some curl noise with a point velocity stop.
[5:08] Inside dops we've got the particle advection, some random drag and bit of pop-force noise.
[5:13] I'm also just sourcing on the first frame.
[5:15] An important to note is that I've set the emission type to all geometry, which will let me emit my packed frames as well as the points simultaneously.
[5:23] So the result of that is this curly particle sim and the reason why it looks so different to the typical smoke evaction is because we only use one frame of the smoke.
[5:31] So the particles will simply be pulled along their set vector directions in the velocity field instead of being evicted every frame by a constantly evolving simulation.
[5:39] All that's left to do now is apply the rotation to vet the particles and the packed primitives.
[5:43] So down here we've got the particle rotation. I'll just delete some of these so we can see the axis doing their thing.
[5:49] And here we can see the points rotating around their local y-axis with varying speed.
[5:53] This is the same logic as before, just written in Vax instead.
[5:56] We achieve the varied speed I simply multiplying frame with a random value unique to each ID.
[6:01] The initial orient randomization is done using the sample orientation uniform function.
[6:05] The rotating axis is simply a vector of 0, 1, 0, the y-axis.
[6:10] And here I construct the rotation quaternion from angle and axis like we did in the Vop example.
[6:15] And then multiply it against the initial orient.
[6:18] After that's all done, all that is left to do is instance your desired geometry.
[6:21] I'm just using these weird strands and assigning them to each point by a class attribute.
[6:27] That is now working nicely.
[6:29] The main benefit of all this is that we don't get any of the unpredictable axis flipping that happens when using simple vectors to do rotations.
[6:35] What I haven't covered yet is the packed prim rotation as we will cover that in the next video.
[6:39] But if you want to see how that is done, you can download the hip file from Gumroad, which includes the render setup too.
[6:44] Alternatively, the code for both particle and packed prim rotations is included in my Vax snippet pack,
[6:50] along with a lot of other useful stuff. I'll drop both links in the description.
[6:54] And that is it for today. Thanks so much for joining me again and I'll see you in the next one.
[6:59] Thanks for watching.



---

## Captured Frames

- [0:32] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_000.jpg
- [0:59] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_001.jpg
- [1:14] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_002.jpg
- [2:15] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_003.jpg
- [3:42] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_004.jpg
- [4:37] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_005.jpg
- [5:43] tutorials/frames/particle-rotations-in-houdini-how-to-rotate-orient/frame_006.jpg

---

## Structured Notes

### Core Technique
Sim-free rotation of particles (and, in a follow-up video, packed primitives) by directly constructing and multiplying **Quaternions** from an angle/axis pair inside a Point VOP or VEX wrangle, driven by attributes or channel parameters instead of a DOP simulation.

### Summary
The video explains how to rotate large numbers of particles procedurally, without simulating anything, by manipulating the native Houdini `orient` attribute (a Vector4/Quaternion) directly. Starting from a single point, an **Attribute Randomize** node creates the `orient` attribute as a 4-component vector (a Quaternion — described as the least ambiguous way to store 3D rotation). Inside a **Point VOP**, the existing `orient` is bound in (set to Vector4), and a second Quaternion is built with a **Quaternion VOP** from an angle and an axis, since rotating one quaternion means multiplying it against another via **Q Multiply**. The axis input just needs to be a normalized vector; the angle input is trickier because it expects radians, and working directly in radians/degrees is called out as "obnoxious" — instead the angle parameter is authored as a normalized 0–1 value (1 = one full revolution) and multiplied by a constant `2*pi` before it reaches the Quaternion node, so artists only ever deal with values like 0–1 (or values >1 for multiple revolutions). Once this is set up on a single point, the technique scales to many points: the rotation axis is randomized per-point with an **Attribute Adjust Vector** (random, "0 centred," meaning vector length averages ~0.5) piped through a **Normalize** (since quaternions require normalized axes), and the angle is driven by global attributes like `$T`/frame or by a custom attribute for spatially-varying rotation (e.g. a linear gradient attribute animated via the **smooth function**, referenced from two earlier videos on that topic) — useful for effects like snow, where added rotation sells turbulence, and for post-sim adjustments since this all works independent of any simulation. A worked render example follows: a sphere is VDB'd, ~1M points scattered inside, 1,000 blasted out with random velocity, then converted via VDB-from-particles into a single cached frame of a Pyro sim's velocity field (sourced only on `$FSTART` so it stays a static single-frame smoke puff) purely to get an interesting velocity field to advect a separate POP particle sim through (mixed with curl noise, drag, and POP Force noise) rather than running a full evolving smoke sim. The emission type is set to "All Geometry" so points and packed primitives (fractured shell pieces, rotated with the technique covered in the follow-up video) emit together. Finally, the same angle/axis quaternion-construction logic is reimplemented directly in **VEX** on the particles: initial orientation is randomized with `sample_orientation_uniform()`, the rotation axis is a constant Y-axis vector `{0,1,0}`, the angle is `frame * random(@id)` (giving each particle a unique, ID-seeded rotation speed), the rotation quaternion is constructed from angle+axis exactly as in the VOP example, and it's multiplied against the initial orient. Instanced geometry (irregular "strand" shapes, assigned per point via a class attribute) is then driven by the resulting `orient` attribute. The stated benefit throughout is avoiding the unpredictable axis-flipping that plain vector-based rotation math can produce.

### Key Steps
1. On a single point, add **Attribute Randomize** to create the native `orient` attribute, set to Vector4 (a Quaternion) with an arbitrary seed.
2. Inside a **Point VOP**, bind in `orient` (Vector4), then build a second Quaternion via a **Quaternion VOP** node fed by a normalized axis vector and an angle in radians; multiply the two quaternions together with **Q Multiply VOP**.
3. Avoid working in raw radians/degrees by driving the angle input with a 0–1 parameter multiplied by a constant `2 * pi` (1.0 = one full revolution, values above 1 = multiple revolutions).
4. Scale to many points: randomize the rotation axis per-point with **Attribute Adjust Vector** (random, 0-centered) piped through **Normalize** before it reaches the Quaternion node.
5. Drive the normalized angle input with global attributes (`$T`/frame, useful for e.g. snow turbulence) or with a custom attribute animated via the **smooth function** (from the channel's earlier smooth-function videos) for spatially varying rotation.
6. Build the render-example particle source: VDB a sphere, scatter ~1M points, blast 1,000 with random velocity, convert to VDB-from-particles, run one frame of a Pyro sim (sourced only on `$FSTART`) purely to bake a usable velocity field.
7. Advect a separate POP simulation (curl noise + drag + POP Force noise) through that single cached velocity field so particles move along fixed vectors rather than a constantly-updating sim; set **emission type to "All Geometry"** so points and packed pieces emit together.
8. Reimplement the rotation in VEX on the particles: `sample_orientation_uniform()` for initial orient, axis `{0,1,0}`, angle `= frame * random(@id)` for per-particle speed variation, construct the rotation quaternion from angle+axis, and multiply it against the initial orient attribute.
9. Instance geometry onto the rotated points via a class attribute for per-point shape variation.

### Houdini Nodes / VEX / Settings
Attribute Randomize (`orient`, Vector4/Quaternion), Point VOP, Quaternion VOP (angle + axis construction), Q Multiply VOP, Normalize VOP, Attribute Adjust Vector (random, 0-centered axis), smooth function (angle-over-attribute animation), VDB from Polygons/scatter, VDB from Particles, Pyro Solver (`$FSTART`-only sourcing for a single-frame velocity field), POP Network (POP Force with curl noise, drag, "All Geometry" emission type), VEX wrangle (`sample_orientation_uniform()`, `quaternion(angle, axis)`, `qmultiply()`-equivalent, `@id`-seeded `random()`), class-attribute-driven instancing.

### Difficulty
Intermediate (requires understanding quaternion rotation math and VOP/VEX attribute wiring, but the actual node graph is compact and the author explains the theory step by step).

### Houdini Version
Not specified.

### Tags
#quaternions #particle-rotation #orient-attribute #vex #vops #point-vop #curl-noise #pop-network #the-point-and-prim

---

## Related Tutorials
- [Houdini: How to mask with the smooth function](houdini-how-to-mask-with-the-smooth-function.md) — same channel/author; directly referenced here as the source of the smooth-function angle-remap technique used to drive spatially-varying rotation.
- [Procedurally mask deforming / animated geometry - Houdini](procedurally-mask-deforming-animated-geometry---houdini.md) — same channel/author, continuing the smooth-function masking series referenced in this video.
- [Techniques for Fast Disintegration FX in Houdini](techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach.md) — same channel/author; reuses this exact rest-to-spinning quaternion blend technique for particle rotation in its disintegration effect.
