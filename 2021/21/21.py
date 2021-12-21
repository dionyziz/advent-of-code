p = [5, 8]
s = [0, 0]
mover = False

cnt = 0
def roll():
  global cnt
  cnt += 1
  return (cnt - 1) % 100 + 1

while s[0] < 1000 and s[1] < 1000:
  move = roll() + roll() + roll()
  p[mover] = (p[mover] - 1 + move) % 10 + 1
  s[mover] += p[mover]
  mover = not mover

loser = s[0] >= 1000
print(cnt * s[loser])
