# Python in Houdini

The `hou` module — Python scripting for Houdini: nodes, parameters, geometry, shelf tools, callbacks, HDAs.

---

## Getting Started

```python
import hou

# Always available in Houdini's Python shell / Python SOP / callbacks
# From external script, initialize first:
# hou.hipFile.load("/path/to/file.hip")
```

---

## Nodes

```python
# Get nodes
root    = hou.node("/")
obj     = hou.node("/obj")
geo     = hou.node("/obj/geo1")
sop     = hou.node("/obj/geo1/scatter1")

# Current node (inside Python SOP or callback)
node = hou.pwd()

# Navigate
parent  = node.parent()
inputs  = node.inputs()         # tuple of input nodes
outputs = node.outputs()        # tuple of output nodes
children= node.children()       # children (inside subnet)

# Create nodes
new_node = geo.createNode("box")          # create by type name
new_node = geo.createNode("attribwrangle", node_name="my_wrangle")

# Set parameters
sop.parm("tx").set(1.0)
sop.parmTuple("t").set((1.0, 2.0, 3.0))

# Read parameters
val = sop.parm("tx").eval()
vec = sop.parmTuple("t").eval()    # returns tuple

# Connect nodes
node_b.setInput(0, node_a)         # input 0 of node_b = output of node_a
node_b.setInput(0, node_a, 1)      # input 0 of B = output 1 of A

# Display flag (what shows in viewport)
sop.setDisplayFlag(True)
sop.setRenderFlag(True)

# Bypass
sop.bypass(True)

# Delete
sop.destroy()
```

---

## Parameters

```python
parm = node.parm("myParam")

# Read
val  = parm.eval()
expr = parm.expression()
lang = parm.expressionLanguage()    # hou.exprLanguage.Python or .Hscript

# Set
parm.set(42.0)
parm.setExpression("$F * 0.1")                         # HScript expression
parm.setExpression("hou.frame() * 0.1",
                   hou.exprLanguage.Python)            # Python expression

# Keyframes
key = hou.Keyframe()
key.setFrame(1)
key.setValue(0.0)
parm.setKeyframe(key)

key2 = hou.Keyframe()
key2.setFrame(100)
key2.setValue(1.0)
parm.setKeyframe(key2)

# Remove keys
parm.deleteAllKeyframes()

# Multiparm (variable parameter blocks)
count = node.parm("myparm").eval()
for i in range(1, count + 1):
    val = node.parm(f"element{i}value").eval()
```

---

## Geometry (Python SOP)

```python
# In a Python SOP — node = hou.pwd(), geo = node.geometry()
node = hou.pwd()
geo  = node.geometry()

# Points
points = geo.points()
for pt in points:
    pos = pt.position()          # hou.Vector3
    idx = pt.number()

# Create point
pt = geo.createPoint()
pt.setPosition(hou.Vector3(1, 2, 3))

# Attributes
# Read
cd_attrib = geo.findPointAttrib("Cd")
for pt in geo.points():
    cd = pt.attribValue("Cd")    # returns tuple for vector

# Create attribute
Cd = geo.addAttrib(hou.attribType.Point, "Cd", (1.0, 1.0, 1.0))

# Write
for pt in geo.points():
    pt.setAttribValue("Cd", (1.0, 0.5, 0.0))

# Primitives
for prim in geo.prims():
    area = prim.intrinsicValue("measuredperimeter")
    pts  = prim.vertices()

# Create polygon
poly = geo.createPolygon()
for pt in [pt0, pt1, pt2, pt3]:
    poly.addVertex(pt)

# Bounding box
bbox   = geo.boundingBox()
center = bbox.center()
size   = bbox.sizevec()
```

---

## Shelf Tools & Scripts

```python
# Shelf tool script (runs at /obj level by default)
import hou

# Get selected nodes
selected = hou.selectedNodes()
for node in selected:
    print(node.path(), node.type().name())

# Create from selection
for node in hou.selectedNodes():
    if node.type().name() == "geo":
        sop_net = node.node(".")
        wrangle = sop_net.createNode("attribwrangle")
        wrangle.parm("snippet").set('v@P += {0, chf("height"), 0};')

# Dialog
result = hou.ui.displayMessage("Do you want to proceed?",
    buttons=("Yes", "No"), default_choice=0)
if result == 0:
    print("User chose Yes")

# Input dialog
val = hou.ui.readInput("Enter amplitude:", initial_contents="1.0")
```

---

## HDAs — Python Scripts

### Parameter Callback
```python
# In HDA Type Properties → Parameters → script callback (per parameter)
# callback script field:
def my_callback(kwargs):
    node  = kwargs["node"]
    parm  = kwargs["parm"]
    value = parm.eval()
    # do something with value
    node.parm("output_param").set(value * 2)
```

### Event Callbacks
```python
# In HDA Type Properties → Scripts tab

# OnCreated — runs when HDA is placed
def onCreated(kwargs):
    node = kwargs["node"]
    node.parm("seed").set(int(hou.time() * 1000) % 9999)

# OnInputChanged — runs when input connection changes
def onInputChanged(kwargs):
    node  = kwargs["node"]
    input_idx = kwargs["input_index"]
    print(f"Input {input_idx} changed")
```

---

## Useful hou Functions

```python
# Time and frame
hou.frame()                     # current frame (float)
hou.time()                      # current time in seconds
hou.fps()                       # frames per second
hou.setFrame(42)                # set current frame

# File operations
hou.hipFile.save()
hou.hipFile.load("/path/file.hip")
hou.hipFile.name()              # current hip file path

# UI
hou.ui.displayMessage("msg")
hou.ui.readInput("prompt")
hou.ui.selectFile(title="Choose file", file_type=hou.fileType.Image)
hou.ui.displayFileDependencyDialog()

# Node search
hou.nodeType("Sop/box")        # get node type object
nodes = hou.node("/obj").recursiveGlob("*", hou.nodeTypeFilter.Sop)

# Evaluate expressions
hou.hscriptExpression("$HIP")  # evaluate HScript expression

# Environment variables
hip = hou.getenv("HIP")
hou.putenv("MYVAR", "value")
```

---

## Common Patterns

### Process All Selected Nodes
```python
import hou
for node in hou.selectedNodes():
    parm = node.parm("myParam")
    if parm:
        parm.set(parm.eval() * 2.0)
```

### Create Wrangle with Code
```python
import hou
geo = hou.node("/obj/geo1")
w = geo.createNode("attribwrangle", "my_wrangle")
w.parm("class").set(0)  # 0=point, 1=vertex, 2=prim, 3=detail
w.parm("snippet").set("""
float noise = fit(noise(v@P * 2.0 + f@Time), 0, 1, -1, 1);
v@P += v@N * noise * chf("amplitude");
""")
```

### Batch Parameter Set Across Nodes
```python
import hou
root = hou.node("/obj")
for node in root.allSubChildren():
    parm = node.parm("divisions")
    if parm:
        parm.set(5)
```
