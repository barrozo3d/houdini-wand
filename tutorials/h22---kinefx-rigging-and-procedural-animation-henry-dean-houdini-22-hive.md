---
title: H22 - KineFX Rigging and Procedural Animation | Henry Dean | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=0YNaNZkjwoM
author: Houdini
ingested: 2026-07-19
houdini_version: "22"
tags: [rigging, animation, procedural, attributes, sop, advanced, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# H22 - KineFX Rigging and Procedural Animation | Henry Dean | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=0YNaNZkjwoM)
**Author:** Houdini
**Duration:** 19m41s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Viewport G-Splat Rigging & Scaling Bugs [0:00]
**Transcript (timestamped):**
[0:00] So hello everyone, and yes, rigging and animating a G-splats
[0:05] entropy in Houdini 22.
[0:06] So the main motivation behind doing this was to show off the fact
[0:12] that we can render G-splats in the viewport directly.
[0:15] And because we can do that, it means all the kinds of things
[0:18] that we want to interact with interactively and how possible.
[0:21] And that includes rigging and animation.
[0:25] So we've just had some really great talks on G-splats.
[0:33] So this is going to feel a lot like finger painting,
[0:35] because I had never touched them before.
[0:42] Fortunately, I didn't really need to,
[0:44] because it really was very straightforward to bring that in
[0:48] by the big G-splats up.
[0:50] And then I've got a point cloud, and I've got points with attributes.
[0:53] So I'm happy, I'm comfortable.
[0:57] The bone-to-form sop just works.
[1:01] And all the other sops just work like the transform sop.
[1:04] Bit closer.
[1:05] Oh, sorry.
[1:07] I was quiet.
[1:08] It's happened again.
[1:10] Start again.
[1:13] Dear God.
[1:17] Where was I?
[1:18] Oh, yeah, the transform sop.
[1:20] So that just works almost.
[1:22] And this is when I begin my little Debbie Downer segment,
[1:27] where I'm just full of problems.
[1:30] So the first thing that I needed to do when I got the model in
[1:32] was scale it.
[1:35] And so I plugged in the transforms sop,
[1:37] and I scaled it down.
[1:39] But all the points got close together,
[1:42] but everything just turned into a big mush.
[1:44] And people that know more than me about this stuff, which
[1:48] is possibly everybody, will know why that's happened.
[1:51] And so in Houdini, if you don't know,
[1:53] attributes can have type information attached to them.
[1:57] And the scale attribute that gets put out by the baked
[1:59] G-splats sop is just three floats, not a vector.
[2:05] And so it won't get transformed by any operations.
[2:09] So I'm scratching my head going, why?
[2:12] What are they up to?
[2:13] This seems like a glaring bug.
[2:15] And I was going to find out why very shortly.
[2:21] So I cast the scale attribute to a vector.
[2:24] And suddenly it all works.
[2:25] Everything's scaling absolutely fine.
[2:27] And then I go to rotate the model.
[2:31] And everything starts to get real weird.
[2:33] And I'm seeing all these streaks and all those ellipsoids
[2:36] that we've heard about before were starting to strafe across.
[2:40] And of course, what was happening was
[2:42] that the non-uniform scale was being rotated as well
[2:46] as the orient attribute.
[2:49] So that is why scale is a three float and not a vector.
[2:55] This does bring up things for the future.
[2:57] And fortunately for this example,
[2:59] I could punt on it and not worry about it.
[3:02] So I have no idea how a squash and stretch rig would work.
[3:06] So if my joints are non-uniform, like I said,
[3:09] I didn't have to think about it.
[3:10] And I'm still not.
[3:13] But anyway, after casting back to a three float,
[3:16] then I could rotate the model and everything was happy.
[3:21] So this is where I tried to get a slide working.
[3:26] Oh, yeah.
[3:28] Can use a touch pad.


### The Challenge of Rigging Without Topology [3:31]
**Transcript (timestamped):**
[3:31] So this was the model that we were working with,
[3:33] provided by Danny Mittell, who does some great work on Supesplat
[3:37] and he does a lot of macro G-splat stuff.
[3:40] And so the one we went to work with was this centipede here,
[3:44] which seems to have been popular in some quarters,
[3:49] not so much in others.
[3:52] And this model was in no way what we would expect
[3:55] to be ready for rigging an animation.
[3:58] So there's no symmetry.
[4:00] This is not a respose.
[4:03] Yeah.
[4:04] So something needed to be done about that.
[4:08] The next little problem that came along
[4:10] was I didn't quite realize before just how much we
[4:14] rely on topology.
[4:17] I'm a character guy.
[4:18] I'm a rigging guy.
[4:20] Point clouds and volumetric things
[4:22] that somebody else's jive.
[4:25] And so yeah, weight painting, joint placement even,
[4:29] not having surfaces to snap to or to stick to.
[4:32] This was all stuff that got really, really hard when it's
[4:35] just a cloud of points.
[4:38] Now, obviously, having listened to the other talks
[4:40] and if you've trained a G-splat offer model,
[4:44] there very well will be techniques
[4:46] for using the original topology to get around these problems.
[4:50] But for me, this was just from photographs
[4:52] and I only had the point cloud.
[4:56] Yeah, viewport selections, other things
[4:58] that we rely on topology for just day to day.
[5:02] They were all swept out from underneath me.
[5:05] So doing it as is was starting to look really quite prohibitive.
[5:15] Now, there are other things about,
[5:20] I don't think that's going to look.
[5:22] But anyway, what I tried to show was that it's not.
[5:27] What I was trying to show there was just the way
[5:29] that G-splats interact with each other.
[5:31] And like I said, this is new territory for me.
[5:32] I've never worked like this.
[5:34] And observing just how, and I think somebody else
[5:38] mentioned the word painterly to do with yes, effects in G-splats.
[5:43] And that's just how it felt to me.
[5:45] The effect of moving things apart and closer together
[5:48] and just how they interact with each other as they overlap
[5:53] was actually incredibly immediate and very refreshing.
[5:57] Now I'm sitting there going, oh, my edge loops.
[6:00] What about my volume preservation?
[6:01] What about my, you know, all of this stuff just went.
[6:05] And suddenly I had something really immediate to work with.
[6:09] It started to feel real good.


### Kit-Bashing a Clean Rest Pose [6:11]
**Transcript (timestamped):**
[6:12] So we still had that rest pose problem.
[6:15] And the idea occurred to me with the way
[6:18] that they interacted with each other.
[6:19] Maybe Danny wouldn't mind if we pursued a different path
[6:24] and actually kit-bashed together a new centipede using
[6:29] the original as a source.
[6:32] Fortunately, Danny agreed to let us butcher his work.
[6:35] And that's how we went forward.
[6:39] At this point, Danny actually went away and did a V2 for us,
[6:44] a version 2 of the G-splat.
[6:46] And I was able to go away and have a think
[6:49] about how centipedes move, loop, and play.


### Decoding the Metacronal Wave Gait [6:58]
**Transcript (timestamped):**
[7:00] And looking this up, they have, and I really like this phrase,
[7:03] the metacronal wave gate of many-legged creatures,
[7:08] normally insects.
[7:11] I'm going to make so many entomological mistakes.
[7:13] So if there's anybody in here that's into that stuff,
[7:16] I apologize.
[7:19] But this describes the wave-like propagation
[7:21] of the footfall pattern in most species, from back to front,
[7:26] in some from front to back.
[7:27] But I went back to front.
[7:29] Again, I might have got that wrong.
[7:33] And I went away and just figured out
[7:35] how that works based off a phase.
[7:37] So what you're seeing is something
[7:38] that's driven off a wheel-like animation.
[7:41] For the first 180 degrees, the leg
[7:43] is lifted and translated forward.
[7:46] For the next 180 degrees, it's just translated backwards.
[7:48] So it's really quite simple.
[7:53] And whilst I'm R&Ding this, I've also
[7:55] got this lingering thing in the back of my mind.
[7:57] It's like, oh, god, sliding, foot sliding.
[8:01] I don't know what to get in.
[8:03] And there's a lot of feet.
[8:08] And basically, one of the things that I love,
[8:10] and it's probably the hardest thing to let go of
[8:12] once you've started rigging stuff in Udini,
[8:15] is to let go of the ability to put stuff off.
[8:21] Never do today.
[8:22] I won't come put off until tomorrow.
[8:23] And I could leave it with this simple prototype.
[8:27] It definitely looks right.
[8:30] And I can leave it there and worry about,
[8:31] get to the finished result first, and then come back
[8:34] and revise that if I need to.
[8:37] As it turned out, when I look back
[8:39] at the reference for centipedes,
[8:44] they do have a very skittering quality to the motion.
[8:47] It's one of the things that I think makes them unnerving.
[8:50] And there is a lot of sliding in the legs.
[8:53] There's so little weight in each one.
[8:55] And it's a lot more like watching something moving
[8:58] through water than it is moving on land.
[9:01] So in the end, it actually added something, thankfully.
[9:07] OK.
[9:09] And this is where that bit of R&D ended up.
[9:12] So at this point, I figured out how
[9:14] to get a change in distance traveled onto that phase
[9:20] to drive the leg motion.
[9:25] After getting that far, Danny came back with a V2.
[9:29] And we were ready to make a start.


### Leg Skinning with Capture Proximity [9:31]
**Transcript (timestamped):**
[9:32] And basically what I was doing is just isolating segments
[9:35] that were cleanish that I thought could be used.
[9:38] And so I picked a couple of narrow ones,
[9:40] a couple of broad ones, and just rigged them as they were.
[9:45] And one of the things that's always been nice about KinFX
[9:48] is that you can do an intermediate bone defamation
[9:52] as part of the setup, as long as you don't
[9:55] delete the capture attributes.
[9:59] So yeah, very, very simple KinFX-like setup.
[10:03] Using the capture proximity, which I haven't touched in ages,
[10:07] because it's definitely not the most robust capture method we
[10:11] have available to us in Houdini.
[10:12] But again, without topology, this is what I had to work with.
[10:18] And as it was, it worked pretty well.
[10:22] So having done that with a few of the segments,


### Segment Assembly via Copy to Points [10:24]
**Transcript (timestamped):**
[10:25] I was then ready to assemble them using a copy-to-point setup.
[10:29] The only things of note here, it's all pretty standard,
[10:35] figuring out how to place the template points based upon the width
[10:39] of the segment coming in.
[10:41] And then of course, because I'm generating new skin geometry,
[10:44] new joints, I had to do some manual wrangling
[10:47] of the capture data.
[10:50] And now I am going to do this shout-out.
[10:53] The fact that we no longer need the 20-float array,
[10:57] pcap data detail attribute is a major feature of Houdini 22.
[11:04] And I won't be told otherwise.
[11:06] It makes doing this stuff a lot easier.
[11:11] So yeah, that was that.
[11:13] And at the end of that setup, I've now
[11:15] got everything I need for the bone to form.


### Apex Rig Build & Spline IK Setups [11:21]
**Transcript (timestamped):**
[11:21] So this was at the point again where I go on to the rig build.
[11:24] I haven't even finished yet.
[11:26] I haven't finished my skinning or any of that stuff.
[11:28] But I've got enough to test the animation
[11:32] that I want to put onto it.
[11:33] So I want to get there as quickly as possible
[11:36] so I can work out how much sleep I need to lose.
[11:41] And this SOP network stayed pretty much the same.
[11:44] I just put my place holders in for what I wanted to do,
[11:48] changed the scripts.
[11:50] But like I said, the broad structures stayed the same.
[11:57] So after I've got all those IK solvers added to the legs,
[12:02] I've got the spine IK for the body,
[12:06] I'm ready to think about getting the procedural animation
[12:09] onto the character.
[12:11] And there's two ways that you can do this.
[12:14] If you're going fully procedural,
[12:17] I can pretty much stop there and just invoke the rig directly,
[12:22] take the result of that metacronal wave,
[12:26] build the parameter dictionary, invoke the rig.
[12:31] And that's it.
[12:33] But of course, if you want to make use of everything
[12:35] that's in the animate state and add some hand animated layers
[12:39] to this for the antenna, the head, the tail,
[12:42] we need to do a couple of extra bits.
[12:46] And this is when I gather all the bits up,
[12:51] pack them up into the format that the animate state wants.
[12:56] So just into the pack folder sub, add that character to the scene.
[13:00] And we've now got something that's ready for the animate state,
[13:04] except we're not quite because we've got this procedural animation.
[13:09] So I build the parameter dictionary,
[13:12] feed that into a motion clip, which gives us a dictionary per frame.
[13:17] Feed that into the channel parameters from motion clip,
[13:19] which now gives us a bunch of animation curves on the geometry,
[13:23] which we can inject via apexine animation.
[13:29] Then I'm ready to plug that into the animate state.
[13:33] And after I've got what I want to invoke it for the skin,
[13:36] the skeleton, or whatever else you want to fetch.


### Reusability Upstream: Antenna Rigging [13:42]
**Transcript (timestamped):**
[13:42] So the last little thing that I wanted to focus on a little bit
[13:48] was the antenna.
[13:50] And this is probably one of my favorite things about working with
[13:52] salt-based rigging is reusability and composition.
[13:59] So placing joints for Spline IK.
[14:03] In an ideal world, we want to use the spline that we're going to use
[14:06] to drive the IK to place the joints.
[14:09] But this can be quite limiting sometimes.
[14:13] Fortunately, with this kind of picture,
[14:15] so this is way upstream in the network
[14:18] before I've done any capturing of the antenna.
[14:21] I want to build the skeleton using the rig.
[14:25] And then I can pass that chunk of rig down the network,
[14:29] fuse it into the rest of it.
[14:31] And I know that everything's going to match up one to one.
[14:35] So it's just, I was going to say, helps you stay sane,
[14:40] but I'm probably the wrong person to say that.
[14:45] And so what I'm able to do is invoke that chunk of rig logic
[14:48] straight away, send that on to capture,
[14:52] and like I said, pass the rest of it on down
[14:54] to be merged with the rest of the rig.
[15:02] I'll just play it.
[15:05] Right, there we go.
[15:06] So what I end up with is something,
[15:09] a kind of quasi viewport tool where I can just use the rig post,
[15:12] position the CVs, check the out, put of my capture as I go,
[15:19] and everything else just works.


### Network Layout Breakdown & Final Animation [15:25]
**Transcript (timestamped):**
[15:25] And that's about it.
[15:27] So this is the network for the whole thing.
[15:31] Looks a little bit big and scary at first,
[15:33] but actually all of the green boxes,
[15:36] that's purely geometry processing.
[15:37] So that's the model.
[15:38] The little pink bit in the middle, that's the rig build.
[15:42] So the actual rigging part was incredibly small,
[15:47] and then the yellow was the animation.
[15:51] So there we go.
[15:52] And I'll see what this video does.
[15:57] Thanks very much.
[15:59] Thanks very much.
[16:07] Thank you, Henry.
[16:09] Are there any questions?
[16:15] Play it again.
[16:16] It was on the, what's the sneak peek?
[16:19] It's on there.
[16:22] It is up here somewhere.
[16:29] I think this is the last part of it.
[16:32] There we go.
[16:34] So just that kind of thing.
[16:42] Sorry, this was, I did this for Fiona.
[16:46] It was meant to be edited.
[16:59] Oh, I would say under that.
[17:01] Wasn't the whole thing.
[17:02] Sorry.
[17:05] Can anyone say how Henry captured the kit bash bits?
[17:11] Oh, yes.
[17:18] This is for the plushie, by the way.
[17:22] Yes.
[17:24] If there are no more questions, then...
[17:27] Oh.
[17:28] There might be one up there.


### Q&A: Adapting Procedural Gaits to Uneven Terrain [17:33]
**Transcript (timestamped):**
[17:38] Hi.
[17:39] My question was, how easily can this be adapted to crowd simulation?
[17:47] Or irregular terrains for automatic walk cycles and stuff like this?
[17:52] So that brings us back to foot planting.
[17:54] So this particular example, and the big, there was an animation of it walking around the log as well,
[18:01] didn't need really close scrutiny on the placement.
[18:06] So if there was something that was a very high frequency uneven terrain,
[18:10] then it would be a lot easier to do it.
[18:12] So if there was something that was a very high frequency uneven terrain,
[18:16] then I would certainly want to do another pass on the procedural animation to get that to look better.
[18:24] So as is, it would depend on the shot.
[18:29] But for something like, more scrutiny, it would need additional work.
[18:34] But fortunately, nothing else needs to be changed.
[18:36] It's purely that bit that was on the right-hand side.
[18:40] Will this work?
[18:42] Of course it won't.
[18:44] It's stupid.
[18:49] Oh, yeah.
[18:51] Yeah, so it's basically what's north of the yellow bit.
[18:54] That's the only bit that needs to be changed on that, because that's the animation solver.
[19:02] Does that answer your question at all?
[19:06] I guess.
[19:09] With confidence.
[19:12] Thank you.
[19:14] Danny, who provided both G-splats of this entropy has agreed to allow us to distribute that for everyone to download.
[19:23] So later on, when 22 comes out, we will have this amongst others in the content library on satirfx.com.
[19:35] I think that's it.
[19:37] Otherwise, thanks, Henry.



---

## Captured Frames

- [2:31] tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/frame_000.jpg
- [5:45] tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/frame_001.jpg
- [9:12] tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/frame_002.jpg
- [10:29] tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/frame_003.jpg
- [13:12] tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/frame_004.jpg
- [15:31] tutorials/frames/h22---kinefx-rigging-and-procedural-animation-henry-dean-houdini-22-hive/frame_005.jpg

---

## Structured Notes

### Core Technique
Rigging and procedurally animating a Gaussian-splat centipede in Houdini 22 with KineFX/APEX: Bake GSplats to a point cloud, kit-bash a clean rest pose, capture-proximity skinning, a phase-driven "metachronal wave" gait, and injecting procedural animation into the animate state via MotionClip → channel prims.

### Summary
Henry Dean's Houdini 22 HIVE talk (using Dany Bittel's photogrammetry G-splat centipede) shows that once H22 renders G-splats directly in the viewport, the whole rigging stack "just works" on the splat point cloud — Bone Deform, Transform, standard SOPs — with two gotchas: the `scale` attribute is deliberately 3 floats (not a vector) so rotations don't shear the non-uniform splat scales (cast to vector only while scaling, cast back before rotating), and everything topology-dependent (weight painting, joint snapping, selections) disappears with a pure point cloud. The fix was kit-bashing a clean, symmetric rest-pose centipede from clean segments of the original, skinned via Capture Proximity, assembled with Copy to Points (manually wrangling capture data — much easier now that H22 drops the 20-float `pcapdata` detail array), legs driven by a wheel-phase metachronal wave (first 180° = lift + move forward, second 180° = drag back) advanced by distance traveled, plus Spline IK for body and rig-built antenna joints reused upstream. Procedural animation reaches the animate state via parameter dictionary → MotionClip → Channel Prims from MotionClip → APEX animation layer, leaving hand-keyed layers available for head/antenna/tail.

