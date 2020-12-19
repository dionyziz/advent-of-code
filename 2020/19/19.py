from lark import Lark
import re

with open('in.txt') as f:
  grammar, inputs = f.read().split('\n\n')

lgrammar = []
for line in grammar.splitlines():
  line = re.sub(r"(\d+)", r"s\1", line)
  lgrammar.append(line)
lgrammar.append('start: s0')
lgrammar = '\n'.join(lgrammar)

l = Lark(lgrammar)
cnt = 0
for input in inputs.splitlines():
  try:
    l.parse(input)
    cnt += 1
  except:
    pass

print(cnt)
