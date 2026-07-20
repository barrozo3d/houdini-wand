---
title: H22 - Copernicus and Time Shift | Jakub Spacek | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=EUjZ7ObaN1Y
author: Houdini
ingested: 2026-07-19
houdini_version: "22"
tags: [cop, procedural, simulation, solaris, karma, advanced, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# H22 - Copernicus and Time Shift | Jakub Spacek | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=EUjZ7ObaN1Y)
**Author:** Houdini
**Duration:** 24m8s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro & Adjacency Workflows [0:00]
**Transcript (timestamped):**
[0:00] Thanks to all of you who are here today!
[0:03] Thank you guys so much for staying awake, thanks to SideFX for having me again, especially
[0:12] Fianna who brought me into this collaboration which is really great, I'm happy to be able
[0:17] to do this.
[0:20] Yeah, what we'll be talking about today.
[0:24] So we'll be talking about adjacency workflows.
[0:28] There were a few other things I was exploring
[0:31] since I started working on this collaboration.
[0:34] I had a certain chunk of time to create this.
[0:38] And originally, I had much grander ideas
[0:41] about how to mix it in with also the machine learning.
[0:44] I'll mention it later as well.
[0:48] I was lucky to have a support on the SideFX Slack
[0:51] from Jeff Lead and also Jakob Pringler,
[0:55] who were working me through some of the things
[0:57] and pointing me to maybe paths that were not as clever to do.
[1:04] So yeah, and originally, when I started working on this,
[1:08] I was using the Houdini Pig Head,
[1:10] which is very simple geometry.
[1:12] It has relatively nice UEs.
[1:14] But then I realized it would be cool to stress
[1:16] these adjacency workflows on geometry
[1:20] that is far more complex, doesn't have UEs,
[1:23] and it would kind of push me to figure out
[1:26] maybe where are the issues people can come across this.


### Mesh Cleanup & UV Optimization for Copernicus [1:31]
**Transcript (timestamped):**
[1:31] So let's start.
[1:32] Good is it of 3dscans.com.
[1:35] I found this lovely statue, and it
[1:38] comes in like triangulated, very dense, not really clean mesh.
[1:44] I just scaled it down in the scene.
[1:46] And find some pose that would work for me in the zero position.
[1:51] And then using the quad-remesh, I created some relatively low
[1:58] poly compared to the original, but still high enough
[2:01] to have good density and remain the detailed geometry.
[2:08] So the first step was to create some arbitrary UVs.
[2:11] In this case, I used UV Unwrap, which gives me
[2:14] this basic layout.
[2:16] And it sort of works.
[2:19] One of the things that I realized working in Compernikus
[2:22] is that you really want to utilize the UV space that the layout gives you.
[2:27] So here, if I would be using the UVs as they are
[2:31] and creating all the intricate detail,
[2:34] it would be so tiny that it would be sort of
[2:37] frustrating to allow resolution even when I was using 4K to 4K space in the Compernikus.
[2:48] So jumping ahead a little bit, working in Compernikus
[2:51] and assigning different noises.
[2:55] I was getting this issue, which was really bugging me,
[2:57] and I couldn't figure out where is these imperfections coming from.
[3:02] And later on, I realized that it must be some of the UV islands
[3:07] being overlapped.
[3:08] That's one of the things you wouldn't have to deal with
[3:11] if you manually create nice UVs
[3:14] or you would have someone who was creating a perfect UV layout on a geometry.
[3:19] And luckily, Houdini does have from Labs, it's a lab note.
[3:25] It isolates the overlapping islands and sort of distributes them into your layout
[3:30] so you can avoid this issue further.
[3:36] And then to properly propagate the UV islands, I used the UV layout,
[3:41] just enable spread islands to all available space
[3:45] and it gives me this relatively good sort of distribution.
[3:51] So one note at this point, because further we will be working with the adjacency notes,
[3:57] the gap between the UV islands will essentially give you
[4:04] how much space you have before a certain operator will cross the boundary.
[4:09] So it's good to have some gap between the islands,
[4:13] but in this case, I left it as tight as possible.
[4:17] So I would be potentially avoiding more issues and stress testing the setup.


### Flattening Geometry & Sourcing Color Points [4:24]
**Transcript (timestamped):**
[4:24] So next step was to flatten the geometry into UV space.
[4:29] The reason for this is in my mind, I wanted to spread sort of
[4:34] dips of paint on the statue from which the spreading would be happening.
[4:38] So in this case, I'm sort of flattening everything
[4:41] and then using simple scatter to give me some sort of color information.
[4:48] I'm using simple expression and also matching the changing ID for the color.
[4:56] So this is the layout before it goes into Copernicus and then I created just, you know,
[5:03] Copernicus and start having into it.
[5:05] As you can see, the UV is really bad, but the adjacency notes that are coming in Houdini 22
[5:11] will crunch through it just fine.
[5:16] So we bring into Copernicus, I bring in the points in the flattened UV space
[5:21] and also the geometry.
[5:25] We have the preview on the 3D geometry and I'm just using
[5:29] standpoint to essentially scatter like a simple circle on the statue.
[5:38] And this is essentially the adjacency notes that are coming in.
[5:44] The one I didn't get to use was the adjacency space transform.
[5:49] Other than that, I had a chance to test everything else.


### The Geometry to Adjacency Packed Cable [5:53]
**Transcript (timestamped):**
[5:53] Not that it's not useful, but in this case, I just didn't have a really use for it.
[6:01] So let's bring the adjacency in.
[6:03] We have our geometry coming in and geometry to adjacency will give us this information.
[6:11] In a nutshell, it is a packed cable with much more fields.
[6:16] And in general, I would recommend doing a little bit of research on how cables work in Copernicus.
[6:23] It's really useful, especially if you'll be working with blocks or other solvers.
[6:29] So here you can just bring in cable unpack and when you click the set fields from input,
[6:34] it'll give you all this information you can later on work with.
[6:40] So let's have a look how we build this spreading effect that will essentially drive
[6:46] everything else in the whole simulation.
[6:49] Now I'm going to make one pro tip by complete accident.
[6:55] If you press X when you're in Copernicus, it will switch between flattened view and 3D preview view,
[7:04] which doesn't seem like a big deal.
[7:05] But if you have a large network, it's such a pain free way to preview between those two super useful.


### Custom Solvers & Procedural Paint Spreading [7:15]
**Transcript (timestamped):**
[7:15] So this is the custom solver that's driving the spreading.
[7:22] In this talk, I will not be diving too much deep into how block works.
[7:27] There's better tutorials on that, especially here from Alex as well or Jeff Lee at online.
[7:34] So for all purposes, I'm just using the incoming color, which is our BGA with alpha, those are the yellow inputs.
[7:43] And then we have the pass through where we're feeding in the adjacency.
[7:49] The naming and indexes is arbitrary.
[7:53] You can name it whatever you want.
[7:55] You just need to set the fields properly.
[7:57] So the green ones are cables.
[8:00] So they are passed through on each iteration, in this case, each frame.
[8:05] So we don't need to recalculate them.
[8:08] And there are not changing adjacencies, not changing every frame.
[8:11] So this way we will save computational time.
[8:15] And as an overview, it's just about each frame.
[8:19] We will add the sourcing color that is dipping onto the statue.
[8:23] And then by using slope direction and adjacency distortion, we'll achieve this sort of spreading noisy effect.
[8:32] So if we look at the most simple portion of this solver,
[8:39] it would be just the circle shape that is spreading outside, thanks to the slope direction.
[8:45] And the adjacency distort already takes care of bridging the UV islands just fine.
[8:52] But this would be relatively boring effect.
[8:54] So we want to bring in some noise.
[8:59] As you can see, it's not properly mapped.
[9:02] So in this case, the adjacency distort at the very end would still correctly bridge the islands without seams.
[9:12] But the way the distorted color is happening would be sort of messed up and crippled by this incorrectly mapped noise.
[9:22] So this is where we want to use adjacency attribute sample.
[9:26] By default, it is sampling position attribute.
[9:30] And this way, we can feed it into the noise and map it correctly.
[9:37] So now the incoming value that's going into the slope direction is distorted.
[9:43] And instead of getting sort of like a boring circles, we're having nice organic pattern growing outside.
[9:51] Because we are working in RGBA with alpha, we are previewing the overall area of influence.
[10:00] So if we want to preview how things are going to be blending together, we just need to multiply it with the alpha.
[10:08] And this is the resulting effect.
[10:11] So next step for me was I wanted to mix up the colors a little bit.
[10:16] And for this, I just used the information itself to offset some values in saturation and hue shift.
[10:25] So I'm essentially remapping value from minus 180 to 180.
[10:30] And over time, it's creating this lovely effect of really bright and juicy colors.
[10:37] We also have the alpha that's coming from the setup and the overarching clipping mask.
[10:43] And all of these things will be later used in the material of building the final effect.


### New Time Manipulation Nodes in COPs [10:50]
**Transcript (timestamped):**
[10:50] So next step, I wanted to create some kind of like a leading edge for this effect.
[10:57] And originally, I built like a solver again, and I was doing some dissipation over time.
[11:02] And then I realized, great, Houdini 22 is coming with some time manipulation notes, which is really useful.
[11:08] So I just offset it the frame by 10 and subtracted it from the original map.
[11:15] And this way I get this really nice sort of leading edge effect that would drive other effects later on.
[11:22] Speaking of the time manipulation, we have time shift, time blend and time loop.
[11:28] Essentially, it works like a, you know, soap level operators.
[11:32] And in this way, you can potentially hold first and last frame or loop the animation and sequence.
[11:39] And I think it'll open up quite cool, you know, things we can do in Copernicus later on in combination with solvers and other stuff.


### Seamless Blurring Inside Blocks [11:52]
**Transcript (timestamped):**
[11:52] So now I'm going to talk about blurring.
[11:54] And I think there was one question earlier today about blurring.
[11:58] So obviously, I have my edge and I want to do some masking, multiplying and then creating maybe more delayed effect of this leading edge.
[12:06] So if I just blur it out of the box, the blur node will cross the boundaries of the UVs, not respecting any sort of adjacency.
[12:16] But we can bring it into block and utilize the adjacency in a way to solve this issue.
[12:23] So essentially, you need to find small enough value for the blur not to cross the boundary.
[12:31] And then by using certain amount of iterations in your block, you can find the value that you wanted to originally achieve.
[12:40] So in this case, it's like 500 iteration, but I don't know, it was like four seconds for it to cook.
[12:47] So it's not that crazy.
[12:50] And this way, I was able to multiply, subtract, do some basic operations.
[12:56] But every time I needed to blur something, I had to put it in a block and do this sort of process.
[13:01] So it is a little bit like annoying, but it's not that expensive in computational time.
[13:08] It's just a blur.


### Turing Patterns & Ripple Solvers [13:11]
**Transcript (timestamped):**
[13:11] And then originally, I had this idea to create some sort of reaction diffusion effect that's sort of following this color spreading.
[13:20] And by complete accident early on in exploration, I came across this Turing pattern courtesy of Alex here.
[13:29] It's really fun. It's similar to reaction diffusion, but it works slightly different and you can achieve different results as well,
[13:36] depending on what color information is going into it.
[13:40] You have some options that I set the way I need it to be.
[13:45] And essentially, we are passing through the adjacency again that goes into the adjacency.
[13:52] And I'm using the spreading mask information to mask the Turing pattern so it doesn't spread beyond the mask.
[14:03] Because with a lot of iterations, it could grow quite quickly.
[14:06] So we just wanted to keep it in the area of interest.
[14:10] Just out of curiosity, reaction diffusion and some other solvers in Copernicus do have adjacency embedded in it.
[14:18] So you can utilize it and as you can see, you will have no issues with any UV seams.
[14:29] And again, I wanted some more exciting colors.
[14:32] So I used the same principle just offsetting the hue shift and saturation.
[14:36] And then I went to testing ripple solver.
[14:40] So now you can do kind of like in SOAP level, you have the ripple solver here.
[14:47] It works really well. It computes fast.
[14:50] The only change I needed to do because usually ripple solver works with like initial value that starts sort of rippling away.
[14:58] I'm just using add to add the leading edge each frame.
[15:03] So I'm kind of sourcing new repos as the spreading effect happens.
[15:08] And because I'm adding each frame, I want to clamp it so we don't go above the value of one.
[15:14] There are some basic settings that I adjusted, you know, conservation waves and spring.
[15:19] So I have the effect roughly how I would imagine it to dissipate.
[15:25] And at the end, I wanted some sort of sort of dissolving effect that would bring the color back into its original simple plaster material.
[15:36] I was doing some again, like a solver and then I realized I can just invert the original animation and it's going to give me this nice blending effect.
[15:45] Now, honorable mention.
[15:48] Nikola was talking about the grunge notes.
[15:51] I'm super excited about it because these are the presets I was always dreaming of having.
[15:56] And now, you know, all of us can use materials and no material will be the same.
[16:01] You can allow editing and dive inside and because they are built by, you know, Copernicus native noises,
[16:11] you could re sort of match them with adjacency notes.
[16:15] So this way you can have like seamless, you know, grunge textures for any object.
[16:21] In this case, I haven't done it because there's quite a lot of steps for every one of these notes.
[16:28] So I just I just faked it and used like an adjacent material, but it was such a small detail and I mixed it up with some MTLX material noises that you can really see and it seems anyway.
[16:43] And then I brought it into Solaris.


### Lookdev in Solaris & Dynamic ML Growth [16:47]
**Transcript (timestamped):**
[16:47] So it's straightforward setup on camera objects in Material Library.
[16:53] We have three materials for each of the objects and I'm using Linker to sort of assign them same with lights.
[17:00] Material Linker, you know, assigns lights for specific objects or excludes them.
[17:06] So I have the lighting exactly as I want.
[17:08] And aside from some minor issues, I had really fun time working with Karma and Solaris.
[17:16] So I would love to explore it more.
[17:18] Yeah, here's a little sneak peek into the material layout.
[17:23] And as Fianna mentioned earlier, you will have, you know, access to everything in the hip file.
[17:28] So you can kind of explore it.
[17:30] I'm going to go over the material.
[17:31] It's pretty much the same as, you know, redshift or octane principles.
[17:37] And here's one more time, the overarching simulation.
[17:41] Originally, I wanted to figure out a way how to sort of separate the spreading effect by ID for each of the colors.
[17:52] And then each of those spreading islands would have like machine learning pattern growing on top of them.
[17:57] But I was a little bit naive on how much time all of that would take.
[18:02] And speaking of machine learning, I'm going to point to Jacob's presentation again.
[18:07] He mentioned the adjacency there.
[18:10] But just as like a little example, you can just, you know, use a simple pattern,
[18:15] train it with the default values and you will get something like this.
[18:21] And as you can see, the preset already has the adjacency input in it.
[18:25] So you can just feed your adjacency and using the spreading mask in a mask by update,
[18:37] you can affect the ML training so you can get this gradual effect.
[18:43] It's pretty exciting.
[18:45] And that's it.
[18:46] So thank you guys.
[18:48] And yeah, any questions?
[18:51] That's lovely.


### Q&A: Texture Caching & Handling Bad Topology [18:54]
**Transcript (timestamped):**
[18:56] Okay.
[19:11] Thanks, Jacob.
[19:12] Great presentation.
[19:15] I was wondering, there is some way to bring inside the block the time shift and use it as maybe some sort of time displacement as in After Effects or something like that.
[19:30] That's actually a good idea.
[19:33] I haven't tried it, but I would imagine you should be able to do that.
[19:39] So yeah, maybe maybe I'll do a test with that as well.
[19:42] It's a good idea because you could potentially loop maybe with the source of the of the color or whatever you would work with.
[19:52] Yeah, that's a good idea.
[19:53] Okay, cool.
[19:54] Thank you.
[19:59] Somebody else.
[20:06] Did you have to bake any of the texture or are you reading them live from cop?
[20:12] That's a great question.
[20:13] I had to bake everything because in 4k, it's massive.
[20:19] Yeah, it is heavy.
[20:22] I think someone here earlier was explaining the unloading the cache for Copernicus.
[20:27] So that's something I also had to figure out.
[20:30] I had a lot of crashes before I realized that.
[20:33] Luckily, I had like almost 400 gigs of RAM, but even with that, it was, yeah, it was pretty, pretty.
[20:40] Like everyone else.
[20:42] Yeah, exactly.
[20:45] Just flexing, you know.
[20:52] Did anybody have any other questions?
[20:57] Okay.
[20:59] There's one in the back in the darkness.
[21:09] Thank you.
[21:10] So I was just wondering why do you have to qualify the topology?
[21:13] Why do I have to qualify the topology?
[21:19] If I remember correctly, when I left it in the triangulation, there were some areas that
[21:25] were like so dense and messy that the UV unwrap was giving me some sort of like issue.
[21:32] Or maybe it, I think it was like cooking until it crashed.
[21:36] So I think that was the reason why.
[21:38] And also it's like cleaner topology.
[21:40] So yeah, don't have exact answer.
[21:45] But I remember it was not liking the triangulated mess.
[22:00] Hi, through really exciting stuff.
[22:03] You're talking about the size of the textures.
[22:06] Is it possible to work to a low resolution size and scan up later effectively?
[22:11] Do you get similar results or is it a bit?
[22:14] Is there a lot of difference between what you're, what way you'll actually end up?
[22:20] There will be different.
[22:22] So for example, do you see these like a nice little pattern happening here?
[22:27] So if I wouldn't apply the UV layout that sort of spreads the UV island.
[22:33] So I'm using as much of the UV space.
[22:35] The edges of this would be super-asterized because in the texture, if you look at it, it's like really tiny and there's not enough pixel information.
[22:45] In terms of the 4x4 resolution, I just wanted to, the quality of the image be really high.
[22:51] So I can do these macro shots and everything is really clean.
[22:55] But you can run it in just, you know, 1024 by 1024, everything will work the same.
[23:02] You just want to have as clean result essentially because it's not vector.
[23:05] It's just rasterized pixel information.
[23:09] Yeah, I was just thinking when you're developing and running through sort of various versions.
[23:14] Yeah.
[23:17] Thank you.
[23:18] Okay, I think we have, we're going to wrap up soon, but we have Flip Pluschi.
[23:26] So who can name the three time-based cop nodes?
[23:34] Okay, I have to go back up there.
[23:37] Time-shape, time-blend and time-loop.
[23:51] Woo-hoo!
[23:53] Okay.
[23:55] I think that's it.
[23:58] Thank you very much, Yako.
[23:59] Thank you guys.
[24:00] And thanks everyone.
[24:01] Thank you.



---

## Captured Frames

- [3:08] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_000.jpg
- [6:29] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_001.jpg
- [8:19] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_002.jpg
- [9:43] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_003.jpg
- [11:15] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_004.jpg
- [13:29] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_005.jpg
- [17:23] tutorials/frames/h22---copernicus-and-time-shift-jakub-spacek-houdini-22-hive/frame_006.jpg

---

## Structured Notes

### Core Technique
Houdini 22 Copernicus **adjacency workflows** — seam-free texture effects across UV islands on bad UVs — driving a custom paint-spreading solver, plus the new COPs **time-manipulation nodes** (Time Shift / Time Blend / Time Loop) for leading-edge effects.

### Summary
Jakub Spacek's HIVE talk builds a paint-spreading/reaction-diffusion look on a 3dscans.com statue with deliberately bad auto-UVs, to stress-test H22's adjacency node family. Geometry to Adjacency emits a packed "cable" (unpacked via Cable Unpack → Set Fields from Input) that lets operators cross UV-island boundaries seamlessly: Adjacency Distort bridges islands, Adjacency Attribute Sample maps noises correctly (sampling P by default), and solvers like Turing Pattern / Reaction Diffusion have adjacency inputs built in. The spread itself is a block solver (slope direction + adjacency-distorted noise per frame), given a leading edge by the new **Time Shift** node ($F−10 subtracted from the current frame — replacing a hand-built dissipation solver), and layered with a masked Turing pattern, a Ripple solver seeded each frame from the leading edge, hue/saturation remapping for color, and blur inside blocks (small radius × many iterations so it never crosses island boundaries). Lookdev happens in Solaris/Karma with Material Linker; textures were baked (4K COPs sims are RAM-hungry — unload the Copernicus cache or crash, even with 400 GB RAM).

### Key Steps
1. **Mesh prep** — scan is dense triangulated mess: Quad Remesh (UV Unwrap crashed/cooked forever on the triangulation), then UV Unwrap for arbitrary UVs; fix hidden **overlapping islands** (caused mystery noise artifacts [frame_000, 3:08]) with the Labs overlap-isolating node; UV Layout with "spread islands to all available space" — island gaps determine how far adjacency operators can go before crossing boundaries.
2. **Sources** — flatten geometry into UV space, Scatter points as paint-dip sources with per-ID colors; bring points + geometry into Copernicus, Stamp Points to splat circles. Tip: **X key toggles flattened UV view vs 3D preview**.
3. **Adjacency in** [frame_001, 6:29] — Geometry to Adjacency → packed cable (many fields); Cable Unpack + "Set Fields from Input" exposes them. Cables (green inputs) pass through solver iterations uncooked — adjacency doesn't change per frame, so this saves compute.
4. **Spreading solver** [frame_002, 8:19] — block solver, per frame: add source color (RGBA) → **Slope Direction** spreads outward → noise distorts, but raw noise maps wrongly across islands; run it through **Adjacency Attribute Sample** first, then **Adjacency Distort** at the end bridges island seams [frame_003, 9:43]. Multiply by alpha to preview blending. Color juice: remap spread value −180..180 into Hue Shift + Saturation.
5. **Leading edge via Time Shift** [frame_004, 11:15] — Time Shift (Mode: Custom, Frame: `$F-10`) → Subtract from current → Clamp = a moving front, no custom dissipation solver needed. The three new time nodes (Time Shift / Time Blend / Time Loop) work like SOP-level time operators — hold first/last frame, loop sequences.
6. **Seam-free blur** — plain Blur crosses UV boundaries; wrap it in a block: radius small enough to stay inside the island gap × ~500 iterations (~4 s cook) to reach the intended blur size.
7. **Turing pattern** [frame_005, 13:29] — courtesy of Alex (Hamer); similar to reaction diffusion (Units: Pixels, Iterations 5, Radius 5, Power 10, Gain 1) with adjacency passed in and the spreading mask clamping growth; RD and several Copernicus solvers have adjacency embedded.
8. **Ripple solver** — COPs Ripple works like the SOP one, but instead of an initial state, **Add** the leading edge every frame (clamp ≤1); tune conservation/waves/spring.
9. **Dissolve-out** — invert the original spread animation to melt colors back to the plaster material — no extra solver.
10. **Lookdev** [frame_006, 17:23] — Solaris: Material Library (3 materials), Material Linker for per-object material and light assignment, Karma render; grunge nodes (new preset library, Copernicus-native noises — adjacency-matchable for seamless grunge) faked here with MTLX noise mixing. ML teaser: the ML pattern preset has an adjacency input; masking training updates with the spread mask grows the pattern gradually.
11. **Q&A** — bake COPs textures (4K live is massive; unload Copernicus cache to avoid crashes); resolution scales down fine (1024² works, edges just rasterize sooner); Time Shift inside blocks for time-displacement is untested but plausible.

### Houdini Nodes / VEX / Settings
- Adjacency family (new in H22): Geometry to Adjacency, Adjacency Distort, Adjacency Attribute Sample, Adjacency Space Transform (not used); cables: Cable Unpack + Set Fields from Input; green cable inputs skip per-iteration recompute
- Time nodes (new): Time Shift (Custom, `$F-10`), Time Blend, Time Loop
- Solver: block begin/end per frame; Add (source), Slope Direction, Fractal Noise 3D, Clamp; Hue Shift/Saturation remap (−180..180)
- Blur-in-block: small radius × ~500 iterations to respect island gaps
- Turing Pattern (Units Pixels, Iter 5, Radius 5, Power 10, Gain 1) masked by spread; Ripple Solver fed by Add each frame, clamped
- SOP prep: Quad Remesh, UV Unwrap, Labs overlapping-UV fix, UV Layout (spread islands), UV flatten + Scatter + Stamp Points
- Solaris: Material Library, Material Linker (materials + light linking), Karma; grunge node presets (H22)
- Shortcut: **X** toggles flattened/3D preview in Copernicus

### Difficulty
Advanced

### Houdini Version
Houdini 22 (adjacency nodes, time-manipulation COPs, grunge presets)

### Tags
cop, procedural, simulation, solaris, karma, advanced, houdini-22

---

## Related Tutorials
- [Houdini 22 | How to Create Terrains in COPs | Utilize Height Fields](houdini-22-how-to-create-terrains-in-cops-utilize-height-fields.md) — layer-based Copernicus fundamentals
- [H22 - Baking with Copernicus | Alex Hamer | Houdini 22 HIVE](h22---baking-with-copernicus-alex-hamer-houdini-22-hive.md) — the Alex credited for the Turing pattern; baking the COPs output this talk needed
- [Wood Barrel Texturing in COPS](wood-barrel-texturing-in-cops.md) — earlier-generation COPs texturing with UV-space workarounds these adjacency nodes obsolete
