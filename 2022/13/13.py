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

c = 0
for i, line in enumerate(lines):
  a, b = line.strip().splitlines()
  a = loads(a)
  b = loads(b)
  if compare(a, b) < 0:
    c += i + 1
print(c)
