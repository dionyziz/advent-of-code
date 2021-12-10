with open('in.txt') as f:
  lines = f.read().splitlines()

inv = {')': '(', '}': '{', ']': '[', '>': '<'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}

def error(line):
  s = []
  for char in line:
    if char in ('(', '{', '[', '<'):
      s.append(char)
    elif len(s) == 0 or s.pop() != inv[char]:
      return score[char]
  return 0

print(sum(map(error, lines)))
