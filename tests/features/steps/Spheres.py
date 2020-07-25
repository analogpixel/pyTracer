from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.util import *
from pyTracer.matrix import *
from pyTracer.rays import *
from pyTracer.sphere import *
from pyTracer.transforms import *

@given(u'r <- ray( point(0,0,-5), vector(0,0,1) )')
def step_impl(c):
  c.r = ray( point(0,0,-5), vector(0,0,1) ) 

@given(u's <- sphere()')
def step_impl(c):
  c.s = sphere()

@when(u'xs <- intersect(s,r)')
def step_impl(c):
  c.xs = c.s.intersect(c.r)

@then(u'xs.count = 2')
def step_impl(c):
  assert len(c.xs) == 2

@then(u'xs[0] = 4.0')
def step_impl(c):
  assert c.xs[0].t == 4.0

@then(u'xs[1] = 6.0')
def step_impl(c):
  assert c.xs[1].t == 6.0

@given(u'r2 <- ray( point(0,1,-5), vector(0,0,1))')
def step_impl(c):
  c.r2 = ray( point(0,1,-5), vector(0,0,1))  

@given(u's2 <- sphere()')
def step_impl(c):
  c.s2 = sphere()

@when(u'xs2 = intersect(s2,r2)')
def step_impl(c):
  c.xs2 = c.s2.intersect(c.r2)

@then(u'xs2.count = 2')
def step_impl(c):
  assert len(c.xs2) == 2

@then(u'xs2[0] = 5.0')
def step_impl(c):
  assert c.xs2[0].t == 5.0

@then(u'xs2[1] = 5.0')
def step_impl(c):
  assert c.xs2[1].t == 5.0

@given(u'r3 <- ray( point(0,2,-5), vector(0,0,1))')
def step_impl(c):
  c.r3 = ray( point(0,2,-5), vector(0,0,1))

@given(u's3 = sphere()')
def step_impl(c):
  c.s3 = sphere()

@when(u'xs3 = intersect(s3,r3)')
def step_impl(c):
  c.xs3 = c.s3.intersect( c.r3)

@then(u'xs3.count = 0')
def step_impl(c):
  assert len(c.xs3) == 0

@given(u'r4 <- ray(point(0,0,0), vector(0,0,1))')
def step_impl(c):
  c.r4 = ray(point(0,0,0), vector(0,0,1))

@given(u's4 = sphere()')
def step_impl(c):
  c.s4 = sphere()

@when(u'xs4 <- intersect(s4,r4)')
def step_impl(c):
  c.xs4 = c.s4.intersect(c.r4)

@then(u'xs4.count = 2')
def step_impl(c):
  assert len(c.xs4) == 2

@then(u'xs4[0] = -1.0')
def step_impl(c):
  assert c.xs4[0].t == -1.0

@then(u'xs4[1] = 1.0')
def step_impl(c):
  assert c.xs4[1].t == 1.0

@given(u'r5 <- ray( point(0,0,5), vector(0,0,1) )')
def step_impl(c):
  c.r5 = ray(point(0,0,5), vector(0,0,1))

@given(u's5 <- sphere()')
def step_impl(c):
  c.s5 = sphere()

@when(u'xs5 <- intersect(s5,r5)')
def step_impl(c):
  c.xs5 = c.s5.intersect(c.r5)

@then(u'xs5.count = 2')
def step_impl(c):
  assert len(c.xs5) == 2

@then(u'xs5[0] = -6.0')
def step_impl(c):
  assert c.xs5[0].t == -6.0

@then(u'xs5[1] = -4.0')
def step_impl(c):
  assert c.xs5[1].t == -4.0

@given(u's6 <- sphere()')
def step_impl(c):
  c.s6 = sphere()

@when(u'i6 = intersection(3.5, s)')
def step_impl(c):
  c.i6 = intersection(3.5, c.s6)

@then(u'i6.t = 3.5')
def step_impl(c):
  assert c.i6.t == 3.5

@then(u'i6.obj = s6')
def step_impl(c):
  assert c.i6.obj == c.s6

@given(u's7 <- sphere()')
def step_impl(c):
  c.s7 = sphere()

@then(u's7.transform = identity_matrix')
def step_impl(c):
  assert c.s7.transform == identity(4,4)

@given(u's8 <- sphere()')
def step_impl(c):
  c.s8 = sphere()

@given(u't8 <- translation(2,3,4)')
def step_impl(c):
  c.t8 = translation(2,3,4)

@when(u's8.applyTransform(t8)')
def step_impl(c):
  c.s8.applyTransform(c.t8)

@then(u's8.transform = t8')
def step_impl(c):
  assert c.s8.transform == c.t8

@given(u'r10 <- ray( (point(0,0,-5), vector(0,0,1) )')
def step_impl(c):
  c.r10 = ray( point(0,0,-5), vector(0,0,1))

@given(u's10 <- sphere()')
def step_impl(c):
  c.s10 = sphere()

@when(u'S10.applyTransform( scaling(2,2,2))')
def step_impl(c):
  c.s10.applyTransform( scaling(2,2,2) )

@when(u'xs10 <- S10.intersect(r10)')
def step_impl(c):
  c.xs10 = c.s10.intersect(c.r10)

@then(u'len(xs10) = 2')
def step_impl(c):
  assert len(c.xs10) == 2

@then(u'xs10[0].t = 3')
def step_impl(c):
  assert c.xs10[0].t == 3

@then(u'xs10[1].t = 7')
def step_impl(c):
  assert c.xs10[1].t == 7

@given(u'r11 <- ray( point(0,0,-5), vector(0,0,1))')
def step_impl(c):
  c.r11 = ray( point(0,0,-5), vector(0,0,1))

@given(u's11 <- sphere()')
def step_impl(c):
  c.s11 = sphere()

@when(u's11.applyTransform( translation(5,0,0))')
def step_impl(c):
  c.s11.applyTransform( translation(5,0,0))

@when(u'xs11 <- s11.intersect(r11)')
def step_impl(c):
  c.xs11 = c.s11.intersect(c.r11)

@then(u'len(xs11) == 0')
def step_impl(c):
  assert len(c.xs11) == 0
