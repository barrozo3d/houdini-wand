---
title: H22 - KineFX Rigging and Animation | Max Rose | Houdini 22 HIVE
source: YouTube
url: https://www.youtube.com/watch?v=2jZjaEzLdco
author: Houdini
ingested: 2026-07-19
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/h22---kinefx-rigging-and-animation-max-rose-houdini-22-hive/
frame_count: 0
frame_status: pending-selection
---

# H22 - KineFX Rigging and Animation | Max Rose | Houdini 22 HIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=2jZjaEzLdco)
**Author:** Houdini
**Duration:** 25m5s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py h22---kinefx-rigging-and-animation-max-rose-houdini-22-hive <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro & Jack in the Box Showcase [0:00]
**Transcript (timestamped):**
[0:00] What's up everybody?
[0:06] I'm Max.
[0:09] I work at SideFX.
[0:11] And, you know, I was planning on originally doing this live, but fortunately I was talked
[0:17] out of it.
[0:18] Because I like doing live presentations.
[0:21] I really don't like doing slideshows.
[0:23] It's hard to...
[0:24] If something goes wrong, you're screwed.
[0:28] Anyway, whatever, I'm going to do this as a slideshow.
[0:31] Try to keep it entertaining.
[0:32] Hopefully this could be short.
[0:33] I think it's going to be like 15 minutes.
[0:36] But what we're going to talk about is how to make this, which is a jack-in-the-box.
[0:41] But not just a jack-in-the-box.
[0:42] We're going to do it in Houdini 22.
[0:44] So, yeah, why don't we go ahead and watch the actual animation first.
[0:49] And then I'll talk about how I went about making it.
[0:55] Charming, right?
[1:08] Thanks everybody.
[1:09] Wow.
[1:10] I was not expecting applause.
[1:11] So, yeah, we're just going to let the animation play out for a little bit.
[1:15] I'm going to talk over it.
[1:16] But the idea here, well, I mean, you know, Fiona came up and asked me to make something.
[1:22] I figured what better than a jack-in-the-box to kind of illustrate some of the new features,
[1:28] the animation features in 22.
[1:31] Because what's really cool here is that there's really just a couple of keyframes driving
[1:35] this whole thing.
[1:36] I think maybe two keyframes.
[1:38] And the rest of it is just coming from, you know, whether it be ragdoll, secondary motion,
[1:44] and everything is dynamically driven from just that base animation.


### Rigging the Spiral Spring in KineFX [1:50]
**Transcript (timestamped):**
[1:50] So let's talk about the rig.
[1:51] Actually, if you're here for rigging, sorry to disappoint you, but this rig is actually
[1:56] very, very simple.
[1:57] The doll, really, it's just like a very simple FK setup.
[2:00] Well, what's nice is that everything in the doll is driven by all that dynamic motion,
[2:05] right?
[2:06] So I really had to do very little for the doll.
[2:09] On the box, it's a little bit different.
[2:13] Pretty much just FK for the most part.
[2:15] But there was one little trick that I actually had to do to get this to work.
[2:19] So as I mentioned before, the majority of the box is just FK, right?
[2:23] Just a little twisting motion, opening the top.
[2:27] That's just FK.
[2:29] But when it came to actually animating the spring, I needed to animate these spiral joints,
[2:34] right?
[2:35] But obviously I couldn't animate it like this, just lifting up one joint at a time.
[2:38] So what I needed was like a centerline to go down these, you know, to go up through
[2:44] the spiral and then grab onto those joints.
[2:47] So if you guys ever wondered how you can animate a spiral, a reg one, this is actually how
[2:52] you're going to do it.
[2:53] So you take these existing joints and you just crunch them down, right?
[2:59] In the X and Z axis and you just leave your Y.
[3:01] And then you have your centerline.
[3:03] And then obviously you want to change the names of those, right?
[3:05] So you go through and change all the names.
[3:07] And that gives you that nice centerline.
[3:11] And then you just go through and just re-parent everything.
[3:13] So this is just two different groups.
[3:15] I'm not going through and re-parenting, you know, one by one.
[3:18] If you throw down a parent joints node and every in you group one, right?
[3:25] So I have a group as the center joints and then another group for the radial joints.
[3:30] And because they share the same point number and they have the same number of joints in
[3:36] each group, it automatically just parents every one of them.
[3:39] So it's pretty quick.
[3:42] It's really just in the, just two different groups and the parent joints node just takes
[3:47] care of the rest of it.
[3:50] So here's the final result of that.
[3:53] So yeah, you can see now just by playing with that Y axis, I can really get that, you know,
[3:58] that springing motion.


