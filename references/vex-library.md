# VEX Library

Core VEX patterns for Houdini wrangles. Each entry: what it does, which wrangle context, and the snippet.

---

## Fundamentals

### Attribute Access Conventions
```vex
// Read / write by type prefix
float  f = f@myFloat;       // float attribute
vector v = v@myVector;      // 3-component vector (also v@P, v@N, v@Cd)
int    i = i@myInt;
string s = s@myString;
vector4 q = p@myQuat;       // quaternion
matrix  m = 3@myMatrix3;

// Point position (always available)
vector pos = v@P;

// Point number and total count
int id  = i@ptnum;
int cnt = i@numpt;
```

### Reading Parameters (chf, chi, chv, chs)
```vex
float amp   = chf("amplitude");   // float channel
int   seed  = chi("seed");        // integer channel
vector col  = chv("color");       // vector channel
string name = chs("name");        // string channel
```

### Time and Frame
```vex
float t     = f@Time;       // current time in seconds
float frame = f@Frame;      // current frame number
float fps   = f@TimeInc;    // 1.0 / FPS
```

---

## Point Wrangles

### Noise Displacement
```vex
// Context: Point Wrangle
vector freq  = chv("frequency");
float  amp   = chf("amplitude");
float  off   = chf("time_offset");

// 4D noise — animate with time
float n = noise(v@P * freq + set(0, 0, 0, f@Time * off));
v@P += v@N * n * amp;
```

### Random Per-Point Color
```vex
// Context: Point Wrangle
int seed = chi("seed");
v@Cd = hsvtorgb(set(rand(i@ptnum + seed), 0.7, 0.9));
```

### Delete Points by Condition
```vex
// Context: Point Wrangle
if (v@P.y < chf("threshold")) removepoint(0, i@ptnum);
```

### Align Normal to Velocity
```vex
// Context: Point Wrangle
if (length(v@v) > 0.001)
    v@N = normalize(v@v);
```

### Point Attraction (move toward target position)
```vex
// Context: Point Wrangle — target position via chv
vector target = chv("target");
float  speed  = chf("speed");
vector dir    = normalize(target - v@P);
v@P += dir * speed * f@TimeInc;
```

---

## Primitive Wrangles

### Set Prim Color from Center
```vex
// Context: Primitive Wrangle
vector center = getbbox_center(0);   // bounding box center
float  dist   = distance(v@P, center);
v@Cd = chramp("color_ramp", fit01(dist, 0.0, 1.0));
```

### Extrude Primitives Procedurally
```vex
// Context: Primitive Wrangle — use after Divide SOP
vector n    = prim_normal(0, i@primnum, {0.5, 0.5});
float  dist = chf("extrude_dist") * rand(i@primnum + chi("seed"));
foreach (int pt; primpoints(0, i@primnum)) {
    vector pos = point(0, "P", pt);
    setpointattrib(0, "P", pt, pos + n * dist, "set");
}
```

---

## Detail Wrangles

### Create Points Procedurally
```vex
// Context: Detail Wrangle
int count = chi("count");
for (int i = 0; i < count; i++) {
    int pt = addpoint(0, set(rand(i)*2-1, rand(i+1)*2-1, rand(i+2)*2-1));
    setpointattrib(0, "Cd", pt, {1, 0.8, 0.2});
}
```

### Pack Attribute into Detail
```vex
// Context: Detail Wrangle
setdetailattrib(0, "total_points", npoints(0), "set");
```

---

## Geometry Functions

```vex
// Point queries
int npts        = npoints(0);
vector pos      = point(0, "P", ptnum);
int nearpt      = nearpoint(0, v@P);           // nearest point
int[] near_arr  = nearpoints(0, v@P, radius);  // points within radius

// Primitive queries
int nprims      = nprimitives(0);
int[] pts       = primpoints(0, primnum);       // points of a prim
vector pn       = prim_normal(0, primnum, {0.5, 0.5});

// Attribute access in functions
float val       = point(0, "myattr", ptnum);
setpointattrib(0, "myattr", ptnum, value, "set");
setprimattrib(0,  "myattr", primnum, value, "set");
setvertexattrib(0,"myattr", primnum, vtxnum, value, "set");
setdetailattrib(0,"myattr", value, "set");
```

---

## Math Utilities

```vex
// Remapping
float r = fit(val, src_min, src_max, dst_min, dst_max);
float r = fit01(val, dst_min, dst_max);    // from 0-1 range
float r = clamp(val, 0.0, 1.0);
float r = smooth(0.0, 1.0, val);           // smoothstep

// Vector ops
float  len  = length(v);
vector n    = normalize(v);
vector c    = cross(a, b);
float  d    = dot(a, b);
float  dist = distance(a, b);

// Angle
float angle = atan2(y, x);                 // 2D angle
vector axis = normalize(cross(from, to));
float  ang  = acos(dot(normalize(from), normalize(to)));
vector4 q   = quaternion(angle, axis);     // quaternion from axis-angle
matrix3 m   = qconvert(q);                 // matrix from quaternion

// Random
float r  = rand(seed);                     // 0-1 float
vector r = rand(seed);                     // 0-1 vector (same call, different lvalue)
int r    = int(rand(seed) * range);        // integer in range
```

---

## Noise Functions

```vex
// Simplex / Perlin noise variants
float n   = noise(pos);                    // 0-1 range, 3D input
float n   = noise(pos, t);                 // 4D (animated)
float n   = snoise(pos);                   // -1 to 1 range
float n   = onoise(pos);                   // original Perlin
float n   = anoise(pos);                   // analytic noise (returns gradient too)

// Fractal / fBm noise
float n   = fbm(pos);                      // built-in fBm
// Manual fBm:
float n = 0; float amp = 1; vector p = pos;
for (int i = 0; i < 6; i++) {
    n += noise(p) * amp;
    amp *= 0.5; p *= 2.0;
}

// Curl noise (divergence-free — good for fluids/particles)
vector curl = curlnoise(pos);
```

---

## String Operations

```vex
string s   = sprintf("prefix_%d", i@ptnum);
int    len = len(s);
string sub = substr(s, start, length);
int    pos = find(s, "search");
string joined = join(array, ",");
```

---

## Common Patterns

### Smooth Follow (spring-like)
```vex
// Context: Point Wrangle in Simulation Zone (or SOP solver)
vector target  = v@target_pos;
float  stiff   = chf("stiffness");
vector vel     = v@vel;
vector force   = (target - v@P) * stiff;
vel += force * f@TimeInc;
v@P  += vel * f@TimeInc;
v@vel = vel;
```

### Instance Rotation from Velocity
```vex
// Context: Point Wrangle — prepares orient attrib for Copy to Points
vector up = {0, 1, 0};
if (length(v@v) > 0.001) {
    vector fwd = normalize(v@v);
    vector right = normalize(cross(up, fwd));
    up = cross(fwd, right);
    p@orient = quaternion(maketransform(fwd, up));
}
```

### VEX Ramp Lookup
```vex
// Context: Point Wrangle — expose ramp parameter in HDA
float t = fit01(f@age / f@life, 0.0, 1.0);
v@Cd = chramp("color_over_life", t);
float scale = chf_ramp("scale_over_life", t);   // note: chf ramp uses different call
```
