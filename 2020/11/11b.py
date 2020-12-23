from copy import deepcopy
from collections import Counter

with open('in.txt') as f:
  prev_board = list(map(list, f.read().splitlines()))

while True:
  board = deepcopy(prev_board)
  for y, line in enumerate(prev_board):
    for x, char in enumerate(line):
      cnt = 0
      for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
          if dx == 0 and dy == 0:
            continue
          yy = y + dy
          xx = x + dx
          while 0 <= yy < len(board) and 0 <= xx < len(board[0]):
            if prev_board[yy][xx] == '#':
              cnt += 1
              break
            if prev_board[yy][xx] == 'L':
              break
            yy += dy
            xx += dx
      if char == 'L' and cnt == 0:
        board[y][x] = '#'
      if char == '#' and cnt >= 5:
        board[y][x] = 'L'
  if board == prev_board:
    break
  prev_board = board

print(sum(line.count('#') for line in board))
