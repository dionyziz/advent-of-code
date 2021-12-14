from collections import Counter

with open('in.txt') as f:
  template, rules = f.read().split('\n\n')

rules = rules[:-1]

def step(first, parts, last):
  new_parts = Counter()
  for part, cnt in parts.most_common():
    mid = apply[part]
    new_parts[part[0] + mid] += cnt
    new_parts[mid + part[1]] += cnt
  return first[0] + apply[first], new_parts, apply[last] + last[-1]

apply = {}
rules = rules.split('\n')
for rule in rules:
  left, right = rule.split(' -> ')
  apply[left] = right

first = template[0:2]
last = template[-2:]
parts = Counter()
for i in range(len(template) - 1):
  parts[template[i:i + 2]] += 1

for i in range(40):
  first, parts, last = step(first, parts, last)

final = Counter()
for part, cnt in parts.most_common():
  final[part[0]] += cnt
  final[part[1]] += cnt
final[first[0]] += 1
final[last[-1]] += 1

x = final.most_common()
print(x[0][1]//2 - x[-1][1]//2)
