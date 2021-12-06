from collections import Counter

with open('in.txt') as f:
  fishes = Counter(map(int, f.read().splitlines().pop().split(',')))

for i in range(256):
  new_fishes = Counter()
  for fish, cnt in fishes.items():
    if fish == 0:
      new_fishes[6] += cnt
      new_fishes[8] += cnt
    else:
      new_fishes[fish - 1] += cnt
  fishes = new_fishes

print(fishes.total())