### Combining Rigs & Packing into Apex [4:01]
**Transcript (timestamped):**
[4:01] So okay, these two models were made completely separately.
[4:07] And this is kind of like the initial problem, right?
[4:09] I actually had to combine both of these rigs.
[4:12] So, you know, everything was modeled in Houdini, you know, textured, whatever, but, you know,
[4:19] all the skinning, everything was like done completely separate from each other.
[4:22] So I actually had to go through and combine these rigs.
[4:25] This is obviously very easy.
[4:28] All I had to do was just take the doll and just put it into position.
[4:33] And then, I mean, yeah, once the doll is in position, I just parented the root joint of
[4:38] the doll to the last joint of my spiral.
[4:43] And just a note here, it's a good idea to do this outside of apex, right?
[4:48] I'm not in apex yet.
[4:50] It's a good idea to do it with kin effects, because once you actually go into apex after
[4:55] doing this, all of your matrices are all set up, right?
[4:59] You don't have to go through and I don't know, do any crazy matrix math to kind of, you know,
[5:06] because when you're parenting things, things can get a little tricky when you're in apex.
[5:10] So when you're doing it in kin effects, it kind of just takes care of all of that for
[5:13] you.
[5:14] So yeah, pro tip, do all your parenting in kin effects first and then jump into apex.
[5:21] Typically, that's the way I like to work.
[5:24] So after that, it was just a matter of plugging in the geo and the joints into an apex pack
[5:30] character node.
[5:31] And then of course, you want to turn on a FK and bone deform components within the actual
[5:37] pack character node.
[5:38] And then yeah, I had my like 90% of my rig done.
[5:43] So the next step I needed to do was to create that spline, right?
[5:46] So I tag that center line, right?
[5:48] Called a coil.
[5:50] And then I throw down an auto rig component and using the spline, I select that coil tag,
[5:56] which creates the spline going down that vertical joint chain.
[6:00] So then I just go through and I set the curve order to three, the joint of the control count
[6:04] three, and it just gives me the spline that I need.
[6:07] So the rig is pretty much done at this point.


