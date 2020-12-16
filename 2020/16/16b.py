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

your = your.splitlines()[1]
your = list(map(int, your.split(',')))
other = other.splitlines()[1:]
other = list(map(lambda x: list(map(int, x.split(','))), other))

good_tickets = []

for ticket in other:
  for value in ticket:
    if not any(rule(value) for rule in evalrule.values()):
      break
  else:
    good_tickets.append(ticket)

fieldsets = [set(evalrule.keys()) for _ in your]

for ticket in good_tickets:
  for ruleset, value in zip(fieldsets, ticket):
    failed = set(name for name, rule in evalrule.items() if not rule(value))
    ruleset -= failed

clear = set()
while True:
  for j, fieldset in enumerate(fieldsets):
    fieldname = list(fieldset)[0]
    if len(fieldset) == 1 and fieldname not in clear:
      for i, otherfieldset in enumerate(fieldsets):
        if i != j:
          otherfieldset.discard(fieldname)
      clear.add(fieldname)
      break
  else:
    break

fields = map(lambda x: x.pop(), fieldsets)

mul = 1
for fieldname, value in zip(fields, your):
  if fieldname.startswith('departure'):
    mul *= value
print(mul)
