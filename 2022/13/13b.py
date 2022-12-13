from functools import cmp_to_key
from json import loads

with open('input') as f:
  lines = f.read().strip().split('\n\n')

def compare(a, b):
  if isinstance(a, int):
    if isinstance(b, int):
      return a - b
    return compare([a], b)
  if isinstance(b, int):
    return compare(a, [b])
  for p, q in zip(a, b):
    c = compare(p, q)
    if c != 0:
      return c
  return len(a) - len(b)

l = [[[2]], [[6]]]

for i, line in enumerate(lines):
  a, b = line.strip().splitlines()
  l.append(loads(a))
  l.append(loads(b))

l.sort(key=cmp_to_key(compare))
r = l.index([[2]]) + 1
s = l.index([[6]]) + 1
print(r * s)
