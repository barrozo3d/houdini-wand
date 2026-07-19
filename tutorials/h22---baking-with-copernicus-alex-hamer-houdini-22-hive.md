---
title: H22 - Baking with Copernicus | Alex Hamer | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=orN8H41hNDE
author: Houdini
ingested: 2026-07-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/h22---baking-with-copernicus-alex-hamer-houdini-22-hive/
frame_count: 0
frame_status: pending-selection
---

# H22 - Baking with Copernicus | Alex Hamer | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=orN8H41hNDE)
**Author:** Houdini
**Duration:** 14m8s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py h22---baking-with-copernicus-alex-hamer-houdini-22-hive <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro & What's New in Copernicus [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, I'm Alex Hamer and welcome to my presentation which is baking only fast.
[0:12] So the site is not working.
[0:16] So fast you hear my, I'm Alex Hamer, I'm an image processing TD at SideFX and I work
[0:21] in the Copernicus team which usually means that I make stuff like this and texture and
[0:25] simulation nodes.
[0:28] So these are some of the things that we've added to Houdini 22 in Copernicus.
[0:31] So now in 22 we have even more compositing, utility simulation and texture nodes.
[0:36] The ones here on the left are existing ones from last release and then the ones on the
[0:40] right are existing ones from last release which we had some nice upgrades to and today
[0:49] we'll be talking about these ones.
[0:50] So baking.
[0:52] So today what we'll be looking at is what baking is, the state of baking in Houdini 21 and some
[0:58] limitations that were there, the new workflow, the new bake-free process up and cop and then
[1:04] a little demo.


### Game Optimization & The Importance of Texture Baking [1:06]
**Transcript (timestamped):**
[1:06] So last release we added the baked Johnston textures node which allowed you to bake a
[1:10] low and high resolution model and then take the Johnston data from the high resolution
[1:14] and output texture maps from it such as it's curvature or normals or height as well as
[1:19] any other custom attributes like vertex color or whatever you wanted really.
[1:23] So what's the point, what can you do with these maps?
[1:25] Well in the beautiful land of real-time rendering we are terrorized by performance and
[1:29] optimizing so baking is a great way of getting extra detail.
[1:33] You can easily use these bake maps like in this example to fake or create extra details
[1:37] without the sacrifice of high polygon counts which is a great application for games.
[1:41] You can see on the left the original high resolution model and then on the right a
[1:45] low resolution copy of it with the baked texture applied and it looks practically identical.
[1:51] But it doesn't just have to be for optimization, you can use the bake maps to drive masks to
[1:55] build materials or use them to drive other effects.
[1:58] It's just a simple example of combining a few maps to add some visual detail to an asset.


### Comparing Tracing Modes: Surface Normal vs. Cage Mesh [2:04]
**Transcript (timestamped):**
[2:04] So there wasn't any major upgrades to baked Johnston textures this release, in fact technically
[2:08] we actually removed stuff from it, sorry.
[2:11] But let's have a look at what this node can actually do.
[2:14] So there are three tracing modes, so surface normal which is where you just have your low
[2:18] and your high and you get the baked Johnston data from your high res.
[2:22] You have cage mesh mode which is where you have your low and your high and a cage mesh.
[2:26] It's the same process almost except you generally get better bake results from it and then you
[2:30] have single mesh mode which is just where you have your low and you treat your low as
[2:33] the high res so it's useful for getting Johnston data on a single mesh as texture maps without
[2:41] tedious processes or things that would not be as easy to get.
[2:45] But cage mesh mode was kind of annoying to do in certain scenarios, it was good for great
[2:49] bakes and let's have a look at why.
[2:52] So let's first look at the default mode from last release which is surface normal.
[2:56] So we take the normal from the low poly, we trace bi-directionally and then we take the
[3:00] first hit that we get.
[3:02] This works okay for most scenarios but there are some problem areas which won't be picked
[3:07] up or are going to be picking up areas that weren't meant to be seen or it will just be
[3:10] a mess basically.
[3:12] So in cage tracing we offset from the low res mesh, we then trace backwards towards the
[3:18] high res and we get our hips that way and the idea behind this is that we basically avoid
[3:22] those problem areas and we get better bake results.
[3:27] Last release when in cage mesh mode we had some options for how to customize your cage
[3:30] such as its cage offset and you could see the results updating live but there was a major
[3:35] problem with this.
[3:36] Here you can see some footage from the launch demo last release.
[3:40] The issue is that you're kind of doing the cage adjustment blind and basing a correct
[3:44] cage on visual results or areas which are the black parts there where the cage is intersecting
[3:48] the high res.
[3:50] Since you couldn't see the cage mesh yourself as it was internally generated inside the
[3:54] baked geometry textures node you couldn't say easy without checking the baked map whether
[3:57] your cage was intersecting your high res which of course would cause issues.
[4:01] And that was the main reason that the default tracing mode was surface normal and these also
[4:07] generated cage parameters were only there as a backup in case you didn't have your own
[4:10] custom cage.


