---
title: Environments in Houdini | Part 4 - Vines, Rocks and Fog
source: YouTube
url: https://www.youtube.com/watch?v=cXbdFwd3u9o
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, vdb, procedural, fracture, environment, scattering, volumes, fog, third-party-plugin, advanced]
extraction_status: complete
frames_dir: tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Environments in Houdini | Part 4 - Vines, Rocks and Fog

**Source:** [YouTube](https://www.youtube.com/watch?v=cXbdFwd3u9o)
**Author:** cgside
**Duration:** 40m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so we will continue on our little environment and the plan for today
[0:07] I'm not sure yet but we will tackle these hanging vines and also do some procedural rocks
[0:14] and if we have time we might move this in into Solaris, let's see. So yeah, let's get into it.
[0:21] All right, I just saved the new scene from where we left, where we the last thing we did was to
[0:27] scatter some trees, I'm going up a bit and let's move these down and also move these parts
[0:37] a bit down, so let's move all of these and get some space in here.
[0:44] So the first thing we're going to do are the those hanging vines. Let's object merge.
[0:51] So I actually need to move these down, oops, and move these in here. Let's object merge this
[1:05] null in here that is already remeshed so we can take advantage of that. But still the resolution
[1:13] is not too much so I'm going to remesh it a bit and the goal is to scatter some points in here
[1:19] in this part of the bridge and then generate the vines from there. So I'm going to remesh this
[1:26] again, so remesh to bridge, I'm not sure if this is labs or not and we're going to do find out
[1:34] do and I believe I didn't change anything else and I'm just going to clip it along the Z axis
[1:42] so clip along Z and by 3 minus 3 so we just have the front part as you can see, I could have
[1:52] clipped it before but now that I have the same density I'm not going to change it. So now we need to
[1:59] we have the curve for for the for this the start of the bridge and we can use that curve to
[2:05] transfer and attribute to the to this geometry. We could easily paint it manually but
[2:12] what we'll learn if we do that right so let's instead go the artway and merge in the curve where
[2:18] is that let's see it's right here so let's select this and go in there where is right here all right
[2:33] so now that we have to curve we need actually to match size it so it is on this side let me see
[2:41] what sort of values I used in here so I'm going to match size let's see and we don't want anything
[2:52] along the x and along the y so none and we do mean in here or center sorry center so we have it
[3:02] right in the center it will be easy to transfer the attribute from and let's see
[3:08] so it's right there now we're going to sweep it so we just have a bit of geometry so let's go
[3:21] with sweep it will be easier to transfer the attribute so we will do ribbon and a width of point
[3:31] of 9 see if that is the value I used yes so the thing is we can do create a natural
[3:41] and do a natural transfer but since I want to do some operations in Vax I will do everything in
[3:47] Vax but you don't need to so you don't have to Vax everything but as a learning experience it
[3:52] might be useful if you learn the art way so for the mask we can use a simple pc open function
[4:03] so let's do that let's create the handle so it will be a need and we do pc open and we will
[4:10] look for input one so the sweep geometry the position and the current position and we will define
[4:17] the radius and let's say we search for 10 and we'll do f at mass before we equal to pc num
[4:28] pc num bound and the handle and let's say if it's bigger than zero let's see how that looks so
[4:37] masked and it doesn't look like much does it because I've done something I need to define the radius
[4:44] of course and the radius you can let's see we can start to introduce the radius in this case I
[4:51] use the radius of 0.115 so something like that but in this case as you can see I'm also getting
[5:00] the mask in here and I don't want that I just want in this middle part well this is a particular
[5:07] look I'm after you might go just with this and be fine so in this case I'm gonna use the dot
[5:15] product from the normal and an app vector to remove some of the parts of this mask so let's let
[5:25] let's do floats and I'm gonna be creative in collie dots and dot between the normal and an app vector
[5:34] in this case I'm gonna set it to minus one and let's say if that is bigger in this case I want
[5:43] a right here if that is bigger than 0.5 and we can just say f at mass multiply equals to dot
[5:54] and that does that why did I have done that
[5:59] now I wonder if that part is anything important because that doesn't seem to change much
[6:10] well let's see if you now let's remove these parts in here actually so let's do I was hoping that
[6:18] that would get rid of some of the value in here so as I can see it's removing some but it's not
[6:25] that important actually let's see if we change this to point one so point nine oops point nine
[6:35] and yeah that starts to get rid of some of the parts that are not along the wire vector
[6:40] but in this case is not as you can see it's not that important so but now we can remove these extra parts
[6:47] we don't want these extra bits well let's do f at mass multiply equals to ramp ramps are always
[6:56] a great way to control these attributes so let's do relative point relative point
[7:03] pounding box and we will do the incoming geometry the current position and the x in this case we
[7:10] want the x axis and let's go in here and change this to ill and now we can start to remove those parts
[7:22] and in this case I didn't use I use linear and I'm going to introduce some values in here
[7:31] so oh my god let's see we can introduce this sort of values and I can be picky about it but let's see
[7:42] this one is fine at the middle then I want to linear so this is fine so I guess this is fine
[7:52] let's see if that's not project is changing anything and it doesn't but let's leave it there so
[7:59] sorry about that yeah I just didn't reveal the file and then maybe I was trying something
[8:05] different at that at that moment but yeah let's ignore that and keep going so now we will do a
[8:13] scatter on that mass get reboot so let's scatter and we will scatter on the mask and we will do only 35
[8:24] and change the seeds I'm gonna be 19 but we can change that and now I did a peek in here because
[8:33] I don't want the roots of the vines to be showing exactly at that part so I'm gonna peek it a little
[8:39] bit let's see if we have normals we do so we will peek and we will not recompute the normals
[8:45] because we might need them and we will do minus point 05 just peek it a bit in and what else do we
[8:51] have here this is always a surprise to me because I didn't review this so let's do one it should
[8:56] wrangle and we will set the normals along the z to be flat otherwise the vines will go in this
[9:05] sort of random directions at least that's so let's do normal dot z it will be equals to 0.0
[9:18] and as you can see it will flatten out those normals along the z let's see let's move this down a
[9:25] bit we need to save it more space and we will create them all in here I don't name it but you can
[9:35] do your naming and be organized and now we will create the vines again I will be using simple tree
[9:43] tools so trunk maker and I'm gonna connect these in here so let's do add sparing put and connect
[9:54] these in here just to know that this is related this now disconnected and let's also connect it to
[10:03] the seed points yes so what sort of things we will change in here so first of all going to trunk I'm
[10:13] gonna change the segments to 40 to have a bit more resolution the length 0.5 and randomize it quite a
[10:21] bit and change the seed and for the weeds so the weeds I'm gonna set it to 0.14 so quite small and
[10:36] randomize it also so now I'm just picking random numbers and let's go with the seed let's see if I
[10:44] change anything else in here no I think it's fine now let's go to modifiers and apply some noise
[10:52] so let's go with noise and I'm gonna change it to noise 2.0 and really just the amplitude
[10:59] change the size of the noise also to 0.6 and we get possibly play with the offset let's see like
[11:08] this one and I believe that's all for this tab now let's move into truth truth bism and play
[11:15] with gravity so in this case I'm gonna set it to 2 so it goes like that and that's fine and let's
[11:24] also introduce some chaos so in the chaos let's introduce 0.375 whoops whatever I done
[11:33] let's 0.375 so some chaos and we could possibly change the seed and we can go in here and change
[11:43] the seed of this let's say I like this one now we just need to do trunk measure no tree measure
[11:51] I'm still getting used to this we could probably have tried to do this with the labs tree tools but
[11:59] I'm not sure about that because I haven't played much with it I just think this is a good deal
[12:07] these sort of tools they are very very versatile so in this case we can change here the profile let's do
[12:14] heal and that will be flat and now it's hard to see so let's change the background am I recording yes
[12:21] let's change the background now it's too light they're about but that's fine let's create a name
[12:29] and I also need to do this for the rest of the assets but we'll do that in a bit so let's
[12:35] create binds and I guess we can merge this over and see if this doesn't crash because I've been
[12:42] having some crashes lately so that's fine let's disable the mask and we could probably clean
[12:49] those attributes and as you can see it's not looking alphabet I think it adds a bit to the
[12:55] to the overall environment and it will look nice with the fog and everything so that's this part done
[13:05] so now we will do the rocks and ignore me if I go a bit slow because I haven't looked I haven't
[13:12] looked into this file in a while so this might go a bit slow but let's do another geometry container
[13:21] and call it rocks and we can color these let's say this color which is always nice and let's
[13:30] dive in the first thing we will do a basic Voronoi fracture to get some rock shapes and then do some
[13:38] volume noises to distort the shape this is very basic but that's that's what we can do
[13:46] this time frame let's say do not spend too much time on it so let's change let's create a
[13:51] platonic and change it to dot decay idron did I say that correctly I'm not sure so now we will
[13:57] do a nice oh let's get there some points inside so we'll do a nice offset and I believe I changed
[14:02] the resolution to 50 so the uniform to have more resolution and let's do a scatter and I just
[14:11] did a few so seven I want only seven rocks so let's change this to dark again and now we can do
[14:22] simple Voronoi fracture so Voronoi fracture let's connect the inputs let's do an exploded view
[14:33] and these will be our rock shapes so what am I doing now I'm going to move them to the zero zero
[14:43] position so to the center so for that I'm gonna back and we have in here a name attribute as you
[14:49] can see which will be useful to move them to the center so we'll do just this three pack them
[14:55] and as you can see in here if you can see that might be too small but we have seven points or seven
[14:59] frames and now we can just do a wrangle and on the packed frames we can do a V at D equals to zero
[15:07] and they will be moved all to the center instead of the wing of our each loop we'll do a
[15:11] far it's loop anyways but anyways so now we can unpack and let me see I believe I need to move
[15:19] the name attributes or does it have already so it transfers we don't need to transfer it again
[15:25] and we will do for each named primitive where is that for each named primitive and let's see as you
[15:33] can see we're iterating through all of them we can do a single pass for now and we will do a
[15:41] basic very basic edge damage so I'm going to rematch just like we did for the bridge
[15:50] so let's rematch and in this case I used a value of point two that's fine attribute blur you know the
[15:56] deal and the attribute blur is also default in this case I'm going to increase the iterations to do
[16:04] and I'm going to do a mount them let's move this a bit and the mount and let's see what sort of
[16:13] values did I use so an amplitude of point 19 and of course we need a positive offset
[16:21] and I also change the element size so to point I'm going to try to get the same results let's see
[16:28] if that works but we can you can easily play with this values and well now let's do a fully
[16:33] unintersect and you can see we start to get these sort of results which are nice let's see the
[16:42] others so this rock shape I guess this is fine but you can possibly play with the scatter seeds and
[16:50] get different results as you can see and it will be pretty fast since these operations are
[16:55] shipped now we will do some we'll add some basic details using VDBs so we need to rematch this so let's
[17:06] do a rematch and I'm gonna change this to point two that is fine and let me see I have an
[17:18] attribute in here that I'm not sure I'm going to use let me see that do we use that attributes
[17:24] so I have a mask in here yeah I'm not using so we will just do a VDB from polygons VDB from polygons
[17:34] let's see I'm gonna use a white a low white a low resolution I'm gonna increase it but for now
[17:42] let's keep it like that and let's say we want an exterior band of one tree so we can
[17:48] have more exterior vuxels and feel interior that's fine now we will do convert VDB
[17:59] and convert this to polygons so we can preview the final result
[18:04] and let's do volume vote and I'm going to go through this very oh I need to change
[18:11] since this is binding to density it's always better to change this to density if it's fog it's
[18:18] already density but we can do that for us the absolute so we don't have to bind that sport to surface
[18:23] and whatnot or do a volume sample so let's go through this quickly basically we create a static noise
[18:34] we will fit the values so feed range where we'll multiply constants to control the effect and
[18:40] let's connect all of these and we add it at the end so we add it to the current density
[18:48] and we need to get the position to the position and let's do frequency create a constant middle
[18:55] click create a constant and do a multiply constant so we can increase the frequency of the noise
[19:01] so change the size of the noise and yeah am I connecting this so why is not doing anything
[19:10] now so let's change this in here to 10 and it's not doing anything oh because I'm not
[19:19] connecting to the value now it's doing something let's change this multiply constant to 0.055
[19:26] so we start to see the results and in this case I'm gonna use a frequency of 3 not 10
[19:35] and I'm also going to change the noise type because this one is pretty boring
[19:40] so we will do worldly cellular F2F1 and change the offset to 80 that's the value I get going
[19:51] and I'm also going to add some fractal but to the position and first of all we want to
[20:00] play with the source mean so we just get this sort of holes on the on the rocks so I'm going
[20:06] with a value of 1.1 something like this and now I want to distort the position before it's
[20:12] connected to the noise before it's sampling the noise so I'm gonna do a net a terrible
[20:18] noise connect the position to the position and since we're going to distort the position we need
[20:24] that 3d noise and we need a zero centred noise so in this case I'm gonna use parts convolution
[20:31] noise which is sort of between minus 1 and 1 and connect this in here and it will be too much
[20:38] by default so in this case I'm gonna change the amplitude to 0.35 so it's a bit less and maybe play
[20:45] with the frequency and we get this sort of nice result at least I think it's a nice result and if we
[20:52] increase this to 0.06 we start to get a bit more detail as you can see all right let's reduce this
[21:00] again to 0.1 and I believe I used it yet another noise so I'm gonna duplicate all of these
[21:11] so old alt and drag down and let's add these to the same input to same output and what
[21:21] did I change in here so first of all I'm gonna change the repetition to 0.5 and I multiply constant
[21:33] a bit less so 0.16 and we might just look at these noise without the other one so we see what
[21:42] we're doing this case I didn't use a hit I used an unclamped bit so it's range unclamped
[21:51] it's connecting or not okay and I'm gonna use a value in your 0.745 so we get this bulging effect
[22:06] and I'm also having the turbulent noise in this case I'm gonna change these a bit to 0.43
[22:15] and change the frequency to 1 so you just have to play around so as you can see this one doesn't look
[22:20] out bad I'm gonna change it to 1 and I believe I also changed the noise let me see
[22:28] yeah I changed the noise in here to just have 1 and play with the offset
[22:36] so 170 we start to get this look let me actually see if that noise makes any sense
[22:57] so in here I have that particular noise but it's not adding much is it or I do I need to increase
[23:04] the resolution I guess I need to increase the resolution let me see something in here so 0.16
[23:14] 0.1 did I use the compliment yeah I used the compliment in here so it goes a bit to create this
[23:21] worldly look as you can see so that is fine let's connect this in here and connect this one in here
[23:28] and I guess this is fine let's just change the resolution to 0.16 go until your PC starts to scream
[23:40] so as you can see nothing too special but we get some nice details and at render time we will
[23:45] also add some displacement so it will be a bit better I guess let me change again this
[23:53] so so in this case
[24:01] what we will do next now we will need the name attribute again we could transfer but let's just
[24:08] do one attribute triangle and create the methane port nodes so this will give us a value of each
[24:14] iteration as you can see in here we have iteration and we connect this in here
[24:19] and we can change this to primitives and say I at class it will be able to detail one iteration
[24:30] and that will just give us a class attribute that we can use later and the thing is now we need a
[24:37] low polyversion also so a proxy version of this and since the port loops don't give us 12
[24:43] we can merge them in and then delete them after the loop so for that I'm gonna just create a dot
[24:51] in here and we will name and we will name this to ipoly I believe so rock with that rock ipoly
[25:04] and let's do in here rock low poly and we will do poly reduce in this case we will do it quite a
[25:15] bit so poly reduce and we will reduce it we will just keep 5% so this doesn't matter it's just a
[25:25] low polyversion to act as a proxy so we won't render this and now we can do a merge
[25:30] and connect this in here so damn it sorry about that so we'll do a merge and I guess this is fine
[25:43] you can just compile this if it works at all so let's do compile oops compile blog let's connect
[25:52] this in here it's connected yeah and let's not forget to change this to multi-treated let's see if
[26:02] that takes too long let's see so tool 3 and it has to calculate the vdb's and do the poly reduce
[26:09] so it's already done that's fine and we will do a file cache so I haven't looked at the results of
[26:18] all the the rocks but let's find so let's do rocks ash ash demo and we don't need time
[26:28] dependent we will just do save to this single frame and now we can split the the the the the
[26:37] high poly let's do it now and another now and change this to out rocks high poly
[26:50] and do out rocks all out poly okay we could possibly do a blast and do that name
[27:04] oops we can do in here so at at class is equal equal to zero and do points and the
[27:12] little not selected so at class is not point sorry is primitives and we can look at our result let's
[27:19] see the other ones and I guess this will work fine as you can see nothing special but I don't
[27:25] like it it's okay nothing special we could have probably changed the offset of the noise to have
[27:31] more variation but let's not worry too much about that so yeah that's our rocks then
[27:38] so now just to finish it off and I've just seen ready for salaries we're going to do some basic
[27:46] fog so we have our rocks taken care of so let's do a geo and name it fog and just for fun just
[27:55] change the color and we will need to dive in here and let's see we can create a null in here
[28:05] and copy the path control C let's go to the fog and object merge and paste
[28:14] so we have the bounds of our geometry and we can actually my mistake we need to connect this
[28:22] in here so we have everything we could possibly get rid of the get rid of the trees did I connect
[28:34] let me see did I connect the plane also probably you need also to connect the plane where did I do
[28:42] that's in this case I also need to connect the planes so let's do a merge and we will do in here
[28:52] we will connect in here and we will also add a name so that's fine let's copy we already have
[28:57] copied so let's go to the fog and we have an object mode let's create a bound and that will be fine
[29:06] right I didn't change anything in the bound just default settings and now let's do a VDB
[29:10] from polygons we will create some fog because I'm not a particular fan of the falloff of the
[29:17] the fog in salaris what is it called fog karma fog box I believe so I'm gonna do my own so VDB
[29:25] from polygons at least in my test my test C didn't look that good so I'm gonna create a density fog
[29:33] and create a point of five and do a basic volume what
[29:38] and in here we will start with the relative bounding box so yeah let's do relative time bounding box
[29:52] relative bounding box we can possibly connect the position and let's do a vector to float to to get
[30:00] in this case we want to get the z axis let's connect that to density and as you can see it starts to
[30:07] falloff based on the position we have but we need actually to fit it a bit so feed range
[30:15] feed range and we can start to play with the values so but first of all I want so we are in here
[30:26] and I want the less fog on the front so let's do a complement doing a vertex result as you can see
[30:34] we start to lose some volume in here and I have some values I'm gonna play with source mean so
[30:39] 0.295 so we'd remove some of that but I don't want to completely remove it so I'm gonna add some
[30:45] value to the low bound so 0.13 as you can see we can change that and that will be fine
[30:53] and we also would multiply constant this to about 0.3 so it has a bit more density less density
[31:03] now this is looking quite boring so we could possibly introduce some noise right here when
[31:09] we are sampling the position so let's do turbulence, turbulent noise and I'm gonna change this
[31:17] to a 3d noise and sparse convolution, connected position and let's change the frequency to 0.6
[31:25] and the offset to 100 these are some values I played with, quite a big amplitude and also some roughness
[31:36] and let's connect this and see the result so let's add and connect it in here so we start to get
[31:42] this sort of result this but I want to play a bit with the attenuation so something like that
[31:49] and maybe do some more turbulence the detail of this noise this for won't be really seen with
[31:57] all with everything happening but we just have it there so it will it will be seen somehow but not
[32:07] this much detail as you can see right here so we could possibly play with the offset as you can
[32:12] see and we start to to have less to have a different result and if we change the amplitude as well
[32:17] as you can see let's change that to 5 and that's fine let's see how everything comes together
[32:26] so now we might do the scattering of the trees the rocks so we can everything we can compose
[32:34] everything at the end and have a nice result let's see um every near did I
[32:41] did I use the rocks in here so we have the trees and we do have the rocks in here
[32:55] so let's go above right where we have this and let's do an object merge and let's look for those
[33:03] rocks so rocks out we can do a lot of polyphano and
[33:16] let me see out rocks do I believe I forgot to add the not putting here so it's great enough
[33:24] on the rocks geometry and connect this and call it out rocks and copy this so we can switch between
[33:36] ion low poly easier easily so let's go to the geometry and paste this in here and now let's do a blast
[33:47] and in this case we can blast we can keep the low polys since we're going to do a basic
[33:51] scattering in here so let me see in this case we will do another object merge and we need to
[34:03] merge in here the terrain so where is that so I don't ever know I need to shape where it is so
[34:18] so after the in here so let's read it now and call it out to the rain
[34:35] copy and where was I in here so let's paste it in here so we want to scatter some rocks
[34:44] right on the edges or on this simple lake so let's do that so there will need a scatter and we
[34:54] will scatter on the river mask so scatter and I'm gonna scatter just a few so wind if or and I'm
[35:03] gonna scatter on that river mask that we have so that's fine let's see and we will change the
[35:13] global seed I have a value in here but we might need to play with it and of course remove the
[35:18] relax situations let's see I might need to play with this seed all right let's do a connectivity in
[35:30] here and I guess points will be fine on the points and we will have a different glass for each
[35:42] rock let's do an attribute from pieces because if we copy the points let's let me just
[35:51] check that out let's make sure we pack we copy the points it will copy all the rocks at the same time
[35:58] so we need to do a natural from pieces and let's name it class and we will pick randomly and we
[36:05] can play with the seed in a bit so let's do this and now in here we can pick a piece attribute and
[36:12] go with class and now we can play here with the seed so for now let's do let's see we might need
[36:22] to play with this seed and let's do first of all an attribute that just load or the p-scale
[36:29] or in this case I use the attribute randomized and we will randomize the p-scale and change this
[36:37] to one since it's a float and let's see what sort of values did I use in here so in this case I
[36:45] changed this to custom ramp and played in here so let's do this plan and I played with these values
[36:52] and I don't want them so small so let's do I just want some big and most of them to be small
[36:58] so I'm not going to be too picky about it and let's do a natural but to just load to
[37:06] change the overall effect so in this case we can just do multiply
[37:13] so constant multiply and we can change the size let's change this to 1.3
[37:19] oops not to 1 and the the thing is now we can change this
[37:28] and I'm not sure why it's changing the seed it should be the same rods but I guess it has
[37:35] something to do with this connectivity in here so yeah let's see
[37:45] yeah so we can keep this the low poly and let's do one margin see if this doesn't crash I just saved
[37:53] it just in case and let's merge it and let me see this is getting too much on this side
[38:04] let me check that reverb attribute so I guess we could have played with it but honestly I'm just
[38:13] going to play with the seed so let's see and I'm not going to worry too much
[38:24] let's keep it like this and we can change this to the high poly
[38:28] and we start to see the results of our efforts and we can probably change the seed also
[38:39] I like that one is so I don't like this one so you can play with it until you find a nice result
[38:51] let's keep it like this for now we could probably create also what camera
[39:02] so let's save just in case we can look at the final results and now let's also go in here and change
[39:12] this file and introduce the geometry and this is starting to get a bit slow but you can see where
[39:22] we're going with this so honestly I'm gonna leave it here and in the next part we can start to
[39:29] focus on the salaries setup and materials and we will move the scattering systems to salaries
[39:36] which will be pretty easy and yeah if you would like to have the files of this scene you can do so by
[39:47] signing up to my Patreon and you can also find exclusive tutorials in there hours of exclusive step-by-step
[39:53] tutorials and also some courses and all the scene files from my videos so yeah let me know in
[39:59] the comments what you think and I hope you are enjoying this one and I'll catch you in the next one thank
[40:07] you



---

## Captured Frames

- [0:10] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_000.jpg
- [4:00] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_001.jpg
- [8:15] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_002.jpg
- [12:30] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_003.jpg
- [17:00] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_004.jpg
- [20:30] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_005.jpg
- [30:30] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_006.jpg
- [38:30] tutorials/frames/environments-in-houdini-part-4---vines-rocks-and-fog/frame_007.jpg

---

## Structured Notes

### Core Technique
Part 4 of the environment series: growing hanging vines from a VEX-driven `pcopen()`-based arch mask, building procedural rocks via Platonic + Voronoi Fracture with layered VDB volume-noise surface detail and a compiled per-piece edge-damage loop, then authoring a custom hand-built **fog volume** (VDB density + layered noise) instead of relying on Karma's built-in fog box falloff.

### Summary
Hanging vines under the bridge arch are grown from a mask built almost entirely in VEX as a learning exercise (rather than pure VOPs): the bridge's arch curve is Match-Sized and Swept into a thin ribbon purely to serve as an attribute-transfer proxy, then a wrangle uses **`pcopen()`** (point-cloud open, searching the swept ribbon's points within a radius) to build an initial proximity mask, refined with a normal·up-vector dot-product multiply (to suppress mask value on non-relevant-facing surfaces) and a **relative-bounding-box-position ramp** (VEX `chramp()` against normalized X position) to taper the mask off toward the arch's edges. Points are Scattered on that mask (~35, seeded), Peaked slightly inward (preserving existing normals) so vine roots don't visibly poke through the stone, and a wrangle flattens `N.z` to zero so vines hang relatively straight down rather than splaying in random directions. The same **Simple Tree Tools** Trunk Maker (fed the scattered points via spare input + seed-points input) grows the hanging vines with high segment count (~40) for smooth curves, small randomized length/width, layered noise, strong downward **Gravity Tropism** (~2) plus **Chaos** (~0.375) for organic droop, and a flat "heal" profile in Tree Mesher for thin vine geometry. Rocks are built from a **Platonic** (dodecahedron) noise-offset and scattered (~7 points, uniform resolution ~50) then **Voronoi Fractured** into irregular chunks; each fractured piece is packed and zeroed to the origin (`v@P = 0` on packed prims) for consistent per-piece processing, then unpacked and run through a **For Each (name/primitive)** loop doing cheap edge damage (Remesh ~0.2, Attribute Blur ~2 iterations, small Mountain with positive/non-zero-centered offset, Volume/Boolean Intersect) — the same "cheap chip damage" pattern from Part 2's bridge stones. Surface detail is added via a hand-built **VDB volume-noise VOP network**: VDB From Polygons (low initial resolution, exterior band ~1-3 voxels) converted back to polygons for preview, driven by a **Volume VOP** reading/writing `density` directly (not surface/absolute), combining multiple layered noises — a primary Worley Cellular F2-F1 noise (frequency ~3, tuned offset ~80) added to base density with fractal detail on position (source-mean ~1.1 to punch holes), a **Sparse Convolution noise** (zero-centered, -1 to 1) used to *distort the sampling position itself* before the primary noise reads it (amplitude ~0.35, tunable frequency for more/less detail), and a second duplicated noise layer (Turbulent Noise variant, unclamped range, different repetition/multiply-constant/offset values, complemented) blended in for additional "worldly"/bulging surface variation — all layered until the rock reads as naturally pitted rather than a smooth Boolean-cut shape (with the note that render-time displacement will add further detail on top). Each rock gets a `class` attribute (via Metadata/iteration read inside the fracture loop) plus both a high-poly render version and a **Poly Reduce**'d (~5%) low-poly proxy version merged together and cached to disk via a File Cache, then split apart (`class == 0` etc.) for later scattering. The final section builds a **custom fog volume** rather than trusting Karma's default fog-box falloff: a Bound around the merged scene geometry (terrain, trees, rocks, bridge) feeds a VDB From Polygons → Volume VOP where density is driven by relative-bounding-box position (Z axis) fit-ranged, complemented (less fog toward the front/camera), and offset (source-mean, low-bound value, multiply-constant for overall density), then layered with a 3D **Turbulent Noise** (Sparse Convolution, tuned frequency/offset/amplitude/roughness) added to the sampled position for organic, non-uniform fog density rather than a flat gradient. Finally, rocks are scattered onto the river/lake-edge mask from Part 1 (Scatter, Connectivity for per-piece class, Attribute from Pieces to assign `class`, a custom **ramp-driven `pscale` randomization** biased toward mostly-small with occasional large rocks via Attribute Randomize + a custom ramp, plus a Multiply-constant overall scale factor ~1.3) and merged with everything else, wrapping up with the plan to move all scattering into Solaris in the next part.

