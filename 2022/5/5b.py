from collections import defaultdict

with open('in.txt') as f:
  arrangement, moves = f.read().split('\n\n')

piles = defaultdict(list)
for boxes in arrangement.split('\n')[::-1][1:]:
  for i, c in enumerate(boxes[1::4]):
    if c != ' ':
      piles[i + 1].append(c)

for move in moves.strip().split('\n'):
  _, cnt, _, src, _, dst = move.split()
  cnt, src, dst = int(cnt), int(src), int(dst)
  piles[dst].extend(piles[src][-cnt:])
  piles[src] = piles[src][:-cnt]

ans = ''
for pile in piles.values():
  ans += pile[-1]
print(ans)
