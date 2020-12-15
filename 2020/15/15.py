from collections import defaultdict

with open('in.txt') as f:
  nums = list(map(int, f.read().split(',')))

num_turns = defaultdict(list)
for turn, num in enumerate(nums):
  num_turns[num].append(turn + 1)
num = nums[-1]

INTERESTING = 2020, 30000000

for turn in range(len(nums) + 1, INTERESTING[-1] + 1):
  prev_turns = num_turns[num]
  try:
    num = prev_turns[-1] - prev_turns[-2]
  except:
    num = 0
  num_turns[num].append(turn)
  if turn in INTERESTING:
    print(num)
