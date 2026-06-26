---
title: module i   week 06   01   introduction to grains v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=XPDsqVutqDw
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [grains, vellum, vellum-configure-grain, points-from-volume, substeps, attraction, beginner-intermediate]
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
**Transcript:** Okay, so we're starting with grains, not starting, we're finishing with grains I suppose. So we're going to create a new project. The name will be module, whatever you like, but this is module one, week six, into the okay, accept and then save the hip. Very important, good job and then let's call it a module one week six dot grains dot because you're one. Hip, great, okay, so now we need to find that project and bring in our files, our FBX. So here's the project, just drag it in and then I've got the FBX here so go, I'll leave that in, do we have an FBX folder? We don't. Just leave it in geo, drag that zombie death in there, okay, and then we can go to file import, thumb box FBX and then go ahead and find out. So I saved it into geo zombie death, accept import. There we have it, spacebar F and we can see our lovely zombie, okay. So first of all, he's too big, so I'm going to press P here and point to one spacebar F and then we can see, you know, roughly a bit under two meters, which is about right. And then I'm going to create a geometry node and call this grain. We're going to object merge in just a geometry, we don't need the rig or anything like that. So go ahead in here and find this zombie geo control C on that and then grain, grab an object merge and you can just paste that in there and we should see him now into this object, there we go. So that will take accounts of the transform there, okay. So there we go, we've got our zombie and he kind of falls over, you can see the animation is just about, you know, 70 or so frames. So we'll change our timeline to reflect that. Just to find the end, you know, he's still moving for 70 frames. So I don't feel simm it that long, but we'll take a look at that. So yeah, grains, like take a make a really quick simulation, just to, you know, start out with quick understanding of grain. So first of all, you can get rid of the animation, drop a time shift, right click delete channels and then that will just freeze it onto the first frame there, okay. And then so for vellum grains, we need to use the vellum grain, which I can't see. Oops, don't want that. Let's just tab grain vellum can figure grain there we go. And then just plug that in and by default it's not doing anything. So we just need to check this create points from volume. So that will create a volume and fill it with points. It doesn't look great. Let's drop the grain size, point of one. So you can see here we have problems because of the geometry is it's not watertight, right? How's Hall's better, that's the, you know, the design, but things like, like this, you can see there, we've got two separate pieces, this hand is a separate piece of the sleeve and there's a hole there's not watertight, right? So easy way to fix that is drop a poly fill there, okay. And you can see we get an error message. So if we just change it to single polygon, we will get endgons, but it doesn't matter because you know, we're not going to be rendering this geometry or doing anything, we're doing anything with this. So, you know, we'll get that will fill the, it will put a cap on those holes and hopefully that will give us grains like that. Okay. So you can see all this, you know, this is not really doing much here. It's just, it's the same as a points from volume, I think. So you could do that as well. You know, it's the same thing. It looks different because here, where we're dropping this sprite material onto each point. So it looks like, you know, they're being lit, but it's just a, it's like an image of a sphere and being copied onto each. Each point you can tell, you know, that the lighting is the same on all of them. So, you know, it's just for, you don't really need it. You can, well, they go, you can turn it off there and they will be pretty much the same. So yeah, we're getting this grain size, which is the diameter, I think we go into the geometry spreadsheet. You can see. Oh, sorry, the p scale is the radius and then the grain size would be the diameter, you know, all the way across. So a p scale will be half of that mass is just said the same on all of them. It doesn't really matter unless you have different amounts of mass. And then we could just get this thing is grain. So that's just an attribute for the solvus or the solvent knows that is to deal with these points as if they're grain because, you know, it will go into a valum solver, which, you know, could be cloth or something else. And that's it, you know, so you could, you don't really have to use this node. It could be that your input, your starting out with points from some source, I don't know. And then you could plug it into this actually or you could just set these attributes up yourself. You don't have to use this node. So and then we can obviously use the valum solver, just quick and simple, plug them in like that. We don't need that. Oh, that's, oh, it requires the constraint geometry. It doesn't really because we don't have any constraints set up here. We could, but we don't need to let's turn on the spread material just for fun and turn on the ground position, turn on real time and press play. We'll see. We get. That's so you might wonder why what's the difference between this and a particle simulation. The main difference is you can see that the grains they don't, well, they shouldn't occupy the same space. So, you know, they know that they hold a piece scale and a size diameter and they shouldn't overlap. Or kind of interpenetrates each other. Okay. So that means they can pile up like this and they can also look at each other so they can stick to each other as well. Thing is, we don't have the options for that. We still don't know on the valum solver here we could just quickly just to show you it's not too important. This is just a demonstration. You can right click, go to allow editing of content. You can see that padlock's unlocked. Now I can go inside and see how they've built this, this HDA, go into the top net, go into the valum solver, go into advanced and then grain collisions. There we go, we've got the, what we, the importance parameters for grains there. And so these are kind of interesting attraction weights and repulsions. So they tell the grains to try to stick together or try to push apart, which is pretty cool. As tenders to one and then hopefully we'll see some clumping there. You can see it's kind of working. One thing, the thing is with grains is that you generally have to start out with at least, I think in the documents it says at least five or four sub-steps before you get anything kind of usable. So straight away there, you know, we're getting something starting to get these nice kind of clusters, clumps holding together. The problem is with grains you're often fighting against this kind of thing where you basically exploding, you know, they're bouncing all over the place. And the answer to that unfortunately is just sub-steps. So you can see it will run much slower, but we should get something much more stable. So, you know, that kind of effect there's not really, don't go looking for, you know, bounce and stuff like that. It's because it needs more sub-steps. So we still got one or two bouncing, which is okay. It's not a big problem, but the majority is sticking together and we get this nice kind of splat, okay, which is kind of cool. Okay, so that's your, you know, basic grain setup, but you know, obviously we're going to be doing something a bit more advanced than that.

