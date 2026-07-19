---
title: H22 - Animation | Motion Mixer | Sasa Budimir | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=VaUleTuvWgA
author: Houdini
ingested: 2026-07-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/h22---animation-motion-mixer-sasa-budimir-houdini-22-hive/
frame_count: 0
frame_status: pending-selection
---

# H22 - Animation | Motion Mixer | Sasa Budimir | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=VaUleTuvWgA)
**Author:** Houdini
**Duration:** 20m43s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py h22---animation-motion-mixer-sasa-budimir-houdini-22-hive <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro & Silly Character Animation Showcase [0:00]
**Transcript (timestamped):**
[0:00] NESTED CLIP
[0:05] Once again, welcome to this presentation
[0:09] throwing everything into the MotionMixer.
[0:13] It's going to be about the MotionMixer, basic workflows,
[0:18] and some new additions in Houdini22 like NESTED clips,
[0:23] and a bit about of wrangle setup and motion mixer setup,
[0:28] everything you have to do before you even go to that stage, get to that stage.
[0:34] And at the end, if I don't like talk too much, it will cover a bit of
[0:40] Solaris and Copernicus.
[0:42] But to go to a little bit about me, I'm Sasha, I'm a freelance 3D artist.
[0:51] I'm like coffee and sandwich enthusiast, of course.
[0:55] And I love making silly animations, silly characters, because they make me happy,
[1:02] they make other people happy.
[1:04] So yeah, it's kind of fun to do that.
[1:07] And regarding the silliness, are you ready for some silliness?
[1:13] Because I'm going to press play anyway.
[1:15] So if it works, yeah, we'll see.
[1:55] Thank you.
[1:58] Thank you.
[1:59] So yeah, regarding silly things, before I start about how all this started,


### Planning Simple Clips & The Animation Blueprint [2:05]
**Transcript (timestamped):**
[2:08] like Fiona contacted me and said, like, would you like to do something with the
[2:13] most mixer?
[2:13] I said, sure, I never touched it before.
[2:16] So why not?
[2:18] And but wasn't like motion mixer intended for like when you have motion capture
[2:24] clips and everything is very advanced and animated and everything.
[2:30] But like, yeah, this will be puppets.
[2:33] This will be very simple.
[2:34] This will be like a silly example.
[2:37] But hopefully you will get some little bits and pieces from it and maybe adapted to your
[2:45] needs, to your workflows.
[2:46] So yeah, be prepared, just be prepared for a very silly example of motion mixer usage.
[2:53] So disclaimer.
[2:57] So what's the plan?
[3:00] The plan was the cunning plan, I would say, to use animatic that I did before in just
[3:09] sops in old Kinefx and Rickbows.
[3:12] I didn't even go to Apex or anything.
[3:15] And to figure out exactly what kind of clips I need, I would love to like do just
[3:23] the basic sets of, you know, like attacks and dodges and whatnot and see, like, how
[3:33] low can I go with the animation without doing too much, without wasting too much time and
[3:41] enhancing it afterwards with, as you'll see, with some noises, like two kinds of noises,
[3:49] one noise for maybe keep alive when the character is standing still and the other one more
[3:55] a lively one when he's in motion.
[4:00] Then combine all those clips in motion mixer to get some kind of choreography, if you can
[4:08] say that.
[4:11] On top of that, add ragdolls, which makes everything very nice and very beautiful and
[4:18] all the stuff that you didn't do in those previous steps.
[4:23] Nobody will notice because ragdoll is amazing and you somehow get all the liveliness and
[4:31] in the end you just profit and have something nice and silly.
[4:37] So let's see what we have to do before even getting to the motion mixer steps.


