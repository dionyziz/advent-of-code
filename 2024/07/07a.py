with open('in.txt') as f:
  lines = [line.strip() for line in f.readlines()]

sum = 0
for line in lines:
  test, eqn = line.split(': ')
  test = int(test)
  nums = [int(num) for num in eqn.split(' ')]

  for b in range(1 << (len(nums) - 1)):
    total = nums[0]
    for i in range(len(nums) - 1):
      if b & (1 << i):
        total += nums[i + 1]
      else:
        total *= nums[i + 1]

    if total == test:
      sum += test
      break

print(sum)