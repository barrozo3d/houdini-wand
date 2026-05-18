---
title: VOPS 04 - Geometry Interactions - Houdini Beginner Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=qDtKmbCDn3k
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vops-04---geometry-interactions---houdini-beginner-tutorial/
frame_count: 0
---

# VOPS 04 - Geometry Interactions - Houdini Beginner Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=qDtKmbCDn3k)
**Author:** Voxyde VFX
**Duration:** 44m22s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Distance & Import Point Attribute [0:00]
**Transcript:** We continue the VOP series with part 4, geometry interactions.  In Houdini there are several ways to use geometry for simulations.  In this part we cover what different operations do and when to use them.  In Houdini there are many ways that different geometries can talk to each other.  So we can have any geometry and we can grab attributes from other geometries  and combine different attributes like position or velocity or really any attribute.  So this will come up all the time in VFX.  So let's say for example we have a particle simulation that starts off the ground  and we want the particles to slowly form the shape of a human or any other shape.  We would have to know how to access information from that human mesh or geometry  and how to apply it in our simulation.  So I will show you some of the main ways that we can achieve this interaction between geometries  and the differences between them.  So I will start with a Geocontainer and I will just drop a grid and maybe just scatter some points  and I will increase the total count.  And we will plug this inside an attribute VOP.  So let's step inside and probably the simplest way to grab attributes from a different geometry  is...


### Nearpoint [5:30]
**Transcript:** So this import point attribute is working fine when we are dealing with just one point.  So we can actually manually point it to the point number, to the correct point number  by doing a constant here and setting it to zero.  But what happens if we have multiple points that we want to interact with our geometry?  So if I go up, let's go ahead and delete this node.  And let's do another scatter from the same grid.  And if I go to this result, let's maybe just scatter a few points.  Okay, so let's say that we want to use these points to generate the distance values.  So I will plug this in the second input and if I check the result,  it will only consider now the point number that has a value of zero.  So if I turn on the point number display, we can see that this one here is going to have a ptNum value of zero.  So this is the one where we generate our distance from.  So if I preview the result, we can see that it's this one over here.  But let's say that we want to consider all of the points.  So let's maybe template our second input.  So our second scatter, we can now use a near point function to determine  based on our position, which of these points, so from our second scatter, ...


### Find Attribute Value [8:56]
**Transcript:** So this import point attribute is very useful.  And we can see that we can combine it with different nodes in order to retrieve the point number that we are interested in.  We can of course use it on the same geometry that is modified in some sort of way.  So I'll go ahead and let's get rid of all of these.  Let's actually go up to our scatter.  And I'll get rid of our second scatter here.  Maybe I'll just delete this attribute.  So let's say that this geometry for whatever reason we needed to go through a different process in order to create a attribute or to modify the position.  So let's say that on the right I will just simply do a attribute noise vector.  And I just want to mess up the position a little bit.  So let's go to this.  I'll set the vector here to be.  And I just want to displace the points.  And maybe I'll just increase the element size.  So this is just to give you an example, but let's say that we achieve this result through some simulations or through some other different methods.  And then on our original geometry.  So on this regular scatter, let's do another attribute.  And let's say that this chain on the right.  So what we are inputting here on the left, th...


### Minpos , XYZDist, PrimUV [20:11]
**Transcript:** Let's take a look at some other ways that geometries can interact with each other.  So I prepared a scene here we have a torus, so just a simple torus, that's a little bit above the ground.  Then we scatter some points on this torus, and then over here we have a grid.  And let's not worry about these nodes that are turned off for now.  But we plug the points of our torus in the first input in an attribute VOP and the grid will go in the second input.  So let's dive inside the attribute VOP and we can see nothing is currently happening.  And one other way that we can interact between the geometries is by using a minimum position.  So let's drop the minimum position node.  So this will return to us the closest position that each of these points can find on the second input.  So on our grid geometry, it will return the closest position on the primitive.  So if I go up real quick, we can see that our grid does have a bunch of primitives.  Now it could work with any amount of subdivisions here and we will see this in a second.  So let's go back inside.  We want our points to look at our grid.  So I will plug the input into the open put tool, which is our grid.  And from the position tha...


### Intersect [28:30]
**Transcript:** So the minimum position and XYZDist combined with the primitive attribute are very useful when we are trying to communicate with a geometry that has primitives.  And I pretty much use them in maybe 95% of the time, but they have some shortcomings, and I want to demonstrate this.  We have the same setup with a torus on which we scatter points, and to the left we have the same grid, so just a flat grid, and let's go inside our attribute VOP, and we are using the minimum position.  So in the mix node here, if I change the bias, we can see exactly where they land on our grid.  So this is working fine because we are dealing with a flat surface, so we get a pretty consistent result.  We kind of retain the shape of our torus. But let's see what happens if we modify our grid.  So I will go to this grid, and I will enable this edit node, where I grab a few points, and I just move them up a little bit.  So if I go to the result of the minimum position now, we have a very weird result, and if I go inside and change the bias, we can see exactly what's happening here.  As I decrease the bias and go back to our original position, we can see, and maybe it's worth if I template our geometry, we ca...


### PCOpen & PCFilter [34:55]
**Transcript:** So minimum position xyz dist and intersect are all fine when we are dealing with geometry that has primitives, but what happens when we want to interact with a geometry that only has points.  So again, we have on the left here a torus and we scatter some points onto this torus and we have the same grid, but instead of dealing with primitives, let's only deal with points.  So let's scatter some points and work with this. So earlier we used a near point function to find which of these points are closest to our geometry.  So if I template this, probably we can see this better in this attribute box. So I already set up the near point function that we created earlier.  So if I go inside, we are grabbing the nearest point from our second geometry and grabbing the position from the points. And in this mix, now we can see that if I increase the blend, all of the points are going to find their nearest point from the second geometry and they're all going to move to that position like so.  So if I wanted to have a more consistent result and get more of the original torus shape, I would have to go up and I would have to scatter more points.  So we would have more information for our position. ...



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
