from itertools import product

with open('in2.txt') as f:
  nums = set(map(int, f.readlines()))

for x, y in product(nums, nums):
  if 2020 - (x + y) in nums:
    print(x * y * (2020 - (x + y)))
    break
