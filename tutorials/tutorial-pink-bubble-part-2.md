---
title: [Tutorial] Pink Bubble. Part 2.
source: YouTube
url: https://www.youtube.com/watch?v=uztbmUElafA
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [rendering, octane, glass, dispersion, specular-material, instancing, lighting, beginner-intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-pink-bubble-part-2/
frame_count: 4
---

# [Tutorial] Pink Bubble. Part 2.

**Source:** [YouTube](https://www.youtube.com/watch?v=uztbmUElafA)
**Author:** Alexander Eskin
**Duration:** 10m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome back to our tutorial about making spheres inside spheres. Today we're gonna render. We're gonna do the rendering in octane because why not? To be honest I'm not a very experienced octane user so I'm gonna make some travel mistakes for all of you, octane all timers so bear with me. But I like the glass. I like how the glass looks in the octane and the refractions. So I'm gonna use octane. So first of all we're gonna move all these things into the orange context. We're not gonna render the source node. We're gonna color it green and leave it be. I'm gonna create bubble base. Bubbles. Big bubbles. Small. We're not gonna move them around or select them in the viewport so I'm gonna check the green one. I hate it. And color now it's red. Now we're gonna merge our geometry into these nodes with the object merge. Out sphere base. This is our base sphere. Nice. Orange. This is gonna be our spheres big. And this are going to be our sphere small. And that's it. Everything is merged. We'll create a camera. Create a null. Set the Z translation to 6 and select our camera. Okay. I don't think we need the 16 by 9 aspect. We're gonna use the square one. And we're gonna change the focal length from 50 to 100. With this out of the way we're gonna create our octane render in the out row. We're gonna create the octane red target in the matte context of the red target. This is the node where all of our render settings are gonna be stored. And octane material. We're gonna need two. Now three background. Bubble. Mine. For face. And small bubbles. Let's create background. It's gonna be our usual box. Big box. Reverse the normals. Blast. Blast. These two things. And also we're gonna leave these tools. And level the thing. Six. Round. Maybe eight. Anyway. That's not going to be noticeable. Number the cares. And set not but not. Okay. With this out of the way. I'm also gonna put the thing a bit close. So let's apply the shaders background to background. Base bubble. To bubble base. And these two small big bubbles should have these small bubbles shader. So everything is white in the viewport and it's making me blind. So I'm gonna decrease the values. For the open-geal preview it's not gonna affect the render just for the sake of not going blind. Okay. That's it. In the render target. We have to change the kernel to the path tracing. Change the environment to texture. Change the image or CIO. Asus. And honestly everything else is gonna work as is. Go to the output and create a clean light. This is gonna be our light big color it yellow. And turn it from quad to circle. Make it bigger. 15, 15, 15, 15 meters. Nice. So uncheck the keypins since power. And let's see the result. Okay. Looks terrible. Barely working. We need the first thing we need to do is to uncheck the camera visibility and general visibility in the light source in the octane light tab. Layer settings shader. Layer settings. Move a light a bit from the surface farther away from the surface. Set the transition to 5, white to 6. And this is something. We need to probably make the render look smaller because this is too much for my tiny screen. Now I'm gonna change the background shader a little bit. Reduce the specular weight. As for the bubble base we're gonna change the standard surface to the specular one. The material specular. There it is. And by default it looks okay. The problem now is that we don't have the tiny particles because they're not rendered as particles. They're not rendered at all. So the next step is to fix that. And the most straightforward way to do this is to just copy the spheres on top of it using the copy to points. No. Change the scale to 2. Polygon. Nice to polygon. And let's see how it looks. Now they are here in the scene. But there are two problems. They're not shaded and they're probably not gonna be shaded nicely. Specuary. So yeah. They don't really look like the bubbles inside the bubbles. In redshift you just use reverse the normals and be done with it. In octane it's a bit more complicated but reverse the normals works as well. So we're gonna stick with it for now. Reload. So now the reflections are better. They look like the proper bubbles or at least I think so. Also you can check the fake shadows because we don't have any shadows. And with fake shadows the rendering should be a bit faster. Now we can add some color to the big bubble in the transmission tab. Set it to pink. And set the value of saturation to 0.5. Of course this is not enough because we have to add dispersion. The best friend of the motion designer. Fashionable dispersion. Nice. Too much. Just a little bit. A little bit of dispersion. And that's it.

**Frame:** tutorials\frames\tutorial-pink-bubble-part-2\frame_000.jpg


---

## Structured Notes

### Core Technique
Octane render setup for pink bubble scene: Object Merge into OBJ-level geo nodes, Octane Specular material for glass bubbles, reversed normals on small sphere geo, reversed-normals box as background env, circle area light (uncheck camera/general vis), pink transmission + dispersion on big bubble.

### Summary
10m13s render tutorial by Alexander Eskin (Part 2 of Pink Bubble series). Sets up an Octane renderer for the bubble scene from Part 1. Uses Octane Specular material (glass-like). Small bubble spheres were just points — fix by Copy to Points of actual sphere geo (scale=2, polygon). Reverse normals on small spheres for correct reflections. Background: large reversed box (blast two open faces). Light: 15m circle area light, uncheck camera/general visibility in Octane. Pink transmission color on big bubble + small dispersion for rainbow effect.

### Key Steps
1. **OBJ context setup**: Create geo nodes: bubble_base (base sphere), bubbles_big (Vellum big bubbles), bubbles_small (small Vellum grains); Object Merge each from the simulation geo
2. **Camera**: Null at Z=6 → Camera parented; square aspect ratio (1:1 not 16:9); focal length=100
3. **Octane Render Target** (in render out context): path tracing kernel; environment=texture; image=Asus; rest default
4. **Background box**: large box → reverse normals → blast 2 bottom/open faces → bevel + subdivide; apply background Octane material
5. **Apply shaders**: background → box; bubble_base → base sphere; big/small → Octane Specular
6. **Light**: area light (circle shape), 15×15m; Octane tab → uncheck camera visibility + general visibility; transmission=5, power=6
7. **Small bubbles fix**: small bubble stream = just scattered points (no geometry) → Copy to Points: copy source sphere (scale=2, polygon type, higher freq) → apply Octane Specular material → **Reverse SOP** on source sphere → correct reflections
8. **Big bubble material**: Octane Specular → Transmission tab → color=pink, saturation=0.5; enable Dispersion (small value for subtle rainbow)
9. Fake shadows: enable in Octane material → faster renders without real shadow ray cost

### Houdini Nodes / VEX / Settings
- **Object Merge** — bring simulated geo into render OBJ-level nodes
- Camera: square aspect ratio; focal length=100; Z=6
- **Octane Render Target** — path tracing; environment=texture; image=Asus
- **Octane Specular material** — for glass/bubble look; transmission + dispersion controls
- **Reverse SOP** — flip normals on small bubble sphere geo for correct Octane reflections
- **Copy to Points** — copy sphere geo (polygon, scale=2) onto small bubble point cache
- Area light (circle, 15m) — Octane tab → uncheck camera/general visibility
- Transmission color=pink, saturation=0.5; Dispersion = small value for rainbow effect
- Fake shadows checkbox — speeds up Octane renders

### Difficulty
Beginner–Intermediate

### Houdini Version
H19

### Tags
[rendering, octane, glass, dispersion, specular-material, instancing, lighting, beginner-intermediate]

---

## Related Tutorials
- tutorial-pink-bubble-part-1.md (Vellum balloon + grains + ripple solver setup)
- tutorial-lipstick-part-3-rendering.md (Octane rendering setup by same author)
- tutorial-glass-tiles.md (Mantra glass/transparency rendering by same author)
