---
title: Houdini COPS Distortion | breakdown & project file
source: YouTube
url: https://www.youtube.com/watch?v=OHf8On_FMOk
author: nscr
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-cops-distortion-breakdown-project-file/
frame_count: 0
frame_status: pending-selection
---

# Houdini COPS Distortion | breakdown & project file

**Source:** [YouTube](https://www.youtube.com/watch?v=OHf8On_FMOk)
**Author:** nscr
**Duration:** 9m13s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-cops-distortion-breakdown-project-file <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Okay, so I want to talk a little bit about how I've been using COPs in Houdini.
[0:05] I've been using it a lot in my personal work to push around UVs and masks to get interesting effects.
[0:11] And I've been bringing it into my work at Future Deluxe to add distortion to products.


### Scene Setup [0:17]
**Transcript (timestamped):**
[0:19] So to dive into this project file, I'll link this down below, probably on my gumroad or something.
[0:24] I'm using a stripped down version that doesn't use any outside models or textures.
[0:29] But really the only thing here is this shoe that I brought off of CGTrader, that's really great.
[0:35] So in this render, there's really just a couple lights.
[0:41] And then we're turning on a few passes here, like the object position.
[0:48] I was using a Puzzle Mat, but we don't really need it.
[0:51] And the depth pass, which you can take it or leave it as well. We'll get into that later.
[0:56] But there's really nothing fancy going on here.


### Basic [1:00]
**Transcript (timestamped):**
[1:01] So once we're in COPs, we get this as our base render here.
[1:12] All I'm doing first is just applying this background.
[1:16] I just wanted a little bit more flexibility of doing it in COPs rather than in render to be able to change it after the fact.
[1:23] So what we're doing is applying a ramp, just blurring it slightly to get a little bit of a better gradient.
[1:30] When I'm merging it over, I also like to do this operation of soft lighting the background onto the foreground.
[1:40] What that means is before we do this, the shoe has no color information.
[1:47] It's just rendered in black and white and the lights have no color either.
[1:52] So to get a little bit of influence from the background, I'm just soft lighting it over the top and then brightening it up slightly and adding some contrast.
[2:05] So what that does for us, if I flip these on and off, is just putting it into that space.
[2:14] It's not a huge change, but I find that stuff like this goes a long way towards making the scene feel a little bit more integrated.
[2:24] But moving on to the distortion effect.
[2:26] If we just drop down to distort, see what that does off the bat.
[2:33] If we increase the scale, it's just moving it over.
[2:37] If we click streak, this is closer to the effect we want. It's just not in the right direction.
[2:42] So what I like to do is drop down a UV map and to get the same aspect ratio, I'll just drop the render into the size ref.
[2:54] And the way that cops works is from one to negative one.
[2:59] That's like the image space that everything sort of works in by default.
[3:04] So if we go to the distort node, this actually is going to work in our favor.
[3:08] Or if we look at like what the scale parameter is going to do, it says overall strength of distortion, negative values follow the directions backwards when tracing.
[3:17] So if I want to match that look from before, all I need is the vertical.
[3:21] So I can just get rid of the U cycles and that just gives us our up and down where the top is positive one, the bottom is negative one.
[3:29] So if I plug this into the UVs, we're starting to get somewhere.
[3:36] Whereas I can stretch this image and from the center it's starting to move in the directions we want.
[3:42] But if I want to expand this area where things aren't getting distorted as much, we can go ahead and make a ramp.
[3:52] We'll do the same size ref so that this gets into a 16 by 9 space.
[3:58] We'll change this to vertical.
[4:01] And if we plug this into scale, it basically acts like a multiplier.
[4:07] So you can kind of see the effect starting to happen, but we want to shape it a little bit more.
[4:13] So if I just change these to cubic so they're smooth and raise this one up, bring these down, make this a little bit sharper.
[4:29] You can kind of start to shape the mask of where you want things to be.
[4:37] Now this is the simple way, but we want to actually use information from the render itself to have a little bit more interactivity between the depth of some of these objects and like the mask for the distortion itself.


### Advanced [4:53]
**Transcript (timestamped):**
[4:54] So if we leave the simple version behind, I've already gone ahead and prepared a more complicated version.
[5:00] Now I want to start working with some of those passes.
[5:03] So if I look at what I output, the main one I want to take a look at is this object position.
[5:10] I'll just output that to a null.
[5:12] Basically what this is is tracking the bounding box of this object, even when it moves around in space.
[5:21] So you could apply this effect and it sticks to the object wherever it is.
[5:25] What we want to get a similar effect as that mask from before is to track the location from the front of the shoe to the back.
[5:33] If we just split out the blue channel and then start to play with like the brightness, we can see that we're moving a mask across the shoe.
[5:44] I have a function in here that's just a sign that will move up and down.
[5:48] That just animates between our timeline and so it loops.
[5:53] I just went ahead and did this instead of keyframing.
[5:56] But now that we have this mask and this range, we can go ahead and remap this to get a similar mask to what we had before.
[6:03] Except it's actually reacting to the information from the render and it's picking up the features and details of the shoe.
[6:12] You get some really nice separation happening.
[6:16] Then when you move it across, the remapped values are picking up what we did before.
[6:22] So then you get this sort of undulating movement.
[6:26] So in our mask, I just inverted this because I want the areas in white to get distorted and have this black area not distorted at all.
[6:39] In the remap, we can use the input min and max to change the width of this effect.
[6:48] And then to combine it with the background, I just took the alpha from the render, inverted that and used it as a mask to blend on top.
[7:01] So that we always get a constant value of being distorted out here.
[7:06] And then this is where our zero distortion on the scale later in black.
[7:13] So if we combine all these tricks, which is just a little bit more complicated version of what we were dealing with before, we get this result.
[7:21] But we get a much nicer movement across this space where the distortions really, I like what it's doing across like the laces.
[7:32] So it's not a complicated effect, but we're just using the parts of the render to influence what's going on.
[7:38] Something else I added in the render that I ended up finishing is adding some distortion into the UVs and post render itself.
[7:49] It's hard to see it, but it's just a little bit of break up that's happening in the first distortion that we're doing.
[7:57] So if I toggle that on and off, we're just getting a little bit more variation.
[8:04] If I play through it, that noise is animated and looping within our timeline.
[8:10] But you can kind of see what the noise is doing, undulating the amount of distortion that we're getting.
[8:16] So I combined that with that same thing across the whole render and then using the mask that we made before to drive the amount of distortion on top of everything else as well.
[8:30] So we go from this to this, which is pushing those pixels like even more.
[8:36] So if we go ahead and distort this, you get this sort of wispy smoke like effect, which I found pretty interesting to look at.
[8:45] But the whole thing is still pretty flexible.
[8:48] If we want to see more of the shoe, we just go back to that remap, either decrease or increase that area.
[8:54] And it all updates pretty quickly.
[8:57] So you can really craft some weird looks.
[9:01] I love what's happening with the laces especially.
[9:07] But yeah, that's pretty much the gist of the effect.
[9:10] Thanks, y'all.



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
