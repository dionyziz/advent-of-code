from collections import Counter

with open('in.txt') as f:
  board = [line.strip() for line in f.readlines()]

def get_candidates(board, dx, dy):
  candidates = []
  for i, line in enumerate(board):
    for j, _ in enumerate(line):
      candidate = ''
      for k in range(4):
        if 0 <= i+k*dy < len(board) and 0 <= j+k*dx < len(line):
          candidate += board[i+k*dy][j+k*dx]
        else:
          break
      else:
        candidates.append(candidate)

  return candidates

candidates = []
for dx in (-1, 0, 1):
  for dy in (-1, 0, 1):
    if dx != 0 or dy != 0:
      candidates += get_candidates(board, dx, dy)

print(Counter(candidates)['XMAS'])