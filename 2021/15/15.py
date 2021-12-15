from heapq import heappop, heappush

with open('in.txt') as f:
  board = [[int(cell) for cell in line] for line in f.read().splitlines()]

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
