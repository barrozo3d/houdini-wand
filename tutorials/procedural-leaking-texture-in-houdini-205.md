---
title: Procedural Leaking Texture in Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=8iK3GD3yeCE
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.170"
tags: [cops, curvature, vex, dot-product, uv-gradient, weathering, decay, procedural-textures, karma]
extraction_status: complete
frames_dir: tutorials/frames/procedural-leaking-texture-in-houdini-205/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Leaking Texture in Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=8iK3GD3yeCE)
**Author:** cgside
**Duration:** 10m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'll be showing you how I created
[0:06] this procedural leak mask. I have done this previously by using a simulation but
[0:13] this time I will be showing you how to do it with Cops and some simple
[0:20] Vax. So yeah let's get started. So I will be showing you the workflow in some
[0:28] simple geometry so it's easier to follow along. So basically I'm starting with
[0:35] the box, did some extrusion, to create some windows and this inner extrusion.
[0:42] Added some normals in this case point normals and subdivided the mesh because
[0:49] the next thing we're going to do is to measure the curvature and for that we
[0:54] need some resolution unfortunately because we don't have these nodes at
[1:01] shading level. So now we have the convexity and also the concave areas which
[1:12] will help us to create the leak mask. So or the leak origin let's say where it
[1:21] should streak down. So basically we won't leak on these areas here, here at the
[1:30] bottom of the windows and also here and on the top. And for that we need to do
[1:37] some mixing of attributes and we have almost everything we need. Now we just
[1:43] need two directional masks. In this case using the dot product between the
[1:50] normal and an up vector in this case the Y. So here's the first one so all the
[1:59] faces, all the frames facing up and we have a second one which all the
[2:06] frames facing down. And from here we just mix both the both directional masks
[2:16] with the convexity and with the concavity. And in the end we end up with this
[2:22] mask. So I'm not an expert on this but this looks like where the legs should
[2:29] start at least in a conceptual way but I'm open to suggestions. So next we create
[2:43] some normals on the vertices and create a p-scale attribute. It's like a
[2:50] natural bit randomized for each of the points that we will scatter on these
[2:56] areas. So we have bigger and smaller legs but we will see that in a bit. Then
[3:04] I'm creating also two masks on at the vertices level because I want them to be
[3:12] super sharp as you can see. So this one at the bottom, using again the dot
[3:17] product is the same workflow and one at the top. As you can see they are super
[3:24] sharp because they are on the vertices. Then I'm unwrapping. So let me just get rid
[3:33] of this. I'm just creating a UV unwrap and these are my UVs. And you notice
[3:43] that all the UVs are super well aligned and this will not create some
[3:54] possible issues. If we feed other type of geometry where we have UVs facing
[4:01] sideways and upside down and so on. So basically we need a natural boot that
[4:07] tells us which way is down. So where the legs should streak down. So for that
[4:15] just to simulate that problem, that problem of the UVs facing other
[4:21] directions, I'm selecting your set of primes, assigning a new color and
[4:29] transforming it, rotating it upside down as you can see. And now we will create
[4:42] a natural boot, a mask that goes from top to bottom. So a gradient as you can see
[4:51] in this by using the relative point bounding box. If I remove this as you can
[4:58] see this is from 0 to 1. And now we need to transform this to UV space. So I'm
[5:09] splitting the UV seams and promoting to a point attribute the UVs and placing them
[5:18] assigning the UV to the position. And we can just remove the visualization. And as
[5:26] you can see this face right here if I showed the attribute again. As you can see
[5:34] is not from white to black as it should be. As you can see this is the front
[5:43] space. This one is slightly darker to white so it's upside down. And the idea
[5:51] here suggested by Swalsh on the CGWiki Discord which I am very grateful is to
[5:59] measure that the gradient of that mask that we created. And if I show you that
[6:09] so mask white and we have here the gradient white. And as you can see this
[6:18] particular face the vector is pointing down because we rotated it. So if I
[6:28] remove this UV transform you can see what is doing. And this is what we want to
[6:35] orient our streaks which we will do next. So the idea now is to scatter some
[6:42] points on that mask that we created with the convexity and directional masks.
[6:51] And we create the attributes in this case the normal since we want to orient
[6:58] the the streaks. In this case I am using the gradient white and setting the
[7:05] up along the z and moving into cops. We can start by importing the points and
[7:15] resturizing the setup so we can move it from negative one to one which is the
[7:22] space that the cops operates. And creating an SDF shape let me resize this. In
[7:31] this case I am just using a line and creating this streak. And converting it
[7:38] to mono, transforming it a bit. And I am just stamping the points. And as you can
[7:44] see that particular tile if you remember it's upside down and the leaks are
[7:51] facing this direction, the up direction. And that's because we have that
[7:58] normal attributes that we just created in here. With that gradient we measured.
[8:08] So this is basically done. Now we just use those masks if you remember that we
[8:16] created the vertex two vertex masks with the top and bottom faces our frames. We
[8:24] maximise the two attributes in words and multiply over those areas as you can
[8:32] see is removing some streaks we don't want. Then we can for instance use the
[8:41] streaks blur, streaks blur, invert it in this case and just preview it. And here we
[8:49] have the final result which is the streaks. And they are obviously two uniform and as
[8:59] you can see this is very simplified. You could load the map and randomize it, add
[9:10] some color, you name it. So yeah that's basically it. That's the same I have
[9:17] done in this particular setup if I can show you as you can see this is the same.
[9:27] But for other set of geometry as you can see we have the windows and it's
[9:35] streaking down and also on the top areas. So where I think it makes sense but I
[9:44] might be wrong with the formula so feel free to correct me in the comments. And
[9:51] that's basically it. You will be able to find this particular setup in my Patreon
[10:00] on my Patreon so feel free to grab it there and other than that thank you for watching
[10:07] and I'll see you next time.



