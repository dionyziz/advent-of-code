from math import ceil
from copy import deepcopy
from itertools import combinations
import json

with open('in.txt') as f:
  lines = f.read().splitlines()

class ASTNode:
  def __init__(self):
    self.parent = None
    self.parent_direction = None

  def replace(self, other):
    if self.parent_direction == 0:
      self.parent.left = other
    else:
      self.parent.right = other

  @classmethod
  def from_list(cls, data):
    if isinstance(data, int):
      return ASTLeaf(data)
    res = ASTInternal(
      ASTNode.from_list(data[0]),
      ASTNode.from_list(data[1])
    )
    res.mark()
    return res

class ASTInternal(ASTNode):
  def __init__(self, left, right):
    super().__init__()
    self.left = left
    self.right = right
    self.level = None

  def get_lefter(self):
    if self.parent is None:
      return None

    if self.parent_direction == 0:
      return self.parent.get_lefter()
    for node in self.parent.left.rtraverse():
      if isinstance(node, ASTLeaf):
        return node

  def get_righter(self):
    if self.parent is None:
      return None

    if self.parent_direction == 1:
      return self.parent.get_righter()
    for node in self.parent.right.traverse():
      if isinstance(node, ASTLeaf):
        return node

  def traverse(self):
    yield self
    yield from self.left.traverse()
    yield from self.right.traverse()

  def rtraverse(self):
    yield from self.right.rtraverse()
    yield from self.left.rtraverse()
    yield self

  def is_pair(self):
    return isinstance(self.left, ASTLeaf) and isinstance(self.right, ASTLeaf)

  def mark(self, level=0):
    self.left.mark(level + 1)
    self.right.mark(level + 1)
    self.level = level
    self.left.parent = self.right.parent = self
    self.left.parent_direction = 0
    self.right.parent_direction = 1

  def magnitude(self):
    return 3 * self.left.magnitude() + 2 * self.right.magnitude()

  def __add__(self, other):
    res = ASTInternal(deepcopy(self), deepcopy(other))
    res.mark()
    while True:
      try:
        res = reduce(res)
      except ValueError:
        break
      res.mark()
    return res

  def __repr__(self):
    return f'({self.left} {self.right})'

class ASTLeaf(ASTNode):
  def __init__(self, value):
    super().__init__()
    self.value = value

  def mark(self, level=0):
    pass

  def magnitude(self):
    return self.value

  def traverse(self):
    yield self

  def rtraverse(self):
    yield self

  def __repr__(self):
    return f'<{str(self.value)}>'

def reduce(tree):
  # explode
  for node in tree.traverse():
    if isinstance(node, ASTLeaf):
      continue
    if node.is_pair() and node.level >= 4:
      node.replace(ASTLeaf(0))
      a = node.get_lefter()
      if a is not None:
        a.value += node.left.value
      b = node.get_righter()
      if b is not None:
        b.value += node.right.value
      return tree

  # split
  for node in tree.traverse():
    if isinstance(node, ASTLeaf) and node.value >= 10:
      node.replace(ASTInternal(
        ASTLeaf(node.value // 2),
        ASTLeaf(ceil(node.value / 2))
      ))
      return tree

  raise ValueError

nums = [ASTNode.from_list(json.loads(line)) for line in lines]
m = -1
for a, b in combinations(nums, 2):
  m = max(m, (a + b).magnitude())

print(m)
