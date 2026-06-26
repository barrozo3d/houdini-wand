---
title: w02   05   deforming with velocity v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=IuvtudgbzLw
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [velocity, attribute-transfer, deformation, trail, vex, wrangle, beginner]
extraction_status: complete
frames_dir: tutorials/frames/w02-05-deforming-with-velocity-v1-1080p/
frame_count: 4
---

# w02   05   deforming with velocity v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=IuvtudgbzLw)
**Author:** The VFX School Archive
**Duration:** 7m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** As I believe I mentioned earlier, we're going to be using velocity as one of our attributes for displacing this geometry. And at the moment, if we take a look, well, we'll come right to the file node, select that, and then go to geometry spreadsheet, we can see what we've got. The attributes we currently have on the points just position, a normal and DVs, and primitive, we just got a couple of groups for the two different blueberries and nothing in detail. So we don't have our velocity attributes yet, so we need to go ahead and make that. So if we take a trail, stop, so by default, if we, I don't know if you'll see much here, let's just drag the length, we'll kind of, yeah, you can see, it's kind of copying the geometry there, making like a, almost like a tail in the geometry, and we turn this off. But we don't want that, okay, I'm going to put this back to default and change this to compute velocity. So this is handy also for your motion blur, if you're working with geometry with animation, and if you don't have a velocity on it and you want to render motion blur, this is quite a common thing that I do and others to get that. And I'm going to turn this up, I'm going to double the velocity scales, just a multiplier, okay, give us more to work with. So if we head up to the geometry spreadsheet now, you could see we've got a velocity in our geometry, we've got some numbers, things for us to work with, okay, on the points. Cool, so let's come back to this attribute transfer. I'm going to take the black here and actually put it onto the grid, okay, we don't have color here now, so there's an error, transferring a something which isn't there, so let's give it that. So I'm going to drop down a attribute, there it is, okay, we used one of these in the first week, so we're going to drop in here and again, we've taken the attributes, so we've got velocity, the velocity attribute and we're going to trans make color from that, okay, if we visualize that now, you can see we've got some weird results, so what I'm going to do is drop a, what is it called vector, to float, so this has one input which is a vector, so we have a vector in x, y and z, and then we can take this while I was to separate those components, so we've got x, y and z, I'm going to take the y component and connect it to the color there, and there you go, already we can see something better, we've got some cleaner values, we don't have vector colors being transferred, okay, so at the moment it's only affecting the color, we can't see any deformation of the yoghurt, so let's drop a attribute, wrangle, and then here we can use the color information to deform the geometry, okay, we're going to drop down a little bit of x, not a lot, nothing too complicated, so we need to access the position attribute in y, okay, we're only going to move our geometry up this way, turn that off, and what we're going to do is we're going to take, oops, so we're going to take the position that we've got, y again, we're going to add the color, so we're changing the color, right, see the, I'm going to put dot x because we don't want the, we only want one part of the color, we'll be the same of the every, because it's gray, if I come here, I'll highlight this and show you, we've got find place where we've got values, yeah, you can see they're the same, x, y, and z, but so we don't want all three, I just want one, just want this one number, it doesn't matter, I can take it from x, from y or z, r, g, or b, sorry, so I'm just going to take it from r, x, I could put r also, in fact, it'll still work, oops, okay, let's go back to our scene views, so we can see this once is happening, in fact if I just drop a, oops, a semicolon there, I think we should get something, yeah, you see that, we got a little, we got a bit of a dip then, see that, so it's already something going on, we would be good to have a bit more control on this, so I'm going to multiply this and we're going to create our own multipliers, so I could just put, I can multiply by two, three, okay, but what we would be nice to do is to make a slider down here, so we can have something to click and drag along and be, we'll have a bit more artistic control, right, so to make a, a channel like that, we use ch, and it will default to a float, but if you want a vector, you put use chanavie, or chanav f for floats, yeah, we don't need to do that because default is a float, which is what we need, and then we give it a name, we call it, molt, close the brackets there, I'm going to put all of this inside one bracket, so we have a correct order of, you know, the math works correctly, so that's gone to zero now, so we have no, so this is multiplied by zero, so we're not getting anything, so if we click this button, that makes our slider, so we have the name there, molt, and it's at zero, so now if I drag this up, we should see, it's a bit hard to see the, you can't see it's dropping down, go from zero to one, but if I middle click, we can go higher or lower, with that, I'm going to change the, this to, let's drag the line, get something a bit smoother, okay, great,

**Frame:** tutorials\frames\w02-05-deforming-with-velocity-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Use Trail SOP (Compute Velocity mode) to generate `v` attribute on animated geometry → Attribute Transfer velocity Y component to grid as color → Attribute Wrangle deforms grid Y position by color with a ch() slider: `@P.y += @Cd.r * ch("mult");`

### Summary
7m30s VFX School Archive module lesson. Part of a blueberry/yogurt tutorial series. Shows how to derive velocity from animated geometry using the Trail SOP, transfer that velocity to a deformable grid as color (via Attribute Transfer + Vector to Float), then use an Attribute Wrangle to displace grid points along Y proportional to the velocity-derived color. Creates a ch() parameter slider for real-time artistic control.

### Key Steps
1. **Trail SOP** — set mode to **Compute Velocity** → adds `v` (velocity) vector attribute to geometry; velocity scale = 2 for more pronounced values; also useful for motion blur on animated meshes without intrinsic velocity
2. **Attribute Transfer** — source: animated geo (velocity attribute); target: static grid → transfers `v` to grid points
3. **Vector to Float** — split `v` vector into X, Y, Z components; grab Y component
4. **Color (Cd)** — plug Y velocity into Cd channel for viewport visualization and downstream use
5. **Attribute Wrangle** — deform grid:
   ```vex
   @P.y += @Cd.r * ch("mult");
   ```
   - `@Cd.r` = same float on all channels (greyscale from Y velocity); `.r`/`.x` either works
   - `ch("mult")` creates slider parameter; click gear button → creates slider → middle-click drag for values above 1

### Houdini Nodes / VEX / Settings
- **Trail SOP**: mode=Compute Velocity; velocity scale=2 → adds `v` attribute
- **Attribute Transfer**: from animated geo → grid; select velocity attribute
- **Vector to Float** (VOP): split vector into X/Y/Z float components
- **Attribute Wrangle**: `@P.y += @Cd.r * ch("mult");`
- `ch("name")` → creates float channel/slider parameter on the node

### Difficulty
Beginner

### Houdini Version
H18+

### Tags
[velocity, attribute-transfer, deformation, trail, vex, wrangle, beginner]

---

## Related Tutorials
- w03-04-adding-viscosity-v1-1080p.md (same VFX School course, FLIP viscosity)
- velocity-forces-20-advanced.md (advanced velocity field techniques)
- tutorial-heavy-chic-part-1.md (Attribute Bind VOP technique for height field → density)
