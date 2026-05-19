---
title: Introduction to Particles in Houdini 21 [FULL Beginner Course 2026]
source: YouTube
url: https://www.youtube.com/watch?v=041qemBc_1Q
author: Pixel In The Frame
ingested: 2026-05-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/introduction-to-particles-in-houdini-21-full-beginner-course-2026/
frame_count: 22
---

# Introduction to Particles in Houdini 21 [FULL Beginner Course 2026]

**Source:** [YouTube](https://www.youtube.com/watch?v=041qemBc_1Q)
**Author:** Pixel In The Frame
**Duration:** 165m26s | 22 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** In this course, I will show you how to work with particles in Goudini.  We will cover a lot of different topics from pop solver to pop forces, volume add  action, instant scene techniques and much more.  Let's start.

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_000.jpg

### POP Source [0:22]
**Transcript:** To do a particle system in Goudini, you should create geometry, go inside, hit up and type  pop network.  It will create for you dope network with basic nodes needed for particle simulation.  If you will hit play button now, you will see that nothing happening, simply because  we didn't set up any meter for particle system.  To fix that, we should set up a meter itself.  As you see now, a mission type we have scatter onto surface, so we need a geometry as  an input and geometry source is the first input of pop network.  So let's go up to solve level and create a sphere after that connected to first input  of pop net.  I will move sphere up.  And now if we hit play, we can see that particles start scattering onto surface of the sphere.  We have a checkbox for guide geometry.  We just create a ghosting wireframe so you can see where is your emitter.  Let's create a gravity force node.  As you see, it's pointing downward, there is 9.8 value.  And if we start playing now, the particles start moving down.  Next mission type, if we click on drop down menu, would be all points.  Basically, sourcing will happen from every point of our input geometry on every substep  of simulation.  And as...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_001.jpg

### POP Solver [10:16]
**Transcript:** I will set initial velocity to zero and set constant activation to one.  Unveil gravity and increase its value a lot until I start to see a sub step issue in  the viewboard.  Alright, as you see we have these gaps between particles.  It's coming because of sub step issue because particle travel too fast.  To solve that we can go up and in simulation type of dog network we can increase global  sub step value.  Now as you see the particle stream gets rid of these gaps between particles.  These here with this method would be that you force dog network constantly do same amount  of extra sub steps.  So let's speak how we can do it adaptively to optimize calculations.  Go inside and select op solver.  In here you will see minimum and maximum sub steps parameters.  And CFO condition is basically threshold which helps to understand solver what amount  of sub steps it should apply.  It takes into account particle travel distance.  Let's set maximum sub steps to 11 and as you see now nothing happens.  It's because to make it work we should have a p-scale attribute on particles.  P-scale is a common points or particle attribute in goodini which determine a size of the  point of particle.  Le...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_002.jpg

### POP Color [17:18]
**Transcript:** Press stop and create pop color node.  This node will create the attribute for particles which mean color diffuse and first color type  what you can see is constant so basically you apply it to every particle same color.  You can choose any color you want in color editor.  Next color type is random.  It assign random color based on particle ID to every particle.  So as you see we have a little Vax expression and you have a seed parameter so basically  you can change random distribution if you don't like original one.  Next color type is ramp.  As you see in Vax expression it uses normalized h so basically it takes h attribute and  divided by life of the particle.  In this case values will be between 0 and 1 so it can easily feed the ramp and you will  have a better control over it.  By default particle life is really huge number is 100 seconds.  Let's set it to 1 so we can easily check how ramp is working.  Now you can see when particles born we have one color and it's black.  In the end of this life it's moving to white color.  You can change flag position or add new flag.  These different colors if you want you can control the range in range parameter and if  you click on gear yo...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_003.jpg

### POP Group [20:16]
**Transcript:** First let's disable alpha update and let's go back to color tab and set color to 0 so  it means it black.  And press top and create pop group node.  In group name parameter set name red it will be the name of particle group and duplicate  pop color in the second pop color node set color to red.  So now we can copy name of the group or choose it in group parameter of pop color second  node.  So now every particle in group red will have red color.  Let's go to pop group node and enable group.  We default it put all particles inside this group and now we can play with different settings.  Let's disable group by rule and go to second top where we can group particles by bounding  object click on enable and choose bounding sphere.  Here we can change the size of the sphere.  If I hit play we can see that all particles inside of sphere become red because they added  to red group.  And as you see when particles leaving bounding sphere it's again become black because first  pop color node always working.  It means we should apply black color only when particle just born to do that we should go  to pop source node and in just born group parameter set group name let's let's be new  PT.  And n...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_004.jpg

### Instancing Geometry [25:06]
**Transcript:** Now we can speak about instancing let's delete all notes what we have except of basic  one.  I switch back to constant activation and create pop instance node.  As you see here we have instance pass parameter so basically we need to provide pass to instance  geometry.  I'll create a sphere choose primitive type to polygon and frequency to one and now I copy  this node and paste it into instance pass parameter.  So to reference to sphere and as you see now we have this wireframe display inside  of ubert and if you middle click on pop solver you'll see that this node create instance  pass string attribute to show what it have.  I'll split viewport and change to geometry spreadsheet.  Let's hide all attributes except of instance pass and as you see this attribute contain  the full pass to instance geometry in our case it's sphere.  So that's how it's finding the proper instance mesh.  But if we go back to sub level as you see we don't have even wireframe display let's import  and clean away particles into sub.  I'll create dope input field drag and drop pop net into dope network choose pop object  and then in presets choose particles.  So now if we change display to dope input field w...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_005.jpg

### POP Force, POP Wind, POP Drag, POP Wind Shadow [32:09]
**Transcript:** I'll delete all nodes except of basic one.  Increase constant burst rate to 15,000 and live expectancy to 3 so particles will live  longer, press stop and create pop force.  Please note allow us to add force directional and turbulence.  So let's set force in X equal to 10 so as you see now we have diagonal motion and if  we increase amplitude of noise to 10 we start to see some turbulence value.  Once decrease force to 3 and change subtle size for noise.  Settle scale help us to scale force in each axis separately.  Last length the duration of lowest frequency animation.  Roughness is scale for each new iteration of noise.  High values will give you bigger jitter in motion and lower values will give you smooth  behavior.  Atinuation responsible for noise atinuation exponent and turbulence is level of detail.  Usually you will use values between 1 and 5.  Let's create pop wind node.  It looks very similar to pop force.  One difference it has a resistance attribute and wind speed.  So this node is tricky because when you create it as you see amplitude for noise is 0  and with velocity 0 as well but this node still will affect your simulation because  a resistance parameter set at 1 a...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_006.jpg

### POP Awaken [40:57]
**Transcript:** Now let's keep only emitter grid surface and check another method how we can activate  particles.  I will move down grid to zero and remove both wind nodes.  Let's keep gravity and I rest up and create pop awakening.  This node will help us to activate or deactivate particles.  First let's create attribute create node and set stop attribute set value to one.  So basically all particles is deactivated.  And now I click on option awakened by volume.  We can choose how we want to set up a pasta object.  I'll create a sphere and we'll animate scale of it.  So I'll click in first frame and I'll click in frame 54.  So the sphere will scale over time.  We'll create VDB from polygons and check field interior.  Go back to pop net and paste the pass to the sphere volume.  Alright, as you see now sphere grows our particles become awakened and you can choose actually  from drop down menu what option you want to use.  We can put it to sleep so it's opposite action.  But in that case we should disable stopped attribute in attribute create.  Okay, let's go back to awakened.  And as you see now we have these artifact points which start on first frame falling.  Even sphere is not grown to this posi...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_007.jpg

### POP Axis Force [43:54]
**Transcript:** Now let's check pop axis force node.  I will disable for now pop group and pop awakened and disable until create rest up and type  pop axis.  Alright, these nodes apply forces around axis.  As you see now particles start to spin around center of the sphere as well we can change  type to torus.  Let's go back to sphere and I will increase the height of the force.  And increase lift speed.  So torus adds simulation to see changes applied.  And let's increase it to 5.  And as you see now particles start moving much faster along the axis.  Again as well increase orbit speed, basically it's spin speed and suction speed.  The force which goes towards the center line of the force.  I will increase radius and increase suction speed so particles stay closer to the center.  As you see we have really fast motion in the beginning for particles.  Okay let's adjust the settings.  As well we can increase influence of force with a resistance parameter.  And let's decrease life expectancy to 1 and decrease the bit orbit speed.  And set lift speed to 3.3 adjust suction speed.  Let's increase fall off.  I'll set soft edge to 1 and I will create pop force to get interesting looking motion.  Let's incr...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_008.jpg

### POP Curve Force [47:27]
**Transcript:** Time to speak about pop cure force.  I'll disable pop force and delete the rest nodes what we created.  Delete a sphere and activate create.  To create a cure for guineae we should press top and type cure.  I will switch primitive type to busy curve to have nice smooth shape.  And if you press select the node and press intern viewport you can start draw a curve.  Let's draw something like that and right click and finish adding points.  I will shift source object to the beginning of the curve.  I will enable ghost in display so I can position grid properly.  Alright let's go back to pop network.  I will set expression and conste activation $f less than 15.  So mission will happen before frame 15.  And create pop cure node.  Choose user context geometry.  And now as you see this line 4 start effect particles.  I will increase life expectancy of particles to 21.  Alright.  See that the particles traveling along the curve and spinning around it.  Maximum influence radius control the distance from the center of the curve where force will  be applied.  A resistance basically it's influence of force.  All scale parameter responsible for speed how fast particle traveling along the curve.  ...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_009.jpg

### POP Attract, POP Interact [54:07]
**Transcript:** And now we can go and discuss pop attraction node.  First I will disable pop force and pop curve force.  Press top and create pop attract.  This node will help us to attract particles to position or surface points or another particles.  First type is position.  If you choose pop attract node and press enter in viewport you'll have axis.  We can drag the position in the space.  And now if you click play particles start going in the direction of settled position.  I will remove constant activation expression and set there one.  So we have constant flow of particles.  In the top force you can control different methods how you would like to attract your particles.  The fault one is x-larate.  It applies force in the direction of goal position.  Your scale is a magnitude of this force.  If I increase it the particles start moving faster.  Reverse all distance parameter describes the distance within particles will have a repulsive  force instead of attractive.  Pick force distance parameter show maximum distance within attraction force is scaling based  on distance to target and outside of this distance attraction force will be equal to force  scale.  And maximum distance is influence ra...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_010.jpg

### POP Collision Detect, POP Properties [63:22]
**Transcript:** Time to speak about collisions.  I'll rub off all nodes here go up picket.  We don't need cure for anymore.  I'll keep great.  I'll regard to default settings for center parameter and rotate.  Move it up.  Great test zone 3 rubber toy.  Increase scale disabled shader.  We don't need it.  Move it closer to great.  Can't even increase scale more.  And now I will set expression into rotation X.  I'll use sign function.  And in brackets I will write dollar F. I need to multiply it for example by 40.  Maybe by 20 and multiply everything by 5 by 15.  Okay so we have some kind of tilt motion.  We will use the rubber toy as collision geometry.  If I shift click on rotate parameter you can see that this expression just give us a  sign curve infinite sign curve.  As well you can use motion effects if you would like there is a plenty of option you can  use noise or another thing but I will use a simple sign curve.  Okay let's go inside of pop network.  I will enable beg gravity and I will set constet activation to 1.  And life expectancy around 2.  And I will create pop collision detect node.  This node help us to detect collisions and apply certain operation on collision.  First we need to c...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_011.jpg

### Static Object (Bouncing Collisions) [71:23]
**Transcript:** What if you want to have a bouncy behavior so basically basic collisions like we expected  to have not sliding not sticking but just bouncing.  In that case let's remove these nodes and we need to use a static geometry.  Let's create merge node.  I'll connect it after gravity and create static object.  I will plug it into merge.  It's very important to remember that there is a relationship so left input affect right  input.  So basically everything on left side will affect anything on right side.  You should switch to be able to use static object correctly or change affect relationships  to mutual.  In that case the order doesn't matter.  So here we can fit our collision geometry.  Let's copy test rubber toy.  On the side and in sub pass I will set pass to collider geometry.  As you see our geometry have animation but in the simulation it not animated because  we need to click on use the deforming geometry checkbox and now we have animation.  We will start colliding but the bounce is really big.  We will fix it a bit later.  Here you can choose collision detection.  It can be a surface collision or volume collision.  I'll show you how to do volume collision in a minute.  Now let's ...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_012.jpg

### POP Replicate [78:35]
**Transcript:** Now can speak about pop replicate node.  This node, draped particles from particles.  Press stop and create pop replicate.  I'll connect it after pop property.  And as you see now every particle have a certain amount of particles rounded.  And what we should know that when we have a collisions inside of simulation we should  have and couple of attributes what go alongside with that.  And one of it is hitnam.  Basically it gives one on collision and zero when particle is not colliding.  So it can help us to determine where collision happened.  So let's choose option and meet from attribute and in attribute parameter type hitnam.  So particles will be replicated only during collision.  I'll decrease constant burst rate to 100.  And change life variance.  So if isn't closer you see that the particles start replicating when it's colliding with  colliders.  I'll decrease uniform scale.  And now we will see it not so good because the piece scale is affecting the radius of replication.  Let's use impulse activation and impulse count to three.  And add to inherit velocity I will set one and point five in y.  So now we can see it better.  Have slight extra velocities on top of inherited one...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_013.jpg

### POP VOP, POP Wrangle [81:07]
**Transcript:** As well in pop network like in soaps we can control attributes of particles with VOP.  In this case it would be pop-up and pop-rangle.  Both of them using VACs.  Just pop-up will have a visual interface for that.  Let's check pop-up node.  I'll connect it with pop-up property.  And let's say we want to have more interesting motion when particles falling.  In this case I'll go inside of pop-up and add curl noise to particle velocity.  So I will adjust it slightly to have more interesting motion.  First what I gonna do I will break velocity into vector and scalar value.  To get direction I'll use normalized node and to get speed itself, scalar speed.  I'll use length.  After that I'll create the curl noise and plug position into position input.  Create add node and add noise to direction of velocity.  Normalize vector again and multiply by scalar speed.  And connect it to output velocity.  As you see now we have some noise in motion but noise have a very big impact.  So to decrease it impact I will use mix node.  And I'll mix between a touch vector of velocity direction and velocity with noise.  And now bias will control how much we affect in the initial velocity direction.  Let's se...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_014.jpg

### POP Kill [90:58]
**Transcript:** and enable pop replicate move it up and create pop kill note.  Connect it after pop replicate.  So as you see first we can enable deleting particles by rule by default that equal to 1.  That means all point replicate particles will be deleted.  So let's type if attribute h bigger than 2.2 then particles will be deleted.  So have a very short lifespan.  Basically here you can use any vex expression to control rule for division.  If I grab it and apply before pop replicate it will affect main particle stream as well.  Okay let's disable rule and go to bounding tab.  Here we can kill particles by bounding box.  First need to click to enable checkbox.  And now all particles inside of bounding box will be killed.  If you wanted to kill outside you should just click on invert.  Let's connect it parallel way.  So the fact in all particles  so as you see everything inside get deleted.  As well you can choose bounding sphere about object about in volume.  There is also random tab where you can render we kill particles.

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_015.jpg

### Orient, POP Spin, POP Speed Limit [93:02]
**Transcript:** Okay let's move forward and now time to talk about spin.  I'll delete all these notes.  And let's create pop.  Spin node.  This node create for us orient attribute even if we don't have it by default.  So if we click now on information you'll see that there is no attribute and when we connect pop  spin. And I'll play it simulation. Now we have it orient because orient it's a vector 4  quaternion is responsible for particle orientation. And in this case spinning.  Let's disable it and go to sub level.  I'll create dog import fields node.  I'll put dog network, popnet, choose the photo object and choose preset particles.  And now I'll create copy to points to instance geometry onto particles.  I'll create box, connect it to first input and to second input particle system.  I'll change size in that axis to 4.  And let's remove any collisions.  And I disable gravity as well.  As you see here is no velocity attribute.  So let's set initial velocities. I'll set it to 7 and y and 7 in z.  And rotate viewport.  So now they go to the side.  This case to the right side.  And as you see now,  particles starting to align these velocity attributes. It's because we don't have  normals or orient....

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_016.jpg

### POP Look [110:40]
**Transcript:** Let's delete these nodes.  Just clean up a space a bit.  Thanks in their move box.  I still need it.  All right, let's keep on with that thing.  I'll move to zero emitter surface.  And go inside of popnet.  Delete unnecessary nodes.  And disable gravity.  Okay, let's disable constant activation and set impulse activation to 100.  Okay, 500 and set activation frame equal to 1.  So it would be created only in first frame.  And create poplookat node.  Connected.  And as you see, we need a reference object.  So let's go to object level, not sub level, but object level and create a null.  Let's move it up.  And to the side in x axis.  And I'll click to set a keyframe.  Go to frame 64 and change, change position.  And set another keyframe.  Set go in diagonal way.  Let's go inside and choose a null  object.  I'll disable use up vector.  And increase p scale attribute to have bigger size for the instance particles.  And now as you see particle, start following the null animation.  So basically it's always looking at target.  That's how you can use this node.

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_017.jpg

### POP Location, SOP Particle Trail [113:12]
**Transcript:** Another option to create particle system is to use poplookation node.  Let's remove pop source, press stop and create poplookation.  Here you can choose a position where emission should happen.  I will move it up.  Use impulse activation.  I will emit only on first frame.  Let's say 500 particles.  Use live expectancy 1.5 and variation 1.  I will add velocity in y axis.  And z axis.  So we have kind of burst of particles.  Increase variance in z axis as well.  And variance in x axis and z axis.  I'll quickly create pop pop.  And add same technique what we used before.  I will normalize velocity to get direction.  And use length to get speed of particle.  Then create curl noise, like position.  And add curl noise to direction.  Normalize vector after.  And mix it.  With original direction.  And the result multiply by speed.  Plug it to velocity output.  Let's add some small bias.  So adding slightly.  I will decrease frequency to get bigger sphere size.  And increase amplitude 2, 3.  Okay, something like that.  I will decrease frequency to get bigger sphere size.  I will increase amplitude 2, 3.  And as you see, the stream will be named publication.  Now I can go up and I will show ...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_018.jpg

### POP Advect By Volumes [119:38]
**Transcript:** Time to speak about volume reduction.  Let's move grid to the origin.  I'll change size.  7 and 7.  Go inside popnet, delete pop pop.  Delete ground, lane.  Delete.  Delete pop location and create pop source.  Keep scatter on surface.  Use first context geometry.  And in barstab.  I'll set impulse activation to one.  Impulse count to 1000.  In impulse activation set expression,  emit particle on first frame.  I'll disable gravity.  And delete particle trail node.  Dym inside popnet.  And create.  Pop at the back by volume start.  Connected.  And as you see, we need to set pass to velocity volume.  I'll create VDB, name well.  Vector field and type velocity.  I'll create bound for the grid.  And increase lower and upper padding for y axis.  Then I create VDB activate node.  Like VDB first input.  And the second input bound.  And choose reference.  To fill bound.  V is VDB volume.  After that, I'll create volume velocity.  And add vertex.  Create node.  And call it well for velocity.  Copy it and paste it into subpass.  So now as you see,  particle starting to be detected by volume velocity.  And when it's rigid limit,  you just keep slightly moving.  I'll create pop at track node.  ...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_019.jpg

### Instancing in LOPs (Collections) and Karma Motion Blur [128:11]
**Transcript:** That's like grade back as a meter.  And let me display and fix those issues with vortex force.  Because yeah, they're going.  And they are going to also.  Let's go up.  And I'll show you.  What happened?  That's so great.  I can use points to display and second input for velocity.  And let's move the center of vortex to the center of a meter.  And if we check now from side, you'll see that we have this.  Bulge.  So let's click on constant velocity and set it to minus one.  So we have flat vortex.  And now it's working.  Good.  But we have these stuck no velocity particles.  Let's create a pop kill.  Enable the rule.  Let's create flow speed.  Local variable equal length velocity.  So it will be a speed of particle.  If it's equal to zero, then we will remove it.  Okay, that's interesting.  I think.  Okay, let's if it less than point two.  Set like that.  Okay.  Now we have only moving particles.  Let's decrease amount of particles to 200.  And go up to the dope input field.  Create a log network.  Go inside create soap import node to import particles inside of salaries.  A great null like the import field call it particles.  Copy node and paste it into subpass.  Change sub layer to...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_020.jpg

### Final Project, render in Karma [140:51]
**Transcript:** and create geometry object. Let's go inside.  Create box. Change size in y axis. And create transform node.  To move it up. And I slightly tilt it.  Okay, now let's do. Arbodiesolver and simulate falling of this object to the ground.  I'll choose ground type ground plane.  And create our BD configure.  To adjust rotational stiffness. Click on rotational stiffness and increase it to two.  Okay, so now we have a box falling to the ground.  And now we can create a meter full volume. I'll do box again. Try to match hate with  current falling box hate.  Next create pyresource node to create points from volume.  This case in the mode I choose volume scatter.  Decrease particle separation.  And add attribute density.  Now I will restoreize volume by attributes.  And I copy separation parameter to voxel size.  Choose an attribute density and p-scale for coverage attribute.  As well check normalized by clamp coverage.  Create pyresolver.  Connect the first input source volume.  In sourcing I delete temperature field burn field velocity field.  We don't need them.  And for density field I'm crease scale to 80.  So it should be dense.  I need sourcing on the first frame. So I'll create delete...

**Frame:** tutorials\frames\introduction-to-particles-in-houdini-21-full-beginner-course-2026\frame_021.jpg


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
