---
title: Direct vs Procedural in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Quj03TwHAN4
author: cgside
ingested: 2026-07-13
houdini_version: "20"
tags: [modeling, vex, uv, procedural, hard-surface, tips, cops, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/direct-vs-procedural-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Direct vs Procedural in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Quj03TwHAN4)
**Author:** cgside
**Duration:** 17m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to show you a few
[0:04] examples comparing procedural versus direct approach when it comes to modeling
[0:10] UVs, group selection and so on. So this will be a bit all over the place with
[0:15] mixed examples but hopefully you'll get away with a few techniques. So let's
[0:19] get into it. I want to start with this example where I shared this file before
[0:26] but when I release that video about the sushi texture but I wanted to go
[0:34] through the modeling stage. So I start with the box right and now I want to
[0:39] select the top and bottom primitives because I want to transform the top. In
[0:43] this case I don't need the bottom but I just keep it there so I can if I need
[0:48] to change the bottom face. So as you can see I have the bottom and top face and
[0:53] this could be easily done with the groups up. In this case we would need to
[0:58] write so now it makes sense to probably select them using some procedural
[1:05] approach other than the groups up. So this is really simple we start with the
[1:09] box and then to select the top and bottom primitives we run a wrangle on
[1:13] primitives and we just create a sign on the position.why since this is
[1:18] centered around the center around the origin. So we can just say the sign of
[1:25] p.y it will be positive one on the top prim and negative one on the bottom. So
[1:32] we can just assign to the top the sign is equal to 1 and for the bottom equal
[1:37] equal to minus 1. Simple enough right now we can transform the top primitives
[1:41] for example to create this shape. Now I want to select these edges as you can
[1:45] see. So this is not easily done and I shared a similar technique before where
[1:51] you can just select we can run these over vertices. In this case as you can see
[1:58] I'm using the top and bottom primitives constraining this wrangle to the top
[2:03] and bottom primitives this way I can just select every other vertex on those
[2:07] primitives as you can see. So the only tool out of four and now I can convert
[2:14] that selection from vertex to edges and I get these that I can later create a
[2:21] bevel and as you can see this bevel as in this case I'm not using that. So let
[2:30] me see in these that we put to just load. Let's see the p scale. So let's see we
[2:38] have two and 1.5 and I'm running that on points. So it should. So it should. Oh
[2:49] of course I'm not scaling by attribute as you can see. So you can use these
[2:53] attributes to just load to default value to have a different value based on a
[2:59] group for example or a attribute. As you can see I'm targeting the top
[3:04] prim in the group and I can change the value of the bevel there but at the
[3:09] bottom we're using this default value I can set a default value for all the
[3:13] other edges. As you can see I can set these two and these one to 1.25 but in
[3:22] this case I'm not gonna I'm not gonna scale by attribute I'm just gonna leave it
[3:26] default. Then I promote the edges to this point group and in this case I'm just
[3:33] selecting the front and back because I will need it and as you can see I'm
[3:37] selecting the Z axis in these keep by normals and also including the normals
[3:41] matching the opposite opposite direction. As you can see I can select both. Then
[3:46] the other trick I wanted to show you in here is this poly-ex route. As you can
[3:50] see I'm do if I disable in here. This one I can do an inset but as you can see
[3:59] at some point it will merge all the points that's how inset works right but
[4:05] if I set this to where I add it so 0.05 and I come to spine control and I play
[4:12] with this thickness ramp as you can see I can still have that inset or I can
[4:18] set it to zero and I don't necessarily merge all the points with the default
[4:27] behavior of the inset as you can see. Of course the inset is more precise when
[4:32] keeping the length between the boundaries but in this case using the
[4:39] thickness ramp gave me the best result as you can see and I can group the
[4:43] unshared and in here I can as you can see I'm grouping the unshared but I'm
[4:49] creating these boundary groups which means that I will have two groups of
[4:53] the unshared so if I go to points I have this unshared 0 and unshared 1 for both
[4:57] groups as you can see. Now I can promote those two edges and use a poly bridge in
[5:03] this case so by bridging from from these unshared 0 to unshared 1 and I can have
[5:10] these results so always useful babbling and a tributtler. So I asked before I
[5:18] found about this thickness scale I was doing something different so basically
[5:23] I just inset it a little bit as you can see just a tiny bit then I group the
[5:31] boundary of the extrude front so I'm outputting these extrude front in here I
[5:35] group the boundary of that group then I created some uniform normals on the
[5:41] center points there's no really point of explaining this but basically we're
[5:46] creating these normals then I'm copying the normals to the other points of
[5:51] the pebble and just picking so basically the same result but as you can see
[5:56] is not necessarily very accurate so just something to keep in mind. Now let's
[6:02] move to these cross example so the bit I wanted to show you in here is how I
[6:08] did the selection for the UV seams but I believe that's still some value on
[6:13] now I created this so we started with the tube then we're doing a clip to
[6:21] select to have these only in one axis then I'm creating a group of the
[6:29] unshared with again this create boundary groups and then I can promote the one
[6:35] of the boundaries in this case along the positive z to edges and then in order
[6:40] to create these results instead of me placing like sticks poly extrudes for
[6:45] the extrude the inset x-rude inset I'm just doing in feedback loop as you can
[6:50] see so fetch feedback and by counting this case to two I can place more and
[6:56] inside I'm just doing let me reset this I'm doing collecting that boundary so if
[7:04] you can see in here and I'm extruding along the point normal by this amount and
[7:09] outputting again the boundary but as you can see I'm not preserving the
[7:13] groups because I don't want to have two groups after this because I already
[7:18] started with this one and when it goes to the next iteration it will accumulate
[7:22] so I'm just taking the preserve groups then I'm doing again another
[7:26] extrusion and saving the same boundary and don't preserve groups and this way I
[7:31] can do these recursive extrusions can you say it's a recursive extrusion I
[7:37] don't know so you get this result polyfilling mirroring and we get something
[7:43] close to work rassa flattening the bottom with this flatten you know they
[7:48] either I believe in Odinit 20 and then I did a simple sculpt just to move the
[7:55] geometry a bit with I believe I did it with with the move brush and then I
[8:02] subdivide and I already get something closer and then another sculpt to
[8:07] refine the shape just smooth and maybe create some creases in here and that's
[8:13] basically so that was not very important the important thing is on how I did
[8:18] these UVs so the first thing you have to keep in mind is you need to think about
[8:24] where the sims should go so the least amount of sims but also that you can get a
[8:28] clean UV map like this one can show you something like this so it makes
[8:34] sense for me to have these UVs running perfectly aligned and for that I'm
[8:40] gonna select these themes in here but I don't want to go around and select all
[8:45] the themes manually so I'm gonna do a very small selection so I can actually
[8:49] demo in here so I'm gonna create a group I don't need a group I can just go in
[8:54] here to select and select edges I know I need this this one this one this one
[8:59] and also a sim long ear and I need that one or instead this one and this one
[9:08] and also this one so something like this I can create a group and let me move
[9:16] it and now we have the group of the edges and I can just run this to a group
[9:21] fine pet so that's the magic note and by default it will be on primitive so
[9:27] I'm gonna select this group 13 and groups 13 as base group and I'm gonna do
[9:33] loops or rings and as you can see is already doing something but not in here
[9:38] so I'm just gonna in this case set it to to extend to edge now believe I also
[9:46] do oh I did close pad so close pad and don't avoid self intersections and we
[9:53] get the seams that we can as you can see I have the same result in here and I can
[9:58] do a UV flatten on the seams and also rectify it because if I don't rectify
[10:03] it I get the UVs all over the place as you can see and when I rectify I get
[10:07] this clean result so yeah that's how I did the UVs for the Crasa so in the
[10:16] in this next example I wanted to show you something you can translate from
[10:21] direct modeling in order you need to procedure modeling so we have this grid
[10:24] and I selected a boundary so not in direct direct modeling I can come in here and
[10:30] select points so let me actually get this point and if I press age and I light a
[10:36] point I can get the boundary so or if I select shift age H I can add to it and
[10:42] the same happens if I select the outside so if I do see shift age I get the
[10:49] extended selection as you can see this is pretty useful and I was wondering how
[10:52] you can create this with we procedurally I mean so we have the boundary now
[11:00] we can select procedurally an inside point that's what I'm doing in here so
[11:06] basically I'm doing these over detail and expanding the point group so getting
[11:11] all the points of that boundary and then it rating over them then I just
[11:15] append to to an array the position of that point and then doing the average I
[11:20] can measure then I can compute the nearest points to the average positions of
[11:25] those points and I set the point group to start so the average point position it
[11:29] will be or the average point it will be this one then I can do a fill boundary
[11:34] which means I name it to fill then I input the start point which is this one
[11:42] and the boundary which is this one and I flood fill to connect a geometry as you
[11:47] can see if I just do a simple group expand it will be something like this but I
[11:51] want to flood fill and then I can select a collision group to the boundary so
[11:55] this way I flood fill that selection me making the same behavior then I can
[11:59] group promote it to Prims for example and include elements entirely
[12:04] containing the original group and finally I can do for example an edge
[12:08] selection of the boundary as you can see with this group from attribute
[12:13] boundary so as you can see in here and as you can see this is different from
[12:18] having this point selection and promoting to edges as you can see it will
[12:22] include these two edges which I don't want and I don't have in here hopefully
[12:26] it's watchable to do recording or compression on YouTube but I don't have
[12:32] these edges in here as I have in here with this group promote and you can try as
[12:36] much as you want with this group promote it will never behave the same way of
[12:41] having this doing this setup so you get a lot of things from this from the
[12:46] group fill to the primitive promotion and the boundary so yeah that was just a
[12:51] quick example of translating from direct modeling to procedural selections let's
[12:58] say now this one is really simple basically I've done this spray bottle for a
[13:04] tutorial that I never finished but there's some things I wanted to share and the
[13:09] main idea is you do procedural if you can but if you can't and it just to too
[13:14] much you go direct modeling and when I say that for example in order to create
[13:20] this shape at the top of the spray can I could have done this with ramps and
[13:25] whatnot with Vax but it's just so simple to drop a curve and do revolve and you're
[13:33] basically done and you have UVs and so on but for example in here I have these
[13:38] two to create the main shape of the can and I filled the end caps and by the
[13:46] thought they will be end gone so I can easily select them with this group
[13:49] expression by getting these five sides or greater so basically a primitive
[13:57] that has a lot of vertices and then I can poly through that part the Wapali
[14:03] Bevel and that's my main shape done with a few subdivisions and yeah so an
[14:08] example of going more direct with the is drawing off the curve it's still
[14:12] kind of procedural but you know what I mean so for example in here I have this
[14:18] shaping that I want to do this inflation and we can do that easily so
[14:25] having the shape we can create a mask in Vax very easily by just computing the
[14:30] length of the vector in this case the position and we get something like this
[14:34] that we can later normalize with these actual normalize floats in this case I
[14:38] inverted from one to zero and then I we can do just a soft peak so as you can
[14:43] see I can input that mask on the soft peak and just play with this case it will
[14:48] be too much so you can increase it or decrease it so yeah that's basically it I
[14:55] have something else in here so yeah the other bit I wanted to show you is that
[15:02] you don't have you don't have to select the seams procedurally so it's totally
[15:08] okay to come in here and select the seams manually as you can see for this
[15:13] shape I wanted to select the seams manually there's no problem doing that since
[15:18] you be is just unless you're doing a generator or something like that there's
[15:22] really no point of selecting all the seams manually so for example in here I
[15:27] have this shape of the cap and selecting this procedurally doesn't make any
[15:34] sense or I don't even know if it's possible so I just selected them manually
[15:38] and fit it to a UV flatten and there you go so there's one last thing I wanted
[15:44] to show you and that when you try I have an image reward in here so an
[15:51] image would for each piece and I can place them but if I want to to send these
[15:58] to cops I can't really arrest the rises ring attribute to identify which part
[16:03] I want to texture and create masks so I can place an enumerate and if I look at
[16:11] that index so doesn't mean much I need to do it based on name and enumerate
[16:15] pieces and now I get as you can see an index from 0 to 3 but if you have when
[16:23] you look at the UVs we have some empty space and since this one is zero this
[16:28] one will also resturize as zero so we need to upset this by one we could
[16:32] easily do that with a wrangle but instead of placing the enumerate and what
[16:36] not I just do it with this with this attribute wrangle running on primitive so
[16:41] basically I'm getting all the values of the name attribute so based can cap and
[16:47] so on and then I can use the find function to create an index so I find the
[16:55] name on the unique valves and just increase one this way I can have a
[16:59] starting value from 1 to 4 as you can see and I name it in the same way so
[17:04] when I resurrect these in cops this one will be one and the background will be
[17:08] zero so yeah guys that's basically the tricks I wanted to show you today so a
[17:13] bit all over the place but hopefully you'll got you got something out of this
[17:16] as always you can grab all these files on my patron I'm gonna upload this
[17:20] entire scene there and you can also find exclusive tutorials and many many
[17:25] hours of exclusive tutorials and courses on my patron shop alongside Weave HDAs
[17:29] so yeah have a night on there and other than that thank you for watching and
[17:35] please let me know your feedback below thank you



