from lark import Lark
import re

with open('in.txt') as f:
  rules, inputs = f.read().split('\n\n')

grammar = ['start: s0']
for line in rules.splitlines():
  grammar.append(re.sub(r'(\d+)', r's\1', line))
grammar = '\n'.join(grammar)

l = Lark(grammar)
cnt = 0
for input in inputs.splitlines():
  try:
    l.parse(input)
    cnt += 1
  except:
    pass

print(cnt)
