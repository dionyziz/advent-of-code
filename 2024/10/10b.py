from collections import deque, defaultdict

with open('in.txt') as f:
  board = [list(map(int, line.strip())) for line in f.readlines()]

def score(board, x, y):
  ret = 0

  visited = set((x, y))
  queue = deque([(x, y)])

  cnt = defaultdict(int)
  cnt[(x, y)] = 1

  while queue:
    x, y = queue.pop()

    if (x, y) in visited:
      continue
    visited.add((x, y))

    if board[y][x] == 9:
      ret += cnt[(x, y)]
      continue

    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
      if 0 <= x + dx < len(board[0]) and 0 <= y + dy < len(board):
        if board[y + dy][x + dx] == board[y][x] + 1:
          queue.appendleft((x + dx, y + dy))
          cnt[(x + dx, y + dy)] = cnt[(x + dx, y + dy)] + cnt[(x, y)]

  return ret

tot = 0
for y in range(len(board)):
  for x in range(len(board[0])):
    if board[y][x] == 0:
      tot += score(board, x, y)
print(tot)