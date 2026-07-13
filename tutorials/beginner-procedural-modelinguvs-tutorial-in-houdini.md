---
title: Beginner Procedural Modeling/UVS Tutorial in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=-1kxDkdmcV4
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H18+)"
tags: [modelling, procedural, vex, uv, beginner]
extraction_status: complete
frames_dir: tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Beginner Procedural Modeling/UVS Tutorial in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=-1kxDkdmcV4)
**Author:** cgside
**Duration:** 18m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back, so in this video we'll be modeling this wine barrel.
[0:04] It will be a good chance to get familiar with some of the most used subnotes alongside
[0:10] with some very simple backs concepts and also how to do the proper UVs or this kind of
[0:18] procedural assets.
[0:20] And if you guys are interested, we can in the next lesson, texture the barrel as you can
[0:25] see here, nothing too crazy, but it could be a good exercise to get familiar with cups.
[0:31] So yeah, let's get into it.
[0:33] So let's start by dropping a geo container and we will start with a tube and I found some
[0:41] values, in this case I want a height of 1.1, 12 rows and 32 columns, so we can make out
[0:50] the wood planks.
[0:53] And I believe that would be it for now.
[0:56] Now let's drop a wrangle and we will deform this into the barrel shape.
[1:02] So let's start by storing the bounding box information or the relative bounding box.
[1:08] In this case we will use relative point bounding box and the incoming geometry and the position.
[1:16] And I can show you, if I create a natural boot in here, I can show you what this means,
[1:24] is basically the relative position of the geometry as you can see.
[1:31] So this is the y going from 0 to 1.
[1:34] If we instead used at b, it would go from minus 1 or minus 0.5 to 0.5.
[1:44] So we want to use the relative bounding box, since we have this centred in our scene.
[1:50] But in this case we don't want to use this, we will use a ramp to deform our shapes.
[1:56] So see a ramp and we will call it ramp deform and we will use the relative bounding box
[2:07] y.
[2:09] And let's have a look at that.
[2:12] Now we want to transform this to a hail shape, so it looks something like this and change
[2:17] the interpolation to b-spline.
[2:19] Let's see how that looks, if we deform both the x and z component of the position.
[2:23] So at b dot x times equals ramp and it will do that on the x and now we can just copy
[2:34] and do the z.
[2:38] As you can see it's creating that shape, but in this case we want to move those handles
[2:46] up and I'm going to copy this value to the last one, so with mirrors whenever I move
[2:53] one it will move the other and I'm going to set it to 0.7 to 5.
[2:59] This was just a value I found work 12.
[3:03] And we have our first back setup done.
[3:05] I believe it's really simple, if you are having trouble understanding it, I can go on
[3:11] the comments and help you out.
[3:14] So now we want to create an attribute for every column, so we will use a kind of bit
[3:19] of backs.
[3:20] In this case, in this one we used points, right now we're going to use primitives because
[3:25] we want an attribute on the primitives.
[3:28] And the first thing we're going to do, we're going to reference the columns from the
[3:31] two, so it will create a variable, an integer and a channel integer called calls, calls.
[3:40] And now we're going to create that parameter and come in here and copy this.
[3:44] This just makes everything more procedural instead of typing the value itself.
[3:49] And now we can just write a premium, premium ID, it will be equals to add to print, print
[4:00] them.
[4:03] And let's have a look at how that Cisco is working.
[4:07] So we have for each primitive we have an ID, a prim ID, but in this case we want to use
[4:13] module to separate them into different columns.
[4:16] So if we divide in this case by the columns, we will have a notice these rows, as you can
[4:24] see, but in this case we want to module it.
[4:27] So we get this sort of result.
[4:29] So it's always useful to divide in the module to this kind of word.
[4:34] And now we can just poly extrude it.
[4:38] So extrude.
[4:41] And we will extrude by about point of 12 was a value I found work well and I'll put
[4:48] the back.
[4:49] So we have the back polygons.
[4:51] And now we want to split it to split each plank.
[4:54] So for that we can use a vertex split.
[4:59] And by default it will use the anature root, we will remove it and use the premium ID.
[5:04] And if we do an exploded view, we will see that we've split it to the planks.
[5:10] But right here it's empty and we want to fill that.
[5:13] But for now we will first do a uniform scale of point of 1 in the exploded view.
[5:20] This will have a little bit of space as you can see.
[5:23] And now we can just poly fill.
[5:26] And what we let rolls will be fine.
[5:28] It will work perfectly as you can see.
[5:31] And that's this part done.
[5:33] So now we want to do our UV.
[5:35] So let's create a group or the seams.
[5:38] In this case I'm gonna select edges and include by edges and select mean edge angle.
[5:44] And it will select those edges.
[5:46] Now we can just see UV flatten.
[5:51] And we will do the group one.
[5:53] And also we will rectify and disable manually out.
[5:57] And if we look at our UVs, there will look clean enough.
[6:01] Please follow.
[6:03] So let's disable the visualization of UVs and create a bevel.
[6:10] And we will exclude the flight edges.
[6:14] So we just bevel the corners as you can see.
[6:19] And in this case I want a value of point of 2 rounds and 3 divisions as you can see.
[6:27] And the UVs should adapt.
[6:29] So that's fine.
[6:31] Now we will subdivide this.
[6:37] And soften the normals.
[6:38] So we have a better preview.
[6:40] As you can see we have this word shaving not sure if it's going through the recording.
[6:45] But if we soften the normals it will look a bit better.
[6:49] And finally we just need to create a attribute.
[6:53] In this case using a rainbow, why not?
[6:55] And just say we want a float attribute called barrel.
[6:59] And it will be called the one.
[7:02] So we just create a attribute.
[7:05] So we can target later in texturing.
[7:08] Now we will fill this barrel by closing in these gaps we have in here.
[7:14] And this should be simple enough.
[7:17] So let's start with a circle.
[7:19] Oops, circle.
[7:23] And we will place it on the ZX plane.
[7:26] Set the divisions to 32.
[7:28] And I know a value of point 3, 8 will be more than enough.
[7:34] And while we are here we will just use the texture of this.
[7:40] In this case on the Y.
[7:43] Let's see how that looks.
[7:44] As you can see it's reversed so we can scale it negatively.
[7:50] And but it will move it down so we can just use an offset of one.
[7:54] So that is fine.
[7:57] Now we can copy.
[7:59] Because we will need another one.
[8:01] So copy and transform.
[8:04] And if offsetting will be fine.
[8:05] It will copy just one.
[8:07] Now we will reverse one of them.
[8:09] Reverse the normals of one of them.
[8:11] So it can be zero.
[8:13] And next we will do some really simple Vex.
[8:18] We will move them apart.
[8:21] So we can just say.
[8:23] Let's see.
[8:28] VHP plus equals.
[8:32] We will display along the normal and multiply it by some value.
[8:38] So let's say this.
[8:40] Let's see if that works for us.
[8:43] And it does.
[8:44] And I know a value of point 5, 3 will be fine.
[8:49] And we also want to create a natural root.
[8:51] So it's in this case I'm going to do another one.
[8:55] And say f at the arrow tops equals to 1.
[9:02] And let's merge this.
[9:05] And see if that aligns.
[9:06] And it does.
[9:07] You can see we can go in here and play with the offset.
[9:12] So let's organize this by pressing A and dragging.
[9:15] This is fine.
[9:16] And let's create the norm.
[9:20] And call it barrel.
[9:26] And we have our UVs.
[9:27] Later on we will lay them out properly.
[9:30] So they have the same scale and whatnot.
[9:32] But for now let's keep it like this.
[9:35] So now we will create the hopes around the barrel.
[9:39] And for that we will start.
[9:41] Let's see.
[9:42] We just circle.
[9:47] And this circle can have 32 subdivision students just to keep some consistency.
[9:53] And on the ZX plane, the size doesn't really matter.
[9:58] For the UVs later we will need some groups.
[10:02] So I'm going to create a range and connect the divisions in here.
[10:09] The copy parameter and paste it in here and divided let's say by four.
[10:15] So we don't have UGV islands.
[10:18] And so this way we can divide it into sections.
[10:22] And now we will create the normals.
[10:24] So that's a good language.
[10:27] I believe I used open arc in here.
[10:29] Yeah, open arc.
[10:30] That's fine.
[10:32] And now we will just create the aperture boot for the sweep that we will use in a bit.
[10:36] So vector up it will be equal to normalize V at P.
[10:43] So this will just create the vectors pointing outwards like this.
[10:50] So that is fine.
[10:53] And now we will match size this.
[10:57] We will align it with the barrel in here.
[11:03] And in this case, let's see, let's visualize this.
[11:09] And we will align it to the max and offset it by 0.03 negative 0.03.
[11:16] So this will be the first hoop.
[11:19] And now we can copy and transform.
[11:24] And we will copy three times and place it by about point all weight, negative point all
[11:32] weights something like this.
[11:34] Now we can mirror this to have also in the bottom.
[11:38] So in this case, I want to do direction to be one in the white.
[11:44] Let's evolve.
[11:45] And it's aligning properly.
[11:48] Now we will do the same for the other.
[11:54] Let me just organize this in here.
[11:58] We will do the same for the middle ones.
[12:01] In this case, we will set it to center and offset it by part 15.
[12:08] And just copy the mirror.
[12:10] And we have this result.
[12:12] Now we can merge this.
[12:16] We have something like this, which is fine.
[12:21] Next we will fuse the points.
[12:24] Make sure we fuse.
[12:26] Because when you create an open arc circle, they will have a point where they are not
[12:31] fused.
[12:32] So it's always a good idea to fuse because right now we want to use the sweep and set
[12:37] it to ribbon.
[12:39] And since we add that aperture boot, you can see if I don't create that, it won't align
[12:44] properly.
[12:46] And in this sweep, we will just play a bit with the size.
[12:51] So two columns.
[12:53] So we don't need much geometry and a value of 0.05 the size.
[13:00] So 0.05 is fine.
[13:03] Now we will merge here the barrel so we can rate this project is geometry onto the barrel.
[13:09] So let's just drag it in here.
[13:13] And let's see, let's rate this.
[13:18] But this won't work even if you create a, if you check reverse raise.
[13:25] Probably because there are open spaces in here, I'm not sure why.
[13:29] But quick fix is just use a convex all.
[13:33] And this will create some some proxy geometry.
[13:41] And now we can rate this and check reverse raise.
[13:46] So that is fine.
[13:49] Now we can just create another wrangle and call it.
[13:54] Oops, so oops.
[13:57] And this is just for cops later so we can mask out some parts.
[14:06] Now we will pick it a little bit.
[14:09] In this case, really small distance.
[14:12] Let me see.
[14:13] So you can see the barrel is over the, the, this option geometry so we'll pick it by 0.05.
[14:23] So this is fine.
[14:25] Now we need to start to think about UVs.
[14:29] So I'm gonna create a group of the unshared edges for now and you will see why in a bit.
[14:37] So unshared edges and now we will extrude it.
[14:44] And we will extrude by about 0.03.
[14:48] And do we need to output the back?
[14:54] In this case, I'm gonna do it the way I did it.
[14:57] But in this case, we didn't need to output the back, I guess.
[15:00] But let's keep it like that.
[15:02] Now we did this grouping here, group by range.
[15:07] So we called UV the mesh now.
[15:09] So if we have a look at the range group.
[15:16] So oh, I didn't call it range.
[15:18] Let me go back and call it range.
[15:22] So as you can see, we have this grouping here.
[15:25] But it's only on the back.
[15:26] It didn't propagate with the extrusion.
[15:30] So we will need to use a node called group line path.
[15:36] So group line path.
[15:39] So we can finish the selection.
[15:41] In this case, I'm gonna call it range.
[15:45] And the base group will be range.
[15:47] Let's set these two edges.
[15:50] But before we need to promote it, of course group promote.
[15:54] Range to edges.
[15:56] Let's see.
[15:58] And in this case, we need to include only elements in the boundary, I believe.
[16:03] Yeah.
[16:04] And now in here, we can just say loops or rings and extend to edge.
[16:12] And as you can see, it created the necessary cuts for the UV flatten that we will do now.
[16:21] So let's connect the UV flatten.
[16:23] And we will use the seams, the range and the unshared and rectified the group and also
[16:31] disable enable manual by out.
[16:34] So and we have nice UVs.
[16:39] And now we can just polybable.
[16:45] And we will be able to ignore the flat edges first and be able to buy a part to point
[16:52] a really small value point of level weight and round tree divisions.
[16:59] Let's see how that looks.
[17:00] That's fine.
[17:02] And now we can just subdivide this.
[17:06] Let's see what else we can choose as softenerables.
[17:15] And let's merge these.
[17:19] And we can just copy this from here and merge it over.
[17:27] Now we will use the UVs are all over each other.
[17:33] So we will use a UV layout.
[17:37] And in this case, I want to scale the islands to match their surface area.
[17:47] And let's see.
[17:51] This doesn't look bad, but I can probably use some iterations to distribute it a little
[18:00] bit better.
[18:01] Let's see.
[18:02] And that works for me.
[18:03] Let's see how that looks in here.
[18:06] Yeah, it looks pretty similar.
[18:11] And I'm gonna introduce some batting.
[18:16] And also apply batting between the islands and the boundary.
[18:21] So that's exactly my result.
[18:25] And this is it for this lesson.
[18:27] If you want to get into the texturing part, we can do that next.
[18:31] Other than that, please check out my Patreon where you will be able to find this project
[18:35] file and many, many others.
[18:39] And also have a look at my courses in there and leave a comment.
[18:43] It's always nice.
[18:44] Thank you.



