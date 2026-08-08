---
title: Recursive Flow Simulations in COPs Houdini
source: YouTube
url: https://www.youtube.com/watch?v=pOQ8HUl-GTY
author: newa
ingested: 2026-08-08
houdini_version: "20.5+ (Copernicus context)"
tags: [copernicus, cops, flow-solver, curvature, recursive-simulation, feedback-loop, sdf-shape, slope-direction, procedural-smoke, splitting-pattern, noise-driven]
extraction_status: complete
frames_dir: tutorials/frames/recursive-flow-simulations-in-cops-houdini/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Recursive Flow Simulations in COPs Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=pOQ8HUl-GTY)
**Author:** newa
**Duration:** 9m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, today I'm going to show you how we can create a recursive flow sim with the flow solver in Copernicus.
[0:07] First, we create a geometry node, then a copnet and dive into that.
[0:13] We start with the SDF shape, we can choose whichever shape we want.
[0:18] I'll go for an interesting one like infinity for example, make it a bit smaller and we convert it to a mono.
[0:26] Then of course we need the flow solver.
[0:30] And you can put the mono shape into the flow.
[0:32] When you play, we don't have anything yet, but this is where the magical happen.
[0:38] First you need to create the velocity.
[0:41] I want to do that by converting it to a mono.
[0:44] Then we will blur it and then do a slope direction and make sure to set it on 180.
[0:50] Then if you plug this into the velocity, there should be something happening.
[0:54] Yes.
[0:55] And it's just like a normal infection between the flow solver.
[1:00] Here we also have some settings that we can change later on, but I'll leave it like this for now.
[1:04] So we have the velocity, but again we want to change this velocity based on something.
[1:10] And for the recursive pattern, the thing we want to do is use curvature.
[1:15] So we plug it from the color to the curvature, then set it to finite difference.
[1:24] Here you get like a, if we do fractal noise to visualize it.
[1:30] It's like 0.5 is the middle and then when it's concave, it's probably black and then the other one is white.
[1:40] So when we plug this in, we don't see anything yet, but I used max and concavity in my setup.
[1:50] I started to switch, but because now we don't see anything, we also need to blur it a bit to get some more values.
[1:57] Then if we sharpen this and make it a bit bigger, gain it, then we can see the shape already because here the values are just so low.
[2:08] So we use a sharpen to make it a bit more brighter.
[2:11] And then if we multiply the velocity with the curvature, then it goes a bit wild, but we can see something is happening.
[2:20] So now it's just viewing our stuff like we can make this smaller.
[2:28] You can do a bright note to make it slower, set it to 0.1 for example.
[2:35] And then if we play it now, it's already a bit better.
[2:39] It's still too hectic.
[2:40] That's probably because of the need to blur it also a bit after we multiply it.
[2:47] Okay, we're starting to get there.
[2:49] We can see it's just a lot of playing around with parameters like blur and like speed.
[2:56] Like if we blur this more, we can get already a good result.
[3:01] Now it's not that recursive yet because if you look here, it's maybe getting blurred too much or like too less.
[3:08] If you can just view the outcome.
[3:11] Now we have this, but something else we need to do is do a max on the color and do this.
[3:22] Maybe wait a little to make it easier.
[3:27] Let's just do it and pass through and then pass through to the max.
[3:31] So we keep our shape.
[3:32] So we keep affecting smoke from it.
[3:36] Okay, now we have this.
[3:38] If you remove this blur, you can get a lot of different effects with this.
[3:46] The most things you need to play around with is the sharpen and the blurs.
[3:51] But you can see here that it starts with a bubble and then it splits, but it's not that clear yet.
[4:00] We can also change the curvature and see if we get any better results with the other ones.
[4:07] This is a more smoky one and here nothing happens.
[4:11] Gosh, it's also looking decent.
[4:14] I think if I do it more or less, we get a lot of different stuff.
[4:20] Maybe set this to 0.5.
[4:22] Okay, so this already helped a bit by adding a remap with this type of curve.
[4:28] Okay, so let's check if we blur it, but not that much.
[4:31] Yeah, so then the curvature, sharpen, remap.
[4:35] Let's check it.
[4:39] Maybe if you add some sub steps.
[4:42] Yes, you can also make this higher, but then the same will go slower.
[4:46] So I'll leave it like this for now.
[4:48] This is how the borders of the cop net work if it's a closed space or open one.
[4:53] Yeah, maybe I should also normalize the incoming vector.
[4:58] Yeah, I think that will do a lot.
[5:00] I think that was the missing piece to the setup.
[5:02] It's already slower now.
[5:04] So if you speed it up again, it's blurred a lot.
[5:07] So let's do this a bit less.
[5:10] Let's blur this also a bit less and we can already see some extra stuff happening.
[5:15] I will also maybe make it 4k.
[5:18] Let's see if it's too slow or not.
[5:20] All right, I'm going to set this back to what I originally had.
[5:25] Well, that's also why it didn't look that good probably.
[5:27] But yeah, if you put this back on what I first had,
[5:31] you can see, you get like here it splits, it splits.
[5:36] It just keeps splitting on and on.
[5:39] So yeah, you can see like getting to this, it's playing a lot with the values, but
[5:45] it's a fun process.
[5:46] Like if you blur this more, we get rounder shapes,
[5:52] like really big shapes.
[5:54] For example, if you want, you can also pixelate it.
[6:00] I already had some pretty cool stuff at that.
[6:04] So of course, not that similar, but it's a more unique effect, I guess.
[6:10] Like here, you can see it's like blocks, because then you're using this to get the curvature.
[6:16] I don't want to remove it for now.
[6:20] But yeah, like these big ones are pretty nice.
[6:24] What happens?
[6:25] Yeah, but you can see them splitting like pretty good.
[6:32] Let's see if I, with the min, it is like more sharper.
[6:40] So if you do the max, you get the nice bubbly shapes.
[6:48] So then you can keep playing with this setup.
[6:52] But for example, you can also use a noise as an input.
[6:56] Then we get this pattern already.
[6:59] Give it more contrast, clamp it, animate it here, put it to four or something.
[7:07] Then we get this.
[7:09] Make it bigger, change it to alligator.
[7:13] Yeah, no, you can just keep on playing with stuff.
[7:17] You can add extra velocities.
[7:21] I, with most of the time, add them before doing the multiply, set them into UV, make them pretty strong.
[7:30] To get some more motion in it, you can also animate this.
[7:34] Then what else can we do?
[7:36] It might be change it to Berlin.
[7:38] I'm going to make this a bit sharper.
[7:40] So yeah, you can also input colors if you want to, or do like an extra thing here that has like real
[7:49] colors and you just affect it by this velocity.
[7:53] So yeah, that's how we can create some recursive smoke.
[7:57] This also works on normal infections if you would want to do it.
[8:02] Just getting the curvature and multiplying it with the velocity.
[8:11] I'm going to remove this for now.
[8:14] Yeah, if you want to add gravity, you can just do a bright note and then here at shift 0, 0.
[8:25] Then my point one, for example, then everything goes down.
[8:30] I will also quickly show some setups with the same setup.
[8:34] It just changed values.
[8:37] Here are some floating ones and they like split.
[8:40] It's their time to split, I guess.
[8:43] They leave some nice strings behind.
[8:45] It's mainly the sharpen and the remap at the end doing this.
[8:49] Like if I change this, you get some lines.
[8:52] But yeah, let's replay it.
[8:57] Maybe also lower the sub steps a bit.
[9:01] But like yeah, this is pretty cool, I think.
[9:04] We get these flowing particles.
[9:08] Another one I had here was this.
[9:13] It was a bit the setup we made using the outline then.
[9:16] Then also this was using a different curvature and here you can see it will go inwards.
[9:22] It's like fighting itself but also going outwards.
[9:26] It's like they split but they kind of come back.
[9:31] It's like also cool.
[9:34] So yeah, if you just change the curvature here, for example,
[9:40] here it was using mean and convexity.
[9:42] If it's this one, sometimes you also need to invert it probably.
[9:48] Like oh yeah, here we can see it very well when it splits.
[9:52] So yeah, there's a lot of possibilities with this.
[9:55] So have fun and try and create some cool stuff with it.
[9:58] Thanks for watching.



