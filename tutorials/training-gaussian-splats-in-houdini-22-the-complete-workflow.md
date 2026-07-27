---
title: Training Gaussian Splats in Houdini 22 – The Complete Workflow
source: YouTube
url: https://www.youtube.com/watch?v=vP609ccWOKo
author: Nodeconnector
ingested: 2026-07-27
houdini_version: "22"
tags: [gaussian-splats, photogrammetry, colmap, top, pdg, solaris, usd, karma, rendering, procedural, houdini-22, advanced]
extraction_status: complete
frames_dir: tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Training Gaussian Splats in Houdini 22 – The Complete Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=vP609ccWOKo)
**Author:** Nodeconnector
**Duration:** 22m55s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Houdini 22 is finally out and one of the features that I'm really excited about is that we can now train Gaussian splats directly inside Houdini.
[0:09] And that's exactly what I want to show you today.
[0:18] Today we will create this little guy here.
[0:20] And that's probably the most horrible object to 3D scan and it was nearly impossible to create something like this before Gaussian splats appeared.
[0:31] This is a toy that my son actually created. He handcrafted it and when I saw it I immediately thought I have to try to scan this because it is so complicated with all the hair and all the details.
[0:46] But I think that it turned out quite nice although I didn't have the best capture footage. So let's take a look at this process.


### Scanning with iPhone [0:54]
**Transcript (timestamped):**
[0:54] The first step of creating a Gaussian splat is always the capture footage and in my case I just used a video capture.
[1:01] I just used my iPhone camera and walked around this object in circles a few times from different angles.
[1:09] And yeah, this is actually what you can see here. Now this is by far not perfect of course.
[1:15] The lighting is not as flat as I would have liked. The depth of field is not perfect because there's a lot of blurriness happening.
[1:23] Then I'm not moving in a constant speed that creates a bit of an irregular pattern in the capture frames.
[1:31] But I really made this very quickly, you know, just quickly capture something and then use that to train the splat.
[1:38] And for this quick process and for this really accessible equipment I think the result was pretty good.
[1:46] But I did not use this whole data. I did not use the video as it is. But I wanted to extract some images from this.


### Extracting the Image Sequence [1:55]
**Transcript (timestamped):**
[1:55] To extract the images I just used the cop network and loaded in this video file.
[2:01] And then in a render rob here I can specify an increment as you can see.
[2:07] So I chose all the frames of this video. These are 6,647.
[2:13] And then I rendered out actually every 30th frame.
[2:18] So I didn't take the 20 increment I used 30 because I didn't want to use a lot of images for the sake of this tutorial.
[2:27] The more images you have the better. But of course the longer the process will take.
[2:32] My goal was to get around 200 images. And the resolution of this video capture is actually 4k.
[2:40] So it is 3840 times 2160. And I also want to keep this resolution for my images.


