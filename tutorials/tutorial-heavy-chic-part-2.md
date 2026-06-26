---
title: [Tutorial] Heavy Chic. Part 2.
source: YouTube
url: https://www.youtube.com/watch?v=mOKs6Dht5Mw
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [particles, rendering, mantra, instancing, gold-material, file-cache, fracture, pscale, depth-of-field, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-heavy-chic-part-2/
frame_count: 4
---

# [Tutorial] Heavy Chic. Part 2.

**Source:** [YouTube](https://www.youtube.com/watch?v=mOKs6Dht5Mw)
**Author:** Alexander Eskin
**Duration:** 17m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, we need to fix a few things before starting the render. First of all, we need to add noise, amplitude 0.5, soil size 0.4, and use of expression. We should multiply amps. By our CD color, this way the particles that want move won't be affected by the noise. Otherwise, they have just float away like this. Like little worms. Now we don't need that. We'll do this. Everything looks great. Also, we need to fix the gamma a bit. We'll fix it by introducing a ramp here. It's going to be a nice, sharp ramp. Let's apply the ramp. And for the preview purposes, I'll apply it into CD. Just don't forget to plug it back. The ramp should be from 0 to 1. And it's going to be, we should add the third point, value 0.15. Select all the three of the points and tell them to be interpolated as the peace-pline. Also move this a bit. Like this. Okay. Don't forget to plug it back. Preview. Okay. Looks pretty good. Now we should increase the particle count. And the point separation decrease the point separation from 0.01 to 0.004. That should increase our point count from 700,000 points to 11 million. Now use the file cache. Name it part equals sim. Don't need it here. Move it there. Did it everything. Also did groups. All of them file path explicit. This is dollar s and dollar four. The dollar s means that the name is going to be derived from the sub name. So here is blah blah blah, our path to the hip file, then jute, then particle sim, particle sim, 0, 0, 0, 1. We can press the middle mouse button to see the full path. So here it is. Okay. Sim. Okay. So it worked. Just fine. Now we should clean this up. Now reduce the scale a bit. Now we can see a little bit. P scale equals scale. That means that we will make a parameter. It's going to multiply the existing P scale by the number here. 2.4. Okay. More like it. Okay. Now we need to create the particle itself because if we're going to use the sphere one, it's going to look at trotters. So do you know the particle geosource? Let's say dark gray box. I's offset scatter. 45 points. I'm going to fracture. I'll have the fractured box. Back it. Back all the pieces. Peace by piece. And group the external pieces, group type points named Blaster. Bounding regions. So is 0.5. Now Blast. Blaster and Aspect. Now I have this clump. Now Shared. Shared. And we'll use connectivity attribute. And select only one piece that we need. Class equals zero. Now select it. Group type should be set to points. Now we're going to select the one piece that we like the most. It doesn't really matter. I like this one. Set the match size. Create the reference box and scale it accordingly to the box. Now it's going to be in the same scale that's our preview sphere. And create another node. Name it particle zero zero. Just in case we're going to need more particles. We won't. But if you want. Now also we need to apply material here in the material context. Create material. Let's shift material builder. Name it gold. And apply it here. Gold. Also impact it. Yeah, like this. Forget about that. And create another node. Call it particle zero zero. And use we can use this one as our instance. And mine the scale. It's going to be multiplied by the p scale of this particles. Now we're going to create the instance node. We're shifting instances. Select the instance object of the node. It's going to be particle zero zero. And in the instance node itself, we're going to import our points from the particle scene. Let's go and render it. We're the light source and the camera. Now we're going to use a node. That way it's more convenient to animate it later on. We're going to fix the resolution to 1080, 90, 90, focal length 200, 6.3, and C axis. And here we're going to move it to the 0.9151143. And rotate it a bit. I'll start to do 35. Go ahead and shoot here 10. And we need to create a light source. Light source would be a simple white. We call it light 10. Make it yellow, make it fun. We get less explosive and change its type from area to distant. We're going to render the default settings. Let's try to render it. So it works. We need to rotate the light source. We'll increase the intensity, fix the shader, make it more metal like reduce the roughness, introduce color. Just eyeball it. The problem right now is that all the particles are rotated at the same angle. So it looks very dull. To make it more magical we should introduce random rotation. We're going to use the first dimension parameters for all. Now let's look at the render. The field really helps. Put the focal points somewhere here. Maybe tweak the shader a bit. To pin. Maybe we should increase the light intensity. Let's see how it looks from the top. Now we're going to use the different render mode for the convenience sake. We're going to use the shot 20. We're going to use the light. We can't edit the light. Let's shot 10. I need to fix the black gaps. I fixed it in a chip way. Out, plane, material. One, sub to you. One, sub to you. Let's see how it looks right now. Much better. I forgot to do that. Nope. The shot 0.10 looks like this right now. I think that's it.

**Frame:** tutorials\frames\tutorial-heavy-chic-part-2\frame_000.jpg


---

## Structured Notes

### Core Technique
Polish and render the Part 1 heavy particle sim: noise multiplied by color (stationary particles untouched), gamma ramp, upres to 11M points, File Cache, custom fractured-box particle geometry instanced with pscale, gold material (metallic, rough, yellow), Instance node render, distant light, random rotation per particle, DOF camera, fix black gaps with opacity subdivisions.

### Summary
17m52s tutorial by Alexander Eskin (continuation of Heavy Chic Part 1). Polishes the particle simulation: adds noise multiplied by Cd (so stationary particles don't drift), applies a b-spline gamma ramp to redistribute particle density, increases point count from 700K to 11M (point separation 0.004). Caches to disk with `$OS.$F4.bgeo.sc`. Creates custom particle geometry: fractures a box, packs pieces, blasts external shell, picks one interesting piece by connectivity class. Instances these geo pieces using the Instance OBJ node driven by pscale. Gold material (metallic, low roughness, yellow tint). Camera: 1080p, 200mm lens, C-axis mode, DOF. Distant light (yellow). Random rotation via first-dimension random. Fixes black gaps with opacity subdivision=1.

### Key Steps

**1. Noise Fix (Stationary Particles)**
- Pop Noise: amplitude=0.5, size=0.4
- VEX: `force *= Cd.x` — particles with dark color (stationary) aren't perturbed; bright particles still get noise variation

**2. Gamma Ramp on Cd**
- Add ramp to Cd → 3 points at 0, 0.15, 1 → set all to B-spline interpolation → shifts density distribution
- Apply to `Cd`, then reconnect into correct pipeline spot

**3. Upres + File Cache**
- Reduce point separation in Points from Volume: 0.01 → 0.004 → 700K → 11 million points
- **File Cache SOP**: name = `particle_sim`; use `$OS` for sub-name derive; explicit file path = `<hip>/geo/particle_sim/particle_sim.$F4.bgeo.sc`
- Middle-mouse on File Cache node to verify full path

**4. Custom Particle Geometry**
- Box → **Scatter** 45 points → **Fracture SOP** (Voronoi) → **Pack** all pieces
- **Group SOP** (bounding region, size=0.5) → groups external face points as "Blaster"
- **Blast**: keep only "Blaster" → **Unpack** → **Connectivity** (class attribute) → select `class == 0` (one piece) → Group (points mode)
- **Match Size** to reference box (so it matches particle pscale)
- Object name: `particle_00`

**5. Gold Material**
- Material Builder: Standard Surface → metallic=1, roughness=low (shiny), base color=yellow
- Apply to particle_00 geometry

**6. Instancing**
- **Instance OBJ node**: point to `particle_00` as instance geometry
- Import cached particle points as Instance node's point source
- Particle pscale multiplies instance scale automatically

**7. Camera + Light**
- Camera: 1080p resolution, focal length=200, C-axis mode; position and rotate in viewport
- Light: type=Distant (not Area), color=white→yellow, increase intensity
- Apply DOF: set focus point in camera, tweak aperture

**8. Random Rotation**
- Add random rotation to particles in wrangle/attribute before instancing: first-dimension based random on orient or rot attribute → prevents all particles looking identical (same angle)

**9. Fix Black Gaps**
- In Mantra render settings or material: opacity → set subdivisions = 1 → removes dark gaps between instanced pieces at render

### Houdini Nodes / VEX / Settings
- **Pop Noise**: amplitude=0.5, size=0.4; VEX: `force *= Cd.x;`
- B-spline ramp on `Cd` — 3 control points (0, 0.15, 1) for gamma correction
- **Points from Volume**: point separation 0.004 → ~11M pts
- **File Cache SOP**: `$OS` for sub-name; explicit path with `$F4` frame padding
- **Fracture SOP** (Voronoi) → **Pack** → **Group** bounding region → **Blast** → **Connectivity** class attribute → select one piece
- **Match Size SOP** — match particle geo to reference bounding box
- **Instance OBJ node** — render particles as instanced geo; reads `pscale` automatically
- **Standard Surface material** — metallic, low roughness, yellow base color
- Camera: focal length=200, C-axis, DOF
- Distant light (yellow), intensity adjusted
- Random rotation wrangle — `@orient = …` or `rot` attribute to randomize per-particle angle
- Mantra opacity subdivisions = 1 → fixes black gap artifacts

### Difficulty
Intermediate

### Houdini Version
H19

### Tags
[particles, rendering, mantra, instancing, gold-material, file-cache, fracture, pscale, depth-of-field, intermediate]

---

## Related Tutorials
- tutorial-heavy-chic-part-1.md (sim setup: height field, pop network, wave animation)
- tutorial-glass-donut.md (Mantra render tricks by same author)
- tutorial-glass-tiles.md (material building by same author)
