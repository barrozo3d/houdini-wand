---
title: VOPS 03 - Vector Operations - Houdini Beginner Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=oT6qzs-Vffk
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vops-03---vector-operations---houdini-beginner-tutorial/
frame_count: 0
---

# VOPS 03 - Vector Operations - Houdini Beginner Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=oT6qzs-Vffk)
**Author:** Voxyde VFX
**Duration:** 31m12s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Subtract, Normalize, Length [0:00]
**Transcript:** Welcome to Intro to Vops Part 3, Vector Operations.  Knowing how to manipulate vectors is going to be your ticket to mastering any kind of simulation  in Houdini.  Now we can talk about Vector Operations, so as visual effect artists we have to know how  to manipulate vectors in order to control the movement of any type of VFX, so whether  we are working with particles or with smoke simulations or we are doing rigids, it's  going to be extremely important to know how we can tell the geometry to move in the way  we want.  So let's go ahead and get started and I will just drop down a Geocontainer and let's  do our test on this Robert toy test geometry, so I will drop this here and I'll just make  this bigger, maybe I'll set the uniform scale to a value of 3 and let's go ahead and do  an attribute VOP and we will step inside and in order to create just a simple vector  we can just drop down a constant and I will set this to a tri-float which is going  to give us a vector and I will just plug the result in our normal, so now I can turn  on the normal display here so we can visualize the vector in our viewport, so I can give  this any direction I want, I can set this to 0, 1 and 0 and no...


### Cross Product [13:18]
**Transcript:** important, now we can talk about the cross product and to illustrate what the cross product is,  I created a simple representation in subs, so ignore all of this over here, this is basically  just creating this thing we have here, so let's say that we have a point over here from where these  two vectors are originating from and if we do a cross product between these two vectors  we are going to get a vector that's perpendicular to these vectors, so if I turn on the normal display  we have this point here with this blue normal vector and if I were to adjust our other vectors,  so if I were to modify this, this vector will always be perpendicular to this sort of imaginary plane  that's created between the other two vectors, so I can make these vectors closer to each other  and it will still create this imaginary plane and we will have this vector that's perpendicular  to the plane, so this is the cross product only of course this vector will also originate from  the point that actually contains these two vectors, so a more accurate representation would be if I  move this point to the same origins, so over here where we have the actual origin of the point,  I just placed this point in...


### Dot Product [24:00]
**Transcript:** the viewport here, so again we are going to have two vectors that originate from the same point  and when we do a dot product operation between these two vectors this is going to be the result  that the dot product will give us, so it will look at the angle between the two vectors and it  will generate a value that goes from one to negative one, so if I decrease the angle between these  two vectors like so we can see that when we start to line up both of these vectors we get a value  closer to one, so when they are completely pointing in the same direction we are going to have a  value of one and as I start to increase this angle difference between the vectors we are going to  go over to a value of negative one, so negative one will mean that the vectors are essentially opposite  to each other and when they are perpendicular we are going to get a value of zero, so this is the  dot product let's move over to our rubber toy and again we will have normals on all of the points  and let's just work with points so we will work from this scatter node, so I will drop an attribute  of here and let's go inside and we will compare the normal with a vector that points directly up  and let's se...


### Reflect [29:00]
**Transcript:** cover is going to be the reflect and this is a vector operation that I rarely use but sometimes  it can be useful so if we focus on our green vector here this will be the first input in our  reflect node and this gray arrow here this is the second input and the result will be our red  vector over here so as I change the rotation of the green vector we can see that this red arrow  gets reflected and this gray arrow you can think of this as sort of like the plane that creates  this reflection so this green vector will sort of bounce off of this gray vector and it will create  this bouncing red vector so over here I have a grid as we can see that's also mapped in the same  direction as our gray vector so we can visualize this a little bit better so if I go back to my green  arrow and change the rotation we can see how this creates sort of like this vector that bounces off  of the ground so we can imagine that if we have a particle simulation and something comes from  over to this side if we want a separate effect to happen we can match the angle sort of on the  other side with this reflect node so now also if we change the rotation of our gray vector we can  see how this affects our r...



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
