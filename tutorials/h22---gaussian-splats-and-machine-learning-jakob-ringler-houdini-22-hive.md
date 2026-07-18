---
title: H22 - Gaussian Splats and Machine Learning | Jakob Ringler | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=LBkowc4gfjs
author: Houdini
ingested: 2026-07-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive/
frame_count: 0
frame_status: pending-selection
---

# H22 - Gaussian Splats and Machine Learning | Jakob Ringler | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=LBkowc4gfjs)
**Author:** Houdini
**Duration:** 33m47s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro & Neural Cellular Automata (NCA) Basics [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, welcome to this presentation on all things ML. I'm Jakob Ringler, I'm a TD
[0:11] side effects and I'm going to be talking about cells, pixels, points and splats. And I will
[0:16] cover three topics today that are new to DD22, the first one being neural cellular automata
[0:22] or NCA, about which I already presented in this very location last October. So there's
[0:28] a lot of new stuff, so if you've been there bare with me, after that I will look at more
[0:33] neural nodes that made their way into Cops before diving into Gaussian splatting in Houdini.
[0:40] Before diving into those neural cellular automata we will look a bit back in time. The core idea
[0:45] of what I will show today is cellular automata. And one, if not the most famous of those cellular
[0:52] automata is Conway's Game of Life. Most people have probably come across this at some point
[0:57] and the way Game of Life works is very simple. Each cell in a grid runs its own little code
[1:02] snippet that decides what to do based on its neighbors. In practice there are four very
[1:07] simple rules that control whether a cell dies, stays alive or becomes alive. Those very
[1:14] simple rules already lead to very interesting, emergent behavior that isn't programmed
[1:19] in in any way. Depending on how you initialize the script, you can get very different outputs.
[1:25] Another one of those cellular automata is Reaction Defusion, which is also part of Houdini's
[1:29] 21. Reaction Defusion works in a very similar way, but it tries to emulate how two chemicals
[1:37] mix. There's also a single algorithm that runs on each cell, but instead of the four rules
[1:41] we had before, this is a bit more complicated formulas that try to emulate how those chemicals
[1:47] react with each other. But just like before, a single cell can only see its direct neighbors
[1:53] and those patterns emerge by applying the formulas on to the data in each time step
[1:58] on each cell over and over again. Now that we know what the general idea behind classical
[2:04] cellular automata is, we can look at what the neural prefix is supposed to stand for.
[2:08] Instead of running a small algorithm on each of those cells, we can run a very small neural
[2:14] network. Instead of programming the rules ourselves, we can train a network to come up with
[2:20] the rules that fit our target use case. The network should ideally learn how to produce
[2:25] a bigger given pattern based on looking at it. This happens all the time in nature, look
[2:31] at C-brass drives, for example. Each cell in the skin of a C-brass seemingly knows whether
[2:37] it's a black or a white cell and what kind of hair to grow to create this infamous C-brass
[2:42] drive pattern. But no cell can ever see this entire C-bride once. At the same time, not
[2:47] every C-brass the same. There are no pixel perfect copies of different C-brass. And patterns
[2:53] like this are often the result of very simple rules that drive local processes. And to train
[3:01] a network to generate a pattern, we need some way to determine if the output of the network
[3:05] is close in terms of style to our target image. We don't want to measure pixel differences
[3:11] here. We is more about seeing if the general shapes and the colors match to our target.
[3:18] The idea comes from the self-organizing textures paper from 2021. They applied a technique discovered
[3:23] for neural style transfer where you are using a second pre-trained neural network's activation
[3:28] functions to determine whether the image contents are similar in terms of style. You're interested
[3:34] in the specifics. I recommend checking out the distilled block shown on the right here.
[3:38] It has a very, very accessible explanation and even comes with this live demo to play
[3:42] around with. But if you want to learn how to do a basic implementation of this as Houdini,
[3:48] you can watch the older presentation I did last year on the topic. But for anyone who
[3:52] just wants to use it, the good news is that you will be able to do so right from within
[3:57] with in Cops and Houdini 22. Before we dive into any examples, we need to look at what
[4:02] kind of network we are dealing with here. Fundamentally, the network is a convolutional neural
[4:07] network. It uses hard-coded convolution kernels to see its neighbors. You use convolutions
[4:13] all the time in compositing or image processing for sharpening, blurring and other operations.
[4:19] But those specific kernels give the network the local image gradients, so basically the rate
[4:24] of change across pixels. This is the perception part of the network and models how the cells
[4:30] see their neighborhood and surrounding. Here you can see the entire network and the kernels
[4:36] are the IK-LAP, KY, KX-Box in the middle. After those perception kernels follows a super
[4:42] simple neural network. And the network outputs multiple channels, which includes RGB and
[4:47] a few extra channels. And the predicted result is then added to the input to iteratively
[4:52] update the result in each time step. The other information on these extra channels I mentioned,
[4:59] the previous slide. I mentioned the previous slide, store latent information that the model
[5:09] comes up with itself. Sort of like a local coordinate system. Those resemble something
[5:13] like a normal map or position passes, but it's not really position data. It's more like
[5:19] a local follow-off or geometric radiance that describes the pattern's relationships. It
[5:25] helps the cells orient themselves within the pattern, know what they should do in the
[5:29] next update. This is more or less the state of the prototype I presented last time I was


### Solving Performance with Split Architecture [5:30]
**Transcript (timestamped):**
[5:34] here. But it has like one big major flaw. Performance scales quadratically and running even a small
[5:41] 10k parameter model on every single pixel only goes so far. Also running it once may be fine,
[5:46] but multiple times in a loop at resolutions of over 512x512 lets you really feel the hit on
[5:52] performance and your VRAM. Since then there was some research being done that proposed a split
[5:57] architecture. The idea is to split the task of rendering the fine details on the texture
[6:02] from the evolution of the cell state. So cells can still operate at a lower resolution,
[6:08] but the second model is used to decode or effectively render those latent cell states into the
[6:13] correct RGB image. This makes it much more useful for typical working resolutions and that's
[6:20] exactly how we implemented it for cops. You can get an NCA core node that will do the NCA
[6:26] inference logic and outputs the cell state and to an NCA decode node that takes care of the rendering
[6:32] and upressing. Now you may ask, okay, how do I get my own NCA into cops now? First you need some


### How to Train Custom NCA Textures in COPs [6:40]
**Transcript (timestamped):**
[6:41] kind of pattern based target image. For example, a close-up of your genes. You crop it and pre-process
[6:47] it a bit and turn it into a reasonable target square. In cops you find the ML train NCA recipe.
[6:55] All you need to do is plug in your target image and then shows you a little helper layout
[6:59] that helps you check for some of the most common pitfalls. The most important one is scale. The
[7:04] general pattern should ideally still be visible at the low-res NCA resolution of 128 by 128 during
[7:10] training. This also relates to long-range dependencies. Generally a single feature in the pattern
[7:17] shouldn't be bigger than say 10 to 15 pixels in the low-res state. The more cells and element
[7:21] covers the harder it becomes for the NCA to update and propagate this information across the
[7:26] entire image. The update ranges only a single pixel per iteration after all. It also should have
[7:34] as little noise as possible and it should be actually pattern based so those crops you see on the
[7:38] right here should show similar content. Generally you want to avoid fine details that turn into
[7:44] sub-pixel detail on the NCA grid. Then all you need to do is click the cook output button which
[7:50] picks up the training process that runs in tops. You can watch the training process in the ML
[7:56] training monitor. There's a view for the total loss as well as the individual loss components
[8:02] that make up that total loss. Besides the loss you can also check test outputs that are produced
[8:07] during training. Let's you see how the model progresses over time. As you can see here we go from
[8:12] Chibarish to a pretty accurate denim texture in a few steps. The chart on the right visualizes
[8:19] at which up-reshing scale and detail level the loss is the highest. Now that we got all the
[8:25] technicality out of the way we can look at some examples. Once you're one-strained, when the training
[8:32] concludes you can drop down the neural cellular automata recipe and load your model into Cops.
[8:38] You can set how many iterations you want to run the model on the core node and if you don't like
[8:42] the content you can simply change the seed and generate a new variation of the same pattern.
[8:47] You can also define the desired up-resolution of up to 8x on the decoder node.
[8:52] This can be very handy to, for example, create a very fast proxy output and the final
[8:57] high-risk one and you can switch depending on what you're working on at the moment.
[9:03] At the end I'm also visualizing those different cell states that drive this under the hood that you
[9:07] can also look at and maybe use to further refine your output. Here's the target and the result
[9:14] side by side. Can you guess which is which? It's pretty close, right?
[9:23] It's also not limited to square textures. While you train on a 1024 by 1024 target you can
[9:28] influence on practically any resolution your VRAM allows. It also stays tie-lovel at non-square
[9:33] resolutions. The way this is set up means that pixels at the border wrap around and see the
[9:38] other side as their neighbor. So out of the box everything is always tie-lovel.
[9:46] Of course it doesn't have to be run in a single-coken, produce a static image. You can just as well
[9:50] make use of the NCA block recipe, which you can find in Cops. It simulates this over time opening
[9:55] the door for all sorts of effects and motion design setups. Here are two other ones that we're
[10:02] trained on images of different roof-tyling. You can see the cell states under right here in
[10:06] how each NCA learns its own latent space that is entirely different from each other.
[10:15] Here are a bunch more NCA's. I trained to test how well certain patterns work for simplicity
[10:20] and comparability, all of those are running in black and white, but it would work for any kind of
[10:25] coloration really. And then, other set, you can really see where it struggles with the long-range
[10:34] consistency at the top right here. It can't get those horizontal lines straight.


### Driving Pattern Growth and Deformations [10:43]
**Transcript (timestamped):**
[10:43] To look at some ways how we can control that simulation, let's just use a very simple regular
[10:47] stripe pattern for now. By default the cell updates happens randomly on a subset of cells on
[10:54] each iteration. Using mask we can drive the strength or the probability of the update per cell,
[10:59] so you can use a simple ramp or any more complicated monolayer to drive the growth.
[11:13] As I explained before, each cell sees its neighbors using those hard-coded convolution kernels.
[11:19] What you can do purely at inference time without changing how your train is rotating those
[11:24] convolution kernels and through that rotation the perception of the cell leads them to produce
[11:29] those rotated patterns because they believe they are still creating a straight line, but really
[11:34] the world around them has worked. You can drive it with a simple ramp or any more complex input layer
[11:39] you want. Another inference time track is to scale this local perception gradient. You can do this
[11:49] for each axis individually and through that influence how far a cell can see and therefore produce
[11:54] smaller scale patterns. That only works for a well-used less than one, otherwise it becomes unstable,
[11:59] but you can already do a lot with that. Of course you can apply any other cops to anywhere in the
[12:08] loop as well. For example, to store the cells and create those liquid honeycombs. After each time
[12:12] step the cell update fixes any damage that was done by distorting and keeping the pattern alive
[12:18] to drive that point home. I turn off the NCA update halfway through the solve here and everything
[12:24] becomes very blurry and any shapes quickly dissolve over a few frames, but enabling it again brings back
[12:30] all of those details. The NCA keeps all the shapes intact by constantly fighting against the blurring
[12:37] and caused by the distortion, but it doesn't really care about the move cells because locally each new
[12:43] pattern is still a valid result. It doesn't just have to be slight distortion, but it regenerates
[12:52] complete damage and I'm sure this can be used for some interesting organic growth or regrowth effects.


### Seamless Mesh Mapping via Adjacency Rasterization [13:02]
**Transcript (timestamped):**
[13:02] So now you may think here, kind of cool ML image processing stuff, but this is a 3D software
[13:09] right? Why can't I run this on measures and make a zebra, a copybarra for example?
[13:15] And while you can't run on measures directly, Houdini 22 introduces a concept called
[13:20] a chase and seerasterization we already heard about today. That's your compute, all the information
[13:25] needed to allow solvers and other cop notes to trump seamlessly between UV islands and that also
[13:30] works for NCA's. We use this logic combined with the scaling and the rotation functionality shown
[13:36] before we can get seamless inference on any mesh with proper UVs.
[13:43] You can combine this with all of the other control inputs available here and creating a mask
[13:48] from the position pass and the position-based noise derived through rotation and scale.
[13:52] And this already lets you create quite intricate effects and remember this is still just
[13:57] simplest right pattern. Without any other changes, you can swap out the model and see the same
[14:06] effect with different NCA's for example, swirly, then honeycomb or green-tiled copybarras.
[14:11] I'm not sure whether you showed but certainly no one is stopping you.
[14:17] What we can also do is to blend between two patterns and I'm not talking about blending the final


### Latent Space Blending Between Patterns [14:18]
**Transcript (timestamped):**
[14:22] result of two independent ones but to blend the cells of two models in the block.
[14:28] Since the cell states are custom in each NCA, we need to train a bit more carefully to produce a
[14:33] state that can be blended between. This can be done by alternating the target texture during training
[14:39] and after every few hundred steps we switch from target texture A to target texture B,
[14:44] which leads to the model converging to a shared local latent space. To do this, you can make use
[14:49] of this partial training mode on the top node and run it in a for loop. Each loop iteration,
[14:54] we run the example for 500 steps and set the target texture to one or the other image.
[15:00] And in the next iteration, the training resumes with everything it has already learned from the
[15:04] first texture but a new target texture. We do this for a good amount of steps before fine-tuning on
[15:09] one or the other image. This is how the output looks and as you can see the cell states in the
[15:15] middle share a very similar value range so all the colors match left and right. They use this to
[15:21] encode different features that makes it incredibly easy to blend between them meaningfully.
[15:26] To blend, I just use a simple mask that drives the update on each of the NCA core nodes and
[15:31] one gets the normal mask, the other gets the inverted one when they operate on the same shared
[15:36] cell state but update different pixels based on the mask. As you can see, the blend in the cell
[15:43] state works very smoothly. Technically you can use a single decoder but generally those diverge a
[15:50] bit with further training so it makes sense to blend those as well with the same mask.
[15:57] And that gives you the following result. And this is again fairly simple,
[16:03] inputs, it's just dots and lines with a bit of a color gradient.
[16:11] Those are the cell states of the final result and you can really see that the cells don't have to
[16:16] do a lot of work to blend from one to the other because the general values are already in the same
[16:20] ballpark. And just like before, you can combine this with other control maps to drive, for example,
[16:30] the rotation. And besides those, maybe more esoteric NCA nodes and cops, we also got two other


### Next-Gen Alpha Masking with Meta SAM 2 [16:47]
**Transcript (timestamped):**
[16:52] neural nodes. Who do you need 22? Shaps with two external models. And one of them is meta segment
[16:58] anything or SAM 2 that can create alpha masks based on simple user prompts. The other one is
[17:03] Microsoft Smog2 which stands for monocular geometry estimation. It's really a powerful model that
[17:10] bundles multiple features such as extracting depth, normal and position information from a single image.
[17:18] SAM 2 provides the backbone for the neural layer to mask cop. The node provides the convenient
[17:24] UI that lets users prompt the model underneath with simple positive or negative clicks as well as
[17:28] a bounding box. It also has a few helpful built-in features to clean up the final masks.
[17:36] Here's another example that shows how well the model understands the geometry of an image
[17:40] and how you can use negative prompts to restrict the mask when the segmentation defaults to a bigger
[17:46] area. Sometimes the model doesn't recognize the object entirely and no matter how many points you
[17:55] had, it really doesn't get better. But there is a trick. The node can output more than just the
[18:02] final predicted mask. Under the hood, the model predicts not just a binary mask but values that
[18:07] can be interpreted as confidence values. And you can visualize those by talking of this mask
[18:12] threshold. Beyond that, you can also get the image embeddings, which is essentially the
[18:16] model's internal representation of the image. And the third output gives you the points you
[18:21] prompted as geometry and wall space. With those three things, you can reuse them to iteratively
[18:28] refine and improve the mask by running the model on a previous output. It's effectively
[18:33] self-improving the result based on a previous prediction and reusing the points and the embeddings
[18:38] makes sure you don't have to reprompt anything so that the slowest part, which is computing those
[18:43] embeddings, doesn't have to be repeated by downstream nodes. And in that case, that takes you from a
[18:48] very rough mask to a quite clean one without any extra manual work. The other model I mentioned


### Extracting Utility Passes and PBR Textures with MOGI 2 [18:56]
**Transcript (timestamped):**
[18:57] before is Moge2 from Microsoft. The model that can predict this whole set of useful utility
[19:02] passes. And here you can see the model running on different images demonstrating how well it
[19:06] generalizes across different types like CT or actual images and content scales.
[19:16] This doesn't have to be a pure, we have X or compositing related tool. Dmitry made this
[19:21] example where he demonstrates how he used this depth to image, image from depth, to drive the
[19:28] height and reuse, does to create PBR textures based on a single flat marble image.
[19:36] So this can just slot in in any texturing workflow you already use.
[19:42] The node also provides a point output and tries to estimate the reasonable camera for the scene.
[19:48] There's options to clean up this point cloud and you can also automatically assign a set of
[19:52] specific attributes to those points, which triggers the viewport to draw them as Gaussian splats.
[19:58] All you need to do is click on this create a cheeseplad points output, which creates the points
[20:04] and draws them in screen space size correctly. So when you look through the camera,
[20:09] you see the entire image not just the dots, but you can move through it in 3D.
[20:15] And that brings us to our last and final topic, which is Gaussian splatting in Houdini.


### Native Gaussian Splatting Training & Relighting [20:17]
**Transcript (timestamped):**
[20:20] And as we've just seen, and I'm sure many of you already know, cheeseplads are really just points
[20:25] with a few extra attributes to tell the viewport how to draw them.
[20:28] And here's what we had in Houdini 21. It's a simple utility node that takes all
[20:33] loaded PLY point cloud files and translates all those properties to Houdini attributes.
[20:38] Turning on this compute cheeseplads gives us Orient scale and GS Alpha, which tells the viewport
[20:45] how big or how transparent a given cheeseplad is. And toggling on this compute stereo harmonics,
[20:50] checkbox also gives us three more attributes. Those are responsible for the view dependent lighting,
[20:56] which makes cheeseplads so useful. They effectively store how the color should change based on the
[21:01] view angle. But in Houdini 22, we can do much more with cheeseplads. You can, for example,
[21:08] rasterize cheeseplads directly inside of Cops. With the landscape example from before,
[21:14] it becomes trivially easy to add a bit of a camera movement to an image, for example. It just takes
[21:18] three nodes if you don't count loading the file. And you get something like this. This is going to
[21:23] work for everything, probably not. But you can get away with a surprising amount sometimes by just
[21:28] adding a bit of parallax to sell your shot. We get back to rasterizing other splats in a few moments,
[21:38] but before that we should look at how to create a splat in the first place. A big addition in
[21:42] terms of working with cheeseplads is being able to drain your own cheeseplad right from within Houdini.
[21:47] I will do a quick run through of what kind of tooling exists and how you can get started,
[21:51] but Peter Sanitra will do a much more hands-on presentation right after. I highly recommend checking
[21:56] this out for a real deep dive. To create cheeseplads model, you need ideally three things. A set of images,
[22:04] camera data for those images, think transform, focal length, aspect ratio, and so on,
[22:09] and a point cloud that we can use to initialize the training. Those are commonly stored in what's
[22:15] known as a call map format. There's just a folder on this that has the images and a few files to
[22:20] describe this extra information. The sort of information then passed the training program that
[22:26] tries to optimize the positions, colors, orientations, opacities of those points to match the ground
[22:32] truth image. It's not training any neural network, but optimizing the point properties using classical
[22:37] machine learning, essentially mathematical optimization using gradient descent. It can also add or
[22:44] remove points to ensure the density is where it needs to be to resolve any given details on the
[22:49] ground truth images. When starting from actual photographs, you need to find out the camera
[22:56] positions from which each of those photos was taken by triangulating different matching features
[23:01] on the image. But since we conveniently know already basically everything about the CG scene,
[23:07] we can just write out the data into a call map format and generate an initial point cloud in
[23:12] Houdini. The core of the training pipeline consists of those two top nodes. The MLP
[23:16] process g-splats top node takes a set of EXR images with camera metadata and the depth AOE.
[23:23] We can then grab the camera information straight from the xr metadata and construct a point cloud
[23:27] from the camera position and depth AOE by turning the depth of each pixel into a point.
[23:33] The second node is the MLTrain g-splats node. You just have to point it through the exported dataset
[23:39] and cook it which should initiate the training process. Before we see that,
[23:44] here's a quick trick this uses under the hood. You get this camera metadata for free for any
[23:49] karma render which lets you conveniently load the cameras from any XR file back into Houdini,
[23:55] for example, and cops like this. It can be incredibly handy for all sorts of other situations
[23:59] where you need the camera to project on some geometry and maybe you don't have to see
[24:04] file anymore or something else got in the way. It's just a very quick way to get the data back.
[24:12] The easiest way to get started training your own is using this LOB's recipe. All you need to do
[24:18] is plug in your scene in the in-stage sublayer node or load any USD file from this. I just quickly
[24:23] demonstrate how the scene looks here when render through karma. But once you're happy with your
[24:28] scene, you can head to the setup camera arrays subnetwork. It comes with a lot of convenience setups
[24:32] to distribute a set of cameras out of the box and has all the required passes setup.
[24:38] You don't have to use any of that. For some complicated scenes, you may require you to set up
[24:44] custom camera arrays to get the right angles of your scene. After setting up those cameras,
[24:51] all you need to do is click this cook output button which should initiate the training process.
[24:57] One thing that's special about Houdini's training system is that you can train extra features
[25:01] into your splat. Those can be most AOVs or attributes that you rendered as custom AOVs, for example.
[25:07] By default, the recipe also trains on normal and albedo, which you can see here. To set this up,
[25:15] all you need to do is point the node to the correct AOVs before submitting and make sure that
[25:19] those actually exist in your LOB scene. When the training has started, you can head to the ML
[25:25] training monitor again, like shown before with the NCA and watch the progress of the loss. And also
[25:30] get intermediate test renders to show the current state of your gsplat. From left to right,
[25:35] you can see the ground truth image, the current gsplat result, and the heat net visualizing the loss
[25:40] between those two images. You can also check different views depending on the size of your data set.
[25:46] And you can also view the different AOVs you're training for, so you can check the normal
[25:50] and albedo in this case and how that is progressing over time.
[25:54] Beyond that, you can also open live training viewer, which brings you into your browser, where you can
[26:01] easily follow every step of the training in real time. It's a full 3D viewer that lets you inspect
[26:06] the gsplat. There's different view options like depth, alpha, and these extra features that we
[26:12] set up previously. The viewer also provides high-level controls for stopping the training early on
[26:18] pausing it, which will trigger the gsplat being saved out to disk and exported before the
[26:23] final training step is reached. Sometimes it's very handy when you want to stop your top net
[26:28] from cooking, but you actually want to get the output that you're seeing and not just cancel it
[26:32] and hardly. And that's the resulting gsplat brought back into Hedini. The training can export PLY
[26:40] and convert to USD file, so you can just stop layer the USD file back onto your stage, where it
[26:45] lifts like any other kind of primitive. And you're not limited to only training synthetic CG
[26:54] based gsplats. The node also has a basic photo-based training functionality. Just set the dataset
[27:00] type to SFM callmap and you can train on any conventional photo-based dataset. You have to
[27:07] create that callmap dataset first, though there's currently no way to do this in Hedini, but there are
[27:12] good external options available to do that. Epic's reality scan, for example, is free and lets you
[27:17] estimate and export your cameras and images to a callmap structure. From there, the process is
[27:23] practically the same. You can watch the training, which I sped up quite a lot here, and it's really
[27:28] satisfying seeing the scene clear up and all the details get extra over time. You can move around
[27:33] in the scene and inspect any areas of interest. Eventually, you can bring a PLY file into subs to do
[27:40] with it wherever you want. Essentially, it just points. A final lead thing enabled by training on
[27:54] albedo and normal heavies is cop-based relighting. You can bring in your gsplats and extract different
[28:00] attributes you trained on. You can then rasterize it using any camera and apply any AOV-based
[28:05] relighting techniques you usually already use when working with CG renders. You're emitting a
[28:10] pink-keylight and a bit of a specular fun reflection, and this works as expected on the entire frame range.
[28:21] And I think that's it from me. I hope you have a lot of fun with Udd22 and some of the new ML features.
[28:28] Thank you very much.
[28:36] Any questions? Do we have time? Yes. We have time for one question. Is that you first?


### Audience Q&A: Animated Splats & Future Tech [28:38]
**Transcript (timestamped):**
[28:52] Hi, thank you for the talk. It's really interesting. I wonder how well, if at all, is Houdini currently
[29:07] with training 40-gauge in spots, like animated gouges, or is it just statics at the moment?
[29:14] Great question. The training system is designed to train single 3D gouges in spots
[29:22] we have this example in the keynote about an explosion sequence being trained as a gouges splat.
[29:27] You need to do some trickery to really get this to work nicely. Depending on how long
[29:34] you have to render your actual data and how long you have to train, you can actually achieve
[29:39] perfect results because training long enough would give you clean enough gouges splats that
[29:44] actually don't flicker. But if you're limited to a few cameras per frame and a limited point cloud
[29:50] to keep it relatively lightweight, you have to come up with other techniques. The training system
[29:54] allows you to basically load a previous g-splat as a checkpoint and start from that and what we did
[30:01] for the explosion demo is that you can basically train one frame, get this frame into Houdini as a g-splat,
[30:09] atveg.gov with the velocity field, take it back to the training, train next frame, and so on.
[30:16] And that lets you achieve quite a lot if you're willing to put in the time. But yeah,
[30:22] it's definitely something for the future. Okay, thank you.
[30:29] And actually, I think we've got time for maybe one or two more. I think I said somebody over here as well.
[30:36] Hello, I've got a lovely open-ended one, great talk. I like breaking this stuff.
[30:40] This is all very well, and like I saw a few hours where maybe you can manipulate it when the
[30:44] training stage and then the reconstruction phase, but you know better. What's a good way to break it?
[30:48] Like for experimental looks, for example, not for like real production. I don't know, it feels like
[30:53] an open-ended thing. You can, this goes like in the same direction, like starting from something
[30:58] that you bring in from from within Houdini, and you can override a lot of the settings and disable
[31:03] certain optimization. So for example, you can lock points in place, you can turn off like the,
[31:07] it's called densification, which adds more points to different areas, but you can basically
[31:12] force it to keep the same point count. And I think you can achieve some very interesting stylized
[31:18] results by okaying some of that stuff, or starting from something that you prepared in Houdini in some
[31:24] way. Yeah, but there haven't been that many tests in that direction yet, so I'm like
[31:29] curious to see. Okay, I'll go right there. Thank you.
[31:35] Have you experimented with with G's blads and Houdini into her?
[31:38] The first thing I did was to spoilers, yes. But the first thing I did with the calmer
[31:45] splats was just add noise, and it turns it painterly. So I was like, I need to do more stuff to see how
[31:49] much more I can break it, but for Arnold, it's going to work the same as calmer, right? Where it's
[31:54] just, it's the same data going in. So, but yeah. One more appear, yeah.
[32:08] Thank you. Great presentation. You talk when talking about draining G's blads is very easy to
[32:17] get AOVs out of them, and that's generally a cool strength of ML learning and stuff. It doesn't
[32:24] really tend to care about how many layers you've got going in. I'm curious with the neural cellulator
[32:30] atometer. I could see you could change the signature of it. I'm wondering how many layers you could
[32:36] actually feed into it, because it feels like a prime example to just feed a full PBR texture into
[32:44] it with diffuse and roughness and normals and metal and all that. Thank you, first of all.
[32:51] Currently, you can't change the signature, but technically nothing is preventing the system
[32:56] under the hood from producing more channels as an output. This was more of a side project to be
[33:02] frying. So, there's definitely room to add the support that you're talking about for PBR textures.
[33:08] And the second paper I linked to it, they are already kind of doing this. So, they're training
[33:13] on multiple textures, but you need to be kind of smart to formalize this in the training to not
[33:20] diverge in the channels, because otherwise they drift and then you get a height map that doesn't
[33:24] match your RGB. So, you need to be, need to do specific special things that currently this doesn't do.
[33:31] But it could in the future. That'd be really cool. Thank you. Thank you.
[33:41] Great stuff, Jacob. Thanks for taking us to that. Thank you.



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
