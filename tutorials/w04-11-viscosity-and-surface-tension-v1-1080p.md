---
title: w04   11   viscosity and surface tension v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=1yb3mindncw
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [flip, fluid, viscosity, surface-tension, jitter, kernel, sub-steps, simulation, beginner-intermediate]
extraction_status: complete
frames_dir: tutorials/frames/w04-11-viscosity-and-surface-tension-v1-1080p/
frame_count: 4
---

# w04   11   viscosity and surface tension v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=1yb3mindncw)
**Author:** The VFX School Archive
**Duration:** 12m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now before I forget, there's one more thing I want to do in the emitter. We jump into the flip source and I'm just going to press spacebar and F to focus in on the selected node. I'm just going to put this in Y of frame so we can see the points. So if I press play now, you can kind of see the kind of static. So to get just a bit more variation in their initial position, you can use this jitter seed. Right? So if I move that, you can see they move. And to get this moving per frame, we've done this before, dollar F. And that way, when I press play, they will each frame, they'll have a different position. Okay, the jitter scale is just how much they move. If I put this to zero, you can see it will be in a grid. So one is fine for us. There's no, can't see any pattern there. So just that. What I want to focus on now, so if the last flip hook we did was pretty chaotic. You know, there was much form in the splash of the fluid. So I'm going to look at adding a couple of things. Just to demonstrate, I'm just going to make another dot network here, actually, just to have something simple and clear. You don't have to do this if you don't want to, just for demonstration. So I'm just going to drop in another dot net and another flip solver. All right, with some gravity in there, and then a flip object. So I'm just going to use the default, oops, default cube for this. And let's bring down the size of this. If we go into volume motion, I think it's in volume motion, yeah, the box size, I just middle click, go down to 20 and maybe move it up 10, something like that. So let's go to the ground plane. Well, move it down up five, maybe just so it's not on the ground. There we go. And then I'm going to bring the particle separation down. Let's do zero two, let's say, and the guide particles turn this to particles. Just so we've got dots there. Okay, let's see, maybe jitter it a bit as well. Let's see, there we go. Put it up to one. Great. So what I want to look at, let's just press plane, see what we get from this cube. See that drop? And just peer through the ground, one thing I forgot to do, turn on these closed boundaries. So that makes this like one big collider in a sense. I'm going to make this a little bit smaller as well. Let's go down to there. Okay, press play again and see. It would be pretty, even get a square where it lands on the ground, see it doesn't look very realistic there. So what I want to do is look at viscosity. So we've already done that in when we did the ice cream, we're also going to look at surface tension in this lesson. So let's just turn that on first of all and see if we get anything different from. So instantly we can see we don't get a square as it splashes on the ground, get a circle. And that's because even before it's collided with anything, it's trying to form a circle basically a sphere. The surface is pulling itself around and trying to form more fluid shapes. So the surface tension can be really helpful for forming these kind of tendrils. You've got to be careful with it. If we put it up too high, you get some weird kind of oily looking, which maybe what you want but it can be easy to go over the top with it. You can really see it being pushed there and you get these sneaky, oily kind of forms with it. And again, it does depend on the scale and you can play around here just to get a sense of it. But even when we move on to our other sim, we will have to play around a little bit with it. And let's try adding some viscosity as well. I'll just turn that on. Remember in the other lesson we used the viscosity attribute, which we imported, but we don't have that here because we've only got the one fluid so it's not necessary. But remember, you need to actually give it some viscosity here. I'll put it up to something pretty low. As this is so small, I'm using pretty low values here when we go to the other sim, we'll raise the map of it. So there you see, they're kind of competing with each other now. You can see the viscosity holding it together, just put this way down to three or something. So you can see the surface tension pulling it round. The viscosity holding it together, it's definitely going to get a bit more details there. Maybe even less. Put it down to one. Okay, starting to get something a bit more interesting there. Another thing I wanted to look at is the this, the velocity transfer. So the way that flip works, it's kind of an almost like an interplay between volumes and particles. What we're watching, what we're visualizing is particles. The way the velocity is calculated, it takes the volume motion into account. So that's why we have things like volume motion here. The velocity is kind of an interplay between the two. So we've got two options here. We've got splashy kernel and swirly kernel, which is kind of self explanatory. But what we can also do, just to get some more information on any parameter really. If you just hold the mouse over, you'll get a little bit of a description. So this says, specifies the method for using transfer velocity from particles to underlying grid before solving them back to the particles. Doesn't help us too much. It sounds a bit complex, convoluted. But then underneath, even more useful, in my opinion, if you see us as press F1, so let's do that. And I will take us directly to the side effects help pages. And we can see we're in the help pages for the flip solver. So I highly recommend doing that when you're playing around with, you know, we've got so many different parameters. Lots of these we haven't touched. But it's useful to go around and, you know, basically changing things, seeing what's happened, putting up the values, lots and experiments. And but also coming in here to read the explanations. So right at the beginning, they've got a splashy versus swirly kernel. So we can take a look at that. And basically it says here, see, we've got splashy. Swirly kernel is typically used for high-voticity simulations. You need to reduce surface noise as much as possible, okay? We're still retaining the swirly nature of the simulation. For example, small scale fluids. So in our case, it is kind of more of a small scale thing. We've got a splash against the strawberry. We don't have a big river or a beach scene or something, which is quite common to do. So let's try this swirly kernel instead. I'll flip that over and see. I'm not sure if we get much different here with this small cube. So we'll definitely switch that over on our other sim. Okay, so let's, I'm just going to jump out of this, delete it. This strawberry, I'm just going to visualize just because it doesn't look nice with the mountains. I'm just going to visualize it from here. Put this back to, let me go, I shade it. And let's implement those in here. So I want to turn on the swirly kernel. Okay, enable viscosity and surface tension. I'm going to, the numbers here are going to be higher because we do have, you know, the volume is bigger. We've got a bigger sim going on here. So we need more surface tension. We've got more velocity. We've got the, it's been kind of squirted out the side of this, of the emitter. Right. So I'm going to push it up to 300. And the viscosity is well. I'm going to push that up to about the same 350. All right. And I'm going to leave this, let's push it down. I'll leave it at three. I'm going to push the, these sub steps up. So if you remember each frame, the flip solver will calculate the position of each particle. So if you want to get more detail, we need to calculate it more times per frame. So that's what sub steps are. So if we jump here into the DopNetwork, we can add more sub steps here. I'm going to put this up to, just do two for now, just double it. Jump inside there. So we got our, just a double check, we got our viscosity, particle separation at three. Let's drop that down to two, a bit more, kind of creeping up in the numbers. Here we got our surface tension, viscosity and swirly kernel turned on. Okay. So back to our camera. Full screen and let's have a look at this flip book. So flip is done. Let's take a look what we've got. I certainly, different. Again, I'll jump this up to frame 38 there. Just watch that part, the slow motion bit. So you can see it's definitely holding together a bit better now. Getting this kind of envelope around with some blobs around. There's some kind of drips being pushed away, some tendrils here. So that's cool. It's still a bit big though, but I'm going to be pushing up the sub steps and the particle separation in a minute. And that will calm things down a bit. So it's kind of a balancing act, you know, it's a bit difficult, but you know, the more we drop down the particle separation, they will slow down a little bit. Okay.

