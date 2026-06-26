---
title: module ii   week 01   04   tetrahedral soft bodies v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=pxWRHQjHpNk
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [vellum, tetrahedral, soft-body, solid-conform, remesh, vellum-source, collisions, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p/
frame_count: 4
---

# module ii   week 01   04   tetrahedral soft bodies v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=pxWRHQjHpNk)
**Author:** The VFX School Archive
**Duration:** 8m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So, let's just drop a position node for the hunter as well. I just want to move him forward just a tiny bit. 5, so that when the cracked ours mouth is actually shut. Ease in the mouth. That's where he gets caught. So let's set up our sim really quick. So, for this part, we'll just use the shelf tools. So, for our hunter for the body, we're not going to be, obviously, we'll simulate the cloth and everything separately. For the body, we're going to be using these new tetrahedral constraints. So, I'm going to click on that, click on the hunter, press enter with my cursor in the viewport here. You can see that it builds up our vellum solver for us. Let's go back out and see what we've got. So, the hunter, let's see, it's on the messed up. All this pint of farm stuff, let's get rid of that, because we'll build that later. So, we've got a poly-reduce. So, obviously, there we can see a problem straight away. We're not going to be able to do anything reduced too much. Let's do a percentage and let's, I don't know, could drop to 50% whatever you want. Okay, just to simplify the geometry, but in fact, to be honest, we don't really need it. We've got a remesh. Okay, so, just like we used on the cloth earlier, let's try and make these a bit smaller. So, for the moment, we'll do that, something like that. Okay, and then we've got a solid conform. So, at the moment, this is still a hollow geometry. A solid conform will convert this into tetrahedral shapes. So, this is not happy. Let's see why. So, we've got intersections. So, that's probably because we've got all these different overlapping geometries. So, let's just, let's just delete what we're not going to be simulating with this. Okay, so, we've got these groups here. So, I want to simulate the body and the shoes, believe it or not. So, let's delete, non-selected, isolate them, remesh them. See, an hour solid conform is happy. That works. Okay, and then we've got our constraints here. Okay, which are a little different, right? So, you can see that they look like polygons now, actually. So, they are basically trying to hold the volume and the whole shape. Of each of these, if I drop a clip in the tier, maybe that can, can see that a bit better. Raise this up. Okay, just a kind of chopper I would go in half. You can see, these are still quite big, but each of these shapes is like a kind of diamond shape. And these constraints are trying to hold that diamond shape the same configuration as it is. And then that will give us a kind of similar to an FEM simulation. Right? Let's make these bits smallest still here. Let's do this bit. 0.5. Smaller. We might probably play with that again a bit more in the future. So, as of today, we've got our geometry and our constraints. Okay, and then on the constraints, we've got all these different attributes, which come from in here. Okay, we don't need to worry about most of these, these rest matrices, vectors. The bottom one's probably stiffness, you'll worry about more. And the type is important, but with this one, you'll just have the one. Maybe velocities as well if you wanted to add velocities to the beginning. And then in the geometry here, we don't have much more on the point. So again, we've got the mass, which will be varying depending on the size of each text. The p-scale, which will be the thickness, okay, which we can, I think, visualize. We can with some, we have visualized thickness, you can see that, as long as they're not overlapping, that's fine. Turn that off. Okay, and you can see that just like the cloth, the mass is being calculated. Okay, that basically helps out when I add more subdivision to this, then the mass should stay relatively similar. The same with the thickness, okay. And then we've got a stiffness for our, of our tetrahedrals. So let's take a look at our solver, what we've got in there. So we've got our vellum object. And this is trying to pull in the geometry and the constraints from the first and second inputs, which it doesn't have. Okay, so you can either source your geometry in here. If you're working with a top network in the, in the shop context. Or if you're doing out here, then you can use a vellum source and just grab it directly like this, okay, which works fine. Let's just drop a ground plane so you can see if we actually get something that works here. Okay, I'll hide our crocodile for the moment. And let's see, should get this smudgy, this smudgy kind of human. There we go, great. And we could, let's bring in the crocodile as a collider. So let's go to collisions, static object. And let's generate my crocodile. Let's just take a look at him. There's the surface geometry and the VDB here. Let's just put a bit of course. So let's bring that down. Oh, five, two, a bit more. Oh, one. And then as I said, so the crocodile is going to be biting at. I'm going to start at about frame 40. So I'm just going to come out here, start frame. On 40, so we won't see anything at the beginning until. Let's press L on my keyboard to tidy this up. Got the crocodile coming in here. Let's just see if this works. We'll skip all the way up to frame 39. Just start. Let's see what happens. Ah, crocodile's not moving. Always forget to do this. Use the forming geometry. And there we go. Well, it's not beautiful. It's kind of weird, but you know, it's something. We got something. So yeah, with, with Valum, pretty much always I'll be pushing up the substats, you know, pretty dramatically. And you know, with low substats, you're always going to get kind of stretching and weirdness with grains as well. Okay. So you can see that it's still stretching with five. So I'll have to do some work to kind of solve that problem. Okay.

**Frame:** tutorials\frames\module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Tetrahedral soft body in Vellum: Remesh + Solid Conform converts a character surface mesh into a tetrahedral volume mesh; Vellum Configure Tet Soft Body generates diamond-shaped constraint primitives that hold the volume (like FEM); use Vellum Source to feed external geometry into an existing Vellum Solver.

### Summary
8m50s lesson (Module II Week 1, lesson 4). Sets up soft body simulation for a human hunter character in a crocodile attack scene. Covers: Poly Reduce + Remesh for cleaner input, Solid Conform to convert hollow polygon mesh into tet volume, Vellum Configure Tet Soft Body for FEM-like volume-preserving soft body, Vellum Source node for external geometry input, and using "Use Deforming Geometry" for animated crocodile collider.

### Key Steps

**1. Geometry Prep (Critical for Solid Conform)**
- Must use only watertight, non-intersecting closed geometry
- Delete groups you're NOT simulating (body + shoes only; remove clothes, accessories)
- Poly Reduce → % mode (e.g., 50%) or skip if Remesh is sufficient
- Remesh: get uniform triangles; try small target length (e.g., 0.5–0.1) for dense enough tet mesh
- Solid Conform: requires clean, non-intersecting closed surface → converts to tetrahedral volume
  - Error "intersections detected" → overlapping geometry in input; delete until only isolated watertight meshes remain

**2. Solid Conform → Tet Soft Body**
- Solid Conform: creates interior tetrahedral mesh from closed polygon surface
- Constraint geometry looks like diamond shapes (each tet = 4 triangular constraint primitives)
- Constraint attributes: `rest_matrices`, `stiffness`, `type`; mass varies by tet size
- Vellum Configure Tet Soft Body (or auto-set by shelf tool): assigns constraint type for tet constraints
- `pscale` = thickness for collision; `mass` = varies by volume of each tet

**3. Vellum Source (External Geometry)**
- When Vellum Solver already exists in DOP network (or SOP solver), feed additional geometry with Vellum Source
- Vellum Source: connects geometry + constraints to an existing Vellum Solver without rebuilding
- Alternative: merge geometry directly if building from scratch

**4. Crocodile Animated Collider**
- Static Object (Vellum collider) → paste path to crocodile VDB or surface
- CRITICAL: enable "Use Deforming Geometry" checkbox on Static Object → without it, collider stays at rest pose (frame 1) and doesn't animate
- Start frame parameter: set to the frame the croc starts interacting (e.g., frame 40) to skip pre-contact frames

**5. Substeps for Soft Bodies**
- Tet soft bodies need at least 5+ substeps to avoid stretching
- Low substeps → unrealistic stretching through collider
- Tradeoff: more substeps = better quality but slower

### Houdini Nodes / VEX / Settings
- **Poly Reduce** — simplify high-poly mesh; use % mode
- **Remesh** — uniform triangulation; target edge length controls density
- **Solid Conform** — converts closed polygon surface → tetrahedral interior mesh; requires watertight non-intersecting input
- **Vellum Configure Tet Soft Body** — assigns tet constraint type; generated by shelf tool "tetrahedral constraints"
- **Vellum Source** — feed geometry into existing Vellum Solver/DOP network
- **Static Object** (Vellum collider) — "Use Deforming Geometry" = required for animated colliders
- Constraint geometry attributes: `rest_matrices`, `stiffness`, `type` (tet), `velocity`
- Geometry attributes: `mass` (varies by tet volume), `pscale` (collision thickness)

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[vellum, tetrahedral, soft-body, solid-conform, remesh, vellum-source, collisions, intermediate]

---

## Related Tutorials
- module-ii-week-01-02-introduction-to-vellum-v1-1080p.md (Vellum overview: cloth/string/struts)
- module-ii-week-01-06-updating-the-rest-blend-v1-1080p.md (rest blend for soft body)