**Frame:** tutorials\frames\module-i-week-06-01-introduction-to-grains-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Vellum grains introduction: Vellum Configure Grain fills geometry volume with points (pscale = radius, grain_size = diameter), feeds into Vellum Solver. Key distinction from particles: grains enforce non-interpenetration (stack/pile) and support attraction (clumping). Requires minimum 4–5 substeps for stability; adjust attraction_weight for clumping vs repulsion.

### Summary
9m56s intro lesson (VFX School Module I Week 6: zombie grains). Imports FBX zombie, creates grain setup from volume. Covers: Vellum Configure Grain (create points from volume, pscale/grain_size attributes, `grain` attribute for solver identification), Poly Fill for non-watertight geometry, Vellum Solver (no constraints required for basic grains), grain vs particle difference (interpenetration prevention → pileup), substep requirement (≥4–5 for stability), attraction/repulsion parameters inside solver HDA.

### Key Steps

**1. Import + Setup**
- FBX import: File → Import → FBX; press P → scale to 0.1 for human-scale
- Object Merge into a new geometry node (avoids long wires)
- Time Shift → right click → delete channels → freeze at frame 1 (no animation needed)

**2. Vellum Configure Grain**
- Enable "create points from volume" → fills mesh interior with grain points
- Grain size: diameter of each grain (e.g. 0.1); pscale = radius (half grain size)
- Creates attributes: `pscale` (radius), `grain_size` (diameter), `mass`, `grain` (flag attribute for solver)
- `grain` attribute = tells Vellum Solver to treat these as grains (not cloth or other constraint type)
- Non-watertight geometry fix: add Poly Fill (single polygon / endgons mode) before Configure Grain

**3. Sprite Display**
- Vellum Configure Grain applies a sprite material per point → each looks like a lit sphere but it's just a billboard image
- Not the actual grain render; turn off if confusing

**4. Vellum Solver**
- Plug Configure Grain output into Vellum Solver geometry input; constraints input can be empty (no constraints)
- Enable ground position → collide with floor
- Grain difference from particles: grains know their pscale and enforce non-overlap → they pile up instead of passing through each other

**5. Substeps (Critical)**
- Grains require minimum 4–5 substeps for stability (explode/bounce without enough substeps)
- More substeps = slower but more stable; most grain instability is solved by increasing substeps

**6. Attraction/Repulsion (Clumping)**
- Inside Vellum Solver HDA: right-click → allow editing of content → enter
- Vellum Solver → Advanced → Grain Collisions: attraction weight, repulsion parameters
- `attraction_weight` close to 1 → grains stick together and clump
- Use for organic grain effects (sand clumping, etc.)

### Houdini Nodes / VEX / Settings
- **FBX Import** (File → Import → FBX) — import character for grain fill geometry
- **Poly Fill** — fills holes in non-watertight geometry; use "single polygon" (endgon) mode
- **Vellum Configure Grain** — "create points from volume" option; grain_size (diameter); pscale = radius; `grain` attribute
- **Vellum Solver** — grain simulation; substeps (min 4–5); ground position toggle; no constraints required
- `attraction_weight` (inside Vellum Solver advanced → grain collisions) — clumping strength
- `grain` attribute — flags points as grains for Vellum Solver type detection
- `pscale` — radius (half of grain_size diameter)

### Difficulty
Beginner–Intermediate

### Houdini Version
H18.5

### Tags
[grains, vellum, vellum-configure-grain, points-from-volume, substeps, attraction, beginner-intermediate]

---

## Related Tutorials
- module-i-week-05-01-importing-the-geometry-v1-1080p.md (Week 5 geometry import)
- module-ii-week-01-01-basic-bullet-sim-v1-1080p.md (Module II Week 1)
