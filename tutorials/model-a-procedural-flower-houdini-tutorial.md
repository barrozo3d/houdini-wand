---
title: Model a Procedural Flower | Houdini Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=pIp3cYSBZc4
author: Fifo
ingested: 2026-06-23
houdini_version: "any modern (H19+)"
tags: [procedural-modeling, vellum, wire-solver, copy-to-points, for-each, quaternion, golden-angle, phyllotaxis, sweep, intermediate]
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
**Transcript:** We finally arrived in Houdini and let's start by dropping down a geo node.  And we name this thing flower that's divin-side.  And for my stem, I'm going to start by drawing a little curve in here.  So let's drop down a curve node.  Let's switch the view to the front.  And let's make a little S curve here.  Like this hit enter to apply.  And let's go back in our perspective mode.  This thing might be a little small for my taste.  So let's drop down a transform node.  Let's say we scale this thing up by approximately 4.  It's still very pointy and very sharp.  So let's fix this by dropping down a resamble node.  And let's go for something quite small with the tree polygons as subdivision curve.  Cool.  Let's apply our curve view attribute.  So we have a value that runs from the first point from 0, up to the last point,  which gets one and all the stuff in between will be interpolation of these values.  This stem right now is quite flat.  And I want to fix this and give it also a little bit of movement over time.  So for this, I'm going to drop down a group by a range to access our first point of this primitive.  Let's get this out here.  Let's say this is the hour first point.  Point.  You want to have the point.  You want to select the first point, not the last one.  And let's invert this range.  So now we have this point selected.  In order to make it wiggle over time, let's drop down a volume here.  Vire design.  You can actually leave everything as is.  And let's go directly ahead and drop a volume.  Sover.  Wire everything.  In, let's go ahead and in the forces tab, let's remove the gravity, because we don't want this string to fall down.  Inside, we will add a pop wind wired into the forces.  And let's say, we give it a verses likely amplitude, but a quite big spiral size.  And let's simulate.  And you can see we are dancing around a bit.  But now everything is dancing.  So let's go into our hair constraint.  And we will go to the pin point, and we will select our first point.  And say this is permanently pin at play.  And now the origin stays always the same.  But the rest of our plant is wiggling in the wind.  Cool.  Let's put on a Vellum IO.  And cache this out.  This will significantly speed up our process.  Put your base name, wherever you want it to be.  This will be mine.  And you can hit save to disk.  That should be really, really quick.  And we have a nice little animation.  And of course, you can tweak it to your liking by just coming in here, adding more forces or play around with those.  Did we already set up?  Let's go outside and let's have a look at the geometry spreadsheet.  Because this will be our root, if you want to say so, for our entire setup.  And we have a shhh, a ton of attributes in here.  So we don't need all of them.  Let's drop on an attribute delete.  Like this.  And I want to make sure that I keep my curvy attribute here.  So let's go in here and select curvy.  And to be honest, the rest can be deleted.  So I say delete, non-selected.  And I've just left this curvy and my groups, which is perfect.  Another thing that we might need is...  Let's drop down another resample note, a tangent U attribute down here.  But let's deselect everything because I don't want to resample it.  Because I'm quite happy with this distribution of points.  But I want to generate this tangent U attribute.  And I want to misuse it a bit.  I don't want to use it as is.  But I want to use it as a normal.  So if you come inside here now, you see our normal of the curve.  We always point from one point on the primitive to the next.  And this gives this really the following shape of those normals.  Which we want to leverage in a second.  Then I would say we drop down an null.  And we call this out as the curve.  Which concludes our first section.  Next up is our blossom.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_002.jpg

