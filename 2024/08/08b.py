from collections import defaultdict
from itertools import combinations
from math import gcd

with open('in.txt') as f:
  board = [line.strip() for line in f.readlines()]

loc = defaultdict(list)
for y, row in enumerate(board):
  for x, c in enumerate(row):
    if c != '.':
      loc[c].append(x + y * 1j)

visited = set()
for c, pts in loc.items():
  for a, b in combinations(pts, 2):
    q = b - a
    g = gcd(int(q.real), int(q.imag))
    q = int(q.real) // g + int(q.imag) // g * 1j
    if q.real < 0:
      q = -q

    for x in range(len(board[0])):
      for y in range(len(board)):
        if (x - a.real) % q.real == 0 and (y - a.imag) % q.imag == 0:
          if (x - a.real) // q.real == (y - a.imag) // q.imag:
            visited.add(x + y * 1j)

print(len(visited))