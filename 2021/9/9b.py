with open('in.txt') as f:
  lines = f.read().splitlines()

board = [list(map(int, line)) for line in lines]

lows = set()
for y, row in enumerate(board):
  for x, cell in enumerate(row):
    neighbours = set()
    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
      try:
        neighbours.add(board[y + dy][x + dx])
      except IndexError:
        pass
    if all([neighbour > cell for neighbour in neighbours]):
      lows.add((x, y))

visited = set()
basin_sizes = []

for x, y in lows:
  if (x, y) not in visited:
    s = [(x, y)]
    visited.add((x, y))

    cnt = 0
    while s:
      x, y = s.pop()
      cnt += 1
      for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
        try:
          if board[y + dy][x + dx] == 9 or board[y + dy][x + dx] <= board[y][x]:
            continue
        except IndexError:
          continue
        if (x + dx, y + dy) not in visited:
          s.append((x + dx, y + dy))
          visited.add((x + dx, y + dy))
    
    basin_sizes.append(cnt)

top = sorted(basin_sizes)[-3:]
print(top[0] * top[1] * top[2])
