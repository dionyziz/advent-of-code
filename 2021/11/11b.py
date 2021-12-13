from pprint import pprint
from itertools import count

with open('in.txt') as f:
  board = [list(map(int, line)) for line in f.read().splitlines()]

def step(board):
  def flood(board, x, y):
    board[y][x] += 1

    if board[y][x] != 10:
      return 0

    cnt = 1
    for dx in (-1, 0, 1):
      for dy in (-1, 0, 1):
        if dx == 0 and dy == 0:
          continue
        if 0 <= x + dx < len(board[0]) and 0 <= y + dy < len(board):
          cnt += flood(board, x + dx, y + dy)
    return cnt

  cnt = 0
  for y, line in enumerate(board):
    for x, cell in enumerate(line):
      cnt += flood(board, x, y)
  
  board = [[cell if cell <= 9 else 0 for cell in line] for line in board]
    
  return (board, cnt)

target = sum([sum([1 for cell in line]) for line in board])

for i in count(1):
  board, flashes = step(board)
  if flashes == target:
    print(i)
    break