### Rigging & Preparing Collision Shapes for Ragdolls [4:41]
**Transcript (timestamped):**
[4:46] So basically you start with your model.
[4:49] By the way, it's all modeled in Houdini.
[4:52] I don't know if I should recommend doing that, but I'm doing that so I love it.
[4:58] And yeah, rig is super simple.
[5:01] It's all FK.
[5:02] It doesn't have any advanced features because I didn't need them.
[5:06] I was mainly interested in, like, hand positions of those controls for the shield, for the weapons,
[5:14] because that is the only thing I cared about where it should be positioned and I was hoping
[5:22] ragdoll would do the rest and it did.
[5:25] So yeah, pretty basic setup.
[5:29] The only new thing I used from Houdini 22 was this auto-recomponent look-at.
[5:35] I think it's a bit updated and much easier to use.
[5:39] So I used that for the stick, for the hand stick or whatever it's called.
[5:46] This step is kind of funky but necessary.
[5:50] You have to prepare all the collision geometry for the ragdoll to work nicely.
[5:57] And depending on the shape of the model, I either used what's it called, I forget.
[6:09] Either you fracture it or you shrink-wrap it.
[6:12] Yeah, I remember.
[6:13] So it takes some time, but I think it's better to spend a little bit more time here and just
[6:22] have better and collision shapes to make ragdoll happy.
[6:31] And of course, this step is pretty nice, pretty needed.


### Auto-Extracting Joint Limits to Save Time [6:36]
**Transcript (timestamped):**
[6:37] You just do some silly animations of the limbs.
[6:44] So the configured joint limits can extract those keyframes, poses, and set up limits properly
[6:52] because otherwise it's lots of manual work and it wants to do manual work.
[6:59] So this is a lifesaver.
[7:02] And in the end, you just test, like I made this simple, like, seven keyframes animation
[7:07] and when you apply ragdolls to it, yay, it works.
[7:14] All the poses, especially on the pauldrons or shields and whatever, everything works.
[7:24] And basically, you just have weapon and a shield as a target for that drives everything
[7:33] else.
[7:34] Of course, it's a lot of fiddling with parameters, physical properties, stiffness and all of
[7:38] that, but in the end, it works amazing.
[7:44] And the last step for the motion mixer part, you have to do this.


### Motion Mixer Basics, Retiming, & Blending Clips [7:45]
**Transcript (timestamped):**
[7:48] I'm not sure exactly why, but there are two things, root control and cycle controls.
[7:54] It has to do something with, I don't know, matching probably when you're in the motion
[8:00] mixer, you'll see when you match Clip's position of your character between a couple of Clips.
[8:07] It just takes those controls that you select and do its magic.
[8:12] So I'm not sure exactly what it is, but it works.
[8:18] So motion mixer workflow, as far as I understand it, so take everything I say with a grain
[8:24] of salt.
[8:27] Basic stuff, if you just drag the Clip, it will loop.
[8:31] If you shift and drag, I think it's re-timing.
[8:37] You can see it, there's a little icon at the bottom, like it speeds it up or slows it down
[8:44] and you can reset it and whatever.
[8:48] You just have fun and play around with it.
[8:50] You can offset individual Clips, you can offset tracks.
[8:55] If you blend between them, like as you see here, it just blends the frames of the previous
[9:05] Clip and the next Clip, so you can do whatever you want.
[9:09] And it's pretty straightforward, pretty nice, pretty fast.
[9:13] You have nice search bar filter.
[9:19] If you have a lot of Clips, you can filter them by name, by whatever you wish.
[9:26] So yeah.
[9:29] And what I'm doing here?
[9:34] So this is the next track where I apply this noise motion.


