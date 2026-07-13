---
title: Quick CGI Integration with Houdini and Solaris
source: YouTube
url: https://www.youtube.com/watch?v=xm9d-Un3Hrg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/quick-cgi-integration-with-houdini-and-solaris/
frame_count: 0
frame_status: pending-selection
---

# Quick CGI Integration with Houdini and Solaris

**Source:** [YouTube](https://www.youtube.com/watch?v=xm9d-Un3Hrg)
**Author:** cgside
**Duration:** 9m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py quick-cgi-integration-with-houdini-and-solaris <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in today's video I wanted to show you a quick
[0:04] setup to do your CGI integrations using Odinia Solaris and rendering with
[0:11] karma. So it's nothing too complicated but it requires a bit of a setup. So
[0:16] let's go through it. So I'm gonna disable the render and come back to my scene.
[0:21] As you can see I have this dome that I just modeled from a sphere and in order
[0:28] to visualize it better in the viewport I'm going to press D and go into
[0:33] optimize and as you can see I have this box here checked to remove back
[0:38] faces. So it's just back face calling in this case and it's just full to
[0:42] have it in the viewport and when you are projecting the HDI to the dome that
[0:47] way you can see what's inside. So I'm taking advantage of the background
[0:52] plate and building an environment to be projected. So in this case in the
[0:59] environment setup I'm starting with a sphere generator and cut it in half in
[1:03] this case and polypheal it, bevel it and subdivide it. Then I'm doing a UV
[1:09] project in this case to polar and I just rotate it around so I can fit it to
[1:15] the back plate. So in this case I also need to come here optimize and remove
[1:20] back faces and make sure you reverse it otherwise you will see the exterior
[1:26] and not the interior. So you can then attach a UV quickshade and load the
[1:33] RHDR or a quick JPEG if you want it to be quicker. Then I'm splitting in
[1:41] the grounds that I'm going to use to catch the shadows and also the
[1:49] environment which I'm going to use to have the HDI projected on. So that's the
[1:54] environment setup. Then I'm doing a render geometry settings on the dome and
[1:59] setting it to let's see in the render visibility. I'm setting it to not cast
[2:06] shadows, neither be visible to primary rays so not visible to the camera.
[2:11] What else do I have in here? I'm loading my model which is the
[2:16] pickup track that I did last week using the modular plugin but I might come to
[2:23] that in another video. Then I have some shadow casters which are just these
[2:30] vegetation alphas let's say that I'm using to project some of the
[2:35] environment around. This is a really sheep way of doing it. I can show you
[2:39] how I did it. So I just traced opacity texture. Then deleting the small parts
[2:47] iterating through them and moving to the center and do a basic remesh. Then
[2:51] copying two points with a line and playing with the scale. Mostly the
[2:58] not the piece scale but actually mostly the scale which I'm affecting the
[3:02] Y component so I can stretch them up and down. So it casts some nice shadows
[3:09] on the end reflections on the track. So we have our environment and our render
[3:16] geometry settings. Then in the back plates I am setting the ground as the
[3:22] primitive store projects the back plate and affect the and cast the shadows.
[3:28] I'm also not rendering the back plates so I'm diving into the background
[3:33] plates and in the render geometry in the render settings I am setting the
[3:38] use background to off. Otherwise I won't get an alpha channel for the
[3:43] for the compositing for the slap comp and for the material of the environment.
[3:49] I'm just I have the UVs because we did the UV project in polar mode for the
[3:56] dome and I'm just loading the HDRI in a standard surface with the emission
[4:02] color and set the emission to 1.5. Then I'm creating a physical sky because
[4:08] this emission won't really cast nice shadows so I'm creating a physical light
[4:14] let's say in this case physical sky and I'm aligning to the HDRI where
[4:21] where the light source is so roughly here so I can cast some nice shadows and
[4:27] this background plates if we look at the render if this doesn't take too much.
[4:32] So if I actually remove this slap comp review you can see that this background
[4:39] plate will output the all-out diffuse and the shadows as you can see and I'm
[4:44] also outputting an aO channel an aO aOv so I can really compete come some
[4:53] contact shadows between the the grounds and the tires that way it will feel
[4:59] more integrated in my opinion. So that's basically the setup we can I can show
[5:06] you some of some tips on the materials but for now let's go to the comp and so
[5:13] I'm doing a basic slap comp import and this will come with the beauty and
[5:19] some other shadows that I'm not using but I'm mostly interested in the all-out
[5:24] shadows that I can come into my back plates and aO. Then I'm loading the
[5:32] back plates and this comes from polyaven some of the HDRI's come with back
[5:37] plates I just search for some coherent environment for for this truck and I found
[5:44] this one which comes with the HDRI and the back plate and a few back plates and
[5:49] you know as soon as you import the back plates it if it doesn't have the same
[5:57] resolution as the render some people are finding some crashes with it so I'm
[6:02] doing a size ref in here and blending we blending it with the background so I
[6:07] don't have any issues of any crashing so but then I'm not actually using that
[6:13] back plates because in this case I remove the shadows so I did a shadow clean
[6:17] plate let's say and I'm loading that instead from there doing a basic color
[6:23] correction to the back plates and in here I'm loading the shadow the all-out
[6:32] shadows as you can see doing a channel extract and just getting the first one
[6:37] doing a basic multiply so I can have more effect and in here as you can see I'm
[6:44] just reducing the value scale because I'm loading that those shadows to the
[6:49] mask of the edges via just then I'm doing a multiplayer near that where I'm
[6:56] loading the ambient occlusion I believe let me see so yeah I'm loading the
[7:01] ambient occlusion in here and doing a basic multiply so as you can see we will
[7:08] have more contact shadows then I'm just blending with the with the beauty which
[7:14] is just this this truck with the alpha channel so and as a mask I'm using the
[7:26] I could have used in here the RGBA instead that would work the same but in this
[7:31] case I am extracting the alpha channel and loading that as a mask to blend in
[7:36] the truck just converting to RGBA and do the block end so yeah that's
[7:43] basically it so as you can see we have the shadows and some of the contact
[7:50] shadows from the ambient occlusion and we have some shadows in here from
[7:54] those alpha vegetation cards let's say and somehow integrates with the
[8:01] environment I just did the materials very quickly is not finished at all but I
[8:09] wanted to show you how I did this headlights which I didn't use UVs and it's a
[8:15] nice trick to know so as a final tip I'm gonna show you how I did those so
[8:19] basically let me see in here where is that grump so last lights I believe is
[8:27] this one so since I don't have UVs I created the texture with a ramp so
[8:35] just repeating a ramp and in here in the material I'm creating a material
[8:42] exposition and from there I am combining the X and Y components and using that
[8:49] as a textured coordinates in a material X image and that will just do a
[8:53] projection along this that which is where this truck is oriented to so and
[8:59] between between I'm doing a simple multiply multiply so I can repeat the
[9:05] texture and I'm using that for for both for the displacement you can use for
[9:12] normal also so it will be the same and so yeah guys that's basically it
[9:18] hopefully you got some tips out of this and I will include the the environment
[9:26] setup in the patreon files as far the truck I will leave it for other time
[9:31] where I will show you the material creation step-by-step so thank you for
[9:37] watching and I'll see you next time



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
