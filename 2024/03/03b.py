import re

with open('in.txt') as f:
  memory = f.read()

matches = re.findall(r'(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)', memory)

sum = 0
enabled = True
for match in matches:
  if match[3]: # do
    enabled = True
  elif match[4]: # don't
    enabled = False
  elif enabled:
    sum += int(match[1]) * int(match[2])

print(sum)
