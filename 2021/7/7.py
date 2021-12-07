with open('in.txt') as f:
  crabs = list(map(int, f.read().split(',')))

best = float('inf')
for x in range(min(crabs), max(crabs) + 1):
  cost = 0
  for crab in crabs:
    cost += abs(crab - x)
  best = min(cost, best)

print(best)
