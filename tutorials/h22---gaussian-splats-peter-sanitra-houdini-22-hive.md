---
title: H22 - Gaussian Splats | Peter Sanitra | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=HUTd8BHNHKI
author: Houdini
ingested: 2026-07-19
houdini_version: "22"
tags: [solaris, usd, cop, top, pdg, volumes, karma, rendering, advanced, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# H22 - Gaussian Splats | Peter Sanitra | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=HUTd8BHNHKI)
**Author:** Houdini
**Duration:** 36m32s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro & What Are Gaussian Splats? [0:00]
**Transcript (timestamped):**
[0:00] Alright everybody, I'm going to talk about the Gaussian splats pipeline in Houdini today.
[0:13] But first let me introduce myself.
[0:17] My name is Peter Sanitra, I am a Houdini generalist with Passion for FX and I currently
[0:22] work at NVIDIA and maybe some of you can remember me from last year's presentation about the
[0:28] NPM solver and the Cream and Cookies demos.
[0:32] But today we're talking about the Gaussian splats of course, about the pipeline, SideFX
[0:38] built for us to generate those and I'm going to demonstrate the work in the pipeline with
[0:45] some of the examples of our typical assets like volumes or animated G-splats.
[0:52] We're going to capture some of the characters and intricate details in fur and look at the
[0:58] environment's capture or interior or exteriors and I'm going to wrap it with some current
[1:04] issues or limitations or where this really shines, where the G-splats are really doing
[1:10] great.
[1:11] So we're going to have a look at this explosion, this is actual G-splats rendering in the viewport,
[1:18] so are these clouds and we're going to animate this parliament, convert it to G-splats and
[1:26] capture these characters, intricate details in fur, you can see the G-splats capturing
[1:32] reflections in the eyes and we're going to have a look at this bar seen from the content
[1:37] library and challenges there with capturing interiors.
[1:45] So for those of you who have no experience with Gaussian splats, what are those?


### Stacking Opacities, Parallax, and Fine Fur Details [1:51]
**Transcript (timestamped):**
[1:52] Of course, we are Houdini artists, so for us it's just points with attributes, but the
[1:59] definition will be of Gaussian splats and anisotropic ellipsoid with multiple attributes and same
[2:07] primitive can be a source sphere like you can see there on the left side or a flight
[2:11] disk or a heritain strand.
[2:14] The important thing is that each of these points carry this spherical harmonic function
[2:20] and that describes how the splat behaves from different viewing angles, so the result is
[2:24] really view dependent.
[2:26] And then of course the job of the pipeline, we have in Houdini's to figure out how to
[2:32] rearrange these points in 3D space, how to scale them or orient them, what attributes
[2:36] or color information or AOVs they carry, how opaque or transparent they are and then we
[2:45] can stack them together and reassemble the final image with them.
[2:49] And then of course when we have those splats we need to render them and that's actually
[2:54] the easy part, we just sort them from to back and stack the alpha of those splats.
[3:01] What you can see on those squares there, imagine those are your splats and in cameras
[3:07] they have different capacities and you stack them and then the view moving sideways and
[3:13] the parallax will create this illusion of for example of the reflection in the eye or
[3:21] specular highlights.
[3:22] And here you can see for example on these whiskers the individual points, those are
[3:28] those G-splats but they are so stretched that they can form these whiskers from very
[3:34] few points.
[3:35] And here you can see how you can capture the intricate details of the fur with this simple
[3:41] method of stacking opacities and stretching these shapes.
[3:50] So let's see how we can do this.


### SideFX's Native Solaris Splatting Recipe [3:52]
**Transcript (timestamped):**
[3:54] Let's prepare this recipe for us, you can just drop it right away in the Solarix, in
[3:59] the stage on the Solarix content and basically you are ready to go with a single click of
[4:03] a button and all you need to do is load your asset in a sublayer or reference or subimport
[4:10] and then execute the graph.
[4:13] And under the hood there are a couple of things going on and we will look at all the individual
[4:19] pieces of that process which will be generating camera rig, then generating the ground tool
[4:25] renders initial point clouds training and exporting to final assets.
[4:33] So first thing of course to do is we need to create these cameras, the viewpoints that
[4:39] will generate the ground tool images that will go into the training and for that of
[4:45] course we really need this recipe to do it for us and as Jakob was showing already there
[4:51] are plenty of options, controls for you to cover your subject perfectly and you can also
[4:57] feed your own cameras because now in Hoonin22 we have cameras in SOPS so you can just copy
[5:05] two points, any cameras you can create rigs like this with copy two points in seconds
[5:10] so it's super easy to work with the cameras.
[5:13] Of course for the interiors and exteriors the courage of the subject is a key factor
[5:19] so you need to work it a little bit more but I'm going to show that in the later sections.
[5:29] And here is such a camera rig that looks almost like a Poldebewek light stage right?
[5:35] I'm trying to capture this hamster model.
[5:41] So these are all the cameras I used to render the ground tool images.
[5:51] So when we have our camera rig set up we need to of course render those images, generate


### Gathering Ground Truth Renders & Extra Feature Training [5:54]
**Transcript (timestamped):**
[5:56] the training data for the training process and you can render those images with anything
[6:03] you really using in Hydra, you've used Karma, Redshift, Arnold, RenderMan, anything will
[6:09] work.
[6:10] The important bit is that you need to render the OpenXR format because the camera with
[6:16] the data is embedded directly into a file so you don't have to provide the camera as
[6:20] a separate assets.
[6:21] And also the OpenXR will store the data information so you can easily generate the initial point
[6:29] cloud from that depth and transfer or project back those OpenXRs to the points including
[6:36] every AOV or any other data you have and then you end up with a feature carrying point
[6:44] cloud that basically holds the information, all the information you need to get that training
[6:50] going.
[6:55] And here are just some examples of the ground tool images from those cameras I rendered
[7:00] in Karma XPU for the training of the cloud asset.
[7:09] And as Jakob was mentioning before, the good news in Hootin22 is that we don't only train
[7:18] the basic RGB information, how we actually see the GSPut but we can also train any extra
[7:24] features coming from AOV layers in the OpenXR.
[7:28] So if you have, for example, normal map or a bid or subsurface for the leaves, for example,
[7:33] in the scene, then you can train it as well and basically you will end up with GSPut on
[7:39] normal map.
[7:40] So this is the actual GSPut displayed in the Hootin22 viewport of a normal map of this
[7:45] palm.
[7:46] And why that is important because then you can really use GSPut as a format or a container
[7:53] that carries all that information and in cops with the new nodes you can resturize those
[7:58] two planes and work like if you were working in Nuke when you can relight it, change the
[8:04] compositing, change the look or layers and contributions.
[8:08] So you have really proper compositing of GSPut, same way as you have with OpenXRs.
[8:19] As far as the actual training process goes, so that is running a top graph and in each


### Training Strategies: Default vs. Monte Carlo [8:20]
**Transcript (timestamped):**
[8:28] step the algorithm is comparing your current version of your splat against the ground truth
[8:33] images and it's pushing those points towards a better fit.
[8:38] So it's trying to find the positions, orientation scales and training the data of those interval
[8:44] points to really represent your asset as best way possible.
[8:50] And there are two ways to do that, one is called default and the other one is Monte Carlo.
[8:58] And the main difference is between them that the default algorithm is adding and removing
[9:04] points so your point count is changing during the training process and in Monte Carlo you
[9:10] can set a fixed limit.
[9:11] For example you just want to have 100,000 points in your GSPut and then the algorithm
[9:15] will just move those points around and retrain them so your point count is fixed.
[9:24] And we have three schedules here you can see on the bottom of the graphs and those are
[9:29] important for us because we want to have as efficient as we can use each of our hardware
[9:38] so we for example need to render those ground truth images.
[9:41] We want to set that for example to submit on a farm or to render five frames at the same
[9:46] time on our hardware and then for the training we want to submit it for example to the GPU
[9:53] number three because that's the one that has the most VRAM so that's how we can configure
[9:59] the efficiency of the execution of this training graph.
[10:07] Of course when the training is running this is something you will see the so called trip
[10:12] tick or these three images when you have the ground truth on the left then your current
[10:17] version of the GSPut in the middle and then the noise or the heat map is very similar
[10:23] to what you are used to from rendering when you are inspecting the noise or the problematic
[10:29] areas you will see the same here.
[10:31] The red areas are showing the areas where your GSPut is not yet matching the ground
[10:37] truth and the blue areas are very close to the ground truth and of course that's interactive
[10:44] or new training so here's how the blue is changing the hues are changing and how the
[10:53] centering is becoming more and more like the ground truth image on the left.


### Tracking Loss Metrics & Splat Count Quality Comparison [11:09]
**Transcript (timestamped):**
[11:09] And here's the left training monitor tab which is the new tab side effects edit for us to
[11:14] actually see the actual values of noise loss and number of iterations and these are more
[11:20] technically important data.
[11:25] So here's one of the graphs that explains really well the strategy, the training and
[11:32] the process of the training.
[11:34] So this is for training the furry character, the hamster model and on the x-axis you will
[11:41] see the number of iterations.
[11:42] I've trained this 400,000 iterations and on the y-axis we can see the number of points
[11:49] in the final GSPut.
[11:52] So we start with sitting 1 million points and then we start the training process and
[11:59] right away we drop to around 200,000 points and then this is the default strategy which
[12:05] is pruning and growing so it's adding and removing, adding and removing, adding and
[12:09] removing that's why we see this so shape growing and removing and after roughly 20,000-30,000
[12:18] iterations the algorithm will realize we have enough points to describe our scene, to our
[12:27] model, our asset in a way that really matches the asset so then it starts to remove more,
[12:35] just adding a little bit, remove more, more, more and then you'll see the point, the number
[12:40] of points in the GSPut is dropping and there are maybe 400,000, 300,000 you start to kind
[12:48] of flatten out, plateau out and then that's the territory where you basically are starting
[12:54] or you are in diminishing return territory where you are training but you are not getting
[13:00] much of a better result and you basically training noise and you should probably stop
[13:05] the training.
[13:09] You can observe very similar behavior here on the, if you're watching for example the
[13:14] noise loss, the drop is almost linear till like 30,000-40,000 that's where the core of
[13:22] the work is getting done and after 50,000 basically flat so from, if you training and
[13:29] you observe this graph you will see that you basically wasting resources like training
[13:34] 400,000 when, for example 10 minutes when I could have already been done by 5 minutes
[13:40] yet 50,000 iterations.
[13:49] And of course you can specify the target point count of the GSPut so you can really go to
[13:55] the high fidelity or light wave GSPut and here I've prepared a bit of a comparison for
[14:00] this hamster.
[14:01] Then we will see the actual GSPut rendering viewport and the point count or the points
[14:08] representing those GSPuts and this is with 300,000 points and I will go down to 80,000
[14:16] and 20,000 and down to 5,000 and you will see how that translates to the quality of the
[14:22] GSPut.
[14:27] So we can see that dropping down from 300,000 down to 20,000 which is a magnitude difference
[14:34] it's definitely not 10 times less representation of that same subject so GSPut really holds
[14:43] really well at low split counts.
[14:50] And here's the same for the face.
[14:55] And if you look at the mouth or nose area you can see those small like individual almost
[15:01] like a brush strokes like shapes and those are those GSPuts that are oriented in certain
[15:08] way so we are looking at them right now we see them as strokes but from the side for
[15:14] example they actually represent that surface.
[15:23] And of course like during the training you're getting some checkpoints so you can, in case
[15:30] you crash or abort you don't lose your work so every 10,000 frames you can export for
[15:35] example the PLY file which is the native format for GSPuts or you can also export the USD file
[15:42] and also you can partially restart or retrain just some specific data like for example you
[15:49] already trained your GSPut with just RGB and you want to end normal suite or subsurface
[15:55] then you just restart from your existing model and only train that new coefficients.


### Volumetric Wins: High-HDR Explosions & Instant Clouds [16:07]
**Transcript (timestamped):**
[16:08] Alright so we're going to have a look at some more examples and start with volumes.
[16:14] So of course volumes they have no surface and they are just continuous distribution
[16:20] of density and density stacking is what makes volume works.
[16:26] By that I mean you have voxels, you have some density and you have many of them in camera
[16:31] Z-Depth and you're stacking them together that's creating the illusion of the representation
[16:37] of the volume of the cloud or the explosion and something very similar is happening with
[16:42] GSPuts you have these ellipsoids that are stacked in depth and they have opacity instead
[16:49] of density but the mechanics is the same you're stacking multiple elements together and creating
[16:56] the image.
[16:58] Therefore the volumes are really great candidates for GSPut representation and of course the
[17:06] optimizer there is no surface on the volume so how it decides where to put those individual
[17:12] GSPuts?
[17:13] Well they will be put in the areas of the most variation or more visual interest in the image
[17:20] so in the explosion where you have a lot of contrast a lot of changes in the data there
[17:25] will be a lot of points same for the clouds you will have a lot of GSPuts on the edges
[17:31] but very little for example in the center area that is very flat there will be very few GSPuts
[17:37] in there.
[17:42] So here's our explosion this is actual GSPut rendering in Karma viewport and what I'm showing
[17:47] is because I want to point out one very important information and that's that GSPuts actually
[17:55] can carry high dynamic range data so if you rendered your ground to the images of this
[18:01] explosion correctly to open XR without clamping that will translate into the GSPut so if we
[18:08] have a look at our GSPut the values for example are over 30 here in this GSPut which means
[18:13] that if you put it in your environment you can basically illuminate the environment with
[18:19] a GSPut and also what notice is the file size reduction of course the original VDB was 1
[18:28] megabyte and GSPut will be 10 times less so there are really useful representations for
[18:36] volumes.
[18:41] So here's the actual explosion and GSPuts the points representing the explosion.
[19:00] Alright so let's have a look at clouds my favorite clouds of course are very interesting
[19:05] because they have this anisotropic scattering right because it's mostly water very strong
[19:10] forward scattering so when you look at the image on the left you will see we are looking
[19:16] along the right light direction and that clouds looks pretty flat compared to against the light
[19:23] you will see all these nice highlight edges and lights scattering through as you will see
[19:29] those white boiling shapes that's the anisotropic scattering to the cloud and of course GSPut
[19:37] being anisotropic and being viewport dependent viewport dependent really captures this final
[19:44] man really well and of course clouds are notoriously slow to render because they need to take many
[19:56] bosses in a race so sometimes you're rendering clouds for hours if you're doing fly throughs
[20:02] compared to that GSPut you have this GSPut will render at like 100 frames per second
[20:08] in the viewport and the magic is almost like one to one with the offline render.
[20:17] So here's that cloud and here we can see the anisotropy like from this angle looks very
[20:23] flat and as soon as we start to rotate we will see a bit of a almost like a specular
[20:28] highlight on the edges and then you'll see the rim light and scattering through the cloud
[20:34] so from this angle really it looks different than from the other angle.
[20:45] And here's what I was talking about the position of those GSPuts on the cloud you can see the
[20:53] clustering that fractal you know cauliflower shapes you can see the points being mostly
[21:02] on the edges on the area of visual interest and there in the center there are almost no
[21:07] points almost no GSPuts because in render or there was a bit of a shadow so those shadow
[21:13] areas can be represented with much bigger or smoother you know splats and the edges they
[21:20] really need to stay sharp so you have a lot of points there on the edges.


### Animating Splats Natively & The New USD Schema [21:28]
**Transcript (timestamped):**
[21:29] So let's have a look at how we can animate GSPuts.
[21:34] So I will show it on the example of this palm which of course I had to only train this GSPut
[21:40] once on a static pose and GSPuts of course they are just for us with ARC it's just a
[21:47] bunch of points with attributes so we can manipulate them as we see fit so we can use
[21:53] any existing tools to deform it so in my case point deform or you can use lattice wires
[21:59] for characters you can absolutely you can use the same rig to rig your GSPut and have
[22:06] an animative character as a GSPut so there is no preferring training needed most of the
[22:11] time you're just driving that single GSPut with any tools as you usually do.
[22:22] So here's that palm which I think was maybe 50 or 70 thousand points the original was
[22:29] million polygons maybe so super lightweight holds up pretty well from those couple of
[22:40] points.
[22:41] And of course when we have animation we usually need to store it in some way and for that
[22:48] USD is a great candidate because Pixar in this year released added a new USD schema for
[22:56] Gautian Splats so the Gautian Splats are now first class citizens in the USD world and
[23:02] of course Solaris reading all the USD's natively can read them as well and that way you can
[23:09] really store efficiently your GSPut on disk because you will only time sample really the
[23:16] changing properties or pre-inverse so if our palm GSPut has opacity, orientation, positions
[23:23] and spherical harmonic functions you only time sampling position as the points are moving
[23:29] you, time sampling orientation and everything remains is just static properties so animating
[23:39] GSPut of palm like this will be maybe will be in hundreds of megabytes compared to the
[23:46] you know polygon model it will be in gigabytes of caches for that mesh for 600 frames animation
[23:53] I was doing.
[23:57] So here is just the palm in viewport natively as USD primitive and here is the wipe of showing
[24:07] the point counts on the palm.
[24:14] This was trained with subsurface and normal ZNLb data and all that so you can see like
[24:18] the leaves have nice subsurface there on the top and as we start to rotate you will see
[24:23] some specular and we start to rotate more different angle it will become flat again
[24:27] because the light is not hitting it so it's really nice and interactive and the anisotropy
[24:33] is there captured in the GSPuts.
[24:37] Alright so let's have a look at a bit of the characters.


### Environment Capture & The Camera Placement Problem [24:39]
**Transcript (timestamped):**
[24:41] First I want to thank Lorraine Evers for providing this beautiful model so I had so much fun
[24:47] trying to capture this and of course characters they have very intricate surface detail they
[24:54] have fur, hair, whiskers and translucent tissues like these ears so it really is quite challenging
[25:02] for patresos as we all know rendering very very thin hair, sub pixel size so I really
[25:09] wanted to see how GSPuts can deal with that and I was really surprised that GSPuts are
[25:14] such a good fit for capturing fur especially for this cat I really wanted to push it so
[25:21] I've rendered like 2k render maybe 300 cameras or something and tweak the optimizer and I
[25:29] think it's representing that subject really well everything to single one every single
[25:36] hair is there in the model.
[25:43] And here's our furry hamster with all those details as well, individual hair strands and
[25:48] here I want to show the anisotropy as well the fur from this angle is pretty flat and
[25:56] as we start to rotate you will see the hair will get nice backlight and transparency showing
[26:06] and again as we rotate it will be rather flat and also the specular in the eye is moving
[26:13] it's very interesting because there is no surface right and just those ellipsoid stacking
[26:21] creating the illusion of moving specular and here's the cat I want to see the yeah showing
[26:30] the points here I think it was nearly half million or something points points for this
[26:35] cat but the match to the offline render is almost like one to one quality for the offline
[26:47] render and specular in the eyes are moving again it's very similar to the hamster.
[26:55] Alright so what about the environments the last bit we did not cover it so let's have
[27:00] a look at this bar scene of course the bar scene I name it as a honest case because this
[27:05] bar is a kind of subject where this really gets harder but not because of the pipeline
[27:11] but because of the inputs like the the bottleneck of course is the data set you are feeding to
[27:16] the training the ground to the images and your split is only ever going to be as good
[27:21] as your input so the environments really are the category where the camera courage gets
[27:30] tricky because you have a lot of surfaces and sometimes you will see them from very
[27:35] awkward angles or you don't see them at all for example under the table like behind the
[27:41] bottles behind the bar or under the counter or really if you don't place a camera there you
[27:49] will not see that you won't be able to generate a G-split for something you you never saw so no
[27:56] matter how many cameras you have or how much how hard do you train if you don't have the
[28:00] courage you will not be able to generate the G-split and of course after I realized that that
[28:06] designing the camera rig actually was the task I need to overcome and I found this paper from
[28:13] 2024 on the optimal camera placement so I thought you know I just implemented in Houdini Rango
[28:19] and you just pipe the pipe the geometry into the Rango it will mathematically position those
[28:28] cameras based on how much they overlap if they are seeing the same subject for multiple angles if
[28:34] they are occluded and so on so if you're ever going to capture environments or interiors you really
[28:42] need to treat camera placement as an engineering problem that's that's the right mindset you will
[28:47] not succeed succeed with spherical rig around the scene right and here's how the bug looks captured
[29:04] and now I will show this interesting bit from me outside that probably nobody ever saw because
[29:11] nothing outside and that will bring me to some of the issues and limitations or how they can
[29:20] manifest so I freeze this frame from the outside you will see a very interesting shapes in there
[29:26] like big soft blobs or these long spiky regions or wrong colors suddenly some green colors there
[29:34] right but this is all the same dominant failure mode simply we don't have cameras there we haven't
[29:42] not seen that subject right or we see it from very few angles so we cannot really model or represent
[29:49] those area without knowing anything about it so that's the main major failure if you start to see
[29:56] stuff like this happening in your viewport that's that's a coverage problem of course grass
[30:03] of reflection mirrors basically they change look based on your camera so each ground through the
[30:11] image will give you different information so you just can't model that correctly
[30:15] alright so what about the other things to watch out for of course the HDR clamping I mentioned
[30:26] if you clamp your images of course you will get very fat and boring looking g-spot so don't
[30:33] clamp your images you want to have nice and rich interior scene with a lot of lights and
[30:37] interaction of course when you are going to train you need to generate those ground to
[30:44] the images so that's a compute heavy for me compute heavy operation I'll give you need if you want
[30:52] to have 500 cameras for perfectly cover the bar you need to do 500 renders right so I need to
[30:59] really plan a little bit for it and of course when you're going to train the g-spot the more
[31:08] images you have the more resolution they have the more VRM they will consume during the training
[31:13] process but but I think it's not so critical for all these assets I trained their trained under
[31:22] a 60 gigabytes of VRM so even on consumer great GPUs you can create nice g-spots like this
[31:29] of course another kind of a drawback here is the temporal solution for g-spots because there is
[31:35] no native native as in algorithm or in code way how to train animated g-spots so sadly at this point
[31:46] the animation is what I was showing capture single g-split deform it or very costly per frame
[31:52] training and of course at this stage there is not many tooling for manipulating g-spots like you
[31:59] have Photoshop for images would be nice to have something like that for g-spots but on more
[32:09] positive notes let's see where this really means as I was saying volumetric capture small clouds
[32:16] and stuff like that and that's an actual feed right we can capture those super easily they render
[32:24] the real-time speed giving us really the offline quality so there's really great case for using
[32:32] g-spots if you are using or producing on virtual sets or the second set extensions or using
[32:39] backgrounds virtual backgrounds you can use g-spot because they have of course high dynamic range
[32:45] so they will respond very nicely to your camera and there are definitely cases for real-time
[32:54] previous application because g-spots are super lightweight right couple of megabytes couple
[32:58] thousand points usually and again they render real-time speed so you can really configure your
[33:05] training for a specific budget you need and you can use it for your real-time stuff or you can use
[33:10] it in a pipeline for example for as a usd display purpose because they are native now and usd and
[33:18] if you are using a student you need a better view for it representation that is still very
[33:23] very lightweight you can use for example g-spot for that instead of some couple of polygons in all
[33:30] models and of course the biggest one here is for Houdini because this pipeline is really end-to-end
[33:36] with a single graph single execution you get the final product as usd or as a ply directly and you
[33:46] can make that for example dependent on your asset publishing so if you're not all published new
[33:52] asset you can kick off this task of generating g-spot automatically and use that directly as
[33:56] a usd preview purpose for example so it's really end-to-end automated you can distribute it on a
[34:02] farm and betrush it and so on so I think it's the first like end-to-end pipeline that some sort
[34:12] of so the Houdini I guess is the first here right and I guess that's that's it for me right
[34:21] super cool we're pretty short on time but maybe one question here
[34:35] hello that thanks for that great presentation I was just interested about lighting them in


### Q&A: Relighting Splats in Copernicus vs. Solaris [34:39]
**Transcript (timestamped):**
[34:49] karma because I think you mentioned maybe you could light them in cops or really light them in
[34:53] cops but in the previous in 21 I don't think I could really do much lighting with them in karma
[34:57] yes there are new nodes in cops that are aware of the g-spot format so you can just do so
[35:05] import and you will recognize it's a g-spot and then you have new nodes for that's called for
[35:11] example g-spot rest rise that you can pick any like a layer basically from the g-spot so you can
[35:18] rest rise RGB of the g-spot rest rise albedo of the g-spot or normal of the g-spot and then basically
[35:25] you have the those as image planes and you can do your standard compositing stuff so for example you
[35:30] can have like a row lighting pass right and you do your lighting and with cop nodes and then you
[35:40] add subsurface on top of it for example or I just call or as much whatever you want and then you
[35:44] rest rise it from camera you can also bring to cops so basically you have like a 3d composition
[35:51] options you can you can modify those relate to relate those in cops and I think there were
[35:55] some videos already on the youtube some other guys showing how you can relate to those you know
[36:00] you need but that's all right in karma so in the salaris bit can can you put these g-spots in and
[36:07] then relight them there because currently I couldn't do that in 21 or don't think yeah you can
[36:11] just load it like a usual primitive like any other geometry in salaris and you can put lights in there
[36:17] and everything okay great yeah really cool stuff Peter thanks for taking us through that



---

## Captured Frames

- [5:35] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_000.jpg
- [7:44] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_001.jpg
- [10:17] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_002.jpg
- [11:34] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_003.jpg
- [14:16] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_004.jpg
- [20:23] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_005.jpg
- [25:36] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_006.jpg
- [29:26] tutorials/frames/h22---gaussian-splats-peter-sanitra-houdini-22-hive/frame_007.jpg

---

## Structured Notes

### Core Technique
Houdini 22's end-to-end synthetic Gaussian-splat pipeline: a single Solaris recipe that generates camera rigs, renders EXR ground truth with any Hydra renderer, trains splats (with AOV feature layers) via a TOPs graph, and exports PLY/USD — demonstrated on volumes, animated assets, fur characters, and interiors.

### Summary
Peter Sanitra (NVIDIA) walks the full H22 G-splat pipeline. Splats are anisotropic ellipsoids with per-point spherical-harmonic view dependence — to Houdini, just points with attributes. The SideFX recipe drops into a Solaris stage: load an asset, execute, and it builds the camera rig (H22's SOP-level cameras allow Copy-to-Points rigs), renders ground-truth **OpenEXR** (camera + depth embedded; any Hydra delegate — Karma/Redshift/Arnold/RenderMan), seeds a point cloud from depth, trains via TOPs with per-stage hardware scheduling, and exports PLY (native) or USD — now a first-class Pixar USD schema, letting animation time-sample only changing properties (hundreds of MB vs gigabytes of mesh caches). Beyond RGB, AOVs (normal, albedo, subsurface) train as extra features, unlocking Nuke-style relighting/compositing in COPs via new splat-aware nodes (GSplat Rasterize). Strengths: volumes (10× smaller than VDB, HDR values >30 can light a scene, 100fps clouds with true anisotropic scattering), fur/whiskers (stacked stretched splats; moving eye speculars with no surface), real-time previz and USD preview purposes. Weaknesses: camera coverage is *the* bottleneck for interiors (treat placement as an engineering problem — he implemented a 2024 optimal-camera-placement paper in VEX/wrangles), glass/mirrors, HDR clamping, VRAM-bound training, no native temporal training, sparse editing tools.

### Key Steps
1. **Recipe** — drop the SideFX G-splat recipe on the Solaris stage, load the asset (sublayer/reference/SOP import), execute: camera rig → ground-truth renders → initial point cloud → training → export.
2. **Camera rig** [frame_000, 5:35] — auto-generated light-stage-style rig, or feed custom cameras (H22 SOP cameras + Copy to Points). Coverage is everything for environments — an implemented optimal-camera-placement algorithm positions cameras by overlap/occlusion; "you will not succeed with a spherical rig around an interior."
3. **Ground truth** — render **OpenEXR** (embeds camera + depth; depth seeds the initial point cloud; every AOV projects back to points → feature-carrying point cloud). Any Hydra renderer works (Karma XPU used).
4. **AOV feature training** [frame_001, 7:44] — splats train RGB, position, orientation, scale, opacity *plus* extra AOVs (normal/albedo/subsurface) in a single pass — the palm's normal-map G-splat displays right in the viewport; rasterize any layer to image planes in COPs for relighting and proper compositing.
5. **Training** [frame_002 triptych; frame_003 graph] — TOPs graph compares splat vs ground truth per step. Strategies: **Default (prune & grow)** — point count fluctuates (SFM init 1,000,000 → sawtooth as opacity resets every 3000 iters → refine-stop freezes count → final 322,285 for the hamster) — or **Monte Carlo** — fixed budget, points only move/retrain. Loss drops near-linearly to ~30–40k iterations then plateaus: stop there, further training is noise. Per-stage scheduling (farm renders, pick the big-VRAM GPU for training). Checkpoints every 10k let you resume or *partially retrain* (add normal/subsurface coefficients to an RGB-trained splat).
6. **Quality vs count** [frame_004, 14:16] — 300k → 80k → 20k → 5k comparison: a 10× point drop is nowhere near a 10× quality drop; low counts hold up. Close-up splats read as oriented "brush strokes."
7. **Volumes** [frame_005, 20:23] — splat opacity-stacking ≈ voxel density-stacking; optimizer concentrates splats at high-variation areas (cloud edges, cauliflower detail; few in flat/shadowed cores). Explosion: HDR intact (values >30 — can illuminate an environment), ~10× smaller than the source VDB; clouds capture anisotropic forward scattering and render ~100fps vs hours offline.
8. **Animation** — train once on a static pose, then deform the splat point cloud with normal tools (Point Deform, lattices, the character's own rig — no retraining). Store via the new USD Gaussian-splat schema, time-sampling only P/orient.
9. **Characters** [frame_006, 25:36] — Lorena E'Vers' cat/hamster: ~2K renders, ~300 cameras, optimizer tuned aggressive on fine detail — every hair, whisker, and moving eye highlight survives close inspection (~half a million points for the cat).
10. **Failure modes & limits** [frame_007, 29:26] — big soft blobs / spiky elongated splats / wrong colors = coverage gaps (areas seen from few or no cameras); glass/refraction/mirrors are view-dependent beyond the model; don't clamp EXRs; training is VRAM-bound (all assets here < 60 GB VRAM); no native time-aware training; editing tooling sparse. Shines: volumetric capture, virtual sets/backgrounds (HDR-responsive), real-time previz, USD preview purpose, and full automation (hook splat generation to asset publishes, distribute on a farm).

### Houdini Nodes / VEX / Settings
- Solaris G-splat recipe (single-click stage setup); SOP-level cameras + Copy to Points rigs (new in H22)
- Ground truth: OpenEXR with embedded camera/depth/AOVs; any Hydra delegate (Karma XPU shown)
- Training: TOPs graph; Default (prune & grow — opacity reset every 3000 iters, refine-stop freeze) vs Monte Carlo (fixed count); loss/iteration monitor tab (new); triptych ground-truth/render/heatmap view
- Export: PLY (native), USD (new Pixar Gaussian-splat schema; Solaris loads natively — lights/relighting work like any prim)
- COPs: splat-aware import + **GSplat Rasterize** (pick RGB/albedo/normal layers → image planes → relight/comp, project back)
- Numbers: hamster SFM init 1M → final 322,285 splats; cat ~500k; palm 50–70k (from ~1M polys); cloud/explosion ≈ 10× smaller than VDB; HDR values 30+; training < 60 GB VRAM

### Difficulty
Advanced

### Houdini Version
Houdini 22 (viewport G-splat rendering, SOP cameras, AOV feature training, USD schema, splat-aware COPs nodes)

### Tags
solaris, usd, cop, top, pdg, volumes, karma, rendering, advanced, houdini-22

---

## Related Tutorials
- [H22 - Gaussian Splats and Machine Learning | Jakob Ringler | Houdini 22 HIVE](h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive.md) — the preceding HIVE talk referenced throughout ("as Jakob was showing")
- [H22 - KineFX Rigging and Procedural Animation | Henry Dean | Houdini 22 HIVE](h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive.md) — rigging/animating the deform-a-static-splat way
- [H22 - Baking with Copernicus | Alex Hamer | Houdini 22 HIVE](h22---baking-with-copernicus-alex-hamer-houdini-22-hive.md) — COPs baking workflows adjacent to splat rasterization
