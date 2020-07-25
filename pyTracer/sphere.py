from pyTracer.util import *
from pyTracer.matrix import *

class sphere:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0
    self.r = 1
    self.transform = identity(4,4)
  def applyTransform(self,trans):
    self.transform = trans
  def intersect(self, in_r):

    # apply the transform to the ray 
    r = in_r.applyTransform(inverse(self.transform))

    sphere_to_ray = r.origin - point(0,0,0)
    a = r.direction.dot( r.direction)
    b = 2 * r.direction.dot(sphere_to_ray)
    c = sphere_to_ray.dot(sphere_to_ray) -1
    discriminant = b**2 -4 * a * c

    # less than 0 is a miss
    if discriminant < 0:
      return []

    t1 = ( -b - math.sqrt(discriminant)) / (2*a)
    t2 = ( -b + math.sqrt(discriminant)) / (2*a)

    if t1 > t2:
      return [intersection(t2,self) ,intersection(t1,self)]
    else:
      return [intersection(t1,self) ,intersection(t2,self)]
