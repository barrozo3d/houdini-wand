---
title: APEX in Houdini: Evolving Animation Workflows for Production | Mattéo Martinez | Paris HUG 2026
source: YouTube
url: https://www.youtube.com/watch?v=fhgP_W-OvUE
author: Houdini
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/apex-in-houdini-evolving-animation-workflows-for-production-matteo-martinez-pari/
frame_count: 0
frame_status: pending-selection
---

# APEX in Houdini: Evolving Animation Workflows for Production | Mattéo Martinez | Paris HUG 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=fhgP_W-OvUE)
**Author:** Houdini
**Duration:** 41m47s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py apex-in-houdini-evolving-animation-workflows-for-production-matteo-martinez-pari <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction & Demystifying Apex in Production Workflows [0:00]
**Transcript (timestamped):**
[0:00] How to make a studio in Paris
[0:06] Wow!
[0:10] Wow, thank you for that.
[0:12] Hi everyone, I'm Matteo Martinez, also the broomer on the socials.
[0:17] I'm a freelance Houdini generalist,
[0:20] but currently working at Brand Studio Paris as a CFXT tech lead.
[0:24] Yeah, at first, I've been working with APEX in the beginning of its beta,
[0:31] and at first it was just by Artisan's exploration,
[0:35] but as the time went on, I realized that it's a very cleverly designed tool
[0:42] and realistically meant for productions.
[0:46] And I think that the current main problem with APEX
[0:49] is that only a few managed to fully learn it.
[0:53] Hence, a lot of people that thought APEX is not meant for this or this
[0:57] or lacks this or this, didn't know that actually they were wrong.
[1:03] APEX is still a bit mysterious for a lot of professionals today,
[1:06] so I wanted to be here to open the discussion about production workflows
[1:12] using APEX.
[1:15] Today, I wish to show you the researches I've been doing all this time
[1:18] and why I believe in a near future APEX may be extremely attractive
[1:24] for a lot of studios and independent artists.
[1:27] We'll get right into it in my first part,
[1:29] and then we'll see why the history of Houdini concerning animation and rigging
[1:33] is very interesting and even a strength in our case here.


### OpenUSD vs. Alembic: The Architecture of Non-Destructive Layering [1:36]
**Transcript (timestamped):**
[1:36] APEX is very exciting for animation and rigging, for characters, prop, etc.
[1:43] But here we'll look at a bigger picture.
[1:47] We'll explore the big cloud of possibilities that surround
[1:50] and make possible rigging and animation in Houdini,
[1:54] which is not talked about much,
[1:56] while it's for me absolutely crucial for APEX viability and strength
[2:00] compared to other solutions and also to mystify how it works.
[2:04] Let's let you in on this secret.
[2:07] What you are looking at right now is a cache.
[2:12] You might know it already, but in Houdini we can do ragdoll simulations
[2:16] directly inside the animation scene.
[2:19] So I threw six characters in ragdolls.
[2:24] Sorry.
[2:27] So I threw six characters in ragdolls just like here.
[2:33] That's just as the green floating boxes.
[2:36] And I added subdivisions to their models
[2:39] so that the cache is heavier to cache on disk and then read
[2:44] so that a maximum of optimization cannot be done.
[2:50] What this cache does is that it caches everything you have in your scene.
[2:54] This means that when we have accesses to the cache with an animation node,
[2:59] we can get everything the animators did.
[3:02] The animation layers are here, the animation keys,
[3:04] the very parameters used for the ragdoll simulations.
[3:07] When we start the simulation again, we get the exact same result as the animators.
[3:12] And this little purple box here is here to show that constraints are also preserved.
[3:25] I did a little comparison using this scene for reading time of the caches.
[3:30] The evaluation time of this cache really nears the evaluation of an ABC cache
[3:35] while exporting the skeleton too.
[3:37] And sometimes it is even faster in our case here with a large scene, it is faster.
[3:43] The beauty of this cache is its weight.
[3:46] For an animation that lasts 240 frames,
[3:49] this cache weighs 35 megabytes on disk.
[3:53] I hope this amaze you as much as I.
[3:56] Using ABC, it would have weighed 27 and 100 gigabytes.
[4:00] It's 745 times smaller.
[4:04] I'll let you ponder what this means for workflows, archiving projects,
[4:09] space on servers, FX artists, CFX artists,
[4:12] animfix that have a lot more tools to work with in the same time,
[4:16] with an evaluation time that needs ABC caches.
[4:19] But actually it's faster when we decided to work on only one character,
[4:25] which is most of the time.
[4:28] Here I show that I'm importing only one character with its skeleton


