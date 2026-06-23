---
title: 53 recreating our solver with pops v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9objvx69_58
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/53-recreating-our-solver-with-pops-v1-1080p/
frame_count: 4
---

# 53 recreating our solver with pops v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9objvx69_58)
**Author:** The VFX School Archive
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** And what we can do is we can create a pop network. And the first thing is that we don't really need to scatter points. We can just feed the surface directly to the first input of the pop network. And that's going to work. In terms of creating the attributes, we also don't need to worry too much about any of these. Let's just go directly to the pop solver. Now, we were generating 100 particles on each frame. So here, when you go inside a pop network, we'll have to take that into consideration. So this is the pop solver. This is where all the calculations will happen. This is the pop object, which is where the information is going to be stored. This is basically just a container that will save all the information that we need. It's through this node that we'll be able to access what's happening. And this is these are the operators that are going to be feeding new information into the solver. To make for things to change through time. The first operator that we have here is a pop source. And the pop source by default is going to work by using as a source. The geometry source is going to be first context geometry. And the emission type is going to be scattered onto surfaces. Now, on the next tab, you'll have a birth. And right now, we have a constant activation of 5,000 per second. We don't want 5,000 per second. We want something similar to what we had. You'll see that we also have a representation of the surface that's generating the particles. And in this case, it's a surface. Let's just disable that. And we want to match the same rate that we had. We were launching 100 particles on each frame. So per second, we were generating 2400 particles. So that's what we're going to be using here. So we'll get the same density. Next, on the attributes, we have a place where we can specify the velocities. So, inherit velocity. Let's say set initial velocity. I'm going to say that there's no variance. And the velocity is 010. And let's say that here on the birth, we also have the life expectancy. Let's say it's 3. And if we play, you'll see that this is exactly what we had before. Exactly the same thing. We can even compare both of them. Let me just make an offset here with the transform. And we can, I'm just going to template these and have a look at those. So before we added randomness, we had something pretty similar. Okay. Now, we added some randomness between 0.5 and 1.5. And here we can also control that with a variance of 0.5, meaning we'll have the same kind of variation. And we'll go up, hit play. And again, we have very similar results, very similar looks. Now, the type of parameters that we have are pretty similar as well. The attributes that are present on one or the other. But we will have a lot more information being stored and taken into account on the pop network. So if we have a look at the geometry spreadsheet of the sub-sauver that we created, we'll see we have position, age, life and velocity. And here on the pop network, we'll have to find our pop object, look for geometry. And here you'll see we have position, age, dad has previous, a bunch of them. ID, life, position, previous, source, UV, a lot more information going on. And that's one of the reasons why this is going to be a lot more powerful and a lot easier to adjust and configure to get some nice interesting motions. We could also do always do the same thing, achieve a very similar result with the solver, with the sub-sauver, but it's a lot more work than just using the pop network. I hope this helped understand that inside the pop network, the essential principles aren't that hard to understand. They're pretty basic operations, but of course there's a lot more to it under the hood, but in terms of optimization, of the calculations, etc. But the essential of what's happening shouldn't be that hard to understand. On the next lessons, we'll continue to explore and develop the knowledge of the pop network.

**Frame:** tutorials\frames\53-recreating-our-solver-with-pops-v1-1080p\frame_000.jpg


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
