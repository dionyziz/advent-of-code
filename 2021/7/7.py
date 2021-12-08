with open('in.txt') as f:
  crabs = sorted(map(int, f.read().split(',')))
print(sum([abs(crab - crabs[len(crabs) // 2]) for crab in crabs]))
