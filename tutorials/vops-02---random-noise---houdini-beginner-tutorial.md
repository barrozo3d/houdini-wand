---
title: VOPS 02 - Random & Noise - Houdini Beginner Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=mORz1y05T7E
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Not specified (H19–H21 UI)"
tags: ["vop", "sop", "noise", "random", "attributes", "procedural", "beginner"]
extraction_status: complete
frames_dir: tutorials/frames/vops-02---random-noise---houdini-beginner-tutorial/
frame_count: 0
---

# VOPS 02 - Random & Noise - Houdini Beginner Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=mORz1y05T7E)
**Author:** Voxyde VFX
**Duration:** 45m51s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Random & Gaussian Random [0:00]
**Transcript:** Welcome to Intro to Vops Part 2, Random and Noise.  In almost any kind of VFX shot, we will need variation in the way the simulation behaves.  This is achieved through adding noise and randomness to various attributes.  Now we can go over a very important node which is going to be the random node.  So I have a simple setup here, basically we have a grid, which has quite a few subdivisions  and then I have a sphere.  Then we are using this switch node so we can easily switch between these two types of  geometries.  So we can see how the random will affect different types of geometry.  Then we have a scatter, so at any point I can turn this on and off by using Q.  So we can either see how this works on geometry or we can see how it works on just simple  points.  And then finally we also have a color, just so we don't have the black points.  And also I will press D in my viewport and let's go to background and I will just change  the color scheme here to dark.  So we can see this a little bit better.  So we will go ahead and drop an attribute of op and let's dive inside.  So the random is actually a very simple node.  If I drop this, we can see that we have this pause input over here ...


### Turbulent Noise [11:49]
**Transcript:** So the random node does have its place.  But if we want something a little bit more complex and with more options and interesting  patterns, we are going to use a noise.  I'll go ahead and let's get rid of all of these.  So we have the same setup here which is going to be this grid or this sphere.  And let's go ahead, let's maybe work on our sphere for now.  So I will set the switching put to one and I'll disable the scatter, leave the color on  and we have our attribute pop.  And let's go ahead and let's do a turbulent noise.  So let's drop this here and just like the random is going to need some values from where  to generate these noise values from.  So 99.9% of the cases we are going to use the our own position.  So I'm going to plug the P into the position and by default the turbulent noise is going  to give us a signature of 1D noise.  Let's go ahead and take a look at this 1D noise and we will export this to our color.  Just so we can preview this in our viewport and maybe I'll press D and I'll set the background  back to a light value.  So we have this nice pattern and we can play around with the frequency and the amplitude  here all this is doing is basically just doing a ...


### Anti Aliased Flow Noise [19:39]
**Transcript:** can only animate this noise by using this offset value here which is essentially just shifting  basically the positions over one of the x, y and z directions so no matter how we animate the  noise by using the offset we are always going to have this sort of directional movement so if I want  to evolve the noise over time we can use an anti-aliased flow noise so if I drop this let's search  for anti-aliased and let's use the flow noise version which gives us a couple of extra properties  and if I were to let's plug our p inside the position and if I were to replace our turbulent  noise we can see that we can get the same result let's also make sure that this will be a 3D  output signature so let's switch this to a 3D noise so this kind of looks the same as our  turbulent noise but now we have a couple of options here a couple of extra options which are  going to be the flow and the flow rate so I can use this flow value to animate our noise  and I can simply plug our time into this flow value and now if I look at the animation  we can see our noise is moving but it doesn't have any particular direction and now our flow rate  if I set this to a value of 2 so if I increase this the mo...


### Curl Noise [24:21]
**Transcript:** this flow noise and I will do a curl noise and I will plug the result of this vector to vector 4  inside our pause and when I do this we can see that this the inputs here switch from green to yellow  so it automatically got set to a signature 4D noise so this is also something worth knowing and I will  set the noise type here to simplex which is going to be my favorite one and I'll get rid  of this connection and let's add this and I'll actually get rid of this turbulent noise and let's  add our curl noise so this is again sort of similar to the flow noise and by having this 4D input  we can see that we also have animation so the same rules will apply here as I change the frequency  I can decrease the speed here if I set the fourth component to a lower value so we can do something  like this we can see I'm not sure how noticeable this is in the viewport let's maybe set this  to a point display if I play the animation we have these straight points that are flying around  our geometry and this is because of this step size here by default this is a very very low value  so if I just increase this a bit to maybe a value of 0.01 we can see that this actually got rid  of that flickering s...


### Worley Noise [28:09]
**Transcript:** also find this type useful for the whirling noise let's maybe go up and I will switch this let's  leave this as a sphere but let's work on the geometry so I will turn off the scatter node let's go  back inside and let's maybe just get rid of all of these start fresh and we will drop down the  whirling noise so we have sort of the same inputs we can generate this from our position  and we have a lot of different outputs over here so if I plug this this to one value so our first  output inside the color we can preview what this noise does for us and essentially what the  whirling noise does it scatters a bunch of points all over the geometry and it computes the  distance from those points so this is why we are getting this sort of cell like pattern and we can  change the way this distance is being calculated so we have this however this is pronounced and then  we have Manhattan and then we have another one that I'm not gonna dare to pronounce but we have  these three methods to generate this distance value but more often than not probably 95% of cases  it's going to be the first one which is again I'm not gonna try to use it again I don't know  but anyway it's this one it's the first...


