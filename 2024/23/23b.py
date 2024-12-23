from collections import defaultdict

with open('in.txt') as f:
  connections = [line.strip().split('-') for line in f.readlines()]

nodes = set()
G = defaultdict(set)
for left, right in connections:
  nodes.add(left)
  nodes.add(right)
  if left < right:
    G[left].add(right)
  else:
    G[right].add(left)

def clique(fixed, candidates, k):
  if len(fixed) == k:
    return fixed
  for candidate in candidates:
    result = clique([*fixed, candidate], candidates & G[candidate], k)
    if result:
      return result
  return None

MAX_K = 20
best_clique = []
for k in range(1, MAX_K + 1):
  for v in nodes:
    fixed = [v]
    candidates = G[v]
    result = clique(fixed, candidates, k)
    if result:
      best_clique = result
      break
  else:
    break

print(','.join(best_clique))