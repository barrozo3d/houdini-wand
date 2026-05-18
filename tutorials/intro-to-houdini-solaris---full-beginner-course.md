---
title: Intro To Houdini Solaris - Full Beginner Course
source: YouTube
url: https://www.youtube.com/watch?v=3BX97YIQERE
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/intro-to-houdini-solaris---full-beginner-course/
frame_count: 0
---

# Intro To Houdini Solaris - Full Beginner Course

**Source:** [YouTube](https://www.youtube.com/watch?v=3BX97YIQERE)
**Author:** Voxyde VFX
**Duration:** 286m6s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Solaris is a huge part of Udini that's getting better and expanding with each update.  While Solaris is primarily built around the USD pipeline, we are going to explore more  the practical side of it and less the technical side. In the first part we are going to explore  each key ingredient in Solaris in isolation, so we'll take a look at the stage manager,  instances, lights and other important components, and in the second half we'll use all of this  knowledge to build an entire magical forest shot from scratch. As a challenge, we are going to  build all of the assets that we need directly in Udini without using any third-party libraries.  There's a lot to talk about, so let's get started and welcome to Intro to Solaris.


### USD & Scene Graph [0:46]
**Transcript:** It's impossible to talk about Solaris without mentioning USD, so Solaris is built as a,  or at least started as a wrapper around USD. USD is a lot of things at the same time,  but mainly it's a file format, and in this sense it can hold any type of 3D object,  it can hold materials, lights, it can hold meshes, curves, and pretty much anything that you can  find in a 3D scene. And the best way that I found this describe is sort of like a limbic on steroids.  Now USD is also a framework for how you build scenes, and really if you go to the USD documentation  from Pixar, you will find a lot of terminology and a lot of concepts, and it can be pretty  overwhelming at first. Now I just want to say right away that we don't have to know everything  from the start, and as we explore Solaris we will uncover more and more USD concepts as we go.  Now USD was developed as a studio workflow, allowing multiple artists to leverage all of their  assets in one single scene in a very efficient manner, so it's more of a pipeline in that sense.  And USD is here to stay, whether we like it or not, and more and more studios are adopting the USD  workflows, and a lot of studios already have incorporated U...


### Scene Assembly [12:58]
**Transcript:** like, and again this is if you are working as a solo artist, I'll go ahead and get rid of everything  and start fresh, and one of the ways that we can create geometry is if we bring it over from the  object level, or we can create it directly, sort of in size Solaris. Let's take a look at the  importing geometry part, let's go over back to the object level, and let's say that we build some  geometry over here, I'll drop down a Geo container, let's rename this, maybe this will be our hero,  and we are going to drop down the rubber toy, let's drop down a match size, and set the justify  y here to min, so it's on the ground, and we can also do a null, so we can point to this,  and this can become our out hero, so we can grab this, I will select this node and copy this with  control C, let's head back over to Lops, and we can do a sub import, and here in our sub path,  we can point to our, so this is the object level, our hero geometry container, and our out hero,  which points to our rubber toy, and we have this over here, we can specify a path here, and we can  notice that this here says path prefix, so we can place this inside, let's say maybe assets,  and we can have a sub director...


### Stage Manager [29:25]
**Transcript:** scene assembly is going to be moving things around, so let's see how we can do that, if I have this  last karma render settings node selected, I can press S in the viewport and I can grab an object,  now it's better if we show the object outline by turning on the display selection button over here,  and now if we press S and select an object, we are going to see the outline, and if I press  T, we can see we have the transform gizmo and we can move the objects around, and we also have  appended automatically an edit node right after our karma render settings, so I can now grab the  rubber toy and I can move it around, I can rotate this, I can press E for scale, R for rotate,  and T for translation, I can also select the assets directly from our scene graph, so if I select  Tommy, from the scene graph, now I can move Tommy around and I can of course scale and rotate and do  all of the usual transform operations, and we can see that all of these are stored in this edit  node that was added, and for example, the coolest part about working in Solaris is that we can  treat almost everything as sort of like an additive operation, meaning that if I were to disable this  node, I can now pre...


### Materials [39:30]
**Transcript:** there are quite a few ways that we have available, and let's explore some of these, so the first method,  and my preformatted of assigning materials, is if we drop down a material library,  now again, we can place this wherever we want in our chain, it just has to be after we place the  objects in the scenes, so with this material library, in order to create a material, we have to  double click to step inside, and inside here, we can drop down our material builder, so if you  have redshift or Arnold, you can drop down a redshift material builder or Arnold material builder,  but since we are going to use karma, we are going to use a karma material builder, so let's go  ahead and drop this here, we can also rename this, let's maybe name this green, we can step inside,  and this is going to be a material X shader, and we'll explore some of the things that we can do  with this material builder in a later lesson, but for now, let's go ahead and just change the  base color, so let's go ahead and let's make this green, and we can go up by pressing you, let's go  up one more time until we are at the Solaris level, and now if we look at our scene graph, we have  our assets, and we also have...


### Component Builder [49:19]
**Transcript:** subcreate and the sub important nodes, but a better way to author assets is going to be by using  the component builder, so if we were to drop down a component builder, we can see that if I place  down this node, this will automatically build for us this entire chain, so very simply put,  we have our component output over here, and we can now see our current scene graph in the case  that we have this component output, and it has a scope for the geo and the MTL, which is going  to be the geometry and the material, and if I rename this here, let's say that we are working on  our hero asset, I'll just name this hero, this will now update in our scene graph over here,  and we have our component geometry where we add the actual mesh geometry over here on the left,  and we can create our material inside this material builder here on the right, and with this  component material node, this will automatically apply the material to our mesh, so let's take a  look at a quick example, if I go to the component geometry node, we have a few settings here, and if  we wanted, we can create the geometry directly inside the component geometry, and this is what we'll  do in a second, but we can also s...


### Light Types & Light Mixer [63:12]
**Transcript:** and let's explore some of the lights that we have available, in earlier lessons we looked at the  Karma physical sky, so this one has a basically it's made out of two components which is the sun and  the sky, so the sky in this sense is going to act like a sort of HDRI, and the sun will be more  of a directional light, and we can control both the sun and the sky tab over here, and I really like  the Karma physical sky because it's a pretty fast light, and it's just something that you can plug  down in your scene, and you can get started with some really simple lighting, and really for outdoor  scenes, especially this works surprisingly well, so we can play around with the solar altitude,  which will bring our sun down, and we can see we have sort of like the sunset look, with the  solar azimuth we can spin the sun around so we can change the angle of our sun, and finally we  also have the angular size over here, let's maybe bring the sun down even more so we can see it,  as we increase or decrease the angular size, this will make our sunlight smaller, and when our  light is smaller, our shadows will naturally be sharper, and this will be the same for any type of  light that we add,...


### Volumetric lights & Emissive Lights [79:06]
**Transcript:** first have to add an actual volume that can contain all of our light and luckily Solaris  provides us with a karma fog box so let's drop this here after our camera node I will type here  karma fog box so we'll add this here let's maybe also disable the geometry outline and  currently it's this container so we can go ahead and increase the uniform scale here and we can  straight away start to see our lights are going to be scattered throughout these volumes and we can  also use the handle here and usually this fog box should contain the entire scene so if you have  a camera in your scene as we do in our case we just have to make sure that all of our objects are  contained within this fog box already that our fog box contains all of the objects so I'll  press escape to hide the handles and now we can see all of our lights have this volumetric effect  to them and we can also disable the light display in our viewport so if we want we can go back to our  light mixer now and we can play around with our lights we can maybe grab our let's grab our key  light and maybe I can increase the exposure here and when we increase the exposure this will  naturally gives us more volumetric in our sce...


### Instancer [88:56]
**Transcript:** Instensor and the Instensor will be a very familiar workflow if you are used to working at the  sub-level with the copy to points node so it's sort of like the sub-version but we have more options  when it comes to the Instensor and in general it's really powerful and you can easily scatter  millions of polygons across your scene and have the scene running pretty smoothly so let's go ahead  maybe we can just ignore our scene that we have here and I'll just drop down the Instensor node  and just like the copy to points we have two inputs over here only in the case for copy to points  we have our geometry that we want to scatter on the left and the template points on the right  and in the case for the Instensor the right input is actually where we are going to place the  geometry that we want to instance and the left input is basically for us to plug into our scene so  basically if I have this scene over here and I want to add some instances I can plug this pretty  much wherever I want of course this depends on how you set up your scene but I can just plug this  over here for example and now this will error out because we actually need our points that we want  to use as our scatter p...


### Layout LOP [100:53]
**Transcript:** node and let's go ahead and just drop this down in our scene again let's maybe just place this  down and I'll drop down a grid before it and let's link this up like so because the layout  now works better if we already have some geometry in our scene again we can place this layout  node wherever we see fit in our chain but we can just focus on this grid for now so I'm not a huge  fan of this node I found it kind of hard to control the times and in general I didn't have the  best time using it maybe I haven't used this enough but I always seem to prefer working with  the instancer instead but let's see how this works so for the layout node we have a few options  that we can use to scatter instances but first we will need to load in our objects over here  and we can load them through our layout asset gallery and if you don't have this window you can  hit this plus you can go to new paint app and you can go to Solaris and here you will find the  layout asset gallery and again Solaris provides us with this default library that we can use and you  can create your own libraries you can for example whenever you use the component builder you can  also store a thumbnail and add it to a gall...


### Initial Layout & Camera [108:15]
**Transcript:** it all comes together and use all the knowledge we have now in Solaris to create a simple scene  from scratch and in order to showcase as much as possible of the potential of Solaris we are going  to create all the assets necessary to build this scene entirely in Houdini so we are not going to  be importing any third party assets and this is to showcase a lot more of the power of the component  builder and how it can all really come together and give us a smooth and seamless process now we  can start directly at the stage level so I can hop over to the lobs context over here and we can  drop down a subcreate to start placing down elements and start to work on our layout the only  problem with doing this is that we are pretty limited in our camera capabilities so when it comes  to creating a camera and especially animating a camera I would much rather do it at the  sub level so in the object context because I personally like to work with a lot of null parenting  and create some very simple camera rigs and it's a lot easier to do at the sub level and while we are  at the sub level we can also place down some simple elements that we can then bring into Solaris  and then from Solaris w...


### Ground & Water materials [126:25]
**Transcript:** we can dive over to the lobs so in stage and we can bring all the elements together if we do a  scene import we see that we have different presets of this node we have seen import all so if I  drop this we can at this point also go to one of our Solaris desktops over here so let's go to  the Solaris mode that Houdini provides us and when we do our scene import all we bring in our camera  so we really bring in all of the objects that we have if we go to our camera here we also have  camera animation so everything is working now I don't really like working this way we can  use this if we want and we can append a stage manager from over here and we can reorganize our  chain in however way we want but usually what I like to do is keep things as separate as possible  this way I found it's easier to have individual treatment for each element and again this is more  concerning the workflow if you are working as a solo artist so let's go ahead and get rid of this  and let's just bring in our camera first we can do a scene import and we can choose the camera's  preset let's drop this here and by default this filter will be set to cameras and here to the  objects let's also make sure that th...


### Grass & Hair material [146:31]
**Transcript:** directly in our stage context so in Solaris we can drop down a sub create from here let's place  this from the start in the right path so we will do slash ENV ground and we are going to do a  grass group and we can plug this in our merge and let's see how our chain will look like we don't  have any geometry inside so this will not update let's go ahead and if I step inside we can  create just one simple blade of grass by using curves so let's drop down a line and we can frame  in on this and let's do a resemble from here and this will give us a few points now we will  probably need to scale this down let's set the length to maybe something like 0.2 and let's go to  the resemble and maybe decrease the length so we have let's try to go for maybe five points from  here we can do a bend and let's set the capture direction here to 0.1 and 0 and the capture  length should be the length of our curve so I will copy this parameter and let's paste relative  references and if I press enter we can grab our bend and we just want to bend this slightly in  either direction this will be fine because we are going to change the orientation per individual  instance so we will use just simple curves t...


### Tree Asset - Component Builder [165:59]
**Transcript:** treatment and we can also explore more of the component builder so let's go ahead and we can  place the component builder pretty much anywhere for now let's drop down the component builder so  this will build our entire chain and right away I will rename this component geometry here let's do  something like tree and the component output let's just export this to a usd asset that's going  to be called tree dot usd and we can set the display flag on this and let's start by building our  geometry so we'll step inside the component geometry and here we will focus on our high resolution  mesh so our render mesh which will go in the first output here and we are going to use the  tree lab tools which are pretty good but if you already have a tree asset maybe from speed tree  or any other library you can just bring that geometry in but to keep things 100% in Houdini we can  use the lab tools so let's start with a trunk generator so labs tree trunk generator let's take a  look and we can framing on this with f and right away I will do a Tommy geometry and place this on  the side and template this with w maybe translate this so it's right next to our tree and maybe I want  this tree to be a ...


### Tree Geo & Material Variation [197:21]
**Transcript:** drop down a component geometry variants and we will plug this here similarly to how I showed you  in the earlier lessons by default with this node we can simply add more component geometry nodes  and we can plug them inside our variance input node here and we can cycle through these variants  so this is the default way this will work and we can see the source mode here is set to inputs  but we have another mode which is going to be this number option here when we are activating this  this mode will allow us to use a seed value inside our component geometry to procedurally generate  multiple different variants so let me show you how this works let's maybe set the number a very  variant here to tool and let's step back inside and for now let's ignore our tree geometry and just  focus on some simple geometry let's maybe do a platonic solids and let's say that this will be our  acid and we can get rid of our proxy for now so if I go up we will only have our platonic over here  so again with this component geometry node here activated and set to the source mode number I can  step inside and I can use that seed value to generate multiple different versions let's maybe  set the display to...


### Instances & Variations [219:29]
**Transcript:** create our point geometry first of all so let's go over here where we have our stage manager for  our hero trees and we'll drop down an instancer again we can plug this maybe we should plug this  after our stage manager I usually like to keep things separate so we could also disconnect this  and just do a merge with our stage manager but in this case we can just append this over here and  we can straight away rename this one to bg trees all right and for our prototype we are going to use  this asset that we built and we can bring it with a reference node so we'll drop down a reference  and let's see what path we used over here I'm going to grab this path where we saved out our tree  component and let's go to our file pattern place this here all right and we can place this as our  prototypes so in our bg trees this is where we will have to create our point geometry so we can  step inside and I usually like to start with a simple point until I figure out the prototype so  let's hit this plus and create one point and if I go up if I look at the bg trees and this is why  and we can see our tree over here let's maybe disconnect this from our stage manager for now so  we can just focus o...


### Particles in Solaris [239:15]
**Transcript:** simulation let's go ahead and we can place all of these nodes here inside a network box and this  will be our trees we'll move this over to the side and maybe make some room and I'm holding down  shift while dragging to select this node and everything that's above it as well so I can also  make some more room over here and for our particle simulation we can just create this at the  sub-level so we can either do a sub-create here and work from within Solaris but in this case  since we already have our ground geometry at the sub-level let's head over to this geocontext  and we can do our particle simulation here so I will unpin the viewport and here is where we have  this ball as a reference for where we want our particles and on this node if we wanted to bring  over geometry from Solaris so maybe we need a reference for where our trees are positioned let's go  ahead let's go back in Lops and if we look at our graph we can see that to bring in our trees and  in this case let's maybe just bring in our hero trees I will select this group over here let's  place control C and this will copy this path to our hero trees we can go back over in object tab  let's do another geocontainer and w...


### Render Settings & AOVs [261:04]
**Transcript:** render settings so let's drop down below a karma render settings node and right away like I  mentioned in earlier lessons let's point this to the correct camera let's also here we can change  the resolution and here I will set this to xpu and in reality I would have appended a karma render  settings node way earlier so usually when I'm building a scene I will drop down a physical sky  and maybe the karma fog box and the karma render settings node all of these three nodes I would  usually place them in the scene graph really early on so that we can build our layout and our effects  on top of these already existing settings so now if I look through our camera if we have our  render settings node this will now use whatever settings we are choosing over here so if we wanted  to increase the quality we can increase the path trace samples we can set this to maybe 256 so now  we can see our renders will take longer but they will have a lot less noise on that node if we go  over to the advanced tab in more recent updates the karma xpu has some new settings for us that we  can choose now generally I would leave these at the default settings which they have over here  but for example we can ...


### Conclusion [285:26]
**Transcript:** the intro to Solaris course we've spent the last four and a half hours learning Solaris and  probably we just uncovered about 10% of it the reality is that this one single course will not  make you a master in Solaris but I really hope that now at least you can feel a little bit more  comfortable with it and that you can use these lessons as a solid foundation on which you can  keep improving if you are interested in Solaris or Houdini in general check out my workshops and  courses on Voxite.com but for now this is it for intro to Solaris thank you so much for watching  and hopefully we'll see each other again in a new course



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
