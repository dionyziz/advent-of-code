from collections import deque

with open('input') as f:
  lines = f.read().strip().splitlines()

G = []
start = None
for y, line in enumerate(lines):
  G.append([])
  for x, c in enumerate(line):
    if c == 'S':
      c = 'a'
    elif c == 'E':
      start = x, y
      c = 'z'
    G[y].append(ord(c) - ord('a'))

def BFS(G, pos):
  q = deque([(pos, 0)])
  seen = set([pos])
  while q:
    (x, y), d = q.popleft()
    if G[y][x] == 0:
      return d
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
      nx, ny = x + dx, y + dy
      if (nx, ny) in seen:
        continue
      if 0 <= nx < len(G[0]) and 0 <= ny < len(G):
        if G[y][x] > G[ny][nx] + 1:
          continue
        seen.add((nx, ny))
        q.append(((nx, ny), d + 1))

print(BFS(G, start))
