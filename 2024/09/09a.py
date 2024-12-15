with open('in.txt') as f:
  s = f.read().strip()

disk = []
id = 0
for c in s:
  for _ in range(int(c)):
    if id % 2 == 0:
      disk.append(id // 2)
    else:
      disk.append(None)
  id += 1

i = int(s[0])
j = len(disk) - 1

while i < j:
  while disk[i] is not None:
    i += 1
  while disk[j] is None:
    j -= 1
  if i >= j:
    break
  disk[i], disk[j] = disk[j], disk[i]
  i += 1
  j -= 1

disk = disk[:i+1]

print(sum([i * id for i, id in enumerate(disk) if id is not None]))
