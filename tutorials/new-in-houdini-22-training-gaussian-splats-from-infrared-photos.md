---
title: New in Houdini 22: Training Gaussian Splats from Infrared Photos
source: YouTube
url: https://www.youtube.com/watch?v=yGCjD0_TIpw
author: Entagma
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/new-in-houdini-22-training-gaussian-splats-from-infrared-photos/
frame_count: 0
frame_status: pending-selection
---

# New in Houdini 22: Training Gaussian Splats from Infrared Photos

**Source:** [YouTube](https://www.youtube.com/watch?v=yGCjD0_TIpw)
**Author:** Entagma
**Duration:** 16m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py new-in-houdini-22-training-gaussian-splats-from-infrared-photos <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] We have a new Houdini version and unfortunately this time the release fell right into the most
[0:06] stressful time of the year for us when we're wrapping up the summer semester at the university
[0:11] where we're teaching at, so just as a heads up we won't be able to publish as many videos
[0:17] as quickly as we did in previous years, but we'll make a way through this release.
[0:22] And as a kickstart I just want to cover the feature that I'm most excited about creating
[0:27] Gaussian splats in Houdini and I will walk you through this as quickly as possible.
[0:32] There will be a more in depth video later for this one, let's get going.
[0:36] Oh and by the way, support us on Patreon, it's the only reason we can make videos like
[0:40] this.
[0:41] Let's talk about the general workflow.
[0:42] First of all we need to get images.
[0:44] These images that you see right here in the background and I took these at my local botanical
[0:48] garden and to make it a bit more special I took these with a camera that I modded to
[0:53] Infrared.
[0:54] So we get this nice really red, really bright red vegetation right here.
[0:59] Once we have our images we're going to use not Houdini but another program called Callmap
[1:05] to calculate the cam positions when we took all those images and also a sparse point cloud
[1:10] that will be the base of our Gaussian splat.
[1:12] This is something that Houdini can't do yet, however Callmap is free and open source and
[1:17] can do this for us.
[1:19] Then we move into Houdini and train our Gaussian splat and finally we can use the tools that
[1:24] are already there since the last release to edit and render a Gaussian splat in the end.
[1:29] Now getting good images for Gaussian splats requires some rules.
[1:33] Andre Leprov has already done a brilliant video on this which I will just link in the
[1:37] description, but to just quickly summarize the most important points.
[1:41] First of all choose a camera or a lens that has no fisheye or that's not overly wide
[1:47] angle.
[1:48] Also move your camera between shots because we need parallax inner images.
[1:53] It's not enough to just rotate the camera, you have to move it.
[1:56] Also you should know your exposure triangle, so your shutter speed should be fast enough
[2:01] so you can get sharp images.
[2:03] The aperture should have a fairly low depth of field and also give you sharp images.
[2:08] Typically with lenses you get the sharpest images around f8 or at the middle of your
[2:13] aperture ring and the ISO should be high enough to cover for those other two because they
[2:19] won't let much light into your camera.
[2:22] At least in my experience it was fine setting the ISO to auto if you're in a pinch and
[2:27] you want to get stuff done quickly.
[2:30] Also if you want less work relighting your scans, choosing for example a cloudy day to
[2:34] get flat lighting is always good and also capturing fewer good images is better than
[2:41] capturing a ton of bad images.
[2:43] In my experience capturing around 200 images is sort of the minimum for a 360 degree view.
[2:50] The scene that we're processing today has only 180 degrees so we're going to use 100
[2:56] images for that.
[2:57] If you live by all those rules you finally have a set of good images that you can run
[3:02] through the software and let's talk about that software next.
[3:05] So again as I said this is not Hedini yet, this is call map and if you're on windows
[3:11] you can just head on over to the releases.
[3:14] Scroll down here and if you have a Nvidia GPU you can download the CUDA version, if you
[3:19] don't then you have to live with the CPU version and in both cases you can just download
[3:24] the zip, unzip it and run the callmap.bed as administrator and you should be good to
[3:30] go.
[3:31] If you're on Linux like me you can check for other Linux releases right here or if like
[3:37] me they're not in this list right here, I had good results using the Docker image to
[3:44] run this program.
[3:45] But once you do so you should have a very beautiful new window like this along with
[3:50] a little console window in here that you can use to just get a quick check that the program
[3:56] is actually doing stuff.
[3:57] And now let's actually use this program to process images.
[4:00] For this we're going to create a new project, so file new project.
[4:04] For this we'll first of all need to create a database, so hit the new button in here
[4:08] and in our folder structure let's just create a new folder in here, call it db, jump inside
[4:14] and let's maybe call it dbv01 and save it and we also need to select our image path,
[4:20] so let's click select here, let's move up one folder and I have my images in this images
[4:24] folder in here, so let's just select this and hit select and hit save.
[4:29] Nothing in here will change, the thing that we need to do now is go to processing and
[4:33] go to feature extraction.
[4:35] This window here will come up and in here the only thing that we have to set is the
[4:40] writing method and I used opencv and you want to click share it for all images in here.
[4:45] You can maybe tweak the other stuff but I generally found that this works fine, so we
[4:49] can hit extract.
[4:50] You get this really nondescript window right here and you will get more info right here
[4:56] in the console.
[4:57] And if you see the ellipse time down here you know that it's done and we can close this
[5:01] window right now.
[5:02] So first step done, we can move on to the next step, this will be the feature matching,
[5:07] it's like this.
[5:08] And in here we mainly want to make sure that we select exhaustive in here, you would use
[5:13] sequential if you grabbed your frames from a video clip, this is not the case for my
[5:18] dataset so let's use exhaustive and let's hit run again.
[5:22] Again very nondescript window, let's take a look at the console and again once you see
[5:26] ellipse time in here you know that this is done.
[5:29] So let's move this window out of the way, let's close this window down.
[5:32] Then we can move on to the last step, the reconstruction step.
[5:36] And in here we just want to say start reconstruction.
[5:40] And as soon as we do so you should see some cameras appearing and also some dots of this
[5:45] barris point cloud.
[5:46] This will be by far the longest step so let's let this run and let this finish.
[5:58] And again once you see the ellipse time down here and you see a lot of cameras and points
[6:03] in your scene here, you know that this part is done and we can finally export our model.
[6:09] So for this let's go to file, export model and now let's create a new folder, let's call
[6:13] it sparse, let's go in here and let's choose the folder.
[6:18] And now in your call map directory that you open up you should have this sparse folder
[6:23] in here and these files in here.
[6:25] And as soon as you see this you know that you're good to go to move on to Houdini.
[6:29] So let's do that next.
[6:31] So now in an empty Houdini scene let's actually build or train our Gaussian splat.
[6:36] I've rearranged by a few in here because we're going to do a ton of parameter diving so our
[6:41] parameter window in here should be nice and big.
[6:44] Also this won't happen in the obj context yet this will happen in the task context.
[6:49] Let's switch into here and also make sure that you already saved your scene because
[6:54] Houdini is going to generate a ton of folders in reference to the location of the zip file.
[7:00] So again just save it in your project folder and you're good to go.
[7:03] Now in the task context we're going to create a top network, we're going to dive inside
[7:08] and we're going to search for gsplat.
[7:10] There are two options in here.
[7:12] The first one is just for creating gsplats from rendered images.
[7:16] We want to use the ml train gsplat option down here.
[7:20] And now we're going to do our parameter diving and the first step in here the data tab is
[7:24] going to tell you the data structure that you need for your data from call map to be
[7:29] read in by Houdini correctly.
[7:32] Adding Chris here before I spend ages making sense of all these parameters in here and
[7:37] derive the folder structure from them.
[7:39] I think it's just easier to just show you the folder structure.
[7:42] So this is your Houdini project folder, at least it's mine.
[7:46] There are my two Houdini files, the one that I use for building the setup and the one that
[7:50] I'm building right now.
[7:51] We can ignore the render, export and backup folder in here and this is not important.
[7:56] For now we're just going to create a folder called ml.
[7:59] In that folder we're going to create another folder with the exact same name as a hipfile.
[8:04] So train gsplats underscore rack for me.
[8:06] This folder up here is again the previous hipfile that I used for building the setup
[8:11] and down here is another folder that the top node will create for us where all the python
[8:17] code lives and all the python libraries to actually train our Gaussian splat.
[8:21] You don't have to worry about that.
[8:22] Tops will do that for you and inside that folder we have another folder that tops will
[8:27] create for us later.
[8:28] This ml training splats 1.run.
[8:31] This is where the results will have.
[8:33] What you will need to create is a folder called data set dot gsplats and in here you're going
[8:39] to create a folder called images where you put all your images in.
[8:43] Again don't worry about the images underscore 3 folder tops will generate that for you and
[8:49] for the data from callmaps you're going to create a folder called sparse and there put
[8:54] a folder called zero and in here put all the data that you got from callmap and this is
[8:58] everything you need to do to get going and training in here.
[9:03] Again I won't go into much details about this whole thing up here.
[9:08] Again this should be as quick as possible.
[9:10] So the main things that I'm going to change in here is I'm going to change my data set
[9:15] from houdini xr's to sfm from callmap.
[9:18] Then I want to go to execution and check the most important checkbox of the whole thing
[9:26] which is cache images to vram.
[9:29] This will make your simulation or your training a whole lot faster.
[9:33] We're talking about training that is done in minutes versus training that is done in
[9:38] hours if this is not checked and also set the number of workers to equal to CPU count
[9:45] less one which will use all the threads on your GPU less one which makes sense for this.
[9:51] Also if you want to make this even more faster what we can also do is go to training and disable
[9:58] testing this will just take every eighth image and compare it to our gaussian's plate and
[10:04] check how good our gaussian's plate resembles our image but again this takes at least a bit
[10:10] of time and I'm in a rush so let's disable that as well.
[10:14] And let's go back to our data in here and the very last and also very important parameter
[10:21] in here is the data downscale factor because we're moving all our data to our vram and
[10:27] we have a limited amount of this.
[10:30] In my case I have 24 gigabytes and the images currently have a width of 6000 pixels and
[10:38] I found for this picture size and the amount of VRAM that I have I need to use a downscale
[10:44] factor of three.
[10:46] If you don't set this Houdini will pretty quickly crash and you just have to restart
[10:51] it increase the number of bit further until it fits all in your VRAM and then you can
[10:57] start training.
[10:58] And then since this is a top node to finally start training we can right click and select
[11:04] cook node in here.
[11:05] Well this node will do a bunch of stuff and a lot of those stuff will take a long time
[11:12] so if you don't want to stare at this beach ball right here going round and round and
[11:16] round and just wonder if it's actually doing stuff the main thing that you want to check
[11:21] out is this icon up here and that brings up all the sub processes within that node so
[11:28] we can check out what's currently doing what.
[11:30] For me most of this is already running and we can take a look at the training run right
[11:36] here the one that is actually currently running and if you want to have more detail in here
[11:41] we can again right click that process and select work item info and we're going to get
[11:46] this little info window down here and in here we actually see what the node is doing or
[11:52] if it actually is doing stuff.
[11:54] Let's wait a bit for this.
[11:56] Yeah it'll soon pop up this and this is something that's quite helpful for us because this will
[12:01] also launch another window where we can actually take a look at the training process while
[12:07] it's happening.
[12:08] To do so in Houdini we can go to monitoring and click open viewer and this will open a
[12:13] browser window where we can see first of all for how many steps we're training.
[12:18] The default is 30,000 steps so this will count up to 30,000 in the end and we can also see
[12:25] our Gaussian splat scene and navigate around it.
[12:28] Now training this on my 4090 took around 12 minutes give or take for now I'm just going
[12:33] to select stop and save and it already saved my Gaussian splat so we can close this down.
[12:40] The node in here should say that it's finished cooking which it does and if we go back to
[12:45] our folder structure and go back in the folder that has the same name as our hip file we
[12:51] should have this run folder in here and in here we should have a folder called gsplats
[12:55] and in here we should have a .ply file and this is our Gaussian splat.
[13:00] So we're now done with our training step and the last thing that we need to do is first
[13:05] of all bring it into Houdini proper and then also render it.
[13:08] So let's do that next and last.
[13:10] So we're done with the tops workflow and let's go back into the obj context.
[13:15] Let's drop down a geonode.
[13:17] Let's dive inside.
[13:18] Let's drop down a file node.
[13:20] Let's again look for our Gaussian splat.
[13:23] So in L I'm going to use the splat that I created earlier so I'm going to move into
[13:27] that folder into the run folder into gsplats and select this one right here.
[13:33] Hit accept.
[13:34] This will first of all import just as a point cloud to turn it into a Gaussian splat.
[13:40] We need to search for a gsplat and use the big gsplat node like we did last year.
[13:46] Now this should already display as a Gaussian splat.
[13:50] Typically the orientation isn't correct at the first try so let's drop down a transform
[13:55] node and after a bit of wrangling with the transform node we have something that looks
[13:59] quite nice.
[14:00] So this is the area that I mainly focus on while doing my Gaussian splat or creating
[14:06] my images and yet this area looks pretty darn good.
[14:09] Of course other areas that don't have as many images will fall apart and also since this
[14:15] is just a point cloud in the end if you have one area that annoys you or that gets in the
[14:21] way you can just drop down a blast node.
[14:25] Go to the group selections like points.
[14:28] I like to use the lasso select and maybe select an area like this that's annoying and hit
[14:35] enter and it's gone.
[14:37] So you can clean your Gaussian splat up like this and once you're happy you can move on
[14:41] to camera by dropping down a null.
[14:44] Let's call it out and let's move on to the stage context.
[14:48] In the stage context all we basically need is a sub-import node.
[14:52] We're going to select our odd null and let's pick a camera angle.
[14:56] Maybe this one.
[14:57] Let's create a camera.
[14:58] We won't need any lights as long as we just have our Gaussian splat in our scene right
[15:03] here and we also don't need any materials so let's move right on to the Karma setup.
[15:08] Let's wire this down below and on the Karma setup of course we want to render with our GPU.
[15:15] You can go pretty low on the path trace samples maybe 32.
[15:19] The only noise where you need more samples is if you have motion blur or out of focus
[15:25] regions otherwise you can pretty much go as low as you want.
[15:29] And one other little trick that I learned in a side effects forum entry is to go to
[15:34] advance and to set the pixel oracle from variance to uniform and this also speeds up rendering
[15:42] roughly by a factor of 2 while also generating images that look a bit nicer.
[15:49] And this is basically all that you need to keep in mind so we can go down to the dust
[15:53] render and we can render this to mplay and we should get a good result in the end.
[15:58] After a very short render time we have something that looks like the photos that we took and
[16:04] of course we can add movement and depth of field and motion blur and everything that
[16:09] we need to make this look more beautiful in the end.
[16:13] So this is the really really quick way to get from a bunch of photos to a Gorschen's
[16:18] Blatt with Houdini 22.
[16:20] Again a quick video to get us started, the next one will come when it's ready and until
[16:26] next time it's cheers and goodbye.
[16:29] And to everyone supporting us on Patreon thanks guys, you're the ones keeping the lights
[16:33] on here and making videos like this possible.
[16:36] Thank you.



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
