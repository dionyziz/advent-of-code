from collections import defaultdict
from heapq import heappush, heappop

with open('in.txt') as f:
  data = f.readlines()

board = {}
for y, line in enumerate(data):
  for x, c in enumerate(line):
    board[x + y * 1j] = c
    if c == 'S':
      start = x + y * 1j
    elif c == 'E':
      end = x + y * 1j

def dijkstra(start, v):
  locs = [(start, v)]
  frontier = [(0, 0, None)]
  parents = defaultdict(list)
  costs = defaultdict(lambda: float('inf'))

  while frontier:
    cost, i, parent = heappop(frontier)
    pos, v = locs[i]

    if cost > costs[(pos, v)]:
      continue

    if parent:
      parents[(pos, v)].append(parent)

    costs[(pos, v)] = cost

    if board[pos] == 'E':
      continue

    npos = pos + v
    if npos in board:
      if board[npos] in ('.', 'E'):
        heappush(frontier, (cost + 1, len(locs), (pos, v)))
        locs.append((npos, v))

    for dv in 1j, -1j:
      heappush(frontier, (cost + 1000, len(locs), (pos, v)))
      locs.append((pos, dv * v))

  tiles = set()
  pending = []
  best_cost = float('inf')
  for v in 1, -1, 1j, -1j:
    if costs[(end, v)] < best_cost:
      best_cost = costs[(end, v)]
  for v in 1, -1, 1j, -1j:
    if costs[(end, v)] == best_cost:
      pending.append((end, v))

  visited = set()
  while pending:
    pos, v = pending.pop()
    if (pos, v) in visited:
      continue
    visited.add((pos, v))
    tiles.add(pos)

    for parent in parents[(pos, v)]:
      pending.append(parent)

  return tiles

print(len(dijkstra(start, 1)))