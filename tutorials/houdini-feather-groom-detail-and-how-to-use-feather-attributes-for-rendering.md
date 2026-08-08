---
title: Houdini Feather Groom Detail and how to use Feather Attributes for Rendering
source: YouTube
url: https://www.youtube.com/watch?v=kSIn2FCzW0c
author: Alexander Weber
ingested: 2026-08-08
houdini_version: "19.5+/20.x (Solaris Feather Procedural)"
tags: [feather, feather-groom, gumi, hair-clump, hair-gen, hair-split, hair-mask, curveu, primvar, solaris, feather-procedural, reference-imagery, featherbase, renderman]
extraction_status: complete
frames_dir: tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini Feather Groom Detail and how to use Feather Attributes for Rendering

**Source:** [YouTube](https://www.youtube.com/watch?v=kSIn2FCzW0c)
**Author:** Alexander Weber
**Duration:** 7m31s | 2 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### How to use the Node [0:00]
**Transcript (timestamped):**
[0:00] So you created your beautiful feather using the feather template, maybe also the feather width, and then you try to create some more detail with the feather noise and feather clump, but this just wasn't enough, and that's why I created the feather boom detail.
[0:18] So you're just gonna throw it down and right off the bat you could adjust the shaft width, but yeah, you don't have to, and then let's just dive inside. So the way this works is that it just decomposes everything, it's not like a workflow that I came up with, but it's just out there and this not just implemented quite well.
[0:43] So you now have curves, and with those curves obviously you can use all of Houdini's tools to adjust them and shape them in whatever way you want, and for example there's guide process and all the Gumi nodes which work quite well with this, so you can just plug this in, maybe connect everything.
[1:02] So now you can see already those just adjust the length, and if you go back up and look on this node, you already have this detail on there, and yeah, with these examples that I plugged down, you can just copy them over and then adjust them or you can come up with stuff on your own.
[1:22] So let's plug this in. So one thing that I noticed, and I don't know why because I'm not that much of a Guma, you can grab this, is that you also need to connect the shaft as the skin up here, and for whatever reason then those nodes work again.
[1:39] So as you can see here I did the hair gen and then just bend those hairs and in the end use the hair clump to get this detail onto my barbs, so you don't want to change the number of barbs you have and the point count and whatever, this just doesn't work.
[1:59] So if you are going to do some heavy adjustments like I did here, then you always have to use a node that transfers those adjustments onto your actual barbs. This is what the hair clump node does for me right here.
[2:12] And sometimes you might also want to split which hairs you're just going to affect, so this is a way to split. Then you also have mask which basically do the same but yeah, sometimes you need this and sometimes you need that.
[2:27] Then you can also do random groups and frizz and whatever, you can just adjust those curves in whatever way and this node will transfer onto the visualized barbs.
[2:41] So this is basically already it. There's another feature which I'm going to quickly show. I have one prepared here. Let me just disable this again. So this is also not something which I spent too much time achieving, but we can also have a quick look inside.
[3:00] So yeah, that's basically the same I guess. And over here I actually used the split node and then I guess I'm just adjusting the barbs down here and merging them back together.
[3:14] And yeah, this just transfers everything over here. And then sometimes you want to take an image and basically work on that image. These images you can find easily on the featherbase.info.
[3:29] It's like a nice website where you can, if you know the names of the biological names or whatever the science of birds is called, you can search them up and then choose the bird that you want.
[3:42] Let's take this one and then you get all the feathers. So if you want to make a specific bird then this website is really nice to see how the feathers of these birds look.
[3:54] And yeah, so sometimes you take the image and want to base it on that. So you can plug the image in here. This is just a cup network that you just do a file and then sometimes you have to adjust the rotation a bit and whatever.
[4:07] So and then if you are doing that, I have this little checkbox which enables quickshade and then you get this image onto your feather.
[4:16] This already creates the UVs in a way that those images will always fit your feather.
[4:21] And in case you don't want to use it for rendering in the end because this obviously doesn't look too good, then you can also create your own UVs with the normal projector V-node which is included in here.
[4:33] That's already basically it. Be free to ask any questions if they come up and maybe this node is also not perfect. I haven't tried it around with it too much so it could be that they have some flaws in it. Just let me know.


### Using Attributes for Rendering [4:45]
**Transcript (timestamped):**
[4:45] So I just realized that I haven't talked about this channel yet and how to transfer attributes that aren't usually on your barbs onto your barbs. So I'm going to real quick show you how to do that.
[5:02] So I just took a few as an example. So just resample nodes then you get this nice gradient from root to tip of your barb.
[5:10] Obviously if you do this, don't ever actually resample those. I mean you could but we don't want to do that because this probably breaks some stuff. I haven't actually tried it.
[5:21] But there's no need to do this. You can do the upstream so don't do it.
[5:26] And yeah I did that on both sides obviously. So then if we go up, you might be wondering, okay there's no curvy on here and this is what this channel is for. So just plug curvy in here and then this automatically creates the curvy which in this case goes from root to tip of the shaft which is not really what we had inside.
[5:52] But it also creates curvy for barb L and barb R so left and right side. Sadly you cannot really inspect this here but this is also true for the width and the UVs.
[6:03] All those channels, okay obviously UVs is different but yeah if you have a channel that's on barbs you cannot really inspect those.
[6:11] And you can just quickly import this into lobs and I'm going to show you how this setup works. It's just default feather setup but yeah.
[6:19] So just create a primitive for the feather then import your feather. Then we use the Houdini feather procedure. Then you use the feather primitive. Then your goom that you imported.
[6:34] One thing that I always do is uncheck velocity because I don't use the deforming of this node. If you use the deforming of this node then obviously you want the velocity but if you don't do it, use it then this will overwrite your velocity that you might have on your feathers already.
[6:50] And yeah that's going to cause some problems. Then you just have to plug the curvy in here. You don't need to add the barb L or barb R just a normal curvy and then this node knows how to convert those back to being a normal curvy.
[7:05] So you can just use this in a shader. So I just use the curvy, call it with a prim bar. This is render man but yeah I'm sure you know which nodes can do that for a karma or whatever else.
[7:19] And then if we hit up the renderer let's quickly do that. And you can see the curvy works while rendering. Yeah and that's basically it.



---

## Captured Frames

- [0:18] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_000.jpg
- [0:43] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_001.jpg
- [1:22] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_002.jpg
- [1:39] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_003.jpg
- [2:12] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_004.jpg
- [3:14] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_005.jpg
- [3:54] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_006.jpg
- [4:07] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_007.jpg
- [5:02] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_008.jpg
- [5:52] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_009.jpg
- [6:19] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_010.jpg
- [6:34] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_011.jpg
- [7:19] tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/frame_012.jpg

---

## Structured Notes

### Core Technique
A creator-made custom HDA, **Feather Groom Detail**, that goes beyond the stock Feather Template/Feather Width/Feather Noise/Feather Clump nodes: it decomposes a feather into individual curves so any of Houdini's standard hair/fur grooming tools (Guide/Gumi nodes — Hair Gen, Hair Bend, Hair Clump, Hair Split, Hair Mask, Hair Frizz, Hair Groups) can be applied directly to the barbs for fine detail, plus a separate second half covering how to get non-standard barb attributes (curveu, width, UVs) onto the actual render-time curves for use in a shader.

### Summary
**Part 1 — Feather Groom Detail node:** Drop the node after building a feather with the stock Feather Template/Width/Noise/Clump chain; it exposes a Shaft Width param but works fine at defaults. Internally it decomposes the feather geometry into individual curves, which unlocks the full Gumi/hair-tool palette (Guide Process and friends) instead of being limited to the feather-specific nodes. A quirk noted: **you must connect the shaft as the "skin" input** on the Gumi nodes for them to actually work — without that connection the standard Gumi tools silently fail to affect anything, for reasons the creator says they don't fully understand ("not that much of a Gumi [expert]"). Demonstrated chain: **Hair Gen** to grow/bend hairs off the barbs, then **Hair Clump** to transfer that adjustment back onto the visualized barb geometry — critically, any heavy curve-level adjustment (bend, frizz, etc.) needs to go through a node like Hair Clump to actually apply to the render-visible barbs; editing the decomposed curves alone does nothing to the barbs on its own. Do **not** change barb count or point count when doing this — it breaks. **Hair Split** and **Hair Mask** both let you restrict which hairs/barbs an adjustment affects (functionally similar, situationally one or the other is more convenient). **Hair Groups** + frizz can add further per-group randomized variation. A second included example repeats the same idea but demonstrates using **Hair Split** to isolate a subset of barbs, adjust them independently, then merge back — for localized rather than whole-feather detail. Finally, the node supports **image-based feather texturing**: a Cop2 network reads a reference photo (the creator recommends **featherbase.info** — a site organized by bird species/biological name where you can browse real reference photos of each species' actual feathers) plugged into the node, with a rotation adjustment as needed and a "Quickshade" checkbox to preview the image mapped onto the feather; the node auto-generates UVs that always fit the feather shape for this purpose. If you don't want image-driven UVs for final rendering, the node also includes a normal Project UV option as an alternative.