### Preparing the Blossom [6:15]
**Transcript:** Therefore, I prepared already a little setup in here.  So I modeled two states, a very small one.  Quite a big state of the blossom, which opened up.  I plugged it into a blend shape and animated it over a span of 120 frames to open up.  You also want to build something like this.  And you can be totally creative here and model your own blossoms.  The most important thing is you see it's quite a simple setup.  We are like starting with a sub divided box.  Where we blasted off one side.  And then with a bunch of different poly extrudes.  And I always just selected one edge here.  I tried to get the base shape.  Sub divided it a bit.  Smooth it out.  And then I split the node graph.  And for the small section, I transformed it quite a bit with soft transforms.  And another sub divide.  And I went ahead and basically did the same.  For the opened state of the flower.  The only thing that you need to keep in mind here is that each of the sides,  and you'll see I highlighted the nodes in yellow, which define number of points.  Because this blend shape here needs to have the same amount of points as an input or the shape one.  And the next shape in order for it to deliver the best results.  On both sides match.  It's the same point number.  You can really seamlessly blend between the two states.  Afterwards, assigned UVs to the biggest state here.  Put them into a UV layout.  And then just copied over the UVs to my animation in order for them to stay in place.  And not jiggle around or like being recalculated in each and every step.  Match size it to the origin here.  And attach the null object.  Let's copy that.  And let's go back into our flower modeling.  Let's already prepare an object merge node in here.  Paste this in in order for us to access this animation in a second.  But we will need to do some vector magic in order to prepare our stem to copying all those blossoms over.  So let's take this in the next step.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_003.jpg

### Natures Magic, Golden Angle and Phyllotaxis [8:43]
**Transcript:** To understand how our blossoms align, we will need to do a bit of studying.  Imagine you are a plant and you want to grow your seeds.  So you have this molecular machinery going on that builds seeds and pops them out.  Then it turns and builds the next one.  But now the question raises.  What is the best angle to occupy the most space?  In other words, what is the most efficient angle with the least gaps?  It's called the golden angle and it appears everywhere in nature.  It derives from the golden ratio of phi approximately 1.618.  If you take a full circle, 360 degrees and divide it by 5 squared,  you will get 137.51 degrees.  This angle has a fascinating property.  When you keep rotating via it, the new points will never overlap.  That's why in nature leaves and paddles spiral perfectly.  Without blocking each other's sunlight, the scientific term for this is filotaxis.  In case you want to give it a little Google afterwards.  Let's jump into Houdini and explain how we will align our blossoms along this stem.  For this, I want to use a point warp.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_004.jpg

