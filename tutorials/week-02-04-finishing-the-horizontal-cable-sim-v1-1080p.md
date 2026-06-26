---
title: week 02   04   finishing the horizontal cable sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=ykTr02tft_k
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H17.5+"
tags: [rbd, guided-sim, bullet, cables, air-resistance, file-cache, strength-attribute, bridge, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-04-finishing-the-horizontal-cable-sim-v1-1080p/
frame_count: 4
---

# week 02   04   finishing the horizontal cable sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=ykTr02tft_k)
**Author:** The VFX School Archive
**Duration:** 9m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now one thing, if you come here, look at the geometry here. And if I turn off guides, you can see the constraints popping back here. So I'll turn that back on, come into this constraints tab within the guided simulations tab. You can see we've got this remove intro-guide constraint. So that's removing constraints which, you know, between two guided things. So just turn that off and then we get our constraints back. All right. So everything else we just leave at default pretty much. I'm going to go back to this setup here. And what controls this strength is how strongly these pieces are being guided by this piece, right? So if I turn this to zero and play that, then pretty much they'll just drop away straight away. See that's changed color. Now they're just moving independently. So we can use this value to control, you know, when they're being kind of moved by this. So basically when, you know, this is also playing with, if we go into the simulation settings, we've got these guide release thresholds. So the angular threshold and linear thresholds. So based on these two values, when this is pulled away quickly or, you know, a long distance or if it's angled, so if it turns away from this, you know, around these values, then they'll break and they'll be released. Okay. So I want to use that same thing that we used in the previous simulation. So this object here, which is kind of like a guide for when pieces should fall, whenever the pieces are inside that, then they become active and they fall. So I'm going to use this, right? I'm going to drop a null here and call this out. Let's call it weak out. Weak. Okay. Copy that. Come out here. Back to my horizontal cables. I was trying to simulate. Just go back to the first frame there. Okay. Give myself some space because I'm going to do it before this simulation. Object merge. Paste that in. Okay. And then maybe we don't need to visualize that. I want to visualize this. So just to make sure that, you know, it captures everything. We'll need to move it up a little bit. Maybe just by one is enough. Okay. So just stretch that forward. You can see what's going on there. So that's fine. Now, I'm going to group the proxy geometry. Any kind of attributes that you want to be controlling the simulation. So I'm on the last frame. Back to the first frame. So things like anything like velocity or force or I don't know, affecting the gravity should be on the proxy geometry. Okay. All coming through here. So just bear that in mind. And also attributes for the guided simulation as well. So I'm going to group these. I'm going to call this week. Let's do this on the points. Okay. Again, simulation attributes tend to be on the points. Constraint attributes on primitives. Other stop a wrangle. Attribute wrangle. Again, on the points. That's fine. And then I'm just going to create a new attribute. So F at week is make it strong. So four, we can play around with that value. Basically, I'm going to be using this to control this strength attributes. Right. So that back to one to default. There we go. And just copy that. And then set that group and set it to zero. I think it should work for us. Maybe it's one. Just so it doesn't break away completely, but it's easier for it to break away. So things in this group will basically be released from this simulation easily. So basically, when they start to fall, this value is applied to these parts inside this box. And then they're allowed to pop and break away from from this. Obviously, we don't want these cables being pulled down here. We want it to be we can be released. But then these parts to still be guided by this by the animation there. OK. So to bring that in, make sure it works. Go back to the first frame. Back into our simulation into this guided part. And then to set up and use vex expression to bring in that attribute. So we're going to be controlling that strength. OK, that's the name of this variable strength is. And then we're just going to set it to F at week. It's as simple as that. That's it. So all we have to do in here. But a couple of other things I want to do. So back to solver. Obviously, to get that sense of scale again, I'm going to bring down the gravity to this as well. And also I'm going to add some drag to slow the movement of this. So I don't want them bouncing and flopping all over the place. Right. So I'm going to give this a lot of air resistance. I'm going to set this to five. Really slow it down. That's a very high value for air resistance, especially if you had things kind of freely flying in the air. But these are constrained. So they're more, you know, it's a sense, you know, it causes the cable. I don't think I'd ever use a value like this if it was pieces which are loose and flying and tumbling around on the floor. OK. So let's just play that through a little bit and see if it works. Maybe I'll do a quick flip book. Well, we can see it releasing there already. Well, yeah, so these pieces in the middle will be, you can see them kind of popping up. As these start to fall down. So you can see the parts in blue here are still connected. So they'll still be following that animation. But in the middle, as it starts to fall, it becomes inside this group and then starts to break and fall just watch out again, you can see it getting pulled across. And then as it releases, it kind of springs back up again. That's kind of what I was looking for. Great. So let's cache this out. We'll drop in another avidio. We'll do this exactly the same way as before with the geometry and the points. So geometry and points there. OK, make sure you're on the first frame to save this. Rest geometry. So let's call this. We'll make another folder. Call this the. Now, sorry, horizontal. Horizontal. Cables. Fold slash. Rest. Pseo. Just copy that whole thing, paste it in here. Save that. And then this will be. Horizontal. Sim. And then here we need dollar F three. Again, make sure you don't have dollar F in this part. We only needed at the top. For our. So that we simulate each frame. OK. I think I already did that, but save that. And then you will save 125 frames. That's fine. Save that to disk. And we can continue from there.

**Frame:** tutorials\frames\week-02-04-finishing-the-horizontal-cable-sim-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Fix guided sim constraint popping (disable Remove Intro-Guide Constraint). Add `f@weak` attribute: default=4 (strongly guided), override=0 in active/falling zone → feed into Guided Sim strength VEX (`strength = f@weak`); pieces in falling zone release from guide naturally. Air Resistance=5 for scale-appropriate cable drag. File Cache: rest.geo + sim $F3.bgeo.sc.

### Summary
9m3s VFX School Archive module. Continuation of Week 2 horizontal cable sim. Fixes constraint popping by disabling "Remove Intro-Guide Constraint" in the Guided Sim constraints tab. Introduces `weak` group: wrangle sets `f@weak=4` on all proxy points, then `f@weak=0` for points inside the active/falling zone (object-merged from Week 1 active boundary). Feeds `f@weak` into Guided Sim strength via VEX expression. Reduces gravity for scale; sets Air Resistance=5 (high for constrained cables). Caches rest geometry + sim frames.

### Key Steps
1. **Fix constraints popping**: Guided Sim → Constraints tab → uncheck **Remove Intro-Guide Constraint** → constraints restored
2. **Strength attribute control**: Guided Sim → strength parameter slider; 0 = pieces drop immediately (no guide); 1 = fully guided; use to tune release
3. **Guide Release Thresholds** (Guided Sim settings): angular + linear thresholds — pieces break from guide when moved too far/fast
4. **"Weak" group setup** (on proxy geo points):
   - Object Merge: import active boundary from Week 1 sim
   - Attribute Wrangle: `f@weak = 4;` on all points (strong guide)
   - Group SOP using bound → "weak" group for points inside falling zone
   - Another Attribute Wrangle: select "weak" group → `f@weak = 0;` (or 1 — easier to break away)
5. **Connect to Guided Sim**: Guided Sim → Setup → VEX Expression: `strength = f@weak;`
6. **Bullet Solver settings for scale**: reduce gravity; **Air Resistance = 5** (very high drag for constrained cable objects — prevents flopping; would not use this value for freely tumbling pieces)
7. **File Cache**:
   - Rest geometry: `horizontal/cables/rest.geo` (static, no $F)
   - Simulation: `horizontal/sim/$F3.bgeo.sc` ($F3 = 3-digit frame number)
   - 125 frames; Save to Disk
   - Important: constraint attributes on primitives; simulation attributes (velocity, force, gravity) on proxy geometry points

### Houdini Nodes / VEX / Settings
- Guided Sim → Constraints tab → **Remove Intro-Guide Constraint**: OFF (fix constraint popping)
- Guided Sim → strength: slider 0→1; 0 = no guide; VEX expression override
- Guide Release Thresholds: angular + linear
- Attribute Wrangle: `f@weak = 4;` (all points), `f@weak = 0;` (weak group)
- VEX in Guided Sim: `strength = f@weak;`
- Bullet Solver: gravity reduced for bridge scale; **Air Resistance = 5** (high for constrained cables)
- **File Cache**: rest.geo path + sim path with `$F3`; constraint attrs on prims; sim attrs on proxy geo points
- Object Merge: bring in active boundary (Week 1 sim)
- Group SOP: bound mode → "weak" group

### Difficulty
Intermediate

### Houdini Version
H17.5+

### Tags
[rbd, guided-sim, bullet, cables, air-resistance, file-cache, strength-attribute, bridge, intermediate]

---

## Related Tutorials
- week-02-03-starting-the-guided-sim-v1-1080p.md (setup: constraints, RBD configure, guided sim start)
- week-02-07-starting-the-vellum-sim-v1-1080p.md (next: vertical cables Vellum sim)
- week-01-11-rbd-configure-v1-1080p.md (active attribute animated boundary, Week 1)
