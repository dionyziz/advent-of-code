from itertools import permutations

with open('in.txt') as f:
  data = [list(line.strip()) for line in f]

board = {}
for y, line in enumerate(data):
  for x, c in enumerate(line):
    board[x + y * 1j] = c

def visit(z):
  visited = set()
  frontier = [z]

  while frontier:
    z = frontier.pop()
    if z in visited:
      continue
    visited.add(z)

    for dz in 1, 1j, -1, -1j:
      if z + dz in board:
        if board[z + dz] == board[z]:
          frontier.append(z + dz)

  return visited

def perimeter(region):
  sides = set()
  for z in region:
    for dz in 1j, -1j, 1, -1:
      if z + dz not in region:
        sides.add((z, z + dz * 1j, dz))

  while True:
    for a, b in permutations(sides, 2):
      if a[1] == b[0] and a[2] == b[2]:
        c = (a[0], b[1], a[2])
        sides.remove(a)
        sides.remove(b)
        sides.add(c)
        break
    else:
      break
  return len(sides)

regions = []
marked = set()
for z in board:
  if z not in marked:
    region = visit(z)
    regions.append(region)
    marked |= region

cost = sum(perimeter(region) * len(region) for region in regions)
print(cost)