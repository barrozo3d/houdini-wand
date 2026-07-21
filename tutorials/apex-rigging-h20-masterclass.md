---
title: APEX Rigging | H20 MASTERCLASS
source: YouTube
url: https://www.youtube.com/watch?v=-0KbPtoP5MU
author: Houdini
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/apex-rigging-h20-masterclass/
frame_count: 0
frame_status: pending-selection
---

# APEX Rigging | H20 MASTERCLASS

**Source:** [YouTube](https://www.youtube.com/watch?v=-0KbPtoP5MU)
**Author:** Houdini
**Duration:** 71m35s | 16 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py apex-rigging-h20-masterclass <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hi, my name is William Harley, I'm currently working as a character TD at SideFX Software.
[0:05] In this masterclass, I'll be showing you how to set up a basic rig in APEX using components,
[0:10] which are scripts that we'll use to add nodes, set data on them and connect them to each other
[0:15] in the rig graph.
[0:16] We'll also have a look at how to set up sub-graphs, which are tools similar to HDAs that contain
[0:21] more complex logic that you can use to simplify your rig width.
[0:26] I'll also go over the chicken and dive deeper into the component scripts that I'm using
[0:30] in that rig.
[0:32] Okay, so let's build a little rig just to show how components and sub-graphs work before
[0:39] we get to the chicken rig.


### Simple Rig - Components [0:40]
**Transcript (timestamped):**
[0:42] So I'm going to create a tube, insert X-axis, radius of 1 and height of 2, and then create
[0:54] some more rows.
[0:57] Then I'm going to create a skeleton.
[1:02] And I'm just going to snap to grid and set that.
[1:09] And I'm going to select all of them, so press S, select all of them and orient the joints.
[1:17] And then I'm going to rename them.
[1:19] So I'm going to select them, root, mid, and tip.
[1:29] Okay, now I'm going to do a Capshift proximity.
[1:41] And then something that I like to do is I like to add an add node and get rid of the
[1:45] geometry that keeps the points.
[1:49] This will make it so that the joint capture proximity will look at the points rather than
[1:53] the parameters for the capture.
[1:55] So it creates a little bit of a smoother transition between the different joints.
[1:58] So I'm going to just change the drop-off and you can see.
[2:03] You'll see better once we add a bone deform.
[2:05] So I'll just add a bone deform so we can just check the weights before we move on.
[2:12] Here I've got my rig pose.
[2:17] Okay, and then I'm just going to move these points.
[2:21] I just turned grid snapping off.
[2:23] Move this up a little bit.
[2:25] Move that guy down.
[2:27] You can see that the weights are way stronger around the joints than they would be if I
[2:35] didn't add the add nodes.
[2:36] If I remove this, you'll see it's quite strange weighting, but it's because it's taking
[2:42] the parameters into account.
[2:43] Okay, so over here I'm just going to increase that drop-off a little bit just to smoothen
[2:51] it out a bit.
[2:52] And something else that you can also do is just add a smooth node.
[2:57] That'll keep the edge weights the same, but it'll smooth them out a little bit.
[3:01] So if I add a bone captures attribute here, I smooth it a bit.
[3:07] I mean while we're looking at the thing.
[3:09] So if I smooth it a bit, you can see the tips are still staying constrained to the,
[3:13] or weighted to the joint tips.
[3:15] Okay, okay, but now that we have a mesh that's captured and we've got a skeleton, let's
[3:23] pack them into folders.
[3:27] So now I've got my pack folders node and I'm going to pack my capture mesh and my capture
[3:34] skeleton and the base dot shape for the mesh and base dot scale for the skeleton.
[3:46] Okay, now the order of the node.
[3:50] So all the auto component node will set up my my rig graph for me.
[3:55] So what what this node does is it will run component scripts and a component script is
[4:01] just a script that will build the rig and add nodes and plug nodes into each other inside
[4:07] the rig graph.
[4:10] So what I want to do here is I want to take the skeleton data and I want to take the mesh
[4:14] data and I want to build a rig from from that using these components.
[4:20] So I'm going to say FK transform.
[4:23] The FK transform will set up a FK rig on the skeleton for me.
[4:29] As you can see here, I've got my transforms.
[4:32] Let me just un-template the tube.
[4:36] I've got my I've got my transforms and they are moving the skeleton around like any other
[4:43] FK rig.
[4:45] It's rotation and translation.
[4:49] Let's have a look at the the rig graph.
[4:51] I'm going to just unpack this quickly.
[4:53] So I'm going to select the unpack folder and you have to unpack it because these are all
[4:59] packed primitives.
[5:00] So if you have a look at the apex network view, so these are all packed primitives.
[5:06] So if I just view that network, the apex network view, I'm not going to see anything.
[5:11] So I really need to isolate that rig that rig graph.
[5:14] So I'm going to select unpack folder and by default it's set to star, which means it'll
[5:19] unpack everything.
[5:21] So you're going to get some of this noise in there, which is coming from the mesh itself.
[5:28] So what we want to do is we want to just specify the rig.
[5:31] So I'm going to say rig.
[5:33] And now you'll get a nice clean network view that just shows you the rig graph.
[5:38] Okay, so I'm going to append this so we can have a look at this while we make some changes
[5:44] on the order component.
[5:46] But essentially what this is doing is it's just recreating what I have here.
[5:51] So it's taking my skeleton, but it's creating transform objects instead of joints.
[5:57] And these transform objects will represent my joint positions.
[6:01] So it'll grab the rest position from the skeleton and set that on here.
[6:06] And it will parent them to each other just like the skeleton is.
[6:10] So on the parameters, you can see these parameters have been exposed.
[6:17] If I look at the order of the component node, you can see over here, I've got my parameters
[6:23] that I exposed.
[6:24] So it's either my translates, my rotates or scale will be promoted.
[6:29] And if they're promoted, you will see that it's visible in the viewport.
[6:33] So I can actually select it here.
[6:34] You can see I've got my translate and my rotate.
[6:37] If I get rid of rotation, you can see now I only have translate.
[6:42] And over here, you can see only the translate for each of the transform objects I exposed.
[6:49] So these transforms then all go to a point transform node.
[6:55] And it's using this name to set the joint name.
[6:59] So it's basically setting the joint transform based on name.
[7:04] So it'll take the skeleton data, deform it and then output that to base skeleton.
[7:15] So another thing that this FK transform, I mean, it creates this point transform, but
[7:19] you can also see what it looks like if you switch it off.
[7:23] Let's just view that component in the viewport.
[7:28] You can see if I switch this off, you'll see how the graph updates and my viewport updates.
[7:32] So you can see now I'm not outputting my base skeleton anymore.
[7:37] You can see it's not reflected in the viewport.
[7:40] So now you can see how this matches up with that.
[7:44] So we're still seeing these controls because they're promoted, but we're not seeing the
[7:47] skeleton.
[7:48] I'm just going to add the promote or the point transform again.
[7:56] Okay, so the next step that we want to take in this rig is we want to create a control


### Control Hierarchy [7:58]
**Transcript (timestamped):**
[8:04] hierarchy that we can control the main joints with.
[8:10] So what I'm going to do is instead of like editing this graph and just duplicating these
[8:15] transform objects, I'm just going to create the, I'm just going to update my skeleton
[8:20] to have the controls in there.
[8:22] So the FK transform component can do it for me, which is a lot simpler.
[8:27] Okay, so let's go to the skeleton quick.
[8:32] Unlock this and I'm going to put down a wrangle node and then I'm just going to rename the
[8:43] skeleton joints that I have there.
[8:45] So I'm going to say app name is less equals to underscore control.
[8:52] Okay, so now if I look at my rig tree, some reason I've got a ghost joint there.
[9:03] Let's just get rid of that.
[9:06] So if you look at my rig tree here, I've got my root control, mid control and tip control.
[9:14] And for these controls, I need to add some shapes as well.
[9:18] So I'm going to use the attach joint geo to add some control shapes.
[9:25] And in this case, I'm not actually changing the controls.
[9:28] So if I look at this order, we're going to hear, I won't be changing these by just attaching
[9:35] geo to it.
[9:37] What I'm doing is I'm going to attach a control shape to it, which I can then read in the
[9:43] apex graph and then set the controls to be the new shape.
[9:49] So I'm just going to load my control geo in.
[9:52] And over here, you can see I've got a control shape, but I've got some nerves, nerves in
[9:58] there as well.
[9:59] So I'm just going to have to convert that quickly.
[10:03] So it'll work with apex because apex doesn't like primitives at once polygon shapes for
[10:09] the for the viewers.
[10:13] And then make it a bit smaller.
[10:19] Just as like a default scale, it's a little bit large.
[10:22] I just want it a bit smaller.
[10:24] Then I'm going to merge pack, name that control and then add that into the shape library of
[10:32] the attach joint geo.
[10:34] And then I'm going to just assign those controls.
[10:37] So I've named it control day.
[10:38] So I'm going to say control.
[10:41] Okay.
[10:44] And I think that's pretty much it for the controls.
[10:48] The only thing that I wanted to add here was just some color to the network.
[10:52] So so we can better see which are the main joints and which are the control joints.
[10:58] So over here, I'm just going to add a color red for the main joints and green for the
[11:05] control joints.
[11:07] Okay.
[11:08] And then I can merge these together and plug it in.
[11:16] Let's get some more space here.
[11:21] Okay.
[11:22] Okay.
[11:23] So now let me just give it a quick update.
[11:31] So now we've got those control shapes on there and we can move these around.
[11:35] But you can see I still have the control shapes in the middle.
[11:40] I can't actually select these shapes.
[11:41] So that's that's what I was saying is that the shapes that you are attaching to the skeleton,
[11:47] that's just data that's coming in with the skeleton.
[11:49] So we want to be able to use this data to change the controls.
[11:56] So what I'm going to do is I'm going to add an order read control.
[12:01] So just another order read component.
[12:03] Sorry.
[12:05] And then I'm going to change this to configure controls.
[12:11] So it's going to run a component that will fetch data or set data.
[12:16] So I can actually set the controls over here manually or I can say, well, just fetch the
[12:23] data from the base skeleton.
[12:25] So I'm going to set that to base.scale.
[12:29] As you can see, now it's updated the controls.
[12:31] And if I move these controls away, you can see that it's attached to the control skeleton,
[12:38] but not the main skeleton.
[12:41] So much easier to select and manipulate.
[12:43] Okay.
[12:46] So I don't really want controls on these guys.
[12:50] So I'm just going to go and clean the if k component up a little bit.
[12:55] So I'm just going to say I want transforms and rotates on both.
[13:00] I only want it on the controls.
[13:02] So I'm going to say controls star control.
[13:09] So any joint now with a with a controller in the name will now be promoted.
[13:14] So it's assuming that that any control will be promoted.
[13:17] So let's go back to component here.
[13:22] Let's just update these just to make sure everything gets updated properly.
[13:31] Okay.
[13:32] And then I move this away.
[13:33] You can see now, I don't know those controls.
[13:36] And I've got a nice control hierarchy that I can start working with.
[13:41] So now I want to constrain the main joints to the control joints.
[13:48] Let's just have a look at this graph again.
[13:54] So in order to constrain them, what I'll have to do is like the X form of the control
[14:03] node into the X form input of the node that I want to control.
[14:09] So you're essentially doing a position constraint or transform constraint rather.
[14:16] So to do a transform constraint to connect these two together, I just have to plug that
[14:21] in and I can create a component that can do this for me so it can be automatic.
[14:27] And in this case, it doesn't feel like it makes a lot of sense to create a whole script
[14:31] to do all the plugging in.
[14:34] But if you have 100, 100 controls and 100 joints and you need to manually plug them in,
[14:41] that's going to be a little bit painful.
[14:42] So let's set up a component to do that.
[14:46] Okay.
[14:48] So for that, I need another order rate component.
[14:54] And then this time I'm going to use a apex edit graph is I want to create create a new
[15:00] graph.
[15:02] And this is going to be my component.
[15:05] And I want to plug all this in and I want to set this to use second input.
[15:13] So now it's going to use this second input as my script that I want to run on the node.
[15:21] Okay.
[15:23] So if we look at this output now, you can see here we can see the graph here.
[15:28] We can't see anything.
[15:30] So what's happening here is that I haven't actually done anything with that graph.
[15:34] So it's just, it's like a dead end.
[15:36] What I need to do is I need to do a pass through or initialize this graph and then I can make
[15:42] some edits to it.
[15:43] I'm going to quickly initialize that so you can see what that looks like.
[15:49] So first we need the submit input.
[15:54] And then we need a subnet output.
[15:58] And I'm just going to clean up these names, bonds and output.
[16:03] Okay.
[16:05] And then I'm going to extract the character graph.
[16:10] So you're essentially loading the graph into this graph.
[16:15] You're loading the rig graph into this graph so you can actually fetch and change nodes
[16:21] in the graph.
[16:22] So what I'm doing here now is like specifying the rig name.
[16:27] So on the component, you're going to be fetching the actual rig name.
[16:32] So it's called rig name.
[16:35] And I'm bringing in the character geometry.
[16:38] So the character geometry will be all the pack primitives that are in this, in this
[16:43] rig.
[16:44] And the rig name will just specify what I'm bringing in and that's base.rig.
[16:51] Okay.
[16:52] So now when we're done with that, I need to update that character.
[16:55] I'm going to update the character graph, plug in the name, the graph and the character
[17:02] mesh and then output the character mesh.
[17:06] Okay.
[17:07] So now you can see it's updated.
[17:10] And if we look at the graph here, it's just basically doing a pass through at the moment.
[17:18] So it's like bringing the graph in and outputting it again, exactly like it used to be.
[17:25] So now that we've got the graph coming in, we can do some stuff to it.
[17:29] So we want to connect the controls or we want to constrain the joints to the controls.
[17:34] So the first thing I want to do here is just make a little bit of a template.
[17:37] So I'm going to make this a little bit larger so we can see clearly.
[17:41] And then I just want to make a template so we can see what we want to do.
[17:45] So this is a silly example.
[17:48] But when you work with a larger, larger component, like this is not such a bad idea.
[17:55] Just creating a little bit of a template so you know what you're doing.
[17:59] So we're going to root and root control.
[18:05] And then what we want to do is plug the X form into that one's X form.
[18:09] That's this is exactly what this component is going to do.
[18:13] But it's going to do it automatically.
[18:16] So the first thing we want to do is we want to find all the control nodes.
[18:20] So I'm going to say find nodes.
[18:24] And this will be the nodes that are in the graph, in the red graph.
[18:29] So we fetching that graph.
[18:32] I'm going to promote this pattern so I can set it on my order of components.
[18:37] I'm going to do that.
[18:39] So if I select this and I update the parameters, then now you'll see.
[18:46] I've got this pattern field that I can enter a string into.
[18:51] And what I want to do is I want to find all the nodes with control in it.
[18:56] So that's what that's going to find.
[18:59] So now I basically have a list of all the nodes.
[19:07] Then I have control in their name.
[19:10] So all the control nodes.
[19:12] So now I'm going to do a for loop over that.
[19:16] Or for each, sorry.
[19:19] For each.
[19:21] And it's a apex node ID.
[19:24] And a for each end.
[19:30] Like that.
[19:33] Let's make a little more space here.
[19:37] Okay, so now each of these elements are one of those control nodes.
[19:42] So what I want to do is I want to find the name of this transform object.
[19:49] And just strip away control.
[19:51] And then I can automatically find the node that it needs to connect to.
[19:55] So I'm going to say find nodes.
[20:00] We'll just find node.
[20:05] And we'll use that.
[20:06] We'll use that to find the final node.
[20:09] And then we're going to say node data.
[20:13] That's the one we want.
[20:15] And then you can see we need the graph.
[20:17] So let's bring the graph into the loop so we can use it.
[20:21] So I'm going to say graph.
[20:24] And then I'm supposed to find the graph.
[20:27] And this is the control node that I want to read the name from.
[20:31] And what I'm going to do is I'm just going to strip this control out of it.
[20:35] So I need a replace.
[20:39] String replace.
[20:43] And I'm going to plug the name into the input.
[20:45] And if you press P, you get the parameters.
[20:48] I'm going to say.
[20:51] Star underscore control.
[20:53] And then it will replace it just with whatever the star was in front of the control.
[21:00] So it'll be root underscore control.
[21:02] Now it'll just be root.
[21:05] And that will be the path for the node that we want to find.
[21:09] So we want to find the node that's called root.
[21:11] So I'm going to plug that in here.
[21:14] Plug graph in.
[21:16] And now we basically have the control node over here as an element.
[21:20] And we have the joint that we want to control.
[21:24] And all we need to do now is just plug them into each other.
[21:26] So I'm going to do a find and connect.
[21:35] And then I'm going to plug the graph in.
[21:37] And the destination node is the joint I want to control.
[21:42] So this one.
[21:44] So that's the destination.
[21:47] And I'm going to plug the graph in.
[21:50] And this is the roots, the control that I want to go from.
[21:56] And that's this search node.
[21:59] And what this is going to do is it's going to find the ports on there.
[22:02] So it's going to find a specific port on there and plug it into another port.
[22:07] So I can say because they both called X form, I'm just going to say X form.
[22:11] And I'm going to say X form over here.
[22:14] So now it'll plug those two into each other.
[22:17] So let's let's export this.
[22:21] Name that graph as well.
[22:23] And then I'll just output this graph.
[22:27] So just to go over this quickly.
[22:30] So the graph is coming in and it's continually running through
[22:38] through this whole network until the end.
[22:40] And sometimes just be wary of this.
[22:43] Like sometimes you miss one of these inputs and then you graph
[22:45] and output and you're wondering why it's not working.
[22:49] It's maybe because you're missing.
[22:51] Missing if like the flow is broken of of of your graph.
[22:56] Okay, so let's have a look at the output that we're getting.
[23:01] So now this is the what this order what this component has done now.
[23:07] So if you look at this, you can see the control is now plugged into the root.
[23:12] And same with the mid and the tip.
[23:16] So everything's plugged in nicely.
[23:18] And so what this means is now we can go to this order component
[23:22] and we can just select this control and you'll see all the joints will now move together.
[23:26] So you can't clearly see the capture skeleton yet.
[23:31] But we will in a moment.
[23:33] So you can see it's all working nicely.
[23:36] Because then the last thing you want to do is now that we've got the controls connected
[23:41] we've got the skeleton we want to add a bone deform.
[23:44] So I'm going to add another order component.
[23:52] And what we're going to do here is we're just going to plug that in and it should automatically
[23:58] fill out all this information for you.
[24:00] So you've got the point transform geo, the base shape, base skeleton and base
[24:06] base shape for the output geo.
[24:09] So if you look at this in the network.
[24:16] So we can reset this.
[24:19] There we go.
[24:20] So now we've got the with the bone deform and that's going into the
[24:26] we've got the point transform that's going into the bone deform using the rest geo and the
[24:32] reskeleton and then that's going to base dot shape.
[24:35] So now that we've got this base dot shape in the output, we should be able to see it in the viewport.
[24:41] So as you can see here, now I've got my controls and I can control this thing and the mesh is also being deformed.
[24:52] You just hide the controls if you want to see the final mesh.


### Subgraph - Squash & Stretch [25:00]
**Transcript (timestamped):**
[25:00] Okay, so now that we've got a skeleton set up, let's build a sub graph.
[25:04] A sub graph is like a HCA that you can use in in apex so you can access it in the tab menu.
[25:10] But first we need some logic that we can put into that sub graph.
[25:13] So let's let's build a squash and stretch setup.
[25:17] So I'm going to use the written tip for my control for my main controls and then I'm going to drive the scale and
[25:24] position of the mid control.
[25:26] And for this to work, I'm just going to have to change the hierarchy a little bit.
[25:30] So I've got my my tip is still parented to my mid control and I'm going to get some dependency loops here if I'm if
[25:36] I'm going to be driving this midpoint using the tip.
[25:40] So let's go to the skeleton.
[25:42] I was just going to add a reparent or a parent.
[25:46] Sorry.
[25:50] And then what I'm going to do here is just just unlock that.
[25:57] And then I'm going to parent the tip to the root.
[26:01] Okay.
[26:03] So now if we look at this last component of press enter, like I can see that now the parenting has changed.
[26:11] And that's what's nice about components is that like once you set them up, it'll run through this whole network and
[26:16] everything will still still connect up and work even though you're changing the hierarchy upstream.
[26:23] Okay, so let's build our red logic.
[26:27] So.
[26:30] I'm going to use unpack folder again.
[26:32] So it's just the rig.
[26:34] And then I'm going to do an edit graph so I can actually change the graph.
[26:40] Okay, let's make this larger.
[26:43] So what I'm going to do is I'm going to get the midpoint between the root and the tip first.
[26:48] So let's do a loop.
[26:51] And the X form into a that X form into B.
[26:56] And set this value to 0.5.
[27:02] And then I'm going to plug that into the mid control because I want to be able to.
[27:07] Drive this control, but also, you know, control it after it's been set.
[27:11] So let me just show you what it looks like if I just constrain it and what happens in the viewport.
[27:18] So first I need to pack that folder back in.
[27:21] So I've got my rig outside of the main stream here.
[27:24] So I need to pack it back in.
[27:27] So I'm just going to say base dot rig.
[27:30] So now we'll override the rig that's in there with this new edit.
[27:33] So the one I'm going to press the pose button so it can create a scene animate node for me.
[27:39] Okay, so now if I move it, you'll see that that position is being set and that's great, but I can't actually move this control.
[27:45] It's it's constrained.
[27:47] So what I'm going to have to do is I'm going to have to calculate the local transform for that for that new position based on the route control as a parent.
[27:59] And then I'm going to set that to the rest local of this mid control so I can still drive the control after it's being set.
[28:05] So I'm going to do an extract local.
[28:08] Then I'm going to want this position and I want it to calculate the local based on this parent on the route.
[28:17] And then I'm going to set this rest local over here and unplug the X form.
[28:24] Okay, so if we go back here, you'll see now I can move this on.
[28:30] Let me just reset the animation state.
[28:32] Can move this and we can update that midpoint.
[28:37] Which is exactly what we want.
[28:41] Okay.
[28:43] So now we want to do the scaling.
[28:46] For that, I'm just going to calculate the distance between the two between the deformed position and the rest position.
[28:54] So I'm just going to do an explode here.
[28:58] Explode transform.
[28:59] Get the local transform for the route and get the local transform for the tip.
[29:07] And then I'm going to do a distance.
[29:11] From the transforms.
[29:13] I'm going to duplicate this and I'm going to get the rest, rest transform.
[29:17] So the rest local for that one, rest local for this one.
[29:22] Now all I need to do is just get the difference between it.
[29:25] So subtract these two floats from each other.
[29:31] And if this value is now at rest, it's going to be zero.
[29:34] So I don't want the scale to be zero.
[29:35] So I'm just going to add a float.
[29:40] And set that to one.
[29:42] Okay.
[29:44] So this value will most likely if I if I move it to the left, I'm going to get the rest.
[29:49] So you will most likely if I if I move it too far, it's going to probably scale below zero.
[29:54] So I want to just clamp this float value.
[29:58] I don't actually want that scale to go below a certain value.
[30:02] So I'm just going to say point two over here and I'm going to say one or 10 over here.
[30:09] So point two for men, 10 for max.
[30:13] And then I want to convert this from a float to a vector.
[30:20] So I can create a scale value out of it.
[30:23] I'm just going to scale the X and Y axis and I'm going to leave the Z axis alone.
[30:27] Just set that to one.
[30:29] And then I'm going to build my transform.
[30:33] Like that into scale.
[30:36] And now you've got a little system that calculates the scale based on the distance and I've got my position in between the two joints and I just want to multiply these together.
[30:47] So I multiply my local transform to my scale and then I'm going to plug that into rest local.
[30:58] Okay, so now if we reset this, you can see if I move this now, you'll get scaling.
[31:05] It's the wrong way around.
[31:06] So let's just quickly edit that and I can just do that by flipping the subtraction here.
[31:11] Reset, move and now you've got scale and it stays at point two for its scaling when it gets too large.
[31:22] Okay, so let's go back to the graph.
[31:26] Now we need to make a sub graph out of this.
[31:28] So we've got our bunch of nodes here, but it's very messy and you're not going to want to create this every time you want to do it.
[31:37] You're not going to want to create this every time you want to do a scale setup.
[31:41] So what I'm going to do now is just collapse this into a subnet, so press Ctrl C and then you can see or like just off of the back, like you can see it's a lot cleaner.
[31:54] And if this is only if this is the node you have to deal with for a squash and stretch, then it would be way nicer to work with.
[32:01] So I'm just going to jump in here and change some of these names just so it's a bit easier to see.
[32:08] So I'm just going to say X form A, X form B, local X form A, A and B.
[32:26] Okay, and then for my output, I'm just going to say X form.
[32:35] Okay, so now we've got our network and just minimize that.
[32:41] You can see it's updated it now.
[32:43] It's got the new names and it's unplugged itself because the naming is different.
[32:48] But essentially, if you just plug these in again, it will work.
[32:53] So now I've got my A control and B control and I can plug them in here.
[32:59] But let's create a subgraph.
[33:01] So to do that, I'm just going to isolate this node.
[33:05] So I'm going to use a blast because these are all points.
[33:07] I'm just going to delete by point.
[33:10] I'm going to say let's first name that joint.
[33:14] This node is going to name it squash.
[33:19] And then I'm going to delete that one.
[33:23] So I'm going to say delete name equals squash.
[33:26] And you can see now it's gone.
[33:27] So I'm just doing delete non-selected and I've got it isolated like this.
[33:31] Then what I'm going to do is just pack it into a folder.
[33:35] And I'm just going to set this to be squash.
[33:45] I'm not going to pack this up and it's going to leave it as is.
[33:50] And I'm not going to give it a type.
[33:52] It's just the easy way to name that primitive.
[33:55] And then I'm going to do a rough output geometry.
[34:00] And I'm going to save that to my hip directory.
[34:05] So hip, Ipxgraph.
[34:10] And then squash.pgo.
[34:18] And then I'm going to save that.
[34:21] And now we need to reload our Houdini session for that to update.
[34:27] So I'm going to quickly do that.
[34:29] So now we've loaded that scene.
[34:32] Let's go have a look in our hipxgraph.
[34:39] So now we've got our subnet over here still and we should be able to press tab and do squash.
[34:45] And there you go.
[34:47] So now we've got our very own tool that we can use in Apex and we can plug that in.
[34:52] And it'll just work.
[34:56] Another thing you can do now with this and why you're doing these subgraphs is that you can use a component node to add these and plug them in.
[35:08] So I'll be going over some of those add nodes in the chicken rig.


### Chicken Rig - Walkthrough [35:15]
**Transcript (timestamped):**
[35:15] Now that we know a little bit about components and subgraphs and how to set up a rig, let's look at how the chicken was set up.
[35:22] So I'm just going to go over the elements quickly.
[35:25] So just the capture mesh, the capture skeleton, the control skeleton, which is derived off of the capture mesh.
[35:33] And then the post shapes that I'm going to be using to drive the eyes with those then get all packed up.
[35:42] So base shape, base skeleton and pose skeleton.
[35:50] Over here, I'm creating an FK transform again to initialize the rig.
[35:55] So you can see.
[35:57] I go into the view state pressing enter.
[36:02] This will create the transforms for my skeleton and my point transform and output my skeleton.
[36:11] And what I'm doing here is like before, I'm just outputting the controls and I'm excluding some of the controls that I don't want to see in the view state.
[36:22] And as you can see here, like it's a little bit large because the chicken is small, so the controls will be overlapping a lot.
[36:30] So what I'm doing here is just adding configure controls node and scaling it to 0.2 and I'm applying that to all the controls.
[36:41] And as you can see here, I'm not using the guide skeleton for this or the guide source because I'm going to be setting up the control shapes a little bit later.
[36:52] So then we create a bender form and this is still set to default.
[36:59] So it's just adding that bender form node.
[37:01] And then over here, we're connecting our controls like we did in the demo and I'm just connecting all the controls and excluding the twist joints.
[37:10] So exactly like we set up in the component demo.
[37:16] Let's have a look at that rig.
[37:21] So here you can see we've got a lot more nodes in here.
[37:25] And this is the reason why we are using components, component scripts to set up all the the rig logic and to plug nodes into each other and add new nodes.
[37:36] It just becomes way simpler to set up a single component than it is to manually change the rig every time something updates upstream.
[37:48] So initially the components might look very intimidating and complicated, but it becomes a lot simpler later down the line.
[37:59] So you have got a set rotation order from Atrib and this is a good example for how to fetch data from the skeleton and then set that on the transform objects or whichever object you want.
[38:13] But in this case, I'm fetching the rotation order attribute that I'm sitting on the skeleton up here.
[38:19] So here I've got my rotation order and I've set it to three and I get that value, the rotation order value from a rig pose.
[38:28] And you can just look at this value over here.
[38:30] So if you get to this drop down, this is the rotation order value that you can get.
[38:34] And this is also your transform order.
[38:39] So now that I've set that value and I've set it on the foot controls, I'm going to show you how I actually set that on the transform object.
[38:49] So let's have a look at this component.
[38:54] So in here, I'm initializing the components, I'm bringing the rig in and I'm updating the rig.
[39:03] And over here, what I'm doing is I'm getting the base skeleton from that character primitive and then I'm looping over all the points in it.
[39:15] And then getting the name for each of those points to find the node that I want to apply the data to.
[39:22] And then I'm getting the rotation order attribute and then building a dictionary which I then update that node with.
[39:28] So over here, you can see my rotation order and I'm plugging that dictionary into the palms, which will update that node.
[39:37] Over here, you can see there is that rotation order that I'm setting.
[39:43] And finally, I'm updating it.
[39:45] And then let's go have a look at what's actually happening on the nodes.
[39:50] So to view these nodes, I'll just show what that looks like if you just view this graph again.
[39:57] As you can remember, it's quite daunting as there's a lot of transform objects and to find the right one can be quite tricky.
[40:05] But because this is all geometry, so if you have a look over here, it's all just geometry and it's points with name attributes on it.
[40:14] And the name attributes match the transform object name.
[40:19] So what I've done is I've built a little subnet where I can give it a group and it will isolate the two nodes that I want to that I've specified here and whatever is connected to it.
[40:34] And to explain how I'm doing that, I'm just going to dive in here.
[40:38] I unpack the folder.
[40:40] And then I group those two controls by name.
[40:45] And then I do a group expand, which will find all the nearest points connected to it by a primitive.
[40:53] And the way that Apex knows what's connected to each other is that each point has vertices on it, which will be the connected ports.
[41:03] And then each primitive will be the wire in between those ports.
[41:10] So because I know that they're connected like that, I can expand the group and I can find all the connected nodes.
[41:16] So now if I do a layout over here, I just delete that group, do a layout and I can see now I've got my two nodes and whatever they plugged into.
[41:25] So nice to see them in context rather than just isolating them.
[41:31] Okay, so now let's look at that attribute.
[41:33] So if I press P and I scroll down, you can see over here, I've got my rest local that's been set and I've got my rotation order, which is now set to three.
[41:44] So the default, if I select the control or the root control, you'll see that that default is zero.
[41:51] So now I can just update that parameter up here and any rotation order on any of the controls will be set for me.
[42:04] Okay, so now let's get to the legs.


### Chicken Legs - Pole Vector Look-at [42:08]
**Transcript (timestamped):**
[42:12] Okay, so this leg is a normal smooth IK setup on the inside.
[42:22] The difference is that I'm adding a automatic pole vector.
[42:26] So you can see I've got my control joints.
[42:28] I've got my driven joints just like the smooth IK and then you have got my pole vector and a override IK tip.
[42:37] This will just control, will add an extra transform object to the tip of the IK so I can control that individually.
[42:47] So for the auto pole vector, how that works is that what I'm doing is I'm getting a midpoint between the root and the ton.
[42:57] And I'm setting that pole vector.
[42:59] So if I now, if you have a look at this control over here, if I just move, if I just enable the right leg,
[43:05] you can see that now that control is jumped up to here.
[43:09] So it's finding that midpoint and then offsetting it by minus 0.4.
[43:15] So if I make this 0.2, you'll see that it'll move closer to the middle point where it used to be.
[43:23] And if I make it 0.4, it'll move back to that position.
[43:26] And the up vector will just determine in which axis it needs to move forward.
[43:32] So like if I go minus one over here, you'll see the leg will flip.
[43:38] Okay, and then just show how that works.
[43:40] Let me just select the leg here.
[43:42] So the foot's not connected yet.
[43:44] So we just, we're just looking at what's happening with the leg.
[43:48] So you can see that that pole vector is now always sitting nicely in between the root and the tip of the IK.
[43:56] And it'll also rotate in the plane of the IK.
[44:02] And we can also move it, obviously.
[44:07] Okay, so let's have a look at what this network is generated before we go into the component.
[44:14] So I'm going to use my viewer here.
[44:18] And then I'm going to change this name here to the name on the component that I've set.
[44:26] Okay, so change that and say star.
[44:30] Okay, so what's happening here?
[44:37] Let me just make that a little bit larger.
[44:39] So I'm going to work backwards so you can just see what it's affecting and then work my way backwards.
[44:45] So here I've got my hip and my knee, and that's being controlled by the smooth IK.
[44:50] The tip is not connected because I'm actually driving that with another control.
[44:56] So here you can get the twist driver control.
[45:00] So here's that look at and the look at's being driven by the rest local from this pole vector blend,
[45:09] which will blend between a, that look position between the root and the tip.
[45:17] And the A position that is connected to the pole.
[45:20] So like a parented position.
[45:22] So I can blend between either having the pole vector attached to the pole,
[45:28] this automatic pole vector.
[45:36] Okay, so this look at control, I'm going to be using a lot throughout this rig.
[45:41] It basically just does a look at with a root offset for you.
[45:46] So in this case, I'm not actually using a root offset.
[45:49] I'm just overriding it.
[45:51] So just doing a straight look at, but I just make sure that the root and the tip of these two controls are always aligned
[46:00] and looks at each other.
[46:02] So when I do a loop, I won't get any flipping.
[46:09] Okay.
[46:11] So now for the ankle look at, so I'm just going to select the eye look at at the bottom here.
[46:16] So we can, these are all using the same, the same component.
[46:20] So I'm just, it's just feeding through.
[46:22] So this one's going into that one, that one, that one, that one.
[46:25] So it's using all the same component.
[46:27] It's just a neat way to organize it.
[46:30] Okay.
[46:31] So now looking at the, this ankle look at it's, it's using that look at control again inside.
[46:38] And it's just calculating the offset to this poll vector because I want the poll vector to be over here.
[46:46] But I want this ankle rotation to stay the same.
[46:49] So it will calculate that offset.
[46:51] So I don't have to worry about it actually shifting its rotation and to show what that does.
[46:59] I'll select the ankle or control.
[47:02] If I change that root aim amount to be completely aiming at the, at the poll vector without that root offset,
[47:11] you'll see that this is what it'll actually look like.
[47:15] So that's not really what I want.
[47:17] So I just want that, that rotation to stay exactly the same.
[47:20] Doesn't matter where I put the poll vector and now it'll be working as expected.
[47:29] And in the parameters here, you can see I've got my root control and tip control.
[47:33] And this will just work out the, the look at between a root position and a tip position.
[47:39] And then I'm setting a driven control based on the roots child.
[47:45] So like there'll be another control under the root, which will then actually be driven to, to drive the tip.


### Chicken Eyes - Look-at Control [47:53]
**Transcript (timestamped):**
[47:53] So that's the look at control.
[47:57] Let's just look at the eyes quickly.
[47:59] And over here you can see I've got my root, root aim amount set to one for that, for this eye over here.
[48:08] And if I set this to zero, you'll see it, it's going to flip around because that's its original rotation.
[48:14] But I wanted to override that rotation completely.
[48:16] So I just wanted to set it to one.
[48:20] And you can see it's doing what it's supposed to do.
[48:26] And for the leg twist joints, you can't really see what it's doing in the, in the actual viewer state.


### Chicken Leg - Twist [48:30]
**Transcript (timestamped):**
[48:37] So I'm just going to have a look at this component.
[48:39] I'll just walk through a little template that I've set up.
[48:43] So with the, the normal network where I'm adding nodes and I'm setting dictionary data and adding the twist on twist node.
[48:53] So over here.
[48:54] So this network here is doing exactly this.
[48:58] So what this, what this twist is doing is it's calculating a, an alert position between the root and the tip.
[49:08] And I'm setting that bias.
[49:10] So it can be point three and point six, six, you know, like how you would get the, the different values between different joints.
[49:18] So imagine this is my root and tip.
[49:20] I'd get my, my position over here and my position over here based on the rotations.
[49:25] And I'm then just doing a look at to line up those, those twist joints so they don't rotate weirdly when this, this node changes its position.
[49:37] So they're always aligned very nicely to, to the, to the tip.
[49:43] So that's what this twist is doing.
[49:47] It's not a very procedural setup.
[49:49] I'm going to definitely change it in the future.
[49:52] It can only handle two joints at this stage.
[49:55] So I want to be able to have as many joints as I want and they should just twist properly.


### Chicken Toe - Look-at Metacarpals [50:02]
**Transcript (timestamped):**
[50:02] So for the toe meter, what this component is doing is it's creating a, a ghost parent joint.
[50:13] So if I just select this parent, like you can see, I've got my, my look at control over here for that, for that, for this joint.
[50:20] And I'm not actually rotating the parent of this one.
[50:25] I've created a in between transform, transform called the FK transform.
[50:30] And then I'm using that transform to now set the, the rotation of this one.
[50:36] So it's essentially like changing the pivot of it and then rotating it.
[50:41] So I didn't have to set up multiple joints.
[50:44] And this is really nice for, and what I, what I originally set it up for was for the eyes.
[50:50] But then because I, because I've got so many joints and I didn't want to create multiple roots, but then I opted for the blend shape method for the eyes.
[51:00] So, so I ended up, I ended up creating all those roots for that.
[51:06] Okay. So that's the toe meter. And you can see in here, you can just give it a control list to get one rate and you give it all the controls you want to, want that, want to use that rate.
[51:17] And then it will automatically set up the, the lookout constraints for you.


### Chicken Neck [51:26]
**Transcript (timestamped):**
[51:26] Okay. So then for the spine and the neck.
[51:29] This is very similar to the normal, normal spine, the normal spine is way more procedural than this one.
[51:37] The only difference with the normal spine setup and this one is that I've got squashes stretch built into this one.
[51:45] So I had to limit it to four joints. So you can't, you can't have five joints for the spine. You can only have four.
[51:52] And, but we've got this, we've got the squash and stretch setup. So I'll just quickly show what that's doing.
[51:59] If you move it, so it's set to very subtle over here. So if I change this value to say minus one, it will now scale down significantly.
[52:08] So you can see there, it's actually doing a proper, proper squash.
[52:14] So that's what this spline is doing.


### Chicken Face Pose Blend [52:19]
**Transcript (timestamped):**
[52:19] Okay. Then for the face pose blend, what I'm doing here is like I said before, I'm doing a blend shape.
[52:27] So I'm just fetching all the, all the poses from that skeleton, from the pose skeleton.
[52:34] And I'm doing a weighted blend as packed primitives on them.
[52:40] So to better explain that, I'm going to show the setup up here by the actual pose shapes.
[52:48] So here I've got my bone deform and I've got my primitives coming in.
[52:55] So here's all my packed primitives.
[52:58] And I'm just setting the weight attribute on one of these primitives to drive that, that blend.
[53:05] And what I'm blending is, and let's just have a look at the blend shape here.
[53:10] I'm blending the local transform and I'm setting the pose blend ID just to be able to know what point I'm blending.
[53:20] And then over here, I've just set this, this multi palm up to be, to have one input that I'm setting to one.
[53:30] And this will make sure that all those weights are blended in.
[53:35] So the trick with this though is you can't just blend the local transform and it will deform this, the skeleton.
[53:42] So the trick is to compute the transform.
[53:44] So compute world from local and this will, this will make it so that this blend shape actually works.
[53:50] So if I switch this off, you'll see and nothing, nothing will happen.
[53:56] Okay. So let's go back to the face pose blend.
[54:02] And have a look at what that network is actually generating.
[54:09] So here, I mean, if you look at the parameters, you can just see the face, the pose joints that I'm blending with my blend group,
[54:18] my point ID that I'm setting and the, the, the folder that I'm using for the blend shapes.
[54:24] Okay. So over here, I'm just going to set this with that name is face.
[54:28] So I'm just going to set this to face.
[54:33] Okay.
[54:35] And you'll see that there's, there's a lot of extra joints that are coming in because they're all called face.
[54:41] But the ones that we want to be looking at is this face prim weights.
[54:47] So this is like the, the attribute wrangle where we were setting all our weights on or our weight attributes.
[54:57] So it's setting a, the weight attribute by name.
[55:01] And it's using that pose to feel it.
[55:05] Yeah. It's using that pose skillet and geometry to set those weights on.
[55:11] And then that goes into the, into the array that goes into the blend shape.
[55:17] And then we're computing the transform just like the setup before.
[55:21] And here the only difference is we actually have to fetch that local transform and then set that onto our face.
[55:29] I joined using the rest local because we still want to be able to control this joint afterwards.
[55:38] Okay. So that's the basic setup on that.
[55:45] In here you can see our component.
[55:51] You can see where I've set up the dictionary for that blend shape.
[55:57] So this is just like before we're just creating all those nodes.
[56:01] Here I'm setting up the dictionary.
[56:04] And as you can see, this is what a multi-palm setup would look like.
[56:09] So what my, my blend one value, my blend two value, so the hash is just the number.
[56:14] And then I've set this to one and then I'm building that dictionary array.
[56:18] And then that's going into the build dictionary as end blends.
[56:23] And then I'm setting that on the parameters of the pose blend shape.
[56:28] Another thing to note is I've got all the names set up for the parameters that I'm exporting.
[56:34] So we can have a look at that quickly again.
[56:38] Over here.
[56:40] So with all these names over here and they promote it nicely with the correct names and the weights are also set up exactly the same.
[56:48] So all these names need to be set.
[56:50] So what I've done there is I'm looping over that, that package here.
[56:56] So over here, I'm using the base dot pose.
[57:01] Just to note, the fine character element is a better, better note to use for this.
[57:07] That's the newer node.
[57:09] I was using this node when I was building this rig.
[57:12] So, but here we're getting the base pose.
[57:16] And then I'm looping over each of those, those primitives and getting their names and then using those to promote the parameters and set attributes on the weight.
[57:31] Attribute from, from Prem.
[57:34] So this one set Prem attributes.
[57:38] Okay.


### Chicken Pose Blend [57:40]
**Transcript (timestamped):**
[57:40] So now, now that we've got this face set up.
[57:46] And let's have a look at the pose, the controls.
[57:54] So in the settings here, you can see I've got all these different axes.
[57:59] So what this is going to do is it's going to take one of these controls like this one.
[58:05] And it's going to take one of the axes and map it to a float value that I can use for the weights.
[58:13] So here you can see I'm mapping I pose, lead up, L control.
[58:18] And that is the one that I'm selecting at the moment.
[58:22] And I'm mapping it to y negative.
[58:25] So if I move this one in y negative, we'll see that it's, that it's actually driving that weight attribute.
[58:34] So that is what, what this node is doing.
[58:37] And internally, let's just isolate those nodes so we can see what we're creating.
[58:43] I'm just going to isolate this node.
[58:48] So that's all we want to see.
[58:53] Here you can see now I've got this overridden one of the, one of the parameters.
[58:58] So see that they're all exposed to these float values.
[59:02] But in order to drive these, I need to, I need to have a control attached to it.
[59:06] So either need an abstract control or I need a normal transform objects parameter to be able to drive them.
[59:13] So here I'm using the I pose, lead up, L control and I'm piping it into my remap sub graph.
[59:21] And in here, I'm just splitting out all the different float values and I'm remapping them to be absolute values.
[59:29] So I can remap the negative values to be positive and clamping them and then piping that into the float value on the face prim weights.
[59:41] So that's what this, what the setup is doing.
[59:44] And if I go down the stream here, you can see how nice this is now.
[59:49] Like I just set up one component and I can apply it to multiple things.
[59:53] So I just keep on adding it and adding it.
[59:57] So it looks like a lot of nodes, but all it is is just separate parameters for the same component.
[60:04] So here you can see now I've plugged all of them in.
[60:09] Okay, so now I've got that set up.
[60:13] Let's just have a look at what that's doing.
[60:15] And now if I select one of the face controls, you can see it's driving those joints using a blend shape.
[60:22] And this one will do the blink and this one will do the angry, angry and sad.
[60:31] Yeah, so now for the IKFK blend.


### Chicken IK-FK Blend [60:34]
**Transcript (timestamped):**
[60:37] What I'm doing here is, and I'll show this in this stash, is it's a little bit simpler to explain.
[60:43] I'm not going to go through the whole component, but I'll explain what it's doing.
[60:48] So let's just frame that a little bit larger.
[60:52] So what I'm essentially doing is I want to do a local blend, so a local transform blend between the IKFK and these IK controls.
[61:05] And as you can see, I've got these FK helper joints.
[61:10] So what this is is just a FK hierarchy representing the positions of my IK controls.
[61:19] So I'm overriding these guys positions by using the IK controls.
[61:26] And that way I can get a local transform that matches with the FK controls up here.
[61:34] And then I can easily blend them.
[61:37] So it's actually quite a simple setup. It's just a bit of a brain scratcher.
[61:45] So over here, I've got my another thing that I need to mention is with the IKFK setup is that we are creating a abstract control.
[61:59] So the abstract control is going to drive the float values for the blend between between IK and FK.
[62:11] So just like I used the controls for the face up here and converting those values, the abstract control will be able to receive float values and then update those values based on what I'm doing to the control.
[62:30] So let me just see if I've got my setup here.
[62:34] Let's just view that quickly.
[62:38] So I'm going to just view the name over here.
[62:52] And then I'm just going to add that abstract control.
[62:57] So that abstract.
[62:59] Okay.
[63:01] So over here you can see I've got these abstract controls.
[63:10] So what the abstract control does, so remember when I replaced my float values with the transform values.
[63:17] So in this case, you can keep your float value there.
[63:20] You just need to feed it into an abstract control.
[63:25] And then you need to give the abstract control a position.
[63:29] So I've created these IKFK or FK IK switch controls, which live in my skeleton control hierarchy.
[63:37] And I'm just giving it that position.
[63:39] So this just says where it's supposed to be and what it's attached to.
[63:43] And this is the value that it's going to be driving.
[63:45] And this value here is also plugged into an actual blend.
[63:50] So you can see in this bias.
[63:52] So that same value is plugged into the bias.
[63:55] This one will just be driving this parameter.
[63:58] So nothing is set up on this control yet.
[64:02] So I haven't set up any parameters, but I'll do that in a second.
[64:09] So you have got my look at control.
[64:12] The hip look at control will just make sure that the hips will stay intact when I do weird things with the knees and the legs.
[64:23] We'll just keep that rotation a little bit more stable.
[64:29] Okay, so here I've done some cleanup on it on the rig.
[64:32] This is not really necessary.
[64:34] If you have a look at the graph here, what I've done is I've just unplugged all the controls from the output.
[64:44] So let me just start over here.
[64:48] If you look at this output, you can see like I've got all these, the normal, the capture joints being deformed by the point transform.
[65:00] And then if I select, if I disable this, you'll see how many more controls we have.
[65:07] So if I enable, I'm reducing it and increasing it.
[65:12] So it's just unplugging the control hierarchy from the point transform because I don't necessarily want to actually deform them.
[65:19] I just want to use them to deform their main joints with.
[65:24] So just clean that up.
[65:26] Okay, and now we can actually configure the joints.
[65:31] So over here, it's just a configure, configure controls node like I used before at the beginning.
[65:41] But what we're doing here is we're actually going to set up all the controls for it.


### Configure Control Shapes [65:42]
**Transcript (timestamped):**
[65:47] So if I press enter, enter that view state, you can see, yeah, I've specified all the scales and like select the name, select the scale.
[65:58] And I can override the shape.
[66:00] So you have done a shape, shape override on the pelvis to make it a box.
[66:04] So here you can set up all those controls.
[66:08] But like I said in the component demo, the attach joint, your method is a much nicer way to set up your skeleton if you have a predefined skeleton that you that you've built before you plug it in.
[66:22] But if you create any kind of controls or joints in your apex network, then this will be a really nice way to set that up.
[66:29] So you can see here I've got my custom controls.
[66:33] So I'll just go in there.
[66:35] Here, I've just added them to merge them all together.
[66:40] All that this needs is a primitive name.
[66:44] So each control just has its own primitive name and then you can use it in the configure controls node.
[66:54] Second one here was just so I can organize which nodes are visible and which are not visible so I can turn visibility on and off on some of them.
[67:06] Okay. And I said we're going to configure the abstract controls later.
[67:12] So I put that into the configure controls section.
[67:15] So over here, what we're doing is we're setting some some values on it, some a minute max values because we just dragging on the X, so zero and one, and then I'm locking that range so it doesn't go past that.
[67:31] So that's kind of what's nice about this abstract control is you can actually limit how far you can drag it.
[67:40] And then over here, I'm setting the control parameters.
[67:44] I've got my dictionary properties and I'm setting up all the things that need to be set up for the actual abstract control.
[67:57] I do have a different example of this whole setup.
[68:01] Let me just jump to the lucha quickly.
[68:05] In this one, what I've done is I've just taken all those extra dictionary values that I've set afterwards.
[68:11] I've just included them in the actual component.
[68:16] So if you go to the IKFK blend of the lucha, you'll see in here all those dictionary values are all set up over here.
[68:24] And then then you don't have to create them afterwards.
[68:27] So you can see it's a little bit cleaner.
[68:32] Okay, so back to the chicken.
[68:35] Okay, and then over here, I'm just setting some some control colors.
[68:40] But if you're using the attach join geo method, like the control colors will come through in any case.
[68:45] But this is just a nice way to see how hard to manipulate the dictionary data for the control shapes.
[68:58] So here I'm applying material to this rig.


### Control Shape Material & Colour [69:00]
**Transcript (timestamped):**
[69:01] So like I want to do some tests.
[69:03] So I just want to add a material so we can do some animation and actually see what the textures look like.
[69:09] Let me just switch that on.
[69:11] Then over here, what I've done is I've just unpacked the shape.
[69:15] So you have to unpack it first, then you apply the material and you have to have the material network in the in the scene that you in.
[69:24] And it has to have a relative path.
[69:26] So it's going to look at this path still.
[69:28] So it doesn't matter how you set up your your rigs.
[69:31] This material is not going to go with your rig when you're exported.
[69:34] So you always need the mat in there.
[69:36] And then what I do then is pack it up.


### Output & Export Rig [69:40]
**Transcript (timestamped):**
[69:40] And then now I can actually go look at the animation state and see what's happening with my rig.
[69:48] Move all my controls and test that everything's working and see that the IKF care is working.
[69:58] And everything works like it should.
[70:02] Okay.
[70:04] And then for your animators, like they're not going to be dealing with this whole graph over here.
[70:08] So what you're doing for them is you exporting the whole rig as a BGO.
[70:14] So this is just a straightforward BGO and that then gets loaded into a scene like over here.
[70:25] So let's just let that load.
[70:28] Okay.
[70:29] So over here with my my literature and my chicken.
[70:33] And as you can see, I do have a material in there because the material is still in my in my network.
[70:41] But if it comes in and it's and it's gray, you just have to apply the material again.
[70:48] So over here, I'm just applied the material and I've set that that met it up the same way I did with the rig.
[70:57] And then that goes in and I can animate my scene.
[71:03] And then to output your geometry is the scene invoke.
[71:08] And the scene invoke, you can just say you can just look on this output all character shapes and then it'll output all the characters that are in there.
[71:17] You can also if you just want to skeleton, you can set this to skeleton.
[71:23] Yeah.
[71:25] So that's the end of the demo.
[71:27] I hope this is helpful and enjoy rigging.



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
