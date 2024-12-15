from collections import deque

with open('in.txt') as f:
  data = f.read()

board, moves = data.split('\n\n')
moves = moves.strip().replace('\n', '')
board = [row.strip() for row in board.split('\n')]

for y, row in enumerate(board):
  row = list(row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
  board[y] = row
  for x, cell in enumerate(row):
    if cell == '@':
      pos = (x, y)
      break

def evolve(board, move, start):
  x, y = start
  dx, dy = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
  }[move]

  visited = set()
  push = []
  frontier = deque([start])
  possible = True

  while frontier:
    x, y = frontier.pop()

    if (x, y) in visited:
      continue
    if not (0 <= x < len(board[0]) and 0 <= y < len(board)):
      continue

    visited.add((x, y))
    push.append((x, y))

    if board[y][x] == '#':
      possible = False
      break
    if board[y][x] == '[':
      frontier.appendleft((x + 1, y))
    if board[y][x] == ']':
      frontier.appendleft((x - 1, y))
    if board[y][x] != '.':
      frontier.appendleft((x + dx, y + dy))

  if possible:
    for x, y in push[::-1]:
      if board[y][x] != '.':
        board[y + dy][x + dx] = board[y][x]
        board[y][x] = '.'
    return (x + dx, y + dy)
  return start

for move in moves:
  pos = evolve(board, move, pos)

s = 0
for y, row in enumerate(board):
  for x, cell in enumerate(row):
    if cell == '[':
      s += 100 * y + x
print(s)
