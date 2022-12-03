with open('in.txt') as f:
  lines = f.read().strip().split('\n')

total = 0
for line in lines:
  left, right = line[:len(line)//2], line[len(line)//2:]
  common = ord((set(left) & set(right)).pop())
  if ord('a') <= common <= ord('z'):
    score = common - ord('a') + 1
  else:
    score = common - ord('A') + 27
  total += score
print(total)
