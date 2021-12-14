from collections import Counter

with open('in.txt') as f:
  template, rules = f.read().split('\n\n')
rules = rules.split('\n')[:-1]

def step(str):
  ret = ''
  for i in range(len(str) - 1):
    lookup = str[i:i + 2]
    ret += str[i] + apply[lookup]
  ret += str[-1]
  return ret

apply = {}
for rule in rules:
  left, right = rule.split(' -> ')
  apply[left] = right

for i in range(10):
  template = step(template)

z = Counter(template)
x = z.most_common()
print(x[0][1] - x[-1][1])
