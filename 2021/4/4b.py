from sys import exit
from collections import Counter

with open('in.txt') as f:
  file = f.read()

draws, *boards = file.split('\n\n')
draws = map(int, draws.split(','))

boards = [
  [
    [int(cell) for cell in row.split(' ') if cell != '']
    for row in board.split('\n')
  ]
  for board in boards
]

board_dicts = []
for board in boards:
  board_dict = {
    cell: (x, y)
    for y, row in enumerate(board)
    for x, cell in enumerate(row)
  }
  board_dicts.append((board_dict, Counter(), Counter()))

won = set()
for draw in draws:
  for idx, (board_dict, rows, cols) in enumerate(board_dicts):
    try:
      row, col = board_dict[draw]
    except KeyError:
      continue
    rows[row] += 1
    cols[col] += 1
    del board_dict[draw]
    if rows[row] == len(boards[0][0]) or cols[col] == len(boards[0][0]):
      won.add(idx)
      if len(won) == len(boards):
        print(sum(board_dict) * draw)
        exit()
