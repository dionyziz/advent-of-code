with open('in.txt') as f:
  crabs = list(map(int, f.read().split(',')))

best = float('inf')
for x in range(min(crabs), max(crabs) + 1):
  cost = 0
  for crab in crabs:
    target = abs(crab - x)
    cost += target * (target + 1) // 2
  best = min(cost, best)

print(best)
