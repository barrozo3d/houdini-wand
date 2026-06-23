---
title: [Tutorial] Lipstick. Part 3. Rendering
source: YouTube
url: https://www.youtube.com/watch?v=6V7Y5aBmjo4
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tutorial-lipstick-part-3-rendering/
frame_count: 4
---

# [Tutorial] Lipstick. Part 3. Rendering

**Source:** [YouTube](https://www.youtube.com/watch?v=6V7Y5aBmjo4)
**Author:** Alexander Eskin
**Duration:** 14m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's render the thing. Geo, we don't need that. We need stick, droplets, lipstick, lipstick itself. Droplets, large droplets. Set the material to water. Now we should create oak, tin, red or no. Camera, call it shot 10 output. We don't need the output. Everything stays the same. We only need to overwrite camera resolution to half. This is going to be contour 1. Go to material, create a container and a target. Color it black, color it, render target 010. Path tracing, quality. Spectre depth 24, max samples 200, something adaptive, light, no deep image, no environment, texture. But for now we want to set the HDR. So it's going to be black. Camera, camera, order focus stays on for now. Image, A still mapping. Denoiser, no, obstetor, no, post processing, no, AOV. You're probably going to need a cryptomite by material node name. That's going to be it for the render settings. That's going to be it. Now we can start the render. Shortcut, go to shortcut number 1 and open up an IPR. My IPR should be black because we don't have an environment or lights yet. Indeed it is. So let's start with the simplest material. It's the background. It shouldn't have any specular weight. And it should be emissive with the mission weight of 3. And nothing is happening probably because we didn't set the background material to background. There it is. Now we need to move the background further a little bit. Minus 5 minus 12 and set the scale the size to 25 to 25 by 25. That's it. Now the next material is water. It's the other simple one. Spicker. And the default should be enough. Let's start with a metal. Set the metal list to 1 and set the specular roughness to 0. And this should reflect a little bit less than 1. 0.4. Okay. That's it for now. Now we need to create a light. It's going to be going to contain light. With the scale of 25 and 5, should rotate it. Move it around. Apply a texture. Texture is called gradient. One pixel black. Keep instance power. Turn this off. And the power should be 16. Looks a bit old. I should probably rotate it a bit. Hmm. Something feels off. I should also turn the general exhibit to 0. And camera is going to be to 0 as well. Now let's create an sunlight. First we should call this one light. 0.10, 0.1. This is the second light. Just illuminate the front part. As you can see, the adapter field is just broke down because our autofocus is focusing on this invisible light. Let's fix that. Should turn off autofocus feature and you can just click, pick focus and click somewhere here. Is it? Or if you don't want any adapter field, you can switch the aperture edge to 0. It also works. So now I have this. Should select light. Power 2. And create third light. Rotate it. And this is going to be our little highlight. Okay, this is the light. I think it's good enough. Now we can adjust the lipstick shader. It's called specular. Specular reflection 0.45. Transmission 3, 4, 5. Sensation 0.35. And Sss should be probably random walk. Density, reduce the density to 75. And color the albedo 2.1 saturation 0.95. Value 0.8. And as probably shouldn't be as specular. Should be GX. Roughness 0.2. Probably should turn off turn-on fake shadows for it to run a bit faster. And maybe bit brighter. What do we have here? Looks okay. So we also should add the flake shader. Flake's. Flog it to normals. Flake's size 0.65. Flake variance 1. Glend factor 0.9. 3D transform. Should be somewhere around 0.0.02. Let's look at this. So yeah, let's add some variation. That's really nice to look at. And load the camera a bit higher. Maybe bit closer. Now our auto focus broke. Should pick again. Now we can add some variation to the metal shader. So the metal shader should have some bump map. Silling 4D noise. Flog it into the bump. Switch the dive to list of turbulence. 3D transform. Because we're in octane. We can just transform the noise inside the node. And scale it down. Yeah, nice. No, the wrong axis. So 0.01. Here it's 1.1. Now we have some sort of machining happening here. Looks okay. Maybe reduce the intensity of it. And we can also add a secondary layer. Specular layer. GX, rough and 0.2. And reflection should be lower. Maybe lower. 0.75. Also we can plug our noise to specular layer as well into the bump node. Okay. Again, it's a bit more space there. 0.65. And we can probably add an HDR texture. Unfortunately, it's got a bit tricky. Because HDR eyes from polyhaven have an insanely high dynamic range. Hence the name. And octane just goes crazy sometimes. Not all the time. Sometimes it just clips the higher values like the sun. But sometimes I had an issue where the specular highlights from the sun just turned purple. So we're just going to clip the HDR eye to some lower values. We're not going to use it to light our scene. We're just going to use it to add some treating radiance. So we're going to move to cops. I'm going to do that. Cop network. File. Choose our pure sky texture. And clamp it. Up limit 35. Drop output. Hip textures. Dollar eyes. We call it pure sky texture tutorial. Clamped render. Now we have a clamp texture. We're going to choose it. Clamped HDR eye. And we have to tweak the colors. So I've rotated and transformed it. I've changed the gamma values. So I wanted this texture to have some contrast. I didn't want it to light everything evenly in any case values. Rotate to the 0.24 tilt. 0.056 roll. We don't touch this tilt minus 24.2 pan minus 9.2. Same goes to wall. That's it. So now we have some small blue tint coming from the right side. And it adds a bit of a liveliness to our render. And let's not forget to increase the intensity of 3. Let's see what's with extreme. Perhaps we should probably reduce the color saturation values. Now it's closer to the reference. Looks good enough. I would say we can see the caustics. Those are nice. That's it. See you.

**Frame:** tutorials\frames\tutorial-lipstick-part-3-rendering\frame_000.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
