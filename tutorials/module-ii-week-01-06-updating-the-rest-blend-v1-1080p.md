---
title: module ii   week 01   06   updating the rest blend v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=aUkXMjjLT-k
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [vellum, rest-blend, bend-sop, bounding-sphere, group, soft-body, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-01-06-updating-the-rest-blend-v1-1080p/
frame_count: 4
---

# module ii   week 01   06   updating the rest blend v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=aUkXMjjLT-k)
**Author:** The VFX School Archive
**Duration:** 12m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now, when we come to simulate the whole thing, we'll find that the position of the body of the hunter kind of stays. So this is the rest position of the body. And if he's going to be kind of holding his arms up like this, as if he's holding a gun which kind of looks weird. So what I want to do is just, I'm just going to bend the arms down because that's the most noticeable thing. You could kind of straighten the legs out or put them in some kind of other pose, but I just want to bring the bend in these elbows out. And then I'll show you how we can bring that into the simulation after the first frame. So first we need to bring a difference, bring this off to the side here. Okay, we're going to group the arms. So I want the left, climb us separately, left arm and the right arm. Right arm there. Okay, and then we're going to do this on the points here. We're going to use bounding region, bounding sphere. And if I grab the tool, I can bring this over. Yeah, obviously I don't want to bend all of the body. Just each arm individually. And then just going to bring that over. Okay, let me, I'll just, um, drop in the values which worked for me. Okay, points. So here are points, six, seven, six, one, two, three, four, six, six, eight, four, two, zero point eight, two, four, nine, eight, four. And then the center will put it, points, two, one, two, three, eight, one, point zero, two, oops, not it's two, six, one, three. And then four points, we've got there two, one, four. Okay, so then I'll just grab the left arm there. And then for the right arm I found because it's a bit weird here, so you can't rotate to these shapes when you use bounding region within the tool. So what you can do is just drop in another object, other geometry, right? So if I, I can just grab a, um, a sphere here, we had rhyme, just use a polygon mesh with that. Okay, um, polygon mesh, sorry, don't need too much subdivision with that. But again, we just plug that into the right input and then changes to points, keep in bounding region, bounding object. And then when I move this sphere over, it's a bit difficult like this because you can't see while you're moving this around, you can't see the selection unless you select this. Okay, but, um, you know, what, what you can do, rotate, which is what you can't do here, which I needed to do to grab that, that, that right arm. So let me just drop in these values as well, very quickly. So in radius zero point, one for, uh, five, one, eight, four, uh, point one, two, three, three, eight, one, point four, three, eight, four, five, seven, center, minus, four, five, two, five, seven, two, three, one point, zero, six, two, one, I really should round these numbers up there. Here we are. One, take two long, three, point seven, nine, one, five, and then the rotating y. Like I said, we need to rotate it a bit because otherwise it's grabbing the, uh, the, the torso there, point six, six, eight. I think that should be as good. There we go. Yeah. So you can see it kind of just grabs the right arm there. Okay. And then the bend tool. Okay. And then obviously setting this up for points with the left arm. Okay. Okay. So right away you can see you get this kind of bend thing there. And if I move that, you can see it's kind of bending the whole arm there, which is no good. If we right click a countryman, the short cook cuts and click toggle, uh, capture handle. And then we get this handy. It gives more here. We can move this over and kind of bring it over to where we want to be actually bending it. Okay, which is at the elbow. I'll put that over like that. So yeah, this will be actually where the center of that bend will be. This will be how much of it will be bent. Okay. What region will be bent? And then this will, how much you're bending. That makes any sense, right? So you can see here which values are changing. So when I move this up and down, that's the bend. When I grab this red box, you can, if I can get it, move forward. That's the capture length. And then the capture origin is this whole gizmo. Okay. So again, I'll just drop in my values that worked for me with this. So for the left arm, that was minus and bend minus 53.2, a 3. And then the capture origin was 1, 2, 2, 5, 9, 7, 1.0, 5, 3, 4, 7, 3.9, 4, 7, 4, 7, 3.9, 4, 5, 6, 5. Okay. And then the capture direction, so a bit of rotation to it as well. Minus point 18, 7, 15, 2, minus point 7, 8, 4, 2, 3, 8, 0.5, 1, 5, 6, 1. And the capture length, so much shorter. So obviously we don't want the whole thing bending there. 0.05, 1, 0, 583, 4, that's one, great. Okay, so it might look a bit weird, but again, yeah, we're going to be deforming the original geometry. It doesn't have to be perfect. Okay, I'm just going to alt-click and drag to copy that and change this to right arm. Okay, there. And then we need to update the values for this one. So this is going to be minus 37. Typing in these values because it took a bit of time of playing around to get this to work well. And let's see what else. Now, let's go back to region 7. Minus point 343, 924, 1.0, 4, 3, 9, 8, 3.5, 8, 3, 4, 6, and the origin 0.0, oops. 0.0, 4, 6, 5, 9, 0.90, 7, 5, 3, 1, 0.4, 1, 7, 4, 4, and then the capture length 0.02. Oh, what's happening there? And it's you, which one is this left arm, right arm? Surely only working on the one group there. Okay, so yeah, it's not the most beautiful bit of modeling, bit of weird polygons there, but that's okay. It'll look fine on the final geometry. Okay, now I'm going to drop a null here. Roll this out, new rest, because that's what we're changing. We're changing the resposition of this topology, right? So we're going to go from this to this, basically. Okay, it's not a massive, excuse me, a massive difference, but should help us a bit. So let's go to frame 140, the beginning of our simulation. Jump inside to a dot network, I'm just going to turn off the collision with the crocdower moment and the gravity actually. Okay, I don't want any forces acting on my guy on this ground plane, just for the moment. And then what I'm going to do is drop in a volume, we type volume, we'll see all the volume tools we've got. Got this rest blend. Okay, and I'm going to plug that into the last port. Let's go into this merge. You can put them in line up as a matter. Okay, go into this rest blend and then find the constraints group, not the constraint group, I think. Oh yeah, sorry. Yeah, so we'll be changing the band and stretch constraints. That's right. Yeah. And we want to find the out in sup. So we'll go out and find that out to node. So which is in the hunter out new rest, grab it there. Okay, we want, you know, fully changed into that new shape. And we're going to do it in there. We're going to update it just once in the single frame on the first frame. Okay, so you could do, you could delay this, but in our case, you know, on the first frame is fine. Now if I just skip to the next frame, maybe we'll see also I'm going to go back and just put this down to one substep for now. That's fine. Let's just press play and hopefully we'll see the arms can see updates and change and then excuse me, bend out. There we go. Okay, so, um, skip on that to stop it. Go back before I forget to do it later. I'll put this back up to age sub steps and we can continue. Actually, let me jump inside and turn everything back on before I forget as well. Turn on the ground plane and the gravity. We'll continue from there.

**Frame:** tutorials\frames\module-ii-week-01-06-updating-the-rest-blend-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Vellum rest blend update: use Bend SOP + bounding sphere groups to repose character arms before simulation, then feed the new rest pose into the Vellum solver's Rest Blend node on frame 1 — this shifts the soft body's natural rest position mid-sim without a visible snap.

### Summary
12m37s lesson. Problem: soft body hunter holds arms in an unnatural raised gun position (rest pose). Solution: (1) create arm groups via bounding sphere/bounding object selection, (2) use the Bend SOP to reshape each arm to a natural lowered position, (3) feed this new geometry into a Rest Blend node inside the Vellum DOP on frame 1 of the sim (band + stretch constraint groups). The Vellum solver then gradually tries to match the new rest shape during simulation.

### Key Steps

**1. Group Arms by Bounding Region**
- Group SOP: group by bounding region → bounding sphere → move/size the sphere handle to isolate left arm
- For rotated shapes (right arm): use bounding object instead — plug in a polygon sphere, move/rotate it externally; Group → bounding object → pick that sphere → can rotate selection volume
- Create separate groups: `left_arm`, `right_arm`

**2. Bend SOP**
- Bend SOP: source type = points; group = left_arm
- Right-click viewport → "toggle capture handle" → reveals separate gizmos: capture origin (where bend pivots), capture length (how much geometry bends), bend amount
- Adjust: capture origin to elbow location; capture length to arm section only; bend amount (e.g., -53 degrees) to lower the arm
- Duplicate for right arm with different values

**3. Rest Blend (Inside Vellum DOP)**
- Go to first frame of sim (e.g., frame 140)
- Inside DOP network: disable gravity + ground plane temporarily
- Add Rest Blend SOP (from volume menu): wire into Merge/solver; last port is typically correct
- Configure: constraint groups = "band and stretch" (update these constraint types' rest lengths)
- Source: object merge/path to the new rest pose geometry (hunter's arm-bent geometry)
- Update each frame: OFF — update only on frame 1 (or desired frame)
- Result: on frame 1, all band+stretch constraints update their rest length to match the bent-arm shape; soft body now naturally tries to relax toward lowered-arms pose
- Re-enable gravity + ground plane

### Houdini Nodes / VEX / Settings
- **Group SOP** → bounding sphere: drag sphere handle to isolate arm geometry
- **Group SOP** → bounding object: use external sphere with rotation to isolate angled arms
- **Bend SOP**: capture origin (pivot point), capture length (reach), bend amount (degrees); right-click → "toggle capture handle" to access separate gizmos
- **Rest Blend** (inside Vellum DOP): "update each frame" = off; constraint group = "band and stretch"; source = new rest geometry path
- band + stretch: the constraint types whose rest lengths are updated to match new rest shape

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[vellum, rest-blend, bend-sop, bounding-sphere, group, soft-body, intermediate]

---

## Related Tutorials
- module-ii-week-01-04-tetrahedral-soft-bodies-v1-1080p.md (tet soft body setup)
- module-ii-week-01-02-introduction-to-vellum-v1-1080p.md (Vellum constraint types)
