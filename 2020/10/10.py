from collections import defaultdict, Counter

with open('in.txt') as f:
  lines = list(map(int, f.read().splitlines()))

lines.sort()
diffs = Counter({3: 1})
prev = 0
for line in lines:
  diffs[line - prev] += 1
  prev = line

print(diffs[1] * diffs[3])

cnt = defaultdict(int)
cnt[0] = 1
for line in lines:
  cnt[line] = cnt[line - 1] + cnt[line - 2] + cnt[line - 3]

print(cnt[lines[-1]])