### Creating Proxies & Configuring Ragdoll Layers [6:09]
**Transcript (timestamped):**
[6:10] But now we're moving on to arguably the most important part of this process.
[6:15] And this is actually creating the rag doll.
[6:17] So a lot of what you saw in the final animation depends on the rag doll and like getting it
[6:24] right.
[6:25] So it's important to do this correctly.
[6:29] So the goal is to get this, right?
[6:30] Which is the final rag doll model.
[6:34] So it's just a simplified representation of your high resolution geometry.
[6:38] So it's just, it's like a proxy and it just serves as a nice proxy so that the rag doll
[6:43] sim can just run nice and smooth.
[6:47] The problem is that the model is made up of lots of different pieces and rag doll typically
[6:53] doesn't like this.
[6:54] Oh my gosh.
[6:55] Someone's calling me.
[6:56] I hate these watches.
[6:58] Oh, by the way, I don't know why I'm wearing this.
[7:02] But yeah, so rag doll doesn't like this, right?
[7:05] It doesn't like all these crazy pieces.
[7:07] So what you need to do is you got to get rid of everything.
[7:11] So step one, get rid of everything you don't need.
[7:15] Now the rag doll, well, you're going to see that like typically when you make your rag
[7:21] doll, there's a node that constructs your rag doll model automatically, but you can actually
[7:26] give it any kind of geometry you want.
[7:28] You don't have to rely on that node to make the geometry for you.
[7:31] You can make your own geometry.
[7:32] So what I'm doing is I just need that centerpiece, right?
[7:35] In case the doll, you know, bumps up against the edge as it's coming up.
[7:39] So I'm just removing everything I don't need.
[7:42] And then for the doll, it's kind of the same thing.
[7:44] I just switched the doll to something much simpler.
[7:47] You know, I'm getting rid of little bells, little neck frill, all the little thread buttons,
[7:52] all that stuff.
[7:55] So once I have that simplified model, I just dropped down in apex, a pex, configure rag
[8:00] doll recipe, which just has everything all set up and preconfigured, right?
[8:06] So all you have to do is just kind of run through the recipe bit by bit.
[8:10] And yeah, you can get your rag doll.
[8:12] So here's the simplified model, right?
[8:15] And all of its glory.
[8:18] So then within that recipe, I just went through and just took that custom rag doll and just
[8:22] switched it.
[8:23] Boom.
[8:24] So I'm just modifying the recipe.
[8:27] So no problem.
[8:28] The recipes are there for that.
[8:30] You guys can always go through and modify them.
[8:33] So here's the fun part.
[8:35] I go through and just start animating my model.
[8:38] So what I like to do with this is I like to put each limb section on its own layer, right?
[8:45] So I'm putting arms, spine, dress hat, everything on its own layer.
[8:51] And this is a nice way to work because if you start running your rag doll and you're
[8:56] finding that it's too floppy, it's too loose, you don't really need to change your animation.
[8:59] All you need to do is just drop the weight of the layer and that'll stiffen up your rag
[9:05] doll.
[9:06] So it's just a nice organized way to work.
[9:08] And now I'm just running through the recipe.
[9:10] And the recipe just does everything else, right?
[9:12] Configures joint limits, turns everything into a motion clip, and boom, I got my rag
[9:16] doll.
[9:18] So the rag doll is looking for the joints and it's looking for the geometry, right?
[9:23] So all the joints are configured.
[9:25] The have that simplified geometry coming in and then it automatically creates the rag
[9:32] doll geometry for you.


### Driving Rest Poses with Set Driven Keys (SDK) [9:35]
**Transcript (timestamped):**
[9:35] So when the rag doll is finished, I need to start thinking about how I'm going to animate
[9:39] this.
[9:40] And the bulk of the work is going to be done using set-driven keys, or at least that really
[9:46] simple animation part.
[9:49] So again, we can start with a recipe.
[9:52] So the way the SDK component works is through layers with an Apex rig pose node, right?
[9:59] They work together in tandem.
[10:02] So the way this works is just, you know, like you're animating, you select the control,
[10:06] put it into a new layer and you just start animating away.
[10:10] And in this case, I'm just doing a really, really simple box opening animation.
[10:14] So nothing too crazy.
[10:16] And the animations can be as crazy as you want.
[10:18] I don't know if you saw Esther's talk yesterday, but they can be really wild.
[10:23] So in this case, all I'm doing is I'm using the SDK component to give myself sort of like
[10:29] a rest pose, right?
[10:31] So I can stuff the doll inside of the box because I don't want to have to do this every
[10:35] time I want to stuff the doll inside of the box.
[10:39] I just have this one SDK that I can just slide back and forth and just close it up.
[10:45] So now I can jump into the auto-rig component, right?
[10:47] Where I'm actually using that SDK component.
[10:49] And then I just look for those animation layers and it automatically creates a slider per
[10:55] layer, right?
[10:56] So now you can see here, I have two sliders and I can open it up.
[11:00] I can close the doll.


### Mapping the Rig to a Mechanical Crank Control [11:02]
**Transcript (timestamped):**
[11:02] What's great here is that you're not limited to just sliders.
[11:05] You can actually use controls in your rig to fire off these set-driven keys, right?
[11:11] So here I'm grabbing the crank.
[11:13] I'm looking for the rotation X value.
[11:15] So here you can see it's going way too fast because it's going from zero to one, right?
[11:20] So what I'm doing is I'm cranking it a bunch.
[11:22] I'm going to grab that value, right?
[11:25] That rotation value.
[11:26] I'm going to put that into my minimum, rotate a little bit more and then grab that again
[11:31] and then put that into my maximum, right?
[11:34] So once it gets to that point, it starts the animation and then as it goes down, it finishes
[11:40] it, right?
[11:41] So I rotated it a whole bunch of times and then it opens just like a real crank, right?