### Implementing the golden Angle 137,518 [10:10]
**Transcript:** Let's call this back tour magic.  Wired in and highlighted our normal.  This will be pretty handy in the moment.  Let's dive inside.  I will make it a little bit more room here because now I'm not working from top to bottom,  but from left to right.  I have my normals here which are basically the tangent view attribute but mapped to the norm.  What I want to do with that is I want to use a cross product in order for the normals to not follow the shape of the curve,  but stick perpendicular to this kind of curve shape.  Let's maybe have a little recap what a cross product is.  Back in your math class, I guess you should have learned that whenever you want to multiply two vectors,  let's call them A and B.  You vector that is basically perpendicular to both A and B.  And that's what we're going to use now.  So let's drop down a parameter.  And in here we will call this cross vector.  So this will be our vector B in this example.  Let's make this also a vector.  And we can select whatever we want.  We can use the x direction, the z direction, or we use both of them if we are like a little bit there.  And the size of here.  Let's drop down a cross product in here and we will just multiply this vector with one or the vector.  And we can have a look.  If I come in here and I say we just go into the z direction, you can see that our vector is pointing into the x direction afterwards.  And if we cross with just the x vector, our normals will look into the z direction.  I will go for both of them again because then it's a bit more in between.  Okay, but now all of them look in the same direction.  And if you look at flowers, as we just learned in the beginning, everything is aligned according to the golden angle.  So let's get this thing in here.  Let's drop down another parameter.  Call this golden angle.  And let's set this to our 137.0.548 degrees.  Let's a float attribute.  And now we want to rotate each point by this angle for this.  We can access this point number here.  Let's multiply each point with the golden angle.  So the first one will be zero because it's point number zero.  The first one will be exactly the golden angle.  The second one will be twice the golden angle, third fourth, and so on, up the chain.  And now we need to rotate this vector according to this angle.  And if we put down rotate, you see we have two options.  And for this, I want to use the rotate by Quaternion.  And this often scares people, but let me show you that it's actually nothing to be scared of Quaternion.  And we need one for that, as you see here in yellow.  So let's drop down a Quaternion.  Wired in.  And to take away your fear, you can basically memorize it like this.  Quaternion is just a special way to describe how something rotates in 3D space.  Quaternion stores a direction like this.  Access, you want to turn around and the angle.  Okay, so as a rotation, we want to use our normal.  Remember, the normal was just following along the shape, which is perfect to then rotate our newly created cross vectors around.  And then the other input, the angle we will put our golden ratio.  But before we do that, it would be actually good to remap this golden angle.  Because here we are working in degrees and I think the Quaternion in Haudini works with radians.  So let's quickly convert this from degrees to radians, multiplying it by our point number,  putting it into the Quaternion and rotate our cross vector by the Quaternion and then plug it into the normal.  And then you see, you rotate it each and every vector around our base shape by the golden angle.  And this result in this typical flower arrangement that you see all over nature.  Perfect. One last thing I want to do, which later on will become quite handy.  We are going to bind export our normal because we overwrite the normal here.  So we still need to have this kind of tension you attribute.  Let's just call this up.  This creates an up vector.  Let me jump out and also visualize this one.  This still runs along our path here.  And once we copy over our blossoms, this will help orient them better.  Let's save this and let's continue.  Let's get rid of this visualization.  So now that we have all of this, let's prepare our flower a little bit more.  So the blossoms should not start here at the bottom.  So let's give us some safe space down here, which will be just a stamp.  So remember we already basically calculated our first point of the primitive.  We can use a group expand node like this, which we name bottom and our base group.  We will be the first point.  So I light it and let's increase the steps here.  Let's say 125.  The next thing I want to do is I want to grow our plant over time.  And for this we need a attribute that runs through here.  It will drive the thickness of the stem.  It will drive when our blossoms will grow.  And the size of those blossoms in a point,  Wop, like this.  Let's call this create mask.  And here we do it manually, but you can also use the mobs tools or like the pyrosprad node.  And yeah, remap the temperature to a mask attribute.  And let's create it in a manual way, not too complicated.  So let's bind our curvue attribute in here.  And we need two more parameters.  We will need a position, which goes from 0 to 1, like our curvue.  And we will need to have another one that is called width.  Perfect.  So now we will fit our curvue to the destination minimum of whatever we put in,  either with.  So if it's like, let's say, smooth, of course, our curvue value should be always at the lowest point of this kind of smoothness.  In the next step, let's add our position together with our width here in order for our,  yeah, with to follow our position.  And let's use another fit range in here, where this value here gets remapped to our position as this was minimum and our following along as the search maximum.  Let's bind export this thing.  Let's call this mask, plug it in.  Let's jump out and we have these two sliders here.  Let's give it a little bit bigger.  And let's visualize our mask attribute.  So once I start pushing this slider up here, you see we will run through it.  And once I put like something like 0.4, 0.5, and here you see we will make it very smooth and we can vary it quite a lot.  And this will be now something that we animate over time.  And let's do this by on option, click in the first frame here and let's say over 72 frames, we want to arrive.  Maybe not at one, but at 0.9 maybe or 0.8.  Yeah, maybe 0.8 because we never want the top part of the flower also fully grown.  So there should be like this kind of tapering shape of our blossoms going upwards.  This is our mask attribute and to put this to task, we can use an attribute delete just to keep this side of the path nice and clean.  Let's delete everything but the mask and let's rename this attribute from mask to peace care.  And let's use sweep node because this will understand our peace care attribute.  And you see we are running from the wrong side.  So maybe we attach an attribute remap before that you want to use the mask as a mask.  So in the middle let's calculate the range.  You want to use it from 0 to 1 and of course invert it.  And now you see our sweep will understand the peace care attribute and scale whatever we put in here.  By this amount, let's give it some caps like a grid here and let's maybe not make it completely zero but 0.05.  So there's always a little thickness and let's also make this maybe half the size which looks a bit better to my eye.  And in this sweep we can even come in here and tweak this further.  Let's come in here and make this a peace plan for example.  Pull the tip down a little bit more even make it up here, make one here.  So like this, let's linear approach to the growing but a bit more organic shape.  And this we can actually name out, stem, geo, and you see it will grow with our mask.  That's pretty cool.  In here we can of course construct some BBs and we're good to go.  Let's save that and now that we have our stem ready, let's copy over our blossoms.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_005.jpg

