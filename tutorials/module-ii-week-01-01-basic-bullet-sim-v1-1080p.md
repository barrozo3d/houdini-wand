---
title: module ii   week 01   01   basic bullet sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=vQSQgkSvm8g
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/module-ii-week-01-01-basic-bullet-sim-v1-1080p/
frame_count: 4
---

# module ii   week 01   01   basic bullet sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=vQSQgkSvm8g)
**Author:** The VFX School Archive
**Duration:** 7m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Right, so here we are in week two. And this week is all about rigidbody simulations, rigidbody dynamics as they're known, ABD. So let's create a project. So project name will be module two. I said run week two and we're in module two week one week one. Let's have a little dash there. Okay, let's be usually save it wherever you want. So we'll basically just build up in complexity in this first week just looking at the bare bones of a rigidbody bullet simulation and just kind of start off super simple, look at a little bit of fracturing and some constraints towards the end as well. So let's just start with a geometry node here and we'll call this ABD intro. Okay, time inside. Let's get a box. We'll start with just the easiest way to make some kind of simulation. We'll start with a box there. Just piece it my parameters and just raise it up. Maybe rotate it. Randomly don't worry about copying parameters. And then press tab and look for ABD bullet solver. Okay, visualize that and we've got two nodes and we've got a simulation. I mean, it's not super interesting. It's just falling down. Make it a bit more interesting if we go into ground here, give it to ground plane and it just drops. So you know, that is a bullet simulation super simple, but it is what it is. Two nodes, look at that. So easy. So the bullet solver, ABD bullet solver, so being able to do all this in shops is quite is a recent addition and it kind of does a lot of things under the hood here. So as you can see by this padlock, it's got a lot of stuff going on on the inside. And they expose all of this to you. So let's look at how, you know, because you know, typically I tend to use these, but it could be that you need to have access to the Dobnet to be able to build this in Dobps as well. It's important to know how to do that as well. So we'll look at that. So let's have a Dobnet work. Okay, plug that in. So we don't have anything in here yet. So let's find we need the rigid body solver. I've got a few other solvers. There's just bullets solver. And then you've got the ABD solver, I think there as well. And this one kind of encompasses both. I always use rigid body solver for ABD simulations. And it's using bullets. You have ABD as well. And this fracture thing, but I never use them. Just use it for bullets. And then ABD packed object. So there needs to go in the first part. And that gives us a clue. We're not seeing anything yet. If we go to first context geometry, we are seeing that. We've got our box there. So we've got an error there. If we take a look, we can see geometry does not contain any primitive types supported by the solver. So what that means is it's looking for packed objects, but we don't have a packed object. Okay, so you know, this is doing that internally is packing our box. So what does that mean? Look at our box here. You can see, you know, we have access to all the primitives. It has eight points, primitives, and so forth. And now if I drop, it's saying we need packed objects. So if I just type pack, put that there. Take a look. You can see visually is kind of looking different. And when I go to select it, that looks different. It's only one box. And then if I look at the information, now I've just got one point, one primitive, one vertex. And we've got this new thing packed geo, one packed geometry. So it's kind of an efficient way of dealing with geometry, you know, with this, all of those points and primitives and the location of all them is packed away. We don't have access to them until we unpack. Okay. And then we have the same as what we had before. So this is, you know, bullets requires packed geometry. It has to be packed to work. Okay. So this will, it's simulating now, but it's not doing anything because we don't have any forces. And you, once you do pack something, if we go into the geometry spreadsheet and go into, if I can remember primitives, and then intrinsic, you can see we've got a whole bunch of other attributes here, which are specific to packed geometry. So packed for transform, you can see we've got a load of values here related to the transform with where our box is. Okay. And you can use these for, to manipulate your geometry before going into the simulation, or within the simulation as well, but typically don't really need to do that, to be honest. So we could add some gravity in here. Same gravity that you use in any simulation, just gravity, put it there. So now it will fall. And let's give it a ground plane and merge that in. So hopefully, you know, if you are just starting out with Houdini, you know, we've done a few different simulations already. Starting to see a pattern with these simulations that we always have object, so that whether that's a VD object or a vellum object, pop object, and then you have a solver, nine times out of 10, 99 times out of 10, you have gravity, a ground plane, and then merge together this way around, and that goes into your output. You know, it's just kind of the same pattern, and then just add on your other bits and bobs. Often you have a source, which you can do with bullets as well, but we don't need to. So we've got the same thing now. We should look identical, I think. We template that. We've got the same, more or less the same thing happening. We've probably got different physical properties, like, you know, bounce and stuff like that. Okay, so, you know, there's your first bullet simulation. How exciting. So obviously next we'll look at making this more interesting, more complex.

**Frame:** tutorials\frames\module-ii-week-01-01-basic-bullet-sim-v1-1080p\frame_000.jpg


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
