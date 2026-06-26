---
title: module i   week 01   09   setting the active attribute v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=VXkmQAGzBbA
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, destruction, active-attribute, rbd-configure, attribute-transfer, speed-limit, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-01-09-setting-the-active-attribute-v1-1080p/
frame_count: 4
---

# module i   week 01   09   setting the active attribute v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=VXkmQAGzBbA)
**Author:** The VFX School Archive
**Duration:** 10m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Alright, let's continue. So I'm going to drop another new note, ABD configure, which is here. So another new part of this pipeline. So I haven't explained about every note that kind of looks like this with this pink imports and the two, you know, multiple imports and outputs is part of the new kind of ABD workflow. The vellum workflow kind of looks similar, but you know, these will all be called IBD, something or other. And they all have, you know, the main geometry line, a constraint line, you know, this doesn't have to be this way. It's just neater because, you know, whenever you're building, the idea was, you know, whenever a typical IBD workflow would have all of these kind of lines anyway and they would be separate and, you know, you'd have one here, one there and they'd be sharing things back and forward. So it's easier just to keep them all together in this one kind of, one stack, I suppose you'd call it. Okay. So we got, yeah, we've got the main geometry, the constraints and the proxy geometry that we built. And if you're not sure, you know, sometimes they are four or three, you can just hover over the top. There we go, proxy here, we've got a static bound geometry. Okay. So this IBD configure will do a few things. It will set the attributes that we need for the simulation. So we could take a look at them if we go into our geometry spreadsheet. Let's see, on the points right now, we don't have anything, but it has packed everything we've already got a name. So, yeah, if we go back here actually and kind of just go into selection mode, you'll see that, you know, these are packed now. And we've got less points. We did before, we got 12,000, whereas before we had two million, right? So, yeah, this is going to pack everything, but we can also use it to set up any attributes that we like. For example, I'm going to use it to set up this, we've got these kind of physical attributes that we can set up, and we can use this concrete one. We've got these defaults, and I'm going to just set this to concrete and yeah, dry and clean services is fine. Okay, so that should, let's have a look. Maybe actually if we select the proxy geometry, I think it will have, yeah, we've got a density a bounce on that now as well. Okay, and then on this geometry, yeah, we don't have those, because these are not going to be simulated. Remember, this geometry is for like rendering to be seen, and then this is what will actually be simulated the proxy geometry. Okay, so, we've got all those sets up. I also want to turn on the active attributes. Okay, so if you look now, they'll all have a attribute, a value of one for active. So, active is, as it sounds, whenever we, the active value is one, bullets will simulate it, it will be able to be affected by forces, basically, we'll fall with gravity, if it's hit by another bullet object, we'll move. If the value is zero, it still collides with other objects, and you can still be constrained to it, but it won't move. Okay, so the reason I'm doing that is that I want to set up a perimeter around the edge of non-active pieces, right? So, that's when we actually simulate this, we'll have, you know, an explosion in the middle, and we don't just have every, the whole road just kind of dropping, or doing, you know, I think it will look weird, so this will have a nice kind of jagged edge around the edge. So, we need to come back right up to the top here, to this geometry, so I'm going to use the edge of the geometry that we made up here. Okay, so I'm going to grab that, maybe I'll just make a null, do it's under here, and call this out, floor pre-fracture, maybe like that. Okay, and then I'll just object merge it in here, so I just don't have a long line coming down. So object merge, drop that here, and then just go and find out, floor pre-fracture. And so after here what I'm going to do is use an actually transfer, to transfer that, that actually be a 12. First we need to, I'm going to make a selection of all the outside. So what I can do is just delete the top, the easiest way I figured of doing that is deleting the top and bottom, so we can delete by normal basically. So if I look for normals facing upwards, okay, and then just do that, and then do the opposite, do another delete, and then change this to minus one, push this up, let's see, it's getting rid of too many, we delete them here. I need to, let's see, there we go, drop that down, and do the same here, there we go, okay, so I just wanted to grab those edge pieces there, and then grab an attribute transfer, which is here, okay, transfer from this, and we also need to generate that, we need that attribute on, on this, so let's call this, it's an integer, i as active is zero, okay, which means you will be off, come here, it's a bit hard to visualize this, so if we just do a delete, here, and let's make sure that we are grabbing that active, okay, and then delete by expression, that's active is zero, which we're kind of points, let's see, you bring this down, there we go, so there you can see where this is what will be active, that seems like it's the wrong way of round, yeah, I'm not sure why exactly, it's doing something weird here, so there should be deleting any points which has an active value of zero, but in fact it's deleting anyone which has a one, it's kind of weird, maybe it doesn't need to, yeah, there we go, okay, so yeah, for the expression you need to, you need to, equals max, so it's like an if statement, okay, so, and if we do, deletes, non-selected, and then I've got this with a disinterreshold of one, a blend width of zero, you can see these, all these parts now won't move, they will collide with our, the other parts, but they won't be affected by any of the forces, right, so just one more thing I want to set up in this Abidi configure is the, if we come to speed limit, I want a speed max and a spin max, okay, because we've got such different pieces, maybe in real life you would have, the smaller pieces would fly off like bullets, but I want to kind of rain that in a bit with our simulation, so I'm going to set speed limit to 20 and a spin of 20 as well, just to kind of calm everything down, just a little bit, to control it, and then so that, you know, because we might have lots of little pieces that get stuck at that max, I'm going to randomize that value a little bit with a, attribute, randomize, just drop that at the end of the need, so the name, we can find that attributes now, that should be generated for us on the points, let's see, it goes to the speed max, so if I, I can change that now, I could have just made it here in this attribute, randomize, but either way, so if I just turn that on a default, now you can see we are setting it to a value between 0 and 1, but I want to actually multiply what we've already got, okay, so now we're going to have values between 20 and 0, okay, so, but I obviously don't want yet it to be 0, I'm going to bring this up to 0.8, so it's going to be multiply 20, 0.8 and 1.2, something like that, and we only need one dimension, it's just a, a float value, okay, so there we get a bit of a different value for that speed max, so that we don't get like a wall of, of, of pieces moving at the same speed, basically, so with that we're pretty much ready to simulate, we just need to build the bombs, actually the system for, for the, the velocity and, you know, the actual simulation itself.

