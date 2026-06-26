---
title: module ii   week 02   01   importing the geometry v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=tC3H8wBaytE
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [import, alembic, lod, path-attribute, exploded-view, rbd, beginner]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-02-01-importing-the-geometry-v1-1080p/
frame_count: 4
---

# module ii   week 02   01   importing the geometry v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=tC3H8wBaytE)
**Author:** The VFX School Archive
**Duration:** 4m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Alright, so let's get started. I'm going to create a new project and this will be module module 2 week 2. Okay, and this goes into my D drive. Alright, so just go ahead and find that and then drag in the Brooklyn building. So that's an Olympics, we'll drop it in here. I've already extracted this, it's a compressed file and then inside you've got these different LODs. All the same building, but different levels, you know, amounts of polygons inside. So I'm going to be using LOD 2, you can use, you know, to get the same results you would do the same, but you can play around with the others. So let's grab a geometry note and we'll call this building. Okay, let's press P to get our parameters. Great, and then dive inside press I, grab an Olympic. Okay, and I just remembered save the project, save the hip file. Okay, so what are we doing here? So reverse gravity. Yeah, kind of like a tractor beam thing. And then we'll go into hip, Olympic, version one, I'm going to use, like I said, LOD 2. So if you press spacebar and F, you can see that it's way too big. So as per usual, we need to make this smaller, just that old kind of Houdini scale thing, you know, meters and other things we can send to meters, I think. So point to one, normally get too close to what you want. So 10 meters there. Yeah, it's roughly right. So there's our model. We've got, let me unpack this. And just take a look at the, we'll grab that path attribute that can be useful. So if we take a look on the primitives, they will have like materials or see it's this really handy is telling you, door. In our case, we're not going to go into that much detail with that, but really, really useful for fracturing when we know what's wood, you know, what's a door, you know, where does this, what materials am I looking at here? What do you, what am I constraining you to stuff like that? In our case, we're going to be doing, you know, something really simple, but it's a good idea to see what information you have whenever you bring in your geometry and you're starting out. Also, if you press nine or any keyboard, go into 3D connectivity. So you can see the separate pieces. So things like the tiles, are they all separate floating pieces or are they, is this one piece of geometry, which is, you know, just extruded in a different way. So that's, that's nice when we fracture this, they'll all be separated. We don't have to look for a way of, I don't know how you would fracture all of them separately. If if it was one piece, maybe in a lower, I think you're actually, we go to LOD 1 there. Now you can see it's just all one piece, okay? It's just kind of fused together, which would be really difficult to get a nice fracture out of this. So we'll go back up to LOD 2, which, you know, still we've got loads of nice details here. Like I said, all the separate tiles, these wooden panels, the windows, everything. So that's great. Another thing you can do, well, I recommend doing is dropping the exploded view. Just plug that in and we'll create a name attribute internally. And you use that to identify pieces, okay. And then you can get it even better look of, you know, what you're starting off with. And it's a good idea to, when you shrink it down, see if you've got lots of pieces overlapping that can be problematic, just seeing there. So things like that, again, in our case, it's pretty simple simulation. It's not too big of a problem. Yeah, that's our building, you know, we'll be prepping this up. Not going to be doing too many complex fracturing operations to it. We'll end up with a core simulation at the end.

**Frame:** tutorials\frames\module-ii-week-02-01-importing-the-geometry-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Import and inspect a multi-LOD Alembic building asset: scale to Houdini units, Unpack to see the path attribute (material per primitive), use 3D connectivity display mode (key 9) to verify piece separation, and drop an Exploded View SOP to create a name attribute and visually inspect overlap before fracturing.

### Summary
4m48s lesson (Module II Week 2, lesson 1). Imports a Brooklyn building Alembic with multiple LODs. LOD 2 chosen: separate tiles, windows, wooden panels (all distinct pieces). LOD 1 is fused and unworkable for fracture. Workflow: Geometry node → Alembic SOP → scale to 0.01 → Unpack → inspect path attribute for material IDs → 3D connectivity display (key 9) to confirm piece separation → Exploded View SOP to name pieces and check overlapping. Project: reverse gravity/tractor beam RBD sim.

### Key Steps

**1. Import Alembic**
- File → New Project (module-ii-week-02)
- Geometry node → dive inside → Alembic SOP
- Navigate to extracted LOD folder; select LOD 2 file
- Scale = 0.01 (standard Houdini/Alembic size mismatch: model comes in at ~100m, need ~10m)

**2. Inspect LOD & Piece Structure**
- Compare LODs: LOD 1 = fused geometry (one piece = bad for fracture); LOD 2 = separate tiles/windows/panels (correct)
- Unpack SOP: necessary to access primitive-level attributes
- After Unpack: check primitives → path attribute shows material name per prim (e.g., "door", "wood", "glass") — essential for knowing what to constrain or fracture separately

**3. 3D Connectivity Display**
- Press 9 on keyboard in viewport → switches to 3D connectivity display mode
- Each separate connected piece gets a unique color → instantly see which geometry is truly separated vs fused
- Confirms tiles are all individual floating pieces (not extruded from one mesh)

**4. Exploded View SOP**
- Drop Exploded View SOP, plug in after Unpack
- Internally creates a name attribute for each piece (critical for RBD and constraints)
- Shrink down the exploded view to see overlapping pieces (problematic for sims)
- Inspect overlap issues early; in this case minimal for a simple sim

### Houdini Nodes / VEX / Settings
- **Alembic SOP** — import multi-LOD building; scale = 0.01 for correct Houdini units
- **Unpack SOP** — unlock packed Alembic geometry to expose primitive attributes
- `path` attribute (primitive) — material/object path per primitive; use to identify material regions for selective fracture or constraints
- **3D Connectivity display** — press 9 in viewport; each connected piece = unique color; confirms piece separation
- **Exploded View SOP** — creates `name` attribute per piece; separates pieces visually; shrink to check overlaps

### Difficulty
Beginner

### Houdini Version
H18.5

### Tags
[import, alembic, lod, path-attribute, exploded-view, rbd, beginner]

---

## Related Tutorials
- module-ii-week-02-01-introduction-v1-1080p.md (project overview: tractor beam/reverse gravity)
- module-i-week-02-01-creating-a-new-project-v1-1080p.md (project setup)
- module-i-week-01-09-setting-the-active-attribute-v1-1080p.md (RBD active attribute setup)
