---
title: Abstract liquid in Houdini | Part 02 - Look Development
source: YouTube
url: https://www.youtube.com/watch?v=axBNpCzJuPY
author: Kotov Roman
ingested: 2026-07-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/abstract-liquid-in-houdini-part-02---look-development/
frame_count: 0
frame_status: pending-selection
---

# Abstract liquid in Houdini | Part 02 - Look Development

**Source:** [YouTube](https://www.youtube.com/watch?v=axBNpCzJuPY)
**Author:** Kotov Roman
**Duration:** 28m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py abstract-liquid-in-houdini-part-02---look-development <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello! Today we will be looking at the second part of the three-part tutorial series.
[0:05] In the first part we dialed in the simulation. Now it's time to do some look development.
[0:10] If you haven't seen the first part, the link is in the video description. And let's get to it.
[0:16] Let's split our viewport into two. To do that, you hover over the viewport and press Ctrl 2.
[0:22] I will be using top one for camera view and the bottom one for scene adjustments.
[0:28] Now we can start building the scene. First we need redshift material. Let's call it points.
[0:37] Assign it to our geometry container and dive inside. There we can use attribute density for
[0:44] coloring our points. So let's get it in. Drop down Particle Attribute lookup and type in density
[0:51] and attribute name field. If we connect it to the surface, we should be able to see it directly
[0:56] in our viewport, but we don't. Not because I still have setup geometry container enabled.
[1:03] And points render doesn't have material assigned.
[1:10] Now we can see that it works. Let's jump back in.
[1:14] Add a ramp and connect it to our particle attribute lookup.
[1:19] I would like to change white color to red.
[1:22] And maybe squish black a bit.
[1:28] Now we can connect it to the base color.
[1:33] I can see that particles are way too big. Let's get back to the setup.
[1:38] Let's dial back the pscale value to 0.005 and see how that works.
[1:47] And even smaller to 0.003.
[1:51] I'd like to decrease minimum value as well to 0.0012.
[2:03] That's about the size that I would want them to be. If we have to, we will change it later.
[2:09] That's probably too many particles, but we will see if that's gonna be a problem.
[2:13] Let's adjust pscale value a bit more and maybe change camera angle as well.
[2:18] Let's increase amplitude on our vertical noise.
[2:25] And I would probably like to disable edge-to-air eye from our camera view.
[2:31] Now it's time to set up a camera angle. And I will see you once I find something that I like.
[2:48] And I think this angle will work just fine.
[2:51] Let's maybe start by setting up the lights for this camera.
[2:54] Let's disable edge-to-air eye and get a rest light into the scene.
[2:58] That's what we're gonna use the bottom viewport for.
[3:01] I would like to set it on the opposite side from the camera.
[3:04] Maybe make it taller, adjust position a bit and exposure.
[3:08] This light is supposed to catch some of the highlights and give us the nice base to start with.
[3:12] Maybe let's try it from the other side.
[3:15] And it's not working so good. I'm also looking to get nice shadows from that light.
[3:22] Maybe let's drop down the spread. And that is already working better.
[3:27] But there is a problem. As you can see, light shines through the particles at the bottom.
[3:32] You can see it better if we enable alpha channel. It is supposed to be fully white.
[3:38] To fix that, I will add a grid to our scene.
[3:40] And then,
[3:44] name it black.
[3:47] We go inside and drop it down a bit so it doesn't intersect with our particles.
[3:55] Now let's create a material for it.
[3:59] Let's call it black and assign it to our grid.
[4:02] We don't need base or reflections for that, so let's drop down their weights to zero.
[4:06] If we refresh a viewport, we can see that alpha is fully white,
[4:10] and light doesn't shine through particles anymore.
[4:15] Let's rename a grid to black underscore render.
[4:21] We can do one more thing. I would like to get transform node, move it down just a bit,
[4:28] and merge point, warp and transform.
[4:32] In that way, bottom particles will maybe catch some reflections.
[4:36] So we have our base light. Let's maybe try and set up second camera.
[4:40] Indeplicate our existing camera and the render robbed.
[4:44] Make sure that the new render robbed renders from a new camera.
[4:48] And let's see if we can find a new angle for the second camera.
[4:51] Something closer to the particles.
[4:57] It's good for now, so let's not shine that and view our first camera.
[5:01] If we look at them side by side, I like the shape that second camera gives,
[5:04] but I like the depth of the first camera better, so I will stick with it.
[5:09] Let's adjust lights a bit more.
[5:13] Let's make our fill light a bit colder.
[5:17] Something like that. Let's duplicate that light and maybe move it closer to the camera.
[5:25] Maybe increase the spread so it's not as harsh.
[5:27] Decrease exposure and make a snapshot for before and after comparison.
[5:32] As you can see, it gives just a bit of light into those deep shadows.
[5:35] It's as good time as any to make some adjustments to our material.
[5:38] Now let's increase IOR to make it a bit shinier.
[5:45] Let's see how much of the roughness do we need.
[5:48] Something around 0.25.
[5:51] So let's add another light. It's going to be really thin and will not have as much spread.
[5:57] It's going to be warmer and going to be on the opposite side from our camera.
[6:02] Let's make a snapshot for before and after and disable other lights for now.
[6:10] Maybe make it a bit smaller and decrease spread even more.
[6:18] That's going to work for now.
[6:22] Let's bring back our lights and adjust intensity for each.
[6:27] And maybe make it a bit warmer.
[6:31] I don't really like that we don't have a nice falloff to that light so let's copy it.
[6:36] And by the way, so we don't have to constantly turn off and on those lights,
[6:40] we can use isolate select instead.
[6:43] Now that we have that copy, let's increase the spread and decrease exposure.
[6:51] And then just gives those not so harsh nicer falloff for that light.
[6:55] We can bring back all of our lights now and balance their exposure.
[7:00] Let's make our fill light really cold.
[7:04] Maybe not so much.
[7:05] Something around that.
[7:08] I'm still thinking particles might be too small.
[7:10] Let's add some bigger particles into the mix.
[7:13] Luckily, ramps can go above one so let's use that.
[7:17] We will make a fourth point and make it three.
[7:20] Now the maximum p-scale value will be three times bigger than the maximum p-scale value.
[7:24] And the one we set.
[7:30] Now we have bigger variety of the particles.
[7:34] I like that material but it's not quite what I'm looking for.
[7:37] We can use a rest material instead.
[7:39] Let's make all the same adjustments that we had in our standard material.
[7:43] If we replace our standard material with a rest material,
[7:46] we can see that it's pretty much the same.
[7:48] The nice thing about the rest material is that it has back wide translucency.
[7:52] So if we connect our colors to it and adjust the weight,
[7:55] we would get fake subsurface scattering.
[7:57] It's not as good as the real SSS but it's gonna render much faster.
[8:01] In conjunction with subsurface scattering,
[8:03] it's a good idea to adjust exposure of our lights.
[8:08] I'm still not quite sure what colors scheme I'm going for,
[8:11] so let's play with the color ramp.
[8:14] If we add just a bit of color into the black,
[8:16] we will have subsurface scattering there as well.
[8:18] That's a bit too much but that should work.
[8:26] That's small tweaks but that would make scenes much more interesting.
[8:31] And again, that's not real subsurface scattering but that should render a lot faster.
[8:38] What I like to do when I render particles is to adjust their roughness based on the Fresnel.
[8:42] Let's also add ramp node and connect all of that to reflection roughness.
[8:48] Let's clamp black a bit and I forgot to make a snapshot.
[8:56] I would prefer particles to be more reflected from the sides,
[8:59] so I will invert Fresnel.
[9:02] The nice thing about that Fresnel is it's gonna tim down all of that visual noise
[9:07] from particles reflecting off one another but still maintaining reflections on the edges.
[9:13] Now that we've changed the material, we should adjust the lighting.
[9:15] So let's turn off fill lights and leave only main lights on and adjust their exposure.
[9:26] We also have a dumb light in our scene.
[9:28] Let's see if that's gonna be a better fill light than the ones we have right now.
[9:38] I like those reflections, so let's maybe disable diffuse and leave reflections on them.
[9:45] And we should color it blue as well.
[9:50] And let's bring back our lights one by one and see if that's working.
[9:57] Let's make a snapshot of before and see what I like best.
[10:03] I think dumb light works better in that specific case.
[10:06] That means that I don't need our old reflection sprite anymore.
[10:11] Let's color it gray so I don't turn it on accidentally.
[10:15] Building a scene is a lot of back and forth, so let's get back to the material and adjust back
[10:19] lighting. Let's also change the color that goes into the back lighting.
[10:24] Up here ramp and adjust dark values to be brighter so we get more translucency there.
[10:30] And as always, let's make a snapshot of what was before
[10:35] and compare it to what we have.
[10:39] That might be a bit too bright.
[10:40] And let's maybe change the red as well.
[10:54] And let's see if we need to adjust the color of our main light.
[10:59] Okay, that works for now, but we don't need that camera.
[11:04] And let's add post effects to the one we need.
[11:07] I would like to enable Tom mapping, set highlights to zero,
[11:14] and adjust exposure, but it's easier to do in the camera itself.
[11:23] I also would like to add a lot, and those are default redshift ones.
[11:29] My go to is quarter 800. In most cases, I enable apply color management before a lot.
[11:36] And let's see how much of that lot we need.
[11:43] And that's already closer to what I had in mind.
[11:46] Let's maybe try to saturate highlights. I think I will leave it on.
[11:55] And increase exposure just a bit.
[11:59] I think red is a bit cold, so let's shift it to the warmer tones.
[12:07] And desaturate our main light a bit.
[12:14] Now is a good time to add the filter scene, so let's enable bokeh,
[12:18] switch to bladed, set spherical duration to two, and blades to six.
[12:23] Let's shift the focus to the center of our scene.
[12:29] The font looks good as well. I think I will animate focus plane a bit later.
[12:34] But for now, let's focus somewhere in the middle.
[12:36] We can adjust the size of our bokeh using f-stops. I think around five should be good for now.
[12:45] Let's think about our second camera, but if we're doing that, let's rename our lights.
[12:49] Cam 01 light 01 and copy that to the rest of them.
[12:54] That will come in handy later when we set up render rows.
[13:01] I have a rough idea of how I want my second camera to look like, so let's jump into the setup.
[13:11] Now I need to get one of the points isolated, preferably one with a lot of movement,
[13:16] but it shouldn't go too close to the edges.
[13:23] Let's see if we can find one.
[13:27] Think this one might work, so let's isolate it using blast and check in on delete non-selected.
[13:35] After that, I would like to freeze it on the last frame using timeshift, so frame 300.
[13:41] And before the timeshift, let's add trail.
[13:45] Set trail length to 300 as well.
[13:49] As you can see, something is not right, that's because I was using PTNAM attribute instead of ID or point isolation.
[13:58] So let's isolate the same point using ID attribute instead.
[14:03] Set selection by attribute.
[14:05] Now we can click delete and that should work.
[14:11] Let's wait a bit while it calculates.
[14:14] After that, we get this path, but it's too short for what I would like to get.
[14:19] Let's maybe choose another point instead.
[14:22] This point gives us a nice line to work with, so let's proceed with this one.
[14:34] We need to drop down add node and connect those points using ID attribute.
[14:39] Now instead of the points, we get one curve.
[14:42] We can drop down null and call it out under score path.
[14:50] Now we need another geo container.
[14:52] Drop object merge and add null in there.
[14:57] Now we can add null in there.
[15:00] Now we need another geo container.
[15:02] Drop object merge and add null in there.
[15:07] Call it camera underscore path, because I will not be rendering this geo container,
[15:12] I will leave it gray and turn off visibility flag.
[15:17] Let's duplicate our camera and jump inside.
[15:21] In there, we will need constraint network and inside of it, we will need follow path node.
[15:27] If we wire it up and choose our camera path container, we will see that camera moves along that path.
[15:36] Let's look at view so it doesn't change when we drop into the camera.
[15:39] When we move position slider, we can see that camera moves.
[15:43] There is clearly something wrong here and I will spend several minutes trying to figure this one out,
[15:48] but as it turns out, I just forgot to reset transform and rotation of my camera.
[15:53] Once I do that, everything works.
[15:56] So as I said, we should leave all of that on default, so we'll get node none.
[16:04] Camera is still not straight, but I have to clear out the transforms.
[16:11] Now it's working as it's supposed to.
[16:18] If we jump into the camera and into the constraint network, we can move position slider.
[16:25] And see that camera moves along the path.
[16:30] Now we can animate the camera.
[16:34] We go to the first frame and set it to zero, then go to the last frame and set it to one.
[16:39] With this setup, you can sometimes see the quirky behavior when the position is set to one,
[16:44] so I will offset that slightly.
[16:45] Now all is left to do is rotate the camera downwards, so minus 90 degrees in X rotation.
[16:51] I will probably do some more adjustments to the camera, so the movement feels more natural.
[16:56] Let's start by animating the Y rotation axis.
[17:00] Let's set it to minus 6 on the first frame and open up animation editor,
[17:05] so it's easier to see what's happening.
[17:09] I want to make camera animation follow the movement, so it feels more fluid.
[17:15] Now that I have the rough idea of how I want that animation to go,
[17:19] I will select all of the keyframes and convert them to Bezier,
[17:22] and work only with the start and the end ones.
[17:31] I'm quite happy with this camera animation, so I think I will leave it to that.
[17:36] Now I want to get the light going.
[17:38] So let's choose camera 0,2 in the render IPR and start rendering.
[17:44] We should enable one of the lights, and probably disable bokeh,
[17:48] so it's easier to see what's going on.
[17:50] New camera already has all the positive facts inherited from the camera one,
[17:55] but we probably will have to animate the lights so they follow the frame.
[18:02] As you remember, this light is supposed to give us nice, deep shadows.
[18:07] Let's shrink it in the Y axis,
[18:09] and maybe move it a bit.
[18:11] Make it wider so it covers all of the particles as the camera moves,
[18:17] and move it down as well.
[18:20] Let's check that it works across all of our animation.
[18:24] Main lights will be a bit trickier, because they are quite thin.
[18:27] To make it easier, we can connect one to another,
[18:30] and reset, transform, and rotate on the child plate.
[18:33] Now let's move the camera to the camera, and move it down as well.
[18:37] We can also adjust the light saturation on the child plate.
[18:40] Now we have only to work with the parent light.
[18:43] Let's get that light in frame.
[18:45] I remember on the camera one, light was shining from the top left corner,
[18:49] so I want to start there.
[18:51] That may be from the right, it'll work better.
[18:54] We can also tilt it back a bit, so we get more shadows.
[18:57] Let's set up a second light so we don't get so harsh falloff on the light streak.
[19:07] First I would like to decrease the spread so it doesn't cover the full frame.
[19:11] And maybe make it thinner.
[19:13] Now let's bring back the main light and then adjust the resize together.
[19:22] Now let's set up the light that was responsible for the specular highlights and find a nice
[19:26] angle.
[19:28] I will make it brighter so it's easier to see.
[19:32] I'm looking to get this light to shine from the same direction as our main light source
[19:36] does.
[19:40] Now we can turn the exposure back down and look at our scene with all the light sources
[19:44] on.
[19:48] Now I would like to see exactly what the specular light source does.
[19:53] Let's check what our first camera looked like to see if we are off.
[19:58] And I can see that our main light needs to be a bit warmer.
[20:02] Now that we have that we can animate our main light so it follows the camera.
[20:06] We can jump to the first frame and set the keyframe there.
[20:12] Then go to the last frame and rotate our light so it isn't framed.
[20:22] I will set the keyframe on the last frame as well.
[20:25] If you shift click on any parameter it will open up animation editor.
[20:31] I can see that x and z value don't really change throughout animation so I don't really
[20:35] need them.
[20:37] Let's go to the sequence and see if the light is in the frame and make some adjustments
[20:41] if it's not.
[20:44] We don't need a lot of keyframes because they are just a rough estimation as to where the
[20:47] light source will be moving and I will delete them later.
[20:54] Now we can convert all of those keyframes into BZ here and delete the ones in the middle.
[21:00] Because as I said I like to work with the first and the last keyframes.
[21:05] Now we can scrub through the animation and check that the light is still in the frame.
[21:14] After that we can set up camera pass processing.
[21:17] First I will enable depth of field and set up focal plane to be our main particle.
[21:26] We can increase depth of field by lowering f-stop value.
[21:29] I know that value of 1 or even lower is not physically accurate but that's fine.
[21:38] I can see that random value is a bit off and maybe contrast as well.
[21:45] In the first camera we had really deep blacks so let's try and simulate that here as well
[21:50] and maybe enable desaturate highlights while we are here.
[21:55] Now that I am looking at both of them I can see that red on the second camera is not as
[21:58] cold as the red on the first camera.
[22:01] Let's maybe change the white balance to fix that.
[22:07] I am also seeing that the first camera had more pronounced highlights so let's maybe
[22:11] increase highlights on the second camera.
[22:13] There is still not identical but that's mostly due to the camera angle.
[22:20] I will try to bring them as close as I possibly can but I think most of that will be fixed
[22:24] in post.
[22:29] Another big fan of those dark spots I will try and see if I can shine some light in there.
[22:35] Let's make a snapshot and see what we can do.
[22:39] First let's change the HD-Rain map.
[22:41] This one might work better.
[22:44] Let's bring back all of our lights.
[22:48] That brings light into those dark spots but maybe I didn't point it that strong.
[22:52] I am also seeing that the tint of those reflections is a bit off.
[22:55] This works a bit better but I am still not quite happy with the results.
[22:59] So let's see if we can find a better HD-Rain.
[23:02] I will use mouse scroll wheel to scroll through HD-Raisers and have it at the folder.
[23:07] And I do reset transform some of that HD-Raisers as well.
[23:18] I can see that highlights are a bit desaturated so let's fix that.
[23:28] I will go and make some small adjustments to the light so they better match with the
[23:32] first camera.
[23:38] Now that I am done with that we can rename lights to camera02 light01 and copy and paste
[23:45] that name to all the camera2 lights.
[23:50] Now we are ready to set up render route but before we do that let's stop IPR rendering
[23:54] and disable all the lights because we will force them to each route.
[24:00] Let's change frame range to render frame range and check that render path is correct.
[24:07] Now we can go to the object tab on the route.
[24:12] We can drag and drop drum trick containers we want to render in the force object field.
[24:16] Let's do that for both of our cameras.
[24:19] We can also delete asterisks for candidat objects.
[24:22] Now let's copy the name of our lights.
[24:24] Delete asterisks for candidat lights and paste the name of the lights to force lights field.
[24:29] Let's change the number to asterisks so it will render every light whose name starts
[24:34] with camera01 underscore light and we will do the same thing for second route as well.
[24:39] Now we can render routes and each of them will bring their own lights.
[24:44] As you can see lights are enabled even though they are disabled in the scene.
[24:49] Now that I am looking through the scene I am noticing that I am lacking vertical noise
[24:53] animation.
[24:56] I will go back into the setup.
[25:00] And if you remember mountain sub that was responsible for the vertical noise I will
[25:04] tick on animation and increase pulse duration.
[25:08] And doesn't play in real time but we can drop down time shift and freeze the first frame
[25:13] so we can see that change is easier.
[25:22] And that looks about right.
[25:24] Don't forget to disable time shift.
[25:26] Now if we go ahead and render camera01 we can see that noise pattern changes.
[25:30] Maybe I don't want that much roughness in the noise.
[25:35] And I would like to decrease element size.
[25:37] It doesn't seem like I have enough amplitude on the noise so let's increase that.
[25:53] Now we can animate depth of field on our camera.
[25:56] So let's go to the first frame, setup focal plane on the front particles and keyframe
[26:01] focus distance.
[26:03] Now we can go to the last frame and I would like focus to be in the middle.
[26:07] I will also setup keyframe there.
[26:10] Now I will go through animation and see where I like focus best.
[26:16] After that is done I can open up animation editor, convert all the keyframes into busy
[26:20] air.
[26:24] And delete the ones in the middle.
[26:33] Now I can scrub through animation and check that the focus is where I want it to be.
[26:40] And make some adjustments if it's not.
[26:47] I'm thinking depth of field might be a bit stronger so let's drop down fstops.
[26:56] I think I'm done with the first camera.
[26:59] Let's check the second one.
[27:07] I can see that depth of field is a bit too strong so let's increase fstops and maybe
[27:12] decrease highlights as well.
[27:14] But increase exposure.
[27:18] Maybe decrease flat intensity while we are here.
[27:26] Maybe I will zoom in a bit as well.
[27:37] I'm not a big fan of that zoom so let's bring it back.
[27:42] I think I'm ready to call it good and send those two cameras to render fun.
[27:47] So I will see you in the third part where we will finish this piece with some light
[27:51] compositing and color grading in After Effects.



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
