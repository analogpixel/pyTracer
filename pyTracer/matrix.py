# from .util import Tuple
from pyTracer.util import Tuple

class matrix:
  def __init__(self, rows, columns):
    self.rows = rows;
    self.columns = columns
    self.data = [[0]*columns for x in range(rows)]
  def __str__(self):
    s = ""
    return "\n".join([ str(x) for x in self.data ])
  def srow(self, row, rowData):
    self.data[row] = rowData
  def get(self,r,c):
    return self.data[r][c]
  def getRow(self, r):
    return self.data[r]
  def getColumn(self,c):
    return [x[c] for x in self.data]
  def __getitem__(self, rc):
    r,c = rc
    return self.data[r][c]
  def __setitem__(self,rc, value):
    r,c = rc
    self.data[r][c] = value
  def __eq__(self, other):
      return self.data == other.data
  def identity(self):
    return identity(self.rows, self.columns)
  def transpose(self):
    retMatrix = matrix(self.rows, self.columns)
    for i in range(0, self.columns):
      retMatrix.srow(i, self.getColumn(i))
    return retMatrix
  def __mul__(self, other):
    # tuple mult
    if isinstance(other, Tuple):
      j = [ sum([x[0] * x[1] for x in zip(self.getRow(i), [other.x, other.y, other.z, other.w])]) for i in range(0,4) ]
      return Tuple(*j)
    # matrix mult
    elif isinstance(other, matrix):
      newMatrix = matrix(self.rows, self.columns)
      for r in range(self.rows):
        for c in range(self.columns):
          newMatrix[r,c] = sum([ x[0] * x[1]  for x in zip( self.getRow(r), other.getColumn(c))])
      return newMatrix

def identity(rows, columns):
  m = matrix(rows, columns)
  for i in range(columns):
    a = [0] * columns
    a[i] = 1
    m.srow(i, a)
  return m

