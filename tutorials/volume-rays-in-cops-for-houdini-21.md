---
title: Volume rays in Cops for Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=nCS6sy53_aw
author: cgside
ingested: 2026-07-13
houdini_version: "21.0.622"
tags: [cops, hda, god-rays, luma-key, compositing, matrix-color-transform, tool-development, houdini-21]
extraction_status: complete
frames_dir: tutorials/frames/volume-rays-in-cops-for-houdini-21/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Volume rays in Cops for Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=nCS6sy53_aw)
**Author:** cgside
**Duration:** 6m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video I wanted to share a new tool that I've been working on called Volume
[0:06] Race.
[0:07] That basically selects the brightest areas of the image and creates these ray effect.
[0:11] You can interrupt in the viewport with a tool or you can manually place it by adjusting
[0:18] the center of set and you can easily animate this of feed.
[0:23] Let's frame between 1 and 45, between 0.3 and 0.06 and 0.3.
[0:34] Let's see, that works.
[0:37] So as you can see it will animate.
[0:38] Of course you can do a key framing because you have the easing options and it will look
[0:43] a bit better.
[0:44] But there's the option.
[0:46] There's also this option to do flickering that will add a noise to the source.
[0:51] And here I'm just ticking effect only if I want to multiply a noise or anything with
[0:57] the effect.
[0:59] And you can also animate in the offset of the noise.
[1:02] So at time multiply by 0.3, let's see.
[1:09] As you can see it will animate the flickering and it will create some nice effects.
[1:13] But again you can play with it.
[1:15] You have the viewport interaction.
[1:17] And you select the luminance range which is doing like a lumaki so we select the brightest
[1:22] areas of the image.
[1:23] You can also re-sample the image.
[1:25] So let's say by default is 0.3 but it will blur a bit the input so you can increase the
[1:30] resolution.
[1:31] Let's say 2.5.
[1:33] You have the iterations which internally this is just repeating the pixels along a direction.
[1:38] So you can increase more if you want but you also have the step scale which is a multiplier
[1:43] of that repetition.
[1:45] But again you start to see some art effects so it's better to decrease it.
[1:51] And you also have a decay that is just like a fading effect as you can see.
[1:58] Then you can have this option just to have the default volume raise and let me increase
[2:04] this.
[2:06] And you can add in here some flickering.
[2:09] And of course you will need to blend it a bit more.
[2:12] So what else?
[2:13] We have some contrast for the flickering.
[2:15] You can play with the noise element scale so you have bigger rays or smaller ones.
[2:21] Again the offset of the noise X and Y.
[2:23] Some contrast then you have some post effects like some blurring, the glow threshold where
[2:29] it starts, the glow brightness and of course the blending.
[2:32] And if you take effect only you don't have that blending option because you will need
[2:36] to manually blend it.
[2:39] So this tool is pretty fast even with animation.
[2:41] It's really a simple effect but it can add a lot of detail to your final renders.
[2:47] So this will work fine on slap comps and whatnot for doing basic compositing.
[2:52] Since now the need doesn't shift necessarily with these effects I thought that I would
[2:58] recreate it and share it for this month's Patreon.
[3:02] So this tool will be available for all the top tier Patreon supporters as part of the
[3:07] subscription.
[3:09] So basically sometimes I share a tutorial, other months I share a tool, this month I will
[3:13] share this tool for free with the Patreon supporters.
[3:16] And but if you are not part of Patreon you can still get it on my Patreon shop.
[3:21] Of course for patrons it will be cheaper.
[3:24] So yeah that's basically it's you can play with the settings and you have also the option
[3:30] to have different signatures.
[3:33] You can have RGB, mono or RGB.
[3:36] You can pick it depends on the input you feed it.
[3:39] It will automatically recognize.
[3:41] So I think I explain all the settings and yeah you can play with it and I hope you enjoy
[3:47] this tool and let me just give you a small update on another tool.
[3:53] So regarding the matrix color transform HDA I just added the UIscale multiplier that
[3:59] you can basically resize the handles.
[4:01] That's an ND feature.
[4:03] If you are zooming in or you have a smaller area to sample and as always you can sample
[4:12] the defined area and play with resolution of the image.
[4:16] But yeah basically if you zoom in a lot you can decrease this and have the desired handle
[4:22] size.
[4:23] Also I added a bit the code of the HDA basically before that I was starting with the shape.
[4:31] Then creating a bounce, creating a matrix as I shared and a different matrix and then
[4:36] apply that to the points that I'm creating by dividing the mesh into 24 sections and
[4:42] extracting the centroid and deforming.
[4:44] But I found a cheaper solution which basically involves again the same add and then do a
[4:50] bounce, sort the points, do some basic UVs from the bounding box and do the same on these
[4:55] sides.
[4:56] And then just generate a grid of points in this case I just generated them at the center
[5:01] and do an XYZ distance from that target position and then I can just attribute interpolate
[5:07] with the X-prem and the X-UV and you can basically play with it and it will have the exact
[5:13] same effect but much cheaper and less work because I was creating transform matrix and
[5:20] applying a different matrix which was just so much.
[5:24] In the years just simple we create a grid of points in this case six columns and four
[5:28] rows, create the column and row ID fitting to the scale of the input mesh.
[5:35] So I'm doing this by numbers 24 and I just create the point at the center because it will
[5:40] be cheaper, it will be a cheaper operation then I can just attribute interpolate and it
[5:44] will interpolate the position, the UVs and whatnot.
[5:47] So that's basically what I'm doing inside this matrix color transform so as you can see
[5:54] and just loading the colors and whatnot.
[5:57] It should be faster and it was already fast but this way it's even a bit faster.
[6:04] So yeah guys I hope you enjoyed the applet and grab the files on Patreon as always thank
[6:10] you so much for all the Patreon supporters and I hope you found this video helpful.
[6:14] I'll see you next time thank you.