**Frame:** tutorials\frames\module-i-week-01-09-setting-the-active-attribute-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
RBD simulation setup: using RBD Configure to set physical material properties and the `active` attribute, then transferring `active=0` to border pieces using edge geometry + Attribute Transfer to create a static perimeter around the fractured area. Speed limit + randomized `speedmax` attribute to control RBD chaos.

### Summary
10m22s lesson (VFX School Module I, Week 1, lesson 9). Covers the full RBD Configure node setup for an explosion simulation: packing geometry, applying concrete material presets, activating the `active` attribute (1=simulates, 0=collides but doesn't move), creating a border ring of inactive pieces by attribute-transferring from edge geometry (delete by normal to isolate sides), and adding randomized speed/spin limits via Attribute Randomize.

### Key Steps

**1. RBD Configure Node**
- Multi-input node (main geometry, constraints, proxy geometry) — part of the new RBD workflow
- Hover over inputs to see labels: geometry, constraints, proxy, static bound geometry
- Sets simulation attributes: packs geometry (12K points instead of 2M), assigns physical material
- Physical presets available: concrete (dry + clean surfaces default) → sets density, bounce on proxy geo

**2. Active Attribute**
- Enable "active" in RBD Configure → all pieces get `active=1` (simulates, moves with forces)
- `active=0`: piece still collides with other objects and can be constrained to, but won't move
- Goal: inner area active (explodes), outer border inactive (stays put = natural jagged edge)

**3. Creating Border of Inactive Pieces**
- Object Merge the original pre-fracture floor geometry
- Delete by Normal (facing up, value 1): removes top faces → keep side faces only
- Delete by Normal (value -1, push down): removes bottom faces → left with just edge ring geometry
- Attribute Create: `i@active = 0` (integer, value 0) on this edge geometry
- Attribute Transfer: transfer `active` attribute from edge ring onto fractured packed pieces (distance threshold 1, blend width 0)
- Visualize: Delete by expression `@active==0` to confirm which pieces are inactive

**4. Speed/Spin Limits + Randomization**
- In RBD Configure → Speed Limit tab: set `speedmax=20`, `spinmax=20` to prevent tiny pieces flying unrealistically fast
- Attribute Randomize (at end of network) → find `speedmax` attribute → mode: multiply, range 0.8–1.2, dimension 1 (float)
- Result: each piece has slightly different max speed (16–24) → avoids wall-of-same-speed movement

### Houdini Nodes / VEX / Settings
- **RBD Configure** — packs geo, sets physical material (concrete preset = density/bounce), enables active attribute, speed/spin limits; multi-input (geo/constraints/proxy)
- **`active` attribute** (integer, per point/piece) — 1=simulates, 0=static collider
- **Delete SOP by Normal** — isolate edge ring geometry by removing top/bottom-facing polygons
- **Attribute Create** — `i@active = 0` to mark border pieces as inactive
- **Attribute Transfer** — copies `active` attribute from edge ring to matching packed pieces by proximity; distance threshold + blend width
- **Attribute Randomize** — multiply mode on `speedmax` (range 0.8–1.2) for varied speed limits

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[rbd, destruction, active-attribute, rbd-configure, attribute-transfer, speed-limit, intermediate]

---

## Related Tutorials
- module-i-week-01-01-intro-v1-1080p.md (course intro / project overview)
- module-i-week-01-01-your-first-houdini-project-v1-1080p.md (Week 1 basics)
