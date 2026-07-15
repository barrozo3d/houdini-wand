---
title: Vellum Fundamentals - Week 5: Cell Splitting Part 1
source: YouTube
url: https://www.youtube.com/watch?v=Q4R7AeCf-Os
author: Tim van Helsdingen
ingested: 2026-07-15
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vellum-fundamentals---week-5-cell-splitting-part-1/
frame_count: 0
frame_status: pending-selection
---

# Vellum Fundamentals - Week 5: Cell Splitting Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=Q4R7AeCf-Os)
**Author:** Tim van Helsdingen
**Duration:** 29m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vellum-fundamentals---week-5-cell-splitting-part-1 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Everybody, my name is Tim, welcome back to the channel and welcome to Vellum Fundamentals
[0:11] week 5.
[0:12] I have checked.
[0:13] It's been over a year since week 4, so we're not exactly doing weekly anymore.
[0:18] I'm not planning to do this weekly anymore, but I wanted to do another Vellum tutorial
[0:24] and I figured this would be just put it into the Vellum Fundamentals series.
[0:28] This is going to be a two-part video, so this is going to be week 5 and it's going to
[0:34] be week 6, 6 as well, because it's going to be a little bit of a longer thing.
[0:37] You can see my dog in the background there.
[0:40] I've got the dog now.
[0:41] Hey Bobby.
[0:42] Yeah.
[0:43] Yeah.
[0:44] Yeah.
[0:45] But anyway.
[0:46] That, Bobby.
[0:47] All right.
[0:48] Anyway, what we're going to be learning is how we can split Vellum Fundamentals.
[0:55] Well, we're going to be learning is how we can split Vellum simulations.
[0:59] So this is something you can not normally do if you've ever tried.
[1:02] If you tried to change the point count in a Vellum simulation by removing something from
[1:05] the simulation, Vellum will break.
[1:08] But there are actually tricks to doing this.
[1:11] And then we can learn how we can create this cool effect of these cells splitting.
[1:16] Yeah.
[1:17] So this is going to be a two-part.
[1:18] In the first part, we're going to be learning how we can source these things into Vellum
[1:24] and then remove things from Vellum.
[1:26] Then the video after that, we're going to take that knowledge and sort of use it to
[1:31] build this cell splitting effect.
[1:33] So yeah, without further ado, let's dive into Houdini and let's learn how we can split
[1:38] Vellum simulations.
[1:39] All right.
[1:40] Let's learn how we can create this cool effect of the Vellum split, same splitting up,
[1:47] which is, yeah, not normally something you can easily do in Vellum if you ever tried
[1:51] to delete stuff or change point counts in Vellum.
[1:54] It will completely break.
[1:55] But it is possible.
[1:56] You just need to know how to do it.
[1:58] There's a couple of steps involved.
[2:01] And then you can make cool effects like this.
[2:03] So yeah, this video is going to be split up into two parts.
[2:06] First we're just going to talk about sort of the basics on sort of just doing like how
[2:10] can we source something into Vellum and then delete it from Vellum.
[2:13] And then we're going to after that, we're going to sort of take that knowledge and then
[2:17] we're going to actually build the splitting setup for the first video.
[2:20] Probably be relatively short.
[2:22] Second video should be a lot longer.
[2:25] So you'll be able to buy all of the source files.
[2:29] They'll be on Gumroad and on Patreon.
[2:31] If you actually, if you get the source files, because like we'll be talking about how to
[2:36] do this, this splitting setup.
[2:38] But of course, as if you saw the intro video, we're actually doing a thing where we're
[2:41] sort of have this whole thing sort of like on a like on a word and sort of randomly
[2:49] sort of splitting up.
[2:50] So this is actually using my path sequence or HDA tool set, which is an HDA tool set that
[2:55] I've built that allows you to sort of take geometry and sort of instance it on points
[3:02] and then sort of randomly time offset it.
[3:04] So we can sort of re time it here to create these things in a very easily or directible
[3:11] way.
[3:12] So if you actually, if you get this on Patreon, you will, the first was will be in the
[3:18] tier where you also be able to download path sequencer, before the full HDA.
[3:23] If you get it on Gumroad, then there will be a discount link to the path sequencer on
[3:30] Gumroad.
[3:31] So your path sequencer will be a 50% discount.
[3:34] So whatever you buy for the source files here, you'll get the effectively off from, yeah,
[3:41] for path sequencer.
[3:43] So this sell division type of effect is actually in effect like I've done this before.
[3:48] I have a course on the Houdini School called Build your brain, which effectively kind
[3:52] of does does this and you also, like you learn a bit more as well.
[3:56] But with this thing, I've actually improved the setup a little bit.
[4:01] I've been wanting to cover this on my own YouTube channel as well.
[4:04] So if I improved the setup from the Build your brain, now it works with sub steps as well.
[4:11] And there's a little thing in here where they actually randomly subdivide so they don't
[4:15] like on the one I did here, they all divide at once.
[4:22] And here you can actually, they actually sort of randomly divide, which is kind of kind
[4:27] of cool.
[4:28] It all just sort of neatly works.
[4:31] And this is actually simmed with some sub steps, so with three sub steps.
[4:35] And it just looks kind of cool.
[4:37] So yeah, in the first video, we're going to be learning how we can source things into
[4:41] the lead term from Valum.
[4:43] Then in the second video, we're going to be learning how we can actually do this subdivision
[4:47] effect.
[4:48] And then at the end of that video, we're also going to be learning how we can sort of get
[4:54] these things to grow on this text 60.
[4:57] It's pretty straightforward.
[4:58] There's a couple of notes just with my path sequencer, HDA tool set.
[5:03] So if you want to try that out, you'll be able to do it as well.
[5:06] But yeah, without further ado, let's learn how we can actually promote.
[5:10] Both stuff from a Valum simulation.
[5:13] All right, so let's make a new note here.
[5:17] I'm going to call this just the tutorial.
[5:20] All right, this is a Valum tutorial.
[5:24] All right, there we go.
[5:28] It's going here.
[5:30] So I'm sure if you've been playing around with Valum, you've had plenty of time because
[5:35] it's been a while that I've done my previous Valum Vendimentals videos.
[5:41] But if you've ever played around with it, you try to remove stuff from a Valum simulation.
[5:46] You're going to be in for root awakening.
[5:49] So let me do a Valum balloon.
[5:52] Configure Valum balloon.
[5:55] Let's do it in a top network because we're going to be doing that in a little bit.
[6:01] So we're going to configure our own Valum simulation.
[6:04] In here, so let's not use the top one.
[6:07] So just make a top network, put the constraints in like this, the geometry and constraints.
[6:12] Let's do a Valum Sover.
[6:15] File them object.
[6:21] Let's just source it in here.
[6:23] Let's do backdick, open input path, open bracket, quotation marks, put zero and backdick.
[6:33] And then do the same and put it on here.
[6:36] Then we should have our sphere here.
[6:39] So this will sort of load it in from first and second input.
[6:44] Right.
[6:46] So let's, I don't know, make a ground.
[6:50] Merge it in.
[6:57] Put this down to a gravity.
[7:03] Right.
[7:04] Beautiful.
[7:05] Right.
[7:06] So we have a little squiggly bounty ball.
[7:09] Right.
[7:10] Let's try something with a Sobsover.
[7:12] So this video is going to be a little bit more complex than any of the other things
[7:15] that we've done before.
[7:16] If you don't know what a Sobsover is, a Sobsover is effectively a note that allows you
[7:21] to use Sobs tools in the end to sort of run over them every frame.
[7:27] Actually have an entire course dedicated to this.
[7:30] I can make it all of the courses.
[7:32] But I actually have an entire course dedicated to building custom Sovers in Houdini.
[7:37] Yeah.
[7:38] So you can learn all about custom Sovers here.
[7:41] It will teach you how to build custom Sovers in a Sobsover.
[7:45] Yeah.
[7:46] Let's make a Sobsover.
[7:49] Let me, by the way, first do, maybe let's do it in here because just to prove a point
[7:54] is to what a Sobsover is, you can also make one here.
[7:57] If you just make a Sover, allows you to here to do it in a Sob network.
[8:02] For example, let's say I do an attribute Wop, which you should all be pretty familiar
[8:07] with.
[8:08] Let's say I do, I add some noise.
[8:13] To sort of prove a point is to what it's going to do.
[8:16] So you kind of understand kind of what it is.
[8:21] So you know that if you do something like this, you can sort of add a noise now to our
[8:25] position.
[8:26] So we're adding a, we're make a Vulp network.
[8:30] We make a noise.
[8:31] We feed our position in here.
[8:33] We add these noise to our position.
[8:36] If you don't understand this basic stuff, watch my Houdini one, how do you want a one
[8:41] course, which sort of goes over the very basic like this, but I'm assuming you know a little
[8:46] bit about, I promoted in the wrong way about how this stuff works.
[8:52] If you don't come back to this tutorial later, because it will be too complex for you.
[8:57] Oh, there's some reason I also not promoted this one.
[9:04] Oh, I'll just keep picking the wrong one.
[9:11] All right, there we go.
[9:14] All right, so this allows us to sort of add some noise to this thing.
[9:21] You can see here, but you can see this will sort of do it.
[9:23] You will see it will get a silver.
[9:24] I get a blue thing and it will do this every frame.
[9:27] So I get a evolving sort of pattern.
[9:30] So this is doing stuff every frame on my geometry.
[9:34] So you can also, you can make a stopsover inside of these are the dops.
[9:40] Actually if you make the one over here, it's actually a, it's actually in a dog network.
[9:48] You can see in here, this is a stopsover in a dog network.
[9:53] So pretty much kind of the same thing.
[9:56] If you go in here and get a stopsover and this stopsover allows you to sort of manipulate
[10:03] geometry with, yeah, with our stop tools.
[10:09] So if we go in here, you see we get a, we get a top import.
[10:14] So these imports are geometry.
[10:16] We can put stuff in between here.
[10:17] And again, you have, you will have all of your stop notes here, like mountain and all
[10:21] of the other crazy stuff that you want to do.
[10:24] We have them all in here.
[10:26] You could manipulate, we could try to do, for example, a thing that we did before.
[10:32] Let's just do it again.
[10:33] Let's just put a turbulent noise.
[10:38] Let's just add some stuff, for example, to our position in here and then you will do
[10:47] it in the solver.
[10:48] So we do add the position and then the solver will do its thing and then you get, you get
[10:53] interesting results.
[10:54] Let's have a look at what this is going to produce.
[10:58] We can have a look at what this is going to do.
[11:03] So you can see we can, we add some to the position and then the solver is going to do it
[11:07] and now we get a walking, swiggly ball, which can be, can be quite cool.
[11:16] So now we have a walking around little, squiggly ball.
[11:24] Pretty cool.
[11:25] This is not what we're going to do.
[11:26] Why, why I'm going to sort of show this thing is we're going to use these things extensively
[11:30] in order to sort of split our, split our simulation.
[11:35] But why I'm going to move this to this side.
[11:38] Why I'm doing this is, if you ever try this, let's try to remove a point from this
[11:45] thing.
[11:46] Let's say we delete a couple of points here from our, from our sphere.
[11:56] Let's say we don't do this at the first frame, we put a switch here, we do this, let's
[12:00] say we do this after couple frames.
[12:03] So we can kind of see what's going to happen.
[12:08] So no, no.
[12:12] No, no.
[12:13] Well frame 50.
[12:14] Right.
[12:15] Now it's going to simulate for 50 frames and then it's going to delete those points.
[12:24] And you can see, right now it's going to, it's going to might even crash.
[12:29] So it indeed did crash.
[12:31] So the reason for this is the way vellum works.
[12:35] If you remember, we have, if we have a look at our stuff here, we have geometry and we
[12:44] have constraints.
[12:47] These constraints are sort of matched with the geometry.
[12:53] So if you, if you certainly remove either some constraints or some geometry, they cannot
[13:00] match the constraint with the geometry anymore and the whole thing just completely implode.
[13:06] So that's why you cannot really do this.
[13:10] We can have a look at another example maybe as to when it breaks.
[13:16] So instead of doing, doing doing like this, let's remove this, let's source this sphere.
[13:24] Let's remove this.
[13:26] Do a vellum source.
[13:29] And if you already know how all of this works, you can skip a little bit of the beginning
[13:32] section, but I like to be thorough in explaining things.
[13:40] But there will be timestamps if you don't want to, if you don't want to wait for the stuff
[13:47] that you might already know.
[13:49] Right.
[13:50] So let's do grid.
[13:52] Let's move that upwards a little bit.
[13:56] Like you already know from the other weeks, how it is all works, but again, some repetition
[14:01] is never problematic.
[14:02] Right.
[14:03] Let's do one point.
[14:04] Let's do, let's change this every frame.
[14:08] And let's say that this should be source points.
[14:18] Go to each frame, store something in here.
[14:26] I'm going to do this one, this one, in some points.
[14:36] I'm going to do some points.
[14:38] Right.
[14:39] Now this should instance, these spheres on my points.
[14:42] You can see they will sort of drop down.
[14:46] Oh, not target path.
[14:49] They should go into constraints.
[14:52] Let's do dollar F.
[14:57] Yeah, let's do dollar F modulo, modulo 10 equals one.
[15:04] So it will only do it every one of the 10 frames.
[15:05] That's we get too much.
[15:07] But you can see now we're sourcing this.
[15:09] Let's try removing one of these and let's see what happens because we're going to run
[15:14] into the same problem.
[15:17] So let's do, do our subs over here.
[15:24] We can just put it in there.
[15:27] So we have our geometry here.
[15:31] Let's say that, all right, that we want to do computer class on here.
[15:37] So we do connectivity and class.
[15:42] So I'm primitive.
[15:43] So this will create an attribute on primitive sort of for each connected attribute, for each
[15:49] connected sphere thing.
[15:53] So if we put, let's say, do a primitive random from attribute and class, we should get,
[16:01] no, I want to run from attribute.
[16:05] So you can see we get a different caller for each of these things.
[16:09] So we could say, is, right, in a certain frame, we're going to delete all of the geometry
[16:16] of let's say, class zero or let's say class, class tree.
[16:23] So we're going to, can just do, let's say, tree connected geometry, edge class.
[16:33] So this will allow us to select a class.
[16:35] We can select one of these.
[16:36] You can see, all right, this is apparently class zero.
[16:41] So we're actually deleting class zero there.
[16:44] Good, of course, change this to be any of the other.
[16:47] Oh, this is class four, by the way, class two or class whatever.
[16:53] So let's say class four, let's say we want to switch.
[16:57] Now you might think, because we're deleting entire sphere here, that this might work,
[17:01] because we're not, not deleting a couple of points.
[17:03] We're deleting this entire thing.
[17:06] Let's try this.
[17:07] The lower f of frame 60.
[17:10] All right, let's have a look at what this is going to do.
[17:14] So it's going to, and it's probably going to crash again.
[17:16] But, all right.
[17:19] So, and then after frame 60.
[17:23] All right, so it's going to try to remove it.
[17:26] All right, and you see weird things here happening.
[17:30] Really weird things.
[17:31] And it just completely breaks.
[17:32] All right, so the trick is to actually remove the geometry and the constraints in the
[17:39] same time step.
[17:40] If you remove them in the same time step, everything will kind of work.
[17:45] So that means we also need to run over the constraints.
[17:49] So as multiple as you can run over constraints, we have this subs over here.
[17:53] This is currently running over geometry.
[17:56] If you actually put constraint geometry here, if you play, you can see it will actually
[18:04] run over the constraints.
[18:05] So there's one way to do it.
[18:07] The other way is to make a sub-s over constraint geometry.
[18:11] This is set up to have multiple in and outputs.
[18:15] And this will now, if we play, this will have both the geometry here and the constraint geometry.
[18:25] It will have available for you and it will output them at the same time.
[18:28] This can be useful.
[18:31] The thing is, as you can see here, there's a compile block.
[18:35] So this block, if you don't want to compile block, there's a compile block, everything
[18:39] you put in there can be compiled, which means it can be sort of multidreaded across all
[18:43] of your course.
[18:45] The thing is not every node works in a compile block.
[18:48] So I don't always like to use this.
[18:50] So we're going to use this now.
[18:51] For this example, later we're going to be switching to using this.
[18:56] But for now, this is going to work pretty well for us.
[18:59] So we're going to find a way to sort of remove both the constraints and the geometry at
[19:05] same time step.
[19:06] And if that happens, then, well, we're happy camper, we can actually remove them at the
[19:12] same time.
[19:13] So let's try to do something like that.
[19:15] Let's put an attribute wrangle here in the beneath the compile block for the geometry.
[19:21] Let's say we want to create an h attribute.
[19:25] The volume doesn't have an h by default, so I can just write an h here.
[19:28] And I'm going to say plus equals at capital time, capital ink, and then some con at h.
[19:41] So this will create an h attribute on our points.
[19:46] So we should have a, we should have it here.
[19:49] As you can see, this will sort of increment them.
[19:51] So time ink effectively, what time ink is it's sort of it's your frame, it's effectively
[19:56] your frame rate divide by your time.
[20:00] That's the timing.
[20:01] So every frame will increment by the time increment.
[20:04] So you can see we get an h attribute.
[20:07] And we can use this h attribute to maybe delete something when it gets above a certain
[20:13] h.
[20:14] We want to do that both on our geometry and our constraints at the same time.
[20:19] So we want to want also have the same age, we also have it on our constraints.
[20:25] Let's just transfer it over h.
[20:27] Right.
[20:28] Now we're also going to get h on our constraint.
[20:32] And you see right now, nothing really changes here.
[20:43] So we now want to put something here to delete when something is above a certain threshold.
[20:49] So we could say, right, we'll do primitives.
[20:52] So we want to delete both our primitives and our points.
[20:58] So let's actually go in here.
[21:02] Let's go for points first, let's load the h attribute that's on our primitives, let's
[21:07] load it into our points for that to do that.
[21:09] We're going to type float my age.
[21:13] We're going to create sort of a local variable here.
[21:17] And we're going to say prim open bracket is allows you to load a primitive attribute.
[21:22] We're going to say, right, from the current input string attribute name and prim numbers,
[21:27] we can say current current attribute, we're going to load age.
[21:30] We want to grab it from the current prim number.
[21:37] So if we write this out like f at cheese or whatever, equals my age, you would get net
[21:47] root here, that's the same.
[21:48] But because we are sort of writing it here as a sort of a local variable, we can just
[21:53] use it in here, right.
[21:54] We're going to say if my age is greater or equal than two, we're going to remove point
[22:04] 0 at pt.
[22:07] So this is see break right now because we haven't done it on the constraint yet, but this
[22:12] will remove all of the points.
[22:15] If their age is bigger or equal than two, let's also do this on our constraint.
[22:23] So that's about it.
[22:31] And you see this actually already works.
[22:34] So this technically I guess might leave us with some empty primitives maybe in there.
[22:40] So for good measure, you should also probably do one over primitives and just say if age
[22:49] is greater or equal than we're going to do over move prim.
[22:54] 0 at prim norm and all of the points.
[23:04] So if you put 0 is going to do all of the points, so we're going to do remove prim.
[23:11] And we're going to do remove prim here as well.
[23:17] This just for good measure, so we have both the primitives and the points deleted that
[23:21] we can be short enough.
[23:23] So because you can effectively have empty primitives of all, even though it was already
[23:28] working, let's use to it for good measure.
[23:31] Yeah, so if we now have a look at this, you can see our spheres that are being spawned are
[23:41] being deleted as well.
[23:43] And this also this works with time steps of all so I could increase my sub steps.
[23:47] It's going to be slow.
[23:51] You can see they get deleted pretty quickly.
[23:54] I think there's something with the, yeah, so because it's now incrementing the age way
[24:04] too fast.
[24:05] So if you wanted to sort of address for that, you would need to grab your subsets here.
[24:10] You would need to go say floats, substep equals.
[24:20] So make a channel.
[24:27] We need to link this up to our subsets.
[24:31] We divide our timing by substep.
[24:39] Then this should work the same as before.
[24:46] Let me reduce the frequency on our three little bits.
[24:52] It's going to simulate a little bit faster.
[24:57] All right, yeah, so you can see works pretty well.
[25:03] So that's sort of the basics of this, of sort of deleting both your geometry and your
[25:12] constraints in the same time step.
[25:15] It doesn't matter if you do it in this solver like we're doing here with the geometry and
[25:20] the constraints in one go.
[25:22] Again, this has some problems because this needs to be able to compile.
[25:25] So some notes you might put in here.
[25:27] Like for example, if you switch if just as an example, I know this note cannot be compiled.
[25:33] This is sort of a switch that uses like if you put a certain attribute in it, it will
[25:38] switch based on the attribute value.
[25:40] For example, that cannot be compiled stuff like that.
[25:43] So if you'd have like you could also what you could do is you could have a stopsover one
[25:51] run over geometry.
[25:53] Then a second stopsover run over run over the run over the constraints and that will
[26:04] they will also work.
[26:06] The best way you could probably do that is you should do something like this called a
[26:10] miltisolver.
[26:11] We could already rebuild this because we're going to be doing that in our once we continue
[26:17] with this setup.
[26:18] A miltisolver allows you to put multiple solvers on a certain object.
[26:21] So we could put a realm object in here.
[26:23] You can want to say it.
[26:24] We want to solve this with a with realm.
[26:27] Remove that.
[26:28] Let's put a gravity below here.
[26:33] Let's put this in here.
[26:37] We're going to see, right, we're going to move this one.
[26:44] We're going to move it to our miltisolver.
[26:47] So this will sort of you put it like this in the miltisolver.
[26:50] It will effectively iterate.
[26:52] So it will iterate on our realm object and it will go through this one by one.
[26:56] So it will first do the iteration on the vellum solver and it will do the iteration
[27:01] on the stopsover.
[27:04] So we played like this.
[27:05] We'll still the work exactly the same as before.
[27:10] But now it's just using the miltisolver and this is going to be a little bit more robust
[27:16] once we start introducing multiple solvers in here.
[27:20] So that's way to our stuff to disappear for some reason.
[27:26] Doesn't seem to work anywhere.
[27:31] Oh, it's just, right, some reason it's just taking longer.
[27:43] All right, there we go.
[27:46] Still works.
[27:47] Let me remove, let me reduce my subsets again.
[27:52] Yeah, so if you were to do that, you would go, if you were to go this route with a regular
[28:00] stopsover.
[28:01] All right, so with these basics working of sort of sourcing stuff into our simulation
[28:09] and removing it, in next video we can focus on actually creating something like this
[28:14] where we are going to be splitting up this actual simulation and we're going to be doing
[28:22] a lot more interesting stuff.
[28:24] We can have a look real quick here.
[28:25] You can see here I am using two different solvers.
[28:28] I'm using the sobs over twice, one over regular geometry and one over constrained geometry.
[28:35] You can see there's a lot more from going on mainly in the sobs over here.
[28:39] So hopefully I'll see you in the next video where we're going to be talking like doing
[28:44] the actual interesting stuff.
[28:45] And of course, all of those techniques you can apply to pretty much anything that you
[28:49] want to do.
[28:50] So see you in the next video.
[28:51] And again, you can download these source files with the link in the description.
[28:56] There will be the source files to this entire thing.
[28:59] All right, see you in the next one.
[29:01] Peace.



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