---

## Captured Frames

- [0:40] tutorials/frames/direct-vs-procedural-in-houdini/frame_000.jpg
- [3:50] tutorials/frames/direct-vs-procedural-in-houdini/frame_001.jpg
- [6:10] tutorials/frames/direct-vs-procedural-in-houdini/frame_002.jpg
- [9:20] tutorials/frames/direct-vs-procedural-in-houdini/frame_003.jpg
- [13:20] tutorials/frames/direct-vs-procedural-in-houdini/frame_004.jpg
- [15:50] tutorials/frames/direct-vs-procedural-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
A wide-ranging comparison of direct/interactive modeling vs. procedural (VEX/group-based) approaches for selection, extrusion, UV seam-picking, and boundary/topology operations, using several real production examples (a sushi box, a "Crassa" creature-like shape, a spray bottle, and an image-reward piece for COPs).

### Summary
Walks through when procedural selection beats manual grouping and vice versa. Sign-of-position wrangles replace manual top/bottom group creation on a symmetric box; vertex-index-modulo wrangles select every-other edge for beveling; attribute-driven bevel widths let one Polybevel vary per group instead of needing multiple nodes; a Poly Extrude "thickness ramp" trick (instead of plain Inset) avoids merging all points at high inset values while still producing a controllable inset-like result; boundary groups + Poly Bridge stitch unshared edges from two separate extrude outputs. A feedback-loop (Fetch) recursive extrusion technique repeatedly extrudes+insets along point normals without stacking duplicate Poly Extrude nodes, careful to disable "preserve groups" each iteration to avoid group accumulation. For UV seams, a small manual edge-loop selection is expanded via **Group Fill Pattern**'s Loops/Rings mode (extend to edge, close path, no self-intersection) to auto-generate full seam loops, then UV Flatten + Rectify cleans the result. A generalizable direct-to-procedural translation shows how manual point selection tools (H = select boundary loop, Shift+H = extend) can be replicated procedurally: average the boundary point positions, find the nearest point to that average as a flood-fill seed, then use **Fill Boundary** (name "fill", start point, boundary group) to flood-fill the interior — importantly different (and more correct) than simply Group Promoting a point selection to edges, which can wrongly include extra boundary edges. The video's philosophy: default to procedural where practical, but drop to direct/manual modeling (e.g. draw-curve + Revolve for a spray-can cap) when procedural would be needlessly complex — manual UV seam selection is also explicitly endorsed as fine for one-off, non-generator assets. Finally, for sending piece-based geometry to COPs texturing, **Enumerate** by name (not raw primitive index) generates a clean per-piece index, then a wrangle using `find()` against the array of unique name values remaps indices to start at 1 (not 0) so the COPs background doesn't collide with a legitimately-indexed piece.

