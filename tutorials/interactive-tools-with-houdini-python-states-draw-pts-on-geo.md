---
title: Interactive Tools with Houdini Python States | Draw pts on geo
source: YouTube
url: https://www.youtube.com/watch?v=ARJFJC79k3k
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [python, hda, procedural, tips, advanced]
extraction_status: complete
frames_dir: tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Interactive Tools with Houdini Python States | Draw pts on geo

**Source:** [YouTube](https://www.youtube.com/watch?v=ARJFJC79k3k)
**Author:** cgside
**Duration:** 32m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] I will go on and welcome back.
[0:03] So in today's video I talked about doing something a bit different, which will be on how to
[0:09] create a tool like this that you can place points, drag points and remove them.
[0:15] So this is the tool we will be creating using Python states.
[0:20] It's like a custom HDA that I've used before in the channel and hopefully you'll get
[0:24] away with some tips.
[0:27] So yeah, let's get into it.
[0:29] So let's actually get started creating the tool and we will try to do this step by step.
[0:35] And I'm not a specialist, so this might go a bit slow as I'm a bit rusty on this, but
[0:40] let's try to do it.
[0:41] So first of all, I'm going to create an ad note.
[0:44] So this will be the multi entry of the points that we will create and we will connect it
[0:48] right away to this input geometry, this test geometry, press shift C to create a subnet.
[0:54] I'm going to name it draw points demo.
[0:58] And right away I'm going to create the digital assets.
[1:01] This can be like this, create and I'm going to interactive and I'm going to make use of
[1:08] a template, which is the endpoint.
[1:11] And I'm also going to create some draw balls.
[1:14] So I'm going to make sure I enable on draw and also on these handle states because I'm
[1:22] going to make use of them.
[1:23] So at point the handle states and on draw.
[1:26] That's accept and I'm going to go into the parameters and dragging these ad nodes.
[1:33] So these parameters in here.
[1:36] And that should be fine.
[1:37] Let's press accept.
[1:38] And now if we enter the tool, so by clicking on the state and as I can see, it's drawing
[1:44] the points, but we don't want to draw the points.
[1:48] And I just went in here on the geometry and increase the point size as you can see.
[1:52] I don't want to draw the points on the grid or randomly.
[1:56] I want to draw them on the geometry.
[1:58] So for that, we will need a geometry intersector.
[2:01] So let's clear this and let's open this in text editor.
[2:08] So in a code editor, let's say, because it will be easier to write everything out.
[2:14] So we're initializing our class, our viewer state.
[2:19] And here we are just making sure we update the number of points.
[2:26] We make sure we have an undo queue.
[2:32] So this is just the default code and we will move right away into the geometry intersector.
[2:39] So before we do the geometry intersection, we need to grab the geometry.
[2:44] So in the initial in the init function, I'm going to set self dot underscore geometry.
[2:50] It will be equal to none.
[2:51] So I'm going to initialize it to none.
[2:54] And then I'm going to make sure I initialize the geometry on on enter.
[3:06] So I'm going to do on enter.
[3:09] And right in here, we are just grabbing the current node.
[3:15] And then we will grab the inputs, so inputs.
[3:20] It will be equal to self dot node.
[3:23] So the current node dot inputs, which in this case, should be the big add.
[3:28] And we just need to make a check.
[3:30] So if inputs and inputs zero, zero.
[3:37] So the single input that we found.
[3:40] So if that is not none, we will initialize the self dot initialize now.
[3:45] We will set the self dot geometry to be the inputs.
[3:51] And the first we found and we need to grab the geometry.
[3:55] So in this case, we grab the geometry itself, not just the node.
[3:59] We also need to grab the add node.
[4:03] So self dot inputs input input points, it will be equal to self dot nodes dot nodes.
[4:12] And we grab the add one, which in this case is inside here and it's called add one.
[4:18] So that's fine.
[4:19] Let's go again to there.
[4:21] And now we will also grab the geometry, the geometry of that add node.
[4:26] So the points it themselves.
[4:28] So self dot input points geo, it will be equal to self dot input points dot geometry.
[4:40] So we're having the geometry itself.
[4:44] Now we will do the geometry intersection.
[4:46] So we will do self dot geo intersect.
[4:51] We will name the variable like this.
[4:54] And we will take advantage of a viewer state utilities.
[4:58] So in this case, we are importing as an alias called SU.
[5:02] And these utilities you can find as you can see, I search on the I couldn't find in the
[5:07] documentation.
[5:08] But if you search on this folder in your own, in your files, we will find these utilities.
[5:14] Utilities dot BY and you will find in here the intersect the geometry intersection class.
[5:22] So we will then again come in here and we will take advantage of that.
[5:27] So where are we?
[5:29] So in here and we will grab that same utilities or that you utilities out by and we will
[5:36] grab the geometry inter intersect.
[5:43] And we just need to feed the geometry.
[5:45] So self dot underscore geometry.
[5:48] And we also need to feed to feed the scene viewer.
[5:51] So the current viewport self dot scene viewer that we should have right away from the default
[5:58] and it function.
[6:00] So we already have that.
[6:02] We don't need to worry about it.
[6:04] So now we initialize it, but we need to actually do the intersection.
[6:09] And that's because right now if we save this and go in here, we still will have the same
[6:15] default behavior.
[6:17] So let's come into the on mouse events.
[6:21] And this is where we will start to change things a bit.
[6:26] So on mouse events and we already have the UI events, the device, which is the mouse or
[6:35] the tablet or something.
[6:36] And we have the origin and the direction that we get from the UI events dot ray that we
[6:42] will need for the intersection.
[6:44] As you can see, this is doing a plainer in an intersection with the grid.
[6:48] We don't want that.
[6:50] So we actually want a geometry intersection.
[6:53] So for that, we will grab the geo intersectors, so geo intersector and we will do an intersect.
[7:01] And this needs the origin and also the direction which we get for free with this UI event dot
[7:08] ray.
[7:09] So that's fine.
[7:10] Now we just need to debug this.
[7:12] So print geo intersector dot and we can come in here and see what these outputs are intersected,
[7:22] whether the geometry intersection succeeded or not.
[7:25] We also get the position, the prime number and a bunch of other outputs.
[7:30] So we need to grab this intersected.
[7:32] Let's copy and let's paste it in here.
[7:37] So geometry intersector dot intersected.
[7:41] Let's see if that works.
[7:42] So if we come in here and enter the tool, so geometry intersector is not defined.
[7:48] So we got our first error.
[7:51] So we need to define self.
[7:55] Sorry about that.
[7:56] So let's close this and go again.
[7:58] As you can see, it's printing through when we are intersecting with the geometry and
[8:02] falls when we are not.
[8:05] So that's fine.
[8:07] Now let's come back in here and we don't want to print this.
[8:13] What we need to do is to grab the position.
[8:19] So we need to grab the position so we can fit that point position to the point where
[8:25] we'll create.
[8:27] So let's grab the position.
[8:29] So position it will be equal to self dot geo intersector dot position because we have
[8:37] that output in here.
[8:38] As you can see, the delay position of the intersect intersection point as vector tree.
[8:43] So we have the position.
[8:49] We can also grab in here the points geo just to make sure self dot node dot geometry.
[9:00] And then if we actually intersect something, we will we will create the point.
[9:10] So let's see in here.
[9:17] The device is left button.
[9:19] We start the state and we create a point.
[9:24] So by creating an entry on the multi-param and by setting the position.
[9:31] So let's actually test that.
[9:35] Let's see if that works for us.
[9:36] So if we enter and we are indeed creating a point on the geometry.
[9:41] Let's I'm going to change this behavior a bit because I want to be able to remove points
[9:46] and to drag points if we are near point.
[9:52] So let me see in here.
[9:57] So we need to do stamping first if I come in here and say you are that you are event reasons.
[10:04] So let's look at that.
[10:06] So we have different UI events in this case or the way we interact with the tool.
[10:12] And in this case, I just want to interact with active mode, which is when we drag the
[10:17] mouse with the left mouse button or another button we can program.
[10:22] So in this case, I'm going to disable all the other modes and just make sure we only
[10:26] use the mouse drag because it will behave a bit better.
[10:31] So let's go in here to this and we can actually set the UI event we have in here and we also
[10:42] need to place in here the reason.
[10:46] So reason it will be equal to UI event dot reason.
[10:52] So this is the way we interact with viewport or with a tool.
[10:57] Let me see.
[11:01] We can come into the mouse events and before we start interacting with the mouse, we can
[11:08] say if reason is not equal to out dot UI event, UI event reason dot active.
[11:20] So if this is not the case, we will self dot finish.
[11:25] We will exit the tool and we can return just true.
[11:29] So we finish the tool when this is not active enough.
[11:34] If the device is left button, we have that in here device, UI event dot device.
[11:38] So if this is left button, we need to make sure we start the tool and then we enter the
[11:48] position and we set the point.
[11:52] So we create a new point and we set that point to the position.
[11:54] We have already that going, but I also want to make sure if it's still left mouse button
[12:01] and we are near a point, I want to drag that point instead of creating a new point.
[12:07] So for that, we will need another variable in here and another function.
[12:13] So let's come in here to do.
[12:19] So we actually need to make sure we don't create, we don't compute if there is no intersection.
[12:26] So for that, I'm going to create a new and if not self dot geo intersector dot intersect
[12:34] it.
[12:36] So if we didn't found an intersection, we can return false.
[12:41] It turns false.
[12:42] So just make sure enough.
[12:45] We get the position, we get points geo and then we need a near point.
[12:52] So we will make sure if we are close to a point that we drag them instead of creating
[12:58] a new point, like I said, let's create a near point and this will be on the points geo dot
[13:06] nearest nearest point.
[13:10] It's the name of the function and we will pass the position that we are.
[13:16] And then let's see what we get from this.
[13:20] So let me go to what Dini and press F1 and get the nearest point.
[13:26] So geometry nearest point and we need to pass a point group which will be none and radius.
[13:34] So that's fine.
[13:35] This is a bit small.
[13:36] I can increase this.
[13:38] So nearest point so point group will be equal to none and max radius.
[13:44] So let's come back to this and point group will be none.
[13:48] I don't want any point group and the radius, we can set it to 0.1 and we can pass this
[13:52] as a parameter.
[13:54] But right now I'm going to keep it as point one.
[13:56] Now we need also to find the near point index.
[14:00] So we can fill that to the to the add node.
[14:04] So near point underscore index.
[14:09] It will be equal to near point and we grab the number of that point.
[14:15] And if near point is true or else we pass it as marked.
[14:25] So in case we have a near point we will write to the number of that point.
[14:32] Otherwise we set it to none so we can filter later down the line.
[14:37] So now let's get back to the if device is left mouse button.
[14:43] We need to check in here.
[14:46] So this is where we check.
[14:47] If near point index is not none so we just did that.
[14:53] We will do the same in here.
[14:56] So let's copy this and paste it in here.
[15:02] So in this case we will sell dot no dot bar dot we don't need index but near point index
[15:08] of the point number we set.
[15:11] And we will also set the position to the same so near point index.
[15:17] And then we can do else.
[15:23] And we do self dot start and we do the same in here.
[15:26] Right now we're using the index that is computed somewhere in here.
[15:31] So let me find index.
[15:33] So index is computed from this function with which is self dot point counts that counts
[15:38] the points.
[15:41] So let's find let's go back and delete all of these.
[15:45] And now let's create a point whoops the object near point index.
[15:49] So I believe I said it to self.
[15:52] So this case I didn't set in yourself so let me share I do it this and save again.
[16:01] Let's clear close.
[16:03] Let's try again.
[16:05] No non type object is not a good of set.
[16:09] One to three.
[16:11] Self dot no dot bar near point index.
[16:18] So guys I think I know why this is not working because right now if we display the geometry
[16:24] we are actually displaying the geometry itself which we don't want.
[16:29] So let's go into type properties and we will go in here to note and select the guide
[16:36] geometry.
[16:39] So let's create a no and name this guide.
[16:44] Now let's connect these into here.
[16:48] So let's apply and accept.
[16:52] And let's go and now we should have a guide geometry.
[16:55] But let me make sure in here.
[16:57] So yeah we don't want to connect this actually we just want like this.
[17:03] So now if we enter so let's enter and we draw the point and we can drag it as you can
[17:10] see.
[17:12] So this should be working.
[17:14] Let me see.
[17:15] Yeah.
[17:16] And now we just need to make sure we because before we were actually interpreting the
[17:21] big as the geometry which you don't want we just want the geometry of the points.
[17:27] So that's why it was not working.
[17:30] Again I did this some time ago and I didn't remember very well how I did it but yeah looking
[17:35] at my initial one we don't want to web that as input to you.
[17:38] We just want the guide and we want the add notes separated.
[17:45] So now let's just do the removal of the points.
[17:48] Let's go into again the mouse events and we will in this case do it with the middle mouse.
[17:59] So we have a near we can create a near an LIF if the oops LIF device is middle middle
[18:14] button and also the near pointing index is not none.
[18:25] We can so if we are near a point and the mouse the button we click is the middle mouse
[18:32] we can remove the point.
[18:34] So in this case we should have we can create these.
[18:39] Let me see where we have that so remove.
[18:43] We don't actually have that so we should have a functioning here.
[18:51] Let me search remove multiparm instance.
[18:54] So in this case we don't so we will do it anyways.
[19:00] So where were we?
[19:01] We can come in here we can copy these out and we will do self.nodes.parm.
[19:10] So we can actually tap these out and we will grab instead the points and we will do a
[19:22] function called remove multi-parm instance and we will remove the near pointing index on
[19:33] near point index and we can apply to the point count so self dot index it will be equal
[19:41] to self dot point count it's a function we have in here so if we actually search for
[19:47] that we are just substituting in the point count.
[19:52] So let's make sure we have that and now if we go to our tool and we draw a point we
[20:01] middle mouse and remove it.
[20:05] So let's make sure we are dragging the point as you can see if we are near a point and
[20:10] we are removing it also.
[20:13] So that's the first part done and next we will do we will do the drawable.
[20:20] So let's do that next.
[20:23] So now we will do the point drawable and for that we will take advantage of the geometry
[20:28] drawable class and let's see what sort of parameters we need to pass or arguments.
[20:34] So in this case we need to pass the scene viewer geometry type a name and we can ignore
[20:40] we can pass also the parameters we can ignore label for now.
[20:45] So geometry type let's see what we have and in this case I don't want to draw a line
[20:50] RF face I want to draw a point so all the need dot drawable dot geometry type dot point.
[20:57] So let's copy this and let's go again to our function where I have that.
[21:04] So we will do this in need function or method and let's start by defining.
[21:14] So let me remove this and let's say self dot point reject it will be equal to how dot
[21:24] geometry drawable geometry drawable like this drawable and we will pass the thing viewer.
[21:36] So self dot scene viewer we will pass that code we that's a name we copied from the
[21:43] docs.
[21:44] So we want a point I'm going to name it point reject and we also need to pass some
[21:51] farms and for that we will do a dictionary so params it will be equal and open this curly
[21:59] bracket and let's pass in your some farms and we just need a color and a radius.
[22:06] So in this case the name is called color one and we will do all dot color and I'm going
[22:14] to set it to 0.4 0.4 1 0.4 so somewhere greenish and we need a comma and we also pass the
[22:31] radius it's another parameter we can pass and I'm going to set it to 10.
[22:35] So that's fine now we need also to set it in here to show the the points of self dot point
[22:46] reject dot show and set it true let's go again to the scene and as you can see we still
[22:56] can't see the drawable we need to actually do something here.
[23:02] So let's see we also need to show it on draw so we have that function on draw and now we
[23:14] have the angle and we need to pass in here self dot point project dot draw and we pass
[23:23] the handle.
[23:26] So let's go in here and if we the handle is not defined let me make sure of I can rename it
[23:34] to handle it was draw and so let's clear exit and try again but as you can see we still
[23:42] long time because we need to create actually the actual geometry so for that we will take advantage
[23:49] of the sub verbs so in the on mouse event on mouse event we will come into after this one
[24:06] can be and we will make sure we are we have intersected otherwise we don't want to draw
[24:14] the point so if self dot geo intersected geo intersected intersected we will create an
[24:21] ad node to create the point so ad verb will use sub verbs so all dot sub node type category
[24:30] and we will create that geometry so node verb and we will create an ad node then we will
[24:41] set some farms so add verb dot set farms and we will open in here and first of all we will
[24:56] set the points and we will open the we'll create a home and open the square brackets and
[25:09] let's just create the parameters so let's do in this case I know it's named use pt and you
[25:20] can check that on the ad node parameters and I'm gonna set it to true and I'm also going to set
[25:28] the point number to the position of the intersection so position and now we as let's clear some space
[25:38] in here oops I didn't mean to do that so I can clear some space in here and now we can do the
[25:51] following we can assign we can create a point we can create a geometry out of geometry then we just
[26:02] need to execute so add verb dot execute and we will pass the point so let me just make sure
[26:15] f1
[26:22] so and we need to pass the inputs we need to pass the verb and we need to pass the inputs in this case
[26:28] I'm not going to pass any input so execute point and the inputs will be empty then we just need
[26:35] to assign it so self dot point project dot set geometry and we will pass the point we just
[26:45] created so if everything is working we should now have a point as you can see which is greenish
[26:51] and when we go outside it doesn't it stays like default behavior but when we drag it we can
[27:00] interact with it so we just have visual feedback to where we will place the point and I'm also
[27:06] going to create another one so when the point is actually created so for that I'm just going to
[27:19] create yet another one so let's go back and in here I'm just going to copy this one
[27:32] and paste it in here and I'm going to name it to geo draw drawable and by I will do the same thing
[27:43] but in this case I'm going to call it point drawable drawable
[27:51] the same parameters but in this case I'm going to change the color to be white
[27:58] and the radius I'm also going to decrease it to 6 I also need to show it so I'm going to copy and
[28:04] paste this so in this case geo drawable dot show that's fine now we just need to show it
[28:15] which in this case we will do on on enter so on enter and I'm going to set in here the
[28:24] drawable we just can't we can just use the the add node the add node with the points so in here we can
[28:30] set elf dot geo geo drawable dot set geometry and we can input self dot input input points geo
[28:42] which is the add node add node geometry so let's find let's make sure that is working so
[28:51] and it's not working because we need to draw that so on draw when we add that on draw we actually need to draw this
[29:03] self dot geo drawable dot draw and dot that's fine make sure we add that and as you can see is drawing
[29:12] that point and when we enter we exit the tool by tumbling around that goes back to the default point
[29:20] and if I change that let's say tree it will be more visible so as you can see it's very small and we
[29:27] have drawn that point let's remove those points and as you can see everything should be working
[29:40] so in this case I think we don't actually need to worry about the the endals because we are not
[29:49] we are not working with endals but actually so we can just delete this we are working with
[29:55] drawable so we can get rid of this and we have only on draw and so we can actually on end
[30:05] all to state we can get rid of this save and come back and we should still be able to do
[30:13] everything so we draw a point we remove and we can drag it and it will be good if we set actually
[30:22] near display of all this work so a guide so let's come back in here and at the top where we have
[30:29] that message which is in here message we can say so let mouse button let's delete this let mouse
[30:39] button drag to add points create a new line so escape a new new line and we can say left mouse
[30:54] button drag over over existing point to move it create a new line
[31:08] and we can say middle mouse drag to delete point so let's now test and as you can see we have left
[31:19] mouse button drag to add point left mouse button drag over existing point to move it that's fine
[31:27] and middle mouse drag to delete so yeah guys that was basically what I had for today as always you
[31:35] can grab the tool on my patreon if you don't want to create it yourself and as always you can get
[31:44] a lot of exclusive tutorials all the project files from my videos and let me know in the comments
[31:51] if these help you out in any ways again I'm not a pro in Python or Python states I'm just getting
[31:56] started and I try to share what I know so thank you for watching and I guess I'll see you next time



