---
title: Procedural tips | Heightfields and VDB
source: YouTube
url: https://www.youtube.com/watch?v=Ue-Wuo87YJI
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.593"
tags: [heightfields, vdb, terrain, vex, volumes, optimization, masks]
extraction_status: complete
frames_dir: tutorials/frames/procedural-tips-heightfields-and-vdb/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural tips | Heightfields and VDB

**Source:** [YouTube](https://www.youtube.com/watch?v=Ue-Wuo87YJI)
**Author:** cgside
**Duration:** 2m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back.
[0:03] Let me share with you a few tips when dealing with light fields in Odini.
[0:07] The first one is how you can use the light field pattern to mask out parts of the terrain.
[0:13] I am using a ramp and playing with the height and center and in this case using it to create
[0:20] some elevation with the remap node.
[0:23] Now I want to create some cliff-like sections on the terrain and for that I use the terrorist
[0:29] but I ended up masking it using a light field mask noise so it's not everywhere.
[0:35] As you can see the default look of the terrorist is not so great.
[0:40] This one might be obvious but I honestly didn't know till recently.
[0:45] I wanted a section of a bigger cliff face at the front so I used a ramp to mask out
[0:51] that part and multiply the noise on top.
[0:55] But then I wanted a bigger area and while I could use a mask expanse playing with the
[1:00] bias of the noise will actually work better to grow and shrink the area.
[1:07] So the next one is an optimization tip when you are working with volume vox and want
[1:13] to clip an area of a VDB.
[1:16] Using the VDB clip you can just connect the box and cut the section to speed up the calculation
[1:22] of the volume vox while maintaining the scale of the noises and the same resolution.
[1:28] Let's say you want to preview a noise, you have volume vox as a color attribute.
[1:34] You can first add a CD attribute using a color node.
[1:38] Then in the VDB from polygons you can pass this attribute and give it a VDB name.
[1:44] Next you'll notice a fog-like preview of the attribute so you might want to hide it
[1:49] using a visibility node.
[1:53] So inside the VOP I am mixing two different noises and using another one as the mixed factor
[2:01] and I wanted to preview it so I can simply bind the export as a vector, the resulting noise
[2:08] and finally using an attribute from volume to see the result.
[2:13] So that's what I wanted to share, feel free to grab the scene on my Patreon and I hope
[2:18] you have learned something new today.
[2:20] See you in the next time.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-tips-heightfields-and-vdb/frame_000.jpg
- [0:40] tutorials/frames/procedural-tips-heightfields-and-vdb/frame_001.jpg
- [1:10] tutorials/frames/procedural-tips-heightfields-and-vdb/frame_002.jpg
- [1:40] tutorials/frames/procedural-tips-heightfields-and-vdb/frame_003.jpg
- [2:10] tutorials/frames/procedural-tips-heightfields-and-vdb/frame_004.jpg

---

## Structured Notes

### Core Technique
A grab-bag of five Heightfield/VDB tips: masking terrain with Heightfield Pattern, masking Erosion with noise so cliffs aren't everywhere, using noise bias instead of Mask Expand to grow/shrink an area, clipping a VDB with a box before Volume VOP for speed, and previewing a volume noise attribute via a Color-node/Attribute-from-Volume round-trip.

### Summary
Heightfield Pattern combined with Remap creates elevation masks (height/center controls). A second Heightfield Pattern (Chippy Shapes) masks where Erosion is applied so cliff-like breakup only appears in some areas rather than uniformly, since Erosion's default look isn't great everywhere. For growing/shrinking a masked area, playing with a noise's **bias** works better than Mask Expand. For performance, VDB Clip lets you cut a box-bounded section of a volume before running expensive Volume VOP noise, speeding up iteration while preserving the noise's scale/resolution. Finally, to preview a volume attribute (e.g. a mixed-noise factor) without exporting it formally, a Color node writes it into `Cd` before VDB from Polygons, then Attribute from Volume reads it back as a visible attribute after conversion.

### Key Steps
1. **Terrain masking**: use Heightfield Pattern's mask output with a Ramp, playing with height and center parameters, then feed it into Remap to shape elevation.
2. **Selective cliff detail**: apply Erosion for cliff-like sections, but mask it using a Heightfield Pattern noise (Chippy Shapes) so cliffs don't appear everywhere — default Erosion coverage looks poor across a whole terrain.
3. **Section masking with Ramp + multiply**: for a bigger cliff face at the front, use a Ramp to mask that region and multiply the noise on top of it.
4. **Growing/shrinking masks — the "obvious in hindsight" tip**: rather than Mask Expand, adjusting the **bias** of the underlying noise grows/shrinks the masked area more naturally and with better control.
5. **VDB Clip for optimization**: when iterating on a Volume VOP setup, connect a box into **VDB Clip** to cut down the working volume section before running expensive noise calculations — speeds up feedback while preserving the same noise scale/resolution as the full volume.
6. **Previewing a volume attribute as color**: add a `Cd` attribute via a **Color node**, pass it through in VDB from Polygons with a VDB name, then hide the resulting fog-like preview with a Visibility node.
7. **Reading the attribute back**: inside the Volume VOP, mix two noises using a third as the mix factor, Bind Export the resulting vector, then after conversion use **Attribute from Volume** to see the final mixed-noise result as a real point/primitive attribute.

### Houdini Nodes / VEX / Settings
Heightfield Pattern (mask, Chippy Shapes), Heightfield Remap, Ramp, Heightfield Erosion (mask-controlled), noise bias parameter (vs. Mask Expand), VDB Clip (box-bounded optimization), Color node (Cd export), VDB from Polygons (named VDB attribute), Visibility node, Volume VOP (Bind Export, noise mixing), Attribute from Volume.

### Difficulty
Intermediate (assumes familiarity with Heightfields and Volume VOPs; the tips themselves are quick/practical).

### Houdini Version
19.5.593 (visible in viewport title bar).

### Tags
heightfields, vdb, terrain, vex, volumes, optimization, masks

---

## Related Tutorials
- [Procedural VDB Cookies](procedural-vdb-cookies.md) — shares the same Color-node/Attribute-from-Volume attribute-preview trick used here.
- [Rock formations with heightfields](rock-formations-with-heightfields.md) — fuller heightfield workflow building on the masking techniques covered here.
- [Houdini Heightfields and Cliffs](houdini-heightfields-and-cliffs.md) — related heightfield erosion/masking techniques from the same channel.
