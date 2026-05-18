---
title: Intro To Houdini Pyro - Full Beginner Course
source: YouTube
url: https://www.youtube.com/watch?v=m8w2OND3rH0
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/intro-to-houdini-pyro---full-beginner-course/
frame_count: 15
---

# Intro To Houdini Pyro - Full Beginner Course

**Source:** [YouTube](https://www.youtube.com/watch?v=m8w2OND3rH0)
**Author:** Voxyde VFX
**Duration:** 145m31s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey there, this is Rez and I've been a Houdini Pro for the last 4 years and let me tell you,  Pyro is the king of fire and smoke simulations.  Yes, there are other software out there like Amber Jen or other plugins for Cinema 4D and Edons  for Blender and while those are cute and you can impress your mom by using them, there's nothing  like the real deal, there's no substitute for Houdini. The amount of control and complexity you  can get in Houdini is unmatched. In this course I'll show you how to use Pyro to achieve amazing  results with simple setups. By the end you'll have the skills to build any kind of fire effect you  can imagine, so let's get started. Let's create a Geo container and we'll step inside and let's

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_000.jpg

### Basic Setup [0:42]
**Transcript:** drop down the Pyro solver. So if we look at the properties here, we can see that we really have a  lot of tabs with a lot of different settings, so there's really a lot of options for us, which is a  good thing because we can get very specific with our simulations but this can be quite overwhelming  at start. So first let's only focus on the sourcing tab over here. This tab is the most important  tab because without sources we can have anything. Pyro solver by default doesn't know how to make  fire or smoke out of nothing, so we have to base it on some existing volume. So let's create a  simple sphere. I'll drop down a sphere. Let's set this to be a polygon and we'll just increase  the frequency here and let's also increase the uniform scale, so we'll make this bigger. Let's try  a value of 3. Now right off the bat scale is very important with pyro simulations and simulations  in general and we'll get more into this later but for now let's just keep the uniform scale  at 3 and this will be fine. So let's turn this into a fog volume, so from our sphere we can drop  VDB from polygons and we'll turn on our fog VDB option here and uncheck the distance VDB and now we  have some smoke. N...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_001.jpg

### Sources [9:49]
**Transcript:** just get rid of this guest turbulence and if I go up I'm going to keep all of these micro solvers  off so we can focus only on the sourcing tab here now by default when we place down a pyrosolver  node it adds a lot of sources here but we only really have density so for now I will just get rid  of any other source and just focus on our density so let's examine what happens here we have a  source volume and a target field now our source volume is grabbing the name that we specify in  our sources here so in our vdb from polygons we set our vdb name to density so this is what our  source volume will look for this is the name that it will look for and now the target field is the  built in name that the pyrosolver recognizes internally to drive our smoke so right now it's a  little bit confusing because we have the same density name for both our source volume and our  target field but for example if I were to go back in the vdb from polygons and I would change this  name here to source all right and we can check that our name here is source we can go back to our  pyrosolver we can see that nothing happens now because we no longer have this here so we have to  update our source volume na...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_002.jpg

### Velocity Field [13:59]
**Transcript:** annoying blue background I'll press D and we can go to the background here I'll change this to  dark so we can preview our volumes better and also here in the guide step I have the draw time  FPS on so we can see the frames per second we are getting when we play our simulation so we can  check sort of like the efficiency of our setups and in this geometry information tab this is always  on so we can also see the amount of voxels we have and this also displays the geometry point number  and primitive number all right so let's close this and I'll also close the parameters over here  I'll close all these tabs so we can only have our network view and I'll just press P so we can  bring back our parameters and this is really my preferred way of working just so we have more  real estate on our screen so again all we have for now is a sphere that's turned into a fog volume  which we are sourcing in as our density field and in the shape tab I turn everything off and in  the sourcing tab we only have this source volume density which is being sourced in the target field  density so let's create a velocity field and the reason I want to bring up the velocity right  away is because by just sour...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_003.jpg

### More Velocity Fields [25:51]
**Transcript:** so I'll go ahead and get rid of this copy and let's get rid of the merge and focus on our main  setup and also in the shape tab I will disable the turbulence and let's make sure that we have  no microsoft words affecting our simulation so we can focus on our sourcing and for our velocity  field let's go back let's preview our volume trail and let's go back in our volume vault and if  I want to add a simple wind to this velocity field we can simply drop down a constant so let's  drop this here I will make this a tree floats let's make this wind point straight up so let's do  0 1 and 0 and we can simply add this to our bind export for our v here so let's go ahead and  add this and we can kind of see the result here let's maybe also do a multiply constant after so  we can also scale down this vector maybe back a bit so I will just reduce the multiplier here  so we can see that as I reduce the strength of our wind we get back more of our noise motion  that we had originally so now from here let's go back and let's see what we get and if I play  the simulation and we can see now that we introduced a simple wind so maybe this is a little bit too  strong I can go back here and I can reduc...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_004.jpg

### Sourcing Operations [35:35]
**Transcript:** are going to continuously add on top of what we have already which is fine for density and this  is mostly because as the simulation progresses the density that we add is getting pushed away  from our source so in this case it's fine that we keep adding density otherwise we wouldn't get  a continuous emission but when it comes to velocity this add operation accumulates speed over time  since each frame we are adding vectors on top of each other so let's head over to photoshop real quick  and let's say that this grid is a cross section of our velocity field and let's say that in our  velocity field we have vectors that look something like this so let's maybe just draw something like  a curve so maybe it goes something like this and let's say that our smoke is maybe over here so  it reached this destination so let's say that when our smoke is on this voxel it's going to pick up  this vector from our velocity field and it's going to move in this direction like so and then when  our smoke reaches this other vector this new vector from this voxel it's going to grab this  direction but it's going to carry over the length from this vector so the new vector that will  get applied is going ...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_005.jpg

### Temperature [46:27]
**Transcript:** let's go ahead and get rid of our velocity source for now and we'll also disconnect our  source sync over here and I'll just drag these over to the side I'll get rid of this merge  so we just have our density source let's also go in the shape tab and let's disable turbulence  so we don't have any microsofters affecting our sim back to our sourcing let's go ahead and work  on our temperature sourcing for now so we can base this on the same source as our density so in fact  I'm gonna go ahead drag this over to the side and while holding out I'll duplicate this setup and  I'll rename this now here let's type temperature source for our vdb from polygons let's also  set this name here to temperature and we'll also have to update our noise fog over here to look  for this temperature volume so let's type here temperature as well and inside this volume noise  fog I will also want to change the offset so we get a different noise pattern from our density  and let's check we have a temperature volume now and this is a simple float field so this will be  a scalar field let's go ahead and merge this back with our density and now in our pyrosolver I can  add a new source this will be source name...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_006.jpg

### Divergence [57:54]
**Transcript:** be divergence and for divergence we'll do the same thing that we did with our temperature we're  just gonna go ahead and grab all of these nodes and duplicate these over let's rename this to  divergence source and for our volume in the VDB from polygons we'll use name divergence and we'll  also use the same name here for our volume noise fog so I'm going to paste this here and also for  our volume noise fog let's again offset our noise pattern so it's different from the other ones  and we can now simply merge this in our chain let's go to our pyrosolver we'll just keep buoyancy  on for our shape tab and in sourcing let's add a new source and we want to source in the divergence  volume source into the target field divergence so if we press play not much changes but if we  increase the source scale here we can use a value of 10 and play this now we can see this expansion  in our smoke and typically for explosions especially we'll use rather high values so we can  set this to 100 and now we can really see a big expansion and this actually resembles more of a  explosion kind of effect now again we are continuously pumping in divergence so we have this  continuous expansion if we wanted...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_007.jpg

### Flame [67:04]
**Transcript:** want to look into will be the flame field now there are a couple more fields like alpha and cd  and usually we deal with those when we need to add vector color information from a volume source  but honestly that doesn't come up that often we usually control the color through the shading tab  so if I go over here and I go to the look tab like we showed earlier I can just change the  smoke color from over here so I can make this green or whatever so we usually control the color  after we simulate through the shading but in very specific cases we might need to add  vector color so this is where these fields are necessary and this also goes a little bit beyond the  scope of this course so for now I just want you to know that these fields exist and maybe in a more  advanced pyro course we can focus on this anyway back to flame the reason that I save this for last  is because in order to explain what the flame field does we need to know what temperature and  divergence does so now that we understand this too we can talk about flame so let's go back to  Houdini and we'll just replicate the setup that we had so far let's maybe I'll just hold on shift  and drag this whole chain to the side ...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_008.jpg

### Wind & Disturbance [79:26]
**Transcript:** the sourcing tab works let's take a deeper look in our shape tab and explore some of these other  microsolvers let's go ahead and just clean up the setup a little bit I'll go ahead and remove our  duplicate let's focus on our parasolver let's see what we have so far so this is all right I might  want to go to buoyancy here let's maybe set this to a lower value point one and in the sourcing tab  I'll turn back on density and also temperature I'll keep these other settings as they are let's  take a look right so we have just a slight expansion kind of like a smoke bomb or something and this  will be fine just to demonstrate our other microsolvers so in our shape tab we have buoyancy flame  expansion that we know so far let's turn on wind and let's see what we get so this is pretty  straightforward we are simply going to push the wind in a direction which is currently on the X  if I increase the speed maybe we can see this better all right so again very simple and straightforward  a very annoying gacha with the wind is that if you have this wind option turn on and you want to  later add vectors particles by this pyrosimulation you have to go in the output tab and turn on this  add win...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_009.jpg

### Shredding & Gas Damp [89:39]
**Transcript:** we have turbulence so we are already familiar with turbulence we have all of the settings that we  are used to by now and generally here I only like to play with disturbance and swirl-size  settings so turbulence is the strength and swirl-size will be how big our noise is so generally I  don't really play around that much with roughness or pulse length in fact I can reset these values  if I want to add high frequency detail I will just use the disturbance instead so I generally use  the turbulence to get our larger swirls and then leave it to disturbance for the high frequency  and we can also control disturbance based on other fields so in the control field here we  could say that we only want turbulence where we have high density values or we can map this to our  flame field or any other field so hopefully by now you get a sense of how this stuff works  shredding is also a type of noise and this is based on the disturbance micro-solver in fact we can  see that over here we have kind of the same settings that we have in our disturbance the difference  with shredding as opposed to the disturbance is that shredding will keep the speed consistent to  what we already have while distur...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_010.jpg

### Setup, OpenCL & Padding [95:12]
**Transcript:** have the voxel size and if we lower this value we will increase the resolution but this naturally  will increase our simulation time but you will get more resolution in the simulation so the general  workflow is that I usually set a higher voxel size when I'm doing tests and while I'm adjusting  the sourcing and micro solvers and all the other settings I want the simulations to run as fast as  possible and then when I get roughly the look that I want I start to decrease the voxel size to get  higher resolutions and then finally I will settle for a final resolution on which I do the file  cache so I might set this to something really low like 0.02 for the final resolution and after  this I would do the file cache and save it to disk we have an option here velocity voxel scale and  this has been added more recently so if we increase this scale here it means that our velocity field  will have a lower resolution so this will in turn make our simulations go a little bit faster  but we might lose some of the detail now in the case where we have this container type vector  field like we created over here like this we have the option to set the resolution of this  velocity field directly f...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_011.jpg

### Collisions [107:59]
**Transcript:** let's look into collisions next and for this I'll first go to the sources here and I'll just  get rid of divergence and flame and also let's go to the shape tab and increase the buoyancy here to  maybe 0.5 so let's see what we get we just have this simple smoke rising simulation now which  will be fine so let's go ahead and drop down a box I'll place this over here and I'll press  I'll grab the handles hold down shift and I'll just scale this on the x and y and the z direction  so we just make it a little bit more stretched let's go ahead and after this I'll drop down a  transform and I'll press enter and I'll just move this over and maybe also move this on the side  all right so let's turn this into a collision and I'll also place down a null here just to keep  things organized and let's rename this to collision so I can plug this directly inside the second  input of the parasolver and now inside the collision tab this is by default set to collision geometry  so if I reset the simulation and press play we should see our collision with the box and we do so  everything works and this used the forming geometry is turned on so in case we had some animation  on our geometry it would pi...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_012.jpg

### Pyro source & Scatter [123:17]
**Transcript:** source as its own separate thing this setup is not really what you will often see I only set it  up this way to illustrate what the different volumes do usually you will base all of the volumes on  the same geometry so maybe I can just go ahead and I'll just grab one of these fears and I'll just  drag this over and we can start fresh in a new chain so the more efficient setup is to create  point attributes on the surface of this sphere and create different attributes for the different  volume so we have a density attribute a temperature attribute and so on and then we can turn all of  these attributes into volumes at the same time with a volume-restaurized attributes so from our sphere  we can do a scatter and we can just increase the total count here until we fill up the surface  and then inside the attribute VOP let's drop down a attribute VOP we can go inside and we can  start creating the attributes that we need so we know that in our sources we usually want to have  noise and breakups so we can base our attributes on a noise from our position I'll just drop down a  turbulent noise and I know by default that turbulent noise outputs values between negative 0.5  and positive 0.5 ...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_013.jpg

### Pyro Burst Source & Examples [133:41]
**Transcript:** pyrosource the pyro birth source is a new addition so let's drop this down let's type pyro  birth source and we'll drop this here so this is a newer addition to the pyro toolkit and this  really makes setting up sources super convenient so if we play the animation we just have a bunch  of points that spawn and then expand and disappear really fast so we see these only less for maybe  five frames and this is usually what we want for explosions let's maybe just set the display  here back to points but also on this node if we set this to lit sphere we can see that these  points here have already read on my scale which will help add noise in our sources and all of  these points have different colors which correspond to a different attribute so one color will be for  density one for temperature and one for bird we'll look at this in a second but right away we can  see that this node sets up a lot of stuff for us so I'll just set this back to points to see  this better now for a long while in Houdini we had to create these sources ourselves from scratch by  combining different scatters on spheres with noises or doing pop simulations and we can still  create our sources from scratch and t...

**Frame:** tutorials\frames\intro-to-houdini-pyro---full-beginner-course\frame_014.jpg


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
