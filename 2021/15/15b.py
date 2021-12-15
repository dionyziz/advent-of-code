import numpy as np
from heapq import heappop, heappush

with open('small.txt') as f:
  tile = np.array([[int(cell) for cell in line] for line in f.read().splitlines()])

board = []
for y in range(5):
  row = []
  for x in range(5):
    next_tile = (tile + (x + y)) % 9
    next_tile = np.where(next_tile == 0, 9, next_tile)
    row.append(next_tile)
  board.append(row)
board = np.block(board)

def dijkstra(board, start, end):
  (sx, sy) = start
  visited = set()
  frontier = [(0, sx, sy)]

  while frontier:
    cost, x, y = heappop(frontier)
    if (x, y) in visited:
      continue
    if (x, y) == end:
      return cost
    visited.add((x, y))

    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
      if 0 <= x + dx < len(board[0]) and 0 <= y + dy < len(board) and (x + dx, y + dy) not in visited:
        heappush(frontier, (cost + board[y + dy][x + dx], x + dx, y + dy))
  
  return None

print(dijkstra(board, (0, 0), (len(board[0]) - 1, len(board) - 1)))