### Preparing Data in COLMAP [2:50]
**Transcript (timestamped):**
[2:50] Here you can see the sequence. So this is every 30th frame of my sequence.
[2:57] And because I did not move quite smoothly around it and I sped up and slowed down the coverage is probably also not perfect.
[3:05] But the process is at least quite fast.
[3:09] And now we have to align this training data.
[3:13] And unfortunately this is a step that we cannot do yet directly in Houdini.
[3:18] So therefore we need an extra software.
[3:21] So the first option that I tested was RealityScan from Epic. It's actually free and it worked quite nice.
[3:27] The second option that I tested is called Callmap.
[3:31] And was specially designed to create the data that we need.
[3:34] And I actually preferred the workflow in Callmap. So I will use this.
[3:39] You can find Callmap on GitHub. And I will also put a link in the video description.
[3:44] And here you can find the release and you can just take the latest release that is available for your system.
[3:50] In my case I am on Windows with CUDA. So I downloaded this one here.
[3:55] When you open up Callmap you will see this empty wide scene here.
[3:59] And we first of all have to create a new project. So let's do that. Let's click on new and project.
[4:04] First you want to specify a database and we want to create a new one.
[4:08] I will do this in my tutorial folder.
[4:11] I will just create it here under the database and here I already created one.
[4:15] So I will just create a second one here. So let's do this here. Database 2.
[4:20] And then I want to select my images.
[4:23] So here I have my footage. And that's it.
[4:28] Now we can hit save.
[4:30] And the first step of the process is that you go to processing and then you save feature extraction.
[4:36] The only setting that we have to change here is the camera model.
[4:40] And in most cases you want to use this open CV here.
[4:44] And then we can just click extract. And now it will start to extract data from our images.
[4:51] And whenever you see this elapsed time down here in this console then you know that the process is finished and we can just close this.
[4:59] The next step of processing is feature matching. So let's just activate this.
[5:04] And here we do not have to change anything. We can just stay here in exhaustive and just run this.
[5:12] Exhaustive is the best option when you have a quite small set of images like objects can like we have it with around 500 images.
[5:22] If you have more than 1000 images this method can get pretty slow.
[5:26] The sequential one is very good if you have for example drone flight or something bigger walkthrough where you have more data to process.
[5:37] So it really depends what kind of footage you have. In my case the exhaustive is the best guess.
[5:44] Now this process is also finished and I can move to the next step which is the reconstruction.
[5:50] And now we just can start this reconstruction here.
[5:54] The capture is finished and as you see my coverage is not perfect. I should have really take another turn up here with a bit of a higher position
[6:03] and tilting down so that I get more information of the top of the object.
[6:08] And the same applies for the bottom part here. I didn't really go very low here.
[6:13] But yeah at least I have a few images from down here.
[6:16] And now we want to export all of this data to import it then in the next step into Houdini.
[6:22] So let's go to file and let's go to export model.
[6:26] And in this case I will just create a new folder here and say that this is my Column App Export.
[6:35] Okay and I will just put everything inside this folder.
[6:39] If we take a look at the folder you see that we have the camera spin, the frame spin, images spin, then we have points 3D spin
[6:46] and then we have the project in here that we do not need in Houdini.
[6:50] And I think that this rigs is also not required but these up here are really important.
[6:56] And now we can jump into Houdini and start our training there.