### Key Steps
1. **Sign-based top/bottom selection:** on a box centered at the origin, run a primitive wrangle: `i@top = sign(@P.y) == 1; i@bottom = sign(@P.y) == -1` (conceptually) to group top/bottom primitives without manual Group SOPs.
2. **Every-other-vertex selection for bevel:** run a vertex wrangle constrained to the top/bottom prim groups, selecting every 4th (or Nth) vertex via a modulo check on vertex/point index, then Vertex→Edge group promotion, feeding a Polybevel.
3. **Attribute-driven bevel width:** instead of scaling by a constant, drive Polybevel's width from a per-group/per-point float attribute (`pscale`-like) so different edge groups (e.g. top prim vs. rest) get different bevel amounts from one node, with a default fallback value for ungrouped edges.
4. **Thickness-ramp inset alternative:** on a Poly Extrude, instead of a large Inset value (which eventually merges all points together), enable "Spine Control" and shape the **Thickness Ramp** to get a controllable inset-like taper without point-merging; less geometrically precise than a real Inset but visually sufficient.
5. **Boundary group + Poly Bridge:** Group the unshared points with "Create Boundary Groups" enabled (produces `unshared0`/`unshared1` sub-groups per boundary), promote each to edges, then Poly Bridge between the two boundary edge groups to stitch them together.
6. **Recursive extrusion via feedback loop:** instead of stacking many Poly Extrude+Inset node pairs, build a **Fetch/feedback loop** (set iteration count, e.g. 2) that on each pass: extrudes along point normal by an amount, insets, and outputs a new boundary group — critically disabling "preserve groups" on each pass so groups don't accumulate duplicate boundary sets across iterations.
7. **UV seam auto-completion via Group Fill Pattern:** manually select just a few key edges (loop-adjacent) forming a partial seam pattern, put them in a group, then run **Group Fill Pattern** (base group = your selection, mode = Loops/Rings, "extend to edge", "close path", disable "avoid self intersections") to automatically extend the pattern into full topological seam loops; finish with UV Flatten on the seam group + **Rectify** (needed or UVs come out skewed/misaligned).
8. **Direct→procedural translation for interior flood-fill selection:** replicate the "select boundary (H), then flood-fill interior" manual workflow procedurally: Group Expand a boundary point group over `detail` scope, average all boundary point positions, find the nearest actual point to that average to use as a flood-fill seed, then use **Fill Boundary** ("fill" name, start point group, boundary group) to flood the interior; a plain Group Expand alone does NOT reproduce this correctly. Group Promote that fill selection to primitives with "include elements entirely containing the original group", then take an edge selection **from the boundary group's attribute** rather than promoting the point group directly to edges — the direct point→edge promotion incorrectly includes extra edges that the attribute-boundary-based group does not.
9. **When to go direct instead of procedural:** for a spray-can cap shape, a hand-drawn curve + Revolve is faster and gives clean UVs "for free," versus building the same profile with ramps/VEX; for end caps, Group Expression selecting primitives with "5 sides or greater" isolates n-gon caps cheaply for a Poly Bevel finishing pass.
10. **VEX inflation mask:** compute `length(@P)` (vector length of position) as a radial falloff, normalize/invert it (Fit/Normalize Float, 1→0), and feed that mask into a **Soft Peak** node's mask input to control inflation intensity per-region.
11. **Manual UV seam selection is fine:** for one-off, non-procedurally-generated shapes (e.g. a cap), manually selecting seams and feeding UV Flatten is explicitly endorsed — there's no benefit to forcing a procedural seam-selection unless building a reusable generator.
12. **Per-piece index for COPs texturing:** use **Enumerate** driven by the `name` attribute (not raw primitive number) to get a stable per-piece index; since index 0 collides with the COPs background (also rasterized as 0), remap with an Attribute Wrangle on primitives that does `i@index = find(unique_name_values[], s@name) + 1` (conceptually), producing indices starting at 1 so the background stays distinguishable at index 0.

