from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.util import *
from pyTracer.matrix import *
from pyTracer.rays import *
from pyTracer.sphere import *

@given(u's1 <- sphere()')
def step_impl(c):
  c.s1 = sphere()  

@given(u'i1 <- intersection(1,s1)')
def step_impl(c):
  c.i1 = intersection(1,c.s1)

@given(u'i2 <- intersection(2,s1)')
def step_impl(c):
  c.i2 = intersection(2, c.s1)

@given(u'xs1 <- intersections(i1, i2)')
def step_impl(c):
  c.xs1 = intersections( c.i1, c.i2)

@when(u'ih1 <- hit(xs1)')
def step_impl(c):
  c.ih1 = c.xs1.hit()

@then(u'ih1 = i1')
def step_impl(c):
  assert c.ih1 == c.i1

@given(u's4 <- sphere()')
def step_impl(c):
  c.s4 = sphere()  

@given(u'i3 <- intersection(-1,s4)')
def step_impl(c):
  c.i3 = intersection(-1,c.s4)

@given(u'i4 <- intersection(1,s4)')
def step_impl(c):
  c.i4 = intersection(1,c.s4)

@given(u'xs2 <- intersections(i3,i4)')
def step_impl(c):
  c.xs2 = intersections(c.i3, c.i4)

@when(u'ih2 <- hit(xs2)')
def step_impl(c):
  c.ih2 = c.xs2.hit()

@then(u'ih2 = i4')
def step_impl(c):
  assert c.ih2 == c.i4

@given(u's3 <- sphere()')
def step_impl(c):
  c.s3 = sphere()

@given(u'i5 <- intersection(-2, s3)')
def step_impl(c):
  c.i5 = intersection(-2,c.s3)

@given(u'i6 <- intersection(-1,s3)')
def step_impl(c):
  c.i6 = intersection(-1,c.s3)

@given(u'xs3 <- intersections(i5,i6)')
def step_impl(c):
  c.xs3 = intersections(c.i5, c.i6)

@when(u'i <- hit(xs3)')
def step_impl(c):
  c.i = c.xs3.hit()

@then(u'i is nothing')
def step_impl(c):
  assert c.i == []