### Revolutionary Caching: Storing Scenes 745x Smaller than Alembic [4:31]
**Transcript (timestamped):**
[4:32] directly from the cache without the need to load the others.
[4:35] We ask the cache to dynamically get only one.
[4:40] The biggest downside of this way of caching
[4:43] is that it's distinct for workflows that almost only use Houdini for its production steps.
[4:49] But in a world where a lot of productions turn away from Maya to do its CFX,
[4:54] FX and infix lightning rendering in Houdini,
[4:58] we can be sure that this is not a niche or obscure proposition.
[5:03] For this tool, I'm making each character transport some important informations about itself,
[5:08] like its name, version, path.
[5:11] When Objects hits the tool, just down there,
[5:15] it creates a list of all the important informations that will help recreate this scene.
[5:20] I call it a registry.
[5:23] It compiles it into a folder and then caches it.
[5:27] When we want to retrieve my scene,
[5:29] I extract the registry first, read it,
[5:33] and then import everything in a loop over all the registry instances.
[5:38] I can then reapply my keys, layers, or ragdoll constraints.
[5:43] And maybe also some custom data as you applied for your specific custom workflows.
[5:50] Create an animation or a rig in Houdini and you can extract very easily a lot of value from it, a lot of data.
[5:58] I just showed that we could transport some sophisticated data like channel primitives, animation layers,
[6:04] but the most likely use cases will be these kind of characters.
[6:11] I created a folder which departments could store or what they need.
[6:15] Items can be retrieved by the identification name.
[6:20] And by the way, I find this way comfier than the very, very, very long ABC paths that we currently use to get only one geometry.
[6:30] And not only the geometry, as you might see it in the CFX folder,
[6:34] I'm importing something that's called cape.deformscript.
[6:39] I import it inside the character, the very script that will deform my highly, highly cape.
[6:49] Perfectly as I always want with the right capture weights and everything else.
[6:58] In any production I've been, we would have loved having that.
[7:02] Every data is well compartmented and has no chance to affect point orders, attributes, etc., etc., and other data.
[7:12] What's interesting to understand from this first part,


### Deep Dive into Apex Scripting and Fast Autorig Components [7:15]
**Transcript (timestamped):**
[7:15] is one of the biggest strengths of Houdini that will influence the rest of this talk.
[7:19] This caching has been made possible because Houdini allows to break down, disassemble, reassemble data very, very easily.
[7:27] This is a great strength of Houdini in general, data management.
[7:32] Assembling and disassembling of this data has a very limited amount of code.
[7:38] This is something I foster myself to do for all the examples of this talk.
[7:42] Use very minimal custom codes or custom methods and maximum use of Houdini accessible tools for everyone.
[7:53] This also means that these tools can be accessible to be made by mid-artists and knowledge more transferable.
[8:02] This is very important and I want to end my first part on this.
[8:06] Easier data management makes tools accessible to mid-artists.
[8:10] The knowledge can be taught more easily.
[8:13] Your workflow is clearer and stable and allows environments like SAP, Apex, Carp, DARP, Top
[8:20] to communicate bringing depth and flexibility to your tools.
[8:24] But I will discuss this topic later.
[8:26] If you have a little dev team of devoted mid-artists, it already can create wonders.
[8:34] I'd like to explore what I mean by flexibility for the tools,
[8:37] but first we'll have to understand where it's from.
[8:40] I will show you two practical examples to show how we work using Apex and Kinefx
[8:45] so that we can be all up to date.
[8:48] For those who are already Apex users who won't learn anything big right now,
[8:53] and I try to make it interesting for the rest.
[8:56] In Houdini, we are sort of expected to create our rigs by creating auto-rigs components.
[9:01] Our rig is a graph like the one shown here.
[9:04] This is a very simple one.
[9:06] Each node you see in this image is a controller.
[9:09] This is a simple FK rig.
[9:11] You can create or modify this graph by operation installed by another graph.
[9:16] This one graph, for example, asks to look for every point in our skeleton geometry
[9:23] and create a node that describes its transformation and parent it.
[9:28] This is how we have our FK rig set up.
[9:31] But if, like me, more so if it's a big rig, you find this laborious to create all the nodes by hand,
[9:38] renaming them, connecting them, you might want to use Apex script, which is Python,
[9:44] but adapted to script faster in Apex, and I cannot emphasize how great Apex script is when you get it going.
[9:52] It's so much nicer to create a loop that connects 200 nodes to their corresponding node than doing it by hand.
[9:59] As you can see, the code is quite compact for the exact same operation I showed you just before.
[10:06] I personally have a small library of my favorite scripts to treasure all my little discoveries,
[10:11] and also operation I often do to gain time.
[10:15] This is very efficient.
[10:17] After you have set up your perfect auto-rig component, you can apply it by your code.
[10:23] We have a very simple joint sector auto-rig.
[10:26] When you select the joint here, it selects all the joints on the finger.
[10:31] Or you can store your script and then apply it visually with the auto-rig builder.
[10:36] This might ring a bell to you.
[10:39] It's very similar to the same feature in Unreal Engine.
[10:42] We just have to click and drag our component inside the viewport on our skeleton.
[10:48] I started using it recently, and so far it proves very useful for non-technical profiles
[10:54] to use your components and to adapt to some workflows.
[10:59] As you can see, there's already an existing list of frequent-rig operations.
[11:05] The auto-rig capabilities are vast, and the possibilities of dragging auto-rig components
[11:11] is an excellent complement to be a bit more manual and visual in our approach.
[11:16] Still, you surely want sometimes to just manually prototype something
[11:21] before going into several hours of scripting.


