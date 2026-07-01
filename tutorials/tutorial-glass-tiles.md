---
title: [Tutorial] Glass Tiles
source: YouTube
url: https://www.youtube.com/watch?v=Ps6ZOKEdDos
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [glass, tiles, animation, orient, quaternion, attribute-transfer, pop, trails, material, blend-material, rendering, mantra, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-glass-tiles/
frame_count: 4
---

# [Tutorial] Glass Tiles

**Source:** [YouTube](https://www.youtube.com/watch?v=Ps6ZOKEdDos)
**Author:** Alexander Eskin
**Duration:** 25m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's start with the Juno. Ju... tiles... source... green. Let's make a tile. It's going to be made from a box. Box... of 0.1, 0.5. And that's it. We're going to color the other side, so it would be easier to determine which side this tile is facing. So the fifth primitive should be red. And now it is. Let's make it more complicated than just a box for the extrude. By extruding it, primitive number 5, number 4 should be extruded by a bit. And inserted by a fair bit. And we should probably check for it. Or a battle. Because we're going to render it and they're going to be glassy or whatever. The refractions will look much, much better. On the battle shapes and subdivided ones. They should be held by a small amount. In the crease mode, two divisions. Like this and subdivided. It's going to look like this. And I'm happy with it. Now... Oh, tiles. So we made a singular tile. Now we should make some points. To copy those tiles to size 10 and height is 2.5. Oh, the X is different. YZ. We didn't need any polygons. We need only points 128, 128. So, copy the points. Copy the points. Don't forget to check the back end instance. And they copied, but they're huge. We need to scale them down. Scale. Just create the P scale attribute. And just scale them down. Select this. Now have a wall. White and red. Oh, good. This is how it was supposed to be. Now we need to create an attribute. It's going to drive the animation. And we're going to drive the animation via attribute transfer. So, the attribute should be called rather. Diffle 0, value 0. This one is going to be value of 1. And the driving thing is going to be just a grid. The grid of a huge size. The bit of a rotation. And a different axis, of course. So, this is the grid. This is our grid. It's going to drive the animation. It needs a bit of a points to it. Otherwise, they won't transfer properly. So, right now we don't see anything because we don't have the visualizer. We can create one by pressing Ctrl, we don't have the mouse button and pressing the left mouse button on the attribute. Now we have one. But it's the colors are pretty ugly. And also, the descent threshold was huge, so we couldn't see anything. I want to fix the colors to lack the orange. I want to add some noise to the fourth. So, we can use mountain. And the mountain is going to work on all the axis except for the X1. We don't have any vectors. Check the noise along the vector checkbox. This is now noise, but we need to return the attribute to the unnoise points before the displacement. So, we just use the attribute copy. And we're going to take these points and displace ones with the attribute. And copy the displaced attribute to the previous undisplaced points. And it's going to look like this. Pretty cool. We also can animate it with the transferring node. The attribute is transferred. The attribute copy of working. Now we need to animate it just like pre-animation. Just to see how it looks. Duh. Blapse. Layer 1. 96 frames. Just with the preview purposes. And now it grows. Everything looks great. Now we need to make them rotate because nothing is happening right now. For the rotation purposes, we're going to use the orient. And it's going to be painful to believe me. So, orient. Orient goes as follows. P orient equals q multiply. P orient. Rotate the attribute that we're going to use for rotation. Rotate the tiles. Rotate the tiles. This is impossible to understand. We have to memorize it. Seriously. Just copy it somewhere. Basically, we're using the orient to... We're rotating orient using this thingy. This attribute with this amount of degrees by this axis. So, you can change the axis here. For example. And now they're rotating in the x axis, which is weird. Okay, eager one. Eager is funnier. But we need a z axis. So, stick to it. The cool thing is that we can bend the orient and nothing will be broken. And we're going to use this. Pressing the B button on the keyboard. And we found the direction. The desired one. I like this part. So, we can create camera now. New camera. Create here and now. Now, move these things around a bit. And create another geo node. But we're going to get render tiles. Import these tiles here. Unscrew the orange tiles. Okay, don't forget to change the instant type to instance where you can compatible jix and instance sub-level back primitives. It will work if you want to change it, but the loading times before the rendering will be much higher. Now we need a background. The background will be just the grid. 5x5 with the xy plane. And hit in the floor. And that's it. Maybe we should move it around a bit. One light should be okay. For our purposes. Light. I didn't like the shape. It doesn't matter. Won't change the outcome. So, the shape disk size 0.5 spread. 0.5 and over here. Make a shortcut. Control-1. Cut the material. Create a red-shot material. We need three. The first one. It's going to be tiles. Second one. It's going to be trails. The third one is going to be back. And let's make a shortcut. Go to output. Create a red-shot. Red-node. Short-cut. Control-3. Half of the resolution. Pressing just 1, 2, 3. We can jump around quickly. There's a resolution. 90, 20, 20, 20. So, something came up. Which is good. Let's not forget to add the materials to the tiles. And to the background. Now we're all set. Let's make the tiles a bit brighter. And we'll loss here. Go back. Change our light source to a more greenish, blueish tint. And decrease intensity. And also we can check the lives of level of dates. That means when we're going to scroll the timeline, the rotation will be updated. And we're going to heal the beautiful stuff that's going on. Back to our tiles shader. Let's go with tiles. It's going to be our default state. Let's just a second down to check the light. Maybe if we decrease the spread, yeah, looks better. Tiles shader. This looks serviceable. I'm not going to change anything here. Just create a blend material. The first one is going to be tiles. The second one is standard emissive tiles. Just make an animation. So we will determine when the material is properly connected. And the third one is going to be just glass. Just glass is 100% transmission. And very rough. Not very rough. A bit rough. Maybe not. Okay, anyway. Layer color. This is correct. Yeah, this shouldn't work because there's no attribute to blend it with. So we have one. Rotor. And we're going to use this for blending. And don't forget to like it in. We could use a ramp to make a sort of wave. So there's going to be a front of the wave. And the back of the wave. Like this. And the whole emission thing should be as extreme as it is right now. Also we need a color. Color-dram. We're going to use the same attribute. But it's going to be green. And then blue. About any white. We're going to plug it into the emissive color. Just need to find it. First emission. Promote. Here it is. Now it's colored. Bitland. So we just use a transmission. Don't really see the beauty behind it. So we're going to use the funnel to make it look better. We're going to plug our ramp into the perpendicular color. Again. And then here. Now it's to subtle. No, it's something. By 25 maybe. Oops. Maybe like so. Anyway, now we need the glass shader to work. We need another ramp. We have the same attribute, but in different fashion. So when the glowing part stops, we're just going to transform everything to the transparent shader. Which is this. I've never seen anything behind it less. So it looks black. This is why we need to add trails. And we're going to create ones. Trails. I have the source when I use the grid. XY plane. I'm going to rotate it. It doesn't really matter. Just. I like it this way. 5 to 0.5. 3. It doesn't really matter what looks neat. Minus 90. Press B a couple of times. Now it's rotated to the desirable angle or axis. And we should move the source grid a bit like this. Now we have a proper source. Drop a pop network node. Now there are some points being sourced. Also we need to move it a bit farther away. Also we need to move it a bit farther away. Like here. Okay. The points are being scattered. And my viewport is being bugged. Okay. Too much for points. I think if I will be enough. Yep. So we're going to add a velocity here. Just. 5, 4, 2. Variants should be 0. Otherwise they're going to fly everywhere. We don't need this. Very nearly the speed variance. True. They're flying but the life expectancy should be 7 seconds with the variance of 2 seconds. We'll do it some unused attributes. I'm going to need ID. And that's it basically. We don't need a velocity or anything. Editorial node. 20 points. Add a time shift before that. Just add some 500 frames for example. Age life doesn't really matter here. Let's add some primitives using the ID attribute that we made beforehand. The top network made the action. ID. Now we have lines. Now we have to color them. CD equals Ctreme. And ID. Load alpha equals Ctreme. And we need the curve view attribute that we haven't made yet. What we will. Yeah. We got a bracket. I'm going to change the color from float to vector. And we have to add curve attributes without the sampling. 0. The color should be green. Blue. And red. And these two should be constant like this. The alpha is facing the wrong direction. Now we have some trails. Awesome. Okay. So everything sort of works. We can make the alpha channel a bit fancier. But it doesn't really matter. Anyway. Let's make another June node. And we have to add trails. And we are going to use trailsource. No, trail source out. And we are going to render them as strands. So we are going to type 0 to subdivisions. We don't need to subdivide them. And we are going to also need our material trails that we haven't set up yet. Let's go to the matte context. So we don't need this. We can use the incandescent material. The two attributes attached. And alpha. Right. Call it the color alpha to alpha. Intensity set to 4. For example. Now let's see. Lamb. Nice. So something's happening. We have the reflection. We have the refraction. Everything looks neat. Perhaps we can reduce the width of the trail without any advanced tricks. Just like this. So that's it.

**Frame:** tutorials\frames\tutorial-glass-tiles\frame_000.jpg


---

## Structured Notes

### Core Technique
Glass tile wall animation: bevel+subdivide box tile → Copy to Points on a grid wall → "rotor" float attribute driven by Attribute Transfer from a noisy grid → animate orient rotation with `qmultiply` quaternion per-frame → Blend Material (tiles → emissive → glass) driven by the same rotor ramp; particle Trail SOP rendered as strands with incandescent shader for sparkle effect.

### Summary
25m6s tutorial by Alexander Eskin. Builds an animated glass tile wall that flips from opaque tiles to glowing emissive to transparent glass in a wave. Tile: Box + PolyExtrude + Bevel + Subdivide. Wall: Copy to Points on grid (128×128 pts, P_scale control). "Rotor" attribute driven by Attribute Transfer from a Mountain-noised grid (undisplaced transfer + Attribute Copy trick). Orient rotated each frame via `@orient = qmultiply(@orient, quaternion(radians(amount), axis))`. Blend Material uses rotor+ramp for three-phase wave (tiles → emissive + color → glass), Fresnel ramp for highlight. POP trail particles rendered as Mantra strands with incandescent material, curve-u-based alpha.

### Key Steps

**1. Model the Tile**
- Box 0.1 × 0.5; color primitive 5 red (reference side)
- PolyExtrude prim 4 by small amount; inset by fair amount
- **Bevel** (critical for glass refraction to look good) → **Subdivide** (crease mode, 2 divisions)

**2. Build the Wall**
- Grid 10×2.5, XY, 128×128 rows/cols, points only (no polygons needed)
- **Copy to Points** (check "pack and instance" for performance) → tiles are huge
- Add `pscale` attribute to scale them down

**3. Animation Attribute "Rotor"**
- Add attribute `rotor` = 0 on tile wall points; set to 1 as target
- Driving grid: large grid with some rotation, different axis
- **Mountain SOP** on grid (noise along vector only; X axis excluded to keep flat)
- **Attribute Transfer** from noised grid → copies displaced position
- **Attribute Copy**: takes undisplaced points + displaced points → copies "rotor" attribute back to original (clean points, noisy attribute)
- Animate **Attribute Transfer** node's time over timeline for wave motion

**4. Orient Rotation**
- In Attribute Wrangle (runs each frame):
  `@orient = qmultiply(@orient, quaternion(radians(chramp("amount", @rotor)), {0,0,1}));`
- Change axis vector to change rotation axis; B key to bend/view orientation
- Rotor attribute controls how much each tile has rotated (0→full rotation)

**5. Render Setup**
- New geo node for render: import tiles, set instance type = "instance or compatible" (not "packed") for faster load
- Background: Grid 5×5 XY, "floor" shader
- Light: disk shape, size=0.5, spread=0.5

**6. Materials**
Three materials: tiles (opaque), trails (strand), background
- **Blend Material** for tiles:
  - Input 1: tiles shader (opaque)
  - Input 2: Standard Surface emissive → color via `chramp("color", @rotor)` (green→blue→white) plugged into emission color; Fresnel ramp plugged into perpendicular color for edge highlight
  - Input 3: glass (100% transmission, slight roughness)
  - Blend driven by `@rotor` attribute + ramp (wave front: tiles → emissive; wave back → glass)

**7. Trails (POP + Trail)**
- Source grid: XY plane, rotated, offset slightly; 5×0.5 scale
- **POP Network**: ~10 points emitted; velocity = `{5, 4, 2}` with 0 variance; life = 7s ± 2s
- Add `id` attribute (keep); delete velocity + unused attributes
- Trail SOP: 20 points trailing; add Time Shift (+500 frames offset for pre-roll)
- Color: `@Cd = chramp("color", @id)` (float to vector → color ramp: green, blue, red)
- Alpha: `@Alpha = chramp("alpha", @curve-u)` (direction reversed so head is bright)
- Curve View attribute (0→1) needed for curve-u
- Render as Mantra strands: type=0 subdivisions; trail width controlled directly
- **Trails material**: Incandescent (emissive); `Cd` → color, `Alpha` → alpha; intensity=4

### Houdini Nodes / VEX / Settings
- **PolyExtrude** — inset + extrude tile face
- **Bevel** — smooth edges for glass refraction
- **Subdivide** — crease mode, 2 divisions
- **Copy to Points** — instance/pack mode for performance; `pscale` attribute for size
- **Mountain SOP** — noise driven along vector (X excluded); animatable
- **Attribute Transfer** — animated to drive wave motion; transfers `rotor` value from noised grid
- **Attribute Copy** — copies attribute from displaced to undisplaced points (attribute-only transfer)
- `@orient = qmultiply(@orient, quaternion(radians(ch("amount")), axis))` — per-frame orient rotation; `chramp` for amount-per-tile
- **Blend Material** — 3-way blend (tiles → emissive → glass) driven by `@rotor` + ramp
- `chramp("color", @rotor)` / `chramp("alpha", @curve-u)` — ramp color/alpha lookups
- **POP Network** — source + solver; velocity, life, id attribute
- **Trail SOP** — N=20, Time Shift offset for pre-roll
- **Mantra incandescent material** — strand rendering; Cd+Alpha attributes

### Difficulty
Intermediate

### Houdini Version
H19

### Tags
[glass, tiles, animation, orient, quaternion, attribute-transfer, pop, trails, material, blend-material, rendering, mantra, intermediate]

---

## Related Tutorials
- tutorial-glass-donut.md (glass material by same author)
- mops-motion-operators-for-houdini-part-3.md (quaternion math for orient rotation)
- tutorial-lipstick-part-3-rendering.md (material blending, glass-like rendering)
