from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.canvas import canvas
from pyTracer.util import color,Tuple
from pyTracer.matrix import matrix,identity

@given(u'the following 4x4 matrix M')
def step_impl(context):
    context.M = matrix(4,4)
    context.M.srow(0, [1,2,3,4])
    context.M.srow(1, [5.5, 6.5, 7.5, 8.5])
    context.M.srow(2, [9,10,11,12])
    context.M.srow(3, [13.5, 14.5, 15.5, 16.5])

    context.M[1,0] = 5.5
    print(context.M)

@then(u'M[0,0] = 1')
def step_impl(context):
  assert context.M[0,0] == 1

@then(u'M[0,3] = 4')
def step_impl(context):
  assert context.M[0,3] == 4

@then(u'M[1,0] = 5.5')
def step_impl(context):
  assert context.M[1,0] == 5.5

@then(u'M[1,2] = 7.5')
def step_impl(context):
  assert context.M[1,2] == 7.5

@then(u'M[2,2] = 11')
def step_impl(context):
  assert context.M[2,2] == 11

@then(u'M[3,0] = 13.5')
def step_impl(context):
  assert context.M[3,0] == 13.5

@then(u'M[3,2] = 15.5')
def step_impl(context):
  assert context.M[3,2] == 15.5

@given(u'the following 4x4 matrix A')
def step_impl(context):
    context.A = matrix(4,4)
    context.A.srow(0, [1,2,3,4])
    context.A.srow(1, [5.5, 6.5, 7.5, 8.5])
    context.A.srow(2, [9,10,11,12])
    context.A.srow(3, [13.5, 14.5, 15.5, 16.5])

@given(u'the following 4x4 matrix B')
def step_impl(context):
    context.B = matrix(4,4)
    context.B.srow(0, [1,2,3,4])
    context.B.srow(1, [5.5, 6.5, 7.5, 8.5])
    context.B.srow(2, [9,10,11,12])
    context.B.srow(3, [13.5, 14.5, 15.5, 16.5])

@given(u'the following 4x4 matrix C')
def step_impl(context):
    context.C = matrix(4,4)
    context.C.srow(0, [1,2,3,0])
    context.C.srow(1, [5.5, 6.5, 7.5, 8.5])
    context.C.srow(2, [9,10,11,12])
    context.C.srow(3, [13.5, 14.5, 15.5, 16.5])

@then(u'A = B')
def step_impl(context):
  assert context.A == context.B

@then(u'A != C')
def step_impl(context):
  assert context.A != context.C

@given(u'the following matrix D')
def step_impl(context):
  context.D = matrix(4,4)
  context.D.data = [ [1,2,3,4], [5,6,7,8], [9,8,7,6], [5,4,3,2] ]

@given(u'the following matrix E')
def step_impl(context):
  context.E = matrix(4,4)
  context.E.data = [ [-2,1,2,3] , [3,2,1,-1], [4,3,6,5], [1,2,7,8]]

@then(u'D * E is the following 4x4 matrix')
def step_impl(context):
  tmpMatrix = matrix(4,4)
  tmpMatrix.data = [ [20,22,50,48], [44,54,114,108], [40,58,110, 102], [16,26,46,42] ]

  print( context.D * context.E)
  assert context.D * context.E == tmpMatrix

@given(u'the following matrix F')
def step_impl(context):
  context.F = matrix(4,4)
  context.F.data = [ [1,2,3,4], [2,4,4,2], [8,6,4,1], [0,0,0,1] ]

@given(u'b ← Tuple(1, 2, 3, 1)')
def step_impl(context):
  context.b = Tuple(1,2,3,1)

@then(u'F * b = Tuple(18, 24, 33, 1)')
def step_impl(context):
  assert context.F * context.b == Tuple(18,24,33,1)

@given(u'the following matrix G')
def step_impl(context):
  context.G = matrix(4,4)
  context.G.data = [ [0,1,2,4], [1,2,4,8], [2,4,8,16], [4,8,16,32] ]

@then(u'G * identity_matrix = G')
def step_impl(context):
  assert context.G * identity(4,4) == context.G

@given(u'tg ← Tuple(1, 2, 3, 4)')
def step_impl(context):
  context.tg = Tuple(1,2,3,4)

@then(u'identity_matrix * tg = tg')
def step_impl(context):
  print( identity(4,4) * context.tg, context.tg )
  assert identity(4,4) * context.tg == context.tg

@given(u'the following matrix H')
def step_impl(context):
  context.H = matrix(4,4)
  context.H.data = [ [0,9,3,0], [9,8,0,8], [1,8,5,3], [0,0,5,8] ]
  context.Ht = matrix(4,4)
  context.Ht.data = [ [ 0,9,1,0], [9,8,8,0], [3,0,5,5], [0,8,3,8] ]

@then(u'transpose(H) is the following matrix')
def step_impl(context):
  assert context.H.transpose() == context.Ht

@given(u'I ← transpose(identity_matrix)')
def step_impl(context):
  context.I = identity(4,4).transpose()

@then(u'I = identity_matrix')
def step_impl(context):
  assert context.I == identity(4,4)