---

## Captured Frames

- [1:50] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_000.jpg
- [4:29] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_001.jpg
- [5:10] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_002.jpg
- [6:19] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_003.jpg
- [8:49] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_004.jpg
- [11:19] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_005.jpg
- [16:21] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_006.jpg
- [18:03] tutorials/frames/beginner-procedural-modelinguvs-tutorial-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Beginner-friendly procedural wine barrel: a tube deformed into a barrel bulge via a ramp-driven VEX wrangle, split into individual wood planks using a `primnum % columns` attribute and Vertex Split, capped with pushed-apart reversed-normal discs, wrapped with swept metal hoops, and finished with a full manual UV workflow (seam groups, Group Find Path for extending cuts through extrusions, UV Flatten, UV Layout).

### Summary
An explicitly beginner-oriented tutorial pairing a simple procedural-modeling exercise with a full, correct UV workflow for procedural assets. The barrel body starts as a Tube, bulged into shape with a **relative bounding-box** VEX wrangle feeding a **Ramp** (a hallmark simple-VEX pattern: `relbbox(0,@P)` gives 0-1 values regardless of scene position, unlike `@P` itself). Planks are separated using a primitive-modulo attribute (`@primnum % cols`) instead of manual selection, split apart with **Vertex Split**, gapped and rejoined with PolyFill. UVs are built properly from the start: seam edges by angle, UV Flatten, then a corner Bevel that the UVs correctly follow. Barrel ends are two reversed-normal, VEX-pushed-apart discs; metal hoops are built from an open-arc Circle swept as a Ribbon, using a **normalized-position "aperture vector"** so the sweep orientation aligns correctly along the barrel curve, then merged and ray-projected onto a Convex-Hulled version of the barrel (needed because raying onto the actual open/non-manifold barrel geometry silently fails). The trickiest UV step is extruding the plank backs while preserving a pre-extrusion group selection for the flatten — solved with **Group Find Path** (promoted to edges, "Loops or Rings, Extend to Edge") rather than trying to re-select after the topology changes.