### Procedural Skinning: Transferring Smooth Capture Weights via Convex Hulls [11:23]
**Transcript (timestamped):**
[11:25] This is why we have the fuse component.
[11:28] Here, I'm creating a very simple IK component.
[11:34] The nodes are added just here in orange.
[11:40] But because we are prototyping, I want to know if these components can be used elsewhere.
[11:44] I can mirror my manual modifications because the fuse-rig component does hold all the heavy lifting
[11:53] to understand how it works, or I can remap my IK to another location, like for the arms.
[12:02] We could argue that even though rigging by proceduralism is advanced by nature,
[12:10] for example, a rig is adapted to be automated,
[12:15] still creating a skeleton, skinning the geometry, we'll always need a human hand.
[12:22] I think that this is right, but it doesn't mean that we are doomed to only use things by hand.
[12:31] We can also make this workflow procedural even for advanced skinning.
[12:35] This is my second example.
[12:38] In this example, there was a piece of geometry that was a bit tricky to skin
[12:42] because of all these little geometry cells on the neck right here.
[12:46] When we try to smooth the capture, these high-resolution clusters make the smoothing not very homogeneous,
[12:54] and painting it by hand needs precision because of the bells.
[12:59] If you are a rigger, you know that if you don't have a tool or a plugin or a script,
[13:04] you're in to spend some time adjusting all that.
[13:07] It won't be as simple.
[13:09] But here we just have to find the trick.
[13:11] I created a convex hull, remesh it, capture the hull instead of the complex geometry,
[13:16] smooth its captures, and then transfer them on the geometry.
[13:20] This is something quite classical, but what I find great specifically in this example
[13:26] is that for every situation you have your perfect technique become everything.
[13:34] I was able to do the full skinning of an advanced model entirely with procedural methods,
[13:41] and it felt so good when the client came back with a heavily modified version of this model,
[13:46] and everything still worked perfectly.
[13:48] I'm sure riggers will like to work this way in the future.
[13:52] Now that we have understood how things might come together using Apex and Kinefx,
[13:58] we can go back to more interesting things.
[14:01] Let's get crazy and show where this flexibility can get us to.
[14:05] Here's a little series of tools that I made to work together.
[14:11] This framework, we'll see several different nodes,


