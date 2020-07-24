#!/usr/bin/env python

import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyTracer.canvas import canvas
from pyTracer.util import color,Tuple,vector,point
from pyTracer.transforms import *

c = canvas(400,400)
# c.x_offset = 200 # center it
# c.y_offset = 200 # center it

p  = point(1, 0,0)

r = rotation_z(math.pi/6)
s = scaling(100,10,10)
t  = translation(200,200)

p = t * s * p
for i in range(12):
  c.pset(p, color(1,0,0) )
  p = r * p

c.save("clock.ppm")