---

## Captured Frames

- [0:18] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_000.jpg
- [0:44] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_001.jpg
- [0:54] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_002.jpg
- [1:24] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_003.jpg
- [2:11] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_004.jpg
- [2:56] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_005.jpg
- [3:38] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_006.jpg
- [3:51] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_007.jpg
- [4:57] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_008.jpg
- [5:31] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_009.jpg
- [5:54] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_010.jpg
- [6:40] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_011.jpg
- [6:56] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_012.jpg
- [8:14] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_013.jpg
- [9:13] tutorials/frames/recursive-flow-simulations-in-cops-houdini/frame_014.jpg

---

## Structured Notes

> **Note on source:** this is an informal, exploratory "playing around with parameters" session (lots of live trial-and-error, not a clean step-by-step recipe) — the notes below capture the underlying mechanism and the parameters that mattered, not a literal reproducible step order.

### Core Technique
A **Flow solver inside Copernicus (COPs)** driven by a velocity field that is continuously self-modified by the *shape's own curvature* — feeding a shape's concave/convex curvature back into its own advection velocity creates a feedback loop where the shape recursively splits, bubbles, and re-splits over time, rather than just diffusing outward like a normal fluid/smoke sim.

### Summary
Base setup: inside a `copnet`, an **SDF Shape** node (any shape works — an infinity/figure-eight shape is used here) is converted to mono and fed into a **Flow** solver node. On its own this does nothing until a **velocity** input is built: the mono shape is blurred, then run through a **Slope Direction** node (angle set to 180) to derive a directional flow field from the shape's gradient — plugged into the Flow solver's velocity input, this alone produces ordinary shape-following advection (comparable to a normal "inflection"/diffusion effect).

