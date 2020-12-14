from parse import parse
from collections import defaultdict

with open('in.txt') as f:
  lines = f.read().splitlines()

def apply_mask(mask, value):
  value |= int(mask.replace('X', '0'), 2)
  value &= int(mask.replace('X', '1'), 2)
  return value

mask = 0
mem = defaultdict(int)
for line in lines:
  var, value = line.split(' = ')
  if var == 'mask':
    mask = value
  else:
    value = int(value)
    address, = parse('mem[{:d}]', var)
    value = apply_mask(mask, value)
    mem[address] = value

print(sum(mem.values()))
