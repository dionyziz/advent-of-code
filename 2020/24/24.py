from collections import defaultdict, Counter

with open('input.txt') as f:
  lines = f.read().splitlines()

deltas = {
  'w': (0, -2),
  'e': (0, 2),
  'nw': (-1, -1),
  'se': (1, 1),
  'ne': (-1, 1),
  'sw': (1, -1)
}

def pos(tile):
  i = 0
  row, col = 0, 0
  while i < len(tile):
    try:
      delta = deltas[tile[i]]
    except:
      delta = deltas[tile[i:i + 2]]
      i += 1
    row += delta[0]
    col += delta[1]
    i += 1
  return row, col

def evolve(floor):
  cnt_neighbours = Counter()

  for pos, cell in floor.items():
    cnt_neighbours[pos] += 0
    if cell:
      for dy, dx in deltas.values():
        neighbour = pos[0] + dy, pos[1] + dx
        cnt_neighbours[neighbour] += 1

  new_floor = floor.copy()
  for pos, cnt in cnt_neighbours.items():
    if floor[pos] and cnt == 0 or cnt > 2:
      new_floor[pos] = False
    if not floor[pos] and cnt == 2:
      new_floor[pos] = True

  return new_floor

floor = defaultdict(bool)
for tile in lines:
  position = pos(tile)
  floor[position] = not floor[position]

print(list(floor.values()).count(True))
DAYS = 100
for _ in range(DAYS):
  floor = evolve(floor)
print(list(floor.values()).count(True))
