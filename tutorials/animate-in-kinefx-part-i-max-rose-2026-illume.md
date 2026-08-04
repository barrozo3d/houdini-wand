---
title: Animate in KineFX | Part I | Max Rose | 2026 Illume
source: YouTube
url: https://www.youtube.com/watch?v=SDyjrpW1ZB8
author: Houdini
ingested: 2026-08-04
houdini_version: "22"
tags: [kinefx, apex, animation, rigging, rbd, secondary-motion, spring, procedural, fbx, intermediate, houdini-22]
extraction_status: complete
frames_dir: tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/
frame_count: 19
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Animate in KineFX | Part I | Max Rose | 2026 Illume

**Source:** [YouTube](https://www.youtube.com/watch?v=SDyjrpW1ZB8)
**Author:** Houdini
**Duration:** 82m20s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everybody, welcome to the webinar. Super happy to be here. Super happy to see everybody
[0:11] joining. A really exciting topic. KineFX is relatively new to the world of Houdini, although
[0:21] it's been around now for a few years. Houdini 22 brings a whole set of new workflows, which
[0:27] we're excited to have a look at today. Max Rose is an in-house specialist who has been focused on
[0:34] APEX and KineFX for years now and joined the team about a year ago to really strengthen our
[0:41] capabilities in being able to show and demonstrate and provide feedback to the R&D team. He's going
[0:47] to take us through the webinar today. Over to Max. Hey guys, great to be here. Nice to virtually
[0:56] meet you guys. Let's see, we are at a lot of people, 116 people. Very cool.
[1:06] Let's see, so this is just going to be the first part of a two-part series where we're going to
[1:11] dive into animation in Houdini, and particularly character animation. This new animation system
[1:17] is being driven by APEX, which you guys may or may not know already. Now, APEX is just a framework
[1:24] that pre-compiles rigs, so it makes everything very fast and snappy. But APEX itself is a rabbit
[1:31] hole of information. It's very deep, it goes very, very far. So we're not really going to dive too
[1:36] deep into how APEX works. So the goal with this is to really try to keep this very practical, right?
[1:43] Personally, I really like using my hands, and I like getting in there, I like getting my hands dirty,
[1:48] and manually moving things around to get what I want. So today, in part one, we're going to go
[1:54] over some of the basics for starters. How do you work with a character in Houdini? What does that
[1:59] feel like? How does it differ from other softwares, maybe, and some of the benefits you may get out of
[2:03] it? And also just some of the tools that we have, including some of the new tools that we have in
[2:08] Houdini 22. So with that, why don't we go ahead and get started? And yeah, you're welcome.
[2:16] Awesome. Let's see. So I'm going to go ahead and share my screen.
[2:25] All right, let's see if this works. So I'm going to share my entire screen.
[2:32] Can you guys see this?
[2:36] Yes. All right, great. So let's see, I need to hide this. This is going to be tough. Here we go.
[2:47] Yeah, I need to kind of organize my scene. Because like, what is it? Zoom gives me this nice overlay
[2:53] that I really don't want, but I'm going to have to work with it. OK, so here we are in the demo
[3:00] scene. So this scene, this is going to be the same scene we're going to use for the next couple weeks.
[3:05] You can see here, so we got part one, the basics, where we're going to go look at animation basics.
[3:11] And we're going to be using Harry to go over the animation basics. And the second part of today
[3:18] is going to be going over some secondary motion and a little bit of set-driven key work.
[3:23] Next week, we're going to go into, well, part two, leveling up. We're going to go into the new mocap
[3:30] recipes and some of the new mocap tools that we have that makes it really, really easy to just
[3:35] get some mocap on your character and start moving. And then some more advanced techniques, which
[3:40] in my opinion are what really sets animation in Houdini apart from other softwares. And I feel
[3:46] like this part isn't really talked about a lot. So stay tuned for that one, because that one's
[3:51] going to be very, very cool. So let's go ahead and jump into animation basics. Now I'm going to go
[3:59] ahead and throw down Harry. OK, there's Harry. He's a rig. He's got everything we need right there.
[4:10] And to get animating, I'm just going to add him to a scene. OK, so I'm going to name him Harry.
[4:22] And now I'm going to put down a scene animate. Press Enter over the viewport.
[4:30] And there we are. Now we are animating. So really quick to just jump right into the animation state,
[4:36] because our rigs can just exist as nodes. We don't really have to find the file, nothing like
[4:43] that. It's all just kind of native Houdini workflow. So let's see. We want to start actually kind of
[4:51] moving him around. So let's actually kind of check out his rig a little bit. So before I start
[4:55] animating, I'm going to press P. And that'll open up this nice parameters window, where this gives
[5:02] me some options where I can kind of customize my interface. So in this case, I'm just going to click
[5:08] on this, the use, click, and drag function. And what this allows me to do is I can just click
[5:13] and just start dragging and immediately just start animating my character. So now I have my rig ready
[5:20] to go. I'm going to make a couple of changes to this. So I'm going to select this little gear
[5:26] control here. And what this is, is just these nice little config controls. You can see they're kind
[5:31] of all over the place. And what these are are just controls that allow us, or allow the animator,
[5:37] allow you and me to configure our rig components. And now a rig component is just an arm, a leg,
[5:46] a foot, spine, head, neck. These are all separate components. And when we build with the actual rig
[5:52] builder, we get these components for free. OK. And Harry was built with the actual rig builder. So
[5:59] we just kind of slapped a bunch of components together. And we had ourselves a rig. And then
[6:02] we get these nice little config controls. And these are great because if I just select this,
[6:07] right, that little IK, and now I just switch it to FK, now I can animate Harry in FK. And I'm a fan
[6:14] of animating in the arms, at least. I like animating my arms in FK. So I'm going to change
[6:20] both arms over to FK. All right. Now, if we're animators here and we're familiar with other
[6:27] animation programs, such as Maya or something like that, where within Maya we have something
[6:32] like Animbot, which gives us selection sets and allows us to kind of create groups of controls.
[6:36] We have the same thing here. All right. So I can just select these guys. I'm going to press G.
[6:43] And this opens up our little docked panel over here. And this panel has been updated, actually.
[6:48] So if you guys are familiar with the floating panels from before, now we kind of consolidated
[6:53] everything into a single panel. So we have layers. So now we can actually access our layers here,
[6:58] as well as over here. And we have settings, right? We have bake and constraint, all that good stuff.
[7:03] And we have the constraint settings up here. So everything is now just within one single window,
[7:08] which makes it very easy to just kind of keep track of where everything is.
[7:12] So now if I want to create a selection set, I have those controllers selected. Now I can just
[7:16] create a set from selected, Hill, Arm, FK. Boom. So now I have that. So now I can just use the
[7:24] selection set to select that. I can hide everything, just show this, just so I can
[7:28] focus really, just focus just on these controls. But in this case, I want to do some animating,
[7:35] but I've already created some selection sets from before. So I'm going to go and import those.
[7:40] All right, so I'm going to go to Apex Sets, Harry, Selection Sets, Replace, Accept.
[7:47] So now I've just filled out my selection set list. So now I have all these nice little selection sets.
[7:51] So I'm going to hide the gears, because I don't need those. I have one called hide,
[7:55] which kind of just has all these helper transforms, right, for the rigging. I'm going to get rid of those.
[8:00] Don't need those. And now I can go ahead and start animating. Okay, I'm going to go to frame one.
[8:05] I think we can kind of close this down a little bit. And let's open up Harry's eyes.
[8:10] Okay, so there he is. And now I can start posing him out. So let's start kind of creating a key
[8:18] pose. But really quick, what I'm going to do is I'm going to press Ctrl A, right, and just press K.
[8:24] And that keyframes everything. All right, you can see here within the channel box,
[8:28] everything is turned green. So now everything is keyframed. So I'm going to go ahead and just start
[8:34] animating Harry. And what I typically like to do when I'm animating my characters is,
[8:40] like if I get a character for the first time, I typically like to kind of do just sort of like a,
[8:46] oh, hey, didn't see you there kind of turn and it kind of thing. You know what I mean? Like it just
[8:52] kind of gives like a good read on the sort of personality of a character. Right. So that's kind
[8:59] of like what I like to do with Harry or whether it be like a xenomorph or, you know, whatever,
[9:04] like I like kind of just doing that sort of thing. So here's his kind of looking away pose. And then
[9:09] we'll get the next pose, right, where he's maybe kind of shocked, right. So we'll grab this,
[9:16] we'll just move this over and pull his arms out. Okay. And again, this all feels very familiar.
[9:24] It's all very, you know, by the way, I'm just pressing this little button here that kind of
[9:29] brings everything back to its original position. This all feels very familiar, right. So if you
[9:34] guys have animated in Unreal or Maya or even 3ds Max, probably not so much Blender because Blender
[9:40] kind of does their own thing, but you're going to feel right at home because this is all,
[9:45] this is pretty much just kind of like industry standard stuff. Okay. Definitely not trying to
[9:51] reinvent any wheels here in terms of rig interaction. Cool. So, okay. So now we have
[9:57] our second pose, right. So we have something like this. But if I press play, it's kind of boring,
[10:02] right. So let's go ahead and use our little animation sliders to add a little bit of in-between.
[10:10] So, or rather moving hold. So we're going to add just this kind of moving hold in the beginning
[10:14] here, right. So just a little bit of motion and then that really quick twist. And let's snap
[10:19] into that second animation faster. Right. So we'll get something like this.
[10:24] There we go. And I'm going to do just a little bit of overlap, right. So I'm going to take the head
[10:30] and just kind of offset that a little bit. So it kind of turns a little bit sooner, right. Okay,
[10:34] cool. So now we actually got ourselves a bit of animation and relatively quickly,
[10:39] but I think we all know how to animate here. So let's say that we have some animation
[10:46] that we like, but we don't want to, you know, go through and just recreate an entire animation,
[10:51] just like right now. I don't want you guys to sit here and watch me animate because that's going
[10:54] to take up like three or four hours. So what I'm going to do is I'm actually going to drop in an
[10:59] animation that I made before. So using the animation catalog, right, I have a few animations saved out.
[11:05] I'm going to go ahead and select all of my controls and just hit apply. And now let me
[11:12] spread this out just a little bit so we can see our full animation. And now, press play.
[11:20] Here's Harry. He says hi and he's cute. Nice. So now I have an animation that I can work with.
[11:27] So now we have this animation, right. So I'm going to just take a sec to focus on what's going on
[11:34] inside of this HDI, all right. Because it's pretty cool actually what you could do with these HDAs.
[11:40] It's kind of like unlimited really. So this is a relatively simple HDA. It's just pulling in a
[11:48] couple of different rigs and I'm assigning a material and then both of these are being
[11:53] passed into a switch node and then just being passed out. So very simple. And if I wanted to
[12:00] use that switch node, I actually have a little toggle that I made on the top level here. So if
[12:04] I select that, I switch out the rig. Okay. Now again, everything in Houdini is procedural
[12:13] as well as character rigging and animation. All of my animation data exists on just this single
[12:20] node right here. So if I wanted to, I could just take this whole thing and just copy it over,
[12:26] right. And now I have just a complete new copy of this. One thing I like to do with my rig nodes
[12:32] is I like to make them red and round. So if I have like a lot of nodes in my network viewer here,
[12:38] I always know, right, like if I scale out and I got a lot of stuff going on, I always know where
[12:42] my animation nodes are. So with these HDAs, there's so much you can do with them. I mean,
[12:48] we can have different materials. We can have different characters. You can even have a master
[12:52] HDA that has like your entire character pipeline just within a certain HDA, have a toggle, be able
[12:59] to select all of your different characters one at a time, just drag that out, get the next one,
[13:04] and put them all into a scene. Okay. So it's very flexible on how you can actually work with this.
[13:12] So let's jump in here. So let's enter. Let's get rid of that. Let's move that back over.
[13:18] And now let's take a look at what we have back here. So we have these little abstract controls,
[13:23] right? And these now come with sliders. So if you guys have messed with these in the past,
[13:30] these sliders didn't exist. So now we have just like a nice, you know, GUI for, you know,
[13:35] just knowing where your float values are. Right. So now we can just use these nice little sliders to
[13:40] kind of connect to certain float values within our rig and animate that way. Now, since we have our
[13:48] wings attached, why don't we add another animation? So I'm going to extend the timeline a little bit.
[13:54] I'm going to open the animation catalog again. Okay. And I'm going to select this fly away
[14:02] animation. Okay. So I'm select all my controls. And now I want to get to the last frame here. So
[14:08] I'm just going to just drag out and then hit shift left, right? Shift left on the arrow keys.
[14:15] And that just snaps me back to my next key frame on the timeline. So with everything selected,
[14:20] I'm just going to hit apply. And now we have our full animation. Okay. So there's a little bit of
[14:27] sliding coming from this layout control because I set some key frames from before. So I'm just
[14:32] going to select all those, shift select, and then just delete. Okay. So now we have a nice clean
[14:38] animation. Let's go ahead and let that play out. There's Harry. He says hi. And then he decides to
[14:46] fly away. Nice. Now, let's say we want to make some changes to this. We have our nice animation,
[14:56] but we want to make some changes. Let's say the director says, hey, we like Harry, but we want to
[15:00] get rid of the wings. And we want him to leave the scene in some other way, some kind of funny way.
[15:05] It's not so graceful, maybe a little bit more clumsy. Okay. So again, we don't need to make
[15:12] a whole new file iteration here. I could just take this, just copy it over again. Right. So now we
[15:17] have three different copies of just our single animation. So what we're going to do is let's get
[15:25] rid of the wings, right? That's going to be step one here. We don't want the wings. And we also need
[15:30] to remove that second animation. Okay. So let's get rid of that. Let's select all of our controls,
[15:35] control A, and let's go to frame 150 and let's get rid of all those, all that keyframe information.
[15:42] So now we just have this, Harry waves, a little heel pop, and he's happy. Cool. So to get Harry
[15:53] out of the scene clumsily, let's pull him out of the scene by his foot. And we're going to pull him
[15:59] out of the scene by his foot using ragdoll. All right. So to get to ragdoll, I'm going to press C
[16:05] and within here we have all these different options, right? So we can jump into sort of
[16:10] substates within the animation state. So here I'm going to go over to ragdoll and you can see that
[16:16] now we've just changed over to the ragdoll rig. See up here we're in animate ragdoll. So now if
[16:21] I press play, Harry collapses. And that's actually exactly what we want, right? We want him to collapse,
[16:27] but not yet. We want him to collapse at frame 150. So let's go back to ragdoll and I'm going to use
[16:37] my selection sets. Okay. So let's go to selection, selection sets, and toggle that down and let's
[16:44] hide the actual controls here. So I'm just going to click this little kind of locator looking icon
[16:49] here where it says next to Harry and that'll hide all the controls. So now we just have our ragdoll
[16:54] and we can just focus on this. Let's select all the ragdoll, right, using my selection set,
[16:59] and I'm going to deactivate it with this little active button here. Boom. Now it's deactivated.
[17:05] So now we can see that we're running our animation. So I'm going to reactivate the ragdoll at frame 150.
[17:11] Boom. So now we do this. Oh, I was playing it backwards. There. Kind of bounces around,
[17:19] but that's what we're looking for. And a little funny thing, if you press down on the arrow keys,
[17:23] it actually plays the animation backwards. If you press it up, it plays it forwards.
[17:29] So he's really kind of flopping around. So let's bring up the stiffness to about 25.
[17:35] Okay. And that looks a little bit better. A little bit more in control. Looks good. Cool. So one
[17:42] important thing we're going to have to do here is in order for ragdoll to work properly when we bake
[17:48] all of that ragdoll data onto our rig, we need to make sure that we're baking it onto the IK controls.
[17:54] Okay. So let's see. This is the, which one is this? This is the leg. So we need the arm configure
[18:00] control. And what we're going to do this is we're going to go to frame 150, right? That's where the
[18:04] ragdoll actually starts. So I'm going to select the FK. And you can see that the IK does its best to
[18:11] match the FK position. All right. So what I'm going to do is go back one frame and turn on the
[18:19] IK FK blend all the way back up to one. So that now we got that switch. Okay. I'm going to go do
[18:27] the same on the other side. Right. So we're going to go to frame 150, select that, change that to FK.
[18:35] One frame back up. Nice. So this is just like a little kind of texas switch, right? Texas,
[18:42] texas switch. I think that's what it's called. Where we're just switching back to the IK really
[18:47] quick. Now that little snap is not going to matter because when we actually bake everything
[18:51] from the ragdoll, it's not going to be noticeable. Okay. So what we're going to need next is a locator.
[18:59] So let's get rid of those controls for now. And let's go to the locator submenu.
[19:07] And now within the locator submenu, I'm going to press H or rather substate.
[19:12] So now we have a locator in our scene. I'm going to go back to animate.
[19:17] And let's kind of just nudge that right around his right foot. Okay. Something like this. And then
[19:23] while we're in animate, let's go to frame 150 and we'll animate this. Okay. So I just press shift T.
[19:30] Right. So now we have our translate key framed. Right. So shift R is to key frame rotation. Shift
[19:37] T is the key frame translation. I'm going to go to frame 180 and just pull this out. Cool. So now we
[19:46] got this little key frame there or rather animation. Nice. So the last step is to go to ragdoll.
[19:55] All right. Now very important when we're using locators to affect our ragdoll, we do not want
[20:00] them to be active. All right. This is not an active RVD object. So we'll just turn that off.
[20:06] All right. And let's go to frame 150. So when ragdoll is turned on, I'm going to go ahead and grab
[20:15] this right foot, grab the locator and press H. And I just tied a pretty much like a tether. Right.
[20:22] This is called a tether constraint. So essentially what I just did was I just tied a rope from Harry's
[20:27] ankle to the locator. All right. So let's go back. Frame one. Let this play out. And let's see what
[20:34] we get. Harry should be pulled violently out of the frame. And there he goes. Very nice.
[20:41] So since we did everything correctly, everything should just bake over nicely. So now with our
[20:50] menu open again, let's go to the bake tab. And well, first I'm going to select all my ragdoll.
[20:57] Okay. Very important. I'm going to select all my ragdoll and then I'm going to go settings, bake,
[21:02] and we're going to bake to a frame range. Okay. And the frame range here is going to be 150 to 200.
[21:10] And also very important, we're going to make sure that we're baking to a new layer and not overriding
[21:17] the base animation. All right. Now let's go ahead and hit bake keys.
[21:24] You can see that it's working and it's writing all that data to the actual controls.
[21:28] So now press play. Harry gets pulled away. Very nice. So there's a couple things happening here.
[21:36] For one thing is eyes are closing. We don't want that. And it's actually kind of funny
[21:40] because it's actually simulating correctly. The eyes are RBD objects, so that's why they're
[21:45] slamming shut like that. So let's just get rid of those key frames. And of course, we can go in
[21:53] here and grab all these controls and just add a new layer. And we can call this fix.
[21:59] And we can just keep on fit or whatever. Let's pretend that it says fix. And now we can just go
[22:04] in and just add some fixes here. All right. So I don't really like how the head's being pulled away,
[22:10] so I'm just going to go ahead and just kind of put that back into place. All right. So just setting
[22:16] some key frames. Just clean this up really quick. So now we have an animation that makes a little
[22:21] more sense. Okay. Nice. So we have our animation. Our director is happy with it. But let's say he
[22:28] says something like, hey, this is great and all, but I want, you know, this is a cartoon. We want
[22:33] some squash and stretch. Now, unfortunately, those squash and stretch controls were not included
[22:38] in the rig. So that means we're going to have to do something about that. So let's use some
[22:43] shot sculpting. Okay. This is my personal favorite tool. It should be yours as well,
[22:49] because it's credible. But we're going to put down the shot sculpt. All right. And well, first,
[22:54] actually, we need to get this animation, this character into a format that we can use. So you
[23:01] can see that I can't select it. Okay. It's not geometry. It's not unpacked geometry yet. So to
[23:08] get it to a format that I can go in and start selecting these points, we're going to put this
[23:13] into a scene invoke. All right. And there's a couple of different ways that you can do this.
[23:18] You can actually just go this way as well. This is just the evaluated Apex graph. But the problem is
[23:24] that this might run a little bit slower. When you invoke the scene, it actually runs a little bit
[23:28] faster. So in this case, I'm just going to use a scene invoke. And now I have unpacked geometry.
[23:35] Okay. I have my animation and I can go in and select and do something like that. And then Harry
[23:42] still does this thing. And we have this like kind of crazy thing going on, but we don't want that.
[23:47] It looks atrocious. So let's get rid of that. And now we're going to plug this into the shot sculpt.
[23:53] Now with the shot sculpt, very important. If you want this to work the way that you want,
[23:57] go to the defaults and turn this to world space. Okay. This just gives you much more predictable
[24:04] results. Now we're going to go into the shot sculpt menu. Let's go to animation, shot sculpt.
[24:11] Okay. And now we get this nice little timeline. So let's see. Let's find the pose, or rather the
[24:19] frame that we're going to want to work with. So right here, right? I think right here is heads
[24:24] kind of collapsing a little bit, but that's just because of that key frame that I said, but whatever.
[24:28] Let's just go in and we'll sculpt this and we'll pull his head out. So I just press B. So now I'm
[24:34] actually in the shot sculpt menu. And from here, we have a lot of controls that look a little bit
[24:38] like Apex actually. So if I press G, we can go in here and we have access to the radius, strength,
[24:44] spacing, all that good stuff within the brush, stroke, mask, symmetry, et cetera. And now I'm
[24:50] going to press three to go into the move brush. Okay. We have a bunch of different brushes here.
[24:54] And the move brush is what I use 90% of the time when I'm doing my shot sculpts.
[25:00] Okay. So let's find that frame. I'm going to press shift and control and drag, and then I can kind of
[25:06] pull that up a little bit. And then let's just kind of yank that out. Okay. And once I do that,
[25:12] it automatically creates this nice little frame here. And we have in and out points, right? We
[25:17] have this nice kind of Bezier interpolation kind of moving in. You can see here that this little
[25:23] white line is actually where I sculpted that track. Okay. So I'm going to pull this in just so it comes
[25:28] in a little bit later. And we can actually start stacking up different sculpts. Okay. So let's
[25:35] maybe kind of curve him a little bit, right? So he kind of curves into this pose.
[25:42] And I mean, I could just do this all day. Right. So this is going to be a small one.
[25:48] And we're just going to turn that off. Nice. So now we're getting something that looks
[25:53] pretty good. That's not bad. So let's exit the state. Let's say we're good with that.
[25:59] And we'll plug this into a cache, right? So that we could just quickly cache this and we can see it
[26:03] in real time. All right. We'll let that play out. And there goes Harry. There goes the shot sculpt.
[26:10] And there he goes. Nice. So really quickly, we added some very, very nice dynamism to this animation.
[26:18] And I mean, you can really just keep on taking this as far as you want, right?
[26:21] So that's the end of this section. Okay. And what I like to do is I kind of like to zoom out
[26:29] and kind of show off everything that we just did, right? Which is very cool. I mean, all within the
[26:33] scene and in just a couple of minutes, you have all these different animations. We switched out
[26:38] the rigs and we added some dynamic motion and then we went and did some shot sculpting. Okay.
[26:46] So I think we could just maybe take five here and maybe take a couple of questions and then I can
[26:52] move on to the next part. Does that sound good? I'm going to drink some water too.
[27:09] Are there any questions? Aliscar, Deb, Chris?
[27:13] So far they've all been covered in the chat by other people.
[27:16] Yeah. Oh, okay. Great. All right. Well, in that case, I think I'll just move on.
[27:21] Yeah. Keep going. That's awesome. Thanks guys. All right. So I'm going to jump up
[27:26] and now we'll go to secondary motion. All right. So we're going to put down a new rig. Okay.
[27:33] And this is the jack-in-the-box. All right. It's a cool little guy I made a while back for the
[27:39] launch. And this rig is actually very, very simple. So let me just show you what he entails.
[27:46] So I'm going to put down an apex add character. Okay. And let's call this jack-in-the-box.
[27:58] Jack-in-the-box. Scene animate. And then we can check out what this guy looks like.
[28:04] All right. So like I said, he's very simple. There's just a simple spline here, right? Just
[28:13] the three control spline that controls the spring. And then the rest of the doll is just FK, right?
[28:23] This is all just FK in here. So no craziness, no crazy bells and whistles. I think people,
[28:30] if you really wanted to, you could add some extra control here and maybe get some spline
[28:35] stuff going on. But in this case, this was enough to serve the following purpose.
[28:42] So what I want is an animation where, you know, that basic jack-in-the-box animation, right?
[28:48] Where we turn our lever, it opens, and then the jack-in-the-box pops out,
[28:54] but with all that nice secondary motion, right? So to get that, we're going to need a couple of
[29:01] things. And first, we're going to need a rest pose for our doll, right? Because I need to stuff the
[29:07] doll into the box. And I also need a mechanism to open up the top, right? So I can just kind of
[29:14] automate everything. A little bit of setup, but then once I have everything automated, I can just,
[29:18] you know, just animate it whenever I want. So we're going to throw down a recipe. And
[29:24] this is the set-driven-key recipe. So Apex set-driven keys. Okay.
[29:32] Now we're going to create the actual animations, right? Because the set-driven-key,
[29:38] the way it works in Apex is a little different from other softwares. This isn't a just one
[29:45] control working on like one parameter. It's actually anything driving a complete animation.
[29:54] Okay. So a whole walk cycle could be plugged into a set-driven key, and it's actually really easy to
[29:59] set up. So let's go ahead and set that up. So with the rig pose, it works a lot like the animation
[30:05] state, but, and this is the Apex rig pose, right? We have a kinfx rig pose, and this is the Apex
[30:11] rig pose. So the way this works is there's a few things you could do with it. Like if you want to
[30:16] set your rest position for your character, you can just click the update rest, which I'm not going to
[30:21] do. You can change the source type from Apex character to skeleton, and you can even promote
[30:30] joint positions that weren't there in the first place. So you can see here that now I have all
[30:34] these like spiral joints in here, but I don't need those. Okay. So I'm just going to get rid of that.
[30:40] All right. And it'll hide all of those unnecessary controls. Now I need to create a couple of
[30:48] animations, and the one, the first animation I'm going to create is the actual closing of our doll.
[30:54] Okay. Because I need that rest position so I can stuff her inside of the box. So I'm going to,
[30:58] let me see, I'm going to hide all of my box controls and grab all my doll controls,
[31:04] and then I'm going to make a new layer. Okay. And this is going to be doll close.
[31:08] Now this is the name of my actual set driven key, and we'll see how to initialize that later within
[31:14] this actual auto-wreck component, but it's important to kind of give this a name. Okay. So now we have
[31:19] that doll close. So with all those controls selected, I'm going to press control R and go to
[31:25] frame 24. I think we can crunch that down a little bit. And now I'm just going to create a kind of
[31:34] not so comfortable position for my doll so that she can just be stuffed inside of the box.
[31:41] All right. Let's grab our clavicles. Let's do this. And I'm going to grab the neck, crunch that down
[31:47] a bit. Let's grab these guys up here, roll those in. All right. This and we need to get these guys.
[31:58] So yeah, just getting these ready to stuff the doll inside of the box. Not a very comfortable
[32:06] position, but like I said, I think it really matters. There. She's very flexible. Cool. So we
[32:13] have our position, our animation set up. Now the next animation we're going to get is the actual
[32:19] opening of the box. All right. So let's get this control, right? This is the actual swivel control
[32:25] that opens the box. You can see that if I try to move it, we get this control not added to active
[32:31] layer, okay? Because we're in this doll close layer. So let's add with this selected, we're going to
[32:37] add, we're going to press this button right here, which is the create layer from selected controls.
[32:42] So now we're going to call this box open, not capital box open. Okay. And now let's just create
[32:50] a little animation here. So I'm going to press shift R and let's go to maybe about frame 12,
[33:00] something like that. And let's turn off this doll animation. I don't really want to see it. It's
[33:05] kind of distracting. So we'll just play that. Let's see. And I think we want that to be a
[33:12] little bit faster. And let's do something like this. And then we'll actually, let's push that
[33:19] a little bit and we'll just get some sort of like some follow through. Right. So it really kind of
[33:25] flies open, just get like a little bit follow through like that. Nice. So that's my animation.
[33:30] Okay. So now I have my two animations. I have a box open and a doll close. So now we can exit the
[33:36] state. We're done with that. Now let's go down to the auto rate component where we have our,
[33:41] the component source set the set driven key. So within our auto rate component, we have all these
[33:45] different components. And in this case, we're using the set different keys. So the animation
[33:51] layer that I'm going to want first is going to be the doll close. All right. And that's frame,
[33:57] start frame from zero to 24, if we remember. And the next one is going to be the box open.
[34:05] Okay. Box open. And that was from frame zero to 21, if I believe correctly. So now let's actually
[34:15] go in and let's jump in to that auto rate component and let's see what we get.
[34:22] All right. So we get this little gear here. All right. I select that. It's got to take a
[34:27] sec to think, but what it will give us is these two sliders, which we can use to now run those
[34:36] set driven keys. Okay. So we have our box open and the doll close. Nice. But like I said before,
[34:45] I wanted to create a mechanism for the box so that if I rotate this guy, right, this control here,
[34:53] that we'll get, that we could open the box that way. So let's actually tie this,
[35:00] this control will be the driver of that animation. All right. So let me set that back to the center
[35:08] and let's go to the driver. All right. So with the control selected, what you can do instead of like
[35:13] looking at the name of the control and trying to like copy and, you know, by memory, what you can
[35:17] do is actually just shift select the current selection option. And then I get that. And then
[35:23] I could just press control C and then just paste it. Hmm. Oops. That's weird. Okay. So now I have
[35:32] my control in there, but what I want to do is press R X. Okay. So we want the rotate X channel
[35:41] to be the thing that drives it. Okay. And really quick, I just want to make sure that everybody's
[35:50] still there, that there was like a weird little glitch here. We're still good, right? Yep. Still
[35:55] good. Okay. Great. Cool. So now I have this crank base, right? And this rotation X channel of the
[36:03] crank base is now going to be driving this animation. So if I rotate this, you can see
[36:09] that it just goes way too fast, right? Way, way too fast. But that's because we're getting to this
[36:16] zero to one range really, really quickly within this rotate X channel, right? So we don't want
[36:22] that. What we want is to rotate it a bunch of times and then have it open. So let's do that.
[36:27] Let's rotate it a bunch of times, which I just did. And we'll select this number. Okay. And I'm
[36:35] going to paste that into there. We'll get rid of that 666 because that's bad, bad juju. And then I'll
[36:40] go rotate it a bit more, right? Just something like that. And then this will be our range. Okay.
[36:50] So I'm going to plug this into the fit min and then the fit max. Great. So now, let's see.
[37:00] Let's set that back to the zero position. So let's rotate this a bunch of times and then, boom, now we
[37:09] have our mechanism, which actually opens up the box in kind of a realistic way. Cool. So now we have
[37:16] everything we need to complete our animation. So let's exit the state. I'm going to go into the scene
[37:24] animate here. All right. And let's just reset everything because I don't want all that extra
[37:31] stuff that I did before. And again, I'm going to make this round and red because I'm just obsessed
[37:39] with doing that with my scene animations. And now let's jump back in. All right. Cool. So now we're
[37:47] back on the scene animate and we have our little set driven keys. Very cool. So let's go ahead and
[37:53] create our first animation. And in this case, we'll just open up the box. Okay. And we're going to
[38:00] create our doll animation first. So let's close up the doll, right? Because we're going to have to do
[38:06] that. And we can hide all of her controls. We're not going to need those for now. I'm going to grab
[38:12] the spline. We'll plug that or we'll just kind of cram her into the box. So there we go. So now the
[38:17] doll is in the box and we'll set a key frame, shift T, right? Just an initial key frame. And we'll go
[38:26] to frame 12. And then we'll just lift this up. Boom. All right. Now the next key frame we're going
[38:32] to have to hit is this set driven key. So with that selected, I'm going to press K and then we're
[38:38] going to go to frame 12 again and just drag that out. Nice. So now our doll is doing her thing.
[38:48] So you can see that there's a little bit of penetration. I'm going to open her up just a
[38:51] little bit later, right? So we'll use this tween to kind of just bring her closer to her rest position
[38:57] and then she pops open. So then we get this. Now this is all we need to get the animation that I want.
[39:05] All right. Just these couple of key frames. So now we're going to start adding some secondary
[39:09] motion to this and some dynamic niceties. Okay. So let's move that over. Let's get some more space.
[39:16] Now to get the secondary motion, we have all these nice little pose tools up here. And secondary
[39:21] motion is the last one, right? So we have full body IK, full body IK posing. You also get the
[39:27] ragdoll here, locators, dynamic motion, all that good stuff. And the last one here is secondary
[39:33] motion. So I'm going to click on that and all my controls turn gray. Okay. Because secondary motion
[39:39] is now waiting for one of these controls to have some secondary motion. So once it turns gold,
[39:48] then it actually has some secondary motion attached to it. So the secondary motion effect
[39:53] that I want, you can see up here, we have a couple of different ones. We have lag,
[39:56] we have a jiggle and we have spring. So obviously spring, right? So let's click on the spring.
[40:04] We're going to click on the spine coil. Really important. One thing I want to do is I want to
[40:09] make sure that we're affecting the translate, okay? And not the rotation. All right. We're going to
[40:15] affect the translate in this case. So once I press plus over here, we add that secondary motion to
[40:23] that control. So from just that one key frame, now we can get something like this. Now the effect is
[40:32] pretty strong. So let's go down to the effect options and I'm going to put this to four. Okay.
[40:39] So now we get something like this. All right. And that looks better. That's a little bit more
[40:44] manageable. It's not going to be so intense. Let's give ourselves a little bit more room down here,
[40:50] about 150. And now the next thing we need to do is bake this. Okay. So very similar to the rag doll
[40:56] workflow where we get our animation that we want, we get some cool dynamic effects, and then we bake
[41:01] it to a key frame, or rather we bake it to a layer, and then we just kind of move on from there.
[41:07] Okay. So with this selected, we're going to have a frame range of one to 100, additive layer, bake to
[41:13] new layer, bake keys. Okay. And what's nice about secondary motion is that the key frames actually
[41:21] bake very quickly. Nice. So we have this. And now from here, we need to add some secondary motion
[41:28] to our doll because this almost looks good, but why not make our doll all kind of floppy and crazy?
[41:35] Right. So let's get our doll controls back. Let's actually just go ahead and select all of them.
[41:41] Actually, no, we don't need to select anything yet. Let's just go straight to
[41:45] the secondary motion state. Now you see that something just jumped, something happened.
[41:51] But what's happening is that this spline coil control still has secondary motion attached.
[41:57] You can tell that because it's this kind of golden color or green. Okay. So we need to remove it
[42:04] because what's happening is it's kind of doing it twice. All right. So it's doubling up because we
[42:10] have a secondary motion here and we also have it here. So I'm going to select it and remove
[42:15] that secondary motion. So now we get what we had before. Now I can hide all the box controls. I
[42:21] don't need those anymore. And let's select all the doll controls. And now I've found that what's
[42:28] best here is to get rid of the root control. Okay. So we don't get any kind of crazy double
[42:35] transformations here. And we're going to use the spring effect again, but this time we're going to
[42:42] affect the rotation channels, not the translation channels. All right. So with all these controls
[42:47] selected, rotation is set up. We have the spring plus plus, and now we have this and it's a total
[42:56] mess. Look at that. Real crazy. That's not what we're looking for. People aren't going to respond to
[43:02] that. So let's start messing with the strength over here. Let's turn this down all the way.
[43:08] All right. And let's turn it on maybe about like right here. Right. We'll set a key frame,
[43:14] alt click on the parameter, right? Just turns green. So now I just set a key frame
[43:19] and let's just jump forward with the arrow keys and go to this point. This kind of like this apex
[43:26] on intended. Okay. Cool. So we get something like that. So when she gets up to the top,
[43:32] boom. Nice. That looks fantastic. I'm very happy with that. So let's go back to the selection
[43:40] set and we're going to grab our doll again. Let's remove this root spline. We'll go to settings
[43:48] and where are we? You need to go to bake and go from one to 100 again with all of our controls
[43:55] selected, additive layer, baking to the layer, check, check, check, bake keys. And then we have
[44:02] a new layer. Let's go back to animate. Cool. And now we have our animation.
[44:10] So we still need another animation here, right? And which animation do we need? We need to open
[44:15] up the box. Okay. Cause the box is already open. We just have this animation here, which is really
[44:21] nice. You know, I'm very happy with it, but we still need to have that, you know, anticipation
[44:26] of the box opening. Now there's a couple of ways I could do this. I could create another scene
[44:31] animate and then copy the animation and then put it into a motion mixer. But all I really need is
[44:37] just another clip. So why don't we just create another clip within the scene animate? So I'm
[44:43] going to go to animation up here. All right. This is the nice little animation tab and I'm going to
[44:48] click on new clip. All right. We're going to call this box open. Okay. Let that load up. Because
[44:57] what it's doing is it's just creating a blank clip within this scene. Now you can see here,
[45:04] it created this nice little dropdown where I have the default clip, which I just made before,
[45:09] and the box open clip, which I just made just now. Okay. So now we, you know, we don't have our
[45:15] animation layers anymore. We're just having a blank clip. So now we can just work with this.
[45:19] This one's going to be easy. So let's just close the doll. Let's get our controls back from our box.
[45:26] We'll stuff the doll into the box. We'll grab this crank base, frame one, shift R, keyframe,
[45:34] pull that out to about 120, rotate it a bunch of times, and then boom. There we go. Nice.
[45:43] So I think we know where this is going to go. Play, play, play, play, play. Great. So now we have
[45:49] our animation. But not just that, we have both of our animations. Okay. On the single scene animate.
[45:56] So now I need to access those animations, right? And plug them into the motion mixer.
[46:03] So let's put down the motion mixer.
[46:08] All right. It's going to take a sec because what it's doing is it's taking those clips
[46:13] and it's converting them to a format that then we can use within the actual motion mixer's sequencer.
[46:18] Okay. So it's taking those clips and kind of checking their in and out points and it's
[46:23] turning them into these nice little clips that then we can kind of put together
[46:29] and mix and blend and do all sorts of good stuff. So now we can jump over to the motion mixer
[46:35] and you can see here that within the actual catalog, right? So the catalog parameter settings
[46:41] within the motion mixer, we now have access to those clips. So we have a rest pose, right?
[46:46] The default pose, which will actually default animation. We didn't give that one a name,
[46:51] but if we remember from before, that one is our opening animation, right? Or rather the bouncing
[46:57] animation. And then the box open. Okay. You can see the length, you can see the clip,
[47:01] how many times it's actually been used. So let's drag these on to our timeline here.
[47:08] So I'm just going to grab this box open. That's our first animation,
[47:12] right? Because we want this to be our first animation.
[47:16] And then default, or rather the opening, or rather the springing animation is going to come second.
[47:24] So I want this to happen like right, right when it opens. So what we're going to do is we're just
[47:31] going to kind of blend these two together. Okay. So find that point, like right there,
[47:37] let's bring it even sooner. There we go. So we get this and then that.
[47:45] Nice. So it doesn't necessarily need to stop there. Let's say we have our animations and
[47:55] we can see here that there's a little bit of something going on here. There's some penetration,
[47:59] but we want to go in there and we want to jump back into the animation state. Okay. So what we
[48:05] could do with the motion mixer is we can go to the settings and we can actually have different
[48:09] output modes. So from here, I'm going to go to Apex Scene. So just to kind of inform you what
[48:16] I want to do here is I want to take this blended animation and I want to take it out of the motion
[48:22] mixer and I want to put it back into an Apex Scene. Okay. So there's a couple steps involved to do
[48:29] that and here's how you do it. So within the mode here, this output mode, you want to change that to
[48:34] Apex Scene. Okay. And it's going to take a sec because what it has to do is it has to convert
[48:40] everything back to a usable Apex Scene. All right. So let's see. Once I can start dragging things out,
[48:48] things are ready to go. And now I want to fetch that motion. Okay. So I'm going to put down a
[48:55] motion mixer fetch and then from here, I can just drag this up to here. Just plug that in and now
[49:03] we're going to output an Apex Scene. We'll click on that. We'll let that cook. Let that do its thing.
[49:15] All right. Just loading up the geometry, building out the Apex Scene.
[49:20] And then once this is ready to go, I can throw down a scene animate.
[49:27] All right. I'm going to make that round and red like always.
[49:29] Let this do its thing and then I can jump back in to Apex. Cool. So now I can go in here and I can make some adjustments.
[49:41] So you can see here that I have my base animation, right? This is the animation that's coming from the motion mixer.
[49:46] Okay. And you can see that there's this penetration in here. So if I really wanted to,
[49:52] I could add this to a new layer, call this fix, and then look for those in and out points, right?
[50:00] So let's rotate this, right? I'm going to hit rotate there and then rotate here, something like that.
[50:08] And then we'll just kind of keep it down like that. There we go. So now we just fix that little bit of penetration there.
[50:15] Great. Nice. So there's our final animation.
[50:20] Awesome. Well, that is the end of this course, of this part, and we still have about nine minutes left.
[50:28] So if there's any really probing questions or something that I feel that people would like to see or anything else,
[50:39] let me know and I'll see if I can...
[50:41] We've had a few along the way, Max.
[50:43] What's that?
[50:45] So we've had a few questions. So Irma says,
[50:49] questionable putting character on high heels, that not a character part and insert it in scene as props. Is that possible now?
[50:55] And could you teach how to do it the proper way?
[50:59] I'm sorry. I feel like there was two parts to that question. I heard how to do it the proper way.
[51:04] I'm sorry. I feel like there was two parts to that question. I heard high heels and then props.
[51:10] Yeah.
[51:12] So...
[51:14] And maybe Irma, if you want to clarify what you're looking for, we'll come back to it.
[51:18] And Guillermo says, are there any IKFK switch matching?
[51:24] Yes, there is. So with Harry, you can do IKFK switch matching.
[51:30] And that actually comes with the rig builder.
[51:32] So if I just put down a new scene animate and move this around,
[51:36] let's see, click drag.
[51:38] And then as I showed before,
[51:42] we just change it over to FK.
[51:44] And we just matched everything.
[51:46] Yep.
[51:48] And you can also blend from FK to IK, right?
[51:52] If you want to kind of smoothen that out a little bit.
[51:54] Because just the solvers are just slightly different.
[51:56] You can see how there's just a little bit,
[51:58] it's almost like a...
[52:00] It's almost like a skinning thing, right?
[52:02] But yeah, yeah, there is.
[52:06] Awesome. And Irma clarified that high heels would be added as props to the scene.
[52:10] High heels would be added as props.
[52:12] And by the way, and this applies to everybody,
[52:14] I just made it so that you're able to unmute yourself.
[52:16] So Irma, if you want to jump in and clarify by audio visual,
[52:22] that'd be helpful.
[52:24] Yeah, sure.
[52:27] I'm sorry.
[52:29] So yeah, I'm trying to add high heels as props to the scene.
[52:31] And just trying to put the character on it.
[52:33] Like, I'm not really interested right now in like,
[52:37] sculpting the character for the high heels.
[52:41] I have the high heels like getting from the other part of the...
[52:45] So that was my question,
[52:47] how I could like adjust the height of the animation.
[52:51] And then I can also adjust the height of the animation.
[52:55] Height of the animation in proper way.
[52:59] Okay, so you could just build out...
[53:01] Let me see.
[53:03] Let's see if I can figure something out really quick.
[53:05] So like you could just build out like a, you know, any kind of control.
[53:09] But then you can also add it as a prop.
[53:11] So I'm just going to show you how to add things as a prop.
[53:13] So let's just call this shoe.
[53:17] Okay, so apex add prop.
[53:19] Okay, so scene add prop.
[53:21] Alright.
[53:23] And let's see, so we're going to do our character scene.
[53:25] So this is the whole scene.
[53:27] And then the next thing we're going to need is this.
[53:29] Okay, so this is the new prop that I just made.
[53:33] Alright.
[53:35] So we're just going to be static animated forming.
[53:39] So that's going to control.
[53:41] Okay, so that should work.
[53:43] So now we're going to put down a new scene animate.
[53:45] Let's see, I'm going a little bit off script here.
[53:47] Let's see if this works.
[53:49] Okay, cool. So now we have this.
[53:51] So we have this nice little prop in here.
[53:53] Let's pretend that this is a shoe.
[53:55] Okay.
[53:57] And we can actually angle this up.
[53:59] Something like that.
[54:01] Let's pretend that this is our high heel.
[54:03] Okay, now we want this prop to actually control this foot IK.
[54:09] Right?
[54:11] So we're actually kind of doing a little bit of rigging within here.
[54:15] So I always kind of forget the order.
[54:17] I think it's child parent.
[54:19] Okay, and then I press H.
[54:21] Yeah, there we go.
[54:23] See? So now we get something like this.
[54:25] So really quick, you can kind of get like a little bit of sort of a high heel kind of look.
[54:31] Right?
[54:33] But I think, yeah.
[54:35] Sorry, I know this part.
[54:37] Yeah, like I'm familiar with that.
[54:39] The problem is like right now, if I'm going to start animate character moving,
[54:45] the height of the character like change and the moving of the part like the heels also should change and affect the floor.
[54:59] So do you mean the geometry?
[55:01] Yeah, yeah.
[55:03] Oh, the geometry of the character.
[55:05] Oh, okay.
[55:07] Yeah, so yeah, that's just kind of like a way to sort of update your rig.
[55:11] So one thing you can do,
[55:13] because again, this is all procedural.
[55:15] Right?
[55:17] So if I were to just kind of like unpack my character.
[55:19] Let's see, unpack character.
[55:21] So I can go in here.
[55:23] I can unpack my character.
[55:25] And let's say I want to actually go in and like change Harry up.
[55:29] So this is one thing.
[55:31] This is one thing you can do with your character.
[55:33] It's actually kind of cool.
[55:35] And I always kind of like doing this because I think it's kind of fun.
[55:37] So let's make sure to turn this on to symmetrical.
[55:41] Okay.
[55:43] And I'm just going to again, just kind of like give Harry some teeth.
[55:45] And make him mad.
[55:47] So, okay, so from what I understand, the question is, you know, how do I kind of update the actual geometry?
[55:55] So it's actually pretty easy.
[55:57] So now we unpack the character.
[55:59] So now I'm going to pack it back up.
[56:01] Okay.
[56:03] Let's do that.
[56:05] And what's really cool here is that if I plug this back in,
[56:09] you can see that we have this new geometry all set up.
[56:15] And this is what I mean by everything being procedural.
[56:19] And one of the huge benefits you get from things being procedural is that you can kind of change anything anywhere at any time.
[56:27] And you still get this nice looking thing.
[56:31] You still get your animation.
[56:33] You don't really lose your data.
[56:35] So I hope that's helpful.
[56:37] I want to get to another question because there's not too much time.
[56:41] But I hope I was able to help with that.
[56:43] Yeah. Carol's got some questions.
[56:45] Three questions.
[56:47] Does Node ShortsCult working with Gsplats as well as with Rig Model?
[56:53] Is the ShotsCult working with Gsplats?
[56:57] I don't know.
[57:01] I don't know if ShotsCult does work with Gsplats.
[57:03] I think it could.
[57:05] I don't see why not.
[57:07] Because the thing is that it's represented with points.
[57:09] So you might have to have a geometry cage and then that kind of thing.
[57:13] Well, let's figure that out.
[57:15] So let's say a box.
[57:17] So if I'm able to do this, then you're able to do it.
[57:21] So we'll say points from volume.
[57:23] Because I'm actually kind of curious about this as well.
[57:27] So points from volume.
[57:29] Let's put this into a sculpt.
[57:33] Let's just try sculpt.
[57:35] Because if it will work in a sculpt, it will work in a ShotsCult.
[57:37] Yeah, it's not working.
[57:39] So my guess is that what you'd have to do is have a cage that actually represents the actual volume of your Gsplat.
[57:53] And then use a point to form to move those Gsplat points.
[57:59] Because I think at the moment we actually can't sculpt points.
[58:02] We can only sculpt geometry cages.
[58:04] So I think that's the way you'd want to do it.
[58:06] You want to create a cage from that Gsplat, sculpt that, and then just do a point to form to the Gsplat.
[58:19] And then third question from Carol is, is it even possible to migrate animation script from Maya to Houdini,
[58:25] create tutorials specifically for Maya animation script writers to show how it will work or what needs to happen in the Houdini environment?
[58:36] Basically migrating.
[58:38] And there's a couple of other people asking about the same sort of thing, like sort of bringing Maya animation into Houdini, MoCap into Houdini.
[58:44] Well yeah, MoCap is, I mean, my own personal biased opinion, I guess.
[58:50] MoCap and Houdini is a done deal.
[58:53] It's so good, it's so easy to use, and it's just endlessly flexible and customizable.
[58:59] And next week we're actually going to check out how that works.
[59:03] Now when it comes to migrating workflows and stuff like that, I think with animation,
[59:09] what we've been doing is just trying to get animation in Houdini to a point where it feels very familiar.
[59:18] And then on top of that, we're going to add some more tools, which we've already had.
[59:23] We can see that we have Ragdoll, we have secondary motion.
[59:26] So we have a lot of these new things as well as what people are familiar with.
[59:32] So the actual workflow of animating, reaching in and grabbing your controls, we're not trying to reinvent that too much.
[59:39] We want that to feel very familiar.
[59:41] But then on top of that, we're going to add some other stuff.
[59:45] So I think when it comes to studio workflows, there's this workflow of just adding a node.
[59:54] For instance, if I want a different character, I could use Elektra, which comes with Houdini.
[59:59] So any install you have Elektra, you can go ahead and start using her and animating with her.
[60:04] And then when it comes to scripting, I'm guessing by scripting you might be referring to rigging.
[60:11] With rigging, it's a bit different.
[60:14] We definitely have a different philosophy with rigging.
[60:18] But the overall philosophy of how parenting works, how matrices work, that's all readily available.
[60:27] And we're not shying away from that.
[60:30] That's all available to you guys.
[60:32] And you can really kind of create whatever you want.
[60:35] I would suggest checking out what Tumblehead has come up with in terms of, because they're all Maya veterans, right?
[60:42] And they've completely moved their pipeline over to Houdini.
[60:44] So check out Tumblehead and their tumble rig.
[60:48] So they've moved everything, they've migrated everything, and they're never looking back.
[60:52] So that's a really good example of what a studio can do.
[60:57] And what a smaller studio can build out with using these tools.
[61:03] We commissioned those guys to create Turbulence, the animated short that you might have seen with the kid in the airplane and being afraid of the turbulence.
[61:12] And they were basically the first ones to really jump onto KineFX and start pushing it and giving a lot of feedback to the R&D team along the way.
[61:21] And so they've been on there for a while.
[61:25] And so it's nice to see them releasing even more stuff.
[61:27] That frog that you might have seen in the Houdini 22 launch.
[61:31] Magnus will be coming over to Toronto for Houdini Hive Aquinox, which is on September 21st to 24th.
[61:37] He'll be coming over here to do a workshop on that frog.
[61:40] So if you want to come to Toronto, we'd love to see you.
[61:44] Yeah.
[61:46] What is the best format for importing, exporting animation into Houdini?
[61:52] FBX.
[61:57] Yeah, I'd say it's FBX.
[62:02] It's pretty straightforward.
[62:04] I mean, for instance, just like a little teaser for next week.
[62:09] So if I throw down a retarget recipe.
[62:12] So Apex Retarget to Rig.
[62:14] All right.
[62:15] So here's just this nice little retarget recipe that we're giving you guys.
[62:19] So recipes, recipes, recipes.
[62:21] Use them. They're awesome.
[62:22] We're giving you guys a bunch of them.
[62:24] And what this one does is it kind of just gives us Electra.
[62:28] Right.
[62:29] So this one is configured to Electra, but you can always change it to anybody else.
[62:33] Now, if I plug this in, you can see here that we have this FBX animation.
[62:39] OK.
[62:40] And typically when you're working with MoCap, it's typically done with FBX.
[62:44] That's sort of like the nice universal format.
[62:49] And here, you know, it's just these nice retargeting tools, which we're going to check out next week.
[62:55] And then here's everything just retargeted.
[62:58] And this is all coming from an FBX rig.
[63:02] So yes, I would definitely say FBX is the way to go.
[63:08] Great.
[63:09] Just a couple of requests for a rigging webinar.
[63:15] Why did Max use the MotionMixer Fetch at the end?
[63:18] Oh, yeah, that was to...
[63:22] So because I wanted to take what I made in the MotionMixer and put it back into Apex.
[63:29] And to do that properly, you got to take your MotionMixer, the output, and put that into the Fetch.
[63:36] Right. So you're kind of grabbing that output and outputting an Apex scene, which then allows you to go back into Apex.
[63:44] Yeah, because I wanted to add some more animation on top of that.
[63:50] Cool. Is it possible to use partial ragdoll to resolve collisions between characters?
[63:56] That's an interesting idea.
[63:58] I've definitely used...
[64:00] If you guys have seen Cedric, the ape, that was one of my guys.
[64:03] That was one of my characters.
[64:05] I rigged and animated him. I didn't mallow him.
[64:09] But I did use ragdoll for his armor.
[64:14] So like his tacit armor and his legs, that was all ragdoll.
[64:18] So that was all properly simulated and everything.
[64:21] So yeah, you could use it for ragdoll.
[64:23] So I suppose, yeah, you could use ragdoll for solving collisions or like intersections.
[64:33] I think that's all of the questions.
[64:41] Thanks to everybody who answered stuff along the way. That was really great.
[64:44] Yeah, thanks guys.
[64:45] Rob Garcia was all over it.
[64:47] Do you mind if I ask a question here?
[64:49] Yeah, of course.
[64:51] So I'm thinking about the things that I do normally that I want to do here.
[64:58] For example, grab and release objects.
[65:01] Do you have any tool already that for it?
[65:03] Like the anim bot, I use a lot the temp controls.
[65:07] I have a grab and release.
[65:09] I want to grab a prop and then let it go.
[65:13] I want the character.
[65:15] Do you have anything planned for that?
[65:17] Well, yeah, at the moment it's through constraints.
[65:22] So again, if we're going to use this kind of this prop idea,
[65:27] it's mostly done through constraints.
[65:29] So I don't think it's at the level of ease and use as anim bot is,
[65:37] but we're definitely planning on like we have some like that's kind of like the end goal with all this is to make it like insanely flexible and easy to use
[65:47] so that you can kind of just do whatever you want.
[65:49] Which is this idea of like where we really want to take all this is this idea of ephemeral rigging, right?
[65:57] Which anim bot is kind of approaching with their temp controls.
[66:04] And yeah, we're definitely kind of heading in that direction.
[66:09] And it's definitely something that we want to do.
[66:11] So in this case, we would do that with constraints.
[66:17] So like I can get my guy into place.
[66:19] Let's go back to my IK.
[66:21] And then I can just do this.
[66:25] I did the wrong way.
[66:26] All right, whatever.
[66:27] But then what I would do is I would keyframe this constraint.
[66:33] OK, so I would just keyframe that blend.
[66:37] But yeah, that's how you would do it in this case.
[66:40] But so it's like the traditional Maya one.
[66:43] So let's say if you wanted to change the constraint of that prop that you did from the hand to the waist.
[66:50] Imagine it's a gun and they are all stirring the gun.
[66:54] You just make two constraints and then you swap the you just turn one off and the other one on when you want to swap.
[67:01] Yeah, that's how it works at the moment.
[67:03] Yeah.
[67:04] OK, so that's the I guess the Maya way.
[67:07] Traditional without any bot.
[67:09] Yeah, it is the traditional Maya way.
[67:11] I mean, we like we've been working on this for three years, I think.
[67:15] And so it's it's but the but the goal is eventually to kind of create that foundation, which we've kind of set up.
[67:22] But now it's it's to get into like the real meaty stuff, which which is this kind of like ephemeral workflow and definitely getting to that point of what you're talking about.
[67:31] Right.
[67:32] Where it's just like just in time rigging.
[67:34] Like I just need that one thing and I need it now and then I'm done with it and I get rid of it.
[67:38] Is that it's that that's where we're heading with all this.
[67:41] Cool. Thanks.
[67:43] All right. Arturo says I have to use Maya and advanced skeleton to have the rig option for animation that I have to export as a limbic for CFX and Houdini.
[67:50] I'd like to know if I can transfer that into Apex.
[67:55] So like export in Olympic from Apex.
[67:58] You want to jump in Arturo?
[68:03] Maybe Arturo is no longer here.
[68:06] No, maybe.
[68:07] He's here.
[68:11] We'll come back to it.
[68:13] I think you'll hand already asked this question, but is there a kinfax animation workflow that works directly with Unreal Engine?
[68:21] Directly.
[68:23] I mean, the way you would you would do that is this.
[68:25] So it involves the scene in books.
[68:28] Or rather, maybe not the scene in book.
[68:30] I think you can actually do it unpack character.
[68:33] So unpack character.
[68:35] So this is really, really powerful.
[68:37] So what we get is we pretty much take our character and we unpack it, which gives us all everything we need to output in FBX.
[68:49] OK, so with this unpack character, I can go to the character name.
[68:54] Harry.
[68:55] Right.
[68:56] And so pretty much what I'm getting at is like this is how you jump out of Apex and you get your characters into a format that like a video game engine or Maya or something else can use.
[69:07] So with this unpack character, what we have is these four outputs.
[69:11] Right.
[69:12] We have one, two, three, four.
[69:13] The first one is just the actual Apex scene.
[69:16] It's everything within the Apex scene.
[69:18] And the second is our geo.
[69:22] The third is the rest scale.
[69:27] And the last is the animated scale.
[69:31] OK, now this is what you're going to want.
[69:34] Right. With your gaming engines.
[69:36] So to export to a gaming engine, you're going to want to use the FBX character output.
[69:43] So wrap FBX character output.
[69:46] So there's two required inputs.
[69:49] OK, it's the geo and the rest scale.
[69:52] And you can plug this in.
[69:55] Right.
[69:56] And this will give you that animated pose.
[69:58] But what you what you know, my preferred workflow with like working with Unreal or something is actually keeping the animation separate.
[70:05] Right. Like so I can kind of import as a clip.
[70:07] So what I would do is let me see.
[70:11] Animation output.
[70:13] Where was that?
[70:14] So FBX animation output.
[70:17] So here it is.
[70:19] Yeah. So this just is just a single FBX animation output.
[70:23] And that this is where that would go.
[70:25] OK. So then you just set your file.
[70:28] Right. Your file.
[70:29] Where that where that goes.
[70:31] And then from here you would just set like, you know, your your your frame range.
[70:38] OK. So like I want like from frame one to two fifty output output FBX file.
[70:45] All that good stuff.
[70:46] So this is this is sort of like the, you know, the video game export system here.
[70:54] So unpack your character.
[70:56] You have everything you need for for the video game engine or Maya or whatever.
[71:03] And then you output it that way.
[71:10] Arturo clarified the question, which is, is there a way to build a rig from Character Creator 5 inside of Houdini?
[71:16] I use Maya as a bridge for rig and animate, but I want to have it all inside of Houdini.
[71:20] And then Robert just replied, take a look at the rigging recipes.
[71:23] There were some demos here.
[71:25] Yeah. Yeah, actually. Yep.
[71:27] There is there actually is a recipe.
[71:30] Let me see. So FBX character.
[71:32] Character.
[71:33] It picks up its character import.
[71:37] There's a different one.
[71:38] It's biped. Yeah, here it is.
[71:42] So yeah, with this recipe, it kind of gives you everything that you need with Character Creator,
[71:49] because I've done Character Creator rigs a bunch of times and every time I do it, I always feel like I had to relearn it.
[71:55] But it has it's got a couple of caveats.
[71:58] For instance, the rest skeleton within a Character Creator skeleton is broken.
[72:04] Right. They have like floating joints, which doesn't the the the auto rig builder really does not like it.
[72:12] OK, so when you're working with a Character Creator skeleton, you want to use.
[72:18] Here, let me show you.
[72:20] So, OK, we get our FBX. Right.
[72:22] So this is the FBX import.
[72:25] OK, now everything we just expand this.
[72:28] So every node in Houdini that has to do with animated characters.
[72:35] Typically always has three inputs and three outputs.
[72:39] OK, three inputs, three outputs.
[72:40] So, for instance, the bone deform.
[72:44] OK, three inputs, three outputs.
[72:46] It packs on that character.
[72:47] It's the one that we just looked at before.
[72:49] Right.
[72:51] Let me see. Where is that?
[72:53] Those three inputs or three outputs.
[72:55] Right. And it always goes like this.
[72:57] So you can see that with this FBX character, it's the same thing.
[73:01] OK, it's the same thing.
[73:03] And essentially what that means is that we have, you know, as I said before, we have our geometry, our rest skeleton and our animated skeleton.
[73:12] Now, with something like Character Creator, you're going to want to use the animated skeleton.
[73:17] OK. And when you're outputting it, make sure that you're not outputting any animation.
[73:22] If you do, you can put down a time shift.
[73:25] All right.
[73:27] And just make sure that it stays on frame one.
[73:29] Like, because sometimes you might output like a, you know, your what's that called?
[73:34] The like the calisthenic kind of animation pass.
[73:38] And what this does is it freezes it on frame one.
[73:41] And then you plug that into your capture pose.
[73:44] And then from there, you work on your rig.
[73:47] Yeah. So, yeah, with Character Creator, it's best to
[73:50] to work on with that, with the animated skeleton, not the actual base skeleton.
[73:57] Here's another question. While exporting from Houdini to Unreal, can we make the joints orientation export as per Unreal?
[74:04] Maybe not without messing up your skinning.
[74:17] Right. Because if you if you change the orientations midway, all of your set, like since, you know, your your your geometry skin to a joint in a specific way, it'll kind of throw everything off.
[74:36] So, yeah, you don't want to change the orientations too much.
[74:41] So you need to make sure that before you skin your model, that the that the the joint orientations are matching what you want it to be down the road.
[74:52] Right. It's not good to change the joint orientations like joint orientations after that could really that can really kind of screw things up.
[75:01] Cool.
[75:03] We'll take maybe one more question and wrap it up. So if anybody wants to jump on, do it by audio, video or jump in the chat.
[75:12] Last question.
[75:17] Hey, guys. My question is only like regarding clothing.
[75:22] If I already have like a cloth made in model model designer, can I actually animate the outfit of the character with the apex or what format would I have to use to actually animate the outfit?
[75:45] I mean, so so the question. Sorry, you're cutting in and out a little bit.
[75:50] The question is basically, can I just import geometry from from Marvelous Designer and use that with an apex like for like an apex character?
[76:00] Yes, but more like vellum type of animation.
[76:05] Oh, sure. Yeah. So the vellum stuff will take place in the CFX process.
[76:10] Yes. So, you know, what you'd want to do is, you know, attach your geometry to your character.
[76:17] Of course, you know what you could do.
[76:20] Let's see. So let's say I already have a character.
[76:23] Okay. I have Electra. I just copy Electra over.
[76:27] And so we have an apex character.
[76:30] All right. So let's say you've like already rigged up your character. It's just like a base model.
[76:34] Right. So what you want to do is unpack your character.
[76:39] So apex unpack character. And now again, you know, I have that geometry.
[76:44] Okay. So now I have the geometry. I can go in here and do stuff with it.
[76:49] Now let's say that we have we've added some clothes right to Electra.
[76:54] So let's go like here. I'm going to press that split that add or delete.
[76:59] Add or delete. Let's get rid of everything.
[77:04] All right. Just to make sure that this is going to work.
[77:07] And then we'll do color. Make that red.
[77:10] All right. And let's see. I'm going to open this up.
[77:14] I know. Not red. Let's use blue because she's already red.
[77:18] And let's just peek this a little bit so we can actually see it.
[77:21] All right. And then go like that.
[77:24] Okay. Cool. So let's pretend that this is our garment.
[77:27] And we want to attach it to Electra.
[77:30] So Electra already has all of the skinning data.
[77:33] So if I go and look at her data. So I just went and pressed this I button.
[77:38] It's taking a long time to load up. Let's see if this works.
[77:42] Because I'm going off script here and things have been very good so far.
[77:45] Let's see if it continues. Okay. So now we have this point attribute in here.
[77:48] The bone capture attribute. Okay.
[77:51] So essentially what I want to do is I just want to take that bone capture attribute.
[77:55] It's sort of just like copy vertex or copy skinning in Maya or something like that.
[78:00] So now I just want to do attribute transfer.
[78:04] Okay. And I'm going to take that.
[78:08] And then this. And I'm going to want to get that bone capture attribute.
[78:13] Right. Not the parameter points.
[78:16] And then so now I have this. Okay.
[78:20] Now what I need to do is merge it back into the actual character.
[78:25] So now I have all that.
[78:28] And now I can just pack my character back up.
[78:32] Okay. That's going to be our right.
[78:36] This is the so I just made some like a bunch of changes to the actual geometry.
[78:41] And now I'm going to grab the apex scene. Right.
[78:44] And what this is going to do is it's going to give me my rig back.
[78:48] Because now it's just now there's just nothing in there.
[78:51] But once I plug this right this actual character scene.
[78:55] The character that goes into here it's going to give me my whole entire rig.
[79:00] Okay. And then you know then I go you know apex character and then apex scene animate.
[79:05] Yeah. So now I just so pretty much what I did was I now have my special garment whatever it is.
[79:10] And then I just do a attribute transfer to get the bone capture from here.
[79:15] So that's the quickest way to just get your clothes onto your character.
[79:20] And then from there you would you would use your scene invoke.
[79:25] Right. And split out the clothes and then you would do your whole CFX vellum process.
[79:30] Thank you.
[79:33] We have one final question that squeezed in from what would be the most quick way to get a simple one line rig IK work in apex.
[79:44] One line IK rig. Let's see.
[79:47] Let's say line.
[79:49] Right. So line. Where'd it go.
[79:53] So okay line is what it looks like. It's points. Right.
[79:57] So in kinfx everything is points.
[80:01] In Maya or in Houdini everything is points in Houdini.
[80:05] I want three points. Okay.
[80:07] I need to turn these into joints.
[80:10] So rig doctor.
[80:13] Okay. We're going to go down initialize transforms.
[80:16] So now we have some points and now these joints.
[80:20] Okay. I'm going to do attribute just tags.
[80:26] All right. We're going to add some tags to this.
[80:29] Number of entries. I say everything.
[80:32] Value arm.
[80:34] Okay.
[80:36] We're going to pack the character. Actually let's just use pack folder.
[80:41] All right. So we're going to pack the folder.
[80:43] Okay. We're going to put this into a format that apex understands.
[80:47] This is going to be base scale.
[80:51] Now we're going to start rigging.
[80:53] Autorig component.
[80:55] And we're going to go to the FK transform.
[80:58] Essentially what this does is it just kind of initializes your rig.
[81:03] Okay.
[81:05] So now I have just a really simple FK rig.
[81:09] All right. Let's jump out of that.
[81:11] Let's add one more.
[81:13] And we're going to use multi IK.
[81:17] Where is it? Multi IK. There it is.
[81:20] And now within the driven, we're going to put arm.
[81:24] Because that's the tag that we set up before. Arm.
[81:28] It's looking for these tags.
[81:31] And now I have my IK.
[81:35] Cool.
[81:37] Super cool.
[81:40] So many requests for a rigging webinar.
[81:43] So it looks like we're going to have to do a part three, four, and five of this series.
[81:47] But thanks everybody for coming. Thanks Max for taking us through that.
[81:50] Thanks everybody who helped answer questions along the way.
[81:53] Really appreciate it.
[81:55] We'll see you again soon. We'll post this on YouTube.
[81:58] You might get an email from Zoom that might give you the recording as well.
[82:02] But certainly we'll put it on our YouTube.
[82:04] So get it there.
[82:06] And the assets, as we said, are on the content library.
[82:09] So you can go follow up with those.
[82:11] And maybe we'll see you next week.
[82:13] Thanks everybody. Awesome. Thanks guys.



---

## Captured Frames

- [3:59] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_000.jpg
- [6:07] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_001.jpg
- [7:03] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_002.jpg
- [11:12] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_003.jpg
- [16:16] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_004.jpg
- [18:04] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_005.jpg
- [20:15] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_006.jpg
- [21:02] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_007.jpg
- [24:11] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_008.jpg
- [25:00] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_009.jpg
- [29:24] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_010.jpg
- [33:41] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_011.jpg
- [36:03] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_012.jpg
- [39:33] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_013.jpg
- [46:03] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_014.jpg
- [48:16] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_015.jpg
- [68:37] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_016.jpg
- [70:17] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_017.jpg
- [79:57] tutorials/frames/animate-in-kinefx-part-i-max-rose-2026-illume/frame_018.jpg

---

## Structured Notes

### Core Technique
Live-webinar tour of Houdini 22's KineFX character-animation workflow (Part 1 of a multi-part series) — Max Rose (SideFX in-house specialist) animates two pre-built rigs (a biped "Harry" and a spring-jointed "Jack-in-the-box") using Apex Scene Animate, covering pose-based keyframing, config/selection-set controls, ragdoll baking, shot sculpting, set-driven keys, secondary motion (spring), the Motion Mixer, and FBX export for game engines/Maya — closing with 20+ minutes of live Q&A.

### Summary
The webinar opens on Harry (a pre-rigged biped built with the Rig Builder) in **Apex Scene Animate**: click-drag posing, the gear icon's config controls (IK/FK toggle per limb), selection sets (create-from-selected or import a saved Apex Sets list), and the animation-slider tool for in-betweens/moving holds/overlap. Rather than animate live, Max drops in saved clips from the **Animation Catalog** (select all controls → Apply), showing that all animation data lives on a single Scene Animate node and can be freely duplicated. He then reworks a "waves and flies away" clip into "waves and gets yanked offscreen by ragdoll": enter the **Ragdoll substate** (press C), deactivate via selection-set + active toggle so the character doesn't collapse prematurely, tune **stiffness** (~25) for a controlled flop, re-blend IK/FK to 1 one frame before the ragdoll starts (avoids a visible snap once baked), add a **locator** substate near the foot with keyframed translate (Shift+T) as a target, and use a **tether constraint** (select foot control + locator, press H) to yank the ragdoll along that path. Ragdoll motion is baked to a new additive layer over a frame range (Settings → Bake → frame range → new layer → Bake Keys); eye RBD objects slamming shut is fixed by deleting those keys on a new "fix" layer. For cartoon squash-and-stretch not built into the rig, Max uses **Shot Sculpt** (world-space default recommended) — press B to enter, G for brush settings, 3 for the Move brush — to hand-sculpt a pose at a chosen frame, which auto-creates an in/out Bezier-interpolated sculpt track that can be stacked with more sculpts. Second half switches to a spring-jointed jack-in-the-box rig to demonstrate **Set-Driven Keys**: create two named animation layers (doll-close rest pose, box-open lid animation) inside an Apex Rig Pose node, then wire them into the Auto Rig component's Set-Driven-Key entries (layer name + frame range) so a single Apex Scene Animate slider scrubs each; a control's **Rotate X channel** can itself act as the driver (via Copy Current Selection → paste into the Driver field, then fit-range-remap so several physical crank rotations map to the 0-1 driven range). **Secondary Motion** (Pose Tools → Secondary Motion) attaches Spring behavior per-control — translate-only on the spring coil, rotation-only on the doll's other controls, tuned via an Effect strength slider (values like 4 shown) and keyed on/off — then baked to an additive layer just like ragdoll (watch for double-application if a control still has secondary motion attached from a prior state). Two clips on one Scene Animate node (Animation tab → New Clip) get combined via the **Motion Mixer**: drag clips onto its timeline, blend/crossfade between them, then switch the Mixer's output mode to "Apex Scene" and use a **Motion Mixer Fetch** node to pull the blended result back into Apex for further editing (e.g. fixing geometry penetration on a new layer). Bonus mini-demos from Q&A: adding **props** (Apex Add Prop / Scene Add Prop) and parenting them to a foot IK control (child→parent order, press H) for e.g. high heels; unpacking/repacking a character (Unpack Character → edit geometry → Pack) to hot-swap geometry without losing animation; transferring clothing skinning via **Attribute Transfer** of the `bonecapture` attribute from an already-skinned character onto new garment geometry; exporting via **Unpack Character → FBX Character Output** (geo + rest scale required) for a static/posed FBX, or **FBX Animation Output** for a separate animation-only FBX (Max's preferred game-engine workflow — keep geometry and animation as separate FBX files); a Character-Creator-5 import caveat (broken/floating rest-skeleton joints — use the **FBX Character** recipe and the *animated* skeleton, not the base rest skeleton, and freeze via Time Shift before Capture Pose); and building a minimal one-line IK rig from raw points using **Rig Doctor → Initialize Transforms** (points to joints) → **Attribute Tags** (tag joints e.g. "arm") → Pack Folder → **Auto Rig component (FK Transform)** → **Multi IK** (driven by the same tag).

### Key Steps
1. **Pose/animate basics** [frame_000, 3:59] — `Scene Add Character` + `Scene Animate` on a rig node; press P for the parameters window and enable click-drag posing; the gear/config control per limb toggles IK↔FK [frame_001, 6:07]; selection sets (create-from-selected, or import a saved `Apex Sets` list) group controls for fast show/hide [frame_002, 7:03]; animation-slider tool adds in-betweens, moving holds, and overlap on top of two hand-set key poses.
2. **Reuse saved clips** [frame_003, 11:12] — Animation Catalog → select all controls → Apply drops in a pre-made animation; all animation data lives on the single Scene Animate node, so duplicating the node duplicates the whole performance (useful for iterating variations without new files).
3. **Ragdoll exit** [frame_004, 16:16] → [frame_005, 18:04] — enter Ragdoll substate (C); use a selection set + Active toggle to keep the ragdoll inert until the desired frame; tune Stiffness (~25); one frame before ragdoll engages, blend the limb's IK/FK config back to 1 so the post-bake transition doesn't visibly snap.
4. **Locator + tether pull** [frame_006, 20:15] — add a Locator substate near the target body part, keyframe its translate (Shift+T) as the pull path; in Ragdoll, select the body control + locator and press H to create a Tether Constraint (locators driving ragdoll must NOT be set Active).
5. **Bake ragdoll** [frame_007, 21:02] — select all ragdoll controls → Settings → Bake → set frame range → Additive/new layer → Bake Keys; clean up side effects (e.g. delete unwanted eye-RBD keyframes) on a separate "fix" layer.
6. **Shot Sculpt for squash/stretch** [frame_008, 24:11] → [frame_009, 25:00] — set Shot Sculpt defaults to World Space; route the Apex character through a Scene Invoke (unpacks it to real geometry) before sculpting; press B to enter the sculpt state, G for brush settings, 3 for the Move brush; each sculpt stroke auto-creates a Bezier in/out track, and multiple sculpts stack.
7. **Set-Driven Keys** [frame_010, 29:24] → [frame_011, 33:41] — build named animation layers in an Apex Rig Pose node (e.g. `doll close`, `box open`) with their own frame ranges; register each as an entry (layer name + start/end frame) on the Auto Rig component's Set-Driven-Key list; the component then exposes one slider per entry to scrub that sub-animation independently.
8. **Control-driven SDK** [frame_012, 36:03] — with a driving control selected, use "current selection" → Copy → paste into the Driver field to avoid hand-typing control paths; pick the driving channel (e.g. Rotate X); since raw rotation may span many turns, sample two rotation values and plug them into Fit Min/Fit Max so several physical rotations remap cleanly to the SDK's 0-1 range.
9. **Secondary Motion (spring)** [frame_013, 39:33] — Pose Tools → Secondary Motion; controls needing motion turn gray, gold once attached; choose Spring, pick Translate or Rotate channel to affect, tune the Effect strength slider; bake to a new additive layer (same recipe as ragdoll baking); remove secondary motion from a control before reapplying it in a new pass to avoid doubling up.
10. **Combine clips in Motion Mixer** [frame_014, 46:03] → [frame_015, 48:16] — author extra takes as additional clips on one Scene Animate node (Animation tab → New Clip); drop a Motion Mixer, drag clips onto its sequencer timeline to order/blend them; switch the Mixer's output mode to Apex Scene, then use a Motion Mixer Fetch node to pull the blended result back into an Apex Scene → Scene Animate for further hand-editing.
11. **Character/animation export** [frame_016, 68:37] → [frame_017, 70:17] — Unpack Character exposes 4 outputs (Apex scene, geo, rest scale, animated scale); feed geo + rest scale into **FBX Character Output** for a posed static export, or use a standalone **FBX Animation Output** node (set file path + frame range) to export just the animation clip — Max's preferred pattern for game-engine work (Unreal) is separate geometry and animation FBX files rather than one combined export.
12. **Minimal one-line IK rig** [frame_018, 79:57] — start from raw points (e.g. a 3-point line); Rig Doctor → Initialize Transforms converts points to joints; Attribute Tags assigns a group tag (e.g. `arm`); Pack Folder formats it for Apex; Auto Rig component set to FK Transform initializes a basic FK rig; add a Multi IK component with its Driven field set to the same tag to get working IK off nothing but tagged points.

### Houdini Nodes / VEX / Settings
- **Character/animation nodes:** Scene Add Character, Scene Animate, Apex Sets (selection-set import), Animation Catalog, Apex Rig Pose (rest pose / set-driven-key source layers), Auto Rig component (FK Transform, Multi IK, Set-Driven-Key entries), Rig Doctor (Initialize Transforms), Attribute Tags, Pack Folder / Pack Character / Unpack Character.
- **Secondary/dynamics nodes:** Ragdoll substate (Active toggle, Stiffness, Bake to layer), Locator substate (Shift+T translate key, Shift+R rotate key; must be inactive when driving a tether), Tether Constraint (H shortcut on selected controls), Secondary Motion / Spring (per-control Translate or Rotate target, Effect strength, bake-to-layer).
- **Sculpt/finishing:** Shot Sculpt (World Space default, Move brush = shortcut 3, per-stroke Bezier in/out tracks), Attribute Transfer (for copying a `bonecapture` skin attribute onto new garment geometry), Motion Mixer + Motion Mixer Fetch (Apex Scene output mode to round-trip a blended performance back into Apex).
- **Export nodes:** FBX Character Output (requires geo + rest scale inputs), FBX Animation Output (separate animation-only FBX, with its own frame-range/file settings), FBX Character recipe (Character-Creator-5 import — use the *animated* skeleton, not the broken rest skeleton, and freeze with a Time Shift before Capture Pose).
- **Rig used:** "Harry" (biped, `harry_rig_v2`/`v4`, built with the Rig Builder — companion asset to [[rig-builder-project-overview]] / the Rig Builder episode series) and a custom spring-jointed "Jack-in-the-box" rig (3-point spline spring + FK body).
- No raw VEX authored on-screen — this is a Scene-Animate/Apex UI workflow session, not a scripting one.

### Difficulty
Intermediate — assumes comfort with basic KineFX/Apex posing already; ragdoll baking, set-driven keys, secondary motion, and the Motion Mixer round-trip are all shown as guided step-by-step workflows rather than assumed prior knowledge.

### Houdini Version
Houdini 22 (KineFX/Apex animation toolset; presenter references "Houdini 22 launch" and the upcoming Houdini Hive Anoxia/Toronto event).

### Tags
kinefx, apex, animation, rigging, rbd, secondary-motion, spring, procedural, fbx, intermediate, houdini-22

---

## Related Tutorials
- `tutorials/h22---kinefx-rigging-and-animation-max-rose-houdini-22-hive.md` — companion piece by the same presenter (Max Rose) building the *rigging* side of this exact jack-in-the-box spring rig (spiral-joint centerline trick, Configure Ragdoll recipe, SDK setup) that this video then animates; watch together.
- `tutorials/rig-builder-project-overview.md` — shows how the "Harry"/iBot-style biped rig used for the animation-basics section of this video was originally modeled, textured, and skinned via the Rig Builder pipeline.
- `tutorials/experimental-motion---chops.md` — alternate (CHOPs-based) approach to secondary motion / spring / jiggle, useful contrast to the Apex Secondary-Motion tool shown here.
- `tutorials/houdini-20-how-to-pose-and-animate-electra.md` — another beginner-friendly Apex pose/animate walkthrough on a different pre-built character (Electra), good companion for reinforcing the Scene-Animate basics covered in Key Step 1.