### Training the Splat in TOPs (ML Gaussian Train) [6:59]
**Transcript (timestamped):**
[7:00] Before I do anything I just want to save my empty scene here because it is important that we create a folder structure, a special one.
[7:08] So let's go to tutorials and to my Gaussian Split Training and I will just create a new folder now.
[7:15] So we will say tutorial recording.
[7:19] This will be my main folder and here I want to save the Split Training.
[7:26] And I do this because now I have a $HIP variable specified which we need in the next step.
[7:31] Now we want to create a top network and instead of creating this in the object context you could also go to the tasks here but it works like that too.
[7:40] And dive inside this and here we want to add in our cheeseblad trainer and this is this note here, ML train cheeseblads.
[7:48] So let's add this in. Let's open up the parameters and let's take a look.
[7:53] The most important aspect here really is the folder structure.
[7:57] This process requires a specific folder structure and you actually can see it here but it's a bit difficult to figure out.
[8:05] So the first thing that we see is we need a base directory that is in our $HIP path.
[8:11] So this is wherever you saved your HIP file and then we need a folder that's called ML.
[8:17] So let's do that. Let's create this. Let's go to my folder that I actually created here in tutorial rack.
[8:23] So here is my scene file, my HIP LC, that's my $HIP path and here I want to create this new folder that's called ML.
[8:32] Now you see we need a dataset folder and this dataset folder should be the base directory which is actually this one here
[8:41] and then the base name and the base name is actually $HIP.
[8:45] So now inside the ML folder we want to create another folder and we want to name it exactly as our HIP file is called.
[8:54] And I called this, I can take a look up here, split underscore training underscore v01.
[9:06] So that's important that you use exactly the same name here.
[9:10] Now inside this folder here that we just created we need another folder and that is called the dataset cheeseplats.
[9:18] So let's go in here and create another folder and call it dataset.cheesplats.
[9:28] And in this one we need two more folders. The first one is an image folder.
[9:33] So let's create a new folder that's called images just like that.
[9:38] And the other one is called sparse.
[9:42] And inside the sparse folder we need another folder and that is called zero.
[9:48] So you really have to create exactly this folder structure to make this work.
[9:54] So let's recap this. You want to start in your $HIP path wherever this is where you saved your HIP file.
[10:01] Then you create an ML folder in this.
[10:04] You create a folder that has exactly the same name as your project file but without the .HIP, LC or whatever version you have.
[10:12] Inside this you want to have the dataset cheeseplats.
[10:15] Inside the cheeseplats you want to have the images and the sparse.
[10:19] And inside sparse you need a folder that has zero.
[10:22] And then you are set.
[10:23] Now we have to copy our data that we created in call map into this folder structure.
[10:29] So let's go out of here again and let's go to my data that I created.
[10:35] And I actually saved this in here.
[10:38] So I will just copy this over for now.
[10:41] I will copy this whole folder and I will go to my project file that I have here.
[10:47] It's not important that you copy it in here.
[10:50] This was just a step to organize my project a bit better.
[10:53] Now I come in here and I select all the bins.
[10:56] As I said, I don't need this project file here and I copy these.
[11:00] And now we want to make sure that we go to the sparse and to the zero folder and paste in everything in here that call map exported.
[11:09] Now the only thing that we have to do is to copy our footage.
[11:12] So let's come in here and let's copy our PNG sequence that I created in Copernicus.
[11:19] And I want to copy this also inside my dataset here into the images folder.
[11:26] And if you did everything right, then this process should now work.
[11:34] But before we start this, we have to set up some settings.
[11:38] One important setting is the dataset type.
[11:40] We are not using Houdini EXRs.
[11:43] There is also the option to train directly from Houdini renders, but we are actually using a call map data.
[11:49] The next setting that is important is this downscale factor here.
[11:54] Downscaling means resizing your source images.
[11:58] In my case, my source images have 4K resolution.
[12:03] And of course, the bigger your images are, the slower the process will be.
[12:08] So you can downscale this here.
[12:10] And if I choose a downscale factor of two, then it will actually take half of the resolution of my images.
[12:16] But this also requires an extra step in the process because it will really re-render all of your images.
[12:23] It will just scale it down and save it into a separate folder.
[12:27] But it is faster, so I will do it now.
[12:30] The quality is of course a little bit worse.
[12:33] But for the sake of this tutorial, I will just leave it at two.
[12:36] Then we are going to the training tab.
[12:38] And in the training tab, we can take a look here.
[12:40] The most important thing is I don't want testing.
[12:44] So testing will just save out a frame every, in this case, every eight frames.
[12:52] And it just takes a lot of time rendering and saving this.
[12:55] It also generates a lot of data.
[12:56] So in my case, I don't want to do that.
[12:58] So I will just disable it.
[13:00] Then you have the total steps.
[13:01] That is very important, of course.
[13:03] So maybe you can get away with lower steps, something like 25,000, maybe even 20,000.
[13:10] If you just want a very quick test, you could even go lower, but then you cannot expect a good result.
[13:16] But if you go very high, then sometimes it will not really help.
[13:20] The good thing is that you can stop the process at any time and save the splat as it is at that moment.
[13:27] I will leave this on 30,000 for now.
[13:30] And what I want to do is change the max batch here.
[13:34] So this is the number of images that are processed per training step.
[13:39] And you see that it says larger batches produce smoother gradients, but they use more GPU memory.
[13:45] I'm training on an RTX 4090 with 24 gigabytes of RAM.
[13:50] And when I increase this to a batch size of six with these settings, I have no problem with my V-RAM.
[13:58] Now monitoring is not that important now.
[14:01] It will be important later on.
[14:03] And the checkpoints, you have the option to export a PLY, which is actually the splat format in a certain interval.
[14:12] So now it is set to 10,000.
[14:14] That means after 10,000 steps, it will save out one PLY.
[14:18] After 20,000 steps, it will save out another one.
[14:22] And then of course, in the end, it will save out the final one anyway.
[14:25] So if you want to have in between PLYs, maybe for further training or for some other purposes, you can set this up here.
[14:32] And you can also export a USD version of this directly in here by activating this.
[14:38] But I will keep this interval here at 10,000. That's fine.
[14:41] Then under execution, this is also very important.
[14:45] Here we have the cache images to V-RAM.
[14:48] And that's probably the most important setting of this whole process, because this can really speed up your training tremendously.
[14:55] And we're really talking here a difference of a few hours to a few minutes.
[15:00] So I will activate this.
[15:02] And then you also have the number of workers.
[15:05] And usually it is only a quarter to the total CPU count.
[15:10] But you can of course increase this.
[15:12] In my case, I like to use the equal to CPU count less one than it uses the full resource except one of the CPU kernels.
[15:22] And yeah, that's basically it.
[15:25] If you have multiple GPUs, you could specify a certain GPU.
[15:30] I have multiple ones, but in my case, it runs on the 1490 only anyway.
[15:35] So this is done.
[15:37] And now we can start the training process and you can start the training process by right clicking and then say cook node.
[15:44] And this will start the training progress.
[15:48] Now, if you want to check out what is actually really happening, then you can click on this icon up here and open up the task graph table.
[15:57] And you see that in my case, it is actually finished with the first tasks.
[16:02] If you run this the first time, then this will take a bit longer because it will download a lot of Python libraries and install a lot of stuff.
[16:11] I don't know exactly what, but this takes a while.
[16:14] And then it starts training.
[16:16] And if you want to have a bit more information of one of these processes, then you can right click and say work item info.
[16:23] And this will open up this info panel here.
[16:27] And down here we have this console like information where we can see what it is now doing.
[16:34] So right now it is already preloading the training images.
[16:39] And the thing is that if you start this for the first time, then it will also convert your images to the smaller resolution version.
[16:48] So this takes a while.
[16:50] I already run this once, so I do not have to do that now.
[16:54] And you see that it is already on step 1300.
[16:58] It is already solving our splat.
[17:00] Now, if you want to watch this, you can actually do so.
[17:03] You can go to the monitoring and just open the viewer, but be aware that this only works when this process is already running.
[17:13] So when you see the step here, then you can watch the viewer.
[17:17] This will open in the browser actually.
[17:20] And now you can really watch the splat generation live here.
[17:26] So as you can see here, it's unfortunately it's not oriented correctly, but you can see the details that I get.
[17:34] And you can also see the number of steps here.
[17:40] So that's actually pretty cool.
[17:45] Now, such a solve requires about 12 to 15 minutes on my system with these settings, with this number of frames.
[17:53] Of course, if you have a higher resolution, more frames than this may take way longer.
[17:58] I will not run this through now because I want to save a little bit of time and I already did that.
[18:03] So we will take a look at the result right away.


