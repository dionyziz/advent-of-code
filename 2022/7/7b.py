from collections import defaultdict

with open('in.txt') as f:
  executions = f.read().strip().split('$ ')

tree = {}
pwd = []

for execution in executions[1:]:
  command, *output = execution.splitlines()
  program, *args = command.split(' ')
  if program == 'ls':
    for line in output:
      size, name = line.split(' ')
      if size != 'dir':
        tree[tuple(pwd) + (name,)] = int(size)
  else: # program == 'cd'
    if args[0] == '..':
      pwd.pop()
    else:
      pwd.append(args[0])

sizes = defaultdict(int)
for path, size in tree.items():
  pwd = []
  for dir in path:
    sizes[tuple(pwd)] += size
    pwd.append(dir)

total = 70000000
needed = 30000000
taken = sizes[()]

for size in sorted(sizes.values()):
  if total - (taken - size) >= needed:
    print(size)
    break
