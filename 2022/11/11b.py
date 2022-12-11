from parse import parse
from collections import deque
from operator import add, mul

with open('input') as f:
  instructions = f.read().strip().split('\n\n')

divisors = []
state = []
for instruction in instructions:
  monkey = parse('Monkey {:d}:' +\
                 '{:s}Starting items: {items}' +\
                 '{:s}Operation: new = {left:w} {op:S} {right:w}' +\
                 '{:s}Test: divisible by {divisor:d}' +\
                 '{:s}If true: throw to monkey {toT:d}' +\
                 '{:s}If false: throw to monkey {toF:d}',
                 instruction).named

  monkey['items'] = [int(item) for item in monkey['items'].split(', ')]
  if monkey['left'] != 'old':
    monkey['left'] = int(monkey['left'])
  if monkey['right'] != 'old':
    monkey['right'] = int(monkey['right'])

  state.append(monkey | {
    'ditems': deque([]),
    'inspections': 0
  })

  divisors.append(monkey['divisor'])

for monkey in state:
  for item in monkey['items']:
    d = {}
    for divisor in divisors:
      d[divisor] = item % divisor
    monkey['ditems'].append(d)

for round in range(10000):
  for j in range(len(state)):
    monkey = state[j]
    while monkey['ditems']:
      monkey['inspections'] += 1
      item = monkey['ditems'].popleft()
      op = { '+': add, '*': mul }[monkey['op']]
      for divisor in divisors:
        left, right = monkey['left'], monkey['right']
        if left == 'old':
          left = item[divisor]
        if right == 'old':
          right = item[divisor]
        item[divisor] = op(left, right) % divisor

      if item[monkey['divisor']] == 0:
        state[monkey['toT']]['ditems'].append(item)
      else:
        state[monkey['toF']]['ditems'].append(item)

performers = sorted(state, key=lambda x: x['inspections'], reverse=True)
print(performers[0]['inspections'] * performers[1]['inspections'])