---

## Captured Frames

- [0:30] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_000.jpg
- [1:10] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_001.jpg
- [1:40] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_002.jpg
- [2:10] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_003.jpg
- [2:50] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_004.jpg
- [3:30] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_005.jpg
- [4:10] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_006.jpg
- [4:40] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_007.jpg
- [5:20] tutorials/frames/volume-rays-in-cops-for-houdini-21/frame_008.jpg

---

## Structured Notes

### Core Technique
Demo of a custom Cops HDA, "Volume Rays," that isolates an image's brightest areas (a luma-key-style threshold) and stretches them into animatable god-ray/light-shaft streaks with flicker, glow, and RGB/mono/multi-channel auto-detection — plus a small efficiency update to a companion "Matrix Color Transform" HDA that replaces a manually-built per-piece transform-matrix pipeline with a cheaper grid-of-points + `xyzdist()` + Attribute Interpolate approach.

### Summary
**Volume Rays** works by first selecting the brightest areas of the source image via a **luminance-range** threshold (a luma-key-style operation), then repeating/streaking those bright pixels along a direction using an internal **iteration** count (how many times the pixels are repeated) combined with a **step scale** multiplier that controls the spacing/distance of each repetition — pushing this too far introduces visible banding/stepping artifacts, so it's best kept moderate. A **decay** parameter fades the streaks off with distance for a natural falloff. The tool supports full **viewport interaction** (drag to set the ray source/center and offset) as well as manual keyframe-based animation (e.g. animating iterations from 1→45 and offset values over a frame range) for evolving light shafts. A **flickering** option adds animatable noise to the source (with an "effect only" toggle to isolate just the flicker contribution for custom blending elsewhere), including animatable noise offset (e.g. driven by `$T * multiplier`), noise element scale (bigger vs. smaller rays), and contrast controls. Post-processing options include re-sampling resolution (default 0.3, blurs the input; increasing it, e.g. to 2.5, sharpens), a glow threshold/brightness pair, and a built-in blend mode (only available when not in "effect only" mode, since effect-only output is meant to be manually composited elsewhere, e.g. in a slap-comp). The tool auto-detects its input signature (RGB, mono, or multi-channel) and adjusts its internal pipeline accordingly. As a secondary quick update, the tutorial revisits the "Matrix Color Transform" HDA (a `.cine`-style color-swatch-based transform tool used for sampling colors from a defined screen area): it previously computed a manual transform matrix per sample (scale, rotate, translate, built from scratch) applied to points generated by dividing a mesh into 24 sections and extracting centroids — a cheaper alternative was found using the exact same base setup (Bounds, sort, basic UVs from bounding box) but instead **generating a grid of points at the center** (6 columns × 4 rows = 24, matching the section count) with column/row IDs fitted to the input mesh's scale, then using **`xyzdist()`** from each grid point to the target position followed by **Attribute Interpolate** (interpolating position, UVs, etc. via the `xyzdist()`-derived X-prim/X-UV coordinates) — functionally identical to the old matrix-based version but noticeably cheaper since it avoids building/applying full per-point transform matrices. A minor UI addition is also mentioned: a **UI-scale multiplier** on the tool's on-screen handles, useful when zoomed in tightly or working with a smaller sampling area, so handle size can be adjusted independent of the geometry's actual scale.

