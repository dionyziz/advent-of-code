from parse import parse
from collections import deque

with open('input') as f:
  instructions = f.read().strip().split('\n\n')

state = []
for instruction in instructions:
  monkey = parse('Monkey {:d}:' +\
                 '{:s}Starting items: {items}' +\
                 '{:s}Operation: new = {left:w} {op:S} {right:w}' +\
                 '{:s}Test: divisible by {divisor:d}' +\
                 '{:s}If true: throw to monkey {toT:d}' +\
                 '{:s}If false: throw to monkey {toF:d}',
                 instruction).named

  monkey['items'] = deque(map(int, monkey['items'].split(', ')))
  if monkey['left'] != 'old':
    monkey['left'] = int(monkey['left'])
  if monkey['right'] != 'old':
    monkey['right'] = int(monkey['right'])
  monkey['inspections'] = 0

  state.append(monkey)

for round in range(20):
  for monkey in state:
    while monkey['items']:
      monkey['inspections'] += 1
      item = monkey['items'].popleft()
      left, op, right = monkey['left'], monkey['op'], monkey['right']
      if left == 'old':
        left = item
      if right == 'old':
        right = item
      new = {'+': left + right,
             '*': left * right}[op] // 3
      if new % monkey['divisor'] == 0:
        state[monkey['toT']]['items'].append(new)
      else:
        state[monkey['toF']]['items'].append(new)

performers = sorted(state, key=lambda x: x['inspections'], reverse=True)
print(performers[0]['inspections'] * performers[1]['inspections'])