### Setting Up the Base Keyframe Animation [11:48]
**Transcript (timestamped):**
[11:48] So now we have everything we need to complete the actual animation.
[11:55] So to start, I'm going to stuff the doll inside of the box, right?
[12:00] As I was saying before, I open the box.
[12:03] I don't know why, but I just did that.
[12:06] And so yeah, with the SDK, I close it up and then I grab the spline control, drop it down,
[12:11] put it inside of the box.
[12:13] So now it's a very simple animation.
[12:15] It's literally just one keyframe, just keep framing out the bottom and then move it up.
[12:20] And then the next keyframe I'm going to be using is the actual SDK, right?
[12:24] That slider.
[12:25] So now the doll opens up and you can see it's kind of like intersecting with the box a little
[12:28] bit so I can go and just kind of drag it back a little bit and then it comes up and
[12:33] boom.
[12:34] That's my base animation and that's what's going to be used to drive everything else
[12:37] afterwards.


### Layering Ragdoll Physics & Secondary Spring Motion [12:39]
**Transcript (timestamped):**
[12:39] So now I can actually go in and start using one of the new features, which is the secondary
[12:46] motion.
[12:47] And here there's a couple of different types of secondary motion, right?
[12:50] And in this case, I'm going to use the spring secondary motion.
[12:53] And once I put it on, I notice that it's way too strong.
[12:55] So I could just go in and turn up dampening to about four, I think it was.
[13:00] And I get a result that I like.
[13:03] So now I'm going to grab that control and bake everything to a new layer, right?
[13:07] So I've select my frame range, grab the control, bake it, and then it's going to go into a
[13:12] new layer, right?
[13:13] Bake the keys, boom.
[13:15] So now I have that new layer.
[13:18] And now I can use that to drive everything else, right?
[13:22] Which is going to be the rag doll.
[13:27] Now this is the trickiest part of this whole process, right?
[13:32] Because you're in a way, how do I even put this?
[13:38] You're playing with like physics simulations, you know what I mean?
[13:43] So you're running that RBDS sim, but you're trying to kind of have artistic control over
[13:47] it.
[13:48] And what's great about this is that, you know, you can bake, you have your layer, you bake,
[13:52] you have your layer, you set keyframes.
[13:54] So not only are you working with these physics simulations, but you have a ton of control
[13:59] of how strong they are when they show up.
[14:02] So let's go ahead and look at how to do this, or rather how I did this.
[14:08] So I only want to use the rag doll for a split second.
[14:12] So I have to turn it on at just the right time, right?
[14:14] So here I'm looking for that frame where I want to turn it on.
[14:19] So I find that frame and I select the actual, just the rag doll controls that I want to
[14:23] initialize and I just set those keyframes, right?
[14:27] So boom, rag doll turns on.
[14:31] So as I mentioned, I only want to use a small portion of this, right?
[14:35] So I'm going to go ahead and take that animation and just bake it to a new layer.
[14:41] And then once I have that on my control rig, see now it's on my control rig.
[14:46] And that's all just, you know, that's why I never had to do anything with the doll.
[14:49] It's all just FK, right?
[14:51] So now that I have that on an animation layer, I can start playing with the actual weight
[15:00] of that animation layer.
[15:03] So again, this is just a lot of finesse, right?
[15:06] Like I'm kind of playing with that rag doll sim that I made.
[15:11] And I'm sort of looking for that position.
[15:14] Like I really want her arms to kind of be flying up in the air.
[15:17] So I'm kind of going back and forth and I'm trying to get that pose from the rag doll,
[15:21] right?
[15:22] And then I'm going to snap it back to that rest pose.
[15:25] And then when I snap it back, that's when I'm going to start adding more dynamic emotion
[15:30] on top of that, which is secondary motion again.
[15:33] So I select all of the controls and you can see the effect is way too strong, right?
[15:39] I mean, this is the spring effect, right?
[15:43] So but of course, you know, we got all these tools to control this.
[15:46] So I just drop the blend value down to zero.
[15:50] And then I can just key frame it back up as much as I want.
[15:54] Right?
[15:55] And I'm leaving this pretty strong on purpose because again, at every step of the process,
[16:00] you have control over this, right?
[16:01] So I go ahead, I'm going to select and see, you know, I can turn things off.
[16:05] I can turn off in the neck.
[16:06] At one point I turn off in the spine, right?
[16:08] So again, you're working with dynamic motion.
[16:11] You're working with sort of physics simulations, but you have a lot of control over the final
[16:16] product.
[16:17] You never locked into anything really.
[16:20] So I'm going to go ahead and bake everything, right?
[16:22] And but the thing is, is that like the final result is still very strong.
[16:27] So yeah, you can see it's way over the top, but that's kind of on purpose, right?
[16:32] Because I want to have something I can then play with later.
[16:35] So I put all that into another layer and then the same thing that I did with the rag doll,
[16:41] I just go back in and I start messing with the layer weights.
[16:45] You see?
[16:46] So again, a lot of finesse here, looking for the point where rag doll finishes and then
[16:51] I want to initialize that secondary motion, right?
[16:54] So kind of interesting.
[16:57] It's your, your, your, uh, layering these different effects, right?
[17:02] Procedural motion.
[17:03] You're layering these different procedural motions and each animation is being dynamically
[17:08] driven by the previous animation, right?
[17:11] But since everything is baked onto layers, you, like I said about a million times is
[17:16] you have full artistic control over the final result.
[17:20] So you're never, like I said, you're never locked into anything.
[17:22] You can always turn things on and off, do it again.
[17:25] It's pretty, it's pretty forgiving.


