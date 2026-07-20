---
title: Quick CG integration with Houdini and Karma
source: YouTube
url: https://www.youtube.com/watch?v=kxg05cfgdQI
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [camera-matching, depth-map, onnx, machine-learning, cops, solaris, karma-xpu, cgi-integration, texture-projection]
extraction_status: complete
frames_dir: tutorials/frames/quick-cg-integration-with-houdini-and-karma/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Quick CG integration with Houdini and Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=kxg05cfgdQI)
**Author:** cgside
**Duration:** 28m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in today's video we will do some quick CGI integration
[0:05] into back plates in Odinni. So this should be a fun one. We will go from camera
[0:11] matching to generating depth maps with Onyx and also do the final render that
[0:17] should look something like this where we integrate our bottle with the depth
[0:26] map that we generated. So let's get into it. So the first step would be to
[0:31] download the back plates in an HDRI. In this case I am using this HDRI from
[0:38] Polyaven and if you go into the back plates you will find this specific one
[0:44] but you can choose another one and play with it. So one thing that we need to do
[0:48] is to download all besides one of these J-Pads that will like us our back
[0:54] plates. We also need the original raw so we can extract the exit data. So we
[1:02] know Dini I'm gonna create a camera and look through it and I'm going to select
[1:10] in here the background image. I believe I have it in here which is this one
[1:15] and I also need to scale it so I need to put the right ratio so I'm going to
[1:22] properties and in here I will have this so 5568, 5568, oops not this one,
[1:33] 68 by 3712. So I need to put 3712. I need to have the correct ratio as you can
[1:42] see. So now is a matter of aligning the grid to the image that shouldn't be too
[1:49] difficult but first of all I'm going to create an object that can represent
[1:57] some part of the environment so I can match it better. So for that I'm going
[2:03] to create a geometry container and use a box and I know that the size of two.
[2:10] You can as if you have measurements is better but if you don't you can assume
[2:15] some dimensions. I'm gonna set this to one and this is about 0.8. So the
[2:21] height and this should be rotated like this towards this axis and let's see
[2:29] I'm going to make sure so I'm gonna make sure this is sitting flat on the
[2:36] ground so I'm gonna copy this and paste it in here and divide it by two. So now
[2:43] is sitting on the ground going back to the camera and now I'm gonna try to align
[2:48] this. Also it's important when you're aligning that you assume some some height
[2:58] of the camera so if I go in here into the transform you can see now I'm at
[3:02] two meters point seven which is not very realistic so usually you want to
[3:07] take like the human height as a reference so I'm gonna try to replicate that
[3:14] so that's fine but as you can see it's not the lining perfectly the vanishing
[3:19] points are not working so well and that's because we don't have a correct
[3:25] focal length or we have a similar one but we can be more precise so if we
[3:30] come in here in this case I don't want this one original Rob so I'm going to
[3:39] properties and into the details I can see here that this was shot on an Econ
[3:44] 7500 and also a focal length of 32 and I happen to know this camera upon
[3:51] research that has a crop factor of 1.5 so if I come in here and set this to 32
[3:58] times 1.5 we will have a focal length of about 48 so it was pretty close already
[4:04] but just in case so let me check something in here I'm going to the transform
[4:12] and make sure I align this properly so I'm gonna press W and something like
[4:22] this should work I'm gonna keep an eye on this so probably scale it a bit more
[4:29] and the dimensions are not correct of this box so I just did an assumption so I
[4:35] guess this will be fine maybe scale it a bit more and I guess this will be fine of
[4:47] course we can come in here into the box let's lock this and we can start
[4:54] too many abilities a bit more to adjust it properly and now I can see the back
[5:02] I can see it's here so it's more or less okay I'm not going to worry too much
[5:07] this is fine so here is our camera and our reference object that we will use
[5:13] to align everything so that's our first part done now we will create that map
[5:21] so for the map we will generate it using machine learning and this is a model I
[5:27] saw on an antagonist video that seems to work okay so I just need to come in
[5:32] in here to 1000 versions on X and unload one of these I believe I will use a large one
[5:39] not this one or I'm gonna use this one I believe or is the large one so
[5:46] it is wind so I'm gonna use this one in here which is about 800 megabytes you
[5:52] just need to download in here so we have our box now we will create a cup net and
[6:00] do a file and import our backplate so let's see if I have anything here I
[6:06] believe I do so yeah and now we will use Onyx and we need to pass this as an RGB
[6:17] and I'm gonna load the module so in here I'm going to my folder in here and
[6:30] I'm gonna load I believe is this one that I used 800 megabytes yeah it is the
[6:37] largest one and I'm gonna set up shapes from model this will take just a second
[6:41] now it's fine and if I enable it it will error out because the resolution is
[6:46] way different as you can see this will output the 384 image so I'm going in here
[6:53] and make sure in the resemble I'm outputting at 384 so now it should be
[7:01] working but you're getting this 128 in height which I didn't understand at
[7:08] first but we need to equalize this just a mixture now we have to that but as you
[7:15] can see we have it like over each other so this will output three tiles in this
[7:22] case so 100 if you're coming here into the output you can change this if you
[7:29] change this this will error out so this will output three tiles along the way of
[7:33] 128 I believe that's for optimization I'm not sure but this is my first time
[7:40] playing with this and if now I if I do a channel split and look in here you can
[7:46] see this is the front of our desk then in the green channel we have the middle
[7:51] ground and on the blue we have the background so we need to combine this
[7:55] somehow there might be some better ways but the one I found that worked well was
[8:02] using the contact sheet and you can load the red the green and the blue let's
[8:08] look at that so here we have but now we need to do this too how did I do this so
[8:14] like this this bottom to top and don't step so now we have our output as you can
[8:21] so we go from this to this so now let's create a node and I'm gonna go it out that
[8:34] and just for reference I'm also going to create in here the backplate version I'm just
[8:42] going to resemble this to be 384 so I'm gonna change this to parameter and
[8:49] 384 384 and I also need to refram the destination so I'm gonna create a node
[9:00] and this will be our color so now I've been the depth map and our also a coloring here we can
[9:12] generate the geometry so let's create the grid I believe I made these like one by one
[9:20] and the contributions will be fine but I'm going to make it along the Z axis also going to
[9:26] create UVs because we will need them and reverse the normals just for good measure
[9:34] so let's check our UVs we need to make these along the Z axis of course and they are looking
[9:42] aligned so let's find this is our box and reference that in a bit and now we will need to subdivide
[9:51] this because right now we won't have enough geometry to display the plane into the depth map
[9:57] so I'm gonna subdivide and I believe I used like all the regions or something yeah and then I'm
[10:04] gonna load in the depth maps which are good for my map and I'm going in here and copy these
[10:10] output to draw C and in here I don't want to use CD I want to use a float and call it X and I'm
[10:22] gonna load it in here with the OP syntax there we have it we don't need to visualize it so I'm
[10:30] just going to see that there we have it now we can also use in here the CD and loading the
[10:44] let's see if it's color yeah and we can load the color just for visualization and now we need to
[10:53] align this plane to the camera so for that let's see our camera right now the plane is in here and we
[11:01] need to place it in the camera first on let's say so for that we'll use some facts first we need
[11:10] to load our camera so for that I'm gonna create a string cam see you just and I'm gonna call it
[11:17] that to cam oops that cam gonna enter in here and I need to edit primary during their phase and
[11:29] where is that so bad to cam and I'm gonna change it to operator path operator path and
[11:38] big cameras only that's fine now I can come in here and just select the camera and then we will do
[11:46] v at p it will be well from ndc and we will load our camera and our position let's look at that so
[11:58] right now it's place it in placing it in the in the camera path but we actually need to offset
[12:06] this so I'm gonna use in here stat at p dot x plus zero point let's just let p dot x and v at p dot y
[12:19] and zero point zero so in this case we need to offset this by 0.5 and no this is correct we just
[12:35] need to offset along the z so at p dot z minus equals and I'm gonna create in here align z
[12:50] and I skip existing and I'm going to do this so at p dot z and I have to pat to the camera so
[13:03] that is fine so yeah I believe we actually need to offset this in here so let's do plus zero point
[13:18] 5 and do y plus zero point 5, 2, 3 and it's not working I need to set the camera set the p and let's set
[13:33] let's read that instead yeah that is worth sorry about that so we need actually the z component and
[13:40] now we can make our camera and move it along the path along the presser oops didn't mean to do that
[13:48] and if we look at the camera it's aligning properly the plane to the camera so we can scale it up and
[13:55] down and move it along the presser so this case I'm gonna set the value of 2.1 and I'm gonna make
[14:02] sure to visualize this so we see and as you can see it's more or less aligning with our reference
[14:10] object and now where do we put our tapped map so we can come in here and do so the normals in
[14:20] this case of the plane are aligning to the camera so I thought that maybe we can do v at p plus equals
[14:26] along the normals and multiply it by the left and you can see that doesn't work so well because
[14:36] this is misaligned so what we actually need to do so let's just keep this in here and let's duplicate
[14:45] this and instead let's use the z component in here and subtract the inverted depth map on the
[14:57] ndc coordinate so let's do a depth dot depth and as you can see now it's aligning much better so we
[15:06] add this and now we have a more realistic result so as you can see we have our objects of course this
[15:13] map is not perfect this is was automatically generated but it can work in some situations and
[15:21] I'm gonna some disease okay for now oh there we have it now if we look at the camera we have
[15:28] everything more or less aligned as you can see and you can come in here and play with offset
[15:35] so here you can play where you want this to go so in this case I know a well up 2.1 is aligning
[15:42] okay with it maybe a bit less so something like this and the cool thing about this is that we
[15:49] can put some objects in here and interact with the environment so that's always nice and in the
[15:56] next part we will add some object to this and do the render in karma so let's clean this up let's
[16:05] delete this and I forgot to mention in the last part that this was this tip was by swoles so he
[16:14] actually helped me in this configuration to set the depth on the MDC coordinates so thank you
[16:21] for that swoles and let's move on so now I'm gonna create in here no and create an out
[16:31] roxy geo and now I'm gonna import your object so I'm just gonna space it in here which is this
[16:41] bottle we use for our texture projection tutorial and I'm going to do in this case a projection on
[16:52] this so I'm gonna use my texture projection tool that you can get on my patreon alongside with this
[16:57] model so I'm gonna load in here so let me just project in here an image I'm gonna load the
[17:06] oldini logo that I have somewhere in here so instead of the default one I'm gonna rotate it
[17:13] holding control and scale it a bit and I also need to play in here with the max distance
[17:21] so it's fine it's fine I'm also going to change this to 2k and just gonna create an out here
[17:32] and that's fine so now I also need to scale this because right now not properly scaled so I'm
[17:41] gonna create a match size and scale it to about 0.3 so about 30 centimeters along the y so I'm
[17:51] gonna scale to fit change this to mean and scale it to 0.3 so this now is about 0.3 in y so
[18:01] 30 centimeters which is fine and I believe that our old jingles written now and now we can do a
[18:12] simple transform like sit on the geometry so I'm gonna load this and in this transform I'm gonna
[18:23] play sit in here by pressing all this is my shortcut I believe the default one is semi-con to
[18:31] to snap objects to other objects so as you can see it's a bit misaligned so I'm gonna sheet and
[18:38] place in here 0.0 so that's fine now we just need to make sure we transform this we rotate this
[18:49] properly so in this case I used a value of 180 ohm blue I so I can see the logo later
[18:58] so this will be fine we can also play with a position along the y but that will be a line so I'm
[19:04] gonna create a name in here this is already named so that's fine I'm gonna create one or this part
[19:14] and I'm gonna go with proxy geo see geo let's merge this to and create that now each I'm going to go
[19:26] out this is where we'll be moving these into solaris so I'm gonna create in here just to make sure I
[19:34] have these in transparent I copy this part so I can import it into shading so I'm gonna create a
[19:43] lubnet not a lot on that one I'm gonna change these to solaris but moving to the object and
[19:54] lubnet so import all these geo so geo let me see in here and I'm going to import the out so now I'm
[20:13] making sure to change this and also import the cameras so see import cameras this should import our
[20:22] camera let's look through that that is fine now we need to let's see if we remove the
[20:35] wireframe and we look through the solid view or to the if we disable this and just look through
[20:43] the camera we will have this background image so I'm gonna instead do camera camera edit to remove
[20:50] the background I believe this should work so let's see going to view and background image set
[20:59] or create and make sure I edit this camera so that's fine that removed background if we do
[21:08] do nothing this will load it back and what else we will do we will create a material library
[21:15] make sure we enable this geometry we will create the online which is where we will load our
[21:25] HDR right of this environment and we also do other reference settings and allow this as
[21:32] XPU and of course we will use the background plates to integrate into to integrate the
[21:40] back plate in here and we will load as a plate our image and as geometry we will use the proxy
[21:50] so that's fine and for the HDR right I'm just gonna load it I have everything here
[22:02] so let's see set this to let long and load it I'm gonna make sure I render only the viewport
[22:10] side and changes to dark changes to light it's fine now we need to align this HDR right
[22:18] with our environment as you can see it's not properly aligned this will never be perfect
[22:24] so I need to change this in here so for that I'm gonna rotate this by about let's say 20 30 let's see
[22:38] and that should be better I'm looking in here that should be better so let's the let's create a material maybe
[22:50] so let's create a material I'm gonna name this to portal so portal name and
[23:02] just gonna set it to gray for now and do
[23:10] or office let's assign this to all of these for now
[23:19] and let's do a simple render so I'll just sure I don't display this
[23:26] and
[23:27] and
[23:29] why is this not aligned
[23:36] you might oh I need to change the in here the camera render settings I need to change this to
[23:40] camera one yeah now that's work so I'm gonna create a smaller spacing here and let's do a simple render
[23:49] and of course we need to change something in here so the background plate I have the
[23:59] ProxyGU I have the plate but I also need to change something in here so in the camera effects I'm
[24:07] gonna disable left of field and motion blur and now is not loading the oh I need I know why it's
[24:15] not loading the shadows the shadow pass because we need to come in here on the image output
[24:22] and import the renderverse and render product so now this should work and as you can see it's working
[24:27] creating the shadow is more or less aligned with this maybe not so maybe we need to change this a bit
[24:42] maybe minus 20 maybe that's fine so let's do off-weated me so that is fine
[24:52] is creating the shadow now just for fun we will create the materials so to finish this we will
[24:58] create just some quick materials for materials for the button I'm gonna create importing here the image
[25:04] but I make sure I have that loaded so near I'm gonna copy this pet and open it and I'm gonna load
[25:15] as an image and make sure I load it as color for and paste this and now we can do a separate color
[25:22] so like we can import the alpha and we use a mix and I'm gonna convert this to RGB only
[25:30] it's not necessary but I just like to do it I'm gonna load this as the foreground
[25:35] these as a mess and as a background I can set this to a gray value and let's load using here
[25:43] and of course is not showing why is that usually oh I need just to set this on the
[25:52] oh it's rotated the other way around so what we can do we can pin this and go in here
[26:05] we can place a transform also in Solaris but I'm just going to rotate this
[26:11] something like this is this fine let's look through the camera yeah maybe it's a bit big
[26:17] but this case I'm gonna rotate it like this so that's fine I'm so used to going to the stage but
[26:23] I wanted to create this in a log net just to be different and our log is a bit big but that's fine
[26:29] so I'm gonna change in here the background color my bottle is orange but we have this orange
[26:35] ear from the bottle so I'm gonna be instead some blue gonna quickly create in here
[26:44] and a gray mat I'm gonna change this to some gray and change this red alert to about 0.5
[26:55] duplicate and call it grown net it's said metalness said the color to bite and he's about
[27:06] 1.3 just on a load materials and send this to the gray mat and this to grown and I'm just
[27:16] gonna increase this to 512 and go in here and change something like some denoiser and let's look
[27:24] for render and yeah the other unit look for his way to be but that's fine so yeah guys this was
[27:32] basically it's I hope you have learned something new from this video you can download this full
[27:39] setup on my patreon alongside with exclusive tutorials I always say the same thing but if you
[27:45] haven't joined my patreon consider supporting me over there because it's what makes me
[27:51] enables me to make these sort of pre videos and I also do exclusive videos on patreon and have
[27:57] some courses in there that are pretty cheap and all the project files from my videos so yeah
[28:03] let me know in the comments what you think and I guess I'll see you next time thank you



