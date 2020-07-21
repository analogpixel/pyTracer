from .util import color

class canvas:
  maxColors = 256

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.data = [color(0,0,0)] * width * height

  def set(self,x,y,c):
    x = int(x)
    y = int(y)
    if x > self.width or x < 0 or y > self.height or y < 0:
      return
 
    self.data[ x + y * self.width] = c

  def get(self,x,y):
    x = int(x)
    y = int(y)
    if x > self.width or x < 0 or y > self.height or y < 0:
      return

    return self.data[ x + y * self.width] 

  def map_range(self,value, low1, high1, low2, high2):
    if value < low1:
      value = low1
    if value > high1:
      value = high1
    return low2 + (high2 - low2) * (value - low1) / (high1 - low1);

  def cmap(self,color):
    return int(self.map_range(color, 0,1, 0, self.maxColors))

  def save(self, filename):
    with open(filename, "w") as f:
      f.write("P3\n")
      f.write("{} {}\n".format(self.width, self.height) )
      f.write("{}\n".format(self.maxColors))
      
      d = ""
      for i in range(0, len(self.data)):
        d += "{} {} {} ".format( self.cmap(self.data[i].red), self.cmap(self.data[i].green), self.cmap(self.data[i].blue))
        if len(d) > 65:
          f.write("{}\n".format(d))
          d = ""
      f.write("{}\n".format(d))
    
