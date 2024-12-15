from collections import defaultdict
from itertools import permutations

with open('in.txt') as f:
  board = [line.strip() for line in f.readlines()]

loc = defaultdict(list)
for y, row in enumerate(board):
  for x, c in enumerate(row):
    if c != '.':
      loc[c].append(x + y * 1j)

visited = set()
for c, pts in loc.items():
  for a, b in permutations(pts, 2):
    q = 2*b - a
    if 0 <= q.real < len(board[0]) and 0 <= q.imag < len(board):
      visited.add(q)

print(len(visited))