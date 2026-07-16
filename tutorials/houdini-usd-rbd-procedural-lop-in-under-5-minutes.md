---
title: Houdini USD RBD Procedural LOP in under 5 minutes
source: YouTube
url: https://www.youtube.com/watch?v=ixJvo0iShiM
author: the point and prim
ingested: 2026-07-16
houdini_version: "Not specified"
tags: [rbd, usd, solaris, procedural-lop, transform-pieces, piece-name, karma, the-point-and-prim]
extraction_status: complete
frames_dir: tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini USD RBD Procedural LOP in under 5 minutes

**Source:** [YouTube](https://www.youtube.com/watch?v=ixJvo0iShiM)
**Author:** the point and prim
**Duration:** 4m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome. So over the last week I've spent my mornings doing some R&D into some techniques for appresing RBDs.
[0:08] I'll be featuring those techniques in a future video, but basically this involves doing a lower SIM which then influences a much higher SIM.
[0:17] As you can imagine this geometry gets heavy pretty quickly. Even in my R&D tests I'm hitting over 2 million points and that's not even production quality.
[0:26] Thankfully there is this magical node called Transform Pieces.
[0:29] If you've done RBD in any serious capacity before you will know all about it.
[0:34] It allows us to load our Render Fractura just once and then apply the transforms from a point cloud onto it.
[0:39] Wish us super efficient and lightweight on disk compared to saving the entire geometry per frame.
[0:45] Great so that's that problem solved and life is good right?
[0:48] Wrong. The problem rises when we start rendering this with Karma.
[0:54] Lops will convert this geometry into USD as soon as you import it into Solaris.
[0:59] Heavy geometry is fine if it's just a static frame but if you have a heavy effect sequence like this it will actually import and do the conversion on every frame which becomes really cumbersome.
[1:08] Thankfully side effects are thought about this and as built the Houdini procedural RBD Lop which emulates the behavior of Transform Pieces in Solaris.
[1:18] You would expect this node to work like Transform Pieces out of the box but sadly it doesn't due to some USD specific quirks.
[1:25] On top of this the documentation is convoluted and confusing.
[1:29] The good news is that we can summarize this entire document with just two Wrangles.
[1:33] I've got a fresh scene here with some Fractura Geo for demonstration purpose.
[1:38] I've got the Proxy Geo Sim here, the Hyrus Fractura that will be rendered on this side, and the RBD points which are being used to apply the transforms of the lower range.
[1:46] Usually we use the name attribute to retrieve the orientation and translation from the points so all we would need to do is make sure the attribute matches on both.
[1:56] When importing our geometry to Solaris both the path and the name attribute are reserved by Houdini for building the Prim hierarchy with path taking precedence and name serving as a backup.
[2:06] This means we can't just use the name attribute like always.
[2:09] Side effects build a workaround for this directly into the procedural in the form of the piece name attribute which is what the giant document is for.
[2:16] So let's build our version of this. Here I have my render Geo making sure it is unpacked.
[2:22] Then I have a Wrangle declaring the path attribute. In this case just slash Geo slash Taurus. Note that I still have the same name attribute here.
[2:31] We then use an attribute swap to move the name attribute into piece name. You can use whatever method you want just make sure the original name attribute gets deleted.
[2:40] In the other stream we've got our RBD points.
[2:43] In this Wrangle we are just fetching the path attribute from the first Wrangle and adding the points name attribute to it to construct piece name.
[2:50] Again making sure we clean up the original name using an attribute delete here. This means on the points we only have the piece name attribute which is the path attribute from the geometry plus the name attribute.
[3:00] Here is a recap of the attributes you will need along with a nice blurry screenshot of the note graph.
[3:07] Let's bring these elements into lots. We can import both these using SOP imports for now. Make sure to check the singrof to validate if your prim hierarchy is correct for your needs.
[3:18] Now drop down a Hedunny RBD procedural lump. Select the Geo prim in the RBD primitive field and the points in the point primitive.
[3:29] You also have the option to reference the points from SOPS or directly from disk with the latter providing large speed improvements with heavier simulations.
[3:36] The next most common question after doing this is going to be how do I get motion blur on this thing. Luckily that is easily solved with a render geometry settings node.
[3:45] Select the geometry itself and not the RBD procedural. If we plug in some lights and a material we can see that that is working as expected.
[3:54] If all of this is still not making sense, I am giving away the Taurus hip file for free on my gumroot so you can download that to inspected further.
[4:03] Link below. I hope you found this video helpful and good luck smashing some RBD shots. Bye for now.



---

## Captured Frames

- [0:26] tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/frame_000.jpg
- [1:08] tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/frame_001.jpg
- [2:22] tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/frame_002.jpg
- [2:43] tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/frame_003.jpg
- [3:18] tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/frame_004.jpg
- [3:45] tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/frame_005.jpg

---

## Structured Notes

### Core Technique
Correctly wiring the **Houdini RBD Procedural LOP** in Solaris to replicate SOP-level "Transform Pieces" efficiency (load render geometry once, apply per-frame transforms from a lightweight point cloud) by manually constructing the reserved **`piece_name`** attribute with two simple wrangles, working around USD's reservation of both the `path` and `name` attributes.

### Summary
A short, practical breakdown (part of the author's larger RBD up-res R&D work) on why RBD rendering gets awkward once it moves into Solaris/USD, and how to fix it in two wrangles. The setup problem: **Transform Pieces** (a SOP-level node any experienced RBD artist knows) loads a render-resolution fracture once and applies per-frame orientation/translation from a much lighter point cloud, avoiding the cost of writing full geometry to disk every frame — cited as hitting over 2 million points even in early R&D tests. The catch is that Karma/Solaris converts imported SOP geometry into USD on import, and unlike a static frame, a full heavy animated sequence gets re-converted **every single frame**, which is very slow. Side FX's answer is the **Houdini RBD Procedural LOP**, which emulates Transform Pieces' behavior inside Solaris — but it doesn't work out of the box the way Transform Pieces does, and its documentation is described as "convoluted." The whole workaround boils down to two wrangles because of a USD-specific quirk: normally Transform Pieces matches `name` on both the render geometry and RBD points, but when importing into Solaris, **both `path` and `name` are reserved attributes** used by Houdini to build the USD prim hierarchy (`path` takes precedence, `name` is a fallback), so the RBD Procedural can't simply reuse `name` — it instead expects a `piece_name` attribute (documented at length, but reducible to two small wrangles). On the render geometry (unpacked): one wrangle declares the USD `path` attribute (e.g. `/geo/Taurus` in the demo) while the original `name` attribute is still present; a second **Attribute Swap** node moves `name`'s value into `piece_name` (any method works, as long as the original `name` is deleted afterward so it doesn't collide with USD's reserved use). On the RBD points (the transform source): a wrangle reads the `path` attribute fetched from the geometry stream and concatenates it with the point's own `name` attribute to construct the matching `piece_name`, again deleting the original `name` attribute afterward via Attribute Delete. Both streams then only carry `piece_name` where USD would otherwise expect `name`. In Solaris: both streams come in via **SOP Import** (checking the Scene Graph tree to validate the prim hierarchy), a **Houdini RBD Procedural LOP** is dropped, the geometry prim is set in the RBD Primitive field and the points in the Point Primitive field (with an option to reference points either from SOPs or directly from disk — the latter giving large speed improvements on heavier sims). Motion blur on the resulting procedural geometry is solved with a **Render Geometry Settings** LOP applied to the geometry itself (not the RBD Procedural node). The demo uses a torus ("Taurus") hip file, which the author gives away for free on Gumroad.

### Key Steps
1. Understand the underlying problem: **Transform Pieces** at the SOP level loads render geometry once and drives it from a lightweight per-frame point cloud (very efficient), but Solaris/Karma converts SOP-imported geometry to USD on every single frame of a heavy animated sequence unless a dedicated LOP-level workflow is used.
2. On the **render geometry** stream (unpacked): add a wrangle that declares the USD `path` attribute (e.g. `s@path = "/geo/Taurus";`) while `name` is still present from the fracture.
3. Use an **Attribute Swap** to move the value of `name` into a new `piece_name` attribute, then delete the original `name` attribute (any method works as long as `name` doesn't survive, since USD reserves it).
4. On the **RBD points** stream: write a wrangle that reads the `path` attribute (fetched from the geometry stream) and concatenates it with each point's own `name` attribute to build `piece_name` on the points too.
5. Delete the original `name` attribute on the points stream with **Attribute Delete** so only `piece_name` remains where USD would otherwise expect `name`.
6. Bring both streams into Solaris via **SOP Import**, checking the Scene Graph Tree tab to validate the resulting prim hierarchy.
7. Drop a **Houdini RBD Procedural LOP**, set the geometry prim in the RBD Primitive field and the points prim in the Point Primitive field; optionally reference points directly from disk instead of SOPs for large speed gains on heavier sims.
8. Add a **Render Geometry Settings** LOP targeting the geometry (not the RBD Procedural node) to enable motion blur.
9. Validate by plugging in lights and a material and confirming the transforms/motion blur render as expected.

### Houdini Nodes / VEX / Settings
Transform Pieces (SOP-level reference technique), Houdini RBD Procedural LOP (RBD Primitive / Point Primitive fields, SOPs-vs-disk point source option), `path` attribute (USD prim-hierarchy, reserved), `name` attribute (USD-reserved, must not survive), `piece_name` attribute (workaround construct), wrangle (`s@path = "..."`, string concatenation for `piece_name`), Attribute Swap, Attribute Delete, SOP Import (Scene Graph Tree validation), Render Geometry Settings LOP (motion blur).

### Difficulty
Intermediate (the concept is simple once explained, but requires understanding USD's reserved `path`/`name` attributes and Solaris-specific import behavior that isn't obvious from Transform Pieces' SOP-level workflow).

### Houdini Version
Not specified.

### Tags
#rbd #usd #solaris #procedural-lop #transform-pieces #piece-name #karma #wrangle #the-point-and-prim

---

## Related Tutorials
- [Art directing large scale RBD sims in Houdini using the up-res method](art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method.md) — same channel/author; that video's Solaris rendering section uses this exact RBD Procedural LOP setup, referencing this tutorial for the detailed breakdown.
- [RBD Procedural Animations in Houdini | Mardini 2026](rbd-procedural-animations-in-houdini-mardini-2026.md) — different author (cgside); directly overlapping RBD Procedural LOP / USD subject matter.
- [Cleaning fractured geometry in Houdini](cleaning-fractured-geometry-in-houdini.md) — different author (cgside); complementary fracture-preparation content in the same RBD pipeline area.