### Copy Blossoms and Time Offset [21:26]
**Transcript:** We want to create a peace care attribute.  So I'll just float because this automatically set to peace care.  Let's save you want to ramp attribute.  You want to use the curve.  You attribute here 10 is around.  This time we want to have a zero 0.05 maybe.  Let's make it a peace plan again.  Let's do the same curve we had in our sweep node like this.  And let's attribute combine this with our mask.  So we use our destination is the P scale.  Everyone multiplied.  We want our mask attribute in order for it to grow.  Let's use a add-sop because we are just interested in the points.  So we say the geometry but keep points.  Let's put our normals and check if they are still there.  Yes.  And the blossoms should not start in the middle of the stem but like a little bit more outside.  So let's use a peak stop like this.  Let's put those points away from the stem along the normal by maybe 0.06.  Yes.  That looks quite cool.  If you look at our normals they are gone.  So let's uncheck recompute point normals.  Yes.  That looks perfect to me.  Points to copy to.  And now it's time to come back and get our object merge with the blossom.  We can just use a copy to points.  And here our target points will be our points but everything.  But the bottom.  So I add our object here and let's highlight it.  And you see we already have this kind of tapered shape around it which grows over time.  But all of our flower heads or blossom heads intersect quite a bit and are growing at the same speed which we don't want.  We want the ones at the bottom open up before while the ones at the top still being very very small and in their closed state.  So how can we do this?  And for this there's a very simple and easy trick.  So first of all we need a kind of attribute that tells us in which point we are working on.  So let's drop down for each loop but for each point let's put this in here.  The output with the this one we will need to create this metadata input note because this will create in our details here kind of iteration.  So you see we will have 140 points in total.  In our object merge we want to attach a time shift note that goes in here.  And usually it's used to increase your animation to a certain point.  But what we can also do is like offset the animation by our iteration number.  So for this let's come in here and let's say $F which gives us the current frame number.  And let's subtract our iteration.  So it's on a detail and it's on the for each metadata one input note.  We are interested in the iteration and we need to put it zero down here.  You can do it like this.  You see this will result in a minus but it will result in a different one for each and every iteration.  And we can also come in here and we add a float which we call offset.  Offset. Let's apply it except we have another slider here. Let's put this to one.  Let's copy this parameter and let's paste the reference.  And let's just make sure we put these two things in the brackets.  You saw already if I come down here in my for each loop highlighted and we play it back.  You see everything is growing but then the flowers start to blossom at the bottom  and making their way up the entire shape of the flower.  Just by offsetting each and every point by the iteration number you can also play around a bit with the offset.  But I just leave it like this which is pretty cool.  And then the next step we just need to fix our overlap.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_006.jpg

### Resolve Intersections with Vellum [26:05]
**Transcript:** So how do we solve those intersections?  For this I want to use a valum solver again where we pipe in our blossoms  and then let the valum constraints do their job by solving those intersections.  And I will need one point down here.  Let's say this middle point, group it and we will say this is our attached point which will be then propagated through our system here.  And we can access it in a second.  Let's group it again. Use the points.  Put in a star in this regular expression to really select all the points and let's say pin.  Let's branch this out to a new null object and let's call this blend shape because this is now this blend shape of all of our blossoms together.  And we will reference this null.  So let's copy it already in a second in our valum setup.  In the same valum I want to put down the valum configure a clock.  And in here for the settings I want to have a very very small etch length scale as stretch stiffness of let's say 10 and a band stiffness of 0.001.  These are the settings that worked good for me with the size of the flower but you might fiddle around a bit with that next.  I want to put on a valum constraints so why are everything in and set it not from distance but to into target.  It's our target geometry.  We want to use our points called pin.  The thickness we want to set uniform to our etch length scale 0.02.  Pin type should be soft.  The orientation type should be soft.  And we want to match the animation and those stretch and band differences will work differently than the normal constraint.  So let's set this to 1 and 1.  And what this one means is basically it follows completely the input or tries to be as close to the points that we put in here as possible.  And the value of 0 would tell the valum server that it can go completely nuts and go fully valum.  And everything in between will be a blend.  So let's say like a 0.6 in here.  Well, I mean 60% it should maintain its shape but valum has 40% to do its thing.  And maybe for the band stiffness we get a 0.8 or something like this.  So these two things are a little bit different from another.  And let's drop down a valum server.  At the end highlight the server.  Get rid of the gravity as usual.  Up the sub steps to 2 maybe.  And drop down the constraint iterations to 32.  But you can also fiddle around with these settings a bit.  Let's dive inside and let's use in here a rest blend.  We wired in and we want to update it each frame.  Now we introduced sub steps so we could also update it each and every sub step.  Maybe we do this for the bindings.  We want to use a SOB.  And I hope I still have it in my keyboard.  Exactly this blend shape and yeah, I'd operate on the constraint geometry.  As the constraint group you want to set the band and the stretch group to work on the right constraints.  And now we can dive out and basically hit simulate.  I will do this wide away in a valum log in, lock this in.  Change to my location and let's hit save to disk.  This should take a brief moment but hopefully not so long.  Speed this process up and we see each other once this is done.  Okay now that this is finished let's have a look at it.  You can see our blossoms deviate each other here and here.  Yeah that looks quite cool.  To further enhance this kind of thing can drop down a valum post process via all of them in.  Let's give this some space with blur with a nice little subdivision to have a little bit more things to work with.  Okay there is a little bit of defects here.  Maybe we can introduce a little detangle.  Yeah that worked quite well.  And let's maybe give all the flowers a little thickness here.  0.1 might be more than enough.  Let's go with that.  And let's tweak our setup a little bit more.  Because right now if we template this them here our flowers hang quite in the air.  So of course we need a little cap down here.  So we can come in here, come in here and say group promote.  And I want to use my attach group.  It was a single point if you remember they want to promote it to primitives.  So here we created the point goes through our entire setup and now we promoted it to primitives.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_007.jpg

