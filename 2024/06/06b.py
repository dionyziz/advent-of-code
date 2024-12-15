with open('in.txt') as f:
  lines = [line.strip() for line in f.readlines()]

board = {}
for y, line in enumerate(lines):
  for x, c in enumerate(line):
    idx = x - y * 1j
    if c == '^':
      pos = idx
      dir = 1j
    board[idx] = c

def loops(board, pos, dir):
  visited = set()
  while True:
    if (pos, dir) in visited:
      return True
    visited.add((pos, dir))
    new_pos = pos + dir
    if new_pos not in board:
      break
    if board[new_pos] == '#':
      dir *= -1j
      continue
    pos = new_pos
  return False

cnt = 0
for y in range(len(lines)):
  for x in range(len(lines[0])):
    idx = x - y * 1j
    if board[idx] == '.':
      board[idx] = '#'
      cnt += loops(board, pos, dir)
      board[idx] = '.'

print(cnt)