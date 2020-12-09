from collections import Counter
from itertools import permutations
import sys

with open('in.txt') as f:
  lines = list(map(int, f.read().splitlines()))

PREAMBLE = 25
for i, num in enumerate(lines[PREAMBLE:]):
  sums = map(sum, permutations(set(lines[i:i+PREAMBLE]), r=2))
  if num not in sums:
    target = num
    break

print(target)

for l in range(2, len(lines) + 1):
  s = Counter(lines[:l])
  window = sum(lines[:l])
  for next, prev in zip(lines[l:], lines[:-l]):
    window += next - prev
    s[next] += 1
    s[prev] -= 1
    if window == target:
      s += Counter()
      print(min(s.keys()) + max(s.keys()))
      break
