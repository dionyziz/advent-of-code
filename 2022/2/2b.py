with open('in.txt') as f:
  games = [line.split(' ') for line in f.read().splitlines()]

score = 0
for other, result in games:
  other = ord(other) - ord('A')
  result = ord(result) - ord('X')
  score += result * 3 + (result + other - 1) % 3 + 1
print(score)
