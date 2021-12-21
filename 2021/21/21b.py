from itertools import product
from functools import cache

@cache
def cnt(p, s, mover):
  if s[0] >= 21:
    return [1, 0]
  if s[1] >= 21:
    return [0, 1]
  c = [0, 0]
  for d in product((1, 2, 3), repeat=3):
    pp = [p[0], p[1]]
    pp[mover] = (pp[mover] + sum(d) - 1) % 10 + 1
    ss = [s[0], s[1]]
    ss[mover] += pp[mover]

    a, b = cnt(tuple(pp), tuple(ss), not mover)
    c[0] += a
    c[1] += b
  return c

p = (5, 8)

print(max(cnt(p, (0, 0), 0)))
