---
title: week 02   03   starting the guided sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=9qkYzPC9IKM
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H17.5+"
tags: [rbd, guided-sim, bullet, constraints, cables, hard-constraints, active-attribute, bridge, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/week-02-03-starting-the-guided-sim-v1-1080p/
frame_count: 4
---

# week 02   03   starting the guided sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=9qkYzPC9IKM)
**Author:** The VFX School Archive
**Duration:** 6m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So let's give these blocks and attributes. So they need, well, that's given us a name attribute, which looks like we've got the visualizer left turned on there. Okay, so each block will have a separate name. Let's connect them together. So I'm not going to pack this yet. Let's give this a proper name. So we'll call it main cable. Okay, and let's drop a, a, b, d constraints from rules. So into the render geometry and the proxy geometry together. Okay, and again, I want surface points here. So you can see we're connecting up the edges between them. Just obviously important that they don't, we don't have constraints between the, the cables like that. So just by default, like that is fine. And then I will add the constraints properties. There we go. Okay, and for this, I'm not going to use softening, I'm going to use, I found that hard constraints work better for me. When I want something really rigid and kind of stiff looking, like cables, and also we don't need plasticity. So obviously with the soft constraints, it's nice to have their plasticity for, you know, metal. But in this case, it's a cable and it's very stiff. It's not going to move a lot. So I'm going to stick with hard constraints for this, you know, you experiment with it too. I often experiment between either hard or soft constraints, because they can be used for the same thing. But I'm going to stick with hard constraints in this case. Okay, let's drop a configure. So I'll be the configure. So this will pack everything up, right? It's to simulate. Okay. And again, we need to, similar to what we did previously, we need to set some of these pieces to be inactive. So that, you know, it's like the cables are being held up by the, we have towers at the end of the bridge, obviously, we don't just want everything to fall. So we'll do that just like before. We'll kind of group it. But this time, it won't be anime to be much more simple. So let's just template that. Make a box. I'll just make it big and then move it across in either direction. Okay. So just move that across. That way until it's just grabbing the last kind of piece. So we'll do 19 and then do another transform and just do it at minus 19 like that. Merge these together. And then plug it into the last input of this configure. And then we will set so the active, not that sorry, the active attribute to use bound. And then let's visualize that active. There we go. Okay. So this needs to be off. I think there we go. Yeah. So anything in the box in the bound is not active. And that by default will set everything else to be active. Okay. So that's all we need to do in there. I believe. Let's drop our ABD bullet solver. Connect up constraints, main geometry and the proxy geometry. Let's visualize this. This should simulate really quickly as we've got. You know, it's quite simple geometry. Let's just going to turn this off just in case they shouldn't stretch or you know, but I'll just get rid of that so we don't want any of these constraints to break. Just press play and we'll see them sag down a little bit. Okay. So what we're going to do with this is use the previous simulation to guide this simulation. So if you go there to the last input you can see we've got this guided sim, which is something that came new into Houdini in 17 I think or 17.5 I'm not too sure. But basically the idea is that you use an animation to guide the simulation of another bullet simulation. Right. So we're going to grab. So from here this, this bridge sim. So I'll just copy that. So I don't have to go looking for it. Come in here and then control V. There we go. And then that grabs that simulation and plug it into the last input. Okay. And then let's come in here. Visualize. So if we turn on show, where are we? This is grayed out because we haven't got it turned on yet. So go to guided simulation, turn on use guides. Go back to visualize and show guided. Okay. So that's turned blue because everything's been guided now. And that should work as it is. If we template that so we can see the bridge and just start the simulation from there. You should see the cable is kind of following along. There we go. Okay. So it's almost like, well it will internally it is that these these pieces are constrained to these pieces. Right. So you can see it's kind of following, following, following, sorry, I can't speak following along. Up to a point. So you know, depending on the on what you set up in here, if this kind of pulls away too quickly or the movement is too fast then that kind of relationship between the two should break. So obviously this here is a problem. I don't want this happening. Okay. I want the constraints. These constraints not to break. And when the bridge starts to fall, I want this to be released from that. So it's like the cables which we're going to be simulating later coming down. It's like when they break, then these cables, you will see them kind of release and pop up a little bit. Okay. So we'll continue with that in the next video.

**Frame:** tutorials\frames\week-02-03-starting-the-guided-sim-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Horizontal cable bullet sim with Guided Simulation: name attribute on cable blocks → Constraints From Rules (hard constraints) → RBD Configure → ABD Bullet Solver; plug Week 1 bridge sim as Guide input; enable Use Guides. Inactive attribute set via two box bounds at X=±19 (tower anchor points).

### Summary
6m47s VFX School Archive module. Part of Manhattan Bridge Destruction Week 2. Sets up horizontal cable simulation with Bullet + Guided Sim workflow. Creates name attributes, hard constraints between cable blocks (no plasticity, stiff behavior), RBD Configure with inactive regions at bridge towers (boxes at ±19 X). ABD Bullet Solver with Guided Simulation tab: imports Week 1 bridge simulation as guide geometry. Guided pieces follow the animation until release conditions are met (angular/linear thresholds). Constraint breaking when bridge falls too fast to be fixed in next lesson.

### Key Steps
1. **Name attribute** — each cable block gets unique name (for constraint creation between adjacent pieces)
2. **Constraints From Rules** — surface points; connects edges between adjacent cable blocks; avoid inter-cable constraints; add Constraint Properties node
3. **Hard constraints** (not soft/plasticity) — stiff, rigid behavior; best for cables; soft constraints better for deforming metal
4. **RBD Configure SOP** — packs everything for bullet simulation
5. **Inactive regions** (tower anchor points):
   - Two transform boxes at X=+19 and X=−19 → merge → plug into last input of RBD Configure
   - Active attribute = use bounds → pieces inside boxes are inactive (held in place by towers)
6. **ABD Bullet Solver** — connect: constraints, main geometry, proxy geometry
7. **Guided Simulation** (Bullet Solver → last input):
   - Guided Sim tab → check **Use Guides**
   - Visualize tab → **Show Guided** (highlights guided pieces in blue)
   - Guide geometry = Week 1 bridge simulation (object merge/copy, plug into last solver input)
   - Guided pieces follow the animation internally constrained to guide
   - Guide release controlled by angular + linear thresholds in Guided Sim settings

### Houdini Nodes / VEX / Settings
- Name attribute (SOP) — unique per cable block
- **Constraints From Rules** — surface points mode, constraint properties node
- **Hard Constraints** — stiff, no plasticity; use for cables vs soft constraints for deforming metal
- **RBD Configure SOP** — packs + prepares geo; last input = active bounds
- Two box SOPs (X=±19) → Merge → last input → active=bounds → inactive anchor points
- **ABD Bullet Solver** — inputs: constraints, main geo, proxy geo, guide geo
- Guided Sim tab → **Use Guides** (introduced in H17/17.5)
- Visualize tab → **Show Guided** (blue = guided pieces)
- Guide Release Thresholds: angular threshold + linear threshold

### Difficulty
Intermediate

### Houdini Version
H17.5+

### Tags
[rbd, guided-sim, bullet, constraints, cables, hard-constraints, active-attribute, bridge, intermediate]

---

## Related Tutorials
- week-02-04-finishing-the-horizontal-cable-sim-v1-1080p.md (completion: strength attr, weak group, air resistance, cache)
- week-01-11-rbd-configure-v1-1080p.md (RBD Configure setup in Week 1)
- week-02-01-intro-v1-1080p.md (week 2 overview)
