---
title: Houdini for Beginners - Part 2:  Navigation
source: YouTube
url: https://www.youtube.com/watch?v=VpkcIxYUOos
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "20.x"
tags: [beginner, navigation, ui-basics, houdini-env, obj-context, sop-context, display-flag, template-flag, bypass-flag, node-info, orthographic-views, uv-viewport, jordan-allen]
extraction_status: complete
frames_dir: tutorials/frames/houdini-for-beginners---part-2-navigation/
frame_count: 14
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini for Beginners - Part 2:  Navigation

**Source:** [YouTube](https://www.youtube.com/watch?v=VpkcIxYUOos)
**Author:** Jordan Allen
**Duration:** 19m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] I want to quickly take a look at navigation inside of Houdini.
[0:03] If we hold ALT and left mouse click, we rotate around the object, which is great.
[0:08] But the problem is the middle mouse button and the right mouse button, I think, are backwards by default,
[0:13] at least the way I typically like to work.
[0:15] Right now, in the default state, if you hold ALT and hold down middle mouse button,
[0:20] you can pan around the scene.
[0:22] And if you do the same, hold ALT and right mouse button, you zoom in and out.
[0:26] I want to switch those.
[0:27] I want the right mouse button to be my pan.
[0:29] Because I just used the scroll wheel to zoom in and out anyway.
[0:33] The same is true of this node view area.
[0:35] I've got this geometry node.
[0:36] If I left mouse click, I drag it around.
[0:38] If I hold ALT and right mouse right now, I zoom in and out.
[0:42] And if I hit ALT and middle mouse button, I pan around.
[0:46] So honestly, this one's completely optional.
[0:47] Well, it's all optional, isn't it?
[0:49] You're not currently being held hostage.
[0:51] I don't think.
[0:52] If so, don't watch this.
[0:54] Call 911.
[0:55] But we can change that very simply just to revert it so that my brain is happy.
[1:00] And maybe yours is too.
[1:01] If you want to join me, we can do that right now.
[1:04] What we want to do is, first of all, close Houdini so that these updates will take effect.
[1:09] And let's open up our file explorer here.
[1:12] Head on over to the documents section.
[1:15] Houdini 20.
[1:16] And this is what we want to touch right here.
[1:18] Our Houdini.env file.
[1:20] This is the environment file.
[1:21] Houdini will look at this every time it opens up.
[1:25] So take a moment to look at the syntax here.
[1:27] Syntax basically is like specifics of coding language, like the specific characters used,
[1:33] so to speak.
[1:34] What you can notice right away is that there's a lot of hashtags.
[1:37] Hashtags in an environment file in Houdini basically mean, hey, yo, don't run me as code.
[1:42] My G. Instead, just look at me as like a bit of text for the user to read.
[1:49] Right?
[1:50] I'm not supposed to be run as code.
[1:51] Coding without a hashtag will be run as if it is supposed to be code when Houdini launches.
[1:58] So what we want to do is we want to add the command in here to say, hey, middle mouse
[2:02] button should not be equal to pan.
[2:05] We don't want that.
[2:06] Now, encoding will go into this in a lot more detail later, but encoding, there are true
[2:10] statements and false statements.
[2:12] True is one, false is zero.
[2:14] So what we want to say is, hey, this middle mouse button, it being pan, yeah, that's equal
[2:19] to zero.
[2:20] That's not true.
[2:21] I don't want that to be true in my world.
[2:23] Now I've already got it copied here, but this is what you want to type all uppercase Houdini
[2:28] underscore middle mouse button underscore pan space equals space zero control S to save
[2:34] that.
[2:35] Okay.
[2:36] So now we're into Houdini, right?
[2:37] And there's a lot going on in this interface, right?
[2:39] It's a little bit overwhelming at first.
[2:41] So I just want you to focus on these three main pains.
[2:44] We've got right here, the scene view we've got over here, the network view.
[2:49] This is where all your nodes are going to live.
[2:50] And then over here, we've got the parameters.
[2:53] These parameters will be associated typically with anything that you are highlighting node
[2:57] wise.
[2:58] So you highlight a node, you see the parameters there.
[3:00] And we'll go ahead and drop like a test geometry here just to explore it a little bit.
[3:04] If you hit tab, click on the OBJ section, click on the, click on the network view section,
[3:10] hit tab and type sphere.
[3:15] Now you'll see if you can actually navigate these with the arrow keys here, just up and
[3:19] down, but there is sphere polygons and sphere primitive.
[3:22] You'll see this a lot in Houdini and we'll go in, we'll go into it more in the future.
[3:27] But just know that these are basically just different variations of the same thing.
[3:31] It's like kind of like a preset up for you.
[3:33] We want to work with polygons right now.
[3:36] So let's go ahead and just highlight this and hit enter.
[3:39] Now you'll see it's still a gray little ghost box.
[3:41] It hasn't actualized yet.
[3:42] You have to click in order to drop that down.
[3:45] So we've got a sphere.
[3:47] Now we've got something in the scene.
[3:49] That's great.
[3:50] Let's quickly go over navigation.
[3:52] Now we went over this a little bit for the node view, but if you hold alt and right mouse
[3:56] button, you pan, if you hold middle mouse button and all you zoom and you highlight
[4:02] if you left mouse button click in the scene view, if you're hovering over this and you
[4:06] hold alt left mouse button will rotate around, middle mouse will zoom in and out.
[4:11] You can also scroll that in and out and the right mouse button will pan.
[4:15] Right.
[4:16] Those are the main ways of navigating inside of the scene view.
[4:19] You'll also see that once we had this created, we got some parameters to play with.
[4:25] Now what if we got here, we've got translate, rotate, scale, pivot, translate, all those
[4:29] fun things that we want.
[4:32] Right out the gate, a very helpful thing to do is if you hold, if you hover over any parameter
[4:37] box and you hold the middle mouse button, you will get this very interesting collection
[4:43] of numbers.
[4:44] As you can see, it's point one, point, oh, one, point, oh, one, point, oh, oh, one, and
[4:49] then it ascends one, 10, 100.
[4:51] Basically whatever you hover over here, when you scroll to the left or right, that's how
[4:56] much it moves incrementally.
[4:58] So if you want to move it a bunch, we'll do one.
[5:00] You can see by sliding left and right, I go to point one.
[5:03] I'm moving it less.
[5:04] This is just some detailed control over how to navigate your parameters.
[5:08] You can also just double click and put in point one or something like that.
[5:13] These parameters work for the full object.
[5:16] You can see we're scaling the X, Y, and the Z where you won't see the rotation, maybe
[5:20] just a little bit.
[5:21] We're rotating there.
[5:23] Now we've got uniform scale as well.
[5:25] All of these parameters are controlling this overall object.
[5:32] But what is this object?
[5:34] We're looking at this object.
[5:35] You look at me and you see a person, just a big old skin wrapper.
[5:40] But underneath that layer, that top layer is what actually is making me me.
[5:46] It's the internals that makes it all possible.
[5:48] You can actually go inside these nodes, just like you can go inside me, which hopefully
[5:54] no one does in my lifetime.
[5:56] If we double click this, we have now entered that geometry.
[6:01] This is what is making it up.
[6:02] We can see there's a sphere node in here as well.
[6:05] Look, this has its own set of parameters.
[6:08] But inside of here, there can be anything.
[6:10] This is what comprises the overall object.
[6:13] If I hit tab and I type cube and hit enter and then click it down, I now have a box.
[6:20] We'll go over these flags in a minute, but if you just click the little blue flag on
[6:24] the right, you can switch between what we're actually seeing.
[6:28] If we pop back up to the top by clicking this OBJ section of the network view, then we pop
[6:34] back up and we can see the box is now actualized because that is what is flagged is going on
[6:39] on the inside.
[6:40] So it's this idea of contexts.
[6:44] And again, we'll go into that also in more detail.
[6:47] I just want to give a real top level overview of this understanding.
[6:51] So OBJ, the object level of your scene.
[6:54] This is the scene, like this is the most macro perspective of your scene.
[7:00] This is the top level where you'll have your sphere and I'll type test geometry and navigate
[7:06] down to rubber toy and just click that too just for the sake of this illustration.
[7:10] I'll move him back on the Z and I'll zoom out a little bit.
[7:13] But we'll have our different geometries that are interacting.
[7:17] And then you may have a light in your scene.
[7:23] You'll have a camera in your scene that you're looking through.
[7:26] You'll have all of these things on this top level, this OBJ level.
[7:29] So we'll be here a lot and we'll be organizing this a lot because this is the thing we have
[7:33] to really keep clean.
[7:35] But inside of these geometry nodes, this is where the objects get built.
[7:42] So if we hit tab and type in merge and combine both of these things and then hit that blue
[7:48] flag, let's highlight the sphere and just scoot it back a little bit.
[7:53] You'll see that we have two things now that both appear and disappear when we type sphere.
[7:59] So you build the characters, you build everything inside of these geometry nodes.
[8:02] I hope I'm not over explaining, but obviously first time in Houdini, like these are important
[8:07] aspects to keep in mind.
[8:09] So I just want to make sure I'm very clear with that.
[8:11] This is the OBJ level.
[8:13] And then if you double click, this is what's called the Sop context.
[8:17] You'll hear something up all the time.
[8:20] This is mop top, Vop, Pop, Sop, Dopp.
[8:24] You'll hear it all the time and we'll explain what those are.
[8:26] But Sop is short for surface operator.
[8:30] This is where we operate on what eventually becomes the surface of our overall object.
[8:35] That's how I like to think of it.
[8:36] Also to show you that inside the surface operator level, the Sop context, there are different
[8:43] controls.
[8:44] If you look at the sphere, let's delete everything, highlight and just delete everything else
[8:48] but this.
[8:49] If we look at the controls on the OBJ level, um, now real quick side note, you double click
[8:55] to go in, you click to go out, but you can also highlight something and press the I key
[9:00] to go in and the U key to go up one level.
[9:04] That's the way I like to think of it.
[9:05] You're going in one level or you're going up one level.
[9:07] So I, you, right?
[9:10] Maybe you prefer that.
[9:11] But if we go to the top level, right?
[9:12] The object level and we look at the parameters here, we've got simple things, translate,
[9:17] scale, pivot, but nothing that, that we can use to actually change the shape of this object.
[9:23] If we go inside the Sop level though, now all of a sudden look, we see our wire, we
[9:27] see our wireframe better.
[9:30] We have a lot of controls over like the radius, kind of like we did on the top level, but
[9:33] these are different, right?
[9:35] The center of where it is, the radius, but there's also things like, look, rows and columns.
[9:39] This is where we can kind of add polygonal definition to our overall mesh.
[9:45] We can also change the primitive type to polygon or primitive, which was again, remember one
[9:50] of those options on the top level where instead of there being polygons, there's really just
[9:55] one point in the middle of this thing, right?
[9:58] So it's simplified geometry.
[10:01] Lots of flexibility inside this level, but it's also where if I take a certain point
[10:09] and I want to do some transformations, I can do all that inside of here, right?
[10:14] I can totally change the shape of this thing in any way that I want.
[10:20] I can destroy it so that it's hideous to look at and go back up to the top level and go,
[10:24] hey, yeah, this is still my sphere, right?
[10:26] We can also add animation inside of that as well.
[10:29] So all of those things take place inside the Sop level.
[10:31] Now don't worry if this isn't making total sense.
[10:33] It's okay.
[10:34] This entire section actually, it's okay if it doesn't make total sense, right?
[10:38] We're just laying the foundation for what we're going to do later and it'll all make
[10:40] sense as we go, I promise.
[10:42] So we've got this hideous deflated monstrosity.
[10:46] It's perfect.
[10:47] But we want to go ahead and navigate around it.
[10:49] Now we did cover that a little bit, right?
[10:51] Holding all left mouse button, holding middle mouse button, holding all and right mouse
[10:55] button.
[10:56] You can do all the different things you want to do.
[10:58] But these are known as perspective views, right?
[11:01] They're the perspective, but sometimes we want orthographic views.
[11:04] You can think of an orthographic view almost as an infinite focal length, right?
[11:09] The longest lens in the world.
[11:11] Everything is completely flattened.
[11:12] There is no perspective.
[11:13] You know, if we get close to this, right?
[11:16] This portion feels closer than this feels because of the perspective of it.
[11:20] But if we hold space and two, we get a top view that is orthographic where everything
[11:27] is flattened basically.
[11:28] It's a perfect top view of our scene.
[11:31] If we hold space and two again, now we get a view of the bottom.
[11:35] Now note that you do have to click into the scene view in order for this to work.
[11:39] If you click in here and hit space one, it's going to do something completely different.
[11:44] So this is context based.
[11:46] Keep that in mind.
[11:47] So click over the scene view, hit space one to go to the perspective view, which again
[11:52] we can navigate around, hit space bar two to go to the top, hit space bar two again
[11:57] to go to the bottom.
[11:58] You can pop back and forth between these.
[12:01] If you hit space bar and three, now you can go to the front or the back of your geometry.
[12:07] Take a nice good look at that.
[12:09] If you hit space bar on four, it's right and left.
[12:12] So you got perspective view, top bottom, front back, and right and left.
[12:16] And you can actually see that right here.
[12:18] We're getting it right here.
[12:19] So we can just click this dropdown as well, go to set view and pick the one that we want.
[12:25] Now what the heck is this?
[12:26] What is the UV viewport?
[12:28] Well, if you hold space bar and hit five, you will enter the UV viewport.
[12:33] If you know nothing about texturing, no worries at all.
[12:36] We will be going into detail on that.
[12:38] But this is where your UV lives, right?
[12:40] This is where we will edit our UV or specify our UV once it's set up.
[12:46] Now this geometry doesn't have any UVs.
[12:49] If I hit tab UV texture, I got to go into it.
[12:53] What am I, a rookie or something?
[12:54] If I hit tab and go UV texture, now we have the UVs.
[13:00] This may look like gobbledygook and that's okay.
[13:02] But point is holding space bar on five will take you to the UV view, which is good to know.
[13:07] So one, two, three, four, five.
[13:11] Very, very handy.
[13:12] Now, I mentioned earlier this blue flag, right?
[13:14] This is important on this level.
[13:16] It's either on or off.
[13:17] That's the display flag, so to speak.
[13:19] So you either turn it on or turn it off.
[13:22] If you go inside of it though, we've got more flags.
[13:24] And if you actually hover over the node, you'll see these icons appear around it, right?
[13:31] If you hover over it long enough, it'll actually give you some text to know what it is.
[13:35] Like if you see this one is bypass, this is node info.
[13:39] This one is lock.
[13:41] This one is a template mode and this one is display.
[13:45] These are the exact same as these buttons right here.
[13:47] You can kind of see them get highlighted when I hover over them, right?
[13:51] The blue flag, the primary flag is the display flag, whichever node has the blue flag checked
[13:58] is the one that we are going to see.
[14:00] We will see that.
[14:01] Let's turn this down.
[14:02] This is too ugly even for me.
[14:05] Let's turn that down.
[14:07] Okay, that's a little bit less ugly.
[14:10] But yeah, whatever the blue flag is on is the one that we are going to see, right?
[14:14] Do this one.
[14:15] We can see this.
[14:16] We do this one.
[14:17] We can see this.
[14:18] And in that way, you can navigate through the stages of your geometry, right?
[14:21] Very, very helpful.
[14:22] Now, another option is the template mode.
[14:27] It's the purple flag here.
[14:28] Since this is displayed already, the purple flag doesn't do anything.
[14:32] But if I click the purple flag on a different one, look, we get the wireframe version, right?
[14:37] The templated version of the next step in the process.
[14:41] So we can essentially get an overlay here.
[14:43] We can display one thing and we can get the overlay of the other, right?
[14:48] That's handy in many circumstances.
[14:51] If we create a box here, let's say we want to wireframe this next step, but we also want
[14:58] to wireframe something else.
[14:59] How do we do that?
[15:00] First, we hold control and click on the purple flag.
[15:04] First it will turn a deep purple and it will actually show the entirety of the object,
[15:09] right?
[15:10] If you hold control and click it again, it'll go to wireframe mode.
[15:14] But now we have two wireframe modes active.
[15:16] You can activate, I think, as many purple flags as you want, which is really handy, right?
[15:21] Turning on as many as you want so you can visualize everything you need to when you're
[15:24] seeing all at the same time.
[15:25] But note that you can only have one deep purple flag active, right?
[15:29] It's a secondary, basically fully opaque piece of geometry.
[15:35] So we've got the purple flag.
[15:37] We've got the blue flag.
[15:38] Now, if you have multiple purple flags active, just be aware that by simply clicking, not
[15:43] with control, just left clicking on any purple flag will set it to be the only one that's
[15:47] active, right?
[15:49] You can mess around with that.
[15:51] We've also got the lock button.
[15:52] I almost never use this button, right?
[15:54] We click this.
[15:55] It doesn't seem to work.
[15:56] I don't know why, but if we click the little frost icon, we can freeze that.
[16:01] It's like freezing your credit for you oldies out there who know what I'm talking about.
[16:07] Once you do it, making any changes at all will have no effect.
[16:11] Same two for anything that comes before it, right?
[16:13] Because Houdini's procedural, it works trickle down style.
[16:17] If this is frozen, it doesn't matter what you change.
[16:20] Nothing will be updated.
[16:21] This is a dangerous node, right?
[16:22] This is something to be aware of.
[16:24] Because if you have this toggled on and you make a bunch of changes, you don't know what's
[16:27] going on and you move on.
[16:28] When you eventually do and you uncheck it, let's say I make changes, I eventually unfreeze
[16:33] it.
[16:34] It's going to say this operation will discard the locked changes.
[16:37] I say, okay, boom, everything updates.
[16:40] All the mistakes I made in my past, you know, come to the forefront, right?
[16:47] And we don't want that.
[16:48] We don't want that.
[16:49] So I almost never use this node, but know that it's there, right?
[16:52] If it's working for your workflow, then it's the right answer for you and that's great.
[16:56] The other flag to be aware of is the bypass flag here.
[17:01] That is at the very end.
[17:03] I typically just click this arrow button.
[17:04] It's easier for me.
[17:06] But it basically says, hey, skip this node, right?
[17:10] So if we've got a node chain of events that's going through, we just toggle that to bypass
[17:14] that particular node.
[17:17] Helpful in a ton of different circumstances.
[17:19] You can also highlight the node and just press B instead B for bypass, which is helpful.
[17:25] Now the other flags too have shortcuts.
[17:28] If I highlight this and I hit R, that will put the display flag on it.
[17:32] If I hit E, that will put the templated flag on.
[17:35] So I can highlight this box.
[17:36] I can press E, this box, press E, and of course B as well.
[17:41] So, you know, it depends what kind of stuff you want to do.
[17:43] I don't typically use the shortcuts myself.
[17:45] I just click the flag.
[17:46] I'm old school like that.
[17:49] But either way, super handy, super helpful.
[17:51] And then the last one here is the information, right?
[17:54] Houdini is built on information.
[17:56] That's stuff that we will go super deep into as we move on in the process here.
[18:01] But by clicking on this node info button, you get a little pop up right here.
[18:06] And this is basically the summation of what this node is, how it's comprised.
[18:12] You can see how many points are on the geometry.
[18:14] You can see the, how many primitives are on, how many vertices, how many polygons total.
[18:18] You can see the center of the object in world space.
[18:21] You can see the minimum and maximum point position of the object.
[18:25] You can see its total size.
[18:27] You see all sorts of information as well as all the attributes that it has that we'll
[18:30] get into later, right?
[18:31] So this is very handy as well.
[18:33] If you click it, it pops up and it stays.
[18:36] You can also middle mouse button, click and hold on the node in order to actualize that
[18:41] same information, right?
[18:42] If you don't want something permanent, you just want to check it out real quick.
[18:45] You can just click and hold that.
[18:47] And that's great too.
[18:48] So yeah, one more time real quick.
[18:49] It's display flag, template flag, freeze flag, bypass.
[18:54] And then there of course is the information that you can toggle on as well.
[18:58] All super handy in different circumstances and who do you.
[19:01] If you enjoyed this video and you want to learn more, head to doublejumpacademy.com slash
[19:06] Jordan for the full course.
[19:08] Links in the description.
[19:09] You just click away.
[19:10] Click it.



