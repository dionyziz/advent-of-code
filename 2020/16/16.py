from parse import parse
from functools import partial

with open('in.txt') as f:
  rules, your, other = f.read().split('\n\n')

def match(a_lo, a_hi, b_lo, b_hi, ticket):
  return a_lo <= ticket <= a_hi\
      or b_lo <= ticket <= b_hi

rules = rules.splitlines()
evalrule = {}
for rule in rules:
  fieldname, ranges = rule.split(': ')
  a_lo, a_hi, b_lo, b_hi = parse('{:d}-{:d} or {:d}-{:d}', ranges)
  evalrule[fieldname] = partial(match, a_lo, a_hi, b_lo, b_hi)

other = other.splitlines()[1:]
other = list(map(lambda x: list(map(int, x.split(','))), other))

cnt = 0
for ticket in other:
  for value in ticket:
    if not any(rule(value) for rule in evalrule.values()):
      cnt += value
print(cnt)
