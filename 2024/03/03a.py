import re

with open('in.txt') as f:
  memory = f.read()

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)

res = sum([int(a) * int(b) for a, b in matches])
print(res)