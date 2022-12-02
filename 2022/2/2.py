with open('in.txt') as f:
  games = [line.split(' ') for line in f.read().splitlines()]

score = 0
for other, me in games:
  other = ord(other) - ord('A')
  me = ord(me) - ord('X')
  score += 3 * ((me - other + 1) % 3) + me + 1
print(score)