### Blending Animation Clips in the Motion Mixer [17:28]
**Transcript (timestamped):**
[17:28] But of course we're missing that cranking animation from the beginning, right?
[17:35] Because yeah, what's a jack in the box without the, you know, anticipation.
[17:39] So to get that cranking animation, what I'm going to do is, uh, within my scene animate,
[17:44] I can go ahead and just create a new clip, which is a really, really nice function.
[17:48] So now we can have multiple clips on a single scene, animate node.
[17:51] So I go ahead and create the new clip and then let's see, I drag that back in.
[17:58] And then all I really need to do to get this motion, since I create that set driven key
[18:02] before is just set a couple of keyframes and just rotate the crank a bunch of times as you
[18:08] would in real life, which is kind of cool.
[18:11] So I just set that keyframe.
[18:13] I look for the, uh, you know, right position.
[18:15] I rotate it back a little bit.
[18:17] So it's a little bit faster.
[18:19] And then I let it play out and then I have this beautiful cranking animation.
[18:25] So once I have that, I can put everything into a motion mixer.
[18:32] And then once I'm in the motion mixer, you could see up top there that I have access
[18:35] to all the animations that exist in my scene, animate, right?
[18:40] So this is pretty simple compared to what Sasha had.
[18:42] I only have like two animations in there, uh, but this is all I needed.
[18:46] So I just dropped those in.
[18:48] And again, it's this kind of finesse thing, right?
[18:51] Where it's up to you to kind of find the right timing and to kind of blend these two animations
[18:58] together.
[19:00] And then, uh, yeah, yeah, I think I was pretty happy with that.
[19:04] So again, here's the final animations, the final animation with all those elements in
[19:11] place, right?
[19:12] So ragdoll secondary motion and set driven keys.
[19:23] All right, cool.
[19:30] That's my talk guys.