### Custom Rigs for CFX: Drawing interactive Skeletons and Deformers [14:14]
**Transcript (timestamped):**
[14:16] this framework was made with the intent of helping CFX artists to art-direct clothes
[14:21] with quick rigs adapted to their current needs for the sharp needs.
[14:26] It can be used before a simulation to bias the results.
[14:30] In the future, I'd like to make it able to do past simulations or corrections for art directions
[14:38] to use the simulation as a base of work instead of the final product.
[14:44] With this user state, we can create points and connect them as we wish,
[14:49] and inside the tool is an interpreter that will change this geometry to a viable oriented skeleton.
[14:57] We can then use Kinefx Capture Nodes workflow or some custom one I made to make it faster.
[15:09] At the very end, it hits this little tool there that will interpret everything we have done so far.
[15:20] It will interpret things a bit dynamically.
[15:26] For example, this spine will be our main skeleton,
[15:31] and all these floating joints will not be part of the main rig.
[15:37] It will be snapped joints to the surface of the geometry so that we have the rig deformations
[15:44] and add another layer of deformation for these floating joints to add more precision to our control.
[15:57] As you can see, what's interesting is that it can behave like a cloth and collide with the character skin
[16:03] thanks to the wrinkle deformer component.
[16:07] Most interesting is the fact that we can combo this workflow with the Autoric Builder still
[16:17] and add some new behaviors to what we just draw.
[16:21] Here, I'm doing a simple wave deform.
[16:28] You can control it interactively inside the viewport.
[16:32] It's a step-by-step progression for the artist, but from what I could see already,
[16:37] once they are accustomed to the workflow, they like the amount of control and possibilities that they are disposed of.
[16:44] They can really adapt to each shot and have a maximum control.
[16:48] Another neat idea is this tool to animate proxies.
[16:52] You know, we very often have these shirt sleeves, pants sleeves, capes, ponytail that are already animated


### Dynamic Proxy Animation: Baking Structural Deformations on the Fly [16:58]
**Transcript (timestamped):**
[17:01] or partially by our animators.
[17:04] The problem is that sometimes it's not just the geometry that follows the character,
[17:09] sometimes the geometry deforms, making working with it harder.
[17:14] Here we have a very rough animation of Electro-Aviboponetail.
[17:18] This tool takes your geometry at rest position and understands how it moves.
[17:25] Rest position and deform position.
[17:27] It creates a rig that travels throughout your geometry and makes its deformation on the skeleton.
[17:34] As you can see right here, when we enter the tool, an animation layer is already set up there
[17:40] and stores everything the tool has understood from the movement of your proxy.
[17:47] As you can see in the animation state, we can also add our new custom logic here.
[17:54] I just put a simple spine auto-recomponent just to have more control on our ponytail
[18:01] and then animate it and then get it into the simulation and have a maximum control.
[18:06] The additional beauty of this tool is because we work inside an apex scene,
[18:12] we can use the apexing tools, native tools.
[18:15] For example, the ragdoll tool I showed earlier was a native apexing tool.
[18:23] If the artist feels more comfortable with the full body IK tool, he can use it
[18:28] because it is very easily set up inside the tool.
[18:33] If the artist is facing a lot of collision or maybe just wants to give a physical movement to the proxy,
[18:40] he can use the ragdoll tool too.
[18:42] We can also set the properties.
[18:45] Just like you see here, you can set the properties of the ragdoll directly inside the tool
[18:52] before going into the simulation.
[18:55] We have, for example, a very nice deformation, something very rigid at the root of the proxy
[19:02] and something much more smooth at the end.
[19:08] With collision and everything, of course.
[19:11] What the positive feedbacks brought me is that before having access to this tool,
[19:16] artists were reluctant to animate proxies by themselves because it was so much harder before.
[19:22] They were not accustomed to it.
[19:25] Once they are, they feel the big control difference and come back often to it to get fast results.
[19:35] Just for fun, this prototype of a tool that merges characters with rig between them.
[19:40] We can modify the rig's transforms and nomenclatures so that we can merge the same rigs multiple times.
[19:47] The beauty of this tool is that it is made almost only with basic nodes like rename, rig pose,
[19:55] the auto-rig fuse graph.
[19:59] I can imagine a show with robots that combine and decombine.
[20:04] With this kind of tool, we can have less trouble managing all the characters created for each combine.
[20:11] We just have to combine them and not have 100 characters rig for a series that counts only three characters, for example.
[20:19] What we can learn from this part is that the flexibility by a ring by the whole apex,
[20:25] Kinefx, Houdini environment, allows us to use the technology for other things than characters' productions,
[20:31] animation and still have a lot of value from it.
[20:34] It can be used by multiple artist profiles and can be used in departments other than rigging animation.
[20:41] I've shown several examples that apply to Cfx, which are industry vastly migrated to Houdini 4.
[20:48] I believe that we may see integration of apex in these production steps just to improve their speed or artistic capabilities.
[20:59] What I find truly fascinating with the approach of Houdini is its synthetic approach.


