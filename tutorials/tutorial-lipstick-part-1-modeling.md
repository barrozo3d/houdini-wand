---
title: [Tutorial] Lipstick. Part 1. Modeling
source: YouTube
url: https://www.youtube.com/watch?v=Zqle_HOS7Jg
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "H19"
tags: [modeling, revolve, boolean, trace, logo-emboss, vdb-remesh, uv, bevel, subdivide, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-lipstick-part-1-modeling/
frame_count: 4
---

# [Tutorial] Lipstick. Part 1. Modeling

**Source:** [YouTube](https://www.youtube.com/watch?v=Zqle_HOS7Jg)
**Author:** Alexander Eskin
**Duration:** 18m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, to make a lipstick with it, to model a lipstick. So let's start with a June out, call it lipstick geo source. It's going to be gray, and I'm inside. Let's switch to frontal view and use curve polygon to draw a shape for the future revolve node. Something like this. Now let's enable snapping, grid snapping, and move the points around a bit. These two at least. And this one. Turn off the snapping. Let's revolve. Let's clip the top part. Because otherwise there's going to be a bit of an overlap. And it's easier to fix it right now rather than after the revolve node. Other than we subdivide it here, fuse it here. And we need to fire subdivisions for later purposes. For the field. For the bottom part. We need to cut the tip using a bullion. And we're going to use just the box. Stretch it a bit. Transform it. Turning around 55 degrees angle will be fine. And just eyeball it. 6131.544. Just for example. Bullion and transform rotated 90 degrees y axis. Okay, that's good enough. I want 0.56. I think we came through the same number. Anyway. Now we need the logo. We don't really need UVs right now. It's distracting. Okay, we just turn them off. For now, now we need the logo. When we use the trace node, choose the loaded eSynLoran logo. My logo is on the alpha channel. So I need to switch the channel for alpha. And now I need to do a bit of a tweaking to fix these parts. The laser sample with the 0.001 dimensions. I'm going to use the whole node. Let the fix the holes. Also we need to divide. We need to divide the future bending of the thing. We check convex, check breaker and enter 0.031. No, let's roll. 0.031. Like that. Now we're going to move these logo accordingly. So it will be somewhere on a reasonable part of lipstick. Look here. Now we're going to use a racer. Project the logo onto the lipstick. So we have these sticking out points. You can use the clean node to fix it. There we are. This looks a bit better. Now we need to lift the thing a little bit. Otherwise when we got a bullion, subtract the logo from the lipstick. These polygons will not intersect with one another and it's going to be messy. So to fix that, we need to lift the logo a little bit. Like 0.01. Then we're going to use polygons. We're going to use the global transform. We're going to extrude it by minus 0.025. Then check out the back. Use another bullion to cut the thing. Then subtract. Okay. Subjecting geometry B from geometry A or you can rewire it. So now we have this crude geometry. And we need to go with crude geogie. Now we need to remesh it to a BDB and back to polygons. BDB from polygons, the resolution should be a bit bigger. 0.0015. Smooth SDF. We need to use the iteration by 1 because it's smooth too much. Convert BDB back to polygons. EA. It looks okay-ish. I'm not sure that the logo should be as high as it is right now. I draw the move a bit lower like 0.65. Yeah, maybe. But with the wadini procedural workflow, you can do it at any time. So there's that. I think it's fine. Now, perhaps we can smooth it out a little bit more. You should not do smooth normals. We need to add normals to points. Otherwise, attribute blur won't be able to smooth it out because it works on the width of points. Adds with blur normals to 5 iterations and they're going to look better. Not pristine, but better. And without render resolution, I don't think it's going to be a problem. Unless you want to render it like this close. But that's not the goal of this lesson. You need a UV and a new UV. Okay, I can put it here. Syllentable projection and initialize is going to be fine. I mean, I'm using the UV for this only because I couldn't figure out how to map the flakes shader to the object coordinates. It didn't work. I don't know. So if you know how to do that, you can leave without the UVs on this lipstick. It's going to be fine. Maybe you can tell me in the comments how to do that. So the next thing we need to do is to model the surrounding. What is it? Case. I don't know. It's the tube. The tube extruded. Click Output Back. Choose some distance. Point 4. So, Pollux Trude then Fully Bevel. We need to change the fillet shape to Cree's. Divisions 2. Distance 0.2. Turn on the exclusions. So, there won't be any bubbling happening here on the side. And we need to fuse these points at these two. They're overlapping ones. We don't see them, but we can tell that they are there. I don't know why there isn't any red colored design for overlapping points here. But I don't know. Maybe I don't know. And it exists. Anyway, we need to fuse them. And we need to pull the bevel again. Now, with the round shapes, with two subdivisions, and the distance should be 0.011. Again, we need to turn on the exclusions. Ignore flat edges. This is OK. Nothing is overlapping. And now we can subdivide it. And then, merge them. This is fine. Anyway, we have to fix the videos here. And we'll increase the subdivisions here. The radius should be 0.8. You know, 0.85. Probably we need to move it lower. This is an illidivized method, by the way. I don't know why I'm doing this. I just need to preview here and render it here. I'm going to just eyeball it. Otherwise, the refresh rate would be too slow to bear. Now, she's still lower now. Well, something like that. Maybe just move it with much size. It would be easier. Much size, lacks. OK. So we need another one. Another layer here. Because this one is metal. This should be plastic. And this is the lipstick itself. There shouldn't be any holes. Just duplicate it and tweak the radius scale to right now. That's about right. And we should move it a bit lower. Like this. Merge it again. Also, there should be U.V. projections here as well. cylindrical. Initialize here as well. And maybe add numbers. So the merge node will get crazy. I mean, it's not necessary. It should probably work as is, but just to be sure. Well, no one's going to notice that this one intersects with the lipstick. So let's leave it as that. I'd like to create materials straight away. Just place hold the materials. We need a lipstick. It's going to be red. For a preview purpose. Then we need metal. It's going to be gray. We're going to need this thick dark. It's going to be dark. I'm also going to need the background material. It's going to be light. And a water shader for our droplets. It's going to be blue. That's it. Now we're going to apply lipstick shaders just right here. The outer material is metal. The inner one here is plastic. And the lipstick itself is lipstick. Now it's so fun and colorful. We're going to create a null node for our expert. Out lipstick. And go to the object context and create a camera. Attach it to null. Turn off selectable. We need to select the cameras in the viewport. At least I didn't like it. And move the camera on the ZXS2-5. Focal length. Switched to Focal length 200. Check out. Oh, this is terrible. The proper aspect ratio. The 80 by 90. 20. And this should be probably at 7. And we should move it a bit higher. As high like this. But to 0.5. Yeah, this is nice. Maybe it's too close. Maybe too close. 8. Well, all depends on your preference. It's not that important. Anyway, let's make a background with just a plane. Color, red, create. XY plane, rotate 180. Now it's going to do. And move it backwards. Minus 5. Check it out. Oh, good enough. I think that's it for the first part. In the next part we should create the droplets.

**Frame:** tutorials\frames\tutorial-lipstick-part-1-modeling\frame_000.jpg


---

## Structured Notes

### Core Technique
Procedural lipstick modeling: curve-to-revolve profile, Boolean tip cut, Trace logo embossed via Boolean subtraction (with VDB remesh to clean up), PolyBevel/Subdivide case tube, cylindrical UV, placeholder materials. Part of a 3-part series (Part 2: FLIP droplets, Part 3: Octane render).

### Summary
18m30s modeling tutorial by Alexander Eskin. Builds a complete lipstick product shot asset procedurally. Lipstick body: polygon curve drawn in front view → Revolve → clip overlap → Subdivide → Fuse; tip cut with Boolean (rotated box ~55°). Logo: Trace SOP on PNG alpha → Resample → Hole SOP → Divide (convex, crease); Raytrace project onto lipstick surface; lift 0.01 → PolyExtrude inward −0.025 → Boolean subtract → VDB remesh (res 0.0015, Smooth SDF 1 iter, Convert back) for clean topology; Attribute Blur normals 5 iters. Metal case tube: PolyExtrude (output back) → PolyBevel (crease, divs 2, dist 0.2, exclusions) → Fuse → PolyBevel (round, dist 0.011) → Subdivide. Cylindrical UVs on all parts. Placeholder shaders: lipstick red, metal gray, plastic dark, background, water. Camera: 200mm lens, portrait aspect ratio.

### Key Steps

**1. Lipstick Body**
- Front view: Curve (polygon mode) → draw profile
- Grid snap to align key points
- **Revolve SOP** → clip top overlap → **Subdivide** → **Fuse**

**2. Tip Cut**
- **Boolean SOP**: subtract a rotated Box (~55°, scaled to cut diagonal angle) from lipstick → eyeball position
- Note: Boolean transform 90° rotation on Y after position

**3. Logo Emboss**
- **Trace SOP**: load PNG, channel = Alpha; **Resample** step=0.001
- **Hole SOP**: fix topology gaps in traced logo
- **Divide SOP**: convex=on, crease=on, crease angle=0.031
- Position/rotate logo onto lipstick surface
- **Raytrace SOP** (or Ray): project logo onto lipstick surface
- **Clean SOP**: fix sticking-out points
- Lift logo 0.01 in normal direction (ensure polygon intersection for Boolean)
- **PolyExtrude** logo: distance=−0.025 (inward), output back=on
- **Boolean SOP**: subtract logo from lipstick
- Remesh via VDB: **VDB from Polygons** (resolution 0.0015) → **Smooth SDF** (iterations=1) → **Convert VDB** → clean mesh
- Adjust logo vertical position (~0.65) using procedural parameters

**4. Surface Cleanup**
- Do NOT use "smooth normals" — use **Add Normals to Points** first (point normals, not vertex)
- **Attribute Blur** on N attribute: 5 iterations → smoother appearance at render res

**5. UV Mapping**
- **UV Project SOP**: cylindrical projection, initialize
- Note: cylindrical UV needed because author couldn't map flake shader to object coordinates

**6. Metal Case (Tube)**
- **PolyExtrude**: output back=on, extrude distance=0.4
- **PolyBevel** 1: fillet shape=Crease, divisions=2, distance=0.2, exclusions=on (prevent bubbling at joins)
- **Fuse** overlapping points from bevel joins
- **PolyBevel** 2: fillet shape=Round, divisions=2, distance=0.011, exclusions=on, ignore flat edges=on
- **Subdivide** → **Merge** with lipstick body
- UV: cylindrical projection, initialize

**7. Plastic Inner Tube**
- Duplicate case geo → adjust radius scale slightly smaller → position lower → UV + Merge

**8. Placeholder Materials**
- Material Builder nodes: lipstick (red), metal (gray), plastic (dark), background (light), water (blue)
- Apply per-object in material node

**9. Camera**
- Null OBJ → Camera parented to null; selectable=off
- Focal length=200; aspect ratio 80:90 (≈9:16 portrait); Z≈8, Y slightly above lipstick

**10. Background**
- XY plane Grid, rotate 180°, translate Z=−5

### Houdini Nodes / VEX / Settings
- **Curve SOP** (polygon) + **Revolve SOP** + Clip to clean overlaps
- **Boolean SOP** — subtract B from A; use for tip cut and logo emboss
- **Trace SOP** — alpha channel, resample=0.001
- **Hole SOP** — fill topology holes in traced curves
- **Divide SOP** — convex=on, crease=on, angle=0.031
- **Raytrace / Ray SOP** — project logo points onto surface
- **Clean SOP** — remove stray/overlapping points
- **PolyExtrude** — distance=−0.025, output back=on
- **VDB from Polygons** (res=0.0015) → **VolumeBlur/Smooth SDF** (1 iter) → **Convert VDB** — remesh after Boolean
- **Add Normals to Points SOP** — required before Attribute Blur on normals
- **Attribute Blur** on N — 5 iterations for smooth shading
- **UV Project** — cylindrical, initialize
- **PolyBevel** — crease shape for hard edges, round shape for final smooth; exclusions=on; ignore flat edges
- **Fuse SOP** — clean coincident points after bevel
- **Subdivide SOP**

### Difficulty
Intermediate

### Houdini Version
H19

### Tags
[modeling, revolve, boolean, trace, logo-emboss, vdb-remesh, uv, bevel, subdivide, procedural, intermediate]

---

## Related Tutorials
- tutorial-lipstick-part-2-flip-sim.md (droplet FLIP sim on this model)
- tutorial-lipstick-part-3-rendering.md (Octane render of this scene)
- tuna-can-procedural-modeling-and-rig-with-kinefx.md (procedural SOP modeling techniques)
