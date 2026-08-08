---
title: Houdini for Beginners-  Part 9:  Layouts
source: YouTube
url: https://www.youtube.com/watch?v=K9aMZvNCRF0
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-for-beginners--part-9-layouts/
frame_count: 0
frame_status: pending-selection
---

# Houdini for Beginners-  Part 9:  Layouts

**Source:** [YouTube](https://www.youtube.com/watch?v=K9aMZvNCRF0)
**Author:** Jordan Allen
**Duration:** 9m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-for-beginners--part-9-layouts <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] The primary goal of this video is to bring the geometry spreadsheet into view so we can see both things at the same time
[0:06] But this does raise a larger question of the overall organization of our scene, right?
[0:11] We've got our network view, we've got our parameters, we've got our scene view
[0:14] But what if we want to customize this a little bit?
[0:17] I mean, there's a setup that I've been using for a long time that I really like
[0:20] And I want to show you guys how to set it up as well. So let's do that right now
[0:24] First things first, let's clean up these tabs
[0:26] This is not necessary, by the way, what I'm doing right now
[0:29] I haven't even done this myself, but I figure, hey, while we're all here cleaning our room, I'll clean mine too
[0:34] I'll clean mine up a little bit as well. So I got some good stuff coming out of this as well
[0:39] This render view tab is the first one I want to get rid of
[0:41] We will go into this at a later date, but essentially there are two renderers that are native to Houdini
[0:47] There is the Mantra renderer or the Mantra renderer if you're a US citizen
[0:52] That is the old version of Houdini's built-in renderer
[0:55] This is the render view that we used to use for that. Let's close that out
[1:00] Let's also get rid of the composite view and the motion effects view for now
[1:04] We can always add those later. Let's also get rid of the geometry spreadsheet
[1:07] If you accidentally close something that you didn't want to, let's say we got the scene view and we closed it
[1:11] Whoops. Well, we can click this new tab button right here or press control T
[1:18] And we can choose what tab we want to open up
[1:23] Now you know there's a lot of them, right?
[1:24] Again, the majority of the stuff is hidden underneath the surface for Houdini
[1:28] It really depends on on your needs
[1:31] So for us, you know in the viewers the scene view is what we need
[1:35] Now it's also good to know how to create this because again
[1:38] If you are having a glitch in your scene view and you don't have labs installed for whatever reason
[1:43] So you can't hit reset viewport then you can just close it out
[1:48] Open a new pane tab type go to viewers and open up the scene view and then you've got it
[1:52] You can just click and drag it to reorder it as well
[1:54] To your heart's content. These are the only two that I think we need open
[1:58] up for our purposes
[1:59] But I do want to get the geometry spreadsheet open
[2:02] And I want it to be on screen at the same time either to the left of the scene view or to the bottom
[2:07] Now considering the majority of things that we're going to be doing in film will probably be roughly a 16 9 aspect ratio
[2:13] Right? It makes more sense for it to be the bottom
[2:16] Because considering my my actual monitor is 16 9 and this is eating into that space
[2:22] 16 9 is somewhere in here
[2:25] Perfect for a little bit of geometry spreadsheet right at the bottom
[2:29] If I want it which I do so let's go ahead and click this little drop down right here at the top right
[2:35] And just so you know this is the maximize pane button if you ever want to just go full screen
[2:40] Well not full screen sorry, but you know dominate the view outside of the tabs and bars and whatnot with your
[2:46] Your scene view you can do that and you can do that with any of these right at any time which is great
[2:51] So very handy, but I want to click the button to the right of that the little drop down arrow
[2:55] You can see it's the pane tab
[2:57] operations and here is where we have a little bit of flexibility in how our panes are are
[3:04] laid out what we want to choose is
[3:07] To split the pane top and bottom and this will create essentially a duplicate pane
[3:13] Underneath my other one, so I'll move this out of the way and then here is where I want to hit that plus button
[3:19] I'll go to my inspectors and my geometry
[3:23] Sheet I can now close that scene view and then we only have one and you'll notice in the middle there are
[3:31] Sections for you to click and drag to extend or contract your windows
[3:35] And there's also little buttons to the left and the right which if you click will fully
[3:40] Collapse or expand these things as well and these exist on every border of every of every window basically
[3:47] Okay, so that's great
[3:50] I'll put this over here again
[3:52] Another thing that I want to do is I want to split my network view and my parameters
[3:57] Window left and right so that I have two versions of them. I'll show you why that is if I have a sphere
[4:05] And I got my camera and all these goodies and I'll create a box
[4:10] I have access to either inside of this the parameters of this
[4:14] Or inside of this the parameters of this now if I am editing these in relation to one another and I'm going in here and I'm
[4:21] You know making a change here for whatever reason now
[4:24] I need to make a change to the box so I go back out and then I go back in here and then I highlight this and I
[4:29] You know make a change here and maybe I rotate it
[4:32] That gets a little old going out and in and out and in
[4:35] Um, there are a few ways to to navigate this headache
[4:38] The first is to hit control and press one two three four or five
[4:42] You see how it's saying set quick mark there
[4:45] This is very handy
[4:46] If I hit control one and then I go to another context entirely
[4:50] And I hit control and press two now if I just press one or two when in the network view
[4:57] I jump to my quick mark right. It's almost like a bookmark
[5:01] location
[5:03] So you can set those up
[5:04] But sometimes it's nice to have them both open at the same time
[5:07] And so what we can do right here is off to the right click that same pain tab operations drop down
[5:13] and
[5:14] Split pain left and right. I'm going to do the same thing up here split pain
[5:19] Left and right and I get a duplicate now
[5:21] I can jump into one on one side or jump into the other on the other side
[5:24] The problem right out the box though is if I jump into one like it changes both
[5:29] Well, that's frustrating
[5:31] Luckily, there is the ability to pin things, which is just literally right here. If you look at this one, it's saying
[5:38] Linked to the same numbered pains. So if we look at the other pains, what do we see?
[5:43] We've got a one here a one here and a one here
[5:46] So if I make a change in here in this pain, it's updating all these pains
[5:50] But if I leave these two both as one because I want the parameters tethered to what's going on in the network view underneath it
[5:58] But I change this by clicking and holding to two
[6:01] And then I change this to two
[6:04] Now if I go back out
[6:06] We stay in
[6:07] And now I've got parameter access for this and if I go into the box here
[6:11] I've got parameter access for this right. I can do whatever changes I want
[6:18] I'm going to collapse this for now just for more visibility in the scene view
[6:22] Um, you can also pin your scene view itself
[6:27] To now right now it's following selection. Whatever you are
[6:30] Clicking is what it is showing in the viewport. But typically I like to use this secondary portion, right?
[6:36] the right hand side of of this split as my
[6:40] Additional tweaks meaning I don't really like to visualize them. I like to keep whatever's in
[6:45] The left section visualized and just tweak the parameters of the right side to update whatever I'm seeing
[6:50] So what I do typically is I click on the pin here click and hold and I let go on one there
[6:56] So now this is tethered specifically to this
[7:00] So just a real quick recap changing this to one one one
[7:05] So these are always tethered and then adding a split to two and two
[7:09] Just so we can use it in the future that'll come in a lot of handy
[7:12] For the most part though, I do collapse these until they're needed and then they're just out of the way, you know
[7:16] I can very quickly just pop these open
[7:19] And make any tweaks I need
[7:21] And then shut it again now
[7:24] If you just close Houdini after doing this and you open it up again, everything will be back to normal
[7:29] We don't want to waste time doing that every single time we open the software
[7:33] And so we're going to save the layout which you can do in this drop down right here. It says build
[7:37] This is the currently active desktop layout, right?
[7:41] And we can save the current desktop meaning that the build layout will now be what we've created
[7:46] Or we can save the current desktop as I'll call it
[7:52] Jordan's
[7:54] Default that's what I'll call mine
[7:56] So now in Jordan's default. We've got our splits as needed that does raise the question real quick on what are these? Well, these are
[8:05] preset setups for you
[8:07] um that you can use when doing specific things in
[8:11] Houdini for example, we will typically live over the duration of this tutorial series in our custom setup
[8:18] the one we just did right now and the
[8:20] Solaris look dev setup, which is more for rendering and whatnot, you know
[8:24] Really when you're working in any different contexts as we've kind of lightly discussed in the past
[8:30] There are different default setups for tools and visualizers for the the specific thing that we're working on
[8:38] So, you know the Solaris look dev is designed specifically for designing your lighting and layout for final render
[8:44] Now i've danced around this idea of contexts a bit and I think
[8:49] I think it's time to make a dedicated video about it
[8:51] If you enjoyed this video and you want to learn more head to double jump academy dot com slash jordan for the full course
[8:57] Links in the description. You just click away click it



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
