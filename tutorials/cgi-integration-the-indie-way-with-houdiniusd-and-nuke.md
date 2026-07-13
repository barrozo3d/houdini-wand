---
title: CGI Integration | The Indie Way with Houdini(USD) and Nuke
source: YouTube
url: https://www.youtube.com/watch?v=RchQ9K5QXtI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cgi-integration-the-indie-way-with-houdiniusd-and-nuke/
frame_count: 0
frame_status: pending-selection
---

# CGI Integration | The Indie Way with Houdini(USD) and Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=RchQ9K5QXtI)
**Author:** cgside
**Duration:** 47m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cgi-integration-the-indie-way-with-houdiniusd-and-nuke <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. In this video I'll go step by step into the wild world of VFX
[0:06] integration. This is by no means the only way you can do it, it's just the way I know.
[0:10] So we'll start in DaVinci Resolve to do the proper color transforms, track the shot
[0:14] in Nuke and finally go to Odini where we'll do a simple simulation and put everything
[0:19] together in Lobs USD workflow. So let's dive in.
[0:24] So to get started we will need to prepare our footage, things it was shot on log and
[0:30] we need to export the JPEG sequence to work in tracking and also in Odini. So let's do
[0:36] that in DaVinci Resolve which I'm using the free version, so not the studio and it will
[0:41] work as fine. So let's start by naming this labada footage prep. Let's create the project.
[0:52] Now in media I'm gonna load my file which is this one, this MOB, I'm gonna change the
[0:57] FPS, the frame rate is 30, that's fine, that's what we'll be working and let me mute
[1:05] this and this is our footage. As you can see it has this strange color because it was
[1:10] shot on log and a specific log because this comes from a phone so it's not very good quality
[1:16] but again I try to replicate as much as possible the workflow. Since I don't have a proper
[1:21] camera I use my phone which is a good phone and it has this option to shoot in log. So
[1:28] yeah let's go to the edit tab and dragging these to the timeline. As you can see the timeline
[1:33] starts at one hour I don't know why but I'm gonna change these to 00 and let's see we have
[1:40] about 8 seconds of footage. Let's save now let's go to the color because we need to work
[1:48] on Aces and for that we need to do some conversions and also we have this log that we won't use
[1:54] so we just need to convert this properly. So the first step is to drag in a node, Alt S.
[2:01] Now let's go to the effects and searching here for color, space transform, drag it and depending
[2:08] on the camera that you shot this you will need to adapt in here but basically this input color
[2:14] space, input color space has to do with the color and this input camera has to do with the luminance
[2:21] so we need to, I'm going to change this to p3d65 this is again recommended by Samsung
[2:32] since I shot this on a Samsung phone and the input camera I'm gonna set it to Rive log c3
[2:39] so something like this then we want to export this as a linear Aces so AP1 Aces and this one will be
[2:48] just linear so we have the linear footage and make sure you don't use any tone mapping because we
[2:55] are not using not using this to compress the the highlight and whatnot and the rest is fine so
[3:02] this is our first step then we're going to do again Alt S to create a new node and drag in again
[3:08] another color transform and this time we're going to use we're going to transfer from Aces since
[3:14] it's the input and linear and we're going to output this into srgb or rx709 in this case and use
[3:24] again of 2.2 I'm not an expert in color science but this was the settings that work for me from
[3:32] seeing other videos and other people work on this kind of footage so make sure we set some
[3:38] tone mapping because right now we want this to be properly displaced on monitor so I'm just
[3:48] going to use luminance mapping and make sure we have enough range and apply this for transform so we
[3:54] get this srgb footage let's say and if we control it to disable this we will have the linear footage
[4:03] that we can use later for compositing let's find let's enable first let's say we enable this one
[4:09] and go for the exports in here I'm gonna browse let me see let's create a new folder and I'm gonna name it
[4:21] Aces linear or let's go the vada Aces linear demo
[4:31] and let's press ok and for this one I want to export the nxr rgb off with some compression
[4:40] I believe that's the one and timeline resolution which is 4k and I'm gonna just name it in here
[4:49] so the vada Aces linear demo let's find let's add the render queue now let's go to color again
[4:55] and control the to enable oops control the on boot to enable this srgb output or rack 709 you could
[5:03] also place a contrast adjustment and a color adjustment in between for this because this is just
[5:09] for display purpose and for tracking also so it might help to add some contrast but I'm going to
[5:14] ignore it for now and now I'm gonna call this vada rack 709 demo I'm gonna browse and in here I'm
[5:25] gonna create a new folder and call it like this ok this is for the the location and for this I'm
[5:35] just gonna do a jpeg sequence and I'm gonna use just hd will be fine we don't need 4k for tracking
[5:43] and previewing so hd will be fine and I guess that's all and we need to wait this render queue
[5:50] select both control as and render all that's wait just a second and it should be done right now
[5:58] so let's have a look at the jpeg sequence first and there we have and we also should have
[6:07] the xr sequence which is aces linear so that's the footage done and next we will jump into Nuke to
[6:14] do the tracking so now in Nuke let's process and load in the aces profile and I also want to
[6:24] change the frame range from 0 to 2 63 and frames per second to 30 and the resolution can be set
[6:33] just to hd so that's fine let's save this let's do v2 and now we want a load our footage so press
[6:44] our to read let's go in here video and I believe is this one so yeah let's have a look and here we
[6:56] have our footage that's fine and so the reason I'm using Nuke is to do the tracking of course
[7:04] because we don't have tracking in Odini we could have tried Blender but again I don't know Blender
[7:09] very well and Nuke I'm not an expert but I can do tracking in Nuke as is pretty easy and if you
[7:16] don't have Nuke you can try the trial just like what I'm doing right now I'm using the trial
[7:22] but I might buy it if there's enough interest in future tutorials about Nuke and integrating Nuke
[7:28] into the Odini workflow so we have the project setting set let's do a camera tracker and we're
[7:36] going to use this better one this better workflow and I know that this camera I have information
[7:45] from the camera so I'm gonna feed it in here so I'm gonna say in focal length known and I'm gonna
[7:52] change it to 23 and then I also know the film back size which is in inches I'm gonna set it in
[7:59] landscape mode to 1.3 and one this is from a Samsung phone where I shot this footage and the rest
[8:06] is fine let's just track okay the tracking is done what am I doing the tracking is done as you can
[8:15] see and we can operate solve and let's see we have some reds but I'm not going to even worry about
[8:22] and here is our scene we need to orient it properly so let's go in here select a few and
[8:29] grum plane set to select it and we get something like this I also would like to scale this because
[8:35] if I do a geo import and I bring in let me see on geo I have here a human reference
[8:45] as you can see and I will need to size this properly so let's go into scene and change the uniform
[8:52] scale to two this will work so I can get rid of this and now I'm gonna also select this and press
[9:02] e to rotate and go to the top view let's zoom out and rotate this so we can have an easier time
[9:12] on our dinner so there you go now that we have scaled and everything we can just um let's see
[9:21] we can go into the camera tracker and create this scene so yeah let's not only the output and let's
[9:29] create and here we have our camera okay to these we should have a camera in here and we have the
[9:39] tracking and now let's do the following I want to generate a mesh also from this so right now
[9:46] we have this sparse pink cloud but I want to generate a mesh also so for that I'm gonna create a
[9:52] near point cloud generator gonna connect this to the camera this to the source and just create an
[10:02] elbow with control and in here I'm gonna press analyze sequence this will take a second
[10:09] that's done now let's do track points and make sure we set the frame range
[10:14] okay now we have a point cloud and we can get rid of some of this visualization and let's go to
[10:21] vertex selection select everything right click create group this will create a grouping here
[10:26] that we can now bake into a mesh so let's press this button and wait a bit
[10:31] okay that took like a minute so let's look into this mesh and get rid of this selection and make
[10:39] sure you enable your delighting and we get something like this which is nice we can see here the
[10:44] wall the lavada and the flowers and the little road in here so we're good so now I want to make
[10:52] sure this is sitting properly though I'm gonna do in here a small setup to generate a wireframe
[10:59] over our footage so unfortunately as you can see this is this is the new workflow that revolves
[11:07] around USD but unfortunately the new USD workflow for wireframe shader is not working at least on my
[11:16] head so we're gonna use the old one which which are these green nodes with the old 3D workflow in
[11:23] so let's first of all export this mesh so let's do export GX ports no it's not GX ports yes it's
[11:37] GX ports sorry so let's do a GX port no we need to write GU I believe yeah write GU because this
[11:46] is the old workflow and in here we just gonna write this to ABC and let's do lavada round
[11:59] round GU underscore demo bo1.abc
[12:08] let's execute and just export one frame that's fine now let's as you can see I want
[12:15] we can't export this to USD as far as I'm aware so what we're gonna do is to load in here
[12:22] so geo import and now we can load so USD this one and let's get rid of this I don't I'm not sure
[12:36] where this is coming so anyways let's load that and let's do a GX port and export this to USD
[12:45] oops USD that's fine let's just modified modified and let's do USD and we just export one frame that's fine
[12:59] so now we're gonna do that test to see if our geometry is aligning properly with the tracking so
[13:06] for that I'm just gonna do a read geo and I'm gonna read this one so this geometry a bit of a work
[13:14] around but we have to do this because the wireframe shader is not working with this new
[13:19] 3d workflow so something the founder should be aware of and we're just gonna create a scene
[13:29] and make sure it's classic in 3d classic and we're also gonna create in here a wireframe shader
[13:39] as you can see there's the better one but it's not working so I'm gonna use this old one and we
[13:43] need an apply material and we also need a scanline render scanline render classic again and we're
[13:51] gonna load the camera from here and we're gonna load in the connect this connect this to be object
[14:03] and the last thing we need to do is to connect this so to the footage so let's drag this one in here
[14:15] let's drag it to here and let's look at that and there we have our wireframe render as you can see
[14:25] and then we can just do a merge and let's merge this over our background I don't know what to
[14:34] using you sorry guys so I was just gonna load that over and we probably need to shift X this yeah
[14:45] so it switches the input we need this the footage over our wireframe and now we can finally
[14:53] test it so let me just cache this and I'll be right back
[14:57] so as you can see this is cached and it's working perfectly and we should have this time result
[15:03] in Odinia at least let's try to have that as you can see it's aligning pretty well and overall
[15:08] I'm happy with the result so let's just do one final step in here these wires in here are crazy
[15:16] anyways so let's just export our camera let's do a right Giu
[15:21] not right Giu so Giu export I always make a confusion because I need to export this as a
[15:28] USD camera we don't need to look at this anyways and let's do USD and let's export this levada
[15:38] cam export then be to dot USD and let's make sure we export the frame range
[15:46] and it should export our camera and the next step is to load everything in Odinia which we will
[15:53] do next again just the reminder that I'm gonna upload the footage and all the setups from the
[15:59] Vinti Resolve to Odinia and also Nuke on my Patreon so you can access all the files in there
[16:05] or you can create your own and do your own tests so I see you on Odinia so iriare in Odinia let's
[16:14] in a fresh news in let's wrap a Giu and I'm gonna work on the stage so I'm gonna create a
[16:20] love network let's dive into it and I'm gonna change these to salaries and enable the timeline
[16:28] and let's the oh we're not in solarium so I'm in solaris so let me just set these to view
[16:33] port size don't display environment lights and change the background to dark it's fine now we
[16:39] want to set this to 30 FPS and 260 from 0 to 260 let's apply make sure we set in year 260
[16:51] so that's fine now we need to load our camera first and you probably or I was doing that using
[16:59] the reference but that apparently doesn't import the frames per second metadata and it will
[17:07] mess up our scene I found that by debugging with some friends over the CG Wicked Discord which I'm
[17:12] very grateful for their help and instead of using the reference we're gonna use the sub layer
[17:19] and this is just for the camera don't text me why these are USD shenanigans so just going to load
[17:26] in here the USD and we should have a Leveye the cam export them is this one let's have a look
[17:33] there we have our camera whoops and it's working fine let's name this cam and as you can see if I
[17:43] enabled these in here and I do in here I don't load the the layer metadata the cam the camera
[17:52] changes so it doesn't interpret the frames per second that's why we need this sub layer and from here
[17:58] we're we're going to load our ground so we can use a reference this time since it's just a static
[18:05] geo and it will work great for that so let's go in here ground geo USD that's fine let's create a
[18:14] karma setup and right away we're gonna change this to XPU and we're gonna load our camera in here
[18:23] so camera camera let's find and let's look through that camera and there we have it should be
[18:31] aligning very well but we also need to load the background image so for that I'm gonna do a camera
[18:36] edit on here and look at this and let's drag in here our camera to the primitives and I'm going
[18:45] to view and enable this background image and I'm gonna load in here sewing video of other
[18:51] Rx709 demo that's fine do a white frame and it should be aligning which it is which is fine
[19:00] and now we also have this black bar so we need to edit in here the
[19:05] these resolution or the aspect ratio so let's do that let's enable in here first the camera aperture
[19:14] and focal length I want to set the focal length to 23 and I happen to know that
[19:22] with the Dory's dot-tole aperture is that one that we input in in Nuke so 1.3 and that will convert
[19:31] to about 33.03 millimeters and now we should have the correct framing as you can see
[19:41] so this was based on experiments and on what me audets so you will just have to bury me also we
[19:49] have this time dependency which we don't want so let's do sample frame range and now it will be
[19:55] much faster to preview our footage it's still loading but as you can see once it's loaded it
[20:00] it works real time so let's just let it load so as you can see it's working pretty well let me just
[20:08] get rid of this we have our geometry that we will use to cast shadows and we could even project
[20:14] this the texture or the footage to the ground geometry and have some light bouncing and whatnot
[20:22] I'm not going to do that I also don't didn't care about lens distortion and so I went pretty quickly
[20:28] about color transforms but again this tutorial will be big already so I don't want to bother you
[20:35] with that kind of stuff but if you're doing this properly make sure you do some lens distortion
[20:40] correction and that sort of stuff that sort of stuff and also do some research on color science
[20:47] and why we're using this oh speaking about color science we also need to check our so edit also
[20:54] settings I'm using ACCG and ACS 1.0 SDR video for the view transform and if we're looking near
[21:01] right click and color correction I'm using SDR display and ACS as you can see to have a proper
[21:08] display of our footage so guys that's this part done the next part we will do a very simple
[21:15] simulation of some balls rolling down this little road so let's do it at next
[21:23] okay guys let's do our little simulation let's stop this and go to G again let me change this
[21:29] to this layout and we're gonna start by to a USD import file import that's it and let's load in the
[21:40] so it's in USD, Lavada, Ground G, is this one? Yes by the time it should be this one and we want
[21:50] we don't want any time dependency import frame is one that's fine and let's to unpack and
[21:58] polygons and we get something like this we want to use a lighter so our animation our I want to
[22:05] do some balls rolling down this and as you can see our camera it will we can also load our camera
[22:10] so lock import camera and let's load the so vjg.lopnet camera edit and let's load that camera
[22:21] and if we'll look through it so we want our balls emitting right here so let's find let's press age
[22:33] let's go in here and let's create a curve so it will be simple and let's go through the top view
[22:41] so control tool let's create let's impress w in here and create a curve it will be something like
[22:48] these just two points and let's enter and press F and select press K and bring it up
[23:00] let me see yeah this will be just fine okay now let's do a re-simple
[23:10] and we will have some points to play with let me see I change these just to maximum segments and
[23:17] five so we have six points then we're gonna create a sphere
[23:26] and I'm gonna change just a scale to 0.0.1 and I'm just gonna copy two points
[23:36] I'm trying to do this pretty quickly because it's already a pretty long video
[23:41] so let's do also an attribute randomize and randomize the orient which works not this one
[23:49] orient which is four dimensions and we want just playing here with random or maybe in here change it
[23:58] to inside sphere so let's pick one let's find now let's load our geometry and create a dot net
[24:07] I'm not gonna use the the sub workflow rbd sub workflow I'm just gonna use the top one because it
[24:15] will be really simple to set up so we load these as our geometry as our first inputs a geometry to
[24:23] emit and this one is a collider but we need to make these spec primitives and we will we'll also
[24:28] need to change the name because otherwise we will have a conflict so yeah let's do one step at a time
[24:34] let's dive into the dot net and we will do the following we will need a
[24:42] rigid body solver we will need rbd back object and let's connect it in here this one to the
[24:51] output and we need some gravity and we will also need a merge because we will load the static collider
[25:00] so static object let's shift our in here shift test and so let's load our object which will be
[25:12] so where is that so in here first context geometry so let's load back and let's find let's make sure
[25:21] we use a sphere and no padding and I also don't want to compute center of mass see let's find
[25:29] now let's load our collider so sub-pad will be something like open footpad and we will load
[25:40] the second input so 0. and let's do this let's go to the collision just gonna set these so let's
[25:52] show guide geometry this will be a convexel just for quick demonstration I'm gonna use concave it's
[25:57] not a very good idea but it will work really fast in this one so we don't need to worry about let's
[26:02] I did the guide geometry and now let's see do we need to play with something here let's just
[26:10] see what this does so we're boring we want actually to emit more spheres so for that I'm gonna do
[26:18] pop source to emit some spheres so pop source and we're going to source all geometry and use first
[26:32] context geometry so we'll emit this geometry and we want to emit just on a few frames so let's say
[26:39] every 10 frame so dollar f modulo 10 is equal equal to 1 I'm not sure so dollar f modulo 10 is equal
[26:49] equal to 1 let's see that as you can see now is emitting but it's also creating in here a conflict
[26:55] because we don't have a point name attribute so let's go back and create that really quickly
[27:01] so buried me let's create a wrangle in here on the points let's set it set name
[27:09] set name we're gonna do it on the points because this is spectrometry and you want the
[27:16] name attribute on point so as it name it will be equal to concave it this is just to join some
[27:21] strings and we're gonna use let's start with a prefix called ball underscore then we're going to
[27:28] use it away to convert the point number to a string and let's let's just see what that gives us so
[27:37] if we look in here we have ball 0, 1, 2 and 3, 4, 5 but then again we also will emit every 10 frames
[27:44] so we need a different name otherwise we will get duplicate after emitting the second batch so
[27:50] for that we're just gonna pin in here maybe there are easier ways to do this but this is the way I found
[27:57] that work so we're gonna also use the frame so f or just add frame and I guess this will be fine
[28:09] so now we get some time dependencies in here so let's just see that points and we have these in here
[28:19] so every frame we will have a different variation so that shouldn't conflict anymore but have a look
[28:27] and now is not complaining anymore as you can see so there we have but I'm not liking too much
[28:34] this result so I think I'm just going to quickly create a vector field maybe or let's just
[28:43] try in here in the pop source let's go to attributes and add to add to velocity and let's do a
[28:55] velocity along the legs let's say 2 let's try that to see if we can bias them yeah it's too much
[29:04] I don't know if it like that so let's get rid of this and let's do another way and this will be a
[29:11] chance to talk about how to create a vector field so let's duplicate this in here I was trying to
[29:19] do this quickly but we will have to do this properly so let's create a curve and let's just
[29:26] know we know E these let's create a curve in here let's say we start and we create a curve okay
[29:34] so let's start something like this I want basically to guide this ball and let's do it almost
[29:43] quick then we can just do a resample let's do subdivision curves and this will be too much let's say
[29:53] 0.5 this will be enough let's do a ray and to our geometry and we can just do
[30:04] let's do norm no let's do attribute no let's do vector sorry and let's do minus 1 or 1 sorry
[30:16] and we have the curve projected to our geometry that we can now orient along curve
[30:24] and let's do the following let's name this well now let's look at that attribute
[30:30] and this should be going in the right direction so I want to push the balls towards this direction
[30:37] that's fine now let's create a vector field really quickly so we get down and I want to set this one
[30:47] is this correct so let's just do let me check something in here
[31:02] yeah this is correct I just want to change a bit maybe this and copy to here to give it some
[31:09] padding then we're gonna do a VDB from polygons and in this case I want to change a bit
[31:16] the boxal size and change this to well and to a wrangle up not this one volume wrangle
[31:25] now let's just sample the velocity in here so be it well and we need also to convert this to a
[31:33] vector VDB so let's just do this you'll be simple one and we want to sample the well we
[31:40] should rename that and using the position and the current position this won't do anything because
[31:48] we need to do a VDB convert and we need to convert this to a VDB and VDB type to vector flow
[31:55] is this correct let's see yeah vector and vector let's just do a scatter on these could be this
[32:05] VDB and do we just change the size to three and we will do well volume trail heavily that's the
[32:14] name yeah this is the points and this is the attributes and we also need to increase in here
[32:20] these bounds so let me see is this one so let's do this one and this one and point two so it's not
[32:31] this one sorry you see this one and this one so let's copy and paste and do let's say point back to
[32:41] give it some bounds and as you can see our velocity field is working let's see over our geometry
[32:48] I guess this will be fine maybe we can increase it's 0.7 yeah this will be fine
[32:56] so now we have in here let's create an all let's name it out well and we can now load this into
[33:11] our doblets our dot that and load this as our third input and let me see what I've done in here
[33:23] I will do just pop it back by volumes yeah that's it pop it back by volumes connect this in here
[33:33] and we will do third context geometry and the well and we want to update velocity
[33:41] and I guess default settings will be fine so let's just have a look let me actually disable this
[33:48] yeah and let's have a look on now is going to look so as you can see it's dragging the balls to
[33:55] this direction some are falling to throw the love other but that's fine I don't bother about that
[34:01] but I also want to add some noise so let's do some wind and this is dragging to the long less and
[34:09] let me know if you're still following to this point because this is already going for a while so
[34:14] let's change the amplitude to 3 a bit while I know but we will do something in a bit and let's be
[34:23] now is a bit wild but is more randomized but as you can see they are still moving a lot in here
[34:28] so I want to change that behavior so let's create an age attributes it's a pop wrangle
[34:34] and let's do f at h it will be very plus equal to f at h plus equal at time ink and this should
[34:50] give us an age attribute and now in the pop wind we can do the following we can load the
[34:56] amplitude so the amplitude is called amp so we can do amp it will be equal to select
[35:06] f at h is smaller than threshold so h trash if that is true we want to input the amp which is
[35:19] 3.0 otherwise we set it to 0 and now let's create a parameter and the age threshold I'm just going
[35:27] to set it to 1 and now if we look we will have that disturbing effect in here but then it will go
[35:35] smoothly after one second a one second since they were born let's say the particles or these spheres
[35:44] let's see all that looks and we will probably just render some frames and I guess we will
[35:51] strip down the end and this beginning so we get just a few frames in between guys you can go
[35:57] ahead and make this a bit better I'm just gonna continue this so we get something done today
[36:04] so let me see there are also some spheres stopping near which I'm not a big fan so
[36:13] let me go back and let's look in here at these cello these and these yeah we need to increase
[36:21] these so let's say 1.5 and now let's look again at our simulation
[36:30] and they should be falling down
[36:34] yeah I guess there will be some that will get stuck in here
[36:49] so this doesn't didn't happen on my original file because I didn't orient
[36:54] than this way but it will be out of frame as you can see so we don't need to worry about
[36:59] so let's move on from this top net we can just create a top import let's drag this top
[37:08] network and load just the balls we don't want to colliders so that we have it now let's do a natural
[37:18] delete and in this case I just want to keep the velocity the ID might keep the age and also the name
[37:34] and now let's do a file cache let's export these as balls
[37:39] same demo the frame rate is fine so let's just save to this okay now I also want an
[37:49] apparently we can't use IDs in Solaris the name ID it will be taken by
[37:57] by USD so we need to somehow have another attribute like a class attribute so I'm just gonna
[38:03] do an attribute swap in here and let's do a copy and I'm gonna copy the what oh I did this
[38:09] wrong I want to do the lead ones I like that now let's just save to this and now we don't have
[38:14] those attributes let's do copy and change the ID to class and now we will have the class attributes
[38:22] which is just an identifier for each sphere that we can use to randomize the colors let's do a USD export
[38:29] and these are packed primitives so we want to do in here in the primitive definition create point
[38:37] instanceer and let's just export this to if USD and also an in let's do v2.usd and I think we render
[38:53] frame range and just save to disk and there we go and I think that's all guys in the next part we
[39:00] will just do the final rendering and integration with the footage so let's do that next okay guys let's
[39:06] jump into Solaris so we have this animation and we can import over our footage so let's go to the
[39:13] top net change these to Solaris oops that's too so Solaris 2 and there we have our settings our
[39:23] scene and let's load as a reference and let's load in here so both on in v2 is this one I guess
[39:33] this one and let's see how that looks and there we have our animation and I think this is fine
[39:42] so apparently we don't have enough frames
[39:45] so is this correct
[39:56] so let's write a load it instead as a sub layer well maybe that's the issue
[40:02] and let's load in the animation
[40:05] and we still got something here because our frames per second is different
[40:17] okay as I found it we need to in here copy layer metadata make sure we set it to yes
[40:21] and now it's loading the correct frame rate I was thinking I was not going to find it so
[40:28] that's the call bit now let's have a look at this and this should start around frame 90 so we
[40:35] gonna get it in there so I am not seeing so let's change this to balls and
[40:49] no so this is reference I don't want this let me just do a bit
[40:58] oh we don't want to delete this we want to delete this and load as a sub layer
[41:09] the balls animation and make sure we do yes in the metadata now let's have a look if this is
[41:17] properly assigned and should be and yeah I guess this is working so now let's change this
[41:28] to start at frame 120 and we will do until about 240 so 240 now let's have a look
[41:42] this should be enough frames for us to render so this will be fine now let's do the following let's create
[41:54] let's create a serial library oh I've created a machine learning at work I don't want that
[42:03] Yaldini so I want a material library the shortcut is broken now and I also want
[42:14] so I'll slow this in here so this is the ground
[42:25] and this is the balls I need and we want a dome light
[42:34] and I'm gonna load in here an HDR from polyaven so let me just load that HDR
[42:43] and let me show you how it looks so we find a little environment light
[42:51] I should be seeing it so
[42:55] okay there you are this is the light we're going to use which is a similar lighting that I
[43:03] add in my original footage I didn't capture an HDRi because I don't have the equipment so we're
[43:13] just gonna use this dome light at the fake effect and it will be just fine so let's try to load
[43:21] in your hour camera and do a render so let's be framing your sister render
[43:31] and of course it's not rendering because I probably forgot something oh let's do just rendering
[43:39] but let's do a restart render and still we don't see it let's look at why
[43:51] so let's
[43:59] hmm oh maybe we need to assign let's first of all let's do a shadow capture
[44:08] and let's load in our primitive software is that so the without the ground geo
[44:17] oh let's look at that oh I know why because we have some left of film going on in here so let's
[44:28] disable left of field now it's working and we should have a shadow but we need also in
[44:36] nearer days we need to add all our shadows to beauty which is somewhere in near so shadow
[44:43] catcher add a lot shadow let's have a look at it and now we have the shadows working and we also need
[44:51] the motion blur so we're going to the camera in here and the enable these and these
[44:58] and then we need to go in here since we have a velocity vector on our points we want to put
[45:04] the camera effects and do velocity blur and let's do velocity blur on the axis now we have proper
[45:12] uh motion blur let's just create the material now let's name it calm let's create a paramaterial
[45:18] builder and these are both both matte and let's load in usd bring bar reader and let's load in
[45:28] a means called class that we export it let's do a random color it's connected in here let's play
[45:37] with seed and connect these to base color color so a specular of 0.1 and assign these to the
[45:50] page we get this result but see if we render we should get this and we have the motion blur so
[45:58] might be a good idea to enable in near to the denoiser but we also need it on the old out so we
[46:07] denoises the shadows books and we should even here the shadows denoise that's fine and now let's
[46:14] just do a quick render of this so I'm just going to really just a very quick render with flip
[46:21] books so flip book with new settings this is fine let's uh constraint it for five seconds and let
[46:29] do in here not resolution just this and let's do start and this will render to when play it should
[46:36] pop up anytime and when it's done I will be back okay guys this is our final result again not
[46:45] perfect result because we got some balls stuck in here we should have played a bit more with
[46:49] that simulation but anyways this was just the poor man guides to the VFX integration in Odini,
[46:57] Nuke and also using the Fincher result now you would render this properly let's say in 4k and
[47:05] composite it back to our linear footage with the proper Aces workflow if you want to go to the
[47:11] trouble do that and recreate a better version of this and upload it so I can see it share it with me
[47:18] and I would love to see your results again if this was useful to you let me know in the comments
[47:24] I hope you you have enjoyed this video and as always if you want to support my work make sure you go
[47:30] to my Patreon and subscribe to my Patreon where you can find all the projects files from this video
[47:35] and all the other videos on my channel alongside with exclusive tutorials hours and hours of
[47:41] exclusive tutorials on Odini and yeah other than that thank you for watching and I guess I'll see
[47:46] you next time thank you.



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