### Houdini Nodes / VEX / Settings
Nodes: Box, Attribute Wrangle (primitives — sign(@P.y) grouping; vertices — modulo-based every-Nth selection; primitives — find()-based re-indexing), Group Promote (point↔edge, vertex↔edge, with "include only elements on boundary" caveats), Polybevel (attribute-driven width), Poly Extrude (Spine Control, Thickness Ramp as an inset alternative), Group (unshared points, Create Boundary Groups → unshared0/unshared1), Poly Bridge, Fetch/feedback loop (recursive extrude+inset, preserve-groups toggle), Group Fill Pattern (Loops/Rings mode, extend to edge, close path, avoid-self-intersections), UV Flatten + Rectify, Draw Curve + Revolve, Group Expression (n-gon/"5 sides or greater" selection), Group Expand (over detail scope), Fill Boundary (name, start point, boundary group), length()/normalize/Fit Float, Soft Peak (mask input), Enumerate (by name attribute), find() VEX function against unique attribute values.

### Difficulty
Intermediate/Advanced — a broad "greatest hits" of production-tested selection and topology tricks; requires solid VEX and group/attribute fundamentals to follow each mini-example.

### Houdini Version
20 (mentions "Rectify... I believe in Odini 20"; UI matches Houdini 20-era look).

### Tags
#modeling #vex #uv #procedural #hard-surface #tips #cops #intermediate

---

## Related Tutorials
Cross-link with direct-and-procedural-modeling-in-houdini.md (same author, overlapping VEX-cleanup philosophy) and any cgside COPs/texturing tutorials once extracted from this batch.
