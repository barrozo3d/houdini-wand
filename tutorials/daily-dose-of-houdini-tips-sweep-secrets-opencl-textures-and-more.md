---
title: Daily dose of Houdini Tips | Sweep secrets, opencl textures and more
source: YouTube
url: https://www.youtube.com/watch?v=1QTfNMlvF1E
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, opencl, vellum, animation, procedural, texturing, cops, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily dose of Houdini Tips | Sweep secrets, opencl textures and more

**Source:** [YouTube](https://www.youtube.com/watch?v=1QTfNMlvF1E)
**Author:** cgside
**Duration:** 5m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I'm gonna share a few tips and tricks that I learned while working on the simple project.
[0:06] I'm saying it's simple but it turned out to be a bit more complex than I wanted.
[0:11] But yeah, let's check out some of those workflows.
[0:16] So after setting up the basic animation of the straw opening, like a straw rig, I'm trying to mesh this.
[0:24] And I think I could use the skin nodes, but another trick that I learned from the CG Wiggy Discord is to use the sweep only connected to the second input.
[0:33] And as you can see that will output the geometry.
[0:36] And after doing the UVs and calculating the normals, we get the proper geometry.
[0:42] So I don't think this is very usual and it's a nice trick to know.
[0:48] So just second input and default settings.
[0:51] Another thing to have in mind is you need to close implicit backbone.
[0:57] Otherwise you will have an open mesh as you can see.
[1:01] So yeah, for the second one.
[1:04] So as you can see we have a very basic animation in here and we have no secondary motion.
[1:09] So in here I have transformed the geometry into a simple line so I can do some deformation on it.
[1:18] The first thing I do is use a natribus noise vector to change the position a bit to noise up the position with animation as you can see.
[1:26] But I want it like a stop motion effect.
[1:29] So for that I'm using a sub-solver.
[1:32] So as you can see, if I enable this and run, as you can see it's just doing this stop motion effect.
[1:39] And it's not happening randomly. It's happening when the straw is opening those little things.
[1:50] I don't know what they call it.
[1:52] So like the accordion thing.
[1:54] So I recorded the frames where that happens.
[1:59] And then in a sub-solver I'm just finding that frame and lurping between the animation, the animated geometry.
[2:07] Which I'm copying the position from the second input and between the previous frames.
[2:12] So that gives us this stop motion effect.
[2:15] But another trick I wanted to show you is that this is the old very static kind of to add some twist to it.
[2:24] So what we can do and this trick I learned from Igor on the CGU record.
[2:28] You can add like a spring solver using Valum.
[2:32] This runs really fast and you'll get the sort of effect of some sort of spring effect as you can see.
[2:40] And the way I'm doing that is by using the Valum constraint set to Pinto targets, set your stiffness and add some damping ratio.
[2:48] And then just use a solver which I just removed the gravity and we get the spring like effect.
[2:56] So now we need to pass this to our animated geometry to our mainstream because right now is just this simple animation.
[3:04] So what we can do is to use a pointeform.
[3:08] And if you check we have the static geo.
[3:11] And I'm not using only a curve to do the pointeform to fit the rest and the animated pose.
[3:17] I'm using a sweep with the same amount of same radius as the original geometry.
[3:23] So that way the pointeform has an easier time deforming the geometry.
[3:28] As you can see I'm sweeping both the rest and the animated geometry.
[3:32] And that way it's much easier for the pointeform to calculate to do the calculations.
[3:37] And as you can see we now have the secondary animation added to our main animation.
[3:45] So what else? The final tip is on how I did the texturing for this draw.
[3:53] So it's not as easy as it might look.
[3:57] So I ended up relying on OpenCL and what did I do in years?
[4:02] So if we look at the destination we have these black and white strips.
[4:07] And for that I am using the UV map.
[4:12] So this is just like a UV map in texture space.
[4:15] Then I'm creating this pattern just by using thin of the Y component of the UVs.
[4:20] Multiply by the repetitions and by.
[4:22] So we have a perfect tiling pattern as you can see.
[4:26] The repetitions I set it to weighty, I can set it to 20 or less or something.
[4:30] But in this case I use 80.
[4:32] Then I'm calculating also an index for each stripe.
[4:36] And for that I can use the floor of the Y component of the UVs multiplied by the repetitions.
[4:41] Then I'm importing the random adder that the side effects provides.
[4:46] For OpenCL I am using the random one function and feeding that index.
[4:52] That way I can have a random value per strip.
[4:55] Then I'm just multiplying that by the pattern.
[4:58] So I can easily color it next.
[5:02] So it will always be this color.
[5:05] I wanted to be always white on the background.
[5:09] I'm also doing a transform in here.
[5:12] I just rotated 45 degrees.
[5:14] And that's my albedo and I'm feeding that to a preview material.
[5:18] And as you can see we have our animation.
[5:21] So yeah guys that was basically it.
[5:23] You can find the full project on my Patreon.
[5:25] I'm going to be sharing how I did all of this.
[5:28] It might be there's a lot of wax involved.
[5:31] But hopefully you'll find it useful.
[5:34] And if you have any questions you can always ask me.
[5:37] So yeah, thank you for watching.
[5:39] As always don't forget to check out the project files on Patreon and the exclusive videos I have on there.
[5:43] And thank you all for all the Patreon supporters that I have that have been helping me along the journey.
[5:50] So thank you.



---

## Captured Frames

- [0:35] tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/frame_000.jpg
- [1:35] tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/frame_001.jpg
- [2:35] tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/frame_002.jpg
- [3:30] tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/frame_003.jpg
- [4:10] tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/frame_004.jpg
- [5:20] tutorials/frames/daily-dose-of-houdini-tips-sweep-secrets-opencl-textures-and-more/frame_005.jpg

---

## Structured Notes

### Core Technique
A grab-bag of production tips learned while rigging/animating a drinking straw: meshing an accordion-fold rig with **Sweep**'s second input, faking stop-motion with a **sub-solver** lerp, adding secondary motion via a **Vellum spring solver**, and generating a tileable candy-cane stripe pattern with hand-written **OpenCL**.

### Summary
Covers four independent tricks from one project. First: to mesh an animated curve/rig (the straw's accordion joints) instead of using Skin, connect the curve only to Sweep's *second* input with default settings — remembering to close the implicit backbone or the mesh stays open. Second: to fake a stop-motion "pop" on the accordion folds, drive a simple line-based deformation with Attribute Noise (VOP), then gate it through a **Solver** that only lerps toward new positions on specific recorded frames (rather than continuously), producing a stepped, non-continuous motion. Third: to add a springy secondary-motion overshoot to the straw, build a Vellum rig using a **Vellum Constraint** set to Pin to Target with tuned stiffness/damping, run it through a **Vellum Solver** with gravity removed, then transfer that curve-only motion back onto the full straw geometry via **Point Deform** — sweeping both the rest and animated curves with the same radius as the real geometry first, which makes Point Deform's job much easier than deforming from a bare curve. Fourth: texturing the striped straw pattern procedurally in **COPs using OpenCL** — computing `frac(uv.y * repetitions)` for the tiling stripe pattern, `floor(uv.y * repetitions)` as a per-stripe index, and feeding that index into Houdini's built-in `random` OpenCL function for per-stripe random color/value variation.

### Key Steps
1. **Accordion mesh from Sweep:** feed the rigged/animated curve into **Sweep**'s *second* input only (leave the first/cross-section input default) to generate geometry directly from the curve's cross-section-implicit shape; follow with UV + Normal calculation. Remember to enable "close implicit backbone" or the resulting mesh is left open.
2. **Stop-motion fake:** convert the animated geometry to a simple line, run an **Attribute Noise (VOP)** to jitter position with the animation for texture, then build a **Solver** (sub-solver) that only updates/lerps to the current animated position on specific pre-identified frames (recorded manually where the accordion folds visibly "pop"), copying position from the second input and lerping from the previous held frame — producing a deliberate stepped/stop-motion look instead of smooth continuous motion.
3. **Vellum spring secondary motion:** build a Vellum setup on the simplified line: a **Vellum Constraint** node set to "Pin to Target" with tuned stiffness and damping ratio, run through a **Vellum Solver** with gravity disabled, producing a fast, springy overshoot effect on top of the base animation.
4. **Transferring motion back to full geometry:** rather than Point Deform-ing straight off a bare curve, **Sweep both the rest-pose and the Vellum-animated curve** using the same radius as the real straw geometry, then use **Point Deform** with those two swept tubes (rest + animated) as the deform pair — this gives Point Deform much more geometry to match against than a 1D curve, producing a cleaner secondary-motion transfer onto the final mesh.
5. **Procedural stripe texture via OpenCL (COPs):** using the UV map in texture space, compute a tiling stripe pattern as `frac(uv.y * repetitions)` (repetitions tunable, e.g. 20 vs. 80 used here); compute a per-stripe index as `floor(uv.y * repetitions)`; feed that index into Houdini's built-in OpenCL `random` function (via the provided random-number VEX/OpenCL header) to get one random value per stripe; multiply the random value by the stripe pattern for per-stripe colorization, keeping the background always white; finish with a 45° rotate transform on the pattern before feeding it as albedo into a preview material.

### Houdini Nodes / VEX / Settings
Nodes/techniques used: Sweep (second-input-only meshing trick, "close implicit backbone" option), UV + Normal calculation, Attribute Noise (VOP), Solver/sub-solver (frame-gated lerp for stop-motion), Vellum Constraints (Pin to Target, stiffness, damping ratio), Vellum Solver (gravity disabled), Point Deform, second Sweep pass (rest + animated curve, matched radius). OpenCL/VEX for texturing: `frac(uv.y * repetitions)` for tiling stripes, `floor(uv.y * repetitions)` for stripe index, Houdini's built-in `random` OpenCL function seeded by stripe index, Transform (2D, 45° rotation) on the resulting pattern, fed as albedo into a preview material — all inside a CopNet.

### Difficulty
Intermediate/Advanced — combines several non-obvious workflow tricks (Sweep's second input, frame-gated solver lerping, Vellum spring rigs, and hand-written OpenCL) that assume familiarity with Houdini's solver/VOP/Vellum systems.

### Houdini Version
20.5 (Copernicus/OpenCL COPs workflow matches the 20.5-era UI).

### Tags
#vex #opencl #vellum #animation #procedural #texturing #cops #tips #intermediate

---

## Related Tutorials
Cross-link with any other cgside COPs/OpenCL-texturing or Vellum secondary-motion tutorials once extracted from this batch.
