from itertools import product
from collections import defaultdict
from pprint import pprint

with open('in.txt') as f:
  connections = [line.strip().split('-') for line in f.readlines()]

nodes = set()
G = defaultdict(list)
for left, right in connections:
  nodes.add(left)
  nodes.add(right)
  G[left].append(right)
  G[right].append(left)

head_nodes = [node for node in nodes if node[0] == 't']

sets = set()
for v in head_nodes:
  for u in G[v]:
    for w in G[u]:
      if w != v and v in G[w]:
        sets.add(frozenset([v, u, w]))

pprint(len(sets))