---

## Captured Frames

- [1:45] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_000.jpg
- [3:15] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_001.jpg
- [7:00] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_002.jpg
- [10:30] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_003.jpg
- [15:00] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_004.jpg
- [17:40] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_005.jpg
- [21:00] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_006.jpg
- [25:00] tutorials/frames/quick-cg-integration-with-houdini-and-karma/frame_007.jpg

---

## Structured Notes

### Core Technique
Integrate a CG bottle into a real photographed back-plate by camera-matching against EXIF data, generating a machine-learning depth map (Onyx/ONNX in Cops) to displace a camera-facing card for a parallax-correct environment, then compositing the object with Karma XPU in Solaris using an HDRI-aligned dome and depth-displaced ground geometry.

### Summary
The pipeline starts with a real back-plate photo (from Polyhaven) plus its RAW original (used only to read EXIF: camera model, focal length, crop factor) for accurate camera matching — a reference box of assumed real-world dimensions is placed and aligned to vanishing points in the image, using an assumed human-height camera position and a corrected focal length (`nativeFocalLength × cropFactor`) for a much better alignment than guessing. A depth map is then generated with a **machine-learning ONNX model** (loaded in Cops, ~800MB "large" variant) that outputs a tiled 384×128 RGB image (three depth tiles stacked vertically — foreground/red, midground/green, background/blue) requiring a Contact Sheet node to reassemble into one usable depth image, matched in resolution to a Resize-matched copy of the back-plate. A subdivided grid (aligned to the same Z-axis/UV orientation as the back-plate) is displaced using the depth map: first a naive attempt (`P += N * depth`) fails because the plane's normals aren't aligned to the camera; the working approach instead aligns the plane to the camera via `fromNDC()` with the camera path (offsetting X/Y by 0.5 and Z via `alignz()`), then displaces along Z using the depth map sampled at NDC coordinates (inverted) — producing a camera-relative displaced "world card" that roughly matches the photographed geometry's depth, letting inserted 3D objects (like the bottle) receive correct shadows/contact and interact believably with the environment. For the actual asset, the bottle (previously logo-projected using the channel's custom Texture Projection tool) is Match-Sized to real-world scale (0.3m), snapped onto the depth-displaced card with Transform "sit" (Alt shortcut), rotated to face correctly, then brought into Solaris/LOPs alongside the imported camera (background image removed via Camera Edit so the viewport shows the true render) and an HDRI dome light (rotated to align its light direction with the photographed scene's actual lighting), rendered in **Karma XPU**. Materials are built with simple color-correction/mix networks (loaded label image, alpha-composited over a gray or colored background) and basic metalness/roughness values for the bottle cap and other quick props, finished with a small render at increased samples and a denoiser.

### Key Steps
1. Download an HDRI back-plate (with its RAW original for EXIF data) from Polyhaven; create a camera in Houdini, load the back-plate as the background image, and set the correct image aspect ratio from its resolution.
2. Add a reference object of assumed real-world size (a box) to the scene, positioned at an assumed human-eye camera height, and align it to the back-plate's vanishing points for camera matching.
3. Correct the camera's focal length using the RAW's EXIF data: `nativeFocalLength × cropFactor` (e.g. 32mm × 1.5 crop factor ≈ 48mm) for a much closer real-world match than an assumed default.
4. Generate a depth map via a **machine-learning ONNX model** loaded in a Cop network (fed the back-plate as RGB) — output comes as a tiled 384×128 image with 3 stacked depth tiles (foreground/red, midground/green, background/blue channels); reassemble with a **Contact Sheet** node into one coherent depth image.
5. Build a subdivided grid aligned to the back-plate's orientation/UVs, and displace it using the depth map — align the plane to the camera first via `fromNDC()` (camera path, offsetting X/Y by 0.5, aligning Z via `alignz()`) since naive normal-based displacement fails without correct camera-relative orientation; then displace along Z using inverted NDC-sampled depth values.
6. Bring in the previously texture-projected CG asset (the bottle, logo-decaled with the channel's custom Texture Projection tool), Match-Size it to a real-world scale (e.g. 0.3m), and snap it onto the depth-displaced card using Transform "sit" (Alt shortcut) with correct rotation.
7. Move everything into Solaris/LOPs: import the geometry and camera, remove the camera's background image via Camera Edit (so render view shows the actual composited result, not the reference photo).
8. Add a Material Library with a Dome Light loading the environment HDRI (rendered viewport-only, set to XPU), rotate the dome to align its lighting direction with the real photographed lighting.
9. Assign quick materials (gray/metal presets, an alpha-composited label image over a colored background for the bottle) and render in **Karma XPU**, enabling the Render Product/Rendervar imports needed for shadow passes to display correctly; increase samples and add a denoiser for the final render.

### Houdini Nodes / VEX / Settings
Camera (matched focal length via EXIF crop-factor correction), reference Box (real-world scale assumption), Cop network: RGB import, ONNX-based ML depth-model node, Resize (384 output), Contact Sheet (tile reassembly), Grid (subdivided, UV-aligned), VEX wrangle (`fromNDC()`, `alignz()`, camera-relative Z-displacement, inverted NDC depth sampling), Match Size, Transform "sit" snap, Solaris/LOPs: Camera import, Camera Edit (background-image removal), Material Library, Dome Light (HDRI, XPU-only render), Karma XPU, Render Product/Rendervar (for shadow-pass imports), basic Color Correct / Mix / metalness-roughness materials.

### Difficulty
Advanced (combines photographic camera-matching math, an ML-based depth-estimation Cops workflow with manual tile reassembly, and camera-relative NDC displacement math for a "world card" — all non-obvious, multi-domain techniques).

### Houdini Version
Not specified.

### Tags
camera-matching, depth-map, onnx, machine-learning, cops, solaris, karma-xpu, cgi-integration, texture-projection

---

## Related Tutorials
- [Texture Projection Tool for Houdini 20.5](texture-projection-tool-for-houdini-205.md) — the tool used here to logo-decal the bottle before this CGI-integration render.
- [Quick CGI Integration with Houdini and Solaris](quick-cgi-integration-with-houdini-and-solaris.md) — companion CGI-integration tutorial from the same channel using an HDRI dome + AOV compositing approach instead of an ML depth map.
- [Free Houdini Tutorial: Machine Learning with ONNX in Houdini 20](free-houdini-tutorial-machine-learning-with-onnx-in-houdini-20.md) — shares `machine-learning`/`onnx`; explains the underlying ONNX Inference SOP fundamentals (tensor shapes, channel-planar RGB restructuring, Attribute Normalize Float) at the SOP level that this tutorial applies inside a Cops network for the depth-map step.
