with open('in.txt') as f:
  s = f.read().strip()

files = []
space = []

id = 0
pos = 0
for c in s:
  if id % 2 == 0:
    files.append([id // 2, pos, int(c)])
  else:
    space.append([pos, int(c)])
  pos += int(c)
  id += 1

files = files[::-1]
for file in files:
  id, file_pos, file_size = file
  for i, (space_pos, space_size) in enumerate(space):
    if file_size <= space_size and space_pos < file_pos:
      space[i] = [space_pos + file_size, space_size - file_size]
      file[1] = space_pos
      break

check = 0
for id, file_pos, file_size in files:
  for i in range(file_size):
    check += (file_pos + i) * id
print(check)
