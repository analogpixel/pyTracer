#!/usr/bin/env python

import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyTracer.canvas import canvas
from pyTracer.util import color,Tuple,vector,point

class env:
  def __init__(self,gravity, wind):
    self.gravity = gravity
    self.wind = wind

class proj:
  def __init__(self,position, velocity):
    self.position = position
    self.velocity = velocity

def tick(e,p):
  position = p.position + p.velocity
  velocity = p.velocity + e.gravity + e.wind
  return proj(position, velocity)


c = canvas(900,500)
p = proj( point(0,1,0), vector(1,1.8,0).normalize() * 11.25) 
e = env( vector(0,-0.1,0) , vector(-0.01, 0,0))

for i in range(0,200):
  p = tick(e,p)
  print(p.position, p.velocity)
  c.set(int(p.position.x), c.height - int(p.position.y), color(1,0,0) )

c.save("test.ppm")