### Introducing the New Bake Pre-Process Node [4:13]
**Transcript (timestamped):**
[4:13] So that spawned the creation of baked pre-process which is a SOP and a COP which is a new node
[4:19] that can be used as a pre-process to your baking which can set up your cage mesh and
[4:22] your geometry for baking.
[4:24] So again we're not just trying to fix the limitation on the backup parameters on the
[4:27] baker itself we also want users to have a dedicated node for setting up a cage.
[4:34] So this is what the workflow looks like you have your low end, your high res, you put
[4:37] it through baked pre-process and then it will help you generate a good cage mesh and then
[4:41] baked geometry textures will give you texture maps.
[4:44] Here's the interface of baked pre-process let's just cover it.
[4:47] I mentioned earlier that we took some things off the main bake node and that was really
[4:50] all of the auto-regenerated cage options so now this is the node that you'll do all of
[4:54] your cage setup on.
[4:56] You have your normals which is a very important aspect of baking.
[4:59] You can customize how the normals are created as well as something called cage softening
[5:02] and let's have a look at what that is.


### Cage Softening, UV Seams, and Skew Prevention [5:06]
**Transcript (timestamped):**
[5:06] So with a simple example of a cube with some bolts on it as our high res and then a simple
[5:10] box as our low res we expand outwards using our low resolution but that could mean that
[5:16] our normals are angled slanted along the flat face.
[5:22] So when we bake we can see that the bolts are skewed at an angle which is obviously something
[5:25] we want to avoid.
[5:27] So instead of we split the cage mesh at the UV seams or technically in this example of
[5:31] a box the faces the bolts are now baked straight on once we adjust the normals sorry the bolts
[5:37] are now baked straight on which is correct and there are other ways around this issue
[5:40] such as skew map painting but we won't cover that today.
[5:46] Going back we have our ray start and ray end offsets so ray start is your cage and then
[5:51] ray end offset is how far the rays will travel past your low res.
[5:54] By default we have no ray end offset though so we have infinitely traveling rays so let's
[5:58] have a look visually as to what that actually looks like.
[6:00] So we have our low resolution and then our high resolution with lots of detail so we
[6:05] expand outwards as our copy of our low res and this is our cage which fill in capsulates
[6:09] our high res then we fire backwards towards the high like what we covered earlier.
[6:14] We can also add a ray end mesh which is another duplicate of the low res which we offset in
[6:19] wards which has to sit fully inside the high resolution and we can then trace all the
[6:23] way from the cage mesh to the ray end mesh.
[6:26] This is useful if you wanted to stop baking at a certain point or there was a certain
[6:30] other jump tube lying around that you didn't want to pick up by the tracer.
[6:35] And lastly we have the cage attributes which store the cage data which sit on the cage geometry
[6:39] output and this is what the baked geometry textures node will use to figure out how the
[6:44] rays should behave.
[6:45] So that's pretty much the whole interface of baked pre-process.


### High-Tech Fan Asset Live Baking Demo [6:49]
**Transcript (timestamped):**
[6:50] So let's use it.
[6:51] Here's a cool high tech fan asset and admittedly the low res are still pretty high res for game
[6:54] standards but if you think of it as a hero asset it works so don't ask any questions.
[7:00] So let's enter Houdini and use our bake setup recipe to set up a baking network and we can
[7:04] link our low and high res.
[7:06] So now we have our geometry ready to be baked.
[7:08] Then we have baked pre-process in the network so we can enter its interactive state in the
[7:12] viewport by pressing enter.
[7:13] And then you'll first see an orange mesh around your main mesh which is your cage.
[7:19] So we can do things like change the opacity and change what it's comparing to whether
[7:24] it's comparing to nothing or the low res or the default which is the high res.
[7:31] So you can probably see some Zed fighting there and that's because at the moment our
[7:34] cage has a zero offset distance so it's intersecting with the high res mesh and as I mentioned this
[7:39] is going to cause big issues.
[7:41] So a way to solve that is to turn on high res intersections which makes the high res red


### Interactive Viewport Cage Editing & Intersections [7:46]
**Transcript (timestamped):**
[7:48] and the cage mesh a bright blue.
[7:50] So then I can zoom in and adjust interactively within the state the cage offset until I have
[7:54] no more red and then I know it's probably safe to bake.
[8:01] That's not the only way we can adjust the cage.
[8:04] I mentioned earlier softening the cage so I can do that by UV seams.
[8:08] So you can see that happening.
[8:10] I'm adjusting the cage offset and it's being split across the UV seams.
[8:13] I think I also maybe mentioned earlier that there are other ways of doing it such as by
[8:18] faces or if you want to get really custom you can do it by an edge group.
[8:22] Or we can even adjust it as an attribute.
[8:26] So I'll quickly add a float attribute to our low res.
[8:31] Then in bake pre-process I can scale the race offset by a very sensibly named attribute
[8:37] and then it's a little hard to see it first but if I make it a little bit dramatic and
[8:40] turn off the model preview you should see that it's being scaled very clearly across
[8:43] our mesh because of our attribute.
[8:47] You can also adjust the end offset as mentioned so I'll clip the geometry in half within the
[8:55] state and then I'll zoom into a section and we can see once I enable it the purple ray
[8:59] end mesh appears and then I can adjust it so it's sitting inside the high resolution.
[9:06] I spoke too fast.


