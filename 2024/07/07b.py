with open('in.txt') as f:
  lines = [line.strip() for line in f.readlines()]

sum = 0
for line in lines:
  test, eqn = line.split(': ')
  test = int(test)
  nums = [int(num) for num in eqn.split(' ')]

  for b in range(3 ** (len(nums) - 1)):
    total = nums[0]
    for i in range(len(nums) - 1):
      if b % 3 == 0:
        total += nums[i + 1]
      elif b % 3 == 1:
        total *= nums[i + 1]
      elif b % 3 == 2:
        total = int(str(total) + str(nums[i + 1]))
      b //= 3

    if total == test:
      sum += test
      break

print(sum)