**The recursive part — curvature-driven velocity modulation:** the flow's evolving color/shape output is fed into a **Curvature** node (mode: **Finite Difference**, later experiments also try **Mean** + **Concavity/Convexity**), which produces a signed field — roughly 0.5 = flat, darker = concave, lighter = convex (visualized directly with a fractal-noise-style ramp to check the 0-1 range). Because the raw curvature values are subtle, they get **blurred** (to introduce more graduated values) then **sharpened** and **gained/brightened** to make the concave/convex structure clearly visible. That curvature field is then **multiplied with the velocity** — this is the actual feedback mechanism: at any point, how much and which way the shape locally advects now depends on how curved that region of the shape currently is, so as the shape deforms, its curvature changes, which changes its velocity, which changes its shape again — a self-reinforcing loop that produces branching/splitting behavior instead of simple diffusion.

**Taming/shaping the result** was mostly a matter of iterating on a handful of interacting parameters: a **Bright** node scaling the velocity down (e.g. ×0.1) to slow an otherwise-too-hectic simulation; additional **blur passes** after the multiply step (too little blur = chaotic/noisy result, too much = shape dissolves — there's a sweet spot); a **Max** (or **Min**) composite between the original shape/color and the evolving simulation to keep re-seeding/retaining the base shape each step rather than losing it entirely to the feedback (Max gives rounder "bubbly" results, Min gives sharper/more angular splits); a **Remap** node with a custom curve shape applied to the curvature or velocity response to bias how aggressively the effect kicks in; and, called out explicitly as a key missing piece that improved the whole setup once added, **normalizing the incoming velocity vector** before use. **Sub-steps** on the Flow solver can be raised for a more resolved (but slower) simulation. Grid resolution can be pushed higher (e.g. toward 4K) at a performance cost. **Pixelating** the input before deriving curvature produces a distinct blocky/faceted variant of the splitting pattern instead of smooth organic bubbles. Swapping the curvature source for **animated procedural noise** (with added contrast/clamping, e.g. a Perlin-family noise) instead of shape-derived curvature produces a different, more patterned family of results. Additional **velocity contributions** (e.g. UV-space motion, made fairly strong, optionally animated) can be added into the mix before the multiply step for extra directional motion in the result. A **Bright** node offset (shift the value, e.g. by 0.1 on one channel) can double as crude **gravity**, biasing the whole field to drift in one direction over time. The same underlying idea (curvature → multiply into velocity) is noted to work equally well on ordinary "normal inflection" style effects, not just this recursive-splitting look.

Several finished example setups are shown with only the curvature source/mode changed: a "floating particles that split and leave trailing strings" look (driven mainly by the sharpen + final remap settings), and an "outline-based, mean + convexity curvature" variant where the shape both contracts inward and pushes outward simultaneously, producing a self-competing, splitting-yet-reconverging pattern (sometimes needing the curvature to be **inverted** depending on mode, to get the desired direction of the effect).

### Key Steps
1. Build an SDF shape (any shape), convert to mono, feed into a **Flow** solver.
2. Derive a base velocity: blur the mono shape, run it through **Slope Direction** (angle 180), plug into the Flow solver's velocity input.
3. Feed the flow's evolving output into a **Curvature** node (try Finite Difference, or Mean + Concavity/Convexity) to get a concave/convex field.
4. Blur the curvature output (to graduate the values), then sharpen/gain it (to make the structure clearly visible).
5. **Multiply the curvature field with the velocity** — this is the core feedback step that produces recursive splitting behavior.
6. Slow the result with a Bright node scaling velocity down (e.g. ×0.1); add extra blur after the multiply to reduce chaotic noise.
7. Composite the evolving result against the original shape/color with **Max** (rounder/bubblier) or **Min** (sharper) to keep re-seeding the base shape each step.
8. Use a **Remap** with a custom curve to bias how the curvature/velocity response behaves.
9. **Normalize the velocity vector** before it's used — called out as a key fix that meaningfully improved the whole setup.
10. Tune sub-steps (quality vs. speed) and grid resolution (up to ~4K, at a performance cost) as needed.
11. Explore variants: pixelate the input for a blocky look, swap in animated noise instead of shape curvature for a different pattern family, add extra UV-based velocity contributions for more motion, or offset a channel via a Bright node for crude gravity.

### Houdini Nodes / VEX / Settings
Copernicus (COPs) context inside a `copnet`. **SDF Shape** (mono conversion), **Flow** solver (velocity input, sub-steps, closed/open border behavior), **Slope Direction** (angle parameter, e.g. 180, for deriving a directional field from a gradient), **Curvature** node (modes: Finite Difference, Mean, Concavity/Convexity; optionally inverted depending on mode), **Blur** (used at multiple stages — on the base velocity source, on the curvature field, and after the velocity×curvature multiply), **Sharpen** / **Gain** (making subtle curvature values visible), **Multiply** (velocity × curvature — the core feedback operation), **Bright** node (scaling velocity for speed control; also repurposed with a channel shift for crude gravity), **Max** / **Min** composite (blending the evolving sim against the original shape — rounder vs. sharper results), **Remap** (custom curve shaping the response), vector-normalize step (on the incoming velocity — flagged as important), **Pixelate** (blocky variant), animated procedural noise (alternate curvature-field source, e.g. Perlin/"Berlin"-family), extra UV-based velocity contributions (added pre-multiply for motion).

### Difficulty
Advanced — not because any single node is complex, but because the technique is a feedback system with several interacting parameters (blur amounts at multiple stages, multiply strength, remap shaping, normalization) that must be tuned together by iterative visual feedback; the source video itself is presented as live experimentation rather than a settled recipe.

### Houdini Version
Not stated on screen; Copernicus (COPs) context places this at Houdini 20.5+.

### Tags
copernicus, cops, flow-solver, curvature, recursive-simulation, feedback-loop, sdf-shape, slope-direction, procedural-smoke, splitting-pattern, noise-driven

---

## Related Tutorials
- [Houdini COPs Datamoshing HDA](houdini-cops-datamoshing-hda.md) — shares the Copernicus (COPs) 2D context and a feedback-loop-driven advection/motion technique, applied there to video pixel displacement rather than a self-modifying flow simulation.
- [Houdini COPS Distortion | breakdown & project file](houdini-cops-distortion-breakdown-project-file.md) — shares the Copernicus (COPs) 2D context for procedural image-space effects driven by derived fields (position/curvature) rather than plain noise.
