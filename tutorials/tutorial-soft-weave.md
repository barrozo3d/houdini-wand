---
title: [Tutorial] Soft Weave
source: YouTube
url: https://www.youtube.com/watch?v=Ohj4ag8DZRo
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [sweep, weave, sine-wave, curve-u, blend, attribute-transfer, hair, redshift, vellum, point-deform, intermediate-advanced]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-soft-weave/
frame_count: 4
---

# [Tutorial] Soft Weave

**Source:** [YouTube](https://www.youtube.com/watch?v=Ohj4ag8DZRo)
**Author:** Alexander Eskin
**Duration:** 36m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's start with a June node. We've got a total weaving source. To have inside, create line, align it to Z axis. Copy length, paste it somewhere here in the Z origin. Delight by 2 minus, now it's in the center. Make it 2000 points for starters. Now we need some sort of the attribute for moving the points around. It could be the rest attribute or curview. I would use curview. Curview, do not resemble, just generate curview. Now we have the attribute and just create the basic structure. Wiring. I'm going to create the wiring using sine function. It be starting with y, v at p y equals sine curview. So, now it looks like this. The amplitude is too big, the frequency is too low. The amplitude is the thing after the brackets. The frequency is multiplied inside the brackets. 100. Now we have the sine wave. Now we just copy that, say p x. Since the frequency is the same, it looks like this. But if we divide the frequency by 2, now we have something that resembles the weaving pattern. To make it a bit more convenient to work with, I would create some sliders for the amplitude and frequency for every axis. So, the base scale would be float scale. Channel float scale. Now I'm going to create the amplitude. Float and put x equals channel float and pay 2. x multiplied by base scale. Now I'm going to copy this a couple of times. It's going to be y, z, amplitude z, amplitude y. And here we are going to change this from and create integer attribute for frequency. X equals channel integer frequency x. And copy paste for every axis. Z, y, y, z. Then, change the numbers to our variables. Frequency x multiplied by amplitude x. Here we have frequency y, amplitude y. And the same will go for z axis. Frequency z, z, and amplitude z. For now, create the variables, sliders. 0.1, amplitude 0.3, 0.15, 133, let's see, 300, 600, 600. The problem is that the z axis is flat. So we have to make it a plus. Now it looks like something. Also, we can add the separators to make it look pretty here. Bam, bam. Now we have these lines. So the sliders are more readable. The next thing is to create the sweep. Just to see how it looks like. The sweep requires backbone. No cross-section journal to provide it. But we can use the default one. This round tube will work fine for our case. Just change the surface type to columns. And the radius to 0.05, columns 6. Now we have something resembling the wiring. 170 twists. And also add the second one to make it more dense. To make it more readable, we can go up to the object context, go to miscellaneous, and press the shade open curves and viewport. Now it's going to look a bit like it has thickness. So what's cool about the sweep supports the P-scale attribute. You can create the temporary animation. Animation temp. Floated P-scale equals ramp. Scale. Curve you. But the problem here is that the second sweep does not inherit the P-scale from the first sweep. This can be fixed in the UV and attributes tab. There's an exception for the P-scale. You can just kill it. And also kill it here if we're going to create the next sweep iterations. So right now this sort of works, but not really. I'll have the time attribute just to demonstrate the animation without moving these keys. Wrong direction. So right now when we animating this P-scale, the strands they spin uncontrollably. And there are a few solutions to that. One of these is to make this spinning not by the distance by the edge, which supposedly should fix this. But it fixes only in the simple occasions. So if you grow things like this, everything's working fine. But if we decide to change the direction, so here like this, say, and it's spinning again. So well, this is a very elegant way to animate this thing. Unfortunately, if you have lots of these and if you're animating it with the infection or noise growth or you're trying to animate them from the center, like, I don't know, like this. And it's just like, it's going to spin. No matter what I tried, it was spinning. And unfortunately, I had to use the blending instead of just the default sweep, P-scale attribute, which would have been great. It would have been an elegant solution. The node tree would work, would look great. But it didn't work for me. If you have some sort of simple animation when you have the close-up of the thing, let's grow it up. Like something like this. You can use it and it's going to look perfect. So the thing that I did in the actual weaving example at the beginning is that I blended three wires with the different width. But here you can just use the same sweep to animate it. For example, you're going to multiply it by two. And then just put the third point, the value 0.5. And it's going to have the same wave as an example. See, sort of, wait, by four. To make it look better. This is nice. I like it. So anyway, for this particular case, it works. And you can use it like this. But we're going to improve it a bit. So let's add more lines. Create another line. X, axis, copy, paste, divide, minus. Here it is. So let's make, for example, eight points, paste into wiring. And now nothing works because we should add a plus here. Otherwise it's going to flatten the whole thing. Let's decrease the width a bit. The problem right now is that they have the same angle and they should sort of intertwine. To fix this, we can change the direction of the Z-axis. But we should change it every other line. So right now we have the primitive numbers available for us. 0, 1, 2, 3, 4, 5, etc. So we can use every other number to change the direction of the wiring. To make it work, we can use the if. For example, if primitive number, 0, 2 equals 0, then we're going to use this. But if it's not 0, we're going to use a different thing. We're going to use minus 3. Primnam. Primnam. Okay. Looks like something. Okay. So the sweep example works great. So you can stop right here. If everything is working great for you, but it didn't work for me. So I'm going to have to make it a bit more difficult. So we're going to kill the temper animation. At least for now. And we're going to add other two sets of sweeps. So this is going to be our sweep final. And I think we should add another two more sweeps. Like this. You can keep adding these until you run out of patience. 0.2.4, 2.5, 0.1. And last one is 0.05. And the spinning should be different in every sweep. 0.170, 0.256, 0.512. 0.512. Okay. Now we have a lot of threads. Now this is going to be our source sweeps. And I'm going to use another set. It's going to be our sweep 0. Meaning this, we're going to have the same parameters except for the radius. It's going to be equal 0. So the amount of points is the same. 6 million, 6 million. And we're going to have to use the blend function. So for now we're going to use the curve view as our attribute for blending, but later we're going to change that. Float our blend, meaning we mapped blend. CHRAMP Blend Curve U plus or minus time multiplied by 0.1. VFP equals Lurp P, meaning the position on the first input then V at OP input 1P, meaning the position on the second input. And we blend it using the R blend. Okay. So right now, no matter which way you spin it, the threads are going to stay the same because it's just the blend. And it works almost as fast. And we have two rows of sweeps basically doing the same thing, but well, I couldn't come up with a more elegant solution. So this is working. You can add some custom attribute to blend the things. For example, attribute transfer. We're going to create the attribute. We're going to create the attribute. The attribute is going to be called blend. And the default value is 0. And the value on the second input is going to be 1. And we're going to use some sort of sphere to blend things. And here we're going to use our newly created blend attribute instead of the curve view. So sphere is huge. We're going to use it like this. And let's see. Okay. Also again, just add the time here. As usual, if we're too lazy to animate it with keyframes. And let's kill these two sweeps for now. So we're going to see what's going on almost in real time. So everything is working as expected. Nothing is spinning. I'm happy with the result. To make it more complex, we can add the third set of sweeps. And it's going to be the transitional sweep, the big one, the big boy. Big. It's going to be four times as big as this one. This is the big boy. And we're going to use the third input to fix our blend function. So this is going to be a bit tricky. All right, now we're going to use the our mapped blend. But we're going to refit the result. So for it to work, we're going to refit the our blend from 0 to 0.5 to 0 to 1. And add the next one. Take the results from the second input, the third input, that's going to be called open input 2. And we're going to take the values from 0.5 to 1. And remember to 0 to 1. So right now, when the blend reaches reaches values from 0 to 0.5, it blends to the second input. And then after 0.5 to 1, values it blends to the third input, creating this sort of line. This is a bug at the center. This shouldn't be here. I'm going to fix it later. Or maybe this one will be noticeable because we're going to move the sphere. Anyway, you cool. Blend our. Also fix the values. We can add a couple of more points to it. Switch the interpolation to a paste line. Now the wave is bigger. Not sure if it's a good thing, but why not? Also, we can just move this transition one a bit higher. So it's going to create this wave, but it's too big. I was going for a much more subtle effect. Maybe 0.15. Now we can move the sphere that drives the propagation of this transition somewhere else. Not here. Also can add a bit of variety to the transfer, but just making noise mountain. So mountain propagation. Now we're going to just attribute copy this to the unnoised weaving. And we're going to copy the blend attribute. So right now the blend is going to have a bit of a noise, but it's not apparent. I'm going to increase it. Maybe reduce a bit in the noise effect. Something like this. This looks good. Depending on the result you're going for, you might want to add some fuzzy strands. Now that can look lively. I'm going to select 1% probably of the existing primitives and just use the mountain out. So we should move along spline. The amp that should be way less. The group should be named fuzzy. And we can turn on these two layers for a bit of viewing. Looks weird. Okay, on the side is 0.1. Aha, nice. Amplitude 0.5. And the percentage should be smaller like, I don't know, 0.01. More like this. Okay. Maybe you don't need it. It's just the matter that look you're going to have. And we can add the variation to this source wiring as well. Just a little bit. Maybe this octave is for the fractal. Maybe bigger, and size. Yeah, maybe like this. So now it has a bit of a wave in it. It can add realism. Looks a bit nicer. I'm going to move it a bit. And I was leftist to deform it a bit. Make it wavy with the point form. Create some basic grid. 150, 50. Maybe one point like this. I'm going to close. I'll solve it. Kill the gravity and add some wind. Amplitude 0.2. Squirrel size 0.3. Post length 5. Behold. Something's happening, okay. Now we use second input to the point form as the resposition. The third one as the deformed position. Everything is laggy. Now it should work. I'm going to turn off a couple of sweeps. For it to run faster. Maybe we can use a time shift. Just add some frames here. So the starting frame would be already deformed. Nice. Stir now these ones. Add some expert node. Call it out. Go to the object context. Create another dune out. Call it weaving. Turn on shade of a curves as well here. Marge this thing from the source. Create a camera node. Click and do it. Camera. Press lock camera. Now we're moving to the viewport and the camera moves with us. Choose some sort of appealing angle. And let's render it. Create a background. Create. OK. Something like this. Camera. Press your flag. One is going to use the background. And another one is going to use the light. The background light is going to be enabled only for the background. And the light is going to be used to light. The weaving is going to be used for everything except the background. Turn it off for now. Go to the out. Add shift. Make a hotkey IPR half. Go to the material context. Create two materials. Redshift material. Press going to be the background. Standard. Light. Almost white. Non-reflective. Second one is going to be weaving. I'm going to use the hair shader for it because otherwise I'm going to have to use the strands of very heavy to render. And hair is pretty light. Weaving here, background here. Background should be dark just for viewport sake. And here it's going to be sort of. This is only for the preview purpose. Anyway. To make it render. The first thing I did, I used the strands, but they're very heavy to render. In terms of geo, the hairs are very fast to convert the strands. So just press this one. Render, render polygons hair. The full hair width is huge, but I'm going to go with it for now. Everything is dark. So sad. The lights are turned away from the background, so it's so dark. We're going to spin it. And it's going to look better. And this one on this. It's smaller. And... The hair looks terrible because it's huge. Every strand is like 100 times as thick as they should be. So... Refresh. You can see anything, but it's better. Why we're not seeing anything? Because I flipped the dimensions. So right now, looks kind of weird. Should be bigger, a bit bigger. Right now, a couple of problems. It looks bad, I don't know, but I'm going to fix this. One thing is low poly hair. So the one thing that we can do is to increase the density of the source points, like maybe 20,000. But it's going to work very slowly. Our setup is going to work very slowly. And another thing that should work is the primitive distillation. It didn't work with the hairs. The distillation didn't work with hair as well. So there is a distillation for exactly hair, but they sort of hit it. It's in the robot output. Global hair. So distillation. Eight steps. So, it worked like this. Now we press the button to render. Now it's so curvy and looking good. Natural. Next thing we can improve the shader of the hair bit by introducing transparency. Tada! Of course it's going to increase the render times drastically, but it's going to help with the look. We can also increase the reflection, reduce the glossiness. Transparency make a transparency bit colorful. And remove this terrible thing. Now we can use the custom with attribute that is going to override the attribute on top of this node. And we're going to use ramp with land multiplied by 0,001. Forget to press the button. So this sort of works, but we have the ugly strands at the back of our transformation. If we move the slider around in theory should fix this, but it didn't. So even with the width equals 0, somehow it renders it. Maybe we're doing something wrong because the small strands disappeared. Maybe they haven't. Anyway, the brute force solution is just to kill the strands with the thickness of 0. Like this. That's it.

**Frame:** tutorials\frames\tutorial-soft-weave\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedural weave from 2D sine waves on a line (curveU-based X/Y offsets with different frequencies, every-other-primitive Z-flip) → multiple Sweep SOPs (different radii/twists) → pscale animation via blending P between radius-0 and radius-N sweeps (lerp avoids spinning artifact) → Attribute Transfer from animated sphere drives blend → Mountain noise adds propagation variation → Point Deform on Vellum cloth grid for wind. Rendered in Redshift as hair (polygon strands → Hair mode, Global Hair distillation 8 steps).

### Summary
36m17s tutorial by Alexander Eskin. Builds a soft weaving fabric animation entirely from procedural SOP geometry (no simulation for the weave itself). Lines with CurveU-based sine-wave offsets create a weave pattern; alternating line direction prevents uniformity. Multiple Sweep SOPs (5 passes at different radii/twists) create strand variety. pscale grow animation via P lerp (not direct pscale on sweep — causes spinning); Attribute Transfer from animated sphere drives propagation blend. Third sweep (4× radius) enables 3-stage blend. Mountain noise on blend attribute. 1% random fuzzy strand group with Move Along Spline. Source variation via Mountain. Vellum wind animation via Point Deform on a simulated cloth grid. Redshift hair shader (much lighter than polygon rendering); Global Hair distillation 8 steps; custom width ramp.

### Key Steps

**1. Base Wiring (Sine Wave Weave)**
- Line SOP: Z-axis, 2000 pts, centered
- **CurveU** attribute (do not resample, just generate)
- Wrangle: `P.y = sin(curveU * freq_y) * amp_y; P.x = sin(curveU * freq_x / 2.0) * amp_x;` — halving X frequency creates interweaving crossover pattern
- `P.z += curveU * amp_z;` (plus = not flat)
- Parameterize: base_scale, amp_x/y/z, freq_x/y/z (float + integer channels)
- Second line on X-axis; 8 total lines → copy/paste parameters
- Every other primitive: `P.z = ((@primnum % 2 == 0) ? 1 : -1) * freq_z * amp_z;` — alternate Z direction so lines interweave

**2. Sweep SOP (Initial)**
- **Sweep SOP**: surface type=Columns, radius=0.05, columns=6, twist=170
- Object context → Miscellaneous → enable "Shade Open Curves in Viewport" → thickness preview
- 5 sweep passes with different radii (0.2, 0.4, 0.25, 0.1, 0.05) and twist values (170, 256, 512…)

**3. pscale Grow Animation (Blend Method)**
- Direct pscale on Sweep causes spinning — don't use for complex/animated weaving
- **Method**: create "Sweep 0" (same params but radius=0, same point count as source sweeps)
- Blend wrangle: `float blend = chramp("blend", curveU + ch("time") * 0.1); P = lerp(v@P, point(1, "P", @ptnum), blend);` → geometry blends from radius-0 to full radius without spinning
- For simple non-animated cases: pscale ramp on curveU → Sweep pscale exception in UV tab → works fine

**4. Attribute Transfer Blend (Sphere Driver)**
- Add `f@blend = 0` on wires; set `f@blend = 1` on a second copy
- **Attribute Transfer** from large animated sphere → radius controls propagation wave
- Add `time` parameter to animate transfer; Mountain noise on blend → noisy propagation edges

**5. Three-Stage Blend (Transitional)**
- Create "big sweep" (4× radius) as third input to blend wrangler
- Refit blend: `fit(blend, 0, 0.5, 0, 1)` → drives lerp from thin→medium; `fit(blend, 0.5, 1.0, 0, 1)` → drives lerp medium→big
- Adds wave height variation; adjust sphere position and Mountain noise on blend
- Move transitional big sweep vertically slightly (scale=0.15) for subtle effect

**6. Fuzzy Strands (1% Variation)**
- **Primitive Group** (random 1% of strands) → **Move Along Spline** with small amplitude (0.5) → group named "fuzzy"
- Adds organic variation; percentage and amplitude tunable

**7. Source Variation**
- **Mountain SOP** on source lines (large fractal size, subtle) → base wiring not perfectly straight → more natural

**8. Vellum Wind via Point Deform**
- Grid 150×50 → **Vellum Cloth** sim: kill gravity, add Vellum Wind (amplitude=0.2, swirl=0.3, pulse length=5)
- **Point Deform SOP**: input1=wires, input2=rest grid, input3=deformed grid → wires inherit cloth cloth deformation without full sim
- Time Shift to use pre-deformed frames as start

**9. Redshift Hair Render**
- Materials: background (Standard, white, no reflection) + weaving (RS Hair Shader — much lighter to render than polygon strands)
- Render settings → **Render Polygons = Hair** → converts curve strands to hair primitives
- **Global Hair distillation**: 8 steps → smoother curves, natural look
- Custom width ramp: Attribute Wrangle `width *= chramp("w", curveU) * 0.001;` — taper strand ends; blast width=0 strands (invisible but still render)
- Transparency on hair shader → better look but slower render
- Lights: two RS lights (one for background, one for weaving only via visibility settings)

### Houdini Nodes / VEX / Settings
- `P.x = sin(curveU * freq_x / 2.0) * amp_x;` — half-frequency for X to create weave crossover
- `P.z += curveU * amp_z;` — add (not assign) Z offset
- `@primnum % 2 == 0` → alternate Z direction per line
- **CurveU SOP** — attribute generate (no resample)
- **Sweep SOP** — surface=columns, radius, twist; 5 passes at different settings
- P lerp blend wrangle: `P = lerp(P, point(1,"P",@ptnum), chramp("blend", curveU + ch("time")*0.1));` — no spinning
- **Attribute Transfer SOP** — sphere-driven propagation; animated by animating sphere position
- `fit(blend, 0, 0.5, 0, 1)` + `fit(blend, 0.5, 1, 0, 1)` — three-stage blend
- **Mountain SOP** on blend → noisy propagation
- **Point Deform SOP** — deform wires by cloth sim (rest → deformed)
- Redshift Render: **Render Polygons = Hair**; **Global Hair distillation** 8 steps
- RS Hair Shader vs RS Standard Material — hair is 10× faster to render
- Width ramp wrangle: `width *= chramp("w", curveU) * 0.001;`

### Difficulty
Intermediate–Advanced

### Houdini Version
H19

### Tags
[sweep, weave, sine-wave, curveU, blend, attribute-transfer, hair, redshift, vellum, point-deform, intermediate-advanced]

---

## Related Tutorials
- tutorial-purple-sponge.md (instanced geo + Redshift render by same author)
- mops-motion-operators-for-houdini-part-2.md (Move Along Spline, Move Along Mesh)
- tuna-can-procedural-modeling-and-rig-with-kinefx.md (procedural SOP modeling)
