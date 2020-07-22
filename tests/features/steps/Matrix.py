from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.canvas import canvas
from pyTracer.util import color,Tuple
from pyTracer.matrix import *

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

@given(u'the following 2x2 matrix J')
def step_impl(context):
  context.J = matrix(2,2)
  context.J.data = [ [1,5], [-3,2] ]

@then(u'determinant(J) = 17')
def step_impl(context):
  assert determinant(context.J) == 17

@given(u'the following 3x3 matrix K')
def step_impl(context):
  context.K = matrix(3,3)
  context.K.data = [ [1,5,0], [-3,2,7], [0,6,-3] ]

@then(u'submatrix(K, 0, 2) is the following 2x2 matrix')
def step_impl(context):
  assert submatrix(context.K, 0,2) == matrix(2,2, [ [-3,2], [0,6] ])

@given(u'the following 4x4 matrix L')
def step_impl(context):
  context.L = matrix(4,4, [[-6,1,1,6],[-8,5,8,6],[-1,0,8,2], [-7,1,-1,1]])

@then(u'submatrix(L, 2, 1) is the following 3x3 matrix')
def step_impl(context):
  assert submatrix(context.L, 2,1) ==  matrix(3,3, [[-6,1,6],[-8,8,6],[-7,-1,1]]) 

@given(u'the following 3x3 matrix M')
def step_impl(context):
  context.M = matrix(3,3, [[2,5,0],[2,-1,-7],[6,-1,5]])

@given(u'N ← submatrix(M, 1, 0)')
def step_impl(context):
  context.N = submatrix(context.M, 1,0)

@then(u'determinant(N) = 25')
def step_impl(context):
   assert determinant(context.N) == 25 

@then(u'minor(M, 1, 0) = 25')
def step_impl(context):
  assert minor(context.M, 1,0) == 25

@given(u'the following 3x3 matrix P')
def step_impl(context):
  context.P = matrix(3,3, [[3,5,0],[2,-1,-7],[6,-1,5]])

@then(u'minor(P, 0, 0) = -12')
def step_impl(context):
  assert minor(context.P, 0,0) == -12

@then(u'cofactor(P, 0, 0) = -12')
def step_impl(context):
  print("cofactor:", cofactor(context.P, 0,0) )
  assert cofactor(context.P,0,0) == -12

@then(u'minor(P, 1, 0) = 25')
def step_impl(context):
  assert minor(context.P,1,0) == 25

@then(u'cofactor(P, 1, 0) = -25')
def step_impl(context):
  assert cofactor(context.P,1,0) == -25

@given(u'the following 3x3 matrix Q')
def step_impl(context):
  context.Q = matrix(3,3, [[1,2,6],[-5,8,-4],[2,6,4]])

@then(u'cofactor(Q, 0, 0) = 56')
def step_impl(context):
  assert cofactor(context.Q, 0,0) == 56

@then(u'cofactor(Q, 0, 1) = 12')
def step_impl(context):
  assert cofactor(context.Q, 0,1) == 12

@then(u'cofactor(Q, 0, 2) = -46')
def step_impl(context):
  assert cofactor(context.Q, 0,2) == -46

@then(u'determinant(Q) = -196')
def step_impl(context):
  assert determinant(context.Q) == -196

@given(u'the following 4x4 matrix Q')
def step_impl(context):
  context.Q = matrix(4,4, [[-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[-6,7,7,-9]])

@then(u'cofactor(Q, 0, 0) = 690')
def step_impl(context):
  print(cofactor(context.Q, 0,0))
  assert cofactor(context.Q,0,0) == 690

@then(u'cofactor(Q, 0, 1) = 447')
def step_impl(context):
  assert cofactor(context.Q, 0,1) == 447

@then(u'cofactor(Q, 0, 2) = 210')
def step_impl(context):
  assert cofactor(context.Q, 0,2) == 210

@then(u'cofactor(Q, 0, 3) = 51')
def step_impl(context):
  assert cofactor(context.Q, 0,3) == 51

@then(u'determinant(Q) = -4071')
def step_impl(context):
  assert determinant(context.Q) == -4071

@given(u'the following 4x4 matrix R')
def step_impl(context):
  context.R = matrix(4,4, [[6,4,4,4],[5,5,7,6],[4,-9,3,-7],[9,1,7,-6]])

@then(u'determinant(R) = -2120')
def step_impl(context):
  assert determinant(context.R) == -2120

@then(u'R is invertible')
def step_impl(context):
  assert invertible(context.R)

@given(u'the following 4x4 matrix S')
def step_impl(context):
  context.S = matrix(4,4, [[-4,2,-2,-3], [9,6,2,6], [0,-5,1,-5], [0,0,0,0] ])

@then(u'determinant(S) = 0')
def step_impl(context):
  assert determinant(context.S) == 0

@then(u'S is not invertible')
def step_impl(context):
  assert not invertible(context.S)

@given(u'the following 4x4 matrix T')
def step_impl(context):
  context.T = matrix(4,4, [[-5,2,6,-8],[1,-5,1,8],[7,7,-6,-7],[1,-3,7,4]])

@given(u'U ← inverse(T)')
def step_impl(context):
  context.U = inverse(context.T)

@then(u'determinant(T) = 532')
def step_impl(context):
  assert determinant(context.T) == 532

@then(u'cofactor(T, 2, 3) = -160')
def step_impl(context):
  assert cofactor(context.T, 2,3) == -160

@then(u'U[3,2] = -160/532')
def step_impl(context):
  assert context.U[3,2] == -160/532

@then(u'cofactor(T, 3, 2) = 105')
def step_impl(context):
  assert cofactor(context.T, 3,2) == 105

@then(u'U[2,3] = 105/532')
def step_impl(context):
  assert context.U[2,3] == 105/532

@then(u'U is the following 4x4 matrix')
def step_impl(context):
  print(context.T)
  print(context.U)
  assert context.U == matrix(4,4, [
                                  [0.21805 ,  0.45113 ,  0.24060 , -0.04511], 
                                  [-0.80827,-1.45677,-0.44361,0.52068],
                                  [-0.07895 , -0.22368 , -0.05263 ,  0.19737],
                                  [-0.52256 , -0.81391 , -0.30075 ,  0.30639 ]])