### Key Steps
1. **Vine-attachment mask setup:** Object Merge and further Remesh the already-remeshed bridge-arch section; separately Object Merge the arch curve, Match Size (mean/center, no X/Y scaling) to align it, Sweep as a thin ribbon (width ~0.09) purely as an attribute-transfer proxy for the mask VEX.
2. **PC-open proximity mask (VEX):** in a wrangle, use **`pcopen()`** against the swept ribbon's point cloud (radius tuned ~0.115) to build `f@mask` from `pcnumfound()`, refined by multiplying in a `dot(N, {0,-1,0})`-style up-vector check (threshold ~0.5-0.9) to suppress mask value on incorrectly-facing surfaces.
3. **Mask edge taper (VEX ramp):** multiply the mask by a **`chramp()`** lookup driven by the point's relative-bounding-box X position (linear/custom-shaped ramp) to taper mask value off toward the arch's left/right edges rather than a hard cutoff.
4. **Vine seed points:** **Scatter** ~35 points on the mask (seed ~19), **Peak** slightly inward (~-0.05, preserving existing normals so they're not recomputed), then a wrangle sets `N.z = 0` to flatten normals so vines grow relatively straight down instead of splaying in random directions.
5. **Vine growth (Simple Tree Tools):** **IFT Trunk Maker** fed the seed points via a spare-input + seed-points connection; segments ~40 (smoother curves), length ~0.5 (randomized), weight ~0.14 (randomized); layered **Noise** (amplitude, size ~0.6, tuned offset); strong downward **Gravity Tropism** (~2) plus **Chaos** (~0.375) for organic hanging droop; **Tree Mesher** with a flat "heal" profile for thin vine geometry; name-tag and merge over the bridge.
6. **Rock base shapes:** **Platonic** (dodecahedron) with a noise offset, **Scatter** (~7 points, uniform resolution ~50 for point placement quality) inside it, then **Voronoi Fracture** using those points as emitters/seeds to break the platonic into irregular rock chunks (Exploded View to preview).
7. **Center pieces for uniform processing:** Pack the fractured pieces, run a wrangle setting `v@P = 0` on packed primitives to move every rock to the world origin (avoiding an explicit for-each just for this step), then unpack.
8. **Per-rock edge damage (For Each, Compile Block):** **For Each (name/primitive)** over each rock: Remesh (~0.2), Attribute Blur (2 iterations), small **Mountain** (amplitude ~0.19, positive/non-zero-centered offset, small element size) for micro-surface bumps, then **Boolean/Volume Intersect** to carve subtle chips — identical cheap-damage pattern to the Part 2 bridge stones; wrap the loop in a **Compile Block** (multi-threaded) for speed.
9. **VDB surface detail via Volume VOP:** Remesh again (~0.2), **VDB From Polygons** (low initial resolution, exterior band ~1-3 voxels for extra outside detail), convert back to polygons for live preview; build a **Volume VOP** binding directly to the `density` volume primitive (not surface/absolute) that: samples a primary **Worley Cellular F2-F1** noise (frequency ~3, offset ~80, fractal detail on position, source-mean ~1.1 to punch holes) and adds it to density; separately runs a **Sparse Convolution noise** (zero-centered -1..1, amplitude ~0.35) to *distort the sampling position* fed into the primary noise (rather than adding directly) for more organic pitting; duplicates the whole chain with different tuning (repetition ~0.5, multiply-constant ~0.16, unclamped range ~0.745 for a "bulging" look, Turbulent Noise variant, frequency ~1, offset ~170, complemented) and blends both noise layers together into final density.
10. **Class + LOD versions:** inside the fracture/damage loop, read the loop **iteration** via a Metadata node and store it as a `class` primitive attribute (since for-each doesn't expose piece index directly by default); after the loop, build both a full-res "high poly" version and a **Poly Reduce**'d (~5%) low-poly proxy version, merge both together, and Compile-Block/Multi-thread the whole rock-generation network for practical iteration speed; cache to disk via a **File Cache** (single frame, not time-dependent) once satisfied, then split high/low-poly outputs by `class` for downstream use.
11. **Custom fog volume (instead of Karma's built-in fog box):** build a Bound around the merged scene geometry (terrain, trees, rocks, bridge — remembering to actually wire in all relevant merge inputs), **VDB From Polygons** to generate a base fog volume (density ~0.5), then a Volume VOP: relative-bounding-box Z position → Vector to Float → **Fit Range** (with Complement to reduce fog near the front/camera, source-mean and low-bound offsets, multiply-constant for overall density ~0.3) drives density falloff, layered with a 3D **Turbulent Noise** (Sparse Convolution, frequency ~0.6, offset ~100, amplitude/roughness tuned) added into the sampled position for non-uniform, organic fog density instead of a flat directional gradient.
12. **Scatter rocks along the river/lake edge:** Object Merge the low-poly rock proxy plus the terrain/river mask from Part 1; **Scatter** a handful of points on the saved river mask (seed tuned, relax disabled); **Connectivity** (points) + **Attribute from Pieces** to assign each scattered rock instance its own `class`; **Attribute Randomize** (custom ramp-shaped distribution) drives `pscale` biased toward mostly-small rocks with occasional large ones, plus an overall **Multiply constant** scale factor (~1.3); Copy to Points the (packed) rocks onto the scattered points, then merge high-poly rocks in for the final render-quality pass, tuning scatter/connectivity seeds until the distribution reads naturally.

### Houdini Nodes / VEX / Settings
SOPs: Object Merge, Remesh (Voxel/Grid, multiple resolutions), Match Size (mean/center), Sweep (ribbon), Attribute Wrangle (VEX: `pcopen()`/`pcnumfound()` proximity mask; `dot()`-based normal-direction masking; `chramp()`-driven relative-bbox-position edge taper; `N.z=0` normal flattening; `v@P=0` packed-primitive centering; per-piece cheap edge-damage math), Scatter, Peak (preserve normals option), Platonic (dodecahedron), Voronoi Fracture, Pack/Unpack, For Each (name/primitive, wrapped in Compile Block with multi-threading), Attribute Blur, Mountain, Boolean/Volume Intersect, VDB From Polygons (exterior band control), Convert VDB, Volume VOP (binding to `density`; Worley Cellular F2-F1 noise; Sparse Convolution / Turbulent Noise for position-distortion and direct density addition; Fit Range, Complement, Multiply Constant, Vector to Float, Relative Point/Bounding-Box Position), Metadata (loop iteration → `class` attribute), Poly Reduce (proxy LOD), Merge, File Cache (single-frame), Blast (class-based split), Bound, Connectivity, Attribute from Pieces, Attribute Randomize (custom ramp), Copy to Points. Third-party: Simple Tree Tools (IFT Trunk Maker: segments, length, weight, Noise, Gravity Tropism, Chaos; Tree Mesher: flat "heal" profile for thin vine strands).

### Difficulty
Advanced/Expert — combines VEX point-cloud queries (`pcopen`), a hand-authored multi-layer VDB volume-noise shading network for both rock surface detail and custom fog density, and Compile-Block-wrapped per-piece procedural loops; assumes strong VEX and VOP/volume fundamentals.

### Houdini Version
20.5 (continuation of the same terrain/bridge project; UI consistent with Houdini 20.5).

### Tags
#vex #vdb #procedural #fracture #environment #scattering #volumes #fog #third-party-plugin #advanced

---

## Related Tutorials
Direct continuation of environments-in-houdini-part-3---vegetation-with-simple-tree-tools.md and environments-in-houdini-part-2---stone-bridge.md (same author, same bridge/terrain project — reuses the Part 2 cheap-edge-damage pattern and the Part 1 river/lake mask). Author announces the next part will move scattering systems and materials into Solaris; cross-link once ingested.
