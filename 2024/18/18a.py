from collections import defaultdict, deque

with open('in.txt') as f:
  lines = f.readlines()[:1024]

board = defaultdict(lambda: '.')
W = H = 70 + 1

for line in lines:
  x, y = [int(i) for i in line.split(',')]
  board[x + y * 1j] = '#'

s = 0
t = W - 1 + (H - 1) * 1j

def bfs(s, t):
  q = deque([(s, 0)])
  visited = set()
  while q:
    pt, dist = q.pop()
    if pt in visited:
      continue
    visited.add(pt)
    if pt == t:
      return dist
    for delta in 1, -1, 1j, -1j:
      n = pt + delta
      if 0 <= n.real < W and 0 <= n.imag < H:
        if board[n] == '.':
          q.appendleft((n, dist + 1))
  return None

print(bfs(s, t))