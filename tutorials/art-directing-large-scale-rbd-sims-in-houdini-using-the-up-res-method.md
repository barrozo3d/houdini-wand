---
title: Art directing large scale RBD sims in Houdini using the up-res method
source: YouTube
url: https://www.youtube.com/watch?v=M6E3f3yY824
author: the point and prim
ingested: 2026-07-16
houdini_version: "Not specified"
tags: [rbd, up-res, voronoi-fracture, solaris, karma-cpu, usd, procedural-lop, art-direction, the-point-and-prim]
extraction_status: complete
frames_dir: tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Art directing large scale RBD sims in Houdini using the up-res method

**Source:** [YouTube](https://www.youtube.com/watch?v=M6E3f3yY824)
**Author:** the point and prim
**Duration:** 11m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. In my last video I talked about doing some R&D into
[0:11] RBD uprising and that is exactly what we're going to talk about today. If you are unfamiliar
[0:16] with what uprising is it is the concept of working with a horrifically low polysim like
[0:21] this one which is very fast to iterate and therefore control. The low res sim is then
[0:25] used to guide a high res sim to achieve a predictable high res result. This is not a golden
[0:31] bullet which reduces the final sim time of the high res but is intended to maximize your
[0:35] valuable hours as an artist. This project file is quite large so we won't have time
[0:39] to cover all of it within the constraints of this video. Instead we'll be focusing on
[0:44] the core concepts. These are the base fracture, the guide sim, secondary fracture and most
[0:52] importantly the upper system. I will also be covering the rendering setup in Solaris
[0:57] and Karma CPU, touching on topics such as subsets, efficient authoring of USD for heavier effects
[1:02] like this and some shading and render setting notes. There isn't anything too complicated
[1:07] going on in that department but enough useful information to help you tie a shot like
[1:11] this together yourself. We are about to go through the core techniques of how to get
[1:15] this effect up and running but if you would still like to learn more or look at the other
[1:18] setups inside the hip file that we don't have time to cover in this video the project
[1:21] file is available on Gumroad, link below. In a stand and workflow you would typically
[1:28] sim at the required resolution evaluate the result and iterate. After all these sims
[1:32] we still might not have the desired result. This quickly gets frustrating as the feedback
[1:36] loop takes around 42 minutes ago in this theoretical example. On top of this our feedback
[1:41] loop is limited by how fast, hour or our studio's hardware can compute the data which
[1:46] can be very slow at production quality. The upper is approach instead focuses spending
[1:51] the bulk of our time iterating and then submitting a high-risk sim with a lot more confidence
[1:55] that the movement will match what we desire. So if you've done RBD before you will be familiar
[2:03] with the commonly promoted workflow of simulating the proxy geometry and then transforming
[2:06] the high-risk fracture pieces using the orientation and translation of the proxy points.
[2:11] You will be used to working with high-risk chunks that look like this. In the upper is method
[2:14] we will then fracture the high-risk pieces a second time and then reapply the transform
[2:18] from the proxy points. This is where things start getting trickier. The twice-fractured
[2:22] chunks will then be simulated again and we will need to manipulate the active and animated
[2:26] attribute so that the pieces at the edges of our chunks gradually get activated as the
[2:30] sim progresses. The terrain is just a grid displaced for the texture map from Gaia. You
[2:37] can of course just use who do any height fields if you want. I call out everything outside
[2:41] of camera frostum so I can maximize the resolution in camera. I use the rest noise rest technique
[2:47] and Vorono fracture this planar geometry, doing the extrusion after it to avoid who
[2:51] Danny cooking a 3D fracture. These chunks then go into a for loop where I remesh the inside
[3:00] group and add some noise displacement. I lurp the points of the outside back onto the
[3:04] original position so I don't modify the terrain surface. I generate a mask with the same
[3:08] outside group and blur it a tiny bit. Then use a lurp once again to a slightly smaller
[3:12] version of the chunk to get this tapered look. This fracturing method allows us to get
[3:16] nice displaced edges and inside faces as well as a nice overhanging edge that will work
[3:20] nicely later when we will eat into it with the upper assimilation. Now that we have our
[3:27] base fracture we can set up the proxy sim. First we need to create the proxy geometry of
[3:32] the pieces. I do this by looping over the pieces, shrink wrapping them and retrieving
[3:36] their name attribute from the incoming iteration of the loop. You can also use the convex
[3:42] decomposition node to do this but I found I was getting better performance by manually
[3:46] building the loop. After this I am using an assemble to pack the pieces and then deleting
[3:50] the pack prims with an ad node in a separate stream so I can work with the points for building
[3:55] the activation and velocity impulse. If we swap to top orthographic and enable this
[3:59] mask attribute we can see what is being used to drive the impulse. This is done using
[4:04] the simple wrangle. We can use the rail bee box function to get the relative bounding
[4:07] box of this geometry using its x component inside a smooth function. By animating the
[4:12] first value in the smooth and adding a tiny amount to the second we can create a really
[4:15] tight, animatable mask. If that made no sense to you then this might. Anything below
[4:21] range bottom returns a zero and anything above range top returns a one. Anything in
[4:25] between is a smooth interpolation from zero to one. If we shift the values around it
[4:29] squeezes all the loose ends of the values meaning if range top is equal to range bottom
[4:33] plus something really small we will get a super tight, basically non-existent easing
[4:37] between the two values. Next I time shift this animation back one frame and compare
[4:41] its mask attribute to the current frame, allowing me to isolate and group whatever has
[4:44] just gained the mask attribute. I use this group to add some velocity onto those points
[4:48] only while I use the masks to set the active attribute from zero to one. You may notice
[4:53] I have these border points around the edge that aren't being affected by the mask and
[4:56] that is because I use the border of the terrain geo to group those points by distance and deactivate
[5:00] them. After this you simply copy your attributes back over to your pack prims. You can use an
[5:05] add node again to validate if they copied correctly. Inside dops you'll need a simple pop
[5:10] wrangle to update the attributes each frame. Just remember you want to set active and add
[5:13] to v. That is it for the proxy sim. I won't spend more time in it as you will want to
[5:17] build your shot differently. Just remember you are going to spend the bulk of your time
[5:20] on the proxy sim in this workflow so it's worth investing extra time into making this
[5:23] part of your node graph easy to use. So now we've catch the proxy sim out as points
[5:29] and it is working as intended transforming the high res pieces. In order to set up the
[5:33] up res we need to fracture the geometry a second time but when we run our second sim we
[5:37] will need a name attribute for those pieces to behave independently. Yet we still need
[5:41] to retrieve the transforms of our proxy sim. This essentially means we need two name
[5:44] attributes. We can do this by renaming the name attribute of the proxy sim to something
[5:48] else on both the pieces and the points. I use x form name but it can be whatever you
[5:53] want as long as they both match up. Now that all the weird name attribute stuff is
[5:58] out of the way I use a connectivity node to generate this chunk attribute which will
[6:01] be essential later so don't forget it. The up res fracture itself is very simple. It
[6:05] is just the rest noise rest technique again using points scattered on the outside group
[6:09] which then pipe into another varanoi. This time I didn't find a way around it. This
[6:12] fracture can get pretty slow depending on your incoming geometry. Let it cook and go
[6:16] to get yourself a couple of coffee. After the up res fracture is complete make sure
[6:20] to validate it by checking it with the proxy points again to make sure the new pieces
[6:23] transform correctly with the new name attribute. In order to simulate this we want to create
[6:26] proxy geo again so we can just repeat the same shrink wrap loop trick. This time we retrieve
[6:31] name x form name and chunk. Cache that out and check your attributes are working as intended.
[6:41] Buckle up because this is going to be theory heavy. First we need to set ID for these pieces
[6:45] as we will need this in a second. This wrangle is the cornerstone of the entire system.
[6:49] Let's have a look at it. So the idea behind the up res is that we calculate the distance
[6:52] between points of neighboring chunks and if that passes a certain threshold we will activate
[6:56] those pieces else it will just follow the proxy sim animation. That means we need to find
[7:00] a way to measure the distance between pair IDs dynamically. If we grab a bunch of these
[7:03] pieces and move them over here we can see the border pieces accumulate and attribute.
[7:09] So we have three beautiful chunks, 0, 1 and 2. We read this in at the top of the wrangle.
[7:13] We have the secondary fracture so our pieces actually look like this. We will operate
[7:16] on just one piece for demonstration purpose. We use the near point function to open a point
[7:19] cloud. Find all nearby points within a certain distance and store them in an array. Next
[7:24] we will loop through all items in the array. Remember we want to find a pair ID on the
[7:27] neighbor chunk, not an current one. We can do this by checking what chunk attribute
[7:31] the array point returns. If it is the same as our current point we continue the loop.
[7:35] As soon as it finds a point on a different chunk it registers that point as a pair ID
[7:38] and breaks a loop, discarding the rest of the items in the array. This means 0.8 and 0.36
[7:43] and our pair together. This will of course repeat over all of the points in the geometry
[7:46] so that all of them will pair up. This doesn't account for unique pairs only as I didn't
[7:50] find it necessary for this shot but you can program in that behavior if needed. Now we
[7:55] can just read the position of the pair ID and compare that to the current position and
[7:58] write that out as an attribute. This will measure the separation between the two. I use
[8:02] a time shift on frame 1 and then create a group based on the pair distance to hard set
[8:05] which points will be allowed to activate as I don't want to eat too far into the chunk.
[8:09] So far our pair distance has values greater than 0 at frame 1 which makes it annoying to
[8:13] control. I normalize this by subtracting the current pair distance by the time shifted
[8:16] pair distance. If we visualize this now we can see the value start on 0 and then increase
[8:20] as the pieces move away from each other. I use the exact same time shift trick from the
[8:24] proxy sim except I compare length and velocity this time. I will create an integer attribute
[8:28] which I use to force some pieces to become active on the first frame for better impact.
[8:32] Now that we have all this we can pipe it into a solver which will dynamically control
[8:36] the active attribute. We are reading the current distance and setting a threshold. We want
[8:42] to compare the distance to the threshold and if it's greater or less than that value
[8:46] accumulate an attribute which is controlled by this rate parameter multiplied by some random
[8:49] resistance. Once that accumulated value goes past a certain point we simply set the
[8:53] active attribute to 1 and the animated attribute to 0. Prior to this all pieces were set
[8:58] to only animate meaning they followed the movement of the proxy sim and that's it for
[9:02] the core elements needed for this system. In Dops we just read the active and animated
[9:06] attribute like we did with the proxy. Over in stage we start by sub importing the
[9:18] RBD pieces we will want to set the layer save path. It's important to do this as it will
[9:22] speed up the RBD procedural later. We also want to scroll down to the bottom of the import
[9:26] data tab and enable subset groups. This will convert our inside and outside group from
[9:30] the fracture into subsets for separate material assignments.
[9:33] Next up we use the RBD procedural lock to correctly set up our RBD simulation for USD. We
[9:37] point to the prime here and read the points directly from disk. As pointed out by her
[9:42] and Yanno this is a lot more optimised when dealing with large amounts of data. We
[9:45] can also check that our subsets are working by making a couple of flat shaders and applying
[9:49] them to test them out. Finally we want to cache this to disk so we can sublay her
[9:52] it back in later. Thank you lazy cinephile for this tip. I do need to mention there is
[9:57] a bit of fiddling around to get the RBD procedural lock to work. I created an entire video dedicated
[10:01] to this so if it gives you any grief make sure to check it out. Link below. We didn't
[10:05] cover the debris simulation in this video but I instanced my prims directly on other
[10:09] points from sops and then cache them out as well as importing the terrain and converting
[10:12] it to USD.
[10:16] Now we can read all our layers back in. We can use the Houdini Preview Procedural node
[10:19] to visualise the procedural. If you leave it off the RBD's won't move in the viewport
[10:23] but it is great for performance. On the right we've got our lights and materials which
[10:27] we graphed into our geometry branch. Shader wise I am mixing the colour map from Gaia
[10:35] with a little bit of noise. I use a different noise to randomly rotate the UV's which
[10:41] I plug into a texture for displacement which I've got disabled in the IPR for speed.
[10:46] I've got a second material for the inside subset which is just using the rest attribute as
[10:54] a position input for a triplanar texture. Nothing crazy here. There are very basic
[10:57] separate shaders for the dust and debris but we won't be covering those now. The last tips
[11:02] I've got for this are that I like to use a render geometry settings node to dial down the
[11:05] Dicing a bit as the default setting is sometimes too brutal for my home machine to handle.
[11:09] You can completely disable it by setting it to zero which is great when you're setting up
[11:13] shaders. Lastly I always use an LBE tag node and standard render vise to split my lights
[11:18] up into separate passes for comp. And that's it for now. I hope there is enough information
[11:23] in this video to start implementing RBD UPRESS techniques yourself. There are several other
[11:28] elements in this project file that I didn't have time to cover here. If you are still curious
[11:32] about this or would like to take a deeper look at these techniques the hip file is available
[11:36] on Gumroad. Link in the description. Thanks so much for watching and see you in the next one.



---

## Captured Frames

- [0:16] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_000.jpg
- [2:47] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_001.jpg
- [3:59] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_002.jpg
- [4:41] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_003.jpg
- [6:45] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_004.jpg
- [8:02] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_005.jpg
- [9:18] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_006.jpg
- [10:16] tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/frame_007.jpg

---

## Structured Notes

### Core Technique
The **RBD "up-res" method**: iterate art direction on a very cheap, low-resolution proxy RBD simulation, then drive a second, much higher-resolution fracture/simulation using dynamically-computed neighbor-distance thresholds so that only the pieces that actually need to separate get activated — followed by an efficient USD/Solaris/Karma CPU pipeline (RBD Procedural LOP, subsets) to render the resulting large-scale destruction shot.

### Summary
This is a follow-up to the author's RBD up-res R&D video, focused on the core concepts rather than every node in the (large) project file: base fracture, guide/proxy sim, secondary (high-res) fracture, and — most importantly — the "up-res system" that decides which high-res pieces activate, plus a Solaris/Karma CPU rendering pass. The motivating problem: standard RBD iteration (sim at final resolution, evaluate, repeat) is slow (the video cites a ~42-minute feedback loop in a theoretical example) and hardware-bound. Up-res instead spends most iteration time on a cheap low-poly guide sim, then submits one high-confidence high-res sim once the motion is dialed in — not a speed guarantee for the final sim, but a way to maximize artist iteration time. The base fracture starts with a displaced grid terrain (author uses a Gaea height texture; Houdini heightfields work too), frustum-culled to the camera to maximize in-camera resolution, fractured with the classic **rest-noise-rest + Voronoi Fracture** technique (fracturing the flat/planar geometry before extrusion to avoid Houdini cooking a full 3D fracture). A for-loop over the resulting chunks remeshes the "inside" faces and adds noise displacement while lerping the "outside" group's points back to their original position (so the terrain surface itself isn't modified); a blurred mask of the same outside group is used with a second lerp toward a slightly shrunk version of the chunk to create a tapered, overhanging edge — useful both for looks and for how the up-res sim later "eats into" that edge. For the **proxy/guide sim**: proxy geometry is built by looping over pieces, shrink-wrapping them, and pulling each piece's `name` attribute from its loop iteration (author found this manual loop out-performs the Convex Decomposition node); pieces are Assembled/packed, then unpacked (via Add SOP in a separate stream) to work with points for activation/velocity setup. A wrangle computes a **mask** using `relbbox()`'s X component fed into the **smooth function** (animating range-bottom, offsetting range-top by a tiny amount, for a tight animatable mask — same core technique as the channel's dedicated smooth-function videos); a Time Shift compares the mask one frame back against the current frame to isolate/group points that "just gained" the mask, which get an added velocity impulse, while the mask itself drives `active` from 0→1. Border points (grouped by distance from the terrain edge) are explicitly deactivated so the terrain boundary doesn't fracture. Proxy attributes are copied back onto the packed prims, validated, and simmed in DOPs with a simple POP Wrangle each frame setting `active`/`v`. For the **up-res** step, the high-res pieces are fractured a second time; since the second sim needs its own independent `name` attribute per new piece while still needing the original proxy transforms, the proxy's `name` is renamed to a second attribute (e.g. `xform_name`) on both pieces and points before re-fracturing, and a **Connectivity** node generates a `chunk` attribute used later. The up-res fracture itself reuses the same rest-noise-rest + Voronoi technique on points scattered on the outside group (called out as slow, "go get a coffee"). After validating the new fracture against proxy transforms, proxy geometry is rebuilt again for the up-res pieces (retrieving `name`, `xform_name`, and `chunk`). The core "cornerstone" wrangle: an `id` is set per up-res piece, then for each point a `nearpoints()` point-cloud lookup gathers nearby points within a radius, looping through the results to find the first neighbor whose `chunk` attribute differs from the current point's (skipping same-chunk neighbors) — that neighbor becomes the point's "pair," registering a pair ID and breaking the loop (not accounting for unique/mutual pairing, called out as an option to add if needed). The pair's position is compared against the current position to compute a **pair distance** attribute measuring separation between neighboring chunks; a Time Shift to frame 1 provides a baseline so the pair distance can be normalized (subtracting the frame-1 baseline so values start at 0 and grow as pieces separate) — the same time-shift-baseline trick used in the proxy sim, but comparing length/velocity this time. An integer attribute forces some pieces active on frame 1 for immediate visual impact. All of this feeds a **DOP Solver** that reads the current pair distance against a threshold, accumulates a value driven by a rate parameter multiplied by random per-piece resistance whenever the distance crosses the threshold, and once the accumulator passes a limit, sets `active = 1` and `animated = 0` for that piece (prior to that, all pieces are `animated`, meaning they simply follow the proxy sim's transform). DOPs then reads `active`/`animated` exactly as in the proxy sim. For **rendering**: in Solaris, RBD pieces are sub-imported with a fixed layer save path (important for RBD Procedural LOP speed) and "enable subset groups" is turned on so the fracture's inside/outside groups become USD subsets for separate material assignment. The **Houdini RBD Procedural LOP** is used (pointing at the prim and reading points directly from disk, cited as significantly more optimized for large datasets — credited to "her and Yanno"'s tip), validated with quick flat-shader tests on the subsets, then cached to disk and sublayered back in. Debris (separately point-instanced, simmed, and cached, plus the terrain converted to USD) is not covered in depth. The **Houdini Preview Procedural** LOP is used to visualize the RBD in viewport (disabling it for performance since RBDs won't move in viewport without it). Shading mixes a Gaea color map with noise-randomized UV rotation for triplanar-style displacement texturing (disabled in IPR for speed); a second material for the "inside" subset uses the `rest` attribute as the triplanar position input. Final tips: use a **Render Geometry Settings** LOP to dial down dicing (0 = fully disabled, useful while lighting/shading) since the default is often too aggressive for lower-spec hardware, and use an **LPE Tag** node with standard render variables to split lights into separate comp passes.

### Key Steps
1. Build the base fracture on a frustum-culled, displaced terrain grid using the **rest-noise-rest + Voronoi Fracture** technique on planar geometry (fracture before extrusion to avoid a full 3D Houdini fracture cook).
2. For-loop over chunks: remesh + noise-displace the "inside" faces, lerp the "outside" group's points back to original position, then use a blurred outside mask + a second lerp toward a shrunk chunk copy to create a tapered/overhanging edge.
3. Build **proxy geometry**: loop over pieces, shrink-wrap each, retrieve its `name` from the loop iteration, Assemble/pack, then unpack in a separate stream for point-level activation work.
4. Write a mask wrangle using `relbbox()`.x fed into the **smooth function** (animated range-bottom, tiny range-top offset) for a tight animatable activation mask; Time Shift one frame back to isolate newly-masked points for a velocity impulse, and drive `active` 0→1 from the mask; deactivate distance-grouped border points at the terrain edge.
5. Copy proxy attributes back onto packed prims, validate, then simulate in DOPs with a simple POP Wrangle setting `active`/`v` per frame.
6. **Up-res fracture**: rename the proxy `name` attribute to a second attribute (e.g. `xform_name`) on both pieces and points, generate a `chunk` attribute via **Connectivity**, then re-run the rest-noise-rest + Voronoi fracture on the outside group's scattered points for the high-res pieces; validate against proxy transforms.
7. Rebuild proxy geo for the up-res pieces (retrieving `name`, `xform_name`, `chunk`) and cache.
8. Write the "cornerstone" wrangle: set an `id`, use `nearpoints()` to find nearby points, loop to find the first neighbor on a **different** `chunk`, register it as a pair, compute **pair distance** between the pair, and normalize against a frame-1 Time Shift baseline; add an integer attribute to force some pieces active on frame 1.
9. Feed pair distance into a **DOP Solver**: compare against a threshold, accumulate via a rate × random-resistance value, and once past a limit, flip `active = 1` / `animated = 0` for that piece (otherwise pieces stay `animated`, following the proxy).
10. In Solaris: sub-import RBD pieces with a fixed layer save path, enable subset groups (inside/outside → USD subsets), wire up the **Houdini RBD Procedural LOP** (reading points from disk for speed), validate with flat shaders on subsets, cache and sublayer back in.
11. Instance/cache debris separately and import the terrain as USD; use **Houdini Preview Procedural** to preview RBD motion in viewport (disable for performance).
12. Shade with a Gaea color map + noise-randomized UV rotation for triplanar displacement (IPR-disabled for speed); use `rest` as the position input for the "inside" subset's triplanar material; dial dicing via **Render Geometry Settings**, and split lights into passes with **LPE Tag**.

### Houdini Nodes / VEX / Settings
Voronoi Fracture (rest-noise-rest technique, planar-then-extrude), For-Each loop (per-chunk remesh/noise/lerp), Shrink Wrap (proxy geo), Assemble (pack), Add SOP (unpack/validate), `relbbox()` + smooth function (activation mask wrangle), Time Shift (frame-1 baseline / one-frame-back comparison), POP Wrangle (`active`, `v` per frame in DOPs), Connectivity (`chunk` attribute), `nearpoints()` point-cloud lookup (pair-ID wrangle), DOP Solver (threshold-accumulator `active`/`animated` logic), Houdini RBD Procedural LOP, Sub-import LOP (fixed layer save path, subset groups), Houdini Preview Procedural LOP, Render Geometry Settings LOP (dicing control), LPE Tag (light-pass splitting), Karma CPU, USD subsets, triplanar texturing (`rest`-attribute-driven).

### Difficulty
Advanced (combines a multi-stage proxy/up-res RBD pipeline with custom neighbor-pairing VEX, a DOP-solver-driven activation system, and a production USD/Solaris/Karma rendering setup).

### Houdini Version
Not specified.

### Tags
#rbd #up-res #voronoi-fracture #solaris #karma-cpu #usd #procedural-lop #art-direction #dop-solver #the-point-and-prim

---

## Related Tutorials
- [Houdini USD RBD Procedural LOP in under 5 minutes](houdini-usd-rbd-procedural-lop-in-under-5-minutes.md) — same channel/author; a focused deep-dive on the exact RBD Procedural LOP node setup used briefly here for the Solaris rendering pipeline.
- [RBD Procedural Animations in Houdini | Mardini 2026](rbd-procedural-animations-in-houdini-mardini-2026.md) — different author (cgside), but directly overlapping RBD Procedural LOP / USD workflow territory.
- [Cleaning fractured geometry in Houdini](cleaning-fractured-geometry-in-houdini.md) — different author (cgside); complementary fracture-preparation techniques relevant to the base/up-res fracture stages here.
