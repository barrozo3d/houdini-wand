---
title: w03   11   meshing v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=H56dPbE3S2E
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [flip, meshing, vdb, particles, attribute-transfer, color-ramp, beginner]
extraction_status: complete
frames_dir: tutorials/frames/w03-11-meshing-v1-1080p/
frame_count: 4
---

# w03   11   meshing v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=H56dPbE3S2E)
**Author:** The VFX School Archive
**Duration:** 7m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now I want to go ahead and generate our mesh. So we've got our point. We need to make a mesh from this. And the workflow we're going to use is VDB. So I'm going to find a VDB from particles. OK, connect that up. We've got an error there. Probably the voxel size is too big. Let's drop that down a little. Still nothing. Maybe the radius scale. It does say that we shouldn't drop it past 1.5. But we're going to be smoothing the VDB after anyway. Try dropping that down to 1. Still nothing. I'll drop this down 0.1. There we go. Getting something still a bit coarse. So I'm going to drop the VDB scale down even further. 0.025. Let's take a while. Now again, something nice and smooth. Probably drop this down a bit. I don't think it'll make much difference now. It should be fine. Good. OK, looks just looking nice now. But still you can see a little bit of roughness there. So we could just drop a VDB smooth. Whoops. VDB smooth SDF. And this is as simple as that. Just connect it up. And we get a much nicer result. Then to bring it back into polygon geometry, we need a convert. I think just by default it will generate our polygonal geometry there. So that's looking really nice. Look, we get all these ripples and waves, all these detail. And that's thanks to the high resolution. OK, so to get some color on here, I'm going to drop a color node, but from a separate stream, I'm going to color the path called first of all. We're going to color the points, but based on a ramp from an attribute. And the attribute will be this cosity, which we still have. So that's going to pull in the viscosity from the same here. And our range, if you remember, the highest velocity was 250. There we go. So we're already getting something there. So now we just need to play with the colors here. So here, let's see on it. I'm going to get some kind of browns going on. OK, so I'm going to bring this one up. Let's find out. Got some values kind of worked out already here. So I'll just drop those in. 0.690, color I want it 0.02435 and 0 there. So we get this nice brown there. And then the position at 2. Great. And then to add another color here, well, I'm going to bring this one down. I'm just going to keep it at white and the position for 0.45. And I'm just going to click on this space here. And that should drop in another color for us. Move that up. And the color for this one will be another kind of brown. 0.525, 0.22665. Not purple, but this kind of yellowy brown color. OK, it's got that colors working there. Now, so we need to transfer these colors onto this geometry. So if you remember from week two, where we were transferring, I think it was the velocity to deform the yogurts, I'm going to do something similar here but with the color. So I'm going to use an attribute transfer, which is here. OK, drop the geometry here. And then just by default, I think it should pretty much work. Let's see if we want to play around. Let's bring the distance down. And then the blend threshold 0.25. Maybe we can get something working a bit nicer there. OK, and then we can maybe if I think we need some color on here to get the blending working. If I drop a color node, I see if that does anything for us. Drop that down in further. We can do this. Well, this is fine as it is for the moment. We'll try a flipbook with this. Let's bring in our the collider. So we got something to look at. So you can see that I'm simulating here. So I'm going to press Escape to cancel that because I highlighted my top network. I'm going to turn off the display there, click on the brain to stop that from running again. Hide the emitter. Go into my collider. Visualize just right at the top. Oh, actually, the go to the transform because we want the correct scale. I'll go back. Let me, I'm going to give a color to this anyway. Put it off to the side. We'll color it to something, something plain like that. OK, let's put it on smooth shaded. Cool. Head back to the start. See, bring the camera in a bit closer. Something like that. Bit far away. Something about there. OK, and then this flipbook, 100 frames. So flipbook is done. Let's take a look. Looks great. Quite subtle, but you can tell that there are different viscosities. The kind of yellowy one is much thicker. The brown one is softer. You can see it because it flows down so much quickly, so much quicker. But it looks really great. Got a lot of detail. Nice little ripples there. And hopefully they'll be able to bring them out even more in the render.

**Frame:** tutorials\frames\w03-11-meshing-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
FLIP particle mesh: VDB from Particles (voxel 0.025, radius scale 1) → VDB Smooth SDF → Convert VDB to polygon. Color ramp from viscosity attribute on particles → Attribute Transfer to mesh.

### Summary
7m49s VFX School Archive module. Part of a chocolate-over-ice-cream FLIP sim tutorial. Meshes cached FLIP particles using the VDB workflow: VDB from Particles (requires small voxel size ~0.025 and radius scale ~1 — don't go below 1.5 without smoothing planned) → VDB Smooth SDF → Convert VDB. Colors particles by viscosity attribute (ramp, range 0–250, brown tones for different chocolate viscosities) → Attribute Transfer to mesh. Flipbook preview confirms different viscosity materials behave differently (yellowy one thicker, brown one flows faster).

### Key Steps
1. **VDB from Particles** — connect FLIP particle cache; reduce voxel size (try 0.1 → 0.025); set radius scale ≈1; small voxel = high resolution but slow
2. **VDB Smooth SDF** — connect after VDB from Particles → smooths rough particle surface; simple default settings work
3. **Convert VDB** — converts SDF to polygon mesh; default settings auto-generate geometry
4. **Color ramp on particles (separate stream)**:
   - Color SOP: mode = "From Attribute"; attribute = viscosity; range 0–250 (max velocity seen in sim)
   - Set ramp colors: brown (0.69, 0.024, 0) at position 0, white at 0.45, yellowy-brown (0.525, 0.227, 0) at higher position
5. **Attribute Transfer** — source: colored particles; target: polygon mesh; distance=small, blend threshold=0.25 → transfers Cd to mesh
6. **Flipbook** — 100 frames to preview result; compare different viscosity flows in same shot

### Houdini Nodes / VEX / Settings
- **VDB from Particles**: voxel size=0.025; radius scale=1 (don't go too low without smoothing)
- **VDB Smooth SDF**: default settings; connect after VDB from Particles
- **Convert VDB**: default polygon output
- **Color SOP**: mode=From Attribute; attribute=viscosity; range 0–250; ramp with brown/white/yellowy-brown
- **Attribute Transfer**: source=colored particles; target=mesh; distance low; blend threshold=0.25
- Flipbook for preview before full render

### Difficulty
Beginner

### Houdini Version
H18+

### Tags
[flip, meshing, vdb, particles, attribute-transfer, color-ramp, beginner]

---

## Related Tutorials
- w03-04-adding-viscosity-v1-1080p.md (same course, adding viscosity to FLIP)
- w04-11-viscosity-and-surface-tension-v1-1080p.md (same course, advanced viscosity+surface tension)
- tutorial-lipstick-part-2-flip-sim.md (FLIP meshing with VDB + Particle SDF approach)
