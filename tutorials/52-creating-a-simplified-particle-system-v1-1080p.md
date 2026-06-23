---
title: 52 creating a simplified particle system v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=l65A4S4YhSw
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/52-creating-a-simplified-particle-system-v1-1080p/
frame_count: 4
---

# 52 creating a simplified particle system v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=l65A4S4YhSw)
**Author:** The VFX School Archive
**Duration:** 7m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now, another common thing is for the pop solver to be able to generate new particles on each frame. And the way we can do that is pretty straightforward. Let's go here to the scatter first. If you notice on the scatter we have this global seed. And as you change the global seed, the distribution of the particles on the surface changes. So we'll put here $F. And this means that on each frame we'll have a different distribution of particles. And here on the solver, we'll take that into account. What we're going to be doing is we're going to be merging these particles, whose position has been updated, and then we'll merge the new particles coming in from input one. Let's go up. To go to the solver, we should now see that we're emitting particles, a stream of particles, and they all have the same speed, the same velocity vector. If you go to the geometry spreadsheet, you'll see that the velocity is constant for all of them, but the position is being updated based on the velocity. What else can we do to kind of simulate the functioning of a pop solver? What we can do is, for instance, we could also update the age of the particles. One of the characteristics of pop solver is that each particle has a lifespan and an age. So the way we can do that is here where we created the velocity, we can create another attribute. I'm going to call this create attributes. And we'll create an attribute called, let me hit the plus button here, we'll create an attribute called age. It's a float, and the value is going to start at zero. Now if you go to the solver, here on the update position, we can also do an update position and age. And to update the age, we just need to add to the current age, the particles age, plus equals, which means age is going to be equal to age plus something. So it's another, we could write this line in the same way, so we could say plus equals, it's going to give us the same result. And age is going to be time, time plus equals, the time increment as well. Now we should see we have an attribute age, and that age is going to be progressing at frame 234, we should have an age of one. We can establish a life, let's say when we create the attributes, let's say that we create a life attribute, which is going to be the lifespan of the particle, and we could say, and we'll establish that each particle has a lifespan of three seconds. So when we go to the solver, we will need to remove every point or particle, let's create a point wrangle, and we'll remove every point that has an age that's above the lifespan. So if age is bigger or equal to life, let's say, if age is bigger than life, then remove point. It's going to be removing point from input zero, and the point is going to be PT number. And since this is just a line, we can write it like this, and now you go up, and we should see that the particles, after a certain point start to die. After frame 72, we start having particles die. And then the pops of a rule will be able to introduce concepts of randomness and variation that will make things look much better. For instance, here when we're creating the attributes on the velocity, for instance, right now we have a value of one on the velocity. Let's create some randomness, so I'll create a point wrangle, and I'll say that the velocity is going to be times equals 501. So I'm going to fit between zero, I'm going to fit a random number based on the point number plus the frame, just so we have a random seed every time. And we're going to give it a random variation between 0.5 and 1.5. So now if we have a look, I'll just say here, rent V, if we have a look at our particles, each one of them will have a different speed. If we disable this, we have all the particles, or all the points have one, the same value of one on the y coordinate. Turning this on will have a variation between 0.5 and 1.5. Now if we run the solver, we should see random velocity. Some are slow, some are faster, some go higher, some stay lower. So it's not the idea with this lesson, it's just to show you that it's not really that complicated to create your own kind of particle system, just based on simple rules and running those rules through the solver. Of course, a pop solver and working with pops, all these are going to be much easier to create. So, and to prove that we can go over a similar process, but just to create a very similar look, but with pops.

**Frame:** tutorials\frames\52-creating-a-simplified-particle-system-v1-1080p\frame_000.jpg


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
