import re
from collections import defaultdict, Counter

with open('in.txt') as f:
  lines = f.read().splitlines()

G1 = defaultdict(list)
G2 = defaultdict(list)
for line in lines:
  child, parents = line.split(' bags contain ')
  if not parents.startswith('no other'):
    for parent in parents.split(', '):
      count, parent = re.match(r'(\d+) (.*) bag', parent).group(1, 2)
      G1[parent].append((child, int(count)))
      G2[child].append((parent, int(count)))

def search(G, root):
  q = [(root, 1)]
  visited = Counter()
  while q:
    item, multiplier = q.pop()
    visited[item] += multiplier
    for child, weight in G[item]:
      q.append((child, weight * multiplier))
  return visited

root = 'shiny gold'
print(len(search(G1, root)) - 1)
print(sum(search(G2, root).values()) - 1)
