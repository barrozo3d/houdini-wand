---
title: Vellum Fundamentals - Week 5: Cell Splitting Part 2
source: YouTube
url: https://www.youtube.com/watch?v=G7SnVk4Jj8U
author: Tim van Helsdingen
ingested: 2026-07-15
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vellum-fundamentals---week-5-cell-splitting-part-2/
frame_count: 0
frame_status: pending-selection
---

# Vellum Fundamentals - Week 5: Cell Splitting Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=G7SnVk4Jj8U)
**Author:** Tim van Helsdingen
**Duration:** 56m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vellum-fundamentals---week-5-cell-splitting-part-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] All right, so let's move out of here. Let's call this just the sourcing basics. Just
[0:16] do we have it in the example file. Let's maybe copy and paste this thing and call this
[0:23] volume splitting. Let's actually do our actual work in here. So we don't really need these
[0:31] source points anymore because we're just going to be starting with just one sphere. We're
[0:37] going to delete the ground plane. We don't really need the gravity in here either. We just want
[0:44] a source just a single piece of geometry. We don't even need the volume source to be honest.
[0:52] We could just source this sphere in here. So we could do up in bootpath like that and
[1:02] with the constraints like that. Let's disconnect the solbs over now. And now we're back to sort of a
[1:11] basic thing where we just have we just have this sphere. Let's put these to one substop.
[1:19] Yeah, so that's pretty much it. So from here we want to start splitting splitting this
[1:25] thing up. So actually build this setup first outside of this main network. Like this.
[1:36] Because we need to start splitting this thing. We can actually just do this here in sub first
[1:42] just to build our little split. And then after that we can implement it in our solver. Right now
[1:49] we don't really need to care about any of the time-stapping stuff. So I'm going to, there's
[1:53] multiplies of course to sort of split a piece of geometry in half. I'm just going to use a
[1:58] Voronoi fracture to do it. So I'm going to scare some points. Scatter two points on this thing,
[2:05] two points. I'm going to do a Voronoi fracture. So Voronoi fracture will fracture this thing in
[2:16] two effectively. You can see if I put a exploded fuel. You can see it splits it into. And if I change
[2:24] the seed, see it's pretty much split it just straight down the half all the time. We could change
[2:31] the seed. We could put a dollar f here so it changes every frame. So if we do do this and it
[2:35] would effectively just change the way that it sort of fractures every frame. So we have something
[2:44] fractured now. But we have a look at this thing. So we cannot really start inflating this because
[2:54] there's no really geometry here on the inside. Right. If we want to inflate this as a bubble,
[2:58] let's we could just try this as I we could just copy our constraints here. Just test this out,
[3:05] show this in here. And let's put a volume over. Let's just have a look at what this looks like.
[3:19] Like that. So if we, let's remove the gravity, let's increase the rest length. So just
[3:29] inflate. So you could see this is not going to work because we have this little piece in the center.
[3:37] In the center. So we need to, we need to remesh this. We put a, let's put a remesh between it.
[3:46] We put a remesh. This will effectively just remesh the entire thing at some more geometry. We can
[3:52] change the target size to be a little bit smaller. So we get a little bit more geometry. Now if we now
[3:59] let's pray. See, it does work, but it sort of sticks into each other because some things here are
[4:09] sort of interpenetrating, which we probably don't want. Pretty easy fixes to do that. So we could do
[4:21] as we could do something like a peak. And peak will allow us to sort of push his thing in or
[4:29] outside. So you can see you can sort of inflate it or outflate it or deflate it. Effectively,
[4:34] all is doing it's just sort of adding or subtracting the normal to the position. You can, you can make
[4:39] a peak like this yourself really easily. It's hard coded, but you could just do this in a, in a
[4:45] vault. You can just add a normal to it and then you get the same thing. So let's do it very
[4:50] slightly. I think this should probably already be enough. Right, XC now if we play, we see them sort
[4:57] of inflating outwards. So that's already works pretty well. And we could, for good measure, maybe
[5:03] add a little bit of a smooth to slightly smooth out maybe these edges here.
[5:10] And this actually seems to, seems to break it. So maybe we don't want to do that too much.
[5:24] I think I might, I think I might just get rid of that. So we could either do like this or we could
[5:30] just get rid of the smooth. I think this smooth does let me make it look a little bit nicer. So
[5:39] let's do this smooth. A little bit like that. Let's do the peak more like that. Let's have a look
[5:52] if this holds up. Seems to hold up pretty well. So we have this sort of coming apart. If we're
[6:03] going to do this in a silver, actually what we want to do is we want to do this multiple times.
[6:07] So in a, like once we're inside a silver, we actually want to start doing a
[6:13] for each loop for each connected primitive. We want to sort of do this again. So it'd be in the
[6:19] for each loop where we would have, we do actually do it by connectivity. We do connectivity.
[6:27] creates a connectivity called class attribute, which checks for connected geometry.
[6:32] And it gives a class. You can see two classes. You would put it to class.
[6:36] And then we would get sort of two passes of this. And then we would effectively just do this again.
[6:44] And in silver, this is not going to be multiple for each loops. But now to just demonstrate here in
[6:51] sobs. And turn off single pass. And yeah, you can sort of see it's sort of being split again.
[7:02] Of course here, like it's not, like it looked a little bit weird because they're not inflated yet.
[7:06] What you can see here, there really is multiple times you can sort of individually keep splitting,
[7:11] keep splitting these things. So let's implement this in our silver.
[7:18] Right. So let's grab our little for each loop thing.
[7:23] And let's go in here. And just remember, we're not going to go in here. Remember,
[7:29] we cannot really start playing this before we also implement all of the other stuff.
[7:35] So from now on, we're sort of just going to work on the static setup for a little bit.
[7:41] Because once we start splitting this, it will immediately break if we play because we haven't dealt
[7:46] with the constraint chat. So we're just going to go in here. And we're going to just be dealing with
[7:51] some stuff in our sobs over. This is making new sobs over just for good measure. Like make a sobs over.
[7:58] And let's call this run on geo. Let's do another one.
[8:08] We're going to our sobs over and call this run on cone strains.
[8:17] And plug this in. And for this one, we're going to say that it should run over the data name,
[8:22] constraint geometry. And if you're confused about how you can find these names or what these
[8:28] things are called, if you ever forget, you can just if you look in here in your geometry spreadsheet,
[8:33] which I always have open here, I like to have my geometry spreadsheet always open in the back.
[8:37] If you don't know that you can split a few top bottom left right like this,
[8:44] or like top bottom, and you can make that something a
[8:50] spreadsheet. So I like to keep that open.
[8:55] Anyway, so if you do that in a open network like in here, you can actually see sort of the
[9:00] context here change to a dog network contact. And you can see here a vellum object. If you go in
[9:05] here, you see all of the things sort of contained in our vellum object. You can see there's
[9:10] collision geometry, constraint geometry, geometry and patch geometry.
[9:15] So we're going to be focusing on this geometry and constraint geometry.
[9:20] There's also this, if you have a collision geometry, that's of course, if you put any colliders in
[9:24] here, it's going to be in here, patch geometry. If you make a vellum source test patch name,
[9:31] effectively, this is just kind of like the group name. So it will like a few source this,
[9:36] it will be pulled in here and would be called vellum source one. If you'd have another one,
[9:43] we vellum source two, it's kind of like just a group that is sort of in and it's going to be
[9:47] a like. So we can have a look in here as sort of these things. So we're going to run over these
[9:54] geometry and constraint geometry. So if we if we play through this and we can have a look here,
[10:00] so here we can just see the geometry. And if we go in here, we will see the constraints.
[10:04] Right. So we will first need to start working in here. And again, this is all plugged into a
[10:12] multi-solver. And the way this is going to work is it is, this multi-solver is going to iterate on
[10:16] this vellum object. And then it's going to do these things from left to right. So it's going to
[10:20] solve vellum, then it's going to solve geometry, then it's going to solve constraint.
[10:25] That allows you to say the primary solver, which is set to zero, which is the first one. I guess
[10:30] if you'd want another one to be the primary solver, yeah, you could change that.
[10:36] You can make that mutual factor, so you can turn it off. For our sake, this doesn't really matter.
[10:45] You can see something here changes about sort of if they're sort of like related to each other.
[10:55] This effectively says that if something happens in here, that should also affect whatever is in
[11:00] here and in there. If you turn it off, these things are only going to influence sort of the main
[11:06] thing that you're sort of iterating on. For our sake, it will work regardless. Yeah, so just like
[11:14] this. So yeah, let's start actually working in our in our geometry. Let's copy this thing.
[11:20] Sure, I still have a copy, but let's copy it. Let's go in there, go into geometry.
[11:27] I want to sort of move this down and I want to sort of branch in here. I want to
[11:39] display a couple frames. Let's have a look. All right, yeah, so I need a connectivity before it.
[11:47] Keep accidentally sometimes pressing just my caps lock. So I need a quality before it.
[11:54] I also not going to work. I want to put it to primitive. Now this should work.
[12:00] So you can see I can actually now play this and nothing will break.
[12:04] So because here is a, this is the output. This is connected to the job, job geometry.
[12:11] It's outputting this thing here on the left. This thing on the right here,
[12:14] we can, like it doesn't matter if we have it highlighted, it's going to sort of output whatever is
[12:20] here. And here we can just work on work on this little part. So it's going to output this side,
[12:25] this part we're going to work. So kind of like what we're going to be doing is we're going to
[12:32] split our geometry here. And then here we're going to set up these age attributes and then once
[12:37] this age sort of reaches a specific value, we're going to replace the thing that's going in here.
[12:43] We're going to sort of swap it out with the thing on the right. So before we can even start doing
[12:48] that, of course, it's not enough to just do this thing because we're splitting it. We also need to
[12:54] create these new, these new constraints and everything. So we actually need to do another for each
[12:59] loop, for each connected piece. So we need to do another one because we kind of, like we don't
[13:10] want to just run over what is created here. So here we are creating this sphere. And then in
[13:15] here, we have these two parts. But we can again, we want to run over these two parts individually.
[13:22] So we could either make this for each loop inside of this existing for each loop, or we can just do
[13:27] it after the fact. That doesn't necessarily really matter. Because you see now here we get,
[13:32] we get these other two parts. So this is going to again, we're going to run over this. And then in
[13:36] that thing, we can start creating these, these constraints. So we would need to do a,
[13:45] could do another volume balloon.
[13:51] Could put this in. Then we would get our thing like this. And then we could do a
[14:00] vellum pack. So we can sort of pack up these constraints. So they only get one output.
[14:08] So we could do like this, like that, and like that. And we can put them here in the output.
[14:16] So we get one one output over here. And then over here, we could do another vellum in back.
[14:22] And then we would have our geometry here on the left. Let's call this, I guess, split
[14:34] geo. And on the other side, split, con. And let's go. All right. So you can see here, we have
[14:46] geometry, we have constraints. And here we of course still have our main thing. So the idea would
[14:54] be to sort of in the same time step, sort of switch to this geometry. And then in our constraints,
[15:03] move to this constraints. So in the same time step, and then it should sort of replace it all,
[15:09] and it should theoretically work. So we can just try this really simply by just before we set up
[15:17] any of the attributes, let's just manually try this. Let's put a switch here. Let's put a switch.
[15:23] So this switch is going to switch from this to this. Let's say we want to do this dollar
[15:29] frame, dollar f above frame, free. So it's going to after frame, free, it's going to switch from
[15:35] this input to this other input. Now we will need to do this again. We want to do this in our
[15:41] constraint geometry as well. Let me open my thing over here on the side again. We have I can have
[15:47] a look at our splitting setup. Let's go in here. Let's go into constraint. So here on here on the right,
[15:58] we're going to have a look at the constraints. So we want to actually object merge, something in
[16:04] here. We want to object merge our constraints from this others over in there. And we want to do another
[16:11] switch. I want to switch on the same time. So we can just copy and paste this input copy and
[16:22] paste reference. So this is going to do the same. So if this goes to one, the other thing also
[16:26] goes to one. So effectively, after frame, free, this will switch to the fracture geo and then the
[16:32] constraints as well. And technically, this should now work. Let's have a look.
[16:39] Right. So it keeps, okay, it keeps doing it now. You can see it does work. So it keeps splitting it up.
[16:48] Score is not what we want. But you can see it does work. Like the volume, the volume doesn't break.
[16:52] It just keeps splitting it up every frame because it effectively just stays at the second input.
[16:57] If we just want to check it, be just at the at the at the other input, what we could do instead is
[17:05] maybe dollar F percentage means module low. Firty equals one. What what this will do?
[17:15] Effectively, right. So percentage module low, Firty will effectively just effectively just keep
[17:25] counting from like zero to 3D. Let me maybe turn off the simulation. I can show you the output.
[17:34] Yeah. So if I do this, it will effectively just keep counting until it gets to 3D and then go
[17:41] then repeats. That's what module out does. So if I then put equals one, it will evaluate to one.
[17:50] I should put this between brackets, by the way.
[17:59] Right. There we go. So now it will evaluate to one every Firty frames.
[18:08] So you can see now it's going to do this every Firty frames. And I probably want,
[18:12] because you see it also does it on the first frame. So I could, what I could do if I don't want to
[18:16] immediately split, I could do a second switch maybe. Let's do let's put a null here. Let's do a second
[18:24] switch. And let's say this one dollar F above frame, I don't know, 20. So let's do 20 frames of
[18:34] not doing it. And then after that, it will sort of switch to this other input.
[18:40] And then it will keep doing it. So let's do the same over here.
[18:53] Right. Here we go. All right. So let's have a look at what this will do.
[18:57] I have to update. All right. There we go. Play. Right.
[19:08] All right. As you can see, we have a splitting volume sim. So of course, this is not really,
[19:14] like it's not inflating yet. But I mean, you can see, like we do have something that works.
[19:23] Quite cool. So in order to inflate, we need to actually override these constraints in here. And
[19:29] what we kind of want to do for that is we actually want to go level up. And we want to actually grab
[19:35] our pressure constraint here. So if you remember, these constraints will have different names,
[19:42] different groups. We've already used this while before. We want to rename our constraint here
[19:47] for our pressure. We want to output a group. I want to output it to pressure, the pressure group.
[19:53] And we want to do the same in the one over here, where we also have a group. I want to call it
[20:00] pressure. And then we want to do a volume constraints. I want to do volume constraint properties.
[20:07] Sorry. Like that. And we want to put it in particle forces. We want to run it over pressure.
[20:15] And we want to say rest length skill equals one. So they will just inflate it to a value of one.
[20:22] Let's have a look what this will do. And oh, not rest length skill. So this is a multiplier
[20:32] of the existing skill. We actually want to override the existing rest length. So it's always one.
[20:36] So let's have a look what this will do. Right. Here you go.
[20:39] Now you can see. So this will sort of override any existing rest length. So if we go in here,
[20:50] if we just have a look in the, if we have a look in the server, let's have a look at the constraints
[20:58] that we have here. That's blast out our pressure constraint.
[21:13] Right. So you can see there's a rest length. It's not, it's not one. If we put that thing on,
[21:21] it will just, it will override it. If we use this other thing,
[21:24] a rest length skill, it will sort of work as a multiplier on the existing rest length.
[21:30] So I guess if we put this to tree, it will also sort of work. So I guess it depends on
[21:38] kind of what you want to do. You can put it to four if you want to inflate it more.
[21:46] So I guess either, either is fine. Either, either, either set a static rest length or
[21:52] uses a multiplier. This will always produce sort of exactly the same sort of size inflation
[21:59] because it's just going to override it. This is going to depend on the size of things that are
[22:03] created. So if one is created smaller and the other one is created bigger, this will work as a
[22:07] multiplier. So it will create a smaller one four times as big, the big room four times as big.
[22:14] Yeah, it kind of depends on kind of what you want to do. So you do see, they are sort of being
[22:18] pushed away quite far. So this is because of the forces at work in the vellum's over. If you want
[22:23] to reduce that, you can go to vellum's over, you can go to velocity damp, dampening, and we can
[22:29] increase the velocity dampening, which is will dampen the velocity. So they sort of stay together
[22:35] a little bit more like this. And you do see this weird thing happening here. So because this
[22:42] thing is being fractured and rematched, it's not pre-computing the normals. So that's why it looks
[22:47] weird. So we just need to recompute the normals. We can either do that after the same or in the same,
[22:52] but if we want to look at it in the same, just see what it looks like. We probably want to just do
[22:57] this inside of the simulation. So we could just put in normal here, just recompute it there. And then
[23:07] where, okay, I guess I don't do it there. Guess maybe I should do it there.
[23:12] Okay, for some reason, visualization seems to still be a little bit off this weird.
[23:25] Doesn't necessarily really matter to be honest. You can just do it if we do it after the fact here.
[23:32] Then it does work. Okay, then I have no idea why it's acting weird because I'm doing exactly the same
[23:37] thing here. I could, I don't know, if I put it here, it should also work because then it's just
[23:43] constantly doing it every frame. All right, that does work.
[23:53] I guess it was, yeah, the reason why it was not working is because it's recalculating the
[23:58] normal on the not inflated jet geometry. So that's why it was looking weird.
[24:03] So, but now we have, yeah, we have a splitting vellum sim. Pretty cool, right?
[24:18] And again, we can either do it like this or we can do it like that.
[24:22] You can see if we do the other one, they get progressively a little bit bigger.
[24:39] So, I guess it depends on the type of effect that you want to achieve. For sales, it wouldn't
[24:46] really necessarily make sense if they get progressively bigger. So, something that probably makes
[24:51] more sense. All right, so we have a, we have our basic thing going. Now we can work on getting this
[25:00] a little bit randomized. So, now they're sort of all splitting at the same time, which maybe what you
[25:07] want, maybe not what you want, but I mean, we have a working setup now. So we can make it a little
[25:12] bit more interesting. So you can start working on this, doing it by H and then randomizing when it
[25:17] switches, et cetera, et cetera. So, let's try that. So, let's make a wrangle. Let's do a tree
[25:24] wrangle. Call it createH. Put two primitives. We actually want to do all of these other things
[25:33] after this. We're going to do first create our H. Right, let's say f at H plus equals at time
[25:40] ink. And we probably, let's make this work for the sub steps as well. So we're going to go in
[25:49] here. Let's make a integer sub steps equals general I, sub steps. Let's link that up.
[26:02] And then we're going to do divided by such steps. All right, there we go.
[26:13] So it works. So now we should have a, we have a primitive H of increasing.
[26:22] Now we can use that H to start sort of splitting, splitting some things up.
[26:30] So, this is in a second wrangle. Let's do wrangle.
[26:37] Actually, we want to maybe want to move this connectivity, we want to move it over here so
[26:42] we can use it in our wrangle as well. Let's do, let's create a random based on our class.
[26:50] Rand equals Rand at class. So we're going to create a random value based on the
[26:59] E-class. So if we have a look at this, you can see we have a class going from 0 to 3. If we were to
[27:06] write this out, you can see we get a random value for every class. All right, now we can fit this
[27:17] value. I could say Rand equals fit 0 1 because we want to fit something that is between 0 1 to
[27:24] something else. So we could say, right, R and then let's say 0.3 to 1. I'm going to fit a machine
[27:32] like between ways of doing 0 1. Oh, not R, Rand. Yeah, I usually, like I often use R as a
[27:42] placeholder variable for my random stuff. All right, now we can say that maybe that if
[27:50] at h is greater or equal than Rand, and also Rand maybe is greater than 0.3 because we don't
[28:04] want to do it every time else is going to split a lot. I can show you the difference in a little
[28:09] bit. Let's first have it set up like this. We're going to say, right, let's set an attribute. Maybe
[28:16] I add my split, comes one. This is going to create an attribute called my split, which is sometimes
[28:22] going to be 0 and sometimes going to be 1. I guess in this case it's always going to be 1 for some
[28:27] reason. All right, because our, of course, our h is above, because we haven't sort of reset our
[28:36] h, which we also need to need to do. Because of course, after their split, their h needs to be
[28:43] reset. So we should do a primitive wrangle sort of after this whole thing. We should do that on,
[28:51] let's do it here. Primitive, we're going to say, right, f at h equals 0. And we also want to say,
[29:00] I add my split equals 0 as well. Because we're going to sort of, once they split, they should
[29:07] restart counting again from 0 else they will just keep incrementing this h. So for now, if we're
[29:13] going to be placing prey, we should be able to go in here. And you can see they will sort of,
[29:26] once they split, boom, they will sort of go back to 0, start counting again. And my split will
[29:33] be 1 here. And then after that, we'll sort of go back to 0. Now we have this is my split attribute.
[29:41] We can actually start sort of removing this stuff that we have here. We could do it with a switch
[29:48] if, and this is the reason why I don't want to use the this one, so for constraint geometry.
[29:54] Because we also need to do the constraint later. And we cannot use switch if in a compiler block.
[30:00] We're going to use switch if I'm going to say, h view value, and I'm going to say, right,
[30:07] I'm going to say that switch or what was it called again. It was called my split.
[30:16] My split is going to be a primitive attribute. It's going to be
[30:24] greater than or equal to say one. So if it's one, oh, no, it's always one. It's not, it's always
[30:32] going to be one because it's a thing. So it can just be equal to, you don't need to be greater
[30:38] or equal to just if it's one is going to switch. And then we need to do the same in our constraint
[30:45] geometry. And we need to make sure that our that this also happens on our constraint. So maybe
[30:52] instead of doing it like this, let's actually put this rainbow maybe on two sides. Let's put it
[30:55] on both our constraints and our geometry. Right. Now I want to go into this thing on constraints
[31:01] and want to load in our geometry here. So I want to do another object merge. I want to load
[31:12] this geometry they have here. I want to transfer something to our constraints
[31:18] from our geometry. I want to transfer age, age and my split. And now we can do the same with this
[31:36] switch if you can just get rid of this. You can say right switch if
[31:42] if it's equal to one is going to switch. And again, so it's grabbing now only constraints.
[31:50] It's going to grab from my regular geometry. It's going to grab the geometry. It's going to transfer
[31:57] age and my split to the constraints as well. And then if it's going to be one, then it's going to
[32:03] switch over. Let's have a look what this does. Let's actually have a look here. Right.
[32:11] All right. Let's see. So this is switching. And this is merging in the geometry.
[32:23] The same frame we should have our geometry here. We should have
[32:30] I think actually if we were to load this and it might actually work.
[32:35] This has some knowns going to grab the thing before it switches. Let's have a look at this
[32:39] actually does anything. All right. There you go. So the reason this works now is because
[32:46] this was switching and then it would grab the reset value here and it wouldn't have the
[32:50] my split. And so then it would break. So let's call this is null out refracture.
[33:00] Now it's going to transfer these over perfectly fine. And now let's have a look at what this is going to do.
[33:16] And it does seem to always split them now for some reason. We need to tweak our little wrangle a
[33:24] little bit I think because I don't want them to always split. Let's have a look at the
[33:31] randomization here. Let's say only if a rent is above 0.9. So let's see if then what will happen.
[33:40] It's going to wait a long time because it's going to wait for rent to be above 0.9.
[33:45] Which only happens 10% of the time. Which I guess is not going to be a lot. All right. Let's tweak
[33:52] it a little bit. Let's make it 0.7. Let's maybe oh I know what's going on. Let's put it to tree.
[34:00] So of course like it's going to do the random on the class but it's always going to be the same random
[34:05] because so like nothing is ever going to change. We probably want to do at class plus at frame.
[34:15] So it's going to change the random that's being called every frame. So now we should get something
[34:19] more interesting. It's still splitting them all at the same time.
[34:33] Now let's have a look if we make this threshold a little bit bigger. What's going to happen?
[34:49] Still happening. Oh wait I forgot the step. Yeah. So what's happening here is that if my split is
[34:58] equal to 1 it will switch this so we replace the entire input but there's no check here
[35:04] to see which one it should fracture. So this is a stupid but again like I like to leave some
[35:09] mistakes in. So you know what's going on. Which is actually also do a switch if here. If it should
[35:15] even fracture them. Also of course it's not going to change anything. So we're going to do
[35:22] at with value switch. So if I call them again my split my split
[35:34] primitive equal to 1. Alright let's have a look at this now works.
[35:45] Still seems to be splitting it. No no. You can see some will stay. This one is not splitting.
[36:01] You can see some are splitting some are not splitting. Alright so we have it working.
[36:07] Beautiful. Yeah so you can see some will split some will not split.
[36:16] And you can change these values from the threshold over here.
[36:21] Alright so with that out of the way let's cash this out actually. Let's do a
[36:30] top IO.
[36:35] And let's slow this in. Let's go and let's load the work.
[36:44] And let's say that we want to load our valum object.
[36:51] And we should get rid of this part over here. We want to do if you chose particles it will
[36:58] grab the geometry as you can see here. And we want to do another one and we want to also load
[37:03] the constraint geometry. Get to constraint geometry. Now we can do a valum IO.
[37:14] So we can cash it out. So some additional thing that you actually might want to do before
[37:19] you cash this out is if you want to texture these you would want maybe some rest geometry on this.
[37:26] So we would want to put a rest here. And you want to put a rest.
[37:35] Where you going here. You'd want to create a new rest probably here.
[37:44] So if you don't know what a rest geometry is. So this effectively stores the position
[37:50] of this geometry. You can use it to sort of map a map texture texture only. It's kind of like a UV
[37:58] but you can use it for triplanar mapping so you can sort of project it
[38:01] sort of during render time. So if I let me show you what what I can do for example with this.
[38:07] If I do an attribute noise.
[38:13] It's a nice factor. So if I were to put some color on here.
[38:22] If I do some color on here by default you can see it's going to float
[38:31] true. Like the noise is going to float through this thing. So if it goes to 360 it's not really
[38:36] sticking on it. Right. If I do this on my rest that I generate these rest positions that will be
[38:44] sort of set the moment it fractures. See now actually I get a static noise on these things.
[38:51] And you can use this in your triplanar mapping when you render this. Yeah you can use this to
[38:59] let me show you how you would do that. I'm actually not using any textures in myself
[39:07] but if you were to do it you can see I did experiment with it a little bit before it.
[39:11] There's a triplanar mapping which you could put some textures in here. You see like I was
[39:16] experimenting with it. I didn't really use it. You can use a printbar reader.
[39:21] You could use a float tree and you could type rest. You can use this position in the position.
[39:27] And now this will sort of map this texture based on this reference position. So you can texture these.
[39:35] So even though they're splitting you can still get some nice textures textures on it.
[39:39] You don't need to so that's how you solve sort of the UV problem. Anyway let's catch this out.
[39:46] I'm going to say cells and let's do 300. Let's maybe stop this thing after certain amount of frames.
[40:00] Let's maybe if we want to stick together a little bit more because you see now they're sort of
[40:04] floating apart. We could actually increase this velocity dampening. So they're at least stick together
[40:09] a little bit more. And if you want them to sort of build up in something like a like a sort of a
[40:21] shape specific shape patch and you could what I did in my sim put a put a collision geometry in
[40:32] there so they will sort of just fit into that shape eventually. Does it really matter for what
[40:39] we're doing here. Let's just catch this out cells. Let's change one more thing. I don't want them to
[40:46] do this anymore after a certain frame. So let's say that do enable solver.
[40:53] And we're going to do a dollar of below frame 250. So it's going to be one.
[40:59] Until we get to frame 250 and it's going to disable it.
[41:03] I'm going to do that on there as well. So it's only going to do this splitting until frame 250.
[41:09] And after that it's just going to run. And now let's save this out.
[41:16] Right so the patch that's being created here is not too big. So this cast pretty quickly actually.
[41:22] So it looks pretty cool. Yeah now finally if we want to sort of maybe instance this on a
[41:35] on a on a text like I did in my in my example. What I first want to do is I want to create a proxy
[41:42] for this because instanting a lot of these might get really slow. So maybe I want to do a sphere.
[41:50] Give it some like this make a little bit bigger. It has ray.
[42:00] Ray this to our original geometry.
[42:10] So we get like a little proxy for for our actual shape. So we can do
[42:17] proxies geometry. We say geo proxy proxy for dot bjo dot sc. Save it out.
[42:31] For no frames.
[42:36] All right this. And then maybe for our render stuff we actually maybe just want to
[42:42] do.
[42:45] We don't care for this entire cache. We don't care for the constraints. We might want to do a
[42:49] valentose process after this.
[42:58] Maybe you might want to maybe pick them a little bit to sort of
[43:05] do something like this. And then let's do a.
[43:12] I could want to maybe attribute delete some stuff. Let's see if there's actually stuff we
[43:16] don't need. We don't need class. We don't need age. Don't need my split. Don't need name.
[43:22] Don't need any of these. We only want to keep some star. Only want to keep
[43:29] lost the rest. And we can call this render geo render geo. So I'm going to save this out again.
[43:45] But nobody actual geometry.
[43:50] Right. And now I could start instant. Installing this. Maybe do I
[43:55] could do anything pretty much could also do this inside of a big. Let's do a big for now. We
[44:00] can. You can do whatever you want on it. Let's do points from volume.
[44:08] Sorry, this let's. Let's.
[44:09] We jitter them a little bit.
[44:12] Now let's do. So we want to now use my pop sequencer again. This is not by default in your
[44:18] Houdini. This is a. It's a A.C.A. toolset that I made. It's paid. You can get it with a discount.
[44:27] If you buy the source files to this tutorial or you can just buy it directly. There will be a link
[44:33] to to these things in the description. So if you're interested, you can do it. There will be a link
[44:38] to the example of what it does as well. Effectively, it's it's an A.C.A. toolset allows you to sort of grab
[44:46] geometry caches or or geometry from this and sort of instance animated geometry on points and
[44:53] then time offset it and it's quite neat. If you type the VH initialize attributes, I want to start
[44:59] initializing attributes on this. So this will initialize an H attribute. You can see here. I can say
[45:06] the start attribute that I want to them to start on. In this case, it's fine from from the first
[45:14] frame. Then I'm going to do a TVH geo sequence. Geo sequence allows me to set up a geometry.
[45:24] So instance geometry sequence, I don't want to do it from scene. I want to do it from this.
[45:28] So I'm going to add a plus icon and I'm going to go here and I'm going to go to hip. I'm going to go
[45:35] to geo render geo one. I'm going to plug it in there. You can see they're quite big. So I'm going
[45:42] to do TVH scale instances. I'm going to plug it in there. I'm going to change the global scale.
[45:49] I'm going to maybe also do some maybe a little bit of a random scale. Maybe I do want a little bit more
[45:58] points. Make it a little bit smaller and let's do for instance as well. We get a little bit more
[46:06] of a random rotation which might be a little bit nicer. Let's do just do an a randomized
[46:19] orient. Might actually do better in this case.
[46:27] So you can see we can see our splitting happening on our sphere. Maybe we already actually want to
[46:32] do. By the way, before we do this because now they're sort of coming, it's called already existing.
[46:36] Maybe we want in the first couple of frames. We want to actually scale in the sphere.
[46:44] So let's do transform. Change from this down. Save this out.
[46:54] And we want to do this on the proxy as well.
[46:57] So all right. Now we can see them sort of appear. I get this. We need to initialize this.
[47:11] Also it's going to open up a little bit weird.
[47:19] Let's open up. Why is this looking weird?
[47:28] Oh, yeah. We need to
[47:35] go to open my scene again. Instanceing sometimes can keep stuff in memory. So you get some weird issues.
[47:48] All right. So it was a weird few-board thing. Now it's working so you can see it's all sort of
[47:53] splitting now. It's happening all at once now, which probably doesn't look that nice. So we want to do a
[48:00] DVH3 time instances.
[48:05] Want to randomly offset maybe some of this. So some will start a little bit sooner. Some will
[48:12] start a little bit later. Right now we actually get a nice. Now we don't if we even need to proxy
[48:23] that I made for this. So what the proxy effectively why I made this for if you have a ton of points,
[48:29] it might get of course slow to instance this and you could put the proxy in.
[48:36] So you could have something that's sort of fast to work with if you look in your freeboard. But
[48:41] it's actually it's not too bad. If we just look at it like this.
[48:45] So we have a whole big growing like this. And now we could if we want to render this in karma,
[48:55] for example, we could grab a out here. Could do a log network.
[49:08] Put a stop import. And now if we want to import this, it's important that we preserve these
[49:12] instances that we created with this thing. Way to do that is you're going to primitive definition,
[49:21] packed primitives point instance. So that's going to create a point instance from it. And now we can
[49:26] load the let's make a let's actually load this thing out. So we're going to load it in here.
[49:33] So this is actually going to create a point instance or with with all of the prototypes that we
[49:38] have here. So all of the different frames that's loading. So you can see it's grabbing these
[49:42] grabbing these things from this. Now you could just do a environment lights do like a stirai.
[49:58] Make a camera.
[50:09] Okay. Alright, there we go. Make a camera. There we go.
[50:14] We're going to do a little bit closer. Like this.
[50:24] Maybe you want to do like a quick material quick service material put it in here.
[50:30] And let's call it cells sign material.
[50:44] We want to maybe by the way call this cells as well. So import pops are actually name cells.
[50:50] We want to assign material to cells and we want to assign our cells material.
[50:55] And we could I know.
[51:03] It depends what you want to do with the look. I don't want to spend too much time here on
[51:10] creating a look for this but
[51:11] let's
[51:23] make you could do something that
[51:28] maybe even that's on during the mission.
[51:34] Let's go to be slow. Let's do it like this.
[51:42] Yeah, so you can see we have we have now a big
[51:50] sort of shaped from cells. And if you want to use these rest attributes in these materials
[51:57] instead of doing this quick service material how you would do it is
[52:06] instead of doing the quick service material what I would actually start doing is I would go
[52:10] material library. Turn off gromming spew. You would do material library. You would make a grama material.
[52:24] Cells. Would do a triplaner. Triplaner projection.
[52:31] Put it in a symbol base color. Then I could point this to a texture. I have a UV texture here.
[52:37] Oh, I can just grab this. So effectively what a triplaner is going to be doing. Oh no,
[52:48] I don't want really messing this up. Right, there we go like that. And finally triplaner is
[52:53] going to create sort of three cameras. Top side side project a texture and sort of have a
[52:59] blend between it. And it's going to do that based on these rest positions. We do a primvar reader
[53:05] flow tree rest. Want to load in these rest positions. I'm going to put it in position.
[53:11] If we want to do tiling on this we could do a multiply here to sort of set up some tiling.
[53:16] And let's assign this material actually.
[53:23] And let's have a look. See it's just a just assign this thing. Just a
[53:34] just the UV just to sort of show you that works. So if we just correct through this,
[53:41] you can actually see it's actually sticking. So you can actually texture this to your
[53:47] hard content. Now we have a we have a cool valum spling simulation. Of course, like you can make
[54:01] this a lot crazy. You can run a lot longer simulation than we have here. This one is quite short.
[54:09] There's not that many splits happening. But of course, you could have them split a lot more.
[54:19] If that's what you want, you could like you can have sub steps on this as well. We could slow down
[54:26] the time scale. If you don't want them to be this that explosive, you could do something like this.
[54:35] You can if you reduce the velocity dampening, you could have them go like that.
[54:42] Yeah, just have at it. Make something cool. But yeah, this is how you split valum simulations.
[54:48] And again, it doesn't have to be cells. You can like you can cut up geometry, like cut off limbs.
[54:56] Do anything crazy that you want. I might do future tutorials as well, where I make some more examples
[55:03] of this. For example, if you'd have a soft body, you could you could overlimp. You could do it
[55:08] dynamically instead of pre-facturing it. You could actually sort of tear it off,
[55:13] like depending on where sort of a thing hits. You could sort of cut it in a solver. Stop like that.
[55:20] Yeah, this is effectively how we do it. I hope you enjoy it. I don't think there's really
[55:27] that many tutorials explaining how to do this. I haven't really seen any online.
[55:33] Yeah, this is how you split film simulations. Yeah, so if you want to download the source files,
[55:41] there will be a link in the description so you can get them on Comrade, Patreon,
[55:47] or other places as well, depending on when you watch this. If you want pop sequence,
[55:53] well, to sort of do this whole instance setup. If you buy the source files to this video, you'll get
[55:59] a discount code to get pop sequence or 50% off, which should be the same cost if you buy pop sequence
[56:05] or directly, but now you also have these files. So you have both, which is nice. If you support
[56:10] on Patreon, you'll be able to download both in the same tier as well. So you get pop sequence
[56:16] or plus, the source files to this thing. So it helps support the channel so I can continue making
[56:23] these videos. Well, hopefully you like this and see you in the next one. Bye.



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
