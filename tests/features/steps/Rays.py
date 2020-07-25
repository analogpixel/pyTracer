from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.util import *
from pyTracer.matrix import *
from pyTracer.rays import *
from pyTracer.transforms import *

@given(u'origin = point(1,2,3)')
def step_impl(c):
  c.origin = point(1,2,3)  

@given(u'direction = vector(4,5,6)')
def step_impl(c):
  c.direction = vector(4,5,6)

@when(u'r = ray(origin,direction)')
def step_impl(c):
  c.ray = ray(c.origin, c.direction)

@then(u'r.origin = origin')
def step_impl(c):
  assert c.ray.origin == c.origin

@then(u'r.direction = direction')
def step_impl(c):
  assert c.ray.direction == c.direction

@given(u'r2 <- ray( point(2,3,4), vector(1,0,0))')
def step_impl(c):
  c.r2 = ray( point(2,3,4), vector(1,0,0))

@then(u'position(r2,0) = point(2,3,4)')
def step_impl(c):
  assert c.r2.position(0) == point(2,3,4)

@then(u'position(r2,1) = point(3,3,4)')
def step_impl(c):
  assert c.r2.position(1) == point(3,3,4)

@then(u'position(r2,-1) = point(1,3,4)')
def step_impl(c):
  assert c.r2.position(-1) == point(1,3,4)

@then(u'position(r2,2.5) = point(4.5,3,4)')
def step_impl(c):
  assert c.r2.position(2.5) == point(4.5, 3,4)

@given(u'r3<- ray( point(1,2,3), vector(0,1,0) )')
def step_impl(c):
  c.r3 = ray( point(1,2,3), vector(0,1,0))

@given(u'm3<- translation(3,4,5)')
def step_impl(c):
  c.m3 = translation(3,4,5) 

@when(u'r4 <- transform(r3, m3)')
def step_impl(c):
  c.r4 = c.r3.applyTransform(c.m3)

@then(u'r4.origin = point(4,6,8)')
def step_impl(c):
  assert c.r4.origin == point(4,6,8)

@then(u'r4.direction = vector( 0,1,0)')
def step_impl(c):
  assert c.r4.direction == vector(0,1,0)

@given(u'r5 <- ray(point(1,2,3), vector(0,1,0))')
def step_impl(c):
  c.r5 = ray(point(1,2,3), vector(0,1,0))

@given(u'm4 <- scaling(2,3,4)')
def step_impl(c):
  c.m4 = scaling(2,3,4)

@when(u'r6  <- r5.applyTransform(m4)')
def step_impl(c):
  c.r6 = c.r5.applyTransform(c.m4)

@then(u'r6.origin = point(2,6,12)')
def step_impl(c):
  assert c.r6.origin == point(2,6,12)

@then(u'r6.direction = vector(0,3,0)')
def step_impl(c):
  assert c.r6.direction == vector(0,3,0)
