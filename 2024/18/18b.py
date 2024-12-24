from collections import defaultdict, deque

W = H = 70 + 1
with open('in.txt') as f:
  lines = f.readlines()
points = list(tuple(int(i) for i in line.split(',')) for line in lines)

def reachable(obstacles):
  board = defaultdict(lambda: '.')
  for pt in obstacles:
    x, y = pt
    board[x + y * 1j] = '#'

  def bfs(s, t):
    q = deque([s])
    visited = set()
    while q:
      pt = q.pop()
      if pt in visited:
        continue
      visited.add(pt)
      if pt == t:
        return True
      for delta in 1, -1, 1j, -1j:
        n = pt + delta
        if 0 <= n.real < W and 0 <= n.imag < H and board[n] == '.':
          q.appendleft(n)
    return False

  return bfs(0, W - 1 + (H - 1) * 1j)

# invariant: first unreachable point pt is in [lo, hi)
lo, hi = 0, len(points)
while lo < hi:
  mid = (lo + hi) // 2
  if reachable(points[:mid]):
    lo = mid + 1
  else:
    hi = mid
assert reachable(points[:lo - 1]) and not reachable(points[:lo])

print(','.join(map(str, points[lo - 1])))