### Houdini's Synthetic Approach: Mirroring Three Decades of Animation Progress [21:04]
**Transcript (timestamped):**
[21:05] What do I mean by that? Let's do a little bit of history.
[21:08] Blender was created in 1994, Maya in 1998, Lightwave 3D in 1990.
[21:15] We are at the very beginning of the CGI animation industry.
[21:20] Yet we don't know how to proceed, even at times where we have the technology.
[21:25] For example, at the very beginning of CGI in the 70s, we used spreadsheets to animate and not controllers.
[21:33] We're not talking about technology here, but also techniques that are being discovered.
[21:39] Interfaces, features, animation sliders, character picker.
[21:42] Go to the web and look at the first interface of Lightwave 3D.
[21:46] You'll see that a long path has been done.
[21:51] Every 3D animation software that existed at the time adds the techniques that have been found in their animation and rigging package.
[21:59] Layers upon layers of new technologies.
[22:02] Plug-ins came along the way, too, adding the new techniques and experience found by the artists themselves that wanted these to be set up in their favorite software.
[22:14] Only Houdini, like behind, and offer a small animation and rigging package,
[22:19] just not to block productions that are crucially needed to do that in Houdini.
[22:25] For these software, changing all this is a bit risky because communities are already constructed upon these layers, shortcuts, logics.
[22:35] Changing this while everything works fine seems kind of absurd.
[22:39] Now, Houdini gets into the animation world and has a unique position where you can build an animation community, an animation and rigging package that has to be created from the ground up,
[22:50] inspired by everything that worked out well in these three decades of animation.
[22:57] And this is the topic of this part, the synthetic approach.
[23:00] Houdini has gathered techniques and knowledge from various sources and tries to synthesize them as a new proposition.
[23:07] Here's a selection of features that materialize what I mean.
[23:11] For example, the motion mixer.
[23:13] The motion mixer gets animation clips and allows to blend them on this timeline there.
[23:18] This is quite interesting for CGDobbles, yes, but also for animatic prototyping, 3D storyboards, or layout animators that may want to animate and retime fast.
[23:30] My guess is that motion builder has very likely inspired the motion mixer.
[23:35] The interfaces look very alike and I'm glad to have it on Houdini now.
[23:40] Another example, you can retime your animation directly in your playblast, the flipbook in Houdini.
[23:47] And of course, it can update your controller inside the animation scene.
[23:51] Quite interesting for giving feedbacks.
[23:54] I'm wondering if we can bridge it to, I don't know, a shotgun or an F-track to give the feedback directly inside this software.
[24:04] And everything is retimed.
[24:08] Let's continue.


### Native Layout Tools: Sliders, Motion Mixers, and Ragdoll Physics [24:09]
**Transcript (timestamped):**
[24:09] Side effects integrated natively some animatons features, like animation sliders just above the timeline there.
[24:17] I mention it because to my surprise, Maya doesn't have its own natively.
[24:21] So it seems that side effects decided that this is too important not to have it directly.
[24:26] If I had more time, I could talk about the animation catalog, which is some sort of equivalent to the animation library.
[24:32] There's one transformation functionality too from Animbot.
[24:37] Having it natively feels smoother because the tool doesn't have to try not to hurt already existing shortcuts or intersects with all the features like Animbot successfully did with temporary pivots.
[24:52] The viewport has of course been set at the center of the logic here.
[24:56] The menus are floating, can be closed, folded, so we can almost work only in the viewport.
[25:02] An insane amount of modification can be done natively to our controllers.
[25:06] They're thickness, transpirers behind the character, hiding behavior.
[25:10] Here I show hiding while scrubbing.
[25:13] Just now.
[25:15] Yeah, scrubbing.
[25:17] Hiding while scrubbing.
[25:20] Or dragging and hiding while dragging.
[25:24] Also, I like to speak the translate and rotate gizmo, keeping the rotation in local transform and translation in world.
[25:31] So you can feel comfy at home.
[25:35] I also already told you about the animation tools, full body IK, ragdoll.
[25:42] The ragdoll tool isn't meant only for specific cases of simulations.
[25:47] If your rig contains a ragdoll configuration, you can collide your controllers using the ragdoll pose.
[25:53] It detects collisions and displaces your controllers to suitable positions.
[25:58] It also works in reverse.
[26:03] I could talk about the locator tools too, but you know that's locators.
[26:10] The one tool I didn't tell you about is a dynamic path tool.
[26:14] It calculates trajectories based on your animation position and timing.
[26:23] By looking at the frame range of your path and its distance, the tool creates the right trajectory with the almost physically accurate timing.
[26:32] And you can still modulate these trajectories, as you can see.
[26:36] And the object is retimed.
[26:38] For example, I have a simple throw animation there, and by making the path longer, like so, the ball is retimed, so is the character that catches the ball later.
[26:56] But one thing that Houdini is very, very good at is synthesizing environments.
[27:02] For example, you are not doomed to use Apex tools inside of Apex.


