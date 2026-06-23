---
title: 78 building the vortex dop network v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=FAE7gVev-ss
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/78-building-the-vortex-dop-network-v1-1080p/
frame_count: 4
---

# 78 building the vortex dop network v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=FAE7gVev-ss)
**Author:** The VFX School Archive
**Duration:** 9m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, so we have the source. Let's create another top network for this. Taurus, Pyro, same. Let's go inside, create necessary ingredients. So we need a Pyro solver. We'll need a smoke object. We'll need volume source. These are the essentials. Let's set up the smoke object. One way that I usually, that I frequently use to set up the size of the smoke object is by creating a static object and choosing the Taurus, in this case, I'll copy this sub-path and copy it here and use object transform. And if we merge it with the scene with the simulation that we have, we will be able to see it here. It's just a temporary setup so that I can adjust the size of the smoke object properly. I'll do the same thing as usual regarding the making sure that the grid is on the ground. So I'll say copy parameter based relative references and say this divided by 2. And I'll make this bigger, maybe 3. Give it a bit more room. Yeah, I'll put it to 1.5. I'm going to make the Taurus go higher here, 1.5. Now we need to remember that we were considering that the center of the Taurus was at 1 of height. So here we need to adjust 1.5 as well. Just make sure that the vectors are concentric. Okay, just showing that they are. Don't need this or this. It's going inside. So now we have 3 here. Let's give it a bit more depth. 4 and 3. Let's see how this works. And the other thing will be for us to kind of push this a bit. Minus 1. Okay. I want this to go towards that direction. So the difference that I'm going to add to this is that here on the... Let's just finish setting this up. So the smoke object, the division size, I'm going to copy this parameter and make sure that the source inherits that parameter here, based relative reference and here as well. Based relative reference. Let's go back to the smoke object. Put this at 0.04. And the volume source, let's choose our source. Our source. And here we want to source smoke. Okay, density, temperature and velocity. Now here on the power solver, the main difference is that I don't want the binds to make things go up. I want the binds to make this simulation go towards that direction, which is minus 1 on the Z axis. Okay. And I think we're all set. I don't think we're going to be needing this anymore. Just going to delete it. And we should be good to go. Oh, let's have the dynamic resize. Same thing as before. Here I'm going to track the source as well. And that's it. Let's see how this looks. I'm going to create a camera, another camera. Let me just run this for a moment. Okay, and let's just create a camera here. Yeah, I think this will work. Cam 2. Let's go to the solver. Let's let this run a bit more. Okay, so this is what we have so far. We have this dynamic. And I'll just make some adjustments. As you can see, the buoyance is not making things go up. It's just making things go back quite fast actually. We don't have a lot of resolution, but the simulation is pretty fast. The shapes that you're seeing here are without any adjustment in terms of disturbance or turbulence. The only thing that's happening is supposedly just here regarding the shape. So we don't need combustion. And regarding the shape, there's some dissipation going on, but still not much. Let's also increase the resolution here to 0.3. Okay, this is what we have. Interesting vortex. It was the main goal. So what I'm going to do is I'll just make some adjustments here. And the first thing I'm going to make sure is that we have a bit of a bit more of dissipation. Quite a bit actually. I'm going to make the dissipation be quite strong 0.2. Okay, so even though I have this dissipation at 0.9, nothing seems to be happening. And it's a great opportunity for us to go over these control field settings for most of these micr-solvers will have this type of controls. This might be something that you're interested in, that you like, all this trail. But what I want is for this to kind of dissipate a bit faster. I don't want it to go as long to the back as it is right now. But so what I'm going to do is I'm going to stop this. I'm going to explain you how this works. So basically what this is saying is that look at the temperature. Check for this control range, meaning that check for the range of temperatures that go from 0 to 1. And remap the dissipation field based on this graph, meaning this is going to be the control minimum. This is going to be the control maximum. And based on these values, so it's going to be from 0 to 1. So whenever you have a temperature that's low, apply more dissipation. And when you have a temperature that's high, being 1, apply less dissipation. But here we have values of density and values of temperature. There are actually much higher than one. If you check the values that you have on the source, let's go to the source. And you go here to the where you have the density. We have a density that goes from 0 to 2 basically. And the temperature is going to be using the same values. So we basically just need for this to have some effect, some visible effect. We need to adjust this control range. And remember, the way those values are being sourced into the simulation is through the volume source. And the volume source is adding on each step of the simulation. It's adding those values. So even though we were bringing into, we're continuously adding 2 plus 2 plus 2 plus 2 plus 2. So we need to take that in consideration as well. So here, the control range, a reasonable value would be for us to use 2. If we weren't adding, but since we're adding, let's go at least with 4. And right now, we should see more of an effect coming from the dissipation solver. OK, so it's dissipating faster already. OK, so it reaches the end, but already with very little dissipation, with very little density there.

**Frame:** tutorials\frames\78-building-the-vortex-dop-network-v1-1080p\frame_000.jpg


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
