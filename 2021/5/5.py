from collections import Counter
from itertools import repeat
from parse import parse

with open('in.txt') as f:
  lines = f.read().splitlines()

points = Counter()
for line in lines:
  startx, starty, endx, endy = parse('{:d},{:d} -> {:d},{:d}', line)
  if startx == endx:
    starty, endy = min(starty, endy), max(starty, endy)
    points += Counter(zip(repeat(startx), range(starty, endy + 1)))
  elif starty == endy:
    startx, endx = min(startx, endx), max(startx, endx)
    points += Counter(zip(range(startx, endx + 1), repeat(starty)))
    
print(len([elem for elem, cnt in points.items() if cnt > 1]))
