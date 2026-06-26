---
title: [Tutorial] Lipstick. Part 2. Flip Sim
source: YouTube
url: https://www.youtube.com/watch?v=T1OTnyioFrA
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [flip, fluid, droplets, surface-tension, stick-field, velocity-field, vdb, collision, pscale, intermediate-advanced]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-lipstick-part-2-flip-sim/
frame_count: 4
---

# [Tutorial] Lipstick. Part 2. Flip Sim

**Source:** [YouTube](https://www.youtube.com/watch?v=T1OTnyioFrA)
**Author:** Alexander Eskin
**Duration:** 26m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** And now it's time for the droplets. Let's create a new node called lipstick. Well, let's source. Reign. Diving. Object merge I would do. Convert it to VDB. Resolution should be a bit higher. Convert back to polygons. Add some normals. And we don't need the bottom part and we don't need the part that we don't see behind the camera. So we're going to scatter the points on the frontal part. So we're going to clip that. Something like that. And another clip for the ZXs. So this is going to be our shape to scatter. Now we're going to scatter some points. We'll use density scale. And we're going to scatter for example, 55. It's going to be our tiny points. Tiny points. Tiny. We're going to create a tribute. Create a fiscal. Equals 0.03. I'd visualize node. And we're going to add some random adjustments to the point scale. Float. I'd just float. For a should multiply pattern random, mean value 0.2. And another, I'd just multiply by noise from the smaller element size. And we'll perhaps have some curve adjustments. So these are going to be tiny points. These are going to be medium points. These are going to be big points. Big. Here. Garage. Here we should have around 100. These 10 big ones are rare. And the base scale should be around 0.05. And for bigger ones, maybe 0.8. I'll show you more around some offsets. Now it looks a bit too evenly distributed. Maybe we'll just base scale a bit. A little seed. Adjust the global seed. And the bigger ones. I want the bigger one on top. I'll look like so. Maybe another one. So yeah, this is not a strict rule. You just have to figure out what works best. Now we're going to push them out a bit with the point roll. We're going to call it this place here. Since we already have the normals on these points, we're going to use the normals up here. Before scatter, we can use the displacement along the normals to push those things away from the surface. We're going to use the p-scale from the points. We're going to use this p-scale to adjust the magnitude of displacement. And scale should promote it. So right now we have the displacements that works like this. So this point has scattered outwards. We're going to use a copy to points. Copy some Sears. Hold it on Spears and scale should be 2. We're going to use the points from volume as our source for flip points. And before that we should create a null. We're going to call it Control, Color Red. And here we can create a float attribute for our flip resolution. Flip, press, flip, press. Range from 0 to 0.1. And default resolution should be probably 0.05. A copy parameter based in here as a relative reference. That's it, we don't need to add a scale attribute, I think. 0.05 is promoted to big. We're going to stick to 0.01. Also increase the jitter scale to 1. And it's going to be 30,000 points, not much. Let's get to the first start. We need to create collisions for our geometry. So we're going to take our source geometry. And put here, the division source. The first output is division g. The second one, division volume. And the volume resolution. Well, I used the same resolution for the flip here. So this is fine. One more thing we need to create starting velocities for our droplets. Otherwise they're going to fly away. I've used the natural bit transfer. Transfer here with the normals from here. Good enough. I use another wrangle. Well, starting well. Here it is. It calls and multiplied by a channel flow scale. And the scale should be 0.01. Probably won't need that later on, but I'll stick with it. In droplets. Now we should create our drop network. Call it flip. Davenside. Create a flip solver. And the flip object. The object is going to be our end droplets. And the resolution. Which you'll be having above her. Should be the same as our flip press. And the initial input should be particle field. There you are. The boundaries are a bit big. Sometimes the viewport doesn't allow you well. So that's why I reduced the boundary size. Viewport log probably. So everything is black now. Also in the guide step, which the visualization from spreads to particles. Which are nicer to look at. So we also need to add gravity now. Gravity force. Don't need it right now. What for for the future? And we're going to disk collider static object. I'll make sure that it's on the left. Because in the opposite makes a difference. And for our static object, we need to tell it to use subgeal. Collider geo in a subpath. And here in collision step, collision detection, volume collisions. Mode, volume sample, proxy volume, pop-up collision volume. It's going to be it. Hopefully. Now, at least for now, we're going to use particle field surgeons. And we're going to tell it not to export everything, but only to expert flip object. Also for debugging purposes. So this scene won't be slow as hell. We're going to do three quarters of all the points that are now scattered on this lipstick. We're going to do it by using the clip node. Here, half, and here, for another half. And maybe, look, so. And I'm going to call it red. So I won't forget to delete them. Although my control is also red. I'm going to think about it for a while. Anyway. So our test, yeah, I forgot to turn the output to particles and visualize velocity in droplets. Where are the droplets? Here they are. Okay. Sim. Everything is flying away because I forgot to negate the normals. So those these are facing the same direction as normals. And they're trying to escape the shape of the lipstick. So here we should have a minus. Okay. So they're splashing now. All good is expected. Okay. Probably increase the resolution a bit. So as for the settings, we should sure we have to add a surface tension. Surface tension equals two. Maybe that will differ now. Yeah, we can also turn the gravity on, but reduce it to minus two. And I've also reduced the physical properties. I've also reduced the density to 200. So the droplets would feel a bit lighter because that's the look that I was going for. Oh my god. We should also decrease the timescale. So it sort of works. Not as good as it should be, but it works. So they collide. They interact with the collider. They collide with each other. And they fall. But the problem is that they don't stick to the lipstick. No matter how hard I try to use collisions. I should turn it on, of course. It wasn't enough. So stick scale equals one. Max distance. I just use cells. So it's just, you know, it's one voxel from the collider. And it's going to be it. Let's try again. Yeah, that's better. Another thing is that they still fall from the lipstick. And also they have these ugly lines. I do not like that. So to fix the falling off lipstick, we should have another Veloster field. It's going to call the bell sticker. It's going to be just tube. Handcaps. Increase the size. So it will cover all the lipstick. It might be increased the radio scale a bit. 1.5. Now I'll create points from volume. Increase the resolution. Add scale attribute. Add a rest attribute. That's also important. Store rest. Now we have to just flatten it. Now we have to flatten it. And create some force that moves the points towards the lipstick. 3. Equals minus normalize t. So as you can see, point trails are showing us that Veloster is aligned towards the center. Now we have to restore the position of the points. Extract rest. And create volume. Restorize attributes. We need a Veloster attribute. Luxe size could be bigger. It's smaller. I mean it's smaller. Okay. So we have our sticker. Remember they were just falling like this. But now we need to of course make it work. Volume source. Source smoke. Move that thing on top. And remove the bottom two. Now we have Veloster. Veloster is a real everything works. And we need to tell it to look for our Veloster. Here's our Veloster. Veloster sticker. We should plug it into the... And right now they should just fly away violently. And they do. It means everything's working. Should decrease the scale to 0.01. 0.01. Now everything is working better. As we can see they're sticking to the surface. Trying their best. There's also one thing we need to fix. For more interesting dynamics. You don't like that they collide too much. There shouldn't be any relaxation situations. I like the big one. To make the movement more fun. We should introduce the stick to collisions volume. We have a tab for it. Control field stick. So there's a tooltip that says it scales the effect by spatially varying field. Which is match the collision field in resolution. Okay. So it's basically some attribute in volume shape that gonna multiply this by stick field. So they're gonna move in a more interesting manner. So we're gonna create here stick mask. Point, what? What are called stick mask? Important node. Our stick mask would be... Next, var an i. Position, then there's a trick that I've been taught recently. Subtract. One from another. And then fit it. And I'm gonna put it to stick. Stick. Also we have to promote the fit for easier control of everything. Now clean this up. Invisible and visible. And visualize stick attributes. Now also another one. Another thing we have to promote the frequency. Okay. Now that's enough. Increase it. Something like that. You can play around with the frequency. It's not a very critical parameter. Anyway, it should decrease the maximum value. Increase the minimum value. We have some spots where the friction would be zero. And some spots where the friction would be one. Looks good enough. Now we have to create a VDB from polygons. We should have the same resolution here as our collider. And it's the same resolution for our Vibsaurus. Subtract. This one. And we have to add a surface attributes which are point stick. And VDB name should be stick. And we should merge the two together. So now they should move a bit different if we apply the control field. Maybe we should kill one of the clip subs. So yeah, this is more fun. But again, the movement is a bit too violent. I mean, the velocities that they produce. So what I did, I cheated and I vetted viscosity. It equals one. So viscosity kills velocities a bit. So now they tend to move a bit more relaxed fashion. So this is going to be a good looking part in our animation. Where the two droplets collide. Now we should create a few new compress. And file cache the thing. Call it something like droplets in the version. 150 frames. A local path, hip, sing. We don't need any of the attributes. Particle separation probably is the same as our lip resolution. Not sure, but okay. And we can cache with our relative low resolution. Maybe higher. We can go higher probably. Oh, kill the clips. 200,000 points. Let's stick to this resolution for now. And we can see 150 frames. We have another particle for the surface here. Okay. So how does it look like? The money shot. Blubble. Okay, looks good. We should be from particles. Our resolution of the flips in divided by two is the left thumb. It would be smooth as the F. It would be smooth. Gaussian. Maybe three iterations would be enough. So we want those small ones. And they may convert to polygons. So we're going to have some geometry render. Now, out droplets. If you're going to use some super close-ups, then you're probably need to increase the resolution. Also, we probably need to add some normals and do-of-them. Add normals to points and add a folder to the normals. Add to bits normals and lower them. Five iterations. Helps a bit. So that's it for the droplets. I think we should render it in our next part.

**Frame:** tutorials\frames\tutorial-lipstick-part-2-flip-sim\frame_000.jpg


---

## Structured Notes

### Core Technique
FLIP droplet sim on lipstick surface: multi-size scattered points (tiny/medium/big) displaced outward by normals × pscale, Points from Volume as FLIP source, VDB collision from lipstick, initial inward velocity (`−normalize(N)`), surface tension=2, stick-to-collision scale=1, custom velocity sticker field (tube → rest → force toward center), noise-based stick control field, viscosity=1 to dampen. Cache, then Particle SDF → Gaussian → Convert VDB for render mesh.

### Summary
26m21s FLIP tutorial by Alexander Eskin. Creates realistic water droplets that cling to the lipstick surface. Three passes of scatter (tiny ~0.03 pscale, medium, big ~0.05–0.8) with random pscale noise variation, displaced outward along surface normals proportionally to pscale. Points from Volume is the FLIP source (resolution from control null parameter `flip_res = 0.01`). Lipstick as VDB collider (Div Source). Initial velocity: inward (negate normals × 0.01 scale). DOP: FLIP Solver + FLIP Object (particle field). Surface tension=2, gravity Y=−2, density=200 (light), timescale tuned. Stick to collision (stick_scale=1, 1-voxel max). Custom velocity sticker: tube volume with rest attribute + force toward center axis → Volume Rasterize → Volume Source "source smoke". Spatially-varying stick control field: noise-based stick mask on VDB surface. Viscosity=1 to calm dynamics. Cache FLIP, then surface: Particle to SDF (res/2) → Gaussian smooth 3 iters → Convert VDB → normals + Attribute Blur 5 iters.

### Key Steps

**1. Source Geometry**
- Import lipstick geo → VDB from Polygons → Convert back (clean normals)
- Clip front half + clip on ZX axis → only visible surface area
- Three scatter passes: **tiny** (55 pts, pscale≈0.03), **medium**, **big** (~10 pts, pscale≈0.05–0.8)
- Random pscale variation: `pscale *= fit01(rand(@ptnum), 0, 0.2)` × noise (small element size)
- **Displace along normals**: `P += N * pscale * ch("scale");` (N from lipstick surface, point carry normals before scatter)

**2. Control Null**
- Null OBJ named "Control" (red): add float attribute `flip_res`, range 0→0.1, default 0.01
- Paste as relative reference into FLIP Object resolution

**3. FLIP Source**
- Copy spheres (scale=2) to scattered points for preview
- **Points from Volume**: jitter_scale=1, point_separation = flip_res (~30K pts at 0.01)
- **Div Source SOP** on lipstick geo: output1=DivGeo, output2=DivVolume (collision volume); resolution=flip_res

**4. Initial Velocity**
- Attribute Transfer: copy normals from lipstick onto scattered/source points
- Wrangle: `v@v = -normalize(v@N) * ch("flow_scale");` (flow_scale=0.01) — inward velocity so droplets splash toward surface, not away

**5. DOP FLIP Setup**
- **FLIP Object**: particle field, resolution=flip_res from control null
- **FLIP Solver**: connect div_geo + div_volume as collision inputs
- **Static Object** (disk collider): use subgeo path, collision detection = volume, proxy volume = collision volume
- Gravity Force: Y=−2 (reduced for light feel)
- FLIP Object settings: surface_tension=2, density=200, timescale tuned down
- Sim test: clip 3/4 of particles for faster iteration

**6. Stick to Collision**
- In FLIP Solver → Stick to Collision tab: stick_scale=1, max_distance=1 cell (1 voxel from collider surface)

**7. Velocity Sticker Field (Keep Droplets on Surface)**
- **Tube SOP**: covers lipstick, radius=1.5x, no caps
- **Points from Volume** on tube: add scale attribute, **Add Rest Attribute** (store rest SOP)
- Wrangle: flatten points (P.y=0 or similar), then `v@v = -normalize(@P) * 3;` (force toward center axis)
- **Extract Rest SOP** → recover original positions
- **Volume Rasterize Attributes**: vel attribute, voxel_size larger → velocity volume
- **Volume Source** (DOP): source smoke mode, plug into FLIP Solver → provides velocity sticker field

**8. Stick Control Field**
- VOP network on points: `stick = fit(noise(@P * freq), minval, maxval, 0, 1)` → spatially-varying stick mask
- Promote frequency, min/max values
- **VDB from Polygons** (same resolution as collider) → subtract from collider VDB → **Add Surface Attribute** (`point_stick`) → VDB name="stick"
- Merge with collider VDB → FLIP Solver reads stick control field → more interesting dynamics

**9. Polish**
- **Viscosity=1** in FLIP Solver physical properties → dampens violent velocities → more relaxed droplet motion
- Kill clips, simulate full 150 frames at reasonable resolution, cache

**10. Surface Reconstruction**
- **Particle Fluid Surface** (or FLIP SDF): resolution = flip_res/2 → Gaussian smooth 3 iters → Convert VDB to polygons
- **Add Normals to Points** → **Attribute Blur** N, 5 iterations → smooth shading

### Houdini Nodes / VEX / Settings
- **Div Source SOP** — generates collision geo + volume from lipstick
- **Points from Volume** — jitter_scale=1; point_separation = flip_res
- `v@v = -normalize(v@N) * ch("flow_scale");` — initial inward velocity on scattered droplets
- **FLIP Object** — particle field, resolution from control null parameter
- **Static Object** (DOP): subgeo path + volume collisions + proxy_volume
- FLIP Solver settings: surface_tension=2, gravity_y=−2, density=200, timescale
- Stick-to-collision: stick_scale=1, max_distance=1 voxel
- **Store Rest SOP** + **Extract Rest SOP** — for velocity field that returns to rest position
- **Volume Rasterize Attributes** — create velocity volume from point field
- **Volume Source** (DOP): "source smoke" mode → velocity sticker
- Stick control field VOP: `fit(noise(P*freq), min, max, 0, 1)` → stick attribute on VDB surface
- Viscosity=1 in FLIP Solver → physical property
- **Particle Fluid Surface** → Gaussian smooth 3 iters → Convert VDB → normals + Attribute Blur 5 iters

### Difficulty
Intermediate–Advanced

### Houdini Version
H19

### Tags
[flip, fluid, droplets, surface-tension, stick-field, velocity-field, vdb, collision, pscale, intermediate-advanced]

---

## Related Tutorials
- tutorial-lipstick-part-1-modeling.md (source lipstick geometry)
- tutorial-lipstick-part-3-rendering.md (Octane render of this scene)
- tutorial-pink-bubble-part-1.md (FLIP/fluid surface effects)
