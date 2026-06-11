---
title: Model a Procedural Flower | Houdini Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=pIp3cYSBZc4
author: Fifo
ingested: 2026-06-11
houdini_version: "Not specified (H20–H21 UI)"
tags: [sop, dop, vop, vellum, modelling, procedural, curves, attributes, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/model-a-procedural-flower-houdini-tutorial/
frame_count: 10
---

# Model a Procedural Flower | Houdini Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=pIp3cYSBZc4)
**Author:** Fifo
**Duration:** 38m34s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Okay, okay, okay. I heard you guys.  What is the flowers?  You look great.  What is the flowers?  In today's video, we are going to build a procedural flower system.  Let's jump in.  First of all, it is essential to not get overwhelmed by the complex structure.  We will break the flower down into manageable.  Less complex parts and assemble all of them in the end.  The overview of the steps we are going to take in the video are creating this step.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_000.jpg

### Game Plan [0:36]
**Transcript:** We are going to build the blossoms.  We will have a look at the magic behind flowers and their alignment.  We will copy those blossoms and make them bloom over time.  In the end, we will resolve their intersections, whose the volume is over.  And voila, we will have a flower.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_001.jpg

### Flower Base - the stem [1:00]
**Transcript:** We finally arrived in Houdini and let's start by dropping down a geo node.  And we name this thing flower that's divin-side.  And for my stem, I'm going to start by drawing a little curve in here.  So let's drop down a curve node.  Let's switch the view to the front.  And let's make a little S curve here.  Like this hit enter to apply.  And let's go back in our perspective mode.  This thing might be a little small for my taste.  So let's drop down a transform node.  Let's say we scale this thing up by approximately 4.  It's still very pointy and very sharp.  So let's fix this by dropping down a resamble node.  And let's go for something quite small with the tree polygons as subdivision curve.  Cool.  Let's apply our curve view attribute.  So we have a value that runs from the first point from 0, up to the last point,  which gets one and all the stuff in between will be interpolation of these values.  This stem right now is quite flat.  And I want to fix this and give it also a little bit of movement over time.  So for this, I'm going to drop down a group by a range to access our first point of this primitive.  Let's get this out here.  Let's say this is the hour first point.  Point...

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_002.jpg

### Preparing the Blossom [6:15]
**Transcript:** Therefore, I prepared already a little setup in here.  So I modeled two states, a very small one.  Quite a big state of the blossom, which opened up.  I plugged it into a blend shape and animated it over a span of 120 frames to open up.  You also want to build something like this.  And you can be totally creative here and model your own blossoms.  The most important thing is you see it's quite a simple setup.  We are like starting with a sub divided box.  Where we blasted off one side.  And then with a bunch of different poly extrudes.  And I always just selected one edge here.  I tried to get the base shape.  Sub divided it a bit.  Smooth it out.  And then I split the node graph.  And for the small section, I transformed it quite a bit with soft transforms.  And another sub divide.  And I went ahead and basically did the same.  For the opened state of the flower.  The only thing that you need to keep in mind here is that each of the sides,  and you'll see I highlighted the nodes in yellow, which define number of points.  Because this blend shape here needs to have the same amount of points as an input or the shape one.  And the next shape in order for it to deliver the best result...

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_003.jpg

### Natures Magic, Golden Angle and Phyllotaxis [8:43]
**Transcript:** To understand how our blossoms align, we will need to do a bit of studying.  Imagine you are a plant and you want to grow your seeds.  So you have this molecular machinery going on that builds seeds and pops them out.  Then it turns and builds the next one.  But now the question raises.  What is the best angle to occupy the most space?  In other words, what is the most efficient angle with the least gaps?  It's called the golden angle and it appears everywhere in nature.  It derives from the golden ratio of phi approximately 1.618.  If you take a full circle, 360 degrees and divide it by 5 squared,  you will get 137.51 degrees.  This angle has a fascinating property.  When you keep rotating via it, the new points will never overlap.  That's why in nature leaves and paddles spiral perfectly.  Without blocking each other's sunlight, the scientific term for this is filotaxis.  In case you want to give it a little Google afterwards.  Let's jump into Houdini and explain how we will align our blossoms along this stem.  For this, I want to use a point warp.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_004.jpg

### Implementing the golden Angle 137,518 [10:10]
**Transcript:** Let's call this back tour magic.  Wired in and highlighted our normal.  This will be pretty handy in the moment.  Let's dive inside.  I will make it a little bit more room here because now I'm not working from top to bottom,  but from left to right.  I have my normals here which are basically the tangent view attribute but mapped to the norm.  What I want to do with that is I want to use a cross product in order for the normals to not follow the shape of the curve,  but stick perpendicular to this kind of curve shape.  Let's maybe have a little recap what a cross product is.  Back in your math class, I guess you should have learned that whenever you want to multiply two vectors,  let's call them A and B.  You vector that is basically perpendicular to both A and B.  And that's what we're going to use now.  So let's drop down a parameter.  And in here we will call this cross vector.  So this will be our vector B in this example.  Let's make this also a vector.  And we can select whatever we want.  We can use the x direction, the z direction, or we use both of them if we are like a little bit there.  And the size of here.  Let's drop down a cross product in here and we will just multi...

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_005.jpg

### Copy Blossoms and Time Offset [21:26]
**Transcript:** We want to create a peace care attribute.  So I'll just float because this automatically set to peace care.  Let's save you want to ramp attribute.  You want to use the curve.  You attribute here 10 is around.  This time we want to have a zero 0.05 maybe.  Let's make it a peace plan again.  Let's do the same curve we had in our sweep node like this.  And let's attribute combine this with our mask.  So we use our destination is the P scale.  Everyone multiplied.  We want our mask attribute in order for it to grow.  Let's use a add-sop because we are just interested in the points.  So we say the geometry but keep points.  Let's put our normals and check if they are still there.  Yes.  And the blossoms should not start in the middle of the stem but like a little bit more outside.  So let's use a peak stop like this.  Let's put those points away from the stem along the normal by maybe 0.06.  Yes.  That looks quite cool.  If you look at our normals they are gone.  So let's uncheck recompute point normals.  Yes.  That looks perfect to me.  Points to copy to.  And now it's time to come back and get our object merge with the blossom.  We can just use a copy to points.  And here our target ...

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_006.jpg

### Resolve Intersections with Vellum [26:05]
**Transcript:** So how do we solve those intersections?  For this I want to use a valum solver again where we pipe in our blossoms  and then let the valum constraints do their job by solving those intersections.  And I will need one point down here.  Let's say this middle point, group it and we will say this is our attached point which will be then propagated through our system here.  And we can access it in a second.  Let's group it again. Use the points.  Put in a star in this regular expression to really select all the points and let's say pin.  Let's branch this out to a new null object and let's call this blend shape because this is now this blend shape of all of our blossoms together.  And we will reference this null.  So let's copy it already in a second in our valum setup.  In the same valum I want to put down the valum configure a clock.  And in here for the settings I want to have a very very small etch length scale as stretch stiffness of let's say 10 and a band stiffness of 0.001.  These are the settings that worked good for me with the size of the flower but you might fiddle around a bit with that next.  I want to put on a valum constraints so why are everything in and set it not from...

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_007.jpg

### Finishing Touches [31:23]
**Transcript:** And we can also say group expand again.  We can use the same name attach.  The base group is also attached.  And let's just grow this maybe eight iterations.  Let's blast this off.  Then we didn't select it like this.  And let's maybe give this little thickness, laps, ticking and very low value.  Maybe both directions 0.01.  Somehow I have this little viewport back here.  Let's close the viewport and let's get this view back.  Put it up here.  It was better to touch all the area here.  I guess this might be still a bit too thick.  Maybe something like this.  And let's use another subdivide node and attach it all.  And say this is out green pedal.  Let's just add a little bit more detail at the end.  Cool.  And now we need to connect this area to our stem and put this last way our attach group.  Let's point this and then of course one delete the non-selected to be left with this little point.  And let's get rid of all the attributes here.  Delete the non-selected.  Let's delete all the groups.  And let's attach a point wrangle here.  And I want to use a very simple expression, which is i at id equals at ptNum.  Close it so we create a little id attribute for each point.  Because thi...

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_008.jpg

### Outro [37:44]
**Transcript:** And now we have our growing flower structure in here.  I will render a quick flipbook for that.  You modelled yourself quite a complex flower setup.  And you can start playing around with this.  Changing the stem's curve.  Changing the blossoms.  And you will be granted with endless varieties.  I hope you found this tutorial useful.  And we will see each other in the next one.  Cheers and goodbye.  Thank you.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_009.jpg


---

## Structured Notes

### Core Technique
Procedural flower system using phyllotaxis (golden angle 137.518°) to spiral-distribute blossoms along a curve-based stem, with VOP cross-product for correct copy orientation, animated blend shapes for bloom, and Vellum cloth constraints to resolve petal intersections.

### Summary
A 38-minute SOP tutorial building a fully procedural and animated flower. Covers: curve-based stem with `resample` and `sweep`, blossom modeling with `blendshape` for open/closed states, implementing the golden angle in a VOP `crossproduct` for phyllotaxis spiral alignment, `copytopoints` with time-offset `pscale` ramp for staged blooming, and a Vellum cloth solver with pin constraints to naturally push overlapping petals apart.

### Key Steps
1. `curve` SOP — draw S-curve for stem in front view
2. `transform` — scale up ×4; `resample` with "Subdivision Curve" mode for smooth interpolation
3. Apply `curveu` attribute (runs 0→1 along curve) for later ramp-based distribution
4. `sweep` SOP — give stem a circular cross-section; animate stem sway in VOP over time
5. Model blossom separately: `box` → `blast` one face → `polyextrude` selected edges → `subdivide` → `smooth`; duplicate network for closed and open states
6. `blendshape` SOP — animate between closed and open states over 120 frames
7. VOP `crossproduct` between stem tangent (N) and a world axis → perpendicular normal; rotate each blossom copy by `ptnum × 137.518°` for golden-angle spiral
8. `copytopoints` — copy blossom geometry to stem points; `pscale` ramp from `curveu` + time offset for staged bloom
9. `peak` SOP — push blossoms outward from stem ~0.06 along normals
10. Uncheck "Recompute Point Normals" on `peak` to preserve orientation
11. Vellum: `vellumconstraints` (cloth type) + pin "attach" group at blossom base; `vellumconstraintproperty` — stretch stiffness 10, bend stiffness 0.001, small stretch length scale
12. `vellumsolver` DOP — run sim to naturally push intersecting petals apart
13. `groupexpand` — expand attach group 8 iterations for smooth pinning
14. `subdivide` + `polyextrude` (thickness 0.01 both directions) for final petal geometry
15. Point wrangle: `i@id = @ptnum;` — create unique ID per point for downstream control

### Houdini Nodes / VEX / Settings
- `curve` SOP
- `resample` SOP — Subdivision Curve mode, small max segment length
- `transform` SOP — uniform scale ×4
- `sweep` SOP
- `blendshape` SOP — blend value 0→1 over 120 frames
- `groupbyrange` SOP — isolate first point of primitive
- `attribvop` / `attribwrangle` — `curveu` attribute, `pscale` ramp
- VOP `crossproduct` — perpendicular vector from tangent + world axis
- VOP `parameter` node — type: vector, name: "cross_vector"
- `copytopoints` SOP
- `peak` SOP — distance ~0.06 along normals; uncheck Recompute Point Normals
- `add` SOP — keep points only
- `vellumconstraints` — cloth constraint type
- `vellumconstraintproperty` — stretch stiffness: 10, bend stiffness: 0.001
- `vellumsolver` DOP
- `groupexpand` SOP — 8 iterations
- `blast` SOP
- `subdivide` SOP
- `polyextrude` SOP — thickness 0.01, both directions
- Point wrangle: `i@id = @ptnum;`

### Difficulty
Intermediate

### Houdini Version
Not specified (H20–H21 UI)

### Tags
sop, dop, vop, vellum, modelling, procedural, curves, attributes, simulation, intermediate

---

## Related Tutorials
- [[vops-03---vector-operations---houdini-beginner-tutorial]] — VOP cross product and vector math foundation
- [[vops-04---geometry-interactions---houdini-beginner-tutorial]] — Geometry attribute transfer and VOP geometry interactions
- [[intro-to-houdini-for-vfx---beginner-course]] — SOP/DOP/VOP foundational workflow
