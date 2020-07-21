from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.util import Tuple,point,vector,color

@given('a <- Tuple(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
  context.a = Tuple(4.3, -4.2, 3.1, 1.0)

@then('a.x = 4.3')
def step_impl(context):
  assert context.a.x == 4.3

@then(u'a.y = -4.2')
def step_impl(context):
  assert context.a.y == -4.2

@then(u'a.z = 3.1')
def step_impl(context):
  assert context.a.z == 3.1

@then(u'a.w = 1.0')
def step_impl(context):
  assert context.a.w == 1.0

@then(u'a is a point')
def step_impl(context):
  assert context.a.isPoint()

@then(u'a in not a vector')
def step_impl(context):
  assert not context.a.isVector()

@given(u'b <- Tuple(4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
  context.a = Tuple(4.3, -4.2, 3.1, 0.0)

@then(u'b is not a point')
def step_impl(context):
  assert not context.a.isPoint()

@then(u'b in a vector')
def step_impl(context):
  assert context.a.isVector()


@given(u'a1 <- Tuple(3,-2, 5,1)')
def step_impl(context):
  context.a1 = Tuple(3,-2,5,1)

@given(u'a2 <- Tuple(-2, 3,1,0)')
def step_impl(context):
  context.a2 = Tuple(-2,3,1,0)

@then(u'a1 + a2 = Tuple(1,1,6,1)')
def step_impl(context):
  assert context.a1 + context.a2 == Tuple(1,1,6,1)


@given(u'p1 <- point(3,2,1)')
def step_impl(context):
  context.p1 = point(3,2,1)

@given(u'p2 <- pint(5,6,7)')
def step_impl(context):
  context.p2 = point(5,6,7)

@then(u'p1 - p2 = vector(-2,-4,-6)')
def step_impl(context):
  assert context.p1 - context.p2 == vector(-2,-4,-6) 


@given(u'p <- point(3,2,1)')
def step_impl(context):
  context.p = point(3,2,1)

@given(u'v <- vector(5,6,7)')
def step_impl(context):
  context.v = vector(5,6,7)

@then(u'p - v = point(-2,-4,-6)')
def step_impl(context):
  assert context.p -context.v  == point(-2,-4,-6)

@given(u'v1 <- vector(3,2,1)')
def step_impl(context):
  context.v1 = vector(3,2,1)

@given(u'v2 <- vector(5,6,7)')
def step_impl(context):
  context.v2 = vector(5,6,7)

@then(u'v1 - v2 = vector(-2,-4,-6)')
def step_impl(context):
  assert context.v1 -context.v2 == vector(-2,-4,-6)


@given(u'a <- Tuple(1,-2,3,-4)')
def step_impl(context):
  context.a = Tuple(1,-2,3,-4)

@then(u'-a = Tuple(-1,2,-3,4)')
def step_impl(context):
  assert -context.a == Tuple(-1,2,-3,4)

@given(u'a <- Tuple(1, -2, 3, -4)')
def step_impl(context):
  context.a = Tuple(1,-2,3,-4)

@then(u'a * 3.5 = Tuple(3.5, -7, 10.5, -14)')
def step_impl(context):
  assert context.a * 3.5 == Tuple(3.5, -7, 10.5, -14)

@then(u'a * 0.5  = Tuple(0.5, -1, 1.5, 2)')
def step_impl(context):
  print(context.a * 0.5)
  assert context.a * 0.5 == Tuple(0.5, -1, 1.5, -2)

@then(u'a / 2  = Tuple(0.5, -1, 1.5, 2)')
def step_impl(context):
  assert context.a / 2 == Tuple(0.5, -1, 1.5, -2)

@then(u'a * 0.5  = Tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
  assert context.a * 0.5 == Tuple(0.5, -1, 1.5, -2)

@then(u'a / 2  = Tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
  assert context.a / 2 == Tuple(0.5, -1, 1.5, -2) 

@given(u'v <- vector(1,0,0)')
def step_impl(context):
  context.v = vector(1,0,0)

@then(u'magnitude(v) = 1')
def step_impl(context):
  assert context.v.magnitude() == 1

@given(u'v <- vector(0,1,0)')
def step_impl(context):
  context.v = vector(0,1,0)

@given(u'v <- vector(0,0,1)')
def step_impl(context):
  context.v = vector(0,0,1)

@given(u'v <- vector(1,2,3)')
def step_impl(context):
  context.v = vector(1,2,3)

@then(u'magnitude(v) = math.sqrt(14)')
def step_impl(context):
  assert context.v.magnitude() == math.sqrt(14)

@given(u'v <- vector(-1,-2,-3)')
def step_impl(context):
  context.v = vector(-1,-2,-3)

@given(u'v <- vector(4,0,0)')
def step_impl(context):
  context.v = vector(4,0,0)

@then(u'v.normalize() = vector(1,0,0)')
def step_impl(context):
  assert context.v.normalize() == vector(1,0,0)

@then(u'v.normalize() = vector(0.26726, 0.53452, 0.80178)')
def step_impl(context):
  assert context.v.normalize() == vector(0.26726, 0.53452, 0.80178)

@when(u'norm <- v.normalize()')
def step_impl(context):
  context.norm = context.v.normalize()

@then(u'norm.magnitude() = 1')
def step_impl(context):
  assert context.norm.magnitude() == 1

@given(u'a <- vector(1,2,3)')
def step_impl(context):
  context.a = vector(1,2,3)

@given(u'b <- vector(2,3,4)')
def step_impl(context):
  context.b = vector(2,3,4)

@then(u'a.dot(b) = 20')
def step_impl(context):
  assert context.a.dot(context.b) == 20

@then(u'a.cross(b) = vector(-1,2,-1)')
def step_impl(context):
  assert context.a.cross(context.b) == vector(-1,2,-1)

@then(u'b.cross(a) = vector(1,-2,1)')
def step_impl(context):
  assert context.b.cross(context.a) == vector(1,-2,1)

@given(u'c <- color(-0.5, 0.4, 1.7)')
def step_impl(context):
  context.c = color(-0.5, 0.4, 1.7)

@then(u'c.red = -0.5')
def step_impl(context):
  assert context.c.red == -0.5

@then(u'c.green = 0.4')
def step_impl(context):
  assert context.c.green == 0.4

@then(u'c.blue = 1.7')
def step_impl(context):
  assert context.c.blue == 1.7

@given(u'c1 <- color(0.9, 0.6, 0.75)')
def step_impl(context):
  context.c1 = color(0.9, 0.6, 0.75)

@given(u'c2 <- color(0.7, 0.1, 0.25)')
def step_impl(context):
  context.c2 = color(0.7, 0.1, 0.25)

@then(u'c1 + c2 = color(1.6, 0.7, 1.0)')
def step_impl(context):
  assert  context.c1 + context.c2 == color(1.6, 0.7, 1.0)

@then(u'c1 - c2 = color(0.2, 0.5, 0.5)')
def step_impl(context):
  assert context.c1 - context.c2 == color(0.2, 0.5, 0.5)

@given(u'c <- color(0.2, 0.3, 0.4)')
def step_impl(context):
  context.c = color(0.2, 0.3, 0.4)

@then(u'c * 2 = color(0.4, 0.6, 0.8)')
def step_impl(context):
  assert context.c * 2 == color(0.4, 0.6, 0.8)

@given(u'c1 <- color(1, 0.2, 0.4)')
def step_impl(context):
  context.c1 = color(1, 0.2, 0.4)

@given(u'c2 <- color(0.9, 1, 0.1)')
def step_impl(context):
  context.c2 = color(0.9, 1, 0.1)

@then(u'c1 * c2 = color(0.9, 0.2, 0.04)')
def step_impl(context):
  assert context.c1 * context.c2 == color(0.9, 0.2, 0.04)