### Layering Additive Noise & Using New Nested Clips [9:35]
**Transcript (timestamped):**
[9:42] But the thing is, you have to apply it a bit digitally, so it just acts on top of that
[9:50] previous track that you have.
[9:54] And of course, you can do keyframes, setting weights on it, so it depends if you want more
[10:02] or less.
[10:05] And basically, that's the only thing you have to do.
[10:10] And the new thing about these nested Clips, this is the only thing I could think of, like
[10:19] in my use case, to see what it does, is to nest this noise motion and whatever keyframes
[10:30] I have on a nested Clip.
[10:32] If you have animation effect or if you have weights or whatever, now if I just slide this
[10:39] Clip, it would also offset the keyframes, of course.
[10:43] But if you go inside the nested Clips, you still have the opportunity to move it around,
[10:48] left or right, find that perfect spot of noise, and all the other keyframes on the top level
[10:57] stay where they are.
[10:58] So it's very, very useful for that kind of work.
[11:03] I mean, probably you would do something more elaborate and, I don't know, useful than
[11:09] this, but this just showcases what it is about.
[11:14] And it's very cool.
[11:18] And after that, I just applied this ragdoll thing to the whole shot.
[11:26] Note, I could have done that in the motion mixer directly because you have access to
[11:33] the animation scene animate, but I just decided to do it afterwards because I knew I'll fiddle
[11:40] around with parameters, key them and everything, so I just wanted to have it separate and not
[11:46] do it in one, but you can do whatever you want.
[11:51] So just to recap, I did everything like that for all the shots, so you go with a simple
[11:58] animation, you really can't go simpler than that.
[12:05] You add some noise, now it's looking more lively.
[12:10] Add ragdoll, yeah, it's even more lively.
[12:16] And you get this guy.
[12:17] I mean, you trust him now.
[12:20] He looks, yeah, you would buy something of him, I don't know.
[12:25] He's legit.
[12:28] And yeah, that was the animation part.


### Cardboard Set Design & Lighting in Solaris [12:30]
**Transcript (timestamped):**
[12:32] Now, the time was running out and I had to do the other things like set design and because
[12:40] all the budget went to the puppets, set design was like cardboard, something, and I made
[12:47] this cardboard maker, it's an awful tool, but it used me, it served me like what I had
[12:56] to do.
[12:59] And yeah, importing everything in Solaris, doing some basic look there.
[13:04] I was kind of happy with it.
[13:07] I mean, half of the time it's out of focus, but if it's not there, it's probably, yeah,
[13:17] somebody will notice like you didn't put effort in the backgrounds.
[13:22] And then, yeah, this is my unseen way of bringing everything in because I'm really not that
[13:30] comfortable in Solaris.
[13:33] But basically, yeah, you have a scene structure, you just reference the characters, you reference
[13:40] the hair, the lights.
[13:43] Here are all the lights, I guess, for mainly all the shots.
[13:48] I did some tweaks from shot to shot, of course, but yeah, a couple of lights to make some
[13:55] kind of low budget children made scene puppets.
[14:02] I don't know what.
[14:04] And yeah, you will notice all these souls, like a crowd of people watching.


### Fast Post-Processing & Compositing in Copernicus [14:15]
**Transcript (timestamped):**
[14:16] And yeah, that's mainly it.
[14:18] I even used Copernicus for some basic compositing because I don't know how to compose it any
[14:24] better.
[14:25] So it's cool.
[14:28] I mean, a couple of notes just to, I always like to make things in render as close as
[14:36] possible to the final shot and just do some little tweaks here and there and yeah, look
[14:43] at that face.
[14:45] And with that face, I would like to say thank you, that's it.
[14:51] And once again, special thanks to Fiana for making everything possible and to Graham for
[15:01] amazing work on the sound and the music.
[15:05] Special thanks, of course, to Warren, who helped me figure out what nested clips are all about.
[15:14] And of course, all the amazing side effects that make this wonderful product for us to
[15:27] use.
[15:28] And super, super special thanks to Nikola, who saved this presentation like 10 minutes
[15:36] before it went, I went on stage.
[15:40] So Nikola, huge thank you.
[15:42] I don't know what I would do without you.
[15:44] I would like have to stand here.
[15:50] So yeah, thank you once again and hope I didn't bore you to that.
[15:54] So yeah, thank you.
[15:58] Wait, wait, you can't leave yet.
[16:05] Get back up there.
[16:07] Any questions?