### Q&A: Apex Scripting & Token-Light MCP Servers [19:31]
**Transcript (timestamped):**
[19:40] Any questions?
[19:41] Thank you.
[19:42] Great presentation.
[19:43] Thanks.
[19:44] Um, from yesterday's keynote, I remember, um, uh, during the, uh, apex, uh, demonstration,
[19:50] there's mention of, uh, mcp and, uh, and I don't know that's the right term, but, um,
[19:58] improved mcp dictionary for more efficient token use and, and LLM.
[20:04] I'm just wondering, um, if, uh, uh, I, I don't, I know this is not related to the talk,
[20:11] but I'm just wondering if this is, uh, specific to apex or, uh, and who indeedy in general.
[20:18] Well, the, well, the, the, the mcp server that you saw yesterday, that, that is specific
[20:22] to apex.
[20:23] Yeah.
[20:24] And so it's specific, it's specific to apex ringing.
[20:26] So, uh, yeah, it's kind of like in, in short, the idea would be that you can vibe code or
[20:32] rig.
[20:33] That's kind of, you know, so it's, it's kind of like, you know, creating a rig with plain
[20:39] English really, you know, make this, make that, um, but not just a rig, but also, uh,
[20:44] components as well.
[20:45] Cause again, you know, apex is all purpose execution.
[20:48] So it's a lot of it has to do with rigging.
[20:51] Like, you know, the way that we're teaching it is based in rigging, but, um, apex can't
[20:57] be extended into other things, you know, like like a bridge tool or something or a building
[21:02] generator, right?
[21:03] So, uh, yeah, we, we, we, we taught this model or this agent, you know, apex, so it knows
[21:09] it really well, it knows the proper syntax.
[21:11] Um, but yes, yeah, it's, it's mainly based in, in apex.
[21:16] I see.
[21:17] Thank you very much.
[21:18] Yep.
[21:19] I think Esther wanted to say something.
[21:21] Oh, did I get it wrong?
[21:24] Yes.
[21:26] No, just, just a few specific actions.
[21:28] So the MCP is specifically for apex script and it is purely operating also in code.
[21:35] So it's in, it's understands apex script syntax.
[21:38] It understands various examples.
[21:40] Of course we have a lot of examples in the rigging realm, but it would work for any other
[21:44] setup that he would want to build with apex, but the overall framework is because of that
[21:49] also fairly token light.
[21:51] So we made, we have like several iterations to make sure that it actually is fairly robust
[21:56] and token light.
[21:58] And I recently even made a few tests where you actually even try it with like cheaper
[22:01] models, and you still get a fairly robust result out of it with the, uh, because of
[22:07] the harness that we have in place for it.
[22:09] Yeah.
[22:10] If that helps, but yeah, but the communication to Houdini works simply by, by, uh, having
[22:15] like an attribute watcher that kind of communicates the code back to Houdini.
[22:20] That is actually what's happening under the hood, but the rest is fairly lightweight.
[22:32] The reason that I was asking whether it's apex specific is I've been using MCP server
[22:38] and I rich like that, that the token uses, uh, is not sustainable and is, is cost way
[22:45] too much.
[22:46] And you mentioned that it was going to be a more token efficient yesterday.
[22:51] And that's why I was wondering whether it is just, uh, it's just applying to apex or,
[22:59] or everything else in Houdini.
[23:01] Like I don't know, like, uh, HDA or VEX and so there's no, okay.
[23:07] Don't take the fun search.
[23:33] Yes.
[23:34] A super quick one.
[23:36] I was just wondering, would this work with live link
[23:39] in other applications, like Unreal or anything?
[23:43] No, we don't have that set up yet.
[23:47] Yeah, but that is a good idea.
[23:49] I was actually just talking with Esther again
[23:51] about doing something like that.
[23:53] But no, that's not set up yet.
[23:56] Somebody else had a question, I think, or no?
[23:59] OK, I have two plushies to give away.
[24:04] Who is the first who can say, why is this an SDK?
[24:16] In the context of the presentation.
[24:18] Oh, wrong.
[24:23] I think you were next.
[24:25] Yeah, I was going to give you one.
[24:28] OK, and what did Max use to get the spraying effect
[24:33] on the doll?
[24:36] Thank you, or first?
[24:41] Yeah, nice.
[24:43] So come on down and I think that's it.
[24:49] Come on down at the end and collect your plushie.
[24:54] Are there any more questions, actually?
[24:58] OK, then that's a wrap.
[24:59] Thank you, Max.
[25:00] Oh, thanks, guys.



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
