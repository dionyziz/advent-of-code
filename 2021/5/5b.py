from collections import Counter
from parse import parse
from itertools import repeat
from numpy import sign

with open('in.txt') as f:
  lines = f.read().splitlines()

points = Counter()
for line in lines:
  startx, starty, endx, endy = parse('{:d},{:d} -> {:d},{:d}', line)
  if startx == endx:
    xrange = repeat(startx)
  else:
    xrange = range(startx, endx + sign(endx - startx), sign(endx - startx))
  if starty == endy:
    yrange = repeat(starty)
  else:
    yrange = range(starty, endy + sign(endy - starty), sign(endy - starty))
  points += Counter(zip(xrange, yrange))
  
print(len([elem for elem, cnt in points.items() if cnt > 1]))