### Importing & Bakesplat [18:06]
**Transcript (timestamped):**
[18:06] Okay, so I just reset my notes so that it keeps not training.
[18:10] And now I want to show you the result.
[18:13] So let's go to my geometry here.
[18:16] And you just use a file node and then you can load in your splat.
[18:21] And the splat will be in ML in the splat training version one.
[18:26] And then Houdini created this ML training splat one.
[18:30] And in the cheese splats folder, you will find the final cheese splat.
[18:34] It is always this dot ply file here.
[18:38] And that is the cheese splat.
[18:40] So you see here a bunch of points all over the place.
[18:45] And yeah, for a little scan of this small object here in the middle, this is actually quite a big, quite a lot of data that I do not need.
[18:53] So after importing the splat, you also want to bake it.
[18:57] And there is this bake cheese splat node in Houdini.
[19:00] So you can just get to that like this, just type in bake, then you get to the bake cheese splats and you just block this in.
[19:07] And this is actually baking or reading all the data of our cheese splats.
[19:12] If we take a look what these cheese splats actually are, these are actually only points with certain attributes.
[19:18] And we can of course take a look at these attributes.
[19:21] So we have a position attribute for all of these.
[19:24] As you can see, we have a color attribute for all of these, an alpha attribute and an orient attribute.
[19:31] And last but not least, a scale attribute.
[19:33] So all a splat is, is actually really like a disc in space that is orientated in a certain way that has a certain length and that has a certain color and an opacity.
[19:45] So and if we take a look at this, we can clearly see that this is exactly what we are seeing here.
[19:50] So a really big mess.


### Cleaning Up the Splat [19:52]
**Transcript (timestamped):**
[19:52] And I have to clean this up, of course, a little bit.
[19:56] So first of all, I want to transform it so that it is orientated the right way.
[20:01] And then I will just create a group.
[20:03] And in this case, I will just create a group using a bounding box.
[20:09] So if you take a look at this, I just selected the inner points here.
[20:14] The group of course has to run over points because we are working with points.
[20:17] And I just wanted to select the points that are important for my object.
[20:22] And with a blast, I'm just blasting away everything else.
[20:25] And that's actually the result that I have now.
[20:28] And you see for this very short amount of time from the capture to the training,
[20:34] all of this lasted about one and a half hours.
[20:38] This is actually a pretty cool result.
[20:41] Of course, we can now keep working on this.
[20:44] We can clean it up and make it way nicer.
[20:47] But I think that it will go over this process in another separate video tutorial.


