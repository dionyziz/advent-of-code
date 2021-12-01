with open('in.txt') as f:
  nums = list(map(int, f.read().splitlines()))

windows = list(map(sum, zip(nums, nums[1:], nums[2:])))
increases = [x - y > 0 for (x, y) in zip(windows[1:], windows)]
print(sum(increases))
