from collections import Counter, defaultdict

with open('in.txt') as f:
  tiles = list(filter(lambda x: x != '', f.read().split('\n\n')))

class Tile:
  def __init__(self, id, tile):
    self.id = id
    self.borders = [
      tuple(tile[0]),
      tuple(tuple(zip(*tile))[-1]),
      tuple(tile[-1]),
      tuple(tuple(zip(*tile))[0])
    ]
    self.neighbours = 4 * [None]
    self.position = None

    assert Counter(self.borders + list(map(lambda x: x[::-1], self.borders))).most_common(1)[0][1] == 1

  def vflip(self):
    self.borders[0], self.borders[2] = self.borders[2], self.borders[0]
    self.borders[1] = self.borders[1][::-1]
    self.borders[3] = self.borders[3][::-1]

  def hflip(self):
    self.borders[1], self.borders[3] = self.borders[3], self.borders[1]
    self.borders[0] = self.borders[0][::-1]
    self.borders[2] = self.borders[2][::-1]

  def rotate(self):
    self.borders[0], self.borders[1], self.borders[2], self.borders[3] =\
      self.borders[3], self.borders[0], self.borders[1], self.borders[2]
    self.borders[2] = self.borders[2][::-1]
    self.borders[0] = self.borders[0][::-1]

  def transform(self):
    for hflip in 0, 1:
      if hflip:
        self.hflip()
      for vflip in 0, 1:
        if vflip:
          self.vflip()
        for _ in range(4):
          self.rotate()
          yield self
        if vflip:
          self.vflip()
      if hflip:
        self.hflip()

  def satisfies(self, constraint):
    side, border = constraint
    return self.borders[side] == border

bordermap = defaultdict(set)
all_tiles = []
for tile in tiles:
  tile = tile.splitlines()
  id = int(tile[0].split(' ')[1][:-1])
  tile = list(map(list, tile[1:]))
  tile = Tile(id, tile)
  all_tiles.append(tile)
  for _ in tile.transform():
    for border in tile.borders:
      bordermap[border].add(tile)

singletonscount = Counter()

for border, tileset in bordermap.items():
  if len(tileset) == 1:
    singletonscount[list(tileset)[0].id] += 1

corners = singletonscount.most_common(4)
mul = 1
for corner, _ in corners:
  mul *= corner
print(mul)
