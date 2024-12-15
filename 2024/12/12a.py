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
        if board[z] == board[z + dz]:
          frontier.append(z + dz)

  return visited

def perimeter(region):
  perimeter = 0
  for z in region:
    for dz in 1, 1j, -1, -1j:
      if z + dz not in region:
        perimeter += 1
  return perimeter

regions = []
marked = set()
for z in board:
  if z not in marked:
    region = visit(z)
    regions.append(region)
    marked |= region

cost = sum(perimeter(region) * len(region) for region in regions)
print(cost)