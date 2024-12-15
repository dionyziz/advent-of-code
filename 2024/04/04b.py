from collections import Counter

with open('in.txt') as f:
  board = [line.strip() for line in f.readlines()]

def get_candidates(board, dx, dy):
  candidates = []
  for i, line in enumerate(board):
    for j, _ in enumerate(line):
      candidate = ''
      for k in range(3):
        if 0 <= i+k*dy < len(board) and 0 <= j+k*dx < len(line):
          candidate += board[i+k*dy][j+k*dx]
        else:
          break
      else:
        if candidate == 'MAS':
          candidates.append((i + dy, j + dx))

  return candidates

candidates = []
for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
  candidates += get_candidates(board, dx, dy)

print(len([c for c in Counter(candidates).most_common() if c[1] == 2]))