---

## Captured Frames

- [0:30] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_000.jpg
- [1:40] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_001.jpg
- [3:20] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_002.jpg
- [4:20] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_003.jpg
- [5:40] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_004.jpg
- [7:00] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_005.jpg
- [8:00] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_006.jpg
- [9:10] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_007.jpg
- [9:50] tutorials/frames/procedural-leaking-texture-in-houdini-205/frame_008.jpg

---

## Structured Notes

### Core Technique
Generate a procedural water/dirt-streak "leaking" mask (no simulation needed) by combining curvature (convexity/concavity) with dot-product-based up/down-facing directional masks to find where streaks should originate, then scatter oriented points there and stamp SDF streak shapes in **Cops** — with orientation corrected per-face via a UV-space gradient measurement so streaks always point "down" even on UV islands that are rotated or upside-down.

### Summary
Starting from simple box geometry with window cutouts, Subdivide adds enough resolution for **Measure Curvature** (Labs) to compute convexity and concavity attributes at SOP level (unavailable at shading level, hence the need for real geometry resolution). Leaks shouldn't originate everywhere — only where water/dirt would naturally collect, e.g. not at the bottom of windows or at the very top — so two directional masks are built from the **dot product between the surface normal and a Y-axis up vector** (one isolating up-facing faces, one down-facing), then mixed together with the convexity/concavity attributes to produce a combined "leak origin" mask. Separately, two vertex-level (not point-level) top/bottom masks are built the same dot-product way for later multiplicative cleanup, kept sharp specifically because they operate on vertices. The trickiest problem solved here is **streak orientation on arbitrarily-rotated UV islands**: naively using the relative point-bounding-box Y (a simple top-to-bottom 0→1 gradient) works fine on aligned faces, but breaks on any face whose UVs have been rotated/flipped (simulated in the video by manually rotating one face's UVs 180°) — the gradient no longer points down in UV space for that face. The fix, suggested by "swalch" on the CGWiki Discord, is to **measure the gradient of that same top-to-bottom mask** (after mapping it into UV space via split-UV-seams + promote-to-point + UV-to-position assignment): the gradient vector naturally points in the correct "down" direction on each face regardless of how its UVs are rotated, and this gradient becomes the true up/orientation reference for the streaks. Points are scattered on the combined leak-origin mask, given a randomized p-scale (for varied streak sizes) and a normal attribute derived from the measured gradient (with up set along Z) for orientation, then everything moves into **Cops**: points are imported and Rasterized (remapped to the -1 to 1 Cops coordinate space), a simple Line-based SDF shape (converted to mono) is Transformed and used with **Stamp Point** to draw the actual streak marks at each scattered point, correctly oriented thanks to the gradient-derived normal attribute. The earlier vertex-level top/bottom masks are combined via Maximum and multiplied over the stamped result to remove unwanted streaks near those edges; a final Streak Blur (inverted) and preview complete the simplified base look — acknowledged as uniform/basic but easily extendable with map loading, randomization, and color.