---

## Captured Frames

- [0:20] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_000.jpg
- [1:18] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_001.jpg
- [2:44] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_002.jpg
- [3:39] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_003.jpg
- [4:56] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_004.jpg
- [5:56] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_005.jpg
- [6:47] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_006.jpg
- [8:13] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_007.jpg
- [10:20] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_008.jpg
- [11:20] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_009.jpg
- [12:33] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_010.jpg
- [13:45] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_011.jpg
- [15:09] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_012.jpg
- [18:06] tutorials/frames/houdini-for-beginners---part-2-navigation/frame_013.jpg

---

## Structured Notes

### Core Technique
Foundational UI/navigation orientation for absolute beginners: default camera controls (and how to remap them via `houdini.env`), the three main interface panes, the OBJ vs. SOP context distinction (and the I/U keys to move between them), the five orthographic/UV view shortcuts, and the node-flag system (display/template/lock/bypass/info) that controls what you actually see and how nodes chain together.

### Summary
**Navigation defaults:** Alt+LMB-drag rotates around the object; by default Alt+MMB pans and Alt+RMB zooms, which the presenter finds backwards (they zoom with scroll wheel anyway) and prefers swapped. To remap: close Houdini, open `Documents/houdini20.x/houdini.env` (the environment file Houdini reads on every launch — lines starting `#` are comments, ignored as code; anything else is parsed as a setting), and add the line `HOUDINI_MIDDLE_MOUSE_BUTTON_PAN = 0` (uppercase, `=` with spaces, `0` = false/off) to disable middle-mouse-pan, then save and relaunch. The same Alt+drag scheme also applies inside the network (node graph) view, not just the 3D scene view.

