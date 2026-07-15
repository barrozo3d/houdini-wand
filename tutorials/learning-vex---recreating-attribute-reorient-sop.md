---
title: Learning Vex - Recreating attribute reorient sop
source: YouTube
url: https://www.youtube.com/watch?v=TAWtLzrITOY
author: cgside
ingested: 2026-07-15
houdini_version: "Not specified"
tags: [vex, matrix, attribute-reorient, custom-function, uv-space, learning-vex, cross-product]
extraction_status: complete
frames_dir: tutorials/frames/learning-vex---recreating-attribute-reorient-sop/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Learning Vex - Recreating attribute reorient sop

**Source:** [YouTube](https://www.youtube.com/watch?v=TAWtLzrITOY)
**Author:** cgside
**Duration:** 13m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video we're going again to another nerdy rant about
[0:05] Vax, which will be basically recreating the attribute reorient with Vax. As you can see,
[0:10] we have a very similar result. Basically we start, I'm gonna do this step by step, but
[0:15] let me just walk you through. So we start with some test geometry, we split the UV seams,
[0:21] create some normals, and we measure the gradient of the position.y, so a value along the
[0:26] Y components, we measure that gradient, we move the geometry to UV space, so we do some
[0:32] sort of space transform between world position and UV space, and after that our attributes, our
[0:38] gradient that was previously oriented along the Y component of the surface is no longer oriented,
[0:44] let's say. So for that we use the attribute reorient and now we have the flow of the Y component
[0:49] of the mesh, as you can see with this gradient. That is easy, but I'm curious, so I wanted to know
[0:55] how I can recreate the sub, which is always useful to know how to recreate some some subs with Vax,
[1:01] and we will do that today, so and let's get started. So we're gonna start with the geo,
[1:09] and let's use the test geometry big, so big, let's not add the shader, like I was telling you,
[1:19] split the UV seams, because we want to move these to UV space and we want the UV,
[1:25] the UV attributes on points, let's also add some normals, because we will use them later,
[1:31] instead of having implicit normals, and let's do the gradient, so measure, gradient, position.y,
[1:42] and we can show points, so let's actually visualize that, let's name it,
[1:47] there, and let's visualize it, so marker vector, what?
[1:57] So marker vector, so that's fine. All right, now what we do, we add your good swap,
[2:07] and we do copy, for example, and choose texture and move it to position, and now let's ignore the normals,
[2:15] but the normals are also a queue, so the normals are no longer updated, as you can see,
[2:20] they are using, that's why we see these weird shading, so if we do attribute reorient,
[2:27] and we take this current geometry, and we will, we connect it to the second input, and we do
[2:36] there, now we have it, and we can also do normal, and the normals are updated, so actually the
[2:41] normals were a nice example to show you, how moving between spaces, we don't get our point
[2:46] attributes updated, so now let's do the nerdy parts, which is recreating this sub, with back,
[2:54] so I'm not gonna even, I'm gonna make my life even more difficult, and not move this geometry
[2:59] to UV space manually, with the attribute swap, so we will do it all inside a wrangle,
[3:05] so let's create an attribute wrangle, and let's name it, let's name it attribute reorient, reorient,
[3:15] let, and we will, the steps are the following, we will need to create a matrix showing the rotation
[3:23] matrix, showing the rotation of all the points, computing the matrix for all the points,
[3:30] regarding the rotation, and we need to compute the matrix also for the, for the UV geometry,
[3:35] and then we take the difference between the two, and we apply that computed matrix to the new
[3:41] geometry to update the attributes I mean, so let's do it step by step, and it will be easier to follow,
[3:48] first of all we need to compute the matrix that shows us how these objects is oriented,
[3:54] or rotate it, not object matrix, like a, just like a single point matrix, we need to compute them
[3:59] for all the points, so let's actually do it, we want to run over points, and first of all we need to
[4:05] make the first matrix, and for that we will need, we will need the current position, the normals,
[4:12] that we have, let's get rid of these, so we will use the normals, and the current position,
[4:17] and a neighbor, so let's start with a neighbor, which will be the first neighbor of the current
[4:22] point we are iterating over, so let's say zero, i, p, t, and the first neighbor, so let's say
[4:30] this point in here, and we just go and grab that point, that point number of the neighbor,
[4:36] so for now we need to create a vector between the current position and that neighbor, so let's do
[4:41] vector, and let's call it u, and we're going to make sure we normalize it, and we take the point
[4:47] expression to grab the position of that neighbor, and we subtract the current position,
[4:54] so that's our first vector, it's just like a vector pointing from the current point to the neighbor,
[5:00] then we're going to create another vector called v, which we're going to normalize also,
[5:05] and can be a cross product between the current normal, and that first vector,
[5:13] so the problem is that we can't make sure this first vector is orthogonal to the normal, so we need
[5:19] to do another cross product, so u, it will be again, we can normalize it just in case, and we just
[5:25] cross between this new cross between this new vector and the normal, and we will visualize this
[5:33] in a bit, so just to make sure we follow, so normalize cross between v and n, what is complaining about?
[5:42] Oh, it's not n, it's v at n, so if we visualize this as a matrix, so let's do matrix for a
[5:50] empty x, is equal to z, and we will do u, v and n, or v at n, 10, v at n, and if we visualize that
[6:03] right now, it will make a bit more sense, so marker and axis, and let's scale it down, so our z
[6:11] axis, as you can see in here, we set it to the normal, so this blue vector is the normal,
[6:17] then we have the x which is u, and we have v which is this green or y component, so this is
[6:24] good starting point, now we need to do this the same thing, but for the uv mesh, and in order to
[6:31] grab the uv mesh, we will just unwrap it in place, so string u, it will be u unwrap, and we take
[6:39] the current geometry and we grab from the uv, so this will give us a pseudo geometry, or we will
[6:45] unwrap it in place, and give us the exact same geometry as this, as you can see, this uv geometry.
[6:53] What we can do now is, for example, we can take the vector, let's say vector uv, so uv position,
[7:02] and we can just read the point position, so instead of typing zero, we type g, we want to access
[7:08] that q, and let's grab the position, and just write within them, so, and now we can just v at b,
[7:14] is equal to uv b, and now we have the uv geometry, so, but we don't want to do this, so the idea now
[7:23] is to do the same matrix computation, but for the uv geometry, but I don't want to do it twice,
[7:32] so I'm going to create a function, which is also a good way to show you how you can create
[7:37] custom functions in Vax, so let's get rid of this, and let's create a function around this, so,
[7:44] let's define the class, so it's a matrix that we want to get, and let's call it a calc matrix,
[7:53] a calc mdx, now we need the arguments, and the arguments, the first one, as you can see,
[7:58] for the second one, we are reading the position of the uv mesh with this string, which is the geo,
[8:06] so as you can see, the string, but for the other ones, we are using a new, new american put,
[8:11] so that will be a problem, we can't just have a string or an integer, so we need to define one type
[8:16] for the input, so I'm gonna define it as a string and call it input, because we can use a trick
[8:24] to instead of using new american put, we can use actually a string, and I'll show you well,
[8:29] then we're gonna grab the normal, and the position, so we can just use a comma,
[8:35] and then we will grab also the point number, so those are our arguments, and let's open the brackets,
[8:45] so we don't have a return, what we want to return at the end is the matrix, and this will error out,
[8:52] so let's, no one step at a time, so let's actually copy this, and paste it inside here,
[8:59] and the neighbor, we will just replace it with input, ptnum, we replace current position,
[9:06] because we can use local variables, so let's replace it with pause, which will be our current
[9:10] position, here we use n, and here we use n, oh I forgot to copy this, and we just define in here
[9:20] and matrix, empty x, and we return the matrix, oh we are using n in here, so let's use n,
[9:26] and now this should be working,
[9:33] let's continue, there might be something we need to do in here after that, so let's now
[9:41] call the function, so first of all we unwrap the geometry, we get the position,
[9:52] and we also get the normal, oh no we don't grab the normal because it will be the same,
[10:00] as the world space normal, so we just set a custom normal along the z axis,
[10:07] because the geometry will be facing, yeah so uvn, the geometry will be facing the z axis as you can see,
[10:14] so we just define it as the normal of our uv mesh, then we will create matrix,
[10:22] rest, empty x, and we will call the function, so call empty x, now we will do it for the world space
[10:30] position, so for that instead of using a numeric input, we will use a string, and we use up input
[10:38] column zero, and then we need to pass the normal, which is the current normal, the current position,
[10:45] and I add bitinum, so let's see if that errors out, no, and then we need to do the same, so matrix
[10:54] uvnth, and it will be the same, call empty x, and we pass the gul, the uvn, the uvp,
[11:07] and we use again i at bitinum, and now if we calculate the difference matrix, so let's call it empty x,
[11:17] and to calculate the difference matrix, we divide one matrix by the other, or you can do the
[11:22] inversion of the rest, empty x, multiplied by the uvnth, and now if we do v at b times it goes empty x,
[11:35] we get all of this mess, because we actually need to also apply the translation on the matrix,
[11:43] so in here, we call back, and we translate, because this is a 4x4 matrix, and we translate the matrix,
[11:51] and we do it by the current position, and now if we apply, we get the geometry, the matrix
[11:59] computed correctly, and we can translate it to the uv position, so now we're simple, so we have
[12:08] let me check, as you can see the normals are still problematic, because they have the other space,
[12:15] the word space normals, so we can just do v at n, multiply equals, and if we do empty x, let's see,
[12:22] that seems correct, somehow, but it's still problematic, because the normal is a vector attribute,
[12:28] and we don't want to translate the normals, so we just apply a matrix 3, so we cast it to a matrix 3,
[12:34] to only apply the rotation, and now the normals are correct, and let's see finally our attribute,
[12:38] which is there, as you can see is all over the place, so if we do the same,
[12:43] we get there, multiply equals by matrix 3 again, so we don't want to apply the translation,
[12:48] and empty x, and now there's something missing in here, so there's actually a bug in our code,
[12:58] because I'm using zero input in here, and we need to use input, sorry about that, and now it's
[13:05] correct, as you can see we successfully translated this locked top into a vex solution,
[13:13] and you might ask why all that work to recreate something that already exists, well, to the
[13:18] precise reason, when you don't have the sub you can create it on your own, so learning all this
[13:25] stuff can help you to come up with your own versions of the sub, or recreate something that
[13:30] doesn't exist by default, that's the power of Aldini, that you can customize it to an extreme level,
[13:36] so yeah, I hope you have learned something from this, please let me know if you have another
[13:41] way of doing this sort of thing, and as always you can grab the files on my Patreon,
[13:47] and let me know what you think in the comments, thank you, and I'll see you next time.



---

## Captured Frames

- [0:10] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_000.jpg
- [1:47] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_001.jpg
- [2:36] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_002.jpg
- [6:03] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_003.jpg
- [7:28] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_004.jpg
- [11:35] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_005.jpg
- [12:05] tutorials/frames/learning-vex---recreating-attribute-reorient-sop/frame_006.jpg

---

## Structured Notes

### Core Technique
Recreate the built-in **Attribute Reorient** SOP entirely from scratch in a single VEX wrangle — building a per-point local rotation matrix (from position, normal, and a neighbor point), computing that same matrix for both the "rest" (original 3D) and "deformed" (UV-space-unwrapped) versions of a mesh, and applying the **difference matrix** between the two to correctly re-orient any point/vector attribute (like a measured gradient) that was computed in one space but needs to remain meaningful after the geometry is moved into a different space (e.g. flattened to UV space for texturing).

### Summary
The motivating problem: measuring the **gradient of `P.y`** on a 3D mesh gives a vector attribute that correctly "flows" along the surface's Y-height direction — but if that mesh is then moved into UV space (via Attribute Swap, copying UV into position), the gradient vectors no longer make sense relative to the new flattened shape, since they were computed for the original orientation. The stock **Attribute Reorient** node fixes this automatically (also demonstrated fixing implicit/point normals that go stale after the same UV-space move), but the video's real goal is reconstructing that fix by hand as a VEX learning exercise. The core insight is that **every point can be given a local 3×3 rotation matrix** by building three orthonormal basis vectors: `u` = a normalized vector from the current point to a neighboring point (found via `neighbour(0, i@ptnum, 0)`), `v` = a normalized cross product between the surface normal and `u`, and then `u` is recomputed as `normalize(cross(v, n))` to guarantee true orthogonality against the normal (since the initial `u`-to-neighbor vector isn't guaranteed perpendicular to the normal) — assembling `u`, `v`, and `n` into a `matrix3` and visualizing it directly with the Marker/Axis vis-type confirms the three basis vectors align with the local surface directions. This matrix-building logic is then wrapped in a **custom VEX function** (`matrix3 calc_mtx(int input; vector pos, n; int ptnum)`) to avoid duplicating the code for both spaces — a "current point's real neighbor" version for the 3D mesh, and a UV-space version built by first `unwrap()`-ing the geometry in place (`geo = unwrap(0, "uv")`) to get a pseudo-geometry matching the UV layout, then manually setting the normal to a flat `{0,0,1}` (since the unwrapped mesh always faces +Z) rather than using the real surface normal. Both the "rest" matrix (3D world space) and the "UVn" matrix (UV/flattened space) are computed via the same function call, and the **difference matrix** is obtained by multiplying the inverse of the rest matrix by the UV-space matrix (`invert(rest_mtx) * uvn_mtx`) — this represents exactly the rotation needed to go from the original orientation to the new one. Applying that difference matrix directly to position causes garbled results because it's a 4×4 matrix carrying translation as well as rotation, so the matrix must first be explicitly translated by the current point's position (`translate(diff_mtx, @P)`) before being applied to `P`; the geometry then correctly lands at the UV position. Normals require a further fix: since normals are directional vectors (not positions), applying the full 4×4 difference matrix also incorrectly translates them, so the matrix is cast down to a **`matrix3`** (rotation-only, `matrix3(diff_mtx)`) before being applied to `N` — after which the previously-garbled normals display correctly. The same `matrix3`-cast difference matrix is then applied to the originally-measured gradient attribute, correctly re-orienting it to match the new UV-space geometry — reproducing the stock Attribute Reorient SOP's behavior with fully custom, from-scratch VEX. A late bug is caught and fixed live: an early version of the function accidentally referenced input `0` (hardcoded) instead of the `input` parameter, which silently broke the UV-space matrix calculation until corrected.

### Key Steps
1. Set up a test mesh with **Split UV Seams** (get UV as a point attribute) and add **Normal** (explicit, since UV-space transforms will make implicit normals stale).
2. **Measure** the gradient of `P.y` and visualize it as a marker/vector — this is the attribute that will need re-orienting later.
3. Demonstrate the problem: **Attribute Swap** UV into position moves the mesh to UV space, but the previously-computed gradient (and implicit normals) no longer make sense; show the stock **Attribute Reorient** node fixing both by feeding it the pre-move geometry as a second input.
4. In a single wrangle, build a **local rotation matrix per point**: `u = normalize(neighbor_position - P)` (via `neighbour(0, i@ptnum, 0)`), `v = normalize(cross(N, u))`, then re-derive `u = normalize(cross(v, N))` to guarantee orthogonality; assemble into a `matrix3` (columns/rows = u, v, n) and visualize with Marker/Axis to confirm correctness.
5. Wrap this logic in a custom function `matrix3 calc_mtx(int input; vector pos, n; int ptnum)` — VEX functions can't take arbitrary geometry-input types directly, so the geometry input is passed as a **string** (`"0"` or `"1"`-style op-input syntax) rather than a numeric literal.
6. Compute the **"rest" matrix** by calling the function against the original (world-space) geometry using the current point's real position, normal, and point number.
7. Compute the **"UVn" matrix** for the flattened geometry: build a pseudo-geometry via `geo = unwrap(0, "uv")`, manually set its normal to `{0,0,1}` (since unwrapped geometry always faces +Z, not the real surface normal), then call the same function against it.
8. Compute the **difference matrix**: `invert(rest_mtx) * uvn_mtx`.
9. **Translate** the difference matrix by the current point's position (`translate(diff_mtx, @P)`) before applying it to `P` — applying the raw (untranslated) 4×4 matrix produces garbled geometry since the 4×4 form also carries translation.
10. Move the geometry into UV space by setting `P` from the UV attribute, then apply the difference matrix (cast down to a rotation-only **`matrix3`**) to `N` — a bare 4×4 matrix would incorrectly translate the normal vectors, so casting to `matrix3` restricts the operation to rotation only.
11. Apply the same `matrix3`-cast difference matrix to the originally-measured gradient attribute, correctly re-orienting it to the UV-space geometry, matching the stock Attribute Reorient SOP's result.
12. Debug note: watch for accidentally hardcoding an input index (e.g. `0`) instead of using the function's `input` string parameter — this silently breaks the second matrix calculation.

### Houdini Nodes / VEX / Settings
Split UV Seams, Normal, Measure (gradient of `P.y`), Attribute Swap (UV→position), Attribute Reorient (stock reference node), point wrangle (`neighbour()`, `normalize()`, `cross()`, `matrix3` construction), Marker/Axis visualization, custom VEX function definition (`matrix3 calc_mtx(...)`, string-typed geometry-input parameter), `unwrap()` (UV pseudo-geometry), `invert()` (matrix inversion), `translate()` (4×4 matrix translation), `matrix3()` cast (rotation-only application to vectors/normals).

### Difficulty
Advanced (building a from-scratch local-basis rotation matrix per point, wrapping it in a custom VEX function usable across two different geometry inputs, and correctly distinguishing 4×4 vs. 3×3 matrix application for positions vs. directional vectors are all non-trivial VEX/math concepts).

### Houdini Version
Not specified.

### Tags
vex, matrix, attribute-reorient, custom-function, uv-space, learning-vex, cross-product

---

## Related Tutorials
- [Vex Problem Solving in Houdini](vex-problem-solving-in-houdini.md) — shares this channel's from-scratch VEX-first problem-solving philosophy applied to a different node-recreation problem.
- [Why you need to learn vex in Houdini #1](why-you-need-to-learn-vex-in-houdini-1.md) — shares the same "recreate it from scratch to really understand it" VEX-education philosophy.
- [Tips and tricks in Houdini 21](tips-and-tricks-in-houdini-21.md) — shares the axis-extraction-from-matrix and look-at-based transform-matrix techniques used here.