### Key Steps
1. **Base shape:** Tube (Height 1.1, 12 Rows, 32 Columns — density chosen to read as wood planks).
2. **Barrel bulge (VEX):** in a wrangle, compute `v@rel_bbox = relbbox(0, @P)` (0 = "use the incoming geometry," relative bbox goes 0→1 regardless of scene position — using `@P` directly instead would run -0.5→0.5 and depend on the object's world position). Feed the Y component into a **Ramp** ("ramp_deform", curved to a barrel/hourglass-ish shape, B-Spline interpolation), then multiply `@P.x` and `@P.z` by the ramp's output — set the ramp's middle handles to mirror each other (~0.725) so adjusting one updates both.
3. **Column/plank attribute:** a second wrangle references a `cols` integer channel parameter (copy-pasted from the Tube's Columns value to stay procedural) and computes `i@id = @primnum % cols` — using modulo rather than plain division-and-floor is what actually separates primitives into repeating column groups instead of just rows.
4. **Split into planks:** **Poly Extrude** (~0.12, output back), then **Vertex Split** using the `id` attribute (instead of the default Name attribute) to separate each column into its own piece; **Uniform Scale** slightly (~0.1) in Exploded View to create gaps, then **PolyFill** (Weighted Rolls) to cap them cleanly.
5. **UVs, first pass:** group seam edges via **Mean Edge Angle**, then **UV Flatten** on that group with Rectify enabled and Manual Layout disabled — clean UVs at this stage, before any beveling.
6. **Bevel (UV-aware):** PolyBevel excluding flat edges (~0.2 Round, 3 Divisions) — the earlier clean UVs adapt correctly through the bevel. Subdivide + soften normals for preview quality, then tag the whole piece with a custom float attribute (e.g. `barrel = 1`) for later use as a texturing mask target.
7. **Barrel end caps:** a Circle on the ZX plane (32 divisions, small radius) with UVs derived from its own texture coordinate on Y (reversed via negative scale + offset to orient correctly); **Copy and Transform** to duplicate, **Reverse** normals on one copy, then a VEX wrangle pushes both apart along their own normals (`@P += @N * amount`, ~0.53) while tagging a root/origin point attribute for alignment reference before merging.
8. **Barrel hoops:** an **open-arc Circle** (32 divisions) with a range/division attribute (divisions ÷ 4, avoiding awkward UV islands later) for grouping; build an **aperture vector** via `v@up = normalize(v@P)` so the vector points radially outward — required for the later Sweep to orient correctly along the barrel curve. **Match Size** to align the circle to the barrel, offset (~±0.03) to place the first hoop, then **Copy and Transform** (3 copies, small offset) plus **Mirror** (direction Y) to place matching hoops symmetrically top/bottom, and a middle hoop set (centered, offset ~0.15) — merge all hoop copies together.
9. **Fuse** all hoop points (open-arc circles leave an unfused seam point by default — always fuse before sweeping), then **Sweep** (Ribbon mode, 2 columns, Size 0.05) using the earlier aperture vector to keep the ribbon correctly oriented; without that vector the sweep doesn't align to the barrel curvature.
10. **Attach hoops to barrel via ray projection:** merge barrel + hoops, then **Ray** the hoops onto the barrel — a direct Ray (even with Reverse Rays checked) silently fails here, likely due to open/non-manifold barrel geometry; the fix is to first generate a **Convex Hull** proxy from the barrel and ray onto that instead, which works reliably.
11. Add a masking wrangle (`f@ao_type = 1` or similar) purely as a placeholder attribute for later COPS texturing use, and **Peak** the hoops slightly (small distance, ~0.05) off the barrel surface to avoid Z-fighting/clipping.
12. **UV finishing — the extrusion/group problem:** group the unshared edges before extruding the plank backs (~0.03, output back) — a range/division group created earlier ("UV the mesh") only exists on the original front faces and does **not** propagate through the extrusion automatically. Fix with **Group Promote** (points→edges) followed by **Group Find Path** (base group = "range", boundary-only elements, "Loops or Rings, Extend to Edge") — this regenerates the correct edge cuts needed for the UV Flatten across the now-extruded geometry.
13. Final **UV Flatten** using the seam, range, and unshared-edge groups (Rectify on, Manual Layout off) gives clean UVs on the extruded planks; PolyBevel the corners lightly again (small Round value, 3 Divisions, exclude flat edges), subdivide, soften normals, and merge everything (barrel + caps + hoops) together.
14. **UV Layout:** since all pieces' UVs currently overlap, run **UV Layout** with "Scale Islands to Match Surface Area" enabled, increase iterations for better distribution, and add island/boundary padding — final coverage in this example landed around 72%.

### Houdini Nodes / VEX / Settings
Tube → Attribute Wrangle (`relbbox(0,@P)`) → **Ramp** (B-Spline, mirrored handles) driving `@P.x`/`@P.z` scale → Attribute Wrangle (`@primnum % cols` via a `cols` channel reference) → Poly Extrude (output back) → **Vertex Split** (by custom `id` attribute, not Name) → Uniform Scale (Exploded View) → PolyFill (Weighted Rolls) → UV seam Group (Mean Edge Angle) → UV Flatten (Rectify, no Manual Layout) → PolyBevel (exclude flat edges) → Subdivide + soften normals → custom float attribute tag · Circle (ZX plane, reversed/offset texture UVs) → Copy and Transform + Reverse (normals) → VEX push-apart wrangle (`@P += @N*scale`) for end caps · open-arc Circle + range/division group + `v@up = normalize(@P)` aperture vector → Match Size + offset → Copy and Transform + Mirror (hoop placement) → Fuse → **Sweep** (Ribbon, aperture-vector-aligned) for hoops · **Convex Hull** (proxy) + **Ray** (reverse rays) to attach hoops to barrel → Peak (small offset) · unshared-edges Group → Poly Extrude → **Group Promote** (point→edge) → **Group Find Path** (Loops or Rings, Extend to Edge) → final UV Flatten → PolyBevel → Subdivide → **UV Layout** (Scale Islands to Match Surface Area, padding).

### Difficulty
Beginner — explicitly pitched as an introductory exercise; the VEX used is minimal (bounding-box remap, modulo attribute, normal-based push-apart) and every UV step is explained from first principles, though the Group Find Path fix for extrusion-broken groups is a genuinely useful intermediate-level trick.

### Houdini Version
Not stated explicitly; uses only long-standing native SOP nodes (Tube, Ramp, Vertex Split, Sweep, Ray, Convex Hull, UV Flatten, UV Layout, Group Find Path) available in any modern Houdini (H18+).

### Tags
#modelling #procedural #vex #uv #beginner

---

## Related Tutorials
Cross-link with [5 Tips and Tricks for Modeling in Houdini](5-tips-and-tricks-for-modeling-in-houdini.md) — shares #modelling #procedural #vex; both use simple attribute-driven VEX tricks (bounding-box remaps, per-piece attributes) to control procedural geometry without complex node graphs.
