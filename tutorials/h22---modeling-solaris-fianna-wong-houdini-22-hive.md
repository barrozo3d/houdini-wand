---
title: H22 - Modeling & Solaris | Fianna Wong | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=CFr-1PANhsk
author: Houdini
ingested: 2026-07-19
houdini_version: "22"
tags: [modelling, sop, lop, solaris, usd, cop, karma, instancing, intermediate, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# H22 - Modeling & Solaris | Fianna Wong | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=CFr-1PANhsk)
**Author:** Houdini
**Duration:** 21m41s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro & Overview [0:00]
**Transcript (timestamped):**
[0:00] Hello, good morning everyone. Welcome to the first talk of the Houdini 22 Hive. As Chris said,
[0:17] my name is Fienna, I work at SideFX, and today we are going to look at USD and SOPs, and that
[0:23] you should just do it in SOPs already. So what does that really look like? It's probably something
[0:30] that you're familiar with already, if you have worked in LOPs or Stage, it's the same thing,
[0:37] and if not, then it's okay if you get up and leave. But you can check out SideFX.com to
[0:46] get some more information about Houdini and everything that you can do inside.
[0:50] So I played this, and so with that bicycle scene, we're going to look at a couple of
[0:58] tools that are new in 22 that I used to put it together. Of course, we don't have time to cover
[1:04] everything of 22, but we'll look at quad-remesh, and if you've seen my past presentations,
[1:10] yes, I'm still covering quad-remesh because there was something new, and yes, it's still in beta.
[1:16] We'll also look at scatter instances, sculpt, implicit surface, texture material library,
[1:22] and some new USD SOP nodes. Also, if you notice the color coordination, it's a big clip down there,
[1:28] but basically orange stuff is SOPs and green is LOPs. So what do we usually do when we need to go


### Image-to-3D Asset Sourcing [1:35]
**Transcript (timestamped):**
[1:36] make something? We look at references. So here are some of the references that I looked at when I
[1:40] thought like, I talked to Development and they're like, we're going to do these things, and I thought
[1:44] what would be cool to make use of those? And I thought a bike shop because
[1:49] namely, I have an asset already, the bike, and then I wanted to put some tools to the test.
[1:56] So with making a bike shop, it means we need to fill it up with a whole lot of assets, and these
[2:02] are just some of them that I went shopping and looked up some images of bins, screws, workbench,
[2:12] power outlets, and such. And not everything made it into the scene, but basically the approach that
[2:20] I went with using image 2.3D conversion, which I use Minocchio. If you don't know what that is,
[2:28] it's just, you can look it up after and install it, but you just take an image, any image,
[2:34] and you put it through this interface, and it gives you this 3D mesh, which generally is garbage,
[2:40] but it allowed me to easily make decisions about what I want to have in my bike shop or not,
[2:47] and I didn't have to commit to building the whole thing from start to end, and then I end up with
[2:52] some assets, and I'm like, well, this doesn't really fit, and I have to keep it somewhere in
[2:57] the back and maybe use it one day. So with this process, I had a lot of stuff that I've been,
[3:05] and the stuff that I did keep, I put it through the Quadremesh, and it's too advanced, like it's
[3:13] too much to call it like a pipeline, but it's just like Quadremesh, a couple of notes to process it,
[3:21] to give it UVs, and then you end up with a usable, like a working asset. So with Houdini 22, if you


### Taming CAD Meshes with the New Quad Mesh [3:27]
**Transcript (timestamped):**
[3:28] guys were on the keynote yesterday, there were some examples of hard surface, like CAD type meshes,
[3:35] and basically what you need to know is that the new method rectangular allows you to process
[3:42] such a type of mesh with better results. But that's not to say that the previous existing method,
[3:51] which was in Houdini 21 uniform, like it's discarded, it really just, there's only two
[3:58] modes, right? So whatever mesh you have, just like try the two, because you'll find the one that
[4:05] gives you the better result. And here is a like walkthrough of some of the assets that I put through
[4:14] this pipe of image to 3D Quadremesh, some kind of like cleanup, and a bike bench,
[4:29] this like wheel walking mechanism that you put on that. And this one actually was a CAD file,
[4:38] which also had like bas surface topology, the normals were flipped. So I also ran it through
[4:43] the Quadremesh. I also put some power outlets. And basically the main takeaway is you kind of
[4:50] don't need reference images anymore, because if you put it through this process, you get everything
[4:55] with the right proportions, which kind of more or less is what you care about. If you want to go back
[5:01] and clean it up, rebuild it properly, so it's like more optimized, you can do that. But if you
[5:07] want to just jam a bunch of things in a scene, see how it fits, this is a really like cool,
[5:14] flexible way to do that. Here's a closer look at the process. I have an image, I input that into
[5:21] the Pinocchio, you get this garbage mesh, it's very dense, but the proportions are there.
[5:29] And the middle is a close up of the mesh, which is totally not usable.
[5:37] As with all Quadremesh, you always want to append a remesh node, because Quadremesh doesn't like
[5:46] irregular shapes. You want to always have like a uniform mesh, regardless if it's just like a
[5:51] bunch of triangles, you'll get like happier results. And when the developer told me, hey,
[5:58] I have this new like rectangular method, you should try it. I got the screw and I had very
[6:03] low expectations. I put it through and it was just like, I don't know, it's like two seconds or three
[6:08] seconds, bam, like this thing with the interior shape, everything like looked as it should. And
[6:15] I was amazed. Here are some different angles of it. Of course, it's not as perfect as if you were to
[6:23] retopulate by hand. But for the amount of time that you put into like try make this asset,
[6:30] clean it up, it has this weird interior like gap that shouldn't exist. But this is like a small
[6:38] tax to pay if you just delete the interior geometry and then just select the actual loops top and
[6:43] bottom polyfill and call it a day. After that, you put it through the auto auto scene. Unwrap
[6:54] it with UV flage in UV layout to lay it out. And then you can bring it into Copernicus to


### Scattering Screws & Karma Rendering [7:00]
**Transcript (timestamped):**
[7:01] generate some materials. And you can even use it in the scatter instances, because I had in mind
[7:08] that I wanted to kind of litter the bike shop with a bunch of screws and like random things. But
[7:17] I ran out of time. But you can see here that I've taken just two assets, or maybe you don't see
[7:24] that because it has such a variety of different scales and rotations and positioning. So it's
[7:32] really as simple as just in this case, I have two assets, these two screws, they're wrong proportions,
[7:38] I don't care. I just modify it and edit position it close to the ground. So I don't have some like
[7:44] offset. If you want an offset, then you know, just leave it. After that, I applied the materials I
[7:50] created from cops and made a shader, applied it to those playing too fast. I applied it to one of
[7:58] the screws. And then I have this configure primitive, which just hides these imported
[8:05] meshes because you don't want them to show when everything instances. And then I have this room
[8:10] where I want to scatter them. And then here is the scatter instances interface where you can just
[8:15] change the number of instances very easily, put what prototypes, which are those screws. And of
[8:21] course, you can have much more than two, you can decide what kind of distribution, the weight that
[8:26] you want to apply one more than the other. And you can just kind of tweak to your heart content,
[8:34] the scale, the orientation, how many you want rotations and everything like that.
[8:43] So one more thing to know just if it wasn't apparent already, this only will appear at
[8:50] render time. So if you're in Vulkan, you're just going to see your like two assets or
[8:56] whichever one that you're looking at. The instances will only appear when you're using
[9:01] Karma XPU or CPU. And because it's only a render time thing, Houdini doesn't really know like
[9:12] this is a geometry. So you will get interpenetrations. And to resolve that, you can just
[9:18] use the relax iterations and tweak it until you get something that works in your camera frame.
[9:23] Okay, next is sculpt. There's nothing mind blowing new here, but just some new additions to help with


### Sculpting Workflow & Quick UI Tweaks [9:25]
**Transcript (timestamped):**
[9:31] your workflow. And that is just a simple G key to bring up a toggle menu, like a floating menu.
[9:39] And you can access all of the sculpt controls, brushes and everything. Put it away when you're
[9:45] done. You can also set values more than the usual range of zero to one using the mouse and
[9:54] keyboard combination. So in three, I applied a strength of and there's also a lazy mouse
[10:04] visualizer, which again, like it's nothing rush shattering. But if you have some mechanical surface
[10:10] that requires tracing along an edge, it's much more visible to see now.
[10:18] And yeah, as I said, this is just minor improvements to help just make things easier,
[10:28] because otherwise you would have to keep a window open, change stuff there or change
[10:32] things up at the top. And everything kind of is at your mouse fingertip, if you will. So here I have
[10:39] the version that I sculpted back in details, because when you put things through the image to
[10:44] 3D conversion, you get the proportions, but everything kind of gets softened and you lose the
[10:50] detail. So using the sculpt is one way to add them back. Next is the implicit surfaces, which I'll


### Fast Booleans via Implicit Surfaces [10:57]
**Transcript (timestamped):**
[10:58] call them cheapo bullions with quad mesh automatically. I use just these three nodes,
[11:05] implicit surface with some basic geometry options, implicit surface operation to do my
[11:11] bullions and then the convert to get it into something usable. And it looks something like this.
[11:18] So I start off with a box and regular box and a tube. I copy it a bunch of times. I do my operation,
[11:28] the Boolean and I convert it and everything is a quad. And you're saying, okay, but I got
[11:35] bullions, I can do that. And I can do that with precision. Yes, you're not able to get like,
[11:41] super crazy accuracy with this, but this asset is somewhere in the distance. I don't have to see every
[11:49] like millimeter of a curve. And that was enough. And it was quick. The next is texture material
[11:55] library. So the main takeaway from this is you can now author all cop nodes inside that you don't


### Texture Material Library & Live COPs [11:56]
**Transcript (timestamped):**
[12:04] have to create a cop net, you don't have to pin a window, you don't have to like op point to something
[12:10] else. You just make that and you put your cop nodes in. So to continue with this breadboard thing,
[12:21] I just bring it in with the UVs. I apply some colors and noises, grunges and stuff. And I'm happy
[12:30] with how it looks. So I can just write it out as a texture. You can of course keep it live.
[12:35] But in my scene, I got so many assets and at different resolutions, I don't, I don't want to
[12:41] put my computer to undo string. And so with some of this like image to 3d process and additional
[12:52] modeling, I also have this resource of polyhaven, which if you don't know, you should it's got a
[12:58] huge repo of hdri materials and assets that are ready to use. And they're creative commons license.
[13:07] So you can use them for commercial as well as personal, of course. So go there if you don't know.
[13:14] And those were all the assets that I put into the scene. And now that takes us to like, I want to


### Organizing USD Hierarchies Directly in SOPs [13:18]
**Transcript (timestamped):**
[13:20] get something rendered, but I never quite got this USD thing. And should I just see an import all
[13:28] and stick it all in there, which is not the really thing, the thing that you should really do,
[13:35] or do a bunch of sub imports, sub creates and then merge everything anyway.
[13:42] I had to do some stuff in sops. And then I kind of have to do similar things in,
[13:48] in stage or lobs, the same thing. Like you're wondering, why do I have to do everything twice,
[13:54] kind of. So I'm happy to introduce two small and mighty nodes that are in 22, which aren't sops.
[14:03] And these two guys will help you define the structure like your USD hierarchy from within sops,
[14:11] which is kind of like a more familiar place. And here is what it looks like. I'll explain it a bit
[14:20] further, but just to show you the interface, it's really two things that I cared about or that I used,
[14:26] which were setting the kind, everything I said is a sub component within the bike shop. So it's
[14:32] like an umbrella of the things. And then everything I did in terms of transform rotation and scale,
[14:39] I did also all within this, like each USD create component nodes. So every asset I had,
[14:46] I would tag it with the USD create component. Because otherwise, you know, you put a bunch of
[14:51] transforms, you put a bunch of edits, and then you forgot like, Oh, this one did what that and the
[14:55] other multiplied like 50 times. And then you have this like rat nest of network. So this will help
[15:02] keep your scene tidy and sane. And then the USD parents geometry, if you like are using multiple
[15:10] of these assets, you want to just like organize them and plug them in under one other umbrella,
[15:16] you do so with that. And it looks like this. So I have a stash node at the top. That's where I
[15:22] did all this quadrimesh pre processing from the image to 3d. And I baked it out with UVs and
[15:28] everything imported the one file. And then I wanted four workbenches. So I just made four of them.
[15:35] And for each, I positioned them individually, then put them in a USD parent geometry and then a
[15:41] no. So it looks something like this, where I already placed other assets in the scene. And
[15:50] the my workflow is that I brought everything as much as possible to their final position
[15:57] in SOPs. So any sort of rotation and translation, I actually had to redo a bunch of these because
[16:05] I saw like all the mess that I had. And I applied back all the transforms and rotations and scale
[16:11] to each of these USD create components. Also, if you're thinking, well, yeah, Fienna, you're saying
[16:22] it's like lightweight, but it's like 12 frames per second. What's up with that? Well, I didn't
[16:27] optimize any of the geometry that I pre processed with this image to 3d. There were like, this
[16:34] like power outlive was like, I don't know how many million faces. But I just wanted to jam things
[16:39] into the scene to see if they would work. And then I can always go back afterwards and optimize my
[16:45] geometry. So here is what the scene looked like. And it looks like a lot, but it's not.


### Putting the Bike Shop Together [16:49]
**Transcript (timestamped):**
[16:54] You'll see these like blue notes everywhere spring. The green stuff was polyhaven. And
[17:01] everything else minus the blue were the quadrimesh items or hand models. And so
[17:08] the blue stuff was just object, object merges where I point to each of the nulls. And I set up
[17:15] in this case, three structures. And it looks like this when I bring them into Lops, it's kind of
[17:21] tidy. I have my three main parts like the bike shop, I have, I can get already skipped that part,
[17:29] the stuff in the room, like the room geometry, and then I have like posters and some license plates.
[17:35] And everything is kind of organized within that. If I want to move anything, I just go do it in
[17:40] SOPS. And I, oops, and I, I hope that gives me an idea of the, like blurring of the borders between
[17:55] SOPS, like working in SOPS and Lops and Copernicus to make an idea come about in Houdini. Thank you.
[18:10] There's no time for questions.


### Q&A: Implicit Surfaces vs. Traditional Booleans [18:12]
**Transcript (timestamped):**
[18:15] Check. Any questions?
[18:21] Viana's wrong, we do have time.
[18:24] Unfortunately, I can't see any hands because I'm in the dark, so too bad.
[18:30] Any questions?
[18:34] All good?
[18:34] Okay.
[18:35] Nice work, Viana.
[18:36] Thanks.
[18:37] Oh, one.
[18:41] Over there, yeah.
[18:42] Good. Hold on.
[18:47] There are forward lights.
[18:57] What is the advantage of implicit surface and in comparison to boolean?
[19:03] So you, you get the automatic quad generation, like the quad mesh generation in that.
[19:12] It's just the, like when you do the final convert, it just outputs a quad.
[19:17] So you get the boolean, but it's, I'm going to say something wrong, so I won't say it, but whatever
[19:23] it is that you're doing as an operation within places surfaces, it doesn't care about your
[19:28] resolution of the mesh. It's not a mesh. So with booleans, it is mesh and you end up usually with
[19:36] all this like long slivers and triangles and things. It's like hideous geometry.
[19:41] Also, it's like can be slower or you get some bits that kind of goes into itself.
[19:48] It's just kind of more lightweight and cleaner, but it's less precise.
[19:54] Oh, I see.
[19:55] Like you have to do an additional operation of like another quad remesh,
[19:58] which I know I was raving about quad remesh and everything. Yes, it has its place, but
[20:02] for me, I don't want to, it sounds stupid, but like if I see that it's kind of like an ugly mesh,
[20:08] then I will have a compulsion to go clean it up. Whereas with the implicit surface, it did the job
[20:14] and it's quad and I can just like get some seams and unwrap it, get the UVs and call it a day.
[20:24] I can show you after if you want.
[20:27] Can I ask one more question? So about you said the whole point of bringing
[20:31] the component, the component into soft is not to repeat the whole process.
[20:38] Then what about do you assign the materials in soft as well?
[20:43] No, you do that in box.
[20:47] Okay, but because in the view point that you showed, you are in softs moving the tables around
[20:53] and when where does the material come from? Eagle eye. So I wanted to get into this,
[20:58] but I was advised not to, but I plan to do a video after the release to explain my own preference
[21:06] that I would like to see textures in the viewport and actually download a GLTFs from Polyhaven.
[21:11] So they automatically load with a texture as opposed to USD, which sounds like counter,
[21:18] we author USD, so it should, but it didn't load the textures automatically and I just
[21:24] wanted something quick and it worked. Okay, thank you very much. Cheers.
[21:31] Okay, anyone else? Goodbye. Good job, Hannah, thank you.



---

## Captured Frames

- [5:21] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_000.jpg
- [6:08] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_001.jpg
- [8:15] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_002.jpg
- [9:39] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_003.jpg
- [11:18] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_004.jpg
- [12:21] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_005.jpg
- [15:35] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_006.jpg
- [17:21] tutorials/frames/h22---modeling-solaris-fianna-wong-houdini-22-hive/frame_007.jpg

---

## Structured Notes

### Core Technique
Houdini 22's SOPs-first USD scene assembly: image-to-3D asset sourcing cleaned with the new rectangular Quad Remesh, render-time Scatter Instances, implicit-surface booleans, the Texture Material Library with embedded COPs, and the new `USD Create Component` / `USD Parent Geometry` SOPs that author USD hierarchy without leaving SOPs.

### Summary
Fianna Wong (SideFX) builds a bike-shop scene to showcase H22 workflows that blur SOPs/LOPs/Copernicus boundaries. Assets are sourced by feeding reference photos through image-to-3D ("Pinocchio"/Meshy-style — output is dense garbage but correctly proportioned), then Quad Remesh — always with a Remesh appended first — using the new **rectangular** method for hard-surface/CAD shapes (try both modes; uniform still exists). Screws seconds-fast retopo with correct interiors [frame_000/001]. Set dressing uses the **Scatter Instances** LOP (prototypes with weights/scale/rotation distributions — render-time only, visible in Karma XPU/CPU not Vulkan; fix interpenetration with relax iterations). Booleans come "cheapo" via Implicit Surface → Implicit Surface Operation → Convert (resolution-independent, all-quad output, no sliver triangles — less precise, fine for background assets). Texturing lives in the **Texture Material Library** which now hosts COP nodes directly (no separate copnet), written out as textures for heavy scenes. The star: **USD Create Component** (per asset: kind = subcomponent, plus its transform) and **USD Parent Geometry** (grouping under umbrella prims) define the USD hierarchy in SOPs, so the LOPs side arrives tidy; final placement is done in SOPs via object merges of nulls.

### Key Steps
1. **Image → 3D sourcing** [frame_000, 5:21] — run reference photos through an image-to-3D tool; dense unusable mesh, right proportions — enough to try assets in a scene without committing to building them ("you kind of don't need reference images anymore").
2. **Quad Remesh (beta) with new rectangular method** [frame_001, 6:08] — always append a **Remesh** first (Quad Remesh dislikes irregular input); rectangular mode nails hard-surface/CAD meshes (screw: 2–3 s with correct interior; delete stray interior geo, PolyFill top/bottom loops); UV Flatten + UV Layout after; uniform mode remains for organic shapes — try both.
3. **Scatter Instances** [frame_002, 8:15] — LOP scattering with prototype groups + weights, count, distribution, scale/rotation ranges; **Configure Primitive** hides source meshes; instances exist only at render time (Karma XPU/CPU) → Houdini can't collide them, use **relax iterations** to fix interpenetrations in frame.
4. **Sculpt QoL** [frame_003, 9:39] — **G-key floating menu** for all sculpt controls/brushes; values beyond 0–1 via mouse+keyboard; lazy-mouse visualizer for tracing mechanical edges; used to re-add detail the image-to-3D softening lost.
5. **Implicit-surface booleans** [frame_004, 11:18] — Implicit Surface → Implicit Surface Operation (boolean) → Convert: quad output automatically, no mesh-resolution dependence, no sliver triangles; less precise — perfect for distant assets (pegboard from box + copied tubes).
6. **Texture Material Library + COPs** [frame_005, 12:21] — author COP nodes inside the material library (no copnet/window pinning); colors/noises/grunges on the UV'd asset; keep live or bake to texture files (bake for many-asset scenes). PolyHaven (CC0) fills the gaps; GLTF downloads load textures in the viewport automatically, unlike USD.
7. **USD hierarchy from SOPs** [frame_006, 15:35] — per-asset **USD Create Component** (kind: subcomponent under the bike-shop umbrella; put final translate/rotate/scale *on this node*, keeping the network sane) and **USD Parent Geometry** to group (4 workbenches → "workbenches" parent → OUT null).
8. **Assembly** [frame_007, 17:21] — object-merge the nulls (blue), three top structures (bike shop / room / posters+plates); LOPs receives a tidy scene graph; to move anything, edit in SOPs. 12 fps viewport = unoptimized image-to-3D geo (a power outlet was millions of faces) — jam first, optimize later.

### Houdini Nodes / VEX / Settings
- Quad Remesh (beta): **rectangular** (new, hard-surface/CAD) vs uniform; precede with Remesh; PolyFill for interior cleanup; UV Flatten + UV Layout
- Scatter Instances (LOP): prototypes, weights, distribution, scale/orient ranges, relax iterations; render-time-only (Karma XPU/CPU); Configure Primitive to hide prototypes
- Implicit Surface / Implicit Surface Operation / Convert — resolution-independent quad booleans
- Sculpt: G floating menu, >0–1 values, lazy-mouse visualizer
- Texture Material Library: embedded COP authoring, bake-to-texture
- New USD SOPs: USD Create Component (kind, transform per asset), USD Parent Geometry (grouping)
- Sources: image-to-3D tool, PolyHaven (CC0; prefer GLTF for auto-loading viewport textures)

### Difficulty
Intermediate

### Houdini Version
Houdini 22 (rectangular quad remesh, Scatter Instances, sculpt QoL, Texture Material Library COPs, USD Create Component / Parent Geometry)

### Tags
modelling, sop, lop, solaris, usd, cop, karma, instancing, intermediate, houdini-22

---

## Related Tutorials
- [Messing with the Edit node in Houdini 22](messing-with-the-edit-node-in-houdini-22.md) — physics-based placement of the assembled assets in LOPs (Edit node physics mode)
- [Intro To Houdini Solaris - Full Beginner Course](intro-to-houdini-solaris---full-beginner-course.md) — the LOPs foundations this SOPs-first workflow feeds into
- [Houdini tips : Solaris, VDB's , COPS and More](houdini-tips-solaris-vdbs-cops-and-more.md) — component-builder and COPs tips in the same territory