**Part 2 — Transferring non-standard attributes onto barbs for shading:** Feather barbs don't carry `curveu` (the standard root-to-tip 0-1 gradient used for e.g. color ramps in shaders) by default, and you can't directly inspect per-barb channel data. Fix: use **Resample** nodes upstream (never resample the actual final barb curves directly — apply the fix earlier in the chain, on the pre-barb curve source, since resampling final barbs risks breaking things downstream) on both the left (`barb_l`) and right (`barb_r`) curve sources to establish even segment spacing, then feed those into the Feather Groom Detail-style channel setup so a `curveu` channel is generated automatically per barb, running root-to-tip along the shaft (not perfectly matching the original per-barb geometry, but functional). The same channel mechanism also carries width and UV data per barb even though those can't be directly inspected on the curve visualization. In **Solaris/LOPs**: create a feather primitive, import your feather SOP network, run it through the **Houdini Feather Procedural** LOP with the feather primitive and your groom plugged in. **Uncheck Velocity** on that node unless you're actually using the node's built-in deformation — leaving it checked when you don't need deformation silently overwrites any velocity attribute already authored on your feathers, causing motion-blur/sim problems. Plug the generated `curveu` in (barb L/R channels aren't needed separately — the node converts a single `curveu` back to the correct per-barb data internally). In the shader (demoed in RenderMan, but the same idea applies to Karma or any renderer with an equivalent node), read the curve attribute via a primvar/curve-attribute node (`primvar` called with a curve-bind mode) to drive shading — confirmed working by rendering the feather with `curveu`-driven variation visible along each barb.

### Key Steps
**Feather Groom Detail node:**
1. Build a feather with the standard Feather Template → Feather Width → Feather Noise → Feather Clump chain first.
2. Drop Feather Groom Detail after that chain; leave Shaft Width at default unless you need to change it.
3. Wire the shaft as the **skin** input on any Gumi/hair node you plug in downstream (Guide Process, Hair Gen, Hair Bend, etc.) — without this the Gumi tools don't affect anything.
4. Use Hair Gen/Hair Bend for coarse shaping, then route the result through **Hair Clump** to actually transfer the adjustment onto the visualized barb curves (adjusting the decomposed curves alone does not affect the barbs without a transfer node).
5. Never change barb/point count while doing this — breaks the setup.
6. Use Hair Split or Hair Mask to restrict an adjustment to a subset of barbs; use Hair Groups + Frizz for randomized per-group variation.
7. For image-based texturing: build a Cop2 network reading a reference photo (featherbase.info for real per-species feather references), plug it into the node, adjust rotation as needed, enable Quickshade to preview — auto-generated UVs always fit the current feather shape. Use the included Project UV node instead if you don't want image-driven UVs for final render.

**Attribute transfer for rendering:**
1. Add Resample nodes upstream on both `barb_l` and `barb_r` curve sources (not on final barb curves) to get even segment spacing.
2. Feed those into the groom-detail channel setup to auto-generate a `curveu` (root-to-tip) channel per barb; width and UV channels are also carried this way even though they can't be directly inspected on the curve display.
3. In Solaris: create a feather primitive, import the feather SOP, run through the Houdini Feather Procedural LOP with the feather primitive + your groom network plugged in.
4. Uncheck Velocity on that node unless actually using its deformation feature — otherwise it silently overwrites any pre-existing velocity attribute.
5. Plug the generated `curveu` into the node's curveu input (no need to separately handle barb L/R — it's converted back to per-barb data internally).
6. In the shader, read the curve attribute via a curve-bind/primvar node (RenderMan shown; Karma/other renderers have an equivalent) to drive shading variation along each barb.
7. Render to confirm the attribute is actually driving visible per-barb variation.

