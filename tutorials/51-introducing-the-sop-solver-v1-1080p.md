---
title: 51 introducing the sop solver v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=8HkP7iVgi0Y
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "Not specified"
tags: ["sop", "vex", "wrangler", "particles", "simulation", "beginner"]
extraction_status: complete
frames_dir: tutorials/frames/51-introducing-the-sop-solver-v1-1080p/
frame_count: 4
---

# 51 introducing the sop solver v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=8HkP7iVgi0Y)
**Author:** The VFX School Archive
**Duration:** 9m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Let's quickly create a new project to go over a brief introduction to particles and pops. So we'll go over to File, New Project, and I'll select the destination. I'll just call this Intro to Pops. It accepts and then I'll save the file. Intro to Pops. Here's your one. Now let's create a jump to Container and I'll call this Sub Solver Demo. Dive inside. Let's start by creating a grid and it's just going to be a one square mirror grid. It's fine. And now that grid will scatter some points. Let's say 100 points and we'll disable the relaxed situations. Let me disable the grid and also switch to a dark background. So clicking D, background, dark. So these are the particles or the points that we generated on the surface. A particle solver will do is essentially grab the points position and each points velocity and calculate what the next points position will be based on that velocity. Position is just a vector. So you have three floats for each one of these coordinates, x, y, and z. A velocity is also going to be a vector which with three floats for each one of the coordinates. And that vector is going to give us the direction of the movement and also the speed. The length of that vector is also going to give us the speed of the object. In this case the points. So what we'll do is we'll just create an attribute. I'm going to go to attribute create. And we'll create an attribute called v from velocity. It's going to be a type vector and we'll say that the value is going to be let's say one. So the velocity right now it's going to be the units as you know inside Houdini is in meters, the spatial units, the speed the velocity is going to be in meters per second. So right now I'm saying that will be these points have a velocity of one meter per second on the y axis. Nothing has happened. But if we were to do the calculation ourselves, we would for instance create a point wrangle and do a very simple line of code where we say that my position at p is going to be equal to my position plus my velocity. Same I call and we have some displacement happening. So this is before we calculate the new position. I'm going to call this create valve create V and here I'm going to call update position. So we updated the position as soon as this information comes in this line of code is applied to the points and we get a new position. But if you move the time slider, this doesn't continue to happen. Okay, we would need to apply this again. And those would keep moving and so on and so forth. And they would keep moving. Now of course we don't do this like that. There is a solver, a soft solver in Houdini. So you can just type solver that will be able to apply whatever operations you want to apply to your geometry through time. Meaning that it will take into account the previous frame to apply that operation on the previous frame. And so on and so forth going forward through time. So the difference will be that if we connect this here and we copy this update position control C inside the solver, you'll see that inside the solver we have input one and put two input three and before which will correspond to these inputs. And we have the previous frame. If we control V, the update position here and we feed it the previous frame. What this means is that on each frame, the solver is going to look at the previous frame and apply this this wrangle, this update position operation. If we go up now and we look at the solver, what we'll see is that the particles keep moving. We need to move through time. And you'll also notice that the timeline, let me just adjust this. We don't need as many let's say 120. So I'm just suggesting the length of our time outline. You'll notice that our timeline starts getting blue, which means that this is being cached. You also have a reset simulation here, which indicates that this is being simulated through time. Okay. Now this isn't correct because we know that our timeline is in in frames and our file is working at 24 frames per second. So if we have a look at this from a front view, space bar three and return on the grid. So if this is one unit or if this is one unit, okay, one, two, what we need to, what we would expect is after one second, knowing that the velocity is in frame in meters per second, after one second, meaning 24 frames, our particles should be at this position. But that's not what's happening. Okay. On each frame, it's jumping one mirror. And the reason for that is because we're applying on this update position, we are, we're not applying it correctly. We're not taking into consideration that the solver is going to be running through per frame and not per second. So even though the speed is per second, the solver is going to be applied per frame. So we need to take that into account and it's pretty easy to do. All we need to do is multiply our velocity by the time increment, which is also a global variable that we have inside Houdini. And it's written like this. The order of operations here is also is going to be first, you have the multiplication happening and then you will have the addition happening. Okay. Now this time increment will be updated according to your frames per second. And it'll know that in this case, it's going to be one by 24. Okay. And it's, that's, we're going to be applying a 24th of the velocity on each frame, meaning that right now, if we go up. So now the particles will only reach the height of two at frame 24. Let me go space mark three. And that's what we should have. Okay. We start at zero, sorry. We start at zero and then they go up and at frame 24, they're at this height. At frame 48, they'll be at that height. Okay. Now it's correct. This is one of the common operations that the pop solve will do. Let me just turn on here at the real time. And this is the speed of our particles.

