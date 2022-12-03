with open('in.txt') as f:
  lines = [set(line) for line in f.read().strip().split('\n')]

total = 0
for knapsacks in zip(lines[::3], lines[1::3], lines[2::3]):
  common = ord((set.intersection(*knapsacks)).pop())
  if ord('a') <= common <= ord('z'):
    score = common - ord('a') + 1
  else:
    score = common - ord('A') + 27
  total += score
print(total)
