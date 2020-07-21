import math

class Tuple:
  def __init__(self,x,y,z,w):
    self.x = x
    self.y = y
    self.z = z
    self.w = w
    self.eps = 0.001
  def isPoint(self):
    return self.w == 1.0
  def isVector(self):
    return self.w == 0.0
  def __add__(self, other):
    return Tuple(self.x + other.x, self.y+other.y, self.z + other.z, self.w + other.w)
  def __sub__(self, other):
    return Tuple(self.x - other.x, self.y-other.y, self.z - other.z, self.w - other.w)
  def __eq__(self,other):
    return (abs(self.x - other.x) < self.eps and 
            abs(self.y - other.y) < self.eps and
            abs(self.z - other.z) < self.eps and
            abs(self.w - other.w) < self.eps )
  def __neg__(self):
    return Tuple(-self.x, -self.y, -self.z, -self.w)
  def __mul__(self, other):
    return Tuple(self.x * other, self.y*other, self.z*other, self.w*other)
  def __rmul__(self, other):
    return Tuple(self.x * other, self.y*other, self.z*other, self.w*other)
  def __truediv__(self,other):
    return Tuple(self.x / other, self.y/other, self.z/other, self.w/other)
  def __str__(self):
    return "{},{},{},{}".format(self.x, self.y, self.z, self.w)
  def magnitude(self):
    return math.sqrt( self.x**2 + self.y**2 + self.z**2 + self.w**2)
  def normalize(self):
    return Tuple( self.x / self.magnitude(), 
                  self.y / self.magnitude(),
                  self.z / self.magnitude(),
                  self.w / self.magnitude())
  def cross(self, other):
    return vector(  (self.y * other.z - self.z * other.y),
                    (self.z * other.x - self.x * other.z),
                    (self.x * other.y - self.y * other.x) )
  def dot(self, other):
    return (self.x * other.x + 
            self.y * other.y + 
            self.z * other.z + 
            self.w * other.w)

def point(x,y,z):
  return( Tuple(x,y,z,1.0) )

def vector(x,y,z):
  return( Tuple(x,y,z,0.0) )

class color():
  def __init__(self,r,g,b,a=1):
    self.red = r
    self.green = g
    self.blue = b
    self.alpha = a
    self.eps = 0.001
  def __eq__(self,other):
    return ( abs(self.red -other.red) < self.eps and 
             abs(self.green - other.green) < self.eps and 
             abs(self.blue - other.blue) < self.eps)
  def __str__(self):
    return "{},{},{},{}".format(self.red, self.green, self.blue, self.alpha)
  def __add__(self, other):
    return color(self.red + other.red, self.green + other.green, self.blue + other.blue, self.alpha + other.alpha)
  def __sub__(self, other):
    return color(self.red - other.red, self.green-other.green, self.blue - other.blue, self.alpha - other.alpha)
  def __mul__(self, other):
    if isinstance(other, color):
      return color( self.red * other.red,  self.green * other.green, self.blue * other.blue, self.alpha *other.alpha)
    else:
      return color( self.red * other, self.green * other, self.blue *other, self.alpha * other)

