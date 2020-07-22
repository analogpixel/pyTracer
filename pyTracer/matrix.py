# from .util import Tuple
from pyTracer.util import Tuple

class matrix:
  def __init__(self, rows, columns, data=None):
    self.rows = rows;
    self.columns = columns
    if data:
      self.data = data
    else:
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
    for rows in range(self.rows):
      for cols in range(self.columns):
        if abs(self[rows,cols] - other[rows,cols]) < .00001:
          continue
        else:
          return False
    return True
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

def determinant(m):
  det = 0
  if m.rows == 2:
    det =  m[0,0] * m[1,1] - m[0,1] * m[1,0]
  else:
    for i in range(0, m.rows):
      det += m[0,i] * cofactor(m, 0, i)
  return det

def submatrix(m, r,c):
  rows = m.data[0:r] + m.data[r+1:]
  cols = [ x[:c] + x[c+1:] for x in rows]
  return matrix( m.rows-1, m.columns-1, cols)

def minor(m, r,c):
  return determinant(submatrix(m, r,c))

def cofactor(m, r,c):
  cof = matrix(4,4, [ [1,-1,1,-1], [-1,1,-1,1], [1,-1,1,-1], [-1,1,-1,1] ])
  return cof[r,c] * minor(m,r,c)

def invertible(m):
  if determinant(m) == 0:
    return False
  else:
    return True

def inverse(m):
  if not invertible(m):
    return False

  m2 = matrix(m.rows, m.columns)

  for r in range(m.rows):
    for c in range(m.columns):
      co = cofactor(m,r,c)
      m2[c,r] = co / determinant(m)

  return m2
