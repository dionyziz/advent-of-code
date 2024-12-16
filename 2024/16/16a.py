from heapq import heappush, heappop
from collections import defaultdict

with open('sample2.txt') as f:
  data = f.readlines()

board = {}
for y, line in enumerate(data):
  for x, c in enumerate(line):
    board[x + y * 1j] = c
    if c == 'S':
      start = x + y * 1j

def dijkstra(start, v):
  locs = [(start, v)]
  frontier = [(0, 0)]
  costs = defaultdict(lambda: float('inf'))

  while frontier:
    cost, i = heappop(frontier)
    pos, v = locs[i]

    if cost > costs[(pos, v)]:
      continue
    costs[(pos, v)] = cost

    if board[pos] == 'E':
      return cost

    npos = pos + v
    if npos in board:
      if board[npos] in ('.', 'E'):
        heappush(frontier, (cost + 1, len(locs)))
        locs.append((npos, v))

    for dv in 1j, -1j:
      heappush(frontier, (cost + 1000, len(locs)))
      locs.append((pos, dv * v))

print(dijkstra(start, 1))