**Frame:** tutorials\frames\w04-11-viscosity-and-surface-tension-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
FLIP viscosity + surface tension for milk/strawberry sim: enable surface tension in FLIP Solver → prevents square splashes, forms tendrils; viscosity holds fluid together; Swirly Kernel (Volume Motion tab) for small-scale high-vorticity sim; increase DopNetwork sub steps for detail. Final milk sim: surface tension=300, viscosity=350, swirly, sub steps=2, particle separation=2.

### Summary
12m32s VFX School Archive module. Part of the Week 4 strawberry-collides-with-milk simulation. First demonstrates viscosity + surface tension on a simple cube DOP test, then applies those settings to the main strawberry+milk sim. Key concepts: FLIP Source jitter seed `$F` for per-frame variation; surface tension prevents square-shaped splashes (makes sphere/circle); viscosity holds fluid together (1–3 for small demo, 300–350 for larger sim); Splashy vs Swirly kernel (swirly = high-vorticity, small-scale); DopNetwork sub steps for more detail per frame. Uses F1 shortcut to open node help pages.

### Key Steps
1. **FLIP Source jitter**: Jitter Seed = `$F` → per-frame unique particle positions; Jitter Scale = 1 (default); 0 = grid pattern
2. **Closed Boundaries** (DopNetwork/FLIP Solver): enable → treats sim bounds as collider, prevents particles escaping
3. **Surface Tension** (FLIP Solver → Surface Tension): enable → particles pull into spheres/circles instead of flat splash; high values → oily, stringy look; balance carefully
4. **Viscosity** (FLIP Solver → Viscosity + FLIP Object → Physical):
   - Small demo: values 1–3
   - Main milk sim: values 300–350
   - Viscosity and surface tension compete/balance each other → tendrils + cohesion
5. **Velocity Transfer Kernel** (FLIP Solver → Volume Motion → Velocity Transfer):
   - Splashy kernel: default, choppy/turbulent
   - **Swirly kernel**: better for small-scale high-vorticity sims (like milk splash); retains swirly nature; recommended for this shot
   - Press **F1** on any parameter → opens Houdini help page for that node
6. **DopNetwork Sub Steps**: set to 2 → calculates particle positions twice per frame → more detail, slower
7. Final milk sim settings: surface tension=300, viscosity=350, swirly kernel ON, sub steps=2, particle separation=2 (down from 3)

### Houdini Nodes / VEX / Settings
- FLIP Source: Jitter Seed=`$F`; Jitter Scale=1
- FLIP Solver → Surface Tension: enable + value (300 for milk scale)
- FLIP Solver → Viscosity: enable (value set in FLIP Object, not here)
- FLIP Object → Physical → Viscosity: value 350 for milk scale
- FLIP Solver → Volume Motion → Velocity Transfer: **Swirly Kernel** (for small-scale high-vorticity)
- DopNetwork → Sub Steps: 2 (doubles calculation frequency per frame)
- F1 on selected node → Houdini help documentation
- Volume Motion box size: 20, position move up 10; Closed Boundaries: enable

### Difficulty
Beginner–Intermediate

### Houdini Version
H18+

### Tags
[flip, fluid, viscosity, surface-tension, jitter, kernel, sub-steps, simulation, beginner-intermediate]

---

## Related Tutorials
- w03-04-adding-viscosity-v1-1080p.md (basic viscosity introduction, same course)
- w04-01-introduction-v1-1080p.md (week 4 introduction)
- w03-11-meshing-v1-1080p.md (FLIP meshing workflow, same course)
