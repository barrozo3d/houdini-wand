---
title: week 02   08   setting the strong constraints and the breaking threshold v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9TNDsfFNoq4
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H17.5+"
tags: [vellum, cables, constraints, breaking, timescale, file-cache, vdb, bridge, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p/
frame_count: 4
---

# week 02   08   setting the strong constraints and the breaking threshold v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9TNDsfFNoq4)
**Author:** The VFX School Archive
**Duration:** 12m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So let's bring in the rest of these cables now. So I'm going to come to here and disable that Delete Blast node. Okay, so that will cycle through all of those now. So it'll take a little bit of time. There we go. So we got all the cables coming through there now. Now I want to make the kind of these longer pieces here. I want to make them the attached constraints unable to break there. Okay, so the ones to kind of near the back while doing tests. So some of these seem to be breaking too early. So I've decided to make these at the back unable to come away from the bridge. Okay, and also, you know, that part of the bridge doesn't fall anyway. So I'm dropping in an object merge here and I'm going to bring in, and we've already got it actually. Sorry, just Alt-click and drag, bring this over. Or we could use the same one, but well, I'll just stick with this one. So let's drop a time shift and go to the last frame on this. Delete channels there and go to frame 250. Okay. So yeah, obviously this part doesn't ever fall. And so it stands to reason that these cables shouldn't break, right? So what I'm going to do is kind of make a selection of these, the attached constraints that we make here of these and make them really strong or the distance that they need to be stretched out to be much longer. Okay. So I'm just going to make a selection here just by, just grabbing the back. Be careful not to go too far forward. Okay. We need the bits at the back here. So if I were to select something here or, you know, basically it's important that any part of the bridge which falls down, we don't include it because I don't want, for example, this cable to be always stuck to the piece that falls down. Otherwise it's going to stretch way far down and not look right. So be conservative. Just grab the kind of last part of the bridge and the same on the other end. Remember to hold the shift click and drag to make that selection. Okay. And then press delete. Delete non-selected just to grab that part and then which is going to do something similar to what we did up here. I kind of making a group with VDBs. All right. VDB from polygons. Okay. Just leave that as it is. We're just making a group here. We don't really care about the shape. So kind of in, you know, make this a bit bigger. I drop a VDB reshape. SDF. Okay. And just by default that dilates it. And we can push it up a bit more just to make it bigger. Just so we be sure that we grab these cables. But again, come back here. Maybe let's just take a look. We select both of these. We can visualize both. Let me come back to this one actually. Select both. Okay. So just want to be sure that I'm not selecting any cables with pieces that are fallen away from them. Okay. So just these ones. That's fine. Good. And then we're going to make a group on the constraints now. So group. This will be a. No, we'll have to make a point group to use a volume. Right. So connect that in there. Just try and tidy the set. I'll to click to drag that up and maybe bring this down like that. Try and keep it as neat as possible. Okay. And then I'm going to call this strong because these are going to be strong. Turn that off. Turn this on and object. And then take a look and we should see that bottom parts selected brilliant. And now since this is a constraint, we need to promote that group. So it's on the primitive. So group. Promote. And set this from. So the where we're strong from points to primitives. Okay. So now we've got that. Let's dive inside the vellum solver. And in here we can change things over time and also take advantage of that group that we just made. Okay. So if we drop a vellum constraint property. Okay. Select that. I'm going to set this to manual. You can see it's taking a bit of time. It's loading that first frame every time. But we don't need to see it yet. So I'm going to grab that group. Not showing us now because I got to set the manual. Sorry. We'll have to turn it back on. Back and forward. So the first one, I'm going to grab the attached group. Okay. So that's all of the constraints connecting down here. And then we're going to animate actually the break threshold. Let me just turn that on there. Okay. Click and drag and do another one. Okay. And set the other one to the strong group delete that. So only on those strong parts here at the end. And the break threshold is going to be way high. Higher than it was before. So point two. So basically, you know, then they're not going to break at this level. And you see when you compare it to, you know, what we use on the other side. So I'm going to set this back to manual while I, because I want to set keyframes here. I know we don't want to be simulating the whole way. Okay. So on the first frame, I'll leave it, I'm going to leave it fairly low, point two, three. Okay. And then move up to frame 90. And keep it there at point three. And then go to frame 120. Just drop it down a bit to point one. Okay. So for the first kind of more or less 100 frames, they stay fairly strong. And then they'll get a bit weaker. So we'll see a few of them, you know, randomly pop off and the rest. And then once it gets to, you know, that final key frame, they'll break away. Fair quite easily. Okay. As the bridge falls away more. And then this one, we just leave at point two because we don't want these to break at all. If they do, we can just raise this value up higher. It doesn't really matter. You know, point two is plenty. Okay. What else do we want to do in these solvers? So again, you know, in all of our simulations here, we're having to do some work to get that sense of scale, which is really important, especially in a simulation like this where we've got, you know, at such a big size, like a big bridge, it's very important to consider that. And it's a feature that you see of kind of bad simulations in Houdini is that things look small always, especially bullet simulations, IBD things are kind of bouncing around like everything's tiny. So you've got to do some work to kind of get that looking right. It's really important. So what I've found with this simulation is what really helped was this timescale, right? So dropping this timescale value gives a sense of slow motion like things are moving in slow motion, but you know, just like dropping the gravity for the bullets in that gives a sense of scale. Things, you know, can't move very quickly when they're very big. So timescale, I'm going to drop that down to 0.25. Okay. Forced here, I'm going to drop the wind drag a bit just so that things are allowed to sway and move for a little bit longer than the normal. And that's pretty much it. The sub steps I found I didn't need to raise the metal. And I think that's pretty much ready to go. Let's go back to the first frame. This simulation does take quite a bit longer than the others. Okay. So maybe let's just go to the first frame. Let me cover to that these templates, they're kind of annoying. Unless just run a flipbook for the first few frames. Okay. You don't want to cache the whole simulation and for it to be completely, you know, first to forget something obvious. So let's save it and then just run a simulation. I'll probably stop it once we're kind of 50 frames in something like that. Just stop the sim there. Just got 27 frames. But I can see, you know, everything's holding now. And then once they get stretched and pulled apart far enough, they start to break then you can see them snapping back. This gives us this nice behavior. So I'm, you know, confident enough to let it go ahead now. So let's go right there. Let's go back here. Just let that run through again. And then let's drop a file cache. This time just standard file cache. Okay. There is vellum.io I think. But that's for saving the constraints and stuff and we don't really need that. Where is it? I know. But in our case, we don't need to save the collision geometry or the constraints. So just standard file cache is fine. So we want frame range. Let's save this into our geometry folder. Let's make a new one. So let's call it VirtCableCache. Okay. And for the slash. Let's just say cable cache. And dollar F3. TopGio. And that's fine. That will create the folder for me. 120, sorry, 250 frames is good. Okay. Save to disk. Actually, let me interrupt that. Always important. Save first. Save to disk. Just run a quick flip book of that simulation that's finished here. And you know, it's kind of okay. But then I find, as it's coming later, it's looking a bit floaty. Just, you know, I've gone a bit overboard with trying to slow things down to make it look like I'm a large scale. Like going overboard, it kind of starts to look like it's underwater or, you know, in slow motion or something. So I'm going to do a couple of things. So come back here. The timescale I'm going to set to 0.35. Okay. And then I'm actually going to push the gravity to minus 15. And hopefully that will solve that for us. Okay. So we'll reset that and then Sim that's a cash out out again and it should be looking good then.

**Frame:** tutorials\frames\week-02-08-setting-the-strong-constraints-and-the-breaking-threshold-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Add all cables; create "strong" constraint group (non-falling bridge end) via VDB selection + Group Promote points→primitives; inside Vellum Solver add Vellum Constraint Property nodes: animate break threshold on "attach" group (0.03→0.1 over frames 1→120); "strong" group threshold=0.2 (never breaks). Scale: timescale=0.35, gravity=−15, drag reduced. Cache 250 frames.

### Summary
12m37s VFX School Archive module. Final step of vertical cable Vellum sim. Brings in all cables (disable blast node). Creates "strong" constraint group for cables near non-falling bridge section (conservative VDB selection + Group Promote to primitives). Inside Vellum Solver: two Vellum Constraint Property nodes — one animates break threshold for "attach" group (strengthens then weakens over time for progressive breaking); one sets very high threshold for "strong" group. Timescale=0.35 and gravity=−15 balance scale vs floaty look. Standard File Cache 250 frames.

### Key Steps
1. **Disable blast node** → all cables come through (previously only one for testing)
2. **Select non-falling bridge section** (conservative — avoid any piece that falls):
   - Select geometry from back part of bridge (shift+click, drag)
   - Delete non-selected → isolated non-falling section
3. **VDB group around cables** to keep near that section:
   - VDB from Polygons → VDB Reshape SDF (dilate, increase size) to encompass nearby cables
   - Group SOP (on cable points) → connect VDB volume
   - Name group "strong"
   - **Group Promote**: from points to primitives (constraints live on primitives)
4. **Inside Vellum Solver → Vellum Constraint Property** (two nodes):
   - Node 1: group="attach" (all attach constraints); enable **Break Threshold** animation:
     - Frame 1: threshold=0.03 (fairly strong)
     - Frame 90: threshold=0.03 (hold)
     - Frame 120: threshold=0.1 (weaker — cables start breaking more easily)
     - Set keyframes linear in animation editor
   - Node 2: group="strong" → break threshold=0.2 (very high → never breaks under normal sim stress)
5. **Scale parameters** (Vellum Solver):
   - **Timescale = 0.35** (slow motion feel for large bridge; 0.25 was too slow/floaty)
   - **Gravity = −15** (stronger than default −9.8; compensates for timescale)
   - Wind Drag: reduce slightly (allow cables to sway longer)
6. **File Cache** (standard, not Vellum IO):
   - Path: `VirtCableCache/cable_cache.$F3.bgeo.sc`
   - 250 frames; Save to Disk
   - Note: standard file cache fine; no need for Vellum IO unless saving collision geo + constraints

### Houdini Nodes / VEX / Settings
- VDB from Polygons → **VDB Reshape SDF** (dilate mode, default) → Group SOP → Group Promote (points → primitives)
- **Vellum Constraint Property** (inside solver): group, break threshold, animate over frames
- "attach" group break threshold: keyframes 0.03 at f1 → 0.03 at f90 → 0.1 at f120 (linear)
- "strong" group break threshold: 0.2 (constant — non-falling section)
- Vellum Solver: **Timescale=0.35**, **Gravity=−15** (adjusted from default −9.8)
- Wind Drag: reduce from default for more natural sway
- **Standard File Cache** (not Vellum IO): `VirtCableCache/cable_cache.$F3.bgeo.sc`; 250 frames
- Group Promote SOP: from points to primitives (constraints are primitive attributes)

### Difficulty
Intermediate

### Houdini Version
H17.5+

### Tags
[vellum, cables, constraints, breaking, timescale, file-cache, vdb, bridge, intermediate]

---

## Related Tutorials
- week-02-07-starting-the-vellum-sim-v1-1080p.md (previous: Vellum setup, rest length, attach geometry)
- week-03-01-intro-v1-1080p.md (next week intro)
- week-01-11-rbd-configure-v1-1080p.md (active attribute animated boundary, same project)
