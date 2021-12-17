from operator import mul, lt, gt, eq
from functools import reduce, partial

with open('in.txt') as f:
  hex_packets = f.read().strip()
packets = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hex_packets])

def parse(packets):
  def consume(n):
    nonlocal packets
    data, packets = packets[:n], packets[n:]
    return data
  version = int(consume(3), 2)
  type_id = int(consume(3), 2)
  if type_id == 4:
    value = ''
    while True:
      literal = consume(5)
      value += literal[1:]
      if literal[0] == '0':
        break
    value = int(value, 2)
    return value, packets
  length_type_id = int(consume(1), 2)
  values = []
  if length_type_id == 0:
    length = int(consume(15), 2)
    subpackets = consume(length)
    while subpackets:
      value, subpackets = parse(subpackets)
      values.append(value)
  elif length_type_id == 1:
    length = int(consume(11), 2)
    for _ in range(length):
      value, packets = parse(packets)
      values.append(value)
  return [
    sum, partial(reduce, mul), min, max,
    None,
    lambda x: gt(*x),
    lambda x: lt(*x),
    lambda x: eq(*x)
  ][type_id](values), packets

print(parse(packets)[0])
