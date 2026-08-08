---
title: Houdini for Beginners-  Part 4:  Tools
source: YouTube
url: https://www.youtube.com/watch?v=ClPDNCDMCBE
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-for-beginners--part-4-tools/
frame_count: 0
frame_status: pending-selection
---

# Houdini for Beginners-  Part 4:  Tools

**Source:** [YouTube](https://www.youtube.com/watch?v=ClPDNCDMCBE)
**Author:** Jordan Allen
**Duration:** 13m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-for-beginners--part-4-tools <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] We have gone over selection. That's great. Pocket that away in the back of your brain.
[0:05] Now let's go over moving things, transformation, right? That all takes place utilizing this right
[0:11] here. It's called the show handle. I call it the transform tool. I don't actually know if that's
[0:16] the actual name for it, but I do use it all the time. So if I ever say the transformation tool,
[0:22] this is what I mean. In select mode, we can pick whatever we want. Now we can move things
[0:27] in the parameters window here. We can rotate them, scale them as we looked at before in an
[0:31] earlier lesson here. But what if we want to do that in a more interactive way? We want to do that
[0:37] on screen. Well, by clicking the show handle, it is going to, believe it or not, show us the
[0:43] handle. You can move on all the different axes, the X, the Z, the Y, you can move it two at a time.
[0:49] You can move it all three. You can rotate. You can drag one of these up top and rotate on two
[0:54] different axes. Like all the different transformations you'd hope to see that just make for a much more
[0:58] interactive experience. Now quick side note, this underneath here, this section of magnets,
[1:03] these are the snapping tools. I'm not going to go into them too much. Just be aware,
[1:07] make sure this is not on because what you'll get is a very strange situation where it's trying to
[1:13] snap it to the ground plane when you're moving it around your scene, right? Which gets for weird
[1:18] results, right? It's trying to snap it. It's causing all sorts of problems. So if you're having like
[1:22] weird glitchy issues dragging it around, it's probably some of the snapping tools that are active,
[1:27] although I don't believe they're active by default. So you may be fine. These are the same
[1:30] transformations, by the way, that you're seeing in your parameters. So it just depends how you
[1:33] want to do it. Calling it the handle node is a little disingenuous, even though it's that's
[1:36] its legal name, it's its birth name. Because the handle tool is very important. You are basically
[1:42] going to live between the select tool or the handle tool. The handle tool needs to be active in order
[1:47] to use any sort of interactivity with any node, right? Without it being on, you will not see the
[1:54] important things, the essentially the handles, I guess, that you need to interact with in order to
[2:00] make changes, right? I'll give you an example of that that makes a little more sense. If we go into
[2:04] the sphere here, the sphere by default, you can see there's a box around it. If we're in select mode,
[2:09] we're selecting our points, we're selecting our faces, etc. If we're in transform mode,
[2:14] we've got our handles, which we might expect, but we also see this bounding box. You see, each
[2:19] node that we create is designed differently. At the end of the day, each node is basically just a
[2:24] collection of code that's been built up with a nice wrapper on it for us to access. The creators
[2:28] of these nodes have designed tools that are interactive for us in the viewport. Those tools
[2:35] are only visible if the handle tool is active. If you are in select mode, take this, for example,
[2:42] the sphere node by default gives you interactivity, not only to rotate it and transform it, but it
[2:48] also wants you to be able to scale it in different ways, holding shift to scale both sides, top and
[2:53] bottom, you know, if you want to make these scale changes, but you have the select tool active,
[2:59] you can't do that. There's no way in order to see the tools that are accessible in this node,
[3:06] you must have the handle active. So to further illustrate this point, let's create a different
[3:11] type of node entirely. We're going to hit tab and type in clip. If we shift enter, it will create
[3:17] it and attach it to the node we had highlighted earlier. The clip works, well, exactly as advertised,
[3:23] it clips the geometry, right? It starts by default clipping on the y-axis, anything that is below,
[3:29] which you can see in the parameters here, it says keep primitives above the plane,
[3:33] and then it shows you the plane. If we're in select mode, though, you're not seeing anything,
[3:37] right? You have no access to the tools that the designers of the clip node built in for you to
[3:43] access and work with. So if you ever don't see the tools and you have the node selected, you're
[3:46] going, what the heck is going on? It's because the handle tool is not selected. The minute that you
[3:50] hit the show handle tool, now you have access to what they designed. You'll notice the handle on this
[3:56] is not the handle that you see in the sphere node, right? If we highlight the sphere node,
[4:01] we've got a traditional handle. We've got the rotation, the positional shifts. Now we do have
[4:05] this box, which is not traditional, but this is also in a way a handle. It's the custom handle
[4:10] for this node in order to interact with it and make changes as you want to change it. So we see
[4:15] in this scene view window, now we see this ground plane visualizer and this that we can
[4:23] use to rotate or we can use to drag it up. We can make changes interactively. We can also make
[4:30] changes obviously in here, but this is more interactive. This is more artist friendly, so to
[4:36] speak. You'll also occasionally get popups on screen. Like we can see clip distance here
[4:41] that we can click and drag as well. More interactivity. So we've got interactivity in the viewport.
[4:46] Now let's hit tab and type in UV flatten. Don't worry about this node at all, but drop that down
[4:52] and look with the select tool active, you are again able to select geometry as you might expect
[4:56] with the handle tool active. It changes the entire interface because again, this is what
[5:02] the designers of this node want to set up for you in order to interact and interface with this
[5:08] particular node. You've got a change to the actual interface itself, but you've also got
[5:13] additional parameter tools above the scene view, right? These disappear when I switch between nodes.
[5:20] Now speaking of handles, we've got our handle tool active. We want to make changes. We've got the
[5:25] big handle here, but what if we only want to make changes to the translation or just to the
[5:30] rotation or just to the scale? Let's say this is a bit finicky and we don't like to deal with that.
[5:34] If we hit T as a shortcut, that will give us our translation handle. R will give us our rotation
[5:40] handle by itself and E will give us our scale handle by itself, which is maybe just a little
[5:46] nicer to interface with. Just remember that E for scale, R for rotation and T for translation.
[5:52] We've covered selection. We've covered transformation. We haven't really talked too much about
[5:57] creating nodes, right? I've shown you the tab approach, but there are many other ways to do
[6:01] that same thing. But first, a little bit of context here. Context being literally the perfect word
[6:06] because there are lots of different contexts in Houdini. What I mean by that is the OBJ level
[6:12] is different than the SOP level as we've talked about, right? Surface operations,
[6:16] it's where we do all our things to build our object. Then the object level is where we kind of
[6:20] set our scene and our light and our camera and all that good stuff. Different contexts exist as
[6:26] organizational boxes for different activities, right? We've only covered two so far, the object
[6:32] level and the SOP level. But one important thing to note is that the context dictates what nodes
[6:37] are available because nodes are designed to work on different things. And in order to work on those
[6:42] specific things, they have to be in that specific environment. So for example, if you click on the
[6:47] network view while in the OBJ level and you hit tab, you will get a list of all the different
[6:53] subcategories of nodes that exist inside of this context. Now you'll notice there's a lot,
[7:01] but not that many, right? You'd expect to see more than this. Well, that's because these are only
[7:07] the nodes that work on this level in this context. If you create a geometry node, this is going to be
[7:14] an empty shell and we double click to go inside of it and then you hit tab in there. Well, now look,
[7:20] we've got whole new worlds of nodes and possibilities, all of these designed to work on the surface,
[7:27] essentially, of the object. Now, just so it's covered, there are plenty of different contexts.
[7:33] If you click and hold on this little icon by the OBJ here, you will actually see that there's lots
[7:37] of different contexts. And each of these will take you into its own little world inside of which
[7:42] there are new unique nodes to use. We will eventually traverse the majority of these,
[7:48] but for now we're going to stick to the OBJ level and a subset of the OBJ level, which is the SOP
[7:53] level, right? Let's highlight and delete the sphere and let's say we don't want to hit the
[7:57] tab method in order to create it. We want something different. Well, up at the top left, there is what's
[8:03] called the create tab and here we'll find, oh, look, a sphere. If we click on this now in our
[8:09] interface, we have a more interactive way to create a sphere. By clicking sphere, it still
[8:15] hasn't created the actual sphere yet. We can pick where in the world that should be. If we hover
[8:20] over here and click, it will realize it in that location in 3D space. If we want it in the middle,
[8:25] we can click and just hit enter and it will create it at the exact center of our world. What's known
[8:30] as world space? The zero, zero, zero of our world. X, Y, Z, zero. I'm done saying zero now.
[8:39] Point is we've got our sphere and the internals are the exact same, right? So we hop back up here.
[8:45] We can see it has created our sphere. There's also another way. If you click on the scene view,
[8:50] again, just a reminder for the names here, we can see scene view on the top left of this tab. So
[8:54] this is how we know this is the scene view. But if we click on the scene view and hit C, essentially
[8:58] create, it will open up a radial menu that we can use in order to create a sphere. Now here,
[9:05] we've got a lot of different options for a lot of different use cases, but I know we want to create
[9:09] geometry and we want to create a sphere. So we click and look, we're right where we left off.
[9:16] If we hit enter, we've created it at the center of our world again. So there is the tab method.
[9:21] There is the shelf method and there is the radial pop-up method. Now it is worth noting,
[9:30] you know, we're dealing in creating geometry, but this is really more about creating nodes than it
[9:35] is creating geometry as we know it. Because if we explore this top shelf area, there's lots of
[9:40] stuff going on. Look, we can create box, sphere, tube, we can create a null, line, spray paint,
[9:45] so many different things. If we move over to the modify tool, which is, believe it or not, for
[9:50] modifying geometry, well, look, we've got very helpful nodes like a duplicate node
[9:54] or a copy to points node that we'll look at later. A delete node, we can affect the model
[10:00] directly if you want to sweep along a curve or you want to scatter onto geometry, you know?
[10:05] All of these tabs contain different tools that are the exact same tools that you can create if you
[10:12] are in the right context hitting tab and typing it in. This is more for, if you can't remember the
[10:17] name of something, this tool is here with helpful icons that will help you. I personally do not use
[10:22] this very often, but I want you guys to know this is here in case you need it, right? There's also
[10:26] this little plus icon at the bottom. These are the shelves that are not shown by default. But for
[10:32] example, I have a grayscale gorilla tool installed that I like to access every once in a while. So
[10:36] if I click this, it's going to actualize that shelf tab for me. So in this way, I can customize my own
[10:42] shelf to be more useful to me. Now, since we're already in the attic exploring the shelves,
[10:48] why don't we mosey onto the right? This is what I call the danger zone over here. A lot of these
[10:53] tabs contain final results. If we click flip fluid from object in this tab in the particle fluids tab,
[11:00] nothing happens. But what we do get in the scene view at the bottom here in blue text,
[11:06] an option to select object to convert into a flip fluid, press enter to accept the selection.
[11:13] So we can now pick our object. I'll click on this sphere and it says to hit enter. Okay, I'll hit
[11:19] enter. And what it does is creates an entire series of nodes. It creates an entire setup to
[11:29] create flip fluids. So the final thing that we get, I'm going to turn off the grid here for
[11:34] visibility. But the final thing that we get is look, it's a simulation of particles, right?
[11:39] It has set up all these nodes for us and these systems for us
[11:44] in order to create a flip fluid simulation. Now on the surface, that sounds great, right? It's like,
[11:51] oh, yeah, shortcut. Get it out of your brain. I want to show you the gun safe so I can lock it
[11:57] in front of you and say you were not allowed in there yet. You're too young. We are going to
[12:02] unlock this section at the very end of the tutorial series. The reality is you should know
[12:07] how the sausage gets made. Okay, so every branch of Houdini that we explore, I want you to understand
[12:13] the fundamental building blocks that go into that specific thing before you touch the shelf tools.
[12:19] The shelf tools really are useful when you are able to dive in and explore how these things are
[12:24] constructed because at that point you will already have the knowledge you need to make the tweaks
[12:28] necessary to actually make a useful system. Right out the gate, you are not going to know
[12:34] what does what and it's all going to be overwhelming and ugly and lonely. Speaking from experience,
[12:39] by the way, so I want to make sure you are trained up before entering this area of the dojo. For me,
[12:44] I like to keep it simple. I don't use the radio menu. I don't use the shelf tools.
[12:48] I just hit tab and I type what I want or God forbid if I forget, I do venture up into the shelves
[12:53] to the area and I find something that will jog my memory. Besides that, I tend to stay away from
[13:00] the shelf tool area. I just want you to know that that's there. If you enjoyed this video and you
[13:04] want to learn more, head to doublejumpacademy.com slash Jordan for the full course. Links in the
[13:09] description. You just click away, click it.



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