### Cross-Environment Ecosystems: Merging VEX, OpenCL, and Machine Learning with Apex [27:05]
**Transcript (timestamped):**
[27:07] There's a lot of bridges you can create with other environments.
[27:10] Here's a bridge with SOP.
[27:13] What I did is create constraints using Vox, Vex, and SOP, and deform these constraints using OpenCL and SOP2.
[27:23] I'm interested in the details of the great tutorial by VoxLFX about this technique.
[27:28] And then I can compile this node graph in a graph that can be interpreted by Apex.
[27:36] Right here.
[27:38] This is the Apex environment.
[27:41] Now you can see that the paintbrush collides and deforms in real time.
[27:46] You can also use the Recal Deformer tool that does that just perfectly.
[27:52] And here is another merge.
[27:56] This time between machine learning and Apex.
[28:00] Credits to Arnold Jetekel for the model and texturing.
[28:04] Here I just created a simple panel of wrinkles here by Blend Shapes.
[28:10] And the ONIX model has learned how to do the poses it didn't know yet.
[28:15] And of course we can still move the wrinkles manually.
[28:22] Here's a little clip of the training.
[28:29] What I want to develop here is not a bashing of interesting features.
[28:34] Apex still can lack some features now, but I want to show that that philosophy is driving side effects for now and later,
[28:42] learning and assimilating natively.
[28:45] The character picker seems to be underway.
[28:48] Devs seem to be aware of these lacks.
[28:52] If you look closely at the Houdini 22 clip, we can see a little icon, a button that says character picker.
[28:59] So I think this is pretty soon.
[29:04] We are in the middle of mayor's decline.
[29:06] Everyone is looking for a successor.
[29:09] And this is why I believe through more accessibility to high-end technology, flexibility, workflow clarity,
[29:17] cohesion and communication between environments, Houdini will make its place inside the animation world.
[29:23] And Apex sits at the middle of it all.
[29:26] Thank you for listening.
[29:33] Also, if you are interested in Apex, we are creating a full training course with Voxel Ethics.
[29:39] So you can contact us if you need more information.
[29:41] Now if you have questions.
[29:47] Thank you.
[29:50] Do you have any great questions?
[29:53] It's a great day.
[29:58] I don't have any questions. I just want to take the floor.
[30:01] I'm a very fast learner. I'm currently a great graphic designer at Brunch.
[30:05] I want to say thank you because it's the lead tech right now.
[30:09] Everything you've done, honestly, I recommend you believe.
[30:13] I'm kidding. Thank you very much for your advice.
[30:16] I hope everyone will understand a little bit of Apex's philosophy.
[30:24] If there are any questions.
[30:26] Is it okay?
[30:32] Thank you for this presentation.
[30:34] It's a quick question. I'm not an animator or anything.
[30:37] I see a lot of companies that decide to adapt to Dini for liking, rendering, FX, etc.
[30:44] But animation seems to be an unattainable citadel where workflow will be used for the anime.
[30:52] What's missing to make the transition?
[30:56] To encourage studios to just assimilate?
[31:02] It's a million dollar question.
[31:05] To be perfectly honest, we could talk about this question for a full afternoon.
[31:11] I saw when I went to see the studios to talk about the solution, to talk to them, to have feedback.
[31:20] To be honest, I realize that what's missing the most is that there are artists and designers inside that have touched technology.
[31:30] They can reassure the studio.
[31:33] I think Apex still lacks some features for the moment.
[31:39] But it's not the real end.
[31:41] For me, studios that are scared, Maya has been there for 20 years, it's a big change for her.
[31:51] There are other questions.
[31:54] I have a question.
[31:57] What's the difficulty of installing Apex for the CFX?
[32:02] Is it necessary?
[32:04] I see your system of proxies, of having a ragdoll on the proxies, which is a really bad time for animators.
[32:12] When animators don't animate, it's gone.
[32:15] We need to animate them by hand, and we're not animators.
[32:19] It's true that having Apex rigs on the capes, on the ponytail, is really important and cool.
[32:25] What's the difficulty of installing when you have graphics that don't know each other?
[32:30] Does one person need a person? How long does it take?
[32:35] For the moment, for a team that doesn't know each other, it's a bit long.
[32:38] Apex is still very new.
[32:41] There are few tutorials, and especially on things that are so deep, like creating an animation layer by hand,
[32:47] and making it into a game, it requires a lot of being dedicated.
[32:55] But I think that these things that will be easier to do in the future,
[32:59] for the moment, it's a bit complicated just because it's still new and there's no tutorial.
[33:03] But when I show these examples, I don't show everyone that you have to do things like that in the future.
[33:11] It was a concept test to tell you what you can do, what works,
[33:16] and of course, each production can adapt to its needs.
[33:22] That's great. Thank you very much.
[33:24] Are there any other questions?
[33:26] Great.
[33:33] Hello.
[33:34] Hello.
[33:35] What would you recommend?
[33:37] It's a bit like the first question.
[33:40] What would you recommend for a studio that is deep in Maya today,
[33:47] so that it can go from Apex to discover Apex when you don't know it at all?
[33:54] What would be the first steps to get into the hands of Apex?
[33:57] That's a great question.
[33:59] That's something we could develop on a personal afternoon.
[34:04] I think that if we start tomorrow, we'll have to have our artists who need to be on top of it.
[34:16] The ideal would be to have a small production, a few shots,
[34:20] to break in, and to explore what we can do,
[34:28] to have a free field where artists don't have to run around.
[34:33] You just have to take a shot.
[34:35] You have to have that attitude to explore the solution a bit deeply.
[34:40] That's how Apex shows muscles.
[34:45] If we try to do it exactly like Maya,
[34:47] if we don't have enough time and try to reproduce it,
[34:50] it won't be as interesting.
[34:53] That's a real question.
[34:57] If you had to propose an entry to Apex,
[35:05] would you think of a role that you were dedicated to Apex?
[35:09] I'm taking the question that was very interesting.
[35:11] As an artist, when I was in Arcan,
[35:14] I was able to create this system, of course, not at your level,
[35:18] to answer the artistic demand.
[35:20] In my CFX, I was able to work on Asterix with Muclis and Astier,
[35:24] but we had this very animated CFX.
[35:27] That's how I needed to create similar Apex tools.
[35:32] I thought that it's impossible to take time to do these tools,
[35:36] to take shots, to set up.
[35:38] There are two jobs, three CFX jobs.
[35:41] There's Tidy CFX, there's Apex artist, and there's this CFX user.
[35:45] If you had to carry Apex in full CFX,
[35:49] what role would you be able to play,
[35:51] or would you be able to do shots, or would you be dedicated only to Apex?
[35:57] I think that's the answer that Tamy Toussin gave earlier
[36:01] about how we develop our CFX pipe.
[36:06] Ideally, it would be before a CFX, with a little time,
[36:11] and then, after a shot,
[36:14] we learned that we don't need to touch Apex anymore,
[36:17] it's supposed to roll.
[36:19] In reality, I think it will be done as a measure,
[36:22] with a lead binom, for example,
[36:25] one that is dedicated a lot more to make sure
[36:29] that we focus solely on the CFX,
[36:32] and the other that focuses on the technique,
[36:35] to make sure that everything can be communicated
[36:37] between each artist or each department.
[36:40] I think that it will be done in reality,
[36:43] where you don't really have a technical role,
[36:46] you will be particularly adaptable,
[36:49] and you will also be able to do Apex.
[36:51] But ideally, it would be great to have a guy in front,
[36:55] who is a girl, there's no problem,
[36:58] who takes care of that,
[37:00] and who is dedicated to the technique to make sure that everything works.
[37:04] To go back to the question, and then I'll stop.
[37:06] It's good because it answers the question of how to ensure the studios,
[37:09] the answer is already there,
[37:12] we are able to do the roles, and then we just do it, and it starts.
[37:17] Yes, yes, after, it's a big organization,
[37:21] especially when we do our transition,
[37:23] there will be a lot of broken pieces before it really starts to turn properly.
[37:30] Thank you very much.
[37:32] With pleasure.
[37:37] Hello, thank you for this presentation.
[37:40] I have a question for you, in terms of learning,
[37:44] there are a lot of people who are on Maya,
[37:47] but with this new Apex method,
[37:50] do you think that for schools and students,
[37:52] it will be easier to learn Apex than Maya,
[37:56] even if there is a lot of tutorials on Maya in the future,
[37:59] do you think that new generations will be able to learn the RIC through Apex?
[38:04] I think that Apex is a little less accessible by nature than Maya.
[38:14] Honestly, I think it's worth it,
[38:18] because afterwards we have a lot more power,
[38:20] but we will have to, for example,
[38:23] if we think about schools, as you mentioned,
[38:26] we will have to think about a real progression.
[38:29] First of all, we have to start to touch a little bit on Udini to Kour,
[38:32] to understand how it works,
[38:34] the primitives, the points, etc.
[38:36] And then, after starting to understand how we work on Apex,
[38:39] because that's where it's going to be the most useful.
[38:41] For example, we had seen earlier that there were Apex Graphs.
[38:45] In fact, the Apex Graphs are not just an untouched environment in a corner,
[38:49] it's a network of primitives and points that have attributes.
[38:52] And when the students understand that,
[38:54] they will be able to understand a whole bunch of things
[38:56] and start becoming independent, working by themselves.
[39:00] If we learn Apex first,
[39:03] they will find themselves blocked
[39:06] and only use what we have learned.
[39:09] So there will be a real challenge
[39:11] to know how we learn Apex, if we want to get to that.
[39:15] And there are challenges to be done,
[39:18] and you have to understand them in advance.
[39:20] Thank you very much for this answer.
[39:22] Thank you.
[39:23] Okay, I don't know anything.
[39:25] Wow, a lot of questions.
[39:28] One more.
[39:30] It's a bit in-depth with the previous question,
[39:33] but regarding finding animators,
[39:37] are there certain complexities to this,
[39:39] a certain reticence,
[39:41] let's say, to go to Udini?
[39:44] That's a good question.
[39:46] I was rather surprised.
[39:48] I was expecting animators to be reticent.
[39:51] Animators are quite interesting and curious.
[39:56] I met a lot of people at the Nancy Festival,
[39:59] who were just trying to go to Udini for the animation.
[40:02] There, where there are more fears,
[40:04] people start to have responsibilities
[40:06] because they are afraid that it will break.
[40:08] But animators are quite curious
[40:10] and when they put their hands on Udini,
[40:13] they often fear three viewports.
[40:16] But when they understood that one is the outliner,
[40:18] it's just that it's more visual,
[40:20] the other is more visual,
[40:22] but it's more visual too,
[40:24] and then there's the viewport.
[40:26] They feel quite comfortable
[40:28] and I find new improvements
[40:30] for the Apex interface
[40:32] even more so because animators are comfortable.
[40:34] So not only are they quite curious,
[40:36] but they are quite satisfied when they touch them.
[40:39] That's great. Thank you.
[40:41] Thank you.
[40:42] There are other questions.
[40:44] That's good.
[40:46] Yes.
[40:48] Thank you all.
[40:49] Wait, there's an island!
[40:51] Sorry, sorry.
[40:53] So this question is for you and also for François.
[40:55] When was the first recording?
[40:59] It's nice to ask.
[41:02] There was very little time to prepare it,
[41:05] but a skeleton was already done.
[41:08] There was already a lot of work that had already been done.
[41:11] For example,
[41:13] what is philosophy?
[41:16] What are the exercises?
[41:18] Already some exercises that are already done.
[41:21] For example,
[41:23] now there is really need to make it professional,
[41:26] adapt, rework, rethink.
[41:29] There is a lot of time on it.
[41:31] For now, there is no date that is planned.
[41:33] It's the plan now,
[41:35] and we want to do it as long as it's hot.
[41:37] So we won't waste time.
[41:39] Great.
[41:41] That's all good.
[41:43] Thank you very much Matteo.
[41:45] Thank you everyone.



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
