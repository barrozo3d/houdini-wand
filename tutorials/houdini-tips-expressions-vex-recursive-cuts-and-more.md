---
title: Houdini Tips | Expressions, VEX, Recursive Cuts and more
source: YouTube
url: https://www.youtube.com/watch?v=2Vw6jvHrnBw
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, uv, vellum, cops, expressions, procedural, tips, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini Tips | Expressions, VEX, Recursive Cuts and more

**Source:** [YouTube](https://www.youtube.com/watch?v=2Vw6jvHrnBw)
**Author:** cgside
**Duration:** 11m35s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### nprimsgroup Expression [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'll share a few tips and tricks
[0:05] that are not so obvious let's say that I would like to share with you. So the
[0:13] first issue I have in this particular object is that in this extrude side, this
[0:21] part here I have a big chunk of UVs like this a big strip and I would like to
[0:30] divide it into sections. So instead of splitting the geometry and the UV separately
[0:40] we can do the following. We can take a group range and target as a base group
[0:51] that particular those particular polygons and then we can select let's say two
[0:59] out of N-prims and divided by five let's say and as you can see the N-prims in
[1:09] here if I just say N-prims is taking all the prims from the object and not the
[1:18] prims on this base group. So if you want to target that base group you want to
[1:25] use another expression which is N-prims group and say zero and the group is
[1:34] extrude side and then now it's targeting those that particular group and we
[1:45] can divide it by five and we get this pattern. So this is quite useful because we
[1:53] can as you can see I have the same in here then I can promote it to edges group
[1:59] expanded and we have the seams that we can fit to a UV flatten and rectify it and
[2:08] then we end up with the UVs like this as you can see which is much cleaner.


### Recursive Cuts [2:19]
**Transcript (timestamped):**
[2:19] So for this one I would like to show you how I did this let's call it recursive
[2:27] cuts that I did with clip node. So let's go through the setup. I have here a simple
[2:36] example that I will be sharing on Patreon along with other example files that
[2:42] you will see in this video. So as you can see I have the amount of iterations and
[2:49] a seed and more or less mimics the same behavior of this one in here. So this is
[3:02] actually pretty simple. I have an initial mesh which is just one single
[3:10] primitive and then in here I am creating a forage loop by using fetch feedback
[3:25] and by count so you can pick the amount of subdivisions you will have and I'm
[3:34] starting by measuring the area and promoting it to a max area so I can check
[3:42] the largest primitive then I'm grouping that largest primitive then in here I'm
[3:49] scattering a point somewhere in the middle of the largest primitive and I'm also
[3:58] randomizing the normals so I can have a random direction just by setting it to
[4:07] inside sphere and randomizing the normal and using the iteration as a seed as a
[4:16] global seed plus a seed that I have defined in this null and then in the clip
[4:24] nodes which is where everything happens I am clipping and setting the origin to
[4:33] the position of that specific point as you can see this point is in here this
[4:39] scatter point and so I'm using the position position x, y and z and in the direction
[4:50] I'm using the normals as you can see normal x, y and z and this happens for an x
[4:58] amount of times and you always get this look of recursive subdivision let's say or
[5:07] recursive clip so it's actually pretty simple but that is not so obvious out of
[5:15] the box let's say so yeah that's how I did that and at the end I got something
[5:25] like this so as you can see in here I have these curves and I'm doing a polybridge and


### Delete curves with vex (prim intrinsic) [5:29]
**Transcript (timestamped):**
[5:39] I'm left with these with the curves along the geometry and I would like to remove it so
[5:45] I can remove it with a blast and blast just primitive 0 and 1 but that might not be
[5:54] always the case and I can always group them so I am grouping in here so I'm
[6:04] grouping the curves in here I just have one but then when I copy they will be in the
[6:10] same group as you can see curves and I can just blast the curves after the bridge but
[6:19] sometimes you might not have that luxury so what we can see in here in the polybridge if we
[6:27] go to the attributes or the geometry spreadsheet and go to primitives and select in trains x and close
[6:36] you can see the primitive 0 and 1 which are the curves have an open attribute let's say or in
[6:46] the closed is set to 0 so what we can do is an attribute wrangle remove those curves by using
[6:54] this if premium trains it closed premium number is equal to 0 we can remove those frames so that's
[7:04] how you can remove leftover curves from the geometry and this particular suggestion came from
[7:14] Fanoliz on discord so thank you a lot for that okay for this particular digital asset which is


### Res expression from cops [7:18]
**Transcript (timestamped):**
[7:23] pretty simple just takes an image and resizes a plane to fit the same resolution while keeping it
[7:32] in the 0 to 1 range so this is actually the way I'm doing this is pretty simple basically I'm
[7:43] reading an image in a copnet then in the grid I am taking as the x size the res which is the
[7:55] resolution of the the copnet and taking the x resolution so the width and multiplied by 1
[8:07] divided by the x resolution so the the the second part just helps helps me to keep the ratio
[8:16] of 0 to 1 and then for the y is just the same thing but in this case the y-rays and multiply
[8:26] by 1 divided by the x resolution or the width so the height and width and this way we can get the
[8:35] same ratio of an image taken from the copnet you only can you only can do it through a copnet
[8:46] so to to read the resolution you can't really read it in a UV quickshade or attribute from Mac
[8:55] so yeah so in here I'm creating this pillow effect and for that I am welding two pieces of clothes


### Class attribute in vellum ballon setup [8:56]
**Transcript (timestamped):**
[9:07] that are almost touching each other they are actually touching on the unshared edges so I'm welding
[9:17] those unshared edges as you can see I'm shared back and I'm shared front and I'm configuring
[9:28] I am using a configure balloon in the first place but if I set it to the default settings which is
[9:37] from connectivity and I test it now you can see the result is quite different it goes all over
[9:50] the place and even can rush your audience session so let's just wait another frame and as you can
[9:59] see this is all messed up let me cancel this and the reason is when you have two pieces of clothes
[10:12] and they are not in the origin this can cause you a lot of issues so what you can do is say
[10:22] Odini that these two pieces of clothes are part of the same the same piece let's say so what you can
[10:32] do is just use an i-at class equals to one just say that they have the same class as you can see
[10:41] instead of two and in the valum pressure just set when you say define pieces instead of from
[10:51] connectivity just use from attributes and specify the class attribute and then when you assimilate it
[11:01] you will have more predictable results as you can see it's not exploding all over the place like
[11:10] before so yeah guys that's basically what I wanted to share today hopefully you picked up a few tips
[11:20] don't forget you can always grab sample files from my patreon along with exclusive tutorials and
[11:30] yeah see you next time thank you



---

## Captured Frames

- [0:20] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_000.jpg
- [1:50] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_001.jpg
- [3:00] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_002.jpg
- [5:10] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_003.jpg
- [6:30] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_004.jpg
- [7:50] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_005.jpg
- [10:00] tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/frame_006.jpg

---

## Structured Notes

### Core Technique
Five non-obvious tricks: the **`nprimsgroup()`** expression (vs. plain `nprims()`) for correctly dividing Group Range selections scoped to a specific group, a **Fetch-feedback recursive Clip loop** for generating fractured/shattered-looking cuts, cleaning up leftover open curves from a Poly Bridge via a **primitive intrinsic (`closed`)** VEX check, reading a COPs image's actual resolution to size geometry in a proper 0-1 aspect ratio (only possible from inside a CopNet), and fixing exploding/unstable **Vellum balloon** simulations on multi-piece cloth by manually setting a shared `class` attribute instead of relying on Configure Cloth's default Connectivity-based piece detection.

### Summary
**`nprimsgroup()` expression:** when using Group Range to select "every Nth primitive" within a specific base group (e.g. a strip of extruded side faces you want to subdivide for cleaner UVs), the natural-seeming `nprims()` expression actually counts *all* primitives in the whole object, not just the target group — producing wrong divisions. The fix is **`nprimsgroup(0, "group_name")`**, which correctly scopes the primitive count to just that named group, letting a `nprims / 5`-style expression divide the group evenly; the resulting selection is promoted to an edge group, expanded, and fed to UV Flatten + Rectify for a much cleaner UV layout than one giant unsplit strip. **Recursive Clip cuts:** a shattered/fractured look is built from a single starting primitive inside a **Fetch (feedback-by-count)** for-each loop: each iteration measures primitive Area, promotes to find the max-area piece, groups that largest primitive, scatters one random point on it (position randomized "inside sphere" with a randomized normal, seeded by iteration + a user-defined seed), then a **Clip** node uses that scattered point's position as its clip origin and its random normal as the clip direction — repeated for N iterations, this always produces a natural-looking recursive subdivision/shatter pattern, always cutting the currently-largest remaining piece. **Cleaning leftover curves via intrinsic:** after a Poly Bridge, leftover 1D curve primitives can remain mixed in with the bridged geometry; rather than a fragile `Blast primitive 0,1` (which breaks if primitive numbering changes) or manual grouping, check the **primitive intrinsic `closed`** (visible in the geometry spreadsheet's Intrinsics tab) — open curves read `closed == 0` — and remove them in a wrangle via `if (primintrinsic(0, "closed", @primnum) == 0) removeprim(0, @primnum, 1)`; a technique suggested by a Discord community member. **Resolution-aware grid from COPs:** Houdini can't read an image's pixel resolution from a UV Quick Shade or Attribute from Map — the *only* way is inside a **CopNet**: load the image, then size a Grid's X using the COPs `res` (resolution) expression's X component multiplied by `1/x_resolution` (to normalize into a 0-1-ratio-preserving size), and the Y size using the Y resolution similarly multiplied by `1/x_resolution` (not `1/y_resolution`) so the aspect ratio is preserved correctly relative to width — giving a plane exactly matching the image's real aspect ratio. **Vellum balloon/pillow class-attribute fix:** for a pillow-style setup welding two separate cloth pieces together at their touching unshared edges, the default **Configure Cloth "Define Pieces: From Connectivity"** setting can produce wildly unstable/exploding simulations when the two pieces aren't centered at the world origin — even crashing the session. The fix: manually set `i@class = 1` (same class value) on both pieces so Houdini treats them as one balloon "piece" instead of two, then in Configure Cloth's Pressure constraint, switch **"Define Pieces"** from "From Connectivity" to **"From Attribute"** and specify the `class` attribute — producing a stable, predictable simulation instead of chaotic mass explosion.