### Solaris + Karma Render [20:51]
**Transcript (timestamped):**
[20:52] So what you can do now with this splat is you can either put in here a null and directly send it
[20:57] to Solaris and render it like that.
[21:00] So we can say here out of a virtual.
[21:03] That's actually the name that my son gave this little animal here.
[21:07] And I could now go to karma.
[21:09] So let's do that.
[21:10] Let's go to Solaris quickly and bring in our object into Solaris.
[21:14] You can do this either by using a sub import.
[21:19] Or you could also just export this as a USD file.
[21:23] That's also possible.
[21:24] But for now, I will just use this like that.
[21:27] And you see that this directly translates into Solaris and it will also directly render with karma XPU.
[21:35] And it actually also renders quite fast, as you can see here.
[21:40] So that's how you can use these.
[21:42] The only downside of these Gaussian splits is that you cannot relight them.
[21:46] So if I put in now an area light and activate this and you see this has no influence
[21:53] at all on my object because these are of course only points with some variables and some attributes on it.
[22:01] So there are ways how to relight splits.
[22:04] I don't know whether these techniques will work on this one here with this wild hair,
[22:08] but I will definitely keep working on this and I will keep trying it out.


### Outro [22:12]
**Transcript (timestamped):**
[22:12] I will definitely prepare another video tutorial where I show you how we can even clean this up further
[22:17] and make this a bit nicer.
[22:19] And if you want to grab the project file from this session also with the Gaussian split included,
[22:25] then please check out the links in the video description.
[22:28] So that's it for now.
[22:29] Thank you very much for watching and I hope to see you next time.
[22:32] Goodbye.
[22:49] Bye.



---

## Captured Frames

- [2:01] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_000.jpg
- [4:40] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_001.jpg
- [7:40] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_002.jpg
- [12:10] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_003.jpg
- [13:39] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_004.jpg
- [17:17] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_005.jpg
- [19:24] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_006.jpg
- [21:14] tutorials/frames/training-gaussian-splats-in-houdini-22-the-complete-workflow/frame_007.jpg

---

## Structured Notes

### Core Technique
End-to-end 3D Gaussian Splat reconstruction from a real-world object using Houdini 22's native PDG/TOPs training pipeline (`ML Train Gsplats`), fed by COLMAP-aligned photogrammetry data rather than Houdini-rendered cameras.

