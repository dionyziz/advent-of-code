with open('in.txt') as f:
  hex_packets = f.read().strip()
packets = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hex_packets])

def parse(packets):
  def consume(n):
    nonlocal packets
    data, packets = packets[:n], packets[n:]
    return data
  version = int(consume(3), 2)
  T = int(consume(3), 2)
  if T == 4:
    while True:
      literal = consume(5)
      if literal[0] == '0':
        return version, packets
  I = int(consume(1), 2)
  if I == 0:
    L = int(consume(15), 2)
    subpackets = consume(L)
    while subpackets:
      ret_ver, subpackets = parse(subpackets)
      version += ret_ver
  elif I == 1:
    L = int(consume(11), 2)
    for _ in range(L):
      ret_ver, packets = parse(packets)
      version += ret_ver
  return version, packets

print(parse(packets))
