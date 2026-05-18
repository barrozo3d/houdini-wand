---
title: Intro To Houdini Volumes - Beginner Course
source: YouTube
url: https://www.youtube.com/watch?v=wR0SDptfygg
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/intro-to-houdini-volumes---beginner-course/
frame_count: 0
---

# Intro To Houdini Volumes - Beginner Course

**Source:** [YouTube](https://www.youtube.com/watch?v=wR0SDptfygg)
**Author:** Voxyde VFX
**Duration:** 137m16s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


### Volumes & Voxels [0:00]
**Transcript:** Volumes are a gigantic part of Houdini and VFX in general.  I would go as far as to say that around 90% of VFX shots require some use of volumes.  And you might think that we as VFX artists only use volumes when creating explosions or smoke type of effects,  but in reality volumes are used all of the time in many types of effects.  This is why it's crucial to have a good understanding on what volumes are and how to use them.  In Houdini there are many ways to create and manipulate volumes and we'll cover them more  as we progress, but let's start with a simple volume. So I'll drop down a geometry container,  let's step inside and I will drop down a volume node. Now we have a bunch of settings here and  I'll go over this in a second, but in order for us to see the volume we need to give it some  initial value. So in our first component here we can set this value here to 1 and now Houdini will  know how to drop this volume in the viewport. And this is the default behavior as I increase this  value here, we can take an up this volume and as I decrease this we can fade it out. So if this  reaches a value of 0 now we won't be able to see this. This doesn't mean that volume doesn't exist...


### VDB vs Standard Volume [8:52]
**Transcript:** in Houdini there are two types of volumes standard volumes and VDBs and it's been decided a long time  ago now that VDBs are the superior version and I'll quickly explain why if we have a geometry that  we want to turn into a volume to later use in a smoke simulation we can do this with an ISO offset  node so here it is and I set the method here by size and set the division size of 0.025  now if I look at the information here we are already working with roughly 500 000 voxels  and even though we see the density only where the geometry is we in fact have voxels inside this  entire bounding box of the geometry so if I do a bound from here this entire box is filled with  voxels that store information it's just that the voxels inside the geometry are one and all of the  voxels outside are zero and this is how Houdini knows how to draw this in the viewport so again I  have a geometric representation of this 3d grid of voxels and I will slice this in half to do a  cross section and we can also preview our geometry as well so this is basically the cross section of  the geometry too so everything inside this bounding box is filled and this is why we have this  large number of voxels so thi...


### SDF Distance Volume [12:31]
**Transcript:** with VDB comes another type of volume that's super important which is called the sign distance field  sdf for short now when I first started using kudini and heard this name sign the distance field it's  sounded super sci-fi like something out of blade runner but in reality it's pretty simple to create  an sdf we can use the same VDB from polygons and here we can say that instead of this fog VDB  we can turn this off and we can turn on the distance VDB instead so distance VDB will give us this sdf  volume which looks something like this in the viewport and the way the sdf works is we have the same  voxels that we had earlier with our density so we are using the same size here but the difference is  that in each voxel now we are simply storing the distance from the surface of the geometry so if I go  back to the cross section geometry representation here and let's also grab our toy as well and let's  let's maybe just do a slice of this so we don't have this entire half of the geometry on the side  and we're left with a thin slice so I'll just do another clip here and reverse this and just  increase the offset like so and I'll repeat this for the geometry as well you don't have to wo...


### Volume VOP [16:54]
**Transcript:** fog vdb or a distance vdb and now we can start having some fun and introduce the volume VOP  so let's go ahead and add this I'll type vv and I will go down here to this volume VOP let's  drop this down and we will connect this with our vdb from polygons and this volume VOP works on both  fog vdb and distance vdb but for now let's focus on the fog vdb so over here I'll turn off the  distance vdb and turn on the fog vdb so we will work on a fog volume first now for this next part  it's important that you have previously watched the intro to VOP series or that you know your way  around VOPs in the context of regular geometry a lot of things we do with VOPs or VEX for regular  geometry can sort of be applied to volumes as well and this is another big reason why Houdini is  super powerful with volumes and I just want to add the regular attribute VOP for now to  compare the two right away we can see a slight difference when we select either of these the  attribute VOP has the option to run over primitive points vertices so all of the different components  of a geometry whereas the volume VOP doesn't have this option at all so it's more unique than a  regular attribute VOP and if we step ...


### Fog Volume VOP examples [25:31]
**Transcript:** of VOPs and this technique is something that I did in a lot of projects over the years let's just  start with a fresh volume VOP so I'll delete this one and I'll drop a new one so volume VOP and  let's dive inside let's say that I want to fade the density along the height of our object so I  want more density at the base and no density right at the top we'll drop down a relative to  bounding box node and we'll connect the position to this node and this node is covered in the  intro to VOP series but just as a refresher this node will give me a 0 to 1 value along each of  the x, y and z dimensions of our bounding box and they're all stored as a vector inside this node  so if I want to grab the 0 to 1 value of our height so the y axis I can do a vector to float from  here and this will split up the x, y and z component so if I want to grab the y component this will  be the middle value over here so if I want I can plug this directly inside the density so let's  plug this over here and we can already see the sort of effect that we want we have a gradient only  that this is starting with high density at the top and no density at the bottom but we can kind of  see this gradient here let...


### Multiple Volumes [37:39]
**Transcript:** density but we can actually store multiple values in the same object so in fire simulations you will  usually need a volume that drives the flame and a separate volume that drives the smoke that  the flame creates so having multiple volumes is important for the simulation process but also  for rendering we usually need different settings to control the flame and the smoke separately we'll  start fresh with a rubber toy and we'll do a VDB from polygons and let's turn this into a fog VDB  and I'll decrease the resolution here or rather increase the resolution by reducing the scale  so I'll use 0.01 now if I do a volume valve from here so far we've been affecting our density  so in between here if I do for example a multiply constant I can increase or decrease the amount of  density we have and everything works now this output here is set by default to export to a volume  that's called density so in our VDB from polygons if I go up and I go back here if I change the name  here to let's say temperature now we can see that this volume valve no longer works so if I go  back inside and modify our values here nothing changes in order to affect this volume that's now  called temperature we ...


### Volume Visualization [43:56]
**Transcript:** now we are drawing both fields as smoke in our viewport but let's say I want to use the  temperature to control the emission of the volume to do this we can use a volume visualization node  so let's append this here in this node we will have two tabs one for smoke and one for emission  and we can specify which fields we want to drive each of these so for smoke we are looking for our  density field by default here so I can use this ramp here to remap our values and we can kind of  see something happening in our viewport let's maybe break up the smoke so we introduce some noise  in order for this to be more obvious so after the VDB from polygons I want to do a volume  noise fog from here and this node is really just sort of like a preset of what we build earlier  ourselves with VOPs so over here I'll set the operation to multiply let's do zero centered  range values and I'll also enable ramp remap ramp here and I'll just bring this point up slightly  so we can see we have the same result that we had earlier so again all of this we can do our  selves in a VOP node and if I press tab and type here volume we can see we have a lot of operations  that do different things and a lot of thes...


### VOPS with SDF [55:18]
**Transcript:** so as the F's let's drop down another VDB from polygons here and we'll use the default distance VDB  here so this will create an SDF that's called surface and let's maybe just decrease the  voxel size here so increase the resolution 0.01 and let's do from here a volume VOP and let's step  inside so again we right away run into the same problem with the naming which is that this volume  VOP is tied to density and we want to bring in our surface field so let's do a bind I will type here  for name surface and if I hold down alt and duplicate this node as it is I can turn on this option  to use this node to set parameter attributes and export here I will type to always and this  essentially now turns it into a bind export node so if I do a bind export we can see that this is  the same node as a bind with just different settings to it so this is how we can recreate the  bind export node so now if I plug the surface input into our output surface in between here we can  modify our volume and if we do a multiply constant and I increase and decrease this value we can see  that nothing happens whereas on a fog volume this will fade out our density or thicken the density  but nothing happens ...


### Working with SDF [62:25]
**Transcript:** so I'll get rid of these three nodes and let's go back to our volume VOP and I'll reduce this  add node in fact let's go inside and let's remove this promoted parameter over here and instead of  adding a constant value to the sdf we can generate noise values and add those instead so from our  position we actually don't need this volume VOP node we can get rid of this I'll get rid of this  global output here and let's just grab our position so the p and we'll do a turbulent noise  and we can plug the values of this noise directly inside our add and we can kind of see something  happening now to further control this we can do a feed range after our turbulent noise to further  control our values and I can decrease the destination max now and we can see that as I increase this  we start to eat away more of our sdf and we also have this nice noise pattern we can also go  to the turbulent noise and I'll set the type here to simplex and I know that the simplex outputs  values between negative 0.5 and positive 0.5 so in our feed range I will set the source main to  negative 0.5 and our source max let's do 0.5 and now we can use the destination mean and max values  here to sort of push in o...


### SDF VOP Examples [67:21]
**Transcript:** so there's really a lot of applications with sdf and they're commonly used to create all types of  shapes and geometry and for example I'll start with a simple sphere so let's drop this down  I'll set this to polygon and increase the frequency and also I might increase the uniform radius  or rather uniform scale here to a value of 2 and let's turn this into an sdf so we'll do VDB  from polygons we'll keep this as surface I might want to increase the resolution so let's do 0.05  and let's append a volume pop here let's step inside and we'll do a bind on our surface so again  the same process that we did earlier I'll set the name here to surface I'll duplicate this node  by holding alt and on this node I'll turn on this use this node to set parameter and export to  always and plug this here so earlier we used a noise pattern to displace this sdf but who did it  really comes with a lot of different patterns that we can use so let's get rid of this density here  and from my position let's do a cellular noise so this comes with all kinds of different parameters  and even outputs let's just see if we add one of these outputs to our surface and if I grab the  border here and add this we c...


### Velocity Field [78:44]
**Transcript:** these two types of volumes distance VDB and fog VDB and these can store float values so here  again this is the cross section of our rubber toy with some voxels running it and this here  this blue line is the surface so with sdf we are storing the distance value to the surface and when  we create smoke or density these will all store simple float values that specify the amount of  density any voxels can have and in both cases the values that we store are float values so these  only have one dimension and the volumes that we create based on float values are called scalar  fields so the density and sdf volumes are both scalar fields now if we want to create some sort of  movement we will have to store a vector value that has both magnitude and direction and now this  new type of volume will become a vector field so in a smoke simulation for example we can move  this smoke around by this vector field so any given voxels will have this vector information  and the direction will specify in which direction our smoke should move and the magnitude will  specify how far along we should push the smoke so this is essentially the strength of a vector  and typically with vector fields we use th...


### Velocity Field VOP Examples [90:00]
**Transcript:** get rid of this and to change the velocity field we'll have to do a bind export and we'll set this  name here to our field which is VEL we also have to specify that this is a tree float vector type  or otherwise we won't get the correct result so we already have an initial value that points along  our x direction but we can override this so if I just drop down a constant node I can set this  to a tree float also let's plug this here and I can use these values now to control our field  so I can give this some direction in the x dimension and we can play around with these settings and  hopefully we can kind of see the way our trails change it's not super noticeable what we're doing  so far so let's modify this further now this should not be a surprise to you at this point but one  of the main ways we can modify velocity is to add noise so from our position we'll generate a  turbulent noise and the signature here has to be a 3d noise because again we are working with  vector so let's add our noise values to our constant and now we can start to see something a little  bit more interesting if we go to the turbulent noise I can increase the amplitude and we can see  how this changes our ...


### Custom Velocity Field [98:21]
**Transcript:** create a velocity field based on a curve so I'll drop down a curve sub from here I'll set the  primitive type to nerves curve let's go to our curve and I'll press I'll hold down spacebar  and press tool to go in the top view and let's just draw this curve maybe across a span of four  units so from negative two to a value of two I'll press enter in the viewport and let's just draw a  simple curve as to maybe something like this I'll press spacebar one to go in the perspective I'll  press F to go into editing and I might just want to also make this more of a 3d curve so just try to  have a more interesting path here this doesn't really matter this much for this example so let's  just do something like this I think this will be fine now because this is a nerves curve it doesn't  have any usable geometry so we usually pair this with a resemble node so let's drop down a resemble  and now if I turn on the point display we have regular geometry that we can use and we can store  attributes now on these points now earlier I said that usually to create a velocity volume we start  with a simple vdb node and create an empty volume first and then use vdb activate to set the size  and all of tha...


### SDF From Particles [118:28]
**Transcript:** volumes based on the geometry but we can also turn geometry that only has points into volumes so if  I create a simple point here I'll drop down an add click this plus a button here and this will  create a point in the center if we want to turn this into a volume we can use a VDB from particles  so let's drop this here and append this and this will create a sphere volume based on our points  and here we have a few settings so first of all we have the usual voxel size that determines the  amount of voxels that we have then we can either create an SDF or distance VDB and we can also  just create a fog VDB like so there's also this mask VDB option but this honestly doesn't come  up that often don't worry about this for now we have our two main classes so the fog VDB and SDF  or distance VDB let's just keep this as an SDF for now and check some of the other settings point  radius scale determines how big will draw our volume in our scene so we can control the size of  this volume now if we have more points this will be applied to all of the points and minimum radius  in voxels determines how many voxels a point needs to cover in order for it to be drawn so if we go  back to our cross s...


### Volume Rasterize Attributes [127:23]
**Transcript:** into an sdf or we can turn them into a fog volume like so but there is a better way to use the  fog volume version and this is by using a volume rasterize attribute node so let's drop this down  over here and we kind of have some of the settings that we are used to we have the Vox  size and the particle scale so this particle scale here will also act as a multiplier kind of like  it does over here in the VDB from particle nodes let's go ahead and just duplicate the attribute  create node which has our p-scale value and the way the volume rasterize works is that it's going  to look for an attribute and base the density or whatever kind of volume we want to create on that  attribute so this is why we don't have anything currently showing because we have to specify which  attribute we want to rasterize so over here we have all of these attributes that we get from our  popnet simulation but let's go ahead and just create a simple density attribute that has a value  of 1 over all of the points so in our attribute create i will hit this plus to add another attribute  i will set the name here to density and i will just give this a value of 1 and now in our volume  rasterize attributes we ...



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
