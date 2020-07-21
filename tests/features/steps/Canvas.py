from behave import *
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pyTracer.canvas import canvas
from pyTracer.util import color

@given(u'c <- canvas(10,20)')
def step_impl(context):
  context.c = canvas(10,20)

@then(u'c.width = 10')
def step_impl(context):
  assert context.c.width == 10

@then(u'c.height = 20')
def step_impl(context):
  assert context.c.height == 20

@then(u'every pixel of c is color(0,0,0)')
def step_impl(context):
  assert all( [x == color(0,0,0) for x in context.c.data] )

@given(u'red <- color(1,0,0)')
def step_impl(context):
  context.red = color(1,0,0)

@when(u'write_pixel(c,2,3,red)')
def step_impl(context):
  context.c.set(2,3,context.red)

@then(u'pixel_at(c,2,3,) = red')
def step_impl(context):
  assert context.c.get(2,3) == context.red

@when(u'ppm <- canvas_to_ppm(c)')
def step_impl(context):
  context.c.save("out.ppm")

@then(u'lines 1-3 of ppm are')
def step_impl(context):
  d = open("out.ppm","r").readlines()
  assert d[0].strip() == "P3" and d[1].strip() == "10 20" and d[2].strip() == "256"