---

## Captured Frames

- [0:40] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_000.jpg
- [2:00] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_001.jpg
- [8:00] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_002.jpg
- [9:40] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_003.jpg
- [17:00] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_004.jpg
- [20:00] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_005.jpg
- [22:30] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_006.jpg
- [31:20] tutorials/frames/interactive-tools-with-houdini-python-states-draw-pts-on-geo/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a custom interactive **Python Viewer State** HDA from scratch ("Draw Points on Geo" — the same tool referenced/used in several other tutorials in this batch, e.g. for manually placing fracture seed points on the perfume bottle) that lets a user click-drag to add points directly on a mesh surface (via a **Geometry Intersector**, not the default construction-plane/grid intersection), drag existing points to reposition them, and middle-click to delete them — with live on-screen visual feedback built from `hou.GeometryDrawable`.

### Summary
The HDA is built around a multi-parm **Add** SOP (one entry per drawn point) wrapped in a Subnet and converted to a Digital Asset with the "Interactive" template plus "On Draw" and "Handle States" enabled. By default, the state's built-in interaction intersects against the flat construction plane/grid — not what's wanted, since points should snap onto the actual input geometry. The fix requires manually building a **`hou.GeometryIntersector`** (from `viewerstate.utils`, aliased `su`) in `onEnter`, initialized against the geometry pulled from the state's first input node (`self.node.inputs()[0]`) — critically the geometry of that connected node, not the tool's own Add-node output (an early bug in the video: intersecting against the tool's own guide/output geometry instead of the actual input mesh caused mysterious failures until this was corrected by properly separating a dedicated **Guide** node in the HDA's Type Properties from the Add node driving the actual points). In `onMouseEvent`, the default plane-intersection call is replaced with `self.geo_intersector.intersect(origin, direction)` using the ray data from `ui_event.ray()`; `.intersected` and `.position` (the hit point in world space) become available once this succeeds. A `reason` check (`ui_event.reason() != hou.uiEventReason.Active`) causes the tool to call `self.finish()` and return early on any non-drag/active event, restricting interaction specifically to left-mouse-drag. On a left-button press with a successful intersection, a new point is added at the intersection position (`self.start()` + `insertMultiParmInstance` at `self.pointCount()`, followed by setting position parms) — but first, a **`nearpoint()`**-style lookup (`points_geo.nearestPoint(position, group=None, max_distance=0.1)`) checks whether the click landed near an *existing* point; if so, that existing multi-parm instance's position is updated instead of creating a new entry, giving drag-to-move behavior. Middle-mouse-button clicks near an existing point instead call `node.parm("points").removeMultiParmInstance(near_point_index)` to delete that point entry. For live visual feedback, two `hou.GeometryDrawable` instances are created in `onEnter`: a "preview" drawable (greenish, larger radius) showing where a point *would* be placed as the mouse hovers/drags (built by constructing a temporary SOP verb — `hou.sopNodeTypeCategory().nodeVerb("add")`, `setParms({"points": [...], "usept": True, ...})`, `execute()` — and feeding the resulting geometry into the drawable each frame the intersection succeeds), and a persistent white, smaller-radius "committed points" drawable showing all points actually added so far (fed from the real Add node's geometry, updated in `onEnter` and rendered every frame in `onDraw`). Handle-related boilerplate (since the tool only needs drawables, not manipulable handles) is stripped out as unnecessary. The tool finishes with a simple on-screen instructional message string (built via `state.msg`/similar, using explicit newlines) summarizing the three interactions: left-drag to add a point, left-drag over an existing point to move it, middle-drag to delete a point.

