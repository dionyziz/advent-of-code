from parse import parse

with open('in.txt') as f:
  lines = f.read().splitlines()

def run(lines):
  visited = set()
  acc, ip = 0, 0
  while ip not in visited:
    visited.add(ip)
    if ip >= len(lines):
      return acc
    if ip < 0:
      break
    opcode, val = parse('{:w} {:d}', lines[ip])
    if opcode == 'acc':
      acc += val
    elif opcode == 'jmp':
      ip += val
      continue
    ip += 1
  return None

for i, line in enumerate(lines):
  opcode, val = line.split(' ')
  if opcode == 'jmp':
    lines[i] = 'nop ' + val
  elif opcode == 'nop':
    lines[i] = 'jmp ' + val
  else:
    continue
  acc = run(lines)
  if acc is not None:
    print(acc)
    break
  lines[i] = line
