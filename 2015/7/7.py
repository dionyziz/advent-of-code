from operator import and_, or_, lshift, rshift, inv
from functools import cache
import re

ops = {
  r'(\w+) AND (\w+)': and_,
  r'(\w+) OR (\w+)': or_,
  r'(\w+) LSHIFT (\d+)': lshift,
  r'(\w+) RSHIFT (\d+)': rshift,
  r'NOT (\w+)': inv,
  r'(\w+|\d+)': lambda x: x
}
gates = {}
with open('in.txt') as f:
  for line in f:
    lhs, rhs = line.strip().split(' -> ')
    for regex, op in ops.items():
      match = re.match(regex, lhs)
      if match:
        gates[rhs] = (match.groups(), op)
        break
    else:
      raise ValueError(f'Unknown operation: {line}')

@cache
def evaluate(wire):
  dependencies, op = gates[wire]
  operands = []
  for operand in dependencies:
    if operand.isnumeric():
      operands.append(int(operand))
    else:
      operands.append(evaluate(operand))
  return op(*operands)

a = evaluate('a')
print('Part 1:', a)

evaluate.cache_clear()
gates['b'] = ((str(a),), lambda x: x)
print('Part 2:', evaluate('a'))