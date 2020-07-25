from pyTracer.util import *
from pyTracer.matrix import *

class ray:
  def __init__(self,origin, direction):
    self.origin = origin
    self.direction = direction
  def position(self, time):
    return self.origin + self.direction * time
  def applyTransform(self, trans):
    return ray( trans * self.origin, trans * self.direction)
