#!/usr/bin/env python

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

output = []
for l in lines:
 output.append( "[" + l.replace("|", ",").replace(' ','')[1:-1] + "]" )

print( "[" + ",".join(output) + "]" )

