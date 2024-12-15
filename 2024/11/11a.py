with open('in.txt') as f:
  nums = [int(num) for num in f.read().split(' ')]

def evolve(nums):
  new = []
  for num in nums:
    if num == 0:
      new.append(1)
      continue
    if len(str(num)) % 2 == 0:
      new.append(int(str(num)[:len(str(num)) // 2]))
      new.append(int(str(num)[len(str(num)) // 2:]))
      continue
    new.append(num * 2024)
  return new

for i in range(25):
  nums = evolve(nums)

print(len(nums))
