---
title: Houdini 22 | How to Create Pyro in COPs | Configure Pyro Recipes
source: YouTube
url: https://www.youtube.com/watch?v=xKrHwJRo-nI
author: Houdini
ingested: 2026-07-18
houdini_version: "Houdini 22"
tags: [cop, pyro, volumes, simulation, compositing, intermediate, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini 22 | How to Create Pyro in COPs | Configure Pyro Recipes

**Source:** [YouTube](https://www.youtube.com/watch?v=xKrHwJRo-nI)
**Author:** Houdini
**Duration:** 14m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This video will show you how to work with the Cops Pyro Recipes.
[0:06] Currently, the recipes use the Cops Pyro Block 2.0.
[0:10] This version puts all of the relevant solver controls on the block and node, and doesn't
[0:14] require solvers to be placed inside the block for standard functions such as dissipation,
[0:18] disturbance, buoyancy, etc.
[0:21] These recipes show various explosive and smoke-based effects, but in this video, we'll just be
[0:25] looking at two of them.
[0:27] Let's start working with our Cops Pyro Recipes.
[0:29] In here, we're going to type in Cops just to grab a Cops Network and drop it down in
[0:34] our object context.
[0:35] This is going to be our geometry object that's going to hold our different Cops Networks
[0:39] inside of it.
[0:40] I'm just going to call this Cops Pyro Recipes, and then we'll dive inside.
[0:46] This Cops Network here is going to contain our smoke simulation, so let's just call that
[0:51] smoke.
[0:52] Let's dive inside of that.
[0:53] In here, we can type in Pyro Config, and this is going to show us all of our Pyro Configure
[0:59] Fire, Fireballs, Candle Flames, cigarette smoke, all of these different setups that we
[1:03] can take a look at, and also our Pyro Configure node, which is basically just a helper node
[1:07] that can help you set up data going into a Pyro simulation.
[1:12] What we're going to do first is take a look at the Bilawee smoke.
[1:14] Let's grab that.
[1:15] We're going to click, drop that down.
[1:16] We're going to see that this adds a bunch of different nodes in our Recipes setup here,
[1:21] and we can see that we actually have a little source in our viewport here.
[1:25] I'll turn the grid on just so you can kind of see that we're in there 3D view here.
[1:29] Let's also change the background to Dark Gray, just to see our simulation just a little
[1:34] bit better.
[1:36] From here, we can see that the Pyro block is what mainly controls this.
[1:40] This has been recently updated to a 2.0 version.
[1:44] The input block here, the begin block, is basically just a pointer to the end.
[1:49] This is where you plug in all of your inputs and they can go and get passed through into
[1:53] this simulation block here.
[1:55] But the end is where all the normal things are set up that we would associate with something
[1:59] like a Pyro simulation.
[2:01] So if you're at all familiar with the Pyro Sop workflow, this should feel very familiar
[2:05] to you.
[2:06] There's setup in here, different things for setting up bounds, collisions, sourcing.
[2:11] Sourcing looks pretty standard here.
[2:12] We've got density, temperature, velocity, that types of things.
[2:15] Our fields are in here.
[2:16] We have forces as well.
[2:18] So a lot of different controls that you would expect from things like your Sop or your
[2:23] Dopp workflows are all put into this block end here.
[2:27] Makes it pretty easy to work with.
[2:28] And unlike previous versions, we don't have to have these intermediate kind of nodes inside
[2:32] of the loop.
[2:33] So we can see here that we have our Pyro configure in our source.
[2:36] Those are both getting plugged in at the intro or at the input block here.
[2:40] And the output is going into these nodes here, which are going to help us rasterize this
[2:45] three-dimensional volume.
[2:46] If we hit play here, we can see this three-dimensional visualization of this.
[2:50] And it's going to take that and flatten it into a 2D representation.
[2:54] And that's what we're going to be doing in Copernicus, right?
[2:56] Because Copernicus is ultimately a 2D image manipulation system, we want to probably
[3:02] bring this three-dimensional data down into two dimensions so that we can manipulate and
[3:06] bring it through to the final renders basically that we want to use this in.
[3:11] So with that in mind, we have a couple of nodes here that help us do that.
[3:14] I'm just going to give myself a little bit more room by changing this vertical layout
[3:18] a little bit.
[3:19] And here we can take a look at a few different things.
[3:20] We have our light ambient.
[3:21] Now, this node by itself isn't going to output anything that's very useful to take a look
[3:25] at, but this can be used to adjust the color and the lighting on our actual volume.
[3:31] So if we go to our rasterize volume here, we can see that now we have this flat two-dimensional
[3:37] image.
[3:38] And in order to see that a little bit better, what I'm going to do is I'm going to do an
[3:40] RGBA to RGB node just at the end here, just so we can see the black border around this
[3:45] so we can get a better understanding of what's happening here.
[3:48] There is also some pre-multiplication happening here.
[3:50] So I'll just turn this off to make sure that we're not getting that render artifact right
[3:53] there.
[3:54] So we have our RGBA to RGB node here that's showing us how this is going to look.
[3:58] Gives us just a better visualization without the alpha in there.
[4:01] We can see the boundaries of our rendered layer here.
[4:04] And this rasterize volume is what's obviously driving that.
[4:07] Now there is another part to this and that is using these now built-in camera operators
[4:12] in Copernicus.
[4:13] So you can see here, this is the camera that we're using.
[4:15] There's our frustum.
[4:16] And at the end of the frustum is going to be the plane that our image is being rendered
[4:20] from.
[4:21] So there you can see at the end of that, there's our 3D view and we're basically flattening
[4:24] it down to a two-dimensional grid.
[4:26] And there is our render.
[4:27] And you can see here that we can change our ambient light.
[4:31] We could change the intensity of this, right?
[4:32] This is just basically our ambient lighting in our scene.
[4:35] We could also change something like the density scale and that's going to change how much,
[4:41] basically how much contrast there's going to be between the inner part of this and the
[4:44] outer part from the lighting and things like that.
[4:46] So that's going to include the volume differently, things like that.
[4:49] And this is basically just a way to adjust our ambient lighting in our scene.
[4:53] Since we're in Copernicus, we don't actually have lights.
[4:56] We're going to use this node to kind of work with some of our volumetric data and light
[5:00] it with the information that we do have.
[5:03] So overall, that is how this Pyro configure node will work.
[5:07] Let's take a look at these inputs here because these are sort of important for how Pyro
[5:12] simulations work in Copernicus.
[5:13] So the first thing is here's our Pyro configure node.
[5:15] If we take a look at this, this is basically a way that we can just set up our simulation,
[5:21] what the voxel size is going to be of it.
[5:22] And this outputs a reference VDB that goes into this VDB reference port on the input here
[5:29] on the Pyro block begin.
[5:30] So now down here, you can see that we have also a source shape.
[5:33] Let's take a look at what this is.
[5:35] This is actually being driven by the new implicit surfaces.
[5:38] And this source shape allows us to use several of those implicit surfaces to kind of use
[5:43] these to build simple emitter shapes basically.
[5:46] So here you can see we have a sphere.
[5:48] We can also change it to be a torus if we wanted, or we could change it into something
[5:52] like a tube or a box.
[5:53] So with a few different just basic sources that we can use here, we can also use more complicated
[6:00] implicit surfaces that have been brought in from our SOP geometry context.
[6:05] In this case, we're just going with these built in ones that we're using here.
[6:09] And implicit surfaces are like almost like a mathematical version of what an STF is.
[6:12] So it knows mathematically where the surface of this volume basically is and describes
[6:20] it mathematically.
[6:22] So you get these perfect representations of these surfaces.
[6:25] So that is what more or less what an implicit surface is.
[6:29] The other thing you can do with this pie-rosource shape is change a bunch of sourcing controls
[6:32] here.
[6:33] We've got density, temperature, things like that.
[6:35] We also have transform, the size of it.
[6:38] And there's this nice little distortion here.
[6:39] So if I turn that on and just go to the end block here and go back to the very first frame
[6:46] and just adjust this distortion amplitude a little bit, you'll see that this is going to
[6:50] actually kind of push and pull the edges of this volume in some interesting ways and
[6:54] it also has some animation to it.
[6:55] I'm going to turn this off because we didn't have that on originally, but there's a lot
[6:59] that you can do with these pie-rosource shapes.
[7:02] So just take a look at those, play around with them and they can kind of give you some
[7:05] nice basic shapes to be able to emit into your pie-ros simulations.
[7:10] Now that we've taken a look at this billowy smoke option, let's jump up one level and add
[7:14] a new cop network here.
[7:16] So I'm going to do a cop network like so.
[7:20] And then we're going to call this one fire.
[7:24] And so from there, let's now jump inside of this.
[7:28] So we're going to do our pie-ro configure and we're going to do pie-ro configure fire.
[7:38] And so now you'll see that this is slightly different.
[7:40] We have a couple other things in here.
[7:41] We have a source shape.
[7:42] We have a collision shape.
[7:43] We also have our standard pie-ro configure up here.
[7:46] Our source is going to just be a disk basically with a little bit of noise on it.
[7:52] If you look in all of these, there's also an option to scale by noise.
[7:55] You can add noise into the individual fields if you'd like to as well, not only just distorting
[7:59] it, but changing the actual field itself.
[8:02] Now down here is a collision shape.
[8:03] This is just a plane.
[8:04] So this is basically like our ground plane that we're putting in here.
[8:07] And if we look at these inputs, you can see we have our source points and our collision
[8:11] points.
[8:12] And that's basically just the geometry that's defining those two different elements that
[8:14] are being input into our pie-ro simulation.
[8:17] Again, there's not really a whole lot changing here.
[8:20] There's some stuff with fields as far as cooling and things like that.
[8:23] Some of our forces are slightly different.
[8:26] But let's just take a look at what this looks like here.
[8:28] So I'm just going to press play and see what happens here.
[8:30] And what you're going to notice, first of all, is we're actually not seeing any color
[8:33] like we would in our SOPS version of pie-ro.
[8:36] The reason for that is we're actually just seeing the density field here.
[8:40] We're not able to actually see the color on top of the density here.
[8:43] So we're just viewing that one field coming out.
[8:47] We could also view things like temperature or the velocity field.
[8:51] We could also view the flame field.
[8:53] So we can actually look at the individual fields themselves, but we're not able to actually
[8:58] visualize those as colors just out of the box from the pie-ro solver itself.
[9:02] So if we want to look at the 2D Rasterization method, we can take a look at this.
[9:07] We can also light this with the ambient light and then use our light scatter to basically
[9:11] scatter inside of this volume itself with some color based on an emission scale and density,
[9:19] things like that.
[9:20] And we can get some nice emission from this.
[9:23] So I'm going to hit play here.
[9:24] We can see this now 2D image.
[9:27] And I'll just display the camera here so that we can see what angle that's coming from.
[9:31] There you go.
[9:32] And so now we have our two-dimensional flame that's basically being rasterized here.
[9:37] You can see there's various noises on the input and that's changing it slightly.
[9:42] And so this 2D kind of point of view is coming from that camera.
[9:46] And we're able to rasterize this here.
[9:47] And you can see we can adjust things like how the emission is being controlled and the
[9:50] scale of that.
[9:52] And we can also come down here and change the tint on that as well.
[9:55] And if we look at the light scatter, that's obviously scattering different color based
[10:00] on the emission that's coming into it.
[10:03] And for the emission, usually what we'll use is the flame output and bring that into
[10:07] the emission right here.
[10:08] And you can see you can wire these things together by using the light output and the
[10:12] light input here.
[10:13] And so you can kind of go through and port these all together and you'll get your various
[10:18] kind of effects kind of all stacked together.
[10:20] We've also done a little bit of blur on the flame field itself just so that the emission
[10:26] isn't quite so solid there.
[10:29] Now what if you wanted to view this as an actual three-dimensional simulation instead of
[10:35] a two-dimensional simulation coming out of here before you rasterize it.
[10:38] Maybe you want to make sure it looks sort of the way you want it to.
[10:41] Well, what we would use is the VDB visualize.
[10:43] So I'm going to type that in and we're going to use the VDB visualize.
[10:47] And so if we take a look at this, we can see that we're looking for a few different things
[10:50] here.
[10:51] We're looking for density, color, emit, and emission color.
[10:54] And so we don't have to plug all these in, but let's just start kind of wiring these
[10:57] in here.
[10:58] So let's wire the density into there.
[11:00] And we can see that this is basically going to be more or less the same as what we saw
[11:04] coming out of there.
[11:05] We can change the density this way, but that's more or less going to be exactly the same.
[11:11] So from there, let's also now grab the emission, right?
[11:15] So we know that that's going to be our flame field.
[11:18] So let's bring that over here and select it like so.
[11:22] And we can turn our emission scale up a little bit.
[11:25] And so we'll do that.
[11:26] We can maybe keep our density scale down.
[11:29] And as we turn this up or down, you can see that this is going to be changing the emission
[11:32] that's happening in here.
[11:34] So let's just take a quick look at what we have in our rasterized volume here.
[11:37] So we have an emission scale at about 45, our density scale at about 15.
[11:42] So let's go in and do those for this.
[11:44] So here we can do our density scale 15, and our emission scale at 45.
[11:51] So we only have a white volume here.
[11:54] So this is a little bit odd.
[11:55] And what we can do is a couple different things.
[11:57] What we can first do is use our mono to RGB.
[12:04] So we can use mono to RGB.
[12:07] And what we can do is we can change this mono volume here of something like temperature.
[12:11] That's usually what we control our flame colors with, especially in our sap pyro workflow
[12:15] and our DAP pyro workflow.
[12:17] So with that in mind, we can now go over to our mono to RGB.
[12:20] We can compute the range here and just make sure that this is sort of been defined well
[12:26] for us.
[12:27] We could maybe go a little bit later here in this and just compute that range again.
[12:31] There we go.
[12:32] And what we're going to do is we're going to adjust the ramp.
[12:34] We're going to grab our little drop down here and we're just going to grab that default
[12:37] black to orange.
[12:39] Now again, this isn't actually able to visualize that.
[12:41] But when we bring this over here into this visualize VDB node, we can see that we're now
[12:47] starting to visualize this itself.
[12:50] And what we could do from here is we could actually do a pyro ambient pyro light ambient
[12:59] and we could plug this into the in line to this.
[13:03] So we could take this RGB, put this into the light input and then we could take this light
[13:07] output and go into both CD and emit CD there.
[13:12] And we also have to wire in our density in order for this to work.
[13:14] So we're just going to wire the density in there.
[13:17] And then we can play around with this a little bit.
[13:19] We could turn the density scale maybe up a little bit.
[13:23] We could turn turn the exposure down a little bit.
[13:29] Basically, we can play around with this a bit and see and get something that's going
[13:38] to be a little bit more representative of what it is that we're actually doing here.
[13:42] And the last little detail that I forgot to copy over was if we come up here to our ambient
[13:47] light.
[13:48] We'll copy over this exposed color.
[13:49] It's a little bit darker.
[13:51] So we're just going to come down here and paste that value in.
[13:54] We should see now that this is going to look a lot closer to what that final render is
[13:59] going to look like.
[14:00] So if we do this VDB visualize versus this here, we'll see that it's fairly close.
[14:05] It's not a one to one, but it'll give you a little bit better understanding of what
[14:09] your simulation might look like.
[14:11] And you can go in here and change some things around with the mono to RGB if you want to
[14:16] have this be brighter, darker, whatever.
[14:20] So you can come in here and hopefully get these to match just a touch bit closer like
[14:24] so.
[14:25] This is how we can use our different pyro recipes to be able to learn a little bit more
[14:30] about how simulations and specifically how pyro simulations work within our Copernicus
[14:35] context.



---

## Captured Frames

- [1:21] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_000.jpg
- [2:40] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_001.jpg
- [3:44] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_002.jpg
- [4:16] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_003.jpg
- [5:50] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_004.jpg
- [9:32] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_005.jpg
- [12:45] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_006.jpg
- [14:03] tutorials/frames/houdini-22-how-to-create-pyro-in-cops-configure-pyro-recipes/frame_007.jpg

---

## Structured Notes

### Core Technique
Running full Pyro simulations inside Copernicus (COPs) in Houdini 22 using the built-in Pyro Recipes, which are driven by the **COPs Pyro Block 2.0** — all solver controls live on the Block End node, no intermediate solver nodes inside the loop.

### Summary
Official SideFX walkthrough of two COP Pyro Recipes (Billowy Smoke and Fire) in Houdini 22. The recipes drop a complete network: `Pyro Configure` (voxel size → reference VDB), implicit-surface `Pyro Source Shape` emitters, the `Pyro Block Begin/End` sim loop, then rasterization to 2D via `Rasterize Volume` with `Pyro Light Ambient`/`Light Scatter` lighting and COPs' built-in camera operators. Also covers previewing the sim in 3D with `VDB Visualize`, coloring flame via `Mono to RGB` (temperature field → black-to-orange ramp), and matching that preview to the rasterized output.

### Key Steps
1. Object context: drop a `COP Network`, name it (e.g. "smoke"), dive inside.
2. Type "Pyro Config" in the TAB menu → pick a recipe (Billowy Smoke, Fire, Fireballs, Candle Flame, Cigarette Smoke) — nodes and a viewport source appear automatically.
3. Understand the **Pyro Block 2.0**: `Block Begin` is only an input pointer; **`Block End` holds all sim controls** (Setup, Bounds, Collisions, Sourcing — density/temperature/velocity, Fields, Forces — dissipation, disturbance, buoyancy). No solver nodes needed inside the loop, unlike 1.0.
4. `Pyro Configure` sets voxel size and outputs a **reference VDB** into the Block Begin's VDB-reference port.
5. `Pyro Source Shape` uses the new **implicit surfaces** (sphere/torus/tube/box, or SOP-imported ones) as mathematically perfect emitters; per-field sourcing controls (density, temperature), transform, scale-by-noise, and an animated **Distortion** amplitude.
6. Rasterize to 2D: `Rasterize Volume` (density scale ≈15, emission scale ≈45 in the demo) + `Pyro Light Ambient` (color/intensity — COPs has no real lights) viewed through COPs **camera operators** (frustum's far plane = the rendered image plane). Append `RGBA to RGB` (premultiply off) to inspect without alpha.
7. Fire recipe: adds a `Collision Shape` (ground plane) and a noisy disk source; feed the **flame** field into emission; slight blur on flame softens the emission; Light Scatter adds colored in-volume scattering; tint controls on the rasterizer.
8. Viewport shows only single fields (density/temperature/velocity/flame) with no color — for a colored 3D preview use `VDB Visualize` (inputs: density, color, emit, emission color).
9. Color the preview: `Mono to RGB` on temperature → Compute Range → default black-to-orange ramp → into VDB Visualize CD/emit CD, via `Pyro Light Ambient` (RGB → light input; light output → CD + emit CD; density also wired). Copy the ambient's exposed color and tweak density scale/exposure to approximate the final rasterized render (close, not 1:1).

### Houdini Nodes / VEX / Settings
- `COP Network` (Object context container)
- `Pyro Configure` — voxel size, outputs reference VDB
- `Pyro Source Shape` — implicit surface emitters; Distortion amplitude; scale-by-noise per field
- `Pyro Block Begin` / `Pyro Block End` (**Pyro Block 2.0** — all controls on End: Bounds/Collisions/Sourcing/Fields/Forces)
- `Rasterize Volume` — density scale 15, emission scale 45 (demo values); emission map ramp; tint
- `Pyro Light Ambient` — exposed color, intensity, exposure, density scale (ambient lighting substitute)
- Light Scatter — emission-driven in-volume color scatter
- `RGBA to RGB` — Remove Premultiplied Alpha off for inspection
- COPs camera operators — frustum far plane = render plane
- `VDB Visualize` — density/color/emit/emission-color 3D preview
- `Mono to RGB` — temperature → Compute Range → black-to-orange ramp

### Difficulty
Intermediate

### Houdini Version
Houdini 22 (COPs Pyro Block 2.0, implicit surfaces, COPs camera operators are H22 features)

### Tags
#cop #pyro #volumes #simulation #compositing #intermediate #houdini-22

---

## Related Tutorials
- Copernicus fundamentals: `references/copernicus.md` (COP context reference)
- Pyro production pipeline: `recipes/pyro-hero-shot.md` — SOP/DOP pyro counterpart to this COPs workflow
