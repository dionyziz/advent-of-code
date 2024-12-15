with open('in.txt') as f:
  data = f.read()

board, moves = data.split('\n\n')
moves = moves.strip().replace('\n', '')
board = [list(row.strip()) for row in board.split('\n')]

for y, row in enumerate(board):
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

  nx, ny = x + dx, y + dy
  while board[ny][nx] == 'O':
    nx, ny = nx + dx, ny + dy
  if board[ny][nx] == '#':
    return x, y
  assert board[ny][nx] == '.'
  board[y][x] = '.'
  x, y = x + dx, y + dy
  board[ny][nx] = 'O'
  board[y][x] = '@'
  return x, y

for move in moves:
  pos = evolve(board, move, pos)

s = 0
for y, row in enumerate(board):
  for x, cell in enumerate(row):
    if cell == 'O':
      s += 100 * y + x
print(s)
