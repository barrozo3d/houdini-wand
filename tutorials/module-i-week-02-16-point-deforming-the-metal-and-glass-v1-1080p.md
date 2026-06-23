---
title: module i   week 02   16   point deforming the metal and glass v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=oZh_MAnZyaQ
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p/
frame_count: 4
---

# module i   week 02   16   point deforming the metal and glass v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=oZh_MAnZyaQ)
**Author:** The VFX School Archive
**Duration:** 5m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So let's do the metal bending bit now. So we need this and we need this. I'm going to move this over here. This is the results of sim2 and I want the, we're going to be deforming that as well in this lesson now. So I'm going to put them over there. Now there's another new note called ABD, deform pieces, which is really handy because what we're doing here is bending as I said before, bending this with this and you have to do like a whole kind of four each loop where you're capturing the geometry and then bending it and another and going iterating over each separate piece in your geometry and it was kind of a pain and a bit complex. Now we've got this setup which helps a lot. So in here we have the geometry that you want to bend. When don't need to connect the constraints, it does say it's required but that's just because well, it depends if you're using constraints here but we're not going to do that so it does work without it. And this goes into the right hand side. What we do need to do here is we need, if you think about it, we need more geometry to be able to bend this. So an easy way to do that is just drop a divide. And then we're going to set this to turn that off and turn on this brick of polygons and just set them all to .05, .05 and that will just drop a load of geometry for us. So that's great and then we can go in here and visualize that. Okay, so it's doing something but obviously it's not there yet. So yeah, you need to kind of play around with these values, rest frame, yeah, just leave that at one. And then I found for me, so I'm pushing this up to .2 and then just grabbing a whole load of points to do it, seem to do almost what I needed. Okay, but then also we want to do, we want to match proxy by attribute. Okay, then we're going to use this section here. Oh, it doesn't need to go here in the cluster. There we go. Yeah. So this, I think that doesn't matter. Does it? It's just this cluster attribute. So if you remember, we set up the sections beforehand. So that's saying, for example, a separate piece like this bar. So this bar is only being bent by the pieces from the original simulation. So basically these pieces from this bar don't have any effect on this or this or anything else only on the section that they refer to is what that's doing. Okay, and it helps us tidy things up, you know, where pieces come close together, it can be problematic. Okay, so that gives us this really nice bending effect. What I also want to do is use, we can use this now to bend these pieces of glass. Also going to divide them. We'll just do the same because they might need to bend a little bit. You know, glass can bend. There's nothing wrong with that. So obviously to an extent. For this, I'm just going to use the pointer form, which is what's going on inside here. Okay, there'll just be a load of, if we go inside, we'll probably see, yeah, see pointer form there and load of other stuff going on. But that's basically the cracks of what we're doing is a pointer forming. So for this, we need the results of this going into here. So we're going to use this to deform the glass. We need a time shift for the rest frame. Okay, just set this to the first frame. Like that in there and then listen to the last port. Okay, and then let's see how that looks. Maybe we should know just so we can see. With the results from there, check that out. I can see what I'm doing there now. This needs to be here also. And let's see. You can see there now. So the glass is following that animation. Okay, I'm just leaving this out at default. It doesn't matter. But yeah, we might get a bit of bending in it. Yeah, you can see that's just flexing just a tiny bit, but not too much and it's not intersecting anywhere. So we're following that perfectly. So that's great. That looks really nice. So next we will do the split everything up here and do the glass that disconnected faces thing.

**Frame:** tutorials\frames\module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