### Key Steps
1. Build sample geometry: Box → window-cutout Extrudes → point Normals → **Subdivide** (needed resolution for curvature measurement, since curvature nodes don't exist at shading level).
2. Run **Measure Curvature** (Labs) to get convexity and concavity attributes.
3. Build two directional masks via **dot product between the surface normal and a Y-axis up vector**: one for up-facing faces, one for down-facing faces.
4. **Mix** the directional masks with the convexity/concavity attributes to produce the combined leak-origin mask, conceptually marking where streaks should start (avoiding window bottoms, top edges, etc.).
5. Build two additional **vertex-level** (sharper, since vertex-scoped) top/bottom masks using the same dot-product approach, for later cleanup multiplication.
6. Create a randomized **p-scale** attribute at the point level for varied streak sizes when later scattering.
7. **UV unwrap** the geometry; to simulate a real-world UV-orientation problem, manually select a subset of primitives, recolor them, and rotate their UVs upside-down.
8. Build a naive top-to-bottom mask via **relative point bounding box** (0 at bottom, 1 at top) — works for aligned faces but fails (doesn't run white-to-black correctly) on the manually-rotated face.
9. **Fix via UV-space gradient** (credit: swalch, CGWiki Discord): split UV seams, promote UVs to a point attribute, assign UV to position (temporarily), then **measure the gradient** of the earlier top-to-bottom mask in that UV-mapped space — the gradient vector correctly points "down" per-face regardless of UV rotation, providing a reliable orientation reference.
10. **Scatter points** on the combined leak-origin mask; assign a normal attribute derived from the measured gradient (with up set along Z) so each point is properly oriented for streak stamping.
11. Move into **Cops**: import the scattered points, **Rasterize** with the coordinate space remapped from -1 to 1 (Cops' native space); build a streak shape from a **Line** converted to a mono SDF, transformed as needed, then use **Stamp Point** to draw a streak at each scattered point — orientation correctly follows the gradient-derived normal, even on the deliberately-rotated test face.
12. Combine the earlier vertex-level top/bottom masks via **Maximum**, multiply over the stamped streak result to remove unwanted streaks near those edges.
13. Apply a **Streak Blur** (inverted) for a final soft pass, then preview — result is intentionally simplified/uniform but easily extendable with texture maps, randomization, and color variation.
14. Demonstrated applied to a more complex building facade with windows, correctly streaking down from tops and around window openings.

### Houdini Nodes / VEX / Settings
Box, Extrude (window cutouts), Normal, Subdivide, Measure Curvature (Labs, convexity/concavity), dot-product wrangle (normal · Y-axis up vector, up/down-facing masks), Mix/Blend (combining directional masks with convexity/concavity), vertex-level dot-product masks (top/bottom, sharp), Attribute Randomize (p-scale), UV Unwrap, manual UV rotation (test case), relative point-bounding-box gradient (naive top-bottom mask), Split UV seams, Attribute Promote (UV to point), UV-to-position assignment, Measure (gradient of mask), Scatter, normal-from-gradient attribute (up along Z), Cops: Rasterize (points, -1 to 1 remap), Line + Convert to Mono (SDF streak shape), Transform, Stamp Point, Maximum (vertex mask combine), Multiply (cleanup masking), Streak Blur (inverted).

### Difficulty
Advanced (the UV-space-gradient orientation-correction technique is a genuinely non-obvious solve for a real production problem).

### Houdini Version
20.5.170 (visible in viewport title bar).

### Tags
cops, curvature, vex, dot-product, uv-gradient, weathering, decay, procedural-textures, karma

---

## Related Tutorials
- [The Donut Tutorial in Cops - Houdini 20.5](the-donut-tutorial-in-cops-houdini-205.md) — related Copernicus/Cops procedural-texturing tutorial using similar Stamp Point/Rasterize techniques from the same channel.
- [Procedural Buildings in Houdini Tips and Tricks](procedural-buildings-in-houdini-tips-and-tricks.md) — likely companion building-weathering tutorial applying this leak-mask technique in a full production context.