**Frame:** tutorials\frames\51-introducing-the-sop-solver-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Manually building a position-integration solver from scratch with the SOP Solver node, to understand what particle/POP solvers do under the hood: feeding each frame's previous-frame geometry back into a wrangle that updates position by velocity × the per-frame time increment.

### Summary
Before touching POPs, builds the same per-frame position update manually to demystify what a solver actually does. Scatters 100 points on a grid, gives them a constant velocity attribute `v` (vector, meters/second — Houdini's native unit), and writes a Point Wrangle (`@P = @P + @v;`) that nudges position once. Demonstrates that running this wrangle once doesn't animate anything over time — it has to be re-applied every frame. Wraps the same wrangle inside a **SOP Solver** node, which automatically feeds back the previous frame's result as input on each subsequent frame, producing real per-frame animation when scrubbing the timeline. Then catches and fixes the classic frame-rate bug: velocity is defined in meters/second, but the solver runs per-frame, not per-second — so naively adding `@v` each frame moves the particles 24× too fast at 24fps. Fix: multiply velocity by Houdini's built-in `$TimeInc` (1/fps) before adding, so the position update is correctly scaled to one frame's worth of motion (`@P = @P + @v * $TimeInc;`).

### Key Steps
1. File → New Project; create a Geometry container, dive in.
2. Grid SOP (1×1) → Scatter SOP (~100 points, relax iterations disabled) → hide the Grid, switch viewport to dark background.
3. Attribute Create: name `v`, type Vector, value (0, 1, 0) — a constant "1 m/s on Y" velocity attribute on every point.
4. Point Wrangle named e.g. "update position": `@P = @P + @v;` — confirms a one-shot position nudge, but scrubbing the timeline does nothing further since it's not re-applied per frame.
5. Add a **SOP Solver** node; copy the wrangle inside it; wire it after the Attribute Create. Inside the solver, the wrangle now reads from "previous frame" input instead of the static first-frame geometry, so each frame's wrangle output feeds the next frame's input.
6. Scrub/play the timeline (e.g. extend playback range to 120 frames) — particles now visibly animate; the timeline turns blue where cached, and a Reset Simulation button appears, confirming it's a real time-dependent simulation.
7. **Bug discovered:** front view (Spacebar 3) shows particles moving 1 unit per FRAME, not per second — wrong, since velocity was defined as meters/SECOND but the solver runs once per frame (24 fps project).
8. **Fix:** multiply `@v` by Houdini's global `$TimeInc` variable (= 1/fps) before adding to position: `@P = @P + @v * $TimeInc;`. Order of operations is multiply-then-add. Result: particles now correctly travel exactly 1 meter by frame 24, 2 meters by frame 48, etc., matching the intended 1 m/s velocity.

### Houdini Nodes / VEX / Settings
Grid, Scatter, Attribute Create (vector attribute `v`), Point Wrangle, **SOP Solver** (feeds previous-frame geometry back as input each frame). VEX: `@P`, `@v`, global `$TimeInc` variable (1/fps, used to convert a per-second velocity into a correct per-frame position delta). Viewport: Spacebar+3 for front view, `d` for background/display options.

### Difficulty
Beginner to Intermediate — foundational for understanding any time-based simulation in Houdini (POPs, DOPs, custom solvers); the `$TimeInc` gotcha is a common early-career bug worth internalizing.

### Houdini Version
Not specified.

### Tags
"sop", "vex", "wrangler", "particles", "simulation", "beginner"

---

## Related Tutorials
- `52-creating-a-simplified-particle-system-v1-1080p.md` — direct continuation, building on this SOP Solver foundation
- `53-recreating-our-solver-with-pops-v1-1080p.md` — recreates this exact solver using native POPs, a natural next step
