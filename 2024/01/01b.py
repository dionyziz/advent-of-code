from collections import Counter

with open('in.txt') as f:
  lines = f.readlines()

lines = [(int(num) for num in pair.split()) for pair in lines]
lists = list(zip(*lines))
first = lists[0]
second = Counter(lists[1])

print(sum(num * second[num] for num in first))
