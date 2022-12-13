import numpy as np

with open('in.txt') as f:
  lines = f.read().strip().splitlines()

s = set([0])
h = 10 * [0]

for line in lines:
  dir, cnt = line.split()
  cnt = int(cnt)
  for _ in range(cnt):
    h[0] += {
      'U': -1j,
      'D': 1j,
      'R': 1,
      'L': -1
    }[dir]
    for i in range(9):
      if abs(h[i + 1] - h[i]) < 2:
        break
      delta = h[i] - h[i + 1]
      h[i + 1] += np.sign(delta.real) + 1j * np.sign(delta.imag)
    s.add(h[-1])

print(len(s))
