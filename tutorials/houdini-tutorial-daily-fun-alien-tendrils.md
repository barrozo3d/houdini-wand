---
title: Houdini Tutorial // Daily Fun / Alien Tendrils
source: YouTube
url: https://www.youtube.com/watch?v=XLiXackQH_k
author: Tim van Helsdingen
ingested: 2026-07-16
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tutorial-daily-fun-alien-tendrils/
frame_count: 0
frame_status: pending-selection
---

# Houdini Tutorial // Daily Fun / Alien Tendrils

**Source:** [YouTube](https://www.youtube.com/watch?v=XLiXackQH_k)
**Author:** Tim van Helsdingen
**Duration:** 37m24s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tutorial-daily-fun-alien-tendrils <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Alright everybody, so yeah I've been a while enough done any videos but I thought this
[0:10] might be sort of fun thing.
[0:12] So the reason I haven't been doing a lot of videos is like I've been mostly been focusing
[0:17] on learning new stuff myself in my free time, I've been learning in real-engine and I'm
[0:21] making a game.
[0:22] Which has been interesting and I am planning to do some sort of like a devlog thing now
[0:28] that have come closer to actually implementing some stuff in there that actually worked.
[0:35] But for the day I thought it might be fun to do a video about this thing.
[0:38] So I just did a sort of essentially just a daily render so I made a daily still render
[0:45] because so my girlfriend is gonna, so we're gonna go to a thing soon where she was gonna
[0:51] sell some prints over her work and I was gonna go with her and I figured well if I'm gonna
[0:55] go there anyway I might as well so maybe put some of my own prints on so I decided
[1:01] to also maybe do one or two prints of my own so I figured I would make something for
[1:07] getting it printed and just putting it there and then I thought it would be cool to do
[1:11] like a QR code in the background and then people could scan it and I could go to the
[1:14] animation.
[1:15] So essentially this was just a daily render thing that I made.
[1:23] And I thought I thought it looked pretty good quite a simple scene but I thought it might
[1:27] be fun to do a little video about how I made it.
[1:31] You can download the source files as all of my projects.
[1:35] You can download the source files on my Patreon.
[1:39] So yeah let's just dive into sort of how I made this.
[1:42] So we're gonna go jump back and forth between sort of the composite here and the render.
[1:50] Actually fun fact is that as you can see the render here looks quite different from the
[1:53] composite.
[1:54] Actually it was meant to look a lot more like the composite but I was stupid enough
[1:59] like I had an HDRI in here in the light down.
[2:02] However I actually used dollar to rip in there and then I submitted it to deadline with
[2:07] submit.
[2:08] And I always tell people not to do that and then I go and do it myself.
[2:13] So what I actually what how should have looked in the render was like this.
[2:19] She's already like a lot closer to what I ended up just faking in the composite but I
[2:25] didn't want to re-render because it's quite a slow render because of the depth of field
[2:29] and the sort of the random walks of service scattering that's going on.
[2:33] Yeah essentially this is what you would need this would need to be dollar job.
[2:40] Yeah just walk through the scene it's quite a simple scene but I think maybe it might
[2:44] still be interesting for some people to see how this was done essentially.
[2:48] So you can see here we have a 10 roll folder which has all of the tendrils you can see
[2:53] it's essentially a couple of patches.
[2:56] I could have just made more tendrils altogether but I just I made the one patch look nice
[3:00] and I just decided to sort of instance those in the scene so essentially you just have
[3:05] to one patch here.
[3:06] We'll go into this in a little bit and then you just put in the instance you put it in
[3:12] fastpoint, instance scene and then you can just place it somewhere in your scene and
[3:16] we'll just instance whatever it is here with all of these settings.
[3:20] So let's just dive in there.
[3:22] So we start off with a grid, I don't know if my light here, start off with a grid, adding
[3:30] a little bit of detail there with the mountains and so up and then scattering some points on
[3:33] it.
[3:34] You can see I'm doing two different scatters so just relax iterations here and then with
[3:40] a lot more points and also still with relaxed iterations we get a nice uniformed-based
[3:47] thing.
[3:48] We're randomizing this piece kill here.
[3:52] The left ones here are a little bit bigger than the right ones, those are a little bit smaller.
[3:55] Then we copy these lines to it and we do the same over here on the right.
[4:00] You can see we get a bottom patch to fill it in and the top patch which are the larger
[4:07] ones.
[4:08] So essentially the larger ones and then you have the bottom ones on the bottom there,
[4:13] which would look quite nice.
[4:14] And there's actually no simulation here, similar to like I like working with noises quite
[4:19] a lot, I like to do a lot of the soaps and so essentially what it is here is I have a
[4:27] have a have a have a have a move this over to the side a little bit.
[4:32] So I'm just grabbing a curl noise, in grabbing the position, adding the curl noise to the
[4:36] position.
[4:37] So we just get some noise there and I have a curve view here.
[4:40] So on the on the line here I'm putting a resample to add some more points.
[4:46] You see here you can add some more points with a resample and I output a curve view attribute.
[4:51] A curve view attribute if you watch how the new one and one you know all about this because
[4:54] this is essentially well I like I do this a lot anyway.
[4:59] But so you get an attribute across your curve from zero to one.
[5:03] So zero to one or zero to one.
[5:04] I don't know what it how it is doing it on this one, particularly, but you can use that
[5:08] in a ramp.
[5:09] So you can bind it in put it in a ramp and you can get some control over sort of sort
[5:17] of where you want the noise to appear.
[5:19] So you can see now it I can sort of not have it appear in the bottom because of course
[5:23] it needs to be stuck to to the bottom part, right?
[5:26] So because if I just had it like this would sort of move everywhere, which you don't necessarily
[5:32] want.
[5:33] So just put it in there and multiply your amplitude by that ramp noise and you put it in the
[5:41] add here and then just put it in position and you get this sort of this nice wave you
[5:44] pattern.
[5:45] And then in your offset you can just animate it.
[5:48] You can innovate with a curve or you could put something like a dollar T in there and
[5:55] it would also animate.
[5:56] I did it with a curve but doesn't necessarily matter how you do it.
[6:02] Animated, but you can see if you just play through it, you can see sort of a nice wave
[6:05] you pattern.
[6:06] And then I'm just I'm smoothing those out a little bit.
[6:09] I could have maybe added a little bit more points to each of one of those, but I didn't
[6:13] want my final curves to end up with too much geometry either.
[6:16] So I decided to not have that much going on there because this is already on the right
[6:22] here.
[6:23] So I want 30,000 points.
[6:24] This is not too much.
[6:25] So there's multiple ways you can render this.
[6:28] You can see here is with the bottom patch as well.
[6:30] You can see it is nice sort of wave you pattern going on.
[6:32] Looks quite nice.
[6:33] Also on the top.
[6:34] Multiplaced render this.
[6:36] You could sweep those and just actually create geometry.
[6:39] So if you put sweep here, put it to a round tube.
[6:42] You can get some round tubes.
[6:44] You can put it to end caps to red.
[6:48] And you will get sort of this top part and you get sort of these things.
[6:52] And you could if you were to do that on sort of the entire thing, you could see we
[6:59] get.
[7:02] We get some stuff there, which is quite nice, but it's a little heavy 1.3 million points.
[7:07] You could of course turn this down and would be a little bit less heavy.
[7:11] So I didn't end up rendering it like that.
[7:13] I ended up rendering it as a redshift curves because it was rendered in redshift.
[7:17] So you can just go to your redshift.
[7:19] So to get your geometry now, redshift tab strands and you can turn render object as strands.
[7:23] And essentially, just going to give you the same result as you can see here in the render
[7:26] also with sort of the top part.
[7:31] So you have the default skill and global skill multiplier.
[7:33] Essentially, this will also pick up on p-scale.
[7:37] You can see you can also ignore p-scale if you want.
[7:39] So that's why we have p-scale here as well to sort of control the thickness.
[7:44] So 1.5.
[7:45] So this is going to be half as thick.
[7:48] And then redshift will just generate these shapes on the mount.
[7:53] I have a desolation quite low because I didn't want it to be too memory hungry.
[7:59] Strands in redshift are not super efficient.
[8:01] They're quite slow actually.
[8:04] But this did give me a little bit better result than just sweeping it and instinct and
[8:08] singing it like that.
[8:10] Because now I think it could still use the screen space adaptive even if it's instance.
[8:15] I'm not completely sure.
[8:17] But I think that should work if it doesn't.
[8:21] So yeah, that's continue.
[8:26] So I also have some particles going on here.


### Particles [8:27]
**Transcript (timestamped):**
[8:29] It's quite a simple thing.
[8:30] So you just have these.
[8:31] Let's have a look at them in the composites.
[8:33] You can actually see what they're doing.
[8:36] So here we have this.
[8:39] All right.
[8:42] Doesn't seem to really want to.
[8:46] All right, there we go.
[8:50] As you can see, it's just essentially just sort of floaty particles, which always just
[8:54] looks quite nice.
[8:58] And some weird thing popping in there.
[9:00] I think that probably was still in memory.
[9:03] So essentially what we're doing here is to just have a box made of VDB from it.
[9:06] It's gathering some points in it.
[9:09] Global seed, dollar T. So you can see it changes.
[9:11] It's going to change every frame.
[9:14] Then the pop network not doing anything too interesting.
[9:17] We just have two noises here.
[9:19] Just sort of move these about.
[9:21] So you can see it's just end.
[9:25] These pop forces also use curl noise.
[9:29] If I'm correct, so it's similar to the noise we were using for you.
[9:32] You can see here if you can dive into it.
[9:34] You can see it actually uses curl noise.
[9:37] So if you didn't know, pop forces are based on curl noise.
[9:41] You can see that it's sort of a nice look with one bear noise and one slightly smaller
[9:47] noise.
[9:48] So just caching that out.
[9:54] Then we're time blending it to make it a little bit slower.
[9:57] Make sure that you use point ID for that.
[9:59] So else is going to pop in and out.
[10:03] Setting some P skills here.
[10:04] Again, seed attribute on ID.
[10:06] Also, if you're going to get jittering, I can show you what it looks like if you want.
[10:11] You can just boot, just put a sphere on it.
[10:18] I should turn on back.
[10:20] Okay, this might crash because I've got to turn up.
[10:22] All right, back in instance.
[10:25] All right, so now this looks fine.
[10:27] If I were to turn off seed ID, you can see it's going to change the scale every frame.
[10:36] So every point has a unique ID.
[10:39] So if you turn this on, it will sort of do the randomized piece scale by the ID, which
[10:45] is unique.
[10:46] If you don't do it, it's going to do it by the point number.
[10:48] But of course, we're sourcing points every frame.
[10:50] So the point number is going to change.
[10:54] So what I did here is kind of redundant.
[10:58] So I'm actually copying disks to it, which I put a texture on it of a little smog puff.
[11:08] So essentially what I have here is I've loaded in the point from the camera.
[11:16] You cannot really see it, but like there's inside of a camera, if you go inside of a camera,
[11:24] you can see it's even pointing to the wrong camera.
[11:27] There was a very quick sort of fun project, like I mentioned.
[11:30] I did this in a couple of hours.
[11:31] So there's a couple of weird things all over the place.
[11:35] So it's not.
[11:36] I mean, it's actually grabbed the correct one.
[11:38] So it's actually correct for the tutorial file.
[11:41] Oh, there we go.
[11:43] So essentially what I'm doing here is I'm just looking through the camera now.
[11:50] I'm grabbing the position of the point inside the camera.
[11:53] And then I am riding out a normal.
[11:57] It's essentially just normalizing sort of the, some subtracting the camera position to
[12:07] the current position.
[12:09] And essentially get a, let's see if it's actually once visualized normal visualization.
[12:16] Oh, you can see it here.
[12:17] So it sort of points to the road to the camera or away from it right now.
[12:21] I'm not sure.
[12:22] You can infer it if you want.
[12:23] And then what you would get is, if I increase the scale, we'd essentially just get these
[12:29] things that are sort of always facing the camera.
[12:34] Essentially.
[12:37] I kind of undone that by just enabling a orient, which kind of I'm randomizing that.
[12:44] So you could, you could disable this and doesn't necessarily do anything because I rendered
[12:50] it like that.
[12:51] Just a little bit too uniform side.
[12:52] Essentially just got rid of it.
[12:55] And then I'm doing it with the, with this and just bising it toward the direction.
[13:00] It just ended up looking nicer like this if it wasn't completely facing the camera.
[13:04] As you can see, if you get close, you can actually see.
[13:10] I'm sort of, move like that.
[13:13] I'm not even sure if the smoke puff was actually correctly applied here.
[13:16] She can actually see the angle.
[13:17] Again, this is very quick sort of, it just looked nice and then I rendered it.
[13:22] Yeah, I'm just off saying the time here.
[13:25] So it actually starts sort of a little bit into it.
[13:29] And then here, cleaning a float.
[13:33] So from age, so based on the age between zero and life.
[13:37] So life is essentially when the age meets life, it's going to kill off the particle in
[13:41] the solver.
[13:42] So if you fit age between zero and life, you're going to get, you can fit it together
[13:47] as zero to one attribute.
[13:49] And you can use that with a ramp to do some alpha ramping.
[13:53] So you can sort of, you don't see it because there's stuff copied towards it.
[13:56] Essentially, you can fade in and out these particles.
[13:58] So you just get these particles there.
[14:02] So that's essentially everything for the geometry stuff.
[14:04] Let's talk a little bit about some of the materials.


### Materials [14:05]
**Transcript (timestamped):**
[14:06] So let's go into retro material.
[14:08] Tendril.
[14:09] So it's a very basic material.
[14:11] I first, I also experimented with some noises, but I kind of liked the, just a sort of uniform
[14:19] look.
[14:20] It kind of, when I started adding some displacement or noises, it kind of didn't look as nice.
[14:26] The material itself is quite basic.
[14:27] So nothing would base color just to uniform gray.
[14:32] Just stounder, just reflective, a little bit of roughness, a little bit of transmissions.
[14:37] We actually get some refraction through this.
[14:40] Aside from that, it didn't really do much with it, but a lot of the color comes from
[14:44] the subsurface.


### Random Walk Subsurface Scattering [14:45]
**Transcript (timestamped):**
[14:45] So actually have random walk subsurface gathering right now, which is actually quite new.
[14:49] It's got introduced like a couple of builds ago in Redshift.
[14:53] So first you had point based and Ray Trash diffusion.
[14:56] Random walk is sort of a, is an algorithm to get much relies on looking and much more accurate
[15:01] subsurface gathering.
[15:02] It's not necessarily the fastest, but it does look quite nice.
[15:06] A point based essentially where it just scatters points inside to your curves and then
[15:10] it just blurstes out to sort of fake the cross takes.
[15:13] Ray Trash was sort of another algorithm to actually rate raise the crossings and random
[15:19] walk.
[15:20] You should just Google what it is.
[15:22] I'll, like if you just Google and find some articles about what random walk is, you
[15:26] will probably get a much better explanation.
[15:27] And I will give you right now, but the random walk is also the default now, because it's
[15:32] a more modern way of doing subsurface gathering.
[15:34] It looks nice.
[15:38] So yeah, that's just the material.
[15:40] About to find out there's not really it all going on here.
[15:42] It's a very basic material.
[15:46] So yeah, particles, essentially the particles is loading in the alpha attribute that we created
[15:52] over here.
[15:53] So we can sort of fade out the opacity.
[15:55] So I'm just popping out the opacity here and then multiplying it by the alpha.
[16:00] So we still have some control here in this material sort of with the alpha color.
[16:09] And then we just multiplying it here.
[16:11] So we can fade it out.
[16:12] I put a sprite here, putting as a text buff, the shoot work, but oh, again, it doesn't
[16:22] didn't work because he's doing like it again, like a shoot.
[16:26] Like always when I do the bigger project and I use my dollar root setup and with the dollar
[16:30] root works, but over here, just I guess I made it.
[16:32] I messed it up with using dollar hip and I, it's because I first I was just rendering.
[16:38] I started this in 19.500.
[16:39] It didn't have deadline working for 19.5.
[16:42] So I figured all right, I'm going to render everything locally.
[16:45] So it doesn't matter if I use dollar hip and I ended up using deadline anyway, because
[16:51] I also wanted to use because the random times were a little bit slow.
[16:53] So I wanted to use my other machine, a surrender as well.
[16:56] So I ended up still using deadline and then this messed that up.
[16:59] So that's why this, this doesn't have the smoke buff applied, but again, they're very
[17:07] small.
[17:08] You don't necessarily see it.
[17:09] It still looks nice.
[17:11] So yeah, I mean, lots of mistakes here, but again, this was just a daily render.
[17:14] So it doesn't really matter in this case.
[17:19] There's a classic pattern here.
[17:20] It's essentially a pattern here in the bottom, which is applied to a grid here on top,
[17:27] which is this thing.
[17:28] It's mainly for the volumetrics.
[17:32] I can show you what the thing looks like.
[17:35] Let's go to out.
[17:37] Let's turn on.
[17:38] Let's switch the camera.
[17:39] Maybe move this a little bit closer.
[17:43] No, I don't want to make it else system.
[17:46] Let's press render.
[17:48] And I had a mission.
[17:52] Wait, so this should be off by default.
[17:55] I had it turned on for the, for previous take that I did.
[18:00] So as you can see here, just using the cost takes finger.
[18:04] And essentially what I'm using is for any, I think something here went wrong with also
[18:08] with the final render.


### Volumetrics [18:09]
**Transcript (timestamped):**
[18:09] How we use this with the volumetrics.
[18:12] But just walk through this.
[18:14] So in the render view, there's a different pulse here for volumetrics.
[18:21] And I might even, I think I should have used this thing.
[18:34] Yeah, right.
[18:37] So I think that you would, because of the diffusion, don't really see that much to be honest.
[18:43] So I put it there to get a little bit more of a gotray look, which I guess didn't really
[18:58] end up doing that much.
[18:59] But essentially, if you just put something like there to sort of block your light, you can
[19:05] sort of use it to get a little bit more control over to get like some nice gotrays.
[19:12] You can see here is not necessarily doing that much, but for the volume.
[19:15] So I'm rendered those separately.
[19:17] As you can see here, let me just put this to back to what it was before.
[19:25] But I am rendering this sort of a, so I'm essentially matting out all of the objects.
[19:30] Have a no here is controls the mat.
[19:35] And then you have here in your, I mean, I rendered this without any posts.
[19:41] Should be like that.
[19:42] And you just have your volume scatter here, which you can sort of control a lot of the
[19:47] stuff.
[19:48] So if you.
[19:50] And it's not necessarily being the fastest right now.
[19:53] Maybe because I'm recording.
[19:54] You see, you can control your scattering there.
[19:57] And this is probably just better to render separately, because you can have still have
[20:05] some controls to work with this in compositing, which I have here.
[20:10] So you see here's my volume render.
[20:14] You see I'm still doing some great on it.
[20:17] And now it's getting really slow, because I'm still doing functions.
[20:22] All right, let me turn off the IPR here.
[20:24] I'm not sure why it's, I think it's because I'm recording it's a thing of right now.
[20:29] You can see here.
[20:30] So you still have some control over what you want to do with your volume metrics.
[20:35] You see, I can still sort of fade the meaning composites.
[20:39] That's kind of a thing that you.
[20:41] Like I like to do, even with simple sort of daily renders like this, it's just nicer
[20:46] to have those controls and having to re-render the entire scene and the side.
[20:50] Or I want a little bit less intense volume metrics.
[20:55] So yeah, that's how that's that set up.
[20:57] For example, particles, not too difficult either.
[21:04] As you can see now I am actually getting the smoke buff.
[21:13] So this is what it was supposed to look like.
[21:18] But I mean, it still still looks decent.
[21:21] I might actually before I upload this tutorial, I might just re because this was pretty fast.
[21:25] I'll just re-render it and just actually company.
[21:27] So maybe the final thing will actually have the smoke buff.
[21:31] Who knows.
[21:32] But yeah, you can see this looks quite nice.
[21:36] And you get sort of sort of the, from the light here, you get sort of the color.
[21:42] For particles like this, if you're going to also do the, I rendered the depth of field
[21:46] into this as well.
[21:47] I did it everywhere.
[21:48] Just a lot of max samples.
[21:49] Like I tried doing the depth of field and compositing.
[21:52] And just ended up looking better by rendering it into the render.
[21:57] Well, I sent like with the stuff, it really depends on what you're doing for this stuff
[22:03] because it was a personal project daily render does like you.
[22:07] I didn't necessarily care too much for keeping the control.
[22:11] Normally on a client project, you would want to keep depth of field in compositing as much
[22:15] as you can because.
[22:18] But if you didn't know, you probably do, but you can do depth of field in compositing actually.
[22:26] Essentially you will, if you have that, you can just pick and choose your focal plane
[22:30] in compositing.
[22:31] And of course, if you have a client project, it's going to be easier if the client decides
[22:34] want a little more, you have to feel a little bit less.
[22:37] Just better to have controls there.
[22:39] Anyway, with the particles, make sure you do a lot of samples because they're small.
[22:43] So if you don't do that, they're not going to pick up.
[22:46] So I'm going to do something like this.
[22:48] It's just it's not going to sample properly.
[22:53] Actually, not too bad here.
[23:03] You can see it's still like it's really fast.
[23:07] So even if I crank up the samples, still, it's still relatively fast.
[23:13] You get just a little bit crisper.
[23:17] I guess here in this case, you can see it's a little bit nicer.
[23:22] So this doesn't necessarily matter that much here, but generally you want to sample your
[23:26] particles quite high, especially if you want to get some passes from it.
[23:33] Because you can see here, if you have a very low sort of pass here, your passes are going
[23:42] to look terrible, which would look better if you just do more samples.
[23:50] Aside from that, there's just the glow light here.
[23:52] Essentially, this moves up.
[23:54] Nothing too interesting there.
[23:55] I did a little bit of a flicker.
[23:56] I did that in compositing.
[23:59] Aside from that, nothing too interesting.
[24:02] Make sure you have controls here over volume.
[24:05] Make sure that's on.
[24:07] However, hard you want it.
[24:11] Essentially, here I have the light, but the color is...
[24:14] Like I mentioned, the color is not super visible in the volume render.
[24:18] That's it for the focus.
[24:21] What I do is you can put the script, V-Length, V2 origin from the origin of the camera,
[24:29] essentially, to the focus target, which is this one.
[24:33] This is essentially where the focus for the render would be, which is essentially with
[24:36] center, and then put focus target.
[24:39] Then it will focus on that specific part of the image.
[24:44] Still don't necessarily know why.
[24:47] Who didn't even just have a thing that you can drag in and it will do that by default.
[24:50] It would be nice to have something for that.
[24:53] This works just...
[24:55] I like a lot of times where I just miss type this and it doesn't work.
[25:00] I just put the thing I tapped in Google, and then who come up with the correct thing.
[25:04] I'm not sure.
[25:05] I keep messing that up all the time.
[25:07] It works.
[25:08] Yes, so do any part.
[25:10] Let's quickly run through the composite as well.
[25:14] Essentially, this is how we start out.
[25:17] Do a little bit of color correction here, and just brighten it up.
[25:22] You can see I have the post effects rendered into here.
[25:25] If you want to separate your post effect from the image and have it as a V, I didn't
[25:32] have that here, but what you would do is you would add another AV, put this to beauty.
[25:41] Then you would get this would be a beauty without post effects.
[25:45] And you could essentially subtract the pretty with post effects from the other one and then
[25:54] you would essentially...
[25:55] Yeah, so the post effects and subtract the regular one from it, then you would get a post
[26:01] effects AV.
[26:02] Or you could rebuild your entire scene here with your AVs and you could do the same.
[26:10] Which will not always work because I rendered this with denoising into the denoising because
[26:15] the alt is the denoise was giving me quite nice results.
[26:18] Let me see where I was.
[26:21] Forget where that is being turned on in Redshift because I don't necessarily use it that much.
[26:29] Alright, who did he suddenly crash out of nowhere?
[26:34] Anyway, let me have a look at where this thing is located again.
[26:38] And there we go.
[26:43] So it's under the Redshift.
[26:45] Oh, by the way, I always use advanced settings for my...
[26:48] I don't like the basic because the auto sample is just generally a lot slower than anything
[26:53] I can just put myself.
[26:55] So I use auto single pass.
[26:58] It gave a quite a nice denoised result.
[27:05] Because especially in this subservice gathering, I had quite a lot of sort of fireflies
[27:10] and just overall not looking great.
[27:12] And alt is essentially cleaned that up better than doing it myself and compulsing.
[27:18] So that's why I ended up using that.
[27:22] So yeah, the render is already quite nice.
[27:26] It looks quite nice.
[27:28] You see, there's a little bit of denoising artifacting here.
[27:32] But because we're sort of a underwater alien type thing, I guess.
[27:38] It's not necessarily annoying.
[27:42] You can see a little bit of jittering here because of the smoothing.
[27:44] I should have used...
[27:45] Maybe used a little bit more points on my...
[27:49] All my curves in retrospect, but whatever.
[27:52] So brightening it up a little bit here.
[27:56] Then here I'm using the C-depth pass.
[27:59] Let's see to grade a little bit.
[28:02] You can see then I have a little bit more control here over.
[28:07] And I'm not sure if I'm doing that much with it that much.
[28:13] So in this case, I don't think it does that much, but you can do here is you have...
[28:21] Let's see.
[28:24] Turn off the contrast.
[28:29] Yeah, right.
[28:33] What you could sort of...
[28:36] Let me just...
[28:37] That's why you can use the Z-Dep.
[28:39] I ended up doing a little bit different here, but you can sort of use this to grade...
[28:49] Oh, it's not even set to luminance.
[28:51] All right.
[28:52] You can see I'm just messing up here.
[28:56] So you can use this to...
[29:01] Essentially brighten certain areas because you have...
[29:06] So now with this, for example, I could specifically grade the bottom like the back part.
[29:14] So that's essentially what you would use something like that for.
[29:18] Because this is set to all of that, it's not necessarily doing a lot.
[29:21] What I am using here is...
[29:23] Oh, okay.
[29:24] I didn't use that in this comp.
[29:26] I thought I had a previous comp where I was using the position pause as well to do something like that, which was quite interesting.
[29:35] Maybe I can show how that works.
[29:37] I mean, if I'm making this video anyway.
[29:40] So what you would do is you would...
[29:43] Let's see, does this have the position pause?
[29:49] All right.
[29:50] So what you would do is you would grab...
[29:52] You render, you would grab...
[29:55] You grab another one.
[29:57] Let's go to...
[29:58] And this also works in New, by the way, but I'm using Fusion for now.
[30:02] So you put...
[30:05] You go into...
[30:08] into channels here.
[30:10] Wait...
[30:12] Where am I?
[30:18] All right.
[30:19] You go into the channels you put...
[30:21] Position, where is it?
[30:23] Position R...
[30:25] Position G...
[30:27] Position B...
[30:28] So this is a position pause.
[30:29] It might look like Jabberis, but essentially this holds the coordinates of everything.
[30:35] Again, position is just a vector and you can display a vector as color.
[30:40] So you would then go in this thing.
[30:43] You do channel Booleans.
[30:45] You would plug it in there.
[30:47] You would just copy and then put RGB to do nothing.
[30:51] So all fat to do nothing.
[30:53] So essentially, it doesn't look like anything changed, but we now got a...
[30:57] We should have...
[30:58] Oh, not yet.
[30:59] We should go to auxiliary inputs, enable extra channels and then go to position.
[31:04] Next position, we would do a red foreground, white position green, foreground green, and then blue foreground.
[31:12] Now we should have a position channel over here.
[31:21] And then we could do a volume mask.
[31:27] And essentially, this allows you to pick there and let's put it to mask only.
[31:33] Essentially, this allows you not to do sort of a mask from a position in space.
[31:41] So let's fade that a little bit more.
[31:48] Maybe in this case, we'll make more sense to...
[31:58] Well, let's try it like this.
[31:59] Let's do a little bit of touch.
[32:02] And you could say you're at color correct.
[32:10] And you could...
[32:12] It's at the luminance.
[32:14] Put it to luminance.
[32:15] Or you could put it to alpha, do whatever you want.
[32:17] And you can see now we can actually have control over...
[32:24] this specific region there.
[32:26] You can see you can do quite a lot in compositing, which is still thing...
[32:30] I think a lot of 3D-only artists, like really miss this.
[32:36] These are really good skills to have.
[32:38] So if you did now that's really...
[32:40] That's why I like to finish my image in compositing, generally.
[32:44] I'll leave this in as well here for the download.
[32:48] So essentially, merging in the volumes there.
[32:55] Taking the color out a little bit.
[33:00] I guess bringing the color in a little bit over there.
[33:05] Doing a little bit of a glow thing here, which...
[33:11] Some reason not necessarily...
[33:15] Showing me a lot here.
[33:19] That's weird.
[33:26] I mean, it's there.
[33:28] But I just have it very mild.
[33:31] Color correcting a little bit up again, I guess.
[33:37] And essentially...
[33:41] Damn, we're through the compositing.
[33:43] I did a little bit of stuff in After Effects as well.
[33:45] Let me just open that as well.
[33:47] Right, so I actually decided to just rerender the particles.
[33:51] So here they are with the puff.
[33:54] I mean, it was a fast render anyway, so...
[33:57] Not a big difference, but there's some difference, I guess.
[34:00] I mean, it doesn't matter.


### After Effects [34:03]
**Transcript (timestamped):**
[34:03] I also did some stuff in After Effects.
[34:07] I know I should stop using After Effects, but just for some stuff, I just like it.
[34:14] For example, I have these nested in Premiere now with some audio on it.
[34:18] First of all, I just wish the ACES support would be better.
[34:21] But I've just baked this to SRGB for the final things.
[34:28] So here I'm just doing the crops.
[34:31] So the Instagram, Post, Story, and the 16 by 9.
[34:39] So I'm doing a little bit of the exposure flicker here,
[34:46] which is essentially just a exposure with...
[34:52] Not that one.
[34:55] Well, through exposure.
[34:57] So just, we go expression in there.
[34:59] So pretty basic, and then I'm adding a little bit of grain.
[35:03] I might actually reduce that a little bit.
[35:06] I'm just still need to do the final export for this anyway.
[35:09] Might as well reduce it a little bit while I'm out here, right?
[35:13] So, yeah, that's essentially...
[35:18] Yeah, that's essentially the whole thing.
[35:21] Did I copy the wrong one?
[35:23] I did.
[35:24] Put it in here.
[35:25] All right.
[35:29] All right, there we go.
[35:32] So yeah, that's it.
[35:34] Just a small project.
[35:35] I do hope that you learned some stuff from this.
[35:42] Right, so that was pretty much the entire thing.
[35:44] So, even though it's a simple setup,
[35:46] I just thought it would be interesting to do this as a tutorial.
[35:49] Just tutorials you can just sort of see how something like this is built.
[35:53] Again, you can get these source files on Grimroad or on Patreon.
[35:58] Like I generally like to share all of the stuff that I do.
[36:01] So, I'll probably do another one for the second sort of daily render thing that I might do.
[36:07] And I might do this more often because I actually had quite a lot of fun doing this.
[36:10] Like I've mostly been either doing client work,
[36:13] and then in my free time doing the Unreal Engine stuff,
[36:16] which is mostly just technical stuff.
[36:18] And I just had a lot of fun just doing this more artistic thing just very quickly.
[36:23] So I might do some more of these.
[36:25] In the meantime, if you liked this video, please let us thumbs up.
[36:29] Subscribe if you want to see more of these stuff that I do.
[36:33] Again, I'm also going to be starting to uploading a real videos pretty soon
[36:38] with within the Engine integration and stuff like that.
[36:41] I'm planning to do a dev log on the game that I'm making.
[36:44] So it's still very early and there's still so much to do there.
[36:47] That might be something interesting to sort of learn Unreal along side me, I guess.
[36:52] Well, I'm just going to discuss all of the things I've learned and some planning to do some videos for that.
[36:59] Anyway, thanks for watching.
[37:01] Hopefully this was educational.
[37:02] You can download this on Patreon or Grimroad, link in the description.
[37:05] And that was it.
[37:07] See you in the next one. Peace.
[37:14] Bye.



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
