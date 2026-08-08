---
title: Houdini COPs Datamoshing HDA
source: YouTube
url: https://www.youtube.com/watch?v=G77PFMXnUMU
author: vanity_ibex
ingested: 2026-08-08
houdini_version: "20.5+ (Copernicus context)"
tags: [copernicus, cops, datamoshing, pixel-mosh, pixel-advect, pixel-pusher, optical-flow, block-matching, motion-vectors, glitch-effect, feedback-loop, compositing]
extraction_status: complete
frames_dir: tutorials/frames/houdini-cops-datamoshing-hda/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini COPs Datamoshing HDA

**Source:** [YouTube](https://www.youtube.com/watch?v=G77PFMXnUMU)
**Author:** vanity_ibex
**Duration:** 12m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Itu dat afternoon, and we certainly like the sound quality of these two but sadly we haven't
[0:27] This is a quick overview of the data mashing nodes.
[0:30] We're going to take a look at how they work and how to control them and what they can do.
[0:38] We're just going to start off here with the pixel-mush node.
[0:43] You typically just have to plug in a video after just prepared this little compilation
[0:50] of some clips from pexels.com and just cut them together.
[0:57] You just pep them in and hit play and you will see some data mashing effects.
[1:04] The way this works, you plug in video and you can choose between two motion extraction algorithms.
[1:13] You've got optical flow and then you also have block matching.
[1:21] Both of these nodes will be included in the Gumroad page on the files.
[1:30] Both of these algorithms try to extract motion from video.
[1:36] They generate these motion vectors which basically tell you how the pixels are moving through space.
[1:47] What we then do is basically take the color data.
[1:54] For example, let's look at the umbrellas here.
[1:57] We take the color data and we basically just move it along the motion extraction algorithms.
[2:08] That causes these smears.
[2:12] What this node does is basically automatically creates masks and the motion data.
[2:20] Then it advects the color data along these motion paths and causes the data-mushing artifacts.
[2:31] Let's take a look at the difference threshold for example.
[2:36] You have the slider here and it will measure how big the difference between the pixels is and the lower you go, the more responsive it is.
[2:49] You can set it to movement which works exactly the same.
[2:53] Measure how big the movement of the current pixel is and create a mask from that.
[3:05] Standard settings, difference and movement combined.
[3:08] Then you have these block size settings right here.
[3:12] What I do is I pixelize the mask and there are two passes and they get merged.
[3:22] You can basically set the size of the pixels here.
[3:27] If you don't want that, you can just turn them down and then you get pixel-sized blocks.
[3:34] The standard data-mushing algorithm basically has bigger blocks and that's why standard is a little bit bigger here.
[3:45] What you can also do is smooth the mask before it gets pixelized.
[3:53] This basically smooths out the data and gives you a little more, just a little bigger areas and it gets rid of high detail noise, which can be quite nice.
[4:10] Those are the mask shape settings and then you have mask settings for blending.
[4:17] The temporal blend is basically how much of the mask is from the previous frame.
[4:24] If you set it to low value, you see the mask lasts a long time and it takes a lot of the previous frames and adds them up.
[4:35] If it's a high value, it's basically only the current frame.
[4:40] Usually 0.5 is quite good.
[4:43] You also have the fade speed of the last frame.
[4:48] It's basically how fast the previous frame fades away.
[4:53] You can set this last button at least.
[4:58] We've got the color shift done here.
[5:01] The typical data-mush algorithm basically measures color difference.
[5:06] Let's say we've got this head pixel right here, this one, and it gets displaced over here.
[5:15] It will measure the color shift.
[5:19] It needs to go from this red to this green.
[5:22] Every advected pixel is basically calculating this color shift and then it's supplying it.
[5:29] That way the colors get distorted.
[5:35] Up here you also have the soft blend setting.
[5:39] The typical behavior with the mask is if it's above 0.5, the values get moved, the color gets advected, and if it's below it stays still.
[5:50] So it's a hard cutoff.
[5:52] But if we turn that on, it will basically smoothly blend based on 0.1.
[5:59] 1 is moshed footage, 0 is the original frame.
[6:03] Instead of having this hard cutoff, you blend between the footage smoothly, which can be quite cool.
[6:11] You basically have this mask here to dial in the effect.
[6:18] Maybe a bit too much color shift.
[6:21] But yeah, you can do some cool stuff with this.
[6:23] Speaking of masks, you also have the option to plug in a custom mask, black and white, which will just constrain the mosh to this area.
[6:33] And this also works with the soft blend.
[6:36] You also have the option to plug in a custom motion vector.
[6:42] For this example right here, I just calculated something using the slop direction.
[6:48] So we're basically converting the footage to mono.
[6:52] Scaling it down a little bit, plugging it into the time of a fractal noise, which will make some of the motion data into the noise, which I quite like to do.
[7:06] Then we put that into a slop direction, which you can see here.
[7:10] There's some sum of a footage comes through.
[7:14] And we basically take that and we pixelate it.
[7:20] And we plug that motion into our mosh.
[7:24] Let that big.
[7:26] And then you have like, yeah, here basically custom motion vectors.
[7:32] You can plug anything in there.
[7:33] You can also use the object flow and the block matching and calculate them out of the node and plug them in.
[7:41] You can use custom motion vectors you've rendered out.
[7:47] So yeah, basically put any motion in there.
[7:52] And let's take a quick look at the outputs.
[7:55] First one is basically our video.
[7:57] Then we have the mask and we have the affected motion.
[8:02] So this is the mix of all the motion that's displacing the video.
[8:09] So yeah, this is basically the pixel moshing node.
[8:13] And while developing and playing around with this, I noticed that you could have a lot more control if you split it into its individual components.
[8:24] This is basically like my best try at making an automatic mosh version that just takes any footage and tries to do something cool with it.
[8:37] So what I've also done is I've split the core components up into their own nodes.
[8:42] So we've got the two motion detection algorithms.
[8:47] But we also have this pixel-advect node, which is basically the core of the advection process.
[8:54] And I've also put that into the files.
[8:57] And you can play around with that and we'll take a quick look at that.
[9:02] So if we just take a look at the pixel-advection node, you basically have most of the other settings.
[9:09] It's a little simpler.
[9:12] You have the soft mask settings, the motion blend and the motion strength.
[9:17] You can also normalize the motion just like before.
[9:22] What this doesn't include is the automatic mask calculation.
[9:26] So you will have to create masks yourself and blend the footage before or after.
[9:32] This is basically what's happening here, but automatically.
[9:38] So if we take a look here, this is basically all of the mask creation and automatic processing.
[9:45] And this isn't included in here.
[9:47] You would have to do it yourself, but that means you also have a lot more freedom to just do whatever you want.
[9:55] The important thing is you need feedback for this to work.
[10:01] So if we take a look at the block here, we've got video motion mask.
[10:05] All of these get feedback and loops.
[10:10] So this video comes out and goes back in here, but you also need access to the new frames, which come in down here.
[10:17] So it's current video and current motion.
[10:21] And yeah, it's basically labeled right here.
[10:25] Feedback video feedback motion.
[10:27] Just plug them in and then you can start messing around.
[10:31] I've also included a simple node called the pixel pusher, which takes a source and a motion vector.
[10:38] And this basically advocates the pixels along the motion vector, but you don't need to run it in a loop.
[10:47] You basically have the iteration setting up here.
[10:50] I've just calculated some slop directions from a noise here and you can turn up the iterations and it will do some cool stuff.
[11:00] You also have the warp option, which will wrap around.
[11:04] So if a pixel goes out of bounds here, it will come back on the other side.
[11:10] You also have the option to normalize motion and then you can increase the strength.
[11:16] It's called sample distance here.
[11:18] Basically the strength of the effect.
[11:22] You can think of this as a Glitchy-Dissort node.
[11:28] They kind of do the same thing, but since this runs in a loop and it allows you to just push pixels around,
[11:39] it serves a little bit more of a different purpose and I just thought I'd include it because I had some fun playing around with it.
[11:48] All of the nodes will have written out tooltips and also help pages, which I hope will make them a little easier to understand.
[12:01] They are also all open, so if you want to take a look at how they work inside, be my guest.
[12:08] Yeah, I think that's basically it. Thanks for watching.



---

## Captured Frames

- [0:43] tutorials/frames/houdini-cops-datamoshing-hda/frame_000.jpg
- [1:13] tutorials/frames/houdini-cops-datamoshing-hda/frame_001.jpg
- [2:08] tutorials/frames/houdini-cops-datamoshing-hda/frame_002.jpg
- [2:36] tutorials/frames/houdini-cops-datamoshing-hda/frame_003.jpg
- [3:12] tutorials/frames/houdini-cops-datamoshing-hda/frame_004.jpg
- [3:53] tutorials/frames/houdini-cops-datamoshing-hda/frame_005.jpg
- [4:17] tutorials/frames/houdini-cops-datamoshing-hda/frame_006.jpg
- [5:01] tutorials/frames/houdini-cops-datamoshing-hda/frame_007.jpg
- [5:52] tutorials/frames/houdini-cops-datamoshing-hda/frame_008.jpg
- [6:23] tutorials/frames/houdini-cops-datamoshing-hda/frame_009.jpg
- [6:48] tutorials/frames/houdini-cops-datamoshing-hda/frame_010.jpg
- [7:55] tutorials/frames/houdini-cops-datamoshing-hda/frame_011.jpg
- [9:02] tutorials/frames/houdini-cops-datamoshing-hda/frame_012.jpg
- [10:05] tutorials/frames/houdini-cops-datamoshing-hda/frame_013.jpg
- [10:31] tutorials/frames/houdini-cops-datamoshing-hda/frame_014.jpg

---

## Structured Notes

### Core Technique
Overview of a custom **datamoshing** HDA suite built in Houdini's Copernicus (COPs) 2D context: an all-in-one `pixel_mosh` node that extracts motion from video and advects color data along that motion to produce classic glitch/datamosh smearing, plus the individual lower-level building blocks (`pixel_advect`, `pixel_pusher`) split out for more manual control.

### Summary
**`pixel_mosh` (the main automatic node):** plug in a video; it extracts a **motion vector field** using one of two selectable algorithms — **Optical Flow** or **Block Matching** — both estimate how pixels are moving frame-to-frame. It then automatically builds a **mask** from that motion data and **advects** (smears/displaces) the color data along the motion paths, producing the classic datamosh smear artifact. Mask-generation controls: **Difference Threshold** (how large a pixel-to-pixel color difference must be to register — lower values make the mask more responsive/sensitive) and **Movement Threshold** (same idea, but keyed to motion magnitude instead of color difference); the default blends both together. **Block Size** settings pixelize the mask in two passes that get merged, controlling the chunkiness of the moshed regions — turned down, you get pixel-sized blocks instead of larger ones (the algorithm's default/"standard" block size is relatively large). The mask can optionally be **smoothed before pixelization**, which softens/enlarges the affected regions and removes high-frequency noise in the mask shape. **Temporal Blend** controls how much of the *previous* frame's mask carries forward into the current one — a low value keeps a long-lasting, accumulating mask; a high value (closer to only-current-frame) is more responsive; ~0.5 is called a good default. A related **fade speed** parameter controls how quickly that carried-over previous-frame mask decays. **Color Shift**: the core moshing process measures the color difference between a pixel's origin and destination along its motion vector and distorts color accordingly as it advects — this is what actually produces the color-smearing look, distinct from just spatial displacement. **Soft Blend**: by default the mask applies as a **hard cutoff** (values above 0.5 fully advect, below 0.5 stay static); enabling Soft Blend instead smoothly interpolates between the original and fully-moshed footage based on the mask's actual 0-1 value, avoiding the hard on/off edge. A **custom black-and-white mask** can be plugged in to constrain where moshing is allowed to happen (compatible with Soft Blend too). A **custom motion vector** input can replace the built-in optical-flow/block-matching extraction entirely — demonstrated by converting footage to mono, scaling it down, feeding it as the time input to a fractal noise, running that through a **slope-direction** node, and pixelating the result, so the "motion" driving the mosh is actually noise shaped by the footage rather than real extracted motion (used here as a creative/stylistic choice, "I quite like to do"); any rendered-out or independently-computed motion vector field can be plugged in this way. Node outputs: the processed **video**, the generated **mask**, and the **motion** (the merged motion field actually used to displace the footage).

**Split-apart lower-level nodes** (added because the presenter found more creative control was possible by breaking the all-in-one node into pieces): **`pixel_advect`** exposes the *core advection process* on its own — soft-mask settings, motion blend, motion strength, and motion normalization — but does **not** include the automatic mask-generation/masking logic that `pixel_mosh` handles for you; you must build and blend your own mask before/after. Critically, `pixel_advect` **requires a feedback loop** to work: it needs both the previous frame's output (video/motion "feedback" inputs) and the current incoming frame's data ("current video"/"current motion") wired in — the node's inputs are explicitly labeled Feedback Video / Feedback Motion vs. the live incoming stream, and this loop structure is what the automatic `pixel_mosh` node is doing internally, just exposed here for direct control.

**`pixel_pusher`:** a simpler standalone node taking a source image and a motion vector, advecting pixels along that vector — but unlike `pixel_advect`, it does **not** need to run in a feedback loop; instead it has an **Iterations** parameter that repeats the push multiple times in one evaluation. Also has a **Warp** option (pixels that would go out of frame bounds wrap around to the opposite side) and motion normalization + a **Sample Distance** parameter controlling effect strength. Conceptually compared to Houdini/COPs' existing "Glitch/Distort"-style node (similar underlying idea), but framed as serving a different purpose since it's iteration-driven rather than loop-driven, giving a different kind of pixel-pushing control.

The presenter notes all nodes ship with tooltips and Houdini help pages, and are unlocked (viewable/editable internally) for anyone wanting to see how they're built.

### Key Steps
1. Plug a video into `pixel_mosh`; choose a motion-extraction algorithm (**Optical Flow** or **Block Matching**).
2. Tune the automatic mask via **Difference Threshold** / **Movement Threshold** (or a blend of both).
3. Adjust **Block Size** (pixelization chunkiness, two merged passes) and optionally **smooth the mask** before pixelization for softer, cleaner regions.
4. Set **Temporal Blend** (how much previous-frame mask persists — ~0.5 as a starting point) and its fade-speed companion for how the accumulated mask decays.
5. Tune **Color Shift** behavior (color distortion along the advection path) for the amount of color smearing.
6. Toggle **Soft Blend** for a smooth 0-1 mask-driven blend instead of the default hard 0.5 cutoff between original and moshed footage.
7. Optionally plug in a **custom black-and-white mask** to constrain where moshing occurs, and/or a **custom motion vector** (e.g. footage-driven noise via mono conversion → fractal noise time input → slope direction → pixelate) to replace the built-in motion extraction entirely.
8. For finer manual control, drop down to `pixel_advect` directly: build your own mask, wire up a feedback loop (previous-frame video/motion feeding back in alongside the current incoming frame), and tune motion blend/strength/normalization yourself.
9. For a simpler non-looping pixel-push effect, use `pixel_pusher` with a source image + motion vector, controlling repetition via **Iterations**, edge behavior via **Warp**, and strength via **Sample Distance**.

### Houdini Nodes / VEX / Settings
Copernicus (COPs) 2D context. **`pixel_mosh`**: Select Input (Optical Flow / Block Matching motion extraction), Difference Threshold, Movement Threshold, Block Size (two-pass pixelization), mask-smoothing-before-pixelization toggle, Temporal Blend + fade speed, Color Shift / Colorshift Strength, Soft Blend, custom black-and-white mask input, custom motion vector input, outputs: video / mask / motion. **`pixel_advect`**: soft mask settings, Motion Blend, Motion Strength, Normalize Motion, Feedback Video / Feedback Motion inputs (requires an explicit feedback loop), current-video/current-motion inputs. **`pixel_pusher`**: source + motion vector inputs, Iterations, Warp (edge wrap-around), Normalize Motion, Sample Distance (strength) — conceptually similar to a Glitch/Distort-style node but iteration- rather than loop-driven. Motion-vector construction example: mono conversion → scale down → fractal-noise time input → slope-direction node → pixelate.

### Difficulty
Intermediate — no VEX authoring required to use the HDAs, but understanding motion vectors, mask blending, and (for the split-apart nodes) COPs feedback-loop wiring is needed to get past the automatic default behavior.

### Houdini Version
Not stated on screen; Copernicus (COPs) context places this at Houdini 20.5+. Screenshots show "Houdini Indie Non-Commercial" 21.0.729.

### Tags
copernicus, cops, datamoshing, pixel-mosh, pixel-advect, pixel-pusher, optical-flow, block-matching, motion-vectors, glitch-effect, feedback-loop, compositing

---

## Related Tutorials
- [Houdini COPS Distortion | breakdown & project file](houdini-cops-distortion-breakdown-project-file.md) — shares the Copernicus (COPs) 2D context and UV/motion-driven pixel-displacement technique, applied there to product-render distortion rather than video datamoshing.
