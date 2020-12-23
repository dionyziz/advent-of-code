from sortedcontainers import SortedSet

MAX_CUP = 1000000
MAX_MOVES = 10000000
INPUT = '586439172'

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def insert_after(self, node):
    node.next = self.next
    self.next.prev = node
    self.next = node
    node.prev = self

  def remove(self):
    self.prev.next, self.next.prev = self.next, self.prev

state = list(map(int, INPUT))

prev = None
begin = None
node = None
node_by_value = {}

for num in state + list(range(max(state) + 1, MAX_CUP + 1)):
  node = Node(num)
  if prev is None:
    begin = node
  else:
    prev.next = node
    node.prev = prev
  prev = node
  node_by_value[num] = node

node.next = begin
begin.prev = node

cur = begin
cups = SortedSet(node_by_value.keys())

for i in range(MAX_MOVES):
  next = cur.next
  x = next
  next.remove()
  next = next.next
  y = next
  next.remove()
  next = next.next
  z = next
  next.remove()

  cups.remove(x.value)
  cups.remove(y.value)
  cups.remove(z.value)

  dest = cur.value - 1
  minimum = cups[0]
  maximum = cups[-1]

  if dest < minimum:
    dest = maximum
  while dest in (x.value, y.value, z.value):
    dest -= 1
    if dest < minimum:
      dest = maximum

  dest_it = node_by_value[dest]
  dest_it.insert_after(x)
  x.insert_after(y)
  y.insert_after(z)

  cups.add(x.value)
  cups.add(y.value)
  cups.add(z.value)

  cur = cur.next

print(node_by_value[1].next.value * node_by_value[1].next.next.value)
