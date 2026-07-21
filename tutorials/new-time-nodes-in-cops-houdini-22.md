---
title: New Time Nodes in COPs | Houdini 22
source: YouTube
url: https://www.youtube.com/watch?v=ewNpXaxZI6w
author: Inside The Mind
ingested: 2026-07-21
houdini_version: "H22"
tags: [cop, time, retiming, looping, flipbook, simulation, intermediate, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/new-time-nodes-in-cops-houdini-22/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# New Time Nodes in COPs | Houdini 22

**Source:** [YouTube](https://www.youtube.com/watch?v=ewNpXaxZI6w)
**Author:** Inside The Mind
**Duration:** 12m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Houdini 22 has added some new time-related nodes to Copernicus
[0:04] so let's look at what they are and how they work
[0:12] So I'm in COPs here, I just have a flow block set up here, nothing too fancy, it's just a
[0:18] one of these new grunges and then we're wiring that in and then a fractal noise.
[0:23] This just gives us just something to work with here that we can use for our time-related nodes
[0:30] and one of the other things that I want to point out with COPs now is if you're starting
[0:34] to have issues with your resolution and VRAM there is a new setting here if you come up to edit and
[0:39] come to Copernicus settings we can set this auto-unload to one of these other settings here
[0:45] and that will unload some of the nodes and kind of free up your VRAM
[0:49] so if you're having issues with VRAM then maybe check out these settings and see if that will
[0:54] help your situation and theory it should, they are in beta so we'll see as time goes on but
[1:00] give those a shot. So we have a set of new nodes here, there are four of them, we have
[1:06] time blend, we've got time loop, time shift, and then time pack, they're all new in 22.
[1:13] So time blend here is basically just going to allow us to hold on some frames or hold the
[1:21] frame so by default it's going to be set to this f start and then the last one will be f end
[1:27] so let's go ahead, I'm going to delete this channel and let's set this to something like 10
[1:32] so what this is going to do is this going to take our frame our first frame here it's going to hold
[1:38] that until frame 10 and then it's going to start to simulate so you can see that we have nothing
[1:45] going on here frame 10 hits and then we start to get that movement we can do the same thing for
[1:51] the the hold the last frame so if I just delete that and I set this to like frame 30 let me just
[1:58] reset that first frame there we're going to simulate up to frame 30 once we hit frame 30
[2:05] it's just going to hold that so if that's something that you want to do this is going to be the node
[2:09] that you want to use time loop works a little bit differently so go ahead jump back to the beginning
[2:16] if we go ahead and press play here you can see that we're going to get this kind of looping
[2:21] animation where it's going to cycle back every 24 frames so 24 frames in on our 25th frame we're
[2:28] going to loop back to that very first frame you can change around the length here and you can
[2:33] change the frame start as well if you want we also have a different loop type so we've got
[2:38] zigzag so if I press play you can see what this is going to do it's going to kind of ping pong
[2:44] back and forth between those frames could give you something interesting depending on what you're
[2:49] going for and then we've got this blend one and we've got some different blend shapes we can either
[2:53] do linear or cosine I'm going to bump this up a little bit maybe to 48 frames it's a little bit
[3:01] hard to kind of see what's going on here I wanted to create a flip book here and let's do to frame
[3:08] 48 and let's start this I should load up our mplay here and it's going to just kind of bake this
[3:17] out for us so that we can play this in real time here and what this is going to do is it's going
[3:23] to blend between our frames give us a in some cases a nice blend in other cases it's not going to
[3:32] work quite as well but if I go ahead and press play here you can see we get this kind of blend
[3:38] between it's trying to create a seamless kind of looping animation here which doesn't exactly
[3:46] work in this case but depending on what you're doing it might work and you can play around with
[3:51] the linear and cosine as well as well as the frame length they can give you just some different
[3:55] results and we've got this time shift here which by default is going to be such this absolute shift
[4:02] with f start as the from and f start as the end so it's basically going to not do anything
[4:13] by default with this absolute shift so if we were to take this first one I'm going to delete this
[4:19] channel here and then I'm going to delete this second one as well actually we'll leave that one
[4:24] so we can take this and let's say we want to start with frame 30
[4:30] now on frame one we've simulated it up to frame 30 and we're moving that back to frame one here
[4:38] so we can simulate through now there's also by time so this one's basically pretty similar to how
[4:45] the time shift node works in like sops then we've got the ability to clamp the frames as well so
[4:53] you can play around with that we also have a relative shift so if I set this back if I want to bump
[5:00] up to frame 30 again we set this to 30 I can press play here you can see you can kind of see this
[5:06] happening in this bar right here this is kind of showing where this is taking place and it kind of
[5:14] moves along here I have noticed just in playing depending on what you're doing it seems to kind
[5:21] of slow things down a little bit so just be wary of that that that may be something that happens
[5:27] and we've got this custom which by default is going to be set to f start and this is where you
[5:31] can which I don't know why they did this they did for some reason I would think that this would just
[5:37] be set to dollar f so we get this because f start I don't know it just it just holds on that first
[5:50] frame which doesn't really makes a lot of sense to me but we can set a frame in here if we want so
[5:57] if we wanted like frame 120 it's going to simulate up through and this is where you get that like hold
[6:04] right so if you just want that one singular frame this is how you're going to go about doing that
[6:11] lastly we have this time pack which is kind of an interesting node I haven't fully figured out exactly
[6:21] what the intended use for this is my brain is just not putting two and two together I guess
[6:28] but basically this creates a cable that has multiple frames that are sampled in it so if you do a
[6:36] cable unpack and we set this to set fields from input we're going to get three different frames here
[6:47] and let me move forward a few frames let's go to frame 59 here and actually I'm going to set this
[6:57] one back let's do dollar f for this one so that we can kind of hop back and forth so the way that
[7:07] we have this set up currently is it's going to take our frame and it's going to take the frame
[7:14] before and the frame after that's what this step is doing so we're going to have one frame in either
[7:19] direction so we're going to go from frame 50 we're on frame 59 so we're going to get color one should
[7:25] be frame 59 frame 58 should be that color zero and then frame 60 should be that color two
[7:35] and we can change this to be the prefix or the suffix that's just what that point zero is so if I
[7:39] look at this we have color zero being displayed right now so this should be frame 58 actually
[7:47] so actually let me I thought I was going to leave this on dollar f let's set this to 58 and we can
[7:53] do like a switch node let's wire these up so here we should be the exact same thing which they are
[8:08] and as I said color one should be frame 59 so if I switch here we should see a difference
[8:15] which we do so if I set this to 59 now these should be the exact same and they are
[8:23] and then lastly we've got color two which should be frame 60 you can see that we get a difference
[8:29] there so that is frame 60 so we also have so this is set to relative we can set this to
[8:36] absolute and we can get if I set fields from inputs here you can see what we get here so we're
[8:44] going to get frames one through ten on this so let's just look at this so color zero one actually
[8:54] let's go all the way up to like nine you can see it's starting to move there just because that the
[8:58] initial flow solver is kind of slow to move but we get the the first ten frames basically out of
[9:05] this and if we wanted to we can set this step up so let's say let's set this to a step of five here
[9:15] and let's go back to color zero so color one we should move forward five frames two
[9:25] we're going to step outside of this because we're we have that frame range that's one to ten so if I
[9:30] set this to 50 this should be different so now at color two we're getting frame 10 color three
[9:40] or frame 11 whatever and then we're getting just the step through on these so color nine
[9:50] we're deep into that simulation so the step is going to control how many frames are in between
[9:58] what the step is basically how many frames are in between so we can do by time as well if we want
[10:03] to do it that way you can stick on relative so it's kind of interesting the way that this works
[10:09] it's a little weird like I said I'm not really sure exactly how this is meant to be used or what
[10:17] this is meant to be used I guess if you need to sample multiple frames initially I thought this
[10:21] was supposed to be for like maybe like the denoise because I think it needs likely yeah it needs a
[10:29] previous frame so I guess you could you could wire it in here that way and just kind of pack them up
[10:37] that way I guess that maybe is the intended to use for those I don't know what this tvd really
[10:44] use that one so maybe that's what this is kind of intended for and then you can cable unpack I don't
[10:50] know if you wanted to do something else with it maybe you can you know sample multiple frames and
[10:56] distort them all if you wanted to do that I don't know if you guys know exactly what this is is
[11:02] supposed to be used for the dykes don't really say anything as far as what that is for other than
[11:09] sampling multiple frames so it just takes a single input and samples at various times to produce the
[11:15] cable so not really sure if it pairs with another node I don't know denoise ai is the only one that
[11:23] I can think of that it would it would use or would pair with well so if you know let me know in the
[11:30] comments I'd be interested to hear if it's a new node that's in there that I'm not aware of then
[11:37] we'll take a look at that one as well but anyways hopefully this has helped you out
[11:40] and you learned about the the new time shift or the new time related nodes and cops glad to see
[11:46] that these are in here they're gonna allow us to do a lot of different things inside of cops and all
[11:51] definitely be taking a look at some of the things that we can do with them in the future
[11:56] and just building some things some general things around them as well so excited to get into all
[12:01] that I am going to be covering a bunch of other things that are new in houdini 22 so if you want
[12:06] to learn more about the stuff that is new in houdini 22 make sure to stick around so that you
[12:12] don't miss any of that anyways thank you guys for watching and have a good day



---

## Captured Frames

- [0:40] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_000.jpg
- [1:08] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_001.jpg
- [1:47] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_002.jpg
- [2:42] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_003.jpg
- [3:40] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_004.jpg
- [5:08] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_005.jpg
- [6:50] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_006.jpg
- [8:50] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_007.jpg
- [9:42] tutorials/frames/new-time-nodes-in-cops-houdini-22/frame_008.jpg

---

## Structured Notes

### Core Technique
Houdini 22's four new time-related Copernicus (COPs) nodes — **Time Blend**, **Time Loop**, **Time Shift**, and **Time Pack** — for holding, looping, retiming, and multi-frame sampling of animated/simulated COP sequences, demoed on a Flow-block + grunge + Fractal Noise setup. Also covers the new (beta) **Copernicus auto-unload** setting for freeing VRAM.

### Summary
Feature walkthrough (12m24s) by "Inside The Mind" of the H22 time nodes, using a simple Flow block driven by one of the new grunges plus a fractal noise as the animated source. Opens with a practical VRAM tip: Edit → Copernicus Settings → **auto-unload** (beta) can unload nodes to free VRAM if high resolutions are causing memory pressure. **Time Blend** holds a chosen first frame (`$FSTART` by default — set e.g. 10 to freeze until frame 10, then simulate) and/or holds the last frame (set e.g. 30 to freeze everything after frame 30). **Time Loop** cycles the sequence (default 24-frame length, adjustable start/length) with three loop types: normal cycle, **zigzag** (ping-pongs back and forth), and **blend** (linear or cosine blend shapes that crossfade the loop seam — demoed by flipbooking 48 frames to MPlay; the blend produces a seamless-ish loop, results vary by content). **Time Shift** defaults to an absolute shift from/to `$FSTART` (a no-op); setting the "from" frame to 30 makes frame 1 show the frame-30 state. Also supports by-time mode (like the SOP Time Shift), frame clamping, a **relative shift** mode (a progress bar on the node shows where sampling occurs; author warns it can slow playback), and a **custom** mode that oddly defaults to `$FSTART` (holds the first frame) — set it to `$F` for normal behavior or a fixed frame (e.g. 120) to hold one specific simulated frame. **Time Pack** samples multiple frames of its input into a single "cable" — unpack with **Cable Unpack** (set *fields from input*) to expose them as `color0/color1/color2...` planes (prefix/suffix naming configurable). In relative mode with step 1 you get previous/current/next frame (verified frame-by-frame with a Switch node); absolute mode with a 1–10 range packs frames 1–10; a **step** of 5 samples every 5th frame. The author's best guess at its intended pairing is nodes needing temporal context like **Denoise AI** (which wants a previous frame); the docs only say "samples multiple frames." Ends noting more H22-feature videos are coming.

### Key Steps
1. Build any animated COP source (here: new-style grunge → Flow block, plus Fractal Noise) to feed the time nodes.
2. **VRAM relief:** Edit → Copernicus Settings → set **auto-unload** (beta) to a non-default option to let Houdini unload node caches and free VRAM at high resolutions.
3. **Hold frames — Time Blend:** set the first-frame parameter (default `$FSTART`) to e.g. 10 → output freezes on frame 1's state until frame 10, then plays; set the last-frame parameter to e.g. 30 → sequence freezes from frame 30 on.
4. **Loop — Time Loop:** choose frame start + loop length (default 24); loop types: cycle, **zigzag** (ping-pong), or **blend** with linear/cosine shapes to crossfade the seam — judge blend results via an MPlay flipbook since real-time playback is hard to read.
5. **Retime — Time Shift:** absolute mode with "from" = 30 shows the frame-30 state at frame 1; by-time mode behaves like the SOP Time Shift; clamp options available; relative mode offsets by N frames (watch for playback slowdown); custom mode: replace the odd `$FSTART` default with `$F` (passthrough) or a constant (e.g. 120) to pin one frame.
6. **Multi-frame sampling — Time Pack → Cable Unpack:** wire the animated input into Time Pack; downstream, Cable Unpack with *set fields from input* exposes sampled frames as `color0..colorN`; relative mode + step 1 = prev/current/next frame; absolute mode + range 1–10 = those exact frames; step N = every Nth frame. Verify which plane is which frame using a Switch node against a reference branch.
7. Likely pairing for Time Pack: temporal nodes such as **Denoise AI** that need the previous frame — pack current+previous and wire the cable in.

### Houdini Nodes / VEX / Settings
- **New H22 COP nodes:** Time Blend (hold first/last frame, defaults `$FSTART`/`$FEND`), Time Loop (frame start, length, loop type: cycle/zigzag/blend, blend shape: linear/cosine), Time Shift (absolute / by-time / relative / custom modes, frame clamping; custom defaults to `$FSTART` — usually change to `$F`), Time Pack (relative/absolute, frame range, **step**, by-time option).
- **Companion nodes:** Cable Unpack (*set fields from input*, prefix/suffix plane naming → `color0/1/2...`), Switch (for frame-verification), Flow block + grunge + Fractal Noise (demo source), Denoise AI (speculated Time Pack consumer), MPlay flipbook (for judging loop blends).
- **Settings:** Edit → Copernicus Settings → **auto-unload** (beta) — frees VRAM by unloading node caches.
- **Caveat:** relative Time Shift can slow playback; Time Pack's official intended use is undocumented as of this recording.

### Difficulty
Intermediate — assumes working COPs familiarity; the nodes themselves are simple but the Time Pack/Cable Unpack plane-mapping takes some care.

### Houdini Version
Houdini 22 (all four time nodes new in 22; auto-unload setting in beta).

### Tags
cop, time, retiming, looping, flipbook, simulation, intermediate, houdini-22

---

## Related Tutorials
- `tutorials/create-seamless-textures-with-adjacency-nodes-and-simulations-houdini-22.md` — same author/series covering H22 Copernicus adjacency nodes; shares tags: cop, houdini-22, simulation.
- `tutorials/basic-procedural-texturing-with-cops-in-houdini-21.md` — foundational COPs workflow the demo setup builds on; shares tags: cop.
- `references/copernicus.md` — primary COPs consult reference; should mention the H22 time nodes (Time Blend / Time Loop / Time Shift / Time Pack) described here.
