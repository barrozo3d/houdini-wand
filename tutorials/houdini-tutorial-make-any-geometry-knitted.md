---
title: Houdini Tutorial: Make Any Geometry Knitted
source: YouTube
url: https://www.youtube.com/watch?v=mTnQji8a8nw
author: PolygonCGI
ingested: 2026-06-11
houdini_version: "Not specified (H20–H21 UI)"
tags: [sop, vop, modelling, procedural, curves, attributes, rendering, redshift, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tutorial-make-any-geometry-knitted/
frame_count: 12
---

# Houdini Tutorial: Make Any Geometry Knitted

**Source:** [YouTube](https://www.youtube.com/watch?v=mTnQji8a8nw)
**Author:** PolygonCGI
**Duration:** 27m27s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro. How to make any object knitted [0:00]
**Transcript:** Hi guys! Today I'll show you how to turn almost any object into a needed one.  We'll see how to transfer textures, patterns, even colors from our geometry onto the needed surface.  For this tutorial I'll use the skull as an example and we'll build the setup from scratch and then we'll try to render it in Ritchift.  So let's dive into Vadini!  Let's start from the creating Geo container and we'll name it skullnit, go inside.  I got a reference image from Pinterest that shows how the needs should look.  And if you break down the problem, as my teacher really on says, we can split a stitch into two parts.  We measure one half, then shift it up or down, mirror it and that Geo is a clean, needed loop.  Later we'll copy this across a grid.  So let's do it!  I already have half prepared, so let's mirror it.  Let's make a knot mirror.  But before we need to use a match size to perfectly unline it on X axis.  Now it's perfectly unlined on X axis.  Now mirror.  Mirror is great because it teaches the points but not polygons.  If you see it's two polygons in primates.  To fix that we can add polypast and now we got a simple primate.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_000.jpg

### Creating the first loop, mirror, and basic knit structure [1:50]
**Transcript:** Also we can add some procedural control before mirror.  We can add a curve knot.  It's kind of like a dream passing after effects.  That way we can control the stitch width later.  Like here.  Now we can add another one, match size to control the scale.  Let's set up it around 0.2 in e-rig axis.  Next we use copying transfer.  Let's shift it by minus 0.5.  And now we got a closed stitch system.  Now we can use a grid.  Let's reuse the size.  1.05.  Now we use points from volume.  It's very handy because in one slider we can set the density.  Also we can put a check mark to add a peak scale attribute.  But by default it's multiplied by 2.  We need to turn it by 1.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_001.jpg

### Copy to points, scaling and offsets [3:39]
**Transcript:** So we'll copy the same peak scale.  Now let's add a copy to points.  Now we have already our neat copy.  We can apply one more polypast to stitch another one.  Primitives.  Let's load the scale.  We need to clean up a bit from unused attributes.  We need to have UVVs and normals.  Later let's add for each connected pieces.  We're using connectivity with UV.  And that's give us each UV island and class attribute.  If we look we can see that we have seven parts.  And for each of them we represent a class attribute.  It's like an ID from 0 to 6.  That's our trick.  We basically flattened this 3D model into 2D UV space.  And we cut out neat pattern there.  And then project back onto 3D scale.  Okay let's move on and add a vertex split node.  Put a UV here as an attribute.  Then we use attribute swap.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_002.jpg

### Attribute swap: projecting mesh into UV space [5:52]
**Transcript:** We are swapping a P position with UV.  Boom the model is flattened.  Then divide node ends later on.  Now we can create nodes.  We will name it as mesh 3D space.  Here will be mesh UV space.  And the last one will be mesh borders UV space.  Now we need to add a little wax code.  I also have it ready.  We put in first input we use in a neat grid, second mesh, third one UV mesh and fourth our borders.  We need to transform our grid in UV space like from 0 to 1 by x axis.  Let's use much size to move it properly.  Let's align it by x axis and on grid by minimum.  Now we have a representation of UV space.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_003.jpg

### Adjusting UV representation and scaling the model [7:44]
**Transcript:** Also we need to reduce size of our skull a bit.  0.1, 0.01.  Here we create a knot clip.  Deleting all below the plane.  Later on, the last one will be using attribute swap.  Here we use attribute rest.  Now we convert in rest to P position.  Here is our part of our head.  Our neat is glued onto the skull surface.  We can reduce a bit of point separation.  The first part of our setup is completed.  We have a perfectly aligned neat on our skull.  Now we can try to transfer our texture by attribute transfer.  Also we need to create attribute from map to load our texture as an CD attribute.  Now we can transfer colors to one of our neat surface.  Also we can add some subdivide to increase the quality of our colors.  I almost recommend you to increase polygon count.  It could be also like in 2.  Multiply it in 2 times.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_004.jpg

### Sweep node: generating strands instead of tubes [10:01]
**Transcript:** Now we are using a sweep knot.  But we are not using tubes.  We will be generating strands.  But we need to make sure that copy to point keeps be scale.  By default it isn't.  Otherwise the sweep will mess it up like here.  Once it is fixed we get nice neat strands wrapping around.  Like our pscale multiplying by this radius value.  We can add some variation with the rest attribute.  So our lines will run the measly offset of each other.  Let's add quality of our fibers.  So let's add rest.  Later we add in attribute whoop.  We name it rest random.  Dive in.  We bind in attribute rest.  Choosing a three forward vector.  And we can add it to position.  And mix.  We can only use a mix.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_005.jpg

### Working with values and attributes [12:11]
**Transcript:** So if we put value one,  it going closer to our rest attribute before the sweep.  By this we can create a bit of randomization.  We add a random.  Also we can create some feed range.  And put it on bias.  Now area of our primitive is randomly offsetting from the center.  And we can control this effect using our feed range.  Next we can add a bit of noise to avoid perfectly straight lines.  And that gives us more natural sweeter look.  We need to add subdivide also here to round a bit of our lines.  And now we can create another one attribute whoop.  Call it Carl noise.  Let's add Carl noise.  Also we need a p-scale.  But sweep, deleting p-scale by default.  So we need to return it back.  Let's go back.  Make a rebrand.  Put p-scale.  And put the flow.  Also random.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_006.jpg

### Randomization: seed and variation for loops [14:32]
**Transcript:** Add some seed.  Like 155.  Wait around.  We divide in our position by p-scale.  We need to convert it to vector 4.  Let's change it on 4D noise.  Let's put it in position.  Let's create add.  We can add position.  And make it a bit complicated.  We use multiply and multiply in our numbers.  But we can also increase the randomization effect.  Here we will reduce by half.  And now we need power node to adjust our effect if we need it.  And now that's all we are combining.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_007.jpg

### Adding noise and controlling amplitude/roughness [16:08]
**Transcript:** Multiply.  Our noise, our p-scale, and also randomization per curve.  And now we can add it to our position.  And let's promote some parameters.  Let's go up and see how it works.  It's a bit of noise.  Let's decrease it.  Decrease the roughness.  Now we can see our fibers.  It has a look like more sweet rule.  Later we will make our shader like hairs.  So we need to make our normals.  Let's create normals from using rest attribute.  And we will subtract our position.  And we will need later to normalize it.  So we use in rest and subtract in it from minus p.  We use in normalize.  Let's rename it as calculate normals.  We can preview the width of our fibers using attribute rename.  We need to rename p-scale to width of attribute.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_008.jpg

### Adjustments and refinement [18:19]
**Transcript:** We need to go up using miswriters tab and use checkmark on shade over curves in report.  Now we can see a representation of our fibers for preview.  Let's reduce our width a bit.  Let's multiply it like 0.1.  Maybe a bit more 0.05.  Now we can rename it back.  We can put it back like width to p-scale.  Also we can put no.  There will be our render node.  Let's call it skull out.  Let's put a flag render flag here.  That's one will be for preview.  Now we can move to the render.  Also I prepared some hj.  And you can use it to create what I'm showing you.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_009.jpg

### Different knit types (like chainmail variation) [20:25]
**Transcript:** And using like two types of need.  Like a chainmail with different settings.  It's fully prepared setup.  You can use it for any kind of geometry.  But you need to have one geometry for one setup.  Because different parts of geometry needs to be created in different setups.  That's the main role in this setup.  For example, if you have a man with a bottle or something,  you need to prepare differently man and then a bottle.  So if you need it, you can download it from the link below.  I found some mistake.  We put a divide node.  But we didn't put anything.  We need to uncheck convex polygons and also enable remote shared edges.  And on the ends node, we need to put a role with the shared edges.  This keeps you border's clean for cutting.  Now we can go to the trading.  Let's add some dome weight.  We'll add some studio HDR.  We'll add some materials.  Let's make it skull.

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_010.jpg

### Material setup and Redshift render settings [22:30]
**Transcript:** We need to put it on material top.  Also, we need to put a check mark to render it as a stretch.  Also, we decrease desolation sub-devices and put it 0.25 to global scale multiplier.  We'll create a camera.  Like from this view.  Let's create a redshift node output.  We put our camera here in the render node.  Let's minibit.  We'll use hair shader.  Let's delete the standard one.  Let's add hair.  We need to transfer our color attributes.  Let's use redshift point attributes.  Let's put it in diffuse color.  We put it white color in reflection.  We don't need transmission.  Add a franel.  Let's make a bit of offset of our angular shift.  Let's adjust a bit of fire.  We'll add a primary reflection weight.  We need to diffuse for sure.  We have a texture and colors.  Also translucent.  For softer light, we open our rendshift render view.  I like to use post effects.  Let's open it.  Let's add a bit of exposure.  Let's add a bloom.  Also, let's adjust color curves.  Let's add some contrast.  Let's move the color.  From here, it's just tweaking.  Maybe you want to add bigger features.  Maybe you need different colors or extra noise.  It's all adjustable.  For example, we can use color ...

**Frame:** tutorials\frames\houdini-tutorial-make-any-geometry-knitted\frame_011.jpg


---

## Structured Notes

### Core Technique
UV-space projection trick to wrap a procedurally built knit stitch pattern onto any arbitrary geometry: flatten the target mesh into 2D UV space via `attribswap` (P ↔ UV), tile the knit grid in that space with VEX, then project back to 3D — combined with `sweep`-based strand generation and Redshift hair shader for final rendering.

### Summary
A 27-minute tutorial by PolygonCGI building a fully procedural knitted-geometry effect on a skull. The core insight is using UV connectivity + attribute swap to project a tiling knit stitch (built from `mirror`/`polyfuse`/`copytopoints`) onto any mesh surface. Strands are generated via `sweep` with `curlnoise` variation and a `rest` attribute for fiber randomization. Final render uses Redshift's hair shader with color transferred from the original skull texture. Frames confirm: final render shows a colored crochet skull; workflow shows knit grid in UV space and fiber preview with Cd color transfer.

### Key Steps
1. Build half-stitch curve → `matchsize` to align on X → `mirror` SOP (welds points, not polygons) → `polyfuse` → single primitive loop
2. `curvewarp` SOP — procedural stitch width control
3. `copytopoints` with offset 0.5 → closed stitch pair; tile on `grid` SOP (size ~1.05)
4. `pointsfromvolume` SOP — set density via single slider; enable pscale attribute (set multiplier to 1, not default 2)
5. `copytopoints` — copy stitch tile to grid points; `polyfuse` to merge; clean unused attributes (keep UV + N)
6. `connectivity` SOP (UV mode) → generates `class` attribute (UV island ID, 0–6)
7. `vertexsplit` SOP on UV attribute → `attribswap` SOP: swap P ↔ UV → mesh flattened into 2D UV space
8. VEX wrangle — map knit grid into 0–1 UV space; `matchsize` to align on X minimum
9. `attribswap` back → restore 3D positions; knit now conforms to skull surface
10. `attribfrommap` SOP — load skull texture as `Cd`; `attribtransfer` → transfer color to knit surface; `subdivide` for smoother color
11. `sweep` SOP — strands mode (not tubes); ensure copytopoints preserves pscale; add `rest` attribute
12. `attribvop` — `curlnoise` for fiber curl; 4D noise driven by P/pscale for per-curve randomization; control roughness/amplitude via promoted parameters
13. `attribvop` — compute normals from rest: `normalize(rest - P)`
14. `attribrename` SOP — rename `pscale` → `width` for Redshift hair curve rendering; enable "Shade Open Curves" in Redshift object settings
15. Redshift hair shader — diffuse + translucency + Fresnel reflection; `rsPointAttributes` node to drive diffuse color from `Cd`; post: exposure, bloom, color curves

### Houdini Nodes / VEX / Settings
- `mirror` SOP — welds points; follow with `polyfuse` for single primitive
- `matchsize` SOP — align to X axis minimum
- `curvewarp` SOP — stitch width control
- `copytopoints` SOP — offset 0.5 for stitch pair; preserves pscale (check setting)
- `grid` SOP — size 1.05
- `pointsfromvolume` SOP — density slider; pscale multiplier set to 1
- `connectivity` SOP — UV mode → `class` attribute (island IDs)
- `vertexsplit` SOP — split on UV attribute
- `attribswap` SOP — swap P ↔ UV (flattens mesh to 2D)
- VEX wrangle — UV-space grid mapping
- `attribfrommap` SOP — texture → Cd attribute
- `attribtransfer` SOP — color from skull to knit surface
- `subdivide` SOP — increase polygon count ×2 for color quality
- `sweep` SOP — strands mode; scale by pscale radius
- `attribvop` — `curlnoise`, 4D noise, `rest` attribute, normalize
- `attribrename` SOP — pscale ↔ width
- `divide` SOP — uncheck Convex Polygons; enable Remove Shared Edges
- Redshift hair shader — diffuse, translucency, Fresnel; `rsPointAttributes` for Cd
- Redshift post: exposure, bloom, color curves, contrast

### Difficulty
Advanced

### Houdini Version
Not specified (H20–H21 UI)

### Tags
sop, vop, modelling, procedural, curves, attributes, rendering, redshift, intermediate, advanced

---

## Related Tutorials
- [[vops-02---random-noise---houdini-beginner-tutorial]] — curlnoise and noise VOP patterns used for fiber variation
- [[vops-04---geometry-interactions---houdini-beginner-tutorial]] — attribtransfer geometry interaction technique
- [[model-a-procedural-flower-houdini-tutorial]] — similar copytopoints + procedural surface distribution approach
- [[houdini-uv-unwrapping-fundamentals]] — UV concepts foundational to the UV-space projection trick