### Relative Bounding Box [38:37]
**Transcript:** the next node that I want to introduce is going to be the relative to bound in box node  and this isn't directly related to the random or any noise function but I didn't know exactly  which category I should put this so I might as well talk about this here this is one of my  all-time favorite nodes and let's just do another attribute verb so we can start fresh and I will  just point this scatter here so let's remember that we are either working with a grid or a sphere  and we have the option to turn the geometry into points so let's go to our attribute verb and let's  work with just geometry for now so I will turn off the scatter and inside here we can drop the  relative to bound in box so what this node essentially does is it's drawing a bound in box around  any object that we have and it's returning the x, y and z value so if I go up let's maybe do  another type of geometry let's drop a rubber toy test geometry and let's look at this instead  so if I plug this into a bound stop I can template the result of this by pressing E so this is the  bound in box that it draws over our geometry so the relative to bound in box node is going to return  these dimensions and it's going to map ...



---

## Structured Notes

### Core Technique
Mastering noise and randomness inside `attribvop`: the `random`, `turbulentnoise`, `aanoise` (anti-aliased flow noise), `curlnoise`, `worleynoise`, and `relbbox` (relative bounding box) VOPs — the toolkit for adding organic variation to any attribute in VFX.

### Summary
A 46-minute beginner tutorial dedicated to noise and randomness in Houdini VOPs. Covers the `random` VOP using point number as seed for per-point color or value variation, then progresses through five noise types: turbulent noise (classic workhorse, 1D–3D signatures), anti-aliased flow noise (directional-free animation via a flow input), curl noise (divergence-free fluid-like motion with 4D simplex), Worley noise (cellular Voronoi patterns using distance methods), and finally the `relbbox` (relative bounding box) node for mapping object extents to a clean 0–1 gradient useful for masking effects.

### Key Steps
1. Use `random` VOP inside `attribvop` — feed point number (@ptnum) or primitive number as the seed input; outputs a 0–1 value per point; change Signature for float (1D) or vector (3D) output; use for per-point color randomization (→ Cd)
2. For Gaussian (bell-curve) distribution, use `random` with Gaussian type — values cluster around 0.5 instead of spreading uniformly; useful for natural variation
3. Use `turbulentnoise` VOP — feed P into position input; Signature: 1D for scalar, 3D for vector; key parameters: Frequency (pattern scale), Amplitude (strength), Roughness (detail), Turbulence (octaves); output → Cd for preview or add to P for displacement
4. To animate turbulent noise directionally: increment offset in X/Y/Z using `$T * speed` — creates sliding motion; not suitable for directionless evolution
5. Switch to `aanoise` (anti-aliased flow noise) for directionless animation: set Signature to 3D; wire `global` → time into the **Flow** input; adjust **Flow Rate** to control evolution speed — noise evolves organically without sliding
6. Use `curlnoise` VOP for fluid-like swirling motion: feed a `vectovec4` (vector to vector4, with `$T` as the 4th component) into the position input — this enables 4D animation; set Noise Type to Simplex; increase **Step Size** (e.g. 0.01) to fix flickering; reduce Amplitude for subtle motion
7. Use `worleynoise` VOP for cellular patterns: feed P → position; choose distance method (Euclidean, Manhattan); first output = closest cell distance → Cd or displacement mask; multiple outputs available for F1, F2 distances
8. Use `relbbox` (Relative Bounding Box) VOP — no inputs required; automatically reads geometry bounds; outputs X, Y, Z values mapped to 0–1 range across the object's bounding box; use the Y output as a vertical gradient mask to blend effects from top to bottom

### Houdini Nodes / VEX / Settings
- `attribvop` SOP — container for all VOP operations; run over Points
- `random` VOP — Seed input: @ptnum or @primnum; Type: Uniform or Gaussian; Signature: 1D (float) or 3D (vector); output → Cd or any float attribute
- `turbulentnoise` VOP — Signature: 1D/3D; Frequency; Amplitude; Roughness; Turbulence (octaves); Position input: P; use Offset to animate (directional only)
- `aanoise` VOP (Anti-aliased Flow Noise) — Signature: 3D; Flow input: connect time for direction-free animation; Flow Rate: controls evolution speed (higher = faster); otherwise same params as turbulentnoise
- `curlnoise` VOP — Noise Type: Simplex (recommended); Position: vectovec4 with time as W; Step Size: ~0.01 to remove flickering; 4D input enables temporal animation; output is divergence-free velocity vector
- `vectovec4` VOP — converts vector + float (time) into a 4D vector for curlnoise position input
- `worleynoise` VOP — Position: P; Distance Method: Euclidean/Manhattan; Outputs: F1 distance, F2 distance, cell color; use first output for cellular mask
- `relbbox` VOP — no inputs; reads current geometry's bounding box; outputs X/Y/Z in 0–1 range; use Y output as vertical gradient mask
- `switch` SOP — Switch Input: 0 = grid, 1 = sphere; use to toggle test geometry
- `scatter` SOP — Q to toggle on/off; Total Count: increase for denser point tests
- **Q** — toggle node bypass (enable/disable) in viewport
- **D** — display options; Background: Dark/Light for better contrast in viewport

### Difficulty
Beginner

### Houdini Version
Not specified (H19–H21 UI)

### Tags
#vop #sop #noise #random #attributes #procedural #beginner

---

## Related Tutorials
- [Intro to VOPS - Houdini Beginner Tutorial](./intro-to-vops---houdini-beginner-tutorial.md) — #vop #sop #attributes #math #beginner
- [VOPS 03 - Vector Operations - Houdini Beginner Tutorial](./vops-03---vector-operations---houdini-beginner-tutorial.md) — #vop #vectors #math #attributes #beginner
- [VOPS 04 - Geometry Interactions - Houdini Beginner Tutorial](./vops-04---geometry-interactions---houdini-beginner-tutorial.md) — #vop #attributes #geometry #beginner
- [Intro To Houdini for VFX - Beginner Course](./intro-to-houdini-for-vfx---beginner-course.md) — #sop #dop #vop #vex #attributes #beginner
