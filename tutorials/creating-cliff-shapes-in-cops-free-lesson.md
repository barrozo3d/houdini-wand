---
title: Creating Cliff Shapes in Cops | Free Lesson
source: YouTube
url: https://www.youtube.com/watch?v=62Mo7udZM_o
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [cops, procedural, texturing, noise, terrain, environment, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Creating Cliff Shapes in Cops | Free Lesson

**Source:** [YouTube](https://www.youtube.com/watch?v=62Mo7udZM_o)
**Author:** cgside
**Duration:** 25m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Okay guys this is where we left off last last time and now we will create the
[0:05] CopNet work for the Stonewall. So let's I just saved a new thing and I'm gonna
[0:11] create in your CopNet and let's get started. So the first thing we're going to
[0:20] do is some sort of cliff and so we can later layer on top of the stones to
[0:27] give it more detail. So let's start with that. Let's go with the nasty F shape and
[0:34] I'm gonna change it to regular polygon, change the number of sides. Five you can go
[0:41] with your own setup. I'm just gonna copy what I have. That worked well for me
[0:48] but basically you can start with a few shapes and start to build up your effect.
[0:52] Right now we're just gonna build the cliff. Well so let's do an nasty F2 mono
[0:58] and in order to have some details we don't want a solid effect we will do
[1:04] like instead of the solid we will do ISO distance and I think I'm going to
[1:12] invert to have this sort of result because if we do a layer properties and we
[1:19] go in here and set the typing to height you can see we have some sort of slope
[1:27] that we can play with. So let's also create a cube 3D and as I mentioned in
[1:35] in the introduction we will be using these cobstance nodes. So this is from
[1:40] cobstance, this cube 3D but if you really want to create it this is just a cube
[1:45] with a transform with some parameters linked and then resturize the depth. So
[1:51] that's basically it. So then we're going to equalize to have enough range and
[1:57] we can play with the I mean we do an equalize so we can play with the range a
[2:02] bit so let's change the white 0.5 and then we can do a blend in here and blend
[2:08] this one with this one and I think we're going to do a min dark and so
[2:14] minimum something like this and if we preview that we get this sort of
[2:22] it and shape as you can see and you can play with the range a bit more it depends
[2:27] on what you want. Alright so what's next? Then I'm going to create a right
[2:33] tall noise and I believe in this case I use the 3D but if we use a 3D it won't
[2:40] tile so it's better to use it to the noise so I'm gonna change this just
[2:47] something like 0.0.2 maybe a bit more 0.08 something like this and the rest is
[2:55] fine so as you can see this noise will actually tile where's if we do a 3D
[3:00] noise this one tile as you can see we use a 3D noise when we have a position
[3:07] so like or hp that comes from a mesh, the original position of the mesh that way
[3:15] it will tile it will perfectly blend with the original position of the mesh. In
[3:21] this case we don't have a mesh we just gonna do this fractal to the noise. Then
[3:26] we need to distort this shape because right now it's just to uniform so I'm just
[3:31] gonna do a multi-directional warp again from constants and we're gonna connect
[3:38] these in here and as the intensity we're gonna connect this fractal noise
[3:43] like this and we need to play with the settings in here so basically an intensity
[3:50] of 20 and we change it to max so like this maybe a bit more maybe 26 it's fine
[4:01] and you can start to see how that looks so we need actually to do
[4:07] RGB RGB8 to mono I believe this is because this know that's this issue of only
[4:14] using RGBA so we need to place an RGB8 to mono so we get something like this which is fine
[4:21] and what else we can do yet another one
[4:26] but this time we're going to transform to the not this one so transform
[4:35] transformation to the and we're gonna get same noise
[4:39] and we're going to stretch it so we can have some more reason down stretch so I'm
[4:46] gonna set the width to 1000 let's see how that looks
[4:51] hmm I think we need to apply with yes and then we can do in here a directional warp
[5:04] and let me see yeah we can do whatever directional warp and we need to connect of course a
[5:11] noise in here I like see how much did I use so maybe around minus 54 an intensity of 10 so we
[5:21] get some sort of result and then we can connect this one to the directional warp
[5:28] and let me see in this case we're just gonna use a value of two for example and set it to max
[5:35] let's find and finally we can do let's see how that looks something like this and finally we can do
[5:44] a slow blur also and connect we can reuse the same noise we can also place a patch in here
[5:53] so we don't always have to be referencing the have these cables in the way but anyways
[6:01] let's do a slow blur and make sure we increase the temp the samples and intensity we can just have
[6:08] a value of 0.15 and maybe change these to max so let's see how that looks
[6:18] though it's not much maybe we can increase it a bit more 0.4 so we're just layering effects over and
[6:27] we're just trying to distort this initial shape because later we will just scatter them randomly
[6:32] and create the clip shape it will make more sense in a beta promising so now we're going to
[6:41] layer yet another effect so let's do a crystal noise and let me see in this case I use the 3D but
[6:50] again we don't want to use a 3D because it went tile to D will tile as you can see
[6:56] what you can see in here and we're just gonna change the center like this element size we can change
[7:03] it to 0.5 something and we can play also with the offset oh offset let me see something like this
[7:13] and I guess the rest is fine then from here from the slow blur we can do a directional work
[7:25] and let's connect this crystal in here let me see how that looks so in this case we want
[7:34] quite a bit in the density and change the angle to something like this so we just maybe that's a bit too
[7:44] much let me see this is not giving me the best result let's just keep it and I'll see in a bit
[7:58] how we we're looking the end because right now we're gonna create a ramp
[8:07] and make sure we set it to vertical and we have a vertex and we do levels for example you can
[8:14] also play with a remastered thing and in the levels I'm just gonna decrease the value increase
[8:22] this value to 1.33.1.3 and the the outer value to about 0.59.3 something like this
[8:35] and then we can do a blend so we'll just want to play with the height so I'm gonna set this
[8:42] to and in this case I'm gonna set it I believe to
[8:46] deploy no in this case to max no sorry minimum so now this will look more like leaf shape as you can
[8:57] see but then again we'll lose all the detail from the that we had previously so let's just
[9:10] see in here I want again the same effect so I'm gonna do a fetch and I'm gonna fetch the same ramp
[9:26] so select and then I'm gonna do is the grams again
[9:31] and I'm gonna change this contrast to 1 and value to 0.5 and I'm just gonna do a directional
[9:46] warp of this and this one in here and this one I'm gonna set it to minus 90 and
[10:00] and I believe to the ordy and then we can just blend it over so I'm gonna blend this with this
[10:12] and in this case I'm just gonna set it to subtract so subtract and we get the top shape so we get
[10:22] this and this and then finally we can fetch yet again the same crystal so fetch and get this crystal
[10:34] and let me see in here so we fetch the crystal in here and we do a directional warp
[10:49] and we connect this crystal in here and I'm going to set the value to 14 point something and
[10:58] I need a city of 50 let me see how that looks yeah something like that
[11:10] and then we can do transformation to the so what am I doing here yeah I'm just gonna flip it
[11:20] now I'm gonna get this directional warp I'm gonna do a transformation transformation to
[11:28] and I'm just gonna flip it so or is it all mirror and this is one of the shapes and then
[11:45] we're gonna get again we're going to back we're going back and duplicate this crystal lines
[11:51] we're just creating some shapes and I'm gonna increase the the styling play with the offset
[12:00] and change the amplitude to 1 and actually I will change the amplitude to 1 in here also
[12:07] and I'm gonna do yet again directional warp and I'm going to get the slope blur that we have in here
[12:16] and this is one and this is the second and for this one I'm just gonna increase the angle
[12:27] to something like this and change the intensity to 20 for example
[12:34] and then in here we can do a blend and we're going to blend between the we're going to blend
[12:44] between the levels so in here I'm just gonna min darken this so minimal and from here we have let's see
[13:07] what do we have in here we can get rid of this so we have this shape we have this shape and this shape
[13:26] so that's it then we're going to do a cable pack and we're going to pack first of all this shape
[13:34] then the mirrored one so we're just creating a bit of variation and finally the full one in here
[13:43] and we're just gonna do this and let's find and now I'm not sure these crystals will work well
[13:53] in here but we'll test it and then we're gonna do a scatter, adder shapes and now this should make
[14:01] a bit more sense like this to the stems let's do a layer properties and I'm just gonna change this to
[14:09] mono mono okay now let's see in here let's change this to height
[14:20] and this is a bit too much so we need to reduce it in the end so let's just do something let's go to
[14:26] the scatter shapes and this is where you want to play with your settings so I'm just gonna change this to
[14:33] 8 then I'm going to change the tile scale to pen scale variance so let's do variance and let's say
[14:44] point three eight one then we're going also to jitter so let's actually previewing here the
[14:53] color correction and decrease this quite a bit so right now it's not very visible why is that
[15:02] I'm gonna have to check in a bit so let's just do a jitter of 1.21 and we also will do angle
[15:12] variance but for now let's do in here let's set it to maximum now it's working a bit better we get
[15:20] this sort of result as you can see this is looking like a cliff face and we also want to play in
[15:27] near wheel let's see with the angle in this case I'm gonna change so where is that angle variance
[15:41] to 11.3 for example and then we're also going to yeah that's basically then we can play with
[15:49] the scatter seeds so maybe 39 let me get this sort of results so you can play with it
[15:59] let me see did I change something else I don't think so and maybe this is not easy to visualize so
[16:08] I'm gonna use ambient occlusion and yeah we get the clip shape and this this one that we are
[16:16] creating it will be just a mix it will be just an overlay for our blocks to have more detail in the end
[16:23] so we get this sort of result you can play with the seed get a different settings and play with
[16:28] the settings in here but that's basically the main effect and yeah let's continue on the next part
[16:38] okay guys so in order to have more variation we're going to duplicate these scatter shapes
[16:43] and I'm gonna play in here with the seed so I'm just gonna set it to 49 for example change the scale
[16:55] to 14 for example and 0.254 variation play with the jitter and then also the angle variance we
[17:08] can reduce it to something like this and what else we will just unlink the stamps and change
[17:18] this to 10 and 9 so we can stretch it a bit and I think we can also stretch a bit to shape so
[17:28] stretch a bit on the x and
[17:33] reduce the y to something like this so let's preview that actually so we get something like this
[17:44] and now we will blend them so the first thing we're going to do is to equalize to have in a fringe
[17:52] and we will equalize both then I'm gonna create a rectangle noise to the
[17:59] and let's see let me check because I use the 3d we're probably going to increase this to 0.25
[18:13] and decrease a bit the roughness so maybe something like this then we can do a directional work
[18:24] and let's play with these let's see let's increase the angle and play with the intensity
[18:40] and let me see if that really makes yes something like that and then we can finally blend these
[18:48] this one and this one and in this case we're going to set it again to minimum
[19:01] and we start to introduce some more details so this will be a bit too much so we can do a remap
[19:09] and just change the job put mix so we get something like this and let me see maybe this is a bit too much
[19:24] but anyways now what I want to do is to soften up these parts of the cliff and like x-threw them out
[19:36] and for that we will do an operation in a loop instead of duplicate nodes so let's create a feedback loop
[19:43] with a block and let's change this to this color and what we will need in here so we will need
[19:56] the incoming texture which is a mono we will need another mono that can be so we can keep track of
[20:04] the iterations another mono for a constant that we will use and that's basically it as for the
[20:12] outputs we just need texture and iterations so in this case mono need texture and we need to
[20:20] feedback also the iteration so we can keep track of it so let's this will make more sense when we start
[20:28] to create the two connect the nodes so as a constant so as the iteration we will start from zero of
[20:39] course so a value of zero and as the constant we will need a value of one to start with
[20:46] and now we will do non-uniform, non-uniform, directional work and we will distort the texture
[21:06] and we will also need to output as a mono so RGBA to mono I believe this is an issue with this
[21:11] node that only accepts the RGBA and we connect this to the texture and now we need also to
[21:23] to feedback the iteration so let's just add so it started zero and we will add so from the
[21:30] iteration we will add a constant of one and we can feed it back to the iteration so now if we look
[21:36] at the iteration we will start from zero one two three four and so on so you can see the value increases
[21:43] so let's look at the texture first and now
[21:46] we will use the constant as the intensity input and we will use
[22:08] as a wrap wrangle so first of all let me set this the intensity to 20 and we want to do this in all
[22:18] directions so what we can do is create a constant let's set it to 4 because that's the amount of
[22:26] iterations that we will set in years so let me see yeah and then we can just divide
[22:39] divide the current iteration by the number of iterations and use it as wrap wrangle input
[22:47] and let's see how that looks
[22:55] am I doing this properly so constant and let me see the constant in EO is 1 I want to add 1
[23:04] for the iteration and I want to divide this constant
[23:09] and let's just connect these solids connect these number of iterations so here
[23:22] so in each iteration we have a different value
[23:26] hmm this is not creating the effect I want so let me oh I need to do a trail length of one
[23:38] so it extrudes out so you can see the effect that is created so we go from this to this sort of
[23:45] effect and now let's actually preview so we can actually have a look in here so we go from this
[23:55] this shape and now if I connect in here you can see we start to create this extrude
[24:02] extrude effect which I think it looks a bit better then we can blur it a bit more in what not
[24:09] but then again we can also increase the amount of iterations so we get something like this
[24:16] so am I previewing ambient occlusion yeah let me see yeah maybe we can change this to
[24:23] three-point lighting maybe not that light that's fine all right I believe that's all for the
[24:33] cliff shape again this part in here this loop is you don't have to do it is just something I add
[24:41] at the end so feel free to skip it if you don't want to do it but anyway it's there so let's just
[24:48] create a node and let me see something yeah and again these tiles as you can see so we can just
[24:58] create in here out with let's give it a color and this is just our preview and the next part we
[25:08] will start to create the stems



---

## Captured Frames

- [0:20] tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/frame_000.jpg
- [2:20] tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/frame_001.jpg
- [7:50] tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/frame_002.jpg
- [13:20] tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/frame_003.jpg
- [16:10] tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/frame_004.jpg
- [24:20] tutorials/frames/creating-cliff-shapes-in-cops-free-lesson/frame_005.jpg

---

## Structured Notes

### Core Technique
Building a tileable, all-procedural cliff-face height/color texture entirely inside a **COPs (Copernicus) network** by layering noise, distortion warps, ramps, and a feedback loop — no 3D geometry, sculpting, or displacement painting involved.

### Summary
Starting from a `polygon`/regular-polygon COP shape (5-sided base), the tutorial builds up a rock-face pattern by blending an ISO-distance-inverted shape with a Cube 3D COP-constant, then repeatedly layering **tileable 2D noises** (never 3D noise, which wouldn't tile without mesh-based position/`P`/`uv` attributes) through **Multi-Directional Warp** and **Directional Warp** nodes to distort the base shape into irregular rock-like silhouettes. Ramps and Levels COPs reshape the tonal range into a "leaf"-like blended mass, ISO/Blend (min-darken) combinations merge multiple distorted variants, and a **Scatter Shapes** COP randomly places/rotates/scales the resulting shapes across a tile (with scale/jitter/angle variance) to build the final cliff-face look, previewed with Ambient Occlusion / 3-point lighting. A second pass duplicates the scatter setup with different seed/scale/jitter values for added variation, then both scatter layers are blended together via another noise-driven directional warp. Finally, an optional **feedback loop** (Block Begin/End COPs carrying texture + iteration count) repeatedly applies a non-uniform directional warp per iteration (intensity scaled by `iteration / total_iterations`, with Trail Length 1) to add an extruded/eroded look to parts of the cliff.

### Key Steps
1. Create a CopNet; start with a **Polygon** COP set to regular, 5 sides, as the base shape.
2. Add **ISO Distance** (inverted) off the polygon, then **Layer Properties** set to "Height" type to get a sloped gradient result.
3. Add a **Cube 3D** COP-constant node (pre-built rig: cube + transform + rasterize depth) and **Equalize** it against the ISO shape to normalize ranges (white point ~0.5), then **Blend** the two with Min-Darken.
4. Layer a **tileable 2D fractal noise** (not 3D — 3D noise won't tile without mesh position data) at a small scale (~0.02–0.08) through a **Multi-Directional Warp**, driven by the noise as intensity (~20–26), followed by an **RGB(A) to Mono** conversion (many COPs only accept RGBA).
5. Add further noise layers (a stretched/transformed noise, a Crystal noise at element size ~0.5) each piped through **Directional Warp** nodes with tuned intensity/angle values, plus a **Slope Blur** for additional softening — building up the distorted rock silhouette incrementally.
6. Use a **Ramp** COP (vertical, Levels-adjusted) blended (min) with the noise stack to reshape into a leaf/rock-like tonal mass; **Fetch** nodes reuse the same ramp/crystal noise elsewhere to avoid re-wiring duplicate nodes.
7. Combine 2-3 distorted shape variants (including a mirrored copy via **Transform** with flip) using **Pack** (Cop Pack) to bundle them for scattering.
8. Use **Scatter Shapes** to randomly instance/tile the packed shapes across the canvas — key parameters: scale variance (~0.38), jitter (~1.21), angle variance (tuned per pass, e.g. ~11.3), and seed — then preview with **Ambient Occlusion** or 3-point lighting to check the cliff-face read.
9. Duplicate the Scatter Shapes setup with a different seed/scale/jitter/stretch to build a second variation layer; blend the two scatter layers together via a Rectangle-noise-driven Directional Warp + min-blend + Remap.
10. (Optional) Build a **feedback loop**: Block Begin (outputs mono texture + iteration count, starting iteration=0, constant=1) → Non-Uniform Directional Warp (intensity driven by `iteration / total_iterations`, Trail Length = 1 to get an extrude effect) → RGBA-to-Mono → Block End (feeds texture + iteration+1 back to Begin) — set total iterations (e.g. 4) to control how many times the erosion/extrude warp is re-applied.

### Houdini Nodes / VEX / Settings
COPs used: Polygon (regular, 5 sides), ISO Distance (inverted), Layer Properties (Height type), Cube 3D (constant), Equalize, Blend (Min-Darken / Subtract variants), tileable 2D Noise / Fractal Noise, Multi-Directional Warp, Directional Warp (several instances), RGB(A) to Mono, Crystal Noise, Rectangle Noise, Transform (flip/mirror), Ramp (vertical, with Levels), Fetch (reuse existing nodes without rewiring), Cop Pack, Scatter Shapes (scale variance, jitter, angle variance, seed), Ambient Occlusion / 3-point lighting preview, Slope Blur, Remap, Block Begin/Block End (feedback loop with mono texture + iteration count constants), Add (iteration+1), Divide (iteration/total for normalized intensity). No VEX in this tutorial — pure node-graph COPs work.

### Difficulty
Intermediate — no VEX/scripting required, but demands a working knowledge of tileable-vs-3D noise behavior, COP RGBA/mono conversion quirks, and building custom feedback loops with Block Begin/End.

### Houdini Version
Not stated explicitly; UI matches Houdini 20.5/21-era Copernicus (COPs) context toolbar.

### Tags
#cops #procedural #texturing #noise #terrain #environment #intermediate

---

## Related Tutorials
Continuation of a multi-part cliff/rock-wall COPs series (references "last time" and "the next part we will start to create the stems") — cross-link with any other cgside COPs/procedural-texturing tutorials (e.g. rock wall, moss, materials-in-COPs) once extracted from this batch.
