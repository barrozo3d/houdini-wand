---
title: module i   week 03   01   introduction to volumes v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=hEcmhhNlpzY
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [volumes, vdb, sdf, fog-volume, velocity-field, vdb-reshape, beginner-intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-03-01-introduction-to-volumes-v1-1080p/
frame_count: 4
---

# module i   week 03   01   introduction to volumes v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=hEcmhhNlpzY)
**Author:** The VFX School Archive
**Duration:** 15m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, so welcome to week three. As per usual, let's go ahead and create a new project. Okay, so this will be we are in module one week, week three, call it whatever you like. And I'm going to say it's in my D drive. Okay, accept on that and then save always save your hip file. So what are we week three? There's one. Great. So yeah, this week is all about volumes. So I'm just clearing up my desktop there by the way, if you want to do the same, just delete those at the top, but you can work however you like. Now I'm going to create a geometry node. Let's call this volumes intro. So we'll just have a quick look at some volumes. So typically in Houdini, if we just drop down a test geometry, pick head, we haven't looked at these, but they're kind of hungry. If you again, you know, tab when you keyboard, start typing test, and you'll see we've got all these different pieces of test geometry. You've got this crag which has some animation and a rig. I think got a pig head repertoire, which are both just models static with textures. You're shadeable, this squalb, this weird alien thing, loads of cool stuff. So we're going to work with this pig head, but I'm going to turn off the shader. I don't want that. And just leave it on the medium. So yeah, typically in Houdini or well, any software package you're working with primitives and points of vertices in Houdini points and vertices. And they kind of, you know, they don't occupy 3D space, really they represent space. So each point, each primitive is infinitely thin. It doesn't have any thickness. Each point is infinitely small. You know, it doesn't occupy any volume. But a volume does occupy volume. So how do we make a volume? So a couple of options. We can use the older or less efficient way, which you know, I wouldn't recommend using, but worth talking about is ISO offset, which will create the native Houdini volume. So connect that and then right away, you can maybe see that if not to press D on your keyboard, turn your background dark and then we can see something that kind of looks like a volume. And we can increase this volume, the sampling division. So you're just kind of dividing this and giving it more detail basically continues to 100. There we go. So you can see that we've got different levels of density going through this. And then if we take a look at the information, we've got no, well, 1 point, 1 primitive, we've got this new thing, 1 volume here. And you can see that a quantity of voxels and how many voxels in each axis. Okay. So that's one way of doing it. Another way is to use something called a VDB from polygons, if we can find it. There you are. Okay. And then if we visualize that, get something that looks really weird. We'll talk about this in a minute, but for now, just turn off distance VDB and turn on fog VDB. Get something more, something similar. The way of splitting this up is not the same. So here we need to lower the value. It's a bit like, you know, a particle separation. So lower the value, the more detail we have, but that gives us a similar result. So, you know, what's the difference between a VDB and a Houdini volume? So basically a VDB is more, I'm not sure what VDB stands for, but it's a, it's basically more efficient. So the way that we can see that, if I drop a Wrangles, so a volume Wrangles, so don't worry too much about what this does. It's just a way of writing code onto volumes. Now, if I, so here we've got where creating a density attribute, you can see that. Okay, and we can, you know, raise or decrease that. So to access that, I just write density, which is the name of the attribute. And then I can equal, set it to two. And I will make it all darker there. You can see two, three, or I can lower it. I can set it to 0.1. Okay, which makes it pretty much disappear. Maybe there. Okay, now if I do the same over here, you'll see something different. Aha, we get a big box. If I set that to 1, we're getting an error there of some reason. I think because, yeah, we don't have a name there. If I change this to density, there we go. So now we're getting a box. So the reason for that is that the Houdini volumes creates a box, a kind of bounding box around your geometry and fills that with a volume. And basically, you know, wherever there isn't geometry, we've got zero value of zero and everything else has, you know, values of whatever you want. However, the VDB just kind of discards any empty space is it doesn't have doesn't contain voxels. So this is much more efficient in terms of memory. So we're talking about Houdini volumes because when you're working in pyro or simulations, we're still using Houdini volumes within the simulation. So when you run a simulation, what you'll get out of that is a Houdini volume. So you may want to convert it to VDB, if necessary, normally it's not necessary, but you know, they basically work in a similar way. It's just when you're working on geometry or kind of static things, not simulating anything, just stick to VDB is what I would do. So a volume can hold different types of attributes. So here we've just got density, but it can hold more. So we could, if we wanted a vector, if we add a point velocity node, we'll add some velocity. Again, I'm just demonstrating here, don't worry about, you know, velocity is just movement, a vector which demonstrates, which indicates movement, you know, velocity. So here I'm just going to drop this point velocity out of colonize. If you come here to this visualize it, display point trails that shows us the velocity. And if we just increase the scale, just so we can see it, maybe if I decrease the swirl size, sorry, increase the swirl size, so you get a sense there. We've got this kind of curly movement. So in a simulation, this would mean that, you know, this, if these were particles, maybe this, these would go this way, I would kind of, they would follow these lines, right. But this, I just want to show you here, if we come to the points, we've got a vector there, which represents the velocity. And this, we can store that within the volume as well. So if we come here and press plus, and if we select this point, V, you can see something changed there. So that's because the display, the view part is trying to display this velocity, it doesn't really do a good job of that. We can do that in another way. We can use a, first of all, if we use a volume slice. Okay, connect that up down here. So that's kind of taking a slice through the geometry, looking at the density in this case. Well, we can specify that's just the density there. But if we take the velocity, delete that and then grab a volume trail. Sorry, the volume trail requires points. So we got point where creating points here and the volume itself. Then we should start to see. Yeah, so trails. Okay, so you can see that these are the, these kind of visualization of that velocity. So obviously, you know, we can just see them here. But if coming out of a simulation, sometimes this is a useful thing to do. If you have a velocity, or you're generating a volume velocity to go into your simulation, this is a handy thing to do. Another way of doing this, if we take a VDB visualization tree, connect that up there. And so what this is showing us is, you know, that's the extent of our volume. You know, we have some padding on the outside and the inside, which is something we'll come back to when we look at distance VDBs. But this is another handy way of kind of visualizing your volumes. But I'm going to generate some points here, turn off these tiles there. Okay, and then connect that up. And this is a cool way of visualizing your velocities as well. Here we go. So there you can see it's kind of cool in itself. What those velocities look like. So it's worth also talking about, if I come here, this surface VDB. Okay, let me actually turn that back on and just drag this over. And I don't want the velocities on it. I don't think it should matter. I'm going to turn on this surface and get rid of that. So now this looks kind of different. So this is another VDB. You can also do this with Houdini. But again, this, you know, I wouldn't recommend it. It changes to STF volume. So they've got a different name, but it's the same thing. An STF volume or a surface, which is a for, you know, is an STF surface. It's just the name. You can change this to whatever you want. So this kind of looks different. You can see kind of looks like a surface. So this is a great way of working on geometry, basically. So instead of we wouldn't use surface volumes for any kind of simulation, you may. I've not done that myself. But this is a good way of working with kind of organic, you know, creating rocks and fixing problems with geometry as well. It's really handy for that. If I kind of demonstrate if we just take a transform and emerge, there's something I do. Oops. Not fire merge, just a normal merge. Grab that. I merge it together. And then if I kind of, if I do something, just like that, you know, you got. Intersecting geometry, you know, is very, very messy. If I connect that up, they kind of blend together nicely. And you can see on the inside, it's kind of made that hollow for me. It's kind of hard to see. But if I do it like that, you can see we've got a hollow space on the inside. Whereas here, I've got polygons in my face. And then what you can do is convert this back to convert back to polygons. It will give you a nice mesh. You can see these are connected now. And we've got a hollow space on the inside, which is a really nice way of creating geometry fixing problems with geometry as well. One thing to be careful of is when you take this and an obstacle can drag and make a difference one here. Because I want to make this hard. And that way it's just an open piece of geometry like that. We got a hole. And normally that's a bit of a problem you can see. You know, it requires a closed surface typically. But what you can do, you know, you can either try to, you know, just drop a polyfill, which will plug that hole for you, generate this. Or you can poly extrude. Also just kind of give it some thickness and make sure you check up it back. And that will also work. Another option is to take your VDB. So it looks like there's no information there, but there is something there. Now if we take a VDB reshape, SDF, that's it. Okay, and just connect that up. You can see it's a dilate. So that's kind of dilating, kind of swelling or inflating your volume. And if I start pushing that up, you get something like that, which is another very useful case. Something I use VDBs for also is, you know, making groups by swelling geometry like this. If you do that with polygons, they kind of, you get some weird results sometimes. So yeah, that's, we'll come back to these later. But first of all, we're looking at clouds. So we're going to be working with these nice soft, wispy clouds.

**Frame:** tutorials\frames\module-i-week-03-01-introduction-to-volumes-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Introduction to Houdini volumes: Houdini native volume (ISO Offset) vs VDB from Polygons (sparse, more efficient); fog VDB vs surface/SDF VDB; storing velocity vectors in volumes; visualization with Volume Slice, Volume Trail, VDB Visualization Tree; VDB boolean union for geometry blending; VDB Reshape SDF for dilation/swelling.

### Summary
15m11s intro lesson (VFX School Week 3, module-i) introducing volume concepts before cloud simulation. Covers native Houdini volumes vs VDB (efficiency = VDB only stores non-empty voxels); fog VDB vs surface/SDF VDB; storing velocity as a vector inside a volume (for simulation); multiple visualization methods (Volume Slice, Volume Trail, point generation from volume, VDB Viz Tree); boolean merge of VDBs to blend intersecting geometry; VDB Reshape SDF dilate for swelling/grouping use case.

### Key Steps

**1. Houdini Volume vs VDB**
- ISO Offset: creates native Houdini volume — bounding box filled with voxels (even empty space has voxels) → memory-inefficient
- VDB from Polygons: sparse grid — only non-empty voxels stored → much more efficient
- In pyro/simulations: simulation output is Houdini native volume; can convert to VDB afterward
- Rule of thumb: for static geometry/non-sim work, always use VDB

**2. Fog VDB vs Surface VDB (SDF)**
- VDB from Polygons has two outputs: distance VDB (SDF) and fog VDB
- Turn off distance VDB, turn on fog VDB → looks like a cloud/smoke (density field)
- SDF / Surface VDB: stores signed distance values (negative inside, positive outside) → looks like a surface; useful for geometry work and boolean operations
- Name attribute in Volume Wrangle: `density` for fog, custom names for SDF

**3. Storing Vector Attributes (Velocity)**
- VDB from Polygons → add Point Velocity node (adds v velocity vector) → Volume Slice to visualize density slice
- Volume Trail: visualize velocity vectors as trails (requires points + volume inputs)
- VDB Visualization Tree: shows volume extent/padding
- Scatter points from volume → display as trails = clean velocity visualization

**4. VDB Boolean Union (Geometry Blending)**
- Merge two geometry pieces (intersecting) → VDB from Polygons → they blend together seamlessly, with hollow interior
- Convert VDB back to polygons (Convert SOP) → clean mesh, hollow interior preserved
- Open geometry (holes): Fix with Poly Fill or Poly Extrude (Add Caps) before VDB conversion

**5. VDB Reshape SDF (Dilate)**
- VDB Reshape, type SDF → Dilate: inflates/swells the volume outward by specified amount
- Use case: creating selection groups from geometry by swelling (avoids polygon-based proximity artifacts)

### Houdini Nodes / VEX / Settings
- **ISO Offset** — native Houdini volume from polygons (legacy, avoid for static work)
- **VDB from Polygons** — sparse VDB; fog output = density field; distance output = SDF
- **Volume Wrangle** — write code on volume voxels; access voxel attribute by name (`density`)
- **Volume Slice** — cross-section visualization of a volume field
- **Volume Trail** — velocity visualization via trail geometry (requires points + volume)
- **VDB Visualization Tree** — shows volume extent and padding bands
- **Convert SOP** — convert VDB → polygons; creates clean closed mesh
- **Poly Fill / Poly Extrude** — close holes in open geometry before VDB conversion
- **VDB Reshape** → SDF type → Dilate: swells volume outward; useful for proximity grouping

### Difficulty
Beginner–Intermediate

### Houdini Version
H18.5

### Tags
[volumes, vdb, sdf, fog-volume, velocity-field, vdb-reshape, beginner-intermediate]

---

## Related Tutorials
- intro-to-houdini-volumes---beginner-course.md (deeper dive into volumes/VDB, Voxyde VFX)
- module-i-week-03-01-intro-v1-1080p.md (same week, project intro)
