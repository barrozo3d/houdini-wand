---
title: Houdini for Beginners-  Part 7:  Timeline and Animation
source: YouTube
url: https://www.youtube.com/watch?v=Nb2YJJ7OHPU
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-for-beginners--part-7-timeline-and-animation/
frame_count: 0
frame_status: pending-selection
---

# Houdini for Beginners-  Part 7:  Timeline and Animation

**Source:** [YouTube](https://www.youtube.com/watch?v=Nb2YJJ7OHPU)
**Author:** Jordan Allen
**Duration:** 25m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-for-beginners--part-7-timeline-and-animation <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Now, I can hear you through the screen, right? You're going,
[0:02] Enough, Jordan.
[0:04] Ha ha, enough of the display options.
[0:07] I don't care about visuals. I care about time.
[0:10] To that, I say, that's a weird sentence.
[0:12] I don't know why you care about time so much, but sure, I'll indulge.
[0:16] Let's talk about the timeline.
[0:18] That was an amazing segue.
[0:19] We'll go ahead and delete everything in our scene. We've got a clean scene here.
[0:22] At the bottom, you may have noticed by now, there is, of course, a timeline, right?
[0:27] This is exactly what you'd expect.
[0:30] Right at the left here, we have our, you know, go to end, go to beginning.
[0:34] We have play forward, play backwards. We have a stop button.
[0:38] But you'll notice if you do hit play, which you can just hit the up arrow to do as well,
[0:43] it's going so fast, right?
[0:45] That's because this button right here is not active.
[0:48] This is an important button. This is the real-time toggle.
[0:51] If you press this, now we are getting playback in real-time along our timeline.
[0:56] That is important because if I create a box, I keyframe this.
[1:01] Whoops. I keyframe the center.
[1:05] And then, you know, let's say over the duration of the entire thing, I want it to move that far.
[1:11] I keyframe that too.
[1:14] If this is off and I want to play back my animation and get a sense of what it looks like,
[1:20] this is not at all a realistic depiction, right?
[1:23] This is way too fast.
[1:25] This is what it actually looks like.
[1:28] So important that you have this active if you need it.
[1:30] I don't really understand use cases where you don't have it on, to be honest with you.
[1:35] So I've just leave this on for the duration of everything that we do here.
[1:39] Now, a little bit more information here.
[1:41] We can see numbers here, right? Two number ones there, and then two number two forties here.
[1:46] By default, your scene will be 240 frames.
[1:49] That is 10 seconds, right?
[1:51] Because the default frame rate is 24 frames per second inside of Houdini.
[1:56] The very left button here is essentially the,
[2:01] if you hover over it, it will tell you it's the global animation start frame.
[2:05] This is essentially the start frame of your scene.
[2:08] The very end one here is the end frame of your scene.
[2:11] And these ones are merely the in and out clamps of what we are seeing in our timeline.
[2:16] If I shrink this, for example, you'll notice the timeline is changing.
[2:20] Now note that my scene duration is not changing.
[2:23] My scene is still very much 240 frames.
[2:25] But what I have access to in the timeline is a shrunk down version of that.
[2:30] Just for the sake of temporal resolution, so to speak,
[2:33] which is, you know, my fancy way to see it is zoom in on the timeline.
[2:36] All right. I shouldn't have said temporal resolution. I'm sorry.
[2:39] I got carried away a little bit.
[2:41] Point is now we've got a shrunk down version of our timeline that we can also, you know,
[2:44] click right in the middle of this thing and just drag around to reframe.
[2:48] Now we have frame one through frame 71 or we go, you know, frame 170 to frame 240.
[2:54] The in and outs here will show you in real time what our in and outs of the timeline are.
[3:00] But if we want to trim the actual duration, let's say, you know, let's go back to one and 240
[3:05] so we can see the full expanse of our timeline.
[3:08] If we actually want to trim the duration, let's say we don't want a 10 second thing.
[3:12] We want a five second thing.
[3:14] We just enter in our new duration right here, 120 frames, and that will clip everything,
[3:19] including the out point of our timeline since we no longer extend past 120 frames.
[3:25] All right. Now I've got this new look.
[3:27] Another way of doing this, I'll move this out of the way real quick.
[3:29] Another way of doing this is to click right here, the global animation options.
[3:34] You can hit alt shift G to open this up or you can just navigate over and press on this button right here.
[3:40] This is the global animation options, which gives you information about your overall timeline and project.
[3:46] We can see the frames per second is 24.
[3:48] We can see the start and end of our scene along with some other helpful stuff.
[3:53] One of the things being this playback, integer frame values,
[3:56] which if you don't know what an integer is versus a float and whatnot,
[3:59] we will get into that a little bit later, but this is helpful because, you know, as it currently stands,
[4:04] we can navigate one frame at a time.
[4:06] But sometimes you may have sub step information inside of your scene that you want to look at.
[4:13] And so by checking this, instead of going one whole number at a time,
[4:17] we can give a fraction of a number.
[4:19] So we're doing point one now.
[4:21] So look, I'm at frame 13.
[4:23] Now I'm 13.1.2, et cetera.
[4:26] And you can totally customize this however you want.
[4:28] I'm going to check that back on.
[4:30] So we have integer frame values again, and I'm going to close this.
[4:34] So just be aware of this here if you need it.
[4:36] Okay. So by now you have probably seen me do my fair share of key framing, right?
[4:41] I do it real quick, do a little animation.
[4:43] And I want to talk a little bit about that.
[4:45] How to actually key frame your own animations.
[4:48] Key frames are basically used to, essentially, time stamp locations in space
[4:53] or specific parameters for things.
[4:56] You can think of it as a key frame.
[4:58] It's a frame of great import, right?
[5:00] It's key to what we're trying to do here.
[5:03] So if we create, we'll hop up to the OBJ level here.
[5:06] I'll just clear my scene and I'll create a cube.
[5:09] And in this little experiment, I want to animate this cube.
[5:15] Purely along, let's actually animate it along all three axes, these translation axes.
[5:21] So I have it selected.
[5:23] How do I actually go about creating a key frame?
[5:26] Well, let's go back to frame one in our scene.
[5:29] And if I hover over any one of these boxes and I hold alt and left mouse button click,
[5:36] it will create a green box here.
[5:38] But this green box always means that this is a key frame, an animated key frame, right?
[5:44] I can key frame this, I can key frame this.
[5:46] And you'll see on the timeline, a little green box has now appeared,
[5:50] letting us know that there is a key frame of some kind in our scene on this frame.
[5:56] It doesn't dictate exactly what it is.
[5:58] It could be anything.
[6:00] It could be multiple parameters that are key frames, like in our case, we have three,
[6:03] but there's only one icon here.
[6:05] Just let us know on that frame, there is some animation, which helps us when we're navigating
[6:09] around the scene and looking for the important frames that we want to tweak after we've already done our animation.
[6:14] Point is, we've got it here.
[6:16] If we want to undo that animation, we hold control and left click.
[6:19] That deletes it entirely.
[6:21] If I hold alt and I click on the name of a three value parameter like this,
[6:27] it will key frame all three values.
[6:29] Same is true if I control click.
[6:31] So let's animate the translation here.
[6:33] Let's hit alt and click to create our key frame.
[6:36] We will then scroll all the way to frame 120, and we will then move this in space on the x-axis,
[6:44] on the z-axis, and on the y-axis.
[6:47] Now you'll notice these parameters are now green again.
[6:50] And it has created a key frame.
[6:52] It did it automatically.
[6:54] And now in between these frames, it will interpolate between our key frames, right?
[6:58] I'm not sure if it's on by default or not, or if it's just my setup,
[7:02] but this key right here to the very right of the timeline, this icon here to the right of the timeline,
[7:08] is where we can set up if we want auto key framing or not.
[7:12] If we undo this, I'll control click to get rid of that.
[7:14] And before I move it in 3D space, I'm going to click this little drop down,
[7:18] and I'm going to turn off auto key changes.
[7:21] Now you'll see that icon changes.
[7:23] Auto is now gone.
[7:25] So if I move it on the x, on the z, and on the y,
[7:29] now we've got like these dirty mustard color that is letting us know,
[7:34] hey, you've made changes to these parameters, right?
[7:37] But it's not confirmed yet.
[7:39] Like you have not locked in this key frame.
[7:41] So if you want to do it, you better do it,
[7:43] or else if you move away from this frame before locking it in, it resets it, and it undoes it.
[7:47] It says obviously that was a mistake, right?
[7:49] So we'll do that again.
[7:51] Boom, boom, boom.
[7:53] And we will key frame, key frame, key frame.
[7:57] And now we have that interpolation between those two positions.
[8:01] So if you want to have auto key frames on or not, that's your choice.
[8:05] There is an actual key frame button here that you can click in.
[8:07] It'll key frame, you know, certain parameters in the node.
[8:11] But to be totally honest with you, I don't even know how it decides which ones to key frame there.
[8:15] I didn't have anything highlighted.
[8:17] It just picked translate rotation and scale, but completely ignored our boys pivot, translate, and pivot, rotate.
[8:21] You know, that's not cool, man.
[8:23] That's not cool.
[8:25] So, you know, I don't typically use this button.
[8:27] I like to just use the, the alt and control click approaches to creating key frames.
[8:31] Now that we've got the key frame, we can play it back in real time.
[8:35] And looking at it, we are noticing it is easing into the animation and then easing out of the animation.
[8:42] Right?
[8:45] And then we can go ahead and change the animation curve.
[8:48] We can click on this animation editor button.
[8:51] We've been living in the scene view this whole time.
[8:53] We've been comfortable.
[8:55] We've made our little home here.
[8:57] It's time to get uncomfortable.
[8:59] It's time to venture outside of the Shire into a new tab.
[9:01] We are going to leave our beloved scene view and we are going to click on the animation editor.
[9:05] Right?
[9:07] This is a whole new world for us.
[9:09] Navigating in here is fairly straightforward.
[9:11] You right click and you're going to see the animation.
[9:13] It's fairly straightforward.
[9:15] You right click and drag in order to pan.
[9:17] You middle mouse button and drag to scale.
[9:19] You can either drag to the right to expand or up and down to shrink and grow.
[9:25] It's very intuitive.
[9:27] And then you can also use a scroll wheel to zoom out and you know, left mouse button click to highlight certain key frames.
[9:33] Now these are our key frames.
[9:35] These are the X, Y and Z translate values manifest as curves.
[9:40] But what does that actually mean?
[9:42] Well, if we click down here in our channel list, we can see our geometry name box one, box one.
[9:47] These are the values of the box right now.
[9:51] These are not key framed.
[9:53] So there's nothing about these that would be indicative of that.
[9:56] But the bottom the translate ones look their green here as well to let us know that they exist and they are animating.
[10:02] If we click on any of these values, we will realize it in the animation editor.
[10:08] If we click hold shift and then click on translate Z to highlight all of them, we can then see them all at the exact same time.
[10:15] Up here we see the timeline.
[10:17] We see frame zero going up to frame 120.
[10:21] So that makes a lot of sense.
[10:23] And we can see the easing that we're talking about.
[10:25] Now just for sake of visibility and simplicity, I'm only going to select the translate X for now.
[10:29] I'm going to zoom in and I'm going to move around and we will see.
[10:32] Yep, sure enough, it is easing into the animation and it's easing out.
[10:36] If we click and drag on any of these key frames, we will see the handles of that.
[10:41] Right.
[10:42] If we click and drag, we can actually change the value of that key frame.
[10:47] And by clicking and dragging on the handles, we can change the easing amount and the easing duration and really alter the way that our animation works.
[10:54] For sake of simplicity, I'm going to do something that we'll look at in a second and I'm going to split to this time.
[10:59] Don't worry about that.
[11:01] I'll cover that in a moment here.
[11:03] But here we can see our animation and our curve in the same thing, which will help us make a little more sense of this.
[11:08] Now, I'm going to move this out of the way.
[11:10] I'm having an issue.
[11:12] I'm so tired of trying to drag this around and scale it to fit in the frickin' window.
[11:17] Well, if I click in the animation editor, I can just click F to move around.
[11:21] I'm going to move around and I'm going to move around and I'm going to move around and I'm going to move around.
[11:26] Well, if I click in the animation editor, I can just click F to frame my selection to the window.
[11:31] This is true of all of them as well.
[11:33] If I highlight all of them and I press F, it's going to frame it all to the scale of the animation editor that exists in my viewport here, which is very helpful.
[11:44] So we can see it eases in and then it eases out.
[11:49] Well, let's say I don't want to deal with that.
[11:51] Well, I can click and drag on this key frame.
[11:53] Again, we'll switch back to just X here.
[11:56] I'm going to click and drag on this key frame and I can shrink this down by clicking and dragging this so that it doesn't exist.
[12:02] And I can click and drag on this to shrink it so it doesn't exist.
[12:06] And now I have a linear interpolation of the X.
[12:10] No more easing, at least on that axis.
[12:13] I'll Ctrl Z to undo that.
[12:15] If you click and drag and hold Ctrl, well, now it actually locks it.
[12:19] Because if you're just clicking and dragging, you can move it up and down on accident.
[12:22] Let's say you don't want to do that.
[12:24] Shift the duration of the handle.
[12:27] If you hold Ctrl and click and drag, you can just do that and drag it all the way in.
[12:31] Do the same here.
[12:33] Ctrl drag all the way in.
[12:35] And now you have a truly linear interpolation.
[12:37] You can actually just highlight the key frame here.
[12:39] Click on the handle itself and you'll get numbers down here.
[12:43] You can actually see acceleration 1.6.
[12:45] So let's say I want it to be an even slower easing.
[12:48] Well, I'll let that to 3 instead.
[12:50] I want it to be a 3 second easing.
[12:52] I mean, you can see that right here.
[12:54] The easing starts at frame 0 and it ends at frame 72.
[12:57] At 24 frames per second, that is 3 seconds.
[13:00] So we can shrink that down to 1 second or get rid of it entirely at 0.
[13:04] Again, lots of ways to do the same thing in Houdini.
[13:07] Resetting this one more time.
[13:09] Another way that we can do this.
[13:11] I'll scale this up for now.
[13:15] But another way that we can do this, if we highlight both of our key frames,
[13:18] let's say we just want to linearize it without clicking and dragging anything at all.
[13:21] Well, there are buttons up here as well that have control over how our handles operate.
[13:26] This, for example, the straight button will just pop them into being straight right away.
[13:31] If we want to get that back, we can click this one, Bezier handles,
[13:34] to get our Bezier handles back that we can now click and drag.
[13:37] Or we can click this one right here, set selected slopes to automatic,
[13:41] which will create automatic ease in and ease out.
[13:44] Lots of ways to play with this, lots of flexibility.
[13:47] You'll notice that they gray out the minute that I click away from any of the key frames.
[13:50] The minute I highlight it back, they're back again.
[13:53] Now there's also display settings.
[13:55] Now you might expect, right?
[13:57] Everything has display settings in Houdini.
[13:59] It's fantastic.
[14:00] Let's zoom in super tight here.
[14:02] Let's say we're in a section we're really working on this handle.
[14:04] And then I want to frame up the entirety of Translate X.
[14:07] I can choose vertical adapt and horizontal adapt to reframe top to bottom
[14:11] and then reframe left to right as well.
[14:13] Or I could again zoom in here, get all lost.
[14:17] And then by highlighting our Translate, clicking in the scene
[14:20] and pressing Ctrl A to select all the key frames that are a part of this slope,
[14:25] we can now hit F or press this button right here to frame that selection perfectly
[14:30] within the bounds of our animation editor.
[14:33] All of these things can be played with and tested.
[14:36] It's changing what handles you have access to, what numbers are visible to you.
[14:41] And you know, can be altered however much or little you want.
[14:45] I typically don't touch any of this.
[14:47] I don't do a ton of animating in here.
[14:49] And when I do, it's really just a matter of changing the easing amounts for the animations
[14:54] or just making them full linear animations.
[14:56] But there's a ton of flexibility that exists in here
[14:59] where you can create a new key frame and then, you know, completely alter
[15:04] the way that your animation plays.
[15:10] Now we were talking about framing a selection.
[15:12] There is one thing I want to cover real quick
[15:14] and that's that you can do the same thing with geometry.
[15:17] If I create another sphere in the scene and I move that way out yonder
[15:22] and I'm working on this and I want to frame the sphere
[15:26] but let's say I'm lost.
[15:27] I'm like, where the heck, where'd it go?
[15:29] You know, you get lost sometimes.
[15:31] It's okay.
[15:32] It's okay to admit.
[15:33] Let's shrink that down.
[15:34] I just clicked that little button to collapse it.
[15:36] Let's say we're lost and we want to get to that sphere.
[15:38] How do we do that?
[15:39] Well, we can frame.
[15:40] If we highlight this, we can hit space bar and f to frame this selected
[15:45] or select this space bar f to frame this selected
[15:48] or space bar and h to frame all the geometry in our scene.
[15:54] So we get like the full macro perspective of our scene.
[15:57] Space bar f and space bar h for that.
[16:00] Anyway, that was just a little subplot there.
[16:03] We're doing side quests now.
[16:05] Figured that was useful information for you to jot down in your notes.
[16:08] But the take home from this really is more about the animation editor.
[16:11] I want to touch one more time on this as far as additional ways to access this tab
[16:17] or at least a less obtrusive version of it.
[16:20] Let's say you want to keep your viewport as it is.
[16:22] You can simply hover over the parameters that you want to edit the curves of
[16:27] and hold shift and click to get a popup version of this animation editor in your scene.
[16:34] Now I can actually edit my animation.
[16:37] In a less obtrusive way, I can add another key frame there
[16:40] and I'll add another key frame there and I'll drag this over and I'll change this
[16:44] and I'll drag that around and I will make what may be deemed the most hideous animation of all time.
[16:51] And the cool thing is I just did it live because I'm that good.
[16:56] Pretty cool. Pretty cool.
[16:58] Now clearing my scene here.
[17:00] I do want to show you one more thing.
[17:02] If I create a sphere at the center of our world,
[17:06] I'm going to frame up to that
[17:08] and I, you know, key frame the translation there and I, you know,
[17:13] I'll say I just move it on the on the X, for example, I've got this right.
[17:17] Let's say I play this back and man, I wish it was stretched out a little more.
[17:22] Well, now I have to go back here and delete and then go here and set a new one.
[17:26] Wouldn't it be great if I could just drag this this key frame in the timeline over a little bit?
[17:31] Well, you probably guessed that you can.
[17:34] It'd be crazy if you couldn't do that.
[17:36] But the way you do it, you know, you don't click and drag, you're going to lose your mind.
[17:39] That's just how you navigate through the timeline.
[17:43] What you want to do is middle mouse button click and drag.
[17:46] That's how you kind of claim a key frame and move it around.
[17:49] But you'll notice it's kind of a funky navigational system because you get these handles over here
[17:54] that you can left click and drag and actually expand.
[17:57] And the way that this works is you can, you can middle mouse button click to create your, your window
[18:02] and then expand the window to encapsulate more than one key frame.
[18:07] Now if you middle mouse click and drag, you can move the collection of key frames over in any way that you want.
[18:13] Really proud of you guys.
[18:14] We're ripping through a lot of stuff here.
[18:16] This is fantastic.
[18:17] I hope you're enjoying it so far.
[18:19] You know, there's so much to explore and I really can't wait to contextualize all of this for you guys
[18:24] in the actual projects we do.
[18:26] But what I want to look at now is very important and we're going to use it a ton.
[18:30] So I wanted to at least touch it in this section.
[18:32] Right now I have a scene, right?
[18:34] I have a sphere that is being copied to a bunch of animated points on a grid that are moving up and down.
[18:40] And we have a, a whole army of spheres here that are undulating and bouncing free.
[18:47] If I pop out here to the OBJ level and I want to see what this animation looks like.
[18:52] Well, I've got my real time toggle checked.
[18:55] So that's good.
[18:56] And I'm going to push play.
[18:58] And what we're getting is, well, it just hit 24 frames.
[19:02] It took like four seconds to reach one second.
[19:04] The reality is there's too much geometry or too much information to compute in real time to get any sort of real time playback.
[19:12] So what am I supposed to do?
[19:14] How am I supposed to know if this looks good?
[19:16] I don't want to render a final image and waste all that time only to have it look like garbage.
[19:21] Well, that is where the flip book comes in.
[19:23] The flip book is this button right down here.
[19:25] Now don't press it yet.
[19:27] Pressing it will activate it.
[19:29] Let's actually pause our scene and right click on this for me.
[19:32] This will give you a flip up with new settings, a little toggle button that we can press, which will open up our render flip book pop up.
[19:40] Now these are essentially the settings for what will eventually be a preview render, so to speak of our scene.
[19:47] It's essentially a cached version of our viewport that we can play back in real time in order to make sure that our animations look good.
[19:54] Now right out the gate, you may see there's a few tabs of settings, but let's stay in the output tab for now.
[19:58] The main and most important one is this frame range.
[20:01] This is just asking what range of frames do you want to render essentially into this flip book preview?
[20:09] Now we've got a dollar RF start and dollar RF end.
[20:13] This is short form code.
[20:15] It's called H script.
[20:17] We are going to talk about H script later on.
[20:19] So for now, let's get rid of this and just replace it with one and replace this with 120 because I know I want the frame range to be one to 120 like my timeline is.
[20:31] Now underneath this, a very big gotcha.
[20:35] This one got me so hard in the beginning.
[20:37] If scoped channel keyframes only is toggled on, you will have a bad time because if there are no keyframes in your scene, it will do nothing.
[20:47] I can prove this by pressing start and it says flip book generation complete, but I got a whole lot of nada.
[20:55] It's only looking to generate flip books for animation frames and whatnot.
[21:00] Now I don't have traditional keyframes in here, so it's not going to do anything for me.
[21:05] That's no good.
[21:06] I always turn that off.
[21:08] That just causes way more problems than you'd want.
[21:10] I mean, it literally tells you here the memory usage.
[21:13] If you toggle that on, it reduces it to zero images.
[21:17] It's going to make no images for you.
[21:19] If I have keyframes here, let's say I create a keyframe there and then I create a keyframe there.
[21:23] I'm just moving the whole lot of them for whatever reason.
[21:25] Now I turn on scope channel keyframes only and look, it's up to two images.
[21:30] That means it's only going to create a preview for the two images that have keyframes.
[21:36] So we don't want that.
[21:37] Turn that off and actually let's delete these these awful keyframes with those keyframes deleted.
[21:42] Let's just go ahead and press start and see what we get.
[21:45] When we press start, we'll maybe we'll get this pop up.
[21:48] I'll go ahead and allow access there.
[21:56] And what we are getting is again a playback of the entire frame range that we selected in its own little m play window.
[22:04] So when it's done, we have a real time playback of what we would have seen in the viewport had it been capable of doing it in real time.
[22:19] Another helpful little thing in here is this top right button right here.
[22:24] This is the disconnect.
[22:26] So for example, if I shrink this down and I move this over here and let's say I change something,
[22:33] let's say I make it way lower, that's it.
[22:35] That's the only change and then I want to do another preview.
[22:37] If I push this button now, if I left mouse button click on this, we'll see it is overwriting what we just did.
[22:45] Right? Every single frame.
[22:47] Now if we go back, it's the lower version.
[22:49] But if we go further on to the ones that haven't done it yet is the higher version.
[22:52] This may be what you want to do.
[22:54] You may want to override it immediately and that's fine.
[22:56] But maybe you don't.
[22:58] Maybe you want to A B test, right?
[23:00] I do it a lot, right?
[23:01] I use my A B test to see the difference between the two.
[23:03] If you click this top right button, this disconnect, this window is now completely separated from what Houdini is doing.
[23:12] It's its own entity now.
[23:13] It's no longer connected to the active Houdini session.
[23:16] So what I can do is I can highlight this.
[23:18] I can bring this way up and then I can run another one.
[23:22] And what it'll do is it will create a new popup.
[23:25] Now, now I have two.
[23:27] And I can directly compare them by playing them both side by side.
[23:30] side by side to see which one I like better.
[23:36] So that's really cool, super duper helpful, right?
[23:38] One of the aspects though is this kind of looks
[23:40] a little bit like butt cheeks, to be telling you the quality
[23:45] on these viewport renders by default aren't that great
[23:48] because they don't have to be, right?
[23:49] It's not important that it's super high quality.
[23:51] It's mainly its main purpose is just to give you some
[23:54] semblance of an idea of what your scene is looking like
[23:57] when it's played back in real time.
[24:00] If I pause this and I go down though and let's say, you know,
[24:03] we can see up at the top here, 1280 by 720.
[24:06] We can see the resolution of this play blast, so to speak.
[24:11] If we right click here and go to flip book with settings,
[24:14] well now we can navigate over to the size tab
[24:16] and we can actually change the resolution
[24:19] of our next flip book render.
[24:21] We can also go into the effects tab
[24:23] and in the anti alias section we can choose high quality.
[24:26] We can even add motion blur if we want to, you know,
[24:29] with specific shutter, the motion blur always ends up
[24:31] looking really grainy because it's all temporary anyway.
[24:33] But let's say we raise the anti alias quality
[24:36] and the resolution.
[24:37] We can now start that one instead.
[24:39] And the quality of this one is much, much better,
[24:42] right out the gate.
[24:43] And we can see we've got that 1920 by 1080 resolution.
[24:46] And just one more time a reminder,
[24:47] if you're having any issues with the flip book,
[24:50] check that scoped channel keyframes only is toggled off.
[24:54] That'll save you a massive throbbing headache.
[24:58] I guarantee it.
[24:59] If you enjoyed this video and you wanna learn more,
[25:01] head to doublejumpacademy.com slash Jordan
[25:04] for the full course.
[25:05] Links in the description.
[25:07] You just click away, click it.



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
