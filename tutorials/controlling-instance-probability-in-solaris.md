---
title: Controlling instance probability in Solaris
source: YouTube
url: https://www.youtube.com/watch?v=OWMKqhVaFF8
author: cgside
ingested: 2026-07-13
houdini_version: "H19.5+ (Solaris)"
tags: [solaris, instancing, scattering, attributes, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/controlling-instance-probability-in-solaris/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Controlling instance probability in Solaris

**Source:** [YouTube](https://www.youtube.com/watch?v=OWMKqhVaFF8)
**Author:** cgside
**Duration:** 2m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] I have everyone and welcome back. In this quick tip I'm going to show you how you can have control over your instances in Solaris.
[0:08] So as you can see I have these color trees just as an example.
[0:15] And by default the InstaSare in Solaris is using a random distribution. We can change the seed but that's about it.
[0:23] We also have the index but it's not very useful by itself and the option we are looking for is index attribute.
[0:33] So we need to create that attribute inside the InstaSare but also keep some randomization.
[0:40] Let's use the attribute randomize, change the name to probability, you can emit anything you want and change the distribution to custom discrete.
[0:52] Now here you need to enter the amount of objects you have in this case I only have three.
[0:58] Next you want to give it an index starting from zero.
[1:03] Let's copy the name of the attribute and paste it in the InstaSare index attribute field.
[1:10] As you can see we have no change. We can check the warning reporting that didn't find any attribute named probability and it's using the index zero or red trees.
[1:23] The problem is that the attribute randomize is outputting float values and we need integers for the index attribute.
[1:33] So that's easy to solve just use an attribute cast and we can convert it to an integer.
[1:40] And now we can control the amount of each tree or the probability of a particular instance.
[1:46] So yeah as you can see it's quite easy to set it up but you have to know the logic and step required.
[1:54] Hopefully this can help you and as I'm working on this project I might be sharing a few tips.
[2:00] Check out my patron and Gumroad if you feel like supporting the channel and see you in the next one.



---

## Captured Frames

- [0:52] tutorials/frames/controlling-instance-probability-in-solaris/frame_000.jpg
- [1:10] tutorials/frames/controlling-instance-probability-in-solaris/frame_001.jpg
- [1:40] tutorials/frames/controlling-instance-probability-in-solaris/frame_002.jpg
- [1:46] tutorials/frames/controlling-instance-probability-in-solaris/frame_003.jpg

---

## Structured Notes

### Core Technique
Controls the relative probability of each prototype in a Solaris Instancer (instead of pure random distribution) by building a custom integer index attribute with Attribute Randomize's Custom Discrete distribution mode, wired into the Instancer's Prototype Index Attribute field.

### Summary
A short, focused quick-tip: by default, Solaris's Instancer only offers a random distribution (with a Seed) across prototypes, plus an Index field that isn't directly useful for weighted control on its own — the actual mechanism needed is the **Prototype Index Attribute** field. To drive it, build an **Attribute Randomize** node with the attribute renamed to something identifiable (e.g. `probability`), distribution set to **Custom Discrete**, and a table populated with one entry per prototype (starting index at 0) — each entry can be given its own relative weight. The first attempt fails silently with a console warning ("didn't find attribute named probability," everything falling back to index 0) because **Attribute Randomize outputs a float**, while the Instancer's index field requires an **integer** — fixed with a simple **Attribute Cast** node converting the attribute to int. Once cast, adjusting each entry's weight in the Custom Discrete table directly controls how often each prototype/tree variant appears.

### Key Steps
1. Note the Instancer's default limitation: only random distribution (with a Seed) is exposed directly; the plain **Index** field alone isn't useful for controlling per-prototype frequency — the real control point is the **Prototype Index Attribute** field.
2. Add an **Attribute Randomize** node upstream, rename the output attribute to something clear (e.g. `probability`), and set **Distribution** to **Custom Discrete**.
3. In the Custom Discrete table, enter the **number of objects/prototypes** you have (e.g. 3), and assign each an **index starting from 0** (matching prototype order) along with a relative weight.
4. Copy that attribute's name into the Instancer's **Prototype Index Attribute** field.
5. **First result appears broken** — no visible change, and the viewport console reports a warning that it couldn't find an attribute named `probability`, silently defaulting everyone to index 0 (all one prototype).
6. **Root cause**: Attribute Randomize outputs a **float** attribute, but the Prototype Index Attribute field expects an **integer**.
7. **Fix**: insert an **Attribute Cast** node to convert the attribute from float to int — once cast, the Instancer correctly reads per-point index values and each prototype's frequency can now be tuned directly via the Custom Discrete table's per-entry weights.

### Houdini Nodes / VEX / Settings
**Attribute Randomize** (Distribution: Custom Discrete, one weighted entry per prototype index starting at 0) → **Attribute Cast** (float → int) → Solaris **Instancer** (Prototype Index Attribute field set to the cast attribute's name).

### Difficulty
Beginner / Intermediate — simple once you know the required attribute type and field name, but easy to get stuck on the silent float-vs-int mismatch without knowing to check the console warning.

### Houdini Version
Solaris-based (LOP context); the Instancer LOP and its Prototype Index Attribute field are available from Houdini 19.5 onward.

### Tags
#solaris #instancing #scattering #attributes #beginner #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers Solaris Instancer prototype-probability control specifically — cross-link with any future Solaris/instancing tutorials once extracted from this batch.
