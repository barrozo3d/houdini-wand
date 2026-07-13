---
title: Ruins randomized brick wall
source: YouTube
url: https://www.youtube.com/watch?v=QEvlyVTk4Jw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ruins-randomized-brick-wall/
frame_count: 0
frame_status: pending-selection
---

# Ruins randomized brick wall

**Source:** [YouTube](https://www.youtube.com/watch?v=QEvlyVTk4Jw)
**Author:** cgside
**Duration:** 10m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py ruins-randomized-brick-wall <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So today I wanted to share with you how I created
[0:06] this broken stone wall with enough variation on the bricks alignment. So I started
[0:17] with a box and this is my initial shape. Then I created this curve that will
[0:31] act as the breaking pattern or the bullion pattern that I'm doing right here.
[0:39] Then this is my input mesh. And from here I am creating some curves. One for the y-axis,
[0:53] one for the x and one for the z. I'm doing that with extracting it from bounds of my input mesh.
[1:03] So then as you can see if I do a Voronoy fracture and see the attribute name, we are creating slices along
[1:16] the geometry. So in order to do that we have the ads. Then I am re-sampling. So I can choose how many
[1:32] sections I will have in this case in the y-axis. Then I am grouping the inner points and jittering
[1:42] those inner points. So I don't get the ends jittered. Then I'm cutting every points. So I create
[1:55] segments. Then having those individual segments I can subdivide. So this way the individual sections
[2:11] will have a consistent amount. If I disable the jitter you can see that they are in the perfectly
[2:21] distributed. So I'm subdividing just one subdivision. Then fusing the points, sorting them in this
[2:38] case in y and grouping the middle points or the every other point and blessing those. And in the
[2:52] end we just set to have the middle points that will be used to do the fracturing. As you can see
[3:09] this is the first level of fracturing. In this case we don't need a loop because we want to
[3:14] randomize it. So then I am going to disable this one and enable this fracturing. So right here I am
[3:29] using a Voronai fracture in a loop. This way I can randomize the jittering of each line. So we have
[3:41] this line here that we are doing exactly the same. But the difference is that I'm using the
[3:49] detailed iteration attributes and a seed value to randomize each layer of fracturing.
[4:02] So if I disable the jittering we will have straight lines like this. This way we are randomizing
[4:12] the position of each brick. Then I'm doing exactly the same for the Z axis. So as you can see here
[4:25] and I can always come back and change the amount of sections.
[4:43] In this case I want 29 and I can do the same here. Make the bricks longer
[4:57] and the same in the Z axis. Then right here I am using an exploded view just to separate the bricks
[5:06] a little bit. This will help for the Boolean and also visually to have some separation between the
[5:14] bricks. Then I am Boolean out a shape. They can from the initial shape and doing a fracture
[5:28] and cleaning it. We end up with something like this that we can use to Boolean.
[5:41] And then I am saving the B inside A from the Boolean output. So I can affect those inner polygons.
[5:54] Then I am creating a connectivity attribute to have an individual piece for each brick.
[6:06] And I am transforming a bit. I am rotating a bit randomly the individual bricks with a
[6:16] transform node. I can set the amount and I also have a seed just with a feed function.
[6:29] And I am creating a attribute here called inside bricks. Just using the fracture bricks group.
[6:41] And then I am blurring the attribute and I am also remapping. So I can use it here in the edge
[6:50] damage or ship edge damage that can be compiled. Basically doing a remesh. First measuring the area of
[7:01] the brick so I can remesh based on the size of the brick as you can see here.
[7:10] Then I am blurring a bit the edges. And as a way to attribute I am using that same inside bricks
[7:25] attribute. And I am also peaking and basically doing a Boolean. And you can play with the amplitude of
[7:37] the noise of the mountain. And with the peak to have more or less damage.
[7:45] And I am doing that for every brick. And if you compile it it should be fast enough.
[8:00] So we end up with something like this. And we can get rid of the attributes.
[8:07] And as you can see this is the final result with some edge damage.
[8:16] More pronounced along the inside bricks as I call it. And less pronounced in these areas where
[8:24] there is no much fracture. And I am doing that again in the attribute blur with a weight attribute.
[8:33] And in the mountain I am also blending the attribute inside bricks.
[8:40] Then I am just creating a black and white mask. So I can use it for texturing or any other purpose.
[8:50] And that is easy enough. Just doing a randomization of the class attribute. And assigning it to
[9:02] to a color attribute or vector attribute. Or you can just do it with the attribute adjust color
[9:10] by feeding the class attribute in a pattern type set to random.
[9:18] So that's basically it. I hope you have learned something new. And make sure to check out the
[9:24] Patreon file if you want to investigate on your own and do your own version.
[9:29] I also included some other setups like this one.
[9:38] As you can see, something like this, even in regular shapes should do a good job.
[9:45] And this is just the basic setup of the bricks without variation.
[9:51] But the more simplified network. And this is the first approach I tried.
[10:01] Which also works. But only for box like shapes. So thank you and see you in the next one.



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