### Finishing Touches [31:23]
**Transcript:** And we can also say group expand again.  We can use the same name attach.  The base group is also attached.  And let's just grow this maybe eight iterations.  Let's blast this off.  Then we didn't select it like this.  And let's maybe give this little thickness, laps, ticking and very low value.  Maybe both directions 0.01.  Somehow I have this little viewport back here.  Let's close the viewport and let's get this view back.  Put it up here.  It was better to touch all the area here.  I guess this might be still a bit too thick.  Maybe something like this.  And let's use another subdivide node and attach it all.  And say this is out green pedal.  Let's just add a little bit more detail at the end.  Cool.  And now we need to connect this area to our stem and put this last way our attach group.  Let's point this and then of course one delete the non-selected to be left with this little point.  And let's get rid of all the attributes here.  Delete the non-selected.  Let's delete all the groups.  And let's attach a point wrangle here.  And I want to use a very simple expression, which is i at id equals at ptNum.  Close it so we create a little id attribute for each point.  Because this comes in handy in a second once I get this stems curve and I object merge it down here.  And what I want to do is I want to array those points back to our stem.  So let's use a array.  So these points go onto this and I want to say minimum distance.  And now they snap into place again.  I will merge those points with my original points.  So now I have a matching point id between the two and I can just simply use an add-sop in here.  And then the polygons I can say instead of all the points I want to use by attribute I say, my id.  And now we have a connection from each source point to the newly created one, which I then going to wiggle around and follow along.  They are quite straight.  So let's reshape in these kind of connections.  Let's use another re-sample for that wire then.  Let's say 0102.  Yeah, that gives us quite some subdivisions to work with.  Of course, preview is always welcome because this we can leverage in another point warp.  Wild in, dive inside and let's bind, preview attribute in here.  And let's take our position and let's split it up.  So vector to float.  And then we use float to vector again.  We want to use especially the y-axis to give it a little, maybe also a little s-curve here.  Let's use a ramp parameter for our curvew attribute.  And then let's multiply our y-direction with our curvew.  Let's pipe it in here and bring it back to the output.  Of course, we did a little mistake.  This ramp here should be a spline ramp.  And once we crank this one up, put everything to one.  You see nothing changed.  But once we expand this, make it also be spline again.  We say we had another point in here, which maybe is 0.01.  And then we put another point in here, hangs down a bit.  0.99, we would like this.  So we have this little curve.  You can basically model it however you like.  Let's resumble this thing again.  0.002, 0.01, maybe.  Yeah, it looks quite okay.  Let's give this another sweep, or why I didn't.  It's way too big for my tastes.  Let's make it go for this.  Let's append a grid at the end again.  And of course, let's scale this along the curve.  To like to get a volcanic shape, we can start quite big.  To get this kind of sprouting root here.  And then go with dinner.  Maybe like this.  Up here it looks a little bit too thick for me.  So let's lower it like this.  We can create an all and say out connections.  And the last thing we need to do is basically  attaching all here as well.  Call this out blossoms.  And now let's object, merge everything together.  Let's take our paddles.  Let's take our blossom.  Let's take our connections in our stem.  Merge together and say no.  Out flower perfect.  Of course we can come in here, also see it.  Compute UVs.  We also need to compute UVs for our thing here.  So let's do a lapse.  Lapse.  Outflow UV.  Very quick in here.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_008.jpg

