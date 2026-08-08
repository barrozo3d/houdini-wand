---
title: Houdini for Beginners-  Part 5:  The Viewport
source: YouTube
url: https://www.youtube.com/watch?v=rgzRA8IXZuw
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-for-beginners--part-5-the-viewport/
frame_count: 0
frame_status: pending-selection
---

# Houdini for Beginners-  Part 5:  The Viewport

**Source:** [YouTube](https://www.youtube.com/watch?v=rgzRA8IXZuw)
**Author:** Jordan Allen
**Duration:** 15m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-for-beginners--part-5-the-viewport <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So let's talk a little bit about the viewport itself, right?
[0:03] This big beautiful box right here, the scene view.
[0:06] What we are looking at right now, we've just got a sphere in the scene, very basic.
[0:10] But the way that it's visibly displayed isn't really showing as much about the object, which,
[0:14] you know, is perfect for us in certain circumstances, but in other circumstances,
[0:18] it'd be nice to see a little more.
[0:20] And so what we have here in the top right of the scene view is basically a shading drop down, right?
[0:25] If you click on this, there's a lot of different options you have access to.
[0:29] Just basically different ways of displaying your geometry that could be helpful to you.
[0:33] So for example, we have smooth wire shaded, right?
[0:36] Right now we're on smooth shaded, which we can kind of see from the icon here.
[0:40] That's a matching icon right there, baby.
[0:42] That's like a, it's like a third grade homework problem.
[0:45] Do the icons match?
[0:46] Yes, they do.
[0:46] So we know this is smooth shaded.
[0:48] What is smooth wire shaded?
[0:49] Well, that is going to add the wire frame or polygonal view on top.
[0:55] So it's going to smooth shade your geometry.
[0:58] So that it doesn't look super rigid because if you look at this geometry itself,
[1:02] this is not a lot of polygonal data, right?
[1:05] This is not a very high depth sphere.
[1:07] So it should be really quite sharp in how it appears.
[1:11] But since we are in smooth shaded, what that is doing is applying essentially a false smoothing
[1:18] operation to make it look smoother than it actually is.
[1:20] You can kind of see that with the specular highlight right here.
[1:23] This is just a default specular highlight that exists in our scene.
[1:26] And you can see it's not running over any hard edges like it totally would if that's
[1:30] how this geometry was actually constructed.
[1:33] One thing smooth shaded doesn't fix though is this surrounding.
[1:37] You can kind of see here how sharp this geometry appears because the silhouette
[1:42] is not being fabricated in any way.
[1:44] It's merely the normals of the object and we'll get a normals and all that stuff at a later date.
[1:49] But point is you've got smooth shaded.
[1:51] This is kind of the default view or smooth wire shaded is typically how I like to work
[1:55] just to see what's going on.
[1:56] But there's other stuff too.
[1:57] There's flat shaded and this is all of a sudden where you see that smoothing operation stripped away.
[2:03] This is the raw ugly truth of your geometry.
[2:05] This is what it looks like right?
[2:06] You can see each polygon with that real sharp fall off.
[2:10] There's also flat line shaded with you know that wire overlay as well if you want to see that or
[2:16] one that you'll use a lot is this wire frame mode that basically strips everything but the
[2:20] polylines that comprise your geometry.
[2:22] You know there's no polygons blocking our view there.
[2:25] And there's also wire frame ghost which is very interesting where it is giving you that wire frame.
[2:30] You can kind of see through the polygons at about 50% opacity.
[2:35] So lots of different ways to operate.
[2:37] Typically you'll find yourself most likely operating between a smooth shaded view
[2:42] and a wire frame view and you know the the the peeps over at Houdini knew that was going to go down.
[2:47] So all you have to do is when you're in the scene view here just press W to activate that ghost
[2:53] wire frame mode and then W again in order to get back to that smooth shaded wire frame mode.
[2:58] But the same is true of any of these modes right?
[3:01] If I start in flat shaded without the wire frame and I hit W I enter that ghost wire frame mode.
[3:05] I hit W again.
[3:06] I go back to what I was previously on.
[3:08] So basically the W key is just a toggle to wire frame from whatever you are currently at.
[3:13] Now to the right of this there's this little icon that looks like a sphere
[3:16] surrounded by some ghost geometry right right here.
[3:19] This is going to be very very handy to you.
[3:22] You're going to use this all the time.
[3:24] Basically this is visibility through contexts and what that means is if I have another geometry here
[3:30] on the OBJ level let's say I have a box and I move it over here and we want to make changes
[3:36] to the internals of the sphere.
[3:37] So if we double click this now we'll notice the box on the upper level has turned into ghost mode.
[3:43] Basically it is being allowed to exist even when going into this level just for reference sake in
[3:50] case you want that.
[3:52] So for example if I click and hold on this I can choose hide other objects and now whenever I go
[3:57] inside an object I just want that object.
[4:00] I want everything else removed from my view so I can work on that independently
[4:05] but I can just change that and allow the ghost through or I can change it and let all the solid
[4:09] geometry through.
[4:10] So I'm still seeing the full scope of my scene even while working on the internals
[4:14] of a given geometry.
[4:15] Super handy.
[4:16] And the last thing over here is your actual view layout breakdown right in the viewport.
[4:21] For example let's say we are modeling and we want to see a perspective view but we also
[4:26] want to see a top view right a top orthographic view of our scene.
[4:31] If we come over here we can choose gosh four views two views stacked two views side by side
[4:36] lots of different combinations of views.
[4:38] Let's do two views side by side for example that will split our scene and look it gives me a top
[4:44] view and a perspective view but by clicking in any of these boxes and hitting space two
[4:49] space three space five space four we can change again that orthographic view we can also do two
[4:55] perspective views from different angles.
[4:58] You're totally free to do whatever you want you know if I want every view I want the front
[5:03] I want the top I want the side and then I have my perspective like that's a great setup
[5:09] but you can also very quickly toggle between these with control and the different numbers
[5:14] for example control one will give you one split right one main view in the scene view window
[5:20] control two you guessed it that's two three is three four is four there is no five I just
[5:25] tried it just out of curiosity it doesn't exist so this is a real quick way for you to you know
[5:31] jump between different setups that you might want for for various different operations
[5:37] inside of Houdini very very helpful so we've got those three things but in true Houdini fashion
[5:41] there are multiple ways to to do the same thing if you press the while in the scene view essentially
[5:47] think of it as like short for view you can change your view settings you can change the viewport
[5:54] layout right here by just dragging over and then selecting the one you want or you can change the
[5:59] shading modes right here as well there's also some selection options over here you know to what
[6:04] we were talking about earlier for example if you wanted to do box or lasso selection only
[6:07] selecting visible geometry like we looked at earlier and and other options there too so
[6:12] this radial menu is there if you want it I don't personally use it but again nice to know that
[6:16] it's there at least now continuing on the theme of the viewport right there is the right hand side
[6:22] of the scene view and this has a lot of very helpful little buttons that we can use and we'll
[6:27] we'll go ahead and explore that now I'm going to highlight and delete this box we've got our sphere
[6:30] back I'm going to go ahead and switch to smooth shaded mode in fact I'll go to smooth wire shaded
[6:36] mode I like this one more and let's go ahead and just do do this one a little different I'll just
[6:41] take a tour down the right hand side to the most important nodes so right at the very top we have
[6:46] a display reference grid right this is the world planes ground zero so to speak and we can see that
[6:53] here you know it's if we navigate over we can see some helpful information essentially our world
[6:59] scale in grid form Houdini works in meters so if you see negative one just know that is negative
[7:05] one meter in length from the center of the world I'm going to get rid of that sphere here but we
[7:09] can see the zero here negative one positive one and this is on the let me actually rotate it this
[7:14] way this is a little easier to see in fact I'll spacebar and go to the top view for a perfect
[7:19] view of this so at the center of our world we have zero zero zero right it is the zero of the
[7:27] x axis of the z axis and of the from the top view we can't see it but the y axis this one up and down
[7:35] if I go to the side view I'll go to the front view we can see yeah a zero in green as well that's the
[7:39] y axis so popping back to the top view here this is all in meters this is one meter positive one
[7:45] meter negative on the x and you can also see this helpful little handle at the bottom left of the
[7:50] scene view that is showing you in real time as you navigate around which direction is x y and z
[7:57] the the direction of the line itself is the positive x y and z so just know that if you are aiming
[8:03] the other way from that line direction that is the negative of x y and z now there are situations
[8:09] where you may want to get rid of this ground plane for example you know there are sometimes where
[8:14] we're working below the ground plane and I'm looking at my geometry and I'm navigating around I've
[8:18] got this floating thing here that's just kind of in my way by just clicking this we can remove it
[8:23] from the scene entirely and now you get this you know this eternal wonderland of gridless space
[8:29] it's pretty beautiful we can turn that back on very easily just toggling it and then you may notice
[8:34] that there's a little black arrow at the bottom right of this icon again indicating that if we
[8:38] click and hold there are other there are other parameters that we can activate for this visualizer
[8:44] here we have ruler on the main axes right this is where we're seeing just that center line have the
[8:49] negative and positive numbers but let's say we're working over here I don't want to count one two
[8:56] three one two I just want to know what this distance is so if I click and hold on this I can actually
[9:02] choose ruler on grid points and now I've actually got the negative values right there I know this
[9:07] is negative three on the x and negative three on the y so that's nice that you can toggle and you
[9:11] can also obviously toggle everything off if you just want the grid for reference of where the ground
[9:16] should be in your scene that's nice too so I'm going to reset this turn it off let's continue down
[9:21] the next thing of import is this lock button this is lock camera to view so let's create a camera we
[9:26] can hit tab and type in camera for now we'll create that and then if we navigate up here next to the
[9:31] perspective drop down that we looked at where we can set all our different views to the right of
[9:36] that we have no cam this is where we can select our camera you can see cam one cam one the same
[9:42] naming convention if I change this to cam 12 or whatever then I'll see that's updated there so
[9:48] if I click this we are now looking through our camera now we're not seeing anything because
[9:53] the camera defaults if you create it with the tab menu to zero zero zero the center point of our
[9:57] world but let's say we want to move it well we can move it with this as you might expect but this is
[10:04] like this is this sucks I hate this I don't want to do that so let's actually reset to zero zero
[10:11] zero and let's say I want to move this just like I would be you know moving my scene if I if I want
[10:16] to rotate my scene around and get a good view this is the best way to do it so if I want to set up my
[10:20] camera the same way how would I do that well this lock is one way to do that if I go ahead and look
[10:25] through the camera and turn on the lock now whenever I navigate as I normally would in Houdini
[10:31] you see this letterbox stays there this has to do with the aspect ratio of the camera settings
[10:35] which we can look at later as well but simply by roaming around and scrolling and zooming as I
[10:41] normally would now I'm actually positioning my camera if I turn this off and I zoom out you see
[10:48] the camera now stays whereas if I'm in there I lock it and now I zoom out the camera moves with me
[10:53] I'll unlock it I'll zoom out again and the camera is now in its new position and this way we can
[10:58] position our camera very freely you will be toggling this a lot there was a very real danger of
[11:03] forgetting this is on me warning you now will not save either of us in the future we're going to
[11:08] make that mistake and it's okay but just remember turn it on when you need it and then as soon as
[11:13] you're done turn it off so it doesn't cause you any more problems continuing down we have the
[11:19] lighting section right here all of these pertain to the exact same thing if I have a light in my
[11:24] scene I'm going to create a little light here and in fact I'll just move this over this is the
[11:29] little shortcut command window so you guys can see what I'm doing I'm going to zoom up I want to put
[11:34] this back on the zero of the ground plane in fact I'll put it 0.5 so it's kind of sitting on the
[11:38] ground here I also want to create a grid this is going to basically give me a ground plane and then
[11:45] this light I'm going to lift it up above my scene right so what we've got is a point light above a
[11:51] sphere above a ground plane and in that way we are getting some light play now it's not high quality
[11:58] it's not like you know what you'd see in a final render but it's giving us some idea of how the
[12:03] light is impacting our scene right we're getting that fall off of light you know as ghetto as it
[12:08] looks and we're getting light cast on the surface of the ground as well but we can change this right
[12:12] we can just toggle between these essentially the very bottom here is disable lighting this is not
[12:19] disabling your lighting in your scene for the render it has nothing to do with that I want
[12:23] you to separate those things in your mind this all pertains all down this side only to what we
[12:28] are seeing in the viewport it's all temporary it's all just servicing us building the scene and that
[12:33] said it doesn't go any further than that so if we toggle disable lighting now we've got no lighting
[12:39] if we are also in smooth shaded mode well now we can't see a gosh darn thing we have no dimensionality
[12:46] so this is actually probably a better view of this this is no lighting in the scene we can then
[12:50] choose the headlight only this will generate a a temporary headlight in our scene that is tethered
[12:56] to where our view is and you can kind of see that in the specular here on the on the sphere itself
[13:01] wherever we move that specular exists because that headlight is essentially attached to our
[13:06] perspective of the scene so in that way you get consistent lighting but we still get that dimensionality
[13:12] right that shadow that will that will separate objects in our perspective that is very helpful
[13:19] when we're working with scenes if you want to up it to the next level you can enter normal lighting
[13:24] and that's where we started essentially again these all have little buttons so we can enable or
[13:29] disable the specular highlight for example from that light we can enable and disable the diffuse
[13:35] itself like we can customize each of these lighting setups in whatever way we want there's a lot of
[13:40] flexibility in the scene view we can also elevate and go to high quality lighting now it's a minor
[13:47] difference here right you're basically seeing like a slight shift in the specular of which we can also
[13:52] turn on and off but like there's other stuff too depth of field bloom like there's a there's a lot
[13:57] of other things that we now have access to to further build out our our temporary view of what
[14:04] it is that we're building but there's also high quality lighting with shadows ooh now look what
[14:09] we got now we've got it casting our hard shadow if we change the light type to a light here with
[14:16] uh a little more area to it right let's say we choose a disc instead we rotate it you know i'll
[14:23] do negative 90 degrees so it's facing right down well now look we got like really nice shadows in
[14:28] this scene for the most part now what you might have is point shadows right out the gate that means
[14:33] no matter what the light source is you are going to have these hard hard hard shadows but the reality
[14:38] is a quick lesson on light is the larger the source of light is uh that is being cast on your object
[14:45] the softer your shadows are because the light is hitting it from more areas so whereas one part
[14:51] of the light is casting a ray that is creating a hard shadow the other part of the light is actually
[14:57] on the other side of the the object and is filling in part of that hard shadow so you instead you get
[15:02] like a fall off so an area this big if i instead want to see what this really looks like i can do
[15:08] area shadows and it'll take all that area of the light into account you can see how much softer
[15:13] that shadow is now if you enjoyed this video and you want to learn more head to doublejumpacademy.com
[15:18] slash jordan for the full course links in the description you just click away click it



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
