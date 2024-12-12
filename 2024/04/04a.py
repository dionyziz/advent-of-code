import sys

with open('in.txt') as f:
  board = [[c for c in line.strip()] for line in f.readlines()]

def get_candidates_E(board):
  candidates = []
  for line in board:
    for j, _ in enumerate(line[:-3]):
      candidates.append(list(line[j:j+4]))

  return candidates

def get_candidates_W(board):
  return get_candidates_E(zip(*(list(zip(*board))[::-1])))

def get_candidates_S(board):
  return get_candidates_E(zip(*board))

def get_candidates_N(board):
  return get_candidates_S(board[::-1])

def get_candidates_SE(board):
  candidates = []
  for i, line in enumerate(board[:-3]):
    for j, _ in enumerate(line[:-3]):
      candidate = []
      for k in range(4):
        candidate.append(board[i+k][j+k])
      candidates.append(candidate)

  return candidates

def get_candidates_SW(board):
  return get_candidates_SE(list(zip(*(list(zip(*board))[::-1]))))

def get_candidates_NE(board):
  return get_candidates_SE(board[::-1])

def get_candidates_NW(board):
  return get_candidates_SW(board[::-1])

candidates = get_candidates_N(board) +\
             get_candidates_NE(board) +\
             get_candidates_E(board) +\
             get_candidates_SE(board) +\
             get_candidates_S(board) +\
             get_candidates_SW(board) +\
             get_candidates_W(board) +\
             get_candidates_NW(board)

cnt = 0
for candidate in candidates:
  if ''.join(candidate) == 'XMAS':
    cnt += 1

print(cnt)