---
title: Rig Builder | Project Overview
source: YouTube
url: https://www.youtube.com/watch?v=VFF2TLfbU3A
author: Houdini
ingested: 2026-07-20
houdini_version: "H21"
tags: [sop, cop, procedural, modelling, texturing, rigging, kinefx, animation, beginner, intermediate, houdini-21]
extraction_status: complete
frames_dir: tutorials/frames/rig-builder-project-overview/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Rig Builder | Project Overview

**Source:** [YouTube](https://www.youtube.com/watch?v=VFF2TLfbU3A)
**Author:** Houdini
**Duration:** 3m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Before we jump into the tutorial series, I just wanted to go through the project itself.
[0:11] There's a lot of pretty exciting stuff going on here for you guys to jump into and check
[0:16] out and hopefully learn from.
[0:19] Everything you see here with this character, the modeling, the texturing, was all done
[0:24] right in Houdini.
[0:26] It was all done right in this project.
[0:29] You can jump into the robot modeling where I did all of the modeling operations.
[0:36] It looks quite complex, but just remember that it's working in any modeling tool.
[0:42] It's just that everything is, all of your operations are being saved.
[0:48] Here's the finger and you have really nice advantages in working in something like Houdini
[0:51] because you just make one finger and just propagate it over all of the fingers and it
[0:57] actually makes things much faster.
[1:00] You can go through and see how I did that.
[1:05] There's a bit of processing done on the actual geometry.
[1:09] I assigned color to the geometry to help out in the texturing process.
[1:16] Just a bit of naming to organize all of my pieces.
[1:21] A lot of the UVs were done here.
[1:25] This is more just the UV layout.
[1:27] This is where I actually created my UDEM UVs.
[1:31] We can jump out of this and go back up.
[1:36] Within the Ibot texturing, this is where I did all of the texturing for the Ibot character.
[1:43] If I go into my COP network, you can see how I actually put together the texture.
[1:50] This looks a little weird because we're using UDEM textures here.
[1:53] At the moment, texturing with cops and UDEMs requires you to actually switch between the
[2:01] UDEMs.
[2:02] That will be fixed in the future, but at the moment, that's why it looks like this.
[2:05] We jump back out.
[2:06] Finally, we actually have the Ibot capture where I created the skeleton.
[2:13] I created the skeleton with pieces.
[2:16] For instance, here's the leg, we have the arm, spine, which is very tiny, and the eye,
[2:25] the fan, and various other things.
[2:28] Combine everything together and do some simple parenting.
[2:33] All of this here is the actual capture.
[2:35] We cache the capture out.
[2:40] Everything happens a lot faster.
[2:41] I center the model along with the joints and I assign the materials and create the FBX
[2:49] material name.
[2:52] In the first episode of this tutorial series, we're going to actually create a new geometry
[2:57] node and import that FBX that we made before.
[3:01] From that FBX, we're going to create our rig.
[3:06] Let's go ahead and jump in and create a rig for this guy.



---

## Captured Frames

- [0:35] tutorials/frames/rig-builder-project-overview/frame_000.jpg
- [1:05] tutorials/frames/rig-builder-project-overview/frame_001.jpg
- [1:40] tutorials/frames/rig-builder-project-overview/frame_002.jpg
- [2:10] tutorials/frames/rig-builder-project-overview/frame_003.jpg
- [2:45] tutorials/frames/rig-builder-project-overview/frame_004.jpg

---

## Structured Notes

### Core Technique
Project/asset-prep walkthrough (not the Rig Builder tool itself) for the "iBot" character — a spherical eyeball-bodied robot — showing the fully-procedural Houdini pipeline (modeling, UDIM UVs, COPs texturing, skeleton/capture, FBX export) that feeds into the Rig Builder tutorial series' first episode.

### Summary
Max Rose (SideFX) tours the Houdini 21 project file used throughout the Rig Builder Series before the hands-on episodes begin, to show that the whole iBot character — modeling, texturing, and skeleton capture — was built entirely inside Houdini. Covers: procedural robot modeling (built once for one finger/limb piece and propagated across symmetric parts for speed), geometry processing (color-assignment per piece to aid texturing, naming/organizing pieces), UDIM UV layout, texturing via a COP2 network (noting that COPs + UDIMs currently requires manually switching between UDIM tiles — a workflow limitation the presenter says will be fixed in the future), and skeleton creation/capture (built joint-by-joint per body part — leg, arm, spine, eye, fan/ear pieces — then combined with simple parenting, cached out for faster iteration). Ends by centering the model on the joints, assigning materials, and exporting an FBX with material names — which becomes the import source for the actual first Rig Builder episode ("create a new geometry node, import the FBX, and build the rig from it").

### Key Steps
1. Model the character procedurally in Houdini SOPs — build one instance of a repeated part (e.g. one finger) and propagate/instance it across symmetric copies rather than modeling each by hand.
2. Geometry processing pass: assign per-piece color attributes to aid the texturing step, and apply consistent naming to organize all the character's geometry pieces.
3. UV layout: lay out UVs per piece, then author UDIM tiles for the final texture set.
4. Texture in a **COP2 (Copernicus/COPs) network** — noted limitation: texturing with COPs across UDIMs currently requires manually switching the active UDIM tile in the network (a workflow gap the presenter expects SideFX to improve).
5. Build the skeleton in labeled sections — Skeleton Creation (per-part joints: leg, arm, spine, eye, fan/other) → Skeleton Assembly (combine + simple parenting) → Capture (bind geometry to the assembled skeleton), then cache the capture to disk so later iteration is fast.
6. Finishing steps before handoff to Rig Builder: center the model on its joints, assign materials, and export an FBX with proper material names — this FBX is the exact asset imported in Episode 1 of the Rig Builder series to begin building the actual rig.

### Houdini Nodes / VEX / Settings
- **Pipeline stages shown on screen (network banners):** Geometry Processing → Texturing → Skeleton and Capture → (Center Character / export).
- **Contexts used:** SOPs (modeling, geometry processing, UV layout), COP2/Copernicus (UDIM texturing network), KineFX-style skeleton/capture SOPs (Skeleton Creation, Skeleton Assembly, Capture subnetworks visible in the network pane).
- No VEX/parameter values called out verbally in this overview — it is a tour of network organization, not a hands-on build (the hands-on rig build is in the numbered episodes of this same series, e.g. "Rig Builder 1 | FBX Import").

### Difficulty
Beginner-to-Intermediate — an orientation/context video; the procedural-modeling and COPs/UDIM content requires some prior Houdini familiarity but nothing is built hands-on here.

### Houdini Version
Houdini 21 (Rig Builder Series).

### Tags
sop, cop, procedural, modelling, texturing, rigging, kinefx, animation, beginner, intermediate, houdini-21

---

## Related Tutorials
- `tutorials/rig-builder-introduction.md` — the series' 26-second trailer clip (needs-review, no real content) for the same Rig Builder Series/presenter; shares tags: apex, rigging, kinefx, houdini-21.
- `tutorials/apex-rigging-h20-masterclass.md` — broader APEX/KineFX rigging content; shares tags: rigging, kinefx, animation.
- `tutorials/basic-procedural-texturing-with-cops-in-houdini-21.md` — COPs texturing workflow in the same Houdini version; shares tags: cop/cops, texturing, procedural.