### Q&A: Real-Time Performance Capture & Demystifying USD [16:10]
**Transcript (timestamped):**
[16:10] Okay, actually, I have a question.
[16:17] Okay, there's two.
[16:20] I'm just blank.
[16:22] Thank you, Sasha.
[16:24] I have more of a wonder than a question because I love your workflow and I love the whole
[16:29] digitally puppeteering thing.
[16:31] I know that you're an animator in heart and of course in profession, which we can see.
[16:37] I'm curious because even though this digital puppetry and you have like Houdini as your
[16:42] main weapon, have you tried any of the like analog capture performance things like using
[16:47] MIDI or something?
[16:48] I didn't try.
[16:49] I would love to try, but I guess it's a bit too technical for me.
[16:56] I'm not the most technical person.
[16:58] I mean, I like to dig around and figure out stuff, but yeah, not that.
[17:05] At some point, I would like to try something, something like, I don't know, maybe some,
[17:11] what's it called, when you have all in the gloves and just pop the tears, something.
[17:16] Leap or something like that.
[17:17] Yeah, motion lips, something like that.
[17:19] That would be amazing.
[17:20] That would be really fun to do because it would save all those tricks I have to do to
[17:28] get just that, which you could do just like in live and in a couple of minutes.
[17:36] Thank you.
[17:37] My pleasure.
[17:44] Thank you for the very fun presentation.
[17:47] And I'm glad to hear that.
[17:48] I've got a really silly question actually.
[17:51] I was wondering, how do you get into like Solaris?
[17:55] Because I'm from the games industry and I don't really mess with like the whole rendering
[17:59] thing.
[18:00] Sorry, I'll have to come closer.
[18:02] Sorry, how do you get into Solaris?
[18:04] So, you know, when you're rendering with all this like higher quality rendering.
[18:08] So it's a really silly question.
[18:10] Wow.
[18:11] Yeah.
[18:12] Never knew how to get into that.
[18:13] I mean, you're wondering like, how do you import all this animation, all this stuff into
[18:22] the Solaris?
[18:24] More, how do I get into Solaris in the first place?
[18:27] Because like I don't know how to answer that.
[18:29] I'm completely wrong person to answer that question because I'm in the same spot as you
[18:35] are, believe it or not, because every time I go there, it's like, what is this place?
[18:41] It's very new.
[18:43] It's very, and it's not Solaris.
[18:48] It's USD really.
[18:50] Yeah.
[18:51] I love it.
[18:52] And I love to see that little spark when I spend some time in it like, oh, I'm starting
[18:58] to understand this, you know, and then it's gone.
[19:04] It turns out I don't understand it.
[19:06] Yeah, but just keep it.
[19:09] It will, yeah.
[19:11] You see, if I could do this in like a month and a half and yeah, it's doable.
[19:20] Just, yeah, just stick with it.
[19:25] Somebody said there's no right or wrong in USD slash Solaris.
[19:30] So basically you can do whatever you want.
[19:33] If it works, fantastic.
[19:36] This is true.
[19:38] Are there any more questions?
[19:45] Did anyone catch the name of the asset that Sasha used to make the set?
[19:51] Oh, you did?
[19:55] Which asset?
[20:03] What's going on?
[20:08] I'm confused.
[20:11] Sorry.
[20:12] Loud voice musician.
[20:13] I'm confused with the asset and was it a wave it or something like that or no?
[20:19] What's the name of the card?
[20:21] Ah, I don't know.
[20:26] Thank you.
[20:27] But let's say it's the right answer.
[20:30] Yeah, yeah, I think because you're the only one who put up the hands.
[20:34] Exactly.
[20:35] Then you get the flip.
[20:38] Thank you, Sasha.
[20:39] Thank you.
[20:40] Thank you.
[20:41] Thank you.



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
