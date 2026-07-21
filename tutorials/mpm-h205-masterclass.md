---
title: MPM | H20.5 Masterclass
source: YouTube
url: https://www.youtube.com/watch?v=0jJXTHjLW8g
author: Houdini
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/mpm-h205-masterclass/
frame_count: 0
frame_status: pending-selection
---

# MPM | H20.5 Masterclass

**Source:** [YouTube](https://www.youtube.com/watch?v=0jJXTHjLW8g)
**Author:** Houdini
**Duration:** 194m38s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py mpm-h205-masterclass <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi, my name is Alex-Santz Wavenier, I'm a Senior 3D Software Developer at SideFX Software
[0:04] and today we're going to take a look at the new MPM solver inside of Houdini 20.5
[0:08] but now let's take a look at this short clip showing you what you can do with this new solver
[1:00] So I hope that you're excited now. By the end of this master class you should be able to do all of


### MPM Theory: What is MPM and what is it good [1:02]
**Transcript (timestamped):**
[1:08] those things. You're going to be provided with all the material to do so and this master class is
[1:12] going to be divided into four sections. So first section we're going through the theoretical side
[1:17] of things about MPM, then we jump inside of Houdini and we look at the nodes that we have
[1:22] available to us and then we're going to go through all of the example that you just saw in this clip
[1:27] and then we look at the tip and tricks and usual troubleshooting regarding MPM. So let's jump into the
[1:34] first part. So first thing first, MPM is very close to FLIP. In fact MPM is an extension of FLIP
[1:44] to solid mechanics. So when you look at the data structure those are very very similar. So you will
[1:50] get like this blob of material which you see in yellow here and you scatter some points inside it.
[1:55] Those points are going to sample and track what is happening with the continuous material
[1:59] underneath. Then those points are transferring data to a background grid. After that there are some
[2:06] calculations done on that grid. Then the result of that calculation is brought back to the particles
[2:11] and the particles are finally addicted forward in time and there are some other calculations done
[2:16] on them. If we compare FLIP and MPM with something like the grain and position based dynamics
[2:25] there are some clear differences. So with grains you expect all of the particles to be like discrete
[2:31] particles that sit on top of each other and you expect to see some collisions between each individual
[2:36] particles. With MPM you have continuous material and you have simple points. So points that are
[2:43] there only to track what is going on with the continuous underlying material. So for example
[2:49] with MPM if you have two points completely stacked on top of each other this is not an issue.
[2:54] It's only like a waste of performance because you have two points doing the exact same task of
[2:59] tracking the same bit of material but those MPM points they are not like bits of the material.
[3:06] They are only there to observe how the material is gearing. Here we see the grid representation
[3:12] with the particle on top of them and then if we go to the meshing step so let's say for example
[3:17] that you just take your points and you use them as you use their radius to just like create a side
[3:24] science field based on the particles you can get this kind of gap between two points. Let's say
[3:30] this is a frame at rest but you still have this gap between the material so you might think that
[3:36] this is an issue of MPM but in fact when we look more closely at this particle transferring data
[3:42] to the grid we see that it's transferring not only to the nearest voxel but also to some voxels
[3:48] that are more further away from it. So here in the grid representation if we look at those two
[3:54] points they are both actually sending information to this voxel and this voxel and they are both
[4:00] tracking what is happening with this bit of material so if this mass is not too important and if
[4:06] the gravity force is applied but the material is so stiff that the volume here cannot be compressed
[4:12] in any way then it makes sense for those two particles to not to get closer together and
[4:17] then when you mesh you see this gap but this is not a problem from MPM. MPM is doing exactly what
[4:23] it's supposed to do based on the material description and how it's supposed to work. It doesn't mean
[4:29] that you cannot fix that if you by default with MPM you get the like the size of each particle
[4:36] is half the size of a voxel okay but you can play with the grid scale and reduce the grid scale
[4:44] so the voxels get closer in size to the particles and this would help with this kind of issue here.
[4:53] So if you compare MPM to FEM now MPM supports solids so it will support both elastic and
[4:59] plastic deformation. Elastic is the deformation that the solver will try to recover from so if
[5:05] you have like a block of jello and you're pushing on it the jello will try to bounce back and
[5:10] recover its original shape as opposed to plastic deformation like if you have a block of snow
[5:14] and you push on it you're just going to create a dent in it and it's going to be like the new
[5:19] rest state of this bit of snow. When you do a material that actually fractures with MPM you
[5:28] have just a bunch of points that are nearby to each other and this has a very different look
[5:33] compared to teacher e-drolls that you would get from a FEM simulation so depending on the material
[5:39] that you're trying to simulate sometimes MPM will give you like a more organic and more interesting
[5:44] look than what you would get with the FEM fractures. So MPM offers you multi-physics supports so you
[5:52] can simulate a bunch of different materials like a solid granular liquid and viscous material
[5:59] they are all interacting with each other you have two way coupling between all of these so you don't
[6:03] need to pick and choose like what material is going to influence the other they can all interact
[6:09] in the same environment and when you get to the render part of things then you can do a meshing
[6:16] like you would do with flip you can also do point and sensing where you use all the material
[6:22] like the MPM points and you just copy geometry onto them and you can also do pulse fracturing this
[6:27] is the most advanced way to do things it's a little bit more tricky to do but it's definitely
[6:34] doable where you're going to get like you start with a geometry you convert it to points do your
[6:38] simulation then you use the last frame of the simulation to fracture to pulse fracture your
[6:44] original geometry and then you do the retargeting of the iris geometry onto the MPM simulation but
[6:51] this is something we're going to see a little bit later in this master class
[6:56] so as I said before we have many constitutive model that we call behavior which describe the
[7:01] different material types that you can simulate so you have a chunky for like snow and soil elastic
[7:07] for jello and rubber there's liquid behavior viscous and sandy so many different materials to pick
[7:15] from but even if you can do multi physics with MPM just keep in mind that MPM is also really
[7:22] really good at simulating what we call like this chunky constitutive model so if you look at the
[7:28] simulation on the left and you look at this big chunk of soil falling down this spaceship this
[7:35] kind of effects would have been very difficult with previous solver like how would you tackle this
[7:40] maybe you do like a bullet simulation of the bigger pieces and then based on impact or based on
[7:47] what's happening during this simulation you can convert that to grains and do a vellum sim on them
[7:53] so you would need like to pick and choose different solver and chain them in some way to achieve the
[7:58] same result now we can just say okay this is going to be like very chunky very like wet soil and
[8:05] it's going to preserve those very large pieces made out of thousands of points until they hit
[8:11] something else and then the dynamically fracture so this kind of effects is much simpler to do now
[8:16] than it used to be okay now we have to talk about this deformation gradient attribute
[8:23] called f inside of Udini so in theory f is made out of two components so as I entered before we
[8:31] have the plastic deformation so fp for the plastic component of the deformation gradient f and fe for
[8:39] the elastic component they are both multiplied together and they form the deformation gradient
[8:45] in our case in Udini we only care about fe because plastic deformation is going to update the rest
[8:52] state of the material so we don't need to track that further because we we're not doing anything
[8:56] with it we're not trying to recover from plastic deformation so in Udini when we say f we actually
[9:03] talk about fe and the pros of this attribute are mainly that it captures a lot of things so you have
[9:10] rotation scaling and shear all captured into this three by three matrix it can also like if you don't
[9:17] need the scaling part of it and the the shearing you can compress it down to a quaternion of four
[9:22] float to make it smaller on this and from this matrix you can extract its determinant can compute
[9:30] the like basically the volume of the transformation and it will help you detect when the material is
[9:36] either compressing or when it's stretching and stretching can be associated with fracturing
[9:41] so it's very very easy to drive a secondary emission of debris from this determinant attribute
[9:49] that we call j and inside of Udini you're going to get both jp and ge
[9:54] pre-computed for you by the solver one con the main con of this attribute is basically the size
[10:01] it's like it's a three by two matrix nine float so if you have millions and millions of points
[10:05] it's going to be pretty heavy on this to cash that every time but when we go through some practical
[10:10] example we're going to see ways to get around this okay so now let's now just try to visualize
[10:16] this deformation gradient a little bit so this is a non-rigid transformation with some rotation
[10:22] scaling and shearing something you used to see in Udini pretty much everywhere if we do a small
[10:28] npm simulation of points falling you can see that if we inspect the deformation gradient on this
[10:34] simulation you can see like the very nice rotation of the points sliding onto this collider so you
[10:41] basically get this for free that's why i was saying earlier that if you need to render this
[10:46] simulation you can just instance geometry on it and you don't have to do any kind of trickery
[10:52] based on looking at the the p-scale of the point and calculating how how it's traveling to set its
[10:58] rotation the rotation scaling and shear is already present on each point and you can just copy to
[11:03] points and get the nice results from it so how is this deformation gradient split into this
[11:10] plastic and elastic component so if we look at this 2d example of a deformation gradient
[11:16] at the moment it's sitting at its at rest space there's no like deformation applied to it and
[11:23] you can see we have this critical compression and this critical stretch point on the x-axis
[11:29] now if we apply a force on it coming from the right and we push this axis on itself we compress
[11:35] the x-axis we're past you can see that we're past this critical compression point and what it's
[11:40] going to do is all of this deformation happening here is going to be considered as plastic deformation
[11:45] so all of this is being thrown away so it's not being like maintained and tracked by the solver
[11:51] because we're not doing anything with that we're not trying to recover from it but here the distance
[11:56] between this point and this point this is the elastic part so from on the next time step the
[12:03] solver is going to try to recover from only the deformation happening here and this is going
[12:07] to be our new deformation gradient those two things critical compression and critical stretch
[12:13] are user-defined parameters that you're going to set yourself and it's going to greatly influence
[12:18] all the materials going to behave elastically or plastically but we're going to see more of that
[12:22] later so with npm we do explicit integration which means this requires a lot of sub-step and
[12:30] this is not necessarily bad news because it will allow the collision and the dynamic friction to be
[12:36] very very accurate the sub-stepping so the amount of sub-step per frame is completely dynamic and
[12:45] it will depend on speed, stiffness, resolution all that stuff is going to drive how many sub-steps
[12:51] are required per frame as a user you have two parameters that you can control to influence
[12:57] that you have the cfl condition which you should be used to and the material condition which is new
[13:01] for this solver there's there's also always a min and max hard limits that you can set so let's say
[13:09] for example you never want to go above 100 sub-steps you can set the hard limit to that but just keep
[13:14] in mind that if the solver requests 3000 sub-step and you clamp it to 100 for example this might
[13:23] lead to instability because there there's most likely a good reason for the solver to request
[13:29] 300 sub-steps instead of 100 so here just a little recap of the cfl condition if we have a particle
[13:37] that is traveling in space and it's trying to go from that point to that point and let's say you
[13:42] have your cfl condition set to a number higher than one maybe that this particle is allowed to
[13:48] to do like two voxels in one go so within a single time step it's going to be able to travel from
[13:54] this point to this point and this is usually something that you want to avoid with grid base
[13:59] solver like that this will either lead to instability or just bad solver that are not going to be very
[14:05] physically accurate as opposed to this when you have a cfl condition smaller than one then your
[14:10] particle are prevented from traveling more than the width of a single voxel in each time step
[14:16] and this is most likely what you want now if we talk about the material condition which is the new
[14:21] thing for npm this has nothing to do with how fast things are moving but it has to do with how
[14:27] fast the impulse are going to propagate through the material so let's say for example here we have
[14:33] this collision happening between those two bodies and we have we see a wave of impulse traveling
[14:38] through the material if this is a very stiff and the other way around if this is a very soft
[14:44] material we might expect to see the actual wave traveling through the material so if it's yellow
[14:49] maybe we have one frame where only this part is affected then the other frame this part is affected
[14:55] and then we finally on the third frame we see this part receive this this wave of impulse but for
[15:01] various this material you expect this whole body to move as a single unit right so within a single
[15:08] frame you need the samples to propagate all the way from this end to this end of the material so
[15:15] this material condition is going to work this way it's going to look at the material description
[15:20] it's going to set like how fast this wave has to travel through the material and it's going to drive
[15:28] the number of steps such that the wave can actually travel the proper distance based on the material
[15:36] this also means that if you double the resolution so if you make the voxel twice as small then
[15:42] you need twice as much sub steps because on a single sub step the single voxel can only transfer
[15:50] data to the nearby voxels and then your voxels are now twice as small so you to travel the same
[15:57] distance in the world unit you need twice as much subsets so this is just something to keep in mind
[16:03] and now just another example to drive this point on even further let's say we have this 2d
[16:08] deformation gradient we have a force coming from the right here we get material inversion on the
[16:13] x-axis this is definitely something that we want to avoid for all types of material this is going
[16:19] to be a huge problem for even like soft material like jello this is not going to work well now
[16:26] now if we divide our time step delta t by 2 we get something more reasonable but for
[16:33] not stiff material so for like jello and things like that this might be a reasonable deformation
[16:38] gradient but if we have a stiff material and we're going to have to go even smaller so maybe
[16:44] delta t divided by 10 to get like a very very small deformation because if we have stiff material
[16:51] with that amount of deformation the the reaction from this deformation on a stiff material
[16:58] will most likely lead to instability and this is something that we want to avoid
[17:04] so just by default if you set your material very stiff the solver is going to make sure that
[17:08] only small amount of deformation is allowed so as I entered multiple times and npm will support
[17:17] stiff materials like concrete and metal it will require a large large amount of subsets but the
[17:23] cool thing is you get dynamic fracturing for free so if you have this this huge building you don't
[17:29] need to define where you want things to break just basically set the appropriate material properties
[17:36] on it you let it simulate and then you need to post fracture the original geometry using the last
[17:42] frame of your simulation so this is why this free is in quote it's just because the setup of doing
[17:49] the retargeting is a little bit more involved than what we're used to with our current bullet workflow
[17:54] but it's still interesting and you can get the cool result by using npm to do some destruction shots
[18:01] this is also something we're going to cover a little bit later in this masterclass
[18:06] fortunately for us uh the solver is all written in open cl so it can run both on cpu and gpu
[18:12] it is recommended to run on the gpu but just know that you're going to be memory bounded which means
[18:17] that what is going to prevent you from going further in resolution is really going to be the amount
[18:23] of VRAM that you have on your graphic card so just if you have access to graphic cards with
[18:29] more memory this would be something to consider for this solver the background grids are using nano
[18:37] which is sparse by default so that's great and the rebuilding of this background grid is currently
[18:43] by default done on the cpu just to give you as much memory as you can on the gpu to scale with
[18:49] more particles and more voxels but if you want you can also force this nano building on the gpu
[18:58] but it will limit a little bit the amount of resolution that you can do so that is all for


### MPM Basics: The nodes in Houdini [19:03]
**Transcript (timestamped):**
[19:05] the theoretical side of things of npm for now and now we're going to jump into idini and look at the
[19:09] nodes that we have at our disposal okay so here we are inside idini and uh i just want to go through
[19:17] the the ecosystem of nodes that we have for npm just like a very high overview of the most useful
[19:23] parameters on those nodes so first of all let's look at the basic uh node tree that you get with npm
[19:30] so right here i can play the insulation so we have an idea of what we're looking at okay we
[19:38] have some soil falling some water so the npm solver has three inputs you have the sources the
[19:45] colliders and the container here for the sources you can just pick any kind of geometry it can be
[19:52] vdb or polygon geometry like that you go through the npm source this will set a bunch of particle
[20:00] npm particles to represent the material and it will also set some point attribute to define
[20:05] the material properties you can inspect them here as point attributes then you can set some color
[20:12] for visualization same goes for the other sources that you have you merge everything together and
[20:18] just plug that in the first input of the solver for the colliders it's very very similar again
[20:23] can be a polygonal geometry it can be vdb can just plug that into the npm collider merge everything
[20:32] together and uh feed that in the second input of the solver for the npm container one thing that you
[20:41] can notice you have this link here from the container to all the other nodes and this is because
[20:46] this node is not only setting like the the spatial boundaries that you might want to add but it's
[20:54] also setting the start frame and the resolution of the simulation so all of these nodes so the
[21:00] colliders and the sources they need to be aware of the resolution of the sim so they can properly
[21:06] fill the geometry with points or properly divide the collider into voxels so the correct resolution
[21:13] reaches the npm solver so we have two ways to provide this connection between those nodes you
[21:18] can either just have this dependency link on this parameter so if i select the collider you have
[21:24] npm container you can just drag the container on here and you have this connection to visualize
[21:30] the this link when you select the node you can just go to uh view and here dependency link just
[21:37] show for selected nodes this is very useful in udin in general so i would always leave that on
[21:44] but the other way if you don't like this invisible link you can just do an explicit link like this
[21:50] okay but i choose most of the time i will not use this way of connecting the container to the
[21:55] other nodes just because make the network very messy so in general i just stick to this dependency
[22:01] link and we're good that's that's all we need and we get our simulation going like this uh if you
[22:11] don't want to set all this up yourself you can just hit tab type npm configure and uh you're gonna
[22:18] get a lot of uh example here of what you can do with npm a lot of very simple example that outlines
[22:25] many different features of of npm but the most basic one is this npm configure so i will use that
[22:31] almost all the time when i want to create a new npm scene because it sets everything everything up
[22:37] for you and also creates this connection between the container and those two nodes so after that if
[22:42] you have a new source you can just like duplicate this one and you get the connection same goes for
[22:48] the npm uh collider so that's pretty much it for the basic tree now i want to visit each of those
[22:56] nodes individually and go a little bit more in depth but uh just put our attention on the very
[23:02] useful feature of each node for now so for the npm source if i select it and by default um the
[23:11] material is supposed to be snow like this this is the default uh behavior of the node and the most
[23:17] important parameter according to me at least would be this material preset so here if you are new to
[23:23] npm you just pick the material you want to start from like let's say jello and then you can further
[23:28] refine the the the attributes that you're going to set on the points so if i look at our jello here
[23:39] we get some cool jello bouncing if i set it back to snow looks like that i can pick also water for
[23:46] example you get this other complete this completely different look and by default as you'll see
[23:54] everything is set to emit once okay so emission type wants uh this is different like this is what
[24:01] you're going to use most of the time but if you want to fill a tank with water you're going to use
[24:05] continuous and this is exactly our other example here it's like this our npm source now is set to
[24:11] continuous for the emission type this is using the water material preset and now if we play this
[24:19] we have some water being projected onto that rotating pig
[24:27] you can also see that we have some initial velocity going in that direction so on the npm source
[24:34] here under initial state we have velocity that is set to go five in the x direction
[24:41] and another thing that you might want to take a look is this visualized tab
[24:48] has to do with how you see the particles in the viewport and you have to know that this doesn't
[24:54] influence the solver at all so even if you make like the the spheres super super small or you may
[24:58] make them very very big this is not used by a solver it's only used for visualization in the
[25:04] viewport and it might also be used in the post simulation when you do meshing and things like
[25:09] that you're you're going to use the p-scale to build your science distance field from those particles
[25:15] but yeah just keep in mind this doesn't affect the behavior of the npm solver at all
[25:22] so that's the high level of view of the npm source let's take a look at the colliders
[25:29] so here the most important parameter would be this the collider type you have three types static
[25:35] animated rigid or animated deforming so first example is the static one you get this very simple
[25:44] collider you use to see that all the time with any solvers the other one is this animated rigid
[25:52] so let's say you have static geometry and then you have rigid transform applied to it like so
[26:00] here if you set your collider type to animated rigid you're going to get something very interesting
[26:06] so it generates the collider on a single frame and then it will just provide the appropriate
[26:13] transformation to the npm solver and with this information the solver is able to very precisely
[26:21] interpolate the collider between each frame and this is going to yield very very accurate collisions
[26:27] and friction and all that good stuff so whenever you can decompose your collider into multiple
[26:34] animated rigid or if you have like just a single body moving as an animated rigid collider use this
[26:40] type it's going to be your best bet to get good results in this case we get the simulation
[26:50] but sometimes you get like a character or you have something more organic that you can decompose
[26:54] into a single rigid transformation like let's say we have this walking character here in this case
[27:00] you go for the the last one so animated deforming and it's going to work fine like it's less efficient
[27:06] than the other type but it's not that bad because when we use this collision type we're actually
[27:13] doing some interpolation using the elastic field to interpolate the sign distance field between
[27:18] the frames so it's more accurate than just like jumping from one sdf representation to the next
[27:23] last thing i want to talk about is the stickiness parameter so here you have friction something
[27:33] that you're used to but you have this other parameter called sticky and what it does is if I set it to
[27:40] one by default this is set to zero but now at one you get this kind of behavior where when the collider
[27:46] touches some npm particles they are going to stick together and this is very very useful if you have
[27:53] like mud splashing around and you don't want the mud to just slide on top of the collider like like
[27:58] it's made of perfect glass you want things to stick a little bit more this is really useful
[28:05] and also keep in mind that this is not bound to zero to one so if you have very fast moving collider
[28:10] or if you have like a large scene don't hesitate to bump that up beyond the one this this is going to
[28:16] change how sticky the material is and same goes for friction you can set friction then no problem
[28:23] okay so that's it for the npm colliders now the container
[28:33] so as i said before this is defining the resolution it's also defining the start frame
[28:39] as you see here and if you look at the result that we're getting from the npm solver if I change
[28:47] the resolution here so if I remove this times two now we get more resolution because we have reduced
[28:54] the particle separation every time you divide this by two you get eight times more resolution
[29:00] because you're dividing by two across all axes so two times two times two equals eight so you get
[29:07] a factor of eight in increase of particles in increase of voxels so just keep in mind when
[29:13] you play with this parameter and you also can define some boundary limits so if we look at this
[29:23] example here just going to reset that
[29:32] so by default it looks like this you can just zoom out a little bit and you don't have any
[29:37] boundaries the reason for this is because we're using sparse grids so this is the the back of
[29:43] grids or all sparse so they should adapt to any kind of configuration in space so you don't need
[29:48] to have boundaries you can just look at the particles and let them go freely anywhere in the world
[29:52] but if you do need boundaries for optimization purposes or if you just need some kind of a
[29:58] collision geometry somewhere to bounce off the particle you can activate that and say okay I want
[30:04] my walls to be closed and then you see the boundaries and now if I play the particles are
[30:11] going to be stopped by the wall and just bounce off you can also set that to delete
[30:18] so it's going to kill the particles and you have some cool visualization to know that
[30:21] this wall is in delete mode and if you want more granular control you can skip that and go
[30:30] per plane right so this one can be closed this one closed and this one delete so what it's going
[30:36] to do is that those two walls are going to bounce off the particles and this plane is going to delete
[30:41] them just like that so it can be useful if you want if you need more precision and more control
[30:48] now to the npm solver so if I select the guide and go in the first tab solver we have iteration
[31:00] at first so time scale this defines if you if you want to do like a slow motion you're going to
[31:06] decrease this value similar to other solvers in udini and global sub steps is set to one by default
[31:12] and it's not being overwritten because this is the dub sub steps so how many times the dub network
[31:18] is going to be evaluated and cooked it has nothing to do with how many times the npm solver is going
[31:24] to run right so this is something that we're going to see a little bit later on but yeah the npm
[31:31] solver is going to run a lot more times than than just one but if you are using the dive target
[31:36] then i'm going to show a little bit later and then if this dive target needs to be evaluated
[31:41] more than once or if you do continuous emission and you don't want to see any stepping in your
[31:45] and your sourcing you can increase this value by but by default this default of one is perfectly
[31:50] fine now those two things cfl condition and material condition those are the two things that I talked
[31:57] about in the first section that are going to influence how the solver is dynamically defining
[32:04] how many sub steps are going to be performed per frames so at the moment this is the more
[32:10] the the most permissive setup so it's trying to go for the lowest number of sub steps so if I run
[32:16] the simulation like that I get this and now if I go to the details attribute you're going to see
[32:24] that we're running at 46 iteration so 46 sub steps per frame 46 npm sub steps and the dub sub steps
[32:34] now if I decrease this value so I make it more aggressive remember this is looking at the speed
[32:39] at which the particles are traveling so the solver now is going to be more it's going to allow
[32:44] less travel in grid space so this should increase our subset count so if I rerun the simulation
[32:54] now we're running at 52 uh 52 sub steps now if I put that back to original and I decrease the
[33:02] material condition now we're being more aggressive but not not in terms of how the particles are
[33:07] moving in space but we're looking more at the material description so how stiff this material is
[33:13] and we're being more restrictive so we have more sub steps when we when we decide how many
[33:19] subsets that we want to run so if I run this again now we're running at 60 and and you also have those
[33:28] clamping parameters so if I say I never want to go above 55 subsets for example and I run that
[33:36] now we can see that we're capped at 55 and in this specific case you can see that the simulation
[33:42] is not that bad at all like it looks very similar to the previous sim that we had running at 60 so
[33:48] in some cases you'll be able to clamp the maximum amount of subsets and get some speed improvement
[33:53] but just keep in mind that if the solver is trying to go with very high number of subsets and you
[34:00] reduce that amount you can run into some instability issues
[34:07] then in the forces you can set your gravity you can set some air drag
[34:18] like that
[34:21] and you have a ground a built-in ground plane this green thing
[34:25] and you can change its position maybe we move it up a little bit
[34:33] you can change it it's a vector
[34:42] and you also have some rotation control here we can rotate it further
[34:46] you have friction and stickiness parameter exactly the same controls that you add on the npm collider
[34:59] and that's pretty much it for the ground plane then if we go to the visualization tab
[35:04] you can show this container or not same goes for the colliders in the ground plane
[35:10] you can also show the background grid so this is not actually like the voxels but
[35:14] those are the tiles that contain the voxels for the background grid you can use that for debugging
[35:21] purposes and finally you can also look at some point attributes on the particles so at the moment
[35:30] we're looking at the plastic component the in fact the determinant of the plastic component of the
[35:35] deformation gradient jp this is the attribute that is very useful to trigger secondary emission
[35:41] but we could be using we could be looking at other scalar attributes like speed or other things
[35:48] and finally we have this output tab where we define the kind of attribute that we want coming
[35:54] out of the solver so as you can see this deformation gradient f that was this three by three matrix
[36:00] it's turned off just to make your cache smaller so if you don't need the deformation gradient
[36:04] just don't cache it and things are going to go a lot smoother you have this fine velocity matrix
[36:11] this is also a three by three matrix i wouldn't recommend outputting that because this is more
[36:17] like a technical attribute internal to npm if you're interested in how npm works you can look at it
[36:24] but it's not really expected to be used in a production context and then you have your velocity
[36:30] you have your gp and ge so determinant of the deformation gradient plastic and elastic p scale
[36:37] id this is not something i talked about but there's a way to do pin constraints on the points so
[36:44] they track onto an animation or they are fixed in space you can output this attribute as well
[36:50] you can set age on the point and you have this source name so all of those source node npm source
[36:57] if you look at the point attributes it's going to pick up the name of the node and set that as an
[37:03] attribute it can be useful post simulation if you want to segment your sources and treat them
[37:10] differently for meshing and so by default this is being exported and you have here a list of other
[37:16] attributes that you can export for the details attribute all of this is very light so i would
[37:22] just keep them always on it's not going to make your cache any heavier we have our subset count
[37:28] and we have other attributes that can be used for meshing so the size of a voxel dx we have the
[37:34] grid scale and the particle separation so as you can see the voxel size is exactly this multiplication
[37:43] so this is a factor of how you multiply the particle separation to get to the voxel size
[37:50] and then that's pretty much it the last thing last but not least is the die target so i'm just
[37:56] going to reset the ground plane something more sensible now if i double click on it
[38:04] i can do like pop force and add this pop node here and put some crazy noise on it
[38:11] if i go back up and hit play we should have some
[38:17] some crazy noise going on cool so now we're done with this quick review of all the npm nodes


### MPM Advanced: Avalanche [38:21]
**Transcript (timestamped):**
[38:24] we've just came over them to look at the the very high level parameters and now we're going to dive
[38:29] into more and both practical example and look at other attributes but more in context of shadow
[38:35] or closer to what you would see in production so here we are inside of wedini and as you can see
[38:41] we have all the setups for all the scenes that we saw at the beginning of this master class and
[38:46] they are very very similar to each other so we're going to go through them one by one but as you
[38:52] get used to the first setup you're going to see a lot of similarities between all of them
[38:56] and you're able to appreciate how easy it is to set up those scenes with npm so before we jump
[39:03] into that i just want to show you one thing so this is something i said before but you can always
[39:10] before continuing on to those more advanced setup you can just type npm config at sub level
[39:16] and you're going to get all of these examples that you can learn a lot of things from so you could
[39:21] look at them before jumping into the next part of this master class or you can just follow with me
[39:28] look at them later okay so now let's just take a look at this first example
[39:37] so they are all set up almost identical to one another so you have the npm setup in here at
[39:43] sub level you have a love network and for the rendering part camera there if we dive in subs
[39:53] the setup is pretty much decomposed in this way you have here model prep so we just prepare the
[40:00] model for simulation here you're going to add your npm simulation after that we convert that
[40:07] well we create the sdf representation of the npm simulation for secondary debris and
[40:14] meshing for rendering here we build our snow representation for the rendering
[40:22] here we generate some points to do secondary emission
[40:27] this is the secondary simulation part this is just like a simple pop network like here we're used to
[40:34] and those nodes at the end are pretty much just preparing the geometry for being passed to karma
[40:39] for rendering so this setup is almost identical everywhere and here this node is also present
[40:46] across all setups and it allows to reduce the resolution so things are more interactive in
[40:51] the viewport and things can run a little bit faster so there's like a multiplier of two apply here
[40:57] if you want to get like a full resolution as what you are seeing at the beginning of the master
[41:01] class just set that to one and everything should be a full range okay so for now in this example
[41:12] we have this montane and we want basically to have like a slab of snow that will detach from this
[41:19] area here that will fall down so the two thing that we need is we need a collider representation
[41:26] of this montane with this part carved in and we need the carved area as a separate geometry
[41:37] to do the emission which is this part here okay so now those are two sdf but it could be a polygonal
[41:46] geometry or it could be something else um so let's take a look at the colliders first
[41:52] so we display this you can see that we have like a very fine pattern like some lines here
[42:01] on top of the collider this is because we have another collider which is this guy here
[42:05] and you might be asking okay why are we having this as a collider and the reason is at the moment
[42:10] mtn doesn't support varying friction as an optimization so if you want varying friction
[42:17] you can just decompose your collider into two vdbs and set different friction value so for
[42:23] in this case we just take this one and we're gonna we're gonna set the friction to 0.15 so it means
[42:30] that when the snow is going to slide on top of that it's going to gain momentum it's going to not be
[42:36] slowed down that much and it's more going to slide down but when it hits these parts like these
[42:42] regions then we have the friction set to 1 so it's going to stop the snow a lot more and make it roll
[42:48] down hill as opposed to just sliding so adding the collider of the slope decompose this way
[42:53] is going to add more variation in the way the snow is traveling downward and it's going to be more
[42:58] interesting so this is the kind of the act that we're doing here those two things are getting
[43:03] merged together and passed this over in terms of the source as I said we use this slab we go through
[43:11] the npm source to generate the material points there and now i'm gonna go through a little bit of
[43:18] the attributes that we have here in more details so we have the density the critical compression
[43:24] and critical stretch are the two things that i referred to earlier on in the theoretical part
[43:30] so if the critical compression well if the compression of the deformation gradient goes
[43:36] above this then this is going to become plastic deformation same goes for the critical stretch
[43:41] so if the deformation is stretching more than this value this is going to become plastic and
[43:46] anything in between those two values like within the allowed range of elastic deformation the solver
[43:55] is going to try to recover from this you also have the compression hardening this is not this
[44:01] something i haven't explained yet so this is going to make the material stiffer as it's being
[44:07] compressed and this kind of makes sense for snow if you think about it like if you have a
[44:12] like powdery snow it's going to be very soft and not that that stiff compared to other material
[44:19] and if you push on it and compress it it's going to become more and more stiff so this parameter
[44:24] is going to take care of this as you make it higher it's going to have more and more effect
[44:29] for the stiffness the default value is 1.4 here for this specific scene because of the scale because
[44:35] of the load that we're after it was crank up to 70 this is really a trial and error thing so you
[44:41] just start with the default just applying the default preset of snow and then you push it more
[44:47] or less depending on the load that you're after so in this case we wanted large pieces of snow
[44:52] to roll down the slope and we didn't want those pieces to crumble into very small bits so this
[44:59] is the reason why we increased this value here we have volume preservation this is something we
[45:05] will revisit in later example and yeah i'll keep that for later but just keep in mind that this will
[45:13] make the material more or less explosive so if you want something to like if you want a ball of
[45:19] snow to hit a wall and really like blow up from the impact you will increase this value a tiny bit
[45:24] maybe to 0.35 or 0.4 if you want the snow to just collapse on itself and not generate a lot of energy
[45:31] from the impact you can keep it at 0.2 or maybe even reduce it to make it the same less explosive
[45:37] but i will give proper explanation of that a little bit later so for now if we select this
[45:43] we have all of those attributes being set on the points and one particular example that we want
[45:51] to play with is the this e attribute which is our stiffness we want to add some variation to it
[45:57] so if i display this node here i set this so i'm generating a noise here with this crazy one liner
[46:06] by the way this is not too crazy this is just something i use all the time so you
[46:11] you generate a noise at first and then you add this noise to your position and then you're going
[46:16] to use this warped position to sample a noise function and this usually gives you like very
[46:23] nice warped detail like you have here then i'm doing an absolute value on that just to make
[46:30] sure that there's nothing negative and then i'm going to use this noise to multiply the
[46:35] stiffness attribute that we have here so i'm fitting i'm fitting the noise here between
[46:43] one and five and i'm just applying that to the stiffness to get a little bit more details a
[46:49] little bit more variation in the way the snow is a configure and i'm done i'm not touching any other
[46:56] attributes in terms of the material configuration after that i'm setting some velocity attribute
[47:03] so here we can see that i'm also adding some noise to this velocity so there are some patches
[47:09] that are going to go down a little faster when we initialize the simulation
[47:16] and apart from that here on that branch what i'm going to do is i'm isolating the top the very top
[47:23] edge of the material point and this is because i want those points to be constrained in space
[47:31] to this area so i basically want some points to stay put and stay attached to the collider
[47:39] and i want like the this edge to be defined by how the snow is going to fracture instead of being
[47:44] defined of on how i selected the polygons to generate this patch so here this is basically what
[47:52] i'm doing i'm just looking at the distance between the fpm points and this geometry and then i'm
[47:56] setting this pin to animation attribute when they are nearby and we can just if we want to visualize
[48:04] that like this
[48:14] so we can see all the points that are being pinned to this piece of geometry and this is really going
[48:22] to help to make the transition between static collider and simulated snow to make this transition
[48:29] a little more organic
[48:33] okay and apart from that i don't think there's anything else
[48:38] that was changed if we select the solver and on the solver tab yeah there's nothing
[48:46] changed we're just removing the ground plane nothing changed nothing changed here we're not
[48:51] using the deformation gradient in this scene we're even removing velocity to make the cache
[48:58] lighter on this we're also removing this pin to animation attribute
[49:04] and for the domain we're killing all the we're killing all the particles that are
[49:11] going too far away from the montane so we're using this montane bounding box as the domain
[49:17] and we're killing everything that is going off so from this setup we're getting this simulation here
[49:24] here we're looking at the our jp attribute so you can see that everything that is in red is breaking
[49:31] and stretching everything purple has preserved the volume that it has at the very beginning
[49:37] of the simulation so not breaking and usually uh want some kind of balance like this like at
[49:43] the moment it seems like there's a lot of things fracturing but um yeah you you basically want to
[49:49] preserve a lot of these these big chunks as you're tumbling down the slope it will add
[49:55] cool vibrations to your simulation uh from that point we want to generate the collision
[50:01] representation of this geometry so we're merging the simulation there computing the velocity because
[50:07] we don't add it anymore and then we generate a dvb from the particles on this dvb we want an sdf
[50:15] and we also want the velocity field to be calculated and in terms of the resolution of the dvb
[50:21] i'm just catching the particle separation the detail attribute on the cache and then i'm dividing
[50:28] that by 1.51 because this node expects the voxel to be 1.5 times smaller than the smallest p scale
[50:37] for for this to to work so if you want like good quality science and skill representation
[50:43] you can just divide by this value and it should give you a good balance between being very heavy on
[50:49] this and being very uh very bad in terms of quality then we split both things so sdf on the side and
[50:58] velocity on the other in this case and it's not like flip where you really want things to be like
[51:04] super smooth and you want things to look like a liquid in this case we still want some level of
[51:11] granularity on the snow but not that much so we're doing some operation some reshaping on it just to
[51:19] get it a little bit more smooth but not as much as as a liquid so some dilation here some smoothing
[51:27] after that we rebuild the sdf this is not something i do often but sometimes you get a lot of
[51:34] pockets of empty space inside of the sdf it makes it very heavy to cache on this so rebuilding
[51:41] will by default get rid of those holes inside of the sdf and yeah it can save you some disk space
[51:49] and on the other side i'm just down raising the velocity field making it not visible and i'm merging
[51:57] both grids and caching that so here we have our sdf representation
[52:06] that is good and after that we want to build the the geometry that we're going to render as the snow
[52:15] so for that we're going to use this sdf but not directly because we got rid of a lot of information
[52:22] by just creating this sdf we want to bring back a lot of the the density variation that we have
[52:29] from the point distribution so again i'm going back to this npm simulation creating the vdb with
[52:36] the appropriate res that we had upstream then i'm restrizing that to a grid so this has a couple
[52:43] of advantages we have cool variation in the density now because where you have like a
[52:49] lonely point in space it's going to be very low density if you have like a lot of points that
[52:53] are being packed somewhere it's going to increase the density so this is really good but it's also
[52:57] very fuzzy like at the moment we can't really see it from the viewport but the edges of the snow is
[53:02] going to be like very very fuzzy and we want some places to be more defined than other so for that
[53:09] we use our sdf convert that to fog we name it well we just isolate the the surface basically
[53:16] and then we're going to use that as a mask so in some areas it's going to make the snow a lot
[53:23] smoother a lot more sharp because we're masking with this and it will prune a lot of the very
[53:30] fuzzy details but the core of the snow is still going to have a lot of variation in its density
[53:37] because of the way we have rasterized it here so this is a good solution to do snow and then
[53:44] we merge that with the velocity and we have our npm snow like that but we got rid of a lot of fine
[53:51] details and we want this powdery load of the avalanche going down the slope so for that we need
[53:56] to do a secondary sim but fortunately for us this is very easy with npm because we have this
[54:04] attribute jp that tells us where things are breaking we can use that to do emission so here
[54:10] if i select this wrangle i'm doing a bunch of different things here basically just computing
[54:17] velocity okay this is an important bit here i'm computing the delta on gp so the variation frame
[54:24] to frame on this determinant of the plastic component of the deformation gradient so basically
[54:31] i'm computing how things are stretching from frame to frame so if we look at our jp attribute here
[54:39] so let's say i told you earlier that if this is set to one it means that everything is like neutral
[54:46] nothing is being deforming it's not compressing it's not stretching but now this is set to 17 so
[54:51] you know for sure that we're going to need to emit some particles but if it stays to 17 between one
[54:58] frame and the next it means that we're still static right like we are sticking to the 17
[55:06] level of stretching so we only want to emit when we're going to go from 17 to 18 so for that we
[55:12] compute the difference between those two so the previous frame jp and the current frame jp and this
[55:18] djp for the delta jp is what we're going to use to do emission so from here i'm just pruning low
[55:26] delta jp i'm pruning slow particles and here i'm also pruning all of the particles that are too
[55:34] far away from the surface let's say you have a surface so this is some snow this is like a fracture
[55:41] in the snow so in this case you only want a particle emission to be very close to the surface like so
[55:57] so you don't want points to be like floating on top of the surface and you don't want to emit
[56:03] secondaries inside of the sign distance seal because they are not going to be visible at
[56:08] render time so what you do is basically you have like a banner around your surface
[56:22] and you want to make sure that all of your emission is within contained within that banner
[56:26] and all of the other points are being removed and this is exactly what we're doing here so our
[56:32] banner width is twice that distance so we're looking at 0.15 above the surface and 0.15 below
[56:39] and this surface is we got this from our npm sdf representation and yeah everything that is out of
[56:46] this banner is going to be removed then after that we just cache that and we get this for our secondary
[56:57] emission source and then we further do some pruning based on the djp djp then we remap the
[57:06] attribute we compute the speed here we replicate based on the this delta jp attribute so if things
[57:15] are breaking a lot you want more points to be replicated because you want more emission in that
[57:20] space and if things are moving fast you also want more replication so here we replicate based on speed
[57:28] because we're spreading those points along their velocity vector so if the velocity vector is very
[57:34] long you want more points to cover more ground like if we have two points
[57:44] okay so this is like a point an emission point at frame one and this is an emission point at frame
[57:49] two um you don't want gaps of emission so when you emit
[57:57] you don't want like a bunch of particles here and then a bunch of particles there and have a huge gap
[58:03] here you want this to be more continuous like you want this to create a more continuous line in space
[58:12] you would want something more like that so it creates something more straight and you
[58:19] don't have like holes and stepping in your emission what we do is it's very simple we just take the
[58:27] velocity vector we multiply it by this time increment variable such that we only get the
[58:35] delta like the difference between two frames and not the difference between two seconds
[58:40] and here we have this random float going from zero to one and this will allow us to spread
[58:47] the particle along their velocity vector so if I just display that
[58:53] enable and disable and you can see that those points are being pushed forward in space to
[58:58] make sure that the emission is going to be smooth okay and that's it for the preparation of the
[59:09] secondary emission then we do our secondary sim and here I'm not diving into the details of this
[59:16] node everyone is doing secondary simulation differently the only thing I'm going to say is
[59:20] you have this fast fdf collision here you don't really need to use that so you can just do like
[59:26] oops can just do like a static object like this and completely disable this node which is
[59:32] probably too complex for no reason the only thing I'm doing here I'm computing like the
[59:40] relative density of the point cloud that this is something I call packing here point packing
[59:46] and if we look at the result so this is our simulation
[59:56] okay so when when the points are very densely packed together it's going to be more on the red
[60:03] side and like the lonely points that are floating separated of the rest in space or more on the
[60:11] dark purple side of things and I'm using this attribute to add more or less wind so when
[60:17] you have a lot of density a lot of points back together I want those points to not be affected
[60:23] by wind that much and when you have lonely points floating in space I want them to be affected a
[60:27] lot by the wind and this adds some nice variation in the simulation so that's the that's the only thing
[60:33] but for the rest it's very straightforward pop simulation after that we're rasterizing this
[60:42] to a grid using again the same resolution computing the velocity here merging back together and here
[60:50] we adjust the density this multiplied by 50 just comes from trial and error so you look at your
[60:57] result in karma and you just tweak this value until you you get the right look and here we merge both
[61:04] our npm snow with our secondary emission using this maximum operation and we have the best of
[61:13] both worlds we have those large smooth chunk of snow coming from the vdb snow but we also have
[61:20] this pottery look coming from the secondary emission those two nodes are just representation
[61:27] of the montane for rendering so here we have our euro montane with some uv's and here we have the
[61:34] environment montains so now if I go in our love network here and I can render that so this setup
[61:47] is pretty straightforward you have your snow here so this is the the vdb representing the snow the
[61:53] euro montane and the environment montains there's one a gri as the the whole lighting this is setting
[62:01] the materials very straightforward material for all those geometry here we import the camera
[62:08] and this is all going into a this karma node we're using xpu at the moment and this is what we get


### MPM Advanced: Rally Drift [62:16]
**Transcript (timestamped):**
[62:17] okay let's now move on to the second example the rally drift example
[62:23] so again the structure is very very similar we just have a little bit more prepping happening here
[62:31] this is all the geometry preparation this is our npm simulation then we do our meshing
[62:40] prepare the points for secondary emission we do secondary emission and we do the final
[62:46] preparation of the geometry for the rendering and this is mainly like the the set not really the
[62:53] npm points being remeshed okay so let's start from the top I'm not going to go through all of this
[63:02] but I just want to let you know that this is the geometry that you that we are using for the ground
[63:08] so it's mainly like just dirt soil and we have some card tracks here to make it look like it's a
[63:16] rally track or something and we have an animated car here so we have this car coming in and drifting
[63:27] just so you know all of this is being animated inside of Udini with the suspension and everything
[63:32] it's it's really not as fancy as the the car rig but it's just like just a fun procedural way of
[63:39] animating a car in a simple fashion so if you want to take a look it's it's all there then after that
[63:46] we're basically like trailing the car like to see where it's going and after that we're extracting
[63:53] we're splitting the ground geometry into two separate parts so the first part is going to be
[63:58] the collider so we have removed this part where the car is coming in and we have separate this out
[64:04] because we want to simulate this and keep the rest static from there we also we're also adding
[64:11] additional geometry so we're scattering a bunch of points on top of the mud and this is going to be
[64:22] like more stiff pebble-like material and we are also adding some muddy water on top of the soil
[64:32] again i'm not going into too much detail on how this is being done this is very
[64:36] like usual Udini sdf kind of manipulation so you can look at the tree upstream to get more information
[64:45] and here i'm going back to the our soil that we're going to simulate we're basically splitting that
[64:52] into again because we're going to use two different uh constitutive model two different material
[64:57] description to simulate the soil so this is going to be like one part of this split
[65:04] and this is going to be the other part those two nodes are being object merge here and this is
[65:11] where we're doing our npm simulation so first i'm going to start with the material here material
[65:17] sources so this is going to be our stiff mud if i go through the first frame we can actually see
[65:23] our npm particles keep in mind again this is after the resolution of the iris version of this scene
[65:32] if you want the full resolution you have to set this back to one but for now for interactive
[65:39] purposes and speed we're going to stick to this so here we're just going to pick the mud preset
[65:44] and that's it there's nothing change here this is just like the mud preset for this
[65:50] and then the other part of the soil this we're going to use the soil preset i think here
[65:58] soil preset and again just this is the soil preset as is there's no change here for both cases like
[66:07] for both the the mud and the more chunky soil we're going to modulate a little bit the attributes
[66:15] so in this case this constitutive model it has some viscosity and in fact i'm going to explain
[66:21] a little bit those two barriers first so stiffness and volume preservation this is the same thing as
[66:27] we had with the other like with this chunky and constitutive model but now we have with this one
[66:36] with the viscous constitutive model we have viscosity and plasticity viscosity is a bound between
[66:41] zero and one so there's no point in setting that higher than one one is going to be like very very
[66:47] very viscous like almost like a solid and zero it's almost behaving like water then you have
[66:53] plasticity in this case plasticity behave in a way where as material is being deformed it's
[66:59] going to hold its shape so this is very useful like if you want to create like a cone of soft ice cream
[67:05] also very good for shaving cream things like that where it just like emit a pile of material
[67:10] and you just want it to hold in place you can play with this plasticity setting in this case we
[67:15] won't just a tiny bit of it for the mud and this is not something we're going to modulate here here
[67:22] we just want to add some variation to the viscosity to get more details on the other side here we do
[67:31] the same thing but with the e so with the stiffness because we're using a different constitutive model
[67:37] when we use a chunky constitutive model it's make make more sense to act on the stiffness and the
[67:44] volume preservation but mainly the stiffness but with the viscous constitutive model acting on the
[67:50] viscosity is going to give us more variation so those two things together are going to represent
[67:56] our mud then if we move here we have our pebbles as I said and here we're doing like a little cheap
[68:04] because normally if you really want those things like if we want those points to hold together as
[68:10] one unit you would need to push the stiffness pretty far so at the moment we're using the
[68:15] soil preset and we're just multiplying the stiffness by two and normally you you would maybe use
[68:20] like the concrete preset or something like that but we don't want the simulation to be super slow
[68:25] and at the rendering stage we're only going to copy geometry on top of each point so we don't
[68:31] re-care if this table like fractured in the middle because on one side you're gonna have
[68:37] some points with some geometry and stands on it and on the other side you're also going to have
[68:41] like separate geometry and it's not going to create any kind of stretching or any weird artifact
[68:46] so for that reason we just stick with a more conservative stiffness and we know that the
[68:50] simulation is going to go through a faster than for the liquid so our puddles we could be using the
[68:59] liquid constant model for this but we want just a tiny bit of viscosity because it's kind of muddy
[69:07] water so for that reason we stick with the viscous constant model and this is exactly the mud preset
[69:13] but we are removing some of the viscosity to make it more like water then we have some color just for
[69:19] visualization and we have that so we have all of our different materials here in terms of collider
[69:28] we have our ground we really want materials to stick to it so we're cranking up the friction
[69:34] and the stickiness very very high and we're also doing the same thing on our car so friction not as
[69:42] high but we really want like if there's a bit of mud touching the car we really want this to stick
[69:47] to the car and here this is very important to also use the animated rigid and not deforming
[69:54] our car can be separated into multiple colliders so if I just play this animation
[69:58] a little bit and we go closer
[70:07] so you can see the individual bounding box for each of the PDB and if I play this you can see
[70:13] that the tires are actually being transformed frame per frame from a single SDF and this is
[70:22] exactly what we need if we want the mud to be a splash in space with very very accurate collision
[70:28] very accurate friction all of the the splashing and the details from the mud is going to be
[70:35] generated by this dynamic friction this is not the kind of detail that you would get if you would
[70:41] just pick animated deforming after that we have a just a simple box here defining what we want as
[70:49] our domain our to limit the space where we're swimming and we're just going to delete everything
[70:55] that goes outside of those boundaries like so and in terms of the solver itself
[71:10] we're not changing anything for the CFL condition and material condition which is
[71:15] keep the default we're not changing the minimal subsets the time scale we want to do a slow motion
[71:20] shot in this case so we set that to a 0.1 and we're going to reference this parameter right after
[71:29] our animation so here we have our final animation let's say so this is our final animation uh
[71:37] yeah this so this is like real time and then we want our slow motion version so we just like
[71:42] reference this like a we multiply the frame by the time scale on the npm solver and we get our
[71:50] slow motion timing correct like so that is one thing then we are simply disabling the ground
[72:08] plane nothing happening here for the output we output the deformation gradient because we want
[72:16] to instance some geometry on the pebbles remember so we need that for the proper orientation of these
[72:23] we're not caching velocity and we're not caching pin to animation but in this case it doesn't change
[72:28] anything to have it checked on our off because there's no there's nothing pin here so this could be
[72:34] safely ignored um and yeah that's it before caching what we do we convert this uh three by three matrix
[72:45] so our deformation gradient we convert that just to a simple quaternion simple orient because our
[72:51] we don't really need to have like the local deformation of each pebble that precise so if
[72:57] we just have proper orientation of the pebble it's gonna be perfectly fine so we do that and then we
[73:02] kill the deformation gradient just to make our cache lighter and then if we cache that on this
[73:11] we should get something that looks like that
[73:20] and here we can look at it more in context
[73:23] cool so we have our
[73:31] huge large club of soil being thrown in the air we have finer details coming from the
[73:38] combination of like viscous almost liquid like material and this more
[73:45] a chunky material of soil and it's it creates like a very rich level of detail
[73:54] across the simulation
[74:00] then when we're done with this we go to the meshing step before rendering so
[74:08] here what you have is exactly the same thing as we had with the avalanche but just like
[74:12] defining the sdf for the npm simulation but here we're going to do like the npm soil then we're
[74:22] going to do the water and after that we do the pebbles so first the soil here we just isolate
[74:30] all the points that belong to both the the mud like the more muddy part of the soil and the
[74:38] more chunky part of the soil like those two basically those two nodes are being merged
[74:45] here like those two sources they are they are being sourced by using this source name
[74:52] then after that we convert them to sdf
[74:59] again if i just dive quickly inside of this node normally if you're doing like liquid you can have
[75:06] this sdf dilate much higher with along with this sdf erode same thing for the smooth but in this
[75:12] case we want things to look more granular more chunky we want to preserve more details so we're
[75:17] going to accept this blobby kind of look for this material and we're going to keep those nodes set
[75:24] up this way but just keep in mind that you can play with that and change the look drastically
[75:29] to go more toward a smooth and liquid look then we can convert that to polygons
[75:39] here i have a small optimization that can be skipped but this is just like to prune
[75:43] some of the the polygons that are not going to be seen in the render so i'm just using like the
[75:49] colliders to prune some polygons and then transferring velocity transferring rest attribute
[75:55] and we get our final geometry that will go to render
[76:02] for the water we have very similar setup the only difference is that we're using the particle fluid
[76:07] surface to generate the initial sign distance field like so then very much the same thing we're just
[76:19] not transferring the rest attribute because we won't use it at render time and here we have
[76:24] two representations of the water the first one being the surface this is what we're going to use to
[76:29] do like a specular reflection things like that and on the other side we have the volume representation
[76:36] for it to get like this nice scattering of the light inside of the water
[76:44] here we have our pebbles and here we're just basically setting like we're adjusting the p scale
[76:51] adding more variation we're defining an index here this is going to be used at render time to
[76:56] instance different pebbles on different points we're adding some variation to the orient attribute
[77:04] and that's pretty much it so just making sure that everything is going to look as natural and
[77:09] organic as possible here we're kind of building our library of rocks we can look at it if i do this
[77:22] so we have this kind of library of low resolution rocks this is what we're going to instance
[77:28] on the points and yeah that's pretty much it for the the the meshing and the preparation of the npm
[77:39] geometry for rendering here this is very similar to what we what we have done with the avalanche
[77:48] so we're just preparing using the npm simulation and extracting the points that we need to do
[77:55] secondary emission i think the only difference is the geometry that we're going to use as
[78:03] colliders but this is very similar here we're doing our simulation again very similar the output
[78:10] of the well okay maybe one thing that is different is since this is slow mo shot i think this node
[78:17] yeah in here we divide the velocity by the time scale okay here we are computing the velocity
[78:25] based on the different in position but we are not considering the fact that this is a slow motion
[78:31] shot so since we're running at one tenth of the real time here we need to divide by this point one
[78:39] to bring back the velocity to what the what the particle is actually traveling within a second at
[78:47] real time and not not in slow motion so this is just making sure that this simulation running also
[78:53] with this time scale of point one will be correct like the points are not going to be slower than
[79:00] they are supposed to be because of that adjustment so just keep that in mind if you're doing a slow
[79:05] motion and your velocity vector vector need to be appropriate after that when we go out of this so
[79:17] let's say let's look at the simulation that we have so this is our secondary simulation
[79:25] again we're looking at our point packing so the points that are tightly packed together
[79:35] are going to be less influenced by the wind and the other way around for the purplish points
[79:41] here we're splitting half of the points to be rendered as soil points so more like a dirt
[79:48] like brown and opaque points and the other half is going to be rendered as clear water
[79:53] and when the arc combined together it's going to create something interesting and add some variation
[80:00] to the secondary sim and finally as i said at the beginning here we just have our
[80:08] final geometry for the environment that we're going to render so this one is the static soil
[80:15] we get this to render around our simulation and then we're scattering a bunch of points on top of
[80:22] it to render as static pebbles just to bridge the gap between the dynamic pebbles and the rest of
[80:31] the ground where there wasn't any pebbles scattered at the beginning now it should be more uniform
[80:37] let's now jump into our log network okay so here if we look at each of the elements one by one
[80:45] and
[80:50] so here here we have our dynamic pebbles so what you basically need to do is you merge your pebbles
[80:59] like your yeah your rock geometry from subs this is being merged in here then you create a collection
[81:07] and each of those instancer are going to fetch in the points so the the npm points that you want to
[81:13] instance pebbles on them and they are going to use this collection of rocks to copy the geometry
[81:19] onto them so you have your dynamic pebbles here here we have our static pebbles
[81:27] like so then we have our npm soil
[81:32] our water
[81:45] if i go on the other side
[81:53] we get both the specular reflection and the cool scattering from the volumetric representation
[81:58] of the water and as you can see for now the water is very very blobby but this is fine because
[82:04] as i said multiple times this is the aphrez version of the the final shot so if you set it to
[82:11] the iris representation if you set the red node to one then you should get like a much mooter surface
[82:17] here this is our static ground
[82:28] and we have our soil points from the secondaries those more opaque dark points
[82:38] then we have our droplets of water
[82:43] all of them merge together get this nice pattern with a lot of variation
[82:50] and then if we look at everything together through the render camera we get this
[82:56] again this setup is pretty simple in terms of the material those are very very straightforward
[83:04] like just one material for the the water exterior the interior of the the water like this for the
[83:10] volumetric representation of the water then you have one material for the soil i think this is
[83:15] also used for the pebbles and then one material for the for the car after that for the lighting it's
[83:21] just a simple hdri and the camera is being merged in going through it karma lups and that's it for
[83:28] this that's it for this shot so now we're going to take a look at this ship bridge thing


### MPM Advanced: Ship Breach [83:30]
**Transcript (timestamped):**
[83:37] okay so first of all we have the spaceship coming out of the ground
[83:41] then we're going to use the animation to generate the ground so first we just trail the motion
[83:46] like so we have the full animation path of our spaceship and then we're going to build our ground
[83:54] from there just to make sure that we cover all the necessary area so basically have this just
[84:00] this is just like the sinus and seal representation of the ground that we want to simulate
[84:04] then we split it to have on one end the the static ground that we're going to use as a collider
[84:10] and then here we just use the trail motion of the spaceship to cut out the area that we want to
[84:17] simulate so this is going to be simulated with mpm like so in terms of the mpm simulation itself so
[84:25] it's happening here for the the material points so we go to our mpm source we're basically just
[84:34] using the soil preset so we're making the compression arning a little bit higher so again
[84:40] this is when you have compression happening it's going to make the material stiffer so it holds
[84:45] more together and it can fracture more easily and we also crank up the stiffness quite a bit
[84:52] because we really want those large chunk of material to all together after that this setup is a little
[84:59] bit different than what i used to do normally and here i'm computing some like i'm just warping
[85:05] the points and i'm going to store this worked position as a rest attribute and then i'm using
[85:11] the attribute adjust float to modulate the stiffness of the material so here we're adjusting the
[85:19] stiffness e we define the range that we want to have as output and we're using this rest attribute
[85:29] then after that i'm using the top layer so this is what like this is the layer sitting on top of
[85:35] our mpm points and i'm going to use the distance between this top layer and the points to define
[85:40] what is going to be the grass layer so here i'm setting this grass group and also i'm changing
[85:48] a bunch of the material properties just to make the grass be a little bit differently than the
[85:53] soil that we have underneath and all those values just come from trial and error so just you start
[85:58] with the preset you run a full version and you just make it more or less stiff depending on the
[86:04] kind of chance that you want to see in your final simulation then i'm setting some colors
[86:10] just as visualization this is not going to be used directly at render time but just to see
[86:16] with our sim then in terms of the colliders we have the spaceship
[86:25] it's using our animated rigid collider type just to make it very precise in terms of friction
[86:32] we're making it a little bit slippery we still want like to see some of the soil just slide on
[86:37] it and fall down but we also make it sticky so if there are some soil that goes in contact with this
[86:44] underneath here it's going to stick to it and it's going to make the simulation a lot more
[86:49] detailed and interesting on the other side here we just have like very very high friction very high
[86:57] stickiness just to make sure that all the material that falls on this stay stay put when it touches
[87:03] this area and one thing to note about the animation of the spaceship like if i just follow this link
[87:09] here and space g and one thing to note is if i disable so here we have like the rotation and
[87:18] translation up if i disable this and we only look at this shape node so this is interesting
[87:24] because you're going to see this is very very subtle motion so just like a very very subtle shape
[87:32] if we don't have this node and you can test that like you can run a simulation without this node
[87:36] and you're going to see that you're going to have like a very large build up of material on top of
[87:42] the spaceship that will never crumble and that will never fall down so one of the ways i found
[87:47] by playing with it to get this thick layer of soil to break progressively and to give me like very
[87:54] nice detail throughout the animation is to have this shake so here there's an animated perimeter
[88:00] so we have like a peak at 175 where it's going to shake the most and then after that we're just
[88:05] fading on each side and yeah you can test with and without and you're going to see like a very
[88:12] large difference between the two simulations in this case we're really relying on the precise
[88:17] collision and the precise friction that we get with the animated rigid colliders and we can get very
[88:24] different looks just by adding those subtle motions
[88:30] and then for the solver itself i don't think we're doing anything fancy
[88:39] so this is all that default same same and for the output we are exporting the deformation gradient
[88:46] we're not going to use the three by three deformation gradient so right after the solver you can see that
[88:50] we're converting our three by three matrix to a four float quaternion just to make it as light as
[88:58] possible on this but this is going to be used for some uprising process on the soil and also for the
[89:04] grass layer that we have on top apart from that we're just eliminating a bunch of attributes to
[89:11] make the cache as light as possible and that's pretty much it if we look at the final result
[89:20] i can probably also template the spaceship
[89:32] so
[89:40] and you can see like if we take a closer look at this piece this is definitely the kind of
[89:47] large pieces that is hard to keep together with the other solver like solver based on the position
[89:52] base dynamic it's very tricky to keep like a very large piece of material like this to preserve its
[89:59] shape before it's something else so yeah npm is really good at keeping that together and even if
[90:07] you increase the resolution because remember that we're still a fray at the moment so if you want to
[90:12] go to the full resolution of the clip that you saw earlier you need to set that to one and
[90:18] you're you will see that those big chunks are still preserved even at higher resolution than this
[90:25] so that's it for the npm installation after that we have our usual sdf representation of the npm
[90:34] sim on the right side here we are meshing this and so we're just going to render that as a polysup
[90:40] so here i'm isolating the surface after that i'm converting that to polysup
[90:47] and you can see that a lot of the polygons have been removed inside because i'm using
[90:56] all of these colliders as a mask to prune all of the polygons that we're not going to see
[91:01] in a final render just to make it lighter on the on the d-ram when we render with the karma xpu
[91:07] then transferring the veil the velocity transferring the rest attribute and the grass attribute this
[91:12] is going to be used at render time and that's it that's it for the meshing process then on the other
[91:19] side here we're doing something interesting like if if we look at our mesh here uh well this is
[91:26] still afrez as i said but even at full resolution this will be pretty smooth and it will look uh
[91:33] not as detailed as what we're looking for so one trick is maybe we can use the npm points so
[91:39] if you take these points so we can use these points and maybe instance some geometry on the point to
[91:46] up res the surface of our fracturing soil but if we use all the points and we copy geometry to it
[91:53] it might we might run out of memory it might be too heavy to render that so we kind of want to
[91:57] isolate just the points that are sitting exactly on the surface of our soil so here's what we're
[92:04] trying to do so we have a piece of material so this is on frame one for example and this is
[92:09] the same piece of material but on frame 10 okay so we have like a big fracture here what we want
[92:15] at frame 10 is to have some tables that are being instanced on the surface here just to
[92:20] up res the detail a tiny bit just to have more geometric details
[92:27] but as this is fracturing we don't want to see points appearing and disappearing we want this
[92:32] to be completely consistent throughout the frame range what we need to do is to solve such that okay
[92:38] on frame one we know that this is what we need like this is the the surface but if you solve all
[92:45] the way to the final frame you also know that you're going to need some points here but all the other
[92:51] points so if you have a point here or if you have a point like floating far away from the surface
[92:57] you basically want these to be eliminated because if you keep those points in it's going to use
[93:05] large amount of memory like if you use all of your mpm points to instance people at render times
[93:10] it's going to take a lot of memory so you don't want that you just want to isolate the minimum
[93:15] amount of point that you're going to see sitting on the surface so this is basically what we're
[93:20] trying to do inside Houdini in the sub solver I can show you in the solver how it's done
[93:25] so here we do like three different things so if the point gets too far away from the surface
[93:33] we're just going to kill it so as soon we're basically solving through all through the whole frame
[93:38] range and as soon as the point gets far away from the surface we're just going to add it to this group
[93:44] to kill and we're going to remove it if it was previously added to the edge group so if at some
[93:49] point it was sitting on the edge then we just again add this attribute back just to make sure
[93:55] that we maintain a history of what was sitting on the edge and if it wasn't on the edge but now
[94:00] it's currently sitting on the edge of the science sense field then we add it again to this edge group
[94:06] when this is solved so we go all the way to the last frame and we solve through the whole frame
[94:14] range then we can isolate this and we're left with only the points that are going to be sitting at
[94:21] the edge at one point or another so this is half a million points compared to 10 million points so
[94:30] this is just like a very small subset of the points and this is going to be a lot more efficient
[94:36] when we copy and when we instance geometry on it at render time now we have the animated version
[94:44] of this and you can see like the cylinder pattern that we're getting from just keeping the edges of
[94:50] those large chunks this is our usual prepping of the emission point for the second iteration
[95:06] so this is very similar to what we saw already this is our secondary emission
[95:12] and here this is a little bit different we're isolating the grass so also this is one of the
[95:18] reason why we were keeping the deformation gradient and the orientation we need now to copy some disc
[95:25] onto the grass layer and we're going to use those isolated discs as a skin to render fur
[95:34] so i'm not going to dive into the details of it because this is a little bit unrelated to npm
[95:39] but here we're setting this up inside of this subnet such that on one end we have the guides
[95:47] so I can display the guides here so we have the guides that we're going to use to
[95:52] interpolate and generate the fur on the skin and on the other side here we have our skin
[95:59] that is going to be used to put the generated grass we have to do the same thing for the static
[96:07] geometry so the exact same setup but for what is not being simulated and here we have our
[96:12] set extension just to fill the ground to the horizon then we can dive in lops
[96:21] so now that we're in lops we see our spaceship rendering with all the elements
[96:28] and we can take a look at them individually so now if I just look at the npm soil
[96:36] I'm going to jump out of the camera and zoom in a little bit so even if we know that this
[96:41] simulation is aphreas you see that this is very very smooth like this is not the kind of detail
[96:46] that you expect from soil so one thing that we can do is try to add those kind those uprising pebbles
[96:55] so those pebbles that we're going to copy on the surface now if I merge the two things together
[97:00] we can look with and without to see the difference
[97:09] so this would be with the added pebbles so it's not like a huge change but you can see that it's
[97:14] adding some high frequency detail and all of those pebbles are going to stick perfectly to this surface
[97:22] so this is going to be fine and now if we remove it you can see like this is much smoother and we
[97:30] have less visual details without them apart from that we have our secondary emission here
[97:37] just small sphere with color based on the rest of our UVs I don't exactly remember and here we have our grass
[98:01] and finally this is just our set extension so if I just connect everything back together
[98:08] we get this looking through the camera looks like this
[98:22] and this concludes our tour of the ship bridge scene let's now move on to the fruit smash scene


### MPM Advanced: Fruit Smash [98:25]
**Transcript (timestamped):**
[98:29] so we have this fruit we have some UV on it and then we want to decompose it into multiple pieces
[98:36] for simulation so we're going to have this crust so if we zoom in and see that the inside is empty
[98:45] we want to have the inside of this fruit and some seeds
[98:54] now here is our npm simulation so for the seeds we're going to start with the
[99:02] so in this case we started with the snow preset and we made the stiffness 100 times
[99:11] larger than it is by default and this might not even be enough so this might not be stiff enough
[99:16] to represent something as stiff as some seeds like that but you're going to see later on
[99:22] how we deal with some seeds that might be breaking up as the simulation is happening
[99:28] and I don't think there's anything special than here we're not even like noising any attributes
[99:36] for the skin again we're not adding any noise to any of the material attributes we're just
[99:44] adding some color to visualize a little bit and then same stiffness as the seeds so definitely
[99:52] you would expect this to be softer than the seeds but yeah we're gonna get back to it to this little
[99:58] later and then here we're making the critical compression and critical stretch twice as big
[100:04] as it is normally with this snow preset so this means that the material is going to be more wiggly
[100:11] so it's going to behave more elastically before the deformation becomes plastic so this is going
[100:17] to allow the crust to bounce on the ground and deform and wiggle more than by default
[100:25] and then for the inside of the melon we have the pulp
[100:30] and here the stiffness has been multiplied by 10 we're still using the snow preset but here
[100:38] we're multiplying this critical compression and critical stretch by 10 so again making the
[100:42] material behave a lot more elastically so this means that only very large deformation are going
[100:48] to be considered as plastic and change the actual rest shape of the material everything else everything
[100:55] else the solver is going to try to restore the original shape and this is going to make this
[101:00] part wiggle a lot more than some snow by default and now I want to talk about this parameter
[101:09] volume preservation and this is called new in the points attributes so if you want to see this
[101:16] on your points you're going to be looking for this guy new this is actually called the Poisson
[101:21] ratio in solid mechanics and this actually represents how the material is going to react
[101:29] perpendicularly to stress that is applied to it and I want to explain this in a little more
[101:35] details visually so let's say for example that you have a piece of jello like this and you stretch
[101:42] it in those directions in this case you're going to expect the jello to become a little bit like that
[101:52] okay so as we're pulling in those directions this direction which is perpendicular to this force is
[102:00] going to squeeze in that direction so it's going to preserve like the total volume that you add here
[102:07] it's kind of preserved here by this part getting thinner and thinner and this is why we set the
[102:13] label on this parameter as volume preservation the same goes for the opposite so if you have a
[102:19] force going in that direction on the jello then you're going to get maybe something like that
[102:23] so as this is pushing inward you're getting expansion here to preserve the volume of the jello
[102:33] and this is not something you see across all materials so for example if this is concrete and
[102:38] you just you just push on it like that it's just going to compress like so so maybe you
[102:46] can have a change of stiffness internally but it's not going to bulge out like you would get
[102:52] from jello same thing like if you pull on a piece of concrete then maybe it breaks this is most likely
[103:00] what you would expect but you're not going to get some like thinning happening here where the material
[103:06] is going to push inward so this is mainly what this attribute controls so for jello let's say you
[103:15] you expect this Poisson ratio to be around 0.4 like that and for concrete I think it's a little
[103:22] bit smaller than 0.2 but for snow it's differently 0.2 so just this small difference of 0.2 makes a
[103:30] very large difference in how the material behaves and just to show that inside of Udini I'm just
[103:36] going to lay down a mpm configure like so so we have our ball of snow falling on top of this wedge
[103:47] I'm going to remove the collider on the material source I'm going to make the stiffness 10 times
[103:54] higher and we're going to keep the volume preservation set to this then we add some initial
[104:02] velocity going downward and you can take a look at what we get okay so you can see that the snow is
[104:08] just like it's just simply collapsing on itself and there's no not a lot of reaction to this
[104:16] deformation going perpendicularly to this impact so we're not getting a lot of material shooting in
[104:22] all direction on this plane that is perpendicular to the downward initial impact okay but if we
[104:30] just change this parameter so let's say we double that 2.4 and we play this
[104:40] now we get a lot more explosive behavior so this is why I was initially referring to this parameter
[104:46] as how your material is going to be explosive on impact this is exactly why so you see like we have
[104:51] an impact and then the material is compressing in that direction so everything that is perpendicular
[104:56] so this plane this xz plane is going to kind of redirect the energy of this impact across the whole
[105:06] plane so it's going to make the material a lot more explosive and for this specific scene this is
[105:11] exactly what we're looking for so we want our fruit to hit the ground and to really like blow out in
[105:18] all direction because we want those nice pieces to fly in the air and to preserve their shape but
[105:25] we want like a lot of energy going outward to create the cool patterns
[105:34] so this is why on this npm source we have this volume preservation set higher than 0.2 so it's
[105:39] almost 0.4 here and that pretty much it for this material here we're adding some variation because
[105:49] this is going to be pretty like thick like this is completely full inside of points so to add more
[105:56] variation and more breakup we're just going to do our usual noise where we modulate the stiffness
[106:02] attribute then we set some colors and then we add some spin so some spin about the y axis
[106:12] then we put the fruit in context and we add some downward velocity so we have some velocity going
[106:21] in that direction in terms of the solver I think okay we only have this is again a slow-mo shot so
[106:31] we have this that is being modified and apart from that this is all default for the output we are
[106:41] outputting the deformation gradient and in this case we're not even changing it like we're not
[106:46] converting it down to a quaternion we're directly caching this three by three matrix
[106:52] a little bit of attribute cleanup here and this is being cached
[106:59] now if we look at our result we get something like that where the fruit is hitting the ground and we
[107:05] have this huge explosion with all the pieces flying in all direction and this is exactly the kind of
[107:12] it really depends on what you're after but in this specific scene we really want this to
[107:17] have a lot of energy going in all direction so this is good
[107:25] here we still have our usual sdf generation setup
[107:29] if we isolate just this the skin so just like the the crust of the of our fruit
[107:44] we're doing a dilation similar to usual we're also doing some smoothing
[107:50] the the one thing that differs is we're going to apply a second smoothing operation because we
[107:55] just want this area so the flat area of the crust we just want this to be a little bit smoother
[108:02] but we don't want to affect the edges here so what we're going to do inside of this subnet
[108:07] build stretch mask so here we just isolate the points that are stretching based on this jp
[108:13] attribute again and then we generate an sdf from it we dilate it we create a fog volume out of it
[108:20] then we use that as a mask to prevent the smoothing to happen on those edges so anything that is
[108:26] fracturing and stretching is not going to be smoothed more but this area is changing so we can
[108:33] see it if i go before after we see that the surface is a lot smoother now then we do another erosion
[108:41] as usual and we finally convert that to polygons and you can see that this is a lot smoother than
[108:47] these edges after that we need to transfer UVs but there's just little thing that we need to be
[108:54] aware of when we do this we have different UV islands so if we look at the original geometry
[109:01] this guy if we go to the UV view you see that we have three different UV islands so we cannot
[109:09] transfer the UVs just with a simple attribute transfer because when we're crossing this boundary
[109:15] going from one island to the other we're going to get very weird artifact in the UVs and I can
[109:20] show that right here if I go back in the viewport you can see here we have a seam coming from this
[109:32] is one island and this is another island and you can see that the transfer between the two is really
[109:37] really bad so we need to treat each of the UV island separately to avoid this so this is exactly
[109:43] what we do so here we have our npm point cloud sitting at rest so we're going to transfer
[109:52] in fact we're doing the transfer here of the UV and the class attribute we're having like one class
[109:58] one unique class per UV island and here we can visualize the result once this is transferred
[110:05] to the point so at the moment this is fine because we have each point is being projected
[110:11] with this ray operator it's projected to this geometry and each point can only pick a single
[110:17] UV island so we don't have any like interpolation issue the issues are going to happen when we
[110:22] transfer to the mesh because we have like a single polygon that could be sharing two different islands
[110:27] and this is what we want to avoid so for now just transfer that we identify each island
[110:32] then we're transferring those attributes to the moving points but after that we ultimately we want
[110:42] those attributes to be on the mesh so we transfer this class attribute to the mesh and then we're
[110:52] going into this for loop where we're going to iterate through each of the island so let's say
[110:56] this is one of the island where this is one island this is one that has been pruned out
[111:02] and this is another one that was removed we inside of the for loop isolate the same thing but for
[111:07] the points and here we do the UV transfer on the mesh and proceeding this way we can zoom in on
[111:16] the boundary between the two UV islands and you can see that now we have a like a clean cut between
[111:23] the two UV islands as opposed to what we use to have here without this trick of going through the
[111:29] for loop and after that we convert everything back to polysuit then we just transfer the
[111:37] velocity as usual here there's nothing specific to say just meshing the pulp
[111:46] so meshing this part and transferring the velocity at the end
[111:56] we get this
[112:00] and for the seeds there's going to be something different so for the seeds what's happening is
[112:05] that we have the level of stiffness of the seed is not that high as I was explaining a little bit
[112:14] before so here we have to identify the seeds that are breaking up and this is going to be
[112:19] done inside of this subnetwork so if I dive here and we look at our input so we have our points
[112:26] at rest that represent the seeds and we have our seeds geometry so first of all we're just going to
[112:32] transfer a class attribute to identify each of the seed like an ID and here we can visualize this ID
[112:39] so now we have some points like each points have been associated to a single seed now from there
[112:45] we just like transfer this attribute and make sure that it it's followed through what we're
[112:51] going to do now is to compare the first frame and the last frame of the simulation and we're going
[112:56] to compute inside of this for loop some kind of distance that represents how each seed has been
[113:02] distorted so here for example we pick this seed so those are some points that represent a single
[113:09] seed in the simulation here we are we just like create an oriented bounding box here we compute
[113:14] this distance which is basically like the sum of the edges that start from point zero to all of its
[113:19] neighbor we do the same thing but with the deform so this is like the last frame of the same seed
[113:25] in this case you see that there's not a lot of distortion it's pretty much all at the same place
[113:29] so when we compute the oriented bounding box and compute the distance it should be very similar
[113:35] to what we add at rest then we compute this difference this this relative difference and
[113:41] you see that this is very small so this means that this seed is most likely going to be preserved
[113:47] and not deleted so now we just transfer that onto a single point that is going to represent our seed
[113:56] so that was for the right branch here and the other branch here is basically like gathering all of the
[114:03] like it's averaging the position of so let's say this is like another another seed it's averaging
[114:09] those positions just to have one centred that represent the seed then it's taking all of the
[114:14] orient attribute and it's storing that inside of an array this area here with all the orient of all
[114:21] of those points then we're transferring that to a single point both the position and the area of
[114:28] orientation here we're going to this is probably not the accurate way of doing this but we're going
[114:36] to average the rotation of all the quaternions so we just like make a one single orient out of the
[114:44] array of the orient that we add this array here so we're just converting that to a single orient
[114:53] attribute and finally looking at the diff attribute that we computed here we're going to prune out all
[114:59] of the points that we consider to be broken so they have like separated during the simulation
[115:07] and we only want to keep the seeds that are not breaking apart so we used to have like a little
[115:13] bit over 10 000 seeds and after the separation we're left with close to 9 000 seeds so not that bad
[115:20] at all and after that when we have those centred this is going to be very similar to what we're
[115:25] used to do with the bullet so we use like the transform pieces to uh and stand those seeds so
[115:33] this geometry we and sense it using the class attribute to identify each seed and we just
[115:39] retarget their position with these transform pieces like so
[115:44] so this is going to be the geometry that we render for the seeds
[115:53] and finally we have just the same setup that we used to have so we prepare the emission points
[115:59] for the secondaries and we do the secondary simulation here so in this case it's just going
[116:05] to be like droplets of water to have to add this high frequency detail that we that we want to see
[116:10] in this kind of sim after that if i jump in lops
[116:19] so we have this scene
[116:24] and again i can look at all the components individually so we have our pulp
[116:31] so this is our yellow material with mainly like subsurface scattering and some specular highlights
[116:36] so we have our seeds
[116:46] then our skin
[116:55] and the secondary water points so just little something to pick up a little bit of
[117:01] highlights and add this high frequency level of detail
[117:06] and we have a grid for the ground you can merge everything back together
[117:11] a simple edge r i light for the light setup and then if we look to the camera
[117:19] you get something like that
[117:22] and this is what concludes our tour of this fruit smash scene


### MPM Advanced: Ice Cream Scoop [117:27]
**Transcript (timestamped):**
[117:27] let's now jump into the ice cream scoop scene
[117:35] so this scene is going to be a lot simpler i think compared to the other one
[117:39] so we start with this animated spoon and we're basically going to grab some ice cream
[117:50] so this is our ice cream this is our spoon and we're just going like that grabbing some ice cream
[117:56] we want this to like swirl inside of the spoon and then this gets dropped down inside of
[118:06] this cup so this is where the ice cream is supposed to fall in the end so
[118:13] pretty simple setup the only thing that we need well first of all we take this ice cream and we
[118:19] split that into two different parts so this is going to be like our static ice cream we don't
[118:24] need to simulate that and this is going to be our dynamic ice cream
[118:33] in terms of the material itself this took a little bit of trial and error because the tree part of
[118:39] this material is like if i look at the if i go to the meshing step
[118:47] and i visualize maybe frame like in this area 70 something like that
[118:54] maybe a little bit before
[119:00] okay so this is what we're looking for like we want this to create a spiral like this but we
[119:05] don't want this to collapse and break so it took a little bit of trial and error to figure out
[119:09] like what were the proper material property to get this to just swirl without breaking and falling
[119:16] and if we look at the mpm source on the first frame we can see that okay first
[119:24] i've moved the critical compression and critical stretch further away so the material is going to
[119:30] behave a little bit more elastically compared to the default snow then i'm completely removing
[119:35] this compression ardening it might sound weird but when you do compression ardening it will
[119:43] make the material break more easily because it's like your material cannot flex that easily so it's
[119:49] only other option when it becomes too stiff is to break basically so that's why for concrete if
[119:54] you remove this so if you put compression ardening to zero concrete is never going to look like
[120:00] concrete because it's not going to break at all so we want the opposite behavior in this case we
[120:07] want things to flow more organically we don't want things to break so set that to zero for the
[120:13] stiffness we use the default stiffness for the snow preset and here volume preservation we
[120:19] set that to a quarter of the original setting again when we compress the snow when we have our
[120:26] spiral building up we don't want this deformation to trigger some perpendicular forces like
[120:36] perpendicular motion going outward because again this would trigger a fracture in the
[120:42] material and it will break our spiral of ice cream so this is why we're setting this that way
[120:47] apart from that we just have colliders after that so one collider for all of this that is static
[120:54] we're setting the friction and stickiness to two we want things to be pretty sticky like if some
[121:00] ice cream falls on top of the static ice cream we don't want that to slide as you would expect in
[121:05] real life but then for this cup that will receive the ice cream we want to mimic the fact that when
[121:12] you have ice cream touching a cup like this this is going to be warmer than the ice cream so the
[121:19] ice cream is going to melt as it touches this material and the thin layer of melted ice cream
[121:24] between the ice cream itself and the glass is going to make the contact between the two very
[121:30] very slippery so we expect the ice cream to fall in and really like spin in this container so for
[121:38] that reason we set the friction very very low but still not completely to zero and for the scoop
[121:45] itself we want the ice cream to be able to swirl in there without too much dynamic friction but we
[121:52] still need a little bit of friction too so setting that to point one again there's no magic recipe
[121:58] just a lot of trial and error to find the right balance and the right look depending on what you're
[122:03] trying to do now looking at the solver we almost have everything at default the solver itself the
[122:09] solver tab nothing has changed visualize is at default for the output we're just not caching
[122:16] velocity as usual but here in the advanced tab we're doing something different we're enabling
[122:21] this checkbox that i never talked about and now we're going to explain it enable particle level
[122:26] collisions and there's multiple modes and the mode that we're using at the moment is velocity
[122:31] based move outside colliders okay so just to explain this part i'm going to go in the drawing
[122:36] software so with npm you can do particle level collision the reason for this is because when
[122:42] you do only grid level collision so this is what you get by default you can have some particle
[122:47] that will drift inside of the collider so here we have like this collider set in orange and this
[122:54] line in yellow this dotted line represents the middle of the collider so as soon as you have
[123:00] a particle that crosses this line so if we have like this particle as soon as the centroid of it
[123:06] will cross this line it will no longer be pushed in that direction to exit the collider it will be
[123:11] more pushed on the other side and this will look like you have particle flowing through the collider
[123:17] which is most likely not what you want so because in npm you get the transfer from particle to grids
[123:25] and then grids back to particles you get some fuzziness you get some imprecision and some drift
[123:30] you can get some particles that will sink inside of the collider but you have three ways where you
[123:35] can compute the collision on the particle to solve this issue so the first way is just to
[123:41] actually do the collision response on the particle so very simply if you have a velocity like this
[123:47] particle and it has a velocity like this it can just be projected onto the collider so instead of
[123:54] having the velocity going inside like this it will be projected to this kind of velocity going
[124:00] tangent to the collider it all depends on the material type but in this case if there's no like
[124:07] bounds if there's no like elastic response from this collision it will just be projected
[124:14] tangent to the collider like this but you can do more than that you can also do this and also move
[124:20] the particle outside of the collider and this can be helpful in some situation because it will
[124:27] not only stop the particle from drifting but it will also make sure that the drift is being
[124:33] corrected at every single time step so if we do it based on position it will just take this particle
[124:39] which is detected inside of the collider and it will move it this way the problem here is that
[124:45] you get a loss of volume because nothing in terms of velocity will reflect this change and now you
[124:51] have like two particles sitting on top of each other so you have a loss of volume and you're likely
[124:56] like over sampling this area of the material because you have basically two particles sitting on
[125:01] top of each other the third way you can do this is by changing the velocity of the particle
[125:08] so we have the velocity of the particle going like that you can first project it like this
[125:16] but you can further correct it such that it will take the particle and move it outside
[125:22] of the collider on the next integration step so in this case you have some velocity that will
[125:29] represent how the particle should be moved outside of the collider within a single sub step and this
[125:35] will result in making both particles so the particle that was drifting inside of the collider but
[125:42] also its neighbor it will force both particles to go completely outside so in this case you don't have
[125:48] a loss of volume you don't have over sampling this is the most physically accurate approach
[125:54] of dealing with the particle level collisions but just keep in mind that the velocity is corrected
[126:00] such that this particle is moved completely outside within a single time step so in some cases
[126:05] if you have this particle way inside of the collider the velocity is going to be very very
[126:09] strong in this melee tool and stability just something to keep in mind so again inside of
[126:15] Udini we have those three modes don't move outside collider is just the original collision
[126:22] response applied to the particles position-based move outside colliders is just changing the position
[126:28] without adding any kind of velocity attributes in the system representing this correction
[126:34] and velocity base move outside collider which is the default and should be the first option you try
[126:40] if we look at the final result we get something like that where the ice cream is rolling then it's
[126:48] being dropped and then it's spinning in the cup exactly like exactly like what we wanted if I display
[126:56] the cup as template
[127:05] so yeah exactly as what we wanted
[127:10] then if we look at the final result look at this I felt that this part was a little bit too granular
[127:17] a little too chunky so I'm doing one step of this called like smooth ice cream just to smooth
[127:23] this part so the part that was in contact with the spoon if we look at before and after we get like
[127:28] some smoothing happening here I'm basically just trailing the animation of the spoon I'm keeping
[127:36] only what has been in contact with the ice cream I'm doing a projection of the simulation onto this
[127:42] geometry and then yeah so this is doing a lurp where I'm only doing this projection for the points
[127:52] that are very close to this to where the spoon is going and after that I'm animating this projection
[128:01] because I only want this to happen after the spoon has passed so at the beginning I want things to be
[128:06] perfectly at rest without any disruption but then as the spoon is passing by I want the points to be
[128:12] projected to get like this very very smooth surface so if we look at before getting here so here the
[128:18] points are completely untouched completely at rest and as the spoon is passing you get all the
[128:25] points being moved slightly to create this smooth surface so here like this lurp from
[128:31] current position of the simulation to the projected position and we use this delta as a mask and the
[128:37] delta is generated by looking at the difference between the current position of the sim and the
[128:43] rest position so pretty typical setup that you see in Udini for this kind of effects
[128:50] and and then I'm setting the color so I'm just merging all the points together so the static
[128:56] representation of the ice cream is being merged with the dynamic representation
[128:59] and then we use this Udini logo to get some cool colors going in the ice cream
[129:05] like so
[129:12] then we have our usual sdf and meshing setup here we're using the exact same trick that we're
[129:19] using for the fruit being smashed so we're building this stretch mask and we are going to smooth
[129:26] everything but the things that are stretching
[129:33] so if we get closer and you look at the results so this is with the additional smoothing this is
[129:40] without you can see that it really helps like this part of the ice cream to become more flat
[129:46] but it doesn't break like it doesn't remove a lot of details from this edge here so this is
[129:50] exactly what we want and then we finally convert that to polygons transfer velocity and color
[129:58] and we're good to go the rest is just like to prep the other geometry for rendering
[130:04] then if I go to lighting
[130:08] get this rendering so again I can decompose the different parts so we have our ice cream
[130:21] then we have our tub with this cool logo of the npm collider
[130:26] the glass here that is receiving the ice cream our just our backdrop basically and the spoon
[130:42] and that's it if we merge everything together in this case I'm using two hri to really get a lot of
[130:48] I don't want a lot of areas to be very dark in each shadows for a product shot like this you
[130:52] want lights to be coming from almost everywhere and you want those cool highlights so adding a secondary
[130:58] a hri light like this really helped me to get some cooler highlights everywhere
[131:04] and then we just had the camera being merged in very similar to the other setup as usual
[131:11] and this is what we get
[131:13] let's now take a look at the obol explosion shot


### MPM Advanced: Hubble Explosion [131:14]
**Transcript (timestamped):**
[131:22] okay so here we have this obol geometry this obol model and then we have some boxes that
[131:29] are flying in all directions starting from the center of the model and we're going to use them
[131:34] to carve some holes and to basically blow up the stiliscope so in terms of the npm source
[131:42] we have something like that and by the way when you select that for the first time it might take
[131:49] a little bit of time to cook because we have some by default we have this segmentation thing set to
[131:55] name attribute and here on the model we can see that we have this name attribute so it's going to
[132:00] iterate through each of those pieces and generate some points for each of them and then merge the
[132:06] result back together and in this case this is perfectly fine because the model is pretty large
[132:11] and we're actually relaxing the points on top of the surfaces so if you do the whole model all
[132:16] at once it might take more time than splitting it into different pieces like this so this is all
[132:22] good and then if we have some overlapping points after going through this node we can just use them
[132:29] so here we have this fuse node that is referencing the particle separation on the npm container
[132:35] just to take care of that then for the npm source this is basically just the middle preset
[132:41] out of the box no change has been applied here the one thing that is different is normally we're
[132:47] using this type volume for to source the point on the model in this case we're actually sourcing on
[132:53] the surfaces and as I was saying we're also doing some relaxed iteration just to make sure that our
[133:00] distribution of points on top of the surface is very uniform I think that's pretty much it for the
[133:07] sourcing and then we're also doing something special for the colliders so we have those boxes
[133:13] flying away and this could be just a deforming collider just a single ptb but when you go from
[133:21] one frame to the next like this you won't have very precise interpolation of motion if you use
[133:27] deforming to get the best quality in terms of collision again just use your animated rigid type
[133:35] this guy here this is going to generate a lot of colliders as you can see so in total we have a
[133:41] 270 different vdb colliders but this is going to give you the most accurate results but also
[133:48] keep in mind that it will slow down things a little bit like when you have 10 20 colliders it's not
[133:56] that noticeable but in this case when you're going through the hundreds of colliders the solver has
[134:01] to iterate through each of them so yeah you can get a little bit of a hit performance from increasing
[134:08] the number of colliders that much it always depends on the the case and the situation you're in
[134:16] then we're just picking the telescope and we're adding some padding to it so 10 across all the
[134:22] direction and we set that as our domain and we're going to delete the points that are escaping this
[134:28] box if we look at the npm solver this is all default we're just not caching velocity
[134:40] on the solver itself i mean on the solver tab we are changing the timescale because this is again
[134:45] a slow motion we are clamping the maximum amount of sub steps to 200 so we just want to make sure
[134:51] that we don't pass this amount of sub steps per frame and we are disabling the ground plane oh and
[134:58] also since we're in space we're also getting rid of the gravity just so all pieces are free to go in
[135:04] all direction now if we look at the simulation that we're getting from this
[135:14] we get this kind of effect
[135:23] and you can see that this works pretty well so we have holes being carved into the body of the
[135:29] telescope we have some metal tearing going on with some bits that are still hanging on creating those
[135:35] cool organic shapes and close to the impact we have a lot of metal just being bent
[135:45] outside like going outside of the the body of the telescope and all of that is plastic
[135:50] deformation so it's going to just hold this shape as this large piece is traveling in space
[135:57] so just very interesting details that we're getting almost for free we haven't done a lot of work
[136:03] to get this going
[136:08] then for the meshing this is very similar to what we were usually doing to generate our
[136:15] sdf representation the one thing that we're doing different is happening in this sub network so if I
[136:22] dive here this is actually building a mask for two things we want to apply a smooth on the smooth
[136:30] surfaces but we want to preserve where the metal is tearing and we also want to preserve details
[136:35] where the model has some interesting curvature interesting like sharp features so in this subnet
[136:41] we're trying to build a mask to protect those areas so on that branch on the left we're going to
[136:48] extract the sharp feature from from the model so here we just do a conversion from sdf to polygons
[136:58] then we smooth the polygons further then we compute the curvature that we transfer to the
[137:03] derivatives and finally we extract all of those eye curvature areas after that we just build an sdf
[137:10] representation from it on the other side we extract everywhere that is tearing so basically
[137:17] this jph reviewed then we build an sdf dilate smooth and we combine that with our curvature mask
[137:26] all of that gets converted to a fog a fog volume and this is what we use as a mask to not smooth
[137:34] those areas so here if I zoom in a little more on the model we can appreciate what it's doing
[137:44] so this is with the smoothing this is without so you can see like this panel here on the telescope
[137:50] is getting a lot more smooth this is great but you can also see that well in practice this
[137:58] geometric detail would be completely preserved but remember that we're running at half the
[138:02] resolution so if you want this to be properly preserved just make sure that you run this all
[138:08] setup with this res multiplication set to one instead of two just to get the same resolution as
[138:14] what we've been showing at the beginning of the masterclass but for now to keep things interactive
[138:19] we're not necessarily getting the best results but yeah this mask should be protecting all of those
[138:24] eye curvature area and also where things are tearing right here so again this is without the smooth
[138:32] and with this smooth on the other side we're just gathering the velocity down raising making it
[138:40] invisible and then merging all that for the sdf representation of our mpm simulation
[138:47] then this is actually where we're doing the meshing of everything
[138:54] so we convert the sdf to polygons then we just sample the value from the volume representation
[139:02] on the other side here we're grabbing the original model with the rest attribute we're
[139:06] grabbing the first frame of the mpm representation of the model and then we just transfer the rest
[139:15] attribute from the model to the points at rest and then after that we transfer from the point at
[139:21] rest to the point in motion and finally we do the transfer from the point in motion to the polygon
[139:28] representation of the telescope after that we convert that to a polysum just to make that as
[139:36] light as possible on disk or in the RAM and then I'm not going to go into details for this is what
[139:45] we've seen across all the the setup this is all always the same we're preparing the points for
[139:51] secondary emission we're doing the secondary emission here the one thing that is different
[139:56] from what we had before is this here we're building a collection of small bits of this telescope to
[140:03] use as debris from the secondary emission so if I dive in here you see that we have our model
[140:08] that we're just segmenting based on connectivity then we run over each piece and we're measuring
[140:16] the size of them then we just keep the very small pieces and you can see that we have very interesting
[140:23] geometric details in those small pieces so after that we just do a bunch of things basically to
[140:30] put them at the center end so they are ready to be in stands like so and we also set a path so this
[140:38] is what is going to be used in usd this path here here just pay attention that we have 1454 pieces
[140:48] and we're going to need that information when you set the index attribute on the points
[140:54] so here this is where we define what pieces is going to be in stands on each point so we have our
[141:00] random point from zero to one that is being multiplied by the amount of unique pieces that we
[141:06] have in this collection and this is what is going to be used at instancing other than that we're
[141:12] just changing the p scale as usual and setting some random orientation to get some variation there
[141:18] after that we can look at our simulation so this is the secondary
[141:28] secondary simulation that we have
[141:33] this is way too much point as it is right now but we can just do
[141:40] some more pruning here just to make sure that we're not excluding completely the npm simulation
[141:45] and this is what we get in subs now if you go in laps
[141:59] we have this going on so a very simple setup on one end we have the telescope
[142:05] so our telescope mesh
[142:16] i don't think that there's a lot of textures being applied to this if we type in the material library
[142:24] so there is some texture being used here of rusty metal
[142:33] and this is all applied using the rest so it's not even using like a UV attribute just based
[142:39] on the rest doing some remapping here we can apply those two textures just to add a little bit more
[142:45] variation on the surface and then i think we have something similar going on for the debris
[142:55] if we look at the debris in isolation you can see that we have very cool
[143:02] geometric details that we wouldn't have if those were just sphere being instanced and this is going
[143:09] to catch some highlights and create some very cool details as they are rotating outward from the
[143:15] explosion center and in terms of light setup again we have just a gri for some star reflection
[143:25] in the background and we have a directional light to get this very strong
[143:30] it like specular highlight on one side of the model then if we look to the camera
[143:38] this is what we get last but not least we need to take a look at this building collapsing


### MPM Advanced: Building Collapse [143:40]
**Transcript (timestamped):**
[143:46] okay so here we have our building and it has an interior that looks like this
[143:56] and it has an exterior well this is the exterior and interior combined looks like that
[144:03] if we look at the npm source we're basically just using the concrete preset
[144:11] simple as that i don't think there's anything else being said here
[144:18] after that we're noising this stiffness attribute like we're used to do we've done that thousands of
[144:23] time by now so yeah i'm using this noise attribute to add some variation to the
[144:30] stiffness so it will crumble in more interesting patterns
[144:39] then for the npm container it's completely open so there's nothing going on here
[144:45] and for the solver itself we have everything at default here and for the output we are
[144:51] outputting this deformation gradient in this case we absolutely need this to do the proper retargeting
[144:57] we don't save the velocity as usual and those two things well yeah since we're not deleting points
[145:04] we don't need an id and then this doesn't really matter since we're not using a pin to animation
[145:10] in this scene okay that's good then if you look at our final simulation with those settings get this
[145:28] so
[145:45] so it seems like there's not really a lot happening at the beginning of the simulation like all of this
[145:51] part almost nothing's happening it really starts at around a frame 300 for some reason so again i
[146:00] know i said that like 10 times already but we're seeming at half rest at the moment so if you want
[146:08] to get closer to the original simulation that you've seen at the beginning of the master class
[146:12] just set that to 1 and it will be more detailed and probably closer in terms of the motion and
[146:19] behavior to what you saw in the demo clips but here for some reason we're just getting a lot of
[146:28] nothing happening here and then from 300 to 500 things are more action packed and the building
[146:35] is collapsing in any case this is going to work perfectly for our example we don't need more than
[146:41] that now if we take our empty end points and we do our usual conversion to a side distance field
[146:52] so we have our sdf with the velocity field this is going to be used for the as a collider for the
[146:59] secondary scene again we have our usual setup where we're using the gp attribute to do a emission
[147:07] so just as a i just so you remember we're using like at the moment we're visualizing this jp
[147:17] attribute so everything that is breaking and stretching will be closer to red and everything
[147:22] else that is almost not deformed is this purple color so we're going to use those fracturing
[147:29] area to emit secondary debris and get some interesting visual going on where things are fracturing
[147:38] after that this is where we're doing our simulation secondary simulation and it looks like that
[147:46] because nothing happening at the beginning and then from 300 to 500 things are really starting to go
[147:55] so this is what we have and in this case in this setup i still have those like round debris
[148:02] i don't think i'm using that in lops i think we're just rendering points but you could
[148:07] if you want copy some rocks onto those points and it would probably look better than just rendering
[148:13] spheres but both should work as well now we're entering the interesting part of this setup
[148:20] because everything upstream here is very very close to what we saw in all the previous scenes
[148:26] but this part here this is quite unique to the building collapse scene so first thing
[148:34] we're going to oppress the geometry a tiny bit so just add more subdivision now i'm going to display
[148:41] the mesh so here i'm isolating the interior representation and i will add this divine
[148:48] node just to make sure that the polygons are not too elongated so i don't want any like polygon to
[148:53] start here and end there so i want all the polygons to be relatively small in relation to this geometry
[149:01] and we're going to do the same thing for the exterior as you can see like let's say this
[149:05] polygon here is pretty tall we don't want that we want smaller polygons to work with so for that
[149:12] i'm just going to apply some border fracturing just so we have smaller polygons like this
[149:18] then we merge everything together and just pay attention to the fact that this geometry at the
[149:28] moment it's completely single sided okay so in like a more realistic scenario you would have
[149:37] geometry that is like convex manifold something that is closed where you would fracture it and
[149:44] actually like generate pieces that have some volume in this case as an optimization just to
[149:49] make the scene simpler we're only going to work with polygons so like the pieces that i'm going to
[149:55] try to retarget onto the npm points are just going to be simple polygons and then we're going to do
[150:01] an extrusion on it at the end just before rendering this is not like necessarily the the best order
[150:06] recommended workflow but this is just like one workflow that kind of works in this case and
[150:12] it's lighter on memory and it's just more interactive that's why i'm going this route in this case
[150:18] but it's gonna make more sense later on just bear with me so here i'm splitting the geometry
[150:26] this part of the setup is again just to add more detail so just to fracture this building more but
[150:33] this is the post fracturing so it's fracturing the building in context to what's happening in the npm
[150:38] simulation so we merge our building then we merge our npm simulation well the first frame so the rest
[150:48] frame of our npm simulation and then the last frame now we're going to sample this jp attribute
[150:55] and copy it to the first frame so now we see by looking at this representation exactly where things
[151:04] are going to fracture so we know at the last frame this is how our building is being fractured
[151:11] and we're going to use this information to post fracture the iris geometry and later on do the
[151:17] retargeting so how it's going to work is here we're pruning all the points that are too far away
[151:24] from the surface so all the points that are kind of inside of the volume we're not really interested
[151:29] we really want the points that are sitting on the surface and you can see from this that now we're
[151:37] isolating where things are going to break and we have very high density of points where fractures
[151:43] are going to happen on the other hand even if some areas are not fracturing like maybe in this area
[151:51] we still need to have some level of fracturing because this piece might be bending so we need
[151:56] some subdivision to be able to represent this deformation and this curvature so we're also
[152:03] going to scatter even distribution of points across the whole model so this is like our basic
[152:08] level of fracturing and this is our very fine level of fracturing to be able to represent
[152:16] things that are breaking apart when we merge that together here we do a split to since we're
[152:22] going to see more of the exterior we're going to fuse some points but anything that is inside of
[152:28] the building we're going to be more aggressive on the fuse so we're doing a fuse of two here
[152:32] we're getting rid of a lot of points just to make that more interactive and more efficient
[152:40] and for the exterior we're also doing some fusing but not that aggressive so four times less
[152:46] aggressive in terms of the fusing just to keep more points where things are actually breaking
[152:53] after that we're also going to partition our building so we grab this building so this is
[152:59] the representation that we had here and then we scatter 500 points in this case and we're going to
[153:06] partition the building such that when we fractured the building we're going to fracture it partition
[153:12] per partition just to make this more efficient this is just an optimization to get this going
[153:18] faster and here we're basically just isolating one of those partitions we're isolating the points
[153:26] that are associated with this partition and we're doing the fractures here
[153:33] after that we're assigning a name and this process is being repeated for all the partition of the
[153:39] building until it's completely fractured everywhere after that we're making sure that new polygons
[153:47] has more than four edges a little bit of housekeeping there setting rest attribute packing things
[153:55] and then we're just caching that and this is going to be like the post fractured version of this
[154:02] building then the final part of the setup this is the retargeting and there's going to be
[154:12] two types of retargeting so here we are retargeting based on points here we are retargeting using the
[154:18] center of the primitives and then at the end here we're going to blend between the two types
[154:24] so the first type here okay so first of all we're bringing our building on packing then we're going
[154:31] to capture each point here on this drawing is going to capture the nearest mpm point at rest
[154:40] so this is what we're starting here and after that we're going to do the retargeting so if we
[154:46] look at the result you can see that we have a lot of stretched polygons but this is perfectly fine
[154:52] so what's happening in this node is that for each point of this geometry as I said we're going to
[155:00] grab the original position of the npm point at rest and we're going to subtract this offset so we
[155:08] are sitting like in the space of this npm point then we apply our deformation gradient our f
[155:15] attribute here we apply the animated deformation gradient at that frame and then we apply the
[155:22] position offset of this npm point in space this will yield very good results where things are not
[155:32] fracturing so this part of the building is going to be deformed a little bit but the retargeting
[155:38] is going to work well for these parts but all of the area where things are fracturing you're
[155:43] going to have maybe one point of one npm point that is going to pull in one direction and another
[155:50] npm point that is going to go in a totally different direction because the material is
[155:53] fracturing and this is going to create those very elongated polygons so on the other hand
[155:59] we're going to do the same thing but based on the primitives so here we're retargeting on the
[156:03] primitives and based on this centroid we're going to capture another npm point and we promote that
[156:11] captured point to the point instead of being on the primitive and then we apply the exact same
[156:18] recipe here so now we don't have any stretching so all the polygons are maintaining their exact
[156:26] same shape but they are being transformed based on a single npm point sitting closest to their center
[156:33] so now we have this like a shattered glass look here and we have this very liquidy look
[156:41] going on here we kind of need to bridge both looks together and to blend them
[156:47] this is exactly what is happening here so this is what we're going to do at that step and the way
[156:53] we're blending between the two is with this t value here and as you can see it's using this
[157:00] distance and this rest distance and the way this is computed you can see it here
[157:08] for each of the primitives we're going to grab the first point of the primitive and we're going to
[157:13] compute the distance between this point and all its other neighbor and we're gathering and aggregating
[157:19] this length into this this point attribute so we're doing that for the deformed this deformed
[157:28] and retiring based on points but we're also doing that for the rest geometry here so when
[157:36] we go to blend between those two we're simply comparing so if we have this if this deformed
[157:44] this is the same as this rest this we're going to get the ratio of one here so we're going to pick
[157:50] the position which is going to be this result here so this is what's happening here but if we
[157:57] have very deformed polygon very elongated polygons like this it means that this value is going to be
[158:03] much larger than this one so we're going to be remapped to one and in this case we're going to
[158:09] pick up this position here which corresponds to the retargeting based on the primitives
[158:18] so with that in place we're able to get a lot of polygonal detail where things are breaking
[158:24] and we're able to get like smooth deformed surfaces where things are just being deformed but
[158:29] we're not fracturing from there we're just sampling the velocity here very simply and after that
[158:37] we're just extruding the geometry because as you can remember there we still have some single sided
[158:44] polygons for the walls so we just need like to poly extrude we compute the normals and we get
[158:49] something more sensible for rendering
[158:54] so yeah as I said before this is definitely not the ideal workflow this is just like one
[159:00] workflow to get you going to give you some ideas of how you can approach this like how you can try
[159:06] to retarget npm simulation onto high resolution meshes in this case we can even see that we have
[159:14] the UVs properly retargeted so you can use that to a texture and this is actually what we're doing
[159:22] in labs but yeah in reality in a production environment you this would not be like
[159:33] retargeting based on the primitives you would be retargeting based on the pieces so each fracture
[159:39] pieces would be retargeted here then this part would probably be kind of similar to this and then
[159:46] you would blend between only moving one piece with a single npm point or moving each individual
[159:54] point of the geometry with this kind of retargeting but it would be kind of similar to this you can
[159:59] also instead of using a single npm point you can use weighted average to gather more points so this
[160:05] capture no deer could be a lot more elaborated where you look at more neighboring points and you
[160:12] weight their contribution based on distance using some kernels there are many many ways to expand on
[160:19] this and make better setups and for our lab network this is very simple we just have our
[160:30] building as one import we have our secondary particles in this case they are not too visible
[160:39] here but yeah you can see them here they are just rendered as shaded spheres but it could be a
[160:47] more more detailed geometry and as you can see if we zoom on piece of geo like this you can see that
[160:55] we have some texture well we get this motion blurred but yeah there's some texture applied to the
[161:01] surface to get some more details and in this case we have like two uh parameter nodes because we have
[161:08] two cameras so there's like a close-up shot and more like an environment shot where we see the
[161:13] whole building okay now that we're done with the more advanced scenes I want to tackle the npm


### MPM Subtleties: Tips, Tricks and Troubleshooting [161:14]
**Transcript (timestamped):**
[161:19] solorties so this is just a bag of miscellaneous tip and tricks and troubleshooting just to help you
[161:26] avoid some of the gutture that you will encounter with npm so let's jump into edinia now so here's
[161:32] all the little things that I want to talk about so let's start from the top I talked a lot about
[161:38] precise and fast collisions one thing to keep in mind is if you have a collider like this okay it
[161:44] might look like an obvious case of a deforming collider but in this case for crack we have like a
[161:49] bunch of different a bunch of isolated rigid parts that are being rigidly transformed but nothing is
[161:56] actually deforming if we look at each piece individually so what you can do is just select
[162:01] our npm collider and you can just set it in admitted rigid mode as we're seeing here and you get this
[162:10] segmentation option it's going to look up the name attribute on those pieces and it's going to treat
[162:14] them individually and generate a single pdb per piece and you get this obviously it creates a lot
[162:20] of colliders so in this case you have 67 colliders instead of a single one but as I said multiple
[162:26] time and you have more precise interpolation of the rotation and the translation and it should
[162:32] lead to a more accurate collision but in this case since we have a high number of colliders
[162:38] in some cases if you don't need very accurate collision you might prefer to go for a deforming
[162:42] but I just want to I just want you to know that you can sometimes decompose a deforming collider
[162:49] into a smaller rigid pieces now let's move on to tin colliders before I talk about tin colliders I
[162:58] just want to talk more about the water in fact the liquid behavior so if we select this npm source
[163:05] so here we are using the water preset this uses the liquid behavior and here you have all the
[163:10] parameters that you can tweak to modify how this liquid will behave those two parameters are the
[163:16] most important to know about you have incompressibility and strict incompressibility so it might
[163:23] sound confusing because you have two parameters that seems to be doing the same thing and they are
[163:27] kind of doing the same thing in this case you have this first parameter that is going to behave
[163:33] in fact to react linearly to change in volume so when the volume of the water gets compressed
[163:39] this is going to react to it but with a linear relationship to the pressure as opposed to this
[163:46] guy which is going to react with a power okay so if you have like very very small change in volume
[163:52] this is going to respond very violently and this number is here is the power that you're using to
[163:58] raise the change in volume so if you don't want the sub steps to explode to very high value you
[164:06] can restrict this value to a lower number like if you set that to one now you're no longer
[164:12] raising this change in volume to a power so the sub step is going to be maintained lower but you
[164:18] will also get some changes in volume like the the liquid will be able to compress and expand a little
[164:25] bit more than if you have that set to seven always depend on the shot if incompressibility is your
[164:30] main concern keep that at seven but if it's just a little puddle of water that you don't really see
[164:36] if it's compressing or not you can get this down and get faster simulations also if you set that to
[164:42] one you might want to increase a little bit this multiplier okay now back to the collision thing
[164:49] if we select this collider it's wine glass you can see that this is very thin
[164:54] we've seen we've seen a thin collider with the ice cream scoop before so this is the same thing
[165:02] again you basically just need to select the npm solver and you just make sure that you have
[165:06] any practical level collision enabled and you can keep the velocity based mode which is the
[165:12] best one to choose from and now if we look at the result you get something like that so we get
[165:20] some liquid coming from this wine glass being poured into the other wine glass
[165:27] and now if I just disable the visibility of the collider so we can focus in the liquid itself
[165:32] we have this which works very well there's two things for this to work as I said we need this
[165:40] particle level collision but we also override the resolution for the colliders so on this npm
[165:45] container we're setting the resolution to this value but for the colliders we're going to
[165:52] override this resolution so we can get finer details if we don't do that so if I bypass this
[165:58] overriding we get this so this is going to be our representation of the collider and this is obviously
[166:04] not going to work and just to show you if I disable the enable particle level collision and if we
[166:11] send that now we get all the liquid just falling on the ground so obviously not the best result
[166:23] and that is that is it just changing the resolution to make sure that you probably capture the
[166:30] the thickness of your collider and enable particle level collision and you should be good
[166:35] let's move on to continuous emission
[166:40] in this case we have this pig receiving this stream of water at the moment it works well
[166:48] like we have some smooth emission here because we're doing multiple dub sub steps so here you
[166:54] can see global sub steps is enabled and we're doing three sub steps but by default this is going
[167:00] to be disabled so we have only one dub sub step if I run this we get this stepping artifact so in
[167:07] this case you want to get rid of the stepping you need to source multiple times between two frames
[167:15] so it can be any number depending of how fast the stream is going but in this specific case
[167:20] treat dub sub step solve the problem and give us this very smooth stream of particles
[167:30] now let's look at dive targets
[167:36] this is something we looked at previously but very briefly in this scene we have this kind of
[167:42] village very low-res village and we have this tornado we can visualize the velocity field so
[167:50] this is basically just just a velocity field representing the force that or like the velocity
[167:57] that would be around this tornado and what we're doing is we're sourcing that into the dive target
[168:03] with just a simple pop wrangle here we're sampling we're sampling the velocity for each of the
[168:11] particles then we're adding this velocity to the velocity of the particles and this line can be safely
[168:17] ignored this is just like some drag so you can use this or you can do a drag the other ways by
[168:23] using other pop nodes or using the global settings on the npm solver
[168:30] when we run that we get something like that
[168:42] so this is important to realize how customizable npm is because of this dive target
[168:49] so a lot of those more complex setup will be achievable and you can be very creative by using
[168:54] this dive target to modify how the sim is behaving as it runs
[169:02] now let's talk about pin constraints so by default let's look at our pig model if we fill
[169:11] that with particles and what you can do here by default this is going to be set like this
[169:18] so you can enable pin constraints by checking that and this blue outline tells you that all of those
[169:24] particles are currently pinned so if I bypass this node and send that it's actually simming but it
[169:32] looks like nothing's happening this is because the npm solver is working so it's doing all the steps
[169:39] that normally does but those points are being constrained to stay put this is not a very interesting
[169:44] simulation so what we can do is to make the particle not pinned at the beginning so you can
[169:52] just initialize as pin and just bypass that so now so this was before and now after nothing is
[170:00] being pinned but the attribute the pin to animation attribute exists here what we're going to do is
[170:07] we're going to isolate the core like the center of this model and we're only going to pin those
[170:13] points so the points sitting at the very core of the model we do that with this point wrangle so
[170:21] whatever is inside of this sdf shape we set this into animation attribute to one and in this case
[170:30] we get something like that where the core of the model is being all in place but then everything
[170:36] everything else is being simulated which is more interesting
[170:42] another thing to note from that scene if we go back to the previous look that we had when
[170:47] everything was frozen here if you pay attention to this number material condition is set to 0.8
[170:53] instead of the default of 0.9 if I set that back to 0.9 and I run the simulation
[170:59] you can see here on the other side that we have some funky stuff happening here so the points are
[171:08] kind of collapsing onto each other and this happens this is usually a sign that you require more
[171:13] sub steps so this is instability going on in the material so in this case it has nothing to do with
[171:20] our fath particle or moving because everything is static so if you want to fix this you can just
[171:27] decrease the material condition to make it more aggressive remember that this parameter is going
[171:31] to look at the material description and based on the stiffness and the whole description basically
[171:37] it's going to infer the number of subset that it needs to make the simulation stable
[171:42] the life I just decreased that tiny bit to 0.8 you're going to increase the subset count
[171:49] and now we have something stable and in fact we're still running at 15 subsets but I'm guessing
[171:56] that at the beginning of the simulation with the previous settings we're probably more around 13 or
[172:01] something like that sometimes it can be just like a very small difference between 13 it's unstable
[172:07] and then at 15 subset it's stable sometimes it's a very fine line when in this case we fix this problem
[172:17] let's look at another example with pin cuffs right so if I dive here
[172:21] and the npm source by default we have things set like that
[172:34] we have our crack model everything is pinned and this is not going to be very interesting if I play
[172:40] this but what we can do is enable animation and what what this does is it provides the
[172:48] points to the npm solver so the npm solver can look at change of attributes like if the position
[172:55] is changing the npm solver is going to pick it up and also if you unpin some points the npm solver
[173:00] is also going to unpin the points and simulate them as three particles so to see the difference
[173:07] like if I just select the npm source and I change frame you see we're always uh
[173:12] pitching we're passing all those points to the solver because normally if you don't have this
[173:16] option enabled you just see this guide representation where it's telling you that okay you're looking
[173:21] at the npm source and you should be sourcing those points but this is not the frame where
[173:27] you're sourcing the frame where you're sourcing particles is in fact the first frame because
[173:31] you're you're set in the in this uh once mode so this is the frame where the particle are passed
[173:38] there's 21 000 points and then on the next frame you just see guide because no points are being passed
[173:44] but if I set that back to enable animation now the points are constantly passed but they are only
[173:51] emitted on the first frame and after that they are only passed as a reference to look at the position
[173:55] of the points and the uh pin to animation attribute so what we're going to do here with this node
[174:02] we're going to start uh we have a little animation and we start from the top of the model and we're
[174:06] going to progressively unpin the particles as we're going down so if we look at the result
[174:13] we get this so the particles are being unpinned and then the model is collapsing on itself
[174:19] which is interesting and uh you can also use the input animation so if I check that it's going to
[174:25] use this animation to transform the points so you now have the points moving in space
[174:32] we're also going to unpin them from top to bottom if we simulate that
[174:43] we get this result uh this is pretty slow and just so you know this is not necessarily because
[174:49] the npm solver is doing a lot of calculation it's mainly because at the moment the retargeting of
[174:54] animation is being done per named piece so each rigid piece is being retargeted in isolation inside
[175:02] of a for loop so at the moment the npm source is doing like most of the work that's why it's so slow
[175:15] so yeah this is the kind of setup that can be used to achieve very interesting effects of like
[175:21] dissolving or disintegrating characters
[175:26] then let's move on to this simple retargeting though and yeah before I talk about the retargeting part
[175:33] I just want to mention a little bit the elastic constip model another thing that I haven't mentioned
[175:39] just yet so this is very similar to the chunky constip model it's just using a subset of the
[175:46] parameter so you only have the stiffness and this volume preservation attribute
[175:52] so uh stiffness is being the same as where you have stiffness in other constip models so it's
[175:59] like the resistance to deformation and then volume preservation is what I explained earlier where if
[176:05] you have some deformation like some stretching going on along an axis you're going to get a reaction
[176:11] along the perpendicular axis that is going to be kind of the opposite so if you pull the material
[176:17] the perpendicular plane is going to compress itself and if you push on the material the perpendicular
[176:23] plane is going to expand just to preserve the volume and you can also see this parameter as
[176:27] how explosive the simulation is so if you want things to just collapse on themselves and absorb
[176:33] the energy of the deformation you can set that to a lower value like 0.1 or 0.2 but if you want
[176:39] things to really react and explode based on the compression and impacts then you're you will boost
[176:45] this value to a higher setting like this okay so in this case we are just setting a name attribute
[176:55] on both of those models and here we make sure that we transfer attributes so we want if we look at
[177:01] the points here we want to make sure that our name is being transferred over so here we have flip
[177:07] and we have pig so when we're done with our simulations we could just look at the sim
[177:14] we get something like this when we're done with the sim we can just go to a for loop and just
[177:20] retarget each model in isolation using this for loop based on the name we're going to use like this
[177:30] point cloud from the npm simulation and we just do a simple point d form
[177:35] so here we get this
[177:38] so obviously if you have pieces breaking this is not going to work so well but this is just
[177:43] like a very simple setup because we haven't really touched on a like squishy object like this using
[177:49] the rubber or the general material preset but yeah this is the kind of setup that you can achieve with
[177:54] this
[177:58] so since the very beginning of this masterclass I have always been using this npm container
[178:03] in this first mode this access line bounding box and this works fine but if you want even more
[178:08] control you have this convex geometry mode and this is very useful if you have like custom geometry
[178:14] like a camera frustrum and you want to let's say prune out all the particles going outside of the
[178:19] view so you just object merge this frustrum geometry then on the npm container you pick the
[178:26] correct type so convex geometry and then you set all the boundaries to be let's say in delete mode
[178:31] in this case if I look at the result you get something like that where the points are just
[178:37] being killed when you reach this boundary another thing that you can do there's this
[178:44] attribute this is a string attribute that you can set on each polygons where you can define
[178:51] the boundary to be either open closed or to be delete so to be like deleting particles but
[178:57] you have to write delete as the the value and what this is going to do if we look at this
[179:04] node in this case we're just setting everything to open but we're picking the third polygon which is
[179:11] this one here and we're setting it to closed we want to visualize the result we go here and we
[179:17] uncheck this override for all the boundaries and we get this so just a single plane that is going
[179:24] outward to infinity set to close and all the other planes are just being open
[179:32] if we look at the new result that we get
[179:37] now with this we get the particles being bounced by this plane
[179:43] instead of being deleted like we had before just keep in mind if you use this technique
[179:50] just keep in mind that each polygon is going to be an infinite plane and they are treated like
[179:54] separately so if you have 1000 polygons as your convex geometry it's definitely going to slow down
[179:59] this in quite a bit but yeah just try to keep something reasonable in terms of the amount of
[180:05] polygons that you're sourcing in this mode because you're not limited to six polygons you could have
[180:10] like 20 polygons it would work fine but yeah just try to stay conservative with this
[180:16] then let's talk about material blending stickiness what does that all mean in MPM as I said multiple
[180:24] time you have your particles that are transferring at view the background grid so there's only one
[180:31] background grid so if you have two materials like this we have a bit of soil and you have a bit of
[180:35] water what happened when those two are touching together like this so what what is being transferred
[180:42] to the background grid at this point when when the two materials are touching each other well you
[180:48] basically have like a blending you have an interpolation between the two materials so this point of
[180:53] material like this point in space is going to be a like a mixture of soil and water what this does
[181:00] is if if we run the like if we run the simulation
[181:04] so what this does is you have a lot of water particles that are just sticking to the soil
[181:13] and in some cases maybe you want the water to just flow on top of the soil and reach the ground
[181:18] very quickly you don't want a lot of water to be stuck in those areas in space but because this is
[181:25] a mixture between soil and water the water particle in those area are receiving some of the soil
[181:31] material description so they are kind of sticking to this pile of soil and they are no longer allowed
[181:36] to just slip and go down two things you can do about this you can scale down the grid so the
[181:44] background grid you can make the voxel smaller and this is controlled here so let's say I'm going to
[181:48] make the grid scale one and you should get better separation between the two material and less blending
[181:55] because now the voxels are kind of the same size as the particles but it's still not going to completely
[182:00] solve the problem if we look at this yeah we get a tiny bit more the holes here where we're
[182:08] seeing like the water particle going all the way down and we can also see that the water
[182:13] is now able to carry some of the soil particle with them which looks probably more realistic
[182:20] but it's not completely solving the problem you still have a lot of water on top of the soil
[182:27] the other way to work with that is maybe to do like a first simulation
[182:31] where you simulate both things together and then you could do a secondary sim where the soil is
[182:36] converted to a sine distance field so basically like an mpm collider in a deforming mode and then
[182:42] you just sim the water on top of it so you have more control to set maybe the soil to a very low
[182:47] friction and then you're going to get the water to run off easily off of the soil so you can like
[182:54] compose the simulation in this way and have more control but if you simulate everything all at once
[182:58] just keep in mind everything is being rasterized to the same background grid and you get this kind of
[183:03] blending a question that is most likely going to come up very often is how can you speed up your
[183:15] mpm simulation it really depends on the material that you're simulating but for sure if you are
[183:20] simulating concrete like in this case it's going to be pretty slow because of the stiffness of the
[183:25] material if we run that you can see that it's not running very fast and if we stop the simulation
[183:34] and look at the details that you viewed you can see that we're running at almost 800 subs steps
[183:40] so what you can do is you can try to reduce the amount of subsets like four steps to not go above
[183:46] 350 for example and now if we zoom we see that it's still stable so that's a that's a win for us
[183:53] because we're now running twice as fast and we're not getting any instability so that's great but in
[183:59] some cases if you push this limit down too much let's say to try 150 now we get some instability
[184:08] you can see like on the first frame the the sphere of concrete is kind of bulging out which means
[184:14] it's not able to resolve the material properly within 150 subs steps so just keep in mind that if
[184:22] you're decreasing the value too much you might run into some problems
[184:36] sometimes you might run into some wiggling material so here I have just like a stack of snow
[184:43] it's using like the default preset for the for the snow if I run this you can see that we get
[184:50] some bounciness in the snow and the reason for that is well there's two ways to fix that so at
[184:57] the moment you have as we said before a fraction of the deformation that is plastic so it's just
[185:02] going to change the rest state of the material but you also have another proportion that is going
[185:07] to be elastics where the solver is going to force against this deformation try to recover from this
[185:14] deformation and this is why you get this oscillation there so what you can do is maybe reduce those
[185:22] boundaries so with those limits of critical compression and critical stretch if you reduce
[185:26] that it's going to make more of the deformation to become plastic and less of it to be considered as
[185:31] elastic so the the material is going to collapse on itself a little bit more but it's not going to
[185:38] wiggle that much and also in this case we're increasing the stiffness to help a little bit
[185:44] and now we get something like this where snow is kind of collapsing on itself but it's no longer
[185:49] like bouncing back at infinity like we used to have so this is good and also keep in mind that
[185:56] another way to tackle this issue is to noise the stiffness attribute so let's say you have this block
[186:02] of uniform snow and you just noise the capital E attribute so the stiffness across the old material
[186:08] you just add some variation across this block of material this is going to make it less kind of
[186:16] perfect less symmetric and a lot of time this variation is going to remove this bounciness
[186:22] that you get in the material so that's another way to deal with this problem
[186:25] so sometimes you can run into situations where the particles are kind of collapsing
[186:36] onto an invisible wall so just to make this more concrete like if I simulate one frame of this
[186:41] you can see that we're getting this result which is pretty alarming if I show the velocity vectors
[186:49] you can see that we're coming from this area and then we're shooting that direction super super fast
[186:54] we have initial velocity here set to 50 in all the axis so what's happening here is that we are
[187:02] going outside of the background grid so on the first frame we have I can just
[187:07] can visualize the background grid here so I'm going to enable this and we're starting from this
[187:13] area we have all of this grid that is perfectly active and ready to be used but then we're moving
[187:20] toward this corner and at some point we're going to try to escape this grid but we don't have any
[187:28] we no longer have any voxels to get the transfer from particle to grid and then grid back to particles
[187:34] so the particles are just like stuck in space here so what you need to do is go in the advanced
[187:39] tab of the MTM solver and play with this min max voxel dilation so for example if I increase this
[187:46] to 60 voxel now we're able to fix the problem and completely cover the area that is going to be
[187:53] traveled by this piece of material so the reason why we have this clamping here is just well this
[188:00] side it has an optimization so if you have like one crazy particle going super fast it's not going to
[188:06] blow up your simulation because you run out of memory it's only going to make this single particle
[188:13] the end of the background grid but for the rest of your material that is not going crazy
[188:17] this is going to be fine so this is an optimization this lower bound is just making sure that we have
[188:22] enough padding around our geometry and right now if you look at this you might feel that this is a
[188:28] huge waste of performance because we have like this very very large bound of a background grid
[188:35] even if our material is going in that direction but the reason why we need to do this is because
[188:40] you never know in what direction things are going to go like if you have a collider hitting this
[188:44] piece of material it can shatter in all directions so you need a lot of padding around the material
[188:52] points in all directions to make sure that you cover where the material might go and the two things
[188:57] that are going to dynamically influence this background grid dilation are the speed of the
[189:02] material and the speed of the colliders so those two things are being read by the solver and the
[189:08] solver is always dynamically trying to predict where the particle might go and it's trying to keep
[189:15] this voxel dilation as small as possible but also padded enough to cover the simulation
[189:23] one thing you have to keep in mind as well is that this is in voxel size and not in the world
[189:29] scale so if you go to a very large scene or to a very small scene this should adapt properly so
[189:35] that's the good news the bad news is since this is not a world scale if you have you're
[189:41] simulating in the af-res because you're just iterating and trying to get a specific look
[189:46] and you're happy with the kind of padding that you have with this voxel dilation and you're set to
[189:51] 60 for example just know that as you're doubling the resolution if you go to your iris and you kick
[189:57] it on the farm just know that by reducing the size of the voxels by half you're also getting half the
[190:03] padding so in this case if you want the exact same padding around your simulation you will need to
[190:09] increase this to 120 so usually this is in the advanced tab so usually you don't really need
[190:16] to look at this constantly and adjust that it should work out of the box most of the time but
[190:21] when it doesn't work you can visualize the background grid and try to play with those numbers
[190:26] so another thing that might run into is instability when you're modifying the material description
[190:36] as the simulation is running so for example here we have this sphere of mud so we're just using like
[190:40] the mud preset here and but we're gonna affect the stiffness of the material so as the simulation is
[190:48] going forward in time we're going to make the material more and more stiff so by default if we
[190:53] just run this we get this kind of result where okay everything is going crazy and flying in all
[190:59] direction the reason why it's doing this is because the material condition is only looking at the
[191:06] material description on the very first frame and it's defining like what would be the proper
[191:11] sub step count to go for based on what's happening on that first frame and after that it's not
[191:17] recomputing it every frame just to save on computation and make the same go faster but in
[191:22] this case if we died in the mpm solver we are changing the stiffness on every frame so this
[191:28] material condition needs to be reevaluated to do that you just go on the mpm solver in the advanced
[191:35] tab and you uncheck assume on changing material properties in this case it's going to make sure
[191:42] that it's reevaluated and it's going to dynamically adjust this sub step count now if we play this
[191:48] we get something that is very stable but we also see that our sub steps are ramping up quite fast
[191:55] so here we start with sub steps of like around 20 and we go all the way past 130 sub steps
[192:05] but at least we get something that that is very stable and that works even with the
[192:09] changing material properties so yeah this is another getcha that you have to keep in mind
[192:19] so here i just want to talk about this send the constitutive model or gave you because again during
[192:26] the previous example i've never had the chance to discuss this one if we look at the mpm source
[192:31] we use let's say the send preset get this material and this is similar to what you see with other
[192:38] constitutive models we have density stiffness volume preservation for send i would say that
[192:43] you should keep all of those parameters to exactly those values you don't really need to change this
[192:48] you should be interested in changing those two guys and so friction friction angle has to do with
[192:55] the friction between the grain of sand so if you want to make a very tall stack of sand you should
[193:00] increase its value so by default you get something like this so it's just like a stacking like dry
[193:08] sand if you want this to stack higher you can crank that up to let's say multiply by two
[193:15] we have more friction between the grain of sand and now we have higher stacks on the other end
[193:22] you can divide that by two and now it's going to create like just a very flat uh puddle of sand
[193:31] and another interesting parameter is this cohesion thing it has to do with how the sand
[193:39] will stick together so if you do wet sand this is definitely something you're gonna look at
[193:44] so if i just add some to this material and isolate it you can see that now it's more cohesive
[193:52] it looks more like wet sand if you set it very high it's almost going to look like a solid
[193:58] like this so so you have a lot of flexibility in how the material behaves just by changing this
[194:05] cohesion parameter and if you do like a beach scene where water is touching the dry sand and you want
[194:10] the sand to behave more like wet sand this is definitely something you want to affect inside
[194:14] of the dive target and you should be able to get the look that you're after so this is what concludes
[194:20] this masterclass i hope you learned a lot of things i really can't wait to see the amazing
[194:25] simulation that you're going to do with this new solver just post your question on the forums
[194:30] and we're going to do our best to improve the tool set and just support you in whatever project you
[194:35] might have thank you for your time



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