### Houdini Nodes / VEX / Settings
Feather Template, Feather Width, Feather Noise, Feather Clump (stock feather nodes), custom **Feather Groom Detail** HDA (Shaft Width param; decomposes feather into curves), Gumi/hair tools: Guide Process, Hair Gen, Hair Bend, **Hair Clump** (transfers curve edits onto visualized barbs — required step), Hair Split, Hair Mask, Hair Groups, Frizz — all require the shaft wired as the **skin** input to function. Cop2 network (image read + rotation) for reference-photo texturing, Quickshade toggle, auto-fit UV generation, alternate Project UV node. Resample (applied upstream on `barb_l`/`barb_r`, not final barbs) to establish even spacing before channel generation; auto-generated `curveu`/width/UV per-barb channels. Solaris/LOPs: feather primitive creation, **Houdini Feather Procedural** LOP (Velocity checkbox — uncheck unless using built-in deformation), curve-attribute/primvar bind node in the shader (shown in RenderMan) to read `curveu` for shading.

### Difficulty
Intermediate/Advanced — assumes familiarity with Houdini's hair/fur (Gumi) grooming toolset and feather-specific nodes already; the value here is bridging feather workflows into that broader hair toolset and getting custom per-barb attributes through to a shader, not a from-scratch feather tutorial.

### Houdini Version
Not stated on screen; Solaris/LOPs Feather Procedural workflow consistent with a recent H19.5+/20.x release.

### Tags
feather, feather-groom, gumi, hair-clump, hair-gen, hair-split, hair-mask, curveu, primvar, solaris, feather-procedural, reference-imagery, featherbase, renderman

---

## Related Tutorials
None yet in this library on feather grooming or barb-level attribute transfer for rendering — first entry covering this.
