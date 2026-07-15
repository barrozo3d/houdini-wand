---
title: Ruins randomized brick wall
source: YouTube
url: https://www.youtube.com/watch?v=QEvlyVTk4Jw
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.593"
tags: [voronoi-fracture, vex, procedural-modeling, bricks, ruins, environment, connectivity, compile-block, texturing]
extraction_status: complete
frames_dir: tutorials/frames/ruins-randomized-brick-wall/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Ruins randomized brick wall

**Source:** [YouTube](https://www.youtube.com/watch?v=QEvlyVTk4Jw)
**Author:** cgside
**Duration:** 10m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So today I wanted to share with you how I created
[0:06] this broken stone wall with enough variation on the bricks alignment. So I started
[0:17] with a box and this is my initial shape. Then I created this curve that will
[0:31] act as the breaking pattern or the bullion pattern that I'm doing right here.
[0:39] Then this is my input mesh. And from here I am creating some curves. One for the y-axis,
[0:53] one for the x and one for the z. I'm doing that with extracting it from bounds of my input mesh.
[1:03] So then as you can see if I do a Voronoy fracture and see the attribute name, we are creating slices along
[1:16] the geometry. So in order to do that we have the ads. Then I am re-sampling. So I can choose how many
[1:32] sections I will have in this case in the y-axis. Then I am grouping the inner points and jittering
[1:42] those inner points. So I don't get the ends jittered. Then I'm cutting every points. So I create
[1:55] segments. Then having those individual segments I can subdivide. So this way the individual sections
[2:11] will have a consistent amount. If I disable the jitter you can see that they are in the perfectly
[2:21] distributed. So I'm subdividing just one subdivision. Then fusing the points, sorting them in this
[2:38] case in y and grouping the middle points or the every other point and blessing those. And in the
[2:52] end we just set to have the middle points that will be used to do the fracturing. As you can see
[3:09] this is the first level of fracturing. In this case we don't need a loop because we want to
[3:14] randomize it. So then I am going to disable this one and enable this fracturing. So right here I am
[3:29] using a Voronai fracture in a loop. This way I can randomize the jittering of each line. So we have
[3:41] this line here that we are doing exactly the same. But the difference is that I'm using the
[3:49] detailed iteration attributes and a seed value to randomize each layer of fracturing.
[4:02] So if I disable the jittering we will have straight lines like this. This way we are randomizing
[4:12] the position of each brick. Then I'm doing exactly the same for the Z axis. So as you can see here
[4:25] and I can always come back and change the amount of sections.
[4:43] In this case I want 29 and I can do the same here. Make the bricks longer
[4:57] and the same in the Z axis. Then right here I am using an exploded view just to separate the bricks
[5:06] a little bit. This will help for the Boolean and also visually to have some separation between the
[5:14] bricks. Then I am Boolean out a shape. They can from the initial shape and doing a fracture
[5:28] and cleaning it. We end up with something like this that we can use to Boolean.
[5:41] And then I am saving the B inside A from the Boolean output. So I can affect those inner polygons.
[5:54] Then I am creating a connectivity attribute to have an individual piece for each brick.
[6:06] And I am transforming a bit. I am rotating a bit randomly the individual bricks with a
[6:16] transform node. I can set the amount and I also have a seed just with a feed function.
[6:29] And I am creating a attribute here called inside bricks. Just using the fracture bricks group.
[6:41] And then I am blurring the attribute and I am also remapping. So I can use it here in the edge
[6:50] damage or ship edge damage that can be compiled. Basically doing a remesh. First measuring the area of
[7:01] the brick so I can remesh based on the size of the brick as you can see here.
[7:10] Then I am blurring a bit the edges. And as a way to attribute I am using that same inside bricks
[7:25] attribute. And I am also peaking and basically doing a Boolean. And you can play with the amplitude of
[7:37] the noise of the mountain. And with the peak to have more or less damage.
[7:45] And I am doing that for every brick. And if you compile it it should be fast enough.
[8:00] So we end up with something like this. And we can get rid of the attributes.
[8:07] And as you can see this is the final result with some edge damage.
[8:16] More pronounced along the inside bricks as I call it. And less pronounced in these areas where
[8:24] there is no much fracture. And I am doing that again in the attribute blur with a weight attribute.
[8:33] And in the mountain I am also blending the attribute inside bricks.
[8:40] Then I am just creating a black and white mask. So I can use it for texturing or any other purpose.
[8:50] And that is easy enough. Just doing a randomization of the class attribute. And assigning it to
[9:02] to a color attribute or vector attribute. Or you can just do it with the attribute adjust color
[9:10] by feeding the class attribute in a pattern type set to random.
[9:18] So that's basically it. I hope you have learned something new. And make sure to check out the
[9:24] Patreon file if you want to investigate on your own and do your own version.
[9:29] I also included some other setups like this one.
[9:38] As you can see, something like this, even in regular shapes should do a good job.
[9:45] And this is just the basic setup of the bricks without variation.
[9:51] But the more simplified network. And this is the first approach I tried.
[10:01] Which also works. But only for box like shapes. So thank you and see you in the next one.



---

## Captured Frames

- [1:30] tutorials/frames/ruins-randomized-brick-wall/frame_000.jpg
- [3:10] tutorials/frames/ruins-randomized-brick-wall/frame_001.jpg
- [5:30] tutorials/frames/ruins-randomized-brick-wall/frame_002.jpg
- [6:40] tutorials/frames/ruins-randomized-brick-wall/frame_003.jpg
- [7:50] tutorials/frames/ruins-randomized-brick-wall/frame_004.jpg
- [9:15] tutorials/frames/ruins-randomized-brick-wall/frame_005.jpg
- [10:10] tutorials/frames/ruins-randomized-brick-wall/frame_006.jpg

---

## Structured Notes

### Core Technique
Build a broken stone/brick wall with realistic non-repeating brick alignment by slicing a box into rows/columns/depth via repeated jittered Voronoi Fractures driven per-layer by a for-loop with a seeded random offset, then adding per-brick edge damage via a compiled mountain/peak pass masked by a "fracture boundary" attribute.

### Summary
Rather than a uniform brick grid, the wall is built by extracting bounding-box-derived guide curves along Y, X, and Z, resampling them into sections, jittering the interior points (endpoints preserved), cutting at each point, and subdividing for consistency. The key realism trick is fracturing each "layer" (row) with its own randomized jitter seed inside a for-loop using the detail iteration attribute — producing the classic randomized/staggered brick-alignment look instead of a perfectly uniform pattern. After an Exploded View separation and Boolean-based cleanup, individual bricks get a Connectivity ID, a small random rotation, and a computed "inside bricks" mask (blurred and remapped) that drives Mountain-based edge/surface damage inside a **Compile Block** for speed, concentrated more heavily on interior fracture bricks and less on boundary bricks. A random-per-class color/attribute pass (via Attribute Adjust Color with pattern type Random, randomized by the class/connectivity attribute) finishes the variation, and a black-and-white mask is exported for texturing.

### Key Steps
1. Start with a box as the base wall shape, plus a hand-drawn curve to act as the fracture/breaking pattern for an initial Boolean cut.
2. Extract three guide curves from the input mesh's bounds — one each for Y, X, and Z axes.
3. Run a **Voronoi Fracture** along the guide curves to create slice divisions; Resample controls how many sections per axis (e.g. Y-axis section count).
4. Group the *inner* points of each guide curve (excluding endpoints) and **jitter** only those inner points so the end sections stay clean, then cut at every point to create individual line segments, and **Subdivide** each segment once for consistent point density per section.
5. Fuse points, sort (e.g. by Y), group every-other point (middle points), and blast to isolate just the fracture-guide points that will drive the first level of slicing.
6. First fracture pass: run **Voronoi Fracture** using those guide points — no loop needed here since this pass isn't randomized per layer.
7. Second/randomized fracture pass (the key trick): run **Voronoi Fracture inside a for-loop** so each iteration (row/layer) gets its **own jitter randomization**, driven by the **detail iteration attribute** combined with a seed value — this randomizes the alignment of each layer of bricks independently rather than uniformly. Repeat the same process for the Z axis. Disabling jitter shows straight/uniform lines for comparison.
8. Use **Exploded View** to separate bricks slightly (helps the Boolean and visual clarity), then Boolean the exploded/fractured shape out from the initial wall shape and clean the result; save the "B inside A" Boolean output group to isolate the inner cut polygons.
9. Run **Connectivity** to give each individual brick a unique piece ID, then apply a small **randomized rotation** per brick (with its own seed, via a fit-based random function) using a Transform node.
10. Create an "inside bricks" attribute from the fracture-bricks group, **blur** it, and **remap** it so it can drive a compiled **edge/surface damage** pass: measure each brick's area (to scale the remesh appropriately per brick size), blur edges a bit, and use the inside-bricks attribute to control Mountain-node amplitude and Peak-based Boolean damage per brick, all wrapped in a **Compile Block** for performance since this runs per-brick.
11. The blurred inside-bricks attribute also feeds an **Attribute Blur** weight and a **Mountain** blend, so edge damage is more pronounced on interior/heavily-fractured bricks and less pronounced near clean boundary areas.
12. Create a black-and-white mask attribute from the same setup for later texturing use.
13. Final color variation: randomize the per-brick **class/connectivity** attribute and feed it to **Attribute Adjust Color** with Pattern Type set to **Random**, randomized by the custom class attribute, to color-vary each brick without manual painting.
14. Author also shares a simpler alternative network in the project file that works for regular box-like shapes without the full randomized-jitter variation setup.

### Houdini Nodes / VEX / Settings
Box, Boolean, Bounds-derived guide curves (per-axis), Voronoi Fracture (guide-curve-driven, jittered, and randomized-per-loop-iteration variants), Resample, Group (inner points, exclude endpoints), Jitter, Cut, Subdivide, Fuse, Sort, Blast, For-Each loop (per-layer randomized fracture using detail `iteration` attribute + seed), Exploded View, Boolean ("B inside A" group extraction), Connectivity (per-brick class/piece ID), Transform (randomized rotation per brick, seeded), Attribute Blur, Remap, Measure (area, for per-brick remesh sizing), Mountain (amplitude driven by inside-bricks attribute), Peak, Compile Block (for per-brick edge-damage performance), Attribute Adjust Color (Pattern Type: Random, randomized by class attribute).

### Difficulty
Advanced (the per-layer randomized-fracture-in-a-loop technique and compiled per-brick edge-damage pipeline require solid procedural/VEX fluency).

### Houdini Version
19.5.593 (visible in viewport title bar).

### Tags
voronoi-fracture, vex, procedural-modeling, bricks, ruins, environment, connectivity, compile-block, texturing

---

## Related Tutorials
- [Procedural Rock Wall without intersections](procedural-rock-wall-without-intersections.md) — alternate RBD-simulation-based approach to a similar stacked-stone-wall problem from the same channel.
- [Procedural Bricks with Houdini](procedural-bricks-with-houdini.md) — simpler, non-fractured brick-pattern technique using grid offsetting instead of Voronoi Fracture.
- [Procedural Buildings in Houdini | Tips and Tricks](procedural-buildings-in-houdini-tips-and-tricks.md) — shares the per-layer randomized Voronoi Fracture inside a loop technique, applied there to a domed roof's brickify pattern.
- [Think Procedural Think Houdini](think-procedural-think-houdini.md) — an alternate, from-scratch (no Voronoi Fracture) brick-wall build using Attribute-Adjust-Float profiling and a pcopen()-based growth solver instead.
