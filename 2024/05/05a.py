from itertools import combinations

with open('in.txt') as f:
  data = f.read()

rules, updates = data.split('\n\n')
rules = rules.split('\n')
rules = set([tuple(int(v) for v in rule.split('|')) for rule in rules])
updates = updates.split('\n')
updates = [[int(v) for v in update.split(',')] for update in updates]

def topo(update):
  for u, v in combinations(update, 2):
    if (v, u) in rules:
      return False
  return True

s = 0
for update in updates:
  if topo(update):
    s += update[len(update) // 2]

print(s)
