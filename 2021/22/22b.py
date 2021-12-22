from copy import copy
from operator import methodcaller
from math import prod

with open('small.txt') as f:
  lines = f.read().splitlines()

class Segment:
  def __init__(self, ends):
    self.ends = ends

  def intersect(self, other):
    return other.ends[0] in self or\
           self.contains_upper_bound(other.ends[1]) or\
           self.ends[0] in other and other.contains_upper_bound(self.ends[1])

  def __contains__(self, point):
    return self.ends[0] <= point < self.ends[1]

  def contains_upper_bound(self, point):
    return self.ends[0] < point <= self.ends[1]

  def size(self):
    return self.ends[1] - self.ends[0]

  def __repr__(self):
    return str(self.ends)

class Rect:
  def __init__(self, seg):
    self.seg = seg

  def within(self, other):
    for me, you in zip(self.seg, other.seg):
      if me.ends[0] not in you or\
         not you.contains_upper_bound(me.ends[1]):
        return False
    return True

  def intersect(self, other):
    for me, you in zip(self.seg, other.seg):
      if not me.intersect(you):
        return False
    return True

  def size(self):
    return prod(seg.size() for seg in self.seg)

  def split(self, dim, point):
    if point in self.seg[dim]:
      seg1 = copy(self.seg)
      seg1[dim] = Segment([seg1[dim].ends[0], point])
      seg2 = copy(self.seg)
      seg2[dim] = Segment([point, seg2[dim].ends[1]])
      return set([Rect(seg1), Rect(seg2)])
    return set([self])

  def __repr__(self):
    return str(self.seg)

  def __eq__(self, other):
    return str(self) == str(other)

  def __hash__(self):
    return hash(self.__repr__())

rects = set()
for instruction in lines:
  toggle, instruction = instruction.split(' ')
  toggle = toggle == 'on'
  minmaxs = [x.split('=')[1] for x in instruction.split(',')]
  segs = []
  for minmax in minmaxs:
    ends = list(map(int, minmax.split('..')))
    ends[1] += 1
    segs.append(Segment(ends))
  this = Rect(segs)

  new_rects = set()
  for other in rects:
    if other.intersect(this):
      children = set([other])

      for dim, seg in enumerate(segs):
        for point in seg.ends:
          new_children = set()
          for child in children:
            new_children |= child.split(dim, point)
          children = new_children
      new_rects |= children
    else:
      new_rects.add(other)

  rects = set([rect for rect in new_rects if not rect.within(this)])
  if toggle:
    rects.add(this)

print(sum(map(methodcaller('size'), rects)))
