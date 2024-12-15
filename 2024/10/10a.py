with open('in.txt') as f:
  board = [list(map(int, line.strip())) for line in f.readlines()]

def score(board, x, y):
  ret = 0

  visited = set((x, y))
  frontier = [(x, y)]

  while frontier:
    x, y = frontier.pop()

    if (x, y) in visited:
      continue

    visited.add((x, y))

    if board[y][x] == 9:
      ret += 1
      continue

    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
      if 0 <= x + dx < len(board[0]) and 0 <= y + dy < len(board):
        if board[y + dy][x + dx] == board[y][x] + 1:
          frontier.append((x + dx, y + dy))

  return ret

tot = 0
for y in range(len(board)):
  for x in range(len(board[0])):
    if board[y][x] == 0:
      tot += score(board, x, y)
print(tot)