---
title: Vex quick tips | Overhang look with channel ramps
source: YouTube
url: https://www.youtube.com/watch?v=SHAgvzji9vM
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [vex, quick-tips, channel-ramp, quaternion, curve, overhang, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Vex quick tips | Overhang look with channel ramps

**Source:** [YouTube](https://www.youtube.com/watch?v=SHAgvzji9vM)
**Author:** cgside
**Duration:** 9m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this video I wanted to show you how you can create this overhang using ramps, which
[0:07] is not as straightforward as it might look because by default you can't do the overhangs
[0:13] in channel ramps, but with a few tricks we can get this look.
[0:17] So let's get started.
[0:20] So we will start from scratch.
[0:22] So let's create a Geo container in a new scene and I'm going to start with a line.
[0:28] I don't think I change anything in here and then we can add a resample to get the
[0:32] curve view.
[0:34] So let's do a resample.
[0:35] In this case I'm going to subdivide it quite a bit, so point all to and I'm going to output
[0:42] the curve view.
[0:44] So let's see we have quite a few points because we will need it to displace it properly
[0:48] and we have the curve view, which is available from 0 to 1 along the curve.
[0:54] So now we will first displace it to have the leaf contour.
[0:59] So for that I'm going to create a wrangle and do a simple displace along the normal.
[1:03] So to make this easy we can create the normals along the x.
[1:10] So back to normal it will be 0 to 1 0 0 so along x.
[1:17] And then we can create a ramp to displace it.
[1:19] So I'm going to call it leave ramp and it will be equal to a C-d ramp.
[1:25] I'm going to call it leave and I'm going to use the curve view to displace it.
[1:29] So curve view.
[1:32] And now we can just displace it along the normals.
[1:37] We have done this plenty of times before and we can multiply it by the leaf ramp.
[1:43] And in the end we can have just another multiplier to control the effect.
[1:48] So I'm going to call it leave this.
[1:52] Let's see how that looks.
[1:53] So leave ramp lower case.
[1:57] So let's create this and increase the displacement as you can see is displacing along the x.
[2:02] This case I'm going to set it to 5.5 and I'm going to pick your busier.
[2:09] Because in this case I can just have a value like so I'm going to put this one down and
[2:19] just displace it in here.
[2:22] So something along those lines we'll do.
[2:26] Let me just check.
[2:29] So around 0.7 something.
[2:31] So just to create the leaf look and I'm going to make sure to drag this one to the end.
[2:36] So something like that if we mirror this we will have the leaf shape and you can play
[2:42] with it to have more or less and play with the displacement amount.
[2:46] This case I think I'm going to yeah something like that will do.
[2:50] So now we want to create that over and look.
[2:53] But before that let's create the normals because we will need them.
[2:57] So already on the long curve and in this case we want we don't want the normals along
[3:03] the tangents we actually want them along the x axis.
[3:07] So this we want this normal so we can rotate them and create that over and look.
[3:14] So now let's create another angle and we still have that curve view that we will need
[3:21] to displace along the attributes and we have the normal.
[3:27] Let's see what we will do.
[3:30] So first of all I'm going to create a float variable called you which will be equal to
[3:35] curve view because we will manipulate it and instead of always typing curve view we can
[3:39] just use a variable it will be easier.
[3:43] Then before we create the overang let's just create let's just displace the normals.
[3:53] So let's do v at n it will be multiplied by a Shannon ramp and I'm going to call it
[3:59] this and along you and then I'm going to displace it.
[4:06] So just like we have done before and I'm going to multiply it by a displacement amount.
[4:13] This per mount.
[4:16] Let's see how that looks so we can create a displacement amount and now in the displacement
[4:22] we can do the following we can take the last value we can create here a new value and
[4:28] drag the last value down and we create this overang look.
[4:34] And now we can repeat the curve view so we can just say we can create the repeating pattern
[4:42] just by multiplying the curve view by a Shannon amount so I'm going to call it perhaps
[4:53] if we do that and let's say 20 and then we need to modular so we can repeat so on the
[5:02] low by 1.0 so we can wrap around.
[5:05] So as you can see it's creating the effect and we can control the displacement amount but
[5:09] as you can see it's not really creating the overang look because to do that we actually
[5:14] need to rotate the normals.
[5:16] So let's do that.
[5:17] Let's create first an angle so a variable called angle and it will be a Shannon ramp.
[5:25] Let's call it angle ramp and it will be along we'll manipulate the U value.
[5:36] Then we want to rotate so far that I'm going to create a quaternion so vector 4 but it
[5:42] will be equal to a quaternion and we will rotate by the angle amount and along in this
[5:48] case along the z axis so set 0 0 1.
[5:55] And let's see all that loops and next we need to actually rotate the normals so we will
[6:02] say v at n it will be equal to q rotate q rotate and we will rotate the quaternion along
[6:12] the normals.
[6:15] So let's see how that looks and if we create the values as you can see it's already
[6:20] creating that look so in this case we want to play with this ramp and as you can see
[6:26] it's creating that look but I still want to tweak it so for that I'm going to create
[6:36] another ramp I believe.
[6:39] We need to create here another ramp for the angle so we can manipulate it along the U
[6:44] attribute.
[6:45] So let's do angle times equals C-A-d ramp and we will say angle, note along the in this
[6:56] case along the curve view not the U because the U is already being repeated.
[7:03] So now if we adjust properly the ramps so the displacement is fine and in the angle ramp
[7:12] we can manipulate it a bit so let's do something like this and for the angle multiplier we
[7:20] can start I and reduce it a bit in here and as you can see it's creating that over-angle
[7:27] look and if we change the displacement about we have something like this.
[7:33] And to finish it off we can actually use a power function in here to create a more smooth
[7:41] look along the U. So if we do U equals to power function of U and let's create a channel
[7:50] float called U power and let's actually create that and let's set it to 1.5 so 1.5.
[8:03] As you can see we can manipulate in here where it starts the follow-up effect let's say.
[8:11] So in this case I set it to 1.5 and you can always manipulate here how it ends in this case
[8:18] I'm gonna set it like this so I can repeat it easily so I can mirror it and it has this look.
[8:25] So that's basically it. I hope you got something out of this it was something I wanted to do for a
[8:33] while but I didn't know how to so now you can you welcome know how to do it and hopefully it will
[8:40] be helpful in your future projects and we can manipulate here the ramp and create in here let's say
[8:48] B spline and we can create another different look and you can always increase in here
[9:00] and create this more rounded look let's say. So you can play with it and yeah that was basically
[9:08] it you can also change the repetitions if you want less let's say 15 and you have this over and
[9:15] look thank you for watching if you want you can grab the file on my patreon alongside with
[9:20] our words of exclusive tutorials and also some some courses that you can find in there. See you
[9:26] next time thank you.



---

## Captured Frames

- [0:55] tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/frame_000.jpg
- [1:40] tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/frame_001.jpg
- [2:27] tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/frame_002.jpg
- [3:47] tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/frame_003.jpg
- [6:00] tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/frame_004.jpg
- [7:22] tutorials/frames/vex-quick-tips-overhang-look-with-channel-ramps/frame_005.jpg

---

## Structured Notes

### Core Technique
Fake an "overhang" curve profile (a leaf-like shape whose displacement doubles back on itself, impossible with a straight displace-along-normal) by rotating each point's normal with a per-point quaternion before displacing along it — channel ramps alone can't produce overhangs because they're single-valued functions, so the rotation trick works around that limitation.

### Summary
Starting from a Line, Resample heavily (0.02) with curve-view output, the curve is first displaced along its X-axis normals using a channel ramp sampled by curve view (`leafRamp`) multiplied by a displacement-amount slider to build a simple leaf-shaped silhouette (mirrorable for a full leaf). To get the overhang look, a second wrangle recomputes normals along the tangent's perpendicular (X axis) instead of along the curve tangent, then builds a `u` variable from curve view that first displaces the normals themselves via a channel ramp (multiplied by a displacement multiplier) before the position is displaced — displacing the normal, not just the position, is what allows the curve to double back on itself. To create a repeating pattern, curve view is multiplied by a "reps" channel float and wrapped with `%1.0`. The actual overhang shape comes from rotating the normals with a quaternion: an `angle` variable is built from a second channel ramp (`angleRamp`) sampled along the *original* (non-repeated) curve view, converted to a quaternion via `quaternion(angle, {0,0,1})`, and applied to the normal with `qrotate()` — this rotation is what lets the displacement fold back over itself into a true overhang. A final `pow(u, upow)` remap on U (channel float `uPower`, e.g. 1.5) smooths where the overhang effect starts along the curve, and the whole shape can be mirrored and repeated (e.g. 15–20 reps) with a B-spline ramp basis for a more rounded variant.

### Key Steps
1. Build a Line, Resample finely (~0.02) with curve-view output for later ramp sampling.
2. Compute normals along X (not the tangent) via a wrangle so the leaf can be displaced sideways.
3. Displace along the normal using a channel ramp (`leafRamp`) sampled by curve view, multiplied by a displacement-amount slider, to create the base leaf-contour silhouette (mirror for the full leaf shape).
4. In a second wrangle, recompute normals along the curve's perpendicular X axis (needed for the overhang rotation step), and build a `u` float copy of curve view to manipulate independently.
5. Displace the *normal* itself (not yet the position) using a channel ramp sampled along `u`, multiplied by a displacement-amount slider — this pre-bends the normal before the final displacement.
6. Multiply `u` by a "reps" channel float and wrap with `mod(u, 1.0)` to create a repeating pattern along the curve.
7. Build an `angle` variable from a second channel ramp (`angleRamp`) sampled along the *original*, non-repeated curve view (important — repeating would break the rotation continuity).
8. Convert `angle` to a quaternion via `quaternion(angle, {0,0,1})` and rotate the normal with `qrotate()` — this is the key step that produces the actual overhang, since a straight displacement can never fold back on itself.
9. Displace the position along the now-rotated normal, multiplied by the displacement amount — the overhang look appears once the angle ramp is tuned.
10. Remap `u` through `pow(u, upower)` (channel float, e.g. 1.5) to control where along the curve the overhang effect starts and how it tapers.
11. Mirror the curve and adjust repetitions (e.g. 15–20) and ramp basis (Linear vs. B-Spline) for variations — more reps/B-spline gives a smoother, more rounded repeating overhang pattern.

### Houdini Nodes / VEX / Settings
Line, Resample (fine, curve-view output), point wrangle ×2 (normal computation along X, leaf-contour displacement via channel ramp; second wrangle for normal pre-displacement + rotation), `chramp()` channel ramps (leafRamp, displacement-amount channel ramp, angleRamp), `chf` sliders (displacement amount, reps, uPower), `quaternion(angle, axis)`, `qrotate()`, `pow()`, `mod()` / `%1.0` wraparound.

### Difficulty
Intermediate (the quaternion-based normal-rotation trick to defeat the single-valued-ramp limitation is a non-obvious VEX technique, but the rest of the setup is straightforward point-wrangle displacement).

### Houdini Version
Not specified.

### Tags
vex, quick-tips, channel-ramp, quaternion, curve, overhang, procedural-modeling

---

## Related Tutorials
- [Vex Quick Tips #2 | Iterating over numbers](vex-quick-tips-2-iterating-over-numbers.md) — same "Vex Quick Tips" series, focused on for-each-over-numbers patterns instead of curve/ramp displacement.
- [Vex Quick Tips #4 - Pineapple Crown](vex-quick-tips-4---pineapple-crown.md) — same series, uses a related curve-parameter + quaternion-rotation approach for leaf/crown orientation.
- [Useful Vex Snippets - Houdini Tips and Tricks](useful-vex-snippets-houdini-tips-and-tricks.md) — shares small hand-written VEX utility patterns in the same quick-tips spirit.