### Key Steps
1. **Base HDA scaffold:** create an **Add** SOP (multi-parm point entry) fed from the test input geometry; wrap in a **Subnet**, convert to a **Digital Asset** using the Interactive template, enabling "On Draw" and "Handle States".
2. **Diagnose default behavior:** entering the tool by default draws points via intersection against the flat construction plane — not the actual input mesh — necessitating a custom Geometry Intersector.
3. **Initialize the intersector on enter:** in `onEnter`, grab `self.node.inputs()[0]` (the connected geometry-providing node, not the tool's own Add output), store its geometry, and build a **`hou.GeometryIntersector`** (via `viewerstate.utils`, aliased `su`) targeting that geometry and the current scene viewer.
4. **Replace default ray intersection:** in `onMouseEvent`, use `ui_event.ray()` for origin/direction and call `self.geo_intersector.intersect(origin, direction)` instead of the default plane test; debug via printing `.intersected` to confirm hits/misses.
5. **Restrict to active drag only:** check `ui_event.reason() != hou.uiEventReason.Active` and call `self.finish()` / return early for any other event reason, so the tool only responds to actual mouse-drag interaction.
6. **Add a point on left-drag:** on a successful intersection with the left mouse button, call `self.start()`, `insertMultiParmInstance(self.pointCount())` on the points multi-parm, and set the new instance's position from `self.geo_intersector.position`.
7. **Near-point lookup for drag-to-move:** before deciding to add vs. move, use `points_geo.nearestPoint(position, group=None, max_distance=0.1)` — if a point is found within that radius, update its existing multi-parm instance's position instead of creating a new one; otherwise fall back to creating a new point.
8. **Fix the "wrong geometry" bug:** initially the state accidentally intersected against the tool's own guide/output geometry rather than the real input mesh, breaking the near-point logic silently; fixed by adding a dedicated **Guide** node in the HDA's Type Properties (Node → Guide Geometry) wired separately from the Add node that actually drives the drawn points.
9. **Delete on middle-click:** check for middle mouse button plus a valid near-point index, then call `node.parm("points").removeMultiParmInstance(near_point_index)` to remove that specific point entry.
10. **Preview drawable (hover feedback):** build a `hou.GeometryDrawable` (geometry type Point, greenish color, larger radius) in `onEnter`; each frame the intersection succeeds, construct a temporary point via a **SOP verb** (`hou.sopNodeTypeCategory().nodeVerb("add")`, `setParms({"usept": True, "pt": [position]})`, `execute(geo, [])`) and feed the resulting geometry into the preview drawable via `setGeometry`, so the user sees exactly where a point would land before committing.
11. **Committed-points drawable:** build a second `hou.GeometryDrawable` (white, smaller radius) fed from the real Add node's actual output geometry, refreshed in `onEnter` and drawn every frame in `onDraw` — shows all points genuinely added so far, distinct from the hover preview.
12. **Strip unused handle boilerplate:** since the tool only needs drawables (not manipulable 3D handles), remove the default `onHandleToState`/`onStateToHandle`-style boilerplate that ships with the Interactive template.
13. **On-screen instructional message:** set a multi-line status message string (left mouse drag = add point; left mouse drag over existing point = move it; middle mouse drag = delete point) so the tool is self-documenting when active.

### Houdini Nodes / VEX / Settings
Nodes: Add (multi-parm point entries), Subnet, Digital Asset (Interactive template, On Draw + Handle States enabled), Type Properties → Node → Guide Geometry (dedicated guide node, separated from the Add node). Python (`viewerstate.utils` aliased `su`, `hou` module): `hou.GeometryIntersector` (geometry + scene-viewer initialization, `.intersect(origin, direction)`, `.intersected`, `.position`), `onEnter`/`onMouseEvent`/`onDraw` state callbacks, `ui_event.ray()`, `ui_event.reason()` / `hou.uiEventReason.Active`, `self.start()`/`self.finish()`, multi-parm manipulation (`insertMultiParmInstance`, `removeMultiParmInstance`, `pointCount()` helper), `geometry.nearestPoint(position, group, max_distance)`, `hou.GeometryDrawable` (geometry type Point, `params` dict for color/radius, `.show`, `.setGeometry`, `.draw(handle)`), `hou.sopNodeTypeCategory().nodeVerb("add")` (temporary SOP verb execution for preview-point geometry, `setParms`, `execute`).

### Difficulty
Advanced/Expert — full custom Python Viewer State authoring (geometry intersection, multi-parm manipulation, SOP verb execution, GeometryDrawable feedback) requiring solid Python/HOM and Houdini state-machine fundamentals.

### Houdini Version
20.5 (UI matches Houdini 20.5-era Python Viewer States API; the resulting HDA — "Place Points on Geo" — is the same tool referenced across several other tutorials in this batch, e.g. for manually placing RBD fracture seed points).

### Tags
#python #hda #procedural #tips #advanced

---

## Related Tutorials
- [Shoe Laces in Houdini - Vex and Vellum](shoe-laces-in-houdini-vex-and-vellum.md) — uses this exact "Place Points on Geo" HDA to hand-place shoelace eyelet points before the procedural pattern/Vellum pipeline.
- [Texture Projection Tool for Houdini 20.5](texture-projection-tool-for-houdini-205.md) — another Python-States-driven custom viewport-interaction HDA, here for click-drag texture projection instead of point placement.
- Cross-link with houdini-beginner-tutorial-creating-a-perfume-bottle.md and houdini-techniques-to-improve-your-level.md (same author, same "Place Points on Geo" HDA referenced/used as a finished tool) once indexed together.
