---
title: week 04   06   cull by speed v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=UFrvmv0rwQI
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18+"
tags: [particles, rain, vex, wrangle, cull, velocity, speed, file-cache, beginner]
extraction_status: complete
frames_dir: tutorials/frames/week-04-06-cull-by-speed-v1-1080p/
frame_count: 4
---

# week 04   06   cull by speed v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=UFrvmv0rwQI)
**Author:** The VFX School Archive
**Duration:** 7m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, let's come up here. Check load from disk and then we can scroll forward. You can see it plays back super fast. It's only points. They don't take much time. So, let's take a look at a flip book. I'm just going to drop a merge and then just connect that right to the top um for preview purposes. Turn that on. So, it's kind of hard to see here. You know, these points are really big. Um, so I'm gonna come out here and go press D on my keyboard and go to geometry and then change this. So particles display. We can display them as pixels. They're just tiny points. Or we can go to uh points and just make it smaller. Maybe I'll do that. Well, that looks pretty good. 1.5 seems about fine. And then let's get rid of this ground plane. Maybe I'd just add some quick color to this as well. Okay. Under there. And just some kind of dark brownie color. Desaturated. Darker than that. Uh, you know, don't worry about copying this. I'm We'll probably come back to this later for the uh, you know, before rendering. Um, less color than that. Still kind of looks brown there, doesn't it? Well, that'll do. Um, okay. And then, well, actually, if I just come here, I want to show you, um, you know, something I noticed later on into the sim, we start getting I kind of had to see now that I made it small. Uh, let's do that. So, you can see some points flying up there. So, they're colliding with the geometry at the bottom. Uh, so our points are falling, but they're, you know, this this this geometry is static and, you know, there's something weird going on. You see some points exploding there. So, well, as you can see, you know, with with the particle so small, it probably won't really see it. Maybe a couple, but just in case, what we can do is just drop a wrangle. I'll do this right after the um after the cache. Okay. And let's just do a quick um you know kind of coloring the the points based on their speed. So float speed is something I do pretty often. So length because the we need a a single float value for the speed, right? Um we take the length of the velocity that will give us the length, right? So just the one value. Well, essentially, yeah, it gives us the speed. So, where are we on point? It's not an attribute. It's just a variable in here. That's why we're not seeing it. But we will have a a number, right? If I if I just do this actually then we should see it there. So, you can see we got a value between zero and 160. It might be better to do that, you know, so you can actually see the numbers, but it's not necessary and I'd probably want to delete it after. So I'll just do that. Float speed is the uh length of the velocity. And then we want to delete points if they are slower than a certain amount. Right? So if the speed is uh more than no sorry if they're faster. Yeah. Then we'll make a channel a float and we'll just do like speed call. I don't know if that's supposed to have double L. I'm not sure. Speed cull. Oops. Um. Oh, not that. Okay. And then curly brackets. Curly bracket. Close. And what do we want to do? We want to remove point the first input and the current points which will be at PT num. Okay, simple as that. So click here. Now you can see it's deleting everything because we are got a really low value. So if we take this up now, if we go up uh let's go to the end where we've got points flying up there. So obviously these points up here we're kind of looking at, right? So that's just going up to one. So somewhere around there 20. There we go. Something like that. About 10. Okay. So, so we're not, you know, I'm just, it doesn't look like we're deleting points which are falling, just the ones which are kind of flying up here. Um, there are still some coming up there. You can see, but from the point of view of the camera, I don't think Whoops. What have I done there? I don't think we'll actually see them. And if we do, we won't notice because it's literally just a couple of points, right? So, okay. So, let's uh like I said, just do a flip book of this. Maybe we should have a brighter color for, you know, just so we can see it. No, we can see it well enough, I think. So, I'm going to go back to the start and maybe zoom in a bit. Go down. We don't need to see above the bridge really. Maybe I'll do something like that. Cool. So, let's have a look at that. So, that's looking good. Kind of like the pattern. So, if I go back here, you know, we're still getting kind of blotches and streaks. It's not too kind of misty, you know, like I was saying, especially there. This part I really like these kind of this pattern of of um thicker areas and lighter areas. Also, you get a sense of it kind of colliding with the bridge there, which is nice. Uh I think along here there's a part where you not see Yeah. kind of bouncing and coming off the edge. It's nice to see some interaction between and yeah, bouncing off the road there. Um, and I'm I can't see any bits kind of flying up from the bottom. That could change with the render. You know, it might be worth uh, you know, having a having a Oops. What am I done there? Having a good look at the render a couple of frames just to make be sure, especially, you know, if we're adding motion blur, you might see a streak flying up and that would be kind of weird. But, um, no, looks really cool.

**Frame:** tutorials\frames\week-04-06-cull-by-speed-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Cull exploding particles from cached rain sim using speed threshold: `float speed = length(@v); if (speed > ch("speed_cull")) { removepoint(0, @ptnum); }` — removes particles going faster than ~10-20 units/frame (collision artifacts) while keeping normal rain fall.

### Summary
7m0s VFX School Archive module. Part of Week 4 rain particle sim on the Manhattan Bridge. Loads cached point sim, adjusts viewport display (pixels or small points, size 1.5). Discovers points flying upward from bridge geometry collision artifacts. Fix: Attribute Wrangle after file cache reads velocity length as speed; `removepoint` for points exceeding threshold (ch("speed_cull") ≈ 10-20). Flipbook preview shows rain interacting with bridge, bouncing off road, with filtered-out erroneous flying particles.

### Key Steps
1. **Load from disk**: File Cache → enable "Load from Disk" → fast playback (points only)
2. **Viewport display**: press D → Geometry → Particles display=Pixels (tiny); or Points, size=1.5
3. **Diagnose problem**: some particles fly upward (collision with bridge geometry produces wrong velocity)
4. **Cull by speed** (Attribute Wrangle after cache):
   ```vex
   float speed = length(@v);
   if (speed > ch("speed_cull")) {
       removepoint(0, @ptnum);
   }
   ```
   - `length(@v)` → scalar speed from velocity vector
   - `ch("speed_cull")` → creates slider; set to ≈10-20 to remove only fast/exploding points
   - Normal rain ≈ 0–10 speed; exploding artifacts ≈ 100–160+
5. **Flipbook** preview — confirm normal particles preserved, flying artifacts removed
6. Note: if adding motion blur at render, worth checking that no streaks from culled particles remain visible

### Houdini Nodes / VEX / Settings
- File Cache: "Load from Disk" checkbox for fast cached playback
- Viewport: D → Geometry → Particle display = Pixels or Points; point size = 1.5
- **Attribute Wrangle**: `float speed = length(@v);` + `removepoint(0, @ptnum);` based on speed threshold
- `ch("speed_cull")` → slider parameter for threshold (≈10-20 units/frame for rain)
- `length(@v)` → extracts scalar speed from velocity vector

### Difficulty
Beginner

### Houdini Version
H18+

### Tags
[particles, rain, vex, wrangle, cull, velocity, speed, file-cache, beginner]

---

## Related Tutorials
- week-03-01-intro-v1-1080p.md (week 3: cars on bridge)
- rain-effect-in-houdini-houdini-tutorial.md (different rain tutorial with POP + VDB collision)
