from parse import parse

with open('in.txt') as f:
  lines = f.read().splitlines()

visited = set()
acc, ip = 0, 0
while ip not in visited:
  visited.add(ip)
  opcode, val = parse('{:w} {:d}', lines[ip])
  if opcode == 'acc':
    acc += val
  elif opcode == 'jmp':
    ip += val
    continue
  ip += 1
print(acc)
