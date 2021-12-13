from collections import defaultdict

with open('in.txt') as f:
  lines = f.read().splitlines()

G = defaultdict(set)

for line in lines:
  start, end = line.split('-')
  G[start].add(end)
  G[end].add(start)

def paths(G, start, path):
  if start == 'end':
    yield

  for neighbor in G[start]:
    if neighbor.isupper() or neighbor not in path:
      yield from paths(G, neighbor, path + [neighbor])

print(len(list(paths(G, 'start', ['start']))))
