from collections import defaultdict
from parse import parse

with open('in.txt') as f:
  lines = f.read().splitlines()

def apply_mask(mask, value):
  value |= int(mask.replace('X', '0'), 2)
  value = bin(value)[2:].rjust(36, '0')
  values = ['']
  for j, x in enumerate(mask):
    if x == 'X':
      new_values = []
      for option in values:
        new_values.append(option + '0')
        new_values.append(option + '1')
      values = new_values
    else:
      for i, option in enumerate(values):
        values[i] += value[j]

  return values

mask = 0
mem = defaultdict(int)
for line in lines:
  var, value = line.split(' = ')
  if var == 'mask':
    mask = value
  else:
    value = int(value)
    address, = parse('mem[{:d}]', var)
    for address in apply_mask(mask, var):
      mem[address] = value

print(sum(mem.values()))