### Summary
The author scans a handmade toy with an iPhone video, extracts a still-image sequence in Copernicus, aligns the images externally in COLMAP (chosen over Epic's RealityScan), then trains a Gaussian splat directly inside a Houdini 22 TOP network using the `ML Train Gsplats` node against that COLMAP dataset. After training, the resulting `.ply` splat is imported, baked with `Bake Gsplats`, cleaned up (transform + bounding-box group + blast), and finally piped into Solaris for a Karma XPU render — with a callout that splats can't be relit by scene lights since they only carry baked color/alpha, not shading response.

### Key Steps
1. **Capture:** walk around the object in circles with an iPhone video (irregular speed/lighting is tolerated).
2. **Extract stills (Copernicus):** load the video in a COP network `File` node, feed a `ROP Image Output` node, and render every Nth frame (author used every 30th of 6,647 frames → ~200 images) at full native 4K resolution.
3. **Align in COLMAP** (not RealityScan, though that also works): New Project → new database → select the image folder → **Feature Extraction** with Camera Model set to `OPENCV` → **Feature Matching** in `Exhaustive` mode (best for small ~200-500 image object sets; use `Sequential` for drone/walkthrough footage with far more frames) → **Reconstruction** → **Export model**, producing `cameras`, `images`, `points3D` bin files (the `.rig` file and project file are not needed).
4. **Build the required disk folder structure** under `$HIP`: `$HIP/ML/<hipfile-name-no-extension>/dataset.gsplats/{images/, sparse/0/}`. Copy the COP-rendered PNG sequence into `images/`, and the COLMAP-exported bin files into `sparse/0/`. The subfolder name under `ML/` must exactly match the `.hip` filename.
5. **Train in a TOP network** (object level or inside a `tasks` context): add an **`ML Train Gsplats`** node (`ml_traingsplats1`). Key parameters:
   - *Directory Structure* — Base Directory = `$HIP`, Base Name = `$HIPNAME` (must match folder from step 4).
   - *Import Data Source* — Dataset Path/Name pointing at `dataset.gsplats`; Data Set Type = **COLMAP** (not "Houdini EXRs" — that's the alternative path for training directly off Karma renders); Data Downscale Factor = 2 for a 4K source (halves resolution, re-renders a downscaled image copy, trades quality for speed).
   - *Training tab* — disable **Enable Testing** (saves a validation render every N steps; costly, skip for a quick result); Total Steps = 30,000 (usable results from ~20-25k; lower for quick tests); Max Batch Size raised to 6 on a 24GB RTX 4090 (larger batch = smoother gradients, more VRAM); Checkpoint export interval left at 10,000 steps (also has an **Export USD** toggle for direct USD output).
   - *Execution tab* — enable **Cache Images to VRAM** (biggest single speed lever — turns a multi-hour train into minutes); Number of Workers set to CPU-count-minus-one.
   - Right-click the node → **Cook Node** to start training; monitor via the Task Graph Table → work-item → **Work Item Info** console log, or **Monitoring → open viewer** (launches a live browser-based splat preview once a step has completed). ~12-15 min training time for this dataset/settings on an RTX 4090.
6. **Import & bake:** `File` SOP pointed at the trained `.ply` inside `ML/<name>/gsplats/`, feeding a **`Bake Gsplats`** SOP. A raw Gaussian splat is just points carrying `P` (position), `Cd` (color), alpha, `orient`, and `scale` attributes — each point renders as an oriented, colored, semi-transparent disc.
7. **Clean up:** `Transform` (correct up-axis orientation) → `Group` (bounding-box group over points, isolating the object of interest from background scan noise) → `Blast` (delete ungrouped points).
8. **Render:** feed the cleaned splat geometry into Solaris (via SOP Import, or alternatively export as USD), then render with **Karma XPU**. Gotcha: splats **cannot be relit** — adding a scene light has zero visible effect, since a splat's color/alpha is baked data, not a shaded response to lighting.

### Houdini Nodes / VEX / Settings
- COP: `File` (video source), `ROP Image Output` (image-sequence render with frame increment).
- TOP: `ML Train Gsplats` (`ml_traingsplats1`) — Directory Structure / Import Data Source / Training / Optimization / Execution / Monitoring / Checkpoints tabs; Data Set Type = COLMAP; Cache Images to VRAM.
- SOP: `File` (load trained `.ply`), `Bake Gsplats`, `Transform`, `Group` (bounding box, point-based), `Blast`.
- LOP/Solaris: SOP-to-LOP style import of the cleaned splat geometry, rendered with **Karma XPU**.
- External tools (not Houdini): iPhone video capture, COLMAP (camera model `OPENCV`, Exhaustive matching) — RealityScan mentioned as a free alternative.

### Difficulty
Advanced (requires an external photogrammetry-alignment tool, exact manual folder-structure creation, and GPU training tuning — but no scripting).

### Houdini Version
22 (uses the new-in-H22 native Gaussian Splats TOP training pipeline).

### Tags
gaussian-splats, photogrammetry, colmap, top, pdg, solaris, usd, karma, rendering, procedural, houdini-22, advanced

---

## Related Tutorials
- [[new-in-houdini-22-training-gaussian-splats-from-infrared-photos]] — also trains H22 native Gaussian Splats via TOPs, but from infrared photo capture instead of iPhone video + COLMAP alignment.
- [[animate-gaussian-splats-with-houdini---free-tutorial-scene-files]] — picks up conceptually where this leaves off: rigging/animating an already-trained splat (H21, uses the G-SOP plugin rather than H22-native nodes).
- [[h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive]] and [[h22---gaussian-splats-peter-sanitra-houdini-22-hive]] — other H22 HIVE talks covering the same native Gaussian Splats toolset from different angles.