### Outro [37:44]
**Transcript:** And now we have our growing flower structure in here.  I will render a quick flipbook for that.  You modelled yourself quite a complex flower setup.  And you can start playing around with this.  Changing the stem's curve.  Changing the blossoms.  And you will be granted with endless varieties.  I hope you found this tutorial useful.  And we will see each other in the next one.  Cheers and goodbye.  Thank you.

**Frame:** tutorials\frames\model-a-procedural-flower-houdini-tutorial\frame_009.jpg


---

## Structured Notes

### Core Technique
Full procedural animated flower pipeline: Vellum wire sim for animated stem wiggle → curveU-based mask attribute for growth animation → golden angle (137.508°) phyllotaxis arrangement via cross product + quaternion rotate → blossom copy with per-point time offset in a For-Each loop → Vellum cloth "into target" constraint to resolve petal intersections → swept stem, curved connections, and assembly merge.

### Summary
38-minute tutorial by Fifo building a complete procedural growing flower. Core innovations: using the golden ratio angle with quaternion rotation for realistic flower phyllotaxis; for-each loop TimeShift trick for sequential blooming (bottom-to-top); Vellum cloth constraints with "match animation" rest blend for intersection resolution. No rigid body physics — all Vellum. Final setup has animated growth, wind wiggle, sequential bloom, and intersection-free petals.

### Key Steps

**1. Animated Stem (Wire Vellum)**
- Curve SOP (S-shape) → Transform (scale ×4) → Resample (subdivision curve, fine step)
- `curveU` attribute via Resample (or manual Attribute Create): runs 0→1 along curve length
- Resample again with "compute tangent U" only (no resampling) → generates tangent as N
- Group By Range → select first point → invert → freeze that point
- Vellum Wire: Gravity off; POP Wind force (low amplitude, large spiral size)
- Hair Constraint → Pin Point = first point group → permanentpin
- Vellum IO → cache to disk; Attribute Delete → keep only curveU + groups

**2. Golden Angle Phyllotaxis (Point Warp)**
- Node: Attribute VOP named "back_to_magic"
- `cross_vector` parameter (vector): choose X or Z axis (or both combined)
- `Cross Product` node: cross_vector × N → creates vector perpendicular to curve normal
- `golden_angle` parameter (float) = 137.508 degrees
- Multiply ptnum × golden_angle → convert degrees to radians → `Quaternion` node (axis=N, angle=radians) → `Rotate by Quaternion` on cross vector
- Result: each point's cross vector rotates by golden angle × ptnum around the curve tangent
- Bind Export the result to N (overwrites normals to point outward in golden-angle pattern)
- Bind Export curveU as `up` vector (tangent along curve) → used for blossom orientation

**3. Growth Mask Attribute (Point Warp)**
- Node: "create_mask" Attribute VOP
- Bind `curveU`; add parameters: `position` (float, 0–1) and `width` (float)
- `fit(curveU, 0, 1, ...)` to remap → `smooth()` → fit to (position - width, position, 0, 1)
- Bind Export as `mask`
- Outside: animate `position` from 0 → 0.8 over 72 frames (never reach 1 = top always thin)
- Attribute Delete → keep only mask → rename mask → pscale
- Sweep node reads pscale for tapered stem; attach grid cross-section; clamp min 0.05

**4. Blossom Copy Points Setup**
- `pscale` attribute for blossom size: Attribute VOP with ramp on curveU (0.05 at base, peak in middle)
- Multiply pscale by mask → growth-controlled sizing
- Add SOP (geometry only = points, delete prims) → Keep normals + up vectors
- Peak SOP: push points out from stem along normal by ~0.06 (uncheck recompute normals!)
- Group Expand from base group → expand 125 steps = "bottom" safe zone
- Object Merge blossom → Copy To Points with "everything but bottom" group as target

