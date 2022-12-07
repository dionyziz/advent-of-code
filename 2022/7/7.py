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

print(sum([size for size in sizes.values() if size <= 100000]))
