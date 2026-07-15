---
title: Vex quick tips #2 | Iterating over numbers
source: YouTube
url: https://www.youtube.com/watch?v=7PHYAnZbTvM
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [vex, quick-tips, for-each, lots-of-division, random-cut, find-shortest-path, expand-point-group]
extraction_status: complete
frames_dir: tutorials/frames/vex-quick-tips-2-iterating-over-numbers/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Vex quick tips #2 | Iterating over numbers

**Source:** [YouTube](https://www.youtube.com/watch?v=7PHYAnZbTvM)
**Author:** cgside
**Duration:** 14m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to show you a quick way to have a more pleasing result with a lot of division
[0:08] lab stool because usually when we feed a flat plane to a lot of division we get these fixed theme fixed edge
[0:17] due to the first iteration of the lot of division as you can see. And one way we can randomize it is to introduce and avoid that
[0:26] that theme is to introduce a random cut and we get a more pleasing result. So let's have a look on how to achieve that with Vax.
[0:36] So let's drop a geo container and agree then by then we'll be fine. The idea is to introduce a random cut and have some procedural way to control it.
[0:48] So we're going to do a bit of a Vax exercise. I'm just going to drop these columns to four because I don't want too many divisions.
[0:58] And the first thing we're going to do is to create a column and a row attribute. So for that I'm going to drop a wrangle.
[1:08] And we're going to reference the columns and rows from these grid geometry so we can create an int called rows.
[1:18] And let's create a channel integer called rows. And we will copy this and do it for columns and call it calls.
[1:30] And let's create that and copy from here the rows. So rows, base relative reference and columns copy and paste.
[1:41] Now we will create the attribute so we can say int row. It will be equal to floor.
[1:50] I at ptnm divided by calls. This will be the row attribute. So we can naturally assign it to an attribute.
[2:02] So we can say I at row it will be equal to row. And let's have a look at that. So we look at that attributes and we do marker.
[2:12] As you can see we have 0, 1, 2, 3 and so on. So that is working. We can disable that visualization.
[2:18] And now let's do the same for the columns. In this case we will call it call and we will use the module operator in here.
[2:27] Copy this, call it call.
[2:31] Let's see if that works. Looks like it's working. So 0, 1, 2, 3. So we have the call and we have the row as you can see.
[2:46] So this can be useful for many different things. So it's always nice to know.
[2:51] So I also want to get the maximum of each attribute. In this case I only need columns. So I'm just going to set a detailed attribute.
[3:01] I want to call it max call and it will be equal to I at call and as a max. I want to set it to the max.
[3:14] And we should have a detailed attributes. So if we go in here we have a tree in the calls and here in the max call we also have tree. So that is working.
[3:23] And now let's do this in a way that is more standard let's say. So I want to select a random point on this side on this column and another random point on the life column.
[3:42] So we can do the following. We can create a natural triangle. And before that we need to sort randomly the points. So random in the point order and select the seed.
[3:55] And now we can do the following. We can read out the max.
[4:00] So int max call will be equal to detail in coming geometry or first input and max call.
[4:10] And then we can just create a variable or an array with all the points in the column zero and in the column in the last column.
[4:20] So we can do int part call ray. It will be equal to expand point group expand point group incoming geometry and at call.
[4:35] So we added the attributes. We need to pass a string in here. So at call equals to zero.
[4:40] And now we can just say we can create a group. So I at group start will be equal to I at ptnum if the point number is equal to start call.
[4:53] And we can just select the first or the first century into in the array.
[4:59] So we can actually get these copies and going here and output selection group. We can say start. And as you can see selecting that point.
[5:07] Let me see if I can increase in here.
[5:10] Sorry, it's in here the point marker size under guides. So as you can see selecting that point over there and I can change the seed and select a different point.
[5:20] And now let's do the same for the end group because we will create the shortest spot between the starting point and an end point in here and then do the random cut on the geometry.
[5:31] So let's get this one.
[5:36] And this will be the end call and expand point group call is equals to I to way and we on the last column. So we can do I to way max call.
[5:50] And we can just copy this and say group and it will be equal to zero.
[6:02] So if we check this and go to points we should have a last point and a first point and let's randomize the order.
[6:11] And that's basically done. Now we can we can find the shorter spot.
[6:20] And we can select in here the start and the end. Start and end and we get this random cut. We can possibly change the seed.
[6:32] And now we can just create a group.
[6:38] We add edges and it's also do a transfer.
[6:47] And we want to transfer the group one and release low threshold. So something like that.
[6:56] And now we also need to select the unchaired edges. So when shared edges and finally we can do so.
[7:06] So if we this solve non selected the group one and the answer and we get this random cut on the geometry.
[7:16] And now we can do lots of division. So lots of division.
[7:21] And we can play with the irregularity and reduce the iterations play with this.
[7:32] And as you can see we get a more randomized look if we play with the seed.
[7:37] We don't get that usual cut. Then probably play every tomorrow.
[7:44] These and also create a visualization. So let's do.
[7:51] I at class it will be I at premium or each cream. A different ID.
[7:58] Let's visualize that. So if we only did so let's go in here and do and remove the group one.
[8:08] So we have the flight plane and we do lots of division.
[8:13] As you can see we have these obvious seeming here. And if we apply our cut we get a more randomized look.
[8:22] And we can play with the seed. And get different results. And we can also go back and play with this sort seed.
[8:33] So that's basically then. But there's one one another another approach that I wanted to show you that might be interesting to know.
[8:42] So we basically solve our issue but there's another way that I wanted to show you that involves iterating instead of points over numbers.
[8:50] Since we just want two points but we only need two iterations. We don't need to iterate over all the points.
[8:56] It will be slightly more involved but you might learn a thing or two and we won't need the sort notes.
[9:04] So we can just select a random point without the sorting the points randomly.
[9:09] So let's create another we will still need the column I the column ID and the rows.
[9:18] So this time we will iterate over numbers and since we just want two points we can just set this to two.
[9:25] So this will only iterate twice. And we will also need this method call and we will need an expand point group so we can just copy from here.
[9:36] So we have max call and let's call these instead calls array.
[9:43] No, we want to call these groups and we will work on it on a bit.
[9:52] So the first thing we need to do is to create an array of the columns we want to iterate over.
[9:57] So that should be simple. Create a string calls array.
[10:03] And this is the only manual work we will have to do. So let's create an array and it will be with will contain the call zero.
[10:15] And the call last column. So in this case plus I to wait max call.
[10:26] So those are the columns that we will iterate over.
[10:32] So the points on those columns. And now we can create these groups array where we expand the point group and we say zero.
[10:40] And we will recall this one.
[10:44] And as the index we will use the I at LNNUM.
[10:52] So which is the each iteration which will be zero in the first iteration and one in the second.
[10:58] That way it will select first column zero and then the last column.
[11:02] And we can use the same concept to create random numbers and to set the point group.
[11:08] So for that let's create a random number first.
[11:13] So in random in this case it will be a random.
[11:19] So it will be a random of the LNNUM.
[11:25] And we will use a C parameter.
[11:29] And we can just multiply by the length of those groups of those points of that array.
[11:40] And then we need to also in it. So create an interrupt.
[11:45] And just close bracket in here.
[11:50] And we should have a random number.
[11:53] And now we can set the point group.
[11:58] So set point group.
[12:00] So we can really use the I at group syntax. We need to actually set the point group.
[12:04] This is similar to iterating over detail where we need actually to do some manual work.
[12:11] So I'm going to call it group and we need two groups.
[12:14] So I'm just going to create here an I to a and use again the LNNUM.
[12:19] So the iteration number.
[12:22] And we will set the groups from the groups array the random number that we will generate.
[12:30] And we can just say set it at the end.
[12:34] And we should have those groups.
[12:36] So let's see group zero group one.
[12:38] And we don't have group one.
[12:40] Let's just create the seed.
[12:42] And it's selecting the same.
[12:46] It's selecting the same in the same column.
[12:51] Why is that?
[12:53] So sorry, I call this calls it call not calls.
[12:57] Now we're selecting.
[12:58] And as you can see selecting randomly one point on each side.
[13:01] And we don't need the sort node or.
[13:05] A lot of iterations to solve this problem.
[13:08] Now we can just do the same in here.
[13:10] Unfortunately, I didn't find a way to rename the groups properly.
[13:13] So we start an end.
[13:15] Maybe if we use the dictionary, but that will just be more work.
[13:19] And we don't need to do that.
[13:21] So let's just say group zero and group one.
[13:23] And do this.
[13:24] And we can create the linear switch.
[13:30] And if we select the first input and I will transfer it.
[13:33] And we do this all.
[13:35] We get the random cut.
[13:37] And finally, we can create the lots of division.
[13:40] And let's play here with the seed.
[13:44] So and we start to get a randomized result.
[13:48] So a lot of work, but I hope you have learned a thing or two.
[13:52] It's always interesting how you can apply these run over numbers.
[13:56] Maybe it was not the best approach, but I found it's interesting
[14:01] by using this element as a seed and as a iterator to create multiple variables, let's say,
[14:09] for iteration.
[14:11] But this is also valid.
[14:13] We just duplicated the code a bit in here.
[14:16] So we use the same commands over and over.
[14:21] So I found this one to be more efficient since we're just running over two iterations.
[14:27] So as always, you can grab the files on my Patreon alongside with exclusive tutorials on there.
[14:32] Hours of exclusive step by step tutorials.
[14:34] I also have some courses in there if you want to check it out.
[14:38] And I'll do project files from my videos.
[14:40] So thank you for watching and let me know what you think in the comments.
[14:43] See you.



---

## Captured Frames

- [0:15] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_000.jpg
- [2:12] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_001.jpg
- [4:05] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_002.jpg
- [5:40] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_003.jpg
- [7:00] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_004.jpg
- [10:20] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_005.jpg
- [13:20] tutorials/frames/vex-quick-tips-2-iterating-over-numbers/frame_006.jpg

---

## Structured Notes

### Core Technique
Break up the visible, repeating seam that **Lots of Division** creates on a flat grid (a fixed diagonal from its first-iteration cut) by introducing a random cut path between two edge points via **Find Shortest Path**, then compares two ways of picking those random start/end points: sorting all points randomly, versus a cheaper "for-each over numbers" (only 2 iterations) approach that avoids sorting entirely.

### Summary
By default, feeding a flat plane straight into Lots of Division produces a visually obvious fixed seam from its first subdivision iteration. The fix is to cut a random path across the grid first with Find Shortest Path, then subdivide. The tutorial builds row/column attributes on a Grid (`row = floor(ptnum/cols)`, `col = ptnum % cols`, with `max_col` stored as a detail attribute), then demonstrates two ways to pick one random point in column 0 and one in the last column to serve as the cut's start/end: **Approach 1 (sort-based)** — randomly sort all points (Sort node, random order + seed), use `expandpointgroup()` on `col==0` and `col==max_col` to get each column's point array, then group the first point of each shuffled array as `start`/`end`; feed those into Find Shortest Path to get a random edge path, group it, Group Transfer it back, then run Lots of Division for a randomized, seam-free result. **Approach 2 (for-each-over-numbers, no sort needed)** — since only 2 points are actually needed (not a full point-order shuffle), iterate a For-Each over just 2 numbers; build a manual `cols_array` (or "groups" array) containing the string names of column-0 and last-column groups, index into it with `@iteration` (0 first pass, 1 second pass) via `expandpointgroup()`, generate a random index with `int(random(@iteration + seed) * len(array))`, and manually `setpointgroup()` at each iteration to build `group0`/`group1` (Houdini doesn't let you rename iterated groups automatically, so a Switch node is used afterward to route between them) — this selects one random point per iteration without any sort node or full-point-order randomization, which is more efficient since only 2 iterations are needed instead of iterating over every point.

### Key Steps
1. On a Grid (subdivided into columns/rows), build `row` and `col` int attributes via a wrangle: `row = floor(ptnum / cols)`, `col = ptnum % cols` — plus a detail attribute `max_col` via `int max_col = @col; ... setdetailattrib(..., "max", ...)` (max reduction) for later reference.
2. **Approach 1 — sort-based:** randomly reorder all points with a **Sort** node (random order, seed), use `expandpointgroup(0, "@col=0")` and `expandpointgroup(0, "@col=" + itoa(max_col))` to get each column's point array (now in randomized order thanks to the Sort), and group the first entry of each as `start`/`end`.
3. Feed the `start`/`end` groups into **Find Shortest Path** to compute a random path between the two columns.
4. Group the resulting path edges, **Group Transfer** them back onto the original geometry, then feed into **Lots of Division** — the random cut breaks up the seam, and changing the seed changes the whole pattern.
5. **Approach 2 — for-each over numbers (no sort):** set a **For-Each Number** loop to iterate exactly 2 times (since only 2 points are needed — one per side).
6. Manually build a string array `cols_array` (or "groups") containing the two group names — column 0 and the last column (`"col=0"`, `"col=" + itoa(max_col)`) — this is the one piece of manual setup required.
7. Inside the loop, use `expandpointgroup()` indexed by `@iteration` (0 on the first pass, 1 on the second) to fetch the correct column's point array each iteration.
8. Generate a random index into that array with `int(random(@iteration + seed_param) * len(array))`, then manually build and assign a group name per iteration (e.g. `group0`, `group1`) via `setpointgroup()`, since Houdini doesn't support renaming iterated for-each groups automatically.
9. After the loop, use a **Switch** node to select between the `group0`/`group1` outputs (workaround for the manual-rename limitation), feed the two points into Find Shortest Path as before, then Lots of Division — same visual result, but without ever sorting or touching every point, since only 2 iterations run instead of N.
10. Optionally visualize with `@class = @primnum` (or `@Cd` via primitive) to distinguish which points/edges belong to which side, and compare frame-rate/complexity between the sort-based and for-each-over-numbers approaches.

### Houdini Nodes / VEX / Settings
Grid, point wrangle (`floor()`, `%` modulo, `int`, detail-attribute max reduction for `max_col`), Sort (random order + seed), `expandpointgroup()`, group creation via point-number comparison, Find Shortest Path (cost-free path search between grouped start/end points), Group, Group Transfer, Lots of Division (irregularity, iterations), For-Each Number (2 iterations), `random()`, `len()`, `setpointgroup()`, `itoa()`, Switch node (group-name workaround).

### Difficulty
Intermediate (the sort-based version is approachable; the for-each-over-numbers alternative requires understanding `expandpointgroup()` indexing by iteration and manual group-array bookkeeping).

### Houdini Version
Not specified.

### Tags
vex, quick-tips, for-each, lots-of-division, random-cut, find-shortest-path, expand-point-group

---

## Related Tutorials
- [Vex quick tips | Overhang look with channel ramps](vex-quick-tips-overhang-look-with-channel-ramps.md) — same quick-tips series, focused on quaternion-based normal rotation instead of for-each/group patterns.
- [Vex Quick Tips #4 - Pineapple Crown](vex-quick-tips-4---pineapple-crown.md) — same series, applies similar attribute-manipulation VEX patterns to a leaf-placement problem.
- [Procedural UV's In Houdini](procedural-uvs-in-houdini.md) — shares the Find Shortest Path technique used here, applied there to seam-snapping for UV flattening.