### Key Steps
1. **Diagnose the wrong expression:** using Group Range's Select-Amount field with `nprims / 5` on a base group of extruded side faces divides based on the *entire object's* primitive count (via `nprims()`), not the group's actual count — producing an incorrect, misaligned split.
2. **Fix with `nprimsgroup()`:** replace `nprims()` with **`nprimsgroup(0, "extrude_side")`** (referencing the actual base group name) so the primitive count used for the division expression is correctly scoped to just that group.
3. **Clean UVs from the corrected split:** promote the resulting primitive selection to an edge group, Group Expand it to get full seam loops, feed to **UV Flatten + Rectify** for a properly divided, clean UV layout instead of one large unsplit strip.
4. **Recursive-clip loop setup:** start from a single-primitive mesh; build a **Fetch (feedback, by count)** for-each loop where the iteration count controls how many recursive cuts occur.
5. **Find and group the largest remaining piece each iteration:** **Measure** (Area) per primitive, promote to find the max area, **Group** that largest primitive so subsequent steps only operate on it.
6. **Scatter a random clip point:** scatter one point on the grouped largest primitive with a randomized position ("inside sphere" distribution) and randomized normal, seeded from the loop's iteration number plus a user-defined global seed (read from a Null) for reproducible-but-varied results.
7. **Clip using the scattered point:** feed the scattered point's position as **Clip**'s origin and its random normal as the clip direction — repeating this each iteration always cuts through the current largest piece, producing a natural recursive fracture/shatter look after N iterations.
8. **Bridge and clean up leftover curves:** after using **Poly Bridge** on the fractured pieces' boundary curves, leftover open curve primitives remain in the geometry; rather than a fragile `Blast primitive 0,1` or manual grouping, check each primitive's **`closed`** intrinsic (Geometry Spreadsheet → Intrinsics tab) — curves read `closed == 0`.
9. **Remove via intrinsic-check wrangle:** `if (primintrinsic(0, "closed", @primnum) == 0) { removeprim(0, @primnum, 1); }` — robustly removes leftover curve primitives regardless of their actual primitive numbers.
10. **Read image resolution in COPs:** load an image into a CopNet; use the COPs **`res()`** expression to read the image's pixel resolution — this is the *only* place resolution is queryable (not available via UV Quick Shade or Attribute from Map on a SOP-side mesh).
11. **Size a Grid to match image aspect ratio:** set the Grid's X size to `res(...).x * (1 / res(...).x)`-style expression (normalizing to a 0-1 base), and Y size to `res(...).y * (1 / res(...).x)` (dividing by the **X** resolution, not Y, to correctly preserve aspect ratio relative to width) — producing a plane matching the image's true proportions.
12. **Diagnose unstable Vellum balloon sim:** weld two separate cloth pieces (e.g. front/back of a pillow) at their touching unshared edges; with **Configure Cloth**'s Pressure constraint left at default "Define Pieces: From Connectivity," the sim can go wildly unstable/explode (and even crash the session) if the two pieces aren't centered at the world origin.
13. **Fix with a shared class attribute:** set `i@class = 1` (an identical value) on both cloth pieces via a wrangle so Houdini treats them as a single connected balloon piece rather than two independent ones.
14. **Switch Configure Cloth to attribute-based pieces:** in the Pressure constraint's "Define Pieces" parameter, switch from "From Connectivity" to **"From Attribute"** and specify the `class` attribute — produces a stable, predictable simulation instead of chaotic explosion.

