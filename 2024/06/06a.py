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

visited = set()
while True:
  visited.add(pos)
  new_pos = pos + dir
  if new_pos not in board:
    break
  if board[new_pos] == '#':
    dir *= -1j
    continue
  pos = new_pos

print(len(visited))