**5. Sequential Blooming (For-Each Loop with TimeShift)**
- For-Each Loop set to "foreach point" (or "foreach number")
- Metadata Input node creates `iteration` detail attribute per iteration
- Inside loop: Object Merge blossom → Time Shift with expression:
  `$F - detail("../foreach_metadata1/", "iteration", 0) * offset`
- `offset` parameter (float, default 1) = frame delay between each blossom
- Result: blossom at point 0 opens first, then point 1, 2, etc. → bottom-to-top bloom wave

**6. Vellum Intersection Resolution**
- Group single center point of each blossom as `attach` group → propagate through loop
- Null "blend_shape" = reference geometry for Vellum to follow
- Vellum Configure Cloth: etch length scale small, stretch stiffness 10, bend stiffness 0.001
- Vellum Constraint: type "into target", points = pin group, uniform thickness = etch length scale, pin/orientation type = soft, match animation enabled, stretch stiffness = 1, bend stiffness = 0.6–0.8
  (1 = fully follow target; 0 = fully Vellum; blend controls how much intersection resolution is allowed)
- Vellum Solver: gravity off, substeps 2, constraint iterations 32
- Inside solver: Rest Blend → "update each frame" (or substep for bindings) → reference blend_shape null
- Cache with Vellum IO
- Post-process: Vellum Post Process → blur, subdivide; Detangle for artifacts; add thickness

**7. Assembling the Flower**
- Group Promote: attach point → primitives → Group Expand → blast to cap blossom base
- Stem connections: blast center attachment points → point wrangle `i@id = @ptnum;`
- Array SOP (minimum distance) → snap center points onto stem → Merge → Add SOP "by attribute" (id) → creates lines from each blossom base to its stem contact point
- Resample lines, Point Warp with ramp on curveU → add Y displacement for S-curve shape
- Sweep connections with small grid cross-section
- Object Merge: stem_geo + blossoms + connections → Merge → out_flower null

### Houdini Nodes / VEX / Settings
- **Curve SOP** → **Resample** (subdivision curve + tangent U only pass)
- **curveU attribute** — 0→1 position along curve, central to all growth/placement
- **Vellum Wire + Hair Constraint** — animated stem with wind wiggle; pin first point
- **Group By Range** — select first/last point of primitive
- **Cross Product (VOP)** — vector perpendicular to curve tangent → used for golden angle rotation
- **Quaternion (VOP)** → **Rotate by Quaternion (VOP)** — rotate cross vector by golden_angle × ptnum around curve tangent
- `degrees_to_radians(value)` — convert golden angle before passing to Quaternion
- **Bind Export** — overwrite N with golden-angle rotated vectors; export curveU as `up`
- **Fit Range (VOP)** — create growth mask from curveU + position/width sliders
- **Attribute VOP "create_mask"** — mask attribute animated position drives 0→0.8 growth
- **Sweep SOP** — uses `pscale` for tapered stem; requires grid cross-section input
- **Peak SOP** — push blossom copy points outward along N; uncheck recompute normals
- **Group Expand** — grow a named group by N point steps along connectivity
- **For-Each Loop** — one iteration per blossom copy point
- **Time Shift SOP** — `$F - detail("../foreach_metadata1/", "iteration", 0) * offset` = sequential bloom
- **Vellum Configure Cloth** — small etch length scale, stretch=10, bend=0.001
- **Vellum Constraint (into target)** — stretch/bend stiffness 1.0 = fully follow shape; blend to 0.6/0.8
- **Rest Blend** — update each frame inside Vellum solver to track animated blossom targets
- **Array SOP** — snap points to nearest location on another geometry (minimum distance)
- **Add SOP "by attribute"** — create polylines between matched id points
- **Point Warp + ramp parameter** — S-curve shape on stem connection lines
- `i@id = @ptnum;` — assign unique ID for attribute-based Add SOP matching

### Difficulty
Intermediate

### Houdini Version
any modern (H19+)

### Tags
[procedural-modeling, vellum, wire-solver, copy-to-points, for-each, quaternion, golden-angle, phyllotaxis, sweep, intermediate]

---

## Related Tutorials
- intro-to-houdini-volumes---beginner-course.md (Vellum concepts appear in same skill set)
- intro-to-vops---houdini-beginner-tutorial.md (VOP math: cross product, quaternion, fit range, ramp)