### Key Steps
1. **Import** [frame_000, 2:31 area] — File (`new_centipede_M.ply`) → **Bake GSplats SOP**: raw .ply becomes points with splat attributes, viewport-renderable in H22. Bone Deform and Transform SOPs work directly on it.
2. **The scale-attribute trap** — Transform scaling mushes splats because `scale` is typed as 3 floats (no transform applied). Cast to vector → scaling works; but then rotation also rotates the non-uniform scale (streaking ellipsoids) — that's *why* it's a 3-float. Cast back after scaling. (Squash-and-stretch rigs on splats: open question.)
3. **No topology** [frame_001, 5:45] — no weight painting, joint snapping, or viewport selections; splats overlap "painterly", which makes kit-bashing forgiving — moving pieces apart/together blends visually with no edge loops or volume preservation to manage.
4. **Kit-bash a rest pose** [frame_003, 10:29] — isolate clean narrow/broad segments from the source splat, rig them individually, then **Copy to Points** onto template points spaced by segment width; manually wrangle capture data for the new geometry/joints (H22's removal of the 20-float `pcapdata` detail attribute makes this far easier). Intermediate bone deformation mid-setup is fine as long as capture attributes aren't deleted.
5. **Skinning** — **Capture Proximity** (not the most robust method, but the only option without topology); worked well here.
6. **Metachronal wave gait** [frame_002, 9:12] — legs keyed off a wheel phase: 0–180° lift + translate forward, 180–360° translate back; phase offset propagates back-to-front along the body; drive phase from change in distance traveled. Foot sliding turned out to *match* real centipede reference (skittery, water-like motion) — prototype first, revise later.
7. **Rig build + APEX injection** [frame_004, 13:12] — leg IK solvers + spine Spline IK. Fully procedural path: build parameter dictionary → invoke rig. Animate-state path: pack SKELETON/SKIN/RIG/OTHER_BITS with **Pack Folders** → **APEX Scene Add Character** → parameter dictionary → **MotionClip** (dictionary per frame) → **Channel Prims from MotionClip** (animation curves on geometry) → **APEX Scene Add Animation** (procedural layer) + **APEX Scene Animate** (manual layers) → **APEX Scene Invoke** for skin/skeleton output.
8. **Antenna reusability** — build the antenna skeleton *with the rig itself* upstream (before capture), pass that rig chunk down and fuse it — joints match 1:1; a quasi-viewport tool: pose CVs, check capture output live.
9. **Network anatomy** [frame_005, 15:31] — green = geometry processing (most of it), small pink block = rig build, yellow = animation solver; adapting to uneven terrain/crowds only requires revising the animation block ("north of the yellow"). Both G-splat versions will ship in the SideFX content library.

### Houdini Nodes / VEX / Settings
- Bake GSplats SOP (.ply → point cloud with splat attributes); H22 viewport G-splat rendering
- `scale` splat attribute: 3 floats intentionally (cast to vector for scaling only; rotation would corrupt non-uniform scale)
- Bone Deform, Transform, Copy to Points, Capture Proximity, Spline IK, Pack Folders
- H22 change: 20-float `pcapdata` detail attribute no longer needed (easier manual capture-data wrangling)
- APEX: Scene Add Character, Scene Add Animation, Scene Animate, Scene Invoke; Attribute Adjust Dictionary (parameter dict) → MotionClip → Channel Prims from MotionClip
- Gait: phase wheel (180° lift/forward, 180° back), phase from accumulated distance, back-to-front wave offset

### Difficulty
Advanced

### Houdini Version
Houdini 22 (viewport G-splat rendering, pcapdata removal)

### Tags
rigging, animation, procedural, attributes, sop, advanced, houdini-22

---

## Related Tutorials
- [H22 - Gaussian Splats | Peter Sanitra | Houdini 22 HIVE](h22---gaussian-splats-peter-sanitra-houdini-22-hive.md) — the G-splat fundamentals talk this rigging demo builds on
- [H22 - KineFX Rigging and Animation | Max Rose | Houdini 22 HIVE](h22---kinefx-rigging-and-animation-max-rose-houdini-22-hive.md) — companion HIVE rigging session
- [H22 - Gaussian Splats and Machine Learning | Jakob Ringler | Houdini 22 HIVE](h22---gaussian-splats-and-machine-learning-jakob-ringler-houdini-22-hive.md) — more G-splat pipeline context from the same HIVE event
