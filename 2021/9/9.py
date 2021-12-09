with open('in.txt') as f:
  lines = f.read().splitlines()

board = [list(map(int, line)) for line in lines]

cnt = 0
for y, row in enumerate(board):
  for x, cell in enumerate(row):
    neighbours = set()
    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
      try:
        neighbours.add(board[y + dy][x + dx])
      except IndexError:
        pass
    if all([neighbour > cell for neighbour in neighbours]):
      cnt += cell + 1
print(cnt)