**Three main panes:** the **Scene View** (3D viewport), the **Network View** (where nodes live — press Tab inside it to search/place a node, e.g. typing "sphere" and choosing the polygon variant over the primitive variant, then clicking to actually place the ghosted preview), and the **Parameters** pane (shows parameters for whatever node is currently selected/highlighted). Hovering any numeric parameter field and holding the middle mouse button reveals a horizontal scrub strip of increment sizes (0.001, 0.01, 0.1, 1, 10, 100...) — scrubbing left/right on that strip picks how coarsely/finely the value changes; double-clicking a field also allows direct numeric entry.

**OBJ vs. SOP context:** the top/object level (**OBJ**) is the "macro" scene — where whole objects, lights, cameras live and get positioned/scaled/organized relative to each other, but has no controls to actually reshape geometry. Double-clicking an object (or selecting it and pressing **I**) drops down into its **SOP** ("Surface Operator") context — the node network that actually builds/deforms that object's geometry; pressing **U** goes back up one level. Inside SOP, the same sphere gets real shape controls (radius, rows/columns polygon density, primitive-type toggle, point-level edits, etc.) that don't exist at the OBJ level — the OBJ level only ever shows whichever node inside has its **display flag** (the blue flag) turned on. Multiple objects/geometry networks can be merged together inside a single SOP network (demoed with a `merge` node combining a sphere and a cube).

