with open('in.txt') as f:
  lines = f.read().split('\n\n')

anyone = []
everyone = []
for group in lines:
  people = list(map(set, group.splitlines()))
  anyone.append(len(set.union(*people)))
  everyone.append(len(set.intersection(*people)))

print(sum(anyone))
print(sum(everyone))
