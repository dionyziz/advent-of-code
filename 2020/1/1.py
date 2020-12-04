with open('in.txt') as f:
  nums = set(map(int, f.readlines()))

for x in nums:
  if 2020 - x in nums:
    print(x * (2020 - x))
    break