**View shortcuts (must click into the Scene View first — these are context-sensitive, same keys do something else if focus is in the Network View):** `Space+1` = perspective view (free navigation), `Space+2` toggles top/bottom orthographic view, `Space+3` toggles front/back, `Space+4` toggles right/left, `Space+5` = UV viewport (where UVs are edited once a `uvtexture` node or similar has generated them — geometry has no UVs by default). These are also selectable from a "Set View" dropdown in the viewport.

**Node flags:** on a node, hovering reveals icon toggles matching buttons in the toolbar: **Display flag** (blue) — determines which single node's output is what OBJ level (or downstream) actually sees; only one can be active per network in the simple case. **Template flag** (purple) — overlays a node's geometry as a wireframe on top of whatever is currently displayed, without making it the actual display node; Ctrl+click cycles a node's template flag through off → wireframe-overlay → solid "deep purple" (fully opaque secondary geometry, only one node can be deep-purple at a time) → off; multiple nodes can have the plain wireframe template active simultaneously, but a plain (non-Ctrl) click on any template flag clears all others and sets only that one. **Lock/freeze flag** (snowflake icon) — freezes a node's output so no upstream changes propagate through it (Houdini is procedural/trickle-down, so this can silently mask a lot of in-progress work); unfreezing prompts a "this will discard locked changes" warning and everything recalculates at once — the presenter says they almost never use this but flags it as something to know about. **Bypass flag** (arrow icon at a node's end) — skips that node in the chain entirely, keyboard shortcut **B**. Display flag keyboard shortcut is **R**, template flag is **E**. **Node info** — click the info icon for a persistent popup (point/primitive/vertex/polygon counts, world-space bounding box center/min/max, size, attribute list), or middle-mouse-click-and-hold on a node for the same info as a temporary popup that disappears on release.

### Key Steps
1. (Optional) Remap Alt+MMB/Alt+RMB pan-vs-zoom by editing `houdini.env` (`HOUDINI_MIDDLE_MOUSE_BUTTON_PAN = 0`) while Houdini is closed, then relaunch.
2. Learn the three panes: Scene View, Network View (Tab to add nodes), Parameters (reflects the currently selected node).
3. Understand OBJ (macro scene, no shape controls) vs. SOP (per-object geometry-building network, entered via double-click or **I**, exited via **U**) — only the node with the display (blue) flag on is what's actually shown/passed up.
4. Use `Space+1` through `Space+5` (with focus in the Scene View) to jump between perspective, top/bottom, front/back, right/left, and UV viewport views.
5. Use the display (blue/R), template (purple/E), lock/freeze, and bypass (B) flags to control what's visible, overlay reference geometry, freeze a node against upstream changes, or skip a node in the chain.
6. Use a node's info icon (click for persistent, middle-click-hold for temporary) to inspect point/primitive/vertex/polygon counts and bounding-box data.

### Houdini Nodes / VEX / Settings
`sphere` (polygon vs. primitive type choice), `cube`, `merge` (combining multiple geometry streams in one SOP network), `mountain` (displacement noise, used here just to produce an example deformed/"hideous" shape for demonstrating navigation and flags — not explained in depth in this video), `uvtexture` (generates UVs so the UV viewport, Space+5, has something to show). `houdini.env` environment-variable file (`HOUDINI_MIDDLE_MOUSE_BUTTON_PAN`). Node flags: display (blue, shortcut R), template (purple, shortcut E, Ctrl+click for solid/deep-purple mode), lock/freeze, bypass (shortcut B), node info (click or middle-click-hold).

### Difficulty
Beginner — pure UI/workflow orientation, no procedural-modeling technique taught in depth (the sphere/mountain/UV examples are just visual aids for demonstrating navigation, not a tutorial on those nodes themselves).

### Houdini Version
Houdini 20.x referenced explicitly (the `houdini.env` file path shown is `Documents/houdini20.x`); presenter notes the node-info popup's visual styling has changed in newer versions but the underlying functionality is the same.

### Tags
beginner, navigation, ui-basics, houdini-env, obj-context, sop-context, display-flag, template-flag, bypass-flag, node-info, orthographic-views, uv-viewport, jordan-allen

---

## Related Tutorials
None yet in this library on Houdini's basic navigation/UI mechanics — first entry in the "Houdini for Beginners" series covering this.
