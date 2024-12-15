from parse import parse
from math import prod

with open('in.txt') as f:
  lines = f.read().splitlines()

ITERATIONS = 1000000
MAX_X = 101
MAX_Y = 103

pos = []
vel = []
for line in lines:
  px, py, vx, vy = parse("p={:d},{:d} v={:d},{:d}", line)
  pos.append([px, py])
  vel.append([vx, vy])

for iter in range(ITERATIONS):
  for i in range(len(pos)):
    pos[i][0] += vel[i][0]
    pos[i][0] %= MAX_X
    pos[i][1] += vel[i][1]
    pos[i][1] %= MAX_Y

  marked = set()
  board = []

  for y in range(MAX_Y):
    board.append([])
    for x in range(MAX_X):
      board[y].append('.')

  for x, y in pos:
    board[y][x] = '#'

  max_cnt = 0
  for y in range(MAX_Y):
    for x in range(MAX_X):
      if (x, y) not in marked and board[y][x] == '#':
        visited = set()
        frontier = [(x, y)]
        while frontier:
          x, y = frontier.pop()
          if (x, y) in visited:
            continue
          visited.add((x, y))
          for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
              nx, ny = x + dx, y + dy
              if 0 <= nx < MAX_X and 0 <= ny < MAX_Y:
                if board[ny][nx] == '#':
                  frontier.append((nx, ny))
        max_cnt = max(max_cnt, len(visited))
        marked.update(visited)

  if max_cnt > 100:
    print(iter + 1)
    break