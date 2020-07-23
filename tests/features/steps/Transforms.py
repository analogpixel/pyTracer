from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.canvas import canvas
from pyTracer.util import color,Tuple
from pyTracer.matrix import *
from pyTracer.transforms import *

@given(u'transform = translation(5,-3,2)')
def step_impl(c):
   c.transform = translation(5,-3,2)


@given(u'p = point(-3,4,5)')
def step_impl(c):
  c.p = point(-3,4,5)

@then(u'transform * p = point(2,1,7)')
def step_impl(c):
  assert c.transform * c.p == point(2,1,7)

@given(u'inv = inverse(transform)')
def step_impl(c):
    c.inv = inverse(c.transform)


@then(u'inv * p = point(-8,7,3)')
def step_impl(c):
  assert c.inv * c.p == point(-8,7,3)

@given(u'v = vector(-3,4,5)')
def step_impl(c):
  c.v = vector(-3,4,5)

@then(u'transform * v = v')
def step_impl(c):
  assert c.transform  * c.v == c.v

@given(u't2 = scaling(2,3,4)')
def step_impl(c):
  c.t2 = scaling(2,3,4)

@given(u'p2 = point(-4,6,8)')
def step_impl(c):
  c.p2 = point(-4,6,8)

@then(u't2 * p2 = point(-8,18,32)')
def step_impl(c):
  assert c.t2 * c.p2 == point(-8,18,32)

@given(u'v2 = vector(-4,6,8)')
def step_impl(c):
  c.v2 = vector(-4,6,8)

@then(u't2 * v2 = vector(-8,18,32)')
def step_impl(c):
  assert c.t2 * c.v2 == vector(-8,18,32)

@given(u'inv2  = inverse(t2)')
def step_impl(c):
  c.inv2 = inverse(c.t2)

@then(u'inv2 * v2 = vector(-2,2,2)')
def step_impl(c):
  assert c.inv2 * c.v2 == vector(-2,2,2)

@given(u't3 = scaling(-1,1,1)')
def step_impl(c):
  c.t3 = scaling(-1,1,1)

@given(u'p3 = point(2,3,4)')
def step_impl(c):
  c.p3 = point(2,3,4)

@then(u't3 * p3 = point(-2,3,4)')
def step_impl(c):
  assert c.t3 * c.p3 == point(-2,3,4)

@given(u'p4 = point(0,1,0)')
def step_impl(c):
  c.p4 = point(0,1,0)

@given(u'half_quarter = rotation_x( pi / 4)')
def step_impl(c):
  c.half_quarter = rotation_x( math.pi /4)

@given(u'full quarter = rotation_x( pi /2)')
def step_impl(c):
  c.full_quarter = rotation_x( math.pi /2)

@then(u'half_quarter * p4 = point (0, sqrt(2)/2, sqrt(2)/2)')
def step_impl(c):
  assert c.half_quarter * c.p4 == point(0, math.sqrt(2)/2, math.sqrt(2)/2)

@then(u'full_quarter * p4 = point(0,0,1)')
def step_impl(c):
  assert c.full_quarter * c.p4 == point(0,0,1)

@given(u'p5 = point(0,0,1)')
def step_impl(c):
  c.p5 = point(0,0,1)

@given(u'half_quarter_y = rotation_y( pi / 4)')
def step_impl(c):
  c.half_quarter_y = rotation_y( math.pi /4)  

@given(u'full_quarter_y = rotation_y( pi /2)')
def step_impl(c):
  c.full_quarter_y = rotation_y( math.pi /2)

@then(u'half_quarter * p = point(sqrt(2)/2, 0, sqrt(2)/2)')
def step_impl(c):
  assert c.half_quarter_y * c.p5== point( math.sqrt(2)/2, 0, math.sqrt(2)/2)

@then(u'full_quarter * p = point(1,0,0)')
def step_impl(c):
    assert c.full_quarter_y * c.p5== point(1,0,0)

@given(u'p6 = point(0,1,0)')
def step_impl(c):
  c.p6 = point(0,1,0)

@given(u'half_quarter_z = rotation_z(pi/4)')
def step_impl(c):
  c.half_quarter_z = rotation_z(math.pi /4)

@given(u'full_quarter_z = rotation_z(pi /2)')
def step_impl(c):
  c.full_quarter_z = rotation_z(math.pi /2)

@then(u'half_quarter_z * p6 = point(-sqrt(2)/2, sqrt(2)/2, 0)')
def step_impl(c):
  assert c.half_quarter_z * c.p6 == point( -math.sqrt(2)/2, math.sqrt(2)/2, 0)

@then(u'full_quarter * p = point(-1,0,0)')
def step_impl(c):
  assert c.full_quarter_z * c.p6 == point(-1,0,0)

@given(u'transform_s1 ← shearing(1, 0, 0, 0, 0, 0)')
def step_impl(c):
  c.transform_s1 = shearing(1,0,0,0,0,0)

@given(u'p7 ← point(2, 3, 4)')
def step_impl(c):
  c.p7 = point(2,3,4)

@then(u'transform_s1 * p7 = point(5, 3, 4)')
def step_impl(c):
  assert c.transform_s1 * c.p7 == point(5,3,4)

@given(u'transform_s2 ← shearing(0, 1, 0, 0, 0, 0)')
def step_impl(c):
  c.transform_s2 = shearing(0,1,0,0,0,0)

@then(u'transform_s2 * p7 = point(6, 3, 4)')
def step_impl(c):
  assert c.transform_s2 * c.p7 == point(6,3,4)

@given(u'transform_s3 ← shearing(0, 0, 1, 0, 0, 0)')
def step_impl(c):
  c.transform_s3 = shearing(0,0,1,0,0,0)

@then(u'transform_s3 * p7 = point(2, 5, 4)')
def step_impl(c):
  assert c.transform_s3 * c.p7 == point(2,5,4)

@given(u'transform_s4 ← shearing(0, 0, 0, 1, 0, 0)')
def step_impl(c):
  c.transform_s4 = shearing(0,0,0,1,0,0)

@then(u'transform_s4 * p7 = point(2, 7, 4)')
def step_impl(c):
  assert c.transform_s4 * c.p7 == point(2,7,4)

@given(u'transform_s5 ← shearing(0, 0, 0, 0, 1, 0)')
def step_impl(c):
  c.transform_s5 = shearing(0,0,0,0,1,0)

@then(u'transform_s5 * p7 = point(2, 3, 6)')
def step_impl(c):
  assert c.transform_s5 * c.p7 == point(2,3,6)

@given(u'transform_s6 ← shearing(0, 0, 0, 0, 0, 1)')
def step_impl(c):
  c.transform_s6 = shearing(0,0,0,0,0,1)

@then(u'transform_s6 * p7 = point(2, 3, 7)')
def step_impl(c):
  assert c.transform_s6 * c.p7 == point(2,3,7)
