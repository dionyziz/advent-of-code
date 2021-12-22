with open('in.txt') as f:
  lines = f.read().splitlines()

on = set()

for instruction in lines:
  toggle, instruction = instruction.split(' ')
  toggle = toggle == 'on'
  x, y, z = map(lambda x: x.split('=')[1], instruction.split(','))
  minx, maxx = map(int, x.split('..'))
  miny, maxy = map(int, y.split('..'))
  minz, maxz = map(int, z.split('..'))
  if -50 <= minx <= maxx <= 50 and\
     -50 <= miny <= maxy <= 50 and\
     -50 <= minz <= maxz <= 50:
    for x in range(minx, maxx + 1):
      for y in range(miny, maxy + 1):
        for z in range(minz, maxz + 1):
          if toggle:
            on.add((x, y, z))
          else:
            on.discard((x, y, z))

print(len(on))
