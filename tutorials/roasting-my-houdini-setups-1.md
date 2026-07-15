---
title: Roasting my Houdini Setups #1
source: YouTube
url: https://www.youtube.com/watch?v=rvDsbo3slXc
author: cgside
ingested: 2026-07-13
houdini_version: "21.0.303"
tags: [for-loop-optimization, capture-by-proximity, labs-file-cache, rig-doctor, wedge, retrospective, best-practices]
extraction_status: complete
frames_dir: tutorials/frames/roasting-my-houdini-setups-1/
frame_count: 14
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Roasting my Houdini Setups #1

**Source:** [YouTube](https://www.youtube.com/watch?v=rvDsbo3slXc)
**Author:** cgside
**Duration:** 13m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So I've been digging into my old setups, mostly setups that I've shared on Patreon and on YouTube, and I wanted to see if I would do it differently today.
[0:13] Mainly getting rid of poor loops and unnecessary operations. So in this first file I have this I start from a sphere and I get this sort of animation.
[0:26] This was part of a Patreon tutorial about a year ago. So basically I will go through the file and show you what I would change in year.
[0:37] So first of all I transform the sphere to have this sort of shape and the first operation I'm doing this for loop is to extract the group, these are horizontal lines.
[0:49] And the way I'm doing that is iterating over each ID that I set in here so I can show you that ID. So I divide these intersections and I iterate over them.
[1:00] And what I do is to do a group by range and select one of every other vertex. But as you can see when I promote it to wedges, it also selects this part because this one in here it collapses to a single point.
[1:13] So it messes up our selection and then I just do a very cheap max edge length in here to subtract or to intersect with the existing group.
[1:22] And that works but we have to do this in a loop, which is not ideal loops are complicated. You have to think twice before you drop a loop.
[1:32] There are situations you really need it needed like feedback loops and whatnot or to divide the operations into chunks like doing a poly reduce, a multi-traded poly reduce, for example, but most of the time we can avoid them.
[1:45] So in order to select this group, that's by the way I need to create the rig. So when I come in here and do the rig as you can see, I need to divide these intersections.
[1:57] And this files will be available on Patreon by the way, but how did I overcome the loop?
[2:04] So what I'm doing in here is selecting all the vertices that have a neighbor count less than five. So in here we have five. So I just want to select all the vertices, all the vertices, but these ones at the extremities.
[2:23] Then I do the final selection, so one out of two by finding the current vertex number in that group we just selected.
[2:32] And if we found if we found a vertex in that group and is every other one, we can select, we can append it to the group.
[2:41] And finally we just need to promote it to edges and there you go. You have the group clean that we can later use to do the reading.
[2:48] So that was easy, right? Now what's next? In this next example, I have this geometry and this geometry prepared for rigging.
[2:58] And in order to use the rig doctor, we need to have individual pieces, but also these middle sections connected to the field with these horizontal sections.
[3:11] So for that in a loop again, I write over them, I field the points as you can see.
[3:16] So as you can see, I field the points and then I polypads and this is necessary, a necessary operation to have a proper rig doctor.
[3:25] And again, we did it, I did it with a for loop, but there's an easier way since we have a class attributes or in this case I call it prem ID.
[3:34] We can just promote it to a point attributes and call it point ID and then we fuse and match the attribute point ID this way.
[3:42] We don't fuse points between between each ID and then we polypads and as you can see the rig doctor will not complain if we don't fuse by ID.
[3:50] As you can see, this will not work because it couldn't rebuild the hierarchy.
[3:56] So that was also very easy and the last step which is a bit more complicated is when we do the capture by proximity.
[4:04] So we have the rig, we have the geometry to capture and since we are doing a capture by proximity, if we don't do it in a loop, so isolating each piece and the same in here and doing the proximity, this won't really work.
[4:21] I can actually show you, so if I duplicate this capture and connect in here and connect this to the rig and I do this and then I append it to here.
[4:30] If I do the bond the form, as you can see, it will not separate the parts and it will be a mess.
[4:37] But when we do it in a loop, so let me show you, as you can see, this will work.
[4:43] But how can we avoid the loop? So that's what I did in here. But we need to, as you can see, I have, let me show you first, as you can see, I have this working in here perfectly without the loop.
[4:55] But in order for that work, we need to move the geometry, we need to separate the geometry and move it to a rest space.
[5:03] So as you can see in here, I have this rest space and I have the same for the UV, so they are separated enough that we can do the capture by proximity and then we can swap it back to the rest position that I'm saving in here.
[5:14] And as you can see, this will work just fine because we capture in a rest position where there's enough space to do the capture by proximity.
[5:22] But how am I creating this geometry? So this is the UV geometry actually.
[5:28] So if we go above where I have this geometry, I do a simple UV flatten and I get this sort of UVs, then I orient the UVs up with this HTA and by the way, let me allow editing of contents.
[5:41] I share this before, but in case you don't have it, you will have access to on Patreon.
[5:45] So this is something I share before this UVs up, this just orient them up and then I do a UV layout and I lay them out this way by using a fixed size and just playing with the settings in here with the scale.
[5:59] This way I can have enough space. Then it's simple, we just promote the UVs to a point attribute and do a natural but swap UV to be or just in a wrangle or something like that, you can do the same.
[6:10] And we do the same in here, you have to be and as you can see, those UVs that we created above, they will propagate to the rig geometry, to the curves because we extracted, we constructed everything with the same geometry.
[6:27] And that's the beauty of proceduralism because we can keep creating geometry and having the attributes transferred and everything in the end works pretty well.
[6:38] So as you can see now everything is working in here.
[6:42] So yeah, that was the first example and then I wanted to show you an extreme case.
[6:48] Okay guys, now in this last example I wanted to show you an extreme case where I have animated geometry and I am doing the loops on the animated geometry.
[6:57] I wasn't very proud at the time but I didn't found another solution in time and I had to release the tutorial.
[7:03] So let's have a look at what I would do today.
[7:06] So the first thing I do in here after creating the simple animation of the jellyfish in this case, I wanted to create variation.
[7:15] So in a forward loop, I do basically a time of sets and I speed up or slow down a bit of the animation ending up with different variations that I can later copy to points and have different variations of the same jellyfish.
[7:32] And how can we avoid doing this loop with animated geometry which is a pain.
[7:39] So what I ended up doing was doing a live file cache and creating in this case three variations the same as we have in here.
[7:47] So I did three copies in here.
[7:49] So labs file cache which includes wedge, wedge feature, same as we have in top.
[7:56] But this one is really simple to set up so you set the wedge count and I create an attribute called seeds that I can feed to the time shift to offset in a random frame and to a time blend that I can use to speed up or slow down randomly each variation.
[8:12] And then at the end I can just load all the geometry, all the variations and also wedges to merge.
[8:19] I set to all wedges so it loads every single variation as you can see.
[8:24] And now I also need in this case I have this copy num so an ID for each variation and in order to create that ID in the file cache you have these let me see file ID X that I later renamed to copy num to play well with my copy to points.
[8:42] So if we go in here as you can see we have about 120 frames per seconds if we do the first solution we get about 40 as you can see then with the copy to points everything gets slow down but that is normal.
[8:53] Okay guys that was the first example of these labs file cache know this really amazing I have to use it more.
[9:01] Now it comes a very hard part that I had no idea how to do this in a proper way basically I have these trails so let me show you first in here I have these trails that I simulated with volume let me slow it down and I want to mesh it with a sweep but without a proper up attributes I can't really have them stable because they are rotating all around and whatnot so what I need is the.
[9:30] Now I have a attribute that points into the geometry and now I did that previously was by creating a group expression and selecting the first point of each curve then group expanding to a flood field geometry and save a step attribute like the CG wiki video that I will link below that does this so we can later fuse.
[9:52] So I can show you you can fuse and study to average and match vegetables tap and this will create a curve in the middle that we can later use with an oriental along curve to create the normals using this banking how is it called banking curves so if I don't do this we get this sort of result which will not be stable for our sweep so we do this and I do this in a loop and we get all the variation but this is animated loop which I really don't.
[10:21] So what I ended up doing was promoting I have a premium ID as you can see on each variation and I promote that to a point attribute called ID X and then in here I take the step attribute from this group expand I take the step attributes and the ID X and I just multiplied by a big value so we have in a variation for the step attributes so it's not the same on every curve and then I just fuse.
[10:51] And we can do this without a loop so we fuse by that step attribute.
[10:56] The thing is when let me set this to zero and go in here and let's see how much the performance of this so let me increase so we get pretty good performance with a loop which I didn't worry too much at the time so it was performing well but when we do this without the loop look at this we get down to 40 frames per second and I was wondering why is that.
[11:20] So the reason is if I enable the second option we get about the same performance back as you can see and what's the difference both are using that match attribute but this fuse the one that performs well is using a snap distance so we feel constrained the fuse to a snap distance even if you're matching by attribute it's always a good idea to use that snap distance so the fuse no doesn't have to calculate an infinite infinite radius let's say.
[11:49] So you can see how much difference that makes from about the max frames per second to all the performance or something like that so as you can see that makes a lot of difference and then later so if we set this to one the green one and we compare it at the end as you can see we have a stable orientation
[12:13] everyone there why your sweep geometry is rotating around normally well that's because you don't have a stable attribute and normal so that's what I'm doing in here although I'm using also some roll to twist it a bit in the sweep but anyways that is basically it's.
[12:30] So guys I really hope you enjoyed this it was something I wanted to share with you.
[12:37] Of course with time we learn new things and we we can improve but hopefully this was helpful also to you and I encourage you to go through your old files and try to improve them again I really advise you to avoid for loops when you can and do it in a more with subs or with wax and try to optimize your setups as always you can grab the files on my Patreon please leave a comment below because I don't ask for life or substrations or anything like that but I always like to wear your feedback.
[13:06] I always like to wear your opinions in the comments so if this was useful to you or you have something to add please let me know in the comments and as always thank you for watching and I guess I'll see you next time thank you.



---

## Captured Frames

- [0:25] tutorials/frames/roasting-my-houdini-setups-1/frame_000.jpg
- [0:55] tutorials/frames/roasting-my-houdini-setups-1/frame_001.jpg
- [1:40] tutorials/frames/roasting-my-houdini-setups-1/frame_002.jpg
- [2:45] tutorials/frames/roasting-my-houdini-setups-1/frame_003.jpg
- [3:40] tutorials/frames/roasting-my-houdini-setups-1/frame_004.jpg
- [4:20] tutorials/frames/roasting-my-houdini-setups-1/frame_005.jpg
- [5:00] tutorials/frames/roasting-my-houdini-setups-1/frame_006.jpg
- [5:50] tutorials/frames/roasting-my-houdini-setups-1/frame_007.jpg
- [7:00] tutorials/frames/roasting-my-houdini-setups-1/frame_008.jpg
- [7:50] tutorials/frames/roasting-my-houdini-setups-1/frame_009.jpg
- [9:20] tutorials/frames/roasting-my-houdini-setups-1/frame_010.jpg
- [10:20] tutorials/frames/roasting-my-houdini-setups-1/frame_011.jpg
- [11:20] tutorials/frames/roasting-my-houdini-setups-1/frame_012.jpg
- [12:10] tutorials/frames/roasting-my-houdini-setups-1/frame_013.jpg

---

## Structured Notes

### Core Technique
A retrospective "what I'd do differently today" review of old Patreon/YouTube setups, focused entirely on **replacing unnecessary for-loops with VEX-native alternatives**: vertex-neighbor-count-based group cleanup instead of a looped edge-group builder, fuse-by-point-ID instead of a looped weld-per-piece step, a rest-space UV-layout trick to make Capture by Proximity work without separating geometry in a loop, Labs File Cache's built-in **wedge** feature instead of manually re-time-shifting animated variations in a for-loop, and a critical reminder that `fuse` should always use a **snap distance** even when matching by attribute, since omitting it can silently tank performance from ~120fps to ~40fps.

### Summary
The first old setup builds a rig from a sphere: originally, extracting a clean "every-other-vertex" edge group required a for-loop iterating over per-section IDs, because promoting a raw group-by-range selection to edges also picked up unwanted collapsed-to-a-point selections at the poles. The improved approach: select all vertices with a **neighbor count less than 5** (isolating vertices away from the pole extremities), then in a second pass find each vertex's own vertex-number within that subgroup and keep only every other one (`vertexnumber % 2`) — producing the same clean edge group with zero loops. The second setup needs rigging pieces both individually-separated (for Capture) and reconnected via horizontal bridge sections (for Rig Doctor); originally a for-loop fused points per-piece and Polypath'd them together — the fix: **promote the per-piece class/prim-ID attribute to points** and Fuse using **match-attribute-by-ID** so points aren't fused across different IDs, letting Polypath run once globally without a loop. The third (hardest) case is **Capture by Proximity**, which requires each piece to be spatially separated to avoid neighboring pieces bleeding into each other's captures — originally done in a for-loop, isolating each piece individually. The loop-free fix: build a **rest-space UV layout** — UV Flatten the geometry, run the channel's own "Orient UVs Up" HDA to align island orientation, then **UV Layout** (fixed scale) to physically spread all islands apart in UV space; promoting those UVs to a point attribute and swapping them into the position attribute (via a wrangle or Attribute Swap) gives a fully separated "rest" version of the geometry with guaranteed inter-piece spacing for Capture by Proximity to work correctly without ever looping — and because everything is procedural, all downstream attributes (rig curves, etc.) built from the same geometry automatically inherit this rest-position UV data. The fourth case covers **animated geometry variation** (a jellyfish): originally a for-loop applied per-copy Time Offsets/speed changes to create variation before Copy-to-Points, which the presenter "wasn't very proud of." The fix: **Labs File Cache**'s built-in **wedge** feature (wedge count + a per-wedge `seed` attribute fed to Time Shift for a random offset frame and Time Blend for random speed) bakes all variations to disk in one pass, loaded back with "all wedges" merge mode and a `copy_num` attribute (renamed from the file cache's `file_id_x`) for Copy-to-Points — reported at ~120fps for the file-cache approach vs. ~40fps for the old for-loop, with Copy-to-Points itself adding further overhead regardless of method (a separate, expected cost). The final and hardest case involves **animated particle-trail meshing without a for-loop**: originally, each animated trail curve needed a stable "up" vector for Sweep, built per-curve inside a loop via a CG-Wiki-style technique (Group Expression selects each curve's first point, Group Expand floods that selection along the curve, saves a "step" attribute, then Fuse-and-average creates a smooth guide curve, Orient Along Curve derives stable banking normals from it). Removing the loop requires per-curve **class-ID offsetting**: promote each curve's primitive-ID to a point attribute (`ptnum_x`), multiply the CG-Wiki "step" attribute by that ID times a large constant so each curve's step values land in a non-overlapping numeric range, then **Fuse by that combined step attribute across all curves at once** (no loop needed) — but critically, Fuse must use a **snap distance** even when matching by attribute, since Fuse-by-attribute-only still computes distances internally; skipping the snap-distance constraint dropped performance from ~120fps to ~40fps in testing, while adding it back (even at a workable but not perfectly tuned value) restored near-full performance — "always use a snap distance, even when matching by attribute."

### Key Steps
1. **Loop-free alternating-edge group:** select vertices with a neighbor count under 5 (excludes pole extremities), then within that subgroup keep only every-other vertex-number (`vertexnumber % 2`), avoiding the pole-collapse artifact a naive group-by-range-then-promote-to-edges approach produces.
2. **Loop-free per-piece fuse + Polypath:** promote each piece's class/primitive-ID to a point attribute, then Fuse using match-attribute-by-ID so fusing never crosses piece boundaries — Polypath can then run once globally instead of inside a for-loop.
3. **Rest-space separation for Capture by Proximity (no loop):** UV Flatten the geometry, run "Orient UVs Up" (the channel's own HDA) to align island orientation, then UV Layout (fixed scale) to physically separate all islands apart in UV space.
4. Promote the resulting UVs to a point attribute and swap them into position (rest attribute) — this separated rest-space geometry lets **Capture by Proximity** work correctly for all pieces at once without ever isolating pieces in a loop; downstream rig/curve geometry built proceduraly from the same source inherits this rest data automatically.
5. **Loop-free animated-variation baking:** instead of a for-loop applying per-copy Time Offset/speed changes, use **Labs File Cache**'s wedge feature — set a wedge count and feed a per-wedge `seed` attribute to a Time Shift (random offset frame) and Time Blend (random speed) to bake all variations to disk in one pass.
6. Load the cached wedges back with "all wedges" merge mode; rename the cache's `file_id_x` attribute to `copy_num` for direct use in Copy-to-Points — measured ~120fps vs. ~40fps for the old per-copy for-loop approach (Copy-to-Points itself still costs some overhead regardless of the upstream method).
7. **Loop-free animated-trail stabilizing:** build the CG-Wiki-style stable guide-curve technique once per class instead of in a loop, by promoting each curve's primitive ID to a point attribute and multiplying the "step" attribute by that ID times a large constant, giving each curve's step values a distinct non-overlapping numeric range.
8. **Fuse by the combined (ID-offset) step attribute across all curves simultaneously** — no for-loop needed since the offsetting guarantees no cross-curve collisions.
9. Always add a **snap distance** to Fuse operations, even when matching by attribute — Fuse still performs internal distance checks, and omitting the snap distance measurably degraded performance (~120fps → ~40fps) in this exact case; adding it back restored near-original speed.

### Houdini Nodes / VEX / Settings
Vertex-neighbor-count wrangle (`neighbourcount() < 5`), `vertexnumber % 2` alternating-vertex wrangle, Group Promote (edges), Attribute Promote (class/ID → point), Fuse (match attribute by ID, snap distance), Polypath, UV Flatten, custom "Orient UVs Up" HDA, UV Layout (fixed scale), UV-to-position Attribute Swap (rest-space build), Capture by Proximity, Labs File Cache (wedge count, wedge feature), Time Shift (random seed offset), Time Blend (random speed), `file_id_x` → `copy_num` rename, Copy to Points, Group Expression (first-point selection), Group Expand (flood-fill along curve), Fuse + Average (guide-curve smoothing, CG-Wiki technique), Orient Along Curve (banking normals), primitive-ID-offset "step" attribute wrangle (`step + ID * large_constant`), Sweep.

### Difficulty
Advanced (each "fix" replaces a for-loop with a non-obvious, purpose-built VEX/attribute technique — especially the rest-space UV-layout separation trick and the ID-offset step-attribute fuse for animated trails).

### Houdini Version
21.0.303 (visible in viewport title bar).

### Tags
for-loop-optimization, capture-by-proximity, labs-file-cache, rig-doctor, wedge, retrospective, best-practices

---

## Related Tutorials
- [Tips and Tricks to level up your Houdini Skills](tips-and-tricks-to-level-up-your-houdini-skills.md) — companion "lessons learned / better workflows" tips video from the same channel, focused on rest-attribute Clip tricks and RBD Pack Inject swaps.
- [Think Procedural Think Houdini](think-procedural-think-houdini.md) — shares the "avoid unnecessary for-loops, use pcopen()/pcfilter() growth-style solvers instead" philosophy demonstrated here.
- [Orient UVS like a PRO in Houdini 21](orient-uvs-like-a-pro-in-houdini-21.md) — the "Orient UVs Up" HDA referenced and reused here for building the rest-space UV layout.
