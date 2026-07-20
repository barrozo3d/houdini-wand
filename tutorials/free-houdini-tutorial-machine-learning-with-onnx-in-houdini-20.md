---
title: Free Houdini Tutorial: Machine Learning with ONNX in Houdini 20
source: YouTube
url: https://www.youtube.com/watch?v=aCAatiY53s8
author: Entagma
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/free-houdini-tutorial-machine-learning-with-onnx-in-houdini-20/
frame_count: 0
frame_status: pending-selection
---

# Free Houdini Tutorial: Machine Learning with ONNX in Houdini 20

**Source:** [YouTube](https://www.youtube.com/watch?v=aCAatiY53s8)
**Author:** Entagma
**Duration:** 20m56s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py free-houdini-tutorial-machine-learning-with-onnx-in-houdini-20 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro to ONNX [0:00]
**Transcript (timestamped):**
[0:00] With Houdini 20 we got our first official machine learning node from SideFX.
[0:06] While we previously had example scene files that did machine learning related stuff, or
[0:10] plugins like ML Ops, this is the first machine learning tool that you get just by installing
[0:15] Houdini.
[0:16] So this makes it quite interesting and we should take a look at what it does and what
[0:20] we can use it for.
[0:21] So this is the node that we got, this is the ONNX inference solve.
[0:25] And I should first of all maybe start by explaining these two words right here.
[0:29] First of all start with inference.
[0:31] If you know your neural network lifecycle, you know that we started by building our neural
[0:36] net, then we're training and testing our neural net with our training data, then we
[0:41] validate the use of a neural net and if we finally are happy with the results that we're
[0:47] getting then we can finally use our neural net for the actual tasks that we set out to
[0:52] do with this neural net.
[0:54] And this final part, this usage part, this is what we call inference.
[0:59] So our ONNX inference solve in the end, we'll also be just there to use trained neural
[1:04] nuts.
[1:05] It's not there to train some neural nets or to build some neural nets.
[1:09] Let's talk about the ONNX part.
[1:11] Why is ONNX important?
[1:12] Well this starts because doing inference the traditional way is quite cumbersome.
[1:18] We need quite a lot of stuff for this.
[1:20] We need a coding environment, usually Python.
[1:23] We need some machine learning libraries, maybe PyTorch.
[1:26] We need our code, usually stored in a .py file and we also need the data that we got
[1:32] through training on neural net.
[1:34] This is usually a checkpoint file and for PyTorch this is a .pt file.
[1:38] So previously if we wanted to do something machine learning related in Houdini we had
[1:44] to make sure that we brought all of those things to Houdini as well, which means set
[1:49] up a custom Python environment with those libraries and it's all again quite cumbersome.
[1:55] To make this easier what also was developed alongside those machine learning tools are
[2:01] so called machine learning runtimes and ONNX is one of them.
[2:05] What those runtimes allow you to do is a runtime first of all takes what's usually done with
[2:10] a coding environment and a machine learning library and simply turns it into a program.
[2:15] In this case it's ONNX runtime.
[2:18] And then we as a user we can simply take a neural network project, a py file and the
[2:23] training checkpoints and export them as an ONNX file as a single file that we can simply
[2:28] hand over to our ONNX runtime and our ONNX runtime will make sure that we can use this
[2:34] machine learning file in a lot simpler way.
[2:37] And what this in the end means for Houdini is that side effects took this ONNX runtime
[2:42] and implemented this into Houdini in this ONNX inference sub and this ONNX file is something
[2:48] that we can provide.
[2:49] We can private either because we trained our own neural net and exported it as an ONNX
[2:53] file or this may be something we got from our technical director at the studio or maybe
[2:58] this is also something that we simply found on the web because ONNX is an open standard
[3:03] and it's been around for quite a while so we also find a lot of really good ONNX files
[3:08] online.
[3:09] And the last part is exactly what we're going to do today.
[3:12] We're going to download a bunch of ONNX files and test them inside Houdini.


### Getting ONNX Models [3:14]
**Transcript (timestamped):**
[3:16] So first of all to download some files I went to github.com slash ONNX slash models.
[3:21] This is a collection of pre-trained ONNX models that we can simply download and play with.
[3:27] And the first one that I'm going to download right here hides under domain based image
[3:31] classification and is an ONNX version of the Amnist model which is a sort of hello world
[3:37] for machine learning.
[3:38] So let's download this and we can download all these models by clicking on this link
[3:42] right here.
[3:43] We have usually a lot of options for selecting different versions basically an ONNX version
[3:49] and an Opset version.
[3:50] In the end there are some technical details surrounding those but in the end this mostly
[3:55] boils down to trying different models out and see which work in Houdini and which don't.
[4:01] And in this case I'm going to use this Amnist-12 model and I'm going to use the simple download
[4:07] without the sample test data.
[4:10] So let's click on this button right here on this link and finally on this page we can
[4:14] click this download button right here.
[4:16] Handwritten digits are a bit boring.
[4:17] Let's select something that's maybe a bit more interesting.
[4:20] And in here under image manipulation we have a fast neural style transfer.
[4:24] So let's try this out as well.
[4:27] Again we have some options to choose from here.
[4:29] We have first of all a bunch of different styles that we can try and we also have this
[4:34] selection between an Opset version of 9 and 8.
[4:37] I think in this case this doesn't matter for Houdini but in the end I'm going to download
[4:42] this Mosaic model and with an Opset version of 9.
[4:45] So let's click this download button right here and let's download it here.
[4:49] And finally I wanted to download something that's maybe a bit more useful for us.
[4:53] I wanted to find an ONNX version of the Midas depth estimation model where we can put in
[4:59] an image and get a depth map out.
[5:02] And in this case I found this project from Julien K which used an ONNX export of Midas
[5:08] for Unity.
[5:09] However, since this is an open standard we can simply use the same files in Houdini as
[5:14] well and we can find those files under files and versions in the ONNX folder.
[5:19] And in here I want to download the dpt-swint2-base model with a resolution of 384 pixels.
[5:27] And I can hit this download button right here to download my model.


### MNIST Model [5:29]
**Transcript (timestamped):**
[5:31] Now finally in Houdini I want to drop down a geonode, I want to dive inside and I want
[5:37] to drop down my ONNX inference node.
[5:40] And the first thing that I'm going to do always when I bring in such an ONNX node is
[5:44] I first of all want to load in the ONNX file that I downloaded.
[5:48] So in this case let's start with Amnesty, let's select this Amnesty 12 model right here.
[5:53] And next we want to hit this button right here, this setup shapes from model button.
[5:58] Let's click this and what this button does is it fills in those four parameters with
[6:03] the right values that this net, this model that we loaded in expects.
[6:08] And what those values are are basically how the data that we're going to feed into a net
[6:12] should be shaped.
[6:13] So let's take a closer look at this.
[6:15] This consists of a bunch of values, those values are read from left to right and top
[6:20] to bottom and these are the dimensions of the input tensor.
[6:25] This is a fancy way of saying that we're going to feed our data to a net in a multidimensional
[6:30] array and that array should have a specific structure that our net expects.
[6:35] Now the first value inside that array will always be the batch size.
[6:39] So in this case how many pictures of handwritten digits we're feeding to our net at a time.
[6:45] And usually with those ONNX models this will be either one, so we're going to feed one
[6:50] image at a time to our net.
[6:52] This is going to be minus one, which means that we can feed any number of images through
[6:57] a net at a time.
[6:59] In this case this is set to one.
[7:01] Next because we're feeding in an image there's a sort of standard data structure and that's
[7:05] quite common with machine learning, which means we get first the number of colors in
[7:10] our images and in this case since this is a grayscale image, this is just a value of
[7:15] one and then we have the resolution of our image and this is 28 by 28 pixels.
[7:20] This is what we're putting in and what we're getting out is again our batch size and then
[7:24] just 10 float values which will be the 10 probabilities how likely a certain number is
[7:30] based on the image that we're feeding in.
[7:33] So let's finally try this out.
[7:34] Let's first of all create a canvas to write on.
[7:37] In this case this will be a grid.
[7:39] I'm going to set the size to one by one, but this doesn't matter in this case.
[7:44] What does matter though is the resolution.
[7:46] We have to put in 28 by 28 pixels like this.
[7:50] Then we need to paint a number onto this.
[7:52] So let's drop down a paid note and I'm going to choose the paint a mask variation of this
[7:57] note.
[7:58] While this in let's switch to a handles tool.
[8:00] Let's make a brush a bit smaller and let's maybe first of all get a visualizer going
[8:06] so you can see what we're doing and let's maybe draw a nice four in here like this.
[8:12] Come back to our camera tool and let's feed this to our next net.
[8:16] Now we have to set up the way how we're going to feed this data to a network.
[8:21] In this case I'm going to use a point attribute and this point attribute is called in this
[8:26] case mask since I used this paint mask note earlier.
[8:29] And finally we have to select how we're going to write this data back out again.
[8:32] In this case again I'm not going to choose a volume.
[8:35] I'm going to choose a point attribute and let's maybe call this proper for probability
[8:40] and now taking a look at the info panel we have 10 points for 10 values and if you take
[8:45] a look at those values you can see them right here and if we sort by the highest value we
[8:50] can see by a large margin 4 seems to be the most probable digit that we drew right here
[8:56] and this is of course also correct.
[8:58] We drew a 4 in here as well.


### Style Transfer Model [9:00]
**Transcript (timestamped):**
[9:00] So a net right here is obviously working.
[9:02] However this isn't hugely exciting.
[9:04] Let's maybe try a style transfer next.
[9:07] Let's drop down another on next note.
[9:09] Let's load in our mosaic 9 model.
[9:12] Again let's hit set up shapes for model.
[9:14] Now this looks like this.
[9:16] Again we have first of all a badge size right here.
[9:18] Now we have 3 values.
[9:20] So an RG and B value since we're putting in color values and we have a different image
[9:25] resolution so in this case 224 by 224 pixels and also output matches exactly our input
[9:31] because again we're just going to transfer a style to our image so the image size should
[9:37] match our input image as well.
[9:40] Let's set up this.
[9:41] Let's drop down a grid node again.
[9:43] Again set the size to 1 by 1 but in here I want to put in 224 by 224 pixels.
[9:49] Also want to set the UVs on this grid.
[9:52] Let's drop in a UV texture node and for the image that I'm going to load in I want to
[9:56] change up the scale and offset a tiny bit.
[9:59] I'm going to set the Y scale to minus 1 and an offset of 1 to flip it the right way around
[10:05] and I want to set the X scale to a value of 0.6 and give it an offset of 0.2 and this
[10:13] is simply there because I'm going to load in a 16 by 9 image and putting this onto a
[10:19] square patch of geometry you would squash it and this is there to limit that squash.
[10:23] Now let's finally load in our image.
[10:25] Drop down an edge from map and in this case I'm going to load in a teaser image from a
[10:29] previous episode and you can choose your own input image that you like.
[10:34] In this case mine will be this right here and let's maybe also turn off a UV grid like
[10:38] this.
[10:39] Let's wire this into our ONIX node.
[10:41] Again we're going to set up how we want to write in and out our data.
[10:45] In this case this will be both our point attributes and let's put in our CD both in the input and
[10:50] the output and since this ONIX node always collapses this output around world origin
[10:56] we have to copy over and attribute again.
[10:59] So let's drop down an attribute copy node and let's copy over in the CD attribute that
[11:03] our ONIX node spits out in the end and also maybe we write this like this so you can actually
[11:08] see the output and as we can see right here this seems to be something wrong with the
[11:13] output.
[11:14] We seem to have made some mistake right here.
[11:16] So what mistake did we make right here?
[11:19] This is something that's quite common with feeding an image data into this ONIX node
[11:23] because the data that we feed in right here, the OCD attribute, doesn't quite match up
[11:28] the data structure right here that ONIX expects.
[11:31] What do I mean by that?
[11:33] Well what ONIX expects is first of all all the red values, then all the green values
[11:38] within our image and then all the blue values within our image.
[11:41] This is what this tells us.
[11:43] However what we're getting it by writing in just a CD attribute is all the RGB values
[11:48] for the first point, then all the RGB values for the second point and so on and so forth.
[11:53] So again what ONIX expects is matching the data that we're feeding in so in the end we're
[11:58] getting a garbage output.
[12:00] Basically this is quite easy to fix.
[12:01] We just have to restructure our data.
[12:04] First of all I want to set a different attribute that I want to write in.
[12:07] Instead of writing in a vector attribute I just want to write in a float attribute that
[12:11] I will call in and I'm going to write out a float attribute that I will call out.
[12:16] And what I want to create now is a set of points, a set of points with a total number
[12:20] of 3 by 224 by 224 that matches this data structure and I can create this with 3 point
[12:27] angles.
[12:28] This is why I'm our first one.
[12:29] I'm going to create a new attribute called in and this should be a float and this should
[12:34] be equal to from a CD attribute just the red value like this.
[12:40] This is all this wrangled us.
[12:41] Now I'm going to copy this two more times and on the second one I'm just going to choose
[12:46] all the green values and on the third one I'm just going to choose all the blue values.
[12:52] And now with our data separated like this I can merge this back together and now taking
[12:57] a look at the info panel I should have 3 by 224 by 224 points right here and this should
[13:03] add up or multiply up to this value right here and on those bunch of points I have the
[13:08] value that I want to feed into our net as a single float value called in and this now
[13:13] should match this structure up here.
[13:16] So let's feed this into our net.
[13:18] Our net isn't complaining anymore and now we have to do the same that we did right here
[13:23] to write our data back out to our grid.
[13:26] So attribute copy won't do here.
[13:28] We need another point wrangle and on this point wrangle I first of all want to grab
[13:32] all the float values.
[13:34] This will be a point function on geo stream 1 which takes a look at the value called out
[13:39] and our float values should simply match our pt num that we're putting in.
[13:44] Then let's grab our green value.
[13:46] A green value should match the pt num that we're putting in plus the total number of
[13:51] points that we have on this geo stream because we have three times less points on this geo
[13:55] stream than we have on this geo stream.
[13:57] So to get a number of points let's first of all create an int called np and this should
[14:04] be equal to the endpoints function on geo stream 0 which gives us the number of points
[14:09] on that geo stream and let's simply write pt num plus np and let's do this one last
[14:16] time for our blue values and our blue values will be the values of our pt num plus np plus
[14:23] np a second time like this.
[14:26] And finally let's write this out to our cd.
[14:28] This is equal to a vector consisting of our rg and b values like this.
[14:35] Now this looks a bit more correct.
[14:36] The one thing that we need to do in the end to make this work is to normalize all those
[14:42] values that our onluxnet here is putting out because the output values of neural nets
[14:47] usually aren't between 0 and 1 values like we need for our color.
[14:51] We have to normalize those ourselves.
[14:53] So in this case I'm going to use a labs attribute normalize float.
[14:57] Let's wire this in and wire in our select out attribute in here and now finally we have
[15:03] the style transfer on the image that we're putting in and since I put in an animation
[15:08] I can scrap in my timeline and as we can see the style transfer is working really quite


### Depth Estimation Model [15:13]
**Transcript (timestamped):**
[15:13] fast and nicely.
[15:15] So this is our style transfer working.
[15:17] Let's maybe now quickly take a look at our depth estimation as well.
[15:21] This in the end should be pretty similar to this setup so let's just copy this.
[15:25] Let's set our display flag at our onluxnet.
[15:28] Let's load in our dpt swim model.
[15:31] Again setup shapes from model.
[15:33] Wait for this to cook.
[15:35] So the data that we're feeding in looks quite similar.
[15:37] We still have a batch size of 1, still 3 colors but now a different resolution, 384 by 384
[15:44] and our output looks a bit different as well because we don't have any colors for our output.
[15:49] We just have single float values for our depth.
[15:52] So in this case our output is just again our batch size and then just our resolution like
[15:57] this.
[15:58] So let's set this up.
[15:59] Here on our grid let's enter 384 by 384.
[16:04] Everything else that we did here loading in our image and separating it and restructuring
[16:08] our data this should all still work.
[16:11] We can still leave this attribute normalized float in here.
[16:14] The only thing that I want to change in here is how we write back our data.
[16:18] We can already see a sort of depth map appearing here.
[16:21] This in this case doesn't need to be discomplicated.
[16:25] What we want to do in the end is simply first of all grab our depth value.
[16:30] So float depth will be a point attribute on tier stream 1 called out and since we have
[16:37] the same number of points on this tier stream as we have on this tier stream we can simply
[16:41] put in at ptnum in here and then let's move our points by our depth value.
[16:47] So v at p plus equals a vector that we're going to create and this has an x value of
[16:53] 0 and y value of depth and a c value of 0 again.
[16:57] Let's take a look at this.
[16:59] This seems to be working already.
[17:01] Let's maybe bring over our attribute from map so we can also see our image overlaid
[17:06] onto this and yes this seems to be a sort of working depth map.
[17:11] At least the kind of quality from a depth map that I'm going to expect from a machine
[17:15] learning model.
[17:16] Let's maybe just make this a bit more shallow.
[17:19] Let's maybe take this to a value of 0.3 like this and yeah I think this looks a bit more
[17:24] accurate.
[17:25] Now this is where I'm going to leave this for today.
[17:27] If you're curious about the teaser image of this episode you can take a look at the
[17:30] scene file.
[17:31] You can see a common version of how I built this in the end.
[17:35] A style transfer on a geometry inside Houdini.


### Limitations [17:37]
**Transcript (timestamped):**
[17:39] What I want to talk about quickly now is what this means for machine learning in Houdini
[17:45] in the future.
[17:46] Is this now a standard way of doing machine learning stuff inside Houdini?
[17:50] Does this make something like ML Ops obsolete?
[17:53] And we now run for example Stable Refusion just with those ONIX nodes.
[17:58] And this is where it gets a bit complicated.
[18:01] Stable Refusion in this case is quite a good example because it's a quite complicated neural
[18:06] network pipeline.
[18:08] I made a very simple diagram of this here.
[18:10] Our prompt goes into the text tokenizer.
[18:13] This goes into the clip encoder.
[18:15] Then we have a latent noise which gets denoised to output image in the end through this unit
[18:21] and schedule a loop.
[18:23] And finally it gets resized to the final output resolution by our variational auto encoder
[18:28] and this in the end gives us an output picture.
[18:31] If you played a bit with ML Ops you're somewhat familiar with this structure right here.
[18:35] If you haven't this isn't really important.
[18:37] What is important is that we can take a look at all these stations that are prompt goes
[18:42] through and sort of categorize them into two categories.
[18:46] Those orange stations which all are consisting of neural nets.
[18:50] Then we have those blue stations which are all just standard algorithms.
[18:54] And at least as far as I'm concerned as far as I got with my testing I think we can just
[19:01] use the ONIX node for those neural net parts.
[19:04] So we can rebuild or use the clip encoder inside Houdini and the unit and the variational auto
[19:09] encoder but not the scheduler or the noise generation or the text tokenizer.
[19:14] For those parts of this Stable Refusion pipeline we still would need to either code this ourselves
[19:20] or use some sort of custom python environment with custom python libraries and this in the
[19:25] end sort of defeats the purpose of using ONIX in the first place.
[19:29] So with some newer neural network workflows or some more complicated neural network workflows
[19:35] at least as far as I can see we are running into some limitations of the tools that we
[19:41] have right now in Houdini.
[19:42] I'd love to be proven wrong on this.
[19:44] I'd love to see some more talent and TDs tackle this challenge right here and maybe
[19:49] create a working version of Stable Refusion inside a vanilla Houdini just with those
[19:54] ONIX nodes.
[19:55] I'm really looking forward to this one but at least from my experience this at the very
[20:00] least seems to be a pretty difficult task.
[20:03] This isn't something that you build in an afternoon.
[20:05] However still with the options that we got right now we still have quite a lot of neural
[20:10] nets that we can use and we have also quite a lot of really interesting applications where
[20:15] we can train our neural nets.
[20:17] This is definitely something that we're going to explore in the future.
[20:20] But until now I hope you have fun playing with this new ONIX node, trying out different
[20:25] models that you can find online and until next time it's cheers and goodbye.
[20:30] If you like what we're doing please consider becoming a patron of ours.
[20:33] Not only for supporting ATACMA but also for access to end-of-courses like our advanced
[20:38] setups course which already includes a couple of videos about neural nets or a complete
[20:42] prevent beginner series with 30 videos telling everything about attributes, simulations and
[20:48] so on.
[20:49] Also let me say thank you so much to all our existing patrons without you this channel
[20:54] would not be possible.
[20:55] Thank you.



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
