with open('in.txt') as f:
  lines = f.read().splitlines()

inv = {')': '(', '}': '{', ']': '[', '>': '<'}
score = {'(': 1, '[': 2, '{': 3, '<': 4}

def error(line):
  s = []
  for char in line:
    if char in ('(', '{', '[', '<'):
      s.append(char)
    elif len(s) == 0 or s.pop() != inv[char]:
      return None
  return s

values = []
for line in lines:
  s = error(line)
  if s is not None:
    value = 0
    for t in s[::-1]:
      value *= 5
      value += score[t]
    values.append(value)

print(sorted(values)[len(values)//2])