### Houdini Nodes / VEX / Settings
Nodes/expressions: Group Range (`nprimsgroup(0, "group_name")` vs. plain `nprims()`), Group Promote, Group Expand, UV Flatten, Rectify, Fetch (feedback, by-count for-each loop), Measure (Area), Group (largest-piece selection), Scatter (inside-sphere position randomization, randomized normal, iteration+seed-based random seeding), Clip (position + direction driven by a scattered point's attributes), Poly Bridge, Attribute Wrangle (VEX: `primintrinsic(0, "closed", @primnum)` check + `removeprim()`), CopNet `res()` expression (image resolution, X and Y components), Grid (resolution-driven X/Y size expressions), Configure Cloth (Pressure constraint, Define Pieces: From Connectivity vs. From Attribute), Attribute Wrangle (VEX: `i@class` assignment for shared-piece grouping), Vellum Solver.

### Difficulty
Advanced — each tip solves a genuinely non-obvious Houdini gotcha (scoped-group expressions, primitive intrinsics, COPs-only resolution access, Vellum piece-definition pitfalls) that assumes solid procedural and simulation fundamentals.

### Houdini Version
20.5 (UI matches Houdini 20.5-era toolset; Vellum Configure Cloth pressure/pieces workflow consistent with current versions).

### Tags
#vex #uv #vellum #cops #expressions #procedural #tips #advanced

---

## Related Tutorials
Cross-link with groups-patterns-in-houdini.md (same author, overlapping group/expression-selection vocabulary) and houdini-tips-and-tricks-2.md (shares the Connectivity-based class-attribute pattern) once indexed together.