### Key Steps
1. **Volume Rays — luma-key + streak:** select the brightest areas of the source image via a luminance-range threshold, then repeat/stretch those pixels along a direction using an iteration count and a step-scale multiplier (spacing between repetitions — push too far and banding artifacts appear).
2. Apply a **decay** parameter to fade the streaked rays with distance for a natural light-falloff look.
3. Use **viewport click-drag interaction** to set the ray source/center and offset directly, or manually keyframe iteration count and offset values over time for animated light shafts.
4. Enable **flickering** to add animatable noise to the source; use "effect only" to isolate just the flicker contribution for manual blending elsewhere, with controllable noise offset (e.g. `$T` * multiplier), element scale, and contrast.
5. Tune post-processing: re-sample resolution (default 0.3 blurs input; higher values like 2.5 sharpen), glow threshold + brightness, and the built-in blend mode (disabled automatically in "effect only" mode since that output is meant for manual compositing, e.g. a slap comp).
6. Rely on the tool's automatic **input-signature detection** (RGB / mono / multi-channel) to adjust its internal pipeline without manual configuration.
7. **Matrix Color Transform efficiency update:** keep the existing setup (Bounds, sort points, basic bounding-box-derived UVs) but replace the old manual transform-matrix construction with a **generated grid of points** (6×4 = 24, matching the mesh's 24 sections) with column/row IDs fitted to the input mesh's scale.
8. Use **`xyzdist()`** from each grid point to the sampling target, then **Attribute Interpolate** (position, UVs, etc., driven by the `xyzdist()`-derived X-prim/X-UV) instead of building/applying a full per-point transform matrix — functionally equivalent output at lower computational cost.
9. Add a **UI-scale multiplier** for the tool's on-screen interaction handles so their size can be adjusted independently of the geometry scale (useful when zoomed in tightly).

### Houdini Nodes / VEX / Settings
Cops "Volume Rays" HDA: luma-key/luminance-range threshold, iteration-based pixel repeat, step-scale spacing, decay falloff, viewport click-drag interaction (source/offset), keyframe animation support, flicker (animatable noise, "effect only" toggle, noise offset/element-scale/contrast), re-sample resolution, glow threshold/brightness, blend mode, auto RGB/mono/multi-channel signature detection. "Matrix Color Transform" HDA update: Bounds, Sort, bounding-box UVs, Point Generate (grid, 6×4 = 24 points, column/row IDs fitted to mesh scale), `xyzdist()`, Attribute Interpolate (X-prim/X-UV-driven), UI-scale multiplier for interaction handles (contrasted against the prior full transform-matrix scale/rotate/translate construction).

### Difficulty
Intermediate (as a tool demo/showcase — the underlying HDA implementations are more advanced, but this video focuses on using and understanding the tool's parameters rather than building it from scratch).

### Houdini Version
21.0.622 (visible in viewport title bar).

### Tags
cops, hda, god-rays, luma-key, compositing, matrix-color-transform, tool-development, houdini-21

---

## Related Tutorials
- [Quick CGI Integration with Houdini and Solaris](quick-cgi-integration-with-houdini-and-solaris.md) — shares the Cops AOV-driven contact-shadow/compositing approach that a tool like Volume Rays would layer into.
- [Texture Projection Tool for Houdini 20.5](texture-projection-tool-for-houdini-205.md) — another custom Cops-backed HDA tool demo from the same channel.
- [Tips and Tricks for a Better Houdini Time](tips-and-tricks-for-a-better-houdini-time.md) — shares a null-driven camera-rig and Cache-node performance-tip philosophy similar to this update's efficiency focus.
