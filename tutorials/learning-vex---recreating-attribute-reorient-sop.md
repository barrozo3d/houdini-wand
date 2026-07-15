---
title: Learning Vex - Recreating attribute reorient sop
source: YouTube
url: https://www.youtube.com/watch?v=TAWtLzrITOY
author: cgside
ingested: 2026-07-15
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/learning-vex---recreating-attribute-reorient-sop/
frame_count: 0
frame_status: pending-selection
---

# Learning Vex - Recreating attribute reorient sop

**Source:** [YouTube](https://www.youtube.com/watch?v=TAWtLzrITOY)
**Author:** cgside
**Duration:** 13m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py learning-vex---recreating-attribute-reorient-sop <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video we're going again to another nerdy rant about
[0:05] Vax, which will be basically recreating the attribute reorient with Vax. As you can see,
[0:10] we have a very similar result. Basically we start, I'm gonna do this step by step, but
[0:15] let me just walk you through. So we start with some test geometry, we split the UV seams,
[0:21] create some normals, and we measure the gradient of the position.y, so a value along the
[0:26] Y components, we measure that gradient, we move the geometry to UV space, so we do some
[0:32] sort of space transform between world position and UV space, and after that our attributes, our
[0:38] gradient that was previously oriented along the Y component of the surface is no longer oriented,
[0:44] let's say. So for that we use the attribute reorient and now we have the flow of the Y component
[0:49] of the mesh, as you can see with this gradient. That is easy, but I'm curious, so I wanted to know
[0:55] how I can recreate the sub, which is always useful to know how to recreate some some subs with Vax,
[1:01] and we will do that today, so and let's get started. So we're gonna start with the geo,
[1:09] and let's use the test geometry big, so big, let's not add the shader, like I was telling you,
[1:19] split the UV seams, because we want to move these to UV space and we want the UV,
[1:25] the UV attributes on points, let's also add some normals, because we will use them later,
[1:31] instead of having implicit normals, and let's do the gradient, so measure, gradient, position.y,
[1:42] and we can show points, so let's actually visualize that, let's name it,
[1:47] there, and let's visualize it, so marker vector, what?
[1:57] So marker vector, so that's fine. All right, now what we do, we add your good swap,
[2:07] and we do copy, for example, and choose texture and move it to position, and now let's ignore the normals,
[2:15] but the normals are also a queue, so the normals are no longer updated, as you can see,
[2:20] they are using, that's why we see these weird shading, so if we do attribute reorient,
[2:27] and we take this current geometry, and we will, we connect it to the second input, and we do
[2:36] there, now we have it, and we can also do normal, and the normals are updated, so actually the
[2:41] normals were a nice example to show you, how moving between spaces, we don't get our point
[2:46] attributes updated, so now let's do the nerdy parts, which is recreating this sub, with back,
[2:54] so I'm not gonna even, I'm gonna make my life even more difficult, and not move this geometry
[2:59] to UV space manually, with the attribute swap, so we will do it all inside a wrangle,
[3:05] so let's create an attribute wrangle, and let's name it, let's name it attribute reorient, reorient,
[3:15] let, and we will, the steps are the following, we will need to create a matrix showing the rotation
[3:23] matrix, showing the rotation of all the points, computing the matrix for all the points,
[3:30] regarding the rotation, and we need to compute the matrix also for the, for the UV geometry,
[3:35] and then we take the difference between the two, and we apply that computed matrix to the new
[3:41] geometry to update the attributes I mean, so let's do it step by step, and it will be easier to follow,
[3:48] first of all we need to compute the matrix that shows us how these objects is oriented,
[3:54] or rotate it, not object matrix, like a, just like a single point matrix, we need to compute them
[3:59] for all the points, so let's actually do it, we want to run over points, and first of all we need to
[4:05] make the first matrix, and for that we will need, we will need the current position, the normals,
[4:12] that we have, let's get rid of these, so we will use the normals, and the current position,
[4:17] and a neighbor, so let's start with a neighbor, which will be the first neighbor of the current
[4:22] point we are iterating over, so let's say zero, i, p, t, and the first neighbor, so let's say
[4:30] this point in here, and we just go and grab that point, that point number of the neighbor,
[4:36] so for now we need to create a vector between the current position and that neighbor, so let's do
[4:41] vector, and let's call it u, and we're going to make sure we normalize it, and we take the point
[4:47] expression to grab the position of that neighbor, and we subtract the current position,
[4:54] so that's our first vector, it's just like a vector pointing from the current point to the neighbor,
[5:00] then we're going to create another vector called v, which we're going to normalize also,
[5:05] and can be a cross product between the current normal, and that first vector,
[5:13] so the problem is that we can't make sure this first vector is orthogonal to the normal, so we need
[5:19] to do another cross product, so u, it will be again, we can normalize it just in case, and we just
[5:25] cross between this new cross between this new vector and the normal, and we will visualize this
[5:33] in a bit, so just to make sure we follow, so normalize cross between v and n, what is complaining about?
[5:42] Oh, it's not n, it's v at n, so if we visualize this as a matrix, so let's do matrix for a
[5:50] empty x, is equal to z, and we will do u, v and n, or v at n, 10, v at n, and if we visualize that
[6:03] right now, it will make a bit more sense, so marker and axis, and let's scale it down, so our z
[6:11] axis, as you can see in here, we set it to the normal, so this blue vector is the normal,
[6:17] then we have the x which is u, and we have v which is this green or y component, so this is
[6:24] good starting point, now we need to do this the same thing, but for the uv mesh, and in order to
[6:31] grab the uv mesh, we will just unwrap it in place, so string u, it will be u unwrap, and we take
[6:39] the current geometry and we grab from the uv, so this will give us a pseudo geometry, or we will
[6:45] unwrap it in place, and give us the exact same geometry as this, as you can see, this uv geometry.
[6:53] What we can do now is, for example, we can take the vector, let's say vector uv, so uv position,
[7:02] and we can just read the point position, so instead of typing zero, we type g, we want to access
[7:08] that q, and let's grab the position, and just write within them, so, and now we can just v at b,
[7:14] is equal to uv b, and now we have the uv geometry, so, but we don't want to do this, so the idea now
[7:23] is to do the same matrix computation, but for the uv geometry, but I don't want to do it twice,
[7:32] so I'm going to create a function, which is also a good way to show you how you can create
[7:37] custom functions in Vax, so let's get rid of this, and let's create a function around this, so,
[7:44] let's define the class, so it's a matrix that we want to get, and let's call it a calc matrix,
[7:53] a calc mdx, now we need the arguments, and the arguments, the first one, as you can see,
[7:58] for the second one, we are reading the position of the uv mesh with this string, which is the geo,
[8:06] so as you can see, the string, but for the other ones, we are using a new, new american put,
[8:11] so that will be a problem, we can't just have a string or an integer, so we need to define one type
[8:16] for the input, so I'm gonna define it as a string and call it input, because we can use a trick
[8:24] to instead of using new american put, we can use actually a string, and I'll show you well,
[8:29] then we're gonna grab the normal, and the position, so we can just use a comma,
[8:35] and then we will grab also the point number, so those are our arguments, and let's open the brackets,
[8:45] so we don't have a return, what we want to return at the end is the matrix, and this will error out,
[8:52] so let's, no one step at a time, so let's actually copy this, and paste it inside here,
[8:59] and the neighbor, we will just replace it with input, ptnum, we replace current position,
[9:06] because we can use local variables, so let's replace it with pause, which will be our current
[9:10] position, here we use n, and here we use n, oh I forgot to copy this, and we just define in here
[9:20] and matrix, empty x, and we return the matrix, oh we are using n in here, so let's use n,
[9:26] and now this should be working,
[9:33] let's continue, there might be something we need to do in here after that, so let's now
[9:41] call the function, so first of all we unwrap the geometry, we get the position,
[9:52] and we also get the normal, oh no we don't grab the normal because it will be the same,
[10:00] as the world space normal, so we just set a custom normal along the z axis,
[10:07] because the geometry will be facing, yeah so uvn, the geometry will be facing the z axis as you can see,
[10:14] so we just define it as the normal of our uv mesh, then we will create matrix,
[10:22] rest, empty x, and we will call the function, so call empty x, now we will do it for the world space
[10:30] position, so for that instead of using a numeric input, we will use a string, and we use up input
[10:38] column zero, and then we need to pass the normal, which is the current normal, the current position,
[10:45] and I add bitinum, so let's see if that errors out, no, and then we need to do the same, so matrix
[10:54] uvnth, and it will be the same, call empty x, and we pass the gul, the uvn, the uvp,
[11:07] and we use again i at bitinum, and now if we calculate the difference matrix, so let's call it empty x,
[11:17] and to calculate the difference matrix, we divide one matrix by the other, or you can do the
[11:22] inversion of the rest, empty x, multiplied by the uvnth, and now if we do v at b times it goes empty x,
[11:35] we get all of this mess, because we actually need to also apply the translation on the matrix,
[11:43] so in here, we call back, and we translate, because this is a 4x4 matrix, and we translate the matrix,
[11:51] and we do it by the current position, and now if we apply, we get the geometry, the matrix
[11:59] computed correctly, and we can translate it to the uv position, so now we're simple, so we have
[12:08] let me check, as you can see the normals are still problematic, because they have the other space,
[12:15] the word space normals, so we can just do v at n, multiply equals, and if we do empty x, let's see,
[12:22] that seems correct, somehow, but it's still problematic, because the normal is a vector attribute,
[12:28] and we don't want to translate the normals, so we just apply a matrix 3, so we cast it to a matrix 3,
[12:34] to only apply the rotation, and now the normals are correct, and let's see finally our attribute,
[12:38] which is there, as you can see is all over the place, so if we do the same,
[12:43] we get there, multiply equals by matrix 3 again, so we don't want to apply the translation,
[12:48] and empty x, and now there's something missing in here, so there's actually a bug in our code,
[12:58] because I'm using zero input in here, and we need to use input, sorry about that, and now it's
[13:05] correct, as you can see we successfully translated this locked top into a vex solution,
[13:13] and you might ask why all that work to recreate something that already exists, well, to the
[13:18] precise reason, when you don't have the sub you can create it on your own, so learning all this
[13:25] stuff can help you to come up with your own versions of the sub, or recreate something that
[13:30] doesn't exist by default, that's the power of Aldini, that you can customize it to an extreme level,
[13:36] so yeah, I hope you have learned something from this, please let me know if you have another
[13:41] way of doing this sort of thing, and as always you can grab the files on my Patreon,
[13:47] and let me know what you think in the comments, thank you, and I'll see you next time.



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
