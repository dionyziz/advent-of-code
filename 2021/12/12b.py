from collections import Counter, defaultdict

with open('in.txt') as f:
  lines = f.read().splitlines()

G = defaultdict(set)

for line in lines:
  start, end = line.split('-')
  G[start].add(end)
  G[end].add(start)

def good(path):
  most_visited = path.most_common(2)
  return most_visited[0][1] + most_visited[1][1] <= 3

def paths(G, start, path):
  for neighbor in G[start]:
    if neighbor == 'end':
      yield
      continue
    if neighbor == 'start':
      continue
    new_path = Counter(path)
    if neighbor.islower():
      new_path += Counter([neighbor])
    if neighbor.isupper() or good(new_path):
      yield from paths(G, neighbor, new_path)

print(len(list(paths(G, 'start', Counter(['start'])))))
