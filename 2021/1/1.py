with open('in.txt') as f:
  nums = list(map(int, f.read().splitlines()))

increases = [x > y for x, y in zip(nums[1:], nums)]
print(sum(increases))
