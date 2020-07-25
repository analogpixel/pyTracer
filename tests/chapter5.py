#!/usr/bin/env python

import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyTracer.canvas import canvas
from pyTracer.util import *
from pyTracer.transforms import *
from pyTracer.sphere import *
from pyTracer.rays import *

ray_origin = point(0,0,-5)
wall_z = 10 
wall_size = 7
canvas_pixels = 100
pixel_size = wall_size / canvas_pixels
shape = sphere()

c = canvas(100,100)

# shape.applyTransform( scaling(2,2,2) )

for y in range( canvas_pixels):
  world_y = (wall_size/2) - pixel_size * y
  for x in range( canvas_pixels):
    world_x = -(wall_size/2) + pixel_size * x
    position = point( world_x, world_y, wall_z)

    r = ray( ray_origin, (position - ray_origin).normalize() )
    xs = intersections( *shape.intersect(r))
    t = xs.hit()
    if t:
      print(t)
      c.set(x,y, color(1,0,0))


c.save("sphere.ppm")

