---
title: module i   week 06   01   introduction to grains v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=XPDsqVutqDw
author: The VFX School Archive
ingested: 2026-06-19
houdini_version: "Houdini 18.5"
tags: [dop, sop, vellum, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-06-01-introduction-to-grains-v1-1080p/
frame_count: 4
---

# module i   week 06   01   introduction to grains v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=XPDsqVutqDw)
**Author:** The VFX School Archive
**Duration:** 9m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Okay, so we're starting with uh grains. Not starting, we're finishing with grains, I suppose. Um so, we're going to create a new project. The name will be module whatever you like, but this is module one. Week six. In 2D. Okay, uh accept. And then save the hip. Very important. Good to go. And then uh let's call it uh uh module one week six dot grains dot version one. Hip. Great. Okay. Um so, now we need to find that project and bring in our um files, our FBX. So, here's the project. Just drag it in. And then I've got the FBX here, so go I'll leave that in Do we have an FBX folder? We don't. Uh we can just leave it in geo. And drag that uh zombie death in there. Okay, and then we can go to file import filmbox FBX. And then go ahead and find that. So, I saved it into geo, zombie death, accept, import. There we have it. Uh space bar and F, and we can see our lovely zombie. Okay. Um so, first of all, he's too big, so I'm going to press P here and point to one. Space bar and F, and then we can see, you know, roughly a bit under two meters, which is about right. And then I'm going to create a geometry node. And call this uh grain. And we're going to object mer...

**Frame:** tutorials\frames\module-i-week-06-01-introduction-to-grains-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Introducing Vellum grain simulations using an FBX zombie animation as the source, scattering grain particles throughout the body volume and using the animated mesh as a deforming collider for a disintegration effect.

### Summary
FBX import workflow: File -> Import Filmbox FBX, then scale down to 0.1 for proper scene scale (~2m character height). Creates a geometry node, uses Object Merge to bring in the zombie, then converts it via VDB From Polygons -> Points From Volume to scatter grain particles throughout the body volume. The grain setup uses the Vellum Grains shelf tool to create the PBD grain solver. Key grain parameters covered: particle separation (controls density), pscale (render size), friction and restitution. The animated zombie is used as a deforming collider so grains interact correctly with the moving body, producing a pour-out/disintegration sand effect as it dies. Notes that Renascence 1.0 uses the Vellum Grains DOP path rather than the older POP Grains node.

### Key Steps
1. [Import FBX] File -> Import Filmbox FBX; scale to 0.1 for correct real-world scene scale
2. [`Object Merge`] Bring the zombie geometry into the working network
3. [`VDB From Polygons`] Convert the zombie mesh to a volume
4. [`Points From Volume`] Scatter grain seed points throughout the body volume
5. [Vellum Grains shelf tool] Build the PBD grain solver from the scattered points
6. [Tune grains] Set particle separation, pscale, friction and restitution
7. [Deforming collider] Use the animated zombie mesh as a collider so grains react to body motion
8. [Result] Grains pour from the zombie as it dies, producing the disintegration effect

### Houdini Nodes / VEX / Settings
- `VDB From Polygons` + `Points From Volume` — standard pipeline for filling a mesh's interior with scatter points
- Vellum Grains (shelf tool) — builds the PBD grain solver network automatically
- Grain parameters — particle separation (density), pscale (render size), friction, restitution
- Deforming collider — an animated mesh used directly as a Vellum collision object so grains respond to motion

### Difficulty
Intermediate

### Houdini Version
Houdini 18.5 (Renascence 1.0 — Module I)

---

## Related Tutorials
- [Importing the Geometry](module-i-week-05-01-importing-the-geometry-v1-1080p.md) — the preceding week's FLIP/Alembic workflow
- [Module II Introduction to Vellum](module-ii-week-01-02-introduction-to-vellum-v1-1080p.md) — broader Vellum fundamentals including grains
- [Tabletop Week 01 Intro](w01-01-introduction-v1-1080p.md) — another RBD/particle instancing-driven effect for comparison
