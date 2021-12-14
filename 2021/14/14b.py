from collections import Counter
from itertools import pairwise

with open('in.txt') as f:
  template, rules = f.read().split('\n\n')
rules = rules[:-1]

def step(parts):
  new_parts = Counter()
  for part, cnt in parts.items():
    mid = apply[part]
    new_parts[(part[0], mid)] += cnt
    new_parts[(mid, part[1])] += cnt
  return new_parts

apply = {}
rules = rules.split('\n')
for rule in rules:
  left, right = rule.split(' -> ')
  apply[tuple(left)] = right

parts = Counter(pairwise(template))
for _ in range(40):
  parts = step(parts)

final = Counter([template[0], template[-1]])
for (a, b), cnt in parts.items():
  final[a] += cnt
  final[b] += cnt

x = final.most_common()
print(x[0][1]//2 - x[-1][1]//2)
