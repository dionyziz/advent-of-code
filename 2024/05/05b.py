from collections import defaultdict
from heapq import heappush, heappop

with open('in.txt') as f:
  data = f.read()

rules, updates = data.split('\n\n')
rules = rules.split('\n')
rules = set([tuple(int(v) for v in rule.split('|')) for rule in rules])
updates = updates.split('\n')
updates = [[int(v) for v in update.split(',')] for update in updates]

def subgraph(G, V):
  G_sub = {}
  for u in G:
    if u in V:
      G_sub[u] = set()
      for v in G[u]:
        if v in V:
          G_sub[u].add(v)
  return G_sub

def nodes(G):
  V = set()
  for u in G:
    V.add(u)
    for v in G[u]:
      V.add(v)
  return V

def toposort(G):
  visited = set()

  V = nodes(G)
  degree = defaultdict(int)
  for u in G:
    for v in G[u]:
      degree[v] += 1
  heap = []
  for u in V:
    heappush(heap, (degree[u], u))

  while heap:
    _, u = heappop(heap)

    if u not in visited:
      yield u
      visited.add(u)

      for v in G[u]:
        degree[v] -= 1
        heappush(heap, (degree[v], v))

G = {}

for u, v in rules:
  G[u] = set()
  G[v] = set()

for u, v in rules:
  G[u].add(v)

s = 0
for V in updates:
  G_sub = subgraph(G, V)
  toposorted = list(toposort(G_sub))
  if V != toposorted:
    s += toposorted[len(toposorted) // 2]

print(s)