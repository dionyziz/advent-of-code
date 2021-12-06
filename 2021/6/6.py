with open('in.txt') as f:
  fishes = map(int, f.read().split(','))

for i in range(80):
  new_fishes = []
  for fish in fishes:
    if fish == 0:
      new_fishes.extend([6, 8])
    else:
      new_fishes.append(fish - 1)
  fishes = new_fishes

print(len(fishes))