### Lookdev, Procedural Shading, and Preview Materials [9:10]
**Transcript (timestamped):**
[9:10] You get the idea.
[9:12] I can then set up a supermaterial using occlusion and curvature I think and then I can see the
[9:18] results updating on preview material across all UDIMs at once.
[9:21] Once I adjust the cage distance you can see once I enable softening cage the results
[9:25] change again and then once I'm happy with it I can move on to making some materials
[9:32] from my baked maps.
[9:37] So we'll build a cop material.
[9:39] Here's our bake setup and then we're using these baked maps to drive various components
[9:46] such as in this example we're using shape scatter and curvature to drive how where scratches
[9:51] are placed on the model or we can use various maps to control how various noises or colors
[9:59] are placed basically using them to drive shaders.
[10:04] And then we can see all together on the preview material across all UDIMs.
[10:08] The lighting might look a little wonky in the viewport but that's because this was made
[10:11] for Unreal so the normals aren't really what the viewport or Copernicus expects.


### Integrating Textures Into Unreal Engine [10:18]
**Transcript (timestamped):**
[10:19] We can then bring it into Unreal itself by setting for simple material in Unreal's material
[10:23] editor and then here we have the final setup in Unreal.
[10:35] That's pretty much it.
[10:36] That's not just that there's a few more slides, a few more slides.
[10:43] I've got thank you slides.
[10:44] A huge thank you to LeWoo Internet Side Effects for helping with this presentation for the
[10:48] model and the textures and baking in the Unreal setup.
[10:51] He's a very talented technical artist and he'll be available for higher end of September.
[10:55] Big thanks as well to Omar, Fiana, Ali, Mark, Nikola, Jeff, Nada and Ethan for helping me
[11:00] with this release, the Python states and this presentation.
[11:03] As well if anything that I said in this presentation didn't make sense there's a button on every
[11:07] node but on the top right it's got a question mark.
[11:09] We have a very good docs team so that's your backup.
[11:13] And that's it.
[11:15] Thank you.
[11:16] Any questions?
[11:17] Yeah.
[11:18] Oh no, it's George.
[11:23] Looks great.


### Q&A: Unreal Map Previews & Baking Parts by Name [11:24]
**Transcript (timestamped):**
[11:26] Thanks.
[11:27] You've wasted about six months of my time.
[11:39] Sorry.
[11:45] But I was curious about the visualization in COPs.
[11:52] Are there any plans to fix it so that there's like a conversion to get it to render correctly
[11:55] while you're in the Houdini context?
[11:59] Visualization in COPs, what do you mean sorry?
[12:00] So you mentioned it didn't look correct because it was set up with the maps for Unreal.
[12:05] Oh yeah.
[12:06] Are there any plans to just add some additional nodes to get it to look correct in Houdini?
[12:12] Not yet.
[12:13] It doesn't exist yet if you want to submit an RFE.
[12:16] I'm happy to look at that.
[12:19] At the moment, pre-material can only handle its own type of normals.
[12:23] So yeah, sorry.
[12:28] And if anybody has any questions about Natsura, which is a foliage system based on Houdini,
[12:34] George Homa is right here.
[12:35] He's one of the co-founders.
[12:36] Talk to him later.
[12:41] Thanks for the great talk.
[12:49] I was just wondering in the Baycar, like in Substance Painter, how you can bake per part,
[12:57] if that makes sense.
[12:58] Is there a feature, like a dropdown where we can add different components?
[13:02] If you've got a really complex model, but maybe you want to bake out to different materials
[13:09] or textures or UDMs or something like that, is there an option where we can match the
[13:14] parts together, like the higher res and the low res, within the same bake or do we have
[13:18] to do a different bake for each part?
[13:23] I went too far.
[13:24] Sorry if you already covered that.
[13:26] No, I didn't cover it, but you should be able to see.
[13:30] Okay, right at the bottom there, you see match pieces by name.
[13:33] So you can do it, yes.
[13:35] And you can basically just have a name attribute on your low and high res, that match, and
[13:39] then it will do it basically in its own, it will do the baking in its own pocket mention
[13:42] for each bit.
[13:44] So yeah.
[13:49] Excellent question.
[13:50] That gets a flippy.
[13:52] Not every excellent question gets a flippy, but some do.
[13:56] Any other questions?
[14:01] We are all good.
[14:03] Nice work.
[14:04] Thanks, Alex.
[14:05] Thanks.



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
