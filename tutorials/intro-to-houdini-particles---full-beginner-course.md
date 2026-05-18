---
title: Intro To Houdini Particles - Full Beginner Course
source: YouTube
url: https://www.youtube.com/watch?v=94YAomHfMbw
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Not specified (H19–H21 UI)"
tags: ["dop", "sop", "vop", "particles", "simulation", "attributes", "wrangler", "procedural", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/intro-to-houdini-particles---full-beginner-course/
frame_count: 8
---

# Intro To Houdini Particles - Full Beginner Course

**Source:** [YouTube](https://www.youtube.com/watch?v=94YAomHfMbw)
**Author:** Voxyde VFX
**Duration:** 122m30s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Basics [0:00]
**Transcript:** Particles in Udili can be pretty easy to set up and get some cool results, but they can be truly difficult to master.  We'll start off simple with all of the basics stuff, but then we are going to step a little bit outside of what I would call beginner level with some of the lessons.  So I don't want to just tell you what buttons to press or sliders to adjust to get pretty effects.  I want you to understand the fundamental concepts of how particle effects work.  Over the years in my professional career I had to make dozens if not hundreds of particle shots,  and these techniques I'm about to show you I applied in almost all of the shots.  They will also carry over to other types of simulations like Vela, Marbidis,  Flip, basically anything that deals with points.  So my goal with this course is to set you up for long term success so that no matter what particle effects you want to create,  you can apply these lessons.  I hope you will find this course useful and let's get started.  Let's dive in and let's get started.  I'll create a geometry container and let's step inside.  Now really all particle effects and all effects in general start with a source,  and it's usually a geometry...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_000.jpg

### Geometry VOP [13:06]
**Transcript:** so let's start with a pretty simple example and let's say that instead of having these particles move  just straight up let's make them go towards an end goal so I'll press you to step back outside at  the sub-level and here next to my sphere I can just drop down and add node and I'll hit this plus  to create a simple point we have a point here in the middle of our scene and also in our display  material icon here I will right click this and I'll switch the display here to points so now it's  just a little bit bigger maybe I can also press the on my keyboard and go to geometry settings and  I'll just increase the point size so we can see this better in our viewport so I can press enter  while having this end node selected and I can just drag this point up in space and let's say that  I want my particles to reach this point let's also drop down a null from here and I'll just rename  this to goal so we keep things nice and organized and this is what we'll actually use to reference  later in our geometry vop and now to make our particles go to this point we have to create this  direction vector and let's maybe just preview our sphere as well I'll press E on my sphere and  select the g...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_001.jpg

### VOP Examples [35:46]
**Transcript:** simulation so I'll go ahead and let's get rid of this geometry VOP I'll just disconnect this and  place it over to the side and for a tornado simulation we might need to change the geometry source  so I'll go up and instead of a sphere let's drop down a torus and let's plug this here and maybe  for my torus let's look at our torus I'll just increase the first radius value here let's just  make this bigger and maybe decrease the second value so it's kind of thin and I might want to just  increase the resolution for the subdivisions this will be fine let's go back inside so currently  we are not doing anything let's actually get rid of this pop color as well and let's go to our  pop source I've should have done this from the beginning let's just disable the guide geometry  so we just see our points all right so if I press play nothing happens or our points just spawn  and now if we want to do a tornado effect with our pop forces nodes we can use a pop  axis force let's drop this here and if I press play nothing happens and this is already a problem  that's really annoying this pop force works with this radius that we have inside here and we have  to increase our radius and now we can...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_002.jpg

### Sourcing [50:14]
**Transcript:** have an idea on how the particles can move equally as important is how we are sourcing in the  particles so let's talk more about this pop source node over here and to better explain this we  can change the source geometry so I'll go up and let's replace this store us let's just do a simple  grid and I'll plug this here let's go to our grid and let's increase the subdivisions here let's  do 100 by 100 and let's see if this works all right so let's go back inside and in our source  tab we have this emission type set to scatter onto surfaces now there are some other types which  we will get to in a second let's focus on this one for now now this does exactly what it says it's  each frame it's looking at our geometry and it's scattering points onto it so maybe I can set this  to a point display and actually let's just disable the geometry for now and let's make these  particles static so if I go forward in time we can see each frame we are just simply adding a new  set of points on top of the previous set of points that we had and each frame we get a different  seed for our scatter so we can control the amount of points we scatter through the birth tab if I  increase this if I add ano...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_003.jpg

### Attributes & Inheritance [75:50]
**Transcript:** inherit any attribute from the source so let's take a look at an example where this is useful  let's maybe just start fresh and we want to create something like a explosion burst type of effect  so let's start fresh and I'll drop down a circle let's set this to zx plane and maybe I will make  this smaller let's increase the subdivisions and I'll decrease the uniform scale to maybe 0.25  and in this case we can see that we don't have any points on our geometry inside the border so  this is again another good example why sometimes you have to scatter your own point so let's drop  down a scatter from here let's disable relaxation disable max point limit and I will maybe want to  decrease this let's maybe use 50 total point count and from here let's create a velocity attribute so  I will do this with an attribute verb let's rename this to set v and I'll step inside now if I want a  burst type of effect I can create the velocities based on our origin so let's say that we want the  points to scatter from the 0 0 0 coordinate here the center origin all we have to do is simply  subtract our points from this center point so from my p I will do a subtract let's promote this  second input to ...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_004.jpg

### Interpolate source [93:58]
**Transcript:** birth time and interpolate source do let's set up another example so I'll go up and we'll need  an animated source to better explain this so I'm just gonna go ahead and let's use test geometry  Craig and this comes with animation by default so if I look at this this is how the animation looks  now let's try to spawn particles from the hammer and I'll go forward in time and really I'm  interesting in this portion of the animation where he swings the hammer and we have some speed  so all I'm gonna do here is let's go ahead and in this animation frame let's add set this to  100 or rather add 185 so this will essentially just offset our animation 185 frames  forward so at frame one we start off with this swinging animation so from here let's isolate  the hammer I'll press S and we can simply grab the hammer and I'll press delete and let's delete  non-selected now the thing with Craig is that this comes as a packed geometry so if I look at the  information here or even here we only have one point and we also have this one packed Geo's that  shows up here so we will have to unpack this let's drop down an unpack now packed geometry is a whole  other subject by itself which will cover more...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_005.jpg

### Collisions [102:31]
**Transcript:** Finally let's talk about collisions and we'll do another example for this let's start again  with a circle and let's let's set this to zx plane and let's also make this smaller increase the  divisions here and let's start to scatter some points drop down is scatter and again the same  things that we did earlier let's go ahead and change the global seed type the dollar ff expression  here and we'll keep this at a thousand all right so we have a random seed per frame now we can use  a attribute of opt to create some velocities like we did earlier but there's a pre-build node that  Houdini set up for us that does pretty much the same thing so we can use a point velocity here  and let's set this initialization to set to a value and we'll use 0, 1 and 0 so this creates the  velocity vector if I turn on the visualizer here is the vector that we have and we can give this  any direction that we want let's just keep this straight up and we also have a very handy  curly noise tab option here so if I turn this on we can just use this to create our noise I'll  scale this down and also the swirl size and maybe increase the grain so kind of the same thing  that we did earlier but we're just usin...

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_006.jpg

### Conclusion [121:21]
**Transcript:** course and I really hope this was helpful I will admit that some of the techniques and workflows that  I've shown might be a little bit more advanced not really suited for complete beginners but like  I mentioned I don't really want you to waste time learning the shortcuts and the pre-built way that  Houdini offers us I would much rather you learn the proper workflow and the proper techniques  from the beginning and sort of rewire your brain into working more with VOPs so whether  it's at the sub-level or at the top level I hope by now that you understand that it's really  the better way of working and it's what's going to allow you to not hit walls all the time and  really progress the furthest in the long game so this was pretty much it thank you for watching  if you want to see how I use particle simulations in real world projects you can check out my pro courses  on VauxSight.com more courses are coming so stay tuned

**Frame:** tutorials\frames\intro-to-houdini-particles---full-beginner-course\frame_007.jpg


---

## Structured Notes

### Core Technique
Professional Houdini particle workflow inside DOPs: POP network setup with Geometry VOP for per-point custom velocity control, sourcing strategies, attribute inheritance from animated geometry, interpolated source, and collision detection.

### Summary
A 2-hour course on Houdini particle simulations from Voxyde VFX, pitched at beginners but covering production-level techniques. Covers the full DOP particle pipeline: popnet/popsource/popsolver setup, custom velocity via Geometry VOP (rather than pre-built POP forces), multiple sourcing types, attribute inheritance, interpolate source for animated geometry, and static/moving collisions. Strongly emphasizes the VOP-first workflow over using shelf presets.

### Key Steps
1. Create geometry container → step inside → build source geo (sphere, torus, grid, circle) → `scatter` SOP if needed for point distribution; disable Relaxation and Max Point Limit
2. Add `popnet` → step inside → connect source geometry to `popsource` input; `popsolver` drives the simulation at each frame
3. Build custom velocity in `geometryvop` (at sub-level inside DOP): `bind` P → `subvector` with goal null position → `normalize` → `bind export` V — particles now seek the goal point
4. `popaxisforce` for tornado/swirl — must set Radius to encompass particle cloud or it has no effect; preview at 120fps
5. Control emission in `popsource` → Birth tab: Emission Type (Scatter onto Surfaces / All Points / Continuous); `$FF` expression in Seed for per-frame variation; Birth Rate for density
6. Inherit source velocity: build `attribvop` before DOP → subtract P from origin `{0,0,0}` → store as `v` attribute → DOP inherits it automatically via Attributes tab in `popsource`
7. Animated source: use `testgeometry_craig`, isolate piece with S+Delete, `unpack` SOP (required for packed geo), feed into `popsource` → Birth tab → enable **Interpolate Source** to sub-frame interpolate positions
8. Add `staticobject` node in DOP for static collision geometry; `rbdpackedobject` for animated colliders; `popbounce` controls Elasticity and Friction inside the POP network
9. `pointvelocity` SOP alternative: Initialization → Set to Value + Direction; enable **Curl Noise** tab with Scale/Swirl Size for organic motion without manual VOPs
10. Convert particle cloud to volume: `vdbfromparticles` (Particle Radius Scale, Minimum Radius in Voxels) or feed into pyro solver as emission source

### Houdini Nodes / VEX / Settings
- `popnet` / `popsolver` / `popsource` — core DOP particle system container and engine
- `popsource` → Birth tab: Emission Type (Scatter onto Surfaces / All Points / Continuous); `$FF` seed; Interpolate Source checkbox
- `geometryvop` (inside DOP sub-level) — per-point attribute VOP running on particle points each frame
- `bind` VOP — reads named attribute (P, V, age, etc.) from points; Name must match exactly
- `bind export` VOP — writes modified value back; Export: Always
- `subvector` VOP — subtraction: P - goal_position = direction vector toward goal
- `normalize` VOP — makes direction vector unit length for consistent speed
- `popaxisforce` — Axis Force inside POP network; Radius must cover geometry; creates swirl
- `popbounce` — Elasticity, Friction parameters; handles collision response
- `staticobject` DOP — static collision geometry; requires collision representation
- `rbdpackedobject` DOP — animated/moving collision geometry
- `scatter` SOP — Total Count: 50–1000; Relaxation: off; Max Point Limit: off
- `attribcreate` SOP — Name: v; Type: Vector; Value: velocity vector before entering DOP
- `pointvelocity` SOP — Initialization: Set to Value; Direction: 0,1,0; Curl Noise: Scale, Swirl Size, Grain
- `unpack` SOP — required to unpack packed/instanced geometry before use as particle source
- `null` SOP renamed "goal" — position reference for directional velocity target
- `vdbfromparticles` SOP — Particle Radius Scale; Minimum Radius in Voxels; Fog VDB or SDF
- `$FF` expression — frame-dependent seed for per-frame scatter variation

### Difficulty
Intermediate (labeled beginner, contains production-level techniques)

### Houdini Version
Not specified (H19–H21 UI)

### Tags
#dop #sop #vop #particles #simulation #attributes #wrangler #procedural #intermediate

---

## Related Tutorials
- [Intro To Houdini for VFX - Beginner Course](./intro-to-houdini-for-vfx---beginner-course.md) — #dop #sop #vop #attributes #simulation #procedural
