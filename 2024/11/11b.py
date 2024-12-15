import functools

with open('in.txt') as f:
  nums = [int(num) for num in f.read().split(' ')]

@functools.cache
def count(num, iters):
  if iters == 0:
    return 1
  if num == 0:
    return count(1, iters - 1)
  s = str(num)
  l = len(s)
  if l % 2 == 0:
    return count(int(s[:l//2]), iters - 1) + count(int(s[l//2:]), iters - 1)
  return count(num * 2024, iters - 1)

print(sum([count(num, 75) for num in nums]))
