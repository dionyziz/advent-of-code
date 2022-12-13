with open('in.txt') as f:
  lines = f.read().strip().splitlines()

s = set([0])
h, t = 0, 0

for line in lines:
  dir, cnt = line.split()
  cnt = int(cnt)
  for _ in range(cnt):
    prev = h
    h += {
      'U': -1j,
      'D': 1j,
      'R': 1,
      'L': -1
    }[dir]
    if abs(t - h) >= 2:
      t = prev
      s.add(t)

print(len(s))
