---
title: [Tutorial] Heavy Chic. Part 1.
source: YouTube
url: https://www.youtube.com/watch?v=fjVERoS2olY
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [particles, pop, height-field, volume, scatter, noise, logo-trace, animation, pscale, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-heavy-chic-part-1/
frame_count: 4
---

# [Tutorial] Heavy Chic. Part 1.

**Source:** [YouTube](https://www.youtube.com/watch?v=fjVERoS2olY)
**Author:** Alexander Eskin
**Duration:** 24m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So let's do some heavy particles chic. Start with the G now. Let's call it particles Sim color green. Start with a simple grid we'll fix it later on because everything is procedural you know, hoodie and stuff. Then scatter some points let's say 100,000 at a p-scale attribute. We'll gonna need it later on and add a pop network. Diving. Let this one we don't need it. An emission type just all points that's gonna mean that we're gonna meet from each point every frame. So the first frame will only have 100,000 and later frames are gonna have 1 million. No. We're gonna need only those points that exist in the frame one. So we're gonna exit by writing an expression f equals equals one. That means that if the frame equals one then the statement is true if it's two then it's zero because the number of the frame is two. Now we're gonna meet only on frame one. So say 100,000 or 100,000 points. Also fixed frame rate. 24 is for the movies we're doing it for the social media so it's 30. So Diving and at pop wind. Pop wind say wind velocity is six. Now every point is gonna fly upwards as expected. But what we need is for some unevenness in their behavior. We can do this by introducing noise like this. Find wolf, turbid noise, just a default one. And in the pop network we're gonna have to use a vex expression. We're gonna multiply velocity y by the color. There's a hint how this parameter is named and as you can see it's named wind y. But that's a trick. If you're gonna use wind y, we add cdx. It's gonna be error because he doesn't know what it is because we have to use wind point y. So like this is gonna work. So the velocity is gonna be multiplied by the color. So it's gonna be slower where the color is darker and faster when where the color is brighter. We awesome. They got this clock so it's gonna be real time. Something like this. I'm gonna need only 150 frames. So I'm gonna reduce the timeline. Amazing. So this sort of works but there's a problem. If we try to animate it, animate this stuff. Say animate source mean. The top network we're gonna only see the first frame. Like tada tada. And say frame 30. Do the usual stuff. If we go here nothing happens. That's why nothing happens. I have no idea. But the first frame of the animation just that's the rules. So we can do the same stuff just inside the dub. Say subs over. There's a note for it. Where we can do the same stuff. Just point of up. Add a point of up node. Dive in. Introduce two balls. Nice. Add a fit. Promote. Enemate. Enemate. Add not put. Not really needed but just for the sacred. And now behold. It's too fast. Okay. Say 60 and let's do it in linear fashion. Okay. So something happens. And it happens the way we intend it. Which is good. Okay. It's diving and making more complex. I'm gonna need two noise. One's gonna be for the lifting. And the other is gonna be for animating. So let's start with the lifting one. So this one is gonna be static. Says like reference one. So it's gonna point. It's gonna be lifted only in the white areas. And the gray ones. Like this. And so if noise one look is bad, we're gonna add another noise. Like this. So it will look more complex. So the parameters are default here and I reduce turbulence. But maybe it's okay. And I have increased frequency of it. 1.7. Okay. So this is the basic noise. Now we need a radial one that's gonna drag the animation. Let's make it length. And fit. Flip this, these ones. And promote those two. So what we're gonna do is to clean this up a bit. We don't need this. We don't need that. But we need a folder to look more sophisticated while it's released. So it's gonna be called spread animation. Spread animation. Yes. Also had not followed. It's gonna be named spread width. And spread width gonna be equals equals spread width equals something like 1.5. So this is gonna be our animation. And maximum value. Copy parameter, paste relative reference. And minus spread width. So spread width is new parameter. Now I'll fix this. Maximum value 5. For 6. So we're gonna animate it like this. Don't really see it. But so the spread width is the distance between the widest point and the blackest point. So it's like the gradient where the gradient really works. Mm-hmm. Like this. I'm gonna animate it. That's gonna be zero. The final point of animation is gonna be 5. Also like to noise this one as well. Not the V, the P. So it has rough edges. Just cool. That's a rough. Like this. Hmm. Not bad, not bad. So this is gonna drive our animation. To make it work, we're gonna just multiply this by this. So now it's gonna work like this. So we see the spread and then the noise takes advantage of particles. Don't really see how much was going on. Let me fix that. So we'll have this animation. I'm going to delete everything except for the the scale and it. The read notes. Okay. Not really cool. So we can use the cool thingy the same that well muses when you create well grains. Just a detail attribute. Let's call GL's fear points. Let's call it preview. So as you can see, it lines a little spheres and they work pretty fast. Amazing. So now what I wanted to do, I want to make the source plain more complex or complex. For this I'm gonna use height field. Size is the same. 5, 25, 9.5. Great spacing is 0025. Then we're gonna use height field noise. I'm gonna use amplitude 3, element size 3. No secondary noise. Just the basic one. Scale 1.1 and 0.7, 0.6, 0.4. Okay. Then I'm gonna use the trick with a stole from Sergei from Bizarre Cell Production. YouTube channel. I'm gonna leave a link in the description. So basically what we're doing is we're creating a volume. And for it to work with height fields, we're gonna use different bindings. So we're gonna primitive as name height and the vex is name density. So basically we're binding density to height, which is cool. Gonna call it sand dues, which they are. Okay. So the trick is to use the raised noise. So position. So. Amazing. No. So we don't need a noise here. We need to add to current density. The values of this noise. So yeah. There's our base geometry, base height field. And we're gonna fix this amplitude by multiplying constant. 0, 0, 5. But the direction is wrong. So we're gonna fix that. I use this value of 0.4 minus 0.4 and 1 to the cool. But we're gonna need to reintroduce the noise into the bit. This noise kind of cool, but not really. So we're gonna use a turbulent noise. Position. Add to position. Basic stuff. The frequency should be 0.721. And this should be a bit lower. Like this. And. I'm gonna test it out. It's a good height field. It's really low res. Uh, whatever. Scatter points. And it works on height field. Cool. Okay. Now we have to use some sort of cool looking logo. So just use a trace. I've done a lot of it some logo beforehand. I'm gonna use it. Uh, my logo is on the transparency. So I'm using the alpha channel. Don't trace it. Tons of useless points. There's a filter for it. Re-sample shape. Eight. Now it looks a bit better. Whole. So we'll reintroduce holes here. Yeah, let's go. Transform. Minus 90. 2.4. Uh, reverse. Then we're gonna extrude it. And then transform it. So it will be inside our height field. Like this. Then we're gonna use the height field mask to project the height field mask from object. Now how mask looks terrible. So we have to up the resolution. To do. Yeah. Cool. I'll just blur it a bit. teeny tiny. Maybe like this. And now a bit. Chicky stuff. I used height field layer. So why would extrude this height field by this mask? I don't know. Maybe there are simpler solutions, but I didn't know about those. Height field layer. And height will transform. So basically I'm transforming this height field by minus 0.5. Taking this source value. And just layering them by mask. Okay. So it looks like this. Now what we can do. We can use the same kind of height field. It's gonna be super slow. I have to reduce the acidity to 0.25. Yeah. So the difference now is that we have a logo. It's gonna help us later on. Fix the mask a bit. And I want to scatter points in volume. So if I just use this scatter later on, not gonna be looking good. Need like a layered type of scatter. That can be achieved with points from volume. But we need a volume first. There's a neat feature extrude by volume. So basically what we're doing is extruding our volume, which is which height field is basically a volume. 0.015. And third and base. Uncheck this one. We're doing it in a third base. And then we're gonna use points from volume. Points from volume. We didn't really see it, but we really have only 700 points. Okay. Reduce this one to 0.1. Okay, at least 700,000 points. But they're very linear. We just don't need this. Just cheat your scale. Set it to 1. Ah, now it looks like sand. What we can do further on, we can just place it here in our port network. Oh, I forgot to check the scale later. Okay, now there's more. So now it's how it works. Oh, amazing. Oh, let's have to do is to render it.

**Frame:** tutorials\frames\tutorial-heavy-chic-part-1\frame_000.jpg


---

## Structured Notes

### Core Technique
Heavy particle simulation on a height field: 100K scattered points emit only on frame 1 (`$F==1`); Pop Wind lifted by noise-controlled color; expanding radial animation wave (length+fit spread mask) drives lift; height field with Logo Trace cutout masks the particle distribution; Points from Volume on extruded height field gives layered density. Part 1 covers setup and geo; Part 2 is presumably rendering.

### Summary
24m4s tutorial by Alexander Eskin. Builds a "heavy chic" particle sand/logo effect. Workflow: scatter points on a height field, emit only frame 1, drive upward pop wind velocity by noise (turbulence via `windpointy *= Cd.x`), animate an expanding wave mask (length + fit) to control when/where particles rise. Complex height field: Height Field Noise + VOP binding trick (height→density) + turbulence VOP. Logo: Trace PNG alpha → Resample → Extrude → Height Field Mask from Object → Height Field Layer composites logo shape into terrain. Points from Volume on extruded HF volume gives 3D-distributed particle source (700K pts). Sphere preview via detail attribute for fast viewport.

### Key Steps

**1. Basic Particle Setup**
- Grid (fix later — procedural) → **Scatter** 100,000 pts → add `pscale` attribute
- **Pop Network**: Pop Source → emission type = "all points"; expression `$F==1` → emit only on frame 1 (prevents particle count explosion each frame)
- Fix timeline to 30 FPS; reduce to 150 frames

**2. Pop Wind + Noise-Driven Velocity**
- **Pop Wind**: wind velocity Y = 6 (upward)
- Add **Turb Noise** to grid (colors points by noise pattern)
- In Pop Wind VEX expression field: `windpointy *= cdx;` — Note: must use `windpointy` not `windy` (includes "point" in the parameter name)
- Darker noise → slower lift; brighter → faster lift

**3. Animated Wave Driving**
- Two noise nodes: noise1 (static, for lift areas), noise2 (layered, higher frequency=1.7 for complexity)
- Radial animation: compute `length(P.xz)` → `fit(len, center, center+spread_width, 1, 0)` to create expanding gradient wave; promote spread_width, animate center 0→5 over 150 frames
- Noise P before fit for rough edges
- Multiply static noise by radial wave → final animation mask
- DOP animation: use **Subs Over** node + **Point VOP** inside DOP to animate grid position (source animation doesn't work from POP Source frame 1 rule — must animate inside DOP)

**4. Fast Viewport Preview**
- Set detail attribute `preview` → enables small sphere display in viewport (same trick as Vellum grain preview)

**5. Height Field Setup**
- **Height Field** SOP: size=5×25×9.5, spacing=0.0025
- **Height Field Noise**: amplitude=3, element size=3, secondary=off, scale=(1.1, 0.7, 0.6, 0.4)
- **VOP trick** (credit: Sergei, Bizarre Cell Production): in Volume VOP — bind primitive attribute name="height", VEX name="density" → height field height drives volume density
- **Turb Noise VOP**: add turbulence to density; frequency=0.721; multiply by 0.005; direction vector (0, −0.4, 1)

**6. Logo Integration**
- **Trace SOP** on logo PNG → use alpha channel; **Resample** (step=8) → Transform (−90°, scale=2.4) → Reverse → **Extrude** → position inside height field bounds
- **Height Field Mask from Object**: increase resolution → **Blur** slightly → creates smooth logo mask
- **Height Field Layer** + **Height Field Transform** (offset=−0.5) → composites logo into terrain (lowers terrain where logo is)
- Reduce particle density to 0.25 where logo is for visual distinction

**7. Points from Volume**
- **Height Field to Volume** (extrude by 0.015, "third base" mode)
- **Points from Volume**: density=0.1 → ~700,000 pts; set pscale=1 for natural-looking sand density
- Feed into Pop Network in place of flat scatter

### Houdini Nodes / VEX / Settings
- **Scatter SOP** + `pscale` attribute (manual add)
- **Pop Source**: emission "all points", `$F==1` condition
- **Pop Wind**: `windpointy *= cdx;` (multiply Y velocity by noise color; note "windpointy" not "windy")
- `length(P.xz)` → `fit(len, 0, spread_width, 1, 0)` — expanding radial wave animation mask
- **Subs Over** (DOP) + **Point VOP** inside DOP — for animating source geometry position inside simulation
- Detail attribute `preview` — enables sphere preview for particles in viewport
- **Height Field SOP** — size, spacing parameters
- **Height Field Noise** — amplitude, element size, scale per-octave
- **Volume VOP** — bind `height` primitive → `density` VEX name trick (Sergei/Bizarre Cell Production)
- **Trace SOP** — traces image alpha/color to curves
- **Height Field Mask from Object** — projects SOP geometry as mask onto height field
- **Height Field Layer** — composite masks/layers
- **Height Field Transform** — offset height by value in masked region
- **Height Field to Volume** / **Extrude Volume** — convert height field to 3D volume
- **Points from Volume** — scatter in 3D volume; density=0.1 for ~700K pts; pscale=1

### Difficulty
Intermediate

### Houdini Version
H19

### Tags
[particles, pop, height-field, volume, scatter, noise, logo-trace, animation, pscale, intermediate]

---

## Related Tutorials
- tutorial-heavy-chic-part-2.md (rendering this particle setup)
- rain-effect-in-houdini-houdini-tutorial.md (POP basics for comparison)
- introduction-to-particles-in-houdini-21-full-beginner-course-2026.md (comprehensive POP reference)
